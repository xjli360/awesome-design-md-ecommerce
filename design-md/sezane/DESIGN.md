---
version: alpha
name: "Sézane"
source_url: "https://sezane.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Two warm extracted tones — a burnished gold (#b2832c) and a dusty olive (#a2944e) — tell the story before any type loads: this is a house that chose warmth over starkness, patina over polish. Sézane, the Parisian label born entirely online in 2013 before expanding into physical "Appartements," carries an editorial sensibility where the white canvas ({colors.canvas}: #ffffff) functions not as absence but as the page on which these warm accents are inked. The gold primary reads differently depending on context — against ivory it becomes amber harvest, against a dark product image it becomes jewellery — and this chromatic flexibility is the point: the brand wants one palette to carry both a silk blouse and a leather bag without typological clash. Display type leans toward elegant serifs at generous sizes, reinforcing the sense of reading a magazine rather than clicking through a grid. Buttons and inputs favor sharp, square geometry ({rounded.none}), avoiding the pill shapes of lifestyle and wellness brands; the hard corner signals fashion-house discipline. Product cards present clean portrait photography with minimal overlay — hover states reveal only the wishlist icon and a second product image crossfade, never flooding the tile with color. The navigation collapses into a clean drawer on mobile, where the full-bleed hero photograph replaces the desktop editorial split. Sézane's digital language trusts the reader to do some work — spacing is generous, calls to action are calm rather than urgent, and the primary gold (#b2832c) never shouts. The olive secondary (#a2944e) earns its role in seasonal editorial banners and category-label accents, providing a muted counterpoint that ages the palette toward something grown rather than designed.

colors:
  primary: "#b2832c"
  primary-active: "#8f6620"
  primary-disabled: "#d9c49a"
  secondary: "#a2944e"
  secondary-active: "#7d7138"
  ink: "#1a1a1a"
  body: "#3a3530"
  muted: "#7a7269"
  hairline: "#e0dbd4"
  hairline-soft: "#eeebe6"
  canvas: "#ffffff"
  canvas-warm: "#faf8f5"
  surface-soft: "#f4f1ec"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#b94040"
  sold-out-text: "#9e9992"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 44px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 1.2px
    textTransform: uppercase
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.4px
  editorial-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1.8px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.3px

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
    padding: 14px 32px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-logo:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.body}"
    gap: "{spacing.sm}"
  product-card-hover:
    wishlistIconColor: "{colors.primary}"
    secondaryImageReveal: true
    transitionDuration: 300ms
  hero-editorial:
    backgroundColor: "{colors.canvas-warm}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    titleColor: "{colors.ink}"
    subtitleColor: "{colors.body}"
    ctaVariant: button-primary
    imagePosition: right
    imageFraction: "55%"
    padding: "{spacing.section}"
  collection-banner:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-md}"
    labelTypography: "{typography.editorial-label}"
    labelColor: "{colors.primary}"
    titleColor: "{colors.ink}"
    padding: "{spacing.xxl}"
  editorial-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.editorial-label}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  wishlist-icon:
    color: "{colors.hairline}"
    colorActive: "{colors.primary}"
    size: 20px
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: "10px 0"
    borderBottom: "2px solid transparent"
    borderBottomActive: "2px solid {colors.primary}"
    activeTextColor: "{colors.ink}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderActive: "1px solid {colors.ink}"
    width: 44px
    height: 44px
  size-selector-sold-out:
    textColor: "{colors.sold-out-text}"
    textDecoration: line-through
    border: "1px solid {colors.hairline-soft}"
    backgroundColor: "{colors.canvas}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.canvas-warm}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section}"
  seasonal-editorial-strip:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.editorial-label}"
    padding: "10px {spacing.base}"

## Components

### Buttons
**`button-primary`** — A flat, sharp-cornered bar (`{rounded.none}`) in burnished gold `{colors.primary}` (#b2832c) with spaced uppercase `{typography.button-md}` at 12px / 1.5px letter-spacing. The square geometry signals fashion-house discipline rather than consumer friendliness. Active state deepens to `{colors.primary-active}` (#8f6620); disabled bleaches to pale straw `{colors.primary-disabled}`. No shadow or elevation — entirely flat.

**`button-secondary`** — Identical square geometry, inverted: white fill with a 1px solid `{colors.ink}` border. Used for secondary CTAs such as "View the full look" or newsletter alternatives. Mirrors the primary's height (48px) and letter-spacing exactly, so paired button rows read as a visual set rather than a hierarchy mismatch.

**`button-ghost`** — Transparent with underline only, no visible box. Used for tertiary prose actions — size guide links, return policy references, accordion triggers within product detail. Shares `{typography.button-md}` to keep label size consistent across all three button variants.

### Text Input
**`text-input`** — Square-edged fields with a single 1px `{colors.hairline}` border that steps to `{colors.ink}` on focus, no shadow or glow. Placeholder in `{colors.muted}`; error and helper text render at `{typography.caption}` beneath the field with `{colors.error}` for error state. The field does not animate its label — a static label sits above the input at all times, matching the editorial flatness of the broader design.

### Navigation
**`nav-bar`** — 64px white bar with a barely-present `{colors.hairline-soft}` bottom rule. The Sézane wordmark uses `{typography.display-sm}` in a serif face at the horizontal center on mobile, shifted left on desktop. Right-side icon cluster covers search, account, and bag with minimal SVG glyphs and no text labels. Desktop hover on category links triggers a full-width mega-drop panel that opens with editorial photography occupying its rightmost column — not a plain link list. The mega-panel background mirrors `{colors.canvas-warm}` to separate it visually from the page scroll.

### Product Card
**`product-card`** — Portrait 3:4 image at zero radius (`{rounded.none}`) so adjacent grid tiles share implied edges. Title renders at `{typography.body-sm}` one line below the image, price at `{typography.price}` on the following line in `{colors.body}`. On hover, a second product image crossfades in (300ms ease) and the wishlist heart at top-right activates in `{colors.primary}` gold (#b2832c). No add-to-cart overlay — the CTA lives exclusively in the product detail page, keeping the grid purely for discovery. Out-of-stock indicators are handled at the size-selector level, not on the card tile.

### Hero
**`hero-editorial`** — Full-bleed or split-panel layout on `{colors.canvas-warm}`. Serif display headline at `{typography.display-xl}` (44px / weight 400 — the brand trusts the serif's intrinsic authority over bold weight), followed by body at `{typography.body-md}`, then `button-primary`. On desktop the image occupies the right 55% with the copy block anchored left; on mobile the image becomes full-bleed at top with the text block below. No text overlay on image — the copy and image always occupy separate zones.

### Collection Banner
**`collection-banner`** — A warm surface block (`{colors.surface-soft}`) inserted between grid rows to introduce seasonal categories or new arrivals. A short `{typography.editorial-label}` line in `{colors.primary}` gold appears above a larger `{typography.display-md}` serif title. The combination of micro-uppercase label and loose serif headline is the brand's primary editorial voice, appearing across landing pages, look-book sections, and email headers.

### Editorial Badge
**`editorial-badge`** — Flat gold chip (`{colors.primary}`, `{rounded.none}`) with 10px `{typography.editorial-label}` text in white, no shadow. Positioned at the top-left corner of a product image with an 8px inset. Used for "New", "Best Seller", seasonal collection names, or limited-edition markers. The badge never stacks — only one per image tile.

### Category Tab
**`category-tab`** — Flat unrounded tab for sub-navigation within category pages (All / Tops / Trousers / Dresses / etc.). Active state is marked solely by a 2px `{colors.primary}` gold bottom border and text lifting from `{colors.muted}` to `{colors.ink}` — no background fill change. The minimal indicator keeps visual weight on the imagery grid below rather than the navigation chrome above.

### Size Selector
**`size-selector`** — A 44×44px square tile with 1px `{colors.hairline}` border and centered `{typography.body-sm}` label. Selected state uses full `{colors.ink}` border (1px → still 1px, just color change). Sold-out tiles (`size-selector-sold-out`) retain position in the grid with line-through text in `{colors.sold-out-text}` and a lightened `{colors.hairline-soft}` border, preventing layout reflow when availability changes.

### Seasonal Editorial Strip
**`seasonal-editorial-strip`** — A full-width announcement banner in `{colors.secondary}` olive (#a2944e) with white `{typography.editorial-label}` text. Used for shipping promotions, limited-window sale notices, and seasonal campaign launches. Sits above the nav-bar on first load and can be dismissed. The olive strip is the only place the secondary color takes a primary-action role; elsewhere it functions as a supporting accent.

### Footer
**`footer`** — Warm canvas background `{colors.canvas-warm}` with a single `{colors.hairline}` top rule. Three or four link columns at `{typography.body-sm}` with `{colors.ink}` link color on hover; a newsletter input and `button-primary` occupy the rightmost column on desktop. Social icons appear as minimal SVG glyphs without labels. The footer carries the same low-temperature feeling as the rest of the site — no bold calls to action, no countdown timers.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger drawer nav; full-bleed hero image stacked above text; category tabs become horizontal scroll strip; footer collapses to single column; editorial strip shows truncated copy |
| Tablet | 744–1128px | Two-column product grid; condensed nav retains key links; split hero panel activates at reduced image fraction; footer in two columns |
| Desktop | 1128–1440px | Three to four-column product grid; full horizontal mega-nav; editorial sidebar content and look-book inserts become visible; hero at full 55/45 split |
| Wide | > 1440px | Content capped at 1440px max-width and centered on page; padding increases symmetrically; hero imagery scales but text block width is capped at ~520px to prevent over-extended line lengths |

### Touch Targets
- All interactive elements maintain a minimum 44×44px touch target regardless of visual size
- Size selector tiles are 44×44px both visually and as touch targets
- Wishlist icon has a 44px hit zone despite the 20px visual glyph
- Category tabs use `{spacing.base}` vertical padding to reach comfortable thumb height
- Footer links use `{spacing.md}` vertical gap for comfortable scrolling

### Collapsing Strategy
- Desktop mega-nav collapses to a full-height hamburger drawer on mobile, with animated slide-in from left and a `{colors.canvas}` overlay
- Category tab row converts from a horizontal rule-underlined set to a side-scrolling strip on mobile; no dropdown replacement
- Hero split-panel becomes stacked image-top / text-bottom on mobile; image aspect ratio shifts from landscape to 3:4 portrait
- Product grid never drops to one column — minimum two columns on mobile to support comparative browsing
- Editorial look-book blocks (full-bleed images between grid rows) collapse to portrait aspect ratio on mobile
- Mega-nav panel editorial photography column is hidden on tablet; only the link columns remain

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Fonts**: Zero font families were extracted — the site very likely loads custom typefaces via JavaScript or a CDN with anti-bot protections active during crawl. Fallback stacks used (Georgia serif for display; system sans-serif for UI). Actual Sézane brand typefaces are unknown; real implementation must replace these stacks with extracted values.
- **Full color palette**: Only two distinctive colors extracted (#b2832c, #a2944e). Surface tones, hairline colors, muted text, and warm canvas variants are inferred from brand aesthetic and the #ffffff meta theme-color — none were measured directly.
- **Spacing and radius values**: No spacing or border-radius tokens extracted; values follow a 4px-base system and a flat-corner fashion-house aesthetic, both inferred rather than measured.
- **Component interaction states**: Hover, focus, and error color values for form fields and interactive elements are derived rather than pixel-measured from live states.
- **Icon set style**: The nav and utility icon library (search, bag, account, wishlist heart) is undocumented; SVG stroke weight and style assumed minimal based on brand aesthetic.
- **Japanese locale typography**: The page title indicates an active Japanese storefront — CJK line-height adjustments, fallback CJK font stacks, and locale-specific font-size tuning are not captured here.
- **Animation curves**: Transition easing functions for hover states, mega-nav open/close, and editorial image crossfades are undocumented; `ease` assumed throughout.
