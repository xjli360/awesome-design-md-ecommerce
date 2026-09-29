---
version: alpha
name: "Stock Tank Pool"
source_url: "https://www.stocktankpool.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Galvanized steel — the material of livestock operations and farm infrastructure — gets recast here as a backyard aspiration object, and the extracted color palette mirrors that tension precisely. The most distinctive non-framework color in the set is `#bcff05`, an electric lime that sits nowhere on a conventional pool company's palette; it fires as a voltage accent against the deep navy-teal `#11262f`, a pairing that reads more surf-brand than spa catalog. The primary green `#2aa527` carries primary CTAs — vivid enough to signal action, natural enough to stay coherent with the brand's outdoor-hardware origin. Mid-tone grays `#a3abb5`, `#b1b8be`, `#d2d6da` form a galvanized-steel gradient that maps directly onto the product's surface finish, creating an unintentional but useful material resonance between the UI neutral scale and the thing being sold. Light surfaces at `{colors.surface-soft}` (`#f3f6f8`) and `{colors.surface-card}` (`#f0f3f6`) register as cloud-gray rather than white-room, keeping the canvas warm-adjacent without slipping into beige. No custom typeface loads on the live domain — it is currently a HugeDomains parking page — so the system falls back to Roboto and the system UI stack, which suits a direct-sell, hardware-focused commerce context. Buttons sit at `{rounded.lg}` — human but not pill-soft — and product photography carries the persuasion load rather than display type. The `{colors.accent}` lime paired with `{colors.deep-teal}` on promo strips and hero CTAs is the single loudest brand differentiator in the system: no traditional pool installer would publish that combination, which is exactly the point.

colors:
  primary: "#2aa527"
  primary-active: "#4f7f2e"
  primary-disabled: "#7bac29"
  accent: "#bcff05"
  on-accent: "#11262f"
  ink: "#010000"
  body: "#323031"
  muted: "#8c959e"
  muted-soft: "#a3abb5"
  hairline: "#d2d6da"
  hairline-soft: "#d9dce1"
  canvas: "#fdfdff"
  surface-soft: "#f3f6f8"
  surface-card: "#f0f3f6"
  on-primary: "#fdfdff"
  deep-teal: "#11262f"
  galvanized-mid: "#b1b8be"
  error: "#ff0303"
  on-error: "#fdfdff"

typography:
  display-xl:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.21
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.25px
  label-upper:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  spec-label:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0

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
    rounded: "{rounded.lg}"
    padding: "14px 28px"
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    opacity: 0.65
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: "13px 27px"
    height: 48px
    border: "1px solid {colors.hairline}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: "14px 28px"
    height: 48px
    border: none
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    border: "1.5px solid {colors.primary}"
    padding: "13px 27px"
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    shadow: "0 2px 8px rgba(1,0,0,0.07)"
  hero-banner:
    backgroundColor: "{colors.deep-teal}"
    textColor: "{colors.canvas}"
    minHeight: 520px
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    overlayOpacity: 0.45
    paddingX: "{spacing.xxl}"
    paddingY: "{spacing.section}"
  promo-strip:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label-upper}"
    height: 40px
    paddingX: "{spacing.base}"
  tank-size-selector:
    backgroundColor: "{colors.surface-soft}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1.5px solid {colors.primary}"
    gap: "{spacing.sm}"
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    border: "1px solid {colors.hairline-soft}"
  accessory-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "5px 12px"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.deep-teal}"
    activeTextColor: "{colors.canvas}"
  installation-guide-card:
    backgroundColor: "{colors.surface-card}"
    accentBar: "4px solid {colors.accent}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    stepNumberTypography: "{typography.display-md}"
    stepNumberColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  material-callout:
    backgroundColor: "{colors.deep-teal}"
    textColor: "{colors.canvas}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.accent}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
  footer:
    backgroundColor: "{colors.deep-teal}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.galvanized-mid}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.spec-label}"
    borderTop: "3px solid {colors.accent}"
    paddingY: "{spacing.xxl}"
  alert-error:
    backgroundColor: "#fff1f0"
    textColor: "{colors.error}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.error}"
    padding: "12px 16px"

## Components

### Buttons

**`button-primary`** — Vivid green `{colors.primary}` (`#2aa527`) on off-white text, `{rounded.lg}` corners, 48px height, 28px horizontal padding. Hover and active state steps down to `{colors.primary-active}` (`#4f7f2e`); disabled state mutes to `{colors.primary-disabled}` (`#7bac29`) at 65% opacity, retaining the green signal while communicating inactivity. Primary buttons appear on product detail pages, cart CTAs, and configuration confirmations.

**`button-accent`** — Electric lime `{colors.accent}` (`#bcff05`) with deep-teal `{colors.on-accent}` text, same 48px height and `{rounded.lg}` radius. Reserve for the single hero-level CTA per view — "Shop Now" on the homepage hero, "Get a Quote" on landing pages — to protect the lime's voltage from dilution. This button is the most brand-charged element in the system.

**`button-secondary`** — White canvas fill, `{colors.body}` text, 1px `{colors.hairline}` border. Paired beside `button-primary` in add-to-cart / learn-more CTA groups. Shares the same 48px height and `{rounded.lg}` radius to align optically with its sibling.

**`button-ghost`** — Transparent fill, `{colors.primary}` green border and text, used in dark-background contexts (hero banners, material callouts, footer) where a white-filled `button-secondary` would punch through the layout. The green border anchors it to the primary palette without competing with `button-accent`.

### Product Card

**`product-card`** — Softly surfaced `{colors.surface-card}` at `{rounded.md}` with a 4:3 image crop, a 1px `{colors.hairline}` border, and a low box shadow (0 2px 8px at 7% opacity). Title uses `{typography.title-sm}`, price uses `{typography.title-md}`, and spec details (diameter, gallon capacity, material gauge) render in `{typography.caption}` at `{colors.muted}`. Cards flow in a 3-column grid on desktop, 2-column on tablet, and single-column stack on mobile. A hover state lifts the shadow to `0 4px 16px` at 11% opacity with no color change.

### Tank Size Selector

**`tank-size-selector`** — A horizontal chip group for selecting tank diameter (8 ft, 10 ft, 12 ft, custom). Unselected chips sit on `{colors.surface-soft}` with `{colors.hairline}` borders and `{colors.body}` text; the selected chip fills to `{colors.primary}` with `{colors.on-primary}` text and a `1.5px` border. Chips gap at `{spacing.sm}`. Unavailable sizes receive 40% opacity and `cursor: not-allowed`. On mobile, the chip row scrolls horizontally rather than wrapping to preserve compact vertical rhythm.

### Spec Badge

**`spec-badge`** — A compact data cell for key product specifications: capacity (gallons), interior diameter, water depth, and steel gauge. The label renders in `{typography.spec-label}` (12px uppercase, 0.5px tracking) in `{colors.muted}`; the value sits below in `{typography.title-sm}` in `{colors.body}`. On desktop, badges sit in a 4-column inline row beneath the product title. Below 744px they collapse to a 2-column grid. The `{colors.hairline-soft}` border keeps individual badges visually separated without creating heavy grid lines.

### Hero Banner

**`hero-banner`** — Full-width image hero with a `{colors.deep-teal}` fallback background and a 0.45 dark overlay for heading legibility over photography. Heading uses `{typography.display-xl}` in `{colors.canvas}`; sub-headline uses `{typography.body-md}`. The primary CTA renders as `button-accent` — the one per-page placement of the electric lime button. Minimum height 520px on desktop, collapsing to 360px on mobile. Padding uses `{spacing.section}` vertical, `{spacing.xxl}` horizontal.

### Promo Strip

**`promo-strip`** — A 40px full-width bar in `{colors.accent}` lime with `{colors.on-accent}` deep-teal text at `{typography.label-upper}` (uppercase, 1.2px tracked). Carries short transactional copy such as free-shipping thresholds, seasonal promotions, or lead-time notices. Sits above `nav-bar` as the topmost page element; the teal-on-lime contrast creates a visual bookend with the teal footer below.

### Installation Guide Card

**`installation-guide-card`** — A step-by-step content card distinguished by a 4px left accent bar in `{colors.accent}` lime. Step numbers render large in `{typography.display-md}` at `{colors.primary}`; step titles use `{typography.title-md}`; body copy uses `{typography.body-sm}`. Cards stack vertically on mobile and shift to a 2-column grid on tablet and desktop. The lime accent bar ensures the numbered sequence reads at a glance when scanning the page.

### Accessory Chip

**`accessory-chip`** — Pill-shaped filter tags (`{rounded.full}`) for accessory filtering: liners, jets, heaters, covers, pump kits. Default state: `{colors.surface-soft}` fill, `{colors.muted}` text, `{colors.hairline}` border. Active state: `{colors.deep-teal}` fill, `{colors.canvas}` text. Used in sidebar filter panels and in horizontal filter bars above accessory product grids.

### Material Callout

**`material-callout`** — A full-width or half-width dark panel in `{colors.deep-teal}` used to explain product materials (18-gauge galvanized steel, food-grade liners, UV-resistant polymer fittings). Heading in `{typography.display-sm}` and body in `{typography.body-md}`, both in `{colors.canvas}`. Accent details and pull-quotes use `{colors.accent}` lime for inline emphasis. Sits between product grid and installation guide sections to break up the page with an educational tone.

### Navigation Bar

**`nav-bar`** — A 64px white bar with a 1px `{colors.hairline}` bottom border, brand logo left-aligned at 36px height, and primary nav links using `{typography.nav-link}`. Cart icon and any account links sit at the right edge. The active nav link gains a 2px bottom border in `{colors.primary}`. Mobile nav collapses to a hamburger icon at under 744px, with a slide-in drawer carrying the full link tree. The promo strip stacks directly above with no separating gap.

### Footer

**`footer`** — Deep teal `{colors.deep-teal}` background with a 3px top border in `{colors.accent}` lime, bookending the promo strip at page top. Column headings use `{typography.spec-label}` in `{colors.canvas}`; links use `{typography.body-sm}` in `{colors.galvanized-mid}` (`#b1b8be`) with underline on hover. Bottom row carries legal and copyright copy in `{colors.muted-soft}`. On mobile, columns stack vertically with 32px gaps.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; spec badges wrap to 2-col; hero height 360px; tank-size-selector scrolls horizontally; footer columns stack vertically |
| Tablet | 744–1128px | 2-column product grid; 3-column spec badges; hero padding reduces to `{spacing.xl}`; installation guide cards shift to 2-column |
| Desktop | 1128–1440px | 3-column product grid; full nav visible; 4-column spec badge row; material callout shifts to half-width + image split |
| Wide | > 1440px | Content max-width 1440px centered; hero and promo strip remain edge-to-edge; side margins use `{spacing.section}` to prevent line sprawl |

### Touch Targets

- All buttons, chips, and nav links maintain a minimum 44px tap target height
- Tank-size-selector chips expand to 44px height on mobile
- Accessory chips expand to 36px height on mobile (from 28px desktop)
- Footer links carry at least 40px vertical spacing between rows on mobile
- Text inputs maintain 44px height across all breakpoints

### Collapsing Strategy

- Navigation: full horizontal bar → hamburger slide-in drawer at < 744px
- Product grid: 3-col → 2-col at < 1128px → 1-col at < 744px
- Spec badge row: 4-col → 3-col at < 1128px → 2-col at < 744px
- Installation guide cards: 2-col → 1-col at < 744px
- Material callout: half-width split → full-width stacked at < 744px
- Promo strip text truncates with ellipsis on screens < 375px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The live domain is currently a HugeDomains parking page; all extracted colors originate from the HugeDomains UI rather than a real Stock Tank Pool brand site — palette assignments reflect inference from the product category and most distinctive extracted values, not verified brand guidelines
- No custom brand typeface detected; font stack defaults to system Roboto and Helvetica Neue — actual brand may use a slab serif, condensed sans, or hand-drawn display face once a real site launches
- No logo, wordmark, or icon system could be extracted — brand mark style, icon treatment, and any illustration or badge work are entirely unknown
- Photography art direction (lifestyle backyard shoots vs. product-on-white vs. user-generated galvanized rings in real yards) cannot be inferred from a parked domain
- Interactive form states — hover color shifts, focus rings, input validation patterns — are estimated from the primary/active token pair with no observed UI reference
- Dark mode strategy is unconfirmed; `{colors.deep-teal}` is used for dark-surface contexts but a formal dark-mode palette has not been established
- Checkout, cart, and account UI patterns were not observable without a live commerce store
- Pricing display conventions (MSRP strikethrough, financing offers, bulk-order tiers) are unknown
