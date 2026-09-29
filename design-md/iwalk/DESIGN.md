---
version: alpha
name: "iWalk"
source_url: "https://www.iwalkworld.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Four shades of blue graduate from deep #003681 navy through #0045a6 and #2f7bbf to a vivid #0051c3 — iWalk's palette behaves like the charge indicator on one of its own portable power banks, the brightest blue reserved for every primary CTA and add-to-cart pulse. A trio of functional accents — red (#bd2426), green (#9bca3e), and orange (#f68b1f) — marks product-line boundaries, compatibility states, and power-level callouts across a catalog of compact chargers and phone accessories, each hue earning its slot through meaning rather than decoration. The interface chrome runs neutral: #313131 ink on a white canvas, #dedede hairlines dividing specification rows, and #ebebeb surfaces lifting product cards with `{rounded.sm}` corners just enough to separate them from the page grid. Typography draws entirely from the platform-native stack — -apple-system through Roboto and Helvetica Neue — with no custom web font loaded, a decision that trades typographic distinction for guaranteed instant rendering on every device and locale where iWalk ships product. Display type runs heavy at weight 700 in `{typography.display-xl}` for hero headlines, body copy relaxes to weight 400 in `{typography.body-md}`, and specification labels sit at weight 600 in `{typography.spec-label}` to hold their own against dense mAh and wattage data. Product cards carry `{spacing.base}` internal padding and minimal border treatment — the product photography and spec overlays do the persuading. Hero sections run full-bleed with device renders floating on dark `{colors.surface-dark}` backgrounds, technical callouts in `{typography.caption}`, and a single `{colors.primary}` button anchoring the lower third of the composition. Buttons use `{rounded.xs}` with compact horizontal padding — utilitarian and conversion-focused rather than playful. The nav bar sits at 64px with a white background and the iWalk wordmark left-aligned, category links set in `{typography.nav-link}` at weight 600. A sticky add-to-cart bar on product detail pages mirrors the primary button against a white surface with a `{colors.hairline}` top border. The overall system is engineered for catalog density and conversion — tight vertical rhythm, functional color coding, and minimal ornamentation that keeps the focus on mAh ratings, connector types, and product renders.

colors:
  primary: "#0051c3"
  primary-active: "#0045a6"
  primary-disabled: "#8fb8e3"
  navy: "#003681"
  link-blue: "#2f7bbf"
  accent-red: "#bd2426"
  accent-green: "#9bca3e"
  accent-orange: "#f68b1f"
  accent-orange-deep: "#ee730a"
  ink: "#313131"
  body: "#404040"
  muted: "#717171"
  muted-soft: "#9e9e9e"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  border-strong: "#d9d9d9"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  star-rating: "#f68b1f"
  error: "#bd2426"
  success: "#9bca3e"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
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
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.4px
    textTransform: uppercase
  price-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary-active}"
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-accent-orange-active:
    backgroundColor: "{colors.accent-orange-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.error}"
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
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 16px rgba(49, 49, 49, 0.10)"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 520px
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  spec-badge-highlight:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  compatibility-tag:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
  compatibility-tag-warning:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
  product-gallery-thumb:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs}"
    border: "2px solid transparent"
    borderActive: "2px solid {colors.primary}"
    size: 64px
  feature-icon-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    iconSize: 48px
    iconColor: "{colors.primary}"
  sticky-cart-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    height: 64px
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    padding: "{spacing.sm} {spacing.base}"
  promo-banner-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    padding: "{spacing.sm} {spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.on-dark}"
  price-display:
    typography: "{typography.price-lg}"
    textColor: "{colors.ink}"
  price-compare:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    padding: "0 12px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action rendered in iWalk blue (`#0051c3`) with white text at 15px/600 weight. Uses a tight 4px radius (`{rounded.xs}`) that matches the utilitarian, tech-product aesthetic — no playful pills here. On hover, the background deepens to `{colors.primary-active}` (`#0045a6`). The disabled state fades to a soft sky blue (`{colors.primary-disabled}` / `#8fb8e3`), maintaining the blue identity while clearly signaling inactivity. Height sits at 44px to meet touch-target minimums without wasting vertical space in dense product layouts.

**`button-secondary`** — An outlined variant with white fill and a 1px `{colors.primary}` border, used for secondary actions like "Compare" or "Add to Wishlist." On hover, the background shifts to `{colors.surface-soft}` and the border deepens to `{colors.primary-active}`, providing a subtle but clear interaction signal. The 1px inset from the border reduces padding by 1px on each side to maintain visual alignment with primary buttons.

**`button-accent-orange`** — A warm conversion button in `{colors.accent-orange}` (`#f68b1f`), reserved for promotional CTAs like "Shop Sale" or "Limited Offer." Its active state deepens to `{colors.accent-orange-deep}` (`#ee730a`). This orange draws the eye against the blue-dominant interface and is used sparingly — typically once per page — to create urgency without undermining the primary blue hierarchy.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel," "View All," or breadcrumb-style navigation links. Inherits the primary blue color and the same 15px/600 weight typography, with a hover state that adds a subtle underline.

### Cards
**`product-card`** — A white card with 8px radius (`{rounded.sm}`) and a light `{colors.hairline-soft}` border. Product imagery fills the top portion edge-to-edge, while the title, price, and spec badges sit below with `{spacing.base}` padding. The price uses `{typography.price-lg}` in ink, with a compare-at price in `{colors.muted}` struck through when applicable. On hover, the card gains a `boxShadow` of `0 4px 16px rgba(49, 49, 49, 0.10)` and the border strengthens to `{colors.hairline}`, creating a gentle lift that signals interactivity.

**`product-card-hover`** — The elevated hover state of the product card. The shadow is deliberately light — this is a tech catalog, not a lifestyle editorial, and the interaction feedback should feel precise rather than dramatic.

### Navigation
**`nav-bar`** — A fixed 64px white navigation bar with a `{colors.hairline-soft}` bottom border. The iWalk logo sits left-aligned, with category links ("Power Banks," "Cables," "Accessories") rendered in `{typography.nav-link}` at 14px/600 weight. Active links receive a 2px bottom border in `{colors.primary}`, while inactive links display in `{colors.muted}`. Cart and search icons sit right-aligned at 24px. The nav bar stays white on scroll — no transparency or blur effects.

**`nav-link-active`** — Distinguished by a 2px primary-blue bottom border. The blue underline provides clear wayfinding without needing background pills or weight changes that would shift layout.

**`nav-link-inactive`** — Default links in `{colors.muted}` (`#717171`), ensuring the active link stands out. On hover, text transitions to `{colors.ink}` before the active underline appears on click.

### Forms
**`text-input`** — A 44px input with white background, 4px radius, and a `{colors.hairline}` border. On focus, the border transitions to `{colors.primary}` (`#0051c3`) with no other visual change — the blue focus ring is distinctive enough against the neutral chrome. Error states swap the border to `{colors.error}` (`#bd2426`), borrowing the red accent from the product-line palette.

### Spec Badges
**`spec-badge`** — Small inline badges used on product cards and detail pages to surface key specifications: "5000mAh," "20W PD," "MagSafe," "USB-C." Rendered in `{typography.spec-label}` at 12px/600 weight on a `{colors.surface-soft}` background with 4px radius. These badges are the workhorse of iWalk's information architecture — every product card carries two to four of them, and they do more selling than the product titles.

**`spec-badge-highlight`** — A variant with `{colors.primary}` background and white text, used to call out the most compelling spec on a product (e.g., "45W Fast Charge" or "Built-in Cable"). Only one highlight badge should appear per product card to maintain visual hierarchy.

### Compatibility Tags
**`compatibility-tag`** — Full-rounded pills in `{colors.accent-green}` (`#9bca3e`) indicating device compatibility: "iPhone 15," "Galaxy S24," "USB-C Laptops." The green signals positive compatibility. Uses `{typography.badge}` at 11px/600 weight with uppercase transform.

**`compatibility-tag-warning`** — An orange variant (`{colors.accent-orange}`) for partial or conditional compatibility, such as "Adapter Required" or "5W Only." The color distinction between green (full support) and orange (partial) is critical for a brand selling across dozens of device types.

### Product Gallery
**`product-gallery-thumb`** — 64px square thumbnails with a `{colors.surface-soft}` background and 4px radius. The active thumbnail receives a 2px `{colors.primary}` border, making the selection state unmistakable. Inactive thumbnails use a transparent border to prevent layout shift on selection. Thumbnails are spaced with `{spacing.sm}` gaps in a horizontal row below the main product image.

### Feature Icon Card
**`feature-icon-card`** — A card component used in feature-grid sections on product detail pages, presenting a single benefit with a 48px icon in `{colors.primary}` above a short description in `{typography.body-sm}`. The card has `{spacing.lg}` padding and `{rounded.sm}` corners. Typical uses include "Compact Design," "Pass-Through Charging," "Airline Safe," and "LED Indicator." The icon color always matches the primary blue to maintain brand coherence across the grid.

### Sticky Cart Bar
**`sticky-cart-bar`** — A 64px bar that fixes to the bottom of product detail pages on scroll, containing the product name, price, and a primary CTA button. The bar has a white background with a `{colors.hairline}` top border separating it from page content. Padding uses `{spacing.sm}` vertical and `{spacing.base}` horizontal. On mobile, this bar becomes the primary add-to-cart interaction, replacing the inline button that scrolls out of view.

### Promo Banner
**`promo-banner`** — A 40px slim banner fixed above the nav bar, used for site-wide messages like "Free Shipping on Orders $35+" or "New: LinkPod Pro Available Now." Default state uses `{colors.primary}` background with white text in `{typography.caption}`. The sale variant swaps to `{colors.accent-red}` (`#bd2426`) for clearance or flash-sale events.

### Search
**`search-bar`** — A 40px search input with `{colors.surface-soft}` background and `{rounded.sm}` corners, positioned in the nav bar. On focus, the background switches to white and a 1px `{colors.primary}` border appears. The slightly shorter height (40px vs. 44px for buttons) signals its utility role without competing with primary CTAs.

### Footer
**`footer`** — A full-width footer in `{colors.ink}` (`#313131`) with link columns rendered in `{colors.muted-soft}` (`#9e9e9e`) using `{typography.body-sm}`. Links brighten to white (`{colors.on-dark}`) on hover. The footer uses `{spacing.section}` vertical padding to create clear separation from page content. Bottom row contains legal links, copyright, and payment-method icons.

### Pricing & Ratings
**`price-display`** — The current product price in `{typography.price-lg}` (24px/700 weight) in ink. The heavy weight makes the price the most visually prominent text element on any product card or detail page.

**`price-compare`** — The original price shown alongside discounted items, rendered in `{colors.muted}` with a line-through decoration. Always appears to the right of or below the current price.

**`rating-stars`** — Star icons in `{colors.star-rating}` (`#f68b1f`) at 16px. The orange star color matches the accent-orange palette, creating a warm, recognizable rating element that stands apart from the blue-and-gray interface.

### Quantity Selector
**`quantity-selector`** — A compact minus/number/plus input with `{colors.surface-soft}` background and `{rounded.xs}` corners. The 44px height aligns with text inputs and buttons. Plus and minus buttons sit at the edges with the count centered in `{typography.body-md}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces nav links, hero text drops to `{typography.display-md}`, sticky cart bar becomes primary CTA surface, spec badges wrap to two rows, full-width buttons |
| Tablet | 744-1128px | Two-column product grid, nav collapses to icon + hamburger hybrid, hero maintains `{typography.display-lg}`, search bar collapses to icon, feature-icon-cards shift to 2x2 grid |
| Desktop | 1128-1440px | Three- to four-column product grid, full top nav with all category links visible, hero uses `{typography.display-xl}`, search bar expands inline, feature grids run four-across |
| Wide | > 1440px | Max-width container (1440px) centered on canvas, four-column product grid with increased card padding, hero images scale proportionally, additional whitespace in section spacing |

### Touch Targets
- All buttons maintain a minimum 44px touch height across breakpoints.
- Nav icon buttons (cart, search, menu) use 24px icons with 44px touch padding.
- Product card tap areas span the full card surface; the "Add to Cart" quick-action on mobile has a minimum 48px target.
- Spec badges and compatibility tags maintain 32px minimum tap height with `{spacing.xs}` internal padding.
- Quantity selector plus/minus buttons are 44px square touch targets.

### Collapsing Strategy
- The top nav collapses to a hamburger + logo + cart-icon layout below 744px, with a slide-out drawer containing category links, search, and account access.
- Search collapses to a magnifying-glass icon on mobile, expanding to a full-width overlay input on tap.
- Product grids collapse from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile), with card aspect ratios held constant.
- Feature-icon-card grids collapse from 4-across to 2x2 on tablet to vertically stacked on mobile.
- Footer link columns stack vertically on mobile, each section collapsing into an accordion.
- The sticky cart bar is hidden on desktop (inline CTA is visible) and appears only on mobile/tablet when the inline add-to-cart button scrolls out of the viewport.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The live site returned a 522 (Connection timed out) during extraction, so all design data is partial — colors and font stacks were recovered from whatever resources loaded before the timeout.
- No custom brand typeface was detected; the site may load a proprietary or licensed font via JavaScript that did not execute during extraction. The system font stack used here is a best-effort fallback.
- No meta theme-color was found; the mobile browser chrome color is unknown.
- Hover states, transitions, and animation durations could not be observed; all hover colors are inferred from the extracted palette.
- Dark mode tokens are not available — the site shows no evidence of a dark theme toggle.
- The exact border-radius values used on the live site could not be confirmed; the `{rounded.xs}` (4px) and `{rounded.sm}` (8px) values used here are inferred from the brand's tech-product visual language.
- Product-line-specific color assignments (which accent color maps to which charger family) could not be verified from the partial extraction.
- Focus ring styles (outline color, offset, box-shadow) are not documented.
- Modal, drawer, and overlay scrim opacity values are not available.
- The site is not on Shopify; the underlying platform and its default component conventions are unknown.
- Icon set (line vs. filled, stroke width, sizing grid) could not be determined from the extraction.
- Promotional or seasonal palette overrides (Black Friday, holiday themes) are undocumented.
