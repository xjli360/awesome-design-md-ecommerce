---
version: alpha
name: "Alienware"
source_url: "https://www.alienware.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Fourteen-sided polygons cut into black glass — that is the first thing the eye registers on any Alienware surface, digital or physical. The brand's Legend industrial-design language translates directly into its UI: hard diagonal clips on hero panels, angular container edges, and a canvas so dark (#0D0D0D) it reads as the absence of light rather than a neutral background. Into that void, a single voltage accent arrives — a bright teal-cyan (#00FFC8) that pulses across primary CTAs, hover states, system-status rings, and the iconic alien-head wordmark. This is not a gaming brand that reaches for neon saturation everywhere; the teal operates surgically against near-black surfaces and cool charcoal cards (#1A1A1A, #242424), making every interactive element feel like bioluminescence in deep water. A secondary violet (#7B2FE0) appears in gradient washes and limited-edition product badging, reinforcing the extraterrestrial mythology without competing for CTA dominance. Typography runs a geometric sans-serif stack led by custom Alienware display cuts at aggressive letter-spacing (-1px to -2px on headlines), producing that wide-set futuristic register at `{typography.display-xl}`. Body copy stays neutral in weight 400 at 15–16px, readable against dark surfaces with an `{colors.body}` of #B8B8B8 that avoids pure-white glare. Buttons are clipped-corner rectangles (`{rounded.xs}` base with CSS clip-path diagonals), not pills — softness is deliberately absent. Product cards float on `{colors.surface-card}` with 1px `{colors.hairline}` borders that brighten to `{colors.primary}` on hover, and spacing runs generous at `{spacing.lg}` to `{spacing.xl}` between grid items, giving each machine its own theater. The overall system reads as: restrained darkness punctuated by precision light.

colors:
  primary: "#00FFC8"
  primary-active: "#00E0B0"
  primary-disabled: "#0D4D3D"
  secondary: "#7B2FE0"
  secondary-active: "#6A1FD0"
  ink: "#FFFFFF"
  body: "#B8B8B8"
  muted: "#808080"
  muted-soft: "#5A5A5A"
  hairline: "#2E2E2E"
  hairline-hover: "#00FFC8"
  border-strong: "#4A4A4A"
  canvas: "#0D0D0D"
  surface-soft: "#141414"
  surface-card: "#1A1A1A"
  surface-elevated: "#242424"
  on-primary: "#0D0D0D"
  on-dark: "#FFFFFF"
  alert: "#FF3B30"
  success: "#00FFC8"
  badge-new: "#7B2FE0"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Alienware', 'Rajdhani', 'Share Tech', -apple-system, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.07
    letterSpacing: -2px
  display-lg:
    fontFamily: "'Alienware', 'Rajdhani', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1.5px
  display-md:
    fontFamily: "'Alienware', 'Rajdhani', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -1px
  display-sm:
    fontFamily: "'Alienware', 'Rajdhani', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  title-md:
    fontFamily: "'Alienware', 'Rajdhani', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-sm:
    fontFamily: "'Alienware', 'Rajdhani', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Inter', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Alienware', 'Rajdhani', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Alienware', 'Rajdhani', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.17
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  spec-label:
    fontFamily: "'Inter', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Alienware', 'Rajdhani', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: -0.5px
  badge:
    fontFamily: "'Inter', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 48px
    clipPath: "polygon(8px 0, 100% 0, calc(100% - 8px) 100%, 0 100%)"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 15px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: 12px 20px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 14px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "rgba(13, 13, 13, 0.95)"
    backdropFilter: "blur(12px)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
    borderHover: "1px solid {colors.primary}"
    transition: "border-color 0.2s ease, box-shadow 0.2s ease"
    boxShadowHover: "0 0 20px rgba(0, 255, 200, 0.08)"
  hero-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section-lg} {spacing.xl}"
    minHeight: 680px
    overflow: hidden
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 560px
  spec-grid:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    display: grid
    gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))"
    gap: "{spacing.base}"
  spec-item-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xs}"
  spec-item-value:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  price-block:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
  price-block-starting:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  configurator-option:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
    borderSelected: "2px solid {colors.primary}"
  configurator-option-selected:
    backgroundColor: "{colors.surface-elevated}"
    border: "2px solid {colors.primary}"
    boxShadow: "0 0 12px rgba(0, 255, 200, 0.12)"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px 12px 44px
    height: 44px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  comparison-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    cellPadding: "{spacing.base} {spacing.lg}"
    borderColor: "{colors.hairline}"

## Components

### Buttons
**`button-primary`** — A clipped-corner teal rectangle that reads as a parallelogram slice. The diagonal clip-path (8px inset at top-left and bottom-right) is the brand's signature geometric language applied to interaction. On hover, a subtle inner glow (0 0 12px rgba(0, 255, 200, 0.15)) reinforces the bioluminescent feel. Active state darkens to `{colors.primary-active}`. Disabled state drops to `{colors.primary-disabled}` background with `{colors.muted}` text, removing the glow entirely.

**`button-secondary`** — Transparent fill with a 1px `{colors.primary}` border and teal text. On hover, the fill floods to `{colors.primary}` and text inverts to `{colors.on-primary}`, creating a satisfying "charge-up" transition over 200ms. Uses the same clip-path diagonal as primary for visual consistency.

**`button-ghost`** — No border, no background. White text with an underline-on-hover pattern. Used for tertiary actions, breadcrumb links, and "Learn more" prompts within content blocks.

### Navigation
**`nav-bar`** — A 64px-tall fixed bar on dark canvas with a 1px `{colors.hairline}` bottom border. The Alienware alien-head logo sits left at 32px height. Navigation links use `{typography.nav-link}` in `{colors.ink}` with a teal underline animation on hover (2px bottom border slides in from center). On scroll, transitions to a frosted-glass treatment with `backdrop-filter: blur(12px)` and slightly elevated opacity background.

### Product Cards
**`product-card`** — Dark card (`{colors.surface-card}`) with a 1px `{colors.hairline}` border and `{rounded.xs}` corners. Product image occupies the top 60% with object-fit contain against a slightly lighter background. Title renders in `{typography.title-md}`, specs summary in `{typography.caption}` with `{colors.muted}` text. Price anchors bottom-left in `{colors.primary}` using `{typography.price-display}`. On hover, the border transitions to `{colors.primary}` and a subtle teal box-shadow appears, creating a "selected" glow without layout shift.

### Hero Panel
**`hero-panel`** — Full-viewport-width dark section with a centered product render (typically 3D or high-res photography) occupying 50–60% of the panel width. Headline in `{typography.display-xl}` sits left-aligned with dramatic negative letter-spacing. A diagonal line graphic (1px teal, 45deg) may slice across the background as a decorative element. CTA buttons align below the subhead with `{spacing.lg}` gap.

### Spec Grid
**`spec-grid`** — A responsive CSS Grid on `{colors.surface-soft}` that displays hardware specifications in a structured layout. Each cell has a muted uppercase label (`{typography.spec-label}`) above a white value (`{typography.title-sm}`). Grid items are separated by `{spacing.base}` gutters. Used on product detail pages below the hero to surface GPU, CPU, RAM, and display stats at a glance.

### Configurator Option
**`configurator-option`** — Interactive selection tile for the build-to-order flow. Unselected state shows a `{colors.hairline}` border; selected state promotes to 2px `{colors.primary}` border with a subtle glow shadow and elevated background (`{colors.surface-elevated}`). Each option tile contains a spec label, a brief description in `{typography.body-sm}`, and a price delta in `{colors.primary}`.

### Price Block
**`price-block`** — Displays the machine's price prominently in `{typography.price-display}` colored `{colors.primary}`. A "Starting at" label sits above in `{typography.caption}` at `{colors.muted}`. Used on product cards, hero panels, and configurator summaries.

### Badges
**`badge-new`** — Small uppercase pill in `{colors.badge-new}` (violet) with white text. Indicates newly launched products or features. Uses `{typography.badge}` at 10px with aggressive letter-spacing.

**`badge-sale`** — Same dimensions as badge-new but in `{colors.primary}` teal with dark text. Used for promotional pricing events.

### Comparison Table
**`comparison-table`** — A structured data table on `{colors.surface-soft}` for side-by-side product comparison. Column headers use `{typography.spec-label}` in uppercase muted text. Cell content uses `{typography.body-sm}`. Rows alternate between `{colors.surface-soft}` and `{colors.surface-card}` for scanability. The "winner" value in each row may highlight in `{colors.primary}`.

### Search
**`search-input`** — A rounded search field with a magnifying-glass icon (16px, `{colors.muted}`) inset left. Background is `{colors.surface-soft}` with a `{colors.hairline}` border that transitions to `{colors.primary}` on focus. Placeholder text in `{colors.muted}`, input text in `{colors.ink}`.

### Footer
**`footer`** — Full-width dark section with `{colors.hairline}` top border. Links organized in columns using `{typography.body-sm}` in `{colors.body}`, hovering to `{colors.ink}`. Dell parent-brand legal text sits at the bottom in `{typography.caption-sm}` at `{colors.muted}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger with slide-out dark drawer. Hero headline drops to `{typography.display-md}`. Product grid becomes single-column. Configurator options stack vertically. Spec grid collapses to 2-column. |
| Tablet | 744–1128px | Product grid runs 2-column. Hero panel reduces min-height to 480px. Nav shows top-level links only, overflow in "More" dropdown. Comparison table scrolls horizontally. |
| Desktop | 1128–1440px | Full nav visible. Product grid runs 3-column. Hero panel at full 680px min-height. Configurator runs 2-column option tiles beside a sticky summary panel. |
| Wide | > 1440px | Content max-width caps at 1440px, centered on canvas. Product grid may expand to 4-column on category pages. Hero product imagery scales up with additional breathing room. |

### Touch Targets
- All interactive elements maintain minimum 44px touch target on mobile
- Configurator option tiles expand to full-width on mobile with 56px min-height
- Nav hamburger icon has 48px tap area
- Card tap targets are the entire card surface, not just the CTA

### Collapsing Strategy
- Spec grids collapse from 4-col → 2-col → 1-col stack with maintained `{spacing.base}` gaps
- Comparison table switches to a swipeable horizontal scroll on mobile with sticky first column
- Hero diagonal decorative lines are hidden below tablet breakpoint
- Footer columns collapse into accordion sections on mobile with `{colors.hairline}` dividers

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned "Access Denied" during extraction — all colors and fonts are based on widely-documented Alienware brand guidelines (Legend 2.0 design language) rather than live CSS extraction
- Exact custom font file names and variable-font axis ranges could not be confirmed; Alienware uses proprietary display cuts that may load under different family names
- Exact clip-path values for the signature diagonal button corners may vary between product lines
- Animation timing curves (easing functions for hover transitions, page transitions) are not captured
- Dark-mode is assumed as default since Alienware has no documented light-mode variant, but a light surface option may exist for Dell-integrated checkout flows
- Exact breakpoint values may differ from the standard 744/1128/1440 used here
- RGB lighting color-picker component (used in AlienFX customization) is not documented here due to its interactive complexity
