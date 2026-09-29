---
version: alpha
name: "Bullfrog Spas"
source_url: "https://www.bullfrogspas.com"
captured_at: "2026-09-28T04:41:16.047470+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation draws from Bullfrog Spas' WordPress/Elementor storefront, where the observed
  palette centers on a saturated blue (#406de1, #579af6, #4386e2) used for links, active-language
  states, and Elementor global accents, paired with neutral grays (#444444, #666666, #999999) for
  body copy and a white (#ffffff) canvas. A soft blue-gray (#ecf0f5) and light gray (#eeeeee) appear
  in the palette and are inferred as card/panel surfaces, while #e5e5e5 and #cccccc read as hairline
  and border tones. An orange (#ff6900) and a supporting slate (#3f4b5b) are present in the palette
  and are treated as secondary accent options for promotional or CTA use, since no CSS rule confirms
  their exact application. Typography combines Montserrat (display/heading candidate) with Open Sans
  (body candidate) and Arial/sans-serif fallbacks; no proprietary or licensed font behavior is
  confirmed. Layout patterns (mega-menu navigation, spa-series comparison grid, JetPak feature
  cards, store-locator CTA) are inferred from page-text structure, not from measured DOM/CSS layout.
  All spacing, radius, and component sizing values below are proposed defaults suited to a
  premium outdoor-living/hot-tub retailer and are explicitly not claimed as observed measurements.

colors:
  primary: "#406de1"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#444444"
  muted: "#666666"
  hairline: "#e5e5e5"
  surface-soft: "#eeeeee"
  surface-card: "#ecf0f5"
  on-primary: "#ffffff"
  accent: "#ff6900"
  link: "#579af6"
  border: "#cccccc"
  border-strong: "#bfc3c8"
  slate: "#3f4b5b"
  success: "#468847"
  warning: "#f0ad4e"
  error: "#cf2e2e"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  none: 0px
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.border}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.slate}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.slate}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.link}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  jetpak-selector-tile:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.caption}"

## Components

**button-primary** is proposed as the primary conversion action (e.g., "Design My Spa," "Get an Instant Price Quote"), using the observed blue (#406de1) fill with white text; hover/active states are not observed and are proposed as a darkened or opacity-shifted variant.

**button-secondary** offers an outlined alternative for lower-priority actions like "Find a Store" links, reusing the primary blue as border/text color on a transparent background; this pairing is inferred from typical retailer patterns, not from a captured hover state.

**text-input** covers search and quote-form fields, using a light border and white background consistent with the neutral palette; focus-ring styling is not observed and is proposed only.

**nav-bar** models the top utility/mega-menu bar referenced in the page text (Store Locations, Support, language switcher). A white background with a hairline bottom border is inferred from the light overall palette; the mega-menu's actual open/active states (e.g., #9dc5e5 hover noted in French-locale CSS) suggest link-hover color shifts toward a lighter blue, which is reflected in the `link` token.

**product-card** represents a spa-series or JetPak listing tile (M Series, A Series, X Series, etc.), using the soft blue-gray surface tone for differentiation from the white page background; card elevation/shadow is not observed and is intentionally omitted.

**hero** models the top-of-page "A More Peaceful Life" banner, using the dark slate tone as an inferred background for a photographic hero overlay, since no explicit hero background color was captured in the CSS evidence — this is a proposed treatment for contrast against large imagery.

**footer** reuses the slate tone with white text and blue links, consistent with common dark-footer patterns; actual footer background was not directly observed in the supplied CSS and is therefore a proposed mapping.

**badge** is proposed for labels such as "New," "Best Seller," or JetPak jet-count indicators, using the orange accent color present in the palette; no confirmed badge usage was found in the evidence, so this is speculative but visually consistent.

**search** models the header search field ("Search …"), using a light gray surface consistent with the palette's #eeeeee tone.

**jetpak-selector-tile** is a category-specific component for the JetPak Therapy System comparison grid described in the page text (Gyrossage, Alleviate, DeepRelief, etc.), presenting jet count, jet type, and target-area metadata in a compact card; this structure is inferred entirely from the textual content, not from captured grid CSS.

## Responsive Behavior

The following breakpoint table is a **recommendation only**; no responsive CSS or media-query evidence was supplied.

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| mobile    | < 480px     | Single-column stacking; nav collapses to a hamburger/off-canvas menu |
| tablet    | 480–1024px  | 2-column product/JetPak grid; sticky header may condense |
| desktop   | 1024–1440px | Full mega-menu with dropdown panels; 3–4 column grids |
| wide      | > 1440px    | Max content width with increased side padding |

Touch targets should be at least 44×44px for primary buttons and nav items (proposed, not measured). The mega-menu should collapse into an accordion or drawer pattern below tablet width; language switcher and utility links likely relocate into a secondary mobile menu. None of this collapse behavior was directly observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS/text extraction does not confirm actual rendered layout, grid structure, or component boundaries; all component shapes above are inferred from page text and partial selector fragments.
- Color-role assignments (e.g., slate for hero/footer, accent orange for badges) are semantic inferences based on palette presence, not confirmed usage in captured rules.
- No hover, focus, active, or disabled states were observed for buttons, links, or form inputs; all such states are proposed.
- No responsive/media-query CSS was present in the supplied evidence; the breakpoint table is a design recommendation, not measured behavior.
- Font availability, licensing, and exact weight/style variants for Montserrat and Open Sans were not verified from the supplied evidence.
- Spacing and corner-radius scales are proposed defaults appropriate to the category and are not derived from measured site values.
- Mobile navigation, menu-collapse mechanics, and touch interaction patterns were not observed and are speculative.
