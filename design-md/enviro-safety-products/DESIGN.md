---
version: alpha
name: "Enviro Safety Products"
source_url: "https://www.envirosafetyproducts.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Safety orange—#ff6128—doesn't moonlight as a brand color here; it is the raw signal color of hard-hat zones and high-visibility vests, worn without irony across every primary CTA, site header stripe, and promotional ribbon. Enviro Safety Products runs Barlow as its workhorse typeface: condensed, utilitarian, and legible at small sizes, which suits a catalogue where SKU labels, compliance certifications, and bulk-pricing tiers compete for vertical space on a dense product grid. A deep teal (#108474) anchors secondary actions, category navigation markers, and informational callouts, creating a two-signal system with the orange — #ff6128 means buy or act, #108474 means navigate or learn. The background hierarchy is warmer than most industrial ecommerce: #f7f4f2 off-white sits beneath cards, #f9fafb near-white serves as page canvas, while #262626 near-black handles primary ink — readable against both tones without needing heavy text shadows or outlines. Alert logic borrows from OSHA's own color grammar: a cluster of greens (#00aa00, #00a500, #008a00) signals in-stock status and order-success states, while #ea0202 flags out-of-stock and validation errors; procurement buyers already know this system and the brand doesn't have to teach it. Corner rounding stays at `{rounded.xs}`–`{rounded.sm}` on buttons and inputs — 4 to 8px — preserving a functional register that avoids the soft pill shapes of consumer DTC. Category tiles use dark navy (#121f36) as background fields so product photography and icon sets emerge with snap, separate from the primary orange system. Poppins enters as a counterweight to Barlow's density: reserved for trust-block headlines and longer-form reassurance copy where the brand needs to speak credibility rather than catalogue. The teal-light surfaces (#e6f7f4 and #edf5f5) back informational banners and feature callouts, maintaining legibility without pulling the eye away from primary conversion paths.

colors:
  primary: "#ff6128"
  primary-active: "#d94f1f"
  primary-disabled: "#ffb898"
  teal: "#108474"
  teal-active: "#0c6a5d"
  teal-soft: "#e6f7f4"
  teal-surface: "#edf5f5"
  ink: "#262626"
  body: "#4a4a4a"
  muted: "#8a9297"
  muted-mid: "#7b7b7b"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  hairline-faint: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f7f4f2"
  surface-card: "#f9fafb"
  surface-mid: "#f7f7f7"
  on-primary: "#ffffff"
  on-teal: "#ffffff"
  navy: "#121f36"
  navy-dark: "#171722"
  link: "#007aff"
  success: "#00aa00"
  success-alt: "#00a500"
  success-dark: "#155724"
  success-surface: "#d4edda"
  success-border: "#c3e6cb"
  error: "#ea0202"
  meta-border: "#b1b7c3"
  mid-gray: "#999ea8"

typography:
  display-xl:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-label:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-lg:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-md:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  mono:
    fontFamily: "monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    hoverBackgroundColor: "{colors.primary-active}"
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
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-teal:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.on-teal}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    hoverBackgroundColor: "{colors.teal-active}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
    placeholderColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    iconColor: "{colors.primary}"
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    height: 48px
  nav-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    topStripBackgroundColor: "{colors.primary}"
    topStripTextColor: "{colors.on-primary}"
    topStripTypography: "{typography.caption-label}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    columnHeadColor: "{colors.teal}"
    columnHeadTypography: "{typography.title-sm}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    badgeBackgroundColor: "{colors.primary}"
    badgeTextColor: "{colors.on-primary}"
    badgeTypography: "{typography.badge}"
    hoverShadow: "0 4px 12px rgba(0,0,0,0.10)"
  category-tile:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.on-primary}"
    hoverBackgroundColor: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"
  safety-badge:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.on-teal}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  stock-badge-in:
    backgroundColor: "{colors.success-surface}"
    textColor: "{colors.success-dark}"
    borderColor: "{colors.success-border}"
    border: "1px solid {colors.success-border}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  stock-badge-out:
    backgroundColor: "#fff0f0"
    textColor: "{colors.error}"
    border: "1px solid #f5c6cb"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  promo-ribbon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-label}"
    padding: "{spacing.sm} {spacing.base}"
  trust-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    iconColor: "{colors.teal}"
    padding: "{spacing.lg}"
  alert-info:
    backgroundColor: "{colors.teal-soft}"
    textColor: "{colors.teal}"
    border: "1px solid {colors.teal}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md}"
  alert-success:
    backgroundColor: "{colors.success-surface}"
    textColor: "{colors.success-dark}"
    border: "1px solid {colors.success-border}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md}"
  alert-error:
    backgroundColor: "#fff0f0"
    textColor: "{colors.error}"
    border: "1px solid #f5c6cb"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md}"
  hero-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    minHeight: 400px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "{colors.canvas}"
    inactiveTextColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.button-sm}"
    minSize: 44px
  footer:
    backgroundColor: "{colors.navy-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    linkColor: "{colors.hairline-soft}"
    linkHoverColor: "{colors.primary}"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — Safety orange (#ff6128) fill, white Barlow semi-bold type, 4px radius, 44px height. This is the dominant purchase trigger: "Add to Cart", "Buy Now", quantity confirm. Active/hover shifts to #d94f1f; disabled drains to pale #ffb898. The color's industrial connotation — cones, hard hats, high-visibility tape — means it reads as urgent without requiring heavy copy support.

**`button-secondary`** — White fill with a 2px orange border and orange type, matching primary in height and rounding. Used for secondary purchase paths such as "Add to Quote", "Request a Sample", or alternate quantity selectors. On hover the border deepens to match primary-active.

**`button-teal`** — Deep teal (#108474) fill with white type, same scale as primary. Reserved for informational CTAs — "View Spec Sheet", "Download SDS", "Learn More" — where the orange primary would overstate purchase urgency. The teal communicates navigate rather than buy.

**`button-ghost`** — Transparent fill, 1px hairline border, ink text. Used for tertiary surface-level actions: pagination anchors, "Back to Results", table sort toggles, and modal dismiss controls.

### Search

**`search-bar`** — Full-width 48px input with 4px radius, hairline rest state border, and a 2px orange focus ring. Right edge holds an orange-background submit button with a magnifier icon in white. On mobile the bar collapses to an icon tap that expands into a full-width overlay with the keyboard raised.

### Navigation

**`nav-bar`** — Two-tier layout. The upper tier is a narrow orange (#ff6128) announcement strip at page top carrying promo copy or free-shipping thresholds in all-caps caption-label white type. The lower tier is dark navy (#121f36), holding the logo on the left, search bar center, and cart/account icons on the right — all in white. Below the desktop breakpoint the nav collapses to a hamburger that opens a full-height slide-in drawer.

**`mega-menu`** — Drops below the navy bar on category hover. White canvas with column groups headed in teal Barlow title-sm; subcategory links in Poppins body-sm ink. A right-side feature panel holds a promoted product or certification callout with image tile and button-teal CTA.

### Product Card

**`product-card`** — White card, 1px hairline border, 4px radius, 12px padding. Title in Barlow title-sm (ink); price in Barlow price-md (ink, bold). An orange badge sits top-left for SALE or NEW flags using all-caps badge typography. A stock badge sits beneath price: green-tinted `stock-badge-in` or red-tinted `stock-badge-out`. On hover the card lifts 4px with a 12px diffuse shadow.

### Category Tile

**`category-tile`** — Navy (#121f36) background tile with centered product-category icon and white Barlow title-sm label beneath. On hover the fill transitions to primary orange with white type retained. Homepage category grid runs 6–8 tiles per row on desktop, 4 on tablet, 2 on mobile.

### Badges

**`safety-badge`** — Teal (#108474) background, white all-caps badge type, 4px radius. Applied on product pages and PDPs to signal compliance certifications: ANSI/ISEA, OSHA compliant, NIOSH approved, UL Listed. Multiple badges stack horizontally.

**`stock-badge-in`** / **`stock-badge-out`** — Inline status chips in OSHA-idiom colors. In-stock: pale green (#d4edda) fill, dark green (#155724) text with a green border. Out-of-stock: pale red fill, #ea0202 text. Both use caption typography and 4px radius for compact inline placement.

**`promo-ribbon`** — Full-width orange bar immediately below the nav or at the top of a page section. All-caps caption-label type in white. Carries sitewide discount codes, free-shipping thresholds, or limited-time offers.

### Trust Block

**`trust-block`** — Off-white (#f7f4f2) horizontal strip, typically three or four icon+headline+body triads covering fast shipping, hassle-free returns, and certified-safety sourcing. Icons render in teal; headlines in Barlow title-sm ink; body copy in Poppins body-sm. Appears above the footer on PDPs and cart pages to reassure procurement buyers before checkout.

### Alerts

**`alert-info`** — Teal-tinted surface (#e6f7f4), 1px teal border, Poppins body-sm teal text. Used for shipping lead-time notices, compliance notes, and regulatory callouts. No icon required; left-border accent alone establishes the tone.

**`alert-success`** / **`alert-error`** — Green-surface and red-surface variants that maintain the OSHA-derived color grammar consistent with the stock badges, reinforcing visual coherence across the purchase flow.

### Hero Banner

**`hero-banner`** — Dark navy (#121f36) or dark image-overlay field; Barlow display-xl headline in white; display-sm subhead; a primary orange CTA button anchored lower-left. Min-height 400px on desktop, 280px on mobile. A secondary teal-backed category-chip strip often runs immediately below the hero image to drive catalogue entry.

### Footer

**`footer`** — Near-black navy (#171722) background; column-structured links in off-white Barlow body-sm; section headings in title-sm. A 3px orange top border separates the footer from the page content directly above it. Link hover state transitions to primary orange, tying footer interactivity back to the main brand voltage.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | 1-column product grid; nav collapses to hamburger with full-height slide-in drawer; search expands to full-width overlay; hero min-height 280px; category tiles 2-up grid; trust block stacks vertically; promo ribbon single truncated line |
| Tablet | 744–1128px | 2–3 column product grid; nav retains promo strip and logo but hides secondary links; mega-menu becomes accordion inside drawer; hero min-height 340px; category tiles 4-up |
| Desktop | 1128–1440px | Full two-tier nav with hover mega-menu; 4-column product grid; hero full-bleed with text column constrained to 720px; trust block 4-icon horizontal row; breadcrumb visible |
| Wide | > 1440px | Content max-width 1440px centered; product grid extends to 5-up; hero background spans full viewport width with content at max-width container |

### Touch Targets

- All tappable elements minimum 44×44px
- Nav hamburger icon padded to 44×44px hit area
- Product card CTA buttons expand to full card width on mobile
- Pagination buttons minimum 44px square
- Form inputs minimum 44px height
- Category tiles minimum 80px height on mobile for thumb-friendly tapping

### Collapsing Strategy

- Primary nav collapses at <1128px to condensed link set, then hamburger drawer at <744px
- Mega-menu converts to stacked accordion inside the mobile drawer
- Category tile grid: 8-up → 4-up → 2-up across breakpoints
- Product grid: 4-up → 3-up → 2-up → 1-up
- Trust block row: horizontal 4-icon → 2×2 grid → vertical stack
- Hero text column: 50% width → 70% → full-width as viewport narrows
- Footer columns: 4-up → 2-up → 1-up stacked on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border-radius not directly observed from extraction; 4px (`{rounded.xs}`) inferred from the brand's industrial register and common Shopify theme defaults
- No custom icon set specifications confirmed; likely a licensed icon library or bundled Shopify theme glyphs — SVG size and stroke weight unknown
- JudgemeStar font detected (Judge.me review widget) but no review-specific star typography or rating-display scale defined
- Barlow variant distribution (Condensed vs. Regular vs. SemiCondensed) not confirmed from extraction; Regular assumed for body, Semi-Bold/Bold for headings
- Exact nav bar height and sticky scroll behavior not confirmed; 56px estimated from common two-tier Shopify patterns
- Specific per-category PDP templates (gloves vs. respirators vs. eyewear) may use distinct badge or color logic not captured here
- Animation and transition timing values (hover duration, drawer slide speed) not extractable from static extraction
- No dark mode or high-contrast accessibility mode observed
- Bulk/quote pricing table styles not captured; likely a bespoke component for B2B procurement flows
