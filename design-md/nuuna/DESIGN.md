---
version: alpha
name: "Nuuna"
source_url: "https://www.nuuna.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Nuuna's notebooks are essentially printed art editions — covers rotate through photography collections, geometric collaborations, and artist partnerships, turning the product grid into something closer to a seasonal gallery than a stationery catalog. The single extracted digital signal, #313131, tells you everything about the interface intention: not pure black but a warm, ink-pulled charcoal that reads as a printing decision rather than a default value; against a white canvas it achieves the contrast of freshly pressed matter without the cold aggression of #000000, and every primary CTA, nav label, and product heading runs at this weight. The dot-grid interior — Nuuna's signature feature — translates into component design through measured spacing and grid-aligned layouts; corners stay close to square throughout, with product cards using at most {rounded.sm} (4px), signaling that the brand's investment lies in the cover photograph rather than the softness of the frame around it. Typography runs on clean system stacks since no custom typeface survived extraction; the scale is deliberately restrained, display sizes capping around 32–40px rather than reaching for hero declarations, because product photography and not headline copy is meant to stop the scroll. Add-to-cart labels and navigation run at weight 500–600 rather than 700+, keeping the voice close to an exhibition caption rather than retail broadcast. High-contrast reversals read as {colors.on-primary} on {colors.primary} — a single charcoal block covering every emphasis state without requiring a secondary accent hue. The overall effect is a site that behaves more like a printed catalog: measured, image-forward, and editorially paced through every breakpoint.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#b0b0b0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#767676"
  hairline: "#e2e2e2"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  cover-overlay: "rgba(49,49,49,0.55)"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.1px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.6px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0

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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "13px 27px"
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "10px 0px"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    textColor: "{colors.ink}"
    captionColor: "{colors.muted}"
    padding: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    overlayColor: "{colors.cover-overlay}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 560px
    layout: full-bleed-image-with-centered-overlay-text
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    paddingY: "{spacing.xxl}"
    borderBottom: "1px solid {colors.hairline}"
  edition-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline-soft}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    textColor: "{colors.ink}"
    rowPadding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.none}"
  cover-swatch-strip:
    swatchSize: 32px
    selectedBorder: "2px solid {colors.primary}"
    unselectedBorder: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    gap: "{spacing.xs}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: none
    padding: "10px 16px"
    height: 44px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.spec-label}"
    paddingY: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — A square-cornered ({rounded.none}) charcoal block (#313131) carrying white label text at 14px weight 500 with 0.5px letter-spacing. The hard edge is a deliberate signal: precision over warmth, print production over consumer softness. Hover darkens instantly to {colors.primary-active} (#1a1a1a) with no animation easing, reinforcing the printed-matter register. Disabled state drops fill to {colors.primary-disabled} and is the only moment softness enters the button vocabulary.

**`button-secondary`** — White fill contained by a 1px {colors.primary} border, identical corner treatment to the primary. Hover shifts fill to {colors.surface-soft} to suggest depth without introducing color. Appropriate for "Save to Wishlist," filter confirmations, and secondary PDP actions.

**`button-ghost`** — Transparent background, {colors.primary} text with underline, using {typography.button-sm}. Used inside spec panels and within body copy for low-hierarchy actions like "View inside pages" or "Download page samples."

### Text Input

**`text-input`** — Borderless on three sides, with a single 1px bottom {colors.hairline} rule at rest, upgrading to {colors.primary} on focus. The form field reads like a ruled page rather than a boxed input, consistent with the notebook metaphor. No border-radius ({rounded.none}). Applied across newsletter signup, checkout fields, and the search overlay.

### Navigation

**`nav-bar`** — 64px height on a {colors.canvas} ground, separated from page content by a 1px {colors.hairline} bottom rule. Logo sits left; category links (Notebooks, Collections, Collaborations, About) run center or right at {typography.nav-link} (13px, weight 500, 0.3px tracking). Cart and search appear as 24px stroke icons far right. No mega-menu; dropdowns open as a thin 1px-bordered panel on {colors.surface-soft}, listing subcategories in {typography.body-sm}.

### Product Card

**`product-card`** — Portrait-oriented 3:4 to mirror the notebook's physical proportions. Cover photography fills the image area with no UI chrome overlaid. Below: title in {typography.title-md} at weight 500, price in {typography.price-display} at weight 400, and a spec line (dot grid · A5 · 176 pages) in {typography.caption} at {colors.muted}. Corner is {rounded.xs} (2px) — nearly invisible, enough to remove aliasing on the image crop without softening the editorial stance. The edition badge ({edition-badge}) pins to the top-left corner of the image.

### Hero

**`hero`** — Full-bleed photography at minimum 560px height with a {colors.cover-overlay} scrim (rgba of #313131 at 55%) enabling white headline text in {typography.display-xl} (40px, weight 300, −0.5px tracking) to hold legibility across any cover photograph. The low weight at large size creates an editorial catalog register rather than brand shout. A `button-primary` CTA sits directly beneath the headline with no gap filler, keeping the composition tight.

### Collection Header

**`collection-header`** — White ground, collection name in {typography.display-md} (28px, weight 400) above a short editorial description in {typography.body-md}. Bottom 1px {colors.hairline} rule separates it from the product grid below. Padding {spacing.xxl} top and bottom gives the header room to breathe like a chapter opener.

### Edition Badge

**`edition-badge`** — Flush charcoal rectangle ({rounded.none}), label in {typography.spec-label} (11px, uppercase, 0.8px tracking) reversed in {colors.on-primary}. Applied at the top-left corner of product cards for "New", "Limited Edition", or season tags. The hard-cornered badge reads as a print run annotation rather than a marketing chip.

### Spec Table

**`spec-table`** — Used on the PDP to list format (A5/A6), page count, paper weight (g/m²), ruling type (dot grid), and cover type. {colors.surface-soft} background with {colors.hairline-soft} row dividers; label in {typography.spec-label} (uppercase, 11px), value in {typography.body-sm}. Zero border-radius throughout. The table echoes the product specification cards printed inside high-end stationery catalogs.

### Cover Swatch Strip

**`cover-swatch-strip`** — A horizontal row of 32×32px thumbnail crops showing available cover variants for a given notebook format. The selected swatch carries a 2px {colors.primary} border; unselected swatches use 1px {colors.hairline}. No border-radius on swatches — their corners match the notebook corner convention. Gap between swatches is {spacing.xs} (4px). On mobile the strip scrolls horizontally rather than wrapping.

### Search Bar

**`search-bar`** — {colors.surface-soft} fill, no visible border, {rounded.none}. On wider viewports it sits inline in the nav as an expandable field; on mobile it opens as a full-screen overlay. Placeholder text in {colors.muted} at {typography.body-md}. Submit triggers grid filtering in place, preserving the catalog-browsing experience without a page reload.

### Footer

**`footer`** — Full-width {colors.primary} fill with {colors.on-primary} text. Four columns on desktop: brand logo and social icons, Shop, About, Newsletter signup. Column headings in {typography.spec-label} (uppercase, 11px), links in {typography.body-sm} weight 400. The dark charcoal footer provides a firm visual close that echoes the cover-photography-forward product grid above — the same charcoal that carries every CTA also closes the page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo + cart icon; hero headline drops to {typography.display-md} (28px); spec table scrolls horizontally; cover swatch strip becomes a scrollable row; hero stacks image over text below 600px |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links without dropdowns; collection-header at reduced padding; hero maintains overlay layout at 480px min-height; footer collapses to two columns |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with hover dropdown panels; hero at 560px min-height with centered overlay text; spec table full-width on PDP |
| Wide | > 1440px | Content max-width ~1360px centered on white canvas; grid holds at four columns; hero background scales with cover-position center; no structural changes beyond centering |

### Touch Targets

- All interactive elements minimum 44×44px; primary and secondary buttons set at 48px height
- Cover swatches at 32px visual size require 6px invisible padding extension to meet 44px tap minimum
- Nav icons (search, cart, hamburger) carry 48px tap zones via padding despite 24px visual size
- Swatch strip on mobile uses momentum scrolling (-webkit-overflow-scrolling: touch) with a visible scroll fade-out on the trailing edge

### Collapsing Strategy

- Nav: hamburger at < 744px; slide-in drawer from left, full height, {colors.canvas} background, category links in {typography.title-lg}, subcategories indented in {typography.body-md}
- Product grid: 1 col → 2 col at 744px → 3 col at 1024px → 4 col at 1280px; gutter stays at {spacing.base} throughout
- Hero: stacked (image top / text + CTA bottom) below 600px; overlay layout with scrim at 600px and above
- Spec table: horizontal scroll on mobile rather than stacking rows, preserving the two-column label/value structure
- Footer: four columns → two columns at 744px → single stacked column at < 480px; newsletter input full-width at all mobile sizes

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Color palette severely under-extracted.** Only one hex value (#313131) was captured — the Nuuna site was behind a Cloudflare challenge page ("Just a moment…") that blocked full CSS token extraction. Any accent colors, warm or neutral secondaries, and seasonal palette additions are entirely inferred from brand category knowledge and should be verified against the live site before shipping.
- **No custom typeface detected.** Only system font stacks (-apple-system, BlinkMacSystemFont, Helvetica Neue, Roboto, etc.) were found. Nuuna likely uses a licensed display or text face (possibly a geometric sans or editorial serif) that loads via JS or a third-party font service not captured during extraction. Confirm against live site or brand asset kit.
- **No meta theme-color.** The Cloudflare challenge page suppressed the `<meta name="theme-color">` tag, so no canonical brand color could be confirmed via that signal.
- **Platform and CMS unknown.** Non-Shopify; the e-commerce stack, checkout flow structure, and component naming conventions are speculative. Component patterns should be adapted to whatever framework the site uses once confirmed.
- **Interactive states and motion unconfirmed.** Hover transitions, focus ring styles, animation easing, and timing values are best-practice defaults. Actual brand motion language (if any) was not extractable.
- **Cover imagery editorial split unconfirmed.** The proportion of photography-based covers versus illustrated, pattern, and typographic covers across the catalog is inferred from general brand knowledge rather than live content inventory.
