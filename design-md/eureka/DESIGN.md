---
version: alpha
name: "Eureka"
source_url: "https://www.eureka.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Amethyst where most floor-care brands reach for navy or safety red — Eureka stakes its entire CTA system on a saturated #70377c, a hue more at home in cosmetics packaging than in the chrome-and-beige world of vacuum design. That choice radiates outward: a muted sibling #ae81ac absorbs disabled states and soft hover fills, while #7037cc, a cooler violet, surfaces in accent contexts and feature call-outs, giving the palette tonal range uncommon in the appliance category. The near-white canvas sits at #fafafa rather than pure white, cutting glare on long product-browsing sessions; three further off-whites (#f6f6f6, #f5f5f5, #efefef) build a depth system — page canvas, section fill, card surface, inset — all distinguishable without heavy shadow lifting. Type runs primarily in Gotham, a geometric grotesque whose mechanical precision aligns with product photography of motors, cyclone chambers, and HEPA filtration stacks; Sk-Modernist and Modernist Bold carry display headings with more editorial authority at larger sizes. Buttons sit at {rounded.sm} (8px) — confident and utilitarian without harshness. Product cards step to {rounded.md} (12px) to soften the grid, while site-wide promo banners break to {rounded.none} for full-bleed authority. Dark text anchors on #1d1d1f, an Apple-ecosystem near-black that pairs cleanly with Gotham's neutrality; body copy steps back to #434343 and secondary labels fade to #949494. Hairlines at #dedede and fills at #f6f6f6 form the quiet three-layer depth: the whole system reads less like a home-appliance catalog and more like a consumer-electronics storefront — tightly spaced product grid, photography-led hierarchy, purple-on-near-white primary actions that make the brand's anchor hue feel deliberate rather than inherited.

colors:
  primary: "#70377c"
  primary-active: "#693a78"
  primary-disabled: "#ae81ac"
  accent-violet: "#7037cc"
  muted-purple: "#ae81ac"
  ink: "#1d1d1f"
  body: "#434343"
  muted: "#949494"
  muted-light: "#b0b0b0"
  hairline: "#dedede"
  hairline-soft: "#e5e5e6"
  canvas: "#fafafa"
  surface-soft: "#f6f6f6"
  surface-card: "#f5f5f5"
  surface-subtle: "#efefef"
  error: "#ff0000"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#121212"
  footer-bg: "#1f1f1f"

typography:
  display-xl:
    fontFamily: "'Sk-Modernist', 'Modernist Bold', Gotham, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Sk-Modernist', 'Modernist Bold', Gotham, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Sk-Modernist', Gotham, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Gotham, 'Sk-Modernist', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Gotham, 'Sk-Modernist', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Gotham, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Gotham, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Gotham, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Gotham, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Sk-Modernist', Gotham, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  button-md:
    fontFamily: "Gotham, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Gotham, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  nav-label:
    fontFamily: "Gotham, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  spec-label:
    fontFamily: "Gotham, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.primary}"
    errorBorder: "1px solid {colors.error}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "10px 20px"
    height: 44px
    iconColor: "{colors.muted}"
    focusBorder: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
    activeLink: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    imageAspectRatio: "1:1"
    imageBackground: "{colors.surface-soft}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    subtextTypography: "{typography.body-sm}"
    subtextColor: "{colors.muted}"
    badgePosition: top-left
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.section} 0"
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  product-badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  product-badge-bestseller:
    backgroundColor: "{colors.accent-violet}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "10px {spacing.base}"
    textAlign: center
  category-filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 18px"
    border: "1px solid {colors.hairline}"
  category-filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 18px"
    border: "none"
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    alternateBackground: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    padding: "12px {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  rating-stars:
    starColor: "{colors.primary}"
    emptyStarColor: "{colors.hairline}"
    countTypography: "{typography.caption}"
    countColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-light}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Eureka's primary button carries the brand's #70377c on white label text in Gotham 600 at 16px, standing 48px tall with {rounded.sm} corners and 28px horizontal padding. The active state deepens to #693a78 with no scale or shadow change; disabled swaps the fill to the muted #ae81ac, keeping the disabled state within the purple family rather than dropping to a generic gray. Used for all primary commerce actions: "Add to Cart," "Shop Now," and "Buy It Now."

**`button-secondary`** — An outlined variant on the canvas fill (#fafafa) with a 2px #70377c border and matching purple label text. On interaction the background shifts to {colors.surface-soft} and the border deepens to {colors.primary-active}, maintaining clear visual subordination to the primary without disappearing. Used for "Compare," "View Details," and secondary CTAs on product pages.

**`button-ghost`** — Transparent background, {colors.body} (#434343) label in Gotham 600/14px, {rounded.sm} for consistent focus ring behavior. Reserved for tertiary actions — "Learn More," "See All Reviews," inline navigation links — where adding a filled or outlined button would crowd the layout.

### Text Input

**`text-input`** — 48px tall, {rounded.sm}, 1px #dedede border that sharpens to 1px #70377c on focus. Placeholder text renders in {colors.muted} (#949494); an error state swaps the border to {colors.error} (#ff0000) with an inline validation message in the same red. Background stays on {colors.canvas} (#fafafa) to sit flush with page surface without visually sinking into section fills.

### Navigation

**`nav-bar`** — 64px tall, anchored at the top of the viewport, {colors.canvas} fill with a 1px #dedede bottom hairline separating it from page content. The Eureka logomark or wordmark renders in {colors.primary}. Navigation links use {typography.nav-label} (Gotham 500/14px) in {colors.ink}; the active section shifts its label to {colors.primary}. A search icon and cart icon-button sit at far right. On mobile, the full link set collapses behind a hamburger with a full-screen drawer overlay on {colors.scrim} (#121212) at 90% opacity.

### Product Card

**`product-card`** — The primary commerce unit. A #f5f5f5 surface card with a 1px #e5e5e6 border at {rounded.md} contains a square 1:1 image region on {colors.surface-soft} (#f6f6f6), followed by the product name in {typography.title-sm} (Gotham 600/16px), price in {typography.price-display} (Sk-Modernist 700/22px), and a model descriptor line in {typography.body-sm} at {colors.muted}. Star ratings in {colors.primary} sit between the name and price. Badges pin to the top-left of the image area with {rounded.xs} corners and 3px top/left offset. The full card is a tappable link target on mobile.

### Badges

**`product-badge-new`** — #70377c fill, white Gotham 700 at 11px ALL CAPS, {rounded.xs}. Signals the latest-generation SKUs in the lineup.

**`product-badge-sale`** — #ff0000 fill, otherwise identical geometry to badge-new. Reserved for price-reduced items; the red reads as urgent against the purple-dominant palette without requiring an entirely new color family.

**`product-badge-bestseller`** — #7037cc (accent violet) fill. The cooler violet distinguishes best-seller status from new/sale while staying within the purple-to-violet frequency of the overall brand palette. All three badge colors remain typologically purple, making the grid feel consistent even when multiple badge types coexist.

### Promo Banner

**`promo-banner`** — Full-width #70377c bar rendered above the nav or between page sections, hard {rounded.none} edges both ends. White Gotham 400/14px text centered. Used for site-wide messaging: "Free shipping on orders over $X," "New model: Eureka Robot J-Series," limited-time discount countdowns. The zero-radius edges signal systemic messaging rather than a content card, and the primary fill ties it to the CTA color system rather than introducing a separate promotional palette.

### Search

**`search-bar`** — Pill-shaped at {rounded.full}, #f6f6f6 fill, 1px #dedede border, 44px tall — slightly shorter than input fields to fit within the 64px nav row without touching its hairline. The search icon renders in {colors.muted}; as the user types, the border activates to 1px #70377c. On mobile, the icon collapses the bar into a search overlay occupying the full nav height.

### Category Filter Chips

**`category-filter-chip`** and **`category-filter-chip-active`** — Chip row above the product grid filters by category (Robot, Stick, Upright, Cordless) and feature (Pet, HEPA, Wi-Fi). Default state: canvas fill, 1px #dedede border, #434343 Gotham 600/14px label. Active state flips to full {colors.primary} fill with white label — the same purple as the primary button, so the filter interaction feels like a committed action rather than a passive toggle. Rendered as a horizontally scrollable single row on mobile.

### Spec Table

**`spec-table-row`** — Alternating canvas (#fafafa) and surface-soft (#f6f6f6) rows. Label column (suction power, bin capacity, noise level, filter type, battery life) renders in {typography.spec-label} (Gotham 700/11px uppercase, {colors.muted}); value column in {typography.body-sm} ({colors.body}). A 1px #e5e5e6 bottom border divides rows. On mobile, the two-column layout collapses to stacked label-above-value blocks with the same alternating row pattern.

### Rating Stars

**`rating-stars`** — Five stars in {colors.primary} (#70377c) for filled, #dedede for empty. Review count appears inline in {typography.caption} (Gotham 400/12px) at {colors.muted}. Using the brand's primary purple rather than conventional amber keeps the rating system coherent with the CTA color and avoids importing an unrelated warm tone into an otherwise cool-neutral palette.

### Footer

**`footer`** — #1f1f1f full-width dark background. Section headings in {typography.title-sm} (Gotham 600/16px) in white; links in Gotham 400/14px at #b0b0b0 ({colors.muted-light}), lightening to white on hover. Legal text, social icons, and copyright line sit at the very bottom in {colors.muted}. The dark footer creates clear end-of-page termination against the otherwise near-white canvas and positions the Eureka logo and category navigation in a format that reads across robot, stick, and upright product families without favoring any single line.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to logo + hamburger + cart icon; hero headline drops from display-xl (48px) to display-md (32px); product grid is 2-column; filter chips scroll horizontally; spec table collapses to stacked pairs; promo banner truncates to one line |
| Tablet | 744–1128px | Nav shows top-level category links without mega-menu; product grid is 3-column; hero uses side-by-side image/copy split at 50/50; filter chips wrap to 2 rows if needed |
| Desktop | 1128–1440px | Full nav with mega-menu dropdown panels; product grid is 4-column; hero at full display-xl with image on right 55%; promo banner at full phrase |
| Wide | > 1440px | Content max-width 1440px centered; gutters expand proportionally; hero image scales to fill; no additional structural changes |

### Touch Targets

- All buttons and filter chips minimum 44px tall
- Nav icon buttons (search, cart, hamburger) carry invisible padding to reach 44×44px hit area
- Full product card is a single tappable link target on mobile
- Filter chips have 8px gap between chips; minimum 36px tall on mobile
- Star rating tap target expanded to 32px height with invisible padding above/below

### Collapsing Strategy

- Nav mega-menu collapses to full-screen drawer on hamburger tap, with accordion-style category expansion
- Horizontal filter chip row becomes a scroll carousel on mobile with no wrapping
- Hero two-column layout stacks vertically on mobile: product-focused heroes lead with image, brand-statement heroes lead with headline
- Spec table collapses from two-column to stacked label-above-value pairs below 744px, retaining alternating row shading
- Footer four-column link grid collapses to single-column accordion on mobile, headings as expand/collapse triggers

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Pure white (#ffffff) is absent from the extracted palette; product card surfaces use #f5f5f5 but the actual card background may be white — verify against live Shopify theme
- Modal, quick-view overlay, and cart-drawer border-radius and scrim behavior not captured; values inferred from card/button conventions
- `swiper-icons` in the font stack is Swiper.js's internal glyph font, not a brand icon system — actual product UI icons (cart, search, hamburger, star) are unidentified
- #007aff in the extracted palette is the iOS system blue, almost certainly a Shopify or browser default for unvisited links rather than an intentional Eureka brand color; excluded from the token system
- Mega-menu layout, hover colors, and flyout structure not confirmed
- Animation timing and easing curves not extractable from static snapshot; 150–200ms ease assumed throughout
- Gotham licensing for web self-hosting is not confirmed; Sk-Modernist is an open geometric grotesque that may serve as fallback if Gotham is unavailable
- Dark-mode palette absent; site appears light-mode only but no explicit `prefers-color-scheme` evidence was captured
