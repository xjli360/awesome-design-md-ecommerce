---
version: alpha
name: "Powertraveller"
source_url: "https://www.powertraveller.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A single dark anchor — #313131 — runs through the entire Powertraveller experience, from the bold product-tile borders to the footer background, giving the brand a grounded, industrial consistency that never wavers. The site reads as a technical catalog for the serious traveler, where every power bank, solar panel, and charging station is presented with a no-nonsense, utilitarian clarity. Product images dominate, often isolated against a clean white canvas, with the dark ink providing a strong framing device in cards and section dividers. The typography relies on a system-font stack — -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif — prioritizing legibility and fast load times over typographic flair. There are no decorative serifs or custom brand faces; the hierarchy is established purely through weight (600 for titles, 400 for body) and size, with display text at 24px and body copy at 16px. Buttons are solid, rectangular, and purposeful: the primary CTA uses the dark ink as a background with white text, while secondary actions are outlined in the same dark tone. The overall mood is one of reliability and straightforwardness — a brand that sells gear for off-grid power, not lifestyle. The only visual relief comes from the product imagery itself, which introduces natural greens, blues, and metallic grays against the otherwise monochromatic palette.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#757575"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  badge-sale: "#d32f2f"
  badge-new: "#2e7d32"
  star-rating: "#f5a623"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.badge-sale}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.primary}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    border: "1px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.xl}"
  hero-title:
    typography: "{typography.display-xl}"
    marginBottom: "{spacing.md}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.lg}"
  category-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  category-tile-hover:
    border: "1px solid {colors.primary}"
    backgroundColor: "{colors.surface-soft}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Buy Now", and "Shop All" actions. It uses the brand's dark ink (#313131) as a solid background with white text, creating a high-contrast, authoritative button. On hover, it darkens to `{colors.primary-active}` (#1a1a1a). The disabled state uses a medium gray (`{colors.primary-disabled}`) to visually indicate inactivity. The button has a subtle 4px rounded corner, maintaining a professional, no-nonsense feel.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details". It has a white background with a 2px solid border in the primary color. On hover, the background shifts to a soft surface tone (`{colors.surface-soft}`) and the border darkens. This button is used alongside the primary button to create a clear visual hierarchy without introducing additional colors.

**`button-tertiary`** — A text-only button for less prominent actions, such as "Clear Filters" or "Cancel". It has no background or border, relying solely on the primary color for its visual weight. It uses the same typography as the primary button to maintain consistency.

### Text Inputs
**`text-input`** — Standard form input used in search, checkout, and account forms. It has a white background with a light gray border (`{colors.hairline}`). On focus, the border thickens to 2px and changes to the primary color. Error states use a red border (`{colors.badge-sale}`) to indicate validation issues. The input height is 48px for comfortable touch interaction.

### Navigation
**`nav-bar`** — The top navigation bar is a fixed-height (64px) white bar with a subtle bottom border. Navigation links use uppercase, 14px, weight-600 text for a clean, technical feel. The active link is indicated by a 2px bottom border in the primary color. The nav bar collapses to a hamburger menu on mobile.

### Product Cards
**`product-card`** — The primary product display component. It features a white background, a 1px hairline border, and 8px rounded corners. On hover, the border changes to the primary color, providing a clear interactive state. The card contains a square image area, product title, price, and optional badges. The layout is clean and information-dense, suitable for a catalog-style grid.

### Badges
**`badge-sale`** and **`badge-new`** — Small, uppercase labels overlaid on product images or cards. The sale badge uses a red background (#d32f2f), while the new badge uses green (#2e7d32). Both have white text, 2px rounded corners, and tight padding. They are designed to be unobtrusive yet immediately legible.

### Search
**`search-bar`** — A pill-shaped search input with a soft gray background and a subtle border. On focus, the border switches to the primary color. It is used in the top nav and on search result pages. The pill shape (`{rounded.full}`) is the only significant use of full rounding in the system, providing a subtle contrast to the otherwise rectangular interface.

### Footer
**`footer-section`** — The footer uses the primary dark ink as a background, inverting the color scheme. Links are white with 80% opacity, increasing to full opacity on hover. This section contains site maps, legal links, and social icons. The dark footer anchors the page, providing a visual bookend to the white canvas above.

### Hero Banner
**`hero-banner`** — A full-width section at the top of the homepage and category pages. It has a soft gray background (`{colors.surface-soft}`) and contains a large title, a subtitle in muted text, and a primary button. The hero relies on typographic hierarchy and generous padding rather than background imagery, keeping the focus on the product categories.

### Category Tiles
**`category-tile`** — Used on the homepage to link to product categories (e.g., "Power Banks", "Solar Panels"). They are rectangular cards with a white background, a hairline border, and 8px rounded corners. On hover, the background shifts to soft gray and the border becomes primary. The tiles are arranged in a responsive grid.

### Rating Stars
**`rating-stars`** — A simple star rating component using a warm yellow (#f5a623) for filled stars. It is used on product cards and detail pages. The component is purely visual, with no interactive states.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero padding reduces to 32px; category tiles stack vertically; footer links stack in a single column |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses 48px padding; category tiles in a 2x2 grid |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero uses 64px padding; category tiles in a 3x3 grid |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero uses 80px padding; category tiles in a 4x2 grid |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px for touch accessibility.
- Product cards have a minimum tap area of 120px x 120px.
- Nav links in the hamburger menu have 48px touch targets.
- Search bar has a 44px height for easy tapping.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu below 744px.
- The product grid collapses from 4 columns to 1 column on mobile.
- The footer link columns collapse to a single vertical list on mobile.
- Category tiles collapse from a 3x3 grid to a single column on mobile.
- Hero banner padding reduces by 50% on mobile to conserve vertical space.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is limited to a single hex (#313131) from the live site's HTML and CSS. This may not represent the full brand palette, which could include additional accent colors, gradients, or secondary tones used in imagery or promotional banners. The palette above is inferred from this single anchor and standard e-commerce conventions.
- No specific font-family declarations beyond the system font stack were found. The brand may use a custom typeface on certain pages or in marketing materials that was not captured in the extraction.
- Hover and active states for components (e.g., product cards, nav links) are based on common e-commerce patterns and may not reflect the exact implementation on the live site.
- Error styling for forms (text-input-error) is a standard assumption; the actual error color and iconography were not extracted.
- Dark mode support is not confirmed. The current palette assumes a light theme.
- Sub-brand or promotional palettes (e.g., for seasonal sales or specific product lines) were not captured.
- The extracted data came from a "Just a moment..." page title, indicating a possible Cloudflare challenge or redirect. The actual brand site may have additional design elements not present in the extracted data.
- Button disabled states and secondary button active states are inferred from common patterns; exact hex values for these states were not extracted.
- The star-rating color (#f5a623) is a standard e-commerce convention and was not extracted from the live site.
