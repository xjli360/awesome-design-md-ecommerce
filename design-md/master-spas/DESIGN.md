---
version: alpha
name: "Master Spas"
source_url: "https://www.masterspas.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The meta theme-color #000c29 — a midnight navy so dark it reads as water viewed from depth — announces the brand before a single image loads. Master Spas builds its entire visual system outward from that near-black ocean floor: a graduated ascent through #1d2e38, #2d4156, and #355973 creates a sense of immersion rather than contrast, as though the UI itself is submerged. Against this column of dark blues, the lighter accent tones #a6c4dd and #c2dff7 read as shafts of refracted light rather than mere highlights — a compositional choice that makes the products feel aquatic at a chromatic level, not just a categorical one.

  Two fonts define the typographic character. Termina — a tight, geometric sans with near-equal stroke weights — carries all display and headline work; it reads as precision engineering rather than aspiration, a sensibility that suits a brand selling $10–$100K spa installations. Titillium Web descends for body copy, form labels, and nav links: slightly wider set, open apertures, and a faint technical quality inherited from its original design for broadcast subtitles. Neither font is warm; together they produce the register of premium outdoor equipment rather than lifestyle retail.

  Cards and containers favor measured corners — `{rounded.sm}` at 8px for inputs and tight UI elements, `{rounded.md}` at 12px for product cards, `{rounded.lg}` at 20px for hero callout panels — avoiding both the hard corners of industrial brands and the full-pill softness of consumer wellness. The primary CTA color is #2d4156, the steel-slate blue that occupies the most distinct position in the palette relative to competitors' reds and oranges, paired with white text on dark backgrounds and dark ink on the light-gray canvas tones (#f1f3f5, #e9edf2). Section backgrounds alternate between the near-white surface grays and deep navy panels at #000c29, creating a rhythm of light-dark-light that mirrors the brand's outdoor/evening use context. Dealer-locator CTAs, configurator steps, and spec comparison modules carry most of the interactive weight; these are high-consideration purchase flows, not impulse commerce, so the design allocates generous spacing and structured information hierarchy over promotional urgency.

colors:
  primary: "#2d4156"
  primary-active: "#1d2e38"
  primary-disabled: "#9199a0"
  navy-deep: "#000c29"
  navy-mid: "#355973"
  accent-blue: "#a6c4dd"
  accent-sky: "#c2dff7"
  ink: "#181b1d"
  body: "#33383c"
  muted: "#667481"
  muted-soft: "#9199a0"
  hairline: "#d5dee2"
  hairline-soft: "#e9edf2"
  canvas: "#ffffff"
  surface-soft: "#f1f3f5"
  surface-card: "#e9edf2"
  surface-mid: "#d8e0e6"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-navy: "#ffffff"
  scrim: "#000c29"

typography:
  display-xl:
    fontFamily: "'Termina', 'Arial', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Termina', 'Arial', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Termina', 'Arial', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Termina', 'Arial', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Termina', 'Arial', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Titillium Web', 'Helvetica', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Titillium Web', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Titillium Web', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Titillium Web', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Titillium Web', 'Helvetica', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  overline:
    fontFamily: "'Termina', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.36
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Termina', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Termina', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Titillium Web', 'Helvetica', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "'Termina', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.36
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Termina', 'Arial', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.14
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
    padding: 14px 32px
    height: 50px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 12px 30px
    height: 50px
  button-ghost-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.on-dark}"
    padding: 12px 30px
    height: 50px
  button-cta-navy:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 50px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 40px 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    logoHeight: 40px
    borderBottom: "none"
  nav-bar-scrolled:
    backgroundColor: "{colors.navy-deep}"
    boxShadow: "0 2px 12px rgba(0,12,41,0.4)"
    height: 64px
  nav-dropdown:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    overflow: "hidden"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    subtitleTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
    hoverShadow: "0 8px 32px rgba(45,65,86,0.16)"
  hero-banner:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    minHeight: 620px
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    overlayGradient: "linear-gradient(to right, rgba(0,12,41,0.85) 40%, rgba(0,12,41,0.2) 100%)"
    ctaSpacing: "{spacing.xl}"
  section-dark:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} 0"
  section-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0"
  section-mid:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} 0"
  spec-badge:
    backgroundColor: "{colors.navy-mid}"
    textColor: "{colors.on-dark}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  promo-ribbon:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.navy-deep}"
    typography: "{typography.overline}"
    padding: "6px {spacing.base}"
  feature-icon-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    iconColor: "{colors.primary}"
    iconSize: 40px
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline-soft}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    headerBg: "{colors.primary}"
    headerText: "{colors.on-primary}"
    headerTypography: "{typography.title-sm}"
    rowAltBg: "{colors.surface-soft}"
    cellTypography: "{typography.body-sm}"
    labelTypography: "{typography.spec-label}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
  configurator-step:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    activeAccent: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.hairline}"
    borderActive: "2px solid {colors.primary}"
    padding: "{spacing.xl}"
  dealer-locator-cta:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    inputBg: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.section} {spacing.xxl}"
  testimonial-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    quoteTypography: "{typography.body-md}"
    authorTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.xl}"
    accentBar: "4px solid {colors.accent-blue}"
  footer:
    backgroundColor: "#23272a"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.accent-blue}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.spec-label}"
    padding: "{spacing.section} 0 {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Termina uppercase at 14px/0.8px tracking on a #2d4156 steel-blue fill with 50px height and `{rounded.sm}` corners. Hover darkens to `{colors.primary-active}` (#1d2e38); disabled state uses `{colors.primary-disabled}` (#9199a0) maintaining white text. The uppercase Termina label gives CTAs a technical, engineered character that distances the brand from spa-and-wellness softness.

**`button-secondary`** — Transparent fill with a 2px `{colors.primary}` border and matching text, same height and type as primary. Used for secondary actions like "Learn More" or "View Specs" where the primary CTA is already claimed by a configurator or dealer-locator action.

**`button-ghost-on-dark`** — Matches secondary geometry but renders in white border and white text for placement on the deep navy hero and dark section backgrounds. The outline holds well against both #000c29 and photographic overlays.

**`button-cta-navy`** — A filled #000c29 deep-navy variant for maximum contrast on light-gray surface sections. Used primarily in feature comparison rows and spec callout panels.

### Navigation

**`nav-bar`** — Deep navy #000c29 full-width bar at 72px with the Master Spas wordmark at 40px height. Links use `{typography.nav-link}` in Titillium Web 600 at 15px — slightly lighter than the Termina display stack, readable at speed. Mega-dropdown panels use `{colors.primary}` (#2d4156) background, creating a clear depth step between the nav and page content. On scroll the bar compresses to 64px with a soft shadow.

### Product Cards

**`product-card`** — `{rounded.md}` corners on a `{colors.surface-card}` (#e9edf2) base with a 1px `{colors.hairline}` border. Product image occupies the full card width above the content area. Title uses `{typography.title-md}` in Titillium Web 600; model sub-label in `{typography.body-sm}`. On hover a box-shadow at `rgba(45,65,86,0.16)` lifts the card 8px — the shadow is tinted from `{colors.primary}` to stay within the blue-gray palette rather than reading as a generic gray shadow.

### Hero

**`hero-banner`** — Full-bleed imagery with a directional gradient overlay (`rgba(0,12,41,0.85)` fading right) to ensure legibility of white display text at `{typography.display-xl}` (52px Termina 700). Minimum height 620px on desktop. The overlay opacity keeps outdoor water photography visible on the right while creating a controlled type zone on the left. Primary and ghost-on-dark buttons sit at `{spacing.xl}` gap in a horizontal row beneath the subtitle.

### Spec & Badge Elements

**`spec-badge`** — Compact #355973 pill at `{rounded.xs}` using `{typography.spec-label}` (Termina 11px uppercase). Applied to product cards and configurator steps to surface key specs (jet count, seating, dimensions) without interrupting the visual hierarchy.

**`promo-ribbon`** — `{colors.accent-blue}` (#a6c4dd) background with `{colors.navy-deep}` uppercase text — one of the few places the lighter accent blues appear at scale, creating a soft highlight band that reads as premium rather than promotional.

### Configurator

**`configurator-step`** — Multi-step purchase flow panel on `{colors.surface-card}` with a 2px border that switches from `{colors.hairline}` to `{colors.primary}` when active. Termina headings at `{typography.title-md}` structure each decision (model, color, features, accessories). The active-accent underline and border use `{colors.primary}` consistently, making the user's position in the flow clear without introducing new colors.

### Dealer Locator

**`dealer-locator-cta`** — Full-width `{colors.navy-deep}` panel with white display type and a zip-code input rendered in `{colors.canvas}` — the only white element inside the dark section, functioning as a beacon. The input and submit button sit in a horizontal row at comfortable 48px height. This module appears near the bottom of product pages, closing the consideration loop before exit.

### Footer

**`footer`** — Near-black #23272a base (slightly warmer than `{colors.navy-deep}`) with `{colors.accent-blue}` (#a6c4dd) link treatment and `{typography.spec-label}` column headers in uppercase Termina. Four to five columns: Products, Support, Dealers, Company, Social. The accent-blue links create a consistent thread back to the brand's water-light motif at the darkest layer of the page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero drops to 480px min-height with stacked CTA buttons; nav collapses to hamburger drawer with full-height dark overlay; spec tables scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; hero uses condensed `{typography.display-lg}` (40px); configurator steps stack vertically; dealer-locator input stacks above button |
| Desktop | 1128–1440px | Three-column product grid; full mega-nav dropdown; side-by-side configurator layout; hero at full `{typography.display-xl}` |
| Wide | > 1440px | Max content width capped at 1440px with `{colors.navy-deep}` bleed on dark sections; product grid may extend to four columns for catalog views |

### Touch Targets

- All buttons minimum 50px height on mobile, matching `button-primary` spec
- Nav hamburger icon 44×44px tap target with 8px padding inset
- Spec-badge and promo-ribbon are display-only; no interactive minimum applies
- Configurator step cards expand to full-width on mobile with 20px side padding

### Collapsing Strategy

- Mega-nav collapses to a dark full-height drawer; product category links become accordion items within the drawer
- Feature icon cards shift from 3-up or 4-up grid to a 1-up vertical stack below 744px
- Comparison table hides secondary spec rows behind a "Show all specs" toggle on mobile to prevent horizontal scroll overflow
- Hero overlay gradient adjusts from directional (left-heavy) to a bottom-up gradient on mobile to protect stacked text
- Footer columns collapse from 5-column to a 2-column grid on tablet, then single-column accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed exact hex for the primary CTA button color from live DOM inspection — `#2d4156` is the most distinctive non-neutral in the extracted palette and is used as primary; verify against actual button elements
- Termina font weight range unknown — only 600/700 assumed available; light/thin variants may exist for editorial layouts
- Exact border-radius values not confirmed from computed styles; `{rounded.sm}` (8px) and `{rounded.md}` (12px) are inferred from the brand's mid-premium positioning
- No confirmed pricing display format (starting-at vs. MSRP vs. "request a quote") — `price-display` token defined but usage context unverified
- Animation/transition timing values not extractable from static hints; micro-interactions on configurator steps and card hovers are unspecified
- Icon system style (line vs. filled, stroke weight) not determinable from color/font extraction alone
- Mobile nav behavior (drawer vs. overlay vs. slide) inferred from category; not confirmed from live DOM
