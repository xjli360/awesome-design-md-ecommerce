---
version: alpha
name: "Fly By Jing"
source_url: "https://flybyjing.com"
captured_at: "2026-09-28T04:32:27.243147+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  The evidence shows a Shopify-based storefront defining two literal font stacks:
  a monospace heading stack (SFMono-Regular, Menlo, Consolas, Monaco, Liberation
  Mono, Courier New, monospace) set to uppercase with normal weight and zero
  letter-spacing, and a system-ui/sans-serif body stack. This produces a
  utilitarian, label-like heading voice (echoing the all-caps "SHOP THE BEST
  CHINESE CHILI SAUCE" title) paired with plain, legible body text — a
  packaging-and-pantry aesthetic rather than an editorial one. The hex palette
  is dominated by a saturated red-orange (#f9423a), supported by a dark
  navy-ink (#272d45), muted blue-gray (#676986), and soft off-white surfaces
  (#f9f9f9, #f4f4f6, #fafafa). Accent hues — magenta (#cb44c2), warm gold
  (#ffb829, #ffc968), and bright yellow (#ffe431) — appear alongside the CSS
  custom-property color-scheme system, which defines many high-contrast
  section themes (green, magenta, purple, black, yellow); this multi-scheme
  structure is treated as inferred evidence of section-level theming rather
  than a single fixed brand palette. Roles below (ink, muted, hairline,
  surface tiers) are inferred assignments from the closest matching observed
  hexes, not confirmed computed styles.

colors:
  primary: "#f9423a"
  ink: "#1c1c1c"
  canvas: "#ffffff"
  body: "#272d45"
  muted: "#676986"
  hairline: "#dedede"
  surface-soft: "#f9f9f9"
  surface-card: "#f4f4f6"
  on-primary: "#ffffff"
  accent-magenta: "#cb44c2"
  accent-blue: "#384ec5"
  accent-gold: "#ffb829"
  accent-yellow: "#ffe431"
  accent-peach: "#ffc968"
  alert: "#f92020"
  deep-black: "#121212"
  pale-cream: "#fff2d4"
  divider-lavender: "#d3d4dd"
typography:
  display-xl: {fontFamily: "SFMono-Regular, Menlo, Consolas, monospace", fontSize: "56px", fontWeight: 400, lineHeight: 1.05, letterSpacing: "0px", textTransform: "uppercase"}
  display-md: {fontFamily: "SFMono-Regular, Menlo, Consolas, monospace", fontSize: "40px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "0px", textTransform: "uppercase"}
  title-md: {fontFamily: "SFMono-Regular, Menlo, Consolas, monospace", fontSize: "24px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "0px", textTransform: "uppercase"}
  body-md: {fontFamily: "system-ui, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "system-ui, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "system-ui, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "SFMono-Regular, Menlo, Consolas, monospace", fontSize: "14px", fontWeight: 400, lineHeight: 1, letterSpacing: "0.5px", textTransform: "uppercase"}
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    borderColor: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.deep-black}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
    borderColor: "{colors.hairline}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  spice-level-indicator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components
**button-primary** uses the observed saturated red-orange (`#f9423a`) as a high-visibility call-to-action fill with white text, matching the monospace/uppercase button convention implied by `--heading-font-stack` and `--heading-capitalize`. **button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Learn More"), reusing the ink color for border and text. **text-input** is proposed with a light hairline border and white background, sized for form fields such as search or newsletter signup; focus/error states are not observed and are proposed only. **nav-bar** assumes a white background with dark ink text and monospace uppercase labels, consistent with the heading font-stack variables, though actual header layout was not observed. **product-card** proposes a soft off-white surface (`#f4f4f6`) with rounded corners for grid-based sauce/condiment listings; hover and quick-add states are not observed and are proposed. **hero** reuses the primary red-orange as a bold section background with large uppercase display type, inferred from the multi-scheme CSS variables suggesting saturated full-bleed banners. **footer** is proposed in near-black (`#121212`) with white text for a grounded closing section, distinct from the vivid scheme colors used higher on the page. **badge** and **spice-level-indicator** are category-appropriate proposed components for condiment merchandising (e.g., "New," "Extra Spicy"), using the warm gold and primary accent colors observed in the palette; neither element nor its copy was directly observed in the supplied evidence.

## Responsive Behavior
This is a proposed breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Behavior |
|---|---|---|
| Mobile | <600px | Single-column stacking; nav collapses to a hamburger/menu icon; product-card grid becomes 1–2 columns. |
| Tablet | 600–1024px | 2–3 column product grid; nav-bar remains horizontal with condensed spacing. |
| Desktop | 1024–1820px | Full multi-column layouts up to the observed `--max-site-width: 1820px`. |
| Wide | >1820px | Content remains capped at `--max-site-width`, centered with surrounding whitespace. |

Touch targets should be at least 44px in height for buttons and nav items; mobile menus and filters are assumed to collapse into drawers or accordions, but this interaction pattern was not observed in the supplied static evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS custom properties and a color/font extraction, not from rendered page observation. Specific mappings — such as which hex applies to body copy versus muted text, or which color-scheme variable (scheme1–scheme6, plus several UUID-named schemes) applies to which page section — are inferred, not confirmed. Font sizes, weights beyond the declared `400`, and letter-spacing values beyond the declared `0.0` for headings are proposed defaults, not measured. Payment-brand icon colors (e.g., Visa blue, Mastercard red/orange, PayPal blues) present in the raw palette were excluded from role assignment as non-brand. Interaction states (hover, focus, active, disabled) and mobile/collapsed navigation behavior were not observed and are proposed only. The presence of unusual font names in the evidence (e.g., JeanLuc, Publico, SimHei) suggests additional typefaces may be used elsewhere on the site, but no corresponding CSS rule was supplied to confirm their role, so they are omitted from this specification; their licensing and availability are unverified.
