---
version: alpha
name: "Jensen Outdoor"
source_url: "https://www.jensenoutdoor.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep navy (#272c51) dominates the header band and footer slab like the twilight edge of a teak table caught in low evening light — a color dark enough to feel architectural but warm enough (via its purple undertone) to avoid the clinical sterility of pure black outdoor-brand defaults. Display type runs in Parisine Std Narrow, a compressed humanist face originally designed for Parisian transit signage, lending headings a European industrial pedigree that pairs unexpectedly well with the organic grain of outdoor timber photography. Body and UI text shifts to Poppins at 400–500 weight with generous line-height (1.6+), creating a visual breath between dense product specification tables. The active CTA blue (#1890d7) is tuned warmer than a standard link blue — closer to swimming-pool cerulean — giving "Add to Cart" and configurator actions a poolside associative nudge without reading as hyperlink-generic. Card surfaces float on a pale canvas (#f0f0f0) with `{rounded.sm}` corners, subtle enough that furniture photography bleeds edge-to-edge; only interactive containers like the material-selector pills and search fields take `{rounded.full}`. A dark teak-brown (#382110) appears in category badges and hover underlines, anchoring the palette to physical material rather than digital abstraction. Spacing runs generous throughout — `{spacing.section}` separates lifestyle hero from product grid, and individual cards sit in `{spacing.lg}` gutters even at tablet breakpoints, refusing to crowd imagery that needs to breathe. The overall system reads as a print catalogue digitized with restraint: generous whitespace, limited color vocabulary, and a type hierarchy that trusts photography to do the emotional selling while text stays informational and crisp.

colors:
  primary: "#272c51"
  primary-active: "#1c2040"
  primary-disabled: "#9a9db3"
  accent-blue: "#1890d7"
  accent-blue-active: "#1478b3"
  accent-blue-disabled: "#a3d4ef"
  teak-brown: "#382110"
  teak-brown-light: "#5c3a24"
  ink: "#1e1f26"
  body: "#444444"
  muted: "#555d66"
  muted-soft: "#7a7f87"
  hairline: "#e2e4e7"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  surface-warm: "#faf8f5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#02e49b"
  warning: "#ff9900"
  error: "#ea4434"

typography:
  display-xl:
    fontFamily: "'parisine-std-narrow', 'century-gothic', 'Poppins', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'parisine-std-narrow', 'century-gothic', 'Poppins', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'parisine-std-narrow', 'century-gothic', 'Poppins', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'parisine-std-narrow', 'century-gothic', 'Poppins', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Poppins', 'century-gothic', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'century-gothic', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'century-gothic', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Poppins', 'century-gothic', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', 'century-gothic', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', 'century-gothic', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', 'century-gothic', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Poppins', 'century-gothic', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-lg:
    fontFamily: "'Poppins', 'century-gothic', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Poppins', 'century-gothic', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', 'century-gothic', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Poppins', 'century-gothic', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  uppercase-tag:
    fontFamily: "'Poppins', 'century-gothic', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Poppins', 'century-gothic', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
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
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.accent-blue-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.accent-blue-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.button-md}"
    padding: 8px 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.accent-blue}
  text-input-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline}
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: 0 2px 8px rgba(30,31,38,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0
    imageAspectRatio: 4/3
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.body-md}"
    gap: "{spacing.md}"
  product-card-hover:
    boxShadow: 0 8px 24px rgba(30,31,38,0.1)
    transform: translateY(-2px)
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-lg}"
    minHeight: 560px
    padding: "{spacing.section-lg} {spacing.xl}"
    overlayGradient: linear-gradient(180deg, rgba(39,44,81,0.6) 0%, rgba(39,44,81,0.2) 100%)
  hero-split:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
    imagePosition: right
    contentMaxWidth: 540px
  category-badge:
    backgroundColor: "{colors.teak-brown}"
    textColor: "{colors.on-primary}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  material-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: 1px solid {colors.hairline}
  material-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    border: 1px solid {colors.primary}
  collection-header:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    textAlign: center
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    rowBorder: 1px solid {colors.hairline-soft}
    padding: "{spacing.md} {spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.nav-link}"
    padding: "{spacing.section} {spacing.xl}"
    columnGap: "{spacing.xxl}"
  footer-newsletter:
    backgroundColor: rgba(255,255,255,0.1)
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  image-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    thumbnailSize: 72px
    thumbnailRounded: "{rounded.xs}"
    thumbnailBorderActive: 2px solid {colors.accent-blue}
    gap: "{spacing.sm}"

## Components

### Buttons
**`button-primary`** — Cerulean blue (#1890d7) fill with white text and barely-there `{rounded.xs}` corners, producing a clean rectangular CTA that doesn't compete with the organic curves of furniture photography. On hover, darkens to `{colors.accent-blue-active}`; disabled state washes to a pale sky tone. Used for "Add to Cart," "Request Quote," and primary form submissions.

**`button-secondary`** — White fill framed by a 2px navy (#272c51) border. On hover the fill inverts to solid navy with white text, creating a satisfying snap between states. Deployed for "View Collection," "Compare," and secondary navigation actions where the blue CTA would be too aggressive.

**`button-tertiary`** — Text-only link-style button in accent-blue with underline decoration. Used inline within content blocks for "Learn more" and "See all materials" affordances.

### Navigation
**`nav-bar`** — 72px-tall white bar with a single hairline bottom border. Logo sits left, primary nav links center in `{typography.nav-link}` (Poppins 500), utility icons (search, account, cart) cluster right. On scroll, the hairline drops away and a soft box-shadow appears via `nav-bar-scrolled`. Mega-menu dropdowns for collections use a full-width panel with `{colors.surface-warm}` background.

### Product Cards
**`product-card`** — Edge-to-edge lifestyle image at 4:3 ratio with `{rounded.sm}` container corners. Title in `{typography.title-sm}`, price in `{typography.body-md}`, no visible border — elevation comes only on hover via shadow and subtle upward translate. Cards never show star ratings or promotional badges; the system trusts photography exclusivity over information density.

### Hero Sections
**`hero-banner`** — Full-bleed lifestyle photography overlaid with a navy gradient scrim, white display type at `{typography.display-xl}`, and a single CTA button. Minimum 560px height ensures cinematic framing even on ultrawide monitors.

**`hero-split`** — Warm off-white (`{colors.surface-warm}`) background with a two-column layout: left column holds headline at `{typography.display-lg}` plus body text and CTA; right column holds a product lifestyle image that bleeds to the container edge.

### Category & Material Selectors
**`category-badge`** — Small teak-brown pill with uppercase white text, used to tag products by wood type or collection series. Appears on product cards and within filter panels.

**`material-pill`** — Rounded-full capsule (`{rounded.full}`) with light gray fill and hairline border. Active state flips to solid navy fill with white text. Used in product detail pages to select cushion fabrics, frame finishes, or table sizes.

### Collection Header
**`collection-header`** — Center-aligned block on warm surface background. Collection title in `{typography.display-md}`, optional subtitle in body weight below. Provides clear hierarchy above the product grid without visual heaviness.

### Specification Table
**`spec-table`** — Alternating-row table for product dimensions, materials, and care instructions. Header cells use `{typography.spec-label}` (13px, weight 500), body cells use `{typography.body-sm}`. Rows divided by `{colors.hairline-soft}` borders, no outer border.

### Search
**`search-bar`** — Pill-shaped (`{rounded.full}`) input on soft gray background. Magnifying-glass icon in muted gray on the left, placeholder text in `{typography.body-md}`. Expands on focus with a blue border ring matching `{colors.accent-blue}`.

### Footer
**`footer`** — Solid navy (#272c51) background spanning full width. Four-column layout with link groups in `{typography.nav-link}`, newsletter signup block inset with semi-transparent white background, and legal text in `{typography.caption}` at the bottom.

### Image Gallery
**`image-gallery`** — Product detail page gallery with a main image slot (soft gray background, `{rounded.sm}`) and a horizontal thumbnail strip below. Active thumbnail takes a 2px accent-blue border. Thumbnails are 72px squares with `{rounded.xs}` corners.

### Breadcrumb
**`breadcrumb`** — Horizontal path trail in `{typography.caption}` with muted-gray links, "/" separators in hairline color, and the current page in ink-black without a link treatment.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + slide-out drawer; hero reduces to 360px min-height with stacked text/image; material pills scroll horizontally; footer collapses to accordion sections; spec-table becomes stacked label/value pairs |
| Tablet | 744–1128px | Two-column product grid with `{spacing.lg}` gutters; nav shows primary links, utility icons remain; hero-split stacks vertically with image above content; footer moves to two-column grid |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with mega-menu dropdowns; hero-banner at full 560px height; footer four-column layout; image gallery shows 5 thumbnails |
| Wide | > 1440px | Content max-width caps at 1440px and centers; product grid may extend to four columns on collection pages; hero imagery scales proportionally; generous `{spacing.section-lg}` vertical rhythm between page sections |

### Touch Targets
- All interactive elements maintain 44px minimum touch target on mobile, even when visually smaller
- Material pills expand to 44px height on touch devices with increased horizontal padding
- Nav hamburger icon touch area extends to 48×48px
- Product card tap area covers the full card surface, not just the image or title

### Collapsing Strategy
- Navigation: full link bar → condensed priority links → hamburger drawer (icons for search/cart persist at all breakpoints)
- Product grid: 4-col → 3-col → 2-col → 1-col, maintaining consistent card aspect ratio
- Hero sections: overlaid text on image → stacked vertical layout with image constrained to 50vh
- Spec tables: horizontal rows → vertical stacked key/value blocks with full-width dividers
- Footer newsletter: inline input + button → stacked full-width input then button below

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Many extracted hex values (#5865f2, #02e49b, #e94c89, #f00075, #0866ff, #f6405f, etc.) are almost certainly social-media icon colors or third-party widget defaults rather than brand tokens — excluded from the palette
- No CSS custom properties or design-token JSON was extractable; color assignments are inferred from frequency and context positioning
- Exact font weights for parisine-std-narrow could not be confirmed (likely 400/700 only based on Adobe Fonts availability)
- Interaction motion/easing curves (transition durations, hover animations) were not captured
- Exact icon set unconfirmed — likely a custom SVG sprite or Feather/Lucide subset given the outdoor-luxury context
- Product configurator (if present) may use additional accent colors or UI patterns not visible on initial page load
- The #ff9900 orange may be an Amazon integration badge rather than a brand token; included only as `{colors.warning}` utility
