---
version: alpha
name: "Agmes"
source_url: "https://www.agmesnyc.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every element on agmesnyc.com arrives without color — five near-achromatic tones spanning near-black (#121212) through silver-gray (#dedede) to cream (#fafafa), with nothing between that could upstage the jewelry itself. Agmes treats the interface as a museum wall: achromatic, recessive, constructed to hold light rather than emit it. The pieces carry all chromatic weight; the site declines the offer to compete. Raleway provides the typographic spine, set at ultralight weights — 200 for display, 300 for subheadings — with letter-spacing pushed to 0.10–0.18em. Headlines feel less like names than dimensions stamped on a studio sample tag, and uppercase tracking governs every label, navigation link, and call-to-action with consistent studio-quiet authority. No headline shouts; each reads like engraving.

  The Shopify storefront organizes around product photography on near-white (#fafafa) grounds with minimal ornamentation — no colored badges, no promotional callouts. Product cards carry image, name in {typography.title-md}, and price in {typography.price-display}. Primary CTAs use full near-black (#191919) as a solid fill with cream type, a deliberate value reversal that makes the add-to-cart button read as a steel stamp on linen. Secondary interactions arrive as hairline-bordered outlines ({colors.hairline}) that dissolve into the surface rather than asserting themselves. Radius vocabulary stays restrained — corners lean toward {rounded.none} or at most {rounded.xs}, echoing the angular silhouettes of the pieces themselves.

  PDP pages breathe with wide vertical margins and screen-height heroes, letting a single pendant float in negative space before descriptive copy appears below. Material and edition labels carry the monospace fallback that surfaces in the font stack — an artifact of artisan-inventory logic meeting Shopify's template layer, and a texture that makes a product specification feel like a laboratory annotation. Spacing is generous throughout: {spacing.section} gutters between editorial zones signal a brand that considers silence between words as load-bearing as the words themselves.

colors:
  primary: "#191919"
  primary-active: "#121212"
  primary-disabled: "#dedede"
  ink: "#191919"
  body: "#555555"
  muted: "#777777"
  hairline: "#dedede"
  canvas: "#fafafa"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#fafafa"
  mid-gray: "#777777"
  dark-gray: "#555555"

typography:
  display-xl:
    fontFamily: "Raleway, sans-serif"
    fontSize: 44px
    fontWeight: 200
    lineHeight: 1.12
    letterSpacing: 0.14em
  display-md:
    fontFamily: "Raleway, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.22
    letterSpacing: 0.10em
  display-sm:
    fontFamily: "Raleway, sans-serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0.08em
  title-md:
    fontFamily: "Raleway, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.18em
    textTransform: uppercase
  title-sm:
    fontFamily: "Raleway, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.20em
    textTransform: uppercase
  body-md:
    fontFamily: "Raleway, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.70
    letterSpacing: 0.02em
  body-sm:
    fontFamily: "Raleway, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.02em
  caption:
    fontFamily: "Raleway, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0.14em
    textTransform: uppercase
  price-display:
    fontFamily: "Raleway, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.05em
  button-md:
    fontFamily: "Raleway, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.20em
    textTransform: uppercase
  button-sm:
    fontFamily: "Raleway, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.18em
    textTransform: uppercase
  nav-link:
    fontFamily: "Raleway, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.18em
    textTransform: uppercase
  label-sm:
    fontFamily: "Raleway, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.22em
    textTransform: uppercase
  material-mono:
    fontFamily: "monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.04em

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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 44px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageBackground: "{colors.surface-soft}"
    nameTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    nameColor: "{colors.ink}"
    priceColor: "{colors.body}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
    padding: "{spacing.md}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 100vh
    textAlign: center
    letterSpacing: 0.14em
    padding: "{spacing.section}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    paddingBottom: "{spacing.xxl}"
    borderBottom: "1px solid {colors.hairline}"
  product-pdp:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.display-sm}"
    priceTypography: "{typography.price-display}"
    descTypography: "{typography.body-md}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.body}"
    descColor: "{colors.body}"
    gap: "{spacing.xxl}"
    sectionPadding: "{spacing.section}"
  material-tag:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.material-mono}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  edition-label:
    backgroundColor: "transparent"
    textColor: "{colors.mid-gray}"
    typography: "{typography.label-sm}"
    letterSpacing: 0.22em
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderLeft: "1px solid {colors.hairline}"
    width: 400px
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.hairline}"
    typography: "{typography.nav-link}"
    linkTypography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.section}"
    borderTop: none
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.display-md}"
    placeholderColor: "{colors.hairline}"
    border: none
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xxl}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    height: 36px
    textAlign: center

## Components

### Buttons
**`button-primary`** — Solid near-black (#191919) fill with cream (#fafafa) uppercase Raleway text at 0.20em letter-spacing and zero corner radius; reads as a steel stamp on the canvas rather than a conventional CTA. Active state deepens to #121212; disabled state flattens to the hairline gray (#dedede) with muted text. Height is fixed at 44px with generous horizontal padding (32px) to give the letterforms room to breathe.

**`button-secondary`** — Transparent fill with a 1px solid ink border; the same uppercase Raleway button-md typography as primary, creating a sibling pair where one is filled and one is outlined. On hover the border steps to primary-active weight without color shift. Never rounded.

**`button-ghost`** — The soft interaction button: hairline border (#dedede), muted text, used for tertiary actions like "View More" or filter chips. Disappears into the surface by design; only visible on close inspection.

### Navigation
**`nav-bar`** — 60px tall, canvas background, hairline bottom border. The wordmark "AGMES" in display-sm Raleway at light weight sits centered or left; navigation links in nav-link style (11px, uppercase, 0.18em tracking) float right. On scroll the bar remains static — no color shift, no shadow.

**`nav-dropdown`** — Appears on hover over collection categories; canvas background with hairline border, body-sm type in dark-gray. No animation beyond a simple opacity transition. Sub-items are plain links with muted hover state.

### Product Grid & Cards
**`product-card`** — Image fills the top of the card on a surface-soft (#fafafa) background that matches the page ground, making the piece appear to float rather than sit in a container. Below: product name in title-md uppercase tracking, price in price-display. No badge overlays, no hover-second-image behavior unless JavaScript is active. Strictly zero corner radius.

**`product-pdp`** — Left column holds a stacked image gallery; right column holds title in display-sm, price in price-display, material tags, size selectors, and the primary CTA. Vertical rhythm uses xxl spacing between each content block. A material-tag row reads like a laboratory annotation — monospace font, hairline border, muted text.

### Material & Edition Tags
**`material-tag`** — Monospace type (11px, #777777) inside a hairline-bordered no-radius chip. Labels like "14K GOLD" or "STERLING SILVER" appear here. The font-family switch from Raleway to monospace is deliberate: it reads as specification data, not editorial copy.

**`edition-label`** — Plain uppercase Raleway at 10px, 0.22em spacing, mid-gray (#777777), no border. Used for edition counts or "HANDMADE IN NYC" callouts; floats above or below the product title.

### Hero
**`hero-banner`** — Full-viewport-height, canvas background, centered text. Headline in display-xl (44px, weight 200, 0.14em tracking) reads as a whisper at scale. Subtext in body-md below. No overlay, no video background — the hero is typographic, not photographic. The near-white ground and pale letterforms create extremely low contrast, which is intentional: the brand values understatement over announcement.

### Cart & Search
**`cart-drawer`** — Slides in from the right, 400px wide, canvas background, 1px hairline left border. Item rows use body-sm. No rounded corners anywhere in the drawer. The close button is a plain text "×" in ink, not an icon.

**`search-overlay`** — Full-width overlay with canvas background. Input text renders in display-md Raleway (28px, weight 300) — you type into a giant letterform field. Placeholder in hairline gray. A 1px hairline bottom border on the input field is the only decoration.

### Footer
**`footer`** — Reverses the site's value: near-black (#191919) background with cream (#fafafa) text, mirroring the primary button's color logic at page scale. Navigation links in caption style; legal text in label-sm. No rounded treatment; the footer is a flat ink block.

### Announcement Bar
**`announcement-bar`** — 36px tall strip in near-black (#191919) above the nav, cream text in label-sm uppercase tracking. Used for shipping thresholds or collection launches. Disappears cleanly on mobile scroll.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger icon + wordmark; hero headline drops to display-md (28px); PDP stacks image above details full-width; cart drawer goes full-width |
| Tablet | 744–1128px | Two-column product grid; nav shows wordmark + hamburger; hero text scales to display-md at 32px; PDP uses 55/45 split |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with category links visible; hero headline at full display-xl (44px); PDP in 50/50 split with sticky add-to-cart |
| Wide | > 1440px | Grid caps at 1400px max-width, centered; four-column product grid optional; hero gains more top/bottom breathing room via increased section spacing |

### Touch Targets
- All buttons hold minimum 44px height on mobile; the add-to-cart button stretches full width on screens < 480px
- Navigation links in the mobile drawer are padded to at least 48px vertical tap height
- Material tag chips are 36px tall minimum on mobile to remain tappable despite small type

### Collapsing Strategy
- The announcement bar hides on mobile scroll-down to reclaim vertical space
- Product card text truncates to one line for name, one line for price — never wraps to three lines
- Footer columns stack vertically on mobile; the ink-block full-width treatment is preserved at all breakpoints
- Nav dropdown becomes a full-screen accordion on mobile; hover states become tap-toggle states

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No accent or brand-signature color was detected; the entire extracted palette is achromatic (#121212 through #fafafa). It is possible the brand intentionally uses zero chromatic color, but a warm metal tone (gold/brass for fine jewelry) may exist in imagery-only contexts and was not captured in CSS/token extraction.
- `surface-card: "#ffffff"` is a minor extrapolation — pure white was not in the extracted palette (nearest is #fafafa). Likely used for product image backgrounds in Shopify's Dawn or similar theme.
- `surface-soft: "#fafafa"` is shared with `canvas`; a subtle distinction between page ground and card ground may exist in practice but could not be resolved from extraction.
- Font weights below 300 (Raleway 100/200) were inferred from fine-jewelry brand conventions and Raleway's available weight range; exact weight usage per element was not confirmed from CSS extraction.
- No specific border-radius values were extracted from the live site; {rounded.none} assumption is based on the brand's angular jewelry aesthetic and monochromatic austerity, not confirmed CSS measurement.
- No motion or transition timing data was extracted (hover durations, drawer animation curves).
- Icon set and glyph style (outline vs. filled, stroke weight) are unknown; fine jewelry brands often use custom SVG sets with thin strokes that match the Raleway weight register.
