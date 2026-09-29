---
version: alpha
name: "Barton Watch Bands"
source_url: "https://www.bartonwatchbands.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Pure electric blue (#0000ff) cuts through a near-void ground — three stops of near-black at #171717, #1f1f1f, and #121212 — with the economy of a movement's indices: no decoration, every element earning its position by function alone. The primary CTA color is not a brand-softened navy or a corporate royal; it is pure CSS blue, used without apology, which turns every add-to-cart button and wizard step label into an unambiguous command against the dark canvas. A secondary blue at #3838ff handles hover and active state, shifting just enough to register as a transition without retreating from the electrical premise. The single light value in the extracted palette is #dedede — a neutral gray for body text and secondary labels — which keeps the interface readable at all breakpoints without lifting the overall mood toward warmth. Inter runs throughout: one typeface chosen for precision legibility over personality, which suits a shopping context where customers compare 18mm versus 20mm lug widths and read material durability ratings rather than absorbing brand narrative. Display sizes reach weight 700 for hierarchy, but the system earns structure through size and contrast rather than font switching. Filter chips and strap-swatch selectors use `{rounded.full}` pill and circle shapes as the one soft-edged exception in the system; primary action buttons hold at `{rounded.xs}` (4px) — the rounded/sharp contrast maps choosers as soft and actions as direct. Cards layer at #121212, slightly darker than the #171717 canvas, creating depth through near-identical tonal steps rather than drop shadows or elevation metaphors. Watch strap selection is a precision exercise: lug width in millimeters, case diameter range, buckle mechanism, material hardness class. The design system serves that exercise with dense filter chips, persistent swatch state, compatibility badges that surface watch brand and case size above lifestyle imagery, and a spec-row table format that treats dimension data as first-class content. The footer closes at `{colors.surface-card}` (#121212) without any decorative interruption.

colors:
  primary: "#0000ff"
  primary-active: "#3838ff"
  primary-disabled: "#1a1a6e"
  ink: "#dedede"
  ink-muted: "#999999"
  body: "#c0c0c0"
  muted: "#606060"
  hairline: "#2c2c2c"
  canvas: "#171717"
  surface-soft: "#1f1f1f"
  surface-card: "#121212"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-md:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-caps:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.04em
    textTransform: uppercase
  button-sm:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.04em
    textTransform: uppercase
  nav-link:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.06em
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
    padding: 12px 24px
    height: 44px
  button-primary-hover:
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
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-secondary-hover:
    border: "1px solid {colors.primary}"
    textColor: "{colors.primary}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "12px {spacing.base}"
    height: 44px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageAspect: "1/1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    border: "none"
    padding: "6px 14px"
  strap-swatch:
    size: 28px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.primary}"
    outline: "2px solid {colors.surface-card}"
    outlineOffset: "1px"
  compatibility-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  material-tag:
    backgroundColor: "transparent"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label-caps}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  spec-row:
    backgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.ink-muted}"
    valueColor: "{colors.ink}"
    padding: "10px {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  hero-block:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    headlineColor: "{colors.ink}"
    subColor: "{colors.body}"
    minHeight: 520px
  strap-finder-widget:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    stepLabelTypography: "{typography.label-caps}"
    stepLabelColor: "{colors.primary}"
    padding: "{spacing.xl}"
  review-summary:
    backgroundColor: "{colors.surface-card}"
    starColor: "{colors.primary}"
    countTypography: "{typography.body-sm}"
    scoreTypography: "{typography.display-sm}"
    rounded: "{rounded.sm}"
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  footer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    linkColor: "{colors.ink}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} 0"

## Components

### Buttons
**`button-primary`** — Electric blue (#0000ff) fill on the dark canvas creates the maximum contrast signal in the interface; the label runs Inter 600 uppercase with 0.04em tracking. Hover shifts to `{colors.primary-active}` (#3838ff), a softer blue that registers state change without abandoning the electrical premise. Disabled state uses `{colors.primary-disabled}`, a very dark blue-gray that keeps the hue family while marking unavailability. Corner radius holds at `{rounded.xs}` (4px) — just enough to avoid a purely mechanical edge.

**`button-secondary`** — Transparent background with a `{colors.hairline}` border sits comfortably against the dark canvas without competing with the primary. On hover, border and text shift to `{colors.primary}` to signal interactivity without filling with blue. Used for secondary actions like "View Details" and "Save to Wishlist."

**`button-ghost`** — Text-only in `{colors.primary}` blue, no border, no fill. Used for low-priority inline actions such as "Learn More" and "See All Reviews."

### Text Input
**`text-input`** — `{colors.surface-soft}` (#1f1f1f) fill separates the field from the `{colors.canvas}` background; border is `{colors.hairline}` at rest, shifts to `{colors.primary}` on focus. Placeholder text uses `{colors.muted}`. Height is 44px to align with button height for consistent vertical rhythm in search and filter rows.

### Navigation
**`nav-bar`** — Pinned at the viewport top at 64px, background matches `{colors.canvas}` (#171717) with a subtle `{colors.hairline}` bottom border separating it from the content zone. Brand wordmark sits left; primary strap category links, a strap-finder CTA, and cart icon sit right. Typography runs in `{typography.nav-link}` (Inter 500, 14px) — present but not heavy-handed on the dark ground.

### Product Card
**`product-card`** — `{colors.surface-card}` (#121212) background sits one tonal step below the canvas, creating lift without drop shadows. Product image occupies the top zone at 1:1 aspect ratio; below it, strap name in `{typography.title-sm}` and price in `{typography.price}` (Inter 700, 20px). A flex row of `strap-swatch` color dots appears beneath the name. A `sale-badge` in `{colors.primary}` blue overlays the image top-left corner when a discount is active.

### Filter Chips
**`filter-chip`** — Pill-shaped at `{rounded.full}`, label in `{typography.label-caps}` (11px uppercase Inter). Inactive state uses `{colors.surface-soft}` fill with `{colors.hairline}` border. Active state fills solid `{colors.primary}` blue with white text, no border needed. Used for lug width (18mm, 20mm, 22mm), material (silicone, leather, nylon, metal), buckle type, and compatible watch brand filtering across the catalog grid.

### Strap Swatch
**`strap-swatch`** — 28px filled circle showing the literal color or material impression of a strap variant. A 2px solid `{colors.primary}` ring plus a 2px `{colors.surface-card}` outline-gap appear on selection, creating a halo that clearly marks the active variant against both dark and light material swatches. Tap area expands to 40×40px on mobile via padding so the visual circle stays compact while the target stays accessible.

### Compatibility Badge
**`compatibility-badge`** — Small pill in `{typography.spec-label}` (11px uppercase) naming compatible watch brands or case diameters, e.g. "Apple Watch 45mm" or "Seiko SKX." `{colors.surface-soft}` fill, `{colors.ink-muted}` text, `{rounded.xs}` radius. Appears directly beneath the product name on the PDP to answer the fit question before a customer reads a single word of copy.

### Spec Row
**`spec-row`** — Horizontal key-value pair used in product detail specification tables: lug width, strap length, buckle type, material, thickness. Label in `{typography.spec-label}` at `{colors.ink-muted}`; value in `{typography.body-sm}` at `{colors.ink}`. `{colors.hairline}` bottom border separates rows. `{colors.surface-soft}` fill alternates optionally on even rows for scannability.

### Strap Finder Widget
**`strap-finder-widget`** — Multi-step configurator embedded in the PDP and as a standalone landing tool. Step counter and prompt labels run in `{typography.label-caps}` colored `{colors.primary}` blue to signal active progress. Outer container uses `{colors.surface-card}` with `{rounded.sm}` and a `{colors.hairline}` border, isolating it from the canvas without elevation. Steps collect watch brand, case diameter, and wrist size before surfacing a filtered strap recommendation set.

### Review Summary
**`review-summary`** — Star glyphs render in `{colors.primary}` blue rather than a conventional gold — a deliberate brand signal that blue is the sole accent voltage. Aggregate score in `{typography.display-sm}`; review count and rating distribution bars in `{typography.body-sm}` at `{colors.body}`. Container uses `{colors.surface-card}` background with `{rounded.sm}`.

### Footer
**`footer`** — `{colors.surface-card}` (#121212) background marks the page close at one tonal step below canvas. Column headings in `{typography.title-sm}`; link rows in `{typography.body-sm}`. A single `{colors.hairline}` top border is the only visual transition from the content zone above. No gradient, no illustration — just the link grid, newsletter input, and brand mark in a structured dark close.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter drawer replaces sidebar; nav collapses to hamburger + wordmark + cart; hero headline drops to `{typography.display-md}`; strap-finder widget steps stack vertically full-width |
| Tablet | 744–1128px | Two-column product grid; filter chips appear as horizontal scroll row above grid; nav shows primary category links, hamburger for secondary; hero headline at `{typography.display-md}` |
| Desktop | 1128–1440px | Three-column product grid; filter sidebar fixed at ~220px left; full nav with all category links and strap-finder CTA; hero at `{typography.display-xl}` |
| Wide | > 1440px | Layout constrained to 1440px max-width container; outer gutters fill with `{colors.canvas}`; no internal layout changes |

### Touch Targets
- `strap-swatch` circles expand tap area to 40×40px on mobile via padding; visual size stays 28px
- Filter chips maintain minimum 36px height on mobile
- Hamburger nav links expand to 48px row height in the drawer
- Add-to-cart and strap-finder primary CTAs are full-width on mobile at fixed 44px height
- Compatibility badges and material tags are display-only on mobile; no tap action required

### Collapsing Strategy
- Product filters collapse from left sidebar to a bottom sheet drawer on mobile; top chip row persists for quick lug-width and material access
- Strap compatibility table collapses to single-column label-above-value list on mobile
- Spec rows remain full-width single-column at all breakpoints; no horizontal scrolling
- Review breakdown bars scale to full container width at all breakpoints
- Footer link columns stack to single column on mobile; section headings become accordion toggles

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Interactive state colors (disabled, focus ring, error) were not directly extractable; values are logically inferred from the extracted palette range
- Specific type size and weight scale is inferred from Inter design conventions, not measured from pixel-accurate screenshots
- Star rating color shown as `{colors.primary}` blue is an inference; may render as a conventional amber/gold if loaded via JS after scrape
- Additional accent colors (error red, success green, warning amber) are not present in the extracted palette; likely exist in form validation and cart states
- Animation and transition timing values were not captured; 150–200ms ease assumed throughout
- Logo mark details (SVG geometry, wordmark weight, icon treatment) are not derivable from color and font extraction alone
- Exact nav height and filter sidebar width are estimated from conventional Shopify storefront patterns, not measured values
