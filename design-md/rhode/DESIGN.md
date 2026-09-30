---
version: alpha
name: "Rhode"
source_url: "https://www.rhode skin.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Glazed-skin close-ups fill the page before the product ever appears — Rhode's art direction treats the formula as the final act, not the subject, letting sun-caught cheekbones and slow-blink video loops carry the brand's warmth before a single ingredient is named. The palette lives in a narrow corridor of roasted cream and near-white: {colors.canvas} (#faf6f0) as the site floor, {colors.surface-soft} (#f4ede1) lifting product cards off the ground, and a near-black {colors.primary} (#1c1c1c) carrying every CTA and the wordmark itself. There is almost no chromatic saturation anywhere on the page — not because the brand is cold, but because pinkish warmth is already embedded in the cream base tones and the photography, making a separate accent hue unnecessary. Type runs in two registers: a classic light-weight serif at display scale that evokes a fashion-magazine masthead rather than a lab panel, and a spare geometric sans for body copy, ingredient lists, and labels. Sizing stays modest — display never pushes past 40px and body holds at 15–16px — which means the grid and photography absorb visual weight rather than headline type. Corners are restrained: most surfaces sit at {rounded.sm} or {rounded.xs}, swatch selectors use {rounded.full} for the small circle forms, and buttons read nearly rectangular in keeping with the editorial restraint. Rhode's signature cylindrical lip case appears as an organizing motif in campaign hero images, shadow-cast product stills, and ingredient-panel illustrations. Generosity lives in spacing rather than in decoration: section gaps run wide, product cards breathe inside a loose grid, and the add-to-cart flow collapses to a single prominent sticky strip on mobile rather than stacking secondary options. Ingredient storytelling panels break the commerce flow with a slower editorial register — large serif headline, short body prose, simple line illustration — signaling a brand comfortable making the user pause rather than accelerating them toward checkout.

colors:
  primary: "#1c1c1c"
  primary-active: "#000000"
  primary-disabled: "#b0a99f"
  ink: "#1c1c1c"
  body: "#3d3936"
  muted: "#8a8178"
  hairline: "#e3d9cd"
  hairline-soft: "#ede5db"
  canvas: "#faf6f0"
  surface-soft: "#f4ede1"
  surface-card: "#faf6f0"
  surface-warm: "#ede5d5"
  on-primary: "#faf6f0"
  blush: "#e8cfc0"
  blush-muted: "#f0ddd3"

typography:
  display-xl:
    fontFamily: "'Times New Roman', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Times New Roman', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Times New Roman', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "Helvetica Neue, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  title-sm:
    fontFamily: "Helvetica Neue, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "Helvetica Neue, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Helvetica Neue, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Helvetica Neue, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.04em
  button-md:
    fontFamily: "Helvetica Neue, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "Helvetica Neue, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "Helvetica Neue, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.06em
  ingredient-label:
    fontFamily: "'Times New Roman', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    iconColor: "{colors.muted}"
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-md}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1:1"
    padding: "{spacing.md}"
    nameTypography: "{typography.body-md}"
    priceTypography: "{typography.price}"
    textColor: "{colors.ink}"
    hoverElevation: "0 4px 16px rgba(0,0,0,0.08)"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    layout: "full-bleed image, text below or overlaid without scrim"
  shade-selector:
    backgroundColor: "{colors.surface-warm}"
    rounded: "{rounded.md}"
    swatchSize: 28px
    swatchRounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.ink}"
    unselectedBorder: "1px solid {colors.hairline}"
    labelTypography: "{typography.caption}"
  ingredient-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headlineTypography: "{typography.ingredient-label}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
    iconSize: 48px
  pdp-gallery:
    backgroundColor: "{colors.canvas}"
    thumbnailRounded: "{rounded.xs}"
    thumbnailSize: 64px
    thumbnailBorder: "1px solid {colors.hairline}"
    activeThumbnailBorder: "2px solid {colors.ink}"
    imageRounded: "{rounded.sm}"
  sticky-atc:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    ctaComponent: "button-primary"
    productNameTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    padding: "{spacing.base} {spacing.lg}"
  badge-new:
    backgroundColor: "{colors.blush}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-sold-out:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  editorial-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    layout: "two-column image + text alternating"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    linkColor: "{colors.ink}"
    typography: "{typography.caption}"
    navTypography: "{typography.title-sm}"
    dividerColor: "{colors.hairline}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons
**`button-primary`** — Near-black (#1c1c1c) fill against the warm cream canvas, with uppercase tracked type at 13px and 4px corners ({rounded.xs}) that read nearly rectangular — the brand's editorial restraint applied to every interactive surface. Active state deepens to true black ({colors.primary-active}); disabled washes to a warm mid-gray ({colors.primary-disabled}) that recedes into the cream ground without alarming contrast.

**`button-secondary`** — Transparent fill with a 1px ink border, matching the primary in height (48px) and type treatment. Provides a ghost alternative for secondary CTAs — "Learn More," "View All," "Read the Story" — without introducing a second fill color.

**`button-text`** — No background, no border, ink text at {typography.button-sm} with underline decoration. Used for low-emphasis navigation links: FAQs, ingredient glossary, shade finder entry points.

### Text Inputs & Search
**`text-input`** — Canvas background, single hairline border ({colors.hairline}) that sharpens to full ink on focus. No shadow, no fill change, no animated label — the form speaks flatly and cleanly. Placeholder runs in {colors.muted}. Height 48px matches buttons so form rows align naturally.

**`search`** — A 40px input strip with the same flat border language as text-input, slightly shorter to distinguish it as a utility rather than a form field. A minimal search icon in {colors.muted} sits at the left edge; the icon turns ink on focus.

### Navigation
**`nav-bar`** — 60px strip on {colors.canvas} with a barely-visible bottom divider ({colors.hairline-soft}). The wordmark "rhode" appears in a light serif ({typography.display-md}, weight 400) — the low weight is intentional, keeping the logo from reading as a shout. A secondary category row runs beneath on desktop; on mobile the whole nav collapses to a hamburger drawer with the wordmark centered.

### Product Cards
**`product-card`** — Set on {colors.surface-soft} with {rounded.sm} corners and square-cropped photography. Name in {typography.body-md} and price in {typography.price} appear below the image with no bolding — neither stat competes with the image. Hover lifts the card with a 4px shadow at 8% black opacity. Sold-out state places the badge-sold-out chip at the image's lower-left corner without dimming the photo.

### Hero
**`hero`** — Full-bleed photography with type overlaid or set below in a constrained text column. Headline runs in the serif display ({typography.display-xl}, 40px weight 400) — the deliberately light weight prevents type from competing with the photograph. No gradient scrim or overlay tint; images are art-directed to allow dark ink text to read cleanly.

### Shade Selector
**`shade-selector`** — A horizontal row of 28px circle swatches ({rounded.full}) keyed to each SKU's actual pigment. Selected state: 2px ink border ring. Resting state: 1px {colors.hairline} ring. The shade name label runs in {typography.caption} below the swatch row. Appears on PDP and inside quick-add overlays on collection pages.

### Ingredient Panel
**`ingredient-panel`** — An editorial pause mid-PDP or on campaign pages: {colors.surface-soft} block with generous {spacing.xxl} padding, an oversized serif headline ({typography.ingredient-label}), short prose ({typography.body-sm}), and a 48px line-drawn ingredient illustration. The component deliberately does not look like a conversion block — it signals a brand comfortable with making a user slow down and read.

### PDP Gallery
**`pdp-gallery`** — Primary image fills 100% width on mobile or 55% column on desktop. A 4-thumbnail strip sits vertically on the left edge on desktop (each 64px square, hairline border, ink outline on active) and migrates to a horizontal scroll row below the main image on mobile. Image corners at {rounded.sm}.

### Sticky Add-to-Cart
**`sticky-atc`** — Appears once the user scrolls past the inline ATC button. A 1px top border on {colors.canvas} carrying product name ({typography.title-md}), price ({typography.price}), and the primary CTA button. Padding is compact ({spacing.base} vertical) so it consumes the minimum bar of screen real estate while remaining tappable.

### Badges
**`badge-new`** — Soft blush fill ({colors.blush}), ink text, pill shape ({rounded.full}), uppercase tracked type ({typography.title-sm}). Applied at the upper corner of product card images for recently launched SKUs.

**`badge-sold-out`** — Warm surface fill ({colors.surface-warm}), muted text, identical pill form. Layered at the lower-left of product card images; does not obscure the photography.

### Editorial Callout
**`editorial-callout`** — Two-column section (alternating image left / image right) used on the homepage and ingredient story pages. Serif headline ({typography.display-lg}, 32px), body prose ({typography.body-md}), {colors.surface-soft} ground, and {spacing.section} top-and-bottom padding — the breathing room is the design signal that this is content, not a promotional block.

### Footer
**`footer`** — {colors.surface-warm} ground with a newsletter capture at top (using the text-input and button-primary components), column links in {typography.caption}, and section headings in {typography.title-sm}. Columns divided by {colors.hairline} rules. Legal and policy links run in {typography.caption} at the lowest row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer + centered wordmark; hero is full-bleed 100vw image with text below; shade selector scrolls horizontally; sticky ATC fills full width |
| Tablet | 744–1128px | 2-column product grid; nav shows category links in a single row; hero switches to 50/50 image-text split; editorial callouts maintain two columns |
| Desktop | 1128–1440px | 3-column product grid; PDP gallery moves to vertical thumbnail strip on left; ingredient panels sit two-column; nav gains secondary category row beneath the wordmark bar |
| Wide | > 1440px | Container max-width ~1440px centers content; product grid may expand to 4 columns; hero image capped to avoid excessive stretch on ultrawide viewports |

### Touch Targets
- All buttons are minimum 48px tall regardless of label length
- Shade swatches (28px visual diameter) are wrapped in a 44×44px tap zone
- Nav icons on mobile use 44×44px touch regions regardless of icon size
- PDP thumbnail strip items on mobile have a minimum 44px touch width
- Badge chips are non-interactive; their parent card surface is the tap target

### Collapsing Strategy
- Primary nav links collapse into a slide-in drawer on mobile; wordmark stays centered in the 60px bar
- PDP gallery thumbnails move from a vertical left rail (desktop) to a horizontal scroll strip below the main image (mobile)
- Ingredient panels reflow from two-column (image + text) to single stacked column on mobile, image above
- Editorial callouts stack image above text on mobile; two-column lock restores at 744px
- Footer columns collapse to an accordion list on mobile with {typography.title-sm} section headers as toggles

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the Rhode site did not expose palette tokens via meta theme-color or static CSS at extraction time. All color values in this file are approximated from widely-circulated brand photography and design coverage; the true computed palette may differ, particularly for {colors.canvas}, {colors.surface-soft}, and {colors.blush}.
- **No font families extracted** — zero font-family stacks detected in the page source. Typography choices (light-weight serif display, geometric sans body) are inferred from brand imagery and design coverage, not confirmed from source code. Rhode may use a proprietary or licensed display typeface rather than system serif fallbacks.
- **Exact button corner radius** — {rounded.xs} (4px) is approximated from visual inspection of screenshots; the live computed value may be 0px (fully rectangular) or up to {rounded.sm} (8px).
- **Primary accent existence** — it is possible Rhode uses a secondary warm accent (a desaturated blush or terracotta) for promotional moments not captured here; {colors.blush} is a best-approximation placeholder.
- **Individual product shade hex values** — per-SKU swatch colors for lip cases and tinted products are not enumerated; these should be sourced from Shopify product metafields or the brand's internal color system at build time.
- **Motion and animation tokens** — hover transitions, scroll-triggered text reveals, and hero video loop behavior are noted qualitatively but not captured as numeric duration/easing tokens.
- **Dark mode** — no evidence of a dark mode variant; all surface and canvas tokens assume light-mode-only operation.
