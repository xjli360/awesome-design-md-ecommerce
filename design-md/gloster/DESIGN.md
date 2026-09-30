---
version: alpha
name: "Gloster"
source_url: "https://www.gloster.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Teak grain rendered as a digital palette — Gloster's interface draws its warmth from #e3ded8 cream surfaces and #b9b2a5 stone accents that echo weathered heartwood, while a single muted forest green (#457364) anchors every navigational CTA and interactive affordance. The restraint is absolute; where most luxury brands lean on serif contrasts or cinematic video loops, Gloster trusts Helvetica Neue at clean weights and enormous product photography against near-white canvas (#e0e0de) to communicate material confidence. Typography runs light and wide — display headings sit at weight 300–400 with generous letter-spacing, letting the furniture occupy the visual stage rather than competing with typographic gesture. Corners stay sharp throughout (`{rounded.none}` on cards, buttons, and containers), reinforcing the rectilinear precision of outdoor dining tables and modular lounge frames. A secondary dark green (#2b483f) surfaces in footer regions and overlay states, creating depth without introducing new hue families. The monochrome gray ramp — from #262625 ink through #706f6f body copy to #c8c8c6 hairlines — is remarkably even, stepping in near-uniform increments that avoid harsh contrast jumps. Spacing favors generous `{spacing.section}` vertical rhythm between content blocks, reflecting the brand's physical product philosophy: each piece commands its own breathing room in an outdoor setting. Hover states are subtle shifts within the gray-green spectrum rather than opacity changes, and the overall impression is of a showroom where every surface has been considered for how it ages under sunlight — digital materials behaving like physical ones.

colors:
  primary: "#457364"
  primary-active: "#2b483f"
  primary-disabled: "#a3c4b8"
  ink: "#262625"
  body: "#706f6f"
  muted: "#a3a2a2"
  muted-soft: "#bbbbb9"
  hairline: "#c8c8c6"
  hairline-soft: "#e0e0de"
  canvas: "#ffffff"
  surface-soft: "#e0e0de"
  surface-card: "#ffffff"
  surface-warm: "#e3ded8"
  stone: "#b9b2a5"
  charcoal: "#484747"
  charcoal-deep: "#282827"
  forest-dark: "#2b483f"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  highlight: "#ffff00"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.14
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  overline:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 1.5px
    textTransform: uppercase
  mono:
    fontFamily: "monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

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
  section: 80px
  section-lg: 120px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 48px
    border: none
  button-primary-hover:
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
    padding: 15px 31px
    height: 48px
    border: 1px solid {colors.ink}
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 16px 0
    border: none
    borderBottom: 1px solid {colors.primary}
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 14px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.ink}
  text-input-label:
    typography: "{typography.overline}"
    textColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline-soft}
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: 0 1px 0 {colors.hairline}
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 0
    imageAspectRatio: 1 / 1
    gap: "{spacing.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-collection:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  hero-section:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    minHeight: 85vh
    padding: "{spacing.section} {spacing.xl}"
    imagePosition: cover
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 720px
  hero-subhead:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
    maxWidth: 560px
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.xxl} 0"
    borderBottom: 1px solid {colors.hairline-soft}
  collection-title:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  collection-description:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 640px
  material-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.charcoal}"
    typography: "{typography.overline}"
    rounded: "{rounded.none}"
    padding: 6px 12px
  footer:
    backgroundColor: "{colors.charcoal-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.overline}"
    textColor: "{colors.muted-soft}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.on-dark}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.xl}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.none}"
    padding: 16px 20px
    height: 56px
    border: none
  image-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    gap: "{spacing.xs}"
  designer-quote:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.charcoal}"
    typography: "{typography.display-sm}"
    padding: "{spacing.section} {spacing.xl}"
    borderLeft: 3px solid {colors.primary}
  specification-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rowBorder: 1px solid {colors.hairline-soft}
    padding: "{spacing.md} 0"
  sustainability-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    padding: "{spacing.lg} {spacing.xl}"
---

## Components

### Buttons

**`button-primary`** — A solid forest green rectangle with no border radius, white uppercase text tracked at 0.8px. On hover, the background deepens to `{colors.primary-active}` (#2b483f) with no transition beyond a 200ms color ease. Disabled state fades to a muted green-gray. The sharp corners mirror the linear silhouettes of Gloster's furniture frames.

**`button-secondary`** — A transparent button with a 1px ink-black border and uppercase black text. On hover, the fill inverts completely to solid black with white text — a decisive state change rather than a gentle fade. Used for secondary actions like "View Collection" or "Download Catalogue."

**`button-tertiary`** — Text-only with a thin underline in primary green, no background. Functions as an inline navigation prompt within editorial content or product detail pages. Hover shifts the underline to `{colors.primary-active}`.

### Inputs

**`text-input`** — Full-width fields with no radius, a single hairline border, and light-weight placeholder text. On focus, the border transitions to full ink black. Labels appear above in `{typography.overline}` uppercase tracking. Error states replace the border color with a warm red rather than the brand green.

### Navigation

**`nav-bar`** — A minimal 72px white bar with uppercase tracked links at 14px. The logo sits left, navigation center-right, and utility icons (search, account, locale) far-right. A faint bottom border separates it from content. On scroll, the bar gains a subtle shadow but no background change. Mobile collapses to a hamburger with a full-screen overlay in white.

### Product Display

**`product-card`** — Square aspect-ratio product images on a white background with zero border radius. Below the image: collection name in caption gray, product title in medium-weight 16px, and price in body gray. No hover shadow or border; interaction is signaled by a subtle image zoom (scale 1.03 over 400ms). Cards sit in a CSS grid with `{spacing.lg}` gap.

**`image-gallery`** — The PDP image gallery uses a soft gray background with 2px gaps between tiles. The main image occupies the left two-thirds on desktop, with a vertical strip of thumbnails on the right. No rounded corners. Lightbox opens on click with a dark scrim.

### Content Sections

**`hero-section`** — Full-viewport lifestyle photography with a warm cream overlay zone for text. Headlines render in the thin 300-weight display scale, creating an airy contrast against dense product imagery. A single CTA button in primary green anchors the composition at lower-left.

**`collection-header`** — A centered text block with display-md title and body-md description, separated from the grid below by a hairline. Generous vertical padding (`{spacing.xxl}`) gives each collection page an unhurried opening.

**`designer-quote`** — An editorial pull-quote block with warm cream background, a 3px left border in forest green, and display-sm italic-style text. Used on "About" and designer collaboration pages to add human voice.

**`material-badge`** — Small rectangular labels in warm cream with uppercase overline text identifying materials: "TEAK," "ALUMINIUM," "ALL-WEATHER WICKER." No radius, 6px vertical and 12px horizontal padding.

### Footer

**`footer`** — A dark charcoal (#282827) full-width block with columns of links in white body-sm text. Section headings use the overline style in muted gray. Generous padding (`{spacing.section}`) and clear column structure. Bottom row holds legal links, copyright, and locale selector.

### Utility

**`search-overlay`** — A full-screen white overlay triggered from the nav magnifying glass. The search input is a borderless field on a soft gray background at 56px height. Results appear below as product cards in a condensed grid. Close icon top-right.

**`specification-table`** — Alternating rows separated by soft hairlines, with dimension labels left-aligned in body-sm and values right-aligned. No zebra striping — the hairlines alone create rhythm.

**`sustainability-banner`** — A full-width bar in primary green with white title-weight text, used to highlight certifications (FSC, PEFC) and environmental commitments. Appears inline within product detail pages below the specification table.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger overlay; hero text stacks below image; section padding reduces to `{spacing.xl}`; display-xl drops to 36px |
| Tablet | 744–1128px | Two-column product grid; nav remains inline but link count may reduce; hero maintains side-by-side layout at tighter ratio; footer stacks to two columns |
| Desktop | 1128–1440px | Three-to-four column product grids; full nav with all links visible; hero at full 85vh with overlay text; image gallery at two-thirds/one-third split |
| Wide | > 1440px | Content max-width caps at 1440px centered; product grid expands to four columns with increased gap; section padding scales to `{spacing.section-lg}` |

### Touch Targets
- All interactive elements maintain a minimum 48px touch target on mobile
- Product cards use the full card surface as a tap target, not just the text
- Navigation hamburger icon has a 48×48px hit area despite the 24px visual icon
- Footer links get increased vertical padding (12px) on mobile for easier tapping

### Collapsing Strategy
- Navigation converts from horizontal uppercase links to a full-screen overlay menu with stacked links at `{typography.title-lg}` size
- Product filter sidebar on collection pages collapses to a bottom-sheet modal on mobile
- Specification tables remain horizontal but gain horizontal scroll on very narrow viewports
- Image gallery thumbnails move from a vertical strip to a horizontal scrollable row below the main image
- Designer quotes maintain their left-border treatment but reduce padding

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font extraction returned only system stacks (Arial, Helvetica Neue, sans-serif); Gloster may load a custom or licensed typeface via JavaScript that was not captured — the brand could use a proprietary serif or geometric sans for display headings
- No meta theme-color was detected; mobile browser chrome color is unknown
- The #ffff00 yellow in extracted colors is likely a focus-ring or debugging artifact rather than a brand token — its role is unconfirmed
- Animation and transition timing values could not be extracted; easing curves and durations above are estimated from visual observation
- Exact grid gutter values at each breakpoint were not captured; spacing tokens are inferred from visual rhythm
- No favicon or icon sprite data was extracted; icon style (line weight, filled vs. outlined) is undocumented
- Platform is non-Shopify; CMS and component framework are unknown, which may affect implementation of interactive patterns like search overlay and filter modals
