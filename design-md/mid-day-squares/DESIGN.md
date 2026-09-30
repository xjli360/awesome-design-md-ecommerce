---
version: alpha
name: "Mid-Day Squares"
source_url: "https://middaysquares.com"
captured_at: "2026-09-28T09:44:48.627211+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Mid-Day Squares' evidence set centers on a near-black ink (#101010) paired
  with white canvas and a saturated brand red (#eb1822, close cousin
  #ca172a/#c30505) used for cart indicators and hover states — this red is
  treated here as the primary accent. Secondary flavor-coded hues appear in
  the palette (#4e008e purple, #001cd4 blue, #48a23f green, #6fdde4 cyan,
  #fff200/#f7cd05 yellow, #ff8400 orange), which strongly suggests a
  per-flavor color-coding system across the "Customize Your Order" grid;
  this role is inferred, not confirmed by layout evidence. Typography leans
  on a custom ABCROM family (ABCROMExtended-Heavy-Trial, ABCROM-Book-Trial,
  ABCROM Condensed/Mono variants) alongside a parallel GT America trial
  stack and NaNHolo-Black, the latter driving an oversized product-name
  display (10.8em) with a colored text-stroke effect. Body copy typography
  was not directly observed in the supplied rules, so body sizes/families
  below are proposed using the same GT America / Helvetica Neue stack as a
  reasonable fallback. Buttons are pill-ish rounded-corner black blocks that
  invert to red or orange-red on hover, reused here as the primary CTA
  pattern. All hex values are drawn from the supplied palette only.

colors:
  primary: "#eb1822"
  ink: "#101010"
  canvas: "#ffffff"
  body: "#414141"
  muted: "#757575"
  hairline: "#dedede"
  surface-soft: "#f4f4f4"
  surface-card: "#f1f0ef"
  on-primary: "#ffffff"
  accent-hover: "#f72901"
  accent-deep: "#c30505"
  flavor-purple: "#4e008e"
  flavor-blue: "#001cd4"
  flavor-green: "#48a23f"
  flavor-cyan: "#6fdde4"
  flavor-yellow: "#f7cd05"
  flavor-orange: "#ff8400"
typography:
  display-xl: {fontFamily: "'NaNHolo-Black', sans-serif", fontSize: 168px, fontWeight: 900, lineHeight: 0.95, letterSpacing: -1px}
  display-md: {fontFamily: "'ABCROMExtended-Heavy-Trial', sans-serif", fontSize: 40px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.25px}
  title-md: {fontFamily: "'GT-AMERICA-CONDENSED-BOLD-TRIAL', sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'GT-America-Standard-Regular-Trial', 'Helvetica Neue', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'GT-America-Standard-Regular-Trial', 'Helvetica Neue', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'GT-AMERICA-STANDARD-MEDIUM-TRIAL', sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.6, letterSpacing: 0.5px}
  button-md: {fontFamily: "'ABCROMExtended-Heavy-Trial', sans-serif", fontSize: 16px, fontWeight: 800, lineHeight: 1.2, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.xl}"
    hover: "backgroundColor: {colors.accent-hover}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.ink}"
    padding: "{spacing.sm} {spacing.xl}"
    hover: "backgroundColor: {colors.accent-deep}; textColor: {colors.on-primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    height: "72px"
    hairline: "{colors.hairline}"
    cartBadge: "backgroundColor: {colors.primary}; textColor: {colors.on-primary}; rounded: {rounded.full}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    ctaVariant: "button-secondary"
  hero:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaVariant: "button-primary"
    overlayTextColor: "{colors.primary}"
    textStrokeAccent: "{colors.flavor-yellow}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    columnHeaderTypography: "{typography.title-md}"
    dividerColor: "{colors.hairline}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.xs}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
  flavor-selector:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    swatchColors: "[{colors.flavor-purple}, {colors.flavor-blue}, {colors.flavor-green}, {colors.flavor-cyan}, {colors.flavor-yellow}, {colors.flavor-orange}]"
    labelTypography: "{typography.caption}"
    selectedBorder: "2px solid {colors.primary}"

## Components
**button-primary** models the observed `.btn_collection` rule: a black
(`{colors.ink}`) block, uppercase heavy type, and a confirmed hover swap to
`#F72901`. Rounded corners and padding are drawn from the desktop variant
(8px radius, generous horizontal padding); the mobile 6px-radius variant is
treated as a responsive override rather than a separate component.

**button-secondary** is a proposed outline counterpart for lower-emphasis
actions (e.g. "Customize"), using the same ink border and an inferred
hover state pulling from the footer link hover color `#C30505`, which was
observed on a related `.btn_collection:hover` footer rule.

**text-input** and **search** are proposed patterns; no distinct input
styling was present in the supplied CSS beyond the newsletter button, so
border/radius/padding values are inferred defaults consistent with the
brand's crisp, low-radius button language.

**nav-bar** reflects the cart-count badge rule directly (`border-radius:
50%`, red background, white text) as the one concretely observed header
element; the surrounding bar height and layout are proposed.

**product-card** is a proposed container for the flavor grid ("PB&J Apple
Cinnamon," "Cookie Dough," etc.) implied by the page text's repeated
flavor/CTA pairs; no card CSS was directly supplied, so background,
radius, and spacing are inferred from the general surface/rounded scale.

**hero** captures the large flavor-name treatment seen in
`.product_closeup_top_text`: NaNHolo-Black type, red fill, and a yellow
text-stroke — a distinctive, directly observed effect reused here as the
hero's signature accent, scaled down for a typical hero rather than the
observed 10.8em close-up size.

**footer** uses the ink background and white text pattern implied by the
button-hover/footer-link rules (`.footer_column ul li a:hover
.btn_collection:hover`), with column headers proposed as condensed-bold
type matching `.footer-header-mobile`.

**badge** and **flavor-selector** are proposed, category-appropriate
components: badge reuses the cart-count red/full-radius pattern for
labels like "No GMO"/"No Soy"; flavor-selector is inferred from the
multi-hue palette (purple, blue, green, cyan, yellow, orange) as a
plausible per-SKU color-coding system for the customizable snack bundle,
though no selector markup or states were observed.

## Responsive Behavior
Recommended, not measured breakpoints:

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| mobile | <600px | Single-column hero/product grid; nav collapses to a hamburger; footer columns stack under `.footer-header-mobile`-style accordions (observed class name, behavior inferred). |
| tablet | 600–1024px | Two-column product grid; nav remains condensed. |
| desktop | >1024px | Multi-column product/flavor grid; full horizontal nav. |

Touch targets should be at least 44px; buttons should retain the ~8–12px
padding pattern seen in `.btn_collection`. Mobile font-size reductions
(e.g. the 0.7em `.btn_collection` variant) suggest the brand already
scales button type down at narrow widths — this proposal continues that
pattern for all button variants.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no live
rendering, computed layout, or interaction testing was performed. Body
copy typography, input styling, and most card/grid measurements were not
present in the supplied evidence and are marked proposed/inferred above.
The flavor-color-coding role for purple/blue/green/cyan/yellow/orange
hues is a plausible but unconfirmed semantic mapping. The `NaNHolo-Black`
and `ABCROM*`/`GT America` families are custom or trial webfonts whose
licensing and actual availability on the live site were not verified;
generic sans-serif fallbacks are assumed. Interaction states (focus,
disabled, error) and true mobile navigation behavior were not observed
and are proposed defaults only.
