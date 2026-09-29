---
version: alpha
name: "Packlane"
source_url: "https://www.packlane.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every primary CTA on packlane.com wears #2e469d — a deep navy-indigo with enough chromatic mass to anchor both a B2B order form and a consumer gift-box configurator. The brand lives at that intersection: authoritative enough for a print buyer ordering 500 custom mailers, approachable enough for a first-time shop owner placing their first tissue paper run. That dual register plays out in the palette. Ringing the core navy is a confetti of material-preview swatches — lemon #f9cf57, arctic mint #98ff98, electric teal #1bdfc7, safety orange #ffa300, and sky wash #b4eef9 — not placed decoratively but as live representations of what cardstock, kraft, and foil can become. The product is the swatch ring, and the interface surfaces that fact without overstatement.

  Libre Franklin carries the full typographic load: a humanist grotesque that renders crisply at both 12px caption labels and 40px display headlines without needing dramatic weight jumps. Packlane stays in the 400–600 weight range for most text, letting the navy-on-white contrast build hierarchy rather than typographic mass. Source Serif 4 surfaces at editorial moments — category intros, campaign landing sections — introducing a serif register that reads print-craft without abandoning the rectilinear grid. Body text rarely demands emphasis; the rendered box previews do the visual work.

  The surface architecture runs in stacked blue-washes: #f6f6f6, #f0f1f4, #e9f0fd, and #f2f8ff form a cool-tinted gradient that keeps the material swatches and 3D box renders luminous against a retreating background. Cards sit on #ffffff with a #d5d5d5 hairline and {rounded.sm} corners, giving the configurator a spreadsheet-precision feel. The interface softens only at step-progress bars and pricing chips — both rendered at {rounded.full} — marking milestones in a pill-shaped language that breaks the grid's rectilinearity just enough.

  The custom-box configurator is the product's central surface: a centered preview canvas with a gentle drop shadow, live-updating swatch selections, a quantity stepper, and a per-unit pricing chip that recalculates with each quantity tier change. State badges map directly to print production stages — proofing, printing, shipping — in success green (#03a74f on #c3e6d0), warning orange (#ffa300 on #fef5dd), and error red (#ce2d2d on #fce5ed). At {rounded.xs}-to-{rounded.sm} across controls and a tight 4px–16px spacing ramp, every pixel signals print precision.

colors:
  primary: "#2e469d"
  primary-active: "#1e3080"
  primary-disabled: "#586aad"
  primary-link: "#2f6cb0"
  primary-link-hover: "#126cb5"
  ink: "#373a3c"
  body: "#373a3c"
  muted: "#6e6d6d"
  hairline: "#d5d5d5"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-muted: "#f0f1f4"
  surface-wash: "#e9f0fd"
  surface-sky: "#f2f8ff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#03a74f"
  success-soft: "#c3e6d0"
  error: "#ce2d2d"
  error-soft: "#fce5ed"
  warning: "#ffa300"
  warning-soft: "#fef5dd"
  swatch-sky: "#b4eef9"
  swatch-mint: "#98ff98"
  swatch-teal: "#1bdfc7"
  swatch-teal-soft: "#d1f9f4"
  swatch-lemon: "#f9cf57"
  swatch-gold: "#f2c94c"
  swatch-orange: "#ffa300"

typography:
  display-xl:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-editorial:
    fontFamily: "'Source Serif 4', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  title-lg:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.15px
  price-display:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  step-label:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 20px
  xl: 32px
  full: 9999px

spacing:
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
    padding: 12px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-wash}"
    textColor: "{colors.primary-active}"
    border: "1.5px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary-link}"
    typography: "{typography.body-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
    textColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    hoverShadow: "0 4px 16px rgba(46,70,157,0.10)"
  hero-section:
    backgroundColor: "{colors.surface-wash}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted}"
    padding: "{spacing.section} 0"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-editorial}"
    headlineColor: "{colors.ink}"
    padding: "{spacing.xxl} 0"
  preview-canvas:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    boxShadow: "0 6px 28px rgba(46,70,157,0.09)"
    border: "1px solid {colors.hairline}"
  color-swatch:
    size: 32px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.primary}"
    borderInactive: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
  color-swatch-sky:
    backgroundColor: "{colors.swatch-sky}"
    rounded: "{rounded.full}"
  color-swatch-mint:
    backgroundColor: "{colors.swatch-mint}"
    rounded: "{rounded.full}"
  color-swatch-teal:
    backgroundColor: "{colors.swatch-teal}"
    rounded: "{rounded.full}"
  color-swatch-lemon:
    backgroundColor: "{colors.swatch-lemon}"
    rounded: "{rounded.full}"
  color-swatch-orange:
    backgroundColor: "{colors.swatch-orange}"
    rounded: "{rounded.full}"
  step-progress-bar:
    activeColor: "{colors.primary}"
    completedColor: "{colors.success}"
    inactiveColor: "{colors.hairline}"
    labelTypography: "{typography.step-label}"
    labelColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 4px
  pricing-chip:
    backgroundColor: "{colors.surface-wash}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.title-sm}"
    height: 44px
    buttonColor: "{colors.muted}"
    buttonHoverColor: "{colors.primary}"
  badge-success:
    backgroundColor: "{colors.success-soft}"
    textColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  badge-warning:
    backgroundColor: "{colors.warning-soft}"
    textColor: "{colors.warning}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  badge-error:
    backgroundColor: "{colors.error-soft}"
    textColor: "{colors.error}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  category-tab:
    activeTextColor: "{colors.primary}"
    inactiveTextColor: "{colors.muted}"
    activeIndicator: "2px solid {colors.primary}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
    backgroundColor: transparent
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    iconColor: "{colors.muted}"
    height: 44px
  material-selector:
    backgroundColor: "{colors.canvas}"
    selectedBackground: "{colors.surface-wash}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.primary}"
    titleTypography: "{typography.label}"
    captionTypography: "{typography.caption}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.swatch-sky}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.label}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
    borderTop: "none"

## Components

### Buttons

**`button-primary`** — The navy #2e469d fill button with white text is the single dominant CTA across all pages: "Get Started," "Add to Cart," "Continue." At 48px tall with {rounded.sm} corners and Libre Franklin 600 at 16px, it reads firmly without aggression. On hover the fill darkens to #1e3080 (`button-primary-active`); the disabled state steps back to #586aad with reduced opacity rather than draining to gray, preserving the brand hue.

**`button-secondary`** — A hollow outline button with a 1.5px primary-colored border and primary-colored text. Used for secondary actions like "Preview Design" or "Save for Later." On hover, the background fills with {colors.surface-wash}, a very light blue tint that signals the same brand family without competing with the primary fill button.

**`button-text`** — Inline link-button in {colors.primary-link} (#2f6cb0) with underline, used for low-priority actions like "Learn More" or "Change Material." No border, no background.

### Inputs

**`text-input`** — A 44px tall, 1px {colors.hairline}-bordered field with {rounded.xs} corners and a crisp 2px primary-blue focus ring. Placeholder text runs in {colors.muted}. No fill color change on focus — the border treatment alone signals active state. Used for all form fields: email, company name, address.

**`search-input`** — Structurally identical to `text-input` with a leading search icon in {colors.muted}. On desktop, lives in the top nav bar or as a full-width bar at the top of category pages.

**`quantity-stepper`** — A 44px tall inline stepper with minus/plus icon buttons flanking a centered number. Border is {colors.hairline} at {rounded.xs}; the operator icons are {colors.muted} until hover, when they step up to {colors.primary}. Paired visually with the `pricing-chip` to its right.

### Navigation

**`nav-bar`** — 64px tall, white canvas background, {colors.hairline} bottom border. The Packlane wordmark sits in primary navy on the left. Nav links run in Libre Franklin 500 at 15px. A "Start Designing" primary button anchors the right edge.

**`category-tab`** — Horizontal tab row below the nav on category pages. Active tab shows a 2px bottom indicator in {colors.primary} and primary-colored text; inactive tabs render in {colors.muted}. No background fill change — indicator-only active state.

### Product & Configurator

**`product-card`** — White surface with a 1px {colors.hairline} border at {rounded.sm}, padding {spacing.lg}. Top half: the product preview image or 3D box render. Bottom half: product name in `title-sm`, material/size caption in `caption`, and price in `price-display`. On hover the card gains a soft navy-tinted box shadow.

**`preview-canvas`** — The central configurator viewport: a {rounded.md} panel on {colors.surface-soft} with a soft 6px/28px shadow. The rendered box occupies the center; live swatch selection updates the box color in this panel. Padding is {spacing.xl} on all sides.

**`color-swatch`** — 32px pill circle at {rounded.full}. The active swatch carries a 2px navy border ring; inactive swatches show a 1px {colors.hairline} ring. Swatches are laid out in a horizontal wrap row with {spacing.xs} gaps. Named swatch tokens (`color-swatch-sky`, `color-swatch-mint`, etc.) map directly to the packaging material palette.

**`material-selector`** — Card-style selector for choosing box material (kraft, matte, glossy, etc.). Inactive state: 1px {colors.hairline} border. Selected state: 2px {colors.primary} border with {colors.surface-wash} background fill. Title in `label`, description in `caption`.

### Progress & Status

**`step-progress-bar`** — A 4px full-width track at {rounded.full}. Completed segments fill with {colors.success}; the active segment fills with {colors.primary}; future segments stay {colors.hairline}. Step labels sit below in `step-label` (11px, uppercase, 0.6px tracking) in {colors.muted}.

**`pricing-chip`** — A {rounded.full} pill in {colors.surface-wash} with `label` typography. Displays "as low as $X.XX each" copy that updates live as quantity changes. Positioned inline with the quantity stepper.

**`badge-success` / `badge-warning` / `badge-error`** — Status pill badges for order tracking. Each is a {rounded.full} chip with a tinted background and matching text color: green for "In Production," orange for "Awaiting Proof Approval," red for "Action Required." All use `caption` typography.

### Footer

**`footer`** — Dark ink (#373a3c) background with off-white text. Column headings in `label` 600, body links in `body-sm`. Link color is {colors.swatch-sky} (#b4eef9), which lifts legibly from the dark ground. No top border — the transition from page canvas to footer is marked purely by the background color shift.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; `preview-canvas` is full-width; `color-swatch` row scrolls horizontally; `step-progress-bar` labels hidden, dots only |
| Tablet | 744–1128px | Two-column product grid; configurator splits 50/50 between swatch panel and preview canvas; nav shows top-level links, hides secondary dropdowns |
| Desktop | 1128–1440px | Three-column product grid; configurator shows full sidebar with material selector, swatch ring, quantity stepper, and pricing chip in one persistent panel |
| Wide | > 1440px | Max-width container at 1280px centered; hero section gains horizontal padding to prevent text from stretching; product grid caps at four columns |

### Touch Targets

- All buttons and `color-swatch` circles meet a minimum 44px tap target on mobile, with swatches bumping to 40px diameter on touch breakpoints
- `quantity-stepper` minus/plus tap zones expand to 44×44px on mobile regardless of visible icon size
- `material-selector` cards use full-row tap targets on mobile, not just the text region
- `nav-bar` links expand to 48px tap height on tablet/mobile

### Collapsing Strategy

- The top nav on mobile collapses to: wordmark left, hamburger icon right; drawer opens from the right with full link list and "Start Designing" CTA
- The configurator sidebar stacks below the `preview-canvas` on mobile rather than running alongside it
- `category-tab` rows become a horizontally scrollable strip with no overflow truncation
- Footer columns collapse from four columns to two on tablet, single column on mobile with accordions for each section

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `primary-active` (#1e3080) is derived by darkening the extracted primary; no explicit hover-state color was captured from the live site
- Font weights for specific heading levels were not extractable from CSS — weight values (600 for titles, 700 for display) are inferred from the Libre Franklin weight axis and common Shopify theme patterns
- No explicit border-radius values were extracted; {rounded.xs}–{rounded.sm} values are inferred from the brand's precision-tooling aesthetic and screenshot comparison
- Custom icon set (packaging product icons, step-wizard icons) was not captured; icon style appears to be outlined with 1.5px strokes
- Animation/transition durations for the live box preview update and swatch selection were not extractable
- Mobile nav drawer background color and drawer animation direction not confirmed from extraction
- Exact button height and padding values may differ slightly from the live Shopify theme implementation
- Source Serif 4 usage scope (which specific pages or sections use it vs. Libre Franklin) was not fully determinable from extraction hints alone
