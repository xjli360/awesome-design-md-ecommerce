---
version: alpha
name: "Helm Boots"
source_url: "https://helmboots.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Warm amber (#f8b52e) cuts across a bone-white canvas (#fbf9f5) like a lantern lit inside a workshop — the organizing metaphor for Helm Boots' visual system, which pairs a deep slate-teal ink (#2d3b43) against parchment backgrounds to suggest permanence rather than trend. Where most footwear DTC brands reach for stark white-and-black, Helm reaches for warmth: the canvas is slightly creamier than white (#fbf9f5 rather than #ffffff), hairlines are warm stone (#e6e4de), and even mid-ground surfaces shift toward oat (#f1f1f1) rather than a cold neutral. The typography pairing does the heavy philosophical lifting — Libre Baskerville anchors display and headline positions with its thick-bracketed serifs and high-contrast stroke, while Instrument Sans handles every label, button, and navigation element with geometric quiet. That combination communicates exactly what "Footwear For Life" promises: something built with old-world intention, purchased through a modern interface. Neon yellow (#ffff00) surfaces only as a punctuation mark — a badge chip or sale callout — functioning as the jolt in an otherwise grounded palette. The amber (#f8b52e) occupies the mid-register between these two poles, appearing in price highlights and hover states that reward attention without demanding it. Interactive blue (#146ff8) routes to links and cart confirmations, keeping transactional affordances visually distinct from brand expression. Rounded corners sit in the minimal range — `{rounded.xs}` to `{rounded.sm}` on most components, with the card surface barely soft enough to read as digital rather than print. The overall composition feels less like a product catalog and more like a reference book that happens to have an add-to-cart button.

colors:
  primary: "#2d3b43"
  primary-active: "#1e2c33"
  primary-disabled: "#8fa4ab"
  accent-amber: "#f8b52e"
  accent-yellow: "#ffff00"
  interactive: "#146ff8"
  interactive-active: "#0d5fd4"
  ink: "#121212"
  body: "#2d3b43"
  muted: "#6b7b82"
  hairline: "#e6e4de"
  hairline-soft: "#dedede"
  canvas: "#fbf9f5"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  surface-warm: "#e6e4de"
  on-primary: "#fbf9f5"
  on-accent: "#121212"

typography:
  display-xl:
    fontFamily: "'Libre Baskerville', Georgia, serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Libre Baskerville', Georgia, serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Libre Baskerville', Georgia, serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Libre Baskerville', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.03em
  body-md:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  label-caps:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  price-display:
    fontFamily: "'Libre Baskerville', Georgia, serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.04em
  button-sm:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.04em
  nav-link:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.01em

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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-accent:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-sm}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "3/4"
    nameTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    padding: "{spacing.section} {spacing.xl}"
    ctaVariant: "button-accent"
  sale-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  material-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderColorSelected: "{colors.primary}"
    borderWidthSelected: 1.5px
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    height: 44px
    width: 44px
  swatch-color:
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.primary}"
    height: 28px
    width: 28px
  pdp-breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
  announcement-bar:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label-caps}"
    height: 36px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.hairline-soft}"
    headlineTypography: "{typography.label-caps}"
    bodyTypography: "{typography.body-sm}"

## Components

### Buttons

**`button-primary`** — A dark slate-teal block (#2d3b43) with minimal 4px radius (`{rounded.xs}`) and cream-white type (`{colors.on-primary}`). At 48px tall with generous horizontal padding it reads as solid and deliberate rather than pill-shaped or fashionable. Hover darkens to `{colors.primary-active}` (#1e2c33); disabled state washes to a flat mid-slate (`{colors.primary-disabled}`).

**`button-secondary`** — Transparent fill with a 1.5px slate border and matching slate text, mirroring primary in height and radius so the two pair cleanly in side-by-side PDP layouts without competing for hierarchy.

**`button-accent`** — Amber-filled (`{colors.accent-amber}`, #f8b52e) with dark ink text (`{colors.on-accent}`). Reserved for high-emphasis moments — the hero CTA, the free-shipping threshold prompt — where the brand's warmth needs to convert.

### Product Card

**`product-card`** — A 3:4 portrait image crops the boot against a neutral or studio ground, with name set in `{typography.title-md}` (Instrument Sans 600) and price in `{typography.price-display}` (Libre Baskerville 700, 20px). No heavy shadow; the card sits on `{colors.surface-card}` with whitespace separating cards rather than visible borders. Material badges (`material-badge`) float over the bottom-left corner of the image on hover or always-on for key construction callouts.

### Navigation

**`nav-bar`** — Canvas background (`{colors.canvas}`) with a single 1px warm hairline border-bottom (`{colors.hairline}`). The HELM logotype is set in Libre Baskerville (`{typography.display-sm}`). Nav links render in Instrument Sans at 14px/500 weight. On mobile the nav collapses to a hamburger; secondary links live in a full-width slide-in drawer.

### Hero Section

**`hero-section`** — Full-bleed slate (`{colors.primary}`) with headline in `{typography.display-xl}` Libre Baskerville reversed to cream. The subhead uses `{typography.display-sm}` at regular weight. The primary CTA renders as `button-accent` in amber, providing the one warm break in the dark slate field and drawing the eye immediately.

### Badges & Tags

**`sale-badge`** — A neon yellow chip (`{colors.accent-yellow}`) with all-caps label-caps typography and 4px radius. Appears on product cards during sale events; its deliberate brightness reads as a functional intrusion rather than a brand accent.

**`material-badge`** — A warm stone chip (`{colors.surface-warm}`) for construction callouts like "Goodyear Welt" or "Full-Grain Leather," set in 11px label-caps. Stacks below the price on mobile PDP or floats over the product image on cards.

### Size Selector

**`size-selector`** — 44×44px square tiles with a hairline border in resting state; selected state upgrades to a 1.5px `{colors.primary}` ring without fill change. The catalog-like grid of tiles reflects the brand's no-frills directness.

### Announcement Bar

**`announcement-bar`** — A 36px amber ribbon (`{colors.accent-amber}`) pinned to the very top of the viewport, set in all-caps Instrument Sans. Used for free-shipping thresholds and limited-edition drops; amber pulls from the same accent system rather than introducing a new promotional color.

### Footer

**`footer`** — Full-bleed slate (`{colors.primary}`) with column headers in `{typography.label-caps}` and links in `{typography.body-sm}`. The canvas-on-dark inversion mirrors the hero, unifying the top and bottom of the page into a single slate frame around the content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column PLP grid; nav collapses to hamburger drawer; hero headline drops to `{typography.display-md}`; size tiles expand to 48×48px for touch |
| Tablet | 744–1128px | Two-column PLP grid; nav shows top-level links, secondary links hidden; hero uses split layout with image right |
| Desktop | 1128–1440px | Three-column PLP grid; full nav with dropdown; PDP uses two-column image-left / details-right layout |
| Wide | > 1440px | Four-column PLP grid; content constrained to 1440px max-width centered; hero padding expands to full section spacing |

### Touch Targets
- All buttons maintain 48px minimum height on mobile
- Size selector tiles pad to 48×48px on touch screens even if visual tile is 44px
- Color swatches pad to 40px touch target even when visual circle is 28px
- Navigation drawer links minimum 48px row height with generous vertical padding

### Collapsing Strategy
- Hero subheadline collapses first on narrowing viewports before headline font-size reduces
- Material badges stack below price on mobile PDP rather than overlapping image
- Announcement bar text truncates with ellipsis on narrow mobile if string exceeds one line
- Footer columns collapse to accordions on mobile with chevron toggles
- Product card name truncates at two lines; price and badges remain always visible

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No explicit border-radius values extracted from live CSS; `{rounded.xs}` (4px) inferred from the heritage/minimal visual style
- Button hover and focus ring specs not directly observed; derived from primary/primary-active color logic
- `#ffff00` neon yellow observed in extracted palette but exact placement (sale badge vs. promo bar vs. alert) not confirmed — assigned to `sale-badge` based on DTC convention
- `#146ff8` interactive blue may be a Shopify theme default rather than a deliberate brand color; brand ownership vs. platform default unclear
- Libre Baskerville weight usage per component (400 regular, 400 italic, 700, 700 italic) inferred from standard Google Fonts availability, not confirmed from CSS
- No dark-mode palette detected
- No animation timing or transition easing values extracted
- PDP image gallery count, zoom trigger behavior, and video support not confirmed
- Mega-menu or flyout structure not observed; dropdown behavior assumed from nav-bar height
