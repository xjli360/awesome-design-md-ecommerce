---
version: alpha
name: "Breeo"
source_url: "https://breeo.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Charred steel and open flame reduced to a near-monochromatic digital surface — Breeo's interface is built almost entirely from black registers (#0c0c0c through #1e201f) that layer like soot cooling on cast iron. The single warm exhale in the palette is a limestone cream (#e2e0d7) that functions as the brand's primary action color: it appears on CTA buttons, hover states, and promotional badges sitting against those deep charcoal grounds, reading like firelight caught on sandstone. Typography runs Chivo — a geometric grotesque with wide apertures and mechanical terminals — set heavy at display scale (fontWeight 700–800) to match the mass of the physical product, then thinned to 400 for body copy where legibility matters more than presence. Nimbus Bold appears in lockup-style moments (wordmarks, feature callouts) where condensed width is needed. Card corners stay sharp at `{rounded.none}` or barely softened at `{rounded.xs}`, reinforcing an industrial vocabulary; only pill-shaped add-to-cart badges and filter chips reach `{rounded.full}`. Vertical rhythm is generous — `{spacing.section}` or larger between hero folds — because the photography (flames licking over X Series grates, overhead shots of glowing ember beds) needs room to breathe. The nav bar is a flat black slab (#0c0c0c) with cream wordmark and minimal link set; it collapses to a hamburger immediately below tablet. Product cards are dark surface tiles (#282828) with cream price text and a subtle 1px hairline (#dedede at 12% opacity), stacking in a 2-up mobile / 3-up desktop grid. The overall rhythm is slow, vertical, image-dominant — each scroll fold is essentially one atmospheric photograph plus one short Chivo headline plus one cream CTA, trusting the fire itself to do the selling.

colors:
  primary: "#e2e0d7"
  primary-active: "#d4d1c5"
  primary-disabled: "#e2e0d780"
  ink: "#0c0c0c"
  ink-soft: "#282828"
  body: "#dedede"
  muted: "#9a9a9a"
  hairline: "#dedede"
  hairline-dim: "#3a3a3a"
  canvas: "#0c0c0c"
  canvas-raised: "#1e201f"
  surface-soft: "#1a1a1a"
  surface-card: "#282828"
  surface-light: "#f2f2f2"
  on-primary: "#0c0c0c"
  on-dark: "#f2f2f2"
  warm-cream: "#e2e0d7"
  charcoal-deep: "#121212"
  meta-dark: "#1e201f"

typography:
  display-xl:
    fontFamily: "'Nimbus Bold', 'Chivo', Arial, Helvetica, sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: -1.2px
  display-lg:
    fontFamily: "'Chivo', Arial, Helvetica, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.8px
  display-md:
    fontFamily: "'Chivo', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Chivo', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Chivo', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Chivo', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Chivo', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Chivo', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Chivo', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-uppercase:
    fontFamily: "'Chivo', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Chivo', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Chivo', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Chivo', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.4px
  price:
    fontFamily: "'Chivo', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Chivo', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
    textDecoration: line-through

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 20px
  xl: 32px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  base: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 64px
  hero: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 15px 31px
    height: 48px
    border: 1px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 48px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.none}"
    padding: 18px 40px
    height: 56px
    width: 100%
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 14px 16px
    height: 48px
    border: 1px solid {colors.hairline-dim}
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: 1px solid {colors.primary}
    backgroundColor: "{colors.surface-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 40px
    borderBottom: none
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    backdropFilter: none
    borderBottom: 1px solid {colors.hairline-dim}
  mobile-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    padding: "{spacing.lg}"
    width: 100vw
    height: 100vh
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    padding: 0
    imageAspectRatio: 1 / 1
    gap: "{spacing.md}"
  product-card-hover:
    transform: none
    imageOpacity: 0.85
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    minHeight: 100vh
    padding: "{spacing.hero} {spacing.xl}"
    textAlign: center
    overlayGradient: "linear-gradient(to bottom, transparent 40%, {colors.canvas} 100%)"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
    maxWidth: 900px
  hero-subline:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 600px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.none}"
    padding: 20px 48px
    height: 60px
  collection-grid:
    columns: 3
    gap: "{spacing.base}"
    padding: "0 {spacing.xl}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  badge-soldout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  feature-callout:
    backgroundColor: "{colors.canvas-raised}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderLeft: 3px solid {colors.primary}
  footer:
    backgroundColor: "{colors.charcoal-deep}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: 1px solid {colors.hairline-dim}
  footer-heading:
    typography: "{typography.caption-uppercase}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.md}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  size-selector:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    border: 1px solid {colors.hairline-dim}
    minWidth: 64px
  size-selector-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: 1px solid {colors.primary}
  image-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    gap: "{spacing.xs}"
    thumbnailSize: 72px
  comparison-table:
    backgroundColor: "{colors.canvas-raised}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    cellPadding: "{spacing.base} {spacing.lg}"
    border: 1px solid {colors.hairline-dim}
---

## Components

### Buttons

**`button-primary`** — A flat, zero-radius rectangle filled with warm cream (#e2e0d7) and dark ink text. Uppercase tracking at 0.6px gives it an engraved quality. On hover the background shifts to `{colors.primary-active}`, a slightly deeper sandstone. Disabled state reduces opacity to ~50% via the alpha channel. No box-shadow in any state — the button relies on color contrast alone against the dark canvas.

**`button-secondary`** — A ghost button: transparent fill, 1px cream border, cream uppercase text. On hover the fill floods to `{colors.primary}` and text inverts to `{colors.on-primary}`, creating a satisfying "fill" transition. Used for secondary actions on product pages and collection headers.

**`button-dark`** — Solid black (#0c0c0c) with light text, used on the rare light-background sections (warranty pages, light promotional modules). Same zero-radius geometry and uppercase treatment as primary.

**`button-add-to-cart`** — An oversized primary button (56px tall, full-width on mobile) that anchors every product detail page. The larger `{typography.button-lg}` scale and extra padding make it the heaviest interactive element on screen.

### Navigation

**`nav-bar`** — A 64px-tall strip of solid black with the wordmark left-aligned and navigation links center or right. Links use `{typography.nav-link}` at weight 500 with 0.4px tracking. No bottom border until scroll, when a subtle `{colors.hairline-dim}` line fades in. The bar is always opaque — no blur/translucency tricks.

**`mobile-menu`** — Full-viewport takeover with a dark background. Links are stacked vertically using `{typography.title-md}` with generous `{spacing.lg}` between items. Close icon top-right, 48px touch target.

**`announcement-bar`** — Sits above the nav, 40px tall, filled with the cream primary. Text is dark on cream at `{typography.caption}` scale. Used for shipping thresholds, seasonal promos, or product launches.

### Product Cards

**`product-card`** — A borderless dark tile (`{colors.surface-card}` / #282828) with a 1:1 image region on top and product info below. Title in `{typography.title-sm}` uses full white; price appears in the warm cream `{colors.primary}` to create a subtle hierarchy signal. No border-radius anywhere. On hover, image opacity dims slightly to 0.85, inviting the click without shifting layout.

### Hero Section

**`hero-section`** — Full-viewport dark canvas with a large background image (fire pit in use, typically dusk/night photography) underneath a bottom-fading gradient that dissolves into the canvas color. Headline centered in `{typography.display-xl}` — up to 56px — with a short subline in `{typography.body-md}` beneath, then a single cream CTA. The vertical spacing between elements uses `{spacing.xl}` to `{spacing.xxl}`.

### Badges

**`badge-new`** — A small rectangular chip (no radius) with cream fill and dark text, positioned absolute top-left on product card images. Uses `{typography.caption-uppercase}` for a tight, all-caps label.

**`badge-soldout`** — Same geometry but with `{colors.surface-soft}` fill and muted text to visually recede.

### Feature Callout

**`feature-callout`** — A wide panel on the raised canvas (#1e201f) with a 3px left border in cream. Contains a `{typography.display-sm}` headline plus body copy. Used to highlight engineering specs (double-wall airflow, X Series compatibility, etc.).

### Size Selector

**`size-selector`** — Inline selectable chips with hairline borders. Default state is transparent with dim border and body-colored text. Active state fills cream with dark text and matches border to fill. Commonly seen on fire pit diameter options (19", 24", 30").

### Comparison Table

**`comparison-table`** — Rows of product specs on a slightly raised surface with hairline cell borders. Header row uses `{typography.title-sm}`; cells use `{typography.body-sm}`. Alternating backgrounds are not used — separation comes purely from the hairline grid.

### Footer

**`footer`** — Deep charcoal (#121212) background, slightly darker than the main canvas, separated by a hairline. Column headings in uppercase caption style; links in muted body-sm that brighten to `{colors.on-dark}` on hover.

### Image Gallery

**`image-gallery`** — Product page gallery with a main image region (no radius) and a row of 72px square thumbnails below, separated by `{spacing.xs}` gaps. Active thumbnail gets a 2px cream border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero headline drops to `{typography.display-md}` (32px); add-to-cart button full-width sticky at bottom; comparison table scrolls horizontally; section padding halved to 32px |
| Tablet | 744–1128px | 2-column product grid; nav links visible but condensed; hero headline at `{typography.display-lg}` (42px); image gallery switches to swipe carousel |
| Desktop | 1128–1440px | 3-column product grid; full nav with all links; hero at full `{typography.display-xl}` (56px); product page uses side-by-side layout (gallery left, info right) |
| Wide | > 1440px | Content max-width capped at 1440px and centered; lateral padding increases to 64px; product grid may expand to 4-up for collection pages |

### Touch Targets

- All interactive elements maintain 48px minimum tap height on mobile
- Size selector chips get extra vertical padding (12px) on touch devices
- Mobile menu links spaced at `{spacing.lg}` (24px) minimum between baselines
- Thumbnail gallery uses horizontal scroll with 44px minimum thumb targets

### Collapsing Strategy

- Navigation links collapse to hamburger below 744px; announcement bar remains visible
- Product page shifts from two-column (gallery + details) to stacked single-column below 1024px
- Comparison tables become horizontally scrollable with a sticky first column below tablet
- Feature callout panels stack vertically and lose the left border accent on mobile, gaining a top border instead
- Footer columns collapse from 4-across to 2×2 grid on tablet, single-stack on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No distinct accent/CTA color beyond the warm cream was detected — if the brand uses a separate highlight (e.g., orange or red for sale pricing), it was not present in the extracted palette
- Chivo weight variants (300, 400, 500, 700, 800, 900) could not be confirmed from extraction; weights above are inferred from typical Chivo usage on Shopify
- Nimbus Bold usage context (whether display-only or also nav) is unclear; assigned to display-xl lockups only
- No icon system or icon font was detected in the extraction
- Exact animation/transition durations (hover fades, menu slides) were not captured
- Dark-mode vs. light-mode split is ambiguous — the site appears predominantly dark, but some interior pages (blog, FAQ) may use `{colors.surface-light}` as canvas; behavior for those pages is not documented here
- Cart drawer / slide-out panel styling was not captured in the color extraction
