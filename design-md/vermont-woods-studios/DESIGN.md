---
version: alpha
name: "Vermont Woods Studios"
source_url: "https://vermontwoodsstudios.com"
captured_at: "2026-09-28T09:50:53.740191+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Vermont Woods Studios sells American-made solid-wood furniture, and the observed
  CSS points to an earthy, editorial palette layered over a standard Shopify (Dawn-
  derived) component system. The deepest, most repeated brand color is a forest
  green (#1c685b, reinforced by nearby #155a4e and #263a2f), which this spec treats
  as the inferred primary brand color, paired with near-black green (#1f2723) for
  ink and warm off-white/cream tones (#ece5df, #e9dfd6, #d9cdc2) for soft surfaces
  that echo raw wood and paper catalog stock. A saturated blue (#1990c6/#136f99)
  appears only on the Shopify-generated accelerated-checkout button and is mapped
  to a link/checkout accent rather than the core brand identity. A red (#b91c1c) is
  reserved for sale/clearance badges given the "20% Off" promotional copy. Typography
  combines "Proza Display" for large display headings, "Proza Libre" for body and
  sub-headings, and "Work Sans" for compact UI chrome (explicitly set on a footer
  button at 12px/600). Root font-size scaling could not be verified from the
  evidence, so pixel equivalents for rem-based prose tokens are inferred assuming a
  common 62.5% base, and are flagged accordingly. Rounded corners default to 0px per
  the observed payment-button variable and are extended conservatively elsewhere.

colors:
  primary: "#1c685b"
  ink: "#1f2723"
  canvas: "#ffffff"
  body: "#212529"
  muted: "#767676"
  hairline: "#dedede"
  surface-soft: "#ece5df"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  accent-mint: "#1fce9c"
  wood-tone: "#5f3a2c"
  wood-deep: "#3c3022"
  surface-warm: "#e9dfd6"
  link-blue: "#1990c6"
  link-blue-hover: "#136f99"
  alert: "#b91c1c"
  border-strong: "#a5a5a5"
typography:
  display-xl: {fontFamily: "'Proza Display', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Proza Display', sans-serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Proza Libre', sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'Proza Libre', sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.44, letterSpacing: 0.6px}
  body-sm: {fontFamily: "'Proza Libre', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.4px}
  caption: {fontFamily: "'Work Sans', sans-serif", fontSize: 12px, fontWeight: 600, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "'Work Sans', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    overlayColor: "#0000000a"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-mint}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  material-swatch:
    backgroundColor: "{colors.surface-warm}"
    borderColor: "{colors.wood-tone}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs}"

## Components

**button-primary** is the core call-to-action style (e.g. "Shop Bedroom Sets", "Add to Cart"), using the inferred forest-green primary against white text with sharp 0px corners, matching the observed default border-radius on the Shopify accelerated-checkout button. Hover/active/disabled states are proposed, not observed.

**button-secondary** provides an outlined variant for lower-emphasis actions (e.g. "Continue shopping"), reusing the primary color as border/text on a white background, consistent with the theme's `.button--secondary` CSS pattern of swapping background/text roles.

**text-input** covers cart notes, search, and account fields; a light hairline border and white background were inferred from the general light/neutral palette, since no explicit input styling was captured.

**nav-bar** represents the mega-menu header (Bedroom, Dining, Office & Living, Outdoor, etc.); a white background with dark-ink text is proposed based on the light overall palette, with a hairline divider beneath it. Sticky/scroll behavior is not observed.

**product-card** models catalog and collection tiles, with a soft off-white/card surface, hairline border, and a title/price typography pairing drawn from the prose heading and body sizes. Image aspect ratio and hover states are proposed.

**hero** models the homepage banner where an observed CSS rule explicitly sets an `h1` to white (#ffffff) inside a themed section, implying a dark or photographic background; ink-dark is used as a placeholder background since no image data was supplied.

**footer** uses the same dark ink background as the hero for visual continuity (proposed, not confirmed identical), with the mint accent for links and the Work Sans family for the observed newsletter/footer button (12px/600/0.5px tracking, directly evidenced).

**badge** supports promotional labels like "20% Off Select Bedroom Sets," using the one clearly non-brand, high-alert red in the palette; this role assignment is inferred from the presence of both the red hex and matching promotional copy.

**material-swatch** is a category-appropriate addition for a woodworking retailer, representing small circular selectors for wood species (Cherry, Walnut, Maple, Oak) referenced in the navigation; colors are proposed using the warm cream surface and a wood-brown border, as no literal swatch CSS was captured.

## Responsive Behavior
This is a recommendation based on standard e-commerce patterns, not measured site behavior:

| Breakpoint | Range | Layout guidance |
|---|---|---|
| mobile | <600px | Single-column product grid, collapsed hamburger nav, sticky "Add to Cart" bar |
| tablet | 600–1024px | 2-column product grid, mega-menu collapses to accordion |
| desktop | 1024–1440px | 3–4 column product grid, full horizontal mega-menu |
| wide | >1440px | Max-width content container (~1440px), extra whitespace at edges |

Touch targets should be at least 44×44px for nav and cart controls. The multi-level mega-menu (Bedroom/Dining/Office & Living/Outdoor with many sub-categories) should collapse into a nested accordion below tablet width; no actual collapse mechanism was observed in the supplied CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived entirely from static CSS/text extraction; no rendered page, computed styles, or interaction states were observed. Root font-size (assumed 62.5%) used to convert rem-based prose tokens to pixels is inferred, not confirmed, so all derived body/heading pixel sizes are approximate. The mapping of `--font-body-family` and `--font-heading-family` to specific families (Proza Libre / Proza Display) is inferred from typical theme conventions, not explicitly evidenced in the supplied rules. Hover, focus, active, and disabled states for buttons, inputs, and cards are proposed defaults, not captured from live interaction. Mobile menu behavior, breakpoints, and collapse thresholds are proposed, not measured. Custom font licensing/availability (Proza Display, Proza Libre, Work Sans) was not verified and should be confirmed before production use. Several supplied colors (grays, alpha values) were treated as generic UI/system tones rather than brand colors due to lack of stronger contextual signal.
