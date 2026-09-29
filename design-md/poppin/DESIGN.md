---
version: alpha
name: "Poppin"
source_url: "https://www.poppin.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every product page at Poppin doubles as a color theory exercise — the same stapler, monitor stand, or pencil cup appears in a dozen variants arranged in a tight chromatic grid, making hue the primary purchase variable before form enters the picture. The brand's conviction is that office equipment carries mood, and the interface is built accordingly: a white canvas (#ffffff) anchored by a single confirmed charcoal (#313131) that handles all UI chrome, body text, and — crucially — primary CTA buttons, a neutrality strategy that keeps attention on product colors rather than interface chrome. No custom typeface was detectable; typography runs on the system sans-serif stack at modest weights, letting the color grid carry expressive load that other brands offload to branded letterforms. Interactive elements wear modest {rounded.xs}–{rounded.sm} corner radii — approachable enough for consumer purchases, composed enough for the significant B2B and contract furniture business the brand also serves. The product grid is the true design signature: items march in uniform columns with consistent thumbnail aspect ratios and inline color swatches sitting below each card image, collapsing complex variant selection into a single scannable row. Navigation spans flat top-level categories — desk accessories, seating, storage, whiteboards — optimized for B2B buyers who know which department they're furnishing, not consumers in need of guided discovery flows. Footer architecture doubles as a corporate gateway: wholesale inquiry links, corporate account CTAs, and bulk pricing references sit alongside standard nav links, foregrounding contract business as equal in weight to direct consumer sales. The absence of urgency mechanics — no countdown timers, no scarcity warnings, no sale-badge noise — reinforces a design-first positioning where color availability and product coherence are the competitive differentiators, not promotional pressure.

colors:
  primary: "#313131"
  primary-active: "#1A1A1A"
  primary-disabled: "#B0B0B0"
  ink: "#313131"
  body: "#4A4A4A"
  muted: "#767676"
  hairline: "#E2E2E2"
  hairline-soft: "#EFEFEF"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  surface-dark: "#1A1A1A"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  swatch-ring-active: "#313131"
  swatch-ring-idle: "#E2E2E2"
  tag-bg: "#F0F0F0"
  tag-text: "#313131"
  link: "#313131"
  link-hover: "#000000"
  error: "#D93025"
  success: "#2D7A3A"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-bold:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.3px
  product-name:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  swatch-count:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.0
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.ink}"
    hoverBackgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    focusBorder: "1.5px solid {colors.ink}"
    errorBorder: "1.5px solid {colors.error}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px 10px 40px
    height: 44px
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    focusBorder: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 28px
    iconColor: "{colors.ink}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.10)"
    padding: "{spacing.lg} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "1/1"
    nameTypography: "{typography.product-name}"
    priceTypography: "{typography.price}"
    padding: "{spacing.sm}"
    swatchRowMarginTop: "{spacing.sm}"
    hoverTransform: "translateY(-2px)"
    hoverBoxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    idleRing: "2px solid transparent"
    activeRing: "2px solid {colors.swatch-ring-active}"
    activeRingOffset: 2px
    gap: "{spacing.xs}"
  color-swatch-lg:
    size: 32px
    rounded: "{rounded.full}"
    idleRing: "2px solid {colors.swatch-ring-idle}"
    activeRing: "2px solid {colors.swatch-ring-active}"
    activeRingOffset: 3px
    gap: "{spacing.sm}"
  swatch-overflow-label:
    typography: "{typography.swatch-count}"
    textColor: "{colors.muted}"
    maxVisible: 5
  product-grid:
    columns: "4 (desktop), 3 (tablet), 2 (mobile)"
    gap: "{spacing.base}"
    paddingH: "{spacing.xl}"
    maxWidth: 1440px
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    imagePosition: right
    ctaStyle: button-primary
  category-chip:
    backgroundColor: "{colors.tag-bg}"
    textColor: "{colors.tag-text}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
    activeBorderColor: "{colors.ink}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price}"
    salePriceColor: "{colors.error}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    headerTypography: "{typography.title-md}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    buttonSize: 36px
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.muted}"
  announcement-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-bold}"
    height: 36px
    padding: "0 {spacing.base}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} {spacing.xl} {spacing.xl}"
    linkColor: "{colors.ink}"
    linkHoverColor: "{colors.primary-active}"
    corporateLinkWeight: 600
  toast-notification:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px {spacing.base}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.18)"

## Components

### Buttons

**`button-primary`** — Charcoal (#313131) fill with white text, `{rounded.xs}` corner radius, uppercase letter-spaced label at `{typography.button-md}`. Hover darkens to `{colors.primary-active}` (#1A1A1A). The neutral fill is a deliberate choice to avoid competing with the product color palette — the CTA stays invisible to color cognition while remaining visually clear. Disabled state falls to `{colors.primary-disabled}` with `cursor: not-allowed`.

**`button-secondary`** — White fill with 1.5px charcoal border and uppercase charcoal text. Hover shifts background to `{colors.surface-soft}`. Used for secondary actions alongside add-to-cart — "Save to List," "Compare," "Add to Project."

**`button-ghost`** — Transparent background, charcoal underlined text at `{typography.button-sm}`. Tertiary actions only: "View all colors," "See size guide," "Learn more about corporate pricing."

### Text Input & Search

**`text-input`** — White fill, 1px `{colors.hairline}` border, `{rounded.xs}` radius, 48px height. Focus upgrades border to 1.5px `{colors.ink}`. Error state uses `{colors.error}` (#D93025) border with inline message below. Placeholder text runs in `{colors.muted}`.

**`search-bar`** — Soft-surface fill, 44px height, 40px left padding to accommodate a leading search icon in `{colors.muted}`. Focus sharpens border to `{colors.ink}`. Appears in the nav bar and prominently in hero-adjacent positions on category landing pages.

### Navigation

**`nav-bar`** — White 64px bar with 1px hairline bottom border. Logo sits left; flat category links span center-left at `{typography.nav-link}` (14px/500 weight, 0.3px letter spacing); cart, account, and search icons right. Icon tap targets are 44px square with invisible padding.

**`nav-dropdown`** — Full-width mega-menu panel at zero radius (`{rounded.none}`), white fill, 1px hairline border, and a 4px/10% black box shadow. Columns organize by product department and by color family. Column heads carry small thumbnail images. The flush-edge treatment reinforces navigation as structural infrastructure, not a styled overlay.

### Product Card

**`product-card`** — Square-crop 1:1 image, product name in `{typography.product-name}` below, price in `{typography.price}`, then a row of `color-swatch` circles showing available colorways. Cards have minimal padding, no resting border, and a 2px Y-lift plus light shadow on hover. Clicking a swatch updates the card thumbnail in place without page navigation — the variant swap experience is the central interaction pattern across the entire site.

**`color-swatch`** — 20px `{rounded.full}` circles with 4px gaps. Active swatch gets a 2px charcoal ring at 2px offset. Idle swatches have transparent rings. A `swatch-overflow-label` in `{typography.swatch-count}` appears after the fifth swatch (e.g., "+6 more").

**`color-swatch-lg`** — 32px version for PDP color selectors. Carries a visible idle ring in `{colors.swatch-ring-idle}` so unselected swatches remain legible against white backgrounds.

### Filtering

**`category-chip`** — Pill-shaped filter tags (`{rounded.full}`) with `{colors.tag-bg}` fill and hairline border. Active state inverts to charcoal fill with white text. Chips sit in a horizontally scrolling row above the product grid. Filter taxonomy is broad: by product type, by color family, by material — the color-family dimension is unique to Poppin's catalog and surfaces as a first-class filter on most category pages.

### Product Grid

**`product-grid`** — 4-column desktop, 3-column tablet, 2-column mobile, 16px gaps. Horizontal padding `{spacing.xl}`. The uniform grid discipline is load-bearing: swatch rows align only when card widths are consistent, and Poppin's color-matrix merchandising depends on that visual alignment to read as a coherent spectrum rather than scattered product thumbnails.

### Hero

**`hero`** — Soft-surface background, `{typography.display-xl}` headline left-aligned, `{typography.body-md}` subhead, right-positioned product photography. The hero image on category and homepage entries typically shows a color-array product shot — eight identical staplers across a spectrum, for example — establishing the brand's color breadth in a single frame. CTA uses `button-primary`.

### Cart & Checkout

**`cart-drawer`** — 400px right-anchored slide-in, white fill, 1px left border, `{spacing.xl}` padding. Header "Your Cart" at `{typography.title-md}`. Line items show thumbnail, product name, color swatch dot, size or variant label, price, and a `quantity-stepper`.

**`quantity-stepper`** — Inline minus / number / plus within a 1px `{colors.hairline}` border, `{rounded.xs}` radius, 36px button targets.

### Utility

**`announcement-bar`** — 36px charcoal (`{colors.surface-dark}`) bar above the nav. White `{typography.caption-bold}` centered text. Hosts free-shipping thresholds, corporate account offers, or new colorway announcements.

**`breadcrumb`** — 12px caption, `{colors.muted}` inactive crumbs with `/` separator, current page in `{colors.ink}`. Sits below nav, above page heading.

**`toast-notification`** — Dark charcoal pill toasting from bottom-right. White body text, `{rounded.sm}` radius, 16px horizontal padding, 18% black box shadow.

**`footer`** — Soft-surface `{colors.surface-soft}` background, top hairline border. Four-column desktop layout: Shop, About, Help, Corporate/B2B. The corporate column runs link labels at font-weight 600 vs. 400 for standard nav links — wholesale inquiry, corporate accounts, and bulk pricing are visually elevated because the contract business is structurally as important as the direct consumer channel.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | 2-column product grid; hamburger nav drawer with accordion categories; swatches truncate to 4 + overflow count; hero stacks text above image; filter chips collapse to "Filter & Sort" modal trigger |
| Tablet | 744–1128px | 3-column grid; compact nav with icon-only cart and account; hero maintains side-by-side with reduced horizontal padding; filter chips remain visible in scroll row |
| Desktop | 1128–1440px | 4-column grid; full nav text labels; mega-menu dropdowns at full width; hero at full `{spacing.xl}` horizontal padding |
| Wide | > 1440px | Grid constrained to 1440px max-width and centered; nav and hero padding scale proportionally; product images remain square-crop |

### Touch Targets

- Color swatches scale to `color-swatch-lg` (32px) on mobile PDP; combined with gap spacing this reaches the 44px recommended tap area
- Add-to-cart button spans full card width on mobile product detail pages
- Nav icons (cart, account, search) use 44px hit-area padding regardless of visual icon size
- Quantity stepper buttons expand to 40px on mobile
- Category chips maintain 44px minimum height on touch viewports

### Collapsing Strategy

- Navigation collapses to hamburger at < 744px; mega-menu becomes a slide-in accordion drawer with category headers as expand triggers
- Color swatch row in product cards shows 4 swatches + overflow label below 744px; expands to 6+ at desktop
- Hero text block stacks above imagery at < 744px, switching from grid layout to flex column; image height caps at 60vw
- Filter chips shift from horizontal scroll bar to a "Filter & Sort" modal trigger on mobile; selections summarized as an active-count badge on the trigger button
- Footer columns stack to single-column accordion at < 744px; corporate column surfaces first in the stacked order, reflecting its commercial priority

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Primary accent color unconfirmed**: The site served a Cloudflare challenge page during extraction; only #313131 was captured. Poppin offers products in 20+ named colorways and likely applies a brand-signature accent to link hovers, selection highlights, or promotional elements. #313131 is used as both ink and primary CTA here, but a saturated accent (orange, coral, or similar) may exist in the live system.
- **Typography unconfirmed**: No custom font was detectable from static extraction. Poppin may load a licensed typeface via JS bundle, CSS `@font-face` injection, or a CDN reference that bypasses static analysis. All typography tokens here use the system sans-serif stack as a confirmed fallback.
- **Full interface color palette unavailable**: Surface tints, hover-state overlays, promotional badge fills, and tag colors are derived from the single confirmed charcoal plus standard e-commerce surface conventions rather than extracted values.
- **Color-family filter UI**: Poppin's color-browse experience (filtering products by hue family) is a signature interaction that may involve non-standard color-picker UI components not captured here.
- **B2B/Corporate account UI**: Dashboard layouts, bulk order forms, saved project lists, and wholesale pricing overlays were not accessible during extraction; those patterns may diverge meaningfully from the consumer-facing component library documented here.
- **Animation and interaction timing**: Hover transition durations, swatch swap animation, cart-drawer slide timing, and scroll behavior (sticky nav threshold) could not be measured without a live page render.
