---
version: alpha
name: "Aurate New York"
source_url: "https://www.auratenewyork.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every Aurate product photograph rests on warm cream (#efeae6), a surface that lets 14-karat gold catch afternoon warmth rather than studio flash. The brand's structural color is not gold but a deep apothecary green (#304038) — applied to primary CTAs, main navigation, and the full-width footer mass with a botanical steadiness that reads as permanence rather than trend. A complete sage family fans behind it: #42544f for hover states and section grounds, #739487 for mid-tonal icons and dividers, #bfccb8 as a wash behind sustainability callouts, and the near-white mint #e6f7f4 anchoring ethical-sourcing storytelling panels. Gold enters the palette precisely and without fanfare — #b26118 highlights price figures and collection badge fills, #c27030 warms hover states, and #ffd196 lightens into chip backgrounds — always proportionate, never decorative for its own sake.

  Canvas temperature shifts deliberately between the warmer cream (#efeae6) for editorial landing moments and the cooler paper tone (#f5f2f0) for utility zones, with near-white cards (#fdfcfc) providing a clean lift above either ground without needing a drop shadow. Typography relies on system font stacks — no custom typeface was captured in extraction, suggesting a branded web font loads post-JavaScript hydration. The visible rhythm reads light and unhurried: display copy at 28–36px weight 400–500 with near-zero letter-spacing; product detail labels in uppercase 10–11px with wide tracking — a fine-jewelry convention that lets the piece, not the label, carry authority.

  Corner geometry is restrained. Product cards sit at `{rounded.sm}`, buttons at `{rounded.sm}`, quantity steppers and search inputs at `{rounded.xs}`, and material-type badges at `{rounded.full}`. Spacing between major sections runs at `{spacing.section}` (64px); internal product grid gutters compress to `{spacing.sm}` (8px), preserving editorial breathing room at the macro level while packing catalog SKUs efficiently. A cluster of brand-signature components — the sustainability banner, material-quality badge row, and sticky add-to-cart strip — distinguishes Aurate's interface vocabulary from mass-market jewelry retail and must render intact to carry the brand's proposition that fine and responsible are the same thing.

colors:
  primary: "#304038"
  primary-active: "#42544f"
  primary-disabled: "#bfccb8"
  accent-gold: "#b26118"
  accent-gold-hover: "#c27030"
  accent-gold-light: "#ffd196"
  ink: "#272727"
  body: "#5f6a66"
  muted: "#9b9b9b"
  hairline: "#e8e8e8"
  hairline-soft: "#eaeaea"
  canvas: "#efeae6"
  surface-soft: "#f5f2f0"
  surface-card: "#fdfcfc"
  surface-mint: "#e6f7f4"
  sage-mid: "#739487"
  sage-light: "#bfccb8"
  sage-deep: "#42544f"
  on-primary: "#ffffff"
  error: "#ea0202"

typography:
  display-xl:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label-uppercase:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
  price-display:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0.3px

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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.accent-gold}"
    padding: "{spacing.sm}"
    gap: "{spacing.sm}"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    paddingY: "{spacing.section}"
    minHeight: 600px
  sustainability-banner:
    backgroundColor: "{colors.surface-mint}"
    textColor: "{colors.primary}"
    typography: "{typography.label-uppercase}"
    paddingY: "{spacing.md}"
    borderTop: "1px solid {colors.sage-mid}"
    borderBottom: "1px solid {colors.sage-mid}"
  material-badge:
    backgroundColor: "{colors.sage-light}"
    textColor: "{colors.primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  gold-karat-badge:
    backgroundColor: "{colors.accent-gold-light}"
    textColor: "{colors.accent-gold}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  price-display-block:
    textColor: "{colors.accent-gold}"
    typography: "{typography.price-display}"
    saleColor: "{colors.error}"
    strikeThroughColor: "{colors.muted}"
  sticky-add-to-cart:
    backgroundColor: "{colors.surface-card}"
    borderTop: "1px solid {colors.hairline}"
    ctaComponent: "button-primary"
    paddingY: "{spacing.md}"
    paddingX: "{spacing.base}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    selectedBackground: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    unselectedTextColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 40px
  quantity-stepper:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    height: 40px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  collection-filter-pill:
    backgroundColor: "{colors.canvas}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.sage-light}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-uppercase}"
    paddingY: "{spacing.xxl}"
    paddingX: "{spacing.xl}"

## Components

### Buttons

**`button-primary`** — Forest-green (#304038) fill with white type at `{typography.button-md}`, 48px height, padded to 14px/32px at `{rounded.sm}` radius. Carries every primary conversion action: add to cart, complete purchase, shop the collection. Active state deepens fill to #42544f; disabled drapes the pale sage `{colors.primary-disabled}` at 0.6 opacity to retire the action visually without resorting to a flat gray block.

**`button-secondary`** — Transparent fill with a 1px `{colors.primary}` border and matching green type. Matches the primary's height and radius for visual parity in split-CTA layouts. Used on editorial landing sections for non-converting navigation — "Explore the collection", "Learn about our process" — and on the PDP alongside the primary add-to-cart. Active state adds `{colors.canvas}` background fill to confirm the hover.

**`button-ghost`** — Underlined text only, no border or background, type weight 500. Appears in footer navigation, inline editorial links, and secondary drawer actions. The underline distinguishes it from passive copy without competing with bordered CTAs.

### Text Input

**`text-input`** — 48px height on `{rounded.xs}` with a 1px `{colors.hairline}` border at rest, sharpening to `{colors.primary}` on focus. Placeholder in `{colors.muted}`; text in `{colors.ink}`. Used in email capture modules, account creation, and checkout. The low-contrast resting border suits the warm canvas environment — the input announces itself on interaction rather than at rest.

### Navigation

**`nav-bar`** — Near-white (#fdfcfc) background, 64px height, soft `{colors.hairline-soft}` bottom rule. Navigation links at `{typography.nav-link}` (13px / 0.3px tracking) feel editorial without being precious. The forest-green wordmark anchors left; search, account, and cart icons cluster right at 44×44px tap targets. On scroll, the bar may pick up a subtle box-shadow to reinforce the sticky layer.

### Product Card

**`product-card`** — Borderless card at `{rounded.sm}` on `{colors.surface-card}`, portrait image ratio 3:4 standard to jewelry close-up photography. Title in `{typography.title-sm}`; price in `{typography.price-display}` colored `{colors.accent-gold}`. No shadow needed — the warm cream canvas creates natural separation. Hover state may swap to a second product image and surface a quick-add button using `button-secondary`.

### Hero

**`hero-editorial`** — Full-bleed section on `{colors.canvas}` with headline in `{typography.display-xl}` and body copy in `{typography.body-md}`, padded `{spacing.section}` top and bottom, minimum 600px height. The primary CTA uses `button-primary`. Photography bleeds to the container edge on desktop; text column stacks above the image on mobile.

### Badges and Labels

**`material-badge`** — Sage-wash pill (`{colors.sage-light}` fill, `{colors.primary}` text) in `{typography.label-uppercase}` at `{rounded.full}`. Communicates metal type, gemstone name, or material story — "14K Gold", "Lab Diamond", "Recycled Silver". Appears on product cards and at the top of the PDP.

**`gold-karat-badge`** — Same pill shape as `material-badge` but in amber fill (#ffd196) with gold text (#b26118). Used exclusively for karat purity designations and gold-type callouts to preserve the color signal: sage means material category, amber means gold quality.

**`sustainability-banner`** — Full-width strip in `{colors.surface-mint}` with `{colors.primary}` type in `{typography.label-uppercase}`, bordered top and bottom by 1px `{colors.sage-mid}` rules. Communicates recycled-gold sourcing, certifications, and ethical-production facts between editorial sections. Should not be clipped on narrow viewports — the message is core brand positioning.

### Product Detail Page

**`sticky-add-to-cart`** — Fixed bottom bar on mobile (and optionally sticky-on-scroll on desktop) with `{colors.surface-card}` background, 1px `{colors.hairline}` top border, and a full-width `button-primary`. Padding `{spacing.md}` vertical, `{spacing.base}` horizontal. Preserves the add-to-cart action across long PDPs without requiring scroll-back.

**`size-selector`** — 40px-tall rectangular buttons for ring sizes and chain lengths at `{rounded.xs}`. Unselected: `{colors.canvas}` background, `{colors.hairline}` border, `{colors.ink}` text. Selected: `{colors.primary}` fill, `{colors.on-primary}` text, `{colors.primary}` border. Sold-out states show `{colors.muted}` text with a diagonal strikethrough overlay on the button face.

**`quantity-stepper`** — Compact minus/number/plus row on `{colors.surface-soft}` at `{rounded.xs}`, 40px tall. Minus and plus control areas should be padded to 44px effective tap target on mobile. Typography in `{typography.title-sm}`.

**`price-display-block`** — Current price in `{typography.price-display}` at `{colors.accent-gold}`. On sale: current price in `{colors.error}`, original price struck through in `{colors.muted}`. The gold price color is one of the few places the accent-gold family appears in typographic form rather than a filled badge.

### Collection Filtering

**`collection-filter-pill`** — Rounded-full pills for metal type, gemstone, price range, and collection category. Inactive: `{colors.canvas}` fill with `{colors.hairline}` border and `{colors.ink}` text. Active: `{colors.primary}` fill with `{colors.on-primary}` text. Type at `{typography.button-sm}`. On mobile, pills overflow into a horizontal scroll row with no clipping — do not wrap to a second line.

### Search

**`search-bar`** — Soft-fill input on `{colors.surface-soft}` at `{rounded.sm}` with a 1px `{colors.hairline}` border. Opens from a top-anchored drawer overlay on mobile; center-expands in a modal strip on desktop. Placeholder and icon in `{colors.muted}`; typed text in `{colors.ink}`.

### Footer

**`footer`** — Deep forest-green (#304038) full-width block grounding the warm-cream page. White body text, sage-light (#bfccb8) link color. Column headings in `{typography.label-uppercase}`, body links in `{typography.body-sm}`. Newsletter email input uses `text-input` embedded on a slightly lighter green surface. The dark forest-green footer mass reinforces the sustainability positioning — the color itself signals the brand's relationship to the natural world before a word is read.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks text above image; sticky add-to-cart bar active full-width; nav collapses to hamburger + icon trio; filter pills overflow horizontally |
| Tablet | 744–1128px | 2-column product grid; hero switches to side-by-side layout; nav shows top-level labels with dropdown on hover; sticky add-to-cart transitions to inline below image stack |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with flyout mega-menu; PDP uses two-column layout with sticky sidebar add-to-cart |
| Wide | > 1440px | Max-width container centered at 1440px; section padding increases; hero minimum height rises to 720px; product grid locked at 4 columns |

### Touch Targets

- All primary and secondary buttons minimum 48px height
- Size selector pills padded to minimum 44px height on mobile
- Quantity stepper minus and plus controls padded to 44×44px effective tap area
- Nav icon cluster (search, account, bag) each 44×44px
- Filter pills in horizontal scroll row must not clip adjacent targets — add right-padding to the scroll container

### Collapsing Strategy

- Nav: full flyout mega-menu on desktop → hamburger drawer with accordion sub-menus on mobile
- PDP: two-column image gallery + details sidebar on desktop → full-width image swiper + sticky bottom add-to-cart bar on mobile
- Product grid: 4-col → 3-col → 2-col → 1-col across breakpoints
- Footer: 4-column link grid → 2-column → single-column with accordion sections on mobile
- Collection filters: horizontal pill overflow row on mobile; vertical facet panel in sidebar on desktop
- Sustainability banner: single-row on desktop; may wrap to two lines on mobile but must never be hidden

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected — only system font stacks captured. Aurate almost certainly loads a licensed grotesque or editorial serif via JavaScript post-hydration; all typography tokens above use system fallbacks and must be updated when the font name is confirmed.
- Exact button and card border-radius values unconfirmed — `{rounded.sm}` (8px) inferred from visual inspection; may be 0px (fully square) in production for the brand's minimal positioning.
- Hover and focus transition timing (duration, easing curve) not extracted.
- Icon set specification (line weight, stroke vs. fill, size grid) not captured — fine jewelry brands typically use 1px hairline stroke icons.
- Gold accent color application rules (#b26118 vs. #c27030 vs. #ffd196) inferred from extracted color ordering, not confirmed from computed styles on specific elements.
- Modal, drawer, and overlay scrim color not extracted.
- Mobile nav drawer background and animation behavior unknown.
- Product image zoom implementation and lightbox behavior not captured.
- Typography weight usage at different breakpoints (some brands lighten heading weight on mobile) not confirmed.
