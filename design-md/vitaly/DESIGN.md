---
version: alpha
name: "Vitaly"
source_url: "https://www.vitalydesign.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  GerstnerProgramm — a typeface named after the Swiss grid theorist Karl Gerstner — runs the display hierarchy at vitalydesign.com, a choice that announces the brand's machine-precision ethos before the first product image resolves. The palette is a studied exercise in high-contrast cold: near-black #121212 on off-white #f1f1f1 canvas, with pure #0000ff surfacing as the electric accent for interactive states and hover underlines. That uncompromising blue carries the same material logic as the stainless steel and brass in the product catalog — it is not softened, not tinted, not friendly. A deep charcoal #242833 backs the navigation header and dark-surface sections where editorial photography needs a harder field, and the pair of reds (#ff0000, #dc0000) handle promotional and sale indicators with zero typographic decoration. Mid-tones #dedede and #d3d3d3 form the hairline and subtle surface tier, keeping the grid readable without introducing warmth. Neue Haas Grotesk Display Pro steps in at title and section-header scale, continuing a Swiss grotesk lineage that Assistant carries into UI body copy. Schengen Core appears at logo and wordmark scale, a bespoke or licensed face that gives the brand mark a geometry distinct from the text hierarchy. Radius discipline across the interface is near-zero: product cards sit at 0–2px, buttons are sharp-cornered rectangles, and no pill shape exists in the component set. Grid density shifts abruptly between editorial hero sections — single-image full-bleed — and collection pages that run three-up or four-up product rows at desktop. The absence of soft radii and the refusal of decorative drop shadows make the interface feel like a hardware product catalog — which, given that each piece is machined from industrial material, is the intended reading.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#888888"
  ink: "#121212"
  body: "#242833"
  muted: "#666666"
  hairline: "#dedede"
  hairline-soft: "#d3d3d3"
  canvas: "#f1f1f1"
  canvas-white: "#ffffff"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  surface-dark: "#242833"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-blue: "#0000ff"
  accent-blue-steel: "#334fb4"
  sale-red: "#dc0000"
  sale-red-bright: "#ff0000"

typography:
  display-xl:
    fontFamily: "'GerstnerProgramm', 'Neue Haas Grotesk Display Pro', sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.02em
  display-lg:
    fontFamily: "'GerstnerProgramm', 'Neue Haas Grotesk Display Pro', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.015em
  display-md:
    fontFamily: "'GerstnerProgramm', 'Neue Haas Grotesk Display Pro', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.01em
  display-sm:
    fontFamily: "'GerstnerProgramm', 'Neue Haas Grotesk Display Pro', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.005em
  logo-wordmark:
    fontFamily: "'Schengen Core', 'GerstnerProgramm', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.1em
    textTransform: uppercase
  title-md:
    fontFamily: "'Neue Haas Grotesk Display Pro', 'GerstnerProgramm', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-sm:
    fontFamily: "'Neue Haas Grotesk Display Pro', 'GerstnerProgramm', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', 'Neue Haas Grotesk Display Pro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Neue Haas Grotesk Display Pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  price-display:
    fontFamily: "'Neue Haas Grotesk Display Pro', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-strike:
    fontFamily: "'Neue Haas Grotesk Display Pro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'Assistant', 'Neue Haas Grotesk Display Pro', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.05em
    textTransform: uppercase
  button-md:
    fontFamily: "'Neue Haas Grotesk Display Pro', 'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Neue Haas Grotesk Display Pro', 'Assistant', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0.08em
    textTransform: uppercase
  badge:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.08em
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    border: none
  button-primary-hover:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
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
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "1px solid {colors.primary}"
    outline: "2px solid {colors.accent-blue}"
    outlineOffset: 0
  nav-bar:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: none
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    letterSpacing: 0.08em
    textTransform: uppercase
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1:1"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price-display}"
    gap: "{spacing.sm}"
    border: none
    boxShadow: none
  product-card-hover:
    imageTransform: scale(1.03)
    transition: transform 0.3s ease
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 6px
    position: top-left
    offset: 0
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  badge-sold-out:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 80vh
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: 64px 32px
    ctaMarginTop: "{spacing.xl}"
  hero-banner-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    minHeight: 60vh
    titleTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    padding: 64px 32px
  search-overlay:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    inputTypography: "{typography.display-md}"
    inputBorder: none
    inputBorderBottom: "2px solid {colors.primary}"
    padding: 32px
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    activeTextColor: "{colors.primary}"
    activeBorder: "1px solid {colors.primary}"
    inactiveBorder: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  price-display:
    regularTypography: "{typography.price-display}"
    regularColor: "{colors.ink}"
    strikeThroughTypography: "{typography.price-strike}"
    strikeColor: "{colors.muted}"
    saleColor: "{colors.sale-red}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.caption}"
    padding: 64px 32px 32px
    columns: 4
  footer-heading:
    typography: "{typography.button-sm}"
    textColor: "{colors.on-dark}"
    textTransform: uppercase
    letterSpacing: 0.1em
    marginBottom: "{spacing.lg}"
  swatch-selector:
    size: 20px
    gap: "{spacing.xs}"
    activeBorder: "2px solid {colors.primary}"
    activeOffset: 2px
    rounded: "{rounded.full}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 48px
    cellMinWidth: 44px

## Components

### Buttons

**`button-primary`** — A sharp-cornered black rectangle (`{rounded.none}`) at 48px height using uppercase `{typography.button-md}` at 0.08em letter-spacing. On hover, the fill flips to pure `{colors.accent-blue}` (#0000ff), an abrupt voltage shift that functions as brand signature and visual reward. `button-primary-active` deepens to pure `{colors.primary-active}` (#000000). `button-primary-disabled` desaturates to `{colors.primary-disabled}`, and the label loses contrast without changing shape.

**`button-secondary`** — Transparent fill with a 1px `{colors.primary}` border, matching text color and the same uppercase `{typography.button-md}`. On hover the entire button inverts: solid black fill, white text. Shares 48px height with `button-primary` so the two stack or sit adjacent without misalignment.

**`button-text-link`** — No background, `{colors.accent-blue}` text with underline, `{typography.body-sm}`. Used inline in editorial copy, product description accordions, and footer navigation.

### Navigation

**`nav-bar`** — 60px bar in `{colors.canvas-white}` with `{typography.nav-link}` uppercase links (0.05em tracking) and a 1px `{colors.hairline}` bottom border. Logo centered or left-aligned using `{typography.logo-wordmark}` (`{colors.primary}`). On editorial and dark-hero sections, the bar swaps to `nav-bar-dark`: `{colors.surface-dark}` fill with `{colors.on-dark}` text; the transition is scroll-triggered, not page-level.

**`announcement-bar`** — Full-width 36px strip in `{colors.primary}` with white uppercase `{typography.caption}` at 0.08em tracking. Appears above the nav and cycles promo codes and free-shipping thresholds. Dismissible via a minimal ×, no animation.

### Product Cards

**`product-card`** — Zero-radius card with a flush square (1:1) image well and a compact two-line text block below: product name in `{typography.body-md}` and price in `{typography.price-display}`. No card border, no shadow — grid gutter is the only separator. On hover, the product image scales to 1.03× over 0.3s ease. Sale price renders in `{colors.sale-red}` with the original in `{typography.price-strike}` `{colors.muted}`.

**`badge-sale`** — Razor-cornered label in `{colors.sale-red}` with white `{typography.badge}` text, flush to the top-left corner of the product image at zero offset. `badge-new` uses `{colors.primary}` fill. `badge-sold-out` uses `{colors.hairline}` background with `{colors.muted}` text — intentionally receding rather than calling attention.

### Hero Banner

**`hero-banner`** — Full-bleed at 80vh minimum, `{colors.surface-dark}` (#242833) as the default dark editorial backing. Headline in `{typography.display-xl}` white, body copy in `{typography.body-md}`, CTA button with `{spacing.xl}` top margin. `hero-banner-light` variant uses `{colors.canvas}` with `{colors.ink}` text and `{typography.display-lg}`, deployed on category landing pages and editorial feature callouts between collection grids.

### Search Overlay

**`search-overlay`** — Full-viewport overlay in `{colors.canvas-white}` that slides down from the nav. The input renders at `{typography.display-md}` scale — treating the search action editorially rather than functionally — with only a 2px bottom border in `{colors.primary}` and no box, no radius. Results render below as a dense type list in `{typography.body-md}`.

### Collection Filters

**`collection-filter`** — Horizontal scroll row of filter tags with zero border-radius. Active tags carry a 1px `{colors.primary}` border and weight-600 text; inactive tags show 1px `{colors.hairline}` border with `{colors.body}` text. No pill shapes. A sort dropdown at the row end uses `{typography.body-sm}` with a minimal chevron icon.

### Price Display

**`price-display`** — Regular price in `{typography.price-display}` `{colors.ink}`. On sale: sale price in `{colors.sale-red}`, original price in `{typography.price-strike}` struck through in `{colors.muted}`. The two values sit inline with `{spacing.xs}` gap.

### Footer

**`footer`** — Full-bleed `{colors.primary}` black with a four-column link grid. Section headings in `{typography.button-sm}` white uppercase with 0.1em tracking. Links in `{typography.caption}` white, underline on hover. A newsletter email input row sits at the top of the footer using an inverted `text-input` style: white border on transparent background, white placeholder text, against the black field.

### Swatches and Quantity

**`swatch-selector`** — 20px circular swatches (`{rounded.full}`) in a row with `{spacing.xs}` gap. Active swatch gains a 2px `{colors.primary}` ring at 2px offset. **`quantity-stepper`** — A three-cell inline control (−, value, +) sharing a single 1px `{colors.hairline}` border, zero radius, 48px height, each cell minimum 44px wide to align with button rows.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger icon + logo + cart; hero at 100vh; announcement bar text center-truncates to single line |
| Tablet | 744–1128px | Two-column product grid; nav shows logo and cart icon only with slide-out drawer; hero at 70vh; filter row horizontally scrollable |
| Desktop | 1128–1440px | Three or four-column product grid; full horizontal nav with dropdown panels; hero at 80vh; `nav-bar` transitions to `nav-bar-dark` on scroll into dark-hero sections |
| Wide | > 1440px | Max container 1440px with auto side margins; hero text block constrained to 50% viewport width; product grid stays at four-up maximum |

### Touch Targets

- All interactive elements are minimum 48×48px tap area on mobile
- Swatch selectors expand invisible tap area to 40×40px despite 20px visual size
- Filter tags expand to full row height (44px) on mobile with negative vertical margin
- Quantity stepper cells are each minimum 44px wide

### Collapsing Strategy

- Navigation collapses to icon bar (hamburger + centered logo + cart) below 1128px; dropdown megas become full-screen slide-in drawers
- Product grid shifts 4-up → 3-up → 2-up → 1-up across breakpoints
- Hero headline scales from `{typography.display-xl}` (desktop) to `{typography.display-md}` (mobile)
- Collection filter row becomes horizontal scroll with no wrapping on mobile; sort control moves to sticky bottom bar
- Footer four-column grid collapses to single-column stacked accordion on mobile with expand/collapse chevrons

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- GerstnerProgramm and Schengen Core are custom or licensed typefaces; exact weight range, variable-font axes, and fallback handling are not publicly documented — stacks fall back to Neue Haas Grotesk Display Pro and system sans
- Site does not declare a `meta theme-color`, so mobile browser chrome color on iOS/Android is unspecified
- Exact mega-dropdown layout and sub-category column structure not confirmed from extraction — column counts and editorial imagery treatment are inferred
- Hover image-swap behavior on product cards (second colorway on hover vs. scale-only) could not be confirmed — scale-only assumed
- Whether `{rounded.xs}` (2px) appears anywhere in production or whether all non-zero radii are only on swatches and `{rounded.full}` elements is unverified
- PDP accordion tab spacing, material-spec table layout, and size-guide modal structure not captured in extraction
- Dark mode or theme toggle — `{colors.surface-dark}` (#242833) appears in the palette but whether the site supports a persistent dark mode or only uses dark surfaces in editorial sections is unconfirmed
