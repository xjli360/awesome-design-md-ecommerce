---
version: alpha
name: "QNAP"
source_url: "https://www.qnap.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep blue #3f3ec6 anchors the QNAP interface — not a friendly sky blue but a saturated, almost indigo tone that signals enterprise-grade reliability and data seriousness. This primary voltage appears on primary CTAs, navigation highlights, and key interactive elements, while a secondary accent of #1891e4 provides a cooler, more technical counterpoint for secondary actions and informational badges. The palette is unusually broad for a networking brand, drawing from extracted site colors that include #db0090 (a magenta accent likely for alerts or promotional badges), #094e7f (a deep navy for footer backgrounds or scrims), and #4ea7d3 (a muted cerulean for hover states or secondary information). The canvas is clean white (#ffffff) with hairline borders in #cacddb, a soft gray that keeps the interface airy despite the density of technical data. Typography relies on system fonts — the extracted declarations show FontAwesome and Bootstrap Icons for iconography, while body text defaults to the browser's sans-serif stack, suggesting a pragmatic approach where readability and performance trump typographic personality. Cards and containers use gentle rounding at {rounded.sm} (8px), with primary buttons at {rounded.md} (12px) — enough softness to feel modern without undermining the professional, hardware-focused identity. The layout prioritizes information density: product grids, specification tables, and download links sit in close proximity, with generous use of {spacing.section} (64px) to separate major content zones. The overall impression is of a brand that knows its audience wants speed, clarity, and reliability — the design gets out of the way, letting the deep blue #3f3ec6 and the technical content do the work.

colors:
  primary: "#3f3ec6"
  primary-active: "#2e3a96"
  primary-disabled: "#828282"
  ink: "#094e7f"
  body: "#4e4534"
  muted: "#828282"
  muted-soft: "#cacddb"
  hairline: "#cacddb"
  hairline-soft: "#e0dafe"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-magenta: "#db0090"
  accent-blue: "#1891e4"
  accent-teal: "#009ba5"
  accent-green: "#129800"
  accent-orange: "#e58741"
  accent-yellow: "#7d6505"
  accent-purple: "#67447e"
  accent-red: "#ff0022"
  scrim: "#094e7f"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.44
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
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
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  button-download:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    padding: 9px 13px
  text-input-error:
    border: "1px solid {colors.accent-red}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(9, 78, 127, 0.08)"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 0
    boxShadow: "0 4px 16px rgba(9, 78, 127, 0.12)"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
    border: "1px solid {colors.hairline-soft}"
    boxShadow: "0 1px 3px rgba(9, 78, 127, 0.06)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(9, 78, 127, 0.1)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "16/9"
  badge-new:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-featured:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-beta:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.canvas}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "2px solid {colors.hairline}"
  table-cell:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-list:
    typography: "{typography.body-sm}"
    spacing: "{spacing.sm}"
  spec-label:
    color: "{colors.muted}"
    fontWeight: 600
  spec-value:
    color: "{colors.body}"
  download-button-group:
    gap: "{spacing.sm}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.md} {spacing.base}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.md} {spacing.base}"
  tab-inactive-hover:
    color: "{colors.ink}"
    borderBottom: "2px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across QNAP's interface, rendered in the deep indigo #3f3ec6 with white text. On hover or active state, it shifts to #2e3a96 (primary-active) for a subtle darkening effect. Disabled buttons drop to #828282, a mid-gray that clearly signals non-interactivity. The button uses {rounded.md} (12px) for a modern, approachable feel, with 12px vertical and 24px horizontal padding at 44px height.

**`button-secondary`** — An outlined variant with a white fill and #3f3ec6 border and text. The 2px solid border maintains visual weight parity with the primary button. On hover, the border shifts to #2e3a96. This button is used for "Learn More" links, secondary actions in product cards, and cancel/back navigation.

**`button-ghost`** — A text-only button with no background or border, using #3f3ec6 text. It appears in navigation dropdowns, table row actions, and contextual menus. Padding is reduced to 12px horizontal for tighter integration with surrounding content.

**`button-download`** — A compact, high-density button colored #129800 (accent-green) for download actions — firmware updates, software packages, and documentation PDFs. It uses {typography.button-sm} at 36px height with 8px vertical padding, making it suitable for placement in product tables and spec lists alongside other metadata.

### Cards & Product Display
**`product-card`** — The primary container for QNAP's NAS models, expansion units, and accessories. A white card with a 1px #e0dafe border and subtle shadow (0 1px 3px rgba(9, 78, 127, 0.06)). On hover, the shadow deepens and the border shifts to #cacddb, providing clear interactive feedback. The card image area uses a 16:9 aspect ratio with {rounded.sm} (8px) corners. Content padding is 16px, consistent with {spacing.base}.

**`badge-new`**, **`badge-sale`**, **`badge-featured`**, **`badge-beta`** — A family of small, uppercase badges that communicate product status at a glance. Each uses a distinctive accent color: #db0090 (magenta) for new products, #ff0022 (red) for sales/promotions, #1891e4 (blue) for featured items, and #009ba5 (teal) for beta releases. Badges are 11px bold uppercase with 2px vertical and 8px horizontal padding, using {rounded.xs} (4px) for a crisp, technical appearance.

### Navigation
**`nav-bar`** — A 64px white header with a 1px bottom border in #e0dafe. Navigation links use 15px medium-weight text in #094e7f (ink). On scroll, the nav gains a subtle shadow (0 2px 8px rgba(9, 78, 127, 0.08)) for visual separation from page content. Dropdown menus use a white background with 8px vertical padding and a more pronounced shadow (0 4px 16px rgba(9, 78, 127, 0.12)).

**`tab-active`** / **`tab-inactive`** — Tab navigation used in product detail pages, support sections, and account dashboards. The active tab displays a 2px bottom border in #3f3ec6 with matching text color. Inactive tabs use #828282 text with no border, shifting to #094e7f on hover with a #cacddb underline. Tabs have 12px vertical and 16px horizontal padding.

### Forms & Inputs
**`text-input`** — Standard text fields for search, login, and contact forms. A white input with 1px #cacddb border and {rounded.sm} (8px) corners at 44px height. On focus, the border thickens to 2px and shifts to #3f3ec6, with padding adjusted by 1px to maintain the same total height. Error states use a 1px #ff0022 border.

**`select-dropdown`** — Matches the text-input styling for visual consistency. Used in product filtering, language selection, and configuration forms.

**`search-bar`** — A pill-shaped search field ({rounded.full}) with a light gray background (#f7f7f7) and 1px #cacddb border. At 40px height, it's compact enough for the nav bar but still clearly interactive. On focus, the background shifts to white and the border becomes a 2px #3f3ec6 outline.

### Tables & Data Display
**`table-header`** — Used in product comparison tables, specification sheets, and download lists. A light gray (#f7f7f7) background with 16px medium-weight text in #094e7f, separated from data rows by a 2px #cacddb border. Cells have 12px vertical and 16px horizontal padding.

**`table-cell`** — Standard data cells with 14px body text in #4e4534 and a 1px #e0dafe bottom border. This creates a clean, readable grid without heavy visual noise — appropriate for dense technical specifications.

**`spec-list`** / **`spec-label`** / **`spec-value`** — A two-column layout for product specifications. Labels appear in #828282 at 600 weight, values in #4e4534 at 400 weight. Items are spaced at {spacing.sm} (8px) for tight, scannable information density.

### Hero & Footer
**`hero-section`** — Full-width banner areas using #094e7f (ink) as background with white text. The heading uses {typography.display-xl} (32px bold) and the subtitle uses {typography.body-md} in #cacddb. Section padding is {spacing.section} (64px) vertical and {spacing.xl} (32px) horizontal.

**`footer`** — A deep navy (#094e7f) footer with muted gray (#cacddb) links and body text. Links shift to white on hover. The footer uses the same generous vertical padding as the hero section, creating a balanced visual bookend for the page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero text reduces to {typography.display-lg}; tables scroll horizontally; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grids; nav links truncate to icons; side-by-side spec lists; hero maintains two-column layout with reduced image size |
| Desktop | 1128–1440px | Three-column product grids; full nav with dropdowns; multi-column footer; hero at full width with large imagery; comparison tables at full width |
| Wide | > 1440px | Max-width container at 1440px; additional whitespace in margins; product grids can expand to four columns; hero content centered with max-width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target
- Primary CTAs are 44px height minimum
- Icon buttons are 36x36px with 44x44px clickable area via padding
- Tab items have 12px vertical padding ensuring adequate tap area
- Product cards are fully tappable with minimum 120px height

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product comparison tables become horizontally scrollable on mobile
- Multi-column footers collapse to single column below 744px
- Hero sections stack vertically on mobile (image below text)
- Product specification lists collapse to single-column label-value pairs
- Search bar moves from nav to full-width below the header on mobile
- Tab navigation becomes a horizontal scrollable strip on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list contains 30+ hex values, many of which appear to be framework defaults (Bootstrap blues, grays) or stock-image dominant tones. The true brand palette likely centers on #3f3ec6 (deep indigo) and #094e7f (navy), but the exact secondary palette (especially the accent colors) should be verified against QNAP's official brand guidelines.
- Font-family declarations only returned FontAwesome and Bootstrap Icons — no primary body or heading fonts were extracted. The system font stack used in this document is a best-guess fallback; QNAP may use a custom typeface (e.g., Noto Sans, Inter, or a proprietary font) that wasn't captured.
- No hover, focus, or active states were extractable from the static analysis — these are inferred from common design patterns for the networking category.
- Error states, validation styling, and disabled input styling are not confirmed from the live site.
- Dark mode support is unknown — the extracted palette suggests a light-mode-only interface.
- The meta theme-color tag was absent, so browser chrome theming behavior is unspecified.
- Sub-brand or regional palette variations (e.g., QNAP for enterprise vs. consumer) could not be determined.
- Animation timing, easing curves, and transition durations are not extractable from static CSS analysis.
- Iconography style (outlined vs. filled, custom vs. library) is inferred from the FontAwesome presence but not confirmed for brand-specific icons.
