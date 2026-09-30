---
version: alpha
name: "Cayl"
source_url: "https://www.cayl.co.kr"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  #54473f — the color of dried clay after rain, of mountain sediment compacted by elevation — is Cayl's primary surface, and the refusal of spectacle it represents is the brand's clearest design statement. Where performance-gear competitors reach for high-vis orange or branded safety yellow, Cayl builds its primary CTA and active states from a muted ash-brown, the same neutral that technical garments take on after a season of genuine use. The full palette doubles down on this restraint: body text runs in #555555 rather than a high-contrast near-black, hairlines hold at #d9d9d9 and #e8e8e8, and the accent — #008bcc, a functional cerulean — exists not as brand voltage but as a navigation signal, appearing where precision pointing matters and disappearing everywhere it doesn't. The deeper #226699 steps in for link hierarchy, creating a two-tier link system that is operational rather than expressive.

  Typography is entirely Pretendard, the contemporary Korean sans-serif whose engineering spans Hangul and Latin with equal optical precision. The weight range is intentionally compressed: 400 for prose, 600 for labels and buttons, 700 for display sizes only. No condensed face for urgency, no slab serif for editorial register, no italic for emphasis. Hierarchy is established through scale — 40px display down to 11px uppercase label — and color value rather than typeface switching, reflecting a design culture that trusts material evidence over ornament.

  Buttons sit on {rounded.sm} corners — a 4px radius that reads barely soft in isolation but nearly square in context, appropriate for a brand whose products are built with box stitching and flat seams. Cards are flush-cornered, imagery-forward, with no drop shadows. The nav bar is flat white with a single hairline divider, no sticky shadow on scroll, no mega-menu. Badges appear sparingly — 'NEW' in {typography.label-upper}, tracked uppercase at 11px, applied without multicolor or iconographic noise. The footer is the one surface where the earth-brown primary fills the full width, making it feel grounded and resolved rather than simply closing a page. Size selectors and color swatches follow the same grammar: square or minimally rounded tiles, ink borders on selection, no animation flourish.

colors:
  primary: "#54473f"
  primary-active: "#3a3028"
  primary-disabled: "#a8998f"
  ink: "#333333"
  body: "#555555"
  muted: "#bbbbbb"
  hairline: "#d9d9d9"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#008bcc"
  accent-deep: "#226699"

typography:
  display-xl:
    fontFamily: "Pretendard, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Pretendard, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "Pretendard, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.1px
  title-sm:
    fontFamily: "Pretendard, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Pretendard, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Pretendard, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Pretendard, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-upper:
    fontFamily: "Pretendard, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "Pretendard, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Pretendard, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  price:
    fontFamily: "Pretendard, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-item:
    fontFamily: "Pretendard, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
    padding: 11px 23px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 9px 16px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    focusBorderColor: "{colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-item}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 24px
  product-card:
    backgroundColor: "{colors.canvas}"
    imageRatio: "4:5"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    captionTypography: "{typography.caption}"
    mutedTextColor: "{colors.muted}"
  hero-section:
    textColor: "{colors.canvas}"
    imageOverlay: "linear-gradient(to bottom, rgba(0,0,0,0.0) 50%, rgba(0,0,0,0.5) 100%)"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 80vh
    ctaMarginTop: "{spacing.xl}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: "3px 6px"
  product-badge-sale:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: "3px 6px"
  category-filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "7px 14px"
    height: 36px
  category-filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: none
    padding: "7px 14px"
    height: 36px
  size-selector-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
    selectedBackground: "{colors.ink}"
    selectedTextColor: "{colors.canvas}"
    unavailableTextColor: "{colors.muted}"
    height: 40px
    minWidth: 48px
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    border: "1.5px solid transparent"
    activeBorder: "1.5px solid {colors.ink}"
    gap: "{spacing.xs}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    height: 44px
    padding: 0 14px
    iconColor: "{colors.muted}"
    focusBorderColor: "{colors.ink}"
    focusBorderWidth: 1px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.lg}"
    borderTop: none

## Components

### Buttons

**`button-primary`** — Earth-brown (#54473f) fill with white text, 48px tall on a 4px-radius square. The active state darkens to `{colors.primary-active}` (#3a3028); disabled fades to `{colors.primary-disabled}` (#a8998f). No drop shadow at any state — solidity communicates through color and proportion alone, not elevation.

**`button-secondary`** — White fill with a 1px primary-brown border and matching text, geometrically identical to primary. Hover inverts to brown fill and white text in a clean swap, no tinted intermediary state.

**`button-ghost`** — Transparent fill with hairline border (#d9d9d9) and body-gray text, 40px tall. Used for low-priority utility actions — wishlist, share, back navigation — where the button should recede behind the primary interaction.

### Nav Bar

**`nav-bar`** — Flat white at 56px, separated from page content by a single 1px hairline (#d9d9d9). No sticky shadow on scroll — the nav floats above content without adding depth. Logo sits left at 24px height; category links (Trail, Mountain, Urban, Archive) run center in 14px weight-500 Pretendard; cart and search icons sit right as bare ink glyphs. On mobile, categories collapse into an off-canvas hamburger drawer.

### Product Card

**`product-card`** — Fully flush-cornered (`{rounded.none}`) in a 4:5 image ratio with no surface lift above canvas — images lay directly onto the white grid. Below the image: product name in `{typography.title-sm}`, terrain/colorway label in `{typography.caption}` muted, price in `{typography.price}` weight-700. Badge slot occupies top-left of image. On hover, a secondary product image crossfades; no zoom or scale transform.

### Hero Section

**`hero-section`** — Full-bleed photography with a bottom-half gradient darkening to rgba(0,0,0,0.5), preserving white headline legibility. Headline runs `{typography.display-xl}` at 40px weight-700; subhead in `{typography.body-md}`. A single `button-primary` sits below subhead with `{spacing.xl}` margin above it. Minimum height 80vh on editorial landings, 100vh on campaign features.

### Product Badges

**`product-badge`** — Flush-cornered label in primary brown with white uppercase text at 11px/0.8px tracking, 3px vertical padding. Sits top-left, overlaid on product card imagery. `product-badge-sale` uses `{colors.accent}` (#008bcc) cerulean — the single brand-blue surface in the product UI, functioning as a functional alert rather than a stylistic choice. Both badge types share identical geometry.

### Category Filter Chips

**`category-filter-chip`** — Pill-shaped (`{rounded.full}`) outlined chips for terrain and use-case filtering. Inactive state: hairline border, body-gray text on white fill. Active state: primary-brown fill, white text, border removed. The pill form deliberately contrasts with the square buttons and flush-cornered cards — softness is reserved for exploratory browsing, not purchase flow.

### Size Selector

**`size-selector-item`** — Nearly square tiles (40px height, 48px minimum width, `{rounded.xs}` 2px radius) arranged in a wrapping horizontal grid. Unselected: hairline border, ink text. Selected: full ink (#333333) fill, canvas text, no radius change. Unavailable sizes render in muted gray (#bbbbbb) with a diagonal strikethrough line. State transitions are instant — no animation.

### Color Swatch

**`color-swatch`** — 20px circular dots (`{rounded.full}`) in a horizontal row spaced at `{spacing.xs}`. Active selection gains a 1.5px ink-colored ring with a 2px transparent gap, creating an offset halo effect without a separate outline element. Earth tones and neutrals dominate the colorway range; swatch rows rarely exceed five options per product.

### Search Bar

**`search-bar`** — Soft gray fill (`{colors.surface-soft}`) at 44px height on `{rounded.sm}` corners. No border in resting state — the gray fill provides the affordance boundary. A search glyph icon sits at left in `{colors.muted}`; placeholder text matches. On focus, a 1px ink border appears. Sits inline in the nav on desktop; expands to a full-width bottom sheet on mobile.

### Footer

**`footer`** — The only full-width surface in primary earth-brown (#54473f), creating a strong visual ground for the page. All text reverses to white. Column headers use `{typography.label-upper}` uppercase tracking; body links use `{typography.body-sm}`. Social icons appear as bare white glyphs. No gradient, no image background — the earth-brown is used flat and total, the same way the color functions in the product palette as a resolved, weathered finish.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero drops to 60vh; filter chips scroll horizontally in a single row; size selector expands to full-width tile grid; CTA button spans full width |
| Tablet | 744–1128px | Two-column product grid; nav retains category links inline; hero at 70vh; filter chips wrap to two rows |
| Desktop | 1128–1440px | Three- to four-column product grid; nav fully horizontal; hero at 80vh; sidebar filter panel available on category pages |
| Wide | > 1440px | Grid holds at four columns; max-width container (1440px) centered; side margins fill with canvas white |

### Touch Targets

- All interactive elements minimum 44×44px on mobile
- Size selector tiles expand to 48px height on touch viewports
- Color swatches expand to 28px diameter on touch devices
- Nav bar height increases to 60px on mobile to clear logo and hamburger
- Category filter chips maintain 36px height with wider horizontal padding on touch

### Collapsing Strategy

- Primary nav collapses to off-canvas drawer sliding from left; overlay scrim at rgba(0,0,0,0.4)
- Category filter chips shift from wrapping row to horizontally scrolling single strip on mobile
- Product card image hover crossfade disabled on touch; tap navigates directly to product
- Footer columns stack to single column on mobile with accordion-collapsed link groups on narrow viewports
- Hero subhead and CTA stack vertically with reduced padding on mobile; headline scales to display-md

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Darkest ink/heading color not directly extracted — #333333 used as logical derivation; actual value may be #222222 or #555555
- primary-active (#3a3028) and primary-disabled (#a8998f) are derived from extracted primary #54473f; not confirmed from live site
- surface-soft (#f5f5f5) not present in extracted palette; derived from surrounding gray family
- No font weight distribution confirmed — 400/600/700 scale inferred from Korean DTC typographic conventions for Pretendard
- Exact nav bar height and logo lockup dimensions not measured from live site
- No motion or animation timing tokens extractable — transition durations absent from this spec
- Product card hover behavior (image swap vs. zoom vs. overlay) not confirmed from extraction
- #007aff in extracted palette is almost certainly an iOS system/browser default; excluded from design tokens
- Pricing currency format (KRW symbol placement, comma separators) and discount display pattern not confirmed
- Swiper-icons font stack is a Swiper.js carousel dependency, not a brand typography choice; excluded from typography system
