---
version: alpha
name: "East End Prints"
source_url: "https://www.eastendprints.co.uk"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The cream comes first. Before any artwork loads, the #f0ece6 background makes its case — not white, not neutral gray, but the specific warm off-white of uncoated art paper, a canvas decision that preemptively frames every print as something already framed and hung. East End Prints is a London-founded indie art shop built on the conviction that original work should cost less than a restaurant dinner, and the design system carries that argument without apology: a deep indigo #221155 anchors the primary nav and main CTAs with the weight of a gallery placard, while coral flashes of #e84040 break through on sale callouts and interactive highlights like a felt-tip correction on a proof sheet. Rubik — a geometric sans running 400 through 700 — handles the functional vocabulary: product titles, filter labels, price lines, all rendered with directness that cedes visual authority to the artwork itself. Times New Roman enters selectively for artist attributions and editorial headers, its serif letterforms creating a deliberate high-low friction against Rubik's modernism. The warm orange-reds (#e64a19, #b5340f) work as a heat spectrum for clearance and discount indicators, a separate urgency register that never bleeds into the primary identity palette. Corner radii are minimal throughout — product cards clip at {rounded.xs}, buttons sit flat or near-flat, and nothing aspires to the pill shapes that softer lifestyle brands favor; the hard-edged grid reads as a wall of prints on a gallery rail rather than a curated boutique shelf. Artwork thumbnails pack at {spacing.sm} gutters to maximize the browsing-wall density, with {spacing.section} top-of-section breath to separate the grid from editorial modules. The footer resolves the warm-paper logic by reversing it: #111111 ink on the cream canvas, a final fine-print layer that uses Rubik at caption weight to close every page with the same material feeling it opened with.

colors:
  primary: "#221155"
  primary-hover: "#1a0d40"
  primary-active: "#120930"
  primary-disabled: "#9d96b8"
  accent: "#e84040"
  accent-hover: "#c93232"
  accent-warm: "#e64a19"
  accent-deep: "#b5340f"
  ink: "#111111"
  body: "#595959"
  muted: "#555555"
  hairline: "#e0dbd2"
  canvas: "#f0ece6"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-editorial:
    fontFamily: "'Times New Roman', Times, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  artist-name:
    fontFamily: "'Times New Roman', Times, serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.2px
    fontStyle: italic
  badge:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 11px
    fontWeight: 600
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    border: "1px solid {colors.primary}"
    height: 44px
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-accent-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: none
    padding: 12px 0px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 34px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    focus-border: "1px solid {colors.primary}"
    placeholder-color: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 14px
    height: 40px
    icon-color: "{colors.muted}"
    focus-border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline}"
    logo-color: "{colors.primary}"
  nav-bar-mobile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 56px
    border-bottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1 / 1"
    titleTypography: "{typography.title-sm}"
    artistTypography: "{typography.artist-name}"
    priceTypography: "{typography.price-display}"
    gap: "{spacing.xs}"
    padding: "{spacing.sm} 0"
  product-card-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  product-card-new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-editorial}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 360px
    padding: "{spacing.section} {spacing.xl}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-editorial}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.xxl} 0 {spacing.lg}"
  artwork-grid:
    backgroundColor: "{colors.canvas}"
    columns: 4
    gap: "{spacing.sm}"
    padding: "0 {spacing.xl} {spacing.section}"
  filter-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 6px 12px
    height: 32px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: 6px 12px
    height: 32px
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
    height: 40px
  size-selector-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: 8px 16px
    height: 40px
  price-tag:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  price-tag-sale:
    textColor: "{colors.accent}"
    typography: "{typography.price-display}"
  price-tag-original:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    textDecoration: line-through
  artist-tag:
    textColor: "{colors.muted}"
    typography: "{typography.artist-name}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  promo-banner:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    padding: 8px {spacing.base}
    textAlign: center
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.caption}"
    linkColor: "{colors.surface-soft}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-heading:
    textColor: "{colors.surface-card}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.md}"

## Components

### Buttons

**`button-primary`** — The deep indigo #221155 fill on a flat {rounded.xs} container is the dominant add-to-cart and checkout CTA. Hover darkens to #1a0d40, active to #120930, and disabled state fades to the muted lavender #9d96b8 so disabled controls read as visibly unavailable without visual noise. The 15px Rubik medium-weight label with 0.3px tracking keeps text crisp at 44px height.

**`button-secondary`** — Sits on the warm {colors.canvas} background with an indigo border and indigo text, used for secondary actions like "View details" or "Add to wishlist." The negative-space relationship with `button-primary` is direct: same height, same radius, same label style — swap fill for outline to lower the visual weight.

**`button-accent`** — Coral #e84040 fill reserved for time-limited promotions, sale CTAs, and editorial campaign buttons. Hover deepens to #c93232. Used sparingly so that accent buttons read as genuine urgency signals rather than brand decoration.

**`button-ghost`** — Zero background, indigo text, no border — used for tertiary actions like filter resets, "Load more", and inline link-style CTAs within product descriptions. No padding on sides to align flush with text content grids.

### Search & Inputs

**`search-bar`** — White surface input with a 1px {colors.hairline} border and a muted search icon inside the left padding. Sits in the nav header on desktop. Focus ring swaps the border to {colors.primary} indigo with no shadow. The 40px height keeps it compact in the nav row without shrinking the tap target below usability.

**`text-input`** — Standard 44px form input used on checkout, account, and newsletter fields. Same focus behavior as the search bar. Placeholder renders in {colors.muted} to maintain readability against the white surface without competing with live user input.

### Navigation

**`nav-bar`** — The 64px warm-cream header sits on {colors.canvas} with a 1px hairline bottom border, horizontally separating navigation from the page content below without a heavy drop shadow. The wordmark renders in {colors.primary} indigo using Rubik 600 at display-md scale. Category links run in 14px Rubik regular, expanding to a mega-menu or dropdown with category artwork thumbnails on hover. Mobile collapses to 56px with a hamburger toggle.

### Product Card

**`product-card`** — A flat white tile with zero radius — the entire visual boundary comes from the image edge against the warm cream grid background. The artwork image fills a 1:1 square aspect ratio. Below the image, title in 15px Rubik 500, artist attribution in italic Times New Roman at 13px, then the price row. Badge overlays (`product-card-badge`, `product-card-sale-badge`, `product-card-new-badge`) stack as absolute flat rectangles at the top-left corner of the image, using uppercase Rubik 600 at 11px for SALE / NEW / LIMITED labels.

### Collection Header

**`collection-header`** — Category and collection titles swap Rubik for Times New Roman via the `display-editorial` scale at 32px regular — a serif headline above a Rubik body paragraph. This serif moment anchors each section landing page with editorial register before the product grid begins, establishing a gallery-catalogue tone.

### Artwork Grid

**`artwork-grid`** — Four columns on desktop with {spacing.sm} gutters, packing prints edge-near to simulate a gallery rail. The tight gap is intentional: it maximizes the number of artworks above the fold and lets the images speak as a curated wall rather than an isolated e-commerce shelf. The {colors.canvas} background bleeds between cards so the cream reads as the grid itself, not an interstitial void.

### Filter Chips

**`filter-chip`** / **`filter-chip-active`** — Inline filter controls for medium, subject, color, orientation, and price. Inactive chips sit on white with a hairline border and muted body text. Active chips invert to solid {colors.primary} indigo fill, signalling selected state clearly without relying on a checkmark icon. Chips are 32px tall to keep the filter rail compact above the artwork grid.

### Size Selector

**`size-selector`** — Used on product detail pages to choose print dimensions. Inactive tiles have a 1px hairline border; selected tiles thicken to a 2px solid {colors.primary} border with indigo text, making the selection state unmistakable without color-fill affordance. The 40px height and body-sm Rubik type match the field-form system.

### Badges

**`product-card-badge`** — Coral flat rectangle for general callout ("NEW", "LIMITED"). **`product-card-sale-badge`** — Orange-red #e64a19 for active sale pricing. **`product-card-new-badge`** — Indigo for new arrivals. All share the same zero-radius flat geometry and uppercase Rubik badge typography — only the fill color changes to encode badge category.

### Promo Banner

**`promo-banner`** — A full-width coral ribbon at the very top of the page, above the nav bar, used for sitewide sale announcements and shipping promotions. Uppercase Rubik 600 badge text on {colors.accent} fill. Single line of copy, center-aligned, 8px vertical padding.

### Footer

**`footer`** — The site closes on a reverse of the warm-paper opening: {colors.ink} (#111111) fill with soft-white text in 12px Rubik regular, 400 weight. Column headings bump to Rubik 500 at title-sm scale. The dark footer reinforces East End Prints' editorial positioning — it reads as a colophon to the browsing experience rather than a regulatory afterthought.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Artwork grid collapses to 2 columns; nav collapses to hamburger + logo; filter chips move into a horizontally scrolling rail; hero banner min-height reduces to 280px; button full-width in product detail |
| Tablet | 744–1128px | Artwork grid renders at 3 columns; nav shows top-level links with hamburger for sub-categories; search bar moves to a modal/overlay; size selector chips wrap to 2 rows |
| Desktop | 1128–1440px | Full 4-column artwork grid; full horizontal nav with category dropdowns; search bar inline in nav; promo banner visible above nav |
| Wide | > 1440px | Max content width ~1360px centered; grid maintains 4 columns with proportionally wider gutters; hero padding expands to {spacing.xxl} horizontal |

### Touch Targets

- All interactive buttons minimum 44px height
- Filter chips 32px height — consider increasing to 40px if used on native mobile
- Size selector tiles minimum 40px × 40px
- Nav hamburger icon minimum 44px × 44px tap region
- Product card image tap region covers full square — no separate "view" overlay required

### Collapsing Strategy

- Primary nav: full links → hamburger at < 1128px; mega-menu collapses to drawer slide-in
- Filter rail: horizontal flex wrap on tablet/desktop; horizontal scroll with snap points on mobile
- Artwork grid: 4 col → 3 col at tablet → 2 col at mobile
- Footer columns: 4 column flex → 2 column → single column stack on mobile
- Hero banner: side-by-side text/image layout → stacked text-above-image on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-weight confirmation for Rubik nav links — extracted stacks show `Rubik` but active weight on navigation items could be 400 or 500; defaulted to 400 regular
- Times New Roman usage scope unclear — extracted as a font stack member but uncertain whether it appears as display headers site-wide or only on specific editorial/artist pages
- No confirmed border-radius values — extracted hints contain no explicit radius tokens; {rounded.xs} (4px) inferred from flat-edged visual convention of UK indie art shop genre
- Button color assignments (primary vs. accent) inferred from color distinctiveness; no live CTA extraction confirmed which hex maps to add-to-cart vs. editorial buttons
- Hover and focus states not confirmed from extraction — all hover colors are darkened-hex derivations rather than observed values
- No animation or transition timings extracted; standard 150–200ms ease assumed for interactive states
- `meta theme-color` is absent, suggesting no PWA manifest or explicit brand color declaration in the `<head>`
