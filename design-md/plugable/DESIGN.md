---
version: alpha
name: "Plugable"
source_url: "https://www.plugable.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A performance-first electronics brand that communicates reliability through a deep green anchor (#006341) and a secondary green (#267e47) that together form a consistent, trustworthy ecosystem across docking stations, USB hubs, and charging accessories. The palette is notably industrial — a slate gray (#5c677a) handles secondary text and muted UI elements, while a crisp red (#ce3525) appears sparingly as an alert or sale accent, never competing with the primary green. The canvas (#f4f4f4) is a soft off-white that reduces eye strain during long browsing sessions, with cards and surfaces lifted by white (#ffffff) and a hairline (#e2e2e2) that defines boundaries without visual weight. Typography runs proxima-nova as the brand face, a geometric sans-serif with moderate contrast that reads clearly at small sizes on product spec tables. Buttons and CTAs use the primary green with white text, corners at {rounded.sm} — a deliberate choice that avoids the overly friendly pill shape of consumer social apps and signals professional-grade hardware. The brand's Shopify platform means checkout flows inherit a separate visual system (Shopify Pay buttons, Klarna badges), but the Plugable storefront maintains its own identity: product cards with clean photography, spec-heavy descriptions set in {typography.body-sm}, and a navigation bar that prioritizes category hierarchy over promotional noise. The overall impression is of a company that sells tools, not toys — the green says "certified, tested, works with everything," and the layout gives you the specifications before the marketing copy.

colors:
  primary: "#006341"
  primary-active: "#005234"
  primary-disabled: "#80b1a0"
  ink: "#111100"
  body: "#5c677a"
  muted: "#88888d"
  muted-soft: "#b3d0c6"
  hairline: "#e2e2e2"
  hairline-soft: "#dedede"
  canvas: "#f4f4f4"
  surface-soft: "#fbfbfb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#ce3525"
  accent-gold: "#f9b434"
  accent-blue: "#3793ff"
  star-rating: "#f9b434"
  sale-badge: "#ce3525"
  new-badge: "#006341"
  tech-spec-bg: "#f7f7f7"
  footer-bg: "#262626"
  footer-text: "#ebebeb"

typography:
  display-xl:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-strong:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  link:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.25px
  price-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0

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
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 16px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
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
    rounded: "{rounded.sm}"
    padding: 16px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 16px
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-compare-price:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    textDecoration: "line-through"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.star-rating}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
    marginTop: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "2px solid {colors.primary}"
  search-icon:
    textColor: "{colors.muted}"
    height: 20px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
    textDecoration: "none"
  footer-link-hover:
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    textDecoration: "underline"
  footer-heading:
    textColor: "{colors.footer-text}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"
  tech-spec-table:
    backgroundColor: "{colors.tech-spec-bg}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  tech-spec-label:
    textColor: "{colors.ink}"
    typography: "{typography.caption-strong}"
  tech-spec-value:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  accordion-header:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    textDecoration: "underline"
  breadcrumb-current:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    height: 32px
    width: 32px
  add-to-cart-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    padding: "{spacing.base}"
    borderTop: "1px solid {colors.hairline}"
    position: "sticky"
    bottom: 0
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  category-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  category-nav-item:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.xs}"
  category-nav-item-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the storefront. Uses the brand green (#006341) background with white text in proxima-nova semibold at 16px. Corners are softly squared at {rounded.sm} (8px), a deliberate choice that reads as professional rather than playful. On hover, the background shifts to {colors.primary-active} (#005234). The disabled state uses {colors.primary-disabled} (#80b1a0), a muted sage that signals unavailability without visual noise.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "Compare." White background with a 2px solid {colors.primary} border and green text. Hover state darkens the border to {colors.primary-active}. Height matches the primary button at 48px for consistent alignment in forms and product cards.

**`button-accent-red`** — Reserved for sale or clearance actions. Uses {colors.accent-red} (#ce3525) as background, white text. Appears on product cards with discounted pricing or in promotional banners. The red is intentionally less saturated than a pure alert red — it reads as "deal" rather than "danger."

**`button-tertiary-text`** — A text-only button for inline actions like "View Details" or "Cancel." Transparent background, {colors.primary} text, no border. Used in accordion headers, modals, and as secondary actions within product detail pages.

**`button-sm`** — A compact version at 36px height for use in cart line items, wishlist actions, and mobile navigation. Uses {colors.primary} background with {typography.button-sm} (14px semibold). Padding is reduced to 8px 16px.

### Cards
**`product-card`** — The core product display unit. White background with a soft {colors.hairline-soft} (#dedede) border and {rounded.sm} corners. Contains a square aspect-ratio image area with {colors.surface-soft} (#fbfbfb) background for loading states. Title uses {typography.title-sm} (16px semibold), price uses {typography.price-sm} (16px bold), and rating stars render in {colors.star-rating} (#f9b434). On hover, the border switches to {colors.primary} and a subtle box shadow lifts the card — the only animation on the product grid, keeping the experience spec-focused rather than flashy.

**`product-card-badge`** — Overlaid on the top-left of product images. Sale badges use {colors.sale-badge} (#ce3525) background with white uppercase text at 11px bold. New-arrival badges use {colors.new-badge} (#006341). Badges are compact at 2px 8px padding with {rounded.xs} corners.

### Navigation
**`nav-bar`** — Fixed-height top navigation at 72px. White background with a 1px bottom border in {colors.hairline} (#e2e2e2). Logo sits left-aligned, category links center-aligned, and utility icons (search, account, cart) right-aligned. Active nav links render in {colors.primary}, inactive in {colors.body} (#5c677a). The nav does not use a sticky position — it scrolls with the page, reinforcing the content-first hierarchy.

**`category-nav`** — A secondary horizontal strip below the hero or above product grids. Light {colors.canvas} (#f4f4f4) background with category items as inline links. Active category uses a {colors.primary} pill background with white text; inactive items use {colors.body} text on transparent background. This pattern helps users navigate product subcategories (Docking Stations, USB Hubs, Chargers, Cables) without leaving the product listing page.

### Forms
**`text-input`** — Standard input field at 48px height with white background, 1px {colors.hairline} border, and {rounded.sm} corners. Placeholder text renders in {colors.muted} (#88888d). On focus, the border thickens to 2px and switches to {colors.primary} — a clear but understated focus indicator. Used in search, newsletter signup, and checkout address forms.

**`select-dropdown`** — Matches the text-input dimensions and styling. Used for product sorting (Price Low-High, Best Sellers, Newest), quantity selection, and filter options. The dropdown arrow is styled in {colors.muted}.

**`quantity-selector`** — A compact inline control for cart line items. White background with {colors.hairline} border, 40px height. Contains minus/plus buttons at 32px square with {colors.primary} text. The numeric value sits center-aligned in {typography.body-md}.

### Footer
**`footer`** — Full-width dark section at {colors.footer-bg} (#262626) with light text (#ebebeb). Organized into columns with {typography.title-sm} headings and {typography.body-sm} link lists. Footer links are white with no underline by default; on hover they turn {colors.primary} and gain an underline. The footer includes trust badges (free shipping, 30-day returns, 2-year warranty) rendered as {colors.surface-soft} pills with {colors.muted} text.

### Product Detail
**`tech-spec-table`** — A key differentiator for Plugable's audience. Light gray background (#f7f7f7) with two-column layout: labels in {colors.ink} semibold, values in {colors.body} regular. Used for port specifications, compatibility lists, power ratings, and physical dimensions. The table has {rounded.sm} corners and {spacing.base} internal padding.

**`accordion-header`** — Used on product detail pages for sections like "What's in the Box," "Compatibility," and "Downloads." White background with {colors.ink} text in {typography.title-sm}. A chevron icon rotates on open state. The header has a bottom border in {colors.hairline-soft} to separate sections.

**`breadcrumb`** — Navigation trail above product titles. Uses {typography.caption} (12px) in {colors.muted} for separators (">"), {colors.body} for clickable links with underline, and {colors.ink} for the current page label. This pattern helps users navigate category hierarchies like "Home > Docking Stations > USB-C Docking Stations."

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row), nav collapses to hamburger menu, hero banner reduces to 250px min-height, category nav becomes a horizontal scrollable strip, footer stacks to single column, product cards use full-width layout, tech-spec table switches to stacked label-value pairs |
| Tablet | 744–1128px | Two-column product grid (2 cards per row), nav shows top-level categories with dropdown for subcategories, hero banner at 350px min-height, footer in 2-column grid, product detail page uses side-by-side layout for image and specs |
| Desktop | 1128–1440px | Three-column product grid (3 cards per row), full nav with all categories visible, hero banner at 400px min-height, footer in 4-column grid, product detail page with sticky add-to-cart sidebar |
| Wide | > 1440px | Four-column product grid (4 cards per row), max-width container at 1440px centered, hero banner at 450px min-height with wider content padding, product detail page uses full-width image gallery |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets (title, image, add-to-cart) are at least 48px tall
- Quantity selector buttons are 32px square — below the 44px recommendation but acceptable for the compact cart interface; consider increasing to 40px in future iterations
- Mobile nav hamburger icon is 44px square
- Category nav items on mobile have 44px tap targets with adequate spacing

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-out drawer for category links
- Product filters collapse to a "Filter" button that opens a modal overlay on mobile
- Product description accordions are collapsed by default on all breakpoints, with the first accordion open on desktop
- Footer link groups collapse to accordion-style expandable sections on mobile, saving vertical space
- Hero banner text and CTA stack vertically on mobile, with the CTA button expanding to full width
- Product image galleries collapse from thumbnail strip to swipeable carousel on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons, text links, and category nav items were inferred from common patterns; actual extracted hover colors were not available
- Error states for form inputs (validation colors, error messages) were not extracted — the red accent (#ce3525) is a candidate for error borders but this is unconfirmed
- Dark mode is not supported on the live site; no dark palette tokens exist
- The extracted font list includes "Font Awesome 5 Pro" as a font-family declaration — this is likely used for icons but no icon-specific styling was captured
- Shopify checkout pages use a separate design system (Shopify's own) that overrides Plugable's brand colors; the extracted palette includes colors from checkout widgets (#19c37d, #0bab69, #068e56) that are not part of the brand's storefront
- The extracted color list is heavily polluted with framework defaults and third-party widget colors — the true brand palette is likely smaller (approximately 8-10 core colors) than the 30 extracted hexes suggest
- Typography scale for display sizes (display-xl through display-sm) was estimated based on common e-commerce patterns; exact font sizes were not extractable from the live site
- Spacing scale was inferred from common Shopify themes; the actual spacing system may differ
- Product card hover shadow values (boxShadow) were not extractable — the reference uses a generic 0 2px 8px rgba(0,0,0,0.08) as a reasonable default
- The brand's logo color and any sub-brand color variations were not captured
- Accessibility contrast ratios between text and background colors have not been verified against WCAG standards
- Animation durations and easing curves for transitions (hover states, accordion toggles, mobile menu) were not extracted
- The "proxima-nova" font may require a paid license; fallback stacks assume system fonts as secondary options
