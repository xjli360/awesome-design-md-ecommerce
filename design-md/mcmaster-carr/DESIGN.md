---
version: alpha
name: "McMaster-Carr"
source_url: "https://www.mcmaster.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  McMaster-Carr's forest-green nav bar (#336633) is one of the most recognizable surfaces in B2B e-commerce — unchanged in character for decades while the rest of the industrial web cycled through skeuomorphism, flat design, and dark mode in succession. The homepage presents no hero image, no promotional carousel, no lifestyle photography: a search bar, a category grid, and a green header. This compression is intentional. The user is an engineer with a part number, a purchasing agent with a deadline, or a maintenance tech with a broken machine — none of them came to browse. The design's job is to disappear. Palette authority is split between the primary forest green (#336633) and an industrial-link blue (#4499dd), with dark blue (#006699) anchoring hover and active link states. Safety-yellow (#fed700) is reserved for stock alerts and availability callouts; the three yellow shades from pale (#ffffb5) to saturated (#feec00) function as a caution-tape system — when yellow appears on McMaster's interface, something time-sensitive is being communicated. Alternating table rows oscillate between white canvas and #efefef with hairlines at #d6d6d6, building the visual rhythm that lets a buyer scan 200 product variants in seconds. Typography reaches for the engineering drawing board: DINNextLTPro-Medium carries navigation and UI chrome — DIN being the typeface literally designed for German industrial signage and engineering documentation — while FuturaLTPro-BoldCond handles condensed display headings with geometric authority, and HelveticaNeueeTextPro-Roman runs body and table text at 12–13px, tighter than consumer web norms because screen real estate serves data, not breathing room. Corner radii are nearly zero throughout — `{rounded.xs}` at 2px or flat `{rounded.none}` everywhere — and button heights at 32px and input heights at 26px reflect monitor-first design for warehouse offices and engineering workstations, not thumb-scroll ergonomics. The entire system encodes one proposition: get the right part into the right hands with zero friction, and everything else is overhead.

colors:
  primary: "#336633"
  primary-active: "#1d591d"
  primary-disabled: "#878787"
  primary-light: "#3c773c"
  accent-blue: "#4499dd"
  accent-blue-dark: "#006699"
  highlight: "#fed700"
  highlight-bright: "#feec00"
  highlight-amber: "#fec914"
  highlight-pale: "#ffffb5"
  ink: "#222222"
  body: "#333333"
  muted: "#777777"
  muted-mid: "#888888"
  muted-light: "#a0a0a0"
  hairline: "#d6d6d6"
  hairline-mid: "#cbcbcb"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#efefef"
  surface-card: "#ffffff"
  surface-green-tint: "#edf2ed"
  on-primary: "#ffffff"
  nav-border: "#3c773c"

typography:
  display-xl:
    fontFamily: "'FuturaLTPro-BoldCond', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0.5px
  display-md:
    fontFamily: "'FuturaLTPro-BoldCond', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  display-sm:
    fontFamily: "'FuturaLTPro-BoldCond', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'DINNextLTPro-Medium', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'DINNextLTPro-Medium', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'HelveticaNeueeTextPro-Roman', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  body-md-med:
    fontFamily: "'HelveticaNeueeTextPro-Md', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0
  body-sm:
    fontFamily: "'HelveticaNeueeTextPro-Roman', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-md:
    fontFamily: "'DINNextLTPro-Medium', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "'DINNextLTPro-Medium', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'DINNextLTPro-Medium', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  search-input:
    fontFamily: "Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  table-header:
    fontFamily: "'HelveticaNeueeTextPro-Md', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px
  part-number:
    fontFamily: "'HelveticaNeueeTextPro-Md', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  category-label:
    fontFamily: "'FuturaLTPro-BoldCond', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 10px
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
    rounded: "{rounded.xs}"
    padding: 6px 14px
    height: 32px
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
    textColor: "{colors.accent-blue-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 5px 13px
    border: "1px solid {colors.hairline}"
    height: 32px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 18px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-light}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 4px 8px
    height: 26px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.search-input}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonTypography: "{typography.button-md}"
    height: 38px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 36px
    borderBottom: "2px solid {colors.nav-border}"
  nav-bar-utility:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    height: 24px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  product-table-row:
    backgroundColor: "{colors.canvas}"
    altBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.xs} {spacing.sm}"
  product-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.table-header}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xs} {spacing.sm}"
  part-number-display:
    textColor: "{colors.accent-blue-dark}"
    typography: "{typography.part-number}"
    textDecoration: underline
  spec-highlight-row:
    backgroundColor: "{colors.highlight-pale}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.highlight-amber}"
  category-nav-item:
    backgroundColor: "{colors.surface-green-tint}"
    textColor: "{colors.primary-active}"
    typography: "{typography.category-label}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
    borderLeft: "3px solid {colors.primary}"
  quantity-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md-med}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    width: 48px
    height: 26px
  breadcrumb:
    textColor: "{colors.accent-blue-dark}"
    separatorColor: "{colors.muted-light}"
    typography: "{typography.body-sm}"
  availability-badge-in-stock:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "1px 5px"
  availability-badge-alert:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "1px 5px"
  filter-chip:
    backgroundColor: "{colors.surface-green-tint}"
    textColor: "{colors.primary-active}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary-light}"
    padding: "2px 8px"
  section-heading:
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    borderBottom: "2px solid {colors.primary}"
    paddingBottom: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg} {spacing.section}"

---

## Components

### Buttons

**`button-primary`** — Forest-green (#336633) fill with white DINNextLTPro-Medium text at 32px tall and a barely-perceptible 2px corner radius. Padding is intentionally compressed (6px × 14px) — this is a monitor-first UI where hover precision replaces generous touch targets. Active state darkens to #1d591d; disabled collapses to neutral gray (#878787) with no opacity trick. The green CTA reads as "proceed" against every surface in the system.

**`button-secondary`** — White canvas with a 1px hairline border and dark blue (#006699) text. Used for secondary flows: Save to List, Request Quote, Print, and Cancel confirmations. The low visual mass ensures the green primary button always wins hierarchy in mixed-action rows.

**`button-add-to-cart`** — Visually identical to `button-primary` with slightly wider horizontal padding (18px vs 14px). Appears inline at the right edge of every product table row and on detail pages. The green reinforces "proceed" at the terminal step of the purchase flow without introducing a distinct third button style.

### Search

**`search-bar`** — The defining UI element of mcmaster.com. A full-width input at 38px height with a forest-green submit button flush at the right edge — no gap, no visual separation. The input runs 16px Arial for legibility of alphanumeric part codes (e.g., 91290A121). A hairline border frames the input field; the button is flush green with white label text. No rounded pill shape: `{rounded.xs}` at 2px keeps the geometry industrial. This component is the entry point for the overwhelming majority of sessions and receives the most prominent real estate on every page.

### Navigation

**`nav-bar`** — A 36px forest-green (#336633) bar with white DINNextLTPro-Medium nav links and a 2px darker-green (#3c773c) bottom border that provides depth without a drop shadow. The McMaster wordmark anchors the left; category links span the center; account, order history, and cart cluster at the right. Link hover states lighten slightly against the green field.

**`nav-bar-utility`** — A 24px secondary bar in light gray (#efefef) with 11px Arial caption text. Carries account-management links, customer service phone number, and subsidiary navigation. Visually subordinate and never competes with the green primary bar.

**`section-heading`** — Category and product-group headings use FuturaLTPro-BoldCond at 16px with a 2px primary-green bottom border. This green underline treatment recurs throughout the site as a section delineator, creating visual rhythm across dense content pages without adding background color blocks.

### Product Data

**`product-table-row`** — The functional core of the McMaster experience. Rows alternate between white canvas and #efefef with a 1px hairline bottom border at #eeeeee. Each row packs: part number (blue underlined link), 4–8 specification columns, price, quantity input, and add-to-cart button — all at 13px HelveticaNeueeTextPro-Roman. Row height is minimized to maximize visible variant count. This component must accommodate up to 10 columns on wide desktop without horizontal scroll.

**`product-table-header`** — Light gray (#efefef) background with 12px HelveticaNeueeTextPro-Md column labels in ink. A 1px hairline bottom border separates headers from data rows. Labels are entirely functional — "Diameter," "Thread Size," "Tensile Strength" — with no sort icons unless interaction is active.

**`part-number-display`** — McMaster part numbers rendered in HelveticaNeueeTextPro-Md at 13px, 0.2px letter-spacing, underlined in dark blue (#006699). The slight extra tracking aids legibility of dense alphanumeric codes. Clicking navigates to the part detail page; the underline is always visible (not hover-only), treating every part number as an explicit navigational affordance.

**`spec-highlight-row`** — When a query parameter matches a specification value within a table row, the matching cell or entire row shifts to pale yellow (#ffffb5) background with an amber-tinted border (#fec914). This search-relevance signal operates without changing row geometry — no padding expansion, no icon injection. The yellow reads as "this is why this row surfaced."

### Category Navigation

**`category-nav-item`** — Left-rail category links on the surface-green-tint (#edf2ed) background with a 3px primary-green left border accent. Futura condensed uppercase at 13px with 0.4px tracking. Active item gets a deeper green-tint background; inactive items sit in the pale green surface. The entire left-rail pattern — from top-level category pages to product-group filter panels — uses this single component token, maintaining structural consistency across a catalog of millions of SKUs.

**`filter-chip`** — Applied filter tags in the green-tinted surface with a primary-light border. Used to display active refinements (material, thread type, diameter range) above or beside the product table. Dismissable via an inline × character at the right of each chip.

### Inputs and Controls

**`text-input`** — 26px tall, 1px hairline border, 4px vertical padding. Appears in filter panels, login forms, address fields, and order-management interfaces. The tight height pairs with button height (32px) for inline-form alignment without extra wrapper padding.

**`quantity-input`** — A narrow (48px wide) numeric input for order quantities, matching `text-input` height at 26px. Sits inline with `button-add-to-cart` in product table rows. The pair — quantity field then green button — is the highest-frequency interaction pattern on the site and the only place where two interactive elements share a row without separation.

### Badges and Status

**`availability-badge-in-stock`** — 0-radius green badge with white 11px caption text. Values include "In Stock," "Ships Today," and specific ship-date callouts. Appears in product tables as a positive confirmation signal; the green color reinforces the primary brand hue at a functional tier.

**`availability-badge-alert`** — Safety-yellow (#fed700) fill with ink text. Signals limited stock, lead-time notices, or delivery exceptions. The yellow-on-white contrast against a neutral table row reads as caution without being an error state — exactly the industrial color convention (yellow = attention, red = stop) applied to inventory communication.

### Footer

**`footer`** — Light gray (#efefef) surface with muted gray (#777777) body-sm text. Contains legal language, regulatory compliance links, subsidiary addresses, and contact information. A 1px hairline top border separates it from page content. No newsletter signup, no social grid, no promotional block — the footer is strictly informational, consistent with the zero-decoration design stance across the rest of the site.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Search bar dominates above the fold at full width; category nav collapses into a hamburger drawer; product tables reflow to stacked cards with one product per card; quantity input and add-to-cart button stack vertically within card; font sizes increase by 1–2px for tap legibility |
| Tablet | 744–1128px | Two-column product layout where feasible; category nav appears as a collapsible left-rail panel toggled by a Filter button; search bar retains full width within the content column; nav-bar secondary links may truncate or move to a utility row |
| Desktop | 1128–1440px | Standard 6–10 column product table; left-rail category nav fixed at ~220px width; nav-bar shows all primary category links without overflow; part-number and spec columns render at full width |
| Wide | > 1440px | Content column constrained to ~1200–1300px centered with white margin fill; no additional columns added — data density is already maximized at desktop widths; search bar max-width caps to match content column |

### Touch Targets

- `button-primary` and `button-add-to-cart` at 32px height fall below the 44px iOS/Android minimum — acceptable for desktop primary use, requires height increase on mobile breakpoints
- `quantity-input` at 26px is significantly undersized for touch; mobile view should expand to at least 40px with wider tap area
- Nav-bar at 36px height is borderline adequate for touch; primary category links need 44px touch target minimum on mobile
- `category-nav-item` padding should expand to a minimum 44px touch height on mobile (currently `{spacing.xs}` vertical is too tight)
- Part-number links at 13px should receive increased line-height or padding on touch viewports to prevent misfire

### Collapsing Strategy

- Primary nav links collapse right-to-left: specialty subcategories first, then secondary category families, with the wordmark and account cluster always visible
- Product spec tables simplify from 8–10 columns at desktop to 3–4 columns on tablet: part number, primary distinguishing spec, price, and quantity — remaining specs move into a row-expansion accordion
- Filter/category left rail moves from a fixed panel to a bottom-sheet drawer on mobile, triggered by a "Filters" button pinned above the product list
- Search bar is persistent and full-width at all breakpoints — it is never collapsed, hidden, or moved below the fold
- Breadcrumb may truncate to the immediate parent category on mobile to preserve horizontal space

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Body text and ink hex values (#222222, #333333) are not extracted from the site; these are standard-dark assumptions for a black-on-white table interface and may not match McMaster's actual computed values
- Canvas color assumed to be pure white (#ffffff); a very slight warm or neutral off-white cannot be ruled out from extraction
- Button height (32px) and input height (26px) are inferred from visual convention, not from measured extraction
- DINNextLTPro-Medium, FuturaLTPro-BoldCond, and HelveticaNeueeTextPro are confirmed in the font-family stack but no computed font sizes, weights, or line-heights were extracted; type scale values are reconstructed from visual patterns and industrial-UI convention
- Hover states for nav links, part-number links, table rows, and filter chips were not captured in extraction
- Error and validation states for `text-input` (error border color, error text color) are undocumented
- Cart, checkout, and order-management UI — which may carry their own component variants — were not extracted
- Icon system is not characterized; McMaster uses minimal iconography and any icon assets or glyph library are unknown
- Mobile breakpoint pixel values are estimated; McMaster's actual CSS breakpoints may differ from the values used here
- Whether McMaster uses CSS custom properties at runtime or a compiled static CSS approach is unknown; design tokens here are reconstructed rather than extracted from live CSS variables
- The #cbcbcb, #c9c9c9, and #a0a0a0 grays from the extraction are not mapped to named tokens; their specific UI roles (disabled borders, scrollbar tracks, placeholder text) are undetermined
