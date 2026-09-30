---
version: alpha
name: "Music Man"
source_url: "https://www.music-man.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every finish option on a Music Man guitar — Vintage Sunburst, Powder Blue, Lemon Drop — has been obsessively photographed under controlled studio light; the website's primary job is to put that photography front and center and then disappear. The UI runs on a Bootstrap 3 scaffold with near-black navigation (#080808), a light-gray page canvas (#f5f5f5), and a Bootstrap-default link-blue (#337ab7) carrying all interactive states. The palette extraction reveals almost nothing proprietary — nearly every sampled hex is a Bootstrap 3 system color, from the #d9534f danger red to the #f0ad4e warning amber and the #5cb85c success green — which means the brand's visual identity is built entirely in the instrument photographs, not the CSS layer. Type runs on system-native stacks: Arial and Helvetica Neue at conventional weights, with Consolas and Menlo appearing only in code or monospace contexts. No custom typeface was detected, no proprietary hex outside Bootstrap defaults, no decorative surface motif. What the design does instead is dense: specification tables with alternating row stripes (#f5f5f5 over white) that let players parse neck radius, pickup configuration, and fret count at a glance; finish-swatch selectors that collapse an entire colorway into a 28px circle ({rounded.full}); and product cards arranged in Bootstrap's twelve-column grid at minimal gutter. The rounding scale sits firmly at Bootstrap defaults — {rounded.xs} corners (4px) on every button and input signal a precision-tool aesthetic rather than consumer-brand softness. Ernie Ball Music Man ships instruments to John Petrucci, Steve Lukather, and St. Vincent; the website does not attempt to out-perform the product. It steps back, organizes, and lets the finish photography close the sale.

colors:
  primary: "#337ab7"
  primary-active: "#286090"
  primary-disabled: "#a8c8e8"
  ink: "#080808"
  body: "#555555"
  muted: "#777777"
  muted-light: "#9d9d9d"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#080808"
  on-primary: "#ffffff"
  success: "#3c763d"
  success-bg: "#dff0d8"
  success-border: "#d6e9c6"
  warning: "#8a6d3b"
  warning-bg: "#fcf8e3"
  warning-border: "#faebcc"
  danger: "#a94442"
  danger-bg: "#f2dede"
  danger-border: "#ebccd1"
  info: "#31708f"
  info-bg: "#d9edf7"
  info-border: "#bce8f1"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  spec-value:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  mono:
    fontFamily: "Consolas, 'Courier New', Menlo, Monaco, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
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
    padding: 8px 16px
    height: 36px
    border: "1px solid {colors.primary-active}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: "1px solid #1a4065"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary-disabled}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
    border: "1px solid {colors.hairline}"
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
    height: 30px
    border: "1px solid {colors.primary-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
    border: "1px solid #cccccc"
    borderFocus: "1px solid {colors.primary}"
    boxShadowFocus: "0 0 8px rgba(51,122,183,0.6)"
    placeholderColor: "{colors.muted-light}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 50px
    linkHoverColor: "{colors.hairline-soft}"
    borderBottom: "none"
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    imagePadding: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-sm}"
    minHeight: 420px
    padding: "{spacing.xxl} {spacing.lg}"
    overlayOpacity: 0.4
  spec-table:
    backgroundColor: "{colors.canvas}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.ink}"
    valueTypography: "{typography.spec-value}"
    valueColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rowEvenBg: "{colors.surface-soft}"
    rowOddBg: "{colors.canvas}"
    cellPadding: "{spacing.sm} {spacing.base}"
    headingTypography: "{typography.title-sm}"
    headingBg: "{colors.surface-soft}"
  finish-selector:
    swatchSize: 28px
    swatchBorder: "2px solid {colors.hairline}"
    swatchBorderActive: "2px solid {colors.ink}"
    swatchRounded: "{rounded.full}"
    swatchGap: "{spacing.xs}"
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    activeLabel: "{colors.ink}"
  artist-badge:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "2px {spacing.sm}"
    textTransform: uppercase
    letterSpacing: "0.5px"
  alert-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.info}"
    border: "1px solid {colors.info-border}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    typography: "{typography.body-md}"
  alert-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    border: "1px solid {colors.success-border}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    typography: "{typography.body-md}"
  alert-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning}"
    border: "1px solid {colors.warning-border}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    typography: "{typography.body-md}"
  alert-danger:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger}"
    border: "1px solid {colors.danger-border}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    typography: "{typography.body-md}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    separatorColor: "{colors.muted-light}"
    activeColor: "{colors.body}"
    padding: "{spacing.sm} 0"
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
    border: "1px solid #cccccc"
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted-light}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline-soft}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    padding: "{spacing.xxl} 0"
    borderTop: "1px solid #222222"

## Components

### Buttons

**`button-primary`** — A Bootstrap-default rectangular button at 36px height with 4px corners ({rounded.xs}), #337ab7 fill, and white text. Hover and active states shift to #286090 with a darker border (#1a4065). Disabled state uses the lightened #a8c8e8 fill without cursor interaction. Used for primary CTAs like "Shop Now", "Add to Cart", and catalog filters.

**`button-secondary`** — White-fill with a #e5e5e5 border and body-gray text, matching Bootstrap's default secondary button. Appears alongside primary actions for cancel, back, and secondary navigation functions.

**`button-sm`** — Compact 30px variant of the primary button, used inside product cards, filter toolbars, and inline actions where vertical space is constrained.

### Text Input

**`text-input`** — 34px input following Bootstrap's standard form control: 1px solid #cccccc border at rest, a #337ab7 focus border with the signature 8px rgba-blue box-shadow ring that marks interactive focus in Bootstrap 3's visual language. Placeholder text falls to {colors.muted-light}. Appears in search, contact, and dealer-finder forms.

### Navigation

**`nav-bar`** — A 50px-tall near-black (#080808) horizontal bar carrying the Ernie Ball Music Man wordmark on the left and top-level category links in {typography.nav-link}. Links are white at rest, shifting to {colors.hairline-soft} on hover. No bottom border — the dark bar creates its own visual separation from the light page canvas below.

### Product Card

**`product-card`** — Sharp-cornered ({rounded.none}) card on a white surface with a 1px {colors.hairline} border. Product photography fills the upper image zone with {spacing.sm} internal padding; the lower zone contains the model name in {typography.title-sm}, an optional short descriptor in {typography.body-md}, and price in {typography.title-md}. Cards snap to Bootstrap's 12-column grid — 4 per row at desktop, 2 at tablet, 1 at mobile.

### Hero

**`hero`** — Full-width dark-field section (#080808 background) with a semi-transparent overlay (0.4 opacity) over instrument photography. Display heading in {typography.display-xl} and subtitle in {typography.display-sm} both render in canvas white. Minimum 420px height. Used for featured model launches and artist spotlights at the top of category pages.

### Spec Table

**`spec-table`** — Two-column specification table with {typography.spec-label} (bold, 13px) in the left column and {typography.spec-value} (regular, 13px) in the right. Even rows carry {colors.surface-soft} (#f5f5f5) zebra-stripe; odd rows are white. Section headers use {typography.title-sm} on a {colors.surface-soft} background. Cell padding is {spacing.sm} vertical by {spacing.base} horizontal. This component is the workhorse of the product detail page — neck profile, fretboard radius, nut width, pickup model, and hardware finish all live here.

### Finish Selector

**`finish-selector`** — A horizontal row of 28px circular swatches ({rounded.full}) representing the guitar's available finish colorways. At rest, each swatch has a 2px {colors.hairline} border; the active swatch switches to a 2px {colors.ink} border. Swatches are spaced with {spacing.xs} gap. Below the row, the active finish name renders in {typography.body-sm} at {colors.ink}. The label defaults to {colors.muted} when no swatch is selected.

### Artist Badge

**`artist-badge`** — A zero-radius label strip (no rounding) in {colors.surface-dark} with white {typography.caption} text set in all-caps with 0.5px letter-spacing. Applied over product card images or within the model name area to denote signature series (e.g., "John Petrucci", "St. Vincent"). Compact and typographically quiet — authority through restraint, not decoration.

### Alerts

**`alert-info` / `alert-success` / `alert-warning` / `alert-danger`** — Bootstrap's standard contextual alert blocks at {rounded.xs}. Each variant pairs a tinted background (info: {colors.info-bg}, success: {colors.success-bg}, warning: {colors.warning-bg}, danger: {colors.danger-bg}) with a matching text and border color from the same system token family. Used for stock notifications, shipping messages, form validation feedback, and promotional notices.

### Breadcrumb

**`breadcrumb`** — Flat, transparent navigation trail in {typography.body-sm} at {colors.muted} with a {colors.muted-light} separator glyph. The terminal (active) crumb shifts to {colors.body} without underline. Appears below the nav bar on all category and product detail pages.

### Footer

**`footer`** — A dark (#080808) full-width footer with {spacing.xxl} top and bottom padding and a subtle #222222 top border to separate from the page body. Column headings render in {typography.title-sm} at {colors.canvas}; body links and text in {typography.body-sm} at {colors.muted-light}. Link hover shifts to {colors.canvas}. Houses dealer locator, social links, warranty information, and Ernie Ball group navigation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Single-column product grid; hamburger nav collapse; hero text scales down to display-md; spec table stacks label above value; finish swatches wrap to two rows if needed |
| Tablet | 768–992px | Two-column product grid; nav collapses to hamburger; hero retains two-column text/image split at reduced font sizes |
| Desktop | 992–1200px | Four-column product grid; full horizontal nav bar; hero at full 420px height; spec table side-by-side at full width |
| Wide | > 1200px | Centered container max-width (~1170px Bootstrap default); page canvas visible on sides; no additional layout changes |

### Touch Targets

- Buttons maintain Bootstrap's minimum 36px height (30px for sm variant) — acceptable but below the 44px iOS recommendation; form inputs at 34px similarly tight on touch
- Finish swatches at 28px are small for touch; consider 40px touch-area padding around the 28px visual swatch on mobile
- Nav links in the collapsed mobile menu should expand to a minimum 44px tap height

### Collapsing Strategy

- Navigation collapses to Bootstrap's default hamburger (`navbar-toggle`) at the 768px breakpoint
- Product grid collapses from 4 → 2 → 1 columns using Bootstrap's `.col-md-3 / .col-sm-6 / .col-xs-12` pattern
- Spec tables on mobile stack label above value rather than side-by-side, converting the two-column layout to a single-column definition list
- The hero section drops to a single centered text column on mobile with a reduced min-height (~280px)
- Footer columns collapse from a multi-column Bootstrap grid row to a single stacked column at mobile breakpoint

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Almost the entire extracted palette is Bootstrap 3's factory default color set; no proprietary brand hex values were isolated. The brand's actual primary campaign color (if distinct from Bootstrap's #337ab7) could not be determined from CSS extraction alone.
- No custom web font was detected. The brand may use a licensed typeface loaded via a third-party CDN that was blocked during extraction, or may deliberately rely on system fonts.
- Hero and campaign banner exact color overlays, gradient stops, and photography art direction could not be quantified without live screenshot analysis.
- Product photography background treatment (pure white vs. gradient vs. contextual studio) was not confirmed in extraction.
- Specific icon set beyond FontAwesome and Bootstrap Glyphicons (e.g., custom guitar-body silhouette icons used in product navigation) was not catalogued.
- Mobile navigation exact behavior (full-screen overlay vs. push drawer vs. dropdown) was not confirmed.
- Any brand-specific animation or transition timing (e.g., finish swatch hover transitions, page-load fade-ins) was not captured.
- E-commerce cart and checkout UI components were not visible in the extraction pass.
