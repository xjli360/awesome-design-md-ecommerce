---
version: alpha
name: "Ideal of Sweden"
source_url: "https://www.idealofsweden.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A phone-case brand that uses a near-monochrome scaffold of #202020 and #111111 to frame a riot of product color — #8d1919, #ffc0ca, #e5bac1, #910048, #ed2939, #ac7d78, #ea9686, #ffff00, #bc002d, #00247d, #dd0300, #fae042, #c60c30, #ffce00, #ffc400, #c60b1e, #164194, #ffec00, #002395, #38485d, #9daf3f, #df2507 — a palette that reads less like a brand system and more like a global flag collection exploded across silicone and polycarbonate. The canvas is #f9f9f9, a warm near-white that softens the high-contrast product photography, while #e9e9e9 provides hairline separators and card borders. The brand's own typographic voice runs on Aspekta and owners — the latter appearing in three distinct cuts (owners, owners-wide, owners-xwide) with `!important` declarations that suggest a hard-won battle for brand typography against Shopify's default stack. Buttons use {rounded.sm} corners, while product imagery and hero sections lean into {rounded.lg} to {rounded.xl} radii that echo the curved edges of the cases themselves. The site reads as a gallery first, store second: generous whitespace, a persistent top nav with a centered logo, and product cards that let the case color do all the emotional work.

colors:
  primary: "#202020"
  primary-active: "#111111"
  primary-disabled: "#4c4c4c"
  ink: "#202020"
  body: "#4c4c4c"
  muted: "#9a9a9a"
  muted-soft: "#b3b3b3"
  hairline: "#e9e9e9"
  hairline-soft: "#f0f0f0"
  canvas: "#f9f9f9"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#8d1919"
  accent-pink: "#ffc0ca"
  accent-rose: "#e5bac1"
  accent-burgundy: "#910048"
  accent-crimson: "#ed2939"
  accent-terracotta: "#ac7d78"
  accent-coral: "#ea9686"
  accent-yellow: "#ffff00"
  accent-gold: "#ffc400"
  accent-blue: "#00247d"
  accent-navy: "#164194"
  accent-flag-red: "#bc002d"
  accent-flag-white: "#ffffff"
  accent-flag-blue: "#002395"
  accent-olive: "#9daf3f"
  accent-orange: "#df2507"
  accent-sweden-blue: "#004b87"
  accent-sweden-yellow: "#ffce00"

typography:
  display-xl:
    fontFamily: "'owners-xwide', 'Aspekta', 'Avenir Next', 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'owners-wide', 'Aspekta', 'Avenir Next', 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'owners', 'Aspekta', 'Avenir Next', 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'owners', 'Aspekta', 'Avenir Next', 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'owners', 'Aspekta', 'Avenir Next', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Aspekta', 'Avenir Next', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Aspekta', 'Avenir Next', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Aspekta', 'Avenir Next', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'owners', 'Aspekta', 'Avenir Next', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'owners', 'Aspekta', 'Avenir Next', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Aspekta', 'Avenir Next', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'owners', 'Aspekta', 'Avenir Next', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'owners', 'Aspekta', 'Avenir Next', 'Helvetica Neue', sans-serif"
    fontSize: 10px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-accent:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-active:
    backgroundColor: "#6b1313"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.md} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid transparent"
  color-swatch-selected:
    border: "2px solid {colors.primary}"
  color-swatch-variant:
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  cart-icon:
    height: 24px
    width: 24px
    textColor: "{colors.ink}"
  cart-count:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
    padding: "0 4px"

## Components

### Buttons
**`button-primary`** — The dominant call-to-action, rendered in {colors.primary} (#202020) with white text and {rounded.sm} corners. On hover, the background deepens to {colors.primary-active} (#111111). The disabled state uses {colors.primary-disabled} (#4c4c4c) to signal inactivity without losing brand consistency. Text is set in {typography.button-md}, uppercase with tight tracking, giving the button a confident, editorial weight.

**`button-secondary`** — An outlined alternative for less assertive actions, using a white background with {colors.ink} text and a 1px {colors.hairline} border. Active state fills to {colors.hairline} (#e9e9e9). Used for "Add to Wishlist," "View Details," and secondary checkout flows.

**`button-accent`** — A high-visibility variant using {colors.accent-red} (#8d1919) for sale triggers, limited-edition drops, and clearance sections. The active state darkens to #6b1313. This button carries the same {rounded.sm} and uppercase typography as `button-primary` but signals urgency through color.

**`button-pill`** — A compact, fully rounded variant for filter tags, category toggles, and quick-add actions. Uses {colors.primary} background with {typography.button-sm} for tighter spacing. The pill outline variant inverts to a transparent background with a {colors.hairline} border for secondary filter states.

### Cards
**`product-card`** — The core product display unit, a white card with {rounded.lg} corners and no internal padding at the container level. The product image fills the top with matching {rounded.lg} top corners and a 1:1 aspect ratio. Below, the title uses {typography.title-md} and the price uses {typography.body-md} in {colors.body}. Badges overlay the image at top-left with absolute positioning.

**`product-card-badge`** — A small, absolute-positioned label that overlays product images. Uses {colors.accent-red} background with white uppercase text in {typography.badge}. Three badge variants exist: `badge-sale` (red), `badge-new` (yellow), and `badge-limited` (pink), each carrying the same structural tokens but distinct brand colors.

### Navigation
**`nav-bar`** — A fixed 72px bar with white background and a 1px {colors.hairline} bottom border. Navigation links use {typography.nav-link} — uppercase, 13px, weight 600 — with active state underlined by a 2px {colors.primary} border. On scroll, the bar gains a subtle box-shadow and remains sticky. The logo sits centered, flanked by nav items on the left and utility icons (search, cart) on the right.

**`nav-link-active`** — The active navigation state, distinguished by {colors.primary} text color and a 2px bottom border in the same shade. Inactive links fade to {colors.muted} (#9a9a9a).

### Forms
**`text-input`** — Standard text entry with {colors.canvas} background, 1px {colors.hairline} border, and {rounded.sm} corners. On focus, the border switches to {colors.primary} (#202020). Error state uses {colors.accent-red} (#8d1919) border. Height is 48px with 12px/16px padding for comfortable touch targets.

**`select-input`** — Dropdown selectors share the same structural tokens as text inputs: 48px height, {rounded.sm}, 1px {colors.hairline} border, and {typography.body-md} text.

### Search
**`search-bar`** — A pill-shaped search field with {rounded.full} corners, white background, and a 1px {colors.hairline} border. On focus, the border shifts to {colors.primary}. Height is 44px with 10px/20px padding, designed to sit comfortably in the nav bar or as a standalone hero element.

### Footer
**`footer-section`** — A dark footer using {colors.primary} (#202020) background with white text at 80% opacity for links. Links use {typography.link} and increase to full opacity on hover. Padding is generous at {spacing.xxl} (48px) vertical and {spacing.lg} (24px) horizontal.

### Color Swatches
**`color-swatch`** — Circular swatches at 32px diameter with {rounded.full} corners. The selected state adds a 2px {colors.primary} border. A smaller variant (`color-swatch-variant`) at 24px is used for inline product variant selectors.

### Badges
**`badge-sale`**, **`badge-new`**, **`badge-limited`** — Three badge variants sharing the same structural tokens ({typography.badge}, {rounded.xs}, 2px/8px padding) but differentiated by background color: red for sale, yellow for new, pink for limited edition. Each carries the brand's uppercase, tight-tracking typographic voice.

### Cart
**`cart-icon`** — A 24px icon in {colors.ink}. The `cart-count` badge overlays the icon with a {colors.accent-red} background, white text, and {rounded.full} shape. Minimum width of 18px ensures single-digit counts display as circles while double-digit counts expand to a pill.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 column), nav collapses to hamburger menu, hero text reduces to {typography.display-md}, search bar moves to full-width below nav, footer stacks vertically, product cards use full-width images |
| Tablet | 744–1128px | Two-column product grid, nav items reduce to icons + labels, hero uses {typography.display-lg}, search bar remains in nav but shrinks width, footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid, full nav with text labels, hero uses {typography.display-xl}, search bar at full width in nav, footer uses 4-column layout |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero content centered with max-width 1200px, nav remains full-width with increased padding |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Color swatches at 32px diameter exceed the 44px touch target guideline; consider increasing to 44px on mobile or adding 6px invisible padding
- Search bar at 44px height meets touch target minimum
- Nav links have 72px bar height providing adequate tap area even with small text
- Product card tap targets include the entire card surface, not just text

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px, with a slide-out drawer revealing all nav items
- Product filters collapse to a "Filter" button that opens a modal on mobile
- Footer link columns collapse from 4 columns on wide to 2 columns on tablet to a single stacked column on mobile
- Hero section reduces font size and padding on mobile, with CTA button becoming full-width
- Product image galleries collapse from thumbnail strip to swipeable dots on mobile
- Search bar transitions from inline nav element to full-width below the nav on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list contains 30+ colors, many of which are likely flag colors from product photography (Swedish, French, British, Italian, German, etc.) rather than brand system colors. The true brand palette is probably more restrained — the extracted data should be treated as a superset that includes product variant colors, not just UI tokens.
- Font stack includes `owners`, `owners-wide`, `owners-xwide`, and `Aspekta` — the exact usage hierarchy (which weights for headings vs. body) could not be determined from extracted CSS alone. The `!important` flag on `owners` suggests it may be injected by a third-party tool or overridden in specific contexts.
- No extracted hover states, focus rings, or active states beyond what was inferred from color relationships.
- Error styling for forms (error messages, validation icons) not extracted.
- Dark mode preferences or alternate themes not detected.
- Animation durations, easing curves, and transition properties not extracted.
- Dropdown menus, mega-menus, and sub-navigation patterns not observed.
- Modal/dialog overlay styling (scrim opacity, close button placement) not extracted.
- Checkout flow styling likely uses Shopify's default checkout (platform-shopify: False suggests custom storefront, but checkout may still be Shopify-hosted).
- Social media icon colors (Instagram, TikTok, etc.) may be inflating the extracted color palette — the presence of #b3d4fc (likely a link blue) and multiple near-identical reds suggests framework defaults or social brand colors that weren't fully filtered.
