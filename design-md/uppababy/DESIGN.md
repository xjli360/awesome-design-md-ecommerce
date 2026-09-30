---
version: alpha
name: "UPPAbaby"
source_url: "https://uppababy.com"
captured_at: "2026-09-28T04:52:28.112334+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is grounded in CSS captured from the UPPAbaby homepage, a strollers-and-car-seats
  storefront. The observed palette is dominated by a near-black ink (#0f0c0a) paired with an off-white
  (#f7f7f7), used consistently as the two-tone button system across hero, banner, and content-block
  components: filled dark-on-light by default, inverting to outline on hover/active. Supporting neutrals
  (#ffffff, #e4e4e4, #efefef, #8f8f8f) suggest a light, editorial canvas typical of a premium baby-gear
  brand. A wider secondary set — blues (#0a629c, #61baf5, #6c92ab), a tan (#d2c4b2), reds (#861212,
  #ce0000, #e76569), a green (#045f20), and warm golds (#ffbd5d, #ffbb37) — appears only in isolated
  hex values without confirmed selectors; these are treated here as inferred accent, badge, and status
  colors rather than confirmed brand hues.
  Two custom display faces, "gelica" and "agenda," are confirmed in heading selectors (hero captions,
  block h1/h2), both falling back to sans-serif; body, button, and form elements rely on an inherited
  system-font stack (system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial). The design
  system below proposes a calm, high-contrast e-commerce layout: bold pill buttons, generous whitespace,
  card-based category and resource tiles, and a warranty/trust-forward footer — reflecting the brand's
  emphasis on safety, registration, and long-term product support found in the page text.

colors:
  primary: "#0f0c0a"
  ink: "#0f0c0a"
  canvas: "#ffffff"
  body: "#202020"
  muted: "#8f8f8f"
  hairline: "#e4e4e4"
  surface-soft: "#f7f7f7"
  surface-card: "#efefef"
  on-primary: "#f7f7f7"
  border-strong: "#c5c5c5"
  accent-blue: "#0a629c"
  accent-sky: "#61baf5"
  accent-red: "#861212"
  accent-coral: "#e76569"
  accent-gold: "#ffbd5d"
  accent-tan: "#d2c4b2"
  accent-green: "#045f20"
  overlay-dark: "#00000099"
typography:
  display-xl: {fontFamily: "gelica, agenda, sans-serif", fontSize: 40px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.5px}
  display-md: {fontFamily: "gelica, agenda, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  title-md: {fontFamily: "agenda, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    overlay: "{colors.overlay-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    mutedTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.md}"
  resource-tile:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    accentColor: "{colors.accent-blue}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"

## Components

**button-primary** reflects the confirmed dark-fill pill button (border-radius 2rem, `#0f0c0a` background, `#f7f7f7` text) used in the hero video caption and content blocks, with an observed hover state that inverts to a transparent/outline treatment.

**button-secondary** mirrors the inverse variant seen on light-background blocks (`.dbl_column` first-column buttons): light fill, dark text and border, with hover flipping to transparent fill and light text — proposed here as the standard secondary action for use on dark or image-heavy sections.

**text-input** is proposed for the newsletter email field referenced in the footer copy ("email ... Submit"); no dedicated input CSS was supplied, so border, radius, and padding are inferred from the broader neutral/hairline palette.

**nav-bar** represents the top utility and category navigation implied by the page text (free-shipping ribbon, Strollers/Car Seats/Travel Systems/At-Home/Accessories/New links, search, account, and mini-cart controls). Exact spacing and collapse behavior are not present in the CSS and are proposed.

**product-card** is a proposed pattern for category and product grids (e.g., stroller/car-seat listings), using the light surface-card neutral and hairline border observed elsewhere in the palette; no explicit card selector was supplied.

**hero** models the confirmed `.refresh_video` banner: full-bleed video/image background, dark overlay, gelica/agenda display headline, and a pill CTA button with a verified hover color-swap.

**footer** is inferred from the extensive footer link text (Our Company, Support, Registry, Media, Contact) and uses the dark ink background with light text, consistent with the confirmed dark-button color pairing found elsewhere on the page.

**badge** is a proposed small pill label (e.g., "New Arrival," "TravelSafe") using one of the unconfirmed warm accent hues (`#ffbd5d`); no badge selector was present in the supplied CSS, so this is a stylistic proposal only.

**search** and **resource-tile** are proposed components: search reflects the aria-labeled search button/field referenced in the page text, and resource-tile models the "Stroller Comparison / Car Seat Center / Warranty Program" three-up layout described in the content, styled with the confirmed hairline and accent-blue tones.

## Responsive Behavior

This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| Mobile | 0–599px | Single-column stack; nav collapses to hamburger + icon row; hero CTA full-width |
| Tablet | 600–1023px | 2-column product/resource grids; nav shows primary categories inline |
| Desktop | 1024–1439px | 3–4 column grids; full nav bar with search/account/cart visible |
| Wide | 1440px+ | Max content width constrained; hero imagery scales, side margins increase |

Touch targets should be at least 44×44px for nav icons, cart, and buttons. Primary/secondary buttons should retain the pill shape and hover-invert treatment across breakpoints. Mobile nav collapse and drawer/mini-cart behavior are proposed conventions, not confirmed from the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.




- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted from static CSS/text of the homepage only; no rendered layout, computed styles, or DOM structure was observed.
- Many supplied hex values (blues, reds, greens, golds, tan) have no associated selector context, so their semantic roles (badge, alert, success, category tagging) are inferred, not confirmed.
- Body, input, and button font sizes/weights are proposed; only two heading font families (gelica, agenda) and two heading font sizes (2rem, 2.5rem) were directly observed in the CSS.
- Component states beyond the confirmed button hover/active pairs (e.g., focus rings, disabled states, form validation) are proposed and unverified.
- Mobile/tablet layout, navigation collapse pattern, and touch interaction were not present in the supplied evidence and are recommendations only.
- Availability, licensing, and hosting terms for "gelica" and "agenda" were not verified; treat as brand-supplied custom fonts pending confirmation.
