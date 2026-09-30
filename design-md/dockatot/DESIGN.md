---
version: alpha
name: "DockATot"
source_url: "https://eu.dockatot.com/"
captured_at: "2026-09-29T03:59:17.635624+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from the DockATot EU Shopify storefront, a
  baby-gear retailer selling the Deluxe+ Dock lounger and its interchangeable
  fabric covers. The supplied CSS is dominated by Shopify theme scaffolding
  (Flickity carousels, PhotoSwipe galleries, accelerated-checkout wallet
  buttons) rather than a bespoke component library, so most role assignments
  below are inferred rather than directly observed on rendered pages.
  The palette leans warm and neutral — a cream canvas (#fffaf6), near-black
  ink tones (#150f12, #141012), and muted greys (#747374, #656565) — which
  suits soft nursery photography and fabric swatches. A cluster of dusty
  sand/olive tones (#968d79, #7c6b47, #cecac0, #b3ad9e) and quiet teal-greens
  (#669b94, #86c8bc, #3fc3aa) likely originate from product swatch imagery
  (e.g. "Sand Chambray", "Celestial Blue") rather than fixed UI chrome, so
  they are treated here as accent/secondary options. The only CSS-confirmed
  interactive color pair is the accelerated-checkout button (#1990c6 default,
  #136f99 hover, white text), which is adopted as the primary action color
  in the absence of a directly observed "Add to Cart" button style.
  Typography stacks include Montserrat, Open Sans, and Avenir/Avenir Next
  alongside system fallbacks; a fluid multi-tier font-size scale (10px–151px
  across three responsive sets) is used to derive the proposed type scale.
  Rounded corners are mostly square in confirmed theme rules (0px on
  model-viewer buttons) with a 50% circular treatment on carousel nav
  controls; other radii are proposed for consistency.

colors:
  primary: "#1990c6"
  primary-hover: "#136f99"
  ink: "#150f12"
  canvas: "#fffaf6"
  body: "#3a3a3a"
  muted: "#747374"
  hairline: "#dedede"
  surface-soft: "#f7f6f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sand: "#968d79"
  accent-clay: "#7c6b47"
  accent-navy: "#113049"
  accent-teal: "#3fc3aa"
  accent-error: "#d02e2e"
  accent-success: "#56ad6a"
  accent-blush: "#dd7975"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: "46px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: "31px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: "22px", fontWeight: 500, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "Open Sans, Avenir, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Open Sans, Avenir, sans-serif", fontSize: "13.5px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Open Sans, Avenir, sans-serif", fontSize: "11.5px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.3px"}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: "13.5px", fontWeight: 500, lineHeight: 1, letterSpacing: "0.5px"}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    overlay: "rgba(0,0,0,0.2)"
    titleTypography: "{typography.display-xl}"
    ctaSpacing: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: "{spacing.lg}"
    gap: "{spacing.xs}"

## Components

**button-primary** is proposed for the main commerce action (e.g. Add to Cart, Shop Now). Its color derives from the only CSS-confirmed interactive button pair on the site, the accelerated-checkout wallet button (`#1990c6` → `#136f99` hover), applied here to a standard flat button since no bespoke "add to cart" style was captured in the evidence. States: default, hover (`primary-hover`), and a disabled/sold-out state (proposed, using `muted` background and reduced opacity).

**button-secondary** is an outline treatment for tertiary actions like "View slide" or filter toggles, using the hairline border and ink text. Hover/focus states (background tint, darker border) are proposed, not observed.

**text-input** covers search and account form fields. Border, background, and padding are inferred from generic Shopify theme conventions; no focus-ring color was present in the evidence, so a focus state using `primary` at reduced opacity is proposed.

**nav-bar** represents the persistent top navigation seen in the page text (Bestsellers, Deluxe+ Docks, Deluxe+ Covers, Dock Safety Tips, My Account, Search, Cart). A transparent/overlay variant is suggested by the presence of `--COLOR-NAV-TEXT-TRANSPARENT` and a header gradient variable in the evidence, implying the nav can sit over a hero image before scroll; this behavior is inferred, not measured.

**product-card** models the repeated dock/cover listings (image, swatch numbers 1–4, title, price, Add to Cart). Card background and border use neutral surface/hairline tokens; the numbered swatch indicators map to the proposed `color-swatch-selector` component.

**hero** represents the top banner ("The Original Baby Lounger" / "Shop Deluxe+ Dock") with a dark overlay gradient value found in the CSS (`rgba(0,0,0,0.2)`), suggesting text is meant to sit on photographic imagery with a scrim for legibility.

**footer** is proposed as a darker contrast band using the observed navy (`#113049`) to separate "Help & Support" and "Company" link columns from the main content, though the actual observed footer background was not directly confirmed in the CSS sample.

**badge** covers "Sold Out" and sale/status labels; `accent-error` (`#d02e2e`) is reused here since it appears in the palette and is thematically consistent with stock-status messaging, though its literal CSS usage target was not confirmed.

**search** and **color-swatch-selector** are category-appropriate additions: search reflects the visible "Search" nav entry, and the swatch selector reflects the repeated numbered variant pickers (1/2/3/4) shown against each Dock/cover product in the page text.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | < 480px | Single-column product grid, nav collapses to hamburger + icons |
| Tablet | 481–768px | 2-column product grid, condensed nav labels |
| Desktop | 769–1024px | 3-column product grid, full nav visible |
| Wide | ≥ 1025px | 4-column product grid (matches 4-swatch pattern seen in listings) |

Touch targets should be a minimum of 44px in line with common accessibility guidance, applied to swatch selectors, carousel arrows (observed at 36px and likely enlarged on touch), and nav icons. This table is a recommendation based on typical Shopify theme conventions and the fluid font-size tiers present in the CSS; it is **not** measured from actual rendered breakpoints or device testing.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted statically from CSS/text; no rendered layout, scroll, or JS-driven carousel/gallery (Flickity, PhotoSwipe) behavior was observed.
- The primary action color (`#1990c6`/`#136f99`) is confirmed only for the Shopify accelerated-checkout wallet button, not for a standard "Add to Cart" button; its use as the general `primary` token is an inference.
- Sand/olive/teal palette entries likely originate from product swatch photography rather than fixed UI chrome; their promotion to named accent tokens is interpretive.
- Font-role assignment (Montserrat for display/headings, Open Sans/Avenir for body) is inferred from the available family list; no explicit selector-to-family mapping was supplied. The presence of "Shippori Mincho" in the font list is unexplained and not assigned a role.
- All font sizes are derived from three overlapping `:root` fluid-scale variable sets; exact breakpoint-to-scale mapping is not confirmed.
- Border-radius values are mostly proposed; only `0px` (model-viewer buttons) and `50%` (carousel nav) were directly observed.
- Mobile nav collapse, focus states, form validation styling, and footer background color were not directly observed in the supplied CSS.
- Custom font licensing/self-hosting status for Montserrat/Open Sans/Avenir was not verified from the evidence.
