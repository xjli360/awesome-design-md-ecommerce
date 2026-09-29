---
version: alpha
name: "Esker Beauty"
source_url: "https://eskerbeauty.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Big Caslon Reg set against cream-washed linen fields announces the Esker proposition before a single product name loads — this brand communicates through background warmth rather than clinical white. The canvas oscillates between #faf6f1 and #f0ede2, two off-whites close enough to read as a single tone but distinct enough to separate sections without hard dividers, creating depth through temperature rather than contrast. Against this ground, charcoal type (#474747 for body, #121212 for display) reads with authority but without the harshness of pure black, and the palette's single genuinely chromatic accent — clay-brown #6b6158 — lands on CTAs and hover states as a color that belongs to pressed earth rather than a brand guidelines document. The type pairing is precise and slightly eccentric: Big Caslon Reg handles all editorial headlines and product names with classical high-contrast serif strokes, while Roboto runs every UI element with the neutral legibility of a service typeface. The combination feels like a handwritten field journal sitting beside a pharmaceutical reference label. A faint sage-gray (#b0b8b6) marks interactive borders and secondary UI without competing with the warmth of the dominant palette. Rounded corners are nearly absent — the brand lives in sharp or barely chamfered rectangles, with `{rounded.xs}` appearing only on inputs and small badges, refusing the soft-pill idiom of mainstream beauty e-commerce. Spacing is expansive; sections breathe at `{spacing.section}` (64px) or wider, and product cards rest in generous isolation so each object reads as a considered thing rather than a tile in a revenue-optimized grid. The overall rhythm is slow and editorial, consistent with a brand that names its line "Intentional Body Care" — every layout decision argues that unhurried attention is itself a form of care.

colors:
  primary: "#6b6158"
  primary-active: "#504840"
  primary-disabled: "#b0a89e"
  ink: "#121212"
  body: "#474747"
  muted: "#6b6b6b"
  muted-soft: "#888888"
  hairline: "#dedede"
  hairline-soft: "#f0ede2"
  canvas: "#faf6f1"
  surface-soft: "#f0ede2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sage-mist: "#b0b8b6"

typography:
  display-xl:
    fontFamily: "'Big Caslon Reg', 'Big Caslon', Georgia, serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Big Caslon Reg', 'Big Caslon', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Big Caslon Reg', 'Big Caslon', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.03em
  body-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  label-uppercase:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  price-display:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    states:
      hover:
        backgroundColor: "{colors.primary-active}"
      disabled:
        backgroundColor: "{colors.primary-disabled}"
        textColor: "{colors.on-primary}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.body}"
    padding: 13px 27px
    height: 48px
    states:
      hover:
        borderColor: "{colors.primary}"
        textColor: "{colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    states:
      focus:
        borderColor: "{colors.primary}"
        outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-sm}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    height: 36px
    letterSpacing: 0.08em
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspectRatio: "4/5"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
    titleTypography: "{typography.display-sm}"
    subtitleTypography: "{typography.body-sm}"
    subtitleColor: "{colors.muted}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.body}"
    states:
      hover:
        border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
    ctaSpacing: "{spacing.lg}"
    overlayColor: "rgba(71, 71, 71, 0.08)"
    layout: split-text-image or full-bleed with scrim overlay
  ingredient-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 6px 12px
  ritual-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    stepNumberTypography: "{typography.display-xl}"
    stepNumberColor: "{colors.hairline}"
    layout: horizontal-steps on desktop, vertical-stack on mobile
  collection-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.xl}"
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    starColor: "{colors.primary}"
    authorTypography: "{typography.title-sm}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headlineTypography: "{typography.label-uppercase}"
    linkTypography: "{typography.body-sm}"
    legalTypography: "{typography.caption}"
    legalColor: "{colors.muted}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — A 4px-radius rectangle (`{rounded.xs}`) filled with clay-brown #6b6158, carrying uppercase Roboto at `{typography.button-md}` (14px, 0.08em tracking) in white. The matte earth tone and sharp geometry deliberately contrast with the glossy high-radius CTAs common in beauty e-commerce. Hover darkens to #504840 (`{colors.primary-active}`); disabled fades to #b0a89e (`{colors.primary-disabled}`) while preserving white text. No shadows, no gradients — the button reads as a label, not a jewel.

**`button-secondary`** — Transparent fill, 1px border in `{colors.body}` charcoal (#474747), same 48px height and `{rounded.xs}` radius as primary. Hover transitions border and text color to `{colors.primary}` clay-brown, surfacing the brand accent without a fill. Used for secondary actions — "View All", "Learn More" — where the primary CTA already anchors the hierarchy.

**`button-ghost`** — No border, no fill; underlined uppercase Roboto in `{colors.ink}`. Appears inline within editorial copy and hero modules where a bordered button would add visual clutter. Functions as a link with button semantics.

### Text Input

**`text-input`** — `{colors.canvas}` (#faf6f1) background with a 1px `{colors.hairline}` border and `{rounded.xs}` radius. Roboto 16px (`{typography.body-md}`) for entered text; `{colors.muted}` for placeholder. On focus, the border swaps to `{colors.primary}` clay-brown — the only focus indicator color on the page. Used across email capture, site search, and checkout fields.

### Navigation

**`nav-bar`** — 64px tall on a `{colors.canvas}` background, grounded by a 1px `{colors.hairline}` bottom rule. The wordmark renders in `{typography.display-sm}` Big Caslon — the one serif intrusion into the utility layer — while all nav links run in `{typography.nav-link}` Roboto (13px, 0.04em tracking). Cart, account, and search sit right-aligned at 24px icon size with 44px tap targets. No mega-menu drop shadows; sub-navigation appears in a flat panel in `{colors.surface-soft}`.

**`announcement-bar`** — A 36px strip in `{colors.surface-soft}` (#f0ede2) above the nav. Roboto caption with 0.08em letter-spacing rotates promotional messages in `{colors.body}` charcoal. No close button on desktop; collapsible on mobile.

### Product Card

**`product-card`** — Square-cornered (`{rounded.none}`) on a white ground (`{colors.surface-card}`). Product image fills a 4:5 frame to card edge with no padding; on hover, a 1px `{colors.hairline}` border traces the card perimeter — the hover state is that subtle. Product name renders in `{typography.display-sm}` Big Caslon (24px serif) to preserve the editorial voice all the way into the grid. Variant or size note falls to `{typography.body-sm}` Roboto in `{colors.muted}`. Price in `{typography.price-display}` Roboto at `{colors.body}`. No badge overlays on the image by default.

### Hero

**`hero`** — Full-width section in `{colors.surface-soft}` cream, or full-bleed photography with a translucent 8% charcoal scrim. Headline in `{typography.display-xl}` Big Caslon (52px, -0.5px tracking) at maximum editorial scale. Body copy in `{typography.body-md}` Roboto with 1.6 line-height. A single `button-primary` CTA sits `{spacing.lg}` below the body. On split layouts, the text column occupies the left half at `{spacing.section}` vertical padding; the image fills the right half edge-to-edge.

### Ingredient Badge

**`ingredient-badge`** — A flat zero-radius label (`{rounded.none}`) with 1px `{colors.hairline}` border, `{colors.surface-soft}` fill, and uppercase Roboto at `{typography.label-uppercase}` (11px, 0.12em tracking) in `{colors.muted}`. Called out on PDPs and editorial sections to name key actives ("Salicylic Acid", "Sea Kelp", "Jojoba Oil"). Intentionally recessive — these are identifiers, not marketing exclamation points.

### Ritual Strip

**`ritual-strip`** — An editorial section presenting a multi-step body-care routine. Step numbers render in `{typography.display-xl}` Big Caslon at `{colors.hairline}` gray — oversized and ghosted, functioning as graphic texture rather than read copy. Step names below in `{typography.display-md}`, descriptions in `{typography.body-md}`. Section uses `{spacing.section}` top/bottom padding on `{colors.surface-soft}`. Steps read as a horizontal row on desktop; collapse to a vertical stack on mobile.

### Collection Banner

**`collection-banner`** — A full-width color-break block in `{colors.primary}` (#6b6158) clay-brown with `{colors.on-primary}` white type. Headline in `{typography.display-md}` Big Caslon, body in `{typography.body-md}` Roboto. Sharp corners (`{rounded.none}`), full viewport width. Placed between category sections as a tonal reset and CTA anchor; the only moment in the layout where the brand's primary accent covers the full canvas.

### Review Card

**`review-card`** — White card (`{colors.surface-card}`) with 1px `{colors.hairline}` border and no radius. Star rating in `{colors.primary}` clay-brown SVG fills. Review body in `{typography.body-sm}` Roboto at `{colors.ink}`; author name in `{typography.title-sm}` medium weight. Cards sit in a horizontal scroll rail on mobile, a 3-column grid on desktop. No rounded corners, no elevation — the cards read as document fragments, not UI widgets.

### Footer

**`footer`** — `{colors.surface-soft}` (#f0ede2) background separated from the main content by a 1px `{colors.hairline}` rule. Column heads in `{typography.label-uppercase}` Roboto uppercase at `{colors.ink}`; links in `{typography.body-sm}` Roboto at `{colors.body}`. Legal copy and copyright in `{typography.caption}` at `{colors.muted}`. `{spacing.section}` top padding; the footer stays in the warm-cream register without inverting to a dark or charcoal ground.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; product grid drops to 2 columns; hero stacks text above image, image runs full-bleed; nav collapses to hamburger + wordmark; announcement bar gains optional dismiss; ritual-strip becomes vertical stack |
| Tablet | 744–1128px | 2–3 column product grid; hero maintains split layout at reduced padding; nav shows primary categories, secondary links fold into overflow menu |
| Desktop | 1128–1440px | 3–4 column product grid; hero at full split or full-bleed; nav fully expanded with all category links; ingredient badges display inline with PDP imagery |
| Wide | > 1440px | Content constrained to ~1400px max-width with auto margins; hero image extends to full viewport while text column stays within grid; product grid caps at 4 columns |

### Touch Targets

- All buttons minimum 48px height on mobile
- Nav icons (cart, account, search) minimum 44×44px tap area regardless of icon render size
- Full product card is a link target, not only the title — entire image and text block activates navigation to PDP
- Ingredient badges are non-interactive by default; minimum 36px height if made tappable for ingredient detail overlays

### Collapsing Strategy

- Navigation: full horizontal bar → hamburger drawer at < 744px; drawer slides from left over `{colors.surface-soft}` with `{typography.display-sm}` Big Caslon section headings inside
- Product grid: 4 → 3 → 2 → 2 → 1 column stepping from Wide to Mobile at each breakpoint
- Hero: side-by-side 50/50 split → stacked text-above-image at Mobile; image becomes 100vw full-bleed with `{spacing.section}` top padding on text
- Ritual strip: horizontal row of numbered steps → vertical accordion or stacked cards at Mobile
- Footer: 4-column grid → 2-column at Tablet → single-column accordion at Mobile with each section collapsible

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No explicit primary-active (#504840) or primary-disabled (#b0a89e) values extracted; both are derived by lightening and darkening #6b6158 — verify against live interactive state screenshots before finalizing
- surface-card white (#ffffff) inferred from Shopify platform defaults and the meta theme-color declaration; not extracted as a distinct named brand token
- Big Caslon Reg loaded with `!important` overrides in multiple variant spellings, suggesting dynamic or JS-injected font loading that obscures exact weight axes; weight 400 assumed from the "Reg" suffix but heavier weights for emphasis may exist
- Manuale (serif) was found in the font stack extraction but no clear component assignment could be identified; may serve pull-quote, editorial aside, or secondary headline contexts — further PDP and editorial template audit needed
- No box-shadow or elevation tokens extracted; flat design assumed throughout, but confirmation against interactive components (dropdowns, drawers, modals) is recommended
- Exact CSS breakpoint pixel values not extractable from static analysis; responsive table uses Shopify default grid conventions and should be validated against theme CSS
- Hover and active transition durations and easing functions not recoverable from extraction
- No dark mode, high-contrast mode, or reduced-motion variants detected
