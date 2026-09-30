---
version: alpha
name: "Lorena Canals"
source_url: "https://lorenacanals.com"
captured_at: "2026-09-28T09:22:18.166979+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Lorena Canals presents itself as a slow-textile, sustainability-led home and
  nursery brand, and the extracted evidence supports a warm, artisanal
  interpretation rather than a bright toy-store aesthetic. The observed
  palette centers on soft off-whites and warm neutrals ("#fcfbf9",
  "#f5f2ed", "#f4eddc") paired with an earthy dark-brown ink ("#392c22")
  and grey body text ("#333333"), which together read as natural-fiber,
  handcrafted, and calm — consistent with washable wool/cotton rugs
  photographed on light backgrounds. A muted brick-red ("#a92b39") appears
  repeatedly among product and review-star tokens and is proposed here as
  the primary brand accent; a soft teal ("#6a969a") and terracotta
  ("#cf7b59") are treated as secondary accents inferred from product-swatch
  colors, not confirmed as UI action colors. A blue ("#6394f8") appears only
  on a third-party gift-wrap widget and is excluded from core UI roles.
  Typography evidence lists both a serif family (Cormorant Garamond / EB
  Garamond) and sans-serif families (Alegreya Sans, Lato, Open Sans) among
  loaded fonts; CSS confirms only that h1/h2 and body pull from separate
  custom-property font tokens, so the serif-for-display, sans-for-body
  pairing below is an inferred, plausible mapping, not a measured one.
  Corners are treated as mostly soft/minimal, following the one observed
  radius signal (review widget uses 0 radius).

colors:
  primary: "#a92b39"
  ink: "#392c22"
  canvas: "#fcfbf9"
  body: "#333333"
  muted: "#7b7b7b"
  hairline: "#e6e6e6"
  surface-soft: "#f5f2ed"
  surface-card: "#fefefd"
  on-primary: "#ffffff"
  accent-teal: "#6a969a"
  accent-terracotta: "#cf7b59"
  star: "#e3d6c9"
  warm-cream: "#f4eddc"
  overlay-dark: "#00000066"

typography:
  display-xl: {fontFamily: "'Cormorant Garamond', 'EB Garamond', serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Cormorant Garamond', 'EB Garamond', serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "'EB Garamond', serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Alegreya Sans', 'Open Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Alegreya Sans', 'Open Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Lato', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Lato', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}

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
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    overlayColor: "{colors.overlay-dark}"
    headingTypography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.warm-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  rug-swatch-selector:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    labelTypography: "{typography.caption}"
    padding: "{spacing.xxs}"

## Components

**button-primary** is proposed for primary calls to action ("Add", "Shop Now") using the brick-red accent against white text, matching the warm, product-photography-led tone of the storefront; hover/active states are not observed and are proposed as a slight opacity or lift transition, consistent with the `--hover-*` custom properties present in the CSS.

**button-secondary** is an outlined variant for lower-emphasis actions (e.g. "View More", "Continue shopping") using ink-colored text and border on a transparent background, inferred from the site's minimal, text-forward navigation style.

**text-input** covers form fields such as newsletter signup ("Join The LC Family") and account/login forms; styling is inferred from generic card/surface tokens since no dedicated input CSS was supplied.

**nav-bar** models the observed multi-level mega-menu structure (Home, Kids, Rugs by Room, Customize, Collections, Get Inspired) on a light canvas background with a thin hairline divider; submenu animation timing (360ms, cubic-bezier easing) is directly evidenced in the CSS custom properties.

**product-card** reflects the repeated product-grid pattern in the page text (title, price or price range, "Add"/"Choose" actions) using a soft off-white card surface and hairline border; layout spacing is proposed, not measured.

**hero** represents the large editorial banners referenced in text ("Living in Wool", "Collection Editorial – Music Studio") with a dark overlay for text legibility over imagery; overlay opacity is proposed using the one observed alpha-black token.

**footer** is proposed as a dark ink-colored band for utility links and language/account selectors, inferred from typical ecommerce footer conventions since no footer-specific CSS was supplied.

**badge** covers small labels like "NEW", "Special Prices", or interactive-rug tags, using a warm-cream fill for a soft, non-alarming accent consistent with the nursery-decor category.

**search** is a pill-shaped input proposed for the header search affordance; no dedicated search CSS was present in evidence, so styling is fully inferred from the surface/hairline tokens.

**rug-swatch-selector** is a category-specific proposed component for choosing rug color/size variants (as implied by "Price range" and multiple color-named SKUs like "Persian Red / Natural / Pink"), using small circular swatches with an active-state ring in the primary accent color.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width      | Notes                                  |
|------------|-----------|-----------------------------------------|
| mobile     | <576px    | Single-column product grid, collapsed nav into hamburger/drawer |
| tablet     | 576–991px | 2-column product grid, mega-menu collapses to accordion |
| desktop    | 992–1439px| Full mega-nav, 3–4 column product grid |
| wide       | ≥1440px   | Max-width content container, larger hero imagery |

Touch targets should be a minimum of 44×44px for cart/add-to-bag icons and swatch selectors. The multi-level "Rugs by Room" / "Kids" mega-menu should collapse into a single-level accordion below tablet width. None of this is confirmed from captured DOM/media-query evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is limited to static CSS custom-property names, a color list, and page text; no rendered layout, spacing, or breakpoint values were captured, so the spacing/rounded scales above are proposed conventions, not measured site values.
- Font-role mapping (which family serves h1 vs. body) is inferred from the list of loaded font families; actual `--font-*` variable values were not resolved in the supplied CSS.
- No hover, focus, active, or error states were observed; all interaction states above are proposed and should be validated against the live site.
- Mobile/tablet navigation collapse behavior was not observed; the responsive table is a UX recommendation only.
- Border-radius evidence is limited to a single third-party review-widget token (`--jdgm-border-radius: 0`); the broader `rounded` scale is a standard proposed scale, not brand-confirmed.
- Custom font licensing/availability (e.g., Cormorant Garamond, Alegreya Sans) was not verified; assume standard Google Fonts distribution pending confirmation.
- The blue "#6394f8" and green tones ("#3ed660", "#006400") appear tied to a third-party gift-wrap app and were deliberately excluded from core brand token roles.
