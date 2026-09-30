---
version: alpha
name: "Sideshow"
source_url: "https://www.sideshow.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every product page on sideshow.com operates as a theatrical stage rather than a storefront — near-black backgrounds (#0d0d0d) hold each figure in dramatic isolation, the way a museum vitrine uses black velvet to silence competing visual noise. Gold (#c9a96e) appears as the single warm voltage threading through edition callouts, primary CTAs, and the thin ruled lines that separate editorial copy from pricing; it reads less like a brand accent and more like a provenance stamp pressed into dark materials. The brand's structural tension is between the sculptural seriousness of its products — hand-painted 1:1 life-size busts, hyper-detailed sixth-scale figures cast in polystone — and the transactional necessity of an e-commerce platform; the design resolves this by letting hero photography bleed edge-to-edge and confining interface chrome to {colors.surface-card} panels that feel closer to gallery plaques than UI widgets. Display typography runs bold and condensed with tight tracking, evoking the credit sequences of the licensed properties (Star Wars, Marvel, DC, Lord of the Rings) that dominate the catalog; body copy runs light-weight sans on dark backgrounds for high contrast without the severity of pure white-on-black. Product cards float on {colors.surface-card} with a 1px {colors.hairline} border demarcating the collectible's frame from the surrounding field, and on hover the border transitions to {colors.primary} with a faint gold inner glow — the active card feels lit from within. Collector-status badges — "Premium Format," "Polystone," "Sixth Scale," "Sideshow Exclusive" — appear as all-caps tracked labels in {colors.gold}, functioning as provenance stamps rather than promotional stickers. The checkout and layaway flow (Sideshow's FlexPay) interrupts the cinematic dark aesthetic only minimally, keeping form surfaces in {colors.surface-soft} rather than switching to a light canvas.

colors:
  primary: "#c9a96e"
  primary-active: "#b8904f"
  primary-disabled: "#6b5a3a"
  ink: "#ffffff"
  body: "#d4d4d4"
  muted: "#8a8a8a"
  hairline: "#2e2e2e"
  canvas: "#0d0d0d"
  surface-soft: "#151515"
  surface-card: "#1c1c1c"
  surface-raised: "#242424"
  on-primary: "#0d0d0d"
  on-dark: "#ffffff"
  gold: "#c9a96e"
  gold-muted: "#8a6f4a"
  error: "#e05252"
  badge-exclusive: "#7b3fa0"
  badge-new: "#2a6dd9"
  star-rating: "#c9a96e"
  scrim: "#000000"
  price-discount: "#e05252"

typography:
  display-xl:
    fontFamily: "'Oswald', 'Barlow Condensed', 'Arial Narrow', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Oswald', 'Barlow Condensed', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
    textTransform: uppercase
  display-md:
    fontFamily: "'Oswald', 'Barlow Condensed', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Oswald', 'Barlow Condensed', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.3px
  badge-label:
    fontFamily: "'Oswald', 'Barlow Condensed', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  edition-stamp:
    fontFamily: "'Oswald', 'Barlow Condensed', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 2px
    textTransform: uppercase
  price-display:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Oswald', 'Barlow Condensed', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Oswald', 'Barlow Condensed', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 10px 20px
  button-wishlist:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    width: 40px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
    focusBorder: "1px solid {colors.primary}"
  nav-bar-top-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    height: 32px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "3/4"
    padding: "{spacing.md}"
    badgePosition: top-left
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 16px rgba(201,169,110,0.15)"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    minHeight: 600px
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.xl}"
  edition-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.edition-stamp}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  badge-exclusive:
    backgroundColor: "{colors.badge-exclusive}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  product-detail-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  price-block:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
    discountColor: "{colors.price-discount}"
    layawayColor: "{colors.primary}"
  star-rating-row:
    starColor: "{colors.star-rating}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
    activeColor: "{colors.body}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 42px
    iconColor: "{colors.muted}"
    focusBorder: "1px solid {colors.primary}"
  category-filter-pill:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
  category-filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
    padding: 6px 14px
  promo-banner:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    borderLeft: "3px solid {colors.primary}"
    padding: "{spacing.base} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.primary}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Sharp, corner-free gold CTA (`{rounded.none}`) used for "Add to Cart," "Pre-Order Now," and checkout actions. All-caps `{typography.button-md}` with 1.5px letter-spacing reads as a label cast in metal rather than a digital affordance. Active state drops to `{colors.primary-active}` (darker amber) to confirm press without losing the gold vocabulary; disabled state renders in `{colors.primary-disabled}` with `{colors.muted}` text, appearing consistently on sold-out or out-of-edition items.

**`button-secondary`** — Transparent fill with a `1px solid {colors.primary}` border and gold text, used for "Notify Me When Available," "View Details," and secondary confirmations. Keeps the gold brand signal present while reserving the filled treatment exclusively for primary transactional intent; never competes visually with the adjacent primary button.

**`button-ghost`** — Hairline-bordered, body-colored button on dark surfaces. Handles pagination controls, sort dropdowns, and filter resets. Text stays in `{colors.body}` rather than gold so these controls recede visually behind primary actions.

**`button-wishlist`** — Circular icon-only button (`{rounded.full}`, 40×40px) with a hairline border, holding a heart or bookmark glyph in `{colors.muted}`. Appears as an overlay on product card images on hover; the circular form is the only rounded element in an otherwise sharp-cornered component system.

### Navigation

**`nav-bar-top-strip`** — A 32px gold bar (`{colors.primary}`) anchoring the top of every page. Carries promo codes, free-shipping thresholds, and flash-sale countdowns in all-caps `{typography.badge-label}` text on `{colors.on-primary}`. This gold band establishes premium positioning before the user sees a single product image.

**`nav-bar`** — 64px near-black bar with a bottom hairline separator. Logo anchors left; top-level category links (New Arrivals, Statues, Sixth Scale, Props, Apparel) center in `{typography.nav-link}`; search, account, and cart icons cluster right. No frosted glass or blur — the bar stays fully opaque to preserve dark consistency even over scrolled content.

### Product Cards

**`product-card`** — `{colors.surface-card}` panel with a 1px hairline border and a 3:4 portrait image ratio, framing figures the way they appear in their collector packaging. Title in `{typography.title-md}` white; price in `{typography.price-display}`; edition and license badges stack top-left in `{typography.edition-stamp}`. Hover state transitions the border to `{colors.primary}` and adds a faint gold outer glow (`box-shadow: 0 0 16px rgba(201,169,110,0.15)`), making the focused card appear lit from within the dark grid.

### Badges

**`edition-badge`** — Square-cornered gold stamp (`{colors.primary}`, `{rounded.none}`) for material and format callouts: "Premium Format Figure," "Polystone," "Sixth Scale," "Life-Size." Text runs in `{typography.edition-stamp}` (all-caps, 2px tracking, 4px vertical padding). These are provenance identifiers, not discount ribbons — they describe craft and scale rather than savings.

**`badge-exclusive`** — Purple-fill (`{colors.badge-exclusive}`) stamp reserved for Sideshow Exclusive variants that include bonus accessories or alternate portraits unavailable through third-party retailers. Shares the top-left badge stack with `edition-badge`, differentiated by hue alone so collectors can identify exclusivity in a grid scan.

**`badge-new`** — Blue-fill (`{colors.badge-new}`) for recently listed items. Visually quieter than the gold edition badge so it doesn't compete with provenance information; removed automatically once an item ages past a defined window.

### Hero & Editorial

**`hero-banner`** — Full-bleed image panel, `minHeight: 600px`, with product photography bleeding to all four edges. Headline in `{typography.display-xl}` (uppercase, tight leading) overlays a dark gradient scrim on the left third of the image, reading like a film title card. Primary CTA and secondary CTA align horizontally directly below the headline. No border-radius anywhere in this component — sharp edges reinforce the cinematic seriousness.

**`promo-banner`** — `{colors.surface-raised}` strip with a 3px left border in `{colors.primary}`. Used for pre-order ship-window estimates, FlexPay layaway callouts, and low-inventory warnings. The gold left accent is the only color in an otherwise neutral component, directing attention without triggering alarm.

### Product Detail

**`product-detail-panel`** — Right-hand panel on the product detail page, full-width within its grid column. Contains price block, edition badges, "Add to Cart" and layaway CTA, then a spec accordion covering scale, materials, dimensions, artist credits, and edition size. Sharp corners (`{rounded.none}`), `{spacing.xl}` internal padding, and generous row spacing keep dense specification data breathable.

**`price-block`** — Three-row pricing structure common on pre-orders: full price in `{typography.price-display}` white; crossed-out MSRP in `{colors.price-discount}` when discounted; FlexPay installment amount in `{colors.primary}` on the third row. The gold installment figure uses the same brand accent as edition badges, subtly equating payment accessibility with collector value.

### Search & Filters

**`search-bar`** — `{colors.surface-soft}` input with a `{colors.muted}` magnifier icon embedded left. On focus, border transitions to `{colors.primary}` with no animation delay. Autocomplete dropdown renders on `{colors.surface-card}` with hairline-separated suggestion rows; matching text in the suggestion highlights in `{colors.primary}`.

**`category-filter-pill`** / **`category-filter-pill-active`** — Horizontal scrolling row above product grids. Inactive pills use hairline borders and `{colors.muted}` text; active pills fill gold (`{colors.primary}`) with `{colors.on-primary}` dark text. Filter dimensions: license property, format/scale, material, availability (In Stock, Pre-Order, Waitlist), and price range. Multiple pills can be active simultaneously.

### Footer

**`footer`** — Four-column link grid on `{colors.surface-soft}`, separated from canvas by a top hairline. Column headers in `{typography.title-sm}` body-white; links in `{typography.body-sm}` weight 300 muted, transitioning to `{colors.primary}` on hover. Newsletter signup and social icons occupy the rightmost column. Legal copy in `{typography.caption}` at `{colors.muted}`. No illustration or decorative treatment — the footer is strictly navigational.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + search icon + cart; hero text stacks full-width above a bottom-aligned CTA pair; filter pills scroll horizontally below a sticky "Filter & Sort" toggle |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + top-level category links + icons (no sub-labels); hero uses 50/50 image-text split; filter panel slides in as a right-side drawer |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with all category links and mega-menu on hover; PDP uses two-column layout (image gallery left, detail panel right) |
| Wide | > 1440px | Grid stays at four columns; page content max-width caps at 1440px with `{colors.canvas}` gutter fill on both sides; hero image scales proportionally while text column stays fixed-width |

### Touch Targets
- All interactive elements minimum 44×44px on mobile; wishlist circle button extends its hit area via transparent padding beyond the 40px visible circle
- Filter pills minimum 36px tall with horizontal padding ensuring comfortable tap width on a dense horizontal scroll row
- Nav hamburger is a 48×48px invisible tap region centered on the visible icon
- Product card touch target is the full card face including the image; no tappable sub-zones within the card at mobile widths

### Collapsing Strategy
- Promo top-strip remains visible at all breakpoints — only the nav bar itself collapses to icons on mobile
- Filter pill row collapses to a single "Filter & Sort" bottom-sheet trigger on mobile; filter state persists when the sheet closes
- PDP spec accordion defaults to all sections collapsed on mobile; each section header is a 48px tap target
- Badge stack on product cards caps at two badges on mobile; overflow badges are suppressed (not truncated with "+N") to preserve card legibility
- Footer four-column grid collapses to a single-column accordion on mobile; each column header acts as the expand/collapse trigger

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors could be extracted from the live site — the site likely renders design tokens via JavaScript or has anti-bot protection active during scraping. All color values above are estimated from widely observable brand UI patterns and should be validated with DevTools before shipping.
- No font families were extracted. Typography stacks above use condensed sans-serif (Oswald/Barlow Condensed) for display/badge text and geometric sans (Roboto/Helvetica Neue) for body/nav, inferred from the visual character of headings and body copy visible in public product pages — exact web font names require live DevTools inspection of the `@font-face` declarations.
- The `{rounded.none}` assumption for primary buttons and detail panels is inferred from the brand's hard-edge cinematic aesthetic; actual border-radius values are unconfirmed and may be 2–4px.
- Dark-mode vs. light-mode checkout strategy is unconfirmed — the primary site appears fully dark but the FlexPay / payment flow may switch to a lighter surface.
- Exact FlexPay installment UI (calculator widget, payment-plan selector) could not be modeled without an authenticated session on an active pre-order; the `price-block` three-row pattern is inferred from public product screenshots.
- Icon glyph library is unconfirmed (could be a custom SVG set or a licensed icon system such as Font Awesome Pro or Phosphor).
- Hover animation timing curves and transition durations are unspecified; the gold border glow on `product-card-hover` is a design recommendation, not an extracted value.
