---
version: alpha
name: "Maev"
source_url: "https://meetmaev.com"
captured_at: "2026-09-28T09:52:38.852357+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Maev's evidence surfaces a warm, natural-foods palette anchored by a cream canvas (#fbf5e3) and a dark forest green (#183613) used as the confirmed hover/interaction color on icon buttons, paired with the same cream as its on-color text — this pairing is treated as the primary brand color and its foreground. Body copy renders in FoundersGrotesk, a grotesk sans confirmed directly on the `body` selector; freight-big-pro and freight-display-pro appear only in the font-family list without a bound selector, so they are inferred as an editorial serif reserved for large display headlines and testimonial pull-quotes, consistent with the page's storytelling sections ("Dig Deeper," founder story, press features).
  Neutral ink (#353535), muted gray (#9a9999), and hairline grays (#dddddd, #f7f7f7) are inferred from the supplied grayscale set to build text hierarchy and card/section separation on the cream canvas. A cluster of saturated hues (#e5ff00, #c47225, #96b108, #66969c, #eb3838, #4f1ee7) is present in the raw palette without confirmed selectors; these are interpreted as accent/tag colors — a bright yellow-green CTA accent and a small set of category tags for the site's "Digestion / Mobility / Coat / Calming" formula groupings — since no direct role evidence exists for them. No custom brand font beyond FoundersGrotesk is verified; layout, spacing, and card structure are proposed conventions suited to a whole-ingredient pet-nutrition DTC storefront, not measured observations.

colors:
  primary: "#183613"
  ink: "#353535"
  canvas: "#fbf5e3"
  body: "#353535"
  muted: "#9a9999"
  hairline: "#dddddd"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#fbf5e3"
  accent: "#e5ff00"
  accent-warm: "#c47225"
  tag-mobility: "#96b108"
  tag-coat: "#66969c"
  tag-digestion: "#eb3838"
  tag-calming: "#4f1ee7"
typography:
  display-xl: {fontFamily: "freight-display-pro, freight-big-pro, serif", fontSize: 56px, fontWeight: 500, lineHeight: 1.08, letterSpacing: -0.5px}
  display-md: {fontFamily: "freight-display-pro, freight-big-pro, serif", fontSize: 36px, fontWeight: 500, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "FoundersGrotesk, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "FoundersGrotesk, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "FoundersGrotesk, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "FoundersGrotesk, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "FoundersGrotesk, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hoverBackground: "{colors.primary}"
    hoverText: "{colors.on-primary}"
    borderBottom: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaBackground: "{colors.primary}"
    ctaText: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkHoverColor: "{colors.accent}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent}"
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
  formula-tile:
    backgroundColor: "{colors.surface-soft}"
    accentBar: "{colors.tag-mobility}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** is the dark forest-green fill (`{colors.primary}`) with cream text, directly grounded in the confirmed `:hover` background/color pairing on the observed IconButton selectors; used here for primary calls-to-action like "Shop Now" and "Join." **button-secondary** is a proposed outlined variant for lower-emphasis actions (e.g., "Read More" links), reusing the primary color as border and text with no fill, a pattern inferred rather than measured. **text-input** proposes a white card surface with a light hairline border for email-capture and search fields, since no explicit input styling was present in the evidence. **nav-bar** sits on the cream canvas and inherits the confirmed hover-state colors (green background, cream text) for its links and icon buttons, matching the SHOP/LEARN/HELP navigation groups referenced in the page text. **product-card** is a white surface with a soft hairline border, sized for formula and treat listings (Whole Ingredient Food, Supplements, Bundles), using the inferred serif title type for product names. **hero** reuses the cream canvas with large serif display type for headline moments like "The way dog food should be," paired with a primary-color CTA button; this composition is proposed, not observed in a captured layout. **footer** inverts to the primary green with cream text, a plausible extension of the confirmed hover-color relationship, hosting the SHOP/LEARN/HELP/CONTACT link columns and legal links noted in the source text. **badge** is a small pill using the bright accent yellow-green, proposed for merchandising flags such as "New" or "Limited Edition," which appear in the page copy but without confirmed styling. **search** proposes a soft-gray field for the Help Center search experience. **formula-tile** is a category-appropriate addition for the "Choose your clinically-proven whole food formula" grid (Digestion, Mobility, Coat, Calming Support), pairing a neutral tile surface with one of the tag colors as a small accent bar to visually differentiate each targeted formula — this color-coding is inferred, not confirmed by CSS.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| mobile | 0–599px | Single-column stacking; nav collapses to a hamburger/off-canvas panel; formula tiles stack full-width. |
| tablet | 600–959px | 2-column product/formula grids; nav may condense text labels. |
| desktop | 960–1279px | Full horizontal nav with SHOP/LEARN dropdowns; 3-column product grids. |
| wide | 1280px+ | Max-width content container (~1280–1440px) with generous side padding using `{spacing.xxl}`. |

Touch targets should be at least 44×44px for nav icon buttons and CTAs, consistent with the 32px icon-button box observed plus padding. Collapse behavior for the mega-menu (SHOP/LEARN columns visible in footer text) is proposed as an accordion on mobile.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, breakpoints, or interaction states beyond the two confirmed `:hover` rules were observed. Semantic role assignments for most palette colors (accent, tag-mobility, tag-coat, tag-digestion, tag-calming, accent-warm) are inferred from color character alone, not from bound selectors, since the supplied CSS rules only confirm `#183613`/`#fbf5e3` as an interactive hover pairing. Freight-big-pro/freight-display-pro are listed in font-family data but not tied to a confirmed selector, so their use as a display/serif typeface is inferred, not verified; font licensing and self-hosting availability were not checked. All typography sizes, spacing scale, rounded-corner values, component paddings, and the responsive breakpoint table are proposed design conventions for a DTC pet-nutrition storefront, not measurements taken from the live site. Mobile navigation behavior, cart/search interactions, and product-card real content were not observed and are placeholder structures only.
