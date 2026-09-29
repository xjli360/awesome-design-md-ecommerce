---
version: alpha
name: "Status Audio"
source_url: "https://status.co"
captured_at: "2026-09-28T09:22:39.735493+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Status Audio's storefront CSS exposes a navy-and-neutral system anchored by the custom
  property --Status-Blue (#202E3B), which drives all body copy and is treated here as the
  primary brand ink and inferred primary action color. The canvas is a warm off-white
  (#F9F9F9) with card surfaces stepping up to pure white (#FFFFFF) and a light gray utility
  tone (#F5F5F5) for secondary panels. A cooler light-blue family (#EEF1F2, #DCE6ED,
  #97B3C6, #BBDEFD) supports feature callouts and specs, consistent with an audio-tech
  positioning. A single saturated teal-blue (#1990C6, hover #136F99) appears only on the
  Shopify accelerated-checkout button and is mapped here as a secondary/checkout accent
  rather than the core brand primary, since evidence does not confirm it appears in
  standard site navigation or hero CTAs. Vibrant-Blue (#0A84FF) is defined as a root
  variable and is treated as an interactive/link accent, inferred pending confirmed usage.
  Status-Red (#9E2A2B) and Status-Green (#34C759) are reserved for error and success
  states respectively, and GoldenSound-Gold (#D5C095) is scoped to the limited-edition
  collaboration line. Typography relies on "Usual" as a likely custom display/brand
  typeface alongside Open Sans for body text and Helvetica Neue as a system fallback;
  all sizing below is proposed, as no rendered font sizes were captured.

colors:
  primary: "#202E3B"
  ink: "#202E3B"
  canvas: "#F9F9F9"
  body: "#202E3B"
  muted: "#666666"
  hairline: "#DDDDDD"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  accent: "#0A84FF"
  accent-checkout: "#1990C6"
  accent-checkout-hover: "#136F99"
  error: "#9E2A2B"
  success: "#34C759"
  gold: "#D5C095"
  light-blue-1: "#EEF1F2"
  light-blue-2: "#DCE6ED"
  light-blue-3: "#97B3C6"
  sky-blue: "#BBDEFD"
  swatch-onyx: "#444444"
  swatch-bone: "#DEDED5"
typography:
  display-xl: {fontFamily: "Usual, Helvetica Neue, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Usual, Helvetica Neue, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Usual, Helvetica Neue, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, Helvetica Neue, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, Helvetica Neue, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, Helvetica Neue, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Usual, Helvetica Neue, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.4px}
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
  button-checkout:
    backgroundColor: "{colors.accent-checkout}"
    backgroundColorHover: "{colors.accent-checkout-hover}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.base} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    height: "64px"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.primary}"
    compareAtColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-swatch:
    onyxColor: "{colors.swatch-onyx}"
    boneColor: "{colors.swatch-bone}"
    size: "20px"
    rounded: "{rounded.full}"
    borderColor: "{colors.hairline}"

## Components

**button-primary** uses the dominant navy (--Status-Blue) as an inferred call-to-action fill with white text, matching the site's use of that color for all body-level text and, by extension, primary chrome. Hover/focus states are not observed and are proposed as a modest opacity or darken shift.

**button-secondary** is a proposed outline variant sharing the navy ink for text and border on a transparent background, suited to secondary actions like "Learn More" links seen adjacent to product CTAs.

**button-checkout** is the one interaction pattern with directly observed CSS: a teal-blue (#1990C6) background darkening to #136F99 on hover, sized via clamp() height and square corners (border-radius 0), taken from the Shopify accelerated-checkout stylesheet. This is scoped to express/wallet checkout buttons and should not be assumed to represent the general brand CTA.

**text-input** is proposed using the card surface and hairline gray border observed in the mono-gray token set (#DDDDDD), since no explicit input styling was captured beyond a reset rule stripping default borders and radius.

**nav-bar** uses the observed `--header-height: 64px` variable and white card surface with navy text, reflecting the color inheritance rule applied to `body, body a, input, textarea, button`.

**product-card** is a proposed pattern for the Pro X / Between 3ANC listings, using white surface, an 8px radius, and navy pricing text with a muted strikethrough compare-at price, consistent with the "$249 $299"-style discount pattern seen in the page text.

**hero** is proposed for the homepage banner ("Introducing Pro X GoldenSound Edition"), using the off-white canvas and large display typography; no hero-specific CSS was supplied, so sizing and layout are inferred from typical DTC hero conventions.

**footer** is proposed as a navy-on-white-text block reflecting the deep link structure (Info & Policies, Connect, About) visible in the page text, though no footer-specific background color was directly observed.

**badge** uses the GoldenSound gold token for the limited-edition colorway callout, a plausible reuse of the one observed accent color outside the neutral/blue system.

**spec-swatch** reflects the actual `.product-variants` swatch rules (Onyx #444444, Bone #DEDED5, plus gradient-based Black Alloy and Moonbeam variants not fully resolved in evidence) used for color-option selectors on product pages.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <640px | Single-column product grid, nav collapses to hamburger, header height may reduce from the observed 64px |
| tablet | 640–1024px | Two-column product grid, condensed nav |
| desktop | 1024–1440px | Full nav bar, three/four-column product grid |
| wide | >1440px | Max-width content container, extra hero padding |

Touch targets should be at least 44px in the primary interactive axis, matching the observed `clamp(25px, …, 55px)` height range on the checkout button. Navigation is expected to collapse into a drawer or overlay below the tablet breakpoint; this was not observed and is a UX convention assumption.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS extraction did not capture rendered font sizes, so all typography scale values are proposed, not measured.
- The dominant navy (#202E3B) is inferred as the primary brand/CTA color based on its use as global text color; no button or nav-background rule confirming this was directly observed.
- "Usual" is treated as a likely custom brand typeface based on its appearance in the font list, but licensing, weights, and availability are not verified.
- Font Awesome families are present for iconography only and are excluded from the typography roles.
- Gradient-based swatches (Black Alloy, Moonbeam) reference CSS variables whose resolved hex values were not present in evidence and are therefore omitted from the color palette.
- No hover, focus, active, or error interaction states were observed beyond the single checkout button hover rule; all other states are proposed conventions.
- Mobile/tablet layout, grid column counts, and navigation collapse behavior were not observed and are UX-convention estimates.
- Rounded-corner values beyond the checkout button's `border-radius: 0` are proposed defaults, not confirmed site tokens.
