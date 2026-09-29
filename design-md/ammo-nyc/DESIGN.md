---
version: alpha
name: "AMMO NYC"
source_url: "https://ammonyc.com"
captured_at: "2026-09-29T03:59:03.446125+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  AMMO NYC's storefront CSS shows a restrained, utilitarian palette built around near-black
  (#121212, confirmed via the body text and secondary-button rules using rgb(25,24,24)),
  white canvas, and a family of neutral grays (#333333, #666666, #dddddd, #cccccc, #f4f4f4,
  #dedede) used for text, borders, and loading-skeleton states. The only chromatic accents
  directly bound to a component are the Shopify accelerated-checkout wallet button's blue
  (#1990c6, hover #136f99); a red (#ee2e24) also appears in the palette and is proposed here
  as a badge/sale accent, though its live role is unconfirmed. Body copy is set in Helvetica
  with sans-serif fallback at 1rem/1.5 line-height, and the theme's `.btn` class specifies a
  bold, tightly tracked 14px label style, which anchors the button-md and body-md typography
  tokens as directly observed. All other display, title, and caption sizes are proposed
  extrapolations consistent with a black/white, product-forward automotive-care brand and are
  labeled inferred. The interpretation favors high-contrast dark CTAs on white, minimal
  ornamentation, and small chromatic accents reserved for utility states (wallet checkout,
  sale/badge) rather than broad brand color usage, since no dedicated brand hue is evidenced.

colors:
  primary: "#121212"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#1990c6"
  accent-hover: "#136f99"
  sale: "#ee2e24"
  border-strong: "#cccccc"
  skeleton: "#dedede"
typography:
  display-xl: {fontFamily: "Helvetica, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Helvetica, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "Helvetica, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Helvetica, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.14, letterSpacing: -0.4px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
  wallet-checkout-button:
    backgroundColor: "{colors.accent}"
    hoverBackgroundColor: "{colors.accent-hover}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.base} {spacing.xl}"

## Components

**button-primary** renders as a solid near-black rectangle with white label text, matching the theme's `.btn--secondary` rule (`rgb(25 24 24)` background, white text). This is the confirmed strong-CTA pattern (e.g. "Add to Cart," "Choose Your System").

**button-secondary** is a proposed outline variant for lower-emphasis actions ("Learn More," filter toggles), using the hairline border color and ink text on a transparent background; hover/active states are not observed and are proposed as a filled inversion.

**text-input** covers search and account/login fields. Border color, radius, and padding are inferred defaults consistent with the theme's utility-first reset (`button,input,...{font-family:inherit}`); no focus-ring color was captured in evidence.

**nav-bar** reflects the site's header structure (logo, All/Kits/Paint/Wheels/Interior links, search, account, cart) inferred from page text. White background and a bottom hairline are proposed; sticky behavior is not confirmed.

**product-card** models the repeating "Add" product tiles seen in Regimens/Best Sellers carousels (title, price, quick-add button). White surface with a light hairline border and medium radius is a proposed baseline; card shadows were not observed in the CSS.

**hero** represents the "EXPERT CAR CARE. MADE SIMPLE." banner: full-width dark section with large white display type and a primary button, inferred from page copy and the available dark/white contrast pair.

**footer** groups the observed link clusters (Get Guidance, Learn, My Account, social icons) into a soft-gray multi-column band with caption-sized links and hairline dividers between sections; exact column layout is not measured.

**badge** is a proposed small pill for merchandising labels (e.g. "Best Seller," "New") using the red accent as a sale/attention color; no such badge markup was present in the supplied CSS, so this is a category-appropriate addition.

**search** models the overlay search panel referenced in page text ("Search Close Search Clear Search Suggestions"), using canvas background and hairline-bordered result rows; open/close transitions are not observed.

**wallet-checkout-button** is directly grounded in evidence: the Shopify accelerated-checkout CSS defines an unbranded wallet button at `#1990c6` with a `#136f99` hover state, full-width block sizing, and no border-radius by default — reproduced here as-is rather than inferred.

## Responsive Behavior
Recommended, not measured from live rendering:

| Breakpoint | Range        | Notes (proposed) |
|-----------|---------------|-------------------|
| mobile    | 0–639px       | Single-column product grid; nav collapses to a hamburger + cart icon; sticky bottom "Add to Cart" bar suggested for PDPs. |
| tablet    | 640–1023px    | 2-column product grid; inline search icon expands to overlay. |
| desktop   | 1024–1439px   | Full horizontal nav with category flyouts; 3–4 column product grids. |
| wide      | 1440px+       | Max-width content container (~1280–1440px) with increased section padding (`{spacing.section}`). |

Touch targets should be at least 44px tall, aligning with the accelerated-checkout button's `clamp(25px, 44px, 55px)` sizing. Primary nav should collapse to a drawer/menu below the tablet breakpoint. None of this reflects observed JavaScript or CSS media-query behavior from the site.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence was extracted statically from compiled CSS bundles and page text; no live DOM, computed styles, or responsive breakpoints were observed.
- Only `body` and `.btn` selectors provided confirmed typography values (Helvetica, sizes/weights/line-heights); all other type scale entries (display, title, caption sizes) are proposed and unmeasured.
- The font list included Baskerville, Nunito Sans, and Roboto alongside icon fonts (JudgemeIcons, swiper-icons); these likely originate from third-party widgets (reviews, sliders) or unused editor font options rather than confirmed brand typography, so they were excluded from tokens.
- Color-to-role mapping is largely inferred: only the wallet checkout button (#1990c6/#136f99) and the dark `.btn--secondary` (#121212/white) have direct selector-level evidence; primary, sale, hairline, and surface roles are reasonable but unverified assignments from the observed palette.
- Corner radius and spacing scales are proposed conventions, not extracted from measured site geometry (the only radius directly observed was `0px` on the checkout button/skeleton default).
- No interaction states (hover/focus/active), mobile menu behavior, or cart drawer layout were observed; all are proposed.
- Custom font licensing/availability (e.g. any use of Baskerville) was not verified and should not be assumed production-ready without confirmation.
