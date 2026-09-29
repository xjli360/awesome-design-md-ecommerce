---
version: alpha
name: "Trek"
source_url: "https://www.trekbikes.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep marine #003344 anchors Trek's digital presence — not a sporty electric blue but the color of a mountain lake at dusk, suggesting endurance and depth rather than speed. This primary sits alongside a warm metallic accent #b79b65, a gold that appears in price callouts, sale badges, and hover states, evoking the precision of a derailleur gear rather than luxury. The canvas is a cool off-white #ebf2fb, a blue-tinted surface that keeps the bike photography feeling crisp and alpine, while the secondary canvas #edebe0 introduces a warmer, more tactile paper-like tone for product detail sections. Typography runs Roboto at modest weights — body copy at 400, buttons at 500, and display weights rarely exceed 600 — letting the geometry of carbon frames and the gloss of component close-ups carry the visual load. Navigation is a persistent dark band (#1a1a1a) with white text, a confident framing device that separates Trek from the white-header convention of most DTC cycling brands. Buttons are softly rectangular ({rounded.sm} ~8px), never pill-shaped, and the primary CTA (#003344) shifts to a lighter navy (#005a85) on hover, a subtle brightening that feels like emerging from shadow. The checkout flow introduces a safety-yellow accent (#f9c929) for promotional banners and urgency indicators, a rare splash of high-energy color in an otherwise restrained palette. Product cards use a generous {rounded.md} (12px) and a hairline border (#e5e5e5) that keeps the layout airy without floating. The overall mood is serious, technical, and quietly premium — a brand that trusts the engineering of its bikes more than any design flourish.

colors:
  primary: "#003344"
  primary-active: "#005a85"
  primary-disabled: "#8baec2"
  ink: "#1a1a1a"
  body: "#484848"
  muted: "#767676"
  muted-soft: "#a0a0a0"
  hairline: "#e5e5e5"
  hairline-soft: "#edebe0"
  canvas: "#ebf2fb"
  surface-soft: "#f8fafc"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#b79b65"
  accent-gold-hover: "#caa148"
  accent-gold-light: "#f8eebc"
  accent-yellow: "#f9c929"
  accent-yellow-soft: "#ffface"
  badge-red: "#c13515"
  badge-green: "#1e7e34"
  link-blue: "#003399"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-md:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-md:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
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
    padding: 12px 28px
    height: 44px
  button-primary-hover:
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
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-gold-hover:
    backgroundColor: "{colors.accent-gold-hover}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.badge-red}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 40px 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-bar-scrolled:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    height: 48px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.accent-gold}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0, 51, 68, 0.1)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.price-md}"
    color: "{colors.primary}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-price-sale:
    color: "{colors.badge-red}"
  product-card-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    height: 500px
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.3
  hero-banner-cta:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.accent-gold}"
  footer-heading:
    color: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    textTransform: uppercase
    letterSpacing: "1px"
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  accordion-hover:
    backgroundColor: "{colors.surface-soft}"
  accordion-content:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "{spacing.base} {spacing.base} {spacing.lg}"
  promo-banner:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  promo-banner-strong:
    backgroundColor: "{colors.accent-yellow-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    fontWeight: 500
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} 0"
  breadcrumb-active:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.hairline}"
    padding: "0 {spacing.xs}"
  filter-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  filter-chip-hover:
    border: "1px solid {colors.primary}"
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  size-selector-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "2px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  rating-stars:
    color: "{colors.accent-gold}"
    size: 16px
  rating-count:
    color: "{colors.muted}"
    typography: "{typography.caption}"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    borderBottom: "1px solid {colors.hairline}"
  tab-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  tab-hover:
    color: "{colors.ink}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 10px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Buy Now", and "Find a Dealer". Rendered in the deep marine {colors.primary} with white text and an 8px radius ({rounded.sm}). On hover, the background brightens to {colors.primary-active} (#005a85), creating a subtle lift. The disabled state uses {colors.primary-disabled} with reduced contrast. Padding is generous at 12px 28px, giving the button a solid, grounded feel that matches the brand's engineering ethos.

**`button-secondary`** — An outlined variant used for secondary actions like "Compare" and "View Details". Uses a white background with a 2px {colors.primary} border and primary-colored text. On hover, the button fills with {colors.primary} and text inverts to white, providing a clear hierarchy against the primary button.

**`button-ghost`** — A text-only button with no background or border, used for less prominent actions like "Learn More" or "Cancel". Maintains the same typography and padding as the primary button but relies on color alone for affordance. Hover state adds a subtle background tint.

**`button-gold`** — A special variant reserved for high-value actions like "Customize Your Bike" or "Book a Test Ride". Uses the warm metallic {colors.accent-gold} with dark ink text, creating a premium visual cue that stands apart from the standard primary/secondary hierarchy. On hover, the gold deepens to {colors.accent-gold-hover}.

### Cards
**`product-card`** — The core product display unit, used in grid layouts across category pages and search results. A white card with a 1px {colors.hairline} border and 12px radius ({rounded.md}). The image area occupies the top with a 4:3 aspect ratio and rounded top corners only. Below, the title uses {typography.title-sm} in {colors.ink}, and the price uses {typography.price-md} in {colors.primary}. Sale prices switch to {colors.badge-red}. On hover, the card gains a {colors.primary} border and a subtle box shadow, signaling interactivity without overwhelming the photography.

**`product-card-badge`** — Overlaid on the product image to indicate special status. Three variants exist: a gold badge ({colors.accent-gold}) for "Best Seller" or "Staff Pick", a navy badge ({colors.primary}) for "New", and a red badge ({colors.badge-red}) for "Sale". All use uppercase 11px bold type with tight letter-spacing and a 4px radius.

### Navigation
**`nav-bar`** — A persistent dark header ({colors.ink}) that spans the full viewport width at 60px height. Navigation links are uppercase 14px medium-weight Roboto with 0.5px letter-spacing, rendered in white. The active page link shifts to {colors.accent-gold}, providing a subtle but clear wayfinding cue. On scroll, the nav bar compresses to 48px. The logo sits left-aligned in white, and the right side contains the search icon, account link, and cart icon.

**`nav-link`** — Individual navigation items within the top bar. White text with 8px 16px padding for comfortable tap targets. Active state uses {colors.accent-gold}. Dropdown menus appear on hover with a white surface and {colors.hairline} borders.

### Forms
**`text-input`** — Standard text input used for search, account forms, and checkout. A white background with 1px {colors.hairline} border, 8px radius, and 44px height. On focus, the border thickens to 2px {colors.primary}. Error state uses a 2px {colors.badge-red} border. Placeholder text uses {colors.muted}.

**`select-input`** — Custom select dropdown for filtering and sorting. Matches the text-input styling but includes a 40px right padding to accommodate a custom chevron icon. The dropdown menu appears as a white overlay with {colors.hairline} borders and {colors.body} text.

**`filter-chip`** — Pill-shaped filter toggles used in category navigation and product listing filters. A white background with 1px {colors.hairline} border and full rounding. Active state fills with {colors.primary} and inverts text to white. Hover state adds a {colors.primary} border.

### Footer
**`footer`** — A full-width dark section ({colors.ink}) with white text, using {spacing.xxl} top/bottom padding and {spacing.section} horizontal padding. Links are 14px regular weight in white, shifting to {colors.accent-gold} on hover. Section headings use {typography.title-sm} in white with uppercase transformation and 1px letter-spacing. The footer typically contains 4-5 columns of links (Shop, Support, About, Legal) plus a newsletter signup and social media icons.

### Promotional Elements
**`promo-banner`** — A full-width banner at the top of the page (below the nav) for promotions, free shipping offers, or financing deals. Uses the safety-yellow {colors.accent-yellow} background with dark ink text, creating high visibility. The strong variant uses {colors.accent-yellow-soft} with medium-weight body text for more important announcements.

**`hero-banner`** — The primary hero section on the homepage and campaign pages. A full-width dark background ({colors.ink}) at 500px height with a semi-transparent overlay ({colors.scrim} at 30% opacity) over the background image. The headline uses {typography.display-xl} in white, and the CTA uses the gold button variant for maximum contrast.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked footer, reduced hero height to 300px, filter chips wrap to two rows |
| Tablet | 744–1128px | Two-column product grid, expanded nav with dropdowns, 4-column footer, hero at 400px |
| Desktop | 1128–1440px | Three-column product grid, full nav bar, 5-column footer, hero at 500px |
| Wide | > 1440px | Max-width container at 1440px, centered content, four-column product grid |

### Touch Targets
- All interactive elements maintain a minimum 44px height for touch accessibility
- Filter chips are 40px tall with 16px horizontal padding
- Product card tap targets extend to the full card area
- Nav links have 8px 16px padding, ensuring comfortable tap zones
- Quantity selector buttons are 40px × 40px

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with the logo centered
- Product filters collapse into a slide-out drawer on mobile, triggered by a "Filter" button
- Footer columns collapse into accordion sections below 744px, with the first column (Shop) expanded by default
- Product image galleries collapse from a multi-thumbnail layout to a single swipeable carousel
- Size and color selectors collapse from inline grids to horizontal scrollable strips

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card badges and filter chips were inferred from common patterns but not directly extracted from the live site
- Error and success messaging styling (form validation, toast notifications) could not be reliably extracted
- Dark mode preferences and associated color tokens are not present in the extracted data
- The extracted font list only includes Roboto and generic fallbacks; the brand may use a secondary display font for headlines that wasn't captured
- Sub-brand palettes (Trek Racing, Trek Travel, Electra by Trek) could not be isolated from the main brand palette
- Checkout flow colors (Shopify Pay buttons, Klarna badges) were filtered but some may remain in the extracted hex list — the primary palette was selected based on frequency and brand alignment
- Animation durations, easing curves, and transition properties were not extracted
- The extracted hex list contains several gold/amber tones (#f8eebc, #e6d08f, #caa148, #c0902e, #ecd587, #f9c929) that suggest a more complex accent system than documented — the gold hierarchy above is a best-guess consolidation
- Iconography style (stroke weight, filled vs outlined) was not captured
- The meta theme-color was absent from the extracted data, suggesting it may not be set or may be dynamically applied
