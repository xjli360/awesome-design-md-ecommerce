---
version: alpha
name: "Tefal"
source_url: "https://www.t-falusa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The red handle on a non-stick pan — that particular warm, saturated red (#eb322f) that signals heat-readiness on every Thermo-Spot indicator — carries straight through to the digital storefront, where it fires on every primary CTA, sale badge, and "Add to Cart" button against a site otherwise dressed in near-black charcoal (#20282a) and surgical white. The palette splits into two thermal registers. The cool side runs deep: a #20282a navigation frame, #111111 ink, steel-gray hairlines (#bbbbbb, #d1d1d1), and pale canvas surfaces (#f6f6f6, #e8e8e8) that evoke stainless-steel countertops and brushed aluminum housings. The warm side flares selectively — amber (#c07600), orange (#ff9635), and a cream banner ground (#fdf0d5) with dark-amber copy (#6f4400) surface for promotional callouts, giving the merchandising layer its own distinct temperature without bleeding into the brand red. Typography leans on DIN Pro in both medium and bold cuts (dinpromedium, dinprobold), the geometric sans-serif originally drafted for German industrial signage and railway timetables. Its mechanical uprightness reads as engineered precision, not lifestyle editorial. Open Sans fills the body-copy role with system fallbacks, and Sofia Sans appears in the font stack as a secondary display option. Buttons wear uppercase DIN Pro Bold with 0.5px letter-spacing and tight `{rounded.xs}` (4px) corners — sharp enough to feel tool-like, soft enough to remain clickable. Product cards sit at `{rounded.sm}` (8px) with a 1px border that firms up on hover, paired with a light lift shadow. The grid maxes out at 1440px with `{spacing.section}` (64px) vertical rhythm between category swimlanes, collapsing to a single-column stack below 744px where the mega-menu folds into a hamburger drawer. Hover states on the primary red darken dramatically to a deep crimson (#780002) — a shift that reads more like heated metal cooling than a standard lighten/darken ramp. The two Magento-inherited blues (#1979c3, #006bb4) handle link and active-link duty, functional rather than expressive. The overall system is an appliance showroom on screen: high-contrast, photography-forward, functionally dense, with just enough color heat on the red and orange channels to keep the eye moving toward conversion.

colors:
  primary: "#eb322f"
  primary-active: "#780002"
  primary-disabled: "#f5a8a7"
  ink: "#111111"
  body: "#222222"
  muted: "#757575"
  muted-soft: "#8f8f8f"
  hairline: "#d1d1d1"
  hairline-soft: "#e4e4e4"
  border-medium: "#bbbbbb"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-strong: "#e8e8e8"
  surface-warm: "#fdf0d5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  nav-dark: "#20282a"
  nav-dark-hover: "#111111"
  promo-orange: "#ff9635"
  promo-amber: "#c07600"
  promo-text-dark: "#6f4400"
  link: "#006bb4"
  link-hover: "#00699d"
  gray-mid: "#7d7d7d"
  gray-soft: "#a0a0a0"
  star-rating: "#ff9635"
  scrim: "rgba(0, 0, 0, 0.55)"

typography:
  display-xl:
    fontFamily: "dinprobold, 'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "dinprobold, 'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "dinprobold, 'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "dinpromedium, 'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "dinpromedium, 'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  button-lg:
    fontFamily: "dinprobold, 'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "dinprobold, 'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "dinpromedium, 'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "dinpromedium, 'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  nav-link-bold:
    fontFamily: "dinprobold, 'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
  price-lg:
    fontFamily: "dinprobold, 'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: 0
  price-sm:
    fontFamily: "dinprobold, 'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "dinprobold, 'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  promo-label:
    fontFamily: "dinprobold, 'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.3px
  micro-label:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 40px
    height: 52px
    minWidth: 220px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.border-medium}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.ink}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
    paddingHorizontal: "{spacing.lg}"
  nav-bar-bottom:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link-bold}"
    height: 48px
    borderBottom: "1px solid {colors.hairline}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  mega-menu-heading:
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-sm}"
    textColor: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 480px
    padding: "{spacing.xxl} {spacing.section}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 560px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: "14px 36px"
    height: 52px
  promo-bar:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.promo-text-dark}"
    typography: "{typography.promo-label}"
    height: 40px
    padding: "{spacing.sm} {spacing.base}"
  promo-badge:
    backgroundColor: "{colors.promo-orange}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    padding: "0 16px"
    border: "1px solid {colors.border-medium}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.ink}"
  search-suggestions:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
    rounded: "{rounded.sm}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
    padding: "{spacing.base}"
  category-tile-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.10)"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: ">"
    activeColor: "{colors.ink}"
  rating-stars:
    filledColor: "{colors.star-rating}"
    emptyColor: "{colors.hairline}"
    size: 16px
    gap: "{spacing.xxs}"
  price-display:
    typography: "{typography.price-lg}"
    textColor: "{colors.ink}"
  price-original:
    typography: "{typography.price-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  price-sale:
    typography: "{typography.price-lg}"
    textColor: "{colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: "1px solid {colors.border-medium}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  pagination:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    activeColor: "{colors.ink}"
    activeFontWeight: 700
  footer:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-heading:
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.md}"
  footer-link:
    textColor: "{colors.gray-soft}"
    typography: "{typography.link}"
    hoverColor: "{colors.on-dark}"
  toast-notification:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.2)"

## Components

### Buttons
**`button-primary`** — The main conversion driver, rendered in Tefal's signature red (#eb322f) with white uppercase DIN Pro Bold text at 16px, 4px corner radius, and 48px height. On hover the fill deepens to a near-black crimson (#780002), a dramatic shift that reads more like heated metal cooling than a standard darkening ramp. Disabled state fades to a washed-out pink (#f5a8a7) while keeping white text. Used for "Add to Cart," "Shop Now," and primary form submissions throughout the site.

**`button-secondary`** — White fill with a 2px solid ink (#111111) border and matching uppercase DIN Pro Bold label. On hover the button inverts completely — ink background, white text — creating a decisive mechanical toggle. Used for "Learn More," "Compare," and secondary actions where the red would compete with a nearby primary CTA.

**`button-add-to-cart`** — A wider variant of the primary button (min-width 220px, height 52px) that dominates the product detail action zone. Same red fill and uppercase typography but with extra horizontal padding (40px) to give the label breathing room alongside a cart icon. This is the single largest interactive target on any PDP.

### Navigation
**`nav-bar`** — A 56px-tall top strip in the brand's dark charcoal (#20282a) carrying the T-fal wordmark, utility links (account, cart icon with count badge), and a search trigger, all rendered in white. DIN Pro Medium at 14px provides the link typography. The dark bar creates an immediate high-contrast frame that grounds every page.

**`nav-bar-bottom`** — A secondary white rail at 48px sitting directly below the dark header, housing top-level category links ("Cookware," "Kitchen Electrics," "Air Fryers") in DIN Pro Bold. A 1px hairline border along the bottom separates it from page content. Active categories show a 2px red underline accent. On mobile this entire bar collapses into the hamburger drawer.

**`mega-menu`** — Drops from the bottom nav with a subtle box-shadow (0 4px 16px rgba(0,0,0,0.12)). Category headings in `{typography.title-sm}` group product-type links in `{typography.body-sm}`. A right-hand column often carries a promotional image tile linking to seasonal campaigns or new product launches. The panel sits on a white background with `{spacing.lg}` internal padding.

### Product Card
**`product-card`** — White card on an 8px radius with a 1px soft border (#e4e4e4) that sharpens to #d1d1d1 on hover, accompanied by a subtle lift shadow (0 2px 8px rgba(0,0,0,0.08)). Product imagery fills the top zone at a consistent aspect ratio. Title sits below in `{typography.title-sm}`, price in `{typography.price-sm}`. When an item is on sale the new price renders in brand red (#eb322f) and the original appears struck through in muted gray. A small red or orange badge floats over the image corner for "Sale," "New," or "Best Seller" flags, using uppercase DIN Pro Bold at 11px.

### Hero & Promotional
**`hero-banner`** — Full-bleed lifestyle photography — often a kitchen scene with product in use — with a text overlay zone carrying a `{typography.display-xl}` headline (DIN Pro Bold 40px) and a `{typography.body-md}` subhead capped at 560px width. A primary red button anchors the CTA. Minimum height of 480px ensures visual dominance. On tablet the headline drops to `{typography.display-md}` (32px); on mobile, minimum height shrinks to 320px.

**`promo-bar`** — A 40px-tall warm cream (#fdf0d5) strip with dark-amber (#6f4400) text in DIN Pro Bold at 13px, positioned between header and hero. Used to announce sitewide promotions like free shipping thresholds, percentage-off sales, or seasonal events. Text is center-aligned with optional left/right arrow navigation for multiple messages.

**`promo-badge`** / **`sale-badge`** — Small pill-like labels (4px radius, 4px 10px padding) in either orange (#ff9635) for general promotions or brand red (#eb322f) for clearance and sale items. Uppercase DIN Pro Bold at 11px with 0.5px letter-spacing. These appear on product cards, hero banners, and category grid tiles.

### Search
**`search-bar`** — A 44px-tall input with 4px radius and a medium-gray border (#bbbbbb) that transitions to a 2px solid ink border on focus. Placeholder text in `{colors.muted}`. In the desktop nav, search sits as a compact field in the top-right of the dark header bar; on mobile it expands to a full-screen overlay with recent-search history and category quick-links.

**`search-suggestions`** — A dropdown panel below the search bar with 8px radius and a soft box-shadow, surfacing product thumbnails with titles, category matches, and popular search terms in `{typography.body-sm}`. Results are grouped by type with subtle hairline dividers.

### Pricing
**`price-display`** — Standard price rendered in DIN Pro Bold at 28px in ink (#111111). When an item is on sale, the original price drops to `{typography.price-sm}` in muted gray (#757575) with line-through decoration, and the sale price takes the large slot in brand red (#eb322f). The visual hierarchy — small struck gray above large bold red — makes discounts immediately scannable.

### Forms
**`text-input`** — 48px-tall input with a 1px medium-gray (#bbbbbb) border and 4px radius. On focus the border sharpens to 2px solid ink for a clear, accessible indicator. Error state swaps the border to brand red with a caption-sized error message below in `{typography.caption}`. Labels float above the field in muted gray.

**`quantity-selector`** — A compact horizontal minus/number/plus control at 44px height, sharing the same border style as text inputs. The increment and decrement buttons are borderless tap targets within the shared container frame, keeping the control visually tight.

### Filtering & Pagination
**`filter-chip`** — Small capsules with a 1px hairline border and uppercase DIN Pro Medium text at 12px. Active chips invert to an ink background with white text, providing a clear binary state. Used in PLP sidebar filters and horizontal filter bars above product grids.

**`pagination`** — Numeric pagination in `{typography.body-sm}` with the active page in bold ink and inactive pages in muted gray. Arrow buttons bookend the sequence. The active number is visually distinguished by weight alone (700 vs 400) without a background fill.

### Categories
**`category-tile`** — Square tiles on a `{colors.surface-soft}` (#f6f6f6) background with product category imagery and a `{typography.title-md}` label. Tiles carry `{rounded.sm}` (8px) corners and lift slightly on hover via a 4px box-shadow. Used on the homepage and category landing pages to guide users into product swimlanes.

### Rating & Reviews
**`rating-stars`** — Five 16px star glyphs filled in orange (#ff9635) with a 2px gap between each. Empty stars show hairline gray (#d1d1d1). Paired with a numeric review count in `{typography.caption}`. The orange tone unifies with the promotional color register rather than competing with the brand red.

### Utility
**`breadcrumb`** — A left-aligned trail in `{typography.caption}` with muted gray (#757575) links separated by ">" characters. The final crumb renders in ink (#111111) without a link. Appears on PDP and category pages to support deep navigation.

**`toast-notification`** — A slide-up bar in ink (#111111) with white text in `{typography.body-sm}` and 8px radius, used for "Added to Cart" confirmations and back-in-stock alerts. Appears at the viewport bottom with a 16px box-shadow and auto-dismisses after 4 seconds.

### Footer
**`footer`** — Full-width dark charcoal (#20282a) block with white section headings in `{typography.title-sm}` and link columns in `{typography.link}` rendered in soft gray (#a0a0a0) that brightens to white on hover. A bottom sub-footer carries legal copy, copyright, payment icons, and social media links on a marginally darker strip. The footer uses `{spacing.xxl}` vertical padding to separate it clearly from page content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column stack; hamburger drawer replaces mega-menu and bottom nav; hero banner shrinks to 320px min-height with `{typography.display-sm}` headline; product grid collapses to 2-up; search expands to full-screen overlay; promo-bar text truncates with ellipsis or scrolls horizontally; footer sections accordion-collapse; filter chips move behind a "Filter" slide-over sheet |
| Tablet | 744–1128px | 3-column product grid; mega-menu renders as two-column dropdown; hero headline drops to `{typography.display-md}` (32px); sidebar filters move into a slide-over drawer; nav-bar-bottom shows top 5 categories with a "More" overflow link; footer uses two-column layout |
| Desktop | 1128–1440px | 4-column product grid; full mega-menu with promotional image tile; hero at full 480px+ height; sidebar filters visible alongside PLP grid; search bar inline in nav-bar; all nav-bar-bottom categories visible |
| Wide | > 1440px | Content area caps at 1440px centered; outer margins fill with `{colors.surface-soft}`; hero imagery may extend full-bleed while the text container stays width-capped; product grid remains 4-column with increased card spacing |

### Touch Targets
- Minimum tap target: 44x44px on mobile, following Apple HIG guidelines
- Product card entire surface is tappable on mobile; hover-only states (shadow lift, border change) are suppressed
- Quantity selector buttons expand to 48px touch zones despite the compact visual frame
- Nav hamburger icon carries a 48px hit area with 12px padding around the 24px glyph
- Footer accordion headers maintain 48px minimum height for comfortable thumb tapping

### Collapsing Strategy
- Top-level category nav (nav-bar-bottom) collapses into the hamburger drawer below 744px
- Mega-menu category columns reflow from 4-column (desktop) to 2-column (tablet) to stacked accordion (mobile)
- Horizontal filter chips collapse behind a "Filter" button triggering a full-height slide-over panel on mobile
- Footer link columns collapse to accordion sections with DIN Pro Bold headings as toggle triggers
- Promo-bar with multiple messages switches from static center-aligned text to a single-line auto-rotating marquee on mobile
- Product comparison tray (desktop sticky bar) hides on mobile, replaced by a "Compare (n)" floating action button
- Breadcrumb trail truncates to show only the parent and current page on screens below 480px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact DIN Pro font file variants (weight axis values, WOFF2 sources) could not be confirmed from external extraction; dinprobold and dinpromedium names are inferred from CSS font-family declarations
- Sofia Sans usage context unclear — may serve as a fallback for DIN Pro or appear only on campaign/landing pages not visible on the main homepage
- The blues #1979c3 and #006bb4 are likely Magento platform defaults (standard link and active-link colors) rather than intentional Tefal brand choices; included as `link` / `link-hover` tokens but may need replacement if the brand specifies custom link colors
- Primary-disabled value (#f5a8a7) is derived by lightening the brand red; the actual disabled-state color was not directly observed
- Multiple extracted grays (#cfcfcf, #efefef, #c2c2c2, #a6a6a6, #858585, #6d6d6d, #6c6c6c, #777777) appear in the CSS but their specific component assignments could not be mapped without deeper DOM inspection
- No motion or animation tokens extracted — transition durations, easing curves, loading skeleton styles, and Thermo-Spot-inspired micro-animations are unknown
- Icon system details (meigee-icons glyph set, Magento icon sizing, stroke widths) could not be determined from external scanning
- Exact grid gutter widths and container max-width are estimated from common Magento Luma/Blank theme defaults and may differ from the production configuration
- Dark mode palette does not appear to exist but was not explicitly confirmed
- The site is Magento-based (not Shopify); some extracted tokens may reflect Magento Luma theme defaults rather than brand-specific design decisions
