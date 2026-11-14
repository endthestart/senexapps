# senexapps.com

The marketing site for the SENEX apps (Pictor, Corvus, Lyra, Towpath, Poundlock, Poundlock Dispatch and Poundlock Toolkit), live at https://senexapps.com on Cloudflare Pages.

Plain HTML and CSS with no JavaScript, analytics or third-party requests. `build.py` wraps each page in `src/pages/` with `src/layout.html` and writes `site/`, which is not committed. It needs only Python 3 and fails on a broken internal link.

## Build and preview

```sh
python3 build.py
python3 -m http.server 8642 --bind 127.0.0.1 --directory site
```

`python3 tools/art.py` redraws the night sky, the favicon and the Lyra and Towpath icons in `src/assets/`. Run `build.py` afterwards.

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

Icons: Pictor's and Corvus's come from their repositories. The Poundlock, Dispatch and Toolkit icons are resized from each repository's 1024-pixel brand icon. `tools/art.py` draws Lyra's from the SENEX icon template and Towpath's, which is a stand-in because Towpath has no icon of its own.

## App releases

A new Pictor or Corvus release changes its page's meta line and Version row. Corvus releases also get an entry in `src/pages/corvus/changelog/`. The Towpath and Poundlock pages name no version and link to the latest release, so they change only when a requirement or limit does. The Lyra page says it isn't released; give it a download and source link when it is.

## Status

Current state, open items and pending owner steps are in [HANDOFF.md](HANDOFF.md).
