---
version: alpha
name: "Danby"
source_url: "https://www.danby.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep navy (#002d52) dominates Danby's digital presence the way a powder-coat finish dominates the front panel of a countertop dishwasher — total, opaque, unapologetic. The Canadian appliance specialist builds its interface on two blues: the anchoring midnight navy for navigation bars, footers, and section headers, and a high-contrast action blue (#0072ce) reserved exclusively for CTAs, inline links, and interactive affordances. Between them sits a quieter steel blue (#2176bd) that bridges the two in hover states and secondary accents, giving the palette a three-stop gradient that reads like brushed aluminum transitioning to anodized chrome. Typography runs Poppins — a geometric sans-serif with perfectly circular counters — paired with an Arial/Helvetica system stack as its fallback. Headings arrive at weight 600–700 with tight letter-spacing, lending the utilitarian directness you'd expect from a brand that sells freezers by their cubic-foot capacity, not lifestyle aspiration. Body text stays at 400 weight and 1.6 line-height for the long specification lists and product descriptions that appliance shoppers actually read. The layout grid is Bootstrap-informed: 12-column with `{spacing.base}` 16px gutters, `{spacing.section}` 64px vertical rhythm between content bands, and product cards that snap from four-across on desktop to a single scrollable column on mobile. Corners stay modest — `{rounded.sm}` 8px on cards and inputs, `{rounded.xs}` 4px on badges and tags — because this is an appliance catalog, not a social app, and sharp geometry signals precision engineering. Product cards foreground the hero image at a fixed 4:3 ratio, with model number, short title, and a price stack below; an "Add to Compare" checkbox rides the card's top-right corner, reflecting the comparison-shopping behavior endemic to major-appliance purchases. The footer is a dense, navy-backed (#001439) four-column grid carrying support links, warranty info, dealer locators, and the bilingual English/French toggle that marks Danby as distinctly Canadian. Alert-state colors (#3c763d success green, #a94442 error red, #8a6d3b warning amber) appear in inventory badges and form validation but never in brand messaging — they are infrastructure, not identity.

colors:
  primary: "#002d52"
  primary-light: "#0072ce"
  primary-active: "#0059b5"
  primary-disabled: "#8ab4d7"
  accent-blue: "#2176bd"
  accent-blue-hover: "#286090"
  link: "#0072ce"
  link-hover: "#003388"
  ink: "#020202"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#9d9d9d"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  border-strong: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-muted: "#f5f5f5"
  surface-card: "#ffffff"
  surface-tint: "#ebf6ff"
  surface-warm: "#f0f0f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  footer-bg: "#001439"
  panel-info-bg: "#d9edf7"
  panel-info-text: "#31708f"
  panel-success-bg: "#dff0d8"
  panel-success-text: "#3c763d"
  panel-warning-bg: "#fcf8e3"
  panel-warning-text: "#8a6d3b"
  panel-danger-bg: "#f2dede"
  panel-danger-text: "#a94442"
  success: "#5cb85c"
  info: "#5bc0de"
  near-black: "#080808"

typography:
  display-xl:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.15px
  button-lg:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  nav-link-sm:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  spec-label:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  spec-value:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  price-display:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  model-number:
    fontFamily: "'Consolas', 'Courier New', Monaco, Menlo, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.5px

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
  section-lg: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 24px
    height: 44px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.65
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 23px
    height: 44px
    border: 1px solid {colors.primary}
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 24px
    height: 44px
  button-info:
    backgroundColor: "{colors.info}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  button-sm:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary-light}
    boxShadowFocus: 0 0 0 2px {colors.surface-tint}
  text-input-error:
    border: 1px solid {colors.panel-danger-text}
    boxShadow: 0 0 0 2px {colors.panel-danger-bg}
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 32px 8px 12px
    height: 40px
    border: 1px solid {colors.hairline}
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 {spacing.lg}
    borderBottom: none
  nav-bar-top:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link-sm}"
    height: 36px
    padding: 0 {spacing.lg}
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} 0"
    boxShadow: 0 4px 16px rgba(0,0,0,0.12)
    border: 1px solid {colors.hairline-soft}
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg} {spacing.xl}"
    boxShadow: 0 8px 24px rgba(0,0,0,0.1)
    borderTop: 3px solid {colors.primary-light}
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
    boxShadowHover: 0 4px 16px rgba(0,0,0,0.08)
    imageRatio: "4:3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    modelTypography: "{typography.model-number}"
  product-card-compare-checkbox:
    position: top-right
    offset: "{spacing.sm}"
    typography: "{typography.caption-sm}"
    accentColor: "{colors.primary-light}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-lg}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 420px
    ctaStyle: button-secondary-inverted
  hero-banner-light:
    backgroundColor: "{colors.surface-tint}"
    textColor: "{colors.primary}"
    titleTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-lg}"
    padding: "{spacing.section} {spacing.xl}"
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    imageRatio: "1:1"
    border: 1px solid {colors.hairline-soft}
    hoverBorder: 1px solid {colors.primary-light}
  badge-new:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.panel-danger-text}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-energy:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-stock:
    backgroundColor: "{colors.panel-success-bg}"
    textColor: "{colors.panel-success-text}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  badge-out-of-stock:
    backgroundColor: "{colors.panel-danger-bg}"
    textColor: "{colors.panel-danger-text}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    padding: 0 44px 0 16px
    border: 2px solid {colors.primary-light}
    iconColor: "{colors.primary-light}"
  search-bar-button:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.on-primary}"
    rounded: "0 {rounded.xs} {rounded.xs} 0"
    height: 44px
    width: 44px
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    separator: "/"
    separatorColor: "{colors.muted-soft}"
    padding: "{spacing.md} 0"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    rowPadding: "{spacing.sm} {spacing.base}"
    stripeColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline-soft}"
  spec-table-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    headerBg: "{colors.surface-tint}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    cellPadding: "{spacing.md} {spacing.base}"
    borderColor: "{colors.hairline}"
    maxProducts: 4
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    titleTypography: "{typography.title-sm}"
    width: 260px
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline-soft}
    checkboxAccent: "{colors.primary-light}"
  alert-info:
    backgroundColor: "{colors.panel-info-bg}"
    textColor: "{colors.panel-info-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    border: 1px solid {colors.info}
  alert-success:
    backgroundColor: "{colors.panel-success-bg}"
    textColor: "{colors.panel-success-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    border: 1px solid {colors.success}
  alert-warning:
    backgroundColor: "{colors.panel-warning-bg}"
    textColor: "{colors.panel-warning-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
  alert-danger:
    backgroundColor: "{colors.panel-danger-bg}"
    textColor: "{colors.panel-danger-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    border: 1px solid {colors.panel-danger-text}
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.link}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
    columns: 4
    borderTop: 4px solid {colors.primary-light}
  footer-bottom:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption-sm}"
    padding: "{spacing.base} {spacing.xl}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    activeBackground: "{colors.primary-light}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    itemSize: 36px
    border: 1px solid {colors.hairline}
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
    maxWidth: 240px

---

## Components

### Buttons

**`button-primary`** — Danby's primary action button uses the bright action blue (#0072ce) background with white text at `{typography.button-md}`. Corners are `{rounded.xs}` (4px), keeping the industrial precision feel. On hover, background darkens to the primary-active (#0059b5). Disabled state reduces to #8ab4d7 at 65% opacity. Height is a consistent 44px with 10px 24px padding.

**`button-secondary`** — White background with a 1px navy border and navy text. On hover, it fills entirely with `{colors.primary}` and text inverts to white — a full swap, not a subtle tint shift. Same 44px height and `{rounded.xs}` rounding as the primary.

**`button-success`** — Green (#5cb85c) variant used for "Add to Cart" and confirmation actions. Same structural dimensions as button-primary. Conveys positive-completion intent distinct from navigation blues.

**`button-info`** — Lighter informational button in #5bc0de, used for "Learn More" and "View Details" tertiary actions. Slightly smaller at 36px height with `{typography.button-sm}`.

### Text Input

**`text-input`** — 40px height, 1px `{colors.hairline}` border, `{rounded.xs}` corners. On focus, border shifts to `{colors.primary-light}` with a 2px light-blue ring (`{colors.surface-tint}`). Error state swaps to red border with a pink shadow ring. The minimal rounding and sharp focus ring keep inputs looking like instrument panels rather than social-app fields.

### Navigation

**`nav-bar`** — A two-tier navigation system. The top strip (`nav-bar-top`) is near-black (#001439) at 36px, carrying utility links (dealer locator, language toggle, account). The main bar sits at 64px height with the brand's primary navy (#002d52) background. Dropdown menus emerge as white panels with a 3px blue top-border accent (`mega-menu`) and subtle box-shadow, giving depth without competing with the dark header.

**`nav-dropdown`** — White surface with `{rounded.xs}` corners and a 16px box-shadow for depth. Links use `{typography.body-md}` and highlight on hover with `{colors.surface-tint}` background. The dropdown appears flush below the nav-bar with no gap.

### Product Card

**`product-card`** — White card with 1px `{colors.hairline-soft}` border and `{rounded.sm}` corners. The product image fills a 4:3 ratio container at the top. Below sits the product title in `{typography.title-sm}`, model number in monospace `{typography.model-number}` (Consolas stack), and price in `{typography.price-sm}`. On hover, the card lifts with a soft shadow (0 4px 16px rgba(0,0,0,0.08)). A compare checkbox sits in the top-right corner — a critical pattern for appliance shoppers evaluating capacity, energy rating, and dimensions across models.

### Hero Banner

**`hero-banner`** — Full-width banner in solid `{colors.primary}` navy with white text. Title runs at `{typography.display-xl}` (36px/700), body text at `{typography.body-lg}`. Minimum height of 420px. Product photography is typically composited on the right side. The CTA uses an inverted secondary style — white outline button on the dark background. A lighter variant (`hero-banner-light`) uses the tinted surface (#ebf6ff) with navy text for promotional sections lower on the page.

### Category Card

**`category-card`** — Square image ratio (1:1) with a soft gray (#f8f8f8) background and `{rounded.sm}` corners. Title sits below in `{typography.title-md}`. On hover, the border shifts from hairline gray to `{colors.primary-light}` — a minimal but clear selection signal. Used on the homepage to route shoppers into appliance categories (dishwashers, refrigerators, freezers, microwaves).

### Badges

**`badge-new`** — Action blue background, white uppercase text at 11px/700. Applied to newly released models. **`badge-sale`** — Red (#a94442) background for clearance and promotional pricing. **`badge-energy`** — Green (#5cb85c) for energy-efficiency certifications. **`badge-stock` / `badge-out-of-stock`** — Tinted background panels using the success/danger alert color pairs for inventory status indicators.

### Spec Table

**`spec-table`** — The workhorse component for appliance product pages. Alternating rows stripe between white and `{colors.surface-soft}`. Labels sit in `{typography.spec-label}` (13px/600), values in `{typography.spec-value}` (13px/400). Section headers get the full navy treatment — `{colors.primary}` background with white text. This is where shoppers spend the most time: dimensions, capacity, noise level, energy consumption, water usage, cycle count.

### Comparison Table

**`comparison-table`** — Side-by-side product comparison grid, up to four products. Header row uses the light tint `{colors.surface-tint}` background. Cell padding is generous at `{spacing.md}` vertical by `{spacing.base}` horizontal. Differences between products can be highlighted with the info panel color pair. The grid collapses to a swipeable horizontal scroll on mobile.

### Filter Sidebar

**`filter-sidebar`** — 260px fixed-width left panel for catalog browsing. Checkbox accents use `{colors.primary-light}`. Category groups are separated by `{colors.hairline-soft}` dividers with `{typography.title-sm}` headers. Price range, dimensions, capacity, and energy rating are the primary filter axes for appliance catalogs.

### Alerts

Four semantic alert levels — **info** (#d9edf7 / #31708f), **success** (#dff0d8 / #3c763d), **warning** (#fcf8e3 / #8a6d3b), **danger** (#f2dede / #a94442) — each using tinted backgrounds with matching text color and `{rounded.xs}` corners. Used for form validation, stock notifications, warranty messages, and shipping updates.

### Search Bar

**`search-bar`** — 44px height with a 2px `{colors.primary-light}` border. The submit button is a solid blue square docked to the right edge, matching the input height. The magnifying-glass icon is white on blue. On mobile, the search bar stretches full-width below the nav.

### Footer

**`footer`** — Dense four-column layout on the near-black (#001439) background with a 4px blue accent along the top edge. Links render in `{colors.hairline}` gray and brighten to white on hover. The bottom sub-footer strip drops to `{colors.near-black}` (#080808) with copyright text in `{typography.caption-sm}`. The bilingual English/French structure and dealer-locator links reflect Danby's Canadian market identity.

### Pagination

**`pagination`** — Row of 36px square items with `{rounded.xs}` corners. The active page fills with `{colors.primary-light}` and white text. Inactive pages show `{colors.body}` text with a hairline border. Used on catalog listing pages where product counts regularly exceed 20 per category.

### Breadcrumb

**`breadcrumb`** — Horizontal chain using `{typography.body-sm}` with "/" separators in `{colors.muted-soft}`. Current page renders in `{colors.ink}`, ancestor links in `{colors.muted}` with underline on hover. Critical for deep appliance-catalog navigation (Home / Dishwashers / Countertop / Model DDW1805...).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu with full-screen navy overlay; hero banner stacks image below text; filter sidebar becomes a slide-out drawer; comparison table horizontally scrollable; search bar expands full-width below nav; footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories, mega-menu triggers on tap; hero banner uses 60/40 text-image split; filter sidebar overlays as a modal panel; spec table remains full-width; footer collapses to two columns |
| Desktop | 1128–1440px | Three- to four-column product grid; full mega-menu navigation; hero banner at full 420px height with side-by-side layout; filter sidebar visible as persistent left column at 260px; comparison table fits up to four products side by side |
| Wide | > 1440px | Content max-width caps at 1440px and centers; additional horizontal padding at `{spacing.section-lg}`; product grid holds four columns with larger card images; hero banner images scale up proportionally |

### Touch Targets
- All interactive elements maintain a minimum 44px touch target on mobile and tablet
- Checkbox hit area extends to include the label text, not just the 16px box
- Navigation hamburger icon has a 48px tap zone
- Filter accordion headers are full-width tap targets at 48px height
- Pagination items maintain 44px spacing even when visually 36px

### Collapsing Strategy
- Navigation: two-tier header collapses to a single 56px bar with hamburger; utility links move inside the slide-out menu
- Product grid: four → two → one columns as breakpoints narrow; card padding reduces from `{spacing.base}` to `{spacing.sm}` on mobile
- Spec table: stays single-column with full width; long values wrap rather than truncate
- Comparison table: fixed first column (product name) with horizontal scroll for remaining columns on mobile
- Footer: four → two → one column stacking; language toggle moves to top of footer on mobile
- Hero banner: side-by-side becomes stacked; minimum height drops to 280px on mobile; CTA button becomes full-width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Many extracted colors (#337ab7, #5cb85c, #5bc0de, #3c763d, #8a6d3b, #a94442, #286090) are Bootstrap 3 framework defaults — they may be intentional brand choices or unthemed framework residue; manual verification against live components is recommended
- Poppins is the only distinctive brand font extracted; actual font weights loaded (300/400/500/600/700) could not be confirmed from static extraction — weight assignments are inferred from visual hierarchy patterns
- No CSS custom properties or design tokens were detected; the site appears to use compiled Bootstrap with overrides rather than a tokenized system
- Exact border-radius values could not be confirmed — 4px and 8px are inferred from the Bootstrap base and common overrides; the site may use 0px (fully sharp) corners on some components
- Icon system uses Font Awesome 5 (both Free and Brands variants) plus Glyphicons Halflings and WooCommerce glyphs; icon sizing and color tokens were not extractable
- WooCommerce is the underlying e-commerce platform; cart, checkout, and account page component styles are likely WooCommerce defaults with minimal brand customization
- No meta theme-color was set; mobile browser chrome color is uncontrolled
- Exact hero banner heights, product-card image ratios, and nav-bar heights are estimated from standard appliance-site patterns rather than measured from the live DOM
- Bilingual (EN/FR) content strategy was inferred from the Canadian market positioning but specific language-toggle UI patterns were not extracted
- No dark-mode tokens or prefers-color-scheme media queries were detected
