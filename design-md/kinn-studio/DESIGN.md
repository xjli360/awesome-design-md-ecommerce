---
version: alpha
name: "Kinn Studio"
source_url: "https://www.kinnstudio.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The deep teal of #012e36 functions like a jeweler's case liner — it makes everything placed against it appear more luminous. Kinn Studio's palette is built around this central tension: a near-black ocean depth as primary, then a graduated ladder of warm creams (#f9f5ec, #f6f4f0, #f1eee8, #f0e6d9) ascending toward light like layers of aged parchment. The brand's typographic architecture is its most structurally interesting feature — Quarto Light and Cormorant handle editorial display with the restraint of fine-print catalog lettering, York Script ES appears as a calligraphic flourish at logotype or campaign moments, and neue-haas-grotesk-text handles all functional UI copy in the Swiss-rational tradition. The combination encodes the tagline "Modern legacy — then, now, always" as a lived typographic system rather than marketing copy. Corner geometry leans almost entirely square, with only the faintest softening at swatch and pill elements; Kinn earns authority through restraint rather than ornament. The coral-red (#e93f2c) appears at sale callouts and promotional badges, sharp against cream but subordinated within the teal-primary identity. Navigation sits on a deep #012e36 field with warm cream type, reversing the lightness of the main canvas and giving the header the visual weight of a vitrine — a display case framing the product beneath. Product cards float on {colors.surface-card}, photographed against warm neutral grounds that echo {colors.surface-warm} to simulate the slightly golden light of a physical showroom tray. The announcement bar runs the deep teal edge-to-edge with fine neue-haas-grotesk-text in {colors.on-primary}. Kinn's gold and silver pieces are worn close to skin, so the digital environment mirrors that warmth at every surface layer — making it feel contiguous with the physical intimacy of fine jewelry.

colors:
  primary: "#012e36"
  primary-active: "#002026"
  primary-disabled: "#7aabb2"
  ink: "#121212"
  body: "#393939"
  muted: "#7d7472"
  hairline: "#dedede"
  hairline-soft: "#e9e5e1"
  canvas: "#f9f5ec"
  surface-soft: "#f6f4f0"
  surface-card: "#f1eee8"
  surface-warm: "#f0e6d9"
  surface-subtle: "#eae6e3"
  on-primary: "#f9f5ec"
  accent-coral: "#e93f2c"
  accent-brown: "#623529"
  sale-red: "#ec0000"
  status-green: "#1a8000"

typography:
  display-xl:
    fontFamily: "'Quarto Light', 'Cormorant', Georgia, serif"
    fontSize: 64px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.02em
  display-md:
    fontFamily: "'Cormorant', 'Quarto Light', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  display-sm:
    fontFamily: "'Cormorant', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  script-accent:
    fontFamily: "'York Script ES', cursive"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'neue-haas-grotesk-display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'neue-haas-grotesk-display', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.03em
  label-caps:
    fontFamily: "'neue-haas-grotesk-display', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'neue-haas-grotesk-display', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'neue-haas-grotesk-display', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  price:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'neue-haas-grotesk-display', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
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
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderWidth: 1px
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    borderWidth: 1px
    borderColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.body-sm}"
    materialTypography: "{typography.caption}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.none}"
    aspectRatio: "3/4"
    imageFit: cover
  product-card-badge:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "#ffffff"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  hero-editorial:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 80vh
    layout: split-50-50
  hero-script-callout:
    textColor: "{colors.primary}"
    typography: "{typography.script-accent}"
    layout: centered-overlay
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  pdp-title:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
  pdp-price:
    typography: "{typography.price}"
    textColor: "{colors.body}"
  pdp-material-tag:
    backgroundColor: "{colors.surface-subtle}"
    textColor: "{colors.body}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  swatch-selector:
    selectedBorderWidth: 2px
    selectedBorderColor: "{colors.primary}"
    defaultBorderWidth: 1px
    defaultBorderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    size: 20px
  search-overlay-input:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    borderBottomWidth: 1px
    borderBottomColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    placeholderColor: "{colors.primary-disabled}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — A solid deep-teal (#012e36) block with warm-cream text set in all-caps neue-haas-grotesk-display at 13px, tracked at 0.1em; no border radius anywhere. Hover deepens to `{colors.primary-active}` (#002026); disabled uses the desaturated teal `{colors.primary-disabled}`. The uppercase small-cap treatment at modest size gives a hallmark quality without requiring ornament.

**`button-secondary`** — Transparent fill with a 1px teal border and teal text, matching the typographic spec of primary. Used for secondary CTAs on light backgrounds — "Add to Wishlist" alongside a primary "Add to Cart," or "Learn More" beneath an editorial headline.

**`button-secondary-on-dark`** — The same outline construction reversed for dark backgrounds (announcement bar, footer): white border, cream text in `{colors.on-primary}`. Preserves the outlined language cleanly against the teal ground without introducing a third CTA style.

**`button-ghost`** — No border, no fill; `{colors.ink}` text with underline decoration. Serves low-hierarchy inline calls like "Learn about gold vermeil" within body copy or PDP description paragraphs.

### Text Input
**`text-input`** — Square-cornered (`{rounded.none}`) field on a warm canvas background. The 1px `{colors.hairline}` border tightens to `{colors.primary}` teal on focus. Used at 48px height across email capture, search forms, and checkout. No shadow or fill shift on hover — the border-color transition alone carries the interaction signal.

### Navigation
**`nav-bar`** — Full-width deep teal (#012e36) bar at 56px, wordmark centered or left-aligned, utility icons (search, account, cart) right. Navigation category links sit in uppercase neue-haas-grotesk-display at 12px/0.08em tracking in `{colors.on-primary}`. On hover, a mega-menu drops in a warm-canvas pane below the teal bar, presenting collection imagery and sub-category links against `{colors.surface-soft}`.

**`announcement-bar`** — A 36px teal strip above the nav, full-width, centered caption text. Used for free-shipping thresholds, promotions, and sustainability messaging. Stays teal at all viewport widths.

### Product Card
**`product-card`** — Sharp-cornered card (`{rounded.none}`) with a 3:4 portrait image region on `{colors.surface-warm}`, a warm buff that mimics showroom photograph lighting. Below the image: product title in body-sm, material descriptor in caption, and price in the `{typography.price}` scale. No drop shadow; cards are differentiated by consistent spacing and warm image ground alone. `product-card-badge` overlays sale or "New" labels at the top-left in coral-red or teal with label-caps type.

### Hero
**`hero-editorial`** — 50/50 split layout at desktop: large Quarto Light display-xl headline (64px, weight 300) left on `{colors.surface-warm}`, full-bleed product or lifestyle photography right. The cream-warm text half makes the type feel contiguous with the product world. Minimum height 80vh; headline scales to display-md on tablet.

**`hero-script-callout`** — York Script ES at 48px placed as a centered overlay on product imagery or a tonal background. Used for campaign-moment copy ("Everyday Gold," "Made for Always") where the calligraphic register carries emotional weight that roman type cannot.

### Collection Header
**`collection-header`** — Full-width `{colors.surface-soft}` band with a Cormorant display-md title (40px) and optional body-md subtitle below. Generous vertical padding (`{spacing.section}`) gives the section title space to breathe before the product grid begins. No border or divider — the surface color shift alone marks the transition.

### PDP (Product Detail Page)
**`pdp-title`** — Cormorant display-sm (28px, weight 400) for the product name; Cormorant's fine serifs read especially well at this size for metal and gemstone vocabulary. `pdp-price` renders immediately below in neue-haas-grotesk-text at 14px, `{colors.body}`. Metal-type and material descriptors appear as inline `pdp-material-tag` chips — square-cornered, surface-subtle background, label-caps typography — that help users scan variant options before reaching the swatch selector.

### Swatches
**`swatch-selector`** — 20px circle swatches for gold / rose-gold / silver / two-tone variants. Selected state carries a 2px `{colors.primary}` teal outline; unselected has a 1px `{colors.hairline}` border. The `{rounded.full}` geometry is among the only soft curves in the entire UI, making the swatch row a deliberate textural contrast within an otherwise square-cornered system.

### Search Overlay
**`search-overlay-input`** — Presents over the darkened nav as a typographic underline field: no border radius, no box, only a bottom border in `{colors.on-primary}`. Placeholder text uses `{colors.primary-disabled}` — a lighter teal — to remain legible without competing with entry text.

### Footer
**`footer`** — Deep teal background matching the nav bar, forming a dark teal frame (top and bottom) around the warm-cream body. Column headings use label-caps in `{colors.on-primary}`; link rows use body-sm. A newsletter input variant of `search-overlay-input` appears inline with a `button-secondary-on-dark` submit trigger. No dividers between columns — spacing alone organizes the grid.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + full-screen teal drawer; hero stacks image above text; announcement bar stays full-width; all CTAs go full-width at 48px height |
| Tablet | 744–1128px | Two-column product grid; hero maintains split layout at reduced headline size (display-md at 40px); nav shows wordmark plus utility icons, hamburger for category mega-menu |
| Desktop | 1128–1440px | Three-column product grid (four at wide); full horizontal nav with mega-menu drop; PDP shifts to side-by-side image gallery left / detail panel right |
| Wide | > 1440px | Content max-width ~1440px centered; hero photography extends edge-to-edge while text column remains fixed; generous lateral whitespace in product grids |

### Touch Targets
- All nav utility icons (search, account, cart) padded to minimum 44×44px touch area
- Swatch selectors padded to 40px minimum tap target despite 20px visual diameter
- Mobile CTA buttons rendered full-width; 48px height preserved across all viewports
- Hamburger and close icons in mobile drawer minimum 48×48px

### Collapsing Strategy
- Product grid: 1 col → 2 col → 3 col → 4 col across breakpoints
- Hero: split 50/50 → stacked (image first on mobile for immediate visual impact)
- Navigation: full mega-menu → utility-icon bar with off-canvas teal drawer
- PDP: side-by-side gallery + details → stacked (gallery scrolls above sticky add-to-cart)
- Footer columns: 2-per-row → single stacked column on mobile
- Announcement bar: truncates with ellipsis below 375px; use a carousel if more than one message

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `{colors.primary-disabled}` (#7aabb2) is derived by lightening #012e36; not present in extracted hex list — verify against actual disabled-state CSS
- `{colors.muted}` (#7d7472) is an inferred warm-gray not in the extracted list; site may render muted text as `{colors.body}` (#393939) at reduced opacity rather than a separate hex
- Exact font weights deployed for Cormorant and Quarto Light not confirmed from extraction; 300 (Light) and 400 assumed from variant naming
- York Script ES usage context (logotype only vs. editorial headings) not confirmed; 48px size is estimated
- Noto Serif KR Medium appears in the font stack, indicating Korean-language product content; no KR-specific typography scale defined here
- All `{rounded}` values are inferred from brand-category norms — no pixel radii extracted from CSS; verify against computed styles on button and card elements
- Hover and focus states for links, swatches, and image carousels not confirmed beyond button colors
- No dark-mode or high-contrast variant detected in extraction
