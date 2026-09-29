---
version: alpha
name: "Daniel Wellington"
source_url: "https://www.danielwellington.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  DWCaslon — a commissioned editorial serif that reads like the masthead of a 1960s horological journal — carries display copy at weights so light the letterforms appear etched rather than set, while DWFutura handles labels and CTAs with the spare geometry of a watch dial. The result is a site built on a single contrast engine: the near-black #00081c campaign canvases give way to near-white #f4f4f4 product pages where a single watch floats in engineered negative space. This alternation between darkness and its absence is the core DW visual argument — the brand never compromises with midtones, and the midrange grays (#545454, #dedede) exist only to signal disabled states and hairlines.

  The amber-gold accent (#f59e0b) arrives sparingly, as a material reference to the yellow-gold case colorways that built the brand, and always against dark backgrounds where it reads as precious rather than decorative. Forest green (#0d4831) surfaces in a dedicated collection environment — a more saturated visual register against the otherwise achromatic system. Crimson (#c8182d) and blush (#e44458) appear in seasonal colorway chips and sale badges, each mapped to a strap color family rather than distributed freely across the interface.

  Strap-color swatches — `{rounded.full}` chips in camel (#85714d), black, navy (#00081c), and white — are the most distinctively DW UI element: a physical-catalog convention translated to a scrollable row with an active-state ring offset rather than a fill change, so the actual color remains legible under selection. The interchangeable-strap premise that built the brand is legible in every product display: the watch head sits once in a square crop, the swatch row beneath it shows every material permutation, and the add-to-cart block never competes visually with that chooser.

  Corner radii are minimal throughout: `{rounded.xs}` on inputs and badges, `{rounded.sm}` on cards, `{rounded.none}` on hero banners and primary CTAs. The brand's watch cases are perfectly round, but its interface is emphatically rectangular — the circle is reserved for the product, not the shell.

colors:
  primary: "#00081c"
  primary-active: "#141d2b"
  primary-disabled: "#545454"
  accent-gold: "#f59e0b"
  accent-gold-light: "#fbbf24"
  accent-green: "#0d4831"
  accent-green-deep: "#126243"
  accent-green-mint: "#93e2bb"
  accent-crimson: "#c8182d"
  accent-crimson-dark: "#9f0813"
  accent-crimson-mid: "#ab1b36"
  accent-blush: "#e44458"
  accent-blush-light: "#e85f70"
  accent-navy: "#2c436c"
  accent-navy-mid: "#355082"
  strap-camel: "#85714d"
  ink: "#111111"
  body: "#1f1f1f"
  muted: "#545454"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#f0f0f0"
  surface-mid: "#e6e6e6"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'DWCaslon', 'DWCaslonItalic', Georgia, serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'DWCaslon', Georgia, serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'DWCaslon', Georgia, serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'DWCaslon', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'DWFutura', 'BeVietnamPro', Jost, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.08px
  title-sm:
    fontFamily: "'DWFutura', 'BeVietnamPro', Jost, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.06px
  label-caps:
    fontFamily: "'DWFutura', 'BeVietnamPro', Jost, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 1.2px
    textTransform: uppercase
  body-md:
    fontFamily: "'BeVietnamPro', Inter, Jost, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'BeVietnamPro', Inter, Jost, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'BeVietnamPro', Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-caps:
    fontFamily: "'DWFutura', 'BeVietnamPro', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 1.4px
    textTransform: uppercase
  price-display:
    fontFamily: "'DWFutura', 'BeVietnamPro', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'DWFutura', 'BeVietnamPro', Jost, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'DWFutura', 'BeVietnamPro', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'DWFutura', 'BeVietnamPro', Jost, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px

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
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 50px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 15px 31px
    height: 50px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 15px 31px
    height: 50px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    accentColor: "{colors.accent-gold}"
    height: 40px
    padding: "0 {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline-soft}"
    height: 64px
    logoHeight: 28px
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.label-caps}"
    headerColor: "{colors.muted}"
    linkTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"
    columnGap: "{spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1/1"
    padding: "{spacing.base}"
    hoverEffect: "scale(1.02) on image only"
  strap-swatch:
    shape: "{rounded.full}"
    size: 24px
    activeBorder: "2px solid {colors.primary}"
    activeBorderOffset: 2px
    inactiveBorder: "1px solid {colors.hairline}"
    gap: "{spacing.sm}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-caps}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-caps}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-collection:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-caps}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    ctaVariant: button-ghost
    layout: "full-bleed image with text overlay left-aligned"
    minHeight: 600px
  collection-hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    layout: "50/50 split — text left, image right"
    padding: "{spacing.section} 0"
  pdp-price-block:
    priceColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    strikethroughColor: "{colors.muted}"
    saleColor: "{colors.accent-crimson}"
    labelTypography: "{typography.body-sm}"
    gap: "{spacing.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    iconColor: "{colors.muted}"
    height: 44px
  collection-filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.caption}"
    linkColor: "{colors.surface-mid}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.label-caps}"
    headingColor: "{colors.on-primary}"
    columns: 4
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — A sharp-cornered (`{rounded.none}`) dark rectangle in `{colors.primary}` (#00081c) with DWFutura tracking at 1px letter-spacing and uppercase transform; the hard corners are a deliberate counterpoint to the circular watch face at the product's center. Hover state deepens to `{colors.primary-active}` with no softening. Disabled state uses `{colors.primary-disabled}` (#545454) at full opacity — a decisive tonal step rather than a transparency fade.

**`button-secondary`** — Same `{rounded.none}` geometry as primary, canvas fill with a 1px `{colors.primary}` border; used for secondary CTAs on product detail pages ("Add to Wishlist" alongside the primary "Add to Cart"). Active state fills to `{colors.surface-soft}` to register press without inverting the label color.

**`button-ghost`** — White border and white type on dark backgrounds. Used exclusively within `hero-banner` modules on `{colors.primary}` canvas; never appears on light-background pages where it would vanish.

### Text Input

**`text-input`** — Minimal `{rounded.xs}` border in `{colors.hairline}`, stepping to `{colors.primary}` on focus with no transition animation beyond the instant color swap. Placeholder text in `{colors.muted}` (#545454) clears on first keystroke — no floating-label pattern. Height is 48px across all form contexts, including the newsletter capture in the footer.

### Navigation

**`nav-bar`** — 64px white bar with `{typography.nav-link}` DWFutura links at 0.5px letter-spacing, just enough spacing to signal a fashion-house register. On mobile the DW wordmark centers; on desktop it shifts left with navigation links right. A sticky `announcement-bar` at 40px sits above in `{colors.primary}` with `{colors.accent-gold}` (#f59e0b) accent text for promotional messaging; both bars together span 104px before content begins.

**`nav-mega-menu`** — Full-width dropdown flush to the nav bottom, `{colors.canvas}` background, organized by product category (Watches, Straps, Jewelry, Accessories). Each column opens with a `{typography.label-caps}` header in `{colors.muted}`, followed by `{typography.body-sm}` item links. No images in the mega-menu — it is purely typographic, which keeps the visual weight below the fold.

### Product Card

**`product-card`** — Square 1:1 image on `{colors.surface-soft}` with `{rounded.none}` — zero softening anywhere. Product name in `{typography.title-sm}`, price in `{typography.price-display}` directly below. A `strap-swatch` row of `{rounded.full}` color chips follows immediately, signaling variant availability without requiring any hover interaction. Badge placement is absolutely positioned top-left using `badge-new`, `badge-sale`, or `badge-collection` as appropriate. On hover, only the image scales (1.02×) while the text block remains static.

### Strap Swatch

**`strap-swatch`** — 24px circular chips with a 2px ring-offset border on active rather than a fill inversion, preserving full legibility of the underlying color. Core four: camel (`{colors.strap-camel}` #85714d), black (`{colors.ink}`), navy (`{colors.primary}`), and white (`{colors.canvas}`). Seasonal colorways add crimson (`{colors.accent-crimson}`) and forest green (`{colors.accent-green}`). Chip gap is `{spacing.sm}`; the row is horizontally scrollable on mobile without wrapping.

### Hero Banner

**`hero-banner`** — Full-bleed dark photography with text left-aligned in `{colors.on-primary}`. Heading runs `{typography.display-xl}` DWCaslon at weight 300 — deliberately light for the scale, relying on the serifed letterform rather than stroke weight for presence. CTA is `button-ghost`. Minimum 600px height on desktop; collapses to text-over-image stacked layout on mobile.

### Badges

Three variants share `{rounded.xs}` geometry and `{typography.caption-caps}` (10px, 1.4px tracking, uppercase, all-caps):
- **`badge-new`** — `{colors.primary}` (#00081c) fill for new releases
- **`badge-sale`** — `{colors.accent-crimson}` (#c8182d) fill for marked-down SKUs
- **`badge-collection`** — `{colors.accent-green}` (#0d4831) fill for collection-grouped products (e.g., "Classic Petite," "Iconic Link")

All three sit top-left of the product image, absolutely positioned, and do not appear simultaneously on the same card.

### Collection Filter Pills

**`collection-filter-pill`** — `{rounded.full}` with a hairline border in idle state, inverting to `{colors.primary}` fill and `{colors.on-primary}` text on active. Used in PLP filter bars to select by case material, strap color, or dial. The pill shape is the one place the interface deliberately departs from its otherwise rectangular grammar — the filter context signals "removable selection" and benefits from the roundness.

### Footer

**`footer`** — Full-width `{colors.ink}` (#111111) background, four-column link grid in `{typography.caption}`. Column headers in `{typography.label-caps}` in `{colors.on-primary}`. Link idle color is `{colors.surface-mid}` (#e6e6e6), stepping to `{colors.canvas}` on hover. The DW wordmark appears in white in the bottom strip alongside copyright text and social icon links.

### PDP Price Block

**`pdp-price-block`** — Full price in `{typography.price-display}` at `{colors.ink}`; when on sale, the original price renders in `{colors.muted}` with strikethrough and the sale price in `{colors.accent-crimson}`. Positioned directly below the product name heading, above the strap swatch row, so the price is always visible without scrolling on desktop.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; announcement bar persists above nav; hero stacks text over image; strap swatch row horizontally scrollable; footer collapses to single-column accordion |
| Tablet | 744–1128px | Two-column product grid; mega-menu replaced by slide-in drawer with accordion categories; hero returns to side-by-side layout |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu on nav hover; hero full-bleed at 600px min-height |
| Wide | > 1440px | Grid max-width capped at 1440px with auto side margins; hero image fills viewport width, text container remains 1440px-bound |

### Touch Targets

- All interactive elements minimum 44×44px on mobile
- Strap swatch chips expand tap area to 36px via padding despite 24px visual size
- Filter pills padded to 40px height on mobile
- Nav hamburger icon 44×44px touch area
- Footer accordion headers minimum 48px tall on mobile for comfortable tap

### Collapsing Strategy

- Mega-menu collapses to a full-screen slide-in drawer with tap-to-expand accordion sections per category
- Three-column footer reduces to single-column accordion; column headers become tap-to-expand toggles
- Strap swatch row becomes a horizontal scroll container — never wraps to multi-line
- PDP layout moves the hero image above the purchase block on mobile (image first, then name / price / swatches / CTA stacked)
- Collection hero 50/50 splits collapse to stacked single column, image first

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No shadow or elevation tokens extracted; DW appears to use flat design with no drop shadows on cards, modals, or drawers
- Exact mobile nav-bar height not confirmed from extraction; 56px assumed based on Shopify theme conventions
- DWCaslon and DWFutura are proprietary brand typefaces — their full weight and style axes are not publicly documented; weight 300 for display and 500–600 for UI are inferred from visual inspection rather than confirmed spec
- Inter and Jost appear in the font stack but their specific usage contexts (likely checkout flows or third-party widgets) are not confirmed
- Motion and transition timing tokens not extractable from static color/font analysis
- Precise PLP grid gutter widths and column counts at each breakpoint inferred rather than confirmed
- The forest green token (#0d4831) may be scoped to a single named collection rather than a standing system-wide accent — collection-specific usage not confirmed
- The navy accent cluster (#2c436c, #355082, #141d2b) may correspond to specific strap or dial colorways rather than UI states; usage context uncertain
