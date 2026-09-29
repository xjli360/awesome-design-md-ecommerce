---
version: alpha
name: "Margaux"
source_url: "https://margauxny.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Amber interrupts near-black with unusual precision: #f59e0b lands on add-to-cart buttons, active filter indicators, and fit-quiz CTAs against an otherwise monochrome field of #141414 ink and white canvas — the brand's clearest statement that warmth is an architectural decision, not decoration. The warm cream band (#f7eadb) surfaces in seasonal promotion callouts and the fit-quiz entry module, evoking the tissue paper inside a shoe box and grounding a digital experience in a specific, physical sensory memory. The two amber values (#f59e0b base, #fbbf24 hover lift) create a subtle luminosity shift rather than the hard-darkening hover convention most footwear brands use, reinforcing a brand disposition toward lightness over weight. Canela's high-contrast hairline serifs carry the display register at weight 300 and generous scale — headlines lean 40–56px, trusting the typeface's inherent editorial posture over typographic force. TT Commons Pro and Inter assume functional custody below: navigation links, filter labels, and product names set between 11px and 16px with modest letter-spacing lifting the uppercase CTA labels into formal territory without stiffness. Corner radii split along a deliberate axis: product cards and editorial surfaces are flush ({rounded.none}), while width-selectors and option pills adopt {rounded.full} pill shapes, signaling interactivity and softening a configurator that might otherwise feel clinical. This pairing keeps the catalog in editorial mode and the customization layer in tool mode so the user never conflates the two registers. Collection grids run four columns on desktop in a 3:4 portrait ratio — tall enough to show foot-in-shoe silhouette, not merely an accessory floating on white. The hairline at #e2e2e2 and medium-gray body text at #545454 produce a three-stop grayscale that reads as controlled and precise against the warm cream accent. The footer inverts the palette entirely to #141414, with Canela wordmarks and TT Commons Pro column heads set in #ffffff — the same typeface pair that opens the page, now carrying the brand's closing posture in reverse.

colors:
  primary: "#f59e0b"
  primary-hover: "#fbbf24"
  primary-active: "#d97706"
  primary-disabled: "#fde68a"
  ink: "#141414"
  ink-deep: "#1f1f1f"
  body: "#545454"
  muted: "#888888"
  hairline: "#e2e2e2"
  canvas: "#ffffff"
  surface-muted: "#f6f6f6"
  surface-soft: "#f7eadb"
  surface-card: "#ffffff"
  on-primary: "#141414"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Canela', Georgia, serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Canela', Georgia, serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.13
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Canela', Georgia, serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.20
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Canela', Georgia, serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'TT Commons Pro', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'TT Commons Pro', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.03em
  body-md:
    fontFamily: "Inter, 'TT Commons Pro', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, 'TT Commons Pro', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'TT Commons Pro', Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  label-caps:
    fontFamily: "'TT Commons Pro', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'TT Commons Pro', Inter, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.10em
    textTransform: uppercase
  button-sm:
    fontFamily: "'TT Commons Pro', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.10em
    textTransform: uppercase
  nav-link:
    fontFamily: "'TT Commons Pro', Inter, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.05em
  price:
    fontFamily: "'TT Commons Pro', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.02em

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "none"
    padding: "0 0 2px 0"
    borderBottom: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
    activeIndicatorColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "3/4"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageBorderRadius: "{rounded.none}"
    padding: "{spacing.sm} 0"
    gap: "{spacing.xs}"
  editorial-hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaStyle: "button-primary"
    minHeight: 600px
    overlayOpacity: 0.25
  fit-quiz-band:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    ctaStyle: "button-primary"
    padding: "{spacing.xxl} {spacing.section}"
    rounded: "{rounded.none}"
  width-selector:
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    inactiveBackgroundColor: "{colors.canvas}"
    inactiveTextColor: "{colors.body}"
    unavailableTextColor: "{colors.hairline}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
    gap: "{spacing.xs}"
  option-pill:
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    inactiveBackgroundColor: "{colors.canvas}"
    inactiveTextColor: "{colors.ink}"
    unavailableTextColor: "{colors.hairline}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
    gap: "{spacing.xs}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    borderBottom: "1px solid {colors.hairline}"
    activeUnderlineColor: "{colors.primary}"
    activeUnderlineHeight: 2px
    height: 48px
  collection-grid:
    columns: 4
    gap: "{spacing.base}"
    mobileColumns: 2
    mobileGap: "{spacing.sm}"
    tabletColumns: 3
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    padding: "{spacing.xxl} 0"
    borderTop: "none"
  announcement-bar:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-caps}"
    height: 36px

## Components

### Buttons

**`button-primary`** — Amber (#f59e0b) fill with near-black on-primary text, uppercase tracked label at 13px, zero corner radius, 48px height. Hover lifts to #fbbf24 creating a luminosity shift rather than the standard darkening convention; active state drops to #d97706; disabled bleaches to #fde68a with medium-gray text. The sharp edge is intentional — softness is reserved for the pill-shaped customization layer, not CTAs.

**`button-secondary`** — Transparent fill with a 1px #141414 border and matching ink text, otherwise identical dimensions to button-primary. Pairs with button-primary in two-up layouts on the editorial hero and fit-quiz band; the border darkens to 1px solid #141414 on hover rather than changing background, maintaining visual weight parity with the amber primary beside it.

**`button-ghost`** — Borderless, uses only a 1px bottom border as underline affordance. Used for "Learn more" and editorial in-line CTAs where full button presence would interrupt the reading flow. Typography matches button-md (uppercase, tracked) but the inline underline signals lower hierarchy than the outlined secondary.

### Text Input

**`text-input`** — Full-width, no border-radius, 1px hairline (#e2e2e2) border at rest sharpening to 1px ink (#141414) on focus. The transition is the only animation; no shadow, no fill shift. Used in email capture, the fit quiz form, and checkout fields. Placeholder text renders at muted (#888888), backing off to body text (#545454) rather than going fully invisible.

### Navigation

**`nav-bar`** — 64px tall, white canvas with a 1px hairline bottom border. The Margaux wordmark sets in Canela display-sm (24px, weight 300) — the only serif in the bar, providing the brand's single typographic signature against TT Commons Pro nav links. Active nav states carry a 2px amber (#f59e0b) underline rather than a fill change, keeping the bar light and scannable. On mobile, collapses to hamburger with full-screen drawer.

### Product Card

**`product-card`** — Flush square images in 3:4 portrait ratio with zero border radius, title in TT Commons Pro title-sm below, price in the price scale. No star ratings, no badge overlays in the default grid state. On hover, a secondary colorway image cross-fades in without scale animation, maintaining the editorial stillness. Width availability indicators appear as pill-shaped micro-labels on hover, giving the customization signal without cluttering the grid at rest.

### Editorial Hero

**`editorial-hero`** — Full-bleed photography with an #141414 overlay at 25% opacity, Canela display-xl headline in on-dark white, body-md subhead, and a button-primary CTA centered or left-aligned at 600px minimum height. The amber CTA is the only warm element in a dark-ground composition, drawing the eye with contrast rather than animation. Mobile crops to a square or taller aspect with the headline reduced to display-md.

### Fit Quiz Band

**`fit-quiz-band`** — The warm cream surface (#f7eadb) differentiates this module from the white grid it interrupts, signaling a service interaction rather than a product listing. Canela display-md headline at weight 300 describes the width-finding quiz in two lines; body-md paragraph below in Inter; a single button-primary CTA. This is the highest-intent persuasion surface on the site outside of the PDP.

### Width Selector and Option Pills

**`width-selector`** and **`option-pill`** — Pill-shaped ({rounded.full}) toggles carrying width labels (Narrow, Medium, Wide) or customization options (toe shape, heel height, material). Active state fills to #141414 with white text; inactive sits on white with hairline border and body text; unavailable options fade the border and text to #e2e2e2 without strikethrough. The pill shape is the only place {rounded.full} appears in the UI, creating an immediately recognizable language for "this is a selection, not a navigation."

### Filter Bar

**`filter-bar`** — A 48px horizontal strip above the collection grid with uppercase-tracked labels (label-caps, 11px) for category filters. Active filter carries a 2px amber underline (#f59e0b) — the same amber accent signal used on nav active states — so the interaction language is consistent across both contexts. No dropdown or modal; filters apply immediately via URL parameter.

### Footer

**`footer`** — Full-width #141414 background reversing the palette, with on-dark (#ffffff) text throughout. Column headings use label-caps (uppercase, tracked, 11px) in white; link lists in body-sm Inter at 13px. No amber appears in the footer — the warm accent is reserved for interactive surfaces, not chrome. Social links and payment icons sit at the base in muted-icon treatment.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Collection grid drops to 2 columns; nav collapses to hamburger drawer; hero headline drops to display-md (32px); fit-quiz band stacks vertically with full-width CTA; width selector scrolls horizontally |
| Tablet | 744–1128px | Collection grid at 3 columns; nav shows full links without overflow; hero headline at display-lg (40px); fit-quiz band shifts to two-column layout |
| Desktop | 1128–1440px | Collection grid at 4 columns; full nav with hover underline states; hero at full display-xl (56px); filter-bar visible inline above grid |
| Wide | > 1440px | Max content width caps at 1440px with auto side margins; grid column widths grow with gaps rather than adding a 5th column; hero photography fills but text block remains max-width constrained |

### Touch Targets

- All option pills and width selectors maintain minimum 36px height on mobile even if visually smaller, via vertical padding adjustment
- Nav hamburger icon is 44×44px tap target regardless of visual icon size
- Footer links spaced at minimum 40px vertical intervals on mobile
- Filter bar scrolls horizontally on mobile with 16px padding bleed at scroll terminus

### Collapsing Strategy

- Navigation: full horizontal links → hamburger with slide-in drawer (no overlay menu stubs)
- Filter bar: inline strip → hidden behind a "Filter" ghost button that opens a bottom sheet modal
- Product card: hover-state secondary image swap disabled on touch devices; color dot indicators used instead
- Fit quiz band: two-column (image + text) → single column, image moved below headline or removed on small mobile
- Footer: multi-column grid → single-column stacked accordion on mobile, headings become expand/collapse toggles

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border-radius not confirmed — zero-radius assumed from brand's editorial posture but may be xs (2px) in production Shopify theme
- Canela font weight range used on site not confirmed; weight 300 assumed based on standard editorial usage, may include a weight 400 variant for subheadings
- Hover micro-interactions (image swap timing, underline animation duration) not extractable from static scrape
- Exact nav height (64px) estimated; may be 56px or 72px depending on announcement bar visibility
- Color roles for #1f1f1f vs #141414 separation not fully confirmed — both appear as near-black; may be the same value in different contexts rather than a deliberate two-stop system
- Secondary palette for limited-edition or seasonal colorways not captured; site may introduce additional accent tokens during sale periods
- Modal and drawer background scrim color and opacity not extracted
- Exact letter-spacing values for Canela display sizes not accessible without font metrics; values estimated from visual inspection conventions for that typeface
