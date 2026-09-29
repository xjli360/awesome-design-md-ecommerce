---
version: alpha
name: "Rastelli's"
source_url: "https://rastellis.com"
captured_at: "2026-09-28T09:29:11.046463+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Rastelli's presents as a heritage butcher/e-commerce brand ("America's Personal
  Butcher," 50 years in business), built on a WordPress/Divi (et_pb_) stack with
  Open Sans as the primary observed body typeface (font-family: Open Sans, Arial,
  sans-serif; 14px; weight 500; line-height 1.7em). Headings inherit body font
  weight 500 and use a dark neutral ink (#333333) rather than pure black, giving a
  softer, editorial tone appropriate to a food-quality narrative. The palette
  pulled from CSS is broad (Divi/Gutenberg default swatches plus site-specific
  values); a deep maroon (#9b2242) and a bright sky blue (#2ea3f2, used on hover
  states and link colors like .posted_in, .nav-single a) stand out as the most
  brand-distinct, non-default colors and are treated here as primary/accent
  respectively — this mapping is inferred, not confirmed via a labeled brand
  token. Neutrals (#666, #999, #ddd, #f4f4f4, #333) form the grayscale system for
  body copy, muted text, hairlines, and soft surfaces. Buttons observed via
  .et_pb_button use a 2px solid border, 3px border-radius, and transparent
  background with hover-state overlay — reproduced here as button-secondary.
  Bebas Neue / bebas-neue-pro-semiexpanded appear in the raw font-family list but
  are not tied to a specific rule in the supplied evidence; their use as a
  display face for hero headlines is proposed/inferred to match a rustic butcher
  aesthetic, not confirmed.

colors:
  primary: "#9b2242"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#666666"
  muted: "#999999"
  hairline: "#dddddd"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#2ea3f2"
  button-dark: "#32373c"
  border: "#cccccc"
typography:
  display-xl: {fontFamily: "'bebas-neue-pro-semiexpanded', 'Bebas Neue', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.7em, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1.6em, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.5em, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Open Sans', Arial, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.7em, letterSpacing: 0px}
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
    borderWidth: "2px"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.primary}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.button-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    iconColor: "{colors.accent}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  weight-selector:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

**button-primary** — A solid, high-contrast call-to-action (e.g. "Shop Now," "Shop Online") using the maroon primary against white text. No hover/active/disabled state was observed in the supplied CSS; state styling is proposed to follow the .et_pb_button hover pattern of a light overlay.

**button-secondary** — Modeled directly on the observed `.et_pb_button` rule: transparent background, 2px solid border, 3px-family rounding, and a light-overlay hover state (`rgba(0,0,0,.05)` on light backgrounds, `hsla(0,0%,100%,.2)` on dark). Used for secondary actions like "Learn More."

**text-input** — Proposed pattern for search and form fields; no explicit input styling was present in the supplied evidence, so border, radius, and padding are inferred from the site's general neutral/hairline palette.

**nav-bar** — Proposed header treatment using a white canvas and dark ink text consistent with the body's neutral system; Divi/Et theme markup implies a standard horizontal nav, but its exact layout was not observed.

**product-card** — A category-appropriate pattern for meat/seafood SKUs: white surface card, hairline border, product title in title-md, and price emphasized in the primary maroon to draw attention against the neutral card background. Layout (image position, grid) is not observed and is proposed.

**hero** — Reflects the homepage's promotional messaging ("Celebrating 50 Years at America's Table"). Dark background with white text and a large display headline is proposed to match the emotive, heritage-brand copy; exact background treatment (image vs. solid color) was not confirmed in the CSS.

**footer** — Uses the dark neutral `#32373c` seen as the default WordPress button/element background, repurposed here as a plausible footer surface; actual footer markup/colors were not present in the supplied evidence.

**badge** — Proposed small pill component (e.g. "USDA Choice," "New") in primary maroon with white text, useful for a specialty-meat storefront to flag quality or freshness claims; not observed directly.

**search** — Icon-accented search field using the observed accent blue (#2ea3f2) for the icon/hover color, consistent with `#et_search_icon:hover` in the supplied CSS.

**weight-selector** — A category-specific component for choosing cut size or weight/quantity, common to butcher e-commerce. Fully proposed; no equivalent selector was present in the supplied evidence, but it follows the established neutral/primary token system.

## Responsive Behavior

Proposed breakpoints (not measured from live site):

| Breakpoint | Width      | Notes |
|---|---|---|
| Mobile | up to 479px | Single-column stacks, nav collapses to menu icon |
| Tablet | 480–980px | 2-column product grids; `--wp--style--global--content-size: 823px` suggests a content-width constraint near this range |
| Desktop | 981–1080px | Content constrained near `--wp--style--global--wide-size: 1080px` |
| Wide | 1081px+ | Max-width container centers content; generous side padding |

Touch targets should be at least 44×44px for buttons and nav items; the observed `.et_pb_button` padding (`.3em 1em`) is likely too small on its own for mobile touch and should be supplemented at small breakpoints. Nav collapse to a hamburger/off-canvas menu is standard for this theme stack but was not directly observed. This table is a recommendation only, not measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS extraction cannot confirm true rendered layout, grid structure, or component states (hover/focus/active/disabled) beyond the few rules explicitly captured (e.g. `.et_pb_button:hover`).
- The primary/accent color mapping (maroon #9b2242, blue #2ea3f2) is inferred from frequency and contextual link/hover usage, not from an explicit brand-token declaration.
- Bebas Neue / bebas-neue-pro-semiexpanded appear only in the raw font-family list without a matched selector rule in the supplied evidence; their assignment to `display-xl` is a proposed, unverified interpretation.
- All pixel sizes for typography beyond the confirmed `14px` body and `20px` button are proposed estimates, not observed values.
- Spacing scale, rounding scale, and most component paddings are proposed conventions layered onto the limited observed CSS (border-radius 3px on buttons is the only confirmed rounding value).
- Mobile/responsive interaction behavior (menu collapse, product grid reflow) was not observed and is a recommendation only.
- Custom font licensing/availability (e.g. Bebas Neue variants, ETmodules icon font) was not verified and should be confirmed before production use.
