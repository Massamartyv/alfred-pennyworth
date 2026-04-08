---
file_type: sop
sop_id: OPS-005
venture: Five Points Digital Studio
status: active
last_updated: 2026-04-06
---

# Project Handoff

Standard procedure for transferring a completed client project from Five Points infrastructure to the client's own accounts.

---

## Trigger

Client engagement complete, or client requests ownership transfer of their web project.

---

## Prerequisites

- Client has their own Vercel account (or creates one)
- Client has their own Supabase organisation (or creates one)
- Client has their own GitHub account (if repo transfer is included)
- All credentials are stored in Vercel environment variables, never hardcoded in source

---

## Build Standards (enforce during development)

These standards must be followed during every client build to ensure a clean handoff:

1. **Supabase credentials in env vars only.** `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY` live exclusively in Vercel environment variables. Never in source code.
2. **No Five Points-specific secrets in client code.** Stripe keys, API tokens, third-party credentials -- all in Vercel env vars.
3. **Domain DNS pointed at Vercel.** Custom domains should use Vercel's DNS records so the transfer does not require DNS changes.
4. **Git repo is self-contained.** No dependencies on Five Points internal repos or private packages.

---

## Handoff Sequence

### Step 1: Transfer Supabase project

1. Open the Five Points Supabase dashboard
2. Navigate to the client project > Settings > General > Transfer Project
3. Enter the client's Supabase organisation ID
4. Client accepts the transfer in their dashboard
5. **Record the new project URL and anon key** -- these change on transfer

### Step 2: Transfer GitHub repository (if included)

1. Go to the repo on `studio-fivepoints` > Settings > General > Transfer
2. Enter the client's GitHub username or organisation
3. Client accepts the transfer

### Step 3: Transfer Vercel project

1. Open the Five Points Vercel dashboard
2. Navigate to the client project > Settings > General > Transfer
3. Select the client's Vercel team as the destination
4. Client accepts the transfer

### Step 4: Update environment variables

1. In the client's Vercel dashboard (or assist them), update:
   - `NEXT_PUBLIC_SUPABASE_URL` -- new URL from Step 1
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY` -- new key from Step 1
   - `SUPABASE_SERVICE_ROLE_KEY` -- if used, new key from Step 1
2. Trigger a redeployment

### Step 5: Verify

1. Confirm the production site loads correctly
2. Test auth flows (sign up, sign in, password reset)
3. Test any database-dependent features
4. Confirm custom domain resolves properly

---

## Decision Points

| Situation | Action |
|---|---|
| Client does not have Vercel/Supabase accounts | Walk them through account creation before beginning |
| Client wants to keep the site on Five Points infrastructure | Switch to a hosting retainer agreement instead of transfer |
| Client wants the repo but not the infrastructure | Transfer GitHub only, keep Vercel/Supabase under a maintenance agreement |
| Transfer fails or project URL does not update | Contact Supabase/Vercel support -- transfers are account-level operations |

---

## Estimated Duration

Five minutes for the transfers. Ten minutes including verification. The entire operation is a config swap, not a rebuild.

---

## After the Handoff

1. Update the client's entry in `_clients-registry.md` -- status to Archived or Completed
2. Move the client folder from `Clientele/Active/` to `Clientele/Archived/`
3. Remove any Five Points-specific access tokens or secrets that referenced the project
4. Send the client a summary of what was transferred and any credentials they need to store
