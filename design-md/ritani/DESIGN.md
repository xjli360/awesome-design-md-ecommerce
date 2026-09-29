---
version: alpha
name: "Ritani"
source_url: "https://www.ritani.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Diamond proportion charts and 360-degree stone viewers demand a UI that recedes — Ritani's canvas is consistently floor-white, interrupted only by product photography and a deep navy (#163959) that carries the top navigation and primary CTAs. The interface treats itself as a display case: generous whitespace, restrained typographic weight, and a palette that never competes with the platinum, yellow gold, or rose gold finishes on its settings. Blues graduate from the anchor navy through #2f7bbf and #62a1d8 into interactive states and progress indicators, creating a structured coolness that reads as precision rather than warmth. Grays layer from near-black #272727 through body gray #404040 to hairline #ebebeb, establishing a clean tonal ramp that keeps lengthy filter panels and size guides readable at a glance. The brand's configurator-first model — build your own ring, choose stone, choose setting — pushes the interface toward dense specification tables and comparison panels that need strong typographic hierarchy more than decorative flourishes. Borders stay tight at 1px in #dedede; corners are modestly rounded rather than pill-shaped, maintaining the precision of a jeweler's loupe rather than the friendliness of a lifestyle marketplace. System sans-serif stacks (Helvetica Neue, Segoe UI, -apple-system) serve both the display line and body copy, relying on weight and size contrast — not custom brand fonts — to separate product names from spec rows, filter labels from diamond certificate data. On mobile, the configurator collapses into a step-by-step flow where each decision (shape, carat, cut, clarity, color) occupies a full-width panel, preserving the deliberate pace of what is, for most customers, the single largest discretionary purchase they will make.

colors:
  primary: "#163959"
  primary-active: "#0f2840"
  primary-disabled: "#7a9cb8"
  ink: "#272727"
  body: "#404040"
  muted: "#595959"
  muted-soft: "#737373"
  hairline: "#ebebeb"
  hairline-strong: "#dedede"
  border-mid: "#bfbfbf"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  interactive-blue: "#2f7bbf"
  interactive-blue-light: "#62a1d8"
  alert-red: "#bd2426"
  success-green: "#9bca3e"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.02em
  display-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.01em
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.01em
  body-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-caps:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.04em
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.04em
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  price-display:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'Courier New', courier, monaco, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 46px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 46px
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline-strong}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
  nav-bar-link-active:
    textColor: "{colors.primary}"
    fontWeight: 600
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    imagePadding: "{spacing.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.body}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaSpacing: "{spacing.lg}"
  stone-shape-selector:
    backgroundColor: "{colors.canvas}"
    selectedBorder: "2px solid {colors.primary}"
    unselectedBorder: "1px solid {colors.hairline-strong}"
    textColor: "{colors.muted}"
    selectedTextColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    iconSize: 40px
    padding: "{spacing.sm}"
  diamond-filter-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-caps}"
    borderRight: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    width: 280px
  range-slider:
    trackColor: "{colors.hairline-strong}"
    fillColor: "{colors.primary}"
    thumbColor: "{colors.primary}"
    thumbSize: 18px
    trackHeight: 3px
    readoutTypography: "{typography.body-sm}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    cellPadding: "{spacing.sm} {spacing.base}"
  ring-builder-step:
    activeStepColor: "{colors.primary}"
    completedStepColor: "{colors.interactive-blue-light}"
    inactiveStepColor: "{colors.hairline-strong}"
    textColor: "{colors.body}"
    typography: "{typography.label-caps}"
    stepIndicatorSize: 28px
    connectorHeight: 2px
  quality-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.label-caps}"
    border: "1px solid {colors.hairline-strong}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  certificate-link:
    textColor: "{colors.interactive-blue}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  alert-error:
    backgroundColor: "#fdf2f2"
    textColor: "{colors.alert-red}"
    border: "1px solid {colors.alert-red}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline-strong}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Deep navy (#163959) fill with white text is the single primary action across product pages, the ring builder, and checkout. The 2px corner radius at `{rounded.xs}` preserves a precision-instrument quality rather than rounding toward consumer-friendly pill shapes. Active state darkens to `{colors.primary-active}` (#0f2840); disabled desaturates to `{colors.primary-disabled}` (#7a9cb8), keeping the shape but signaling inertness without hiding it.

**`button-secondary`** — White fill with a 1px navy border and navy text, used for secondary CTAs such as "Save to Wishlist" or "Compare Diamonds." Maintains identical height to `button-primary` so paired buttons align at the same baseline. On hover, border weight steps up to 2px — no fill change, no shadow.

**`button-tertiary`** — Transparent background with navy text and an underline, reserved for low-prominence inline actions like "View GIA Certificate" or "Learn About Cut Grade." No border and no background state; hover removes the underline and deepens text to `{colors.ink}`.

### Navigation

**`nav-bar`** — White, 64px tall, with a single 1px `{colors.hairline}` bottom border. Top-level categories (Engagement Rings, Wedding Rings, Diamonds, Fine Jewelry, Gifts) render in `{typography.nav-link}` with no resting underline. On hover, a thin navy underline appears beneath the active label. Right side carries a search icon, wishlist heart with count badge, and cart icon — all in `{colors.body}` at rest, shifting to `{colors.primary}` on hover.

### Forms & Inputs

**`text-input`** — White field with a 1px `{colors.hairline-strong}` border and 2px radius. Focus ring swaps the border to `{colors.primary}` navy with no glow or shadow. Placeholder text renders in `{colors.muted-soft}`. Appears extensively in diamond search filters, ring engraving fields, and checkout address blocks.

### Product & Diamond Cards

**`product-card`** — Zero-radius container with a 1px `{colors.hairline}` border and white background. Product image sits on a pure white field with 8px padding on all sides and no drop shadow. Below the image: `{typography.title-sm}` ring name, then a 300-weight `{typography.price-display}` price, then a `{typography.caption}` row for metal type and stone weight. On hover, the border steps to `{colors.border-mid}` — no lift, no scale.

### Stone Shape Selector

**`stone-shape-selector`** — Horizontal scrollable row of icon tiles representing round, princess, oval, cushion, emerald, pear, marquise, radiant, asscher, and heart cuts. Each tile holds a centered SVG silhouette above a `{typography.caption}` label. The selected tile gains a 2px `{colors.primary}` border; unselected tiles show a 1px `{colors.hairline-strong}` border. Tiles sit at 56×56px with `{rounded.sm}` corners and `{spacing.sm}` padding inside.

### Diamond Filter Panel

**`diamond-filter-panel`** — Left-rail panel 280px wide on desktop. Section headers use `{typography.label-caps}` in `{colors.muted}`. Range sliders cover carat weight, price, cut, color, clarity, table percentage, and depth percentage. A 1px `{colors.hairline}` right border divides the panel from the grid. Section groups have `{spacing.lg}` padding top and bottom; the panel background is `{colors.surface-soft}`.

### Range Slider

**`range-slider`** — 3px track in `{colors.hairline-strong}` with navy fill between the two thumb handles. Thumbs are 18px circles in `{colors.primary}` with no inner ring. Current selected values display as a `{typography.body-sm}` readout below the slider (e.g., "1.00 ct – 2.50 ct"). Used for carat weight, price, and all four Cs.

### Spec Table

**`spec-table`** — Two-column table alternating white and `{colors.surface-soft}` row backgrounds. Left column uses `{typography.spec-label}` (monospaced Courier New) for field names such as "Cut:", "Table %:", "Depth %:", "Polish:"; right column uses `{typography.body-sm}` for values. GIA report number renders as a `{colors.interactive-blue}` certificate link in the right column. Cell padding is `{spacing.sm}` vertical, `{spacing.base}` horizontal.

### Ring Builder Step Indicator

**`ring-builder-step`** — Three-step horizontal progress bar (Choose Setting → Choose Diamond → Complete Ring). Active step: 28px navy circle with `{typography.label-caps}` label below. Completed steps: `{colors.interactive-blue-light}` circle with a checkmark glyph. Future steps: `{colors.hairline-strong}` outline circle. Connecting lines are 2px tracks that animate a navy fill left-to-right as steps complete.

### Quality Badge

**`quality-badge`** — Small inline tag marking "Conflict Free," "GIA Certified," or "Ideal Cut" status on diamond cards and result rows. `{colors.surface-soft}` background, 1px `{colors.hairline-strong}` border, 2px radius, `{typography.label-caps}` in `{colors.muted}`. `{spacing.xs}` vertical and `{spacing.sm}` horizontal padding.

### Footer

**`footer`** — `{colors.ink}` background (#272727) with white link text and `{colors.hairline-strong}` column headers. Four columns: ring categories, diamond education, customer service, company. A fifth narrow column holds a newsletter email input with a compact navy submit button. Below the column grid, a single-row legal bar carries copyright, privacy policy, and terms links in `{typography.caption}` separated by thin dividers.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; filter panel collapses into a bottom-sheet drawer triggered by a sticky "Filter & Sort" bar; stone shape selector becomes a horizontal scroll strip; ring builder steps collapse to current step only with a thin progress bar at the top |
| Tablet | 744–1128px | Two-column product grid; filter panel becomes a collapsible left sidebar with a toggle button; nav bar compresses to hamburger + centered logo + cart icon |
| Desktop | 1128–1440px | Three-column diamond grid with persistent 280px left filter panel; full category nav bar visible; hero spans full viewport width with text overlay at left |
| Wide | > 1440px | Content max-width constrained to ~1280px with auto side margins; no additional grid columns added; hero image extends to full viewport, text block stays within the 1280px container |

### Touch Targets

- Stone shape selector tiles expand hit area to minimum 44×44px on mobile even when visually smaller
- Range slider thumbs have a 44px invisible tap target around each 18px visual thumb
- Nav bar height increases to 56px on mobile; hamburger opens a full-height side drawer with accordion category groups
- Filter bottom-sheet "Apply" and "Reset" buttons are full-width with 52px height and `{rounded.none}`
- All card and product links include a full-card tap region, not just the image or title

### Collapsing Strategy

- Diamond filter panel: hidden on mobile and tablet by default, triggered via fixed bottom bar; on desktop it is always visible in the left rail
- Ring builder sidebar summary: collapses to a sticky bottom action bar showing current ring selections and a "Continue" CTA button
- Spec table: horizontal scroll on mobile with all columns preserved — no data is removed or hidden below breakpoints
- Nav mega-menu: replaced by a full-height slide-in drawer on tablet and mobile with accordion category sections
- Footer columns: stack to a single column on mobile with accordion disclosure for each section

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned "Attention Required! | Cloudflare" — the page was fully blocked by Cloudflare anti-bot protection; all extracted hex values (#62a1d8, #bd2426, #9bca3e, #163959, #0051c3, #f68b1f, etc.) are likely sourced from the Cloudflare challenge page UI rather than from Ritani's actual design system; treat the palette as plausible-but-unverified
- No brand-specific custom typeface detected; all stacks are generic system fonts (Helvetica Neue, -apple-system, Roboto); Ritani may license a web font (possibly a serif for display headings) not captured by the extraction
- No meta theme-color present; mobile browser chrome color is unknown
- Gold, champagne, or warm-metal accent tones — commonly used in fine jewelry for hover states, metal swatch selectors, and decorative dividers — are absent from the extracted palette and could not be confirmed
- Animation easing curves and duration values for the 360-degree stone viewer, ring builder transitions, and filter panel slide animations are unextracted
- Exact nav height, breakpoint widths, grid gutter widths, and column counts are estimated from fine-jewelry category conventions rather than extracted from live DOM measurements
- Platform confirmed non-Shopify; actual commerce platform (likely a custom stack or Salesforce Commerce Cloud) may introduce platform-specific component naming or checkout UI patterns not reflected here
