---
version: alpha
name: "AllPosters"
source_url: "https://www.allposters.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Half a million thumbnails stacked in a relentless four- to five-column grid — AllPosters is a catalog machine that trusts the artwork to do all visual heavy lifting. The surrounding chrome is deliberately minimal: the near-black #313131 carries every text element against a white (#ffffff) canvas, so that saturated movie stills, fine-art reproductions, and photographic prints read without competition from the interface. There are no editorial curves, no aspirational lifestyle photography — just image density, price, and an Add to Cart button, a pragmatic directness that acknowledges the central tension of a store selling reproductions of other people's art: the UI cannot afford ego. Primary calls-to-action reach for a catalog-red, a hue with the same instinctive urgency as a sale sticker, calibrated for a price-competitive mass-market poster trade where impulse drives conversion. Hard-edge frames (`{rounded.none}`) on product image tiles echo the physical experience of a gallery wall or a poster bin; buttons pick up only the lightest radius at `{rounded.xs}` — enough to signal interactivity without breaking the utilitarian register. The search bar is the functional center of gravity: with a catalog too large to browse linearly, a prominent full-width field anchored in the nav header carries more UX weight than any hero image. A left-rail filter sidebar on desktop handles secondary refinement across subject, style, color, orientation, and format — collapsing to a drawer on mobile. Typography runs on Arial-based system stacks at modest weights, letting the massive inventory render at maximum performance without a custom font load. Price figures appear at a larger bolder weight ({typography.price-display}) to anchor purchase decisions in the card grid, while product titles stay small and quiet ({typography.product-title}), deferring to the image above them. The overall effect is deliberate anti-aestheticism: AllPosters occupies the utilitarian end of the art retail spectrum, and every interface decision reinforces that position.

colors:
  primary: "#cc0000"
  primary-active: "#a30000"
  primary-disabled: "#f2a0a0"
  ink: "#313131"
  body: "#444444"
  muted: "#767676"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  rating-star: "#f5a623"
  link: "#0066cc"
  footer-bg: "#222222"
  footer-text: "#cccccc"
  footer-link: "#dddddd"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0
  product-title:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
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
    padding: 10px 20px
    height: 40px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    width: "100%"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 38px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 90px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-announcement:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    height: 30px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 40px
    submitButtonBackgroundColor: "{colors.primary}"
    submitButtonTextColor: "{colors.on-primary}"
    submitButtonRounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageBorder: "1px solid {colors.hairline-soft}"
    titleTypography: "{typography.product-title}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.sm}"
    gap: "{spacing.xs}"
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  price-display:
    textColor: "{colors.primary}"
    typography: "{typography.price-display}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    separatorColor: "{colors.hairline}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    width: 220px
    borderRight: "1px solid {colors.hairline}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 320px
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  rating-stars:
    starColor: "{colors.rating-star}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  product-grid:
    gap: "{spacing.sm}"
    columnsMobile: 2
    columnsTablet: 3
    columnsDesktop: 4
    columnsWide: 5
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    linkColor: "{colors.footer-link}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.xl}"

---

## Components

### Buttons

**`button-primary`** — A compact, all-caps, slightly rounded red button (`{rounded.xs}`) at 40px height used for primary catalog actions. Background shifts from `{colors.primary}` to `{colors.primary-active}` on hover; washes to `{colors.primary-disabled}` in the disabled state while keeping white text. Letter-spaced uppercase `{typography.button-md}` signals transactional intent throughout the interface.

**`button-add-to-cart`** — Full-width variant of `button-primary` at 44px height. Stretches to span the product card or sidebar container width without explicit pixel sizing, making it the dominant action in both grid and detail contexts.

**`button-secondary`** — White canvas fill with a 1px `{colors.hairline}` border and `{colors.ink}` text in the same uppercase `{typography.button-md}` style. Used for secondary actions like Save to List, View More, and modal dismiss. Border darkens one step on hover; no fill change, keeping it clearly subordinate to the red primary.

### Search Bar

**`search-bar`** — A wide 40px input spanning the center column of the nav bar on desktop. A 2px hairline border and `{rounded.xs}` make it slightly more prominent than secondary inputs. The submit button attaches flush to the input's right edge with `{rounded.none}` and `{colors.primary}` fill — no gap, no separator — forming a single horizontal unit. Autocomplete drops below with `{colors.canvas}` fill and `{colors.hairline}` row dividers.

### Product Card

**`product-card`** — Hard-edge (`{rounded.none}`) card with a `{colors.hairline-soft}` border on the image container that mimics the feel of a print in a physical bin. Title in `{typography.product-title}` sits below the image at quiet weight; price in `{typography.price-display}` at `{colors.primary}` anchors the eye. Sale badges overlay the image corner using the `sale-badge` component. Format selection swatches (framed, canvas, poster) appear as small inline pills on hover or focus, encouraging format consideration before click-through to the PDP.

### Navigation

**`nav-bar`** — White background at 90px height with a bottom `{colors.hairline}` rule. An announcement strip (`nav-bar-announcement`) in `{colors.ink}` fill sits above at 30px height, carrying shipping promotion copy in `{typography.caption}` reversed to `{colors.canvas}`. Logo anchors left; the search bar occupies the center third; cart, account, and wishlist icon-buttons cluster at right. Category navigation links in `{typography.nav-link}` run in a second row below the primary bar on desktop.

### Filter Sidebar

**`filter-sidebar`** — A 220px left-rail panel with a `{colors.hairline}` right border. Accordion sections for Subject, Style, Color, Orientation, and Format each expand via a chevron toggle. Selected filters render as dismissible `category-pill` tokens. On mobile the panel becomes an off-canvas drawer triggered by a sticky Filter toggle at the top of the product grid; selected filter count appears as a numeric badge on the trigger button.

### Hero Banner

**`hero-banner`** — A `{colors.surface-soft}` strip at minimum 320px height used on category landing pages and promotional placements. Heading in `{typography.display-xl}`; supporting copy in `{typography.body-md}`. CTA button floats left-aligned below copy as `button-primary`. On promotional banners the background is replaced with a full-bleed image and the text block receives a translucent dark scrim for legibility — the text tokens remain identical.

### Category Pills

**`category-pill`** — Soft gray fill, 1px hairline border, `{rounded.full}`, all-caps `{typography.button-sm}` text. Used as browsable subject tags at the top of category pages and in related-browse rows below PDPs. Active state (`category-pill-active`) inverts fill to `{colors.primary}` and text to `{colors.on-primary}`, providing clear selection feedback without increasing size.

### Sale Badge

**`sale-badge`** — Zero-radius red chip in `{colors.primary}` with `{colors.on-primary}` text at `{typography.badge}`. Applied as an absolute overlay on the top-left or top-right corner of product card images. Carries copy such as SALE, NEW, or a discount percentage. The hard edge (`{rounded.none}`) matches the product image frame so the badge reads as part of the image container rather than floating above it.

### Pagination

**`pagination`** — Numbered page chips at `{rounded.xs}` with a 1px `{colors.hairline}` border and `{colors.canvas}` fill. Active chip inverts to `{colors.primary}` fill and `{colors.on-primary}` text. Prev and Next arrows flank the number row. A per-page selector (24 / 48 / 96 items) sits adjacent to the bar, letting power users increase grid density to reduce page-flip overhead.

### Rating Stars

**`rating-stars`** — Five-star row using `{colors.rating-star}` amber fill for filled stars and `{colors.hairline}` for empty. Review count appears in `{typography.body-sm}` at `{colors.muted}` inline with the star row. The star assembly is non-interactive in grid context; on the PDP it anchors the jump-to-reviews link.

### Footer

**`footer`** — Deep charcoal (`{colors.footer-bg}`) full-width band containing three to four column link groups. Section headings in `{typography.title-sm}` at `{colors.footer-text}`; body links in `{typography.body-sm}` at `{colors.footer-link}`. A bottom sub-footer row holds social icons, legal links, and a copyright line in `{typography.caption}`. The dark ground anchors the page and provides clear visual closure after the densely packed product grid above.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Product grid collapses to 2 columns; filter sidebar becomes full-height off-canvas drawer; search bar moves to its own full-width row below logo; hero-banner height reduces to 200px; pagination shows only prev/next arrows plus current page number |
| Tablet | 744–1128px | Product grid expands to 3 columns; filter sidebar visible at 180px, collapsible via toggle; nav bar retains single-row layout; announcement strip visible |
| Desktop | 1128–1440px | 4-column product grid; 220px filter sidebar always visible; full nav-bar with announcement strip; hero-banner at full 320px+ height; per-page selector visible beside pagination |
| Wide | > 1440px | 5-column product grid; content max-width 1440px centered with lateral canvas flanks; filter sidebar width fixed at 220px regardless of viewport |

### Touch Targets

- All buttons, filter checkboxes, and pagination chips maintain a minimum 44×44px touch target on mobile
- Product card hit area covers the full card including title and price row, not just the image thumbnail
- Off-canvas filter drawer opens and closes via a sticky 48px-height toggle button pinned to the top of the scroll context
- Category pills in horizontal scroll rows have 8px side padding to prevent accidental adjacent-pill activation

### Collapsing Strategy

- Search bar drops to a full-width second row below logo/cart row on mobile rather than collapsing or hiding
- Filter sidebar transitions from a persistent left-rail on desktop/tablet to a modal overlay drawer on mobile, triggered by a Filter & Sort chip in a sticky sub-header
- Product grid reduces via CSS grid `auto-fill` column reduction (5→4→3→2) without reflowing text nodes
- Nav category links collapse into a horizontal scroll row on tablet and into a hamburger drawer on mobile
- Announcement strip remains visible at all breakpoints but reduces to a single rotating message on mobile

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex value extracted (#313131) — the site was behind Cloudflare anti-bot protection at crawl time, blocking full CSS and token extraction
- Primary red (#cc0000), footer dark (#222222), and all secondary palette values (muted, hairline, surface, rating-star, link) are derived from general brand knowledge of AllPosters, not extracted from live CSS — treat as informed approximations
- No brand-specific typeface detected; Arial/system-ui stack inferred from historical site observation and the extracted system font list; the live site may load a licensed sans-serif via JavaScript after page hydration
- Rating star amber (#f5a623) is a conventional e-commerce default, not confirmed from live CSS
- No meta theme-color tag was present; native mobile browser chrome color (address bar, status bar) is unknown
- Exact border-radius values for buttons and cards could not be confirmed; set to minimal e-commerce conventions matching the utilitarian brand posture
- Dark mode variant tokens not available — site does not appear to declare a prefers-color-scheme dark stylesheet
- Promotional overlay and lightbox component styling not confirmed
