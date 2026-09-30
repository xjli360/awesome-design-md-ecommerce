---
version: alpha
name: "Proclamation Goods"
source_url: "https://proclamationgoods.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Proclamation Goods Co. speaks in the quiet, confident tones of a heritage kitchen workshop, where every surface is a canvas of warm, earthy restraint. The brand's visual identity is anchored by a deep forest green (`#2a4532`) that acts as the primary voltage — appearing on buttons, navigation bars, and key product accents — against a parchment-like canvas (`#f4f2e6`) that feels tactile and aged, like a well-worn recipe card. This is not a sterile white kitchen; it's a space where light plays across matte surfaces, where a muted steel (`#dedede`) and a deep, almost-ink (`#121212`) provide structure without shouting. Two signature blues — a bright cerulean (`#1990c6`) and a deeper teal (`#136f99`) — appear sparingly as editorial accents, perhaps on sale badges or ingredient callouts, adding just enough cool contrast to the warm green-and-cream palette. The typography leans on two distinct voices: `matrix` for display headings, a serif that carries the weight of a hand-stamped label, and `sofia sans` for body text, a clean, approachable sans-serif that keeps product descriptions and navigation feeling modern but never cold. Rounded corners are generous but not pillowy — `{rounded.md}` (12px) on cards and `{rounded.lg}` (20px) on buttons — suggesting a brand that is friendly and tactile without sacrificing the craftsmanship implied by its name. The overall mood is one of curated simplicity: every element feels intentional, from the `{spacing.xxl}` (48px) breathing room around product grids to the soft `{hairline}` (`#dedede`) that separates sections without harshness. Proclamation Goods doesn't shout about quality; it lets the materials — the greens, the creams, the matte metals — do the talking.

colors:
  primary: "#2a4532"
  primary-active: "#1f3426"
  primary-disabled: "#a3b8a8"
  ink: "#121212"
  body: "#2a2a2a"
  muted: "#5a5a5a"
  muted-soft: "#8a8a8a"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#f4f2e6"
  surface-soft: "#ece8d8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#1990c6"
  accent-teal: "#136f99"
  badge-sale: "#1990c6"
  badge-new: "#136f99"
  star-rating: "#2a4532"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'matrix', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'matrix', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'matrix', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'matrix', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Sofia Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Sofia Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Sofia Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Sofia Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Sofia Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Sofia Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Sofia Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Sofia Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Sofia Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Sofia Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Sofia Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Sofia Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    rounded: "{rounded.lg}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.lg}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-icon-square:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid #c13515"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.xl}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  hero-heading:
    typography: "{typography.display-xl}"
    maxWidth: 600px
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 56px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xl}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's deep forest green (`{colors.primary}`) with white text and generous 20px rounded corners (`{rounded.lg}`). Uppercase, 15px Sofia Sans at 600 weight gives it a deliberate, crafted feel. On hover or active, it shifts to a darker green (`{colors.primary-active}`). The disabled state uses a muted sage (`{colors.primary-disabled}`) to signal unavailability without visual noise.

**`button-secondary`** — An outlined variant on the parchment canvas (`{colors.canvas}`) with a 2px solid green border. The text and border share the primary green, creating a cohesive but less dominant alternative to the filled button. Active state darkens both border and text. Ideal for secondary actions like "Learn More" or "Save for Later."

**`button-tertiary-text`** — A text-only button with no background or border, using the primary green for the label. Used for inline actions like "View All" or "Add to Cart" where a full button would feel heavy. Hover state adds a subtle underline.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with 12px rounded corners (`{rounded.md}`) and 16px padding. The product image sits at the top with 8px rounding, followed by the title in Sofia Sans 16px/500, and the price in 16px/400 body text. A small badge (sale or new) can be overlaid on the image, using the brand's accent blue or teal. The card feels tactile and clean, like a recipe card on a kitchen counter.

**`hero`** — A full-width section on the parchment canvas (`{colors.canvas}`) with generous 64px vertical padding. The heading uses the serif display-xl (36px, 700 weight) for a hand-stamped headline feel, while the subheading stays in Sofia Sans body-md for readability. The hero is intentionally sparse, letting the typography and the product photography carry the weight.

### Navigation
**`nav-bar`** — A fixed-height 72px bar on the canvas background, containing the logo and navigation links in uppercase Sofia Sans 14px/500. The active link is underlined with a 2px green border (`{colors.primary}`) and the text shifts to the primary green. The bar is uncluttered, with generous 32px horizontal padding.

**`nav-link`** — Uppercase, 14px, 500 weight Sofia Sans with 0.3px letter spacing. Inactive links use the ink color (`{colors.ink}`), active links use primary green. No background change on hover — just a subtle color shift to maintain the clean, editorial feel.

### Forms
**`text-input`** — A white input field with a 1px hairline border (`{colors.hairline}`) and 8px rounded corners. On focus, the border thickens to 2px and turns green. Error state uses a red border. The 48px height and 16px horizontal padding provide a comfortable tap target. Placeholder text uses the muted color (`{colors.muted}`).

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) on a white background with a 1px hairline border. At 56px tall with 24px horizontal padding, it's designed for both desktop and mobile use. On focus, the border becomes a 2px green ring. The shape is friendly and inviting, like a well-worn kitchen tool.

### Footer
**`footer`** — A deep green (`{colors.primary}`) footer section with white text. Links are set at 14px with 0.8 opacity, increasing to full opacity on hover. The footer uses the same generous spacing as the rest of the site (`{spacing.xxl}` vertical padding), maintaining the brand's commitment to breathing room. A subtle divider (`{colors.primary-active}`) separates link groups.

### Badges
**`badge-sale`** and **`badge-new`** — Small, uppercase 11px badges with 4px rounding (`{rounded.xs}`). Sale uses the bright cerulean (`{colors.accent-blue}`), new uses the deeper teal (`{colors.accent-teal}`). They sit on product card images or hero sections, adding a touch of editorial color without overwhelming the earthy palette.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, nav collapses to hamburger, hero padding reduces to 32px, product cards stack full-width, buttons become full-width, search bar reduces to 48px height |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, hero maintains 48px padding, search bar at 56px height |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, hero at 64px padding, search bar at 56px height |
| Wide | > 1440px | Max-width container at 1440px, centered content, hero heading max-width at 600px, product grid can expand to four columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px and minimum width of 44px.
- Icon buttons are 40px x 40px with 8px rounding.
- Search bar and text inputs are 48px minimum height.
- Navigation links have 32px minimum tap area (padding + height).

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses to a hamburger menu icon. The logo remains centered.
- Product cards stack in a single column on mobile, expanding to two columns on tablet and three on desktop.
- Hero sections reduce vertical padding from 64px to 32px on mobile.
- Footer link groups stack vertically on mobile, with a single column layout.
- The search bar reduces in height from 56px to 48px on mobile, and the pill shape remains but with reduced horizontal padding.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components (buttons, links, inputs) are inferred from common patterns; exact color transitions and durations are unknown.
- Error styling for forms (red border) is assumed; specific error message typography and iconography are not extracted.
- Dark mode is not present on the live site; no dark palette tokens are defined.
- Sub-brand or seasonal palettes (e.g., holiday collections) are not captured.
- The exact font weight for `matrix` display headings is assumed (700 for display-xl, 600 for display-md); actual weights may vary.
- The `sofia sans` font family may include variable weight support; only static weights are defined here.
- Animation durations and easing curves (e.g., button hover transitions) are not extracted.
- The `scrim` color is set to black but overlay opacity values for modals or drawers are unknown.
- Product card hover states (e.g., image zoom, shadow elevation) are not documented.
- The exact spacing between product grid items is assumed to be `{spacing.base}` (16px); actual gap may differ.
- The `star-rating` component uses the primary green color, but the exact star shape and spacing are not extracted.
