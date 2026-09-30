---
version: alpha
name: "Framework"
source_url: "https://framework.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Orange module rails click into a matte-aluminum chassis — that physical gesture of snapping an expansion card into place is the entire design language compressed into one interaction. Framework's digital presence mirrors the hardware philosophy: exposed structure, no decorative veneer, every element earning its pixel footprint. The brand orange (#FF6B00) appears sparingly — a single CTA, a progress indicator, an active state — never as a wash or gradient, always as a precise signal against vast white canvas (#FFFFFF) and deep carbon ink (#1A1A1A). Typography runs a tight geometric sans-serif stack (Inter) at restrained weights; display headings sit at 600 weight rather than 800, trusting letter-spacing and generous line-height to create hierarchy without shouting. Product photography dominates: exploded-view diagrams, close-ups of screw threads and copper heat pipes, shot on neutral gray (#F5F5F5) surfaces that recede behind the hardware. Cards use barely-there radii (`{rounded.xs}` at 4px), reinforcing the machined-edge precision of the physical product. The component grid aligns to an 8px baseline (`{spacing.sm}`) with section gaps at 64–80px, giving each module — configurator, specs table, expansion-card picker — room to breathe like components laid out on an anti-static mat. Navigation is flat and utilitarian: no mega-menus, no animated dropdowns, just a slim 64px top bar with text links in medium weight. The configurator — Framework's signature UI — stacks selectable cards vertically with radio-style selection states bordered in `{colors.primary}`, turning a purchase flow into a bill-of-materials. Footer and legal text drop to 13px caption weight, maintaining the engineering-document tone through the last pixel.

colors:
  primary: "#FF6B00"
  primary-active: "#E55E00"
  primary-disabled: "#FFD4B0"
  ink: "#1A1A1A"
  body: "#3D3D3D"
  muted: "#6B6B6B"
  muted-soft: "#9E9E9E"
  hairline: "#E0E0E0"
  hairline-soft: "#EEEEEE"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  surface-dark: "#1A1A1A"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  on-dark-muted: "#A0A0A0"
  success: "#2E7D32"
  warning: "#F9A825"
  error: "#D32F2F"
  configurator-selected: "#FF6B00"
  configurator-border: "#E0E0E0"
  badge-new: "#FF6B00"
  badge-preorder: "#1A1A1A"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.4px
  display-md:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  overline:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  spec-label:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  spec-value:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  mono:
    fontFamily: "'JetBrains Mono', 'SF Mono', 'Fira Code', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
  section-lg: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 48px
    border: 1px solid {colors.hairline}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.ink}
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.ink}
  text-input-error:
    border: 1px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline-soft}
    padding: 0 {spacing.xl}
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    imageAspect: 4:3
  product-card-hover:
    boxShadow: 0 4px 12px rgba(0,0,0,0.08)
  configurator-option:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base} {spacing.lg}"
    border: 1px solid {colors.configurator-border}
  configurator-option-selected:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.configurator-selected}
  configurator-option-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.hairline-soft}
    opacity: 0.6
  expansion-card-slot:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    width: 80px
    height: 80px
    border: 1px dashed {colors.hairline}
  expansion-card-slot-filled:
    backgroundColor: "{colors.canvas}"
    border: 1px solid {colors.hairline}
  specs-table-row:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    padding: "{spacing.md} 0"
    borderBottom: 1px solid {colors.hairline-soft}
  specs-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  specs-table-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section-lg} {spacing.xl}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-lg}"
  hero-section-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section-lg} {spacing.xl}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-lg}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.on-dark}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    headerTypography: "{typography.title-sm}"
    cellTypography: "{typography.body-sm}"
    cellPadding: "{spacing.base}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    linkColor: "{colors.on-dark-muted}"
    linkHoverColor: "{colors.on-dark}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    height: 40px
    padding: 0 {spacing.base}
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px 12px 44px
    height: 48px
    border: none
    focusBorder: 1px solid {colors.ink}
  sidebar-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    activeTextColor: "{colors.ink}"
    activeWeight: 600
    padding: "{spacing.sm} {spacing.base}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    fillColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  tooltip:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
---

## Components

### Buttons

**`button-primary`** — Solid orange (#FF6B00) rectangle with 4px radius and white text at 16px/500. Hover darkens to `primary-active`; disabled fades to a peach tint (`primary-disabled`) with no cursor change. Used exclusively for purchase CTAs and single primary actions per viewport — never stacked.

**`button-secondary`** — White fill with a 1px `hairline` border. On hover the border strengthens to `ink` and background shifts to `surface-soft`. Sits beside primary buttons for secondary paths like "Learn More" or "Compare."

**`button-dark`** — Inverted button for use on light hero sections where the primary orange would compete with product photography. Carbon-black fill, white text, same 4px radius.

**`button-text`** — Unadorned text link styled as a button; uses `primary` orange color with no background. Underline appears on hover. Reserved for tertiary actions and inline navigation prompts.

### Navigation

**`nav-bar`** — A minimal 64px strip pinned to the top with a subtle bottom hairline. Logo left, text links center-right at 14px/500 weight. Collapses to a hamburger icon below 744px. No background blur or transparency effects — the bar is opaque white.

**`nav-bar-dark`** — Carbon-black variant used on product landing pages where the hero image bleeds to the top edge. White text links, same 64px height.

### Product Cards

**`product-card`** — Light gray (`surface-soft`) rounded container with 8px radius holding a 4:3 product image, title in `title-sm`, and a brief spec line in `body-sm`. On hover, a subtle 4px box-shadow lifts the card. No border in default state.

### Configurator

**`configurator-option`** — The signature interaction pattern. Each hardware choice (RAM, storage, display) renders as a horizontal card with a 1px gray border. Selecting an option swaps to a 2px orange border (`configurator-selected`) with no other visual change — the border IS the selection state. Disabled options reduce opacity to 0.6 and show a dashed border.

**`configurator-option-selected`** — Active state with 2px orange border replacing the default 1px gray. Interior padding compensates for the extra border pixel to prevent layout shift.

### Expansion Card Slots

**`expansion-card-slot`** — An 80×80px square with dashed border representing an empty port slot in the configurator. Users drag or click to assign a module (USB-C, HDMI, storage). Filled state switches to solid border and shows the module icon centered.

### Specs & Comparison

**`specs-table-row`** — Two-column layout: left column uses `spec-label` (14px/500, muted color) and right column uses `spec-value` (14px/400, ink). Rows separated by `hairline-soft` bottom borders. No zebra striping.

**`comparison-table`** — Multi-column table with sticky header row in `title-sm`. Cell padding at 16px. Outer border uses `hairline` with internal column dividers in `hairline-soft`. Highlights differing specs with a subtle `surface-soft` background.

### Hero Sections

**`hero-section`** — Full-width white section with centered content. Display heading at 48px/600, subtitle at 18px/400 body text below, then a single CTA button. Product image occupies 60% of the width on desktop, stacks below text on mobile.

**`hero-section-dark`** — Carbon-black variant with white text. Used for flagship product launches where dramatic contrast against the aluminum hardware creates visual tension.

### Badges

**`badge-new`** — Small orange pill with white uppercase text at 12px/600. Applied to newly released products and expansion cards.

**`badge-preorder`** — Same form factor in carbon-black. Signals upcoming availability.

### Footer

**`footer`** — Dark background with four-column link grid in muted white (`on-dark-muted`). Links brighten to full white on hover. Bottom row contains legal text in `caption` and region selector. 64px vertical padding from content edge.

### Utility Components

**`announcement-bar`** — 40px orange strip above the nav bar for shipping notices, product launches, or sale events. White bold caption text, centered. Dismissible with an × icon.

**`search-input`** — Rounded 8px input with gray fill and a left-aligned magnifying glass icon. No visible border until focus, when a 1px `ink` border appears. Placeholder text in `muted`.

**`progress-bar`** — 4px tall bar with full-radius ends. Gray track with orange fill. Used in checkout flow and configurator completion indicators.

**`sidebar-nav`** — Vertical text list for documentation and support pages. Active item uses 600 weight in `ink`; inactive items use 400 weight in `body` color. No background highlight on active state.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column stack. Nav collapses to hamburger. Hero image stacks below text. Configurator options become full-width cards. Expansion card slots shrink to 64×64px. Specs table remains two-column but labels truncate. |
| Tablet | 744–1128px | Two-column grid for product cards. Configurator retains side-by-side layout. Hero splits 50/50 text-image. Nav links partially visible with overflow scroll. |
| Desktop | 1128–1440px | Full layout. Three-column product grid. Configurator shows all options without scrolling. Comparison table displays up to 4 products. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Side margins grow proportionally. Hero images scale up with higher-resolution assets. |

### Touch Targets

- All interactive elements maintain a minimum 44×44px touch area on mobile, even if the visual element is smaller (e.g., icon buttons pad their hit area with transparent space).
- Configurator option cards expand to full viewport width on mobile, providing ample tap surface.
- Close/dismiss buttons (announcement bar, modals) use 48px touch targets.

### Collapsing Strategy

- Navigation links collapse into a slide-out drawer (from left) below 744px; the drawer uses `surface-dark` background with `on-dark` text.
- Comparison tables scroll horizontally on mobile with a sticky first column showing product names.
- Specs tables remain intact but reduce padding from 16px to 12px on mobile.
- Footer columns collapse from four to two on tablet, then single-column accordion on mobile.
- Expansion card slot grid reflows from horizontal row to 2×2 grid on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extractable from the live site — likely loaded via JavaScript bundle or CSS custom properties injected at runtime. The orange `#FF6B00` is based on Framework's widely-documented brand color appearing in marketing materials and product imagery, but the exact production hex may differ.
- No font-family stacks were detected in static HTML. Inter is inferred from visual inspection and common usage in tech hardware sites; the actual typeface may be a custom cut or alternative geometric sans.
- Dark mode token set is not captured — Framework likely ships a dark theme given their developer audience, but toggle behavior and dark palette values are unavailable.
- Motion/animation tokens (transition durations, easing curves) are not documented.
- Exact configurator interaction states (drag behavior, keyboard navigation, error messaging) require JavaScript inspection.
- Community forum and marketplace styling (if applicable) may use a separate design system not reflected here.
- Icon library and illustration style tokens are not captured.
