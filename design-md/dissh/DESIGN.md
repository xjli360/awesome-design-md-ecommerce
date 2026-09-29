---
version: alpha
name: "Dissh"
source_url: "https://dissh.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Sand-toned canvases and near-black ink open Dissh's digital register — the site runs on a warm off-white (#f8f5f1) field where ABC Diatype Light carries every headline at a weight that reads less as fashion authority and more as editorial understatement. The typeface, a Swiss-rooted geometric grotesque from ABC Dinamo, sets a contemporary tone coherent with the brand's wearable, trend-led Australian sensibility; a companion "Items Light" stack suggests a secondary display cut used for editorial callouts or category statements. What distinguishes the palette from standard Antipodean fashion neutrals is a soft mint-teal surface (#e6f7f4) that breaks from the otherwise warm sandy register — it recurs as a refresh zone against the dominant linen-and-brown spectrum (#ede7df, #bca99f, #3c302a). The deepest brand anchor is a warm molasses-brown (#3c302a) rather than a cool charcoal, pulling the dark end of the scale toward a terracotta-adjacent spectrum that signals resort dressing. Three color registers emerge clearly from extraction: ink darks (#272727, #1c1c1c, #3c302a, #251e1a), warm surfaces (#f8f5f1, #ede7df, #fef3e2, #bca99f), and blue-gray UI chrome (#b1b7c3, #999ea8, #121f36) — the latter cluster appearing in metadata, pagination, and secondary interface elements. Alert red (#ea0202) flags sale pricing and error states but does not function as a brand primary; Bootstrap-adjacent alert surfaces (#f8d7da, #d4edda, #fff3cd) confirm these as Shopify system states rather than brand choices. Buttons and inputs carry minimal rounding consistent with the sharp editorial mode, and the overall hierarchy trusts photography and negative space over typographic weight — the Light font cut is used almost universally rather than escalating to Bold for emphasis, so the lone CTA button on a warm dark fill becomes the loudest thing on screen by contrast alone.

colors:
  primary: "#3c302a"
  primary-active: "#251e1a"
  primary-disabled: "#bca99f"
  ink: "#272727"
  body: "#3c302a"
  muted: "#9b9b9b"
  muted-mid: "#6b6b6b"
  hairline: "#e8e8e8"
  hairline-soft: "#eaeaea"
  hairline-warm: "#dedede"
  canvas: "#f8f5f1"
  surface-soft: "#ede7df"
  surface-cream: "#fef3e2"
  surface-mint: "#e6f7f4"
  surface-card: "#f5f5f5"
  surface-cool: "#f4f8fe"
  on-primary: "#f8f5f1"
  ui-gray: "#999ea8"
  ui-blue-gray: "#b1b7c3"
  deep-navy: "#121f36"
  accent-taupe: "#bca99f"
  error: "#ea0202"
  error-dark: "#721c24"
  error-surface: "#f8d7da"
  error-text: "#642223"
  success-surface: "#d4edda"
  success-text: "#155724"
  warning-surface: "#fff3cd"
  warning-text: "#856404"

typography:
  display-xl:
    fontFamily: "'ABC Diatype Light', 'ABC Diatype Light Fallback', sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'ABC Diatype Light', 'ABC Diatype Light Fallback', sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'ABC Diatype Light', 'ABC Diatype Light Fallback', sans-serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: -0.2px
  items-display:
    fontFamily: "'Items Light', 'Items Light Fallback', 'ABC Diatype Light', sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.4px
  title-md:
    fontFamily: "'ABC Diatype Light', 'ABC Diatype Light Fallback', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'ABC Diatype Light', 'ABC Diatype Light Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'ABC Diatype Light', 'ABC Diatype Light Fallback', sans-serif"
    fontSize: 15px
    fontWeight: 300
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'ABC Diatype Light', 'ABC Diatype Light Fallback', sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'ABC Diatype Light', 'ABC Diatype Light Fallback', sans-serif"
    fontSize: 11px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0.2px
  price:
    fontFamily: "'ABC Diatype Light', 'ABC Diatype Light Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'ABC Diatype Light', 'ABC Diatype Light Fallback', sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'ABC Diatype Light', 'ABC Diatype Light Fallback', sans-serif"
    fontSize: 11px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  label-uppercase:
    fontFamily: "'ABC Diatype Light', 'ABC Diatype Light Fallback', sans-serif"
    fontSize: 10px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'ABC Diatype Light', 'ABC Diatype Light Fallback', sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0.5px

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
    padding: "14px 32px"
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "13px 31px"
    border: "1px solid {colors.primary}"
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: none
    padding: "0"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.xxl}"
  promo-banner:
    backgroundColor: "{colors.surface-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.primary}"
    salePriceColor: "{colors.error}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} 0"
    gap: "{spacing.xs}"
  product-card-hover:
    imageSwapEnabled: true
    quickAddVisible: true
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderFocusColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 44px
    iconColor: "{colors.muted-mid}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.body}"
    padding: "{spacing.xxl} {spacing.section}"
    textAlign: left
  editorial-banner:
    backgroundColor: "{colors.surface-mint}"
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl} {spacing.xxl}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "#ffffff"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-sold-out:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted-mid}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    selectedBorder: "1px solid {colors.primary}"
    selectedBackground: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    unavailableBorder: "1px solid {colors.hairline-soft}"
    unavailableTextColor: "{colors.muted}"
    height: 40px
    minWidth: 40px
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    selectedRing: "2px solid {colors.primary}"
    selectedRingOffset: 2px
    soldOutDiagonal: true
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "6px 14px"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline-warm}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    headingColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.section}"
  alert-error:
    backgroundColor: "{colors.error-surface}"
    textColor: "{colors.error-text}"
    borderColor: "{colors.error-dark}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  alert-success:
    backgroundColor: "{colors.success-surface}"
    textColor: "{colors.success-text}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  alert-warning:
    backgroundColor: "{colors.warning-surface}"
    textColor: "{colors.warning-text}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"

## Components

### Buttons

**`button-primary`** — Sharp-cornered (`{rounded.none}`), warm molasses-brown (#3c302a) fill with near-white (#f8f5f1) text set in 12px uppercase ABC Diatype Light at 1.5px tracking. Hover darkens to `{colors.primary-active}` (#251e1a); disabled state falls back to the warm taupe `{colors.primary-disabled}` (#bca99f), keeping tonal warmth rather than dropping to a generic gray. Fixed height of 48px ensures mobile CTA parity with touch targets.

**`button-secondary`** — Transparent fill with a 1px `{colors.primary}` border and matching ink text; the same uppercase micro-type as primary. Used for secondary confirmations, wishlist actions, and "View All" category links; left-right padding matches primary so button pairs align in height and width without visual competition.

**`button-ghost`** — Borderless, zero-padded, `{colors.ink}` text. Functions as navigation text-links, filter resets, and modal dismissals. Underline appears on hover. The absence of a container is intentional — ghost actions recede so product and primary CTAs read forward.

### Navigation

**`nav-bar`** — 60px fixed bar over `{colors.canvas}` (#f8f5f1) with a 1px `{colors.hairline}` underline. ABC Diatype Light at 13px/0.5px tracking keeps nav labels typographically indistinguishable from body copy — there is no weight bump for navigation. The `promo-banner` strip in `{colors.surface-mint}` (#e6f7f4) rides above the bar at 36px, providing the only non-warm, non-neutral element in the global chrome. Mega-menu panels drop below the bar on category hover, pairing editorial image tiles with link columns in the same light-weight type.

### Product Card

**`product-card`** — Sharp-cornered 3:4 portrait frame with no background fill; the warm canvas shows through between grid items. Title in `{typography.body-sm}` (13px Light) and price in `{typography.price}` (14px Light) sit left-aligned beneath the image with `{spacing.xs}` gap. On hover, a second product image swaps in and a quick-add tray slides up from the card bottom edge. Sale price renders in `{colors.error}` (#ea0202) with the original struck through in `{colors.muted}`. Badge overlays position absolutely at image top-left.

### Badges

**`badge-new`**, **`badge-sale`**, **`badge-sold-out`** — All share `{typography.label-uppercase}` (10px, 300 weight, 2px tracking, uppercase) over square corners. NEW uses `{colors.primary}` fill with `{colors.on-primary}` text; SALE uses the alert red `{colors.error}` (#ea0202); SOLD OUT uses the neutral `{colors.hairline}` fill with `{colors.muted-mid}` text. All badges are absolute-positioned at image top-left, stacking vertically when multiple states coexist.

### Size Selector

**`size-selector`** — Grid of square, hairline-bordered tiles in `{typography.body-sm}`. Selected tile inverts to `{colors.primary}` fill and `{colors.on-primary}` text. Unavailable sizes retain the soft border but apply a diagonal strike-through line and `{colors.muted}` label rather than hiding options — scarcity is shown, not hidden. Tile minimum height and width of 40px meets touch target requirements.

### Color Swatch

**`color-swatch`** — 24px circles (`{rounded.full}`) with a 2px offset selection ring in `{colors.primary}`. Sold-out swatches display a diagonal line over the fill color. The swatch row sits between price line and size selector in the PDP action sidebar, functioning as both a selector and a visual inventory signal.

### Hero Banner

**`hero-banner`** — Full-bleed image with `{colors.surface-soft}` (#ede7df) as the load and fallback background. Headline in `{typography.display-xl}` (40px, Light) left-aligned over the image or beneath it depending on layout variant; sub-copy in `{typography.body-md}`. The hallmark move is the Light weight at scale — at 40px the letters feel drawn rather than stamped. CTA row pairs `button-primary` with a `button-ghost` text link.

### Editorial Banner

**`editorial-banner`** — A mint-surface (#e6f7f4) horizontal strip used for seasonal campaign callouts and email capture prompts. Headline in `{typography.display-md}` (28px Light); layout varies between centered and left-aligned by campaign. The mint tone is the sole cool interruption in an otherwise warm palette, giving it high contrast value for attention without resorting to red.

### Search

**`search-bar`** — Sharp-cornered, 44px tall, over `{colors.surface-card}` (#f5f5f5) fill. Placeholder in `{colors.muted}` at `{typography.body-sm}`; a magnifying-glass icon in `{colors.muted-mid}` sits left of the input field. Results drop as a full-width panel below the bar on `{colors.canvas}` with `{colors.hairline}` dividers between result rows.

### Filters

**`filter-chip`** — Rectangular chips with no radius for collection refinement. Inactive: `{colors.canvas}` background, 1px `{colors.hairline}` border, `{colors.ink}` text at `{typography.caption}`. Active: full `{colors.primary}` fill, `{colors.on-primary}` text. On mobile, chips wrap into multiple rows rather than scrolling horizontally, keeping the full filter vocabulary visible.

### Footer

**`footer`** — Warm dark primary fill (`{colors.primary}`, #3c302a) inverts the page: `{colors.on-primary}` (#f8f5f1) text throughout. Category headings in `{typography.label-uppercase}` (10px, 2px tracking, uppercase); link body in `{typography.body-sm}` (Light weight). Newsletter input sits inline with a right-aligned submit, ghost-styled for the dark context. Payment method logos and social icons render as white SVGs against the dark fill.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav with slide-in drawer, hero headline drops to `{typography.display-md}`, filter panel becomes full-screen modal |
| Tablet | 744–1128px | Two-column product grid, condensed nav with top-level categories visible, hero retains full image-text layout |
| Desktop | 1128–1440px | Three- to four-column product grid, full mega-menu on hover, sticky action sidebar on PDP |
| Wide | > 1440px | Container max-width capped at ~1440px, centered, with `{spacing.section}` lateral padding; product grid column count held at four |

### Touch Targets
- All primary CTAs (buttons, size tiles) hold 48px minimum height
- Color swatches are 24px visually but wrapped in a 40px tap zone
- Nav links in the mobile drawer carry 48px row height
- Filter chips on mobile are min-height 40px vs. 32px on desktop
- Quick-add tray on product cards covers the lower 48px of the card image on mobile

### Collapsing Strategy
- Mega-menu collapses to a slide-in drawer with accordion expand/collapse per category
- PDP sidebar (swatch, size, CTA, description accordion) stacks below the full-bleed product image on mobile
- Hero banner shifts to image-above, text-below stacking below 744px
- Footer four-column link grid becomes single accordion-per-column on mobile
- Promo banner reduces to 28px height on mobile; copy truncates with ellipsis if needed

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed single signature accent hue; warm dark brown (#3c302a) is assigned as primary based on list position but may function purely as a text/ink color rather than a CTA fill — actual CTA color may be `{colors.ink}` (#272727) or a value not captured in extraction
- Font weight variants for ABC Diatype beyond Light (Regular, Medium, Bold) not confirmed — only the Light cut is attested in the extracted stack; additional weights may load via JS and control heading emphasis on sale or editorial pages
- "Items Light" / "Items Light Fallback" family role is unclear — could be a distinct editorial display cut or an aliased internal name for ABC Diatype; no confirmed size or placement context available
- Button corner radius not confirmed from extraction — `{rounded.none}` assigned based on minimal-fashion Shopify patterns; may actually be `{rounded.xs}` (2px) on inputs and some buttons
- Deep navy (#121f36) and blue-gray (#b1b7c3, #999ea8) roles in UI chrome not fully traced — likely used in pagination dots, secondary metadata labels, or a specific colorway product category rather than primary interface elements
- Product card image aspect ratio (3:4) is a convention inference for women's apparel; not directly extracted from grid markup
- Navigation height (60px) and sticky/transparent-on-scroll behavior are estimated; exact scroll transition not confirmed
- No confirmed brand icon set weight or style (line vs. filled, stroke width) documented from extraction
