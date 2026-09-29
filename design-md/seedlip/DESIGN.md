---
version: alpha
name: "Seedlip"
source_url: "https://seedlipdrinks.com"
captured_at: "2026-09-28T04:33:11.253546+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Seedlip's public site evidence points to a botanical, apothecary-inspired
  identity built on deep forest greens, warm neutrals, and a single citrus-
  yellow accent. The palette centers on a dark bottle green (#154734) paired
  with near-black greens (#091c14, #042b1a) for text and dense surfaces,
  offset by a warm cream (#fff1e4) and soft sage/tan neutrals (#e8edeb,
  #d0d5cc, #f0bf9b, #fdd086) that read as label stock and botanical
  illustration tones. #ffcd00 is treated as the sole high-chroma accent for
  callouts and badges; its role as "brand accent" is inferred from contrast
  against the greens, not confirmed brand guidelines. A blue focus ring
  (#2189d4) is directly observed in the CSS as an accessibility outline
  color and is retained only for that purpose. Typography uses three custom
  families (mollieGlaston, brCandor, fsNeruda) referenced with explicit
  "Fallback" variants; generic serif/sans-serif stand-ins are used here since
  the proprietary glyphs cannot be verified. The interpretation assumes
  mollieGlaston serves display/editorial headlines, brCandor for structural
  titles, and fsNeruda for body and UI text — all font-role assignments are
  inferred from naming convention only. Radius and spacing scales approximate
  the site's rem-based design tokens (e.g. --radii-large:100px, --space-*
  variables) at common breakpoint tiers.

colors:
  primary: "#154734"
  ink: "#091c14"
  canvas: "#ffffff"
  body: "#091c14"
  muted: "#666666"
  hairline: "#eaeaea"
  surface-soft: "#fff1e4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#ffcd00"
  accent-soft: "#e3e48d"
  tan: "#f0bf9b"
  peach: "#fdd086"
  pale-blue: "#b9d3dc"
  sage: "#e8edeb"
  sage-dark: "#617c71"
  forest-deep: "#042b1a"
  focus-blue: "#2189d4"
  overlay-dark: "#0000004d"
  overlay-light: "#ffffff66"
typography:
  display-xl: {fontFamily: "mollieGlaston, serif", fontSize: 88px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "mollieGlaston, serif", fontSize: 56px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "brCandor, sans-serif", fontSize: 30px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "fsNeruda, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "fsNeruda, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "fsNeruda, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "fsNeruda, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.2px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    focusRing: "{colors.focus-blue}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    borderBottom: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  hero:
    backgroundColor: "{colors.forest-deep}"
    overlay: "{colors.overlay-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  flavor-tag:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.sage}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

**button-primary** – The dominant call-to-action treatment, using the deep bottle-green fill against a white label. Pill-shaped radius is drawn from the observed `--radii-large:100px` token. Hover/active states exist in the source CSS (`.br-button-primary:hover/:active`) but their exact color values are HSL custom properties not resolvable from static evidence; a darker-green hover is proposed but unverified.

**button-secondary** – An outline variant mirroring the site's `.br-button-outline` class, transparent by default with a green border and text, filling on hover. Exact hover fill is proposed, not observed.

**text-input** – A minimal bordered field for newsletter/search forms. The focus outline color is one of the few directly observed interaction styles (`outline-color:var(--blue-600)` on `:focus-visible`), mapped here to `focus-blue`.

**nav-bar** – Proposed as a dark-green header bar carrying the wordmark and primary links in cream/white type; sticky behavior and exact height are not confirmed by the evidence supplied.

**hero** – A full-bleed introductory panel using the forest-deep background with a dark scrim (`overlay-dark`, matching an observed `#0000004d` token) to seat white display type. Content pairing (image vs. video) is not observed.

**product-card** – Represents a spirit/product tile: white surface, soft border, product name in title-md, price in body-sm. Shadow/elevation is proposed, not confirmed by CSS evidence.

**flavor-tag** – A category-appropriate chip for labeling botanical notes (e.g. "Citrus", "Spice", "Grove"), using the pale accent-soft yellow-green tone observed in the palette. Purely inferred as a merchandising pattern for a non-alcoholic spirits brand.

**badge** – A small pill using the singular high-chroma yellow accent, proposed for "New" or promotional flags; no such badge was directly observed in the supplied CSS.

**search** – A pill-shaped input consistent with the button radius convention, proposed for site search; icon placement and behavior are not observed.

**footer** – A dense near-black green band with sage-toned link text, echoing the header's dark palette for a bookended layout; column structure is proposed, not measured.

## Responsive Behavior
| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| Mobile    | < 640px     | Single-column stacks; nav collapses to a hamburger menu (not observed) |
| Tablet    | 640–1024px  | Two-column product grids; spacing steps down per the smaller `--space-*` tier observed in CSS |
| Desktop   | > 1024px    | Multi-column grids; typography steps up to the larger `--fontSize-*` tier observed in CSS |

Touch targets should be at least 44px in the proposed scale, using `{spacing.md}`–`{spacing.lg}` padding on interactive elements. Breakpoint pixel values and collapse behavior are recommendations only; no live responsive layout was observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Colors were extracted from static CSS/JS bundles; no live rendering or screenshot was captured, so actual applied roles (e.g., which green is truly "primary" vs. a background tint) are inferred from frequency and contrast, not confirmed.
- Button/component state colors (hover, active, secondary, outline) reference HSL custom properties (`--component-button-color-*`) whose resolved values were not present in the supplied evidence; described hover/active behavior is proposed.
- Font families (`mollieGlaston`, `brCandor`, `fsNeruda`) are named custom fonts; their licensing, weights, and actual glyph design are unverified, and generic fallback stacks are used per instruction.
- The spacing and radius scales are conventional design-system defaults approximated against observed rem-based tokens (`--space-*`, `--radii-large`); exact pixel parity with the live site is not guaranteed.
- No interaction, animation, or mobile-specific layout was observed; all responsive guidance above is a proposed convention only.
- Component existence (nav-bar, hero, footer, product-card, etc.) is inferred from typical e-commerce/beverage-brand patterns and the presence of button/utility classes, not from confirmed DOM structure.
