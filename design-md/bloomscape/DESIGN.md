---
version: alpha
name: "Bloomscape"
source_url: "https://bloomscape.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep forest green (#224229) saturates Bloomscape's header, footer, and primary CTAs like chlorophyll pooling at the edges of a leaf — the entire interface frames a warm parchment canvas (#fcf9f3) the way a glazed ceramic pot frames soil. Typography pairs Nib Pro, a high-contrast serif with calligraphic stroke terminals, against Circular's geometric neutrality; display headlines land in Nib Pro at weight 500–600 to convey botanical-catalog authority without heaviness, while body copy runs Circular at 16px/1.6 for long-form plant-care guides that read like magazine editorial. The bright accent green (#018342) fires on "Add to Cart" and quick-shop overlays — it sits mid-spectrum between the near-black primary and the warm peach tones (#f6cfb2, #f4c4a0) that tint promotional banners, seasonal gift badges, and hover states on lifestyle photography. Card radii stay at `{rounded.sm}` (8px), keeping product tiles orderly in a dense grid; buttons run `{rounded.xs}` (4px) for a squared-off nursery-label feel rather than the pill shapes common in beauty and wellness DTC. Spacing is generous — `{spacing.section}` (64px) separates collection rows, letting large square plant photographs breathe against the cream ground. A muted sage (#607765) handles secondary text and icon strokes, bridging the gap between the dark ink and bright whites without introducing a cold gray. The surface hierarchy layers three warm tones: pure canvas (#fcf9f3), a slightly cooler card white (#fdfcfa), and a deeper linen (#f8f1e3) for feature callouts and care-tip modules. Navigation is minimal — a sticky top bar in forest green with white wordmark and sparse utility icons — reflecting a curated catalog philosophy where the plant imagery, not the chrome, sells.

colors:
  primary: "#224229"
  primary-active: "#1a3320"
  primary-disabled: "#607765"
  accent: "#018342"
  accent-active: "#006b35"
  ink: "#224229"
  body: "#3d3d3d"
  muted: "#777777"
  muted-soft: "#888888"
  hairline: "#ede3d6"
  hairline-soft: "#f2eadc"
  canvas: "#fcf9f3"
  surface-soft: "#f8f1e3"
  surface-card: "#fdfcfa"
  surface-warm: "#f2eadc"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  peach: "#f6cfb2"
  peach-deep: "#f4c4a0"
  sage: "#607765"
  green-mid: "#117744"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Nib Pro', 'Nib', Georgia, serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nib Pro', 'Nib', Georgia, serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Nib Pro', 'Nib', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Nib Pro', 'Nib', Georgia, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "Circular, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Circular, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Circular, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "Circular, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "Circular, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Circular, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Circular, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "Circular, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Circular, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Circular, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Circular, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  uppercase-tag:
    fontFamily: "Circular, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price:
    fontFamily: "Circular, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
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
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
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
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 {spacing.xl}
  nav-bar-transparent:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  announcement-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageRatio: 1/1
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    hoverTransform: translateY(-2px)
    hoverShadow: 0 4px 16px rgba(34,66,41,0.08)
  product-card-badge:
    backgroundColor: "{colors.peach}"
    textColor: "{colors.primary}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-lg}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    contentMaxWidth: 560px
  hero-split:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    imageRatio: 1/1
    gap: "{spacing.xxl}"
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    rounded: "{rounded.sm}"
  care-tip-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    titleTypography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    iconSize: 32px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    border: 1px solid {colors.hairline}
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.primary}
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    shadow: 0 8px 32px rgba(34,66,41,0.12)
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.nav-link}"
    padding: "{spacing.section} {spacing.xl}"
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    quoteTypography: "{typography.display-sm}"
    attributionTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    border: 1px solid {colors.hairline}
  promo-banner:
    backgroundColor: "{colors.peach}"
    textColor: "{colors.primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — A bright mid-green (#018342) rectangle with 4px radius and white text in Circular medium. On hover, darkens to #006b35 with a subtle 120ms background transition. Disabled state drops to the muted sage (#607765) at 60% opacity. Used for "Add to Cart," "Shop Now," and checkout progression.

**`button-secondary`** — Transparent fill with a 2px forest-green (#224229) border and matching text. On hover, the fill inverts to solid primary with white text — a clean toggle that keeps the page from feeling over-saturated with green. Used for "Learn More," filter toggles, and secondary CTAs on product pages.

**`button-tertiary`** — A text-only link-style button with underline, used inline within care guides and editorial content. No background, no border — just the dark green text with underline that thickens slightly on hover.

### Navigation

**`nav-bar`** — A sticky 64px header in solid forest green (#224229). The Bloomscape wordmark sits left in white, utility icons (cart, account, search) cluster right. Mega-menu dropdowns open on hover for "Plants," "Pots & Planters," and "Plant Care" — each dropdown uses a warm cream (#fcf9f3) background with product thumbnails and serif category headers. On mobile, collapses to a hamburger that triggers a full-screen slide-over in the same forest green.

**`announcement-bar`** — A 40px warm-linen strip (#f8f1e3) above the nav, used for free-shipping thresholds and seasonal promotions. Text in Circular 13px medium, centered. Dismissible with a small × icon.

### Product Cards

**`product-card`** — Square 1:1 plant photography on a near-white card (#fdfcfa) with 8px radius. Title in Circular 16px semibold, price in Circular 16px semibold below, both in forest-green ink. On hover, the card lifts 2px with a soft green-tinted box shadow. Variant dots (pot color options) appear as 12px circles below the price when multiple options exist.

**`product-card-badge`** — A small uppercase tag in peach (#f6cfb2) with dark green text, positioned absolutely at the top-left of the card image. Used for "NEW," "EASY CARE," "PET FRIENDLY," and seasonal callouts like "GIFT FAVORITE."

### Hero Sections

**`hero-banner`** — Full-bleed forest-green background with a single large plant photograph bleeding off one edge. White serif headline (Nib Pro 48px) and white body text (Circular 18px) occupy a max-width column on the opposite side. A primary-green CTA button anchors the composition. Minimum height 560px ensures presence on desktop viewports.

**`hero-split`** — A two-column layout on cream canvas: left column carries a Nib Pro headline and Circular body text; right column holds a square lifestyle photograph with 8px radius. Used for mid-page storytelling sections and seasonal collection intros.

### Collection & Category

**`collection-header`** — A rounded linen-toned (#f8f1e3) banner at the top of collection pages. Centered serif headline (Nib Pro 28px) with a Circular body paragraph below. Provides visual separation between navigation and the product grid.

### Care & Education

**`care-tip-card`** — Linen background (#f8f1e3), 8px radius, 24px internal padding. A small 32px plant-care icon (watering can, sun, thermometer) sits top-left. Title in Circular 16px semibold, body in Circular 14px regular. These tile in a 3-column grid on plant detail pages under a "Plant Care" accordion.

### Product Detail

**`size-selector`** — A row of rectangular option chips with 4px radius and hairline borders. The active selection fills solid forest green with white text. Used for pot-size selection (e.g., "Small — 6″ pot," "Large — 10″ pot") on PDP.

### Form Elements

**`text-input`** — 48px tall with 4px radius, hairline border (#ede3d6) that transitions to forest green on focus. Placeholder text in muted gray (#777777). Used in email signup forms, checkout, and the search overlay.

### Search

**`search-overlay`** — A centered modal card with 8px radius and a soft green-tinted drop shadow. Contains a large text input with magnifying-glass icon, plus a grid of "Popular Searches" chips below as peach-toned pill badges. Triggered by the nav search icon with a scrim backdrop.

### Footer

**`footer`** — Full-width forest green (#224229) with white text. Four-column link grid (Shop, Learn, About, Support) in Circular 15px, an email signup input with a white outline style, and social icons. Copyright and legal links run in caption-sm at the bottom edge.

### Social Proof

**`testimonial-card`** — White card with hairline border, 8px radius. A pull quote in Nib Pro 22px italic, customer name in Circular 13px caps below. Used in a horizontal scroll carousel on the homepage.

### Promotional

**`promo-banner`** — A warm peach (#f6cfb2) rounded strip with forest-green text in Circular 18px semibold. Used inline between product grid rows to highlight seasonal offers, gift-card promotions, or subscription plant deliveries.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2-up on wider phones). Nav collapses to hamburger. Hero stacks vertically — image above, text below. Section spacing drops to 48px. Display-xl falls to 32px. Footer stacks into accordion sections. |
| Tablet | 744–1128px | Product grid goes 3-up. Hero split remains side-by-side at reduced image size. Nav keeps horizontal links but hides mega-menu hover panels behind tap. Care-tip cards go 2-column. |
| Desktop | 1128–1440px | Full 4-column product grid. Sticky nav with mega-menu dropdowns. Hero banner at full 560px height. All spacing at defined token values. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Product grid remains 4-up with larger card images. Hero imagery scales proportionally within the max-width constraint. |

### Touch Targets

- All interactive elements maintain 44px minimum touch area on mobile
- Size-selector chips expand vertical padding to 14px on touch devices
- Nav hamburger icon uses a 48×48px tap zone
- Card tap targets encompass the entire card surface, not just the text

### Collapsing Strategy

- Navigation mega-menus become a slide-over drawer with accordion category groups
- Footer link columns collapse into expandable accordions
- Product filters move from a persistent sidebar to a bottom-sheet modal
- Care-tip grids stack single-column with horizontal scroll option preserved
- Testimonial carousel maintains swipe behavior but hides arrow controls

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Nib Pro webfont weights and exact optical sizes could not be confirmed from extraction alone — the font loads via JS/CSS bundle and only the family name was captured
- Exact box-shadow values on product card hover states are estimated from visual inspection
- Transition/animation durations (likely 120–200ms ease) were not extractable from static analysis
- Dark-mode tokens were not detected — the brand likely does not ship a dark theme
- Icon set (likely custom SVG) details including stroke width and grid size are undetermined
- Exact mega-menu structure and column counts may vary by seasonal merchandising configuration
- The loyalty/rewards widget styling (if present) was not captured in color extraction
