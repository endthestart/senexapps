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

As of 2026-11-05 the site is live and this repository has no remote. The owner chose public GitHub, `endthestart/senexapps`. Until it's pushed, it exists only on the Mac Pro.

There is no contact email: Support and About point to GitHub.

A new app release changes its page's meta line and Version row. Corvus releases also get an entry in `src/pages/corvus/changelog/`.
