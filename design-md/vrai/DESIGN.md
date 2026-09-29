---
version: alpha
name: "Vrai"
source_url: "https://www.vrai.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Vrai measures purity in two registers at once: the optical grade of a lab-grown diamond and the zero-emission record of the foundry that grew it. That dual accounting shapes the entire visual system. The canvas drifts warm at #faf9f7 rather than stark white, the ink sits at #241f20 — near-black with a barely perceptible brown undertone, geological rather than digital — and the single voltage color is #009161, a medium green that appears nowhere decoratively: it surfaces on sustainability certifications, zero-emission copy, and the most direct environmental CTAs. Its restraint is the point. Every other hue in the extracted palette is desaturated: warm sage (#d0d9c8), dusty teal (#54787c), champagne (#f5eecc), and a barely-there mint wash (#ebf9f4) behind proof-of-sustainability callouts. The system reads more like a mineral sample card than a luxury advertisement.

  Navigation is architectural — flat horizontal bands, near-zero ornamentation, no rounded heroes. Product photography carries the full emotional weight: rings float on pale cream grounds with shadow minimized, stone geometry doing all the persuasion. The product card uses {rounded.none} with a 1px hairline in #e5e5e5, keeping the container nearly invisible so the stone appears free-floating on the surface.

  Primary CTA buttons carry #009161 against off-white — a combination that reads closer to a certification label than a luxury impulse trigger. This is intentional: Vrai's customer is researching an ethical high-consideration purchase across multiple sessions, not impulse-buying. The button typography is uppercase, tracked wide, and set at a modest 13px, which keeps the action surface quiet enough that the photography remains dominant. A secondary outlined variant uses the near-black ink border, again at {rounded.none}, maintaining the flat-panel aesthetic throughout checkout.

  The ring configurator — Vrai's centrepiece product experience — deploys a dense grid of cut, carat, and metal selectors. Metal swatches render as {rounded.full} circles in gold (#c8ab6e), white, and rose variants against the warm canvas. A side panel tracks live price in {typography.price-display} with component breakdowns in {typography.caption}. The warm gold accent (#c8ab6e) appears exclusively on metal UI affordances, never as a brand decoration, which preserves its meaning as a material signal rather than a brand color. The extracted font stack is entirely system fallbacks; Vrai's live headings carry a geometric humanist face that was not captured and is flagged below.

colors:
  primary: "#009161"
  primary-active: "#007a52"
  primary-disabled: "#d0d9c8"
  ink: "#241f20"
  body: "#3c3c3b"
  muted: "#737368"
  muted-soft: "#9ca3af"
  hairline: "#e5e5e5"
  hairline-soft: "#eaeaea"
  canvas: "#faf9f7"
  surface-soft: "#f7f7f7"
  surface-card: "#f1f1f1"
  on-primary: "#f7f7f7"
  accent-gold: "#c8ab6e"
  accent-cream: "#f5eecc"
  accent-sage: "#d0d9c8"
  accent-teal: "#54787c"
  accent-teal-light: "#719093"
  accent-mint: "#ebf9f4"
  error: "#e54141"
  error-dark: "#9f1d1d"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: 0.02em
  display-md:
    fontFamily: "'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0.01em
  display-sm:
    fontFamily: "'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.01em
  title-sm:
    fontFamily: "'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.04em
  price-display:
    fontFamily: "'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  label-uppercase:
    fontFamily: "'Helvetica Neue', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.14em
    textTransform: uppercase

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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.base}"
    height: 48px
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoAreaWidth: 120px
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "4/5"
    imageBackground: "{colors.surface-card}"
    padding: "{spacing.base}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-caption:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
    maxWidth: 640px
    ctaSpacingTop: "{spacing.xl}"
  sustainability-badge:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: "{spacing.xs} {spacing.sm}"
    iconColor: "{colors.primary}"
  metal-swatch:
    shape: "{rounded.full}"
    size: 28px
    borderDefault: "2px solid transparent"
    borderSelected: "2px solid {colors.ink}"
    backgroundColor_gold: "{colors.accent-gold}"
    backgroundColor_white: "#e8e8e8"
    backgroundColor_rose: "#d4a090"
    gap: "{spacing.sm}"
  configurator-panel:
    backgroundColor: "{colors.canvas}"
    borderLeft: "1px solid {colors.hairline}"
    width: 368px
    padding: "{spacing.xl}"
    priceTypography: "{typography.price-display}"
    labelTypography: "{typography.caption}"
    sectionLabelTypography: "{typography.label-uppercase}"
    textColor: "{colors.ink}"
  diamond-grade-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
    border: "1px solid {colors.hairline}"
  collection-filter-pill:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xs} {spacing.base}"
  collection-filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  certification-strip:
    backgroundColor: "{colors.accent-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.primary}"
    padding: "{spacing.md} {spacing.base}"
    textAlign: center
    borderBottom: "1px solid {colors.hairline-soft}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.xl}"
    linkColor: "{colors.surface-soft}"
    linkHoverColor: "{colors.canvas}"
  diamond-cut-selector:
    backgroundColor: "{colors.surface-soft}"
    selectedBackground: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
    imageSize: 48px

## Components

### Buttons

**`button-primary`** — Flat rectangle, no border-radius, #009161 fill with #f7f7f7 text in uppercase 13px tracked at 0.1em. Height 48px, padding 14px 32px. On hover, transitions to `primary-active` (#007a52); disabled state drops to the sage tone #d0d9c8 with muted text and `not-allowed` cursor. Used exclusively for high-intent actions: "Add to Cart", "Begin Customizing", sustainability-linked CTAs.

**`button-secondary`** — Transparent fill, 1px solid #241f20 border, same uppercase typography as primary. Mirrors the primary height and tracking exactly so the two sit side-by-side without visual imbalance. On hover, fill inverts to #241f20 with #faf9f7 text. Used for secondary actions like "Learn More About Origin", "View All Settings".

**`button-ghost`** — No border, no background, underline decoration. Used for text-level navigation links within editorial copy and for "dismiss" interactions in overlays.

### Text Inputs

**`text-input`** — Zero border-radius, 1px hairline border in #e5e5e5 at rest, transitions to 1px solid #241f20 on focus. Height 48px. Placeholder text in #9ca3af. Used across ring-search, email capture, and contact forms. Label sits above the field in `{typography.label-uppercase}` style, never floating inside.

### Navigation

**`nav-bar`** — 64px tall, warm #faf9f7 fill with a 1px soft hairline (#eaeaea) bottom border. Logo left-anchored at ~120px wide. Center links in 13px/0.04em tracked nav-link style. Right cluster holds search, account, and cart icons at 20px, no labels. On scroll past 40px the bar gains a subtle drop shadow without changing color.

### Product Cards

**`product-card`** — Fully flat, 1px #e5e5e5 border, 4:5 image ratio on a #f1f1f1 image ground. Title in `title-md`, price in `price-display` (weight 300, 24px), secondary descriptor line in `caption`/`muted`. No hover scale — instead the image ground lightens to #f7f7f7 on hover to suggest selection without motion.

### Configurator

**`configurator-panel`** — Fixed-right side panel, 368px, 1px left border, warm canvas fill. Live price updates in `price-display` with breakdown lines in `caption`. Cut selector grid uses `diamond-cut-selector` tiles in a 3–4 column responsive grid. Metal swatches use `metal-swatch` 28px circles with a 2px selected ring in #241f20. Carat and diamond-grade options render as flat tile buttons mirroring `diamond-grade-badge` styling.

### Sustainability Badges

**`sustainability-badge`** — #ebf9f4 mint background, 1px solid #009161 border, uppercase 10px label in #009161. Appears on PDP headers and configurator panel above the price. The sole location where primary green appears as a container fill — keeping it highly legible as a certification signal rather than a decorative element.

### Certification Strip

**`certification-strip`** — Full-width warm cream (#f5eecc) horizontal band, center-aligned `body-sm` text with a small #009161 icon prefix. Appears immediately below nav on the homepage and PDP, stating zero-emission provenance. One of very few places where `accent-cream` is used as a background at full bleed.

### Footer

**`footer`** — Near-black #241f20 fill. Four-column link grid at desktop in `caption` style on #f7f7f7 text. Column headers in `title-sm` uppercase. Bottom row carries legal copy in `caption`/`muted-soft` approximation. The dark footer anchors the page against the near-white canvas system — the only true dark surface in the layout.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; configurator panel converts to full-screen bottom sheet; nav collapses to hamburger + logo + cart; hero text drops to `display-sm`; metal swatches increase tap target to 36px |
| Tablet | 744–1128px | Two-column product grid; configurator panel sits below product image in stacked layout; nav shows top-level categories inline, sub-nav via dropdown |
| Desktop | 1128–1440px | Three-column product grid; configurator panel fixed-right at 368px beside product image; full nav visible; certification strip remains full-bleed |
| Wide | > 1440px | Max content width 1440px centered; grid gains fourth column; hero image bleeds full viewport width with text overlaid on left half |

### Touch Targets

- Metal swatches: minimum 36×36px on mobile (base size 28px, tap area padded)
- All nav icons: 44×44px touch target with visual icon at 20px
- Diamond cut selector tiles: minimum 60×60px on mobile
- Filter pills: minimum 36px height on mobile with 12px horizontal padding

### Collapsing Strategy

- Configurator panel collapses from fixed-right to a bottom sheet triggered by a persistent sticky bar showing current price and a "Customize" CTA
- Category nav collapses to a horizontal scrollable chip row below the main nav bar on tablet
- Certification strip collapses to a single marquee line on mobile to preserve vertical space
- Footer columns collapse to a single accordion stack on mobile with `title-sm` headings as toggles

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom typeface was captured in extraction — only system font fallbacks (-apple-system, Helvetica Neue, Roboto). Vrai's live headings appear to use a geometric humanist sans that is loaded via JavaScript and was not present in the static font-family declarations. All typography tokens above use system fallbacks and will not replicate the exact heading character.
- Specific interactive animation curves (ring-spin on configurator, image crossfade on cut selection) were not extractable from static analysis.
- Exact modal/overlay backdrop opacity and blur values not confirmed — `surface-card` used as approximation for overlay grounds.
- Dark mode support status unknown; only light-mode tokens are defined here.
- Hover transition durations not captured; assumed 150–200ms ease-out based on category norms.
- The extracted red tones (#e54141, #9f1d1d, #d0021b) appear in error/validation states only; no marketing use confirmed for red.
