---
version: alpha
name: "Knix"
source_url: "https://knix.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Strip away every accent color from a lingerie site and what remains is a bet — that the human body itself is the only pigment the interface needs. Knix commits to this wager fully, running an almost colorless palette of near-blacks (#141414, #121212), mid-grays (#545454), and whisper-light surfaces (#f6f6f6, #e2e2e2, #dedede) that recede behind full-bleed campaign photography of unretouched torsos, stretch marks, and post-surgical scars. The typography is Inter — clean, geometric, emotionally neutral — loaded at weights 400 through 700 without display fireworks, because the editorial voice here is the copy itself ("Wear what moves you," "Designed for every body") rather than the letterforms carrying it. Buttons are solid rectangles of #141414 with `{rounded.sm}` corners and white text, giving CTAs the density of a rubber stamp pressed onto paper; there is no gradient, no shadow, no color-coded hierarchy — just ink-on-canvas confidence. Product cards sit on `{colors.surface-card}` with `{rounded.md}` softness, each one a quiet frame for the product image that dominates its area. The announcement bar runs full-width in `{colors.announcement-bg}` (#141414) with `{typography.announcement}` text in white, cycling through promotions with the cadence of a departures board. Category navigation uses oversized lifestyle imagery rather than icon glyphs, turning the mega-menu into a mood board. Size-inclusive quiz flows, prominent "Find Your Fit" CTAs, and trust badges ("Leak-proof," "Wire-free," "60-day trial") appear as first-class UI components rather than afterthoughts, reflecting a brand where conversion and body confidence are the same goal. Spacing is generous — `{spacing.section}` (64px) between content blocks, `{spacing.lg}` (24px) gutters — creating the breathing room of a magazine editorial spread rather than a cluttered marketplace. The overall sensation is of a dressing room with excellent lighting: minimal, warm, and designed to make you look at yourself rather than the furniture.

colors:
  primary: "#141414"
  primary-active: "#000000"
  primary-disabled: "#a0a0a0"
  ink: "#121212"
  body: "#545454"
  muted: "#757575"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-warm: "#faf9f7"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  announcement-bg: "#141414"
  announcement-text: "#ffffff"
  error: "#d32f2f"
  error-soft: "#fce4e4"
  success: "#2e7d32"
  success-soft: "#e8f5e9"
  badge-bestseller: "#141414"
  badge-new: "#545454"
  badge-sale: "#d32f2f"
  star-rating: "#141414"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Inter', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Inter', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  announcement:
    fontFamily: "'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.3px
  button-lg:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0
  link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  micro-label:
    fontFamily: "'Inter', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-compare:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
    textDecoration: line-through
  quiz-heading:
    fontFamily: "'Inter', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px

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
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 52px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 52px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 52px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 52px
    border: 1.5px solid "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 52px
    border: 1.5px solid "{colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
    textDecoration: underline
  button-add-to-bag:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 56px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    border: 1.5px solid "{colors.primary}"
  text-input-error:
    border: 1.5px solid "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.announcement-bg}"
    textColor: "{colors.announcement-text}"
    typography: "{typography.announcement}"
    height: 40px
    padding: 0 "{spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: 3 / 4
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    padding: "0 {spacing.base} {spacing.xs}"
  product-card-price-compare:
    typography: "{typography.price-compare}"
    textColor: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.badge-bestseller}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-swatch-row:
    padding: "0 {spacing.base} {spacing.md}"
    gap: "{spacing.xs}"
  color-swatch:
    width: 16px
    height: 16px
    rounded: "{rounded.full}"
    border: 1px solid "{colors.hairline}"
  color-swatch-active:
    border: 2px solid "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 0
    minHeight: 560px
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    overflow: hidden
    aspectRatio: 4 / 5
  category-tile-label:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.md}"
  size-quiz-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.quiz-heading}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl} {spacing.lg}"
  size-quiz-option:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 14px 20px
    border: 1.5px solid "{colors.hairline}"
  size-quiz-option-selected:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 14px 20px
    border: 1.5px solid "{colors.primary}"
  trust-badge:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    iconSize: 24px
    gap: "{spacing.sm}"
  trust-badge-bar:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.lg} {spacing.base}"
    gap: "{spacing.xl}"
  star-rating:
    color: "{colors.star-rating}"
    size: 14px
    gap: 2px
  star-rating-count:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  reviews-summary:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  review-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    borderBottom: 1px solid "{colors.hairline-soft}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px 12px 40px
    height: 48px
    border: none
  search-input-focus:
    border: 1.5px solid "{colors.primary}"
  search-suggestion:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} {spacing.base}"
  quick-add-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg} {rounded.lg} 0 0"
    padding: "{spacing.lg}"
  quick-add-drawer-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
    minWidth: 48px
  size-selector-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: 1px solid "{colors.primary}"
  size-selector-disabled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    border: 1px solid "{colors.hairline-soft}"
    textDecoration: line-through
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
    borderTop: 1px solid "{colors.hairline-soft}"
  mega-menu-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "0 0 {spacing.md}"
  mega-menu-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.xs} 0"
  mega-menu-link-hover:
    textColor: "{colors.primary}"
  mega-menu-image:
    rounded: "{rounded.md}"
    aspectRatio: 3 / 4
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "0 0 {spacing.md}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-bottom:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    borderTop: 1px solid "{colors.hairline}"
    padding: "{spacing.lg} 0 0"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: 1px solid "{colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0 {spacing.base}"
  press-logo-bar:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.xxl} {spacing.lg}"
    gap: "{spacing.xxl}"
  press-logo:
    height: 24px
    opacity: 0.5
  press-logo-hover:
    opacity: 1

## Components

### Buttons
**`button-primary`** — A solid #141414 rectangle with `{rounded.sm}` (8px) corners and white text set in `{typography.button-lg}` — 16px semibold Inter. The button stands 52px tall with generous 32px horizontal padding, giving it the proportions of a stamp pressed cleanly onto the page. On hover, the background deepens to `{colors.primary-active}` (#000000). The disabled state drops to `{colors.primary-disabled}` (#a0a0a0), maintaining shape and typography while draining the density. No shadows, no gradients — the button's authority comes entirely from its contrast against the white canvas.

**`button-secondary`** — An outlined counterpart using a 1.5px solid border in `{colors.primary}` on a white fill, matching the primary button's 52px height and `{rounded.sm}` corners. Text is `{colors.primary}` in `{typography.button-lg}`. On hover, the fill shifts to `{colors.surface-soft}` (#f6f6f6) and the border darkens. Used for secondary actions like "View Details" or "Shop Now" when paired alongside a primary CTA.

**`button-tertiary`** — A stripped-back text link with no container or background. Set in `{typography.button-md}` (14px semibold) with an underline decoration in `{colors.primary}`, it serves as the quietest call-to-action in the system. Used for "Learn More," "See All Reviews," and inline navigational prompts within content blocks.

**`button-add-to-bag`** — A full-width variant of the primary button at 56px height, used exclusively on the product detail page. Its increased vertical padding and 100% width give it the visual weight of a commitment — the final action in the shopping flow before the cart drawer opens.

### Text Inputs
**`text-input`** — A 48px-tall field with `{rounded.sm}` corners and a 1px border in `{colors.hairline}` (#dedede). Text renders in `{typography.body-md}` (16px regular Inter), with placeholder text in `{colors.muted-soft}` (#999999). On focus, the border thickens to 1.5px and shifts to `{colors.primary}` (#141414), creating a firm visual anchor without color theatrics. Error states use `{colors.error}` (#d32f2f) for the border, paired with an error message in `{typography.caption}` below the field.

### Navigation
**`nav-bar`** — A 64px-tall white bar with a subtle 1px bottom border in `{colors.hairline-soft}` (#e2e2e2). The logo sits left-aligned, with navigation links in `{typography.nav-link}` (14px medium-weight Inter) centered or left-adjacent. Right side holds icon buttons for search, account, and cart. On scroll, the bar gains a sticky position and the border may strengthen to `{colors.hairline}`. The bar is always preceded by the announcement bar on initial page load.

**`announcement-bar`** — A 40px strip in `{colors.announcement-bg}` (#141414) spanning full width, with rotating promotional messages in `{typography.announcement}` (13px medium, white, 0.3px letter-spacing). Supports left/right navigation arrows for cycling through messages. Closes on scroll or via a dismiss button.

**`mega-menu`** — Triggered on hover over nav links, the mega-menu drops below the nav-bar with a 1px top border. It contains column headings in `{typography.title-sm}`, link lists in `{typography.body-sm}`, and large lifestyle images in `{rounded.md}` frames. The image columns double as category navigation, making the menu feel more like a mood board than a sitemap.

### Product Cards
**`product-card`** — A white card with `{rounded.md}` (12px) corners, holding a 3:4 aspect-ratio product image that rounds at the top. Below the image, the product title appears in `{typography.title-sm}` (16px semibold) with `{spacing.md}` top and `{spacing.base}` side padding. Price follows in `{typography.price}` (16px semibold), with an optional struck-through compare price in `{typography.price-compare}` using `{colors.muted}`. A color swatch row of 16px circles with `{rounded.full}` sits at the bottom. An optional badge ("Bestseller," "New") in `{typography.badge}` floats absolute in the top-left corner over the image, using `{colors.badge-bestseller}` with white text and `{rounded.xs}` corners.

### Hero Banner
**`hero-banner`** — A full-bleed section anchored by lifestyle photography at a minimum height of 560px. Text overlays sit on the image with `{typography.display-xl}` (48px bold, -1px tracking) for the headline and `{typography.body-md}` for the subheadline. A `hero-cta` button provides the primary action. The entire composition relies on the photograph for emotional weight — there is no background color treatment beyond `{colors.surface-warm}` (#faf9f7) as a fallback when the image hasn't loaded.

### Category Tiles
**`category-tile`** — A 4:5 aspect-ratio card with `{rounded.md}` corners and hidden overflow, containing a full-bleed lifestyle image with a text label overlay at the bottom. The label uses `{typography.title-sm}` in `{colors.ink}` on a semi-transparent white gradient. These tiles form a scrollable horizontal row on mobile and a multi-column grid on desktop, serving as the primary entry point to product categories.

### Size Quiz
**`size-quiz-card`** — A `{rounded.lg}` (20px) card on `{colors.surface-soft}` housing the multi-step fit quiz. Headings use `{typography.quiz-heading}` (24px bold). Quiz options are individual `size-quiz-option` tiles — white rectangles with `{rounded.sm}` corners and a 1.5px border in `{colors.hairline}` that switches to `{colors.primary}` on selection. The quiz is a signature conversion tool, prominently linked from the nav and product detail pages.

### Trust Badges
**`trust-badge-bar`** — A horizontal strip on `{colors.surface-soft}` displaying 3–5 trust icons (Leak-proof, Wire-free, 60-Day Trial, Free Shipping) with `{typography.caption}` labels. Each badge is a 24px icon paired with descriptive text in `{colors.body}`, spaced at `{spacing.xl}` apart. This bar typically appears below the hero section and above the product grid, reinforcing the brand's functional promises.

### Size Selector
**`size-selector`** — A row of rectangular tap targets (`{rounded.sm}`, 44px tall, minimum 48px wide) used on the product detail page for size selection. Default state has a 1px border in `{colors.hairline}` with `{typography.button-md}` text. The active/selected state inverts to `{colors.primary}` background with white text. Disabled (out-of-stock) sizes use `{colors.muted-soft}` text with a line-through decoration and a faint `{colors.hairline-soft}` border.

### Search
**`search-overlay`** — A full-width overlay that slides down from the nav bar, dimming the page behind a `{colors.scrim}` layer. The search input sits on `{colors.surface-soft}` with no border by default (a 1.5px `{colors.primary}` border appears on focus), and includes a search icon inset at the left. Suggestions appear below in `{typography.body-sm}`, with recent searches and trending queries listed vertically.

### Quick-Add Drawer
**`quick-add-drawer`** — A bottom sheet on mobile (top-rounded at `{rounded.lg}`) or a slide-in panel on desktop, used for quick size/color selection from the product grid without navigating to the PDP. Contains the product image, title in `{typography.title-md}`, size selector row, and a full-width `button-add-to-bag`. Padded at `{spacing.lg}` on all sides.

### Reviews
**`review-card`** — A stacked card with a bottom border in `{colors.hairline-soft}`, containing a star rating row, reviewer name in `{typography.caption}`, date, and review body in `{typography.body-sm}`. The reviews summary block uses `{typography.display-md}` for the aggregate score alongside a star row.

### Footer
**`footer`** — A full-width section on `{colors.surface-soft}` (#f6f6f6) with `{spacing.section}` vertical padding. Contains 4 columns on desktop: Shop, Help, About, and a newsletter signup. Column headings use `{typography.title-sm}` in `{colors.ink}`, with links in `{typography.link}` at `{colors.muted}` that darken to `{colors.primary}` on hover. A bottom row separated by a 1px `{colors.hairline}` border displays copyright, legal links, and payment icons in `{typography.caption}`.

### Accordion
**`accordion`** — Used on the PDP for product details, materials, and care instructions. Each panel has a title in `{typography.title-sm}` with a chevron icon, separated by 1px `{colors.hairline-soft}` borders. Expanded content renders in `{typography.body-sm}` at `{colors.body}`. The first panel is typically open by default; others collapse. Touch targets span the full row width.

### Press Logo Bar
**`press-logo-bar`** — A horizontal row of grayscale media logos (Vogue, Cosmopolitan, Forbes, etc.) displayed at 50% opacity and 24px height on a white background. On hover, individual logos fade to full opacity. The bar is padded at `{spacing.xxl}` and typically appears in the lower third of the homepage as social proof.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger + logo + cart icon; hero banner switches to stacked layout with text below image; mega-menu becomes a full-screen slide-out drawer; category tiles become a horizontal scroll strip; size quiz becomes full-screen modal; trust badge bar stacks into 2x2 grid; footer columns collapse to accordion; quick-add becomes bottom sheet; announcement bar text reduces to single line |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows top-level links with hamburger for overflow; hero banner maintains side-by-side at reduced height; mega-menu shows fewer image columns; category tiles in 2x2 grid; footer in 2-column layout; search overlay maintains full width |
| Desktop | 1128–1440px | Four-column product grid; full nav-bar with all links and mega-menu on hover; hero banner at full bleed with generous padding; trust badges in single horizontal row; footer in 4 columns; quick-add becomes side drawer; size quiz renders inline within page flow |
| Wide | > 1440px | Content max-width of 1440px centered; product grid may expand to 5 columns for collection pages; hero banner maintains maximum aspect ratio; all other components inherit desktop behavior within the centered container |

### Touch Targets
- All buttons maintain minimum 44x44px touch area on mobile and tablet
- Size selector tiles are 44px tall with 48px minimum width for comfortable tapping
- Nav-bar icon buttons (search, cart, account, hamburger) are 44x44px
- Product cards are full-card tap targets on mobile
- Accordion headers are 48px minimum height
- Color swatches use 32px tap targets (16px swatch + 8px padding per side)
- Quick-add drawer close button is 44x44px

### Collapsing Strategy
- Primary navigation collapses to hamburger at 744px; mega-menu becomes a full-screen drawer
- Product grid reduces from 4 columns to 2 at 744px, then to 1 below 480px
- Hero banner switches from side-by-side to vertical stack at 744px
- Footer columns collapse from 4 to 2 at 744px, then to stacked accordion below 480px
- Trust badge bar switches from horizontal row to 2x2 grid at 744px
- Category tiles switch from grid to horizontal scroll at 744px
- Size quiz transitions from inline to full-screen modal at 744px
- Search overlay remains full-width at all breakpoints
- Press logo bar scrolls horizontally on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No accent or CTA color was extracted from the live site — the palette is entirely neutrals (#141414, #121212, #545454, #dedede, #e2e2e2, #f6f6f6). Knix may use a warm or brand-specific accent loaded via JavaScript or applied conditionally; this could not be verified from static extraction
- Only one font family (Inter) was detected; the brand may load additional display or serif faces via JavaScript or font-loading APIs that were not captured
- Exact button heights, padding values, and border-radius values are inferred from visual patterns rather than extracted CSS tokens
- Animation and transition timing (drawer slides, accordion expand, hover fades) could not be extracted
- The fit quiz flow's full multi-step UI, progress indicators, and result screens are behind interactive state and could not be fully documented
- Cart drawer / mini-cart component specifications are not captured — likely a slide-in panel similar to the quick-add drawer
- Dark mode or seasonal palette variations are not present in the extracted data
- Focus ring styles for keyboard accessibility are not documented; a 2px solid outline in `{colors.primary}` with 2px offset is recommended as a safe default
- Loading states (skeleton screens, lazy-load image placeholders) are not defined
- Promotional banner and sale event color treatments may deviate from the standard palette
- Video player component used in hero sections and PDP galleries is not specified
- The exact z-index stacking for overlays (mega-menu, search, quick-add drawer, scrim) could not be determined
