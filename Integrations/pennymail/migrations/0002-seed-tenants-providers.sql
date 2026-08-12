-- Pennymail 0002 – tenant and provider seed
--
-- Six pipelines, matching Pennyone's routing keys plus Atlas. Two providers,
-- routed per lane: Postmark for transactional, SES for marketing and cold.
--
-- Providers hold the NAME of the credential variable, never the credential.
-- Sending identities are not seeded here – they require real domains, verified
-- DNS and provider-side identity records, which belong to Phases 2, 4 and 6.

begin;

insert into pm.tenants (slug, name, kind) values
  ('personal',           'Personal',                    'personal'),
  ('marty_gras',         'Marty Gras',                  'venture'),
  ('five_points',        'Five Points Digital Studio',  'venture'),
  ('paradigm',           'Paradigm',                    'venture'),
  ('lillie_and_lynette', 'Lillie and Lynette',          'venture'),
  ('atlas',              'Atlas',                       'venture')
on conflict (slug) do nothing;

insert into pm.providers (slug, display_name, credential_env_var, config) values
  (
    'postmark',
    'Postmark',
    'POSTMARK_SERVER_TOKEN',
    jsonb_build_object(
      'lanes',        jsonb_build_array('transactional'),
      'api_base',     'https://api.postmarkapp.com',
      'stream_model', 'message_streams',
      'note',         'Postmark forbids cold outbound and purchased lists. Transactional only.'
    )
  ),
  (
    'ses',
    'Amazon SES',
    'AWS_SES_SECRET_ACCESS_KEY',
    jsonb_build_object(
      'lanes',              jsonb_build_array('marketing', 'cold'),
      'region',             'us-east-1',
      'isolation_model',    'configuration_sets',
      'configuration_sets', jsonb_build_object(
        'marketing', 'pm-marketing',
        'cold',      'pm-cold'
      ),
      'note',               'Separate configuration sets per lane so reputation metrics and event streams never mix.'
    )
  )
on conflict (slug) do nothing;

commit;
