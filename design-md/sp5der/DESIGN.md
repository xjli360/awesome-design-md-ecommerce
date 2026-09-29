---
version: alpha
name: "Sp5der"
source_url: "https://kingspider.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The banner reads SP5DER WORLDWIDE in Michroma caps — a geometric sci-fi face where every character has terminal angles and zero curves — announcing the brand before a single image loads. Neon green (#3ed660) spider-web graphics erupt against an almost lightless canvas (#121212), a single chromatic detonation that makes each product page feel like a drop-table built for hype rather than a browsable store. The palette does not resolve into brand harmony: amber (#ee9441), deep red (#8b0000), and forest green (#006400) exist as colorway signals across stacked swatches, so the site itself performs the same maximalist collision as the garments. Mid-gray tones (#777777, #555555) carry the resting UI — dividers, placeholders, disabled states — giving the scroll a rhythm of voltage and quiet, loud product image against gray separator against loud product again. Buttons sit at `{rounded.xs}` with minimal radius, keeping geometry sharp and hype-adjacent; the brand has no visual softness budget to allocate to interactive elements. The spider-web motif functions simultaneously as logo, background texture, and implied grid: negative space becomes silk between product nodes, and the whole layout leans on full-bleed photography as the web's anchor points. Inter carries all transactional copy — prices, size labels, form fields — while Michroma holds every headline and label, creating a two-register system where aspiration and transaction speak in recognizably different voices. The "WORLDWIDE" suffix in every brand treatment signals drop-culture ambition over geography, matching a colorway cadence where no two releases share a palette and the UI must accommodate that chromatic chaos without a fixed tonal anchor.

colors:
  primary: "#3ed660"
  primary-active: "#2bb84d"
  primary-disabled: "#1a6b2e"
  ink: "#dedede"
  body: "#c8c8c8"
  muted: "#777777"
  hairline: "#555555"
  canvas: "#121212"
  surface-soft: "#191919"
  surface-card: "#191919"
  on-primary: "#121212"
  accent-red: "#8b0000"
  accent-orange: "#ee9441"
  accent-forest: "#006400"
  mid-gray: "#555555"

typography:
  display-xl:
    fontFamily: "'Michroma', 'Michroma-Regular', monospace"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: 0.06em
    textTransform: uppercase
  display-md:
    fontFamily: "'Michroma', 'Michroma-Regular', monospace"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.05em
    textTransform: uppercase
  display-sm:
    fontFamily: "'Michroma', 'Michroma-Regular', monospace"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.05em
    textTransform: uppercase
  title-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.01em
  price:
    fontFamily: "Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-label:
    fontFamily: "'Michroma', 'Michroma-Regular', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  badge:
    fontFamily: "'Michroma', 'Michroma-Regular', monospace"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'Michroma', 'Michroma-Regular', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Michroma', 'Michroma-Regular', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.1em
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    border: "1px solid {colors.ink}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1:1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    padding: "{spacing.md} 0"
    imageOverlayHover: "rgba(62,214,96,0.06)"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-sm}"
    overlayColor: "rgba(18,18,18,0.55)"
    minHeight: 600px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    height: 36px
    padding: "0 {spacing.base}"
  colorway-badge:
    size: 24px
    rounded: "{rounded.full}"
    borderDefault: "2px solid transparent"
    borderActive: "2px solid {colors.primary}"
    borderOffset: 2px
  size-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderActive: "1px solid {colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    disabledTextColor: "{colors.muted}"
    disabledTextDecoration: line-through
    disabledBackgroundColor: "{colors.canvas}"
  drop-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px {spacing.sm}"
  drop-badge-sold-out:
    backgroundColor: "{colors.mid-gray}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px {spacing.sm}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0 {spacing.lg}"
  web-texture-overlay:
    color: "{colors.primary}"
    opacity: 0.07
    blendMode: overlay
    pattern: spider-web-radial
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.ink}"
    typography: "{typography.caption}"
    linkTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The add-to-cart and checkout CTA runs neon green (#3ed660) background with near-black (#121212) text via `{typography.button-md}` in Michroma uppercase, sitting at `{rounded.xs}` with 4px corner radius so the shape reads industrial rather than friendly. On hover the fill shifts to `{colors.primary-active}` (#2bb84d), a slightly deeper green that communicates press state without leaving the voltage register. Disabled state drops to `{colors.primary-disabled}` with `{colors.muted}` text, visually receding but preserving the structural footprint so layout does not reflow when a size sells out.

**`button-secondary`** — Transparent fill with a `{colors.hairline}` (#555555) border and `{colors.ink}` text, used for secondary actions like "Save to Wishlist" or filter toggles. Active and hover states strengthen the border to `{colors.ink}` (#dedede), giving feedback through border weight rather than fill. The Michroma uppercase label at `{typography.button-md}` keeps visual parity with the primary button so the two can sit side-by-side without one appearing heavier.

### Inputs

**`text-input`** — Email capture, search, and checkout fields sit in `{colors.surface-soft}` (#191919) with a `{colors.hairline}` border, barely distinguishable from the canvas at rest so form regions feel embedded rather than interrupting. Focus state brings the border to `{colors.primary}` (#3ed660) — the only moment neon green appears in a UI control rather than a product image — making the active field unmistakable. Placeholder text runs at `{colors.muted}` (#777777); all copy uses `{typography.body-md}` Inter, keeping form labels in the transactional register separate from Michroma's hype layer.

### Navigation

**`nav-bar`** — A 64px dark bar at `{colors.canvas}` (#121212) with `{colors.hairline}` bottom border, keeping the header flush with the page canvas so it disappears rather than frames. Category labels use `{typography.nav-label}` — 12px Michroma at 0.08em tracking, uppercase — matching the brand wordmark register so the entire top band feels like a single typographic system. On mobile the nav collapses to a hamburger with a full-screen dark drawer that preserves the same Michroma label style.

### Product Card

**`product-card`** — Square 1:1 product images on `{colors.surface-card}` (#191919) with zero border radius (`{rounded.none}`) — the brand's refusal of soft corners extends to every grid cell. Title runs `{typography.title-sm}` in Inter at 500 weight; price runs `{typography.price}` in Inter 600, both in `{colors.ink}` (#dedede). On hover, a faint neon green scrim (`rgba(62,214,96,0.06)`) washes over the image, suggesting the web-texture color without overpowering the product photography. Drop badges (`drop-badge-new`, `drop-badge-sold-out`) sit as absolute overlays at the top-left of the image frame.

### Hero Banner

**`hero-banner`** — Full-bleed photography with a `rgba(18,18,18,0.55)` dark overlay that lets the near-black canvas bleed through product imagery, reinforcing the site's single tonal ground. Headline uses `{typography.display-xl}` — 56px Michroma at 0.06em tracking, uppercase — in `{colors.ink}`. The spider-web overlay component (`web-texture-overlay`) at 7% opacity and `overlay` blend mode sits beneath the headline, giving the hero a subtle web pattern without competing with product focus. Minimum 600px height on desktop; mobile drops to a 480px version with a tighter overlay to preserve legibility.

### Announcement Bar

**`announcement-bar`** — A 36px strip in `{colors.primary}` (#3ed660) that runs the full viewport width above the nav, used for drop alerts, shipping thresholds, and WORLDWIDE campaign pushes. Text is `{colors.on-primary}` (#121212) at `{typography.badge}` — 10px Michroma, 0.12em tracking, uppercase — so the copy feels like a dispatch rather than a promotional banner. The neon green strip is the single highest-saturation element on the page, readable as a status bar from a distance before any product image registers.

### Colorway Badge & Size Selector

**`colorway-badge`** — 24px circular swatches with 2px transparent border at rest; active state lifts to a 2px `{colors.primary}` (#3ed660) border with a 2px offset gap, creating a neon ring around the selected color rather than an outline fill. The neon ring treatment is borrowed from gaming UI conventions — unsurprising for a brand that runs Michroma as its primary display face. Multiple colorways can be visible simultaneously, making the swatch row a color catalog rather than a selector.

**`size-selector`** — 44px tiles at `{rounded.xs}` with `{colors.hairline}` border; selected tile upgrades to `{colors.primary}` border. Sold-out sizes use `{colors.muted}` text with `line-through` decoration and drop to `{colors.canvas}` background, visually removing the option from the grid while keeping it physically present for reference. Size labels run `{typography.button-sm}` in Michroma, matching the button register so size selection feels like a micro-action within the same hype system.

### Drop Badges

**`drop-badge-new`** — A sharp `{rounded.none}` rectangle in `{colors.primary}` (#3ed660) with `{colors.on-primary}` (#121212) Michroma badge text, overlaid on the product card image at top-left. The zero-radius chip reads as a label gun tag — functional and industrial — rather than a decorative pill. Used for new arrivals and active drop windows.

**`drop-badge-sold-out`** — Same geometry as `drop-badge-new` but `{colors.mid-gray}` (#555555) fill with `{colors.ink}` text, visually deactivating without removing the card from the grid. Keeping sold-out items visible is deliberate: in drop culture, a sold-out badge is social proof of demand, not a UX failure.

### Collection Header

**`collection-header`** — Category page headers run `{typography.display-md}` (32px Michroma uppercase) in `{colors.ink}` against `{colors.canvas}`, with a `{colors.hairline}` bottom border marking the transition to the product grid. No hero imagery at collection level — the headline and filter bar carry the full load, keeping the focus on volume of product rather than editorial staging.

### Spider Web Overlay

**`web-texture-overlay`** — A decorative SVG spider-web pattern in `{colors.primary}` at 7% opacity with `overlay` blend mode, used as a background layer on hero sections and select landing modules. At this opacity level the web dissolves into a subtle radial texture rather than a legible motif — the brand signature is present without overpowering photography or text. The pattern tiles from center-out, with denser geometry at the focal point and open negative space at the edges.

### Footer

**`footer`** — `{colors.surface-soft}` (#191919) background lifts the footer 1-stop above the canvas, creating a section break without a dramatic contrast step. Link text runs `{colors.ink}` (#dedede) at `{typography.body-sm}` Inter; legal copy and social handles use `{colors.muted}` (#777777) at `{typography.caption}`. A `{colors.hairline}` top border at 1px marks the footer boundary. No logo lockup or hero treatment — the footer is a utility region that the brand deliberately keeps understated relative to the high-voltage product grid above it.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen dark drawer; hero drops to 480px min-height; announcement bar wraps to two lines if needed; size selector tiles wrap to a two-column grid |
| Tablet | 744–1128px | Two-column product grid; nav expands to show top-level Michroma labels inline; hero returns to 520px min-height; announcement bar restores single line |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav with hover dropdowns; hero at 600px min-height with full web-texture overlay; collection header expands padding |
| Wide | > 1440px | Grid expands to five columns max; content container caps at 1440px with centered layout; announcement bar scrolls marquee text on wide viewports to fill horizontal space |

### Touch Targets

- All size-selector tiles minimum 44×44px
- Colorway badge tap area padded to minimum 36×36px via surrounding invisible hit zone
- Nav hamburger minimum 44×44px
- Button-primary and button-secondary minimum 48px height maintained across breakpoints
- Footer links padded to minimum 44px vertical tap height on mobile

### Collapsing Strategy

- Product grid: 1-col (mobile) → 2-col (tablet) → 4-col (desktop) → 5-col (wide)
- Navigation: hamburger drawer (mobile) → inline Michroma labels (tablet+)
- Hero headline: `display-xl` 56px scales down to `display-md` 32px on mobile
- Announcement bar: single line on tablet+; wraps to double line on mobile if copy exceeds viewport
- Size selector: wraps naturally; tiles maintain fixed width and wrap to new rows
- Footer: single-column stacked links on mobile; two- to three-column grid on desktop
- Collection filter bar: collapses to a "Filters" pill that opens a bottom-sheet drawer on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- SP5DER's signature hot pink and electric purple colorways (widely visible in product photography) did not appear in the extracted hex palette — these colorway hues are product-level, not site-chrome; coding agents should not assume a fixed pink or purple brand color from this file
- Exact Michroma font weight availability is unclear (the face is a single-weight geometric); `fontWeight: 400` used throughout but the face may only render one optical weight
- Hover animation timing and web-texture parallax behavior not extractable from static scan; motion values are unspecified
- Nav dropdown structure and category taxonomy not captured; labels like "Hoodies," "Tees," "Accessories" assumed but not confirmed from extraction
- Mobile drawer transition style (slide vs. fade) and overlay opacity not determined
- Exact grid gutter widths at each breakpoint not extracted; standard 16px gutter assumed
- Meta theme-color was not set, so browser chrome color on mobile is unspecified; dark (`#121212`) assumed
