---
version: alpha
name: "Vuori"
source_url: "https://vuoriclothing.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every primary CTA on vuoriclothing.com fires in a saturated Pacific blue (#006dff) — a single electric note against a palette otherwise built from Californian neutrals: warm near-black (#17120f), charcoal (#3e3e3e), medium gray (#727272), and a near-white canvas (#f8f8f8). The contrast is deliberate: Vuori sells the idea that performance and everyday life share the same garment, and the blue CTA is where that proposition becomes a transaction. AktivGrotesk carries the entire type system — a geometric grotesque with even strokes and open apertures that reads effortlessly at both the 12px caption scale and the 48px hero headline. Weight does the work of variation; the face never needs italic or condensed cuts to assert hierarchy. Product cards float on a surface-soft layer (#f8f8f8) with a minimal 4px radius, keeping the aesthetic closer to a design studio's lookbook than a sporting-goods catalog. Secondary accents — sky blue (#a4def9), ocean (#29a8e0), amber (#faaf43), lemon (#f8eb30), navy (#336799) — surface as product color swatches and limited editorial moments rather than structural UI chrome, preserving the neutral foundation. Sale pricing and error states run in a distinct red (#d02e2e), which reads clearly against both the light canvas and the charcoal body text. Navigation is flat and label-driven, relying on AktivGrotesk at medium weight and a generous top-bar height rather than icons or mega-menu theatrics. The overall effect is a site that feels like a well-lit Encinitas showroom: unhurried, airy, and willing to let product photography carry the persuasion while the blue button closes the sale.

colors:
  primary: "#006dff"
  primary-active: "#0056cc"
  primary-disabled: "#a4def9"
  ink: "#17120f"
  body: "#3e3e3e"
  muted: "#727272"
  hairline: "#c6c6c6"
  hairline-soft: "#ededed"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  surface-mid: "#ededed"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale: "#d02e2e"
  accent-sky: "#a4def9"
  accent-ocean: "#29a8e0"
  accent-amber: "#faaf43"
  accent-yellow: "#f8eb30"
  accent-navy: "#336799"

typography:
  display-xl:
    fontFamily: "'AktivGrotesk', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'AktivGrotesk', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'AktivGrotesk', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'AktivGrotesk', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'AktivGrotesk', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.6px
    textTransform: uppercase
  body-md:
    fontFamily: "'AktivGrotesk', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'AktivGrotesk', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'AktivGrotesk', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-xs:
    fontFamily: "'AktivGrotesk', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  price-md:
    fontFamily: "'AktivGrotesk', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'AktivGrotesk', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'AktivGrotesk', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'AktivGrotesk', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
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
    padding: 14px 28px
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
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
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
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-announcement:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-md}"
    swatchSize: 16px
    padding: "{spacing.md}"
  product-card-sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-xs}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  product-card-new-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-xs}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    headlineColor: "{colors.on-dark}"
    overlayColor: "rgba(23,18,15,0.25)"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 600px
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.ink}"
    borderInactive: "1px solid {colors.hairline}"
    disabledOpacity: 0.4
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.ink}"
    disabledTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    iconColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
  category-pill:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  category-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  price-display:
    regularColor: "{colors.ink}"
    saleColor: "{colors.sale}"
    originalColor: "{colors.muted}"
    typography: "{typography.price-md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Solid Pacific blue (#006dff) fill, white label in AktivGrotesk 600 at 15px, 4px radius, 48px tall. Hover transitions to `{colors.primary-active}` (#0056cc) in 150ms; disabled state uses the sky-wash `{colors.primary-disabled}` (#a4def9). Applied exclusively to primary purchase actions: "Add to Cart," "Shop Now," "Checkout."

**`button-secondary`** — White fill with a 1px `{colors.ink}` border, identical height and typography to `button-primary` so the two can sit side-by-side in hero CTA rows without vertical misalignment. Hover state darkens border to full black and adds a subtle ink background at 4% opacity.

**`button-ghost`** — Transparent background, underlined ink label at button-md weight. No border, no shadow. Used for low-priority actions: "See All," breadcrumb navigation, and filter resets where a full button would overweight the page.

### Text Input
**`text-input`** — White canvas fill, 1px `{colors.hairline}` (#c6c6c6) border stepping up to `{colors.ink}` on focus, 4px radius matching button geometry. 48px height keeps touch targets consistent with primary buttons. Placeholder runs `{colors.muted}` (#727272); error state swaps border to `{colors.sale}` (#d02e2e).

### Navigation
**`nav-bar`** — White 64px bar with a soft #ededed bottom rule. Logo anchors left at approximately 120×24px; top-level category links in nav-link (14px, weight 500) run center-spaced. Cart and account icons right-align at 24×24px with 44px touch padding. The `nav-bar-announcement` strip pins above in full `{colors.ink}` with white caption-scale text cycling free shipping thresholds and seasonal promos.

### Product Card
**`product-card`** — Portrait 3:4 image fills the card top flush; the card container carries a 4px radius but the image corners are clipped to match. Color swatches sit beneath the image in 16px `{rounded.full}` circles — active swatch gets a 2px ink ring with a 2px white gap via box-shadow. Product name in title-sm (uppercase, 0.6px tracking, 600 weight) and price in price-md (16px, 500 weight). Sale price in `{colors.sale}` (#d02e2e) with the original struck through in `{colors.muted}`.

**`product-card-sale-badge`** — Sharp-cornered (#rounded.none) red chip overlaying the top-left of the card image. Label-xs uppercase white text on `{colors.sale}` fill. Visible only on discounted SKUs.

**`product-card-new-badge`** — Identical geometry to sale badge; `{colors.ink}` fill with `{colors.on-dark}` text. Applied to new-arrival items in the first few weeks of a drop window.

### Hero Banner
**`hero-banner`** — Full-bleed photography with a 25% dark scrim overlay (rgba of #17120f). Headline in display-xl (700, -0.5px tracking) renders white over imagery. On lighter editorial images the overlay increases to 40% for contrast compliance. Subhead in body-md at 400 weight, max-width 560px. CTA uses `button-primary` anchored bottom-left on split layouts, centered on full-bleed editorial. Minimum 600px tall on desktop; scales to 360px on mobile.

### Color Swatch
**`color-swatch`** — 20px circles with `{rounded.full}`. Inactive: 1px `{colors.hairline}` ring. Active: 2px `{colors.ink}` ring with 2px white gap (box-shadow technique for gap). Sold-out swatches render at 40% opacity with a diagonal CSS line.

### Size Selector
**`size-selector`** — Rectangular chip, 4px radius, 1px `{colors.hairline}` border at rest. Selected: border upgrades to 1px `{colors.ink}`. Out-of-stock: text in `{colors.muted}` with a diagonal strike line. Body-sm typography for legibility across XS–3XL range.

### Search
**`search-bar`** — Activates as an expanding overlay from the nav magnifier icon. Surface-soft (#f8f8f8) background, 4px radius, muted placeholder text, magnifier icon in `{colors.muted}`. As the user types, results populate beneath as a flat list: 48×64px product thumbnail, name in title-sm, price in price-md. No autocomplete dropdown — straight to product results.

### Category Pills
**`category-pill`** / **`category-pill-active`** — Pill-shaped filter chips (`{rounded.full}`) lining collection page tops. Inactive: surface-mid (#ededed) fill, ink text in button-sm. Active: ink fill, white text in button-sm. Background-color transition 150ms ease. On mobile the pill row scrolls horizontally without wrapping.

### Price Display
**`price-display`** — Regular price in `{colors.ink}`, sale price in `{colors.sale}` (#d02e2e) preceding the original struck through in `{colors.muted}`. All at price-md (16px, weight 500) for visual balance with the title-sm product name above.

### Footer
**`footer`** — Full-width `{colors.ink}` (#17120f) block closing the page. Column headings in title-sm (uppercase, 600 weight, 0.6px tracking) in white. Body links in body-sm at `{colors.hairline}` (#c6c6c6) tone. Social icons 20×20px in white at `{spacing.lg}` spacing. Newsletter input runs inline with a ghost underline submit label. Four columns collapse gracefully; the dark mass anchors the otherwise light-canvas experience with deliberate visual weight.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo + cart icon; hero min-height 360px; announcement bar truncates to one line with no dismiss button |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level labels only with no flyout; hero 480px tall; category pill row appears above grid |
| Desktop | 1128–1440px | Three-column product grid; full nav with flyout mega-menus on hover; hero 600px; nav becomes sticky after 80px scroll |
| Wide | > 1440px | Four-column product grid; max content width 1440px centered with auto side margins; hero image scales to fill but headline max-width caps at 680px |

### Touch Targets
- All buttons, size chips, and swatches minimum 44×44px on mobile
- Nav icons (cart, account, hamburger) padded to 44px touch target regardless of glyph size
- Color swatch circles expand to 24px on mobile for easier selection
- Announcement bar includes a 44px-tall dismiss region if a close control is present

### Collapsing Strategy
- Mega-nav flyout collapses to accordion-style drawer in a full-height side sheet on tablet and below
- Three-column editorial feature blocks stack full-width vertically on mobile
- Footer four-column layout collapses to two columns on tablet, single column on mobile
- Collection filter/sort bar collapses to a bottom-sheet modal on mobile; active filter count shown in the trigger chip
- Product image gallery switches from horizontal-scroll thumbnail strip to swipe carousel with dot indicators on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Button border-radius may be 0px (fully squared) rather than 4px — extraction shows near-zero rounding on most interactive elements; 4px used as a conservative estimate
- AktivGrotesk weight naming conventions not confirmed from extraction; 400/500/600/700 inferred from standard grotesque-family practices
- Exact mega-menu layout (column count, featured imagery placement, hover behavior) not derivable from static extraction
- Hover color for nav links (underline vs. tint shift) not confirmed
- Announcement bar background color likely varies by promotion; `{colors.ink}` used as fallback
- Klarna Headline detected in font stacks but belongs to the Klarna payment widget, not Vuori's own type system — excluded from design tokens
- Structural role of accent colors (#faaf43, #f8eb30, #a4def9, #29a8e0, #336799) unconfirmed beyond product swatch contexts
- Grid gutter widths and exact card padding rhythm not confirmed from extraction
