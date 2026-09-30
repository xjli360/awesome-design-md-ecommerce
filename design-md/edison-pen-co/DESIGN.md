---
version: alpha
name: "Edison Pen Co."
source_url: "https://edisonpen.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Parchment arrives before chrome at Edison Pen Co. The dominant surface is #dcd7ca — an unbleached cream much closer to cotton rag paper than digital white — and it primes every visitor to decelerate before reading a single word: this is a maker's site, not a marketplace. Against that warm field, crimson (#cd2653) appears with the economy of a wax seal: at the single decisive CTA moment — add to cart, confirm selection, initiate custom order — and nowhere else. The rest of the palette reads like a working desk: charcoal (#32373c) for running copy, near-black (#1e1f26) for display headings, and a deep molasses brown (#382110) that suggests dried iron-gall ink pooled in a glass bottle under an incandescent lamp. Muted gray (#6d6d6d) and its lighter sibling (#949494) handle secondary copy and ornamental hairlines without competing with the warm ground.

  Typography is unapologetically pre-digital. Palatino and Georgia dominate the display hierarchy — serif stacks chosen for a customer who selected a fountain pen over a ballpoint, who registered that a nib was adjusted by hand. System sans-serif (Geneva, Verdana) enters only for form labels, utility navigation, and small swatches; brief, functional appearances that prevent the reading experience from sliding into commodity UI. Display scale sits at 28–40px at normal weight (400) rather than the bold-heavy register of apparel brands; type trusts white space rather than mass to assert hierarchy.

  Corners are almost uniformly square. Product cards, swatches, and image frames carry {rounded.xs} at most — coherent with the hand-turned acrylic and ebonite rods Edison machines on a lathe. Pill shapes ({rounded.full}) appear exclusively on finish-color swatch circles. Spacing breathes generously in editorial zones — section gaps at 64px or wider let photography carry the argument — then contracts to a consistent grid on catalog pages where comparison is the primary job. The footer holds the same parchment canvas as the header and lets secondary navigation recede to muted gray (#949494), keeping the warm groundplane unbroken from masthead to page end.

colors:
  primary: "#cd2653"
  primary-active: "#a81e43"
  primary-disabled: "#e8a0b2"
  ink: "#1e1f26"
  body: "#32373c"
  muted: "#6d6d6d"
  muted-soft: "#949494"
  hairline: "#dddddd"
  hairline-soft: "#f0f0f0"
  canvas: "#dcd7ca"
  surface-white: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#dcd7ca"
  brown-ink: "#382110"
  charcoal-dark: "#24292d"
  text-secondary: "#444444"

typography:
  display-xl:
    fontFamily: "Palatino, 'Palatino Linotype', 'Book Antiqua', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Palatino, 'Palatino Linotype', 'Book Antiqua', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.22
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Palatino, 'Palatino Linotype', 'Book Antiqua', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "Palatino, 'Palatino Linotype', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Georgia, Palatino, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Georgia, Palatino, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Georgia, Palatino, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "Georgia, Palatino, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Geneva, Verdana, 'Lucida Grande', 'Lucida Sans Unicode', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-ui:
    fontFamily: "Geneva, Verdana, 'Lucida Grande', 'Lucida Sans Unicode', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "Geneva, Verdana, 'Lucida Grande', 'Lucida Sans Unicode', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "Geneva, Verdana, 'Lucida Grande', 'Lucida Sans Unicode', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "Geneva, Verdana, 'Lucida Grande', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.6px
    textTransform: uppercase
  price-display:
    fontFamily: "Georgia, Palatino, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "Geneva, Verdana, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase

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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.body}"
    padding: 11px 27px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.body}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: none
    padding: 8px 0px
  text-input:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    border: "1px solid {colors.body}"
    outline: none
  text-input-error:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-link-active:
    textColor: "{colors.primary}"
    borderBottom: "1px solid {colors.primary}"
  nav-bar-link-hover:
    textColor: "{colors.ink}"
  announcement-bar:
    backgroundColor: "{colors.brown-ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
    padding: 0 {spacing.base}
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: none
    imageAspectRatio: "4/3"
    padding: "{spacing.base} 0"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-subtitle:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  finish-badge:
    rounded: "{rounded.full}"
    width: 20px
    height: 20px
    border: "2px solid {colors.hairline}"
    display: inline-block
  finish-badge-selected:
    border: "2px solid {colors.body}"
    outline: "2px solid {colors.body}"
    outlineOffset: 2px
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    minHeight: 560px
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 640px
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    maxWidth: 520px
    marginTop: "{spacing.lg}"
  model-selector:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.body}"
    typography: "{typography.label-ui}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    height: 44px
    cursor: pointer
  model-selector-active:
    border: "1px solid {colors.body}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
  model-selector-hover:
    border: "1px solid {colors.muted-soft}"
  nib-spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    borderTop: "1px solid {colors.hairline}"
  nib-spec-table-row:
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} 0"
  collection-filter:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.label-ui}"
    rounded: "{rounded.none}"
    border: none
    padding: "{spacing.xs} {spacing.sm}"
    cursor: pointer
  collection-filter-active:
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.ink}"
  search-input:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    height: 40px
  search-input-focus:
    border: "1px solid {colors.body}"
    outline: none
  custom-pen-cta:
    backgroundColor: "{colors.brown-ink}"
    textColor: "{colors.on-dark}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
    paddingLeft: "{spacing.xxl}"
    paddingRight: "{spacing.xxl}"
    rounded: "{rounded.none}"
  custom-pen-cta-headline:
    typography: "{typography.display-md}"
    textColor: "{colors.on-dark}"
  custom-pen-cta-body:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
    marginTop: "{spacing.base}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.xxl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.base}"
  footer-link:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
    display: block
    marginBottom: "{spacing.sm}"
  footer-link-hover:
    textColor: "{colors.body}"
  pen-image-viewer:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    aspectRatio: "4/3"
  pen-image-thumbnail:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    width: 72px
    height: 54px
    cursor: pointer
  pen-image-thumbnail-active:
    border: "1px solid {colors.body}"

## Components

### Buttons

**`button-primary`** — Square-cornered ({rounded.none}), crimson (#cd2653) fill, uppercase Geneva 13px at 0.8px letter-spacing, 44px tall. The all-caps treatment reads as a printer's slug — functional and print-adjacent rather than a soft digital affordance. On hover darkens to #a81e43; disabled state fades fill to the blush #e8a0b2 while retaining white text and a `not-allowed` cursor. Used exclusively for the single decisive action per page: add to cart, submit custom inquiry, confirm selection.

**`button-secondary`** — Transparent fill, 1px solid charcoal (#32373c) border, same uppercase Geneva label and 44px height as primary. On hover, fill inverts to charcoal and text lifts to canvas (#dcd7ca), performing a linocut-print reversal. Used for secondary CTAs: view details, browse collection, learn about nibs.

**`button-ghost`** — No border, no fill, muted gray (#6d6d6d) uppercase text in 11px Geneva. Underline appears on hover. Used for tertiary actions and dismiss affordances that should not compete visually with either primary or secondary buttons.

### Navigation

**`nav-bar`** — 64px tall, parchment canvas (#dcd7ca) background with a 1px hairline border at the bottom. All links in Geneva 13px at 0.2px tracking. Active link shifts to crimson (#cd2653) with a matching 1px underline. No heavy drop-shadow menus — subcategories open as flat panels matching the canvas color. Logo anchors left; cart and search icons anchor right as minimal icon buttons.

**`announcement-bar`** — A full-width molasses strip (#382110) placed above the nav, 36px tall, centered Geneva 12px in canvas-colored (#dcd7ca) text. Reserved for lead-time notices ("Custom orders currently shipping in 8–10 weeks"), promotional events, and supply alerts. The dark warm brown grounds the page before the parchment navigation appears.

### Product Card

**`product-card`** — Zero radius, no box-shadow, no card border. Pen photography sits at a 4:3 ratio against a soft gray (#f0f0f0) panel. Pen name in Georgia 18px below the image, followed by price in Georgia 20px charcoal. Finish-color swatches (20px circles with {rounded.full}) sit in a horizontal row below the price; the selected swatch receives a 2px outline-offset ring in body charcoal, emulating the contact ring left by a barrel held flat. Hover state on the card image offers a subtle 1:1.03 scale — no shadow theater.

### Hero

**`hero`** — Parchment canvas (#dcd7ca) ground, minimum 560px tall with equal 64px vertical padding. Headline in Palatino 40px at normal weight — wide enough to command attention without resorting to typographic heaviness. Sub-headline in Georgia 16px, muted gray (#6d6d6d), capped at 520px for comfortable line length. A single `button-primary` anchors below with 24px gap. No carousel; one full-width pen photograph preferred, lit from a single source to emphasize material grain and finish depth.

### Collection Filter

**`collection-filter`** — Text-only tab row with no pill outlines or card backgrounds. Inactive filters in muted gray (#6d6d6d), Geneva 13px; the active filter shifts to ink (#1e1f26) and gains a 1px bottom border — like a proofreader's underline mark. Filters cover pen series, material category, price tier, and nib size. On mobile the row becomes horizontally scrollable without wrapping.

### Model Selector

**`model-selector`** — Flat rectangular option tile with 1px hairline border ({rounded.none}). On selection, border sharpens to body charcoal (#32373c) and background lifts to canvas parchment (#dcd7ca). Used on the product detail page for pen body material (acrylic, ebonite, urushi), nib grade (student, artist, flex), and color variant. Selected state is legible at a glance without requiring radio-button chrome.

### Nib Spec Table

**`nib-spec-table`** — Soft gray (#f0f0f0) background panel, Georgia 14px for cell content, rows divided by 1px hairlines (#dddddd). Surfaces nib width (EF through BBB), feed material, slit geometry, and recommended ink viscosity in structured rows. The serif body type in a spec table is intentional: it signals that this data deserves to be read like a reference, not scanned like a feature matrix.

### Pen Image Viewer

**`pen-image-viewer`** — Main image at 4:3 aspect ratio, soft gray background, 1px soft hairline border. A horizontal strip of thumbnail tiles (72×54px each) sits below; the active thumbnail carries a 1px body-charcoal border. No lightbox modal by default — the large image expands in-place rather than interrupting the page reading flow.

### Custom Pen CTA Band

**`custom-pen-cta`** — Full-width editorial band in molasses brown (#382110), Palatino 24px headline in canvas text, body paragraph in muted gray (#949494). 64px top and bottom padding. Sits between the catalog section and the footer. Square-cornered, no decorative border. This is the brand's single moment of chromatic departure from the warm neutral field — it functions as a register shift, signaling that custom work is a different relationship than catalog purchase.

### Footer

**`footer`** — Continuous parchment canvas from the page body, divided only by a 1px hairline at the top. Section headings in Georgia 16px charcoal; links in Geneva 12px muted gray (#949494), spaced with 8px vertical gaps. No contrasting dark footer background — the page ends as it begins, on the same warm cream ground that opened it.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer on parchment background; hero headline drops to Palatino 28px; finish swatches wrap to two rows; announcement bar truncates to one key message; nib spec table scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; nav shows primary categories inline, secondary links in overflow drawer; hero shifts to 50/50 image–text split with image right; custom pen CTA reduces to 40px vertical padding |
| Desktop | 1128–1440px | Three- or four-column catalog grid; full horizontal nav with all primary categories visible; hero at full 560px with centered composition; nib spec table displayed in full |
| Wide | > 1440px | Content max-width 1280px centered on the parchment canvas; catalog grid holds at four columns; hero photography expands edge-to-edge behind a constrained text container |

### Touch Targets
- All interactive elements — buttons, finish swatches, filter tabs, nav links, thumbnail tiles — maintain a minimum 44×44px touch area
- Finish swatch circles (20px visual diameter) receive a 44px invisible tap target via padding or pseudo-element expansion
- Model selector tiles padded to 44px height on mobile regardless of label length
- Thumbnail strip tiles expand to full-bleed tap regions on mobile

### Collapsing Strategy
- Navigation: full horizontal links on desktop → hamburger slide-in drawer on mobile with parchment background (#dcd7ca) and standard nav-link typography
- Collection filter: horizontal tab row on desktop → single-line horizontally-scrollable row on mobile (no wrapping, no dropdown collapse)
- Custom pen CTA band: vertical padding reduces from 64px to 32px on mobile; headline steps down from display-md (24px) to display-sm (20px) Palatino
- Nib spec table: horizontal scroll on mobile rather than column collapse — data integrity takes priority over layout compression
- Hero: stacks image above text on mobile; image shifts to 100vw bleed and text sits below in full-width block with standard horizontal padding

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Many extracted hex values (#21759b, #00d084, #0693e3, #fdf497, #ff9900, #5865f2, #e94c89, #02e49b, #0757fe, #0a7aff, #4280ff, #f45800, #0866ff, #0461dd, #1d4fc4, #f00075, #e65678) appear to originate from WordPress Gutenberg editor UI, social-share widgets, or embedded third-party services — they were excluded from the brand palette
- No meta theme-color was found; mobile browser chrome color is unspecified and will default to system behavior
- Font stacks are system defaults (Geneva, Verdana, Georgia, Palatino) with no evidence of custom web fonts loaded via @font-face or Google Fonts; if a proprietary typeface exists, it was not detectable from extracted metadata
- No explicit dark-mode palette was detected; canvas/parchment inversion behavior for prefers-color-scheme: dark is unspecified
- Logo treatment, wordmark dimensions, and any logomark SVG data were not extractable from meta or CSS
- Exact transition durations and easing curves not extracted — 150ms ease assumed throughout
- No animation or micro-interaction tokens (parallax, scroll-triggered reveals) detected from available data
- Product photography art direction (background color, lighting angle, prop styling) inferred from brand category; not directly extractable
