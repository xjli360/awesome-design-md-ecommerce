---
version: alpha
name: "Nature Hills"
source_url: "https://www.naturehills.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep nursery teal (#108474) saturates every primary call-to-action on a nearly-white canvas, a color choice that reads more botanical garden signage than typical e-commerce green — and that distinction matters. Nature Hills pairs this anchor with a supporting leaf-lime (#8abb54) for category badges and secondary highlights, then punctuates seasonal promotions with a warm marigold (#ffdb27) that catches the eye without competing against the dominant green family. Typography runs a two-font system — Figtree for body copy and navigational text where its open counters aid scanability across long plant descriptions, and Barlow for display headings and button labels where its slightly condensed proportions let "Japanese Maple 'Bloodgood'" fit a product card title without wrapping. Corners land at a moderate `{rounded.sm}` (8px) on cards and inputs, stepping down to `{rounded.xs}` on tight UI like availability badges and up to `{rounded.full}` on pill-shaped filter chips and "Add to Cart" buttons — a deliberate split that separates browsing containers from action triggers. The grid breathes generously: product cards sit in a 3-up or 4-up layout with `{spacing.lg}` gutters, hero banners claim the full viewport with overlay text knocked out in white, and category navigation tiles stack lush photography behind semi-transparent dark scrims. Earthy accent browns (#8c564b) surface in zone-hardiness badges and seasonal icons, while a dark forest green (#5f8c32) reinforces trust in footer links and guarantee callouts. Error and alert states lean on a muted brick red (#b71c1c) rather than a synthetic scarlet, keeping even validation messages within a naturalistic register. The overall effect is a digital greenhouse catalog — dense with living-product imagery yet navigable, where the design system's job is to frame each plant photograph rather than compete with it.

colors:
  primary: "#108474"
  primary-active: "#1e7e34"
  primary-disabled: "#c5f7f0"
  secondary: "#8abb54"
  secondary-dark: "#5f8c32"
  secondary-darker: "#5a8a2e"
  accent-gold: "#ffdb27"
  accent-amber: "#ed9b20"
  accent-brown: "#8c564b"
  accent-purple: "#413389"
  error: "#b71c1c"
  ink: "#222222"
  body: "#3d3d3d"
  muted: "#7b7b7b"
  hairline: "#dedede"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  surface-warm: "#f3fde8"
  surface-teal: "#edf5f5"
  surface-neutral: "#f5f5f5"
  surface-muted: "#eeeeee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  button-lg:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.15px
  nav-link:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    border: 2px solid {colors.primary-active}
  button-add-to-cart:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-add-to-cart-active:
    backgroundColor: "{colors.secondary-dark}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-gold-promo:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 2px solid {colors.primary}
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 2px solid {colors.error}
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 48px 12px 20px
    height: 48px
    border: 2px solid {colors.hairline-soft}
    focusBorder: 2px solid {colors.primary}
  search-icon-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline-soft}
  nav-category-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: 1px solid {colors.hairline-soft}
    shadow: 0 2px 8px rgba(0,0,0,0.06)
  product-card-hover:
    shadow: 0 4px 16px rgba(0,0,0,0.10)
    border: 1px solid {colors.primary}
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: 1 / 1
    objectFit: cover
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    overlay: linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35))
  hero-subtitle:
    typography: "{typography.body-lg}"
    textColor: "{colors.on-dark}"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    shadow: 0 2px 6px rgba(0,0,0,0.08)
  zone-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.secondary-darker}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sale-badge:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  bestseller-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: 1px solid {colors.hairline}
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  breadcrumb:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  trust-bar:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.secondary-darker}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: 1px solid {colors.hairline}

---

## Components

### Buttons

**`button-primary`** — The default conversion button rendered in deep teal (#108474) with white text and a fully pill-shaped radius (`{rounded.full}`). On hover, background darkens to `{colors.primary-active}` (#1e7e34). Disabled state swaps to the pale mint `{colors.primary-disabled}` with muted text, signaling unavailability while preserving layout stability.

**`button-secondary`** — White fill with a 2px teal border and teal text. Used for "Learn More", "View Details", and secondary actions that should not compete with the primary CTA. On hover the background tints to `{colors.surface-teal}` and the border deepens to `{colors.primary-active}`.

**`button-add-to-cart`** — The highest-priority commerce button in leaf-lime (#8abb54), intentionally differentiated from the navigational teal so that "Add to Cart" pops against product cards even when adjacent to other teal UI. Slightly taller at 52px to increase tap target on mobile PDP layouts. Active state darkens to `{colors.secondary-dark}`.

**`button-gold-promo`** — Seasonal and promotional CTA in bright marigold (#ffdb27) with dark ink text. Used sparingly in hero banners and promotional strips to create urgency without relying on red. Smaller scale (40px height) keeps it subordinate to primary commerce buttons.

### Inputs

**`text-input`** — Standard form input with 1px hairline border on `{rounded.sm}`. On focus, border swaps to 2px solid teal, providing clear active-state feedback. Error state uses `{colors.error}` border. Placeholder text renders in `{colors.muted}`.

**`search-bar`** — Full-width pill-shaped search with an integrated circular teal search button (`search-icon-button`) inset on the right. The generous horizontal padding (20px left, 48px right for icon clearance) keeps typed queries from colliding with the icon. Focus state elevates the border to solid teal.

### Navigation

**`nav-bar`** — Sticky top navigation at 72px height on white canvas. Logo sits left, search bar centers, and cart/account icons cluster right. A 1px bottom hairline separates it from page content. On scroll, a subtle box-shadow appears (0 2px 8px rgba(0,0,0,0.06)) to indicate elevation.

**`nav-category-bar`** — Secondary navigation row beneath the main nav, listing top-level plant categories (Trees, Shrubs, Perennials, Fruit, Roses, Vines). Rendered on `{colors.surface-soft}` at 48px height. Active category receives a 2px bottom border in `{colors.primary}`.

### Product Cards

**`product-card`** — Vertical card with square plant photography at top, title, botanical name in muted caption, zone badge, and price. Card sits on white surface with a subtle hairline border and soft shadow. On hover, shadow deepens and border tints to teal, inviting click-through. Price renders in `{colors.primary}` using `{typography.price-sm}` to emphasize value.

### Badges

**`zone-badge`** — Hardiness zone indicator (e.g., "Zones 4-8") on a light green surface (`{colors.surface-warm}`) with dark green text. Uses uppercase badge typography at 11px. Appears on product cards and PDP sidebar.

**`sale-badge`** — Red (#b71c1c) background with white uppercase text. Positioned absolutely at the top-left corner of product card images. Communicates clearance or percentage-off pricing.

**`new-badge`** — Marigold background with dark ink text. Signals recently added cultivars or seasonal arrivals.

**`bestseller-badge`** — Teal background with white text. Applied to high-velocity SKUs to provide social proof within category grids.

### Hero & Promotional

**`hero-banner`** — Full-bleed image section with dark overlay gradient and white display text. Minimum height 480px ensures visual impact even with short headlines. CTA button (typically `button-primary` or `button-gold-promo`) sits below the subtitle with `{spacing.lg}` gap.

**`trust-bar`** — Thin horizontal strip in light green (`{colors.surface-warm}`) communicating shipping guarantees, expert support, or seasonal offers. Renders above or below the hero. Icon + short text pattern at `{typography.body-sm}`.

### Category & Filtering

**`category-tile`** — Square or 4:3 card with plant category photography and overlaid title text. Used on the homepage grid to guide users into taxonomy. Soft shadow and `{rounded.sm}` corners. On hover, a slight scale transform (1.02) provides tactile feedback.

**`filter-chip`** — Pill-shaped toggles for refining plant listings by sun exposure, zone, height, bloom color. Default state uses soft gray surface with hairline border; active state fills solid teal with white text.

### Footer

**`footer`** — Dark ink background (#222222) with white text organized in 4-column grid: Shop categories, Resources (planting guides, FAQs), Company info, and Newsletter signup. Footer headings use `{typography.title-sm}` in white. Links use `{typography.body-sm}` with subtle opacity hover (0.7 → 1.0).

### Utility

**`breadcrumb`** — Horizontal path trail (Home › Trees › Shade Trees › Red Maple) in muted body-sm text. Separators render in hairline color. Current page omits the link treatment and displays in `{colors.ink}`.

**`quantity-selector`** — Compact minus/value/plus control with `{rounded.sm}` border. Plus and minus buttons highlight to `{colors.surface-soft}` on hover. Used on PDP and cart line items.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + search icon; hero text drops to `{typography.display-md}`; category tiles stack 2-up; filter chips horizontally scroll; footer stacks single-column |
| Tablet | 744–1128px | 2-up product grid; nav shows condensed category links; hero maintains full-bleed with reduced min-height (360px); filter panel as slide-out drawer |
| Desktop | 1128–1440px | 3-up or 4-up product grid; full horizontal nav with category bar; sticky sidebar filters on collection pages; hero at full 480px height |
| Wide | > 1440px | Content max-width 1440px centered; 4-up product grid with increased card padding; generous `{spacing.section-lg}` between page sections |

### Touch Targets
- All interactive elements maintain minimum 44×44px tap area on mobile
- Filter chips carry 8px vertical padding plus surrounding margin to prevent mis-taps
- Mobile "Add to Cart" button stretches full-width on PDP for easy thumb access
- Quantity selector buttons padded to 44px square hit areas despite 40px visual height

### Collapsing Strategy
- Desktop sidebar filters collapse into a modal/drawer on tablet and mobile, triggered by a "Filter & Sort" button
- Category bar condenses into a horizontally-scrollable row on tablet and disappears into the hamburger menu on mobile
- Product card information prioritizes: image → title → price → zone badge; botanical name and secondary details hide below 744px
- Footer columns collapse into accordion sections on mobile with tap-to-expand headings
- Trust bar items stack vertically on mobile or cycle in a single-line carousel

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font weights for Barlow and Figtree could not be confirmed beyond presence of the family stacks; weights above are inferred from visual hierarchy
- No theme-color meta tag was extracted; mobile browser chrome color is unknown
- Specific box-shadow values on cards and nav are approximated from visual inspection rather than computed styles
- Transition/animation durations (hover states, drawer slides) could not be extracted from static analysis
- Icon system details (SVG sprite vs inline, stroke width, optical sizing) are undetermined
- Exact max-width constraint for the content container at wide breakpoints is estimated at 1440px
- Dark-mode palette, if any, was not detected
- Promotional banner rotation logic and timing could not be inferred from static extraction
