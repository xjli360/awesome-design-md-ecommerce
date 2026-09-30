---
version: alpha
name: "Yoko London"
source_url: "https://www.yokolondon.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Pearl jewelry tends to reach for cream and ivory; Yoko London reaches instead for a deep wine burgundy (#3c1929) and the cool precision of slate-blue gray (#586877) — the palette of a gem archive rather than a bridal suite. Against that dark-cool ground, champagne gold (#e6c297) and petal blush (#f0c7bc) read as the actual surface tones of the pearls being sold, luminescence pulled into the UI rather than applied as ornamental accent. Buttons, input fields, and image containers carry no radius at all ({rounded.none}): hard corners everywhere, a curatorial sharpness that refuses the softening gesture most jewelry brands make to read as feminine or approachable.

  Type is split sharply between two registers. Display headings and price figures run in SaolText — a high-contrast editorial serif whose hairline strokes reference gem-certificate engraving — at light weight (300) and tight leading. Navigation links, UI labels, and all button copy run in Rawline, a geometric sans with mild personality, tracked wide in uppercase for buttons (letterSpacing 0.12em). The combination puts the brand in a gallery-guide register rather than a shopping register: SaolText could sit credibly in a double-page editorial spread; Rawline could caption a contemporary jewellery exhibition.

  The primary burgundy (#3c1929) anchors both primary CTAs and the full-bleed footer inversion, so the pigment that opens the first brand impression also closes the page — a deliberate chromatic bracket. A champagne annotation badge (#e6c297) doubles as editorial label and pearl-type indicator, referencing the specific tonal quality of golden south-sea pearls in a single token. The pale rose strip (#e8dadd) threads through editorial dividers, close enough to pearl nacre that it blurs the boundary between colour reference and material reference. Product imagery runs 4:5 portrait with hard-edge containers, framing gems the way a lightbox frame photographs specimens. The filter bar uses tracked uppercase Rawline labels on hairline borders — sparse, museum-like, designed to disappear once a user has made their selection.

colors:
  primary: "#3c1929"
  primary-active: "#2a0f18"
  primary-disabled: "#b89aa0"
  ink: "#121212"
  body: "#586877"
  muted: "#a4afb9"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  slate: "#586877"
  slate-light: "#a4afb9"
  champagne: "#e6c297"
  blush: "#f0c7bc"
  petal: "#e8dadd"

typography:
  display-xl:
    fontFamily: "'SaolText', Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'SaolText', Georgia, serif"
    fontSize: 34px
    fontWeight: 300
    lineHeight: 1.18
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'SaolText', Georgia, serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Rawline', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.04em
  title-sm:
    fontFamily: "'Rawline', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.06em
  body-md:
    fontFamily: "'Rawline', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Rawline', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Rawline', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.04em
  nav-link:
    fontFamily: "'Rawline', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.07em
  button-md:
    fontFamily: "'Rawline', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Rawline', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  editorial-label:
    fontFamily: "'Rawline', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.15em
    textTransform: uppercase
  price-display:
    fontFamily: "'SaolText', Georgia, serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0
  price-sm:
    fontFamily: "'SaolText', Georgia, serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.3
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
    padding: 14px 36px
    height: 48px
  button-primary-hover:
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
    padding: 13px 35px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 13px 35px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxHeight: 32px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    labelTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    imageObjectFit: contain
    padding: "{spacing.md}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.editorial-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    minHeight: 80vh
    imagePosition: right
  editorial-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.editorial-label}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  champagne-badge:
    backgroundColor: "{colors.champagne}"
    textColor: "{colors.ink}"
    typography: "{typography.editorial-label}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  pearl-accent-strip:
    backgroundColor: "{colors.petal}"
    textColor: "{colors.primary}"
    typography: "{typography.editorial-label}"
    padding: "{spacing.md} {spacing.section}"
    textAlign: center
  collection-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-md}"
    captionTypography: "{typography.editorial-label}"
    minHeight: 400px
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.muted}"
  newsletter-signup:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    inputTypography: "{typography.body-md}"
    buttonTypography: "{typography.button-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.nav-link}"
    headingTypography: "{typography.editorial-label}"
    padding: "{spacing.xxl} {spacing.section}"

## Components

### Buttons

**`button-primary`** — Solid burgundy (#3c1929) fill, white text, zero border radius, 48px tall with generous 36px horizontal padding. Uppercase Rawline at 12px/0.12em tracking keeps the label restrained and curatorial. Hover darkens to `{colors.primary-active}` (#2a0f18); disabled mutes to `{colors.primary-disabled}`. The hard corners are non-negotiable — they signal precision over approachability.

**`button-secondary`** — White fill with a 1px burgundy border and burgundy text, matching the primary's height and padding. Functions as an outlined counterpart on white canvas backgrounds, distinguishing "add to wishlist" actions from "add to bag." Hard corners mirror the primary.

**`button-ghost`** — Transparent fill with a 1px hairline (#dedede) border and ink text. Used for low-priority actions — "back", "filter", "more info" — where the button should recede. Same uppercase tracking as primary, same height.

### Navigation

**`nav-bar`** — 72px white bar with a hairline bottom border, logo left, primary links center or right at 13px tracked Rawline. No pill shapes or rounded dropdowns. On scroll, the bar stays fixed and opaque; no blur or transparency effects were observed. Dropdown panels (`nav-dropdown`) open beneath the hairline border as full-width white sheets with editorial body-sm link grids.

### Product Card

**`product-card`** — Lives on `{colors.surface-soft}` (#f6f6f6), no rounding, 4:5 portrait container with `object-fit: contain` so gem photography is never cropped. Label text is `{typography.body-sm}` Rawline; price is `{typography.price-display}` SaolText at 300 weight. An editorial badge in burgundy or champagne can anchor to the top-left corner. No hover shadow; a subtle opacity shift or image-swap is the expected hover gesture.

### Hero

**`hero`** — Typically a split layout: editorial SaolText headline (`{typography.display-xl}`) on left at 300 weight, high-resolution pearl or model photography on right. Minimum 80vh, background `{colors.surface-soft}`. A single primary CTA button sits below a one-to-two line subtitle in `{typography.body-md}`. No carousel auto-play; the brand prefers static editorial imagery.

### Badges and Labels

**`editorial-badge`** — Burgundy fill, white uppercase Rawline editorial-label text, no rounding, 3px×8px tight padding. Used for "NEW", collection names, or "BESTSELLER" stamps on product cards and category headers.

**`champagne-badge`** — Warm gold (#e6c297) fill, ink text, same zero-radius structure. Used for pearl type or grade annotations — "South Sea", "Akoya", "Freshwater" — functioning simultaneously as editorial label and gem category.

**`pearl-accent-strip`** — A full-width pale rose (#e8dadd) band used as a section divider between editorial content blocks. Typography is uppercase Rawline editorial-label in burgundy. Padding is generous vertically; the strip exists primarily as a chromatic pause rather than an information carrier.

### Collection Banner

**`collection-banner`** — Full-bleed burgundy panel (#3c1929) with a SaolText display headline at 300 weight in white and an editorial-label caption above the headline in uppercase Rawline. Minimum 400px tall. Used at the top of collection pages as a category statement, anchoring the category name in the brand's primary pigment.

### Filter Bar

**`filter-bar`** — White, hairline-bordered row of uppercase Rawline title-sm labels representing category facets (metal, pearl type, price range). Active state moves text to `{colors.ink}`; inactive states sit at `{colors.body}` (#586877). No pill chips — filters are underline-only or plain text toggles to maintain the museum-like spareness.

### Newsletter Signup

**`newsletter-signup`** — Light (#f6f6f6) panel with a SaolText display-sm heading at 300 weight, a brief body-md description, a borderless or hairline-bordered text input, and a button-primary CTA. Padding is generous (`{spacing.section}` vertical) and the layout centers its content column on wide screens.

### Footer

**`footer`** — Full burgundy (#3c1929) inversion of the canvas, white text and links throughout. Heading labels are uppercase Rawline editorial-label; body links are nav-link weight 500 Rawline. A chromatic bracket — the same pigment that opens the primary CTA experience closes the full-page experience. Newsletter input and submit may appear here in an inverted-on-burgundy variant.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hamburger nav replaces horizontal links; product grid collapses to 2 columns; hero stacks text above image, full-width; filter bar scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; nav may retain horizontal links or use a condensed variant; hero maintains split but at tighter proportions |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav with dropdowns; hero at full 80vh split; filter bar inline with results count |
| Wide | > 1440px | Max-width container (~1400px) centered; hero and banner imagery scales up; typography scales minimally — layout breathes rather than reflows |

### Touch Targets

- All buttons maintain 48px minimum height on mobile
- Filter labels and nav links expand tap area with padding to at least 44px tall
- Product card images are tappable in their full 4:5 container, not just the label row below

### Collapsing Strategy

- Filter facets collapse into a bottom sheet or modal drawer on mobile behind a "Filter & Sort" trigger button
- Navigation collapses to hamburger at < 744px; dropdown submenus become full-screen slide-in panels
- Newsletter and editorial strips stack vertically and reduce horizontal padding from `{spacing.section}` to `{spacing.xl}`
- Collection banners maintain full-bleed but reduce headline from display-md to display-sm on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover and focus ring colors were not directly extracted; `{colors.primary-active}` (#2a0f18) is derived by darkening the extracted primary (#3c1929)
- `{colors.primary-disabled}` (#b89aa0) is inferred; no disabled-state hex was captured in the extraction
- SaolText and Rawline font weights in use beyond 300/400/500/600 are not confirmed; full weight axes were not extracted
- Animation/transition durations and easing curves (hover states, drawer open, image swap) were not captured
- Icon set and icon sizing were not identified — likely SVG inline icons or a custom icon font not surfaced in the extraction
- Exact nav height (72px used here) is an estimate; extraction did not confirm a computed value
- `#007aff` in the extracted palette is an iOS WebKit system color (Shopify mobile meta or a system UI default), not a Yoko London brand color — excluded intentionally
- Mobile-specific typography scaling (fluid type, viewport-relative units) was not confirmed; fixed px values are used throughout
- Swiper carousel configuration (pearl or collection carousels) — visual styling, pagination dot color, and arrow treatment — not confirmed from extraction
