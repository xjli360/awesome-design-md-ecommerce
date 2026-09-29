---
version: alpha
name: "StationeryHQ"
source_url: "https://www.stationeryhq.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Ocean teal (#0081a3) and forest green (#006e52) split the brand's visual authority in a way that most print-on-demand services never attempt: one color runs CTAs and navigation chrome, the other anchors secondary actions, confirmation states, and informational badges — a two-pole color system that keeps hierarchy legible even when a product grid is dense with paper stocks, finish options, and quantity tiers. The charcoal body ink (#58595b), noticeably softer than a true black, acts as a moderating tone between the bold chroma of that teal/green pair and the cool light grays (#dedede, #f0f0f0) that define card edges and form backgrounds. Arial is the sole typeface across every text scale — no web font payload, no FOUT, no rendering variance across operating systems — a choice that suits a Shopify-native checkout flow where milliseconds matter and accessibility compliance can't hinge on variable font fallback behavior. The lighter teal (#6cc4d5) appears in disabled states and pale badge fills, tying tonal variation back to the primary hue rather than introducing a third brand color. Corner radii land squarely in the utilitarian register: 4px on cards and inputs, none of the aggressive pill shapes that DTC apparel brands favor. Near-black (#121212) is reserved for display headings and primary navigation labels where maximum contrast is required, while the charcoal (#58595b) handles all running body copy. The #0000ff in the extracted palette is almost certainly browser-default link styling rather than a branded color. The result is a system engineered for a B2B/B2C hybrid audience — creative professionals ordering bulk business cards alongside consumers designing single-run wedding invitations — with a visual language that prioritizes form legibility, color-coded status clarity, and sub-second load times over editorial drama.

colors:
  primary: "#0081a3"
  primary-hover: "#006e87"
  primary-active: "#005f75"
  primary-disabled: "#6cc4d5"
  secondary: "#006e52"
  secondary-hover: "#005a42"
  secondary-active: "#004a36"
  teal-mid: "#2cadc2"
  teal-pale: "#6cc4d5"
  ink: "#121212"
  body: "#58595b"
  muted: "#828384"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  price:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  tab-label:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    hover:
      backgroundColor: "{colors.primary-hover}"
    active:
      backgroundColor: "{colors.primary-active}"
    disabled:
      backgroundColor: "{colors.primary-disabled}"
      textColor: "{colors.canvas}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    hover:
      backgroundColor: "{colors.secondary-hover}"
    active:
      backgroundColor: "{colors.secondary-active}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 2px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
    hover:
      backgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    hover:
      textColor: "{colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    labelTypography: "{typography.label}"
    labelColor: "{colors.body}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    labelTypography: "{typography.label}"
    labelColor: "{colors.body}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    linkTypography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 40px
    dropdownBackground: "{colors.canvas}"
    dropdownBorderColor: "{colors.hairline}"
    dropdownShadow: "0 4px 16px rgba(0,0,0,0.1)"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    borderRadius: "{rounded.xs}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.primary}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    padding: "{spacing.base}"
    hover:
      borderColor: "{colors.primary}"
      boxShadow: "0 2px 12px rgba(0,0,0,0.08)"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    headingTypography: "{typography.display-xl}"
    headingColor: "{colors.ink}"
    subheadingTypography: "{typography.body-md}"
    subheadingColor: "{colors.body}"
    paddingY: "{spacing.section}"
    ctaSpacing: "{spacing.lg}"
    imagePosition: right
    layout: "50/50 split"
  paper-option-tile:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    borderColorSelected: "{colors.primary}"
    borderWidth: 1px
    borderWidthSelected: 2px
    backgroundSelected: "rgba(0,129,163,0.05)"
    rounded: "{rounded.xs}"
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.ink}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    padding: "{spacing.md}"
  finish-swatch:
    size: 32px
    rounded: "{rounded.full}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    borderColorSelected: "{colors.primary}"
    borderWidthSelected: 2px
    tooltip:
      typography: "{typography.caption}"
      backgroundColor: "{colors.ink}"
      textColor: "{colors.canvas}"
      rounded: "{rounded.xs}"
      padding: 4px 8px
  quantity-stepper:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    height: 40px
    buttonColor: "{colors.primary}"
    buttonHover: "{colors.primary-hover}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    iconColor: "{colors.muted}"
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
  category-badge:
    backgroundColor: "{colors.teal-pale}"
    textColor: "{colors.primary-active}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  promo-badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  order-summary-panel:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    headerTypography: "{typography.title-md}"
    headerColor: "{colors.ink}"
    lineTypography: "{typography.body-sm}"
    lineColor: "{colors.body}"
    totalTypography: "{typography.price}"
    totalColor: "{colors.ink}"
    padding: "{spacing.lg}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.body}"
    typography: "{typography.caption}"
    separatorCharacter: "/"
  footer:
    backgroundColor: "#2c2c2c"
    textColor: "#c8c8c8"
    linkColor: "{colors.teal-mid}"
    linkColorHover: "{colors.teal-pale}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    paddingY: "{spacing.xxl}"
    borderTop: "3px solid {colors.primary}"
    columns: 4

## Components

### Buttons

**`button-primary`** — Filled ocean teal (#0081a3) with white text, 4px corner radius, and 44px height. Hover darkens to #006e87; active press to #005f75; disabled renders in pale teal (#6cc4d5) to preserve brand color continuity rather than falling back to a generic gray. The 0.4px letter-spacing on 15px Arial bold keeps the text crisp at small display sizes.

**`button-secondary`** — Forest green (#006e52) fill with white text, matching geometry to `button-primary`. This color separation is functional: teal signals "configure / start / explore" while green signals "confirm / save / complete," giving users a visual grammar for stage of the order flow without relying on position alone.

**`button-outline`** — Transparent background with a 2px teal border and teal label. Used for lower-priority actions like "Download Sample," "View Specs," or "Add to Wishlist." Hover applies the pale surface-soft fill without losing the border. Same 44px height maintains tap-target parity across the button family.

**`button-ghost`** — Text-only, no border, charcoal label in `{typography.button-sm}`. Reserved for dismissal actions, modal cancellation, and inline "clear filters" controls where visual weight should not compete with surrounding content.

### Inputs

**`text-input`** — 44px height, 1px hairline border, 4px radius. On focus, the border switches to primary teal (#0081a3) — the only color change, no glow or shadow, keeping the form aesthetic minimal. Bold 13px labels sit above each field in `{typography.label}`, necessary for multi-field customizer forms (dimensions, text content, bleed preferences) where label-inside-field patterns would collapse under simultaneous editing.

**`select-input`** — Mirrors `text-input` in all dimensions and focus state. Used for paper weight selectors (80gsm / 120gsm / 350gsm), finish type (matte / gloss / soft-touch), size (A5 / A4 / DL), and delivery speed — the dominant interaction pattern across the product configurator.

### Navigation

**`nav-bar`** — 64px tall white bar with a 1px hairline bottom border. Top-level links render in 14px bold Arial. On hover over a category link, a full-width dropdown panel descends with a soft box shadow, white background, and hairline border, organizing product subcategories in a column grid. The logo sits at 40px height, left-aligned.

**`announcement-bar`** — A 36px teal strip pinned above the nav bar, carrying a single centered message in 14px white body text. Used for free shipping thresholds, promotional codes, and seasonal deadlines. No close button — always visible for the session.

### Product Display

**`product-card`** — White card with 1px hairline border and 4px radius. A 4:3 image ratio suits flat product photography of stationery items. Product name in `{typography.title-sm}` (15px bold charcoal), price in `{typography.price-sm}` (16px bold teal). On hover, the border shifts to primary teal and a light drop shadow lifts the card 2px, providing clear interactive feedback without animation overhead.

**`paper-option-tile`** — The signature configurator component. A selection tile for paper stock or size variants; in resting state it shows a 1px hairline border and white background. When selected, the border upgrades to 2px teal and the background applies a 5% opacity teal tint, signaling selection state without obscuring the label text. A bold body-sm label and caption stack vertically inside with `{spacing.md}` padding on all sides.

**`finish-swatch`** — 32px circular swatch for gloss, matte, uncoated, and soft-touch finish selection. Resting state: thin hairline ring. Selected: 2px teal ring. On hover, a `{typography.caption}`-styled tooltip in a dark-ink pill appears above the swatch with the finish name. Tappable area expands to 44px via invisible padding on mobile.

**`quantity-stepper`** — Minus / count / plus control rendered in a hairline-bordered row on `{colors.surface-soft}`. The increment and decrement icons render in primary teal to distinguish them from the numeric display. Height 40px; used in both the product configurator and the cart line-item row.

### Search

**`search-bar`** — Full-width on mobile, fixed-width inline in the nav on desktop. A hairline-bordered text field with a teal-filled submit button flush to the right edge. Placeholder text in `{colors.muted}`; focus transitions the border to primary teal. On mobile, the search field is hidden behind a magnifier icon in the nav; tapping it expands a full-width overlay input.

### Badges

**`category-badge`** — Pale teal (#6cc4d5) background with deep teal (#005f75) uppercase text in `{typography.badge}` (11px, 0.6px tracking). Appears on category landing tiles and product cards to label product type (BUSINESS CARDS, FLYERS, NOTEPADS). The pale teal fill ties back to the primary palette without using the primary itself, reserving that color for CTAs.

**`promo-badge`** — Forest green (#006e52) background with white uppercase text. Overlaid on product card images at the top-left corner to flag SALE, NEW, or BESTSELLER items. The green distinguishes promotional status from the teal category labels, preventing visual confusion when both appear on the same card.

### Checkout

**`order-summary-panel`** — A light gray (`{colors.surface-soft}`) panel used in the checkout sidebar. 1px hairline border, 8px radius. Header in `{typography.title-md}`, line items in `{typography.body-sm}` charcoal, order total in `{typography.price}` near-black. Padding `{spacing.lg}` on all sides. Stacks below the form on mobile; fixed in the right rail on desktop.

**`breadcrumb`** — Small 12px caption-weight links in `{colors.muted}`, separated by forward slashes in `{colors.hairline}`. The current page segment renders in `{colors.body}` (charcoal) without a link underline. Critical for multi-step configurator flows where users need to navigate backward between paper, finish, quantity, and artwork upload steps.

### Footer

**`footer`** — Dark #2c2c2c background with a 3px ocean teal top accent border that signals the brand palette transition from the white page canvas. Section headings in `{typography.title-sm}` white; body links in `{colors.teal-mid}` (#2cadc2) with a pale-teal hover. A 4-column grid on desktop collapses to stacked accordion sections on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces top-level links; `paper-option-tile` grid goes 2-up; `order-summary-panel` moves below the configurator form; hero stacks text above image full-width; search becomes icon-triggered overlay |
| Tablet | 744–1128px | 2–3 column product grid; side-by-side layout for configurator and order summary; nav shows primary categories inline, secondary items behind dropdowns |
| Desktop | 1128–1440px | 4-column product grid; full mega-nav with column dropdowns; hero splits 50/50 image and text; `order-summary-panel` fixed in right rail at ~320px |
| Wide | > 1440px | Content container capped at 1440px and centered; `announcement-bar` and `hero-banner` backgrounds bleed full viewport width while content remains constrained |

### Touch Targets

- All interactive elements (buttons, steppers, input fields, swatch tiles) minimum 44×44px
- `finish-swatch` base size is 32px; invisible padding expands tappable area to 44px on touch devices
- `paper-option-tile` minimum 80px tall to ensure comfortable single-tap activation on 375px-wide screens
- Nav hamburger icon padded to 44×44px tap target regardless of icon visual size
- Quantity stepper minus and plus controls minimum 44px wide each

### Collapsing Strategy

- Mega-nav collapses to a full-screen slide-over drawer with accordion category groups and a back-arrow per level
- Footer 4-column grid stacks vertically on mobile; each section becomes a tap-to-expand accordion with a chevron indicator
- Product configurator options (paper type, finish, size, quantity) reorder into a linear vertical stacked flow on mobile, replacing the multi-column grid layout
- `announcement-bar` text truncates with ellipsis at viewports below 360px; the bar height stays fixed at 36px
- Category filter tabs above product grids collapse into a horizontally scrollable single-row strip on mobile, no wrapping

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom typeface detected — Arial is the sole font stack across all extracted styles; it is unknown whether a display or brand font loads via JavaScript after initial paint or via a third-party font service not caught by static extraction.
- Only 9 hex values were extracted; error states (red), success states, warning colors, and focus ring variants are inferred from the primary palette and Shopify defaults rather than observed directly.
- Pure blue (#0000ff) in the extracted palette almost certainly reflects browser-default unvisited hyperlink color rather than a deliberate brand token; treated as a system default and excluded from the design system.
- No motion or transition data was extractable; easing curves, animation durations, and hover transition timing all follow Shopify theme defaults in this spec.
- Print-specific UI patterns — bleed/safe-zone preview overlays, proof approval modals, color profile warnings, artwork upload progress states — could not be assessed without completing a live product configuration flow.
- No spacing or sizing tokens were directly extractable from the live site; all values follow Shopify grid conventions inferred from the platform default.
- Dark mode support is unknown; no `prefers-color-scheme` signals or alternate color sets were detected in extraction.
- Icon system (style, weight, library) is unconfirmed; no SVG sprite or icon font was identified in the extracted hints.
