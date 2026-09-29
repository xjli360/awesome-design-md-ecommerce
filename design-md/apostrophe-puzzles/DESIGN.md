---
version: alpha
name: "Apostrophe Puzzles"
source_url: "https://www.apostrophepuzzles.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A puzzle brand that wears its primary red (#cc3b3b) like a signature stamp — not a loud shout, but a confident mark that appears on the Add to Cart button, the logo wordmark, and the small heart icon that lets you save a puzzle for later. The site runs on a near-white canvas (#fafafa) with text in near-black (#111111), creating a high-contrast reading environment that lets the puzzle artwork — often intricate illustrations of botanical gardens, Parisian streetscapes, or celestial maps — do the emotional work. Typography splits between Archivo Black (used for the brand name and major headings, a chunky geometric sans that feels like a wooden puzzle piece) and Josefin Sans (a slender, elegant sans-serif with subtle contrast, used for product titles and body copy). The red appears again in a lighter, almost blush variant (#e99292) used for sale badges and secondary accents, while a muted silver-gray (#aaaaaa) handles borders, dividers, and inactive UI. Rounded corners are restrained — buttons get a gentle {rounded.sm} (8px), product cards a slightly softer {rounded.md} (12px) — but the site avoids pill shapes entirely, preserving a crisp, geometric feel that mirrors the precision of a well-cut jigsaw piece. The footer stacks links in a single column on mobile, with a subtle hairline (#e1e1e1) separating sections, and the navigation bar uses a fixed position with a white background and the red logo centered on desktop, left-aligned on mobile.

colors:
  primary: "#cc3b3b"
  primary-active: "#bd0000"
  primary-disabled: "#e99292"
  ink: "#111111"
  body: "#272727"
  muted: "#aaaaaa"
  muted-soft: "#e1e1e1"
  hairline: "#e1e1e1"
  hairline-soft: "#eeeeee"
  canvas: "#fafafa"
  surface-soft: "#fbfbfb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-badge: "#e99292"
  star-rating: "#cc3b3b"
  footer-bg: "#1e1e1e"
  footer-text: "#eeeeee"

typography:
  display-xl:
    fontFamily: "'Archivo Black', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Archivo Black', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Josefin Sans', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'Josefin Sans', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Josefin Sans', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Josefin Sans', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Josefin Sans', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Archivo Black', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Archivo Black', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.4px
  link:
    fontFamily: "'Josefin Sans', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  nav-link:
    fontFamily: "'Josefin Sans', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Archivo Black', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.3px
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
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-heart:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 36px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-divider:
    backgroundColor: "{colors.muted}"
    height: 1px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for Add to Cart, Checkout, and Submit actions. Rendered in the brand red (#cc3b3b) with white text in Archivo Black at 15px. On hover, the background deepens to `{colors.primary-active}` (#bd0000). The disabled state uses `{colors.primary-disabled}` (#e99292), a lighter blush red that signals the action is unavailable. The button has a subtle 8px rounded corner (`{rounded.sm}`) and 14px vertical padding for a solid, clickable feel.

**`button-secondary`** — A bordered alternative to the primary button, used for secondary actions like "View Details" or "Continue Shopping." It has a white background with a 2px hairline border (`{colors.hairline}`) and ink-colored text. On hover, the border becomes solid ink and the background shifts to `{colors.surface-soft}`. The typography matches the primary button for visual consistency.

**`button-tertiary-text`** — A text-only button used for inline actions like "Clear Filters" or "Remove from Cart." It appears as a transparent background with primary red text in the smaller button typography (`{typography.button-sm}`). No border or rounded corners — it sits flush with surrounding content.

### Cards
**`product-card`** — The primary content container for puzzle listings on collection pages and search results. It has a white background with 12px rounded corners (`{rounded.md}`) and no padding at the container level — the image fills the top with matching corner radius, and the title and price are padded internally. The card includes a heart icon (wishlist save) positioned in the top-right corner, rendered as a 36px circle with the primary red fill on active state. A sale badge (`{product-card-sale-badge}`) overlays the image when a puzzle is discounted, using the blush red (#e99292) background with white uppercase text.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with a white background and a subtle bottom border (`{colors.hairline-soft}`). The brand logo (in Archivo Black, primary red) is centered on desktop and left-aligned on mobile. Navigation links use Josefin Sans at 14px with 0.5px letter spacing and uppercase transformation. The active page link is highlighted in primary red, while inactive links appear in muted silver. On mobile, the nav collapses into a hamburger menu with a slide-out drawer.

### Forms
**`text-input`** — Standard text input fields used in the newsletter signup, contact form, and checkout. They have a white background, 48px height, 8px rounded corners, and a 1px hairline border. On focus, the border thickens to 2px and turns primary red. The typography uses Josefin Sans at 16px for readability.

**`search-bar`** — The site search input, visually identical to `text-input` but with a magnifying glass icon positioned inside the left edge. On focus, the border transitions to primary red. The search bar is centered on desktop and full-width on mobile.

### Footer
**`footer`** — A dark footer section with a near-black background (#1e1e1e) and light text (#eeeeee). Links are styled in the same light color with Josefin Sans at 14px. A thin divider line (`{footer-divider}`) separates link groups. The footer stacks in a single column on mobile and expands to three columns on tablet and desktop.

### Quantity Selector
**`quantity-selector`** — A compact input group for adjusting puzzle quantities on the product page. It has a white background, 40px height, and a 1px hairline border with 8px rounded corners. The decrement and increment buttons are 40px squares with primary red text and no background. The current quantity is displayed in the center in body typography.

### Star Rating
**`star-rating`** — A row of five star icons used on product cards and the product detail page. Filled stars are rendered in primary red (#cc3b3b), while empty stars use the muted silver (#aaaaaa). Each star is 16px in size. The rating is displayed as a decimal (e.g., 4.5) next to the stars on the product detail page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Navigation collapses to hamburger menu; product cards stack in 2 columns; footer stacks to single column; hero section padding reduces to 32px; search bar becomes full-width; product card heart icon moves below image |
| Tablet | 744–1128px | Navigation links remain visible; product cards display in 3 columns; footer expands to 2 columns; hero section uses 48px padding; search bar is centered at 60% width |
| Desktop | 1128–1440px | Full navigation with centered logo; product cards in 4 columns; footer in 3 columns; hero section uses 64px padding; search bar is centered at 50% width |
| Wide | > 1440px | Content max-width capped at 1440px with centered layout; product cards may expand to 5 columns; hero section uses 80px padding |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Quantity selector buttons are 40px squares — acceptable for touch but borderline; consider 44px minimum on mobile
- Product card heart icon is 36px — below the 44px touch target recommendation; consider increasing to 44px on mobile
- Navigation links have 48px tap areas (padding + height)
- Search bar and text inputs are 48px tall, exceeding the 44px minimum

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px
- Footer link columns collapse from 3 to 2 at 744px, then to 1 below 480px
- Product card grid collapses from 4 columns to 3 at 744px, then to 2 below 480px
- Hero section image may stack below text on mobile
- Secondary navigation (filters, sort) collapses into a dropdown or expandable panel on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components were inferred from common patterns; actual extracted hover colors are not available
- Error styling for form inputs (red border, error message typography) was not extractable from the live site
- The extracted color list includes #040404 and #1e1e1e which appear to be footer/dark mode colors, but dark mode implementation is unconfirmed
- Font weights for Archivo Black and Josefin Sans were inferred; the extracted CSS may include additional weights not captured
- The extracted hex list is dominated by reds, grays, and whites — the brand's true primary (#cc3b3b) is the most distinctive color, but secondary accent colors beyond the blush red (#e99292) are not confirmed
- Spacing values (padding, margins, gaps) were estimated from common e-commerce patterns; actual extracted spacing tokens are not available
- The product card hover state (shadow, border, or scale transform) was not extractable
- The checkout flow (if any) may use different button styles or colors not present on the main site
- Sub-brand or seasonal color palettes (holiday, limited edition) are not documented
- The site may use a different font stack for body copy than what was extracted; Josefin Sans was the most distinctive secondary font found
