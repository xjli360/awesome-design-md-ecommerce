---
version: alpha
name: "Blendtec"
source_url: "https://www.blendtec.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Industrial red (#d6403d) punches through a near-black canvas (#111111) like a power button glowing on a commercial-grade motor housing — that single chromatic move anchors every CTA, sale badge, and "Add to Cart" moment on Blendtec's Shopify storefront. The site operates in a deliberately narrow tonal corridor: charcoal ink (#323232, #444444) over warm-cool neutrals (#f4f4f4, #e8e8e1), letting full-bleed product photography of brushed-steel jar assemblies and powder-coated bases do the heavy sensory lifting. A surprising pink accent (#ff82af) surfaces in promotional banners and seasonal callouts — a deliberate temperature shift that softens what is otherwise an engineering-forward palette and nods toward the smoothie-bowl, wellness-adjacent audience that buys a $500 blender for daily use rather than spectacle. Typography runs Lato at generous weights: display headings land bold at 600–700 in the 36–48px range with tight negative tracking, communicating precision engineering without the coldness of a condensed industrial face. Body copy at 400-weight and 16px breathes comfortably at 1.6 line-height — readable against both the dark hero sections and the light product-grid canvas. Buttons are confidently squared off with only `{rounded.xs}` softening, reinforcing the machine-tooled aesthetic; product cards take `{rounded.sm}` to separate content zones without looking playful. Spacing is generous throughout — `{spacing.section}` between content blocks, `{spacing.xl}` gutters on desktop grids — giving each blender model room to command attention the way a flagship appliance commands counter space. The navigation bar pins dark (#121212) with white logotype, establishing the "professional kitchen" atmosphere before a single pixel of content scrolls into view.

colors:
  primary: "#d6403d"
  primary-active: "#b8312e"
  primary-disabled: "#e8a09e"
  accent-pink: "#ff82af"
  accent-pink-active: "#e06b96"
  ink: "#111111"
  body: "#323232"
  muted: "#444444"
  muted-soft: "#717171"
  hairline: "#dedede"
  hairline-soft: "#e8e8e1"
  canvas: "#ffffff"
  canvas-dark: "#111111"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-warm: "#e8e8e1"
  surface-dark: "#121212"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-dark-muted: "#dedede"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Lato', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-bold:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Lato', -apple-system, system-ui, sans-serif"
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 15px 31px
    height: 52px
    border: 2px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-secondary-light:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 15px 31px
    height: 52px
    border: 2px solid {colors.on-dark}
  button-accent:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 14px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.ink}
  text-input-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 14px 16px
    height: 48px
    border: 1px solid {colors.muted}
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 40px
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    boxShadow: 0 2px 8px rgba(0,0,0,0.3)
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0
    imageAspectRatio: 1/1
    imageFit: contain
    imageBackground: "{colors.surface-soft}"
    contentPadding: "{spacing.base} {spacing.base} {spacing.lg}"
  product-card-hover:
    boxShadow: 0 4px 16px rgba(0,0,0,0.1)
    transform: translateY(-2px)
  hero-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 600px
    padding: "{spacing.section-lg} {spacing.xl}"
    textAlign: center
  hero-split:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    minHeight: 500px
    padding: "{spacing.section} {spacing.xl}"
    gridColumns: 1fr 1fr
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    cellPadding: "{spacing.md} {spacing.base}"
  feature-icon-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    iconSize: 48px
    textAlign: center
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    height: 40px
    padding: 0 {spacing.base}
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark-muted}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.md}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    boxShadow: 0 8px 32px rgba(0,0,0,0.12)
    padding: "{spacing.xl}"
  price-display:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  price-compare-display:
    typography: "{typography.price-compare}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  video-hero:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 80vh
    overlay: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4))

---

## Components

### Buttons

**`button-primary`** — A bold red (#d6403d) rectangle with barely-there rounding (`{rounded.xs}`) and uppercase Lato 700 tracking. Hover deepens to `{colors.primary-active}`, active state depresses 1px via translateY. Disabled state fades to `{colors.primary-disabled}` with reduced opacity. Used for "Add to Cart", "Shop Now", and primary conversion actions.

**`button-secondary`** — Transparent fill with a 2px solid ink border and uppercase ink-colored text. On hover the fill inverts to `{colors.ink}` with white text, creating a stark binary toggle effect. The light variant swaps to white border/text for use on dark hero backgrounds. Both share the same 52px height as primary buttons.

**`button-accent`** — The pink (#ff82af) variant reserved for promotional moments: seasonal sales, limited-edition launches, newsletter signup CTAs. Slightly smaller at 44px height to distinguish it from transactional primaries.

### Navigation

**`nav-bar`** — Fixed-position dark bar (#121212) spanning full viewport width at 64px height. Logo sits left in white, navigation links center in uppercase Lato 700 at 14px with generous letter-spacing (0.5px). Cart icon and account link anchor right. On scroll, a subtle box-shadow fades in to lift the bar off content.

**`mega-menu`** — Drops from nav on hover with category imagery and product quick-links arranged in a 3–4 column grid. White canvas background with a soft shadow keeps focus contained. Category headings use `{typography.title-sm}`, links use `{typography.body-md}`.

**`announcement-bar`** — Slim 40px red strip above nav promoting free shipping thresholds or active sales. White uppercase caption text, optionally animated with a horizontal ticker for multiple messages.

### Product Cards

**`product-card`** — Light gray surface (`{colors.surface-soft}`) with the product photographed on a clean background at 1:1 aspect ratio using `object-fit: contain`. Below the image, product name in `{typography.title-sm}`, price in `{typography.price}`, and a compare-at price struck through in muted gray when on sale. The `{rounded.sm}` corners and hover lift (translateY -2px with soft shadow) add just enough dimension without competing with the product imagery.

**`sale-badge`** — Small red pill overlaid at the top-left corner of product card images. "SALE" or percentage-off text in uppercase 11px bold white. Positioned with absolute offset of `{spacing.sm}` from card edges.

**`new-badge`** — Same dimensions as sale-badge but in accent pink (#ff82af), used for new product launches and restocked favorites.

### Heroes

**`hero-dark`** — Full-width dark canvas section with centered display-xl white text layered over blender product photography or looping video. Minimum 600px height ensures impact on desktop. Primary CTA centered below headline with `{spacing.lg}` gap.

**`hero-split`** — Two-column layout on desktop: left column holds headline (`{typography.display-lg}`) and body copy with CTA, right column holds a full-bleed product image or lifestyle shot. Collapses to stacked on mobile with image first.

**`video-hero`** — Full-viewport looping background video (typically the "Will It Blend?" content or product demonstrations) with a 40% dark overlay ensuring white text legibility. CTA floats center-bottom.

### Content Blocks

**`comparison-table`** — Side-by-side blender model comparison with model images at top, feature rows alternating white and `{colors.surface-soft}` backgrounds. Check/cross icons for boolean features, text values for specs. Sticky header row on scroll.

**`feature-icon-card`** — Centered icon (48px) above a short feature title and one-line description. Arranged in 3–4 column grids to communicate blender capabilities (power, noise level, jar material, warranty). Light background with `{rounded.sm}`.

### Form & Input

**`text-input`** — Standard 48px-height input with hairline border that sharpens to ink-black on focus. No border-radius beyond `{rounded.xs}`. Placeholder text in `{colors.muted-soft}`, filled text in `{colors.ink}`.

**`text-input-dark`** — Inverted variant for dark-background sections (newsletter signup in footer). Dark fill with muted border, white text.

### Footer

**`footer`** — Dark (#121212) multi-column layout with category headings in white `{typography.title-sm}` and link lists in muted gray `{typography.body-sm}` that brighten to white on hover. Social icons row, payment badge row, and legal links occupy the bottom band separated by a hairline border in `{colors.muted}`.

### Pricing

**`price-display`** — Bold 20px Lato in ink for the current price. When a compare-at price exists, it appears adjacent in 16px muted gray with a line-through, and the current price may optionally render in `{colors.primary}` to emphasize the deal.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2-up cards), hamburger menu replaces nav links, hero text drops to `{typography.display-md}`, comparison table scrolls horizontally, section padding reduces to `{spacing.xl}` |
| Tablet | 744–1128px | 3-column product grid, nav links visible but condensed letter-spacing, hero split stacks vertically, footer collapses to 2-column |
| Desktop | 1128–1440px | 4-column product grid, full mega-menu on hover, hero split side-by-side, comparison table fully visible, section padding at `{spacing.section}` |
| Wide | > 1440px | Content max-width caps at 1440px and centers, product grid may expand to 5 columns on collection pages, hero imagery scales to fill with fixed text sizing |

### Touch Targets

- All interactive elements maintain minimum 44×44px tap area on mobile
- Product cards receive full-surface tap target (entire card is clickable)
- Nav hamburger icon padded to 48×48px hit zone
- Quantity steppers in cart enlarged to 40×40px on touch devices
- Footer links spaced at minimum `{spacing.lg}` vertically for thumb reach

### Collapsing Strategy

- Desktop mega-menu converts to full-screen slide-out drawer on mobile with accordion category sections
- Comparison table locks first column (model name) and enables horizontal swipe for feature columns
- Hero split sections stack image-above-text on mobile, maintaining visual hierarchy
- Feature icon grids collapse from 4-column to 2-column at tablet, single-column at mobile
- Announcement bar text truncates with ellipsis on narrow viewports or cycles messages via auto-scroll
- Footer columns stack vertically in single column with collapsible accordion headings on mobile

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one font family (Lato) was detected; the site may load additional display or icon fonts via JavaScript bundles or Shopify theme asset pipeline that were not captured in static extraction
- No CSS custom properties or Shopify theme tokens were extracted — spacing and rounded values are inferred from common Shopify theme patterns and visual inspection conventions
- The exact hover/active state color shifts (primary-active, accent-pink-active) are interpolated from the base colors rather than extracted from computed styles
- Motion/animation tokens (transition durations, easing curves, parallax behaviors) could not be determined from static extraction
- Dark mode preferences or alternate color schemes may exist in theme settings but were not surfaced
- The relationship between #ff82af (pink accent) and seasonal campaigns vs. permanent brand usage is unclear — it may rotate with promotions
