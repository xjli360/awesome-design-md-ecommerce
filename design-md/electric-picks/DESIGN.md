---
version: alpha
name: "Electric Picks"
source_url: "https://www.electricpicks.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  "Not Just Another Gold Chain" signals intent before a product image loads — Electric Picks sets this anti-category tagline in GT America Expanded, a wide-cut muscular grotesque that is essentially absent from the costume-jewelry category but reads as precisely correct once seen in context. The typographic choice is the whole argument: where competitors reach for delicate script fonts and monotone blush, this brand uses that same blush palette — pale #fdecf0 through candy-pink #f7adc3 and terracotta-edged #d6938a — but grounds it in near-black (#231f20, #303030) and deploys a single saturated cherry-red (#e60c41) only at moments of action: add-to-cart, promotional banners, hover highlights. On the warm cream canvas (#fafaf7) and blush card surfaces, that red lands with billboard weight rather than generic urgency. A custom electric-picks font stack appears alongside GT America Expanded, suggesting a bespoke display lockup reserved for hero moments and the wordmark — the two-font system gives the brand editorial range without incoherence. Corner radii are kept deliberately tight: {rounded.full} appears only on filter pills and swatch dots, while buttons and product cards hold {rounded.sm} so the system never tips into the approachable softness of a skincare DTC. Warm intermediate grays (#9e9f9f, #c7c7c7, #bebebe) handle hairlines and secondary metadata so the blush-pink family remains exclusive to brand-identity surfaces. The spacing system opens generously at editorial callout rows and hero sections ({spacing.section} and {spacing.xxl}) but tightens to {spacing.sm}–{spacing.md} within product grids, maintaining density without catalogue-page compression. The overall system reads as a jewelry brand that has decided its product already does the delicate work — the interface can afford to be bold.

colors:
  primary: "#e60c41"
  primary-active: "#e70a44"
  primary-disabled: "#c7c7c7"
  ink: "#231f20"
  body: "#303030"
  muted: "#555555"
  muted-soft: "#9e9f9f"
  hairline: "#dedede"
  hairline-soft: "#ececec"
  canvas: "#fafaf7"
  surface-soft: "#f4f4f4"
  surface-card: "#fdecf0"
  surface-blush: "#f8ede7"
  surface-warm: "#f7f1ef"
  on-primary: "#ffffff"
  blush-mid: "#f7adc3"
  blush-warm: "#f3dedc"
  blush-deep: "#dea8a1"
  blush-terracotta: "#d6938a"
  near-black: "#010101"
  mid-gray: "#bebebe"
  light-gray: "#dbdbdb"

typography:
  display-xl:
    fontFamily: "'electric-picks', 'GT America Expanded', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'GT America Expanded', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'GT America Expanded', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'GT America Expanded', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'GT America Expanded', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  body-md:
    fontFamily: "'GT America Expanded', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'GT America Expanded', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'GT America Expanded', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'GT America Expanded', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'GT America Expanded', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'GT America Expanded', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'GT America Expanded', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  announcement:
    fontFamily: "'GT America Expanded', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge:
    fontFamily: "'GT America Expanded', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.button-sm}"
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    padding: 12px 16px
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: none
    padding: 10px 20px
    placeholderColor: "{colors.muted-soft}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.announcement}"
    padding: "{spacing.sm} {spacing.base}"
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
    height: 64px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    imageRounded: "{rounded.xs}"
    priceTypography: "{typography.price-display}"
    badgeTypography: "{typography.badge}"
    hoverShadow: "0 4px 16px rgba(35,31,32,0.10)"
    padding: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    minHeight: 560px
    padding: "{spacing.section} {spacing.lg}"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "8px 16px"
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
    padding: "8px 16px"
  badge-new:
    backgroundColor: "{colors.blush-mid}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.hairline}"
    selectedBorder: "1.5px solid {colors.ink}"
  quick-add-pill:
    backgroundColor: "{colors.surface-blush}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    headerTypography: "{typography.title-md}"
    borderLeft: "1px solid {colors.hairline-soft}"
    width: 400px
  editorial-callout:
    backgroundColor: "{colors.surface-blush}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.mid-gray}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    linkColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Cherry-red (#e60c41) fill with white uppercase text in GT America Expanded at 13px, 1px letter-spacing — the compressed tracking gives it fashion-label authority rather than generic e-comm urgency. Height locks at 48px with 28px horizontal padding; the tight {rounded.sm} (4px) keeps corners nearly square, consistent with the brand's editorial restraint. Active state shifts to #e70a44 (visually identical at a glance, but registers hover feedback). Disabled state collapses to mid-gray (#c7c7c7), maintaining the same uppercase form without false action signal.

**`button-secondary`** — Transparent background with a 1.5px solid ink (#231f20) border, matching uppercase typography and identical 48px height so primary/secondary pairs sit pixel-aligned side by side. On blush surfaces the dark outline provides sufficient contrast without competing with the red signal. Hover typically inverts to ink fill with canvas text.

**`button-ghost`** — Text-only, no border, muted-soft (#9e9f9f) color for low-weight actions like "View all" inside editorial modules. Uses `button-sm` at 11px/1.5px tracking — reads as a quiet prompt rather than a CTA.

### Text Inputs

**`text-input`** — Canvas white (#fafaf7) field with a 1px hairline (#dedede) border, 4px radius, 48px tall. Focus sharpens the border to solid ink (#231f20) — no glow or shadow, just a clean threshold change. Placeholder in muted-soft (#9e9f9f). The search variant uses a pill form (`search-bar`, {rounded.full}) on the soft-surface (#f4f4f4) background so it reads as a contained input zone rather than an open field.

### Navigation

**`nav-bar`** — 64px tall, warm-white canvas, single 1px hairline bottom border. Wordmark rendered in `display-sm` (GT America Expanded, 24px/600), left-aligned on desktop. Nav links at 13px/500 with 0.5px tracking; cart and account appear as bare icon buttons (no background, 44px minimum tap target). The announcement bar above drops an ink-black (#231f20) 40px strip — the black-to-white transition is a clean editorial entry that also reinforces the dark-ground brand language seen in the footer.

### Product Cards

**`product-card`** — Near-flush 2px radius ({rounded.xs}) on both container and image so photography bleeds softly to the card edge without hard geometric cropping. Product name in `body-sm` (14px/400), price in `price-display` (16px/500) below. Badges overlay the top-left image corner. On hover a subtle 0 4px 16px shadow at 10% ink opacity lifts the card without the motion-heavy animations common on Shopify themes — the photography does the selling.

**`badge-new`** — Candy-pink (#f7adc3) fill with ink text, 10px/700 uppercase, 2px radius. Reads as brand-colored accent, not a generic "NEW" stamp. **`badge-sale`** — Cherry-red (#e60c41) fill, white text, identical size; the only other UI surface that uses primary red, linking discount signal to CTA urgency.

### Hero

**`hero-banner`** — Full-bleed, minimum 560px tall on desktop, blush-light (#fdecf0) background behind photography. Headline in `display-xl` — the custom electric-picks stack falls back to GT America Expanded at 56px/700, -0.5px tracking. Subhead in `body-md` (16px/400). A single `button-primary` CTA sits below the subhead. Text block left-aligns on a 50/50 text-image split desktop layout; stacks full-width on mobile with text above image.

### Filters and Swatches

**`filter-pill`** / **`filter-pill-active`** — {rounded.full} pill tags sort the product grid. Inactive state: canvas fill, hairline border, muted body text. Active state: ink fill, white text, ink border — a clean binary toggle with no intermediate states. `color-swatch` dots are 20px circles with 1.5px hairline ring inactive, upgrading to 1.5px ink ring on selection; no checkmark overlay keeps the surface clean.

### Quick Add

**`quick-add-pill`** — Surface-blush (#f8ede7) background, ink text, {rounded.full}, 11px uppercase. Appears as an overlay on product card hover, giving shoppers a path to bag without leaving the grid. The warm blush background is intentional: it reads as brand-surfaced, not a generic tooltip.

### Cart Drawer

**`cart-drawer`** — Right-side slide-in panel, 400px wide, canvas background, `body-md` for line items, `title-md` for the "Your Cart" header. A 1px hairline-soft (#ececec) left border separates it from the page content. Checkout button runs `button-primary` at full drawer width — the only instance where the red CTA spans edge-to-edge, maximizing conversion surface at the highest-intent moment in the funnel.

### Editorial Callout

**`editorial-callout`** — Full-width surface-blush (#f8ede7) band, no radius (edge-to-edge warmth), headline in `display-md` (36px/700), body in `body-md`. Used for brand story, collection launches, and value-proposition copy. Paired with `button-secondary` (outline) so the red CTA voltage is not diluted in editorial context — the red is reserved for transactional moments.

### Footer

**`footer`** — Ink (#231f20) background with mid-gray (#bebebe) body text and canvas-white links, echoing the announcement bar's dark-ground language to bookend the page. Column headings in `title-sm` (13px/600 uppercase). {spacing.section} top and bottom padding creates visual distance from the product grid above, signaling a genuine page end rather than an abrupt stop.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks text above image at full width; nav collapses to hamburger + wordmark + cart icon; filter pills scroll horizontally in a snap container; announcement bar runs as marquee if copy exceeds one line |
| Tablet | 744–1128px | Two-column product grid; hero shifts to 50/50 side-by-side split; nav may abbreviate secondary links to icons; cart drawer expands as bottom sheet rather than side panel |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with all links visible; cart drawer fixed at 400px right side; editorial callout uses side-by-side text-image layout |
| Wide | > 1440px | Content max-width ~1440px centered on page; hero photography fills full viewport width with centered text overlay; four-column grid with relaxed {spacing.base} gutters |

### Touch Targets

- All tappable buttons minimum 48×48px, matching the height spec in `button-primary` and `button-secondary`
- Filter pills minimum 40px tall on mobile for reliable thumb activation
- Color swatches expand to 28×28px on touch viewports via padding increase, preserving the 20px visual dot
- Nav icon hit areas padded to 44px minimum around the 24px glyph
- Quick-add pill minimum 36px tall on touch; expands to full card width on mobile product grid

### Collapsing Strategy

- Navigation: hamburger drawer at < 744px; drawer slides from left, ink-black background, canvas text — mirrors footer palette for brand consistency
- Product grid: 1-col mobile → 2-col tablet → 3-col desktop → 4-col wide; gutter scales from {spacing.sm} to {spacing.base}
- Hero: headline scales from ~32px (mobile) to 56px (desktop) via responsive breakpoints or fluid clamp; layout flips from stacked to side-by-side at 744px
- Filter panel: horizontal scroll pill row on mobile; sticky left sidebar with pills or checkboxes on desktop at ≥ 1128px
- Announcement bar: single-line fixed 40px height throughout; text truncates or marquees at mobile widths

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No `meta theme-color` extracted; mobile browser chrome color unknown — likely ink (#231f20) based on dark announcement bar and footer pattern
- Exact weight range of GT America Expanded in use not confirmed; 400/500/600/700 assumed from genre conventions for expanded grotesques
- Custom `electric-picks` font not publicly documented; whether it is a variable font, a webfont subset, or a logo SVG is unknown — extraction shows the name in the font stack only
- Per-component border-radius not confirmed from extraction; {rounded.sm} (4px) on buttons and {rounded.xs} (2px) on cards are inferences from the overall editorial tone; some CTAs may be fully square ({rounded.none})
- Hover transition timing curves not extractable from static analysis
- Whether product grid uses 3 or 4 columns on 1128–1440px viewports not confirmed; 3-col assumed as default with 4-col optional
- Mobile nav drawer background assumed ink (#231f20) by pattern inference; not directly observed
- Exact blush surface assignment per page template unclear — multiple blush values (#fdecf0, #f8ede7, #f7f1ef) appear in palette and likely rotate across hero, editorial, and card surfaces by section rather than strict token mapping
