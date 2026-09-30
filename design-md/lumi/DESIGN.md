---
version: alpha
name: "Lumi"
source_url: "https://www.lumi.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every CTA on Lumi burns the same warm amber-orange (#ff5c28) against a near-black marketing canvas (#0d0d0d) — a single voltage that distinguishes this brand from the white-field-plus-generic-blue register of most B2B SaaS. The choice is intentional: Lumi sells packaging as infrastructure to founders and ops leads, and the dark-field-orange-signal pairing reads more like a logistics control room than a checkout page. Type is geometric sans-serif, most likely Inter or a close sibling, at compressed weights and tight negative tracking; headlines arrive at 52px, weight 700, with -1.5px letter-spacing — a specification-board density that signals a tool for operations professionals, not a lifestyle storefront. Corner radii stay spare: `{rounded.sm}` (4px) on buttons and inputs, `{rounded.md}` (8px) on cards, and fully square `{rounded.none}` on data-table rows. There is no pill button anywhere in the primary transactional flow.

  The platform runs three distinct surface registers: a marketing tier (dark canvas, large display type, orange CTAs, generous section spacing), a dashboard/account tier (light canvas, tight 8px grids, small body type, hairline separators), and a quoting/ordering tier (tabular data, monospace spec labels, a live pricing calculator that highlights active inputs with `{colors.primary}`). This stacking is unusual — most consumer-facing companies flatten everything into a single visual register — and it reflects Lumi's position as packaging infrastructure for other brands rather than a product sold directly to consumers. Brand-signature moments concentrate in that pricing calculator where `{colors.primary}` glows on focus, a browser-rendered packaging visualizer on a `{colors.mono-100}` field, and an order-status tracker styled as a logistics manifest with `{typography.caption}` overline labels and `{colors.primary}` active dots. Imagery is almost entirely product photography — die-cut packaging forms on white or near-black backgrounds — with no aspirational lifestyle photography in the primary marketing position. The footer collapses to `{colors.ink}` black with muted navigation links, closing the frame in the same dark register that opens the homepage. The net effect reads like a platform built by engineers who care about brand: structured, orange-lit, precise without being cold.

colors:
  primary: "#ff5c28"
  primary-active: "#e04a18"
  primary-disabled: "#ffc4af"
  ink: "#0d0d0d"
  body: "#1a1a1a"
  muted: "#6b6b6b"
  hairline: "#2a2a2a"
  hairline-light: "#e5e5e5"
  canvas: "#ffffff"
  canvas-dark: "#0d0d0d"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark-card: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  orange-muted: "#ff8a64"
  orange-faint: "#fff1ec"
  success: "#22c55e"
  error: "#ef4444"
  mono-100: "#f5f5f5"
  mono-200: "#e5e5e5"
  mono-300: "#d4d4d4"
  mono-700: "#404040"
  mono-900: "#171717"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1.5px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.8px
  display-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.4px
  title-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.1px
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-mono:
    fontFamily: "'JetBrains Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  overline:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  spec-label:
    fontFamily: "'JetBrains Mono', 'Fira Code', monospace"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
    padding: 12px 24px
    height: 44px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-light}"
    padding: 11px 23px
    height: 44px
  button-secondary-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid rgba(255,255,255,0.25)"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-light}"
    focusBorder: "1px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
  text-input-dark:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-light}"
  nav-bar-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-light}"
    padding: "{spacing.lg}"
    imageRounded: "{rounded.md}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
  product-card-dark:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
  hero-marketing:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
    ctaStyle: "button-primary"
  pricing-calculator:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.lg}"
    border: "1px solid {colors.hairline-light}"
    inputStyle: "text-input"
    focusHighlight: "{colors.primary}"
    labelTypography: "{typography.overline}"
    valueTypography: "{typography.display-sm}"
    valueColor: "{colors.primary}"
  spec-chip:
    backgroundColor: "{colors.mono-100}"
    textColor: "{colors.ink}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  spec-chip-dark:
    backgroundColor: "{colors.mono-900}"
    textColor: "{colors.on-dark}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  packaging-visualizer:
    backgroundColor: "{colors.mono-100}"
    rounded: "{rounded.lg}"
    minHeight: 320px
    canvasBackground: "{colors.canvas}"
  order-status-tracker:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-light}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.caption}"
    statusDotActive: "{colors.primary}"
    statusDotComplete: "{colors.success}"
    statusDotPending: "{colors.mono-300}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-category:
    backgroundColor: "{colors.mono-100}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  data-table-row:
    backgroundColor: "{colors.canvas}"
    hoverBackground: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-light}"
    padding: "12px {spacing.base}"
    rounded: "{rounded.none}"
  section-divider:
    borderTop: "1px solid {colors.hairline-light}"
    marginY: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.mono-300}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — The primary action token in orange (#ff5c28) at 44px height with `{rounded.sm}` corners and weight-600 button text. Hover darkens to `{colors.primary-active}` (#e04a18) with no scale transform. Disabled state softens to `{colors.primary-disabled}` and blocks pointer events. Used on every primary CTA: "Get Started", "Request a Quote", calculator submit.

**`button-secondary`** — White fill with a 1px `{colors.hairline-light}` border and `{colors.ink}` text, matching the primary button's height and padding exactly. Sits alongside `button-primary` in two-action rows where the secondary action is "Learn More" or "See Examples". A dark-surface variant (`button-secondary-dark`) replaces the border with `rgba(255,255,255,0.25)` for use over `{colors.canvas-dark}` hero sections.

**`button-ghost`** — Transparent background, `{colors.ink}` text, no border. Reserved for tertiary actions inside dense dashboard panels where adding a bordered button would create visual noise.

### Navigation

**`nav-bar`** / **`nav-bar-dark`** — A 64px sticky bar that switches registers based on page context: light (`{colors.canvas}`) on interior dashboard and product pages, dark (`{colors.canvas-dark}`) on the marketing homepage hero. Both variants use `{typography.nav-link}` (14px, weight 500). Product category dropdowns use hover-reveal panels rather than mega-menus. The Lumi wordmark anchors left; primary CTAs anchor right.

### Forms & Inputs

**`text-input`** / **`text-input-dark`** — 44px height, `{rounded.sm}`, with a 1px hairline border that transitions to `{colors.primary}` on focus — the orange focus ring is the clearest on-screen signal that this brand is interactive. Dark variant used inside the pricing calculator and dashboard modals.

### Cards

**`product-card`** — Packaging category cards with `{rounded.md}` corners, a 1px `{colors.hairline-light}` border, and `{spacing.lg}` internal padding. Images sit in a `{rounded.md}` container at the top; title uses `{typography.title-sm}` and body uses `{typography.body-sm}`. The dark variant (`product-card-dark`) mirrors these values against `{colors.surface-dark-card}` for use in dark-themed feature sections.

### Hero

**`hero-marketing`** — Full-width dark-canvas (`{colors.canvas-dark}`) section with `{typography.display-xl}` headline at negative tracking and `{spacing.section}` vertical padding. Subheadline runs `{typography.body-md}` in `{colors.on-dark}`. A single `button-primary` CTA sits below. Background may include a subtle grid or product-outline illustration in dark gray — never photography at this position.

### Pricing Calculator

**`pricing-calculator`** — A `{colors.surface-soft}` panel with `{rounded.lg}` corners that accepts packaging type, dimensions, quantity, and material inputs using `text-input` fields. Active input borders highlight with `{colors.primary}`. The live price output renders in `{typography.display-sm}` weight 600 at `{colors.primary}` — the orange value is the payoff of the interaction. Section labels use `{typography.overline}` (uppercase, 0.8px tracking) to separate input groups.

### Spec Chips

**`spec-chip`** / **`spec-chip-dark`** — Monospace `{typography.spec-label}` label in a 2px-rounded pill, used to surface packaging dimensions, material codes, and print specs inline on product cards and the quoting tool. The light variant sits on white surfaces; the dark variant on `{colors.mono-900}` for use in dark table cells.

### Order Status Tracker

**`order-status-tracker`** — A manifest-style timeline panel with `{typography.caption}` overline labels (ORDERED, IN PRODUCTION, SHIPPED, DELIVERED) and `{colors.primary}` dot for the active state, `{colors.success}` for completed steps, and `{colors.mono-300}` for pending. The overall container uses a 1px `{colors.hairline-light}` border and `{rounded.md}` at `{spacing.lg}` padding.

### Packaging Visualizer

**`packaging-visualizer`** — A browser-rendered 3D/flat-layout packaging preview on a `{colors.mono-100}` background inside a `{rounded.lg}` container with a minimum height of 320px. Inner canvas is white (`{colors.canvas}`). No brand chrome inside the visualizer frame — the packaging art fills the space uninterrupted.

### Badges

**`badge-new`** — Orange `{colors.primary}` fill, white text, `{typography.overline}` uppercase, `{rounded.xs}` — used sparingly on new material types or product categories in the catalog.

**`badge-category`** — Neutral `{colors.mono-100}` fill with `{colors.muted}` caption text at `{rounded.xs}` — applied to product listing pages as filterable category tags (Mailer Boxes, Poly Mailers, Labels, etc.).

### Data Table

**`data-table-row`** — Square corners (`{rounded.none}`), 1px `{colors.hairline-light}` bottom border, `{typography.body-sm}` text. Hover state surfaces `{colors.surface-soft}` background. Used in the order history and account dashboards where density matters.

### Footer

**`footer`** — Full `{colors.ink}` black background with `{colors.on-dark}` primary text and `{colors.mono-300}` for secondary links. `{typography.body-sm}` throughout. `{spacing.section}` padding. Columns: Product, Company, Resources, Legal. Bottom row holds copyright and social icons as outline circles.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger drawer on `{colors.canvas-dark}`; `display-xl` drops to 34px; pricing calculator stacks inputs vertically; product cards go full-width; hero CTA block stacks headline above subhead above button |
| Tablet | 744–1128px | Two-column product grid; nav shows wordmark + primary CTA only, secondary links in drawer; hero restores two-column text/visual split; pricing calculator goes two-column input grid |
| Desktop | 1128–1440px | Full nav bar with all category links visible; three- or four-column product grid; hero at full `display-xl` 52px; packaging visualizer appears alongside the quoting form |
| Wide | > 1440px | Max content width 1280px centered; hero section adds lateral padding; visualizer panel widens; data tables gain additional visible columns |

### Touch Targets

- All interactive elements minimum 44×44px on mobile (buttons, input fields, nav items)
- Spec chips expand tap area with 8px invisible padding on mobile to prevent mis-taps
- Order tracker step dots minimum 32px tap target with extended hit area
- Dropdown nav items use 48px row height on mobile drawer

### Collapsing Strategy

- Pricing calculator collapses advanced options (material finish, printing sides) behind an expandable "Advanced Options" row on mobile; core inputs (type, size, quantity) always visible
- Product card metadata (spec chips, material callouts) collapses to a single "View specs" link below the fold on mobile
- Data table columns prioritize: status, date, order number — secondary columns (unit price, SKU) hidden on mobile behind a row-expand chevron
- Footer switches from four-column to accordion-collapsed sections on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site — the site likely loads design tokens via JavaScript or is behind anti-bot protection. All color values in this file are approximated from visual brand observation and should be verified against the live site or Lumi's internal design system before production use.
- No font-family stacks were extracted. Inter is inferred from the geometric sans-serif appearance; the actual typeface (and whether a custom variable font is used) must be confirmed.
- Dark-mode behavior is unconfirmed — it is unclear whether the platform dashboard uses the same dark-canvas theme as the marketing homepage or switches to a light canvas.
- Exact button border-radius values are estimated at 4px (`{rounded.sm}`); the live site may use 6px or 3px.
- Dashboard and account-portal UI (post-login surfaces) are not publicly crawlable; the data table, order tracker, and visualizer component specs are inferred from marketing screenshots and product documentation pages.
- Animation and transition timing values (hover durations, calculator live-update behavior) could not be extracted and are not defined in this spec.
- Icon set identity (whether Lumi uses a licensed icon library or custom SVGs) is unknown.
