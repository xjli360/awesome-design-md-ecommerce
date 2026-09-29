---
version: alpha
name: "Furnace Record Pressing"
source_url: "https://www.furnacemfg.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  An order portal for vinyl manufacturing rarely announces itself this directly — a near-black navigation at #1a1e21 carries the Furnace wordmark highlighted in amber (#f29b1f), the precise color of heated steel, and every primary call-to-action picks up that same amber, making the furnace metaphor literal and structural rather than decorative. Montserrat at heavy weights (700–800) handles all display and heading work, its geometric strokes echoing the mechanical tolerances of a pressing plant; at weight 400 it serves the dense spec tables and pricing breakdowns that define the B2B quoting experience. The canvas is a near-white (#f9fafb) for content areas, but sections that need gravity — hero banners, footers, announcement bars — drop to #1a1e21 or #141619, maintaining a factory-floor seriousness that softer palettes would undercut. Primary link-style actions and secondary structural chrome run deep navy (#003388); amber and navy trade roles by page section without competing. Rounded corners are minimal throughout — {rounded.xs} at 4px on inputs and buttons, {rounded.sm} at 6px on cards — constraints that read as manufacturing specification rather than stylistic preference. Cards use a 1px #e2e3e5 hairline border rather than box-shadows, keeping the interface flat and precise. Order-status badges repurpose Bootstrap's semantic layer — amber for in-progress, green-surface (#d1e7dd) for complete, near-white (#eeeeee) for pending — but the amber badge reads as brand identity before it reads as a state indicator, which is a quiet alignment between framework defaults and the brand name. The multi-step quote form (vinyl weight, quantity, jacket type, deadwax notes, timeline) is the primary conversion path and receives the most interface investment: file-upload zones with dashed borders, a spec-row layout for confirming selections, and an amber submit anchoring the bottom of every step.

colors:
  primary: "#003388"
  primary-active: "#0a58ca"
  primary-disabled: "#bacbe6"
  amber: "#f29b1f"
  amber-dark: "#664d03"
  ink: "#141619"
  body: "#41464b"
  muted: "#636464"
  hairline: "#e2e3e5"
  hairline-soft: "#cbccce"
  canvas: "#f9fafb"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  surface-dark: "#1a1e21"
  surface-separator: "#565e64"
  on-primary: "#ffffff"
  primary-tint: "#cfe2ff"
  success: "#198754"
  success-dark: "#0f5132"
  success-surface: "#d1e7dd"
  success-surface-soft: "#bcd0c7"
  danger: "#842029"
  danger-mid: "#b02a37"
  danger-surface: "#f8d7da"
  info-dark: "#055160"
  info-surface: "#cff4fc"
  neutral-dark: "#084298"

typography:
  display-xl:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 44px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.6px
  display-md:
    fontFamily: "'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', system-ui, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', system-ui, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge-label:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  eyebrow:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.4px
    textTransform: uppercase
  price-display:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.5px

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 20px
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
    backgroundColor: "{colors.amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "12px 28px"
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.amber-dark}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 2px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "10px 26px"
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.primary-tint}"
    textColor: "{colors.primary}"
    rounded: "{rounded.xs}"
  button-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "12px 28px"
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    padding: "10px 14px"
    height: 44px
    focusBorderColor: "{colors.primary}"
    focusOutlineColor: "{colors.primary-tint}"
    placeholderColor: "{colors.muted}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    padding: "10px 14px"
    height: 44px
    focusBorderColor: "{colors.primary}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    padding: "10px 14px"
    minHeight: 120px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
  nav-bar-logo:
    textColor: "{colors.amber}"
    typography: "{typography.display-sm}"
  nav-link-active:
    textColor: "{colors.amber}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.amber}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    subheadingTypography: "{typography.body-md}"
    accentColor: "{colors.amber}"
    minHeight: 460px
    padding: "{spacing.section} {spacing.xl}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.amber}"
  pricing-tier:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    padding: "{spacing.xl}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    featureTypography: "{typography.body-sm}"
  pricing-tier-featured:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.amber}"
    borderWidth: 2px
    padding: "{spacing.xl}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    badgeBackgroundColor: "{colors.amber}"
    badgeTextColor: "{colors.ink}"
    badgeTypography: "{typography.badge-label}"
  badge-pending:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  badge-in-progress:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  badge-complete:
    backgroundColor: "{colors.success-surface}"
    textColor: "{colors.success-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  badge-attention:
    backgroundColor: "{colors.danger-surface}"
    textColor: "{colors.danger}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  badge-info:
    backgroundColor: "{colors.info-surface}"
    textColor: "{colors.info-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  process-step:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    stepNumberColor: "{colors.amber}"
    stepNumberTypography: "{typography.display-md}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    connectorColor: "{colors.hairline}"
    iconBackgroundColor: "{colors.surface-soft}"
  spec-row:
    backgroundColor: "{colors.canvas}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-md}"
    borderBottomColor: "{colors.hairline}"
    padding: "{spacing.md} 0"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    headerBackgroundColor: "{colors.surface-dark}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"
  quote-form:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    padding: "{spacing.xl}"
    headingTypography: "{typography.title-md}"
    stepIndicatorActiveColor: "{colors.amber}"
    stepIndicatorInactiveColor: "{colors.hairline}"
  file-upload:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    borderStyle: dashed
    borderWidth: 2px
    rounded: "{rounded.sm}"
    textColor: "{colors.muted}"
    iconColor: "{colors.muted}"
    activeBackgroundColor: "{colors.primary-tint}"
    activeBorderColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  section-eyebrow:
    textColor: "{colors.amber}"
    typography: "{typography.eyebrow}"
    marginBottom: "{spacing.sm}"
  alert-info:
    backgroundColor: "{colors.info-surface}"
    textColor: "{colors.info-dark}"
    borderColor: "{colors.info-dark}"
    borderLeftWidth: 4px
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
  alert-success:
    backgroundColor: "{colors.success-surface}"
    textColor: "{colors.success-dark}"
    borderColor: "{colors.success}"
    borderLeftWidth: 4px
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.amber}"
    linkHoverColor: "{colors.on-primary}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-primary}"
    borderTopColor: "{colors.surface-separator}"
    borderTopWidth: 1px
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Amber (#f29b1f) fill with ink-black text, Montserrat 700 uppercase at 15px, 4px radius. The choice of amber over navy for primary actions makes every CTA read as "furnace-lit" — hover deepens to amber-dark (#664d03) with white text for contrast. Disabled state falls to a muted blue-tint (#bacbe6) matching the Bootstrap disabled token.

**`button-secondary`** — White fill with a 2px navy (#003388) border and navy text, pairing against the amber primary to create a clear action hierarchy. Hover floods the fill with primary-tint (#cfe2ff) at low opacity. Use for cancel, back, and secondary form actions throughout the quoting flow.

**`button-dark`** — Full navy (#003388) fill with white text. Appears on light-canvas sections where amber would lose contrast against surrounding warm tones, such as the mid-page service overview rows and pricing CTA rows outside the featured tier.

**`button-ghost`** — Transparent with navy text, no border. Reserved for tertiary in-flow links like "learn more," download spec PDFs, or FAQ toggles within accordion components.

### Text Inputs & Forms

**`text-input`** / **`select-input`** — 44px height, 1px hairline border (#e2e3e5), xs-radius, with a primary-blue (#003388) focus border and primary-tint (#cfe2ff) focus outline ring. Placeholders in muted (#636464). Both fields share identical sizing to allow mixed rows in the multi-column quote form without visual inconsistency.

**`file-upload`** — Dashed 2px hairline border, surface-soft (#eeeeee) background, sm-radius. On drag-over, the background transitions to primary-tint (#cfe2ff) and the border sharpens to solid navy (#003388), signaling acceptance. Used for audio files (lacquer reference), artwork, and label copy uploads during order intake.

**`quote-form`** — A contained card (surface-card, 1px hairline, md-radius, xl padding) that wraps the multi-step intake. A horizontal step-indicator runs amber dots for completed steps and hairline circles for upcoming ones. Heading uses title-md; helper text body-sm in muted.

### Navigation

**`nav-bar`** — 64px dark surface (#1a1e21), full width, no border. The Furnace logotype in amber anchors the left; primary links (Services, Pricing, Turntimes, Contact) in nav-link weight 600 at 14px run right of center. A "Get a Quote" amber button-primary sits at the far right as a persistent CTA. On scroll, the bar gains no elevation change — it remains flat against the page, consistent with the no-shadow design language.

### Product / Service Cards

**`product-card`** — White fill, 1px hairline border, sm-radius, lg padding. Title in title-md Montserrat 700 over body-sm for description text. Used for service tiers (Standard, Rush, Lacquer-Cut) and add-on modules (color vinyl, picture disc, tip-on jacket). No hover elevation — a thin amber left-border accent (4px) highlights the selected or hovered card instead.

**`pricing-tier`** / **`pricing-tier-featured`** — Base tier uses hairline border. Featured tier swaps to a 2px amber border with an amber badge-label chip ("POPULAR" or "BEST VALUE") pinned to the top-right corner. Price uses the price-display token at 36px/800 in ink-black; per-unit pricing in caption below. Feature list uses body-sm with success-colored checkmarks.

### Status Badges

**`badge-pending`** / **`badge-in-progress`** / **`badge-complete`** / **`badge-attention`** — All share badge-label typography (11px/700/uppercase/+0.6px tracking) and xs-radius pill shape. In-progress is amber-fill/ink-text, echoing the brand primary; complete is success-surface/success-dark-text; attention is danger-surface/danger-text; pending is surface-soft/body-text. These appear in the order-tracking dashboard and production timeline tables.

### Process Steps

**`process-step`** — Step number rendered in display-md Montserrat 800 in amber, title in title-md, body copy in body-sm muted. A horizontal hairline connector links steps on desktop; on mobile the connector collapses to a vertical line left of the number column. Background is canvas white; the active step receives an amber left-border accent.

### Spec Table

**`spec-table`** — Dark-surface (#1a1e21) header row with on-primary text in spec-label weight 600. Alternating rows use canvas and surface-soft (#eeeeee) for legibility across wide spec grids (format, RPM, weight, quantity, jacket type, color). Thin hairline-soft borders between all cells; xs-radius on the outer container.

### Alerts

**`alert-info`** / **`alert-success`** — Inline alert bars with a 4px left-border accent (info-dark for info, success for success), matching background tint, xs-radius, and body-sm copy. Used for order confirmations, estimated ship dates, and spec-change notices. Bootstrap semantic structure retained but styled to the site's flat, border-heavy vocabulary.

### Footer

**`footer`** — Full-width dark surface (#1a1e21), 1px separator line at top in surface-separator (#565e64), section padding top and bottom. Column headings in title-sm Montserrat 600 in on-primary; links in body-sm amber (#f29b1f) that turn full white on hover. Social icons and legal copy sit in a sub-footer row at caption size.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger nav (dark drawer from left, amber close icon), single-column quote form, stacked process steps with vertical connector, pricing tiers scroll horizontally in a snap-scroll carousel, spec tables collapse to label/value stacked rows |
| Tablet | 744–1128px | 2-column pricing grid, side-by-side process steps (2-up), quote form fields reflow to 2-column where semantically grouped (e.g., quantity + format), nav retains full link row at reduced 13px |
| Desktop | 1128–1440px | 3-column pricing grid, 4-step process row with horizontal connectors, quote form splits 60/40 (form left, live spec summary right), full nav-bar with persistent CTA button |
| Wide | > 1440px | Container max-width ~1320px centered with auto side margins, hero padding extends but text block stays constrained to ~720px for line-length legibility |

### Touch Targets

- All buttons minimum 48px height (matches Bootstrap's btn sizing)
- Nav links padded to 44px touch height on mobile even at 13px text size
- File-upload drop zone minimum 120px height on mobile; tap opens OS file picker
- Badge chips minimum 32px touch height in order dashboard rows
- Step-indicator dots minimum 24×24px hit area with 8px outer padding

### Collapsing Strategy

- Quote form fields collapse to full-width stacked below 744px; label above input (not inline)
- Spec tables switch to a card-per-row accordion below 744px — each row expands to show all specs for that SKU
- Process step grid (4-up desktop) collapses to 2-up at tablet and 1-up vertical at mobile
- Pricing tier carousel on mobile uses scroll-snap with a visible partial bleed on the right to signal scrollability
- Footer 4-column grid collapses to 2-col at tablet, full-stack at mobile with section dividers between each column

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex palette is dominated by Bootstrap 5 utility colors; it is difficult to definitively separate brand-owned tokens (amber #f29b1f, navy #003388) from coincidental Bootstrap variables without auditing CSS custom properties directly
- `surface-card: "#ffffff"` is inferred — pure white did not appear in the top hex extraction
- `danger-surface: "#f8d7da"` is Bootstrap's standard alert-danger background and almost certainly present but did not rank in the top extracted colors
- Custom illustration or icon assets (record grooves, pressing-machine diagrams) were not captured; their specific stroke and fill colors may introduce additional palette tokens
- Whether `#003388` vs `#003399` is the canonical brand navy could not be determined from extraction alone — both appear and differ by one step; #003388 was chosen as primary
- Actual hero photography color grading (if any tinted overlays are used) is unknown
- No custom font license or variable-font axes information was extractable for Montserrat; weight range and axis behavior assumed from standard Google Fonts distribution
- Order-dashboard table typography at very small sizes (10–11px caption rows) may use a different weight than extracted; density of tabular data suggests possible monospace or condensed column variant not captured
