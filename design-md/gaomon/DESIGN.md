---
version: alpha
name: "Gaomon"
source_url: "https://www.gaomon.net"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Gaomon pairs a deep drawing-teal (#108474) against a hot-orange (#f97300) — two ink-palette opposites that read as "creative toolkit" before a single product image loads. The combination lands closer to art-supply packaging than consumer electronics, which suits a brand that positions itself as the entry point for aspiring digital illustrators and students worldwide. Surfaces hold light and near-white (#f9fafb, #fafafa, #f4f2e7), letting product photography carry the visual weight while the teal anchors global navigation and the orange fires every primary CTA and promotional badge. Montserrat at moderate weights — 700 for display, 600 for titles, 400 for body — gives a clean, geometric backbone that scales comfortably across both Latin and Japanese character sets, a practical requirement for a brand operating in both global and Japanese markets simultaneously. Cards lift on soft gray planes (#eeeeee, #f4f2e7) with gentle rounding ({rounded.sm} to {rounded.md}), landing between the hard-cornered engineering aesthetic and the full pill-softness of wellness brands. The palette extends into a small range of pastel tints — lavender (#e4d3f1), sky (#a4cff0), warm cream (#fef5d8), spring (#f7f9ea) — which function as product-line category tags rather than structural tones, encoding SKU differentiation within a two-tone brand identity. Star ratings render via the JudgemeStar font, a Shopify review-app convention integrated seamlessly alongside Montserrat body text. Footer and utility zones pull from near-black neutrals (#2c2930, #403d44), grounding the page while leaving the hero and product grid as bright, open drawing surfaces. Error states use a red-coral (#e65960), success indicators use a saturated green (#4d9902), and secondary links pull from a mid-blue (#0070e8) — a compact system-state vocabulary that avoids overloading the primary teal-orange identity.

colors:
  primary: "#108474"
  primary-active: "#0a6a5c"
  primary-disabled: "#7bbfb8"
  accent: "#f97300"
  accent-active: "#ef8200"
  accent-warm: "#f08200"
  accent-disabled: "#ffdbaf"
  ink: "#2c2930"
  body: "#403d44"
  muted: "#7b7b7b"
  muted-soft: "#a5a3a3"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#fafafa"
  surface-warm: "#f4f2e7"
  surface-tint: "#edf5f5"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  link: "#0070e8"
  info: "#2f60ea"
  error: "#e65960"
  success: "#4d9902"
  category-lavender: "#e4d3f1"
  category-sky: "#a4cff0"
  category-cream: "#fef5d8"
  category-spring: "#f7f9ea"
  scrim: "#2c2930"

typography:
  display-xl:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.36
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.4px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  price:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  tag-uppercase:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  star-rating:
    fontFamily: "JudgemeStar, 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
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
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.accent-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-teal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-teal-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-tint}"
    border: "2px solid {colors.primary-active}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-sm:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-error:
    border: "1px solid {colors.error}"
    textColor: "{colors.error}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoColor: "{colors.primary}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(44,41,48,0.08)"
    height: 64px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "2px solid {colors.primary}"
    boxShadow: "0 8px 24px rgba(44,41,48,0.10)"
    padding: 32px 40px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 40px
    padding: 0 16px
  search-icon-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    width: 40px
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.md}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.ink}"
    padding: "{spacing.base}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 16px rgba(16,132,116,0.12)"
  product-badge-new:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  product-badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  product-badge-bestseller:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 560px
    padding: 80px 0
  hero-banner-teal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 480px
  category-chip:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  tag-category-lavender:
    backgroundColor: "{colors.category-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.tag-uppercase}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  tag-category-sky:
    backgroundColor: "{colors.category-sky}"
    textColor: "{colors.ink}"
    typography: "{typography.tag-uppercase}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  tag-category-cream:
    backgroundColor: "{colors.category-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.tag-uppercase}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  tag-category-spring:
    backgroundColor: "{colors.category-spring}"
    textColor: "{colors.ink}"
    typography: "{typography.tag-uppercase}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  star-rating-widget:
    starColor: "{colors.accent}"
    emptyStarColor: "{colors.hairline}"
    typography: "{typography.star-rating}"
    countTypography: "{typography.caption}"
    countColor: "{colors.muted}"
  price-tag:
    typography: "{typography.price}"
    color: "{colors.ink}"
  price-tag-sale:
    typography: "{typography.price}"
    color: "{colors.error}"
  price-tag-original:
    typography: "{typography.price-sm}"
    color: "{colors.muted}"
    textDecoration: line-through
  spec-table:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    rowAltBackground: "{colors.surface-soft}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  pagination:
    backgroundColor: "{colors.canvas}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    width: 36px
    height: 36px
  compare-toggle:
    backgroundColor: "{colors.surface-soft}"
    checkedColor: "{colors.primary}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.muted-soft}"
    linkColorHover: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    bodyTypography: "{typography.body-sm}"
    padding: 48px 0 24px 0
  newsletter-input:
    backgroundColor: "{colors.body}"
    border: "1px solid {colors.muted}"
    borderFocus: "1px solid {colors.accent}"
    textColor: "{colors.canvas}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 44px

## Components

### Buttons
**`button-primary`** — Orange (#f97300) CTA using `{typography.button-lg}` in uppercase Montserrat 700. This is the urgency color: add-to-cart, buy-now, and time-limited promotional actions. Hover and press deepen to `{colors.accent-active}` (#ef8200); disabled state fades to `{colors.accent-disabled}` (#ffdbaf) with `{colors.muted}` text. Corners hold at `{rounded.sm}` (8px) — resolved, not rounded off.

**`button-teal`** — Brand-primary teal (#108474) button reserved for brand-forward CTAs such as "Shop Now" on hero banners or "Explore Series" in category intros. Same geometry as `button-primary`; active state steps down to `{colors.primary-active}`. The two button colors create a clear visual hierarchy: teal signals identity and exploration, orange signals transaction.

**`button-secondary`** — White canvas with a 2px teal border and teal text. Used as a paired secondary action beside an orange primary (e.g., "Specs" next to "Buy Now"). Active state fills the interior with `{colors.surface-tint}` and sharpens the border to `{colors.primary-active}`.

**`button-sm`** — Compact 32px orange tile for grid-level actions (quick-add, wishlist). Shares orange brand voltage at reduced scale using `{typography.button-sm}`.

### Text Inputs & Search
**`text-input`** — White canvas with `{colors.hairline}` border that snaps to teal on focus. Montserrat body-md placeholder in `{colors.muted}`; fixed 44px height ensures comfortable touch target. Error variant swaps border and text to `{colors.error}` coral.

**`search-bar`** — Sits inside the nav on a `{colors.surface-soft}` ground to visually separate from the white bar. A teal `search-icon-button` (40×40px) attaches flush at the right edge, maintaining the teal-as-navigation-system rule.

### Navigation
**`nav-bar`** — White 64px bar with Montserrat 600 nav links. The teal logo acts as the sole color presence in the resting state. On scroll, `nav-bar-sticky` adds a subtle shadow without changing color. The `mega-menu` drops with a 2px teal top border, semantically connecting navigation state to the structural brand color. Category columns inside the mega-menu use `{typography.body-sm}` with `{colors.primary}` hover on link text.

### Product Cards
**`product-card`** — `{colors.surface-card}` ground, `{colors.hairline-soft}` border, `{rounded.md}` corners. Image zone uses `{colors.surface-soft}` as a neutral photographic base — important for pen tablet and display products whose packaging varies widely in color. Hover state replaces the border with teal and lifts the card with a teal-tinted shadow. Title in Montserrat 600, price in Montserrat 700; star ratings via `star-rating-widget` at card bottom.

**Product badges** sit top-left of the card image. New arrivals use orange (`product-badge-new`), sale items use red-coral (`product-badge-sale`), and bestsellers use teal (`product-badge-bestseller`) — the badge color communicates intent without additional iconography.

### Hero
**`hero-banner`** — Full-bleed `{colors.ink}` (#2c2930) dark background with `{typography.display-xl}` Montserrat 700 white headline. Minimum 560px tall on desktop. A `hero-banner-teal` variant (filled #108474) is used for category landing pages where the brand color should dominate rather than product photography.

**`announcement-bar`** — 40px teal strip pinned above the nav. Montserrat 500 caption-scale text in white, centered. Carries shipping thresholds, limited offers, and regional promotions.

### Category Navigation
**`category-chip`** — Pill-shaped `{rounded.full}` chips on a `{colors.surface-warm}` ground for browsing by product series. Active state fills with teal. Extended pastel tints (lavender, sky, cream, spring) map to `tag-category-*` variants on product cards and series headers, encoding product line membership at a glance without requiring iconography.

### Spec Table
**`spec-table`** — Alternating-row table with `{colors.surface-soft}` even rows. Label column in `{colors.muted}` caption scale; value column in `{colors.ink}` body-sm. Pen pressure levels, LPI resolution, and response rates are primary purchase-decision content on this site — the table is a first-class component, not a secondary detail panel. Used on PDP and product comparison pages.

### Ratings
**`star-rating-widget`** — JudgemeStar glyphs in `{colors.accent}` orange for filled stars, `{colors.hairline}` for empty. Review count in `{colors.muted}` caption scale. Appears on product cards (compact, no count) and PDPs (full count + aggregate).

### Footer
**`footer`** — Deep `{colors.ink}` base with white heading text in Montserrat 600, `{colors.muted-soft}` body links that brighten to white on hover. Four-column grid on desktop. Newsletter zone uses a dark-field `newsletter-input` with orange focus border, keeping the CTA color consistent even in the darkest region of the page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with slide-in teal-accented drawer; hero drops to display-md (28px) and 300px min-height; announcement-bar truncates to one line; spec-table horizontally scrollable |
| Tablet | 744–1128px | Two-column product grid; condensed horizontal nav; hero uses display-lg (36px); mega-menu converts to accordion dropdown; category chips scroll horizontally |
| Desktop | 1128–1440px | Three- to four-column product grid; full hover mega-menu with teal top border; hero at full display-xl (48px); spec-table in side-by-side two-column layout |
| Wide | > 1440px | Max-width container centered at 1440px; product grid extends to five columns; hero padding increases to `{spacing.section}` vertical; footer grid gains breathing room |

### Touch Targets
- Primary and teal CTA buttons: 48px minimum height
- Text inputs and search bar: 44px minimum height
- Search icon button: 40×40px minimum
- Nav links: padded to 44px tap height on mobile via drawer
- Product cards: full-card tap area including image zone
- Category chips: minimum 36px height
- Pagination controls: 36×36px with 8px gap between items

### Collapsing Strategy
- Top nav collapses to logo + hamburger at ≤744px; all nav links move into a full-height slide-in drawer with teal accent on active items
- Mega-menu converts to stacked accordion sections inside the mobile drawer
- Product grid: 4-col → 3-col (1128px) → 2-col (744px) → 1-col (mobile)
- Footer columns: 4-col grid → 2-col grid (tablet) → single-column accordion (mobile) with teal expand chevrons
- Hero layout: image-right / text-left split on desktop; image becomes background with overlay text on mobile
- Announcement bar: multi-message carousel on mobile with 4s auto-advance; static centered text on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No CSS custom properties or design tokens found in extracted source; all type scale values are estimated from Montserrat's standard usage patterns for creative/tech DTC brands
- Primary vs. accent role ambiguity: both #108474 (teal) and #f97300 (orange) appear prominently — teal is assigned structural/nav and orange is assigned CTA/transaction based on common DTC conventions, but live implementation may weight these differently
- JudgemeStar is a Shopify review-app font; its rendered size, weight, and spacing defaults are app-controlled and may differ from values specified above
- Pastel tints (#e4d3f1, #a4cff0, #fef5d8, #f7f9ea, #899df1, #edf5f5, #ffffdf) confirmed in extraction but their exact component-level assignments (series tags, promo banners, UI states) could not be determined from color extraction alone
- No dark mode token signals detected
- Icon set style (outlined vs. filled, stroke weight) not determinable from font/color extraction
- Hover transition durations and easing curves not extractable; 200ms ease-in-out assumed throughout
- Mobile drawer background color and active-state treatment not confirmed; teal accent assumed from brand logic
- Image aspect ratios for product card thumbnails not confirmed; 4:3 assumed based on tablet peripheral photography conventions
