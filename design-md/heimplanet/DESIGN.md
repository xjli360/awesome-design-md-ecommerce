---
version: alpha
name: "Heimplanet"
source_url: "https://heimplanet.com"
captured_at: "2026-09-29T04:10:16.635694+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Heimplanet's storefront CSS evidence shows a monochrome-first system: pure black (#000000) and white (#ffffff) drive buttons, borders and body copy, with #333333 as the running text color and a family of light neutrals (#f5f5f5, #fafafa, #f3f3f3, #dedede) available for card and section backgrounds. Buttons are explicitly zero-radius (border-radius:0 on .button and on the Judge.me review widget tokens), reinforcing a squared, technical aesthetic consistent with tents, tarps and hardware-oriented gear. Two custom families are declared in the theme stack, Simplonnorm (body/heading) and Simplonmono (likely a technical/label face); Arial and Helvetica Neue appear as inherited theme fallbacks rather than brand faces. Uppercase, letter-spaced button labels (.2em) and a large uppercase H1 (4.375rem) suggest a confident, editorial-technical tone typical of outdoor equipment brands. A muted blue-grey (#758696) and mid greys (#999999, #9b9b9b) are treated here as inferred secondary-text/muted roles, since no explicit semantic label was present in the CSS. Multi-hue colors tied to payment-method iconography (e.g. #eb001b, #f79e1b, #0071ce) are excluded from the brand palette as non-brand. One warm red (#ea384c) is retained as an inferred sale/badge accent given the "Archive Sale 50%" content context. All other structure below is proposed and clearly labeled as such.

colors:
  primary: "#000000"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#758696"
  hairline: "#dedede"
  surface-soft: "#f5f5f5"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-sale: "#ea384c"
  neutral-mid: "#999999"
  neutral-dark: "#1c1c1c"
typography:
  display-xl: {fontFamily: "Simplonnorm, sans-serif", fontSize: 70px, fontWeight: 500, lineHeight: 1, letterSpacing: 0px}
  display-md: {fontFamily: "Simplonnorm, sans-serif", fontSize: 36px, fontWeight: 500, lineHeight: 1.1, letterSpacing: 0px}
  title-md: {fontFamily: "Simplonnorm, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Simplonnorm, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.43, letterSpacing: 0px}
  caption: {fontFamily: "Simplonmono, monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.05em}
  button-md: {fontFamily: "Simplonnorm, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1, letterSpacing: 0.2em}
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
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.neutral-dark}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** renders the observed solid-black, zero-radius button pattern (.button in heimplanet-4-0.css), used for primary calls to action like "Jetzt entdecken." Hover states beyond the documented is-outline invert were not captured, so any hover treatment here is proposed.

**button-secondary** mirrors the observed `.button.is-secondary` rule: a transparent fill with a black border and black text, intended for lower-emphasis actions such as "Mehr erfahren" links. The white-on-transparent hover variant seen in `.is-secondary.is-white:hover` confirms an invert-on-hover pattern exists somewhere in the system, though its exact trigger context is not observed here.

**text-input** is a proposed field style; no explicit input CSS was present in the evidence, so border, radius and padding follow the brand's general zero-radius, hairline-bordered convention rather than a captured rule.

**nav-bar** is inferred from the shop's menu-heavy text content (Shop, Magazin, Unternehmen, DE/EN) and the uppercase, letter-spaced button typography token; exact height, sticky behavior and mobile collapse were not present in the static CSS.

**product-card** reflects a catalog-first storefront (Bestseller list with title, price, review count) and uses the light surface-card background with a hairline border to separate cards on a white canvas; card shadow/elevation was not observed and is omitted.

**hero** is proposed for banner sections such as "THE CAVE XL" and "Mavericks 2026," using the large uppercase display-xl heading style captured from the h1 rule, set on a dark neutral background since hero imagery/overlay darkness was implied by promotional banner copy but not measured.

**footer** keeps the site's light canvas background and body-sm typography since no dark-footer evidence was found; a hairline top border separates it from content, consistent with the hairline-driven division pattern seen elsewhere.

**badge** supports "Neu," "Sale 50%," and similar flagging seen throughout the navigation and promo copy; it borrows the sale-red accent color as an inferred, non-observed semantic assignment.

**search** is a minimal proposed pattern for the "Search Suggestions" feature referenced in page text; no dedicated search-input CSS was supplied.

**spec-table** is a category-appropriate addition for outdoor/technical gear (tent poles, DYECOSHELL™, COOLEVER™ material callouts), using the monospace caption font for label/value pairs to echo a technical spec-sheet feel; this pairing of Simplonmono to tabular data is a stylistic inference, not an observed rule.

## Responsive Behavior
This is a recommended, not measured, breakpoint structure:

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| mobile    | 0–479px     | Single-column product grid, nav collapses to a toggled menu |
| mobile-lg | 480–767px   | Two-column product grid |
| tablet    | 768–991px   | Two to three-column grid, nav-bar may show partial inline links |
| desktop   | 992–1439px  | Full horizontal nav, three to four-column product grid |
| wide      | 1440px+     | Max-width content container, four+ column grid |

Touch targets should be at least 44×44px for nav and cart controls; the mobile nav toggle (`.w-nav-button`) exists in the theme scaffold but its open/close behavior was not observed in static CSS. Collapse of secondary nav categories (Zelte & Tarps, Taschen & Rucksäcke, Bekleidung, etc.) into an accordion on small screens is a reasonable but unverified assumption given the deep category list in the page text.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS plus page text only; no rendered layout, computed spacing, or actual breakpoints were observed.
- Semantic color roles (muted, hairline, surface-soft/card, accent-sale) are inferred from generic greys/reds in the palette, not from explicit class-to-role documentation.
- Simplonnorm and Simplonmono are declared as font-family values in the stylesheet; their licensing, weights, and actual availability/fallback rendering were not verified.
- Typography sizes beyond the h1 (4.375rem), body (.9375rem/15px), and button (.75rem) rules are proposed estimates, not extracted values.
- Border-radius is documented as 0 for buttons and the review widget; radius values for cards, inputs, and badges are proposed defaults, not confirmed.
- No hover/focus/active states were observed beyond `.is-outline:hover` and `.is-secondary.is-white:hover`; all other interaction states in components above are proposed.
- Mobile menu, search overlay, and cart drawer behavior (referenced in page text as "Warenkorb") were not present in the supplied CSS and are not described as observed.
