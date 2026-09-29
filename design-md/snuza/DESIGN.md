---
version: alpha
name: "Snuza"
source_url: "https://www.snuza.com"
captured_at: "2026-09-29T04:18:39.723658+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Snuza's public site runs on a Foundation-framework base, and the supplied CSS
  exposes Foundation's default utility palette (blues, grays, semantic alert
  colors) rather than a fully bespoke brand system. The dominant confirmed
  values are a Foundation blue (#1779ba) used on primary buttons, a near-black
  body ink (#0a0a0a), and a near-white canvas (#fefefe). A distinct family of
  cyan/teal hexes (#00b1ce, #00c3e3, #1ad0ed, #00c4e2, #02dbff) recurs across
  the palette and is treated here as an inferred Snuza accent, likely tied to
  product photography or callouts, since no selector confirms its exact role.
  Typography is confirmed as a Helvetica Neue / Helvetica / Roboto / Arial
  sans-serif stack for both body copy and headings; several additional family
  names (museo-sans-rounded, vag-rounded variants, Raleway) appear in the
  extracted font list but are not tied to any selector in the evidence, so
  they are excluded from active tokens and flagged in Known Gaps. This
  interpretation proposes a clean, trustworthy child-care/tech aesthetic:
  square-cornered buttons (matching the observed border-radius:0), generous
  whitespace, and a calm blue/teal accent pairing appropriate for a
  parenting-safety brand.

colors:
  primary: "#1779ba"
  ink: "#0a0a0a"
  canvas: "#fefefe"
  body: "#343434"
  muted: "#8a8a8a"
  hairline: "#cacaca"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#fefefe"
  accent: "#00b1ce"
  accent-bright: "#1ad0ed"
  secondary: "#767676"
  success: "#3adb76"
  warning: "#ffae00"
  alert: "#cc4b37"
typography:
  display-xl: {fontFamily: "\"Helvetica Neue\", Helvetica, Roboto, Arial, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "\"Helvetica Neue\", Helvetica, Roboto, Arial, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "\"Helvetica Neue\", Helvetica, Roboto, Arial, sans-serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "\"Helvetica Neue\", Helvetica, Roboto, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "\"Helvetica Neue\", Helvetica, Roboto, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "\"Helvetica Neue\", Helvetica, Roboto, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "\"Helvetica Neue\", Helvetica, Roboto, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  compatibility-checker:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.accent-bright}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** — Maps directly to the observed `.button` / `.button.primary` rule: blue (#1779ba) background, near-white text, and an explicit `border-radius:0`, so `rounded.none` is used rather than a proposed radius. Padding follows the `.85em 1em` observed proportions, approximated with the spacing scale.

**button-secondary** — Based on the observed `.button.secondary` rule (#767676 background, same white text and zero radius). Proposed for lower-emphasis actions like "Learn More" links that are not the page's primary CTA.

**text-input** — Not directly styled in the supplied CSS beyond Foundation resets (`font-family:inherit`), so border color, radius, and padding are proposed, using the hairline gray and a small radius consistent with the square-leaning button treatment.

**nav-bar** — Inferred from the page text listing "Location / Cart / Accessories / Login / About / Products / Support / Blog / Contact." Styled on the light canvas background with dark ink text; exact height, sticky behavior, and dropdown states are not observed.

**product-card** — Proposed pattern for the three featured devices (Pico 2, HeroSE, LooksiA1), each pairing a bold product-name title with a short marketing description and a "Learn More" action, matching the repeated content structure in the page text.

**hero** — Proposed layout for the top banner ("Award-winning child-care aids... BUY NOW / LEARN MORE"), using the soft light background and a large display title; exact hero imagery, overlay, or crop behavior is not observed in the CSS.

**footer** — Inferred from the extensive footer link list (About, Support, Legal, Certifications, Newsletter signup with birthday fields). Dark background is proposed for contrast against the light body, since Foundation's default footer styling isn't present in the supplied rules.

**badge** — Proposed small pill component for callouts like "Rated 4.5 out of 5 stars on Amazon," using the accent cyan family observed in the palette rather than the primary blue, to visually separate trust signals from primary actions.

**search / compatibility-checker** — The footer text references a "Detect Compatibility" page, appropriate for a device/tech brand where customers must confirm a monitor model works with their setup. This component is proposed as a lightweight form panel using the brighter cyan accent for interactive affordances (e.g., a compatibility-check button), since no CSS for this specific tool was supplied.

## Responsive Behavior

Recommended (not measured) breakpoints, aligned to Foundation's typical scale referenced in the extracted font-family string (`small=0em&medium=40em&large=64em&xlarge=75em&xxlarge=90em`):

| Breakpoint | Width      | Notes (proposed) |
|-----------|-----------|-------------------|
| small     | 0–39.9em  | Single-column stack; nav collapses to a hamburger/off-canvas menu |
| medium    | 40–63.9em | Two-column product grid; nav items may remain inline |
| large     | 64–74.9em | Three-column product grid (matching the three featured devices) |
| xlarge+   | 75em+     | Wider gutters/max-width container; no additional column changes assumed |

Touch targets for buttons and nav items should be at least 44×44px given the child-care/commerce context, though this is a general accessibility recommendation, not a site-observed metric. Mobile nav collapse and any accordion/off-canvas interaction are assumed based on common Foundation patterns but are not confirmed in the supplied CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no live rendering, computed layout, or JavaScript-driven interaction (cart, login, newsletter form validation) was observed.
- Several font-family names (museo-sans-rounded, vag-rounded-black-ssi-bold, vag-rounded-standard-thin, Raleway-Bold, Raleway-Medium) were present in the extracted font list but had no associated selector in the supplied CSS rules, so their actual usage (e.g., logo, headings, marketing graphics) and licensing/availability are unverified and excluded from active typography tokens.
- The cyan/teal color family (#00b1ce, #00c3e3, #1ad0ed, #00c4e2, #02dbff) is inferred as a brand accent based on repetition in the palette, not confirmed by any selector tying it to a specific UI role.
- Component definitions for nav-bar, hero, product-card, footer, badge, search, and compatibility-checker are structurally inferred from page text/content order, not from layout-specific CSS in the evidence.
- All spacing and rounded-corner scale values beyond the explicit `.button` `border-radius:0` are proposed conventions, not measured from the site.
- Mobile/responsive breakpoint behavior is a general recommendation based on a Foundation-style breakpoint string, not observed viewport testing.
