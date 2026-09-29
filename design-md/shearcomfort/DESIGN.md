---
version: alpha
name: "ShearComfort"
source_url: "https://shearcomfort.com"
captured_at: "2026-09-29T04:09:07.620116+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  ShearComfort's storefront runs on a BigCommerce Stencil theme whose CSS confirms a single
  typeface family, "Titillium Web" (falling back to Arial, Helvetica, sans-serif), applied to
  body copy, headings, and buttons alike. The confirmed palette centers on a near-black slate
  (#3f4b54) for body text and headings against a white canvas, with a saturated red (#d80027)
  reserved for primary calls-to-action such as "Add to Cart" and configurator buttons — fitting
  for a seat-cover retailer whose merchandising leans on bold percent-off badges and urgency
  messaging. Neutral grays (#ededed, #ecedee, #e5e5e5, #b2b7bb) recur across buttons, panel
  headers, and form borders, suggesting a restrained, utilitarian UI built for a large
  vehicle-fitment catalog rather than a boutique aesthetic. Additional palette entries (#f1a500,
  #008a06, #2778c4, #cc4749) are present in the theme stylesheet but their exact UI role could not
  be confirmed from the supplied selectors; they are mapped here to plausible, clearly inferred
  roles (warning, success, link, error). Rounded corners are intentionally minimal — the one
  confirmed button radius is 2px — reinforcing a squared-off, functional automotive-parts retail
  feel rather than a soft consumer-lifestyle brand.

colors:
  primary: "#d80027"
  ink: "#3f4b54"
  canvas: "#ffffff"
  body: "#3f4b54"
  muted: "#6f787f"
  hairline: "#b2b7bb"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  surface-alt: "#e5e5e5"
  control-bg: "#ededed"
  control-bg-hover: "#ecedee"
  text-strong: "#202020"
  disabled-bg: "#f3b3be"
  accent-warning: "#f1a500"
  accent-success: "#008a06"
  link: "#2778c4"
  error: "#cc4749"
typography:
  display-xl: {fontFamily: "\"Titillium Web\", Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: 0.25px}
  display-md: {fontFamily: "\"Titillium Web\", Arial, Helvetica, sans-serif", fontSize: 34px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.25px}
  title-md: {fontFamily: "\"Titillium Web\", Arial, Helvetica, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0.25px}
  body-md: {fontFamily: "\"Titillium Web\", Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: normal}
  body-sm: {fontFamily: "\"Titillium Web\", Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: normal}
  caption: {fontFamily: "\"Titillium Web\", Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "\"Titillium Web\", Arial, Helvetica, sans-serif", fontSize: 15px, fontWeight: 700, lineHeight: normal, letterSpacing: normal}
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
    backgroundColor: "{colors.control-bg}"
    textColor: "{colors.text-strong}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceColor: "{colors.primary}"
  hero:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.base}"
  vehicle-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.body-sm}"
    buttonTypography: "{typography.button-md}"

## Components

**button-primary** – Maps directly to the observed `.button--primary` rule: red (#d80027) fill, white text, 2px radius. Hover/active states (darkening to #202020 then #424242) are confirmed in the stylesheet and preserved conceptually as state transitions; exact timing/easing values beyond the transition property are proposed.

**button-secondary** – Derived from the default `.button` rule (light gray #ededed fill, #424242-family text). A hairline border is added here as a proposed affordance since the source CSS does not declare a border for this state.

**text-input** – No explicit input-field selector was supplied; styling is inferred from the `.form-body` panel treatment (white background, #b2b7bb border, subtle shadow) scaled down to a single-field control.

**nav-bar** – Inferred from body-level typography and hairline gray tones; the header's actual height, sticky behavior, and icon layout (cart, account, search, phone number) were not present in the CSS sample and are proposed based on the page-text structure (USA/CAD toggle, "Free Shipping," search, account, cart).

**product-card** – Proposed pattern for seat-cover/category tiles, using confirmed card-text color (#3f4b54) and a red price accent consistent with the promo-heavy page copy ("25% OFF," "30% OFF").

**hero** – Uses the light gray panel-header tone as an inferred section background for a "Select Your Vehicle" / promotional hero, paired with the largest display type; actual hero imagery, overlay treatment, or the alpha-channel color `#0a0a0aab` (likely a scrim/overlay) were not confirmed in context.

**footer** – Entirely proposed; no footer-specific selectors were supplied. Reuses the panel-header gray and muted text tone for plausibility rather than observation.

**badge** – Directly motivated by the extensive discount-banner text ("UP TO 45% OFF") using the primary red fill; pill shape is a proposed convention, not confirmed by a border-radius rule for this element.

**search** – Proposed compact search field styling; a search affordance is confirmed in page text ("Search Keyword: Search") but its visual treatment was not present in the CSS sample.

**vehicle-selector** – A category-appropriate proposed component for the "Select Your Vehicle / Perfect Fit Guaranteed" Year/Make/Model widget referenced in the page copy, styled consistently with the confirmed card/panel treatment.

## Responsive Behavior
The supplied theme CSS contained media-query fragments at 551px, 801px, 1261px, and 1681px, indicating the theme's own breakpoint scale. These are adopted below as a proposed responsive table; no actual layout shifts, column counts, or component reflow at these widths were observed.

| Breakpoint | Range | Proposed behavior |
|---|---|---|
| mobile | up to 551px | Single-column stacking, nav collapses to a menu affordance, touch targets ≥44px |
| tablet-sm | 551–801px | Two-column product grids, condensed nav |
| tablet-lg | 801–1261px | Three-column grids, full nav visible |
| desktop | 1261–1681px | Standard multi-column layout, hero at full width |
| wide | 1681px+ | Max-width content container, extra gutter space |

This table is a recommendation for implementation, not a record of measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Extraction is static (CSS + text only); no rendered screenshots, computed layout, or JS-driven interaction states were captured.
- Several palette entries (#f1a500, #008a06, #2778c4, #cc4749, #6654dc, #a5dc86, #166534, etc.) appear in the stylesheet without selector context; their assignment to warning/success/link/error roles above is inferred, not confirmed.
- Font families "Crimson Text," "Fontjek," "Lato," "Montserrat," "Nunito Sans," and "Source Sans Pro" appear in the raw font list from the theme package but are not tied to any confirmed selector; only "Titillium Web" (with Arial/Helvetica/sans-serif fallback) is confirmed in use via `body`, headings, and `.button` rules. Licensing and hosting of any custom font were not verified.
- Breakpoint values (551/801/1261/1681px) were parsed from media-query strings, not from observed responsive rendering; actual mobile navigation, cart drawer, and menu-collapse behavior were not observed.
- The `#0a0a0aab` value (8-digit hex with alpha) suggests a dark overlay/scrim but its exact usage (modal backdrop, image overlay, etc.) is unconfirmed.
- Spacing and rounded-corner scales beyond the confirmed 2px button radius and 1.5rem panel padding are proposed conventions for consistency, not measured values.
