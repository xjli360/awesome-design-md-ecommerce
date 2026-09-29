---
version: alpha
name: "Kith"
source_url: "https://kith.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Amber-priced markdown figures against #141414 product cards — a single warm pigment in an otherwise achromatic system, where #f59e0b appears on sale callouts and strike-through labels while everything else runs through a tight grayscale from off-white canvas (#f6f6f6) to deep ink (#121212). Typography carries the brand's duality most visibly: altesse-std-64pt and linotype-didot-headline govern editorial moments with high-fashion authority, setting display at 60–72px in a light roman that reads closer to Vogue than a sneaker drop, while rocky-compressed and proxima-nova-extra-condensed build the counter-register — tightly tracked uppercase at 11–13px, stamped onto size chips and add-to-cart buttons like a garment care label. The wordmark sits on a cleared axis, black on #f6f6f6 in the default state; over dark editorial photography the nav inverts to white-on-transparent without swapping assets.

  Product cards make no editorial claims: full-bleed photography at a 3:4 aspect ratio, a one-line product name in {typography.title-md}, price below in {typography.price-display}. No badge appears unless an item is on sale, in which case {colors.accent-amber} carries the discount figure beside a struck-through original in {colors.muted}. Card corners are flush square ({rounded.none}) on desktop grids; hover state swaps the hero image to an alternate colorway at 200ms opacity — no translate, no scale, no overlay. Spacing between grid items holds at {spacing.sm} (8px), compressing the grid into the catalog density of a printed lookbook page.

  Hero modules break the product-grid logic entirely: full-viewport imagery, white centered display type in {typography.display-xl}, zero sub-heading, and a single ghost CTA at the lower edge. Seasonal lookbook sections import {typography.editorial-caption} in adobe-caslon-pro for set copy with generous leading. Footer runs on a #1f1f1f dark surface with link groups in {typography.nav-link} and legal copy in {typography.caption}, reversing the above-the-fold palette into the only persistently dark zone on the page. The Kith Treats sub-brand applies the same grammar — {typography.display-md} in adobe-caslon-pro against a warmer cream — demonstrating that the system extends to hospitality contexts without requiring new tokens.

colors:
  primary: "#141414"
  primary-active: "#000000"
  primary-disabled: "#dedede"
  ink: "#121212"
  body: "#1f1f1f"
  muted: "#545454"
  hairline: "#e2e2e2"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-dark: "#1f1f1f"
  on-primary: "#f6f6f6"
  on-dark: "#f6f6f6"
  accent-amber: "#f59e0b"
  accent-gold: "#fbbf24"

typography:
  display-xl:
    fontFamily: "'altesse-std-64pt', 'linotype-didot-headline', Georgia, serif"
    fontSize: 72px
    fontWeight: 300
    lineHeight: 1.0
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'altesse-std-24pt', 'linotype-didot', Georgia, serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'adobe-caslon-pro', 'garamond-premier-pro', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'adobe-caslon-pro', 'garamond-premier-pro', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'proxima-nova', Inter, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.04em
    textTransform: uppercase
  title-sm:
    fontFamily: "'proxima-nova', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.06em
    textTransform: uppercase
  body-md:
    fontFamily: "Inter, 'proxima-nova', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, 'proxima-nova', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, 'proxima-nova', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  editorial-caption:
    fontFamily: "'adobe-caslon-pro', 'garamond-premier-pro', Georgia, serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  price-display:
    fontFamily: "Inter, 'proxima-nova', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-sale:
    fontFamily: "Inter, 'proxima-nova', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'rocky-compressed', 'proxima-nova-extra-condensed', 'proxima-nova', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'rocky-compressed', 'proxima-nova-extra-condensed', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.10em
    textTransform: uppercase
  nav-link:
    fontFamily: "'proxima-nova', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  logo-wordmark:
    fontFamily: "'rocky-compressed', 'proxima-nova-extra-condensed', sans-serif"
    fontSize: 22px
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: 0.06em
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    rounded: "{rounded.none}"
    padding: 14px 24px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 23px
    height: 44px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 23px
    height: 44px
    border: "1px solid {colors.on-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    borderError: "1px solid {colors.accent-amber}"
    padding: 12px 16px
    height: 44px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.logo-wordmark}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-inverted:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.logo-wordmark}"
    height: 60px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    textColor: "{colors.ink}"
    hoverEffect: image-swap
    hoverTransition: 200ms opacity
  sale-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  sale-price:
    textColor: "{colors.accent-amber}"
    typography: "{typography.price-sale}"
  price-strike:
    textColor: "{colors.muted}"
    typography: "{typography.price-display}"
    textDecoration: line-through
  size-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 36px
    minWidth: 40px
  size-chip-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    height: 36px
  size-chip-unavailable:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    height: 36px
    textDecoration: line-through
  editorial-hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    displayTypography: "{typography.display-xl}"
    ctaVariant: button-ghost
    minHeight: 100vh
    contentAlign: center
  lookbook-module:
    backgroundColor: "{colors.canvas}"
    captionTypography: "{typography.editorial-caption}"
    titleTypography: "{typography.display-md}"
    textColor: "{colors.ink}"
    gridColumns: 2
    gap: "{spacing.sm}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.display-sm}"
    suggestTypography: "{typography.nav-link}"
    rounded: "{rounded.none}"
    backdropColor: "rgba(18,18,18,0.6)"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    logoTypography: "{typography.logo-wordmark}"
    linkTypography: "{typography.nav-link}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0"
    columnGap: "{spacing.xl}"
    gridColumns: 4

## Components

### Buttons

**`button-primary`** — 44px tall, square corners ({rounded.none}), full-bleed #141414 fill. Label in {typography.button-md}: rocky-compressed uppercase at 13px with 0.12em letter-spacing. Active state deepens to {colors.primary-active} (#000000); disabled renders {colors.primary-disabled} (#dedede) fill with {colors.muted} label. On mobile the button expands to full container width.

**`button-secondary`** — Same 44px height and square geometry, white fill with a 1px {colors.ink} border. Used as a paired secondary CTA beside button-primary on product detail pages. Hover inverts: black fill, white text via 150ms transition.

**`button-ghost`** — Transparent background with a 1px {colors.on-dark} border, deployed exclusively over full-bleed dark photography in {editorial-hero} modules. On light backgrounds it falls back to button-secondary styling. No rounding.

### Inputs

**`text-input`** — 44px height, {rounded.none}, 1px {colors.hairline} border at rest sharpening to 1px {colors.ink} on focus. Placeholder in {colors.muted}; label floats above in {typography.caption}. Error state uses a 1px {colors.accent-amber} bottom border — amber replaces a conventional red, consistent with the brand's single-accent discipline.

### Navigation

**`nav-bar`** — 60px tall, {colors.surface-soft} (#f6f6f6) background with 1px {colors.hairline} bottom border. Left: wordmark in {typography.logo-wordmark}. Center: category links in {typography.nav-link} — no underline at rest, underline on hover. Right: search icon, account icon, cart count as a plain {typography.caption} figure with no pill container. Sticks on scroll past 60px. On editorial hero pages loads as nav-bar-inverted (transparent, {colors.on-dark} text) without asset swap.

**`announcement-bar`** — 36px strip pinned above the nav, {colors.primary} fill, {colors.on-primary} text in {typography.button-sm}. Carries shipping thresholds and drop notifications. Single centered line; dismissed via cookie.

### Product Card

**`product-card`** — No shadow, no rounding. Image fills a 3:4 container; on hover a second image (alternate angle or colorway) swaps in at 200ms opacity — no transform, no scale. Below the image: product name in {typography.title-md} (tracked uppercase), brand label in {typography.caption} at {colors.muted}, price in {typography.price-display}. On-sale state: {sale-price} replaces default price, {price-strike} sits to its right, {sale-badge} ({colors.accent-amber} fill, {rounded.xs}) pins to the top-left corner of the image.

### Size Selector

**`size-chip`** / **`size-chip-selected`** / **`size-chip-unavailable`** — 36px-tall square buttons in a horizontal wrap grid with no gap between chips, abutting flush like a physical size-run tray. Unselected: white fill, {colors.hairline} border, {typography.button-sm} label. Selected: {colors.ink} fill, {colors.on-primary} text. Unavailable: white fill, struck-through label in {colors.hairline}, {colors.hairline-soft} border.

### Editorial Hero

**`editorial-hero`** — 100vh full-bleed image or video, white centered type in {typography.display-xl} (altesse-std-64pt, weight 300, −1.5px tracking). A single {button-ghost} CTA sits 60–80px above the bottom edge. No gradient overlay — photography provides contrast by art direction. On mobile, display type scales to {typography.display-lg} and the CTA goes full-width.

### Lookbook Module

**`lookbook-module`** — Two-column editorial grid with {spacing.sm} gutter, each cell a full-bleed image at variable aspect ratios. Section title in {typography.display-md} (adobe-caslon-pro). Caption in {typography.editorial-caption} (adobe-caslon-pro, 13px, generous leading) sits below each image, left-aligned. No CTA buttons; the entire module links to a collection page.

### Search Overlay

**`search-overlay`** — Full-page {colors.canvas} overlay with a large borderless input in {typography.display-sm} (adobe-caslon-pro, 22px). Recent searches and trending terms appear below in {typography.nav-link}. Backdrop: rgba(18,18,18,0.6). Dismiss via Escape or × icon top-right.

### Footer

**`footer`** — {colors.surface-dark} (#1f1f1f) background, the only persistently dark region. Wordmark in {typography.logo-wordmark} (white) anchors the top of the column grid. Four-column link groups in {typography.nav-link}. Legal copy and copyright in {typography.caption} at {colors.on-dark}, 60% opacity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + cart icon; hero display scales to {typography.display-lg} (48px); all CTAs full-width; announcement bar 32px; image-swap replaced by swipe gesture |
| Tablet | 744–1128px | Two-column product grid; nav shows wordmark + hamburger or partial category links; lookbook retains two-column layout |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with all category links visible; hero at full 100vh with {typography.display-xl} |
| Wide | > 1440px | Max-width container (~1440px) centered on viewport; product grid may expand to five columns; editorial imagery spans full viewport width with content constrained |

### Touch Targets

- All interactive elements minimum 44px tall (buttons, size chips, nav icons)
- Size chips on mobile expand horizontally to fill available width at a fixed 44px height
- Cart and account icons in mobile nav are 44×44px tap targets regardless of visible icon size
- Product image swipe gesture (left/right for alternate colorway) replaces hover swap on touch devices

### Collapsing Strategy

- Navigation collapses to hamburger drawer at < 1024px; drawer contains full category hierarchy in {typography.nav-link}
- Footer four-column grid reduces to two columns at tablet, single-column accordion on mobile
- Lookbook two-column grid collapses to full-width sequential panels on mobile with captions below each image
- Announcement bar shortens to a tighter copy variant on mobile if provided by content operators
- Search overlay input scales from {typography.display-sm} (22px) to {typography.body-md} (14px) on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact border-radius for sale-badge not confirmed from extraction; {rounded.xs} (2px) is inferred from the brand's near-flat rounding posture
- Color for interactive focus rings not extracted; {colors.ink} used as the closest approximation
- Kith Treats sub-brand cream/warm palette hex values not present in extraction; the Treats section uses warmer canvas tones that diverge from the main site's #f6f6f6
- Whether bickham-script-pro-3 appears in live UI or only inside editorial photography overlays is ambiguous from the extracted font stack alone
- Exact nav-bar height (60px used here) not confirmed; inferred from Shopify theme norms and comparable brand patterns
- Collaboration-specific seasonal site skins (known to exist for Versace, BMW, and others) not captured in this extraction snapshot
- Transition easing curves and precise duration values not available; 200ms opacity assumed from category convention
- Whether aurea-ultra is used for the wordmark or only for editorial display moments could not be determined from extraction alone
