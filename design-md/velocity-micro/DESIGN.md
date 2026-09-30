---
version: alpha
name: "Velocity Micro"
source_url: "https://www.velocitymicro.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Steel-blue (#486d97) glows against near-black panels the way a single RGB strip illuminates the interior of a hand-built tower — that restrained accent is the optical signature of a builder that ships machines one at a time, not by the container. The palette runs overwhelmingly dark: a #181818 canvas absorbs light on hero sections and product showcases while #262626 surfaces lift configurator cards just enough to separate them from the void. Where most gaming brands saturate every pixel, Velocity Micro keeps voltage in reserve, deploying #3086ab teal and #005a78 deep-ocean highlights only for interactive affordances — configure buttons, spec-highlight pills, and hover states on the nav bar. Typography is industrial and condensed: Roboto Condensed carries headlines at weight 700 with negative letter-spacing that mirrors the compressed geometry of a CNC-milled chassis, while Open Sans at 400/600 handles body copy and UI labels with quiet legibility. Corner radii stay minimal — `{rounded.xs}` on buttons and cards, `{rounded.none}` on hero banners — communicating precision engineering rather than consumer friendliness. The 80px top navigation holds a wordmark left-aligned against `{colors.dark-canvas}` with category links in `{typography.nav-link}` white type, each underscored on hover by a 2px `{colors.primary}` rule. Product cards stack a full-bleed system photograph over a `{colors.dark-surface}` spec block, price in `{typography.title-md}`, and a "Configure" CTA in `{colors.primary}` with `{colors.on-primary}` text. Section padding runs generous at `{spacing.section}` vertically, letting each build class breathe — the layout trusts the photography and the specs, not ornament.

colors:
  primary: "#486d97"
  primary-active: "#3086ab"
  primary-disabled: "#7a9ab8"
  ink: "#ffffff"
  ink-inverse: "#181818"
  body: "#d9d9d9"
  muted: "#777777"
  muted-soft: "#727272"
  hairline: "#474747"
  hairline-light: "#d9d9d9"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  dark-canvas: "#181818"
  dark-surface: "#262626"
  dark-elevated: "#2b2b2b"
  accent-navy: "#063950"
  accent-teal: "#005a78"
  accent-teal-bright: "#3086ab"
  success: "#5cb85c"
  warning: "#f0ad4e"
  danger: "#d9534f"
  info: "#5bc0de"

typography:
  display-xl:
    fontFamily: "'Roboto Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'Roboto Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -1px
  display-md:
    fontFamily: "'Roboto Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  title-lg:
    fontFamily: "'Roboto Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Roboto Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-lg:
    fontFamily: "'Open Sans', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'Roboto Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Roboto Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Open Sans', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  spec-label:
    fontFamily: "'Roboto Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price:
    fontFamily: "'Roboto Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  mono:
    fontFamily: "Consolas, 'Courier New', Menlo, Monaco, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-configure:
    backgroundColor: "{colors.accent-teal-bright}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.dark-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: 1px solid {colors.hairline}
  text-input-focus:
    backgroundColor: "{colors.dark-elevated}"
    textColor: "{colors.on-dark}"
    border: 1px solid {colors.primary}
  nav-bar:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 80px
    padding: 0 {spacing.xl}
  nav-bar-dropdown:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
  hero-banner:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section-lg} {spacing.xl}"
    rounded: "{rounded.none}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subhead:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
  product-card:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
    padding: 0
    overflow: hidden
  product-card-image:
    aspectRatio: 4/3
    backgroundColor: "{colors.dark-elevated}"
  product-card-body:
    padding: "{spacing.lg}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.on-dark}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.on-dark}"
  spec-badge:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.accent-teal-bright}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 6px 10px
  spec-table-row:
    backgroundColor: "{colors.dark-elevated}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
    border-bottom: 1px solid {colors.hairline}
  spec-table-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  configurator-panel:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
  configurator-option:
    backgroundColor: "{colors.dark-elevated}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
  configurator-option-selected:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    border: 1px solid {colors.primary}
    rounded: "{rounded.xs}"
  category-nav-item:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.md} {spacing.base}"
  category-nav-item-active:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    border-bottom: 2px solid {colors.primary}
  footer:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-md}"
    textColor: "{colors.on-dark}"
  alert-success:
    backgroundColor: "#dff0d8"
    textColor: "#3c763d"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  alert-warning:
    backgroundColor: "#fcf8e3"
    textColor: "#8a6d3b"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  alert-danger:
    backgroundColor: "#f2dede"
    textColor: "#a94442"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.dark-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 40px
    border: 1px solid {colors.hairline}

---

## Components

### Buttons

**`button-primary`** — A steel-blue (#486d97) rectangle with `{rounded.xs}` corners and uppercase Roboto Condensed lettering at weight 700. Hover lifts the background to `{colors.primary-active}` (#3086ab), producing a teal brightening that reads as electrical activation. Disabled state washes to `{colors.primary-disabled}` at 60% opacity, flattening the button into the dark surface it sits on.

**`button-secondary`** — Transparent fill with a 2px `{colors.primary}` border and white uppercase text. On hover the fill floods to `{colors.primary}` and text remains white — a clean inversion that keeps the visual weight balanced against adjacent primary CTAs. Used for "Learn More" and secondary navigation actions.

**`button-configure`** — The high-intent CTA that launches the system configurator. Uses `{colors.accent-teal-bright}` (#3086ab) to separate it from the standard primary palette, signaling that this action leads to a custom-build flow rather than a static page.

### Navigation

**`nav-bar`** — An 80px-tall strip of `{colors.dark-canvas}` (#181818) spanning full viewport width. Logo sits left; category links (Gaming, Workstation, Proton, Support) are set in `{typography.nav-link}` Open Sans 600. Hover state applies a 2px bottom rule in `{colors.primary}`. On mobile, the bar collapses to a hamburger icon with a slide-in panel using `{colors.dark-surface}` as the drawer background.

**`nav-bar-dropdown`** — Mega-menu panels that descend below the nav on hover, rendered in `{colors.dark-surface}` with no border-radius and a single `{colors.hairline}` top border. Product thumbnails display inline at 80x60px alongside model names in `{typography.body-sm}`.

### Hero

**`hero-banner`** — Full-bleed dark canvas section featuring a high-resolution product photograph (typically an angled chassis shot showing internal RGB lighting). Text overlay sits left-aligned with `{typography.display-xl}` headline, `{typography.body-lg}` subhead in `{colors.body}`, and a `button-primary` CTA. Vertical padding uses `{spacing.section-lg}` (96px) to give the composition room to breathe.

### Product Cards

**`product-card`** — A vertical card with `{rounded.xs}` corners and `{colors.dark-surface}` background. The top region holds a 4:3 product image on a `{colors.dark-elevated}` mat. Below, `{spacing.lg}` padding wraps the system name in `{typography.title-md}`, a one-line spec summary in `{typography.body-sm}` / `{colors.muted}`, the price in `{typography.price}`, and a `button-configure` CTA. Hover lifts the card with a subtle box-shadow (0 4px 16px rgba(0,0,0,0.4)).

### Spec & Configurator

**`spec-badge`** — Small pill-like labels displaying component brands or performance tiers (e.g., "RTX 5090", "i9-14900K"). Dark navy `{colors.accent-navy}` background with `{colors.accent-teal-bright}` text in `{typography.spec-label}` — uppercase, 11px, 1px letter-spacing. Used inside configurator panels and product detail pages.

**`configurator-panel`** — The primary container for build-option groups (Processor, GPU, RAM, Storage). `{colors.dark-surface}` background, 1px `{colors.hairline}` border, and `{rounded.xs}` corners. Each option row is a `configurator-option` item; selecting one transitions it to `configurator-option-selected` with an `{colors.accent-navy}` fill and `{colors.primary}` border highlight.

**`spec-table-row`** — Alternating specification rows inside product detail pages. `{colors.dark-elevated}` background, `{typography.body-sm}` value text, with the label column rendered in `{typography.caption}` / `{colors.muted}`. Rows are separated by a 1px `{colors.hairline}` bottom border.

### Alerts

**`alert-success`** / **`alert-warning`** / **`alert-danger`** — Standard notification bars using Bootstrap-derived background/text pairs (#dff0d8/#3c763d, #fcf8e3/#8a6d3b, #f2dede/#a94442). Applied to cart confirmations, out-of-stock warnings, and form validation messages. `{rounded.xs}` corners and `{spacing.base}` padding.

### Footer

**`footer`** — Full-width `{colors.dark-canvas}` section with `{spacing.section}` vertical padding. Four columns of links (Products, Support, Company, Legal) headed by `{typography.title-md}` in white, link text in `{typography.body-sm}` / `{colors.muted}`. A bottom bar carries copyright, social icons (Font Awesome), and payment badges.

### Search

**`search-bar`** — A compact 40px-tall input with `{colors.dark-elevated}` fill and `{colors.hairline}` border. Placeholder text in `{colors.muted}`, typed text in `{colors.on-dark}`. Focus state swaps the border to `{colors.primary}`. Positioned in the nav bar's right cluster on desktop; expands to full-width overlay on mobile.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Nav collapses to hamburger + slide drawer. Hero headline drops to `{typography.display-md}`. Product cards stack vertically full-width. Configurator options become full-width accordions. Footer columns stack. |
| Tablet | 744–1128px | Two-column product grid. Nav remains horizontal but drops less-used links into a "More" dropdown. Hero image scales; text overlay remains left-aligned. Configurator panel splits into two columns of options. |
| Desktop | 1128–1440px | Three-column product grid. Full horizontal nav with all category links visible. Hero uses max-width 1200px centered container. Configurator uses sidebar layout (options left, summary right). |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Product grid may extend to four columns. Hero image fills additional space while text container stays fixed-width. Generous lateral whitespace. |

### Touch Targets

- All interactive elements maintain minimum 44px tap target on mobile
- Configurator option rows expand to 52px height on touch devices
- Nav hamburger icon uses 48×48px hit area
- Card CTAs span full card width on mobile for easy thumb access

### Collapsing Strategy

- Navigation: full horizontal → condensed with "More" overflow → hamburger + slide panel
- Product grid: 4-col → 3-col → 2-col → 1-col stack
- Configurator: side-by-side (options | summary) → stacked with sticky summary footer
- Spec tables: remain full-width but scroll horizontally if columns exceed viewport
- Footer: 4-column grid → 2×2 grid → single-column accordion

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Many extracted colors (#337ab7, #5cb85c, #5bc0de, #f0ad4e, #d9534f, #3c763d, #8a6d3b, #a94442) are Bootstrap 3 framework defaults rather than intentional brand tokens — the site appears built on an older Bootstrap scaffold
- No CSS custom properties or design-token layer detected; all values are likely hardcoded in compiled CSS
- Roboto Black usage (exact weight 900 contexts) could not be confirmed from extraction alone — assumed for display-xl fallback
- Exact hero image dimensions, aspect ratios, and overlay gradient values were not captured
- Animation/transition timing functions and durations are unknown
- Exact breakpoint values are inferred from Bootstrap 3 conventions (768/992/1200) rather than confirmed custom values
- No theme-color meta tag present; PWA/mobile-browser chrome color is unspecified
- Icon system appears to mix Font Awesome 5 and legacy Glyphicons Halflings — migration state unclear
- Configurator interaction patterns (drag-to-reorder, radio vs. checkbox, pricing update behavior) require JS inspection not available from static extraction
