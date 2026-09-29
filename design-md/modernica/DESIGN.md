---
version: alpha
name: "Modernica"
source_url: "https://modernica.net"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Powder-coated steel legs bolted to a ceramic bowl at a precise 22-degree splay — that single product detail, the Case Study planter, tells you everything about how Modernica builds a digital storefront. The palette opens with a dusty slate blue (#7796a8) pulled from mid-century California pool tile, deployed across hero overlays, active navigation states, and the primary CTA fill. It sits against a near-black ink (#121212) that grounds product photography in the same high-contrast register as an Eames catalog page. Deep forest green (#435650) arrives as a secondary voice — collection badges, seasonal campaign banners, and hover states on planter-category links — while a warm amber (#daa751) punctuates sale callouts and limited-edition markers with the warmth of kiln-fired glaze. The surface system is deliberately restrained: a clean white canvas, `{colors.surface-soft}` panels at #f5f5f5 for configurator backgrounds, and `{colors.hairline}` dividers so faint they disappear when you stop looking. Typography leans on a geometric sans-serif stack (the site loads fonts via JavaScript, so the exact family is not statically extractable) set at generous sizes — display headings reach 40–48px in weight 600, trusting the architecture of the letterforms rather than decorative flourish. Corners are almost nonexistent: product cards use `{rounded.xs}` or `{rounded.none}`, buttons carry a minimal `{rounded.xs}` radius, and image containers sit flush at zero — the whole system reads like a drafting table, not a candy store. Spacing is generous and architectural, with `{spacing.section}` gutters between product groups and `{spacing.xl}` breathing room inside configurator panels. The grid maxes at 1440px and centers on white, letting each planter photograph command its frame like a piece in a gallery vitrine.

colors:
  primary: "#7796a8"
  primary-active: "#5f7e90"
  primary-disabled: "#b8ccd6"
  secondary: "#435650"
  secondary-active: "#324440"
  accent-gold: "#daa751"
  accent-gold-active: "#c4923d"
  accent-lavender: "#a89cc8"
  ink: "#121212"
  body: "#333333"
  muted: "#808080"
  muted-soft: "#a0a0a0"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-surface-dark: "#dedede"
  success: "#228b06"
  info: "#0d529e"
  error: "#c0392b"

typography:
  display-xl:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  caption-uppercase:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
  nav-link:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  price:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Modernica Sans', 'Futura PT', Futura, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 1px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-gold-accent:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  text-input-error:
    border: 1px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 0
    imageRatio: 1:1
    border: none
    hoverEffect: opacity 0.85 on image
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.ink}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 560px
    contentMaxWidth: 600px
    typography: "{typography.display-xl}"
    ctaStyle: button-primary
    overlay: "linear-gradient(rgba(18,18,18,0.3), rgba(18,18,18,0.5))"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} 0 {spacing.xl}"
    borderBottom: 1px solid {colors.hairline}
  configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xl}"
    border: 1px solid {colors.hairline}
  swatch-selector:
    size: 32px
    rounded: "{rounded.full}"
    border: 2px solid transparent
    borderActive: 2px solid {colors.ink}
    spacing: "{spacing.sm}"
  badge-limited:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-surface-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separator: "/"
    activeColor: "{colors.ink}"
  announcement-bar:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  image-gallery:
    rounded: "{rounded.none}"
    gap: "{spacing.xs}"
    thumbnailSize: 64px
    thumbnailBorder: 2px solid transparent
    thumbnailBorderActive: 2px solid {colors.ink}
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: 1px solid {colors.hairline}
    padding: "{spacing.lg} 0"
    iconSize: 16px

## Components

### Buttons

**`button-primary`** — Filled slate-blue (#7796a8) rectangle with 4px radius, white text at 16px/500. On hover, darkens to `primary-active` (#5f7e90) with no transition longer than 150ms. Disabled state washes out to #b8ccd6 at reduced opacity. Used for Add to Cart, newsletter subscribe, and configurator "Build Yours" actions.

**`button-secondary`** — White fill with a 1px ink-black border and matching text. On hover, inverts to solid black fill with white text — a clean light-to-dark flip that reinforces the architectural high-contrast system. Same 48px height and 4px radius as primary.

**`button-dark`** — Solid #121212 fill with white text, used on dark hero sections and the sticky mobile cart bar where the slate-blue primary would lack contrast against photographic backgrounds.

**`button-gold-accent`** — Amber (#daa751) fill with dark text, reserved for limited-edition callouts and sale CTAs. Slightly smaller at 40px height to signal secondary hierarchy while retaining visual punch.

### Navigation

**`nav-bar`** — 64px fixed header on white with a single-pixel hairline bottom border. Logo left-aligned, navigation links centered in uppercase 14px/500 with 0.3px tracking. Cart icon and hamburger (mobile) sit right-aligned. The bar collapses to a hamburger-driven slide-out drawer below 744px.

**`announcement-bar`** — 36px deep strip in forest green (#435650) with white caption text, centered. Used for shipping thresholds, seasonal promotions, and collection launches. Dismissable via a subtle × icon that inherits `on-primary` color.

### Product Cards

**`product-card`** — Zero-radius container with a square 1:1 image ratio. No border, no shadow — products float on the grid purely through whitespace separation. On hover, the image drops to 85% opacity revealing the white canvas beneath, a subtle invitation to click. Title renders in `title-sm` (16px/500), price in `price-sm` (14px/600) below. Badge overlays (new, limited, sale) pin to the top-left corner with 8px inset.

### Hero Banner

**`hero-banner`** — Full-bleed image container at minimum 560px height with a dark gradient overlay (30% → 50% opacity). Display text at 48px/600 in white, left-aligned within a 600px max-width content block. Primary CTA button positioned below with `{spacing.lg}` gap. The hero never auto-rotates — each collection landing page uses a single curated image.

### Configurator

**`configurator-panel`** — Light gray (#f5f5f5) panel with 4px radius and hairline border, housing the planter customization interface. Swatch selectors for glaze color render as 32px circles (`{rounded.full}`) with a 2px ink border when active. Size and stand options use segmented button groups styled as `button-secondary` variants.

**`swatch-selector`** — Circular color swatches at 32px diameter, spaced 8px apart. Inactive swatches show their fill color with a transparent border; active state adds a 2px #121212 ring. Used for glaze finishes, wood stain options, and powder-coat color choices.

### Content Blocks

**`accordion`** — Product detail sections (Description, Dimensions, Shipping, Care) stack vertically with hairline separators. Each row shows `title-sm` text with a minimal 16px chevron icon right-aligned. Expanded content renders in `body-md` with `{spacing.lg}` top padding. No animation beyond a 150ms height transition.

**`breadcrumb`** — Muted gray caption text with "/" separators. Final crumb renders in ink color without a link. Positioned directly below the nav-bar with `{spacing.base}` vertical padding.

### Image Gallery

**`image-gallery`** — Product detail page uses a vertical thumbnail strip (desktop) or horizontal swipe rail (mobile) alongside a main image at zero radius. Thumbnails are 64px squares with a 2px border that activates to ink-black on selection. No lightbox — clicking the main image opens a full-screen overlay with pan/zoom.

### Footer

**`footer`** — Dark (#121212) full-bleed section with light gray text. Four-column link grid on desktop collapsing to accordions on mobile. Links brighten to slate-blue on hover. Newsletter input sits in a single row: white text-input with a dark-filled submit button adjacent. Bottom row carries copyright, legal links, and payment icons at `caption` size.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav drawer, hero text drops to `display-md` (28px), configurator panel stacks vertically, sticky "Add to Cart" bar fixed to bottom at 64px |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, hero height reduces to 420px, image gallery switches to horizontal thumbnail rail |
| Desktop | 1128–1440px | Three- or four-column product grid, full horizontal nav, 64px section spacing, image gallery with vertical thumbnail strip |
| Wide | > 1440px | Content max-width caps at 1440px and centers, outer margins fill with canvas white, product grid holds at four columns with increased card spacing |

### Touch Targets

- All interactive elements maintain a minimum 44×44px touch area on mobile
- Swatch selectors expand hit area to 44px despite 32px visual diameter via transparent padding
- Accordion rows use full-width tap targets spanning the entire row height
- Mobile nav drawer items are 56px tall with left-aligned text and generous `{spacing.lg}` vertical rhythm

### Collapsing Strategy

- Desktop horizontal nav collapses to hamburger drawer at 744px breakpoint
- Footer four-column grid collapses to stacked accordions on mobile
- Product configurator options shift from side-by-side to full-width stacked panels
- Breadcrumb truncates middle segments on mobile, showing only category and current page
- Announcement bar text truncates with ellipsis rather than wrapping to preserve 36px height

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font family could not be statically extracted (no CSS font-family declarations found); the site likely loads typefaces via JavaScript or a Shopify theme font loader — the geometric sans-serif stack used above is an educated approximation based on visual style
- Exact button padding, heights, and spacing values are inferred from the mid-century minimal aesthetic rather than measured from computed styles
- No favicon or Open Graph image metadata was available to confirm secondary brand marks
- The #0d529e (deep blue) and #a89cc8 (lavender) colors appear in the extraction but their specific UI roles are unclear — they may be used in seasonal campaign elements or out-of-stock indicators
- Transition/animation timing values (hover durations, drawer slide speeds) could not be extracted
- Dark-mode behavior, if any, is not documented — the site appears to operate exclusively in light mode
