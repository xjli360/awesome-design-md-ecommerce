---
version: alpha
name: "Lista"
source_url: "https://www.lista.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Where most tool-storage competitors reach for safety-orange or hi-vis yellow to signal industrial credibility, Lista anchors its visual identity in a deep Swiss corporate navy (#003399) — the color of aerospace tolerances and precision instrumentation, not a showroom gesture. Paired with a mechanical mid-blue (#008bd2) that reads like anodized aluminum detailing, and grounded by a neutral gray (#707070) for secondary labeling, the palette operates as a strict two-tone system derived from European engineering culture: navy owns headers, primary CTAs, and structural navigation; the lighter blue carries interactive states and accent rules that break up specification-heavy pages. No warm tones dilute the navy's authority; no tertiary hues compete with it.

  Typography runs Ballinger as the primary display face — a geometric sans-serif whose near-circular letterforms share design DNA with ITC Avant Garde Gothic Pro, Lista's secondary face deployed in label and caption contexts. Both typefaces trace back to the rationalist 1960s–70s tradition that produced Swiss railway signage and industrial machine manuals. Display type sits large and confident, often uppercase with open tracking for section headings; body text runs at 16px regular weight for specification paragraphs that run long and technical. The system never reaches for a serif face — nothing in Lista's product line invites antiquarian warmth.

  Interface geometry is tight: buttons and inputs arrive with near-square 2px corners (`{rounded.xs}`), reflecting a grid system where radius is functional compression, not friendliness. Product cards are specification-first — load ratings, dimension arrays, and drawer counts lead before lifestyle photography appears. The hero section is a full-width navy module with a photographic overlay and centered display type that establishes institutional scale before the user reaches a product configurator or category browser.

  At wide breakpoints Lista centers content within a roughly 1280px container while the navy header, footer, and full-bleed accent bars extend edge to edge — an enterprise-facing layout discipline that signals this is a specifying tool for procurement managers, not a consumer storefront. The overall register is information-dense, legible at any zoom level, and free of decorative surface treatment.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#99aacc"
  secondary: "#008bd2"
  secondary-active: "#006fa8"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#707070"
  hairline: "#d0d0d0"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f6f7"
  surface-card: "#ffffff"
  surface-dark: "#001f66"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Ballinger', 'ITC Avant Garde Gothic Pro', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Ballinger', 'ITC Avant Garde Gothic Pro', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Ballinger', 'ITC Avant Garde Gothic Pro', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Ballinger', 'ITC Avant Garde Gothic Pro', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Ballinger', 'ITC Avant Garde Gothic Pro', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Ballinger', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Ballinger', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Ballinger', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-caps:
    fontFamily: "'Ballinger', 'ITC Avant Garde Gothic Pro', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Ballinger', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Ballinger', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Ballinger', 'ITC Avant Garde Gothic Pro', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Ballinger', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Ballinger', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 24px
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
    padding: "12px 24px"
    height: 44px
    border: none
    hoverBackgroundColor: "{colors.primary-active}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "11px 23px"
    height: 44px
    border: "1px solid {colors.primary}"
    hoverBackgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "10px 16px"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.muted}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "10px 14px"
    height: 44px
    border: "1px solid {colors.hairline}"
    focusBorderColor: "{colors.primary}"
    focusOutlineColor: "{colors.secondary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "3px solid {colors.secondary}"
    logoColor: "{colors.on-primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    hoverBorderColor: "{colors.secondary}"
    hoverBoxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    minHeight: 480px
    overlayColor: "rgba(0,51,153,0.55)"
    paddingVertical: "{spacing.section}"
    ctaSpacingTop: "{spacing.xl}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    stripeColor: "{colors.surface-soft}"
    rowHeight: 40px
  configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.label-caps}"
    labelColor: "{colors.muted}"
    accentColor: "{colors.secondary}"
    selectedBorderColor: "{colors.primary}"
  category-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    hoverTextColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.primary}"
    height: 44px
    focusBorderColor: "{colors.secondary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    headingColor: "{colors.on-primary}"
    linkColor: "rgba(255,255,255,0.7)"
    linkHoverColor: "{colors.on-primary}"
    borderTopColor: "{colors.secondary}"
    legalTypography: "{typography.caption}"
    paddingVertical: "{spacing.xxl}"

---

## Components

### Buttons

**`button-primary`** — Navy (#003399) fill with white label set in `{typography.button-md}` at 0.5px letter-spacing, 44px height, and near-square 2px corners (`{rounded.xs}`). On hover, the fill deepens to `{colors.primary-active}` (#002277) with no transition softening — the shift is immediate, matching the brand's engineering directness. Used for primary configuration CTAs ("Configure", "Request Quote", "Download Datasheet") and top-level search submission.

**`button-secondary`** — White fill with a navy border and navy label, matching the primary's 44px height and `{rounded.xs}` geometry. On hover, background fills to `{colors.surface-soft}` as a low-contrast wash. Appears alongside the primary in dual-CTA arrangements where one action requires secondary emphasis — for example, "Configure" paired with "View Datasheet".

**`button-ghost`** — Transparent background with a `{colors.hairline}` border and `{colors.body}` label type in `{typography.button-sm}`. 10px vertical / 16px horizontal padding. Used for utility actions — pagination, filter resets, secondary download links, and subsidiary navigation controls. Border transitions to `{colors.muted}` on hover.

### Text Input

**`text-input`** — White canvas with `{colors.hairline}` border and `{rounded.xs}` corners. On focus, border color shifts to `{colors.primary}` with a 2px secondary outline in `{colors.secondary}` providing an accessible highlight ring. Placeholder text in `{colors.muted}`. Height 44px, internal padding 10px / 14px. Deployed across all form contexts: configurator option entry, RFQ and dealer-locator forms, newsletter sign-up. Error state is expected to use a distinct border color; not confirmed from extraction.

### Nav Bar

**`nav-bar`** — Full-width navy (#003399) header at 64px height with a 3px bottom accent rule in `{colors.secondary}`. White logotype sits left-aligned; product category links in `{typography.nav-link}` are grouped center-to-right with a search icon, language switcher, and country selector at the far right. Mega-menu dropdowns on product categories expose sub-category grids with thumbnail imagery and secondary navigation links. The bar remains fixed on scroll with no color or opacity transition. Below 1128px, the nav collapses to a hamburger toggle that opens a full-screen navy drawer overlay.

### Product Card

**`product-card`** — White card with a 1px `{colors.hairline}` border and `{rounded.sm}` (4px) corners. Top area holds square-format product photography. Below: product family label in `{typography.caption}` muted gray, product name in `{typography.title-sm}` ink, a key specification line (e.g., "Load capacity: 200 kg") in `{typography.body-sm}`, and a "Configure" button-ghost CTA at the bottom flush edge. On hover, border shifts to `{colors.secondary}` with a low ambient shadow. In grid view, cards run three-per-row at desktop; condensed list view drops the image and expands the specification field horizontally.

### Hero Banner

**`hero-banner`** — Full-width module with a minimum height of 480px. Product or environment photography fills the frame; a navy-tinted overlay at approximately 55% opacity darkens the image for white-text legibility. Title is centered in `{typography.display-xl}`, subtitle in `{typography.body-md}` at reduced opacity below, then `{spacing.xl}` gap before a `button-primary` CTA row. No border-radius is applied (`{rounded.none}`) — the module bleeds fully edge to edge. Used as the primary entry surface on category landing pages and campaign entries; not present on every product detail page.

### Spec Table

**`spec-table`** — Two-column table for technical product specifications. The header row uses `{colors.surface-soft}` background with a category group label in `{typography.spec-label}` (uppercase, 1px tracking). Alternating data rows stripe between white and `{colors.surface-soft}`. The left column renders attribute names ("Dimension", "Load Rating", "Drawer Count") in `{typography.spec-label}` `{colors.muted}`; right column values in `{typography.spec-value}` `{colors.ink}`. 1px `{colors.hairline}` borders all sides, 40px row height. At mobile breakpoints the table scrolls horizontally rather than collapsing — preserving the full column pair so values never orphan from their labels.

### Configurator Panel

**`configurator-panel`** — Surface-soft gray panel with `{rounded.sm}` corners and `{spacing.lg}` internal padding. Section group labels in `{typography.label-caps}`. Interactive option chips — color swatches, dimension selectors, accessory toggles — carry `{colors.hairline}` borders in their default state and `{colors.primary}` border on selected state. A pricing / summary sub-panel anchors sticky to the right column at desktop, collapsing below the options grid on tablet and mobile. Availability indicators and "Most Popular" callouts use `{colors.secondary}` as the accent signal.

### Category Badge

**`category-badge`** — Compact filter label in `{typography.label-caps}` with 4px vertical / 10px horizontal padding and `{rounded.xs}` corners. Default state: `{colors.surface-soft}` background, `{colors.muted}` text. Active/selected state fills to `{colors.primary}` with `{colors.on-primary}` text. Appears as filter pills above product browse grids (e.g., "WORKBENCHES", "DRAWERS", "SHELVING", "ACCESSORIES"). Pill shape (`{rounded.full}`) is intentionally avoided — the brand's angular geometry applies even to small interactive controls.

### Breadcrumb

**`breadcrumb`** — Horizontal ancestor trail in `{typography.caption}`. Ancestor links render in `{colors.muted}`; the current page node in `{colors.ink}`. The separator character "/" is rendered in `{colors.hairline}` with consistent horizontal spacing. Hover transitions link text to `{colors.primary}` without underline. Breadcrumb appears directly below the nav-bar on all product detail and sub-category pages, providing the primary secondary navigation path for deep-linked users arriving from search.

### Search Bar

**`search-bar`** — White input at 44px height with `{rounded.xs}` corners and a `{colors.hairline}` border. A magnifier icon in `{colors.primary}` sits inset at the trailing edge. On focus, the border transitions to `{colors.secondary}`. In the nav-bar context, clicking the search icon expands a full-width overlay drawer over the page rather than an inline input. Typeahead results list items in `{typography.body-sm}` with product category group headers in `{typography.label-caps}` muted gray separating result clusters.

### Footer

**`footer`** — Full-width navy block with a 3px `{colors.secondary}` top border as the primary visual separator from page content. Column headings in `{typography.label-caps}` full white. Link lists in `{typography.body-sm}` at 70% white opacity, transitioning to full `{colors.on-primary}` on hover. A bottom legal strip holds copyright and compliance copy in `{typography.caption}`, social icon links, and a locale / country selector. Vertical padding `{spacing.xxl}` top and bottom. On mobile, column groups collapse into an accordion so the footer depth stays manageable without a long scroll.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen navy drawer; hero min-height reduces to 280px; spec tables scroll horizontally; configurator panel fully stacked; footer columns collapse to accordion |
| Tablet | 744–1128px | Two-column product grid; nav shows primary category labels inline without mega-menu; configurator summary panel moves below options grid; hero at 380px; breadcrumb retained |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu dropdowns active; configurator summary panel sticky-right; content max-width 1280px; hero at 480px |
| Wide | > 1440px | Content container stays at 1280px centered; navy header, footer, and full-bleed hero extend edge-to-edge; no additional grid column increase |

### Touch Targets

- All interactive elements maintain a minimum 44px height on mobile (buttons, inputs, nav links, accordion toggles)
- Category badge filter pills display in a horizontally scrolling row rather than wrapping to multiple lines
- Product card CTAs expand to full card width on mobile for easier tap targeting
- Configurator option chips scale to a minimum 44×44px touch footprint on touch breakpoints
- Footer accordion controls carry a minimum 48px tap height

### Collapsing Strategy

- Navigation: hamburger at < 1128px, full mega-menu dropdown at ≥ 1128px
- Product grid: 3-col → 2-col → 1-col as breakpoints decrease
- Configurator: side-by-side (options left / summary right) → fully stacked below 744px
- Spec table: always horizontal scroll on overflow — never collapses to card-stack format
- Footer: multi-column layout → accordion stack on mobile, no horizontal overflow

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only three hex colors extracted (#003399, #008bd2, #707070) — surface variants, error/success states, hover mid-tones, and disabled fill colors are derived rather than confirmed from live extraction
- No meta theme-color detected — browser chrome color on mobile Safari and Chrome not confirmed
- Ballinger font weight and size scales not confirmed from static extraction; values follow standard geometric-sans usage conventions for industrial B2B contexts
- Exact button dimensions, padding, and border widths not confirmed from live DOM inspection
- Animation and transition timing curves (easing, duration) not extractable from static hints
- Icon system details (SVG sprite vs. icon font, stroke weight, fill vs. outline convention) not available
- Dark mode support unknown — site does not appear to offer a dark variant
- Exact mega-menu structure, sub-category depth, and thumbnail dimensions not confirmed
- Product image aspect ratio and lazy-load strategy not confirmed
- Whether ITC Avant Garde Gothic Pro is a display-face alternative or strictly deployed in label/caption contexts is unconfirmed from extraction
