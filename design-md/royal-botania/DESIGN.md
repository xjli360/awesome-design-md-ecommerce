---
version: alpha
name: "Royal Botania"
source_url: "https://www.royalbotania.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Bronze light pooling on a teak slat at golden hour — that is the color temperature Royal Botania builds its entire digital presence around. The extracted palette pivots on #ba8748, a burnished amber that appears in hover states, accent lines, and primary CTAs, pulling the user's eye toward configurators and collection links the way afternoon sun catches oiled wood grain. Supporting it is a full gradient of warm earth tones (#cec9c0 through #342f28) that replace the cold grays most luxury sites default to; even the lightest canvas (#fafafb) carries a barely-perceptible warmth at #fbfaf9 and #f5eee5, so white space reads as sunlit limestone rather than sterile gallery wall. Typography pairs a refined serif (used for display headings and product names — loaded as `fontSecondary` via Next.js font optimization) with a clean geometric sans-serif (`fontPrimary`) handling navigation, body copy, and interface labels. Weights stay restrained: display type at 300–400, body at 400, buttons at 500 — the brand whispers rather than shouts. Corner radii are minimal throughout; product cards and image containers sit at `{rounded.xs}` or `{rounded.none}`, reinforcing the architectural precision of the furniture itself. Buttons use a subtle `{rounded.xs}` with generous horizontal padding, reading as slim material strips rather than bubbly pills. Spacing is generous — section gaps push to 80–120px on desktop, letting full-bleed lifestyle photography breathe. The navigation bar is a thin, transparent-to-white element that overlays hero imagery, collapsing to a hamburger early (below 1024px) to preserve visual real estate. Color-coded collection badges use muted earth variants (#9b907d, #655c4e) rather than saturated tags, keeping the page temperature unified. The overall effect is a digital showroom that feels like walking through a Belgian courtyard — warm stone, polished metal, and diffused natural light.

colors:
  primary: "#ba8748"
  primary-active: "#946b38"
  primary-disabled: "#dcc2a2"
  accent-bronze: "#aa7b40"
  accent-dark: "#7a582e"
  accent-warm: "#ceaa7d"
  ink: "#121212"
  body: "#454545"
  muted: "#807e7e"
  muted-warm: "#9b907d"
  hairline: "#eaeaea"
  hairline-warm: "#e0ddd7"
  border-strong: "#a7a7a7"
  canvas: "#fafafb"
  canvas-warm: "#fbfaf9"
  surface-soft: "#f5f5f5"
  surface-warm: "#f5eee5"
  surface-card: "#ffffff"
  surface-tinted: "#f2f0ee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  teak: "#655c4e"
  stone: "#4b453a"
  charcoal: "#2b2b2b"
  deep-earth: "#342f28"
  sand-light: "#e9d8c4"
  sand-mid: "#cec9c0"
  sand-dark: "#b6aea0"
  overlay-scrim: "#121212"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.1px
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.15px
  body-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-uppercase:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  product-name:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
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
  section-lg: 96px
  section-xl: 120px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
    borderWidth: 0
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 8px 0
    borderBottom: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
  text-input-label:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  nav-bar:
    backgroundColor: "rgba(255,255,255,0.95)"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    backdropFilter: "blur(12px)"
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-transparent:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    overflow: hidden
    imageAspectRatio: "4:3"
    padding: 0
  product-card-body:
    padding: "{spacing.lg} {spacing.base}"
    titleTypography: "{typography.product-name}"
    subtitleTypography: "{typography.caption}"
    subtitleColor: "{colors.muted}"
  product-card-hover:
    transform: "translateY(-2px)"
    transition: "transform 0.3s ease"
  hero-section:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-lg}"
    minHeight: "90vh"
    overlayGradient: "linear-gradient(to bottom, rgba(18,18,18,0.2), rgba(18,18,18,0.5))"
    contentAlignment: "center"
    padding: "{spacing.section-xl} {spacing.xl}"
  hero-caption:
    typography: "{typography.caption-uppercase}"
    textColor: "{colors.sand-light}"
    marginBottom: "{spacing.base}"
  collection-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  collection-badge:
    backgroundColor: "{colors.sand-mid}"
    textColor: "{colors.deep-earth}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  material-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    borderWidth: 2px
    borderColor: "{colors.hairline-warm}"
    selectedBorderColor: "{colors.primary}"
  material-swatch-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted-warm}"
  configurator-panel:
    backgroundColor: "{colors.canvas-warm}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    borderLeft: "1px solid {colors.hairline-warm}"
  configurator-option:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.deep-earth}"
    textColor: "{colors.sand-light}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section-lg} {spacing.xl}"
    linkColor: "{colors.sand-mid}"
    linkHoverColor: "{colors.on-dark}"
  footer-heading:
    typography: "{typography.caption-uppercase}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.lg}"
  search-overlay:
    backgroundColor: "rgba(18,18,18,0.85)"
    textColor: "{colors.on-dark}"
    inputBackgroundColor: transparent
    inputBorderBottom: "2px solid {colors.primary}"
    inputTypography: "{typography.display-sm}"
    backdropFilter: "blur(8px)"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  image-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    thumbnailSize: 64px
    thumbnailBorder: "2px solid transparent"
    thumbnailActiveBorder: "2px solid {colors.primary}"
    gap: "{spacing.sm}"

---

## Components

### Buttons

**`button-primary`** — A slim, uppercase-lettered bar in burnished amber (#ba8748) with white text. Corners are barely softened at `{rounded.xs}`, reading as a precise metal strip rather than a soft consumer pill. On hover, the background deepens to #946b38; disabled state fades to #dcc2a2 with reduced opacity. Generous horizontal padding (32px) gives the label breathing room.

**`button-secondary`** — Transparent fill with a 1px ink border and uppercase label matching the primary button's typographic treatment. On hover, the fill inverts to full ink (#121212) with white text, creating a decisive state change. Used for secondary actions like "View Collection" or "Download Specs."

**`button-tertiary`** — A text-only link-style button with an amber underline, used inline within editorial content or as "Read More" triggers. No background, no border radius — just label and rule.

### Navigation

**`nav-bar`** — A 72px-tall bar that begins transparent over hero imagery (white text) and transitions to a frosted white (95% opacity + 12px backdrop blur) on scroll. Navigation links are uppercase at 13px with 0.5px letter-spacing. Logo sits left; a hamburger menu and search icon sit right. The bar uses a subtle 1px bottom hairline in scrolled state.

**`nav-bar-transparent`** — The overlay variant used on collection and product landing pages where full-bleed imagery extends to the top edge. White text ensures legibility over dark lifestyle photography.

### Product Display

**`product-card`** — A borderless, square-cornered container with a 4:3 image ratio and light gray (#f5f5f5) background. Product name appears in serif type (`{typography.product-name}`), with collection/material subtitle in muted caption below. On hover, the card lifts 2px with a smooth 300ms ease transition — no shadow, just spatial shift.

**`image-gallery`** — Product detail pages use a vertical thumbnail strip (64px squares) alongside a large primary image. Active thumbnail gets a 2px amber border; all others show transparent borders. No rounded corners on images — everything is architectural.

**`configurator-panel`** — A right-aligned panel on product pages allowing material, finish, and dimension selection. Warm canvas background (#fbfaf9) with a left border separating it from the image area. Options are listed vertically with subtle bottom hairlines between them.

**`material-swatch`** — Circular swatches (32px diameter) representing fabric, teak, or metal finish options. Selected state shows a 2px amber border; unselected uses the warm hairline color. A caption label below identifies the material name.

### Content Sections

**`hero-section`** — Full-viewport lifestyle imagery with a subtle gradient overlay (20% to 50% opacity dark) ensuring text legibility. Display type at 56px light-weight serif centers vertically. A caption-uppercase kicker line in sand-light sits above the main title. Minimum height is 90vh.

**`collection-banner`** — A warm-tinted section (#f5eee5 background) used to introduce product collections. Display-md serif heading with generous padding. These banners break up the product grid rhythm.

**`collection-badge`** — Small uppercase tags in muted sand tones (#cec9c0 background, #342f28 text) that label product categories or material types. Minimal radius at `{rounded.xs}`.

### Utility

**`search-overlay`** — A full-screen dark overlay (85% opacity #121212 with 8px blur) that presents a large serif input field with a 2px amber bottom border. Search suggestions appear in on-dark text below.

**`breadcrumb`** — A minimal path indicator in caption-size type, using muted gray for ancestor links and ink for the current page. Separator is a simple hairline-colored slash.

### Footer

**`footer`** — Deep earth background (#342f28) with sand-light text. Organized in a 4-column grid on desktop collapsing to accordion on mobile. Heading labels are uppercase caption-style in white; links are sand-mid warming to white on hover. Generous vertical padding (96px top/bottom) treats the footer as a proper section rather than an afterthought.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero type drops to `{typography.display-md}`; nav collapses to hamburger + logo + search icon; configurator panel stacks below image; footer columns become accordions; section spacing reduces to `{spacing.xl}` |
| Tablet | 744–1128px | 2-column product grid; hero type at `{typography.display-lg}`; nav remains collapsed; configurator panel sits below gallery in a full-width drawer; collection banners reduce min-height |
| Desktop | 1128–1440px | 3-column product grid; full horizontal nav visible; configurator panel as right sidebar; hero at full `{typography.display-xl}`; footer in 4-column layout |
| Wide | > 1440px | Content max-width caps at 1440px with centered alignment; product grid may expand to 4 columns; increased section spacing at `{spacing.section-xl}`; hero imagery extends full bleed while text container remains capped |

### Touch Targets

- All interactive elements maintain 48px minimum touch target on mobile
- Material swatches expand to 44px on touch devices with increased gap spacing
- Navigation hamburger icon has a 48×48px tap area
- Card tap targets extend to the full card surface area, not just the text

### Collapsing Strategy

- Navigation collapses at 1024px to a hamburger slide-out panel with full-height dark overlay
- Product grid reduces columns at each breakpoint: 4 → 3 → 2 → 1
- Configurator panel transitions from sidebar to below-image stack at tablet breakpoint
- Footer columns collapse to expandable accordions with `{spacing.md}` between sections
- Hero caption + subtitle hide on mobile, leaving only the primary headline
- Image gallery thumbnails move from vertical side strip to horizontal scroll beneath the main image on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font-family names could not be extracted — the site uses Next.js font optimization with hashed class names (`__fontPrimary_ca2ea3`, `__fontSecondary_af2e54`). Georgia and Arial are listed as fallbacks in the font stacks, suggesting a serif display face and a geometric sans-serif body face, but the primary loaded typefaces remain unidentified.
- No meta theme-color was set, so mobile browser chrome color is unknown.
- Interaction animations (easing curves, durations for page transitions, parallax scroll behavior on hero imagery) were not captured in the extraction.
- Exact breakpoint values are inferred from common patterns — the site may use different thresholds.
- Icon system details (stroke width, grid size, icon library) are not available from the extraction.
- Form validation states (error colors, success indicators) are not represented in the extracted palette — the site may use a red/green pair not captured.
- Exact shadow values for elevated elements (dropdowns, modals) were not extracted.
