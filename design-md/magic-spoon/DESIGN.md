---
version: alpha
name: "Magic Spoon"
source_url: "https://magicspoon.com"
captured_at: "2026-09-28T04:59:41.161219+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Magic Spoon's supplied CSS centers on a saturated violet-purple, #3f0791, used consistently as the button background, border, and CTA text color across both the review-widget (Okendo) custom properties and the site's own navigation components. White (#ffffff) serves as the on-primary and canvas color, with a hover treatment that swaps the primary pill into a pink-to-violet gradient (#d034a2 to #5222e3), suggesting an energetic, playful secondary accent pairing. The broader observed palette includes soft pastel tints (#bfefff, #dad9ff, #b2f9e9, #f3eeca, #faec76) that read as flavor-callout or badge backgrounds rather than core UI chrome; these are treated here as inferred accent/surface roles since no selectors confirm their usage. Body and helper text in the review widget use a cooler slate tone (#676986), which this spec assigns to the body role, alongside a darker inferred ink (#272d45) for headings. Typography draws on Poppins (confirmed in nav/button rules, uppercase, weight 700) for display and button text, Open Sans for body copy, and Saira Condensed as an inferred condensed headline alternate, all loaded on the page but not fully mapped to selectors. Rounded pill shapes (50px/100px observed) are generalized here as a "full" radius token. No live layout, spacing, or breakpoint behavior was observed; those below are proposed conventions consistent with a DTC snack/cereal subscription storefront.

colors:
  primary: "#3f0791"
  ink: "#272d45"
  canvas: "#ffffff"
  body: "#676986"
  muted: "#9a9db1"
  hairline: "#e5e5e5"
  surface-soft: "#f4f4f6"
  surface-card: "#f8f8ff"
  on-primary: "#ffffff"
  accent-pink: "#d034a2"
  accent-violet: "#5222e3"
  highlight-yellow: "#faec76"
  mint: "#b2f9e9"
  sky-tint: "#bfefff"
  lavender-tint: "#dad9ff"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Saira Condensed, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1px}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    hoverBackgroundGradient: "linear-gradient(270deg, {colors.accent-pink}, {colors.accent-violet})"
    hoverTextColor: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    ctaBackground: "{colors.canvas}"
    ctaBorder: "1px solid {colors.primary}"
    ctaTextColor: "{colors.primary}"
    rounded: "{rounded.full}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.title-md}"
    badgeBackground: "{colors.highlight-yellow}"
  hero:
    backgroundColor: "{colors.canvas}"
    accentBackground: "{colors.lavender-tint}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.mint}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-widget:
    backgroundColor: "{colors.surface-card}"
    accentBackground: "{colors.sky-tint}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    ctaComponent: "button-primary"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"

## Components

**button-primary** is the core purchase/CTA action, directly grounded in the Okendo `--oke-button` custom properties: solid `#3f0791` background, white text, fully rounded corners, 12px/24px padding, and 700-weight Poppins-style text. This pattern is treated as the site's dominant action style.

**button-secondary** represents the outlined nav pill observed in `ms25-bundle-builder-cta` (white fill, purple border and text, uppercase Poppins, 40px-tall pill). Its hover state — a purple-to-pink linear gradient — is directly copied from the supplied hover rule and proposed for reuse on other secondary actions.

**text-input** is a proposed form field pattern; no input styling was directly observed beyond generic `font-family:inherit` resets in the review widget, so sizing, border, and radius are inferred defaults consistent with the brand's soft, rounded aesthetic.

**nav-bar** reflects the confirmed white sticky-header background (`background-color:#fff!important`) and purple toggle/hamburger accent (`#3f0791`) from the mobile navigation CSS, extended into a full desktop bar pattern that is otherwise unobserved.

**product-card** is proposed for the flavor/bundle tiles implied by the page text ("CEREAL VARIETY 4-PACK", ratings, pricing). Card surface, radius, and price/title typography are inferred; no card-specific selectors were supplied.

**hero** models the large marketing banners referenced in the text excerpt ("High-Protein Cereal That Actually Tastes Like Cereal"). Layout, spacing, and lavender-tint background are proposed, not measured.

**footer** is a proposed low-emphasis section using the muted body color and a soft surface tint, since no footer-specific selectors were present in the evidence.

**badge** covers small callouts like "0-2g Sugar" or "80,000+ 5-Star Reviews" chips; the mint tint and pill radius are inferred choices consistent with the pastel accent colors present in the palette but not tied to a confirmed badge selector.

**search** is a proposed utility input pattern for product/flavor lookup; unobserved directly, styled to match the pill-shaped, soft-surface language established by the confirmed buttons.

**subscription-widget** is the category-appropriate component for this snack/subscription brand, reflecting the repeated "Build Your Bundle" / "Subscribe & Save" content blocks. It reuses the primary button and a light sky-tint accent surface; exact layout is inferred.

## Responsive Behavior

The following breakpoints are a proposed convention, not measured from the live site:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–599px | Single-column stacking; nav collapses to hamburger toggle (consistent with the observed `.mobile-menu .btn-toggle` and `#mobile-slides-content` rules) |
| tablet | 600–959px | Two-column product grids; hero text scales down from display-xl to display-md |
| desktop | 960–1279px | Full nav bar with visible bundle-builder CTA pill |
| wide | 1280px+ | Max-width content container; unchanged component scale |

Touch targets should be at minimum 44×44px, matching the observed 40px-tall nav CTA rounded up for accessibility. Mobile nav collapse into a slide-out/drawer pattern is inferred from the `mobile_slide` and `.mobile-menu` class names present in the CSS, but actual open/close animation and breakpoint pixel values were not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived entirely from static CSS fragments, a page-text excerpt, and a color/font inventory; no rendered layout, computed spacing, or responsive behavior was directly observed. Role assignments for ink, body, muted, hairline, and surface colors are inferred from limited usage context (e.g., `#676986` only confirmed on review-widget helper text) and may not reflect the brand's actual design-system intent. Pastel palette entries (mint, sky-tint, lavender-tint, highlight-yellow) are assigned speculative UI roles since no selectors tie them to specific components. Typography sizes, line-heights, and letter-spacing beyond the confirmed 16px/700-weight Poppins button rule are proposed values, not measured. Saira Condensed and Saira Extra Condensed are listed as loaded fonts but no selector usage was supplied, so their assigned "title" role is inferred. Mabry Pro appears in the font inventory but is unused in this spec pending confirmed selector evidence; its licensing and actual deployment were not verified. Interaction states (focus, disabled, error) and mobile/tablet layout composition are proposed conventions only, not observed behavior.
