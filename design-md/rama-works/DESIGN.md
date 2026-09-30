---
version: alpha
name: "RAMA WORKS"
source_url: "https://ramaworks.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Clarkson display type pressed against a near-void #111111 canvas gives RAMA WORKS the visual weight of machined aluminum billet — the typographic choice signals that this is an engineering catalog for people who debate gasket-mount flex and switch pre-travel in tenths of millimeters, not a lifestyle accessories shop. The single chromatic departure from the near-monochrome palette is #f0523d, a vivid coral-red that surfaces on primary calls-to-action and select interactive accents; everywhere else the system cycles through graduated charcoals (#131313, #272727, #3e3e3e) with primary text rendered in #f6f6f6 rather than pure white, softening the tonal snap without compromising legibility on dark surfaces. Inconsolata — the monospace stack present in the site's font-family declarations — earns a structural role in spec readouts: switch actuation force, board weight in grams, plate thickness, travel distance. Numbers set in a fixed-pitch face read as measurements rather than marketing copy, and the font choice alone repositions the product as an instrument. Proxima Nova handles navigation labels and body prose with clean geometric neutrality so the photography of anodized aluminum cases and brass weight bars can operate without typographic competition. The design logic is deliberately sparse: product cards float on {rounded.xs} corners over {colors.surface-card} fields, maintaining the flat geometry of CNC machining. Buttons are near-rectangular ({rounded.xs}), resisting the friendly pill forms that consumer-electronics brands favor. The coral {colors.primary} activates group-buy entry points, add-to-cart states, and the few hover cues that break the otherwise static dark surface — appearing rarely enough to read as a functional signal rather than decoration. The total experience mirrors the product: a deliberately constrained material palette, almost zero surface ornamentation, and the confidence to let dark silence carry the brand's authority.

colors:
  primary: "#f0523d"
  primary-active: "#cc3a2a"
  primary-disabled: "#5a2018"
  ink: "#f6f6f6"
  body: "#d0d0d0"
  muted: "#aaaaaa"
  hairline: "#2f2f2f"
  hairline-soft: "#222222"
  canvas: "#111111"
  surface-soft: "#131313"
  surface-card: "#1c1c1c"
  surface-mid: "#272727"
  surface-raised: "#3e3e3e"
  on-primary: "#ffffff"
  on-dark: "#f6f6f6"
  scrim: "#080808"
  badge-limited: "#f0523d"
  badge-sold-out: "#3e3e3e"
  badge-available: "#7dbb00"

typography:
  display-xl:
    fontFamily: "'Clarkson', Helvetica Neue, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -1.5px
  display-md:
    fontFamily: "'Clarkson', Helvetica Neue, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.8px
  display-sm:
    fontFamily: "'Clarkson', Helvetica Neue, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.4px
  title-md:
    fontFamily: "'proxima-nova', Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'proxima-nova', Helvetica Neue, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.4px
    textTransform: uppercase
  body-md:
    fontFamily: "'proxima-nova', Helvetica Neue, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-nova', Helvetica Neue, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-nova', Helvetica Neue, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  mono-md:
    fontFamily: "'Inconsolata', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  mono-sm:
    fontFamily: "'Inconsolata', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  label-caps:
    fontFamily: "'proxima-nova', Helvetica Neue, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'proxima-nova', Helvetica Neue, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'proxima-nova', Helvetica Neue, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'proxima-nova', Helvetica Neue, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1.2px
    textTransform: uppercase
  price-display:
    fontFamily: "'Inconsolata', 'Courier New', monospace"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 28px
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
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-mid}"
    borderColor: "{colors.surface-raised}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: none
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.surface-raised}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoFontFamily: "'Clarkson', sans-serif"
  nav-dropdown:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.body}"
    padding: "{spacing.base}"
    hoverBorder: "1px solid {colors.surface-raised}"
    hoverElevation: none
  product-card-status-badge:
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.muted}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  badge-available:
    backgroundColor: "{colors.badge-available}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted}"
    minHeight: 80vh
    layout: fullbleed
    overlayColor: "{colors.scrim}"
    overlayOpacity: 0.35
    ctaMarginTop: "{spacing.xl}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    keyTypography: "{typography.label-caps}"
    keyColor: "{colors.muted}"
    valueTypography: "{typography.mono-md}"
    valueColor: "{colors.ink}"
    rowBorder: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.xs}"
  colorway-swatch:
    size: 24px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.primary}"
    gap: "{spacing.sm}"
    tooltipTypography: "{typography.caption}"
    tooltipBackgroundColor: "{colors.surface-mid}"
    tooltipTextColor: "{colors.ink}"
  group-buy-countdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    numberTypography: "{typography.display-sm}"
    labelTypography: "{typography.label-caps}"
    labelColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
  image-gallery:
    backgroundColor: "{colors.canvas}"
    thumbnailBorder: "1px solid {colors.hairline-soft}"
    thumbnailBorderActive: "1px solid {colors.primary}"
    thumbnailRounded: "{rounded.xs}"
    thumbnailSize: 64px
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.ink}"
    headingTypography: "{typography.label-caps}"
    headingColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — A near-rectangular slab with {rounded.xs} corners, coral #f0523d fill, and all-caps Proxima Nova tracking at 1px — it reads as a precision control rather than an invitation. Hover darkens to {colors.primary-active} (#cc3a2a) with no scale transform; the state change is pure color. Disabled state drops to {colors.primary-disabled} with muted text, maintaining the flat aesthetic without graying to an ambiguous neutral.

**`button-secondary`** — Transparent fill with a 1px {colors.hairline} border and {colors.ink} text; on hover, the background lifts to {colors.surface-mid} and the border thickens visually by color shift to {colors.surface-raised}. Functions as the outline-only sibling for "Learn More" and colorway-change actions.

**`button-ghost`** — No border, no fill, {colors.muted} text. Used for lower-hierarchy actions like "View all" or pagination nudges. The absence of chrome keeps focus on product content.

### Nav Bar

**`nav-bar`** — 60px tall, {colors.canvas} background with a 1px {colors.hairline-soft} bottom border that only becomes visible when the page scrolls past the hero. Navigation links are Proxima Nova all-caps at 12px / 1.2px tracking — the typographic register of an instrument panel, not a marketing header. The wordmark "RAMA WORKS" uses Clarkson at a slightly larger optical weight. Dropdowns open as flat {colors.surface-soft} panels with their own 1px border, no shadows.

### Product Card

**`product-card`** — A dark {colors.surface-card} tile with {rounded.xs} corners and a near-invisible 1px {colors.hairline-soft} border that separates cards from the canvas without casting shadows. Product name renders in {typography.title-md} (Proxima Nova 600), price in {typography.price-display} (Inconsolata 18px) — the monospace price reinforces engineering provenance. Hover shifts the border to {colors.surface-raised} but makes no elevation or scale change; the interaction is deliberately understated. Status badges ({badge-limited}, {badge-sold-out}, {badge-available}) sit flush to the card corner with zero radius — hard-edged stencil stamps.

### Hero

**`hero`** — Full-bleed photography or render occupying at minimum 80vh, with a {colors.scrim} overlay at 0.35 opacity to maintain text legibility. Heading in {typography.display-xl} (Clarkson 56px / weight 300) creates the impression of engraved lettering on the product photograph. Subhead in {typography.body-md} at {colors.muted} keeps the frame quiet. CTA button pair sits {spacing.xl} below the subhead.

### Spec Table

**`spec-table`** — The most distinctively RAMA WORKS component: two-column rows where keys render in {typography.label-caps} (Proxima Nova 700 / all-caps / 1.2px tracking) and values in {typography.mono-md} (Inconsolata 14px). The monospace value column aligns numbers by decimal point across rows. Background is {colors.surface-soft}, row dividers are 1px {colors.hairline}, and the whole block sits in a {rounded.xs} container. This is where materials, dimensions, and compatibility information live — the component that closes the sale for the target buyer.

### Colorway Swatch

**`colorway-swatch`** — 24px filled circles with {rounded.full}, spaced at {spacing.sm} gaps. Unselected swatches have a transparent 2px border; selected swatches show a 2px {colors.primary} ring, the only place on the PDP where coral appears at rest without a user action. Tooltips use {typography.caption} in {colors.surface-mid} containers on hover.

### Group-Buy Countdown

**`group-buy-countdown`** — A segmented timer block in {colors.surface-card} with 1px {colors.hairline} border and {rounded.xs} corners. Each segment (days / hours / minutes / seconds) shows a number in {typography.display-sm} (Clarkson 24px) and a label in {typography.label-caps} at {colors.muted}. The countdown is functional infrastructure — it creates commitment without decorative urgency.

### Announcement Bar

**`announcement-bar`** — 36px full-width strip in {colors.primary} with centered {typography.label-caps} text in {colors.on-primary}. Used for active group-buy windows, shipping notices, and policy updates. The coral fill at full viewport width is one of the few moments where the primary accent dominates rather than punctuates.

### Footer

**`footer`** — {colors.surface-soft} background separated from page content by a 1px {colors.hairline} top border. Section headings in {typography.label-caps} at {colors.ink}; link lists in {typography.body-sm} at {colors.body} with hover to {colors.ink}. No decorative elements — the footer is a directory, not a brand statement.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger icon + wordmark only; hero heading drops to {typography.display-md}; spec table scrolls horizontally within a fixed container; colorway swatches wrap to two rows max |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links, secondary items move into a "More" overflow; hero heading at {typography.display-md}; spec table full-width |
| Desktop | 1128–1440px | Three or four-column product grid; full horizontal nav with dropdown support; hero at full {typography.display-xl}; spec table two-column layout at comfortable reading width |
| Wide | > 1440px | Max content width capped at ~1400px with equal left/right margins; product grid stays at four columns; hero imagery scales to fill without upscaling |

### Touch Targets

- All interactive buttons and nav links minimum 44×44px tap area
- Colorway swatches expand invisible tap zone to 40×40px even though visual size is 24px
- Footer links padded to 44px row height on mobile
- Announcement bar text remains selectable but the strip itself is non-interactive unless a CTA link is present

### Collapsing Strategy

- Primary nav links collapse behind a hamburger at < 744px; the drawer opens from the left over a {colors.scrim} overlay
- Product card details (weight, material sub-label) are hidden below 744px, showing only name and price
- Spec table reflows to a stacked single-column layout below 480px, each key-value pair becoming its own full-width row
- Group-buy countdown condenses to two rows (days/hours / minutes/seconds) on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed border-radius values extracted from live site; {rounded.xs} (2px) values inferred from engineering-aesthetic brand positioning and comparable precision-goods stores
- Clarkson weight variants (whether the brand uses 200 / 300 / 400 exclusively or also 600–700) could not be confirmed from extraction; display tokens use 300 based on the observed light-weight editorial style common to this brand tier
- Exact nav height (60px) and announcement bar height (36px) are estimates; live DOM inspection would confirm
- Social icon colors (#3b5998, #0099e5, #f94877, etc.) were present in the extraction and excluded from the brand palette — they are third-party icon font colors, not RAMA WORKS brand tokens
- No hover animation timing or easing values extracted; duration and curve defaults (150ms ease-in-out) should be validated against live site interactions
- Mobile-specific typography scale not confirmed; breakpoint font-size reductions inferred from convention
- Product photography art direction (white studio vs. lifestyle vs. dark studio) not verifiable from extraction alone
