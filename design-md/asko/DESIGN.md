---
version: alpha
name: "Asko"
source_url: "https://www.asko.com/us"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep Nordic navy (#14293a) — the color of a Baltic winter dusk — anchors every navigation bar, hero panel, and primary call-to-action across ASKO's digital storefront, separating the brand from the clinical silvers and appliance-white defaults that crowd the laundry category. The canvas underneath is not pure white but a warm parchment (#f7f6f4), the off-white you encounter inside a well-lit Stockholm showroom where poured-concrete floors meet birch veneer cabinetry. Typography pairs Questrial for display headings with IBM Plex Sans for body and interface text — both geometric sans-serifs, but Questrial's single 400-weight letterforms give headlines an architectural lightness that IBM Plex's heavier UI weights (500, 600) counterbalance with functional clarity. Weights stay restrained throughout: even the largest hero headline runs regular-weight at 48px, trusting generous letter-spacing and product photography — enormous full-bleed images of brushed-steel drum interiors and flush-mounted control panels — to do the persuasion. A secondary blue (#1f7bc0) surfaces in interactive links and hover states while its darker sibling (#14517e) anchors utility navigation and footer links. The neutral scale runs warmer than expected for an appliance manufacturer: grays like #b8b6b6 and #d8d6d2 lean toward taupe rather than the cool steel most competitors reach for. Corner radii stay modest — `{rounded.xs}` on buttons and inputs, `{rounded.sm}` on cards — echoing the squared-off geometry of the appliances themselves. Status messaging uses tinted surface panels: soft green (#f0fbe4) for energy-rating confirmations, pale red (#fff1f1) for stock alerts, warm amber (#fff5df) for promotional callouts, each paired with its semantic accent. Spacing is generous — `{spacing.section}` between content blocks creates the breathing room that premium positioning requires. Product cards present as clean containers on `{colors.surface-card}` with `{colors.hairline}` borders, letting the product image and a two-line specification summary speak without decorative noise. The overall impression is a digital showroom that borrows its confidence from physical retail heritage: clean sightlines, materials that feel substantial, and an editorial restraint that trusts the engineering to sell itself.

colors:
  primary: "#14293a"
  primary-active: "#212738"
  primary-disabled: "#8e9baa"
  accent-blue: "#1f7bc0"
  accent-blue-dark: "#14517e"
  ink: "#1e1e1e"
  body: "#5e5e5e"
  muted: "#6c7079"
  muted-soft: "#b8b6b6"
  hairline: "#d8d6d2"
  hairline-soft: "#d3d6db"
  canvas: "#f7f6f4"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  surface-alt: "#f4f4f4"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#38871f"
  error: "#db0002"
  success-bg: "#f0fbe4"
  error-bg: "#fff1f1"
  warning-bg: "#fff5df"
  info-bg: "#deeffe"
  link: "#055f9f"
  scrim: "rgba(30, 30, 30, 0.6)"

typography:
  display-xl:
    fontFamily: "'Questrial', 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Questrial', 'IBM Plex Sans', -apple-system, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Questrial', 'IBM Plex Sans', -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'IBM Plex Sans', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'IBM Plex Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'IBM Plex Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'IBM Plex Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'IBM Plex Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'IBM Plex Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  overline:
    fontFamily: "'IBM Plex Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'IBM Plex Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'IBM Plex Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'IBM Plex Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  spec-label:
    fontFamily: "'IBM Plex Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'IBM Plex Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    borderWidth: 1.5px
    borderColor: "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.button-sm}"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 2px 8px rgba(30, 30, 30, 0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    borderWidth: 1px
    borderColor: "{colors.hairline}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(20, 41, 58, 0.1)"
    borderColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xxl}"
  hero-banner-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
  feature-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  specification-row:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline}"
  specification-row-alt:
    backgroundColor: "{colors.surface-alt}"
  energy-badge:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  promo-badge:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  status-banner-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  status-banner-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  status-banner-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  status-banner-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.accent-blue-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  comparison-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  comparison-cell:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    gap: "{spacing.sm}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    textColor: "rgba(255, 255, 255, 0.7)"
    typography: "{typography.nav-link}"
  mega-menu:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    boxShadow: "0 8px 32px rgba(30, 30, 30, 0.12)"
    padding: "{spacing.xl}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    aspectRatio: "4/3"
  category-tile-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  overline-label:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.overline}"
---

## Components

### Buttons

**`button-primary`** — Solid deep-navy rectangle with `{rounded.xs}` corners and white text set in `{typography.button-md}`. On hover, the background deepens to `{colors.primary-active}` (#212738) with a 200ms ease transition. Disabled state washes to `{colors.primary-disabled}` with reduced opacity. The 48px height and 28px horizontal padding give the button enough presence on product pages without overwhelming the sparse layout.

**`button-secondary`** — A 1.5px navy-outlined rectangle on a transparent background, matching the primary button's dimensions and corner radius. On hover, the fill inverts: background becomes `{colors.primary}` and text flips to `{colors.on-primary}`, creating a clean toggle effect. Used for secondary actions like "Compare Models" and "Download Specifications."

**`button-tertiary`** — An underline-on-hover text link in `{colors.accent-blue}`, used inline within body copy or specification panels. No background, no border, minimal padding — just the text itself with a baseline underline that fades in on hover.

### Navigation

**`nav-bar`** — A 72px-tall white bar pinned to the top of the viewport. The ASKO wordmark sits left in `{colors.ink}`, and primary category links (Laundry, Dishwashing, Cooking, Cooling) are spaced evenly in `{typography.nav-link}`. On scroll, the bar gains a soft box-shadow via `nav-bar-scrolled`, dropping the bottom border in favor of the shadow for depth. A 1px `{colors.hairline}` border separates the nav from the content below at rest.

**`mega-menu`** — Opens below the nav bar as a full-width dropdown panel on `{colors.surface-card}` with an 8px blur-radius shadow. Product sub-categories appear as `{typography.nav-link}` links organized in columns, supplemented by `category-tile` visual entry points showing product imagery. The menu opens with a 250ms slide-down and fades the page content behind a light `{colors.scrim}` overlay.

**`breadcrumb`** — A horizontal trail in `{typography.caption}` at `{colors.muted}`, with right-chevron separators spaced at `{spacing.sm}`. The terminal item renders in `{colors.ink}` via `breadcrumb-active` without a trailing link.

### Hero

**`hero-banner`** — Full-bleed container at a minimum 560px height, typically split between a product lifestyle photograph (a washer recessed into a matte-black laundry alcove, a dishwasher flush-mounted in a birch kitchen island) and a content panel. In the dark variant, the background is `{colors.primary}` with the headline set in `{typography.display-xl}` at white. The light variant (`hero-banner-light`) flips to `{colors.canvas}` with `{colors.ink}` type. A single `button-primary` or `button-secondary` CTA sits below the subhead with `{spacing.lg}` clearance. Product model identifiers appear above the headline as an `overline-label`.

### Product Cards

**`product-card`** — A contained card with `{rounded.sm}` corners and a 1px `{colors.hairline}` border on `{colors.surface-card}`. The product image fills the upper two-thirds at a 4:3 aspect ratio on a neutral background. Below the image, the model name appears in `{typography.title-sm}`, followed by a one-line feature summary in `{typography.body-sm}` at `{colors.body}`. On hover, the card lifts with `product-card-hover` shadow and the border shifts to `{colors.primary}`. An optional `energy-badge` or `promo-badge` floats in the top-right corner of the image area, offset by `{spacing.sm}`.

### Category Tiles

**`category-tile`** — A 4:3 rectangular tile on `{colors.surface-soft}` with `{rounded.sm}` corners, showing a centered product category image with the category name in `{typography.title-sm}` below or overlaid. On hover via `category-tile-hover`, the entire tile fills with `{colors.primary}` and text inverts to `{colors.on-primary}`, providing strong interactive feedback. Used in mega-menus and category landing pages.

### Specification & Comparison

**`specification-row`** — A key-value row on product detail pages. The specification label sits left in `{typography.spec-label}` at `{colors.body}`, the value right-aligned in the same style. Rows alternate between transparent and `{colors.surface-alt}` backgrounds via `specification-row-alt`, separated by a 1px `{colors.hairline}` bottom border. Rows group logically under section headers set in `{typography.title-sm}`.

**`comparison-header`** — The sticky top row of the product comparison table, rendered in `{colors.primary}` with white text in `{typography.title-sm}`. Each column contains a product thumbnail, model number, and a "Remove" icon button. The header remains visible while scrolling through specification rows below.

**`comparison-cell`** — Individual data cells in the comparison grid, using `{typography.spec-label}` on `{colors.surface-card}`, separated by `{colors.hairline}` borders. Cells that match across compared products receive no special treatment; differences may be highlighted with a subtle `{colors.info-bg}` background.

### Feature Panels

**`feature-panel`** — A soft-background container on `{colors.surface-soft}` with `{rounded.sm}` corners and `{spacing.xl}` internal padding. Contains a title in `{typography.title-md}`, a body paragraph in `{typography.body-md}`, and optionally a product image, icon, or animation. Used throughout product detail pages to highlight specific technologies — Steel Seal drum construction, Active Drum wash motion, Pro Wash spray systems — each panel acting as a self-contained feature story.

### Badges

**`energy-badge`** — A compact label on `{colors.success}` with white uppercase text in `{typography.badge}`, rendered with `{rounded.xs}` corners. Displays energy efficiency ratings (A+++, A++) on product cards and detail pages. Positioned absolutely in the top-right of the product image container.

**`promo-badge`** — Identical geometry to `energy-badge` but on `{colors.error}` background. Used for promotional tags like "NEW" or "SALE" and positioned in the same image-corner slot; only one badge renders per card.

### Status Banners

**`status-banner-success`** — A notification bar on `{colors.success-bg}` with `{colors.success}` text, an optional checkmark icon left-aligned, and `{rounded.sm}` corners. Used for availability confirmations and order-status updates.

**`status-banner-error`** — Same structure on `{colors.error-bg}` with `{colors.error}` text. Surfaces for form validation summaries and out-of-stock alerts.

**`status-banner-warning`** — Amber-tinted background (`{colors.warning-bg}`) with `{colors.ink}` text. Used for shipping-delay notices and partial-availability warnings.

**`status-banner-info`** — Blue-tinted background (`{colors.info-bg}`) with `{colors.accent-blue-dark}` text. Used for informational callouts: installation guides, warranty details, service reminders.

### Search

**`search-bar`** — A 48px-tall input on `{colors.surface-soft}` with `{rounded.xs}` corners. Placeholder text renders in `{colors.muted}`, active input in `{colors.ink}`. A magnifying-glass icon sits left-aligned within the field. On focus, a 1px border in `{colors.primary}` fades in at 150ms. Search suggestions drop below in a `{colors.surface-card}` panel with `mega-menu`-style shadow.

### Text Input

**`text-input`** — Standard form input at 48px height with a 1px `{colors.hairline}` border and `{rounded.xs}` corners on `{colors.surface-card}`. Active state transitions the border to `{colors.primary}` at 150ms. Error state applies `text-input-error`, swapping the border to `{colors.error}` and rendering inline validation text in `{typography.caption}` below the field.

### Footer

**`footer`** — Full-width block on `{colors.primary}` with white text. Content organizes into four-column link groups using `footer-link` styling — `{typography.nav-link}` at 70% white opacity — with column headers in full-white `{typography.title-sm}`. The ASKO wordmark and legal copy appear in a lower row in `{typography.caption-sm}` at reduced opacity. Total vertical padding is `{spacing.section}`.

### Labels

**`overline-label`** — An uppercase eyebrow label in `{typography.overline}` at `{colors.muted}`, used above section titles and product names to provide category context (e.g., "WASHING MACHINES", "PRO SERIES", "ELEMENTS"). Spaced `{spacing.sm}` below itself before the headline it introduces.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Hero banner stacks image above copy at 360px min-height. Nav collapses to a hamburger icon with a full-height slide-out drawer. Product grid becomes a single-column scrollable list. Comparison table scrolls horizontally with a sticky first column for spec labels. Footer stacks to a single-column accordion. |
| Tablet | 744–1128px | Two-column product grid. Hero banner retains side-by-side layout at a 40/60 image-to-content ratio. Mega-menu renders as a single scrollable column instead of multi-column. Feature panels stack vertically. Specification rows remain full-width. |
| Desktop | 1128–1440px | Three- or four-column product grid. Full mega-menu with multi-column category layout. Hero at full 560px height with 50/50 split. Comparison table supports up to four products side-by-side. Feature panels display in two-up horizontal arrangements. |
| Wide | > 1440px | Content max-width caps at 1440px and centers horizontally. Side margins grow symmetrically. Hero banner may extend full-bleed while inner content remains constrained. Product grid holds at four columns. |

### Touch Targets
- All interactive elements maintain a minimum 44×44px touch target on mobile via padding expansion
- Product card entire surface is tappable on mobile, not just the title link
- Comparison table cells expand vertically on touch devices to accommodate finger taps
- Footer accordion headers carry 48px tap height with clear expand/collapse chevron indicators

### Collapsing Strategy
- Navigation categories collapse into a hamburger icon below 744px, opening a full-height slide-out drawer with accordion-expandable category sections
- Product specification tables collapse into expandable accordion rows on mobile, with the section header as the toggle trigger
- Feature panels reorder from two-up horizontal to single-column vertical via CSS grid reflow
- Footer link columns collapse into expandable accordion sections, with `{typography.title-sm}` headers as toggles
- Comparison tool limits to two products on mobile (four on desktop), with horizontal swipe navigation between product columns
- Mega-menu converts from a multi-column overlay to a full-screen slide-in panel on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font assignments per element could not be confirmed — Questrial, IBM Plex Sans, and Inter all appear in stylesheets, but which serves as display vs. body vs. UI may differ from the pairing assumed here
- No CSS custom-property or design-token variable names were extracted; token naming in this file is inferred from visual hierarchy and role
- Logo SVG dimensions, wordmark lockup spacing, and the full icon set are not documented
- Animation durations and easing curves for hover states, menu transitions, and page-load sequences are estimated, not measured
- Product comparison interaction patterns (add/remove, sticky scroll behavior, highlight logic) are assumed from common appliance-site conventions
- The warm canvas (#f7f6f4) may shift to pure white (#ffffff) on certain interior or account pages — extraction captured the homepage palette only
- Mobile gesture patterns (swipe for comparison columns, pull-to-refresh) could not be verified from static extraction
- Form validation UX beyond border-color change (inline error messages, field-shake animations) is not documented
- Exact responsive breakpoints are estimated from common patterns; ASKO may use custom values not visible in extracted CSS
