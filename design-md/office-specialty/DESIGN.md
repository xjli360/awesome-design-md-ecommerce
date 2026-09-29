---
version: alpha
name: "Office Specialty"
source_url: "https://www.officespecialty.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The GSA contract number embedded in the page title — "GSA Small Business" — announces Office Specialty's primary customer before a single product loads: this is specification-grade furniture for federal workspace buildouts and modular filing systems, sold through government procurement channels, and #116dff, an institutional cornflower blue, carries that procurement authority into every CTA, link, and active navigation state. It is the blue of government form headers and agency contracting portals, chosen for compliance and recognition rather than brand distinction. The type stack never ventures beyond Arial and Helvetica — system fonts selected for compatibility with locked-down IT environments in federal agencies and corporate facilities departments rather than for aesthetic ambition; near-black #080808 grounds all spec copy and data tables with maximum density, the visual weight of a technical product catalog built to be read, not admired.

  Steel gray #5f6360 runs beneath everything as the workhorse neutral: secondary labels, muted metadata, dimension callouts, the quiet infrastructure of a product that sells on specification rather than sensation. It reads as the color of filing cabinet drawer pulls and powder-coated bracket hardware — chosen for accuracy, not warmth. Buttons land at {rounded.sm} 4px and inputs at {rounded.xs} 2px, a sharp, nearly right-angled register that signals industrial function over consumer comfort. The layout is dense by design: product cards carry part numbers, finish codes, lead times, and ADA compliance flags alongside pricing, because the buyer is a facilities manager running a GSA quote, not a first-time browser looking for inspiration.

  A USA-made manufacturing badge and GSA contract indicator appear as trust anchors near the search field and in the header, doing the work that lifestyle photography does for consumer brands. Category tiles for modular systems, filing cabinets, seating, and accessories organize a deep SKU catalog into specifiable groups. The hero is utilitarian — product imagery against white canvas, dimension callouts, and a primary CTA in {colors.primary} blue — with no atmospheric gradients or lifestyle staging. A footer closed by a 3px {colors.primary} blue top border brings the same institutional authority the header opens with. This is a catalog built for repeat specification visits by procurement officers and facilities architects who already know what they need and want to configure it precisely.

colors:
  primary: "#116dff"
  primary-active: "#0052cc"
  primary-disabled: "#99c2ff"
  ink: "#080808"
  body: "#2c2c2c"
  muted: "#5f6360"
  muted-soft: "#8a8e8b"
  hairline: "#d8d9d8"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f4f5f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#116dff"
  link-visited: "#0052cc"
  usa-badge: "#b22234"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.28
    letterSpacing: -0.25px
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  spec-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.36
    letterSpacing: 0.6px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.2px
  breadcrumb:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
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
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 38px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    dropdownBackground: "{colors.surface-soft}"
    height: 60px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    submitButtonBackground: "{colors.primary}"
    submitButtonColor: "{colors.on-primary}"
    submitButtonTypography: "{typography.button-md}"
    height: 38px
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    partNumberTypography: "{typography.caption}"
    partNumberColor: "{colors.muted}"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.ink}"
    ctaBackground: "{colors.primary}"
    ctaColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-sm}"
    ctaRounded: "{rounded.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted}"
    ctaBackground: "{colors.primary}"
    ctaColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  gsa-contract-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  usa-made-badge:
    backgroundColor: "{colors.usa-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  category-nav-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    hoverBorder: "1px solid {colors.primary}"
    hoverTextColor: "{colors.primary}"
    padding: "{spacing.lg}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    headerColor: "{colors.muted}"
    rowTypography: "{typography.body-sm}"
    rowColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    stripeBackground: "{colors.surface-soft}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.breadcrumb}"
    separatorColor: "{colors.muted-soft}"
  product-configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-md}"
    valueColor: "{colors.ink}"
    padding: "{spacing.lg}"
    ctaBackground: "{colors.primary}"
    ctaColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.primary-disabled}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — A solid #116dff rectangle at 40px height with 4px rounding, carrying 14px bold Arial with 0.2px letter-spacing. Used for "Add to Quote," "Request Catalog," and configurator submit actions. Active state deepens to #0052cc; disabled state bleaches to #99c2ff while retaining white text, signaling an unavailable configuration option rather than an error.

**`button-secondary`** — White fill with a 1px #116dff border and matching blue text, paired alongside the primary button when two actions share equal billing — "Download Spec Sheet" vs. "Add to Quote." Shares the same 40px height and 4px rounding to sit in tight pairing without vertical imbalance.

**`button-ghost`** — Transparent background with #116dff text and no border. Reserved for lower-hierarchy inline actions within dense product grids: "See all finishes," "Compare," and "View lead time." Padding-only boundary keeps the action readable without competing with card borders.

### Navigation
**`nav-bar`** — A 60px white header with a 1px bottom hairline. Category labels ("Modular Systems," "Filing," "Seating," "Accessories") render in 14px bold Arial; dropdowns open against {colors.surface-soft} to lift off the white nav plane. A GSA contract badge and search bar anchor the right cluster; the logo anchors left with no decorative flourishes.

### Search
**`search-bar`** — A full-width 38px input with 2px rounding, a hairline border shifting to #116dff on focus, and a solid blue submit button flush to the right edge. Placeholder text renders in #5f6360. The submit button uses {colors.primary} fill with {colors.on-primary} text — effectively a contained button-primary at input height.

### Product Cards
**`product-card`** — A 1px hairline-bordered card with 4px rounding and 16px internal padding. The SKU part number renders in 12px #5f6360 above the product title; price in 18px bold ink below; an "Add to Quote" CTA button at card base. Finish codes, weight capacity, and lead-time data appear in {typography.spec-label} uppercase beneath the primary dimensions — the information density of a government procurement catalog rather than a storefront grid.

### Trust Badges
**`gsa-contract-badge`** — A compact #116dff badge with 2px rounding, uppercase 11px bold white text, reading "GSA CONTRACT." Appears in the header adjacent to the logo and at the top of product detail pages to signal procurement eligibility before the buyer scans any other copy.

**`usa-made-badge`** — Same geometry as the GSA badge but in #b22234, reading "USA MADE." Pairs with the GSA badge on qualifying product cards; appears in the hero banner as a credentialing anchor rather than a decorative element.

### Category Navigation Tiles
**`category-nav-tile`** — Surface-soft (#f4f5f7) tiles with 1px hairline borders and 4px rounding, each carrying a category icon and 15px bold label. Hover shifts the border to #116dff and the label to match — a hard, immediate response that reads as a product designed for repeat keyboard-and-click users rather than casual explorers.

### Specification Tables
**`spec-table`** — Full-width tables with a surface-soft header row carrying uppercase 11px bold attribute labels in #5f6360. Data rows render in 13px regular ink with alternating surface-soft stripes. Used for dimensions, weight ratings, finish options, ADA compliance flags, and applicable GSA contract line items. Borders are hairline throughout with no decorative rules.

### Hero
**`hero-banner`** — Surface-soft background with product photography, a 36px bold display headline, a 15px regular subhead in {colors.muted}, and a solid blue primary CTA. No gradients, overlays, or lifestyle staging — the hero reads as a product announcement panel in the register of a trade publication advertisement.

### Configurator Panel
**`product-configurator-panel`** — A surface-soft side panel with 1px hairline border and 4px rounding, used for modular system builders and finish selectors. Spec labels render in uppercase 11px bold #5f6360; selected values in 15px regular ink. The panel is a vertical stack of labeled option groups — material, finish, dimension, quantity — resolved by a primary button at the base.

### Footer
**`footer`** — Near-black (#080808) background with a 3px #116dff top border that restates brand authority at page close. Column headers in 15px bold white; body links in #99c2ff (muted blue, readable against dark without asserting primary weight); copyright, cage code, and GSA contract number in 13px regular at reduced opacity.

### Breadcrumb
**`breadcrumb`** — 12px regular Arial in {colors.muted} for ancestor nodes, shifting to {colors.ink} for the current page. Separator is a "›" character in {colors.muted-soft}. Renders below the nav bar and above the page title on all category and product detail pages — functional wayfinding for deep-catalog navigation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + search icon; search bar expands full-width; spec tables scroll horizontally with pinned first column; hero stacks image below text block; configurator panel becomes a bottom-sheet modal |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories with overflow dropdown; category tiles in 3-column grid; configurator panel collapses to a drawer triggered by a "Configure" button; badges move to below-title position |
| Desktop | 1128–1440px | Three-to-four-column product grid; full horizontal nav with category mega-menu dropdowns; configurator panel renders inline at right of product detail; hero is a two-column image-left / text-right split |
| Wide | > 1440px | Content constrained to ~1400px max-width, centered with canvas margins; product grid holds at four columns; hero image scale-clips rather than expanding |

### Touch Targets
- All buttons minimum 44px touch height on mobile — button-primary and button-secondary expand from 40px below 744px
- Category nav tiles minimum 48px height on mobile for reliable tap
- Nav dropdown items minimum 44px line-height in the mobile slide-over drawer
- Breadcrumb links padded to 32px vertical touch area on mobile
- Badge elements non-interactive; no touch-target minimum required

### Collapsing Strategy
- Top nav collapses to logo + hamburger at < 744px; mega-menu becomes a full-screen slide-over drawer with a back-navigation header
- Spec tables use horizontal scroll with a sticky first column (attribute name) on mobile rather than collapsing to a stacked definition list
- Product configurator panels become bottom-sheet modals on mobile, triggered by a sticky "Configure This Product" bar fixed at the viewport bottom on product detail pages
- Footer columns stack vertically at mobile; GSA and USA-made badge cluster moves to the top of the footer above the column grid
- Two-badge header cluster (GSA + USA MADE) compresses to icon-only at narrowest mobile widths with full text restored at ≥ 375px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only three hex values were extracted (#116dff, #5f6360, #080808); all surface, hairline, error, warning, and visited-link colors are derived from the extracted palette by lightening and darkening — none confirmed from live site inspection
- No meta theme-color was set; true mobile browser chrome tint is unconfirmable
- Font stack is entirely system fonts (Arial, Helvetica); no custom or webfont typeface was detected, but a font loaded via JavaScript or a @font-face declaration outside the static extraction window may exist
- Japanese font entries (Hiragino Kaku Gothic Pro, Meiryo) appear in the detected CSS stack — unclear whether this indicates a localized product catalog, legacy third-party widget CSS, or inherited framework defaults; no locale-specific layout or color rules could be inferred
- No brand icon set was identified; icon style (filled vs. outline, stroke weight, grid size) is unknown and not specifiable
- Hover transition timing functions and durations are not extractable from static scans; all interaction states in this spec use instantaneous color shifts
- Product photography art direction (background treatment, cropping discipline, lifestyle vs. product-only) unconfirmed
- Actual GSA contract badge artwork, cage code display format, and any official certification graphic treatments are not visually confirmed; badge specifications above are derived from brand logic
