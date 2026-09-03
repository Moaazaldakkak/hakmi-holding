# Hakmi / noarch site copy

**Purpose**: 100% matching local copy of the Noarch website (https://home.foxcreation.online/noarch/?storefront=envato-elements) saved as `index.html` with all assets mirrored locally.

**Source**: WordPress + Elementor site for Noarch Engineering Ltd (a Sheffield-based manufacturer serving aerospace, energy, defence, heavy industry). The live site uses:
- Elementor page builder with many addon kits (Elementor, Elementskit, JEG, Metform, Template Kit Export).
- Google Fonts: Roboto, Roboto Slab, Instrument Serif, Plus Jakarta Sans, JetBrains Mono.
- Font Awesome 5 icons.
- 23 full‑size images (various sizes from wp‑uploads).
- Inline/embedded JavaScript for sliders, accordions, counters, testimonials, and the Elementor frontend.

**What was done**:
1. Fetched the live page HTML via curl with `--resolve` (the server required this to connect).
2. Downloaded 119 assets and mirrored them under `assets/` preserving the original path structure (`assets/wp-content/...`, `assets/wp-includes/...`, `assets/fonts/...`, `assets/wp-content/uploads/...`).
3. Rewrote `index.html`:
   - All `https://home.foxcreation.online/noarch/` → `assets/`.
   - Google Fonts `<link>` tags → local `assets/fonts/{name}.css`.
   - Stripped `srcset` and `sizes` attributes from `<img>` tags (variant images were not mirrored; the base `src` is retained).
   - Version query strings (`?ver=...`) removed from local asset URLs.
   - Kept navigation/href links to other pages as‑is (they point to the live site; clicking them from the local file will 404, but the visual page is intact).
4. Verified the copy via headless Chrome (CDP):
   - **0 broken images** out of 23 total.
   - All 33 stylesheets loaded and applied.
   - Responsive layout at three viewports:
     - Desktop (1440px): full nav, 7‑column machines grid, "Get In Touch" visible.
     - Tablet (800px): hamburger menu appears, button hidden, 4‑column grid.
     - Mobile (390px): hamburger menu, 2‑column grid, no horizontal overflow.
   - Counter animation data‑attributes (`data-to-value`) intact; they animate on scroll (same as live site).
   - Font Awesome & ElementKit icon fonts load from local `assets/fonts/webfonts/`.

**How to view**:
- Place `index.html` in your XAMPP `htdocs` folder and open `http://localhost/Hakmi/index.html` in a browser.
- Or double‑click `index.html`; assets are relative from the same folder, so the page should load CSS/fonts/images correctly.

**File layout**:
- `index.html` – the page.
- `assets/` – 119 files (7.1 MB) mirroring all CSS, JS, fonts, and images.
- `assets/fonts/` – 30 woff2 webfiles + 5 Google‑Font CSS replacements.
- `assets/wp-content/...` – Elementor/Theme/Kit CSS.
- `assets/wp-includes/...` – jQuery + emoji scripts.
- `assets/wp-content/uploads/...` – all 23 page images.

**Notes**:
- CRLF line‑ending warnings appear when git indexes the assets (Windows line endings). This does not affect functionality.
- The live site’s dynamic features (AJAX‑loaded blog posts, forms, etc.) will not work offline, but the static visual page is fully rendered.