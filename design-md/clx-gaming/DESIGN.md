---
version: alpha
name: "CLX Gaming"
source_url: "https://www.clxgaming.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Dark as a powered-down chassis before the LEDs ignite — CLX Gaming's digital storefront opens on #080707, a near-black canvas that swallows ambient light and forces every product render, every spec callout, every CTA to earn its photons. The primary voltage is a saturated emerald (#17b26a) that traces the path from configurator buttons to checkout confirmation, cooled by lighter mints (#73e2a7, #aaf0c7) on success states and progress indicators. This green isn't decorative; it maps directly to the build-flow funnel — "Customize," "Add to Cart," "Complete Build" — each step lit in the same hue so the eye never loses the thread. A secondary indigo spectrum (#6172f3 through #1a1c4c) surfaces on informational badges, spec-comparison highlights, and the loyalty program tier markers, giving the interface a second axis of color without competing for CTA dominance. A hot-pink warning band (#ff6476) fires on out-of-stock alerts and clearance flags, injecting urgency into an otherwise controlled palette. Typography loads via JavaScript bundles, rendering undetectable in static extraction, but the live site runs a geometric sans in the vein of industry-standard gaming faces — tight letter-spacing on headlines, weight 700+ for display, and all-caps transforms on category labels and badge text. Corners stay sharp: `{rounded.xs}` on input fields, `{rounded.none}` or `{rounded.xs}` on buttons, because beveled edges read as precision-machined in a hardware context. Spacing is generous vertically (`{spacing.section}` between hero and product grid) but compressed horizontally within product cards, mimicking the density of a spec sheet. The overall composition treats the viewport like a showcase chassis — matte-black panels, green accent lighting, and components mounted with mechanical precision.

colors:
  primary: "#17b26a"
  primary-light: "#3bcc84"
  primary-lighter: "#73e2a7"
  primary-soft: "#aaf0c7"
  primary-wash: "#d3f8e0"
  primary-surface: "#edfcf3"
  primary-active: "#0b9055"
  primary-disabled: "#097347"
  primary-deep: "#094b31"
  secondary: "#6172f3"
  secondary-light: "#7f97fa"
  secondary-soft: "#a4bbfd"
  secondary-wash: "#c6d7ff"
  secondary-surface: "#eef4ff"
  secondary-active: "#444be7"
  secondary-deep: "#1a1c4c"
  alert: "#ff6476"
  alert-soft: "#ff9da8"
  alert-wash: "#ffc5cc"
  alert-surface: "#fff1f3"
  ink: "#fafafa"
  body: "#fafafa"
  muted: "#8a8a8a"
  hairline: "#2a2a2a"
  hairline-soft: "#1e1e1e"
  canvas: "#080707"
  surface-soft: "#111010"
  surface-card: "#161515"
  surface-elevated: "#1c1b1b"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"
  on-dark: "#fafafa"
  scrim: "#080707"

typography:
  display-xl:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.07
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.09
    letterSpacing: -1px
  display-md:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.11
    letterSpacing: -0.75px
  display-sm:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: -0.5px
  title-lg:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.2px
  title-sm:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-lg:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-upper:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.4px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  spec-value:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  price-display:
    fontFamily: "'Inter', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 800
    lineHeight: 1.12
    letterSpacing: -0.5px

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
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 52px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 30px
    height: 52px
    border: 2px solid {colors.ink}
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.ink}
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 16px
    border: none
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 14px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.primary}
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.alert}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline-soft}
    backdropFilter: "blur(12px)"
  nav-bar-scrolled:
    backgroundColor: "rgba(8, 7, 7, 0.95)"
    borderBottom: 1px solid {colors.hairline}
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0
    border: 1px solid {colors.hairline-soft}
    overflow: hidden
  product-card-hover:
    border: 1px solid {colors.primary}
    boxShadow: "0 0 24px rgba(23, 178, 106, 0.15)"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    minHeight: 85vh
    padding: "{spacing.section-lg} {spacing.xl}"
    overlay: "linear-gradient(180deg, transparent 40%, {colors.canvas} 100%)"
  configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
  configurator-option:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    border: 1px solid {colors.hairline}
  configurator-option-selected:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.primary}
    boxShadow: "0 0 12px rgba(23, 178, 106, 0.2)"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    rowDivider: 1px solid {colors.hairline-soft}
  badge-in-stock:
    backgroundColor: "{colors.primary-surface}"
    textColor: "{colors.primary-active}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  badge-out-of-stock:
    backgroundColor: "{colors.alert-surface}"
    textColor: "{colors.alert}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  price-block:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
    prefixColor: "{colors.muted}"
  price-block-sale:
    textColor: "{colors.alert}"
    strikethroughColor: "{colors.muted}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid {colors.primary}
    padding: "{spacing.md} {spacing.base}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid transparent
    padding: "{spacing.md} {spacing.base}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: 1px solid {colors.hairline-soft}
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px 12px 44px
    height: 44px
    border: 1px solid {colors.hairline}
    iconColor: "{colors.muted}"
  tooltip:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.4)"
---

## Components

### Buttons

**`button-primary`** — Full-width or auto-width CTA rendered in `{colors.primary}` (#17b26a) with white text set in uppercase weight-700. Corners clip at `{rounded.xs}` (4px) for a machined, hardware-catalog feel. On hover the background deepens to `{colors.primary-active}` (#0b9055); disabled state drops to `{colors.primary-disabled}` with reduced opacity and `{colors.muted}` text. Height locks at 52px for comfortable touch targets on mobile configurator flows.

**`button-secondary`** — Transparent fill with a 2px `{colors.ink}` border and white uppercase text. On hover, the fill inverts to `{colors.ink}` (#fafafa) with `{colors.canvas}` text, creating a flash-on effect. Used for secondary actions like "View Specs" or "Compare Builds" where the primary green would create visual competition.

**`button-ghost`** — No border, no fill, green text only. Used inline within spec tables and comparison grids where a full button would disrupt the data-dense layout.

### Navigation

**`nav-bar`** — Fixed 72px bar on `{colors.canvas}` with a subtle bottom hairline. Links render in `{typography.nav-link}` (14px, weight 600, uppercase, 0.3px tracking). On scroll, background gains 95% opacity with a 12px backdrop blur to maintain readability over hero imagery. Logo sits left; primary nav center-aligned; cart icon and account icon right-aligned with `{colors.ink}` fill.

**`category-tab-active` / `category-tab-inactive`** — Horizontal tab strip below the nav for product categories (Pre-Built, Custom, Components, Sale). Active tab gets a 2px `{colors.primary}` bottom border and green text; inactive tabs show `{colors.muted}` text with a transparent border that transitions on hover.

### Product Cards

**`product-card`** — Dark card (`{colors.surface-card}` #161515) with 1px `{colors.hairline-soft}` border and `{rounded.sm}` corners. Image occupies the top 60% with no padding; specs and price stack below in `{spacing.base}` padding. On hover, the border shifts to `{colors.primary}` and a faint green box-shadow bleeds outward, simulating LED underglow. Product name renders in `{typography.title-sm}`; GPU/CPU summary in `{typography.spec-value}`; price in `{typography.price-display}`.

### Configurator

**`configurator-panel`** — The PC builder's central workspace: a `{colors.surface-soft}` panel with `{rounded.sm}` corners housing selectable component options. Each option (`configurator-option`) is a horizontal row showing component name, price delta, and a radio/checkbox indicator. Selected state (`configurator-option-selected`) gains a 2px `{colors.primary}` border with a soft green glow, making the active configuration instantly scannable.

### Spec Table

**`spec-table`** — Alternating-row data grid on `{colors.surface-soft}` with `{colors.hairline-soft}` dividers. Labels render in `{typography.spec-label}` (12px, weight 600) on the left column; values in `{typography.spec-value}` (14px, weight 500) on the right. Used on PDP pages to present full hardware manifests — CPU, GPU, RAM, storage, PSU, cooling.

### Badges

**`badge-in-stock`** — Mint-wash background (`{colors.primary-surface}` #edfcf3) with dark green text (`{colors.primary-active}`), uppercase at 11px. Sits top-right on product cards or inline on configurator options.

**`badge-out-of-stock`** — Pink-wash (`{colors.alert-surface}`) with `{colors.alert}` text. Same geometry as in-stock badge but signals unavailability immediately through color contrast against the dark canvas.

**`badge-sale`** — Solid `{colors.alert}` (#ff6476) fill with white text. Used sparingly on clearance items and flash-sale heroes.

### Price Display

**`price-block`** — Large price rendered in `{typography.price-display}` (32px, weight 800) with tight negative tracking. Dollar sign prefix in `{colors.muted}` at smaller weight to reduce visual noise. Sale variant strikes through the original in `{colors.muted}` and renders the new price in `{colors.alert}`.

### Hero Banner

**`hero-banner`** — Full-viewport dark section (min 85vh) with product photography or 3D renders composited against `{colors.canvas}`. A bottom gradient fades imagery into the page. Headline in `{typography.display-xl}` (56px, weight 800) with -1.5px tracking. CTA button primary centered or left-aligned below a one-line subtitle in `{typography.body-lg}`.

### Search

**`search-bar`** — Compact 44px input with magnifying-glass icon in `{colors.muted}`, `{rounded.xs}` corners, and `{colors.surface-card}` fill. Focus state swaps border to `{colors.primary}`. Positioned in nav or as an expanding overlay on mobile.

### Footer

**`footer`** — Full-width section on `{colors.canvas}` separated by a single `{colors.hairline-soft}` border. Four-column grid on desktop (Products, Support, Company, Legal) collapsing to accordion on mobile. Link text in `{typography.body-sm}` / `{colors.muted}`, hovering to `{colors.ink}`. Social icons render at 20px in `{colors.muted}`, transitioning to `{colors.primary}` on hover.

### Tooltip

**`tooltip`** — Small overlay on `{colors.surface-elevated}` with `{rounded.xs}` corners, used to explain spec abbreviations and component compatibility notes in the configurator. Appears on hover/focus with a 4px 16px dark shadow for depth separation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + slide-out drawer; configurator stacks vertically with full-width option rows; hero headline drops to `{typography.display-sm}` (28px); footer columns collapse to accordions; price display reduces to 24px |
| Tablet | 744–1128px | Two-column product grid; nav remains horizontal but drops less-critical links into overflow menu; configurator shows 2-column option grid; hero maintains large type but reduces min-height to 70vh |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with all links visible; configurator uses sidebar layout (options left, live preview right); hero at full 85vh with centered composition |
| Wide | > 1440px | Content max-width caps at 1440px centered; four-column product grid on collection pages; configurator gains extra whitespace between option groups; hero image scales but text size holds at display-xl cap |

### Touch Targets

- All interactive elements maintain minimum 44px touch target on mobile and tablet
- Configurator option rows expand to 56px height on touch devices for reliable thumb tapping
- Nav hamburger icon area is 48×48px minimum
- Close/dismiss buttons on modals and drawers are 44×44px with generous padding from edges
- Price and spec text remains minimum 14px on all breakpoints for readability

### Collapsing Strategy

- Product grid reduces columns (4 → 3 → 2 → 1) rather than shrinking card width below 280px
- Configurator transitions from side-by-side (panel + preview) on desktop to stacked (panel above, preview below or hidden behind tab) on mobile
- Navigation shifts from full horizontal bar to hamburger drawer below 744px; logo remains fixed-left
- Spec tables switch from two-column horizontal layout to stacked label-above-value on mobile
- Footer transitions from 4-column grid to single-column accordion with expandable sections
- Hero CTAs stack vertically on mobile with full-width buttons

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font family could not be reliably extracted (only `inherit` detected); the site likely loads custom fonts via JavaScript bundles or dynamic CSS injection — the Inter/Roboto system stack used here is a reasonable approximation of the geometric sans visible on the live site but may not match exactly
- Exact border-radius values could not be confirmed from static extraction; `{rounded.xs}` (4px) is inferred from the sharp, machined aesthetic visible in screenshots
- Animation/transition timing (hover durations, ease curves) not extractable from color/font hints
- Dark mode is assumed as the only mode based on the #080707 canvas dominance; if a light-mode toggle exists, its tokens are not captured here
- Exact nav height, button heights, and padding values are best-guess based on gaming-industry conventions and visual proportion — verify against live DOM measurements
- The indigo (#6172f3) and pink (#ff6476) color roles are inferred from their position in the extracted spectrum; actual usage contexts (loyalty tiers, alerts, promotions) should be confirmed against live UI states
- No icon system or illustration style data was extractable
