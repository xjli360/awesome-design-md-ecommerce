---
version: alpha
name: "Miele"
source_url: "https://www.mieleusa.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Miele's product photography uses a very specific gray — not warm, not cool — as the default rendering surface for appliance renders, and the extracted site palette confirms that same discipline in the UI: four hex values (#1f1f1f, #343434, #6b6b6b, #ececec), all achromatic, spanning from near-black to light ash with no deviation toward warmth or coolness. Helvetica Neue handles all display type at light-to-regular weight, functioning not as a personality carrier but as a neutral readout — the register a technician expects from an equipment panel rather than a storefront sign. The Miele Icon Font, a fully proprietary glyph set, handles all pictographic communication; its existence signals a design vocabulary thorough enough to have developed its own symbol system rather than licensing from a standard library. Every interactive element holds {rounded.none}: buttons, inputs, product cards, and filter bars all terminate in a hard corner — soft radii would telegraph consumer softness, while zero-radius geometry matches the machined edges of a refrigerator door handle or oven fascia. The primary CTA resolves to {colors.primary} (#1f1f1f), a near-black that avoids the aggression of pure black while maintaining authority; active states shift to {colors.primary-active} (#343434), a delta barely perceptible on screen but present in the system hierarchy. Product cards float on {colors.canvas} white against {colors.surface-soft} backgrounds, delineated by {colors.hairline} (#ececec) rules that mark territory without simulating depth or shadow. Spec tables and comparison grids employ {typography.spec-label} — small, spaced uppercase Helvetica Neue — to label technical attributes, borrowing the visual grammar of equipment datasheets rather than retail marketing copy. {spacing.section} (64px) governs the rhythm between page sections, giving each feature module the breathing room of a showroom floor rather than an e-commerce scroll; the overall posture is horizontal, unhurried, and large-format — each panel aspires to the footprint of a full-bleed photograph of steel and glass.

colors:
  primary: "#1f1f1f"
  primary-active: "#343434"
  primary-disabled: "#6b6b6b"
  ink: "#1f1f1f"
  body: "#343434"
  muted: "#6b6b6b"
  hairline: "#ececec"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-mid: "#ececec"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  spec-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0.1em
    textTransform: uppercase
  product-model:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em

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
    padding: 14px 32px
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 80px
    logoHeight: 28px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageBg: "{colors.surface-soft}"
    border: "none"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    modelTypography: "{typography.product-model}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "{spacing.section} 0"
    ctaVariant: button-ghost
  series-badge:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.ink}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  spec-table:
    backgroundColor: "{colors.canvas}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    textColor: "{colors.ink}"
    rowBorder: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  award-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  feature-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    iconColor: "{colors.primary}"
    iconFont: "'Miele Icon Font'"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    separatorColor: "{colors.hairline}"
  product-filter-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    activeColor: "{colors.primary}"
    activeIndicator: "2px solid {colors.primary}"
    inactiveColor: "{colors.muted}"
    height: 48px
  comparison-table:
    backgroundColor: "{colors.canvas}"
    headerBg: "{colors.surface-mid}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    rowBorder: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.spec-label}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Filled near-black (#1f1f1f) with all-caps, spaced Helvetica Neue at 14px. Zero border radius throughout; the hard corner is consistent with the brand's manufacturing-derived geometry. Hover state deepens to `button-primary-active` (#343434); disabled state uses the mid-gray (#6b6b6b) fill with white text, preserving the shape at reduced contrast. Height is fixed at 48px for consistent touch targets.

**`button-secondary`** — White fill with a 1px `{colors.primary}` border and matching text, producing an outlined sibling to the primary. Same typographic treatment, same 48px height. On dark backgrounds the `button-ghost` variant flips to a white border-and-text outline on transparent, used in hero and dark-section contexts.

### Text Input

**`text-input`** — Square-cornered (`{rounded.none}`) with a `{colors.hairline}` border at rest, upgrading to a `{colors.ink}` border on focus. No inner shadow, no fill tint — the input sits flush with the page surface and signals state through border weight alone. Placeholder text uses `{colors.muted}` (#6b6b6b); label copy uses `{typography.spec-label}` to maintain the datasheet register.

### Navigation

**`nav-bar`** — 80px tall, white background with a single 1px `{colors.hairline}` bottom rule. The Miele wordmark sits at 28px height, left-aligned. Navigation links use `{typography.nav-link}` (14px regular Helvetica Neue), spaced horizontally. No dropdown mega-menu background tints — sub-menus extend the white canvas. Icons use the Miele Icon Font exclusively.

### Product Card

**`product-card`** — No border, no shadow. The product image renders on a `{colors.surface-soft}` (#f7f7f7) tile; the copy zone below sits on `{colors.surface-card}` white. Model names are set in `{typography.product-model}` (13px, wide tracking), acting as a part number rather than a marketing headline. Series badges (`series-badge`) appear inline above the model name as a `{colors.surface-mid}` chip with `{typography.spec-label}` uppercase text.

### Hero

**`hero`** — Full-width, `{colors.primary}` (#1f1f1f) background with `{colors.on-primary}` white type. Display headline uses `{typography.display-xl}` (48px, weight 300) — the light weight prevents the dark surface from feeling heavy. CTAs on the hero use `button-ghost` (white outlined) to maintain the monochromatic discipline. Minimum height 560px; padding `{spacing.section}` top and bottom.

### Spec Table

**`spec-table`** — Row-based, with labels in `{typography.spec-label}` (11px spaced uppercase, `{colors.muted}`) and values in `{typography.body-sm}` (`{colors.ink}`). Each row separated by a 1px `{colors.hairline}` rule. No zebra striping, no cell background fills — legibility comes from vertical rhythm alone. Used on product detail pages for technical specifications: capacity, dimensions, energy class, noise level.

### Comparison Table

**`comparison-table`** — Multi-column grid with a `{colors.surface-mid}` header row for model names and a white body. Labels in `{typography.spec-label}`, values in `{typography.body-sm}`. Row borders use `{colors.hairline}`. Sticky first-column behavior expected; all corners `{rounded.none}`.

### Feature Tile

**`feature-tile`** — `{colors.surface-soft}` background tile with no border. Icon from the Miele Icon Font renders in `{colors.primary}` at 32–40px. Title in `{typography.title-md}`, supporting copy in `{typography.body-sm}`. Tiles sit in a 3- or 4-column grid with consistent `{spacing.xl}` internal padding and no separating gutters — the background fill creates the grid cadence.

### Award Badge

**`award-badge`** — Small, filled `{colors.primary}` chip with white `{typography.caption}` text, no radius. Used to call out design awards, test-winner designations, and energy ratings. Appears overlaid on product card images or adjacent to model names.

### Product Filter Bar

**`product-filter-bar`** — Horizontal tab row at 48px height on a white background with a `{colors.hairline}` underline. Active filter uses a 2px `{colors.primary}` bottom indicator and `{colors.ink}` text; inactive tabs use `{colors.muted}`. Typography is `{typography.body-sm}`. No pill or chip shaping — tabs are flush text with a line indicator only.

### Footer

**`footer`** — Full-width `{colors.primary}` (#1f1f1f) background. Column headings in `{typography.spec-label}` (uppercase, spaced), links in `{typography.body-sm}`. All text `{colors.on-primary}` white. `{spacing.xxl}` (48px) vertical padding. The footer's black-on-black visual weight bookends the page, matching the hero's dark register and signaling that the brand's primary color is structural, not merely promotional.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces horizontal link row; hero headline drops to `{typography.display-sm}` (24px); spec tables scroll horizontally; filter bar scrolls horizontally with no line wrap |
| Tablet | 744–1128px | Two-column product grid; nav may use condensed horizontal row or hamburger depending on link count; hero at `{typography.display-md}` (32px); feature tiles in 2-column grid |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav bar at 80px; hero at full `{typography.display-xl}` (48px); feature tiles in 3-column grid; comparison table fully visible |
| Wide | > 1440px | Max-width container (~1440px) centered; hero background bleeds full width while content observes gutter; product grid expands to 4 columns; spec tables remain content-width |

### Touch Targets

- All buttons minimum 48px height
- Filter bar tabs minimum 48px height, adequate horizontal padding for tap zone
- Nav links on mobile minimum 44px touch target height in stacked mobile menu
- Product cards full-surface tappable, not limited to title or image zones

### Collapsing Strategy

- Navigation collapses to hamburger icon (Miele Icon Font glyph) below 744px; drawer slides from left on `{colors.canvas}` white
- Spec tables and comparison tables switch to horizontal scroll containers on mobile rather than stacking rows
- Hero CTA buttons stack vertically with `{spacing.sm}` gap on mobile
- Feature tile grid collapses: 4-col → 2-col → 1-col at successive breakpoints
- Footer column grid collapses to 1-column accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only 4 hex colors extracted, all achromatic — Miele's documented brand red (used in logo and select accent treatments, circa #bb0a1e) did not appear in the crawl; no accent or highlight color is confirmed for this system
- `{colors.canvas}` (#ffffff) and `{colors.surface-soft}` (#f7f7f7) are reasonable derivations from the white-ground convention but were not directly extracted
- Font weights for Helvetica Neue not confirmed beyond what the typeface natively provides (300, 400, 500, 700); medium (500) used as a stand-in for semi-bold display needs
- No price typography or promotional pricing treatment captured
- No color confirmed for interactive states beyond the two extracted darks; error, success, and warning states (form validation, dealer locator) are entirely unconfirmed
- Animation and transition values (drawer timing, hover transitions, image carousel behavior) not extractable from static crawl
- Mobile navigation pattern (drawer vs. bottom sheet vs. condensed bar) not confirmed
- Miele Icon Font glyph set and sizing conventions not mapped; only its existence is confirmed
