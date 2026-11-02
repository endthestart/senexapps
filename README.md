# senexapps.com

The marketing site for the SENEX photo apps, live at https://senexapps.com on Cloudflare Pages.

Plain HTML and CSS with no JavaScript, analytics or third-party requests. `build.py` wraps each page in `src/pages/` with `src/layout.html` and writes `site/`, which is not committed. It needs only Python 3 and fails on a broken internal link.

## Build and preview

```sh
python3 build.py
python3 -m http.server 8642 --bind 127.0.0.1 --directory site
```

`python3 tools/art.py` redraws the night sky and favicon in `src/assets/`. Run `build.py` afterwards.

## Deploy

Each deploy needs the owner's yes. Wrangler writes working files into its current folder, so run it from a temporary one:

```sh
python3 build.py
cd "$(mktemp -d)"
WRANGLER_SEND_METRICS=false npx -y wrangler@4.151.0 pages deploy ~/Development/senexapps/site --project-name senexapps --branch main --commit-dirty=true
```

The Cloudflare Pages project is `senexapps`. The domain and its DNS are at Cloudflare, and senexapps.com and www.senexapps.com are attached in the dashboard.

## Wrangler login

The login is an encrypted file, `~/Library/Preferences/.wrangler/config/default.enc`. Its key is in the login keychain under service `wrangler`, account `default`. It can write to Pages and read the account and user, and it can't change DNS or Workers.

To log in on another machine, approving the code from any browser:

```sh
npx -y wrangler@4.151.0 login --device --use-keyring --scopes account:read user:read pages:write
```

## Images

Use only generated art and app screenshots of synthetic data, never personal photos. Corvus's images are cropped from `docs/screenshots/` in its repository, and Pictor's come from its UI tests using the built-in demo scene.

## Status

As of 2026-11-02 the site is live and this repository has no remote.

Decisions open with the owner:

- **Contact email:** Support and About point to GitHub for now.
- **Pictor wording:** the home page says Pictor's source "opens with its first release". It stays while Pictor isn't release-ready.
- **Repository location:** public on GitHub or private on Gitea.

If Corvus's GitHub repository is renamed, update `andermic-photo-importer` in the Corvus, Support and About pages. The Corvus page's version details change with its first release under the new name.

Before the Mac Pro move: this repository is local-only, so it must be copied to the MiniPC or pushed to a remote, which is the owner's decision.
