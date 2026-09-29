---
version: alpha
name: "Cometeer"
source_url: "https://cometeer.com"
captured_at: "2026-09-28T10:20:36.834642+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Cometeer's storefront CSS shows a warm, café-inspired palette built on a cream canvas (#f7f0d3) with near-black ink (#2c2b2b) for body copy, and a golden-yellow accent (#f5d577) used explicitly as the primary button background, with a deeper gold (#d6ba68) on hover and a muted sage-gray (#d8dacf) for disabled states. The stylesheet sets BauTF as the primary typeface across body and buttons, with system sans-serif fallbacks; additional families (Agipo, BauTF-Medium, JetBrainsMono) appear in the font list but their applied roles are not confirmed in the supplied rules, so they are treated as inferred secondary/mono options for headings or numeric price display. Buttons use uppercase text, wide letter-spacing (0.2em), and fully pill-shaped corners (50px radius), suggesting a soft, tactile e-commerce aesthetic suited to a DTC coffee brand. A cluster of saturated hues (teals, browns, a plum, and a red) also appears in the palette; these are inferred as roast-level or flavor-tag accents (e.g., light/medium/dark/decaf badges, "Sweet & Fruity" tags) given the product copy, not confirmed component colors. This interpretation extends the observed button, background, and text tokens into a broader system for cards, navigation, and subscription UI, while flagging anything not directly evidenced as proposed.

colors:
  primary: "#f5d577"
  primary-hover: "#d6ba68"
  ink: "#2c2b2b"
  canvas: "#f7f0d3"
  body: "#2c2b2b"
  muted: "#696969"
  hairline: "#d8dacf"
  surface-soft: "#f7f8f0"
  surface-card: "#ffffff"
  on-primary: "#2c2b2b"
  cream-alt: "#f3f5e8"
  disabled-bg: "#d8dacf"
  roast-light: "#a1775e"
  roast-medium: "#814f34"
  roast-dark: "#422513"
  badge-teal: "#1189a9"
  badge-teal-bright: "#03b8a6"
  badge-red: "#c94644"
  badge-plum: "#bd62a6"
  badge-amber: "#d6832b"
  focus-blue: "#2563eb"
typography:
  display-xl: {fontFamily: "BauTF, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "BauTF, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.3px}
  title-md: {fontFamily: "BauTF, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "BauTF, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen-Sans, Ubuntu, Cantarell, Helvetica Neue, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "BauTF, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "BauTF, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.05em}
  button-md: {fontFamily: "BauTF, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 24px, letterSpacing: 0.2em}
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
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
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
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.roast-medium}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  subscription-selector:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.primary}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.base}"

## Components
**button-primary** reflects the directly observed `.image-bullets__submit-button` rule: gold fill (#f5d577), dark ink text, pill radius (mapped here to `rounded.full`), uppercase 12px BauTF label with wide tracking, and a darker gold hover state — this is the strongest evidence in the source data.

**button-secondary** is proposed as an outlined counterpart (ink border, transparent fill) for lower-emphasis actions like "Learn More," since no secondary button rule was supplied; treat as inferred pattern.

**text-input** is proposed for account/email/gift-message fields seen in the page copy (e.g., "Recipient's Email"); background and border values are inferred from the surface/hairline tokens, not a captured input rule.

**nav-bar** is inferred from the presence of an extensive mega-menu structure in the page text (Shop, Gifts, How It Works) and the `--cometeer-mobile-header-height` custom property, which confirms a fixed-height header exists but not its full styling.

**product-card** is proposed for the coffee listing grid (roaster name, origin, roast, flavor notes, price, "Add" button) implied by repeated product blocks in the page text; card background and radius are inferred defaults.

**hero** is proposed for the top banner ("The perfect cup — every time") using the canvas cream background and a large display type scale; no hero-specific CSS was supplied.

**footer** is proposed with an inverted ink background and cream text as a plausible contrast pairing from the observed palette; not confirmed by a footer selector.

**badge** covers roast-level and flavor tags ("Medium," "Sweet & Fruity") visible in the product copy; colors are drawn from the extended palette's brown and saturated hues, inferred as a roast/flavor-coding system rather than confirmed badge CSS.

**search** and **subscription-selector** (box-size, cadence, one-time vs. membership toggles referenced in cart copy) are proposed components supporting the subscription commerce flow described in the text, styled from the shared token set since no dedicated rules were captured.

## Responsive Behavior
Recommended breakpoints (not measured): mobile ≤ 480px, tablet 481–1024px, desktop ≥ 1025px. A `--cometeer-mobile-header-height: 56px` custom property confirms a distinct mobile header exists, supporting a collapsed/hamburger nav pattern below tablet width. Touch targets for buttons should maintain the 44px+ height implied by the swiper navigation size token (`--swiper-navigation-size: 44px`). Product-card grids are recommended to collapse from a multi-column desktop layout to a single or two-column mobile stack; this is a proposed convention, not an observed layout.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered page, computed layout, or interaction states (hover/focus/active transitions beyond the one captured button) were observed. Several font families (Agipo, BauTF-Medium, JetBrainsMono) appear in the font list without corresponding selector rules, so their actual usage, weight mapping, and licensing/availability are unverified. Many palette entries (teals, plum, red, amber) have no confirmed component association and are mapped here to badge/roast roles by inference from adjacent product copy only. All typography sizes except the 12px button rule are proposed estimates, not measured values. Mobile menu behavior, cart drawer interaction, and subscription-toggle mechanics are described only via page text, not CSS, so their visual implementation is unconfirmed.
