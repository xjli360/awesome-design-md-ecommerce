---
version: alpha
name: "Write Notepads & Co."
source_url: "https://www.writepads.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The ruled page is this brand's organizing metaphor: #ddfaf4, a barely-there mint that reads like fresh paper catching diffuse studio light, recurs as the primary hero surface, and the payoff arrives when #45bea6 — a seafoam teal with Caribbean warmth — appears as the single active voltage, carrying every cart button, hover ring, price highlight, and focused-input underline. Against it stands #1b175d, a near-indigo navy as dense as dried fountain pen ink, anchoring announcement bars, section headers, and editorial callouts; the brand owns two pigments that map almost literally onto the stationery ritual: blank page and mark made. The rest of the palette keeps its distance — a spine of near-blacks (#121212, #111827, #1f2937) handles body and navigation type; a warm-gray range (#555353, #606060, #6b7280) carries metadata and supporting copy without competing with product photography; hairlines and borders draw from a cooler family (#c7c7c7, #d1d1d1, #e5e7eb), keeping spiral-bound notebooks, brass-ferrule pencils, and matte-finish pen barrels clean and unframed. Typography could not be extracted from the live Shopify theme (see Known Gaps), but the "for Professionals & Creatives" brand positioning calls for a confident geometric or humanist sans-serif at medium weights — display sitting around 28–40px at 600–700, body at 16px/400 — authority earned through restraint rather than typographic muscle. Components follow a Shopify-standard grid inflected with light brand character: product cards wear {rounded.sm} corners and a 1px #d1d1d1 border; primary buttons fill the teal at {rounded.xs}; the mint surface (#ddfaf4) returns in a full-width newsletter band above the footer, echoing the blank-page energy of the hero, while the #121212 footer beneath it closes the page like a notebook cover laid flat. {rounded.full} appears only in the search icon affordance and circular icon buttons, never on primary CTAs.

colors:
  primary: "#45bea6"
  primary-hover: "#3aaa94"
  primary-active: "#349e8a"
  primary-disabled: "#a8ddd5"
  navy: "#1b175d"
  navy-active: "#13104a"
  mint-surface: "#ddfaf4"
  ink: "#121212"
  body: "#1f2937"
  muted: "#606060"
  muted-soft: "#6b7280"
  mid-gray: "#555353"
  hairline: "#d1d1d1"
  hairline-soft: "#e5e7eb"
  hairline-strong: "#c7c7c7"
  subtle-gray: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#ddfaf4"
  surface-card: "#ffffff"
  surface-neutral: "#f3f4f6"
  on-primary: "#ffffff"
  on-navy: "#ffffff"
  sale-red: "#c0392b"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-caps:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  announcement:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px

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
    padding: 13px 24px
    height: 48px
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
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.hairline-strong}"
    borderHover: "1.5px solid {colors.primary}"
    backgroundHover: "{colors.surface-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 23px
    height: 48px
  button-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 24px
    height: 48px
  button-navy-active:
    backgroundColor: "{colors.navy-active}"
    textColor: "{colors.on-navy}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 14px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
  announcement-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.announcement}"
    padding: 10px {spacing.base}
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "4/5"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.body}"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.08)"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 540px
    padding: "{spacing.xxl} {spacing.section}"
    ctaComponent: button-primary
  collection-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-navy}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    overlay: "linear-gradient(to top, rgba(27,23,93,0.55) 0%, transparent 60%)"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-bestseller:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  search-bar:
    backgroundColor: "{colors.surface-neutral}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    textColor: "{colors.ink}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 44px
    padding: 0 {spacing.base}
  search-icon-button:
    backgroundColor: "{colors.canvas}"
    iconColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 44px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    buttonHoverColor: "{colors.primary}"
    height: 44px
    width: 120px
  product-option-swatch:
    border: "1.5px solid {colors.hairline}"
    borderSelected: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    size: 36px
    gap: "{spacing.sm}"
  breadcrumb:
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.subtle-gray}"
    linkColor: "{colors.subtle-gray}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
    copyrightTypography: "{typography.caption}"
    copyrightColor: "{colors.muted-soft}"
  newsletter-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.xxl}"
    inputComponent: text-input
    ctaComponent: button-primary
  mini-cart-drawer:
    backgroundColor: "{colors.canvas}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    headingTypography: "{typography.title-md}"
    headingColor: "{colors.ink}"
    badgeBackgroundColor: "{colors.primary}"
    badgeTextColor: "{colors.on-primary}"
  promo-section-card:
    backgroundColor: "{colors.mint-surface}"
    textColor: "{colors.navy}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxl}"
    border: "none"

## Components

### Buttons

**`button-primary`** — The principal CTA fills in the seafoam teal (#45bea6) with white type at `{typography.button-md}` weight, carrying 13px/24px padding to a 48px height and `{rounded.xs}` corners — minimal radius that reads as professional rather than playful. Hover nudges the fill to #3aaa94; active deepens to #349e8a; disabled washes out to #a8ddd5, the color of a pen running dry.

**`button-secondary`** — A white canvas outlined variant with a 1.5px #c7c7c7 border, matching height and type scale to `button-primary`. On hover the border lifts to teal and the background gains a #ddfaf4 tint, creating a clear two-level hierarchy without abrupt contrast shifts.

**`button-navy`** — Deep #1b175d fill used in announcement bars, sale callouts, and editorial sections where the teal would compete with product photography. Shares the same 48px height and `{typography.button-md}` type scale as the primary for visual alignment across contexts.

### Navigation

**`nav-bar`** — 64px tall, white canvas, anchored by a single 1px #d1d1d1 bottom border. Brand logo sits left; desktop links in `{typography.nav-link}` occupy the center; cart count, search, and account icons fill the right. On scroll the bar stays fixed with no opacity animation — the border alone signals elevation.

**`announcement-bar`** — 40px #1b175d navy band that spans the full viewport above the nav, reversed white type at 13px/500. Carries free-shipping thresholds and promotional codes. Functions visually as a notebook-cover band — the same deep ink blue that bookcovers and spines carry.

### Product Card

**`product-card`** — Rectangular card with 1px #d1d1d1 border and `{rounded.sm}` corners, housing a 4:5 portrait image that fills the upper portion. Below: title at `{typography.title-sm}`, price at `{typography.price-display}`, and optional badge positioned absolute at the top-left of the image. Hover lifts with a 4px 16px rgba shadow. No inline add-to-cart — the brand routes through the full PDP.

### Hero Banner

**`hero-banner`** — #ddfaf4 mint or white canvas background, `{typography.display-xl}` headline, `{typography.body-md}` supporting copy, and a single `button-primary` CTA. Minimum 540px tall on desktop with `{spacing.xxl}` vertical and `{spacing.section}` horizontal padding. The mint surface is the brand's most direct invocation of blank-page energy on the digital screen.

### Collection Card

**`collection-card`** — Full-bleed photography card with a `linear-gradient(to top, rgba(27,23,93,0.55) 0%, transparent 60%)` overlay — the navy from #1b175d used as the gradient anchor so the shadow reads on-brand rather than generic black. Collection name sits reversed in `{typography.title-md}` weight above the fade line.

### Badges

**`badge-new`** — Teal (#45bea6) pill at `{typography.label-caps}` (11px/600/uppercase/0.8px tracking), 3px × 8px padding, `{rounded.xs}` corners, positioned absolute top-left over product card images. **`badge-bestseller`** mirrors the shape in #1b175d navy. The two badge types never appear on the same card, keeping signal clean.

**`badge-sale`** — Red (#c0392b) fill, same label-caps type and rounded. Used exclusively in clearance and sale pricing contexts; the red is the only departure from the core teal/navy palette and signals urgency without decorative intent.

### Search

**`search-bar`** — Full-width overlay triggered from the nav search icon (a `{rounded.full}` circle button). 44px input height, `{colors.surface-neutral}` background, `{rounded.xs}` corners, 1px #d1d1d1 border that upgrades to 1.5px teal on focus. Muted magnifying-glass icon leads the field. Autocomplete results drop in a card panel with `{rounded.sm}` corners and a soft shadow.

### Newsletter Callout

**`newsletter-callout`** — Full-width #ddfaf4 stripe placed above the footer with no border-radius on the outer container — it bleeds edge to edge as a page-spanning band. `{typography.display-sm}` heading, `{typography.body-md}` subtext, inline email `text-input` paired with `button-primary`. The mint recurrence here bookends the page against the hero's opening surface.

### Footer

**`footer`** — Near-black (#121212) background that reads as a closed notebook cover. Four-column layout on desktop: brand statement or logo left, then Product, Company, and Support link columns. Links in #dedede, section headings in white `{typography.title-sm}`. Bottom strip carries copyright in `{colors.muted-soft}` at `{typography.caption}`. No top border — the background transition is separation enough.

### Mini Cart Drawer

**`mini-cart-drawer`** — 400px right-panel overlay with white background and 1px #d1d1d1 left border. Product rows carry 64px square thumbnails. Cart icon badge in `{colors.primary}` fill with `{colors.on-primary}` text. Checkout CTA at drawer base uses `button-primary` full width.

### Promo Section Card

**`promo-section-card`** — Mint (#ddfaf4) card used in editorial grid sections to spotlight featured products, gift guides, or maker stories. Deep navy #1b175d text at `{typography.display-sm}` heading weight creates the highest-contrast pairing in the palette. `{rounded.sm}` corners, no border, `{spacing.xxl}` internal padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo + cart icon; hero stacks headline above image; announcement-bar wraps to two lines; mini-cart drawer expands to full viewport width |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + collapsed hamburger menu + cart/search icons; hero uses split layout at reduced padding; footer collapses to two columns |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with all category links visible; hero at full 540px height; footer four-column |
| Wide | > 1440px | Max-width container (~1440px) centered with generous side margins; grid and hero content constrain to container; no new layout shifts beyond white-space breathing room |

### Touch Targets

- Primary and secondary buttons maintain 48px minimum height at all breakpoints
- Cart, search, and account icons hit 44px × 44px minimum tap target on mobile
- Quantity selector increment and decrement buttons maintain 44px height with adequate horizontal tap zone
- Product option swatches are minimum 36px × 36px with 8px gap between adjacent options
- Announcement bar links carry 40px full-height tap target by default

### Collapsing Strategy

- Navigation: full horizontal links collapse to a full-height slide-in drawer at < 1024px; drawer overlays with white background and close button top-right; sub-navigation expands inline with accordion
- Footer: four columns → two columns at tablet → single stacked column at mobile; legal/copyright strip always renders below all content columns
- Hero banner: side-by-side split layout collapses to stacked image-above-text at < 744px; min-height reduces from 540px to auto
- Collection card grid: 4-up desktop → 2-up tablet → 2-up compact mobile with reduced card height
- Product card image aspect ratio (4:5) preserved at all breakpoints; card width follows the column grid

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family stacks were extracted from the live Shopify theme; typography uses a Helvetica Neue / system-ui fallback and must be validated against the actual brand typeface before production use
- The site likely loads webfonts via Shopify CDN or a JS-injected stylesheet that was not captured in the extraction pass
- Meta theme-color was absent; no OS-level browser chrome accent color could be confirmed
- Exact button and card border-radius values are inferred from the brand's professional positioning — live component measurements were not captured
- Hover and active color variants for the primary teal (#45bea6) are derived by proportional darkening — no explicit hover hex was present in the extracted palette
- Sale badge red (#c0392b) follows e-commerce convention; no red was present in the extracted hex list and this value is not confirmed from the live site
- Animation timing, easing curves, and transition durations for hover states, drawer behavior, and cart interactions were not captured
- Exact header height and sticky-scroll behavior could not be confirmed from extraction alone
- Dark-mode or alternate color scheme support is unknown; the extracted palette shows no dark-surface tokens beyond the near-black ink colors
