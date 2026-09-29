---
version: alpha
name: "Erie Basin"
source_url: "https://www.eriebasin.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The near-black #121212 and cool silver #dedede of Erie Basin's palette read less like a brand choice and more like the actual tones of oxidized sterling and old photographic paper — the interface takes its color from the objects it sells. Based in Brooklyn's Carroll Gardens neighborhood, the shop stocks Georgian mourning pieces, Victorian rose-cut diamonds, and estate rings alongside its own EB Modern line, and the site treats each object with the spatial deference of a museum vitrine. There are no accent colors competing for attention; the entire chromatic vocabulary is a two-stop monochrome that forces the eye toward the jewelry itself. This constraint is not minimalism as aesthetic posture — it is a deliberate editorial argument that the pieces are old enough and rare enough to need no brand embellishment. Typography was not extractable from static HTML (the site loads tokens via JavaScript), so the type system below is modeled on the spare serif-plus-grotesque pairings common to gallery and estate contexts: a fine-weight serif for editorial headlines and a neutral sans-serif for UI chrome. Spacing is generous at every breakpoint, echoing the white-glove presentation of physical auction catalogs. Buttons are flat, sharp-cornered (`{rounded.none}`), and rendered in ink on canvas or inverted — never pill-shaped, never rounded, never soft. Product cards use no drop shadows; separation comes from hairline rules and deliberate void. The cart and account icons sit in the top-right corner of a hairline-ruled nav bar, with the logo centered in the manner of a jewelry house logotype rather than a DTC startup wordmark. The total effect is a site that smells faintly of old velvet trays and wears its restraint like a calling card.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#888888"
  ink: "#121212"
  body: "#2a2a2a"
  muted: "#6b6b6b"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-silver: "#dedede"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Garamond', 'EB Garamond', Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.02em
  display-md:
    fontFamily: "'Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0.01em
  display-sm:
    fontFamily: "'Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  price-display:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  logo-display:
    fontFamily: "'Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.15em
    textTransform: uppercase
  editorial-pull:
    fontFamily: "'Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0.01em

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
    height: 44px
    border: none
  button-primary-hover:
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
    padding: 13px 27px
    height: 44px
    border: 1px solid {colors.ink}
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: 1px solid {colors.ink}
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
    textUnderlineOffset: 3px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.ink}
    padding: 12px 14px
    height: 44px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: 1px solid {colors.hairline}
    layout: center-logo with flanking nav groups
    logoTypography: "{typography.logo-display}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border: 1px solid {colors.hairline}
    padding: "{spacing.lg}"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: none
    imageAspectRatio: 1/1
    gap: "{spacing.sm}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    hoverEffect: second-image crossfade
  product-grid:
    columns: 4
    gap: "{spacing.xl}"
    padding: 0
    mobileColumns: 2
    mobileGap: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    layout: full-bleed editorial image with overlaid or below-image text
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.editorial-pull}"
    padding: "{spacing.section} 0"
    imagePosition: center
  collection-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.section}"
    rounded: "{rounded.none}"
    borderBottom: 1px solid {colors.hairline}"
  section-label:
    textColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.lg}"
    borderBottom: none
  divider-hairline:
    color: "{colors.hairline}"
    height: 1px
    margin: "{spacing.xxl} 0"
  badge-era:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    border: 1px solid {colors.hairline}
    rounded: "{rounded.none}"
    padding: 4px 8px
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: 1px solid {colors.hairline}
    height: 48px
    activeColor: "{colors.ink}"
    inactiveColor: "{colors.muted}"
  product-detail-layout:
    imageColumn: 60%
    infoColumn: 40%
    gap: "{spacing.xxl}"
    rounded: "{rounded.none}"
    priceTypography: "{typography.price-display}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
  inquiry-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl}"
    rounded: "{rounded.none}"
    border: 1px solid {colors.hairline}
    note: used for items requiring direct inquiry rather than add-to-cart
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    linkTypography: "{typography.button-sm}"
    padding: "{spacing.xxl} {spacing.section}"
    rounded: "{rounded.none}"
    columnLayout: 3-column
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: 1px solid {colors.hairline}
    rounded: "{rounded.none}"
    width: 420px
    overlay: rgba(18,18,18,0.4)

## Components

### Buttons

**`button-primary`** — A flat, square-cornered (`{rounded.none}`) block in #121212 with white uppercase tracking-wide label at 12px. No shadow, no gradient, no hover animation beyond a snap to pure black (#000000). Disabled state mutes to #888888 with unchanged geometry. This is a button that behaves like a ink stamp: immediate, declarative, no soft edges.

**`button-secondary`** — Same dimensions and typographic spec as primary but inverted: white fill with a 1px #121212 border. On hover the fill transitions to `{colors.surface-soft}` — a barely-there off-white — signaling interactivity without softening the silhouette. Used for secondary actions such as "Save" or "Share" on product detail pages.

**`button-text`** — Transparent background, inline underline with a 3px offset. Reserved for tertiary actions like "View more" in collection footers or legal links in the footer. Inherits `{typography.button-sm}` tracking so it remains consistent with other UI chrome.

### Navigation

**`nav-bar`** — 60px tall, white background, 1px `{colors.hairline}` bottom border. The Erie Basin logotype sits centered in `{typography.logo-display}` — a widely-spaced uppercase serif. Flanking nav groups (left: Shop, Collections, EB Modern; right: Search, Cart, Account) use `{typography.nav-link}`. No hamburger on desktop. The centered-logo arrangement is a deliberate fine-jewelry convention that reads as a house mark rather than a startup wordmark.

**`nav-dropdown`** — Full-width or column-constrained panel in white, flush to the nav bottom border, with 1px hairline surround. Content is set in `{typography.nav-link}`, grouped by category (Era, Metal, Stone). No icons, no images in nav — navigation is pure text taxonomy.

### Product Display

**`product-card`** — Square image at 1:1 aspect ratio, no border, no shadow, no rounded corners. Title renders in `{typography.body-sm}` and price in `{typography.price-display}` below. On hover, a second product image crossfades in — the only animation on the page. No "Add to Cart" button surfaces on the card; selection always routes to the PDP.

**`product-grid`** — Four columns on desktop with `{spacing.xl}` gaps, collapsing to two columns on mobile. No container padding at edges; the grid runs to the layout margin. Section label (`{typography.title-sm}`, muted color) sits above the grid separated by `{spacing.lg}`.

**`product-detail-layout`** — Split 60/40 column layout: imagery left, detail right. The image column may scroll through multiple views while the right panel stays sticky. Title uses `{typography.display-sm}` (serif), price `{typography.price-display}` (sans), and provenance/description text `{typography.body-md}`. Many pieces route to an `{inquiry-block}` rather than a standard add-to-cart flow, reflecting the one-of-a-kind estate nature of inventory.

### Editorial & Marketing

**`hero`** — Full-bleed editorial photograph, often a close macro of a single piece against neutral ground. Headline overlaid or placed below in `{typography.display-xl}` at light weight 300. Body text in `{typography.editorial-pull}`, a fine-weight serif at 18px. No colored overlays on the image — the photograph is never tinted or dimmed.

**`collection-banner`** — Off-white `{colors.surface-soft}` band with centered headline in `{typography.display-md}` and a supporting caption in `{typography.caption}`. Separated from the grid below by a `{colors.hairline}` 1px rule. Used at the top of filtered collection pages (e.g., "Georgian," "Art Deco," "EB Modern").

**`section-label`** — A muted uppercase label in `{typography.title-sm}` floated above a content block with `{spacing.lg}` margin below. No decorative rule beneath. Used to introduce grid sections ("Recently Added," "Estate Diamonds") without adding visual weight.

**`badge-era`** — A small rectangular tag with 1px `{colors.hairline}` border, no fill, set in `{typography.caption}` muted color. Used to surface era metadata (Georgian, Victorian, Edwardian, Art Deco) directly on PDP or as a filter chip. Shape is always rectangular (`{rounded.none}`).

**`inquiry-block`** — A `{colors.surface-soft}` panel with 1px hairline border replacing the standard add-to-cart widget for one-of-a-kind pieces. Contains a brief note in `{typography.body-sm}` and a primary button labeled "Inquire" or "Email Us." This component is central to the estate jewelry buying flow.

### Footer

**`footer`** — Inverted: #121212 background, white text. Three-column layout at `{spacing.section}` horizontal padding. Navigation links in `{typography.button-sm}` uppercase tracking; legal copy and newsletter field in `{typography.caption}`. The full inversion is the single moment of high contrast in the page composition, closing the scroll with the brand's primary ink color.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column nav collapses to hamburger; product grid drops to 2 columns; hero text moves below image; inquiry-block stacks vertically; footer collapses to single column |
| Tablet | 744–1128px | Product grid is 3 columns; nav may show abbreviated link set; hero image cropped to portrait; PDP stacks image above info |
| Desktop | 1128–1440px | Full 4-column product grid; 60/40 PDP split; centered logo nav fully expanded; hero runs edge-to-edge |
| Wide | > 1440px | Max content width capped around 1440px; hero image continues full-bleed behind constrained text column |

### Touch Targets

- All nav links and icon buttons maintain minimum 44×44px tap target via padding
- Filter bar items use `height: 48px` regardless of text size
- Cart and account icons in the nav bar have explicit 44px tap areas even when visually smaller
- CTA buttons are `height: 44px` minimum; inquiry form inputs `height: 44px`

### Collapsing Strategy

- Nav collapses to hamburger at < 744px; logo remains centered in mobile nav bar
- Product grid: 4 col → 3 col → 2 col (no 1-col grid; always pairs)
- PDP: side-by-side 60/40 → stacked full-width image then full-width info panel
- Footer columns collapse to single stacked column at mobile; newsletter input moves above link groups
- Section labels and era badges remain visible at all breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font families detected from static HTML extraction — the site almost certainly loads typography via a JavaScript theme layer or Shopify section schema; the type system above (Garamond serif + Helvetica Neue sans) is inferred from brand character and gallery-retail conventions, not extracted data
- Only two hex values extracted (#dedede, #121212) plus the theme-color white (#ffffff); the full color system beyond these three stops is inferred from the monochromatic palette logic rather than confirmed CSS custom properties
- Exact font weights, sizes, and letter-spacing values for headings and body text could not be confirmed; all typography scales are modeled estimates
- Hover animation timing and easing curves (particularly for the product-card second-image crossfade) were not extractable
- Whether EB Modern uses a typographically distinct sub-brand treatment (different weight, size, or typeface) could not be confirmed from extraction
- Breakpoint values (exact pixel thresholds for Shopify theme responsive behavior) are estimated from Shopify defaults, not confirmed from the live theme
- Cart drawer vs. cart page preference unconfirmed; drawer assumed based on modern Shopify theme conventions
