---
version: alpha
name: "FLIR Systems (Teledyne FLIR)"
source_url: "https://www.flir.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The electric mint at #40e09c sits against #080808 like a thermal signature resolving on a cold sensor — luminous, isolated, precisely locatable. Teledyne FLIR's digital palette is not corporate convention applied to a technology brand; it is the visual logic of thermal imaging operationalized into a UI language. Deep blacks (#080808, #1a1d20) stand in for the cold-field background that makes infrared targets visible; the mint CTA and its spectral cousins (#a0f0ce, #c6f6e1) chart the temperature gradient from ambient to active; amber at #f7a840 and teal at #37aeb3 echo the false-color palettes FLIR's own cameras produce when scanning for heat anomalies in industrial or defense contexts. Typography is anchored by Industry-Light for display headings — a typeface whose name does the positioning work, with geometric precision and restrained weight that reads as instrumentation rather than marketing copy. Inter handles body copy and UI navigation at weights 400–600, holding legibility on dark surfaces without competing with the brand's high-contrast accent system. Museo-Sans fills the gap at data labels, specifications, and compact UI text, where its humanist numerals improve scanability in dense product tables. Rounding is minimal: buttons take `{rounded.sm}` (4px), product cards stay at `{rounded.xs}` (2px), and only search pills and classification chips reach `{rounded.full}`. The interface communicates through contrast ratios designed for screen-use in demanding operational environments — not consumer softness, but operator-grade clarity. Product detail pages arrive at `{colors.canvas-light}` (#f6f6f6) to let component photography breathe against a neutral field, while marketing heroes and landing sections stay resolutely in the dark register. The overall effect is a brand that earns authority through visual restraint and precision — a measurement-grade UI surface that happens to also be a commerce and content destination.

colors:
  primary: "#40e09c"
  primary-active: "#26865e"
  primary-disabled: "#a0f0ce"
  thermal-amber: "#f7a840"
  teal-signal: "#37aeb3"
  ink: "#f6f6f6"
  body: "#d1d0ce"
  muted: "#54565b"
  hairline: "#323339"
  canvas: "#080808"
  surface-soft: "#1a1d20"
  surface-card: "#323339"
  on-primary: "#080808"
  mint-soft: "#a0f0ce"
  mint-faint: "#c6f6e1"
  canvas-light: "#f6f6f6"
  ink-on-light: "#080808"
  gray-warm: "#d8d8d8"

typography:
  display-xl:
    fontFamily: "'Industry-Light', 'Industry', sans-serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Industry-Light', 'Industry', sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Industry-Light', 'Industry', sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Museo-Sans', 'museo-sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Museo-Sans', 'museo-sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.6px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.4px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Museo-Sans', 'museo-sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px

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
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-amber:
    backgroundColor: "{colors.thermal-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoWidth: 120px
  mega-menu:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.primary}"
    padding: "{spacing.lg} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageBg: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
    accentColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
  hero-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "{spacing.xxl} {spacing.section}"
  hero-split:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    subtitleTypography: "{typography.body-md}"
    imagePosition: right
    accentColor: "{colors.primary}"
    padding: "{spacing.xxl} {spacing.xl}"
  application-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    accentBar: "3px solid {colors.primary}"
    padding: "{spacing.lg}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    headerBg: "{colors.surface-card}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    rowHoverBg: "{colors.hairline}"
  badge-thermal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  badge-amber:
    backgroundColor: "{colors.thermal-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    iconColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  category-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderActive: "1px solid {colors.primary}"
    textColorActive: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  alert-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.xl}"
  thermal-palette-chip:
    height: 8px
    width: 48px
    rounded: "{rounded.full}"
    gradient: "linear-gradient(to right, {colors.teal-signal}, {colors.primary}, {colors.thermal-amber})"
  footer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    linkColor: "{colors.mint-soft}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.spec-label}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The principal CTA uses #40e09c electric mint fill with #080808 ink, producing luminance contrast that exceeds WCAG AA requirements without any color-inversion tricks. Padding is 12px vertical / 24px horizontal at `{rounded.sm}` (4px), keeping corners crisp enough to read as engineered rather than consumer-friendly. Hover transitions to `{colors.primary-active}` (#26865e), a deep botanical green that communicates state without animation drama. Disabled state uses `{colors.primary-disabled}` (#a0f0ce), the softest mint, which visually recedes while retaining color family membership.

**`button-secondary`** — A transparent ghost with a 1px #40e09c border and matching text, deployed for secondary actions sharing a CTA cluster with `button-primary`. On dark surfaces this resolves cleanly; on `{colors.canvas-light}` pages, the mint border provides sufficient contrast against the neutral field.

**`button-ghost`** — Neutral ghost with `{colors.hairline}` (#323339) border and `{colors.ink}` text. Used for tertiary actions, filter toggles, and utility controls that must not compete with the mint hierarchy.

**`button-amber`** — The amber (#f7a840) reserve CTA for urgency-adjacent actions such as "Request a Quote" or "Contact Sales." Appears at most once per page section so it reads as a thermal-warning signal rather than a decorative variant. Uses `{colors.on-primary}` (#080808) for text, matching the primary button's dark-on-light ink convention.

### Navigation

**`nav-bar`** — A 64px bar on `{colors.canvas}` (#080808) with `{typography.nav-link}` (14px Inter Medium) links and the Teledyne FLIR wordmark at 120px wide. A 1px `{colors.hairline}` border-bottom separates it from the page. Primary nav groups (Products, Solutions, Support, About) open `mega-menu` panels on hover.

**`mega-menu`** — Full-width overlay on `{colors.surface-soft}` (#1a1d20) with a 1px `{colors.primary}` top accent line — the only instance where mint appears as a structural border rather than a fill. Content is organized in 4-column grids with `{typography.spec-label}` section headers (uppercase, 11px, Museo-Sans) and `{typography.body-sm}` link lists below them.

### Product Card

**`product-card`** — Cards sit on `{colors.surface-card}` (#323339) with a 1px `{colors.hairline}` border and `{rounded.xs}` (2px) corners — nearly square, communicating engineering precision rather than consumer warmth. The product image occupies the top 60% of the card on a `{colors.surface-soft}` field. Title in `{typography.title-sm}`, model number or price range in `{typography.caption}`. A mint accent line appears at the bottom edge on hover. Cards on `{colors.canvas-light}` product listing pages invert to `{colors.ink-on-light}` text and a lighter border.

### Hero Sections

**`hero-dark`** — Full-bleed dark heroes use `{colors.canvas}` (#080808) with `{typography.display-xl}` (56px Industry-Light) headlines in `{colors.ink}` and a single `button-primary` CTA. Thermal or sensor product imagery is right-justified, typically with a false-color thermal overlay to establish category context. Minimum height 560px; padding `{spacing.xxl}` vertical and `{spacing.section}` horizontal.

**`hero-split`** — Two-column layout for application-specific landing sections: text left, product imagery right, on `{colors.surface-soft}` (#1a1d20). Uses `{typography.display-md}` (36px Industry-Light) for the headline and `{typography.body-md}` for a 2–3 sentence sub-lead. The `{colors.primary}` accent appears as a short decorative rule between the eyebrow label and headline.

### Application Cards

**`application-card`** — Organizes FLIR's industry vertical navigation (Defense & Security, Industrial Automation, Public Safety, Science & Research, Marine). Each card shows a `{typography.spec-label}` category tag above a `{typography.title-md}` vertical name, anchored by a 3px left border in `{colors.primary}`. Background `{colors.surface-card}`, padding `{spacing.lg}`, corners `{rounded.xs}`.

### Specification Table

**`spec-table`** — Technical spec blocks on product detail pages. Outer container on `{colors.surface-soft}` with `{colors.surface-card}` header rows and `{rounded.sm}` outer corners. Labels use `{typography.spec-label}` (uppercase, 11px Museo-Sans, 0.6px tracking); values use `{typography.body-sm}` (14px Inter). Row hover shifts background to `{colors.hairline}`. Scrolls horizontally on narrow viewports; does not truncate values.

### Badges

**`badge-thermal`** — Pill badges in `{colors.primary}` (#40e09c) fill for "New," "In Stock," and compliance labels (e.g., "NDAA Compliant"). **`badge-amber`** uses `{colors.thermal-amber}` (#f7a840) for urgency markers ("Limited Availability," "Sale"). **`badge-outline`** is a 1px mint border badge for attribute labels (sensor type, wavelength range) that do not need full fill weight. All three share `{typography.badge}` and `{rounded.full}`.

### Search

**`search-bar`** — A `{rounded.full}` pill on `{colors.surface-soft}` with a mint search icon at the leading edge. Width expands from 200px idle to 320px on focus; focus state replaces the `{colors.hairline}` border with a 1px `{colors.primary}` stroke. Appears in the global nav (compact) and on product catalog pages (full-width variant).

### Thermal Palette Chip

**`thermal-palette-chip`** — An 8px-tall, 48px-wide gradient pill running `{colors.teal-signal}` (#37aeb3) → `{colors.primary}` (#40e09c) → `{colors.thermal-amber}` (#f7a840). Used inline in thermal imaging product descriptions and spectral range callouts to visually explain the false-color rendering without a separate legend block. Purely presentational; no interactive states.

### Alert Strip

**`alert-strip`** — A full-width mint bar at `{colors.primary}` fill for site-level announcements (trade show schedules, firmware updates, compliance notices). `{typography.body-sm}` text in `{colors.on-primary}` (#080808). Appears at the very top of the viewport, above `nav-bar`, and collapses on dismiss.

### Footer

**`footer`** — Dark footer on `{colors.surface-card}` (#323339) with `{typography.spec-label}` section headers and `{typography.body-sm}` link lists. Links are `{colors.mint-soft}` (#a0f0ce) at rest, transitioning to `{colors.primary}` on hover. A 1px `{colors.hairline}` top border separates the footer from the page body. Padding `{spacing.xxl}` vertical, `{spacing.xl}` horizontal. Includes subsidiary Teledyne brand lockup and legal/compliance links at the very bottom in `{typography.caption}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; mega-menu becomes a full-screen drawer with accordion sections; hero switches to stacked (headline above image); product grid drops to 1 column; spec-table scrolls horizontally inside a constrained container |
| Tablet | 744–1128px | Nav shows top-level links only (no hover mega-menu; tap to expand accordion drawer); hero-split stays 2-column but reduces padding to `{spacing.xl}`; product grid is 2 columns; application cards are 2×2 grid |
| Desktop | 1128–1440px | Full mega-menu on hover; hero-dark at full 560px min-height; product grid 3–4 columns; spec-table fully visible without scroll |
| Wide | > 1440px | Content max-width 1440px centered; hero imagery scales proportionally; hero-dark may use background video loop for thermal product demos |

### Touch Targets

- All buttons minimum 44px height as defined in component specs
- Category pills and nav links receive padding inflation to 44px tap target even when visual height appears shorter
- Product card tap target spans the entire card surface, not just the title text
- Search bar closes on outside tap; surfaces system keyboard with search return key bound

### Collapsing Strategy

- Global nav hamburger-first; mega-menu becomes a full-height left drawer with accordion-collapsed subsections on mobile
- Product filter sidebar collapses to a bottom sheet or modal drawer below 744px
- Spec-table switches to stacked definition-list format (label above value) below 560px when horizontal scroll would require 3+ swipes to read a single row
- Application-card grid goes from 4-up → 2-up → 1-up as viewport narrows
- Thermal palette chip stays visible at all breakpoints at its fixed 48px × 8px size

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No cart, checkout, or account UI colors were extractable — FLIR may route direct purchase through distributor links or a separate e-commerce portal rather than an on-site storefront
- Exact nav height and mega-menu animation timing (duration, easing) not confirmed; 64px height is inferred from standard B2B nav conventions
- Dark-mode vs. system-preference behavior unclear — site may be dark-only or toggle via `prefers-color-scheme`; no `meta theme-color` was present to hint at either
- Museo-Sans weight variants actually in use could not be confirmed; `spec-label` weight 700 is inferred from the family's standard Bold offering
- Industry-Light specific metrics (x-height ratio, optical size behavior) are not measurable from extraction; display sizes are estimated from visual conventions for technical brand display type
- Several extracted colors match Bootstrap 5 framework defaults (#198754, #0dcaf0, #d63384, #0d6efd, #6610f2, #6f42c1, #fd7e14, #20c997) and were excluded from the brand palette as likely framework noise rather than brand decisions
- The role of #d9d803 (yellow-green) and #ed6b70 (salmon) in the extracted palette is unclear — possibly product status indicators or UI state colors in a dashboard-adjacent context not reached by the surface scrape
- Motion and animation specs (hover transition durations, scroll-triggered reveals, thermal scan animation on hero) are not derivable from static extraction
- Print and PDF stylesheet behavior for spec sheets is unconfirmed
