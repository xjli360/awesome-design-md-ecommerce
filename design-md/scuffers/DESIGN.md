---
version: alpha
name: "Scuffers"
source_url: "https://scuffers.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Army green (#2b7551) does the heaviest lifting in Scuffers' palette — a muted, military-inflected hue that reads as both streetwear credibility and a deliberate refusal of the softer sage tones that have overtaken the category. It anchors every primary action against a near-monochrome neutral field that runs from off-white (#f6f6f6) through mid-gray (#c8c8c8), the whole stack existing to give that green somewhere to land. The lone disruptive note is a warning-stripe yellow (#ffee5b): saturated, industrial, almost tape-measure yellow — the kind of accent that streetwear borrows from construction sites and safety gear rather than from fashion. Typography stays entirely in the system stack (Arial, Helvetica Neue, Segoe UI) with no custom display face, which reads less as budget constraint and more as a streetwear-adjacent austerity — the brand doesn't need a logo font to signal taste, the colorwork does that. Dark surfaces draw from a pair of near-black charcoals (#1b2224 and #263033) that feel closer to wet concrete than pure black, giving the dark-mode or footer zones a gritty warmth. Rounding throughout is restrained: buttons and cards hold a modest `{rounded.sm}` — no pill shapes, no bubble UI — because the vocabulary is urban utility, not approachable consumer tech. Spacing is generous at the section level to let product photography breathe, compressed at the component level to signal density and a full catalog. The overall posture is confident understatement: a two-accent system (green + yellow) deployed with discipline against a field of grays, no gradients, no decorative type, and a strict grid that lets garments define the visual temperature of any given page.

colors:
  primary: "#2b7551"
  primary-active: "#1f5a3d"
  primary-disabled: "#a4c8b5"
  accent: "#ffee5b"
  accent-active: "#f0d800"
  ink: "#1b2224"
  ink-secondary: "#263033"
  body: "#263033"
  muted: "#6b7072"
  hairline: "#c8c8c8"
  hairline-soft: "#e7e7e7"
  canvas: "#f6f6f6"
  surface-soft: "#eaeaea"
  surface-card: "#f8f8f8"
  surface-mid: "#e8e8e8"
  on-primary: "#ffffff"
  on-accent: "#1b2224"
  on-dark: "#f6f6f6"
  dark-surface: "#1b2224"
  dark-surface-raised: "#263033"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -1px
    textTransform: uppercase
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
    textTransform: uppercase
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-bold:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.25px
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  announcement:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.ink}"
    padding: 12px 26px
    height: 48px
  button-secondary-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.on-dark}"
    padding: 12px 26px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
    height: 48px
    placeholderColor: "{colors.muted}"
  text-input-dark:
    backgroundColor: "{colors.dark-surface-raised}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    iconColor: "{colors.ink}"
    cartBadgeBackground: "{colors.primary}"
    cartBadgeText: "{colors.on-primary}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.announcement}"
    height: 40px
    padding: 0 {spacing.base}
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageBackground: "{colors.surface-mid}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    salePriceColor: "{colors.primary}"
    originalPriceColor: "{colors.muted}"
    badgePosition: top-left
    padding: "{spacing.sm}"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    overlayColor: "rgba(27,34,36,0.45)"
    ctaButton: "{components.button-accent}"
    minHeight: 560px
    textAlign: left
    padding: "{spacing.section} {spacing.xl}"
  collection-hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    padding: "{spacing.xl} {spacing.section}"
    borderBottom: "1px solid {colors.hairline}"
  product-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-badge-soldout:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 44px
    minWidth: 44px
    selectedBackground: "{colors.ink}"
    selectedText: "{colors.on-dark}"
    selectedBorder: "1px solid {colors.ink}"
    soldoutOpacity: 0.35
    soldoutTextDecoration: line-through
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.ink}"
    offset: 3px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    headerTypography: "{typography.display-sm}"
    itemTitleTypography: "{typography.title-sm}"
    itemPriceTypography: "{typography.price}"
    subtotalTypography: "{typography.title-md}"
    checkoutButton: "{components.button-primary}"
  collection-filter:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.caption-bold}"
    borderBottom: "1px solid {colors.hairline}"
    activeFilterBackground: "{colors.ink}"
    activeFilterText: "{colors.on-dark}"
    activeFilterTypography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.caption-bold}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.surface-soft}"
    linkHoverColor: "{colors.on-dark}"
    dividerColor: "{colors.dark-surface-raised}"
    padding: "{spacing.section} 0"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 48px
    iconColor: "{colors.muted}"
    padding: 0 {spacing.base}

## Components

### Buttons

**`button-primary`** — Square-cornered (`{rounded.none}`) green (#2b7551) block with all-caps, wide-tracked type at 1.5px letter-spacing. Hover deepens to `{colors.primary-active}` (#1f5a3d) with no border-radius softening; the shape stays hard-edged throughout the interaction. Disabled state fades the fill to `{colors.primary-disabled}` while keeping white text, preserving legibility. Height locks at 48px across all breakpoints.

**`button-accent`** — Same sharp geometry as primary but fires in warning-stripe yellow (`{colors.accent}`, #ffee5b) with near-black text (`{colors.on-accent}`). Used for highest-urgency CTAs — limited drops, flash sales, cart checkout — where the green reads as "brand" but the yellow reads as "act now." Active state deepens to `{colors.accent-active}`.

**`button-secondary`** — Transparent fill with a 2px solid ink border; text matches the border color. On dark backgrounds, `button-secondary-dark` flips both border and text to `{colors.on-dark}`. The no-radius treatment ensures it reads as a deliberate design choice, not an oversight.

**`button-ghost`** — Text-only, no border, primary green color with underline. Used for lower-hierarchy actions like "View all", "See more", editorial links.

### Navigation

**`nav-bar`** — Canvas-colored (`{colors.canvas}`) bar at 60px height, sitting below a 40px `announcement-bar` in primary green. Navigation links render in all-caps 13px with 1.5px tracking — the same compressed-utility register as a workwear label. Cart icon carries a badge in `{colors.primary}` green. Mobile collapses to hamburger with full-screen drawer.

**`announcement-bar`** — Full-bleed green (#2b7551) strip at the top of every page. White all-caps type at 12px / 1.5px tracking for shipping thresholds, drop countdowns, or promotional codes. Single-line; no dismiss control on mobile.

### Product Cards

**`product-card`** — No border-radius anywhere on the card frame. Image zone sits on `{colors.surface-mid}` (#e8e8e8) as a loading/fallback state. Title renders in 14px bold all-caps (`{typography.title-sm}`), price in 16px bold (`{typography.price}`). Sale price adopts `{colors.primary}` green with the original struck through in `{colors.muted}`. Badges (`product-badge`, `product-badge-sale`, `product-badge-soldout`) are sharp-cornered and sit top-left over the image.

### Product Detail

**`size-selector`** — Grid of sharp-cornered tiles; unselected state is light card with hairline border, selected inverts to solid ink fill with white text. Sold-out sizes retain their tile but render with reduced opacity (0.35) and a strikethrough — they stay visible so customers understand the range, not hidden to suggest the size doesn't exist.

**`color-swatch`** — 28px circular swatches with a 2px offset ring for the selected state; the ring color is `{colors.ink}` so it works over any swatch fill including white.

### Cart

**`cart-drawer`** — 400px side drawer from the right edge, separated from the main canvas by a hairline border. No border-radius on the container. Subtotal and checkout button anchor to the bottom of the drawer; the item list scrolls independently above. Checkout button inherits `button-primary` full-width.

### Collection

**`collection-filter`** — Flat filter bar with no radius. Active filters render as small ink-colored chips (`{colors.ink}` fill, white text, `{typography.badge}`). Filter labels are all-caps caption weight; the active state is a hard inversion, not a soft highlight.

**`collection-hero`** — Muted gray-surface header zone with the collection name in `{typography.display-md}` all-caps, no photography. Clean separation from the product grid below via hairline border.

### Hero

**`hero-banner`** — Dark-surface base (#1b2224) with a translucent overlay (rgba 45%) allowing full-bleed photography to read through. Headline in `{typography.display-xl}` (48px, 800 weight, uppercase) hard-left aligned. CTA defaults to `button-accent` yellow — the only moment yellow and black meet on a dark field, maximizing contrast. Minimum height 560px; mobile drops to 420px.

### Footer

**`footer`** — Full-width dark surface (#1b2224) with column headings in `{typography.caption-bold}` (all-caps, tracked) and link lists in `{typography.body-sm}`. Link color is `{colors.surface-soft}` (#eaeaea) rather than pure white, softening the contrast slightly against the near-black background. Internal dividers use the slightly lighter charcoal (`{colors.dark-surface-raised}`, #263033).

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with full-screen overlay drawer; hero min-height 420px; cart drawer full-width; announcement bar wraps to two lines if needed |
| Tablet | 744–1128px | Two-column product grid; nav bar retains full links if catalog is small, otherwise hamburger; cart drawer 360px |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with dropdowns; cart drawer 400px; hero 560px min-height |
| Wide | > 1440px | Grid constrained to 1440px max-width centered; hero background extends edge-to-edge, content centered within 1440px container |

### Touch Targets

- All interactive tiles (size selectors, color swatches, filter chips) minimum 44×44px on mobile
- Cart and hamburger icons in nav: 44px tap zone regardless of visual icon size
- Product cards expand full column width; image occupies top portion, info below — no hover-only states on touch

### Collapsing Strategy

- Navigation: hamburger at < 1024px; drawer slides in from left with overlay scrim
- Filter bar: collapses to a horizontal scroll strip on mobile; "Filters" button opens a bottom sheet
- Product grid: 1 col (mobile) → 2 col (tablet) → 3 col (desktop) → 4 col (wide)
- Footer: single-column accordion on mobile (section headings toggle link lists); two columns on tablet; four columns on desktop
- Announcement bar: single line on desktop; wraps and increases height on mobile if text is long

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand font detected — all typography stacks are system fonts (Arial, Helvetica Neue, Segoe UI). Scuffers may load a custom face via JS after bot-check or may intentionally use system fonts as a design choice; this cannot be confirmed from extraction alone.
- Color palette is sparse in saturation: only #2b7551 (meta theme-color) and #ffee5b provide chromatic signal; all other extracted values are near-neutral grays. The brand may use additional accent colors in campaign pages or lookbooks not captured in the crawl.
- #007aff appears in the extracted palette but is the iOS/Safari system highlight color, not a Scuffers brand color — excluded from the design system.
- No icon style, icon library, or illustration system could be inferred from extraction.
- Typography sizing, weight hierarchy, and spacing rhythms are estimated from streetwear category conventions; no computed CSS values were extracted.
- Dark mode support (if any) could not be determined from the extraction; the dark-surface tokens above are inferred from the dark charcoal colors (#1b2224, #263033) present in the palette.
- Shopify theme name unknown; component markup conventions may differ from standard Shopify Dawn defaults.
