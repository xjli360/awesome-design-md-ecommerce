---
version: alpha
name: "Winix"
source_url: "https://www.winixamerica.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The same engineering discipline that grades a Winix True HEPA filter at 99.97% particle capture shows up in the digital interface as a near-bare off-white plane (#f8f8f8) with almost nothing competing for attention except product photography and CADR specification tables. Mid-gray (#888888) handles secondary labels, supporting copy, and filter metadata — a pairing so restrained it reads closer to a technical datasheet than a lifestyle catalogue. Typography runs entirely on the system stack (Arial, Helvetica Neue) with no custom lettering, a choice that keeps load performance tight and positions the brand squarely in consumer-electronics territory rather than in the aspirational wellness space that many air-quality competitors now occupy. Corner radii are small — `{rounded.xs}` on tags and badges, `{rounded.sm}` on cards and inputs — crisp enough to signal precision manufacturing without the cold edge of zero-radius grid lines. Primary actions carry a navy-blue derived from widely-documented Winix brand identity; surface treatments rely almost entirely on the two confirmed neutral tones, with `{colors.surface-soft}` marking section backgrounds, comparison-table zebra rows, and filter-chip rails. Spacing is generous: `{spacing.lg}` column gaps in the product grid, `{spacing.xl}` padding within content modules, and full `{spacing.section}` breaks between page chapters — creating an uncluttered environment where CADR ratings, filter-coverage specs, and PlasmaWave technology claims land without visual noise. Navigation architecture follows a three-tier model — global product-category nav, a utility bar carrying account and cart, and persistent filter rails on category pages. Product detail pages anchor the conversion argument to a sticky buy-box with replacement-filter awareness; a compatible-filter badge promotes the consumable cycle that sustains the business. The site extraction attempt returned a 429 anti-bot block, leaving the full palette unconfirmed; the tokens below use the two extracted neutrals as anchors and fill remaining structural roles with conservative estimates.

colors:
  primary: "#005eb8"
  primary-active: "#004a93"
  primary-disabled: "#99c0df"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#888888"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  caution: "#e67e00"
  success: "#2d8a4e"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.8px
    textTransform: uppercase
  spec-value:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 26px
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
    padding: 13px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 26px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-utility-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    imageAspectRatio: "1/1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} 0"
    ctaGap: "{spacing.sm}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    height: 34px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
  spec-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  replacement-filter-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    accentColor: "{colors.caution}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  tech-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  review-stars:
    starColor: "{colors.caution}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    altRowBackground: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.spec-label}"
    bodyTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
  sticky-buy-box:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    shadow: "0 4px 12px rgba(0,0,0,0.08)"
    priceTypography: "{typography.price-display}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    separator: "/"
    separatorColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "#cccccc"
    linkColor: "#ffffff"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Solid navy-blue (`{colors.primary}`) fill with white text at `{typography.button-md}` weight and `{rounded.sm}` corners, 48px tall. Hover state darkens to `{colors.primary-active}`; disabled washes to `{colors.primary-disabled}` while retaining white text. Used for primary purchase and "Add to Cart" CTAs throughout the purchase funnel.

**`button-secondary`** — White canvas background with a 2px `{colors.primary}` border and matching navy text. Mirrors the primary button's height and typographic weight to create a clear two-level CTA hierarchy without doubling the blue-fill density. Common uses: "Compare", "Learn More", "Add to Wish List".

**`button-ghost`** — Transparent background, `{colors.body}` text, no border or fill. Used for soft in-page navigation actions such as "View All Reviews" or "See Full Specs" where a bordered control would add visual noise to a content-dense row.

### Text Input & Search

**`text-input`** — White canvas fill, 1px `{colors.hairline}` border, `{rounded.sm}` radius, 44px height. Focus ring shifts the border to `{colors.primary}`; placeholder text renders in `{colors.muted}`. Used in account forms, checkout fields, and newsletter capture.

**`search-bar`** — Mirrors the text-input spec with an inline search icon colored `{colors.muted}`. Sits in the nav header and expands on focus; results appear in a dropdown overlay against `{colors.canvas}`.

### Navigation

**`nav-bar`** — White canvas bar at 64px height with a 1px `{colors.hairline}` bottom border. Logo anchors left; product category links in `{typography.nav-link}` sit inline; cart and account icons anchor right. Desktop renders all links flat; mobile collapses to a hamburger trigger opening a left-side drawer.

**`nav-utility-bar`** — A `{colors.surface-soft}` slim band (36px) above the main nav, carrying promotional messages ("Free Shipping on Orders Over $X"), regional selectors, or login prompts. Renders in `{typography.caption}` and `{colors.muted}`.

### Product Card

**`product-card`** — White surface with a 1px `{colors.hairline}` border and `{rounded.sm}` radius. Square product image at top (1:1 aspect ratio), product name in `{typography.title-sm}`, price in `{typography.price-display}`, and a compact `review-stars` row below. A `tech-badge` floats over the image corner to signal key technology (PlasmaWave, True HEPA). Cards sit on a `{spacing.lg}` gap grid; hover lifts with a subtle box-shadow to confirm interactivity.

### Hero

**`hero`** — Full-width section on `{colors.surface-soft}` with a product unit on one half and headline copy in `{typography.display-xl}` on the other. Minimum 480px height with `{spacing.section}` vertical padding. Two CTAs sit with `{spacing.sm}` gap between them: a `button-primary` ("Shop Now") and a `button-secondary` ("Learn More"). Below 744px, image stacks above copy.

### Spec Callout

**`spec-callout`** — Compact panel showing a single key metric (e.g., "CADR: 243 CFM") with the label in `{typography.spec-label}` (uppercase, tracked) above a large `{typography.spec-value}` figure. Background `{colors.surface-soft}`, corners `{rounded.sm}`. Displayed in horizontal rows of three to five on PDP pages to surface performance data at a glance.

### Filter Chips

**`filter-chip`** / **`filter-chip-active`** — Pill-shaped (`{rounded.full}`) controls with a 1px `{colors.hairline}` border in default state; navy `{colors.primary}` fill with white text in active state. Used in category pages for room-size filters, technology type, and sort controls. 34px height keeps the rail compact; active state makes selections immediately legible.

### Replacement Filter Badge

**`replacement-filter-badge`** — Small `{colors.surface-soft}` tag with a `{colors.caution}` accent marking compatible replacement filter availability. Uses `{typography.badge}` uppercase type and `{rounded.xs}` corners. Appears on product cards and inside the sticky buy-box to keep the consumables repurchase cycle visible without interrupting the primary purchase flow.

### Tech Badge

**`tech-badge`** — Navy `{colors.primary}` fill, white `{typography.badge}` type, `{rounded.xs}` corners. Carries technology labels such as "PlasmaWave", "True HEPA", or "WiFi Ready". Overlays the product image corner on collection cards; appears inline in spec blocks on PDP pages where multiple technology claims need disambiguation.

### Spec Table

**`spec-table`** — Full-width data table with `{typography.spec-label}` headers (uppercase, tracked) and `{typography.body-sm}` value cells. Alternating rows use `{colors.surface-soft}` as the alt-row background; thin `{colors.hairline}` borders divide columns. Covers CADR ratings by dust/smoke/pollen, room coverage in square feet, filter replacement interval, and noise levels in dB — converting the brand's engineering argument into scannable purchase inputs.

### Sticky Buy Box

**`sticky-buy-box`** — White panel with `{rounded.md}` radius and a soft 12px box-shadow that lifts it off the page. Contains the price in `{typography.price-display}`, stock status, the primary "Add to Cart" `button-primary`, and a `replacement-filter-badge` link. Sticks to the right side on desktop PDP as the user scrolls through spec content; collapses to a fixed bottom bar spanning the full viewport width on mobile.

### Review Stars

**`review-stars`** — Five-star glyph row with filled stars in `{colors.caution}` (amber). Aggregate rating count rendered in `{typography.caption}` and `{colors.muted}`. Appears on product cards in the grid and anchored below the product title on PDP pages, directly above the spec callout row.

### Breadcrumb

**`breadcrumb`** — Compact horizontal trail in `{typography.body-sm}`. Inactive ancestors in `{colors.muted}`; current page label in `{colors.ink}`. Slash separator in `{colors.muted}`. Sits between the utility bar and the hero or product area on all interior pages to orient users within the product taxonomy.

### Footer

**`footer`** — Dark `{colors.ink}` background with white link text (#ffffff) and supporting copy in #cccccc. Four-column grid carries product-category links, customer-support links, replacement-parts links, and social icons. `{typography.body-sm}` throughout. Newsletter signup uses the `text-input` field inlined with a `button-primary` adapted for dark backgrounds.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with left-side drawer; hero stacks image above copy; sticky buy-box becomes full-width fixed bottom bar; spec callouts stack vertically; filter chips scroll horizontally in a single row |
| Tablet | 744–1128px | Two-column product grid; nav may abbreviate or collapse to hamburger; hero side-by-side resumes; spec table gains horizontal scroll; filter sidebar converts to bottom-sheet modal |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav inline; sticky buy-box fixed at right of PDP two-column layout; spec callouts render in a horizontal row of four to five |
| Wide | > 1440px | Content max-width capped at ~1280px with auto side margins; product grid may expand to five columns; no other major layout changes |

### Touch Targets
- All buttons, filter chips, and nav links minimum 44×44px on mobile viewports
- Filter chips expand vertical padding to `{spacing.md}` on touch devices
- Product card tap target covers the full card surface, not only the image or title text
- Sticky bottom buy-box renders at 56px button height on mobile for reliable thumb reach
- Star-rating row includes an invisible tap-extension to the full row height

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 1128px; drawer slides in from the left
- Category filter sidebar converts to a bottom-sheet modal on mobile; applied filters persist as chips above the product grid
- Spec callout row wraps to a 2×N grid on tablet and single-column stack on mobile
- Spec table gains horizontal scroll with the first (label) column sticky on narrow viewports
- Hero text and image switch from side-by-side to vertical stack at the 744px breakpoint; headline downsizes from `{typography.display-xl}` to `{typography.display-md}`

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Full color palette unconfirmed** — site returned HTTP 429 (anti-bot block) during extraction; only two hex values confirmed: `#f8f8f8` (off-white surface) and `#888888` (mid-gray text). All other palette entries are conservative estimates.
- **Primary blue (`#005eb8`) is estimated** — derived from publicly visible Winix logo and product packaging, not from a live site token. Exact hex is unconfirmed and may differ from the live stylesheet.
- **Accent and state colors unconfirmed** — `caution: #e67e00` and `success: #2d8a4e` are structurally required but entirely estimated with no brand-source confirmation.
- **No meta theme-color extracted** — typically confirms the primary brand color on mobile browsers; its absence leaves the primary hue unanchored by site data.
- **No custom font detected** — extracted stack is the OS system default (Arial / Helvetica Neue); Winix may load a custom web font not caught during the blocked extraction pass.
- **Icon library unknown** — product-technology icons (PlasmaWave glyph, filter-type illustrations) are proprietary; style weight, fill approach, and grid size cannot be determined without live asset access.
- **Connected-device and smart-home UI** — any companion app or device-dashboard design language is not visible from the main marketing site.
- **Promotional and sale color** — discount badge color, sale price highlight, and clearance label styling are not available in the extraction data.
- **Secondary brand tones** — whether Winix uses a secondary accent (e.g., a teal or light blue for PlasmaWave branding, seen in some product imagery) could not be confirmed from extraction.
