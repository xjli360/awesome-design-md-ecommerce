---
version: alpha
name: "Simms Fishing"
source_url: "https://www.simmsfishing.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Acumin Pro Extra Condensed Bold running at headline weight is the first tell — Simms packs product names into tall, tight stacks the same way a wader chest pocket packs gear into minimal real estate. Against an ink field of deep charcoal (#282824) and river-stone neutrals (#434240, #989990), one color breaks the surface: a burnt orange (#c94b1d) that marks every primary CTA the way a high-vis strike indicator marks a fly on dark water. The site's vertical rhythm is deliberate — generous `{spacing.section}` gaps between editorial chapters, near-white backgrounds (#f7f8f9, #f5f4f3) that let product photography carry emotional weight without chromatic competition. CSBloom appears as a decorative script accent layered over Acumin's angular compression, bridging technical precision with a hand-rendered warmth that other outdoor brands force through raw imagery alone. Product cards stay nearly square-cornered (`{rounded.sm}`), reinforcing an engineering-forward identity — these are precision tools built in Bozeman, Montana and priced like it. Basis Grotesque Pro handles all body copy at comfortable reading weights, its neutrality letting the condensed display faces dominate the hierarchy without typographic collision. A secondary terracotta (#c46441) and an olive-stone spectrum (#737368 through #989990) extend the brand's geological palette across badges, secondary labels, and interface borders, never reaching for the primary orange unless directing action. The alert red (#bf0909) and outdoor green (#158c15) serve as pure status signals — inventory warnings, size availability — never decorative. The result is a storefront that reads like a technical fly shop: organized by function, lit in the warm tones of river stone and late-afternoon sun, with exactly one flash of color to tell you where to go next.

colors:
  primary: "#c94b1d"
  primary-active: "#a33a15"
  primary-disabled: "#e4a070"
  ink: "#282824"
  body: "#434240"
  muted: "#737368"
  stone: "#989990"
  hairline: "#dfdedc"
  hairline-soft: "#dedede"
  canvas: "#f7f8f9"
  surface-soft: "#f5f4f3"
  surface-card: "#f1f1f1"
  surface-sage: "#e4e5dd"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  terracotta: "#c46441"
  olive: "#43433c"
  alert: "#bf0909"
  success: "#158c15"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Acumin Pro Extra Condensed', sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Acumin Pro Extra Condensed', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Acumin Pro Extra Condensed', sans-serif"
    fontSize: 38px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Acumin Pro Extra Condensed', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  script-accent:
    fontFamily: "'CSBloom', cursive"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Acumin Pro Semibold', 'Acumin Pro', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'Acumin Pro Semibold', 'Acumin Pro', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Basis Grotesque Pro', 'Acumin Pro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Basis Grotesque Pro', 'Acumin Pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Basis Grotesque Pro', 'Acumin Pro', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  price-display:
    fontFamily: "'Acumin Pro Semibold', 'Acumin Pro', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Acumin Pro Semibold', 'Acumin Pro', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Acumin Pro Semibold', 'Acumin Pro', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Basis Grotesque Pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Acumin Pro Extra Condensed', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.8px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.on-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-utility-bar:
    backgroundColor: "{colors.olive}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: none
    logoColor: "{colors.on-dark}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
    swatchSize: 16px
    swatchGap: "{spacing.xs}"
    hoverEffect: image-zoom-1.03
    badgePosition: top-left
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    scriptAccentTypography: "{typography.script-accent}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    minHeight: 560px
    overlayScrim: "linear-gradient(to right, rgba(18,18,18,0.72) 40%, transparent)"
    padding: "0 {spacing.xl}"
  hero-editorial:
    backgroundColor: "{colors.surface-sage}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.xl}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  product-badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  product-badge-sale:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  size-chip-available:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    height: 40px
  size-chip-unavailable:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.stone}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    textDecoration: line-through
    padding: "8px 12px"
    height: 40px
  size-chip-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 40px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "12px 16px"
    iconColor: "{colors.muted}"
    height: 48px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "6px 12px"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  category-tile:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-sm}"
    ctaTypography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    overlayGradient: "linear-gradient(to top, rgba(40,40,36,0.78) 0%, transparent 60%)"
  wader-spec-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.title-sm}"
    borderTop: "2px solid {colors.primary}"
    padding: "{spacing.lg}"
    rounded: "{rounded.none}"
  alert-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.stone}"
    linkHoverColor: "{colors.on-dark}"
    dividerColor: "{colors.olive}"
    padding: "{spacing.section} 0"

## Components

### Buttons
**`button-primary`** — A sharp-cornered (`{rounded.none}`) rectangle in burnt orange (#c94b1d) carrying white all-caps type tracked at 1.2px in Acumin Pro Semibold. Fixed height of 48px with 28px horizontal padding provides generous click area without softness. Hover state darkens to `{colors.primary-active}` (#a33a15); disabled washes to `{colors.primary-disabled}` while preserving shape. The uppercase letter-spacing mirrors product-spec language and sets the tone that every purchase decision on this site is a technical one.

**`button-secondary`** — Identical dimensions to primary but with a 2px solid `{colors.ink}` border and transparent fill. Deployed alongside primary on product detail pages to separate Add to Cart from secondary actions such as Find a Retailer or Add to Wishlist. No rounding; no softness.

**`button-ghost`** — Transparent fill with a 2px white border and white uppercase type at `{typography.button-md}`. Used over hero photography and dark editorial sections where the primary orange would fight the image rather than lead the eye. On hover, fills to a semi-transparent white overlay.

### Navigation
**`nav-utility-bar`** — A 36px olive-charcoal (#43433c) strip sitting above the primary nav. Carries shipping threshold copy, store-finder link, and account shortcuts in 12px Basis Grotesque Pro. Collapses completely on mobile, with key links absorbed into the hamburger drawer.

**`nav-bar`** — Full-width dark charcoal (#282824) bar at 56px with the Simms wordmark in white and navigation category links in `{typography.nav-link}` Basis Grotesque Pro. The dark treatment prevents a white bar from interrupting the editorial photography on scroll. Mega-menu drawers open on hover at desktop, revealing subcategory links against the same dark surface.

### Product Card
**`product-card`** — Zero-radius card with a `{colors.surface-soft}` image field. Product title in `{typography.title-md}`, price in `{typography.price-display}` at 20px Acumin Semibold. Color swatches render as 16px circles spaced at `{spacing.xs}`. On hover the product image scales to 1.03× within the fixed container, hinting at depth without theatrics. Badges lock to the top-left corner of the image using `product-badge`, `product-badge-new`, or `product-badge-sale`. No drop shadow — the card reads through negative space rather than elevation.

### Hero
**`hero-banner`** — Full-bleed editorial hero at minimum 560px. A left-directional gradient scrim (`rgba(18,18,18,0.72)` fading to transparent at 40% width) keeps portrait photography readable on the right while protecting white type on the left. Headline runs in `{typography.display-xl}` at 72px/0.95 leading; seasonal campaigns layer in a `{typography.script-accent}` CSBloom line beneath or above the condensed headline for contrast of texture. The primary CTA uses orange fill with white uppercase type. Left-edge padding holds at `{spacing.xl}` from the container boundary at desktop.

**`hero-editorial`** — Lower-voltage section hero in `{colors.surface-sage}` (#e4e5dd) for brand story content, conservation initiatives, or ambassador features. No photography overlay. Headline in `{typography.display-md}`, body in `{typography.body-md}`. Vertical padding uses `{spacing.section}` top and bottom.

### Badges
**`product-badge`** — A zero-radius orange slab label in 11px all-caps Acumin Extra Condensed Bold tracked at 0.8px, used for "FEATURED" or "BESTSELLER" callouts. `product-badge-new` swaps fill to `{colors.ink}` for a dark inversion. `product-badge-sale` uses `{colors.alert}` (#bf0909) to signal price urgency without ambiguity.

### Size & Variant Selection
**`size-chip-available`** — 40px-tall square chip with hairline border and all-caps Acumin Semibold label. `size-chip-selected` fills ink with white type; `size-chip-unavailable` renders stone-gray label on soft background with a strikethrough decoration — still occupying grid space so users understand the full size range even when sold out.

### Search
**`search-bar`** — Square-edged 48px input with hairline border and muted placeholder text. Magnifier icon in `{colors.muted}` sits inside the left padding zone. At mobile breakpoints the search field expands into a full-screen overlay. Typeahead suggestions drop into a `{colors.canvas}` panel using `{typography.body-sm}` result rows, with keyword matches highlighted in `{colors.primary}` orange.

### Filters
**`filter-chip`** and **`filter-chip-active`** — 2px-radius chips for PLP facet filters. Inactive chips use a hairline border on white canvas. Active chips invert to `{colors.ink}` fill with white caption text. The near-zero rounding keeps them consistent with the brand's sharp interface grammar while still reading as toggleable selectors.

### Category Tile
**`category-tile`** — Full-bleed photography tile with a bottom-up gradient scrim from `rgba(40,40,36,0.78)` to transparent. Category name in `{typography.display-sm}` Acumin Extra Condensed Bold, white. A small all-caps `{typography.button-sm}` shop label anchors below the name. Used in grid layouts routing visitors to Waders, Outerwear, Wading Boots, and Accessories.

### Technical Spec Panel
**`wader-spec-panel`** — A `{colors.surface-soft}` panel with a 2px `{colors.primary}` orange top border as its only brand accent. Label/value pairs display spec data — material weight, waterproof rating, seam construction — in `{typography.caption}` / `{typography.title-sm}` stacks. Zero rounding, `{spacing.lg}` internal padding. Appears on wader and outerwear PDPs anchored below or beside the product description block.

### Announcement Bar
**`alert-bar`** — Single-line `{colors.ink}` bar at the very top of the page above the utility nav. Centered `{typography.body-sm}` copy in white; inline links use `{colors.primary}` orange. Used for shipping thresholds, limited-edition drops, and seasonal promotions. Dismisses with a close icon on the right edge.

### Footer
**`footer`** — Dark (#282824) footer with `{typography.title-sm}` column headings in white and `{typography.body-sm}` links in stone gray (#989990) lightening to white on hover. Divider rules between columns use `{colors.olive}`. Newsletter input inverts `text-input` styling against the dark surface — white border, white placeholder, transparent fill. Social icon row in `{colors.stone}` sits above the legal baseline copy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger replaces nav link row; hero switches to portrait crop at 100vw with headline scaling to `{typography.display-lg}`; filter chips collapse behind a "Filter" drawer trigger; search expands to full-screen overlay |
| Tablet | 744–1128px | Two-column product grid; nav retains full link row in condensed spacing; hero headline scales to `{typography.display-lg}`; category tiles switch to 2×2 grid |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav-bar with utility bar above; hero at full 560px+ with left-aligned text block; wader-spec-panel appears inline beside product images |
| Wide | > 1440px | Content capped at 1440px centered on `{colors.canvas}`; side margins increase proportionally; hero headline may reach full `{typography.display-xl}` at 72px |

### Touch Targets
- All size chips and swatches minimum 40px height / 40px width
- Nav-bar links padded to 44px tap zone with extended hit area
- Product card image tap target spans the full image container, not just the title
- Filter drawer uses 48px row height per facet value for thumb-friendly selection
- Hero carousel supports swipe gesture on mobile with dot-position indicators below

### Collapsing Strategy
- Utility bar collapses first at mobile; its links move into the hamburger drawer
- Product grid collapses 4 → 3 → 2 → 1 column across Wide → Desktop → Tablet → Mobile
- Wader-spec-panel shifts below the image carousel on Tablet and Mobile instead of sitting inline
- Footer columns collapse to stacked accordions on Mobile; all links are revealed on expand
- Category tile grid collapses from 4-across to 2-across at Tablet, horizontal scroll row at Mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; nav-bar color (#282824) assumed for mobile browser chrome
- `primary-active` (#a33a15) and `primary-disabled` (#e4a070) are derived approximations — hover and disabled states were not confirmed from live DOM inspection
- CSBloom is present in the font stack but its precise size scale and usage contexts in production could not be confirmed; treat `{typography.script-accent}` values as informed estimates
- Exact nav-bar height (56px) and utility-bar height (36px) were inferred from visual inspection, not measured DOM values
- Button border-radius behavior (`{rounded.none}` vs `{rounded.xs}`) was inferred from brand aesthetic; computed values were not captured from the live stylesheet
- Animation timing curves for card hover zoom, drawer transitions, and hero carousel were not surfaced in extraction
- Dark mode support, if any, was not identified in the extracted color set
- Swiper-icons is present as a font stack entry, indicating a carousel component; exact pagination dot styling and transition behavior are unknown
