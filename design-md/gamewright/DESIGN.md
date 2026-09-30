---
version: alpha
name: "Gamewright"
source_url: "https://gamewright.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A saturated, primary-color playground where #eec703 (a high-gamut marigold) and #5b0a69 (a deep plum) clash and harmonize across every product tile, badge, and navigation bar — the brand treats color as a game mechanic, not decoration. The extracted palette reads like a box of crayons dumped onto a white canvas: #027acd cyan, #f16d00 tangerine, #1da120 lime, #b9cc1a chartreuse, #cc007b fuchsia, and #29358e navy all appear with near-equal frequency, suggesting a system where any game can claim its own accent pair. Typography splits between Itim (a hand-drawn, slightly wobbly sans for display and titles) and Open Sans (a neutral, legible workhorse for body and instructions), with Wellfleet (a serifed slab with irregular letterforms) reserved for special callouts or age-rating badges. Corners are soft but not pill-shaped — `{rounded.md}` (12px) on cards and `{rounded.sm}` (8px) on buttons keep the interface approachable without losing the crispness needed for game component grids. The overall mood is unapologetically loud, child-forward but not childish: the brand trusts that saturated color blocks and chunky typography can signal fun without needing illustration or photography to carry the emotional load.

colors:
  primary: "#eec703"
  primary-active: "#d4b000"
  primary-disabled: "#f5e080"
  ink: "#212121"
  body: "#3a3a3a"
  muted: "#6a6a6a"
  muted-soft: "#9a9a9a"
  hairline: "#dadada"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#212121"
  plum: "#5b0a69"
  plum-light: "#77359b"
  cyan: "#027acd"
  cyan-light: "#1292d3"
  orange: "#f16d00"
  orange-light: "#f28019"
  green: "#1da120"
  green-light: "#32a93a"
  chartreuse: "#b9cc1a"
  fuchsia: "#cc007b"
  navy: "#29358e"
  navy-light: "#29358f"

typography:
  display-xl:
    fontFamily: "'Itim', 'Comic Neue', 'Patrick Hand', cursive, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-lg:
    fontFamily: "'Itim', 'Comic Neue', 'Patrick Hand', cursive, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'Itim', 'Comic Neue', 'Patrick Hand', cursive, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Itim', 'Comic Neue', 'Patrick Hand', cursive, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Itim', 'Comic Neue', 'Patrick Hand', cursive, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Itim', 'Comic Neue', 'Patrick Hand', cursive, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Wellfleet', 'Courier Prime', 'Roboto Slab', serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Itim', 'Comic Neue', 'Patrick Hand', cursive, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "'Itim', 'Comic Neue', 'Patrick Hand', cursive, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Itim', 'Comic Neue', 'Patrick Hand', cursive, sans-serif"
    fontSize: 16px
    fontWeight: 400
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.plum}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
    border: "2px solid {colors.plum}"
  button-secondary-active:
    backgroundColor: "{colors.plum-light}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-accent-cyan:
    backgroundColor: "{colors.cyan}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-accent-orange:
    backgroundColor: "{colors.orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-accent-green:
    backgroundColor: "{colors.green}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-pill:
    backgroundColor: "{colors.plum}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.fuchsia}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    textColor: "{colors.plum}"
    borderBottom: "3px solid {colors.plum}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.plum}"
    boxShadow: "0 4px 12px rgba(91, 10, 105, 0.15)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-badge-age:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-award:
    backgroundColor: "{colors.cyan}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-new:
    backgroundColor: "{colors.green}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.plum}"
  footer:
    backgroundColor: "{colors.plum}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "48px 24px"
  footer-link:
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "12px 0"
  category-tab:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  category-tab-active:
    backgroundColor: "{colors.plum}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "48px 24px"
    rounded: "{rounded.md}"
  hero-banner-plum:
    backgroundColor: "{colors.plum}"
    textColor: "{colors.canvas}"
  hero-banner-cyan:
    backgroundColor: "{colors.cyan}"
    textColor: "{colors.canvas}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-thick:
    backgroundColor: "{colors.plum}"
    height: 4px
    rounded: "{rounded.full}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's signature marigold `{colors.primary}` (#eec703) and dark text for maximum contrast. On hover, it shifts to a slightly deeper gold `{colors.primary-active}` (#d4b000); disabled state uses a pale yellow `{colors.primary-disabled}` (#f5e080) with muted text. The `{rounded.sm}` (8px) radius keeps it friendly without being overly pill-shaped.

**`button-secondary`** — An outlined variant with a white fill and a 2px solid border in `{colors.plum}` (#5b0a69). On hover, the background fills with `{colors.plum-light}` (#77359b) and text inverts to white. Used for "Learn More" or "View Details" actions alongside primary buttons.

**`button-accent-cyan`**, **`button-accent-orange`**, **`button-accent-green`** — Solid accent buttons in `{colors.cyan}`, `{colors.orange}`, and `{colors.green}` respectively, all with white text. These allow product pages or category sections to adopt a game-specific accent color without breaking the button pattern. Each follows the same `{rounded.sm}` and 48px height as the primary button.

**`button-pill`** — A fully rounded (`{rounded.full}`) pill button in `{colors.plum}` with white text and smaller typography. Used for filter tags, age-range selectors, or "Shop by Category" links where a compact, playful shape is appropriate.

### Cards
**`product-card`** — A white card with `{rounded.md}` (12px) corners, a 1px `{colors.hairline-soft}` border, and 16px padding. On hover, the border shifts to `{colors.plum}` and a subtle plum-tinted shadow appears. The card contains a square image area (`{rounded.sm}`) and text below for the game title, age rating, and player count.

**`product-badge-age`**, **`product-badge-award`**, **`product-badge-new`** — Small, uppercase badges using `{typography.badge}` (Wellfleet font, 11px, uppercase). The age badge uses `{colors.primary}` with dark text; award badges use `{colors.cyan}` with white text; new-release badges use `{colors.green}` with white text. Each has `{rounded.xs}` (4px) corners and tight padding.

### Navigation
**`nav-bar`** — A white 72px header with a subtle bottom border (`{colors.hairline-soft}`). Navigation links use Itim at 16px with 8px/16px padding. Active links gain a 3px plum underline and plum text color. The nav bar is fixed at the top on desktop and collapses to a hamburger menu on mobile.

**`category-strip`** — A horizontal scrollable strip of pill-shaped category tabs below the nav. Each tab is `{rounded.full}` with a soft gray background (`{colors.surface-soft}`) and dark text. The active tab fills with `{colors.plum}` and white text. Categories include "Ages 2-4", "Ages 5-7", "Ages 8+", "Card Games", "Dice Games", etc.

### Forms
**`text-input`** — A 48px input with `{rounded.sm}`, 12px/16px padding, and a 2px `{colors.hairline}` border. On focus, the border turns `{colors.primary}`. Error state uses `{colors.fuchsia}` (#cc007b) for the border. Typography is Open Sans at 16px.

**`search-bar`** — A pill-shaped (`{rounded.full}`) search input with a soft gray background (`{colors.surface-soft}`) and a 1px hairline border. On focus, the border thickens to 2px `{colors.plum}`. Used in the nav bar and on the homepage.

### Footer
**`footer`** — A full-width plum (`{colors.plum}`) footer with white text in Open Sans 14px. Links use `{colors.primary}` (#eec703) for high contrast against the dark background. Padding is generous at 48px top/bottom and 24px sides. The footer contains columns for "Games", "About", "Support", and "Connect".

### Hero
**`hero-banner`** — A large promotional banner with `{rounded.md}` corners, typically using `{colors.primary}` as the background with dark text in `{typography.display-xl}` (Itim 36px). Variants exist for plum (`{colors.plum}` with white text) and cyan (`{colors.cyan}` with white text) backgrounds, allowing seasonal or game-specific hero treatments.

### Dividers
**`divider`** — A 1px hairline (`{colors.hairline}`) horizontal rule for separating sections. **`divider-thick`** is a 4px plum (`{colors.plum}`) bar with `{rounded.full}`, used as a decorative accent between major content blocks.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack in single column; hero banner reduces to 32px padding; category strip is horizontally scrollable; footer columns stack vertically |
| Tablet | 744–1128px | Nav links visible but condensed; product cards in 2-column grid; hero banner at 40px padding; footer in 2-column layout |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero banner at 48px padding; footer in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; additional whitespace on hero |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height and 44px width for touch accessibility.
- Category tabs in the strip are at least 40px tall with 16px horizontal padding.
- Nav links have 8px/16px padding, ensuring tap targets exceed 44px.
- Search bar is 48px tall with 20px horizontal padding.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu below 744px, with a slide-out drawer from the left.
- The category strip remains horizontally scrollable on all breakpoints but gains arrow indicators on mobile.
- Product grids collapse from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Footer columns collapse from 4 to 2 to 1 as viewport shrinks.
- Hero banners reduce padding and font size on mobile (display-xl drops to 28px).

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were inferred from the brand's color system rather than extracted from live CSS. The specific hover transitions (duration, easing) are unknown.
- Error and validation styling for forms (error messages, success states) was not present in the extracted data. The fuchsia error border is an assumption based on the palette's high-contrast accent colors.
- Dark mode is not supported on the live site; no dark theme tokens exist.
- The exact font weights for Itim and Wellfleet were not extractable — Itim appears to be used at weight 400 (its only weight) and Wellfleet at weight 400 (its only weight). Open Sans weights were inferred from common usage (400 for body, 600 for links).
- The extracted color list is unusually large (30+ hex values), suggesting the site uses many accent colors per game or section. The primary palette above selects the most frequent and distinctive colors, but individual game pages may introduce additional accent colors not captured here.
- Spacing values (padding, margins, grid gaps) were not extractable from the live site and are estimated based on common DTC board-game patterns.
- The `rounded` values for specific components (cards, buttons, inputs) were inferred from the site's general aesthetic rather than measured from CSS.
- Animation and transition specifications (hover durations, page transitions, loading states) are not documented.
- Accessibility contrast ratios have not been verified against WCAG standards.
