---
version: alpha
name: "Ghent"
source_url: "https://www.ghent.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Boards at scale — Ghent's catalog is organized around products measured in feet rather than inches: eighteen-foot markerboard walls, floor-to-ceiling tackboards, mobile partitions that reconfigure a floor plan overnight. The primary action color `#37c2dd` is a cyan-forward teal that breaks cleanly from the navy-dominant blues saturating the commercial-office supply category; it carries enough chroma to anchor navigation and primary CTAs while reading warmly against the near-white canvases (`#f6f6f6`, `#f5f5f5`) that structure most catalog pages. A quieter sibling, `#aacccc` dusty sage, handles secondary fills, hover states, and footer link treatments, giving the two-tonal teal system a low-contrast coherence that never competes with product photography. Display headings use `mr-eaves-xl-modern`, a humanist sans with subtle calligraphic undertones that introduce brand character without breaking the authoritative register required for commercial procurement pages; interface body and UI copy run in `proxima-nova` at 14–16px, and `proxima-nova-condensed` appears wherever horizontal density matters — SKU codes, dimension fields, specification tables. The dark charcoal `#4b4f54` carries navigation backgrounds and heavy content anchors, stepping down from near-black `#090909` reserved for display ink; a graduated gray family (`#555555`, `#777777`, `#9d9d9d`) fills muted body copy, disabled states, and hairlines. Corner geometry stays conservative — `{rounded.sm}` on cards and inputs, `{rounded.xs}` on badges — because buyers evaluating NoteVision glass finishes and mounting bracket load ratings expect an interface that signals precision. The Bootstrap 3 framework underneath contributes utility alert colors (success `#5cb85c`, danger `#d9534f`, warning `#f0ad4e`, info `#5bc0de`) that are infrastructural rather than brand-expressive; the real brand signal lives in the teal pairing, the condensed type handling specification density, and the wide, low-density grid layouts that let product dimensions and finish options read at a glance.

colors:
  primary: "#37c2dd"
  primary-active: "#1fa8c3"
  primary-disabled: "#a8dde6"
  primary-dark: "#4b4f54"
  secondary: "#aacccc"
  secondary-active: "#8bb5b5"
  ink: "#090909"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#9d9d9d"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-mid: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  nav-bg: "#4b4f54"
  state-success: "#5cb85c"
  state-success-bg: "#dff0d8"
  state-success-text: "#3c763d"
  state-danger: "#d9534f"
  state-danger-bg: "#f2dede"
  state-danger-text: "#a94442"
  state-warning: "#f0ad4e"
  state-warning-bg: "#fcf8e3"
  state-warning-text: "#8a6d3b"
  state-info: "#5bc0de"
  state-info-bg: "#d9edf7"
  state-info-text: "#31708f"

typography:
  display-xl:
    fontFamily: "'mr-eaves-xl-modern', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'mr-eaves-xl-modern', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'mr-eaves-xl-modern', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'proxima-nova', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'proxima-nova', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'proxima-nova', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-nova', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-nova', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'proxima-nova', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'proxima-nova', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25px
  nav-link:
    fontFamily: "'proxima-nova', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  product-code:
    fontFamily: "'proxima-nova-condensed', 'proxima-nova', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0.5px
  spec-label:
    fontFamily: "'proxima-nova-condensed', 'proxima-nova', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  breadcrumb:
    fontFamily: "'proxima-nova', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  filter-label:
    fontFamily: "'proxima-nova', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
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
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
    border: none
  button-primary-active:
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
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 38px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    outlineFocus: none
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 50px
    padding: 0 16px
  nav-bar-top-utility:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 34px
    padding: 0 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    codeTypography: "{typography.product-code}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    padding: "{spacing.base}"
    imageAspectRatio: 4/3
  hero-banner:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 320px
    padding: 48px 32px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    hoverBackgroundColor: "{colors.canvas}"
    padding: "{spacing.lg}"
    textAlign: center
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    submitButtonBackground: "{colors.primary}"
    submitButtonColor: "{colors.on-primary}"
    submitButtonHoverBackground: "{colors.primary-active}"
    height: 38px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.body}"
    typography: "{typography.breadcrumb}"
    separator: "/"
    separatorColor: "{colors.muted-soft}"
  spec-table:
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rowAlternateBackground: "{colors.surface-mid}"
    padding: 8px 12px
  filter-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.filter-label}"
    borderRight: "1px solid {colors.hairline}"
    checkboxAccent: "{colors.primary}"
    padding: "{spacing.base}"
  product-badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  alert-success:
    backgroundColor: "{colors.state-success-bg}"
    textColor: "{colors.state-success-text}"
    borderColor: "{colors.state-success}"
    border: "1px solid {colors.state-success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  alert-danger:
    backgroundColor: "{colors.state-danger-bg}"
    textColor: "{colors.state-danger-text}"
    border: "1px solid {colors.state-danger}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  alert-warning:
    backgroundColor: "{colors.state-warning-bg}"
    textColor: "{colors.state-warning-text}"
    border: "1px solid {colors.state-warning}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  footer:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.secondary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    padding: 64px 0 32px

## Components

### Buttons
**`button-primary`** — Solid `#37c2dd` background, white text at `{typography.button-md}`, `{rounded.sm}` corners, 40px height. Used for all primary procurement and quote-request actions: "Add to Cart," "Request Quote," "Get a Sample." Hover transitions to `#1fa8c3`; disabled state bleaches to `{colors.primary-disabled}`. The weight-600 label at 0.25px tracking gives the button a slightly formal authority consistent with a B2B catalog register.

**`button-secondary`** — White background with a `#37c2dd` border and matching teal text; creates a clear paired hierarchy alongside the primary without competing for attention. Active state shifts background to `{colors.surface-soft}` and border to `{colors.primary-active}`. Used for secondary actions like "Add to Compare," "Download Spec Sheet," and "View All in Category."

**`button-ghost`** — Transparent background with a `{colors.hairline}` border in `{colors.body}` text; reserved for low-emphasis actions such as filter resets, modal dismissals, and "Clear All" in faceted search. Inherits `{typography.button-md}` for consistent label sizing across the button family.

### Forms
**`text-input`** — 38px height, `{rounded.sm}` corners, `{colors.hairline}` border at rest transitioning to a solid `{colors.primary}` border on focus (no box-shadow ring). Placeholder copy in `{colors.muted}`, filled values in `{colors.ink}`. Appears across quote request forms, dealer-locator address fields, and quantity selectors on product detail pages. Label text sits above the input at `{typography.body-sm}` in `{colors.body}`.

### Navigation
**`nav-bar`** — Dark charcoal `#4b4f54` bar at 50px height, white `{typography.nav-link}` labels, hosting primary category links (Markerboards, Corkboards, Dry-Erase Glass, Accessories, Custom Solutions). A slimmer `nav-bar-top-utility` strip at 34px sits above it in the same dark palette for account links, phone numbers, and shipping callouts. The teal `{colors.primary}` appears in the nav only as the search submit button, creating a deliberate accent-only usage rather than flooding the dark bar.

**`search-bar`** — Inline search embedded in the nav zone: white `{text-input}`-style field with `{colors.hairline}` border and a solid `{colors.primary}` submit button. The teal button reinforces brand frequency at the top of every page and serves as the highest-traffic interactive element in the nav. Hover on the submit button transitions to `{colors.primary-active}`.

**`breadcrumb`** — Small `{typography.breadcrumb}` crumbs in `{colors.muted}` with a forward-slash separator in `{colors.muted-soft}`; the active (current) segment steps up to `{colors.body}` without bold weight. Appears on all category and product detail pages to support deep catalog navigation — a catalog with dozens of subcategories requires reliable wayfinding more than decorative hierarchy.

### Product
**`product-card`** — White card with a `{colors.hairline}` border, `{rounded.sm}` corners, and a 4:3 image block above product metadata. Title in `{typography.title-sm}`, SKU in `{typography.product-code}` (condensed, 0.5px tracking for alphanumeric scan-reading). Hover lifts border to `{colors.primary}` without shadow — a deliberate choice that keeps the catalog grid low-noise and non-gamified. Price or "Request Quote" label sits below the code in `{typography.body-sm}`.

**`category-tile`** — Icon-forward tile with a centered label in `{typography.title-sm}` on a `{colors.surface-soft}` background; hover transitions fill to white and border to `{colors.primary}`, drawing the eye without animation overhead. Used on the homepage and top-level category landing pages to funnel buyers into product families quickly. Icon treatment uses Bootstrap Glyphicons or SVG equivalents at ~48px.

**`spec-table`** — Dense specification layout using `proxima-nova-condensed` for column labels (`{typography.spec-label}`, uppercase, 0.5px tracked) and `{typography.body-sm}` for values. Alternating rows use `{colors.surface-mid}` against white; header row uses `{colors.surface-soft}` with `{colors.ink}` labels. Handles finish options, dimension ranges (often 4–6 width variants per SKU), weight capacities, substrate types, warranty terms, and ADA compliance indicators. This component is the primary decision surface for B2B procurement.

**`filter-sidebar`** — Left-rail filter panel in `{colors.surface-soft}` with a `{colors.hairline}` right border. Filter group headings use `{typography.filter-label}` in `{colors.ink}`; checkbox labels use `{typography.body-sm}`; active checkboxes accent in `{colors.primary}`. Facets typically include Mounting Type, Surface Material, Frame Color, Size Range, and Series — expect 6–10 filter groups on a typical category page.

**`product-badge`** and **`product-badge-new`** — Two-slot badge system: `{colors.secondary}` (`#aacccc`) for evergreen category or material tags ("Porcelain," "Cork," "Fabric"), `{colors.primary}` for promotional or new-arrival labels. Both use `{typography.caption}` at `{rounded.xs}` — precise enough to sit flush against product codes and image corners without visual bloat. Badges layer into the top-left corner of the product card image.

### Layout
**`hero-banner`** — Full-width `#4b4f54` charcoal banner with heading in `{typography.display-xl}` and subhead in `{typography.body-md}`, both in white. Minimum 320px height; used on category landing pages and campaign entry points. A single `button-primary` CTA sits below the subhead. The charcoal background allows product photography with lighter tones to integrate cleanly when positioned right-aligned within the banner.

### Feedback
**`alert-success`**, **`alert-danger`**, and **`alert-warning`** — Bootstrap-derived alert blocks used in quote confirmation flows, form validation feedback, and stock-availability notices. Success uses `{colors.state-success-bg}` / `{colors.state-success-text}`; danger uses `{colors.state-danger-bg}` / `{colors.state-danger-text}`; warning uses `{colors.state-warning-bg}` / `{colors.state-warning-text}`. These are system-functional rather than brand-expressive and should not be repurposed for decorative content blocks.

### Footer
**`footer`** — Dark `#4b4f54` footer with white body text and `#aacccc` sage for links — the secondary teal reads as warm accent against dark rather than the cold primary at `#37c2dd`. Four-column layout covers product categories, resources (CAD files, installation guides), company info, and contact details. `proxima-nova-condensed` handles address blocks and phone numbers where horizontal density matters. Section headings use `{typography.title-sm}` in white.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger toggle revealing off-canvas drawer; search bar drops below logo row; hero-banner min-height reduces to 200px and heading drops to `{typography.display-md}`; spec-table scrolls horizontally; filter-sidebar becomes a modal sheet triggered by "Filter" button |
| Tablet | 744–1128px | Two-column product grid; top-utility bar remains visible; nav labels truncate or wrap to two lines; filter-sidebar collapses to horizontal pill-strip above grid; hero-banner at 240px |
| Desktop | 1128–1440px | Three or four-column product grid; full nav with mega-menu dropdowns for category subcategories; hero-banner at full 320px; filter-sidebar visible as persistent left rail; spec-table fully expanded |
| Wide | > 1440px | Max content width constrains at ~1400px with centered layout; hero-banner background bleeds edge-to-edge while content stays centered; product grid holds at four columns with increased card padding |

### Touch Targets
- All primary and secondary buttons maintain 40px minimum height on mobile
- nav-bar hamburger toggle padded to 44×44px tap area
- product-card entire surface is a single tap target — not just the title text
- Quantity increment/decrement steppers use minimum 38px height and 44px width
- Filter checkboxes padded to 32px vertical zones within the filter sheet
- Breadcrumb links padded to 32px touch height on mobile with increased horizontal padding

### Collapsing Strategy
- Primary nav collapses to an off-canvas drawer at < 744px; second-level categories become accordion items within the drawer, defaulting to collapsed
- Spec table scrolls horizontally on mobile rather than reflowing — column alignment is essential for cross-variant comparison and must not be broken
- Hero banner heading scales from `{typography.display-xl}` (42px) to `{typography.display-md}` (28px) below 744px; subhead remains `{typography.body-md}`
- Category tiles reflow from a 4-column grid on desktop to 2-column at tablet and a 2-column grid on mobile (tiles are compact enough to remain legible at half width)
- Footer columns stack vertically on mobile with collapsible accordion sections per column, defaulting closed to reduce scroll length
- Filter sidebar transitions from persistent left rail (desktop) to horizontal chip strip (tablet) to full-screen modal sheet (mobile)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Canvas white (`#ffffff`) does not appear in the extracted color list; it is assumed as the base page surface but could not be confirmed directly — `#f6f6f6` and `#f5f5f5` may serve as the true canvas on some sections
- `primary-active` (`#1fa8c3`), `primary-disabled` (`#a8dde6`), and `secondary-active` (`#8bb5b5`) are derived programmatically from the extracted primary and secondary values — not observed directly in the live site
- `mr-eaves-xl-modern` is confirmed in the font-family stack but specific weight usage (300 vs 600 vs 700) in display headings could not be extracted; weights here are inferred from humanist display conventions
- No custom icon system confirmed — Bootstrap Glyphicons Halflings is present in the font stack, suggesting Bootstrap icons are the primary icon set, but a proprietary SVG glyph library may supplement it for product-category imagery
- No transition timing or animation easing data was extractable — motion behavior (hover transitions, drawer open/close, accordion) is entirely inferred
- `open_sanslight` is in the font stack but no clear usage context was identified; it may be a legacy or secondary body weight no longer actively used
- Dark mode, high-contrast mode, or accessibility-variant color schemes were not observed in extraction
- Product photography treatment (pure white cut-out vs. environment/lifestyle) and image aspect ratio enforcement could not be confirmed from extraction alone
- Actual mega-menu structure and second-level category hierarchy not confirmed — component assumes standard dropdown but nav depth and layout are unverified
