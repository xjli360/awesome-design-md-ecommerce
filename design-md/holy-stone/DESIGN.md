---
version: alpha
name: "Holy Stone"
source_url: "https://holystone.com"
captured_at: "2026-09-28T09:23:23.046061+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Holy Stone's storefront CSS points to a utilitarian, Bootstrap-derived foundation (glyphicon and contextual-alert classes, .navbar-fixed-top) layered with a small set of custom brand tokens declared as CSS variables: --hs-yellow (#fce30d), --hs-green (#577054), --hs-mint (#bfccb5), and neutral panel/background tones (#edf0f5, #e3e3db). This interpretation treats #577054 as the primary brand accent (used on hover states and "more" links), #fce30d as a high-contrast activation/highlight color (seen on an active shop-toggle state), and #111111/#333333 as the core ink and body-text pair. Muted grays (#666666, #999999) and hairlines (#dddddd, #e5e5e5) are inferred from common Bootstrap gray-scale usage rather than directly observed on visible text. Typography is inferred from the declared font stack: Poppins for display/heading weight (matching the bold 700-900 weight nav labels) and Helvetica Neue/Arial for body copy, consistent with the Bootstrap-era sans-serif defaults present in the CSS. A custom "Holystone" font family is referenced in the stylesheet but its glyphs, weights, and licensing are unverified. Bootstrap's contextual alert palette (success/info/warning/danger) is preserved as semantic feedback color, likely used for form validation or stock-status messaging rather than primary branding.

colors:
  primary: "#577054"
  primary-hover: "#4f6b54"
  accent-yellow: "#fce30d"
  accent-orange: "#ff902d"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#e5e5e5"
  surface-soft: "#edf0f5"
  surface-alt: "#e3e3db"
  surface-card: "#f5f5f5"
  mint: "#bfccb5"
  dark-surface: "#262626"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#dff0d8"
  success-ink: "#3c763d"
  warning: "#fcf8e3"
  warning-ink: "#8a6d3b"
  danger: "#f2dede"
  danger-ink: "#a94442"
  info: "#d9edf7"
  info-ink: "#31708f"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 600, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 14px, fontWeight: 800, lineHeight: 1, letterSpacing: 0.2px}
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
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    hoverBackground: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    height: "74px"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.mint}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  spec-chip:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** uses the observed --hs-green (#577054) as a solid fill with white text, intended for primary conversion actions like "Add to Cart" or "Shop Now." The bold button-md typography mirrors the 800-weight, 14px labels observed on the site's `.cat13-actions-list a` links.

**button-secondary** is a proposed outline variant sharing the primary green as text/border color on a white canvas, for secondary actions such as "Compare" or "View Specs" alongside a primary CTA.

**nav-bar** reflects the measured `--header-h: 74px` custom property and the `.user-menu a:hover` rule, which sets a `#f5f5f5` hover background and `#222` text — mapped here to surface-card and body/ink tokens respectively.

**product-card** is inferred from the dense catalog structure in the page text (model name, spec line, thumbnail) rather than any directly captured card CSS; hairline borders and soft radius are proposed to unify the many drone tiles (T60A, HS900PRO, HS175D, etc.).

**hero** proposes the --hs-bg-1 (#edf0f5) panel tone as a section background for the "Dare to Fly / Soar to Live" tagline area, paired with the large display-xl heading style.

**footer** is inferred as a dark section using #262626 (approximating the observed but unlisted #1f1f1f dark CTA background) with mint-green (#bfccb5) links for legal/support navigation (Warranty, Privacy Policy, Terms of Use).

**badge** repurposes the --hs-yellow (#fce30d) activation color seen on the active `.hs-shop-toggle` state as a small pill, proposed for "New," "Top Pick," or promo-code callouts like "NONSTOPFUN."

**spec-chip** is the category-specific component: small inline tags for recurring spec strings ("48MP," "4K@30fps," "GPS," "10km") that appear throughout every product listing, using the neutral surface-alt background (#e3e3db) to stay visually secondary to primary CTAs.

**search** and **text-input** are proposed, unobserved form patterns using the generic hairline/surface-card neutrals for consistency with the rest of the interface, since no dedicated search-input CSS was supplied.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior (no media queries were supplied in evidence):

| Breakpoint | Width      | Layout notes (proposed)                        |
|-----------|------------|-------------------------------------------------|
| mobile    | <480px     | Single-column product grid, collapsed nav-bar into a menu icon |
| tablet    | 480–1024px | 2-column product grid, condensed category flyout |
| desktop   | 1024–1440px| Full mega-menu (matching `.cat13` multi-column pattern), 3–4 column grid |
| wide      | >1440px    | Max-width container, additional hero spacing |

Touch targets should be at least 44px tall (nav-bar height of 74px supports this), with `button-primary`/`button-secondary` padding sized at `{spacing.md} {spacing.lg}` to remain tap-friendly. The multi-column `.cat13` navigation should collapse to an accordion or drawer pattern below tablet width; none of this collapse behavior was directly observed and is proposed for usability only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is generated from static CSS/text extraction only; no rendered layout, animation, or interaction states were observed. Semantic color roles (primary, muted, hairline, surface tiers) are inferred from variable names and rule context (e.g., `--hs-green`, `--hs-yellow`, alert-color patterns) rather than confirmed visual usage across the live site. All component paddings, radii, and breakpoints are proposed conventions, not measured values. The custom "Holystone" font family appears in the font-family list but its actual glyph set, weight range, and licensing terms were not verified and should not be assumed production-ready. Mobile menu behavior, hover/focus states beyond the two captured rules, and card/grid structure for the product catalog were not present in the supplied CSS and are therefore treated as inferred, standard e-commerce patterns rather than site-confirmed facts.
