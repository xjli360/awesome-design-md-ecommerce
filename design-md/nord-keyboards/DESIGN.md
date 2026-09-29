---
version: alpha
name: "Nord Keyboards"
source_url: "https://www.nordkeyboards.com"
captured_at: "2026-09-28T09:15:16.479168+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is grounded in CSS extracted from the Nord Keyboards site, a Swedish
  manufacturer of stage pianos and organs. The defining brand color is a deep signature
  red (#8c1a11), applied consistently to active-state underlines, hover states on contact
  links, and primary button fills — a restrained, high-contrast accent against a
  black-on-white editorial base. Two darker red variants (#70150e, #54100a) appear in the
  palette and are inferred here as hover/active states for the primary red, since no
  distinct hover rule was observed. Body copy and navigation use a Helvetica Neue LT
  license family across several weight cuts (regular, medium, bold, heavy), with generic
  sans-serif fallback declared throughout — no proprietary web font beyond this licensed
  family is claimed. Grays (#e0e0e0, #f5f5f5, #fafafa, #757575, #9e9e9e, #bdbdbd) are
  mapped to hairlines, muted text, and card/surface backgrounds; these role assignments
  are inferred from typical usage patterns, not directly observed on those exact
  elements. A small set of status-like colors (green #2e8b48/#eaf7ee, red-orange
  #e0564a/#fdf2ed, blue #007aff) is present in the palette and is proposed here for
  success/error/focus states, though no corresponding component markup was observed. The
  overall interpretation favors a spare, product-photography-forward layout consistent
  with a premium instrument manufacturer.

colors:
  primary: "#8c1a11"
  primary-hover: "#70150e"
  primary-active: "#54100a"
  ink: "#000000"
  body: "#333333"
  muted: "#757575"
  muted-light: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-strong: "#bdbdbd"
  surface-soft: "#f5f5f5"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  canvas: "#ffffff"
  success: "#2e8b48"
  success-soft: "#eaf7ee"
  error: "#e0564a"
  error-soft: "#fdf2ed"
  focus: "#007aff"
  overlay: "#00000080"
typography:
  display-xl: {fontFamily: "Helvetica Neue LT W01_91488938, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Helvetica Neue LT W01_71488914, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Helvetica Neue LT W01_65 Md, sans-serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.32, letterSpacing: 0px}
  body-md: {fontFamily: "Helvetica Neue LT W01_41488878, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica Neue LT W01_41488878, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Helvetica Neue LT W01_41488878, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.68, letterSpacing: 0px}
  button-md: {fontFamily: "Helvetica Neue LT W01_65 Md, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.32, letterSpacing: 0px}
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
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "none"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    activeIndicatorColor: "{colors.primary}"
    typography: "{typography.body-md}"
    padding: "{spacing.none} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlayColor: "{colors.overlay}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.success-soft}"
    textColor: "{colors.success}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  compare-tray:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline-strong}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"

## Components

**button-primary** — The observed `.Button--Primary` rule sets a white-on-red fill (`#8c1a11`/`#fff`) with `border-radius:4px` and medium-weight type, used here for primary calls to action such as "Shop Now" or "Compare." Hover/active darkening to `#70150e`/`#54100a` is proposed, not observed.

**button-secondary** — Derived from `.Button--Secondary`: a white background with a solid black 1px border and black text, with an observed `transition:border .5s`. Proposed for secondary actions like "Learn more" alongside a primary button.

**text-input** — No dedicated text-input rule was observed; this is a proposed pattern styled consistently with the observed `SearchField` (no border, hairline underline) for use in newsletter or contact forms.

**nav-bar** — Based on `.Header__Wrap` (white background, `box-shadow:0 1px 1px #e0e0e0`) and `.Header__MenuLink`/`.Header__DropdownButton`, which reveal a red underline (`#8c1a11`, `height:3px`) animating on hover/active via `transform:scaleX`. This underline-reveal interaction is observed in the CSS transition properties, though the resulting visual behavior itself was not visually confirmed.

**product-card** — Proposed component for the eight-product lineup (Electro 7, Stage 4, Piano 6, etc.) described in the page text. Uses the light `surface-card` (`#fafafa`) against a hairline border, since no explicit card class was present in the supplied CSS.

**hero** — Proposed full-bleed banner for statements like "The Original Red Keyboards / Handmade in Sweden," using a dark/ink background with reversed white text, matching the brand's high-contrast red-black-white identity. Layout and imagery are not observed.

**footer** — Proposed structural pattern using the light gray surface tone and hairline dividers consistent with the palette's neutral grays; no footer-specific selector was supplied.

**badge** — Proposed small label component (e.g., "New" tags for products like Organ 3 or Stage 4) using the green success tokens present in the palette, which otherwise have no confirmed usage context in the supplied evidence.

**search** — Based on `.Header__SearchField`, which observably transitions `width` on interaction (48px base, expanding), with black text/placeholder and no border, implying an icon-triggered expanding search affordance.

**compare-tray** — A category-specific component proposed for the site's evidenced "Compare Products" feature, styled as a persistent bottom tray using the primary red as an accent for selected-item counts.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| Mobile | <600px | Single-column stacking, nav collapses to a hamburger/drawer, hero title drops to `display-md` scale |
| Tablet | 600–1024px | Two-column product grids, dropdown nav remains inline or condenses |
| Desktop | 1024–1440px | Full horizontal nav as observed (`Header__MenuLink` row), 3–4 column product grids |
| Wide | >1440px | Max-width content container, generous section padding (`spacing.section`) |

Touch targets should be at least 44px in height, particularly for the primary/secondary buttons and header dropdown triggers. The header's dropdown panels (`Header__DropdownContent`) should collapse into accordions on mobile given their absolute-positioned, full-width desktop implementation.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Extraction is static (CSS + text only); no rendered screenshots, computed styles, or DOM interaction states were available.
- Hover, focus, and active visual states (beyond the two explicitly observed underline/border transitions) are proposed, not confirmed.
- Numeric font weights for each Helvetica Neue LT cut were not supplied; weight mappings (400/500/600/700) are inferred from filename conventions (Rg/Md/Bold/Black-style naming).
- Font sizes for `display-xl`, `display-md`, and `product-card`/`hero` spacing are proposed design values, not measured from live layout.
- Semantic roles for several neutral grays (`muted`, `hairline-strong`, `surface-card` vs `surface-soft`) are inferred from typical usage conventions, not directly tied to observed selectors.
- Status colors (success, error, focus blue) exist in the extracted palette but no corresponding component markup was found in the supplied CSS; their assigned roles are speculative.
- Mobile/tablet navigation collapse behavior, product grid column counts, and compare-tray placement are proposed and have not been observed on the live site.
- Licensing and web-font availability of "Helvetica Neue LT W01" cuts and "Helvetica Neue for IB W01 Rg" have not been verified; these are proprietary licensed fonts referenced as-is with sans-serif fallback.
