---
version: alpha
name: "Outdoor Vitals"
source_url: "https://outdoorvitals.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep-teal (#108474) pulse runs through Outdoor Vitals like a seam stitch — it is the brand's primary voltage, appearing on every add-to-cart button, sale badge, and navigation highlight against a near-white canvas of #f9fafb. The palette is drawn from the alpine landscape: ink-dark #0f3b56 for headlines, a muted slate #558499 for secondary text, and a full spectrum of grays from #eeeeee through #bababa to #777777 that build hierarchy without shouting. Montserrat carries the weight at 600–700 for headings and buttons, while Nunito Sans handles body copy at 400 — a pairing that reads as athletic and direct, not decorative. Product cards use soft corners at {rounded.md} and generous {spacing.base} padding, with the primary teal reserved for high-signal moments: the floating cart badge, the size-selector highlight, the "Free Shipping" callout. The site trusts photography over illustration — hero sections are full-bleed landscape shots with a teal gradient overlay at 20% opacity, letting the gear sit in its natural environment. There is no hard black anywhere; the darkest tone is #0d3863, a navy-adjacent ink that keeps the brand feeling outdoorsy rather than corporate. Checkout buttons invert to white-on-teal, and the footer collapses into a dense column of #f5f5f5 links — functional, fast, built for the trailhead browser session.

colors:
  primary: "#108474"
  primary-active: "#0d6b5e"
  primary-disabled: "#a3d5cc"
  ink: "#0f3b56"
  body: "#558499"
  muted: "#7b7b7b"
  muted-soft: "#bababa"
  hairline: "#d5d5d5"
  hairline-soft: "#e7e7e7"
  canvas: "#f9fafb"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-badge: "#108474"
  nav-ink: "#0d3863"
  footer-bg: "#f9f9f9"
  star-rating: "#108474"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Nunito Sans', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.nav-ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-sticky:
    backgroundColor: "{colors.surface-card}"
    boxShadow: 0 2px 8px rgba(15, 59, 86, 0.08)
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    padding: 0 "{spacing.base}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  search-bar-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: 2px solid "{colors.primary}"
    rounded: "{rounded.full}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-overlay:
    background: linear-gradient(135deg, rgba(16, 132, 116, 0.2), rgba(15, 59, 86, 0.4))
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.primary}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 36px
    padding: 0 12px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with the brand teal {colors.primary} (#108474) and white text. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, shifts to {colors.primary-active} (#0d6b5e) with no border change. Disabled state uses {colors.primary-disabled} (#a3d5cc) with white text — low contrast but intentional to signal non-interactivity. Full-width on mobile, auto-width on tablet and up.

**`button-secondary`** — Outlined variant with white background and {colors.ink} text, used for "View Details", "Learn More", and secondary actions. Has a 1px {colors.hairline} border that darkens to {colors.muted} on hover. Same 48px height as primary for alignment in forms.

**`button-tertiary`** — Text-only link styled as a button, using {colors.primary} for the text and no background. Used for "Clear Filters", "Cancel", and inline actions within product cards. Underlines on hover.

### Text Inputs
**`text-input`** — Standard form field with 48px height, {rounded.sm} corners, and a 1px {colors.hairline} border. Background is white, text is {colors.ink}. On focus, the border becomes 2px solid {colors.primary} with no outline shift — the teal ring is the only focus indicator. Placeholder text uses {colors.muted-soft} (#bababa). Used for search, email capture, and checkout forms.

### Navigation
**`nav-bar`** — Fixed top navigation at 72px height, white background, with {colors.nav-ink} (#0d3863) for link text. The logo sits left, primary links center (Shop, Learn, About), and cart/account icons right. On scroll, gains a subtle box-shadow using {colors.ink} at 8% opacity. Mobile collapses to a hamburger menu with a slide-out drawer.

**`nav-link`** — Montserrat 600 at 14px with 0.3px letter spacing. Active page or hover state underlines with a 2px {colors.primary} bar. No uppercase — the brand keeps navigation readable and direct.

### Product Cards
**`product-card`** — A white card with {rounded.md} (12px) corners, no border, and a subtle shadow on hover (2px offset, 8px blur, {colors.ink} at 6%). The product image fills the top with rounded top corners. Title uses {typography.title-md} in {colors.ink}, price uses {typography.body-md} in {colors.primary}. A {sale-badge} appears as a teal pill in the top-left corner when a discount is active. Star ratings sit below the title in {colors.star-rating}.

**`sale-badge`** — A small uppercase pill badge in {colors.primary} with white text, 4px padding, and {rounded.xs}. Positioned absolutely over the product image. Text reads "SALE" or a percentage like "20% OFF".

### Search
**`search-bar`** — A pill-shaped input with {rounded.full}, 44px height, and a {colors.surface-soft} (#f5f5f5) background. Placeholder text is {colors.muted} (#7b7b7b). On focus, background shifts to white and a 2px {colors.primary} border appears. A magnifying glass icon sits at the left in {colors.muted}. On mobile, expands to full width below the nav.

### Hero Section
**`hero-section`** — Full-width section with a minimum height of 400px, background in {colors.ink} (#0f3b56), and white text. A gradient overlay ({colors.primary} at 20% opacity to {colors.ink} at 40%) sits over a background image. Headline uses {typography.display-xl} (36px, 700 weight). A single {button-primary} sits below the headline. On mobile, height reduces to 300px and headline drops to 28px.

### Footer
**`footer-section`** — A dense, multi-column footer on {colors.footer-bg} (#f9f9f9). Links use {colors.muted} (#7b7b7b) and shift to {colors.primary} on hover. Columns collapse to a single stack on mobile. Includes newsletter signup with a {text-input} and {button-primary}. Social icons appear in {colors.muted} at 20px.

### Category Pills
**`category-pill`** — Horizontal scrollable strip of pill-shaped filters (e.g., "Tents", "Sleeping Bags", "Cookware"). Each pill is {rounded.full} with {colors.surface-soft} background and {colors.ink} text. Active pill uses {colors.primary} background with white text. 8px horizontal padding, 8px vertical. Scrollable on mobile with hidden scrollbar.

### Cart Badge
**`cart-badge`** — A small circle (20px) in {colors.primary} with white text, positioned at the top-right of the cart icon in the nav. Shows the item count. Uses {typography.badge} (11px, 700 weight, uppercase). Only visible when count > 0.

### Quantity Selector
**`quantity-selector`** — A compact input group for adjusting item quantities on the cart page. Has a minus button, a number display, and a plus button, all in a row with {rounded.sm} corners. Background is {colors.surface-soft}, text is {colors.ink}. Buttons are 36px tall with 12px horizontal padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; hero height drops to 300px; footer stacks vertically; category pills scroll horizontally; buttons go full-width; search bar expands below nav |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero keeps 400px height; footer shows 2 columns; category pills wrap to 2 rows |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 450px; footer shows 4 columns; search bar in nav |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to 4 columns; hero at 500px; all elements centered with generous margins |

### Touch Targets
- All buttons and links maintain minimum 44px tap target height
- Category pills are 36px tall but have 8px padding for tap area
- Quantity selector buttons are 36px with 12px padding — meets 44px effective tap area
- Cart badge is 20px but sits inside a 44px icon container

### Collapsing Strategy
- Primary nav links collapse into hamburger menu below 744px
- Product grid collapses from 4 columns to 1 column below 744px
- Footer columns collapse from 4 to 1 below 744px
- Hero text overlay collapses to single column below 744px
- Category pills switch from wrapped rows to horizontal scroll below 744px
- Search bar moves from inline nav position to full-width below-nav bar below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components could not be reliably extracted from the static HTML/CSS — only primary button hover was confirmed via extracted styles
- Error state styling for text inputs (red border, error message placement) is not present in extracted data
- Dark mode is not supported on the live site — no media query or color-scheme meta found
- Sub-brand or collection-specific color palettes (e.g., "Summit Series" or "Trail Lite") could not be identified
- The extracted font list includes "JudgemeStar" (a review widget icon font) and "Times" (likely a fallback) — these are not brand fonts and were excluded
- Font sizes and weights for typography tokens are estimated based on common Montserrat/Nunito Sans pairings and extracted CSS values — exact values may vary across pages
- Spacing tokens are inferred from common patterns; exact padding/margin values may differ on specific components
- The extracted hex list is dominated by grays (#eeeeee through #777777) and two distinctive colors (#108474 and #0f3b56) — the teal is confirmed as primary based on its usage in CTAs and badges, but secondary accent colors beyond the palette listed are unknown
- Shopify checkout page styling (Shopify Pay button, Klarna/Afterpay badges) is not included — those follow Shopify's own design system, not Outdoor Vitals'
