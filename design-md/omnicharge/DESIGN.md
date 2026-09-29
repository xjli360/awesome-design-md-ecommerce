---
version: alpha
name: "Omnicharge"
source_url: "https://www.omnicharge.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Red voltage arcs across a near-black field — that single #ec0101 punch is the visual shorthand Omnicharge uses to signal raw wattage in a market drowning in matte-white pebble chargers. The site opens on a deep #121212 canvas with product photography lit like studio stills: power stations float against darkness, their LED indicators glowing in brand-red and status-green (#428445), letting the hardware do the talking rather than lifestyle imagery. Typography is pure Roboto at disciplined weights — headlines land at 600/700 in the 32–48px range, body copy at 400/16px — no custom face, no decorative serif, just the mechanical neutrality of a spec sheet that happens to be beautiful. Navigation sits in a slim white bar with dark ink text, creating a stark frame-shift from the immersive hero below. Product cards use `{rounded.sm}` corners on `{colors.surface-card}` backgrounds with generous `{spacing.lg}` internal padding, each card anchored by a single product silhouette and a bold price in `{typography.title-md}`. CTAs are solid red rectangles (`{rounded.xs}`) — deliberately squared-off to echo the angular aluminum chassis of the power stations themselves. A secondary gold tone (#e0b252) surfaces for premium-tier badges and limited-edition callouts, while an orange (#ff4e00) fires on urgency states like low-stock alerts. The spacing system breathes at `{spacing.section}` (64px) between major blocks, compressing to `{spacing.base}` (16px) inside dense spec-comparison grids that are central to the purchase decision. Overall the system reads as an industrial catalog with consumer polish — dark, confident, and information-dense without clutter.

colors:
  primary: "#ec0101"
  primary-active: "#c40000"
  primary-disabled: "#f5a3a3"
  ink: "#121212"
  body: "#383838"
  muted: "#878787"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#dfdfdf"
  canvas: "#ffffff"
  canvas-dark: "#121212"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#222222"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-green: "#428445"
  accent-gold: "#e0b252"
  accent-orange: "#ff4e00"
  accent-blue: "#0774d7"
  success: "#109533"
  error: "#eb001b"
  status-green: "#00a500"

typography:
  display-xl:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.3px
  button-lg:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-md:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  price:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 700
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 1px solid {colors.hairline}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.ink}
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-outline-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    border: 1px solid {colors.on-dark}
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.ink}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline-soft}
  nav-bar-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    imageAspect: 1:1
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
  product-card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    imageAspect: 1:1
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
  hero-section:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-lg}"
    padding: "{spacing.section-lg} {spacing.xl}"
    minHeight: 600px
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headerTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-md}"
    rowPadding: "{spacing.md} 0"
    rowBorder: 1px solid {colors.hairline-soft}
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 6px 10px
  premium-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  urgency-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  status-indicator:
    activeColor: "{colors.status-green}"
    errorColor: "{colors.error}"
    size: 8px
    rounded: "{rounded.full}"
  comparison-grid:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headerTypography: "{typography.title-sm}"
    cellTypography: "{typography.body-sm}"
    cellPadding: "{spacing.md} {spacing.base}"
    border: 1px solid {colors.hairline}
    rounded: "{rounded.sm}"
  feature-icon-block:
    backgroundColor: "{colors.surface-soft}"
    iconColor: "{colors.ink}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    iconSize: 40px
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px 12px 40px
    height: 44px
  wattage-display:
    textColor: "{colors.primary}"
    typography: "{typography.display-xl}"
    unitTypography: "{typography.title-lg}"

---

## Components

### Buttons

**`button-primary`** — Solid #ec0101 red with white text, `{rounded.xs}` corners producing a squared-off industrial shape. Hover darkens to `{colors.primary-active}` (#c40000) with a subtle 120ms ease transition. Disabled state washes to `{colors.primary-disabled}` with reduced opacity. Used for all revenue-critical actions: Add to Cart, Buy Now, Subscribe.

**`button-secondary`** — White fill with a 1px `{colors.hairline}` border and `{colors.ink}` text. On hover the border snaps to `{colors.ink}` and background shifts to `{colors.surface-soft}`. Paired alongside primary buttons for secondary actions like "Learn More" or "Compare Models."

**`button-dark`** — Solid `{colors.ink}` (#121212) fill with white text. Used in dark hero contexts where the red primary would compete with product LED photography. Same `{rounded.xs}` corners and 48px height as the primary.

**`button-outline-dark`** — Transparent with a 1px white border, used on dark backgrounds for tertiary actions. On hover, fills to rgba(255,255,255,0.1). Smaller padding for inline placement near spec callouts.

### Navigation

**`nav-bar`** — 64px-tall white bar with a thin `{colors.hairline-soft}` bottom border. Logo sits left, nav links center in `{typography.nav-link}` (Roboto 500/14px), cart icon right. On scroll, gains a subtle box-shadow (0 2px 8px rgba(0,0,0,0.06)). On dark product pages, switches to `nav-bar-dark` variant with `{colors.canvas-dark}` background and white text.

**`announcement-bar`** — Full-width `{colors.primary}` red strip above the nav, 40px tall, centered white text in `{typography.caption}`. Used for shipping promos, sale events, or new product launches. Dismissible with an × icon.

### Product Display

**`product-card`** — Light `{colors.surface-soft}` background with `{rounded.sm}` corners. Product image sits in a 1:1 aspect container with no border. Below: product title in `{typography.title-md}`, a one-line capacity spec in `{typography.body-sm}` muted text, and price in `{typography.price}` (Roboto 700/20px). Hover lifts with box-shadow (0 4px 16px rgba(0,0,0,0.08)) and a 200ms ease transition.

**`product-card-dark`** — Same structure on `{colors.surface-dark}` for use within dark-background sections. Text flips to `{colors.on-dark}`. Used on the homepage hero grid where products sit against the dark canvas.

**`wattage-display`** — Large red numerals in `{typography.display-xl}` with the unit suffix ("Wh" / "W") in `{typography.title-lg}`. Used as a hero callout on product detail pages to emphasize capacity as the primary purchase signal.

### Specs & Comparison

**`spec-table`** — Clean two-column layout: left column uses `{typography.spec-label}` (uppercase 12px 700-weight Roboto with letter-spacing) for labels, right column uses `{typography.body-md}` for values. Rows separated by 1px `{colors.hairline-soft}` rules. No zebra striping — density is the priority.

**`comparison-grid`** — Multi-column table with a sticky header row on `{colors.surface-soft}`. Column headers display product names in `{typography.title-sm}`. Cells use `{typography.body-sm}` with `{spacing.md}` vertical and `{spacing.base}` horizontal padding. Check marks render in `{colors.accent-green}`, dashes in `{colors.muted}`. Outer container uses `{rounded.sm}` and a 1px `{colors.hairline}` border.

### Badges & Indicators

**`spec-badge`** — Small pill on `{colors.surface-soft}` with `{typography.caption}` text and `{rounded.xs}` radius. Used to tag features like "USB-C PD", "AC Outlet", "Wireless Charging" on product cards and detail pages.

**`premium-badge`** — Gold (#e0b252) background with dark text in `{typography.caption-sm}`. Applied to limited-edition or pro-tier products to visually separate them from standard SKUs.

**`urgency-badge`** — Orange (#ff4e00) fill with white text. Appears on product cards and cart when inventory falls below threshold. Text reads "Low Stock" or "Last 5 Units."

**`status-indicator`** — 8px circle, fully rounded (`{rounded.full}`). Green (`{colors.status-green}`) for in-stock/charging, red (`{colors.error}`) for out-of-stock/fault. Placed inline next to availability text.

### Content Blocks

**`hero-section`** — Full-bleed dark canvas (`{colors.canvas-dark}`) with centered or left-aligned layout. Headline in `{typography.display-xl}`, subtitle in `{typography.body-lg}`, both white. A single CTA button (primary-red or dark variant) sits below with `{spacing.lg}` top margin. Product photography occupies the opposing half or background layer. Minimum height 600px.

**`feature-icon-block`** — Grid item used in 3- or 4-column feature grids. Light `{colors.surface-soft}` card with `{rounded.sm}` corners, 40px monoline icon at top, title in `{typography.title-sm}`, description in `{typography.body-sm}` muted. Padding `{spacing.lg}` all sides.

### Search & Input

**`text-input`** — 48px-tall field with `{rounded.xs}` corners, 1px `{colors.hairline}` border, transitioning to `{colors.ink}` on focus. Placeholder in `{colors.muted}`. Label sits above in `{typography.caption}`.

**`search-input`** — Slightly shorter (44px) with `{colors.surface-soft}` fill, no visible border at rest. A 20px search icon sits left-inset. On focus, gains a 1px `{colors.ink}` border. Used in the nav flyout and support/FAQ pages.

### Footer

**`footer`** — Dark `{colors.canvas-dark}` background spanning full width. Four-column link grid in `{typography.body-sm}` with `{colors.muted}` default color brightening to `{colors.on-dark}` on hover. Bottom row carries legal text, payment icons, and social media links. Top padding `{spacing.section}`.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks vertically (image above, text below); nav collapses to hamburger + logo + cart icon; comparison grid becomes horizontally scrollable; section padding drops to `{spacing.xl}` |
| Tablet | 744–1128px | Two-column product grid; hero splits 50/50; nav shows top-level links, secondary items behind "More" dropdown; spec table remains full-width |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero uses asymmetric 60/40 split; comparison grid shows up to 4 products side-by-side |
| Wide | > 1440px | Content max-width caps at 1440px and centers; product grid expands to four columns; hero image scales proportionally with generous negative space |

### Touch Targets

- All interactive elements maintain a minimum 44×44px touch area on mobile
- Buttons use full-width stacking on viewports below 744px
- Nav hamburger icon has 48×48px tap zone with 8px padding beyond the visual icon
- Product card entire surface is tappable, not just the title link

### Collapsing Strategy

- Desktop mega-menu nav collapses to a slide-in drawer on mobile with full-height overlay
- Spec comparison grid switches from fixed columns to a horizontally scrollable container with snap points
- Feature icon grids collapse from 4-col → 2-col → 1-col stack
- Footer columns collapse into accordions on mobile, each section header tappable to expand
- Announcement bar text truncates with ellipsis on narrow viewports; full message visible on tap

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one font family (Roboto) detected; the brand may load additional display weights or a secondary face via JavaScript or Shopify's font loader that wasn't captured in static extraction
- No custom icon set or SVG sprite information could be extracted — the brand likely uses inline SVGs or an icon font loaded asynchronously
- Exact border-radius values from live components could not be confirmed (values inferred from visual patterns); actual implementation may use slightly different rounding
- Animation/motion tokens (easing curves, duration scales) are not represented in extraction data
- Dark mode toggle behavior unclear — the site uses dark sections extensively but whether a full dark-mode preference is respected via `prefers-color-scheme` is unknown
- Email/newsletter modal styling and popup timing could not be captured from static extraction
- Mobile navigation drawer transition and overlay opacity values are estimated
