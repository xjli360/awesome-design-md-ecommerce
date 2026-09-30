---
version: alpha
name: "Spiritual Gangster"
source_url: "https://www.spiritualgangster.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Five extracted colors — all of them neutrals, ranging from near-black (#121212) to pale silver (#dedede) — map a brand that refuses the soft sage-and-cream palette expected of yoga activewear. The darkest tone (#121212) functions as an anchor across hero sections and full-bleed overlays, while the slightly warmer charcoal (#343333) handles body text, giving the brand a chromatic temperature of graphite rather than pure ink. What breaks this austerity is not color but typeface: nitti-typewriter appears in five distinct cuts — cameo, corrected, normal, open, underlined — a monospace family that writes product callouts and mantra text as if struck on a midcentury machine, physically imperfect and analog-intimate in a digital storefront. Set against a clean grotesque like aktiv-grotesk or moderat for body copy and UI labels, the collision of utilitarian Swiss sans and typewriter letterpress creates the brand's spiritual-meets-streetwear tension without a single pixel of decoration. Navigation sits flat and typographic against the white canvas, buttons use near-black `{colors.primary}` with no visible hover glow — interaction is communicated through opacity rather than color shift. Product cards lean toward flush full-bleed imagery with caption overlays set in nitti-typewriter, treating each garment as an editorial spread rather than a standard e-commerce listing. Corners are spare: `{rounded.xs}` or `{rounded.none}` on most interactive elements, signaling that refinement here comes from proportion and material photography rather than softness of shape. The spiritual vocabulary — mantras, Sanskrit-inflected copy, eclipse and mandala motifs — lives almost entirely in the typography layer, not in brand color, making the nitti-typewriter family the brand's most singular visual asset and the clearest signal of its identity.

colors:
  primary: "#343333"
  primary-active: "#121212"
  primary-disabled: "#d7d7d7"
  ink: "#1c1c1c"
  body: "#343333"
  muted: "#6b6b6b"
  hairline: "#dedede"
  hairline-soft: "#d7d7d7"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#1c1c1c"

typography:
  display-xl:
    fontFamily: "moderat, aktiv-grotesk, halcom, sans-serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "moderat, aktiv-grotesk, halcom, sans-serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "moderat, aktiv-grotesk, halcom, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.2px
  title-md:
    fontFamily: "aktiv-grotesk, moderat, halcom, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "aktiv-grotesk, moderat, halcom, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.04em
  body-md:
    fontFamily: "aktiv-grotesk, moderat, halcom, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "aktiv-grotesk, moderat, halcom, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "aktiv-grotesk, moderat, halcom, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  typewriter-display:
    fontFamily: "nitti-typewriter-normal, nitti-typewriter-open, monospace"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  typewriter-overlay:
    fontFamily: "nitti-typewriter-cameo, nitti-typewriter-normal, monospace"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  typewriter-caption:
    fontFamily: "nitti-typewriter-open, nitti-typewriter-normal, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  nav-link:
    fontFamily: "aktiv-grotesk, moderat, halcom, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "aktiv-grotesk, moderat, halcom, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "aktiv-grotesk, moderat, halcom, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  label-uppercase:
    fontFamily: "aktiv-grotesk, moderat, halcom, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.15em
    textTransform: uppercase
  price:
    fontFamily: "aktiv-grotesk, moderat, halcom, sans-serif"
    fontSize: 15px
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
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.on-dark}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  announcement-bar:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-uppercase}"
    height: 36px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
  product-card-name:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    textColor: "{colors.muted}"
    textDecoration: line-through
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-badge-sale:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  quick-add:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    height: 40px
  size-selector:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  size-selector-active:
    border: "1px solid {colors.primary}"
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  size-selector-sold-out:
    textColor: "{colors.primary-disabled}"
    border: "1px solid {colors.hairline}"
    textDecoration: line-through
  hero-full-bleed:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    overlayOpacity: 0.35
    titleTypography: "{typography.typewriter-display}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 100vh
  hero-split:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    imageWidth: "50%"
    gap: "{spacing.section}"
  mantra-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.typewriter-overlay}"
    padding: "{spacing.xxl} {spacing.section}"
    textAlign: center
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    padding: "{spacing.xxl} 0"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Full-width or inline dark charcoal block, no border radius, uppercase with 0.1em letter-spacing doing the visual lifting rather than weight. Active state deepens to `{colors.primary-active}` (#121212) with no animated transition; hover communicates through opacity shift rather than a color change. Disabled falls back to the pale `{colors.primary-disabled}` gray.

**`button-secondary`** — Transparent fill with a 1px `{colors.primary}` border and matching typographic scale. Used for secondary CTAs on white canvas surfaces where the charcoal outline reads cleanly against the light ground. Pair with `{button-primary}` for clear CTA hierarchy on product pages.

**`button-ghost`** — Identical structure to secondary but inverted for dark contexts: white text and white 1px border on `{colors.surface-dark}` hero and `{mantra-banner}` sections. Prevents the secondary outline from disappearing against dark overlays. Used as the primary CTA inside `{hero-full-bleed}`.

**`quick-add`** — Appears on product card hover, slides up from the card's bottom edge at 40px height. Same uppercase tracked label scale as buttons but at `{typography.button-sm}`, full card width, no border radius. On mobile, visible by default rather than revealed on hover.

### Text Inputs

**`text-input`** — Flush-cornered with a 1px `{colors.hairline}` border. Focus state shifts border to `{colors.ink}` with no glow or shadow ring — restraint over feedback. Placeholder text in `{colors.muted}`. Search contexts may use a bottom-border-only underline variant rather than full border.

### Navigation

**`nav-bar`** — 64px tall, white canvas with a `{colors.hairline}` bottom rule. Links rendered in uppercase `{typography.nav-link}` at 13px/0.08em tracking. When positioned over a dark hero, transitions to `{nav-bar-dark}` — same geometry, inverted palette. Cart, search, and account icons cluster right; hamburger replaces the full link list below the tablet breakpoint.

**`announcement-bar`** — 36px strip sitting above the nav in `{colors.primary-active}` near-black. Uppercase `{typography.label-uppercase}` copy, typically a scrolling marquee for shipping thresholds and promotions. No border radius.

### Product Cards

**`product-card`** — Portrait 3:4 image, no card rounding, no drop shadow. Image fills the full tile width flush. Product name in `{typography.body-sm}` and price in `{typography.price}` sit left-aligned below the image with `{spacing.sm}` gap. Sale price shows the original struck through in `{colors.muted}`. On hover, `{quick-add}` slides up from the bottom edge and the image may apply a subtle scale(1.03) zoom within its crop frame. `{product-badge}` chips sit absolute top-left of the image.

**`size-selector`** — Grid of 40×40 square tiles with 1px `{colors.hairline}` border. Active swatch flips to a `{colors.primary}` fill with white text. Sold-out tiles receive struck-through text and subdued border with no diagonal SVG line.

### Hero Sections

**`hero-full-bleed`** — Full viewport-height dark photograph with a `{colors.surface-dark}` overlay at 35% opacity. Headline set in `{typography.typewriter-display}` — nitti-typewriter at 36px creates a handset editorial feel over the imagery. Supporting CTA uses `{button-ghost}`. Mobile reduces to 80vh to keep the CTA in viewport without scroll.

**`hero-split`** — 50/50 image-plus-copy split on a white canvas. Copy block uses `{typography.display-xl}` at weight 400 — the brand's openness to lightweight display rather than heavy-weight headlines signals confidence in whitespace over typographic muscle. Used for lookbook entries and category heroes.

**`mantra-banner`** — Full-width `{colors.surface-dark}` strip with centered `{typography.typewriter-overlay}` text. Site mottos, Sanskrit phrases, or seasonal copy. `{spacing.xxl}` vertical padding, `{spacing.section}` horizontal. No image background — the typewriter font is the only visual element.

**`collection-header`** — White canvas, title in `{typography.display-md}` at weight 400, optional editorial description in `{typography.body-md}`. Sits above the product grid with `{spacing.xxl}` top padding.

### Search

**`search-overlay`** — Full-width panel that drops over the nav on canvas white. Input field flush, full-width, no rounding, `{typography.body-md}`. Recent searches and trending products appear below as a plain typographic list with no card wrapping or image thumbnails.

### Cart

**`cart-drawer`** — Right-side slide-in panel, 400px wide, 1px left border in `{colors.hairline}`. Product rows show thumbnail, name, size/color attribute, quantity stepper, and line price. Footer holds order total and a full-width `{button-primary}` checkout CTA.

### Footer

**`footer`** — `{colors.surface-dark}` background, four-column grid of link groups. Column headings in `{typography.label-uppercase}` with `{colors.on-dark}` link text in `{typography.body-sm}`. Social icon row at the bottom. Newsletter input sits either in a dedicated column or as a full-width stripe above the link grid.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with slide-in drawer; hero reduces to 80vh; hero copy drops to `{typography.display-md}`; cart drawer goes full-width; footer collapses to accordion; `{quick-add}` always visible |
| Tablet | 744–1128px | Two-column product grid; nav may remain visible with condensed links; hero-split stacks vertically image above copy; search overlay full-width |
| Desktop | 1128–1440px | Three or four-column product grid; full nav bar with all links visible; hero-split true 50/50; cart drawer fixed at 400px |
| Wide | > 1440px | Max content width ~1400px centered; product grid holds at 4 columns; hero images scale to fill without crop distortion; gutters grow proportionally |

### Touch Targets

- All interactive controls minimum 44×44px on mobile
- Size selector tiles expand to 48×48px on mobile breakpoint
- Nav icons (cart, search, account) maintain 44px tap zones regardless of rendered icon size
- `{quick-add}` displayed by default on mobile at full card width — not gated behind hover

### Collapsing Strategy

- Top nav collapses to hamburger + logo + cart icon below 744px; all secondary links move into a slide-in left drawer
- Footer link groups collapse to accordion panels on mobile — only `{typography.label-uppercase}` headings visible until tapped
- Hero-split stacks image above copy on mobile; image height caps at 60vh to keep the CTA visible without scrolling
- Announcement bar text truncates to a static single line on mobile when short; marquee activates when text exceeds viewport width
- Product filter panel shifts from a left sidebar on desktop to a bottom-sheet drawer on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand accent or highlight color surfaced in extraction — all five extracted hex values are near-black to near-white neutrals. If Spiritual Gangster uses a seasonal brand accent (warm gold, dusty rose, earthy terracotta) it did not appear in the top extracted palette. Verify against current lookbook or brand style guide before asserting any accent token.
- Exact font role assignments are inferred rather than extracted: the stack lists moderat, aktiv-grotesk, halcom, Almarai, and five nitti-typewriter cuts without indicating which serves display, body, or UI roles. Assignments above reflect brand aesthetic logic.
- Almarai (a wide geometric Arabic-Latin sans) appears in the font stack; its specific use context — potentially locale-switching for an Arabic storefront variant or a legacy load — could not be confirmed.
- No meta theme-color was set on the page, and no explicit border-radius values were extracted. `{rounded.none}` as the dominant component radius is inferred from the brand's geometric-minimal aesthetic.
- Exact button height, internal padding, and hover transition timing (duration and easing curves) were not available from extraction.
- Sticky versus static nav behavior on scroll could not be confirmed from the extraction data.
- Sale/discount color treatment (whether a red or orange accent is used for sale pricing) did not surface — `{colors.muted}` is used as a conservative fallback.
