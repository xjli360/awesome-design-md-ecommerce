---
version: alpha
name: "The Frankie Shop"
source_url: "https://thefrankieshop.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  ZukaBeta — the brand's own condensed display typeface, named and proprietary — does the work that color refuses to do: The Frankie Shop's entire extracted palette is four shades of near-black and gray (#1a1a1a, #121212, #a0a0a0, #dedede) against a white (#ffffff) canvas, with no accent hue anywhere on the site. This is not minimalism as a trend position; it is a sustained editorial commitment that mirrors the brand's garment logic — architectural tailoring, clean structured shoulders, pieces designed to hold shape on the body the way a good typeface holds shape on a page. The result is a storefront that reads more like a fashion magazine grid than a Shopify template: generous whitespace absorbs product photography, ZukaBeta carries all headline weight, and the gray hairline (#dedede) is the only decorative element permitted. Buttons resolve to solid #1a1a1a fills with white reversal, or thin outlines that borrow the same ink — there is no softness in the CTA design, no pill radius, no gradient. Inputs and form fields use an underline-only discipline, sitting close to invisible until focus activates a 1px #121212 stroke. Navigation is sparse: a wordmark lockup in ZukaBeta flanked by functional text links at caption weight, the entire header anchored to a thin #dedede bottom border. Product cards strip everything except the image, a plain product name, and a price — no star ratings, no urgency badges, no quick-add overlays competing with the photography. The monospace fallback in the font stack signals an engineering-adjacent precision: this is a brand that chose a typeface with the same intention a developer might pick a terminal font. The absence of color in the design system is itself the brand color.

colors:
  primary: "#1a1a1a"
  primary-active: "#000000"
  primary-disabled: "#a0a0a0"
  ink: "#121212"
  body: "#1a1a1a"
  muted: "#a0a0a0"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-mid: "#f0f0f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  placeholder: "#a0a0a0"

typography:
  display-xl:
    fontFamily: "'ZukaBeta', monospace"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'ZukaBeta', monospace"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.96px
  display-md:
    fontFamily: "'ZukaBeta', monospace"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.48px
  display-sm:
    fontFamily: "'ZukaBeta', monospace"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: -0.22px
  wordmark:
    fontFamily: "'ZukaBeta', monospace"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.02em
  title-md:
    fontFamily: "inherit, system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "inherit, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  body-md:
    fontFamily: "inherit, system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "inherit, system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "inherit, system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  caption-upper:
    fontFamily: "inherit, system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  button-md:
    fontFamily: "inherit, system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "inherit, system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "inherit, system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.02em
  price:
    fontFamily: "inherit, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.0
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
    padding: 14px 24px
    height: 44px
    border: none
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
    padding: 13px 23px
    height: 44px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 0px"
    border: none
    borderBottom: "1px solid {colors.hairline}"
    focusBorderBottom: "1px solid {colors.ink}"
    placeholderColor: "{colors.placeholder}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.wordmark}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    productNameTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    gap: "{spacing.sm}"
    hoverEffect: "secondary image crossfade"
    border: none
    shadow: none
  hero-editorial:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    padding: "{spacing.section}"
    textAlign: left
    imagePosition: "full-bleed behind text scrim"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-upper}"
    height: 36px
    textAlign: center
  category-label:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
    border: none
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
    selectedBackgroundColor: "{colors.ink}"
    selectedTextColor: "{colors.on-primary}"
    unavailableTextColor: "{colors.muted}"
    unavailableDecoration: line-through
    height: 40px
    minWidth: 40px
  product-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    headlineTypography: "{typography.display-sm}"
    lineItemTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.display-sm}"
    rounded: "{rounded.none}"
    borderBottom: "1px solid {colors.hairline}"
    overlayType: full-screen
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    linkTypography: "{typography.caption}"
    padding: "{spacing.section}"
    borderTop: none
    columnLayout: 4-col-desktop

## Components

### Buttons

**`button-primary`** — A flat #1a1a1a rectangle with zero border radius and uppercase 13px tracking-wide text. There is no gradient, no shadow, no pill shape. On hover, the fill steps to pure #000000; disabled states use #a0a0a0 fill with white text. The CTA is a binary contrast event — black or nothing.

**`button-secondary`** — White fill with a 1px #1a1a1a border that inverts to solid black on hover, reversing the text to white. The transition is a full fill-flood rather than a tint shift, matching the brand's all-or-nothing approach to color. No intermediate hover state.

**`button-ghost`** — Transparent background, black underlined text at 11px uppercase. Used for secondary actions like "Continue Shopping" in the cart or inline editorial links. No border, no radius.

### Nav Bar

A 56px header holds the ZukaBeta wordmark with sparse text navigation links flanking it in 13px regular system font. A single 1px #dedede bottom border is the only structural separator between header and page content. An announcement bar sits above the header — 36px full-width #1a1a1a with centered uppercase caption text in white. On scroll, the header may condense or gain a subtle background opacity; the hairline border remains the only visual anchor.

### Product Card

Cards are image-forward with a 3:4 portrait ratio filling the full card width. On hover, a secondary product photograph crossfades in — no overlay, no quick-add button competing for attention. Below the image: product name in 13px regular system font and price in 14px regular, both left-aligned with no additional decoration. No star ratings, no review counts, no badges unless explicitly flagged as NEW or SALE via `product-badge`. No card border, no shadow, no corner radius.

### Text Input

Inputs use an underline-only treatment: no enclosing box, just a 1px #dedede bottom stroke that transitions to 1px #121212 on focus. Vertical padding is 12px with no horizontal inset, so the form reads as continuous text until activated. Placeholder text sits in #a0a0a0. Error state would darken the underline without adding a red box.

### Size Selector

Size options render as minimum 40×40px square tiles with 1px #dedede borders. The selected tile floods to #1a1a1a with white text — same binary logic as the primary button. Unavailable sizes display in #a0a0a0 with strikethrough, using typography alone as the signal rather than a diagonal rule or separate UI treatment.

### Hero Editorial

Full-bleed photography with ZukaBeta display text at 72px overlaid left-aligned. A scrim sits behind text when contrast demands it. The juxtaposition of the large geometric condensed typeface against model photography is the visual signature of the brand — no graphic overlays, no illustrated elements interrupt the image plane. Campaign text runs at tight -1.5px letter-spacing to compress the headline into a dense editorial block.

### Product Badge

A flat #1a1a1a tag with white uppercase caption text (11px, 0.1em tracking) and no corner radius. Appears at the top-left of product card images. Used sparingly — only for editorially meaningful status (NEW, LAST FEW), never urgency theater like countdown timers.

### Cart Drawer

A 400px right-edge panel with white fill and a 1px #dedede left border as the only separator from page content. The drawer headline renders in ZukaBeta display-sm (22px). Line items are stripped to image thumbnail, product name in body-sm, price, and a quantity field that uses the same underline input discipline. The checkout CTA is a full-width button-primary spanning the drawer's inner padding.

### Search Overlay

A full-screen white overlay with a single large input styled at display-sm scale (22px ZukaBeta). No box border around the input — just the underline treatment. Results populate as a product-card grid below the search field. Close action is a plain text link or minimal icon, no rounded close button.

### Footer

Full-width #1a1a1a footer with white caption-weight links organized in four columns on desktop. No heavy visual dividers between columns — column layout alone provides structure. Social handles appear as text or minimal SVG icons without circular containers. Legal text runs at caption scale, muted against the dark background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger icon replaces text nav links; hero text scales to display-md (32px); cart drawer becomes full-screen slide-up sheet; footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid; nav may collapse secondary links into hamburger; hero text at display-lg (48px); cart drawer remains side panel |
| Desktop | 1128–1440px | Three-to-four column product grid; full horizontal text nav; hero at display-xl (72px); cart drawer at fixed 400px width |
| Wide | > 1440px | Content centered within max-width container; product grid may extend to five columns; hero text holds at display-xl with increased horizontal padding |

### Touch Targets

- Size selector tiles: minimum 44×44px tap area on mobile even if visually 40×40px
- Nav icons (hamburger, bag, account): padded to 44px touch area
- Product card image: full-card tap target navigates to PDP
- Announcement bar links: 36px height meets minimum touch target

### Collapsing Strategy

- Desktop text nav links collapse into hamburger icon below 744px
- Announcement bar truncates to marquee scroll if content overflows on mobile
- Product grid reduces 4-col → 2-col → 1-col across breakpoints
- Footer column layout stacks vertically on mobile, maintaining link hierarchy
- Hero editorial text moves below image on narrow mobile rather than overlaying where legibility would suffer

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No accent or highlight color extracted — site appears fully monochrome; if a campaign color exists it is applied only through imagery and is not a persistent UI token
- ZukaBeta font metrics (x-height, variable axes, weight range, available weights) are not publicly documented; the monospace fallback may alter vertical rhythm materially
- Body font stack uses `inherit` — the rendered system font depends on OS and browser; no web font for body text confirmed from extraction
- Exact grid column counts and gutter widths not confirmed from live site; all product-grid values are design-inferred
- Animation durations and easing curves for drawer open/close, image crossfade, and hover transitions not extracted
- Mobile navigation drawer background color and secondary navigation depth not confirmed
- Specific border-radius values not confirmed from site; all `{rounded.none}` assignments are inferred from brand aesthetic and monochrome discipline
- Sale or markdown price color treatment not extracted — assumed to remain in ink/muted without a red accent given the monochrome constraint
