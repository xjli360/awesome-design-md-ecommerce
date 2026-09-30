---
version: alpha
name: "Orcas Island Leather"
source_url: "https://orcasislandleather.com"
captured_at: "2026-09-28T09:13:42.428795+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Orcas Island Leather Goods is a Shopify-powered storefront for handcrafted DIY
  leather kits and finished leather goods (wallets, bags, belts, home goods) made
  on Orcas Island, Washington. The dominant observed text/heading color is a
  muted slate-navy (#2b445e), applied consistently to body copy, headings, and
  the logo link, giving the brand a coastal, understated tone rather than a
  typical "leather brown" palette. Headings use Bodoni Moda, a serif with
  editorial warmth, while body copy and interface elements (buttons, forms) use
  Lato, a humanist sans-serif — a classic serif/sans pairing for craft-goods
  retail. A third-party review widget explicitly declares #108474 (teal) as its
  "primary" color, which is adopted here as the interactive accent since no
  stronger brand accent is evidenced; this mapping is inferred, not confirmed
  from primary navigation or CTA markup. Neutral grays (#dddddd, #eeeeee,
  #95a2af) support hairlines, muted price text, and soft surface fills. A
  secondary blue (#1990c6/#136f99) appears only on an unbranded accelerated
  checkout button and is treated as a system/payment accent, not a core brand
  color. Layout structure (grid columns, spacing rhythm, breakpoints) is not
  present in the supplied CSS and is proposed by convention for an e-commerce
  storefront.

colors:
  primary: "#108474"
  ink: "#2b445e"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#95a2af"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  accent: "#1990c6"
  accent-hover: "#136f99"
  leather-tan: "#a09489"
typography:
  display-xl: {fontFamily: "'Bodoni Moda', serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0px}
  display-md: {fontFamily: "'Bodoni Moda', serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "'Bodoni Moda', serif", fontSize: 24px, fontWeight: 400, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Lato, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.625, letterSpacing: 0px}
  body-sm: {fontFamily: "Lato, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Lato, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Lato, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1, letterSpacing: 0.3px}
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
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    priceColor: "{colors.muted}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.leather-tan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  kit-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    descriptionTypography: "{typography.body-sm}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    padding: "{spacing.base}"

## Components

**button-primary** — Solid-fill call-to-action (e.g. "Add to Cart", "Check out") using the inferred teal accent as background with white text. Square corners follow the `--jdgm-border-radius: 0` convention observed in the review widget variables, extended here by inference to primary buttons generally. Hover/active/disabled states are proposed, not observed.

**button-secondary** — Outline-style button for lower-emphasis actions ("Quick shop", "View cart") using the ink navy as both text and border color on a transparent background, matching the restrained, non-decorative styling implied by the theme's flat button base (`background:transparent;border:0` in `.button` base rules, adapted for a bordered variant).

**text-input** — Standard form field styling (newsletter signup, search, account forms) with a light hairline border and body-copy color text. Focus/error states are proposed and not present in the supplied CSS.

**nav-bar** — Top navigation housing the "COLLECTIONS", "GIFTS", and account/cart controls referenced in the page text. White background with ink-navy text keeps continuity with the logo-link color rule (`color:#2b445e`) found in `.header-branding .logo-link`. Mega-nav / mobile collapse behavior is proposed, not observed.

**product-card** — Card wrapper for items such as the "Travel Cribbage Board" or "Nano Wallet" listings referenced in the featured-goods text. Price text explicitly uses the muted gray (`#95a2af`, 13px) per the `.product-price` rule; title uses the serif display style shared with page headings.

**hero** — Full-width introductory band ("Handcrafted leather goods made with island heart…") using a soft neutral background and the largest serif display size for the headline, paired with Lato body copy for the supporting paragraph. Exact hero imagery/layout is not present in the supplied CSS and is inferred from the page-text excerpt only.

**footer** — Dark-ink footer band containing legal links, newsletter, and social icons ("Facebook Pinterest Instagram YouTube") mentioned in the excerpt. Inverted text-on-dark treatment is proposed for contrast; exact footer background was not directly evidenced and is inferred from the ink token.

**badge** — Small pill label for merchandising flags such as "Just Added" or gift-price tiers ("Under $50", "Under $100") referenced in the collections list. Uses the warm leather-tan neutral as an evocative, non-primary accent; this color's badge role is inferred, not confirmed from markup.

**search** — Header search input styled identically to text-input, supporting the `header-search-button` icon rule (`chiko-icons` font-family) observed in the theme CSS for search/nav iconography.

**kit-card** — A category-appropriate component for the DIY Leather Kits collection, distinguishing kit listings (which combine a product title, short description, and a CTA to begin a project) from standard finished-goods product-cards. Structure is proposed by analogy to product-card, using the primary accent for its CTA to emphasize the "start making" action central to the DIY kit business line.

## Responsive Behavior

The following breakpoint table is a **recommendation**, not measured site behavior — no media queries or responsive layout rules were present in the supplied CSS.

| Breakpoint | Width      | Notes (proposed) |
|-----------|------------|-------------------|
| mobile    | 0–599px    | Single-column product grid, collapsed hamburger nav, stacked hero text |
| tablet    | 600–959px  | 2-column product grid, condensed nav links |
| desktop   | 960–1279px | 3–4 column product grid, full horizontal nav |
| wide      | 1280px+    | Max-width content container, generous section padding (`{spacing.section}`) |

Touch targets should be a minimum 44×44px for buttons and nav items per common accessibility guidance (not site-verified). Navigation should collapse into a disclosure/hamburger pattern below tablet width; this is a proposed pattern only, as no mobile nav markup or behavior was captured in the evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This document is derived from static CSS/text extraction only; no rendered page, computed layout, or DOM screenshots were available.
- Color **role assignments** (e.g. treating `#108474` as brand "primary" and `#2b445e` as "ink") are inferred from selector context and variable naming, not from confirmed brand style guidelines.
- All typography **sizes** beyond the explicitly observed values (body `16px`/`1.625` line-height, `.header-branding h1` `2.1428571429rem`, `.product-price` `13px`) are proposed and not directly measured for every listed scale step.
- No breakpoints, media queries, or responsive grid rules were present in the supplied CSS; the responsive table above is a convention-based recommendation only.
- No hover, focus, active, error, or disabled interaction states were observed in the evidence; all such states in this document are proposed.
- Mobile navigation, quick-shop modal behavior, and cart drawer layout were referenced in page text ("Quick shop", "Cart") but their visual/interaction design was not observed.
- Bodoni Moda and Lato availability, licensing, and exact weight range are not verified beyond their appearance in `font-family` declarations; fallback stacks (`serif`, `sans-serif`) are assumed generic system fallbacks.
- Rounded and spacing scales are proposed conventions; only the `border-radius:0` value for review-widget and accelerated-checkout buttons was directly observed.
