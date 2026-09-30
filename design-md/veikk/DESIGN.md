---
version: alpha
name: "Veikk"
source_url: "https://www.veikk.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Near-black at #171717 framing electric lime (#cdf564) CTAs reads like a drawing tablet's pressure canvas lit in a darkened studio — the site mirrors the working conditions of the artists who use the hardware. Veikk runs this inversion deliberately: while most consumer hardware brands scaffold in white and blue, the primary chrome lives on #171717 and #121212, making the lime and the structural teal (#108474) accelerate with the same intensity as highlight strokes on a top digital layer. The structural brand color is #108474, a deep teal that anchors product headers, feature callout borders, and secondary CTA fills. Electric lime (#cdf564, with a near-twin at #ccff66) surfaces specifically on the highest-priority actions — "Add to Cart," "Buy Now," sale banners, and active filter states — functioning as a voltage spike that the dark field amplifies rather than diffuses. A golden yellow (#fbcd0a) pulls discount and urgency badges; a soft lavender (#a89cc8) appears on accessory lines and mid-tier product markers, broadening the palette without muddying the dominant teal-lime pairing. Mint washes (#c5f7f0, #c1e6e6) tint backgrounds behind compatibility callouts and bundle promotions, signaling a softer product tier within the same range. Nunito Sans supplies warmth to an otherwise cold-hardware aesthetic: its curved apertures and generous x-height hold up across both the dark hero canvas and the light product-listing grids (#f9f9f9). Inter steps in for dense specification tables and filtering interfaces where tighter metrics matter more than personality. Rounding follows a two-tier logic: product cards and form inputs land at {rounded.sm} to {rounded.md}, while category filter pills and quick-add badges snap to {rounded.full} — the round pill registers as browseable while the near-square card registers as purchasable. On large viewports a full-bleed rendered pen display dominates the hero's dark field; mobile compresses this to a stacked composition where the lime CTA button expands edge-to-edge as the sole focus element, every decorative surface receding into the #171717 field behind it.

colors:
  primary: "#108474"
  primary-active: "#0a6358"
  primary-disabled: "#6ab5ab"
  accent-lime: "#cdf564"
  accent-lime-active: "#b8e050"
  accent-yellow: "#fbcd0a"
  accent-lavender: "#a89cc8"
  accent-mint: "#c5f7f0"
  teal-light: "#c1e6e6"
  ink: "#eeeeee"
  ink-dark: "#171717"
  body: "#bbbbbb"
  muted: "#888888"
  hairline: "#555555"
  hairline-light: "#dedede"
  canvas: "#171717"
  canvas-light: "#f9fafb"
  surface-soft: "#121212"
  surface-card: "#f9f9f9"
  surface-raised: "#e9e9e9"
  on-primary: "#ffffff"
  on-accent: "#121212"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  label-upper:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  spec-label:
    fontFamily: "'Inter', 'Nunito Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 800
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
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.accent-lime-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-outline-hover:
    border: "1px solid {colors.ink}"
    textColor: "{colors.ink}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    activeUnderlineColor: "{colors.accent-lime}"
    activeUnderlineHeight: 2px
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline-light}"
    rounded: "{rounded.sm}"
    imageBg: "{colors.surface-raised}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink-dark}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink-dark}"
    ctaHoverStrip:
      backgroundColor: "{colors.accent-lime}"
      textColor: "{colors.on-accent}"
      typography: "{typography.button-sm}"
      height: 40px
  hero-section:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    sublineTypography: "{typography.body-md}"
    sublineColor: "{colors.body}"
    ctaComponent: button-primary
    backgroundGradient: "radial-gradient(ellipse at 60% 50%, #1a1a1a 0%, {colors.surface-soft} 100%)"
    productImageMaxWidth: 55vw
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  badge-sale:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  badge-bundle:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink-dark}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  category-pill:
    backgroundColor: transparent
    border: "1px solid {colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    height: 32px
    padding: 0 14px
  category-pill-active:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.accent-lime}"
    textColor: "{colors.ink}"
  spec-row:
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.spec-label}"
    valueColor: "{colors.ink}"
    padding: 10px 0
    borderBottom: "1px solid {colors.hairline}"
    alternateBackgroundColor: "{colors.surface-soft}"
  price-display:
    currentPriceTypography: "{typography.price}"
    currentPriceColor: "{colors.ink}"
    originalPriceTypography: "{typography.body-md}"
    originalPriceColor: "{colors.muted}"
    originalPriceDecoration: line-through
    discountBadge:
      backgroundColor: "{colors.accent-yellow}"
      textColor: "{colors.on-accent}"
      typography: "{typography.caption}"
      rounded: "{rounded.xs}"
      padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    iconColor: "{colors.accent-lime}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 40px
    padding: 0 {spacing.md}
  footer:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.ink}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.accent-lime}"
    columnGap: "{spacing.xxl}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Electric lime (#cdf564) background with dark #121212 text is the page's highest-contrast touch target, engineered to punch out of the dark canvas at maximum luminosity. Padding is 14px vertical, 28px horizontal at 48px height with {rounded.xs} corners — deliberately less rounded than the cards it sits on, signaling action over browsing. Hover state darkens to `accent-lime-active` (#b8e050); disabled state falls back to {colors.hairline} with {colors.muted} text.

**`button-secondary`** — Deep teal (#108474) fill with white text handles lower-priority CTAs such as "Compare," "Learn More," and wishlist flows. Shares the 48px height and {rounded.xs} geometry with the primary, so the two buttons stack cleanly in split-CTA layouts. Active state tightens to `primary-active` (#0a6358).

**`button-outline`** — Transparent ghost button with a 1px {colors.hairline} border and {colors.ink} text for use over dark backgrounds on product pages and modal footers. On hover the border brightens to full {colors.ink}, making the affordance read as interactive without introducing fill color competition with the lime primary.

### Navigation

**`nav-bar`** — Sticky dark bar at {colors.canvas} carrying the Veikk wordmark left, product category links in {typography.nav-link} center, and icon cluster (search, cart, account) right. A 2px lime underline ({colors.accent-lime}) slides in on hover and persists on the active route. On scroll past the hero, a 1px {colors.hairline} bottom border materializes to visually separate the nav from the light product content below.

### Product Cards

**`product-card`** — Light-surfaced card ({colors.surface-card}) with a square image well on {colors.surface-raised}, model name in {typography.title-md} at {colors.ink-dark}, and price in {typography.price} below. A 1px {colors.hairline-light} border encloses the card at {rounded.sm}. On hover a lime-filled strip slides up from the card bottom carrying a compact "Add to Cart" label in {typography.button-sm}, keeping the default resting state clean and uncluttered.

### Hero Section

**`hero-section`** — Full-bleed {colors.canvas} (#171717) field with a radial gradient blending to {colors.surface-soft} (#121212) behind the product visual. Headline runs in {typography.display-xl} at {colors.ink}; the subline drops to {typography.body-md} at {colors.body}. The rendered pen display or tablet image occupies up to 55% of viewport width on the right half, leaving the left column for text and the lime CTA button. No border, no card, no shadow — the product floats directly on dark.

### Badges

**`badge-new`** — Small {rounded.full} pill with {colors.primary} teal background and white {typography.label-upper} text, positioned top-left on product card images. Signals recently released SKUs.

**`badge-sale`** — Same pill geometry as `badge-new` using {colors.accent-yellow} (#fbcd0a) background with {colors.on-accent} dark text. Used for time-limited discounts and bundle promotions. The yellow contrasts sharply against both the dark canvas and the light card backgrounds, maintaining legibility in both contexts.

**`badge-bundle`** — Soft mint ({colors.accent-mint}) background signals accessory bundle deals — stylus tips, gloves, carrying cases — distinct from sale pricing without competing with the lime primary.

### Category Pills

**`category-pill`** — Outlined {rounded.full} pill at 32px height for product type filters (Pen Displays, Pen Tablets, Accessories). Inactive state uses a 1px {colors.hairline} border with {colors.muted} text. Active state fills with {colors.surface-soft} and switches to a {colors.accent-lime} border with {colors.ink} text, confirming selection without reaching for fill-color weight.

### Spec Table

**`spec-row`** — Two-column key-value row: label in {typography.spec-label} at {colors.muted} left; value in {typography.spec-label} at {colors.ink} right. Rows sit on transparent backgrounds with a 1px {colors.hairline} bottom border; even rows alternate to {colors.surface-soft} for zebra rhythm on dark-background specification panels.

### Price Display

**`price-display`** — Current price in {typography.price} at {colors.ink}, large enough to register immediately in card and PDP contexts. When a discount applies, the original price appears inline in {typography.body-md} with line-through at {colors.muted}, and a compact yellow badge ({colors.accent-yellow}) shows the percentage saved in {typography.caption}.

### Search Bar

**`search-bar`** — Compact inline field within the nav: {colors.surface-soft} background with a 1px {colors.hairline} border at {rounded.sm}, 40px height. Placeholder in {colors.muted}; a lime magnifier icon ({colors.accent-lime}) anchored right serves as submit trigger. On focus the border shifts to {colors.primary} teal.

### Footer

**`footer`** — Dark {colors.canvas} section with a 1px {colors.hairline} top divider and four-column link grid at {spacing.xxl} column gap. Column headers in {typography.title-sm} at {colors.ink}; links in {typography.body-sm} at {colors.body} lift to {colors.accent-lime} on hover. A newsletter row above the columns reuses `text-input` and `button-primary` side by side. Social icon row at bottom uses extracted platform colors (Facebook #3b5998, Twitter/X #1da1f2, Pinterest #e60023).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero stacks product image above text; lime CTA button expands to full width; nav collapses to hamburger; category pills scroll horizontally; product grid becomes 2-column |
| Tablet | 744–1128px | Two-column hero with smaller image (45% width); product grid switches to 3-column; nav shows top-level categories with overflow menu; spec table retains two-column layout |
| Desktop | 1128–1440px | Full hero split (55% product image / 45% text+CTA); 4-column product grid; sticky nav with all categories visible; spec table may expand to inline tabs |
| Wide | > 1440px | Max-width container (~1440px) centered; hero image scales up with preserved aspect ratio; additional featured product row appears in hero section |

### Touch Targets

- All interactive elements (buttons, category pills, nav icons) maintain a minimum 44×44px touch target
- Product cards are fully tappable; the hover CTA strip becomes a persistent bottom bar on touch devices
- Category pill scroll row uses momentum scrolling with 16px padding inset on both ends

### Collapsing Strategy

- Primary nav collapses to hamburger at < 744px; drawer slides from left over {colors.canvas} background
- Hero product image drops below the text+CTA stack on mobile so the CTA is immediately visible above the fold
- Spec table remains two-column on mobile but font size reduces to {typography.body-sm} to fit narrower viewports
- Footer compresses to single-column accordion on mobile; each column header is a tap-to-expand trigger

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom display typeface confirmed — Nunito Sans and Inter are inferred from the font stack extractions; a proprietary or licensed display face may exist but was not detected
- Exact button border-radius values not confirmed from live computed styles; {rounded.xs} (4px) is an inference from the visual appearance
- Dark-mode vs. light-mode switching logic unclear — the meta theme-color is #171717 but many near-white backgrounds (#f9f9f9, #eeeeee) appear in extraction, suggesting either mixed-mode sections or a toggleable theme
- Baskerville appears in the font stack but no editorial or display usage pattern was identified; its role is unknown
- Social platform colors (#3b5998, #1da1f2, #dd4b39, #e60023, #0073b1) are platform-standard and were excluded from the brand color system
- Exact hover/active transition durations and easing curves not extractable from static analysis
- Icon system (product-line glyphs, UI icons) not catalogued — likely SVG inline or a custom icon font separate from JudgemeIcons
