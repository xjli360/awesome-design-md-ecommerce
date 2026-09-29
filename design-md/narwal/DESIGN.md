---
version: alpha
name: "Narwal"
source_url: "https://www.narwal.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The overhead shot — robot exactly at frame center, floor stretching edge-to-edge, no human in frame, no lifestyle set-dressing — is Narwal's single most distinctive design decision. The machine is the protagonist; the floor is the proof. That confidence in hardware specificity carries into the color system: a saturated teal near #0CBECE operates not as warmth or approachability but as instrumentation — the color of LIDAR returns, progress arcs in companion-app UI, and the radial coverage maps that animate across hero sections on deep navy (#0D1729) backgrounds. Against near-black ink (#111827) and a surface hierarchy that moves from hero-canvas through surface-soft to surface-card, this teal does all the chromatic work; the rest of the palette is cool gray and white, giving the system an economy unusual in consumer hardware. Type runs a compact geometric sans-serif tight at display sizes — letterSpacing near −0.5px on headlines at weight 700 — then relaxes to 400 weight at comfortable line heights for body copy without ever softening into editorial warmth. The station — the self-cleaning, self-emptying dock that anchors every product — appears in a recurring cutaway diagram treatment: line-art on dark backgrounds, glowing teal callouts rendered in caption-scale type, an aesthetic that borrows from engineering documentation rather than consumer lifestyle catalogs. Rounding is controlled: product cards sit at {rounded.md}, primary CTAs at {rounded.sm}, and pill badges at {rounded.full} — the geometry never reaches the softness of a wellness brand. Section spacing is generous at {spacing.section}, with a predictable mobile collapse that preserves the overhead product anchor while stacking spec content into accordions. The result communicates premium consumer hardware that would rather show a floor map than a family scene.

colors:
  primary: "#0CBECE"
  primary-active: "#09A8B7"
  primary-disabled: "#9DDDE4"
  ink: "#111827"
  body: "#374151"
  muted: "#6B7280"
  hairline: "#E5E7EB"
  hairline-dark: "#374151"
  canvas: "#FFFFFF"
  surface-soft: "#F9FAFB"
  surface-card: "#FFFFFF"
  hero-canvas: "#0D1729"
  hero-surface: "#162035"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  teal-soft: "#E0F9FB"
  coverage-glow: "rgba(12,190,206,0.20)"

typography:
  display-xl:
    fontFamily: "'DIN Next LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'DIN Next LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'DIN Next LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'DIN Next LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'DIN Next LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'DIN Next LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'DIN Next LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DIN Next LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'DIN Next LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'DIN Next LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'DIN Next LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  spec-label:
    fontFamily: "'DIN Next LT Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.hero-canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    captionColor: "{colors.muted}"
    typography: "{typography.title-md}"
    descTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  hero-banner:
    backgroundColor: "{colors.hero-canvas}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaColor: "{colors.primary}"
    padding: "{spacing.section} 0"
  station-diagram:
    backgroundColor: "{colors.hero-surface}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    calloutTypography: "{typography.caption}"
    labelTypography: "{typography.spec-label}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  coverage-badge:
    backgroundColor: "{colors.teal-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  spec-row:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    textColor: "{colors.ink}"
    mutedColor: "{colors.muted}"
    padding: "{spacing.md} {spacing.base}"
  comparison-chip:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    activeAccent: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  product-tag:
    backgroundColor: "{colors.hero-surface}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px

## Components

### Buttons

**`button-primary`** — Teal fill (`#0CBECE`) with white label at 15px/600 weight, 8px radius, 48px tall. Active state darkens to `#09A8B7`; disabled washes to `#9DDDE4`. This is the sole purchase CTA across both dark hero and light product sections — teal on dark canvas and teal on white are both in active use.

**`button-secondary`** — White fill with `{colors.hairline}` border and `{colors.ink}` label, dimensions matching `button-primary`. Appears alongside the primary CTA for "Learn More" or "Compare" actions; on dark hero sections the border reads against `{colors.hero-canvas}` at sufficient contrast.

**`button-ghost`** — Transparent background with `{colors.primary}` teal label, no visible border. Used for in-page navigation links, "See All Specs" calls-to-action inside spec tables, and secondary anchors within feature callout rows. Inherits `{typography.button-md}` tracking.

### Nav Bar

**`nav-bar`** — 64px tall, white canvas with a 1px `{colors.hairline}` bottom rule, `{typography.nav-link}` at 14px/500 for product category links. Swaps to `nav-bar-dark` (deep navy `#0D1729`, no bottom border) when overlaid on the full-bleed hero section. Logo is left-anchored; product links center; cart, account, and locale icons right.

### Product Card

**`product-card`** — White surface at `{rounded.md}` with `{colors.hairline}` border and `{spacing.lg}` internal padding. Model name in `{typography.title-md}`, short descriptor in `{typography.body-sm}/{colors.body}`, price in `{typography.display-sm}/{colors.ink}`. Overhead product shot fills the top two-thirds of the card at full bleed. Hover lifts a soft box-shadow without border-color mutation.

### Hero Banner

**`hero-banner`** — Full-bleed `{colors.hero-canvas}` section, white headline at `{typography.display-xl}`, body copy at `{typography.body-md}`. Primary CTA button follows directly. On desktop the product sits in a right column as a large overhead or 45-degree render; on mobile it stacks above the text block. `{spacing.section}` padding top and bottom provides breathing room against adjacent light sections.

### Station Diagram

**`station-diagram`** — The brand's signature component: a `{colors.hero-surface}` dark container at `{rounded.md}` housing a cutaway line-art render of the self-cleaning dock. Callout leader lines terminate in `{colors.primary}` teal dots; feature labels ("Auto-Refill", "Self-Empty", "Hot-Air Drying") render in `{typography.spec-label}` uppercase with `{typography.caption}` descriptor lines. This diagram appears on every product page and functions as the primary technical differentiator surface — it makes the internal mechanism legible without photography.

### Coverage Badge

**`coverage-badge`** — Pill-shaped (`{rounded.full}`) badge in soft teal (`{colors.teal-soft}`) with `{colors.primary-active}` uppercase label at 11px/600. Surfaces key quantitative capabilities ("5500 sq ft Coverage", "LIDAR Mapping", "AI-Powered Obstacle Avoidance") inline within product cards and as subheads in hero sections. Never used as a navigational element.

### Spec Row

**`spec-row`** — Specification table unit with alternating `{colors.surface-soft}` and white rows divided by `{colors.hairline}` rules. Left column is the spec label in `{typography.spec-label}` uppercase muted treatment; right column is the value in `{typography.body-sm}/{colors.ink}`. Padding `{spacing.md}` vertical × `{spacing.base}` horizontal. On mobile the table collapses into a full-width accordion.

### Comparison Chip

**`comparison-chip`** — Compact card used in the horizontal "Which Narwal is Right for You" decision rail. White surface, `{colors.hairline}` border at `{rounded.sm}`; selected state draws a 2px `{colors.primary}` inset border. Typography `{typography.body-sm}`. Minimum 44px tall for touch. Chips scroll horizontally on mobile with scroll-snap.

### Product Tag

**`product-tag`** — Small rectangular label (`{rounded.xs}`) with `{colors.hero-surface}` background and `{colors.primary}` teal text in `{typography.badge}` uppercase. Applied to product imagery and listing cards to mark tier and line ("Freo X Ultra", "Freo Z Ultra Combo"). Not interactive; purely informational.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero stacks product image above headline at ~32px display size; nav collapses to hamburger + cart icon; station-diagram callout lines collapse to numbered legend below image; spec-rows become full-width accordion panels; comparison rail scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; hero goes side-by-side with display-xl scaled to ~40px; nav shows primary product categories, secondary links behind overflow menu; station-diagram at reduced scale with callouts visible |
| Desktop | 1128–1440px | Three-column product grid; full hero with overhead render right-anchored; station-diagram at full callout render; nav-bar shows complete link set; spec rows side-by-side in two-column layout |
| Wide | > 1440px | Max content width ~1400px centered; hero background canvas bleeds full viewport width; product grid stays three-column with wider column gutters; station-diagram can expand to wider viewport proportion |

### Touch Targets

- All interactive elements minimum 44 × 44px on mobile
- Nav icons (cart, hamburger) padded to 48 × 48px tap area
- `coverage-badge` when linked padded to minimum 36px height
- `comparison-chip` minimum 44px height within horizontal scroll rail
- `spec-row` accordion toggle area minimum 48px tall on mobile

### Collapsing Strategy

- Three-column product grid collapses to two-column at tablet, single-column at mobile
- Station-diagram callout overlay converts to numbered callout list beneath the image below 744px
- Horizontal comparison chip rail stays horizontal at all breakpoints with scroll-snap; does not stack
- Hero display text scales: 56px → 40px at tablet → 32px at mobile via breakpoint overrides or `clamp()`
- Footer link columns (four-column desktop) collapse to two-column at tablet, single accordion group per category at mobile
- Spec table converts from two-column side-by-side layout to full-width accordion at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the site likely loads design tokens via JavaScript or sits behind anti-bot protection; all color values in this file are inferred from widely-observed brand materials (product pages, press imagery, app store screenshots) and must be verified against live CSS before production use.
- **Exact primary teal value unconfirmed** — `#0CBECE` is an approximation; the live value may be closer to `#00B5CC`, `#12B8CA`, or another nearby hue. Verify against the site's CSS custom properties or Figma source.
- **No font families extracted** — `DIN Next LT Pro` is inferred from visual inspection of brand collateral; Narwal may use a licensed geometric sans-serif, a custom typeface, or a system font stack. Inspect the live site's `@font-face` declarations to confirm.
- **Dark/light mode split logic unconfirmed** — the brand uses both deep-navy hero sections and white product sections; the exact scroll or page-level rule governing when `nav-bar-dark` vs `nav-bar` applies was not confirmed from live extraction.
- **Motion and animation tokens absent** — coverage-map radial animations, station-diagram entry reveals, and product-image scroll parallax are visible on the live site but timing curves and durations are not specced here.
- **Icon system inventory missing** — Narwal uses a custom icon set for feature callouts (suction power, water tank capacity, LIDAR, obstacle avoidance); glyph count, stroke weight, and SVG grid size are not confirmed.
- **Mobile app design language** — the Narwal companion app uses progress rings, map views, and scheduling UI that may diverge from the marketing site tokens documented here.
