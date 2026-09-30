---
version: alpha
name: "Wemax"
source_url: "https://wemax.com"
captured_at: "2026-09-28T10:17:43.612399+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Wemax's storefront (Shopify-based) is built on a restrained near-monochrome
  foundation: pure white (#ffffff) canvas paired with near-black ink
  (#171717, matching the theme's `--color-foreground` token) and a stepped
  series of dark neutrals (#1c1c1c, #1f1f1f, #232323, #2b2b2b, #333333,
  #121212) used across text, dark sections, and overlays. Light hairlines
  and surfaces come from #dedede and #e5e5e5. A semi-transparent white
  (#ffffffbf) appears on frosted UI chrome such as the lightbox/gallery
  buttons (`backdrop-filter: blur`). The wide burst of saturated hues in the
  raw palette (Facebook blue, Pinterest red, WhatsApp green, Mastercard's
  red/orange, PayPal blue, etc.) are third-party social-share and payment
  icon colors, not brand color — they are intentionally excluded from the
  interpreted brand palette below and are only referenced as
  "social/payment icon" swatches if needed. Typography is anchored on
  Inter as the observed sans-serif; a monospace stack (SFMono/Menlo/
  Consolas fallbacks) is present in the CSS and is inferred here as a
  numeric/price treatment rather than a body font. All pixel sizes below
  are proposed unless explicitly present as CSS custom properties; the
  theme's fluid `clamp()` heading tokens confirm a scaling display type
  system, which this spec approximates with fixed reference sizes.

colors:
  primary: "#171717"
  ink: "#171717"
  canvas: "#ffffff"
  body: "#232323"
  muted: "#333333"
  hairline: "#dedede"
  surface-soft: "#e5e5e5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  surface-dark: "#121212"
  overlay-glass: "#ffffffbf"
  overlay-scrim: "#00000000"
typography:
  display-xl: {fontFamily: "Inter, sans-serif", fontSize: 56px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Inter, sans-serif", fontSize: 40px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Inter, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.3px"}
  price-mono: {fontFamily: "SFMono-Regular, Menlo, Consolas, monospace", fontSize: 18px, fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-mono}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.overlay-scrim}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  feature-hotspot:
    backgroundColor: "{colors.overlay-glass}"
    dotColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs}"

## Components

**button-primary** is the dark, near-black call-to-action ("Add to cart", "Subscribe") matching the theme's `--color-foreground` token; solid fill with white text signals highest-priority actions like purchasing or bundle building.

**button-secondary** is an outline/ghost treatment for lower-priority actions (e.g., "Continue shopping", "View full details"), using the same ink color as text on a white field bordered by the light hairline gray — a proposed pairing, not a captured hover/active state.

**text-input** covers newsletter, discount-code, and search fields; a thin hairline border on white with body-sized text is inferred from typical Shopify Dawn-family input styling implied by the theme's CSS variable structure.

**nav-bar** is the sticky/top navigation containing the WEMAX wordmark, category links (Laser TV, Projector, Screen, Refurbished, Support), search, account, and cart icons on a white background — spacing and exact height are proposed from the `--topbar-height` tokens present in CSS.

**product-card** represents catalog and bundle-builder tiles (e.g., Nova Pro, VP04) showing image, title, star rating, and price; the price uses the observed monospace font stack as an inferred numeric treatment distinct from body copy.

**hero** models the homepage slideshow ("Turn Any Room into a True Home Theater") — large display type over a dark or image background with a scrim, sized against the theme's fluid `--title-xl` clamp tokens; exact imagery and motion are not verifiable from static CSS.

**footer** groups newsletter signup, social icons, and utility links (FAQ, Track my order, Contact) on a dark surface, echoing the dark neutral tokens seen elsewhere in the theme.

**badge** covers promotional labels such as "Save 46%" or "Sale" pills on product cards; pill shape uses the confirmed `--rounded-full` token from the lightbox button CSS, reused here for brand consistency.

**search** is the expandable/modal site search seen in the nav ("Search Site navigation"); soft-gray pill field is a proposed pattern, not a measured overlay.

**feature-hotspot** is a category-specific component modeling the interactive product-image markers evidenced by `--hotspot-x/--hotspot-y/--hotspot-color` variables tied to `shopify-block-product` — small glass-effect dots that likely reveal feature callouts on hover/tap; the reveal interaction itself is inferred, not observed.

## Responsive Behavior
Recommendation only — no live breakpoints were measured.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <640px | Single-column hero/product grid; nav collapses to hamburger + icon cluster |
| Tablet | 640–1024px | 2-column product grid; sticky nav remains horizontal |
| Desktop | 1024–1280px | 3–4 column grids; `--page-container` caps near 1280px per CSS |
| Wide | >1280px | Content capped at `--page-width`; side padding grows via `--page-padding` |

Touch targets should be ≥44px for cart, nav icons, and hotspot dots. Search and cart drawers are assumed to collapse into slide-in panels on mobile, consistent with common Shopify theme conventions, but this behavior is not confirmed from the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This spec is derived from static CSS custom properties, a text excerpt, and a flat color/font list — no rendered layout, computed styles, hover/focus states, or JavaScript-driven interactions were observed. Numeric `--sp-*` spacing values referenced in the source CSS (e.g., `sp-12`, `sp-14`, `sp-23`) could not be resolved to exact pixel values, so all spacing and typography sizes above are proposed approximations, not extracted figures. The large set of saturated colors in the supplied palette are attributed to third-party social/payment iconography rather than brand identity; this inference could be wrong if any are in fact used as accent colors elsewhere on the site. Font licensing/self-hosting status for Inter is not verified. Mobile menu structure, cart-drawer behavior, and hotspot hover/tap interactions are assumed from naming conventions only and are not confirmed observations.
