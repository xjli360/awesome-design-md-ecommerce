---
version: alpha
name: "Dream Arcades"
source_url: "https://dreamarcades.com"
captured_at: "2026-09-29T04:03:41.707137+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Dream Arcades' stylesheet defines a dark, premium "luxury" theme built on CSS custom
  properties: a near-black canvas (#0a0a0a), white primary text (#ffffff), a muted
  grey secondary text (#a0a0a0), and a saturated orange-red accent (#ee4612) with a
  brighter hover state (#ff5722). Surfaces step up from the canvas via #1a1a1a and
  #262626, giving cards and hover states subtle depth against the black background.
  Typography pairs Outfit (sans-serif, body/UI) with Playfair Display (serif),
  imported together via Google Fonts; Outfit is the declared body font, while
  Playfair Display's presence in :root strongly implies serif display headlines for
  a "handcrafted, premium" tone, though exact heading assignments are inferred, not
  observed in markup. Buttons are explicitly defined (uppercase, bold, 4px radius,
  orange fill inverting to orange-outline on hover). Additional palette values —
  warm gold (#dfa76b) and yellows (#fbc02d/#f9a825) — appear only as raw hex entries
  with no confirmed selector role, so they are treated here as inferred decorative
  accents (e.g., badges, ratings) rather than confirmed brand colors. This spec
  channels that evidence into a dark, editorial arcade-manufacturer interface.

colors:
  primary: "#ee4612"
  primary-hover: "#ff5722"
  ink: "#ffffff"
  canvas: "#0a0a0a"
  body: "#a0a0a0"
  muted: "#888888"
  hairline: "#333333"
  surface-soft: "#1a1a1a"
  surface-card: "#262626"
  on-primary: "#ffffff"
  deep-black: "#050505"
  accent-gold: "#dfa76b"
typography:
  display-xl: {fontFamily: "'Playfair Display', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Playfair Display', serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Outfit', sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Outfit', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Outfit', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "'Outfit', sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "'Outfit', sans-serif", fontSize: 18px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 1px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hoverAccent: "{colors.primary}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    hoverBackgroundColor: "{colors.surface-card}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    backgroundGradient: "radial-gradient(#333, #000)"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    subtitleColor: "{colors.body}"
    ctaComponent: "button-primary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.deep-black}"
    textColor: "{colors.body}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    dividerColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.accent-gold}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  feature-tile:
    backgroundColor: "{colors.surface-soft}"
    iconColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** — Directly derived from `.btn`: a solid accent-orange (#ee4612) button with white text, uppercase 600-weight Outfit type, 4px radius, and a soft orange box-shadow. This is the primary CTA style, e.g. "BUILD YOUR DREAM."

**button-secondary** — Modeled on the confirmed `.btn:hover` state (background clears to transparent, text/border switch to accent orange). Proposed here as a standalone outline variant for secondary actions like "Learn More," since only the hover transform was directly observed.

**text-input** — Not present in supplied CSS; proposed to match the dark-surface aesthetic (surface-soft background, hairline border, white text) for contact/quote-request forms implied by "sales@dreamarcades.com."

**nav-bar** — Proposed top navigation using the canvas background and body-sm Outfit links, with hover behavior modeled on the observed `.header-notice a:hover` pattern (accent color plus accent underline).

**product-card** — Built from the `.slide-wrap .product-text` rules, which show bold, uppercase, centered product labels beneath carousel images, animated with an 0.8s transition. Card container styling (surface-soft background, hover elevation to surface-card) is inferred since no card wrapper rule was supplied.

**hero** — Reflects the `--bg-gradient` radial gradient token and canvas background variable, paired with a large serif headline (Playfair Display, inferred display role) and a primary button. Layout (copy left/image right, etc.) is not observed and is left unspecified.

**footer** — Proposed using the darkest palette value (#050505) and muted secondary text, grouping "Important Links" and "Contact Us" columns per the extracted footer text, with accent-colored link hovers consistent with `.header-notice a:hover`.

**badge** — Proposed small pill component for short trust markers ("TRUSTED BY GLOBAL LEADERS," "100% LICENSED") using the unassigned gold (#dfa76b) as an inferred decorative accent color, since its selector role was not confirmed in the supplied CSS.

**search** — Not observed anywhere in the evidence; included only as a standard utility pattern matching text-input styling, since no search feature was indicated on the page.

**feature-tile** — Category-appropriate component for the icon+heading+description blocks seen in the content ("LEGAL INTEGRITY," "WINDOWS POWERED," "AMERICAN CRAFTSMANSHIP," "CONCIERGE SUPPORT"), using Font Awesome-style icon glyphs in accent orange on a surface-soft tile — well suited to an arcade manufacturer's technical/trust messaging.

## Responsive Behavior

Proposed breakpoints (not measured from live site):

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <600px | Single-column stack; nav collapses to a hamburger/off-canvas menu; hero title drops to `display-md` scale |
| tablet | 600–1024px | Two-column product grid; carousel controls remain visible |
| desktop | 1024–1440px | Full multi-column layout as implied by carousel + grid content |
| wide | >1440px | Max content width with generous canvas margin |

Touch targets should be at least 44px, matching the generous `.btn` padding (1rem 2.5rem) already observed. Carousel prev/next controls ("< >") should have comparable tap targets on mobile. All figures are recommendations only; no responsive CSS or breakpoints were present in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS/text extraction only; no rendered layout, DOM structure, or JavaScript-driven behavior (e.g., the product carousel's actual mechanics) was observed. The assignment of Playfair Display to headline roles is inferred from its presence in `:root` alongside Outfit, not from confirmed heading selectors. Several palette values (#dfa76b, #fbc02d, #f9a825, and the alpha-variant hexes) have no confirmed selector/role in the supplied CSS and are labeled inferred/decorative. Spacing and rounded scales beyond the one confirmed `border-radius: 4px` are proposed conventions, not extracted values. Font licensing/self-hosting terms for Outfit and Playfair Display were not verified beyond their Google Fonts `@import`. Mobile navigation, form, and search interactions were not present in the evidence and are therefore fully proposed.
