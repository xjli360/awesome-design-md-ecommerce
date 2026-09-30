---
version: alpha
name: "Snake River Farms"
source_url: "https://snakeriverfarms.com"
captured_at: "2026-09-28T09:12:00.925723+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Snake River Farms presents itself as a heritage American Wagyu and Kurobuta pork
  purveyor, and the extracted CSS confirms a restrained, editorial palette built on
  near-black text (#222020, #121212) against white and light-grey surfaces
  (#ffffff, #f7f7f7, #e9e9ea). Buttons observed in theme markup are flat
  (border-radius: 0), either solid dark-on-white outlined pairs or filled dark
  fills, signaling a butcher-shop/utility aesthetic rather than rounded e-commerce
  softness. A small red (#a8291f) and green (#174907) pair are declared as
  --error/--success tokens, inferred here for stock and validation states. A
  gold tone (#b59410 on #fff8db) appears in the wider palette and is inferred
  as the premium "SRF Gold Plus™" tier badge, unconfirmed in the supplied rule
  set. Typography mixes Josefin Sans (likely display/heading use), Roboto
  (probable body face), and Gowun Batang, a serif that plausibly styles recipe
  or editorial copy given the site's recipe-forward content. Body text uses an
  explicit 0.06rem letter-spacing and 1.5rem base size per :root CSS. Layout
  patterns (hero overlays, product grids, subscription messaging) are inferred
  from repeated homepage text blocks, not measured DOM structure. This
  specification proposes a flat, high-contrast, protein-forward interface
  consistent with the observed tokens.

colors:
  primary: "#222020"
  primary-active: "#000000"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#575656"
  muted: "#75757a"
  hairline: "#d7d7d9"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  secondary: "#4a4a51"
  secondary-active: "#915bb4"
  border-strong: "#acacaf"
  accent-gold: "#b59410"
  accent-gold-bg: "#fff8db"
  error: "#a8291f"
  success: "#174907"
  focus-ring: "#4400ff"
  grey-3: "#e9e9ea"
typography:
  display-xl: {fontFamily: "Josefin Sans, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Josefin Sans, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Josefin Sans, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: "0.06rem"}
  body-sm: {fontFamily: "Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.04rem"}
  caption: {fontFamily: "Roboto, sans-serif", fontSize: 10px, fontWeight: 700, lineHeight: 0.9, letterSpacing: "0.02rem"}
  button-md: {fontFamily: "Roboto, sans-serif", fontSize: 12px, fontWeight: 700, lineHeight: 1.0, letterSpacing: "0.02rem"}
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
    padding: "{spacing.sm} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    hoverBackgroundColor: "{colors.surface-soft}"
    hoverBorder: "2px solid {colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    focusRing: "{colors.focus-ring}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    height: "proposed 72px"
    cartBadgeBackground: "{colors.primary}"
    cartBadgeText: "{colors.on-primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    salePriceColor: "{colors.error}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.primary}"
    overlayTextColor: "{colors.on-primary}"
    eyebrowTypography: "{typography.caption}"
    headlineTypography: "{typography.display-xl}"
    ctaComponent: "button-secondary"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    hairline: "{colors.secondary}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    inStockBackground: "{colors.success}"
    inStockText: "{colors.on-primary}"
    saleBackground: "{colors.error}"
    saleText: "{colors.on-primary}"
    premiumBackground: "{colors.accent-gold-bg}"
    premiumText: "{colors.accent-gold}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    iconColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  recipe-card:
    backgroundColor: "{colors.surface-card}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    accentFont: "Gowun Batang, serif (proposed decorative use)"
    ctaComponent: "button-primary"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
  subscription-widget:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.secondary-active}"
    discountBadge: "{colors.accent-gold-bg} / {colors.accent-gold}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components
**button-primary** uses the dark near-black fill (#222020) with white text, matching the `--color-button`/`--color-button-text` root tokens; this is the confirmed default Shopify button pairing on this theme.

**button-secondary** mirrors an observed outlined pattern (`.featured-button-template`) with white background, 2px dark border, and a hover state that lightens to grey-1 with a grey-6 border — directly lifted from supplied CSS.

**text-input** is proposed using the grey-1 surface and grey-4 hairline seen elsewhere in the palette, with the declared `--ada-outline` (#4400ff) applied as the focus ring for accessibility compliance; exact input styling was not present in the supplied rules.

**nav-bar** is inferred from the presence of "My Account," cart count, and search text in the page excerpt; white background with dark text is consistent with the root color variables, though header layout itself was not observed.

**product-card** reflects the repeated price patterns in the text (e.g., "$79.00 $69.00"), so a strikethrough/sale-price treatment in the error red is proposed; card chrome (border, flat corners) follows the site's zero-radius button convention.

**hero** is inferred from `.body_copy *:not(a) { color: var(--white) }` rules tied to hero/skinny-hero sections, implying dark-image-with-white-text banners; background fill here uses the primary dark token as a stand-in since actual hero imagery wasn't supplied.

**footer** is proposed as a dark ink-toned band for contrast and wayfinding; no footer-specific CSS was supplied, so this is an inferred, category-typical pattern.

**badge** covers three proposed states — success/in-stock (green), sale (red), and a gold "Gold Plus™" premium tier badge inferred from the product taxonomy text ("SRF Gold Plus™") and the presence of gold/cream tones in the broader palette.

**search** and **subscription-widget** are both directly motivated by literal page copy ("Enter the keyword to search," "Subscribe and Save! Up to 10% off"); styling is proposed using existing soft-grey and gold/purple accent tokens since no dedicated component CSS was extracted.

**recipe-card** responds to the recipe content block ("Double Bone Pork Chops with Brown Butter Peanut Vinaigrette... MAKE NOW") and proposes the serif Gowun Batang for a more editorial, recipe-magazine feel distinct from the sans-serif commerce UI — this pairing is a design proposal, not a confirmed usage.

## Responsive Behavior
This breakpoint table is a **recommendation**, not measured site behavior:

| Breakpoint | Width | Layout notes |
|---|---|---|
| mobile | <600px | Single-column product grid, collapsed nav to hamburger, sticky search icon |
| tablet | 600–1024px | 2-column product grid, condensed hero copy |
| desktop | 1024–1440px | 3–4 column product grid, full nav bar visible |
| wide | >1440px | Max content width ~1280px, extra whitespace margins |

Touch targets should be a minimum 44×44px for buttons and nav icons. Navigation should collapse to a hamburger/drawer pattern below tablet width; filters and subscription controls should stack vertically on mobile. None of this was confirmed via responsive CSS in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from static CSS custom properties, a limited set of component-level selectors, and homepage text content — not a rendered or interactive audit of the live site. Several gaps remain:

- **Semantic color mapping is inferred**: roles like `body`, `muted`, and `hairline` are approximated from the closest matching grey-scale tokens (`--grey-1` through `--grey-9`), since exact usage per role wasn't traceable in the supplied rule set.
- **Gold/cream badge tokens** (#b59410, #fff8db) appear in the observed palette array but were not tied to a specific selector in the supplied CSS; their "Gold Plus™" badge role is a plausible but unconfirmed inference.
- **Typography sizes are largely proposed.** Only button (12px/700), image-button caption (10px/700/90%), and body letter-spacing (0.06rem) were explicitly observed; display/title sizes are estimated for a premium food-commerce hierarchy.
- **Layout, grid, hero imagery, and footer structure were not observed** — no layout/grid CSS was supplied, so all structural components above are proposed patterns based on textual content cues only.
- **Interaction and mobile behavior were not observed**; hover states exist for two button variants only, and no responsive/media-query CSS was included in the evidence.
- **Font licensing/availability is unverified.** Josefin Sans, Roboto, and Gowun Batang are listed as observed families in the CSS but whether they are self-hosted, Google Fonts-linked, or otherwise licensed for reuse was not confirmed.
