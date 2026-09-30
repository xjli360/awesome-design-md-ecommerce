---
version: alpha
name: "RC Fastener"
source_url: "https://www.rcfastener.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Metropolis — a geometric sans-serif with Bauhaus DNA — lands as the display and navigation typeface atop a Bootstrap 3 skeleton at RC Fastener, a productive mismatch between a font engineered for contemporary visual identity and a grid system optimized for wholesale procurement efficiency. The brand blue is #0064af, pulled noticeably deeper and more saturated than Bootstrap's native #337ab7 — a deliberate deviation that carves out brand ownership without abandoning the familiar 12-column grid. Nearly the entire structural color vocabulary runs on Bootstrap's own semantic alert system: success green (#3c763d text on #dff0d8 ground), warning amber (#8a6d3b on #fcf8e3), danger red (#a94442 on #f2dede), and info blue (#23527c on #d9edf7). These alert-state pairs are not cosmetic residue — for wholesale buyers tracking minimum order quantities, lead times, and stock availability windows, a precise semantic palette is functional infrastructure, not decoration. Corners hold near-square throughout at {rounded.xs} and {rounded.sm}, a configuration that signals procurement density over consumer warmth. The body ink is #2c2a29, a slightly warm near-black that sustains legibility across dense spec tables without the optical harshness of pure black on white. Arial carries all body text and table data; Metropolis reserves its geometric clarity for page-level headings, category titles, and nav labels where cap-height distinctiveness helps buyers scan a deep catalog quickly. A secondary accent at #cb090d — a crimson red — marks price callouts and urgent stock warnings, injecting signal weight without drifting the system toward retail tone. The whole palette, taken together, reads like a trade counter digitized: dense, unambiguous, and calibrated for buyers who arrive knowing their thread pitch and order volume before the page loads.

colors:
  primary: "#0064af"
  primary-active: "#23527c"
  primary-disabled: "#337ab7"
  accent-danger: "#cb090d"
  accent-danger-dark: "#9a070a"
  ink: "#2c2a29"
  body: "#595959"
  muted: "#777777"
  muted-soft: "#aaaaaa"
  hairline: "#eeeeee"
  hairline-strong: "#9a9a9a"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  state-success-text: "#3c763d"
  state-success-bg: "#dff0d8"
  state-success-border: "#d6e9c6"
  state-warning-text: "#8a6d3b"
  state-warning-bg: "#fcf8e3"
  state-warning-border: "#faebcc"
  state-danger-text: "#a94442"
  state-danger-bg: "#f2dede"
  state-danger-border: "#ebccd1"
  state-info-text: "#23527c"
  state-info-bg: "#d9edf7"
  state-info-border: "#bce8f1"

typography:
  display-xl:
    fontFamily: "'Metropolis', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Metropolis', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Metropolis', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Metropolis', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Metropolis', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Metropolis', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "'Metropolis', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'Metropolis', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  table-header:
    fontFamily: "'Metropolis', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  label-sm:
    fontFamily: "'Metropolis', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
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
    padding: 8px 16px
    height: 36px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.65
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 7px 15px
    height: 36px
    border: "1px solid {colors.hairline-strong}"
  button-danger:
    backgroundColor: "{colors.accent-danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-sm-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
    border: "1px solid {colors.hairline-strong}"
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(0,100,175,0.2)"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
    border: "1px solid {colors.hairline-strong}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 50px
    padding: 0 16px
  nav-bar-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    boxShadow: "0 2px 6px rgba(0,0,0,0.15)"
  top-utility-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    padding: 0 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.accent-danger}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-strong}"
    submitBackgroundColor: "{colors.accent-danger}"
    submitTextColor: "{colors.on-primary}"
    submitTypography: "{typography.button-md}"
    padding: 6px 12px
  alert-success:
    backgroundColor: "{colors.state-success-bg}"
    textColor: "{colors.state-success-text}"
    border: "1px solid {colors.state-success-border}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  alert-warning:
    backgroundColor: "{colors.state-warning-bg}"
    textColor: "{colors.state-warning-text}"
    border: "1px solid {colors.state-warning-border}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  alert-danger:
    backgroundColor: "{colors.state-danger-bg}"
    textColor: "{colors.state-danger-text}"
    border: "1px solid {colors.state-danger-border}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  alert-info:
    backgroundColor: "{colors.state-info-bg}"
    textColor: "{colors.state-info-text}"
    border: "1px solid {colors.state-info-border}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.body}"
    linkColor: "{colors.primary}"
    typography: "{typography.caption}"
    separator: "/"
  price-block:
    priceColor: "{colors.accent-danger}"
    priceTypography: "{typography.price-display}"
    labelColor: "{colors.muted}"
    labelTypography: "{typography.caption}"
  data-table:
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.table-header}"
    rowTextColor: "{colors.body}"
    rowTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    stripeBackgroundColor: "{colors.surface-soft}"
  category-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    activeLinkColor: "{colors.primary}"
    activeFontWeight: 600
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
  stock-badge-in-stock:
    backgroundColor: "{colors.state-success-bg}"
    textColor: "{colors.state-success-text}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  stock-badge-low-stock:
    backgroundColor: "{colors.state-warning-bg}"
    textColor: "{colors.state-warning-text}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  stock-badge-out-of-stock:
    backgroundColor: "{colors.state-danger-bg}"
    textColor: "{colors.state-danger-text}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: 48px 0 24px
---

## Components

### Buttons
**`button-primary`** — Solid #0064af fill with white text at 14px Metropolis 600, 4px corners (`{rounded.sm}`), 36px tall to match Bootstrap's default button height. Hover state deepens to #23527c (`{colors.primary-active}`); disabled bleeds to #337ab7 at 65% opacity, preserving legibility while clearly withdrawing the interaction.

**`button-secondary`** — White fill with #2c2a29 ink text and a 1px #9a9a9a border. Used for secondary actions alongside a primary CTA — particularly in cart and checkout flows — where equal height with `button-primary` keeps pairs aligned in button rows without visual competition.

**`button-danger`** — Solid #cb090d fill reserved for destructive or time-sensitive actions: remove from cart, cancel order, clear form. Semantically distinct from `button-primary` so that crimson always carries consequence; overuse in general UI would collapse the signal.

**`button-sm-outline`** — 13px Metropolis 600, 2px radius (`{rounded.xs}`), #0064af border and text on white. Used inline within product listing rows and quick-spec panels where a full-height button would disrupt table rhythm.

### Form Inputs
**`text-input`** — 34px tall, 1px #9a9a9a border, 2px radius, 6px vertical and 12px horizontal padding. Focus ring is a 3px #0064af halo at 20% opacity — Bootstrap's familiar `:focus` box-shadow treatment requiring no custom override. Placeholder color is #777777. Pairs with `select-input` in search and filter forms; both share identical dimensions so mixed rows align without offset.

**`select-input`** — Identical construction to `text-input`. Used extensively in product search for filtering by grade, drive type, thread pitch, and material specification — where the dropdown label is as important as the field itself.

### Navigation
**`nav-bar`** — #0064af background with white Metropolis 600 labels at 14px, 50px tall. Dropdown panels break to white canvas with 1px `{colors.hairline}` border, 2px radius, and a light drop shadow. At mobile breakpoint, collapses via Bootstrap's standard hamburger toggle to a full-height vertical stack.

**`top-utility-bar`** — A 36px strip above the main nav with a #2c2a29 background and white 12px Arial text. Carries the phone number, account login, and cart icon. Its dark ground against the blue nav creates a clear two-tier hierarchy: utility above, primary navigation below.

### Product Catalog
**`product-card`** — 1px `{colors.hairline}` border, 2px radius, 12px interior padding. Product title in 15px Metropolis 600 (`{typography.title-sm}`), price in 20px Metropolis 700 at #cb090d (`{typography.price-display}`). Stock badge floats top-right using `stock-badge-in-stock`, `stock-badge-low-stock`, or `stock-badge-out-of-stock`. Grid runs 4-up on desktop, 2-up on tablet, 1-up on mobile.

**`data-table`** — Primary display surface for spec-heavy product listings and bulk pricing tiers. Column headers in 13px Metropolis 700 on `{colors.surface-soft}`. Body rows alternate between `{colors.canvas}` and `{colors.surface-soft}` at 13px Arial. All borders in `{colors.hairline}`. On small screens, the table never stacks — it scrolls horizontally with a sticky first column so spec comparisons remain readable.

**`price-block`** — Standalone price unit: a 20px Metropolis 700 numeral in #cb090d preceded by a 12px Arial "Unit Price:" label in #777777. Deployed both inside product cards and in the product-detail page header directly beneath the product title.

### Search
**`search-bar`** — Full-width input at 34px height with a 2px radius and `{colors.hairline-strong}` border, paired with a #cb090d submit button carrying white Metropolis 600 text. Using crimson — rather than the primary blue — for the submit trigger is a deliberate departure: it makes the search action immediately visible without relying on proximity to the input for context, a practical choice in a catalog where search is the primary navigation tool.

### Alerts and Status
**`alert-success`** / **`alert-warning`** / **`alert-danger`** / **`alert-info`** — Bootstrap's four semantic alert panels, each a 1px bordered block with role-matched background and text. Employed for order confirmations (success), shipping cutoff notices (warning), out-of-stock declarations (danger), and minimum-order policy notes (info). The four-state vocabulary is used consistently enough that color alone carries meaning without needing icon reinforcement.

**`stock-badge-*`** — Compact 11px Metropolis uppercase pills in three variants: in-stock (#3c763d on #dff0d8), low-stock (#8a6d3b on #fcf8e3), out-of-stock (#a94442 on #f2dede). Color meanings mirror the alert palette exactly, so the semantic map transfers without re-learning.

### Category Navigation
**`category-sidebar`** — Left-column filter panel on category pages. #f5f5f5 background, `{colors.body}` text at 14px Arial, active link in #0064af at weight 600, no border-radius anywhere. On mobile, stacks into a collapsible accordion to preserve vertical screen real estate for the product grid.

### Footer
**`footer`** — Full-width #2c2a29 background with white link text at 13px Arial and section headings in 15px Metropolis 600. Three-column grid on desktop, single-column stacked on mobile. Contains company address, phone number, department links, and policy pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; top utility bar hides; category sidebar becomes collapsible accordion; data tables scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; nav horizontal but condensed; sidebar visible at reduced width; footer two-column |
| Desktop | 1128–1440px | Four-column product grid; full horizontal nav with dropdowns; three-column footer; sidebar at standard width |
| Wide | > 1440px | Content constrains to ~1200px centered; gutters expand symmetrically; no layout changes beyond centering |

### Touch Targets
- All buttons minimum 36px tall; primary nav links padded to 44px touch height on mobile
- Product card tap target spans the full card area including image, title, and price zones
- Quantity inputs paired with +/− stepper buttons, each 36px minimum, for thumb-friendly cart editing
- Search submit button minimum 44px tall on mobile
- Category sidebar accordion headers minimum 44px tap area

### Collapsing Strategy
- Top utility bar (phone, account, cart) hides entirely on mobile; these links fold into the hamburger overlay
- Category sidebar converts to a collapsible accordion at tablet breakpoint; collapses fully on mobile
- Data tables never reflow to stacked rows — horizontal overflow with sticky first column preserves spec comparison usability
- Multi-level dropdown nav flattens to a full-screen slide-in overlay on mobile with explicit back navigation per level
- Footer columns stack vertically on mobile with `{spacing.lg}` between each section

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom icon set documented; FontAwesome 4 is in use but specific glyph-to-category mappings are not captured
- Metropolis font weight subset loaded (400/500/600/700 all assumed available, but subset could not be confirmed from static extraction)
- Exact nav-bar dropdown animation timing and easing curves not observed
- Product image aspect ratio and placeholder treatment not extracted; assumed 1:1 square crop based on catalog convention
- Pagination component active-state color and disabled-state treatment not directly observed
- Inline form-validation error treatment (likely `{colors.state-danger-text}` beneath input, not full alert panel) not confirmed
- Mobile hamburger overlay background, animation, and z-index stacking not captured
- Bulk/tiered pricing table display rules and threshold badge treatment not documented
- Whether #ff0000 and #4bd963 are live brand colors or extracted from third-party widgets could not be confirmed; excluded from primary palette
