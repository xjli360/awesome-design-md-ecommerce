---
version: alpha
name: "HP"
source_url: "https://www.hp.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The HP Simplified typeface — geometric, wide-set, engineered to feel like precision tooling rendered as letterforms — sets the entire tonal register of hp.com before a single product image loads. Display headings run at weight 300 (Light) where most technology brands would reach for 600+, trusting the typeface's inherent structural openness to provide visual mass without typographic aggression. The site's primary voltage is #165dba, a medium-saturation corporate blue that functions less as decoration and more as a wayfinding rail: every primary CTA, active navigation indicator, and configuration selector pulses this hue, while a darker #114a94 variant anchors pressed states and footer link hovers. What distinguishes HP's digital palette from a generic tech-blue system is the breadth of its accent spectrum — #7d3894 purple codes OMEN gaming hardware, #debc33 gold signals the Spectre premium line, #009d69 green marks sustainability initiatives, and #fd0032 red drives sale badges and urgency states. These accents never collide; they occupy distinct product swim-lanes against a predominantly monochromatic stage of #2c3038 ink, #5a5a5a body copy, and #e8e8e8 structural dividers on a #f5f5f5 canvas. Product cards use `{rounded.sm}` corners and buttons hold `{rounded.xs}` — deliberately restrained radii that reinforce the precision-engineering positioning over the friendly pill shapes favored by consumer lifestyle brands. Navigation stacks two tiers: a slim utility bar in `{typography.nav-utility}` carrying support and account links above a 56px primary bar with mega-menu dropdowns that reveal editorial imagery alongside category links. The hero carousel occupies full viewport width, cycling through product launches with a single `button-primary` CTA centered over full-bleed photography. Footer inverts the page's light canvas to a #2c3038 dark ground, running a dense four-column layout that creates a definitive visual terminus. The overall rhythm is spacious, systematic, and optimized for comparison shopping across hundreds of SKUs — every element sized and spaced to move a buyer from category to configuration to cart.

colors:
  primary: "#165dba"
  primary-active: "#114a94"
  primary-disabled: "#ccdef5"
  ink: "#231f20"
  body: "#2c3038"
  muted: "#5a5a5a"
  muted-soft: "#767676"
  hairline: "#c7c7c7"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-blue: "#cceaf7"
  surface-blue-light: "#99d5ee"
  surface-lavender: "#f7f2f9"
  surface-yellow: "#f8fab8"
  surface-mint: "#c3ffde"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-purple: "#7d3894"
  accent-purple-deep: "#4b4096"
  accent-gold: "#debc33"
  accent-gold-bright: "#ffd24d"
  accent-gold-dark: "#bd8c28"
  accent-red: "#fd0032"
  accent-red-dark: "#d6002a"
  accent-red-deep: "#8c031c"
  accent-orange: "#d64000"
  accent-green: "#009d69"
  accent-green-bright: "#00b04f"
  accent-pink: "#ffbdc9"
  link: "#187ee6"
  footer-bg: "#2c3038"
  footer-ink: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'HPSimplifiedLight', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'HPSimplifiedLight', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-lg:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 0
  nav-link:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 0
  nav-utility:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  price:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  price-strike:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: line-through
  spec-label:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  badge:
    fontFamily: "'HPSimplifiedRegular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.17
    letterSpacing: 0.2px
  icon:
    fontFamily: "'HPIcons'"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: 1px solid {colors.primary}
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 44px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  nav-utility-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-utility}"
    height: 36px
    padding: 0 {spacing.xl}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: 0 {spacing.xl}
    borderBottom: 1px solid {colors.hairline-soft}
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.xxl}"
    boxShadow: 0 4px 16px rgba(0,0,0,0.1)
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: 1px solid {colors.hairline}
    padding: 0 12px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
    hoverBorder: 1px solid {colors.primary}
    hoverShadow: 0 2px 8px rgba(0,0,0,0.08)
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    titleTypography: "{typography.display-xl}"
    ctaComponent: button-primary
  category-badge:
    backgroundColor: "{colors.surface-blue}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  omen-badge:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  spectre-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  price-cluster:
    currentPriceTypography: "{typography.price}"
    currentPriceColor: "{colors.ink}"
    strikePriceTypography: "{typography.price-strike}"
    strikePriceColor: "{colors.muted}"
    savingsColor: "{colors.accent-red}"
    savingsTypography: "{typography.body-sm}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    headerTypography: "{typography.title-sm}"
    rowBorder: 1px solid {colors.hairline-soft}
    padding: "{spacing.md} {spacing.base}"
  configurator-option:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    border: 1px solid {colors.hairline}
    selectedBorder: 2px solid {colors.primary}
    selectedBackgroundColor: "{colors.surface-blue}"
  compare-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: 72px
    boxShadow: 0 -2px 8px rgba(0,0,0,0.1)
    padding: "{spacing.md} {spacing.xl}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.surface-blue-light}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 40px
    padding: 0 {spacing.base}
---

## Components

### Buttons

**`button-primary`** — Solid #165dba rectangle with `{rounded.xs}` corners and white label text in `{typography.button-md}`. On hover the background darkens toward `{colors.primary-active}`; on press it deepens further with a subtle 1px inset shadow. Disabled state uses `{colors.primary-disabled}` — a pale blue wash that reduces contrast against white text to signal inactivity. Height stays at 44px across all breakpoints.

**`button-secondary`** — White fill with a 1px `{colors.primary}` border and blue label text. On hover the interior fills to `{colors.surface-blue}` while the border remains. Often paired alongside `button-primary` in product detail CTAs — "Add to Cart" primary, "Save for Later" secondary. Active state darkens the border to `{colors.primary-active}`.

**`button-ghost`** — Transparent background with `{colors.primary}` text, no border. Used for tertiary actions like "View all" links, breadcrumb-adjacent prompts, and inline "Learn more" triggers. Hover state adds an underline rather than a background fill.

### Navigation

**`nav-utility-bar`** — A 36px-tall strip at the very top on `{colors.surface-soft}` gray, containing support links, order status, country/language selector, and sign-in in `{typography.nav-utility}` at `{colors.muted}`. Links darken to `{colors.ink}` on hover. This bar collapses entirely on mobile viewports.

**`nav-bar`** — The primary navigation directly below the utility bar at 56px height on white canvas. The HP logo (blue wordmark) anchors left; top-level categories (Laptops, Desktops, Printers, Ink & Toner, Accessories, Support) sit center in `{typography.nav-link}`. A search icon and cart icon occupy the right edge. On mobile, the bar compresses to logo + hamburger + cart icon.

**`mega-menu`** — A full-width dropdown that opens on category hover, presenting subcategories in a multi-column grid alongside a featured product image or promotional banner. Text runs in `{typography.body-sm}` with category headers in `{typography.title-sm}`. A subtle box shadow separates the panel from the page below. Closes on mouse-leave with a brief delay to prevent accidental dismissal.

### Product Display

**`product-card`** — Vertical card with a large product image (roughly 4:3 aspect ratio) above a text block containing a category badge, product name in `{typography.title-md}`, a one-line spec summary in `{typography.body-sm}`, and the `price-cluster` at bottom. Uses `{rounded.sm}` corners and a `{colors.hairline-soft}` border that transitions to `{colors.primary}` on hover with a light shadow lift. Cards sit in a 3-up grid on desktop, 2-up on tablet, single column on mobile.

**`price-cluster`** — Grouped price display: current price in `{typography.price}` at `{colors.ink}`, struck-through original in `{typography.price-strike}` at `{colors.muted}`, and savings amount in `{colors.accent-red}` using `{typography.body-sm}`. When no discount applies, only the current price renders. Tax-inclusive pricing note appears below in `{typography.caption}`.

**`category-badge`** — A compact label reading "Laptop", "Desktop", or "Printer" on `{colors.surface-blue}` background with `{colors.primary}` text. Sits above the product name on cards. Product-line variants use distinct accent backgrounds: `omen-badge` (purple) for gaming, `spectre-badge` (gold) for premium.

**`sale-badge`** — A compact `{colors.accent-red}` rectangle with white text announcing "SALE" or a percentage off. Positioned at the top-right of the product card image area. Uses `{typography.badge}` at `{rounded.xs}`.

### Product Configuration

**`configurator-option`** — A selectable tile representing a configuration choice (processor, RAM, storage, display). Shows option name and price delta in `{typography.body-sm}` inside a `{rounded.xs}` bordered container. Selected state receives a 2px `{colors.primary}` border and `{colors.surface-blue}` background fill. Unselected tiles use a 1px `{colors.hairline}` border on white.

**`spec-table`** — Alternating-row specification table on product detail pages. Header row uses `{colors.surface-soft}` background with `{typography.title-sm}` labels. Data rows use `{typography.spec-label}` with 1px `{colors.hairline-soft}` bottom borders. Generous `{spacing.md}` vertical padding keeps dense specification data scannable across 30–40 rows.

### Promotional

**`hero-banner`** — A full-bleed section (minimum 480px tall) anchoring the homepage and category landings. Features full-width product photography or lifestyle imagery with a text overlay containing a `{typography.display-xl}` headline, a subhead in `{typography.body-md}`, and a `button-primary` CTA. Overlay is left-aligned on desktop, centered on mobile. Background may use `{colors.surface-soft}` or a dark product shot with white text.

**`promo-banner`** — A narrow 40px strip pinned above the utility bar, running a single promotional message (free shipping threshold, seasonal sale) in `{typography.body-sm}` white text on `{colors.primary}` blue background. Includes a dismiss icon at the far right.

### Utility

**`compare-bar`** — A sticky bottom bar appearing when products are selected for comparison. Shows up to four product thumbnails with names in `{typography.body-sm}`, a "Compare" `button-primary`, and a clear-all link. Elevated above page content with an upward box shadow. On mobile, collapses to a floating action button with a badge count.

**`search-bar`** — A 44px input field with `{rounded.xs}` corners, a 1px `{colors.hairline}` border, and a magnifying-glass icon at the left edge. On focus, the border shifts to `{colors.primary}`. A dropdown suggestion panel appears below on keystroke, listing recent searches and suggested products with thumbnail images.

**`footer`** — Dense four-column layout on `{colors.footer-bg}` (#2c3038) dark ground. Columns contain product links, support links, partner programs, and company info in `{typography.body-sm}` white text. A secondary row below holds legal disclaimers, privacy links, and country/language selector. Social icons run as a horizontal row above the legal strip.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, nav collapses to hamburger + logo + cart, hero text centers and stacks above image, utility bar hidden, mega-menu becomes full-screen slide-over, footer stacks to single column with accordion sections |
| Tablet | 744–1128px | 2-column product grid, nav shows abbreviated top categories with overflow in hamburger, hero banner maintains side-by-side at reduced image scale, footer collapses to 2 columns |
| Desktop | 1128–1440px | 3-column product grid, full horizontal nav with mega-menu dropdowns, hero banner at full expression with left-aligned text overlay, 4-column footer, compare bar shows full product thumbnails |
| Wide | > 1440px | Content max-width caps at 1440px and centers, side gutters grow symmetrically, product grid may expand to 4 columns on category pages, hero image scales to fill extra width |

### Touch Targets
- All interactive buttons maintain minimum 44px touch height on mobile
- Nav hamburger icon uses a 48px tap zone
- Product card is fully tappable on mobile, not just the title text
- Configurator option tiles maintain at least 44px height on all breakpoints
- Footer accordion headers use 48px tap zones on mobile

### Collapsing Strategy
- Navigation: two-tier bar collapses to single sticky bar with hamburger; mega-menu becomes full-screen slide-over drawer
- Product grid: 4 → 3 → 2 → 1 columns as viewport shrinks
- Spec tables: switch to stacked key-value pairs below 744px
- Hero banner: side-by-side layout (text | image) becomes stacked (image above, text below)
- Footer: 4-column grid → 2-column → single-column accordion
- Compare bar: sticky bottom bar becomes a floating action button with badge count on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- HP Simplified (Light and Regular) are proprietary fonts served from HP's CDN and not publicly licensable — implementations must obtain a license or fall back to Helvetica Neue / Arial
- HPIcons icon font glyph mappings were not extracted; implementations need the actual font file or should substitute a comparable icon library (e.g., Lucide, Phosphor)
- Exact transition durations and easing curves for hover states, mega-menu open/close, and hero carousel animation were not captured from the live site
- The extracted source is HP's Japanese site (hp.com/jp); type sizing, spacing, and content density may differ from the English-language global storefront
- Form validation states (error, success, warning) beyond focus-blue border were not observed in the color extraction
- Dark-mode or high-contrast accessibility variants were not detected in the extraction
- Exact box-shadow values on hover cards and mega-menu are approximated from visual observation, not from computed style extraction
- The precise mapping of which accent color applies to each product sub-brand beyond OMEN (purple) and Spectre (gold) could not be fully confirmed
