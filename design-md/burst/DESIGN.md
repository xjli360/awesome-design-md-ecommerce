---
version: alpha
name: "Burst"
source_url: "https://burstoralcare.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep violet #370078 anchors Burst's entire visual system — not as a subtle accent but as the dominant field behind product shots, the full-bleed hero background, and the primary button fill, creating a sense of clinical authority that feels more like a premium electronics brand than an oral-care company. Against this violet field, a high-voltage marigold #ffdd00 becomes the single accent color for CTAs, price highlights, and promotional badges, generating the kind of contrast that makes the "SHOP NOW" button feel like an urgent invitation rather than a passive link. The canvas is a cool off-white #f4f4f6, slightly softer than pure white, with a secondary surface tone #e5e5eb that gives cards and input fields a subtle dimensionality. Typography runs a neutral sans-serif stack at moderate weights — display headlines sit at 600 weight rather than the heavy 700+ common in DTC, letting the violet backdrop and product imagery carry the emotional weight rather than typographic muscle. Product cards use softly rounded corners ({rounded.md}) and generous whitespace, while the search bar and newsletter signup adopt pill shapes ({rounded.full}) that echo the ergonomic curves of the brand's sonic toothbrush handles. The overall mood is confident, clean, and slightly clinical — a brand that trusts its deep violet authority and yellow voltage more than decorative flourishes.

colors:
  primary: "#370078"
  primary-active: "#2a005e"
  primary-disabled: "#9a9db1"
  ink: "#121212"
  body: "#272d45"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#cecece"
  hairline-soft: "#e5e5e5"
  canvas: "#f4f4f6"
  surface-soft: "#e5e5eb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#ffdd00"
  accent-yellow-active: "#e6c700"
  accent-yellow-soft: "#ffee80"
  rating-star: "#ffdd00"
  error: "#4285f4"
  error-bg: "#e5e5eb"

typography:
  display-xl:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
  button-accent:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-yellow-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-accent:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  text-input-error:
    border: 2px solid "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.on-primary}"
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
  newsletter-button:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
  rating-stars:
    textColor: "{colors.rating-star}"
    fontSize: 16px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with deep violet {colors.primary} and white text. Used for "Add to Cart", "Subscribe", and "Shop Now" actions. On hover, shifts to {colors.primary-active} (#2a005e). Disabled state uses {colors.primary-disabled} (#9a9db1). All primary buttons use {rounded.sm} (8px) corners.

**`button-accent`** — The high-voltage alternative, filled with {colors.accent-yellow} (#ffdd00) and dark {colors.ink} (#121212) text. Used for promotional CTAs, limited-time offers, and "Get Started" flows. Active state shifts to {colors.accent-yellow-active} (#e6c700). Creates maximum contrast against the violet hero background.

**`button-secondary`** — An outlined variant with a white background, violet text, and a 2px violet border. Used for "Learn More" and secondary actions alongside primary buttons. Maintains the same 48px height and {rounded.sm} corners for visual consistency.

**`button-pill-primary`** and **`button-pill-accent`** — Pill-shaped variants ({rounded.full}) used for compact CTAs in navigation, search bars, and newsletter signups. These are shorter (40px) with tighter padding, designed for inline use rather than standalone hero buttons.

### Cards
**`product-card`** — A white card with {rounded.md} (12px) corners and {spacing.base} padding. Contains a product image (with {rounded.sm} on the image itself), title, rating stars in {colors.rating-star}, and price in {colors.primary}. The card has a subtle shadow on hover and a 1px {colors.hairline-soft} border in its default state.

**`product-card-badge`** — A small yellow badge ({colors.accent-yellow}) with uppercase bold text, pinned to the top-left corner of product cards. Used for "NEW", "BEST SELLER", and "SALE" labels. Compact at 2px 8px padding with {rounded.xs} corners.

### Navigation
**`nav-bar`** — A 72px white navigation bar with uppercase nav links in {colors.ink}. The logo sits left-aligned, with links centered or right-aligned. On scroll, a subtle box shadow appears to create separation from page content. The mobile version collapses links into a hamburger menu with a slide-out drawer.

**`nav-link`** — Uppercase, 14px, weight 600 with 0.5px letter spacing. Active links may use {colors.primary} text color or an underline indicator. The uppercase treatment gives the navigation a clean, editorial feel.

### Forms
**`text-input`** — Standard input fields with a white background, {rounded.sm} corners, and a 1px {colors.hairline} border. On focus, the border thickens to 2px and shifts to {colors.primary}. Error state uses a 2px {colors.error} (#4285f4) border. Height is 48px for consistency with buttons.

**`newsletter-input`** and **`newsletter-button`** — A paired pill-shaped input and button for email signups. The input uses {rounded.full} and white background, while the button uses {colors.accent-yellow} for visual contrast. The pair is typically placed in the footer against the violet {colors.primary} background.

### Hero
**`hero-section`** — A full-bleed violet ({colors.primary}) section with white text. Contains a headline in {typography.display-xl}, a subheadline in {typography.body-md}, and a primary CTA button. The hero may include product imagery or lifestyle photography overlaid on the violet field. Padding is {spacing.section} (64px) vertically.

### Footer
**`footer-section`** — A violet ({colors.primary}) footer with white links and white text. Contains link columns, social icons, and the newsletter signup component. The footer uses the same deep violet as the hero, creating a visual bookend for the page.

### Accordion
**`accordion-header`** and **`accordion-content`** — Used for FAQ sections and product details. Headers are clickable with a {colors.ink} title and a chevron icon that rotates on expand. Content panels reveal with a smooth height animation. A 1px {colors.hairline-soft} border separates each accordion item.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to {typography.display-md}; buttons become full-width; footer links collapse into accordion |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains two-column layout with image and text side by side; search bar remains full-width |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses full display-xl; search bar in nav is visible; footer columns display in a 4-column grid |
| Wide | > 1440px | Max-width container (1440px) centered; product grid expands to 4 columns; hero content remains centered with max-width on text; all components use max-width constraints |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Product card tap targets (title, price, image) are each at least 44px tall
- Accordion headers are 48px minimum tap height
- Nav links in mobile menu are 48px tall for easy tapping
- Newsletter input and button are both 48px tall

### Collapsing Strategy
- Navigation collapses to a hamburger menu with a slide-out drawer below 744px
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer link columns collapse to an accordion pattern on mobile, with each column becoming an expandable section
- Hero section stacks vertically on mobile, with text above imagery
- Search bar moves from the nav bar (desktop) to a prominent position below the nav (mobile)
- Secondary navigation (category filters, sort options) collapses to a dropdown selector on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted font-family declarations only returned "inherit" and widget-specific fonts (oke-widget-icons). The actual brand font family could not be reliably extracted from the live site CSS. The typography block uses a system font stack as a fallback. If the brand uses a custom typeface (e.g., a licensed font), that should replace the `inherit` value.
- Hover and active states for most components are inferred from common patterns rather than extracted from the live site. Specific hover transitions, shadows, and color shifts should be verified against the actual implementation.
- Error states for forms (validation messages, error icons) could not be extracted. The error color (#4285f4) is an extracted hex but may be a Shopify checkout widget color rather than a brand error color.
- Dark mode styling is not present on the live site and is not defined.
- The extracted color list includes several grays (#cecece, #dedede, #efefef, #f7f7f8, #d3d4dd) that may be Shopify framework defaults or stock image tones. The primary violet (#370078) and accent yellow (#ffdd00) are the most distinctive and brand-specific colors in the extraction.
- The "oke-widget-icons" font suggests the brand uses Okendo for reviews, but the review widget's specific styling (star sizes, spacing, colors) could not be extracted.
- Sub-brand or promotional micro-palettes (e.g., for specific product lines or seasonal campaigns) are not captured.
- Animation durations, easing curves, and transition properties are not defined.
- The Shopify platform dependency means some UI elements (cart drawer, checkout, product variants) may use Shopify's default styling rather than the brand's custom design system.
