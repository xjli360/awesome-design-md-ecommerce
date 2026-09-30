---
version: alpha
name: "Sentai Filmworks"
source_url: "https://www.sentaifilmworks.com"
captured_at: "2026-09-29T04:22:41.261186+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The captured evidence for sentaifilmworks.com consists almost entirely of the
  unmodified Bootstrap 4.3.1 framework stylesheet: its CSS custom-property
  palette (blue, indigo, purple, pink, red, orange, yellow, green, teal, cyan,
  grays) and its default system font stack. No brand-authored color tokens or
  custom component selectors were present in the supplied rules, so every
  color below is a reused Bootstrap default rather than a confirmed brand
  hue; roles (primary action, ink, canvas, hairline, etc.) are inferred from
  Bootstrap's own semantic variable names, not from observed rendered
  screenshots. Two font families outside the default Bootstrap stack —
  Montserrat and Roboto — appear in the page's computed font list, so this
  spec assigns Montserrat to display/heading roles and the system stack
  (matching Bootstrap's default) to body copy; this pairing is inferred, not
  verified against live rendering.
  The interpretation targets an anime media storefront: a clean white canvas,
  dark neutral ink text, Bootstrap-blue calls to action, and status colors
  (danger/success/warning/info) repurposed for stock, pre-order, and sale
  badges. Layout proportions, spacing scale, and radii are proposed
  conventions sized to Bootstrap's own .25rem control radius, not measured
  from the live site.

colors:
  primary: "#007bff"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#212529"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  secondary: "#6c757d"
  dark: "#343a40"
  success: "#28a745"
  danger: "#dc3545"
  warning: "#ffc107"
  info: "#17a2b8"
  focus-ring: "#80bdff"
typography:
  display-xl: {fontFamily: "Montserrat, -apple-system, BlinkMacSystemFont, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, -apple-system, BlinkMacSystemFont, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, -apple-system, BlinkMacSystemFont, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.25px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    focusRing: "2px solid {colors.focus-ring}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
  streaming-promo-banner:
    backgroundColor: "{colors.info}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"

## Components

**button-primary** is the default call-to-action treatment (Add to Cart, Subscribe, Checkout), using the Bootstrap-blue primary token against white text; corner radius follows Bootstrap's own `.25rem` control default. Hover/active state darkening is proposed, not observed.

**button-secondary** offers an outlined variant for lower-priority actions (e.g. "View Catalog"), sharing the primary hue as border/text color on a white fill; this pairing is a proposed convention, not confirmed from captured CSS.

**text-input** covers newsletter and search fields, with a light hairline border and a proposed focus ring using the Bootstrap `focus-ring` blue-tint token; disabled/error states are not observed.

**nav-bar** is a proposed sticky/static header shell in white with an ink wordmark/links and a bottom hairline; the site is known to include a mega-menu ("Shop", "Discover", "Catalog") per the page text, but its rendered layout is not observed.

**product-card** models Blu-ray/merch tiles with a hairline-bordered white card, image area, title in Montserrat, and price in body copy; badge overlays (Pre-Order, Limited Edition) use the badge component. Grid arrangement is proposed.

**hero** proposes a dark full-bleed banner (using the Bootstrap dark-gray token) for the streaming/theatrical announcements seen in the page text ("Ninja Scroll in 4K", HIDIVE titles), with large display type in white; this is a layout inference, not a captured screenshot.

**footer** groups the observed link set (About, Careers, Terms, Privacy, Cookies, Store Policy, FAQ, Contact, Accessibility) plus social icons on a dark background, matching the "Expand Footer Menu" text found in evidence; exact column layout is proposed.

**badge** is a small pill label repurposed from Bootstrap's danger/warning/success tokens to flag Pre-Order, Sale, or New Release status on product tiles — an inferred merchandising pattern common to e-commerce, not confirmed in the CSS.

**search** proposes a light-gray search field styled consistent with the surface-soft token, used for the catalog/product search implied by "Discover Catalog" in the page text.

**streaming-promo-banner** is the category-specific component for this Movies & TV brand: a slim, full-width strip using the info/cyan token to surface the rotating HIDIVE streaming callouts ("Stream ... on HIDIVE") visible in the page text; dismissal/carousel behavior is proposed, not observed.

## Responsive Behavior

Recommended, not measured, breakpoints (aligned to Bootstrap 4's defaults present in the evidence):

| Breakpoint | Width | Behavior (proposed) |
|---|---|---|
| xs | <576px | Single-column product grid; nav collapses to hamburger; promo banner stacks above hero |
| sm | ≥576px | 2-column product grid; search field full-width |
| md | ≥768px | 3-column product grid; nav-bar shows inline primary links |
| lg | ≥992px | 4-column product grid; footer expands to multi-column |
| xl | ≥1200px | Max-width content container; hero uses full display-xl scale |

Touch targets should be at least 44×44px for cart/nav controls; the nav-bar should collapse into a slide-in or accordion menu below `md`. None of this is measured from live responsive behavior of sentaifilmworks.com.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static extraction returned framework (Bootstrap 4.3.1) default variables and font stacks; no brand-authored selectors, hex values, or component classes specific to Sentai Filmworks were present in the supplied CSS, so the palette above is a reused default set, not confirmed brand identity color.
- Montserrat/Roboto usage is inferred from their appearance in the page's computed font list; no selector tying them to specific headings or body text was supplied.
- All typographic sizes, weights, letter-spacing, radii, and spacing values are proposed design conventions, not measurements from rendered pages.
- No interaction states (hover, focus, active, disabled), mobile menu behavior, or cart-drawer layout were observed; all such details in this spec are labeled proposed.
- Font licensing/self-hosting status for Montserrat/Roboto was not verified; assume Google Fonts or system availability unless confirmed otherwise.
- Grid column counts, hero imagery, and footer column arrangement are inferred from page text (link labels, promo copy) rather than visual layout capture.
