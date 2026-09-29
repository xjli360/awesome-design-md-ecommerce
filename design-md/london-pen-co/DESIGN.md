---
version: alpha
name: "London Pen Co."
source_url: "https://www.londonpenco.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Ink-pool navy (#112233) forms the brand's gravitational center — a blue so dark it reads as black until placed beside the slightly warmer near-blacks (#272727, #111111) that carry body type, revealing the cool depth underneath. London Pen Co. mounts Rubik as its primary typeface: a geometric sans-serif with subtly softened terminals that keeps the all-dark palette from reading as corporate severity. The red-family secondaries (#cc3b3b, #bd0000) function as punctuation rather than identity — CTA buttons, sale badges, price highlights — evoking the lacquered barrel of a classic British pen without literal illustration or heritage cliché. A dusty rose tone (#e99292) softens error and discount states, giving the alert palette warmth rather than alarm. The near-white canvas (#fafafa) and soft surfaces (#fbfbfb, #eeeeee) create just enough lift beneath dark typographic elements without the clinical brightness of pure white.

  Buttons carry virtually no rounding ({rounded.xs}), their squared silhouette echoing ruled lines and nib geometry rather than the pill shapes that signal app-era softness. Navigation stays lean — dark text on light canvas, no mega-menu excess — communicating a focused SKU range where pen type, nib grade, and ink color are the meaningful filters. Product cards sit on {colors.surface-card} with a {rounded.sm} edge, a thin {colors.hairline} border, and price rendered in {colors.accent} on sale, signaling markdown without shouting. The spacing system stays compressed at the component level ({spacing.sm}, {spacing.md}) and opens only at section breaks ({spacing.section}, {spacing.xxl}), giving the catalog a grid-book density appropriate to a product line measured in millimeters. The overall result is a storefront built for precision craft: spare, direct, weighted by color rather than ornament — the palette of a well-stocked writing desk, rendered in pixels.

colors:
  primary: "#112233"
  primary-active: "#112255"
  primary-disabled: "#667788"
  accent: "#cc3b3b"
  accent-strong: "#bd0000"
  accent-soft: "#e99292"
  ink: "#111111"
  body: "#272727"
  muted: "#aaaaaa"
  hairline: "#e1e1e1"
  hairline-soft: "#eeeeee"
  canvas: "#fafafa"
  surface-soft: "#fbfbfb"
  surface-card: "#ffffff"
  on-primary: "#fafafa"
  on-accent: "#fafafa"
  scrim: "#040404"

typography:
  display-xl:
    fontFamily: "'Rubik', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Rubik', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Rubik', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Rubik', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Rubik', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Rubik', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Rubik', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Rubik', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Rubik', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Rubik', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  product-name:
    fontFamily: "'Rubik', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  price-display:
    fontFamily: "'Rubik', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Rubik', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  label-xs:
    fontFamily: "'Rubik', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.4px

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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1.5px solid {colors.primary}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-accent-active:
    backgroundColor: "{colors.accent-strong}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  nav-bar-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    imageAspectRatio: "1:1"
    titleTypography: "{typography.product-name}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
  product-card-sale:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    priceColor: "{colors.accent}"
    strikethroughColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"
  sale-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  ink-swatch:
    shape: "{rounded.full}"
    size: 28px
    border: "1.5px solid {colors.hairline}"
    borderSelected: "2px solid {colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    gap: "{spacing.xs}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 9px 14px
    height: 40px
  price-tag:
    normalColor: "{colors.ink}"
    saleColor: "{colors.accent}"
    strikethroughColor: "{colors.muted}"
    typography: "{typography.price-display}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"

## Components

### Buttons

**`button-primary`** — Filled navy ({colors.primary}, #112233) with near-white text, all-caps Rubik at 14px with 0.8px letter-spacing, and near-zero rounding ({rounded.xs}, 2px). The hard-cornered silhouette reads as a ruled edge rather than a soft consumer shape. Hover state shifts to {colors.primary-active} (#112255); disabled desaturates to {colors.primary-disabled} without opacity tricks.

**`button-secondary`** — Transparent fill with a 1.5px {colors.primary} border and matching text; same height and typography as the primary. Used for secondary CTAs — wishlist, compare, filter toggles — where the navy fill would dominate. Mirrors the primary's square corners so both buttons sit at the same visual weight in paired layouts.

**`button-accent`** — Filled {colors.accent} (#cc3b3b) reserved for sale, urgency, or campaign CTAs. Hover deepens to {colors.accent-strong} (#bd0000). Never used as a default navigation element; appears only where promotional pressure is deliberate, most visibly inside the `hero-banner` component where red against deep navy maximizes contrast.

### Navigation

**`nav-bar`** — Light {colors.canvas} background on standard pages with a single 1px {colors.hairline} base rule. Logo renders in {colors.primary}. Links use {typography.nav-link} at weight 500 — legible but not heavy. The `nav-bar-dark` variant inverts to a full {colors.primary} fill with {colors.on-primary} text for hero-adjacent or campaign pages, allowing the navigation to dissolve into the header band rather than interrupt it.

### Product Card

**`product-card`** — White {colors.surface-card} with a thin {colors.hairline} border and {rounded.sm} (4px) corners — structural rather than decorative. Product name in {typography.product-name} (Rubik 500, 16px), subtitle line in {typography.caption} for nib size or material spec, price in {typography.price-display} at weight 600. The `product-card-sale` variant switches the current price to {colors.accent} and renders the original in struck-through {colors.muted}, signaling discount without a visual alarm.

### Hero Banner

**`hero-banner`** — Full navy fill ({colors.primary}) with white headline at {typography.display-xl} and supporting copy at {typography.body-md}. The CTA inside should use `button-accent` (red on navy) for maximum contrast — the one layout context where the accent button appears against a dark field rather than a light one. Vertical padding at {spacing.xxl} gives the headline breathing room without requiring imagery to fill the frame.

### Ink Swatch Selector

**`ink-swatch`** — Circular ({rounded.full}) 28px color dots for pen ink variant selection, the component most native to this product category. Unselected state carries a thin {colors.hairline} ring; selected state upgrades to a 2px solid {colors.primary} ring with no label text required — the color dot is self-describing. Hit area expands to 44px via invisible padding to meet touch targets without inflating the visual dot size.

### Badges

**`sale-badge`** — Hard-cornered ({rounded.xs}) block in {colors.accent} with all-caps Rubik at 10px and 1px letter-spacing, positioned top-left on product card imagery. **`new-badge`** uses identical geometry in {colors.primary} navy. Both sit flush to the card image edge, sized to be legible at a glance without obscuring product photography.

### Search

**`search-bar`** — Soft {colors.surface-soft} fill with a {colors.hairline} border and muted placeholder text in {colors.muted}. On focus, the border upgrades to {colors.primary} with no glow or shadow addition. Corners at {rounded.xs} match all other input elements. On mobile, collapses to an icon-only trigger that expands to a full-width overlay bar.

### Price Tag

**`price-tag`** — Normal price in {colors.ink}, sale price in {colors.accent}, original price with strikethrough in {colors.muted}. All states use {typography.price-display} (Rubik 600, 20px) — heavier than body but not display-scale, keeping pricing prominent without dominating product name hierarchy.

### Footer

**`footer`** — Full {colors.primary} navy panel mirroring the hero, forming a dark bookend around the light catalog body. Link text in {colors.accent-soft} (#e99292), the dusty rose that holds adequate contrast against navy without defaulting to white. Column headings in {typography.title-sm} at weight 500; body links in {typography.body-sm}. Padding at {spacing.xxl} vertical matches the hero generosity.

### Collection Header

**`collection-header`** — Pale {colors.surface-soft} band with headline in {typography.display-md} (Rubik 600, 32px) and a 1px {colors.hairline} base rule separating it from the product grid. Used at the top of category pages to orient the user without the full weight of the navy hero.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero headline drops to {typography.display-md}; ink swatches stack below product image; section padding compresses to {spacing.base} |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + condensed links + icons; hero remains full-bleed; filter sidebar collapses to top filter bar |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav-bar with all links visible; hero at full {typography.display-xl}; sidebar filters exposed |
| Wide | > 1440px | Max content width capped (~1320px) with canvas margins; product grid stays at four columns; hero background extends edge-to-edge behind contained content |

### Touch Targets
- All interactive elements minimum 44×44px on mobile (buttons, ink swatches, nav icons)
- Ink swatch dots expand hit area to 44px via invisible padding; visual dot stays 28px
- Cart, search, and hamburger icons in the nav-bar each maintain 44px tap targets
- Pagination controls minimum 44px height on mobile even if visually smaller

### Collapsing Strategy
- Navigation: full link row → icon strip + hamburger menu (below 744px)
- Filters: left sidebar → horizontal-scroll pill toggles pinned below nav (below 1128px)
- Hero CTA layout: side-by-side primary + secondary → single full-width accent button (below 744px)
- Product grid: 4 col → 3 col → 2 col → 1 col as breakpoints decrease
- Footer columns: 4 col → 2 col → 1-col stacked accordion (below 744px)
- Collection header headline: {typography.display-md} → {typography.title-md} on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No `meta theme-color` was detected; mobile browser chrome color is unknown — assume {colors.primary} (#112233) for consistency with the `nav-bar-dark` variant
- Font weight range in use is unconfirmed; Rubik supports 300–900 but only weights 400, 500, and 600–700 are specified here based on visual inference from category conventions
- No explicit border-radius values were extractable from the live site; {rounded.xs} (2px) and {rounded.sm} (4px) are inferred from brand positioning rather than measured pixel values
- Hover transition durations (fade speed on buttons, card lift on hover) could not be extracted
- Mobile navigation pattern (side drawer vs. full-screen overlay vs. drop-sheet) is unconfirmed
- Whether the site uses a sticky nav on scroll or a return-to-top anchor is unknown
- Secondary or editorial typeface (if any; e.g., a serif for blog or brand-story pages) is not evidenced in the font-stack extraction — only Rubik and system sans-serif fallbacks were detected
- Exact grid gutter and column count for the product listing page could not be confirmed from extraction
