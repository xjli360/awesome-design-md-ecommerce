---
version: alpha
name: "Kollokium"
source_url: "https://www.kollokium.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Pale aquamarine (#aadddd) is the first surprise — a muted, chapter-ring teal appearing as the brand's primary voltage in a category that almost universally reaches for gold, black, or carbon. Kollokium frames itself not as a watch company but as a watch projects operation, a micro-brand disposition that treats each reference as a finite, documented experiment rather than a catalog line. The deep near-black palette (#121212 as the primary ink surface, #230d0d adding a faint burgundy undertone to the darkest elements) keeps the stage deliberately dim, so that the aquamarine and the occasional #ff8900 orange accent read as genuine dial-color references rather than decorative UI choices. A secondary band of steel blues (#7396a2, #5487a0) reinforces the nautical and industrial undertone — these are colors borrowed from the objects, not from a mood board. The surface system is minimal: #fefefe and #f5f5f5 whites keep product photography isolated, while #f3f3f3 and #dedede grays mark structural separations without competing with the dial imagery. The rust accent (#a24e4e) completes a palette that reads like a cross-section of an actual watch case — anodized aluminum, blued steel, ceramic bezel, aged lume. No custom font stack was recoverable from the live site, pointing to JS-loaded or variable-font delivery; the system defaults here use a geometric sans that is consistent with independent watch brand practice: compact, legible, carrying small numbers and spec strings well. Components use `{rounded.sm}` geometry throughout — nothing pill-shaped, nothing with a hard zero radius. The overall spatial register is spare: generous white-field photography padded with wide margins, short nav labels, and CTA buttons sized for confident one-tap interaction on mobile. The orange (#ff8900) appears as a single-point accent reserved for active state highlights and edition markers, never as a fill, making it the brand's most attention-focused signal.

colors:
  primary: "#aadddd"
  primary-active: "#7396a2"
  primary-disabled: "#c8e8e8"
  accent-orange: "#ff8900"
  accent-rust: "#a24e4e"
  steel-mid: "#5487a0"
  steel-soft: "#7396a2"
  ink: "#121212"
  ink-deep: "#230d0d"
  body: "#444444"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#f3f3f3"
  canvas: "#fefefe"
  surface-soft: "#f5f5f5"
  surface-card: "#f3f3f3"
  on-primary: "#121212"
  on-dark: "#fefefe"

typography:
  display-xl:
    fontFamily: "'Inter', 'DM Sans', system-ui, -apple-system, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', 'DM Sans', system-ui, -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Inter', 'DM Sans', system-ui, -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', 'DM Sans', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Inter', 'DM Sans', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.03em
  body-md:
    fontFamily: "'Inter', 'DM Sans', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'DM Sans', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'DM Sans', system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  label-uppercase:
    fontFamily: "'Inter', 'DM Sans', system-ui, -apple-system, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  specs-mono:
    fontFamily: "'JetBrains Mono', 'Roboto Mono', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'Inter', 'DM Sans', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.04em
  nav-link:
    fontFamily: "'Inter', 'DM Sans', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
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
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-ghost-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    border: "1px solid rgba(254,254,254,0.3)"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    paddingH: "{spacing.xl}"
    borderBottom: "1px solid {colors.hairline-soft}"
    logoColor: "{colors.ink}"
  nav-bar-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    paddingH: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    imageBorderRadius: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-sm}"
    hoverElevation: "0 4px 16px rgba(18,18,18,0.08)"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted-soft}"
    accentColor: "{colors.primary}"
    minHeight: 560px
    paddingV: "{spacing.section}"
    paddingH: "{spacing.xl}"
  project-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  edition-tag:
    backgroundColor: "transparent"
    textColor: "{colors.accent-orange}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    border: "1px solid {colors.accent-orange}"
  sold-out-badge:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  specs-table:
    backgroundColor: "{colors.surface-soft}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.label-uppercase}"
    valueTypography: "{typography.specs-mono}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    rowDivider: "1px solid {colors.hairline}"
  watch-dial-swatch:
    borderRadius: "{rounded.full}"
    size: 32px
    border: "2px solid {colors.hairline}"
    activeBorder: "2px solid {colors.primary}"
  project-status-pill:
    available:
      backgroundColor: "rgba(170,221,221,0.18)"
      textColor: "{colors.primary-active}"
      typography: "{typography.label-uppercase}"
      rounded: "{rounded.full}"
      padding: "4px 12px"
    coming-soon:
      backgroundColor: "rgba(255,137,0,0.12)"
      textColor: "{colors.accent-orange}"
      typography: "{typography.label-uppercase}"
      rounded: "{rounded.full}"
      padding: "4px 12px"
    archived:
      backgroundColor: "{colors.surface-card}"
      textColor: "{colors.muted}"
      typography: "{typography.label-uppercase}"
      rounded: "{rounded.full}"
      padding: "4px 12px"
  image-lightbox:
    backgroundColor: "rgba(18,18,18,0.92)"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    closeButtonColor: "{colors.on-dark}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.label-uppercase}"
    headingColor: "{colors.muted}"
    paddingV: "{spacing.section}"
    paddingH: "{spacing.xl}"
    borderTop: "1px solid rgba(254,254,254,0.08)"

## Components

### Buttons

**`button-primary`** — Filled teal (#aadddd) with dark ink text on-top, 44px tall, `{rounded.sm}` geometry. Hover state deepens to `{colors.primary-active}` (#7396a2) without animation overshoot. Disabled state uses `{colors.primary-disabled}` with `{colors.muted}` label to signal, not hide, unavailability. Used exclusively on purchase and reservation CTAs.

**`button-secondary`** — Transparent fill with a `{colors.hairline}` 1px border; matches primary height and padding so the two can sit side-by-side in a CTA pair without vertical misalignment. On dark backgrounds, swap to `button-ghost-dark` which uses a semi-transparent white border.

**`button-ghost-dark`** — For hero and dark-section use. Transparent background, `{colors.on-dark}` label, and a 30% opacity white border. Avoids the heavy-fill visual weight that would compete with watch photography.

### Navigation

**`nav-bar`** — 60px fixed header on a `{colors.canvas}` white ground, separated from content by a `{colors.hairline-soft}` bottom rule. Logo sits left in `{colors.ink}`; navigation labels use `{typography.nav-link}` — compact 14px, 0.03em tracking — favoring legibility over display weight. A dark-mode variant (`nav-bar-dark`) inverts to `{colors.ink}` background with `{colors.on-dark}` labels for hero overlays.

### Product Card

**`product-card`** — Sits on `{colors.surface-card}` (#f3f3f3) with `{rounded.sm}` corners and a mild shadow on hover (`0 4px 16px rgba(18,18,18,0.08)`). Title uses `{typography.title-md}` (500 weight, compact tracking); price uses `{typography.title-sm}`. Status pills (`project-status-pill`) float above the image to communicate availability without consuming card body space.

### Hero

**`hero`** — Dark-ground section (`{colors.ink}`) with a minimum 560px height and generous `{spacing.section}` vertical padding. Headline runs `{typography.display-xl}` at light 300 weight — the restraint is intentional, letting the watch image carry visual mass. Subhead in `{colors.muted-soft}` reads as annotation. Aquamarine `{colors.primary}` appears as a typographic accent or underline, not a fill.

### Badges and Tags

**`project-badge`** — Solid `{colors.primary}` fill, all-caps `{typography.label-uppercase}` label in `{colors.on-primary}`, `{rounded.xs}` corners. Applied to active project cards to signal availability.

**`edition-tag`** — Outlined in `{colors.accent-orange}` (#ff8900) with matching text; transparent fill keeps it lightweight. Used for limited-edition callouts and batch identifiers. Never filled — orange as fill would overpower the palette.

**`sold-out-badge`** — Deep `{colors.ink-deep}` (#230d0d) fill with `{colors.on-dark}` text. The burgundy undertone differentiates it visually from a plain black while keeping the tone somber.

### Specs Table

**`specs-table`** — On `{colors.surface-soft}` ground with `{rounded.sm}` container. Label column uses `{typography.label-uppercase}` in `{colors.muted}` (10px, spaced caps); value column uses `{typography.specs-mono}` for watch specifications (case diameter, lug-to-lug, movement ref, water resistance). Row dividers in `{colors.hairline}`. This component is central to the brand's project-documentation ethos.

### Dial Swatch

**`watch-dial-swatch`** — 32px circular color disc, `{rounded.full}`, `{colors.hairline}` 2px default border; active selection border upgrades to `{colors.primary}`. Rendered in a tight horizontal row below the product title for color-variant selection.

### Project Status Pill

**`project-status-pill`** — Three states: available (teal tint background, `{colors.primary-active}` label), coming-soon (orange tint, `{colors.accent-orange}` label), archived (neutral `{colors.surface-card}`, `{colors.muted}` label). `{rounded.full}` geometry, all-caps `{typography.label-uppercase}`.

### Footer

**`footer`** — Full-width dark section on `{colors.ink}`, `{spacing.section}` vertical padding, topped by a hairline-opacity rule. Section headings in `{typography.label-uppercase}` / `{colors.muted}`; body links in `{colors.on-dark}` defaulting to `{colors.primary}` on hover. Reinforces the dark-world product aesthetic from the bottom of every page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger icon; hero text scales to `{typography.display-md}`; specs-table scrolls horizontally; dial swatches increase touch target to 44px |
| Tablet | 744–1128px | Two-column product grid; nav shows abbreviated labels; hero maintains full dark ground; specs-table displays inline |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero may use split-layout with image offset; side-by-side CTA pair on PDPs |
| Wide | > 1440px | Grid max-width constrained to ~1280px with auto side margins; hero background bleeds full width, content centered |

### Touch Targets

- All buttons minimum 44×44px on mobile regardless of visual size
- Dial swatches expand to 44px diameter on touch viewports; default 32px on desktop
- Nav hamburger tap area padded to 44×44px
- Project-status pills are display-only and do not require minimum tap sizing

### Collapsing Strategy

- Primary navigation: icon-only hamburger on mobile, full labels from 744px up
- Product grid: 1 → 2 → 3 columns at 744px and 1128px breakpoints
- Specs table: horizontal scroll with sticky label column on mobile; full inline table above 744px
- Footer columns: stack to single column below 744px, two columns at tablet, four columns at desktop
- Hero copy: `display-xl` only at 1128px+; steps down to `display-md` at tablet, `display-sm` at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font families detected — the font-family extraction returned only a CSS property value (`object-fit: contain`) rather than a typeface name, indicating fonts are loaded via a JS bundle, @font-face in a lazy stylesheet, or a Shopify theme asset not reachable at extraction time. The typography spec above uses Inter/DM Sans as placeholder geometric sans-serifs consistent with the micro-brand watch category; replace with actual typeface when available.
- No `meta theme-color` set, so mobile browser chrome color is undetermined.
- The generic blue (#3498db) in the extracted palette is almost certainly a Shopify or Bootstrap framework default and has been excluded from the design token set.
- Exact button border-radius values are inferred from the rounded system; no computed style data confirmed the specific pixel values used on-site.
- Motion and animation values (transition duration, easing curves) are not present in the extracted hints.
- Dark-mode support status is unknown — the palette contains both a near-white canvas and a near-black canvas, which could indicate a theme toggle or simply different section treatments.
- No icon set or icon style (line weight, corner rounding) was recoverable.
