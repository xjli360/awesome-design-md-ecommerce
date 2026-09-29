---
version: alpha
name: "Steelcase"
source_url: "https://www.steelcase.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The #003388 navy that Steelcase holds across every primary button, masthead strip, and brand lockup is not a corporate blue chosen for authority alone — it is the particular blue of a company whose clients measure workplace ROI in square footage and retention rates, and whose founding product was a steel wastebasket manufactured in 1912. Against that navy, a supporting cast of warm grays — #727a71 sage, #949494 mid-tone, #f0f0f0 canvas-light — keeps pages from reading as procurement documents. No proprietary typeface was detected in the extraction; Georgia and Arial anchor the type stack, consistent with an enterprise brand whose primary audience reads on IT-managed Windows machines where system fonts are ground truth. Display headers sit at modest weights (600 maximum), trusting institutional navy and generous whitespace to carry authority rather than heavy typographic mass. Product photography is large and environmental — workspace vignettes over isolated product shots — so product cards carry generous aspect ratios and minimal interior chrome. Primary buttons use {rounded.xs} corners, consistent with a professional-services aesthetic that signals precision over playfulness. The site architecture segments into large category hubs (Office, Education, Healthcare) before descending into deep product configurator pages; navigation is utility-first, built around megadropdown panels rather than editorial sequences. An unusual sage-gray (#727a71) appears as a secondary surface tone and category badge hue — warm enough to soften the navy-dominated palette without reading as mint or teal. Spec tables, configurator side panels, and resource download cards are signature surface types that distinguish this from any consumer furniture brand: the visual system must communicate at the enterprise RFP level, not the impulse-buy level.

colors:
  primary: "#003388"
  primary-active: "#001e5c"
  primary-disabled: "#99aac4"
  ink: "#0f0f0f"
  body: "#272725"
  muted: "#727a71"
  hairline: "#aaaaaa"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  surface-dark: "#1e1f26"
  charcoal: "#32373c"
  mid-gray: "#949494"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  eyebrow:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25px
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
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
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.mid-gray}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xl} {spacing.section}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    imagePaddingBottom: "66.67%"
    padding: "{spacing.base}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.08)"
  category-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    displayTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xxl}"
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    displayTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xxl}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.mid-gray}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    height: 44px
    iconColor: "{colors.primary}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.charcoal}"
    headerTypography: "{typography.spec-label}"
    rowTextColor: "{colors.body}"
    rowTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline-soft}"
    rowAltBackgroundColor: "{colors.surface-soft}"
  configurator-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    bodyTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline-soft}"
    sectionBorderTop: "2px solid {colors.primary}"
    padding: "{spacing.lg}"
  resource-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    eyebrowColor: "{colors.muted}"
    eyebrowTypography: "{typography.eyebrow}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  segment-tab:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "{colors.canvas}"
    inactiveTextColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: "8px 20px"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.section} {spacing.xxl}"

## Components

### Buttons
**`button-primary`** — Deep #003388 navy fill with white type at {typography.button-md} (Arial 15px/600), {rounded.xs} corners, 44px height, and 24px horizontal padding. Hover darkens to `primary-active` (#001e5c); disabled fades to a desaturated #99aac4 that preserves the shape without implying interactivity. The 4px corner sharpness reads as institutional precision and consistently appears across every primary CTA: "Request a Quote," "Shop Now," "Contact a Dealer."

**`button-secondary`** — White fill with primary-navy text and a 2px navy border, same height and radius as `button-primary`. Used for secondary actions (e.g., "Learn More" beside a primary "Request a Quote") where the pair must share equal visual weight but maintain a clear hierarchy.

**`button-ghost`** — Transparent fill, 1px hairline border, primary-navy text. Appears in table rows, configurator steps, and product-card footers where a filled button would overload the surface density.

**`button-dark`** — #1e1f26 fill with white text for CTAs placed over dark hero banners or the footer. Shares radius and padding with `button-primary` to keep the action footprint consistent across light and dark contexts.

### Text Input
**`text-input`** — 44px field with 1px hairline border, {rounded.xs}, and Arial body type. Focus ring upgrades to 2px primary-navy without shifting field dimensions. Placeholder renders in {colors.mid-gray} (#949494). Used across site search, dealer-locator zip fields, and RFQ form pages.

### Navigation
**`nav-bar`** — 72px tall on a white canvas with a 1px hairline-soft bottom divider. Links use {typography.nav-link} (Arial 14px/600). The Steelcase wordmark anchors the left; segment selectors (Office, Education, Healthcare) occupy the center region; utility icons (search, account, region) sit right-aligned. `nav-bar-dark` swaps background to #1e1f26 with white link text for campaign pages.

**`mega-menu`** — Full-width dropdown anchored by a 3px primary-navy top edge and a subtle box shadow. Interior sections are organized by product family with {typography.eyebrow} section headers and small product thumbnails. Navigation is purely utilitarian — no lifestyle photography, no editorial copy in the dropdown panel itself.

### Product Card
**`product-card`** — Zero border-radius ({rounded.none}), 1px hairline-soft border, 2:3 landscape image aspect ratio. Product name in {typography.title-sm}, descriptor in {typography.body-sm}. Hover lifts box-shadow to 0 4px 16px rgba(0,0,0,0.08) and thickens the border to {colors.hairline}. Category badges ({typography.eyebrow} labels on {colors.surface-soft} chips) appear in the image upper-left corner. No rounded corners anywhere on the card signals that this is a professional catalog grid, not a consumer shop.

### Hero
**`hero-banner`** — Full-bleed dark (#1e1f26) environmental hero with Georgia display type ({typography.display-xl}, 48px), white body text, and 560px minimum height. Large workspace photography fills the frame behind a left-aligned text column. `hero-banner-light` swaps to {colors.surface-soft} (#f0f0f0) with ink text — used on category landing pages that open directly into a product grid rather than a lifestyle vignette.

### Search
**`search-bar`** — 44px input, {rounded.xs}, primary-navy magnifier icon. At focus, border thickens to 2px primary. Nested in the nav utility cluster; on mobile it expands to a full-bleed overlay with a visible close target.

### Spec Table
**`spec-table`** — The signature B2B data surface. Header row uses {colors.surface-soft} fill with {typography.spec-label} (Arial 13px/600, {colors.charcoal}). Data rows alternate between white and {colors.surface-soft} for scannability across dense attribute sets. All borders use {colors.hairline-soft}. Columns map to enterprise-purchasing attributes: Dimensions, Finish Options, Weight Capacity, Lead Time, Certifications.

### Configurator Panel
**`configurator-panel`** — Sticky right-side panel on product detail pages. A 2px primary-navy top border delineates the active configuration section from the page chrome. Option labels use {typography.spec-label}; descriptive copy uses {typography.body-sm}. Configuration sections stack vertically separated by {colors.hairline-soft} dividers; the summary CTA ("Add to Quote") is always a `button-primary` pinned to the panel bottom.

### Resource Card
**`resource-card`** — Used for case studies, whitepapers, and planning guides. Eyebrow in {typography.eyebrow} at {colors.muted} sage. Title in {typography.title-md}, body excerpt in {typography.body-sm}. Hard corners ({rounded.none}), 1px hairline-soft border. A ghost-style download button sits at the card bottom-right. Cards appear in three-column grids on the Resources hub and as related-content rows at the bottom of product pages.

### Segment Tabs
**`segment-tab`** — Hard-edged toggles ({rounded.none}) that switch between Office, Education, and Healthcare product views. Active state is navy fill with white type; inactive is white with navy border and navy text — no visual ambiguity about which segment is selected. Uses {typography.button-sm}. On mobile, the tab row becomes full-width with each tab at 48px height.

### Footer
**`footer`** — #1e1f26 dark surface with a 3px primary-navy top border mirroring the mega-menu accent. Column headings in {typography.title-sm} (white), links in {typography.body-sm} at reduced opacity. Bottom bar carries legal links, social icons, region/language selectors, and certification logos (BIFMA, GREENGUARD). Padding mirrors the hero sections at {spacing.section} horizontally.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger drawer replaces mega-menu; search expands full-bleed overlay; single-column product grid; hero min-height drops to 360px; display type steps down from 48px to 28px; segment tabs become full-width row |
| Tablet | 744–1128px | Two-column product grid; nav retains top bar but mega-menu becomes scrollable overlay panel; configurator panel collapses to bottom-sheet drawer; resource cards in two-column grid |
| Desktop | 1128–1440px | Three- to four-column product grid; full mega-menu at viewport width; configurator panel sticky at 320px fixed width; spec tables render all columns |
| Wide | > 1440px | Content container caps at 1440px centered; product grids hold at four columns; hero imagery edge-to-edge while text block centers within the max-width container |

### Touch Targets
- All interactive controls minimum 44×44px on touch viewports
- Segment tabs expand to full-width row with 48px height on mobile
- Nav utility icons (search, account, region) carry 44px hit areas despite 24px visual glyphs
- Configurator option swatches minimum 44×44px with 8px gap between targets

### Collapsing Strategy
- Mega-menu collapses to an accordion list within a full-height slide-in drawer; category eyebrow headers become accordion triggers
- Spec tables scroll horizontally on mobile with row-label column pinned at 120px on the left
- Configurator panel migrates from sticky right-side column to a bottom-anchored drawer with expand/collapse handle; summary CTA remains always visible
- Resource cards collapse from three-column grid to single-column stacked list on mobile; eyebrow and body excerpt are hidden to keep card height compact
- Hero text overlay shifts from left-aligned 50% wide column to full-width bottom overlay with a dark gradient scrim behind white type

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No proprietary brand typeface detected in static extraction; Steelcase likely loads a custom sans-serif via JS or a CDN font host. Georgia and Arial are used as production-safe fallbacks but may not match the heading typeface in live production.
- Numerous extracted colors (#00d084, #0693e3, #ff9900, #1778f2, #1ea0c3, #02e49b, #e94c89, #ea4434, #f00075, #e21b24, #f45800) are attributable to WordPress Gutenberg block-editor defaults, social media embed SDKs, or third-party widgets — not Steelcase brand tokens. These have been excluded from the palette.
- `meta theme-color` absent; no declared mobile chrome accent color.
- Platform is not Shopify; the quote and purchase flow likely routes to a dealer-integrated configurator application separate from the marketing site, which was not crawled.
- Exact production button border-radius unconfirmed; {rounded.xs} (4px) is inferred from the brand's professional-services visual register.
- Hover, drawer open/close, and mega-menu transition curves were not captured; easing and duration values are unspecified.
- Product configurator 3D viewer, material swatch grid sizing, and finish-selector interaction patterns were not captured from the live tool.
- Dark-mode support status unknown; no `prefers-color-scheme` tokens were detected.
