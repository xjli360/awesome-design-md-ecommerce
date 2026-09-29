---
version: alpha
name: "Epomaker"
source_url: "https://epomaker.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  That saturated teal (#108474) hitting you from every "Add to Cart" button and category badge signals a brand more comfortable in the mechanical-switch hobbyist world than in minimalist consumer electronics — it is bright enough to pop against the dark product photography of keycap sets and aluminum cases, yet muted enough to avoid clashing with the rainbow of keyboard colorways on display. Epomaker's type system leans on Poppins, a geometric sans-serif whose rounded terminals echo the pill-shaped keycaps the brand sells; headings land at weight 600–700 in modest sizes (24–32px display), trusting large product imagery and specification grids to do the heavy visual lifting rather than oversized typography. The layout defaults to a near-black ink (#181818) on a white canvas, with generous use of #f5f5f5 surface panels to separate product grids from editorial blocks, and a mint-tinted surface (#dff8ef) reserved for promotional banners and "in-stock" success states that reinforce the primary teal family. Corners stay relatively tight — `{rounded.sm}` on buttons and cards, `{rounded.xs}` on badges — conveying the precision-engineering ethos of the product line without descending into brutalist hard edges. A secondary electric blue (#0037c9) appears in hyperlinks and informational callouts, while a bold red (#da3f3f) marks sale pricing and low-stock warnings. Gold (#dec700) punctuates limited-edition releases and rating stars, adding a collector's-market energy. The component library is dense: spec-comparison tables, switch-type selectors with color swatches, group-buy countdown timers, and a sticky bottom bar on mobile PDPs all reflect a catalog that demands more UI surface than a typical lifestyle storefront. Navigation stacks product categories horizontally with dropdown mega-menus exposing keyboard size (60%, 65%, 75%, TKL, full) and switch-type filters — the information architecture of a hobbyist marketplace compressed into a Shopify theme.

colors:
  primary: "#108474"
  primary-active: "#0c6b5e"
  primary-disabled: "#a3d9cf"
  accent-blue: "#0037c9"
  accent-electric: "#001fff"
  accent-purple: "#5900ff"
  sale-red: "#da3f3f"
  highlight-gold: "#dec700"
  highlight-amber: "#ffbf00"
  surface-mint: "#dff8ef"
  ink: "#181818"
  ink-secondary: "#202223"
  body: "#484d5b"
  muted: "#7b7b7b"
  muted-soft: "#8b8b8b"
  hairline: "#d0d0d0"
  hairline-soft: "#ededed"
  border-strong: "#6d7175"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-strong: "#f0f0f0"
  surface-neutral: "#f9fafb"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#000000"
  dark-bg: "#222222"
  warm-dark: "#433808"

typography:
  display-xl:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-lg:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.2px
  display-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-lg:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  price-lg:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0
  price-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-strikethrough:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 1px solid {colors.hairline}
  button-secondary-active:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.ink}
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.primary}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline-soft}
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg} {spacing.xl}"
    boxShadow: 0 4px 16px rgba(0,0,0,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    imageRatio: 1:1
    hoverTransform: translateY(-2px)
    boxShadow: 0 2px 8px rgba(0,0,0,0.06)
  product-card-badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 52px
  countdown-timer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  countdown-digit:
    backgroundColor: "{colors.ink-secondary}"
    textColor: "{colors.highlight-gold}"
    typography: "{typography.display-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    labelTypography: "{typography.spec-label}"
    borderBottom: 1px solid {colors.hairline-soft}
  switch-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    border: 1px solid {colors.hairline}
    selectedBorder: 2px solid {colors.primary}
  color-swatch:
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
    border: 2px solid {colors.hairline}
    selectedBorder: 2px solid {colors.primary}
  price-block:
    currentPrice:
      textColor: "{colors.ink}"
      typography: "{typography.price-lg}"
    comparePrice:
      textColor: "{colors.muted}"
      typography: "{typography.price-strikethrough}"
      textDecoration: line-through
    saveBadge:
      textColor: "{colors.sale-red}"
      typography: "{typography.caption}"
  sticky-atc-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    height: 72px
    boxShadow: 0 -2px 8px rgba(0,0,0,0.08)
    borderTop: 1px solid {colors.hairline-soft}
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    boxShadow: 0 8px 32px rgba(0,0,0,0.12)
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    linkColor: "{colors.hairline-soft}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  promo-banner:
    backgroundColor: "{colors.surface-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  rating-stars:
    filledColor: "{colors.highlight-amber}"
    emptyColor: "{colors.hairline}"
    size: 14px
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: 1px solid {colors.hairline}
    activeBorder: 1px solid {colors.primary}

---

## Components

### Buttons

**`button-primary`** — Full-width on mobile PDPs, inline on desktop. The teal (#108474) background with white text at `{typography.button-lg}` weight 600 provides clear CTA hierarchy. On hover, darkens to `{colors.primary-active}` (#0c6b5e) with no scale transform. Disabled state washes to `{colors.primary-disabled}` with reduced opacity. Minimum touch target 48px.

**`button-secondary`** — White fill with a 1px `{colors.hairline}` border, used for "Buy Now" alternatives and secondary actions like "Add to Wishlist." On hover the border strengthens to `{colors.ink}` and the background tints to `{colors.surface-strong}`. Same 48px height as primary.

**`button-dark`** — Inverted variant with `{colors.ink}` background and white text, reserved for hero CTAs on light-background banners and the newsletter signup submit. Shares geometry with primary.

**`button-sm`** — Compact 32px-height variant used inside product cards for quick-add and inside filter pills. Uses `{typography.button-sm}` at 12px and tighter `{rounded.xs}` corners.

### Navigation

**`nav-bar`** — 64px fixed header with logo left, category links center (Poppins 500/14px), and icon cluster right (search, account, cart with count badge). A thin `{colors.hairline-soft}` bottom border separates it from content. On scroll, a subtle box-shadow replaces the border.

**`nav-mega-menu`** — Drops below category links on hover. Organized into columns by keyboard size (60%, 65%, 75%, TKL, Full-size) and accessory type (keycaps, switches, cables). Each column header uses `{typography.title-sm}`. Product thumbnails (40×40) appear next to featured items.

### Product Card

**`product-card`** — 1:1 image ratio with `{rounded.sm}` corners. Slight upward translate on hover with a soft 6% opacity shadow. Badge stack (top-left) can show "NEW" in teal, "SALE" in red, or "SOLD OUT" in gray. Below the image: product title in `{typography.title-sm}`, a one-line spec summary (switch type, connectivity) in `{typography.caption}`, price block, and 5-star rating row. Cards sit in a 4-column grid on desktop, 2-column on mobile.

### Hero Banner

**`hero-banner`** — Full-bleed dark (#222222) background with large product photography composited right. Left-aligned headline in `{typography.display-xl}` white, a supporting line in `{typography.body-lg}`, and a teal `hero-cta` button. Minimum height 480px desktop, 320px mobile. Swiper dots at bottom for carousel variants.

### Countdown Timer

**`countdown-timer`** — Used for group-buy and flash-sale deadlines. Dark background bar with individual `countdown-digit` cells displaying days/hours/minutes/seconds in gold `{colors.highlight-gold}` type against `{colors.ink-secondary}`. Positioned below the hero or inline on PDP above the ATC button.

### Spec Table

**`spec-table`** — Alternating-row layout on a `{colors.surface-soft}` background. Label column uses `{typography.spec-label}` (12px/600) and value column uses `{typography.body-md}`. Covers connectivity, battery, switch type, keycap material, dimensions, weight. Rounded container with `{rounded.sm}`.

### Switch & Color Selectors

**`switch-selector`** — Horizontal row of bordered rectangles, each containing a switch name and small color dot. Selected state gains a 2px `{colors.primary}` border. Used on PDP for choosing between Gateron, Budgerigar, or Sea Salt switches.

**`color-swatch`** — Circular 24px swatches for keyboard colorway selection. Selected swatch gains a primary-colored ring. Unselected has a light hairline border to be visible on white backgrounds.

### Pricing

**`price-block`** — Current price in `{typography.price-lg}` (bold 22px, ink). When on sale, the compare-at price sits to the right in `{typography.price-strikethrough}` with line-through and `{colors.muted}` color. A "Save X%" caption in `{colors.sale-red}` appears below on deep discounts.

### Sticky Add-to-Cart Bar

**`sticky-atc-bar`** — Appears on mobile when the main ATC button scrolls offscreen. 72px height, white background with top shadow. Contains a condensed product title, current price, and a full-width teal primary button. Slides up with a 200ms ease transition.

### Search

**`search-overlay`** — Modal overlay with `{rounded.md}` container, triggered from the nav search icon. Auto-suggest results grouped by "Products" and "Collections." Each result row shows a 48×48 thumbnail, title, and price. Input field uses `{typography.body-md}` with a teal focus ring.

### Footer

**`footer`** — Dark (#222222) background with four-column link grid (Shop, Support, Community, About) in `{typography.body-sm}`. Links lighten to near-white on hover. Bottom row contains payment icons, locale selector, and copyright line. Newsletter signup input with inline submit button spans the top of the footer section.

### Announcement Bar

**`announcement-bar`** — 36px teal bar pinned above the nav. White `{typography.caption}` text auto-rotates between shipping info, current sale, and new-release callouts. Closeable via an × icon at right.

### Promotional Banner

**`promo-banner`** — Mint-tinted `{colors.surface-mint}` inline banner with `{rounded.sm}`, used mid-page to highlight bundle deals or group-buy entry points. Left icon, body text, and a teal text-link CTA.

### Rating Stars

**`rating-stars`** — Amber-filled (#ffbf00) 14px stars with empty state in `{colors.hairline}`. Paired with review count in `{typography.caption}`. Appears on product cards and PDP below the title.

### Collection Filters

**`collection-filter`** — Sidebar on desktop, bottom-sheet on mobile. Filter groups (Size, Switch Type, Connectivity, Price Range) are collapsible accordions. Active filter chips gain a primary border. "Clear All" link in `{colors.accent-blue}`.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2-col for cards), hamburger menu replaces horizontal nav, sticky ATC bar appears on PDP, hero height reduces to 320px, mega-menu becomes full-screen slide-in panel, spec table stacks label/value vertically |
| Tablet | 744–1128px | 3-column product grid, horizontal nav visible but condensed, hero maintains side-by-side layout at reduced image scale, filters move to a collapsible top bar, footer collapses to 2-column |
| Desktop | 1128–1440px | 4-column product grid, full mega-menu dropdowns, sticky ATC bar hidden (main button always visible), hero at full 480px height, sidebar filters on collection pages |
| Wide | > 1440px | Content max-width 1440px centered, additional whitespace on flanks, product grid may expand to 5 columns on collection pages, hero imagery scales proportionally |

### Touch Targets

- All interactive elements maintain minimum 44×44px touch area on mobile
- Switch selector chips expand padding to 12px 16px on touch devices
- Color swatches grow to 32px diameter with 12px gap on mobile
- Mega-menu links gain 48px row height in mobile slide-in panel
- Close/dismiss icons use 44px hit area regardless of visual size

### Collapsing Strategy

- Navigation: horizontal links → hamburger icon + slide-in drawer at <744px
- Product grid: 4-col → 3-col → 2-col as viewport shrinks
- Hero: side-by-side (image + text) → stacked (image above text) at <744px
- Spec table: two-column row → stacked label-over-value at <744px
- Footer: four-column grid → two-column → single-column accordion at <744px
- Filters: persistent sidebar → collapsible top bar (tablet) → bottom sheet (mobile)
- Countdown timer: inline row → wraps to 2×2 digit grid on very narrow viewports

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font aliases `M-Body-Font` and `M-Heading-Font` could not be resolved to specific font files; Poppins is the only explicitly named family in the extracted stacks and is assumed to be the theme's heading and body font
- `JudgemeStar` is a review-widget icon font, not a brand typeface — excluded from the type system
- Exact font weights for heading vs. body aliases are inferred from common Shopify theme patterns, not directly extracted CSS custom properties
- No theme-color meta tag was found; the teal primary (#108474) is derived from color-frequency extraction rather than an explicit brand declaration
- Exact border-radius values on the live site could not be confirmed — the rounded scale uses standard increments that visually match observed screenshots
- Dark-mode or alternate colorway tokens were not detected; the brand may ship a single light theme only
- Exact spacing tokens are standardized estimates — the Shopify theme likely uses a 4px/8px base grid but specific custom properties were not extractable
- Motion/animation timing values (easing curves, durations) were not captured from the live site
- The warm-dark color (#433808) appears in limited contexts (possibly a limited-edition product badge or vintage-themed section) and its exact usage could not be confirmed
