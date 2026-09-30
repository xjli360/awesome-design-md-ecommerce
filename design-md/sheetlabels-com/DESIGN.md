---
version: alpha
name: "SheetLabels.com"
source_url: "https://www.sheetlabels.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The #0096ff anchoring SheetLabels.com is the rarest kind of primary color choice — one that earns its saturation. Full-voltage blue, not the softened cobalt most e-commerce platforms reach for when they want "trustworthy," but a signal-pure hue that reads as clickable before the eye finishes forming the thought. Against a white (#ffffff) canvas that matches the meta theme-color precisely, it functions as directional infrastructure: every CTA, nav item, link underline, and filter toggle runs in that same blue, making the interactive layer spatially legible even under the dense SKU grids a label buyer needs. The counterweight is #da532c, a warm orange-red deployed narrowly for urgency — promotional banners, sale price overrides, and inventory-low callouts — a color temperature that fires at a different frequency than the blue and never competes with it. SheetLabels.com sells to buyers who arrive with a spec in hand: sheet dimensions, material grade, perforation layout, die-cut shape. The catalog is built for specification-first navigation rather than lifestyle discovery — cards expose label dimensions, per-sheet counts, and material badges in the thumbnail zone; mega-menu navigation surfaces the full shape-and-substrate taxonomy before a search query is typed; configurator panels on detail pages lead with dimensions and quantity-break pricing tables rather than brand imagery. No custom typeface was recoverable from the extracted site data, suggesting either a system-ui rendering path or font assets behind bot-protection, so the design system defaults to a clean geometric sans-serif stack and relies on weight contrast — bold SKU codes and dimension strings, medium CTAs, regular descriptive copy — to establish hierarchy without a signature typeface. Corners run at modest radii (`{rounded.xs}` to `{rounded.sm}`) throughout: functional enough to soften the grid without veering toward the pill-and-blob vocabulary of consumer wellness brands. Spacing compresses to `{spacing.base}` gutters in product grids to maximize above-fold SKU density, the defining behavioral signal that this is a catalog built for efficiency over delight.

colors:
  primary: "#0096ff"
  primary-hover: "#007fd9"
  primary-active: "#0077cc"
  primary-disabled: "#99d0ff"
  accent: "#da532c"
  accent-active: "#b8431f"
  accent-disabled: "#f0b89f"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#6b7280"
  hairline: "#e5e7eb"
  hairline-soft: "#f3f4f6"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  nav-bg: "#0096ff"
  price-red: "#cc0000"
  success: "#16a34a"
  badge-material-bg: "#e8f4ff"
  badge-material-text: "#0077cc"
  footer-bg: "#1e3a5f"
  footer-link: "#9dc8f0"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  sku-code:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
  dimension-spec:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase

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
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-accent-hover:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 38px
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: "0 {spacing.lg}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.lg}"
    shadow: "0 4px 12px rgba(0,0,0,0.12)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 38px
    searchButtonBg: "{colors.primary}"
    searchButtonColor: "{colors.on-primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    dimensionTypography: "{typography.dimension-spec}"
    priceTypography: "{typography.price-display}"
    skuTypography: "{typography.sku-code}"
  badge-sale:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-material:
    backgroundColor: "{colors.badge-material-bg}"
    textColor: "{colors.badge-material-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.title-sm}"
    valueTypography: "{typography.body-md}"
    activeBorderColor: "{colors.primary}"
  quantity-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    buttonBg: "{colors.surface-soft}"
    buttonHoverBg: "{colors.primary}"
    buttonHoverColor: "{colors.on-primary}"
    height: 38px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaButtonBg: "{colors.accent}"
    ctaButtonColor: "{colors.on-accent}"
  promo-banner:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.body}"
    hoverBackgroundColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.footer-link}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The dominant action color across every page: a flat #0096ff rectangle at 40px height, 4px corners, semibold 15px label. "Add to Cart," "Get Pricing," "Shop Now," and filter-apply actions all use this variant. Hover shifts to `{colors.primary-hover}` (#007fd9); disabled washes to `{colors.primary-disabled}` without altering the radius. The absence of drop shadows or gradients matches the catalog's no-decoration ethos — the color alone carries the signal.

**`button-secondary`** — White fill with a 1px `{colors.primary}` border and matching text color, 40px height and identical 4px radius to button-primary. Used for secondary actions: "Save for Later," "Request Sample," filter reset, and compare functions. Hover lifts the background to `{colors.surface-soft}` while keeping the border and text unchanged.

**`button-accent`** — The #da532c orange-red variant reserved for promotional and urgency CTAs: "Shop Sale," "Flash Deal," and hero-zone offers. Shares the same height and radius as button-primary to preserve vertical rhythm. Hover deepens to `{colors.accent-active}` (#b8431f). Because this color appears nowhere else in the UI chrome, its appearance reads immediately as an alert or opportunity rather than navigation.

### Navigation

**`nav-bar`** — A solid #0096ff bar at 56px height carries the SheetLabels logo in white, a persistent search input with an attached submit button, and top-level product-category links in white semibold 14px. The full-saturation blue makes the bar visually dominant and cleanly separates it from the white catalog content below. No secondary color appears in the bar — it functions as a pure brand signal.

**`mega-menu`** — Triggered on hover over category nav links, the panel drops on a white surface with a 3px solid `{colors.primary}` top border and a 12px box shadow. Column headings use `{typography.title-sm}`, sub-links use `{typography.body-sm}` at `{colors.ink}`. The top-border echo of the nav color creates visual continuity without repeating the full blue background in the dropdown. Active link states use `{colors.primary}` text.

### Search

**`search-bar`** — Full-width within a constrained container. Zero-radius (`{rounded.none}`) input field with a right-attached `{colors.primary}` submit button carrying a white magnifying-glass icon. The sharp rectangular form mirrors the grid's geometry — this is a catalog search tool, not a conversational prompt. Focus ring applies `{colors.primary}` border color to the input.

### Products

**`product-card`** — White surface with a 1px `{colors.hairline}` border and `{rounded.sm}` corners, no drop shadow. The thumbnail occupies roughly 55–60% of card height with the label shape on white or light-gray background. Below the image: the product name in `{typography.title-sm}`, dimensions in bold `{typography.dimension-spec}` (e.g., "2" × 4""), per-sheet count in `{typography.body-sm}`, price in `{typography.price-display}`, and a monospace SKU in `{typography.sku-code}`. Material type badges (`badge-material`) stack horizontally beneath the SKU. The dense information stack is intentional — buyers need specs at a glance without clicking through.

**`badge-sale`** — An absolute-positioned #da532c chip at the top-left corner of the product thumbnail. White uppercase `{typography.badge}` text, 4px radius, tight padding. Carries text like "SALE," "15% OFF," or "BULK DEAL." Because #da532c appears only on sale/urgency signals, this badge color functions as an immediate semantic shorthand.

**`badge-material`** — A light blue-tinted chip in `{colors.badge-material-bg}` with `{colors.badge-material-text}` text, uppercase `{typography.badge}`. Indicates substrate: "GLOSS," "MATTE," "WEATHERPROOF," "KRAFT," "CLEAR." Multiple badges stack horizontally and wrap to a second line as needed. The blue tint echoes the primary hue family without competing with the active-blue interactive elements.

**`badge-new`** — A `{colors.success}` green chip using the same radius and `{typography.badge}` scale, reserved for newly added SKUs or recently introduced materials. Appears alongside badge-material, never overlapping badge-sale.

### Configurator

**`configurator-panel`** — The product detail page's primary interaction surface: a `{colors.surface-soft}` panel with a 1px hairline border and `{rounded.sm}` corners. Section labels in `{typography.title-sm}`, descriptive copy in `{typography.body-md}`. Dimension inputs, material selectors, quantity break tables, and finish options all live within this container. Active selection states apply a `{colors.primary}` border to the relevant control, using the same blue that runs through all interactive chrome.

**`quantity-input`** — A three-part stepper at 38px height: a hairline-bordered number input flanked by minus and plus buttons. Stepper buttons use `{colors.surface-soft}` fill at rest; on hover they fill to `{colors.primary}` with white text, the same transition pattern as button-primary. This signals that quantity is a primary decision node — not an afterthought spinner — appropriate for a catalog where unit economics change at volume breaks.

### Promotional

**`promo-banner`** — A full-width `{colors.accent}` strip at 8px vertical padding used for site-wide urgency messages ("Free Shipping Over $50," "Flash Sale Ends Tonight"). White `{typography.body-md}` text, no icon decoration. Sits above the nav bar or immediately below it. The orange-red matches no other persistent UI element, ensuring it registers as an alert rather than structural navigation.

**`hero-banner`** — A #0096ff full-width block with white display heading in `{typography.display-xl}`, white subtitle in `{typography.body-md}`, and a `{colors.accent}` CTA button. The monochromatic blue field keeps brand voltage high without introducing a third hue into the hero zone. Image overlays may appear as a right-aligned product shot or label-stack photograph cropped to the panel height.

### Navigation Aids

**`breadcrumb`** — Compact `{typography.caption}` trail sitting above category titles and product detail headings. Ancestor nodes in `{colors.muted}`, current node in `{colors.ink}` with no underline or pointer. Separated by "/" with `{spacing.xs}` horizontal padding. Kept visually subdued so it aids orientation without distracting from the product title directly below.

**`pagination`** — A row of numbered links at `{rounded.xs}` corners. Active page fills `{colors.primary}` with white `{typography.body-sm}` text. Inactive pages show `{colors.body}` on transparent, hovering to `{colors.surface-soft}`. Previous/Next chevron buttons use `{colors.primary}` fill on hover, matching link affordance patterns across the site.

### Footer

**`footer`** — A deep navy (#1e3a5f) block that departs from the bright #0096ff nav, creating a bracketing effect: the site opens in full-saturation primary blue and closes in its dark desaturated cousin. Column headings in white `{typography.title-sm}`, links in `{colors.footer-link}` (#9dc8f0 — a muted sky-blue that harmonizes with both the brand blue and the dark background). The color shift signals authority and company credibility without requiring a second brand family.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + logo; search moves to full-width second row; product grid drops to 2-column; configurator panel goes full-width stacked below product image; mega-menu becomes a slide-out drawer |
| Tablet | 744–1128px | 3-column product grid; nav shows top-level links without mega-menu hover; search stays inline in header; configurator panel sits beside product image in a 50/50 split |
| Desktop | 1128–1440px | 4-column product grid; full mega-menu on hover; search bar and category links inline in `{colors.nav-bg}` bar; configurator panel in right column beside image gallery |
| Wide | > 1440px | Content centered in ~1400px max-width container; side whitespace grows proportionally; hero banner heading scales to `{typography.display-xl}`; product grid may expand to 5 columns |

### Touch Targets
- All primary and accent buttons minimum 44×44px on mobile
- Quantity stepper ± buttons each expand to 44px width and full input height on touch viewports
- Product card tap area covers the full card surface, not just the title or image
- Mega-menu drawer links minimum 44px tap height on mobile
- Search submit button minimum 44×44px
- Filter chips and material selectors minimum 36px height with 8px horizontal padding

### Collapsing Strategy
- Primary nav collapse: mega-menu hover taxonomy → slide-out hamburger drawer at < 744px; all categories accessible one level deep
- Grid collapse: 4-col → 3-col (tablet) → 2-col (mobile); never 1-col for products, as side-by-side comparison is load-bearing for spec-driven buyers
- Configurator: desktop shows image gallery left + configurator right; below 744px the image moves above, configurator below, full-width
- Promo banner: persists full-width at all breakpoints; font size reduces from 16px to 14px on mobile; single-line messages only
- Footer: 4-column layout at desktop, 2-column at tablet, single-column accordion at mobile with each section collapsible

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family stacks were extractable from the live site; the typography system defaults to system-ui. The actual site likely uses a licensed web font (Open Sans, Lato, or a similar neutral sans-serif) loaded via JavaScript or a CDN not captured in static extraction.
- Only two brand hex values were identified (#0096ff, #da532c); all neutral tokens (ink, muted, hairline, surface-soft, footer-bg, footer-link) are derived from standard e-commerce conventions rather than direct extraction.
- Exact button corner radius was not confirmed — the site may use fully square (`{rounded.none}`) or slightly larger (`{rounded.sm}`) corners rather than the 4px (`{rounded.xs}`) assumed here.
- Icon style (outlined vs. filled, stroke weight, glyph set family) was not recoverable; components referencing icons assume a standard 16–24px icon grid compatible with either Material Icons or a generic SVG library.
- Whether #da532c is deployed as a CTA color on non-promotional primary actions (e.g., "Add to Cart" on sale items) or exclusively on sale/urgency signals is ambiguous from static extraction.
- Hover, focus, and active state animation durations and easing curves are unspecified; 150ms ease-in-out is assumed throughout.
- Quantity-break pricing table component (tiered price display within the configurator) is inferred from category conventions but not confirmed in extracted data.
