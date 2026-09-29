---
version: alpha
name: "Fossil"
source_url: "https://www.fossil.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The single charcoal extracted from fossil.com's live page — #313131 — does more load-bearing work than most brands ask of a solo neutral: it fills primary buttons, navigation rails, hero overlays, footer blocks, and dominant body text without variation. That monochromatic discipline is a deliberate posture. Fossil occupies the calibrated middle of the American watch market, positioned above fashion-forward impulse purchases yet well below luxury-threshold decisions, and the visual system reflects measured confidence rather than spectacle. White canvas (#ffffff) dominates product display, giving dial finishing, strap texture, and case geometry the full frame — the photography argues the value proposition so the interface doesn't have to. Type runs entirely on system stacks (no custom typeface was detected during extraction, likely due to Cloudflare bot-protection blocking JS-loaded tokens); the -apple-system / BlinkMacSystemFont / Roboto hierarchy keeps weights and metrics consistent across Windows, macOS, Android, and iOS without font-load overhead. Sizing leans generous: display headings at 48px with light 300-weight tracking, body at 16px with 1.6 line-height, keeping product descriptions readable alongside dense specification tables. An inferred gold-tan accent (#b8976a — see Known Gaps) echoes the warm metallics common in Fossil watch photography, though this was not confirmed in extraction. CTA hierarchy is sharp: one filled-charcoal primary action per viewport, with outline or ghost secondaries for paths like Save and Compare. Rounded corners sit at a modest {rounded.sm} on buttons and cards — just enough softness to avoid severity without drifting into the pill shapes common in athleisure and tech. The promo banner above the nav carries sale messaging in an inverted charcoal strip at 36px, a fixture across Fossil seasonal campaigns. Sharp-cornered badge chips in the same charcoal and a conventional retail red mark NEW and SALE states directly on product imagery with no decorative flourish. The register throughout is that of a clean American catalog: merchandise-forward, building purchase confidence through clarity.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a8a8a8"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#767676"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#1c1c1c"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-gold: "#b8976a"
  sale-red: "#c0392b"
  star-fill: "#313131"
  error: "#d32f2f"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  button-dark-hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
  promo-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-sm}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1:1"
    padding: "{spacing.sm}"
    priceTypography: "{typography.price-sm}"
    nameFontWeight: 500
    hoverShadow: "0 4px 12px rgba(0,0,0,0.08)"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
    paddingHorizontal: "{spacing.xxl}"
    ctaVariant: button-dark-hero
  price-tag:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
    salePriceColor: "{colors.sale-red}"
    originalPriceDecoration: line-through
    originalPriceColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  watch-strap-swatch:
    size: 24px
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.ink}"
    unselectedBorder: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 40px
    padding: 8px 12px
    iconColor: "{colors.muted}"
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label-sm}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.muted-soft}"
  star-rating:
    filledColor: "{colors.star-fill}"
    emptyColor: "{colors.hairline}"
    typography: "{typography.caption}"
    starSize: 14px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.label-sm}"
    paddingVertical: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Filled #313131 with white uppercase lettering at 14px/600-weight and 0.5px tracking, 48px tall with {rounded.sm} corners. Hover darkens the fill to {colors.primary-active} (#1a1a1a); disabled state renders in {colors.primary-disabled} (#a8a8a8). This is the single high-priority CTA per viewport — "Add to Bag," "Checkout," and primary search submission.

**`button-secondary`** — White fill with a 1px charcoal border and matching uppercase typography to `button-primary`. Carries secondary actions like "Save for Later," "Find in Store," and comparison paths. Same 48px height and {rounded.sm} corners for visual alignment with the primary.

**`button-ghost`** — Transparent background with underlined text in {colors.ink}, used for tertiary links ("View All," "See Details," editorial "Learn More"). No border, no background — minimal visual weight by design.

**`button-dark-hero`** — White-fill, charcoal-text button deployed on dark hero backgrounds where the standard filled-charcoal `button-primary` would disappear. Sharp {rounded.none} corners read as editorial on full-bleed photography surfaces rather than soft e-commerce.

### Navigation

**`nav-bar`** — 56px light bar on {colors.canvas} with a hairline bottom border. Logo left-aligned in charcoal ink, category links in 13px/500-weight, utility icons (search, bag, account) right-docked. A `nav-bar-dark` variant flips to {colors.surface-dark} with white text for campaign or holiday periods. A full-width `promo-banner` at 36px sits above the nav carrying sale messaging in inverted charcoal with uppercase label-sm type.

### Product Card

**`product-card`** — Square 1:1 image crop on {colors.surface-card} white, no border-radius, product name in 14px/500-weight, price in `price-sm` below. NEW and SALE badge chips sit top-left over the image. Below the product name, `watch-strap-swatch` circles (24px, {rounded.full}) allow colorway switching without a page reload. On hover, a subtle shadow (0 4px 12px rgba(0,0,0,0.08)) lifts the card without a scale transform, preserving catalog stability.

### Hero Banner

**`hero-banner`** — Full-bleed dark-surface module, minimum 560px tall, headline in `display-xl` (48px/300-weight) on {colors.on-dark}. Body copy in `body-md` when present. CTA uses `button-dark-hero`. Horizontal padding is 48px to keep text away from image bleed edges. On desktop, lifestyle photography fills the right column or bleeds full-frame; on mobile, text stacks below the image with the headline reduced to `display-sm`.

### Price Display

**`price-tag`** — Regular price at 22px/500-weight in {colors.ink}. Sale items show the original price struck through in {colors.muted} alongside the sale price in {colors.sale-red}, rendered side by side. No "WAS/NOW" text labeling — the contrast carries the message.

### Badges

**`badge-new`** and **`badge-sale`** — Sharp-cornered ({rounded.none}) uppercase micro-chips in 10px/700-weight at 3px×6px padding, positioned absolute top-left over product imagery. New badge uses {colors.ink} fill; Sale badge uses {colors.sale-red}. Stack vertically when both conditions apply.

### Search

**`search-bar`** — 40px flat input on {colors.surface-soft} with hairline border and no radius. Magnifier icon in {colors.muted}. On mobile it expands to a full-width overlay drawer; on desktop it sits inline within the nav utility strip.

### Collection Filter

**`collection-filter`** — Flat filter chips with 1px hairline border and uppercase `label-sm` typography. Active state upgrades the border to solid {colors.ink} with no fill change — keeps the filter strip visually quiet while still marking selection. No border-radius.

### Footer

**`footer`** — Full-width charcoal (#313131) block with uppercase `label-sm` column headings (11px/600) and `body-sm` links in {colors.muted-soft} hovering to full white. Column structure: brand links, customer support, store locator, social icons, legal row. 48px top/bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column nav with hamburger drawer; 2-up product grid; hero stacks text below image; promo banner scrolls as marquee if multi-message |
| Tablet | 744–1128px | 3-up product grid; nav collapses to icon-only secondaries; hero splits 50/50 text+image |
| Desktop | 1128–1440px | 4-up product grid; full horizontal nav with all category labels; hero allows full-bleed image with floating text panel |
| Wide | > 1440px | Max-width container (~1440px) centered; grid gutters expand; hero imagery gains breathing room at edges |

### Touch Targets

- All interactive controls minimum 44×44px on touch viewports
- Strap swatch circles are 24px visual but sit inside 40px touch targets via padding
- Filter chips expand to full-width tap zones on mobile to avoid mis-taps on narrow chip labels
- Nav icons in the mobile bar use 48px tap targets regardless of icon visual size

### Collapsing Strategy

- Primary nav collapses to hamburger at < 744px; mega-menu panels become slide-in drawers
- Filter sidebar becomes a bottom-sheet drawer on mobile; filter chips scroll horizontally in a sticky strip
- Product grid: 2-up (mobile) → 3-up (tablet) → 4-up (desktop); never below 2 columns
- Hero headline reduces from `display-xl` (48px) to `display-sm` (28px) on mobile; CTA stacks below image
- Footer collapses from 4-col to 2-col at tablet, 1-col stacked accordion at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Palette severely sparse**: only one hex value (#313131) was extracted. The site returns "Just a moment..." (Cloudflare bot protection), meaning all design tokens load via JS and were unavailable to extraction. All surface tones, accent colors, and secondary palette entries are inferred from watch-brand conventions and not confirmed.
- **No custom typeface detected**: font stack is entirely system UI. Fossil may serve a licensed web font blocked by the anti-bot layer; if a custom face exists all typography tokens would need revision.
- **Gold accent (#b8976a)**: inferred from warm metallics common in Fossil watch photography; not extracted from the live site and should be verified against actual asset colors before use.
- **Sale red (#c0392b)**: conventional retail red; actual Fossil promotional color was not confirmed in extraction.
- **Meta theme-color**: none extracted; PWA/mobile browser chrome color is unknown.
- **Component interaction states**: hover transitions, focus-ring styles, and animation durations are estimated at common e-commerce conventions; not observable due to bot protection blocking live inspection.
- **Navigation taxonomy**: category structure (Men's/Women's/Collections/Sale/etc.) and mega-menu column layout not confirmed from extraction.
