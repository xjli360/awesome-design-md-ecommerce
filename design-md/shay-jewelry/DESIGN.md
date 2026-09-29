---
version: alpha
name: "Shay Jewelry"
source_url: "https://www.shayjewelry.com"
captured_at: "2026-09-28T04:14:45.221376+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  SHAY's stylesheet centers on a near-monochrome palette: true black (#000000)
  and a softened off-black (#1c1c1c) carry primary UI weight, set against a
  white canvas (#ffffff) with a family of light neutrals (#f5f5f5, #eaeaea,
  #e5e5e5, #d0d0d0) forming hairlines and soft surfaces. Body copy uses a
  warm dark gray (#272727) rather than pure black, consistent with an
  editorial, gallery-like tone appropriate to fine jewelry. Typography is
  forced to 'Hanken Grotesk' with `!important` across headings, body, links,
  and lists, paired with a notably compact type scale (11px–18px root
  tokens), suggesting a refined, low-contrast, small-caps-adjacent system
  typical of minimalist luxury e-commerce; larger display sizes are proposed
  extrapolations, not observed. A red accent (#ea0202) is inferred for
  sale/error signaling. Bootstrap-style alert triads (success/warning/error
  backgrounds and text) and a blue Shopify checkout-button pair (#1990c6/
  #136f99) appear to be third-party or system defaults rather than core
  brand colors, and are labeled accordingly. Two soft tints (#e6f7f4 mint,
  #fef3e2 peach) are present with unclear usage and are treated as inferred
  accent surfaces for badges or seasonal callouts. Corner treatment favors
  sharp edges (0px on checkout buttons) with a single observed 16px radius
  on a chat widget, informing the rounded scale below.

colors:
  primary: "#1c1c1c"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#272727"
  muted: "#6b6b6b"
  hairline: "#e5e5e5"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-neutral: "#ececec"
  accent-sale: "#ea0202"
  link: "#1990c6"
  link-hover: "#136f99"
  success-bg: "#d4edda"
  success-text: "#155724"
  warning-bg: "#fff3cd"
  warning-text: "#856404"
  error-bg: "#f8d7da"
  error-text: "#721c24"
  surface-deep: "#121f36"
  surface-mint: "#e6f7f4"
  surface-peach: "#fef3e2"
typography:
  display-xl: {fontFamily: "'Hanken Grotesk', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Hanken Grotesk', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Hanken Grotesk', sans-serif", fontSize: 18px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Hanken Grotesk', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Hanken Grotesk', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Hanken Grotesk', sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "'Hanken Grotesk', sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.5px}
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
    padding: "{spacing.md} {spacing.xxl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xxl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xxl}"
  badge:
    onSaleBackground: "{colors.accent-sale}"
    onSaleText: "{colors.on-primary}"
    soldOutBackground: "{colors.badge-neutral}"
    soldOutText: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  authenticity-panel:
    backgroundColor: "{colors.surface-mint}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the near-black `#1c1c1c` fill against white text, matching the black accent color tokens declared for chat/checkout accents. Sharp corners (`rounded.none`) reflect the observed `border-radius:0px` default on the Shopify accelerated-checkout button. Hover/pressed states are not observed and are proposed as a slight opacity or fade to `#000000`.

**button-secondary** is an outlined variant for lower-emphasis actions (e.g. "Add to Wishlist"), sharing the primary's type and padding but using a hairline-weight border and transparent fill. Its hover state is proposed, not observed.

**text-input** keeps a light hairline border (`#e5e5e5`) on white, with compact 12px body copy consistent with the site's small root type tokens. Focus-state styling (border/ring color) was not present in the supplied evidence and is proposed as a subtle darkening to `{colors.primary}`.

**nav-bar** is inferred from header grid variables (`primary-nav logo secondary-nav`) and padding tokens (~1.6rem block padding, close to `{spacing.lg}`). Logo width (100px) and a three-column grid are observed structurally, though visual rendering was not captured.

**product-card** proposes a bordered, cardless-looking tile typical of jewelry PDBs, using hairline borders rather than shadow, in keeping with the flat, sharp-corner aesthetic implied by the checkout button radius token.

**hero** is a proposed full-bleed banner using the deep navy `#121f36` as an alternate dark surface (distinct from the neutral blacks used for buttons/footer), intended for seasonal or campaign moments. Its use as a hero background is inferred, not confirmed.

**footer** reuses the primary near-black surface with white text and the compact body-sm scale, consistent with a minimal, contrast-forward footer commonly paired with fine-jewelry brand sites.

**badge** consolidates the explicitly declared sale/sold-out/custom badge tokens (`on-sale-badge-background: 227 44 43`, approximated here as `#ea0202`; `sold-out-badge-background: #efefef`, approximated as `{colors.badge-neutral}`). These are the most directly evidenced component tokens in the CSS.

**search** is a proposed lightweight overlay/input pattern using the soft neutral surface (`#f5f5f5`) for visual separation from the white canvas, without observed confirmation of an actual search UI.

**authenticity-panel** is a category-specific, proposed component for displaying gemstone/metal certification (e.g. "18K Gold, Conflict-Free Diamonds") using the unexplained mint tint (`#e6f7f4`) as a soft, trust-signaling surface — its brand role is inferred, not confirmed by the evidence.

## Responsive Behavior
This is a recommendation based on common e-commerce patterns, not measured site behavior; no breakpoint values or media queries were present in the supplied evidence.

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | <768px | Single-column product grid, nav collapses to hamburger + drawer |
| Tablet | 768–1023px | 2-column product grid, condensed header nav |
| Desktop | ≥1024px | 3–4 column product grid, full three-region header grid as declared (`primary-nav logo secondary-nav`) |

Touch targets should be a minimum of 44px (matching the clamp range seen on the Shopify payment button, `25px–55px`). Header collapse behavior, drawer/menu interactions, and any transitions are proposed conventions, not observed states.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived entirely from static CSS custom properties and rule declarations; no rendered page, computed layout, or interaction states were observed. Several color-to-role mappings (mint `#e6f7f4`, peach `#fef3e2`, deep navy `#121f36`) are inferred from adjacency in the palette list, not confirmed usage. The Bootstrap-style alert triad (success/warning/error) and the blue Shopify checkout-button colors (`#1990c6`/`#136f99`) likely originate from third-party app or platform defaults rather than the core SHAY brand system, and should be verified before reuse in primary UI. `Work Sans` appears in the observed font-family list but its actual application (if any, given the `!important` Hanken Grotesk override) could not be determined. All display-tier font sizes, weights above what's declared, letter-spacing, and line-heights are proposed extrapolations from the small observed `--text-*` scale (11px–18px), not directly observed values. Breakpoints, mobile navigation behavior, hover/focus states, and card/grid layouts are proposed conventions only. Licensing and hosting terms for Hanken Grotesk were not verified in this extraction.
