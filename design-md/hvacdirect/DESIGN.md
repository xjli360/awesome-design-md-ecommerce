---
version: alpha
name: "HVACDirect"
source_url: "https://www.hvacdirect.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Contractor catalogs rarely bother with softness — and HVACDirect's single extractable brand anchor, a flat charcoal (#313131), confirms that the interface is engineered for specification, not aspiration. The brand cuts distributor margins by selling HVAC equipment directly to contractors and homeowners, and the design follows the same operating logic: no lifestyle photography of wind and comfort, no editorial warmth — just part numbers, efficiency ratings, and a purchase path that should be navigable from a phone with dirty gloves on. The #313131 charcoal functions as both the dominant surface tone and the typographic ink, signaling the same industrial seriousness found in supply-house print catalogs, where black-on-white legibility outranks brand personality at every scale.

  Typography runs entirely on system fonts — Arial, Roboto, and the -apple-system stack — with no proprietary typeface detected. This is a deliberate economy: system fonts load instantly on contractor tablets and job-site laptops, and the Arial/Roboto pairing carries dense specification data at the small sizes that HVAC equipment tables demand (tonnage, SEER, AFUE, BTU, refrigerant type all competing for column width). Button labels and table headers sit at 13–14px in a medium or semi-bold weight, matching the convention of industrial supply catalogs where information density outranks typographic hierarchy.

  Because the extraction yielded only a single color — the site sits behind Cloudflare anti-bot protection — the remainder of the palette is constructed from industrial e-commerce convention. A near-white canvas holds product grids; light gray surfaces separate spec table rows; a utility blue CTA accent (#1a6dcc, inferred) delivers the primary Add-to-Cart and Quote-Request actions in a register that reads as technical authority without veering into consumer warmth. Product cards sit at the center of gravity: each holds a thumbnail, model number, key performance specs, price, and Add-to-Cart — sized for fast procurement decisions by buyers who already know what they need. The rounded system stays at {rounded.xs} for buttons and inputs, {rounded.none} for table cells and sidebar panels, because hard edges read as precision in industrial contexts. A persistent search bar with category filters and the deep catalog navigation tree in the footer both carry the load of a technical catalog that must be browsable by trade professionals across hundreds of SKUs.

colors:
  primary: "#313131"
  primary-active: "#1c1c1c"
  primary-disabled: "#a0a0a0"
  cta: "#1a6dcc"
  cta-active: "#155bb0"
  cta-disabled: "#a0bfe8"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#767676"
  hairline: "#d4d4d4"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-mid: "#eeeeee"
  on-primary: "#ffffff"
  on-cta: "#ffffff"
  success: "#2d7a3a"
  success-soft: "#e8f5eb"
  error: "#c0392b"
  error-soft: "#fdecea"
  warning: "#e07b00"
  warning-soft: "#fff4e0"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-xs:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  price-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.2px

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
    backgroundColor: "{colors.cta}"
    textColor: "{colors.on-cta}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 42px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.cta-active}"
    textColor: "{colors.on-cta}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.cta-disabled}"
    textColor: "{colors.on-cta}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.cta}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 42px
    border: "1px solid {colors.cta}"
  button-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 42px
    border: none
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.cta}"
    placeholderColor: "{colors.muted}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 10px
    height: 36px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    paddingHorizontal: "{spacing.lg}"
    borderBottom: none
  nav-bar-utility:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 32px
    paddingHorizontal: "{spacing.lg}"
  nav-mega-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.cta}"
    padding: "{spacing.lg}"
    shadow: "0 4px 12px rgba(0,0,0,0.12)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 40px
    border: "2px solid {colors.hairline}"
    borderFocus: "2px solid {colors.cta}"
    placeholderColor: "{colors.muted}"
  search-button:
    backgroundColor: "{colors.cta}"
    textColor: "{colors.on-cta}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 40px
    padding: 0 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    shadow: "0 1px 3px rgba(0,0,0,0.08)"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    captionTypography: "{typography.body-sm}"
  product-card-hover:
    border: "1px solid {colors.cta}"
    shadow: "0 3px 10px rgba(26,109,204,0.12)"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 320px
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.section}"
  category-hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    borderBottom: "1px solid {colors.hairline}"
    paddingVertical: "{spacing.xl}"
    paddingHorizontal: "{spacing.lg}"
  category-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
    width: 220px
    paddingVertical: "{spacing.sm}"
  sidebar-heading:
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    paddingVertical: "{spacing.sm}"
    paddingHorizontal: "{spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  sidebar-item-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.cta}"
    typography: "{typography.body-sm}"
    paddingVertical: "{spacing.xs}"
    paddingHorizontal: "{spacing.base}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    headerTextColor: "{colors.muted}"
    rowBorder: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.none}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    paddingVertical: "{spacing.sm}"
  badge-efficiency:
    backgroundColor: "{colors.success-soft}"
    textColor: "{colors.success}"
    typography: "{typography.label-xs}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-promo:
    backgroundColor: "{colors.cta}"
    textColor: "{colors.on-cta}"
    typography: "{typography.label-xs}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-clearance:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-xs}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-instock:
    backgroundColor: "{colors.success-soft}"
    textColor: "{colors.success}"
    typography: "{typography.label-xs}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  price-block:
    primaryColor: "{colors.ink}"
    primaryTypography: "{typography.price-display}"
    strikeColor: "{colors.muted}"
    strikeTypography: "{typography.body-sm}"
    savingsColor: "{colors.error}"
    savingsTypography: "{typography.caption}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    activeBackgroundColor: "{colors.cta}"
    activeTextColor: "{colors.on-cta}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 36px
    minWidth: 36px
  alert-success:
    backgroundColor: "{colors.success-soft}"
    textColor: "{colors.success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.success}"
    padding: "{spacing.sm} {spacing.base}"
  alert-error:
    backgroundColor: "{colors.error-soft}"
    textColor: "{colors.error}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.error}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.surface-mid}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-primary}"
    borderTop: "3px solid {colors.cta}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.lg}"
  footer-bottom-bar:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    height: 44px
    paddingHorizontal: "{spacing.lg}"

## Components

### Buttons

**`button-primary`** — The main Add-to-Cart and Quote-Request action rendered in the inferred utility blue (#1a6dcc) with white text, 42px height, and {rounded.xs} corners. Hover state deepens to {colors.cta-active}; disabled state uses {colors.cta-disabled} and removes pointer events. The 600-weight Arial label at 15px holds legibility at small sizes on mobile product grids.

**`button-secondary`** — An outlined variant in white canvas with a 1px {colors.cta} border and matching text, used for secondary procurement actions like "Add to Quote" or "View Details." The border provides strong contrast against {colors.surface-soft} category backgrounds.

**`button-dark`** — Full {colors.primary} background (#313131) with white text, used for editorial CTAs on hero banners and dark-surface sections such as promotional callouts. Shares the same {rounded.xs} and height contract as `button-primary`.

**`button-ghost`** — A lightweight outlined button in {colors.hairline} border with {colors.ink} text, used for secondary filter actions, pagination, and inline form controls that should not compete with Add-to-Cart calls.

### Inputs

**`text-input`** — 40px height, 1px {colors.hairline} border, {rounded.xs}, with focus upgrading to a {colors.cta} border. Placeholder in {colors.muted}. Standard width fills the parent column in quote forms and account flows.

**`search-bar`** — A 40px input with a 2px border flush-left and a `search-button` component flush-right in {colors.cta} blue, forming a compound control. The zero-radius join between input and button (right side `{rounded.none}`) reinforces the catalog-search paradigm over consumer search aesthetics.

**`select-input`** — 36px dropdown for filter controls in the category sidebar (brand, efficiency rating, tonnage range). Shares {rounded.xs} and {colors.hairline} border with `text-input`, sized slightly smaller to fit filter sidebar columns.

### Navigation

**`nav-bar`** — 56px charcoal (#313131) primary bar carrying logo, global search compound, cart, and account controls in white. A `nav-bar-utility` strip (32px, deeper {colors.primary-active}) sits above it for phone, account links, and promotions. `nav-mega-panel` drops from top-level category items with a {colors.cta} 3px top border to anchor the panel visually.

**`breadcrumb`** — 12px Arial in {colors.muted} with `>` separators, current page in {colors.ink}. Appears on all category and product detail pages, essential for catalog depth navigation.

**`category-sidebar`** — 220px fixed panel with heading rows in {typography.title-sm} and items at {typography.body-sm}. Active items highlight background in {colors.surface-soft} and text in {colors.cta}. Borders only on the right edge ({colors.hairline}) — no card shadow — consistent with a utility data interface.

### Product Cards

**`product-card`** — White surface, 1px {colors.hairline} border, {rounded.xs}, 8px shadow. Contains product thumbnail, model number in {typography.title-sm}, a 2–3 line spec summary in {typography.body-sm}, and `price-block` + `button-primary` stacked at the bottom. Hover state upgrades border to {colors.cta} and subtly lifts shadow. Cards tile in a 4-column grid on desktop narrowing to 2 on tablet and 1 on mobile.

**`price-block`** — 22px 700-weight price in {colors.ink}, struck-through MSRP in {typography.body-sm} {colors.muted} above, savings label in {colors.error} caption below. The three-line structure is a standard industrial supply convention signaling transparency on margin.

### Badges

**`badge-efficiency`** — Light green surface / dark green text, uppercase 11px label for energy certifications (ENERGY STAR, High-Efficiency). `badge-promo` uses {colors.cta} blue for sale or new-arrival flags. `badge-clearance` uses {colors.error} red for end-of-line stock. `badge-instock` uses pill {rounded.full} in success-soft for inventory status inline with product title.

### Spec Table

**`spec-table`** — Full-width table on product detail pages, zero-radius corners, {colors.surface-soft} header row with {typography.spec-label} uppercase column headers in {colors.muted}. Row borders in {colors.hairline-soft} only (no column lines), alternating row backgrounds optional. The density pattern matches Grainger and Fastenal specification tables.

### Hero & Category Banners

**`hero-banner`** — Full-width {colors.primary} (#313131) background, white headline at {typography.display-xl}, body in {typography.body-md}, 320px minimum height. Carries seasonal promotions and brand campaigns. A `category-hero` variant uses {colors.surface-soft} white-gray for internal category landing pages with a {typography.display-md} heading and {colors.hairline} bottom border.

### Alerts

**`alert-success`** / **`alert-error`** — Soft-toned notification bars in the respective semantic colors with matching border. Appear at form-top for quote submission confirmations and add-to-cart errors. {rounded.xs}, 600px max-width on desktop.

### Footer

**`footer`** — Full-width {colors.primary} block with a {colors.cta} 3px top border accent, white headings, {colors.surface-mid} link color, 4-column navigation grid on desktop (Equipment, Brands, Resources, Account). `footer-bottom-bar` in {colors.primary-active} holds legal copy, policy links, and copyright in {colors.muted} caption text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; sidebar filters collapse into a drawer triggered by a "Filter" button; nav-bar consolidates to hamburger menu + search icon + cart; hero-banner reduces to 200px height with smaller headline; spec-table scrolls horizontally |
| Tablet | 744–1128px | 2-column product grid; sidebar filters remain visible but narrow to 180px; nav-bar shows abbreviated category links; price-block and Add-to-Cart stack vertically inside card |
| Desktop | 1128–1440px | 4-column product grid with 220px sidebar; full mega-nav; hero-banner at full 320px+; spec-table full-width with all columns visible |
| Wide | > 1440px | Max content width clamps to 1400px centered; product grid stays 4-column; lateral whitespace increases; footer grid expands to 5 columns |

### Touch Targets
- All buttons minimum 42px height, 120px minimum width on mobile
- Sidebar filter checkboxes minimum 44px tap area with extended padding
- Pagination controls minimum 44×44px each
- Nav hamburger icon minimum 44×44px hit area
- Add-to-Cart button full-width on mobile product cards

### Collapsing Strategy
- Category sidebar → off-canvas drawer with overlay scrim at < 744px
- Mega-nav panel → accordion list inside hamburger drawer on mobile
- Spec table → horizontal scroll container, first column sticky (model attribute label)
- Breadcrumb → truncated to last 2 nodes on mobile with ellipsis
- Footer navigation columns → 2-column stacked grid on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color extracted (#313131): the site is behind Cloudflare anti-bot protection ("Just a moment..." page title), blocking full CSS/JS token extraction. All colors other than #313131 are inferred from industrial e-commerce convention and are unverified.
- CTA accent color (#1a6dcc, utility blue) is an inference — actual brand accent may be orange, red, green, or a different blue; must be verified against the live site.
- No custom font detected; all stacks are system fonts. A web font (e.g., custom sans-serif) may load via JS after bot-block clears — verify with DevTools on an authenticated session.
- Meta theme-color is absent, preventing any mobile chrome color confirmation.
- Logo treatment (wordmark vs. icon+text, color inversion on dark nav) not extractable.
- Exact border-radius values for cards and buttons not confirmed; {rounded.xs} (4px) is a conservative default for industrial suppliers.
- Promotional badge palette (sale, new, clearance) colors unverified.
- Whether HVACDirect uses a filter sidebar or top-filter-bar pattern on category pages could not be confirmed from extraction.
- Account, checkout, and quote-cart flow UI patterns entirely unextracted.
