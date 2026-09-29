---
version: alpha
name: "Sfoglini"
source_url: "https://sfoglini.com"
captured_at: "2026-09-28T05:01:48.587719+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Sfoglini's supplied CSS centers on a single dominant brand teal, "#34617a", applied to
  body text, headings, and the site header/background, paired with a bold, uppercase,
  wide-tracked "Roboto Slab" for all heading and navigation typography and a plain
  "Inter" sans-serif for body copy. This pairing signals an artisanal, slightly rustic
  food-craft identity — serif slab headlines evoke Italian tradition and stamped-label
  typography, while the teal reads as a calm, non-food-primary brand color rather than
  a literal pasta or wheat tone. A warm off-white ("#f9f8f4") is inferred here as a soft
  canvas/surface tone appropriate to a flour/semolina-adjacent palette, since no true
  cream/wheat hex was present but the value is closest to a paper/dough tint in the
  observed set. A deep red ("#a32035") and gold ("#ffb400") are inferred as secondary
  accent candidates (badges, ratings, CTAs), drawn from the Italian-flag-adjacent reds
  and warm golds already present in the swatch. Neutral grays ("#777777", "#dddddd")
  are mapped to muted text and hairline dividers based on their consistent low-emphasis
  usage in fancybox and subheader rules. All layout proportions, spacing rhythm, and
  interaction states below are proposed, not measured.

colors:
  primary: "#34617a"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#34617a"
  muted: "#777777"
  hairline: "#dddddd"
  surface-soft: "#f9f8f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  secondary: "#18526f"
  accent: "#a32035"
  gold: "#ffb400"
  tint-info: "#d4eaf7"
typography:
  display-xl: {fontFamily: "Roboto Slab, serif", fontSize: "48px", fontWeight: 800, lineHeight: 1.1, letterSpacing: "1px", textTransform: "uppercase"}
  display-md: {fontFamily: "Roboto Slab, serif", fontSize: "26px", fontWeight: 800, lineHeight: 1.8, letterSpacing: "2px", textTransform: "uppercase"}
  title-md: {fontFamily: "Roboto Slab, serif", fontSize: "20px", fontWeight: 800, lineHeight: 1.4, letterSpacing: "1px", textTransform: "uppercase"}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.8, letterSpacing: "0px"}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  caption: {fontFamily: "Inter, sans-serif", fontSize: "11px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.5px"}
  button-md: {fontFamily: "Roboto Slab, serif", fontSize: "12px", fontWeight: 800, lineHeight: 1.2, letterSpacing: "2px", textTransform: "uppercase"}
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    padding: "{spacing.sm} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  shape-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components

**button-primary** uses the observed brand teal as fill with white text, following the slab-serif, uppercase, letter-spaced button/nav style found in `.nav a` rules. It is the default add-to-cart / primary CTA pattern. Hover/active states are proposed (e.g., slight darken toward "{colors.secondary}") and not confirmed by the static CSS.

**button-secondary** is a proposed outline variant for lower-emphasis actions ("View Recipe", "Learn More"), reusing the same typography token so all buttons share consistent voice while visually subordinating to the primary fill button.

**text-input** is inferred from generic form needs (newsletter signup, account fields visible in footer copy) since no explicit input styling was supplied; hairline border and soft rounding follow the restrained, low-ornamentation aesthetic implied by the rest of the sheet.

**nav-bar** directly reflects the observed `#header` and `.nav a` rules: solid teal background, white uppercase slab-serif links with 2px letter-spacing. The real header CSS shows `display:none` by default, so exact persistent/sticky behavior is not confirmed and is treated as proposed.

**product-card** is a proposed container for shop-grid pasta SKUs, using a plain white surface and hairline border since no explicit card shadow or radius was present in the evidence; this keeps the card visually quiet so product photography carries emphasis.

**hero** is proposed for homepage banner/collection intro sections referenced in the page text ("Try Our Newest Noodles!", "Explore All Sfoglini Pasta Collections"), using the largest display type and the primary teal as a full-bleed background, consistent with the brand-color-forward header treatment already observed.

**footer** mirrors the primary/on-primary pairing seen in the header, sized down to body-sm typography, matching the plain-text footer link list ("Home, Shop, Where to buy, FAQS, Press, Wholesale...") described in the page content.

**badge** is inferred for potential "New", "Limited-Edition", or sale labeling (the site text references "Specialty & Limited-Edition Pastas"), using the deep red accent pulled from the palette since no literal badge component CSS was supplied.

**search** is a proposed minimal input pattern for the (unconfirmed) site search affordance, styled consistently with text-input.

**shape-tile** is a category-specific component proposed for Sfoglini's core "Pasta Shape Artistry" concept — a card used to browse individual pasta shapes (e.g., Cascatelli, Reginetti, Cavatelli) with a soft cream surface suggesting flour/dough, a hairline edge, and slab-serif title typography matching the brand's heading style.

## Responsive Behavior

| Breakpoint | Approx width | Notes (proposed) |
|---|---|---|
| Mobile | <600px | Single-column stacks; nav collapses to a disclosure/hamburger pattern (a `summary`/`.nav summary` selector was present, suggesting a native `<details>`-style collapse mechanism, though its trigger visuals are unconfirmed). |
| Tablet | 600–1024px | Product/shape tiles move to a 2-column grid; header remains full-width. |
| Desktop | >1024px | Multi-column grids (3–4 across) for shop/shape listings; nav-bar shows full inline link list. |

Touch targets should be at least 44×44px for nav links and buttons. This table is a recommendation based on common Shopify-theme conventions and is **not** measured from live responsive behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted from static CSS/text only; no live DOM, computed styles, or rendered screenshots were available, so real layout, spacing, and grid structure are not confirmed.
- The `body { color: #34617a }` rule ties brand teal to base body text, which is unusual; `ink` was mapped to `#333333` as an inferred readability-oriented alternative rather than assuming teal is the actual paragraph copy color everywhere.
- `surface-soft` (`#f9f8f4`) and accent colors (`#a32035`, `#ffb400`) are present in the palette but their functional usage (backgrounds vs. incidental UI chrome) was not confirmed by selector context.
- No custom/licensed font files were observed beyond standard family names (Inter, Roboto Slab, Avenir, Helvetica); availability, weights, and licensing for production use are not verified.
- Interaction states (hover, focus, active, disabled) beyond the single `.fancybox-button` example are proposed, not observed.
- Mobile/tablet layout, breakpoint values, and nav-collapse visuals are not observed; the responsive table above is a design recommendation only.
- The captured page included a password/access-lock overlay (EasyLockdown app) and currency-selector markup unrelated to core visual design; these were excluded from styling decisions.
