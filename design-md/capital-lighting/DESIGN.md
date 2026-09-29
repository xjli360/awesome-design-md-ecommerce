---
version: alpha
name: "Capital Lighting"
source_url: "https://capitallightingfixture.com"
captured_at: "2026-09-28T09:56:08.637317+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Capital Lighting's public CSS is built on a Bootstrap 4 utility framework, so the observed palette is largely the Bootstrap default set (--primary #007bff, --secondary #6c757d, --dark #343a40, --light #f8f9fa) rather than a bespoke brand system. Body background is pure white (#ffffff) with body copy inheriting Bootstrap's default #212529/#495057 grayscale. Borders and dividers use the standard #dee2e6 hairline. Two font families appear in the evidence: Playfair Display, a serif suited to the brand's "Artisan Crafted," "Sophisticated Shine" collection language, and Roboto alongside a system sans-serif stack (-apple-system, Segoe UI, Helvetica Neue, Arial) for UI and body text. This interpretation assigns Playfair Display to display/heading roles (inferred, since no selector explicitly binds it to h1–h6) and the sans-serif stack to body, navigation, and controls, matching typical decorative-lighting retail patterns of a refined serif for product storytelling paired with a clean utility sans-serif for commerce UI. Button, card, and form patterns below extend Bootstrap's .btn-primary/.btn-secondary conventions using only the observed hex values. All spacing, radius, and non-color sizing are proposed conventions, not measured from the live site.

colors:
  primary: "#007bff"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#495057"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  ink-strong: "#000000"
  line-dark: "#343a40"
  surface-alt: "#e9ecef"
  disabled: "#999999"
  danger: "#dc3545"
  success: "#28a745"
typography:
  display-xl: {fontFamily: "'Playfair Display', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Playfair Display', serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Roboto, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.3px}
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
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.muted}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.line-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.line-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  finish-swatch:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xxs}"

## Components

**button-primary** maps directly to the observed `.btn-primary` rule (`#007bff` fill, white text, matching border) and is proposed for primary CTAs such as "Explore Collection" or "Find a Dealer." Hover/active darker shades (`#0069d9`, `#0062cc`) are observed in the CSS but not confirmed live.

**button-secondary** mirrors `.btn-secondary` (`#6c757d` fill) for lower-priority actions like "View Details" or filter toggles; hover state (`#5a6268`) is evidenced in CSS, proposed for interaction.

**text-input** is proposed for search fields, wish-list, and dealer-login forms, using the Bootstrap-style hairline border (`#dee2e6`) and white canvas background; focus ring color is not evidenced and left unspecified.

**nav-bar** represents the top utility/primary navigation (Wish List, Dealer Login, Search, category menu) inferred from the page's text structure; background is proposed as white canvas with a bottom hairline, typography set to title-md.

**product-card** is proposed for luminaire listings (e.g., "Jensen Semi-Flush," "Morada Vase Pendant") using a soft off-white surface (`#f5f5f5`) and a light rounded border to separate cards in a grid; no live grid metrics were observed.

**hero** covers the homepage banner ("Elevate Your Everyday," collection launches) using the dark surface (`#343a40`) as an inferred moody backdrop for large Playfair Display type; actual hero background imagery/color is not confirmed from CSS alone.

**footer** is proposed using the same dark surface for the contact/company/resources columns seen in the page text, with white text and small body typography for links and copyright.

**badge** is proposed for "New" labels seen throughout the collection list (e.g., "New Homeplace Collections"), using the primary blue pill shape; actual badge styling on-site is not confirmed.

**finish-swatch** is a category-specific proposed component for the "Signature Finishes" feature (e.g., Taupe, Aged Brass, Tibetan Hammered Brass), rendered as a small rounded chip with a hairline border to represent selectable finish options.

## Responsive Behavior

Proposed breakpoint table (source values are Bootstrap CSS variables observed in `:root`, layout behavior itself is not measured):

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| xs | 0px | Single-column stacking, collapsed nav |
| sm | 576px | Two-column product grids begin |
| md | 768px | Nav collapses to hamburger below this point (proposed) |
| lg | 992px | Three/four-column product grids, full nav visible |
| xl | 1200px | Max-width container, generous section padding |

Touch targets are recommended at a minimum 44×44px for buttons and nav items; mobile nav collapse, drawer behavior, and hover-to-tap conversions are proposed conventions only, not observed in this evidence set.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS/text extraction only; no live rendering, computed styles, or DOM inspection was performed. The supplied CSS is largely unmodified Bootstrap 4 default theming (utility color variables, `.btn-*`, `.table-*` classes), so brand-specific customization beyond these defaults may exist on the live site but is not evidenced here. The mapping of Playfair Display to display/heading roles and the sans-serif stack to body/UI is inferred from font-family presence in the stylesheet, not from explicit selector bindings to heading elements. All spacing scale, radius scale, and most typography sizes are proposed design conventions, not measured pixel values from the site. Component states (hover, focus, active, disabled) beyond the few Bootstrap hover rules shown are proposed, not observed. Mobile/responsive layout behavior, breakpoint-triggered navigation collapse, and touch interactions were not observed and are recommendations only. Font licensing and self-hosting/CDN availability for Playfair Display and Roboto were not verified.
