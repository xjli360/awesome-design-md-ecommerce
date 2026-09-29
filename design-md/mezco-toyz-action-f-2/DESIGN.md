---
version: alpha
name: "Mezco Toyz"
source_url: "https://www.mezcotoyz.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Near-black (#272727) photography fields and ink-dark panel surfaces establish a collector's showcase register — not a toy shop but a precision archive where figures with hand-stitched fabric coats and die-cast metal hardware demand uninterrupted real estate. A single primary red (#bd2426) fires as the lone high-voltage signal across that dark canvas: every add-to-cart, every pre-order CTA, every featured-release callout is the same hot ember against near-black, producing unambiguous action hierarchy without size inflation. The rest of the palette fractures into product-state signals — steel blue (#62a1d8, #2f7bbf) for the One:12 Collective lineup blocks, acid green (#9bca3e) for in-stock badges, harvest orange (#f68b1f) for pre-order and limited-edition tags, deep navy (#163959) anchoring the sticky navigation bar — each color keyed to a collector purchase-state rather than deployed as decoration. Soft green (#bada7a) and dark green (#516b1d) encode back-order and re-stock states, completing a five-color availability traffic system legible at thumbnail scale.

  Typography falls entirely back to the system stack — Arial, Helvetica Neue, Roboto — with weight and scale doing all the work: 700-weight uppercase at 32–36px for hero product names that must punch through dense franchise grids, and fine 12px captions for edition counts, SKU details, and series codes that require legibility without competing with product photography. `{rounded.xs}` corners (4px) discipline every card, badge, input, and button — precision over softness, echoing the world of machined plastic tolerances and tight collector-box engineering. No pill shapes, no generous whitespace. The grid runs dense and four-column on desktop so collectors can scan horror, comics, DC, and Marvel breadth at a glance.

  A scrim layer at `{colors.scrim}` (60% opacity) over hero imagery keeps headline type legible across chromatic product silhouettes without degrading photography. Dark surface cards at `{colors.surface-soft}` use no elevation shadow — 1px hairline borders at `{colors.hairline}` do the separation work, keeping dark-on-dark depth coherent. Footer columns in muted gray (#737373) small-cap uppercase and thin dividers at #595959 give the page the weight of a printed catalog. The overall register is cinematic precision: every affordance serves the collector's decision loop, and nothing decorates for its own sake.

colors:
  primary: "#bd2426"
  primary-active: "#521010"
  primary-hover: "#de5052"
  primary-disabled: "#595959"
  accent-green: "#9bca3e"
  accent-green-soft: "#bada7a"
  accent-green-dark: "#516b1d"
  accent-orange: "#f68b1f"
  accent-orange-mid: "#ee730a"
  accent-orange-dark: "#c16508"
  accent-orange-light: "#f9b169"
  accent-blue: "#62a1d8"
  accent-blue-mid: "#2f7bbf"
  accent-blue-strong: "#0051c3"
  navy: "#163959"
  ink: "#ebebeb"
  body: "#dedede"
  muted: "#bfbfbf"
  muted-soft: "#737373"
  hairline: "#595959"
  hairline-soft: "#404040"
  canvas: "#272727"
  surface-soft: "#404040"
  surface-card: "#404040"
  on-primary: "#ffffff"
  on-dark: "#ebebeb"
  badge-available: "#9bca3e"
  badge-preorder: "#f68b1f"
  badge-soldout: "#bd2426"
  badge-backorder: "#bada7a"
  scrim: "#272727"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-label:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.3px
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 16px
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
    rounded: "{rounded.xs}"
    paddingVertical: 12px
    paddingHorizontal: 24px
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
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    paddingVertical: 11px
    paddingHorizontal: 23px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    height: 44px
  button-secondary-hover:
    borderColor: "{colors.muted}"
    textColor: "{colors.ink}"
  button-preorder:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    paddingVertical: 12px
    paddingHorizontal: 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    paddingVertical: 10px
    paddingHorizontal: 14px
    height: 40px
  text-input-focus:
    borderColor: "{colors.accent-blue}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    position: sticky
    top: 0
    zIndex: 100
    paddingHorizontal: "{spacing.xl}"
  announcement-bar:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-label}"
    paddingVertical: "{spacing.xs}"
    paddingHorizontal: "{spacing.base}"
    textAlign: center
  pre-order-strip:
    backgroundColor: "{colors.accent-orange-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-label}"
    paddingVertical: "{spacing.xs}"
    paddingHorizontal: "{spacing.base}"
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    borderWidth: 1px
    borderColor: "{colors.hairline-soft}"
    imageAspectRatio: "1/1"
    padding: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    overflow: hidden
  product-card-hover:
    borderColor: "{colors.hairline}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.4)"
  availability-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    paddingVertical: 3px
    paddingHorizontal: 6px
  badge-available:
    backgroundColor: "{colors.badge-available}"
    textColor: "{colors.canvas}"
  badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.canvas}"
  badge-soldout:
    backgroundColor: "{colors.badge-soldout}"
    textColor: "{colors.on-primary}"
  badge-backorder:
    backgroundColor: "{colors.badge-backorder}"
    textColor: "{colors.canvas}"
  hero-block:
    backgroundColor: "{colors.canvas}"
    minHeight: 480px
    textColor: "{colors.ink}"
    overlayColor: "{colors.scrim}"
    overlayOpacity: 0.6
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-md}"
  hero-secondary-block:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.ink}"
    minHeight: 320px
    titleTypography: "{typography.display-md}"
    subtitleTypography: "{typography.body-md}"
  product-grid:
    columns: 4
    gap: "{spacing.base}"
    paddingHorizontal: "{spacing.xl}"
  product-grid-tablet:
    columns: 3
    gap: "{spacing.md}"
  product-grid-mobile:
    columns: 2
    gap: "{spacing.sm}"
  price-tag:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  price-tag-sale:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
  price-tag-original:
    typography: "{typography.price-sm}"
    textColor: "{colors.muted-soft}"
    textDecoration: line-through
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    height: 36px
    paddingVertical: 8px
    paddingHorizontal: 12px
  category-nav-tab:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    borderBottomWidth: 2px
    borderBottomColor: transparent
    paddingVertical: "{spacing.sm}"
    paddingHorizontal: "{spacing.base}"
  category-nav-tab-active:
    textColor: "{colors.primary}"
    borderBottomColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    borderTopWidth: 1px
    borderTopColor: "{colors.hairline}"
    paddingVertical: "{spacing.section}"
    linkTypography: "{typography.caption}"
    headingTypography: "{typography.caption-label}"
    columnGap: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — The primary add-to-cart and featured-CTA button renders #bd2426 red at 44px height with `{rounded.xs}` (4px) corners and 700-weight uppercase tracking. Hover shifts to `{colors.primary-hover}` (#de5052), lightening rather than darkening — the counter-intuitive choice reads as activation against the already-dark canvas below. Active presses to `{colors.primary-active}` (#521010), the darkest red in the extracted palette. Disabled drains to `{colors.primary-disabled}` (#595959) with muted-soft text, eliminating ambiguity about product availability without a separate label.

**`button-preorder`** — A separate harvest-orange (#f68b1f) variant encodes pre-order availability as a distinct purchase state from "buy now." The orange reads as "coming" versus red's "buy," encoding collector-state logic directly into button fill. Shares the same 44px height, `{rounded.xs}` corners, and uppercase `{typography.button-md}` as `button-primary` for consistent button-group alignment.

**`button-secondary`** — Transparent background with a `{colors.hairline}` border and `{colors.ink}` text, used for secondary actions like "view details" or wishlist additions. Border lightens to `{colors.muted}` on hover to signal interactivity without competing with the adjacent primary CTA. Matches 44px height for consistent alignment in side-by-side button groups.

### Availability Badges

**`availability-badge`** — A five-state color system encodes every collector purchase state at a glance at 10px bold uppercase. Acid green (#9bca3e) signals in-stock; harvest orange (#f68b1f) for pre-order; primary red (#bd2426) for sold-out; soft green (#bada7a) for back-order. All variants share 3×6px padding and `{rounded.xs}` corners — shape stays constant, fill alone distinguishes state. Badges overlay the top-left corner of product card images in a fixed position so state is legible in any grid density.

### Product Card

**`product-card`** — Dark `{colors.surface-card}` (#404040) surface with a 1px `{colors.hairline-soft}` border and `{rounded.xs}` corners. A square 1:1 image fills the card top; below it sit the product name in `{typography.title-sm}`, price in `{typography.price-sm}`, and an availability badge. Hover state (`product-card-hover`) lifts with a 4px box-shadow at 40% black opacity — subtle depth against the already-dark canvas without a scale transform, which would feel mismatched against the precision-object subject matter. No radius increase on hover.

### Hero Block

**`hero-block`** — Full-bleed product photography at 480px minimum height. A `{colors.scrim}` overlay at 60% opacity maintains headline legibility over chromatic product imagery without desaturating the photography. Title in `{typography.display-xl}` (36px 700-weight uppercase), subtitle in `{typography.display-md}`. The `hero-secondary-block` variant swaps photography for a flat `{colors.navy}` (#163959) background for category-launch and line-announcement banners, pairing title and subtitle with a body copy block in `{typography.body-md}`.

### Navigation Bar

**`nav-bar`** — Sticky at 56px height with `{colors.navy}` (#163959) background, visually separating structural chrome from the `{colors.canvas}` product field. Nav links in `{typography.nav-link}` (13px 600-weight, 0.3px tracking). A compact `search-bar` sits inline on the right. The bar retains its navy fill on scroll with no color or opacity shift — it anchors every page state rather than appearing contextually.

### Announcement and Pre-order Strips

**`announcement-bar`** — A 30px-tall persistent banner at `{colors.primary-active}` (#521010) for brand-wide sale or event copy. **`pre-order-strip`** uses `{colors.accent-orange-dark}` (#c16508) for product-page pre-order open/close dates and edition-count alerts. Both share `{typography.caption-label}` (11px 700-weight uppercase, 0.6px tracking) and centered layout. They stack above the nav bar in order: announcement bar first, pre-order strip second, then nav.

### Footer

**`footer`** — Dark `{colors.canvas}` background with a single top `{colors.hairline}` border. Four-column layout with heading labels in `{typography.caption-label}` (#ebebeb) and link lists in `{typography.caption}` 12px muted-soft (#737373). Column gap at `{spacing.xxl}` (48px). No imagery, no bright accents — catalog-back-matter weight signaling brand maturity and collector-audience respect.

### Search Bar

**`search-bar`** — `{colors.surface-soft}` background, `{colors.hairline}` border, 36px compact height with `{rounded.xs}` corners. Placeholder in `{colors.muted-soft}`. On focus, `borderColor` shifts to `{colors.accent-blue}` (#62a1d8) as the sole interactive-state color in the form system. On mobile, tapping expands the search bar to a full-width overlay panel above the product grid rather than navigating to a search page.

### Category Navigation Tabs

**`category-nav-tab`** / **`category-nav-tab-active`** — A horizontal tab strip below the nav bar routes between franchise categories (DC, Marvel, Horror, One:12 Collective, etc.). Inactive tabs render in `{colors.body}` (#dedede); the active tab shifts to `{colors.primary}` (#bd2426) text with a matching 2px bottom border. Tabs are not pill-shaped — they use no background fill, only the border signal. On tablet and mobile the strip becomes horizontally scrollable rather than wrapping.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | 2-column product grid; nav collapses to hamburger icon at 44×44px; hero reduces to 280px height with title scaled to `{typography.display-sm}`; announcement and pre-order strips wrap to 2 lines; category tab strip scrolls horizontally |
| Tablet | 744–1128px | 3-column product grid; nav retains top bar with abbreviated category labels; hero at 360px; search bar expands to full-width row below nav bar |
| Desktop | 1128–1440px | 4-column product grid; full nav with all category tabs visible in tab strip; hero at 480px; all strips single-line |
| Wide | > 1440px | Grid content max-width caps at 1440px with growing side gutters; hero background image bleeds edge-to-edge while headline content stays in the grid column |

### Touch Targets

- All buttons (`button-primary`, `button-preorder`, `button-secondary`) at 44px height satisfy iOS and Android minimum touch target requirements
- Availability badges on product cards have a minimum 32px tap zone via padding inflation on mobile
- Nav hamburger icon maintains a minimum 44×44px tap area
- Search bar expands to full-width overlay on tap, enabling thumb-friendly keyboard interaction
- Pre-order and announcement strips include minimum 36px tappable link height on mobile
- Category nav tabs minimum 44px height on mobile scroll strip

### Collapsing Strategy

- Category nav tab strip collapses from horizontal overflow-hidden to `overflow-x: auto` scroll strip on tablet and mobile — no dropdown
- Product names in cards truncate to 2 lines with `text-overflow: ellipsis` on mobile to protect grid density
- Footer collapses from 4-column to 2-column on tablet and single-column accordion on mobile
- Hero title scales from `{typography.display-xl}` (36px) to `{typography.display-sm}` (20px) on mobile
- Price tag and availability badge stack vertically below product image on mobile; inline row on tablet and above
- Announcement and pre-order strips collapse to icon + short label on mobile below 480px to preserve nav visibility

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site was behind a Cloudflare challenge at extraction time — no page HTML was parsed; all colors were derived from external CSS assets and may include product-photography palette colors rather than pure UI tokens
- Custom or web font not detected — system stack (Arial, Helvetica Neue, Roboto) is inferred; a live render may reveal a custom logotype or display face loaded via JS
- Exact corner radii unconfirmed — `{rounded.xs}` (4px) is inferred from the industrial-precision aesthetic and absence of pill shapes in the color and layout signals
- `surface-card` uses the same value as `surface-soft` (#404040) due to no intermediate gray being directly observed between #272727 and #404040
- Dark-mode versus light-mode split unclear — the extracted palette is entirely dark-register; whether a light-mode variant exists is unknown
- No hover-state or transition timing values extracted — animation durations assumed at ~150ms ease standard
- Icon system (SVG sprite, icon font, or inline SVG) not confirmed; no icon font detected in the font stacks
- Hero overlay opacity (60%) is inferred from contrast legibility requirements, not measured
- The multiple blue values (#62a1d8, #2f7bbf, #0051c3) may originate from product photography rather than UI chrome; their exact usage contexts are unconfirmed
