---
version: alpha
name: "Grace Lee"
source_url: "https://www.gracelee.com"
captured_at: "2026-09-28T04:14:38.607010+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Grace Lee presents a restrained, editorial aesthetic suited to fine jewelry and engagement-ring
  merchandising. The observed palette is built almost entirely from neutrals: true black (#000000)
  and white (#ffffff) anchor primary actions and headings, a warm off-white (#f0efeb) and light
  grays (#f2f2f2, #dedede) suggest soft section backgrounds and card surfaces, and mid-grays
  (#333333, #666666, #999999, #cccccc) carry secondary text and hairline borders. A small cluster
  of saturated colors — deep red (#8b0000), forest green (#006400), bright green (#3ed660), orange
  (#ee9441), and two blues (#1990c6, #136f99) — appears alongside near-black (#0a142f, #121212,
  #262626) tones; these are treated as inferred status/accent and footer-depth colors (e.g. stock
  indicators, sale badges, informational links) rather than core brand colors, since their exact UI
  role is not confirmed in the extracted rules.
  Typography is uniformly set in Anuphan with sans-serif fallback; Assistant appears in the font
  stack list but has no confirmed rule usage, so it is treated as an unverified alternate. Observed
  sizes are notably small and tightly tracked (11–14px), with uppercase, letter-spaced buttons and
  h2 labels — a quiet, boutique tone. Hero/display sizes are proposed extrapolations for marketing
  surfaces, not measured values, since no large heading rule was captured.

colors:
  primary: "#000000"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dedede"
  surface-soft: "#f0efeb"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  border-strong: "#999999"
  border-subtle: "#cccccc"
  footer-ink: "#0a142f"
  overlay-scrim: "#00000066"
  overlay-faint: "#0000001a"
  accent-info: "#1990c6"
  accent-info-deep: "#136f99"
  status-success: "#006400"
  status-success-bright: "#3ed660"
  status-alert: "#8b0000"
  status-highlight: "#ee9441"
typography:
  display-xl: {fontFamily: "Anuphan, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: 0em}
  display-md: {fontFamily: "Anuphan, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0em}
  title-md: {fontFamily: "Anuphan, sans-serif", fontSize: 11px, fontWeight: 700, lineHeight: 1.4, letterSpacing: 0.15em}
  body-md: {fontFamily: "Anuphan, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.8, letterSpacing: 0em}
  body-sm: {fontFamily: "Anuphan, sans-serif", fontSize: 10px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0em}
  caption: {fontFamily: "Anuphan, sans-serif", fontSize: 9px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1em}
  button-md: {fontFamily: "Anuphan, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.15em}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.footer-ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.status-highlight}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  metal-swatch-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs}"

## Components
**button-primary** renders the confirmed hover pattern (black background, white text) drawn directly from the `.button:hover` rule; the resting state is proposed as an outlined black-on-white treatment consistent with `.add-to-cart-button` borders.

**button-secondary** mirrors the inverse hover behavior observed on `.button-secondary:hover` (white background, black text), used for lower-emphasis actions like "view details" or wishlist toggles; resting styling is inferred from the shared button border pattern.

**text-input** is a proposed pattern for filter/search and account fields; no explicit input styling was captured, so padding and radius follow the site's generally low-radius, minimal aesthetic.

**nav-bar** reflects the measured `--header-padding: 26px` and the `.header-actions__text-style` 11px gray text; sticky/transparent-on-scroll behavior implied by `.header[transparent]` is noted but not visually confirmed.

**product-card** is a proposed grid tile using the light gray surface (#f2f2f2) as a neutral product-photography backdrop, appropriate for ring/diamond imagery; hover states (e.g., swap image, show quick-add) are not observed and are proposed.

**hero** uses the warm off-white (#f0efeb) as an inferred full-bleed section background for campaign or collection introductions; copy hierarchy and imagery layout are proposed, not measured.

**footer** adopts the dark navy (#0a142f) as an inferred footer background distinct from the mostly light UI, giving newsletter/legal content visual weight; column layout is proposed.

**badge** is a proposed status label (e.g., "New," "Limited," "Made to Order") using the orange highlight color observed in the palette; exact badge usage on the live site was not confirmed.

**search** is a proposed overlay/panel pattern for product discovery, styled with the light card surface and muted placeholder text; no search UI markup was present in the supplied evidence.

**metal-swatch-selector** is a category-appropriate proposed component for engagement-ring configuration (rose/white/yellow gold, platinum), using small circular swatches; colors, states, and interaction were not present in the evidence and are fully proposed.

## Responsive Behavior
Recommended breakpoints (proposed, not measured): mobile ≤480px, tablet 481–768px, desktop 769–1199px, wide ≥1200px. Suggest collapsing the nav-bar into a hamburger + drawer pattern below tablet, consistent with the presence of `.menu-drawer__close-button` and `#cart-drawer` in the evidence, though drawer visual behavior itself was not observed. Touch targets for buttons and swatches should maintain a minimum 44×44px hit area on mobile. Product-card grids are recommended to shift from multi-column desktop layouts to single or two-column mobile stacks; this is a general recommendation, not a measured layout change.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is derived from static CSS custom properties and selector fragments only; no rendered page, computed layout, or interaction was observed. Several color roles (status-success, status-alert, accent-info, footer-ink) are inferred from hex presence alone and may represent unrelated UI states (e.g., form validation, third-party embeds) rather than confirmed brand accents. Display-level typography sizes (display-xl, display-md) are proposed extrapolations since the only captured heading rule (h1 at 14px) is unusually small and likely a component-level label rather than a hero heading. The Assistant font family appears in the font-family list but no rule ties it to a specific element, so its actual usage and licensing status are unverified. Hover/focus states beyond the two explicitly captured button rules, mobile menu/drawer visuals, and all spacing/radius values not tied to a literal CSS declaration are proposed conventions rather than confirmed site behavior. Custom font hosting via Google Fonts was referenced in an `@import` fragment but weight/style availability and licensing terms were not verified.
