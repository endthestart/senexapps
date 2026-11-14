# senexapps.com handoff

Updated 2026-11-13. This file stands on its own; `README.md` has the commands.

## What it is

The marketing site for SENEX, the owner's suite of apps that run on your own machines: Pictor and Corvus (photo, Mac), Lyra (music library organizer, formerly SenexSong), Towpath (self-hosted personal archive), and Poundlock with its companions Dispatch and Toolkit (local AI). It is plain HTML and CSS built by a Python-stdlib script and hosted on Cloudflare Pages, with no JavaScript, analytics, cookies or third-party requests.

## Where things stand

- **Live:** https://senexapps.com and https://www.senexapps.com, Cloudflare Pages project `senexapps`, production deployment `c785647e` from 2026-11-10, built from commit `d013475`. Every page matched the build on 2026-11-13.
- **Pages:** Home, Pictor, Corvus, Corvus release notes, Lyra, Towpath, Poundlock, Poundlock Dispatch, Poundlock Toolkit, Support, Privacy, About and a custom 404. The five new app pages were added on 2026-11-13 and are not live until the next deploy.
- **Apps described:** Pictor 0.1.0 preview (2 November 2026, github.com/endthestart/senex-pictor) and Corvus 0.2.0-alpha.1 source preview (5 November 2026, github.com/endthestart/senex-corvus). Both were still the latest releases on 2026-11-13. Towpath, Poundlock, Dispatch and Toolkit are described without version numbers, from their public repositories under github.com/endthestart. Lyra is listed as in development, with no download or source link.
- **Repository:** public at https://github.com/endthestart/senexapps, `main` only, pushed 2026-11-13. The working copy is `~/Development/senexapps` on the Mac Pro. SSH to GitHub timed out from the Mac Pro, so the remote uses HTTPS: push with `git -c credential.helper='!gh auth git-credential' push`.
- **Domain:** registered at Cloudflare on 2026-10-30 and expires 2027-10-30. DNS is at Cloudflare, and the apex and www are attached to the Pages project in the dashboard. The TLS certificate from Google Trust Services runs to 2027-01-29, and Cloudflare renews it.
- **Deploy login:** a Wrangler login limited to Pages write plus account and user read, stored on the Mac Pro only. See "Wrangler login" in the README.

## Run, check and deploy

The README has the commands to build and preview, deploy, and log in to Wrangler on another machine. Every deploy needs the owner's yes.

`build.py` fails on a broken internal link. To check that the live site matches a fresh build, run this in sh or bash from the repository:

```sh
python3 build.py
for p in "" pictor/ corvus/ corvus/changelog/ lyra/ towpath/ poundlock/ poundlock/dispatch/ poundlock/toolkit/ support/ about/ privacy/; do
  curl -s "https://senexapps.com/$p" | cmp -s - "site/${p}index.html" && echo "ok /$p" || echo "DIFFERS /$p"
done
```

## Open items, in priority order

1. **Corvus PR #8** in `endthestart/senex-corvus` fixes its README clone line and changelog date. It waits on the owner's merge, and the site doesn't depend on it.
2. **App releases.** A new Pictor or Corvus release changes its page's meta line and Version row, and a Corvus release also gets an entry on the release notes page. Then build, check and deploy.
3. **Lyra.** When it has a public repository and a first release, give its page a download button, a Source row and a Support section.
4. **Towpath icon.** The site draws a stand-in in `tools/art.py`. Replace it when Towpath gets an icon of its own.

## Owner steps pending

- Merge Corvus PR #8.
- Check that auto-renew is on for senexapps.com in the Cloudflare dashboard before 2027-10-30. It hasn't been verified.

## Decisions already made

- Static HTML and CSS only: no JavaScript, analytics, tracking cookies or third-party requests.
- Cloudflare Pages by direct upload with Wrangler, not a Git-connected build.
- No contact email: Support and About link to GitHub issues.
- Images are generated art or app screenshots of synthetic data, never personal photos.
- The music app is named Lyra, and Towpath and Poundlock keep their canal names (owner, 2026-11-13). Each app has its own page, the home page groups them as Photo, Music, Personal archive and Local AI, and the header has one Apps link.
- The look follows SENEX design tokens v1 from the apps' `docs/DESIGN-TOKENS.md`. `docs/RESEARCH.md` holds the original research and design reasoning from 2026-10-30.

## Known risks

- The Wrangler login exists only on the Mac Pro and may need renewing after a long break. Another machine needs its own login.
- Wrangler is pinned at 4.151.0. With it, `pages project create` hands a new project to Workers unless `--force` is passed. Deploys to the existing project aren't affected.
- Page copy drifts when an app releases, renames its repository or lifts a limit. The Pictor page lists the preview's limits (two cameras, lens data, macOS only, not notarized); remove each one as it's lifted. The Towpath and Poundlock pages state requirements (Docker Engine 28, Linux x86_64, Python 3.11, Node.js 22.19.0) taken from each README on 2026-11-13.

## On resume

1. Pull `main` from GitHub, or clone it on a new machine.
2. Run the live check above.
3. Check the latest Pictor and Corvus releases on GitHub, and update their pages if either has moved past 0.1.0 or 0.2.0-alpha.1.
