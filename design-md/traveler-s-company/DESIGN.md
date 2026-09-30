---
version: alpha
name: "Traveler's Company"
source_url: "https://www.travelers-company.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Worn leather in #382110 arrives before the headline — this is a brand that treats its primary color as a material sample rather than a branding decision, the same shade as the flagship notebook cover after six months of daily use. Type is set exclusively in serif stacks with no custom web font loading detected, an unusual restraint for an e-commerce site that makes every product name and editorial paragraph read like text stamped into paper rather than rendered on glass. The navigation header runs full bilingual identity — "TRAVELER'S COMPANY" and "トラベラーズカンパニー" — as a composed visual object rather than a localization footnote, the double-line title as structurally load-bearing as a product photograph. Product photography operates without overlaid text or gradient scrims; leather texture, visible stitching, and ink-bleed on insert pages carry all persuasive weight. The extracted palette orbits a warm analog register: #382110 leather brown as the primary voltage, near-black at #1e1f26, and a family of grays from #e1e1e1 to #f0f0f0 that approximate the color of aged cream paper. Several Gutenberg-editor and social-embed blues (#0693e3, #1778f2, #003399, #0757fe) appear in the extraction and trace to WordPress block editor defaults and embedded widgets rather than brand surfaces — those are excluded from component definitions. Corner radii stay at {rounded.none} on editorial containers and at most {rounded.xs} on interactive elements; no pill-shaped CTAs, no soft rounded-full affordances appear anywhere. The refillable leather cover is a system of components rather than a single SKU — the site dedicates structured diagram panels to making that system legible, a content type with no direct analogue in conventional DTC product pages. The interaction model reads closer to a craft atelier than a growth-optimized DTC storefront: sparse product grids, generous negative space, long-form founder-voice copy sections, and no urgency mechanics.

colors:
  primary: "#382110"
  primary-active: "#1e0e06"
  primary-disabled: "#9b7a62"
  ink: "#1e1f26"
  body: "#32373c"
  muted: "#949494"
  muted-soft: "#aaaaaa"
  hairline: "#e1e1e1"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  dark-bg: "#24292d"
  accent-blue: "#2098d1"

typography:
  display-xl:
    fontFamily: "serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.02em
  display-md:
    fontFamily: "serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  display-sm:
    fontFamily: "serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  title-md:
    fontFamily: "serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.05em
    textTransform: uppercase
  title-sm:
    fontFamily: "serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.10em
    textTransform: uppercase
  body-md:
    fontFamily: "serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0
  body-sm:
    fontFamily: "serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0
  caption:
    fontFamily: "serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  caption-bilingual:
    fontFamily: "serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.02em
  button-md:
    fontFamily: "serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.10em
    textTransform: uppercase
  button-sm:
    fontFamily: "serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.10em
    textTransform: uppercase
  nav-link:
    fontFamily: "serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.06em
  product-name:
    fontFamily: "serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  logo-display:
    fontFamily: "serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.15em
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
    padding: 12px 32px
    height: 44px
    border: none
  button-primary-hover:
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
    padding: 11px 31px
    height: 44px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: "10px {spacing.base}"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-logo:
    primaryTypography: "{typography.logo-display}"
    primaryColor: "{colors.ink}"
    secondaryTypography: "{typography.caption-bilingual}"
    secondaryColor: "{colors.muted}"
    gap: "{spacing.xs}"
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    productNameTypography: "{typography.product-name}"
    productNameColor: "{colors.ink}"
    priceTypography: "{typography.body-sm}"
    priceColor: "{colors.body}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    padding: "{spacing.sm}"
    gap: "{spacing.sm}"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    imageLayout: full-bleed
    maxWidth: 1440px
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    subtitleTypography: "{typography.body-sm}"
    subtitleColor: "{colors.muted}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.xl}"
    textAlign: center
  story-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    maxWidth: 720px
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
    imagePosition: alternating
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: "3px {spacing.sm}"
  product-badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: "3px {spacing.sm}"
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    borderSelected: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.body}"
    iconColor: "{colors.muted}"
    height: 40px
    padding: "8px {spacing.base}"
  refill-diagram:
    backgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    accentColor: "{colors.primary}"
    padding: "{spacing.xxl}"
  language-switcher:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separator: "|"
    gap: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.muted-soft}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"

## Components

### Buttons

**`button-primary`** — A flat #382110 rectangle with no border radius, uppercase spaced serif labels at 13px with 0.10em tracking. The hover state darkens to #1e0e06, reading less like a rollover highlight and more like pressing leather into a surface. Disabled state washes to #9b7a62 without changing shape. Padding is generous at 12px 32px to give the spaced serif caps room to breathe.

**`button-secondary`** — White fill enclosed by a 1px #1e1f26 border with matching uppercase serif type. Hover shifts fill to #f0f0f0 surface-soft without animating the border, maintaining the austere register. Matches the primary at 44px height so paired button groups align without adjustment.

**`button-ghost`** — Transparent background with a 1px #e1e1e1 hairline border, used for secondary filters, supplementary navigation actions, and pagination. Type scales down to 11px button-sm. Border alone shifts on hover — no fill introduced. Consistent with the brand's avoidance of color emphasis on secondary interactions.

### Form Inputs

**`text-input`** — Square-cornered fields with a 1px #e1e1e1 hairline border that upgrades to #1e1f26 on focus. Serif 16px body type inside; placeholder in #949494. No floating label animation, no border radius. Height 44px aligns with button rows in checkout and search bar contexts.

### Navigation

**`nav-bar`** — 60px tall, #ffffff canvas background with a 1px #e1e1e1 bottom border. The brand identity renders as a stacked bilingual block via `nav-bar-logo`: roman uppercase "TRAVELER'S COMPANY" in 14px logo-display with 0.15em tracking, and beneath it the Japanese name in 11px caption-bilingual at #949494. This double-line composition is the most distinctive navigational element on the site — it is never collapsed to a single mark. Navigation links sit at 13px serif with 0.06em tracking; no mega-menus, categories drop as compact lists.

### Product Cards

**`product-card`** — No shadow, no border, no radius. Product imagery in a 3:4 portrait aspect ratio (the natural proportion of a vertical notebook). Product name in 15px product-name serif below the image, price in 14px body-sm, material or series descriptor in 12px caption at #949494. The stripped-back card relies entirely on image quality for merchandising — there are no hover zoom effects or quick-add overlays in the base specification.

### Editorial / Hero

**`hero-editorial`** — Full-bleed photography to the container edge, no gradient overlay, no text superimposed on the image. Headline copy appears below or alongside in 36px display-xl serif at weight 400 — the lightness against the large size is the brand's typographic signature. Section-scale vertical padding (64px top and bottom) enforces the negative-space discipline.

**`collection-header`** — A centered title block on a #f0f0f0 surface-soft band used as a section divider between editorial and product grid content. Collection title in 24px display-md, short descriptor in 14px body-sm at #949494. No background imagery, no decorative rules. Functions as a breathing pause between content densities.

**`story-section`** — Long-form editorial panels with a 720px max-width text column and alternating image placement (image left on even sections, right on odd). Body copy at 16px body-md with 1.7 line-height — noticeably generous for e-commerce copy, prioritizing reading rhythm over information density. These sections carry origin mythology: the founder, the first prototype, the philosophy of recording journeys.

### Product System

**`refill-diagram`** — A #f0f0f0 panel that diagrams the refill-insert system: numbered component callouts with 12px caption labels in #949494, connector lines or leader arrows in #382110 primary. This component is unique to the brand's product architecture — the leather cover is a platform for interchangeable inserts and accessories, and the diagram makes that system legible to first-time visitors. No analogous component exists in standard DTC product page templates.

**`color-swatch`** — 20px circular swatches enclosed by a 1px #e1e1e1 hairline border, upgrading to a 2px #1e1f26 ring on selection. Used on product detail pages where leather covers are offered in multiple patina colorways (camel, black, blue, olive). Gap between swatches at 4px.

**`product-badge`** — Flat #382110 rectangle with 3px 8px padding, 11px uppercase serif, no radius. Used sparingly for limited editions and collaborations. The `product-badge-new` variant uses #1e1f26 for new arrivals. Both badges sit at the top-left corner of product card images, never overlapping the subject of the photograph.

### Search & Utility

**`search-bar`** — Square-cornered input on a #f0f0f0 background with a 1px #e1e1e1 border. FontAwesome search glyph at #949494 on the left edge. Focus promotes the border to #32373c. Consistent with the site's total avoidance of pill or rounded-full search affordances.

**`language-switcher`** — Caption-scale text in #949494 with a pipe separator (EN | JA), the active language promoted to #1e1f26. Sits in the top utility bar and repeats in the footer. The dedicated switcher — rather than auto-detection only — treats the Japanese audience as co-primary rather than a regional secondary market.

### Footer

**`footer`** — Dark #24292d background with white body links at 14px and section headings in 11px uppercase serif at #aaaaaa. No top border — the dark block terminates visually without needing a rule. Columns cover product categories, care and repair, store locator, brand story, and distributor information. Language and region selectors repeat here. No newsletter capture form in the base specification.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger menu replaces horizontal nav links; hero image stacks above headline text; story sections collapse to single-column with image above copy; bilingual logo block stays but compresses line-spacing |
| Tablet | 744–1128px | Two-column product grid; navigation links visible but tighter letter-spacing; hero may crop to landscape ratio; story alternating layout becomes stacked with reduced horizontal padding; refill diagram collapses to vertical list |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with bilingual title block; full-bleed hero at natural image proportions; story sections at alternating left/right with 720px text column; refill diagram at full multi-column layout |
| Wide | > 1440px | Max-width container constrains layout; no additional grid columns added beyond four-up; hero photography scales but text blocks remain within readable measure; excess horizontal space becomes balanced negative margin |

### Touch Targets

- All buttons and nav links minimum 44px height to meet iOS and Android touch guidelines
- Color swatches display at 20px but are wrapped in minimum 36px tap-target containers
- The 60px nav bar height makes primary navigation inherently thumb-accessible
- Footer utility links (language switcher, region selector) receive minimum 32px tap zone height
- Product card tap area covers the full card surface including the image, name, and price zones

### Collapsing Strategy

- Product grid: 4-col → 3-col at 1128px → 2-col at 744px → 1-col below 744px
- Navigation: horizontal link list collapses to hamburger drawer at 744px; bilingual brand title remains visible at all breakpoints as the identity anchor
- Story sections: alternating side-by-side layout collapses to stacked (image above, text below) below 744px; max-width column constraint removed at mobile
- Refill diagram: multi-column callout grid collapses to vertically scrolling labeled list below 744px
- Hero editorial: full-bleed landscape crop at desktop; portrait crop or vertically stacked text-then-image at mobile
- Collection header: centered text block remains centered at all widths; font size steps down one scale unit at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom web font detected — the live site may load a proprietary Latin or Japanese typeface (mincho or gothic) via JS or self-hosted files not captured in CSS extraction; the `serif` generic is used throughout but the specific typeface is unknown
- Multiple extracted hex values (#0693e3, #1778f2, #003399, #0757fe, #00d084, #02e49b, #ff9900, #f45800, #e94c89, #f00075, #1ea0c3, #0461dd) are consistent with WordPress Gutenberg block editor palette defaults and embedded social widget colors (Facebook, Twitter/X button blues); these are excluded from the design system
- Meta theme-color tag is absent — browser chrome accent color on Safari iOS and Android is undefined
- Exact logo mark treatment (wordmark only, compass rose, or combined lockup) not confirmable from extraction
- Price display conventions (sale price color, strikethrough formatting, currency symbol sizing) not extractable from static hints
- Spacing scale and grid gutter values are inferred from conventions for this product category, not extracted
- Animation and transition timing values (hover durations, image crossfade behavior on product cards) not present in extraction
- Dark-mode support status unknown — no `prefers-color-scheme` media query tokens detected
