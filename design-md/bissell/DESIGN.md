---
version: alpha
name: "Bissell"
source_url: "https://www.bissell.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every primary CTA on bissell.com fires in the same vivid red (#fa1400) — a saturated alert-color pulled from the appliance world's safety vocabulary, placed on a cream canvas (#fcfcec) and deep-navy header bands that give it room to ignite. The site's visual logic is binary: if it asks you to act, it runs red; if it orients you within the catalog, it runs #00174d, a navy dark enough to absorb ambiguity yet retaining enough blue to read as intentional brand identity rather than inherited default. Warm amber (#fab812) surfaces in promotional callouts and limited-time badges — a golden accent that pushes urgency without collapsing into generic sale-yellow. Burnt orange (#e7772f) orbits the promotional register as secondary warmth, appearing in icon fills and hover overlays. Soft periwinkle (#92aedb) moderates the spectrum in filter chips and secondary tag rings, giving the filtering UI a lighter hand than the bold CTA register. Type is delivered entirely via system-ui — no custom web font was captured in extraction, which places the brand's visual differentiation firmly in color and product photography rather than letterform. Display headings run large and weight-heavy against the cream hero sections; body copy sits in near-black (#1a1918) on white cards for maximum contrast on appliance specification tables. Product cards use modest {rounded.sm} corners — no decorative radius, no shadow theater — signaling a brand that prioritizes legibility and conversion over visual flourish. The search bar runs {rounded.full} and sits center-header, wide enough to handle multi-word cleaning queries in one line without truncation. Navigation deploys a mega-menu with category icon glyphs above text labels; the icons carry the wayfinding load so label text can remain compact. In aggregate, the UI expresses a brand that makes useful machines: direct, high-contrast, and oriented entirely around matching a shopper to the right cleaning tool as quickly as possible.

colors:
  primary: "#fa1400"
  primary-active: "#c81000"
  primary-disabled: "#fca99f"
  brand-navy: "#00174d"
  brand-navy-active: "#001133"
  brand-navy-light: "#001e4b"
  accent-amber: "#fab812"
  accent-orange: "#e7772f"
  accent-blue-soft: "#92aedb"
  ink: "#1a1918"
  body: "#3d3c3a"
  muted: "#718096"
  hairline: "#cbd5e0"
  hairline-soft: "#e2e8f0"
  canvas: "#ffffff"
  canvas-cream: "#fcfcec"
  surface-soft: "#f7fafc"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-navy: "#ffffff"
  success: "#27ca40"
  info-bg: "#e8f4f9"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 40px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  price-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.brand-navy}"
    border: "2px solid {colors.brand-navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-navy:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.brand-navy}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "2px solid {colors.hairline}"
    borderFocus: "2px solid {colors.brand-navy}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 14px 56px 14px 20px
    height: 50px
  nav-bar-top-strip:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.caption}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: 24px 48px
    shadow: "0 4px 20px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    shadow: "0 4px 16px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.canvas-cream}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: 64px 48px
  hero-banner-navy:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-navy}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: 64px 48px
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  promo-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 14px
  filter-chip-active:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-navy}"
    border: "1px solid {colors.brand-navy}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 14px
  price-block:
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    originalPriceTypography: "{typography.price-sm}"
    originalPriceColor: "{colors.muted}"
    savingsColor: "{colors.primary}"
  rating-stars:
    filledColor: "{colors.accent-amber}"
    emptyColor: "{colors.hairline}"
    typography: "{typography.caption}"
  trust-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    iconColor: "{colors.accent-orange}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    padding: 16px 0
  category-tile:
    backgroundColor: "{colors.canvas-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.lg}"
  category-tile-hover:
    border: "1px solid {colors.accent-orange}"
  info-callout:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.brand-navy}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.accent-blue-soft}"
    padding: "{spacing.base}"
  footer:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-navy}"
    linkColor: "{colors.accent-blue-soft}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: 48px 0
  footer-bottom-bar:
    backgroundColor: "{colors.brand-navy-active}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    height: 48px

## Components

### Buttons

**`button-primary`** — The dominant CTA: #fa1400 fill with white uppercase text at 0.5px letter-spacing, 48px tall, {rounded.sm} corners. Hover shifts to `primary-active` (#c81000) without a border change. The uppercase treatment and tight radius give it an instruction-manual directness that fits a brand communicating product function rather than lifestyle aspiration.

**`button-navy`** — Used for "Add to Cart" and commitment-stage actions: #00174d fill, white uppercase text, identical height and radius to `button-primary`. The two-button system is chromatic shorthand — red means explore or compare, navy means commit to purchase.

**`button-secondary`** — White background with a 2px navy border; appears alongside primary CTAs for "Compare," "Learn More," and wishlist actions where a second option must be present but subordinate. Shares the uppercase type treatment to maintain system coherence.

### Search Bar

**`search-bar`** — Full pill ({rounded.full}), 50px tall, with a red-tinted search icon inset right. Sits center-header at roughly 540px wide on desktop. The pill shape visually separates it from the rectangular filter inputs in the sidebar. Focus lifts the border from hairline to navy; placeholder runs in {colors.muted}. Queries like "pet hair deep carpet cleaner" fit without truncation at the target width.

### Navigation

**`nav-bar-top-strip`** — A 36px navy band above the main header carrying shipping thresholds, loyalty program links, and store-finder in white caption type. Appliance retail standard for communicating logistics above the fold.

**`nav-bar`** — White, 72px, with the Bissell logotype left-anchored in navy, category links centered in {typography.nav-link} weight, and search plus cart icons right-aligned. A bottom hairline separates it from the page without adding visual weight.

**`mega-menu`** — Triggers on category hover: full-width white panel dropping below the nav, marked by a 3px red top accent. Content is a 4–6 column grid of icon-above-label subcategory tiles. A soft drop shadow anchors it to the page plane. On mobile it converts to a slide-in accordion drawer.

### Product Cards

**`product-card`** — White surface with 1px soft hairline border, {rounded.sm} corners, and a {colors.surface-soft} image well for product photography on light backgrounds. Title in {typography.title-sm}, current price in {typography.price-sm}. Badge slots at the top-left corner stack `sale-badge`, `promo-badge`, and `new-badge` vertically. `product-card-hover` lifts border strength and adds a soft shadow.

### Badges

**`sale-badge`** — Red (#fa1400) fill, white uppercase type at 11px/700. Applied for percentage-off and clearance labels; its red echo of the primary CTA signals actionable urgency.

**`promo-badge`** — Amber (#fab812) fill, ink text. Reserved for bundle promotions, gift-with-purchase, and limited-time callouts. The gold distinguishes it from the harder red of sale pricing.

**`new-badge`** — Navy (#00174d) fill, white text. Applied to product launches and newly listed SKUs; the brand-color fill reads as authoritative introduction rather than promotional pressure.

### Filter Chips

**`filter-chip`** — Pill-shaped ({rounded.full}) in {colors.surface-soft} with a hairline border; used in both sidebar filter panels and horizontal filter bars above product grids. Active state (`filter-chip-active`) inverts to solid navy with white text — a full inversion rather than a partial accent, so selected filters read unambiguously at a glance.

### Price Block

**`price-block`** — Current price at 22px/700 in {colors.ink}; original price at 15px/600 in {colors.muted} with strikethrough; savings amount in {colors.primary} red below. The three-tier stack communicates the discount math without needing additional labels.

### Trust Strip

**`trust-strip`** — Horizontal band between hero and product grid, carrying 3–4 benefit icons (free shipping threshold, satisfaction guarantee, BISSELL Foundation pet rescue donation) in {colors.accent-orange} with {typography.caption} labels below each. Hairline borders top and bottom integrate it without creating a full section break.

### Hero Banners

**`hero-banner`** — Cream canvas (#fcfcec) at full bleed, 64px vertical padding, flush-left display headline in {typography.display-xl}, a body subhead in {typography.body-md}, and a `button-primary` CTA. Product or lifestyle photography fills the right half at desktop; stacks below text on mobile.

**`hero-banner-navy`** — Same structure but #00174d background; headline and subhead run white ({colors.on-navy}); CTA remains `button-primary` in red for contrast. Used for seasonal hero campaigns and flagship product launches where the cream canvas reads too light.

### Category Tile

**`category-tile`** — Cream-canvas background ({colors.canvas-cream}), {rounded.md} corners, a soft hairline border that sharpens to {colors.accent-orange} on hover. Title in {typography.title-sm} below a category icon or lifestyle thumbnail. Used in home-page category navigation grids and mega-menu subcategory panels.

### Footer

**`footer`** — Navy (#00174d) background with a four-column link grid. Section headings in white {typography.title-sm}; body links in {colors.accent-blue-soft} (#92aedb) — the muted sky-blue creates legible contrast against the dark ground without using full white on every link. Social icons in white. `footer-bottom-bar` runs near-black (#001133) with legal copy in {colors.muted} gray, 48px tall.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger drawer replaces header nav; search bar drops full-width below logo row; product grid collapses to 1 column; hero goes single-column with image stacked above text; mega-menu converts to accordion slide-in; trust strip reflows to 2×2 grid |
| Tablet | 744–1128px | 2-column product grid; top nav shows abbreviated category labels or icon-only; search bar inline at 320px; hero two-column with reduced padding (32px); filter sidebar collapses to modal sheet |
| Desktop | 1128–1440px | 3–4 column product grid; full mega-menu on hover; hero at full 64px vertical padding; trust strip renders as horizontal 4-icon band; filter sidebar inline at 240px |
| Wide | > 1440px | Content max-width ~1320px centered; hero image scales proportionally; grid holds at 4 columns; surplus horizontal space absorbed by hero padding rather than extending the grid |

### Touch Targets

- All buttons minimum 48px height; minimum 44px tap width enforced on small CTAs
- Hamburger and header icon buttons minimum 44×44px touch target with invisible padding
- Filter chips minimum 40px height on mobile
- Product card entire surface is tappable; embedded CTA button maintains 48px minimum
- Cart, search, and account icons in header minimum 44×44px

### Collapsing Strategy

- Mega-menu collapses to full-screen accordion drawer on mobile; each category tap expands subcategories in place
- Trust strip collapses from 4-across horizontal to 2×2 grid at mobile; no items hidden
- Footer collapses from 4-column grid to single-column stacked sections with accordioned link groups on mobile
- Badge stack on product cards limits to one visible badge at mobile to prevent vertical overflow
- Price block retains full three-tier layout (current / original / savings) at all breakpoints — no data hidden

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom web font was captured — the site likely delivers a brand typeface via JavaScript or a third-party font service that was not available during static extraction. All typography uses system-ui as a stand-in; the actual font family, weight range, and optical sizing may differ substantially.
- A large share of extracted hex values appear to originate from payment-provider badge icons rendered in the checkout flow: Mastercard (#ed0006, #eb001b, #f9a000), Visa (#222357, #254aa5, #001ee6), PayPal/Amex (#016fd0, #0176d3), and likely an additional provider accounting for #5115f7 (purple) and #ffb3c7 (pink). These were excluded from the design token set.
- The gray ramp (#f7fafc, #edf2f7, #e2e8f0, #cbd5e0, #a0aec0, #718096) matches Tailwind CSS / Chakra UI defaults and may represent framework scaffolding rather than intentional brand choices; surface and muted tokens are drawn from it conservatively.
- Meta theme-color was not set, removing the most direct signal for dominant mobile chrome color.
- Hover transition timing, animation easing curves, and scroll-triggered behaviors were not extractable and are not specified.
- Icon system type (SVG sprite, inline SVG, icon font) and visual style (filled vs. outline, stroke weight) could not be determined from extraction; inferred from typical appliance retail patterns.
- Exact rating-star rendering, review count placement, and star fill treatment were not captured.
- Specific product-tier color coding (if any difference between entry, mid, and premium lines) could not be confirmed from static extraction alone.
