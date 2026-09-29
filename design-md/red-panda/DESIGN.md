---
version: alpha
name: "Red Panda"
source_url: "https://www.redpandalab.com"
captured_at: "2026-09-29T03:56:52.378728+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Red Panda Lab's storefront runs on a BigCommerce Stencil theme with a
  restrained black-and-white base punctuated by a single saturated red
  accent (#e3001d) used for primary buttons, links, and required-field
  markers. Body text and headings share Roboto at a near-black ink
  (#1a1718) on white canvas, with a hover state that darkens the red to
  #d1001b. A secondary lime-green accent (#a6c832, hovering to #819b27)
  appears on alert-context buttons, and a burnt-orange (#ef682d) marks
  required-field asterisks — both are treated here as rare, functional
  accents rather than brand primaries. Grays across the palette (#8d8b8c,
  #727272, #f8f3f4, #fafafa, #e8e8e8) are inferred as disabled, muted-text,
  and soft-surface roles since no explicit semantic class ties them to a
  single purpose. Karla and Montserrat are present in the loaded font
  stack but no captured rule assigns them a role, so they are treated as
  available but unverified secondary faces; Roboto is the only family with
  confirmed body/heading/button usage. The interpretation favors a
  compact, technical, slightly industrial aesthetic befitting effects
  pedals: sharp 3px button radii, uppercase tracked button labels, and
  minimal ornamentation, extended here into card, nav, and product-detail
  patterns not directly observed on the live site.

colors:
  primary: "#e3001d"
  primary-hover: "#d1001b"
  ink: "#1a1718"
  canvas: "#ffffff"
  body: "#1a1718"
  muted: "#8d8b8c"
  hairline: "#e8e8e8"
  surface-soft: "#f8f3f4"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-green: "#a6c832"
  accent-green-hover: "#819b27"
  accent-orange: "#ef682d"
  disabled: "#727272"
  overlay-light: "#dddddd"
typography:
  display-xl: {fontFamily: "Roboto, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Roboto, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Roboto, sans-serif", fontSize: 28px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.666, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.02em}
  button-md: {fontFamily: "Roboto, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.1em}
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
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.overlay-light}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  audio-demo-player:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"

## Components

**button-primary** maps directly to the observed `.button-primary` rule: red (#e3001d) fill, white text, 3px radius, uppercase tracked Roboto label, darkening to #d1001b on hover/focus per the captured CSS. This is the confirmed primary call-to-action pattern (Add to Cart, checkout actions).

**button-secondary** mirrors the observed `.account-button-secondary`/`.button-secondary` pair: white fill, red text and border, inverting to solid red on hover. Proposed for lower-emphasis actions like "View details" or "Compare."

**text-input** is inferred from general Stencil form conventions; no explicit input border color was captured, so the hairline gray (#e8e8e8) is a proposed border with white fill and standard body typography.

**nav-bar** is proposed: white background, dark ink text, hairline bottom border, reflecting the site's flat header/mega-menu structure implied by the "PRODUCTS / COMPANY / ARTISTS / DEALERS / SUPPORT" text list, though exact nav styling was not captured in CSS.

**product-card** is proposed for pedal listing tiles (e.g., RD-1 Pitch Delay, Radius, Particle 2), using the light #fafafa surface and hairline border to separate cards on a white page background, since product-grid CSS itself wasn't in the evidence.

**hero** is proposed for the homepage "Explore New Sound" banner, using dark ink as a full-bleed background with white display type, an inference since only text content ("Explore New Sound") was observed, not hero styling.

**footer** is proposed using the dark ink background with light gray text, consistent with typical BigCommerce Stencil footer patterns and the site's link-heavy footer content (Categories, Instagram/Facebook/Twitter, payment icons), though footer colors were not directly in the CSS sample.

**badge** is proposed for labels like "2" counters seen next to product names (Bitmap 2, Context 2) or a "New" flag, using the orange accent already tied to required-field emphasis, repurposed here as an attention color.

**search** is proposed for the site search field referenced by "0 results found for 'undefined'" text, using the soft pink-tinted surface (#f8f3f4) observed elsewhere as a background treatment.

**audio-demo-player** is a category-appropriate addition for guitar-pedal demo audio/video embeds (the site references "Videos"), styled as a neutral card with the red primary as a functional accent for play/progress controls — entirely proposed, no player markup was in evidence.

## Responsive Behavior

Recommended breakpoints (not measured from the live site):

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| Mobile | <600px | Single-column product grid, collapsed hamburger nav, stacked hero text |
| Tablet | 600–959px | 2-column product grid, condensed nav links |
| Desktop | 960–1279px | 3–4 column product grid, full horizontal nav |
| Wide | ≥1280px | Max-width content container, generous section spacing |

Touch targets should maintain a minimum 44×44px hit area for buttons and nav items; the primary/secondary button padding tokens above satisfy this at default font sizes. Mobile nav is assumed to collapse into a drawer or accordion below the tablet breakpoint. This table is a design recommendation only, not an observation of the site's actual responsive implementation.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was drawn from static CSS extraction and homepage text only; no rendered layout, computed styles, or interaction states (focus rings, active states, form validation) were observed.
- Karla and Montserrat appear in the loaded font stack but no captured selector assigns them a role; their use is unverified and excluded from the typography scale.
- The `pxu` font is assumed to be an icon font and is not used for text typography here.
- All pixel sizes in the typography scale beyond the two directly measured heading rules (1.54286rem, 1.71429rem) are proposed approximations, not extracted values.
- Component definitions for nav-bar, hero, footer, product-card, search, and audio-demo-player are inferred patterns based on page text and category convention, not captured selectors.
- Color-to-role mapping for neutral grays (hairline, surface-soft, surface-card, disabled) is inferred from partial rule context, not a documented style guide.
- Mobile/responsive behavior and breakpoints are recommendations only; no media queries were included in the supplied evidence.
- Font licensing/self-hosting status for Roboto, Karla, and Montserrat was not verified from the supplied evidence.
