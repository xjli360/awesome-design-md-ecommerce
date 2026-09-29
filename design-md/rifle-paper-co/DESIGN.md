---
version: alpha
name: "Rifle Paper Co."
source_url: "https://riflepaperco.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Berthold Baskerville Pro set at display scale in near-black (#272727) on pale canvas opens every Rifle Paper Co. editorial moment — it reads less like a website headline than like the title page of a hardcover stationery catalog, and that confusion is intentional. The brand's structural anchor is deep forest green (#214232), which carries primary CTAs and the brand mark with the permanence of pressed botanicals, while lighter greens (#3f533a, #c2caac, #a6b3ad) layer outward like growth rings, softer with each step; below the structural greens the palette branches into seasonal keys — warm rust (#d6381d) marks promotions and urgency, soft periwinkle (#899df1) carries collectible and gift contexts, deep teal (#0e7a82) surfaces for special-edition runs, each hue distinct enough that a returning customer reads the seasonal story before reading the copy. Navigation sits in a sage (#c2caac) announcement band above the logo, with nav links set in Nautica uppercase at generous letter-spacing — deliberately keeping wayfinding words secondary to illustration; product card surfaces rest on near-white (#f4f4f6, {colors.surface-soft}), framed by hairline borders (#dedede) so thin they read more as a breath than a boundary. Corners are restrained throughout — buttons take {rounded.xs}, product cards stay {rounded.none} — because the brand's physical goods are paper-edged rectangles and the UI reflects that without needing to say so. The footer drops to deep navy (#272d45), a chromatic register shift that closes the page the way a dark endpaper closes a hardcover; footnote links retire to muted lavender-gray (#676986). The cream wash (#ffebb4) appears as illustration background rather than UI surface, a reminder that the illustration is the product and the interface is the frame, while Baskerville body copy at 16px and 1.6 line height gives those illustrations room to breathe, and price points appear in the same serif at 18px weight-400 — no bolding, no color signal — because value in this brand registers through restraint, not emphasis.

colors:
  primary: "#214232"
  primary-active: "#1d3a2c"
  primary-disabled: "#a6b3ad"
  primary-accent: "#3f533a"
  ink: "#272727"
  body: "#272727"
  muted: "#616161"
  muted-soft: "#9a9db1"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f4f4f6"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  accent-sage: "#c2caac"
  accent-lavender: "#676986"
  accent-periwinkle: "#899df1"
  accent-red: "#d6381d"
  accent-teal: "#0e7a82"
  accent-cream: "#ffebb4"
  accent-tan: "#867456"
  footer-bg: "#272d45"

typography:
  display-xl:
    fontFamily: "'berthold-baskerville-pro', 'Baskerville', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'berthold-baskerville-pro', 'Baskerville', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'berthold-baskerville-pro', 'Baskerville', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'berthold-baskerville-pro', 'Baskerville', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'nautica', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'nautica', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.4px
  body-md:
    fontFamily: "'berthold-baskerville-pro', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'berthold-baskerville-pro', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'nautica', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'nautica', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'nautica', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'nautica', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'berthold-baskerville-pro', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'nautica', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  collection-label:
    fontFamily: "'nautica', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  link:
    fontFamily: "'berthold-baskerville-pro', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline

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
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
    border: "1.5px solid {colors.primary}"
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
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 42px
    focusBorder: "1px solid {colors.primary}"
  announcement-bar:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
    letterSpacing: 0.5px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
    dropdownBg: "{colors.canvas}"
    dropdownBorder: "1px solid {colors.hairline}"
    dropdownShadow: none
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    nameTypography: "{typography.body-sm}"
    labelTypography: "{typography.collection-label}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    imageBg: "{colors.surface-soft}"
    padding: "{spacing.md}"
    gap: "{spacing.sm}"
    hoverImageTranslate: -2px
  collection-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  collection-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    overlayColor: "rgba(255,255,255,0.55)"
    ctaComponent: button-primary
    minHeight: 580px
    padding: "{spacing.section} {spacing.xxl}"
  editorial-hero:
    backgroundColor: "{colors.accent-cream}"
    textColor: "{colors.primary}"
    headlineTypography: "{typography.display-lg}"
    subheadTypography: "{typography.title-md}"
    layout: two-column
    illustrationSide: right
    maxWidth: 1440px
    padding: "{spacing.section} {spacing.xxl}"
  illustration-tile:
    backgroundColor: "{colors.accent-cream}"
    labelTypography: "{typography.collection-label}"
    labelColor: "{colors.muted}"
    headlineTypography: "{typography.display-md}"
    headlineColor: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl}"
    hoverIllustrationScale: 1.02
  search-drawer:
    backgroundColor: "{colors.canvas}"
    overlayColor: "rgba(39,39,39,0.4)"
    inputTypography: "{typography.display-sm}"
    inputBorderBottom: "1px solid {colors.hairline}"
    inputBorderOther: none
    textColor: "{colors.ink}"
    resultLabelTypography: "{typography.collection-label}"
    padding: "{spacing.xl}"
  gift-wrap-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.hairline-soft}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-primary}"
    newsletterInputBg: "rgba(255,255,255,0.1)"
    newsletterInputBorder: "1px solid rgba(255,255,255,0.25)"
    newsletterInputRadius: "{rounded.xs}"
    legalTypography: "{typography.caption}"
    legalColor: "{colors.muted-soft}"
    dividerColor: "rgba(255,255,255,0.1)"
    padding: "{spacing.xxl}"
    columns: 4

---

## Components

### Buttons

**`button-primary`** — Forest-green (#214232) fill, white Nautica uppercase at 13px/1px letter-spacing, 4px corner radius, 44px height. Hover and press states shift to #1d3a2c — a darkening that reads as shadow falling over a leaf rather than an explicit affordance signal. Disabled state uses muted sage (#a6b3ad) at 60% opacity; the button remains visible but recedes. No box shadow at any state; the button is flat the way a stamp block is flat.

**`button-secondary`** — Canvas background with a 1.5px forest-green border and matching green Nautica text, forming the hollow counterpart to `button-primary`. Maintains identical height and typography so the two sit side by side without disrupting the grid. Border weight drops to 1px on hover, shifting the emphasis inward rather than adding color.

**`button-ghost`** — Transparent background, ink-colored Nautica body-sm text replaced by underline. Used for back-navigation, editorial "Read More" links, and secondary actions on illustrated layouts where a bordered button would compete with the art. Minimum touch height 44px via invisible vertical padding.

### Inputs

**`text-input`** — Single-pixel hairline (#dedede) border, canvas fill, Baskerville body-md at 16px. Focus replaces the hairline with forest green at the same 1px weight — the shift is subtle, barely louder than the resting state. Placeholder text runs in muted-soft (#9a9db1). Corner radius `{rounded.xs}` keeps the form element consistent with the brand's paper-rectangle vernacular.

### Navigation

**`nav-bar`** — 64px height, canvas background, 1px hairline bottom border. The forest-green logo anchors left or center depending on breakpoint. Nav links run in Nautica uppercase at 13px and 0.8px letter-spacing, keeping wayfinding secondary to illustration. Dropdowns open against canvas with hairline borders and no shadow; the page behind dims to a 20% dark overlay without blur. The `announcement-bar` sits directly above, 36px in sage (#c2caac) with primary-green text — a botanical ground layer before the main surface begins.

**`announcement-bar`** — Full-width 36px bar in sage (#c2caac), centered Nautica caption text set in forest green. Carries free-shipping thresholds, collection launch dates, and promotional windows. No dismiss control — it reads as environmental signal rather than interruptive notification.

### Product Cards

**`product-card`** — Flat, rectangular, zero rounding. Top zone is the illustration image on surface-soft (#f4f4f6); below sits the collection label in Nautica 11px/1.5px-tracking uppercase (muted gray), product name in Baskerville body-sm, then price in Baskerville price-display at 18px/400 weight with no color differentiation. A hairline-soft border surrounds the card; no shadow. Hover animates the illustration up 2px with no card-level lift — the product moves, the frame does not. `collection-badge` and `collection-badge-sale` position absolute top-left over the image.

**`collection-badge`** — Flat rectangle (`{rounded.none}`), forest green for NEW arrivals, warm rust (#d6381d) for SALE. Nautica badge typography at 10px/1px tracking uppercase, 3px×8px padding. The sharp edges are deliberate — they read as printed sticker or price tag, consistent with the stationery context.

### Hero & Editorial

**`hero`** — Full-bleed editorial image with a white overlay (rgba 0.55) letting illustration breathe through the headline. Baskerville display-xl at 48px/400 weight — not a heavy hero; the type asserts itself without competing with photography. Primary CTA button sits below. Minimum height 580px; the image always earns more vertical space than the copy stack.

**`editorial-hero`** — Two-column desktop layout: illustration right, editorial copy left on pale cream (#ffebb4) background. Headline in Baskerville display-lg, subhead in Nautica title-md in primary green. This component carries the most concentrated brand voice and appears for seasonal collection launches, gift guides, and collaboration features. On mobile it stacks to image-above, copy-below with the image cropped to 4:3.

**`illustration-tile`** — Square or near-square tile on cream (#ffebb4), centered illustration, collection label in Nautica uppercase beneath, headline in Baskerville display-md in forest green above or below depending on composition. Used in category landing grids ("Shop Notebooks", "Shop Calendars"). Hover scales the illustration to 1.02; the tile container stays fixed.

### Overlays & Drawers

**`search-drawer`** — Full-width panel descending from the nav. Canvas background, no rounding. Search input rendered at display-sm scale (22px Baskerville), with only a bottom-border hairline — no input box outline. Results group under Nautica collection-label headings ("Products", "Collections"). Behind the drawer, a rgba(39,39,39,0.4) overlay dims the page without blur. No slide animation easing beyond a simple 200ms ease-out.

### Specialty

**`gift-wrap-callout`** — Narrow inline banner in surface-soft (#f4f4f6) with a forest-green icon at left, Baskerville body-sm copy, and a ghost-style underline link. Appears on product detail pages and cart to surface gift-wrapping service. 8px corner radius (`{rounded.sm}`) — the one context where rounding appears without the brand's usual rectangular discipline, softening a service callout rather than a product representation.

### Footer

**`footer`** — Full-width deep navy (#272d45) block. Four columns on desktop: brand bio left, three link columns (Shop, Company, Help). Link text in hairline-soft (#e5e5e5) Baskerville body-sm; column heads in Nautica title-sm white. Newsletter subscription row at bottom: a low-opacity white-field input with white-alpha border, beside a forest-green `button-primary`. Social links render as icon-only at 24px in white. Fine-print legal copy drops to muted-soft (#9a9db1) caption scale. The navy registers as a complete color break from the page — a clean closure, not a continuation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Two-column product grid (portrait); hamburger nav with full-screen green-header drawer; hero min-height 380px; display-xl drops to 28px; footer collapses to touch-accordion link groups; announcement-bar wraps to two lines |
| Tablet | 744–1128px | Two-to-three column product grid; nav collapses to icon-only with drop-drawer; editorial-hero stacks vertically image-above; footer reduces to two columns |
| Desktop | 1128–1440px | Four-column product grid; full horizontal nav with mega-menu dropdowns; editorial-hero two-column active; footer four-column layout |
| Wide | > 1440px | 1440px max-width container centered on page; gutters expand symmetrically; hero image extends edge-to-edge behind the content container; grid stays four-column maximum |

### Touch Targets

- All nav links minimum 44px tap height via vertical padding extension — visible text is smaller
- Product card entire surface is the tap zone, not just image or title
- Ghost buttons receive 44px minimum height via invisible padding — underline text alone is too small to target reliably
- Announcement-bar link is the full bar height on mobile
- Footer accordion headers minimum 48px touch height with full-row tap zone
- Collection badges do not function as independent tap targets — the card surface handles the tap

### Collapsing Strategy

- Navigation collapses to hamburger below 1128px; drawer slides in from left, full-screen, forest-green header, white Nautica links stacked at 48px touch height, category icons optional
- Product grid: 4-column (desktop/wide) → 3-column (tablet landscape) → 2-column (tablet portrait / mobile) — single column avoided to preserve the catalog-browse feel
- Footer accordion on mobile: each column head becomes a tap-to-expand trigger; newsletter row remains full-width and always visible
- Editorial-hero stacks image-above on mobile with image cropped to 4:3; headline and CTA follow below on cream background
- Hero copy repositions to bottom-third overlay on mobile to avoid obscuring the focal illustration
- Search drawer narrows to full-width on mobile with input font reduced to display-sm (22px)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hero overlay opacity and blend mode not extractable from static extraction — rgba(255,255,255,0.55) is inferred from visual brightness of live site
- Whether Nautica is a proprietary Rifle Paper Co. typeface or a commercially licensed font could not be confirmed; fallback stack defaults to sans-serif
- No meta theme-color set; mobile browser chrome color on iOS/Android is unknown
- Mega-menu column count, imagery inclusion, and layout within desktop nav dropdowns not captured
- Product card hover micro-animation specifics (duration, easing, exact translate distance) are inferred — 2px upward translate at 200ms ease is an estimate
- Grid gutter widths and precise breakpoint column-count thresholds not extracted — Shopify default 24px gutters assumed
- Collection-specific roles for accent-periwinkle (#899df1) and accent-teal (#0e7a82) are inferred from color extraction frequency, not confirmed from specific UI placement
- Dark mode: no evidence of a dark mode variant detected; assumed light-only
- Icon set (navigation icons, social icons, UI affordance icons) not extractable — style assumed to match the hand-illustrated brand language but SVG details unknown
