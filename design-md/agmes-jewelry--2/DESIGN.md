---
version: alpha
name: "Agmes"
source_url: "https://agmesnyc.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The palette runs from #121212 to #fafafa without a single chromatic accent — a total commitment that strips the Shopify canvas to a gallery wall so that cast bronze, open-form rings, and hand-formed sculpture carry all the color themselves. AGMES NYC presents its objects the way a museum presents artifacts: generous whitespace, type that recedes rather than competes, and product photography scaled to command the viewport. Raleway at weight 300 with wide letter-spacing echoes the open negative space inside the brand's sculptural forms — headlines breathe at roughly 0.08em tracking, letting each letterform stand as an individual element rather than a compressed block. The monospace stack surfaces in secondary callouts (material provenance, edition notes), borrowing the precision of a workshop specification sheet and setting it quietly against editorial softness. Buttons sit at `{rounded.none}` — zero radius, no softening conceit — matching the rectilinear rigor of the jewelry. Product cards present on near-white (#fafafa) ground separated by hairline borders in #dedede, just enough to register edges without introducing noise. Navigation renders in small-caps Raleway with extended tracking, keeping the header bar architecturally thin and undemanding. The mid-gray spectrum (#555555 to #777777) handles secondary prose and captions, graduating naturally between near-black ink and pale canvas without ever reaching for an additional hue. Price and material labels use the monospace stack at 11px, signaling workshop precision inside an otherwise editorial layout. This monochromatic discipline — never once broken by a warmth or color flourish — reads as confidence rather than limitation. AGMES lets the objects earn all attention while the interface becomes invisible.

colors:
  primary: "#191919"
  primary-active: "#121212"
  primary-disabled: "#dedede"
  ink: "#191919"
  ink-deep: "#121212"
  body: "#555555"
  muted: "#777777"
  hairline: "#dedede"
  canvas: "#fafafa"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#fafafa"

typography:
  display-xl:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: 0.08em
  display-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.06em
  title-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.04em
  title-sm:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.06em
  body-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.01em
  body-sm:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.01em
  caption:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.14em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  price:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  product-name:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0.05em
  material-label:
    fontFamily: "monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
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
    backgroundColor: "{colors.ink-deep}"
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
    padding: 13px 31px
    height: 44px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    padding: "{spacing.sm}"
    productNameTypography: "{typography.product-name}"
    priceTypography: "{typography.price}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    layout: "full-bleed image, centered or bottom-left text"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    minHeight: 80vh
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    descriptionMaxWidth: 520px
    paddingVertical: "{spacing.xxl}"
  material-badge:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.material-label}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "4px 8px"
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    separatorGlyph: "/"
  newsletter-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    padding: "{spacing.xxl} {spacing.section}"
    layout: "headline left, input+button row right"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.caption}"
    sectionHeadTypography: "{typography.title-sm}"
    columns: 4
    paddingVertical: "{spacing.xxl}"
  filter-pill:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "6px 14px"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.ink}"

## Components

### Buttons

**`button-primary`** — A flat rectangle in #191919 with zero border radius (`{rounded.none}`), uppercase Raleway at 12px/0.14em tracking, and 44px height. The stark geometry mirrors the brand's sculptural jewelry and refuses any softening. Active state deepens to #121212 (`{colors.ink-deep}`); disabled shifts fill to #dedede with `{colors.muted}` text. All CTAs — "Add to Cart", "Shop Now", "Subscribe" — use this component.

**`button-secondary`** — Identical dimensions and `{typography.button-md}` but hollow: transparent fill with a 1px `{colors.ink}` border. Used for secondary actions like "Add to Wishlist" or "View Collection". Hover inverts to a filled #191919 state matching `button-primary`.

**`button-ghost`** — Text-only in `{colors.muted}`, no border, uppercase tracking from `{typography.button-md}`. Reserved for tertiary links such as "See All" at section footers or dismissal actions.

### Inputs

**`text-input`** — Square corners (`{rounded.none}`), 1px `{colors.hairline}` border at rest, transitioning to 1px `{colors.ink}` on focus. No inner shadow or glow — focus communicates entirely through the border color shift. Field labels render above in `{typography.caption}` uppercase with `{colors.muted}` color.

### Navigation

**`nav-bar`** — 64px tall, `{colors.canvas}` (#fafafa) background, 1px `{colors.hairline}` bottom border. The AGMES wordmark sits left-aligned in a light Raleway rendering; primary nav links use `{typography.nav-link}` (11px uppercase, 0.12em tracking) and rest in `{colors.muted}`, stepping to `{colors.ink}` on hover with no underline. Cart icon and search icon occupy the right end at 20×20px.

### Product Card

**`product-card`** — Zero-radius container on `{colors.canvas}`. Image occupies a 3:4 portrait crop with a hairline 1px `{colors.hairline}` border surrounding the full card. Below the image: product name in `{typography.product-name}` (Raleway 300, 0.05em tracking) and price in `{typography.price}`. No drop shadow, no overlay badge. Hover state fades in a secondary material or angle image within the same crop frame.

### Hero

**`hero`** — Full-bleed editorial image at 80–100vh minimum. Headline in `{typography.display-xl}` (Raleway 300, 0.08em tracking) centers or anchors bottom-left, always positioned over the light tonal zone of the photograph. A single `button-primary` CTA sits beneath the headline with `{spacing.lg}` separation. No text-shadow or scrim — the photographer is trusted to provide the negative space.

### Collection Header

**`collection-header`** — Text-only zone: collection name in `{typography.display-md}`, a one-sentence description in `{typography.body-md}` capped at 520px max-width for readability. Large vertical padding (`{spacing.xxl}` top and bottom) creates gallery-scale breathing room. No background treatment — sits on the shared `{colors.canvas}` ground.

### Material Badge

**`material-badge`** — Inline label using the monospace stack (`{typography.material-label}`) with a 1px `{colors.hairline}` border and no background fill. Appears on the PDP below the product name to denote material (e.g. "Bronze", "14k Gold Fill", "Sterling Silver"). The monospace face reads as a specification tag against the editorial Raleway environment, borrowing the legibility of workshop notation.

### Price Display

**`price-display`** — Raleway 400 at 14px/0.02em tracking in `{colors.ink}`. Single price rendered plainly; no strikethrough sale state observed in extraction. Material or edition notation rendered adjacently in `{typography.material-label}` and `{colors.muted}`.

### Breadcrumb

**`breadcrumb`** — Small-caps Raleway (`{typography.caption}`) in `{colors.muted}`, separated by a "/" in `{colors.hairline}`. Sits above the product title on PDP pages. Current page segment renders in `{colors.ink}` to indicate position.

### Filter Pill

**`filter-pill`** — Used in collection pages for material, metal, and category filters. Transparent background with 1px `{colors.hairline}` border at rest; active state fills to `{colors.ink}` with `{colors.on-primary}` text — the same visual logic as `button-primary`. Typography is `{typography.caption}` uppercase.

### Newsletter Banner

**`newsletter-banner`** — Sits immediately above the footer on `{colors.surface-soft}` (#fafafa). Headline in `{typography.title-md}` on the left; email `text-input` and `button-primary` ("Subscribe") inline on the right. Wide horizontal padding (`{spacing.section}`) on desktop. Collapses to a stacked single-column layout on mobile.

### Footer

**`footer`** — Inverted section: `{colors.ink}` (#191919) background, `{colors.on-primary}` (#fafafa) text. Four columns on desktop: About, Shop, Customer Care, and Social/Contact. Section headings in `{typography.title-sm}`; links in `{typography.caption}` uppercase at slightly reduced opacity. Collapses to two columns at tablet and a single stacked column on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger icon (44×44px tap target); hero headline drops to `{typography.display-md}`; newsletter banner stacks vertically; footer single-column |
| Tablet | 744–1128px | Two-column product grid; full nav bar visible; hero at 60vh; footer two-column |
| Desktop | 1128–1440px | Three-column product grid; full nav with hover states; collection header at full width with 520px description cap |
| Wide | > 1440px | Grid and content max-width capped ~1400px; outer margins expand symmetrically to preserve whitespace balance |

### Touch Targets

- All buttons maintain minimum 44px height on mobile
- Nav hamburger icon is minimum 44×44px tap target
- Product cards span full column width with no floating overlay elements obscuring the tap zone
- Filter pills and material badges are minimum 36px height when used as interactive toggles
- Cart and search icons in the nav bar padded to 44×44px active area

### Collapsing Strategy

- Primary navigation collapses to hamburger at < 744px; drawer slides in from left on `{colors.canvas}` background with the same `{typography.nav-link}` links at larger 14px size
- Three-column product grid collapses to two columns at tablet and one column at mobile
- Footer four-column layout collapses to two columns at tablet, single stacked column at mobile
- Collection header description max-width constraint (520px) is removed on mobile for full-width text reflow
- Newsletter banner row layout (headline + input side-by-side) stacks vertically at < 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No chromatic accent color detected anywhere in extraction; palette is fully achromatic (#121212–#fafafa) — if a warm metallic accent (gold, bronze, patina) is applied via CSS custom properties loaded through JS or theme settings, it was not captured in static extraction
- No meta theme-color set; mobile browser chrome color on iOS/Android is unconfirmed
- Exact Raleway weights in use not confirmed beyond the light/regular range; brand may restrict to weight 300 and 400 only for display, with 500/600 reserved for UI elements
- Precise letter-spacing values for display typography were inferred from the sculptural-jewelry-with-Raleway visual idiom; inspector measurement required to confirm exact em values
- Hover transition timing (image swap on product cards, border color on inputs) not captured
- Cart drawer, mini-cart, and quick-add modal component styling not observed in extraction
- No sale or promotional pricing badge color confirmed; presence of markdown UI is unknown
- Animation easing curves (drawer open, image crossfade) not available from static extraction
