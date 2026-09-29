---
version: alpha
name: "Betterway"
source_url: "https://betterwaypaper.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Betterway ships bamboo toilet paper in kraft-brown wrapping without a single strip of plastic — the outer material is already the brand argument, leaving the digital presence to carry that same restraint into pixels. Rather than investing in hero illustration or high-production lifestyle shoots, the site relies on a muted green primary (inferred ~#4a7c59) acting as the one voltage color against warm-cream surfaces that echo unbleached pulp. Product photography sits on {colors.surface-soft}, a near-paper off-white that reads like the inside of a cardboard box left in good light. Buttons carry gentle {rounded.sm} corners rather than the pill shapes that playful eco brands favor, placing Betterway closer to the earnest-utility end of the DTC spectrum than the gift-able novelty end. Body copy is compact and factual — claim density is high, marketing rhetoric low — suggesting a design brief that said "let the numbers do it." The primary green holds WCAG AA on both white and cream surfaces without a border stroke, letting subscription-plan comparison cards and add-to-cart actions feel legible rather than loud. A tight spacing scale keeps section padding from sprawling: the gap between a product image and its price tag reads the same as the gap between a sustainability stat and its label, creating visual rhythm through consistency rather than drama. Certifications and third-party badges — FSC, carbon-neutral marks — cluster near the footer and PDP trust zone in small-cap type at roughly 11–12px, a convention shared by every impact-first paper brand. Navigation is spare: wordmark left, utility icons right, category dropdowns only when SKU count demands them. The overall palette — kraft, leaf, and white — maps directly to the three materials in the supply chain, making the design system feel less like a brand choice and more like a consequence of what the product actually is.

colors:
  primary: "#4a7c59"
  primary-active: "#3a6347"
  primary-disabled: "#a8c9b4"
  ink: "#1c1c1c"
  body: "#3d3d3d"
  muted: "#717171"
  hairline: "#dedad4"
  canvas: "#ffffff"
  surface-soft: "#f5f1eb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  kraft: "#c8a96d"
  leaf-light: "#e8f0ea"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  label-caps:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.5px
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
    rounded: "{rounded.sm}"
    padding: 13px 24px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.primary}"
    padding: 12px 23px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
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
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageBackground: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    subtextColor: "{colors.muted}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    paddingVertical: "{spacing.section}"
  subscription-plan-card:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    activeBackgroundColor: "{colors.leaf-light}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.title-md}"
    detailTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  sustainability-badge:
    backgroundColor: "{colors.leaf-light}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  kraft-badge:
    backgroundColor: "{colors.kraft}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  certification-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.label-caps}"
    borderTop: "1px solid {colors.hairline}"
    paddingVertical: "{spacing.lg}"
  pdp-trust-zone:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    subtextColor: "{colors.muted}"
    bodyTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    linkColor: "{colors.primary}"
    mutedTextColor: "{colors.muted}"
    bodyTypography: "{typography.body-sm}"
    labelTypography: "{typography.label-caps}"
    borderTop: "1px solid {colors.hairline}"
    paddingVertical: "{spacing.xxl}"

## Components

### Buttons
**`button-primary`** — 48px tall, {rounded.sm} corners, {colors.primary} fill with white text via {typography.button-md}. Hover darkens to {colors.primary-active}; disabled washes to {colors.primary-disabled} at reduced saturation. Used for Add to Cart, Subscribe, and all primary conversion actions. The green is the only saturated color on most pages, so the button draws the eye without competing with anything.

**`button-secondary`** — White fill with a 1.5px {colors.primary} border and matching text, identical 48px height to primary. Prevents green oversaturation on pages with multiple CTA rows — "View All", "Learn More", and secondary subscription plan actions use this treatment.

### Text Input
**`text-input`** — 48px tall, {rounded.sm}, {colors.hairline} border at rest sharpening to a {colors.primary} focus ring. Placeholder text in {colors.muted}. Used in newsletter sign-up and any onsite quiz or subscription configuration flow. No fill tint — stays on {colors.canvas} to read as neutral against the warm cream page ground.

### Navigation
**`nav-bar`** — 64px tall bar on {colors.canvas}, separated from page content by a {colors.hairline} bottom border. Wordmark sits left; cart and account icons sit right. Category links use {typography.nav-link} at 15px/500 weight. No megamenu unless depth of collections demands it — the SKU catalog for a paper brand is narrow enough to handle with a simple dropdown or flat links.

### Product Card
**`product-card`** — Image crops sit on {colors.surface-soft} cream, giving the photography a paper-like ground without a hard outline or drop shadow. Title in {typography.title-md}, price and pack-size detail in {typography.body-sm}/{colors.muted}. {rounded.sm} on the card shell; {spacing.base} internal padding. No star rating overlay on the card face — reviews surface on PDP only.

### Hero Section
**`hero-section`** — Full-width band on {colors.surface-soft}, headline in {typography.display-xl} (40px/700), supporting claim in {typography.body-md}. Primary CTA is `button-primary`. {spacing.section} top and bottom padding. Photography appears right-aligned on desktop, stacking above text on mobile with the headline leading in DOM order.

### Subscription Plan Card
**`subscription-plan-card`** — Selector card for subscribe-and-save vs. one-time purchase options. At rest: {colors.surface-soft} fill, {colors.hairline} border. Selected state adds a {colors.primary} border and {colors.leaf-light} background tint as a confirmation signal. {rounded.md} corners; {spacing.lg} internal padding. The full card is a tap target, not just the radio control.

### Sustainability Badge
**`sustainability-badge`** — Inline pill used inside product cards and hero copy to call out "100% Bamboo", "FSC Certified", "No Plastic". {colors.leaf-light} fill, {colors.primary} text, {rounded.full} pill shape, {typography.caption} at 12px/500. Non-interactive display only — never used as a filter trigger.

### Kraft Badge
**`kraft-badge`** — Rectangular promo callout in {colors.kraft} with white {typography.label-caps} text. Applied to sale, bundle, or limited-run labels where the green primary would create visual conflict with the sustainability badge. {rounded.xs} corners, tight xs padding to read as a stamp rather than a chip.

### Certification Strip
**`certification-strip`** — Horizontal row of third-party certification logos (FSC, carbon-neutral, 1% for the Planet) rendered at 32px height. Housed on {colors.surface-soft} with a top {colors.hairline} rule. Accompanying text uses {typography.label-caps}/{colors.muted}. Appears in the page footer and optionally beneath the PDP trust zone.

### PDP Trust Zone
**`pdp-trust-zone`** — Block sitting beneath the Add-to-Cart button, listing shipping window, return policy, and subscription terms. {colors.surface-soft} fill, {typography.body-sm} for detail rows, {typography.caption} for sublabels, {rounded.sm} outer shell, {spacing.base} padding. Separated from the PDP price block by a {colors.hairline} horizontal rule.

### Footer
**`footer`** — {colors.surface-soft} background with a top {colors.hairline} border. Column grid: brand links, sustainability links, account links, newsletter input. Column headers in {typography.label-caps}/{colors.ink}; link rows in {typography.body-sm}/{colors.primary}. Certification strip appears above the legal line. Bottom copyright row in {colors.muted}/{typography.body-sm}. {spacing.xxl} top and bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero image moves above headline; nav collapses to hamburger; product grid goes 2-column; subscription plan cards stack vertically |
| Tablet | 744–1128px | Hero splits 50/50 text-image; product grid 3-column; nav links visible without hamburger; certification strip wraps to 2 rows if count exceeds 4 |
| Desktop | 1128–1440px | Full 4-column product grid; hero image at 55% width; nav fully expanded; subscription plan cards side by side |
| Wide | > 1440px | Max-width container at 1440px centered on canvas; hero adds breathing room via increased padding, not image scaling |

### Touch Targets
- All interactive elements minimum 44×44px; primary and secondary buttons at 48px height
- Subscription plan card tap target spans the full card face, not just the radio or label
- Certification logo strip is display-only; no tap target sizing required
- Cart and account nav icons padded to 44px hit area even if visually rendered smaller
- Sustainability badges are non-interactive; no tap target enforcement needed

### Collapsing Strategy
- Hero: image-right desktop → image-above-text mobile; headline always first in DOM order for screen readers
- Product grid: 4 → 3 → 2 columns across breakpoints; card image aspect ratio locked at 1:1; padding contracts by one spacing step per breakpoint
- Subscription plan selector: side-by-side on desktop, stacked on mobile with selected card confirmed by border color, not position change
- Footer: 4-column grid → 2-column tablet → single column mobile; newsletter input spans full width on mobile
- Certification strip: horizontal scroll on mobile rather than wrapping logos to preserve brand mark aspect ratios

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Zero hex colors extracted** — betterwaypaper.com returned no extractable color tokens; all palette values are inferred from the sustainable bamboo paper goods category and general DTC brand conventions, not measured from the live site
- **No fonts extracted** — font-family stacks could not be scraped; all typography uses `system-ui` fallback; the actual brand may use a licensed geometric sans (Graphik, Söhne, GT America, or similar)
- **Exact green hue unconfirmed** — `#4a7c59` is a category-reasonable forest green; the real primary could be lighter (sage ~#7aaa8a), darker (hunter ~#2d5a3d), or shifted toward teal or olive
- **Kraft accent unverified** — `#c8a96d` is an estimated kraft-paper tone; actual brand packaging color not confirmed from digital extraction
- **Platform non-Shopify** — platform=False prevents inference of Shopify-specific component patterns (variant selectors, metafield blocks, cart drawer); component shapes above are estimated from DTC conventions
- **Subscription widget architecture unknown** — whether subscribe-and-save is handled via ReCharge, Skio, or a custom implementation affects plan-card interaction patterns; estimated above as a simple toggle card
- **Logo and wordmark treatment** — typeface, weight, any accompanying icon mark, and lockup proportions not verified
- **Motion and animation tokens absent** — hover transitions, page-load reveals, and skeleton states not captured
- **Dark mode** — no evidence of dark-mode support extracted; not modeled in this spec
