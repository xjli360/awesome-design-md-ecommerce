---
version: alpha
name: "Woof Concept"
source_url: "https://woofconcept.com"
captured_at: "2026-09-28T09:35:35.833822+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Woof Concept presents itself as a premium, Canadian-made lifestyle pet brand
  selling collars, leashes and harnesses backed by a lifetime warranty. The
  extracted CSS shows a high-contrast, editorial foundation: headings render in
  CooperHewitt (falling back to Futura, then sans-serif) at 700 weight,
  uppercase, with 1px letter-spacing, while body copy uses Noto Sans at
  14px/1.6 line-height in solid black on white. Interactive elements sampled
  from the on-site review widget reveal pill-shaped buttons (50px
  border-radius) in solid black with white text, a hover shift to #1a1a1a,
  and a neutral border/text vocabulary (#dbdde4, #e5e5eb, #676986) used for
  secondary UI chrome. Beyond the monochrome black/white/gray core, the
  palette carries a small set of accent hues — teal (#1ab3bc/#14888f), red
  (#d02e2e/#e30000) and green (#56ad6a) — that plausibly serve sale, alert,
  and success/in-stock roles respectively, though their exact on-site usage
  is inferred rather than confirmed. This interpretation extends the observed
  monochrome-plus-accent system into a full component set: bold uppercase
  display type for hero and category headers, pill buttons for primary
  actions, soft gray surfaces for product cards, and a warranty badge that
  leans on the teal accent to echo the brand's lifetime-warranty promise.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#676986"
  hairline: "#e5e5eb"
  surface-soft: "#f7f7f7"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  border-input: "#dbdde4"
  hover-ink: "#1a1a1a"
  accent-teal: "#1ab3bc"
  accent-teal-dark: "#14888f"
  sale-red: "#d02e2e"
  alert-red: "#e30000"
  success-green: "#56ad6a"
  overlay-scrim: "#00000080"
typography:
  display-xl: {fontFamily: "CooperHewitt, Futura, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: 1px, textTransform: uppercase}
  display-md: {fontFamily: "CooperHewitt, Futura, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 1px, textTransform: uppercase}
  title-md: {fontFamily: "CooperHewitt, Futura, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 1px, textTransform: uppercase}
  body-md: {fontFamily: "Noto Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: normal}
  body-sm: {fontFamily: "Noto Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: normal}
  caption: {fontFamily: "Noto Sans, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "CooperHewitt, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 1px, textTransform: uppercase}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    hover: {backgroundColor: "{colors.hover-ink}"}
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    hover: {backgroundColor: "{colors.surface-soft}"}
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.border-input}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.muted}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.border-input}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  warranty-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-teal-dark}"
    accentColor: "{colors.accent-teal}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** is the solid black, pill-shaped call-to-action pattern (Add to Cart, Shop Now), directly modeled on the review widget's `--oke-button-*` tokens which specify a 50px radius, black fill, white uppercase text, and a darker `#1a1a1a` hover — the hover and active states are proposed extensions of this observed pattern to site-wide buttons.

**button-secondary** is an inferred outline variant for lower-emphasis actions (e.g., "View All," "Learn More"), reusing the ink color as border and text with a soft-gray hover fill; no outline button was directly observed, so this is a proposed complement to the primary pattern.

**text-input** covers search fields, newsletter signup, and account forms. The border color `#dbdde4` and neutral font inheritance come from the review-widget input styling; the compact radius and padding are proposed for consistency with the pill/rounded button language at a smaller, less rounded scale.

**nav-bar** is a proposed light header with uppercase body-sm link styling consistent with the site's heading transform rules, sitting on a white canvas with hairline-gray dividers; actual sticky/collapse behavior was not observed.

**product-card** anticipates the grid of leash/collar/harness listings implied by the navigation taxonomy (Collars, Leashes, Harnesses, Starter Kits). It uses the off-white `surface-card` tone and hairline border sampled from the palette, with uppercase title-md product names and body-md pricing, mirroring the heading/body split found in the theme CSS.

**hero** proposes a large uppercase display treatment on white canvas for homepage and collection banners, extending the observed `h1`/`.title` rule (CooperHewitt/Futura, 700 weight, uppercase, 1px tracking) to a bigger promotional scale.

**footer** is an inferred dark-mode block (ink background, white text) for site-wide links and legal/warranty copy; no footer-specific CSS was supplied, so background/text inversion is a stylistic proposal rather than a confirmed pattern.

**badge-sale** uses the observed red family (`#d02e2e`) as a small pill label for discounted items, consistent with the "Sale" and "Just Dropped" navigation entries; exact shape/color usage on sale tags was not directly evidenced.

**search** reuses the input pattern on a slightly tinted `surface-soft` background to differentiate it from standard form fields in the header/overlay search experience referenced in the page text ("Search").

**warranty-badge** is a category-appropriate addition for a leash/collar/harness brand that foregrounds its "lifetime warranty" promise in the page copy; it borrows the teal accent (`#1ab3bc`/`#14888f`) as a trust/assurance color, since teal appears in the palette without a confirmed existing role and is a reasonable inferred fit for warranty/trust messaging distinct from the red sale accent.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width       | Behavior (proposed) |
|-----------|-------------|----------------------|
| mobile    | 0–599px     | Single-column product grid, collapsed hamburger nav, sticky bottom cart CTA |
| tablet    | 600–1023px  | 2-column product grid, condensed nav with visible search icon |
| desktop   | 1024–1439px | 3–4 column product grid, full horizontal nav with dropdown mega-menus |
| wide      | 1440px+     | 4+ column grid, max-width content container with generous side margins |

Touch targets for buttons and nav items should maintain a minimum 44×44px hit area; the pill button radius (`{rounded.full}`) should be preserved at all sizes. Header navigation is expected to collapse into a slide-out or accordion menu below the tablet breakpoint, given the depth of the observed category taxonomy (Dogs, Kitchen, Clothing, Collections, Collabs, Accessories, Cats, Company).

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted from static CSS/HTML and a third-party review widget (`oke-*` classes); actual site-authored button, nav, and card CSS were not directly captured, so several component mappings (button-secondary, nav-bar, footer, product-card, search) are inferred from adjacent evidence rather than confirmed selectors.
- Color-to-role assignments for the accent teal, red, and green hues are plausible but unconfirmed; the site may use them differently (e.g., in-stock indicators, promotional banners, or third-party payment icons such as the Visa/Mastercard-like blues/oranges also present in the palette).
- All pixel sizes in the typography scale beyond the confirmed `14px`/`1.6` body values are proposed, not measured.
- No interaction states (focus rings, disabled buttons, form validation) or actual mobile/responsive layout were observed; the breakpoint table above is a design recommendation only.
- CooperHewitt is referenced as a custom font in the stylesheet; its licensing and actual load/availability on the live site were not verified in this extraction. Futura, Noto Sans, and Arial are used as fallbacks per the CSS but their rendering fidelity was not confirmed.
- Baskerville, Jost, Consolas, and Lucida Sans Unicode appear in the supplied font list but were not attributed to any specific selector in the evidence, so they are omitted from the typography tokens above as unconfirmed roles.
