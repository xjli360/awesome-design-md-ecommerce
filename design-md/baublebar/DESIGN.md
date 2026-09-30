---
version: alpha
name: "BaubleBar"
source_url: "https://www.baublebar.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  BaubleBar doesn't open with jewelry photography — it opens with drop rhythm. Collections arrive with the urgency of a fashion release: countdown timers, "JUST DROPPED" chips, and limited-run charm sets that signal a brand meant to be checked weekly, not only at gift-giving season. The visual system supports that cadence with a high-contrast near-black (`#0b0b0b`) ink-on-white grid that never competes with product color — charm bracelets in sherbet hues, beaded sets in gradient lavender, and layered chains in plated gold all pop against restrained chrome. The type pairing is the sharpest design decision: Utopia Std — an Adobe optical-size serif with old-style figures and ink-trap construction — handles all editorial display work, sitting in deliberate counterpoint with Mulish, a humanist geometric sans that runs the UI chrome, product labels, and CTA copy. Utopia Std lends the authority of a printed catalog; Mulish keeps the interface fast and legible at 11–13px. Buttons run uppercase with tracked letter-spacing in Mulish at 14px/700 — clipped and directive rather than conversational. The primary CTA is coral `#f94c43`, landing on add-to-cart buttons and sale price reductions. A golden amber `#f6a429` marks personalization entry points and gifting callouts — warm and celebratory without alarm. Teal `#009879` functions as a tertiary accent for confirmations and filter selections. All supporting tones are a deliberate grayscale: `#0b0b0b` for ink, `#6d7175` for secondary copy, `#dedede` for hairlines, `#f1f1f1` for surface fills. Geometry is almost universally square-cornered (`{rounded.none}`) — the editorial grid holds hard — with `{rounded.full}` reserved as a pointed exception for color swatch pickers and social icon circles. Personalization panels ease to `{rounded.sm}`, softened just enough to signal interactivity. `{spacing.section}` padding on hero blocks gives Utopia headlines typographic room to land.

colors:
  primary: "#f94c43"
  primary-active: "#d93028"
  primary-disabled: "#fcc4c1"
  secondary: "#f6a429"
  accent-teal: "#009879"
  ink: "#0b0b0b"
  body: "#202223"
  muted: "#6d7175"
  muted-soft: "#939393"
  hairline: "#dedede"
  hairline-soft: "#e7e7e7"
  canvas: "#ffffff"
  surface-soft: "#efefef"
  surface-card: "#f1f1f1"
  cool-gray: "#c5c8d1"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'utopia-std-headline', 'utopia-std', Georgia, serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'utopia-std-headline', 'utopia-std', Georgia, serif"
    fontSize: 38px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'utopia-std', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'utopia-std', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Mulish, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Mulish, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Mulish, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Mulish, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  price:
    fontFamily: "Mulish, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-strike:
    fontFamily: "Mulish, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
    textDecoration: line-through
  caption:
    fontFamily: "Mulish, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.4px
  badge:
    fontFamily: "Mulish, sans-serif"
    fontSize: 10px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  label-sm:
    fontFamily: "Mulish, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "Mulish, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "Mulish, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "Mulish, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  announcement:
    fontFamily: "Mulish, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px

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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.announcement}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    imageAspectRatio: "1 / 1"
    imageRounded: "{rounded.none}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    strikePriceTypography: "{typography.price-strike}"
    strikePriceColor: "{colors.muted}"
    salePriceColor: "{colors.primary}"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    padding: "{spacing.section}"
    minHeight: 480px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 7px"
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 7px"
  badge-personalize:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 7px"
  badge-gift:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 7px"
  swatch-picker:
    size: 24px
    gap: "{spacing.xs}"
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.ink}"
    selectedOffset: 2px
  personalization-panel:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.label-sm}"
    labelColor: "{colors.muted}"
    inputTypography: "{typography.body-md}"
  charm-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    selectedBorder: "2px solid {colors.primary}"
    unselectedBorder: "1px solid {colors.hairline}"
    labelTypography: "{typography.caption}"
    padding: "{spacing.sm}"
  gift-callout:
    backgroundColor: "{colors.surface-card}"
    borderLeft: "3px solid {colors.secondary}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.none}"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.ink}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    padding: "8px 16px"
  collection-grid:
    columns: 4
    gap: "{spacing.base}"
    tabletColumns: 3
    mobileColumns: 2
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.cool-gray}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons
**`button-primary`** — Solid coral `#f94c43` fill with all-caps Mulish at 14px/700 and 1px letter-spacing, square corners (`{rounded.none}`), 48px tall. Hover deepens to `#d93028`; disabled washes to `#fcc4c1` at reduced opacity. Used exclusively for add-to-cart, checkout progression, and primary modal confirmation actions.

**`button-secondary`** — White fill with a 1px `{colors.ink}` border; same uppercase Mulish type and 48px height as primary. Acts as the outlined counterpoint on hero and collection pages where the coral primary would compete with product imagery.

**`button-tertiary`** — Transparent background with underlined Mulish body text; no border, no fill. Used for secondary actions like "View Full Details" and "Learn More" where the page already carries a primary CTA.

### Text Input
**`text-input`** — Square-edged, 48px tall, 1px `{colors.hairline}` border that snaps to `{colors.ink}` on focus. Placeholder runs in `{colors.muted}` (`#6d7175`). Found across search, personalization name fields, and gift-message boxes. No border-radius — the form fields match the editorial grid's hard geometry.

### Navigation
**`nav-bar`** — White canvas, 64px tall, bottom hairline divider. Nav links run in Mulish 13px/700 with slight tracking. The announcement bar sits above it: full-width `#0b0b0b` strip with reversed white type at 12px/600, rotating shipping and promotion messages at 36px height.

### Product Card
**`product-card`** — Square image crop with no corner radius, name in Mulish 14px/400 below, price in Mulish 15px/700. Sale price renders in coral `{colors.primary}` alongside a struck-through original price in `{colors.muted}`. Badges (`badge-sale`, `badge-new`, `badge-personalize`) float top-left in the image frame. Swatch pickers render below the title as 24px filled circles with a 2px `{colors.ink}` ring on selection.

### Hero Banner
**`hero-banner`** — Full-bleed section with Utopia Std Headline at 52px/400 for the primary display line, which can wrap to two lines on tablet. Subtitle in Mulish 16px/400 with generous line-height. CTA buttons sit inline or stacked below copy. Background alternates between `{colors.surface-soft}` (`#efefef`) and full-bleed product imagery. Minimum 480px height preserves type breathing room.

### Badges
**`badge-sale`** — Coral `#f94c43` block, all-caps 10px/800 Mulish, 0.6px tracking, no radius. Placed top-left of product image tiles and inline beside sale prices. **`badge-new`** — Same dimensions in `#0b0b0b` with white type. **`badge-personalize`** — Amber `#f6a429` fill with dark `{colors.ink}` text for contrast, signals a customizable item. **`badge-gift`** — Teal `#009879` fill for gift-set or bundled-gifting products.

### Personalization Panel
**`personalization-panel`** — Light `{colors.surface-card}` background, 1px hairline border, `{rounded.sm}` softening. Section label in 11px/700 uppercase Mulish with `{colors.muted}` color, input fields below in body-md. Used for name engravings, monograms, and charm selections on PDP. The `charm-selector` component lives inside: a grid of square tiles with a 1px hairline default border and 2px coral border on selection.

### Gift Callout
**`gift-callout`** — Surface-card background with a 3px amber left border (`{colors.secondary}`), body-sm Mulish copy, 16px horizontal padding. Appears on PDP and cart to surface gift-messaging, free-gift-wrap thresholds, and gifting add-ons.

### Filter Pills
**`filter-pill`** — Rounded-full pill outline at 1px hairline, body-sm uppercase Mulish, 8px/16px padding. Active state inverts: `{colors.ink}` fill with white text. Used on collection pages for material, color, price, and occasion filters.

### Footer
**`footer`** — Full-width `#0b0b0b` block with reversed type. Section headings in Mulish 15px/700 white; body links in `{colors.cool-gray}` (`#c5c8d1`) that brighten to white on hover. Social icons in `{rounded.full}` circles. Email capture input sits inline with a white outlined submit button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav drawer; hero type scales to display-md (28px); announcement bar wraps to two lines at 44px height; personalization panels go full-width |
| Tablet | 744–1128px | Three-column product grid; nav collapses category flyouts into horizontal scroll row; hero type at display-lg (38px); filter pills scroll horizontally below search |
| Desktop | 1128–1440px | Four-column product grid; full mega-nav with category columns and featured imagery; hero at display-xl (52px); filter sidebar on collection pages |
| Wide | > 1440px | Content max-width 1400px centered; hero sections remain full-bleed behind padded content container; product grid stays at four columns with larger gap |

### Touch Targets
- All buttons minimum 48px tall, matching `text-input` height for consistency
- Swatch pickers expand hit area to 40px × 40px with 8px invisible padding around the 24px visible circle
- Filter pills minimum 40px tall on mobile
- Nav drawer links minimum 52px tall for thumb reachability

### Collapsing Strategy
- Mega-nav collapses to hamburger drawer at < 1128px; drawer slides from left with category accordion
- Collection page filter sidebar converts to a bottom-sheet modal on mobile and tablet
- Personalization panel stacks vertically on mobile, two-column on tablet and above
- Hero CTA buttons stack vertically at < 480px viewport width
- Footer columns collapse from four to two on tablet, single-column on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No explicit brand primary color confirmed from Shopify storefront CSS — `#f94c43` coral inferred as the CTA primary from the extracted palette; actual brand-defined primary may differ
- Exact Utopia Std optical-size variant (Text vs. Display vs. Headline) per breakpoint not confirmed; display-xl and display-lg assigned `utopia-std-headline` by inference from font-family stack ordering
- Mulish weight usage (600 vs. 700 vs. 800) per label type not directly measured; assignments reflect standard hierarchy conventions
- Spacing scale values are standard 8pt-grid assumptions — no design token file was accessible to confirm BaubleBar's internal spacing system
- Animation and transition values (hover timing, drawer slide, carousel easing) not extractable from static hints
- Dark-mode or alternate theme presence not confirmed
- Exact mega-nav flyout structure and featured image slot dimensions not captured
