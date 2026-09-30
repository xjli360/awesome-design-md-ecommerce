---
version: alpha
name: "Smallbatch Pets"
source_url: "https://smallbatchpets.com"
captured_at: "2026-09-29T04:01:40.575541+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Smallbatch Pets' evidence is dominated by an earthy, natural palette: a deep
  forest green (#0a4919, used as --color-foreground and as the oke-widget
  primary/button color) paired against a warm off-white canvas (#fcfdf8,
  --color-background). A brighter lime (#96bc2f) and pale lime (#caea83)
  appear as hover/border accents on the review-widget buttons, suggesting a
  secondary accent role. A muted gray-blue (#676986) is explicitly used for
  helper/date text in reviews, supporting a "muted" text role. Neutral grays
  (#dbdde4, #f4f4f6, #e5e5eb) recur as borders and light surfaces. Two
  distinct blues (#1990c6, #136f99) belong to the Shopify accelerated-
  checkout button and are treated here as a system/payment accent rather than
  brand color. Orange (#ff682e), teal (#b2f9e9), navy (#272d45) and slate
  (#2c3e50) are present in the raw palette but their applied role is not
  confirmed by the supplied CSS, so they are mapped as optional accent
  tokens (inferred). Typography references "Sharp Sans" for body copy and
  a custom-named "DesMontilles" for what is inferred to be display/heading
  use; both are unverified as licensed or actually rendered. The design
  system below proposes a clean, food-forward, trustworthy layout consistent
  with the observed farm-to-bowl, ingredient-led messaging.

colors:
  primary: "#0a4919"
  ink: "#0a4919"
  canvas: "#fcfdf8"
  body: "#144520"
  muted: "#676986"
  hairline: "#dbdde4"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-lime: "#96bc2f"
  accent-lime-soft: "#caea83"
  accent-orange: "#ff682e"
  accent-teal: "#b2f9e9"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  navy: "#272d45"
  slate: "#2c3e50"
  sage: "#829084"
  dark: "#121212"
typography:
  display-xl: { fontFamily: "DesMontilles, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px }
  display-md: { fontFamily: "DesMontilles, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px }
  title-md: { fontFamily: "Sharp Sans, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px }
  body-md: { fontFamily: "Sharp Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.06rem }
  body-sm: { fontFamily: "Sharp Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px }
  caption: { fontFamily: "Sharp Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.02rem }
  button-md: { fontFamily: "Sharp Sans, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.04rem }
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  protein-filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    activeBackgroundColor: "{colors.accent-lime}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary** reflects the review-widget's `--oke-button-backgroundColor:#0a4919` with white text, matching the observed hover swap to lime (`#96bc2f`); a proposed hover state is not otherwise confirmed sitewide.

**button-secondary** is an inferred outline variant using the same forest-green ink on the canvas background, intended for lower-emphasis actions like "Continue shopping" or "View cart," styled consistently with the primary palette rather than a separately observed rule.

**text-input** uses the neutral border (`#dbdde4`) seen on oke widget buttons and a white/card surface, proposed for search and account forms; no dedicated input CSS was supplied.

**nav-bar** is modeled on the `.list-menu__item` rule, which explicitly sets bold text in the dark-green foreground color against what is inferred to be the canvas background, supporting the site's multi-level Shop/Learn navigation.

**product-card** is a proposed pattern for the Best Sellers grid (e.g., "Freeze-Dried Raw Chicken Sliders"), using the white/card surface and hairline border for definition; corner radius and internal spacing are proposed, not measured.

**hero** corresponds to the homepage banner content ("Better treats in bigger batches," "Wild caught, wildly crunchy") and is assumed to sit on the soft light-gray surface with large display type; exact hero styling was not present in the supplied CSS.

**footer** is proposed as a reversed-color block (green background, white text) echoing the brand's primary color, appropriate for social links and legal text visible in the page text (Facebook, Instagram, TikTok, YouTube); not directly confirmed by footer-specific CSS.

**badge** models small labels such as "NEW" or "Free Shipping $49+," using an outlined pill style consistent with the badge-foreground/background/border variables defined in `:root`.

**search** reuses the text-input treatment for the header search affordance referenced in navigation text ("Search"); exact search-bar styling is unobserved.

**protein-filter-chip** is a category-specific, proposed component for the "Shop by Protein" taxonomy (Beef, Chicken, Turkey, Lamb, Duck, etc.), using the lime accent for an active/selected state to visually differentiate protein filtering from primary navigation.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width       | Layout guidance                                    |
|-----------|-------------|-----------------------------------------------------|
| mobile    | < 480px     | Single-column stack, collapsed hamburger nav        |
| tablet    | 480–1024px  | 2-column product grid, condensed protein-chip row   |
| desktop   | 1024–1440px | 3–4 column product grid, full mega-menu on hover    |
| wide      | > 1440px    | Max-width content container, extra whitespace       |

Touch targets should be a minimum of 44×44px for nav items, filter chips, and buttons. The multi-level Shop/Learn menu should collapse into an accordion pattern on mobile rather than the hover-based `.header__submenu` behavior implied by desktop CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- All CSS was extracted statically; no rendered layout, actual breakpoints, or interaction states (hover/focus/active) beyond the oke-widget rules were observed.
- "DesMontilles" and "Sharp Sans" are referenced font-family names only; their availability, licensing, and actual visual rendering are unverified.
- Several palette colors (`#ff682e`, `#b2f9e9`, `#272d45`, `#2c3e50`, `#829084`, `#121212`) appear in the supplied swatch list without a confirmed applied selector; they are included as optional accent tokens but their brand role is inferred, not confirmed.
- Base typographic sizes (16px body, 48px display, etc.) are proposed conventions, not measured pixel values, since the only concrete size evidence was `font-size: 1.5rem` on `body` with an unconfirmed root font-size.
- The `--color-background-contrast` RGB value in the source CSS (210,225,149) does not correspond to any hex in the supplied palette and was therefore omitted from the color tokens.
- Mobile navigation collapse, product-card grid counts, and hero composition are proposed patterns based on page-text content, not confirmed screenshots or measured DOM structure.
