---
version: alpha
name: "Postery"
source_url: "https://www.postery.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  TTRamillas — a high-contrast editorial serif almost never seen outside print catalogs — appears at the product-card level, not only in the hero, which tells you that Postery treats every purchase as an encounter with typography as much as image. Against near-white (#f7f7f8) and cloud-white (#f3f4f6) canvas surfaces, the midnight-navy primary (#00112c) reads less like a call-to-action color and more like the ink of a limited-edition print run: concentrated, deliberate, and used sparingly. Navigation runs in Moderat, a geometric sans set at 14px with zero letter-spacing inflation — legible without asserting itself over the poster images that command the grid. Filters and product selectors use {rounded.none} chips with a hairline border (#dbdee2) that flip to solid #00112c on activation, a binary toggle free of visual ceremony; that same principle extends to primary buttons, which carry no border-radius and rely on the color's weight alone. The editorial logic reaches the footer, which inverts fully to midnight navy, turning what is usually a typographic afterthought into the visual anchor of the page. Product cards sit in a strict 2:3 portrait ratio mirroring standard poster proportions, so the grid functions as a wall of hung art rather than a retail shelf. Sale callouts reach for #e22d2d; in-stock confirmation draws on #3f6b47 forest green; star ratings appear in #f5a623 amber — three punctuation marks in an otherwise controlled palette. The color field holds its restraint so the posters, photographed flat against white, do all the chromatic work. Frame and size selectors are inline controls rather than modal drawers, keeping configuration compact and non-disruptive. The entire system behaves like a gallery catalog that happens to support adding items to a cart.

colors:
  primary: "#00112c"
  primary-active: "#00081a"
  primary-disabled: "#5c687c"
  ink: "#00112c"
  body: "#5c687c"
  muted: "#8d95a3"
  hairline: "#dbdee2"
  border-medium: "#c9cdd3"
  canvas: "#ffffff"
  surface-soft: "#f7f7f8"
  surface-card: "#f3f4f6"
  surface-warm: "#eeeff1"
  on-primary: "#ffffff"
  link: "#0000e6"
  error: "#e22d2d"
  error-dark: "#c72727"
  error-surface: "#ffdede"
  success: "#3f6b47"
  star: "#f5a623"
  muted-warm: "#5a5656"

typography:
  display-xl:
    fontFamily: "'TTRamillas', Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "'TTRamillas', Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'TTRamillas', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Moderat', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Moderat', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Moderat', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Moderat', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Moderat', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Moderat', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Moderat', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "'Moderat', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  price-display:
    fontFamily: "'Moderat', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0
  filter-label:
    fontFamily: "'Moderat', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    opacity: 0.5
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "2/3"
    gap: "{spacing.sm}"
    padding: "{spacing.sm}"
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.body}"
  product-card-hover:
    outline: "1px solid {colors.border-medium}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    imagePosition: right
  hero-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
  collection-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.section}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.filter-label}"
    borderBottom: "1px solid {colors.hairline}"
    height: 48px
    gap: "{spacing.lg}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
    padding: 6px 14px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
    activeBackground: "{colors.surface-soft}"
    padding: 8px 12px
  frame-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
    activeBackground: "{colors.surface-soft}"
    padding: 8px 12px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: none
    placeholderColor: "{colors.muted}"
    padding: 12px 16px
    height: 48px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-primary}"
    linkHoverOpacity: 0.7
    padding: "{spacing.xxl} 0"
  toast-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  toast-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px

---

## Components

### Buttons

**`button-primary`** — Solid midnight-navy (#00112c) fill with no border-radius whatsoever: the sharp-cornered rectangle is a deliberate refusal of the rounded-corner friendliness that saturates DTC. On hover the fill deepens to #00081a; disabled state mutes to `{colors.primary-disabled}` at reduced opacity. Height is 48px throughout with generous horizontal padding to give the label breathing room.

**`button-secondary`** — White canvas with a 1px #00112c border and matching midnight-navy text. Hover introduces a `{colors.surface-soft}` fill so the button reads as pressed into the background. Same sharp corners and 48px height as the primary, with 1px inset padding to optically match.

**`button-ghost`** — Transparent background, `{colors.body}` slate text, no border. Used for secondary navigational actions — "View all", category pivots — where visual weight would compete with the poster imagery.

### Filter Bar & Chips

**`filter-bar`** — A slim 48px tray sitting below the category header, uppercase `{typography.filter-label}` labels at 12px with 0.8px letter-spacing. A hairline bottom border separates it from the product grid without adding visual bulk.

**`filter-chip`** — Pill-shaped (`{rounded.full}`) with a 1px `{colors.hairline}` border on a white ground. Inactive chips recede; active chips invert to solid midnight navy with white text, no animation — just a direct swap that reads as authoritative rather than playful.

### Product Card

**`product-card`** — Portrait 2:3 ratio image filling a soft `{colors.surface-soft}` tile, title in `{typography.body-sm}`, price in `{typography.price-display}` at a muted `{colors.body}` slate. Cards have no rounding; hover state reveals a 1px `{colors.border-medium}` outline rather than a shadow, keeping the grid clean and map-like. Badges (`badge-new`, `badge-sale`) sit as flat rectangles in the top-left corner of the image.

### Hero

**`hero`** — White canvas with a TTRamillas display headline (`{typography.display-xl}`, 52px, weight 300) flanked by a large poster image on the right. The light weight of the serif at large scale creates an airy, editorial register. `hero-dark` is the full midnight-navy inversion used for seasonal or featured campaigns — the same type stacks reversed to `{colors.on-primary}`.

### Size & Frame Selectors

**`size-selector`** and **`frame-selector`** — Inline rectangular buttons with a 4px radius (`{rounded.xs}`) and 1px hairline border. Selected state swaps to a `{colors.primary}` border with a `{colors.surface-soft}` fill, avoiding the full-inversion that the filter chips use — keeping the product configurator visually quieter than the browse-level controls.

### Navigation

**`nav-bar`** — 64px tall, white ground, midnight-navy logotype, `{typography.nav-link}` at 14px with no weight boost. A 1px `{colors.hairline}` bottom border grounds the bar. The nav relies on its midnight-navy logo for brand presence rather than a colored bar.

### Footer

**`footer`** — Full midnight-navy inversion: `{colors.primary}` background, all text and links in `{colors.on-primary}` white with 0.7 opacity hover. The footer functions as the page's chromatic anchor, giving weight to a layout that otherwise runs mostly white and pale gray.

### Search

**`search-input`** — Set on a `{colors.surface-soft}` ground with no visible border, creating a recessed trough appearance. Placeholder text in `{colors.muted}` and no radius; the search bar reads as an editorial caption field rather than a form widget.

### Cart Drawer

**`cart-drawer`** — 400px slide-in panel from the right, white canvas, 1px `{colors.hairline}` left border. No shadow — the border alone defines the edge, consistent with the brand's avoidance of depth effects.

### Badges & Toasts

**`badge-new`** and **`badge-sale`** — Flat rectangles with no radius, typeset in `{typography.caption}` at 12px. New badges fill midnight navy; sale badges fill `{colors.error}` (#e22d2d). Both sit flush on the image corner. Toast notifications mirror the badge logic — success in `{colors.success}` forest green, error in `{colors.error}` red — with a minimal 4px radius (`{rounded.xs}`) as the only soft edge in the system.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter bar collapses to a bottom sheet or modal overlay; nav collapses to hamburger; hero switches to stacked layout with image above headline |
| Tablet | 744–1128px | 2-column product grid; filter bar persists as horizontal scroll; nav shows primary categories, secondary items in overflow menu |
| Desktop | 1128–1440px | 3–4 column product grid; filter sidebar option may appear left of grid; hero returns to side-by-side layout |
| Wide | > 1440px | Max content width capped with generous lateral gutters; grid may extend to 5 columns; hero image scales to fill the wider frame |

### Touch Targets

- All buttons and chips minimum 44px tall on mobile
- Filter chips expand vertical padding to 10px on touch viewports
- Size and frame selectors minimum 44×44px hit area even when visually smaller
- Nav links padded to full-height of the 64px bar for easy tap

### Collapsing Strategy

- Filter bar collapses first: transitions from persistent horizontal tray to a "Filter & Sort" button that opens a bottom sheet
- Secondary nav items collapse into an overflow drawer before the hamburger triggers
- Cart icon persists at all breakpoints; cart drawer width narrows to full-width on mobile
- Collection banner headline scales from `{typography.display-md}` (desktop) to `{typography.display-sm}` (mobile) via fluid step
- Hero image moves above text on mobile; image aspect ratio shifts from 3:2 landscape crop to square

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font weights for TTRamillas in use (light/regular/medium) not confirmed from extraction; weight 300 for display assumed from Scandinavian editorial conventions
- Moderat weight usage across UI states (400 vs 500) inferred; no computed-style confirmation
- No meta theme-color present — mobile browser chrome color unknown
- Hover/focus animation timing curves not extractable; transitions assumed 150–200ms ease
- Exact grid column counts and gutter widths at each breakpoint not extracted
- Whether the filter bar uses a left sidebar variant on desktop or strictly a top bar is unconfirmed
- Product card image background color (white vs surface-soft) varies by poster; exact tile background not confirmed
- Star rating component structure (half-stars, count display format) not extracted
- Wishlist / save functionality design (heart icon, saved state color) not captured
- Frame and material swatch rendering (color dot vs thumbnail vs text) not confirmed from extraction
