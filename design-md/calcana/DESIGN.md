---
version: alpha
name: "Calcana"
source_url: "https://www.calcana.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The store gate — "Shop Calcana Infrared Heaters | Choose USA or Canada Store" — is the brand's first statement: Calcana routes buyers by jurisdiction before they see a product, the move of a cross-border industrial supplier rather than a lifestyle shop. That operational transparency runs straight through the visual language. The single warm element in an otherwise industrial palette is `#f28c1f`, the precise amber of a gas pilot flame, which appears on every primary CTA and heat-output badge against near-black surfaces (`#151414`, `#2f2e2e`) and cool off-whites (`#f1f0ef`, `#f5f7ff`). Nothing else is warm; the orange earns its temperature through isolation and contrast. Typography reinforces the technical register without tipping into the utilitarian. Futura LT drives headlines and call-to-action labels — geometric and engineered — with uppercase buttons tracked at 1.2px in `{typography.button-md}` that read like silk-screened panel markings. DIN Next Light handles specification labels, sustaining the data-table cadence that commercial and residential contractors expect: BTU output, coverage area, mounting type, IP rating, all in small-caps. Avenir Light carries navigation and secondary copy — still clean-working-class but fractionally warmer than DIN. Proxima Nova handles installation guides and FAQ body text, a dependable serif-substitute for long-form technical prose. Corner radii are nearly flat: `{rounded.xs}` at 4px for buttons and inputs, `{rounded.sm}` at 8px for cards. The spec strip — a full-bleed `{colors.ink}` band carrying BTU, coverage, and rating columns in tracked white caps — is the signature component, porting catalog-page density directly into the product experience. Two geo-flag badges (`badge-usa` in `#116dff`, `badge-canada` in `#df3336`) appear at the product-card level to signal regulatory and shipping jurisdiction, a pattern that belongs to industrial portals rather than consumer lifestyle brands. The footer closes every page with a column-grid in `{colors.ink}` that mirrors the spec strip, making the last impression one of data density rather than brand warmth.

colors:
  primary: "#f28c1f"
  primary-active: "#d4730a"
  primary-disabled: "#f9d6b0"
  accent-blue: "#116dff"
  accent-blue-deep: "#0f2ccf"
  accent-blue-soft: "#597dff"
  danger: "#df3336"
  danger-dark: "#9c2426"
  success-dark: "#0d4f3d"
  success: "#4b916d"
  ink: "#151414"
  body: "#383838"
  muted: "#767574"
  muted-soft: "#a8a6a5"
  hairline: "#e0dfdf"
  hairline-soft: "#f1f0ef"
  canvas: "#ffffff"
  surface-soft: "#f1f0ef"
  surface-card: "#ffffff"
  surface-dark: "#2f2e2e"
  surface-mid: "#525150"
  on-primary: "#ffffff"
  on-dark: "#f1f0ef"
  scrim: "#080808"

typography:
  display-xl:
    fontFamily: "'futura-lt-w05-book', 'futura-lt-w01-book', 'Futura LT', Arial, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'futura-lt-w05-book', 'futura-lt-w01-book', Arial, sans-serif"
    fontSize: 34px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'futura-lt-w05-book', 'futura-lt-w01-book', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'avenir-lt-w05_35-light', 'avenir-lt-w01_35-light1475496', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'avenir-lt-w05_35-light', 'avenir-lt-w01_35-light1475496', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'proxima-n-w01-reg', 'Proxima Nova', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-n-w01-reg', 'Proxima Nova', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-n-w01-reg', 'Proxima Nova', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'futura-lt-w05-book', 'futura-lt-w01-book', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1.2px
    textTransform: uppercase
  button-sm:
    fontFamily: "'futura-lt-w05-book', 'futura-lt-w01-book', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'avenir-lt-w05_35-light', 'avenir-lt-w01_35-light1475496', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.4px
  spec-label:
    fontFamily: "'din-next-w01-light', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 1.8px
    textTransform: uppercase
  spec-value:
    fontFamily: "'futura-lt-w05-book', 'futura-lt-w01-book', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'futura-lt-w05-book', 'futura-lt-w01-book', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  footer-heading:
    fontFamily: "'futura-lt-w05-book', 'futura-lt-w01-book', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1.5px
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
    rounded: "{rounded.xs}"
    padding: 14px 32px
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
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 30px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-ghost-white:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    border: "2px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 30px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoArea: 140px
  store-selector-tab:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    activeIndicatorColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: "8px 16px"
    rounded: "{rounded.xs}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageBackground: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    subtitleTypography: "{typography.body-sm}"
    hoverBorderColor: "{colors.primary}"
    hoverTransition: "border-color 0.15s ease"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    overlayGradient: "linear-gradient(to bottom, rgba(21,20,20,0.35) 0%, rgba(21,20,20,0.80) 60%, rgba(21,20,20,0.95) 100%)"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.title-md}"
    ctaSpacingTop: "{spacing.xl}"
    minHeight: 580px
    padding: "{spacing.section} {spacing.xl}"
  spec-strip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    labelColor: "{colors.muted-soft}"
    accentColor: "{colors.primary}"
    padding: "{spacing.xl} 0"
    columnGap: "{spacing.xxl}"
    borderTop: "3px solid {colors.primary}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    hoverOverlay: "rgba(242,140,31,0.10)"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
  badge-heat-output:
    backgroundColor: "rgba(242,140,31,0.12)"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "5px 10px"
  badge-usa:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-canada:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  accordion-faq:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    activeBorderColor: "{colors.primary}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base} {spacing.lg}"
    iconColor: "{colors.primary}"
  product-tabs:
    backgroundColor: "{colors.canvas}"
    activeTextColor: "{colors.ink}"
    inactiveTextColor: "{colors.muted}"
    activeIndicator: "2px solid {colors.primary}"
    typography: "{typography.nav-link}"
    tabHeight: 48px
    borderBottom: "1px solid {colors.hairline}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.ink}"
    headerTextColor: "{colors.on-dark}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    highlightRowColor: "rgba(242,140,31,0.06)"
    border: "1px solid {colors.hairline}"
    cellPadding: "{spacing.base} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.footer-heading}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Calcana's primary CTA renders in `#f28c1f` amber with tracked uppercase Futura at 1.2px, 4px corners, and a 48px touch height. On dark hero sections the `button-ghost-white` variant maintains the same geometry with a 2px white border and transparent fill, preserving legibility without introducing a competing warm tone. Hover darkens to `#d4730a`; disabled washes out to `#f9d6b0` and drops pointer events.

**`button-secondary`** — An outline button in `{colors.ink}` with a 2px border and no fill, used for secondary actions on light surfaces such as product pages and FAQ panels. Activating fills the background with `{colors.ink}` and flips the label to `{colors.on-dark}`, giving a confident pressed-plate feel rather than a gradual fade.

### Navigation

**`nav-bar`** — A 72px white bar with a 1px `{colors.hairline}` bottom border. Navigation labels use Avenir Light at 14px with 0.4px tracking, lighter than a typical nav to keep the header visually recessed relative to the heavy hero below. The `store-selector-tab` pill sits at the right edge of the header bar, with a `{colors.primary}` underline on the active jurisdiction.

**`store-selector-tab`** — The USA/Canada store selector renders as a pair of `{colors.surface-dark}` tabs with `{typography.button-sm}` uppercase labels. The active store tab carries a `{colors.primary}` bottom indicator. On mobile the selector collapses into a flag-icon dropdown.

### Product Cards

**`product-card`** — A 1px `{colors.hairline}`-bordered card on white with an `{colors.surface-soft}` image well. Title renders in `{typography.title-sm}` Avenir, price in `{typography.price-display}` Futura at 26px. Hover transitions the border to `{colors.primary}` over 150ms, the only color animation in the system. Geo-flag badges (`badge-usa` or `badge-canada`) pin to the top-right of the image well to surface regulatory jurisdiction without breaking the card's clean grid.

**`badge-heat-output`** — An amber-tinted chip with a full `#f28c1f` border and `{typography.spec-label}` tracked caps reading something like "40,000 BTU". This badge appears on both product cards and within spec strips, functioning as a quick-glance performance signal without competing with the primary CTA.

### Hero

**`hero`** — A full-bleed darkened image section with a bottom-weighted gradient (`rgba(21,20,20,0.95)` at 100%) to guarantee headline legibility over any product photography. Title uses `{typography.display-xl}` Futura at 52px; the CTA pair (`button-primary` + `button-ghost-white`) sits `{spacing.xl}` below the subtitle. Minimum height 580px collapses to 360px on mobile.

### Spec Strip

**`spec-strip`** — A full-width `{colors.ink}` band separating hero from product grid, carrying 3–5 horizontal columns of BTU output, coverage area, IP rating, and voltage specs. Labels render in `{typography.spec-label}` (`#a8a6a5` muted), values in `{typography.spec-value}` Futura at 22px white. A `3px solid {colors.primary}` top border connects the strip visually to the primary palette. This component is the most brand-distinctive element on any Calcana page — it ports industrial-catalog density directly into e-commerce.

### Comparison & FAQ

**`comparison-table`** — A bordered data table with an `{colors.ink}` header row in white `{typography.spec-label}` caps. Alternating highlight rows use a 6%-opacity amber tint (`rgba(242,140,31,0.06)`) to subtly mark the featured product column. Cell padding is `{spacing.base} {spacing.lg}`.

**`accordion-faq`** — Standard expand/collapse with a 1px border that transitions to `{colors.primary}` when open. The open-state chevron icon also renders in `{colors.primary}`. Title typography is `{typography.title-sm}` Avenir; body text is `{typography.body-md}` Proxima Nova for comfortable reading of multi-paragraph installation and warranty answers.

### Footer

**`footer`** — A full-width `{colors.ink}` footer with a `3px solid {colors.primary}` top edge echoing the spec strip. Column headings use `{typography.footer-heading}` Futura tracked caps in white; body links use `{typography.body-sm}` Proxima in `{colors.muted-soft}`, transitioning to `{colors.primary}` on hover. The dual-store architecture means two distinct contact and policy link sets appear side by side in final columns.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero height reduces to 360px; spec strip stacks vertically 2×2; nav collapses to hamburger with store-selector dropdown; comparison table horizontally scrollable |
| Tablet | 744–1128px | Two-column product grid; spec strip stays horizontal at 4 columns; hero text scales to `{typography.display-md}`; nav shows logo + hamburger |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links visible; spec strip 5 columns; hero at full 580px min-height |
| Wide | > 1440px | Max-width container 1440px centered; hero background bleeds to edge but content constrained; four-column product grid |

### Touch Targets

- All primary and secondary buttons minimum 48px height
- Nav links minimum 44px tap region with padding compensation
- Store-selector tabs minimum 44×36px
- Accordion triggers minimum 48px height with full-row tap target
- Product card is fully tappable (entire card is anchor)

### Collapsing Strategy

- Navigation: hamburger at ≤ 1024px, full links at > 1024px
- Spec strip: 5-column horizontal on desktop/tablet, 2×2 stack on mobile with remaining column below
- Comparison table: horizontal scroll with sticky first column on mobile
- Hero CTA pair: stacks vertically on mobile with `button-primary` first
- Store selector: tabs in header on desktop, icon-triggered modal sheet on mobile
- Footer: 4-column grid collapses to 2 columns on tablet, single-column accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The blue family (`#116dff`, `#0f2ccf`, `#2f5dff`, `#597dff`, and the full tint ramp through `#f5f7ff`) closely matches Wix platform default CTA and focus-ring colors; it is unclear whether these are Calcana brand choices or editor-injected defaults
- No meta `theme-color` was present, so the mobile status-bar brand color is unconfirmed
- Japanese font stacks (Hiragino Kaku Gothic Pro, Meiryo) suggest a localized content variant exists, but no Japanese-market design tokens or layout adaptations could be extracted
- Hero photography palette is unknown — gradient overlay values are estimated defaults rather than extracted from actual images
- No cart, checkout, or account UI was accessible for extraction; e-commerce flow components are inferred from product-page patterns only
- Exact logo dimensions, SVG geometry, and clearspace rules were not extractable from the live site
- The success green (`#0d4f3d`, `#4b916d`) appears in the color set but no clear component context was identified — possibly used for in-stock badges or promotional banners
