---
version: alpha
name: "Pandasaurus Games"
source_url: "https://pandasaurusgames.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A board-game publisher that wraps its playful, tabletop energy in a deep-navy anchor (#121e37) and a marigold-yellow accent (#f8ca14) that reads like a sunlit game box lid. The brand lives in the contrast between that warm, almost retro yellow and a secondary teal (#108474) that appears on buttons, hover states, and product badges — a two-tone palette that signals both approachability and considered craft. The site runs Work Sans across headings and body text, a geometric sans-serif that balances readability with a slight editorial crispness; there is no heavy display weight, no decorative script, just clean utilitarian letterforms that step back and let the game art and product photography carry the visual story. White space is generous — product grids breathe with {spacing.lg} gutters, and the hero section uses a full-bleed background with a soft overlay, letting the featured game’s cover art dominate. Cards use {rounded.sm} corners, buttons are pill-shaped ({rounded.full}) with the yellow primary, and the secondary teal provides a calm, trustworthy alternative for less urgent actions. The footer collapses into a dense, link-heavy column on mobile, and the top navigation uses a sticky bar with a centered logo and a hamburger menu on small screens. The overall mood is bright, hobbyist-friendly, and slightly nostalgic — like a well-lit game cafe rather than a sterile e-commerce store.

colors:
  primary: "#f8ca14"
  primary-active: "#e0b312"
  primary-disabled: "#fff3c6"
  ink: "#121e37"
  body: "#1a2847"
  muted: "#7b7b7b"
  muted-soft: "#dadada"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#f9f9f9"
  on-primary: "#121e37"
  accent-teal: "#108474"
  accent-teal-active: "#0d6b5d"
  accent-orange: "#f26e21"
  badge-green: "#4cbb87"
  badge-yellow-bg: "#fff3c6"
  badge-yellow-text: "#121e37"
  star-rating: "#f8ca14"
  scrim: "#09172e"

typography:
  display-xl:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
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
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25px
  link:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
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
  price:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.accent-teal-active}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  button-tertiary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.accent-teal}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
    padding: "0 {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.canvas}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.canvas}"
    opacity: 0.85
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.canvas}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  social-icon:
    width: 24px
    height: 24px
    rounded: "{rounded.full}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's marigold yellow (#f8ca14) and set in dark navy text. Used for "Add to Cart", "Pre-Order", and primary checkout actions. On hover, it shifts to a slightly deeper yellow (#e0b312) for a subtle, friendly press. The disabled state uses a pale yellow wash (#fff3c6) with muted text, indicating unavailability without harsh visual noise. All buttons use pill-shaped corners (`{rounded.full}`) and 44px height for comfortable tap targets.

**`button-secondary`** — A teal-filled alternative (#108474) for secondary actions like "View Details" or "Learn More". White text ensures contrast against the darker teal. Hover deepens to #0d6b5d. This button appears alongside the primary in product cards and feature sections, providing a calm, trustworthy counterpoint to the energetic yellow.

**`button-tertiary`** — An outlined button with a white fill and a light gray border (#dedede). Used for less prominent actions such as "Cancel" or "Clear Filters". The border provides structure without competing with primary or secondary fills. Hover state darkens the border slightly.

**`button-ghost`** — A text-only button with no background or border. Used for inline actions like "See More" or "Read Reviews". Inherits the navy ink color and relies on the surrounding layout for visual weight.

### Cards
**`product-card`** — A clean, white card with a soft 8px radius (`{rounded.sm}`). The card contains a full-width product image (top-rounded), a title block using `{typography.title-md}`, and a price line using `{typography.price}`. No shadow by default; a subtle hover shadow may be added in implementation. Cards are arranged in a responsive grid with `{spacing.lg}` gaps. The image area is the primary visual anchor — game box art is colorful and busy, so the card body stays minimal.

**`product-card-image`** — The top portion of the product card, clipped to `{rounded.sm}` at the top corners and square at the bottom. Uses `object-fit: contain` (as seen in extracted CSS) to ensure the game box art is fully visible without cropping. A consistent aspect ratio (e.g., 1:1 or 4:3) should be enforced across the grid.

### Badges
**`badge-new`** — A small green (#4cbb87) badge with white uppercase text, used to flag newly released games. The green reads as "fresh" and "available" — a positive signal that doesn't clash with the yellow primary. Placed in the top-left corner of the product card image.

**`badge-sale`** — An orange (#f26e21) badge for discounted items. The orange provides urgency without the alarm of pure red. Same uppercase, small format as the new badge.

**`badge-sold-out`** — A gray (#dadada) badge with muted (#7b7b7b) text for out-of-stock items. Low contrast intentionally — sold-out items should recede visually.

### Navigation
**`nav-bar`** — A sticky top navigation bar, 72px tall, white background with a thin bottom border (#eeeeee). The brand logo is centered on desktop, with navigation links (uppercase, 14px, weight 500) on either side. On mobile, the logo remains centered and a hamburger menu replaces the link rows. The active page link uses the yellow primary color.

**`nav-link`** — Uppercase, 14px, weight 500, with 0.5px letter spacing for a slightly spaced-out, editorial feel. The uppercase treatment gives the nav a board-game rulebook vibe — precise and intentional.

### Forms
**`text-input`** — A standard input field with a white background, 1px solid light gray border (#dedede), and 8px rounded corners. On focus, the border thickens to 2px and turns teal (#108474), providing a clear, calm focus indicator. Padding is 12px vertical, 16px horizontal, with a 48px height for comfortable typing.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a white background and a 1px light gray border. Used in the hero section and possibly in a mobile search overlay. The pill shape matches the button family, maintaining the brand's friendly, rounded aesthetic.

### Footer
**`footer-section`** — A full-width footer with a dark navy background (#121e37) and white text. Links are set in 14px weight 400 with 0.8 opacity, lightening to full opacity on hover. The footer typically contains columns for "Shop", "About", "Support", and social media icons. Social icons are 24px circles (`{rounded.full}`) — likely using SVG icons for Instagram, Twitter/X, Facebook, and YouTube.

### Hero
**`hero-section`** — A full-bleed hero with a dark navy background (#121e37) and white text. The hero features a large game title (`{typography.display-xl}`), a subtitle in body weight, and a primary CTA button. The background may include a subtle pattern or gradient overlay. Minimum height is 400px, with generous padding (`{spacing.section}`) top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger menu replaces top nav links; hero text scales down to `{typography.display-lg}`; footer collapses to stacked columns; search bar moves to a toggleable overlay |
| Tablet | 744–1128px | Two-column product grid; top nav links visible but condensed (maybe icons only); hero maintains two-thirds width text block; footer uses two-column layout |
| Desktop | 1128–1440px | Three-column product grid; full top nav with uppercase links; hero uses full-width background with centered text; footer uses four-column layout |
| Wide | > 1440px | Max-width container (1440px) for content; hero may use a wider text block; product grid can expand to four columns if space allows |

### Touch Targets
- All buttons and links maintain a minimum 44px height (buttons) or 44x44px tap area (icon-only links).
- Product card tap targets are the entire card surface — no tiny "View" links.
- Search bar and text inputs are 48px tall for comfortable mobile typing.
- Hamburger menu icon is at least 44x44px.

### Collapsing Strategy
- Top navigation links collapse into a hamburger menu below 744px.
- Product grid collapses from 3 columns to 2 at tablet, to 1 at mobile.
- Footer columns collapse from 4 to 2 at tablet, to 1 at mobile.
- Hero section reduces vertical padding on mobile (from `{spacing.section}` to `{spacing.xxl}`).
- Search bar may collapse into an icon that expands to a full-width overlay on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states for product cards**: The extracted CSS did not include hover shadow or scale transforms. A subtle box-shadow or slight lift on hover is common in e-commerce but could not be confirmed.
- **Error and validation styling**: No form error colors (red borders, error text) were extracted. The brand likely uses a red like #c13515 or similar, but this is speculative.
- **Dark mode**: No dark mode styles were detected. The site appears to be light-mode only.
- **Sub-brand or expansion palettes**: Pandasaurus Games may have seasonal or campaign-specific color variants (e.g., holiday themes, convention banners). These were not extracted.
- **Font weights beyond 600**: The extracted CSS showed Work Sans but did not specify weights for all contexts. The weights above (400, 500, 600) are inferred from common usage; heavier weights (700+) may exist for display but were not seen.
- **Shopify-specific widgets**: Colors like #007aff (Shop Pay blue) and #fafafa (generic background) appear in the extracted list but are likely from Shopify's checkout widget or default theme, not the brand's design system. They have been excluded from the palette above.
- **Star rating component**: A star-rating color (#f8ca14) is defined, but the exact component (size, spacing, half-star rendering) was not extracted. The `JudgemeStar` font-family suggests Judge.me integration for reviews, but the star glyph details are unknown.
- **Animation and transition timing**: No CSS transition durations or easing functions were extracted. The brand likely uses 150-300ms ease-in-out for hover states, but this is unconfirmed.
