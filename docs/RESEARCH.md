# senexapps.com: reference research

Reviewed 2026-10-30. Each home page was opened in a browser (800 × 600, dark
appearance) and measured after 3 s: bytes loaded (uncompressed, first view
only, lazy images excluded), script bytes, requests, third-party hosts,
landmarks and headings, and whether the CSS has dark-mode and reduced-motion
rules. Structure and copy come from the page text.

## 1. Measurements

| Site | Kind | Theme | First view | JS | Requests | Third parties |
|---|---|---|---|---|---|---|
| lux.camera | suite, blog-first | dark, fixed | 1985 KB | 171 KB | 27 | GTM, Plausible, jsDelivr |
| rogueamoeba.com | suite | follows system | 635 KB | 57 KB | 55 | Plausible, Help Scout |
| bjango.com | suite | light | 1187 KB | 0 | 30 | none |
| sindresorhus.com/apps | suite (66 apps) | follows system | 982 KB | 19 KB | 13 | GoatCounter, Cloudflare |
| panic.com | catalogue | dark, fixed | 5094 KB | 33 KB | 75 | Umami, Cloudflare |
| bombich.com | one product | follows system | 582 KB | ~0 | 8 | none |
| halide.cam | one app | dark, fixed | 4360 KB | 1 KB | 31 | Plausible |
| darkroom.co | one app | dark, system-aware | 1446 KB | 567 KB | 58 | GTM |
| raycast.com | one product | dark, fixed | 5330 KB | 3026 KB | 120 | Sentry, ProfitWell, YouTube, tracker |

Accessibility at a glance: only Sindre Sorhus has a skip link. Rogue Amoeba,
Bjango, Bombich and Halide have no h1; Lux has five and Panic nine. Rogue
Amoeba, Bombich, Halide and Raycast have no `main` landmark. Rogue Amoeba has
seven images without alt text. Raycast's grey secondary copy (#6A6B6C on
#07080A) is 3.8:1, below WCAG AA for body text.

## 2. Pros and cons for SENEX

### Lux (suite)

- + Four apps as equal cards (name, one line), each linking to its own site.
- + The journal does the selling: essays (Process Zero) and camera reviews
  double as release notes. Confident, editorial tone.
- + Dark and photo-led.
- − The home page is a blog; the app grid sits under a hero article. No
  prices, downloads, changelog, press kit or privacy link on it.
- − Support jumps to halide.cam. Five h1s, no skip link, GTM loaded.

### Rogue Amoeba (suite)

- + The clearest suite pattern: seven equal tiles (icon, name, three-word
  tagline), each with Learn, Download and Purchase.
- + A site directory with per-app release notes; a support hub (manuals,
  knowledge base, macOS compatibility status, legacy downloads); press kit and
  privacy under Company.
- + Follows system dark mode; light scripts.
- − Busy: promo banner, news, quick links and directory compete for attention.
- − No h1 or `main`; seven images lack alt; a chat beacon loads on the home page.

### Bjango (suite)

- + No JavaScript, no third parties. Large product cards, each in its own colour.
- + Astrophotography prints sit beside the apps: the closest cousin to SENEX.
- + Short, playful taglines ("The ultimate system monitor").
- − Light only; no h1; download and price only on product pages; no
  changelog or press kit on the home page.

### Sindre Sorhus (suite)

- + Best accessibility here: skip link, one h1, landmarks, dark-mode and
  reduced-motion CSS, 19 KB of script.
- + Scales to 66 apps: a featured row, then a list; cards with icon, one line,
  price and platform tags; filter chips. FAQ, Older Versions and Feedback.
- − Trust stats ("6M+ users") only work at scale; the footer repeats the nav.
- − No changelog or privacy link on the page; filters are overkill for 2–4 apps.

### Panic (catalogue)

- + Products grouped by kind (apps, games, hardware) on consistent cards.
- + A good support block: docs, serial lookup, older versions. Warm, funny copy.
- − 5 MB first view; nine h1s; the page opens on a games marquee, not apps.
- − Release notes and press kit are not linked from the home page.

### Bombich, Carbon Copy Cloner (one product)

- + Textbook single-product page: one CTA ("Download 30-Day Trial") with
  system requirements beside it, feature jump links, "New in CCC 7",
  testimonials, a knowledge base in seven languages.
- + Almost no script, eight requests.
- − Dated look (glossy screenshot, rounded display face); no h1 or `main`.
- − A cookie policy; release notes reduced to a "new features" section.

### Halide (one app)

- + Sells the result: sample photos and before/after comparisons.
- + A "Private by Design" block; press kit and contact under "Made by Lux".
- + Nearly no script.
- − 4.4 MB first view; no nav, h1 or `main`.
- − Price and trial terms unstated; support and docs elsewhere; no changelog.

### Darkroom (one app)

- + Strong hero ("Everything to edit. No import needed."), awards strip.
- + A dedicated Updates page (versioned changelog), a help centre, Press and
  Brand pages, privacy and terms. One h1, `main`, system-aware dark CSS.
- − 567 KB of script and GTM; a promo bar, eleven sections and a newsletter
  push dilute the page.

### Raycast (one product, the look the owner likes)

- + The polish target: near-black ground (#07080A); hairline borders at 6–8 %
  white; 12–16 px radii; faint radial gradients inside cards; a coloured glow
  per feature; Inter; a 64 px h1 and 20 px section heads written as a white
  lead sentence followed by a grey one.
- + A floating, blurred nav bar; keycap styling; real product UI in every
  section; changelog, manual, press kit and privacy all in the footer.
- − The heaviest site here: 3 MB of script, 120 requests, a WebGL hero that is
  empty black until it loads, error and revenue trackers.
- − No `main` or `nav` landmarks; the grey copy fails AA contrast.

## 3. What the references treat as standard

| Page | Seen on | For SENEX |
|---|---|---|
| Home with app grid | Lux, Rogue Amoeba, Bjango, Sindre Sorhus, Panic | yes |
| One page per app | all | yes |
| Download and requirements | Rogue Amoeba, Bombich, Raycast | section of each app page |
| Changelog | Rogue Amoeba (per app), Darkroom, Raycast | yes, per app |
| Docs and support | all | one Support page; docs stay in each repo |
| Privacy | Rogue Amoeba, Bjango, Panic, Bombich, Darkroom, Raycast | yes |
| About and contact | Rogue Amoeba, Sindre Sorhus, Bombich, Darkroom | one About page |
| Press kit | Rogue Amoeba, Halide, Darkroom, Raycast | later, with signed releases |
| Journal | all but Halide | not at launch |

## 4. Proposal

### (a) Page set

| Path | Page | When |
|---|---|---|
| `/` | Home: app grid | launch |
| `/pictor/` | SENEX Pictor | launch |
| `/corvus/` | SENEX Corvus | launch |
| `/pictor/changelog/`, `/corvus/changelog/` | release notes | launch |
| `/support/` | support for all apps | launch |
| `/privacy/` | site and app privacy | launch |
| `/about/` | about and contact | launch |
| `/404.html` | not found | launch |
| `/reticulum/`, `/horologium/` | hub and planner | when each is named or built |
| `/press/` | press kit | with the first signed release |

### (b) Page outlines

**Header and footer (every page).** Skip link; SENEX wordmark; nav: Pictor,
Corvus, Support, About. Footer: apps, Support, Privacy, About, GitHub, and
"© 2026 Michael Anderson".

**Home.**
1. Hero: one sentence on what the suite is (for example "Mac photo apps for
   the night sky and the camera card"), a short subline, and a night-sky band
   drawn from the icon template (gradient, Milky Way, stars, treeline).
2. App grid: a card per app with icon, name, constellation, one line, a status
   badge (Alpha, Source preview, Coming) and a platform tag. Reticulum and
   Horologium appear as quiet "coming" cards only if the owner wants them shown.
3. Principles: runs on your Mac; no account, cloud or telemetry; open source
   (licence per app).
4. Footer.

**App page (one template for Pictor and Corvus).**
1. Hero: icon, "SENEX <App>", one-line promise, one primary action
   (Download, or Build from Source while there is no signed build), a
   requirements line, and the version with its date and changelog link.
2. A screenshot of the real UI on generated test data.
3. Three to six feature sections, each a white lead sentence and a muted
   follow-on, with keycaps for shortcuts.
4. Privacy: what the app never does.
5. Download details: requirements, licence, source link, older versions.
6. Support: docs in the repo, issues, contact.

Pictor's features from its README: Import checks a RAW folder (runs, lit and
overexposed frames); Frames explains each frame's use; Sky & ground; Scene
(hero frame or moment); Compare (A/B with crops); Look & export (32-bit
master, TIFF, JPEG, HDR JPEG); the same steps as the `pictor` command.
Corvus's: copies only new originals from a card or folder; card detection;
thumbnail grid; date and event folder templates; verified copies and
duplicate checks; menu-bar app; no account, cloud or telemetry.

**Changelog.** Newest first: version, date, short list. Built from each
repo's `CHANGELOG.md` if the generator allows, otherwise copied by hand.

**Support.** Per app: docs, known issues, how to report (GitHub issues for
public repos), contact, requirements, older versions.

**Privacy.** The site: no cookies, no analytics unless the owner chooses
some, and what the host logs. The apps: per-app statements, checked against
each app before publishing.

**About.** Who makes SENEX, why constellations, how to get in touch.

**Press (later).** Icons as SVG and PNG, screenshots, one-paragraph
descriptions, a fact sheet.

**404.** The night-sky band and a link home.

### (c) Visual direction

SENEX tokens map one-to-one to CSS custom properties: GROUND for the page,
CHROME for header and footer, CARD for cards, LINE for hairlines, ACCENT for
links and the primary button. Measured contrast on GROUND: TEXT 15.7:1,
MUTED 8.1:1, ACCENT 9.1:1, GROUND text on ACCENT 9.1:1; all pass AA on CARD
and RAISED too. LINE (1.5:1) is decorative only; focus is a 2 px ACCENT ring,
the apps' selection rule.

Take from Raycast:
- the near-black ground and 1 px hairline cards (LINE), 12 px card radius
  (the token's `card`), and a faint radial gradient inside cards;
- a soft ACCENT glow behind the hero and each app icon; one accent for every
  app, as the tokens require, with the constellation emblem telling apps apart;
- section heads as a TEXT lead sentence and a MUTED follow-on, at 8:1
  instead of Raycast's 3.8:1;
- a floating header bar: CHROME at 80 % with backdrop blur;
- keycaps for shortcuts: `key` radius, LINE_STRONG border;
- real UI in every section, never stock imagery.

Leave out: the WebGL hero, megabytes of script, trackers, autoplay video and
low-contrast grey.

Type: the system font stack (SF Pro on a Mac, matching Corvus; no font
download). Inter, self-hosted, is the alternative if the owner prefers
Pictor's face everywhere. Web sizes: h1 40–64 px fluid, section heads 20–24,
body 17, nothing under 13.

Imagery: a generated night sky from the icon template, constellation line
art per app as SVG, and screenshots of generated test data. No personal photos.

Motion: none required. Hover transitions of 150 ms at most, removed under
`prefers-reduced-motion`. `color-scheme: dark`; no light theme, since the
tokens are dark only. Under `prefers-contrast: more`, borders use LINE_STRONG.

Budget: under 150 KB per page before screenshots, no JavaScript on content
pages (the planner will need some), every image with width, height and alt.

## 5. Separate note: should Raycast's look influence Pictor and Corvus?

For the owner to decide; nothing here changes the apps.

The tokens already sit close to Raycast's own app UI: a dark ground, one
accent, hairline borders, 12 pt cards, keycaps. What Raycast adds on its
website (glows, gradients, glass) is marketing, and it would hurt photo apps:
coloured light around a photo skews colour judgement in Pictor's Look &
export, and Corvus deliberately keeps native AppKit controls, which a custom
skin would fight.

One idea is worth taking from Raycast the app rather than the website:
keyboard-first discovery. Pictor has six screens and single-key shortcuts
(O, S, G, Space); a ⌘K command list and keycap hints beside actions would
make them findable.

Recommendation: no visual change to either app now. Consider a command list
for Pictor as a separate feature request. Any future visual change goes
through a DESIGN-TOKENS v2 in both repos, as the tokens file requires.
