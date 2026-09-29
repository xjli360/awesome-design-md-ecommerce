---
version: alpha
name: "Cora"
source_url: "https://cora.life"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The Cora site runs on four extracted tones — near-black (#121212), slate-gray (#6e7577), pale silver (#dedede), and near-white (#eeeeee) — and makes that austerity feel deliberate rather than absent. Where most femcare brands reach for blush, botanical green, or powdery pastels to signal body-safety, Cora's visible palette is as controlled as a Swiss editorial grid: no decorative accent, no category-specific color coding between period care and bladder care, just modulated darkness calibrated against a white canvas. Type runs on Arial in the extracted stack — the site's actual web font did not surface past the JavaScript layer — set at modest weights that favor hierarchy through size and generous spacing rather than aggressive typographic contrast. Navigation sits horizontally across the top in clean, unhurried text; Font Awesome glyphs handle cart and search iconography rather than bespoke illustration. Product cards run photography-forward: the image supplies the warmth and bodily language that the UI palette deliberately withholds. Lightly rounded surfaces at {rounded.md} soften what could otherwise read as clinical severity — the rounded corner is Cora's one formal concession to approachability in a brand otherwise committed to restraint. The Shopify architecture is conventional, but the editorial pacing above the fold — body copy set like a magazine caption, subcategories named as clean categorical nouns — positions Cora as a wellness company rather than a drugstore shelf staple. Slate gray (#6e7577) functions as the sole tonal bridge, carrying secondary labels, meta-copy, inactive states, and supporting UI, producing a clean three-step value ladder (ink → muted → canvas) that disciplines hierarchy without any loud color. Section padding is generous, product grids unhurried, giving each category room to assert itself without ornamental typography filling the silence.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#dedede"
  ink: "#121212"
  body: "#2a2a2a"
  muted: "#6e7577"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  surface-mid: "#f5f5f5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-caps:
    fontFamily: "Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
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
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderFocusColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
  product-card-title:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-meta:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
    layout: split-image-right
  category-nav-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
  promo-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  subscription-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  trust-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.md} 0"
    layout: flex-row-centered-gap-lg
  product-detail-hero:
    backgroundColor: "{colors.canvas}"
    imageBackgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    priceTypography: "{typography.price}"
    imageRounded: "{rounded.none}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    height: 40px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — A full-black (#121212) rectangle with no border radius (`{rounded.none}`), signaling editorial conviction over commercial softness. Text renders in `{typography.button-md}` (Arial 14px, 700 weight, 0.5px tracking) at 48px height with 28px horizontal padding. Hover state collapses to `{colors.primary-active}` (#000000); disabled state desaturates to `{colors.primary-disabled}` fill with `{colors.muted}` label, signaling inactivity without a color system bleed.

**`button-secondary`** — Identical dimensions to primary but white fill with a 1px solid `{colors.ink}` border. Pairs cleanly with the primary CTA on product pages where "add to cart" and "learn more" share the same row. Active state shifts border to `{colors.muted}` and text to `{colors.muted}`.

**`button-ghost`** — Transparent background, no border, underlined `{colors.ink}` text in `{typography.button-md}`. Used for tertiary actions — ingredient disclosures, expanded product detail links, editorial navigation — where adding a container would over-weight the hierarchy.

### Navigation

**`nav-bar`** — 64px tall white bar with a 1px `{colors.hairline}` bottom rule that separates it from page content without shadow drama. Logo anchors the left; category links run center in `{typography.nav-link}` (Arial 14px regular); Font Awesome cart, search, and account glyphs sit right. On scroll the bar maintains its white fill, the hairline doing the separation work. Mobile collapses to logo-left, cart-and-hamburger-right, with a full-width slide-in drawer for nav links.

**`category-nav-pill`** — Horizontally scrollable filter row that appears below the hero on category pages. Inactive pills use `{colors.canvas}` fill, `{colors.hairline}` border, and `{colors.muted}` `{typography.label-caps}` text. The active state flips cleanly to `{colors.ink}` fill with `{colors.on-primary}` text and `{rounded.full}` shape — a binary toggle that requires no accent color to communicate selection.

### Inputs

**`text-input`** — A zero-radius 48px-tall outlined field with `{colors.hairline}` default border sharpening to `{colors.ink}` on focus. Placeholder copy in `{colors.muted}`; live input in `{colors.ink}`. No background tint, no inset shadow — the border-only feedback model keeps forms visually consistent with the rest of the stripped-back UI. Used across email capture, subscribe-and-save flows, and search.

### Product Cards

**`product-card`** — Portrait-ratio (3:4) image tile with `{rounded.none}`, no drop shadow, and no card border — photography bleeds to the edge. Product name in `{typography.body-md}` `{colors.ink}` below the image, price in `{typography.price}` on the next line, and meta-text (subscribe availability, unit count) in `{typography.caption}` `{colors.muted}`. Grids run 2 columns on mobile, 3–4 on desktop. Hover lifts the card with a faint 4px shadow rather than a color-state change.

**`subscription-badge`** — A small `{colors.surface-soft}` pill with `{rounded.xs}` positioned directly beneath the product title. Carries a subscribe-and-save callout in `{typography.label-caps}` `{colors.muted}`. Keeps subscription messaging visible at the browse layer without disrupting the card's photographic silence.

### Hero

**`hero`** — Split 50/50 layout at desktop: editorial headline in `{typography.display-xl}` and a `button-primary` CTA occupy the left column on a `{colors.surface-soft}` background; full-bleed lifestyle or product photography fills the right column with no border radius. The `{colors.surface-soft}` (#eeeeee) ground distinguishes the hero zone from the white nav above without requiring a color change. On mobile the image stacks above, cropped to 16:9, with headline and CTA stacked below on white.

### Utility Strips

**`promo-banner`** — Full-width `{colors.ink}` bar pinned above the nav. Single line of `{typography.body-sm}` in `{colors.on-dark}`, centered. This is the brand's only loud UI surface — the one place the near-black ground is used decoratively rather than functionally. No dismiss button in standard configuration.

**`trust-strip`** — A full-width row of 3–4 short certification or value signals (organic, dermatologist-tested, flexible subscription) in `{typography.caption}` `{colors.muted}`, separated by thin `{colors.hairline}` vertical rules. Sits between the hero and the first product grid, framing the browse experience with brand credibility before products appear.

### Product Detail

**`product-detail-hero`** — Two-column layout at desktop: image fills the left half on a `{colors.surface-soft}` tile with `{rounded.none}`; detail occupies the right. Title in `{typography.display-sm}`, price in `{typography.price}`, description in `{typography.body-md}`. A `quantity-stepper` and `button-primary` sit at the bottom of the right column. On mobile the image stacks above full-width; detail flows below in a single column.

**`quantity-stepper`** — An outlined 40px row: minus / count / plus in a three-cell layout, all sharing a single `{colors.hairline}` border rectangle with `{rounded.none}`. Count label in `{typography.title-sm}`. No background fill, no color on interaction — border shifts to `{colors.ink}` on focus.

### Footer

**`footer`** — Full-width `{colors.ink}` block with `{colors.on-dark}` text. Column headers in `{typography.label-caps}` provide categorical anchors (Shop, About, Help, Social); links in `{typography.body-sm}` `{colors.hairline}` sit beneath each. Standard four-column Shopify layout at desktop, two columns at tablet, accordion-collapsed at mobile. A bottom bar carries copyright in `{typography.caption}` and a payment icon strip from Font Awesome Brands.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column nav collapses to hamburger drawer; hero image stacks above text at 16:9 crop; product grid locks to 2 columns; category filter pills scroll horizontally; footer accordions into expandable sections; promo banner truncates to one short line |
| Tablet | 744–1128px | Nav links remain visible but may truncate long category names; hero maintains split layout at reduced horizontal padding; product grid uses 3 columns; footer collapses to 2 columns |
| Desktop | 1128–1440px | Full nav with all category links; hero at 50/50 split with full `{spacing.section}` padding; product grid at 3–4 columns; trust strip shows all signals inline; footer at full 4 columns |
| Wide | > 1440px | Content constrained to ~1400px max-width container and centered; hero image does not stretch beyond container bounds; 4-column product grid maintained; additional whitespace absorbed by centering margins |

### Touch Targets

- All interactive elements minimum 44×44px on mobile viewports
- Category filter pills minimum 36px height with generous horizontal padding for thumb reach
- Quantity stepper minus and plus buttons each padded to minimum 44px wide on mobile
- Nav icon glyphs (cart, search, hamburger) padded to 48px hit area even when the rendered glyph is smaller
- Product card entire surface area is tappable to navigate to PDP

### Collapsing Strategy

- Navigation: top-level links collapse into a full-height slide-in drawer at < 744px; sub-category panels stack vertically inside the drawer with `{colors.hairline}` dividers
- Product grids: 4-col → 3-col at 1128px → 2-col at 744px; 1-col is avoided even on small mobile to maintain the browseable grid feel
- Hero: side-by-side split collapses to image-top / text-bottom stack at < 744px; image crops to 16:9 rather than maintaining the desktop portrait proportion
- Trust strip: inline multi-signal row collapses to a single rotating or most-important signal at mobile
- Footer: 4-column layout → 2-column at tablet → single-column accordion at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No distinctive brand accent color captured.** All four extracted colors are neutrals (#dedede, #6e7577, #eeeeee, #121212). Cora may carry a warm blush, rose, or terracotta accent for campaigns, CTAs, or packaging-echo UI — this did not surface and likely loads via Shopify theme CSS custom properties or a JS-injected variable file.
- **Web font not captured.** Arial is the extracted fallback stack. Cora's branded typeface (possibly a licensed humanist or geometric sans) loads via a JavaScript-deferred `@font-face` that bypassed static extraction. All typography tokens above are structural placeholders pending a live DevTools inspection.
- **Meta theme-color absent.** No mobile browser chrome accent color was declared; mobile chrome defaults to system white or gray.
- **Promotional and sale-state colors unknown.** No sale price color, low-stock warning red, or success-state green appeared in the extracted palette; these are likely stored in Shopify theme editor settings rather than top-level CSS.
- **Subscription tier UI specifics unknown.** Cora's subscribe-and-save interface — discount badge styling, frequency-selector component, savings callout pattern — was not derivable from the static hints.
- **Icon set partially identified.** Font Awesome 5 and 6 (Brands + Free) confirmed; any proprietary or brand-specific icon family was not detected.
- **Color for rating or review UI unknown.** No star-rating color, review score badge, or verified-purchase indicator was captured in the palette extraction.
