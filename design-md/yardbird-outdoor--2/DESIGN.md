---
version: alpha
name: "Yardbird"
source_url: "https://yardbird.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Poolside teal (#7bc7c7) washes across every call-to-action and collection header like sunlight refracted through shallow water — an immediate signal that this is a brand built around the outdoor moment, not the showroom. Yardbird's digital presence runs on Montserrat in light-to-medium weights, keeping headlines at 600 weight and body copy at 400, which lends an architectural clarity that mirrors the clean geometry of their modular sofa frames. The palette extends through a gradient of ocean blues — steel (#7396a2), deep water (#5487a0), bright sky (#53b8d4) — layered against an extremely neutral gray system (#f3f3f3 to #f7f7f7 surfaces, #dedede hairlines) that never competes with large-format lifestyle photography. Dark text anchors at #121212 for headlines and #4d4d4d for body, with secondary text in #656565 providing comfortable reading contrast on those pale surfaces. Cards sit on pure white with generous `{spacing.lg}` padding and soft `{rounded.sm}` corners — enough softness to feel residential rather than commercial, but squared enough to communicate structural permanence. The frost-blue surface tone (#d8edf5) appears as a promotional banner backdrop and collection feature highlight, bridging the gap between the teal primaries and the neutral canvas. Navigation is minimal and wide-set, trusting the photography grid to do the selling. Product configuration tools — the heart of Yardbird's modular pitch — get the deepest interaction treatment: toggles and selectors carry `{rounded.full}` pill shapes in the primary teal, while material swatches sit in tight `{spacing.sm}` grids. The overall system reads as coastal-modern with zero ornamentation: no gradients, no shadows deeper than 4px blur, no texture overlays. Everything defers to the furniture itself.

colors:
  primary: "#7bc7c7"
  primary-active: "#5487a0"
  primary-disabled: "#d8edf5"
  ink: "#121212"
  body: "#4d4d4d"
  muted: "#656565"
  muted-soft: "#a8a8a8"
  hairline: "#dedede"
  hairline-soft: "#c9c9c9"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-frost: "#d8edf5"
  surface-card: "#ffffff"
  surface-warm: "#f3f3f3"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-ocean: "#53b8d4"
  accent-steel: "#7396a2"
  accent-deep: "#0e84c1"
  ink-warm: "#230d0d"
  link: "#1c64f6"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.3px
  button-lg:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.1px
  label:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.1px
  price:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  price-compare:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  uppercase-tag:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1.2px
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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    border: 1.5px solid {colors.ink}
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    border: 1.5px solid {colors.ink}
    height: 48px
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    border: 1px solid {colors.hairline}
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    border: 2px solid {colors.primary}
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
    boxShadow: 0 2px 4px rgba(0,0,0,0.04)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0
    overflow: hidden
  product-card-image:
    aspectRatio: 1 / 1
    objectFit: cover
    backgroundColor: "{colors.surface-warm}"
  product-card-body:
    padding: "{spacing.base} {spacing.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    comparePriceTypography: "{typography.price-compare}"
  hero-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-lg}"
  hero-banner-dark:
    backgroundColor: "{colors.ink-warm}"
    textColor: "{colors.on-dark}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-lg}"
  collection-header:
    backgroundColor: "{colors.surface-frost}"
    textColor: "{colors.ink}"
    padding: "{spacing.xxl} {spacing.xl}"
    headlineTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  material-swatch:
    width: 40px
    height: 40px
    rounded: "{rounded.full}"
    border: 2px solid transparent
  material-swatch-active:
    width: 40px
    height: 40px
    rounded: "{rounded.full}"
    border: 2px solid {colors.ink}
  configurator-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: 1px solid {colors.hairline}
  configurator-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: 1px solid {colors.primary}
  badge-sale:
    backgroundColor: "{colors.accent-ocean}"
    textColor: "{colors.on-primary}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    linkColor: "{colors.surface-soft}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    boxShadow: 0 8px 32px rgba(0,0,0,0.12)
    padding: "{spacing.lg}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: 1px solid {colors.hairline}
    padding: "{spacing.base} 0"
  testimonial-card:
    backgroundColor: "{colors.surface-frost}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    quoteTypography: "{typography.display-sm}"

---

## Components

### Buttons

**`button-primary`** — Full teal (#7bc7c7) background with white text and barely-rounded corners (`{rounded.xs}`). The tight 4px radius maintains the structural, furniture-like geometry of the brand. On hover, the background deepens to the steel-ocean #5487a0, creating a perceptible but non-jarring shift. Disabled state fades to the frost-blue #d8edf5 with reduced opacity, keeping the button visible but clearly inactive.

**`button-secondary`** — White fill with a 1.5px dark border and ink-colored text. This treatment appears on product pages for "Add to Wishlist" and comparison actions. On hover, the fill shifts to `{colors.surface-soft}` while the border stays solid. The secondary button always sits to the right of or below a primary CTA, never competing for visual hierarchy.

**`button-tertiary`** — Text-only with an underline in the deeper blue-teal, used for inline actions like "View Details" within feature grids or "Learn More" below body copy. No background, no border, minimal footprint.

### Navigation

**`nav-bar`** — A 72px-tall white bar with a single-pixel hairline bottom border. The Yardbird wordmark sits left; navigation links in Montserrat 500 weight are evenly spaced at center. Cart icon and account link anchor right. On scroll, the bar compresses to 64px and gains a subtle 4px box-shadow to separate from content below.

**`promo-banner`** — A 40px teal strip above the nav carrying promotional messaging (free shipping thresholds, seasonal sales) in small white uppercase text. It persists on scroll on desktop but collapses on mobile after the first viewport.

### Product Cards

**`product-card`** — A borderless card with `{rounded.sm}` corners and hidden overflow. The image area is a 1:1 square with a warm gray (#f3f3f3) placeholder behind lazy-loaded photography. Below the image, product title in `{typography.title-sm}`, price in `{typography.price}`, and a compare-at price struck through in muted gray. Hover lifts the card with a 4px translateY and a faint shadow (0 4px 12px rgba(0,0,0,0.06)). No border, no separator between image and text — the white background of the card body flows directly out of the image container.

### Hero

**`hero-banner`** — Full-bleed section with a minimum height of 560px. Photography dominates the left or right half (depending on layout variant); the text half sits on warm gray (#f3f3f3) or frost-blue (#d8edf5). Headlines run at `{typography.display-xl}` with a primary CTA button below. The dark variant (`hero-banner-dark`) inverts to #230d0d background with white text, used for seasonal campaigns.

### Collection Header

**`collection-header`** — A contained banner at the top of collection pages using the frost-blue surface (#d8edf5). Headline centered in `{typography.display-md}`, description below in body weight. The block has `{rounded.sm}` corners and generous vertical padding (`{spacing.xxl}`), creating a soft card-like container that separates the collection introduction from the product grid below.

### Configurator

**`configurator-pill`** — Pill-shaped option selectors (`{rounded.full}`) for choosing size, layout, and configuration options on product detail pages. Inactive pills have a hairline border and muted text; active pills flip to teal fill with white text. These sit in horizontal rows with `{spacing.sm}` gaps.

**`material-swatch`** — 40px circular swatches displaying fabric or finish colors. The active swatch gains a 2px ink-colored ring; inactive swatches show only the color fill with no visible border. Swatches are spaced at `{spacing.sm}` in a wrapping flex row.

### Badges

**`badge-sale`** — A compact uppercase tag in ocean-blue (#53b8d4) with white text, positioned absolutely in the top-left of product card images. Used for percentage-off callouts.

**`badge-new`** — Same dimensions as the sale badge but in solid ink (#121212) with white text. Applied to recently launched collections or products.

### Footer

**`footer`** — Dark ink background (#121212) with white/soft-gray text organized into four columns: Shop, About, Support, and Social. Link typography is `{typography.body-sm}` in `{colors.surface-soft}`, shifting to full white on hover. The footer includes a newsletter signup input with a teal submit button and social icon row. Vertical padding uses `{spacing.section}` for generous breathing room.

### Utility Components

**`search-overlay`** — A centered modal with `{rounded.sm}` corners and a deep box-shadow. The input auto-focuses with a 2px teal border on focus. Suggested results appear below in a scrollable list with product thumbnails, titles, and prices.

**`breadcrumb`** — Muted-gray text at `{typography.caption}` scale with chevron separators. The final (current) segment renders in ink color without a link. Used on product and collection pages, positioned between the nav and the page heading.

**`accordion`** — Used on product pages for specs, materials, and shipping info. Each row is separated by a hairline border. Title sits in `{typography.title-sm}` with a plus/minus icon aligned right. Content area uses `{typography.body-sm}` with `{spacing.base}` padding when expanded.

**`testimonial-card`** — Frost-blue background cards featuring customer quotes in `{typography.display-sm}` italic style, with attribution below in caption weight. Used in a horizontal scroll carousel on the homepage.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero stacks vertically (image above, text below); configurator pills wrap to 2 rows; footer stacks to single column; promo banner hides after scroll |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links only (mega-menu behind hamburger); hero shifts to 60/40 image/text split; collection header padding reduces to `{spacing.lg}` |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with dropdowns; hero at full 50/50 split; configurator inline beside product image; all footer columns visible |
| Wide | > 1440px | Content max-width caps at 1440px and centers; product grid at four columns with increased card spacing (`{spacing.lg}`); hero image scales but text area stays at readable line lengths (~65ch max) |

### Touch Targets

- All interactive elements maintain a minimum 44×44px tap area on mobile and tablet
- Material swatches scale up to 48px on touch devices with `{spacing.md}` gaps
- Configurator pills increase padding to 12px 20px on mobile for comfortable thumb selection
- Footer links gain 12px vertical padding between rows on mobile

### Collapsing Strategy

- Navigation mega-menu items collapse into an accordion-style slide-out drawer on mobile, grouped by category
- Product page configurator moves below the image carousel on mobile rather than beside it
- Homepage collection grid switches from a masonry/feature layout to a simple vertical stack with full-bleed images
- Testimonial carousel becomes a vertical card stack on mobile with swipe hint (partial next-card visible)
- Search transitions from an inline expandable input to a full-screen overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No CSS custom properties or design tokens file was directly accessible — color extraction relied on rendered pixel sampling; actual CSS variable names are unknown
- Montserrat weight range may extend beyond 400–700; variable font axes (if used) were not confirmed
- Exact box-shadow values on hover states are approximated — the site may use CSS transitions with different easing curves
- Icon system (likely SVG sprite or icon font beyond Glyphicons Halflings) was not fully catalogued
- Motion/animation tokens (transition durations, easing functions) were not extractable from static analysis
- Dark mode support is unknown — no prefers-color-scheme media queries were confirmed
- The #1c64f6 blue appears in the palette but its specific usage context (likely links or a third-party widget) was not pinpointed with certainty
