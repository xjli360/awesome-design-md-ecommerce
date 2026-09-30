---
version: alpha
name: "Sun Noodle"
source_url: "https://sunnoodle.com"
captured_at: "2026-09-28T10:05:09.341492+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Sun Noodle's observed CSS exposes a small, named palette built around three
  custom properties: --noodle (#faf6de, a warm cream used as the noodle-dough
  base tone), --cookedNoodle (#f2e6c4, a slightly deeper cream for secondary
  surfaces), and --sriracha (#c72040, the brand's red accent, named after the
  condiment and used as the primary interactive color). Button variants show
  an intentional swap pattern: a "classic" button uses sriracha as background
  with noodle-cream text, while "inverted" reverses this, confirming cream
  functions as an on-primary text color rather than a plain white. A darker
  red (#a1122d) and a muted gold (#fcb316) appear in the palette and are
  inferred here as hover/active and secondary-accent roles, since no hover
  color variable was captured directly. Typography pairs a custom display
  face, Dreamboat, for headlines (with Zen Maru Gothic as a Japanese-script
  fallback for the bilingual site) against Work Sans for body copy, with Noto
  Sans JP as its Japanese fallback. This suggests a brand voice that is
  playful and heritage-driven (rounded serif-like display type, warm cream
  grounds) balanced against a clean, legible sans body for product and
  food-service content. Neutral grays (#9ca3af, #e5e7eb) and soft dark-tinted
  overlays (#2d2a2620 etc.) are treated as muted text and hairline dividers.
  All layout proportions, spacing scale, and breakpoints below are proposed
  conventions, not measured from the live site.

colors:
  primary: "#c72040"
  primary-hover: "#a1122d"
  ink: "#2d2a26"
  canvas: "#faf6de"
  body: "#2d2a26"
  muted: "#9ca3af"
  hairline: "#e5e7eb"
  surface-soft: "#f2e6c4"
  surface-card: "#f0e7c8"
  on-primary: "#faf6de"
  accent-gold: "#fcb316"
  accent-yellow: "#fdd756"
  accent-coral: "#f98571"
  accent-orange: "#ffa168"
  accent-lavender: "#cb8bda"
  accent-sky: "#8bb8e8"
  overlay-scrim: "#00000080"
  hairline-strong: "#2d2a2633"
typography:
  display-xl: {fontFamily: "Dreamboat, Zen Maru Gothic, sans-serif", fontSize: 48px, fontWeight: 900, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Dreamboat, Zen Maru Gothic, sans-serif", fontSize: 32px, fontWeight: 900, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Dreamboat, Zen Maru Gothic, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Work Sans, Noto Sans JP, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Work Sans, Noto Sans JP, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Work Sans, Noto Sans JP, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Dreamboat, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1rem, letterSpacing: 0.5px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
    border: "2px solid {colors.primary}"
    hover: "backgroundColor {colors.primary-hover}, borderColor {colors.primary-hover} (proposed)"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
    border: "2px solid {colors.primary}"
    hover: "backgroundColor {colors.surface-soft} (proposed hollow-variant pattern, inferred from .hollow button)"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    focusState: "borderColor {colors.primary} (proposed, not observed)"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
    linkHover: "color {colors.primary} (proposed)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    shadow: "0 1px 2px {colors.overlay-scrim} (proposed, subtle)"
  recipe-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    imageAspect: "4:3 (proposed)"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.caption}"
    accentBar: "{colors.accent-gold} (proposed category tag color, e.g. Ramen vs Mazemen)"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaVariant: "button-primary"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    linkColor: "{colors.accent-gold}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"

## Components
**button-primary** reflects the observed `.classic` button pattern: a sriracha-red fill with cream (`--noodle`) text and a matching red border, using the custom Dreamboat display font in uppercase per the CSS `text-transform:uppercase`. The hover treatment darkens to the secondary red (#a1122d); this exact hover color is inferred from the palette's presence, not from a captured `--hoverBackground` value.

**button-secondary** mirrors the `.hollow` variant seen in CSS: cream background, sriracha border and text, intended for lower-emphasis actions like "See all" or "Learn more" links alongside a primary CTA.

**text-input** is a proposed pattern for newsletter/slurpmail signup and store-locator search, since form styling wasn't directly captured beyond generic `button,input` resets. Cream background and thin hairline border keep it visually consistent with card surfaces.

**nav-bar** is inferred from the page's structural text (Home, Products, About, Store Locator, 日本語 toggle) rather than measured CSS; a light cream bar with a thin bottom hairline keeps the header visually quiet against colorful hero imagery.

**product-card** is proposed for the Ramen/Tsukemen/Mazemen/Yakisoba product-family grid implied by the nav structure, using the deeper cream `surface-card` tone to differentiate from the page background.

**recipe-card** is a category-appropriate component for content like "Miso Butternut Curry Miso Ramen," pairing an image block with a gold accent bar to signal recipe/feature content distinct from commerce cards.

**hero** uses the soft cooked-noodle cream as a background wash behind a large Dreamboat headline, consistent with a warm, food-forward homepage banner; exact hero copy/layout is not observed, only inferred from page-text excerpts like "Hello Hawai'i."

**footer** is proposed as a dark-ink block for contrast, holding the sitemap links (Careers, Our Noodles, Blog, FAQ) enumerated in the page text, with gold-accented link hover states drawn from the palette's gold token.

**badge** and **search** are supporting, proposed utility components for tagging (e.g., "New," "Preservative Free") and the Ramen Finder / Store Locator search field referenced in the page copy.

## Responsive Behavior
This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <640px | Single-column stacks; nav collapses to a hamburger/menu overlay (page text references "Menu Close"). |
| Tablet | 640–1024px | Two-column product/recipe grids; hero text scales down from display-xl to display-md. |
| Desktop | >1024px | Multi-column grids (3–4 cards); full horizontal nav bar. |

Touch targets for buttons and nav links should maintain a minimum 44×44px hit area; the observed button padding (`.75rem 1rem` / `12px 32px`) is compatible with this at desktop sizes but should be re-verified for compact mobile buttons. Menu collapse behavior is inferred solely from the "Menu Close" label in page text, not from observed JavaScript or breakpoint CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no live rendering, computed styles, or interaction states (hover, focus, active, disabled) were directly observed beyond the `:hover` rules explicitly listed. Several hex values (e.g., #a1122d as a hover-red, #fcb316 as an accent-gold) are plausible role assignments based on palette proximity and naming conventions (`--hotSriracha` was referenced but its value not captured), not confirmed CSS variable bindings. All spacing scale, breakpoint widths, and component sizes not explicitly present in the supplied CSS are proposed conventions for internal consistency, not measurements. Mobile menu behavior, grid column counts, and card layouts are inferred from page text and general e-commerce/blog conventions, not from captured layout CSS. The custom font Dreamboat's licensing, hosting, and full character-set availability were not verified from the supplied evidence; Work Sans and Noto Sans JP are assumed to be standard web-font loads. Japanese-locale-specific styling (`html[lang=ja]`) confirms bilingual support but its visual treatment beyond font-family swaps was not fully captured.
