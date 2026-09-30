---
version: alpha
name: "Gnome"
source_url: "https://trygnome.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Charcoal dominates the viewport before any green appears — Gnome's digital presence opens on near-black (#161616) hero panels where a compact robotic mower floats against darkness like a product render in a pitch deck, not a garden catalog. The palette extracted from the live site skews entirely monochrome (#222222 ink, #161616 deep background, #c2c2c2/#d9d9d9 for secondary surfaces), suggesting the brand treats green not as an ambient wash but as a surgical accent — a single-color voltage reserved for CTAs, status indicators, and the lawn itself in lifestyle photography. Typography defaults to the system stack (system-ui, -apple-system, Segoe UI, Helvetica, sans-serif) at clean weights, giving the interface a native-app crispness that reinforces the "smart device" positioning over "outdoor power equipment." Corners stay tight — `{rounded.sm}` on buttons, `{rounded.xs}` on input fields — projecting engineering precision rather than consumer friendliness. Spacing runs generous at section boundaries (`{spacing.section}` 64px+) to let product imagery breathe, while interior card padding stays compact (`{spacing.md}` to `{spacing.base}`), creating a rhythm that alternates between cinematic pause and dense specification tables. The overall system reads as a hardware-tech brand that happens to live outdoors: dark, controlled, data-rich, with moments of vivid green breaking through like a freshly cut stripe on a dark lawn.

colors:
  primary: "#3db549"
  primary-active: "#2f9a3b"
  primary-disabled: "#a8ddb0"
  ink: "#222222"
  ink-deep: "#161616"
  body: "#3a3a3a"
  muted: "#6b6b6b"
  muted-soft: "#c2c2c2"
  hairline: "#d9d9d9"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  canvas-dark: "#161616"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-elevated: "#1e1e1e"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#3db549"
  warning: "#e6a817"
  error: "#d94040"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.07
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.8px
  display-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.1px
  title-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-value:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif"
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
  hero: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 1.5px solid {colors.ink}
  button-secondary-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 1.5px solid {colors.on-dark}
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.ink}
  text-input-dark:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.muted}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline-soft}
  nav-bar-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  hero-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    paddingBlock: "{spacing.hero}"
    minHeight: 90vh
  hero-media:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-lg}"
    paddingBlock: "{spacing.section}"
    aspectRatio: 16/9
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    imageAspectRatio: 4/3
  product-card-dark:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    rowPadding: "{spacing.md} 0"
    divider: 1px solid {colors.hairline}
  spec-table-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    rowPadding: "{spacing.md} 0"
    divider: 1px solid {colors.muted}
  feature-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  status-indicator:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    width: 8px
    height: 8px
  section-header:
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    marginBottom: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    hoverColor: "{colors.primary}"
  comparison-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    headerTypography: "{typography.title-md}"
  cta-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl} {spacing.xxl}"
  mobile-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md} {rounded.md} 0 0"
    padding: "{spacing.lg}"
    scrim: "{colors.ink-deep}"
    scrimOpacity: 0.6
---

## Components

### Buttons

**`button-primary`** — Solid green (#3db549) fill with white text at 600 weight, 8px radius keeping edges precise. On hover, background darkens to `primary-active` (#2f9a3b) with no scale transform; on disabled, fill fades to a pale mint (`primary-disabled`) at reduced opacity. Used for all purchase-path CTAs: "Buy Now," "Add to Cart," "Get Started."

**`button-secondary`** — White fill with a 1.5px ink-black border and black text. Provides equal visual weight to primary without competing for attention. Hover state fills background to `surface-soft` while maintaining border. Used for secondary actions: "Learn More," "Compare Models," "View Specs."

**`button-secondary-dark`** — Inverted variant for dark hero sections: transparent fill, white border, white text. Hover fills to a low-opacity white (rgba 255,255,255,0.08). Maintains the same 48px height and 8px radius as the standard secondary.

**`button-ghost`** — No background, no border; text-only with a subtle underline on hover. Sized smaller (14px / button-md) for inline actions like "See all features" within content sections.

### Inputs

**`text-input`** — Light mode: white background, 1px hairline border that sharpens to ink-black on focus. Tight 4px radius reads technical. Placeholder text at `muted` (#6b6b6b). Dark variant (`text-input-dark`) uses the elevated surface (#1e1e1e) with a muted border that brightens on focus.

### Navigation

**`nav-bar`** — Fixed 72px bar, white background with a 1px hairline-soft bottom border that appears only on scroll. Logo left-aligned, nav links centered at 15px/500 weight, CTA button right-aligned. The dark variant (`nav-bar-dark`) uses the deep canvas (#161616) with no bottom border — it bleeds into the hero below.

**`nav-bar-dark`** — Transparent-to-dark transition: starts fully transparent over the hero image and gains the `canvas-dark` background after 100px scroll, transitioning over 200ms.

### Hero

**`hero-dark`** — Full-viewport dark panel (#161616) with a centered product shot. Headline runs at `display-xl` (56px/700) with tight -1.5px tracking. Subheadline at `body-lg` (18px/400) with generous line-height. CTA buttons stack horizontally with `spacing.md` gap. The hero occupies minimum 90vh to ensure the mower image commands the viewport before scrolling into specs.

**`hero-media`** — A 16:9 video/image panel used for lifestyle content (mower in action on real lawns). Text overlay positioned bottom-left with a subtle gradient scrim from transparent to 60% black.

### Product Cards

**`product-card`** — Light gray (`surface-soft`) card with 8px radius, housing a 4:3 product image, model name at `title-md`, a one-line descriptor at `body-sm`, and price at `title-sm` weight 600. No border — relies on background contrast against white canvas. Hover lifts with a 0 4px 16px rgba(0,0,0,0.08) shadow.

**`product-card-dark`** — Same structure on the elevated dark surface (#1e1e1e). Used in the comparison/lineup sections where the page runs full-dark.

### Specification Tables

**`spec-table`** — Two-column layout with uppercase 12px/700 labels on the left and 14px/500 values on the right, separated by hairline dividers. Key specs for mowers: cutting width, battery life, yard coverage, noise level, slope capability. Dark variant mirrors structure on the dark canvas.

### Badges & Indicators

**`feature-badge`** — Small green pill (4px radius, not fully rounded) labeling key differentiators: "GPS Mapping," "Auto-Schedule," "Rain Sensor." Sits atop product cards or within spec sections.

**`status-indicator`** — 8px green dot used alongside mower connectivity status: "Online," "Mowing," "Charging." Pulses with a subtle animation when active.

### Comparison

**`comparison-card`** — Used in the "Compare Models" section. Light surface with 12px radius, model name header, and a vertical list of spec rows. The selected/recommended model gets a 2px primary border on the top edge and a "Recommended" feature-badge.

### CTA Banner

**`cta-banner`** — Full-width green banner with white display text and a `button-secondary-dark`-styled button (white border on green). Used mid-page to break up content sections with a conversion prompt.

### Footer

**`footer`** — Deep black (#161616) with four-column grid: Products, Support, Company, Legal. Link text at `body-sm` in muted-soft (#c2c2c2), hovering to primary green. Bottom row contains copyright, social icons, and payment badges.

### Mobile Drawer

**`mobile-drawer`** — Bottom-sheet pattern with 12px top-radius corners, white background, and a dark scrim behind. Houses mobile nav, filters, or cart summary. Slides up with a 300ms ease-out curve.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Hero headline drops to `display-lg` (40px). Nav collapses to hamburger + mobile-drawer. Product cards stack vertically full-width. Spec tables scroll horizontally. CTAs go full-width. |
| Tablet | 744–1128px | Two-column product grid. Hero headline at `display-lg`. Nav links visible but condensed spacing. Comparison cards stack 2-up. Section padding reduces to `spacing.xxl`. |
| Desktop | 1128–1440px | Three-column product grid. Full nav bar with all links. Hero at full `display-xl`. Spec tables run side-by-side with product imagery. Comparison shows all models in a row. |
| Wide | > 1440px | Content max-width caps at 1440px, centered. Additional whitespace on flanks. Hero image scales to fill but text container stays fixed-width at ~680px. |

### Touch Targets

- Minimum tap target: 44x44px on all interactive elements
- Mobile nav links padded to 48px row height
- Buttons maintain 48px height across all breakpoints; width goes full-bleed on mobile
- Card tap targets encompass the entire card surface, not just the text

### Collapsing Strategy

- Nav links collapse into hamburger drawer at < 744px; logo and cart icon remain visible
- Product grid: 3-col → 2-col → 1-col stack at breakpoints
- Spec tables: side-by-side columns collapse to a single scrollable column on mobile
- Comparison section: horizontal scroll with snap points on mobile, full grid on desktop
- Footer columns: 4-col → 2-col → single accordion stack on mobile
- Hero CTA buttons: horizontal row on desktop, vertical full-width stack on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Site blocked by anti-bot verification** — page title returned "Bot Verification," meaning all extracted colors (#222222, #161616, #c2c2c2, #d9d9d9) likely represent the challenge page, not the actual brand design. The monochrome palette used here is inferred from those values but may not match the live product pages.
- **Primary green (#3db549) is an informed estimate** — Gnome is a lawn-care robotics brand where green is the expected accent, but the exact hex could not be verified from extraction. The true primary may differ in hue or saturation.
- **No custom typeface detected** — only system font stacks were found. The brand may load a custom webfont (e.g., a geometric sans like Inter or Manrope) via JavaScript that the extractor could not capture.
- **No meta theme-color set** — mobile browser chrome color unknown.
- **Component dimensions (nav height, card aspect ratios, spacing values) are architectural recommendations** — actual measurements could not be taken from the blocked page.
- **Dark-mode vs. light-mode split is assumed** — the brand likely uses dark hero sections with light content sections, but the actual page structure was not observable.
- **Animation and motion tokens not captured** — transition durations, easing curves, and scroll-triggered behaviors are estimates based on hardware-tech brand conventions.
