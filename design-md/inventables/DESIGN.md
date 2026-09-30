---
version: alpha
name: "Inventables"
source_url: "https://www.inventables.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The amber voltage of #fea609 punches through near-black surfaces the way a laser trace glows across raw acrylic — and that contrast is the entire visual argument Inventables makes. Four near-identical dark backgrounds (#272929, #1a1d1d, #1d1d1d, #121212) serve distinct depth roles across the interface: the deepest pools anchor the global nav and footer, midrange darks carry product spec panels and feature callouts, and the amber family (#ffa400, #fea245, #ffb762) provides three tonal stops that handle hover states, pricing accents, and bundle badge highlights without introducing a second hue. Nothing here is accidental — the brand sells precision machines to people who think in thousandths of an inch, and the color system reflects that discipline.

  AlrightSans runs the full typographic load across ten declared weights. Inventables uses the spread intentionally: ExtraThin handles spec annotations and dimensional whisper labels, Light carries extended body copy, Medium anchors navigation and form inputs, and Bold drives CTAs and product headings at the density required by a SKU-heavy catalog. The near-geometric letterforms carry a mechanical quality in uppercase — that setting mirrors a G-code comment block rather than a lifestyle editorial, and buttons are set in tracked Bold uppercase to reinforce that precision-tool register at every action point.

  Rounded corners stay deliberately tight — {rounded.sm} on buttons and inputs, near-square on product cards — echoing CNC path geometry rather than the bubble radii of consumer apps. The interface does not soften itself for lifestyle appeal: this is a maker's toolkit mapped onto a commerce layer, and every design decision signals competence to the professional buyer scanning machine specs. Dark-surface hero and callout sections carry the brand's visual weight, with amber CTAs providing the single primary contrast event per screen. Light-canvas product pages use #dedede and #eeeeee for grid dividers and disabled states, keeping the industrial palette intact without overwhelming material photography. FontAwesome handles all iconography at nav, badge, and inline documentation scales, keeping glyph rendering consistent across the machine-spec-heavy content that defines the Inventables catalog.

colors:
  primary: "#fea609"
  primary-active: "#d48500"
  primary-disabled: "#ffb762"
  amber-alt: "#ffa400"
  amber-warm: "#fea245"
  ink: "#121212"
  body: "#272929"
  muted: "#1a1d1d"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  surface-dark: "#272929"
  surface-mid: "#1a1d1d"
  surface-darkest: "#121212"
  on-primary: "#121212"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'AlrightSans-Bold', Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'AlrightSans-Bold', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'AlrightSans-Medium', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'AlrightSans-Medium', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'AlrightSans-Medium', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'AlrightSans-Regular', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'AlrightSans-Light', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'AlrightSans-Regular', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'AlrightSans-ExtraThin', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 100
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'AlrightSans-Bold', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'AlrightSans-Medium', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'AlrightSans-Medium', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  price-display:
    fontFamily: "'AlrightSans-Bold', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  tag-label:
    fontFamily: "'AlrightSans-Bold', Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 28px
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
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.5
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  button-dark:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.on-dark}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: none
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspect: "1/1"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
  hero-dark:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    minHeight: 540px
    paddingVertical: "{spacing.section}"
  machine-spec-table:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    rowBorder: "1px solid {colors.muted}"
    padding: "{spacing.base}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-bundle:
    backgroundColor: "{colors.amber-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    iconColor: "{colors.body}"
    height: 44px
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    dividerColor: "{colors.muted}"
    padding: "{spacing.xxl}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    buttonBackgroundColor: "{colors.surface-soft}"
    height: 44px
  material-swatch:
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    size: 36px

## Components

### Buttons

**`button-primary`** — Amber (#fea609) fill with near-black text ({colors.on-primary}), set in tracked uppercase AlrightSans-Bold at 14px and 44px tall. Hover deepens to {colors.primary-active} (#d48500); disabled applies {colors.primary-disabled} at reduced opacity. This is the only warm-fill button in the system — every primary CTA on dark and light surfaces resolves here.

**`button-secondary`** — Transparent background with a 2px amber border and amber text, mirroring the primary palette without filling a surface. Used for secondary CTAs alongside `button-primary` on product pages, giving the pairing an outlined/filled contrast that reads clearly against the white canvas.

**`button-dark`** — Near-black fill ({colors.surface-darkest}) with white text, used in dark-surface hero and feature callout sections where an amber button would create over-saturated contrast. Pairs with `button-ghost` for primary/secondary hierarchies inside dark bands.

**`button-ghost`** — Transparent with a 1px white border and white text; the secondary action for dark-section layouts. Hover should dim the border opacity rather than change fill color.

### Navigation

**`nav-bar`** — Full-width near-black bar ({colors.surface-darkest}, 60px tall) with white AlrightSans-Medium links. No bottom border creates a seamless visual merge into dark hero sections directly beneath it. Logo sits left; primary category links center or left-cluster; cart and account icons right. On scroll, the bar stays fixed and opaque — the dark background ensures legibility over any hero imagery.

### Product Card

**`product-card`** — White surface with 1px {colors.hairline} border and {rounded.sm} corners, keeping product photography clean and uncontested. Title uses {typography.title-md} in {colors.ink}; price renders in {typography.price-display}, colored {colors.primary} on sale or {colors.ink} at full price. Badge overlays (badge-new, badge-sale) anchor top-left corner at {rounded.xs}.

### Hero

**`hero-dark`** — Full-width near-black band ({colors.surface-darkest}) at 540px minimum height. Display headline in {typography.display-xl} white; body copy in {typography.body-md}. Primary CTA renders as `button-primary` (amber). Vertical padding at {spacing.section} (64px) provides the breathing room needed to convey machine scale. Secondary action uses `button-ghost`.

### Machine Spec Table

**`machine-spec-table`** — Dark surface ({colors.surface-dark}) with {typography.spec-label} labels in tracked uppercase ExtraThin (100 weight) and {typography.body-sm} values in Light weight. Row separators use {colors.muted} (#1a1d1d) for a subtle dark-on-dark division. This is the brand-signature component: precision buyers read spec tables before product descriptions, and the dark treatment gives data the gravitas it requires without competing with product imagery on adjacent panels.

### Badges

**`badge-new`** — Amber fill with near-black uppercase text at 10px tracked, {rounded.xs} corners (2px). Used sparingly when new SKUs enter the catalog; amber keeps it in the brand voltage without reading as a discount signal.

**`badge-sale`** — Near-black fill ({colors.surface-darkest}) with white text, contrasting clearly against the white product card surface without borrowing the amber reserved for primary actions.

**`badge-bundle`** — Uses {colors.amber-warm} (#fea245) to distinguish bundle and kit pricing from core SKU pricing — a tonal differentiation within the amber family that a buyer scanning quickly can decode instantly.

### Search

**`search-bar`** — White fill with 1px {colors.hairline} border and {rounded.sm}; FontAwesome search glyph in {colors.body} at left inset. On focus, border transitions to 1px {colors.primary} amber — the only light-surface amber interaction accent in the system, creating a consistent focus signal across all inputs.

### Footer

**`footer`** — Near-black ({colors.surface-darkest}) multi-column layout. Section headings in {typography.title-sm}, links in {typography.body-sm} Light. Column dividers use {colors.muted} for low-contrast separation. Social icons via FontAwesome. Legal and policy links sit in a narrow sub-footer row with reduced opacity.

### Category Pills

**`category-pill`** — Light gray fill ({colors.surface-soft}) with {rounded.full} shape, providing visual softness against the harder-edged button system. Active state flips to amber fill ({colors.primary}) with near-black text ({colors.on-primary}), creating a clear selection state without adding new hue vocabulary to the page.

### Quantity Stepper

**`quantity-stepper`** — White field with 1px {colors.hairline} border and {rounded.sm}; increment and decrement buttons use {colors.surface-soft} fill to softly demarcate them from the count input. Height matches `text-input` and `button-primary` at 44px for consistent alignment in add-to-cart rows.

### Material Swatches

**`material-swatch`** — Near-square tiles at 36px with {rounded.xs} corners. Transparent 2px border at rest; 2px {colors.primary} amber border on selection. Designed for dense material and finish selector grids on product pages — the amber selection border is the only amber element in what is otherwise an all-neutral selection component.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen {colors.surface-darkest} drawer; hero stacks headline above CTA vertically; spec table becomes horizontally scrollable panel |
| Tablet | 744–1128px | Two-column product grid; nav shows primary category links with overflow in hamburger; hero splits to two-column with image right |
| Desktop | 1128–1440px | Three-column product grid; full nav bar visible; hero text block constrained to ~600px, image fills remainder |
| Wide | > 1440px | Content max-width 1440px centered; hero image bleeds edge-to-edge behind constrained text block; product grid can expand to four columns |

### Touch Targets
- All interactive controls (buttons, steppers, swatch tiles) hold 44px minimum height
- Nav icons use 44×44px touch target padding regardless of visual glyph size
- Category pills expand vertical padding on mobile to reach 40px minimum tap height
- Material swatches grow from 36px to 44px on mobile grids to prevent mis-taps in dense selector rows

### Collapsing Strategy
- Primary nav collapses to hamburger below 744px; drawer uses {colors.surface-darkest} full-screen overlay with white links
- Machine spec tables become horizontally scrollable panels on mobile rather than stacking key–value pairs vertically
- Product card image aspect locks at 1:1; title, price, and badge stack below image on all breakpoints
- Hero text prose width caps at 600px on wide viewports; dark background extends full-bleed

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border-radius values not extractable from live site — {rounded.sm} (4px) inferred from industrial aesthetic and CNC-geometry visual language
- Primary-active hover color (#d48500) is derived from primary (#fea609) by darkening approximately 15%; no hover-state hex was captured from the live site
- Dark-mode versus light-mode section split is inferred — site likely alternates dark hero/callout bands with white product-page canvases, but exact section boundaries were not mapped
- FontAwesome version and specific glyph subset used for icons not determinable from extraction
- Exact nav height (60px) inferred from Shopify theme proportions; live value may differ by 8–12px
- No motion or animation tokens captured — transition timing for hover fills, drawer opens, and accordion spec panels unknown
- AlrightSans is a licensed typeface; fallback rendering in Arial/Helvetica will differ noticeably in weight contrast and letter spacing across all scales
