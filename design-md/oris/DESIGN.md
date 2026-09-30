---
version: alpha
name: "Oris"
source_url: "https://www.oris.ch"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The red of an Oris crown cap — #bf342d, specific enough to be identified across a watchmaker's bench — is the only chromatic commitment the brand permits on a layout otherwise composed entirely of deep charcoal (#2b333f), warm off-white (#f6f6f5), and a hierarchy of mechanical grays. Every primary button, every hover state, every active indicator resolves to that one red, functioning the way the physical crown mark functions on a watch case: a single orienting signal in an otherwise precision-machined object. Brown LL TT, the Swiss geometric sans from Lineto, carries all editorial and navigational text — its even-stroked, optically regularized letterforms sit closer to engineering specification than advertising copy, which suits a brand whose product pages read like technical bulletins as much as luxury retail. Display type runs large and light (weight 300–400), relying on spatial isolation rather than typographic mass; the photography — deep-focus lightbox watches against controlled dark grounds — does the tonal work.

  Section architecture alternates between the warm off-white canvas ({colors.canvas}) and full-bleed dark panels ({colors.surface-dark}), a rhythm that mirrors the alternating metal and lume segments of a watch dial. Product cards carry no rounding ({rounded.none}), their hard rectangular borders echoing the case geometry of the watches inside them; the only softness in the layout comes from 2px hairlines in #b5b5b5 that define table rows and input fields, approximating the thin case lug bevel visible in a close-up product photograph. A steel midtone, #73859f, appears in secondary navigation labels and collection taxonomy — a color that reads as brushed metal without illustration. Technical specification tables — movement calibre, power reserve, water resistance in metres — render in a monospace stack (Consolas, then Courier New) that positions the data as engineering output rather than marketing copy. The result is a site that feels less like a luxury boutique and more like a well-lit instrument workshop: everything in its place, no surface decorated beyond function, and one small red mark to tell you which way to turn the crown.

colors:
  primary: "#bf342d"
  primary-active: "#ba251e"
  primary-disabled: "#b95a56"
  ink: "#2b333f"
  body: "#343434"
  muted: "#565656"
  muted-soft: "#888888"
  hairline: "#b5b5b5"
  hairline-soft: "#ebebeb"
  canvas: "#f6f6f5"
  surface-soft: "#efefef"
  surface-card: "#fbfbfb"
  surface-dark: "#2b333f"
  on-primary: "#ffffff"
  on-dark: "#f6f6f5"
  steel: "#73859f"
  error: "#ffa3a5"
  badge-sale: "#ffcc66"

typography:
  display-xl:
    fontFamily: "'Brown LL TT', 'Brown LL TT Cyrillic', Arial, Helvetica, sans-serif"
    fontSize: 64px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Brown LL TT', Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Brown LL TT', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.15px
  title-md:
    fontFamily: "'Brown LL TT', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Brown LL TT', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Brown LL TT', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Brown LL TT', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Brown LL TT', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Brown LL TT', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Brown LL TT', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Brown LL TT', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.5px
  mono-spec:
    fontFamily: "Consolas, 'Courier New', Liberation Mono, Menlo, Monaco, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
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
    padding: 14px 32px
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
    opacity: 0.6
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-inverted:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.on-dark}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxWidth: 80px
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    imagePadding: "{spacing.lg}"
    nameTypography: "{typography.title-md}"
    refTypography: "{typography.caption}"
    priceTypography: "{typography.body-md}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    minHeight: 640px
    padding: "{spacing.section} {spacing.xl}"
    ctaVariant: button-primary
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    sublineTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    borderBottom: "1px solid {colors.hairline}"
  collection-nav:
    backgroundColor: transparent
    inactiveTextColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    activeIndicator: "2px solid {colors.primary}"
    height: 48px
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.mono-spec}"
    rowBorder: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  watch-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  watch-badge-limited:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.display-sm}"
    rounded: "{rounded.none}"
    inputBorderBottom: "1px solid {colors.hairline}"
    backdropColor: "rgba(43,51,63,0.6)"
  steel-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.steel}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 4px 12px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: none

## Components

### Buttons

**`button-primary`** — A solid #bf342d rectangle with `{rounded.none}`, uppercase Brown LL TT at 13px/1.5px letter-spacing, white label, 48px height. Hover steps to #ba251e (`{colors.primary-active}`); disabled uses `{colors.primary-disabled}` at 0.6 opacity. The hard unrounded geometry signals engineering instrument precision — there is no softness in an Oris button.

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` border and identical uppercase type treatment. Used alongside the primary on product pages for "Find a retailer" and "Add to wishlist" actions. The inverted variant (`button-secondary-inverted`) swaps to `{colors.on-dark}` border and text for deployment against dark hero panels.

**`button-ghost`** — Bare `{colors.primary}` text with an underline, no padding or border, used for inline editorial "Read more" links and footnote anchors.

### Navigation

**`nav-bar`** — 64px tall, `{colors.canvas}` background with a 1px `{colors.hairline}` bottom border. The Oris wordmark sits left at ≤80px wide; collection labels center in `{typography.nav-link}` (13px, 0.5px tracking); cart and search icons sit right. The dark variant (`nav-bar-dark`) renders over full-bleed hero imagery with `{colors.surface-dark}` fill and `{colors.on-dark}` text, no bottom border. The mega-menu drops as a full-width panel in `{colors.surface-card}` with hairline top and bottom rules.

**`collection-nav`** — A horizontal strip of watch family labels (Aquis, Divers Sixty-Five, ProPilot, Big Crown, Culture) in `{typography.title-sm}` uppercase. Inactive labels in `{colors.muted}`; the active label underlined by a 2px `{colors.primary}` bar anchored to the strip's bottom edge.

### Product Card

**`product-card`** — Strictly rectangular (`{rounded.none}`), 1px `{colors.hairline-soft}` border, `{colors.surface-card}` background. Watch photography renders with generous `{spacing.lg}` internal padding on all sides; no drop shadow. Collection family and reference number appear in `{typography.caption}` `{colors.muted}` above the model name in `{typography.title-md}`; price in `{typography.body-md}`. Limited references carry a `watch-badge-limited` chip overlaid at the top-left corner of the image area.

### Hero Banner

**`hero-banner`** — Full-bleed `{colors.surface-dark}` panel, minimum 640px tall. Headline in `{typography.display-xl}` (64px, weight 300) sits left-aligned with a short descriptor in `{typography.body-md}` and a `button-primary` below. On desktop the watch image bleeds to the right edge while text occupies the left half; on mobile the image stacks above the text block. The alternation between `{colors.canvas}` and `{colors.surface-dark}` sections across the scrolling page is the primary structural rhythm of the site.

### Spec Table

**`spec-table`** — Two-column table presenting technical watch data: Movement type, Calibre, Jewels, Power reserve, Water resistance, Case diameter, Strap material. Labels in `{typography.caption}` uppercase at `{colors.muted}`; values in `{typography.mono-spec}` (Consolas) at `{colors.ink}`. Each row separated by a 1px `{colors.hairline-soft}` rule, no outer border, `{spacing.base}` vertical padding per row. The monospace rendering of numbers ("300 m / 1,000 ft", "Cal. 400") reads as specification documentation rather than retail copy.

### Badges

**`watch-badge`** — A flat #bf342d rectangle in `{typography.button-sm}` uppercase applied to new-season releases and highlighted references. **`watch-badge-limited`** uses `{colors.ink}` fill for limited editions, collaborations, and numbered pieces — distinguishing rarity tier from novelty at a glance.

### Search Overlay

**`search-overlay`** — Full-viewport panel in `{colors.canvas}` over a `rgba(43,51,63,0.6)` scrim. The search input renders in `{typography.display-sm}` (28px) with no visible border except a 1px `{colors.hairline}` underline rule; results appear below as a vertical list in `{typography.title-md}`. No rounded corners anywhere in the overlay.

### Steel Chip

**`steel-chip`** — Small material or finish label (e.g. "Stainless Steel", "Bronze", "Titanium", "DLC") in `{colors.steel}` text on `{colors.surface-soft}` background with a 1px `{colors.hairline}` border. Used in filter panels and product detail sidebars to surface material options; the `{colors.steel}` (#73859f) directly references the visual character of brushed metal without illustration.

### Footer

**`footer`** — `{colors.ink}` (#2b333f) background in four columns: Collections, Services, Company, Legal. Column headings in `{typography.title-sm}` uppercase; links in `{typography.body-sm}` `{colors.on-dark}`. A newsletter signup field uses `text-input` styling with `button-primary` inline. No rounded corners; no decorative dividers beyond hairline rules.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger triggers full-screen drawer in `{colors.surface-dark}`; hero headline drops to `{typography.display-md}` (40px); spec table scrolls horizontally; collection-nav becomes scrollable horizontal strip |
| Tablet | 744–1128px | Two-column product grid; collection-nav remains visible; hero text column at 55% width with image bleeding right |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with mega-menu dropdown; hero splits 50/50 text and image |
| Wide | > 1440px | Layout locked to 1440px max-width and centered; four-column product grid; hero image fills right half at full bleed |

### Touch Targets

- All interactive elements maintain a minimum 44×44px touch target
- `collection-nav` tab items extend tap area with 16px vertical padding beyond the visible label
- Entire product card surface is tappable on mobile
- Mobile nav drawer rows use 56px row height minimum
- Badge and chip elements are non-interactive display only; no touch target requirement

### Collapsing Strategy

- Top nav collapses to hamburger icon at <744px; drawer slides in from left over the dark scrim
- Hero layout stacks image above, text below at <744px (reversal of desktop order)
- Spec table remains two-column at all breakpoints; table scrolls horizontally if column overflow occurs at mobile
- Footer four-column grid collapses to a single-column accordion at <744px with `{colors.hairline}` dividers between sections
- Product grid: 1 col (mobile) → 2 col (tablet) → 3 col (desktop) → 4 col (wide)
- `collection-header` headline steps down: `{typography.display-xl}` on desktop → `{typography.display-md}` on tablet → `{typography.display-sm}` on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color was set; mobile browser chrome tint color could not be confirmed
- Exact nav-bar height and mega-menu column layout were inferred from visual inspection, not pixel-measured from source
- Whether `{colors.steel}` (#73859f) appears in live navigation or primarily in embedded video player UI (VideoJS) could not be confirmed — treat as approximate secondary accent
- `#ffcc66` and `#ffa3a5` appear in the extracted palette; their precise UI roles (sale badge, error highlight, rating star) could not be confirmed from static extraction alone
- `#007aff` and `#0000ff` are excluded as system/browser defaults rather than brand tokens
- `#66a8cc` appears in the palette but is likely a VideoJS control or system highlight; excluded from brand tokens
- Exact Brown LL TT weight variants licensed on the live site (likely 300, 400, 500) could not be enumerated; weight 700+ may not be part of the licensed set
- Animation timing for hero transitions, hover states, and mega-menu opens could not be extracted from static analysis
