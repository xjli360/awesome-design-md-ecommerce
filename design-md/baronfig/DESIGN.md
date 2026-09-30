---
version: alpha
name: "Baronfig"
source_url: "https://baronfig.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The electric acid-yellow (#e5ff01) running through Baronfig's hero and promotional surfaces reads like a highlighter drawn across a white page — a visual pun that is also a brand thesis. "Tools for Thinkers" is the tagline; the neon chartreuse is how the brand literalizes it onscreen, deploying the color in single-word emphasis spans and CTA containers rather than washing entire backgrounds. Against that voltage, a deep institutional cobalt (#001da3) carries every primary action — CTA buttons, active states, and focus rings hold the same ink-blue that appears in university notebooks and archival pens. The warm off-whites pulled from the palette (#f7f5ef, #ece9e2, #e6e2d9) are not generic light-mode backgrounds; they carry the temperature of laid paper and old notebook stock, giving the storefront a material register that pure white would flatten. Figtree runs throughout as the sole type system, a geometric sans with open counters that stays crisp at the tight line-lengths a stationery product grid demands. Headlines run at weight 700 and 52px on hero entries, but body copy drops immediately to 400 weight at 16px — the brand trusts photography and product surfaces over typographic muscle. Letter-spacing sits at or below zero on all display sizes, pressing characters into the compact rhythm of a ruled notebook page. Corners are nearly flat: {rounded.sm} at 4px governs cards and text inputs; {rounded.xs} at 2px appears on inline UI chips and quantity steppers. The only {rounded.full} elements are pill-shaped quantity controls and small tag badges — the sole concession to softness in an otherwise spare geometry. No drop shadows separate cards from canvas; the separation comes from the hairline border (#d9d9d9) and a one-step background shift to surface-warm (#f7f5ef). The announcement bar and hero sections invert: near-black (#212121) or cobalt (#001da3) ground with white type, and the acid-yellow reserved for a single highlighted phrase or promo label, replicating the physical act of marking one sentence in a page of running text.

colors:
  primary: "#001da3"
  primary-hover: "#0022bc"
  primary-active: "#000f56"
  primary-disabled: "#e7ebff"
  accent: "#e5ff01"
  accent-muted: "#cfe700"
  accent-hover: "#a1b300"
  accent-soft: "#f5ff9a"
  gold: "#fed602"
  gold-deep: "#e6c101"
  ink: "#212121"
  body: "#2e2e2e"
  muted: "#646464"
  muted-light: "#9e9e9e"
  hairline: "#d9d9d9"
  hairline-soft: "#ededed"
  canvas: "#ffffff"
  surface-soft: "#f7f9fa"
  surface-card: "#f2f2f2"
  surface-warm: "#f7f5ef"
  surface-warm-mid: "#ece9e2"
  surface-warm-deep: "#e6e2d9"
  cobalt-tint: "#e7ebff"
  on-primary: "#ffffff"
  on-accent: "#212121"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-sm:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  overline:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-lg:
    fontFamily: "'Figtree', Inter, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.1px

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
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-hover:
    backgroundColor: "{colors.accent-muted}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    typography: "{typography.body-md}"
  text-input-focus:
    borderColor: "{colors.primary}"
    outlineColor: "{colors.primary}"
    outlineWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
  announcement-bar:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label-sm}"
    height: 36px
    padding: "0 {spacing.base}"
  announcement-bar-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    height: 36px
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageRounded: "{rounded.xs}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-hover:
    border: "1px solid {colors.ink}"
  hero-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  hero-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  hero-warm:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  highlight-span:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    padding: "2px 4px"
    rounded: "{rounded.xs}"
  badge-new:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-limited:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    height: 40px
    padding: "0 {spacing.base}"
    typography: "{typography.body-sm}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 36px
    minWidth: 100px
    typography: "{typography.title-sm}"
  collection-card:
    backgroundColor: "{colors.surface-warm-mid}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    headlineTypography: "{typography.display-sm}"
  section-divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Deep cobalt (#001da3) fill with white type at 15px/600 weight, flat {rounded.sm} corners at 4px. Hover shifts to the brighter #0022bc (`primary-hover`); active drops to near-black navy #000f56 (`primary-active`); disabled fades to pale cobalt tint with muted text. Height locks at 44px. The primary choice for add-to-cart actions on white and warm backgrounds.

**`button-accent`** — Acid-yellow (#e5ff01) fill with near-black type, same 4px rounding and 44px height as primary. Deployed for hero CTAs on dark backgrounds where the yellow reads as a literal highlighter. Hover shifts to the slightly muted chartreuse (#cfe700). Use at most once per viewport — its intensity is the signal; repetition destroys the effect.

**`button-secondary`** — White fill, 1px solid {colors.ink} border, {colors.ink} text, matching 44px height. Sits beside primary or accent buttons as the secondary choice (View All, Learn More). Hover lifts background to {colors.surface-soft}.

**`button-ghost`** — No fill, no border; cobalt text with underline. Reserved for inline editorial links and tertiary actions within body copy where a bordered control would interrupt reading flow.

### Navigation

**`nav-bar`** — 60px tall on a white ground with a hairline-soft bottom border. Logo sits flush left; navigation links in {typography.nav-link} at 15px/500; cart icon right with an item-count badge. On dark-hero pages, `nav-bar-dark` inverts to {colors.ink} fill with {colors.on-dark} type — the transition reinforces the page's tonal shift rather than fighting it.

**`announcement-bar`** — 36px tall strip stacked above the nav. Default `announcement-bar` uses the acid-yellow with near-black type for free-shipping thresholds and launch notices. `announcement-bar-dark` swaps to cobalt fill with white type for sale events or urgency messaging. Both use {typography.label-sm} centered in the strip.

### Inputs & Search

**`text-input`** — White background, 1px {colors.hairline} border, {rounded.sm} corners, 44px height. On focus, border and a 2px outline both shift to {colors.primary} cobalt. Placeholder in {colors.muted}. Used for email capture, checkout fields, and account forms.

**`search-bar`** — Compact 40px height with {colors.surface-soft} background and {typography.body-sm} query text. Lives inline in the nav-bar on desktop, and expands to a full-width overlay on mobile. No visible border at rest; on focus it acquires the same cobalt outline as `text-input-focus`.

**`quantity-stepper`** — The one consistently pill-shaped ({rounded.full}) control in the UI. Minus and plus triggers sit on the ends at 36px total height, with the count centered. Hairline border at rest; reinforces the precision-tool aesthetic of the product category.

### Product Cards

**`product-card`** — White background, 1px {colors.hairline} border, {rounded.sm} corners. Product image fills the upper portion of the card with {rounded.xs} (2px) clipping; product name in {typography.title-sm}; price in {typography.price} at weight 700. On hover, the border sharpens to 1px solid {colors.ink} — no shadow, no lift, just a crisper frame. Internal padding is {spacing.base} on all sides.

**`collection-card`** — Category navigation tile in warm mid-surface (#ece9e2). Headline in {typography.display-sm}, product image overlaid at an angled or floating crop. Represents notebook lines, pen families, or object collections rather than individual SKUs.

### Hero Sections

**`hero-dark`** — Full-bleed near-black (#212121) background, white type. Headline in {typography.display-xl} at 52px/700, subhead in {typography.body-md}. Padding {spacing.section} vertical, {spacing.xl} horizontal. Primary surface for new product launches and brand-statement pages.

**`hero-accent`** — Same full-bleed structure with acid-yellow (#e5ff01) fill and near-black type. Used for limited drops and seasonal campaigns where maximum attention is required. A `highlight-span` within the headline will use the cobalt or dark ink for contrast inversion.

**`hero-warm`** — Off-white (#f7f5ef) background with {colors.ink} text. Calmer editorial surface for brand-story sections, journal content, and "about" entries. The paper-stock temperature makes it feel like a continuation of the product rather than a generic page.

### Badges & Labels

**`badge-new`** — Acid-yellow fill, near-black overline type, {rounded.xs} corners, 3px×8px padding. Applied to product card images for recently launched SKUs.

**`badge-sale`** — Cobalt fill, white overline type. Applied to discounted items in the grid.

**`badge-limited`** — Near-black fill, white overline type. Applied to limited-run or low-inventory items.

**`highlight-span`** — Inline text emphasis: acid-yellow background behind one word or short phrase, {rounded.xs} 2px radius, 2px×4px internal padding. Used in headlines and editorial copy to replicate the physical act of running a highlighter across a sentence. Should appear on at most one phrase per headline block.

### Footer

**`footer`** — Near-black ({colors.ink}) background, white body text and links at {typography.body-sm}. Link color at rest is {colors.hairline} (light gray, legible against dark); hover lifts to {colors.canvas} white. Padding is {spacing.xxl} above and below the link grid. Newsletter sign-up input and social icons sit at the top of the footer column before the link navigation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger + centered logo + cart icon; hero headline steps down to display-md (32px); announcement-bar truncates to single-line marquee ticker; search expands to full-screen overlay on trigger |
| Tablet | 744–1128px | Two-column product grid; nav shows primary categories with overflow hamburger for secondary; hero stays full-bleed with reduced side padding |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with all primary categories visible; hero shifts to split layout (text left, product image right) on select templates |
| Wide | > 1440px | Content capped at ~1400px with auto margins; four-column grid maintained; hero padding increases to push content toward vertical center |

### Touch Targets

- All interactive controls (buttons, inputs, quantity stepper, nav links) maintain a minimum 44×44px touch target
- Product card tap area covers the full card face, not just the title or image region
- Announcement bar dismiss control (×) sized to 44px minimum height with additional invisible padding
- Hamburger menu trigger is 44×44px minimum with extended tap area inward

### Collapsing Strategy

- Navigation: full horizontal category links → primary links + overflow hamburger → full hamburger drawer with stacked links
- Product grid: 4-col → 3-col → 2-col → 1-col stepping through breakpoints
- Hero headline: display-xl (52px) → display-lg (40px) → display-md (32px) from wide to mobile
- Footer: 4-column link grid → 2-column → single-column stacked accordion on mobile
- Search: inline bar in nav-bar on desktop → icon trigger expanding to full-screen overlay on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed border-radius values from live site extraction; values assigned by visual inference from the brand's precision-tool aesthetic (nearly flat geometry throughout)
- Button heights and exact padding not extracted; 44px height and 12px/24px padding inferred from minimum touch-target requirements and standard Shopify DTC patterns
- Gold and amber tones (#fed602, #e6c101) appear in the extracted palette; their exact usage context (limited-edition product colorways, seasonal sale accents, or writing instrument finish references) is not confirmed
- No motion or animation tokens extracted; brand likely uses short 150–200ms ease transitions given the spare utilitarian aesthetic, but no values confirmed
- Nav switching logic between light and dark variants not confirmed from extraction; both variants inferred from the range of hero surface colors in the palette
- No icon system identified; brand likely uses a minimal geometric line-icon set consistent with Figtree's proportions, but style and stroke weight unconfirmed
- Grid gutter widths not extracted; {spacing.base} (16px) used as gutter inference from Shopify grid defaults
- Figtree weight assignments (300–800 available) based on visual inference from stationery-brand conventions; no computed style extraction confirmed specific weights in use
