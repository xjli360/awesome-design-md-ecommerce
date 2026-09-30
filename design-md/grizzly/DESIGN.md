---
version: alpha
name: "Grizzly"
source_url: "https://grizzly.com"
captured_at: "2026-09-29T04:06:39.541508+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Grizzly Industrial's storefront runs on a Bootstrap-derived foundation: the CSS custom
  properties expose the stock Bootstrap ramp (--primary:#007bff, --secondary:#6c757d,
  --success:#28a745, --danger:#dc3545, --warning:#ffc107, --info:#17a2b8) alongside
  Bootstrap's neutral grays (#f8f9fa, #e9ecef, #dee2e6, #343a40, #212529). Body text and
  base typography are set from the system font stack (-apple-system, Segoe UI, Roboto,
  Helvetica Neue, Arial) at 1rem/1.5 line-height/400 weight, confirmed directly from the
  body selector. A second font token, proxima-nova, appears in the supplied family list
  and is treated here as an inferred display/heading face, since no selector evidence ties
  it to a specific element. Additional palette entries such as #ec1f27, #ae0101, #149547,
  and #1e94b6 fall outside the Bootstrap defaults and are interpreted as brand/utility
  accent colors (e.g., alerts, stock badges, promotional callouts) rather than confirmed
  UI roles. The resulting interpretation favors a dense, catalog-driven industrial
  storefront: flat surfaces, restrained radii (Bootstrap's .25rem default), and a
  Bootstrap-blue primary action color, with red/green accents reserved for status and
  inventory signaling common to machinery retail.

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
  accent-red: "#ec1f27"
  accent-red-dark: "#ae0101"
  accent-green: "#149547"
  accent-teal: "#1e94b6"
  success: "#28a745"
  danger: "#dc3545"
  warning: "#ffc107"
  info: "#17a2b8"
  dark: "#343a40"
  border-light: "#e9ecef"
typography:
  display-xl: {fontFamily: "proxima-nova, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "proxima-nova, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "proxima-nova, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
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
    padding: "{spacing.sm} {spacing.md}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  category-mega-menu:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge-stock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  badge-alert:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** — Maps directly to the observed `.btn-primary` rule (`#007bff` background, `.25rem` radius, `1rem/1.5` type). Used for primary catalog actions such as "Add to Cart" or "Search." Hover/focus states are not present in the supplied CSS and are proposed as a standard darken-on-hover pattern.

**button-secondary** — An outline variant inferred from the generic `.btn` base rule (transparent background, `#212529` text, border, same radius/padding). Proposed for secondary actions like "View Details" or "Compare."

**text-input** — Not directly evidenced by a selector snippet, but inferred from Bootstrap form conventions present in the bundle (hairline border, canvas background, body typography). Used for search fields and account forms.

**nav-bar** — Proposed top navigation shell reflecting the site's confirmed mega-menu category structure (Woodworking, Metalworking, Shop Essentials, etc.). White background and hairline border are inferred from the surrounding Bootstrap neutral palette; no direct nav selector was supplied.

**category-mega-menu** — A category-appropriate component addressing the extensive nested category taxonomy in the page text (Table Saws → Table Saw Accessories → Inserts, etc.). Proposed as a multi-column flyout panel using the light surface and hairline border tokens; depth/behavior is not observed.

**product-card** — Proposed container for machinery/tool listings, using `surface-card` and `hairline` border with title/body typography pairing. Grid layout and image treatment are not confirmed by supplied evidence.

**hero** — Proposed top-of-page promotional band using the light gray surface token and display typography; no hero markup or imagery was present in the supplied evidence.

**footer** — Proposed dark footer using the Bootstrap `dark` (#343a40) token with white text, appropriate for the multi-link footer implied by "Back to Main Menu" / "Product Recalls" navigation entries.

**badge-stock / badge-alert** — Proposed status indicators using the non-Bootstrap accent colors (#149547 green, #ec1f27 red) found in the palette but not tied to a specific selector. Likely candidates for stock availability, recall notices, or promotional flags given the industrial/retail context; role is inferred.

**search-bar** — Proposed global search input reflecting the "Search Products and Help Articles" text found on the page, styled with muted placeholder text and hairline border.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior. The CSS exposes Bootstrap's standard breakpoint variables (`sm:576px`, `md:768px`, `lg:992px`, `xl:1200px`), which are used here as a baseline:

| Breakpoint | Width | Layout guidance (proposed) |
|---|---|---|
| xs | 0–575px | Single-column, collapsed hamburger nav, stacked category menu |
| sm | 576–767px | Two-column product grid, condensed search bar |
| md | 768–991px | Three-column product grid, mega-menu begins horizontal disclosure |
| lg | 992–1199px | Full horizontal nav bar, four-column product grid |
| xl | 1200px+ | Max-width container, full mega-menu with multi-column flyouts |

Touch targets are recommended at a minimum 44×44px hit area for nav and button elements, though this is not confirmed by the supplied CSS. Mobile nav collapse behavior (hamburger vs. persistent bar) is proposed, not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS extraction and a page-text excerpt only; no rendered layout, JavaScript-driven interaction, or mobile viewport was observed. The `.btn` padding (`.375rem .75rem`) does not map exactly to the proposed spacing scale and was approximated to the nearest tokens. The `proxima-nova` font family appears in the supplied font list but is not tied to a specific selector in the evidence provided; its use as a display/heading face is inferred, and licensing/availability (it is a commercial Adobe Fonts family) has not been verified. Several palette colors (#ec1f27, #ae0101, #149547, #1e94b6, #e88500, #ffd032, and various grays) appear in the supplied swatch list without an accompanying selector, so their semantic roles (badges, alerts, accents) are inferred rather than confirmed. Component states (hover, focus, active, disabled), the mega-menu's actual interaction pattern, and responsive collapse behavior are proposed patterns only and have not been observed on the live site.
