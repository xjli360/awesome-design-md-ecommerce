---
version: alpha
name: "AeroGarden"
source_url: "https://www.aerogarden.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The purple-magenta bloom of AeroGarden's LED grow-panels is the brand's sharpest design signal — a deliberate product decision that marks these countertop units as precision growing technology, not kitchen decor. That same confidence in category clarity shapes the visual system. Green carries the entire brand load: a saturated, mid-range growth green that reads closer to agricultural science than lifestyle wellness, sitting against backgrounds so clean they approach clinical whiteness. The extracted site canvas of #f6f6f6 confirms a near-zero-warmth base — AeroGarden does not reach for cream or linen to soften its technological premise. Cards, input fields, and modal surfaces step up only marginally to pure white, keeping the layering flat and readable rather than deeply shadowed.

  Typography leans toward compact, high-x-height sans-serifs — the kind of face that communicates legibly on a seed-pod label and a 4K monitor alike. Body copy runs tight, product spec tables use tabular figures, and CTAs tend toward sentence-case urgency ("Shop Now", "Add to Cart") rather than ALL-CAPS formality. The spatial rhythm is generous on hero sections — large imagery of lush basil and tomato clusters pushed to full-bleed — then tightens sharply at the product grid and spec level, where information density earns the space.

  Rounded corners sit in the mid-range (`{rounded.md}`, `{rounded.lg}`): assertive enough to signal a consumer product, restrained enough to avoid the pillow-soft look of meal-kit or supplement brands. Primary CTAs use `{rounded.full}` pill forms, tying the button shape to the cylindrical pods the hardware ships in. The product-card is the system's workhorse — a portrait-ratio image tile with pod-count badge, LED-type label, and price block — and it reads as a living plant catalog rather than an electronics listing.

  AeroGarden's brand green, the product's LED purple-pink, and the clean near-white `#f6f6f6` function as a minimal three-color system: photographic content (lush red tomatoes, bright green herbs inside glowing pods) provides all the chromatic richness the brand needs without additional accent hues. Component state changes rely on green-to-dark-green shifts rather than hue swaps, keeping the system cohesive at every scale from nav cart-count badges to full-bleed hero banners.

colors:
  primary: "#38a034"
  primary-active: "#2a7a28"
  primary-disabled: "#a8d4a6"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  grow-glow: "#c050d8"
  sale-red: "#e53935"
  warning-amber: "#f57c00"
  success: "#2e7d32"

typography:
  display-xl:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  spec-label:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  button-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
    states:
      hover:
        backgroundColor: "{colors.primary-active}"
      disabled:
        backgroundColor: "{colors.primary-disabled}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
    padding: 12px 26px
    height: 48px
    states:
      hover:
        borderColor: "{colors.primary-active}"
        textColor: "{colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoHeight: 36px
    cartBadge:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.badge}"
      rounded: "{rounded.full}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.md}"
    imageAspectRatio: "3/4"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    badgePosition: top-left
    shadow: "0 2px 8px rgba(0,0,0,0.06)"
    states:
      hover:
        shadow: "0 6px 20px rgba(0,0,0,0.12)"
        transform: "translateY(-2px)"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    minHeight: 560px
    layout: split-50-50
    textSide: left
    imageSide: right
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    ctaComponent: button-primary
    padding: "{spacing.xxl} {spacing.section}"
    mobileLayout: stack-image-top
  grow-pod-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  led-glow-badge:
    backgroundColor: "{colors.grow-glow}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  sale-badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    rowPadding: 12px 16px
    alternateRowBackground: "{colors.canvas}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
    height: 44px
    inputTypography: "{typography.body-sm}"
    iconColor: "{colors.muted}"
    padding: "0 {spacing.base}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    height: 40px
    textAlign: center
    linkColor: "{colors.on-primary}"
    linkDecoration: underline
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-bold}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    states:
      active:
        backgroundColor: "{colors.primary}"
        textColor: "{colors.on-primary}"
        border: none
  plant-count-ring:
    strokeColor: "{colors.primary}"
    trackColor: "{colors.surface-soft}"
    numberTypography: "{typography.display-sm}"
    numberColor: "{colors.ink}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    size: 120px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "#cccccc"
    linkHoverColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.section}"
    dividerColor: "#444444"
    logoFilter: "brightness(0) invert(1)"

## Components

### Buttons

**`button-primary`** — A full-pill `{rounded.full}` green CTA, 48px tall, in `{colors.primary}` with `{colors.on-primary}` text at `{typography.button-md}`. The pill form is consistent across the entire site: "Shop Now," "Add to Cart," and "Get Started" all share the same shape. Hover deepens to `{colors.primary-active}`; the disabled state uses `{colors.primary-disabled}` and removes the pointer cursor. The pill geometry deliberately echoes the cylindrical pod housings of the hardware product.

**`button-secondary`** — White fill with a 2px `{colors.primary}` outline at `{rounded.full}`, same 48px height as the primary. Used for "Learn More" and alternative CTAs adjacent to primaries in hero splits. Hover shifts border and text to `{colors.primary-active}` without filling the button, preserving the lighter visual weight.

**`button-ghost`** — Transparent fill, `{colors.ink}` text, `{colors.hairline}` 1px border, `{rounded.full}`, 40px height at `{typography.button-sm}`. Handles filter toggles, "View All" links, and utility nav actions like "Sign In" without competing with product CTAs.

### Text Input

**`text-input`** — White fill, `{colors.hairline}` 1px border, `{rounded.sm}`, 48px height at `{typography.body-md}`. On focus, the border steps to 2px `{colors.primary}` — the only moment the brand green appears on a form element. Placeholder text renders at `{colors.muted}`. Applied uniformly in email capture modules, the search field, and checkout forms.

### Navigation

**`nav-bar`** — 72px white bar with a 1px `{colors.hairline-soft}` bottom border. Logo sits left at 36px height; primary nav links use `{typography.nav-link}` in `{colors.ink}`; the cart icon carries a `{colors.primary}` badge at `{typography.badge}` for item count. A subtle box-shadow activates on scroll to maintain separation from scrolled content. On mobile below 744px, primary links collapse into a left-slide drawer behind a hamburger icon.

### Product Card

**`product-card`** — 3:4 portrait image tile with `{rounded.md}`, 1px `{colors.hairline-soft}` border, and a 6px shadow that lifts to 20px with a 2px upward translate on hover. The `grow-pod-badge` sits top-left of the image; `sale-badge` overlays top-right when active; the two never occupy the same corner simultaneously. Below the image: model name in `{typography.title-md}`, price in `{typography.price-display}` at `{colors.ink}`, and a condensed add-to-cart button using `{typography.button-sm}`.

### Hero Banner

**`hero-banner`** — Full-width 50/50 split with text left and product photography right, minimum 560px height. Headline at `{typography.display-xl}`, subhead at `{typography.body-md}` in `{colors.body}`. Background is `{colors.surface-soft}` (#f6f6f6), creating a seamless lift off the page canvas without a hard edge. Below 744px, layout stacks with image above (16:9 crop) and text below at reduced heading scale (`{typography.display-md}`).

### Grow Pod Badge

**`grow-pod-badge`** — A small `{colors.primary}` pill at `{rounded.xs}` displaying pod capacity in uppercase `{typography.badge}`: "6-POD", "9-POD", "24-POD". Appears on product cards, product detail pages, and comparison tables. The consistent green treatment links pod count directly to the brand's primary growth signal, making model differentiation scannable at a glance.

### LED Glow Badge

**`led-glow-badge`** — Same pill form as `grow-pod-badge` but rendered in `{colors.grow-glow}` (the brand's LED purple-pink). Used exclusively for "Full Spectrum LED" and grow-light type labels. Grounds the purple-pink in a functional product attribute — it is the color the light actually produces — rather than using it decoratively elsewhere in the system.

### Sale Badge

**`sale-badge`** — Identical geometry to `grow-pod-badge` and `led-glow-badge` but `{colors.sale-red}` fill. Displays "Sale" or percentage-off text at `{typography.badge}`. Positioned top-right of product card images, the opposite corner from `grow-pod-badge`, so all three badge types have consistent, non-overlapping placement rules.

### Spec Table

**`spec-table`** — Two-column key-value layout on a `{colors.surface-soft}` container with `{rounded.sm}` corners and `{colors.hairline}` dividers. Labels in `{typography.spec-label}` at `{colors.muted}`, values in `{typography.body-sm}` at `{colors.ink}`. Alternating rows flip to `{colors.canvas}` for readability across wattage, pod count, dimensions, and nutrient-solution specs. Used on all product detail pages.

### Search Bar

**`search-bar`** — Full-pill `{rounded.full}` input, 44px height, on `{colors.surface-soft}`. A magnifying-glass icon at `{colors.muted}` anchors the left side; padding is `{spacing.base}` each side. Border shifts from `{colors.hairline}` to `{colors.primary}` on focus. Lives inline in the desktop nav; on mobile, the search icon expands a full-width bar that overlays the nav row.

### Promo Banner

**`promo-banner`** — A 40px `{colors.primary}` strip pinned above the nav bar. Short promotional copy centered in `{typography.caption-bold}` white with an underlined link in `{colors.on-primary}`. Dismissible via an X icon. When a promo is active, the nav-bar's top border is replaced by the banner's bottom edge, so no double-line gap appears.

### Category Chip

**`category-chip`** — Small filter pills at `{rounded.full}` used on shop and search results pages. Default: `{colors.surface-soft}` fill, `{colors.hairline}` border, `{colors.body}` text at `{typography.caption-bold}`. Active: `{colors.primary}` fill, `{colors.on-primary}` text, border removed. Multiple chips can be active simultaneously. On mobile, chips scroll horizontally in a single snapping row.

### Plant Count Ring

**`plant-count-ring`** — A circular progress ring used in the "Track Your Grow" dashboard module. Stroke in `{colors.primary}`, track in `{colors.surface-soft}`. Center displays a large integer in `{typography.display-sm}` at `{colors.ink}` with a label like "pods growing" in `{typography.caption}` at `{colors.muted}`. Default size 120px; scales to 80px on mobile layouts.

### Footer

**`footer`** — Dark `{colors.ink}` base with the logo rendered white via `brightness(0) invert(1)` CSS filter. Four-column link grid on desktop — column headings in `{typography.title-sm}`, links in `{typography.body-sm}` at `#cccccc` hovering to `{colors.on-primary}`. Newsletter capture uses an inline email input above the link columns. Social icons row sits above the legal text line. On mobile below 744px, columns collapse to an accordion with expand/collapse per section.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks image (16:9) above text; nav collapses to hamburger drawer; search expands full-width overlay; spec table scrolls horizontally; footer collapses to accordion; category chips scroll in single horizontal row |
| Tablet | 744–1128px | Two-column product grid; hero split preserved but text column narrower; nav shows primary links, hides secondary utilities; promo banner shortens copy |
| Desktop | 1128–1440px | Three-column product grid; full 72px nav bar; hero at 50/50 split with full bleed photography; spec table shows all columns inline |
| Wide | > 1440px | Four-column product grid; content max-width 1440px centered; hero photography bleeds to viewport edge beyond the content container |

### Touch Targets

- All buttons minimum 48px height per WCAG 2.1 AA touch target guidance
- Category chips increase to 40px height and 10px 16px padding on mobile
- Nav hamburger, search icon, cart icon, and account icon each carry a 44×44px tap zone with compensating negative margins
- Grow pod, LED glow, and sale badges are display-only — no touch-target minimum applies
- Plant count ring interactive variant (if tapped to expand grow log) uses a 48px minimum tap radius

### Collapsing Strategy

- Primary nav collapses to hamburger at < 1128px; drawer slides from left with a semi-transparent scrim behind it
- Search becomes icon-only in nav below 744px; tapping icon expands a full-width bar overlaying the nav row with an autofocus input
- Hero splits to vertical stack at < 744px: photography first at 16:9 crop, then text block with heading scaled to `{typography.display-md}`
- Footer four-column grid stacks to single-column accordion below 744px; each section has an independent expand toggle
- Spec table switches from two-column inline layout to a horizontally scrollable strip below 744px with a fade-out right edge to signal overflow
- Promo banner trims to its shortest phrase on mobile; the dismiss X remains always visible and never collapses

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Palette severely under-extracted**: only `#f6f6f6` was captured from the live site. The brand-signature green (`#38a034`) is estimated from widely observed brand materials — verify the precise hex against the live DOM or brand guidelines before production use.
- **No font-family stacks detected**: the site likely loads its typeface via a JavaScript-injected stylesheet or CDN-hosted font CSS that bypassed extraction. The Inter system-font stack here is a plausible approximation for AeroGarden's clean sans-serif aesthetic; the actual typeface may differ (Proxima Nova and similar geometric sans-serifs are common in this product category).
- **LED glow purple (`#c050d8`) is a product-derived estimate**: this color is inferred from photography of AeroGarden's full-spectrum LED panels, not extracted from the CSS. It may not exist as a design-system token at all — confirm before using it in non-product-label contexts.
- **Meta theme-color absent**: no mobile browser chrome color was set on the scanned page, removing a secondary confirmation signal for the primary brand hue.
- **No shadow, spacing, or border-radius values were extracted from the DOM**: all padding, gap, box-shadow, and corner-radius values in this spec are inferred from product category conventions and visual inspection of brand photography, not measured from computed styles.
- **Dark mode support unknown**: no `prefers-color-scheme` media query tokens or dark surface palette variants were surfaced by extraction. Dark mode may not be implemented.
- **ScottsMiracle-Gro parent brand relationship**: the page title references ScottsMiracle-Gro as the parent company. It is unclear whether AeroGarden shares any design tokens with the parent brand's system or operates as a fully independent design system.
