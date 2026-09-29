---
version: alpha
name: "Acid League"
source_url: "https://acidleague.com"
captured_at: "2026-09-29T04:00:22.395763+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Acid League's evidence draws from a Squarespace-hosted CSS bundle showing a restrained
  black/white/off-white base (#000000, #ffffff, #fffefa, #fafafa) accented by a warm
  coral-red (#f0523d) and a sharp lime-yellow (#e3e935), consistent with a playful,
  condiment-forward food brand. Grays (#272727, #3e3e3e, #666666, #d8d8d8, #e7e7e7)
  supply text and hairline roles. Observed font families include GT-Alpina-Standard-Bold
  and GT-Alpina-Standard-Light (a serif display pairing), new-spirit-condensed, Clarkson,
  Helvetica Neue, Arial, and ibm-plex-mono; several other families (Roboto, monospace,
  squarespace-ui-font) appear to be platform/UI defaults rather than brand-authored type.
  This interpretation assigns GT-Alpina-Standard-Bold/Light to display headlines for
  editorial warmth, Helvetica Neue/Arial to body copy for legibility, and ibm-plex-mono
  as an inferred accent for small caption/label text (e.g. store-locator tags), matching
  the CSS variable naming pattern for utility text seen in form/checkbox tokens. Coral
  (#f0523d) is proposed as the primary action color against the near-black ink and warm
  white canvas; lime (#e3e935) is reserved as a secondary highlight. All layout metrics,
  spacing, and component states below are proposed conventions, not measured observations.

colors:
  primary: "#f0523d"
  accent: "#e3e935"
  ink: "#000000"
  canvas: "#fffefa"
  body: "#272727"
  muted: "#666666"
  hairline: "#d8d8d8"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-strong: "#3e3e3e"
  neutral-100: "#f6f6f6"
  neutral-300: "#e7e7e7"
  neutral-500: "#999999"
typography:
  display-xl: {fontFamily: "GT-Alpina-Standard-Bold, serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "GT-Alpina-Standard-Light, serif", fontSize: 36px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "new-spirit-condensed, serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "ibm-plex-mono, monospace", fontSize: 12px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.5px}
  button-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  retailer-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.lg} {spacing.xl}"

## Components
**button-primary** is the coral call-to-action used for cart/purchase actions ("Shop Lil Croutons"); a solid fill with white text is proposed for contrast against the warm-white canvas. **button-secondary** offers an outlined ink-on-transparent variant for lower-emphasis actions like "Find a Store," echoing the outline-button CSS hooks (`primary-button-style-outline`) present in the source bundle. **text-input** is a light-bordered field for newsletter/email capture ("Sign Me Up!"), using body typography and a subtle hairline border consistent with the neutral grays observed. **nav-bar** is proposed as a flat, warm-white bar holding "Our Story / Recipes / Products" links with a thin hairline divider beneath, matching the near-white canvas tones. **product-card** groups product imagery, a condensed-serif title, and body-sized price/description text with rounded corners, intended for the Condiments/Dressings/Living Vinegars grid. **hero** pairs a bold serif display headline with supporting body copy on a soft off-white background, sized generously for the "Where taste and creativity collide" statement. **footer** inverts to full black with white text for the closing navigation and social links, echoing the strong ink/canvas contrast in the palette. **badge** is a small pill using the lime accent to flag "NEW!" items such as Lil Croutons. **search** is a rounded, low-emphasis field for site search, proposed rather than observed. **retailer-strip** is a muted-text horizontal band representing the Wegmans/Target/Whole Foods logo carousel, using caption typography and soft background tones.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:
| Breakpoint | Width | Nav | Grid |
|---|---|---|---|
| mobile | <600px | collapsed/hamburger (proposed) | 1-column product cards |
| tablet | 600–1024px | condensed inline nav | 2-column grid |
| desktop | >1024px | full inline nav | 3–4 column grid |

Touch targets should be at minimum 44×44px for buttons and nav links (proposed). Retailer-logo carousel and Instagram row are assumed to collapse to a horizontally scrollable strip on mobile; this is inferred from the "Item 1 of 10" / "Item 1 of 5" carousel markers in the page text, not from measured DOM/CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no live rendering, computed layout, or interaction states (hover/focus/active, mobile menu behavior) were observed. Semantic color roles (primary, accent, muted, hairline) are inferred by matching hex frequency and contrast patterns to typical brand usage, not confirmed via labeled CSS custom properties tied to brand identity. Several font families in the raw evidence (Roboto, squarespace-ui-font, social-icon-font, monospace) appear to be Squarespace platform defaults rather than brand-selected type, and were excluded from primary typographic roles. Font pairing assignments (display vs. body vs. caption) are proposed based on naming conventions (GT-Alpina = display serif, Helvetica Neue = body sans) and not verified against rendered output. All spacing, rounding, and breakpoint values are conventional proposals, not measured from the site. Licensing/availability of GT-Alpina, Clarkson, and new-spirit-condensed for reuse outside the original Squarespace license was not verified.
