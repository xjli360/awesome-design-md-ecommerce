---
version: alpha
name: "Aimé Leon Dore"
source_url: "https://aimeleondore.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Where other streetwear labels foreground the logo, Aimé Leon Dore foregrounds the photograph — the garment in natural light, on a real body, against a near-neutral background — with Sohne holding caption and navigation text at near-whisper weights along the periphery. The site operates at a deliberate quietness: canvas white (#ffffff) carries the editorial spreads, near-black (#181818) anchors CTAs and primary text, and the grays (#c4c4c4, #dedede) handle dividers and disabled states without ever demanding attention. A powder blue (#5bbad5) and its lighter complement (#aadddd) appear as accent tokens — colors pulled from vintage New Balance colorways the brand helped redefine — surfacing in seasonal product highlights and favicon identity rather than structural UI. The orange-red (#e42c00) functions as a signal color: sale markup, alert badge, the occasional editorial callout that punctures the otherwise achromatic surface.

  Typography runs Sohne — a geometric sans-serif in the tradition of Akzidenz Grotesk, but warmer — at weights between 300 and 500, never the heavy 700 that hype-era streetwear reaches for. Display text sits at 48px weight 300, as if the brand is deliberately underperforming expectations. Buttons carry their labels in tracked uppercase at 11–12px, maintaining the restraint at the moment of conversion. Navigation collapses to a slim single row of text links without icons or visual embellishment.

  The geometry is flatly architectural: `{rounded.none}` on buttons, cards, and inputs without exception. No softened corners break the grid logic. The spatial system holds tight — product grids pack at 16px gutters, section transitions breathe at 64px — giving the site its magazine-page-to-page rhythm. Every color held back, every border radius removed, every font weight held one notch lower than expected leaves room for the clothes to do the speaking.

colors:
  primary: "#181818"
  primary-active: "#000000"
  primary-disabled: "#c4c4c4"
  ink: "#121212"
  body: "#181818"
  muted: "#c4c4c4"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#5bbad5"
  accent-teal: "#aadddd"
  accent-red: "#e42c00"
  accent-orange: "#da532c"
  scrim: "#181818"

typography:
  display-xl:
    fontFamily: "'Sohne', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Sohne', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Sohne', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Sohne', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Sohne', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Sohne', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Sohne', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Sohne', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Sohne', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Sohne', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Sohne', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  label-caps:
    fontFamily: "'Sohne', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  price-display:
    fontFamily: "'Sohne', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

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
    padding: 14px 20px
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
    padding: 13px 19px
    height: 44px
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
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: none
    borderBottom: "1px solid {colors.hairline}"
    borderFocusBottom: "1px solid {colors.ink}"
    padding: "12px 0"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    logoWidth: 120px
  product-card:
    backgroundColor: "{colors.canvas}"
    imageRatio: "3/4"
    rounded: "{rounded.none}"
    typographyName: "{typography.body-sm}"
    typographyPrice: "{typography.price-display}"
    textColor: "{colors.ink}"
    gap: "{spacing.sm}"
    hoverOpacity: 0.85
  editorial-hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typographyHeadline: "{typography.display-xl}"
    typographySubhead: "{typography.body-md}"
    layout: full-bleed image, text block below in grid column
    overlayScrim: none
    minHeight: 80vh
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    mutedColor: "{colors.muted}"
    borderBottom: "1px solid {colors.hairline}"
    height: 44px
    position: sticky
    top: 56px
  size-selector:
    backgroundColor: "{colors.canvas}"
    selectedBackground: "{colors.ink}"
    selectedTextColor: "{colors.on-primary}"
    unavailableTextColor: "{colors.muted}"
    unavailableDecoration: line-through
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 40px
    minWidth: 44px
    gap: "{spacing.xs}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    typographyItem: "{typography.body-sm}"
    typographyTotal: "{typography.title-sm}"
    padding: "{spacing.xl}"
    slideTransition: 200ms ease-in
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  lookbook-caption:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    paddingTop: "{spacing.sm}"
    maxWidth: 320px
  newsletter-signup:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typographyLabel: "{typography.label-caps}"
    typographyBody: "{typography.body-sm}"
    inputBorderBottom: "1px solid {colors.hairline}"
    inputFocusBorderBottom: "1px solid {colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted}"
    typography: "{typography.caption}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
    columnGap: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — A flat black (#181818) rectangle with `{rounded.none}`, carrying its label in tracked uppercase Sohne at 12px weight 500. Height holds at 44px; horizontal padding at 20px. On press, background deepens to pure black (#000000). Disabled state drains to #c4c4c4 with white text. No hover animation — the brand avoids decorative micro-interactions at the conversion moment.

**`button-secondary`** — White fill with a 1px solid #121212 border; identical geometry and typography to primary, 1px of padding exchanged for the inset border. Used for "Add to Wishlist", filter reset, and any action secondary to the primary purchase flow. Never rounded.

**`button-ghost`** — Transparent background with underline on the label text in `{typography.button-md}`. Used for tertiary actions — "Size Guide", "View All", policy links — that appear inline with editorial content rather than in a button slot.

### Product Card

**`product-card`** — Portrait image at a fixed 3:4 ratio with no card chrome: no shadow, no border, no radius. Product name and price appear below in Sohne body-sm and price-display scale respectively, left-aligned, with an 8px gap from the image edge. On hover the image drops to 85% opacity to signal interactivity without motion. New and collaboration items may carry a `sale-badge` in signal red (#e42c00) as an absolute overlay at the top-left corner of the image.

### Navigation

**`nav-bar`** — 56px tall, white canvas, 1px hairline bottom border. Brand mark sits left or center; a left cluster of category text links in `{typography.nav-link}` (13px, weight 400, natural tracking) extends to the right; utility icons (search, account, cart) as minimal line icons anchor the far right. No background color change on scroll, no drop shadow — the nav holds flat white as editorial content moves beneath it.

### Editorial Hero

**`editorial-hero`** — Full-bleed photography at minimum 80vh. No text overlay, no gradient scrim: the headline (Sohne `{typography.display-xl}`, weight 300) and optional subhead in `{typography.body-md}` sit below the image in a grid-aligned text block rather than over the photograph. The composition reads as a magazine spread: image occupies its space entirely, text begins on the next visual tier.

### Collection Header

**`collection-header`** — Full-width white section with collection title in `{typography.display-md}` (Sohne 32px weight 300), sitting 64px from the top with 32px below before the hairline divider that opens the grid. No background color, no decorative elements — just text and the dividing line establishing grid territory below.

### Filter Bar

**`filter-bar`** — Sticky below the nav (top: 56px), 44px height, white background with a 1px hairline bottom border. Sort and filter controls labeled in `{typography.label-caps}`. An active filter state adds an underline to the label — no pill, no badge, no color change. Filter dropdowns open as flat white overlays with checkbox lists in `{typography.body-sm}`, `{rounded.none}` throughout.

### Size Selector

**`size-selector`** — A horizontal grid of flat rectangles (minimum 44px × 40px, `{rounded.none}`), each labeled with the size string in `{typography.label-caps}`. Available: white fill, 1px hairline border, ink text. Selected: black fill (#181818), white text (#ffffff). Unavailable: muted gray text (#c4c4c4) with strikethrough, same 1px hairline border. State flips instantly — no transition animation. Gap between cells is 4px.

### Cart Drawer

**`cart-drawer`** — Slides in from the right at 400px width over a 200ms ease-in transition. White background, 1px left border in hairline gray (#dedede). Item rows show a small product thumbnail, name in `{typography.body-sm}`, plain-text quantity input, and price right-aligned. Order total and a full-width primary button ("Checkout") pin to the bottom of the drawer. No shadow behind the drawer — just the border edge.

### Sale Badge

**`sale-badge`** — Flat rectangle in signal red (#e42c00), `{rounded.none}`, padded 2px × 6px, labeled "SALE" or a percentage discount in `{typography.label-caps}` with white text. Applied absolute at the top-left corner of product card images. The orange variant (#da532c) appears on editorial lookbook labels and promotional callout tags rather than product availability contexts.

### Lookbook Caption

**`lookbook-caption`** — Small text block in `{typography.caption}` at muted gray (#c4c4c4) appearing below editorial imagery in lookbook and campaign grids. Maximum width 320px, 8px top gap from the image edge. Functions as a discreet credit or product annotation line, never as a headline element.

### Newsletter Signup

**`newsletter-signup`** — Appears in the pre-footer on a light gray (#f7f7f7) surface. Section label in `{typography.label-caps}`, one-line description in `{typography.body-sm}`. Input field has no box border — only a bottom line in hairline gray that transitions to ink on focus. Submit renders as `button-primary` full-width or inline-right. No card framing, no elevation — the section is a surface color break, nothing more.

### Footer

**`footer`** — Full-width near-black (#121212) background. Column links in `{typography.caption}` white (#ffffff); hover state transitions to muted gray (#c4c4c4). Column headers in `{typography.label-caps}` white. Four to five columns at desktop with 48px column gaps; legal and copyright text at the base at 10px muted gray. The near-black footer creates a strong terminal boundary for every page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger icon + centered wordmark + cart icon; filter bar becomes a bottom-sheet overlay; hero text moves below image at `display-sm` scale; cart drawer expands to full screen width |
| Tablet | 744–1128px | Two-column product grid; nav text links remain visible but at tighter spacing; editorial heroes may switch to side-by-side image-and-text split at 50/50; footer collapses to two columns |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav bar with all category links visible; editorial heroes run full-bleed at 80vh minimum; filter bar sticky at 56px offset |
| Wide | > 1440px | Content max-width caps at 1440px with symmetric outer gutters; typography scales hold — no display-xl inflation at wider viewports; hero images crop to center rather than scaling up |

### Touch Targets

- All interactive controls maintain a minimum 44px touch target height
- Size selector cells are minimum 44px × 40px; transparent horizontal padding compensates for narrow size strings
- Nav icon buttons (search, account, cart) hold 44px × 44px tap area regardless of visual icon size
- Cart drawer quantity controls include 44px-height invisible tap zones even when visually compact
- Filter bar labels include expanded tap padding to reach 44px height

### Collapsing Strategy

- Navigation: full text-link row → hamburger icon with full-screen white slide-in overlay; overlay links in `{typography.display-sm}` (24px), stacked vertically with `{spacing.lg}` gaps
- Filter bar: sticky horizontal row → single "Filter & Sort" button → full-screen bottom-sheet overlay with checkbox stacks
- Editorial hero: full-bleed 80vh image with text below → full-width image at natural height with stacked text block at `{typography.display-sm}`
- Product grid: 4-col → 3-col (tablet) → 2-col (mobile) → 1-col only on screens narrower than 360px
- Footer: 4–5 column grid → 2-column grid (tablet) → single-column accordion with expand/collapse chevrons (mobile); near-black background holds full-width at all breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Sohne weight values per component not confirmed from CSS extraction; weights 300/400/500 are inferred from visual analysis of documented brand usage
- Hover transition timing and easing curves not captured in static extraction; 200ms ease-in for cart drawer is an estimate
- `{colors.surface-soft}` (#f7f7f7) is inferred — the exact tinted pre-footer background was not directly extracted from the live site
- Structural role of `{colors.accent-blue}` (#5bbad5) and `{colors.accent-teal}` (#aadddd) is unconfirmed; these may be favicon/PWA manifest colors rather than active UI tokens in the current season
- `{colors.accent-orange}` (#da532c) role is inferred as editorial/lookbook use; not confirmed as a sale or alert system color
- Logo dimensions, clearspace rules, and logo variant (wordmark vs. monogram) not extracted
- Exact product grid gutter values approximated at 16px; confirmation requires CSS inspection
- Mobile navigation exact interaction (hamburger vs. text list vs. overlay) not confirmed from static extraction
- Animation easing curves for size-selector state change and filter overlay entrance not available
- Cart drawer width (400px) is an estimate; actual implementation value not extracted
