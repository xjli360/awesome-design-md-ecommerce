---
version: alpha
name: "Suzanne Kalan"
source_url: "https://www.suzannekalan.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Sage green — not gold, not ivory, not the expected cold white of a diamond case — is where Suzanne Kalan plants her chromatic flag: #aaccaa, a mint that reads as living and botanical rather than metallic. This choice alone marks the departure. Against a warm cream canvas (#ebe5dc), the sage carries a kind of garden vitality, suggesting these pieces belong in daylight, worn rather than stored behind glass. Deep aubergine navy (#1b1e2f) takes the weight of all primary text and headlines — not flat black but something with hue, something that shifts under light — while terracotta coral (#d77e6a) punctuates in select moments, the color of a stone's interior warmth or late afternoon sun catching a facet edge.

  Type moves through classic serifs. Baskerville and Apple Garamond establish editorial seriousness across display headers and product titles, with Source Serif Pro as the web-safe fallback — each cut chosen for fine strokes that hold at small sizes without collapsing. Figtree, a contemporary geometric sans, handles UI labels, form elements, and caption text; the pairing keeps navigation readable without competing with jewelry photography. Button copy runs uppercase at 0.08em letter-spacing, formal enough to signal premium without becoming stiff.

  Surfaces layer deliberately: warm near-white (#f5f5f5) underpins page background, stepping into cream (#ebe5dc) for featured collection panels, so gemstone photography reads luminous and warm rather than clinical. Corner radii stay restrained — `{rounded.xs}` for buttons, `{rounded.sm}` for inputs and cards, `{rounded.md}` for label chips — a geometry that suggests craft and precision rather than soft consumer casualness. The footer inverts to deep navy (#1b1e2f) with warm cream on-dark text, anchoring the scroll without the shock of pure black. Across every surface, the interaction palette resolves to sage primary, making the brand's unusual color choice a reliable functional signal rather than decoration alone.

colors:
  primary: "#aaccaa"
  primary-active: "#8aaa8a"
  primary-disabled: "#c8ddc8"
  terracotta: "#d77e6a"
  alert: "#e14a1c"
  ink: "#1b1e2f"
  body: "#262626"
  muted: "#7c7c7c"
  hairline: "#dedede"
  hairline-soft: "#e1e3e4"
  canvas: "#ebe5dc"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#1b1e2f"
  on-dark: "#ebe5dc"

typography:
  display-xl:
    fontFamily: "'Baskerville', 'Apple Garamond', 'Source Serif Pro', 'Iowan Old Style', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.02em
  display-md:
    fontFamily: "'Baskerville', 'Apple Garamond', 'Source Serif Pro', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'Baskerville', 'Apple Garamond', 'Source Serif Pro', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  price-display:
    fontFamily: "'Baskerville', 'Apple Garamond', 'Source Serif Pro', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  label-sm:
    fontFamily: "'Figtree', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-md:
    fontFamily: "'Figtree', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Figtree', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.06em

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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 8px 0
    borderBottom: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1 / 1"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 80vh
    overlayScrim: "rgba(27, 30, 47, 0.15)"
  gemstone-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: 4px 10px
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    textAlign: center
  pdp-price:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
    saleColor: "{colors.terracotta}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    backdropColor: "rgba(27, 30, 47, 0.4)"
  product-gallery:
    backgroundColor: "{colors.surface-soft}"
    thumbnailBorder: "2px solid transparent"
    thumbnailBorderActive: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    gap: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline-soft}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-sm}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Sage green (#aaccaa) fill with deep navy text via `{typography.button-md}` (uppercase, 0.08em spacing), 48px tall with `{rounded.xs}` edges. On hover the fill steps to `{colors.primary-active}` (#8aaa8a); disabled state uses `{colors.primary-disabled}` with `{colors.muted}` text and pointer-events none. The uppercase letter-spacing gives a formal jeweler's counter feel without needing a border.

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` border, same height and type as primary. On hover, background fills to `{colors.surface-soft}` at low opacity. Communicates equal weight to primary without the sage signal, used for secondary actions like "View Details" or "Add to Wishlist."

**`button-ghost`** — Transparent with no border, only a 1px `{colors.ink}` bottom underline, carrying `{typography.button-md}`. Used inline within editorial content and collection intros where a full button block would be visually heavy.

### Text Input

**`text-input`** — `{colors.surface-soft}` background with a 1px `{colors.hairline}` border, sharpening to `{colors.ink}` on focus. `{rounded.sm}` corners, 48px height, body text in `{typography.body-md}`. Placeholder rendered in `{colors.muted}`. Error state swaps border to `{colors.alert}` (#e14a1c). The warm off-white fill keeps form fields from floating as bright white boxes against the cream canvas.

### Navigation

**`nav-bar`** — 72px tall, `{colors.canvas}` background with a subtle `{colors.hairline-soft}` bottom border. Links in `{typography.nav-link}` (Figtree, 13px, 0.06em spacing) against `{colors.ink}`. Logo centered or left-aligned at larger sizes. Utility icons (search, bag, account) right-aligned at 40px touch targets. On scroll past the hero, the nav gains a subtle drop shadow at 4px blur; background stays cream, not white.

### Product Card

**`product-card`** — Square-crop image at 1:1 aspect ratio on a `{colors.surface-soft}` slab with `{rounded.sm}` corners. Title in `{typography.title-md}` (Baskerville, 18px) below the image; price in `{typography.price-display}` (Baskerville, 22px); material or stone descriptor in `{typography.caption}` with `{colors.muted}` text. On hover, the image scales to 1.03× over 300ms ease-out; no overlay or text reveal. Spacing uses `{spacing.base}` padding with `{spacing.sm}` gap between title and price.

### Hero Banner

**`hero-banner`** — Full-bleed image with a `rgba(27, 30, 47, 0.15)` scrim so headline text in `{typography.display-xl}` (Baskerville, 48px, 400 weight) reads against dark and light photography alike. Sub-copy in `{typography.body-md}`. Minimum 80vh height; CTA button (`button-primary`) centered at the lower third. On mobile, min-height drops to 60vh and display type scales to 32px.

### Gemstone Badge

**`gemstone-badge`** — Small label chips for cut, metal, stone type, or collection membership. `{colors.surface-soft}` fill with a 1px `{colors.hairline}` border, `{rounded.md}` corners (12px), and `{typography.label-sm}` (Figtree 11px uppercase, 0.1em spacing). These appear in PDP below the product title as a horizontal stack; they scroll horizontally on mobile rather than wrapping.

### Collection Header

**`collection-header`** — Centered editorial block on `{colors.canvas}`, headline in `{typography.display-md}`, body paragraph in `{typography.body-md}`. `{spacing.section}` vertical padding top and bottom. An optional terracotta rule (2px, `{colors.terracotta}`, 40px wide) may sit between headline and body as a typographic divider.

### PDP Price

**`pdp-price`** — Price in `{typography.price-display}` (Baskerville 22px) at `{colors.ink}`. When a sale price is present, original price renders in `{colors.muted}` with strikethrough at `{typography.body-sm}`, and the sale price picks up `{colors.terracotta}` to signal reduction without urgency-red alarm.

### Search Overlay

**`search-overlay`** — Full-viewport overlay at `rgba(27, 30, 47, 0.4)` scrim behind a centered white input panel with `{colors.canvas}` background. Input rendered at `{typography.body-md}`, `{rounded.sm}`, 1px `{colors.hairline}` border. Results appear as a scrollable list with `{typography.title-md}` product names and `{typography.caption}` category labels. Closes on ESC or backdrop click.

### Footer

**`footer`** — Full-width `{colors.ink}` (#1b1e2f) slab with `{colors.on-dark}` (#ebe5dc) text and `{colors.hairline-soft}` links. Column labels in `{typography.label-sm}` (uppercase, 0.1em spacing); body links in `{typography.body-sm}`. `{spacing.section}` vertical padding. Newsletter input reverses to a light border-only field against the dark background, swapping `{colors.surface-soft}` fill for transparent with a `{colors.hairline}` border.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo; hero min-height 60vh; display-xl scales to 32px; gemstone badges scroll horizontally; add-to-cart button full-width |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links but hides subcategories behind hover flyout; hero 70vh; collection headers reduce padding to `{spacing.xl}` |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with flyout mega-menu; hero 80vh; collection headers restore `{spacing.section}` padding |
| Wide | > 1440px | Max content width 1440px centered; hero image extends full bleed beyond content column; side whitespace renders in `{colors.canvas}` |

### Touch Targets

- All interactive elements minimum 44×44px on mobile
- Gemstone badge chips minimum 36px tall for thumb tap
- Nav hamburger icon 44×44px tap target
- Quantity stepper buttons minimum 44×44px each
- Thumbnail gallery items minimum 64×64px

### Collapsing Strategy

- Top nav collapses: logo centers, hamburger left, bag/search icons right
- Mega-menu flyouts become full-screen slide-in drawers on mobile
- PDP layout stacks gallery above title/price/CTA (no side-by-side below 744px)
- Footer columns collapse from four-across to two-column at tablet, single-column at mobile
- Collection header text-align shifts from center to left on mobile for legibility at narrow widths
- Breadcrumb truncates to first and last segment with ellipsis on mobile

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed brand typeface name beyond system serif stacks; Baskerville and Apple Garamond appear in font-family declarations but a custom or licensed display face (e.g., a proprietary serif or script) may exist that is loaded via JavaScript and not captured in static extraction
- Muted text color (#7c7c7c) is derived, not extracted; no mid-gray utility tone appeared in the top hex list
- Primary-active (#8aaa8a) and primary-disabled (#c8ddc8) are derived from the sage primary; actual hover/disabled states from Shopify theme customization were not captured
- No confirmed icon style (line weight, filled vs. outline, stroke width) extracted — fine jewelry typically uses thin 1px stroke icons
- Animation timing and easing curves not captured; transitions above are inferred from luxury e-commerce norms
- No confirmed grid column count or max-width container token from the Shopify theme config
- The #5873f9 blue in extracted colors appears to be a Shopify framework UI artifact (focus ring or third-party widget) rather than a brand color — excluded from the palette intentionally
