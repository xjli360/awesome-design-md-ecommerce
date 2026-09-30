---
version: alpha
name: "Leon & George"
source_url: "https://www.leon-and-george.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Named after the founders' two dogs, Leon & George trades on a domestic intimacy unusual for a premium brand — the name sounds like a legal firm or a jazz duo, which makes the reveal (a plant delivery service) land with quiet surprise. The design system doubles down on this tension: serious editorial restraint and white-dominant layouts carry a catalog of living things that resist the language of pure commerce. Photography is the primary visual currency here, with each plant styled against bone-white walls or sun-warmed concrete in the way a shelter magazine might frame a still life — never a product shot, always a portrait. The palette reads almost entirely neutral: warm white canvas, near-black charcoal ink, soft stone hairlines, and a single deep botanical green ({colors.primary}, estimated around #3B5234) that surfaces almost exclusively on primary CTAs and selection states. The green is forest-floor rather than garden-center — it avoids the fresh lime or sage that mainstream plant brands default to, and it almost disappears into the white field around it. Typography pairs a classic serif at modest weights for display hierarchy — headings feel borrowed from a horticultural quarterly rather than a DTC homepage — with a spare geometric sans for pricing, nav, and UI chrome. Cards use minimal rounding ({rounded.xs} to {rounded.sm}) rather than pillowy corners; this keeps the product photography flush and the overall register closer to a well-designed print catalog than to a Shopify template. Leon & George is a rare case where the brand's most deliberate design choice is what it leaves out: no urgency banners, no badge proliferation, no lifestyle content competing with the specimen — the plants are trusted to sell themselves.

colors:
  primary: "#3B5234"
  primary-active: "#2D4028"
  primary-disabled: "#A8BAA2"
  ink: "#1A1A18"
  body: "#3D3D3B"
  muted: "#7A7A76"
  hairline: "#E0DDD8"
  canvas: "#FFFFFF"
  surface-soft: "#F8F6F2"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  accent-stone: "#C8B99A"
  accent-stone-soft: "#EDE8DF"

typography:
  display-xl:
    fontFamily: "serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.03em
  price:
    fontFamily: "sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.04em
  label-uppercase:
    fontFamily: "sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.15em
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
  product-card-title:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  product-card-label:
    typography: "{typography.label-uppercase}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  hero:
    backgroundColor: "{colors.canvas}"
    layout: split
    textSide: left
    imageSide: right
    minHeight: 80vh
    padding: "{spacing.section}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 480px
  plant-detail-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    aspectRatio: "4/5"
  care-guide-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    iconColor: "{colors.primary}"
  pot-selector:
    backgroundColor: "{colors.canvas}"
    borderDefault: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    borderDefault: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    typography: "{typography.label-uppercase}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  editorial-callout:
    backgroundColor: "{colors.accent-stone-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.section}"
    rounded: "{rounded.none}"
  section-divider:
    borderTop: "1px solid {colors.hairline}"
    marginY: "{spacing.xxl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section}"
  footer-heading:
    typography: "{typography.label-uppercase}"
    textColor: "{colors.surface-soft}"

## Components

### Buttons
**`button-primary`** — A full-bleed deep botanical green block with zero border-radius and uppercase tracked lettering at 0.1em; the shape and type treatment together signal editorial intent rather than ecommerce urgency. Active state deepens to `{colors.primary-active}` with no shadow or scale animation. Disabled fades to a pale sage (`{colors.primary-disabled}`). The square silhouette is the signature detail — no pill, no rounding, no softening.

**`button-secondary`** — White canvas with a 1px solid ink border; identical uppercase tracking to `button-primary`. Used for secondary actions like "View Care Guide" or pot-style alternatives. The thin stroke border is the only ornament, preserving the flat-editorial register.

**`button-ghost`** — No background, no border, underlined; reserved for tertiary navigation nudges ("See all plants," "Learn more"). Minimal visual weight protects the photography hierarchy from UI chrome competition.

### Text Input
**`text-input`** — Square-cornered, hairline border in default state, thickening to solid ink on focus. No fill color change, no drop shadow, no inner glow. Form fields read as structural slots cut from the page rather than interactive widgets with their own visual personality.

### Nav Bar
**`nav-bar`** — A 64px white bar with a single bottom hairline as the only separator. Navigation items use `{typography.nav-link}` at 13px with 0.04em tracking — spacious, lowercase, unhurried. Logo anchors the left; cart and account icons sit right. The absence of a search bar in the primary nav is consistent with the brand's posture of curated browse over keyword hunt.

### Product Card
**`product-card`** — No border-radius, no shadow, no stroke frame. The 3/4 portrait image (plants are tall and vertical) fills the card top; plant name follows in `{typography.body-md}`, then a muted species or collection label in `{typography.label-uppercase}`, then price in `{typography.price}`. Grid gutters and white space do the separation work — there is no card surface, only content sitting on canvas.

### Hero
**`hero`** — Split layout at desktop: editorial headline in `{typography.display-xl}` at weight 400 serif on the left, full-bleed plant portrait on the right. The weight 400 serif at 48px is the signature move — light enough to read as a magazine cover rather than an ecommerce header. Background is `{colors.canvas}` with generous section padding. At mobile, the image leads and the headline overlays the bottom of the frame.

### Plant Detail Gallery
**`plant-detail-gallery`** — A near-full-width portrait image at 4/5 aspect ratio against `{colors.surface-soft}`. Multiple angles stack vertically on scroll rather than a carousel, keeping the experience closer to browsing a print lookbook than a product configurator. No lightbox chrome; zoom activates via cursor change only.

### Care Guide Badge
**`care-guide-badge`** — Compact inline pills in `{colors.surface-soft}` with a leading icon (sun exposure, watering frequency, humidity) rendered in `{colors.primary}` and descriptive text in `{typography.caption}`. A horizontal row of four to six badges appears on the product detail page, delivering horticultural specs at a glance without the visual weight of a data table or accordion.

### Pot Selector
**`pot-selector`** — Square swatches with a 1px hairline in resting state; selection state swaps to a 1px ink border with no fill color shift or checkmark. Material and finish labels sit in `{typography.caption}` below each swatch. The restraint of the selector mirrors the product — no color washes, no hover animations.

### Size Selector
**`size-selector`** — Rectangular, unrounded buttons with hairline borders; selected state uses an ink border. Labels are uppercase at `{typography.label-uppercase}` showing pot-diameter measurements or S/M/L/XL shorthand. Width tracks label content rather than a fixed column grid.

### Editorial Callout
**`editorial-callout`** — Full-bleed warm-sand sections (`{colors.accent-stone-soft}`) used for brand essays, care philosophy text, or seasonal introductions. Typography is `{typography.body-md}` at the default line-height of 1.6; no heading, no badge, no decorative rule — pure centered prose running at a comfortable measure.

### Footer
**`footer`** — Charcoal reversal block (`{colors.ink}`) with text in `{colors.surface-soft}`. Column headings use `{typography.label-uppercase}`; link lists use `{typography.body-sm}`. Newsletter subscription carries the same `text-input` geometry but with an inverted border against dark ground. No social icon grid, no trust-badge strip — just four link columns and a copyright line.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero becomes stacked (image top, text below as full-width block); nav collapses to hamburger; product grid switches to one column; care badges wrap to two rows |
| Tablet | 744–1128px | Two-column product grid; hero split collapses to image-above, text-below; nav shows category links inline without secondary flyouts |
| Desktop | 1128–1440px | Three-column product grid; split hero active; editorial callout uses 70% max-width centered column; nav at full width |
| Wide | > 1440px | Content capped at ~1440px with canvas gutters on both sides; four-column product grid; display type scales conservatively (display-xl stays ≤ 52px) |

### Touch Targets
- All buttons meet 48px minimum height on mobile
- Pot selector swatches expand touch target via padding rather than visual swatch size
- Hamburger icon touch area is 44×44px minimum, visually smaller
- Full product card area is tappable, not just the text region
- Care guide badges are display-only on mobile, not interactive tap targets

### Collapsing Strategy
- Desktop split hero → image-above / headline-below at tablet → full-bleed portrait with headline overlay at mobile bottom
- Horizontal care badge row → two-row wrap at ≤ 375px viewport width
- Three-column product grid → two-column at tablet → single-column at mobile
- Footer four-column grid → two-column at tablet → single-column accordion at mobile (headers are expand/collapse toggles)
- Pot and size selectors scroll horizontally at mobile rather than wrapping to a new line

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All hex colors are estimated from brand knowledge** — live site extraction returned zero color values (likely JavaScript-loaded design tokens or anti-bot protection). All palette values should be verified against the live site or brand kit before production use.
- **Primary green shade unconfirmed** — #3B5234 is an educated estimate consistent with the premium botanical category; the brand may use a lighter sage, a warmer olive, or even near-black as its primary action color.
- **All font families are estimated** — extraction returned no font-family stacks. Leon & George likely uses a licensed editorial serif (candidates: Freight Display, Canela, Domaine Display, or a bespoke foundry face) paired with a geometric or neo-grotesque sans; actual names require live CSS inspection or brand kit access.
- **Border-radius confirmation** — `{rounded.none}` is assumed from the editorial brand archetype; the actual computed radius on cards and buttons may be 2–4px and should be measured.
- **Exact typography sizes and weights** — all font sizing, weight, and tracking values are estimated; the serif display face in particular may run lighter (weight 300) or at different optical sizes.
- **Animation and transition tokens** — not derivable without live inspection; hover-state transitions, page fade behavior, and cart-drawer animation omitted entirely.
- **Dark mode** — unknown; not publicly documented; assumed absent based on the brand's white-canvas editorial identity.
- **Platform confirmation** — extraction flagged platform-shopify as False; the actual storefront platform is unconfirmed, which may affect component architecture (particularly cart, checkout, and collection-filter patterns).
