---
version: alpha
name: "Skout's Honor"
source_url: "https://skoutshonor.com"
captured_at: "2026-09-28T09:17:34.448880+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Skout's Honor presents as a clean, high-trust pet-care storefront built on Shopify's Dawn-derived theme architecture, evidenced by CSS custom properties like --color-background, --color-foreground, and a spacing scale (--sp-*) driving both layout and type sizing. The observed neutral core — white (#ffffff) canvas, near-black (#171717) foreground text, and mid-grey (#333333) for secondary UI like carousel controls — signals a restrained, product-forward palette typical of DTC pet brands. A single saturated red (#d82026) appears distinctly against the neutral system and is interpreted here as the primary brand/CTA accent, paired with white text for contrast. Two additional darks (#030f14, #121212) are treated as inferred deep-surface options for footer or high-contrast panels, not confirmed as brand-intentional. Light greys (#dedede, #e5e5e5) are mapped to hairlines and soft surface fills for card and section separation. Typography evidence lists Figtree and Merriweather among font_families; given heading/body CSS variables reference separate font-family tokens, Figtree is inferred as the body/UI sans and Merriweather as the heading serif, lending warmth to an otherwise utilitarian, science-forward brand voice ("microbiome-friendly," "B Corp"). Numeric type sizes are proposed, since source values resolve through an internal --sp-* spacing scale rather than static pixel figures. This interpretation favors clarity, generous whitespace, and a single confident accent for commerce actions.

colors:
  primary: "#d82026"
  ink: "#171717"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#dedede"
  hairline: "#e5e5e5"
  surface-soft: "#e5e5e5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  ink-deep: "#030f14"
  surface-dark: "#121212"
typography:
  display-xl: {fontFamily: "Merriweather, serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Merriweather, serif", fontSize: 34px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Merriweather, serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Figtree, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Figtree, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Figtree, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Figtree, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.2px}
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: "{spacing.xxl}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    hairline: "{colors.surface-dark}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  rating-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.xs}"

## Components

**button-primary** carries the single observed red accent (#d82026) as a solid fill, reserved for high-intent actions like "Shop Now," "Subscribe," and "Check out." Its rounded-sm corner and button-md typography keep it compact and legible against the light canvas. State: hover/active darkening is proposed, not observed in the CSS evidence.

**button-secondary** is an outlined, ink-on-white variant using the observed hairline grey (#e5e5e5) for its border, intended for lower-priority actions ("Learn More," "Continue shopping") that sit beside a primary button without competing for attention. Focus/hover treatments are proposed.

**text-input** reflects the newsletter and discount-code fields referenced in the page text ("Enter your email," "Discount code"). A thin hairline border and generous horizontal padding are proposed to match the general Shopify-theme input convention; no explicit input CSS was supplied.

**nav-bar** is inferred from the #shopify-section header block, which explicitly sets --color-background: 255 255 255 and --color-foreground: 23 23 23, plus a --topbar-height token. This supports a fixed-height, white nav with dark text and a bottom hairline for separation from page content; sticky/scroll behavior is proposed, not confirmed.

**product-card** draws on the repeated best-seller/team-favorite listing pattern in the page text (product name, star rating like "4.6," and price such as "$21.49"). A soft card border and modest corner rounding are proposed to visually group these repeating grid items; actual grid/flex implementation was not present in the supplied CSS.

**hero** corresponds to the top-of-page "Life-Changing Pet Essentials" headline and supporting copy. It uses the largest display typography scale and sits on the soft surface tone rather than pure white, offering separation from the nav without introducing a new, unobserved color. Copy alignment and imagery layout are proposed.

**footer** is mapped to the darkest observed near-black tones (#030f14 as background, #121212 as an internal hairline/divider) to differentiate the informational footer (hours, policies, social links) from the light body content, echoing the brand's B Corp/"Made in USA" trust messaging. This dark-footer pattern is inferred, not confirmed via footer-specific CSS.

**badge** represents small status labels such as "New" (seen before the HydroClear™ Collection) using the primary red pill shape for visibility. Full-rounded corners and caption-scale type keep it unobtrusive at small sizes; exact badge markup was not in the supplied CSS.

**search** models the site's visible search affordance ("Search Site navigation... Search Clear") as a bordered field consistent with text-input, prioritizing quick product lookup; live overlay/autocomplete behavior is proposed only.

**rating-badge** is the category-appropriate component for a grooming/pet-essentials storefront: a small, muted-surface chip showing the numeric star rating (e.g., "4.6," "4.9") adjacent to each product name in listings, reinforcing social proof without competing with the price or CTA typography.

## Responsive Behavior
This is a recommended breakpoint strategy, not measured site behavior, since no media-query evidence was supplied.

| Breakpoint | Width | Nav | Product Grid |
|---|---|---|---|
| mobile | <768px | Collapsed hamburger, search icon-only | 1–2 columns |
| tablet | 768–1024px | Condensed horizontal nav | 2–3 columns |
| desktop | >1024px | Full horizontal nav with dropdowns | 3–4 columns |

Touch targets are recommended at a minimum 44px height for buttons and nav items. Primary/secondary buttons should collapse to full-width on mobile. The search and account/cart icons in the header are assumed to remain persistently visible across breakpoints based on the header markup pattern in the page text, though exact responsive collapse was not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from static CSS custom properties, a partial page-text excerpt, and a discrete color/font list — no rendered layout, computed styles, or interaction states were observed. The mapping of Figtree to body text and Merriweather to headings is inferred from the font_families list and the presence of separate --font-body-family/--font-heading-family variables, but no rule confirming this pairing was supplied. Numeric type sizes in the typography tokens are proposed estimates, since actual values resolve through an internal --sp-* spacing scale without corresponding pixel output in the evidence. The red (#d82026) is assumed to be the primary brand accent based on its distinctiveness against the neutral palette, but no explicit --color-primary or CTA-specific rule was present. Dark tones (#030f14, #121212) are inferred for footer/dark-surface use without direct footer CSS. Hover, focus, active, and disabled states across all components are proposed conventions, not observed. Mobile navigation collapse, grid column counts, and touch-target sizing are recommendations only. Custom font licensing and self-hosting availability for Figtree and Merriweather were not verified.
