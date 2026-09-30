---
version: alpha
name: "Off-White"
source_url: "https://off---white.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every physical Off-White garment ships with an industrial zip-tie tag and a label printed in quotation marks — "FOR WALKING", "FOR DISPLAY" — the conceptual gesture that separates Virgil Abloh's streetwear house from pure fashion retail and plants it closer to institutional critique. The digital storefront carries that same rigour: a near-absolute black (#171717) field broken only by the signature caution-tape orange (#ff6200), which fires on sale callouts, editorial badges, and price highlights with the same declarative confidence it stamps on physical packaging. Whitespace is not generous here; the grid presses close, editorial photography bleeds to the edge, and the typography is stripped to a grotesque without ornament — uppercase labels locked in tight tracking, prices set large, and the trademarked Off-White™ wordmark carrying all the warmth the rest of the system deliberately refuses. The canvas itself is barely off-white (#fffffe), maintaining just enough temperature to distinguish from the hottest whites in photo treatments. Gray (#c1c1c1) appears as a structural note — hairlines, muted metadata, secondary text — while a warm beige-rose (#bbaaaa) surfaces on product swatches and body-copy accents to prevent the palette from reading as purely monochrome. Navigation is a horizontal band in deep black with white type and no hover underlines — just a colour shift and cursor change, trusting the user's literacy entirely. Product cards are flush to their edges with no rounding ({rounded.none}), stacked photography on top and stark metadata below: price prominent, SKU minimal, out-of-stock conveyed by a single grey flag rather than a disabled opacity wash. The diagonal caution-stripe — alternating black and #ff6200 at 45 degrees — recurs across announcement bars and campaign panels, the most recognisable graphic device in streetwear translated faithfully from physical hangtag to screen. The overall register is closer to a gallery wall than a conventional storefront: clinical enough to communicate premium, warmed just enough by the orange pulse to avoid institutional coldness.

colors:
  primary: "#ff6200"
  primary-active: "#cc4e00"
  primary-disabled: "#f7c9aa"
  ink: "#171717"
  body: "#1d1d1b"
  muted: "#c1c1c1"
  muted-warm: "#bbaaaa"
  hairline: "#c1c1c1"
  hairline-soft: "#e5e5e5"
  canvas: "#fffffe"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  brand-black: "#171717"
  brand-orange: "#ff6200"
  brand-orange-alt: "#ef7d00"
  stripe-dark: "#171717"
  stripe-light: "#ff6200"
  scrim: "#000001"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
    textTransform: uppercase
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.36
    letterSpacing: 0.2px
  label-mono:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 2px
    textTransform: uppercase
  quotation-tag:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 9px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 1px
    textTransform: uppercase
  price-display:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.5px

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
    padding: 14px 24px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-black:
    backgroundColor: "{colors.brand-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 24px
    height: 48px
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 13px 23px
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
    backgroundColor: "{colors.brand-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: none
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price-display}"
    metaTypography: "{typography.caption}"
    textColor: "{colors.ink}"
    metaColor: "{colors.muted}"
  hero-editorial:
    backgroundColor: "{colors.brand-black}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 80vh
    padding: "{spacing.xxl}"
    imagePosition: center
  quotation-badge:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.quotation-tag}"
    border: "1px solid {colors.muted}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  diagonal-stripe-banner:
    backgroundPattern: "repeating-linear-gradient(45deg, {colors.stripe-dark}, {colors.stripe-dark} 10px, {colors.stripe-light} 10px, {colors.stripe-light} 20px)"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-mono}"
    height: 36px
  sale-badge:
    backgroundColor: "{colors.brand-orange}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-mono}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  oos-badge:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.label-mono}"
    border: "1px solid {colors.muted}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    size: 48px
  category-filter:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    textColorActive: "{colors.ink}"
    typography: "{typography.label-mono}"
    rounded: "{rounded.none}"
    borderBottom: "2px solid transparent"
    borderBottomActive: "2px solid {colors.ink}"
  search-overlay:
    backgroundColor: "{colors.brand-black}"
    textColor: "{colors.on-dark}"
    inputBorder: "1px solid {colors.muted}"
    inputBorderFocus: "1px solid {colors.on-dark}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.brand-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.muted-warm}"
    padding: "{spacing.section}"

## Components

### Buttons
**`button-primary`** — A 48px tall flush rectangle in brand orange (#ff6200) with white all-caps type at 1.5px letter-spacing. On hover, the fill deepens to `{colors.primary-active}` (#cc4e00) — a snap rather than a gradient, keeping the interaction feel binary and decisive. The disabled state washes out to a light peach (`{colors.primary-disabled}`) rather than using opacity, preserving legibility without implying interactivity. Used for transactional moments — newsletter subscribe, checkout confirm — where the orange voltage serves as a functional signal rather than a purely editorial one.

**`button-black`** — Identical geometry to `button-primary` but in `{colors.brand-black}`. Serves as the dominant "Add to Cart" and primary commerce CTA across the product detail page. No rounding anywhere; the hard corner is deliberate and consistent with the industrial material reference.

**`button-secondary`** — A transparent 48px frame with a 1px solid `{colors.ink}` border and black all-caps label. Appears paired beneath the primary CTA for secondary actions (e.g., "Save to Wishlist"). The border snaps to 2px on hover — no colour change, just a weight shift.

### Labels and Badges
**`quotation-badge`** — The brand's most distinctive UI motif: a 1px-bordered rectangle rendering a short all-caps descriptor wrapped in typographic quotation marks — `"SAMPLE"`, `"ARCHIVAL"`, `"NEW ARRIVAL"`. Set in `{typography.quotation-tag}` (9px, 700 weight, 1px letter-spacing) in `{colors.muted}`, it reads as curatorial metadata rather than a marketing shout. Derived directly from the physical garment hangtag convention.

**`diagonal-stripe-banner`** — A 36px announcement band generated by a CSS `repeating-linear-gradient` at 45° alternating `{colors.stripe-dark}` and `{colors.stripe-light}` at 10px intervals. Used for site-wide alerts, campaign launches, and sale signals. The caution-tape reference is explicit and intentional; text is set in `{typography.label-mono}` in white, centred vertically.

**`sale-badge`** — A flush, unrounded rectangle in `{colors.brand-orange}` with white `{typography.label-mono}` type. Positioned absolute to the top-left of the product image at 4px inset. No shadow, no rounding.

**`oos-badge`** — Same rectangle geometry, but transparent with a 1px solid `{colors.muted}` border. Signals out-of-stock with the same visual grammar as the sale badge, at a lower energetic register.

### Product Card
**`product-card`** — A 3:4 portrait image tile that bleeds to all four card edges with `{rounded.none}`. Below the image: product name in `{typography.body-md}`, colorway descriptor in `{typography.caption}` at `{colors.muted}`, price prominent in `{typography.price-display}`. There is no elevation shadow or rounding on hover; instead, the image swaps to an alternate editorial angle. The gallery-wall flatness is deliberate — hover elevation would signal a Shopify template, not a fashion house.

### Navigation
**`nav-bar`** — A 56px full-bleed deep black (#171717) bar with no bottom border. The Off-White™ wordmark sits left-aligned in white. Bag, search, and account icons align right as outlined white glyphs. Horizontal category links occupy the centre at `{typography.nav-link}` — on hover, type colour shifts to `{colors.brand-orange}`; no underline appears. On mobile, all links collapse behind a hamburger that triggers a full-screen black overlay with items stacked vertically.

### Forms and Filters
**`text-input`** — Square-cornered 48px input fields. Idle border is 1px `{colors.hairline}`; focus border snaps immediately to 1px `{colors.ink}` — no animated transition. Placeholder text in `{colors.muted}`. The hard-corner, snap-focus behaviour matches the brand's rejection of rounded, softened UI conventions.

**`size-selector`** — 48×48px square tiles. Idle: `{colors.hairline}` border, `{colors.ink}` type in `{typography.title-sm}`. Selected: border upgrades to 1px `{colors.ink}` with no background fill change. Unavailable sizes display a diagonal line drawn in `{colors.muted}` across the full tile — not hidden, not ghosted, explicitly marked as absent stock.

**`category-filter`** — Inline horizontal tabs in `{typography.label-mono}` uppercase. Active tab gains a 2px solid `{colors.ink}` bottom border; inactive tabs render in `{colors.muted}`. No pill backgrounds, no fills — the underline-only affordance keeps the filter row typographic rather than widget-like.

### Hero
**`hero-editorial`** — Full-bleed 100vw × 80vh minimum with editorial fashion photography. Headline at `{typography.display-xl}` renders in `{colors.on-dark}` anchored to the lower-left quadrant with `{spacing.xxl}` padding. No overlay scrim — photography is art-directed to carry sufficient contrast natively. On lighter campaign images, a black `{colors.ink}` headline variant is applied.

### Search
**`search-overlay`** — A full-screen `{colors.brand-black}` takeover triggered by the nav search icon. A single borderless text input at large scale dominates the top third, with a 1px `{colors.muted}` bottom border that upgrades to `{colors.on-dark}` on focus. Recent searches and trending terms appear below in `{typography.label-mono}` in `{colors.muted}`.

### Footer
**`footer`** — Full-width `{colors.brand-black}` panel in a 4-column link grid on desktop. Links in `{typography.body-sm}` white, hover state shifts to `{colors.brand-orange}`. Social icons as outlined white glyphs. The Off-White™ wordmark repeats at reduced scale across the bottom alongside legal text in `{colors.muted-warm}`. No divider lines — sections are separated by column gaps alone.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to full-screen black overlay; hero headline reduces to `{typography.display-md}`; size-selector tiles maintain 44px minimum touch target; quotation-badge metadata hidden on product card, visible on PDP only |
| Tablet | 744–1128px | Two-column product grid; nav links partially visible with overflow into "More" dropdown; hero remains full-bleed at reduced padding; diagonal-stripe-banner text truncates to a short label |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with all category links visible; hero at full `{typography.display-xl}`; filter row pinned below nav on scroll |
| Wide | > 1440px | Layout centres at 1440px max-width; product grid holds four columns with wider gutters; hero bleeds edge-to-edge beyond content container |

### Touch Targets
- All interactive tiles (size-selector, category-filter tabs, nav links) maintain minimum 44×44px tap area regardless of visual size
- The hamburger icon renders at 48×48px tap zone even when the visual glyph is 20px
- Category-filter tabs switch to a horizontally scrollable strip with no line-wrapping on mobile
- Product cards are full-width on mobile; the entire card is a tap target to the PDP

### Collapsing Strategy
- The diagonal-stripe-banner collapses to a single-line marquee on screens narrower than 375px
- The 4-column footer link grid collapses to a single-column accordion on mobile, each heading toggles its link group
- On mobile product cards, only name and price are shown; colorway descriptor and quotation-badge are deferred to the PDP
- The search overlay remains full-screen at all breakpoints; no sidebar variant

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font families were extracted from the live site — Off-White likely serves type through a protected CDN or CSS custom-property system. The `Helvetica Neue` stack used here is consistent with the brand's documented industrial grotesque aesthetic but the precise licensed cut (potentially a custom or restricted typeface) is unconfirmed.
- The extracted blues (#253b80, #016fd0, #179bd7, #7375cf, #00a2e5, #0047ba, #1434cb, #222d65) and additional reds/ambers (#eb001b, #ff5f00, #f79e1b) are identifiable as PayPal, Visa, and Mastercard brand colors from the checkout payment row and have been excluded from the brand palette entirely.
- The role of #ffb3c7 (pale pink) and #bbaaaa (warm beige-rose) is ambiguous — they may be seasonal product colorway swatches rather than recurring system UI tokens.
- #ef7d00 and #ff6200 are both present; which is the canonical brand orange and whether they serve distinct semantic roles (e.g., hover vs. idle) could not be determined from static extraction.
- Exact button corner radius is unconfirmed — the brand aesthetic strongly implies {rounded.none} but the live site may apply 1–2px for sub-pixel rendering on dark backgrounds.
- Motion values (easing curves, transition durations) were not extractable; the brand register suggests very short (<150ms), snappy transitions with minimal easing.
- Product grid column count, gutter width, and pinned-filter scroll behaviour could not be confirmed from static extraction.
