---
version: alpha
name: "Fy!"
source_url: "https://www.iamfy.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The checkout button is mint — not seafoam or sage, but a saturated screen-glow mint (#00e6aa) that reads from across a room, the clearest signal that Fy! is an art-discovery platform first and a retail shop second. That primary CTA color sits against near-black (#121212) in charged moments and retreats to white everywhere else, creating a binary contrast rather than the layered neutral ramps most poster shops reach for. Playfair Display carries every editorial moment — collection headlines, artist names, feature callouts — at weights that reference broadsheet culture without settling into pastiche. Geist, the clean geometric sans designed for developer tooling, handles the platform layer: nav links, price tags, filter chips, add-to-cart labels. The pairing is purposefully discordant — one typeface traces 18th-century punch-cutting traditions; the other emerged from a 2023 GitHub design system. Between them they articulate Fy!'s core pitch: independent artists, algorithmically surfaced, delivered as product.
  Accent colors behave as semantic signals rather than decoration. Alert red (#eb0004) marks sale states and error messages; amber (#ffb500) marks featured or curated picks, adding warmth only where editorial emphasis demands it. The ambient palette stays cool and nearly monochrome — mid gray (#dedede) for hairlines, light gray (#c8c8c8) for disabled states and image placeholders. Product cards sit on a white surface with only a soft gray border at {rounded.sm}, keeping visual weight on the artwork rather than the container. The global search bar extends pill-shaped to {rounded.full}, signaling discovery mode; primary action buttons use {rounded.md} to feel purposeful without severity. Spacing is generous inside product pages — large image crops, breathing room between the frame selector and the buy button — then tightens to a dense grid on collection pages where three or four columns of prints compete for attention. Geist Mono appears on price displays and format labels, adding a specification-like precision that reinforces the idea that choosing a frame size is a considered decision rather than an impulse.

colors:
  primary: "#00e6aa"
  primary-active: "#00cc94"
  primary-disabled: "#99f5de"
  accent-red: "#eb0004"
  accent-amber: "#ffb500"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  hairline: "#dedede"
  border-mid: "#c8c8c8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#121212"
  on-dark: "#ffffff"
  scrim: "rgba(18,18,18,0.5)"

typography:
  display-xl:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Geist', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'Geist', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'Geist', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Geist', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Geist', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  price-display:
    fontFamily: "'Geist Mono', 'Courier New', monospace"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  label-mono:
    fontFamily: "'Geist Mono', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.05em
    textTransform: uppercase
  artist-name:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Geist', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-sm:
    fontFamily: "'Geist', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  nav-link:
    fontFamily: "'Geist', -apple-system, BlinkMacSystemFont, sans-serif"
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
    rounded: "{rounded.md}"
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.border-mid}"
    padding: 13px 23px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.md}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorderColor: "{colors.primary}"
    placeholderColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 12px 20px
    height: 48px
    focusBorderColor: "{colors.primary}"
    searchIconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    iconColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageRadius: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.border-mid}"
    padding: "{spacing.sm}"
    gap: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    artistTypography: "{typography.artist-name}"
    priceTypography: "{typography.price-display}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRadius: "{rounded.md}"
    padding: "{spacing.section} {spacing.xl}"
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-mono}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  featured-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.label-mono}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  artist-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 4px 12px
  size-selector:
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackground: "{colors.canvas}"
    inactiveTextColor: "{colors.ink}"
    typography: "{typography.label-mono}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    activeBorderColor: "{colors.primary}"
    padding: 8px 16px
    height: 40px
  frame-selector:
    activeBackground: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    inactiveBackground: "{colors.canvas}"
    inactiveTextColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 16px
    height: 44px
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    activeBackground: "{colors.ink}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    borderLeft: "1px solid {colors.hairline}"
    overlayBackground: "{colors.scrim}"
    titleTypography: "{typography.title-md}"
    itemTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    checkoutButtonBackground: "{colors.primary}"
    checkoutButtonTextColor: "{colors.on-primary}"
    checkoutButtonRadius: "{rounded.md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.canvas}"
    accentColor: "{colors.primary}"
    borderTop: "1px solid rgba(255,255,255,0.1)"

## Components

### Buttons

**`button-primary`** — The main purchase CTA fills with the brand's signature mint (#00e6aa) and uses near-black {colors.on-primary} text for contrast — never white, since mint is luminous enough to fail with white copy. Corner radius is {rounded.md} (12px), height 48px, type in Geist {typography.button-md}. Active state deepens to #00cc94; disabled washes out to #99f5de with `cursor: not-allowed`.

**`button-secondary`** — White background with a 1px {colors.hairline} border and {colors.ink} text. Same 48px height and {rounded.md} radius as primary, creating a consistent CTA pairing for "Save to wishlist" or alternative framing choices. Border shifts to {colors.border-mid} on hover.

**`button-ghost`** — Transparent background with ink text in {typography.button-sm}. Used for low-priority inline actions like "View artist" or "See all." No border, no fill — relies on context for affordance.

### Search Bar

**`search-bar`** — Pill-shaped at {rounded.full}, the search field sits on a {colors.surface-soft} ground to lift it visually from the white canvas. The border animates to {colors.primary} mint on focus, the one moment the brand's primary color appears in a form element rather than a button. Deployed prominently in the nav and in a hero slot on the homepage.

### Product Card

**`product-card`** — A minimal white card with a 1px {colors.hairline} border and {rounded.sm} clipping on the artwork image. Hover shifts the border to {colors.border-mid} without elevation or drop-shadow, keeping attention on the image. Artist attribution renders in italic Playfair Display ({typography.artist-name}) beneath the work title; price appears in Geist Mono ({typography.price-display}) to suggest specification precision rather than retail softness.

### Badges

**`sale-badge`** — Alert red (#eb0004) rectangular badge in {typography.label-mono} — uppercase Geist Mono at 11px — overlaid on the image corner. {rounded.xs} corners keep it sharp rather than playful.

**`featured-badge`** — Amber (#ffb500) counterpart to sale-badge, used for "Featured" or "Editor's pick" labels. Ink text instead of white for contrast against the warm ground. Same {rounded.xs} structure.

### Size Selector

**`size-selector`** — A horizontal strip of format pills (A4, A3, 50×70 cm, 70×100 cm, etc.) below the product image. The active pill fills with {colors.primary} mint with {colors.on-primary} ink text; inactive pills are white with a hairline border. Type is {typography.label-mono} uppercase Geist Mono, reinforcing the spec-like register. Scrolls horizontally on mobile rather than wrapping.

### Frame Selector

**`frame-selector`** — Larger tap targets than size-selector with descriptive text labels (Natural Oak, Black, White, No Frame). Active state uses near-black {colors.ink} fill with {colors.on-dark} white text — deliberately differentiated from the mint used in size selection to signal a separate decision dimension. {rounded.sm} corners, 44px height.

### Artist Chip

**`artist-chip`** — Rounded pill in {colors.surface-soft} with a hairline border and {typography.caption} Geist text. Used in collection filter bars and "More from this artist" rows on the product detail page. Tapping navigates to the artist's collection.

### Category Chip (Filter Bar)

**`category-chip`** — Horizontally scrolling filter strip above collection grids. Default: {colors.surface-soft} background, {colors.muted} text. Active: {colors.ink} fill, {colors.on-dark} white text signaling a locked filter. {rounded.full} pill shape, {typography.caption} type. No wrapping — the strip scrolls.

### Hero Banner

**`hero-banner`** — Full-bleed dark {colors.ink} background banner. Headline in {typography.display-xl} Playfair Display at on-dark white. Subhead in {typography.body-md} Geist. CTA button carries mint fill and {rounded.md} radius — the primary color's first appearance in the scroll. Padding is generous ({spacing.section} vertical) to let a large artwork image breathe beside the copy block.

### Cart Drawer

**`cart-drawer`** — Slides in from the right over a {colors.scrim} overlay. White background with a 1px left border at {colors.hairline}. Item rows use {typography.body-sm} Geist for titles and {typography.price-display} Geist Mono for prices. The sticky checkout button at the drawer's base uses the full mint primary fill, matching the product-page CTA exactly.

### Footer

**`footer`** — Full-width {colors.ink} dark background. Section headings in {typography.title-sm} Geist semi-bold, links in {typography.body-sm}. The Fy! wordmark and newsletter input accent are rendered in {colors.primary} mint against the dark ground, echoing the CTA color and giving the footer its only vivid moment. Newsletter input uses a white fill with a mint focus border.

### Nav Bar

**`nav-bar`** — White canvas, 64px tall, with a 1px {colors.hairline} bottom border. Nav links in {typography.nav-link} Geist medium. Search icon, wishlist, and cart iconography on the right rail. Collapses below 1128px to logo + icons only; full-screen drawer reveals links on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | 1-column product grid; nav collapses to hamburger + full-screen drawer; size and frame selectors scroll horizontally; search bar full-width below logo row; hero headline drops to {typography.display-sm} |
| Tablet | 744–1128px | 2-column product grid; nav shows logo and cart icon only; search bar inline in header; category filter bar horizontally scrollable |
| Desktop | 1128–1440px | 3–4 column product grid; full nav with all links visible; product detail page splits image left and controls right at 60/40; cart drawer width fixed at 420px |
| Wide | > 1440px | Container max-width ~1440px centered; grid holds at 4 columns; hero gains extra horizontal padding; artwork images scale up within the grid cell |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Size selector pills expand via padding to 44px height on touch viewports
- Artist chips minimum 36px height with 12px horizontal padding
- Cart, search, and wishlist icons use 44×44px invisible tap area with optical centering
- Frame selector options minimum 48px height on mobile

### Collapsing Strategy
- Nav: links hidden below 1128px; hamburger opens a full-screen overlay drawer listing all navigation links, search, and account links
- Filter bar: horizontally scrollable pill strip below 744px; no wrapping at any breakpoint
- Product grid: 4-col → 3-col at 1128px → 2-col at 744px → 1-col at 480px
- Product detail: stacked single column below 744px (image full-width on top, controls below); side-by-side above 744px
- Hero: Playfair headline drops from {typography.display-xl} (48px) to {typography.display-sm} (24px) on mobile; CTA button goes full-width below 480px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact computed font sizes for display-xl and display-md not confirmed from live extraction; values estimated from Playfair Display editorial conventions
- No confirmed border-radius values from computed styles; {rounded.sm} and {rounded.md} inferred from visual screenshot descriptions
- primary-active (#00cc94) and primary-disabled (#99f5de) derived algorithmically — not extracted from CSS custom properties
- No box-shadow or elevation tokens extracted; product cards assumed to use border-only treatment
- Exact nav-bar height (64px) is an estimate; not confirmed from computed styles
- Spacing scale follows 8px grid convention — actual CSS custom property values not extracted
- Cart drawer animation easing and timing not captured
- Mobile-specific type scale overrides not confirmed; breakpoint values for typography assumed
