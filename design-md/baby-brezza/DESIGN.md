---
version: alpha
name: "Baby Brezza"
source_url: "https://babybrezza.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Warm greiges and charcoal-tinted grays — a palette running from #bcb2a8 through #62605d down to #303030 — form the environmental backdrop rather than a pediatric-primary palette, signaling that Baby Brezza is marketing to design-conscious parents who live in neutral-toned homes. The true brand voltage arrives via #006fba, a saturated utility blue that carries every add-to-cart button, primary CTA, and active nav element. Work Sans handles all typography — a geometric sans-serif that reads as modern and approachable without the clinical coldness of Inter or the retro warmth of Futura; at title weights (600) it has enough mass to anchor product names across the Formula Pro Advanced and Sterilizer categories, while at body weight (400) it stays legible at small sizes for instruction-dense product detail pages.

  Three secondary accents surface in the extraction: #308ac7 (a lighter blue for hover states and secondary actions), #6c69de (a blue-violet that appears on promotional badges and bestseller callouts), and #559b60 (a green reserved for in-stock indicators and trust or eco badges). Error states run through #d63a2f and #a60f00, giving form validation enough visual weight without alarming the parent-purchaser mid-checkout. The surface system layers white (#ffffff) canvas beneath soft warm hairlines (#cfcfcf, #dedede) and card surfaces (#ebebeb), giving lifestyle photography on warm beige backgrounds space to breathe without harsh contrast shifts.

  Rounded corners sit at a friendly `{rounded.sm}` (8px) for cards and inputs — soft enough to read as safe for a baby-product context — while buttons step up to `{rounded.md}` (12px) for a pill-adjacent shape that stops short of fully circular. The nav runs at full white with a bottom hairline and collapses to a hamburger-first mobile drawer on narrower viewports. Announcement bars sit above the nav in solid #006fba with white Work Sans type, carrying shipping thresholds and limited promotions. Product cards surface brief feature bullets below the price on hover, a pattern calibrated for parents who comparison-shop appliances by spec — compatible bottle count, noise decibels, self-cleaning cycles — rather than by aesthetic instinct alone.

colors:
  primary: "#006fba"
  primary-hover: "#308ac7"
  primary-active: "#005a9e"
  primary-disabled: "#99c5e3"
  ink: "#121212"
  body: "#303030"
  muted: "#62605d"
  muted-soft: "#aaaaaa"
  hairline: "#cfcfcf"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#ebebeb"
  surface-card: "#ffffff"
  surface-warm: "#c6c3bd"
  on-primary: "#ffffff"
  accent-violet: "#6c69de"
  accent-green: "#559b60"
  error: "#d63a2f"
  error-dark: "#a60f00"
  warm-mid: "#bcb2a8"
  warm-dark: "#5d5853"

typography:
  display-xl:
    fontFamily: "'Work Sans', system-ui, -apple-system, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Work Sans', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "'Work Sans', system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Work Sans', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Work Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Work Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Work Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Work Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Work Sans', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'Work Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Work Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  badge:
    fontFamily: "'Work Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  label:
    fontFamily: "'Work Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
    textTransform: uppercase
  price:
    fontFamily: "'Work Sans', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Work Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  announcement:
    fontFamily: "'Work Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.2px

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
    rounded: "{rounded.md}"
    padding: 13px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 27px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1.5px solid {colors.primary-active}"
    rounded: "{rounded.md}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoHeight: 36px
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    fontWeight: 600
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.announcement}"
    padding: 8px 16px
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderRadius: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.primary}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.muted}"
    padding: "{spacing.base}"
    hoverBorder: "1px solid {colors.hairline}"
    hoverBackground: "{colors.surface-soft}"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-bestseller:
    backgroundColor: "{colors.accent-violet}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-instock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted}"
    padding: "{spacing.section} {spacing.xl}"
    ctaVariant: "button-primary"
  feature-strip:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    iconColor: "{colors.primary}"
    typography: "{typography.label}"
    padding: "{spacing.lg} 0"
    itemGap: "{spacing.xl}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    border: "1px solid {colors.hairline}"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    borderRadius: "{rounded.full}"
    iconColor: "{colors.muted-soft}"
    iconColorFocus: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: 10px 20px
    height: 44px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.canvas}"
    headerTypography: "{typography.title-md}"
    headerColor: "{colors.ink}"
    borderLeft: "1px solid {colors.hairline}"
    itemTypography: "{typography.body-sm}"
    itemColor: "{colors.body}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.ink}"
    width: 400px
    ctaVariant: "button-primary"
  trust-badge:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    iconColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  rating-stars:
    activeColor: "{colors.primary}"
    inactiveColor: "{colors.hairline}"
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    height: 40px
    buttonWidth: 40px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.hairline}"
    linkColor: "{colors.muted-soft}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — The primary call-to-action runs #006fba at 48px height with Work Sans 600/15px and 12px corner radius (`{rounded.md}`). On hover it lightens to #308ac7; on active press it deepens to #005a9e. The disabled state fills with #99c5e3, preserving the button shape so parents scanning a checkout flow can still read the control even when it is temporarily inactive.

**`button-secondary`** — An outlined variant with a 1.5px #006fba border on a white fill carries secondary actions such as "Learn More" on feature modules and "View All" on category grids. Hover adds a soft #ebebeb background fill to signal interactivity without competing with the primary CTA nearby.

**`button-ghost`** — Transparent-background ghost buttons (Work Sans 600/13px, `{rounded.sm}`) appear in nav drawers and accordion footers for low-priority navigation like "See All" or "Back". No border, no fill — used only where hierarchy demands the lightest visual footprint.

### Navigation

**`nav-bar`** — A 64px white header with a 1px #cfcfcf bottom hairline. Logo sits at 36px height flush left; desktop shows category links in Work Sans 500/14px spread horizontally; cart, account, and search icons cluster right. The active category link shifts to #006fba at weight 600 with no underline or pill indicator — color alone carries the state.

**`announcement-bar`** — A 36px bar above the nav filled solid #006fba with white Work Sans 500/13px copy announcing free-shipping thresholds or time-limited promotions. A dismissible chevron sits right-aligned. This bar is the only element where primary blue occupies full-width real estate — everywhere else it is reserved for buttons and accents.

### Search

**`search-bar`** — A pill-shaped (`{rounded.full}`) field with an #ebebeb fill and 1px #cfcfcf border. The search icon is #aaaaaa at rest and flips to #006fba on focus alongside the border. On desktop the bar collapses to an icon trigger in the nav; expanding it on click opens a full-width overlay with real-time suggestions.

### Product Cards

**`product-card`** — White cards with 1px #dedede border and 8px radius hold a square product image on an #ebebeb image-well. Below: product name in Work Sans 600/16px (#121212), a 1–2 line feature callout in Work Sans 400/14px (#62605d), price in Work Sans 600/16px (#006fba), then a `button-primary`. On hover the card border strengthens to #cfcfcf and the image-well background lightens with the `{colors.surface-soft}` fill.

**`badge-sale`** — #d63a2f rectangle with 4px radius, uppercase Work Sans 700/11px in white. Positioned top-left over the product image, never stacked with other badges.

**`badge-bestseller`** — Same geometry in #6c69de. Applied to top-selling SKUs in category grids and on the PDP below the product title.

**`badge-new`** — #006fba fill on the same badge shape marks newly launched products. Sits adjacent to `badge-bestseller` when both apply, ordered new → bestseller left to right.

**`badge-instock`** — #559b60 fill used as a "ships today" or in-stock assurance chip on the product detail page below the price row.

### Hero

**`hero-banner`** — Full-width split-column section: #ebebeb background left column holds headline in Work Sans 700/40px, subhead in Work Sans 400/16px (#62605d), and a single `button-primary`. Right column carries lifestyle photography — typically a device plus infant against a warm beige/cream environment — with no overlay or gradient. The two columns coexist at equal visual weight rather than the photography dominating behind text.

### Feature Strip

**`feature-strip`** — A warm #c6c3bd band placed between the hero and the product grid carries 3–4 icon-plus-label pairs (free shipping, 2-year warranty, BPA-free, easy returns) spaced 32px apart. Icons are #006fba at 24px; labels are uppercase Work Sans 600/12px in #121212. This band anchors trust signals in the warm neutral palette without pulling attention from the product grid below.

### Cart

**`cart-drawer`** — A 400px right-anchored drawer on desktop (full-screen sheet on mobile) with a white background and a 1px left border in #cfcfcf. Header "Your Cart" in Work Sans 600/18px. Line items show a square thumbnail, product name in Work Sans 400/14px, and price in Work Sans 600/16px. A sticky drawer footer holds a full-width `button-primary` labeled "Checkout" and an order total summary above it in Work Sans 700/20px.

### Trust

**`trust-badge`** — Small white cards (`{rounded.sm}`, 1px #cfcfcf border) with a #006fba icon at top and a 2-line text block in Work Sans 400/12px (#62605d). Displayed in a 4-up horizontal row below product detail pages and above the footer — a persistent reminder of warranty and safety credentials.

**`rating-stars`** — Five stars using #006fba for filled and #cfcfcf for empty. Review count in Work Sans 400/14px #62605d follows inline. No separate rating number displayed at large size — the count alone carries the social-proof signal.

### Category Navigation

**`category-chip`** — Pill-shaped (`{rounded.full}`) filter tags for collection pages. Default state: #ebebeb fill, 1px #cfcfcf border, Work Sans 600/12px uppercase text in #303030. Active state: #006fba fill, white text, border removed. Chips scroll horizontally on mobile with a hidden scrollbar.

### Form Elements

**`text-input`** — 48px height, white fill, 1px #cfcfcf border at rest, 1px #006fba border on focus. Placeholder in #aaaaaa; active text in #121212. 8px radius (`{rounded.sm}`). Used in email signup blocks, account forms, and address entry at checkout.

**`quantity-selector`** — Inline stepper at 40px height: #ebebeb background, 1px #cfcfcf border, minus and plus icon buttons each 40px wide, quantity count centered in Work Sans 600/16px (#121212). Flanked on the right by the `button-primary` "Add to Cart" on the product detail page.

### Footer

**`footer`** — Dark #121212 background with white section headings in Work Sans 600/16px and #aaaaaa link text in Work Sans 400/14px. Four-column desktop layout (Shop, Support, Company, Social) collapses to a single-column accordion on mobile. A pre-footer band directly above holds an email signup `text-input` beside a `button-primary` "Subscribe" — the one instance of full-width dark-on-blue contrast in the layout.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger + logo + cart icon; hero image stacks full-width above headline text; product grid is 1–2 columns; cart drawer becomes full-screen bottom sheet; feature strip wraps to 2×2 grid; category chips scroll horizontally; footer becomes single-column accordion |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + cart + hamburger only (category links hidden); hero splits 60/40 text-to-image; feature strip stays single row of 4; cart is 360px side drawer |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with all category links visible; hero splits 50/50; cart is 400px side drawer; trust badges in 4-up row; announcement bar text left-centered with max-width cap |
| Wide | > 1440px | Content max-width ~1280px centered with background bleed; four-column product grid; hero gains horizontal padding buffer; footer column gaps widen to breathing room |

### Touch Targets
- All interactive elements maintain a minimum 44×44px tap target on mobile
- `quantity-selector` minus and plus buttons are 40px square with invisible 4px padding buffer on mobile
- Cart and hamburger icons in the mobile nav use 44px hit areas regardless of visible icon size
- Category chips have a minimum 36px touch height with 8px vertical padding to reach 44px on narrower chips

### Collapsing Strategy
- Nav collapses at 744px: the horizontal category link row is replaced by a hamburger-triggered full-screen drawer with accordion sub-categories
- Footer switches from 4-column grid to single-column accordion below 744px; each section heading becomes a tap-to-expand toggle
- Hero image moves from right-column float to full-width top block below 744px; text column becomes full-width below the image
- Category chip filter row on collection pages switches from wrapping grid to horizontally scrolling single row (overflow-x: auto, scrollbar hidden) below 744px
- Feature strip wraps to 2×2 grid below 480px with increased vertical padding between rows

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom typeface confirmed: Work Sans is extracted from the site, but specific weight extremes (whether ExtraBold/800 is used at hero scale vs. Bold/700) are unverified — defaulted to 700 for `display-xl` and 600 for title scales
- Exact nav height and logo dimensions are not derivable from color/font extraction — 64px height and 36px logo are estimates calibrated to comparable Shopify DTC storefronts
- Cart drawer width (400px) is an estimate; the actual Shopify theme drawer width may differ by theme configuration
- Feature strip background (#c6c3bd) is inferred from the warm-neutral palette cluster; the actual section may use pure white or #ebebeb
- Secondary accent usage (#6c69de violet, #559b60 green) is inferred from badge-level application patterns; exact page placement and frequency are unconfirmed
- No dark-mode evidence: meta theme-color is #ffffff and the palette shows no dark-surface system, suggesting light-only — but Shopify JS-loaded styles could add one
- Animation durations, easing curves, scroll behaviors, and hover transition timing are not extractable from color and font hints alone
- Price display format (whether sale prices use strikethrough + red, or a separate "was/now" layout) is unconfirmed from extraction data
