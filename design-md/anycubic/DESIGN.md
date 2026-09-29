---
version: alpha
name: "Anycubic"
source_url: "https://www.anycubic.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every color token in Anycubic's extracted palette maps almost perfectly to Element UI's default Vue component theme — #409eff as primary, a stepped gray scale running #c0c4cc / #909399 / #606266 / #303133, and semantic status tokens in danger-red (#f56c6c), warning-amber (#e6a23c), and success-green (#67c23a) — which places the brand's visual identity in product photography and layout density rather than a bespoke color language. The electric blue at #409eff reads as generous and pragmatic rather than corporate: it carries every primary CTA, filter-active state, and in-page link without modification, sitting cleanly against both the white-canvas product grid and the near-black workshop darks (#1a1a1a, #303133) that frame hero sections. MiSans appears in the font stack — a Chinese sans-serif released by Xiaomi that signals Shenzhen maker-community roots while preserving Latin legibility — falling back through Helvetica Neue and system-ui for non-CJK environments. No proprietary display typeface was pulled from CSS; the brand trusts hardware credibility and competitive pricing over editorial font investment.

  The layout vocabulary is grid-forward and utilitarian: product listing pages run four-column card arrays at desktop, collapse to two columns at tablet, and go single-column on mobile with no intermediate lazy-design breaks. Buttons carry a modest 4px radius (`{rounded.sm}`) and nothing reaches pill territory — establishing an engineering-product UX register rather than fashion or lifestyle retail. Surface hierarchy is deliberately quiet: #f5f7fa for page backgrounds, #ffffff for product cards, #f2f6fc for nested filter panels, #ebeef5 for divider zones in settings screens. Status semantics borrowed from Element UI run throughout the product catalog: "New" and "Best Seller" badges in success-green (#67c23a), clearance alerts in danger-red (#f56c6c), and low-stock warnings in amber (#e6a23c). These four semantic hues — primary blue, success green, warning amber, danger red — constitute the entire interactive color vocabulary; everything else is a gray or a white.

  Hero sections break from the off-white grid entirely: full-bleed dark panels at #1a1a1a hold product renders on controlled gradients that fade from the machine's casing color into black, achieving a CAD-visualization aesthetic that lets hardware geometry read as sculpture. CTAs in dark hero zones still render the same #409eff button, keeping single-color CTA coherence across light and dark contexts. The "For Freedom to Make" headline lands more as a maker-movement rallying phrase than a lifestyle aspiration, which the system's matter-of-fact color logic reinforces — nothing here is decorative for its own sake.

colors:
  primary: "#409eff"
  primary-hover: "#3a8ee6"
  primary-active: "#337aff"
  primary-light: "#ecf5ff"
  primary-disabled: "#a0cfff"
  disabled: "#c0c4cc"
  ink: "#1a1a1a"
  body: "#303133"
  dark-ink: "#444444"
  muted: "#606266"
  muted-soft: "#909399"
  hairline: "#dcdfe6"
  hairline-soft: "#e4e7ed"
  hairline-muted: "#ebeef5"
  canvas: "#ffffff"
  surface-soft: "#f5f7fa"
  surface-card: "#ffffff"
  surface-page: "#f5f5f5"
  surface-panel: "#f2f6fc"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  hero-bg: "#1a1a1a"
  hero-bg-alt: "#303133"
  danger: "#f56c6c"
  danger-dark: "#dd6161"
  success: "#67c23a"
  success-dark: "#5daf34"
  warning: "#e6a23c"
  warning-dark: "#cf9236"

typography:
  display-xl:
    fontFamily: "'MiSans', 'Helvetica Neue', Helvetica, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'MiSans', 'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'MiSans', 'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'MiSans', 'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'MiSans', 'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'MiSans', 'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'MiSans', 'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'MiSans', 'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'MiSans', 'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0
  button-sm:
    fontFamily: "'MiSans', 'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0
  badge:
    fontFamily: "'MiSans', 'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'MiSans', 'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'MiSans', 'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'MiSans', 'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    height: 36px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.disabled}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
    padding: 9px 19px
    height: 36px
  button-secondary-hover:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 9px 19px
    height: 36px
  button-ghost-hover:
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  button-sm-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 28px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 0 12px
    height: 40px
  text-input-focus:
    border: "1px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "1px solid {colors.danger}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-link-hover:
    textColor: "{colors.primary}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
    rowHoverBackground: "{colors.surface-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    hoverBoxShadow: "0 4px 16px rgba(0,0,0,0.10)"
  product-card-name:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-price-original:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-soft}"
    textDecoration: line-through
  hero-dark:
    backgroundColor: "{colors.hero-bg}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    paddingVertical: "{spacing.section}"
  hero-dark-alt:
    backgroundColor: "{colors.hero-bg-alt}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-md}"
    subheadTypography: "{typography.body-md}"
  badge-new:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-bestseller:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
  category-pill-active:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 14px
    border: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
    padding: 0 12px
    iconColor: "{colors.muted-soft}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    headerBackground: "{colors.surface-page}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    cellPadding: "10px 16px"
    rounded: "{rounded.md}"
  price-tag-current:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  price-tag-original:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-soft}"
    textDecoration: line-through
  price-tag-savings:
    typography: "{typography.badge}"
    textColor: "{colors.danger}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.body}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.muted-soft}"
  pagination:
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    hoverBackground: "{colors.surface-soft}"
  footer:
    backgroundColor: "{colors.hero-bg}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.disabled}"
    linkHoverColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    dividerColor: "{colors.hero-bg-alt}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Renders in #409eff with white text, 4px radius (`{rounded.sm}`), and 36px height; it is the identical button whether it sits on a white product-grid background or inside a dark hero panel. Hover shifts to #3a8ee6 (`{colors.primary-hover}`) and active press lands at #337aff (`{colors.primary-active}`), providing perceptible feedback without animation delay. Disabled state uses a washed-out #ecf5ff background with #c0c4cc text and `cursor: not-allowed`, matching Element UI's disabled-button convention exactly.

**`button-secondary`** — Outlined at #409eff border over a transparent background, same 36px height as primary. On hover the fill shifts to a very light #ecf5ff tint while the border persists — matching Element UI's outlined-button hover. Used for secondary CTAs such as "Add to Wishlist" or "Compare Models."

**`button-ghost`** — Neutral #dcdfe6 border with #606266 muted text and no background fill. On hover the border and text switch to #409eff primary. Used for low-emphasis actions (clear filters, close modal) where the blue would imply undue weight.

### Inputs and Search

**`text-input`** — 40px height, 4px radius, #dcdfe6 border that transitions to #409eff on focus with no shadow ring — clean Element UI input behavior. Placeholder text at #909399 reads comfortably against the white field. Error state swaps the border to danger-red (#f56c6c) with no icon, relying on color alone.

**`search-bar`** — Mirrors `text-input` geometry with a magnifier icon prepended at 16px left inset; icon color at #909399 (`{colors.muted-soft}`). Sits in the top navigation bar at desktop; collapses to a full-width row below the nav on mobile. Active state shows a blue border and the icon color inherits primary.

### Navigation

**`nav-bar`** — 64px tall, white background, bottom hairline at #dcdfe6. Logo anchors left; category links run center at desktop; search, cart, and account icons sit right. The active category link shows a 2px #409eff underline. On scroll past 64px the bar sticks with the same white background and hairline border — no shadow or elevation transition.

**`nav-dropdown`** — Appears on category hover as a white panel with 8px radius (`{rounded.md}`), `0 4px 12px rgba(0,0,0,0.08)` shadow, and a thin #e4e7ed border. Body typography at 14px / 400-weight; hovered rows fill with #f5f7fa surface-soft. Closes on outside click or Escape.

### Product Cards

**`product-card`** — White card, 8px radius (`{rounded.md}`), thin #e4e7ed border, `0 4px 16px rgba(0,0,0,0.10)` shadow on hover. Product image fills the top ~60% of the card at 1:1 aspect ratio. Below: product name at 16px/600 (`{typography.title-md}` in ink), price at 22px/700 (`{typography.price-display}`), and an "Add to Cart" primary button spanning full card width. Discount pricing shows the original price in muted-gray with a line-through immediately adjacent to the current price. Status badges overlay the image top-left corner as absolute-positioned chips.

### Hero

**`hero-dark`** — Full-bleed section at #1a1a1a; headline at 40px/700 white (`{typography.display-xl}`), subhead at 22px/600 (`{typography.display-sm}`). Product renders are composited on a gradient mask that fades from the printer's body color to black at the bottom edge, letting hardware geometry read as the primary visual. A single #409eff CTA button sits below the subhead. Vertical padding is 64px (`{spacing.section}`) above and below the content block.

**`hero-dark-alt`** — Same structure as `hero-dark` but at #303133 background; used for sub-brand or promotional sections where full black would be too stark.

### Spec Table

**`spec-table`** — Two-column table with 8px outer radius (`{rounded.md}`) and a full #dcdfe6 outer border. Left column holds spec labels at 13px/500 muted-gray (`{typography.spec-label}`, `{colors.muted}`); right column holds values at 13px/400 body-color. Alternating rows use #f5f7fa and #ffffff for light zebra striping. Cell padding 10px vertical, 16px horizontal.

### Category Filters

**`category-pill`** — Small chips used in sidebar filter panels and inline filter rows above product grids. Inactive: #f5f7fa background, body-text color, #dcdfe6 border, 4px radius (`{rounded.sm}`). Active: #ecf5ff background (`{colors.primary-light}`), #409eff text and border — the Element UI primary-light tag treatment. Minimum 32px height for touch usability.

### Badges

**`badge-new`** and **`badge-bestseller`** — Both render in success-green (#67c23a) with white text, 2px radius (`{rounded.xs}`), 11px/600 label, 2px×6px padding. Positioned as absolute overlays at top-left of the product card image.

**`badge-sale`** — Danger-red (#f56c6c), otherwise identical geometry to success badges. Applied to clearance and time-limited promotional items.

**`badge-warning`** — Amber (#e6a23c) for "Low Stock" or estimated shipping delay notices. Same 11px/600 geometry.

### Price Tag

**`price-tag-current`** — 22px/700 ink (#1a1a1a); occupies its own typographic line. When a discount exists, the original price appears inline to its right at 13px/400 muted-gray with line-through, and a savings label in danger-red badge style appears below or inline depending on layout width.

### Footer

**`footer`** — Full-bleed #1a1a1a background to match hero section darks. Column layout with link lists at 14px/400 in #c0c4cc, hovering to white. Top border separator at #303133 (`{colors.hero-bg-alt}`). Contains a newsletter sign-up input (inherits `text-input` geometry but with a #444444 border and #e6e6e6 text on the dark background) and a social icon row. Copyright and legal caption at 12px / #909399.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; search drops below nav in a full-width row; hero headline reduces to display-sm (22px); spec table gains horizontal scroll |
| Tablet | 744–1128px | 2-column product grid; nav shows category icons without text labels; hero image shifts to right 40% of viewport; filter sidebar collapses to horizontal scrollable chip row above grid |
| Desktop | 1128–1440px | 4-column product grid; full nav with text labels and hover dropdowns; hero is 50/50 split text-left / render-right; spec table full-width in product detail layout |
| Wide | > 1440px | Grid constrained to 1440px max-width, centered; hero content area caps at 1200px; white gutters appear on either side |

### Touch Targets

- All buttons minimum 36px rendered height; touch-sensitive zones extend to 44px via transparent padding
- Category pill chips minimum 32px height on mobile
- Nav icon buttons (cart, account, search) are 44×44px tap areas even when the visual icon is 24px
- Product card "Add to Cart" button spans full card width on mobile for thumb reachability
- Text inputs minimum 44px height on mobile via additional top/bottom padding

### Collapsing Strategy

- Navigation hamburger opens a full-height off-canvas drawer containing the complete category tree; closes on outside tap or swipe-left
- Filter sidebar transforms to a horizontal scrollable chip row pinned above the product grid on tablet and mobile
- Product images maintain 1:1 aspect ratio at all breakpoints; column count adjusts
- Hero sections maintain full-bleed width; vertical padding reduces from 64px to 40px on mobile
- Spec tables gain `overflow-x: scroll` on mobile rather than wrapping values; row labels remain sticky at left

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface found in CSS; MiSans is in the font stack but weight variants (Light, Regular, Medium, Bold) and CJK subset coverage are unconfirmed
- Exact nav-bar height not extracted; 64px is estimated from Element UI's default layout patterns
- Dropdown animation timing and easing curves were not captured from CSS
- Dark hero gradient parameters (angle, color-stop positions, opacity) are undocumented — described as common practice for the 3D printer category
- No explicit breakpoint pixel values extracted; 744px and 1128px are inferred from grid-collapse behavior
- Icon set source not identified — no icon font URL or SVG sprite reference found in extraction
- Product image aspect ratio inferred as 1:1 but may vary by printer category (resin vs. FDM)
- Exact box-shadow values for product cards are estimated; no shadow design tokens were extractable
- Newsletter input dark-background treatment is inferred; exact border and text colors on dark footer are unconfirmed
- Mobile hamburger menu animation and drawer behavior not confirmed from extraction
