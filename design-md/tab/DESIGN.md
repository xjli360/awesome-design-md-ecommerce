---
version: alpha
name: "TAB"
source_url: "https://tab.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every color in TAB's palette earns its position by function — the institutional blue (#1863dc) marks every navigable action while alert red (#dc001b) carries decades of physical filing urgency into the UI, and everything else recedes into a graded sequence of near-whites and neutrals that let the catalog breathe. Deep navy (#293c5b) layers across nav bars and section anchors; near-black (#212121) handles primary reading text; medium gray (#858585) labels secondary metadata; and three stepped surface tones — #f4f4f4, #ededed, #ebebeb — establish visual depth without introducing warmth. Red (#dc001b) appears at two deliberate moments: on primary call-to-action buttons where urgency is appropriate to a purchasing workflow, and at alert and error states — a direct inheritance from the physical filing system vocabulary where the red tab means "act on this." The site returns `inherit` for all font stacks, which in a B2B enterprise context reads as intentional rather than incomplete: system fonts render predictably across managed Windows workstations, legacy enterprise browsers, and corporate endpoint configurations, accepting Segoe UI on Windows and Helvetica on Mac without complaint rather than imposing a branded typeface that may not be licensed for deployment environments. Corner radii are nearly absent — `{rounded.xs}` at 4px appears on buttons and inputs while the majority of containers are squared to match the visual grammar of a filing system, where the right angle governs folder edges, drawer labels, and row dividers; only pill badges at `{rounded.full}` use curves, and they signal interactivity rather than brand warmth. Spacing is generous in the data zone and compressed in navigation: product listings and form sections use `{spacing.base}` to `{spacing.lg}` internal padding while nav links stack tightly at `{spacing.sm}` gaps. The product card reads as a data row first — SKU, category, and spec labels competing equally with product imagery — and a visual object second. The overall system is calibrated for procurement professionals navigating hundreds of SKUs across multiple sessions, not for impulse conversion.

colors:
  primary: "#1863dc"
  primary-dark: "#003388"
  primary-active: "#0056a7"
  primary-disabled: "#d9dfe7"
  alert: "#dc001b"
  alert-active: "#b50014"
  success: "#008000"
  navy: "#293c5b"
  ink: "#212121"
  body: "#313131"
  muted: "#858585"
  muted-soft: "#cbced6"
  hairline: "#dedfe0"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#f1f5fa"
  surface-mid: "#ededed"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  table-header:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-alert:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-alert-active:
    backgroundColor: "{colors.alert-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: 9px 19px
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    focusBorderColor: "{colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-top-utility:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 32px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    skuColor: "{colors.muted}"
    skuTypography: "{typography.caption}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    borderBottom: "2px solid {colors.primary}"
  category-tab-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    borderBottom: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    height: 40px
    padding: 8px 12px
    iconColor: "{colors.muted}"
  status-badge:
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  status-badge-available:
    backgroundColor: "#e6f4e6"
    textColor: "{colors.success}"
  status-badge-low-stock:
    backgroundColor: "#fff3cd"
    textColor: "#856404"
  status-badge-unavailable:
    backgroundColor: "#fde8ea"
    textColor: "{colors.alert}"
  data-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.table-header}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "2px solid {colors.hairline}"
  data-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
    hoverBackground: "{colors.surface-soft}"
  section-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.navy}"
    typography: "{typography.display-sm}"
    padding: "{spacing.lg} 0"
    borderBottom: "3px solid {colors.primary}"
  hero:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    ctaBackground: "{colors.alert}"
    ctaTextColor: "{colors.on-primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.body}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "#d9dfe7"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The default action button carries TAB's institutional blue (#1863dc) with white text at `{rounded.xs}` corners. Hover deepens to `{colors.primary-active}` (#0056a7); disabled state uses `{colors.primary-disabled}` with `{colors.muted}` text, maintaining the color family without implying interactivity.

**`button-alert`** — Red (#dc001b) is not reserved for errors alone — it appears on primary CTAs for actions that carry urgency in a procurement workflow: "Request Quote," "Contact Sales," "Order Now." This borrows the physical filing vocabulary where the red tab means "act on this immediately." Active state deepens to `{colors.alert-active}`.

**`button-secondary`** — White background with a 1px `{colors.primary}` border and matching text, same `{rounded.xs}` corner radius as primary. Used where a secondary option sits alongside a primary action on the same surface.

**`button-ghost`** — Transparent with a `{colors.hairline}` border. Reserved for utility actions (download PDF, export, filter reset) that should not compete with primary or alert CTAs in the visual hierarchy.

### Text Input

**`text-input`** — A 40px input with `{rounded.xs}` corners and a 1px `{colors.hairline}` border that changes to `{colors.primary}` on focus. Placeholder text renders at `{colors.muted}`. No box shadow on focus — the border-color change alone signals the active state, consistent with the minimal-decoration approach across the system.

### Navigation

**`nav-bar-top-utility`** — A 32px strip in `{colors.ink}` sits above the main nav, carrying account links, phone numbers, and regional selectors in `{typography.caption}` white text. This utility tier serves the multiple user types of a B2B platform — sales reps, IT admins, warehouse managers — each needing different entry points.

**`nav-bar`** — The main 56px bar in deep navy `{colors.navy}` carries primary product category links in `{typography.nav-link}` white text. The two-tier structure — black utility strip above navy nav — uses contrast of darkness rather than color variety to signal hierarchy.

### Category Tabs

**`category-tab-active`** / **`category-tab-inactive`** — A flush tab strip with no border radius. Active tabs fill with `{colors.primary}` and white `{typography.button-sm}` text. Inactive tabs sit on `{colors.canvas}` with `{colors.body}` text and a `{colors.hairline}` bottom border. No rounded corners — the tab strip reads as a drawer handle, not a pill filter.

### Product Card

**`product-card`** — A 1px `{colors.hairline}` bordered tile at `{rounded.xs}` with `{spacing.base}` internal padding. Part number and SKU appear above the product title in `{typography.caption}` at `{colors.muted}` — catalog-first presentation where the identifier is as important as the name. Title in `{typography.title-sm}`, price in `{typography.title-md}`. Image occupies a 4:3 aspect ratio region without decorative chrome.

### Search Bar

**`search-bar`** — A 40px `{rounded.xs}` input with a magnifier icon in `{colors.muted}` and a `{colors.hairline}` border. Positioned either within the nav tier or as a full-width element atop category pages. No pill treatment — the search bar is a tool, not a brand moment.

### Status Badges

**`status-badge`** — Pill shape at `{rounded.full}` with `{typography.label}` uppercase text. Three inventory-state variants: available (light green background / `{colors.success}` text), low stock (amber fill / dark amber text), unavailable (light red fill / `{colors.alert}` text). These map directly to warehouse inventory vocabulary and scan instantly in a 200-row catalog table.

### Data Table

**`data-table-header`** — `{colors.surface-soft}` background with `{typography.table-header}` uppercase column labels and a 2px `{colors.hairline}` bottom border separating head from body. **`data-table-row`** — 1px `{colors.hairline-soft}` row separator; hover transitions the row to `{colors.surface-soft}`, providing enough feedback for keyboard-navigable tables without animated effects.

### Hero

**`hero`** — A full-width `{colors.navy}` band at minimum 480px height. Headline in `{typography.display-xl}` white; body copy in `{typography.body-md}` white. The CTA uses `{colors.alert}` (red) against the dark navy, placing maximum contrast behind the primary conversion action. Padding is `{spacing.section}` vertical with `{spacing.xl}` horizontal inset.

### Section Header

**`section-header`** — A `{colors.surface-soft}` background band with a `{colors.navy}` headline in `{typography.display-sm}` and a 3px `{colors.primary}` bottom border that anchors the section to the brand blue without painting the full background. Separates product catalog tiers and landing page content zones.

### Breadcrumb

**`breadcrumb`** — `{typography.caption}` ancestor links in `{colors.muted}`, current page label in `{colors.body}`. Separator uses `{colors.muted-soft}`. No background, no border, flush left in the page container — a navigational utility element rather than a brand component.

### Footer

**`footer`** — `{colors.ink}` (#212121) background closes the page at the same black level as the top utility strip, framing the content between two dark horizontal bands. Column headers in `{typography.title-sm}` weight, link text in `{typography.caption}`. Link color uses `#d9dfe7` (light blue-gray) rather than pure white to reduce halation on dark backgrounds. `{spacing.xxl}` vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; both nav tiers collapse to hamburger drawer; hero min-height drops to 280px; data tables scroll horizontally with sticky first column; search bar expands to full width; category tab strip scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; main nav bar stays visible, utility strip collapses; category tabs scroll if overflow; hero min-height 360px |
| Desktop | 1128–1440px | Three-column product grid; full two-tier nav visible; category tab strip fully rendered; data tables show all columns |
| Wide | > 1440px | Content container capped at ~1400px centered; four-column product grid; nav and hero content constrained to container width while backgrounds extend edge-to-edge |

### Touch Targets

- All interactive controls minimum 40px height; primary and alert buttons 44px on mobile viewports
- Category tab strip rows 44px touch height on mobile regardless of label height
- Hamburger drawer nav links use 48px row height for comfortable thumb navigation
- Form inputs rendered at 44px height on mobile to prevent iOS automatic zoom-on-focus behavior

### Collapsing Strategy

- Top utility nav strip (32px black bar) collapses entirely below 744px; its links migrate into the hamburger drawer as a secondary section
- Main nav collapses to hamburger icon at < 744px; category megamenu panels become accordion drawers within the slide-over
- Product grid: 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- Data tables below 744px: horizontal scroll with the SKU/product-name column sticky at left
- Footer: 4-column layout → 2 columns at tablet → single stacked column at mobile with 40px section separators

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font families detected — all font stacks return `inherit`; system font assumptions used throughout. Actual deployed typeface may differ if loaded via JavaScript or a third-party CDN not captured in extraction.
- Multiple blues in the extracted palette (#4285f4, #0693e3, #007cba, #006ba1, #005a87) appear to be WordPress Gutenberg editor defaults rather than brand tokens; brand-specific blues identified as #1863dc, #003388, and #293c5b based on distinctiveness and position order.
- Hover and focus state colors inferred by darkening extracted primaries a consistent step; not confirmed from live DOM inspection.
- Exact button and input border-radius not confirmed from extraction; `{rounded.xs}` (4px) assumed from the angular character appropriate to a filing-system brand.
- No modal, overlay, or drawer component patterns captured; scrim and overlay tokens not defined.
- Promotional display patterns (MSRP strikethrough, sale badges, volume pricing tiers) not confirmed from extraction.
- No icon set or illustration style observed; icon references in search-bar and nav components assume a standard outline glyph library.
- Green (#008000) and teal (#34e2e4) tokens present in extraction but usage context unknown; #008000 conservatively assigned to success/availability states only.
- No form validation pattern (inline error messaging, field-level error states) confirmed from extraction.
