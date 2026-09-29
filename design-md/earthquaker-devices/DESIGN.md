---
version: alpha
name: "EarthQuaker Devices"
source_url: "https://www.earthquakerdevices.com"
captured_at: "2026-09-29T04:12:01.800778+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  EarthQuaker Devices is an Akron, Ohio guitar-pedal maker whose Squarespace-hosted storefront presents a dark, workshop-adjacent aesthetic: near-black inks (#111111, #000000, #1c1c1c) against a white canvas, with a single warm orange (#f58220) and a secondary red-orange (#f0523d) available as accent colors for calls-to-action and status marks. Neutrals span a wide gray range (#333333 to #cccccc) used for body copy, dividers, and card surfaces, consistent with a photography-forward site where pedal artwork carries the color load rather than the UI chrome.
  Font evidence points to a Squarespace font stack rather than site-authored custom type: declared families include Libre Franklin, Open Sans, proxima-nova, Clarkson, Ultra, and Calibre alongside Helvetica/Arial fallbacks. Because no CSS rule confirms which family renders headlines versus body copy, this spec infers Clarkson/Ultra for display roles (consistent with Squarespace's own display-font naming) and Libre Franklin/proxima-nova for body and UI text; these mappings are explicitly inferred, not observed in computed styles. Button typography (uppercase, 15px/400) and cookie-banner caption styling (12px, 0.05em tracking) are the two directly observed type rules and anchor the button-md and caption tokens below.

colors:
  primary: "#f58220"
  accent: "#f0523d"
  ink: "#111111"
  ink-strong: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#818181"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#f2f2f2"
  surface-alt: "#ededed"
  on-primary: "#ffffff"
  overlay-scrim: "#22222266"
typography:
  display-xl: {fontFamily: "Clarkson, Georgia, serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "Ultra, Georgia, serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "proxima-nova, 'Helvetica Neue', sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Libre Franklin', Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Libre Franklin', Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Helvetica Neue', Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.05em}
  button-md: {fontFamily: "'Libre Franklin', Helvetica, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px, textTransform: uppercase}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.ink-strong}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairlineBottom: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink-strong}"
    overlay: "{colors.overlay-scrim}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink-strong}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  audio-demo-player:
    backgroundColor: "{colors.surface-card}"
    accentColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"

## Components
**button-primary** carries the orange accent (#f58220) as a call-to-action fill (e.g., "EXPLORE →", "SUBSCRIBE"), uppercase per the observed newsletter-button rule. **button-secondary** is a proposed outlined variant for lower-emphasis actions like "DEALERS" or "SUPPORT" nav links styled as buttons.

**text-input** is proposed for the newsletter email field and any on-site search box; border and radius are inferred defaults since no input-specific CSS was supplied.

**nav-bar** reflects the dark top navigation implied by the site's black chrome and uppercase link labels (DEVICES, DEALERS, BLOG, ABOUT, STUDIOS, ONOMATOPEDAL, MERCH); exact height and collapse behavior are not observed.

**product-card** is proposed for pedal listing grids, using the light gray card surface (#f2f2f2) against the white canvas, appropriate for photographing individual stompboxes.

**hero** models the homepage banner ("Stereo Easy Listening / Analog amp simulator") as a dark, full-bleed block with a scrim overlay for text legibility over pedal imagery; the overlay token is drawn directly from the observed `--color-component-overlay-bg`-style semi-transparent value.

**footer** uses the darkest ink with muted gray body text and white links, matching the multi-column utility footer (Knowledge Base, Contact, Support, Careers) plus copyright line.

**badge** covers the "product-mark" status tag observed in Squarespace's summary-block CSS (`background:#222;color:#fff`), reused here for "NEW," "SOLD OUT," or similar pedal-status labels.

**audio-demo-player** is a category-appropriate proposed component for embedding pedal sound-demo video/audio, since guitar-pedal commerce typically relies on audio previews; no player markup was present in the supplied evidence, so styling is inferred from the card and accent tokens.

## Responsive Behavior
Proposed breakpoints (not measured): mobile ≤600px, tablet 601–1024px, desktop ≥1025px. Nav collapses to a hamburger/off-canvas menu below tablet width; product-card grids proposed at 1 column (mobile), 2 columns (tablet), 3–4 columns (desktop). Touch targets for button-primary/secondary should maintain a minimum 44px height. Hero headline typography (display-xl) should step down toward display-md scale on mobile to avoid overflow. This section is a recommendation derived from common e-commerce patterns, not an observation of the live site's responsive CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This spec is built from static CSS excerpts and page text only; no rendered screenshots, computed styles, or DOM layout were available. Font-role mapping (which family serves headlines vs. body vs. buttons) is inferred from Squarespace's typical font-library naming (Clarkson, Ultra, Calibre, proxima-nova) rather than confirmed selector-level usage. Rounded-corner and spacing scales are proposed defaults, not measured border-radius/margin values from the site. Interactive states (hover/focus/active) beyond the two documented Affirm-button and tooltip-button rules are unverified. Mobile navigation, cart, and product-detail layouts were not observed. Availability and licensing of the named custom fonts (Clarkson, Ultra, Calibre, proxima-nova, futura-pt-bold) were not verified and may require separate licensing from Squarespace or the respective foundries before reuse.
