---
version: alpha
name: "The Rag Company"
source_url: "https://theragcompany.com"
captured_at: "2026-09-29T04:04:01.085565+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  The Rag Company's storefront runs on a Shopify theme (base.css tokens like
  --color--bg, --font--body) layered with a black-and-white header
  (--header-bg-color:#000000, --header-text-color:#ffffff) and a single
  saturated accent, #00abe0, used as the hover/active state for the Okendo
  review widget's buttons. This suggests a high-contrast, utilitarian
  detailing-brand palette: black and near-black (#000000, #0d0d0d, #212121)
  for chrome and primary actions, white and off-white surfaces
  (#ffffff, #f5f5f5, #f2f2f2, #f7f7f8) for content areas, light greys
  (#e4e4e4, #e5e5e5) for hairlines/dividers, and #00abe0 reserved as the
  single interactive accent (links, focus, hover). A supplementary red
  (#d12328) and green (#00964d) are carried forward for sale/clearance and
  stock-status badges respectively, inferred from typical e-commerce
  category naming (Clearance, TRCMA) rather than directly observed on
  elements. Montserrat appears in the font stack alongside system sans
  fallbacks (Arial, Helvetica, -apple-system); Montserrat is treated as the
  display/heading face and the system stack as body copy, both inferred
  pairings since no explicit heading selector was captured. Corner radii are
  largely square (observed button-border-radius:0), with soft rounding
  reserved for skeleton/loading states (.5em) and proposed sparingly
  elsewhere for cards and inputs.

colors:
  primary: "#000000"
  ink: "#0d0d0d"
  canvas: "#ffffff"
  body: "#212121"
  muted: "#666666"
  hairline: "#e4e4e4"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#00abe0"
  accent-alt: "#00c3ff"
  danger: "#d12328"
  success: "#00964d"
  warning: "#ff7f15"
  border-strong: "#212121"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "normal"}
  body-md: {fontFamily: "Arial, Helvetica, -apple-system, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "normal"}
  body-sm: {fontFamily: "Arial, Helvetica, -apple-system, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "normal"}
  caption: {fontFamily: "Arial, Helvetica, -apple-system, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Arial, Helvetica, -apple-system, sans-serif", fontSize: "14px", fontWeight: 700, lineHeight: 1, letterSpacing: "0.3px"}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
    hover:
      backgroundColor: "{colors.accent}"
      border: "1px solid {colors.accent}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
    hover:
      textColor: "{colors.accent}"
      border: "1px solid {colors.accent}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
    focus:
      border: "1px solid {colors.accent}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: "72px"
    padding: "{spacing.sm} {spacing.lg}"
  mega-nav-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    shadow: "none"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    border-top: "1px solid {colors.hairline}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  free-shipping-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base}"
    rounded: "{rounded.none}"

## Components

**button-primary** is the black-fill, white-text action used for add-to-cart and primary CTAs, matching the observed `--oke-button-backgroundColor:#000` / hover-to-`#00abe0` pattern from the review widget, extended here as the site-wide primary button convention (proposed extension, not directly observed on storefront buttons).

**button-secondary** is an outlined, white-fill variant for lower-emphasis actions (e.g., "Learn More"), using the same border-to-accent hover transition inferred from the primary button's observed hover token.

**text-input** covers search and form fields with a light hairline border and accent-colored focus ring, a conventional pattern proposed for consistency; no live input focus state was captured in the evidence.

**nav-bar** reflects the observed `--header-bg-color:#000000` and `--header-text-color:#ffffff` custom properties, rendered as a fixed-height black bar; sticky behavior is available via `--header-is-sticky` but its runtime value (0) suggests it is currently non-sticky.

**mega-nav-panel** is proposed to house the extensive category tree evident in the page text (Exterior, Interior, Tools, TRC Ultra, etc.) as a white flyout panel beneath the black nav bar, since a catalog this deep implies a multi-column dropdown, though its exact layout was not observed.

**product-card** is a white card with a hairline border for grid listings, sized modestly for a dense catalog; shadow is intentionally omitted since no elevation values were present in the evidence.

**hero** uses the black/white header palette at larger scale for homepage banners (e.g., "Ultra H2O is live"), with display typography; exact hero copy layout is not observed and is treated as a proposed pattern.

**footer** mirrors the header's black background and white text for brand consistency, hosting shipping/policy links; border-top hairline separates it from the last content section (proposed).

**badge** repurposes the observed red (#d12328) for sale/clearance labels seen in navigation ("Clearance"), rendered as a small square-cornered tag; the green (#00964d) is reserved as an alternate badge state for in-stock or success messaging (inferred, not directly observed on a badge element).

**search** and **free-shipping-banner** are both drawn from explicit page copy ("Free Shipping on Orders $115 and Up"), styled as a slim ink-colored strip and a soft-surface search field respectively; visual treatment is proposed.

## Responsive Behavior

This is a recommendation based on standard e-commerce patterns, not measured site behavior:

| Breakpoint | Width | Nav | Grid |
|---|---|---|---|
| Mobile | < 480px | Collapsed hamburger, single-column mega-nav accordion | 1 column product grid |
| Tablet | 480–1024px | Hamburger or condensed horizontal nav | 2–3 column product grid |
| Desktop | > 1024px | Full horizontal nav with mega-nav flyouts | 4+ column product grid |

Touch targets for nav and button components should maintain a minimum 44×44px hit area. The mega-nav-panel should collapse into an accordion list below tablet width given the depth of the observed category tree. No JavaScript-driven interaction (menu open/close, cart drawer) was observed in static extraction; these behaviors are assumed based on typical Shopify theme conventions.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered page, computed styles, or interaction states were observed. The mapping of Montserrat to headings and system-stack fonts to body copy is inferred from the presence of both in the font-family list, not from a captured heading selector. Most color-to-role assignments (danger, success, warning, accent-alt) are inferred from typical e-commerce usage patterns (sale badges, stock status) rather than directly observed on labeled elements — the bulk of the observed palette (teals, magentas, purples like #272d45/#676986) belongs to the third-party Okendo review widget and was excluded from core brand roles as likely non-brand UI chrome. All typography sizes except font-family are proposed, since no font-size values were captured for storefront headings or body text. Border-radius values are mostly proposed; only the button radius (0) and skeleton-loader radius (.5em) were directly observed. Mobile/responsive layout, hover/focus states beyond the Okendo button tokens, and sticky-header behavior are not observed and are marked proposed throughout. Custom font licensing and self-hosting for Montserrat were not verified from the supplied evidence.
