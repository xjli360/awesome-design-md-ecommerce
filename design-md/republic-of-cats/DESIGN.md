---
version: alpha
name: "Republic of Cats"
source_url: "https://republicofcats.com"
captured_at: "2026-09-28T10:11:28.092797+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Republic of Cats is a UK subscription cat-food brand pairing a playful, high-contrast palette with DM Sans (Arial/sans-serif fallback), the only typeface confirmed in the supplied CSS. The clearest observed evidence is the primary call-to-action: a pill-shaped button (border-radius ~45px) with a bright yellow background (#ffdc3f) and near-black text (#1d1d1b), set in DM Sans at 16px/700. A secondary dark pill variant reverses this, using #1d1d1b as background with white text, suggesting a light/dark button pairing. Body copy inherits #1d1d1b on a white canvas. Standard navigation-style buttons use small 4px radii, white backgrounds, and 14px/400 DM Sans, implying restrained, low-emphasis UI chrome for header links and menu items.
  Beyond these directly observed rules, the wider palette (teal, coral, pink, gold, navy) is inferred as an illustrative/accent system for cat-personality theming, recipe categories, or review-badge accents rather than confirmed UI roles. Soft teal tints (#e4f1f2, #c9e4ea) are proposed as gentle surface tones for cards and sections, echoing the "healthy, natural" positioning implied by the copy. Layout, spacing, and responsive behavior are not observed and are proposed conventions suited to a personalization-led DTC food subscription flow.

colors:
  primary: "#ffdc3f"
  primary-dark: "#1d1d1b"
  ink: "#1d1d1b"
  canvas: "#ffffff"
  body: "#1d1d1b"
  muted: "#666666"
  hairline: "#efeef0"
  surface-soft: "#e4f1f2"
  surface-card: "#c9e4ea"
  on-primary: "#1d1d1b"
  on-dark: "#ffffff"
  accent-teal: "#64acb3"
  accent-coral: "#ff6d55"
  accent-pink: "#e294c4"
  accent-gold: "#f2c930"
  navy: "#0a313e"
typography:
  display-xl: {fontFamily: "DM Sans, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "DM Sans, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "DM Sans, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "DM Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "DM Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "DM Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  button-md: {fontFamily: "DM Sans, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.19, letterSpacing: 0px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    itemPadding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  plan-quiz-step:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.accent-teal}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"

## Components

**button-primary** is the confirmed CTA pattern: a bright yellow pill (near-full radius, ~45px observed) carrying bold 16px DM Sans in near-black ink, matching the observed "£5 Taster Box"/"GET STARTED" style buttons. **button-secondary** mirrors this shape but inverts to a dark fill with white text, based on the observed header CTA (#1d1d1b background, white text); proposed as the secondary/alternate action pattern (e.g., "Log In").

**text-input** and **search** are proposed, unobserved in the CSS; they assume a light surface, hairline border, and small radius consistent with the sm-radius (4px) buttons seen throughout the nav.

**nav-bar** is inferred from the cluster of white-background, black-text, 4px-radius, 14px/400 DM Sans link buttons repeated across header positions ("Dry food", "Wet food", "Our Story", "Blog"), suggesting a flat, low-contrast top navigation.

**product-card** and **plan-quiz-step** are proposed category-specific components for displaying dry/wet food recipes and the personalization flow ("Tell us about your cat"); they use the soft teal surface tones as an inferred, on-brand background distinct from stark white.

**hero** is proposed to hold the headline ("Tailored nutrition they'll love") atop white canvas with the primary yellow accent, sized at the larger, unobserved display-xl scale.

**footer** is proposed dark-navy (#0a313e), reusing an observed palette color not otherwise assigned a confirmed role, with white text for contrast.

**badge** is proposed for small callouts like "Based on 7043 reviews" or "£5", using the gold accent for visual pop without conflicting with the primary CTA yellow.

## Responsive Behavior

Proposed breakpoints (not measured):

| Breakpoint | Width      | Notes                                  |
|------------|-----------|------------------------------------------|
| mobile     | <640px    | single-column, stacked nav, full-width CTA |
| tablet     | 640–1024px| two-column product/plan cards           |
| desktop    | >1024px   | multi-column hero + nav row (matches observed ~1042px right-aligned button position) |

Touch targets should be at least 40px tall, matching the observed button heights (40px nav buttons, 50px primary CTA). Navigation is expected to collapse to a hamburger/menu (the page text includes a "≡" menu glyph) below tablet width. This section is a recommendation derived from conventional patterns, not measured site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS declarations and page text only; no live rendering, computed layout, or interaction states (hover, focus, active, disabled) were observed. Color-role assignments beyond the directly evidenced primary/dark buttons and body text are inferred from palette proximity and common DTC subscription-site conventions. Typography sizes above 16px (display and title scales) are proposed, not measured, since only 14px and 16px DM Sans values appear in the supplied CSS. The border-radius value of ~45px on CTA buttons is treated as functionally equivalent to a full pill and mapped to `rounded.full`, though the exact 9999px value was not observed. Spacing tokens are conventional proposals, not extracted from layout measurements. Mobile/responsive behavior, breakpoints, and menu collapse mechanics are not observed and are offered only as standard recommendations. DM Sans's licensing and self-hosted vs. third-party delivery were not verified from the supplied evidence.
