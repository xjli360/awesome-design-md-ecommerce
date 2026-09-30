---
version: alpha
name: "Marine Layer"
source_url: "https://www.marinelayer.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The product photography consistently shows crumpled hems and relaxed posture — no crisp folds, no catalogue stiffness — and the digital palette makes that strategy explicit; only three hex values came through extraction. #121212 near-black handles every primary CTA and product title with flat authority, no gradients, no drop shadows, nothing that implies effort; against a white canvas, #dedede hairlines barely register, creating the impression that product imagery simply floats; #475569 slate manages secondary copy and navigational metadata with enough distance from near-black ink to read hierarchy without opening a second color channel. No brand-voltage accent punches through — the restraint is the entire design position. Primary CTAs run in #121212 with #ffffff type, a dark-button treatment that carries authority without aggression, with the active state falling to pure black and disabled pulling back to a mid-gray, all within the same monochrome register. Font extraction returned nothing, signaling JavaScript-loaded tokens; from widely visible brand usage, Marine Layer deploys a humanist sans-serif at measured weights — display around 500–600, body at 400 — with generous 1.5 line heights that add air without color. Rounded corners are conservative throughout: product cards at {rounded.xs}, CTA buttons at the same, only Re-Spun sustainability pill tags closing to {rounded.full}. Whitespace is the primary layout tool — {spacing.lg} gutters on the product grid, {spacing.section} for section breaks — and the footer gives email capture real estate without decorating it. The whole system communicates one thing: the garment is soft; everything else stays out of the way.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#b0b0b0"
  ink: "#121212"
  body: "#2d2d2d"
  muted: "#475569"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  slate: "#475569"

typography:
  display-xl:
    fontFamily: "'Aktiv Grotesk', 'Helvetica Now', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Aktiv Grotesk', 'Helvetica Now', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Aktiv Grotesk', 'Helvetica Now', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Aktiv Grotesk', 'Helvetica Now', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Aktiv Grotesk', 'Helvetica Now', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Aktiv Grotesk', 'Helvetica Now', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Aktiv Grotesk', 'Helvetica Now', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Aktiv Grotesk', 'Helvetica Now', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Aktiv Grotesk', 'Helvetica Now', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
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
    rounded: "{rounded.xs}"
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
    padding: 13px 23px
    height: 48px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxHeight: 28px
  promo-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "10px {spacing.base}"
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    secondaryTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  product-card-original-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    imageOverlay: "rgba(0,0,0,0.15)"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.hairline}"
    activeRing: "2px solid {colors.ink}"
    activeRingOffset: 2px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.ink}"
    disabledTextColor: "{colors.primary-disabled}"
    height: 40px
    minWidth: 40px
  re-spun-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
    border: "1px solid {colors.hairline}"
  sale-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  newsletter-signup:
    backgroundColor: "{colors.surface-soft}"
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    inputBg: "{colors.canvas}"
    inputBorder: "1px solid {colors.hairline}"
    buttonBg: "{colors.primary}"
    buttonText: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.xl}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    linkColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.badge}"
    dividerColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.ink}"
    padding: "{spacing.base} 0"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"

## Components

### Buttons

**`button-primary`** — A flat #121212 rectangle at 48px tall with {rounded.xs} corners and 14px/500-weight type set at 0.5px letter-spacing in #ffffff. There is no hover color shift, no shadow on press — the active state moves to pure #000000 and the disabled state pulls back to #b0b0b0, keeping all three within the same monochrome register. This is a brand that does not decorate its actions.

**`button-secondary`** — Same 48px height as primary, white fill with a 1px #121212 perimeter stroke and dark type. The border carries the hierarchy signal rather than a fill color, making it read as an alternative CTA alongside the primary — particularly useful in hero layouts where a photography backdrop already provides a dark field. Focus state adds a 2px offset ring matching the border color.

**`button-text`** — A bare underlined link at {typography.body-sm} for secondary navigation actions such as "View All" or "Learn More" that would be over-weighted by a bordered button. No padding box, inherits surrounding line height, inherits container color.

### Text Input

**`text-input`** — 48px tall with {rounded.xs} and a #dedede hairline border that upgrades to a solid #121212 stroke on focus. Placeholder type runs in {colors.muted} slate. The border-weight-and-color change is the only interactive signal in the system — no glow, no background shift — keeping form fields invisible when idle and legible when active. Used across search, email capture, and account flows.

### Nav Bar

**`nav-bar`** — 60px tall white bar with a 1px #dedede bottom divider that only becomes perceptible when content scrolls beneath it. Logo sits left at a maximum 28px height; utility icons (search, bag, account) cluster right; primary navigation is a centered horizontal list at {typography.nav-link} 14px/400 weight. On mobile the horizontal list collapses into a hamburger that opens a full-screen overlay drawer. A `promo-banner` strip — #121212 background, {typography.caption} white text, dismissible via a right-aligned ✕ — sits above the nav and is factored into scroll-offset calculations so sticky positioning doesn't miscalculate.

### Product Card

**`product-card`** — Portrait 3:4 image above a two-line text stack: product name in {typography.body-sm} and price in {typography.body-md}. No card border, no box shadow — cards float on the white canvas with only image edges for definition. {rounded.xs} on the image container. On hover, a secondary colorway image swaps in and a "Quick Add" button surfaces at the bottom of the image without altering card dimensions. Sale items show the original price struck through in {colors.muted} at {typography.body-sm}, with the sale price in {colors.ink} at {typography.body-md}. A `sale-badge` in #121212 may overlay the top-left image corner.

### Hero Banner

**`hero-banner`** — Full-width photography with a 15% dark overlay to hold white type without heavy scrim treatment; Marine Layer's photography is consistently well-exposed. Heading at {typography.display-xl} 32px/500 sits left-aligned or centered depending on campaign. A subtitle at {typography.body-md} follows with a button-primary CTA below at {spacing.md} gap. Mobile crops to 4:5 or full viewport height and the heading steps down to {typography.display-md}.

### Color Swatch

**`color-swatch`** — 24px circles at {rounded.full} with a 1.5px #dedede border at rest. The active swatch gains a 2px #121212 outer ring with 2px offset, a clear selection state that requires no color. A white swatch carries the same #dedede border with no active-ring ambiguity since the border reads on canvas. Displayed as a horizontal row of up to eight swatches beneath the product name on both the grid card hover and the product detail page.

### Size Selector

**`size-selector`** — Square-adjacent 40px minimum buttons at {rounded.xs} with a #dedede border at rest and a #121212 border when selected. Sold-out sizes appear in {colors.primary-disabled} with a diagonal strike-through line through the center. Type at {typography.body-sm}. Displayed as a horizontally scrollable row on mobile; wraps to grid on desktop for extended sizing runs.

### Re-Spun Badge

**`re-spun-badge`** — A small pill at {rounded.full} with {colors.surface-soft} fill, #dedede border, and {colors.muted} text in {typography.badge} uppercase. Marks products eligible for Marine Layer's garment-return and recycling program. Appears beneath the price on the product detail page rather than on the grid card, keeping the browse experience clean and surfacing sustainability context only to engaged shoppers reading the full PDP.

### Promo Banner

**`promo-banner`** — A thin #121212 strip above the nav bar, horizontally centered white {typography.caption} text. Used for sitewide promotions, free-shipping thresholds, and sale countdowns. A right-aligned ✕ icon in {colors.on-primary} dismisses it for the session. Height is content-driven, typically 36–40px for a single text line.

### Newsletter Signup

**`newsletter-signup`** — A full-width {colors.surface-soft} section with {spacing.xxl} vertical padding. Heading at {typography.title-md}, supporting copy at {typography.body-sm} in {colors.muted}. Email input runs full-width with a joined button-primary on desktop and stacked full-width input plus button on mobile. No illustration, no background pattern — the section earns attention through spatial weight alone.

### Footer

**`footer`** — White background with {spacing.xxl} vertical padding. Link columns at {typography.body-sm} with column headings at {typography.badge} uppercase and {spacing.md} bottom margin. Social icons are monochrome #121212 at 20px, spaced at {spacing.base}. A horizontal #dedede rule separates the link block from the legal/copyright strip at the base. Re-Spun program copy often occupies a dedicated module directly above the main footer block.

### Accordion

**`accordion`** — Used on product detail pages for Fabric & Care, Fit Notes, and Sustainability panels. Each row has a 1px #dedede bottom border and a right-aligned chevron or +/− icon in {colors.ink}. Body text at {typography.body-sm} expands with {spacing.base} top padding inside the open panel. Height transition only — no fade, no bounce — consistent with the brand's anti-effort visual language.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero crops to 4:5 or full-viewport height with heading at {typography.display-md}; size selector scrolls horizontally; newsletter input and button stack full-width; footer columns collapse to accordion panels |
| Tablet | 744–1128px | Two-column product grid; nav may show primary links if space allows, otherwise drawer; hero remains full-width with intermediate heading scale |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav; hero at full viewport width; newsletter input and CTA inline |
| Wide | > 1440px | Content caps at ~1440px max-width container with auto side margins; hero image remains edge-to-edge behind the bounded content layer |

### Touch Targets

- All interactive elements — buttons, swatches, size tiles, nav icons — maintain a minimum 44×44px touch target
- Color swatches at 24px visual size are padded to 44px tap area via transparent padding
- Mobile nav utility icons maintain {spacing.xl} horizontal separation
- Accordion rows have {spacing.base} vertical padding ensuring a comfortable tap zone on the trigger row
- Promo banner ✕ dismiss icon has a minimum 44px target regardless of visual icon size

### Collapsing Strategy

- Navigation: full horizontal list → hamburger with full-screen slide-in drawer; account, search, and bag icons persist at all widths in the fixed header
- Product grid: 4 col → 3 col → 2 col → 1 col as viewport narrows
- Footer: multi-column link layout → stacked accordion panels on mobile; legal strip remains a single centered line at all widths
- Hero CTAs: side-by-side primary + secondary → stacked vertically on mobile with full-width buttons
- Promo banner: full message visible on desktop → shortened to essential offer text on mobile if line wraps

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Exact font family unconfirmed**: JavaScript-loaded tokens blocked font extraction; the Aktiv Grotesk / Helvetica Now stack is inferred from visual brand inspection and should be replaced with the confirmed loaded family once verified via browser DevTools Network panel
- **No accent or campaign color captured**: the palette is three neutral values; Marine Layer likely deploys seasonal accent colors (warm sage, clay, coastal blue) for campaign periods that were not present during extraction
- **No meta theme-color set**: the brand does not appear to declare a theme-color meta tag, so mobile status-bar and browser chrome color cannot be confirmed
- **Exact border-radius unverified**: {rounded.xs} 4px is inferred from visual inspection; actual computed values may be 0px (fully sharp) or 6px — verify in DevTools computed styles on button and card elements
- **Button height and padding**: 48px / 14px 24px are DTC apparel defaults; confirm against computed styles since Shopify themes sometimes override these at the theme-settings level
- **Sale accent color**: no red or secondary accent appeared in extraction; if a sale-red exists in the system it was not captured and `{colors.ink}` is used as a conservative fallback for sale pricing
- **Re-Spun badge placement rules**: product-detail-only placement is inferred from common DTC pattern; some templates may surface the badge on the grid card as well
- **Promo banner persistence**: unknown whether dismissal is session-scoped, cookie-controlled with TTL, or always-visible on each page load
