---
version: alpha
name: "Anine Bing"
source_url: "https://aninebing.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every primary action on aninebing.com fires from a solid #121212 rectangle — no rounded corners, no gradient, no softening. The brand applies exactly one warm signal to an otherwise fully monochromatic interface: #ff0000, a saturated primary red reserved for sale pricing and urgency badges, never warmed to coral or cherry. All other surfaces sit in a compressed grayscale band running from the near-black #121212 ink through mid-range neutrals (#4a4a4a, #656565, #808080) to a cool off-white #f6f6f6 that replaces pure white on product-listing backgrounds. Two typefaces carry the entire system — DidotLT, a high-contrast didone serif with dramatic thin-to-thick stroke variation, handles display headlines and editorial title moments, its proportions echoing the mastheads of print fashion titles rather than digital-native display fonts. Gibson, a geometric humanist sans-serif, runs everything operational: navigation labels, body copy, product names, size charts, and button text. The pairing maps directly onto the brand's dual identity — European fashion-house rigor through DidotLT, California directness through Gibson.

  Buttons are strictly rectilinear ({rounded.none}) and run full-width on mobile, a move that signals confidence rather than constraint. The primary CTA fills black with white Gibson uppercase text; the secondary inverts to a white fill with a 1px black border. Neither button rounds its corners even at hover. Product cards are equally restrained: a 4:5 portrait image, the product name in Gibson body-sm, the price in the same weight, and a quick-add layer that appears on hover without panel animation — just an immediate black bar sliding up from the bottom edge of the image. The announcement bar anchors the top of every viewport in solid #121212 with white caption text cycling through shipping thresholds.

  Navigation on desktop spans the full viewport width at 64px tall with the ANINE BING wordmark in DidotLT display-sm and a horizontal row of Gibson nav-link uppercase labels beneath. The hairline border (#dedede) at the nav base is the system's thinnest visual divider. On mobile, links collapse behind an icon toggle while the wordmark and cart icon share a two-column header. Section spacing is generous — 64px between editorial blocks — keeping imagery dominant and text subordinate. Size selectors carry a hairline border that upgrades to a solid ink border on selection, the sole interactive affordance that shifts state through border weight rather than fill color.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#979797"
  accent-sale: "#ff0000"
  ink: "#121212"
  body: "#4a4a4a"
  muted: "#656565"
  muted-mid: "#808080"
  muted-soft: "#979797"
  muted-lighter: "#828282"
  hairline: "#dedede"
  hairline-soft: "#e4e4e4"
  hairline-lighter: "#d8d8d8"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#000001"

typography:
  display-xl:
    fontFamily: "'DidotLT', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'DidotLT', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'DidotLT', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Gibson', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'Gibson', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  body-md:
    fontFamily: "'Gibson', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gibson', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Gibson', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Gibson', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gibson', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Gibson', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  label-uppercase:
    fontFamily: "'Gibson', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Gibson', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  announcement:
    fontFamily: "'Gibson', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.5px
  price:
    fontFamily: "'Gibson', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
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
    padding: "14px 24px"
    height: 48px
    width: "100%"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: "13px 23px"
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 48px
    padding: "0 16px"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.announcement}"
    height: 40px
    padding: "0 16px"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "4/5"
    nameTypography: "{typography.body-sm}"
    nameColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.accent-sale}"
    originalPriceColor: "{colors.muted}"
    gap: "{spacing.sm}"
    rounded: "{rounded.none}"
  hero-full:
    imageOverlay: "rgba(0,0,0,0.12)"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.on-dark}"
    sublineTypography: "{typography.body-md}"
    sublineColor: "{colors.on-dark}"
    ctaVariant: button-primary
  badge-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 6px"
    position: absolute
    placement: top-left
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 6px"
    position: absolute
    placement: top-left
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    textColorOutOfStock: "{colors.muted}"
    height: 40px
    minWidth: 40px
  quick-add-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    height: 40px
    position: absolute
    placement: bottom
  search-drawer:
    backgroundColor: "{colors.canvas}"
    overlayColor: "rgba(0,0,0,0.4)"
    inputBorderColor: "{colors.hairline}"
    inputTypography: "{typography.body-md}"
    resultNameTypography: "{typography.body-sm}"
    resultPriceTypography: "{typography.price}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headlineTypography: "{typography.title-sm}"
    headlineColor: "{colors.ink}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.body}"
    borderTop: "1px solid {colors.hairline}"
    padding: "48px 0"

## Components

### Buttons
**`button-primary`** — A solid #121212 rectangle at 48px tall, full-width on mobile and auto-width on desktop, with Gibson uppercase letter-spaced text in white. No radius at any state; on hover the fill deepens to `{colors.primary-active}` (#000000). Disabled state swaps fill to `{colors.primary-disabled}` (#979797) with the same white label and `cursor: not-allowed`.

**`button-secondary`** — White fill with a 1px solid black border and identical Gibson uppercase label in black. On hover the fill shifts to `{colors.surface-soft}` (#f6f6f6). Used for secondary CTAs on PDPs and in editorial modules where a black primary CTA already anchors the layout.

### Text Input
**`text-input`** — Flat, border-only field with no radius. Hairline `{colors.hairline}` border at rest upgrades to a solid `{colors.ink}` 1px border on focus — the only state shift. 48px height, 16px horizontal padding. Placeholder text renders in `{colors.muted}`. Applied to newsletter forms, email capture, and search.

### Navigation
**`nav-bar`** — 64px tall, white canvas, hairline bottom border. On desktop the ANINE BING wordmark displays in DidotLT display-sm above a horizontal row of Gibson nav-link uppercase labels. Cart and account icons live in the right cluster; a search icon triggers the search drawer overlay. On mobile the layout collapses to wordmark-center with a hamburger toggle left and cart icon right.

**`announcement-bar`** — Solid #121212 band above the nav, 40px tall, cycling promotional text in white Gibson announcement weight. No close affordance; persists across all pages including PDP and checkout entry.

### Product Card
**`product-card`** — 4:5 aspect portrait image with no radius on a white card background. Product name sits below the image in Gibson body-sm, followed by price on the next line in the same weight. Sale items render the original price in `{colors.muted}` with strikethrough and the marked-down price in `{colors.accent-sale}` (#ff0000). On hover, the `quick-add-bar` slides up from the bottom edge of the image — a solid black strip with uppercase Gibson button-sm text reading "QUICK ADD" — with no easing delay.

### Hero
**`hero-full`** — Full-viewport editorial image with a 12% black scrim layer. Headline in DidotLT display-xl white, positioned bottom-left or centered depending on layout variant. A single `button-primary` CTA sits beneath the headline. Scrim may be omitted on high-contrast images. Secondary editorial modules use a 50/50 image-text split with DidotLT display-md headline and Gibson body-md body copy.

### Badges
**`badge-sale`** — Flat #ff0000 label in uppercase Gibson badge weight, no radius, positioned absolute over the top-left corner of a product image tile. **`badge-new`** — Identical geometry using `{colors.ink}` fill. Both badges appear only on the grid card view, never on the PDP hero.

### Size Selector
**`size-selector`** — Square tiles at 40px minimum dimension. Hairline border at rest; border upgrades to 1px solid ink on selection without any fill change. Out-of-stock sizes render with a diagonal strikethrough line and `{colors.muted}` text — tappable to trigger a restock notification.

### Search Drawer
**`search-drawer`** — Full-width overlay anchored beneath the nav bar with a 40% black scrim behind. White background, single text input with hairline border and no radius. Results surface as a two-column image grid styled to match `product-card`, with names and prices in the same typography scale.

### Footer
**`footer`** — White canvas with a single hairline top border and 48px top padding. Column headings in Gibson title-sm uppercase in `{colors.ink}`; body links in body-sm `{colors.body}`. Social icon glyphs in ink. Newsletter capture uses the standard `text-input` field paired with a full-width `button-primary`, maintaining the system-wide vocabulary.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid minimum 2-up; full-width buttons; hamburger nav slide-in drawer; announcement bar truncates to one offer |
| Tablet | 744–1128px | 2-column product grid; nav condenses to logo + collapsed category links; hero copy constrains to 60% viewport width |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with wordmark and link row; quick-add on card hover enabled |
| Wide | > 1440px | Content width capped ~1440px with growing side gutters; hero image extends edge-to-edge behind content container |

### Touch Targets
- All buttons and interactive tiles minimum 44px height on mobile
- Size-selector tiles expand to 48px on touch viewports
- Nav icon cluster (hamburger, cart, account) spaced at minimum 44px per target
- Announcement bar links wrapped in full-height tap targets
- Quick-add replaces hover trigger with a persistent sticky bottom CTA on mobile PDP

### Collapsing Strategy
- Desktop horizontal nav → mobile hamburger slide-in drawer at < 744px
- 4-column product grid → 3-column at tablet → 2-column on mobile; 1-column is not used
- 50/50 editorial image-text split → stacked single-column below 744px, image above text
- Desktop hover quick-add bar → sticky bottom CTA button on mobile PDP
- Multi-column footer → 2-column at tablet → single-column accordion at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Canvas white (#ffffff) and pure black (#000000) not present in extracted palette; inferred from Shopify defaults and confirmed by meta theme-color (#000000)
- DidotLT weight variants (italic, bold) not confirmed from extraction — only regular weight evident in font-family stack
- Gibson weight range not confirmed beyond what extraction suggests; semibold (600) is assumed from common Gibson licensing tiers
- Exact letter-spacing values for nav and button text are estimated from visual archetype rather than extracted CSS custom properties
- No motion or transition timing data extracted; duration and easing are inferred from brand positioning
- Filter and sort panel component styling not captured
- Color swatch picker interaction not extracted
- Cart drawer behavior (slide-in panel vs. full-page redirect) not confirmed
- Sticky nav behavior on scroll (hide/show, shrink, border change) not captured
