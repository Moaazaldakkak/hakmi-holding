# Hakmi Holding — Corporate Website

Arabic RTL corporate website for **مجموعة الحاكمي القابضة** (Hakmi Holding).

**Live:** https://hakmi.elogyc.com/

## Stack

| Layer | Details |
|-------|---------|
| Pages | Static HTML (`index.html` + inner pages) |
| Direction | Arabic RTL (`lang="ar" dir="rtl"`) |
| Styles | `assets/hakmi.css`, `assets/hakmi-redesign.css`, `assets/design-guidelines.css`, `assets/rtl-overrides.css` |
| Scripts | `assets/site-chrome.js`, `assets/site-content.js`, `assets/site-enhancements.js` |
| Fonts | Lyon Arabic Display (`assets/fonts/lyon-arabic.css`) |
| Homepage base | Evolved from a local WordPress/Elementor export (`assets/wp-content/…`) |
| Page generator | `scripts/build-pages.py` (optional — regenerates inner pages from template) |

No Node/npm build step. Open HTML files directly or serve the repo root with any static file server.

## Brand tokens

| Token | Hex | Usage |
|-------|-----|-------|
| Navy | `#1a344c` | Primary text, headers |
| Teal | `#026481` | Secondary navy / accents |
| Gold | `#d9aa5a` | Highlights, CTAs |
| Coral | `#d65a3c` | Accent / emphasis |
| Font | Lyon Arabic Display | Corporate Arabic typography |

See `reference.html` and `assets/design-guidelines.css` for the full UI system.

## Key pages

| Page | File |
|------|------|
| Homepage | `index.html` |
| About, Sectors, Companies, Projects, Presence, News, Partnerships, Careers, Contact, Legal | `about.html` … `legal.html` |
| Design reference | `reference.html`, `ui-reference.html` |
| Official Arabic content (source of truth) | `website_content_ar.html` |

## Local setup

```bash
git clone https://github.com/Moaazaldakkak/hakmi-holding.git
cd hakmi-holding
```

**Quick preview:** open `index.html` in a browser (relative asset paths work from repo root).

**With a local server (recommended for inner-page navigation):**

```bash
python3 -m http.server 8080
# → http://localhost:8080/index.html
```

**Regenerate inner pages** (only when editing `scripts/build-pages.py` or page templates):

```bash
python3 scripts/build-pages.py
```

## Review checklist

- [ ] RTL layout and Arabic copy read naturally
- [ ] Navigation links resolve across pages
- [ ] Brand colors and Lyon Arabic Display render correctly
- [ ] Changes match content in `website_content_ar.html` — do not invent company facts
- [ ] Compare against `reference.html` for UI patterns

## Deploy

**Hostinger git auto-deploy from `master`.** Push merged changes to `master`; Hostinger pulls and publishes automatically.

If the live site looks stale after a deploy, clear cache in hPanel (LiteSpeed / site cache).

## Project docs (start here)

| File | Purpose |
|------|---------|
| [AGENTS.md](./AGENTS.md) | Operating rules for AI and human contributors |
| [STATUS.md](./STATUS.md) | Current project state (updated after meaningful work) |
| [TASKS.md](./TASKS.md) | Open checklist; mirrored in [GitHub Issues](https://github.com/Moaazaldakkak/hakmi-holding/issues) |
