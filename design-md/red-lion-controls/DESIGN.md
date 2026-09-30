---
version: alpha
name: "Red Lion Controls"
source_url: "https://www.redlion.net"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Two blues — a signal-clear medium #1268b3 and a pressure-vessel navy #043d5d — do nearly all the chromatic work on a canvas that is otherwise white and cool gray. That restraint is deliberate: Red Lion makes the hardware that reads temperatures inside industrial furnaces and relays data across factory floors, and the website mirrors that operational honesty. Nothing competes for attention except the information itself. Industry, a typeface built for bold condensed rendering, carries every display headline; it has the same visual register as panel labels on PLCs — dense, readable at a distance, zero ornament. Lato runs body copy, spec tables, and form labels with the neutral fluency that keeps long product pages scannable without visual fatigue. Rounded corners are minimal: cards sit at a 4–8px radius, buttons at 4px, and nothing approaches a pill — this is not a consumer brand trying to feel soft. The primary action color is the brighter #1268b3 on white, while #043d5d surfaces as hover states, header fills, and footer backgrounds, giving depth without introducing a third hue. Component density is high: product cards carry part numbers, protocol badges, and download links inside a compact 240–280px column. Hero sections layer a dark navy overlay over industrial photography, with white display type set in Industry Bold and a single {colors.primary} CTA button as the only warm accent. The information architecture favors engineers: navigation groups by product family (Controllers, Monitors, Networking, Software), not by use case or vertical. Search is prominent and always visible in the top bar because the primary user journey is "I need part number X" not "let me browse." Data tables, spec sheets, and firmware download links are treated as first-class UI elements rather than afterthoughts hidden in a support section.

colors:
  primary: "#1268b3"
  primary-active: "#0d57a0"
  primary-disabled: "#8ab8de"
  primary-hover: "#1172c4"
  navy: "#043d5d"
  navy-active: "#032f48"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d4d8dd"
  hairline-soft: "#eaecef"
  canvas: "#ffffff"
  surface-soft: "#f4f6f8"
  surface-card: "#ffffff"
  surface-dark: "#043d5d"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  alert-warning: "#f59e0b"
  alert-error: "#dc2626"
  alert-success: "#16a34a"
  protocol-badge-bg: "#e8f0f9"
  protocol-badge-text: "#1268b3"

typography:
  display-xl:
    fontFamily: "'Industry', 'Lato', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Industry', 'Lato', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Industry', 'Lato', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Industry', 'Lato', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Lato', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  part-number:
    fontFamily: "'Lato', monospace, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Lato', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lato', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  badge-label:
    fontFamily: "'Lato', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Lato', sans-serif"
    fontSize: 13px
    fontWeight: 700
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
    padding: 12px 24px
    height: 44px
    hoverBackgroundColor: "{colors.primary-hover}"
    activeBackgroundColor: "{colors.primary-active}"
    disabledBackgroundColor: "{colors.primary-disabled}"

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 2px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
    hoverBackgroundColor: "{colors.surface-soft}"

  button-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    hoverBackgroundColor: "{colors.navy-active}"

  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    borderColor: "{colors.on-dark}"
    borderWidth: 1px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px

  button-sm-link:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: 10px 12px
    height: 44px
    focusBorderColor: "{colors.primary}"
    focusOutline: "2px solid {colors.primary}"
    focusOutlineOffset: 0px

  nav-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    padding: 0 32px
    logoHeight: 36px
    dropdownBackgroundColor: "{colors.canvas}"
    dropdownTextColor: "{colors.ink}"
    dropdownBorderTop: "3px solid {colors.primary}"

  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    height: 40px
    submitButtonBackgroundColor: "{colors.primary}"
    submitButtonTextColor: "{colors.on-primary}"
    submitButtonRounded: "{rounded.none}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    imageHeight: 180px
    imageBackgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    partNumberTypography: "{typography.part-number}"
    partNumberColor: "{colors.muted}"
    hoverBorderColor: "{colors.primary}"
    hoverShadow: "0 2px 8px rgba(18,104,179,0.12)"

  hero-banner:
    backgroundColor: "{colors.navy}"
    overlayColor: "rgba(4,61,93,0.75)"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    minHeight: 480px
    padding: "80px 64px"

  protocol-badge:
    backgroundColor: "{colors.protocol-badge-bg}"
    textColor: "{colors.protocol-badge-text}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    borderColor: "{colors.primary}"
    borderWidth: 1px

  spec-table:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.none}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.body}"
    rowAlternateBackgroundColor: "{colors.surface-soft}"
    padding: "10px 16px"

  download-cta:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    iconColor: "{colors.primary}"
    labelTypography: "{typography.caption-bold}"
    labelColor: "{colors.ink}"
    subtextTypography: "{typography.caption}"
    subtextColor: "{colors.muted}"

  section-header:
    backgroundColor: "{colors.surface-soft}"
    borderBottom: "3px solid {colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    padding: "20px 32px"

  alert-banner:
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "12px 16px"
    warning-backgroundColor: "#fffbeb"
    warning-borderColor: "{colors.alert-warning}"
    warning-textColor: "#92400e"
    error-backgroundColor: "#fef2f2"
    error-borderColor: "{colors.alert-error}"
    error-textColor: "#991b1b"
    success-backgroundColor: "#f0fdf4"
    success-borderColor: "{colors.alert-success}"
    success-textColor: "#14532d"

  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    linkColor: "#93c5e8"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    padding: "48px 64px 32px"
    borderTop: "4px solid {colors.primary}"

  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
    hoverColor: "{colors.primary}"

---

## Components

### Buttons

**`button-primary`** — The workhorse CTA: #1268b3 fill, white uppercase Lato Bold text at 15px with 0.3px tracking, 4px radius. Hover steps to a slightly lighter `{colors.primary-hover}`, active compresses to `{colors.primary-active}`. Disabled state uses `{colors.primary-disabled}`, a washed medium blue, keeping the shape readable without implying availability.

**`button-secondary`** — White fill with a 2px `{colors.primary}` border and matching text color. Used for secondary actions on light backgrounds — "View Datasheet," "Compare Products." Hover tints background to `{colors.surface-soft}` to signal interactivity without the full primary weight.

**`button-navy`** — Dark `{colors.navy}` fill with white text; used when a CTA sits on a light canvas section and needs heavier visual presence than primary blue, or when secondary hierarchy demands contrast from primary CTAs on the same page.

**`button-ghost`** — Transparent background, white border and text, used exclusively on dark hero/navy sections where a secondary action must be visible against the dark overlay without competing with the primary blue CTA.

### Navigation

**`nav-bar`** — 60px tall, `{colors.navy}` (#043d5d) background, white Lato Bold 14px links. Dropdowns open with a 3px `{colors.primary}` top border accent and white background, creating a strong signal that industrial-level information architecture has been entered. Logo sits at 36px height left-aligned; search bar floats right.

**`search-bar`** — Always visible in the nav bar. White input, flat `{rounded.none}` submit button in `{colors.primary}` to marry cleanly to the input. This is the highest-frequency interaction for engineers looking up part numbers or protocol compatibility.

### Product Cards

**`product-card`** — 1px `{colors.hairline}` border, 4px radius, white background. Product image renders on a `{colors.surface-soft}` tray at 180px height. Part number displays in `{typography.part-number}` — monospaced caps, 12px, muted — beneath the product title. Protocol badges (`protocol-badge`) stack horizontally below the part number. Hover state adds a `{colors.primary}` border and a subtle blue-tinted drop shadow.

**`protocol-badge`** — Small inline tag in `{colors.protocol-badge-bg}` with a 1px `{colors.primary}` border and blue text. Communicates supported protocols (EtherNet/IP, Modbus, PROFINET) at a glance — this is a primary filtering signal for industrial buyers comparing devices.

### Content Sections

**`hero-banner`** — Navy `{colors.navy}` background with a semi-opaque overlay (rgba 0.75) on industrial photography. `{typography.display-xl}` headline in Industry Bold, white; body in Lato 16px white. Single `button-primary` CTA sits below. Minimum 480px height. The opacity overlay preserves photography context while guaranteeing text contrast at WCAG AA without requiring dark-text-on-dark alternatives.

**`spec-table`** — No-radius table with 1px `{colors.hairline}` borders. Header row uses `{colors.surface-soft}` background with `{typography.spec-label}` (Lato Bold 13px). Alternating rows use surface-soft for scanability across 20–40 row spec sheets. This is where engineers spend most of their time — the design prioritizes density and legibility over visual interest.

**`section-header`** — Light `{colors.surface-soft}` background with a 3px bottom border in `{colors.primary}`. `{typography.display-sm}` title in Industry 22px. Visually anchors major page sections (Product Family, Resources, Related Products) with the brand blue accent line without consuming vertical space.

**`download-cta`** — Compact card for firmware files, datasheets, and software downloads. `{colors.surface-soft}` background, primary-colored icon, bold caption label, and a muted file-size/date subtext. Treated as a first-class feature rather than a sidebar link, reflecting that downloads are a core user journey for Red Lion's engineering audience.

**`alert-banner`** — Three variants (warning amber, error red, success green) with matching soft background tints. Used for product discontinuation notices, firmware advisories, and stock availability warnings. Typography is `{typography.body-sm}` to keep density high; rounded at `{rounded.xs}` to match the site's restrained corner language.

**`footer`** — `{colors.navy}` background with a 4px `{colors.primary}` top accent stripe. Four-column link grid in Lato, white headings, `#93c5e8` link color (a desaturated blue that reads on dark without glowing). Full-width at all breakpoints.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; search bar moves below nav strip; product cards stack single-column; hero text drops to `{typography.display-md}`; spec tables scroll horizontally |
| Tablet | 744–1128px | Nav shows top-level items only, dropdowns preserved; product cards 2-column grid; hero at 380px height; section headers maintain full width |
| Desktop | 1128–1440px | Full nav with dropdown mega-menus; product cards 3–4 column grid; hero at 480px; spec tables full-width with fixed first column |
| Wide | > 1440px | Content constrained to ~1400px max-width centered; hero extends edge-to-edge behind content container; footer columns expand to 5 |

### Touch Targets

- All buttons minimum 44px height on mobile
- Nav hamburger icon target: 48×48px tap zone
- Protocol badges are display-only below tablet; on mobile, tap product card to see full spec page
- Download CTA rows expand to full-width on mobile with 16px vertical padding for safe tapping

### Collapsing Strategy

- Mega-menu nav collapses to a full-screen drawer on mobile; product family categories listed vertically with expand/collapse chevrons
- Spec tables use horizontal scroll with a sticky first column (parameter name) to preserve context on narrow screens
- Hero photography drops behind a stronger overlay on mobile where viewport height constrains image area
- Footer collapses from 4-column to 2-column at tablet, single-column at mobile; legal links move below fold

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only two brand hex colors were extracted (#1268b3, #043d5d); all neutral grays, surface colors, and semantic alert colors are derived from brand context rather than extracted from live CSS
- No meta theme-color was set, so mobile browser chrome color is unconfirmed
- The "Industry" typeface is a third-party commercial font (Monotype); exact weights used for body vs display were not confirmed from extraction — Lato fallback behavior is an assumption
- Exact button corner radius not confirmed from extraction; 4px is inferred from industrial-brand convention
- No extracted hover or focus state colors; all interactive states are derived from the primary/navy pair
- Dropdown and mega-menu visual structure not confirmed; described from category-page observation
- No confirmed dark mode or high-contrast accessibility mode detected
