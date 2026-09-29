---
version: alpha
name: "Blowout Cards"
source_url: "https://www.blowoutcards.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Blowout Cards runs on anticipation — every page is organized around the moment before a box is cracked, and the UI architecture reflects it: heavy red call-to-action buttons against a near-black persistent header, category grids dense enough to scan forty SKUs without scrolling, and price tags rendered at knockout weight so a $299 hobby box reads as immediately as a $19 blaster. The primary red (approximately #cc1a1a, estimated from brand knowledge — no hex values were extracted from the live site) is the sole voltage color in an otherwise monochrome interface, appearing on "Add to Cart" controls, sale callouts, the wordmark, and badge accents. Without that red, the page would read as a dark-mode corporate catalog; with it, the urgency of a limited-release drop is always present. Body text runs at high density by consumer-retail standards, accommodating the long, hyphenated SKU strings that hobby collectors depend on — "2024 Panini Prizm Football Hobby Box" must fit on one line on a product card without truncation. Navigation is flatter than the catalog depth would suggest: a dark persistent bar holds sport and category links with direct dropdowns, and a forum link surfaces the Blowout Forums community beside the shop header — dual-mode browsing between purchasing and community discussion is a primary use pattern, not an afterthought. Product cards operate at fixed aspect ratios around sealed-box photography, with a "New" or "Hot Deal" badge system providing the site's only secondary color accents (orange for deals, blue-tinted for new releases). The checkout flow is built for multi-item hauls: a persistent mini-cart sits in the header and the cart page encourages bundle building before proceeding, reflecting that a typical session involves four to eight items rather than a single impulse buy. A rotating sale or featured-deal banner occupies the top of every page, functioning as the primary weekly retention mechanism for collectors who return for new set releases. On mobile, the dense category nav collapses into a search-first layout that acknowledges collectors arrive knowing the exact set name they want rather than browsing by category.

colors:
  primary: "#cc1a1a"
  primary-active: "#a81414"
  primary-disabled: "#e8a0a0"
  primary-text-on-light: "#b01010"
  ink: "#111111"
  body: "#2e2e2e"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  surface-dark-mid: "#2a2a2a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  deal-badge: "#e06b00"
  new-badge: "#1560a8"
  in-stock: "#1a8a3a"
  out-of-stock: "#999999"
  pre-order: "#7a44aa"
  sale-banner-bg: "#cc1a1a"
  sale-banner-text: "#ffffff"
  forum-accent: "#cc1a1a"
  star-fill: "#f5a623"

typography:
  display-xl:
    fontFamily: "'Arial Black', 'Impact', 'Franklin Gothic Heavy', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Arial Black', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: 0
  price-lg:
    fontFamily: "'Arial Black', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: 0
  badge-label:
    fontFamily: "Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  sku-label:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 10px
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
    rounded: "{rounded.xs}"
    padding: 10px 18px
    height: 40px
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    height: 40px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 9px 17px
    height: 40px
  button-sm-red:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 30px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 36px
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 44px
    borderBottom: "2px solid {colors.primary}"
  nav-dropdown:
    backgroundColor: "{colors.surface-dark-mid}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    borderTop: "2px solid {colors.primary}"
    padding: "{spacing.sm} 0"
  utility-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 32px
  sale-banner:
    backgroundColor: "{colors.sale-banner-bg}"
    textColor: "{colors.sale-banner-text}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 36px
    submitButtonBackgroundColor: "{colors.primary}"
    submitButtonTextColor: "{colors.on-primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    padding: "{spacing.sm}"
    hoverBorderColor: "{colors.primary}"
  deal-badge:
    backgroundColor: "{colors.deal-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  new-badge:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  pre-order-badge:
    backgroundColor: "{colors.pre-order}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  in-stock-badge:
    textColor: "{colors.in-stock}"
    typography: "{typography.caption-bold}"
  out-of-stock-badge:
    textColor: "{colors.out-of-stock}"
    typography: "{typography.caption-bold}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 4px 12px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  price-strike:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    textDecoration: line-through
  section-header:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    padding: "{spacing.sm} {spacing.base}"
    borderLeft: "4px solid {colors.primary}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    height: 32px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    padding: "{spacing.xxl} {spacing.xl}"
  mini-cart-indicator:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    size: 18px

## Components

### Buttons
**`button-primary`** — The red (#cc1a1a) add-to-cart button is the single most important UI element on the site; it appears on every product card and detail page in a compact 40px height with minimal 2px radius, communicating efficiency over elegance. Hover darkens to `{colors.primary-active}` with no animation delay. Disabled state uses `{colors.primary-disabled}` at full opacity rather than reduced opacity, keeping layout stable.

**`button-sm-red`** — A compact 30px variant used for secondary actions on product cards ("Quick View", "Wishlist"), keeping the primary red language consistent at smaller scale. Used inside card overlays and table-row actions in list-view mode.

**`button-secondary`** — White background with hairline border, used for non-purchase actions like "Continue Shopping" and filter resets. Matches `button-primary` in height so they can sit side by side without vertical misalignment.

### Navigation
**`nav-bar`** — Dark chrome (#1a1a1a) top bar with a 2px red bottom border marking the brand's primary chromatic signature. Nav links are rendered at 13px bold in white, with dropdowns opening against `{colors.surface-dark-mid}` also topped by a 2px red rule. The forum link sits at the far right as a persistent community entry point. Height is kept at 44px — narrower than typical retail navs — to maximize vertical space for dense product grids.

**`utility-bar`** — A near-black bar above the main nav carrying account links, order tracking, and a phone number. Typography is `{typography.caption}` at 12px, ensuring it recedes behind the primary nav without disappearing.

**`sale-banner`** — Full-width red (#cc1a1a) announcement bar directly below the nav, used for sitewide promotions and new release alerts. Text is set in `{typography.title-sm}` bold white, center-aligned. This persists across all page types and is the brand's primary promotional surface.

### Search
**`search-bar`** — A white input field with a red submit button directly attached to the right end, no gap between field and button. This inline submit pattern is faster for collectors who arrive with specific set names to search. The field takes up roughly 40% of the header width on desktop, positioned centrally between the logo and cart.

### Product Cards
**`product-card`** — Cards hold sealed-box photography at a 3:4 portrait ratio, reflecting the physical shape of hobby boxes. Title text runs at `{typography.body-sm}` 13px with no truncation limit — long product names like full set titles are shown in full, wrapping to two lines if needed. Price renders in `{typography.price-display}` red. The card border highlights red on hover as the sole interactive affordance, with no shadow or lift effect. Badges (deal, new, pre-order) stack vertically in the top-left corner of the product image.

**`price-strike`** — Original prices before markdown appear in muted gray with line-through, set in `{typography.caption}` at 12px, sitting directly above the active price. The size contrast between 12px struck-out and 18px active price communicates savings without needing a percentage badge.

### Badges
**`deal-badge`** — Orange (#e06b00) pill in 11px uppercase bold, appearing on products with price promotions. Orange was chosen to avoid competing with the primary red while still reading as urgent.

**`new-badge`** — Medium blue (#1560a8) pill signaling recent releases. The blue/red/orange badge trio gives collectors a quick visual taxonomy: new set (blue), promotional deal (orange), primary purchase action (red).

**`pre-order-badge`** — Purple (#7a44aa) signals upcoming releases not yet in stock, distinguishing them from out-of-stock items which use the muted gray `{colors.out-of-stock}` text label.

### Section Headers
**`section-header`** — Dark background strip with a 4px red left-border accent, used to head product category sections on the homepage and category pages. The left-border stripe is the site's secondary use of red outside of buttons, giving section breaks visual weight without a full-bleed color block.

### Footer
**`footer`** — Dark (#1a1a1a) multi-column layout with white section headings and muted gray links. Column structure: Customer Service, My Account, About Blowout Cards, Connect With Us (social icons). Forum link appears prominently in the Connect column. No color decoration; the darkness of the footer provides sufficient contrast from the white product body.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger nav replaces dark bar; search bar moves to full-width row directly under logo; product grid drops to 2 columns; sale banner text truncates to one line; utility bar hidden |
| Tablet | 744–1128px | Nav links condense to 6 primary categories with "More" overflow; product grid is 3 columns; search bar stays in header row; mini-cart expands to show item count |
| Desktop | 1128–1440px | Full nav bar with all category links visible; 4-column product grid; search occupies center header; utility bar restored |
| Wide | > 1440px | Content max-width constrained to ~1400px with centered layout; product grid stays at 4 columns with wider card padding; hero banners expand to full bleed |

### Touch Targets
- All buttons minimum 40px height on mobile, 44px on touch devices
- Category pills expand padding to 8px vertical on mobile for easier tap
- Product card tap target covers entire card surface, not just title or button
- Nav hamburger target is minimum 44×44px
- Pagination buttons minimum 36px with 4px gap between items

### Collapsing Strategy
- Category nav: top-level sport categories survive to tablet; sub-categories (by sport, by product type) move into hamburger on mobile
- Utility bar collapses entirely on mobile; account and orders accessible via hamburger footer links
- Sale banner remains visible on all breakpoints but reduces to a single-line ticker format on mobile
- Product card badges maintain position and size across all breakpoints (no scaling)
- Footer columns stack to single-column accordion on mobile with expand/collapse per section

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site — JS-rendered styles or anti-bot protection blocked extraction; all color values in this file are estimates based on general brand knowledge and should be verified against the live site or brand assets before production use
- No font-family stacks were extracted; typography uses generic system-sans fallbacks (Arial-based) which may not match the actual typefaces deployed on the site
- Exact primary red value unconfirmed — #cc1a1a is an estimate; the actual value could range from a brighter #dd2020 to a deeper #aa1010
- Deal badge orange (#e06b00) and new-release blue (#1560a8) are inferred from category convention, not extracted
- No theme-color meta tag was present, so OS-level accent color behavior is unknown
- Animation/transition timing values not captured; hover and dropdown behavior timings are guesswork
- Forum (Blowout Forums) visual design system may differ from the main shop and was not analyzed separately
- Mobile nav behavior (hamburger vs. persistent tabs) not confirmed via extraction
- Actual grid column counts on product listing pages were not confirmed from DOM structure
