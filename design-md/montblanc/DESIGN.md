---
version: alpha
name: "Montblanc"
source_url: "https://www.montblanc.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The eight-pointed Snowcap star pressed into every pen cap since 1913 sets the logic for an entire design system — a palette that refuses to compete with the object it frames. On screen the black deepens to near-true (#000000) against a white canvas (#ffffff), broken only by a champagne-gold accent (#c5a028) that surfaces at the brand mark, clip trim in product close-ups, and the rarest tier of CTA. The rest of the interface earns no color. Body copy settles at a slightly warm #1c1c1c rather than pure black, making product photography the mid-range tonal anchor; nothing decorative lives in this palette — every hue references something you can hold.

  Type runs on a refined, wide-tracked serif at display positions — 48–64px in weight 400 so letterform proportions breathe rather than press — paired with an uppercase geometric sans for navigation, buttons, and all functional labels. The contrast between a tall serif headline and a tightly-spaced 0.12em uppercase CTA below it captures the brand's core tension: ancien régime craft, contemporary retail directness. Buttons everywhere are sharp-cornered (`{rounded.none}`); no pill, no soft radius appears anywhere that might suggest approachability. The interaction vocabulary is architectural — the grid line, the ruled separator, the precise cut — which is why `{colors.hairline}` rules appear between content zones in addition to spatial gaps, referencing instrument-making tolerances rather than web convention.

  Product cards foreground the object on a white `{colors.surface-card}` ground with a 4:5 image ratio, the product name in the display serif, and price in unemphasized body weight directly below — Montblanc does not typographically foreground the number. Editorial sections alternate full-bleed dark zones carrying serif headlines against bright white product grids, a rhythm that recalls opening and closing a presentation box. A small "PERSONALISATION AVAILABLE" badge in `{colors.gold}` on key product cards signals the engraving service — the brand's most irreversible act of ownership — without requiring explanation.

colors:
  primary: "#000000"
  primary-active: "#2a2a2a"
  primary-disabled: "#8c8c8c"
  gold: "#c5a028"
  gold-light: "#e8d49a"
  ink: "#1c1c1c"
  body: "#3d3d3d"
  muted: "#767676"
  hairline: "#d4d0cc"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f3f0"
  surface-card: "#ffffff"
  surface-dark: "#111111"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-gold: "#000000"
  snowcap: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Montblanc Text', 'Didot', 'Playfair Display', Georgia, serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: 0.02em
  display-lg:
    fontFamily: "'Montblanc Text', 'Didot', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: 0.015em
  display-md:
    fontFamily: "'Montblanc Text', 'Didot', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: 0.01em
  display-sm:
    fontFamily: "'Montblanc Text', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.28
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.375
    letterSpacing: 0.08em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.10em
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.04em
  price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
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
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.06em
  editorial-kicker:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.15em
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
    borderWidth: 0
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.on-dark}"
  button-gold:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    borderWidth: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    placeholderColor: "{colors.muted}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottomWidth: 1px
    borderBottomColor: "{colors.hairline}"
    logoMaxWidth: 140px
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottomWidth: 0
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "4/5"
    padding: "{spacing.lg}"
    nameTypography: "{typography.display-sm}"
    nameColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.body}"
    hoverBoxShadow: "0 4px 24px rgba(0,0,0,0.08)"
    rounded: "{rounded.none}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    sublineColor: "{colors.on-dark}"
    minHeight: 640px
    contentPaddingVertical: "{spacing.xxl}"
    contentPaddingHorizontal: "{spacing.xl}"
  editorial-strip:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    kickerTypography: "{typography.editorial-kicker}"
    kickerColor: "{colors.gold}"
    headlineTypography: "{typography.display-md}"
    paddingVertical: "{spacing.section}"
  engraving-badge:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  snowcap-star:
    color: "{colors.snowcap}"
    defaultSize: 20px
    displaySize: 40px
  search-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.display-md}"
    inputBorderColor: "{colors.hairline}"
    overlayColor: "rgba(0,0,0,0.6)"
  collection-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
    borderWidth: 1px
    borderColor: "{colors.hairline}"
  footer-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.caption}"
    linkColor: "{colors.muted}"
    paddingVertical: "{spacing.xxl}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted}"
    activeColor: "{colors.ink}"

## Components

### Buttons

**`button-primary`** — A sharp-cornered (`{rounded.none}`) 48px black block in `{colors.primary}` with white uppercase spaced type, 0.12em tracking. Hover state transitions immediately to `{colors.primary-active}` (#2a2a2a) — no easing, no lift, no shadow. Disabled state renders `{colors.primary-disabled}` gray, which reads as inert architecture rather than a warning. The button never rounds.

**`button-secondary`** — 1px `{colors.primary}` border on a white canvas, identical height and type treatment as primary. Communicates "explore further" in contexts where the solid black reads "commit now." Use on light sections only; switch to `button-ghost` on dark backgrounds.

**`button-ghost`** — White 1px border and white text, transparent fill, for use atop `{colors.surface-dark}` hero sections and editorial strips. Matches the height and letterform rhythm of all other button variants — the only variable is ground color.

**`button-gold`** — `{colors.gold}` fill, `{colors.on-gold}` text. Reserved for engraving and personalisation service CTAs, heritage-edition product launches, and anniversary collection pages. Never used for general commerce actions; its appearance signals a tier above the standard catalogue.

### Navigation

**`nav-bar`** — 72px tall bar on white, separated from page content by a 1px `{colors.hairline}` rule. The Montblanc wordmark in SVG sits left-aligned; navigation items in `{typography.nav-link}` (0.06em tracked sans-serif) distribute across the remaining width. Mega-menus drop at the hairline boundary without shadow, bleeding edge-to-edge at full viewport width, and contain both category links and editorial imagery. Pages with full-bleed dark heroes switch to `nav-bar-dark`, which sits transparently over the dark field with white type.

### Product Card

**`product-card`** — No border, no resting shadow, `{colors.surface-card}` ground. Product name renders in `{typography.display-sm}` (24px serif, weight 400) — even short names get the display treatment. Price appears in `{typography.price}` (16px, weight 400) immediately below, with no color, size, or weight differentiation from body text. At hover, a diffuse shadow (`0 4px 24px rgba(0,0,0,0.08)`) lifts the card; corners stay square. An `engraving-badge` in `{colors.gold}` may appear at the bottom-left of the image frame on eligible products.

### Hero

**`hero`** — Full-bleed dark section, minimum 640px, `{colors.surface-dark}` background or full-frame product photography with a dark scrim. Headline in `{typography.display-xl}` (64px weight-400 serif, 0.02em tracking) with generous line height. A `{typography.editorial-kicker}` line in `{colors.gold}` uppercase precedes the headline on collection launches. A single CTA button sits below the text block; nothing overlays the image directly.

### Editorial Strip

**`editorial-strip`** — Dark full-width band alternating with white product grids to create the opening-and-closing-box rhythm of the page. Kicker in `{typography.editorial-kicker}` + `{colors.gold}`, headline in `{typography.display-md}` serif, body in `{typography.body-md}`. Two-column layout (image left, text right) at desktop; collapses to stacked (image above text) at mobile. `{spacing.section}` padding top and bottom.

### Engraving Badge

**`engraving-badge`** — A flat `{colors.gold}` rectangle with `{colors.on-gold}` text in `{typography.caption}` (0.04em tracking). Reads "PERSONALISATION AVAILABLE" or "ENGRAVING" depending on context. Sharp corners, tight padding (`{spacing.xs}` vertical, `{spacing.sm}` horizontal). Appears on product cards and PDP hero rows; its presence communicates value-add without price decoration.

### Search Drawer

**`search-drawer`** — Drops from the top of the viewport at full width, `{colors.canvas}` fill. The text input renders at `{typography.display-md}` scale (36px serif) — the user's query is treated as a headline, not a form field. A `{colors.hairline}` underline replaces the box border. Results surface in a grid below the input, adapting the `product-card` layout. A hairline close icon at top-right dismisses; Escape key also closes.

### Collection Badge

**`collection-badge`** — A `{colors.surface-soft}` pill (no radius — sharp corners) with `{typography.title-sm}` uppercase label in `{colors.ink}`, 1px `{colors.hairline}` border. Used as filter chips on collection pages and as category labels in nav mega-menus. Never uses color fill beyond the off-white surface.

### Footer

**`footer-bar`** — `{colors.surface-dark}` background, three or four link columns in `{typography.caption}` with `{colors.muted}` link color. The Snowcap star SVG in `{colors.snowcap}` at small scale anchors the footer header. Legal row below the column grid in 11px caption. No gradient, no image treatment — the dark footer is a clean exit from the editorial field above.

### Breadcrumb

**`breadcrumb`** — `{typography.caption}` in `{colors.muted}`, forward-slash separator, with the current page label shifting to `{colors.ink}`. Sits above the PDP headline row, 12px type, no underline on inactive segments except hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grids; hero headline drops to `{typography.display-md}` (36px); nav collapses to hamburger drawer; editorial strips stack image above text; footer columns collapse to single accordion list |
| Tablet | 744–1128px | Two-column product grids; hero at `{typography.display-lg}` (48px); nav shows primary categories inline with overflow in drawer; editorial strips maintain two-column at 50/50 split |
| Desktop | 1128–1440px | Three- or four-column product grids; full nav-bar with mega-menu; hero at `{typography.display-xl}` (64px); editorial strips at asymmetric 60/40 split |
| Wide | > 1440px | Content max-width constrained to ~1440px; hero fills edge-to-edge but text block centers within the content column; product grids cap at four columns |

### Touch Targets

- All buttons minimum 48px tall; width expands to label + padding, never shrinks below 120px
- Nav hamburger icon touch target minimum 44×44px
- Product card tap area spans the full card including image
- Search icon and close icon in drawer minimum 44×44px touch target

### Collapsing Strategy

- Primary navigation collapses to an icon-only hamburger at < 1024px; category labels disappear first, Montblanc wordmark remains visible at all widths
- Editorial strip image drops below text block on mobile rather than hidden
- Engraving badge shifts from bottom-left of image to below product name on mobile product cards
- Footer link columns collapse into tappable accordion rows at mobile, one column visible at a time
- Mega-menu is replaced by a nested drawer at tablet and below, preserving the full category depth

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted**: The site likely loads design tokens via JavaScript or is behind anti-bot protection; all color values above are derived from widely-documented Montblanc brand assets (pen lacquer black, Snowcap white, hardware gold) and should be verified against live computed styles before production use
- **No font stacks extracted**: Typography stacks above reference the commonly cited "Montblanc Text" custom typeface and Helvetica Neue; the actual web font filenames, weights loaded, and fallback order require inspection of live network requests
- **Gold hex value uncertain**: The `{colors.gold}` value (#c5a028) approximates the warm champagne tone visible in product photography and the star emblem; the precise brand gold (which may vary between print and digital specifications) was not confirmed from extraction
- **Dark section background depth**: Whether `{colors.surface-dark}` is true black (#000000) or a very dark near-black (#111111 or similar) could not be confirmed; Montblanc often uses near-black in digital to retain depth in photography
- **Button border-radius confirmation**: `{rounded.none}` (sharp corners) is consistent with observed brand direction but not confirmed from CSS extraction; verify whether any interactive elements carry a 1–2px radius
- **Animation and transition values**: Hover transition timing, mega-menu entrance easing, and hero parallax behavior could not be extracted and are absent from this spec
