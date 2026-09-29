---
version: alpha
name: "Soldano"
source_url: "https://www.soldano.com"
captured_at: "2026-09-29T04:01:37.442041+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Soldano's storefront runs on a WooCommerce/Divi stack whose observed CSS is
  dominated by pure black (#000000) and white (#ffffff), with body copy set
  in a mid-grey (#595959) and secondary chrome (top bar, links) in a lighter
  grey (#969696). A single hairline grey (#eeeeee) separates header regions,
  and WooCommerce action buttons are explicitly black with square corners
  (border-radius: 0), uppercase labels, and 1px letter-spacing — a deliberate,
  workshop/industrial tone fitting a hand-built tube-amp brand. Font stacks
  reference Poppins and Roboto ahead of system sans-serif fallbacks; role
  assignment (Poppins for display, Roboto for body/UI) is inferred from
  ordering, not confirmed via computed styles. Supporting greys (#f2f2f2,
  #fafafa, #444444) and one recurring interactive accent (#9999ff, seen on a
  "load more" hover state) round out the palette; brighter block-editor
  swatches present in the raw palette are treated as unused defaults, not
  brand colors. This spec proposes a restrained black/white/grey system with
  square, high-contrast controls, leaving spacing, radii, and most component
  states as reasoned proposals rather than measured observations.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#595959"
  muted: "#969696"
  hairline: "#eeeeee"
  surface-soft: "#fafafa"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  secondary-dark: "#32373c"
  accent-hover: "#9999ff"
  input-text: "#444444"
  border-generic: "#cccccc"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Roboto, Helvetica Neue, Arial, sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 1px}
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
    backgroundColor: "{colors.secondary-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.input-text}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    priceColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg} {spacing.base}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.muted}"
    headingColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.input-text}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border-generic}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"

## Components

**button-primary** mirrors the WooCommerce submit-button rule directly observed in the CSS: black background, white text, zero border-radius, uppercase tracking. Used for "Add to cart," "Buy Now," and checkout actions.

**button-secondary** is drawn from the theme's default `.wp-element-button` rule (`#32373c` background, white text). Proposed for lower-emphasis actions like "Read more" or "Find out more" links, since no distinct secondary style was captured beyond this default.

**text-input** is a proposed pattern for account, newsletter, and checkout fields. It borrows the `#444` input-text color seen on the search field and pairs it with the observed hairline grey for borders; exact padding/radius are not confirmed and are set to reasonable defaults.

**nav-bar** reflects the confirmed black background of `#main-header` and `#top-header`, with the muted grey (`#969696`) used for top-bar link color and white reserved for active/primary nav items. Hover and open-state treatments are proposed, not observed.

**product-card** generalizes the mini-cart product row styling (`.xoo-wsc-product`, 20px/15px padding, transparent-to-light background) into a full storefront grid card, approximated against the spacing scale since exact pixel values weren't a clean match.

**hero** is a proposed composition for feature banners such as the "SLO PLUS" and "SLO-100" promotional sections described in the page text — full black background, large display type, and a primary-button CTA. No hero layout, image treatment, or breakpoint behavior was actually measured.

**footer** infers a black background consistent with the header/top-header rules, muted-grey body text, and white headings for widget titles, matching the `#main-footer` heading-color rule captured in evidence. Column structure and newsletter form layout are proposed.

**badge** is an inferred small-label component for merchandising callouts (e.g., "Special Offer," "New") using the one clearly interactive accent color (`#9999ff`) found in the evidence (a load-more hover state), repurposed here as a static highlight since no dedicated badge color was observed.

**search** reuses the `#444` text-color rule from the slide-in menu search input, placed on a white field with hairline border; icon and autocomplete-dropdown styling are not evidenced and are omitted.

**configurator-panel** is a category-specific, proposed component modeling the site's described "Custom Shop" flow (choosing Tolex, grillcloth, panel, and voltage options before purchase). It uses the light surface and generic border grey with body-sm copy for option labels; no actual configurator markup or interaction was captured in evidence.

## Responsive Behavior

Proposed breakpoints (not measured from the live site): mobile ≤480px, tablet 481–1024px, desktop ≥1025px, aligned loosely to the theme's `--wp--style--global--content-size` (823px) and `--wide-size` (1080px) tokens, which suggest a content column near 823px and a wide layout ceiling near 1080px. Nav should collapse to an off-canvas/slide-in menu below tablet width (consistent with the `.et_slide_in_menu_container` selectors present in evidence), touch targets should be at least 44px tall for cart, nav, and configurator controls, and product-card grids should reduce from a multi-column layout to a single column below 480px. This section is a recommendation only; no responsive CSS or viewport behavior was directly observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- All CSS was extracted statically; no rendered/live layout, hover, focus, or animation states were observed.
- Font-family roles (Poppins for display, Roboto for body/UI) are inferred from stack ordering only; actual computed usage per element was not confirmed, and licensing/self-hosting of Poppins/Roboto was not verified.
- Several palette entries in the raw evidence (e.g., bright WordPress block-editor defaults such as `#f5a623`, `#cf2e2e`, `#00d084`) appear to be unused theme-default swatches rather than confirmed brand colors, and were intentionally excluded from the token set.
- Spacing, radius, and most component paddings are proposed approximations against a fixed scale; only the WooCommerce submit-button's `border-radius: 0`, `font-size: 17px`, and `letter-spacing: 1px` were directly evidenced.
- Mobile/tablet layout, breakpoint values, and menu-collapse behavior are proposed conventions, not measured from the site.
- Component states (hover/active/disabled) beyond the single documented `#9999ff` load-more hover are unobserved and marked proposed.
