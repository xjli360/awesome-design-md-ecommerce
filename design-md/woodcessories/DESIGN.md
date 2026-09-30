---
version: alpha
name: "Woodcessories"
source_url: "https://www.woodcessories.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep-ocean teal (#108474) meets bare-wood warmth on a nearly white canvas — the first thing you notice on Woodcessories' storefront is how seriously it takes negative space, letting product photography of walnut-grain cases and cork AirPods sleeves breathe against expanses of #f8f8f8 and #fafafa. The primary teal functions as the single confidence color: add-to-cart buttons, sustainability badges, and trust-bar icons all pull from the same hue, creating a visual throughline that says "this purchase is a good-for-the-planet decision" without ever resorting to cliché leaf graphics. A flash of signal yellow (#ffd602) punctuates sale callouts, urgency labels, and rating stars — it is deliberately sparingly deployed so it reads as sunlight on wood rather than retail noise. Typography pairs Heldane Display in its Medium and Italic cuts for editorial headlines — product-story modules, sustainability manifestos, material deep-dives — with Figtree and Avenir Next sharing body and UI duty. Heldane's high-contrast serifs at large sizes (`{typography.display-xl}`) bring a craft-magazine authority, while Figtree at `{typography.body-md}` keeps navigation and product specs feeling modern and unpretentious. Corners sit at `{rounded.sm}` to `{rounded.md}` for cards and inputs, never fully pill-shaped except on filter chips and small icon badges (`{rounded.full}`); the geometry mirrors the chamfered edges of their real-world cases. The ink tone (#191919) is not true black — a concession to the natural-material ethos that avoids harsh contrast against the pale canvas. A secondary palette of blue-slate (#557a95, #5487a0) surfaces in informational modules: material comparisons, compatibility charts, and eco-impact counters. Red (#de2a2a) is strictly reserved for error states and low-stock warnings, never for branding. Spacing is generous — section gaps of `{spacing.section}` or wider give each product story room, reinforcing the editorial, almost lookbook quality that distinguishes Woodcessories from commodity-accessory competitors.

colors:
  primary: "#108474"
  primary-active: "#0c6b5e"
  primary-disabled: "#a3d5cd"
  accent-yellow: "#ffd602"
  accent-yellow-active: "#e6c102"
  accent-cyan: "#13dede"
  info-slate: "#557a95"
  info-slate-deep: "#5487a0"
  success: "#008b10"
  error: "#de2a2a"
  ink: "#191919"
  ink-warm: "#230d0d"
  body: "#545454"
  muted: "#7b7b7b"
  muted-soft: "#6c6c6c"
  hairline: "#dadada"
  hairline-soft: "#e7e7e7"
  border-light: "#eaeceb"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-warm: "#f9fafb"
  surface-mid: "#f9f9f9"
  surface-card: "#ffffff"
  surface-muted: "#f3f3f3"
  surface-strong: "#eeeeee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  dark-ui: "#343a3f"

typography:
  display-xl:
    fontFamily: "'Heldane Display Medium', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Heldane Display Medium', Georgia, serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.17
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Heldane Display Medium', Georgia, serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.21
    letterSpacing: -0.2px
  display-editorial:
    fontFamily: "'Heldane Display Italic', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
    fontStyle: italic
  display-regular:
    fontFamily: "'Heldane Display Regular', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Figtree', 'Avenir Next', -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  body-lg:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  nav-link-active:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.4px
    textTransform: uppercase
  eco-label:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.1px
  price:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: 0
  price-compare:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 0
    textDecoration: line-through
  link:
    fontFamily: "'Figtree', 'Avenir Next', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    transition: background-color 0.2s ease
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 1
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 1.5px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 1.5px solid {colors.ink}
  button-accent:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-yellow-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: 1px solid {colors.primary}
    boxShadow: 0 0 0 1px {colors.primary}
  text-input-error:
    border: 1px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.border-light}
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: 0 1px 4px rgba(0,0,0,0.06)
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 0
    overflow: hidden
    imageAspectRatio: 1 / 1
    imageBackgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    comparePriceTypography: "{typography.price-compare}"
    bodyPadding: "{spacing.base} {spacing.base} {spacing.lg}"
  product-card-hover:
    boxShadow: 0 4px 16px rgba(0,0,0,0.08)
    transform: translateY(-2px)
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-lg}"
    ctaComponent: button-primary
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    contentMaxWidth: 540px
    imagePosition: right
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-editorial}"
    bodyTypography: "{typography.body-lg}"
    padding: "{spacing.section-lg} {spacing.xl}"
  sustainability-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    iconSize: 14px
  sustainability-badge-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.eco-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    border: 1px solid {colors.primary}
  sale-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  low-stock-badge:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  material-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: 1px solid {colors.hairline}
  material-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: 1px solid {colors.primary}
  color-swatch:
    rounded: "{rounded.full}"
    height: 28px
    width: 28px
    border: 2px solid {colors.hairline-soft}
  color-swatch-active:
    rounded: "{rounded.full}"
    height: 28px
    width: 28px
    border: 2px solid {colors.ink}
  eco-impact-counter:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    numberTypography: "{typography.display-lg}"
    labelTypography: "{typography.caption}"
    numberColor: "{colors.primary}"
  trust-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    iconColor: "{colors.primary}"
    iconSize: 24px
    height: 48px
    gap: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    iconColor: "{colors.muted}"
    placeholderColor: "{colors.muted}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: 1px solid {colors.primary}
    boxShadow: 0 0 0 1px {colors.primary}
  dropdown-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} 0"
    boxShadow: 0 4px 24px rgba(0,0,0,0.12)
    itemPadding: "{spacing.sm} {spacing.base}"
  dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.xxl}"
    boxShadow: 0 8px 32px rgba(0,0,0,0.1)
    borderTop: 1px solid {colors.border-light}
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
    dividerColor: "{colors.dark-ui}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    padding: 0 {spacing.base}
  material-info-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.border-light}
    iconSize: 40px
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
  compatibility-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headerTypography: "{typography.caption}"
    cellTypography: "{typography.body-sm}"
    headerBackgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline-soft}"
    rounded: "{rounded.sm}"
    cellPadding: "{spacing.md} {spacing.base}"
  image-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    thumbnailSize: 64px
    thumbnailRounded: "{rounded.xs}"
    thumbnailBorder: 2px solid transparent
    thumbnailActiveBorder: 2px solid {colors.ink}
    gap: "{spacing.sm}"
  rating-stars:
    filledColor: "{colors.accent-yellow}"
    emptyColor: "{colors.hairline}"
    size: 16px
    gap: 2px

---

## Components

### Buttons

**`button-primary`** — A solid teal (#108474) rectangle with `{rounded.sm}` corners, white text set in `{typography.button-md}`. On hover, the background deepens to #0c6b5e (`button-primary-active`). The disabled state fades to a muted mint (#a3d5cd) while keeping white text — the shape remains recognizable but clearly de-emphasized. Used for all conversion-critical actions: "Add to Cart," "Buy Now," newsletter subscribe.

**`button-secondary`** — White fill with a 1.5px dark border and `{typography.button-md}` text in `{colors.ink}`. On hover the fill shifts to `{colors.surface-soft}`. This is the companion CTA for actions like "Learn More," "View Details," or "Compare Materials" — always next to a primary button, never alone as the main action.

**`button-accent`** — Signal-yellow (#ffd602) fill with dark ink text, reserved strictly for time-sensitive promotions, flash-sale CTAs, or seasonal campaign heroes. The yellow darkens to #e6c102 on hover. Deployed sparingly to maintain its urgency value.

### Form Inputs

**`text-input`** — A 48px-tall field with `{rounded.sm}` corners, a subtle 1px `{colors.hairline}` border, and `{typography.body-md}` text. On focus, the border snaps to `{colors.primary}` teal with a matching 1px outer ring. Error state swaps the border to `{colors.error}` red. Placeholder text uses `{colors.muted}`.

### Navigation

**`nav-bar`** — A clean white bar at 64px height with a single-pixel `{colors.border-light}` bottom edge. Logo sits left, navigation links in `{typography.nav-link}` are center or left-aligned, and cart/search icons anchor right. On scroll, the bottom border is replaced by a soft box-shadow (`nav-bar-scrolled`), giving the impression of the bar lifting off the content beneath it.

**`mega-menu`** — Drops below the nav with a full-width white panel, organized into columns with `{typography.title-sm}` headings and `{typography.body-sm}` links. Product category images sit alongside text links. A `{colors.border-light}` top border anchors it to the nav bar, and a generous 32px box-shadow creates depth.

**`announcement-bar`** — A 40px teal strip above the nav bar, typically promoting free shipping thresholds or sustainability milestones. White text in `{typography.caption}`, sometimes with a dismiss icon.

### Product Card

**`product-card`** — A `{rounded.md}` container with a square product image on a `{colors.surface-soft}` background at top, product title in `{typography.title-sm}`, and price in `{typography.price}` below. Sustainability badges and material chips can overlay the bottom-left of the image area. On hover, the card lifts with `translateY(-2px)` and gains a soft shadow. Compare prices appear in `{typography.price-compare}` with a line-through. The card body has `{spacing.base}` horizontal and `{spacing.lg}` bottom padding.

### Badges & Chips

**`sustainability-badge`** — Small teal rectangle with `{rounded.xs}` corners, white uppercase text in `{typography.badge}`, and a leaf or tree icon at 14px. Used on product cards and detail pages to denote "CO₂ Neutral," "Made from Wood," or "Plastic-Free Packaging."

**`sustainability-badge-outline`** — Same shape but transparent fill with a teal border, used in product detail sidebars where the solid badge would be too heavy.

**`sale-badge`** — Yellow fill with dark text, same `{typography.badge}` sizing. Appears on product card image overlays for active promotions.

**`low-stock-badge`** — Red (#de2a2a) fill with white text. Only appears when inventory is critically low — never as a general urgency tactic.

**`material-chip`** — Pill-shaped (`{rounded.full}`) with a hairline border, used in product filters to let shoppers select Wood, Cork, Stone, or Bamboo. The active state fills with teal and switches text to white.

### Color & Variant Selectors

**`color-swatch`** — A 28px circle with a light border, representing case color options. Active state swaps to a dark `{colors.ink}` border. Swatches are always paired with a text label in `{typography.caption}` below or beside them.

### Eco-Impact Counter

**`eco-impact-counter`** — A `{rounded.md}` card on `{colors.surface-warm}` showing a large teal number in `{typography.display-lg}` (e.g., "1,240,000") with a caption like "Trees Planted" in `{typography.caption}`. Used in the homepage sustainability section and footer. The number color explicitly uses `{colors.primary}` to tie the metric back to brand identity.

### Trust Bar

**`trust-bar`** — A horizontal strip at 48px height on `{colors.surface-soft}`, repeating three to five trust signals ("Free Shipping," "FSC Certified," "CO₂ Neutral Shipping") with 24px teal icons and `{typography.caption}` text. Sits below the hero or above the footer.

### Search

**`search-bar`** — A pill-shaped (`{rounded.full}`) input on `{colors.surface-soft}` with a muted search icon and placeholder. On focus, the background lightens to white with a teal border ring. Used in the nav bar on desktop and as a full-width overlay on mobile.

### Product Detail

**`image-gallery`** — Primary image in a `{rounded.md}` container on `{colors.surface-soft}`, with a row of 64px thumbnails below. Active thumbnail gets a 2px `{colors.ink}` border; inactive thumbnails have transparent borders. Smooth scroll or click navigation between images.

**`compatibility-table`** — Displays device compatibility (iPhone models, iPad models) in a clean table with a `{colors.surface-soft}` header row, `{typography.caption}` column headings, and `{typography.body-sm}` cell content. Rounded at `{rounded.sm}` with `{colors.hairline-soft}` cell borders.

**`material-info-card`** — Bordered card (`{colors.border-light}`) with a 40px material icon (wood grain, cork texture), a `{typography.title-sm}` heading ("Real Walnut Wood"), and `{typography.body-sm}` description. Used in a grid on product pages to explain material properties.

### Rating Stars

**`rating-stars`** — Yellow (#ffd602) filled stars at 16px with 2px gaps. Empty stars use `{colors.hairline}`. Always accompanied by a review count in `{typography.caption}`.

### Footer

**`footer`** — Dark (`{colors.ink}`) background with white headings and lighter gray links. Organized in a multi-column grid with `{typography.title-sm}` section headings ("Products," "Sustainability," "Support") and `{typography.body-sm}` links. Dividers use `{colors.dark-ui}`. Sustainability certifications and payment icons sit at the bottom with generous `{spacing.section}` vertical padding.

### Dropdown

**`dropdown-menu`** — White panel with `{rounded.sm}` corners and a 24px shadow. Menu items use `{typography.body-sm}` with `{spacing.sm}` vertical / `{spacing.base}` horizontal padding. Hover state fills the row with `{colors.surface-soft}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces top nav links, hero image stacks above copy, mega-menu becomes full-screen accordion, search bar is icon-only (expands on tap), trust bar scrolls horizontally, footer columns stack vertically, image gallery uses swipe carousel |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but mega-menu narrows, hero uses 50/50 text-image split, eco-impact counters shift from row to 2×2 grid, footer uses two-column layout |
| Desktop | 1128–1440px | Three- or four-column product grid, full mega-menu on hover, hero at designed proportions, all trust-bar items visible without scroll, image gallery shows thumbnails in a vertical strip beside the main image |
| Wide | > 1440px | Content max-width caps at 1440px and centers on canvas, product grid stays at four columns with increased card padding, hero image scales but copy area remains fixed-width at 540px |

### Touch Targets

- All interactive elements maintain a minimum 44×44px tap area on mobile and tablet
- Color swatches expand to 36px on touch devices with increased gap spacing
- Material chips increase vertical padding to 10px on mobile for comfortable thumb tapping
- Dropdown menu items increase to 48px row height on touch devices
- Close/dismiss icons on modals and drawers use a 48×48px hit zone

### Collapsing Strategy

- Navigation collapses into a slide-out drawer from the left with full-height white panel, category headings as expandable accordions
- Product filters move from a sidebar to a bottom sheet (mobile) or slide-out drawer (tablet)
- Footer columns collapse into expandable sections with `{typography.title-sm}` headers and a chevron icon
- Compatibility tables scroll horizontally with a fade-out edge indicator when content overflows
- Eco-impact counter row wraps to a stacked layout, each counter taking full width with a `{colors.border-light}` separator between items
- Material info cards shift from a 3-column grid to a vertical stack with reduced padding

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font weights and size scales for Heldane Display cuts could not be confirmed from extraction — the three variants (Regular, Medium, Italic) were detected by font-family declaration but precise usage mapping (which headings use which cut) may differ from what is specified here
- Avenir Next and Figtree both appear in font stacks; the division of labor between them (which is primary body, which is fallback) could not be determined from CSS extraction alone — they are listed together in stacks here
- No CSS custom properties or design-token variable names were extractable; Shopify likely loads these through theme settings or JavaScript
- Exact box-shadow values on product cards and navigation are estimated from visual inspection conventions, not extracted values
- Transition timing functions and animation curves (e.g., add-to-cart confirmation, image gallery transitions) were not captured
- The JudgemeStar font detected in extraction is a review-widget icon font, not a brand typeface — it is excluded from the typography system
- Mobile breakpoint behavior is inferred from Shopify Dawn/standard theme conventions; actual breakpoints may differ
- Dark-mode styles, if any exist, were not detected in the extraction
