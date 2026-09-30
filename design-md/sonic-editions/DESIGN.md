---
version: alpha
name: "Sonic Editions"
source_url: "https://www.soniceditions.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Crimson edition stamps (#ce051d) break the surface of an otherwise monastic gallery — every product page uses this single voltage against archival paper tones (#f7f5f2, #e7e4da) that read less like a web store and more like unfolding an envelope of print stock. Canela-Light carries all display and editorial typesetting, its airy thin serifs evoking museum wall text rather than retail headline hierarchy; HelveticaNowPro handles the commerce layer — prices, CTAs, navigation — keeping the transactional register clean and separate from the curatorial one. The palette divides cleanly into three registers: the crimson primary for edition count badges and primary actions; a family of dark navy-slates (#272d45, #676986, #9a9db1) that stand in for the dark gallery wall behind a lit photograph; and a run of warm off-whites (#fbfaf8 through #e7e4da) that mimic the tonal range of actual fine-art paper. A teal accent (#0e7a82) surfaces on hover states and secondary links — quiet enough not to compete with the photography, present enough to give the interface a second signature color beyond the crimson. Edition size numerals, photographer names, and print dimensions all get Canela-Light at restrained weights; the result is a hierarchy built around reverence for the image rather than urgency around the purchase. Corners are consistently sharp or near-sharp — product cards, input fields, and primary buttons all use minimal radii, reinforcing the print-object seriousness. The grid is wide and uncluttered, relying on generous whitespace and the natural draw of large-format photography thumbnails to move the eye. Soft {rounded.xs} radii on UI chrome keep the interface from feeling clinical while preserving the sense of a physical, institutional space.

colors:
  primary: "#ce051d"
  primary-active: "#a50418"
  primary-disabled: "#eb9ba5"
  ink: "#212121"
  body: "#424242"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f7f5f2"
  surface-warm: "#f1efe9"
  surface-card: "#fbfaf8"
  surface-paper: "#e7e4da"
  on-primary: "#ffffff"
  navy: "#272d45"
  slate: "#676986"
  slate-light: "#b3b4c3"
  teal-accent: "#0e7a82"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Canela-Light', serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Canela-Light', serif"
    fontSize: 38px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Canela-Light', serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Canela-Light', serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'HelveticaNowPro', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'HelveticaNowPro', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.03em
  body-md:
    fontFamily: "'HelveticaNowPro', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'HelveticaNowPro', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'HelveticaNowPro', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  edition-label:
    fontFamily: "'HelveticaNowPro', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  photographer-name:
    fontFamily: "'Canela-Light', serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'HelveticaNowPro', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'HelveticaNowPro', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'HelveticaNowPro', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.04em
  price-display:
    fontFamily: "'HelveticaNowPro', Helvetica, Arial, sans-serif"
    fontSize: 16px
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    border: "none"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 12px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.ink}"
  nav-link-hover:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/3"
    padding: 0
    gap: "{spacing.sm}"
  product-card-title:
    typography: "{typography.photographer-name}"
    textColor: "{colors.ink}"
  product-card-meta:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  edition-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.edition-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  edition-badge-sold-out:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.edition-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
  hero-editorial:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.section}"
  print-size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  print-size-unavailable:
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
    textDecoration: line-through
  photographer-credit:
    typography: "{typography.photographer-name}"
    textColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    paddingTop: "{spacing.base}"
  edition-counter:
    typography: "{typography.edition-label}"
    textColor: "{colors.primary}"
    letterSpacing: 0.1em
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separator: "/"
    gap: "{spacing.xs}"
  filter-bar:
    backgroundColor: "{colors.surface-soft}"
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  filter-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  filter-tag-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 12px 16px
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.slate-light}"
    linkHoverColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  footer-heading:
    typography: "{typography.edition-label}"
    textColor: "{colors.canvas}"
    marginBottom: "{spacing.base}"
  newsletter-input:
    backgroundColor: "transparent"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.slate-light}"
    rounded: "{rounded.none}"
    padding: "10px 14px"

## Components

### Buttons

**`button-primary`** — A flat crimson (#ce051d) rectangle with no border radius, zero softening. Text runs in HelveticaNowPro at 13px with 0.08em uppercase letter-spacing, giving the CTA the feel of a print label rather than a digital affordance. Active state darkens to #a50418; disabled state desaturates to the muted pink #eb9ba5 while holding white text.

**`button-secondary`** — Transparent fill with a 1px ink-colored border mirrors the print-object aesthetic — the outline reads like a frame. On hover, the background inverts to full ink and text flips white, a confident all-or-nothing toggle with no intermediate tint states.

**`button-ghost`** — Used for secondary navigation actions (Share, Wishlist, Back to category). No border, muted text, understated; disappears into the canvas and lets photography carry the visual weight.

### Product Card

**`product-card`** — No border-radius on any corner; images are displayed full-bleed with a consistent 4:3 aspect ratio to maintain grid rhythm across landscape and portrait photographs. The photographer's name sits below in Canela-Light (`{typography.photographer-name}`), followed by a descriptor line in `{typography.caption}` at `{colors.muted}`, then the price in `{typography.price-display}`. No box shadow, no card lift on hover — hover state is communicated through a subtle image scale transition only.

### Edition Badge

**`edition-badge`** — The single most brand-defining component: a flat crimson slab (`{colors.primary}`) carrying uppercase edition text in 11px HelveticaNowPro at 0.1em tracking. Applied as an overlay on the product image, bottom-left corner, or as an inline tag in product detail. Sold-out editions swap to `{colors.navy}` to maintain legibility while communicating closure without a strikethrough.

### Hero

**`hero-section`** — Wide-format canvas with display text in Canela-Light `{typography.display-xl}`, centered or left-aligned against clean white. Relies entirely on a single full-width photograph to establish atmosphere; no gradient overlays, no text shadows. The `{typography.display-xl}` at 52px/300 weight keeps the serif airy.

**`hero-editorial`** — Dark navy (`{colors.navy}`) full-bleed panels used for collection features or photographer spotlights. Text reverses to canvas white with `{typography.display-lg}`, giving a gallery-catalogue feel distinct from the commerce hero.

### Navigation

**`nav-bar`** — 64px tall, white background, 1px hairline bottom border. Links in `{typography.nav-link}` — 13px HelveticaNowPro with modest tracking. Active category underlined with a 1px solid ink line. No mega-menu backgrounds or flyout panels with fills; sub-navigation drops against white. Logo sits left at modest size, secondary actions (Search, Cart, Account) iconographic on the right.

### Print Size Selector

**`print-size-selector`** — A grid of flat rectangular options, no radius, 1px border. Unselected: `{colors.hairline}` border. Selected: `{colors.ink}` border with no fill change — the border weight alone communicates selection. Unavailable sizes are shown with muted text and a line-through rather than removed, preserving the awareness of what the edition offered.

### Filter Bar

**`filter-bar`** — A soft-surface strip (`{colors.surface-soft}`) housing pill-shaped filter tags (`{rounded.full}`) and sort controls. Tags are white with hairline borders at rest; selected tags invert to ink fill with white text. Typography runs in `{typography.button-sm}` uppercase.

### Footer

**`footer`** — Navy (`{colors.navy}`) full-width slab; section headings in `{typography.edition-label}` uppercase, body links in `{typography.body-sm}` at `{colors.slate-light}`, warming to canvas on hover. The newsletter input is a transparent rectangle with a slate-light border, blending into the dark slab.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero text drops to `{typography.display-md}`; filter bar scrolls horizontally; nav collapses to hamburger + logo + cart icon; print-size selector becomes a horizontal scroll row |
| Tablet | 744–1128px | Two-column product grid; hero maintains full-width photo with text overlay; nav shows top-level links inline, secondary links in flyout; edition badge repositions to image overlay bottom-left |
| Desktop | 1128–1440px | Three- or four-column product grid; photography detail pages split into 60/40 image/info layout; filter bar anchors sticky below nav; full footer four-column layout |
| Wide | > 1440px | Grid constrained to max-width ~1440px, centered; hero photography runs full viewport width behind a centered content container; generous side margins prevent line lengths from exceeding ~75ch |

### Touch Targets

- All interactive buttons minimum 44px height
- Print size selector cells minimum 44×44px tap target even at small label sizes
- Nav icons minimum 44px hit area with negative-space padding
- Filter pill tags minimum 36px height, 44px if stacked

### Collapsing Strategy

- Photography grid: 4-col → 3-col → 2-col → 1-col at breakpoints
- Footer columns: 4-col → 2-col → 1-col stacked
- Product detail: horizontal 60/40 split collapses to stacked image-above-info on tablet/mobile
- Hero editorial panels: side-by-side image/text at desktop; stacked image-above-text at mobile
- Photographer spotlight sections: horizontal scroll carousel on mobile, static grid on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact nav height and logo dimensions not confirmed; 64px is inferred from Shopify theme patterns
- Hover animation timing and easing curves not extractable from static snapshot
- Whether Canela-Light is licensed as a web font or loaded as a local variable font could not be confirmed; fallback to `serif` is present in the stack but optical size may differ
- `#000f9f` (deep blue) and `#007aff` (system blue) appear in extracted colors but their precise context — links, interactive states, or third-party widget injections — could not be determined; omitted from primary palette
- `#eb9ba5` (muted pink) appears to be a UI state color (disabled, sale badge) but exact usage context was not confirmed
- Spacing scale between header and first content section is not precisely measured; `{spacing.section}` is an estimate
- Wishlist / save-for-later interaction pattern (icon button style) not confirmed from extraction
