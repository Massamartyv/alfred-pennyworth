# Fountain Christian Center — DNS cutover

Vercel side is fully configured. DNS change at Register.com is the final cutover step.

## Current state (as of 2026-05-07)

- Domain: `fountainchristiancenter.com` (`.com`, not `.org` — handoff had wrong TLD)
- Registrar: Register.com
- Nameservers: `dns1.register.com`, `dns2.register.com` (DNS managed at Register.com)
- Currently serving: existing Weebly site at IP `199.34.228.181`
- Vercel project: `studio-fivepoints/fountain-christian-center` (project ID `prj_pkAULKrQvw2IXjYjdFdCPQFAuVHm`, team `team_WYO4svCJKeaeKO6f00PpUg2y`)
- Apex attached to Vercel project — ownership verified
- `www` attached to Vercel project — 308 redirect to apex set
- Latest production deploy: `fountain-christian-center-mu.vercel.app`

## DNS records to add at Register.com

Remove existing A records pointing at `199.34.228.181` (apex and www), then add:

| Type | Host | Value | TTL |
|---|---|---|---|
| A | `@` | `216.198.79.1` | 1 hour |
| A | `@` | `64.29.17.1` | 1 hour |
| CNAME | `www` | `cname.vercel-dns.com.` | 1 hour |

Notes:
- Vercel issues a longer per-domain CNAME (`de604294b6ad9de7.vercel-dns-017.com.`) which is rank-1 recommended. If Register.com's DNS panel accepts it, use that. Otherwise fall back to `cname.vercel-dns.com` — works identically.
- Two A records on the apex give Vercel redundancy.
- TTL 1 hour is fine for the cutover. Lower it (5–15 minutes) the day before if you want faster propagation, then raise back to 1 hour after cutover settles.

## Pre-cutover checklist

Hold the DNS change until all of these are done:

- [ ] Bishop Watts memorial portrait in place at `/public/images/legacy/bishop-watts-memorial.jpg`
- [ ] `HAS_PORTRAIT` flipped to `true` in `src/app/in-memoriam/bishop-watts/page.tsx`
- [ ] Sunrise / Sunset dates filled in on the memorial page
- [ ] LegacyLeaders updated to render Bishop Watts' portrait
- [ ] Image walkthrough complete (or paused at a state we are happy to ship)
- [ ] Vercel GitHub auto-deploy connected (so post-cutover updates ship on push)
- [ ] `RESEND_API_KEY` set in Vercel production
- [ ] Resend domain verification complete for `fountainchristiancenter.com`
- [ ] Final production deploy from `main`, smoke-tested at the Vercel URL

## Cutover sequence

1. Final production deploy. Confirm the Vercel URL renders cleanly.
2. Lower TTL on existing Weebly A records to 300 seconds, wait one cycle.
3. Replace records at Register.com per the table above.
4. Watch propagation: `dig +short fountainchristiancenter.com A`.
5. Once propagated, confirm `https://fountainchristiancenter.com` serves the new site, `https://www.fountainchristiancenter.com` 308-redirects to apex, contact form submits successfully.
6. Cancel the Weebly subscription once the new site has been live and stable for a few days.

## Post-cutover

- Verify SSL certificate provisioned automatically by Vercel (Let's Encrypt). Should be near-instant once DNS resolves.
- Confirm `fountain-christian-center-mu.vercel.app` still resolves as a Vercel-side alias for emergency rollback.
- Check Google Search Console for the apex once propagated; submit sitemap.
