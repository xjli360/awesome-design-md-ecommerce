---
version: alpha
name: "Molekule"
source_url: "https://molekule.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  FDA clearance precedes the product name in the page title — that ordering is the brand's core argument: this is a medical instrument first and a home appliance second. Molekule builds its entire visual logic around a single chromatic column of green, running from the near-black forest of #161f15 through #0b5b30 and the brand primary #118849, then surfacing into light mint tones of #cfe9db and #a4f4c9 that fill cards and soft backgrounds; no competitor color appears in that column, with the greens doing clinical and natural work simultaneously. Akkurat LL — a Swiss modernist grotesque with nearly the same DNA as Helvetica but more open in tight settings — carries all interface text, from display-sized headlines at AkkuratPro-Light weight to compact UI labels in bold; Crimson Pro and Plantin appear as editorial accents, a serif counterpoint that occasionally grounds the all-sans system in something warmer, suggesting a brand that wants to feel scientific but not sterile. The canvas is clean white throughout the commerce flow, with surfaces floating on #dce7db at section breaks, and product cards using {rounded.md} corners — not the aggressive pill shapes of wellness startups, not the hard rectangles of industrial hardware. CTA buttons sit at {rounded.xs}, a restraint that reads as medical-grade rather than playful. The mint #cfe9db appears as badge fills and callout backgrounds, a visual shorthand for clean air. Dark marketing sections use #161f15, a green so deep it reads as black until placed beside actual black (#141414), at which point the forest undertone reveals itself. Technology communication dominates the component vocabulary: FDA-cleared badges, PECO callouts, and filtration statistics are first-class UI objects, not footnotes; {spacing.section} governs all major content breaks, and the warm-leaning gray tones (#d7d5d4, #3c3b3b) ensure the system reads earthy rather than synthetic.

colors:
  primary: "#118849"
  primary-active: "#0b5b30"
  primary-light: "#30694b"
  primary-disabled: "#71976b"
  primary-subtle: "#cfe9db"
  ink: "#141414"
  body: "#3c3b3b"
  muted: "#888888"
  muted-soft: "#a9a9a9"
  hairline: "#d7d5d4"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#dce7db"
  surface-card: "#ffffff"
  surface-mint: "#cfe9db"
  surface-deep: "#161f15"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  green-mid: "#30694b"
  green-sage: "#515650"
  green-moss: "#445b40"
  green-soft: "#cfe9db"
  green-bright: "#77eeaf"
  green-pale: "#a4f4c9"
  slate: "#4a5764"
  error: "#e50122"
  warning: "#f59e0b"

typography:
  display-xl:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', AkkuratPro-Light, Arial, 'Helvetica Neue', sans-serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.07
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.19
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.1px
  title-lg:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-sm:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.1px
  eyebrow:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 0
  editorial-serif:
    fontFamily: "'Crimson Pro', Plantin, Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  stat-number:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.04
    letterSpacing: -1px
  badge-label:
    fontFamily: "'Akkurat LL', 'Akkurat Pro', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.3px

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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    hover:
      backgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 1.5px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    hover:
      backgroundColor: "{colors.primary-subtle}"
  button-ghost-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    borderColor: "{colors.on-dark}"
    borderWidth: 1px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  announcement-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    padding: "{spacing.xl}"
    badgeBackgroundColor: "{colors.surface-mint}"
    badgeTextColor: "{colors.primary-active}"
    titleTypography: "{typography.title-lg}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.title-md}"
    shadow: "0 2px 12px rgba(17,136,73,0.06)"
    hover:
      borderColor: "{colors.primary}"
      shadow: "0 4px 24px rgba(17,136,73,0.12)"
  hero:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-dark}"
    eyebrowColor: "{colors.green-bright}"
    headlineTypography: "{typography.display-xl}"
    eyebrowTypography: "{typography.eyebrow}"
    bodyTypography: "{typography.body-md}"
    minHeight: 640px
    paddingX: "{spacing.section}"
    paddingY: "{spacing.section}"
  hero-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    eyebrowColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    eyebrowTypography: "{typography.eyebrow}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
  fda-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 12px
    height: 24px
  technology-badge:
    backgroundColor: "{colors.surface-mint}"
    textColor: "{colors.primary-active}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 5px 10px
  stat-callout:
    backgroundColor: "{colors.canvas}"
    numberTypography: "{typography.stat-number}"
    numberColor: "{colors.primary}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    dividerColor: "{colors.hairline}"
  editorial-module:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    quoteTypography: "{typography.editorial-serif}"
    quoteColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    eyebrowTypography: "{typography.eyebrow}"
    padding: "{spacing.section}"
  dark-section:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.green-bright}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  comparison-table:
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    rowAltBackgroundColor: "{colors.surface-soft}"
    cellTypography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    borderColor: "{colors.hairline}"
    checkColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-dark}"
    mutedTextColor: "{colors.green-sage}"
    linkColor: "{colors.green-bright}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.caption}"
    dividerColor: "#2a3a29"
    padding: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — Forest green (#118849) fill with white text, Akkurat Medium 16px, 4px radius ({rounded.xs}), 48px tall. On hover the fill deepens to {colors.primary-active} (#0b5b30), a perceptibly darker forest tone that signals engagement without introducing a new hue. Disabled state uses {colors.primary-disabled} (#71976b), a muted sage read as unavailable without harsh graying. Used for all primary commerce actions: "Shop Now," "Add to Cart," "Get Started."

**`button-secondary`** — White fill with a 1.5px #118849 border and matching green text, matching the geometry and typographic weight of the primary button. Hover fills with {colors.primary-subtle} (#cfe9db), a mint wash that signals interactivity without competing with the primary button's weight. Used for secondary actions like "Learn More" and "Compare Models."

**`button-ghost-dark`** — Transparent background with white border and white text, reserved for CTA placement over {colors.surface-deep} sections. Same Akkurat Medium 16px type as the primary family ensures visual consistency across light and dark contexts.

**`button-text-link`** — Inline green text with underline, no background or border. Used for supplementary navigation within body copy, FAQ modules, and legal footer links.

### Navigation

**`nav-bar`** — White 64px bar with #118849 Molekule wordmark at left, links in Akkurat Regular 14px at {colors.ink}, hairline bottom border. A green underline or dot marks the active section. On scroll, the bar holds position (sticky) and retains its white background without adding shadow weight. On mobile, collapses to logo plus hamburger icon with a full-height overlay drawer.

**`announcement-banner`** — A 36px green ribbon at the absolute top of the page, Akkurat Regular 12px in white, centered. Communicates promotions, free shipping thresholds, or FDA clearance messaging. Sits above the nav in the document flow and is dismissible with a close icon at right.

### Cards

**`product-card`** — White card at {rounded.md} with a 1px {colors.hairline} border and a subtle green-tinted box shadow. Product name in {typography.title-lg}, price in {typography.title-md}, supporting copy in {typography.body-sm}. FDA-cleared and model-tier `technology-badge` elements appear in the upper corner of the card image. On hover the border animates to {colors.primary} and the shadow lifts, signaling interactivity. Cards appear in two- and three-column grids depending on viewport.

### Hero

**`hero`** — Full-bleed {colors.surface-deep} (#161f15) section with headline in {typography.display-xl} at AkkuratPro-Light weight and white text. An uppercase eyebrow label in {colors.green-bright} (#77eeaf) precedes the headline, front-loading the technology claim before the product name appears. A primary CTA and optional ghost button sit below. Used for the above-the-fold homepage and campaign landing pages where maximum brand voltage is needed.

**`hero-light`** — Same compositional structure as `hero` but on white canvas with {colors.ink} headline text and {colors.primary} eyebrow. Used for product detail page headers and interior section entrances where the dark background would feel tonally heavy or inconsistent with the commerce context below.

### Badges and Trust Signals

**`fda-badge`** — Pill-shaped ({rounded.full}) #118849 badge in Akkurat Medium 11px white text, 24px tall. Displays "FDA-Cleared." This badge is first-class UI — it appears in the nav bar, product cards, PDPs, and checkout confirmation, representing the primary differentiator between Molekule and commodity air purifiers. It receives prominent placement and is never buried below the fold on product pages.

**`technology-badge`** — Rectangular {rounded.xs} badge with {colors.surface-mint} fill and {colors.primary-active} text. Used for technology callouts — "PECO Technology," "H13 HEPA," "For Large Rooms" — and stackable in groups of two or three in product cards and PDP headers without visual crowding.

### Statistics

**`stat-callout`** — Large Akkurat Light numeral in {colors.primary} ({typography.stat-number}, 48px) over a muted gray descriptor label ({typography.caption} in {colors.muted}). Groups of three or four stats sit in a horizontal row separated by {colors.hairline} vertical dividers. Used in "Why Molekule" and efficacy proof sections to communicate filtration percentages, particle capture rates, and room coverage figures as scannable landmarks.

### Editorial

**`editorial-module`** — {colors.surface-soft} (#dce7db) background section with Crimson Pro pull-quote text ({typography.editorial-serif}) in {colors.ink}, preceded by an uppercase eyebrow in {colors.primary}. Used in "The Science" and brand story narrative sections to give research claims an authoritative long-form reading texture, tonally distinct from the product commerce UI. The serif intrusion into an otherwise all-sans system signals that this content is worth slowing down for.

### Dark Sections

**`dark-section`** — {colors.surface-deep} (#161f15) background with white body copy and {colors.green-bright} (#77eeaf) accent elements, used to present indoor air quality data, pollution statistics, or product technology diagrams. Headlines in {typography.display-md}, Akkurat Regular. The bright mint accent is the only color that reads clearly against the near-black green ground without feeling jarring or synthetic.

### Comparison

**`comparison-table`** — Product comparison table with {colors.primary} header row and white text, alternating {colors.surface-soft} row fills, and green checkmark icons for included features. {rounded.sm} on the outer container. Used on the product lineup page to distinguish Air Mini, Air Pro, and Air Pro+ models across coverage area, filtration type, and connectivity features.

### Footer

**`footer`** — {colors.surface-deep} (#161f15) background with column headings in Akkurat Bold 11px uppercase at {colors.green-sage} and link text in {colors.green-bright}. Body type in {colors.on-dark} at {typography.body-sm}. A dark green divider (#2a3a29 — slightly lighter than the background) separates content columns from the legal footer row. Social icons appear in {colors.muted-soft} and brighten to {colors.green-bright} on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout. Nav collapses to logo plus hamburger with full-height overlay drawer. Hero headline drops to {typography.display-md}. Product cards stack vertically. Stat callouts reflow to a 2×2 grid. Comparison table freezes first column and scrolls horizontally. |
| Tablet | 744–1128px | Two-column product card grid. Nav shows logo, hamburger, and cart icon only. Hero headline scales to {typography.display-lg}. Stat callouts in a 4-across horizontal row. Editorial modules shift to a 60/40 text-image split. |
| Desktop | 1128–1440px | Full nav with all category links visible. Three-column product grid. Hero at full {typography.display-xl} with side-by-side product image. All comparison table columns visible without horizontal scroll. |
| Wide | > 1440px | Content max-width capped at 1440px with auto side margins. Hero background bleeds full viewport width. Section vertical padding scales via CSS clamp to approximately {spacing.section} × 1.5. |

### Touch Targets

- All buttons minimum 48px tall and 44px wide
- Nav hamburger: 44×44px tap area with padding
- Product card fully tappable as a single target on mobile — no isolated CTA required
- Badge labels are display-only; no tap target required
- Footer links: 40px minimum tap height via increased line-height

### Collapsing Strategy

- Horizontal stat rows collapse to a 2-column grid at tablet width and a single column on mobile
- Three-column product grid steps to two columns at tablet, single column on mobile
- Editorial module text-image splits stack image below text on mobile with full-width image bleed
- Comparison table freezes the model name column and allows horizontal scroll on tablet and mobile viewports
- Announcement banner text truncates to a single centered line with ellipsis below 375px viewport width
- Hero eyebrow label and headline maintain their vertical stacking order across all breakpoints; only font size scales

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom icon set was captured in extraction — Molekule may use a proprietary SVG icon library for navigation, filter indicators, and air quality UI not visible in the color/font pass
- Serif weight and proportion in the live design is unconfirmed: Crimson Pro and Plantin appear in the font stack but may be limited to editorial landing pages; their frequency relative to Akkurat is estimated
- Exact button border-radius was not measured from live CSS — {rounded.xs} (4px) is inferred from the medical-precision aesthetic and general brand positioning
- Motion and animation system not extractable: transition durations, easing curves, and scroll-triggered animation behavior for product cards, stat counters, and hero elements are unspecified
- Dark-mode support is unclear — meta theme-color is #ffffff, indicating a light-primary system, but Molekule's homepage has historically used a dark-forward layout and a dark variant may carry distinct token values
- Social platform colors (#1da1f1, #4266b2, #f14336) were excluded from the brand palette as third-party embed artifacts
- Akkurat LL weight availability in the web font delivery is unconfirmed — the presence of AkkuratPro-Bold and AkkuratPro-Light in the stack suggests a two-weight delivery; the Medium (500) weight used in button and title styles is assumed but may fall back to Bold in practice
- Filter/air-quality indicator UI (particle counters, real-time air quality displays) likely uses a distinct sub-palette not fully captured in the static extraction
