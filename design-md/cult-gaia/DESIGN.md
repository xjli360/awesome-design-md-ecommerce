---
version: alpha
name: "Cult Gaia"
source_url: "https://cultgaia.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The warm ivory canvas (#fffef8) — not white but the color of bleached linen or dried pampas grass — is the first perceptual decision separating Cult Gaia from fashion peers operating on sterile white grounds. Against it, SURT Ultra Bold Expanded stacks in monumental compressed letterforms atop every editorial section: the typeface functions less as text and more as architectural volume, each headline occupying space the way the brand's signature lattice bags and geometric mules occupy the frame in campaign photography. LoveRegular arrives as editorial caption or secondary accent, its organic curves creating deliberate tension between engineered mass and handmade warmth. The near-black #393939 does all UI heavy lifting — nav links, body copy, and primary CTAs set against the warm ivory at this tone rather than pure black, shaving just enough contrast to feel editorial rather than utilitarian. Crimson (#af1d32) and terracotta (#a94120) surface surgingly: sale badges, reduced-price states, and seasonal accents carry urgency without altering the neutral temperature of the broader palette. Sage (#bac8c3) and warm taupe (#c8c7ba) fill the mid-register as hover tints, alternating editorial row backgrounds, and muted subtitle color. Corners are near-absent throughout — {rounded.none} to {rounded.xs} dominate across buttons, cards, and inputs, reflecting the brand's debt to clean geometry and artisanal construction. Product photography bleeds edge-to-edge on borderless cards, creating a gallery feel rather than a catalogued grid. The announcement strip rides every page in the near-black ground with tightly tracked Inter against {colors.on-dark}, while the main navigation holds as a minimal horizontal bar in {colors.ink} against {colors.canvas}, collapsing to a hamburger at mobile. Category filters and size selectors use flat rectangular chips with hairline outlines at {colors.hairline} that fill to {colors.ink} on selection — restraint maintained through every conversion touchpoint.

colors:
  primary: "#af1d32"
  primary-active: "#8a1527"
  primary-disabled: "#d9a0a8"
  terracotta: "#a94120"
  terracotta-active: "#8b3419"
  ink: "#393939"
  body: "#393939"
  muted: "#b8b8b8"
  muted-soft: "#bababa"
  hairline: "#e7e7e7"
  hairline-soft: "#eeeeee"
  canvas: "#fffef8"
  surface-soft: "#eeeeee"
  surface-card: "#fffef8"
  warm-gray: "#c8c7ba"
  sage: "#bac8c3"
  on-primary: "#fffef8"
  on-dark: "#fffef8"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Surt Ultra Bold Exp', 'SURT', Arial, sans-serif"
    fontSize: 72px
    fontWeight: 800
    lineHeight: 0.95
    letterSpacing: -1.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Surt Ultra Bold Exp', 'SURT', Arial, sans-serif"
    fontSize: 42px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -0.5px
    textTransform: uppercase
  display-sm:
    fontFamily: "'SURT', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.2px
  editorial-accent:
    fontFamily: "'LOVE', 'LoveRegular', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Inter, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  price-display:
    fontFamily: "Inter, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  nav-link:
    fontFamily: "Inter, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "Inter, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  announcement:
    fontFamily: "Inter, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.06em

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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
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
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.announcement}"
    height: 36px
    padding: "0 {spacing.base}"
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageSizing: cover
    imageAspectRatio: "3/4"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.sm} 0"
    border: none
  product-card-hover:
    imageTransform: scale(1.03)
    transition: transform 0.4s ease
  product-badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 3px 8px
    position: absolute
    placement: top-left
  product-badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 3px 8px
    position: absolute
    placement: top-left
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.editorial-accent}"
    imageLayout: full-bleed
    contentPosition: bottom-left
    padding: "0 {spacing.xxl} {spacing.xxl}"
  hero-editorial-row:
    backgroundColor: "{colors.warm-gray}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
    textAlign: center
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 6px 12px
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 6px 12px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 44px
    width: 44px
  size-selector-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  size-selector-sold-out:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
    textDecoration: line-through
  wishlist-icon:
    iconColor: "{colors.muted}"
    hoverColor: "{colors.primary}"
    size: 20px
    position: absolute
    placement: top-right
    tapAreaPadding: 12px
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.display-sm}"
    rounded: "{rounded.none}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.section}"
  category-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    subTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0 {spacing.lg}"
    textAlign: center
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.section}"
    borderTop: none

## Components

### Buttons
**`button-primary`** — Flat rectangular with no rounding, set in uppercase 13px Inter at 0.08em tracking. The `{colors.ink}` (#393939) fill on the warm ivory ground reads as authoritative without aggression; hover deepens to `{colors.scrim}` full black. Disabled state shifts to `{colors.muted}` fill, staying within the palette's neutral temperature rather than signaling error.

**`button-secondary`** — Same 48px height and uppercase treatment as primary, inverted to `{colors.canvas}` fill with a 1px `{colors.ink}` border. Used for secondary conversion actions such as "Save to Wishlist" or "Continue Shopping" without competing with the primary CTA.

**`button-ghost`** — Zero background, 1px `{colors.hairline}` border. Handles low-priority utility actions — filter resets, "View All", pagination links — without drawing visual weight.

### Navigation
**`nav-bar`** — A 56px horizontal bar in `{colors.canvas}` carrying the Cult Gaia wordmark and category links in 12px uppercase `{typography.nav-link}`. A 1px `{colors.hairline}` bottom rule activates on scroll to separate the nav from page content. Cart, search, and account sit flush right. The bar is intentionally low-chrome, trusting the SURT display type below it to carry brand identity.

**`announcement-bar`** — A 36px `{colors.ink}` strip anchored above the nav, carrying the 10% first-order offer in tight `{typography.announcement}` against `{colors.on-dark}`. Sits above all other fixed elements. Dismissible on mobile via an inline close glyph.

### Product Cards
**`product-card`** — Borderless on the `{colors.canvas}` ground. Portrait 3:4 images fill the tile width with no interior padding or enclosing rule — photography edge-to-edge creates a gallery register rather than a catalog. Product name below in `{typography.body-sm}`, price below that in `{typography.price-display}`. Sale prices surface in `{colors.primary}` crimson beside a struck-through original. On hover the image scales to 103% over 400ms ease; no secondary image swap, no text overlay.

**`product-badge-sale`** and **`product-badge-new`** — Zero-radius rectangular labels positioned absolute top-left inside the image frame. Sale renders on `{colors.primary}`, new arrivals on `{colors.ink}`. Typography at `{typography.caption}` — deliberately small to avoid overwhelming the image.

### Filters and Size Selection
**`filter-chip`** — Flat rectangular chips in `{colors.canvas}` with a 1px `{colors.hairline}` outline. Active state fills immediately to `{colors.ink}` with `{colors.on-dark}` text — no transition animation, consistent with the brand's directness. Chips horizontally scroll at mobile below the category header.

**`size-selector`** — 44×44px square targets preserving a uniform touch surface. Sold-out sizes render `{colors.muted}` text with `line-through` rather than a diagonal slash, keeping the visual register clean.

### Hero and Editorial
**`hero-banner`** — Full-bleed photography at 100vw, headline in `{typography.display-xl}` anchored bottom-left. SURT Ultra Bold Expanded at 72px creates architectural dominance without additional graphic framing; `{typography.editorial-accent}` in LoveRegular provides a softer subline. Minimal padding inside the text block so type appears to rest at the image's edge.

**`hero-editorial-row`** — Text-only interstitial rows with `{colors.warm-gray}` (#c8c7ba) background. Used between product grid sections or to frame a campaign concept. Headlines in `{typography.display-md}`, body in `{typography.body-md}`, centered or left-aligned by editorial direction.

### Search
**`search-overlay`** — Full-screen `{colors.canvas}` takeover with a single large text input in `{typography.display-sm}`. A single `{colors.hairline}` line under the input field is the only border element. Results populate in a plain list below with no category group headers.

### Footer
**`footer`** — Dark `{colors.ink}` field carrying a multi-column link grid, email capture, and legal copy. Column headings in `{typography.title-sm}`, links in `{typography.body-sm}`, all in `{colors.on-dark}`. Email input inverts to `{colors.canvas}` fill on the dark ground. No divider lines between columns at desktop — whitespace alone delineates zones.

### Wishlist
**`wishlist-icon`** — Inline heart icon at 20px, resting at `{colors.muted}` and switching to `{colors.primary}` crimson on hover or toggle. State change is immediate, no scale or fill animation. Touch target padded to 40px+ around the 20px glyph.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Two-column product grid; hamburger nav replacing link set; announcement bar dismissible; hero headline drops to `{typography.display-md}` ~42px; filter chips enter horizontal scroll; size selector grid wraps |
| Tablet | 744–1128px | Two- to three-column product grid; nav may show abbreviated link set or full set with tighter spacing; hero type at full `{typography.display-xl}` with narrower side margins |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav with all category links visible; hero runs full viewport width |
| Wide | > 1440px | Content max-width capped at ~1440px; side margins expand symmetrically; product grid holds at four columns |

### Touch Targets
- All buttons and inputs minimum 44px height
- Size selectors maintain 44×44px on touch — no reduction
- Nav links padded to minimum 48px effective tap height inside the hamburger drawer
- Wishlist icon tap area expanded to 40px centered on 20px glyph
- Filter chips minimum 36px height with horizontal padding for comfortable tap

### Collapsing Strategy
- Nav collapses to hamburger at < 744px; drawer slides from left on `{colors.canvas}` ground with full category hierarchy
- Filter panel becomes a "Filter & Sort" bottom sheet at mobile; chips convert to list items with toggle inside the sheet
- Hero editorial row stacks to single column at mobile with halved vertical padding
- Footer four-column grid collapses to two-column at tablet, single-column accordion at mobile with `{colors.hairline}` dividers and expand chevrons
- Category header subtext hides at mobile to reduce vertical stack height

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- SURT and LoveRegular are confirmed present in font stacks but exact weight values, size scales, and @font-face parameters were not extractable — display sizes above are inferred from brand convention
- Button background color for primary CTAs not confirmed from extraction; near-black `{colors.ink}` (#393939) is inferred from dominant palette and fashion-brand convention rather than direct observation
- Hover and focus transition timing (duration, easing) not captured from live CSS
- Exact nav height not confirmed; 56px is an estimate consistent with fashion e-commerce norms
- Product card secondary image (hover swap) behavior not confirmed — scale-only hover above is inferred
- Crimson (#af1d32) vs. terracotta (#a94120) usage split (which drives sale badges vs. which drives seasonal accents) not confirmed
- No icon system or SVG glyph specifications extracted
- LoveRegular specific pairing contexts and editorial size usage not confirmed beyond detection in font stack
- Mobile drawer animation direction and duration not available from extraction
