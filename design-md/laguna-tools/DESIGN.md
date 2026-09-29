---
version: alpha
name: "Laguna Tools"
source_url: "https://www.lagunatools.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Laguna (Condensed), the brand's proprietary compressed sans-serif, does the work that stock fonts cannot — every machine category header, hero callout, and model designation carries it, immediately separating Laguna Tools from the distributors and resellers that share the same SKUs. The palette anchors on a deep navy (#141b38) for the primary navigation and hero backgrounds, drops to a confident process blue (#0068a0) for every interactive CTA, and uses a warm near-black (#231f20) for body copy that reads as letterpress ink rather than screen emission. Red travels in two registers: a muted burgundy (#841919) flags clearance and sale conditions, while a harder #aa0000 handles urgent promotional copy and error states. A light lavender tint on the canvas — #fcfbfe as the page base, #e9e6ed as the soft surface for alternating table rows — suggests showroom lighting rather than factory concrete, softening what would otherwise be an entirely industrial system. Amber (#ffba00, #fbb040) appears specifically in financing callouts and price-tag badges, borrowing the physical urgency of a sale sticker without designing a dedicated component. Corner radii are deliberately restrained throughout — {rounded.xs} on buttons and cards, {rounded.sm} only when grouping requires visual softness — signaling the precision tolerances that buyers of CNC routers and laser cutters expect from the machines themselves. Spec tables are the dominant PDP content pattern: 12px uppercase Open Sans labels in #69727d alternate against 14px regular values in #231f20, rows striped with the lavender surface, giving technical buyers a scan path that mirrors printed machine catalogs. Font Awesome 5 carries all iconography — chevrons, phone glyphs, social brand marks — keeping the component count low and load times fast across spec-heavy product pages that routinely run past 3,000 words. The two-tier header (a 36px utility bar in #2c324c above the 60px primary navy nav) indexes the site on a B2B purchasing convention, signaling that dealers, service technicians, and procurement managers are first-class users alongside direct buyers.

colors:
  primary: "#0068a0"
  primary-active: "#1e85be"
  primary-disabled: "#2ea2cc"
  ink: "#231f20"
  body: "#3c3c3c"
  muted: "#69727d"
  muted-soft: "#767676"
  hairline: "#d3d3d3"
  hairline-soft: "#eeeeee"
  canvas: "#fcfbfe"
  surface-soft: "#e9e6ed"
  surface-card: "#ffffff"
  surface-warm: "#e3ddd8"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  dark-bg: "#141b38"
  dark-mid: "#2c324c"
  slate: "#434960"
  dark-body: "#1f2124"
  dark-ink: "#111111"
  accent-red: "#841919"
  sale-red: "#aa0000"
  alert-bg: "#fceded"
  error: "#ed1024"
  promo-amber: "#ffba00"
  promo-orange: "#fbb040"
  success: "#008a20"

typography:
  display-xl:
    fontFamily: "'Laguna (Condensed)', 'Laguna', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Laguna (Condensed)', 'Laguna', 'Open Sans', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Laguna (Condensed)', 'Laguna', 'Open Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Laguna', 'Open Sans', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Laguna', 'Open Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Laguna', 'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Roboto, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Roboto, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm-bold:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0.3px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  price:
    fontFamily: "'Laguna', 'Open Sans', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Laguna', 'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Laguna', 'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Laguna', 'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  utility-link:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
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
    padding: 12px 24px
    height: 44px
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-dark:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-sm-outline:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.hairline-soft}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    focusBorder: "2px solid {colors.primary}"
    placeholderColor: "{colors.muted-soft}"
  nav-top-utility:
    backgroundColor: "{colors.dark-mid}"
    textColor: "{colors.on-dark}"
    typography: "{typography.utility-link}"
    height: 36px
    linkColor: "{colors.hairline-soft}"
  nav-bar:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    activeUnderlineColor: "{colors.primary}"
    dropdownBg: "{colors.dark-mid}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    height: 48px
    iconColor: "{colors.primary}"
    placeholderColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    hoverBorderColor: "{colors.primary}"
    hoverShadow: "0 4px 12px rgba(0,0,0,0.12)"
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-promo:
    backgroundColor: "{colors.promo-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-instock:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  hero-banner:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    overlay: "linear-gradient(to right, {colors.dark-bg} 55%, transparent 100%)"
    padding: "{spacing.section} 0"
    minHeight: 480px
  category-tile:
    backgroundColor: "{colors.dark-mid}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    border: "1px solid {colors.slate}"
    rounded: "{rounded.none}"
    hoverBorder: "2px solid {colors.primary}"
    hoverBg: "{colors.dark-bg}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    rowBorder: "1px solid {colors.hairline-soft}"
    altRowBg: "{colors.surface-soft}"
    headerBg: "{colors.dark-bg}"
    headerColor: "{colors.on-dark}"
  financing-callout:
    backgroundColor: "{colors.promo-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-bold}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    iconColor: "{colors.dark-body}"
  price-display:
    saleColor: "{colors.sale-red}"
    regularColor: "{colors.ink}"
    strikeThroughColor: "{colors.muted}"
    typography: "{typography.price}"
    saveBadge: "{colors.sale-red}"
  alert-banner:
    backgroundColor: "{colors.alert-bg}"
    textColor: "{colors.accent-red}"
    border: "1px solid {colors.accent-red}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    linkHoverColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.dark-ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline-soft}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    borderTop: "3px solid {colors.primary}"
    mutedColor: "{colors.muted-soft}"

## Components

### Buttons

**`button-primary`** — Uppercase "Laguna" typeface at 15px/700 on a solid #0068a0 background, 4px corners ({rounded.xs}), 44px tall with 24px horizontal padding. Hover shifts to #1e85be ({colors.primary-active}), confirming interaction without a brightness jump. Disabled state uses #2ea2cc at 60% opacity. This is the canonical "Add to Cart," "Request Quote," and "View Details" action across every product context.

**`button-secondary`** — Transparent fill, 2px #0068a0 border, matching blue text in the same uppercase Laguna treatment. Hover floods the interior with the primary blue and inverts to white text — no border animation. Used for "Compare," "Learn More," and secondary PDP actions that share a row with the primary CTA.

**`button-dark`** — Deep navy (#141b38) fill for CTAs embedded inside hero banners and dark-section backgrounds where the blue primary would disappear into the canvas. Same uppercase Laguna type, white text. Common on category landing pages below the hero.

**`button-sale`** — #aa0000 red fill with the same uppercase Laguna/700 treatment. Reserved for clearance category CTAs and flash-sale interstitials. Never appears alongside button-primary on the same element.

**`button-sm-outline`** — 36px hairline-bordered ghost button in white text, used on dark backgrounds for secondary utility actions like "Download Spec Sheet" or "Find a Dealer." Smaller footprint than button-secondary; stays subordinate to the primary CTA.

### Navigation

**`nav-top-utility`** — A 36px strip in #2c324c sits above the main nav, carrying phone numbers, account links, dealer locators, and cart in 13px Open Sans. Font Awesome phone and user-circle icons precede each label. This two-tier pattern signals B2B purchasing infrastructure to machine buyers who expect a direct sales line.

**`nav-bar`** — 60px primary navigation in #141b38. Category labels ("CNC Routers," "Laser Cutters," "Woodworking," "Metalworking") set in "Laguna" 14px/600. Dropdowns reveal {category-tile}-style mega-menu panels in {colors.dark-mid}. Active items receive a 2px #0068a0 underline. No visible bottom border — the navy-to-canvas contrast does the work.

**`search-bar`** — 48px tall, 2px solid #0068a0 border at rest (not only on focus), Font Awesome search icon right-aligned in #0068a0. White interior, 14px Open Sans placeholder in #69727d, 4px radius. The always-on blue border signals that search is the primary discovery path for a 500+ SKU catalog.

### Product Card

**`product-card`** — White card with 1px #d3d3d3 border at rest; hover elevates to a 2px #0068a0 border and a 12px shadow. Product image fills the top third at 4:3 ratio. Below: title in "Laguna" 16px/600, price in "Laguna" 24px/700. A short spec summary (horsepower, table size, spindle speed) renders in 12px uppercase Open Sans ({typography.spec-label}) at #69727d. Sale ({badge-sale}), New ({badge-new}), and Promo ({badge-promo}) badges stack vertically on the image's top-left corner.

### Hero Banner

**`hero-banner`** — Full-width section in #141b38 with a left-to-right gradient overlay that holds text opacity at left and fades to transparent at 55%, letting machine photography bleed to the right edge. Display headline in Laguna (Condensed) at 48px/700 ({typography.display-xl}); subhead at 28px/700 ({typography.display-md}); body copy at 16px Open Sans. Primary CTA uses {button-primary} or {button-dark} depending on proximity to the photography bleed. Minimum 480px tall; padding is {spacing.section} (64px) on the vertical axis.

### Category Tiles

**`category-tile`** — Zero-radius blocks in #2c324c with a #434960 border at rest that sharpens to a 2px #0068a0 highlight on hover, with background deepening to #141b38. Category name in "Laguna" 22px/700 in white ({typography.display-sm}); descriptor line in 14px Open Sans. Arranged in a 4-column grid on desktop, tiling the full content width without gutters — butted edges create a paneled catalog look.

### Spec Table

**`spec-table`** — Two-column table dominating PDP layouts. Column-one labels in 12px uppercase Open Sans, 0.8px letter-spacing, #69727d ({typography.spec-label}). Column-two values in 14px Open Sans regular, #231f20. Alternating rows use the lavender surface (#e9e6ed) against the canvas (#fcfbfe) for scan contrast without ruled borders. Table header row uses a full-width #141b38 band with white "Laguna" 16px/600 for section groupings like "Motor Specs" and "Table Dimensions."

### Financing Callout

**`financing-callout`** — Amber #ffba00 strip at 14px Open Sans 700, sitting directly below the price display on every PDP. Carries "As low as $X/month with financing" with a Font Awesome credit-card icon. The warm yellow reads immediately as a price-tag convention, registering before the text is processed. No border; radius stays at {rounded.xs}.

### Price Display

**`price-display`** — Sale price in #aa0000 at 24px Laguna/700; crossed-out regular price in #69727d at 18px with line-through decoration. Non-sale prices render in #231f20 at the same 24px scale. "Save $X" renders inline as a {badge-sale} chip. The {financing-callout} strip attaches directly below when monthly payment terms are available.

### Badges

**`badge-sale`** — Solid #aa0000, uppercase 12px Open Sans/700, 4px radius, 3px×8px padding. **`badge-new`** — Navy #141b38 fill, same type treatment. **`badge-promo`** — Amber #ffba00 fill, {colors.ink} text for contrast. **`badge-instock`** — Success green #008a20, white text. All four pin to the image top-left and stack vertically when multiple conditions apply simultaneously; DOM order determines badge priority.

### Alert Banner

**`alert-banner`** — Light red (#fceded) background, #841919 border and text, used for out-of-stock notices, long lead-time warnings, and LTL freight shipping disclosures that appear on heavy CNC and bandsaw product pages. Full-width inside the content column, 14px Open Sans, {rounded.xs}, {spacing.md} top/bottom and {spacing.base} left/right padding.

### Breadcrumb

**`breadcrumb`** — 13px Open Sans in #69727d with #d3d3d3 slash separators. The active (current page) segment renders in #231f20 without an underline. Preceding segments are linked and underline on hover in #0068a0. Appears below the primary nav and above the page hero on all category and product pages — essential wayfinding in a deep catalog hierarchy.

### Footer

**`footer`** — Near-black (#111111) base with a 3px solid #0068a0 top rule acting as the brand closing mark. Section headings in "Laguna" 16px/600, white. Link columns in 14px Open Sans at #eeeeee. Typical columns: Products, Accessories, Support, About Laguna, Dealers. A bottom bar carries social icons (Font Awesome Brands), copyright, and legal links in 13px Open Sans at #767676. Newsletter input uses the {text-input} component with a {button-primary} inline submit.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category tiles stack to 1-up; nav collapses to hamburger in {colors.dark-bg} bar; hero scales to {typography.display-md} (28px) with image stacked above text; spec tables scroll horizontally; footer collapses to accordion |
| Tablet | 744–1128px | 2-column product grid; category tiles 2-up; hero retains side-by-side split with reduced overlay width; primary nav shows top-level categories only, secondary into overflow drawer |
| Desktop | 1128–1440px | 3–4 column product grid; full mega-menu with {category-tile} panels; hero at full cinematic width with Laguna Condensed {typography.display-xl}; spec table adds a "Notes" column |
| Wide | > 1440px | Content max-width ~1400px centered; hero photography scales but text rail stays fixed left; category tile grid maintains 4 columns with proportional tile growth |

### Touch Targets

- All primary and secondary buttons are minimum 44px tall
- Mobile nav accordion items are minimum 48px tall with {spacing.lg} vertical padding
- Product cards are fully tappable — the entire card surface links to the PDP, not only the title text
- Breadcrumb links extend tap area to 36px height via increased padding rather than font-size increase
- Badge chips are decorative only and do not require independent touch targets

### Collapsing Strategy

- Primary mega-menu collapses to a full-screen dark drawer on mobile, organized by machine category with accordion expansion per subcategory; {nav-top-utility} collapses to a secondary row inside the drawer
- Hero banners reflow from left-text/right-image to image-above/text-below at mobile breakpoint; overlay gradient is removed since there is no bleed composition on single-column
- Spec tables that exceed viewport width receive horizontal scroll within a fixed-height container; column-one labels stay sticky at left so context is never lost while scrolling right
- Footer multi-column grid collapses to single-column accordion: {typography.title-sm} headings become tap targets that reveal link lists below
- {financing-callout} becomes a sticky bottom bar on mobile PDPs, persisting in view as users scroll the spec table — mimics the "always in view" financing strip of physical floor tags

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact weight variants and optical sizes for the "Laguna" and "Laguna (Condensed)" proprietary typefaces could not be confirmed from extraction — it is unclear whether a single weight file or a full VF axis is served; fallback stack (Open Sans → Roboto → Arial) covers rendering in absence
- The extracted color #720eec (vivid purple) context is unconfirmed — it may belong to a live-chat widget, a third-party financing embed, or a limited-run product-line badge; it has been excluded from the brand token set
- #cc3366 (pink-magenta) and #958e09 (olive-gold) were extracted but appear to originate from third-party embeds rather than the Laguna Tools design system proper; excluded from tokens
- Meta theme-color is unset — #141b38 is used as the inferred mobile browser chrome color based on the nav-bar background, but this is not confirmed
- Button, card, and input border-radius values are inferred from the industrial visual language at {rounded.xs} (4px); no CSS custom properties or measured pixel values were extractable
- Hover transition timing (duration, easing) could not be extracted; 150ms ease-in-out is assumed throughout
- Grid gutter widths, column counts, and max-content-width breakpoints are inferred from visual analysis rather than measured from CSS variables or a confirmed design token file
- Whether the site uses a design-token build system (CSS custom properties, Sass variables, Tailwind config) or hand-authored styles is unknown
