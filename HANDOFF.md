# senexapps.com handoff

Updated 2026-11-13. This file stands on its own; `README.md` has the commands.

## What it is

The marketing site for SENEX, the owner's suite of Mac photo apps: Pictor, a nightscape stacker, and Corvus, a camera-card importer. It is plain HTML and CSS built by a Python-stdlib script and hosted on Cloudflare Pages, with no JavaScript, analytics, cookies or third-party requests.

## Where things stand

- **Live:** https://senexapps.com and https://www.senexapps.com, Cloudflare Pages project `senexapps`, production deployment `c785647e` from 2026-11-10, built from commit `d013475`. Every page matched the build on 2026-11-13.
- **Pages:** Home, Pictor, Corvus, Corvus release notes, Support, Privacy, About and a custom 404.
- **Apps described:** Pictor 0.1.0 preview (2 November 2026, github.com/endthestart/senex-pictor) and Corvus 0.2.0-alpha.1 source preview (5 November 2026, github.com/endthestart/senex-corvus). Both were still the latest releases on 2026-11-13.
- **Repository:** local git at `~/Development/senexapps` on the Mac Pro, `main` only, clean, no remote. Nothing is pushed anywhere, so this is the only copy.
- **Domain:** registered at Cloudflare on 2026-10-30 and expires 2027-10-30. DNS is at Cloudflare, and the apex and www are attached to the Pages project in the dashboard. The TLS certificate from Google Trust Services runs to 2027-01-29, and Cloudflare renews it.
- **Deploy login:** a Wrangler login limited to Pages write plus account and user read, stored on the Mac Pro only. See "Wrangler login" in the README.

## Run, check and deploy

The README has the commands to build and preview, deploy, and log in to Wrangler on another machine. Every deploy needs the owner's yes.

`build.py` fails on a broken internal link. To check that the live site matches a fresh build, run this in sh or bash from the repository:

```sh
python3 build.py
for p in "" pictor/ corvus/ corvus/changelog/ support/ about/ privacy/; do
  curl -s "https://senexapps.com/$p" | cmp -s - "site/${p}index.html" && echo "ok /$p" || echo "DIFFERS /$p"
done
```

## Open items, in priority order

1. **Push the repository.** The owner chose public GitHub, `endthestart/senexapps`, but the repository can't be created or pushed without their own yes. Its history was checked for private data on 2026-11-03 and was clean.
2. **Corvus PR #8** in `endthestart/senex-corvus` fixes its README clone line and changelog date. It waits on the owner's merge, and the site doesn't depend on it.
3. **App releases.** A new Pictor or Corvus release changes its page's meta line and Version row, and a Corvus release also gets an entry on the release notes page. Then build, check and deploy.

## Owner steps pending

- Type in a session working on this repository: "Create a public GitHub repo endthestart/senexapps and push main."
- Merge Corvus PR #8.
- Check that auto-renew is on for senexapps.com in the Cloudflare dashboard before 2027-10-30. It hasn't been verified.

## Decisions already made

- Static HTML and CSS only: no JavaScript, analytics, tracking cookies or third-party requests.
- Cloudflare Pages by direct upload with Wrangler, not a Git-connected build.
- No contact email: Support and About link to GitHub issues.
- Images are generated art or app screenshots of synthetic data, never personal photos.
- The look follows SENEX design tokens v1 from the apps' `docs/DESIGN-TOKENS.md`. `docs/RESEARCH.md` holds the original research and design reasoning from 2026-10-30.

## Known risks

- The repository exists only on the Mac Pro until it is pushed.
- The Wrangler login exists only on the Mac Pro and may need renewing after a long break. Another machine needs its own login.
- Wrangler is pinned at 4.151.0. With it, `pages project create` hands a new project to Workers unless `--force` is passed. Deploys to the existing project aren't affected.
- Page copy drifts when an app releases, renames its repository or lifts a limit. The Pictor page lists the preview's limits (two cameras, lens data, macOS only, not notarized); remove each one as it's lifted.

## On resume

1. If `git remote -v` is empty, ask the owner for the push and do it. Otherwise pull.
2. Run the live check above.
3. Check the latest Pictor and Corvus releases on GitHub, and update their pages if either has moved past 0.1.0 or 0.2.0-alpha.1.
