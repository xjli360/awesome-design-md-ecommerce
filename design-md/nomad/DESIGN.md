---
version: alpha
name: "Nomad"
source_url: "https://nomadgoods.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A monochromatic landscape of #0e0e0e and #2f2f2f punctuated by a single electric accent of #0048ff — Nomad’s design language reads like a precision instrument manual translated into digital commerce. The brand’s visual system is built on extreme contrast: near-black ink on near-white canvas (#f3f3f3), with every surface, card, and button carrying the same tight {rounded.sm} radius that echoes the chamfered edges of a machined aluminum phone case. Typography runs Gotham at 700 weight for display and 400 for body, a choice that signals industrial durability without the coldness of a true sans-serif like Helvetica. The navigation bar sits at 80px with a hairline bottom border (#dedede) that’s barely there — the brand trusts its product photography to carry the emotional weight. Product cards use a subtle shadow and {rounded.md} corners, while the primary CTA (#0048ff) sits on white text with a hover state that deepens to #005bd3. The checkout flow introduces a secondary accent (#e3163b) for error states and a warm gold (#efcf07) for limited-edition badges. There is no gradient, no glassmorphism, no decorative flourish — every pixel is either structural (gray, black, white) or functional (blue CTA, red error, gold badge). The footer collapses to a single column on mobile, and the search bar expands to full width below 744px. This is a brand that sells $50 leather cable ties and $300 titanium watch bands; the design system treats every product as a hero, every button as a tool, and every interaction as a transaction of trust.

colors:
  primary: "#0048ff"
  primary-active: "#005bd3"
  primary-disabled: "#96b4ff"
  ink: "#0e0e0e"
  body: "#2f2f2f"
  muted: "#676767"
  muted-soft: "#b2b2b2"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#f3f3f3"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  error: "#e3163b"
  gold-badge: "#efcf07"
  orange-accent: "#ff5a00"
  green-accent: "#00ff54"
  green-soft: "#d6fa9e"
  navy: "#153661"
  slate: "#4c6282"
  sage: "#4d5245"
  sage-soft: "#949e94"
  taupe: "#837e74"
  taupe-soft: "#cecdc0"
  steel: "#688292"
  steel-soft: "#c7c8ca"
  dark-surface: "#1a1a1a"

typography:
  display-xl:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-bold:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  price:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0

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
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
  nav-bar-desktop:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
  nav-bar-mobile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  search-bar-expanded:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.sm} 0 {spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    padding: "0 {spacing.sm} {spacing.sm} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.gold-badge}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    height: 480px
  hero-banner-image:
    rounded: "{rounded.none}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.caption-bold}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.gold-badge}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  collection-grid:
    gap: "{spacing.base}"
  collection-item:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
  accordion-content:
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.lg} {spacing.base}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
  color-swatch-selected:
    rounded: "{rounded.full}"
    height: 32px
  star-rating:
    color: "{colors.gold-badge}"
    size: 16px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.body}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the entire site, used for "Add to Cart," "Checkout," and "Shop Now" actions. Rendered in the brand’s signature #0048ff with white text and a tight {rounded.sm} radius that echoes the chamfered edges of Nomad’s physical products. On hover, the background shifts to #005bd3 with no scale or shadow animation — just a clean color swap. The disabled state uses #96b4ff, maintaining the same typography and padding but removing pointer events.

**`button-secondary`** — Used for "Learn More," "View Details," and secondary checkout actions. Rendered as an outlined button with a 1px #dedede border on the {colors.canvas} background, with {colors.ink} text. On hover, the border thickens to 2px and the background fills with {colors.surface-soft}. The text-only variant (`button-tertiary-text`) uses {colors.primary} text with no background or border, reserved for inline actions within product cards and accordion panels.

**`button-pill`** — A compact, fully rounded variant used for filter tags, category chips, and mobile navigation CTAs. Uses {colors.primary} background with white text, {typography.button-sm} sizing, and {rounded.full} corners. Active state inverts to an outlined pill with {colors.primary} text on a transparent background.

### Cards
**`product-card`** — The core product display unit, used in collection grids, search results, and related-product carousels. A white surface with {rounded.md} corners and a subtle box-shadow (0 1px 3px rgba(0,0,0,0.08)). The image area occupies the top 60% of the card with its own {rounded.md} radius, while the title and price sit below with {spacing.sm} padding on all sides. Badges (New, Sale, Limited, Sold Out) overlay the top-left corner of the image with {rounded.xs} corners and {typography.badge} sizing.

**`hero-banner`** — Full-width promotional banner used on the homepage and collection landing pages. The background is {colors.canvas} with the hero image bleeding edge-to-edge. The text overlay uses {typography.display-xl} in {colors.ink} with a single CTA button beneath. On mobile, the height collapses to 320px and the text stack moves below the image.

### Navigation
**`top-nav`** — Fixed-position navigation bar at 80px height on desktop, 64px on mobile. The background is {colors.canvas} with a 1px bottom border in {colors.hairline}. The brand logo sits left-aligned, with nav links in {typography.nav-link} (13px, 700 weight, 1px letter spacing, uppercase) centered. The right side contains a search icon, account icon, and cart icon — all rendered as {icon-button} with 40px touch targets. On scroll, the nav gains a subtle box-shadow (0 2px 8px rgba(0,0,0,0.06)).

**`search-bar`** — Inline search input with a {rounded.sm} radius and {colors.surface-soft} background. On focus, it expands to full width with a white background and a 2px {colors.primary} border. The expanded state (`search-bar-expanded`) uses {typography.body-md} for the input text and includes a clear button on the right.

### Forms
**`text-input`** — Standard form input for checkout, account creation, and newsletter signup. A white background with a 1px {colors.hairline} border and {rounded.sm} corners. On focus, the border shifts to {colors.primary} at 2px. The error state (`text-input-error`) uses a 2px {colors.error} border with an error icon and message below.

**`quantity-selector`** — A compact input group for adjusting cart quantities. Rendered as a horizontal row with a minus button, the quantity value, and a plus button — all within a 44px tall container with {rounded.sm} corners. The value is centered in {typography.body-md} with {colors.ink} text, while the buttons use {colors.muted} icons.

### Footer
**`footer`** — Full-width footer with a {colors.ink} background and white text. Organized into four columns on desktop: Shop, Support, Company, and Connect. Each column has a {typography.caption-bold} heading with {typography.link} links below in {colors.muted-soft}. The bottom bar contains copyright text, payment icons, and social links. On tablet, the columns collapse to two; on mobile, they collapse to a single-column accordion.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to 64px with hamburger menu; product grid goes to 1 column; hero banner height reduces to 320px; footer accordion; search bar expands to full width; buttons go full-width |
| Tablet | 744–1128px | Nav bar remains at 80px with condensed links; product grid at 2 columns; footer at 2 columns; hero banner at 400px |
| Desktop | 1128–1440px | Full nav with all links; product grid at 3–4 columns; footer at 4 columns; hero banner at 480px |
| Wide | > 1440px | Max-width container at 1440px; product grid at 4 columns; hero banner at 520px |

### Touch Targets
- All interactive elements (buttons, links, icons) maintain a minimum 44px height and 44px width for mobile touch targets
- Icon buttons in the nav bar are 40px with 24px icons and 12px padding
- Product card CTAs are 48px tall with 14px vertical padding
- Quantity selector buttons are 44px tall with 32px width
- Color swatches are 32px diameter with 4px padding between swatches

### Collapsing Strategy
- Top nav collapses from horizontal links to hamburger menu at 744px
- Product grid collapses from 4 columns → 2 columns → 1 column
- Footer collapses from 4 columns → 2 columns → single-column accordion
- Hero banner text overlay moves from side-by-side to stacked below image on mobile
- Search bar collapses from inline to full-width overlay on mobile
- Collection filters collapse from sidebar to horizontal scroll strip on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted from the live site — the primary button hover (#005bd3) is inferred from the extracted hex list, but secondary and tertiary hover states are estimated based on common patterns
- Error state styling for forms (borders, icons, messages) is inferred from the extracted error red (#e3163b) but the exact implementation (icon style, message placement, animation) is unknown
- Dark mode styling is not present on the live site — all extracted colors are from the light theme
- The extracted font list includes "Aleo" and "Inconsolata" which may be used in specific contexts (blog, code snippets) but the primary brand font is Gotham based on frequency and brand recognition
- The extracted color list is heavily weighted toward grays and blues — the brand's true accent palette (gold, orange, green, sage, taupe, steel) is inferred from the less frequent hex values and may represent seasonal collections or limited-edition products rather than core brand colors
- Animation and transition timing values (hover transitions, scroll effects, loading states) are not extracted and use standard 200-300ms ease-in-out defaults
- The checkout flow (Shopify-powered) uses platform-default styling for payment buttons, address forms, and order summaries — these are not part of the brand's custom design system
- Sub-brand or collection-specific palettes (e.g., "Horween Leather" vs. "Sport Band") could not be distinguished from the global extracted colors
- The extracted hex list includes several colors (#bbbbbb, #d6d6d6, #ebebeb) that are likely framework defaults from Shopify's UI components rather than intentional brand choices — these are noted but included for completeness
