---
version: alpha
name: "Koch-Chemie"
source_url: "https://koch-chemie.com"
captured_at: "2026-09-28T10:01:27.307933+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Koch-Chemie's public site exposes a Bootstrap-derived design system layered with a single branded accent. The measured palette centers on a cyan-blue primary (#009FDA), paired with near-black ink (#1E1E1E) on white canvas, and a neutral grey (#919396) used as Bootstrap's "light" token. Bootstrap's full status-color ramp (success, danger, warning, info, secondary) is present in the CSS, suggesting these are retained for form validation, alerts, and admin-style UI rather than core brand expression. Typography uses "HelveticaNowDisplay" with Arial and sans-serif fallbacks, a clean, technical sans consistent with an industrial/professional chemical manufacturer rather than a lifestyle retailer.
  This interpretation treats #009FDA as the primary action color, #1E1E1E as body/ink, and white as the dominant canvas, with light greys (#f4f5f5, #ececec, #e6e6e6) inferred as soft surface and hairline tones for card separation and section banding, since no explicit surface tokens were supplied. Rounded corners follow the observed .25rem button radius. All sizing beyond the literal .btn padding and border-radius is proposed, scaled to a professional B2B/B2C hybrid catalog (product cards, spec sheets, dealer locator) rather than measured from live layout.

colors:
  primary: "#009fda"
  ink: "#1e1e1e"
  canvas: "#ffffff"
  body: "#1e1e1e"
  muted: "#919396"
  hairline: "#e6e6e6"
  surface-soft: "#f4f5f5"
  surface-card: "#ececec"
  on-primary: "#ffffff"
  secondary: "#6c757d"
  primary-hover: "#0083b4"
  primary-active: "#007aa7"
  primary-deep: "#00678e"
  primary-tint: "#8ee0ff"
  success: "#28a745"
  danger: "#dc3545"
  warning: "#ffc107"
  info: "#17a2b8"
  hairline-strong: "#cccccc"
typography:
  display-xl: {fontFamily: "HelveticaNowDisplay, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "HelveticaNowDisplay, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "HelveticaNowDisplay, Arial, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "HelveticaNowDisplay, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-sm: {fontFamily: "HelveticaNowDisplay, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "HelveticaNowDisplay, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "HelveticaNowDisplay, Arial, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.4, letterSpacing: 0px}
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
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    overlayColor: "{colors.primary-deep}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.primary-tint}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-sheet-card:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline-strong}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"

## Components

**button-primary** is the core call-to-action, using the branded cyan (#009FDA) with white text, matching the observed `.btn-primary` rule set including its 4px radius. Hover/active darkening (#0083b4 / #007aa7) is observed in CSS and should be preserved in implementation.

**button-secondary** uses Bootstrap's grey (#6c757d) for lower-emphasis actions such as "Learn more" links or filter toggles; hover states are proposed to follow the same darkening pattern seen on `.btn-secondary`.

**text-input** is a proposed pattern for search and contact/dealer-locator forms. No live input styling was supplied, so border, padding, and radius are inferred from the button radius and neutral hairline palette.

**nav-bar** represents the top-level "Products & Brands / Company / Competence / Career / Contact" navigation implied by page text. Layout, sticky behavior, and dropdown mechanics are not observed and are proposed as a light, white-background bar with dark text.

**product-card** supports listings for the Automotive, Marine, COLOURLOCK, and Industrial brand tiles referenced in the content. Card surface, radius, and spacing are proposed; no card CSS was directly supplied.

**hero** models the homepage banner ("Protection Unit. Three Specialists. One Mission.") as a dark, full-bleed section with large display type, since large-scale hero typography was not directly measured.

**footer** covers the region-selector and legal-link footer (Privacy Policy, Imprint, Terms of Service) implied by the text excerpt; dark background with light text is proposed to contrast the light body, not confirmed by CSS.

**badge** is a proposed small label component for tagging new products (e.g., "New Products," "Ceramic Neo") using the primary color pill pattern, unobserved in supplied CSS.

**search** models the header search icon/field referenced in page text ("Search"), styled as a soft, low-contrast field consistent with the neutral surface tones.

**spec-sheet-card** is a category-specific proposed component for the "Data Sheets" / technical documentation area typical of a chemical manufacturer, using muted surface and caption/body-sm typography for label-value pairs (e.g., dilution ratios, pH).

## Responsive Behavior

This is a recommendation based on Bootstrap breakpoint variables found in `:root` (xs:0, sm:576px, md:768px, lg:992px, xl:1200px), not measured live behavior.

| Breakpoint | Width | Layout guidance |
|---|---|---|
| xs | 0–575px | Single-column stack; nav collapses to hamburger/menu drawer |
| sm | 576–767px | Two-column product grids begin; larger touch targets |
| md | 768–991px | Nav bar expands inline; 2–3 column product/brand cards |
| lg | 992–1199px | Full desktop nav; 3–4 column grids; hero at full scale |
| xl | 1200px+ | Max-width container centers content; spacing.section applied generously |

Touch targets should be at least 44×44px for primary and secondary buttons on mobile. Navigation and any multi-region/language selector (noted in page text: Great Britain, Germany, USA, etc.) should collapse into an accordion or modal below the `md` breakpoint. None of this collapse/interaction behavior was directly observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered page, DOM interactions, or viewport testing was performed. Semantic role mapping for surface, hairline, and card colors is inferred from Bootstrap grey-scale conventions, not confirmed brand tokens. The `body` font-size value (1.4375rem) in source CSS appears unusually large and may depend on an unlisted root font-size rescale; body-md/sm sizes here are proposed 16px/14px defaults rather than the literal computed value. Spacing scale, rounded-corner sizes beyond the observed 4px button radius, hero/footer layout, card structure, and all hover/focus/active states beyond the explicitly supplied `.btn-primary`/`.btn-secondary`/`.btn-success` rules are proposed, not observed. Mobile navigation collapse, language/region switcher behavior, and product-grid responsive breakpoints are inferred from generic Bootstrap conventions, not measured. Availability, licensing, and web-font-loading behavior of "HelveticaNowDisplay" were not verified from the supplied evidence.
