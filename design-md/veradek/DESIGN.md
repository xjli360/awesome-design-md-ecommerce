---
version: alpha
name: "Veradek"
source_url: "https://www.veradek.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep forest green (#00371f) anchors every navigation bar, primary button, and hero overlay on Veradek's site — a color so saturated it reads almost black until sunlight hits a screen outdoors, which is precisely where the brand's planters live. The secondary palette layers three botanical greens: a bright leaf (#a9c772) for badges and seasonal callouts, a softer sage (#b6cf91) for hover states and accent fills, and a muted eucalyptus (#809b8f) that quietly colors divider lines and icon containers. Typography pairs Domaine — a high-contrast serif used sparingly at display scale for campaign headlines — with Euclid Circular B as the workhorse geometric sans across body, navigation, and buttons; Montserrat appears only in uppercase micro-labels and product-spec tables. Cards sit on a pure white surface with `{rounded.sm}` corners and a single `{colors.hairline}` border, never a drop shadow, letting oversized product photography (planters shot on patios, terraces, urban rooftops) serve as the sole visual texture. Spacing is generous: `{spacing.section}` between content blocks, `{spacing.xl}` gutters on desktop grids, producing the open-air feel of a landscape catalog rather than a cramped e-commerce shelf. The dark charcoal ink (#22201e) replaces pure black for long-form descriptions, keeping contrast high without harshness against the near-white canvas (#f5f5f5). A warm peach (#fddab5) surfaces only in promotional banners and sale badges, providing temperature contrast against the dominant cool-green system. Button radii stay tight at `{rounded.xs}` — square enough to feel architectural, echoing the geometric silhouettes of Veradek's rectangular and cube-shaped planters.

colors:
  primary: "#00371f"
  primary-active: "#0f2e1d"
  primary-disabled: "#809b8f"
  accent-leaf: "#a9c772"
  accent-sage: "#b6cf91"
  accent-eucalyptus: "#99afa5"
  accent-warm: "#fddab5"
  ink: "#22201e"
  body: "#272d45"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#e0e0e0"
  hairline-soft: "#eaeaea"
  border-strong: "#c7c7c7"
  canvas: "#f5f5f5"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  surface-strong: "#f4f4f6"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#6d2323"
  error-soft: "#874c4c"
  slate: "#2c3e50"
  sage-tint: "#c8d0cc"
  dark: "#121212"

typography:
  display-xl:
    fontFamily: "'Domaine', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Domaine', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Domaine', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'EuclidCircularB', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'EuclidCircularB', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'EuclidCircularB', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'EuclidCircularB', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'EuclidCircularB', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'EuclidCircularB', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'EuclidCircularB', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'EuclidCircularB', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'EuclidCircularB', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  micro-label:
    fontFamily: "'Montserrat', -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Montserrat', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'EuclidCircularB', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-add-to-cart:
    backgroundColor: "{colors.accent-leaf}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 52px
    border: none
  button-add-to-cart-hover:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.primary}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  text-input-error:
    border: 1px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline-soft}
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    boxShadow: 0 2px 8px rgba(0,55,31,0.06)
  nav-mega-menu:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg}"
    borderTop: 1px solid {colors.hairline-soft}
    boxShadow: 0 8px 24px rgba(0,55,31,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline-soft}
    padding: 0
    overflow: hidden
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    aspectRatio: 1 / 1
    objectFit: cover
  product-card-body:
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    subtitleTypography: "{typography.body-sm}"
  product-card-hover:
    border: 1px solid {colors.primary}
    boxShadow: 0 4px 16px rgba(0,55,31,0.08)
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    overlay: linear-gradient(to right, rgba(0,55,31,0.85), transparent)
  hero-split:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section-lg} {spacing.xl}"
    imagePosition: right
    imageFit: cover
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    descriptionTypography: "{typography.body-md}"
    padding: "{spacing.xxl} 0"
    textAlign: center
  badge-sale:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.accent-leaf}"
    textColor: "{colors.primary}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-bestseller:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  color-swatch:
    rounded: "{rounded.full}"
    height: 28px
    width: 28px
    border: 2px solid {colors.hairline}
  color-swatch-active:
    border: 2px solid {colors.primary}
    boxShadow: 0 0 0 2px {colors.surface-card}, 0 0 0 4px {colors.primary}
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    border: 1px solid {colors.hairline}
  size-selector-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: 1px solid {colors.primary}
  spec-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    rowPadding: "{spacing.md} 0"
    borderBottom: 1px solid {colors.hairline-soft}
  search-overlay:
    backgroundColor: "rgba(18,18,18,0.6)"
    contentBackground: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    maxWidth: 640px
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 14px 16px 14px 44px
    height: 52px
    border: none
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.sage-tint}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"
  announcement-bar:
    backgroundColor: "{colors.accent-leaf}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
---

## Components

### Buttons

**`button-primary`** — Deep forest green (#00371f) fill with white text set in Euclid Circular B 600 weight at 15px. Corners use `{rounded.xs}` (4px) to match the architectural geometry of Veradek's planter silhouettes. On hover, the background darkens to `{colors.primary-active}` (#0f2e1d). Disabled state uses `{colors.primary-disabled}` (#809b8f) at reduced opacity.

**`button-secondary`** — White fill with a 2px forest-green border and green text. On hover, the fill inverts to `{colors.primary}` with white text, creating a satisfying color-flip transition. Used for "View Details" and "Compare" actions where the primary CTA should retain visual dominance.

**`button-add-to-cart`** — Bright leaf green (#a9c772) fill with dark green text, slightly taller at 52px to anchor the product detail page's purchase zone. The warm-green tone differentiates it from the site-wide primary and signals "go" without competing with navigational elements.

### Navigation

**`nav-bar`** — 72px-tall white bar with a subtle bottom hairline. Logo sits left, category links center (Euclid Circular B 500/14px), utility icons right. On scroll, the bottom border disappears and a soft box-shadow (`rgba(0,55,31,0.06)`) slides in. The mega-menu drops below with `{spacing.lg}` internal padding, organized in a grid with product-category thumbnails.

**`announcement-bar`** — A 40px strip in `{colors.accent-leaf}` sits above the nav bar with promotional copy ("Free shipping on orders $99+") in dark green. Uses `{typography.caption}` weight for readability at small size.

### Product Cards

**`product-card`** — White card with `{rounded.sm}` corners and a barely-visible `{colors.hairline-soft}` border. The image area fills a 1:1 ratio container with a light-gray (`{colors.surface-soft}`) placeholder behind it. Below the image, `{spacing.base}` padding wraps the product title (Euclid 600/16px), price (Euclid 700/18px), and an optional color-swatch row. On hover, the border transitions to `{colors.primary}` and a 4px/16px spread shadow lifts the card.

### Hero Sections

**`hero-banner`** — Full-bleed lifestyle photography (planters on patios, rooftop gardens) with a left-to-right dark-green gradient overlay. Headline text uses Domaine serif at 48px/700, body copy in Euclid 400/16px, and a `button-primary` CTA. Minimum height 560px ensures cinematic presence even on wide viewports.

**`hero-split`** — Two-column layout on desktop: left column holds headline (Domaine 36px), descriptive paragraph, and CTA; right column is an edge-to-edge product image. Used on collection landing pages where product context matters more than mood.

### Badges

**`badge-sale`** — Warm peach (#fddab5) background with dark ink text, creating visible contrast against both white cards and green overlays. Positioned absolute in the top-left corner of product-card images with 4px radius matching the card's corner style.

**`badge-new`** and **`badge-bestseller`** — Leaf green and forest green variants respectively, both using `{typography.micro-label}` (Montserrat 11px uppercase 700) for maximum legibility at small sizes.

### Product Detail

**`color-swatch`** — 28px circles with a hairline border. Active state adds a double-ring effect: 2px white gap then 2px green outline via box-shadow, clearly indicating selection without tooltip dependency.

**`size-selector`** — Pill-like rectangles with `{rounded.xs}` corners in a horizontal row. Active state fills forest green with white text. Disabled (out-of-stock) state uses `{colors.hairline}` fill with struck-through text.

**`spec-table`** — Alternating rows with Montserrat uppercase labels on the left and Euclid body values on the right, separated by `{colors.hairline-soft}` lines. Used for dimensions, materials, weight capacity, and drainage specs.

### Search

**`search-overlay`** — A dark scrim (`rgba(18,18,18,0.6)`) covers the viewport. A centered 640px-wide white panel with `{rounded.sm}` corners holds the search input and instant results. The input field uses `{colors.surface-soft}` fill with no border and a left-aligned magnifying glass icon.

### Footer

**`footer`** — Full-width forest green (#00371f) background with four-column link grid. Headings use `{typography.title-sm}` in white; links use `{colors.sage-tint}` (#c8d0cc) for softer contrast that doesn't compete with body content above. Bottom row holds copyright, payment icons, and social links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces nav links, hero text overlays center-aligned at 28px display, footer collapses to accordion, announcement bar text truncates with ellipsis |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, hero maintains full bleed with reduced min-height (420px), mega-menu becomes scrollable drawer |
| Desktop | 1128–1440px | Three- or four-column product grid, full mega-menu hover, hero at 560px min-height, split-hero shows 50/50 columns, footer four-column layout |
| Wide | > 1440px | Content max-width caps at 1440px and centers, product grid gains additional gutter space, hero images extend to bleed while text column stays within max-width |

### Touch Targets

- All interactive elements maintain minimum 44×44px touch area on mobile
- Color swatches expand tap target to 44px via transparent padding despite 28px visible size
- Product cards are fully tappable (entire card is link target), not just the title text
- Footer accordion headers use 48px row height with full-width hit area

### Collapsing Strategy

- Navigation collapses to a slide-out drawer at < 744px with full-height overlay and `{colors.primary}` header
- Product filters collapse to a bottom-sheet modal on mobile, remaining as a sidebar on tablet and above
- Spec tables reflow from two-column (label | value) to stacked single-column on mobile
- Hero split sections stack vertically (image on top, text below) at tablet breakpoint
- Product image galleries switch from thumbnail strip to swipeable carousel below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font-weight and OpenType features for Domaine could not be confirmed from extraction alone; weight 700 for display is inferred from visual density
- Euclid Circular B licensing and variable-font axis details not available from CSS extraction
- Animation/transition durations (hover states, mega-menu reveals, cart drawer slides) not captured
- Exact box-shadow values on scrolled nav and card hovers are approximated from visual inspection
- Icon system details (stroke weight, grid size, custom vs. library) not determinable from color/font extraction
- Dark-mode or alternate theme tokens not detected; site appears to use a single light theme
- Montserrat usage scope is inferred from font-stack presence — actual deployed locations may differ from spec-label and micro-label assignments above
