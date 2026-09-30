---
version: alpha
name: "Bite"
source_url: "https://bitestep.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A glass jar of 62 compressed toothpaste bits — not a squeeze tube, not a pump, not a plastic cap — is where Bite's entire visual grammar begins, and the material specificity of that jar cascades into every pixel decision. The canvas holds a warm near-white, a shade close to natural linen (#FAFAF7), wide enough to let product photography breathe against a surface that reads closer to cotton than screen. The primary accent sits in a deep forest green, a register oral-care convention avoids but that Bite's zero-waste positioning earns outright — it reads chlorophyll and glass recycling rather than clinical white. Typography runs a single geometric grotesque at every scale; no serif appears on any product-facing surface, with weight variation doing all the hierarchy work and letter-spacing kept tight or at zero throughout. Section gutters run at 64–80px minimum; the glass jar image never touches a card border. The subscription configurator, Bite's primary conversion funnel, carries its own visual layer — a pill-segmented three-step progress indicator in muted sage that activates with a 2px `{colors.primary}` border rather than the heavy numbered circles of standard checkout UI. Ingredient-list sections break from the grid into full-bleed editorial treatments where a single ingredient name renders at 72px, borrowing print packaging language rather than web PDP convention, and the sections alternate forest-green and warm-white in a binary rhythm down the page. Trust signals (zero plastic waste, B-Corp certified, carbon-neutral shipping) appear as horizontal eyebrow-type pill chips at 11px uppercase — never as star-count widgets. Social proof enters through pull-quote photography rather than review carousels, keeping the page tone editorial rather than aggregated.

colors:
  primary: "#2E4D3C"
  primary-active: "#1E3329"
  primary-disabled: "#A8BFAF"
  ink: "#1A1A1A"
  body: "#3D3D3D"
  muted: "#717171"
  muted-soft: "#9A9A9A"
  hairline: "#E5E0D8"
  hairline-soft: "#EFEBE5"
  canvas: "#FAFAF7"
  canvas-warm: "#F5F0E6"
  surface-soft: "#F0EDE7"
  surface-card: "#FFFFFF"
  surface-refill: "#EAF0EA"
  surface-starter: "#F5EEE2"
  on-primary: "#FFFFFF"
  accent-mint: "#B8D4C4"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'GT Walsheim', 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.07
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'GT Walsheim', 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'GT Walsheim', 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.21
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'GT Walsheim', 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  title-lg:
    fontFamily: "'GT Walsheim', 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'GT Walsheim', 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'GT Walsheim', 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'GT Walsheim', 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'GT Walsheim', 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'GT Walsheim', 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  eyebrow:
    fontFamily: "'GT Walsheim', 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.36
    letterSpacing: 0.1em
    textTransform: uppercase
  ingredient-hero:
    fontFamily: "'GT Walsheim', 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px
  button-md:
    fontFamily: "'GT Walsheim', 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "'GT Walsheim', 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0
  nav-link:
    fontFamily: "'GT Walsheim', 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 26px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  hero:
    backgroundColor: "{colors.canvas-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    layout: split-50-50
    imageSide: right
    paddingY: "{spacing.section}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    imageBorderRadius: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-sm}"
  subscription-step-indicator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.primary}"
    activeBorderColor: "{colors.primary}"
    rounded: "{rounded.xl}"
    typography: "{typography.caption}"
  sustainability-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  ingredient-spotlight:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.ingredient-hero}"
    bodyTypography: "{typography.body-md}"
    layout: full-bleed
    paddingY: "{spacing.xxl}"
  trust-badge-strip:
    backgroundColor: "{colors.canvas-warm}"
    textColor: "{colors.muted}"
    typography: "{typography.eyebrow}"
    layout: horizontal-scroll
    paddingY: "{spacing.lg}"
    gap: "{spacing.xl}"
  flavor-selector:
    backgroundColor: "{colors.surface-card}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.hairline}"
    selectedBorder: "1.5px solid {colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
  refill-upsell-card:
    backgroundColor: "{colors.surface-refill}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    badgeBackgroundColor: "{colors.primary}"
    badgeTextColor: "{colors.on-primary}"
    badgeTypography: "{typography.eyebrow}"
    badgeRounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"

## Components

### Buttons

**`button-primary`** — Forest green (`{colors.primary}`) pill at full radius (`{rounded.full}`), 48px height, white type at `{typography.button-md}`. Carries all primary conversion actions: "Get Started," "Subscribe & Save," and "Add to Bag." Active state drops to `{colors.primary-active}` without altering shape; disabled state desaturates to pale sage `{colors.primary-disabled}`. This is the only CTA shape on the site — Bite does not use square or softly-rounded buttons anywhere.

**`button-secondary`** — Transparent fill with a 2px `{colors.primary}` stroke and matching green type at the same `{rounded.full}` pill radius. Used beneath the primary CTA in dual-button hero sections and on "Learn More" or variant-comparison contexts. Hierarchy between primary and secondary reads through fill versus outline, never through shape change.

**`button-ghost`** — No border, no fill; underlined `{colors.ink}` text at `{typography.button-md}`. Reserved for tertiary low-stakes actions such as "Cancel subscription," "Skip this delivery," or inline text links within help and account flows. Never appears as a standalone CTA in marketing surfaces.

### Text Input

**`text-input`** — Canvas white fill (`{colors.canvas}`) with a `{rounded.md}` 12px radius and a 1px `{colors.hairline}` border that sharpens to `{colors.primary}` on focus. Fixed 48px height, `{typography.body-md}` type. Email capture fields in the hero and footer share this spec unchanged; checkout address and billing fields inherit it identically. No floating label pattern — placeholder text retreats on focus without animation.

### Navigation

**`nav-bar`** — 64px fixed bar on `{colors.canvas}` with a `{colors.hairline-soft}` base border. Logo anchors left; product category links (Toothpaste Bits, Mouthwash, Floss, Gum) center using `{typography.nav-link}` at 14px/500 weight; account and cart icons sit right. A secondary sustainability-badge strip can occupy a band directly below, adding approximately 40px to occupied header height. On mobile the center links collapse into a hamburger icon opening a full-height slide-in drawer.

### Hero

**`hero`** — Warm linen background (`{colors.canvas-warm}`) in a 50/50 split at desktop, glass-jar product shot on the right, headline plus CTA stack on the left. Headline at `{typography.display-xl}` (56px/700/−0.5px tracking), supporting copy at `{typography.body-md}`, primary button pill below with 16px top margin. Vertical padding at `{spacing.section}`. On mobile the image stacks above the text block at full viewport width, then the copy and CTA follow below.

### Product Card

**`product-card`** — White `{colors.surface-card}` surface with `{rounded.lg}` corners and `{spacing.lg}` inner padding. Product image occupies the upper portion with a nested `{rounded.md}` crop that keeps the jar silhouette from touching card edges. Title typeset in `{typography.title-md}`, price in `{typography.title-sm}`. No star rating widget appears on the card face — review data surfaces on the PDP only. Cards compose into a three-column grid at desktop, two-column at tablet, single-column at mobile.

### Subscription Step Indicator

**`subscription-step-indicator`** — A three-segment horizontal pill progress tracker for the kit builder configurator. Inactive segments use `{colors.surface-soft}` fill and `{colors.muted}` label text at `{typography.caption}`, shaped by `{rounded.xl}`. The active segment gains a 2px `{colors.primary}` border and primary-colored text without changing its pill geometry. Segment labels carry the step name rather than a numeral — no filled circles or numbered badge convention.

### Sustainability Badges

**`sustainability-badge`** — Pill chips in `{colors.surface-soft}` carrying short claim text ("Zero Plastic," "Recyclable Glass," "Leaping Bunny," "Carbon Neutral Shipping") at `{typography.eyebrow}` — 11px uppercase with 0.1em tracking. Appear in a horizontal row below the nav bar, between content sections, and within footer columns. Entirely non-interactive; no hover state. No icon glyphs accompany the text — the claim stands alone.

### Ingredient Spotlight

**`ingredient-spotlight`** — Full-bleed section on `{colors.primary}` forest green with `{colors.on-primary}` white type throughout. The ingredient name renders at `{typography.ingredient-hero}` — the sole instance on the page where type reaches 72px; every other display scale stays at or below 56px. Three to four sentences of supporting copy follow in `{typography.body-md}`. These sections alternate with `{colors.canvas-warm}` warm-white equivalents to produce a green/linen binary cadence down the long-scroll page.

### Trust Badge Strip

**`trust-badge-strip`** — A full-width band on `{colors.canvas-warm}` carrying four to six proof claims at `{typography.eyebrow}`, items separated by centered dot glyphs. Padding `{spacing.lg}` top and bottom. At desktop the strip distributes items evenly across the full viewport; at mobile it becomes a horizontally scrollable container with a visible overflow hint on the trailing edge. Non-interactive throughout.

### Flavor Selector

**`flavor-selector`** — Inline pill chips for product variant selection (Mint, Charcoal, Watermelon Sorbet, Berry Twist). Default state: `{colors.surface-card}` fill, `{colors.hairline}` border, `{colors.ink}` text at `{typography.body-sm}`. Selected state: `{colors.primary}` fill, `{colors.on-primary}` text, `{colors.primary}` border. Full radius (`{rounded.full}`), 8px 18px padding. Chips wrap to a second row at narrow viewports rather than scroll horizontally — no truncation or overflow pattern.

### Refill Upsell Card

**`refill-upsell-card`** — Surfaces in the cart drawer and post-purchase confirmation. The `{colors.surface-refill}` sage-tinted background visually separates it from standard white product cards without requiring a border. A "SAVE 15%" badge anchors the top-right corner: `{colors.primary}` fill, `{colors.on-primary}` text, `{typography.eyebrow}` label at `{rounded.full}` radius. Card title in `{typography.title-md}`, supporting copy in `{typography.body-sm}`.

### Footer

**`footer`** — Full `{colors.primary}` forest green background, `{colors.on-primary}` white type throughout. Four columns at desktop: Products, Sustainability, Account, Social. Column headings at `{typography.title-sm}`, links at `{typography.body-sm}`. Newsletter email input inherits the text-input spec with a white-bordered inversion against the dark fill. No light footer variant exists — the green footer is consistent across every page template in the site.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout. Hero image stacks above text and CTA block. Nav collapses to hamburger with full-height slide-in drawer. Ingredient spotlight headline scales from 72px to 40px. Flavor chips wrap to second row. Cart opens as full-screen overlay. |
| Tablet | 744–1128px | Two-column product grid. Hero split preserved with reduced padding. Ingredient headline at 56px. Nav product links visible; cart and account render icon-only. Trust badge strip spans full width without scroll. |
| Desktop | 1128–1440px | Three-column product grid. Full nav with all text links visible. Hero 50/50 split at `{spacing.section}` vertical padding. Ingredient spotlight at full 72px headline. Footer four-column grid. |
| Wide | > 1440px | Container max-width 1440px centered on viewport. Ingredient spotlight and trust-strip sections bleed full edge-to-edge behind a constrained inner content column. Hero and section gutters expand proportionally beyond the spacing scale. |

### Touch Targets

- All interactive controls minimum 44×44px hit area on mobile and tablet.
- Primary and secondary buttons fixed at 48px height across all breakpoints.
- Flavor selector chips maintain minimum 40px height with 8px gaps between chips.
- Nav icons (cart, account, hamburger) use 44×44px hit areas with 24px visual glyph size.
- Sustainability badge chips and trust-strip items are non-interactive — no touch-target requirement applies.

### Collapsing Strategy

- Sustainability badge strip below the nav hides entirely on mobile; individual badges resurface as inline chips embedded within product-description copy sections.
- Footer four-column grid collapses to two-column at tablet, then single-column accordion at mobile where each section expands and collapses independently.
- Subscription step indicator collapses from labeled pill segments to compact numbered step dots on screens narrower than 375px.
- Hero editorial pull-quote (when present) truncates to a single sentence at mobile rather than hiding completely.
- Ingredient spotlight sections adopt scroll-snap behavior on mobile — one section occupies the full viewport height per snap stop; desktop maintains free continuous scroll.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All hex colors are approximations** — live site extraction returned no palette data, likely due to JS-injected design tokens or anti-bot protection. Every hex value in this file derives from widely-observed Bite visual identity across product photography, editorial coverage, and packaging reference — not confirmed DevTools extraction. Verify all values against the live site before shipping.
- **No web font confirmed** — `font-family` stacks (GT Walsheim, Neue Haas Grotesk) are brand-plausible geometric grotesque stand-ins. The actual typeface used at bitestep.com is unconfirmed; a network-tab inspection will reveal the correct font name and foundry.
- **Border-radius values unconfirmed** — `{rounded.full}` CTA pill shape and `{rounded.lg}` card radius are inferred from screenshot analysis; pixel-exact values require DevTools inspection on the live site.
- **No `meta theme-color` detected** — mobile browser chrome color is unspecified; verify `<meta name="theme-color">` in page source.
- **Subscription configurator UI not fully mapped** — the multi-step kit builder and refill cadence selector were unreachable via static analysis. Component specs are inferred from Bite's known subscription model rather than direct observation.
- **Animation and transition tokens absent** — hover-state transitions, scroll-triggered ingredient reveals, and cart drawer slide animations are not captured in this spec.
- **Dark-mode palette undefined** — no dark-mode media query data was extractable; the site may not implement dark mode.
- **Exact spacing values unconfirmed** — section gutters, card inner padding, and grid column gaps use brand-reasonable approximations from the spacing scale rather than measured values.
