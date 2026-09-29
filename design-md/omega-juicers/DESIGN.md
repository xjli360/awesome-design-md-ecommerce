---
version: alpha
name: "Omega Juicers"
source_url: "https://omegajuicers.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Two greens anchor the entire interface — a saturated mid-tone (#298556) that fills primary buttons, collection badges, and "Add to Cart" bars, and a darker forest (#007a3e) that surfaces on hover states and the sticky header wordmark. The effect is less "wellness pastel" and more produce-aisle conviction: celery stalk, wheatgrass shot, the cap of a cold-pressed bottle. Display headlines land in Poppins at 600–700 weight, giving product names a geometric solidity that pairs well with appliance photography where chrome cylinders and matte housings dominate the frame. Body copy and UI labels drop into DM Sans, a grotesque with open apertures that stays readable at 14px on dense spec-comparison tables — the kind Omega leans on heavily, stacking RPM, wattage, and warranty years in side-by-side grids. A golden amber accent (#ffb922) marks sale callouts, star ratings, and limited-edition flags; it reads warm against the green without drifting into citrus cliché. A deep berry (#9c005f) appears sparingly — clearance badges, urgent inventory warnings — functioning as a second alert layer distinct from standard error red. Cards sit on a pure-white canvas (#ffffff) with `{rounded.sm}` corners and a single `{colors.hairline}` border; product imagery bleeds to the card edge while text content observes `{spacing.base}` internal padding. The nav bar is slim (64px), ink-dark (#111111) text over white, collapsing to a hamburger at mobile with a full-screen drawer whose backdrop uses the same near-black (#121212) at 85% opacity. Spacing is utilitarian — `{spacing.section}` (64px) between homepage modules, `{spacing.lg}` (24px) gutters in the product grid — and the overall density is higher than lifestyle brands because the audience cross-shops on specs, not mood. Touch targets honor 48px minimums, pill-shaped filter chips use `{rounded.full}`, and the sticky mobile cart bar anchors to the viewport bottom with a `{colors.primary}` background that keeps the conversion action visible through long scroll depths.

colors:
  primary: "#298556"
  primary-active: "#007a3e"
  primary-disabled: "#9fc4ab"
  ink: "#111111"
  ink-alt: "#1d1d1d"
  body: "#333333"
  muted: "#6b6b6b"
  hairline: "#dedede"
  hairline-soft: "#e1e1e1"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-gold: "#ffb922"
  accent-berry: "#9c005f"
  star-rating: "#ffb922"
  error: "#cc2936"
  success: "#298556"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.36px
  display-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.28px
  display-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.11px
  title-lg:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.12px
  caption-sm:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.11px
  button-lg:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.16px
  button-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.14px
  button-sm:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.13px
  nav-link:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.44px
    textTransform: uppercase
  spec-label:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  spec-value:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0
  price-display:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
    textDecoration: line-through
  link:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    border: 2px solid {colors.primary-active}
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 10px 16px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 52px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.error}
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px 12px 44px
    height: 44px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: 0 1px 4px rgba(0,0,0,0.08)
  mobile-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 100%
    padding: "{spacing.lg}"
    scrim: "{colors.scrim}"
    scrimOpacity: 0.85
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline-soft}
    padding: 0
    imageRatio: 1 / 1
    contentPadding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    hoverShadow: 0 4px 16px rgba(0,0,0,0.08)
    hoverTranslateY: -2px
    transition: all 0.2s ease
  product-card-badge-sale:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-badge-clearance:
    backgroundColor: "{colors.accent-berry}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-lg}"
    ctaComponent: button-primary
    padding: "{spacing.section-lg} {spacing.xl}"
    minHeight: 520px
    overlayGradient: linear-gradient(90deg, rgba(18,18,18,0.75) 0%, transparent 60%)
  hero-split:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-lg}"
    padding: "{spacing.section} {spacing.xl}"
    imagePosition: right
    imageFit: contain
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    padding: "{spacing.xxl} 0"
    textAlign: center
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    rowPadding: "{spacing.md} 0"
    rowBorder: 1px solid {colors.hairline-soft}
    stripeColor: "{colors.surface-soft}"
  comparison-grid:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.title-md}"
    cellTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    cellPadding: "{spacing.base}"
    columnMinWidth: 200px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: 1px solid {colors.hairline}
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  star-rating:
    filledColor: "{colors.star-rating}"
    emptyColor: "{colors.hairline}"
    size: 16px
    gap: "{spacing.xxs}"
  price-block:
    currentTypography: "{typography.price-display}"
    currentColor: "{colors.ink}"
    compareTypography: "{typography.price-compare}"
    compareColor: "{colors.muted}"
    saveTypography: "{typography.caption}"
    saveColor: "{colors.accent-berry}"
    gap: "{spacing.sm}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    padding: 0 "{spacing.base}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.link}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: none
  newsletter-signup:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    inputComponent: text-input
    buttonComponent: button-primary
    rounded: "{rounded.sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  mobile-cart-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    height: 56px
    padding: 0 "{spacing.lg}"
    position: fixed
    bottom: 0
    boxShadow: 0 -2px 8px rgba(0,0,0,0.12)
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    gap: "{spacing.sm}"

---

## Components

### Buttons

**`button-primary`** — Full green (#298556) background with white text in DM Sans 600 weight. Corners at `{rounded.sm}` (8px) keep the shape utilitarian rather than playful. On hover, background darkens to `{colors.primary-active}` (#007a3e) with a 150ms ease transition. Disabled state washes to `{colors.primary-disabled}`, a muted sage that signals inactivity without losing the green identity.

**`button-secondary`** — White background with a 2px `{colors.primary}` border and green text. On hover, the background shifts to `{colors.surface-soft}` and the border darkens to `{colors.primary-active}`. Used for secondary actions — "Compare Models," "View Specs" — where the page already has a dominant green CTA.

**`button-tertiary`** — No background, no border. Green text with an underline on hover. Appears in breadcrumbs, inline links within product descriptions, and footer navigation where visual weight must stay minimal.

**`button-add-to-cart`** — A full-width variant of `button-primary` at 52px height and heavier 32px horizontal padding. This is the single highest-conversion element on any PDP; it spans the full content column and uses `{typography.button-lg}` at 600 weight. On mobile, it yields to the `mobile-cart-bar` when the user scrolls past the fold.

### Navigation

**`nav-bar`** — 64px tall, white background, `{colors.hairline}` bottom border. Logo sits left; category links ("Juicers," "Accessories," "Recipes," "Support") center in `{typography.nav-link}` at 500 weight. Cart icon and search trigger sit right. After scroll, `nav-bar-scrolled` replaces the border with a subtle box-shadow for depth separation. On mobile, category links collapse behind a hamburger icon that opens `mobile-drawer`.

**`mobile-drawer`** — Full-screen overlay with `{colors.scrim}` at 85% opacity behind a white panel. Navigation items stack vertically at `{typography.title-md}` weight. The drawer animates from the left edge (300ms ease-out) and includes an accordion for subcategories within "Juicers" (Cold Press, Centrifugal, Citrus, Nutrition Systems).

**`announcement-bar`** — Sits above the nav at 36px height, `{colors.primary}` background with white `{typography.caption}` text. Cycles between promotional messages (free shipping thresholds, sale events) with a crossfade transition. Dismissable via an × icon that sets a session cookie.

### Product Cards

**`product-card`** — White card with `{rounded.sm}` corners and a 1px `{colors.hairline-soft}` border. Product image fills a 1:1 ratio container at the top edge; image scales to 1.03× on hover with overflow hidden. Below the image, `{spacing.base}` padding wraps the product title in `{typography.title-sm}`, star rating row, and price block. On hover the entire card lifts 2px with a soft shadow transition. Badge variants (`product-card-badge-sale`, `product-card-badge-new`, `product-card-badge-clearance`) position absolutely at the top-left corner of the image container.

**`price-block`** — Stacks the current price in `{typography.price-display}` (Poppins 700, 24px) with an optional compare-at price in `{typography.price-compare}` struck through in `{colors.muted}`. When a sale is active, a "Save $X" caption appears in `{colors.accent-berry}`.

### Spec & Comparison Tables

**`spec-table`** — Alternating-row layout with `{colors.surface-soft}` striping. Labels sit in `{typography.spec-label}` (DM Sans 500, 13px) and values in `{typography.spec-value}` (DM Sans 700, 13px). Rows are separated by a 1px `{colors.hairline-soft}` rule with `{spacing.md}` vertical padding. Common rows: RPM, Wattage, Warranty, Feed Chute Size, Weight, Dimensions.

**`comparison-grid`** — Multi-column table used on category pages and dedicated comparison landing pages. A pinned header row with `{colors.surface-soft}` background holds product thumbnails and names in `{typography.title-md}`. Cell content is `{typography.body-sm}`. Each column is at least 200px wide; the container scrolls horizontally on mobile with a visible scrollbar track.

### Filtering

**`filter-chip`** — Pill-shaped (`{rounded.full}`) chip with a 1px `{colors.hairline}` border. When active, the chip inverts to `{colors.primary}` background with white text. Used in collection pages to filter by juicer type, price range, and features. Chips wrap naturally in a flex row with `{spacing.sm}` gap.

**`search-input`** — Full-width rounded pill (`{rounded.full}`) with a search icon inset left. Background is `{colors.surface-soft}` transitioning to `{colors.canvas}` on focus with a `{colors.primary}` ring. Autocomplete dropdown renders below in a `{colors.surface-card}` panel with `{rounded.sm}` corners and shadow.

### Hero Sections

**`hero-banner`** — Full-bleed lifestyle image (juicer on a kitchen counter with produce) with a left-to-right gradient overlay from `{colors.surface-dark}` at 75% opacity to transparent. Headline lands in `{typography.display-xl}` (Poppins 700, 48px) with the CTA button below. Minimum height 520px on desktop. On mobile, the image crops center and the overlay covers the full frame to maintain text legibility.

**`hero-split`** — Two-column layout with text left and a contained product image right. Used for individual product features or "Why Cold Press?" educational content. Headline in `{typography.display-lg}`, body in `{typography.body-lg}`, and a CTA button beneath. The image uses `object-fit: contain` to respect product silhouettes.

### Footer & Newsletter

**`footer`** — Dark background (`{colors.surface-dark}`) with white text. Four columns: Shop, Support, Company, and a newsletter signup. Column headings use `{typography.title-sm}`, links use `{typography.link}` in `{colors.hairline}` transitioning to `{colors.on-dark}` on hover. Bottom row holds copyright, payment icons, and legal links.

**`newsletter-signup`** — Optionally embedded in the footer or as a standalone band above it. `{colors.surface-soft}` background with a headline in `{typography.title-md}`, a short description in `{typography.body-sm}`, an inline `text-input` and `button-primary` pair. The pair sits side-by-side on desktop and stacks on mobile.

### Utility Components

**`breadcrumb`** — Slash-separated path in `{typography.caption}` with `{colors.muted}` for ancestors and `{colors.ink}` for the current page. Each ancestor is a link with underline on hover.

**`star-rating`** — Filled stars in `{colors.star-rating}` (#ffb922), empty stars in `{colors.hairline}`. 16px size with 2px gap. Optional half-star support via clipped fill. Numeric average renders beside the stars in `{typography.caption}`.

**`mobile-cart-bar`** — Fixed-bottom bar at 56px height with `{colors.primary}` background. Displays "Add to Cart — $XX.XX" in white `{typography.button-lg}`. Appears on PDP pages once the main add-to-cart button scrolls out of view. An upward box-shadow separates it from page content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid. Nav collapses to hamburger + mobile drawer. Hero banner stacks vertically with full overlay. Comparison grid scrolls horizontally. Sticky mobile-cart-bar appears on PDP. Announcement bar text truncates to single line. Filter chips scroll horizontally. |
| Tablet | 744–1128px | Two-column product grid. Nav remains visible but category links may truncate to a horizontal scroll. Hero maintains side gradient but at reduced min-height (400px). Spec tables remain full-width. Footer collapses to two-column grid. |
| Desktop | 1128–1440px | Three-column product grid with `{spacing.lg}` gutters. Full nav with all category links visible. Hero at full 520px height. Comparison grid shows up to 4 columns without scroll. Footer expands to four columns. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Product grid may extend to four columns. Hero image scales proportionally. Generous `{spacing.section-lg}` between homepage modules. |

### Touch Targets

- All interactive elements observe a 48px minimum tap target on mobile, even when visually smaller (padding extends the hit area).
- Filter chips are at least 36px tall with 8px vertical padding to ensure comfortable tapping in scroll rows.
- Close/dismiss icons (announcement bar ×, drawer close) use a 44px tap zone.
- Cart icon in the nav bar has a 48×48px touch area despite rendering at 24px visual size.

### Collapsing Strategy

- Product grid shifts from 4 → 3 → 2 → 1 columns as viewport narrows, using CSS grid with `minmax(260px, 1fr)`.
- Comparison grids never stack vertically; they scroll horizontally with snap points aligned to each column.
- Spec tables remain single-column but condense row padding from `{spacing.md}` to `{spacing.sm}` below 744px.
- Footer columns collapse from four → two → single stack. Newsletter input/button pair stacks below 744px.
- Hero split-layout reverses to image-on-top / text-below on mobile.
- Breadcrumbs truncate to "… / Parent / Current" on mobile to prevent wrapping.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color was detected; the system infers white or green from brand context but the actual value for mobile browser chrome is unconfirmed.
- Exact border-radius values on the live site could not be confirmed through extraction; `{rounded.sm}` (8px) is inferred from typical Shopify theme defaults and visual inspection.
- Whether DM Sans or Poppins serves as the primary heading face versus body face is an assumption based on weight distribution; the live site may assign them differently or load additional weights via JavaScript.
- Specific animation durations and easing curves (e.g., hero carousel timing, card hover transitions) are estimated at standard values (150–300ms ease) and were not directly extracted.
- The golden accent (#ffb922) usage is assumed for ratings and sale badges; actual deployment may include additional contexts (e.g., warranty seals, promotional banners) not captured in the color extraction pass.
- Icon system details (stroke weight, size grid, icon font vs. inline SVG) were not extracted.
- Form validation states (focus ring width, error message typography, success check color) are inferred from the component tokens rather than directly observed.
- The berry accent (#9c005f) appeared in extraction but its exact application context (clearance vs. a product-line sub-brand) could not be confirmed from color data alone.
