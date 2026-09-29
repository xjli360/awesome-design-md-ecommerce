---
version: alpha
name: "Polaroid"
source_url: "https://polaroid.com"
captured_at: "2026-09-29T04:07:25.134778+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Polaroid.com is confirmed as the brand's official US storefront, presenting
  its current camera, film, and printer catalog (I-2, Flip, Now+, Now, Go)
  under active merchandising and membership programs. The extracted palette
  centers on a near-black ink (#151515) used across alpha-blended overlays
  and a pure white canvas, with a dark neutral gray (#3d3d3d) suited to body
  copy. A cluster of saturated hues — orange, red, cyan/blue, yellow, and
  green — appears repeatedly in the raw palette; this is interpreted here as
  an evidenced "spectrum" accent set, echoing Polaroid's historic rainbow
  motif, rather than a single confirmed brand primary. Orange (#ff8200) is
  selected as the working primary accent for CTAs since it is the most
  frequent saturated hue in the sample, but this mapping is inferred, not
  measured from live component states.

  Typography relies on a custom sans display family (REAL_HEADER_OFFC, in
  Regular and Demibold weights) for body and heading text, a serif
  (SAOL_TEXT) apparently reserved for editorial or campaign moments, and a
  monospace (COMMIT_MONO) likely used for prices, SKUs, or technical labels.
  Only four body sizes (20/15/13/10px) and their tight negative
  letter-spacing are directly observed in CSS; all larger display sizes are
  proposed extrapolations for a photography-forward, image-led ecommerce
  layout with generous imagery and minimal chrome.

colors:
  primary: "#ff8200"
  ink: "#151515"
  canvas: "#ffffff"
  body: "#3d3d3d"
  muted: "#cccccc"
  hairline: "#e9e9e9"
  surface-soft: "#f8f8f8"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-red: "#d31f26"
  accent-cyan: "#27b4da"
  accent-yellow: "#ffb500"
  accent-green: "#78be20"
  accent-blue: "#198cd9"
  accent-crimson: "#d6001c"
  overlay-ink-50: "#15151580"
  overlay-ink-20: "#15151533"
typography:
  display-xl: {fontFamily: "REAL_HEADER_OFFC_DEMIBOLD, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "REAL_HEADER_OFFC_DEMIBOLD, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.4px"}
  title-md: {fontFamily: "REAL_HEADER_OFFC_REGULAR, sans-serif", fontSize: "20px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "-0.5px"}
  body-md: {fontFamily: "REAL_HEADER_OFFC_REGULAR, sans-serif", fontSize: "15px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "-0.28px"}
  body-sm: {fontFamily: "REAL_HEADER_OFFC_REGULAR, sans-serif", fontSize: "13px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "-0.21px"}
  caption: {fontFamily: "REAL_HEADER_OFFC_REGULAR, sans-serif", fontSize: "10px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "-0.125px"}
  button-md: {fontFamily: "REAL_HEADER_OFFC_DEMIBOLD, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.0, letterSpacing: "0.5px"}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
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
    textColor: "{colors.ink}"
    priceTypography: "{typography.title-md}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.overlay-ink-50}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    hairlineColor: "{colors.overlay-ink-20}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    backgroundColor: "{colors.canvas}"
    swatchColors: ["{colors.accent-red}", "{colors.accent-cyan}", "{colors.accent-yellow}", "{colors.accent-green}", "{colors.accent-blue}", "{colors.primary}"]
    activeBorderColor: "{colors.ink}"
    rounded: "{rounded.full}"
    labelTypography: "{typography.caption}"

## Components
button-primary is the main commerce action (Shop Now, Add to Bag), rendered in the orange accent against white text; this color choice is inferred from frequency in the palette rather than a confirmed CTA screenshot. button-secondary is a lower-emphasis outline variant, useful for "Learn More" or filter toggles, using ink-on-white with an ink border; hover/focus states are proposed, not observed.

text-input covers newsletter and account fields, using the soft off-white surface and hairline border seen in the palette for subtle field separation; focus and error states are proposed since no interaction states were captured.

nav-bar reflects the category mega-menu structure visible in the text content (Cameras, Film, Printers, Accessories, Journal), set on white with ink text and a hairline base to separate it from content; sticky/scroll behavior is proposed.

product-card is the core catalog unit for camera and bundle listings ("Now+ Generation 3 Starter Set", etc.), pairing a card surface tone with a prominent price line and small caption for bundle callouts like "Free Film Pack"; badge overlays and stock states are proposed.

hero supports full-bleed campaign moments such as the Pokémon collaboration banner, using the near-black ink as a base with a semi-transparent overlay so imagery remains legible under large display type; exact hero imagery and cropping were not observed.

footer groups navigation, social, and legal links on the dark ink background with reduced-opacity dividers drawn from the observed alpha tokens; this mirrors the multi-column footer structure implied by the page's link inventory.

badge is a small pill for merchandising flags (e.g., savings or bundle callouts), using one accent color from the spectrum set; multiple badge colors could rotate across accent hues, which is a proposed pattern.

search is a rounded, low-contrast input intended for the product/camera finder tools mentioned in navigation (Camera Finder, Product Finder); its full-width mobile behavior is proposed.

color-swatch-selector is a category-specific component for choosing a camera's color/finish, using the observed saturated accent hues as literal swatch fills — a reasonable proposed use given Polaroid cameras are commonly sold in color variants, though no live swatch markup was captured in this evidence.

## Responsive Behavior
Recommended, not measured, breakpoints:

| Breakpoint | Width      | Layout notes (proposed)                          |
|-----------|------------|---------------------------------------------------|
| mobile    | <480px     | Single-column stack, collapsed hamburger nav      |
| tablet    | 480–1024px | 2-column product grid, condensed nav labels       |
| desktop   | 1024–1440px| Full mega-menu, 3–4 column product grid           |
| wide      | >1440px    | Max-width content container, extra hero padding   |

Touch targets should be at least 44px for buttons and nav items. The mega-menu (Cameras/Film/Printers/Accessories) should collapse into an accordion on mobile; the camera color-swatch selector should remain thumb-reachable near the bottom of the product image on small screens. None of this is measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS module rules, a text/DOM excerpt, and a color/font inventory only; no rendered screenshots, computed layout, or interaction states (hover, focus, open menu, mobile breakpoints) were observed. The mapping of specific hex values to semantic roles (primary, muted, hairline, surface tones) is inferred from naming context and frequency, not confirmed usage in a live component. All display-size typography values and the button-md style are proposed extrapolations beyond the four directly observed body font sizes. Custom font availability, licensing, and actual rendering of REAL_HEADER_OFFC, SAOL_TEXT, and COMMIT_MONO were not verified beyond their declared font-family names. The "spectrum" accent grouping and color-swatch-selector component are reasonable but unverified interpretations of the palette's multiple saturated hues.
