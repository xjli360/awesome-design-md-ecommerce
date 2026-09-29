---
version: alpha
name: "Traeger"
source_url: "https://www.traegergrills.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Burnt orange (#d95e16) hits like the first lick of flame inside a preheated barrel — it is Traeger's singular brand voltage, present on every primary CTA, promo badge, and temperature dial accent across the site. The canvas is never clinical white; it sits at a smoky off-white (#f6f4f3) with warm taupe undertones (#d4d2ca, #b4aca6) that evoke ash-dusted steel and weathered hardwood. Knockout — Hoefler&Co's ultra-condensed gothic — dominates display headlines in weights 46 through Banner, delivering the verticality and compression of stenciled text on industrial equipment. Body copy drops to Roboto at 400/500 weight, a workhorse sans-serif that stays legible against those warm-neutral backgrounds. The type scale punches hard at the top — display headlines often hit 48–72px in Knockout-68 with heavy letterspacing — then compresses fast into modest 14–16px body. Corner radii are restrained: product cards use `{rounded.xs}` to `{rounded.sm}`, buttons sit at `{rounded.xs}`, and only pill badges or toggle chips reach `{rounded.full}`. The palette's depth lives in its neutral range — six distinct warm grays between #e9e9e6 and #393939 create layered surfaces without a single cool blue-gray in sight. Secondary accent orange (#e9ae85) and a red band (#e03d24 for sale states, #b72a1c on hover) extend the fire spectrum, while a single bright green (#3ce783) signals availability and success. Navigation is dark and dense (#25282a background, white text, Knockout-48 uppercase links), reinforcing the brand's tool-catalog DNA over lifestyle softness. Spacing is generous at the section level (`{spacing.section}` = 64px between content blocks) but tight within product grid cells, packing grill imagery edge-to-edge with only `{spacing.sm}` gutters.

colors:
  primary: "#d95e16"
  primary-hover: "#b84308"
  primary-active: "#963c03"
  primary-disabled: "#e9ae85"
  primary-light: "#faf0ea"
  accent-orange: "#e97f38"
  accent-warm: "#e9ae85"
  sale: "#e03d24"
  sale-hover: "#b72a1c"
  sale-light: "#f7efed"
  success: "#3ce783"
  success-light: "#eafaef"
  ink: "#25282a"
  ink-deep: "#1a1a1a"
  body: "#393939"
  muted: "#747778"
  muted-soft: "#808285"
  muted-pale: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-warm: "#d4d2ca"
  border-warm: "#b4aca6"
  canvas: "#f6f4f3"
  canvas-alt: "#f5f4f1"
  surface-soft: "#e9e9e6"
  surface-card: "#ffffff"
  surface-dark: "#25282a"
  surface-charcoal: "#313c3f"
  surface-deep: "#101010"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  warm-brown: "#423933"
  neutral-mid: "#b3b3b1"
  neutral-dim: "#727170"

typography:
  display-xl:
    fontFamily: "'Knockout-68', 'Knockout', 'Arial Narrow', sans-serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 1.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Knockout-48', 'Knockout', 'Arial Narrow', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: 1px
    textTransform: uppercase
  display-md:
    fontFamily: "'Knockout-46', 'Knockout', 'Arial Narrow', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.5px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Knockout-46', 'Knockout', 'Arial Narrow', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.14
    letterSpacing: 0.5px
    textTransform: uppercase
  title-lg:
    fontFamily: "'Knockout-48', 'Knockout', 'Arial Narrow', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "'Roboto', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'Roboto', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'Knockout-48', 'Knockout', 'Arial Narrow', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Knockout-46', 'Knockout', 'Arial Narrow', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Roboto', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Knockout-48', 'Knockout', 'Arial Narrow', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 1px
    textTransform: uppercase
  banner-display:
    fontFamily: "'Knockout-Banner', 'Knockout-68', 'Arial Narrow', sans-serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: 2px
    textTransform: uppercase
  price:
    fontFamily: "'Roboto', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  price-sale:
    fontFamily: "'Roboto', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  label:
    fontFamily: "'Roboto', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 52px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
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
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 30px
    height: 52px
    border: 2px solid {colors.ink}
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 52px
  button-dark-hover:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 14px 16px
    height: 52px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.ink}
  text-input-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 40px
  nav-bar-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 24px 32px
    boxShadow: 0 8px 24px rgba(0,0,0,0.12)
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: 0
    imageAspectRatio: 1/1
    imageBackgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    textColor: "{colors.sale}"
  hero-banner:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.banner-display}"
    padding: 80px 40px
    minHeight: 600px
    overlay: linear-gradient(to top, rgba(0,0,0,0.6) 0%, transparent 60%)
  hero-subtitle:
    typography: "{typography.body-lg}"
    textColor: "{colors.on-dark}"
  promo-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.success}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-lg}"
    rounded: "{rounded.xs}"
    padding: 24px
    imageAspectRatio: 4/3
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: 1px solid {colors.hairline}
    iconColor: "{colors.muted}"
  temperature-dial:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    rounded: "{rounded.full}"
    borderWidth: 4px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: 64px 40px
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-lg}"
    textColor: "{colors.on-dark}"
  comparison-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    cellPadding: 16px
    border: 1px solid {colors.hairline}
  spec-list:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    divider: 1px solid {colors.hairline-warm}
    rowPadding: 12px 0
  toast-notification:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px 20px
    boxShadow: 0 4px 16px rgba(0,0,0,0.2)

## Components

### Buttons
**`button-primary`** — Burnt-orange fill with white Knockout uppercase text at 1.2px letterspacing. Corners are barely softened at `{rounded.xs}`. On hover, background darkens to `{colors.primary-hover}`; on press, drops further to `{colors.primary-active}`. Disabled state uses the washed-out `{colors.primary-disabled}` at reduced opacity. Height is a generous 52px, wider than many DTC sites, giving the condensed type room to breathe.

**`button-secondary`** — Transparent fill with a 2px solid `{colors.ink}` border and dark Knockout text. On hover the entire button inverts to solid ink with white text, creating a decisive toggle effect. Used for secondary actions like "View Details" or "Compare Models."

**`button-dark`** — Solid charcoal/ink fill with white text, used on light backgrounds where the orange primary would compete with product photography. Hover lightens slightly to `{colors.body}`.

### Navigation
**`nav-bar`** — Dark (#25282a) horizontal bar at 64px height. Links are Knockout-48 uppercase at 14px with generous letterspacing. Dropdown mega-menus open on hover with a white card, no border-radius, and a subtle drop shadow. The nav communicates catalog density — grills, accessories, sauces, recipes — without lifestyle softness.

**`nav-bar-dropdown`** — Full-width white panel with multi-column layout. Category headers use `{typography.title-sm}`, item links use `{typography.body-sm}`. Imagery is inline (grill thumbnails at 80px) to aid product recognition.

### Product Cards
**`product-card`** — Square image container on a warm `{colors.surface-soft}` background with `{rounded.xs}` corners. Title sits below in Roboto Bold 16px, price in Roboto Bold 18px. Sale prices render in `{colors.sale}` with the original price struck through in `{colors.muted}`. Cards have no border or shadow — the tinted background provides separation against the canvas.

### Hero Banner
**`hero-banner`** — Full-bleed photography (typically a grill in use, smoke billowing) with a bottom-up dark gradient overlay. Headline in Knockout-Banner at 72px sits in the lower third. A subtitle in Roboto 18px and a `button-primary` CTA complete the composition. Minimum height 600px ensures cinematic impact.

### Badges
**`promo-badge`** — Small orange pill with uppercase white label text (11px, 700 weight). Sits in the top-left corner of product cards for promotional callouts.

**`sale-badge`** — Same dimensions as promo-badge but in `{colors.sale}` red. Indicates markdown pricing.

**`new-badge`** — Bright green (#3ce783) background with dark text, signaling new arrivals or product launches.

### Category Tiles
**`category-tile`** — Rectangular cards (4:3 aspect ratio) with product-category photography and an overlay Knockout title. Background uses `{colors.surface-soft}` as fallback. Tiles link to collection pages and appear in a 2–4 column grid depending on viewport.

### Search
**`search-bar`** — Pill-shaped (`{rounded.full}`) input field with a muted search icon on the left. Used in the nav-bar dropdown and mobile overlay. Placeholder text in `{colors.muted}`, active text in `{colors.ink}`.

### Footer
**`footer`** — Dark background matching the nav-bar. Four-column layout with Knockout uppercase headings and Roboto body links. Links lighten on hover rather than underlining. Newsletter signup input uses a dark-themed variant of `text-input` with a `button-primary` submit.

### Comparison Table
**`comparison-table`** — Used on grill category pages to compare specs across models. White card with `{rounded.sm}` corners, thin `{colors.hairline}` cell borders, sticky header row with model names in `{typography.title-sm}`. Check/cross icons replace text for feature presence.

### Spec List
**`spec-list`** — Vertical key-value list on product detail pages. Label in `{typography.caption}` muted gray, value in `{typography.body-md}` dark. Rows separated by warm hairlines (`{colors.hairline-warm}`). Used for dimensions, weight, hopper capacity, cooking area.

### Toast Notification
**`toast-notification`** — Dark rounded card that slides up from bottom-right on add-to-cart. White body text with product thumbnail and a brief confirmation message. Auto-dismisses after 4 seconds.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, nav collapses to hamburger with full-screen dark overlay, hero banner reduces to 400px min-height with display-md headline, category tiles stack 1-up, comparison table scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid, nav remains collapsed, hero headline scales to display-lg, category tiles in 2-column grid, footer collapses to 2-column |
| Desktop | 1128–1440px | Three- to four-column product grid, full horizontal nav with mega-menu dropdowns, hero at full 600px+ height with banner-display type, footer in 4-column layout |
| Wide | > 1440px | Content max-width caps at 1440px and centers, product grid may extend to 5 columns on collection pages, increased section spacing (96px) |

### Touch Targets
- All interactive elements maintain 48px minimum touch target on mobile
- Product card tap area extends to full card surface (not just title/image)
- Nav hamburger icon padded to 48×48px hit area
- Filter/sort dropdowns use 52px row height on touch devices

### Collapsing Strategy
- Desktop mega-menu navigation collapses into a slide-out drawer below 1128px
- Product comparison table switches from fixed columns to horizontal scroll below 744px
- Spec lists remain vertical but reduce padding on mobile
- Hero CTA buttons stack vertically on mobile with full-width stretch
- Footer columns collapse from 4 → 2 → 1 as viewport narrows

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Knockout font weights and exact OpenType features could not be fully verified from extraction — the site loads multiple cuts (46, 48, 68, Banner) but precise weight mappings may differ from the 400-weight assumption used here
- No CSS custom properties or design-token JSON was exposed in the extracted data; color and spacing values are inferred from computed styles
- Motion/animation specifications (transition durations, easing curves) were not extractable
- Dark-mode variant not detected — the site appears to run a single warm-light theme only
- Icon system details (stroke width, grid size, icon font vs SVG) could not be determined from color/font extraction alone
- Exact breakpoint values are estimated from common patterns; Traeger may use slightly different thresholds
- The `Roboto!important` entry in font stacks suggests override specificity battles in the CSS — actual rendering priority between Knockout and Roboto on edge cases may vary
