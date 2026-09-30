---
version: alpha
name: "Q Acoustics"
source_url: "https://qacoustics.com"
captured_at: "2026-09-28T04:55:27.392100+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Q Acoustics' storefront evidence shows a Shopify-based theme built on Inter for
  interface type, paired with a monospace fallback stack (SFMono-Regular, Menlo,
  Consolas, Liberation Mono) that is likely reserved for technical or code-like UI
  elements such as order notes. Measured theme variables set --color-foreground to
  rgb(23 23 23) — #171717 — against a white --color-background, confirming a
  high-contrast, near-black-on-white editorial palette typical of premium audio
  hardware retailers. Among the remaining supplied hex values, most (for example
  #3b5998, #00acee, #e60023, #25d366, #f1e04d) match standard social-share icon
  colors and are deliberately excluded from brand role assignment; they are noted
  in Known Gaps rather than mapped to UI roles. The one non-social, non-neutral hex
  — #23185c, a deep indigo — is treated as an inferred primary accent, plausibly
  used for call-to-action emphasis or a brand mark, though its exact on-page
  application was not directly observed. Neutrals (#cccccc, #dedede, #e5e5e5,
  #333333, #121212) supply borders, muted text, and dark surfaces such as footer
  or hero-overlay panels. The interpretation favors a minimal, high-end audio
  aesthetic: generous whitespace, restrained color, bold Inter display type for
  hero product statements, and rounded pill controls consistent with the observed
  --rounded-full token used on the theme's lightbox buttons.

colors:
  primary: "#23185c"
  ink: "#171717"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#cccccc"
  hairline: "#dedede"
  surface-soft: "#e5e5e5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  surface-dark: "#121212"
  overlay: "#ffffffbf"
typography:
  display-xl: {fontFamily: "Inter, sans-serif", fontSize: 64px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "Inter, sans-serif", fontSize: 40px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.25px}
  title-md: {fontFamily: "Inter, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "SFMono-Regular, Menlo, Consolas, monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.muted}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: "{spacing.xxl}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlayColor: "{colors.overlay}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  swatch-selector:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
    size: "{spacing.lg}"

## Components

**button-primary** — Proposed as the main add-to-cart / "Shop Now" / "Reserve Now" control seen across hero slides and product grids. Uses the inferred indigo accent (#23185c) as its background; hover/active states were not observed and are proposed as a slight darken or opacity shift.

**button-secondary** — An outlined, lower-emphasis action (e.g. "View" or "Choose options" links) sitting on white/neutral surfaces, using the hairline border color rather than a filled background.

**text-input** — Covers fields such as the newsletter email capture, discount code entry, and search box. Border and padding are proposed; no focus-ring or validation styling was captured in the evidence.

**nav-bar** — A white, fixed-height top bar containing the site navigation (Shop, Our Story, Support, Contact), login, search, and cart icons observed in the page text. Sticky/scroll behavior is proposed, not confirmed.

**product-card** — Represents grid tiles like the 3090Ci, 5020, and 3050i listings, pairing a title, price, and color-variant swatches. Card border and radius are inferred defaults consistent with a clean commerce grid; no shadow values were present in evidence.

**hero** — The homepage slideshow ("Meet the 3040c", "Generation C", "SUBlime Sound") uses large display type over a dark or image background with a semi-transparent white overlay (#ffffffbf), matching the one alpha-white value present in the supplied palette.

**footer** — A dark, full-width block (mapped to #121212, a supplied near-black not otherwise assigned) housing quick links, policy pages, and social icons; proposed layout stacks link columns above a newsletter signup.

**badge** — Small pill labels for award callouts ("Product of the Year 2023") or stock/shipping notices ("Fast & Free Shipping"), using the full-radius token also confirmed by the theme's `--rounded-full` pagination/lightbox button.

**search** — An expandable/inline search affordance referenced in site navigation ("Search Site navigation"), styled as a soft rounded field distinct from the primary text-input to signal a lighter, secondary utility.

**swatch-selector** *(category-specific)* — A speaker-finish picker (e.g. Rosewood, Black, White Oak, English Walnut, Carbon Black, Arctic White) shown repeatedly in product listings; rendered as small circular swatches with a highlighted ring on the selected option, proposed to use the primary accent for the selection state.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior — no media queries or viewport-specific layout were present in the supplied evidence.

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| Mobile     | < 480px     | Single-column product grid, collapsed nav into a hamburger/drawer, sticky cart icon |
| Tablet     | 480–1024px  | Two-column product grid, condensed nav with visible search icon |
| Desktop    | 1024–1280px | Three to four-column grid, full horizontal nav (matches `--page-width`/`--page-container` tokens observed) |
| Wide       | > 1280px    | Content capped near the observed `max(var(--page-width), 1280px))` container ceiling |

Touch targets should be a minimum of 44×44px for nav icons, cart, and swatch selectors. Primary navigation is assumed to collapse into a drawer below tablet width; this assumption is not confirmed by observed CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from static CSS custom properties and page text only; no rendered layout, hover/focus states, or JavaScript-driven interactions (cart drawer, search overlay, slideshow transitions) were observed. Font sizes for `--text-h1` through `--text-h6` and `--title-lg`/`--title-xl` were expressed as `var(--sp-N)` spacing tokens without resolvable pixel values, so all typography sizes in this document are proposed estimates, not measured. Color-role assignment is uncertain: most of the supplied hex values (#3b5998, #00acee, #e60023, #3390f7, #25d366, #0064ff, #61f0f3, #ff3484, #f1e04d, #309fff, #b635ff, #049cff, #35ee7a, #00e166, #0066ec, #f7d00b, #f60e0e, #b700ff, #1990c6, #136f99) closely match conventional social-share icon brand colors and were excluded from primary/UI role mapping rather than guessed. The single accent color (#23185c) has no confirmed usage context and is an inferred brand accent only. Custom font licensing/availability for Inter was not verified beyond its presence in the supplied font-family list. Mobile navigation collapse, swatch-selector interaction states, and footer column structure are proposed patterns, not observed layout.
