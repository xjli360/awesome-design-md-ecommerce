---
version: alpha
name: "Foundrae"
source_url: "https://foundrae.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Coral fire (#ff7f50) interrupts an otherwise near-monochrome hierarchy — charcoal bodies (#1c1c1c), near-void backfields (#0a0e10), and ash midtones (#808080) — marking the single CTA pulse in a layout otherwise organized around restraint. Foundrae's digital environment is built around the medallion: a disc, a symbol, a weight felt in the hand. The editorial engine runs on essentially four tones — the near-black ground, a medium gray for secondary text, an olive-stone mid (#757562) that reads like aged metal in certain light, and a pale ash (#dedede) used for hairlines so thin they suggest engraved lines rather than dividers.

  Type runs on inherited system stacks — exact typefaces couldn't be extracted from the live site, suggesting font delivery via JavaScript or a proprietary loader. The visual evidence points toward a serif-dominant display register: tall, unhurried letterforms over dark imagery, small caps for collection labels, and generous tracking in category headers that gives each word room to breathe without competing with the jewelry itself. Body copy stays at a modest 14–16px range and never fights the headline for dominance.

  Product cards run edge-to-edge on the image, with price and title in a compact stack below — the emphasis is always the object, never the surrounding container. `{rounded.none}` governs card and button geometry, a hard-cornered vocabulary that reads architectural rather than approachable. The sole softness in the system comes from `{rounded.full}` pill tags used for material or collection filters, where circular borders signal interactivity without breaking the editorial register.

  The coral primary (#ff7f50) appears with surgical precision: the Add to Cart CTA, newsletter submit, and hover states on selected swatches. Everything else defers to the near-black (#0a0e10) foundation. Foundrae treats its symbolic inventory — the Wholeness medallion, the Alchemy disc, the protective Eye — as the true visual language of the brand; the UI exists to step aside and let those objects speak.

colors:
  primary: "#ff7f50"
  primary-active: "#e5612e"
  primary-disabled: "#f5c4ae"
  ink: "#0a0e10"
  body: "#1c1c1c"
  muted: "#808080"
  muted-soft: "#757562"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  canvas-dark: "#0a0e10"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  olive-stone: "#757562"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: 0.04em
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.03em
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.02em
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.06em
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.01em
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.05em
  label-uppercase:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.14em
    textTransform: uppercase
  price-display:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.10em
    textTransform: uppercase

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
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.on-dark}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: none
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  nav-bar-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
    logoColor: "{colors.on-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageRatio: "1 / 1"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.body}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    padding: "{spacing.sm}"
    gap: "{spacing.xs}"
    hoverImageScale: 1.03
    hoverTransition: "transform 400ms ease"
  hero-editorial:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: "button-secondary-on-dark"
    minHeight: 80vh
    contentAlign: center
    overlay: "rgba(10,14,16,0.35)"
  collection-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.label-uppercase}"
    imageRatio: "3 / 4"
    rounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.xl}"
    gap: "{spacing.lg}"
  symbol-badge:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.muted}"
  filter-pill:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 16px"
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
    padding: "6px 16px"
  engraving-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    ctaTypography: "{typography.button-sm}"
    ctaColor: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  pdp-swatch:
    size: 28px
    rounded: "{rounded.full}"
    borderDefault: "2px solid transparent"
    borderSelected: "2px solid {colors.ink}"
    borderHover: "2px solid {colors.muted}"
    gap: "{spacing.sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.label-uppercase}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.on-dark}"
    borderTop: "1px solid {colors.muted}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Coral-filled (#ff7f50) with hard-cornered geometry (`{rounded.none}`), uppercase tracking at 0.12em, 48px tall. On `:hover`, shifts to the active tone (#e5612e); on `:disabled`, bleaches to the pale blush (#f5c4ae). Used exclusively for the highest-intent action on screen — typically "Add to Cart" or "Shop Now."

**`button-secondary`** — Transparent background with a 1px solid border inheriting the ink color (#0a0e10). Matches the primary's geometry and uppercase type; reads as an outlined press against light canvases. The `button-secondary-on-dark` variant swaps the border and label to #ffffff for use over hero and editorial dark backgrounds.

**`button-ghost`** — No border, no fill; muted gray text at `{typography.button-sm}`. Used for low-priority actions like "Learn More" or "View Details" where the environment should carry the weight.

### Navigation
**`nav-bar`** — 64px tall, white canvas with a single 1px hairline border below. All nav links run `{typography.nav-link}` — 12px, 500 weight, 0.10em letter-spacing, all caps — keeping the header tightly architectural. On pages with dark hero images the `nav-bar-dark` variant activates, flipping canvas and label to near-black and white respectively, producing a transparent-feeling overlay. The wordmark centers or left-aligns depending on viewport width; cart and search sit right.

### Product Card
**`product-card`** — Square or near-square image ratio dominates; title and price appear below in a compact two-row stack with no visual container. Title uses `{typography.title-sm}` in the body gray (#1c1c1c); price runs `{typography.price-display}` — the sole serif-stack appearance in the card, giving the number an heirloom weight. On hover the image scales to 1.03× over 400ms with an ease curve, the only motion in an otherwise static layout. Cards sit in CSS grid with no visible gutters at the smallest breakpoint, narrow gaps on wider viewports.

### Hero Editorial
**`hero-editorial`** — Full-bleed dark image or video with a 35% black overlay. Headline runs `{typography.display-xl}` — 48px, 300 weight, wide tracking — in #ffffff. A secondary CTA uses `button-secondary-on-dark` positioned below by `{spacing.xl}`. Minimum height is 80vh on desktop, full screen on mobile. Content alignment centers both horizontally and vertically, placing the jewelry silhouette and brand statement on the same axis.

### Collection Strip
**`collection-strip`** — Horizontal row of 3–5 portrait-ratio category images with label text running `{typography.label-uppercase}` below each tile. The strip sits on the `{colors.surface-soft}` ground to lift it from the white product grid above. No card border, no shadow — just the image edge against the soft background.

### Symbol Badge & Filter Pills
**`symbol-badge`** — Pill-shaped (`{rounded.full}`) against the dark surface (#121212), used to tag products by their symbolic meaning (Wholeness, Protection, Transformation). `{typography.label-uppercase}` in white with a 1px muted border. `filter-pill` and `filter-pill-active` follow the same pill geometry in the light variant: inactive is hairline-bordered on white; active inverts to ink fill with white text.

### Engraving Callout
**`engraving-callout`** — Inset panel on the PDP, soft-surface background with a 1px hairline border and generous padding (`{spacing.xl}`). A small headline in `{typography.title-md}` introduces the service; body copy in `{typography.body-sm}` explains personalization options. The inline CTA renders in coral (`{colors.primary}`) using `{typography.button-sm}`, the only colored link in the form area.

### PDP Swatches
**`pdp-swatch`** — 28px circles, `{rounded.full}`, with a 2px transparent border by default. The selected state shows a 2px ink border with a subtle 2px offset gap between swatch and border ring, achieving the "halo" selection indicator common in jewelry metal selectors. Hover previews the selection border in muted gray.

### Footer
**`footer`** — Near-black (#121212) ground with section headers in `{typography.label-uppercase}` (on-dark), link columns in `{typography.body-sm}` starting at muted gray (#808080) and lighting to white on hover. A single 1px muted border separates footer from body. Newsletter input uses a dark-variant `text-input` with a coral submit button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + cart icon; hero goes full-screen (100vh); collection strip scrolls horizontally; PDP image stacks above details |
| Tablet | 744–1128px | Two-column product grid; nav retains top bar with abbreviated labels; hero 80vh; collection strip shows 3 tiles |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav with all category labels; hero 80vh; collection strip 4–5 tiles; PDP splits 50/50 image–detail |
| Wide | > 1440px | Max content width ~1400px centered; four-column grid; editorial hero letterboxes to avoid over-stretching; side margins increase with `{spacing.section}` |

### Touch Targets
- All nav links and icon buttons are minimum 44×44px tap area regardless of visual size
- Swatch circles (28px visual) receive a 44px invisible tap target via padding or pseudo-element
- Filter pills maintain 36px minimum height on mobile even if label is short
- Footer links padded to 40px height for comfortable mobile navigation

### Collapsing Strategy
- Nav links collapse to a drawer at < 744px; category mega-menus become full-screen overlays
- Collection strip switches from a fixed-width grid to horizontal scroll-snap on mobile
- Engraving callout collapses inline below the Add to Cart button on mobile (not beside it)
- PDP image gallery collapses from a multi-thumbnail sidebar view to a swipeable single-image carousel

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font families could not be extracted — the live site returns `inherit` for all font-family declarations, indicating font tokens are delivered via JavaScript or a protected asset loader; typography scales above use system-serif/system-sans fallbacks
- No meta theme-color was set, so mobile browser chrome color is unspecified
- Brand may use a proprietary or licensed serif display typeface (evidence from editorial imagery suggests tall, light-weight serif letterforms) — confirm via brand guidelines or font inspector with JS enabled
- Hover and transition values for nav mega-menus, drawer animations, and PDP image zoom could not be reliably sampled
- Exact grid gutter widths and max-width breakpoints were not extractable from the live Shopify theme
- Dark-mode treatment is unconfirmed — extracted colors suggest a dark-first editorial preference but no `prefers-color-scheme` media query evidence was found
- Exact border-radius on the logo wordmark and any SVG icon treatment unknown
