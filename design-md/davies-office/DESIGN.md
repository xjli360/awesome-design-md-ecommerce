---
version: alpha
name: "Davies Office"
source_url: "https://www.daviesoffice.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The 30-color extracted palette reads almost entirely as Bootstrap 3's semantic alert system — success greens (#3c763d, #dff0d8), warning ambers (#8a6d3b, #fcf8e3), danger reds (#a94442, #f2dede), info teals (#31708f, #d9edf7) — deployed not as decoration but as live product-status and availability signals across a dense B2B catalog. The brand's own voltage arrives in two blues that step outside Bootstrap's defaults: a deep corporate #0072cf sits as the true primary action color, while #00b4e0 lifts it as a lighter, more dynamic accent used in feature callouts and search interactions. Between these blues runs a charcoal-to-gray text system (#36373a ink, #777777 secondary, #9d9d9d hint) that keeps product data legible across dense specification tables. Open Sans carries all the work — weights 400 through 700 across sizes that prioritize scan-ability over display drama. The interface trusts function over personality: near-square-cornered cards, subdued borders (#eeeeee, #e5e5e5), and flat surfaces that step back behind product photography. The sustainability mandate from the page title surfaces in green badge states and category callouts rather than in decorative illustration. Components favor grid density over whitespace generosity — a horizontal nav with dropdown category mega-menus, filterable product grids with specification-heavy cards, and Bootstrap-inherited form controls built for quote requests and procurement workflows. The overall effect is a catalog-first workspace designed for office managers and facilities buyers who need confidence and specificity, not an emotional brand journey.

colors:
  primary: "#0072cf"
  primary-active: "#286090"
  primary-disabled: "#4a89bf"
  primary-light: "#4a89bf"
  secondary-cyan: "#00b4e0"
  ink: "#222222"
  body: "#36373a"
  muted: "#777777"
  muted-soft: "#9d9d9d"
  hairline: "#eeeeee"
  hairline-soft: "#e5e5e5"
  hairline-rule: "#e7e7e7"
  border-strong: "#555555"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success-text: "#3c763d"
  success-bg: "#dff0d8"
  success-border: "#d6e9c6"
  warning-text: "#8a6d3b"
  warning-bg: "#fcf8e3"
  warning-border: "#faebcc"
  danger-text: "#a94442"
  danger-bg: "#f2dede"
  danger-border: "#ebccd1"
  info-text: "#31708f"
  info-bg: "#d9edf7"
  info-border: "#bce8f1"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  table-header:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  label:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  status-badge:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
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
    padding: 8px 16px
    height: 36px
    border: none
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
    padding: 7px 15px
    height: 36px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    borderColor: "{colors.primary-active}"
    textColor: "{colors.primary-active}"
  button-danger:
    backgroundColor: "{colors.danger-text}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-success:
    backgroundColor: "{colors.success-text}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(0,114,207,0.15)"
  nav-top-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 32px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 50px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspect: "4/3"
    hoverBorderColor: "{colors.primary}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.primary}"
  product-card-price:
    typography: "{typography.title-md}"
    textColor: "{colors.body}"
    fontWeight: 700
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    hoverBorderColor: "{colors.primary}"
  alert-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.success-border}"
    padding: "10px 16px"
  alert-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.warning-border}"
    padding: "10px 16px"
  alert-danger:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.danger-border}"
    padding: "10px 16px"
  alert-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.info-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.info-border}"
    padding: "10px 16px"
  status-badge-in-stock:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text}"
    typography: "{typography.status-badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    border: "1px solid {colors.success-border}"
  status-badge-low-stock:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning-text}"
    typography: "{typography.status-badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    border: "1px solid {colors.warning-border}"
  status-badge-out-of-stock:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger-text}"
    typography: "{typography.status-badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    border: "1px solid {colors.danger-border}"
  status-badge-sustainable:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text}"
    typography: "{typography.status-badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
    border: "1px solid {colors.success-border}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
    padding: "0 12px"
  search-button:
    backgroundColor: "{colors.secondary-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    roundedRight: "{rounded.sm}"
    roundedLeft: "{rounded.none}"
    height: 40px
    padding: "0 20px"
  data-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.body}"
    headerTypography: "{typography.table-header}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rowHoverBackgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.body}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    borderRight: "1px solid {colors.hairline}"
    labelTypography: "{typography.label}"
    textColor: "{colors.body}"
    checkboxAccentColor: "{colors.primary}"
  quote-request-form:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    labelTypography: "{typography.label}"
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.primary-light}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — Solid #0072cf fill at 36px height, Open Sans semibold 14px, 4px corners (`{rounded.sm}`), and 8px/16px padding. Hover darkens to `{colors.primary-active}` (#286090); disabled washes to `{colors.primary-disabled}` (#4a89bf) without an opacity reduction. Used for all primary catalog CTAs: "Add to Cart", "Request a Quote", "View Product".

**`button-secondary`** — White canvas with a 1px #0072cf border and matching text, same 36px height. Paired alongside `button-primary` on product detail pages for secondary actions such as "Save for Later" or "Download Spec Sheet". Border and text shift to `{colors.primary-active}` on hover; no background fill change.

**`button-danger`** and **`button-success`** — Bootstrap-derived semantic variants at the same 36px height and `{rounded.sm}` rounding. Danger (#a94442) surfaces on destructive form actions and discontinuation notices; Success (#3c763d) appears on order confirmations and "In Stock" CTAs. Both use `{colors.on-primary}` text.

### Alerts & Status Indicators

**`alert-success`**, **`alert-warning`**, **`alert-danger`**, **`alert-info`** — The full Bootstrap 3 alert quartet, each a lightly tinted panel (pastel background, muted border, dark semantic text) at `{rounded.sm}` and 10px/16px padding. These carry real operational meaning: info alerts for shipping policy notices, warning for low-inventory thresholds, danger for discontinued or backordered items, success for order confirmations and recycled-content certifications.

**Status badges** — Four compact inline chips at `{typography.status-badge}` (11px uppercase Open Sans) using the same semantic color system as alerts. `status-badge-in-stock`, `status-badge-low-stock`, and `status-badge-out-of-stock` use `{rounded.xs}` (2px) to read as data labels; `status-badge-sustainable` uses `{rounded.full}` to visually distinguish eco-certification from inventory states and reinforce the brand's sustainability positioning.

### Navigation

**`nav-top-strip`** — A 32px #0072cf header bar carrying utility links (account, order tracking, contact) in white caption text. This is the first brand-color signal on page load and frames the page before the main nav renders.

**`nav-bar`** — A 50px white bar below the strip with Open Sans semibold nav links and a `{colors.hairline}` bottom border. On desktop it expands to a mega-menu with category columns; on tablet and below it collapses to a hamburger toggle. The nav sits flush against the top strip with no gap.

### Product Catalog

**`product-card`** — White-surface card with 1px `{colors.hairline}` border and `{rounded.sm}` corners, `{spacing.base}` interior padding. Product name links render in `{colors.primary}` at `{typography.title-md}`; price renders in fontWeight 700 body text. Image region locks to a 4:3 aspect ratio. The entire card border shifts to `{colors.primary}` on hover — not a shadow, just a border color swap consistent with the flat, utilitarian aesthetic.

**`category-tile`** — A `{colors.surface-soft}` tile for homepage and category landing pages, grouping major catalog segments (Filing, Storage, Seating, Desks). Displays a category icon, title at `{typography.title-md}`, and optional product count in `{colors.muted}`. Border highlights to `{colors.primary}` on hover.

### Search

**`search-bar`** with **`search-button`** — An inline pair: a 40px text input with a flush-attached `{colors.secondary-cyan}` submit button (no gap, shared height, rounded only on the right side). The #00b4e0 cyan deliberately breaks from the primary blue to signal a distinct search-mode register. The input itself uses `{colors.hairline}` border; focus state adds a soft #0072cf glow ring.

### Data & Forms

**`data-table`** — Dense specification tables for product comparisons, order histories, and compatibility matrices. Header row sits on `{colors.surface-soft}` with `{typography.table-header}` (13px, all-caps, +0.3px tracking); body rows are white with `{colors.hairline}` borders and a `{colors.surface-soft}` hover highlight. No banded stripe pattern — the grid relies on borders alone for row separation.

**`filter-sidebar`** — Left-rail filter panel with labeled checkbox groups at `{typography.label}`. Checkboxes accent in `{colors.primary}`; section headings render at `{typography.title-md}`. Collapses to an overlay drawer on mobile.

**`quote-request-form`** — A `{colors.surface-soft}` panel for B2B procurement requests, `{rounded.md}` corners, `{spacing.xl}` internal padding. Form fields follow the `text-input` pattern with `text-input-focus` ring states. Submit button is `button-primary`. Targeted at office managers requesting volume pricing.

**`footer`** — Dark charcoal (#36373a) base with white body text and #4a89bf link color for legibility on dark. A 3px #0072cf top border anchors the footer to the primary brand blue. Typography at `{typography.body-sm}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, filter sidebar becomes full-screen drawer overlay, search bar expands full-width below strip, nav-top-strip condenses to cart and account icons only |
| Tablet | 744–1128px | Two-column product grid, nav bar retains horizontal links but no mega-menu dropdowns, filter sidebar collapses to a toggle button above grid |
| Desktop | 1128–1440px | Three-column product grid, full mega-menu dropdowns on hover, filter sidebar as fixed left rail (~240px), quote-request-form floats as right-rail aside on product pages |
| Wide | > 1440px | Four-column product grid, max-width container (~1400px) centered, nav-top-strip may surface promotional text |

### Touch Targets

- All buttons expand to minimum 44px height on mobile (up from desktop 36px via padding increase)
- Filter checkboxes have minimum 44×44px tap area with padding compensation
- Mobile nav drawer links minimum 48px height per row
- Product card entire surface is tappable, not just the title link
- Search-button expands to 44px height on mobile

### Collapsing Strategy

- Mega-menu nav collapses to hamburger drawer at < 1128px; top strip reduces to icon row only at < 744px
- Filter sidebar transitions from fixed left rail → above-grid toggle panel → full-screen drawer as viewport narrows
- Data tables gain a horizontal scroll wrapper on mobile with sticky first column (product name) for orientation
- Quote-request-form moves from aside float to full-width stacked layout below product details at mobile breakpoint
- Category tiles reflow from a 4- or 6-up grid to a 2-up grid on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed custom brand typeface — Open Sans inferred from font stack; exact weight split (400/600/700) and size ramp are estimates based on B2B catalog norms
- Meta theme-color absent — mobile status bar color unconfirmed; #0072cf used as best-fit
- Custom icon set (`aslsicons2`) found in font-family stack — glyph map, sizing, and usage contexts not determinable from static extraction
- Mega-menu structure (column count, featured image slots, nested depth) not extractable without JavaScript rendering
- `danger-border: "#ebccd1"` is a Bootstrap 3 framework default, not confirmed as an explicit brand override — may be identical to live site but cannot be verified from extraction alone
- Dark mode palette unknown — no `prefers-color-scheme` tokens observed
- Confirmed logo dimensions, SVG lockup, and clearance rules not extractable
- Hover/focus animation timing and easing not derivable from static extraction
- Cart drawer and checkout flow color usage unconfirmed
- Bootstrap 3 heritage means many semantic colors (#337ab7, #5cb85c, #d9534f, etc.) may be unchanged framework defaults rather than deliberate brand tokens — true custom overrides cannot be fully isolated from extraction alone
