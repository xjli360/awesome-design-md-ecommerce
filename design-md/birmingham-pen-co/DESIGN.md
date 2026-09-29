---
version: alpha
name: "Birmingham Pen Co."
source_url: "https://www.birminghampens.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The first color you encounter on birminghampens.com reads less like a brand choice and more like a well-shaken bottle of iron gall ink — #b74038, a deep brick-crimson that sits closer to oxidized copper than fire-engine red, carrying the warmth of Birmingham's metalworking heritage into every primary CTA and hover state. Young Serif handles all display work at normal weight, bringing an unhurried editorial gravity to pen names and collection headers that conjures the pleasure of a hand-typeset broadside; Figtree runs the interface layer — nav links, body copy, price strings, filter pills — as a clean geometric sans that keeps commerce legible without competing with the serif's personality. The canvas is #fafaf6, a warm off-white that reads like quality laid paper rather than a screen default, while the near-black body sits at #2e2e28, noticeably brown-tinted rather than neutral — a detail that makes text feel inked rather than printed. A secondary voltage, amber #ffb503, surfaces on sale badges and highlight moments; the color of brass nibs and sealing wax, it signals warmth and craft rather than markdown urgency. Corners stay deliberately modest: {rounded.xs} (4px) on buttons and inputs, {rounded.sm} (8px) on cards — precise enough to suggest hand-finishing, nothing so round it reads as consumer-app. Ink swatches render as small filled circles ({rounded.full}) with a thin hairline ring on hover, giving the catalog its most distinctive UI moment: a row of ink puddles, each named. The overall register is workshop-serious: a brand that names products plainly, photographs them on the warm canvas without lifestyle staging, and trusts the objects themselves to close the sale. No gradients, no neon, no hero text overlaid on lifestyle imagery — just objects, light, and two fonts working in deliberate contrast.

colors:
  primary: "#b74038"
  primary-active: "#9a2e27"
  primary-disabled: "#d99490"
  accent: "#ffb503"
  accent-active: "#e0a000"
  accent-on: "#2e2e28"
  error: "#d72c0d"
  ink: "#2e2e28"
  body: "#131313"
  muted: "#6b6b65"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#fafaf6"
  surface-soft: "#f4f6f8"
  surface-card: "#ffffff"
  on-primary: "#fafaf6"
  on-dark: "#fafaf6"

typography:
  display-xl:
    fontFamily: "'Young Serif', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Young Serif', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Young Serif', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Young Serif', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "'Figtree', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-lg:
    fontFamily: "'Figtree', system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Figtree', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Figtree', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Figtree', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Figtree', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  label-uppercase:
    fontFamily: "'Figtree', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
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
    padding: 13px 24px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 23px
    height: 46px
    border: "1.5px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.primary}"
    padding: 12px 23px
    height: 46px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.ink}"
    padding: 10px 14px
    height: 44px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
    logoColor: "{colors.ink}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: "1 / 1"
    imageFit: contain
    imageBackground: "{colors.canvas}"
    padding: "{spacing.md}"
    gap: "{spacing.sm}"
  product-card-badge-sale:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-on}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 7px
  product-card-badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 7px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 520px
    padding: "{spacing.section} {spacing.xl}"
    ctaGap: "{spacing.md}"
  ink-swatch:
    width: 28px
    height: 28px
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.hairline}"
    hoverBorder: "2px solid {colors.ink}"
    hoverScale: 1.15
    tooltipTypography: "{typography.caption}"
    tooltipBackground: "{colors.ink}"
    tooltipColor: "{colors.on-dark}"
    tooltipRounded: "{rounded.xs}"
  ink-swatch-row:
    gap: "{spacing.sm}"
    display: flex
    flexWrap: wrap
    marginTop: "{spacing.sm}"
  collection-filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
  collection-filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.ink}"
  section-label:
    textColor: "{colors.muted}"
    typography: "{typography.label-uppercase}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.sm}"
    marginBottom: "{spacing.lg}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    gap: "{spacing.xs}"
  quantity-stepper:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    buttonSize: 36px
    width: 108px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-sm}"
    subtotalTypography: "{typography.title-md}"
    borderLeft: "1px solid {colors.hairline}"
    width: 400px
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark}"
    linkOpacity: 0.7
    linkHoverOpacity: 1
    padding: "{spacing.xxl} 0"
    borderTop: none

## Components

### Buttons

**`button-primary`** — Solid brick-crimson (#b74038) fill with warm off-white text, 4px radius, 46px tall. The hover state deepens to #9a2e27 with no transition delay, giving a crisp press feel. Disabled state washes to #d99490 with the same radius and no cursor change beyond the browser default. Use for all primary purchase actions: Add to Cart, Checkout, Subscribe.

**`button-secondary`** — Warm canvas background with a 1.5px ink-colored border and ink text, matching the primary button's dimensions exactly so the two can sit side-by-side without optical imbalance. Hover darkens the border to match the active ink tone. Use for secondary navigation within flows (Continue Shopping, View Full Collection).

**`button-ghost`** — Transparent background with a 1.5px primary-crimson border and matching text. Appears on product detail pages alongside the primary CTA to offer a secondary action (e.g., Add to Wishlist) without competing for visual weight. On hover the border thickens to 2px.

### Text Input

**`text-input`** — White surface card background, 1px hairline border (#dedede), 4px radius. On focus the border steps to 1.5px ink (#2e2e28), giving a clean activation signal without color. Placeholder text uses the muted tone (#6b6b65). Height is fixed at 44px to align cleanly with nav and stepper elements.

### Navigation

**`nav-bar`** — Warm canvas background, 64px tall, separated from content by a single hairline bottom border. The wordmark renders in Young Serif at display-sm scale (22px, weight 400) — the only place the brand name appears in the serif face within chrome. Nav links use Figtree nav-link (15px, weight 500). Cart, search, and account icons sit at 20px in ink color.

**`announcement-bar`** — Full-width crimson band (36px tall) above the nav, reversed out in warm off-white Figtree badge type. Used for shipping thresholds, new ink launches, and limited edition notices. Sits at the very top of the page hierarchy.

### Product Card

**`product-card`** — White card with a soft hairline border on a canvas grid, 8px radius. Product images use 1:1 aspect ratio on the canvas background color so ink bottles and pen bodies float rather than crop. The product name renders in Figtree title-sm (15px, semibold); price sits below in Figtree price (16px, semibold). Sale badges ({product-card-badge-sale}) appear absolute-positioned to the top-left in amber #ffb503 with ink text; New badges appear in the same position in ink with reversed-out text.

### Hero Banner

**`hero-banner`** — Dark ink (#2e2e28) field with a minimum height of 520px, allowing full-bleed product or atmospheric photography to underpin the text layer. The heading runs in Young Serif display-xl (48px); the subhead in Figtree body-md. Two CTA buttons sit below with a 12px gap — typically one primary (crimson) and one ghost (crimson outline). Padding is generous at 64px vertical to let the serif heading breathe.

### Ink Swatches

**`ink-swatch`** / **`ink-swatch-row`** — The most brand-specific UI component: small 28px circles filled with the actual ink color, arranged in a flex row with 8px gaps. Each swatch carries a 1.5px hairline ring that steps to a 2px ink ring on hover, and scales to 1.15× so color can be examined without a tooltip. A tooltip ({typography.caption}, ink background) appears on hover or focus with the ink's proper name. On the product detail page this row replaces a standard color-option select.

### Collection Filters

**`collection-filter-pill`** / **`collection-filter-pill-active`** — Pill-shaped filter controls using Figtree button-sm. Inactive state is surface-soft (#f4f6f8) with hairline border; active inverts to ink fill with reversed-out text. The pill shape ({rounded.full}) is the only place the brand uses a fully-rounded form — all other interactive elements use xs (4px) radius — creating a clear visual grammar: pills are filters, rectangles are actions.

### Section Label

**`section-label`** — Uppercase Figtree at 11px, weight 600, 1px letter-spacing in muted (#6b6b65), with a single hairline bottom rule. Used to head collection grid sections (Featured Inks, New Arrivals, Pen Kits) and product page detail groups (Ink Properties, In the Box). Provides structure without competing with the Young Serif display headings.

### Cart Drawer

**`cart-drawer`** — 400px slide-in panel from the right edge, canvas background, separated from page content by a 1px hairline border. Heading in Young Serif display-sm (22px); subtotal line in Figtree title-md (18px, semibold). Line items use body-sm. The primary button runs full-width at the bottom of the drawer in primary crimson.

### Footer

**`footer`** — Ink-colored (#2e2e28) full-width footer with reversed-out Figtree body-sm links at 70% opacity, stepping to full opacity on hover. Column headings use Figtree title-sm at full on-dark color. No top border — the dark field creates its own visual break from the canvas content above. Padding is 48px vertical.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + cart icon; hero heading steps down to display-md (28px); announcement bar wraps to two lines if needed; ink-swatch-row wraps freely; collection filter pills scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links, hides secondary; hero heading at display-lg (36px); cart drawer full-height; filter pills remain in-line |
| Desktop | 1128–1440px | Three or four-column product grid; full nav with all links visible; hero at display-xl (48px) with side-by-side CTAs; cart drawer at fixed 400px |
| Wide | > 1440px | Grid max-width capped at ~1280px, centered on canvas; hero content max-width ~900px; type sizes unchanged |

### Touch Targets

- All buttons minimum 44px tall × 44px wide
- Ink swatches expand hit area to 44×44px via padding even though the visible circle is 28px
- Nav hamburger icon hit area minimum 44×44px
- Collection filter pills minimum 36px tall with generous horizontal padding; scroll container has momentum scrolling on iOS

### Collapsing Strategy

- Primary navigation collapses at 744px to a slide-in drawer triggered by a hamburger icon; the wordmark stays centered with the cart icon right-aligned
- Product grid collapses from four → three → two → one columns at 1440 → 1128 → 744 → 375px
- Ink swatch rows that overflow the container scroll horizontally on mobile rather than wrapping to a second line, preserving the single-row visual grouping
- Hero CTAs stack vertically (primary above secondary) below 744px
- Footer columns collapse from four-column to two-column at 744px and single-column at 480px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed border-radius values from the live site; xs (4px) and sm (8px) are inferred from the brand's precision aesthetic, not extracted measurements
- Font weights for Young Serif could not be confirmed from extraction — the face is typically weight 400 only; if additional weights are loaded, adjust display-xl and display-lg accordingly
- Hover and transition timing (duration, easing) not extractable; defaults of 150ms ease are assumed for color transitions and 200ms for transforms
- Exact nav height (64px) is estimated; actual measured value may differ
- No confirmed shadow values; product cards are assumed to use border-only elevation rather than box-shadow
- Secondary palette colors (#d72c0d, #f9423a, #f1e04d) appear in extracted data but their roles (error states, promotional callouts, in-stock badges) could not be confirmed — error (#d72c0d) assigned cautiously
- Several extracted hex values (#008060, #35ee7a, #049cff, #d1d5db, #f4f6f8) are standard Shopify admin UI chrome colors and have been excluded from the brand palette; they do not represent Birmingham Pen Co.'s design intent
- Cart drawer width and behavior (drawer vs. modal vs. page redirect) is an assumption based on common Shopify Dawn-derived theme patterns
