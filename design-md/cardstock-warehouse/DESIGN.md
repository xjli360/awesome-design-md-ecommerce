---
version: alpha
name: "Cardstock Warehouse"
source_url: "https://www.cardstockwarehouse.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Amber ink on periwinkle stock — the dominant CTA color (#ff9f1c) lands against soft lavender category chips (#bbc1e1) and a barely-blue canvas (#f5f9ff) that reads like lightly tinted card stock rather than blank white. Raleway, a geometric sans with Art Nouveau echoes in its letterforms, carries every heading at weight 700, giving the headline type a distinctiveness that neutral system stacks cannot offer. Body and navigation text settles into a cooled slate (#50596c): not warm gray, not cold charcoal, but the color of a soft pencil line on smooth card.

  The periwinkle family runs three depths — #899df1 for active UI states, #bbc1e1 for filter chips and surface accents, #e1e6f9 for soft background fills — giving the shop a tonal range tuned to selling paper by color swatch. Sale badges snap to #e63946, alert-red like a stamped discount sticker; forest green (#2e7e4b) flags in-stock status. Pale amber (#faeaa1) fills site-wide promotional banners without the visual noise of the full primary orange. Every interactive edge softens: inputs sit at {rounded.sm}, product cards at {rounded.md}, and filter pills expand to {rounded.full}, so the overall register is boutique stationery studio rather than warehouse liquidator.

  Spacing leans generous, using {spacing.section} (64px) gaps between content rows — the whitespace logic of a well-laid magazine spread rather than a tightly packed category page. The type scale runs Raleway from 36px display headings down to 11px badge labels, with slight negative letter-spacing at large sizes and subtle positive tracking on uppercase badge text to keep small caps sharp. The result is a paper shop confident enough in its curation to give each product room to breathe.

colors:
  primary: "#ff9f1c"
  primary-active: "#e08800"
  primary-disabled: "#ffd68a"
  sale-red: "#e63946"
  error-deep: "#d72c0d"
  success: "#2e7e4b"
  success-soft: "#abdbc0"
  periwinkle: "#bbc1e1"
  periwinkle-active: "#899df1"
  ink: "#1a1b18"
  body: "#50596c"
  muted: "#767167"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#f5f9ff"
  surface-soft: "#e1e6f9"
  surface-card: "#ffffff"
  surface-promo: "#faeaa1"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.2px
  nav-label:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.1px
  price-display:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge-label:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  promo-headline:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.2px

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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.body}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    focusBorderColor: "{colors.periwinkle-active}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 42px
    iconColor: "{colors.muted}"
    focusBorderColor: "{colors.periwinkle-active}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageRounded: "{rounded.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
  category-filter-pill:
    backgroundColor: "{colors.periwinkle}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    activeBackgroundColor: "{colors.periwinkle-active}"
    activeTextColor: "{colors.on-dark}"
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-instock:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaComponent: "button-primary"
  promo-banner:
    backgroundColor: "{colors.surface-promo}"
    textColor: "{colors.ink}"
    typography: "{typography.promo-headline}"
    padding: "{spacing.sm} {spacing.lg}"
    linkColor: "{colors.body}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.body}"
  price-regular:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  price-sale:
    textColor: "{colors.sale-red}"
    typography: "{typography.price-display}"
  price-original:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    textDecoration: line-through
  quantity-stepper:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    height: 40px
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.periwinkle}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Amber (#ff9f1c) fill at {rounded.sm} with white Raleway 600 text, 44px tall. The hover state deepens to #e08800; the disabled state fades fill to #ffd68a while retaining white text. This is the dominant action button across add-to-cart, checkout entry, and filter application.

**`button-secondary`** — White fill with a 1px slate (#50596c) border and matching slate text. Identical height (44px) and radius to `button-primary` so paired button rows sit flush. Used for secondary navigation choices, modal cancellations, and "View All" links.

**`button-ghost`** — Transparent background, slate body text, no border. Appears in inline content contexts, breadcrumb supplemental links, and de-emphasized repetitive actions.

### Form Inputs

**`text-input`** — White fill, 1px #dedede border at {rounded.sm}, 42px tall. On focus, the border color swaps to periwinkle-active (#899df1) with no drop-shadow halo. Placeholder text renders in {colors.muted} at normal weight.

**`search-bar`** — Pill-shaped ({rounded.full}) variant of the standard text input, used as the site-wide primary search. A search icon sits at the interior left in {colors.muted}; the focus border activates to #899df1. Consistent 42px height with the standard input for toolbar alignment.

**`quantity-stepper`** — A three-cell inline unit (decrement | count | increment) sharing a 40px height, hairline borders between cells, and {rounded.sm} on the outer corners only.

### Navigation

**`nav-bar`** — White background at 64px tall with a 1px hairline bottom divider. Logo anchors left; primary category links run center or collapse to a hamburger drawer on mobile; cart and account icons sit right. All nav text uses {typography.nav-label} in {colors.body}.

**`breadcrumb`** — Caption-scale (#767167) trail with hairline chevron separators. The current-page crumb uses {colors.body} without underline; ancestor crumbs are muted with hover underlines.

### Product Display

**`product-card`** — White card with 12px radius and a 1px hairline border. Product photography fills the top image area with {rounded.sm} applied; below: title in {typography.title-sm}, price in {typography.price-display}. Badge overlays pin to the top-left corner of the image region.

**`category-filter-pill`** — Periwinkle (#bbc1e1) fill at {rounded.full} with slate text in Raleway 600 at 13px. The active state flips to deeper periwinkle (#899df1) with white text. These chips scroll horizontally above the product grid as the primary facet navigation.

**`badge-sale`** — Red (#e63946) rectangular badge at {rounded.xs}, uppercase 11px Raleway 700, 3px/8px padding. Applied as an image overlay on product grid cards and detail page headers.

**`badge-new`** — Identical geometry and spec to `badge-sale`, amber (#ff9f1c) fill. Marks recently added SKUs across the catalog.

**`badge-instock`** — Forest green (#2e7e4b) fill, same geometry. Used as a positive availability signal on product detail pages; not applied at grid card scale.

### Hero & Promotions

**`hero-banner`** — Light periwinkle surface (#e1e6f9) background with the display-xl headline and body-md supporting copy. The primary CTA renders as `button-primary`. Vertical padding is generous at {spacing.section} (64px) to create the page-spread quality characteristic of the brand.

**`promo-banner`** — Pale amber (#faeaa1) full-width strip that sits above or below the nav bar. Headline text uses {typography.promo-headline} in {colors.ink} with a body-colored text link inline. Dismissible via an X icon at the far right.

### Pricing

**`price-sale`** and **`price-original`** — Sale price renders in red (#e63946) at {typography.price-display}; the original price renders immediately adjacent in {colors.muted} at {typography.body-sm} with a line-through decoration. Regular-price products use `price-regular` in {colors.ink} alone.

### Footer

**`footer`** — Slate (#50596c) background with white text and periwinkle (#bbc1e1) link accents. Column headings use {typography.title-sm} in {colors.on-dark}; body links use {typography.body-sm}. Vertical padding is {spacing.xxl} (48px) top and bottom.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; filter pills become a horizontally scrollable strip with no wrapping; hero headline drops to display-md; promo banner wraps to two lines |
| Tablet | 744–1128px | Two-column product grid; top-level nav links render inline; hero shifts to side-by-side text and image; filter chips stay above grid in a wrapping row |
| Desktop | 1128–1440px | Three or four-column product grid; full nav with flyout dropdowns; hero runs display-xl; sidebar filter panel renders to the left of the grid |
| Wide | > 1440px | Container max-width ~1440px centered; outer gutters grow; grid can expand to five columns for high-density catalog browsing |

### Touch Targets

- Filter pill minimum height 36px on mobile to meet thumb-tap spec
- Quantity stepper cells minimum 40×40px tap zone
- Nav icons (cart, search, account) minimum 44×44px
- Primary CTA buttons on mobile expand to full container width
- Product card tap target spans the full card face

### Collapsing Strategy

- Sidebar filters collapse into a bottom-sheet modal triggered by a "Filter" pill button on mobile and tablet
- Category navigation collapses into a full-screen slide-in drawer at widths below 744px
- Promo banner truncates to a single line with a "See more" inline link on mobile
- Footer columns stack to a single column on mobile, two-up on tablet

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand font files confirmed beyond the Raleway stack — weight variants (100–900 available in Raleway) used at each scale are inferred from visual pattern, not extracted from CSS
- Meta theme-color not set; exact nav and header background tones cannot be definitively confirmed from extraction alone
- Extracted palette mixes brand colors with Shopify admin UI artifacts (#008060, #409eff, #03de90) — filtered out as framework colors, not brand tokens
- Hover and focus state colors for the periwinkle chip family are inferred from palette depth; actual interaction states not observed
- Product detail page layout (image gallery type, variant swatches, tab structure) not derivable from hex/font extraction
- Mobile breakpoint pixel values inferred from Shopify theme conventions; actual breakpoints may differ from the values specified here
- Logo treatment, wordmark sizing, and top-nav lockup proportions not extractable from current hints
- Whether #ffb503 (extracted amber-yellow) is used distinctly from #ff9f1c in the live UI could not be confirmed — treated as a secondary amber shade not separately tokenized
