---
version: alpha
name: "Fireball Printing"
source_url: "https://fireballprinting.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The name earns its color — #cf4646, a warm declarative red that ignites every primary call-to-action on the site before a visitor reads a single headline. Against a canvas washed in printer's-proof blue-white (#f5f9fb, #e0ecf4), that red arrives with the urgency of a deadline stamp, and the entire design system is organized around that moment of contrast. The typography system runs exclusively on Brown — Brown-Bold for headlines, price displays, CTAs, and quantity labels; Brown-Regular for body copy, spec tables, and form fields — a geometric sans-serif that sits between Futura's precision and something more workday and durable, legible at 12px caption labels and authoritative at 40px hero headlines without visual strain in either register. The color vocabulary is unusually broad for a printing service: a structured blue axis descends from deep navy #002e47 through brand-blue #3483ac down to pale wash tones (#ddeaf2, #cadfeb) that tile as surface separators and product-category backgrounds — a whole range that likely maps to pantone reference sheets and paper-stock swatches rather than arbitrary branding decisions. Alongside this, a deliberate accent system introduces yellow (#fae351), green (#76ae31, #9cd15a), and amber (#dc9600) as category flags and turnaround-status markers: rush-order urgency versus eco-stock availability, each distinguishable at scroll speed across a dense product grid. Rounded corners are consistent throughout — {rounded.sm} (8px) on interactive elements, {rounded.md} (12px) on product cards and calculator panels — approachable without veering toward consumer-app pill shapes; the geometry signals tool, not toy. The overall layout is catalog-dense: inline pricing on product cards, a quote-calculator widget that front-loads quantity and specification selection, a footer that treats turnaround times and paper options as first-class navigation. Every {spacing.lg} gap earns its keep by separating a paper finish option from its price tier, and the print workflow — configure, upload, proof, order — is the organizing spine of every page template on the site.

colors:
  primary: "#cf4646"
  primary-active: "#9f2929"
  primary-disabled: "#e9abab"
  primary-light: "#f4d4d4"
  brand-blue: "#3483ac"
  brand-blue-active: "#286585"
  brand-navy: "#002e47"
  ink: "#231f20"
  body: "#3d4d57"
  muted: "#4c616d"
  hairline: "#eeeeee"
  hairline-soft: "#ddeaf2"
  canvas: "#ffffff"
  surface-soft: "#f5f9fb"
  surface-blue: "#e0ecf4"
  surface-card: "#ffffff"
  surface-wash: "#eaf3f7"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-yellow: "#fae351"
  accent-yellow-light: "#fdf3b4"
  accent-green: "#76ae31"
  accent-green-light: "#b4dc82"
  accent-amber: "#dc9600"
  status-error-light: "#efbfbf"

typography:
  display-xl:
    fontFamily: "'Brown-Bold', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Brown-Bold', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Brown-Bold', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Brown-Bold', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Brown-Regular', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Brown-Regular', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Brown-Regular', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Brown-Regular', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Brown-Bold', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Brown-Bold', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Brown-Bold', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'Brown-Bold', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.2px
  quote-price:
    fontFamily: "'Brown-Bold', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  badge-label:
    fontFamily: "'Brown-Bold', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Brown-Regular', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.brand-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.brand-blue-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  button-ghost-blue:
    backgroundColor: transparent
    textColor: "{colors.brand-blue}"
    border: "2px solid {colors.brand-blue}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.brand-blue}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.brand-blue}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar-top-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspect: "4 / 3"
  hero-banner:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 420px
    padding: "{spacing.xxl} {spacing.section}"
  quote-calculator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    priceTypography: "{typography.quote-price}"
    priceColor: "{colors.primary}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.xl}"
  file-upload-zone:
    backgroundColor: "{colors.surface-blue}"
    borderColor: "{colors.brand-blue}"
    borderStyle: "2px dashed"
    textColor: "{colors.body}"
    iconColor: "{colors.brand-blue}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
  category-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  category-badge-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  category-badge-blue:
    backgroundColor: "{colors.brand-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  turnaround-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  paper-swatch-chip:
    backgroundColor: "{colors.surface-wash}"
    borderColorDefault: "{colors.hairline}"
    borderColorSelected: "{colors.primary}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  order-steps:
    backgroundColor: "{colors.surface-soft}"
    activeStepColor: "{colors.primary}"
    completedStepColor: "{colors.accent-green}"
    inactiveStepColor: "{colors.hairline}"
    labelTypography: "{typography.caption}"
    connectorHeight: 2px
  footer:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.surface-blue}"
    headlineTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline-soft}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The primary CTA, rendered in fireball red (#cf4646) with white Brown-Bold type at 15px. Used for "Order Now," "Get a Quote," and all checkout-flow progression actions. Active state deepens to `{colors.primary-active}` (#9f2929); disabled state washes to `{colors.primary-disabled}` (#e9abab) with white type preserved. Corner radius is `{rounded.sm}` (8px) — clearly interactive without drifting into pill territory.

**`button-secondary`** — Brand-blue (#3483ac) fill with white type, matching the height and geometry of `button-primary`. Appears on supporting CTAs within the quote flow, category-page navigation actions, and "View Details" prompts on product listings. Active state shifts to `{colors.brand-blue-active}` (#286585).

**`button-ghost`** and **`button-ghost-blue`** — Transparent fill with a 2px solid border, in either `{colors.primary}` red or `{colors.brand-blue}`. Used for optional or supplementary actions — "See Samples," "Learn More," "Download Template" — that should not compete visually with the primary CTA. Both share the same 44px height and `{rounded.sm}` radius.

### Inputs and Forms

**`text-input`** — 44px tall with a `{rounded.sm}` corner and a `{colors.hairline}` (#eeeeee) default border that transitions to `{colors.brand-blue}` on focus. Placeholder text in `{colors.muted}`. Brown-Regular at 16px for legibility across dense spec forms.

**`select-input`** — Identical geometry and focus behavior to `text-input`. Quantity pickers, size selectors, paper-weight dropdowns, and finish options throughout the quote calculator all use this variant. A Font Awesome chevron icon anchors the trailing edge.

**`quote-calculator`** — A `{colors.surface-soft}` panel with `{rounded.md}` corners and a hairline border, containing stacked `select-input` fields for product specifications. The computed per-unit and total price renders in `{typography.quote-price}` (32px Brown-Bold) in `{colors.primary}` red, updating as selections change. The "Get a Quote" or "Add to Cart" button is always `button-primary`, pinned at the panel's bottom edge.

**`file-upload-zone`** — A `{colors.surface-blue}` wash field with a 2px dashed `{colors.brand-blue}` border and a centered Font Awesome upload glyph above the drop prompt text in `{typography.body-sm}`. Accepts PDF, AI, EPS, and PSD artwork files for prepress. Corner radius `{rounded.md}` (12px). On mobile it becomes a tappable button that opens the system file picker.

### Navigation

**`nav-bar-top-strip`** — A 36px-tall `{colors.primary}` red announcement bar sitting above the main nav, used for shipping promotions ("Free Shipping Over $99"), turnaround callouts, and seasonal offers. Type is Brown-Regular caption-weight in white.

**`nav-bar`** — Deep navy (#002e47) background, full-width, 60px tall. Product category links render in Brown-Bold 14px white. A search field and account/cart icons anchor the right side. The Fireball logo mark (flame + wordmark) sits left at approximately 130px wide. No border-bottom — the navy itself provides sufficient separation from the blue-wash page canvas.

### Product and Catalog

**`product-card`** — White card with a 1px `{colors.hairline}` border, `{rounded.md}` corners, and a 4:3-ratio product thumbnail. Title in `{typography.title-md}` (18px Brown-Bold), starting price in `{typography.price-display}` (24px Brown-Bold), and a short descriptor line in `{typography.body-sm}`. A `category-badge` chip sits over the image corner to flag product type (Business Cards, Banners, Apparel). Hover state applies a subtle drop shadow without layout shift.

**`category-badge`** — A small all-caps chip in `{colors.accent-yellow}` (#fae351) with dark ink type, used for the most prominent product category flag. `category-badge-green` uses `{colors.accent-green}` for eco and recycled stock products. `category-badge-blue` uses `{colors.brand-blue}` for digital or specialty printing categories. All three share `{rounded.xs}` (4px) corners and `{typography.badge-label}` (11px uppercase Brown-Bold).

**`turnaround-badge`** — Amber `{colors.accent-amber}` (#dc9600) chip in the same geometry as category badges, appearing on product cards or listing rows to signal rush or next-day turnaround availability. White type in `{typography.badge-label}`.

**`paper-swatch-chip`** — A spec-selector chip for paper stock, finish, or material options. Default border is `{colors.hairline}` (hairline gray); selected state flips to a 2px solid `{colors.primary}` (red) border to confirm the active choice. Label in Brown-Regular 13px (`{typography.spec-label}`). On desktop product configuration pages, a horizontal row of these chips replaces dropdown selects, giving customers a tactile visual comparison at a glance.

### Order Flow

**`order-steps`** — A horizontal step-indicator bar tracking the active order stage (Configure → Upload Artwork → Proof → Checkout). Active step node fills `{colors.primary}` red; completed steps fill `{colors.accent-green}` green; future steps remain `{colors.hairline}` gray. Connector lines are 2px wide and change color to match the completed state as the user progresses. Step labels use `{typography.caption}` (12px Brown-Regular).

### Hero

**`hero-banner`** — Full-width navy (#002e47) section, minimum 420px tall. Headline in `{typography.display-xl}` (40px Brown-Bold, white), subhead in `{typography.body-md}` (Brown-Regular, white at ~80% opacity). The primary CTA (`button-primary`) sits below. Optional background: a halftone overlay or print-press photography at low opacity ensures text remains legible across all viewport widths.

### Footer

**`footer`** — Matches the nav-bar navy (#002e47). Four-column link grid: Products, Services, Turnaround Options, Help & Support. Column headers in Brown-Bold 16px white (`{typography.title-sm}`); links in Brown-Regular 14px at `{colors.surface-blue}` (light blue, readable against dark ground). A thin `{colors.hairline-soft}` rule separates the link grid from a bottom bar carrying legal links, social icons (Font Awesome Brand set), and the Fireball wordmark.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger menu replaces full nav-bar; quote calculator stacks vertically and anchors as a bottom-sheet; paper-swatch-chip rows scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; nav-bar collapses secondary category links into a "More" dropdown; hero-banner reduces to 320px tall; quote calculator sidebar collapses inline |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav-bar visible; quote calculator persists as a sticky sidebar widget on product configuration pages |
| Wide | > 1440px | Content grid max-width 1440px, centered with {spacing.section} gutters; nav and footer content remain within the 1440px container |

### Touch Targets

- All buttons maintain a minimum 44px height to meet touch-target minimums on mobile
- `paper-swatch-chip` invisible padding expands tap area to 44×44px even when the visible chip is smaller
- Nav-bar hamburger trigger and icon buttons are minimum 44×44px tap zones
- `file-upload-zone` fills full column width on mobile; a prominent "Tap to Upload" label replaces the desktop drag-and-drop instructions

### Collapsing Strategy

- Nav collapses to a hamburger icon at < 744px; product categories appear in an off-canvas left drawer with `{colors.brand-navy}` background
- `quote-calculator` transitions from a persistent sidebar widget (desktop) to a bottom-sheet drawer triggered by a sticky "Configure & Price" button that floats above the mobile viewport
- Hero headline reduces from `{typography.display-xl}` (40px) to `{typography.display-md}` (28px) below 744px; subhead shifts from `{typography.body-md}` to `{typography.body-sm}`
- Footer collapses from four columns to single-column accordion at < 744px; each column header becomes a tap-to-expand trigger with a Font Awesome chevron indicator
- `nav-bar-top-strip` is hidden below 744px if the banner message is non-critical; retained for active promotions

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color was extracted; mobile status-bar color assumed from `{colors.brand-navy}` (#002e47) — verify against actual device rendering
- Brown is a licensed Lineto typeface; the web-font loading mechanism (self-hosted vs. CDN, WOFF2 subset) and whether a Brown Light weight is in use for any body context were not detectable from static extraction — confirm before implementation
- Font Awesome variants 5 and 6 (Regular, Pro, Duotone, Sharp, Brands) were all detected; the specific subset and style class conventions used for product UI icons versus decorative icons are not distinguished — map icon usage to style classes before building the icon system
- Exact box-shadow values for card hover states, modal backdrops, and the sticky quote-calculator on scroll were not extractable from color data alone — infer from visual inspection or request from brand
- Animation and transition timing is absent; a print-catalog UI typically uses 150–200ms ease-out transitions — treat as defaults until a motion spec is confirmed
- The green accent range (#76ae31, #b4dc82, #9cd15a) and amber (#dc9600) usage contexts — whether green signals eco stock, a product category, or a promotional state — could not be confirmed from extraction alone; validate against live product catalog
- Dark-mode support, if any, is unconfirmed; the deep navy surface suggests a dark-variant palette may exist but was not validated
