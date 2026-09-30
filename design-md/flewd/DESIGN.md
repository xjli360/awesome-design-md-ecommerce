---
version: alpha
name: "Flewd"
source_url: "https://flewd.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Electric chartreuse (#e0fe2c) against near-black navy (#112233) — the combination reads almost radioactive, which is exactly the point for a bath soak brand built around the phrase "Stress Destroying." Flewd doesn't soften its premise with botanical beige or hushed type; the dominant signal color is a sharp yellow-green that vibrates against dark grounds like voltage on a circuit board. The warm cream (#fff5ef) enters only as a secondary surface, pulling spa-register warmth into a palette that otherwise reads closer to performance nutrition than bath product. That tension — medicinal aggression plus the sensory heat of a long soak — is the whole brand proposition delivered purely through color. Typography couldn't be reliably extracted from the live site (fonts load via JavaScript, only "inherit" and "swiper-icons" surfaced), but the brand voice ("Stress Destroying," "Anxiety, Insomnia, Aches") demands a wide, heavy grotesque — all-caps utility labels, not serene calligraphy. Full-pill shapes (`{rounded.full}`) on buttons and badges carry the brand's anti-softness stance: stress relief here is an act, not a ritual. The Swiper-based carousel architecture (visible from the font stack) signals a mobile-first product browsing experience. CTAs in chartreuse on dark navy achieve contrast ratios well above WCAG AA with zero softening — the brand's refusal to mute its primary is a deliberate signal that passive wellness is not the offer. A secondary lime (#f0ff96) provides a gentler tint for hover states and callout backgrounds, while the warm cream canvas gives product photography room without the clinical coldness of pure white. Alert red (#cc0000) reserved for urgency — sold-out flags, limited inventory — makes every other color in the system feel calm by contrast, a kind of chromatic hierarchy that mirrors the brand's core logic: name the stressor, then eliminate it.

colors:
  primary: "#e0fe2c"
  primary-active: "#c8e200"
  primary-hover: "#d4f020"
  primary-disabled: "#f0ff96"
  ink: "#112233"
  body: "#1e2d3d"
  muted: "#5a6a7a"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#fff5ef"
  surface-card: "#ffffff"
  surface-dark: "#112233"
  on-primary: "#112233"
  on-dark: "#ffffff"
  lime-soft: "#f0ff96"
  alert: "#cc0000"
  near-black: "#121212"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -1.5px
    textTransform: uppercase
  display-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.5px
    textTransform: uppercase
  display-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  label-caps:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px

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
    padding: 14px 32px
    height: 52px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 52px
    border: "2px solid {colors.ink}"
  button-secondary-light:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 52px
    border: "2px solid {colors.on-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1.5px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    padding: 8px 16px
    textAlign: center
  alert-banner:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-caps}"
    padding: 10px 16px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "1/1"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    accentColor: "{colors.primary}"
    minHeight: 600px
    padding: "64px 24px"
  stress-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  benefit-tag:
    backgroundColor: "{colors.lime-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  ingredient-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    accentBorderLeft: "3px solid {colors.primary}"
  product-carousel:
    gap: "{spacing.base}"
    scrollBehavior: smooth
    navigationDotColor: "{colors.primary}"
    navigationDotInactive: "{colors.hairline}"
    overflowX: scroll
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    starColor: "{colors.primary}"
    bodyTypography: "{typography.body-sm}"
    metaTypography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    bodyTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    linkHoverColor: "{colors.primary}"
    padding: "64px 24px"

## Components

### Buttons
**`button-primary`** — Full-pill shape (`{rounded.full}`) in electric chartreuse (`{colors.primary}`) with dark navy type (`{colors.on-primary}`), 52px tall with 32px horizontal padding. All-caps, 700 weight via `{typography.button-md}`. Hover shifts to `{colors.primary-hover}` (#d4f020); disabled washes to `{colors.primary-disabled}` (#f0ff96) with `{colors.muted}` text. Every primary CTA — add-to-cart, "Start Destroying Stress," subscribe — uses this variant exclusively; the chartreuse surface is the brand's most recognizable design move.

**`button-secondary`** — Transparent background with a 2px solid `{colors.ink}` border, identical pill shape and 52px height as primary. Paired with primary on light backgrounds where two actions share a row. On dark hero sections, `button-secondary-light` swaps border and text to `{colors.on-dark}` white, maintaining the pill silhouette against navy.

### Navigation
**`nav-bar`** — 64px tall white bar with a 1px `{colors.hairline}` bottom separator. Logo left-aligned in `{colors.ink}`; links in `{typography.nav-link}` (14px semibold). On dark hero placements, `nav-bar-dark` runs the same structure against `{colors.surface-dark}` navy with white text. An `announcement-bar` in `{colors.primary}` sits above the nav as the highest DOM element — the chartreuse stripe is the very first visual hit on page load, carrying free-shipping thresholds or campaign callouts in `{typography.label-caps}`.

### Product Card
**`product-card`** — White surface with a 1px `{colors.hairline}` border and `{rounded.md}` (12px) corners. Product image in a 1:1 aspect ratio square at the card top. Product name renders in `{typography.title-sm}` (15px semibold), price in `{typography.title-md}` (18px bold). Benefit tags (`benefit-tag`) in `{colors.lime-soft}` stack beneath the name as horizontal chips. The primary CTA stretches full card width at the bottom using `button-primary`.

### Hero Section
**`hero-section`** — Full-bleed `{colors.surface-dark}` navy, minimum 600px tall. Headline in `{typography.display-xl}` (56px, 800 weight, uppercase, −1.5px tracking) in `{colors.on-dark}` white, with the key stress target word — "ANXIETY," "INSOMNIA," a stat — rendered in `{colors.primary}` chartreuse for intra-headline contrast. Subhead in `{typography.body-md}` white. Primary CTA below uses `button-primary`; a secondary option uses `button-secondary-light`. On mobile the headline collapses to `{typography.display-md}` sizing.

### Stress Badge
**`stress-badge`** — Full-pill chip in `{colors.primary}` chartreuse with `{colors.on-primary}` navy label-caps text (`{typography.label-caps}`). Applied as overlay tags on product cards and PDP section headers to flag targeted conditions: "ANXIETY," "INSOMNIA," "ACHES." No icon — the chartreuse field carries all the signal. A lighter variant swaps the fill for `{colors.lime-soft}` and uses `benefit-tag` styling for lower-urgency descriptors.

### Announcement Bar
**`announcement-bar`** — Full-width stripe in `{colors.primary}` sitting above the nav, 8px vertical padding, centered `{typography.label-caps}` in `{colors.on-primary}`. The brand's first chromatic statement before any product imagery loads. Carries time-sensitive copy (free shipping, limited drops). When urgency escalates to stock or fulfillment warnings, `alert-banner` replaces it with `{colors.alert}` (#cc0000) red.

### Ingredient Callout
**`ingredient-callout`** — Warm cream surface (`{colors.surface-soft}`, #fff5ef) with `{rounded.md}` corners and `{spacing.lg}` inner padding. A 3px `{colors.primary}` left-border accent anchors it visually without adding a full card border. Body in `{typography.body-md}` ink. Used on PDPs to explain what each mineral or botanical does — the warm surface temperature distinguishes "science" copy from the aggressive hero register above it.

### Product Carousel
**`product-carousel`** — Swiper-based horizontal scroll (`overflow-x: scroll`) with `{spacing.base}` gap between cards and smooth scroll behavior. Navigation dots render in `{colors.primary}` chartreuse (active) and `{colors.hairline}` gray (inactive). On mobile the carousel is the primary product discovery surface; desktop may switch to a static grid.

### Review Card
**`review-card`** — White card with `{rounded.md}` and a 1px `{colors.hairline}` border. Star ratings render in `{colors.primary}` chartreuse — a distinctive departure from conventional amber/gold that keeps the brand palette coherent throughout the social-proof zone. Review body in `{typography.body-sm}` ink; reviewer name and date in `{typography.caption}` muted. Cards appear in a `product-carousel` row below the product description.

### Footer
**`footer`** — Near-black background (`{colors.near-black}`, #121212) with `{colors.on-dark}` body copy in `{typography.body-sm}`. Section headings in `{typography.label-caps}` at reduced opacity. Link hover color is `{colors.primary}` chartreuse — the same primary surfaces again in the footer as the sole accent against black, completing a chromatic frame around the page. Newsletter input uses `text-input` with dark-adapted border color.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline collapses to `display-md`; nav collapses to hamburger with full-screen dark overlay; announcement bar wraps to two lines if needed; product carousel becomes swipe-scroll with dot indicators |
| Tablet | 744–1128px | Two-column product grid; nav shows partial links with overflow drawer; hero gains horizontal padding; ingredient callout runs two columns |
| Desktop | 1128–1440px | Three-column product grid; hero text left-aligned at ~50% width with product image filling right half; full nav links visible |
| Wide | > 1440px | Max-width container (~1400px) centered; section padding scales up; hero image bleeds to edge behind centered content column |

### Touch Targets
- All buttons minimum 52px tall, 44px wide
- Stress badge chips minimum 36px tall for reliable tap
- Nav hamburger icon minimum 44×44px hit area
- Product carousel: full card width is swipe surface, no minimum drag threshold
- Footer accordion section headers minimum 48px tall on mobile

### Collapsing Strategy
- Announcement bar collapses from multi-message cycling to single static line on mobile
- Ingredient callout stacks from two-column to single column below 744px
- Footer collapses from 4-column link grid to tap-to-expand accordion sections on mobile
- Product card tags truncate to two chips with "+N more" overflow on narrow cards
- Hero subhead may be hidden at smallest mobile breakpoint to preserve headline impact

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Fonts not extractable**: Only "inherit" and "swiper-icons" found in computed font stacks — the actual brand typeface loads via JavaScript after parse and could not be captured. All typography tokens use system-ui fallback stacks. The real brand likely uses a licensed compressed or extended grotesque (e.g., Monument Extended, Neue Haas Grotesk, or similar).
- **Border-radius not confirmed**: Actual button and card radius values not extracted; tokens inferred from brand voice and DTC wellness conventions.
- **Inner surface variants sparse**: Input background colors, focus rings, modal scrims, and overlay tints are inferred — only 8 colors extracted total.
- **#007aff excluded**: Extracted as a top color but identified as iOS system-default blue (framework artifact); removed from brand palette.
- **Animation and motion tokens**: Hover transition timing, carousel easing curves, and scroll animation parameters not capturable from static extraction.
- **Dark mode behavior**: No `prefers-color-scheme` handling confirmed; dark mode tokens not defined.
- **Icon system**: No icon font or SVG sprite detected beyond the Swiper navigation system; icon style (outline vs. filled, stroke weight) unknown.
