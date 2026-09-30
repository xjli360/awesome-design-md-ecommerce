---
version: alpha
name: "Pioneer"
source_url: "https://www.pioneerminisplit.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Gunmetal gray (#303030) and near-white (#fafafa) carry the frame of a site engineered to inform rather than seduce — Pioneer's pages read like specification sheets adapted for commerce, with BTU counts, SEER ratings, and seasonal efficiency ratios occupying the same visual weight as the price. The brand's mid-navy (#485bad) — closer to blueprint ink than consumer electric blue — anchors every primary call-to-action and active nav state, deliberately distanced from the pale Shopify link-blue (#2c6ecb) that handles secondary affordances. Where most appliance retailers lean into lifestyle photography, Pioneer leans into data: efficiency-green (#168804) appears on in-stock indicators and energy-star callouts; sale red (#f4270c and #c30000) marks promotional pricing with the directness of a warning label. An olive register (#929457, #c6c775) surfaces in certification badges and secondary labels, a muted earthy counterpoint that reads as competence rather than embellishment. Type runs entirely on Inter — a geometric sans that handles engineering terminology cleanly at 14–16px body sizes, stepping up to 700-weight display for product headings without reaching for a separate display face. Buttons carry modest {rounded.sm} corners, inputs sit on {colors.surface-soft} at {rounded.xs}, and product cards use a thin {colors.hairline} border on a {colors.canvas} field — no shadow theatrics. The category grid is dense by consumer-brand standards: six to eight products per viewport, filterable by BTU range, application type, and heating or cooling mode. A persistent promotional banner in {colors.error-bright} red rides above the nav, a convention borrowed from appliance retail that signals Pioneer knows its buyers arrive price-sensitive and comparison-ready. The palette's warm taupe and cool sage channels (#938888, #868f89, #b5c2b9) appear in alternating spec-table rows and comparison tab backgrounds — low contrast, high legibility, calibrated for reading a twenty-line specification chart without eye fatigue.

colors:
  primary: "#485bad"
  primary-active: "#3a4d9a"
  primary-disabled: "#a5aed7"
  ink: "#303030"
  body: "#5e5e5e"
  muted: "#919191"
  muted-soft: "#c2c9cf"
  hairline: "#e2e2e2"
  hairline-soft: "#ededed"
  canvas: "#fafafa"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#168804"
  error: "#c30000"
  error-bright: "#f4270c"
  link: "#2c6ecb"
  badge-olive: "#929457"
  badge-olive-light: "#c6c775"
  warm-muted: "#938888"
  cool-sage: "#868f89"
  cool-sage-light: "#b5c2b9"
  promo-banner: "#f4270c"

typography:
  display-xl:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "Inter, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  spec-label:
    fontFamily: "Inter, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "Inter, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  nav-link:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  promo-text:
    fontFamily: "Inter, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    pointerEvents: none
  button-secondary:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
    focusBorder: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 40px
    iconColor: "{colors.muted}"
    focusBorder: "1px solid {colors.primary}"
  promo-banner:
    backgroundColor: "{colors.promo-banner}"
    textColor: "{colors.on-primary}"
    typography: "{typography.promo-text}"
    padding: 8px 16px
    height: 36px
    textAlign: center
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    linkHoverColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    hoverBorderColor: "{colors.primary}"
  efficiency-badge:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  sale-badge:
    backgroundColor: "{colors.error-bright}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  olive-badge:
    backgroundColor: "{colors.badge-olive}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  stock-badge-in:
    backgroundColor: transparent
    textColor: "{colors.success}"
    typography: "{typography.badge}"
    iconColor: "{colors.success}"
  stock-badge-out:
    backgroundColor: transparent
    textColor: "{colors.error}"
    typography: "{typography.badge}"
    iconColor: "{colors.error}"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    headerTextColor: "{colors.muted}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.body}"
    alternateRowBackground: "{colors.hairline-soft}"
    padding: "{spacing.base}"
  category-filter:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 14px"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.title-lg}"
    overlayColor: "rgba(48,48,48,0.55)"
    minHeight: 480px
    ctaPadding: "{spacing.lg}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    linkColor: "{colors.canvas}"
    linkHoverColor: "{colors.primary-disabled}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.body}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Flat {colors.primary} navy block, white Inter at 15px/600, 44px tall with {rounded.sm} corners and 12px 24px padding. Active state darkens to {colors.primary-active}; disabled fades to {colors.primary-disabled} and suppresses pointer events. Used for Add to Cart, Buy Now, and search submission throughout the store.

**`button-secondary`** — White {colors.canvas} fill with a 1px {colors.primary} border and navy label text; matches button-primary in height and radius for side-by-side CTA groupings. Typical pairings: "View Details" next to "Add to Cart" on product cards, or "Contact Support" beside a primary purchase CTA.

**`button-ghost`** — No fill or border; {colors.ink} text at 13px/600. Handles filter resets, spec-panel secondary actions, breadcrumb sub-links, and modal dismissals.

### Inputs & Search

**`text-input`** — {colors.surface-soft} background, 1px {colors.hairline} border, 42px tall, {rounded.xs} corners. Focus swaps the border to 1px {colors.primary}. Placeholder in {colors.muted}. Used for checkout fields, account forms, and quantity selectors.

**`search-bar`** — A compact 40px text input with a leading magnifier icon in {colors.muted} and the same {rounded.xs} geometry. Appears in the nav rail on desktop and as a full-width element in mobile category headers. Focus border follows the same 1px {colors.primary} treatment.

### Navigation

**`nav-bar`** — 64px tall, {colors.canvas} background with a 1px {colors.hairline} bottom rule. Logo sits left; nav links (Products, Where to Buy, Support, About) center on desktop; cart and account icons anchor right. Collapses to hamburger plus logo plus cart below tablet breakpoint. Link hover tints to {colors.primary}.

**`promo-banner`** — Full-width 36px bar anchored above the nav in {colors.promo-banner} red, white {typography.promo-text} centered. Carries free-shipping thresholds, seasonal sale copy, and limited-time financing offers. Dismissable on mobile if a close icon is present.

### Cards & Listings

**`product-card`** — White {colors.surface-card} field, 1px {colors.hairline} border, {rounded.sm} corners. On hover, border steps to {colors.primary}. Image occupies a 4:3 slot at the top; title in {typography.title-sm}, BTU/zone caption in {typography.body-sm}, and price in {typography.title-md} stack below with {spacing.base} interior padding. Efficiency, sale, and in-stock badges overlay the image top-left corner.

### Badges & Status

**`efficiency-badge`** — Solid {colors.success} green pill with white {typography.badge} text, {rounded.xs} corners, 2px 8px padding. Carries SEER rating (e.g. "SEER 20") or Energy Star qualification. Appears on product cards and PDP hero sections.

**`sale-badge`** — Identical geometry to efficiency-badge but in {colors.error-bright}. Carries discount percentage (e.g. "–18%"). Stacks below the efficiency badge when both are present.

**`olive-badge`** — {colors.badge-olive} fill, same shape. Used for certification labels (e.g. "ETL Listed", "AHRI Certified") and line-specific product tiers.

**`stock-badge-in`** / **`stock-badge-out`** — Text-only inline indicators. In-stock renders {colors.success} with a filled circle icon; out-of-stock renders {colors.error}. Both use {typography.badge} weight. Appear below the price on product cards and on the PDP above the Add to Cart button.

### Data Display

**`spec-table`** — Two-column dense table for technical specifications. Header row in {colors.surface-soft} with spec names in 11px uppercase {typography.spec-label} at {colors.muted}; values in {typography.body-sm} at {colors.body}. Alternating rows in {colors.hairline-soft}. Wrapped in {rounded.sm} with a perimeter {colors.hairline} border. Spans full column width on PDP below product description. Scrolls horizontally on mobile rather than collapsing.

### Filtering

**`category-filter`** — Horizontal chip strip for filtering product grids by BTU range (9,000–36,000+), zone count (single/multi), application (mini-split, portable, heat pump), and mode (cooling only, heat pump). Default: {colors.surface-soft} with {colors.hairline} border. Active: {colors.primary} fill, white text. {rounded.xs} corners, 6px 14px padding. Wraps to two rows on mobile.

### Hero

**`hero-banner`** — Minimum 480px tall with a {colors.ink} base and a 55% opacity overlay over product or lifestyle imagery. Headline in {typography.display-xl} at {colors.canvas}; subhead in {typography.title-lg}. Single primary button CTA. Desktop: text and CTA left-aligned. Mobile: full-width stacked layout, headline steps down to {typography.display-md}.

### Navigation Context

**`breadcrumb`** — Slim trail in {colors.muted} {typography.caption}, with the current page segment in {colors.ink}. Appears on PDP and category pages immediately below the nav bar. Separator chevrons in {colors.hairline}.

### Footer

**`footer`** — {colors.ink} background with {colors.muted-soft} body copy and {colors.canvas} link labels. Section headings in {typography.title-sm}. Four-column layout on desktop (Products, Support, Company, Connect); single-column accordion on mobile. A top rule in {colors.body} separates footer from page content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav; hero text and CTA stack vertically; spec-table scrolls horizontally; category-filter chips wrap to two rows; promo-banner truncates text |
| Tablet | 744–1128px | Two-column product grid; nav links visible if five or fewer; hero shifts to left-aligned text with image right; spec-table fixed layout |
| Desktop | 1128–1440px | Three-to-four-column product grid; full nav with inline search bar; spec-table full-width; promo-banner single line |
| Wide | > 1440px | Content max-width 1440px centered; outer gutters absorb additional space; product grid holds at four columns |

### Touch Targets

- All primary and secondary buttons minimum 44×44px tap target
- Nav links and hamburger icon padded to 44px height on mobile
- Category filter chips minimum 36px height; tap padding expands hit area to 44px
- Efficiency and sale badges are display-only; Quick Add and wishlist icon buttons maintain 44px height independently

### Collapsing Strategy

- Nav collapses to hamburger at < 744px; cart icon always visible
- Promo banner truncates to ellipsis on < 375px if copy exceeds single line at 13px
- Spec-table switches to horizontal scroll container on mobile; column count unchanged
- Footer section columns collapse into tap-to-expand accordion panels on mobile
- Hero subheadline hidden at < 375px to keep primary CTA above the fold
- Category filter chips reflow to two rows before becoming a dropdown modal at < 375px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand font confirmed; Inter appears to be the sole typeface — no webfont URL or secondary face detected
- Exact button border-radius and padding values are inferred from Shopify Dawn theme conventions and may differ from live implementation
- Active and hover state colors for button-primary ({colors.primary-active}) are derived by darkening the extracted primary — not directly confirmed from scrape
- Sale strikethrough price color not extracted; {colors.muted} assumed
- Mobile nav drawer overlay opacity and background color not captured
- Grid gutter widths not confirmed; {spacing.base} (16px) gutters assumed
- Product image aspect ratio assumed 4:3; portable AC and outdoor unit images may use different crops
- The olive register (#929457, #c6c775) and sage/taupe tones (#938888, #868f89, #b5c2b9) are present in the extracted palette but their exact UI roles are inferred rather than confirmed — may serve category-specific accent or comparison-table purposes
- Animation durations and easing curves not extractable from static scrape; 150ms ease-in-out transitions assumed throughout
