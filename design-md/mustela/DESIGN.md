---
version: alpha
name: "Mustela"
source_url: "https://mustelausa.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A blue-and-white clinical warmth, where #004d9d (a deep, confident navy) anchors every primary action and #00b2ff (a crisp, medical-grade cyan) signals interactive moments across a baby-care site that refuses to be saccharine. The palette reads more like a pediatrician’s office than a nursery — #f2f6fa (a cool, almost-ice canvas) replaces the expected pastel pink or mint, while #4a5464 and #728197 provide a slate-gray body hierarchy that keeps product photography (creams, lotions, oil bottles on white backgrounds) as the sole source of softness. Work Sans, a geometric sans-serif with open apertures, runs at moderate weights (400–600) and never above 28px, letting the brand’s French-pharmacy heritage speak through clean layout rather than typographic flourish. Buttons carry {rounded.sm} corners — not pill-shaped, not sharp — a deliberate midpoint that feels both approachable and precise. The Shopify platform reveals itself in the checkout-widget blues (#dcdfe5, #dedede) that creep into the extracted palette, but the brand’s own voice is the navy-cyan binary: #004d9d for add-to-cart and nav bars, #00b2ff for hover states and secondary accents. Product cards use a white surface ({colors.surface-card}) with a thin #dcdfe5 hairline, and the footer collapses into a dense, link-heavy block on #23282f — a dark inversion of the otherwise airy layout. The overall effect is trustworthy, dermatologist-adjacent, and deliberately un-cute: Mustela sells baby skincare the way a medical brand sells efficacy, not emotion.

colors:
  primary: "#004d9d"
  primary-active: "#003d7a"
  primary-disabled: "#b0cce5"
  ink: "#23282f"
  body: "#4a5464"
  muted: "#728197"
  muted-soft: "#c1c8d1"
  hairline: "#dcdfe5"
  hairline-soft: "#dedede"
  canvas: "#f2f6fa"
  surface-soft: "#f2f6fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#00b2ff"
  accent-cyan-hover: "#0099e0"
  dark-bg: "#23282f"
  dark-text: "#ffffff"
  error: "#c13515"
  success: "#2e7d32"

typography:
  display-xl:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-cyan-active:
    backgroundColor: "{colors.accent-cyan-hover}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    padding: 4px 0px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.error}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0, 77, 157, 0.1)"
  product-card-title:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base} 0 {spacing.base}"
  product-card-price:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-badge:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.dark-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.dark-text}"
    typography: "{typography.caption}"
    textTransform: uppercase
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in Mustela’s deep navy {colors.primary}. On hover, it shifts to {colors.primary-active} for a subtle darkening effect. Disabled state uses {colors.primary-disabled}, a muted blue-gray. All primary buttons use {rounded.sm} corners and {typography.button-md} for a clean, professional feel.

**`button-secondary`** — An outlined variant with a white background and navy border/text. On hover, it fills with {colors.primary} and inverts to white text. Used for secondary actions like “Learn More” or “View Details” alongside primary CTAs.

**`button-cyan`** — The accent button, using {colors.accent-cyan} as background. This appears for promotional badges, sale indicators, or highlight actions. Hover state shifts to {colors.accent-cyan-hover}. Use sparingly — it’s the brand’s voltage bump.

**`button-text-link`** — A text-only button styled as an inline link, using {colors.primary} and {typography.link}. No background, no border. Used for “Read more” or “See all” links within content sections.

### Cards
**`product-card`** — A white card with a thin {colors.hairline} border and {rounded.sm} corners. The card itself has no padding — the product image fills the top, and text content uses its own padding tokens. On hover, the border shifts to {colors.primary} and a subtle navy-tinted shadow appears. The card title uses {typography.title-md} in {colors.ink}, while the price sits below in {typography.body-sm} in {colors.body}.

**`product-badge`** — A small cyan badge, typically positioned over the top-left corner of a product image. Uses {colors.accent-cyan} background, white text, and {rounded.xs} corners. Text is uppercase via {typography.badge}. Used for “NEW”, “SALE”, or “BESTSELLER” labels.

### Navigation
**`top-nav`** — A fixed-height 64px bar on {colors.canvas} with a 1px bottom border in {colors.hairline}. Navigation links use {typography.nav-link} — uppercase, 14px, 0.5px letter-spacing. Active links switch to {colors.primary}, inactive links use {colors.body}. The bar contains the logo (left), category links (center), and utility icons (search, account, cart — right).

**`nav-link-active` / `nav-link-inactive`** — No background, just text color changes. Active state uses {colors.primary} to indicate the current page or section. Inactive uses {colors.body}.

### Forms
**`text-input`** — Standard text input with a white background, {colors.hairline} border, and {rounded.sm}. On focus, the border thickens to 2px and turns {colors.primary}. Error state uses a 2px {colors.error} border. Height is 48px for comfortable tapping.

**`search-bar`** — A compact 40px input with {colors.hairline} border and {rounded.sm}. On focus, the border becomes 2px {colors.primary}. Uses {typography.body-sm} for placeholder text.

**`quantity-selector`** — A compact 40px input for cart quantity adjustments, with {colors.surface-card} background, {colors.hairline} border, and {rounded.sm}. Contains increment/decrement buttons on either side.

### Footer
**`footer`** — A dark section on {colors.dark-bg} with white text. Links use {colors.muted-soft} for readability against the dark background. Column headings use {typography.caption} in uppercase. The footer is dense with links, legal text, and social icons, with generous {spacing.xxl} vertical padding.

### Accordion
**`accordion-trigger`** — A clickable row with {colors.ink} text in {typography.title-md}, separated from content below by a {colors.hairline} border. No background. Used for FAQ sections and mobile product descriptions.

**`accordion-content`** — The expandable panel below the trigger, using {colors.body} text in {typography.body-sm}. Padding collapses to zero when hidden.

### Hero
**`hero-section`** — A full-width section on {colors.canvas} with {spacing.section} vertical padding. Contains a headline in {typography.display-xl}, supporting text in {typography.body-md}, and a prominent {colors.primary} CTA button. The hero may include a product image or lifestyle photography on the right side.

**`hero-cta`** — The primary button within the hero, slightly larger than standard buttons at 48px height and 32px horizontal padding. Uses {colors.primary} background and {typography.button-md}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack vertically; hero text centers; accordions replace tabbed content; footer columns stack; search bar becomes full-width. |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links (logo + 3 categories); hero uses 60/40 split (text/image); footer shows 2-column grid. |
| Desktop | 1128–1440px | Full top-nav with all categories; three-column product grid; hero uses 50/50 split; footer shows 4-column grid; search bar appears in nav. |
| Wide | > 1440px | Max-width container (1440px) centers content; product grid expands to 4 columns; hero remains 50/50 but with larger imagery; whitespace increases around sections. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Icon buttons (search, cart, account) are at least 44x44px with adequate padding.
- Accordion triggers have 48px minimum tap height.
- Product card CTAs (“Add to Cart”) are 44px tall with generous padding.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer for category links.
- Product filters collapse into a “Filter” button that opens a modal on mobile.
- Footer link columns collapse into accordion-style sections on mobile, with the first column (Newsletter signup) remaining visible.
- Hero section stacks vertically on mobile — image below text.
- Product description tabs collapse into a single accordion on mobile.
- Cart drawer (if used) slides in from the right on all breakpoints, but becomes full-width on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and cards were inferred from common patterns — exact timing, easing, and shadow values were not extracted from the live site.
- Error and success states for forms (validation messages, input error icons) were not observed in the extracted data.
- The exact font-weight hierarchy for Work Sans (which weights are used for headings vs. body) was approximated from typical usage — the live site may use a different distribution.
- Dark mode is not present on the live site and was not designed for.
- The accent cyan (#00b2ff) usage frequency is unclear — it may appear only in promotional badges or also in links and hover states.
- Sub-brand or collection-specific palettes (e.g., “Mustela Maternity” vs. “Mustela Baby”) were not extracted.
- The Shopify checkout overlay colors (#dcdfe5, #dedede) are present in the extracted palette but are not part of Mustela’s brand system — they should be ignored for brand components.
- Iconography style (line vs. filled, stroke weight, corner radius) was not extracted.
- Animation durations, easings, and micro-interaction patterns were not captured.
- The “fontello” font-family declaration suggests icon fonts are in use, but the specific icon set and styling were not extracted.
