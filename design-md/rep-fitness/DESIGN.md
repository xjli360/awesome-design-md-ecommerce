---
version: alpha
name: "Rep Fitness"
source_url: "https://www.repfitness.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The most unusual moment in the Rep Fitness palette isn't the deep navies (#001730, #272d45) that absorb the header and hero sections — it's #ffcf2a, a high-chroma gold that detonates on promotional badges, sale callouts, and discount overlays against near-black backgrounds. The contrast is intentional and hard: molten amber on nighttime blue reads as earned value signal, not lifestyle flattery. Neue Haas Grotesk in two optical sizes — `neue-haas-grotesk-display` at heavy weights for headlines, `neue-haas-grotesk-text` at regular for body copy — grounds the UI in a precision-instrument register: the same typeface choice a camera manufacturer or mechanical watch brand might make, here applied to power racks and barbells. Primary interactive actions run on a confident medium blue (#0078b5), a cooler note that sits in visual tension with the warm gold and prevents the palette from ever reading as automotive. A second, higher-saturation blue (#136dff) handles active links and inline affordances where additional differentiation is needed. The surface system runs almost entirely cool: a tight progression from near-white (#f8f7f5, #f4f4f6) through lavender-gray dividers (#d3d4dd, #e5e5eb) to muted blue-slate (#676986), giving the UI a workshop atmosphere without resorting to true industrial grays. Cards sit low-elevation on the warm canvas, bordered by hairline lavender rather than neutral gray, creating a faintly technical cast that differentiates Rep from lifestyle-first fitness brands. Corner radii stay conservative — `{rounded.xs}` on buttons, `{rounded.sm}` on cards — none of the pill shapes associated with consumer wellness apps. Section spacing is generous, product grids are dense, and specification data surfaces at full weight: the brand assumes its customer wants to read the numbers before committing to a $1,200 barbell.

colors:
  primary: "#ffcf2a"
  primary-active: "#e6b800"
  primary-disabled: "#fff3b3"
  on-primary: "#121212"
  cta-blue: "#0078b5"
  cta-blue-active: "#005f8f"
  cta-blue-bright: "#136dff"
  on-cta: "#ffffff"
  ink: "#121212"
  body: "#252525"
  muted: "#54575b"
  muted-soft: "#757575"
  muted-lighter: "#c5c5c5"
  slate: "#676986"
  hairline: "#d3d4dd"
  hairline-soft: "#e5e5eb"
  hairline-light: "#e3e3e3"
  canvas: "#f8f7f5"
  surface-soft: "#f4f4f6"
  surface-card: "#f7f7f8"
  surface-neutral: "#e0e2e8"
  surface-subtle: "#dbdde4"
  on-dark: "#ffffff"
  navy: "#272d45"
  navy-deep: "#001730"
  navy-mid: "#003b6f"
  navy-alt: "#2c3e50"
  charcoal: "#393939"

typography:
  display-xl:
    fontFamily: "'neue-haas-grotesk-display', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'neue-haas-grotesk-display', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.11
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'neue-haas-grotesk-display', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'neue-haas-grotesk-display', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: -0.1px
  title-lg:
    fontFamily: "'neue-haas-grotesk-display', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'neue-haas-grotesk-text', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'neue-haas-grotesk-text', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'neue-haas-grotesk-text', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'neue-haas-grotesk-text', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'neue-haas-grotesk-text', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-strong:
    fontFamily: "'neue-haas-grotesk-text', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  badge:
    fontFamily: "'neue-haas-grotesk-text', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'neue-haas-grotesk-text', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  button-lg:
    fontFamily: "'neue-haas-grotesk-display', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  button-md:
    fontFamily: "'neue-haas-grotesk-display', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'neue-haas-grotesk-display', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.17
    letterSpacing: -0.2px
  price-sale:
    fontFamily: "'neue-haas-grotesk-display', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.17
    letterSpacing: -0.2px
  price-was:
    fontFamily: "'neue-haas-grotesk-text', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  spec-label:
    fontFamily: "'neue-haas-grotesk-text', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.1px
  rating-sm:
    fontFamily: "'neue-haas-grotesk-text', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
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
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-cta:
    backgroundColor: "{colors.cta-blue}"
    textColor: "{colors.on-cta}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 24px
    height: 48px
  button-cta-active:
    backgroundColor: "{colors.cta-blue-active}"
    textColor: "{colors.on-cta}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.navy}"
    borderColor: "{colors.navy}"
    borderWidth: 2px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 22px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.cta-blue}"
    typography: "{typography.button-md}"
    padding: 0
  button-dark:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: 10px 14px
    height: 44px
    focusBorderColor: "{colors.cta-blue}"
  promo-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    height: 36px
    textAlign: center
  nav-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
    iconColor: "{colors.on-dark}"
    iconSize: 24px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
    ratingTypography: "{typography.rating-sm}"
    imageAspectRatio: "4/3"
    imageBackground: "{colors.surface-soft}"
  price-callout:
    regularPriceColor: "{colors.muted-soft}"
    salePriceColor: "{colors.primary}"
    salePriceTypography: "{typography.price-sale}"
    regularPriceTypography: "{typography.price-was}"
    regularTextDecoration: line-through
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  new-badge:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero-banner:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    overlayColor: "{colors.navy-deep}"
    overlayOpacity: 0.45
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
  category-tile:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.title-lg}"
    overlayColor: "{colors.navy}"
    overlayOpacity: 0.35
    hoverOverlayOpacity: 0.52
    rounded: "{rounded.sm}"
    minHeight: 280px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    iconColor: "{colors.muted}"
    height: 44px
  spec-table:
    backgroundColor: "{colors.canvas}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline-soft}"
    alternateRowColor: "{colors.surface-soft}"
    rowPadding: "{spacing.sm} {spacing.base}"
  comparison-table:
    backgroundColor: "{colors.surface-card}"
    headerBackground: "{colors.navy}"
    headerTextColor: "{colors.on-dark}"
    headerTypography: "{typography.title-sm}"
    cellTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    highlightColor: "{colors.primary}"
    highlightTextColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.surface-neutral}"
    headlineTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    borderTopColor: "{colors.primary}"
    borderTopWidth: 2px
    iconColor: "{colors.slate}"
    iconHoverColor: "{colors.on-dark}"

## Components

### Buttons

**`button-primary`** — Gold (#ffcf2a) fill with near-black `{colors.on-primary}` text in uppercase `{typography.button-lg}`, 48px tall at `{rounded.xs}`. Carries the brand's signature value signal: used on promotional landing pages, sale-section headers, and anywhere price urgency is the message. Active state drops to #e6b800 (`{colors.primary-active}`); disabled washes to pale gold (`{colors.primary-disabled}`) with `{colors.muted}` text. On dark navy backgrounds this button reads immediately without needing additional visual weight.

**`button-cta`** — The workhorse Add-to-Cart and checkout button: medium blue (#0078b5) fill, white text, identical 48px geometry as `button-primary`. The cooler register separates transactional actions from promotional ones so a product page can carry both without visual collision. Active darkens to `{colors.cta-blue-active}`; `{colors.cta-blue-bright}` (#136dff) appears as a link-hover or high-emphasis inline CTA variant.

**`button-secondary`** — Transparent fill with a 2px `{colors.navy}` border and matching text in uppercase `{typography.button-md}`. Used for secondary actions such as "View Details," "Compare," or "Learn More." Hover fills with `{colors.surface-soft}`. On dark backgrounds, swap `borderColor` and `textColor` to `{colors.on-dark}`.

**`button-ghost`** — Text-only in `{colors.cta-blue}` for inline tertiary actions (filter resets, "See all reviews," warranty page links). No border, no background, no height constraint.

**`button-dark`** — Navy (#272d45) fill with white text; used inside hero banners and category-tile CTAs where the gold button would over-compete with the gold promo-bar above.

### Promo Bar & Nav Bar

**`promo-bar`** — A 36px gold (#ffcf2a) band that sits above the navigation, carrying shipping thresholds, limited-time messaging, and countdown copy in uppercase `{typography.caption-strong}` at `{colors.on-primary}`. This is the first element a visitor encounters; the gold-on-gold repetition between promo-bar and CTA buttons creates brand cohesion. On mobile the bar collapses to a marquee scroll when content overruns one line.

**`nav-bar`** — Deep navy (#272d45) header, 64px tall, with white navigation links in `{typography.nav-link}` at medium weight. Logo sits left-aligned in white or reversed brand mark. Cart, account, and search icons render at 24px in `{colors.on-dark}`. The combined `promo-bar` + `nav-bar` stack creates an immersive dark-entry header that immediately signals industrial authority before a single product image loads.

### Product Card

**`product-card`** — Light-surface card (`{colors.surface-card}` #f7f7f8) with a 1px lavender-gray border (`{colors.hairline}` #d3d4dd), 8px radius, and 16px internal padding. Product title in `{typography.title-md}` at weight 600; regular price in `{typography.price-display}` at 24px bold. When an item is on sale, `price-callout` layers over it: regular price renders in `{colors.muted-soft}` with `text-decoration: line-through` at `{typography.price-was}`, and the sale price erupts in `{colors.primary}` gold at `{typography.price-sale}`. The `sale-badge` overlays the image top-left. Image area is 4:3 on a `{colors.surface-soft}` background; no white vignette or drop shadow — the hairline border does the separation work.

### Hero Banner

**`hero-banner`** — Full-bleed lifestyle or product image with a `{colors.navy-deep}` overlay at 45% opacity, minimum 560px tall. Headline in `{typography.display-xl}` (48px/700) in `{colors.on-dark}`; supporting copy in `{typography.body-md}` at 80% opacity white. A gold `button-primary` or `button-dark` anchors the CTA below copy, left-aligned on desktop. On mobile the overlay deepens to 60% to maintain headline legibility over fast-panning photography, and headline drops to `{typography.display-md}` (28px).

### Badges

**`sale-badge`** — Gold (#ffcf2a) chip at `{rounded.xs}` with uppercase `{typography.badge}` in `{colors.on-primary}`. Carries "SALE," percentage-off amounts, and time-limited offer labels. Image-overlaid at the top-left corner of product cards, approximately 22–26px tall. The hard gold against product photography reads at a glance even at thumbnail sizes.

**`new-badge`** — Same geometry as `sale-badge` but navy (#272d45) fill with white text. Used for product launches and newly added SKUs where promotional urgency isn't the message.

### Spec Table

**`spec-table`** — Two-column grid on warm canvas (#f8f7f5). Spec labels in `{typography.spec-label}` at `{colors.muted}`; values in `{typography.body-sm}` at `{colors.ink}`. Alternating rows use `{colors.surface-soft}` (#f4f4f6) for scannability across long parameter lists. Dividers are `{colors.hairline-soft}` (#e5e5eb). This component is structurally prominent on power rack and barbell PDPs where load ratings, weight capacity, and dimensional data are purchase-critical. Values like "1,000 lb. rated" render at full ink weight rather than muted gray.

### Comparison Table

**`comparison-table`** — Multi-column spec comparison for products in the same category. Column headers carry a `{colors.navy}` background with `{colors.on-dark}` text in `{typography.title-sm}`; the currently viewed or recommended product header highlights in `{colors.primary}` (#ffcf2a) with `{colors.on-primary}` text to surface the "best value" signal. Cell text in `{typography.body-sm}`. Boolean rows (✓ / —) use ink and `{colors.muted-soft}` respectively.

### Category Tile

**`category-tile`** — Full-bleed lifestyle image with `{colors.navy}` overlay at 35% opacity, minimum 280px tall. Title in `{typography.title-lg}` white, bottom-left positioned. On hover the overlay deepens to 52% and the title translates up 4px with a 150ms ease transition. Used in category-navigation grids: 2-across on mobile, 4-across on desktop. The navy overlay ensures text legibility across the full range of background photography without hardcoding a scrim.

### Search Bar

**`search-bar`** — Soft-surface input (`{colors.surface-soft}`) with 1px `{colors.hairline}` border, `{rounded.xs}` radius, 44px tall. Magnifier icon in `{colors.muted}` at left-inset. On desktop, the bar lives in the right portion of the nav. On mobile, tapping the nav icon expands a full-width overlay with `{colors.navy}` backdrop, full-width search input, and recent-searches list. Placeholder text in `{colors.muted-soft}`.

### Footer

**`footer`** — Deepest navy (#001730) background with a 2px `{colors.primary}` rule at the top edge — the gold line reappears here after the promo-bar and product badges, bookending the page. Column headers in `{typography.title-sm}` white; nav links in `{colors.surface-neutral}` (#e0e2e8) at `{typography.body-sm}`. Social icons at 20px in `{colors.slate}` (#676986), lightening to `{colors.on-dark}` on hover. Legal copy and copyright run at `{typography.caption}` in `{colors.muted-soft}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with slide-in drawer on `{colors.navy}` overlay; hero drops to 400px min-height; `{typography.display-xl}` scales to `{typography.display-md}`; promo-bar marquee-scrolls if content overflows; spec table scrolls horizontally |
| Tablet | 744–1128px | 2-column product grid; nav collapses mega-menus to dropdowns; hero 480px; category tiles 2-across; comparison table adds horizontal scroll |
| Desktop | 1128–1440px | 3–4 column product grid; full mega-nav with flyout panels; hero 560px; spec table and comparison table side-by-side on PDP |
| Wide | > 1440px | Max content width 1440px centered; hero image scales edge-to-edge beyond 1440px container; product grid stays 4-across; section padding grows to `{spacing.xxl}` |

### Touch Targets

- All buttons minimum 48px tall; icon-only buttons padded to minimum 44×44px hit area
- Nav links in mobile drawer minimum 48px row height with full-width tap zone
- Product card tap area covers entire card face, not just title or button
- Promo-bar links are full-bar-height tap targets on mobile
- Filter chips minimum 36px tall with 8px horizontal padding on each side

### Collapsing Strategy

- Navigation mega-menu collapses to hamburger icon at < 1128px; drawer slides in from left over a `{colors.navy}` scrim
- Product filter sidebar collapses to a "Filter & Sort" bottom-sheet on mobile, full-height panel on desktop
- Spec table transitions from two-column grid to vertically stacked label-above-value pairs below 480px viewport width
- Hero copy stacks headline → subhead → CTA button vertically on mobile; left-aligned with right image bleed on desktop
- Comparison table collapses to a 2-column format (current product vs. one competitor) on mobile with swipe to see additional columns
- Footer four-column grid becomes single-column accordion on mobile; each column header is a tap-to-expand toggle

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; `{colors.navy}` (#272d45) inferred as mobile browser chrome color from nav-bar background
- Active-state gold (#e6b800) and disabled-state gold (#fff3b3) are derived by ±10% lightness from #ffcf2a — not confirmed from extraction
- CTA blue active (#005f8f) derived from darkening #0078b5; not present in extracted palette
- Font sizes, weights, and line-heights for Neue Haas Grotesk at specific hierarchy levels are inferred from standard brand usage of this typeface; the extraction confirmed the font-family stacks but not the applied scale
- Whether #ffcf2a appears on primary action buttons (Add to Cart) or strictly on promotional/badge elements is not confirmed from static extraction; the design system treats it as the primary brand accent usable in both contexts
- Exact hover/focus ring color for `text-input` and `search-bar` not confirmed; `{colors.cta-blue}` is used as the inference
- Animation durations and easing curves not extractable from site scrape
- Mega-navigation column count, category groupings, and icon usage not confirmed
- Star/rating color not confirmed; `{colors.primary}` gold is the recommended choice given palette, but could be a separate token
