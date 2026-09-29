---
version: alpha
name: "Ubisoft Store"
source_url: "https://store.ubisoft.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A darkly atmospheric game storefront where #0a0a0a ink meets a cyan voltage of #008aa4, the primary that pulses through every CTA, badge, and hover state. The palette reads like a night-ops briefing: #c8cedd and #e5e8f0 form the muted silver of secondary text and hairline borders, while #00c248 and #1bc55a inject a neon-game-green for wishlist hearts and sale badges. Ubisoft Sans — a proprietary geometric sans — carries the brand's weight at display sizes with a crisp 600 weight, while body copy settles into Roboto for readability across game descriptions and system menus. The top nav is a persistent black bar (#0a0a0a) with white text, housing a full-width search field with a #008aa4 focus ring and a cart icon that glows the same cyan on hover. Product cards use a #fefefe canvas with #e6e6e6 borders and a subtle shadow, but the real signature is the "Add to Cart" button: a #008aa4 pill with white text, 48px tall, that shifts to #0058c4 on active and #007a91 on hover — a three-state cyan gradient that feels both gamey and trustworthy. Badges for pre-order, sale, and "New" use #ffdd00 gold, #cc4b37 red, and #00c248 green respectively, each with white text and a 4px radius. The footer is a dense #0a0a0a slab with #444444 dividers, legal links in #428ee0, and social icons in #929db6. Every corner is either sharp (0px on nav and cards) or softly rounded (8px on buttons, 4px on badges) — no pill extremes except the search bar, which uses a 20px radius to feel approachable. The overall mood is "premium gaming utility": dark, high-contrast, with cyan as the single source of brand heat.

colors:
  primary: "#008aa4"
  primary-active: "#0058c4"
  primary-disabled: "#66dae6"
  ink: "#0a0a0a"
  body: "#444444"
  muted: "#8a8a8a"
  muted-soft: "#929db6"
  hairline: "#e6e6e6"
  hairline-soft: "#f2f2f2"
  canvas: "#fefefe"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#ffdd00"
  accent-red: "#cc4b37"
  accent-green: "#00c248"
  accent-green-hover: "#1bc55a"
  accent-purple: "#7469ff"
  accent-purple-soft: "#9b93ff"
  link-blue: "#428ee0"
  link-blue-hover: "#006ef5"
  social-gray: "#929db6"
  footer-divider: "#444444"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Ubisoft Sans', 'Ubisoft Sans Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Ubisoft Sans', 'Ubisoft Sans Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Ubisoft Sans', 'Ubisoft Sans Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Ubisoft Sans', 'Ubisoft Sans Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Ubisoft Sans', 'Ubisoft Sans Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Ubisoft Sans', 'Ubisoft Sans Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Ubisoft Sans', 'Ubisoft Sans Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Ubisoft Sans', 'Ubisoft Sans Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "Roboto, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Ubisoft Sans', 'Ubisoft Sans Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-primary-hover:
    backgroundColor: "#007a91"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
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
    padding: 13px 23px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-ghost-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  top-nav-item-hover:
    textColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 12px 16px
    height: 48px
  search-bar-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-discount:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-preorder:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.link-blue-hover}"
  footer-divider:
    backgroundColor: "{colors.footer-divider}"
    height: 1px
  social-icon:
    textColor: "{colors.social-gray}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  social-icon-hover:
    textColor: "{colors.canvas}"
  wishlist-button:
    backgroundColor: transparent
    textColor: "{colors.accent-green}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
  wishlist-button-active:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
  rating-star:
    textColor: "{colors.accent-gold}"
    fontSize: 16px
  platform-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the store. Rendered as a solid #008aa4 pill with white text, 48px tall, using Ubisoft Sans at 15px weight 600. On hover, the background shifts to #007a91 — a slightly deeper cyan — and on active press it deepens further to #0058c4. The disabled state uses #66dae6, a pale cyan that maintains readability without inviting interaction. Padding is 14px horizontal, 24px vertical, with an 8px border radius that feels soft but not pill-like. **`button-secondary`** — An outlined variant with a white background, #0a0a0a text, and a 1px #e6e6e6 border. Hover fills the background with #f2f2f2. Used for "Learn More" and secondary purchase paths. **`button-ghost`** — Transparent background with #008aa4 text, used for text-based actions like "View Details" in tight spaces. Hover adds a #f8f8f8 background. **`icon-button`** — A 40x40px square with transparent background and #8a8a8a icon color, used for cart, search, and menu toggles. Hover fills with #f8f8f8 and darkens the icon to #0a0a0a.

### Navigation
**`top-nav`** — A persistent 64px black bar (#0a0a0a) spanning the full viewport width. Navigation links use Ubisoft Sans at 14px weight 500, uppercase with 0.5px letter spacing, rendered in white. On hover, link text shifts to #008aa4. The bar contains the Ubisoft logo (left), a full-width search bar with a #008aa4 focus ring, and a cart icon that glows cyan on hover. The search bar itself is a white pill with 20px radius, 48px tall, with placeholder text in #8a8a8a. Below the top nav, a secondary category strip (also black) holds genre links (Action, RPG, Strategy, etc.) in the same uppercase style.

### Cards
**`product-card`** — A white card (#fefefe) with no border radius — sharp corners that contrast with the soft buttons. The card contains a full-width game art image (16:9 ratio), a title in Ubisoft Sans 16px weight 500, a price in Roboto 16px weight 400 (#444444), and optional discount badges. The card has a subtle shadow (0 2px 8px rgba(0,0,0,0.08)) on hover. Discount badges use #00c248 background with white text, 11px uppercase, 4px radius, positioned top-left on the image. Pre-order badges use #ffdd00 gold with black text; "New" badges use #00c248 green; sale badges use #cc4b37 red. A wishlist heart icon sits top-right, initially transparent with a #00c248 outline, filling solid green on active.

### Forms
**`text-input`** — Standard input fields use a white background, #e6e6e6 border (1px), 12px border radius, and Roboto 16px text. Focus state swaps the border to #008aa4 with a 2px width. Error state uses #cc4b37 border with a #cc4b37 caption below. Placeholder text is #8a8a8a. Height is 48px with 12px horizontal padding.

### Footer
**`footer`** — A dense black slab (#0a0a0a) with #444444 horizontal dividers between sections. Links use #428ee0 blue on Roboto 14px, shifting to #006ef5 on hover. Social media icons are 32px circles in #929db6, turning white on hover. The footer contains columns for Support, Legal, Community, and About, with the Ubisoft logo and copyright in #8a8a8a at the bottom.

### Badges & Tags
**`badge-preorder`** — Gold (#ffdd00) background with black text, 11px uppercase Ubisoft Sans weight 700, 4px radius, 2px vertical / 8px horizontal padding. **`badge-new`** — Green (#00c248) background with white text, same typography. **`badge-sale`** — Red (#cc4b37) background with white text. **`platform-badge`** — A muted tag (#f8f8f8 background, #8a8a8a text) for platform indicators (PC, PS5, Xbox), 12px Roboto, 4px radius, 4px/8px padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; search bar moves to a full-width overlay; product cards stack in single column; footer columns stack vertically; badges scale to 10px font |
| Tablet | 744–1128px | Top nav shows limited links (Logo, Search, Cart, Menu); product cards display in 2-column grid; footer shows 2-column layout; search bar remains visible but shrinks to 40px height |
| Desktop | 1128–1440px | Full top nav with all links; product cards in 3-column grid; footer in 4-column layout; search bar at full 48px height |
| Wide | > 1440px | Max-width container (1440px) centered; product cards in 4-column grid; additional whitespace around content; footer columns expand to 5 |

### Touch Targets
- All buttons and interactive elements minimum 44x44px on mobile
- Search bar tap target 48px tall
- Icon buttons 40x40px (44x44px on mobile with padding)
- Wishlist heart 40x40px hit area
- Navigation links minimum 44px tall tap area

### Collapsing Strategy
- Top nav links collapse to hamburger menu below 744px
- Secondary category strip collapses to a horizontal scrollable strip below 744px
- Product card grid reduces columns: 4 → 3 → 2 → 1
- Footer columns collapse to single column below 744px
- Search bar becomes a full-screen overlay on mobile, triggered by a search icon
- Cart icon remains visible at all breakpoints, but cart preview panel becomes full-screen on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is heavily weighted toward generic web blues, grays, and checkout-widget colors (Shopify Pay, Klarna, Afterpay). The distinctive cyan (#008aa4) and green (#00c248) are the most brand-specific signals; the true primary may be a different shade of cyan or teal not captured in the top 30 hexes.
- Font sizes and line heights are inferred from common gaming store patterns and the extracted font stack; exact values may differ from the live site's CSS.
- Hover and active states for buttons and links are based on common darkening patterns (10-15% darker); the actual brand may use different transition values.
- Error styling (form validation, error messages) could not be extracted; assumed to follow standard red (#cc4b37) patterns.
- Dark mode is not detected; the site appears to use a light canvas with dark ink as default.
- The "Ubisoft Sans Bold" font may be a separate weight file; exact font-weight mapping for the variable font is unknown.
- Sub-brand palettes (for specific game franchises like Assassin's Creed, Far Cry, Rainbow Six) are not captured; each franchise likely has its own accent color.
- Animation durations and easing curves (button transitions, card hover effects, nav dropdowns) are not extracted.
- The search bar's focus ring width and color are assumed; actual implementation may use a different blue or a box-shadow approach.
- Cart icon badge count (number of items) styling is not captured; assumed to use a red (#cc4b37) circle with white text.
