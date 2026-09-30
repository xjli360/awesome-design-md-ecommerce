---
version: alpha
name: "KTC"
source_url: "https://www.ktcplay.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep violet-magenta — #910582, a shade that most gaming display brands consign to accent highlights — anchors every primary CTA and interaction state across KTC's interface, an unusual choice that separates the brand from the electric-blue-and-RGB pack without signaling aggression. The near-blacks #1d2129 and #1d1d1d carry primary surfaces and navigation with a density suited to high-performance monitor marketing: hardware expected to run in darkened rooms and compete on spec sheets. Against those grounds, the magenta reads with gemstone specificity rather than system-default urgency. Body copy runs a Chinese/Western hybrid stack — PingFang SC and Microsoft YaHei for mainland legibility, Helvetica Neue and Arial as Latin fallbacks, with MiSans-Normal as a quality-signal first choice that mainland users associate with Xiaomi's premium ecosystem. Corner radii are deliberately contained: product cards and primary buttons hold {rounded.sm} to {rounded.md}, resisting the pill shapes common in lifestyle consumer electronics and landing closer to the engineering-adjacent register that display hardware earns. Error, success, and link semantics follow the Element Plus palette exactly — #f56c6c for danger, #67c23a for success, #409eff for informational states — which reveals a Vue-based front-end and keeps interaction patterns consistent for developers extending the system. Light surfaces use a warm near-white (#efebeb) alongside a neutral #f5f5f5, giving product imagery a slightly warmer ground than cold white would. Spec-heavy sections — resolution callouts, refresh-rate badges, panel-tech comparisons — exploit the generous {spacing.section} rhythm, letting numbers like "4K 144Hz" or "1ms GTG" breathe as standalone claims rather than cramming into a feature list. The footer and navigation compress to a #282626 ground, keeping the brand's dark register consistent from header to base and reinforcing that KTC addresses an audience that already lives in dark-mode environments.

colors:
  primary: "#910582"
  primary-active: "#720068"
  primary-disabled: "#d4a0d0"
  error: "#f56c6c"
  error-active: "#c45656"
  error-light: "#fef0f0"
  success: "#67c23a"
  link: "#409eff"
  ink: "#1d1d1d"
  ink-dark: "#1d2129"
  body: "#4a5565"
  muted: "#909399"
  hairline: "#dcdfe6"
  hairline-soft: "#e4e7ed"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-warm: "#efebeb"
  surface-card: "#ffffff"
  surface-dark: "#1d2129"
  surface-darkest: "#282626"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'MiSans-Normal', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'MiSans-Normal', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'MiSans-Normal', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'MiSans-Normal', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'MiSans-Normal', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'MiSans-Normal', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'MiSans-Normal', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'MiSans-Normal', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'MiSans-Normal', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  spec-value:
    fontFamily: "'MiSans-Normal', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  spec-unit:
    fontFamily: "'MiSans-Normal', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  spec-label:
    fontFamily: "'MiSans-Normal', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'MiSans-Normal', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'MiSans-Normal', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    border: "1px solid {colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.surface-dark}"
    logoAccent: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.md}"
    padding: 24px
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    hoverBorder: "1px solid {colors.primary}"
    imageBg: "{colors.surface-soft}"
  hero-banner:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.title-lg}"
    subtitleColor: "{colors.muted}"
    minHeight: 560px
    paddingVertical: 64px
    paddingHorizontal: 48px
    accentBar: "3px solid {colors.primary}"
  spec-callout:
    backgroundColor: "{colors.surface-dark}"
    valueTypography: "{typography.spec-value}"
    valueColor: "{colors.primary}"
    unitTypography: "{typography.spec-unit}"
    unitColor: "{colors.muted}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: 32px 24px
    borderLeft: "3px solid {colors.primary}"
  spec-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  tag-new:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  tag-featured:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  model-selector:
    backgroundColor: "{colors.surface-soft}"
    borderBottom: "2px solid {colors.hairline}"
    activeTabBorder: "2px solid {colors.primary}"
    activeTabColor: "{colors.primary}"
    inactiveTabColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    height: 48px
  spec-table:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    headerBg: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    headerColor: "{colors.body}"
    cellTypography: "{typography.body-sm}"
    cellColor: "{colors.ink}"
    altRowBg: "{colors.surface-warm}"
    rounded: "{rounded.sm}"
  comparison-highlight:
    backgroundColor: "{colors.surface-dark}"
    rounded: "{rounded.md}"
    padding: 32px
    border: "1px solid {colors.primary}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.on-dark}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-dark}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    textColor: "{colors.on-dark}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.muted}"
    height: 40px
  footer:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.muted}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    paddingVertical: 48px
    paddingHorizontal: 64px
    borderTop: "1px solid {colors.surface-dark}"

## Components

### Buttons

**`button-primary`** — The primary action button fills with KTC's #910582 magenta against white text, with `{rounded.sm}` corners that sit firmly in the functional register rather than the lifestyle-soft pill end of the spectrum. Hover state deepens to `{colors.primary-active}` (#720068); disabled washes to `{colors.primary-disabled}`, a desaturated lavender that communicates unavailability without disappearing. Used for all purchase-intent CTAs — "Buy Now," "Add to Cart," and spec-sheet download triggers.

**`button-secondary`** — Canvas fill with a `{colors.hairline}` border and `{colors.body}` text handles secondary actions like "Learn More" or "Compare Models." Paired alongside `button-primary` in two-action rows, it recedes without vanishing. Height matches primary at 44px so the two buttons sit flush in the same row.

**`button-ghost`** — Transparent background with a `{colors.primary}` magenta border and matching text label. Used for optional or exploratory actions — "View All Models," filter toggles, series navigation — where a filled button would misrepresent the action's weight. Shares `{rounded.sm}` and height with the other button variants for visual consistency.

### Navigation

**`nav-bar`** — A `{colors.surface-darkest}` (#282626) ground with white nav-link typography creates a clean dark envelope that persists above both light product pages and dark hero sections. The KTC wordmark carries a `{colors.primary}` magenta accent element. At 64px height the bar is compact relative to the hero imagery below it. A subtle `{colors.surface-dark}` bottom border separates the bar from page content without a harsh line.

### Product Card

**`product-card`** — White surface with a `{colors.hairline-soft}` border that upgrades to a full `{colors.primary}` magenta outline on hover, providing a clear focus affordance without disrupting the page grid. Monitor names in `{typography.title-md}` support both Chinese and Latin characters at equal weight. `spec-badge` elements float over the product image in the upper corner, calling out key specs like "4K" or "165Hz" in magenta fills. Cards carry `{rounded.md}` corners at 12px.

### Hero

**`hero-banner`** — Full-bleed `{colors.surface-darkest}` section with a 3px `{colors.primary}` accentBar running along the left edge of the headline block. The primary headline uses `{typography.display-xl}` at 48px/700 in white; the subheadline steps to `{typography.title-lg}` in `{colors.muted}`. Minimum height of 560px reserves room for key-art photography of the featured panel. A single `button-primary` CTA anchors the bottom-left of the text column.

### Spec Callout

**`spec-callout`** — Dark `{colors.surface-dark}` tile with a 3px `{colors.primary}` left-edge accent bar. The metric value — "165," "4," "1" — renders in `{typography.spec-value}` at 36px/700 in magenta; the unit ("Hz," "K," "ms") in `{typography.spec-unit}`; and the descriptor ("Refresh Rate," "Resolution," "Response Time") in all-caps `{typography.spec-label}` in `{colors.muted}`. Four to six callouts tile horizontally across a product page break, replacing a paragraph of features with a scan-first grid.

### Badges and Tags

**`spec-badge`** — Compact magenta chip with `{rounded.xs}` corners and white `{typography.badge}` text. Floats over product card images and hero imagery to announce standout technical claims. **`tag-new`** uses `{colors.error}` (#f56c6c) fill for recently launched SKUs — the red-to-magenta shift signals newness without the two tags visually competing when both appear on the same card. **`tag-featured`** shares the magenta fill of `spec-badge` for editorially selected models.

### Model Selector

**`model-selector`** — Horizontal tab strip in `{colors.surface-soft}` with a full-width 2px bottom border in `{colors.hairline}`. The active tab overrides that border with `{colors.primary}` magenta at the same 2px weight, and the tab label shifts from `{colors.muted}` to magenta. Used to navigate between size variants (24 inch, 27 inch, 32 inch) or resolution tiers on listing and detail pages. Tab height of 48px meets minimum touch target requirements on mobile.

### Spec Table

**`spec-table`** — Two-column or multi-column technical table. The header row sits on `{colors.surface-soft}` with all-caps `{typography.spec-label}` labels in `{colors.body}`. Data rows alternate between `{colors.canvas}` and `{colors.surface-warm}` (#efebeb) — the warm tint is subtle enough to avoid visual noise across the full panel specification list while preserving row distinction. A `{rounded.sm}` outer radius softens the table boundary within a detail page.

### Comparison Highlight

**`comparison-highlight`** — Dark `{colors.surface-dark}` card with a full `{colors.primary}` border, reserved for the "Recommended" or "Best Value" unit in side-by-side comparison grids. The full-perimeter magenta border does the editorial work of a badge without adding a floating element — it makes one card visually prior to its neighbors purely through border weight and color. Title renders in white `{typography.title-md}`; supporting copy in `{colors.muted}` `{typography.body-sm}`.

### Search

**`search-bar`** — Dark `{colors.surface-dark}` background with a `{colors.hairline}` border that flips to `{colors.primary}` on focus, consistent with the `text-input` focus ring. Placeholder and icon both render in `{colors.muted}`; active input text in `{colors.on-dark}`. Lives inside the nav at desktop widths and expands to a full-width top-of-listing filter row on mobile.

### Footer

**`footer`** — Matches the nav's `{colors.surface-darkest}` (#282626) ground, creating a dark envelope that brackets the page. Navigation links render in `{colors.hairline}` gray and elevate to `{colors.primary}` magenta on hover, so the brand's primary color reappears as the footer's only interactive signal. All footer typography uses `{typography.body-sm}`. A single `{colors.surface-dark}` top border provides a clean separation from the last content section.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero reduces to 320px min-height with stacked text; spec callouts compress to horizontal snap-scroll row (2 visible, third peeking); nav collapses to hamburger with full-screen dark overlay; spec tables scroll horizontally with sticky first column |
| Tablet | 744–1128px | Two-column product grid; hero holds 440px min-height with text/image side-by-side; spec callouts in 3-column grid; model-selector tabs scroll if overflow |
| Desktop | 1128–1440px | Three-column product grid; hero at full 560px; spec callouts in 4–6 column row; nav fully expanded with all primary links visible |
| Wide | > 1440px | Content max-width caps at 1440px centered; hero background extends full-bleed while text column stays constrained; 4-column product grid maximum |

### Touch Targets

- All buttons, tabs, and card interactive areas maintain a minimum 44×44px tap target
- Model-selector tabs expand to 48px height on mobile for thumb-friendly switching
- Spec callout tiles link to anchor sections; full tile is tappable at minimum 48px height
- Footer links spaced at minimum 24px vertical gap to prevent mis-taps on dense link columns
- Search bar height increases from 40px to 44px on mobile breakpoints

### Collapsing Strategy

- Nav primary links collapse into hamburger below 1128px; dark full-screen overlay maintains brand register
- Hero text/image layout switches from side-by-side to stacked below 744px; headline scales from `{typography.display-xl}` (48px) to `{typography.display-md}` (32px)
- Spec callout row converts to horizontally scrollable snap-scroll container on mobile showing 2 tiles with a third partially visible
- Product card image area reduces from 240px to 160px on mobile while badge overlays remain
- Comparison highlight cards stack vertically on mobile; the recommended card is pinned to the top of the stack
- Spec table wraps to a single-column definition-list layout below 480px as an alternative to horizontal scroll

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom KTC typeface detected; MiSans-Normal appears in the font stack but may be loaded via a CDN not captured in static extraction — confirm whether a licensed brand typeface exists separate from the Xiaomi/HarmonyOS MiSans release
- Primary color #910582 confirmed from extraction but no CSS custom property names were recovered; token naming conventions for the live codebase are inferred
- Dark-mode specifics unclear — the dark surfaces (#1d2129, #282626) may be section-level background choices rather than a system-level dark theme toggle; requires dynamic rendering to verify
- The blue spectrum (#007aff through #ecf5ff) and error reds (#f56c6c through #fef0f0) and success greens (#67c23a through #e1f3d8) match Element Plus component defaults exactly; these are likely UI-framework tokens, not brand-authored colors, and should not be treated as brand palette
- No shadow or elevation system detected; box-shadow values for cards, modals, and dropdowns should be measured from live DevTools
- Animation and transition timings for hover states, page transitions, and scroll-triggered reveals not captured in static extraction
- Logo safe-area padding, minimum reproduction size, and clear-space rules not available from extraction
- Explicit CSS grid column count and gutter width not confirmed; column counts above are inferred from monitor-brand conventions and the 1440px content-width pattern common in Chinese tech hardware brands
