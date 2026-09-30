---
version: alpha
name: "Toshiba"
source_url: "https://www.toshiba-lifestyle.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Red as a heat element — that's how #e61e1e lands on Toshiba Lifestyle's pages, appearing not as a decorative accent but as a functional signal: the single action color for primary CTAs, navigation highlights, and category badges across a sprawling Japanese appliance catalog. The canvas is an almost-white #f9f9f9 layered with card surfaces at #ffffff and soft divider bands of #f6f6f6, creating depth without shadow abuse. Typography relies entirely on the Japanese system stack — Hiragino Kaku Gothic ProN falling back to Meiryo — set at modest weights (400 body, 700 display) that let product photography dominate. Four category accent colors partition the product universe: #f376b4 for living/beauty, #369ae9 for cooling/air, #03ad6b for kitchen/eco, #f49b00 for cooking/heat — each paired with a barely-there tinted surface (#fef7fb, #f3f9fe, #f0faf6, #fef9f0) that bleeds behind section cards. Corner radii stay conservative: `{rounded.sm}` on buttons and inputs, `{rounded.md}` on product cards, never reaching pill territory except for small badges. The grid breathes at `{spacing.section}` between major blocks, collapsing to `{spacing.lg}` on mobile where the single-column layout stacks category tiles vertically. Navigation is a sticky white bar with ink-black text, the logo left-aligned, and a hamburger menu on mobile replacing the horizontal category links. Product cards favor a tall aspect ratio — large square image, two-line title in `{typography.title-md}`, a muted model-number caption, then a red price callout when on sale. The overall impression is Japanese consumer-electronics restraint: nothing competes with the product image, color is rationed to one red and four category hues, and whitespace does the structural work that borders would do on a busier site.

colors:
  primary: "#e61e1e"
  primary-active: "#cc1a1a"
  primary-disabled: "#ffd9d9"
  ink: "#333333"
  body: "#5e5e5e"
  muted: "#707070"
  muted-soft: "#777777"
  hairline: "#dedede"
  hairline-soft: "#e7e7e7"
  border-strong: "#b3b3b3"
  canvas: "#ffffff"
  canvas-alt: "#f9f9f9"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-strong: "#f0f0f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#0052cc"
  error: "#ff0000"
  category-living: "#f376b4"
  category-living-bg: "#fef7fb"
  category-air: "#369ae9"
  category-air-bg: "#f3f9fe"
  category-kitchen: "#03ad6b"
  category-kitchen-bg: "#f0faf6"
  category-cooking: "#f49b00"
  category-cooking-bg: "#fef9f0"
  sale-badge: "#ff0008"
  success: "#96cf92"
  divider: "#ededed"

typography:
  display-xl:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  display-md:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  display-sm:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  title-md:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  title-sm:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-lg:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0
  body-md:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0
  body-sm:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.02em
  button-sm:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.02em
  nav-link:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif"
    fontSize: 13px
    fontWeight: 600
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
  section-lg: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: 1px solid {colors.hairline}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.border-strong}
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: 1px solid {colors.hairline}
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: 2px solid {colors.primary}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.divider}
    position: sticky
  nav-bar-logo:
    height: 28px
    color: "{colors.primary}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid {colors.primary}
    padding: 12px 16px
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: 12px 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 0
    border: 1px solid {colors.hairline-soft}
    overflow: hidden
  product-card-image:
    aspectRatio: "1 / 1"
    backgroundColor: "{colors.surface-soft}"
    objectFit: contain
    padding: "{spacing.lg}"
  product-card-body:
    padding: "{spacing.base}"
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.sale-badge}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    minHeight: 480px
    padding: "{spacing.section}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 40px
  category-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline-soft}
    textAlign: center
  category-card-icon:
    height: 64px
    width: 64px
    margin: 0 auto {spacing.md}
  category-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  category-section:
    backgroundColor: "{colors.canvas-alt}"
    padding: "{spacing.section} 0"
  category-badge:
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: 4px 12px
    height: 24px
  category-badge-living:
    backgroundColor: "{colors.category-living-bg}"
    textColor: "{colors.category-living}"
  category-badge-air:
    backgroundColor: "{colors.category-air-bg}"
    textColor: "{colors.category-air}"
  category-badge-kitchen:
    backgroundColor: "{colors.category-kitchen-bg}"
    textColor: "{colors.category-kitchen}"
  category-badge-cooking:
    backgroundColor: "{colors.category-cooking-bg}"
    textColor: "{colors.category-cooking}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: 1px solid {colors.hairline-soft}
    rounded: "{rounded.sm}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    typography: "{typography.spec-label}"
    padding: "{spacing.md} {spacing.base}"
  spec-table-cell:
    padding: "{spacing.md} {spacing.base}"
    borderBottom: 1px solid {colors.divider}
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: none
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: 2px solid {colors.primary}
    rounded: "{rounded.sm}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separator: ">"
    gap: "{spacing.sm}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.md}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  footer-bottom:
    borderTop: 1px solid {colors.hairline}
    padding: "{spacing.lg} 0"
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"

---

## Components

### Buttons

**`button-primary`** — Solid Toshiba red (#e61e1e) with white text, used for all primary conversion actions: "カートに入れる" (add to cart), "詳しく見る" (learn more), form submissions. Hover darkens to `primary-active`; disabled state fades to the soft red wash of `primary-disabled` with reduced opacity. Height is 48px with generous horizontal padding (32px) to give the label breathing room in both Japanese and English text lengths.

**`button-secondary`** — White fill with a 1px hairline border, used alongside primary buttons for lower-priority actions like "比較する" (compare) or "お気に入り" (favorite). On hover, the background shifts to `surface-soft` and the border strengthens. Shares the same 48px height to maintain alignment when placed inline with primary buttons.

**`button-text`** — A borderless, background-free text link styled in `primary` red. Used for inline actions within cards or beneath product descriptions — "スペックを見る" (view specs), "もっと見る" (see more). No minimum height constraint; padding is vertical only.

### Navigation

**`nav-bar`** — A sticky white bar at 64px height with a thin bottom divider. The Toshiba logo (red wordmark) sits left at 28px height; navigation links are horizontally arranged in `nav-link` weight 500 on desktop. A search icon and hamburger menu occupy the right side. On scroll, no background-color change occurs — the bar remains pure white with its subtle border providing separation from content.

**`category-tab-active` / `category-tab-inactive`** — Horizontal category filters beneath the nav on product listing pages. Active state shows `primary` red text with a 2px red bottom border; inactive tabs are `muted` gray with no border. Tabs scroll horizontally on mobile with overflow hidden and touch-drag enabled.

### Product Cards

**`product-card`** — A vertical card with a 1:1 image area (product centered on `surface-soft` background with `contain` fit and inner padding), followed by a body section containing the product title in `title-sm` and price in `price-sm`. The card has `rounded.md` corners and a `hairline-soft` border. No box-shadow is used — the border alone provides edge definition against the canvas. On hover, a subtle border-color darken to `hairline` signals interactivity.

**`product-card-sale-price`** — When a product is on sale, the original price is struck through in `muted` and the sale price appears in `sale-badge` red (#ff0008), bold weight, drawing the eye without any background badge.

### Hero Banner

**`hero-banner`** — Full-width section with a light gray (`surface-soft`) background, minimum 480px tall, holding a large product image and headline text in `display-xl`. No rounded corners — the hero bleeds edge to edge. A single red CTA button (`hero-banner-cta`) sits below the headline with extra-wide padding (40px horizontal) to create visual weight.

### Category System

**`category-card`** — A bordered card with centered icon (64×64) above a `title-md` label. Used on the homepage to direct users into product verticals (microwave, toaster oven, refrigerator, etc.). Cards sit in a responsive grid — 4-up on desktop, 2-up on mobile.

**`category-badge`** — Small pill-shaped badges (`rounded.full`) that color-code product categories. Each category maps to a specific hue: living/beauty is pink, air/cooling is blue, kitchen/eco is green, cooking/heat is amber. The badge uses the light tinted background with the saturated color as text.

### Spec Table

**`spec-table`** — A bordered table with alternating row structure used on product detail pages to display technical specifications (wattage, dimensions, capacity). Header cells use `surface-soft` background with `spec-label` bold type; body cells use standard `body-md` with generous `md` padding. The table has `rounded.sm` corners with overflow hidden.

### Search

**`search-bar`** — A flat input field with `surface-soft` gray background and no visible border in default state. On focus, it switches to white background with a 2px `primary` red border, clearly signaling input readiness. Sits at 44px height with `body-md` typography. Typically positioned in the nav bar or as a prominent element on the support/search page.

### Breadcrumb

**`breadcrumb`** — A compact path trail in `caption` size using ">" separators with `sm` spacing between segments. All ancestors render in `muted` gray; the current page renders in `ink` black. Used on product detail and category pages to provide hierarchical context.

### Footer

**`footer`** — A `surface-strong` gray background section with multi-column link lists. Each column is headed by a `title-sm` bold label followed by `body-sm` links in `muted` gray. A `hairline` top-border separates the bottom row (copyright, legal links) from the link columns above. The footer maintains `section` vertical padding to balance against the content above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger + logo + search icon; hero image stacks above text; product grid becomes 2-up; category tabs horizontally scroll; footer stacks into accordion sections; spec table scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories inline; hero sits at 360px height; footer remains multi-column at 3-up; category cards are 3-up |
| Desktop | 1128–1440px | Full nav with all categories visible; product grid 3–4 up; hero at 480px with side-by-side image and text; spec table at full width; footer at 4-column layout |
| Wide | > 1440px | Content max-width caps at 1440px and centers; increased section padding to `section-lg`; product images scale up slightly within cards; hero may extend to full bleed while content remains constrained |

### Touch Targets

- All interactive elements maintain a minimum 44×44px touch area on mobile
- Category tabs have 12px vertical padding ensuring the tap zone exceeds the visible text
- Product cards are tappable as a single unit (entire card is the hit target)
- Footer accordion headers expand to 48px height on mobile for easy tapping
- Spacing between adjacent tap targets is at minimum `spacing.sm` (8px)

### Collapsing Strategy

- Navigation categories collapse into a slide-out drawer (hamburger trigger, left edge)
- Product filters move from a left sidebar to a bottom-sheet modal on mobile
- Spec tables maintain their two-column (label/value) structure but allow horizontal scroll within a constrained viewport
- Hero banners shift from side-by-side (image + text) to stacked (image top, text below) at the tablet breakpoint
- Footer link columns collapse into expandable accordion sections with a "+" toggle icon

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom web font detected — the site relies on Japanese system fonts (Hiragino Kaku Gothic ProN / Meiryo), so actual rendered weights may vary between macOS and Windows
- No CSS custom properties or design-token layer was extractable; colors were inferred from computed styles on rendered elements
- Exact border-radius values could not be confirmed from extraction — the `rounded` scale is estimated from visual inspection
- Animation/transition timing (easing curves, durations for hover states, drawer slides) was not captured
- Icon system details (SVG sprite vs inline, sizing grid, stroke width) could not be determined from extraction
- The "slick" reference in font stacks is the Slick carousel library class, not a typeface — carousel configuration (autoplay, timing, dots vs arrows) is unknown
- Dark mode: no alternate color scheme was detected; the site appears to be light-only
- Exact grid gutter and max-width values could not be confirmed — spacing scale is inferred from visual patterns
