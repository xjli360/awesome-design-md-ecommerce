---
version: alpha
name: "Snuggle Me Organic"
source_url: "https://snugglemeorganic.com"
captured_at: "2026-09-28T04:24:30.704028+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Snuggle Me Organic's observed palette pairs a muted slate-navy (#2b4970) with warm, undyed-linen creams (#faf9f6, #f4f2ec, #e7e7d6) and soft earth tones (#9b8e6f, #b2a37f), evoking organic textiles and nursery softness. Deep charcoal text (#1a1a1a, #3a3a3a) sits on cream and white surfaces for readability without stark contrast. A muted teal (#6a9bac) and a leaf green (#56ad6a) appear as secondary accents, plausibly tied to "organic/natural" badging, while two reds (#c01e25, #d02e2e) and a bright gold (#ffd200) are inferred as sale, alert, or promotional highlights given their saturation relative to the otherwise desaturated system.

  Font evidence lists both a serif (Sabon Next) and sans families (Avenir, Avenir Next, Poppins, Helvetica Neue) with body CSS confirming ~17px size, 1.6 line-height, and 0.03em letter-spacing. This interpretation assigns Sabon Next to display headings for an editorial, heirloom-brand feel, and Avenir Next/Poppins to body and UI text for clarity — this pairing is inferred, not verified from rendered pages. The custom-property naming (---color-primary, ---color-bg) confirms a themed Shopify design system but not exact hex-to-role bindings; role assignments below are best-fit inferences from context (nav height, dot indicators, model-viewer controls).

colors:
  primary: "#2b4970"
  ink: "#1a1a1a"
  canvas: "#faf9f6"
  body: "#3a3a3a"
  muted: "#666666"
  hairline: "#dedede"
  surface-soft: "#f4f2ec"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#c01e25"
  accent-sale: "#d02e2e"
  accent-green: "#56ad6a"
  accent-gold: "#ffd200"
  accent-earth: "#9b8e6f"
  accent-teal: "#6a9bac"
  deep-navy: "#223a56"
  error-bg: "#fff6f6"
typography:
  display-xl: {fontFamily: "Sabon Next, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Sabon Next, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Avenir Next, Avenir, Helvetica Neue, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0em}
  body-md: {fontFamily: "Avenir Next, Avenir, Helvetica Neue, sans-serif", fontSize: 17px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0.03em}
  body-sm: {fontFamily: "Avenir Next, Avenir, Helvetica Neue, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.02em}
  caption: {fontFamily: "Avenir Next, Avenir, Helvetica Neue, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.04em}
  button-md: {fontFamily: "Poppins, Avenir Next, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.05em}
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
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: "70px"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    shadow: "0 1px 3px rgba(0,0,0,0.05)"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.deep-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  playmat-spec-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    typography: "{typography.body-sm}"
    accent: "{colors.accent-earth}"

## Components
**button-primary** uses the navy primary as fill with white text, suited to "Add to Cart" and checkout actions; hover/active darkening is proposed, not observed. **button-secondary** is an outlined variant for lower-emphasis actions like "Learn More," sharing the same radius and type scale for visual consistency.

**text-input** assumes a plain white field with a light hairline border matching the cream-and-charcoal system; focus-ring color is unobserved and proposed as the primary navy at reduced opacity. **nav-bar** is inferred from the confirmed `--menu-height: 70px` custom property and the transparent-text nav variable, suggesting a fixed-height header that may switch text color over hero imagery — this transparency behavior is proposed, not measured.

**product-card** wraps loungers/playmats in a white surface with modest radius and shadow, reflecting typical Shopify PDP/collection grid patterns; exact shadow and hover-lift are inferred defaults, not extracted values. **hero** applies the display serif at large scale over a cream surface-soft background, appropriate for lifestyle photography sections common to organic/DTC gear brands.

**footer** is proposed on the deepest navy (#223a56) for contrast against the light body, holding link lists and newsletter signup in white text — this color-to-footer binding is inferred from tonal weight, not confirmed layout evidence. **badge** uses the green accent for "organic certified" or "in stock" labeling, a plausible but unverified semantic pairing given the color's isolation in the palette.

**search** proposes a pill-shaped input consistent with the `rounded.full` token, matching modern ecommerce search patterns; no search markup was present in the supplied evidence. **playmat-spec-panel** is a category-specific component for material/dimension callouts on Gear/Playmats PDPs, styled with the earth-tone accent to reinforce organic-material messaging.

## Responsive Behavior
This is a recommended structure, not measured site behavior:

| Breakpoint | Width | Nav | Grid |
|---|---|---|---|
| Mobile | <640px | Collapsed/hamburger, 70px bar | 1 column |
| Tablet | 640–1024px | Inline nav, condensed spacing | 2 columns |
| Desktop | >1024px | Full nav, `{spacing.section}` gutters | 3–4 columns |

Touch targets should meet a 44px minimum (aligned with the Swiper `--swiper-navigation-size:44px` evidence). Filter/search UI is proposed to collapse into a drawer below tablet width; this is a design recommendation, not an observed interaction.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
Evidence was extracted from static CSS/theme files, not a rendered browser session, so no live layout, hover states, animation, or breakpoint values were directly observed — the responsive table above is a proposed convention only. Color-to-role bindings (e.g., navy as primary, green as organic badge, red/gold as sale accents) are inferred from usage context and saturation contrast, not confirmed design tokens. Font-role assignment (Sabon Next for display, Avenir/Poppins for body) is inferred from the font-family list and generic body CSS; actual heading font usage was not verified. Custom font licensing and web-font availability (Sabon Next, Avenir, Avenir Next) were not verified. Component states (focus, hover, disabled, error) and mobile navigation behavior are proposed patterns for a Shopify-based gear/playmat storefront, not extracted from live interaction.
