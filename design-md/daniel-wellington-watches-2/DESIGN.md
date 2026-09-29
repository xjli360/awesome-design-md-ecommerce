---
version: alpha
name: "Daniel Wellington"
source_url: "https://danielwellington.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  DWCaslon does the work that most watch brands assign to photography — the custom serif's bracketed strokes and classical proportions carry a century's worth of horological authority even at body-copy scale, before a single product image loads. Against a canvas that oscillates between pure white and near-linen off-whites (#f4f4f4, #f0f0f0, #f5f5f5), the near-black navy #00081c anchors wordmarks and primary CTAs with a depth that a flat black cannot replicate. It is a color that reads as midnight water rather than printer ink, and the entire palette calibrates around its gravity. Mid-tone neutrals (#545454, #1f1f1f) handle supporting text at weights that let DWFutura's geometric sans carry the structural load without strain. The muted warm gold #85714d — aged brass rather than bright gilt — marks price points and seasonal badges, tying the digital surface back to the physical case metal.

  Seasonal collection colors break from this austerity in controlled, archival bursts. A deep forest green (#0d4831, #126243) reads like Indian ink; a suite of graduated reds (#91172e, #c8182d, #e31b33) marks sale events with the precision of a red enamel chapter ring; a mint family (#93e2bb, #7bdcac) surfaces limited drops without unsettling the core neutrality. These are campaign registers, not system colors — they appear on banners and collection-entry pages, then yield back to the neutral grid. Button geometry confirms this restraint: filled primaries at `{rounded.none}`, never pill-shaped, because a pill shape signals the casual tech-forward energy that Daniel Wellington has deliberately withheld. The strap configurator — the brand's signature interactive — swaps product imagery in place over a completely still layout with no spring animations. Cart and search overlays darken behind a `{colors.scrim}` field at reduced opacity, as though the transactional layer is simply the editorial catalogue extended one register deeper.

  DWCaslonItalic appears almost exclusively in editorial callouts — campaign headlines, gift-guide splash pages — treating the italic cut as a quotation register rather than an emphasis register. BeVietnamPro and Jost carry utilitarian roles: form labels, filter selectors, stock status indicators, breadcrumbs. The system never mixes the two registers casually; a utility label set in DWCaslonItalic would read as a category error. Letter-spacing on all-caps labels runs at 1–1.5px, giving the geometric sans the optical breathing room it needs without resorting to weight increases. Product cards use `{rounded.xs}` corners — barely perceptible, almost a concession to edge-softening convention rather than a deliberate design choice. The brand trusts stillness, tonal contrast, and proprietary type over motion or personality.

colors:
  primary: "#00081c"
  primary-active: "#141d2b"
  primary-disabled: "#545454"
  ink: "#141414"
  body: "#1f1f1f"
  muted: "#545454"
  hairline: "#dedede"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#f0f0f0"
  surface-strong: "#e2e2e2"
  on-primary: "#ffffff"
  gold: "#85714d"
  forest-green: "#0d4831"
  forest-green-mid: "#126243"
  mint: "#93e2bb"
  mint-light: "#7bdcac"
  sale-red: "#c8182d"
  sale-red-dark: "#91172e"
  sale-red-bright: "#e31b33"
  navy-mid: "#2c436c"
  navy-blue: "#355082"
  amber: "#f59e0b"
  scrim: "#00081c"

typography:
  display-xl:
    fontFamily: "'DWCaslon', Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'DWCaslon', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'DWFutura', 'Jost', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
  display-editorial:
    fontFamily: "'DWCaslonItalic', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.3px
    fontStyle: italic
  title-md:
    fontFamily: "'DWFutura', 'BeVietnamPro', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  title-sm:
    fontFamily: "'DWFutura', 'BeVietnamPro', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  body-md:
    fontFamily: "'BeVietnamPro', 'Jost', Inter, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'BeVietnamPro', 'Jost', Inter, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'BeVietnamPro', 'Jost', Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'DWFutura', 'BeVietnamPro', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'DWFutura', 'BeVietnamPro', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'BeVietnamPro', 'Jost', Inter, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.4px
  label:
    fontFamily: "'BeVietnamPro', 'Jost', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  price-md:
    fontFamily: "'DWFutura', 'Jost', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.3px
  price-lg:
    fontFamily: "'DWFutura', 'Jost', sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge:
    fontFamily: "'BeVietnamPro', 'Jost', Inter, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    rounded: "{rounded.none}"
    padding: "13px 32px"
    height: 44px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "12px 31px"
    height: 44px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "12px 0"
    border: none
    borderBottom: "1px solid {colors.ink}"
  button-sm-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "8px 20px"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
    focusBorderColor: "{colors.primary}"
    errorBorderColor: "{colors.sale-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "10px 14px"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoMaxWidth: 140px
    padding: "0 {spacing.xl}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    letterSpacing: 0.5px
    textAlign: center
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
    boxShadow: "0 8px 24px rgba(0,8,28,0.08)"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageBorderRadius: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-md}"
    captionTypography: "{typography.body-sm}"
    padding: "{spacing.sm}"
    hoverImageScale: 1.04
    transition: "transform 0.35s ease"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-badge-new:
    backgroundColor: "{colors.forest-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-badge-gold:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 560px
    layout: split-50-50
    ctaGap: "{spacing.xl}"
    imageFit: cover
  hero-editorial:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-editorial}"
    subheadTypography: "{typography.body-md}"
    minHeight: 480px
    textAlign: center
  collection-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    descriptionTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  strap-swatch:
    width: 32px
    height: 32px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    activeBorder: "2px solid {colors.primary}"
    gap: "{spacing.sm}"
    transition: "border-color 0.2s ease"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    padding: "10px 16px"
    height: 44px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    headerTypography: "{typography.title-md}"
    itemTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-md}"
    subtotalTypography: "{typography.price-lg}"
    scrimColor: "{colors.scrim}"
    scrimOpacity: 0.4
  search-modal:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    resultTitleTypography: "{typography.title-sm}"
    resultPriceTypography: "{typography.price-md}"
    borderBottom: "1px solid {colors.hairline}"
    scrimColor: "{colors.scrim}"
    scrimOpacity: 0.5
    padding: "{spacing.xl}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
    padding: "8px 16px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0 {spacing.xl}"
    borderTop: none
    linkOpacityHover: 0.7

## Components

### Buttons

**`button-primary`** — Square-cornered (`{rounded.none}`), 44px tall, all-caps DWFutura at 12px with 1.5px letter-spacing. The near-black navy #00081c fill is the CTA across all shopping contexts: add-to-cart, checkout, newsletter submit. On hover the fill shifts to `{colors.primary-active}` (#141d2b), a barely perceptible lightening that signals interactivity without breaking the tonal system. Disabled state desaturates to `{colors.primary-disabled}` (#545454) with pointer events removed.

**`button-secondary`** — White fill with a 1px `{colors.primary}` border and matching navy text; used for secondary actions like "View Details" or "Save for Later" alongside the primary add-to-cart. Mirrors the primary's geometry and typography exactly so the two sit comfortably side by side without competing.

**`button-ghost`** — Transparent background, `{colors.ink}` text, with an underline border-bottom rather than a full outline. Used for soft editorial CTAs ("Explore the Collection", "Learn More") where a bordered or filled button would feel too commercial. No rounded corners; the underline itself is the affordance.

### Text Input & Forms

**`text-input`** — Zero border-radius, 48px height, 1px `{colors.hairline}` border on all sides. Focus shifts the border to `{colors.primary}` — the single interactive highlight in an otherwise muted input chrome. Error state uses `{colors.sale-red}`. Placeholder text in `{colors.muted}` (#545454). Form labels use `{typography.label}` (all-caps, 11px, 1px tracking).

### Navigation

**`nav-bar`** — 64px tall, white background, 1px `{colors.hairline-soft}` bottom border. The DW wordmark sits left at max-width 140px. Center nav links use `{typography.nav-link}` (13px, weight 500) with no underline on hover — instead a subtle opacity drop to 0.7. A cart count badge and currency/region selector anchor the right side. On scroll the bar gains no shadow or color change; it stays flush white.

**`announcement-bar`** — 36px strip above the nav, `{colors.primary}` background, white `{typography.caption}` text centered. Used for free-shipping thresholds, sale countdowns, and new collection alerts. Dismissible via an `×` icon at far right; dismissed state persists via sessionStorage.

**`nav-dropdown`** — Full-width mega-menu panel that drops below the nav on category hover. White background, subtle box-shadow at `0 8px 24px rgba(0,8,28,0.08)`. Category headings in `{typography.title-sm}` (all-caps, 12px, 1.2px tracking); links in `{typography.body-sm}`. Imagery panels — campaign photography or collection thumbnails — occupy the right column at roughly 40% width.

### Product Card

**`product-card`** — No border-radius on the card or image. `{colors.surface-soft}` background behind a full-bleed product image that scales to 1.04× on hover with a 0.35s ease transition — the only animation in the grid. Product name in `{typography.title-sm}` (all-caps, 12px, 1.2px tracking), price in `{typography.price-md}` (DWFutura, 15px). Color/strap variant name appears as a `{typography.caption}` line in `{colors.muted}`. Badges (`product-badge`, `product-badge-sale`, `product-badge-new`) pin to the top-left corner of the image at absolute position.

### Badges

Three distinct badge variants share the same zero-radius geometry and 10px all-caps typography. **`product-badge`** (navy) marks editorial picks or bundles. **`product-badge-sale`** (sale-red #c8182d) fires during promotional events; **`product-badge-new`** (forest-green #0d4831) surfaces recent releases. A gold variant (`product-badge-gold`, #85714d) appears on premium or limited-edition lines. All four are interchangeable in the same slot — only color signals meaning.

### Strap & Size Selectors

**`strap-swatch`** — 32px circular swatches rendered as a color-fill circle with a 2px border that transitions from transparent to `{colors.primary}` on selection. Swatches sit in a horizontal row with `{spacing.sm}` gap; an active selection also triggers the product imagery swap. **`size-selector`** — rectangular chips (zero radius, 1px border) that invert to `{colors.primary}` fill + white text when active. Both selectors drive the product configurator without page reload.

### Cart Drawer

**`cart-drawer`** — 400px panel sliding in from the right, white background, 1px `{colors.hairline}` left border. Header ("Your Bag" or "Cart") in `{typography.title-md}`. Line items use `{typography.body-sm}` for product name and `{typography.price-md}` for unit price. The order subtotal anchors the panel bottom in `{typography.price-lg}`. A `{colors.scrim}` overlay at 40% opacity covers the page content behind the open drawer.

### Hero Modules

**`hero`** — Split 50/50 layout on desktop: product or lifestyle photography on one half, headline + body copy + CTA stack on the other. `{colors.surface-soft}` (#f4f4f4) fills the copy panel; imagery bleeds to the panel edge with no padding. Headline in `{typography.display-xl}` (DWCaslon, 56px). **`hero-editorial`** — full-bleed dark module with `{colors.primary}` (#00081c) background and a `{typography.display-editorial}` headline (DWCaslonItalic, 48px italic) centered over campaign photography at reduced opacity. Used for seasonal campaign launches.

### Footer

**`footer`** — Full-width `{colors.primary}` (#00081c) panel. Column headings in `{typography.title-sm}` (all-caps white). Links in `{typography.body-sm}` at full white opacity, dropping to 0.7 on hover. Social icons render as minimal SVG strokes in white. Country/language selector sits in a bottom sub-footer row alongside legal links in `{typography.caption}`.

### Search Modal

**`search-modal`** — Triggered by a magnifier icon in the nav. Drops a full-width panel below the announcement bar with a large text input (no border-radius, 1px bottom border in `{colors.hairline}`). Instant results appear in a two-column grid: product image thumbnail + title in `{typography.title-sm}` + price in `{typography.price-md}`. The scrim behind uses `{colors.scrim}` at 50% opacity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + slide-in drawer; hero shifts to stacked layout (image top, copy below); cart drawer expands to full viewport width; announcement bar text truncates with marquee scroll |
| Tablet | 744–1128px | Two-column product grid; mega-menu condenses to accordion; hero remains split but copy column narrows; filter sidebar collapses to a top filter bar with horizontal scroll chips |
| Desktop | 1128–1440px | Three-to-four column product grid; full mega-menu with image panel; hero at minimum 560px height; cart drawer at fixed 400px |
| Wide | > 1440px | Content max-width locked at 1440px with symmetric margin auto; hero image panels fill edge-to-edge outside the content column; footer columns redistribute to five-column layout |

### Touch Targets

- All interactive elements (swatches, size chips, icon buttons) minimum 44×44px touch target even if visually smaller
- Strap swatches (32px visual) receive 6px transparent padding to meet minimum
- Filter chips maintain 44px height on mobile
- Cart icon and nav links in mobile drawer at 48px tap height

### Collapsing Strategy

- Mega-menu collapses to full-screen slide-in nav with accordion category expansion on mobile
- Product filter sidebar hides behind a "Filter & Sort" bottom sheet on mobile and tablet
- Hero split layout stacks vertically on mobile with image first, copy panel below at `{spacing.xxl}` padding
- Footer column layout collapses from five columns → three → single stacked list as viewport narrows
- Announcement bar: single message visible; multiple messages rotate via CSS animation on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed border-radius value for the product image carousel or modal overlays — `{rounded.none}` used as the system default based on overall sharp-corner aesthetic
- Amber/gold values (#f59e0b, #fbbf24) appear in the extraction but their specific use contexts (star ratings, promotional timers, or watch imagery overlays) could not be confirmed; `{colors.gold}` (#85714d) used as the primary brand gold with these as possible accent-only values
- Navy-blue family (#2c436c, #355082, #141d2b) extracted but specific assignment (gift-box UI, loyalty tier, map components) is unclear — included as named tokens but not assigned to primary components
- DWCaslon and DWFutura are proprietary typefaces; exact weight axes (if variable font), fallback rendering behavior, and whether DWCaslonItalic is a separate file or axis value are not publicly documented
- Product configurator interaction model (strap builder, case/dial combinator) — animation curves, transition timing, and whether it uses a canvas or DOM-swap approach — not extractable from static site analysis
- Exact hover state for nav links (opacity drop value, underline variant, or color change) not confirmed; 0.7 opacity used as reasonable default
