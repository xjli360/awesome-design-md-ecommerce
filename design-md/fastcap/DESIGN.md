---
version: alpha
name: "FastCap"
source_url: "https://fastcap.com"
captured_at: "2026-09-29T04:06:40.690455+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  FastCap's storefront runs on a Bootstrap-derived front end layered with a
  vendor-specific accent. The observed palette mixes Bootstrap's default
  utility colors (#007bff, #28a745, #dc3545, #ffc107, #17a2b8, #6c757d) with a
  warm brand-orange (#d3812e, #ff9209) that appears in accent and CTA
  contexts, plus a neutral grayscale range (#fff, #f8f9fa, #eeeeee, #dddddd,
  #999999, #333333, #212529) used for backgrounds, hairlines, and body copy.
  Typography is system-stack sans-serif (the Bootstrap
  `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue",
  Arial, "Noto Sans", sans-serif` chain) for UI chrome, with Arial explicitly
  set on product-description paragraphs. Raleway, Lato, and Crete Round are
  present in the font manifest and are treated here as inferred
  display/heading candidates, since no selector ties them directly to a role.
  This interpretation proposes a utilitarian, catalog-driven design: dense
  navigation, plain product cards, and a restrained orange accent reserved for
  primary actions and category highlights, consistent with a practical
  tools-and-hardware retailer rather than a lifestyle brand. All measurements
  beyond the observed CSS are proposed defaults for a functional e-commerce
  layout.

colors:
  primary: "#d3812e"
  accent: "#ff9209"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#f9f9f9"
  on-primary: "#ffffff"
  border-strong: "#cccccc"
  success: "#28a745"
  warning: "#ffc107"
  danger: "#dc3545"
  info: "#17a2b8"
  heart-pink: "#f89fa1"
typography:
  display-xl: {fontFamily: "Raleway, -apple-system, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Raleway, -apple-system, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "normal"}
  body-md: {fontFamily: "Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "normal"}
  body-sm: {fontFamily: "Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "normal"}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.2px"}
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
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-spec-table:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    stripeColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components
**button-primary**: The main CTA style, using the brand orange (`{colors.primary}`) with white text, matching the observed `.product .button.button-3d { color: white !important; }` pattern. Proposed for "Add to Cart" and primary form submissions.

**button-secondary**: An outlined variant using the same orange on a white background, for secondary actions like "View Details" or filter toggles. Border and hover states are proposed, not observed.

**text-input**: A neutral bordered field styled with the hairline gray (`#dee2e6`) border and body copy color, intended for search boxes, account forms, and quantity fields. Focus-state styling is proposed.

**nav-bar**: A white top navigation bar reflecting the site's deep category structure ("Products", "Videos", "Dealers", "About"). Layout assumes a horizontal bar on desktop collapsing to a drawer on mobile; this collapse behavior is proposed, not observed.

**product-card**: A light-bordered card (surface-card background, hairline border) for catalog and category grids, holding product image, title (`title-md`), and price (`body-md`). Corner radius is small to match the utilitarian, catalog-style aesthetic.

**hero**: A soft-background banner section using `{colors.surface-soft}` for promotional messaging (e.g., free-shipping threshold banner seen in page text). Typography uses the proposed display font at medium scale.

**footer**: A dark footer block (`{colors.ink}` background, white text) consolidating contact info, dealer links, and legal/policy links, consistent with the dense link list observed in page text (Privacy Policy, Terms of Use, Shipping Policy, etc.).

**badge**: A small pill using the secondary accent orange (`{colors.accent}`) for labels like "New," "Clearance," or "Most Popular," aligning with the observed product-category taxonomy (New Products, Clearance Products, Most Popular Products).

**search**: A rounded search input paired with an icon button, proposed for header search given the large multi-category catalog implied by the navigation list.

**product-spec-table**: A striped table component (using `{colors.surface-soft}` row striping and hairline borders, echoing the Bootstrap `.table-striped` rule) suited to woodworking-tool spec sheets, measurement charts, or MSDS reference data referenced in the site's footer links.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Layout intent |
|---|---|---|
| xs | 0–575px | Single-column product grid, collapsed hamburger nav, stacked footer links |
| sm | 576–767px | Two-column product grid, condensed search bar |
| md | 768–991px | Three-column product grid, horizontal nav begins to expand |
| lg | 992–1199px | Full horizontal nav, four-column product grid |
| xl | 1200px+ | Max-width container, four-to-five-column grid |

Touch targets are recommended at a minimum 44×44px for buttons and nav items. Mobile navigation should collapse into a drawer/accordion given the extensive category list observed in page text; this collapse pattern is proposed, not confirmed via captured markup or scripts.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is limited to static CSS/text extraction; no rendered layout, computed styles, or interaction states (hover, focus, active, disabled) were observed.
- Color-to-role mapping is inferred: Bootstrap's default utility colors (#007bff, #28a745, etc.) may be present in the codebase but unused in final rendered UI; brand-orange usage (#d3812e, #ff9209) is inferred from CTA/button context, not visually confirmed.
- Raleway, Lato, and Crete Round appear in the font manifest but are not tied to specific selectors in the supplied evidence; their assignment to display/heading roles is speculative.
- All spacing, rounded-corner, and breakpoint values beyond the literal Bootstrap `--breakpoint-*` variables are proposed defaults, not measured from the live site.
- Mobile/responsive behavior, collapse patterns, and touch-target sizing are recommendations only; no mobile viewport CSS or media-query content was supplied.
- Custom font licensing/availability (if Raleway/Lato/Crete Round are used) was not verified.
