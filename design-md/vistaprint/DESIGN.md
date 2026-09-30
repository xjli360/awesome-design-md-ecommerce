---
version: alpha
name: "Vistaprint"
source_url: "https://www.vistaprint.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Eleven categorically mapped hues — teal (#117a5e) against sustainability copy, burnt orange (#b94f07) for urgency and rush shipping, salmon (#ffa497) for lifestyle product ranges — transform Vistaprint's color system from a brand palette into a navigational schema that customers decode before they read a headline. The structural axis runs deep navy (#2f3a53) as primary ground to sky-bright accent (#6fd0f5); this specific navy-to-cerulean contrast carries more specificity than the undifferentiated blue-gray systems that most print platforms use. Equally sharp is the type pairing: Tiempos, an editorial serif with ink-press lineage, takes the display and headline register while Graphik handles the functional UI layer — a combination that positions the brand as designed-for-professionals rather than a commodity print shop. Darker navy (#003d62) frames the footer and hero bands, providing visual mass without leaning on product photography to supply it. Warm tinted surfaces (#fff1de, #ffeeeb) back promotional modules and sale callouts; cool-tinted surfaces (#e5f5fd, #e2f8e7) frame informational or environmental messaging — the system encodes editorial tone through surface tint rather than copy length alone. The red (#cc3011) is reserved exclusively for sale pricing and urgency badges; amber (#faa837) marks trending or featured items. Corners stay measured rather than generous: product cards and inputs at {rounded.sm}, primary buttons at {rounded.xs}, nothing reaching pill shape — signaling a working-professional audience rather than a consumer lifestyle brand. Interactive affordances — focus rings, active states, link underlines — run through {colors.primary-accent}, keeping the energetic sky blue active across the interaction layer without competing with {colors.accent-red}'s urgency signal. The result is a printing platform whose color breadth is not decorative abundance but a compressed catalog index.

colors:
  primary: "#2f3a53"
  primary-active: "#003d62"
  primary-disabled: "#b9bcc5"
  primary-accent: "#6fd0f5"
  ink: "#1d1d1d"
  body: "#3a3a3a"
  muted: "#656b80"
  ink-soft: "#505050"
  hairline: "#e6e6e6"
  hairline-mid: "#b9bcc5"
  canvas: "#ffffff"
  surface-soft: "#f2f3f4"
  surface-card: "#ffffff"
  surface-warm: "#fff1de"
  surface-promo: "#ffeeeb"
  surface-cool: "#e5f5fd"
  surface-eco: "#e2f8e7"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-red: "#cc3011"
  accent-red-deep: "#a5030b"
  accent-orange: "#faa837"
  accent-orange-deep: "#b94f07"
  accent-teal: "#117a5e"
  accent-green: "#77ce97"
  accent-salmon: "#ffa497"
  navy-deep: "#003d62"
  scrim: "#1d1d1d"

typography:
  display-xl:
    fontFamily: "Tiempos, Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Tiempos, Georgia, serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Tiempos, Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Graphik, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Graphik, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "Graphik, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Graphik, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Graphik, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label-sm:
    fontFamily: "Graphik, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "Graphik, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Graphik, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "Graphik, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  price-large:
    fontFamily: "Graphik, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Graphik, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "Graphik, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.3px
    textTransform: uppercase
  tag:
    fontFamily: "Graphik, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    states:
      hover:
        backgroundColor: "{colors.primary-active}"
      disabled:
        backgroundColor: "{colors.primary-disabled}"
        cursor: not-allowed

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    states:
      hover:
        backgroundColor: "{colors.surface-soft}"
        borderColor: "{colors.primary-active}"

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary-accent}"
    typography: "{typography.button-md}"
    padding: 12px 0

  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 34px

  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline-mid}"
    borderFocusColor: "{colors.primary-accent}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    padding: 10px 14px
    labelTypography: "{typography.label-sm}"
    labelColor: "{colors.body}"

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxHeight: 32px
    activeColor: "{colors.primary}"
    hoverColor: "{colors.primary-active}"

  mega-menu:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.primary}"
    padding: "{spacing.xl} {spacing.xxl}"
    shadow: "0 8px 24px rgba(47,58,83,0.12)"

  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    imageAspectRatio: "4/3"
    priceTypography: "{typography.price-large}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.accent-red}"
    originalPriceTypography: "{typography.price-sm}"
    originalPriceColor: "{colors.muted}"
    padding: "{spacing.base}"
    states:
      hover:
        borderColor: "{colors.hairline-mid}"
        shadow: "0 4px 16px rgba(47,58,83,0.10)"

  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.primary-accent}"
    minHeight: 480px
    paddingY: "{spacing.xxl}"

  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.tag}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
    border: "1px solid {colors.hairline}"

  urgency-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px {spacing.xs}"

  promo-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-red}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
    borderLeft: "3px solid {colors.accent-orange}"

  search-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline-mid}"
    borderFocusColor: "{colors.primary-accent}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    height: 48px
    padding: "0 {spacing.base}"
    iconColor: "{colors.muted}"
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"

  trust-signal:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    iconColor: "{colors.primary-accent}"
    headingTypography: "{typography.label-sm}"
    bodyTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"

  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary-accent}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    legalTypography: "{typography.caption}"
    legalColor: "{colors.muted}"
    padding: "{spacing.xxl} 0"

  price-tag:
    salePriceTypography: "{typography.price-large}"
    salePriceColor: "{colors.accent-red}"
    originalPriceTypography: "{typography.price-sm}"
    originalPriceColor: "{colors.muted}"
    textDecoration: line-through

  quantity-stepper:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 40px

## Components

### Buttons
**`button-primary`** — The primary action uses deep navy (#2f3a53) with white text at `{rounded.xs}` corners, projecting utility and authority rather than warmth. On hover the background deepens to `{colors.primary-active}` (#003d62); the disabled state drains to `{colors.primary-disabled}`, a desaturated blue-gray that communicates unavailability without alarm. Button text is `{typography.button-md}` at weight 600 in Graphik — heavier than body copy, lighter than a display head.

**`button-secondary`** — An outlined variant with a 1.5px navy border on a white field; background fills to `{colors.surface-soft}` on hover, keeping the hover state legible on both white and light-gray page backgrounds. Used for secondary actions like "Preview design" or "Save for later" alongside a primary purchase CTA.

**`button-ghost`** — Transparent background with `{colors.primary-accent}` sky-blue text, no border. Used inline within body copy, help text, or category navigation where a bordered button would impose too much visual weight. Signals a hyperlink-level action at button-grade type weight.

**`button-sm`** — The compact variant (34px height) for dense product-listing rows, quantity controls, or badge-adjacent actions. Same navy treatment as primary, reducing only size and padding.

### Inputs
**`text-input`** — A clean rectangular input at `{rounded.xs}` with a `{colors.hairline-mid}` border at rest; focus ring transitions to `{colors.primary-accent}`, mirroring the interactive-layer accent throughout the system. Form labels use `{typography.label-sm}` at medium weight, sitting above the input rather than inside it — keeping the placeholder slot free for contextual guidance. Height is 44px across all breakpoints.

### Navigation
**`nav-bar`** — A 64px white bar with a 1px `{colors.hairline}` bottom border. The Vistaprint wordmark sits left; product-category links run center in `{typography.nav-link}` at weight 500. A utility cluster — search icon, cart, account — sits right. No shadow is added on scroll; shadow is reserved exclusively for the mega-menu reveal. Active category links accent to `{colors.primary}`; hover steps to `{colors.primary-active}`.

**`mega-menu`** — A full-width panel that drops below the nav bar on category hover, bounded top by a `{colors.hairline}` rule and lifted by a soft navy-tinted shadow. Column headings use `{typography.title-sm}` semibold; links use `{typography.body-sm}` regular at `{colors.body}`. Each product-category column may carry its categorical accent color as a left-side icon or rule, connecting the nav structure back to the multi-hue palette.

### Product Card
**`product-card`** — A lightly bordered card at `{rounded.sm}` with a 4:3 image crop. Title sits in `{typography.title-md}`; price in `{typography.price-large}`. When a sale price is present, the original renders in `{colors.muted}` with strikethrough at `{typography.price-sm}` and the sale figure shifts to `{colors.accent-red}`. On hover the border steps to `{colors.hairline-mid}` and a shallow box shadow lifts the card — a motion cue without full elevation.

### Hero
**`hero`** — Full-width navy (#2f3a53) band with white text, minimum 480px tall. The headline uses `{typography.display-xl}` in Tiempos — the editorial serif earns its place here by giving the brand designed authority a sans-only system wouldn't supply. Subheadings drop to `{typography.display-sm}` in the same face. Sky-blue `{colors.primary-accent}` marks CTA labels or highlight words within the headline, giving the dark composition a focal point without adding a competing hue.

### Category Chip
**`category-chip`** — A small pill-shaped filter tag (`{rounded.full}`) used in product-listing filter rows and homepage browse rails. At rest: `{colors.surface-soft}` background, `{colors.body}` text, hairline border. When active: background flips to `{colors.primary}`, text to white. Set in `{typography.tag}` — small but not micro — so horizontal scroll rows remain readable on mobile.

### Urgency Badge
**`urgency-badge`** — A flat `{colors.accent-red}` tag at `{rounded.xs}` overlaid on product cards, cart line items, or deadline-driven promotional copy. Set in `{typography.badge}` — 11px uppercase with 0.3px letter-spacing — so the tag reads at thumbnail scale. Usage is narrowly reserved for sale events and shipping deadlines; deploying it decoratively would erode the urgency signal.

### Promo Banner
**`promo-banner`** — A warm-tinted (`{colors.surface-warm}`) horizontal strip with a 3px left-side amber rule (`{colors.accent-orange}`). Used for sitewide discount announcements or seasonal campaign messaging. Body copy is `{typography.body-sm}`; the discount value or promo code can escalate to `{typography.title-sm}` inline. The warm surface distinguishes the banner from the white page body without requiring a full-bleed color band.

### Search
**`search-bar`** — A 48px input with a right-attached submit button in `{colors.primary}`. At rest the border is `{colors.hairline-mid}`; focus transitions the border to `{colors.primary-accent}`, consistent with the text-input focus convention. The magnifier icon uses `{colors.muted}`. On mobile the bar collapses behind a search icon in the nav that expands to a full-screen overlay, preventing zoom-on-focus keyboard issues on iOS.

### Trust Signal
**`trust-signal`** — A compact info tile on `{colors.surface-soft}` at `{rounded.sm}` pairing a `{colors.primary-accent}` icon with a heading in `{typography.label-sm}` and supporting detail in `{typography.caption}`. Appears in three-up or four-up horizontal rows beneath the hero or above the footer — site-quality guarantees, delivery estimates, design-tool callouts. The sky-blue icon color anchors these tiles back to the interactive accent, reinforcing that the brand's cerulean is the "help and afford" color.

### Footer
**`footer`** — A `{colors.navy-deep}` band using the full dark-background vocabulary: `{colors.on-dark}` body text, `{colors.primary-accent}` link color, `{colors.canvas}` on hover. Column headings in `{typography.title-sm}` semibold; navigation links in `{typography.body-sm}` regular. Legal copy sits in `{typography.caption}` at `{colors.muted}`, slightly dimmed against the dark field. The footer is the only surface that uses navy-deep as a background — no other component shares this register.

### Price Tag
**`price-tag`** — Sale price renders in `{colors.accent-red}` at `{typography.price-large}` (22px, weight 700); the original price sits immediately adjacent in `{typography.price-sm}` at `{colors.muted}` with CSS `text-decoration: line-through`. The red-muted contrast communicates was/now without an explanatory label, keeping the card layout compact.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid. Nav collapses to hamburger + search icon. Hero stacks text above CTA. Product grid is 2-up. Category chips scroll horizontally. Mega-menu becomes full-screen drawer. |
| Tablet | 744–1128px | 2–3 column product grid. Nav retains wordmark + search + cart; category links move to a horizontal scroll row beneath the main bar. Hero shifts to side-by-side text and image layout. |
| Desktop | 1128–1440px | Full mega-menu active. 4-column product grid. Nav bar at full 64px with all category links visible. Hero spans full bleed within a 1200px max-width content container. |
| Wide | > 1440px | Max content width 1440px; side gutters grow. Hero image fills the available field; headline block is constrained to ~600px. Product grid stays 4-column with increased card padding. |

### Touch Targets
- Minimum 44×44px for all interactive controls — buttons, chips, quantity steppers, icon buttons
- Mobile drawer nav links expand to full-width rows with 52px minimum tap height
- Product cards are fully tappable — the entire card surface links to the product detail page, not just the image or title
- Search input on mobile activates a full-screen overlay to avoid zoom-on-focus keyboard behavior on iOS

### Collapsing Strategy
- Category navigation: desktop mega-menu → tablet horizontal scroll row → mobile full-screen drawer
- Search: desktop inline bar with attached submit button → mobile icon-to-full-screen-overlay
- Trust signals: desktop 4-up horizontal row → tablet 2×2 grid → mobile single-column stack
- Footer: desktop 5-column link grid → mobile single-column accordion with expand/collapse per section
- Product grid: 4-up (desktop) → 3-up (tablet) → 2-up (mobile)
- Hero: side-by-side text + image (desktop/tablet) → stacked text-above-image (mobile)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Canvas white (#ffffff) was not in the extracted palette (filtered as a framework default); all card and page-background whites are inferred as standard white rather than a confirmed off-white brand canvas
- Exact Tiempos sub-variant (Tiempos Text vs. Tiempos Headline) and available optical sizes are unconfirmed; `Tiempos` is used as the family name without specifying a cut
- Graphik weights available in the production type specimen are unknown; weights 400, 500, and 600 are used conservatively as likely-available cuts
- Category-to-color mapping — which specific hex corresponds to which product vertical (business cards, signage, apparel, packaging) — could not be reliably extracted from static analysis
- Interactive motion timings (easing curves, hover transition durations) were not extractable from the live site
- Exact box-shadow values are approximated from visual convention; no design-token source for elevation was found
- Dark-mode token set is unknown; the deep-navy footer is the only confirmed dark-surface component
- Primary button border-radius may differ slightly from the `{rounded.xs}` (4px) approximation; Vistaprint's buttons appear close to square-cornered but exact measurement is unconfirmed
