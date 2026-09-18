# Agent guide — Hakmi Holding

Read this before touching code. Pair with [STATUS.md](./STATUS.md) and [TASKS.md](./TASKS.md).

## What this repo is

Single source of truth for the **Hakmi Holding** corporate Arabic RTL website. Not a monorepo — do not add unrelated products or sites here.

**Live:** https://hakmi.elogyc.com/

## Content rules

- **Official content lives in-repo.** Primary reference: `website_content_ar.html` (and page HTML derived from it).
- **Never invent** company facts, numbers, ownership, project statuses, office addresses, or partner details.
- If copy is missing or marked as pending (e.g. contact office placeholders), leave it or flag it in TASKS — do not guess.
- Tone: professional Arabic corporate RTL; match existing voice on published pages.

## Brand & UI

- Colors: navy `#1a344c`, teal `#026481`, gold `#d9aa5a`, coral `#d65a3c`
- Font: **Lyon Arabic Display** (see `assets/fonts/lyon-arabic.css`)
- Reuse patterns from `reference.html`, `assets/hakmi.css`, and `assets/design-guidelines.css`
- Inner pages share chrome via `assets/site-chrome.js` and `assets/site-content.js`

## Workflow

1. Read **STATUS.md** and **TASKS.md** before starting.
2. Prefer **pull requests**; **`master` is the deploy branch** (Hostinger git auto-deploy).
3. User preference: **merge completed Hakmi PRs without asking** unless told otherwise.
4. After meaningful work, update **STATUS.md** (dated bullet) and check off or add items in **TASKS.md**.
5. Open or update **GitHub Issues** for trackable work — Issues are the cross-device task board; keep them in sync with TASKS.md.

## Stack (short)

Static HTML/CSS/JS. Homepage retains Elementor-export assets under `assets/wp-content/`. Inner pages use the Hakmi design system. Optional: `python3 scripts/build-pages.py` to regenerate inner pages.

## Deploy & cache

- Deploy: push to **`master`** → Hostinger auto-deploys.
- Stale live content: clear site cache in **hPanel** (LiteSpeed).

## Do not

- Mix other products into this repo
- Add npm/build pipelines unless explicitly requested
- Replace placeholder contact data with invented addresses or phone numbers
- Remove `website_content_ar.html` or drift copy away from approved content without user direction
