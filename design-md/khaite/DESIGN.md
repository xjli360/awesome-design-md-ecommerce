---
version: alpha
name: "Khaite"
source_url: "https://khaite.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  ITC Galliard's ink-pooling ball terminals and Fakt Pro's sliced-circle geometry occupy the same interface without softening toward each other — that deliberate typographic standoff defines how Khaite approaches everything from product naming to navigation labels. The near-black canvas (#141414) is specifically chosen to be softer than #000000 while still reading as absolute dark; photography floats against it with none of the warmth a cream or off-white background would introduce. The brand has decided austerity is the luxury signal, and the interface enforces that conviction throughout every scroll depth.

  The accent stack is kept aggressively small. #da0000 — a traffic-signal red deployed sparingly for sale badges and alert states — is the only color that breaks the achromatic register. An amber tone (#f59e0b) appears at system-interaction moments, likely form validation or notification states, while a neutral sequence from #f8f8f8 through #555555 handles every surface, border, and secondary-text function. The light blue (#b3d4fc) reads as a Shopify-inherited focus ring rather than a brand asset. Every editorial color decision is made by subtracting, not adding.

  Corners are `{rounded.none}` everywhere: product cards, drawers, form fields, filter chips. There are no pill shapes, no architectural softening of any radius. The grid runs tight, with images cropped flush to their container edges. Navigation categories appear in Fakt Pro at tracked uppercase — small, precise, deliberately unintrusive — while campaign and lookbook moments break into ITC Galliard serifs at display scale, creating an editorial register shift from shop to magazine within a single scroll. Product cards carry only the essential signal: name, price, swatch count. The image is expected to close the sale.

  Spacing is generous at the macro level — sections breathe at `{spacing.section}` — but micro-level density is high: form elements, size selectors, and navigation items sit closer together than a soft-lifestyle brand would permit. On mobile, the horizontal nav collapses to a full-screen drawer while preserving cap-height tracking and weight unchanged, refusing to trade typographic precision for ease of tap-target compliance. The footer inverts to near-black (`{colors.primary}`) with `{colors.on-primary}` links, closing the interface on the same dark tonic note it opened with.

colors:
  primary: "#141414"
  primary-active: "#000000"
  primary-disabled: "#bebebe"
  accent-red: "#da0000"
  accent-amber: "#f59e0b"
  ink: "#141414"
  body: "#555555"
  muted: "#7f7f7f"
  muted-soft: "#bebebe"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  hairline-mid: "#dadada"
  canvas: "#f8f8f8"
  surface-soft: "#f6f6f6"
  surface-card: "#e2e2e2"
  on-primary: "#f8f8f8"
  on-dark: "#f8f8f8"
  scrim: "rgba(20,20,20,0.5)"

typography:
  display-xl:
    fontFamily: "'ITC Galliard', Georgia, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'ITC Galliard', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'ITC Galliard', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Fakt Pro', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Fakt Pro', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  body-md:
    fontFamily: "'Fakt Pro', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Fakt Pro', Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Fakt Pro', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  nav-label:
    fontFamily: "'Fakt Pro', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'Fakt Pro', Inter, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  price-tag:
    fontFamily: "'Fakt Pro', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    borderBottom: "1px solid {colors.hairline}"
    borderBottomFocus: "1px solid {colors.ink}"
    padding: "8px 0"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    imageRatio: "3:4"
    rounded: "{rounded.none}"
    productName: "{typography.body-md}"
    productPrice: "{typography.price-tag}"
    gap: "{spacing.sm}"
  hero-editorial:
    layout: full-bleed
    imageRatio: "16:9 desktop / 9:16 mobile"
    overlayHeadline: "{typography.display-xl}"
    overlayColor: "{colors.on-primary}"
    ctaStyle: button-primary
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "3px 6px"
  filter-chip:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "6px 12px"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  drawer-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    width: "100vw (mobile) / 420px (desktop)"
    rounded: "{rounded.none}"
    backdropColor: "{colors.scrim}"
  size-selector:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    disabledTextColor: "{colors.muted-soft}"
    height: 40px
    width: 40px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    activeColor: "{colors.ink}"
  quickview-overlay:
    backdropColor: "{colors.scrim}"
    panelBackground: "{colors.canvas}"
    rounded: "{rounded.none}"
    width: 480px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-primary}"
    linkHoverColor: "{colors.muted-soft}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Full-width on mobile product pages, fixed-width on desktop, set in Fakt Pro at tracked uppercase 12px. Renders at 48px height with no border-radius (`{rounded.none}`), a near-black (#141414) fill, and near-white (#f8f8f8) text. Active state deepens to true black (#000000); disabled state uses muted gray (#bebebe) fill. No hover elevation, shadow, or transform — the brand relies solely on color transition.

**`button-secondary`** — Identical dimensions to the primary but inverted: transparent fill with a 1px solid #141414 border and #141414 text. Used for secondary cart actions such as "Save to Wishlist," appearing alongside the primary CTA on product detail pages. Same tracked-uppercase Fakt Pro type, same sharp corners.

**`button-ghost`** — Inline text link with underline, no border, no fill. Fakt Pro body-sm weight. Used for editorial navigation triggers ("Explore the Collection") and filter-clear actions throughout collection pages.

### Inputs
**`text-input`** — Underline-only form fields: no box border, only a 1px bottom border in #dedede that sharpens to #141414 on focus. Placeholder text renders in #7f7f7f. The underline-only treatment enforces the brand's consistent rejection of enclosed rectangles throughout the interface — no input has a bounding box anywhere on the site.

### Navigation
**`nav-bar`** — 56px tall, #f8f8f8 background, 1px #dedede bottom hairline. Categories set in Fakt Pro at 11px, 0.12em letter-spacing, all-caps — small enough to read as a secondary signal rather than a dominant wayfinding system. Logo wordmark anchored left; cart and account icons right. No mega-menu on initial render; hover triggers a dropdown with subcategory links in the same `{typography.nav-label}` treatment.

**`drawer-nav`** — Full-screen on mobile (100vw), 420px panel on desktop, sliding in from the left over a `{colors.scrim}` backdrop. Internal category links match the nav-bar uppercase Fakt Pro; subcategory links step down to `{typography.body-sm}` with `{spacing.lg}` indentation.

### Product Display
**`product-card`** — Image-dominant at 3:4 ratio, filling its grid column flush with no container padding. Product name in Fakt Pro `{typography.body-md}` below the image; price follows in `{typography.price-tag}` weight. Color swatch count appears as `{typography.caption}` text — swatches themselves are not shown in grid view. No hover shadow or card lift; the only interaction signal is a subtle image crossfade to an alternate colorway on hover.

**`size-selector`** — Individual 40×40px square tiles, `{rounded.none}`, 1px #dedede border. Selected state fills to #141414 with #f8f8f8 text. Out-of-stock tiles retain the border but drop text to `{colors.muted-soft}` (#bebebe) with no strikethrough — scarcity is communicated by color alone, not typographic decoration.

**`sale-badge`** — Small rectangular label, #da0000 fill, white text in `{typography.caption}`, `{rounded.none}`. Anchored to the top-left corner of product card images. Never stacked with other badge types.

### Overlay & Search
**`quickview-overlay`** — Right-side panel at 480px on desktop, full-height with `{colors.scrim}` backdrop. No border-radius on the panel edge. Carries the size-selector grid, add-to-cart CTA, and primary product imagery identical to the full product detail page.

**`filter-chip`** — Flat rectangular tags for collection filtering, `{rounded.none}`, 1px `{colors.hairline}` border, `{typography.caption}` Fakt Pro. Active/selected state fills #141414 with `{colors.on-primary}` text. A `button-ghost` "Clear all" appears beside the active chip row.

### Footer
**`footer`** — Full-width near-black (#141414) block, mirroring the primary brand color. `{colors.on-primary}` body-sm text for nav links; hover state lightens to #bebebe (`{colors.muted-soft}`). Four-column link grid on desktop collapses to stacked accordions on mobile, preserving type treatments throughout.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to full-screen `drawer-nav`; hero switches to 9:16 portrait ratio; `button-primary` stretches full-width; size-selector tiles reflow to eight-across row |
| Tablet | 744–1128px | Two-column product grid; nav bar visible but condensed; hero retains 16:9 ratio; quickview panel at 380px |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with hover dropdowns; quickview panel at 480px; editorial hero at full 16:9 |
| Wide | > 1440px | Grid constrained to max-width container (~1440px centered); hero image scales with viewport but `{typography.display-xl}` headline caps at 56px |

### Touch Targets
- Size selector tiles are 40×40px — at the minimum recommended tap size; add padding to reach 44×44px in production
- Filter chips render at approximately 32px height on mobile — increase vertical padding to meet 44px tap target
- Nav icon buttons (cart, account) should carry a minimum 44×44px invisible tap area regardless of visible icon size
- Add-to-cart CTA is always 48px full-width on mobile, meeting the target comfortably

### Collapsing Strategy
- Primary nav: horizontal category labels collapse to hamburger icon at < 744px; full-screen `drawer-nav` overlays the page
- Footer columns: four-column link grid collapses to stacked accordions with disclosure chevrons on mobile
- Product grid: transitions 4-col → 3-col → 2-col → 1-col across Wide → Desktop → Tablet → Mobile
- Filter panel: sidebar on desktop folds into a modal drawer on mobile, triggered by a "Filter" `button-secondary` above the grid
- Hero headline: `{typography.display-xl}` (56px) scales to `{typography.display-md}` (36px) on mobile without switching typeface

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Pure white (#ffffff) canvas is likely present in some contexts (checkout, product detail page body) but did not appear in the extracted hex list — #f8f8f8 used as canvas approximation
- Light blue (#b3d4fc) appears in extracted colors but is almost certainly a Shopify-default browser focus ring or accessibility state; excluded from the brand palette
- Amber tones (#f59e0b, #fbbf24) are present in extraction — source is ambiguous between Tailwind CSS defaults, a notification component, and promotional banners; assigned speculatively to `accent-amber` but not wired into components pending confirmation
- Exact nav-bar height could not be confirmed from metadata; 56px is an estimate based on comparable fashion DTC sites on Shopify
- ITC Galliard font weights in use could not be confirmed from extraction — italic variant use for editorial captions also undetermined
- Whether the nav bar is sticky/fixed or scrolls away with the page could not be determined
- Swatches-in-grid vs. color-count-only display on product cards could not be confirmed from extraction
- Exact logo lockup (wordmark only vs. mark+wordmark) and any minimum clear-space rules not confirmed
- #191919, #1f1f1f, #121212, and #222222 all appear in the extracted list alongside #141414 — whether these represent distinct semantic roles (e.g., hover states, modal backgrounds) or are incidental variations across components could not be determined
