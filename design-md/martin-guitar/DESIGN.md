---
version: alpha
name: "Martin Guitar"
source_url: "https://www.martinguitar.com"
captured_at: "2026-09-28T04:41:16.050633+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Evidence points to a heritage-forward acoustic instrument retailer built on a Salesforce Commerce Cloud (Demandware) storefront. The only brand-specific typeface found in the CSS is "Marsden Compact Bold," paired directly with a dark teal-green background (#245c4f) in a hero-style rule, suggesting a custom display face reserved for section headings or promotional banners. Body and UI copy fall back to the observed system/sans stack (Open Sans, Roboto, Noto Sans, Helvetica Neue, Arial), typical of a Salesforce-templated site rather than a custom brand typesystem.
  The supplied palette is broad and includes many likely UI-framework utility colors (Bootstrap-style grays, alert reds/greens/blues) alongside a smaller set of colors that plausibly carry brand meaning: the deep teal-green (#245c4f/#2b3830), a warm brass/gold (#c4a154) evocative of wood and hardware finishes, a muted cream (#edeae0/#dedad2) suited to product photography backgrounds, and a deep red (#a3080f) usable for sparing accents. This interpretation treats teal-green as primary, gold as a secondary wood-toned accent, and neutrals/cream as the surface system, with all other supplied hues retained for semantic states (link, success, warning) rather than brand identity. Layout, spacing, and interaction patterns below are proposed, not observed.

colors:
  primary: "#245c4f"
  primary-dark: "#2b3830"
  accent-gold: "#c4a154"
  accent-red: "#a3080f"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#4d4d4d"
  muted: "#6c757d"
  hairline: "#bebebe"
  surface-soft: "#edeae0"
  surface-card: "#dedad2"
  on-primary: "#ffffff"
  link: "#3091e7"
  success: "#008827"
  warning: "#ffcc00"
  danger: "#a3080f"
typography:
  display-xl: {fontFamily: "'Marsden Compact Bold', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Marsden Compact Bold', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Open Sans', 'Noto Sans', sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', 'Noto Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', 'Noto Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', 'Noto Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Open Sans', 'Noto Sans', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.2px}
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
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    hairline: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"

## Components
**button-primary** is proposed for primary calls to action ("Shop Now," "Add to Cart"), using the teal-green primary against white text; hover/active states are not observed and would need real interaction capture.

**button-secondary** is an outlined variant for lower-priority actions ("Learn More," "Compare Series"), sharing the same radius and type scale as the primary button but with transparent fill, proposed for visual hierarchy rather than confirmed in markup.

**text-input** covers search boxes, forms (serial lookup, dealer finder), using a light canvas fill with a thin hairline border; focus-ring styling is not observed and is left undefined.

**nav-bar** models the observed mega-menu structure implied by the deep category taxonomy (Guitars, Ukuleles, Strings, Custom Shop, Gear & Accessories); white background with dark text is proposed since no explicit header CSS was captured, only utility/video-player rules.

**product-card** is proposed for guitar/model listings (e.g., 16 Series, Road Series), using the muted card surface color to separate product imagery from the page background, with rounded corners for a modern catalog feel.

**hero** applies the one concretely observed background/typeface pairing (#245c4f + Marsden Compact Bold) to large promotional banners such as "New for 2026" or "Project 91," treating this as the strongest available brand signature in the evidence.

**footer** is proposed using the darker teal-green tone for a heritage, workshop-like footer band containing support links (Find a Dealer, FAQs, Shipping Policies) seen in the navigation text.

**badge** uses the gold/brass accent for labels like "New," "Signature," or limited-edition flags (Project 91, Special Editions), evoking hardware/fret-marker tones; this is an inferred stylistic choice, not a captured badge style.

**search** is a lightweight variant of text-input for the site's global search, set on the warm cream surface tone to differentiate it from standard form fields.

**product-spec-table** is a category-specific component for presenting guitar specifications (body size, tonewood, series) referenced throughout the navigation (Body Sizes, Wood Materials, Compare Series); proposed as a simple bordered key/value table using the soft surface background.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| mobile | 0–599px | Single-column nav collapses to a hamburger/menu icon; product cards stack full-width. |
| tablet | 600–1023px | Two-column product grids; sticky search bar. |
| desktop | 1024–1439px | Multi-level mega-menu visible; 3–4 column product grids. |
| wide | 1440px+ | Max-width content container with increased side padding using `{spacing.xxl}`. |

Touch targets are recommended at a minimum of 44x44px for buttons and nav items. Mega-menu collapse behavior, hover vs. tap interactions, and actual mobile navigation patterns were not observed and should be validated against the live site before implementation.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence was extracted from static CSS/text snapshots; no rendered layout, computed styles, or DOM structure were observed, so component composition above is inferential.
- The dark teal-green (#245c4f) and gold (#c4a154) are treated as brand colors based on limited signals (one hero-style CSS rule and general wood/guitar-industry plausibility); this mapping is not confirmed against a style guide.
- Most of the supplied palette (Bootstrap-style grays, alert colors, chart colors like #6610f2, #20c997) appears to originate from a UI framework rather than brand guidelines and has been assigned to semantic/system roles rather than brand identity.
- "Marsden Compact Bold" is used as-is from the CSS; its licensing, availability, and whether it is a licensed custom font or a mislabeled system font were not verified.
- All font sizes, weights, spacing, and radius values not explicitly present in the supplied CSS are proposed defaults for a content-rich commerce site and require design review.
- No interaction states (hover, focus, active, disabled), animation behavior, or mobile menu structure were observed; all such details are marked proposed above.
