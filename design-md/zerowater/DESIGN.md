---
version: alpha
name: "ZeroWater"
source_url: "https://www.zerowater.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Five-stage filtration brands typically lean clinical white or safety-lab blue; ZeroWater builds its entire hero experience on #000e2e, a near-black midnight navy so dense it absorbs ambient UI noise and makes the electric mint (#6bffc6) CTAs read as a purification signal rather than a routine prompt. That voltage contrast — deep navy against glowing mint — carries the brand's core claim: water measured to zero total dissolved solids, not approximated. The TDS (Total Dissolved Solids) meter is ZeroWater's signature artifact, and the type stack is built around its readout: Manrope handles interface labels, product titles, and navigation in clean geometric strokes at weights 400–700, while a monospace family — Consolas, Menlo, Monaco — renders the three-digit dissolved-solids reading at hero scale, making '000' feel like a precision instrument rather than a headline. IBMPlexSerif enters for editorial moments: 'Why Zero?' explainer flows, filtration science callouts, and certification copy, lending the brand a credentialed voice without full clinical sterility. Secondary interactive states draw from two accent blues (#2968fe, #2563eb) and an electric purple (#5a31f4), but mint and navy carry every primary communication channel. A four-step success-green family (#22c55e → #4ade80 → #86efac → #dcfce7) maps to certification confirmation states — graduated, not binary — implying a multi-step verification UX rather than a single badge moment. Corner radii sit in the moderate range: {rounded.xs} on inputs and filter badges, {rounded.md} on product cards, {rounded.sm} on CTAs — no pill shapes, because the brand's differentiator is measured precision rather than approachability. Vertical section spacing is generous ({spacing.section} = 64px), keeping the dark canvas from closing in while giving the mint CTAs negative space to command attention. The system reads as a lab instrument meets consumer confidence — dark enough to signal seriousness, bright enough to remain purchasable.

colors:
  primary: "#6bffc6"
  primary-active: "#4ae8b0"
  primary-disabled: "#a8fde0"
  brand-navy: "#000e2e"
  accent-blue: "#2968fe"
  accent-blue-alt: "#2563eb"
  accent-purple: "#5a31f4"
  ink: "#111827"
  ink-on-dark: "#f3f4f6"
  body: "#374151"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-dark: "#1f2937"
  canvas: "#fafaf9"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#000e2e"
  success: "#22c55e"
  success-mid: "#4ade80"
  success-light: "#dcfce7"
  error-light: "#fee2e2"

typography:
  display-xl:
    fontFamily: "'IBMPlexSerif', Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'IBMPlexSerif', Georgia, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  tds-display:
    fontFamily: "Consolas, Menlo, Monaco, 'Courier New', ui-monospace, monospace"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -2px
  title-lg:
    fontFamily: "'Manrope', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Manrope', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Manrope', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Manrope', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Manrope', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Manrope', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Manrope', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  label-mono:
    fontFamily: "Consolas, Menlo, Monaco, 'Courier New', ui-monospace, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "'Manrope', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 15px
    fontWeight: 600
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-ghost-dark:
    backgroundColor: transparent
    textColor: "{colors.ink-on-dark}"
    border: "1px solid rgba(255,255,255,0.25)"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.ink-on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: none
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-lg}"
    hoverShadow: "0 4px 24px rgba(0,14,46,0.10)"
  hero-dark:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.ink-on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
  tds-meter-display:
    backgroundColor: "{colors.brand-navy}"
    valueColor: "{colors.primary}"
    labelColor: "{colors.muted-soft}"
    valueTypography: "{typography.tds-display}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg} {spacing.xl}"
    border: "1px solid {colors.hairline-dark}"
  filter-stage-badge:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  certification-stamp:
    backgroundColor: "{colors.success-light}"
    textColor: "{colors.success}"
    iconColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  info-badge:
    backgroundColor: "{colors.accent-blue}"
    textColor: "#ffffff"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  comparison-table:
    headerBackgroundColor: "{colors.brand-navy}"
    headerTextColor: "{colors.ink-on-dark}"
    rowBackgroundColor: "{colors.canvas}"
    altRowBackgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    highlightColumnBorder: "{colors.primary}"
    headerTypography: "{typography.title-md}"
    cellTypography: "{typography.body-sm}"
  filter-stage-tracker:
    trackColor: "{colors.hairline}"
    activeNodeColor: "{colors.primary}"
    completedNodeColor: "{colors.success}"
    inactiveNodeColor: "{colors.hairline}"
    labelTypography: "{typography.label-mono}"
    nodeSize: 32px
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

### Buttons

**`button-primary`** — Electric mint fill (#6bffc6) with deep navy text ({colors.on-primary}) holds WCAG-passing contrast on both light and dark surfaces. Manrope Bold 15px at 0.3px letter-spacing reads as direct and purposeful; the 48px height and 28px horizontal padding give the tap target authority without over-sizing. `button-primary-active` darkens the mint to #4ae8b0 on press; `button-primary-disabled` fades to the washed mint ({colors.primary-disabled}) while preserving the navy label.

**`button-secondary`** — Transparent fill with a 2px mint border and mint label; the outlined counterpart for light-canvas product pages where a full mint fill would compete with photography. Matches primary in height and Manrope Bold 15px typography.

**`button-ghost-dark`** — Transparent background, 25%-opacity white border, and {colors.ink-on-dark} label; reserved exclusively for secondary CTAs inside `hero-dark` and navy promotional sections. Prevents stacking two opaque accent colors on the dark surface.

### Navigation

**`nav-bar`** — Full-width at 72px on {colors.brand-navy}, no bottom border required since the navy creates natural separation. Logo anchored left; links in {typography.nav-link} (Manrope SemiBold 15px) at {colors.ink-on-dark}; right slot holds a mint `button-primary` CTA. A `promo-banner` strip typically rides above the bar for active promotions, producing the navy-on-mint inversion at the top of every page that anchors brand recognition at first glance. Collapses to hamburger at mobile breakpoints.

### Product Card

**`product-card`** — White card ({colors.surface-card}) with {rounded.md} corners and a 1px {colors.hairline} border at rest. Hover surfaces a diffused navy shadow (rgba(0,14,46,0.10)) that lifts the card without a harsh outline change. Product name in {typography.title-md} (Manrope SemiBold), price in {typography.title-lg} (Manrope Bold 24px). `filter-stage-badge` chips cluster at the lower-left to communicate filtration tier and pitcher/dispenser compatibility at a glance, reducing pre-purchase friction.

### TDS Meter Display

**`tds-meter-display`** — The brand's signature UI panel: a dark navy slab ({colors.brand-navy}) with a {colors.hairline-dark} border, displaying a three-digit TDS reading in the monospace stack at 72px in electric mint. A "TDS" or "mg/L" unit label in {typography.caption} at {colors.muted-soft} sits directly below the digits. This component anchors hero sections, product comparison modules, and "Verify Your Water" onboarding flows, translating the filtration claim from marketing copy into a visible, instrument-style readout that the brand's physical TDS meter makes literal.

### Hero Dark

**`hero-dark`** — Full-width section on {colors.brand-navy} with {spacing.section} top and bottom padding. Headline in {typography.display-xl} (IBMPlexSerif Bold 56px) at {colors.ink-on-dark}; supporting paragraph in {typography.body-md} Manrope at slightly dimmed near-white. A `button-primary` anchors the primary CTA, with an optional `button-ghost-dark` beside it for a secondary path (e.g. "See How It Works"). The `tds-meter-display` occupies a right-column or centered sub-panel beneath the headline, grounding the hero claim in a measurable form.

### Certification & Trust

**`certification-stamp`** — Pill badge ({rounded.full}) on {colors.success-light} with {colors.success} text and a checkmark icon. Applied inline with product headlines on PDPs and in strips adjacent to the nav for NSF/ANSI certification marks and "Certified 0 TDS" labels. Signals verifiable third-party validation rather than brand self-assertion.

**`filter-stage-badge`** — Dark navy chip ({colors.brand-navy}) with a 1px mint border and mint {typography.caption} label, indicating filtration tier ("5-Stage", "Elite"). Placed at the lower edge of product cards and beside spec-list line items. The navy-background treatment reads as an inset from the surrounding white card surface, making the badge feel part of the product hardware rather than a marketing overlay.

**`info-badge`** — Filled {colors.accent-blue} chip for category metadata: "New", "Best Value", "Limited Edition". Sits above product titles on cards. {typography.caption} in white, {rounded.xs}.

### Comparison Table

**`comparison-table`** — ZeroWater's primary competitive tool. Navy header row with column names in {typography.title-md} at {colors.ink-on-dark}; alternating {colors.canvas} and {colors.surface-soft} data rows for scan-ability; the ZeroWater column is highlighted with a {colors.primary} left-border treatment that makes the brand's column visually dominant. Check marks use {colors.success}; cross/fail marks use {colors.error-light}. Cell content in {typography.body-sm}.

### Filter Stage Tracker

**`filter-stage-tracker`** — Five-step horizontal progress indicator for educational and product-detail content. Inactive nodes are {colors.hairline} circles; the active node is {colors.primary} (mint); completed nodes fill to {colors.success} (green). Step labels in {typography.label-mono} (Consolas), which reinforces the instrument-panel framing and makes "Stage 3 / 5" read like a calibrated readout rather than a content outline. Node diameter is 32px.

### Promo Banner

**`promo-banner`** — Slim full-width announcement strip on {colors.primary} (mint) with {colors.on-primary} (navy) text in {typography.button-sm}. Sits above the nav-bar. The inverted color swap — navy text on mint background above, mint button on navy nav below — makes the site-topper feel native to the brand system rather than appended.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger + logo; hero-dark stacks TDS meter below headline text; product grid is 1-up; comparison-table horizontally scrolls with sticky first column; filter-stage-tracker converts to vertical labeled list |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows primary links only, abbreviated; hero-dark 50/50 split between text and TDS panel; comparison-table shows up to 3 columns |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links and CTA button; hero-dark runs at full typographic scale; comparison-table fully visible |
| Wide | > 1440px | Content max-width ~1280px centered; hero-dark adds horizontal padding; product grid max 4-up |

### Touch Targets

- All buttons minimum 48px height × 44px width
- Nav hamburger and close icons: 44×44px tap area
- `filter-stage-badge` and `certification-stamp` padded to minimum 36px height on mobile
- Product card tap area spans full card surface with no interior interactive zone overlap
- `filter-stage-tracker` nodes expand to 40px tap area on touch devices

### Collapsing Strategy

- `nav-bar`: full links → abbreviated links → hamburger across three breakpoints
- `comparison-table`: sticky first column (ZeroWater brand column), horizontal scroll container on mobile
- `tds-meter-display`: font scales from 72px (desktop) → 48px (tablet) → 36px (mobile) via fluid type
- `hero-dark`: two-column text + TDS panel split collapses to stacked single column at mobile; TDS meter moves below headline
- `filter-stage-tracker`: horizontal 5-step track collapses to a 2-column labeled grid on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact live border-radius values not confirmed from DOM; {rounded.sm} (8px) on buttons is an inference from visual proportion
- IBMPlexSerif usage split between 600 and 700 weight in hero sections not measured from live renders
- Hover/focus transition timing and easing curves not captured; 200ms ease is assumed throughout
- Mobile nav expanded-state background color and overlay opacity not observed
- Whether #5a31f4 (accent-purple) maps to a specific product sub-line (e.g. a pitcher range) or is incidental to the Shopify theme defaults is unclear
- Custom icon system style (line vs. filled, stroke weight, grid size) not confirmable from color extraction alone
- Footer column structure, background color treatment, and link styling not extracted
- Sale/promotional pricing treatment (strikethrough color, sale badge shape and color) not observed
- Product image aspect ratio conventions (square, 3:4, free crop) not confirmed
- Exact letter-spacing and line-height values for IBMPlexSerif display sizes are inferred, not measured from live text nodes
