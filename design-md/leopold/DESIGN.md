---
version: alpha
name: "Leopold"
source_url: "https://global.leopold.co.kr"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The keyboard is the only decoration Leopold allows itself — the global storefront wraps every product in a white field with near-black text (#1c1c1c) and hairline dividers (#e0e0e0) that read less like retail and more like an instrument catalogue from a precision-tool manufacturer. The South Korean maker has spent over a decade building a community following almost entirely on internal architecture: POM plates, Cherry and Leopold-manufactured switches, doubleshot PBT keycaps with legends that outlast the board itself. The site enforces the same material hierarchy — the keyboard photograph dominates, surrounded by specification rows set in a clean system sans-serif at modest weights, and the only gesture toward softness is the faint gray of the surface-soft background (#f5f5f5) behind product grids. Color options are presented as small rectangular swatches, not lifestyle imagery; the copy reads in the plainspoken register of a spec sheet. Leopold has no signature brand color because it does not need one — the product palette shifts with each model (beige, gray, black, white) and the UI palette stays neutral enough to defer entirely to whatever keyboard sits in the frame. Navigation is flat and typographic, with no icon flourish; buttons are near-black rectangles ({rounded.xs}) that match the keycap profile rather than softening toward the rounded pill shapes of lifestyle brands. The compact keyboard form factor — the 60%, TKL, and 65% layouts Leopold specializes in — informs the entire grid: space is not wasted, every element occupies the minimum footprint for its function. Footer links stack in clean columns at the same weight and size as body text, no hierarchy inflation. The engineering is the design, and the design system's role is to not argue with that.

colors:
  primary: "#1c1c1c"
  primary-active: "#000000"
  primary-disabled: "#aaaaaa"
  ink: "#111111"
  body: "#333333"
  muted: "#777777"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  swatch-border: "#cccccc"
  error: "#c0392b"
  link: "#1c1c1c"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.2px
  model-name:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.4px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  tag:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.1px

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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 34px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    padding: 0 24px
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    fontWeight: 700
  category-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    activeTextColor: "{colors.primary}"
    activeBorderBottom: "2px solid {colors.primary}"
    padding: 8px 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    imageAspect: "4/3"
    padding: 12px
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.body}"
    hoverShadow: "0 2px 8px rgba(0,0,0,0.08)"
  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: 64px 0
    imagePosition: right
    maxWidth: 1280px
  product-detail-header:
    backgroundColor: "{colors.canvas}"
    modelTypography: "{typography.model-name}"
    modelColor: "{colors.ink}"
    subTypography: "{typography.body-sm}"
    subColor: "{colors.muted}"
    padding: 32px 0
  spec-table:
    backgroundColor: "{colors.canvas}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    rowBorder: "1px solid {colors.hairline-soft}"
    rowPadding: 12px 0
  color-swatch:
    size: 24px
    rounded: "{rounded.none}"
    border: "1px solid {colors.swatch-border}"
    selectedBorder: "2px solid {colors.primary}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    gap: 4px
  switch-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    border: "1px solid {colors.hairline}"
  keyboard-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    padding: 24px
    thumbnailSize: 72px
    thumbnailBorder: "1px solid {colors.hairline}"
    activeThumbnailBorder: "2px solid {colors.primary}"
  model-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.tag}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-dark}"
    padding: 48px 0
    borderTop: none

## Components

### Buttons

**`button-primary`** — A near-black (#1c1c1c) rectangle at {rounded.xs} corner radius, 44px tall, padded 12px vertically and 24px horizontally. This is the dominant CTA for add-to-cart and regional purchase flows. Active state deepens to pure black (#000000); disabled washes to #aaaaaa while preserving white text. The minimal rounding echoes the right-angle geometry of keycap profiles — no softening concession to lifestyle aesthetics.

**`button-secondary`** — White fill with a 1px primary-colored border at {rounded.xs}, matched in height and padding to button-primary so the two sit side-by-side without optical imbalance. Used for "View Details," compare, and region-selector actions.

**`button-ghost`** — Transparent fill with a {colors.hairline} border. Reserved for tertiary controls — filter toggles, sort dropdowns, pagination — where additional ink weight would crowd the spec-dense layouts.

**`button-sm`** — A compact 34px variant of button-primary in {typography.button-sm}. Used for inline actions inside product cards and specification tables where a full-height button would overpower its context.

### Navigation

**`nav-bar`** — A 60px white header with a single 1px {colors.hairline} bottom border providing the only structural division. Logo anchors left; category links run center in {typography.nav-link} at weight 500; region selector, search, and cart icons anchor right. No drop shadow, no mega-menu decoration — the nav reads as a clean index, not a marketing surface.

**`category-nav`** — A horizontal tab row for keyboard family navigation (FC660M, FC750R, FC900R, and compact lines). The active tab receives a 2px {colors.primary} underline border rather than any background highlight, keeping the bar typographically flat. Inactive tabs sit at {colors.body} weight with no hover animation beyond a color shift to {colors.ink}.

### Product Display

**`product-card`** — White card with a faint {colors.hairline-soft} border and a 4:3 keyboard photograph on {colors.surface-soft}. Title in {typography.title-md} at ink weight; price in {typography.body-md} at body weight. On hover, a 0 2px 8px shadow lifts the card without rounding it. No ribbon, badge overlay, or promotional sticker unless a model-badge is explicitly needed for series identification.

**`keyboard-gallery`** — The product detail image module: a large main image on a {colors.surface-soft} field, with a horizontal strip of 72px thumbnails below. Each thumbnail sits in a {colors.hairline} box; the active thumbnail upgrades to a 2px {colors.primary} border. No lightbox or overlay — image swaps inline to keep focus on hardware detail without UI interruption.

**`color-swatch`** — 24px square swatches at {rounded.none}, arranged in a horizontal row with 4px gaps. Inactive swatches carry a 1px {colors.swatch-border} border; the selected swatch upgrades to a 2px {colors.primary} border. Swatch label in {typography.caption} at {colors.muted} appears below the row. The square geometry is a direct reference to the keycap legend grid and signals that this is a material selector, not a decorative palette picker.

**`switch-selector`** — A segmented control for choosing switch type (Cherry MX Red, Brown, Blue, Silent Red, and Leopold-branded equivalents). Each tile is a {colors.surface-soft} block in {typography.body-sm} with a {colors.hairline} border. Selected tile inverts to {colors.primary} fill with {colors.on-primary} text. Placed inline in the product configurator above the add-to-cart button. On mobile, tiles wrap to a two-column grid rather than scrolling horizontally.

### Product Information

**`spec-table`** — A definition list in alternating rows separated by 1px {colors.hairline-soft} borders on a white background. Label column renders in {typography.spec-label} at {colors.muted}; value column in {typography.body-sm} at {colors.ink}. No zebra striping, no row hover — the table communicates data hierarchy through weight contrast alone. Key rows: Layout, Switch, Keycap, Case Material, PCB, Weight, Dimensions.

**`model-badge`** — A rectangular tag at {rounded.none} with {colors.surface-soft} fill and {typography.tag} text in {colors.muted}. Used to label keyboard series and layout class in product grid headers. The uppercase tracking (0.5px) gives it a technical classification register without color noise.

**`product-detail-header`** — The model name in {typography.model-name} at {colors.ink}, followed by a subtitle line (switch type, layout class) in {typography.body-sm} at {colors.muted}. Sits above the keyboard-gallery at 32px vertical padding. No star rating, no review count — Leopold's direct sales model does not surface user-generated social proof at this position.

### Hero

**`hero`** — Full-width section on {colors.surface-soft} with headline in {typography.display-xl} and supporting description in {typography.body-md}. Product image sits right of text in a two-column split on desktop; stacks below on mobile. No gradient overlay, no full-bleed photographic background — the image is always isolated on a clean field so finish and keycap detail read clearly. CTA is a single button-primary.

### Search

**`search-bar`** — A rectangular input at {rounded.xs} on {colors.surface-soft} with a magnifier icon at {colors.muted} on the right side. Border upgrades from {colors.hairline} to {colors.primary} on focus. No pill shape, no animation beyond the border transition. Sits inline in the nav-bar on desktop; on mobile collapses to an icon that expands to a full-width overlay input.

### Footer

**`footer`** — Dark {colors.ink} background with {typography.body-sm} link columns in {colors.muted-soft}. Links shift to {colors.on-dark} on hover. Four columns on desktop: Products, Support, Company, Region Selector. No brand color appears in the footer — the dark field alone provides contrast separation. No newsletter signup or social icon grid; the footer is a navigation index, not a marketing surface.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero stacks vertically with image below text; spec-table runs full-width with label/value stacking on < 375px; switch-selector tiles wrap to two columns; keyboard-gallery thumbnails scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; nav shows abbreviated category labels; hero maintains split layout at reduced padding; spec-table uses 55/45 label-value column split |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all category links visible; hero at full two-column split; spec-table full-width with comfortable row padding |
| Wide | > 1440px | Max-width 1280px container centered; product grid optionally four columns; hero image scales in proportion; no additional layout changes |

### Touch Targets

- All buttons maintain a minimum 44px height across breakpoints
- Color swatches expand to 32×32px on mobile with gap preserved at 4px
- Switch-selector tiles pad to at least 44px tall on mobile for reliable tap registration
- Nav hamburger is a 44×44px touch target with no sub-pixel trim
- Category-nav tabs on mobile scroll with 16px horizontal padding so first/last items have clear affordance

### Collapsing Strategy

- Category nav collapses to a horizontally scrollable strip on mobile — no truncation, no overflow clipping
- Spec table stays full-width on all breakpoints; label and value stack vertically only below 375px
- Keyboard gallery thumbnails shift from a fixed row to a horizontal scroll strip on mobile with snap points
- Footer four-column layout collapses to two columns on tablet, single column on mobile
- Search bar hides from the nav-bar on mobile and reveals as a full-width overlay triggered by an icon tap
- Hero image drops below the text column on mobile; aspect ratio is preserved at 4:3

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extractable from the live site — the site likely loads design tokens via JavaScript or has anti-bot protections blocking static extraction; the entire palette is inferred from brand knowledge and must be verified against the actual rendered site
- Font family stack is unconfirmed — system-ui with Noto Sans KR as Korean fallback is assumed based on common Korean DTC brand conventions; the actual web font (if any custom typeface is loaded) is unknown
- No meta theme-color was detected, so the mobile browser chrome color is unspecified
- The e-commerce platform is not Shopify; the likely platform (Cafe24, WooCommerce, or a custom Korean system) is unconfirmed and may impose its own checkout component constraints
- Exact button border-radius values are estimated at 4px; Leopold may use fully rectangular (0px) buttons — verify against computed styles
- Price display localization logic (KRW on the Korean site vs. USD/EUR on the global site) and currency formatting patterns are unknown
- Stock and availability states for individual switch variants per model are not documented — disabled swatch and out-of-stock overlay patterns require direct verification
- Switch availability matrix across models (not all switches available for all layouts) may require a dedicated filter/constraint UI pattern not captured here
