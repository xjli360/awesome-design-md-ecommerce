---
version: alpha
name: "Whiteside"
source_url: "https://whitesiderouterbits.com"
captured_at: "2026-09-28T09:55:18.125697+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Whiteside Machine Company's storefront presents itself as an industrial, no-nonsense tools catalog, and the extracted CSS supports that reading. The body element sets a near-black background (#111111) with matching #111111 text, while headings and navigation consistently use Oswald in uppercase with 0px letter-spacing, giving the brand a stamped, machined feel. Body copy runs in Open Sans at 14px with a generous 1.8 line-height, suited to dense technical catalog listings. The signature accent is a deep industrial red (#ab112c), used for the utility header bar, link hovers, and active states, with a darker red (#8f051d) present in the palette as a plausible pressed/emphasis variant. Grays span from #666666 through #e8e8e8, evidencing a layered neutral system for borders, muted subtext, and card surfaces rather than a colorful UI. A pill-shaped gray CTA (#666666, ~35px radius) appears in the source and is generalized here to the rounded.full token. Because static CSS extraction cannot confirm true content-area backgrounds versus the page-frame color, canvas is inferred as white for card/content regions while #111111 is treated as both ink and outer frame background, reusing tokens per the observed evidence rather than assuming unverified layout.

colors:
  primary: "#ab112c"
  primary-deep: "#8f051d"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#111111"
  muted: "#777777"
  hairline: "#e8e8e8"
  surface-soft: "#f7f7f7"
  surface-card: "#f3f3f3"
  on-primary: "#ffffff"
  neutral-600: "#666666"
  border: "#dcdcdc"
  divider-on-dark: "#ffffff33"
typography:
  display-xl: {fontFamily: "Oswald, sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: 0px}
  display-md: {fontFamily: "Oswald, sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Oswald, sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.8, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.2px}
  button-md: {fontFamily: "Open Sans, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.neutral-600}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.xxl}"
  hero:
    backgroundColor: "{colors.ink}"
    overlayColor: "{colors.divider-on-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    dividerColor: "{colors.divider-on-dark}"
    typography: "{typography.button-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    altRowColor: "{colors.surface-card}"
    dividerColor: "{colors.hairline}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** is proposed as the main commerce action (add to cart, checkout) using the observed brand red (#ab112c) with white text, since this red is the only strong accent color repeated across header and hover states in the CSS.

**button-secondary** maps directly to the observed `.guest_button` pattern: a gray (#666666) pill-shaped control with a ~35px radius, generalized here to the `rounded.full` token; its hover behavior (text shifting to red while background stays gray) is an observed state and is proposed for reuse on secondary actions like "continue as guest" or "view details."

**text-input** is proposed for search and account forms; no explicit input-field CSS was supplied, so border, radius, and padding are inferred from the site's general neutral/hairline system rather than measured directly.

**nav-bar** reflects the `.nav a` and `#header` rules: uppercase Oswald links in white on a red utility bar. A second, image-overlay navigation context (`.feature_image .header .nav a`) with text-shadow was observed, suggesting the primary nav may sit transparently over a hero image rather than on a solid fill; this dual-context behavior is noted but not fully resolved from static CSS alone.

**hero** is proposed using the dark ink background and a translucent dark overlay observed in the palette (rgba blacks such as `#0000004d`), intended to hold large display typography and a CTA over a machinery/product photograph, consistent with the "Ranked #1" and "Family Owned Since 1970" promotional copy in the page text.

**product-card** is a proposed pattern for the extensive router-bit catalog grid; it reuses the observed `h2.product_name a` ink color and red hover, placed on a light neutral card surface with a hairline border for separation in a dense listing.

**footer** is inferred from `.footer_menu a` sharing heading typography (Oswald, uppercase) and the body's dark background rule, suggesting a dark footer band with light dividers; exact footer layout and columns were not present in the supplied CSS.

**badge** is proposed for trust markers like "Family Owned & Operated Since 1970," using the primary red as a compact pill label, since no dedicated badge class was present in the evidence.

**search** is proposed for the header "SEARCH" affordance referenced in the page text; visual treatment is inferred from the general input/neutral palette, not from a captured search-field rule.

**spec-table** is a category-appropriate addition for router-bit technical specifications (diameter, shank size, flute length, up-cut/down-cut) using alternating light surfaces and hairline dividers to support scannable technical data, a pattern not directly observed but reasonable given the product catalog's technical depth.

## Responsive Behavior

This is a proposed recommendation, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <600px | Single-column catalog list; nav collapses to a hamburger/drawer using `{colors.ink}` background; touch targets ≥44px. |
| tablet | 600–1024px | 2–3 column product-card grid; nav-bar remains horizontal with condensed spacing. |
| desktop | 1024–1440px | Full multi-column catalog grid; sidebar filters alongside spec-table content. |
| wide | >1440px | Max content width constrained; hero imagery scales, typography holds at `{typography.display-xl}`. |

Collapse behavior, sidebar filter interaction, and actual mobile menu implementation were not present in the supplied CSS and are proposed only.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from a static CSS/text extraction and carries the following limitations: no DOM screenshots or rendered layout were observed, so component composition (hero structure, card grids, footer columns) is inferred, not confirmed. The relationship between the dark `body` background (#111111) and predominantly white-seeming content areas is ambiguous from CSS alone; canvas/content-surface colors are a best-effort inference. Font availability for Oswald and Open Sans is assumed via standard web-font loading but licensing and actual delivery (self-hosted vs. third-party) were not verified. Sizes for `display-xl`, `display-md`, `body-sm`, `caption`, and `button-md` are proposed and not directly measured in the supplied rules, apart from `title-md` and `body-md`, which match observed `h1` and `body` declarations. No hover/focus/active states beyond the two explicitly captured (`h1 a:hover`, `.guest_button:hover`) were confirmed, so all other interaction states are proposed. Mobile menu, search overlay, and breakpoint values are recommendations only and were not present in the evidence.
