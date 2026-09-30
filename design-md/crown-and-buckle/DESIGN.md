---
version: alpha
name: "Crown & Buckle"
source_url: "https://www.crownandbuckle.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Gold hardware against warm cream — #c59529 sits at the center of Crown & Buckle's palette the way a gilt buckle clasp catches light on a leather deployant. The brand runs its entire visual language through this amber-gold primary: hover states, price callouts, active nav underlines, and the occasional badge all reach for that same warm metal tone before anything else. The canvas is never pure white; instead #eeebe4, a slightly toasted off-white, reads like aged linen or unbleached cotton — exactly the material a high-quality strap arrives wrapped in. Beneath it sits #f4ebd7, a deeper parchment used for surface differentiation without introducing cold gray. The near-black ink at #231f20 carries a brownish warmth that avoids the harshness of true black, reinforcing a brand that positions itself in the horological enthusiast space rather than the mass-market segment. A rust accent at #a72d0a handles error states and clearance callouts — it reads as patina rather than alarm. Type is set in Proxima Nova for display and interface work, falling back to Open Sans and Helvetica Neue; the stack skews humanist and slightly editorial, consistent with a catalog-driven retailer whose product photography does heavy lifting. Rounded corners are minimal — buttons and inputs use modest {rounded.xs} to {rounded.sm} values that read as precise and machined rather than soft and consumer. The overall spatial rhythm is generous: product grids breathe, filter panels collapse cleanly, and strap detail pages stack specifications in tight monospaced type against the cream ground, evoking a watchmaker's reference card more than a typical accessories e-commerce layout.

colors:
  primary: "#c59529"
  primary-active: "#a57c1e"
  primary-disabled: "#e8d49a"
  primary-text-on-light: "#8a6818"
  accent-rust: "#a72d0a"
  accent-rust-active: "#8a2408"
  ink: "#231f20"
  body: "#404040"
  muted: "#716468"
  muted-soft: "#777777"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  border-mid: "#bbbbbb"
  canvas: "#eeebe4"
  surface-parchment: "#f4ebd7"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-strong: "#e8e8e8"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#e02b27"
  disabled-text: "#aeaeae"
  price-special: "#a72d0a"

typography:
  display-xl:
    fontFamily: "'proxima-nova', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'proxima-nova', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'proxima-nova', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'proxima-nova', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'proxima-nova', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'proxima-nova', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-nova', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-nova', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  spec-mono:
    fontFamily: "Consolas, Menlo, Monaco, 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'proxima-nova', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'proxima-nova', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'proxima-nova', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.4px
  label-uppercase:
    fontFamily: "'proxima-nova', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price-display:
    fontFamily: "'proxima-nova', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 14px 28px
    height: 48px
    states:
      hover:
        backgroundColor: "{colors.primary-active}"
      disabled:
        backgroundColor: "{colors.primary-disabled}"
        textColor: "{colors.disabled-text}"

  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 12px 26px
    height: 48px
    states:
      hover:
        borderColor: "{colors.primary}"
        textColor: "{colors.primary}"

  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px

  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 52px
    width: 100%
    states:
      hover:
        backgroundColor: "{colors.primary-active}"

  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.border-mid}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    states:
      focus:
        borderColor: "{colors.primary}"
        outline: "2px solid {colors.primary-disabled}"
      error:
        borderColor: "{colors.error}"

  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    activeIndicator:
      color: "{colors.primary}"
      style: "2px bottom border"

  mega-menu:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.xxl}"
    categoryHeader:
      typography: "{typography.label-uppercase}"
      textColor: "{colors.primary}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "1 / 1"
    padding: "{spacing.base}"
    productName:
      typography: "{typography.title-sm}"
      textColor: "{colors.ink}"
    price:
      typography: "{typography.price-display}"
      textColor: "{colors.ink}"
    priceSpecial:
      textColor: "{colors.price-special}"
    swatchRow:
      marginTop: "{spacing.sm}"
      dotSize: 14px
      rounded: "{rounded.full}"
      gap: "{spacing.xs}"

  swatch-selector:
    activeRing: "2px solid {colors.primary}"
    inactiveRing: "1px solid {colors.border-mid}"
    size: 20px
    rounded: "{rounded.full}"
    gap: "{spacing.xs}"

  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    states:
      selected:
        backgroundColor: "{colors.ink}"
        textColor: "{colors.on-dark}"
        borderColor: "{colors.ink}"
      outOfStock:
        textColor: "{colors.disabled-text}"
        textDecoration: line-through

  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.border-mid}"
    activeColor: "{colors.ink}"

  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  badge-sale:
    backgroundColor: "{colors.accent-rust}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    minHeight: 480px
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    imagePosition: right 60%
    overlayPadding: "{spacing.xxl}"
    cta:
      component: button-primary

  filter-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    width: 240px
    borderRight: "1px solid {colors.hairline}"
    sectionHeader:
      typography: "{typography.label-uppercase}"
      textColor: "{colors.muted}"
      paddingBottom: "{spacing.sm}"
      borderBottom: "1px solid {colors.hairline}"
    optionTypography: "{typography.body-sm}"
    activeCheckmarkColor: "{colors.primary}"

  spec-table:
    backgroundColor: "{colors.surface-parchment}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    keyTypography: "{typography.label-uppercase}"
    keyColor: "{colors.muted}"
    valueTypography: "{typography.spec-mono}"
    valueColor: "{colors.ink}"
    rowPadding: "{spacing.sm} {spacing.base}"
    rowBorder: "1px solid {colors.hairline}"

  pagination:
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    itemSize: 36px

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.surface-strong}"
    headingTypography: "{typography.label-uppercase}"
    headingColor: "{colors.primary}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons
**`button-primary`** — Gold-filled (#c59529) with white label in uppercase Proxima Nova at 0.8px tracking; sits at 48px tall with `{rounded.xs}` corners that read as machined rather than soft. Hover darkens to #a57c1e. Disabled state washes gold to #e8d49a with gray label. Used exclusively for add-to-cart, checkout proceed, and primary filtering actions.

**`button-secondary`** — Transparent field, near-black border and label at full weight; transitions border and text to gold on hover, maintaining the brand's gold-first interaction language without filling the background. Preferred for secondary CTAs like "View Details" or "Save to Wishlist."

**`button-ghost`** — Single-pixel gold border, gold text, 36px height. Used inline in product cards and comparison panels where space is tight. Matches the low-weight editorial feel of specification blocks.

**`button-add-to-cart`** — Full-width variant of `button-primary` at 52px, mounted below the size selector. Only appears at full opacity when a strap length and width are selected; otherwise renders disabled state.

### Inputs & Selectors
**`text-input`** — White fill, mid-gray border at rest; focus ring draws a soft gold outline using #e8d49a at 2px with the inner border snapping to #c59529. Error states switch to #e02b27 border. Height 44px with `{rounded.xs}`.

**`swatch-selector`** — 20px dots in `{rounded.full}`, inactive ringed in #bbbbbb, active ringed in gold at 2px with a 1px gap between ring and dot. Swatches represent strap colorways; out-of-stock dots carry a gray diagonal strike.

**`size-selector`** — Strap width options (16mm, 18mm, 20mm, 22mm) rendered as square pill buttons with `{rounded.xs}`. Selected state inverts to near-black fill with white label — the only place the brand uses near-black as an active fill rather than an outline.

### Navigation
**`nav-bar`** — White bar at 64px with bottom hairline; logo sits left in #231f20. Nav links in uppercase 14px/0.4px tracking; the active category gets a 2px gold underline rather than fill or bold. A persistent search icon right-side leads to an expanding input field.

**`mega-menu`** — Drops full-width below the nav with white fill. Category headers render in `{typography.label-uppercase}` at #c59529, beneath which subcategory links sit in `{typography.nav-link}` at body weight. A product highlight panel on the right shows a featured strap with image and gold CTA.

### Product Display
**`product-card`** — Square-image card with no border-radius; border is a thin #dedede line that fades on hover as a light box-shadow appears. Product name in `{typography.title-sm}`, price in `{typography.price-display}`. Sale pricing stacks original (struck, muted) above discounted (#a72d0a). Swatch dots appear below price when multiple colorways exist.

**`spec-table`** — Rendered on product detail pages against the parchment surface (#f4ebd7), this component displays lug width, length, thickness, and hardware finish in monospaced type. Keys in uppercase gray label, values in Consolas mono at 12px. The table reads as a technical datasheet and is the most distinctive layout element in the brand.

**`hero-banner`** — Canvas-toned background (#eeebe4) with right-biased strap photography; headline in `{typography.display-xl}` at 700 weight, body copy in `{typography.body-md}` at modest width (~540px). The cream field behind the text requires no scrim. A single gold `button-primary` anchors the CTA.

### Utility & Chrome
**`filter-sidebar`** — 240px fixed panel in #f6f6f6 with category sections separated by hairline rules. Section headers in `{typography.label-uppercase}` at #716468, options in `{typography.body-sm}`. Active filters checked in gold. Collapses to an off-canvas drawer on mobile behind a "Filter" trigger.

**`breadcrumb`** — Caption-scale in #716468, separated by forward slashes in #bbbbbb. The current page name renders in #231f20 without link underline. Sits below the nav bar at `{spacing.sm}` top padding.

**`footer`** — Near-black (#231f20) footer with a 3px gold top border as the primary brand moment. Section headings in `{typography.label-uppercase}` at #c59529; link columns in `{typography.body-sm}` at #e8e8e8. Newsletter input sits in a white field with gold submit button.

**`pagination`** — Row of 36px square controls; active page fills gold, numerals render in `{typography.button-sm}`. Prev/Next arrows flank the number row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter sidebar becomes off-canvas drawer triggered by sticky filter bar; nav collapses to hamburger; hero stacks text above image; spec-table scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; filter sidebar visible as collapsible accordion above grid rather than fixed side panel; mega-menu drops to single-column list |
| Desktop | 1128–1440px | Three-column product grid with fixed 240px filter sidebar; mega-menu at full width with category columns and featured panel |
| Wide | > 1440px | Grid max-width caps at 1440px with auto side margins; hero banner image extends full-bleed while text column stays within content column |

### Touch Targets
- All swatches and size selectors minimum 44×44px on mobile regardless of displayed dot/button size
- Nav hamburger icon minimum 48×48px tap zone
- Filter accordion headers minimum 48px tall
- Pagination controls minimum 44×44px

### Collapsing Strategy
- Filter sidebar collapses to a fixed bottom bar ("Filter | Sort") on mobile; tapping opens a full-screen overlay
- Mega-menu becomes standard accordion in the hamburger drawer
- Spec-table on mobile: allow horizontal scroll within a contained scroll region, do not reflow to definition lists
- Product card swatches hide beyond 5 colorways with a "+N" overflow indicator
- Breadcrumb truncates middle segments with ellipsis on viewports below 480px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Custom typeface weight and variant details for Proxima Nova not extractable from CSS alone; weights assumed from visual inspection (400, 600, 700)
- No explicit design token file or CSS custom properties exposed — all values inferred from computed styles and extracted hex dump
- Icon system (luma-icons, pagebuilder-font) is Magento Luma theme default; brand-custom icon set, if any, was not resolvable from extraction
- Motion and animation timings (hover transitions, drawer animation curves) not captured
- Exact product image background treatment (pure white vs. warm light) not confirmed from extraction alone
- Mobile navigation interaction details (sticky behavior, scroll behavior of filter bar) inferred from category structure, not observed
- Dark mode or alternate theme presence not confirmed; no `prefers-color-scheme` tokens found in extraction
