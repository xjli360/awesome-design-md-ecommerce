---
version: alpha
name: "Avaline"
source_url: "https://drinkavaline.com"
captured_at: "2026-09-29T03:56:23.151591+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Avaline presents as a clean, ingredient-forward organic wine DTC site built
  on a warm, muted palette rather than a typical deep-cellar wine scheme.
  Observed CSS shows a dominant off-white/cream family (#f9f7f5, #f5f4e9,
  #f6f2e8) paired with a warm charcoal text color (#4d4844) that recurs across
  multiple template blocks, plus a warm brown (#856056) that appears
  repeatedly at varied alpha values (33, 4d, 66, 99), suggesting it functions
  as a recurring tint/accent rather than a single flat brand color — its role
  as "primary" here is inferred. A soft olive-gray (#70776b) also recurs with
  alpha variants and is mapped as a muted/secondary tone. Buttons
  (.btn-filled-dark, .btn-outline-dark) show real, observed styling: uppercase
  text, 2.38px letter-spacing, 14px/1.3 line-height, and 14px 50px padding,
  with a global reset forcing border-radius:0 on native form elements —
  treated here as the basis for a squared, editorial button language. Font
  evidence includes Basis Grotesque (Light/Medium/Regular) for UI and body
  text, Marion Standard (Regular/Italic) as a serif candidate for display
  headlines, and Fugue Mono bound to --font-mono. Serenity, Seriously
  Nostalgic, and Outfit are present in the font list but their applied role on
  the page is unconfirmed and treated as decorative/unassigned.

colors:
  primary: "#856056"
  ink: "#4d4844"
  canvas: "#ffffff"
  body: "#4d4844"
  muted: "#70776b"
  hairline: "#dedede"
  surface-soft: "#f9f7f5"
  surface-card: "#f5f4e9"
  on-primary: "#ffffff"
  accent-red: "#e73c3e"
  accent-blue: "#528ea7"
  accent-gold: "#dda860"
  sand: "#d4cfc0"
  stone: "#a79a93"
  slate: "#495363"
typography:
  display-xl: {fontFamily: "Marion Standard Regular, serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Marion Standard Regular, serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Basis Grotesque Medium, sans-serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.333, letterSpacing: 0px}
  body-md: {fontFamily: "Basis Grotesque Regular, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Basis Grotesque Regular, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4286, letterSpacing: 0px}
  caption: {fontFamily: "Basis Grotesque Light, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.333, letterSpacing: 0.5px}
  button-md: {fontFamily: "Basis Grotesque Medium, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 2.38px}
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
    padding: "{spacing.md} {spacing.xxl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xxl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    accent: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    overlay: "linear-gradient(224deg, rgba(211,38,38,0) 60%, rgba(0,0,0,0.9) 100%)"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  add-to-box-control:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    accent: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary** renders as a solid, squared call-to-action (e.g. "Shop Wines," "Add to box") using the warm brown `{colors.primary}` fill against white text, matching the observed `.btn-filled-dark` pattern of uppercase text, 2.38px tracking, and 14px/50px padding. Its `rounded.none` value reflects the observed global `border-radius:0` reset on native buttons rather than a rounded-pill treatment.

**button-secondary** mirrors `.btn-outline-dark`: transparent background, ink-colored border and text, same uppercase/tracked typography, intended for lower-emphasis actions like "Learn More." Hover-state color shifts toward a brand-green variable were present in CSS but no corresponding hex was supplied, so this state is proposed, not confirmed.

**text-input** is a proposed minimal field (search box, newsletter signup) using a hairline border and square corners consistent with the button reset pattern; no explicit input-field CSS was observed beyond the shared font-inherit reset rule.

**nav-bar** represents the top utility/nav strip implied by page text ("Skip to content," "Shop Wines," "Search," "AVALINE," cart/account links). Layout, sticky behavior, and exact height are inferred from typical DTC patterns, not measured.

**product-card** covers the repeated wine listings (White $24, Pinot Noir $30, etc.) shown in the text excerpt, using the cream `surface-card` background for a soft, paper-like product tile with an "Add to box" stepper control.

**hero** models the homepage banner ("A Fall Worth Savoring") using the one observed gradient overlay value, applied over a dark base with light text for legibility; exact hero height/crop is not observed.

**footer** is proposed from the presence of "Find Us," account, and secondary nav links in the text excerpt, using the muted olive-gray for lower-emphasis footer copy against the cream surface.

**badge** covers promotional callouts like "Unlock 15% in cart" or "Bestseller," using the one clearly red-ish observed hex (#e73c3e) as an inferred alert/highlight color — its brand role is not confirmed by name.

**search** is a proposed overlay/panel pattern implied by "Search Suggestions," "Trending," and "View Search Results" text, styled consistently with text-input.

**add-to-box-control** is a category-specific stepper (+/− quantity, "Add to box," "__COUNT__ __NAME__ added to box!") drawn directly from the page text's build-a-box/wine club flow, styled with the cream surface and brown accent for quantity affordances.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | ≤ 599px | Single-column product grid, collapsed hamburger nav, sticky "Build Your Box" summary bar |
| Tablet | 600–959px | 2-column product grid, nav condenses to icon-only search/account |
| Desktop | ≥ 960px | Multi-column grid (3–4 across), full horizontal nav with mega-menu-style "By Type"/"By Flavor Profile" panels |

Touch targets should be at least 44px tall for stepper controls and nav links. This table is a recommendation based on standard DTC ecommerce conventions, not measured breakpoints from the site's CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is drawn from static CSS/text extraction only; no rendered layout, spacing, or breakpoint values were directly observed.
- `--color-brand-green`, `--color-brand-green-bg`, `--color-noir`, `--color-off-white`, and `--color-red-blend` are referenced as CSS variables but their resolved hex values were not supplied, so `primary`/`badge` role assignments are inferred from the available literal hex palette instead.
- Font role mapping (Marion Standard as display/serif, Basis Grotesque as body/UI) is inferred from naming convention and typical DTC pairing, not from confirmed `font-family` declarations on specific elements.
- Serenity, Seriously Nostalgic, Fugue Mono (beyond its `--font-mono` binding), and Outfit have unconfirmed application and are not assigned to any typography token.
- Interaction states (hover, focus, disabled) beyond `.btn-outline-dark:disabled` and the two documented hover rules are proposed, not verified.
- Mobile/tablet layout, nav collapse behavior, and grid column counts are not observed and are marked as recommendations only.
- Font licensing/availability (webfont hosting, license terms) was not verified; treat all named fonts as requiring confirmation before production use.
