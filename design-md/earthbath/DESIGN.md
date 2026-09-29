---
version: alpha
name: "Earthbath"
source_url: "https://earthbath.com"
captured_at: "2026-09-28T09:54:13.052959+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Earthbath's storefront CSS exposes a compact palette built around a saturated blue (#0076c7 / #0176c7, used as header text color and the loading-bar accent) paired with a warm orange (#ff8920) that likely functions as a secondary call-to-action or promotional accent, though its exact usage was not visually confirmed. Neutral values run from pure white (#ffffff) canvas through light grays (#eeeeee, #e2e2e2, #dedede) for surfaces and hairlines, down to near-black (#000000, #121212) for ink. Several near-black alpha values (#0000001a, #00000012, #00000026, #00000033) suggest layered shadow/overlay treatments typical of a Shopify Dawn-derived theme. Typography is dual-track: a custom display face ("Oz Handicraft" / "OzHandicraft BT") appears in the font stack and is inferred to drive headings and hero copy for a friendly, handcrafted brand voice, while Arial/Helvetica carry body and UI text for legibility. Heading scale is explicitly defined via CSS custom properties across at least two breakpoints (58–72px H1/display down to 18–20px H6), giving a confident, generous editorial rhythm. Button and form-field heights are fixed at 52px (44px for small buttons), implying a comfortable, touch-friendly control size. All semantic role assignments (primary vs. accent, surface tiers) are inferred from usage context, not confirmed brand guidelines.

colors:
  primary: "#0076c7"
  primary-hover: "#136f99"
  accent: "#ff8920"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#767676"
  muted: "#767676"
  hairline: "#dedede"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-soft: "#e2e2e2"
  overlay-scrim: "#00000033"
  overlay-faint: "#0000001a"
  transparent: "#00000000"
typography:
  display-xl: {fontFamily: "'OzHandicraft BT', 'Oz Handicraft', Arial, sans-serif", fontSize: "62px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'OzHandicraft BT', 'Oz Handicraft', Arial, sans-serif", fontSize: "44px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "'OzHandicraft BT', 'Oz Handicraft', Arial, sans-serif", fontSize: "28px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "13px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "14px", fontWeight: 700, lineHeight: 1, letterSpacing: "0.3px"}
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
    backgroundColor: "{colors.transparent}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.transparent}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.border-soft}"
    height: "52px"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    hairline: "1px solid {colors.hairline}"
    position: "sticky (proposed, inferred from --enable-sticky-header: 1)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.button-md}"
    rounded: "{rounded.md}"
    hairline: "1px solid {colors.border-soft}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    hairline: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.border-soft}"
    height: "52px"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"

## Components
**button-primary** anchors primary conversion actions (Add to Cart, Shop Now) using the blue brand color observed as the header/logo tone; the 52px control height matches the site's `--button-height` variable. **button-secondary** is a proposed outline variant for lower-emphasis actions like "Learn More," reusing the primary blue as text/border on a transparent field. **text-input** and **search** both draw from the observed `--form-input-field-height: 52px` and a light hairline border consistent with `.input__field` rules; focus/error states are proposed, not observed. **nav-bar** reflects the confirmed sticky-header flag (`--enable-sticky-header: 1`) and the white background/blue text pairing from `#shopify-section-header`; mobile collapse behavior is inferred, not measured. **product-card** is a proposed pattern for the grid of shampoos/wipes/conditioners referenced in navigation, using a card surface with soft border and standard corner radius since no explicit card CSS was supplied. **hero** models the observed large slideshow headline treatment (e.g., "Zero gunk. All vibes.") using the largest display type scale and generous section padding drawn from the `--vertical-breather` values (64–90px across breakpoints). **footer** groups the extensive link taxonomy (Company, Support, Community) seen in page text, using muted body copy and primary-colored links consistent with the site's link hover rule. **badge** is proposed for promotional or "Sale price" callouts, borrowing the orange accent for visual contrast against the blue-dominant palette. **filter-chip** is a category-appropriate pattern for the "By Life Stage" and "By Concerns" navigation groups (Allergies, Shedding, Dry Skin, etc.), proposed as pill-shaped toggles with an active state in brand blue.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior. CSS variables show at least two responsive tiers (a tighter mobile set with 58px H1/40px gutter-scale values and a wider desktop set with 62–72px display sizes), implying a mobile-first fluid type scale.

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | 0–599px | Single-column stacks, nav collapses to menu icon, `--vertical-breather: 64px` |
| Tablet | 600–999px | 2-column product grids, `--vertical-breather: 80px` |
| Desktop | 1000px+ | Full 20-column grid (`--grid-column-count: 20`), `--vertical-breather: 90px` |

Touch targets should meet a 44–52px minimum height, matching the observed `--button-height` (52px) and `--button-small-height` (44px) tokens. Sticky header behavior is confirmed via `--enable-sticky-header: 1`; sticky announcement bar is disabled per `--enable-sticky-announcement-bar: 0`.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is derived solely from static CSS custom properties, selector declarations, and page text supplied as evidence; no rendered layout, interaction states (hover/focus/active), or mobile behavior were directly observed. The role of orange (#ff8920) as an accent versus a rarely-used utility color is inferred from its presence in the palette alongside a dominant blue, not confirmed by component-level CSS. The `--header-border-color` value (rgb 217,234,247) was excluded because it has no corresponding hex entry in the supplied observed palette. Font family "Oz Handicraft"/"OzHandicraft BT" is treated as a licensed or self-hosted custom display font whose availability, licensing, and exact glyph coverage were not verified. Heading and section spacing values were taken directly from `:root` custom properties across cascading breakpoint blocks, but the precise pixel-to-breakpoint mapping was not confirmed from a live viewport test. Component patterns without direct CSS evidence (product-card, badge, filter-chip, hero padding) are labeled proposed and should be validated against real rendered pages before implementation.
