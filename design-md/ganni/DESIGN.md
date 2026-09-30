---
version: alpha
name: "Ganni"
source_url: "https://ganni.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Three navy depths — #28356a, #22284f, #15195a — stack in GANNI's extracted palette like progressive denim washes, a deliberate chromatic build that anchors every call-to-action and navigation element against a warm, sand-toned field. A taupe (#cac3bd) leads the extraction in visual weight, materializing at borders, divider lines, and skeletal states — not a background throwaway but the brand's ambient temperature, the digital equivalent of undyed heavy linen that recurs across runway set design and product photography props. The Danish label's Shopify storefront operates as a gallery container: near-white surfaces (#f3f3f3, #f0f0f0) and near-black type (#111111, #231f20) stand back so that seasonal imagery — neon tulip prints, cobalt vinyl minis, sequin-heavy knits — carries all visual brightness without the interface competing.

  Rounded corners register almost as an afterthought. Product cards sit at near-zero radius ({rounded.none} or {rounded.xs}), CTAs render as rectangular slabs rather than the pill shapes common to softer lifestyle brands, and text inputs use minimal rounding consistent with {rounded.xs}. This keeps the layout vocabulary aligned with print editorial — a Scandinavian-modernist grid density, tight tracking, and generous negative space — rather than consumer-app softness. No font families were extractable from the live site (likely assembled via a client-side JS bundle), but GANNI's brand materials and editorial history consistently signal a grotesque sans-serif at modest weights: display copy at 500–600, body at regular 400, letterSpacing kept tight to neutral. Button labels run uppercase at smaller hierarchy tiers and sentence-case at primary-action level, avoiding the slab-serif and ornamental flourishes of Parisian heritage houses.

  The announcement bar rotates sustainability messaging alongside seasonal promotions — GANNI's "Dun[no] about good, doing less bad" positioning surfaces in digital copy before product. Badges are minimal and monochrome rather than fluorescent sticker-energy. Footer architecture is link-dense and compact, deprioritizing marketing prose in favor of navigation depth and country-selector access.

colors:
  primary: "#28356a"
  primary-active: "#15195a"
  primary-disabled: "#8d95b0"
  ink: "#111111"
  body: "#231f20"
  muted: "#6e6b68"
  hairline: "#f0f0f0"
  hairline-strong: "#cac3bd"
  canvas: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#f0f0f0"
  on-primary: "#ffffff"
  sand: "#cac3bd"
  navy-mid: "#22284f"
  navy-deep: "#15195a"

typography:
  display-xl:
    fontFamily: "'HelveticaNow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'HelveticaNow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'HelveticaNow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'HelveticaNow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'HelveticaNow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'HelveticaNow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'HelveticaNow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'HelveticaNow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'HelveticaNow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'HelveticaNow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'HelveticaNow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  label-uppercase:
    fontFamily: "'HelveticaNow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  announcement:
    fontFamily: "'HelveticaNow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  price:
    fontFamily: "'HelveticaNow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0

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
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 13px 23px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline-strong}"
    borderFocused: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.announcement}"
    padding: 10px 16px
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    imageBorder: none
    productNameTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    gap: 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  badge-sale:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  badge-sustainability:
    backgroundColor: "{colors.sand}"
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline-strong}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    height: 40px
    unavailableTextColor: "{colors.muted}"
    unavailableDecoration: line-through
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-strong}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    minHeight: 600px
    textAlign: left
  newsletter-capture:
    backgroundColor: "{colors.sand}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 48px 32px
  quick-add:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    height: 40px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headingTypography: "{typography.label-uppercase}"
    linkTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline-strong}"
    columnGap: 32px
    padding: 48px 0

## Components

### Buttons

**`button-primary`** — A flat navy (#28356a) slab with no border radius, uppercase tracking at 0.5px, and 48px height. Active state deepens to #15195a; disabled renders in the muted slate #8d95b0. There is no hover shadow or lift effect — color-shift alone signals state, consistent with the brand's anti-ornament posture.

**`button-secondary`** — White fill with a 1px navy border and matching navy text, same sharp-cornered silhouette as primary. Provides clear hierarchy contrast on light surfaces without resorting to ghost or tonal variants. On hover, background transitions to a faint surface-soft (#f3f3f3).

**`button-ghost`** — Transparent background, black text, no border. Used for navigation-level actions and editorial CTAs within hero modules where surrounding imagery provides enough contrast context.

### Text Input

**`text-input`** — Zero border radius, 1px hairline-strong (#cac3bd) border at rest tightening to 1px ink (#111111) on focus. Placeholder in muted gray (#6e6b68). The sharp corners align with product-card and button geometry, maintaining a unified editorial grid across interactive elements.

### Navigation

**`nav-bar`** — White canvas, 56px tall, 1px hairline bottom border. Links run at 14px/400 weight with no decoration until hover, where an underline or color shift signals interaction. The logo anchors center or left depending on viewport; a hamburger collapses the full category tree on mobile. No sticky behavior by default — the page scrolls under the nav, keeping full image bleed on hero modules.

**`announcement-bar`** — Deep navy (#28356a) band above the nav, 13px announcement type in white, centered. Rotates sustainability copy and promotional messaging. Height is fixed at roughly 40px; on mobile it may wrap to two lines before collapsing to a dismissible drawer.

### Product Card

**`product-card`** — Zero border radius, 3:4 portrait aspect ratio for imagery, no visible card border or shadow. Product name in body-sm (14px/400), price in price style (14px/500). On hover, a quick-add bar slides up from the bottom of the image at 40px height, or an alternate colorway swatch row appears. Badge overlays (badge-new, badge-sale) anchor top-left at absolute position.

### Badges

**`badge-new`** — Navy rectangle, uppercase label at 11px/500 with 1px letter-spacing, no radius. **`badge-sale`** — Identical geometry in near-black (#111111). **`badge-sustainability`** — Sand (#cac3bd) fill with ink text, used for responsible-material callouts. All three use the same zero-radius slab and label-uppercase type.

### Size Selector

**`size-selector`** — 40px-tall rectangular tiles with 1px hairline-strong borders in rest state. Selected tile inverts to primary navy fill with white text. Unavailable sizes render in muted gray with a line-through decoration rather than being hidden, preserving the size-range context for fit reference.

### Filter Chips

**`filter-chip`** — Outlined rectangular chips (1px hairline-strong border, 0px radius) that invert to full-ink fill on active selection. Body-sm type. The chip row sits in a sticky-top position within the product listing page and scrolls horizontally on mobile before wrapping.

### Hero Banner

**`hero-banner`** — Full-bleed image or video with overlaid text anchored bottom-left or center-left. Headline in display-xl (48px/500), subhead in body-md, CTA as button-primary. On editorial campaigns the text panel may be isolated white-background column occupying the right 40% of a split layout, leaving the image uncropped.

### Newsletter Capture

**`newsletter-capture`** — Sand (#cac3bd) fill module, zero radius, title-md headline, body-sm supporting copy, a text-input row paired inline with a button-primary. The warm sand ground differentiates this block from the white/light-gray page sections without switching to a dark theme.

### Footer

**`footer`** — White canvas, four to five link columns using label-uppercase headings and body-sm links. A 1px hairline-strong top border provides the only structural divider. The bottom row contains legal copy in caption size plus country/language selector and payment badge icons (Visa, Mastercard, Amex — not brand colors).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav collapses full category tree; announcement bar may wrap to two lines; hero text anchors bottom with translucent scrim; filter chips scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + hamburger or partial link row; hero switches to split 50/50 layout; newsletter capture stacks vertically |
| Desktop | 1128–1440px | Three or four-column product grid; full horizontal nav with dropdown mega-menus; hero at full 600px+ min-height; filter bar sticky below nav |
| Wide | > 1440px | Max-width container (~1440px) centered; product grid may expand to five columns; hero imagery scales without cropping via object-fit cover |

### Touch Targets

- All interactive elements (buttons, size tiles, filter chips) meet 40px minimum height on mobile
- Quick-add and badge overlays on product cards activate on tap rather than hover; a secondary tap confirms add-to-cart
- Nav drawer links have 48px row height with full-width tap area
- Size selector tiles are at least 40×40px; unavailable tiles remain tappable to show a restock notification entry

### Collapsing Strategy

- Navigation collapses to a full-screen drawer at < 744px; top-level categories are expandable accordion rows
- Product filters move from a sidebar (desktop) to a bottom-sheet modal (mobile) triggered by a "Filter & Sort" fixed bar
- Hero banners use a vertical stacked layout on mobile (image above, text below) rather than overlaid text to preserve readability without requiring scrim overlays
- Footer columns collapse to a single-column accordion list on mobile; country selector moves to a standalone row above legal copy

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font families were extractable from the live site; the typography stack (`'HelveticaNow', 'Helvetica Neue', Helvetica, Arial, sans-serif`) is inferred from GANNI's brand materials and editorial history — verify against the actual web font loaded in DevTools
- Exact font weights and sizes for display and body type are approximated; GANNI may use a custom-licensed grotesque or a variable-weight variant not identifiable without direct inspection
- `primary-disabled` (#8d95b0) and `muted` (#6e6b68) were not directly extracted and are derived approximations — confirm against actual disabled-state renders
- Several extracted hex values (#ff5f00, #eb001b, #f79e1b, #006fcf, #298fc2) appear to be Mastercard, Visa, and AmEx payment-badge colors rendered in the checkout footer, not brand colors; they are excluded from the palette
- Hover transition durations and easing curves (likely 150–200ms ease) could not be extracted
- The exact height and behavior of the sticky filter bar on PLP pages (whether it collapses on scroll or remains fixed) requires live QA
- Dark-mode or seasonal-theme overrides (GANNI occasionally ships campaign-specific color moments) are not captured here
