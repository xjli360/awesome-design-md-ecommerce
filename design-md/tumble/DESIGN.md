---
version: alpha
name: "Tumble"
source_url: "https://tumble.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The product photography at Tumble solves a familiar DTC problem — how to sell something flat and square — by staging every rug mid-use: a dog splayed across a patio weave, children's chalk drawings framing a geometric border, a cocktail glass casting a long shadow across the pile. That staging decision shapes the entire visual system. The palette is warm without being rustic: a clay-orange primary (approximated here as #D96C3A, inferred from public catalog imagery in the absence of extracted tokens) anchors the brand against an off-white canvas that photographs well against concrete, wood decking, and coastal grass. Ink falls to a near-black #1A1A1A rather than pure black, keeping body text from reading too sharp against softer surface tones; the surface-soft value (#F5F0EA) carries just enough warmth to suggest sun-washed concrete rather than a clinical laboratory white. Typography runs on a geometric sans-serif in the 400–600 weight range — display headings at 28–40px in weight 500 rather than the heavy 700+ of fashion brands, letting product photography carry the emotional mass. Rounded corners track consistently at {rounded.md} across product cards, buttons, and size selectors, with {rounded.full} reserved for color swatch indicators and the brand's most recognizable UI element: a horizontally scrollable row of pill-shaped filter chips that rearrange the product grid in place without a page reload. Promotional messaging runs above the nav in warm amber (#F0A847) — a honey tone that reads as sunny announcement rather than sale-alarm red. The brand's written voice matches the visual compression: "Machine wash. Air dry. Done." is the entire care instruction, six words where a lifestyle brand would spend twenty-five. That economy extends through the component system — controls are minimal, states are binary-clear, and the rug's own geometry — stripes, diamonds, organics — remains the loudest visual element on every page.

colors:
  primary: "#D96C3A"
  primary-active: "#B8532A"
  primary-disabled: "#EDCABC"
  accent-amber: "#F0A847"
  accent-amber-soft: "#FDF3E0"
  ink: "#1A1A1A"
  body: "#3D3430"
  muted: "#6B5E57"
  muted-soft: "#9E918C"
  hairline: "#E0D8D3"
  hairline-soft: "#EDE8E5"
  canvas: "#FFFFFF"
  surface-soft: "#F5F0EA"
  surface-warm: "#FAF6F1"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  on-amber: "#1A1A1A"
  promo-banner: "#F0A847"
  star-active: "#D96C3A"

typography:
  display-xl:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', 'DM Sans', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Inter', 'DM Sans', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', 'DM Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'DM Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'DM Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'DM Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'DM Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label:
    fontFamily: "'Inter', 'DM Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'DM Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', 'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'DM Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Inter', 'DM Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "'Inter', 'DM Sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Inter', 'DM Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
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
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: 13px 27px
    height: 52px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    rounded: "{rounded.md}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  button-pill-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  button-pill-filter-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.ink}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
  promo-banner:
    backgroundColor: "{colors.promo-banner}"
    textColor: "{colors.on-amber}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-mobile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    overflow: hidden
    imageRounded: "{rounded.md}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    padding: "{spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-amber}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  rug-swatch-selector:
    swatchSize: 32px
    swatchRounded: "{rounded.full}"
    swatchBorderActive: "2px solid {colors.ink}"
    swatchBorderIdle: "1.5px solid {colors.hairline}"
    gap: "{spacing.xs}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    borderActive: "1.5px solid {colors.ink}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    selectedBackground: "{colors.ink}"
    selectedText: "{colors.canvas}"
  category-filter-bar:
    backgroundColor: "{colors.canvas}"
    scrollBehavior: horizontal-scroll
    gap: "{spacing.sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
    chipIdleBackground: "{colors.canvas}"
    chipIdleText: "{colors.ink}"
    chipIdleBorder: "1px solid {colors.hairline}"
    chipActiveBackground: "{colors.ink}"
    chipActiveText: "{colors.canvas}"
    chipRounded: "{rounded.full}"
    chipHeight: 36px
    chipTypography: "{typography.button-sm}"
  product-grid:
    gap: "{spacing.base}"
    padding: "0 {spacing.xl}"
    columnsDesktop: 4
    columnsTablet: 3
    columnsMobile: 2
  hero-full-bleed:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 520px
    contentMaxWidth: 560px
    layout: image-right text-left
    padding: "{spacing.xxl} {spacing.section}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    headerTypography: "{typography.title-md}"
    itemTitleTypography: "{typography.body-sm}"
    itemPriceTypography: "{typography.price-sm}"
  review-summary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    starColor: "{colors.star-active}"
    ratingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label}"
    mutedColor: "{colors.muted-soft}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The main CTA runs in `{colors.primary}` (#D96C3A) with white text, `{rounded.md}` corners, and a 52px height that reads confidently on both mobile and desktop without needing to expand full-width except at the narrowest viewports. On hover the fill deepens to `{colors.primary-active}`; on disabled state it fades to the pale `{colors.primary-disabled}` wash. Padding at 14×28px ensures the button feels generous without dominating the surrounding whitespace.

**`button-secondary`** — Canvas white with a 1.5px `{colors.hairline}` border; hover state tightens the border to `{colors.ink}` and warms the fill to `{colors.surface-soft}`. Sits at the same 52px height as `button-primary` so paired side-by-side CTAs never mismatch. Most commonly appears alongside `button-primary` on the PDP for "Add to Cart" / "Save for Later" pairings.

**`button-ghost`** — Transparent background, `{colors.ink}` text with an underline, `{typography.button-sm}` weight. Used for lower-hierarchy actions — "View all", "Read more", "See size guide" — that must not visually compete with the primary CTA.

**`button-pill-filter`** / **`button-pill-filter-active`** — The brand's most visible UI pattern. Idle state is `{colors.canvas}` with a `{colors.hairline}` border; active state inverts to `{colors.ink}` background with `{colors.canvas}` text. `{rounded.full}` shape at 36px height. These chips populate the `category-filter-bar` and are the primary navigation mechanism on collection pages.

### Text Input

**`text-input`** — 48px height, `{rounded.md}`, `{colors.hairline}` border at rest that upgrades to a 1.5px `{colors.ink}` ring on focus. Placeholder text in `{colors.muted-soft}`. Used for site search and email capture fields; the focus state is the only visible interaction affordance — no shadow or glow.

### Navigation

**`nav-bar`** — 64px white bar with `{typography.nav-link}` links (15px, weight 500), a `{colors.hairline-soft}` bottom border, logo anchored left, cart and account icons right. The promo banner sits above this bar in the DOM — together they form a paired header block before any page content. On mobile, `nav-bar-mobile` drops to 56px and mid-level category links collapse behind a hamburger icon.

**`promo-banner`** — A persistent warm amber stripe above the nav using `{colors.promo-banner}` (#F0A847). Text in `{typography.caption}`, centered. The amber reads as a sunny announcement rather than the alarm-red urgency of discounting brands — consistent with Tumble's lifestyle positioning over pure promotional pressure.

### Product Card

**`product-card`** — `{rounded.md}` card, overflow-hidden image filling the top portion, followed by a title in `{typography.title-sm}` and price in `{typography.price-sm}`. Minimal `{spacing.sm}` padding keeps the grid dense. On hover the card lifts with a subtle box-shadow transition. Promotional `product-card-badge` chips float over the top-left of the image in `{colors.accent-amber}` pill form — "New", "Bestseller", or seasonal labels.

**`rug-swatch-selector`** — A compact row of 32px circular swatches (`{rounded.full}`) appearing beneath the product title on both cards and the PDP. Active swatch carries a 2px `{colors.ink}` ring with a 2px gap; idle swatches carry a 1.5px `{colors.hairline}` border. Swatch fills reflect the actual rug colorway, making the selection immediate and visual rather than text-dependent.

**`size-selector`** — Rectangular chips (`{rounded.sm}`) for rug dimensions (2×3, 4×6, 5×8, 8×10, runner, etc.). Idle: `{colors.canvas}` with `{colors.hairline}` border in `{typography.body-sm}`. Selected: inverts to `{colors.ink}` background with `{colors.canvas}` text. The binary selected/idle state avoids a third intermediate hover color — any chip is either chosen or it isn't.

### Category Filter Bar

**`category-filter-bar`** — A horizontal-scrolling strip of pill chips fixed below the nav on collection pages. Filter facets cover style (Geometric, Solid, Stripe, Abstract), color family, size range, and indoor/outdoor use rating. The scroll container hides the scrollbar on desktop while remaining fully touch-scrollable on mobile. Active chips use `{colors.ink}` fill to stand out from the `{colors.canvas}` idle chips, creating a clear at-a-glance summary of applied filters. No collapse to dropdown — the bar persists at all breakpoints.

### Hero

**`hero-full-bleed`** — Full-width section split between a `{colors.surface-warm}` left text panel and a lifestyle photograph anchored right. Heading at `{typography.display-xl}` in weight 500 (never the heavy 700+ of apparel brands), body copy at `{typography.body-md}`, and a `button-primary` CTA. Minimum height 520px; content column maxes at 560px. The warm off-white background prevents the clinical tension of a pure-white panel and echoes the outdoor surface tones in the photography. On mobile the layout stacks, image above text.

### Cart Drawer

**`cart-drawer`** — A 400px right-side slide-over panel with `{colors.canvas}` background and a `{colors.hairline}` left border. Header in `{typography.title-md}`. Line items carry the product thumbnail (square crop, `{rounded.sm}`), title in `{typography.body-sm}`, and price in `{typography.price-sm}`. A full-width `button-primary` at the bottom converts the drawer into a direct checkout entry point. On mobile the drawer expands full-width.

### Review Summary

**`review-summary`** — A `{colors.surface-soft}` warm panel with a large aggregate rating number in `{typography.display-sm}`, star icons in `{colors.star-active}` (orange-clay to match the brand primary rather than the conventional gold), and individual review text in `{typography.body-sm}`. `{rounded.md}` corners and `{spacing.xl}` internal padding give the module room to read as a distinct trust signal within the PDP rather than a cramped afterthought.

### Footer

**`footer`** — Deep `{colors.ink}` background with `{colors.canvas}` text. Column headers in `{typography.label}` (uppercase, 0.5px tracking, 11px) and link text in `{typography.body-sm}` at weight 400. Muted secondary links use `{colors.muted-soft}`. The dark footer creates a strong visual ground after the warm, light-toned body of the page — the contrast is intentional and abrupt, signaling end-of-page rather than a soft fade.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Two-column product grid; nav collapses to hamburger with slide-over subcategory panel; filter bar scrolls horizontally; hero image stacks above text block; cart drawer expands full-width; swatch rows truncate to 5 with "+N" overflow |
| Tablet | 744–1128px | Three-column product grid; nav shows logo and cart only; filter bar visible and scrollable; hero side-by-side at reduced display-md heading scale; cart drawer at 360px |
| Desktop | 1128–1440px | Four-column product grid; full nav links visible; category filter bar sticky below nav on scroll; hero at full proportions with display-xl heading |
| Wide | > 1440px | Grid constrained to 1440px max-width; outer margins expand; hero content column capped at 560px; no layout changes beyond margin growth |

### Touch Targets

- All filter pill chips maintain minimum 36px height; increase padding to 10px vertical on mobile
- Swatch selectors are 32px circles — bump to 36px minimum on mobile with increased gap to 6px
- Nav icons (cart, menu, account) hold minimum 44×44px tap target via padding extension
- Size selector chips target minimum 40px height on mobile

### Collapsing Strategy

- Category navigation: full link set on desktop; collapses to hamburger below 1128px with subcategories in a slide-over panel
- Filter bar: remains a horizontal scroll row at all breakpoints — no dropdown collapse
- Product grid: steps 4→3→2 columns desktop→tablet→mobile; tablet retains three columns to avoid excessive card size on mid-range viewports
- Hero: image and text stack vertically at < 744px with image rendered first (above the fold) to preserve visual entry
- Cart drawer: side-panel on tablet and desktop; full-screen overlay on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the site returned no CSS color tokens during extraction, likely due to JS-rendered styles or anti-bot protection. Every hex value in this file is inferred from publicly observable catalog imagery and outdoor-brand conventions; treat all as placeholders requiring verification against brand assets.
- **No font family extracted** — typography stack defaults to Inter/DM Sans as plausible geometric sans-serif stand-ins. The actual brand typeface is unconfirmed.
- **No theme-color meta tag** — cannot confirm the primary brand color from the document head; the #D96C3A primary is estimated.
- **Platform unconfirmed** — Shopify detection returned false; the actual e-commerce platform and its default component behaviors (drawer animation, cart state, etc.) are unknown.
- **Motion and animation system** — no transition or keyframe data extractable; hover lift on cards, drawer slide timing, and filter-chip transitions are assumed from DTC conventions.
- **Icon library** — whether Tumble uses a custom icon set, Heroicons, or a third-party system could not be determined.
- **Spacing scale precision** — padding and gap values are estimated at a 16px base unit; the brand may use a tighter or looser rhythm.
- **Dark mode support** — unknown; no dark-mode token data was extractable.
- **Sale and clearance states** — color handling for strike-through pricing, sale badges, and discount labels is not confirmed from extraction.
