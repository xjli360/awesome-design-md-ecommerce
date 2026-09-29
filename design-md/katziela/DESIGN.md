---
version: alpha
name: "Katziela"
source_url: "https://katziela.com"
captured_at: "2026-09-28T09:54:59.764151+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Katziela sells airline-compliant pet carriers, beds, and travel accessories through a Shopify storefront. The only clearly brand-specific accent in the evidence is a teal (#108474), reused across the Judge.me review widget (star color, primary button, reviewer name) — this is treated as the primary brand color. A warm orange (#f7a627) appears on a secondary slideshow button and is proposed as a supporting call-to-action accent, with a matching yellow (#fbcd0a) as a lighter highlight. Neutrals span from near-black (#1c1c1c, #000000) for text/ink to a family of light grays (#eeeeee, #f2f2f2, #dddddd) for surfaces and hairlines; these role assignments are inferred from typical Shopify theme conventions since layout was not directly observed. Typography uses Jost (a geometric sans, assigned to headings/buttons) and Nunito Sans (assigned to body copy), both confirmed in the font-family evidence; the root `--text-*` custom properties (12–20px) are observed and mapped directly to body/caption/title scale steps. Rounded and spacing scales mostly follow conventional defaults, with two observed anchors: `0px` radius (Judge.me widget) and `16px` radius (Shopify chat widget). Payment-network and social-icon colors in the palette were excluded as non-brand.

colors:
  primary: "#108474"
  ink: "#1c1c1c"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6c848c"
  hairline: "#dddddd"
  surface-soft: "#f2f2f2"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-warm: "#f7a627"
  accent-highlight: "#fbcd0a"
  tint-primary: "#ebf9f5"
  border-strong: "#303030"
typography:
  display-xl: {fontFamily: "Jost, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Jost, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Jost, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Nunito Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito Sans, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Nunito Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Jost, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.tint-primary}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  collection-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components
**button-primary**: Solid teal fill (`{colors.primary}`) with white text, matching the Judge.me "write a review" button color observed in CSS variables. Proposed for primary storefront actions like "Choose options" or "Add to cart."

**button-secondary**: Uses the observed orange slideshow-button treatment (`#f7a627` background, dark ink text, 700-weight 16px type) as a secondary/promotional call-to-action style, distinct from the primary teal action.

**text-input**: A minimal bordered field using the light hairline gray and white canvas, sized to the observed `--text-base` (14px) body scale. States (focus, error) are proposed, not observed.

**nav-bar**: Reflects the observed header grid (`logo`/`primary-nav`/`secondary-nav` columns) and padding tokens (`1rem`–`1.6rem` observed in header CSS variables). Sticky behavior is indicated by `--header-is-sticky: 1` in evidence, so a fixed/sticky nav is a reasonable inferred pattern.

**product-card**: Light gray card surface for listing items such as the "Luxury Rider Pet Carrier" or "Rolling Rover" products, with title/price typography drawn from the text-scale tokens. Hover and quick-add states are proposed.

**hero**: A tinted teal background (`#ebf9f5`, inferred from the primary teal) supporting a large headline announcing "Airline-Compliant Pet Carriers & Supplies," matching the homepage's promotional intro copy. Exact hero layout/image treatment was not observed and is inferred.

**footer**: Dark ink-background footer for contrast against the light body, holding navigation links (Wholesale, Blog, Contact) seen in the page text. Structure/column count is proposed.

**badge**: Pill-shaped teal badge for labels such as "Airline-Compliant" or sale/new-arrival tags, echoing the on-sale/custom-badge CSS variables present in evidence (colors adapted to the confirmed brand teal rather than the unverified rgb sale-red).

**search**: Light-gray search field matching the "Open search" header control referenced in the page text; icon and dropdown states are proposed.

**collection-tile**: Category-appropriate component for the "Shop by Collection" grid (Rolling Carriers, Travel Bags, Slings & Pouches, Beds) described in the page text — a soft-surface tile pairing a title and short descriptive caption, sized for grid presentation.

## Responsive Behavior
Proposed breakpoints (not measured from live site): mobile ≤480px, tablet 481–768px, desktop 769–1200px, wide ≥1201px. Nav collapses to a hamburger/menu icon below tablet width, consistent with the "Open navigation menu" control referenced in the page text. Product grids are assumed to move from a 1-column mobile layout to 2–4 columns at tablet/desktop widths. Touch targets should be at least 44×44px for cart, search, and account icons. This section is a recommendation based on common e-commerce patterns, not a confirmed observation of Katziela's responsive implementation.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no live rendering, computed layout, or interaction testing was performed. Color-to-role mapping (e.g., which grays serve as card vs. section backgrounds) is inferred from naming conventions and typical Shopify theme structure, not confirmed via visual inspection. Font sizes for display-xl/display-md and letter-spacing values are proposed defaults, since only the 12–20px text scale and one 16px button size were directly observed. Hover, focus, error, and mobile-menu states are proposed patterns, not verified interactions. Availability and licensing of the Jost and Nunito Sans font files were not verified. Payment-network and social-media brand colors present in the raw palette were intentionally excluded from role assignment as non-brand elements.
