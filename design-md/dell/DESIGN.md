---
version: alpha
name: "Dell"
source_url: "https://www.dell.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A blue-and-gray precision system built for enterprise confidence, where #00468b (Dell Blue) anchors the primary action layer while #0076ce and #0672cb provide a cooler, more technical secondary blue spectrum — the palette reads as IT-procurement serious, not consumer playful. The extracted palette is dominated by a dozen gray values (#636363, #707070, #6e6e6e, #444444, #535657) and multiple blues (#00468b, #0672cb, #0063b8, #0076ce, #1d73c2, #006bbd, #0477cf, #007db8), with #f0f0f0 and #f5f6f7 as the primary canvas surfaces — there is no accent color outside the blue family except #6ea204 (a muted green likely for status indicators or sustainability badges) and two purple tones (#7f234f, #40155c) that may belong to sub-brand or checkout widgets. Typography runs a sans-serif stack of Arial, Helvetica, and Roboto with Japanese fallbacks (Hiragino Kaku Gothic, Meiryo UI, MS UI Gothic), suggesting a global B2B system that prioritizes legibility over personality. The site uses sharp corners ({rounded.none}) on navigation and cards, with subtle rounding ({rounded.sm}) only on buttons and input fields — this is a brand that communicates through dense product grids, spec tables, and configurator interfaces rather than editorial whitespace. The presence of #141d28 (a near-black) as a text color alongside #0e0e0e suggests a two-tier hierarchy for headings versus body copy, while #d9f5fd and #94dcf7 appear as informational blue backgrounds for alerts or feature callouts.

colors:
  primary: "#00468b"
  primary-active: "#006bbd"
  primary-disabled: "#b6b6b6"
  ink: "#141d28"
  body: "#444444"
  muted: "#636363"
  muted-soft: "#707070"
  hairline: "#c8c9c7"
  hairline-soft: "#e0e1e2"
  canvas: "#ffffff"
  surface-soft: "#f5f6f7"
  surface-card: "#ffffff"
  surface-strong: "#f0f0f0"
  on-primary: "#ffffff"
  accent-blue: "#0076ce"
  accent-blue-light: "#d9f5fd"
  accent-green: "#6ea204"
  dark-bg: "#141d28"
  text-heading: "#0e0e0e"
  text-body: "#444444"
  text-muted: "#636363"
  border-default: "#c8c9c7"
  border-soft: "#e0e1e2"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, Roboto, 'Hiragino Kaku Gothic ProN', 'Meiryo UI', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, Helvetica, Roboto, 'Hiragino Kaku Gothic ProN', 'Meiryo UI', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arial, Helvetica, Roboto, 'Hiragino Kaku Gothic ProN', 'Meiryo UI', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica, Roboto, 'Hiragino Kaku Gothic ProN', 'Meiryo UI', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, Roboto, 'Hiragino Kaku Gothic ProN', 'Meiryo UI', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, Roboto, 'Hiragino Kaku Gothic ProN', 'Meiryo UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, Roboto, 'Hiragino Kaku Gothic ProN', 'Meiryo UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, Roboto, 'Hiragino Kaku Gothic ProN', 'Meiryo UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, Roboto, 'Hiragino Kaku Gothic ProN', 'Meiryo UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-lg:
    fontFamily: "Arial, Helvetica, Roboto, 'Hiragino Kaku Gothic ProN', 'Meiryo UI', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "Arial, Helvetica, Roboto, 'Hiragino Kaku Gothic ProN', 'Meiryo UI', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, Helvetica, Roboto, 'Hiragino Kaku Gothic ProN', 'Meiryo UI', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  link:
    fontFamily: "Arial, Helvetica, Roboto, 'Hiragino Kaku Gothic ProN', 'Meiryo UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, Roboto, 'Hiragino Kaku Gothic ProN', 'Meiryo UI', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  badge:
    fontFamily: "Arial, Helvetica, Roboto, 'Hiragino Kaku Gothic ProN', 'Meiryo UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px rgba(0, 70, 139, 0.15)"
  text-input-error:
    border: "1px solid #c13515"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
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
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.08)"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 0
    boxShadow: "0 4px 16px rgba(0, 0, 0, 0.12)"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 16px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0, 0, 0, 0.08)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.text-heading}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 700
  product-card-cta:
    typography: "{typography.link}"
    textColor: "{colors.primary}"
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "#c13515"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    padding: 48px 24px
  hero-banner-dark:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-primary}"
    padding: 48px 24px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px rgba(0, 70, 139, 0.15)"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.primary}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    borderBottom: "3px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
  configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 24px
  configurator-option:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  configurator-option-selected:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.surface-soft}"
  table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.text-heading}"
    typography: "{typography.body-sm}"
    fontWeight: 700
    padding: "12px 16px"
    borderBottom: "2px solid {colors.hairline}"
  table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "12px 16px"
    borderBottom: "1px solid {colors.hairline-soft}"
  table-row-hover:
    backgroundColor: "{colors.surface-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across Dell's product pages, configurators, and checkout flows. Uses Dell Blue (#00468b) as a solid fill with white text, 4px corner rounding, and 44px height for comfortable touch targeting. On hover, shifts to #006bbd for a lighter, more approachable state; disabled renders in #b6b6b6 with no interaction. The button carries 700-weight type at 14px with 0.3px letter spacing, giving it a confident, procurement-ready posture.

**`button-secondary`** — An outlined variant for secondary actions like "Compare" or "Learn More." White fill with a 2px Dell Blue border, matching the primary button's 44px height and 4px rounding. Hover state inverts to a light gray fill (#f5f6f7) with the active blue border. The same 700-weight type ensures visual parity with the primary button in a two-button layout.

**`button-tertiary`** — A text-only button for low-emphasis actions such as "Cancel" or "View Details." Transparent background with Dell Blue text, no border, and standard 12px 24px padding. Hover state adds a subtle underline or opacity shift.

**`button-ghost`** — Used in navigation and toolbar contexts where the button needs to sit flush against a white background. Transparent with dark ink text (#141d28), 12px 16px padding, and no rounding. Hover adds a light gray background (#f5f6f7) for hit-state feedback.

### Forms
**`text-input`** — Standard single-line text input for search, login, and form fields. White background with a 1px #c8c9c7 border, 4px rounding, and 44px height. Focus state gains a Dell Blue border with a 2px blue-tinted box-shadow ring for accessibility. Error state uses a red (#c13515) border with no shadow ring.

**`select-input`** — Dropdown selectors for product configuration (memory, storage, color). Matches text-input dimensions and border styling, with a custom chevron icon in #636363. Focus and error states mirror text-input behavior.

### Navigation
**`nav-bar`** — The primary top-level navigation bar at 64px height, white background with a 1px #e0e1e2 bottom border. Navigation links use 14px/600-weight type with 0.2px letter spacing. On scroll, the bar gains a subtle drop shadow (0 2px 8px rgba(0,0,0,0.08)) and becomes sticky. Dropdown menus use a white panel with 4px rounding, 8px vertical padding, and a 0 4px 16px shadow for depth.

**`tab-active` / `tab-inactive`** — Tab navigation used on product detail pages and category listings. Active tab has a 3px Dell Blue bottom border with blue text; inactive tabs use muted gray (#636363) with no border. Both use 14px/700-weight button type for clear hierarchy.

### Product Cards
**`product-card`** — The primary product display unit across category pages and search results. White background with a 1px #e0e1e2 border, no corner rounding, and 16px internal padding. Images sit at a 4:3 aspect ratio with no rounding. On hover, the card gains a 0 4px 12px shadow and the border shifts to #c8c9c7. The title uses 18px/600-weight type in near-black (#0e0e0e), while the price sits at 16px/700-weight in dark ink (#141d28). A blue link ("View Deal" or "Customize") provides the primary action.

### Badges
**`badge-new`** — A compact uppercase label for "NEW" or "FEATURED" indicators. Uses accent blue (#0076ce) fill with white 11px/700-weight type, 2px rounding, and 2px 8px padding. Appears on product cards and category strip items.

**`badge-sale`** — A red badge for "SALE" or "DEAL" indicators. Uses #c13515 fill with white type, matching badge-new dimensions.

**`badge-green`** — Used for sustainability badges ("ECO," "RECYCLED") or in-stock indicators. Uses #6ea204 fill with white type.

### Hero & Content Blocks
**`hero-banner`** — Full-width promotional banners on the homepage and campaign pages. Uses a light gray background (#f0f0f0) with dark text, 48px 24px padding. A dark variant (`hero-banner-dark`) uses #141d28 background with white text for high-contrast messaging. Both variants center content with a max-width container.

**`configurator-panel`** — The product configuration sidebar or modal where users customize specs (processor, RAM, storage). Uses a light gray background (#f5f6f7) with no rounding, 24px padding. Individual options (`configurator-option`) are white cards with 4px rounding, 1px #c8c9c7 border, and 12px 16px padding. Selected options gain a 2px Dell Blue border with a light blue fill.

### Tables
**`table-header` / `table-row`** — Specification comparison tables used on product detail pages. Headers use a light gray background (#f5f6f7) with 700-weight type and a 2px bottom border. Rows alternate white background with 1px #e0e1e2 bottom borders. Hover state on rows adds a light gray tint for readability in dense spec comparisons.

### Footer
**`footer-section`** — The site footer with link columns, legal text, and social icons. Uses a light gray background (#f5f6f7) with #444444 body text and #636363 link text. Links hover to Dell Blue. Padding is 48px 24px with a max-width container. Legal text uses 12px caption type.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grids; nav collapses to hamburger menu; hero banners stack vertically; configurator becomes full-screen modal; tables scroll horizontally; footer links stack in single column |
| Tablet | 744–1128px | Two-column product grids; nav shows top-level links only; configurator appears as bottom sheet; tables show 3-4 columns; footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grids; full nav with dropdowns; configurator as sidebar; full table width; footer uses 4-column layout |
| Wide | > 1440px | Four-column product grids; max-width containers (1440px) for content; configurator remains sidebar; tables show full spec rows |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card CTAs are full-width on mobile (min 48px height)
- Nav hamburger icon is 44x44px with 8px internal padding
- Filter and sort controls use 48px height on mobile for easy thumb reach
- Close buttons on modals and overlays are 44x44px

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-in drawer for full nav
- Product comparison tables collapse to a horizontal scroll container on mobile, with sticky first column
- Configurator panel collapses from sidebar to full-screen modal on mobile, with a sticky "Apply" button at bottom
- Footer link columns collapse from 4 columns to 2 on tablet, to 1 on mobile
- Hero banners stack vertically on mobile, with image above text
- Product card grids reduce from 4 columns to 3 to 2 to 1 as viewport shrinks

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted from the live site; the above hover states are inferred from common Dell patterns and should be verified against design specs
- Error styling for forms (error messages, validation icons) was not observable; red border (#c13515) is assumed from industry convention
- Dark mode or high-contrast mode tokens are not present in the extracted data
- Sub-brand palettes (Alienware, XPS, Precision, Inspiron) likely exist but were not extractable from the main dell.com page; each sub-brand may have distinct accent colors and typography
- The two purple tones (#7f234f, #40155c) could not be confidently assigned; they may belong to checkout widgets, promotional badges, or legacy sub-brand elements
- Animation and transition timing values (durations, easing curves) were not extractable
- Iconography style and sizing conventions were not observable from the extracted data
- Loading states, skeleton screens, and empty states are not documented
- Print styles and reduced-motion preferences are not captured
- The #6ea204 green is assumed to be a status/sustainability accent but its exact usage context is unconfirmed
- Japanese-specific typography adjustments (line-height, font-size scaling for CJK characters) are not documented beyond font-family declarations
