---
version: alpha
name: "Mejuri"
source_url: "https://mejuri.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Warm ivory (#faf7f0) does most of the work on Mejuri's pages — the canvas is not white but a sun-bleached cream that makes 14k gold feel warmer and silver more deliberate. Against this base, a family of stone neutrals (#79786c, #68675e, #b2b0a1) carry hierarchy without tension, while a spare gold token (#bda37d) surfaces only where the product literally is: price highlights, hover states on featured pieces, and small editorial callouts that function as a visual sample of the metal itself. Deep warm brown (#544432) anchors the most legible text without tipping into pure black, keeping even fine-print captions warm. BrandonGrotesque runs the brand's everyday voice — pragmatic, precise, set tight on product labels and loose on editorial headers. KapraNeue and Moulin step in for display moments, adding display tension that prevents the site from reading like any other commerce template. SimonMono and CourierNew appear in data contexts — order confirmations, filter states, SKU labels — a utilitarian counterpoint. SyndicatGrotesk fills in secondary UI copy where BrandonGrotesque might read too soft. Corner radii stay minimal throughout: {rounded.xs} on input fields and badges, {rounded.sm} on cards and drawers — there is no pill shape on a Mejuri CTA. CTAs in warm stone (#79786c) with cream text sit at {rounded.sm}, grounding the interface without ornament. The sage family (#ebf1e1, #dbe9cc) appears in seasonal campaign surfaces and editorial callouts — not as brand color but as seasonal atmosphere, a background that retreats when the jewelry steps forward. Navigation is spare and horizontal, relying on generous spacing and {typography.nav-label} in tracked small caps rather than icon glyphs or heavy labels. Product cards hold to a strict two-column grid on mobile and four columns on desktop, each with a single hover-reveal for a second product image — the only animation Mejuri regularly employs. Promotional red (#d80027) appears only in sale and notification contexts, never as brand identity, so its appearance reads as urgency. The whole system encodes one thesis: the fewer design moves you make, the more the jewelry speaks for itself.

colors:
  primary: "#79786c"
  primary-active: "#68675e"
  primary-disabled: "#b2b0a1"
  gold: "#bda37d"
  gold-warm: "#cdc3b4"
  ink: "#544432"
  body: "#68675e"
  muted: "#b2b0a1"
  muted-soft: "#c0b9b8"
  hairline: "#ebebe8"
  hairline-soft: "#f3f3f3"
  canvas: "#faf7f0"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  surface-sage: "#ebf1e1"
  surface-sage-deep: "#dbe9cc"
  on-primary: "#faf7f0"
  on-dark: "#faf7f0"
  alert: "#d80027"
  alert-deep: "#9c0001"
  promo: "#ff9626"
  accent-pink: "#f2447b"

typography:
  display-xl:
    fontFamily: "'KapraNeue', 'Moulin', 'BrandonGrotesque', sans-serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'KapraNeue', 'Moulin', 'BrandonGrotesque', sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'BrandonGrotesque', 'SyndicatGrotesk', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'BrandonGrotesque', 'SyndicatGrotesk', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'BrandonGrotesque', 'SyndicatGrotesk', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'BrandonGrotesque', 'SyndicatGrotesk', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'BrandonGrotesque', 'SyndicatGrotesk', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'BrandonGrotesque', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  caption-mono:
    fontFamily: "'SimonMono', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  nav-label:
    fontFamily: "'BrandonGrotesque', 'SyndicatGrotesk', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'BrandonGrotesque', 'SyndicatGrotesk', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'BrandonGrotesque', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'BrandonGrotesque', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-sale:
    fontFamily: "'BrandonGrotesque', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge-text:
    fontFamily: "'BrandonGrotesque', sans-serif"
    fontSize: 9px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  eyebrow:
    fontFamily: "'BrandonGrotesque', 'SyndicatGrotesk', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 2px
    textTransform: uppercase
  product-name:
    fontFamily: "'BrandonGrotesque', 'SyndicatGrotesk', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px

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
    padding: 14px 32px
    height: 44px
    transition: background-color 200ms ease
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: none
    padding: 0
    textDecoration: underline
  button-gold:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 24px
  nav-bar-transparent:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-label}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    nameTypography: "{typography.product-name}"
    priceTypography: "{typography.price-display}"
    nameColor: "{colors.ink}"
    priceColor: "{colors.body}"
    hoverImageSwap: true
    badgePosition: top-left
    gap: "{spacing.sm}"
  product-card-grid:
    columns-mobile: 2
    columns-tablet: 3
    columns-desktop: 4
    gap: "{spacing.base}"
  hero-editorial:
    backgroundColor: "{colors.surface-sage}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaVariant: button-primary
    layout: full-bleed
    minHeight: 80vh
    padding: "{spacing.section}"
  hero-warm:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaVariant: button-primary
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge-text}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  badge-sale:
    backgroundColor: "{colors.alert}"
    textColor: "#ffffff"
    typography: "{typography.badge-text}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  badge-low-stock:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge-text}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  price-regular:
    typography: "{typography.price-display}"
    color: "{colors.body}"
  price-sale-display:
    typography: "{typography.price-sale}"
    color: "{colors.alert}"
  price-original-struck:
    typography: "{typography.price-display}"
    color: "{colors.muted}"
    textDecoration: line-through
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
    padding: 6px 14px
  swatch-picker:
    size: 20px
    rounded: "{rounded.full}"
    border-unselected: "1px solid transparent"
    border-selected: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
  drawer-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    width: 320px
    padding: "{spacing.lg}"
    borderRight: "1px solid {colors.hairline}"
  eyebrow-section:
    typography: "{typography.eyebrow}"
    color: "{colors.muted}"
    marginBottom: "{spacing.sm}"
  editorial-callout:
    backgroundColor: "{colors.surface-sage-deep}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section}"
    rounded: "{rounded.none}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: none
    padding: 10px 16px
    height: 40px
  quantity-selector:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 44px
    width: 120px
  sticky-add-to-cart:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.base}"
    ctaVariant: button-primary
    position: fixed
    bottom: 0
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.gold-warm}"
    linkColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.nav-label}"
    padding: "{spacing.section}"
  membership-banner:
    backgroundColor: "{colors.surface-sage-deep}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    eyebrowTypography: "{typography.eyebrow}"
    padding: "{spacing.md} {spacing.base}"

## Components

### Buttons

**`button-primary`** — Full-width on mobile, fixed-width (min 200px) on desktop. Background is warm stone (#79786c), text cream (#faf7f0), uppercase tracked BrandonGrotesque at 13px/1px spacing, 44px height with {rounded.sm}. Hover shifts to `button-primary-active` (#68675e) over 200ms. Disabled state uses muted stone (#b2b0a1) and `cursor: not-allowed`; no opacity trick — the background swap communicates unavailability more cleanly than a fade.

**`button-secondary`** — Transparent fill with a 1px {colors.ink} border, same height and typography as primary. Used for "Add to Wishlist", secondary CTAs on editorial pages, and overlay close triggers. On dark editorial backgrounds, the border color flips to {colors.on-dark}.

**`button-ghost`** — No border, no background. Underlined body text in {colors.body}, 11px/0.8px tracked uppercase. Used for "View all", inline filter resets, and dismissal links inside drawers and toasts.

**`button-gold`** — Identical spec to `button-primary` but background is {colors.gold} (#bda37d). Reserved for membership upsell CTAs, gifting flows, and anniversary/limited edition product pages where the metal color itself is the message.

### Inputs & Search

**`text-input`** — Warm ivory (#faf7f0) fill, 1px hairline border (#ebebe8) at rest, stepping to 1px primary (#79786c) on focus — no box-shadow ring. Placeholder in {colors.muted}. Used for email capture, checkout fields, and gift message. Height 44px, {rounded.xs}, body-md type.

**`search-bar`** — Surface-soft (#f3f3f3) fill, borderless, {rounded.xs}. Sits inside a full-width overlay panel that drops from the nav on icon click. Placeholder "Search jewelry, materials, or collections" in {colors.muted} at body-sm. Results appear below in a scrollable panel with product thumbnails and category shortcuts.

### Navigation

**`nav-bar`** — 64px tall, canvas (#faf7f0) background, 1px hairline bottom border. Logo centered on mobile, left-aligned on desktop. Nav links in `nav-label` (12px uppercase, 1.5px tracking). On editorial hero pages, `nav-bar-transparent` overlays the image with cream text; it re-renders as the opaque canvas variant on scroll past 80px. A cart icon with item-count dot sits right; the dot uses {colors.alert} background (#d80027) for non-zero counts, {colors.ink} for zero.

**`drawer-nav`** — 320px slide-in from left. Canvas background, hairline right border. Top section holds the full category tree in `nav-label` with indented subcategories in `body-sm`. Bottom section exposes account, wishlist, and country selector. Overlay scrim uses rgba(84,68,50,0.4) drawn from {colors.ink}.

### Product Cards & Grid

**`product-card`** — No border, no shadow. Image fills a strict 3:4 aspect ratio; second image swaps in on hover (desktop) or on tap-hold (mobile) — no fade, straight swap. Product name in `product-name` (13px, weight 400, {colors.ink}), price below in `price-display` ({colors.body}). Sale pricing shows `price-sale-display` in {colors.alert} alongside `price-original-struck` in {colors.muted}. Badges (`badge-new`, `badge-sale`, `badge-low-stock`) float top-left over the image at {spacing.xs} inset, stacked vertically if multiple apply. No border radius on the card itself — images bleed to the container edge.

**`product-card-grid`** — 2 columns on mobile (gap {spacing.base}), 3 on tablet, 4 on desktop. No asymmetric hero cards or featured-size overrides in the base grid; editorial breakouts happen in separate full-bleed row modules above or below the grid.

### Hero & Editorial

**`hero-editorial`** — Full-bleed at 80vh minimum. Background defaults to `surface-sage` (#ebf1e1) for seasonal campaigns; swap to `surface-sage-deep` (#dbe9cc) for richer tones or full-bleed photography with `nav-bar-transparent`. Headline in `display-xl` (56px, weight 300, KapraNeue/Moulin), eyebrow in `eyebrow` above it, CTA is `button-primary`. Text block sits bottom-left on desktop, centered on mobile.

**`editorial-callout`** — A full-width content band with `surface-sage-deep` background. Used between product grid sections to break commerce rhythm with short brand copy or material education. Headline in `display-md`, body in `body-md`, optional CTA in `button-secondary`. No border radius — the band bleeds edge to edge.

**`membership-banner`** — Slim persistent band (56px) in `surface-sage-deep` anchored below the nav. Eyebrow in `eyebrow` ("MEJURI FOR ALL"), body copy in `body-sm`. Dismissable with a ghost close button right-aligned. Used for loyalty program and free-shipping threshold messaging.

### Badges

**`badge-new`** — Black fill (#544432 ink), cream text, 9px uppercase BrandonGrotesque, 1px tracked. Sits top-left on product card images, no radius, flush rectangular label. Never applied to products older than 60 days from launch.

**`badge-sale`** — Alert red (#d80027) fill. Same spec as badge-new. Only fires when a variant has an active compare-at price. Coexists with badge-new stacked vertically if needed.

**`badge-low-stock`** — Gold (#bda37d) fill, cream text. Fires when inventory drops below 5 units on a variant. Communicates scarcity without the alarm of a red badge.

### Filtering & Swatches

**`filter-pill`** — Full pill shape ({rounded.full}), 1px hairline border, canvas background. Inactive state uses {colors.body} text; active flips to `filter-pill-active` with ink fill and cream text. Used in horizontal scroll rows above collection grids. Labels in `caption` (11px, 0.5px tracked).

**`swatch-picker`** — 20px circles, gap {spacing.xs}. At rest, no visible border on the circle itself — hover adds a faint 1px hairline ring. Selected state shows a 2px {colors.ink} ring with a 2px gap (ring-offset effect). Tooltip on hover shows material name in `caption-mono` for non-obvious colors.

### Pricing

**`price-regular`** — 15px BrandonGrotesque weight 400, {colors.body}. Displayed below product name on cards and at the top of PDP price block.

**`price-sale-display`** — Same size, weight 500, {colors.alert} (#d80027). Replaces `price-regular` position when a sale price is active. The original price renders as `price-original-struck` immediately to the right, struck through in {colors.muted}.

### Checkout Components

**`sticky-add-to-cart`** — Fixed bottom bar appearing when the primary PDP CTA scrolls out of view. Canvas background with a 1px hairline top border. Contains product thumbnail (32px, {rounded.xs}), truncated product name in `title-sm`, selected variant in `caption-mono`, and a full `button-primary` CTA. Hidden on desktop where the PDP sidebar remains in view.

**`quantity-selector`** — Minus / number / plus in a 120px × 44px row, 1px hairline border, {rounded.xs}. Minus and plus are icon buttons with {colors.body} ink; the count reads in `body-md` center-aligned. Quantity caps at available inventory; at cap, the plus icon dims to {colors.muted-soft}.

### Footer

**`footer`** — Dark warm-brown (#544432) fill, four-column link grid on desktop collapsing to accordion on mobile. Column headings in `nav-label` with {colors.gold-warm} (#cdc3b4) color; links in `body-sm` with {colors.muted-soft}. Social icons (Instagram, Pinterest, TikTok) right-aligned. Newsletter email input rendered in `text-input` variant with dark-mode overrides: canvas replaced by rgba(255,255,255,0.08), border {colors.muted-soft}. Legal copy in `caption-mono` at the very bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column hero text centered; product grid 2-col; nav collapses to hamburger + centered logo + cart icon; `drawer-nav` replaces horizontal nav; filter pills scroll horizontally; sticky ATC bar visible; footer accordion |
| Tablet | 744–1128px | 3-col product grid; nav shows primary categories only (secondary on hover); hero text left-aligned; `drawer-nav` still used for full category tree |
| Desktop | 1128–1440px | 4-col product grid; full horizontal nav with mega-menu dropdowns; PDP switches to two-column layout (images left, details sticky right); sticky ATC hidden |
| Wide | > 1440px | Max-width container 1440px centered; product grid stays 4-col; hero content max-width 1200px; additional whitespace added via increased section padding |

### Touch Targets

- All interactive elements minimum 44 × 44px on mobile
- Swatch pickers expand tap target to 32px via padding even though visible circle is 20px
- Filter pills minimum 36px height with extended horizontal padding
- Nav drawer links 48px row height with full-width tap target
- Quantity selector buttons 44px × 44px, not icon-sized

### Collapsing Strategy

- Primary nav: full horizontal links → hamburger drawer (no hybrid icon-only state)
- Hero: full-bleed image with overlaid text → stacked image-above / text-below on mobile
- Footer: 4-column grid → single-column accordion with expand/collapse per section
- PDP layout: 2-column sticky sidebar → single-column with sticky ATC bar
- Filter bar: horizontal overflow scroll with fade mask at right edge; no dropdown fallback
- Editorial callout: side-by-side image + text → image full-width stacked above text

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No definitive confirmation of exact button border-radius value from live site; {rounded.sm} (8px) is inferred from general brand softness — could be {rounded.xs} (4px)
- `surface-card` (#ffffff) is not in the extracted palette; it is implied by product card backgrounds and may be identical to {colors.canvas} (#faf7f0) in practice
- Exact font-weight assignments for KapraNeue and Moulin display faces not confirmed — weight 300 is inferred from the brand's preference for light editorial headlines
- Liquid and Slick font stacks appear in extraction but their usage context is unclear; Liquid may be a custom script/logotype face used only in SVG, Slick may be a carousel library default
- Mega-menu dropdown structure and hover animation timing not extractable from static analysis
- Mejuri For All membership program badge/icon assets not captured
- Exact letter-spacing values for display-xl and display-md are estimates; the brand may use tighter tracking on larger KapraNeue sizes
- Gold accent usage boundary between editorial and functional contexts is not precisely mapped; {colors.gold} (#bda37d) application rules are inferred from brand positioning rather than confirmed token assignment
