---
version: alpha
name: "xTool"
source_url: "https://www.xtool.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The most calibrated detail in xTool's UI system is the primary CTA color: #00cb69, a machine-readout green borrowed from CNC status displays rather than consumer e-commerce convention, detonating against a layered grey canvas (#f8f9fd, #f2f3f5, #ecedf0) with the visual clarity of a "job running" indicator. The ink runs to #191a19 — not pure black but a near-black with a trace of olive warmth that softens the industrial reference without losing the workshop register. Type is set in InterTight, a narrow geometric sans optimized for label-dense specifications: weights cluster at 600–700 for headers and 400–500 for body, never reaching the heavy 800–900 range that would make a product spec page feel aggressive rather than precise. Montserrat appears on marketing callouts and hero headlines; Nunito Sans handles longer body paragraphs and review text.

  Corner radii are modest: {rounded.sm} (8px) on buttons and inputs, {rounded.md} (12px) on product cards — professional rather than playful, closer to industrial software than consumer lifestyle. Pill chips ({rounded.full}) appear only on category selectors and small filter tags, where their compact floating quality serves legibility in dense filter bars. Spacing leans generous, with section padding at 64px and product grid gutters at 24–32px — the photography-first approach puts large laser engravers and DTF printers in full-bleed hero frames where whitespace is the structural decoration.

  The danger and error states run through #9d0000 and #f5222d (traffic-light logic: green confirms, red warns), and a deep teal (#329179 / #108474) surfaces in secondary hover states and informational accents, maintaining the technical-precision register without repeating the primary green. Sale badges hit #9d0000, availability and buy buttons hit #00cb69, and the spectrum between is occupied by disciplined greys — a system that reads as workshop dashboard rather than marketplace.

colors:
  primary: "#00cb69"
  primary-active: "#28be44"
  primary-disabled: "#bfbfbf"
  secondary: "#329179"
  secondary-dark: "#108474"
  danger: "#9d0000"
  danger-bright: "#f5222d"
  ink: "#191a19"
  body: "#1d1d1d"
  muted: "#555555"
  muted-soft: "#7d827d"
  hairline: "#d9d9d9"
  hairline-soft: "#e5e5e5"
  canvas: "#f8f9fd"
  surface-soft: "#f2f3f5"
  surface-card: "#ecedf0"
  surface-strong: "#eeeeee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  info: "#1677ff"

typography:
  display-xl:
    fontFamily: "'InterTight', 'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'InterTight', 'Montserrat', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'InterTight', 'Montserrat', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'InterTight', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'InterTight', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'InterTight', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'InterTight', 'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'InterTight', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  badge:
    fontFamily: "'InterTight', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'InterTight', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "'InterTight', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'InterTight', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px

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
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 8px 20px
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    focusBorder: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 16px
    imageAspect: "4/3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    gap: 8px
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    minHeight: 560px
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "64px 0"
  category-chip:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
    iconColor: "{colors.muted}"
  promo-banner:
    backgroundColor: "{colors.secondary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    height: 40px
    padding: 0 16px
  spec-table-row:
    backgroundColor: "{colors.surface-soft}"
    alternateBackgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    padding: 8px 16px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-compare-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: 24px
    highlightBorder: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "64px 0 32px"

## Components

### Buttons
**`button-primary`** — The primary action button renders in #00cb69 at 48px height with {rounded.sm} corners (8px), never pill-shaped. In `:active` state the background shifts to the slightly deeper #28be44, maintaining the green-on-neutral signal without losing brand continuity; disabled state drains to {colors.primary-disabled} (#bfbfbf), communicating unavailability without introducing red. Text is InterTight 600 at 16px with 0.2px tracking for optical crispness against the saturated fill.

**`button-secondary`** — Canvas ({colors.canvas}) background with a 1px solid {colors.hairline} border and {colors.ink} text at the same 48px height as button-primary. Appears alongside the primary CTA in product page pairs ("Buy Now" + "Add to Cart") and in modal confirmation flows. The height match is intentional — both buttons sit on the same optical baseline.

**`button-ghost`** — Transparent background with {colors.hairline} border, {typography.button-sm} (14px InterTight 600). Used in filter panels, variant selectors, and wherever a tertiary action needs presence without competing with the primary green. Shares {rounded.sm} for system consistency.

**`button-dark`** — {colors.ink} fill with {colors.on-dark} text. Appears inside dark hero sections where the standard primary button would read as a floating green chip against the near-black field, and on dark promotional strip overlays.

### Navigation
**`nav-bar`** — 64px tall on a {colors.canvas} base with a 1px {colors.hairline} bottom rule. Navigation links in {typography.nav-link} (InterTight 500, 14px). Inverts to `nav-bar-dark` when the hero section bleeds to viewport top, switching to {colors.ink} background with {colors.on-dark} text for full-bleed product landing pages.

**`search-bar`** — 40px height, {colors.surface-soft} fill, {rounded.sm} radius, icon in {colors.muted} (#555555). On focus, the border transitions to 2px solid {colors.primary} — the green focus ring extends brand vocabulary into utility interactions, reinforcing that the CTA color owns "active state" across the entire UI.

**`promo-banner`** — 40px bar pinned above the nav in {colors.secondary-dark} (#108474, deep teal). Used for free-shipping thresholds, countdown promotions, and site-wide discount messaging. The teal distinguishes promotional context from the green primary CTA without introducing a third hue family.

### Product Card
**`product-card`** — {rounded.md} (12px) corners on a {colors.surface-card} (#ecedf0) base with 16px internal padding. Title in {typography.title-sm} (InterTight 600, 16px), price in {typography.price-display} (InterTight 700, 24px). The 4:3 image aspect ratio accommodates the boxy tabletop form factor of xTool's desktop laser units. Badge chips overlay the top-left of the image at 3px vertical, 8px horizontal padding.

### Hero Section
**`hero-section`** — Full-bleed {colors.ink} (#191a19) background at minimum 560px. Headline in {typography.display-xl} (InterTight 700, 48px, −0.5px tracking), subtitle in {typography.body-md}. The consistent dark hero creates a showroom-floor effect across product launch pages — machine photography glows against the near-black field with no additional overlay treatment needed. Primary CTA runs button-primary; secondary runs button-ghost or button-secondary depending on contrast context.

### Spec Table
**`spec-table-row`** — Alternating {colors.surface-soft} and {colors.canvas} rows with an 8px 16px padding rhythm. Labels in {typography.spec-label} (InterTight 600, uppercase, 0.5px tracking) — the all-caps treatment is the brand's clearest nod to instrument-panel UI conventions, distinguishing this component from standard prose tables. Values in {typography.body-sm}. Used on every product detail page to present laser power, working area, speed, connectivity, and material compatibility specs.

### Product Compare Card
**`product-compare-card`** — Default state: 1px {colors.hairline} border on {colors.canvas}. Selected/featured state: 2px solid {colors.primary} (#00cb69) highlight border with no fill change — the green border alone signals selection without altering the card's background. The comparison module is prominent in xTool's cross-product navigation, where buyers move between power tiers of the same laser family.

### Badges
**`badge-new`** — {colors.primary} (#00cb69) background, all-caps {typography.badge} (11px, 700 weight, 0.3px tracking), {rounded.xs} corners. Applied to recently-launched SKUs, reinforcing the green-as-active system language.

**`badge-sale`** — {colors.danger} (#9d0000) background, same typography specification. The deep crimson reads as reduction and urgency without the alarming brightness of a pure red, keeping the palette disciplined.

### Category Chip
**`category-chip`** — Default: {colors.surface-strong} background, {colors.body} text, {rounded.full} pill shape, 6px 16px padding. Active: {colors.ink} background with {colors.on-dark} text, producing a solid black selected chip. Used in horizontal-scroll filter rows on collection pages where buyers filter by machine type, material compatibility, or power class.

### Footer
**`footer`** — {colors.body} (#1d1d1d) background providing visual closure against the light-grey content field above. Column headings in {typography.title-sm} at {colors.on-dark}; body links in {typography.body-sm} at {colors.muted-soft} (#7d827d). The footer's greenish-grey link color rhymes subtly with the primary #00cb69, maintaining tonal coherence in a de-emphasized context.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero headline scales to display-md; spec tables scroll horizontally inside 300px max-height container; category chips in horizontal-scroll pill row |
| Tablet | 744–1128px | 2-column product grid; nav shows top-level categories with tap-triggered mega-menu; hero at display-lg; compare module reduces to 2-column |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with hover dropdowns; hero at display-xl; spec table fully visible with visible column widths |
| Wide | > 1440px | Max-width container (~1440px) centered with generous side gutters; grid stays 4 columns; hero photography expands to fill but text and CTA remain in the constrained column |

### Touch Targets
- All primary and secondary buttons: minimum 48px height satisfies 44px WCAG target
- Category chips expand to 10px 20px internal padding on mobile
- Nav links hold a minimum 44px hit-target height via padding, not element height
- Full product card is the tap target on mobile — no link-only zone inside the card
- Icon buttons (wishlist, share) minimum 40×40px with 4px external touch extension

### Collapsing Strategy
- Mega-nav collapses into a full-screen slide-out drawer on mobile; top-level category items become accordion sections
- Spec table scrolls horizontally inside a fixed-height container with a scroll-shadow affordance at the right edge
- Product comparison module reduces from 4-column to 2-column at tablet, hidden on mobile behind a "Compare" modal entry point
- Promo banner collapses to 32px height and truncates copy with ellipsis below 744px
- Hero subtitle copy is visually hidden on mobile to prevent text overload below the headline

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No yellow or gold color extracted — review star color (Judge.me integration confirmed by JudgemeIcons font) defaults to Judge.me's own orange-gold rather than a brand-defined value; exact hex unconfirmed
- Relative weight of Montserrat vs InterTight in marketing contexts not deterministic from extraction alone — assumed InterTight for all product/UI text, Montserrat for hero marketing headlines only
- Baskerville appears in the font stack but its use context (editorial blog, legal copy, or fallback only) is unconfirmed
- No animation or transition duration tokens extracted; easing curves for hover/CTA states unknown
- Dark mode support is unconfirmed — dark backgrounds may be section-level patterns rather than a system-level theme toggle
- Logo clear-space and minimum-size specifications not available from extraction
- `{colors.info}` (#1677ff) appears in extraction and likely originates from Ant Design component defaults (modal, tooltip); brand-intentional use unconfirmed
- Exact mega-menu layout structure, column count, and featured-image treatment not confirmed from extraction
