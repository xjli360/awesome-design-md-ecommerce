---
version: alpha
name: "OnlineLabels.com"
source_url: "https://www.onlinelabels.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every product tile on OnlineLabels.com renders a miniature of the physical label sheet — white stock with dotted perforation lines and a dimension callout printed in the margin — treating the substrate itself as the hero image rather than lifestyle photography. This catalog-born logic runs through the entire interface: a dense left-panel filter hierarchy organized by shape, size, material, printer type, and finish sits beside a tight product grid, all anchored by a search bar calibrated to SKU-level specificity (OL123, 4" × 2" Glossy, Round Kraft). The one reliably extracted color is #313131, a near-black charcoal that functions as the universal ink register — heading text, filter labels, SKU identifiers, and checkbox borders all run through this single dark tone. A utility blue (inferred from brand knowledge; not confirmed by live extraction due to Cloudflare anti-bot interception) handles primary CTAs: "Add to Cart," the Maestro Label Designer launch button, and active navigation highlights. Typography falls entirely on the operating system native sans-serif stack — no custom typeface, no brand font files — consistent with a site that has served commercial label buyers since the early web and treats reliable page load over font licensing as a design constraint. Label dimensions display in mixed units (inch-primary, millimeter-secondary in parentheses), signaling a dual audience of consumer buyers and B2B print-shop operators. The Maestro Label Designer — the brand's in-browser design-to-print tool — is the primary differentiator over plain warehouse fulfillment, surfaced as a persistent CTA on every product page. Rounded corners are minimal and functional — small `{rounded.sm}` radii on buttons and cards, never pill-shaped — keeping the interface in catalog territory rather than soft-consumer DTC. The overall density reads closer to a parts database than a lifestyle store: filter counts appear in parentheses beside each facet option, bulk-pricing tiers are shown inline on product cards, and printer-compatibility matrices appear as icon-row indicators rather than prose copy.

colors:
  primary: "#1c6fb5"
  primary-active: "#155a96"
  primary-disabled: "#a8cce8"
  ink: "#313131"
  body: "#444444"
  muted: "#767676"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-filter: "#f9f9f9"
  on-primary: "#ffffff"
  success: "#2e8b4a"
  warning: "#d97706"
  error: "#c0392b"
  sale-accent: "#d94f2b"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  sku-label:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.4px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  filter-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  dimension-callout:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 10px
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
    padding: 10px 20px
    height: 40px
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 38px
    typography: "{typography.body-md}"
    focusBorder: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-utility:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    height: 32px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px
  product-card-sheet-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
  product-card-sku:
    typography: "{typography.sku-label}"
    textColor: "{colors.muted}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    height: 42px
    typography: "{typography.body-md}"
    iconColor: "{colors.muted}"
    focusBorder: "1px solid {colors.primary}"
  search-submit-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 42px
    width: 42px
  filter-panel:
    backgroundColor: "{colors.surface-filter}"
    textColor: "{colors.ink}"
    typography: "{typography.filter-label}"
    borderRight: "1px solid {colors.hairline}"
    width: 220px
    padding: 16px
  filter-section-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    paddingBottom: 8px
    borderBottom: "1px solid {colors.hairline-soft}"
  filter-checkbox-row:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    accentColor: "{colors.primary}"
  filter-count-badge:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  dimension-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.dimension-callout}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  compatibility-icon-row:
    backgroundColor: "{colors.surface-soft}"
    iconColor: "{colors.muted}"
    activeIconColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: 32px 64px
    borderBottom: "1px solid {colors.hairline}"
  maestro-cta-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: 32px
    rounded: "{rounded.md}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    hoverBorder: "1px solid {colors.primary}"
    padding: 16px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  bulk-pricing-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    height: 38px
    typography: "{typography.body-md}"
  template-gallery-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    hoverShadow: "0 2px 8px rgba(0,0,0,0.10)"
    padding: 8px
  pagination:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.primary}"
    borderTop: "1px solid {colors.hairline}"
    padding: 48px 64px

## Components

### Buttons

**`button-primary`** — Solid `{colors.primary}` blue with `{colors.on-primary}` white text, `{rounded.sm}` corners, 40px tall, and `{typography.button-md}` weight-600 labeling. Appears on product pages as "Add to Cart," throughout the Maestro design tool flow as "Design & Print" or "Use Template," and as the search bar submit element. Active state flattens to `{colors.primary-active}` (#155a96); disabled bleaches to `{colors.primary-disabled}`. No drop shadow, no animation — state changes are flat color swaps suited to a catalog UI.

**`button-secondary`** — White fill with a 1px `{colors.primary}` border and primary-blue text, same height and `{rounded.sm}` radius as primary. Used for secondary actions such as "Download Template," "View Specs," and "Save to My Labels." The 1px inset padding prevents layout shift against primary siblings in button pairs.

**`button-ghost`** — Transparent background, primary-blue text, no border, `{typography.button-sm}`. Used for low-prominence inline actions: "See all sizes," "Clear filters," "Show more," and pagination Previous/Next controls.

### Navigation

**`nav-bar`** — 56px tall white header with a 1px `{colors.hairline}` bottom border. Left: brand logo. Center: `search-bar` spanning roughly 40% of the header width. Right: account link, order tracker, and cart icon with item count badge. Above the main bar, `nav-bar-utility` runs at 32px on `{colors.surface-soft}` gray, carrying a phone number, live-chat link, and a free-shipping threshold notice in `{typography.caption}` muted gray — the only place contact information appears in the shell.

### Search

**`search-bar`** — 42px tall input with a 1px `{colors.hairline}` border and `{rounded.sm}` radius, flush against a `search-submit-button` on its right edge. The submit button is a 42×42px solid `{colors.primary}` square with a white magnifier icon — the only full-bleed primary color element in the nav shell. Focus promotes the input border to a 1px `{colors.primary}` outline. Placeholder text reads "Search by size, shape, part number…" in `{colors.muted}`.

### Product Card

**`product-card`** — White card with a 1px `{colors.hairline}` border and `{rounded.sm}` corners. Top area: `product-card-sheet-image`, a rendered thumbnail of the physical label sheet on a `{colors.surface-soft}` background. Below: the SKU in `{typography.sku-label}` (monospace, `{colors.muted}`), then product name in `{typography.title-sm}`, then price in `{typography.price-display}`. A `compatibility-icon-row` sits below the price showing printer-type icons (laser / inkjet / thermal) at small scale with `{typography.caption}` labels, and a `dimension-badge` shows the label's primary measurement inline.

### Filter Panel

**`filter-panel`** — Fixed 220px left sidebar on `{colors.surface-filter}` with a 1px `{colors.hairline}` right border. Filter sections are divided by `{colors.hairline-soft}` horizontal rules. Each section opens with a `{typography.title-sm}` heading, then a list of `filter-checkbox-row` items: `{colors.primary}` accent checkboxes, `{typography.body-sm}` option labels, and `filter-count-badge` item counts in parentheses in `{colors.muted}`. The canonical filter hierarchy is: Shape → Size → Material → Finish → Printer Type → Color → Brand.

### Dimension Badge

**`dimension-badge`** — A compact inline tag on `{colors.surface-soft}` with a 1px `{colors.hairline}` border and `{rounded.xs}` corners. Renders in `{typography.dimension-callout}` (11px, 0.3px letter-spacing): "4" × 2" (101.6 × 50.8 mm)." Appears in product titles, size selectors, and within the filter panel facets. The mixed-unit format is a deliberate signal to the B2B buyer segment.

### Maestro CTA Banner

**`maestro-cta-banner`** — A full-width `{colors.primary}` blue block promoting the Maestro Label Designer, with `{colors.on-primary}` white heading in `{typography.display-md}` and body copy in `{typography.body-md}`. The inline CTA button inverts to a white-fill / primary-blue-border secondary button style — the only context where a secondary button appears on a colored background. Placed as a section break between the product grid and footer on category browse pages.

### Bulk Pricing Table

**`bulk-pricing-table`** — An inline table on `{colors.surface-soft}` with a 1px `{colors.hairline}` border and `{rounded.sm}` corners, showing quantity break tiers (e.g., 1–9 sheets: $X.XX / sheet; 10–49: $X.XX; 50+: $X.XX). Header row uses `{typography.title-sm}`; body rows use `{typography.body-sm}`. Displayed directly on product pages below the `quantity-selector`, not in a modal, because pricing transparency at point-of-decision is central to the B2B purchasing flow.

### Template Gallery Card

**`template-gallery-card`** — White card with `{rounded.sm}` border and an 8px internal pad. Shows a filled-label thumbnail preview, a category tag in `{typography.caption}`, and a "Use This Template" `button-secondary` that surfaces on hover. On mobile, the hover button is replaced with an always-visible smaller CTA below the thumbnail. Used in the template library and inside the Maestro designer's browse panel.

### Category Tile

**`category-tile`** — Square or near-square tiles on `{colors.surface-soft}` with a `{colors.hairline}` border that promotes to `{colors.primary}` on hover. A line-art icon of the label shape (circle, rectangle, oval, roll) sits centered at top; a short title in `{typography.title-sm}` sits below. Used on the homepage category grid and in the "Shop by Shape" navigation dropdown.

### Footer

**`footer`** — `{colors.surface-soft}` background with a 1px `{colors.hairline}` top border. Four-column link grid in `{typography.body-sm}` with `{colors.primary}` anchor color. Bottom strip carries copyright, BBB accreditation badge, SSL seal, and payment method icons, with a `{typography.caption}` muted disclaimer. Link categories: Products, Resources, Account, Company.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Filter panel collapses to a bottom-sheet drawer opened by a sticky "Filters (N)" button showing active filter count; nav search becomes full-width below logo row; product grid is 2-column; bulk pricing table scrolls horizontally; dimension badges show inch-only (no mm suffix) |
| Tablet | 744–1128px | Filter panel becomes a collapsible left sidebar with a toggle button; product grid is 3-column; Maestro CTA banner reduces horizontal padding; utility nav bar collapses to a single link row |
| Desktop | 1128–1440px | Full 220px filter panel visible; 4-column product grid; nav bar shows all primary nav links with dropdowns; Maestro CTA banner renders in side-by-side text + CTA layout |
| Wide | > 1440px | Content max-width capped at 1400px centered; filter panel stays 220px fixed; product grid expands to 5 columns; hero banner gains increased horizontal breathing room |

### Touch Targets
- All filter checkboxes minimum 44×44px tap area regardless of visual checkbox size
- "Add to Cart," "Design & Print," and "Use Template" buttons minimum 44px height on mobile
- Pagination controls minimum 44px tap target with generous surrounding padding
- Quantity selector increment/decrement buttons minimum 40×40px each
- Category tiles minimum 80px height in mobile grid
- Search submit button remains 44×44px on mobile even when input collapses

### Collapsing Strategy
- Filter panel converts to a bottom-sheet modal on < 744px; active filter count shown on the trigger button
- Utility top bar (phone, chat, shipping notice) hidden below tablet breakpoint; phone/chat moves to footer
- Dimension badges truncate to inch-only format below 375px viewport width
- Bulk pricing table collapses from a horizontal tier row to a vertical stacked list on mobile
- Template gallery card "Use This Template" hover button becomes an always-visible below-thumbnail CTA on touch devices
- Breadcrumb truncates to the last two segments with a leading ellipsis on mobile
- Compatibility icon row labels hidden below 375px; icons only with tooltip on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Nearly all hex colors unextracted** — the site returned a Cloudflare challenge page ("Just a moment...") during live crawl; only #313131 was captured. All other palette values — primary blue, surface grays, accent colors, error/success/sale states — are inferred from brand knowledge and label e-commerce conventions, not live extraction.
- **Primary blue hex not confirmed** — `#1c6fb5` is an approximation based on known OnlineLabels.com branding patterns; the exact production value may differ. Verify against the live stylesheet or design source before production use.
- **No custom brand font detected** — the entire font stack is system UI. It is unclear whether a custom webfont is injected via JavaScript after initial HTML response; no `@font-face` declarations or font files were captured.
- **Meta theme-color absent** — no `theme-color` meta tag was found; the brand has no declared mobile chrome bar color.
- **Icon system unknown** — the brand likely uses a custom SVG set or a common library (Font Awesome, Material Icons) for printer-compatibility and shape icons; no icon font or sprite was extractable.
- **Maestro designer sub-system** — the in-browser label design tool may carry its own distinct UI language (toolbars, color pickers, panel chrome) that diverges from the marketing shell; no extraction was possible for this surface.
- **Dark mode** — no dark-mode variants were detected; assume light-only unless confirmed by a design audit.
- **Promotional and sale color** — a warm accent (orange or red) is commonly used in this category for sale-price callouts and promotional badges; `{colors.sale-accent}` (#d94f2b) is a reasonable guess but not confirmed.
- **Navigation dropdown structure** — the depth and content of mega-menu dropdowns (if any) could not be mapped from the intercepted page response.
