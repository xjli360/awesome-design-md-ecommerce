---
version: alpha
name: "Kreg Tool"
source_url: "https://kregtool.com"
captured_at: "2026-09-28T04:20:00.678787+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Kreg Tool's public storefront runs on a Salesforce Commerce Cloud (Demandware) theme with Bootstrap-derived utility classes layered under a custom brand palette. The CSS root variables declare a primary corporate blue (#004c97) alongside a warm secondary gold (#dea037), a teal success tone (#008574), and a brown-toned danger/utility color (#612c17), all sitting on a neutral gray-scale system (#3a3a3a body text, #6c757d muted, #dee2e6 hairlines, #343a40 dark). Body copy renders in Montserrat with sans-serif fallback at a relaxed 1.625 line-height; monospace stacks (Consolas, Menlo, Courier New) appear only in code/utility contexts and are not treated as brand type. Button radius is explicitly observed at .1875rem (3px), informing the "sm" rounding token.
  This interpretation proposes a tool-and-hardware retail aesthetic: confident primary blue for calls-to-action and navigation accents, gold/warning tones reserved for promotional badges and sale pricing, and generous neutral surface tints (#f4f4f4, #e9f0f6) for card and section separation. Heading weight, hierarchy sizing, and several component states below are inferred design proposals, not measured page observations, since only CSS rules and a color/font inventory were supplied.

colors:
  primary: "#004c97"
  secondary: "#dea037"
  ink: "#212529"
  body: "#3a3a3a"
  canvas: "#ffffff"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f4f4f4"
  surface-card: "#e9f0f6"
  on-primary: "#ffffff"
  success: "#008574"
  danger: "#612c17"
  info: "#17a2b8"
  dark: "#343a40"
  light: "#d8d9da"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.625, letterSpacing: 0px}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.625, letterSpacing: 0px}
rounded:
  none: 0px
  xs: 2px
  sm: 3px
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
    borderColor: "{colors.secondary}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    mutedTextColor: "{colors.light}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    stripeColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    headerTextColor: "{colors.ink}"
    bodyTextColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** is the principal call-to-action treatment (Add to Cart, Shop Now), using the observed `--primary` blue with white text and the site's measured 3px button radius. State transitions (hover/focus/disabled) are proposed, not confirmed beyond the generic `.btn:hover` text/decoration reset seen in CSS.

**button-secondary** provides a lower-emphasis outline action using the gold secondary token as a border accent against neutral ink text, suited to "Learn More" or filter-toggle actions on a tool retailer's category pages.

**text-input** models form fields (search box, account forms, newsletter signup) with a hairline border and white canvas background, matching Bootstrap's reset-driven `input,button,select` typography inheritance observed in the CSS.

**nav-bar** proposes a white header bar with a bottom hairline and primary-blue accent for active/hover states, consistent with a persistent white body background and the brand's blue identity color.

**product-card** is inferred for woodworking tool/kit listings: a soft blue-tinted card surface, hairline border, medium rounding, and title/body type pairing to present product name, price, and short description.

**hero** proposes a full-bleed primary-blue banner for homepage or seasonal promotions, echoing the site's seasonal CSS variables (blue-dominant seasonal tokens) with white reversed text for large display headlines.

**footer** uses the dark neutral (#343a40) as a grounding band with white and light-gray text, appropriate for site-wide links, warranty/support info, and legal text common to tool manufacturer sites.

**badge** repurposes the gold secondary color for sale/clearance or "new" labels on product cards, using pill rounding and compact caption type; exact badge copy and positioning are not observed.

**search** is a compact variant of text-input intended for a persistent header search field; icon presence (Font Awesome families were present in the font list) is plausible but not confirmed from layout evidence.

**spec-table** is a category-appropriate proposal for tool specification/comparison tables, leveraging the observed `.table-striped` rgba(0,0,0,.05) zebra pattern (mapped to `surface-soft`) and Bootstrap-style hairline borders for dimensions, torque, or compatibility data typical of woodworking tool pages.

## Responsive Behavior

*Recommendation only — no measured breakpoints or mobile layout were observed; the CSS variables list Bootstrap-style breakpoints (`sm` 576px, `md` 768px, `smTablet` 900px, `lg` 992px, `desktop` 1024px, `xl` 1200px, `xxl` 1400px), reused here as structural guidance.*

| Range | Layout guidance |
|---|---|
| < 576px | Single-column stack; nav collapses to a hamburger/drawer pattern; product-card grid becomes 1-up. |
| 576–899px | 2-up product grid; nav-bar may show condensed logo and icon-only search/cart. |
| 900–1199px | 3-up product grid; full nav-bar links visible; hero padding increases toward `spacing.xxl`. |
| ≥ 1200px | 4-up product grid; max-width content container; full `spacing.section` vertical rhythm. |

Touch targets should meet a minimum ~44px hit area for buttons and nav items (padding derived from `spacing.md`/`spacing.lg`). Primary navigation should collapse into a toggled drawer below the `md` breakpoint; search and cart icons should remain persistently visible.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS custom properties, a small rule sample, and an unordered color/font inventory — no rendered page, computed layout, or DOM structure was observed. Semantic role assignments (e.g., which grays serve as body vs. muted vs. hairline) are inferred from Bootstrap-convention naming (`--dark`, `--light`, `--gray`) and typical usage, not confirmed visually. All typography sizes beyond the observed `body { font-size:1rem; line-height:1.625 }` and the `.btn` reset are proposed scale values, not measured. Rounded values beyond the observed `.1875rem` button radius are estimated. No hover/focus/active/disabled interaction states, animations, or mobile breakpoint behavior were actually observed in a browser. Custom font availability, weights, and licensing for Montserrat are not verified from this evidence and should be confirmed against the site's actual `@font-face` or webfont-loader configuration before implementation.
