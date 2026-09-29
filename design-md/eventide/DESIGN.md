---
version: alpha
name: "Eventide"
source_url: "https://www.eventideaudio.com"
captured_at: "2026-09-28T10:10:06.489305+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Eventide's public site is a WordPress/Astra-based storefront for professional
  effects pedals, rack processors, and plug-ins, and its extracted CSS is
  dominated by two overlapping systems: a Bootstrap-derived utility palette
  (grays, semantic reds/greens/yellows) and a smaller set of brand-leaning
  accents (a cyan-blue #0274be/#004a80 pair, a warm gold #c8a96e, and a teal
  #74ddc7 used explicitly on the site's audio-preview player controls). Because
  no dedicated brand stylesheet was isolated, role assignments below are
  inferred: #0274be is treated as the primary interactive color, #74ddc7 as a
  secondary "live/playing" accent carried over from the observed audio-player
  component, and #c8a96e as a premium/limited-edition accent echoing pedal
  marketing language ("Knife Drop," "H9000 Immersive"). Neutrals (#ffffff,
  #f8f9fa, #f1f1f1, #dee2e6, #343a40, #212529) form the light-mode structure,
  while #0c0c0c/#080808 are reserved for dark hero or product-stage panels,
  fitting a gear brand that photographs black hardware on dark backgrounds.
  Typography combines Montserrat for display/heading weight (inferred, common
  Astra pairing) with Open Sans for body copy, the only family directly tied
  to a font-weight:700 declaration in the evidence; Inter, Arial, and system
  fonts serve as fallbacks. Layout, spacing, and rounding values are proposed
  conventions, not measured from the live DOM.

colors:
  primary: "#0274be"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#343a40"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#f1f1f1"
  on-primary: "#ffffff"
  accent-teal: "#74ddc7"
  accent-gold: "#c8a96e"
  dark-surface: "#0c0c0c"
  danger: "#dc3545"
  success: "#28a745"
  warning: "#ffc107"
  info: "#17a2b8"
typography:
  display-xl: {fontFamily: "Montserrat, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Open Sans, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  audio-preview-player:
    backgroundColor: "{colors.dark-surface}"
    accentColor: "{colors.accent-teal}"
    controlTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** is the main call-to-action pattern ("Explore →", "Learn More") using the inferred brand blue `{colors.primary}` against white text; the arrow-suffixed CTA style seen repeatedly in the excerpt suggests a consistent, low-ornamentation link-button treatment.

**button-secondary** proposes an outline variant for lower-emphasis actions (e.g. "Shop Rackmount" alongside a primary "Shop Effects Pedals"), reusing the primary blue for both fill and border to keep the accent vocabulary tight.

**text-input** covers the site search field ("Search...") and any account/login forms; neutral canvas background with a hairline border keeps it visually quiet against product imagery. State styling (focus, error) is proposed, not observed.

**nav-bar** models the persistent header implied by the repeated menu structure (Products, Community, Support, Company, Shop, Log In). A light canvas background with a bottom hairline is proposed for a typical sticky-header pattern; no scroll-state behavior was captured.

**product-card** represents pedal/plug-in listing tiles (H9 Harmonizer, Temperance Pro, Music Mouse). A soft card surface with rounded corners and a title/body pairing supports the grid-like product news sections referenced in the text excerpt.

**hero** covers the large top-of-page promotional banners ("H9 Harmonizer Gen 2 — The Next Generation Harmonizer"). A dark surface is proposed to match music-gear photography conventions and the site's `#0c0c0c`/`#080808` dark tones, though the live hero background was not directly measured.

**footer** groups the extensive link taxonomy (Community, Company, Support columns) evident in the navigation text. Dark background and muted text reuse existing neutrals rather than introducing new colors.

**badge** proposes a small label for "New," "Limited Edition," or "AVAILABLE NOW" flags (e.g. Knife Drop, H9 Dark) using the gold accent to signal limited/collectible product runs.

**search** is a compact variant of text-input for the header search affordance explicitly present in the page text ("Search...", "Search for:").

**audio-preview-player** is grounded directly in observed CSS (`#sonaar-player`, `.iron-audioplayer`), which is the one component with concrete selector-level evidence: a dark player shell with teal (`rgba(116,221,199,1)`) progress/handle accents and white control text, fitting a pedal/plug-in site that likely embeds audio demos of effects.

## Responsive Behavior

A compact, proposed breakpoint table (not measured from live responsive behavior):

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <576px | Nav collapses to a hamburger/off-canvas menu; single-column product cards; search field expands full-width on focus. |
| Tablet | 576–991px | Two-column product grids; nav may remain collapsed depending on menu depth (Products/Community/Company are multi-level). |
| Desktop | ≥992px | Full horizontal nav with dropdowns; three-to-four column product/news grids; hero at full bleed. |

Touch targets are recommended at a minimum 44×44px for nav items, buttons, and player controls. Given the deep multi-level navigation implied by the text excerpt (Products → Effects Pedals/Plug-ins/Subscriptions/Rack Effects/Eurorack/Broadcast/Software/Apps), a collapsible accordion pattern is recommended for mobile rather than nested hover menus. This section is a design recommendation only; no actual responsive markup or breakpoints were observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This DESIGN.md is derived from static CSS/text extraction only; no rendered layout, computed styles, or interaction states (hover, focus, active, disabled) were observed. Color-role assignments (primary, accent-teal, accent-gold, dark-surface) are inferred from a mixed palette that includes generic Bootstrap defaults, and the true brand-specific colors used in the live header/hero/buttons were not isolated from utility-class colors. Typography is only partially confirmed: Open Sans is tied to one explicit `font-weight:700` declaration on an audio-player component; Montserrat, Inter, and other listed families are present in the font pool but their actual assigned roles (headings vs. body) are inferred, not measured. All spacing, rounding, and breakpoint values are proposed conventions rather than extracted measurements. Mobile navigation behavior, sticky-header behavior, and product-card grid structure are not observed and are proposed patterns only. Font licensing/self-hosting status (e.g., whether Montserrat/Open Sans are served via Google Fonts, a font CDN, or self-hosted) was not verified.
