---
version: alpha
name: "KitchenAid"
source_url: "https://www.kitchenaid.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Empire Red — the exact shade that has lived on the tilt-head stand mixer since 1955 — doubles as every primary call-to-action on kitchenaid.com, a rare case where a product colorway and a digital brand token are literally the same pigment (#C41230). The site frames appliances the way a gallery frames sculpture: generous white canvas, restrained sans-serif type set no heavier than 600 except for price displays, and product photography that bleeds to full-width on desktop heroes. Navigation is a slim 64px black bar with white wordmark and sparse utility icons; category mega-menus drop on hover with a subtle `{colors.hairline}` border, never a heavy shadow. Cards use `{rounded.sm}` corners and a single `{colors.hairline}` stroke — the brand trusts product silhouettes to sell, not decorative containers. Add-to-cart buttons sit in Empire Red at `{rounded.xs}`, squared off enough to feel professional-grade rather than playful, while secondary actions use a 1px black outline on `{colors.canvas}`. Typography leans on a geometric sans-serif stack close to Mark Pro or Helvetica Neue; body copy stays at 15–16px / 400 weight with comfortable 1.6 line-height, giving spec-heavy product pages room to breathe. The color system below Empire Red is intentionally muted — warm grays for muted text, a near-white `{colors.surface-soft}` for alternating content bands, and a single accent black (`{colors.ink}`) that carries headlines, price tags, and the persistent sticky-nav. Spacing is architectural: 64–80px between homepage content blocks, 24–32px gutters inside product grids, and 48px padding on comparison-table rows. The overall impression is of a brand that treats every pixel as seriously as it treats die-cast zinc alloy.

colors:
  primary: "#C41230"
  primary-active: "#A30E28"
  primary-disabled: "#E8A0AC"
  ink: "#1B1B1B"
  body: "#333333"
  muted: "#6B6B6B"
  muted-soft: "#999999"
  hairline: "#D9D9D9"
  hairline-soft: "#EBEBEB"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  surface-dark: "#1B1B1B"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  success: "#2E7D32"
  warning: "#F9A825"
  error: "#D32F2F"
  promo-badge: "#C41230"
  compare-highlight: "#FFF3E0"
  rating-star: "#1B1B1B"

typography:
  display-xl:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-bold:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  price-lg:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-md:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  spec-label:
    fontFamily: "'MarkPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
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
  section-lg: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 1px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.ink}
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.ink}
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 40px
  nav-bar-utility:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    height: 36px
    borderBottom: 1px solid {colors.hairline-soft}
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.xxl}"
    borderTop: 1px solid {colors.hairline}
    boxShadow: 0 8px 24px rgba(0,0,0,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
    hoverBorder: 1px solid {colors.hairline}
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: 1 / 1
    objectFit: contain
    padding: "{spacing.lg}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xxl}"
  hero-banner-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xxl}"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: 2px solid {colors.hairline}
    borderActive: 2px solid {colors.ink}
  color-swatch-sm:
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
    border: 1px solid {colors.hairline}
  comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.spec-label}"
    cellPadding: "{spacing.base} {spacing.lg}"
    rowBorder: 1px solid {colors.hairline-soft}
  badge-promo:
    backgroundColor: "{colors.promo-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  rating-stars:
    color: "{colors.rating-star}"
    size: 16px
    gap: "{spacing.xxs}"
  price-display:
    typography: "{typography.price-lg}"
    textColor: "{colors.ink}"
  price-sale:
    typography: "{typography.price-lg}"
    textColor: "{colors.primary}"
  price-original:
    typography: "{typography.price-md}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    padding: 0 16px
    border: 1px solid {colors.hairline}
  sticky-add-to-cart:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 72px
    padding: "{spacing.base} {spacing.xxl}"
    borderTop: 1px solid {colors.hairline}
    boxShadow: 0 -2px 8px rgba(0,0,0,0.06)
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
    linkColor: "{colors.on-dark}"
    linkHoverOpacity: 0.7
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"

## Components

### Buttons

**`button-primary`** — Empire Red background (#C41230) with white text, 4px radius that reads as precisely machined rather than soft. On hover the red deepens to `primary-active`; disabled state fades to a muted rose. Used exclusively for Add to Cart, Shop Now, and checkout-flow CTAs. Height is a consistent 48px across breakpoints.

**`button-secondary`** — White fill with a 1px solid black border and black text. Hover fills with `surface-soft` gray. Appears for Compare, Save to List, and filter-apply actions. Same 48px height as primary to maintain alignment in side-by-side layouts.

**`button-tertiary`** — Text-only with underline, no background or border. Used for inline links within product descriptions, "View all" triggers, and breadcrumb-adjacent navigation.

### Navigation

**`nav-bar`** — 64px-tall black bar spanning full viewport width. White KitchenAid wordmark left-aligned, category links centered in `nav-link` style (14px, weight 500), utility icons (search, account, cart with count badge) right-aligned. On scroll, the bar remains fixed with no visual change — the dark tone already provides sufficient contrast against scrolling content.

**`nav-bar-utility`** — A slim 36px light-gray strip above the main nav containing promotional messaging (free shipping thresholds, financing offers) in `caption` type. Dismissable via an ×  icon.

**`mega-menu`** — Drops below nav on category hover. White background, organized into 3–4 columns with category thumbnails (small appliance silhouettes on neutral backgrounds). Heading text uses `title-sm`; links use `body-sm`. A featured promo card occupies the rightmost column.

### Product Cards

**`product-card`** — Vertical card with product image on a light gray field (`surface-soft`), color swatches below the image as `color-swatch-sm` circles, product name in `title-sm`, price in `price-md`, and a star-rating row. Border is nearly invisible (`hairline-soft`) until hover strengthens it. Cards sit in a 3-up grid on desktop, 2-up on tablet, 1-up on mobile.

### Hero

**`hero-banner`** — Full-width section, minimum 560px tall, with a large product photograph occupying 60% of the frame and text content left- or right-aligned. Headline in `display-xl`, subhead in `body-lg`, and a `button-primary` CTA. Light variant uses `surface-soft` background; dark variant (`hero-banner-dark`) reverses to near-black with white type.

### Product Detail

**`color-swatch`** — 32px circles representing available product colors (the brand offers 40+ mixer colors). Active swatch gets a 2px black border; inactive uses a light hairline stroke. Swatches are spaced 8px apart in a wrapping flex row.

**`comparison-table`** — Horizontal scrolling table for side-by-side appliance specs. Column headers show product thumbnails and names; rows list specs (wattage, capacity, dimensions) in `spec-label` uppercase headers with `body-sm` values. Alternating row backgrounds use `surface-soft` for scannability.

**`sticky-add-to-cart`** — Appears on scroll-past-fold on PDP. Contains product name (truncated), price, color-swatch mini row, and a `button-primary` Add to Cart. Fixed to bottom of viewport with upward shadow.

### Pricing

**`price-display`** — Bold 24px black for standard pricing. When on sale, the current price renders in Empire Red (`price-sale`) and the original price appears adjacent in gray with strikethrough (`price-original`).

### Badges

**`badge-promo`** — Small red pill with white uppercase text ("SALE", "NEW COLOR"). Positioned absolute top-left on product card images.

**`badge-new`** — Black background variant for "NEW" or "EXCLUSIVE" callouts.

### Search

**`search-bar`** — 44px-tall input with light gray background, subtle border, and a magnifying glass icon. Expands to an overlay on mobile with recent searches and trending terms below.

### Footer

**`footer`** — Dark background matching `surface-dark`, organized into 4 columns of link groups (Products, Support, About, Connect). Links in white `body-sm` with reduced opacity on hover. Bottom row contains legal links, country selector, and social icons.

### Breadcrumb

**`breadcrumb`** — Caption-size text with "/" separators in muted gray. Final item (current page) rendered in `ink` without a link.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces category links; hero becomes stacked (image above text); sticky add-to-cart bar always visible on PDP; mega-menu becomes full-screen slide-over; comparison table horizontally scrollable with freeze-first-column |
| Tablet | 744–1128px | 2-column product grid; nav categories visible but condensed; hero image/text split 50/50; mega-menu drops as overlay with 2 columns |
| Desktop | 1128–1440px | 3-column product grid; full mega-menu with 4 columns; hero at full 560px height with 60/40 image/text split; sticky add-to-cart appears on scroll |
| Wide | > 1440px | Content max-width capped at 1440px and centered; side gutters grow; product grid may expand to 4-up for category pages; hero imagery scales proportionally |

### Touch Targets

- All interactive elements maintain 44×44px minimum tap area on mobile
- Color swatches expand to 40px on touch devices with 12px gap
- Nav hamburger icon padded to 48×48px hit zone
- Sticky add-to-cart button spans full width minus 16px side margins on mobile

### Collapsing Strategy

- Desktop mega-menu collapses into a slide-from-left drawer on mobile with accordion sections per category
- Product spec tables collapse into stacked key-value pairs on mobile; comparison mode becomes a swipeable carousel
- Footer columns collapse into accordions on mobile, each section expandable
- Utility nav strip hides on mobile; promotional content moves into a dismissable banner below the main nav
- Breadcrumbs truncate middle segments with "..." on mobile, showing only parent and current page

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned "Access Denied" during extraction — all color values, font stacks, and spacing tokens are based on widely-documented KitchenAid brand guidelines and public brand assets rather than live CSS inspection
- Exact hex for Empire Red may vary between #C41230 and #C8102E depending on regional site version; the value used here (#C41230) is the most commonly referenced in brand documentation
- Font family could not be confirmed from live site; MarkPro is inferred from Whirlpool Corporation's documented brand typeface but the actual web font may differ (possibly a custom subset or licensed alternative)
- Exact border-radius values, box-shadow definitions, and animation/transition timings are estimated from brand convention rather than extracted CSS custom properties
- Mega-menu structure and interaction patterns (hover delay, animation direction) could not be observed due to anti-bot blocking
- Dark mode or reduced-motion preferences could not be assessed
