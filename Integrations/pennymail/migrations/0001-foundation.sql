-- Pennymail 0001 – foundation
--
-- Creates the `pm` schema: tenants, providers, sending identities, contacts,
-- consent, lists, suppressions, templates, campaigns, sequences, messages and
-- events. Enables row-level security on every tenant-scoped table.
--
-- Design notes that are not obvious from the DDL:
--
--   Lane locking. `sending_identities` carries a unique key on (id, lane).
--   Campaigns, sequences and messages reference it as a composite foreign key,
--   so a marketing campaign cannot be dispatched from a cold-lane identity.
--   The constraint is structural, not a convention.
--
--   Burner isolation. A cold-lane identity must be flagged `is_burner`, and a
--   burner may not serve any other lane. Bidirectional, enforced by CHECK.
--
--   Email normalisation. Addresses are stored lowercased and a CHECK enforces
--   it, rather than depending on the citext extension being on the search path.
--
--   Events are append-only. A trigger rejects UPDATE and DELETE.
--
--   No personal data in tracking URLs. `messages.tracking_token` is an opaque
--   random value; `events.ip_hash` is salted and hashed at the edge.

begin;

create schema if not exists pm;

-- ---------------------------------------------------------------------------
-- Enumerations
-- ---------------------------------------------------------------------------

create type pm.lane as enum ('transactional', 'marketing', 'cold');

create type pm.tenant_kind as enum ('personal', 'venture', 'client');

create type pm.consent_status as enum (
  'subscribed', 'pending', 'unsubscribed', 'bounced', 'complained', 'suppressed'
);

create type pm.consent_basis as enum (
  'double_opt_in', 'single_opt_in', 'purchase', 'event_attendance',
  'existing_relationship', 'import', 'clay_prospecting'
);

create type pm.list_kind as enum ('static', 'dynamic');

create type pm.campaign_status as enum (
  'draft', 'scheduled', 'sending', 'paused', 'sent', 'cancelled', 'failed'
);

create type pm.message_status as enum (
  'queued', 'sent', 'delivered', 'bounced', 'complained', 'failed', 'skipped'
);

create type pm.event_type as enum (
  'queued', 'sent', 'delivered', 'open', 'click', 'bounce_hard', 'bounce_soft',
  'complaint', 'unsubscribe', 'reply', 'failed'
);

create type pm.suppression_scope as enum ('global', 'tenant', 'lane');

create type pm.suppression_reason as enum (
  'unsubscribe', 'bounce_hard', 'complaint', 'manual', 'role_address',
  'competitor', 'legal_request'
);

create type pm.enrollment_status as enum (
  'active', 'paused', 'completed', 'stopped_replied',
  'stopped_unsubscribed', 'stopped_bounced'
);

-- ---------------------------------------------------------------------------
-- Shared helpers
-- ---------------------------------------------------------------------------

create or replace function pm.set_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at := now();
  return new;
end;
$$;

create or replace function pm.current_tenant_id()
returns uuid
language sql
stable
as $$
  select nullif(current_setting('app.tenant_id', true), '')::uuid;
$$;

-- ---------------------------------------------------------------------------
-- Tenants and providers
-- ---------------------------------------------------------------------------

create table pm.tenants (
  id          uuid primary key default gen_random_uuid(),
  slug        text not null unique,
  name        text not null,
  kind        pm.tenant_kind not null,
  active      boolean not null default true,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now(),
  constraint tenant_slug_shape check (slug ~ '^[a-z][a-z0-9_]*$')
);

comment on table pm.tenants is
  'One row per pipeline. Single-tenant in practice, multi-tenant in structure.';

create table pm.providers (
  id                  uuid primary key default gen_random_uuid(),
  slug                text not null unique,
  display_name        text not null,
  credential_env_var  text not null,
  config              jsonb not null default '{}'::jsonb,
  active              boolean not null default true,
  created_at          timestamptz not null default now(),
  updated_at          timestamptz not null default now(),
  constraint provider_slug_shape check (slug ~ '^[a-z][a-z0-9_]*$')
);

comment on column pm.providers.credential_env_var is
  'Name of the variable in .env. The secret itself never enters this table.';

-- ---------------------------------------------------------------------------
-- Sending identities
-- ---------------------------------------------------------------------------

create table pm.sending_identities (
  id                     uuid primary key default gen_random_uuid(),
  tenant_id              uuid not null references pm.tenants (id) on delete cascade,
  lane                   pm.lane not null,
  provider_id            uuid not null references pm.providers (id) on delete restrict,
  domain                 text not null,
  from_email             text not null,
  from_name              text not null,
  reply_to               text,
  is_burner              boolean not null default false,
  provider_identity_ref  text,
  dkim_verified          boolean not null default false,
  spf_verified           boolean not null default false,
  dmarc_policy           text,
  daily_cap              integer,
  verified_at            timestamptz,
  active                 boolean not null default true,
  created_at             timestamptz not null default now(),
  updated_at             timestamptz not null default now(),

  -- Cold lane requires a burner domain; a burner serves no other lane.
  constraint cold_lane_requires_burner check ((lane = 'cold') = is_burner),
  constraint from_email_lowercase check (from_email = lower(from_email)),
  constraint reply_to_lowercase check (reply_to is null or reply_to = lower(reply_to)),
  constraint domain_lowercase check (domain = lower(domain)),
  constraint daily_cap_positive check (daily_cap is null or daily_cap > 0),

  -- Target of the composite foreign keys that lock lane end to end.
  unique (id, lane),
  unique (tenant_id, lane, from_email)
);

comment on constraint cold_lane_requires_burner on pm.sending_identities is
  'Brand domains never send cold outbound; burner domains never send anything else.';

-- ---------------------------------------------------------------------------
-- Contacts and consent
-- ---------------------------------------------------------------------------

create table pm.contacts (
  id              uuid primary key default gen_random_uuid(),
  tenant_id       uuid not null references pm.tenants (id) on delete cascade,
  email           text not null,
  first_name      text,
  last_name       text,
  company         text,
  title           text,
  phone           text,
  timezone        text,
  attributes      jsonb not null default '{}'::jsonb,
  source          text not null,
  source_ref      text,
  clay_record_id  text,
  created_at      timestamptz not null default now(),
  updated_at      timestamptz not null default now(),

  constraint contact_email_lowercase check (email = lower(email)),
  constraint contact_email_shape check (email ~ '^[^@[:space:]]+@[^@[:space:]]+\.[^@[:space:]]+$'),
  unique (tenant_id, email)
);

comment on column pm.contacts.attributes is
  'Clay enrichment lands here. Merge fields resolve against it at render time.';

create table pm.consent (
  id          uuid primary key default gen_random_uuid(),
  tenant_id   uuid not null references pm.tenants (id) on delete cascade,
  contact_id  uuid not null references pm.contacts (id) on delete cascade,
  lane        pm.lane not null,
  status      pm.consent_status not null,
  basis       pm.consent_basis not null,
  evidence    jsonb not null default '{}'::jsonb,
  granted_at  timestamptz,
  revoked_at  timestamptz,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now(),

  unique (contact_id, lane)
);

comment on table pm.consent is
  'Provenance, not a flag. An import and a double opt-in are different records.';

comment on column pm.consent.evidence is
  'Form URL, submission timestamp, hashed IP, Clay table reference. Audit trail.';

-- ---------------------------------------------------------------------------
-- Lists
-- ---------------------------------------------------------------------------

create table pm.lists (
  id          uuid primary key default gen_random_uuid(),
  tenant_id   uuid not null references pm.tenants (id) on delete cascade,
  slug        text not null,
  name        text not null,
  description text,
  lane        pm.lane not null,
  kind        pm.list_kind not null default 'static',
  definition  jsonb not null default '{}'::jsonb,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now(),

  unique (tenant_id, slug),
  constraint dynamic_list_needs_definition
    check (kind = 'static' or definition <> '{}'::jsonb)
);

comment on column pm.lists.definition is
  'Filter expression for dynamic lists. Empty for static lists.';

create table pm.list_members (
  id          uuid primary key default gen_random_uuid(),
  tenant_id   uuid not null references pm.tenants (id) on delete cascade,
  list_id     uuid not null references pm.lists (id) on delete cascade,
  contact_id  uuid not null references pm.contacts (id) on delete cascade,
  added_at    timestamptz not null default now(),
  added_by    text,
  removed_at  timestamptz
);

-- A contact holds at most one live membership per list; history is retained.
create unique index list_members_live_uniq
  on pm.list_members (list_id, contact_id)
  where removed_at is null;

-- ---------------------------------------------------------------------------
-- Suppressions – these outrank list membership and campaign configuration
-- ---------------------------------------------------------------------------

create table pm.suppressions (
  id          uuid primary key default gen_random_uuid(),
  tenant_id   uuid references pm.tenants (id) on delete cascade,
  email       text not null,
  scope       pm.suppression_scope not null,
  lane        pm.lane,
  reason      pm.suppression_reason not null,
  note        text,
  created_at  timestamptz not null default now(),
  expires_at  timestamptz,

  constraint suppression_email_lowercase check (email = lower(email)),
  constraint global_scope_has_no_tenant check ((scope = 'global') = (tenant_id is null)),
  constraint lane_scope_has_lane check ((scope = 'lane') = (lane is not null))
);

create index suppressions_lookup on pm.suppressions (email, scope);

create or replace function pm.is_suppressed(
  p_tenant uuid,
  p_email  text,
  p_lane   pm.lane
)
returns boolean
language sql
stable
as $$
  select exists (
    select 1
    from pm.suppressions s
    where s.email = lower(p_email)
      and (s.expires_at is null or s.expires_at > now())
      and (
        s.scope = 'global'
        or (s.scope = 'tenant' and s.tenant_id = p_tenant)
        or (s.scope = 'lane' and s.tenant_id = p_tenant and s.lane = p_lane)
      )
  );
$$;

comment on function pm.is_suppressed is
  'Send-time hard stop. Called by the dispatch worker before every message.';

-- ---------------------------------------------------------------------------
-- Templates
-- ---------------------------------------------------------------------------

create table pm.templates (
  id            uuid primary key default gen_random_uuid(),
  tenant_id     uuid not null references pm.tenants (id) on delete cascade,
  slug          text not null,
  name          text not null,
  subject       text not null,
  preheader     text,
  html_body     text not null,
  text_body     text not null,
  brand_tokens  jsonb not null default '{}'::jsonb,
  version       integer not null default 1,
  created_at    timestamptz not null default now(),
  updated_at    timestamptz not null default now(),

  unique (tenant_id, slug, version)
);

comment on column pm.templates.text_body is
  'Required, not optional. A missing plain-text part is a spam signal.';

-- ---------------------------------------------------------------------------
-- Campaigns
-- ---------------------------------------------------------------------------

create table pm.campaigns (
  id                   uuid primary key default gen_random_uuid(),
  tenant_id            uuid not null references pm.tenants (id) on delete cascade,
  slug                 text not null,
  name                 text not null,
  lane                 pm.lane not null,
  template_id          uuid not null references pm.templates (id) on delete restrict,
  sending_identity_id  uuid not null,
  list_id              uuid references pm.lists (id) on delete restrict,
  status               pm.campaign_status not null default 'draft',
  scheduled_at         timestamptz,
  started_at           timestamptz,
  completed_at         timestamptz,
  notion_page_id       text,
  created_by           text,
  created_at           timestamptz not null default now(),
  updated_at           timestamptz not null default now(),

  unique (tenant_id, slug),

  -- Lane lock: the identity must serve this campaign's lane.
  foreign key (sending_identity_id, lane)
    references pm.sending_identities (id, lane) on delete restrict,

  constraint scheduled_needs_time
    check (status <> 'scheduled' or scheduled_at is not null)
);

-- ---------------------------------------------------------------------------
-- Sequences – multi-step, used by cold outbound and nurture
-- ---------------------------------------------------------------------------

create table pm.sequences (
  id                   uuid primary key default gen_random_uuid(),
  tenant_id            uuid not null references pm.tenants (id) on delete cascade,
  slug                 text not null,
  name                 text not null,
  lane                 pm.lane not null,
  sending_identity_id  uuid not null,
  stop_on_reply        boolean not null default true,
  active               boolean not null default false,
  created_at           timestamptz not null default now(),
  updated_at           timestamptz not null default now(),

  unique (tenant_id, slug),
  foreign key (sending_identity_id, lane)
    references pm.sending_identities (id, lane) on delete restrict
);

create table pm.sequence_steps (
  id           uuid primary key default gen_random_uuid(),
  tenant_id    uuid not null references pm.tenants (id) on delete cascade,
  sequence_id  uuid not null references pm.sequences (id) on delete cascade,
  position     integer not null,
  template_id  uuid not null references pm.templates (id) on delete restrict,
  delay_hours  integer not null default 0,
  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now(),

  unique (sequence_id, position),
  constraint position_positive check (position > 0),
  constraint delay_not_negative check (delay_hours >= 0)
);

create table pm.enrollments (
  id            uuid primary key default gen_random_uuid(),
  tenant_id     uuid not null references pm.tenants (id) on delete cascade,
  sequence_id   uuid not null references pm.sequences (id) on delete cascade,
  contact_id    uuid not null references pm.contacts (id) on delete cascade,
  current_step  integer not null default 0,
  status        pm.enrollment_status not null default 'active',
  next_send_at  timestamptz,
  enrolled_at   timestamptz not null default now(),
  completed_at  timestamptz,
  updated_at    timestamptz not null default now(),

  unique (sequence_id, contact_id)
);

create index enrollments_due
  on pm.enrollments (next_send_at)
  where status = 'active';

-- ---------------------------------------------------------------------------
-- Messages – one row per email actually dispatched. The spine.
-- ---------------------------------------------------------------------------

create table pm.messages (
  id                   uuid primary key default gen_random_uuid(),
  tenant_id            uuid not null references pm.tenants (id) on delete cascade,
  contact_id           uuid not null references pm.contacts (id) on delete restrict,
  campaign_id          uuid references pm.campaigns (id) on delete set null,
  sequence_step_id     uuid references pm.sequence_steps (id) on delete set null,
  lane                 pm.lane not null,
  sending_identity_id  uuid not null,
  provider_id          uuid not null references pm.providers (id) on delete restrict,
  provider_message_id  text,
  subject              text not null,
  status               pm.message_status not null default 'queued',
  tracking_token       text not null unique,
  queued_at            timestamptz not null default now(),
  sent_at              timestamptz,
  failure_reason       text,

  foreign key (sending_identity_id, lane)
    references pm.sending_identities (id, lane) on delete restrict,

  constraint origin_is_campaign_or_sequence
    check (num_nonnulls(campaign_id, sequence_step_id) = 1),
  constraint tracking_token_opaque
    check (length(tracking_token) >= 22)
);

comment on column pm.messages.tracking_token is
  'Opaque random value. The only identifier that appears in a tracking URL.';

create index messages_dispatch_queue
  on pm.messages (queued_at)
  where status = 'queued';

create index messages_by_campaign on pm.messages (campaign_id);
create index messages_by_contact  on pm.messages (contact_id, queued_at desc);

-- ---------------------------------------------------------------------------
-- Links and events
-- ---------------------------------------------------------------------------

create table pm.links (
  id            uuid primary key default gen_random_uuid(),
  tenant_id     uuid not null references pm.tenants (id) on delete cascade,
  campaign_id   uuid references pm.campaigns (id) on delete cascade,
  template_id   uuid references pm.templates (id) on delete cascade,
  token         text not null unique,
  original_url  text not null,
  created_at    timestamptz not null default now()
);

create table pm.events (
  id           uuid primary key default gen_random_uuid(),
  tenant_id    uuid not null references pm.tenants (id) on delete cascade,
  message_id   uuid not null references pm.messages (id) on delete cascade,
  type         pm.event_type not null,
  occurred_at  timestamptz not null default now(),
  link_id      uuid references pm.links (id) on delete set null,
  user_agent   text,
  ip_hash      text,
  raw          jsonb not null default '{}'::jsonb,

  constraint click_has_link check (type <> 'click' or link_id is not null)
);

comment on column pm.events.ip_hash is
  'Salted hash written at the edge. The raw address is never persisted.';

create index events_by_message on pm.events (message_id, type);
create index events_by_time    on pm.events (tenant_id, occurred_at desc);

-- Append-only.
create or replace function pm.reject_event_mutation()
returns trigger
language plpgsql
as $$
begin
  raise exception 'pm.events is append-only; % is not permitted', tg_op;
end;
$$;

create trigger events_append_only
  before update or delete on pm.events
  for each row execute function pm.reject_event_mutation();

-- ---------------------------------------------------------------------------
-- updated_at triggers
-- ---------------------------------------------------------------------------

do $$
declare
  t text;
begin
  foreach t in array array[
    'tenants', 'providers', 'sending_identities', 'contacts', 'consent',
    'lists', 'templates', 'campaigns', 'sequences', 'sequence_steps',
    'enrollments'
  ]
  loop
    execute format(
      'create trigger %I before update on pm.%I
         for each row execute function pm.set_updated_at()',
      t || '_set_updated_at', t
    );
  end loop;
end;
$$;

-- ---------------------------------------------------------------------------
-- Row-level security
--
-- Enabled from the first migration so tenancy is never retrofitted. The
-- service role used by the edge functions carries BYPASSRLS; anon and
-- authenticated roles see only the tenant named in app.tenant_id.
--
-- FORCE is deliberately not used. Under FORCE the table owner is also subject
-- to the policies, and since pm.current_tenant_id() is null during a migration
-- every seed insert would fail its WITH CHECK. Owner-run migrations and seeds
-- must stay unblocked; the isolation that matters applies to anon and
-- authenticated, which are never table owners.
-- ---------------------------------------------------------------------------

do $$
declare
  t text;
begin
  foreach t in array array[
    'tenants', 'sending_identities', 'contacts', 'consent', 'lists',
    'list_members', 'templates', 'campaigns', 'sequences', 'sequence_steps',
    'enrollments', 'messages', 'links', 'events'
  ]
  loop
    execute format('alter table pm.%I enable row level security', t);
  end loop;

  -- Tenant-scoped tables key off the session setting.
  foreach t in array array[
    'sending_identities', 'contacts', 'consent', 'lists', 'list_members',
    'templates', 'campaigns', 'sequences', 'sequence_steps', 'enrollments',
    'messages', 'links', 'events'
  ]
  loop
    execute format(
      'create policy tenant_isolation on pm.%I
         using (tenant_id = pm.current_tenant_id())
         with check (tenant_id = pm.current_tenant_id())',
      t
    );
  end loop;
end;
$$;

-- The tenants table itself: a session sees only its own row.
create policy tenant_self on pm.tenants
  using (id = pm.current_tenant_id());

-- Suppressions carry nullable tenant_id for global entries, so the policy
-- differs: a session sees its own suppressions plus every global one.
alter table pm.suppressions enable row level security;

create policy suppression_visibility on pm.suppressions
  using (scope = 'global' or tenant_id = pm.current_tenant_id())
  with check (scope = 'global' or tenant_id = pm.current_tenant_id());

-- Providers hold no tenant data and no secrets, only variable names.
alter table pm.providers enable row level security;
create policy providers_readable on pm.providers for select using (true);

commit;
