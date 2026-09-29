---
version: alpha
name: "Fatboy"
source_url: "https://www.fatboy.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Seventeen kilos of recycled EPS beads inside a double-stitched nylon shell — that is the Fatboy Original, and the Dutch irreverence behind it reads clearly in the brand's digital aesthetic: oversized headlines, unapologetic color blocks, and product photography that treats bean bags and garden lamps as objects worth serious attention. The site operates on a near-monochrome frame — #1A1A1A ink on an #FFFFFF canvas, with mid-gray neutrals handling secondary text and hairlines — that exists almost entirely to amplify the product palette, which spans forty-plus colorways per SKU. Primary brand voltage arrives in a saturated orange (#FF5500), deployed sparingly on key CTAs, hover states, and swatch selection rings — precise enough to feel designed and warm enough to remain fun. Display typography runs at heavy weights, with uppercase lockups at hero scale giving the brand the presence of a design-fair installation rather than a catalog page. Product cards sit at {rounded.sm} — corners clipped but not bubbly — reinforcing a sensibility that is playful without tipping into juvenile. The filtering system accommodates an unusually wide color dimension: shoppers sort by product colorway, which demands swatch arrays rendered as {rounded.full} circles rather than dropdown menus, each swatch carrying a selection ring that echoes the primary orange. Navigation is horizontal and category-forward, with subcategories revealed in a full-width flyout panel that relies on {spacing.section} padding to separate editorial photography from product links. Outdoor hero sections run to full viewport width — no crop, no text overlay — letting the object's physical scale do the storytelling. The footer anchors in {colors.brand-black}, inverting the page canvas, with white body text and the primary orange appearing only on link hovers, sustaining brand hierarchy to the last scroll position.

colors:
  primary: "#FF5500"
  primary-active: "#CC4400"
  primary-disabled: "#FFB899"
  ink: "#1A1A1A"
  body: "#333333"
  muted: "#777777"
  hairline: "#E5E5E5"
  hairline-soft: "#F0F0F0"
  canvas: "#FFFFFF"
  surface-soft: "#F7F7F7"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  brand-black: "#1A1A1A"

typography:
  display-xl:
    fontFamily: "'Neue Haas Grotesk', 'Haas Grotesk', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 72px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -2px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Neue Haas Grotesk', 'Haas Grotesk', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  display-md:
    fontFamily: "'Neue Haas Grotesk', 'Haas Grotesk', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  title-md:
    fontFamily: "'Neue Haas Grotesk', 'Haas Grotesk', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Neue Haas Grotesk', 'Haas Grotesk', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Neue Haas Grotesk', 'Haas Grotesk', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Neue Haas Grotesk', 'Haas Grotesk', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Neue Haas Grotesk', 'Haas Grotesk', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Neue Haas Grotesk', 'Haas Grotesk', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Neue Haas Grotesk', 'Haas Grotesk', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  overline:
    fontFamily: "'Neue Haas Grotesk', 'Haas Grotesk', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1 / 1"
    padding: "{spacing.md}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    priceTypography: "{typography.title-md}"
    border: "1px solid {colors.hairline-soft}"
  hero-fullbleed:
    width: 100vw
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.display-md}"
    subheadColor: "{colors.ink}"
    padding: "0"
    imageObjectFit: cover
    overlayOpacity: 0
  color-swatch:
    shape: "{rounded.full}"
    size: 24px
    selectedRingColor: "{colors.primary}"
    selectedRingWidth: 2px
    selectedRingOffset: 2px
    tooltipTypography: "{typography.caption}"
  product-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.overline}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "8px 16px"
    selectedBackgroundColor: "{colors.ink}"
    selectedTextColor: "{colors.canvas}"
    selectedBorderColor: "{colors.ink}"
  category-flyout:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    categoryTitleTypography: "{typography.title-md}"
    padding: "{spacing.section}"
    borderTop: "1px solid {colors.hairline}"
  footer-dark:
    backgroundColor: "{colors.brand-black}"
    textColor: "{colors.canvas}"
    bodyTypography: "{typography.body-sm}"
    linkColor: "{colors.canvas}"
    linkHoverColor: "{colors.primary}"
    headlineTypography: "{typography.title-md}"
    headlineColor: "{colors.canvas}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Sharp-cornered ({rounded.none}) orange block at 48px tall, {colors.primary} (#FF5500) fill with {colors.on-primary} uppercase label at {typography.button-md} (0.5px letter-spacing). Hover darkens the fill to {colors.primary-active} (#CC4400); disabled state uses {colors.primary-disabled} with identical geometry. The hard corner is a deliberate brand signal — no rounding softens the brand's confident rectangle.

**`button-secondary`** — Same 48px height and square-cornered geometry as the primary, {colors.canvas} fill with a 1px {colors.ink} border and dark uppercase text. Used for secondary CTAs like "Add to wishlist" or "View all colors" when a primary button is already present in the same zone.

**`button-ghost`** — Transparent, no border, {colors.ink} text with underline, {typography.button-md}. Reserved for tertiary actions in editorial copy and informational panels where a bordered button would overwhelm the layout.

### Form Inputs

**`text-input`** — Flat-cornered ({rounded.none}) 48px input with a single 1px {colors.hairline} border that transitions to {colors.ink} on focus. Placeholder text at {colors.muted}, body type at {typography.body-md}. No inner shadow or rounded treatment — the geometry stays consistent with the button system throughout.

### Navigation

**`nav-bar`** — 64px tall, fixed on scroll, {colors.canvas} background separated from page content by a bottom hairline at {colors.hairline-soft}. Fatboy wordmark logo anchors left. Primary category links sit center at {typography.nav-link} weight 500. Country selector and cart icon align right. No drop shadow on scroll — the hairline alone is the separator.

**`category-flyout`** — Full-width panel that descends from the nav-bar on category hover. {colors.canvas} background, {spacing.section} internal padding. Left column carries the category hierarchy in {typography.title-md}; right columns hold editorial lifestyle imagery alongside a featured product. No border-radius, no box shadow — the flyout top edge sits flush with the nav hairline.

### Product Components

**`product-card`** — Square 1:1 image ratio with {rounded.sm} corners on the card container and a 1px {colors.hairline-soft} border. Product name at {typography.body-sm}, price at {typography.title-md} in {colors.ink}. A color-swatch row below the name shows up to five available colorways using the `color-swatch` component; overflow is surfaced as a "+N more" label at {typography.caption}. On hover, an "Add to bag" ghost-button row fades in over the image bottom edge at 80% opacity background scrim.

**`color-swatch`** — 24px {rounded.full} circles rendered at the product's literal colorway. Selected state shows a 2px {colors.primary} ring offset 2px from the circle edge. Tooltips display the colorway name at {typography.caption} in a flat dark popover. Used in product cards, collection page filter rows, and the full-page product detail swatch selector.

**`product-badge`** — Sharp-edged label ({rounded.none}) anchored to the image top-left corner. Standard variant: {colors.ink} fill, {colors.canvas} text at {typography.overline}. New-product and launch variants use {colors.primary} fill with {colors.on-primary} text at the same {typography.overline} spec — the geometry never changes, only the fill.

**`filter-chip`** — Unselected: {colors.canvas} fill, 1px {colors.hairline} border, {colors.ink} text at {typography.button-sm}. Selected: fills to {colors.ink} with {colors.canvas} text, border matches fill. {rounded.none} keeps the filter row visually contiguous with the button family. Chips in the color-filter row swap to `color-swatch` circles rather than text chips.

### Marketing Components

**`hero-fullbleed`** — Viewport-width image block, zero internal padding. Headline overlays sit in the lower-left quadrant at {typography.display-xl} (72px, weight 800, uppercase) in either {colors.ink} or {colors.canvas} depending on image brightness — no scrim by default; content teams are expected to supply images with usable contrast zones. Subhead at {typography.display-md}, followed by a `button-primary` with {spacing.lg} top margin.

### Footer

**`footer-dark`** — Full-width block in {colors.brand-black}, inverting the page canvas. Four-column desktop layout: brand links, shop categories, support, newsletter signup. Column headers at {typography.title-md} in {colors.canvas}. Body links at {typography.body-sm}, default {colors.canvas}, hover {colors.primary}. Newsletter field uses a dark-surface variant of `text-input` with {colors.hairline} border on the dark ground. Social icons appear as 20px monochrome marks aligned baseline with the copyright {typography.caption} line.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero headline drops to {typography.display-md} (32px); filter chips become horizontal scroll track; color swatches reduce to 20px circles; hero CTA stacks below headline |
| Tablet | 744–1128px | Two-column product grid; nav stays horizontal but fewer categories visible (overflow moves to drawer); hero headline at {typography.display-lg} (48px); footer collapses to two columns |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with flyout panels active; hero at full {typography.display-xl}; footer at four columns with newsletter inline |
| Wide | > 1440px | Content constrained to 1440px max-width centered; edge-to-edge hero image persists while headline block observes max-width; additional whitespace absorbed in side gutters |

### Touch Targets

- All interactive elements minimum 44px height; nav category links padded to 44px vertical tap zone
- Color swatches padded to 36px tap target despite 24px visual diameter
- Filter chips minimum 44px height on mobile, overriding the 36px desktop height
- Cart icon and hamburger minimum 44×44px hit area with transparent padding

### Collapsing Strategy

- Navigation: full horizontal with flyout → hamburger drawer sliding from left, full-width overlay
- Category flyout replaced by accordion panels inside the hamburger drawer
- Product grid: 4-col → 3-col → 2-col → 1-col across breakpoints
- Filter bar: horizontal chip row → horizontally scrollable track on mobile (no drawer; chips remain permanently visible)
- Footer: 4-col → 2-col → stacked single column; newsletter form moves to top of footer stack on mobile
- Hero: full display-xl headline truncates at 3 lines max on mobile with ellipsis; image crops center on smaller viewports

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Palette unverified**: fatboy.com returned no extractable hex tokens (likely JS-injected design tokens or anti-bot protection). The primary orange (#FF5500) is inferred from published brand imagery and editorial usage; the exact value must be confirmed against live CSS custom properties or a Figma source file before production use.
- **Typeface unconfirmed**: No font-family stacks were captured from the page. "Neue Haas Grotesk" is a reasonable inference given the brand's Dutch design heritage and the geometric sans-serif character visible in screenshots, but has not been verified. The font name, weights, and CDN path should be confirmed and replaced.
- **Secondary accent colors**: Fatboy products exist in 40-plus colorways but site-chrome accent colors beyond the primary orange (#FF5500) are unknown. The colorway values in swatch components are product-data values, not design-system tokens, and were not captured.
- **Dark-mode palette**: No dark-mode overrides exist in this spec; the system is light-mode only. Whether Fatboy implements a dark mode at all is unconfirmed.
- **Icon system**: Product-category icons in navigation and UI controls are unspecified — line weight, corner radius, and size grid could not be extracted.
- **Animation curves**: Hover transitions for product card overlays, flyout panels, and swatch rings are unspecified; 200–300ms ease defaults are assumed throughout.
- **Exact grid gutter values**: Column counts per breakpoint are inferred from visual inspection of brand materials; exact gutter widths (likely 16–24px) should be confirmed from the live grid system.
