---
version: alpha
name: "Farer"
source_url: "https://www.farer.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The deep navy at #021a30 — closer to an ink-soaked sea chart than a corporate blue — anchors every primary surface and CTA on Farer's site, creating a presence that reads as resolved rather than merely restrained. The brand formats its tagline as a technical equation: "British Design x Swiss Made," using a multiplication operator rather than a conjunction, signaling a methodology rather than a marketing pairing. FoundersGrotesk carries all typographic work across the site, its geometric skeleton and open counterforms providing clean-room legibility that steps out of the way of dial photography. Color on the UI side runs deliberately cold and narrow — near-whites at #f4f4f4, #f3f3f3, and #f1f1f1, off-grays at #dedede and #dfdfdf, a muted blue-gray at #374757 for secondary interface surfaces — a neutral viewing chamber that refuses to compete with the coral, teal, and bicolor dials it frames. Corners are consistently sharp; the design vocabulary trusts the rectangle the way a case maker trusts a straight edge, and no decorative radius softens CTAs or product cards into approachability. Product imagery takes full priority within card bounds, with series names and reference codes rendered in uppercase tracking labels below rather than layered over the image. Navigation renders in {colors.ink} on {colors.canvas}, with {colors.primary} reserved for active states and CTA surfaces, so the single color capable of weight always signals actionability. Specification tables on product pages use {typography.label-upper} keys in {colors.muted} against {typography.body-md} values in {colors.ink}, adopting the register of a technical data sheet rather than marketing copy. The swatch selector is where Farer's suppressed color finally surfaces in the UI — coral, slate, olive, cream dial swatches set in {rounded.full} circles against an otherwise monochrome interface. Vertical section rhythm is expansive; pages carry product-dense grids but minimal prose, letting the object itself make the argument.

colors:
  primary: "#021a30"
  primary-active: "#0a3055"
  primary-disabled: "#8fa3b5"
  ink: "#121212"
  body: "#383838"
  muted: "#374757"
  hairline: "#dedede"
  hairline-soft: "#dfdfdf"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#f3f3f3"
  surface-mid: "#f1f1f1"
  on-primary: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "FoundersGrotesk, sans-serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "FoundersGrotesk, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "FoundersGrotesk, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "FoundersGrotesk, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "FoundersGrotesk, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "FoundersGrotesk, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "FoundersGrotesk, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "FoundersGrotesk, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-upper:
    fontFamily: "FoundersGrotesk, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "FoundersGrotesk, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.04em
  button-sm:
    fontFamily: "FoundersGrotesk, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.04em
  nav-link:
    fontFamily: "FoundersGrotesk, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
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
    padding: 14px 28px
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
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoArea: left
    actionsArea: right
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    imageAspect: "4/5"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    subtitleTypography: "{typography.label-upper}"
    subtitleColor: "{colors.muted}"
    priceTypography: "{typography.body-sm}"
  product-card-hover:
    imageScale: 1.02
    transitionDuration: 300ms
    boxShadow: none
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 80vh
    layout: split-left-copy
    contentMaxWidth: 560px
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    padding: "{spacing.section} 0"
    layout: centered
  collection-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  spec-row:
    backgroundColor: "{colors.canvas}"
    keyTypography: "{typography.label-upper}"
    keyColor: "{colors.muted}"
    valueTypography: "{typography.body-md}"
    valueColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md} 0"
  swatch-selector:
    size: 24px
    gap: "{spacing.sm}"
    activeBorder: "2px solid {colors.primary}"
    activeRingOffset: 2px
    inactiveBorder: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
  collection-filter:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    activeBorderBottom: "2px solid {colors.primary}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    inputTypography: "{typography.display-sm}"
    inputColor: "{colors.ink}"
    rounded: "{rounded.none}"
    backdropColor: "{colors.scrim}"
    backdropOpacity: 0.4
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    padding: "{spacing.xxl} 0"
    borderTop: none

## Components

### Buttons

**`button-primary`** — Full navy (#021a30) fill on a flat rectangle with zero border radius, `{typography.button-md}` in white at 14px with tracked uppercase-leaning weight. The hard corner is structural, not incidental: it echoes the angular geometry of Farer's case designs and signals precision over warmth. Hover transitions to `{colors.primary-active}` (#0a3055), lighter than the resting state to maintain legibility. Disabled state shifts to `{colors.primary-disabled}`, a desaturated blue-gray that recedes without leaving the navy register.

**`button-secondary`** — White canvas fill with a 1px `{colors.primary}` border and navy text. Matches the primary button's height (48px) and corner geometry exactly, producing an optically balanced pair. Used for secondary choices — model comparisons, "Learn more" — where the primary CTA is already committed to a purchase action.

**`button-ghost`** — Transparent background with a 1px `{colors.hairline}` border, ink text. Appears in editorial zones and alongside media where any fill would add visual mass. Typical labels: "View collection," "See all."

### Navigation

**`nav-bar`** — 64px white bar, Farer wordmark left-aligned, cart icon and navigation links right-aligned. Links in `{typography.nav-link}` at 14px weight 500 in `{colors.ink}`. A single 1px `{colors.hairline}` bottom border separates the bar from content without introducing shadow. On scroll, `nav-bar-scrolled` retains the same border-only treatment — the bar never gains background elevation or opacity change.

### Product Card

**`product-card`** — `{colors.surface-soft}` (#f4f4f4) background, no border, no radius. The image occupies a 4:5 aspect ratio container and scales 1.02× on hover over 300ms — the only interactive signal the card produces. Below the image: series name in `{typography.label-upper}` at `{colors.muted}`, model name in `{typography.title-sm}` in `{colors.ink}`, price in `{typography.body-sm}`. No star ratings, no urgency banners; the card trusts photography over merchandising signals.

### Hero

**`hero-banner`** — Full-bleed navy `{colors.primary}` at minimum 80vh. Headline in `{typography.display-xl}` in `{colors.on-primary}`, supporting copy in `{typography.body-md}` below it. Split layout: copy column left at max-width 560px, product photography right. The dark ground eliminates any ambient light bleed around the watch image — the object reads as a precise physical artifact, not a lifestyle prop.

**`hero-editorial`** — Interior collection page hero on `{colors.surface-soft}`. Headline in `{typography.display-md}` in `{colors.ink}`, centered single column, wide-aspect image above or below the text block. Lower visual intensity than `hero-banner`, appropriate for browsing contexts where the full-navy treatment would overwhelm adjacent product grids.

### Specification Table

**`spec-row`** — Appears on individual product pages for movement type, case diameter, water resistance, crystal, and strap materials. Keys in `{typography.label-upper}` in `{colors.muted}`, values in `{typography.body-md}` in `{colors.ink}`. Each row divided by a 1px `{colors.hairline-soft}` bottom border. No header row background, no alternating fills — the table reads as a clean technical manifest with no chrome.

### Swatch Selector

**`swatch-selector`** — Dial color swatches at 24px diameter circles in `{rounded.full}`, spaced 8px apart. This is the only place in the UI where Farer's suppressed color range surfaces: coral, slate, olive, cream, bicolor arrangements all appear here against the otherwise monochrome interface. Active swatch takes a 2px `{colors.primary}` ring offset 2px from the swatch edge; inactive swatches carry a 1px `{colors.hairline}` border.

### Collection Filter

**`collection-filter`** — Horizontal tab strip of series names (Cobb, Lander, Portofino, etc.) in `{typography.label-upper}`, muted at rest, ink when active. Active state is signaled by a 2px `{colors.primary}` bottom border only — no fill, no pill, no background change. The filter strip stays flush with the surface below it, maintaining the flat, architectural quality of the overall layout.

### Search Overlay

**`search-overlay`** — Full-window canvas overlay with a single dominant input in `{typography.display-sm}`. No visible icon chrome — the input field consumes the panel. Results populate below the input as the user types. Backdrop uses `{colors.scrim}` at 40% opacity. Dismisses on Escape or click outside. The overlay's blankness enforces focus; there is nothing else to look at.

### Footer

**`footer`** — Full-width `{colors.primary}` navy background with all text in `{colors.on-primary}`. Column headings in `{typography.label-upper}`, links in `{typography.body-sm}`. No lifestyle photography, no brand imagery — the footer is pure information architecture in the primary color, bookending the page with the same dark anchor that opens hero sections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces link row; hero stacks to image above, copy below; spec table runs full-width; collection filter strip scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; nav retains wordmark with condensed link set or hamburger; hero maintains split layout at reduced proportion |
| Desktop | 1128–1440px | Three-column product grid; full nav link row visible; hero at full 80vh with split layout |
| Wide | > 1440px | Four-column product grid with increased gutters; hero content column stays at 560px max-width, image fills remainder |

### Touch Targets

- All interactive targets meet 44×44px minimum; swatch selectors at 24px visual size are padded to 44px touch area
- Nav icons (cart, hamburger) use 44px touch targets
- Entire product card surface is tappable on mobile; spec rows are display-only and not interactive
- Collection filter tabs meet 44px height via vertical padding

### Collapsing Strategy

- Navigation collapses to hamburger at mobile breakpoint; off-canvas drawer slides in from left on `{colors.primary}` background with white links
- Collection filter tabs scroll horizontally on mobile rather than wrapping or dropping to a select element
- Hero copy column takes full width on mobile with image repositioned above the text block
- Footer columns stack vertically on mobile; column headings in `{typography.label-upper}` act as accordion triggers to expand and collapse link lists

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No UI-level accent or highlight color extracted beyond the primary navy; Farer's dial colors (coral, teal, olive, bicolor) are product attributes surfaced only in the swatch selector, not interface tokens
- `primary-active` (#0a3055) and `primary-disabled` (#8fa3b5) are derived values, not extracted from live stylesheets
- Canvas base assumed to be #ffffff; extracted near-whites (#f4f4f4, #f3f3f3, #f1f1f1) are treated as surface variants, but a pure-white canvas was not confirmed in extraction
- FoundersGrotesk weight range confirmed only as a family; specific weights per scale (500/600) are inferred from typical usage patterns, not inspected from computed styles
- Typography scale sizes (display-xl at 56px, etc.) are informed estimates; actual rendered sizes require direct viewport inspection
- Hover and transition animation specs beyond product card image scale not extracted
- Mobile nav drawer behavior and whether it slides from left or right not confirmed
- No data on sticky "add to cart" bar or floating CTA behavior on product detail pages
- No confirmation of whether Farer uses a cookie/consent banner and its visual treatment
