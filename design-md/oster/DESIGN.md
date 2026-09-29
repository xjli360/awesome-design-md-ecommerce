---
version: alpha
name: "Oster"
source_url: "https://www.oster.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Brushed stainless steel on a white laminate counter — that is the image Oster builds every page around, and the entire design system exists to stay out of the photograph's way. The sole brand accent is a saturated warm red (#DA291C) pulled from decades of packaging, blister cards, and the wordmark lockup; it fires on "Add to Cart" bars, sale callouts, and the persistent mobile CTA strip, always set against `{colors.on-primary}` white at contrast ratios well above 4.5:1. Ink sits at #313131, a soft charcoal that avoids the clinical edge of true black and pairs naturally with the system-native font stack headed by -apple-system, Segoe UI, and Roboto — Oster treats typography as plumbing, not decoration, letting product photography carry the visual weight. Display headings land between 28–36px at weight 700, heavy enough to anchor spec-dense detail pages where wattage, cubic-foot capacity, and preset counts compete for attention, while body copy at 16px/1.5 in weight 400 keeps feature lists and care instructions scannable across a long vertical scroll. A dark navy-charcoal (#2D3142) surfaces in the top navigation bar, the footer, and comparison-table headers, grounding the red without competing for attention. Cards use `{rounded.sm}` corners with a 1px `{colors.hairline}` border and zero drop-shadow — utilitarian, catalog-grid clean — while product imagery fills a fixed 4:3 frame on a `{colors.surface-soft}` neutral background that makes chrome finishes pop. Buttons are compact rectangles (`{rounded.xs}`, 48px tall, 14px vertical padding) sized for toolbar-style filter bars yet comfortable enough for touch. Sale badges snap to the card's top-left with `{spacing.sm}` inset, using `{typography.badge}` uppercase type at 11px/700 on the same `{colors.primary}` red. The layout grid caps at 1280px with `{spacing.section}` vertical rhythm between hero, feature grid, comparison table, and review blocks — an appliance showroom rendered in markup, with just enough red to steer the eye toward conversion.

colors:
  primary: "#DA291C"
  primary-active: "#B8221A"
  primary-disabled: "#F2B3AE"
  secondary: "#2D3142"
  secondary-active: "#1F2233"
  ink: "#313131"
  body: "#4A4A4A"
  muted: "#767676"
  muted-soft: "#999999"
  hairline: "#D9D9D9"
  hairline-soft: "#EBEBEB"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  surface-strong: "#EDEDED"
  on-primary: "#FFFFFF"
  on-secondary: "#FFFFFF"
  on-dark: "#FFFFFF"
  success: "#2E7D32"
  error: "#C13515"
  error-soft: "#FCE4E0"
  star-rating: "#F5A623"
  sale: "#DA291C"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.2px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
    textDecoration: line-through
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0
  spec-value:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline

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
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
    opacity: 1
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 1px solid "{colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 1px solid "{colors.ink}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 48px
    height: 52px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    border: 1px solid "{colors.ink}"
  text-input-error:
    border: 1px solid "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline}"
  nav-bar-promo:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid "{colors.primary}"
  nav-link-inactive:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    border: 1px solid "{colors.hairline-soft}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "4:3"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-hover:
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
    border: 1px solid "{colors.hairline}"
  product-card-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: absolute
    inset: "{spacing.sm} auto auto {spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 480px
    padding: "{spacing.xxl} {spacing.xl}"
  hero-banner-headline:
    typography: "{typography.display-xl}"
  hero-banner-subline:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    imageAspect: "1:1"
  sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  rating-stars:
    filledColor: "{colors.star-rating}"
    emptyColor: "{colors.hairline}"
    size: 16px
    gap: 2px
  price-block-current:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  price-block-compare:
    textColor: "{colors.muted}"
    typography: "{typography.price-compare}"
  price-block-sale:
    textColor: "{colors.sale}"
    typography: "{typography.price-display}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    stripedRow: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    rowPadding: "{spacing.md} {spacing.base}"
    border: 1px solid "{colors.hairline-soft}"
  comparison-table:
    headerBackground: "{colors.secondary}"
    headerText: "{colors.on-secondary}"
    headerTypography: "{typography.title-md}"
    cellPadding: "{spacing.base}"
    border: 1px solid "{colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    iconColor: "{colors.muted}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: 1px solid "{colors.ink}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
    border: 1px solid "{colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separator: "/"
    gap: "{spacing.sm}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline-soft}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link-hover:
    textColor: "{colors.on-secondary}"
    textDecoration: underline
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderBottom: 1px solid "{colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0"

---

## Components

### Buttons
**`button-primary`** — A solid `{colors.primary}` red rectangle with `{rounded.xs}` corners and `{typography.button-lg}` white text at weight 600. On hover the background darkens to `{colors.primary-active}` (#B8221A) with a 150ms ease transition; focus shows a 2px offset outline in `{colors.primary}`. The disabled state swaps to `{colors.primary-disabled}` (#F2B3AE) with no pointer cursor. Minimum width of 160px prevents visual collapse on short labels.

**`button-secondary`** — White fill with a 1px `{colors.ink}` border and charcoal text, sharing the primary button's dimensions and `{typography.button-lg}` type. On hover the background shifts to `{colors.surface-soft}` while the border remains. Used for secondary actions — "Compare Models," "View Specs," "Save for Later" — wherever a red CTA would overpower the hierarchy.

**`button-add-to-cart`** — A full-width variant of the primary button stretched to 52px height with generous horizontal padding, reserved for the product detail page's purchase zone. It sits below the price block and above the spec summary. On mobile it detaches from flow and becomes a sticky bar fixed to the viewport bottom with `{spacing.base}` padding and a top `{colors.hairline}` border.

### Text Inputs
**`text-input`** — A 48px-tall field with `{rounded.xs}` corners, a 1px `{colors.hairline}` border, and `{typography.body-md}` text. Placeholder text renders in `{colors.muted-soft}`. On focus the border switches to `{colors.ink}`; error states use `{colors.error}` (#C13515) with an inline error message below in `{typography.caption}`. Used across newsletter signup, search overlays, and checkout forms.

### Navigation
**`nav-bar`** — A 64px-tall white bar separated from content by a 1px `{colors.hairline}` bottom border. The Oster wordmark anchors left, category links center in `{typography.nav-link}` at weight 500, and cart/search/account icons sit right. The active link gains a 2px `{colors.primary}` red underline.

**`nav-bar-promo`** — A 40px utility bar in `{colors.secondary}` dark navy-charcoal sitting above the main nav, carrying centered promotional text ("Free Shipping on Orders $50+" or "Memorial Day Sale") in `{typography.caption}` white. Dismissible via a small close icon at the right edge.

### Product Cards
**`product-card`** — A vertical card with a 4:3 product image on a `{colors.surface-soft}` background, `{rounded.sm}` corners, and a faint 1px `{colors.hairline-soft}` border. Below the image, `{spacing.base}` padding wraps the product name in `{typography.title-md}`, a star-rating row using `{colors.star-rating}` filled icons, and the price in `{typography.body-sm}`. On hover a soft box-shadow lifts the card and the border strengthens to `{colors.hairline}`. Sale badges use `{typography.badge}` uppercase white on `{colors.sale}` red, positioned at the image's top-left with `{spacing.sm}` inset.

### Hero Banner
**`hero-banner`** — A full-width section with 480px minimum height, split between a lifestyle photograph (60% width on desktop) and a text block carrying `{typography.display-xl}` headline, `{typography.body-lg}` subline in `{colors.body}`, and a primary CTA button. The `{colors.surface-soft}` background separates the hero from the white canvas above and below. On mobile the layout stacks vertically — image on top, text below at full width with `{spacing.lg}` padding.

### Category Tiles
**`category-tile`** — Square tiles with 1:1 product-category imagery, `{rounded.sm}` corners, and a `{typography.title-md}` label. Arranged in a responsive CSS grid: four columns on desktop, two on tablet, horizontal scroll on mobile. The `{colors.surface-soft}` fill distinguishes tiles from the page canvas.

### Price Block
**`price-block-current`** — The current price in `{typography.price-display}` at `{colors.ink}`. When a sale is active, the original price appears beside it in `{typography.price-compare}` with strikethrough in `{colors.muted}`, and the reduced price renders in `{colors.sale}` red. The two values sit side-by-side with `{spacing.sm}` gap.

### Spec & Comparison Tables
**`spec-table`** — An alternating-row table with `{colors.surface-soft}` stripes. Labels sit in the left column using `{typography.spec-label}` at weight 600; values use `{typography.spec-value}` at weight 400 on the right. Row padding is `{spacing.md}` vertical by `{spacing.base}` horizontal. A 1px `{colors.hairline-soft}` border separates rows.

**`comparison-table`** — A horizontal comparison grid with `{colors.secondary}` header cells carrying product names in `{typography.title-md}` white text. Body cells use `{colors.hairline}` borders and `{spacing.base}` padding. On mobile the first column (spec label) becomes sticky while the product columns scroll horizontally.

### Search Bar
**`search-bar`** — A 44px input with `{colors.surface-soft}` fill, `{rounded.xs}` corners, and a magnifying-glass icon in `{colors.muted}` at the left edge. Placeholder text uses `{typography.body-md}` in `{colors.muted}`. On focus the fill switches to `{colors.canvas}` and the border appears in `{colors.ink}`. Suggestion dropdown renders in a white card below with `{typography.body-sm}` items.

### Filter Chips
**`filter-chip`** — Outlined chips with a 1px `{colors.hairline}` border, `{typography.button-sm}` text, and `{rounded.xs}` corners for catalog filtering (appliance type, price range, finish color). Active chips invert to `{colors.ink}` fill with `{colors.on-dark}` white text. Chips wrap on wider viewports and scroll horizontally on mobile with `{spacing.sm}` gap between items.

### Rating Stars
**`rating-stars`** — A row of 16px star icons filled with `{colors.star-rating}` (#F5A623) amber. Unfilled stars use `{colors.hairline}` gray. Stars are separated by 2px gaps. The numeric rating and review count follow in `{typography.body-sm}` with `{spacing.xs}` gap.

### Breadcrumbs
**`breadcrumb`** — A horizontal trail using `{typography.caption}` in `{colors.muted}` separated by "/" characters with `{spacing.sm}` gaps. The final item renders in `{colors.ink}` without a link. Positioned above the product title on detail pages with `{spacing.md}` bottom margin.

### Footer
**`footer`** — A full-width block in `{colors.secondary}` navy-charcoal with four-column link groups in `{typography.body-sm}`. Links use `{colors.hairline-soft}` and underline on hover. The Oster logo appears in white above the columns, followed by a newsletter signup input, social-media icons, and a legal/copyright row. Padding is `{spacing.xxl}` vertical by `{spacing.xl}` horizontal. On mobile, columns collapse into accordion sections.

### Accordion
**`accordion`** — Vertically stacked expandable sections with `{typography.title-md}` labels and a bottom border in `{colors.hairline-soft}`. Expanded content uses `{typography.body-sm}` in `{colors.body}` with `{spacing.base}` padding. A chevron icon rotates 180 degrees on open. Used in mobile footer navigation, product FAQ sections, and spec groupings.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid. Hero stacks vertically (image over text). Nav collapses to hamburger menu with slide-out drawer. Add-to-cart becomes a sticky bottom bar. Comparison table scrolls horizontally with sticky first column. Footer columns collapse into accordions. Filter chips scroll horizontally. Promo bar text truncates with ellipsis. |
| Tablet | 744–1128px | Two-column product grid. Hero image shrinks to 50% width beside text. Nav shows top-level categories with overflow in a "More" dropdown. Comparison table displays up to 3 products. Category tiles show in a 2-column grid. |
| Desktop | 1128–1440px | Four-column product grid within 1280px max-width container. Full horizontal nav with all categories visible. Hero at full 60/40 image-text split. Spec and comparison tables at full width. Footer in four columns. |
| Wide | > 1440px | Content remains at 1280px max-width, centered. Increased `{spacing.section}` between major blocks. Hero image may bleed to viewport edge while text stays within container. |

### Touch Targets
- All interactive elements maintain a minimum 44x44px tap area on mobile
- Product card tap target covers the entire card surface, not just the title text
- Filter chips maintain `{spacing.sm}` gap to prevent mis-taps
- Sticky add-to-cart bar is 52px tall with the full-width button
- Nav hamburger icon and cart/search icons are 44x44px with adequate padding
- Accordion headers provide a 48px minimum hit area

### Collapsing Strategy
- Navigation: full horizontal links -> hamburger with slide-out drawer below 744px
- Product grid: 4 columns -> 2 columns -> 1 column
- Hero banner: side-by-side 60/40 split -> stacked, image on top
- Footer: four columns -> accordion sections on mobile
- Comparison table: full grid -> horizontally scrollable with sticky label column
- Spec table: two-column layout maintained at all sizes, full-width on mobile
- Category tiles: 4-column grid -> 2-column grid -> horizontal scroll carousel
- Promo bar: full text -> truncated with ellipsis on narrow viewports

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Anti-bot wall**: The site returned a Cloudflare "Just a moment..." challenge page, blocking all meaningful CSS/JS extraction. Only one hex color (#313131) was captured from the static HTML.
- **Primary red (#DA291C)**: Inferred from Oster's widely-documented packaging, logo, and marketing materials spanning decades — not extracted from the live site. The actual web implementation may use a different shade.
- **Secondary navy (#2D3142)**: Estimated from common Oster retail-page patterns; not directly extracted.
- **Typography**: No custom web fonts were detected — only system font stacks were returned. Oster may load brand-specific typefaces via JavaScript bundles or font-loading APIs behind the anti-bot gate.
- **Component dimensions**: All padding, height, border, and shadow values are estimated from standard appliance-retail patterns; no live CSS was available for measurement.
- **Accent or sub-brand colors**: Oster may use additional colors for product-line differentiation (e.g., blender vs. toaster oven categories) or seasonal promotions that could not be captured.
- **Icon set and illustration style**: No icon font, SVG sprite, or illustration assets were extractable.
- **Motion and animation**: Transition timing, easing curves, and scroll-triggered animations are estimated defaults; no live animation data was captured.
- **Dark mode**: No evidence of a dark-mode theme; unable to confirm or deny support.
- **Focus ring styles**: Keyboard-navigation focus outlines are not documented; a 2px solid outline in `{colors.primary}` with 2px offset is recommended as a baseline.
- **Loading states**: Skeleton screens, shimmer patterns, and spinner styles are not defined.
