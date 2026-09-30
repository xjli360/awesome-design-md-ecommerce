---
version: alpha
name: "Eagle Creek"
source_url: "https://eaglecreek.com"
captured_at: "2026-09-28T05:03:03.932014+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Eagle Creek's supplied CSS shows a neutral e-commerce shell (white canvas, near-black and mid-gray text tones) accented by an earthy olive-green pairing (#4b6633 hover state, #6c785a announcement button) and a warm sand/cream tone (#c9c1a6, #f2f0e9) consistent with an outdoor/adventure-travel positioning. Supporting hues include a utility blue (#0068c6, referenced as --ec-blue for link-style controls), a signal orange (#ec7f21) and red (#de3618) likely reserved for sale or alert badges, though their exact application was not directly observed beyond token presence.

  The body element's font-size/line-height (1.6rem/2.4rem = 16px/24px, 1.5 ratio) is the only directly measured type value; the resolved --font-body-family was not itself disclosed as a literal name, so "Lato" is treated as the primary observed candidate from the supplied font list, with Times, Garamond, IBM, and Inter carried forward as unconfirmed fallback candidates rather than confirmed brand fonts. The rebuy search overlay's uppercase, 800-weight, 14px product-title styling is the only confirmed weight/case treatment and informs the proposed button and caption styles. Radii, most spacing, and component states below are inferred defaults consistent with a Shopify-based storefront, not measured layout observations.

colors:
  primary: "#4b6633"
  secondary: "#6c785a"
  ink: "#232323"
  canvas: "#ffffff"
  body: "#353535"
  muted: "#757575"
  hairline: "#dedede"
  surface-soft: "#f2f0e9"
  surface-card: "#f6f6f6"
  on-primary: "#ffffff"
  sand: "#c9c1a6"
  deep-green: "#203012"
  link: "#0068c6"
  accent-orange: "#ec7f21"
  alert-red: "#de3618"
  border-strong: "#d1d1d1"
typography:
  display-xl: {fontFamily: "Lato, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Lato, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Lato, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Lato, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Lato, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Lato, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.5px}
  button-md: {fontFamily: "Lato, sans-serif", fontSize: 14px, fontWeight: 800, lineHeight: 1.2, letterSpacing: 0.5px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
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
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.deep-green}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.sand}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.alert-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-strong}"
    resultTitleTypography: "{typography.caption}"
    resultTitleColor: "{colors.ink}"
    linkColor: "{colors.link}"
    rounded: "{rounded.sm}"
  warranty-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.deep-green}"
    iconAccent: "{colors.secondary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base} {spacing.lg}"

## Components

**button-primary** anchors primary calls to action (e.g., "Shop Now") in the observed olive-green hover token (#4b6633), reversed to white text, matching the confirmed `.button:hover` background rule. Default (non-hover) state color is not directly confirmed and is proposed as the same tone for consistency.

**button-secondary** is a proposed outline treatment for lower-emphasis actions (e.g., "See More" in the quick-view search), using the primary green for text and border on a transparent field; the actual outline pattern was not observed and is inferred from common Shopify button pairing.

**text-input** covers search and newsletter fields; canvas background and hairline gray border are inferred defaults since no dedicated input CSS was supplied, aside from the newsletter button reference.

**nav-bar** models the header/submenu structure implied by "Featured/Luggage/Packing Cubes/Travel Bags/Accessories Submenu" text, using a white background and near-black ink text; exact height, spacing, and dropdown mechanics are not observed.

**product-card** reflects the light-gray (#f6f6f6) surface tone present in the palette, paired with the confirmed uppercase 800-weight product-title styling from the rebuy quick-view CSS, scaled here to body-sm for a general product grid context.

**hero** proposes a sand/cream (#f2f0e9) banner surface for feature promotions such as "Room to Experience More" or "Sustainably Made Gear," sized with the section spacing token; no hero-specific CSS was supplied, so this is an interpretive layout only.

**footer** uses the deep green (#203012) as a grounding dark surface with sand-colored links, inferred from the brand's earthy palette; actual footer background color was not confirmed in the supplied rules beyond generic `.footer-block` selectors.

**badge** applies the observed red (#de3618) for promotional or sale flags (e.g., "Up To 30% Off"), a proposed but palette-grounded use since no explicit badge selector was supplied.

**search** models the rebuy quick-view search flyout using the confirmed border color (#d1d1d1), uppercase bold result titles (#232323), and the `--ec-blue`-styled "see more" link, mapped here to the observed #0068c6 blue token.

**warranty-callout** is a category-appropriate proposed component for the repeated "No Matter What® Warranty" and "Easy 60-Day Returns" trust messaging seen throughout the announcement content, using sand surface and deep-green text to echo the brand's outdoor tone; no dedicated CSS for this element was supplied.

## Responsive Behavior

This is a recommended structure, not measured site behavior:

| Breakpoint | Width | Nav | Product grid |
|---|---|---|---|
| Mobile | <600px | Collapsed/hamburger | 1–2 columns |
| Tablet | 600–1024px | Condensed horizontal | 2–3 columns |
| Desktop | 1024–1600px | Full mega-menu | 3–4 columns |
| Wide | >1600px (page-width cap 160rem observed) | Full mega-menu, centered container | 4+ columns |

Touch targets should target a minimum 44px height for buttons and nav items; the mega-menu submenus (Featured, Luggage, Packing Cubes, Travel Bags, Accessories) should collapse into accordion-style disclosures on mobile. None of this collapse behavior was directly observed in the supplied CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is built solely from static CSS/text extraction and carries several limitations: the actual computed value of `--font-body-family` was not disclosed, so "Lato" is a best-candidate inference from the supplied font list rather than a confirmed brand typeface; Times, Garamond, IBM, and Inter appear in the evidence but their functional roles (if any) are unknown. Color-to-role mapping (e.g., which green is "primary" vs. "secondary," which grays serve as body vs. muted text) is inferred from limited hover/button context and may not match the live design system's intended semantics. All rounded-corner values, most spacing values, and most typography sizes beyond the single confirmed body font-size/line-height pair are proposed defaults, not measured. No interaction states (focus, active, disabled), animation behavior, or actual mobile/responsive layout were observed; the responsive table above is a general recommendation only. Font licensing and self-hosted vs. third-party delivery were not verified.
