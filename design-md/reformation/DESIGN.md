---
version: alpha
name: "Reformation"
source_url: "https://thereformation.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every product page displays a RefScale counter—liters of water saved, pounds of CO2 avoided, pounds of waste reduced—before the size selector even appears. That data-first honesty is echoed in the design: a warm cream canvas (#eeece4) that reads like unbleached paper, type set in an editorial serif rather than a punchy grotesque, and deep navy (#0a1a69) standing in for the flat black that most fashion brands reach for. The site runs no decorative flourishes crowding the product imagery; generous negative space and restrained type do the entire job of positioning. Product cards float on the cream ground with zero border and zero shadow—context comes entirely from typography hierarchy and image placement, not UI chrome. Navigation is compressed to a single horizontal rule: brand name centered, category links flanking, account utilities at the right margin, all in a compact all-caps sans that defers to the photography below. The palette extracted from the live site is dominated by payment-processor injection—PayPal UI blues cluster around #003087 and #009cde—alongside the brand's own cream, a mid-gray body tone (#575757), and a high-energy red (#f50100) reserved exclusively for sale pricing and promotional callouts. Rounded corners skew sharp: cards and inputs sit at {rounded.xs} or {rounded.none} rather than the pill shapes common in softer DTC categories. Even the add-to-cart button is a full-width bar that stays flush against the product details panel, extending edge-to-edge on mobile. The overall effect is a fashion magazine printed in one ink with great photography—deliberate, flat, and legible at a glance.

colors:
  primary: "#0a1a69"
  primary-active: "#012169"
  primary-disabled: "#8e9ac4"
  ink: "#1a1a1a"
  body: "#575757"
  muted: "#8c8c8c"
  hairline: "#d8d5cc"
  canvas: "#eeece4"
  surface-soft: "#f7f4ed"
  surface-card: "#ffffff"
  on-primary: "#eeece4"
  sale: "#f50100"
  navy-mid: "#2e42a5"
  near-white: "#f7fcff"

typography:
  display-xl:
    fontFamily: "'Canela', 'Cormorant Garamond', Georgia, serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Canela', 'Cormorant Garamond', Georgia, serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Canela', 'Cormorant Garamond', Georgia, serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.04em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.06em
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  refscale-number:
    fontFamily: "'Canela', 'Cormorant Garamond', Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.0
    letterSpacing: -0.3px
  refscale-label:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  price:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-sale:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.05em
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
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
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 48px
    width: 100%
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 15px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 10px 20px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    width: 100%
    height: 52px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    focus-borderColor: "{colors.primary}"
  newsletter-input:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    placeholder-textColor: "#9aaad0"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: transparent
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
    name-typography: "{typography.body-md}"
    price-typography: "{typography.price}"
    price-sale-color: "{colors.sale}"
    hover: "second-image-crossfade"
  refscale-widget:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    number-typography: "{typography.refscale-number}"
    label-typography: "{typography.refscale-label}"
    textColor: "{colors.ink}"
    layout: "3-column-equal-metrics"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.title-md}"
    layout: "full-bleed-image-centered-overlay"
    overlayOpacity: 0
    padding: "{spacing.section} {spacing.xl}"
  category-pill:
    backgroundColor: transparent
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    active-backgroundColor: "{colors.primary}"
    active-textColor: "{colors.on-primary}"
    active-borderColor: "{colors.primary}"
  sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "#ffffff"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  size-selector:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
    selected-backgroundColor: "{colors.primary}"
    selected-textColor: "{colors.on-primary}"
    soldout-textColor: "{colors.muted}"
    soldout-decoration: line-through
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selected-border: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
  sustainability-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm}"
    textAlign: center
    height: 36px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.nav-link}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    columnGap: "{spacing.xxl}"
  image-grid-editorial:
    gap: "{spacing.xs}"
    columns: 2
    imageAspectRatio: "4/5"
    backgroundColor: "{colors.canvas}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    active-textColor: "{colors.ink}"

## Components

### Buttons

**`button-primary`** — Full-width, zero-radius bar set in all-caps 12px Helvetica Neue with 0.1em tracking against deep navy (#0a1a69). The `width: 100%` treatment means it spans the entire product panel on desktop and bleeds edge-to-edge on mobile, consistent with the brand's flat-magazine layout logic. Hover state darkens to `{colors.primary-active}` (#012169); disabled state washes to `{colors.primary-disabled}`. No shadow, no gradient—pure flat fill.

**`button-secondary`** — Canvas-ground button with a 1px primary navy border and matching uppercase typography. Used for secondary actions such as "Save to Wishlist" or nav-adjacent CTAs. Zero border-radius matches the overall geometric restraint; the border distinguishes it from ghost variants without introducing color weight.

**`button-ghost`** — Hairline-bordered transparent button for tertiary actions: quick-view, share, notify-me. Slightly smaller type (`{typography.button-sm}`) to signal lower hierarchy without color change. Hover state upgrades border to `{colors.body}`.

**`button-add-to-cart`** — Visually identical to button-primary but defined as a separate component because it always renders at 52px height, full-width, and is pinned to the bottom of a sticky product panel on scroll. On mobile it docks to a fixed bottom bar with a safe-area-inset buffer.

### Text Inputs

**`text-input`** — Flat field on the cream canvas with a single 1px hairline bottom border in default state; on focus, the border upgrades to all-sides 1px primary navy. Zero radius, no background fill change. Used in search, checkout fields, and account forms. The spare styling keeps the field invisible until the user engages with it.

**`newsletter-input`** — Footer variant rendered against the navy background. Border and text both use `{colors.on-primary}` (cream), producing a ghost-field appearance. Placeholder text is a desaturated blue-cream (#9aaad0) that reads as a hint without disrupting the dark footer.

### Navigation

**`nav-bar`** — 56px-tall single bar with logo centered horizontally, category links arrayed left, and account plus cart icons at the right margin. Background is canvas cream (#eeece4) with a 1px hairline bottom border. All nav text is 12px all-caps, 0.05em spacing—minimal visual weight relative to the photography below. As the user scrolls past the hero, the bar pins and the background transitions from cream to white surface-card.

### Product Card

**`product-card`** — Borderless, shadowless card on the cream canvas. Portrait images at 3:4 ratio span the full card width; on hover the card cross-fades to a second lifestyle or detail image. Below the image: product name in body-md (400 weight, 14px), color name in muted caption, and price in price-style. Sale prices render in `{colors.sale}` (#f50100) with the original price struck through in muted gray. No chip, no badge background, no corner radius. The card sits in a 2-up mobile grid and 4-up desktop grid with `{spacing.xs}` gutters to maintain editorial density.

### RefScale Widget

**`refscale-widget`** — Reformation's signature sustainability scorecard rendered directly beneath the product price. Three metrics—liters of water saved, lbs of CO2 avoided, lbs of waste reduced—sit in equal-width columns inside a soft-surface no-radius panel with a 1px hairline border. Each metric displays a large editorial-serif numeral in `{typography.refscale-number}` (36px, weight 300) above a 10px all-caps label in `{typography.refscale-label}`. This widget is not collapsible; it is load-bearing brand communication, not optional content.

### Hero Banner

**`hero-banner`** — Full-bleed image with editorial serif headline at `{typography.display-xl}`, centered or left-aligned. No overlay tint—photography is trusted to carry itself. Subheadline (when present) in `{typography.title-md}` all-caps. CTA renders as `button-secondary` (canvas fill, navy border) to avoid clashing with diverse imagery. On mobile, headline drops to `{typography.display-md}` and the CTA stacks below in a full-width `button-add-to-cart` treatment.

### Category Pills

**`category-pill`** — Horizontal-scroll filter row below the collection header on browse pages. Each chip: 1px hairline border, all-caps title-sm, full radius, transparent fill at rest. Active state fills with primary navy, text flips to on-primary cream. The row does not wrap—it scrolls horizontally on mobile without a fade mask.

### Sale Badge

**`sale-badge`** — Flat, zero-radius red (#f50100) label overlaid at the top-left corner of a product card image. Text is 11px all-caps white. Used exclusively for price-marked items; editorial labels like "New" or "Back in Stock" appear as plain text beneath the image to preserve the badge's urgency signal.

### Size Selector

**`size-selector`** — 40×40px squares arranged in a single row. Default: transparent fill, 1px hairline border, body-sm label. Selected: navy fill, cream text. Sold-out: muted gray label, strikethrough, border unchanged. On mobile the row wraps to a second line if the size range spans more than six options.

### Color Swatch

**`color-swatch`** — 24px circles with a 2px transparent border at rest, upgrading to a 2px solid ink border on selection. `{spacing.xs}` gap between swatches. Clicking updates the main product image and URL slug without a full page reload.

### Sustainability Banner

**`sustainability-banner`** — 36px sticky bar anchored above the nav at the top of every page. Primary navy background with cream text in body-sm, centered. Carries site-wide messaging: free-shipping thresholds, seasonal campaigns, or sustainability milestone announcements.

### Footer

**`footer`** — Full-width navy (#0a1a69) block with cream typography. Four-column desktop layout: company links, category links, sustainability and legal, and newsletter signup. Collapses to stacked accordion sections on mobile; the newsletter column always renders expanded regardless of viewport. All link text uses `{typography.nav-link}` all-caps. Newsletter input renders in the `newsletter-input` ghost style against the dark ground.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | 2-column product grid; nav collapses to hamburger drawer with full-screen navy overlay and display-md serif links; add-to-cart docks to fixed bottom bar with safe-area inset; hero headline at display-md; refscale widget stacks to 3 rows; footer accordions; size selector wraps at 6+ options |
| Tablet | 744–1128px | 2-column product grid; top-level nav categories visible, sub-menus hidden; hero at display-lg; refscale widget stays 3-column; product detail stacks image above info panel |
| Desktop | 1128–1440px | 4-column product grid; full horizontal nav with all category labels; product detail splits 50/50 image scroll + sticky info panel; RefScale widget 3-column inline |
| Wide | > 1440px | Content max-width 1440px centered; canvas-cream side margins fill the viewport; product grid stays 4-column but image cells scale with available width |

### Touch Targets

- Nav icons (account, search, bag): 44×44px minimum tap area regardless of visual icon size
- Size selector squares: 40×40px visual—on viewports under 375px expand to 44px to meet guidelines
- Color swatches: 24px visual with 8px invisible padding on all sides → 40px effective touch target
- Category pills: minimum 36px height on mobile via vertical padding adjustment
- Footer accordion headers: full-width tap row at minimum 48px height

### Collapsing Strategy

- Top nav collapses all category links into a full-screen drawer (navy background, cream links in display-md serif, closes on tap-outside)
- Collection filter bar converts from sticky horizontal pill-scroll to a slide-up filter sheet triggered by a full-width "Filter & Sort" ghost button
- Product image gallery collapses from a vertical scroll of full-width images to a swipeable carousel with dot pagination
- Footer four-column grid collapses to vertically stacked accordions; newsletter section always expanded (never collapsed)
- RefScale widget stacks its three metric columns vertically on viewports under 480px, maintaining equal visual weight for all three data points

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No font stacks extracted**: The site loads typefaces via JavaScript (likely Adobe Fonts or a proprietary CDN), defeating static extraction. Display serif is widely observed as Canela or a licensed equivalent; body sans appears to be Helvetica Neue. All typography tokens are informed approximations—verify against live rendered text before production use.
- **Primary CTA color uncertain**: The extracted navy cluster (#0a1a69, #012169, #003087, #2e42a5) may partly originate from PayPal's embedded payment UI rather than Reformation's own brand palette. Deep navy #0a1a69 is used here as primary on the basis that Reformation's current branding employs a dark navy for CTAs; this should be confirmed against the live add-to-cart button.
- **PayPal/payment processor injection likely**: #009cde, #003087, and #2e42a5 are canonical PayPal brand colors and almost certainly appear only in the checkout payment module. They are not assigned to any product-side component token in this spec.
- **Canvas color reliable**: #eeece4 is clearly Reformation's brand cream and the dominant page background—this token can be trusted.
- **True ink/black not extracted**: No near-black appeared in the extraction. `{colors.ink}` is set to #1a1a1a by convention; verify against body text on the live site.
- **Animation and motion data unavailable**: Transition durations, easing curves, and the product card image-crossfade timing cannot be recovered from color/font harvesting alone.
- **Spacing scale unconfirmed**: The 8px base-unit grid is a reasonable Shopify-theme default; actual theme spacing tokens may differ from values here.
