---
version: alpha
name: "Renoun Skis"
source_url: "https://renoun.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand built on the tension between deep alpine blue (#272d45) and a single, unapologetic accent of marigold (#ffc032) — the kind of high-voltage yellow that reads as both caution tape and sunrise on a powder day. The palette is otherwise restrained: slate (#676986) for body text, a near-white canvas (#f4f4f6) that feels colder and more technical than a pure white, and a teal (#0e7a82) that surfaces in product details and secondary badges, suggesting the cool of snowmelt. DM Sans runs the typography, a geometric sans-serif with enough warmth to keep the brand from feeling like a ski-patrol manual. Buttons are pill-shaped (`{rounded.full}`), a deliberate choice that softens the angularity of ski equipment and mountain geometry. The nav bar sits at a compact 64px, and product cards use a generous `{rounded.lg}` (20px) — the brand trusts photography of skis in motion over decorative flourishes. The marigold accent is never used as a background fill; it appears only as a highlight on dark surfaces — a CTA text color, a badge dot, a loading indicator — always a signal, never a wash. The overall mood is confident, alpine, and slightly muted: a brand that knows its product is the hero and the interface is just the lift line.

colors:
  primary: "#272d45"
  primary-active: "#1c2135"
  primary-disabled: "#8b8fa3"
  ink: "#121212"
  body: "#676986"
  muted: "#8b8fa3"
  muted-soft: "#e5e5eb"
  hairline: "#dedede"
  hairline-soft: "#f5f5f5"
  canvas: "#f4f4f6"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#ffc032"
  accent-teal: "#0e7a82"
  accent-marigold-active: "#e5a62d"
  accent-teal-active: "#0a6368"

typography:
  display-xl:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
    textTransform: uppercase
  badge:
    fontFamily: "'DM Sans', sans-serif"
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-accent:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-marigold-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.accent-marigold}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
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
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
    objectFit: cover
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  badge-feature:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-cta:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "16px 36px"
    height: 56px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.accent-marigold}"
    typography: "{typography.link}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  size-selector-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill with deep navy background and white text. On hover, the background deepens to `{colors.primary-active}`. In disabled state, the button shifts to `{colors.primary-disabled}` with reduced opacity (0.5) and cursor set to not-allowed. Used for "Add to Cart", "Pre-Order", and "Shop Now" actions.

**`button-accent`** — The marigold variant used for high-visibility CTAs like "Buy Now" or "Explore the Collection". The yellow against dark backgrounds creates maximum contrast. Active state shifts to `{colors.accent-marigold-active}`. Never used on light backgrounds — reserved for hero sections and dark product cards.

**`button-secondary`** — An outlined pill with navy border and transparent fill. Used for secondary actions like "Learn More" or "View Details". On hover, the background fills with `{colors.primary}` at 5% opacity. The 2px border maintains visual weight alongside the primary button.

**`button-tertiary-text`** — A text-only button in marigold, used for inline links within product descriptions or as "Read Reviews" triggers. No background or border — relies entirely on the accent color for visibility.

### Navigation
**`nav-bar`** — A compact 64px navigation bar on a near-white canvas (`{colors.canvas}`) with a subtle bottom border. Logo sits left-aligned, nav links are uppercase DM Sans at 14px/600. The bar collapses to a hamburger menu on mobile. Active nav links use `{colors.primary}` text; inactive links use `{colors.body}`.

**`nav-link-active`** — The active state for navigation items, rendered in deep navy. No underline or background — the color shift alone indicates the current page.

**`nav-link-inactive`** — Inactive nav links in slate gray (`{colors.body}`). On hover, they shift to `{colors.primary}` with a smooth 200ms transition.

### Cards
**`product-card`** — A white card with 20px rounded corners containing a product image, title, and price. The image fills the top of the card with top-rounded corners. No shadow — the brand relies on the card's white surface against the `{colors.canvas}` background for separation. On hover, a subtle lift effect (translateY(-2px)) with a soft shadow appears.

**`product-card-title`** — The product name set in DM Sans 16px/500, padded below the image. Truncated to two lines with an ellipsis overflow.

**`product-card-price`** — The price rendered in navy (`{colors.primary}`) at 16px/400, distinguishing it from the title. Sale prices appear in `{colors.accent-teal}` with the original price struck through in `{colors.muted}`.

### Badges
**`badge-new`** — A marigold badge with dark text, used to flag new arrivals. Compact at 4px/8px padding with 8px rounded corners. The yellow stands out against both white and navy backgrounds.

**`badge-sale`** — A teal badge (`{colors.accent-teal}`) with white text for sale or clearance items. The cool tone contrasts with the warm marigold of the new badge, creating a clear visual hierarchy between the two promotional states.

**`badge-feature`** — A navy badge with white text for technical features like "VibeStop™" or "All-Mountain". Used on product detail pages to highlight key selling points.

### Forms
**`text-input`** — A standard input field with white background, 12px rounded corners, and a light gray border. On focus, the border thickens to 2px and shifts to `{colors.primary}`. Placeholder text uses `{colors.muted}`. Used for email signups, search, and checkout fields.

**`quantity-selector`** — A compact input for selecting product quantities, with a border and 8px rounded corners. The value sits centered between minus and plus icon buttons.

**`size-selector`** — A selectable button group for ski length or size options. Active sizes use the navy fill with white text; inactive sizes show the white background with navy border. Disabled sizes (out of stock) appear with reduced opacity and a line-through.

### Hero
**`hero-section`** — A full-width section with deep navy background, used for landing pages and collection headers. The large display text sits in white with generous padding. Background may include a subtle mountain silhouette pattern or product photography overlay.

**`hero-cta`** — The oversized marigold button in the hero, 56px tall with generous padding. The larger size and accent color draw immediate attention against the dark hero background.

### Footer
**`footer-section`** — A navy footer with white text, containing link columns, social icons, and legal text. Links shift to marigold on hover. The footer uses `{spacing.xxl}` for top/bottom padding and `{spacing.lg}` for side padding.

**`footer-link`** — Standard footer link in white. On hover, transitions to marigold (`{colors.accent-marigold}`) with a 200ms ease-in-out transition.

### Iconography
**`icon-button`** — A circular icon button with transparent background and slate icon color. On hover, a soft gray background (`{colors.surface-soft}`) appears behind the icon, and the icon shifts to `{colors.ink}`. Used for cart, search, and menu icons in the nav bar.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero padding reduces to 32px; buttons become full-width; footer links stack vertically |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards display in 2-column grid; hero maintains 48px padding; search bar appears in nav |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero at full padding; side-by-side product details layout |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero content centered with max-width 1200px |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons are 40px minimum with 48px touch area via padding
- Product card tap targets (title, price, image) have 48px minimum touch areas
- Size selectors are 44px tall with 48px minimum width

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product filters collapse to a slide-out drawer on mobile
- Footer link columns collapse to a single column accordion on mobile
- Product image galleries collapse to a single-image carousel with dots on mobile
- Size and quantity selectors stack vertically on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette includes several generic web colors (#2c3e50, #dedede, #121212) that may be framework defaults or checkout widget colors rather than intentional brand choices. The primary (#272d45) and accent (#ffc032) are the most distinctive and likely authentic.
- Font-family declarations only returned "DM Sans" and generic fallbacks. No specific weights or sizes could be extracted — the typography tokens above are inferred from common DTC ski brand patterns and may not match the live site exactly.
- Hover states for buttons and links are inferred from common interaction patterns; actual hover colors may differ.
- Error states for form inputs (validation colors, error messages) were not extractable from the static HTML.
- Dark mode or high-contrast mode styles were not present in the extracted data.
- The teal accent (#0e7a82) appears in the extracted colors but its specific usage (badges, links, or decorative elements) is inferred from context.
- Spacing values are based on common 8px grid patterns; actual spacing may vary.
- The `oke-widget-icons` font-family reference suggests Okendo reviews are integrated, but review widget styling details are not available.
- Shopify platform integration means checkout buttons and cart UI may follow Shopify's default styling rather than the brand's design system.
