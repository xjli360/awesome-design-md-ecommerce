---
version: alpha
name: "Automic Gold"
source_url: "https://www.automicgold.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep violet (#350b60) saturates every hero edge at Automic Gold — not the lavender of spas or the dusty mauve of minimalism, but a full-chroma jewel tone that reads as political and expensive in the same breath. Against it sits a 24-karat gold (#ffcc33) that matches the brand name literally: coin-bright, high-chroma, worn as both primary accent and ideological declaration. This purple-and-gold pairing is the brand's most legible statement — a queer-owned New York fine jeweler refusing the safe beige-and-ivory grammar of the category. The palette runs from this violet peak down through dark indigo (#18084d), to near-void navy (#08003c) at footers and editorial dividers, so the page travels from noon gold to absolute midnight. Blush (#fce2e6) enters as surface relief — the campaign-image fill or product-card background that prevents the composition from reading as all nightclub, all the time.

  Type runs on Soleil, a geometric humanist sans-serif whose even stroke weight lets jewelry copy breathe without fighting photography, and Boldline, a heavier display face that carries headlines. Neither font reaches for heavy weights to manufacture authority — the palette does that work. Letter-spacing stays tight, letting the gold-on-violet contrast carry the visual voltage rather than typographic scale.

  Form language mirrors the inventory: `{rounded.full}` pill CTAs and search bars that echo ring shanks, softly radiused product cards at `{rounded.md}`, and thumbnails with just enough radius (`{rounded.sm}`) to signal approachability. No hard interactive corner exists. The grid is generous at desktop — wide margins that frame each piece of jewelry as a standalone object — then collapses at mobile to full-bleed imagery that turns the viewport into a display case. The announcement bar runs `{colors.gold}` type on `{colors.primary}` background, reinforcing the brand's two-color signature at every scroll position. Sustainability and queer-owned identity are not footnotes here; they appear in badges and page-title copy with the same visual weight as the product name.

colors:
  primary: "#350b60"
  primary-active: "#240c72"
  primary-disabled: "#dedede"
  gold: "#ffcc33"
  blush: "#fce2e6"
  ink: "#121212"
  body: "#121212"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#fce2e6"
  surface-card: "#ffffff"
  deep-navy: "#18084d"
  abyss: "#08003c"
  on-primary: "#ffcc33"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Boldline', 'soleil', Arial, Helvetica, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Boldline', 'soleil', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Boldline', 'soleil', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'soleil', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'soleil', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'soleil', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'soleil', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'soleil', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-upper:
    fontFamily: "'soleil', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'soleil', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
  button-sm:
    fontFamily: "'soleil', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
  nav-link:
    fontFamily: "'soleil', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'soleil', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  badge-label:
    fontFamily: "'soleil', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "transparent"
    border: "2px solid {colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 30px
    height: 48px
  button-ghost-gold:
    backgroundColor: "transparent"
    border: "1px solid {colors.gold}"
    textColor: "{colors.gold}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    placeholderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    height: 36px
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.md}"
    imageRounded: "{rounded.md}"
    swatchSize: 14px
    swatchGap: "{spacing.xs}"
    hoverShadow: "0 4px 20px rgba(53,11,96,0.10)"
    padding: "{spacing.sm}"
  badge-sustainable:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-queer-owned:
    backgroundColor: "{colors.blush}"
    textColor: "{colors.primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.deep-navy}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    accentColor: "{colors.gold}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.full}"
    minHeight: 580px
    paddingX: "{spacing.xxl}"
  hero-homepage-split:
    backgroundLeft: "{colors.primary}"
    backgroundRight: "{colors.canvas}"
    textColorLeft: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    accentTypography: "{typography.caption-upper}"
    accentColor: "{colors.gold}"
  collection-grid:
    gap: "{spacing.base}"
    columnsDesktop: 4
    columnsTablet: 3
    columnsMobile: 2
    cardComponent: "product-card"
  pdp-image-gallery:
    mainImageRounded: "{rounded.md}"
    thumbnailRounded: "{rounded.sm}"
    thumbnailBorderActive: "2px solid {colors.primary}"
    thumbnailBorderInactive: "2px solid transparent"
    backgroundColor: "{colors.surface-soft}"
  filter-chip:
    backgroundColor: transparent
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 18px"
    height: 36px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 18px"
    height: 36px
  material-selector:
    backgroundColor: "{colors.surface-soft}"
    borderActive: "2px solid {colors.primary}"
    borderInactive: "2px solid transparent"
    textTypography: "{typography.caption-upper}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.abyss}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.gold}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.deep-navy}"
    paddingY: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Pill-shaped (`{rounded.full}`) with deep violet fill (#350b60) and gold (#ffcc33) text, this is the brand's most recognizable element: every primary CTA from "Add to Cart" to "Shop Now" wears this combination. Hover deepens to `{colors.primary-active}` (#240c72). Disabled state fills with `{colors.primary-disabled}` (light gray) to signal unavailability without the branded voltage.

**`button-secondary`** — Outlined pill using a 2px violet border with violet text on transparent background. Used for secondary actions like "View All" or filter resets. Maintains the pill silhouette so primary and secondary CTAs share a family resemblance without competing.

**`button-ghost-gold`** — Thin 1px gold-bordered pill with gold text on dark or violet backgrounds. Appears inside dark hero sections and editorial panels where the violet primary button would disappear into the background.

**`button-text-link`** — Underlined violet text, no background. Used for tertiary actions, fine-print links, and in-copy navigation within product descriptions.

### Navigation

**`nav-bar`** — White canvas bar at 64px height with a bottom hairline, violet logo mark, and Soleil 600-weight links. Desktop shows full category links; mobile collapses to hamburger. A persistent cart icon and search icon anchor the right end. The announcement bar above it runs inverted: violet background, gold uppercase text.

**`announcement-bar`** — 36px violet strip at the top of every page carrying rotating messages in `{typography.caption-upper}` gold — used for shipping thresholds, sustainability messaging, and new-collection alerts. The gold-on-violet here mirrors the button colors, creating instant brand recognition before any product is visible.

### Cards

**`product-card`** — Product image sits on a blush (#fce2e6) background at `{rounded.md}`, so every piece of jewelry photographs against a warm neutral. Below the image: product name in `{typography.title-md}`, price in `{typography.price-display}`, and a row of metal/size swatches. On hover, a soft violet-tinted shadow lifts the card. Badge overlays (`badge-sustainable`, `badge-new`) sit in the image's top-left corner.

**`pdp-image-gallery`** — Main image fills a blush-background container at `{rounded.md}`; thumbnail strip runs below with 2px violet borders activating on selection. Thumbnail insets use `{rounded.sm}` so the gallery reads as a family of soft-cornered surfaces.

### Badges

**`badge-sustainable`** — Gold fill (#ffcc33) with violet text, uppercase Soleil at 11px, 0.8px letter-spacing. Small enough to sit over a product image without obscuring the piece, prominent enough to read at a glance as the brand's primary credential.

**`badge-queer-owned`** — Blush fill (#fce2e6) with violet text. Same typography and pill shape as `badge-sustainable`, so the two identifiers form a paired system — one financial (gold), one political (pink).

### Hero

**`hero-section`** — Deep navy (#18084d) full-width canvas with white headlines in `{typography.display-xl}` and a gold accent line or subhead in `{typography.caption-upper}`. The primary CTA button uses the violet+gold combination. Minimum 580px height on desktop to let campaign photography breathe without cropping necks or hands.

**`hero-homepage-split`** — Two-panel layout: left half violet with gold headline and white subhead, right half white with a product photograph. The hard vertical split at the midpoint is the one place in the UI where no radius appears — the panel edge is `{rounded.none}`, making it read as intentional contrast to the otherwise pill-and-curve language.

### Filters and Selection

**`filter-chip`** / **`filter-chip-active`** — Pill chips for metal type, price range, and category filters. Inactive state is hairline-bordered and low-key. Active flips to violet fill with gold text, matching the CTA system so active selections feel like confirmed choices rather than mere highlights.

**`material-selector`** — Used on PDPs for gold-karat and metal-type selection. Soft-cornered rectangular tiles on blush background, 2px violet border activates. Caption uppercase label inside.

### Footer

**`footer`** — Near-void navy (#08003c) background with white body copy and gold links. The darkest surface on the site, it anchors the page and gives the gold link color maximum contrast. Four-column grid on desktop collapses to stacked accordion on mobile. Brand marks (sustainability certifications, queer-owned identifier) repeat here as footer badges.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + cart icon; hero goes full-bleed with text overlay; filter chips scroll horizontally; announcement bar reduces to single rotating message |
| Tablet | 744–1128px | 2–3 column product grid; nav shows logo + icons with hamburger for links; hero splits stack vertically; pdp gallery thumbnails move to horizontal strip below main image |
| Desktop | 1128–1440px | 4-column product grid; full nav link row visible; hero-homepage-split activates two-panel layout; pdp gallery shows vertical thumbnail column left of main image |
| Wide | > 1440px | Max content width ~1400px, outer margins fill in canvas white; hero padding expands to keep text optically centered; collection-grid column count holds at 4 |

### Touch Targets

- All interactive elements minimum 44×44px on touch viewports
- Pill CTAs set to `height: 48px` with horizontal padding expanding to preserve tap area
- Product swatches expand to 20px on mobile (from 14px desktop) via touch media query
- Filter chips minimum 36px height, 44px horizontal at smallest with label wrapping suppressed

### Collapsing Strategy

- Desktop 4-col product grid → Tablet 3-col → Mobile 2-col (never 1-col; even on 320px the grid holds 2 columns to show browse context)
- Horizontal announcement bar message truncates at 1 item on mobile, cycling via JS
- Footer 4-col links collapse to accordion (closed by default) on mobile; social icons and brand badge remain visible without expansion
- Hero split panel stacks on tablet with image moving below text; image height caps at 300px stacked to avoid scroll depth issues
- PDP image gallery: vertical thumbnail column on desktop → horizontal thumbnail strip on tablet → hidden strip with dot-indicator pagination on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Canvas white (#ffffff) and surface-card white were not in the extracted palette — inferred as implicit background; verify against live computed styles
- No mid-tone gray for body text in a muted or secondary context was extracted; #dedede (hairline gray) and #121212 (ink) represent the extremes only — a mid-gray around #767676 may exist for captions but could not be confirmed
- Disabled-state text color on `button-primary-disabled` is estimated; the actual disabled appearance was not extractable from static scrape
- Boldline font metrics (exact weights available, OpenType features, variable-font range) are unconfirmed — use as display-only with Soleil as the reliable fallback
- Exact nav height, announcement-bar height, and hero minimum height are estimated from visual inspection rather than extracted computed values
- Hover and focus ring styles (outline color, offset, width) were not captured; assume `{colors.primary}` 2px outline with 2px offset as an accessible default
- Product card hover shadow (rgba violet tint) is a design interpretation — the exact shadow token was not extracted
