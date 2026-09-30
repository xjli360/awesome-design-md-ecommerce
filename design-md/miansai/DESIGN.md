---
version: alpha
name: "Miansai"
source_url: "https://www.miansai.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Metal staging drives the interface — the same #313131 charcoal that backgrounds Miansai's cuff-and-cord photography bleeds into navigation chrome and editorial sections, treating every screen surface as a dark velvet setting for the pieces themselves. Founded in Miami by Michael Saiger, the brand built its identity on a specific visual tension — raw nautical rope knotted through precision-milled brass hardware — and that push-pull reads in the digital system too: hard geometric grid structures offset by warm metallic accent tones, stark ink on open white canvas interrupted by the close crop and the deliberate absence of decoration. The color vocabulary lives almost entirely in one extracted tone (#313131), a blue-black charcoal that is neither true black nor a warm gray, working throughout as primary CTA fill, body type anchor, and the dominant value in product photography. White canvas (#ffffff) provides the negative space with near-zero surface hierarchy — surface-soft barely separates itself at #f9f9f9 — which keeps focus relentlessly on the metal, cord, and stone in the product frames. A muted brass-gold (#c4a97d) enters only as accent: in material-selector indicators, engraving badges, and occasional editorial callout headlines, calibrated to read as the actual jewelry rather than a branding device. Typography runs on system sans-serif stacks — no custom typeface was captured in extraction, likely served via a JS-loaded resource or anti-bot wall — favoring restraint throughout: display sizes under 40px, body type at 15–16px with generous 1.6× line-height, and near-total absence of uppercase tracking except on small collection-filter labels. Component geometry is deliberately austere: `{rounded.none}` or `{rounded.xs}` on buttons and inputs, no pill shapes anywhere. The product card is essentially a full-bleed photograph with a single line of type and price at the bottom edge — corner radius zero. This is a system that trusts its product photography completely and strips every UI element that might compete with a shot of oxidized silver against black cord.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#1a1a1a"
  body: "#313131"
  muted: "#767676"
  muted-soft: "#a8a8a8"
  hairline: "#e0e0e0"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  surface-dark-overlay: "rgba(26,26,26,0.55)"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-gold: "#c4a97d"
  accent-gold-soft: "#e8d9bb"
  error: "#b52a2a"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 38px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.02em
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  caption-upper:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  price-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.10em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.10em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.04em

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
    rounded: "{rounded.none}"
    padding: "14px 28px"
    height: 46px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "13px 27px"
    height: 46px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "0 0 2px 0"
    borderBottom: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    padding: "12px 14px"
    height: 46px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoHeight: 20px
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: none
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "4/5"
    imageRadius: "{rounded.none}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.body}"
    padding: "0 0 {spacing.base} 0"
    gap: "{spacing.sm}"
    hoverOverlay: none
  product-card-quick-add:
    overlayBackground: "rgba(255,255,255,0.92)"
    buttonStyle: "button-primary"
    overlayTransition: "opacity 180ms ease"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 580px
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    paddingX: "{spacing.xl}"
    paddingY: "{spacing.xxl}"
    textAlign: left
    overlayStyle: "{colors.surface-dark-overlay}"
  hero-split:
    layout: "50/50 grid"
    leftBackground: "{colors.surface-dark}"
    rightBackground: "{colors.canvas}"
    imagePosition: left
    textPadding: "{spacing.xl}"
    titleTypography: "{typography.display-md}"
  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
    padding: "4px {spacing.sm}"
    border: "1px solid {colors.hairline}"
  material-badge-gold:
    backgroundColor: "{colors.accent-gold-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
    padding: "4px {spacing.sm}"
  engraving-badge:
    backgroundColor: transparent
    textColor: "{colors.accent-gold}"
    typography: "{typography.caption-upper}"
    iconSize: 12px
    borderBottom: "1px solid {colors.accent-gold}"
    padding: "0 0 2px 0"
  collection-filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption-upper}"
    activeIndicator: "2px solid {colors.primary}"
    gap: "{spacing.xl}"
    paddingY: "{spacing.md}"
    borderBottom: "1px solid {colors.hairline}"
  swatch-selector:
    size: 20px
    rounded: "{rounded.full}"
    borderDefault: "1px solid {colors.hairline}"
    borderSelected: "2px solid {colors.primary}"
    gapBetween: "{spacing.sm}"
    goldSwatch: "{colors.accent-gold}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.primary}"
    padding: "8px 14px"
    unavailableLine: "1px diagonal"
  product-detail-sticky-bar:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    ctaWidth: 200px
    position: fixed
    bottom: 0
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    height: 36px
    textAlign: center
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.ink}"
    linkHoverColor: "{colors.primary}"
    borderTop: "1px solid {colors.hairline}"
    columnGap: "{spacing.xxl}"
    paddingY: "{spacing.section}"
    headingTypography: "{typography.caption-upper}"
    headingColor: "{colors.muted}"

## Components

### Buttons

**`button-primary`** — A full-fill charcoal (#313131) rectangle with zero radius, 46px height, and uppercase tracked text at 0.10em letter-spacing. The hard edge signals precision over approachability — appropriate for a brand that manufactures to tight tolerances. Hover darkens to `{colors.primary-active}` (#1a1a1a) with no motion; disabled state desaturates to `{colors.primary-disabled}` with identical geometry.

**`button-secondary`** — Same geometry as primary but white fill with a 1px charcoal border. Used for secondary actions like "Save to wishlist" or size guide links. Active state fills with `{colors.surface-soft}` to avoid a bare white-on-white read.

**`button-ghost`** — Transparent background with only a bottom border underline in `{colors.primary}`. Used inline within product descriptions, editorial modules, and "Read more" expanders. The stripped-down form keeps text-adjacent CTAs from adding visual weight to dense editorial copy.

### Inputs

**`text-input`** — Flat rectangle, no radius, 46px height matching button height. Border transitions from `{colors.hairline}` to `{colors.primary}` on focus — no box-shadow, no glow, just a crisp 1px swap that keeps the interaction vocabulary consistent with the product photography's hard-edge aesthetic.

### Navigation

**`nav-bar`** — 60px tall, white canvas, 1px soft hairline bottom. Logo centered or left-aligned at 20px height. Links in `{typography.nav-link}` (13px, light tracking). On editorial/campaign pages with dark hero imagery, flips to `nav-bar-dark`: surface-dark background, white type, no border — the bar becomes part of the image composition rather than a UI layer on top of it.

**`announcement-bar`** — 36px strip in `{colors.primary}` with white uppercase caption text. Sits above the nav bar and carries free shipping thresholds, new collection launches, or engraving promotions.

### Product Card

**`product-card`** — 4:5 aspect-ratio image, zero border-radius, flush to the grid edge. Below the image: a single line of `{typography.body-sm}` product name in `{colors.ink}`, then price in `{typography.price}` in `{colors.body}`. No add-to-cart button visible by default; `product-card-quick-add` overlays a 92%-opacity white scrim on hover with a full-width `button-primary` ("Add to Cart") appearing at bottom center. The overlay uses a 180ms ease fade — slow enough to feel deliberate, not accidental.

### Hero

**`hero`** — Full-width dark section with minimum 580px height, product photography filling the frame, overlay scrim at 55% opacity to ensure white type contrast. Title at `{typography.display-xl}` (38px, weight 300) sits left-aligned with a maximum width of ~520px to prevent the heading from spanning the full frame. A `button-primary` CTA sits 24px below the subtitle.

**`hero-split`** — 50/50 two-column layout for collection launches: full-bleed product image on the left (dark staging), editorial text block on right in white canvas with `{typography.display-md}` heading and a ghost button. Used to introduce new material colorways.

### Badges and Tags

**`material-badge`** — Small pill-less rectangle with `{typography.caption-upper}` text (11px, 0.12em tracking, uppercase) in surface-soft with a hairline border. Carries values like "14K Gold" or "Sterling Silver" on product cards and detail pages. A gold variant (`material-badge-gold`) swaps the background to `{colors.accent-gold-soft}` for precious metal designations.

**`engraving-badge`** — Text-only label in `{colors.accent-gold}` with a bottom-border underline in the same tone. Appears on product detail pages to indicate engraving availability — the gold color gives it the only moment of warm metal hue in an otherwise neutral chrome.

### Selectors

**`swatch-selector`** — 20px circle swatches with `{rounded.full}`, hairline border default, swapping to a 2px solid `{colors.primary}` ring on selection. Gap between swatches at `{spacing.sm}`. Gold swatch renders as `{colors.accent-gold}`.

**`size-selector`** — Flat rectangular buttons in `{typography.caption-upper}`, 1px hairline border default, 1px `{colors.primary}` border selected. Unavailable sizes show a diagonal line through the center — no background change, just the strikethrough to keep the grid visually clean. Padding 8px × 14px.

**`collection-filter-bar`** — Horizontal tab row in `{typography.caption-upper}`. Active tab marked by a 2px bottom border in `{colors.primary}` rather than a background fill — consistent with the brand's avoidance of filled shapes beyond CTAs. Sits above collection grids with a hairline separator from page content below.

### Product Detail Sticky Bar

**`product-detail-sticky-bar`** — Fixed to the bottom viewport edge on scroll past the main CTA zone. White canvas background with a 1px hairline top border. Contains product name at `{typography.title-sm}`, price at `{typography.price}`, and a 200px-wide `button-primary`. The narrowed CTA width keeps the bar from feeling like a full-width banner and allows related metadata to sit beside it.

### Footer

**`footer`** — Surface-soft (#f9f9f9) background with 1px hairline top border. Four-column grid: Shop, About, Customer Service, and Social/Newsletter. Column headings use `{typography.caption-upper}` in `{colors.muted}`. Links use `{typography.body-sm}` in `{colors.ink}`, transitioning to `{colors.primary}` on hover. Section padding 64px top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo; hero height drops to 420px; sticky bar becomes full-width; filter bar scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links only, secondary links in overflow; hero split becomes stacked (image top, text below) |
| Desktop | 1128–1440px | Three or four-column product grid; full nav visible; hero split renders at 50/50; sticky detail bar visible |
| Wide | > 1440px | Grid max-width capped at ~1360px with auto side margins; hero and editorial modules remain full-bleed with centered content column |

### Touch Targets

- All buttons and inputs minimum 46px height on mobile
- Swatch selectors expand to 28px diameter on touch viewports
- Size selector buttons increase padding to 12px × 20px on mobile
- Nav hamburger target minimum 44 × 44px
- Product cards in mobile grid maintain full tap surface including image; no hover-only interactions

### Collapsing Strategy

- Desktop four-column grid → three-column at tablet → two-column at mobile landscape → single-column at mobile portrait
- Hero split module stacks vertically at tablet breakpoint; text block sits below image at full width
- Announcement bar persists across all breakpoints; text truncates with ellipsis below 375px
- Filter bar switches from horizontal tab row to a horizontal scroll strip at mobile, with scroll-snap alignment per filter item
- Footer four-column grid collapses to two-column at tablet and single accordion-style column at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extracted from the live site — the page returned an anti-bot challenge ("Just a moment...") blocking full CSS extraction. All palette values beyond `{colors.primary}` (#313131) are inferred from brand context and may not match production tokens.
- No custom typeface was captured; extraction returned only system-font stacks. Miansai likely serves a licensed or custom sans-serif (possibly a Helvetica variant or a bespoke grotesque) via a JS-loaded font resource. Typography tokens use Helvetica Neue as the best available proxy.
- No meta theme-color was available, so mobile browser chrome color is unconfirmed.
- Exact border-radius values for image containers and modals are unconfirmed — zero-radius is inferred from brand aesthetic.
- Hover and transition timing functions are unconfirmed beyond qualitative observation.
- Dark-mode support status is unknown.
- Specific grid gutter widths and column counts are inferred from common Miansai layout observations rather than extracted CSS grid values.
