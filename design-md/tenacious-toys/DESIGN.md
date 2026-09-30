---
version: alpha
name: "Tenacious Toys"
source_url: "https://tenacioustoys.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bungee — the chunky, all-caps display face borrowed from urban signage and construction hoardings — handles every headline and category label on Tenacious Toys' storefront, giving the grid the visual weight of a toy store window stuffed with designer vinyl. The site alternates between two distinct atmospheric registers: hero sections and artist-feature banners run on near-black (#121212, #1d1d1d) for the low-lit drama of a gallery case, while product listings and checkout surfaces open onto light neutral grays (#f2f2f2, #f6f6f6) that let product photography and hand-painted colorways carry the page. Coral red (#f04f36) is the primary brand voltage — editorial CTAs, sale flash badges, and limited-run callouts all carry this orange-red charge, pushed to #e32619 on active press; it is never a Shopify default and never confused with the interactive layer. A co-equal electric blue (#1268f1, softening to #4a9afc at secondary and hover contexts) routes add-to-cart buttons, nav highlights, and interactive links — the deliberate separation between editorial red and transactional blue gives the two-voltage CTA system legibility at a glance. Then the magenta spike: #dd30dd appears as controlled chromatic disruption on blind-box labels, artist-edition stickers, and mystery-item badges — the kind of saturated pop that Designer Toy culture wears as identity rather than accident. Body copy runs Nunito Sans at 400 and 700 weight for warmth and legibility; price spans and catalog numbers drop into a monospace stack (Consolas, SFMono-Regular, Menlo) that echoes print price-guide notation familiar to collectors, making column alignment in dense grids feel intentional. Rounded corners stay structural: {rounded.sm} on product cards, {rounded.md} on dialogs, {rounded.full} only on filter pills — there are no fully dissolved edges in the geometry, echoing the hard-edge sculptural world the inventory celebrates. Availability logic is chromatic and explicit: green (#56ad6a) for in-stock, amber (#dfa354) for pre-order, gray (#949494) for sold-out — a scanning aid across dense multi-column product grids. A warm cream (#fffbd9) tints featured-artist callout strips, breaking the gray-surface monotony of listing pages and signaling editorial curation rather than algorithmic placement. The dark nav and dark footer bracket sandwich the light product canvas, giving every page the contained, print-catalog feel of a specialty retailer that knows exactly what it is.

colors:
  primary: "#f04f36"
  primary-active: "#e32619"
  primary-disabled: "#f05d5d"
  accent-magenta: "#dd30dd"
  accent-blue: "#1268f1"
  accent-blue-light: "#4a9afc"
  accent-blue-surface: "#eff5ff"
  status-instock: "#56ad6a"
  status-preorder: "#dfa354"
  status-sold: "#949494"
  highlight: "#fffbd9"
  ink: "#1d1d1d"
  body: "#4d4d4d"
  muted: "#949494"
  hairline: "#c7c7c7"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#f6f6f6"
  surface-dark: "#121212"
  surface-dark-alt: "#1d1d1d"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-accent-blue: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Bungee', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.02em
    textTransform: uppercase
  display-md:
    fontFamily: "'Bungee', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.02em
    textTransform: uppercase
  display-sm:
    fontFamily: "'Bungee', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.01em
    textTransform: uppercase
  title-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.04em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.04em
    textTransform: uppercase
  badge-label:
    fontFamily: "'Bungee', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.05em
    textTransform: uppercase
  price-display:
    fontFamily: "Consolas, 'SFMono-Regular', Menlo, 'Liberation Mono', monospace"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  price-lg:
    fontFamily: "Consolas, 'SFMono-Regular', Menlo, 'Liberation Mono', monospace"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0
  nav-label:
    fontFamily: "'Nunito Sans', 'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.02em

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
    hover:
      backgroundColor: "{colors.primary-active}"
    disabled:
      backgroundColor: "{colors.primary-disabled}"
      textColor: "{colors.on-primary}"

  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    borderColor: "{colors.accent-blue}"
    borderWidth: 2px
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
    hover:
      backgroundColor: "{colors.accent-blue-surface}"

  button-add-to-cart:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-accent-blue}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    width: 100%
    hover:
      backgroundColor: "{colors.accent-blue-light}"

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    focus:
      borderColor: "{colors.accent-blue}"
      outlineColor: "{colors.accent-blue-surface}"
    placeholder:
      textColor: "{colors.muted}"

  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-label}"
    height: 56px
    logoAccentColor: "{colors.primary}"
    borderBottom: none

  nav-category-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-label}"
    padding: 0 8px
    hover:
      textColor: "{colors.primary}"

  search-bar:
    backgroundColor: "{colors.surface-dark-alt}"
    textColor: "{colors.on-dark}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.muted}"
    height: 40px
    focus:
      borderColor: "{colors.accent-blue}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 8px
    imageAspectRatio: "1 / 1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    borderColor: "{colors.hairline-soft}"
    borderWidth: 1px
    hover:
      borderColor: "{colors.hairline}"
      boxShadow: "0 2px 8px rgba(0,0,0,0.10)"

  blind-box-badge:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px

  limited-edition-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px

  new-badge:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-accent-blue}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px

  status-badge-instock:
    backgroundColor: "{colors.status-instock}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 6px

  status-badge-preorder:
    backgroundColor: "{colors.status-preorder}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 6px

  status-badge-soldout:
    backgroundColor: "{colors.status-sold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 6px

  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.hairline}"
    padding: 64px 24px
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.sm}"

  featured-artist-strip:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: 24px 24px

  collection-filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    active:
      backgroundColor: "{colors.ink}"
      textColor: "{colors.on-dark}"

  price-sale-display:
    originalPriceColor: "{colors.muted}"
    originalPriceDecoration: line-through
    salePriceColor: "{colors.primary}"
    typography: "{typography.price-display}"

  artist-tag:
    backgroundColor: "{colors.surface-dark-alt}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px

  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: 64px 24px

## Components

### Buttons
**`button-primary`** — Coral red (#f04f36) fill with uppercase Nunito Sans at 700 weight via {typography.button-md}, using {rounded.sm} geometry. Active state darkens to #e32619; disabled lightens to {colors.primary-disabled}. Reserved for editorial CTAs, hero "Shop Now" actions, and sale-page callouts — never the add-to-cart transactional button, keeping the two-voltage system unambiguous.

**`button-secondary`** — Transparent background with a 2px electric-blue ({colors.accent-blue}) border and matching text. Hover fills with the pale blue tint {colors.accent-blue-surface} (#eff5ff), signaling interactivity without fully saturating. Used for "View Collection," "See More," and comparison actions adjacent to primary CTAs.

**`button-add-to-cart`** — Full-width electric blue (#1268f1) at 48px height, distinct from the coral primary so that transactional intent reads independently of brand voltage. On mobile it spans the card bottom; on desktop it anchors the PDP sidebar. Hover shifts to {colors.accent-blue-light} (#4a9afc), a slightly friendlier tone that doesn't feel alarming mid-purchase.

### Product Card
**`product-card`** — Square 1:1 image ratio on a {colors.surface-card} (#f6f6f6) tile with {rounded.sm} corners and a 1px hairline-soft border. Title in {typography.title-sm} (Nunito Sans bold, 15px); price in {typography.price-display} (monospace 18px), reading like catalog notation from a print price guide. Badge overlays stack in the top-left corner — blind-box-badge in magenta, limited-edition-badge in coral, new-badge in blue; a maximum of two badges show on mobile. Hover lifts the card with a soft shadow without changing the card's footprint.

### Badges
**`blind-box-badge`** — Magenta (#dd30dd) fill with Bungee uppercase type at 11px via {typography.badge-label}, {rounded.xs} corners. The deliberately loud color signals mystery products where the buyer does not know which variant they will receive. Used exclusively on blind-box and mystery-item listings — never on standard products.

**`limited-edition-badge`** — Coral red ({colors.primary}) with Bungee uppercase type; same size and geometry as the blind-box badge. Signals scarcity for artist-run limited releases and store exclusives. The coral color links it visually to primary editorial CTAs, signaling urgency.

**`artist-tag`** — Near-black ({colors.surface-dark-alt}) chip with Bungee uppercase type in {colors.on-dark}. Appears on product cards credited to a specific designer or studio, functioning as a secondary filter anchor. Its dark fill makes it distinct from the colored availability badges and reads as provenance rather than urgency.

### Status Badges
**`status-badge-instock`** / **`status-badge-preorder`** / **`status-badge-soldout`** — Three-state availability system using {typography.caption} Nunito Sans on {rounded.xs} chips. Green (#56ad6a), amber (#dfa354), and gray (#949494) respectively. Positioned inline below price on product cards, and prominently in the PDP sidebar. The chromatic logic speeds scanning across a dense multi-column grid without requiring reading.

### Hero
**`hero-dark`** — Near-black ({colors.surface-dark}) full-width banner with Bungee display type in white via {typography.display-xl}. Subtitle copy in {typography.body-md} with hairline-gray (#c7c7c7) color for legible contrast against the dark field. Primary CTA renders in coral red with {rounded.sm}. Used for new-release announcements, artist collaboration reveals, and seasonal campaign launches — the dark register creates visual separation from the light-surface product grid below.

### Featured Artist Strip
**`featured-artist-strip`** — Warm cream (#fffbd9) callout band with {rounded.sm} corners that breaks the neutral-gray monotony of the listing grid. Bungee {typography.display-sm} anchors the artist or brand name; body copy runs {typography.body-md} in {colors.body}. This component signals editorial curation rather than algorithmic placement — cream is the only warm-toned surface in the palette and reads as a mark of distinction.

### Filter Pills
**`collection-filter-pill`** — Soft-gray ({colors.surface-soft}) pills with {rounded.full} radius, 700-weight Nunito Sans via {typography.button-sm}. Active state inverts to near-black ({colors.ink}) fill with white text — a clear binary toggle without requiring a colored accent. Used across category pages for Brand, Series, Price, and Availability filter axes. Pills scroll horizontally on mobile.

### Price Display
**`price-sale-display`** — Monospace {typography.price-display} throughout: original price in {colors.muted} with strikethrough, sale price in coral red ({colors.primary}). The monospace stack (Consolas/SFMono-Regular/Menlo) provides natural column alignment in grid views and echoes the catalog-notation aesthetic of print price guides and collector databases.

### Navigation
**`nav-bar`** — Near-black ({colors.surface-dark}) 56px bar with the wordmark accented in {colors.primary} coral. Category links use {typography.nav-label} (Nunito Sans bold 14px with letter-spacing); hover shifts to coral. The integrated search bar ({typography.body-md}, {rounded.sm}) sits right-of-center on desktop, collapsing to a search icon on mobile. No bottom border — the dark field itself creates visual separation from the light product surface below.

### Footer
**`footer`** — Matches the nav's near-black ({colors.surface-dark}), using Bungee {typography.display-sm} for column headings and Nunito Sans {typography.body-sm} for links. Link default is hairline-gray (#c7c7c7); hover activates coral ({colors.primary}). The paired dark nav and dark footer bracket the light product canvas like front and back matter in a printed catalog, giving every page a framed, self-contained feel.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; add-to-cart full-width below image; nav collapses to hamburger + search icon; hero title drops to {typography.display-md}; filter pills scroll horizontally in a single strip; badge overlays capped at two per card |
| Tablet | 744–1128px | 2–3 column product grid; top-level nav categories show inline with sub-categories in dropdown; hero maintains full-width with reduced vertical padding; search bar expands inline |
| Desktop | 1128–1440px | 4-column product grid; full nav category row visible; sidebar filters appear on collection pages; price-sale-display aligns in monospace columns naturally |
| Wide | > 1440px | Grid content max-width capped at 1440px; hero background bleeds full-width while content column centers; Bungee display-xl renders at full 48px in hero without wrapping |

### Touch Targets
- All interactive elements minimum 44×44px on mobile: buttons, filter pills, nav icons, badge overlays
- Product card tap target is the full card surface; badges are display-only overlays, not nested tap targets
- Add-to-cart button spans 100% card width on mobile for maximum hit area
- Filter pills maintain 6px vertical padding to meet 44px minimum height on touch
- Nav hamburger and search icons each occupy a 44×44px touch zone at the bar edges

### Collapsing Strategy
- Nav: hamburger menu at < 744px; full category row at ≥ 1128px; accordion sub-menus on mobile
- Product grid: 1-col mobile → 2-col at 480px → 3-col at 744px → 4-col at 1128px
- Hero CTAs: stacked vertically on mobile, inline on tablet and above
- Badge overlays: max two badges per card on mobile (priority: blind-box > limited-edition > new); additional badges hidden behind a "+N" indicator
- Featured artist strip: full-width on mobile with 16px horizontal padding; max 60% width centered on desktop with the remainder used as whitespace
- Filter sidebar: collapses to a horizontal scrolling pill row on mobile and tablet; persistent left sidebar on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Confirmed canvas base (#ffffff) not found in extracted hex list — assumed from Shopify theme defaults; actual canvas could be a warm off-white
- Exact heading size ladder not directly measured from computed CSS — Bungee and Nunito Sans usage confirmed via font-family extraction but specific scale breakpoints (display-xl, display-md, display-sm) are calibrated estimates
- No confirmed border-radius values from computed styles — all rounded values are design-system defaults calibrated to visual inspection of comparable Shopify storefronts
- Exact nav-bar height (56px used) not measured; estimate from visual inspection
- Logo lockup treatment unclear — may use a custom SVG wordmark or a Bungee variant styled via CSS rather than the font itself
- Box-shadow depth values not extracted; estimates used based on category conventions for collectibles retail
- #0077b5 (LinkedIn blue) and #3c9342, #e99114, #bf262f appear to be social icon and UI-state colors in the footer, not brand-chosen palette entries — excluded from brand tokens
- Dark-mode behavior not detected; site appears to use dark surfaces only for hero and nav/footer chrome, not as a full alternate theme
- Animation and transition timing values not extractable from static hint data — hover transitions assumed at 150–200ms ease
