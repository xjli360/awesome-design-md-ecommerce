---
version: alpha
name: "Larq"
source_url: "https://www.livelarq.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Four pastel color pools — warm peach (#fce8d6), sky blue (#bee6fa), soft lavender (#e4d9fd), and watermelon coral (#f3756d) — divide the Larq site into product category lanes, each lit against a near-white (#f5f6fa) canvas and grounded by a single commanding navy (#153a5b). That navy, confirmed as the meta theme-color, functions as the brand's anchor point: it appears on primary buttons, the global nav, and the hero headline weight, pulling clinical technology toward a confident lifestyle register without sliding into the cold chrome of industrial filtration brands. The custom typeface, fontLarqGeologica — a geometric variable built on the Geologica family — carries all display work at generous weights (600–700) and slightly negative tracking, giving a certificate-of-quality legibility that sits between lab documentation and premium e-commerce copy. Rounded corners read as moderate and deliberate: product cards hold a 12px radius, buttons closer to 8px, never pill-shaped and never sharp — the geometry signals precision tooling rather than approachability-by-softness. The accent pastels double as section backgrounds and as product-family indicators: peach for the Bottle line, sky for Pitcher and Filter, lavender for subscription refill content, coral for limited colorway callouts. A secondary blue (#2299dd) handles interactive links and UI affordances while the deeper navy anchors authority. Gray neutrals (#5a5e60, #757575, #6f7477) form a layered ink system — darkest for primary body copy, mid for secondary labels, lightest for metadata and timestamps. Hairlines pull from the cool blue-gray end (#d9e2e9, #ccd7e0) to echo water-adjacent imagery without leaning photographic. The UV-C indicator glow is the product; the palette frames it.

colors:
  primary: "#153a5b"
  primary-active: "#0d2640"
  primary-disabled: "#ccd7e0"
  primary-light: "#f0f6ff"
  accent-blue: "#2299dd"
  accent-blue-mid: "#205ecc"
  accent-blue-soft: "#4c9fe9"
  accent-peach: "#fce8d6"
  accent-sky: "#bee6fa"
  accent-lavender: "#e4d9fd"
  accent-coral: "#f3756d"
  error: "#d02525"
  ink: "#5a5e60"
  body: "#757575"
  muted: "#6f7477"
  hairline: "#d9e2e9"
  hairline-soft: "#e5e5e9"
  canvas: "#fafafa"
  canvas-white: "#ffffff"
  surface-soft: "#f5f9fc"
  surface-card: "#f5f6fa"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'fontLarqGeologica', 'fontLarqGeologica Fallback', 'Geologica', sans-serif"
    fontSize: 60px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'fontLarqGeologica', 'fontLarqGeologica Fallback', 'Geologica', sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'fontLarqGeologica', 'fontLarqGeologica Fallback', 'Geologica', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'fontLarqGeologica', 'fontLarqGeologica Fallback', 'Geologica', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'fontLarqGeologica', 'fontLarqGeologica Fallback', 'Geologica', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'fontLarqGeologica', 'fontLarqGeologica Fallback', 'Geologica', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'fontLarqGeologica', 'fontLarqGeologica Fallback', 'Geologica', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'fontLarqGeologica', 'fontLarqGeologica Fallback', 'Geologica', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'fontLarqGeologica', 'fontLarqGeologica Fallback', 'Geologica', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  label-upper:
    fontFamily: "'fontLarqGeologica', 'fontLarqGeologica Fallback', 'Geologica', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.36
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "'fontLarqGeologica', 'fontLarqGeologica Fallback', 'Geologica', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.02em
  button-sm:
    fontFamily: "'fontLarqGeologica', 'fontLarqGeologica Fallback', 'Geologica', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.02em
  nav-link:
    fontFamily: "'fontLarqGeologica', 'fontLarqGeologica Fallback', 'Geologica', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  price:
    fontFamily: "'fontLarqGeologica', 'fontLarqGeologica Fallback', 'Geologica', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    border: "1.5px solid {colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoColor: "{colors.primary}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    imageBackground: "{colors.surface-soft}"
    imageRounded: "{rounded.md}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    subtitleTypography: "{typography.body-sm}"
    subtitleColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 600px
    padding: "{spacing.section} {spacing.xl}"
  category-lane-peach:
    backgroundColor: "{colors.accent-peach}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    labelTypography: "{typography.label-upper}"
    titleTypography: "{typography.display-md}"
  category-lane-sky:
    backgroundColor: "{colors.accent-sky}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    labelTypography: "{typography.label-upper}"
    titleTypography: "{typography.display-md}"
  category-lane-lavender:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    labelTypography: "{typography.label-upper}"
    titleTypography: "{typography.display-md}"
  feature-badge:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.accent-blue-mid}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    padding: 6px 12px
  uv-indicator:
    backgroundColor: "{colors.primary}"
    glowColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    width: 48px
    height: 48px
  product-color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.primary}"
  filter-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderActive: "1px solid {colors.primary}"
    backgroundActive: "{colors.primary-light}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  comparison-table:
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.title-sm}"
    rowBackgroundEven: "{colors.canvas-white}"
    rowBackgroundOdd: "{colors.surface-soft}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.ink}"
    borderColor: "{colors.hairline-soft}"
    rounded: "{rounded.md}"
  star-rating:
    filledColor: "{colors.primary}"
    emptyColor: "{colors.hairline}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    borderTopColor: "{colors.primary-active}"
    padding: "{spacing.xxl} {spacing.xl} {spacing.section}"

## Components

### Buttons

**`button-primary`** — Navy (#153a5b) fill, white text, 48px tall, 8px radius corners, 600-weight Geologica at 15px with 0.02em tracking. Hover darkens to #0d2640 via `button-primary-active`; disabled state pulls back to the blue-gray `primary-disabled` fill with white text. This is the dominant purchase-path CTA — "Shop Now," "Add to Cart," "Buy Now."

**`button-secondary`** — White fill with a 1.5px navy border and navy text, matching 48px height. Sits alongside `button-primary` on product pages for secondary paths like "Learn More" or "Compare Models."

**`button-ghost`** — Transparent fill with a 1.5px white border and white text, same 48px dimensions. Used exclusively on navy hero sections where a bordered white button reads cleanly against the dark surface.

**`button-small`** — 36px compact variant at 13px/600 Geologica, 4px radius. Appears on filter panels and dropdown menus for quick-action affordances with minimal visual weight.

### Inputs

**`text-input`** — White background, 1px hairline (#d9e2e9) border at rest, navy border on focus. 48px tall, 8px radius, 16px/400 Geologica body-md. Placeholder in muted gray (#6f7477). Shared by email capture, search, and checkout forms.

### Navigation

**`nav-bar`** — White background, 64px tall with a faint hairline-soft (#e5e5e9) bottom border. Brand logo in primary navy at left; product nav links in 14px/500 Geologica centered; cart icon and primary CTA at right. On scroll, gains a subtle drop shadow without changing fill color.

**`announcement-bar`** — Full-width navy strip at 40px height, 12px white caption text centered. Carries promotional copy ("Free shipping on orders over $75") and stacks above the nav-bar at the top of every page.

### Product Cards

**`product-card`** — Surface-card (#f5f6fa) background at 12px radius. Image area fills the upper portion against a cooler surface-soft (#f5f9fc) tint. Title in 16px/600 Geologica; price in 20px/700 directly below; subtitle copy in muted gray at 14px/400. On hover the card lifts with a box-shadow. Color swatches render as 24px `product-color-swatch` circles in a row beneath the title, with a 2px navy selection ring on the active choice.

### Hero

**`hero`** — Full-bleed navy (#153a5b) section, minimum 600px tall. Headline in display-xl (60px/700, -1px tracking) in white; supporting copy at body-md 16px/400. A `button-primary` and `button-ghost` pair renders side by side on desktop. Product photography floats over the right half on wide viewports with a soft #2299dd radial glow behind the bottle to evoke the UV-C emission.

### Category Lanes

**`category-lane-peach`**, **`category-lane-sky`**, **`category-lane-lavender`** — Pastel section blocks at 20px radius, each housing a product-family feature zone. An 11px uppercase 700-weight label with 0.08em tracking introduces the category; a 32px/600 display-md headline follows; body copy and a card grid or horizontal scroll complete the lane. Peach (#fce8d6) maps to the Bottle family; sky (#bee6fa) to Pitcher and Filter; lavender (#e4d9fd) to subscription and refill content.

### Badges and Labels

**`feature-badge`** — Full-radius pill with a light blue (#f0f6ff) fill and medium blue (#205ecc) text in 11px uppercase/700 Geologica with 0.08em tracking. Used inline with product imagery to call out claims: "UV-C Technology," "BPA-Free," "NSF Certified."

**`uv-indicator`** — 48px navy circle with a #2299dd glow ring rendered via box-shadow. Represents the active UV-C purification state. Appears on product detail pages and animated feature sections; meant to pulse on a timed interval to mirror the bottle's physical LED cycle.

### Filters and Comparison

**`filter-pill`** — Full-radius pill, surface-card fill with hairline border at rest; primary-light (#f0f6ff) fill with navy border when active. 13px/600 Geologica, 8px vertical padding. Used on collection pages to filter by volume (17oz, 32oz), material (stainless, Tritan), or technology (UV-C, filtered).

**`comparison-table`** — Navy header row with white 16px/600 type; alternating white and surface-soft (#f5f9fc) row fills; 12px radius wrapping the whole table. Check marks in primary navy, cross marks in muted gray (#6f7477). Primary use: Bottle vs. Pitcher comparisons and tiered subscription plan grids.

### Star Rating

**`star-rating`** — Five-star row, filled stars in primary navy (#153a5b), empty stars in hairline gray (#d9e2e9). Review count and aggregate score in 12px/400 muted gray beside the stars.

### Footer

**`footer`** — Navy (#153a5b) background with white copy. Column headings in 11px uppercase/700 Geologica with 0.08em tracking; nav links in 14px/400 body-sm. Four to five columns (Shop, Technology, Sustainability, Support, Legal) on desktop, collapsing to tap-to-expand accordion rows on mobile. Social icons in white along the bottom edge. A thin primary-active (#0d2640) line separates the footer from the body above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero headline drops to display-md (32px); nav collapses to hamburger drawer; product cards stack vertically at full width; category lanes go edge-to-edge; comparison table scrolls horizontally with sticky first column |
| Tablet | 744–1128px | Two-column product grid; hero splits 50/50 (text left, image right); nav links visible but condensed to icon + label; category lanes use 2-up card grid |
| Desktop | 1128–1440px | Three to four-column product grid; hero at full display-xl (60px); announcement bar + nav both visible; comparison table fully in-viewport |
| Wide | > 1440px | Max-width container (~1400px) centered with expanding gutters; hero image scales while text column stays at a fixed measure to preserve reading comfort |

### Touch Targets
- All buttons minimum 48px tall and 44px wide on mobile
- Product color swatches expand from 24px visible to 36px touch area via invisible padding ring
- Nav hamburger icon minimum 44×44px tap zone
- Filter pills minimum 36px tall on mobile with 8px vertical padding
- Star rating row minimum 44px tall tap zone for review navigation

### Collapsing Strategy
- Footer columns collapse into accordion panels on mobile; each heading row is a tap-to-expand trigger
- Comparison table wraps in a horizontal scroll container with the first product-name column position: sticky
- Category lane feature lists collapse to "See all features" expand toggle below three visible bullets on mobile
- Nav product submenus become a full-screen slide-in drawer on mobile; desktop hover opens a floating mega-panel

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border-radius not extracted from computed styles; 8px (`{rounded.sm}`) is estimated from visual inspection
- fontLarqGeologica is a brand-hosted variable font; exact wght axis range and optical size variants not confirmed
- Precise nav-bar scroll behavior (shadow depth, opacity ramp) not extractable from static hints
- Card hover animation timing and easing (transform, shadow) not captured
- UV-C indicator pulse interval and glow opacity not available from static extraction
- Image aspect ratios per card size (portrait vs. landscape crop) not confirmed
- Dark mode palette not observed; site appears light-mode only but this is unconfirmed
- "700px" appearing in extracted font stacks is a framework artifact, not a valid font-family; discarded
- Swiper-icons is a slider component icon font, not a brand face; excluded from the typography system
- Coral accent (#f3756d) role is inferred as limited-colorway callout; actual CMS usage not confirmed
