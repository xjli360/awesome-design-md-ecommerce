---
version: alpha
name: "System76"
source_url: "https://system76.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep indigo (#221155) pooling behind hero panels like a terminal session at dusk — that single chromatic bet is what separates System76's visual identity from the sea of silver-and-white hardware marketing. The color reads simultaneously as night-sky computing and defiant independence from mainstream OEMs, and it saturates full-bleed sections while product photography floats on lighter `{colors.surface-soft}` (#f5f5f5) cards. A secondary electric blue (#3c64f4) fires every call-to-action, drawing the eye against both the dark purple backgrounds and the pale product grids with equal urgency. Body text lives in a warm brown-charcoal (#574f4a) rather than pure black — a subtle humanist decision that softens the otherwise engineering-forward tone and keeps long spec sheets from feeling clinical. Typography inherits system sans-serif stacks, almost certainly loaded dynamically at runtime; the result on-page is a geometric, medium-weight face set at 16px body with generous line-height, leaning toward Fira Sans or similar open-source-friendly families. Corner radii stay modest: `{rounded.sm}` on buttons, `{rounded.md}` on cards, never fully rounded — the aesthetic says precision machined, not consumer bubbly. Spacing is generous vertically (`{spacing.section}` between feature blocks) but compact horizontally inside product grids, creating a rhythm that mirrors the dense-but-breathable layout of a well-configured IDE. Navigation is dark-on-light with category mega-menus (Laptops, Desktops, Accessories, Pop!_OS) that expand on hover rather than click, treating the top bar more like a filesystem tree than a retail nav.

colors:
  primary: "#221155"
  primary-active: "#1a0d44"
  primary-disabled: "#8878aa"
  accent: "#3c64f4"
  accent-active: "#2b4fd6"
  accent-disabled: "#a3b5f9"
  ink: "#574f4a"
  ink-strong: "#2d2926"
  body: "#574f4a"
  muted: "#7a726d"
  muted-soft: "#a39e9a"
  hairline: "#e0ddd9"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#221155"
  surface-dark-alt: "#1a0d44"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-accent: "#ffffff"
  success: "#2ecc71"
  warning: "#f39c12"
  error: "#e74c3c"

typography:
  display-xl:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  spec-value:
    fontFamily: "'Fira Mono', 'SF Mono', 'Cascadia Code', 'Consolas', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  nav-link:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.accent-disabled}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.accent}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
    border: 2px solid {colors.accent}
  button-secondary-active:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.sm}"
  button-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-dark-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
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
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.accent}
  text-input-dark:
    backgroundColor: "{colors.surface-dark-alt}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid rgba(255,255,255,0.2)
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline-soft}
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    boxShadow: 0 8px 32px rgba(34,17,85,0.12)
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    minHeight: 360px
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    boxShadow: 0 4px 20px rgba(34,17,85,0.1)
    transform: translateY(-2px)
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section-lg} {spacing.xl}"
    minHeight: 560px
  hero-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
  spec-table-row:
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    padding: "{spacing.md} 0"
    borderBottom: 1px solid {colors.hairline-soft}
  configurator-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    border: 1px solid {colors.hairline}
  configurator-option:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: 2px solid transparent
  configurator-option-selected:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 2px solid {colors.accent}
  badge-new:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-os:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  price-display:
    textColor: "{colors.ink-strong}"
    typography: "{typography.price}"
  price-starting:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: rgba(255,255,255,0.7)
    typography: "{typography.body-sm}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px 12px 44px
    height: 44px
---

## Components

### Buttons

**`button-primary`** — The primary action button uses the electric blue accent (#3c64f4) on a white label with `{rounded.sm}` corners and 600 weight text. On hover, it darkens to `{colors.accent-active}` with no border shift. Disabled state desaturates to `{colors.accent-disabled}` and drops cursor interactivity. Used for "Add to Cart", "Configure", and "Buy Now" flows.

**`button-secondary`** — A ghost-style button with a 2px solid blue border and transparent fill. On hover/active, it inverts to filled blue with white text. Maintains identical sizing to `button-primary` so the two sit side-by-side without vertical misalignment.

**`button-dark`** — Deep purple (#221155) fill with white text, reserved for high-emphasis CTAs on light backgrounds where the brand identity needs reinforcement — typically hero sections and promotional banners. Active state deepens to `{colors.primary-active}`.

**`button-ghost`** — Minimal button with no border or background, relying on text color and hover underline for affordance. Used inline in product grids and comparison tables where button density would create visual noise.

### Navigation

**`nav-bar`** — Fixed 72px white top bar with a thin `{colors.hairline-soft}` bottom border. Logo sits left, category links center, and utility icons (search, cart, account) right. Category links use `{typography.nav-link}` at 500 weight with a 2px bottom indicator on active state.

**`nav-mega-menu`** — Full-width dropdown that appears on category hover, never on click. Contains product thumbnails in a 3-4 column grid with model names below. Drops a soft purple-tinted shadow (rgba(34,17,85,0.12)) and has no border-radius, snapping flush to the nav bar bottom edge.

### Product Cards

**`product-card`** — Rectangular card on `{colors.surface-soft}` with `{rounded.md}` corners. Product image occupies the top 60% with transparent PNG on the gray background. Below: model name in `{typography.title-md}`, a one-line tagline in `{typography.body-sm}`, and starting price in `{typography.price}`. On hover, lifts 2px with a purple-tinted box-shadow.

### Hero Sections

**`hero-dark`** — Full-bleed deep purple (#221155) background with a large product render centered or offset to one side. Headline in `{typography.display-xl}` white, supporting copy in `{typography.body-lg}` at rgba(255,255,255,0.85). Minimum height 560px. CTA uses `button-primary` (blue on dark purple creates strong contrast).

**`hero-light`** — Light gray (#f5f5f5) background variant for secondary product features. Product photography is lifestyle-oriented (hands-on-keyboard, desk setup). Headline in `{typography.display-lg}` using `{colors.ink-strong}`.

### Configurator

**`configurator-panel`** — The hardware customization interface, presented as a white card with `{rounded.md}` and a thin border. Options are listed in groups (Processor, Memory, Storage, etc.) with group headers in `{typography.title-sm}`.

**`configurator-option`** — Individual spec choice presented as a selectable tile on `{colors.surface-soft}`. Shows component name, brief spec, and price delta. Selected state switches to white background with a 2px `{colors.accent}` border.

### Spec Table

**`spec-table`** — Technical specifications displayed in alternating label/value rows. Labels use `{typography.spec-label}` (500 weight sans-serif) and values use `{typography.spec-value}` (monospace for alignment of numbers and model strings). Rows separated by `{colors.hairline-soft}` borders.

### Badges

**`badge-new`** — Small uppercase pill in accent blue, used on product cards for recently launched models. Sits top-right of the product image with `{rounded.xs}` corners.

**`badge-os`** — Deep purple variant marking Pop!_OS or Ubuntu compatibility. Same sizing and placement rules as `badge-new`.

### Pricing

**`price-display`** — Bold 20px price in `{colors.ink-strong}`, always formatted with "Starting at" prefix in `{typography.caption}` muted color above it.

### Footer

**`footer`** — Deep purple background matching the hero-dark treatment. Four-column link grid with categories: Products, Support, About, Community. Links render at 70% white opacity, brightening to full white on hover. Bottom row contains legal links and social icons.

### Search

**`search-bar`** — Inset search field on `{colors.surface-soft}` with a magnifying glass icon left-padded at 16px. Focus state adds a 1px `{colors.accent}` border. Used in nav and support knowledge base.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu with slide-out drawer. Hero text drops to `{typography.display-md}`. Product grid becomes single-column stacked cards. Configurator options stack vertically. Footer columns collapse to accordion. |
| Tablet | 744–1128px | Product grid shifts to 2-column. Hero maintains full-bleed but image scales down. Nav keeps top-level links but mega-menu becomes scrollable dropdown. Configurator shows 2-column option grid. |
| Desktop | 1128–1440px | Full layout: 3-column product grids, mega-menu with thumbnails, side-by-side hero text + product image. Configurator panel sits beside product render. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Additional breathing room in hero sections. Product grid can expand to 4 columns for accessory pages. |

### Touch Targets

- All interactive elements maintain 44px minimum touch target on mobile
- Configurator option tiles expand to full-width tappable rows on mobile
- Nav hamburger icon is 48px square with generous hit area
- Product cards are entirely tappable (not just the title link)

### Collapsing Strategy

- Nav categories → hamburger drawer with nested accordion for sub-categories
- Product grid: 4-col → 3-col → 2-col → 1-col (wide → mobile)
- Spec tables maintain full width; cells wrap value text rather than truncating
- Configurator: side panel → below product image → full-width stacked
- Footer link columns → single-column accordion sections

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font family could not be reliably extracted (site returns `inherit`; fonts are loaded dynamically via JavaScript). The spec assumes Fira Sans based on System76's open-source alignment and visual similarity, but the actual loaded typeface may differ.
- Only 4 hex colors were extracted from the static page; interactive states, gradient values, and any additional accent colors (e.g., Pop!_OS orange tones) are not captured.
- No CSS custom properties or design tokens were extractable — the site likely uses a JS-rendered framework that injects styles at runtime.
- Icon system details (icon font vs SVG sprite vs inline SVG) could not be determined from static extraction.
- Exact animation/transition values (easing curves, durations) for hover states and page transitions are unknown.
- Dark mode toggle behavior, if any exists beyond the naturally dark hero sections, was not captured.
