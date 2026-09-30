---
version: alpha
name: "Shop RSA"
source_url: "https://www.shoprsa.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Signed memorabilia lives at the intersection of athletic achievement and archival permanence, and Shop RSA's interface has absorbed that logic completely — the palette is almost entirely a family of cool neutrals (#fefefe, #f3f3f3, #dedede, #aaaaaa, #888888, #121212) interrupted by exactly one voltage color: #3498db, a clear cerulean that lands on every CTA, cart button, and active filter without competition. The restraint is purposeful. A signed Wayne Gretzky jersey or a Ruth-inscribed baseball already carries its own chromatic weight; an interface competing for attention would undercut the merchandise. In that vacuum the typography does real brand work: the serif stack — Big Caslon, Bodoni MT, Cardo, Georgia — gives product titles and hero copy a museum-placard authority, while Oswald's condensed uppercase runs category labels, filter rails, and navigation with the compressed urgency of a sports scoreboard. The two registers coexist without clashing because they occupy distinct zones: serif for editorial and provenance copy, condensed sans for UI chrome and data. Button geometry favors modest rounding ({rounded.sm}) rather than pill shapes, grounding the store in a collector's-market directness rather than a consumer-softness idiom. Product cards use {rounded.xs} corners and a faint {colors.hairline} border to frame each piece like a display-case window, with photography dominating and price sitting in Oswald bold below the fold of the image. The single-blue-accent strategy means every interactive affordance registers immediately — there is no secondary teal, no accent amber pulling the eye sideways. Section headers in Oswald tight-tracked uppercase echo sports-media information density: box scores, statistics rails, sideline graphics. White space is measured rather than generous, a pragmatic call for a catalogue that can run several hundred authenticated pieces deep, where inventory exposure competes with readability. The overall register is a specialist retailer confident in its category — more certified-dealer than boutique, more archive than lifestyle brand.

colors:
  primary: "#3498db"
  primary-active: "#2980b9"
  primary-disabled: "#a8d4f5"
  primary-hover: "#2e86c1"
  ink: "#121212"
  body: "#333333"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#f3f3f3"
  canvas: "#fefefe"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  surface-mid: "#dedede"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  badge-auth: "#3498db"
  badge-auth-text: "#ffffff"
  badge-sale: "#121212"
  badge-sale-text: "#ffffff"
  price-highlight: "#121212"
  star-active: "#3498db"
  star-inactive: "#dedede"

typography:
  display-xl:
    fontFamily: "Oswald, 'Arial Narrow', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "Oswald, 'Arial Narrow', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 0.3px
    textTransform: uppercase
  display-sm:
    fontFamily: "Oswald, 'Arial Narrow', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  editorial-serif:
    fontFamily: "'Big Caslon', 'Bodoni MT', Cardo, Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  title-md:
    fontFamily: "Oswald, 'Arial Narrow', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'Big Caslon', 'Bodoni MT', Cardo, Georgia, serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Myriad, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Myriad, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Myriad, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-label:
    fontFamily: "Oswald, 'Arial Narrow', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "Oswald, 'Arial Narrow', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "Oswald, 'Arial Narrow', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "Oswald, 'Arial Narrow', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  price-sm:
    fontFamily: "Oswald, 'Arial Narrow', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-label:
    fontFamily: "Oswald, 'Arial Narrow', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  badge:
    fontFamily: "Oswald, 'Arial Narrow', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  breadcrumb:
    fontFamily: "Myriad, 'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  nav-bar-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-bar-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "4/5"
    padding: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
    hoverShadow: "0 4px 12px rgba(0,0,0,0.10)"
  product-card-badge:
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
    backgroundColor: "{colors.badge-auth}"
    textColor: "{colors.badge-auth-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 7px"
  product-card-sale-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.badge-sale-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 7px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.editorial-serif}"
    captionTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xxl}"
  hero-cta-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: "0 {spacing.base}"
    searchIconColor: "{colors.muted-soft}"
    searchButtonBackgroundColor: "{colors.primary}"
    searchButtonTextColor: "{colors.on-primary}"
  authenticity-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    iconColor: "{colors.primary}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.xs}"
    padding: "6px 10px"
    border: "1px solid {colors.hairline}"
  category-filter-rail:
    backgroundColor: "{colors.surface-soft}"
    borderBottom: "1px solid {colors.hairline}"
    itemTypography: "{typography.nav-label}"
    itemPadding: "10px {spacing.base}"
    activeItemColor: "{colors.primary}"
    activeItemBorder: "2px solid {colors.primary}"
    inactiveItemColor: "{colors.muted}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "6px 12px"
    height: 32px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 32px
  price-tag:
    textColor: "{colors.price-highlight}"
    typography: "{typography.price-display}"
  price-tag-original:
    textColor: "{colors.muted}"
    typography: "{typography.price-sm}"
    textDecoration: line-through
  breadcrumb-nav:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.breadcrumb}"
    padding: "{spacing.sm} 0"
  section-header:
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    borderBottom: "2px solid {colors.primary}"
    paddingBottom: "{spacing.sm}"
    marginBottom: "{spacing.lg}"
  product-grid:
    columns: 4
    gap: "{spacing.base}"
    padding: "0 {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.caption-label}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
    borderTop: "3px solid {colors.primary}"
  pagination:
    textColor: "{colors.body}"
    activeTextColor: "{colors.on-primary}"
    activeBackgroundColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    itemSize: 36px

## Components

### Buttons

**`button-primary`** — Flat cerulean (#3498db) fill, white Oswald uppercase text at 14px with 1px letter-spacing, 8px corner radius, 44px height. Hover deepens to #2e86c1; active state collapses to #2980b9; disabled washes out to the pale #a8d4f5 tint. Used for all primary commerce actions — Add to Cart, Buy Now, Submit inquiry.

**`button-secondary`** — White canvas background with a 1px #dedede border and black Oswald uppercase text. Matches button-primary in height and padding for side-by-side layout on product pages. Hover adds a light #f3f3f3 fill and slightly darkens the border to #aaaaaa. Used for Wishlist, Share, and secondary navigation actions.

**`button-add-to-cart`** — Full-width variant of button-primary at 48px height for product page placement. The extra height creates a landing-zone feel for the primary conversion action, consistent with Shopify cart conventions.

### Search Bar

**`search-bar`** — A 44px-tall rectangular field with 1px hairline border and a cerulean search button icon appended on the right. On focus the border upgrades to a solid 1px #3498db stroke to indicate active state without any shadow or glow. The inline submit button inherits `{colors.primary}` so the affordance is unambiguous.

### Navigation

**`nav-bar`** — 60px white bar with a 1px #dedede bottom border. Logo sits left in Oswald bold at ink color. Navigation links use `{typography.nav-label}` — Oswald 13px uppercase, 0.6px tracking — in muted gray by default. Active links gain a 2px cerulean underline and text shifts to `{colors.primary}`. The compressed-sans register echoes sports-media header bars rather than luxury e-commerce.

### Product Card

**`product-card`** — White card with a 1px #dedede border and 4px corner radius. Image occupies a fixed 4:5 aspect-ratio area; below it sits the product title in `{typography.title-sm}` (serif, 15px), a signer/athlete attribution line in `{typography.body-sm}` (muted), and the price in `{typography.price-display}` (Oswald 20px bold, ink). On hover the card lifts with a soft 12px shadow. Authenticity badges and sale flags sit absolutely in the top-left corner of the image zone.

**`product-card-badge`** — Cerulean pill in the image corner reading "AUTHENTICATED" or a sport category in Oswald 10px uppercase. Sale variants use the near-black `{colors.badge-sale}` fill for visual contrast against the card's neutral field.

### Hero Banner

**`hero-banner`** — Full-width dark (#121212) slab, minimum 480px tall. Heading runs `{typography.display-xl}` in Oswald 40px 700 uppercase against the dark ground; subheading uses `{typography.editorial-serif}` in Big Caslon or Cardo at 20px for provenance copy ("Authenticated. Certified. Legendary."). The CTA inside the hero inherits the same cerulean primary button with no modification — color consistency over contextual restyling.

### Category Filter Rail

**`category-filter-rail`** — A horizontal scroll band pinned just below the nav bar on category and collection pages. Items are Oswald 13px uppercase with 10px vertical padding. Active items get a 2px cerulean underline and shift text to `{colors.primary}`. Inactive items sit in #888888 muted. The rail uses `{colors.surface-soft}` as background to lift it slightly off the canvas without introducing a heavy shadow.

### Filter Chips

**`filter-chip`** and **`filter-chip-active`** — 32px pill-adjacent chips (8px radius, not full-rounded) used in sidebar and inline filter panels. Inactive state is white with hairline border. Active state flips to solid cerulean fill with white Oswald text, providing high-contrast selection feedback in dense filter grids.

### Authenticity Badge

**`authenticity-badge`** — A small inline badge appearing within product description blocks and below the product title on listing cards. Combines a cerulean icon (shield or checkmark) with `{typography.caption-label}` uppercase text in #333333 on a #f3f3f3 background with 1px hairline border. Communicates COA presence without disrupting the information hierarchy.

### Section Header

**`section-header`** — Oswald display-md (28px uppercase) with a 2px solid cerulean bottom border and 8px padding below. Used to open every category section on the homepage and collection pages — "NFL AUTOGRAPHS", "HALL OF FAME SIGNATURES", "NEW ARRIVALS". The underline doubles as both decoration and divider, eliminating the need for a separate horizontal rule element.

### Footer

**`footer`** — Near-black (#121212) band with a 3px cerulean top border as the sole chromatic accent. Column headings use `{typography.caption-label}` (Oswald 11px uppercase, #aaaaaa). Body links use `{typography.body-sm}` in muted-soft (#aaaaaa), upgrading to white on hover. The cerulean top border echoes the single-accent strategy at page bottom, bookending the design.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category filter rail becomes horizontal-scroll; nav collapses to hamburger with drawer; hero height reduces to 320px; section padding halves to `{spacing.xl}` |
| Tablet | 744–1128px | Two-column product grid; filter rail remains visible; nav shows top-level categories inline; search bar expands to full width in header |
| Desktop | 1128–1440px | Four-column product grid; sidebar filter panel appears left of grid; nav bar shows full category set with hover dropdowns; hero at full 480px height |
| Wide | > 1440px | Grid max-width caps at 1440px with centered container; hero bleeds edge-to-edge with content constrained to inner column; whitespace increases proportionally |

### Touch Targets

- All buttons minimum 44px height on mobile to meet touch spec
- Filter chips expand padding to 10px 16px on mobile
- Pagination items minimum 40px × 40px on touch viewports
- Nav hamburger target minimum 44px × 44px
- Product card tap area covers the full card, not just title text

### Collapsing Strategy

- Filter sidebar collapses to a bottom-sheet drawer triggered by a "Filter" chip at top of grid on mobile/tablet
- Category filter rail hides overflow and becomes horizontally scrollable with gradient fade on right edge
- Hero subhead (editorial-serif) is hidden on mobile to preserve headline impact in compressed height
- Price and title in product card collapse to a two-line layout; signer attribution line drops to caption-sm on mobile
- Footer columns stack vertically on mobile; cerulean top-border remains the visual anchor

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand-specific font files confirmed on-site; Big Caslon and Bodoni MT appear in the CSS font stack but may fall through to Georgia in most browser environments
- Exact brand-primary blue (#3498db) is a widely used generic Bootstrap/utility blue — cannot confirm whether this is a deliberate brand color or a Shopify/theme default; flagged as primary given it is the only non-neutral in the extracted palette
- No explicit hover/focus state colors extracted; values for `{colors.primary-hover}` and `{colors.primary-active}` are standard 10–15% darkened derivations
- Meta theme-color is absent — no lock-screen or PWA brand color available
- No motion or animation tokens extracted — transition durations and easing curves are unspecified
- Logo mark design, wordmark font, and brand symbol are not observable from CSS extraction alone
- Social proof styling (star ratings, review counts, COA badge visual treatments) could not be confirmed from static extraction
- No confirmed custom icon set; icon style (outline vs filled, stroke weight) is unknown
