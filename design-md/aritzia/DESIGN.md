---
version: alpha
name: "Aritzia"
source_url: "https://aritzia.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Aritzia's digital storefront operates as a precision instrument for restraint — the extracted palette collapses to a single non-white signal, #313131, a near-charcoal positioned not at ink-black nor at neutral gray but in the measured gap between them, a zone where structural chrome and product copy absorb into full-bleed photography without competing for hierarchy. No badge burst, no promotional sticker, no color accent interrupts the product grid; instead the brand generates desire through white space and sequential exposure to its house of distinct labels — Wilfred, TNA, Sunday Best, Contoyou, Denim Forum — each surfaced through shared navigation architecture but given its own editorial register. Uppercase compressed tracking on category links and sub-brand identifiers creates a consistent voice across the header, one that reads as fashion-magazine masthead rather than retail navigation. Product cards present the garment alone at large scale, with sub-brand attribution in a small uppercase label below the image and price flush to the left — no star ratings, no review counts, no urgency timer polluting the editorial plane. Buttons are either fully dark or bare outlines, never rounded to pill shape; the brand's geometry skews toward the architectural, with sharp or nearly-sharp corners (`{rounded.none}`) on all interactive surfaces, maintaining tension between minimal-luxury apparel and functional e-commerce utility. The checkout and product-detail flows inherit this flatness, with form inputs carrying hairline `{colors.hairline}` borders and no fill tint, so the white canvas dominates every state. Typography — likely a curated expanded geometric sans-serif — uses modest weight contrasts, with display copy set at weight 400–500, preferring scale and letter-spacing over bold declarations. Responsive behavior preserves editorial hierarchy down to mobile with two-column product grids and a full-viewport drawer that exposes the house-brand taxonomy without truncation.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#b0b0b0"
  ink: "#1a1a1a"
  body: "#313131"
  muted: "#767676"
  muted-soft: "#a0a0a0"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale: "#c0392b"
  sub-brand-label: "#767676"

typography:
  display-xl:
    fontFamily: "'GT America Expanded', 'Neue Haas Grotesk', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'GT America Expanded', 'Neue Haas Grotesk', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'GT America Expanded', 'Neue Haas Grotesk', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'GT America Expanded', 'Neue Haas Grotesk', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'GT America Expanded', 'Neue Haas Grotesk', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
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
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'GT America Expanded', 'Neue Haas Grotesk', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'GT America Expanded', 'Neue Haas Grotesk', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'GT America Expanded', 'Neue Haas Grotesk', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  sub-brand:
    fontFamily: "'GT America Expanded', 'Neue Haas Grotesk', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0

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
    rounded: "{rounded.none}"
    padding: 14px 24px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 23px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
  text-input-error:
    border: "1px solid {colors.sale}"
    textColor: "{colors.sale}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 20px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    subBrandTypography: "{typography.sub-brand}"
    subBrandColor: "{colors.sub-brand-label}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    subBrandColor: "{colors.sub-brand-label}"
    subBrandTypography: "{typography.sub-brand}"
    nameTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    salePriceColor: "{colors.sale}"
    originalPriceDecoration: line-through
    originalPriceColor: "{colors.muted}"
    rounded: "{rounded.none}"
    imageGap: "{spacing.sm}"
    metaGap: "{spacing.xs}"
  product-card-hover:
    imageCursor: pointer
    swatchReveal: true
    secondaryImageFade: true
  hero-editorial:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    overlayType: full-bleed-image
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaVariant: button-primary
    textAlign: center
    padding: "{spacing.section} {spacing.xl}"
  hero-split:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    layout: image-left-text-right
    padding: "{spacing.xl}"
    gap: "{spacing.xl}"
  sub-brand-badge:
    textColor: "{colors.sub-brand-label}"
    typography: "{typography.sub-brand}"
    backgroundColor: transparent
  category-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
    selectedBorder: "1px solid {colors.ink}"
    unavailableTextColor: "{colors.muted-soft}"
    unavailableDecoration: line-through
  color-swatch:
    height: 24px
    width: 24px
    rounded: "{rounded.full}"
    selectedRing: "2px solid {colors.ink}"
    selectedRingOffset: 2px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    activeTextColor: "{colors.ink}"
  product-grid:
    gap: "{spacing.base}"
    columns: 4
    mobileColumns: 2
    tabletColumns: 3
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 36px
    padding: 0 12px
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    selectedBorder: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 44px
    iconColor: "{colors.ink}"
    focusBorder: "1px solid {colors.ink}"
  mobile-nav-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    subBrandTypography: "{typography.sub-brand}"
    subBrandColor: "{colors.sub-brand-label}"
    width: 100vw
    height: 100vh
    overlayColor: "{colors.ink}"
    overlayOpacity: 0.4
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    headingTypography: "{typography.button-sm}"
    padding: "{spacing.xxl} 0"
    borderTop: none
  loyalty-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"

## Components

### Buttons
**`button-primary`** — A full-bleed dark rectangle at 48px height, #313131 background with white uppercase tracking text at `{typography.button-md}`. No border radius; the hard corner is load-bearing to the brand's architectural identity. Active state deepens to `{colors.primary-active}` (#1a1a1a); disabled state fades background to `{colors.primary-disabled}` without changing the rectangle shape.

**`button-secondary`** — White canvas with a 1px `{colors.primary}` border and `{colors.primary}` text at the same uppercase tracking. On hover, the button inverts — background fills to `{colors.primary}`, text flips to `{colors.on-primary}` — a deliberate swap that reinforces the monochromatic vocabulary. Same 48px height and `{rounded.none}` geometry as primary.

**`button-text-link`** — Transparent background with underline decoration; used for secondary actions within product detail pages (size guides, return policy) where a full button would over-weight the layout. Inherits `{typography.button-sm}` uppercase tracking.

### Inputs
**`text-input`** — A bare white rectangle with 1px `{colors.hairline}` border, no fill tint, no border radius. Focus upgrades the border to `{colors.ink}` without adding a glow or shadow. Error state swaps border and label text to `{colors.sale}`. Form fields stack with tight `{spacing.sm}` gap, leaning on label weight (500) to separate field groups rather than using background shading.

### Navigation
**`nav-bar`** — 56px sticky bar, white canvas, containing the wordmark at left (20px height), primary category nav in compressed uppercase `{typography.nav-link}` at center, and a three-icon cluster (search, wishlist, bag) at right. A 1px `{colors.hairline}` bottom border separates it from page content. No background blur or shadow on scroll.

**`nav-dropdown`** — Full-width panel anchored below the nav bar, white background with a 1px `{colors.hairline}` top edge. Sub-brand names render in `{typography.sub-brand}` at `{colors.sub-brand-label}` as section headers above category links in `{typography.body-md}`. No animation beyond a simple opacity fade-in; no nested flyouts.

**`mobile-nav-drawer`** — Full-viewport overlay sliding in from the left. White background; sub-brand taxonomy exposed vertically with sub-brand identifiers in `{typography.sub-brand}` at `{colors.sub-brand-label}`. A 40% opacity `{colors.ink}` scrim covers the remaining viewport behind the drawer.

### Product Cards
**`product-card`** — Flush-edge rectangle at `{rounded.none}`. Image fills the top portion against a `{colors.surface-soft}` placeholder background; below the image a tight stack: sub-brand in `{typography.sub-brand}` at `{colors.sub-brand-label}`, product name in `{typography.body-sm}`, then price in `{typography.price-display}`. On sale, the original price renders with `line-through` in `{colors.muted}` alongside the sale price in `{colors.sale}`. On hover, a secondary product image fades in and color swatches appear below the name — no card border or shadow is ever added.

**`color-swatch`** — 24×24px filled circle at `{rounded.full}`, ring-selected via a 2px `{colors.ink}` outline with a 2px gap. Unavailable swatches render at 40% opacity with a diagonal line overlay.

**`size-selector`** — 40×40px square buttons at `{rounded.none}`. Default state: 1px `{colors.hairline}` border, `{colors.ink}` text. Selected state: 1px `{colors.ink}` border, text weight stays the same — selection indicated purely by border weight. Unavailable sizes show `{colors.muted-soft}` text with `line-through`.

### Product Grid & Filtering
**`product-grid`** — 4 columns on desktop, 3 on tablet, 2 on mobile; `{spacing.base}` gap both axes. No card shadow, no card border — grid lines implied only by the gap. Sorting and filter controls sit in a sticky sub-bar beneath the nav at desktop; they collapse into a bottom-sheet on mobile.

**`filter-chip`** — Compact 36px-tall label pill at `{rounded.none}`. Unselected: `{colors.canvas}` with `{colors.hairline}` border. Selected: fills to `{colors.primary}` with `{colors.on-primary}` text. No animation; state change is instant.

### Editorial & Hero
**`hero-editorial`** — Full-bleed image with centered text overlay. Title at `{typography.display-xl}` in `{colors.on-dark}`, a short body line in `{typography.body-md}`, and a `button-primary` CTA. No gradient scrim; relies on art-direction to ensure legibility. Padding `{spacing.section}` vertical, `{spacing.xl}` horizontal.

**`hero-split`** — Two-column layout at desktop: image left, editorial copy right. Title at `{typography.display-lg}` in `{colors.ink}`, body in `{typography.body-md}`. Collapses to stacked image-above-text on mobile.

### Search
**`search-bar`** — 44px bar at `{rounded.none}`, matching text-input geometry. A magnifier icon in `{colors.ink}` sits at the leading edge. On mobile, the search icon in the nav expands into a full-width overlay bar rather than navigating to a separate page.

### Footer
**`footer`** — Dark `{colors.primary}` background with `{colors.on-primary}` text and links. Sub-brand names and category column headers in `{typography.button-sm}` uppercase. Link text in `{typography.caption}`. Legal text and copyright in `{typography.caption}` at reduced opacity. No dividing lines between columns; columnar layout implied by spacing grid alone.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | 2-column product grid; hamburger nav opens full-viewport drawer; hero switches to stacked image + text; filter/sort collapse into bottom sheet; search becomes overlay bar |
| Tablet | 744–1128px | 3-column product grid; nav retains top bar with horizontal scroll if needed; hero-split collapses to stacked; dropdown megamenu remains active |
| Desktop | 1128–1440px | 4-column product grid; full megamenu dropdown; hero-editorial at full bleed with centered CTA |
| Wide | > 1440px | Content max-width capped (~1440px), centered with canvas gutters; product grid stays 4 columns, image sizes scale up within grid cells |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Size selector buttons expand from 40px to 44px tap target on touch devices
- Color swatches minimum 44px tap target with invisible padding surround
- Nav icons in top bar maintain 44px tap area despite visual 24px icon size

### Collapsing Strategy
- Primary nav compresses to icon-only at mobile with full-viewport drawer revealing brand taxonomy
- Mega-dropdown replaced by accordion-style expand in drawer
- Filter sidebar collapses to bottom-sheet triggered by a sticky "Filter & Sort" bar
- Hero-split reflows image above copy on tablet and below; image always leads on mobile
- Footer columns reflow to 2-column grid on tablet, single column on mobile with accordions for each section

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site was behind Cloudflare anti-bot at extraction time ("Just a moment…"); only one hex value (#313131) was recovered — full palette including secondary accent colors, hover states, and any off-white variants is inferred from brand knowledge, not extracted
- No custom font stacks were detected; all observed stacks are OS/browser system fonts — the custom display typeface (likely a licensed expanded geometric sans-serif) loads via JS or is hosted on a protected CDN and was not captured
- No theme-color meta tag present; mobile browser chrome color is unconfirmed
- Exact border-radius values for any rounded components (if any exist) could not be measured — all `{rounded.none}` assignments above are inferred from editorial photography of the site, not pixel-measured
- Sub-brand color differentiation (whether Wilfred, TNA, Sunday Best carry distinct accent colors vs. sharing the monochromatic system) could not be confirmed from extraction
- Animation and transition timing values (nav dropdown, product image hover swap, drawer slide) are absent and would require live instrumentation to confirm
