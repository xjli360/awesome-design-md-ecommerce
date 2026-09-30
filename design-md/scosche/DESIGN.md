---
version: alpha
name: "Scosche"
source_url: "https://www.scosche.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-voltage accessory brand that uses its own product category as its primary design signal — the bright #f5d83e yellow of a mounting clamp or charging indicator becomes the system’s only saturated accent, appearing on primary CTAs, sale badges, and the brand’s signature “#1 Mount” claim. Everything else recedes into a grayscale spectrum: the body grid runs on #303030 ink, #555555 muted text, and #ededed hairline dividers, with #111111 used sparingly for hero headlines. The typography stack is pure Helvetica Neue in four weights (Regular, Medium, Bold, and a condensed Bold for display), a no-nonsense Swiss choice that mirrors the brand’s mechanical, mount-and-hold engineering ethos. Buttons are sharp-cornered rectangles ({rounded.sm} ~8px) rather than pills — the brand avoids softness, preferring the visual torque of a yellow rectangle against a white or dark canvas. Product cards use #f0f0f0 surface fills with #c2c2c2 borders, and the search bar sits as a full-width #e8e8e8 field with no decorative icon. The palette’s secondary accent is #1979c3, a technical blue used exclusively for hyperlinks and “Learn More” text — never for CTAs. The overall effect is a system that looks like it was designed by an industrial engineer: every color has a job, every corner is a right angle, and the yellow is the only thing that moves.

colors:
  primary: "#f5d83e"
  primary-active: "#e9bc34"
  primary-disabled: "#c39f31"
  ink: "#111111"
  body: "#303030"
  muted: "#555555"
  muted-soft: "#767676"
  hairline: "#c2c2c2"
  hairline-soft: "#d1d1d1"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#f4f4f4"
  on-primary: "#111111"
  link-blue: "#1979c3"
  link-blue-active: "#006bb4"
  accent-orange: "#ff5501"
  badge-yellow: "#f5d83e"
  badge-yellow-text: "#9b6e00"
  dark-bg: "#111111"
  dark-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'HelveticaNeueLTStdCnBold', 'HelveticaNeueBold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'HelveticaNeueLTStdCnBold', 'HelveticaNeueBold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'HelveticaNeueBold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'HelveticaNeue-Medium', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'HelveticaNeue-Medium', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'HelveticaNeue-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'HelveticaNeue-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'HelveticaNeue-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-md:
    fontFamily: "'HelveticaNeue-Medium', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'HelveticaNeue-Medium', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'HelveticaNeue-Regular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'HelveticaNeue-Medium', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'HelveticaNeueBold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
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
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.muted}"
  button-dark:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.dark-text}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-dark-active:
    backgroundColor: "#2a2a2a"
    textColor: "{colors.dark-text}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
    padding: 0
  button-link-active:
    textColor: "{colors.link-blue-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "1px solid {colors.accent-orange}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 56px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.ink}"
    border-bottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.badge-yellow}"
    textColor: "{colors.badge-yellow-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.link-blue}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    border: "1px solid {colors.hairline}"
    backgroundColor: "{colors.canvas}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheadline:
    typography: "{typography.display-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.md}"
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.dark-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "#bbbbbb"
    typography: "{typography.body-sm}"
  footer-link-hover:
    textColor: "{colors.dark-text}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-dark:
    backgroundColor: "#333333"
    height: 1px

## Components

### Buttons
**`button-primary`** — The brand’s primary call-to-action, filled with #f5d83e yellow against a white or light canvas. Text is #111111 Helvetica Neue Medium at 15px with 0.3px letter-spacing, giving the button a dense, readable weight. Corners are slightly squared at {rounded.sm} (8px), avoiding the pill shape common in consumer brands — this is a mount-and-charge company, not a social app. On hover, the yellow deepens to #e9bc34 with no shadow or scale transform; the brand does not animate its buttons. The disabled state uses #c39f31, a muted gold that signals unavailability without introducing a new color.

**`button-secondary`** — An outlined variant with a 2px #c2c2c2 border on a white fill. Text is #303030 body color. Used for “Compare” and “Learn More” actions alongside primary CTAs. Active state swaps the border to #555555 and adds a #f0f0f0 background.

**`button-dark`** — Used on the black footer and dark hero sections. Fill is #111111, text is white. Hover shifts to #2a2a2a. No border — the brand trusts the dark canvas to separate the button from surrounding content.

**`button-link`** — A text-only link styled in #1979c3 blue, used for “View Details” and “Shop All” actions within product grids. No underline in default state; hover adds underline via text-decoration. Active state shifts to #006bb4.

### Cards
**`product-card`** — A white card (#f4f4f4 fill) with a 1px #d1d1d1 border and 8px corner radius. The product image sits in a #f0f0f0 square container with 4px rounding. Title uses Helvetica Neue Medium at 18px (#111111), price uses Regular at 16px (#303030). On hover, the border intensifies to #c2c2c2 and a subtle 2px/8px shadow appears — the only shadow in the system. Cards are laid out in a 3- or 4-column grid with 16px gaps.

**`badge-sale`** — A yellow badge (#f5d83e fill, #9b6e00 text) in 11px bold uppercase. Used exclusively for discount indicators. The text color is a dark gold, maintaining legibility without introducing black text on yellow.

**`badge-new`** — A blue badge (#1979c3 fill, white text) for new arrivals. Same typography and shape as the sale badge. The two badges never appear on the same card — the system enforces one badge per product.

### Navigation
**`nav-bar`** — A 56px white bar with a 1px #d1d1d1 bottom border. Navigation links are 14px Helvetica Neue Medium in uppercase with 0.5px letter-spacing — a technical, industrial feel. The active link gets a 2px #f5d83e bottom border. The bar contains the logo (left), category links (center), and a search icon + cart icon (right). On mobile, the category links collapse into a hamburger menu.

### Forms
**`text-input`** — A 44px white input with 1px #c2c2c2 border and 8px rounding. Focus state swaps to a 2px #f5d83e border with no outline. Error state uses a 1px #ff5501 border — the orange accent appears only here, reserved for validation feedback. Placeholder text is #767676.

**`search-bar`** — A full-width input on a #f0f0f0 background with 1px #d1d1d1 border. No search icon inside the field — the brand places a magnifying glass button to the right. On focus, the background shifts to white and the border to #c2c2c2.

### Footer
**`footer`** — A #111111 background section with white body text at 14px. Links are #bbbbbb, shifting to white on hover. The footer is divided into columns (Support, Products, Company, Connect) with no dividers between columns — the dark background provides enough structure. A thin #333333 horizontal divider separates the bottom legal row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked footer columns, hero text reduced to 28px |
| Tablet | 744–1128px | 2-column product grid, expanded nav links, hero at 32px |
| Desktop | 1128–1440px | 3-column product grid, full nav, hero at 36px |
| Wide | > 1440px | 4-column product grid, max-width container at 1440px, centered |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height
- Product card tap targets (image, title, price) are separate clickable areas, not a single card link
- Nav links have 48px minimum tap area (padding + height)
- Search bar and text inputs are 44px tall

### Collapsing Strategy
- Primary nav links collapse into a hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1
- Footer columns stack vertically below 744px
- Hero section reduces padding from 64px to 32px on mobile
- Badge text truncates to “SALE” instead of “SALE - 20% OFF” on cards narrower than 200px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components were inferred from the extracted color palette and common patterns — the live site may use different transitions or shadows
- Error, success, and warning form states beyond the orange error border could not be extracted
- Dark mode is not present on the live site; the dark footer and dark button are the only dark-surface components
- Sub-brand or product-line-specific color variations (e.g., Scosche Sport, Scosche Car) could not be identified
- The extracted font list includes multiple Helvetica Neue variants with `!important` flags — the exact font-weight-to-variant mapping was reconstructed and may differ from the live CSS cascade
- Animation durations, easing curves, and micro-interactions (e.g., hover scale, button press) were not extractable
- The extracted color list is heavily weighted toward grays and blues, with #f5d83e as the only distinctive accent — this is consistent with a brand that uses yellow as its single brand color, but secondary accents beyond #1979c3 and #ff5501 may exist on sub-pages
- Shopify Pay, Klarna, and Afterpay widget colors may be present in the extracted list but were filtered out; checkout-specific styling is not captured
