---
version: alpha
name: "Agendio"
source_url: "https://agendio.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Agendio opens with a row of chooseable cover colors — teal (#92d9e1), sage (#cadcb0), lavender (#e4c0e9), coral (#ff5f57) — and the premise that configuring a planner should feel like browsing a stationery boutique rather than completing a checkout form. The active CTA color is a warm amber (#ffc20c), crisp against a gray-toned structural shell built from two layered steel grays (#b3bcc0, #a4afb4) and a stack of near-white surfaces (#f7f7f7, #fafafa, #fcfcfc). That layered neutrality ensures the cover swatches carry visual interest rather than the interface chrome — each planner cover acts as its own product photograph. The deep forest green (#088043) operates as a secondary brand accent and success-state color, never competing with the amber primary because they occupy different semantic roles: amber means act, green means confirmed. An electric magenta (#e605ff) sits in the extraction as a catalog cover option, suggesting the range runs from minimal to vivid without apologizing for either end.

  Typography layers three distinct voices: Isidora anchors display headlines with geometric warmth appropriate to a boutique product that also ships in bulk; Montserrat handles navigation labels, UI copy, and body paragraphs with clean geometric efficiency; Rufina introduces a serif register in editorial pull-quotes and section intros, referencing letterpress craft that the customer base appreciates. Chivo Mono appears on order numbers and date strings, adding a precision note inside an otherwise warm system. Corner radii sit consistently in the {rounded.sm}–{rounded.md} range throughout — the same soft-rectangle language applies to product cards, format-selector chips, and text inputs; no element goes full-pill except isolated promotional badges, and nothing collapses to a hard corner. The customizer flow — date range, format, cover color, quantity — is Agendio's primary product surface, and the palette, spacing, and step-indicator components are calibrated to make that flow feel unhurried and boutique-grade rather than transactional.

colors:
  primary: "#ffc20c"
  primary-active: "#e6a800"
  primary-disabled: "#fff0a0"
  on-primary: "#1a1a1a"
  green: "#088043"
  green-light: "#98cdaa"
  green-pale: "#cadcb0"
  teal: "#92d9e1"
  lavender: "#e4c0e9"
  coral: "#ff5f57"
  electric: "#e605ff"
  amber-soft: "#ffca5d"
  amber-warm: "#ffbe2f"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#b3bcc0"
  muted-soft: "#a4afb4"
  hairline: "#dde1e3"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#fafafa"
  surface-muted: "#f5f5f5"
  scrim: "#000000"
  error: "#dc2626"
  error-dark: "#991b1b"
  error-light: "#fef2f2"
  error-border: "#fca5a5"
  success: "#088043"
  success-light: "#f0fdf4"
  success-mid: "#dcfce7"

typography:
  display-xl:
    fontFamily: "'Isidora', 'Montserrat', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Isidora', 'Montserrat', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Isidora', 'Montserrat', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Isidora', 'Montserrat', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  editorial:
    fontFamily: "'Rufina', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.1px
  editorial-sm:
    fontFamily: "'Rufina', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  mono:
    fontFamily: "'Chivo Mono', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label-caps:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  chip:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
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
    padding: 13px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 27px
    height: 48px
    border: "1.5px solid {colors.hairline}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.green}"
    typography: "{typography.button-md}"
    border: none
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    focusBorder: "1.5px solid {colors.primary}"
    errorBorder: "1.5px solid {colors.error-border}"
    errorBackground: "{colors.error-light}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-sm}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    overflow: hidden
    coverAspectRatio: "3/4"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.body-sm}"
    gap: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    accentColor: "{colors.primary}"
    minHeight: 520px
    padding: "{spacing.xxl} {spacing.lg}"
  customizer-panel:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    headlineTypography: "{typography.display-md}"
    labelTypography: "{typography.label-caps}"
    stepActiveColor: "{colors.primary}"
    stepCompleteColor: "{colors.green}"
    stepDefaultColor: "{colors.muted-soft}"
  cover-swatch:
    size: 40px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.ink}"
    hoverBorder: "2px solid {colors.muted}"
    gap: "{spacing.sm}"
  format-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.chip}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    border: "1.5px solid {colors.hairline}"
    selectedBackgroundColor: "{colors.ink}"
    selectedTextColor: "{colors.canvas}"
    selectedBorder: "1.5px solid {colors.ink}"
  date-range-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.mono}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.hairline}"
    padding: 10px 14px
    focusBorder: "1.5px solid {colors.primary}"
    calendarHighlight: "{colors.primary}"
    calendarRangeBackground: "{colors.primary-disabled}"
  quantity-stepper:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    buttonSize: 36px
    border: "1px solid {colors.hairline}"
    activeButtonColor: "{colors.ink}"
    activeButtonTextColor: "{colors.canvas}"
  planner-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  success-badge:
    backgroundColor: "{colors.success-light}"
    textColor: "{colors.green}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
    border: "1px solid {colors.success-mid}"
  step-indicator:
    activeColor: "{colors.primary}"
    completeColor: "{colors.green}"
    defaultColor: "{colors.muted-soft}"
    connectorColor: "{colors.hairline}"
    labelTypography: "{typography.caption}"
    dotSize: 10px
  review-summary-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.label-caps}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-md}"
    totalTypography: "{typography.title-md}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    linkColor: "{colors.green}"
    typography: "{typography.body-sm}"
    navTypography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Amber (#ffc20c) fill with dark ink text in `{typography.button-md}` Montserrat bold, 48px tall at `{rounded.sm}` corners. The dark-on-amber treatment reads as warm and confident without visual aggression — it echoes a wax-seal stamp rather than a neon alert. Hover state darkens to `{colors.primary-active}` (#e6a800); disabled fades to `{colors.primary-disabled}` with muted gray text and no pointer events.

**`button-secondary`** — White canvas background, 1.5px `{colors.hairline}` border, `{colors.ink}` text, matching 48px height for optical alignment in side-by-side CTA pairs. Hover lifts the background to `{colors.surface-soft}` and darkens the border to `{colors.muted-soft}`.

**`button-ghost`** — Transparent background with `{colors.green}` text in `{typography.button-md}`, no border. Reserved for secondary in-flow actions inside the customizer panel — reset, skip, back — where amber would compete with the active step indicator.

### Text Input

**`text-input`** — White background, 44px height, `{rounded.sm}` corners, 1.5px `{colors.hairline}` border at rest. On focus the border transitions to `{colors.primary}` amber, connecting the active field to the CTA color family without using a colored fill. Error state replaces the border with `{colors.error-border}` and tints the background `{colors.error-light}`. Placeholder text in `{colors.muted}` steel-gray maintains legibility without competing with filled values.

### Navigation Bar

**`nav-bar`** — 64px white bar with a 1px `{colors.hairline}` bottom rule. The Agendio wordmark renders in `{typography.display-sm}` Isidora to reinforce brand identity in the persistent header. Navigation links use `{typography.nav-link}` Montserrat semibold at 14px. The mobile breakpoint collapses to hamburger + logo + cart icon; the drawer overlays content with a `{colors.scrim}` at 40% opacity.

### Product Card

**`product-card`** — `{rounded.md}` card on a `{colors.surface-card}` background with a 1px `{colors.hairline}` border. The cover image occupies a 3:4 aspect ratio (portrait planner proportion) and bleeds to the card edge above the padded metadata zone. Title in `{typography.title-sm}`, price in `{typography.body-sm}`, separated by `{spacing.sm}`. Hover lifts the card with a soft drop shadow without scale transforms.

### Hero

**`hero`** — `{colors.surface-soft}` background, minimum 520px height. Headline in `{typography.display-xl}` Isidora leads the left column; a `{typography.body-md}` subhead follows in Montserrat at normal weight. The right column holds an animated planner preview with a row of cover-swatch dots below it. The `button-primary` amber CTA sits left-aligned below the text block; a thin 3px amber `{colors.primary}` accent rule may appear along the left edge of the headline to mark the entry point.

### Customizer Panel

**`customizer-panel`** — The core product surface. White canvas, `{rounded.md}` corners, 1px `{colors.hairline}` border, `{spacing.xl}` internal padding. Section headlines in `{typography.display-md}` Isidora; field labels in `{typography.label-caps}` Montserrat uppercase at `{spacing.sm}` margin above each control. The `step-indicator` runs across the panel top: amber dots for the active step, green for completed, `{colors.muted-soft}` for upcoming.

### Cover Swatch

**`cover-swatch`** — 40px circles (`{rounded.full}`) presenting the cover color catalog: teal (#92d9e1), sage (#cadcb0), lavender (#e4c0e9), coral (#ff5f57), electric (#e605ff), amber (#ffc20c), green-light (#98cdaa), and additional options. Default state has a transparent border; selected shows a 2px `{colors.ink}` ring with 2px offset gap between dot and ring. Hover adds a 2px `{colors.muted}` ring. On mobile the row scrolls horizontally rather than wrapping.

### Format Chip

**`format-chip`** — Selectable chips for planner dimensions (A5, A4, Letter, Half-Letter, etc.). Default: `{colors.surface-soft}` fill, `{colors.ink}` text, 1.5px `{colors.hairline}` border, `{rounded.xs}` corners. Selected state inverts to a solid `{colors.ink}` background with `{colors.canvas}` text — a high-contrast toggle that communicates selection without color dependence. Only one chip may be selected at a time.

### Date Range Input

**`date-range-input`** — Start and end date fields rendered in `{typography.mono}` Chivo Mono, giving date strings typographic distinctness from surrounding body copy. Same `{rounded.sm}` corners and focus-border in `{colors.primary}` as the standard `text-input`. The inline calendar popover fills selected range cells with `{colors.primary-disabled}` amber-tint; start and end endpoint cells fill solid `{colors.primary}`.

### Quantity Stepper

**`quantity-stepper`** — A horizontal minus/value/plus unit in `{typography.title-sm}`, wrapped as a single `{rounded.sm}` control on a `{colors.surface-soft}` background with a 1px `{colors.hairline}` border. Decrement and increment buttons default to transparent fill; active state fills button with `{colors.ink}` and `{colors.canvas}` icon to confirm the tap.

### Planner Badge

**`planner-badge`** — Short `{colors.primary}` amber chip in `{typography.label-caps}` uppercase, marking "New," "Popular," or limited-run catalog entries. The `success-badge` variant switches to a `{colors.success-light}` fill with `{colors.green}` text and a `{colors.success-mid}` border — used for in-stock confirmation and post-order status labels.

### Step Indicator

**`step-indicator`** — Horizontal dot sequence connected by thin `{colors.hairline}` lines. Active dot in `{colors.primary}` amber; completed dots in `{colors.green}`; upcoming in `{colors.muted-soft}`. Step labels in `{typography.caption}` beneath each dot. On mobile the full dot row collapses to a compact "Step 2 of 5" text in `{typography.caption}` to preserve horizontal space.

### Review Summary Card

**`review-summary-card`** — A `{rounded.md}` `{colors.surface-card}` panel with a 1px `{colors.hairline}` border and `{spacing.lg}` padding, used at the final customizer step to display chosen options before checkout. Field labels in `{typography.label-caps}` `{colors.muted}`; values in `{typography.body-md}`; the total line in `{typography.title-md}` with stronger weight.

### Footer

**`footer`** — `{colors.surface-soft}` background with a 1px `{colors.hairline}` top rule. Three-to-four column link grid in `{typography.caption}` Montserrat 12px. Link hover uses `{colors.green}` for a secondary brand voice distinct from the amber primary. Legal and copyright text beneath the link columns in `{typography.body-sm}` at `{colors.muted}`. The Agendio wordmark repeats at reduced opacity as a footer signature.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single column throughout. Nav collapses to hamburger + logo + cart. Customizer steps go full-width with a bottom-fixed `button-primary` "Next Step" CTA. Cover swatch row scrolls horizontally. Format chips wrap to two rows. Hero headline drops to `display-md` (28px). Step indicator condenses to text. |
| Tablet | 744–1128px | Two-column customizer: option controls left, live planner preview right. Nav expands to show all top-level links inline. Product grid goes 2-up. Hero shows text + CTA left, preview right. |
| Desktop | 1128–1440px | Three-column product grid. Customizer panel max-width ~840px, centered. Full nav visible. Hero gains more vertical padding. Footer four-column. |
| Wide | > 1440px | All content constrained to ~1280px max-width, centered on `{colors.surface-soft}` side gutters. Display typography scales up 4–6px at hero level. Customizer panel stays fixed-width. |

### Touch Targets

- Cover swatches: 40px visual size with invisible padding to reach 44×44px minimum touch area
- Format chips: minimum 36px height on tablet+; expand to 44px on mobile
- Quantity stepper buttons: minimum 44px hit area on mobile regardless of visual size
- Nav links in mobile drawer: minimum 48px height per item
- Date inputs: minimum 44px height at all breakpoints

### Collapsing Strategy

- **Customizer steps** shift from a side-by-side two-column layout (tablet+) to full-screen sequential panels (mobile) with a bottom-fixed amber CTA advancing through each step
- **Product grid** collapses 3-up → 2-up → 1-up; card width grows proportionally at each step
- **Hero** collapses from two-column text+preview to stacked: preview above the fold, headline and CTA below
- **Footer** collapses from four-column link grid to a two-column accordion with each section togglable
- **Nav drawer** slides in from the right over a `{colors.scrim}` overlay at 40% opacity

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No explicit dark/ink color extracted from the site — `{colors.ink}` (#1a1a1a) is a conventional near-black default, not confirmed from extraction
- `{colors.primary-active}` (#e6a800) and `{colors.primary-disabled}` (#fff0a0) are derived tints of the extracted #ffc20c, not independently confirmed from computed styles
- `{colors.hairline}` (#dde1e3) is derived from the extracted steel grays; exact border token not directly captured
- Isidora, Rufina, and Montserrat role assignments (which is display vs. body vs. editorial) are inferred from font-stack order and brand context — not directly measured from live rendered layout
- "Overlays" font-family entry in the extraction is ambiguous — may be a display/texture font name, a CSS class name misread as a font, or a framework artifact; omitted from the typography system pending clarification
- Button corner radii (`{rounded.sm}`, 8px) are an inference from the overall visual register — exact values not captured from computed styles
- Mobile navigation pattern (hamburger drawer vs. bottom tab bar) not confirmed from extraction
- Electric magenta (#e605ff) presence in extraction is unconfirmed as a planner cover color vs. an errant UI element or browser extension artifact
- The full red ramp (#fef2f2 → #7f1d1d) closely matches the Tailwind CSS default red scale and may be framework defaults rather than deliberate brand choices; used only for error states with that caveat
- The green ramp (#f0fdf4 → #bbf7d0) similarly maps to Tailwind's default green scale; `{colors.green}` (#088043) is treated as the confirmed brand green, the ramp values as utility-only
