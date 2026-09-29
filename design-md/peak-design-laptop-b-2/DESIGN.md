---
version: alpha
name: "Peak Design"
source_url: "https://www.peakdesign.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The darkest value in Peak Design's extracted palette — #1a211e, a green-black that reads like submerged forest canopy — is not a design neutral but the structural foundation of the brand's UI. It dominates full-bleed hero sections, the navigation shelf, and footer, creating a dark-studio surround where products emerge from shadow rather than sit on a white shelf. The primary action color is sage green (#407961): measured enough to sidestep the urgency of a retail red, specific enough to signal that the brand's currency is field-tested hardware and long-carry ergonomics rather than seasonal taste. Lighter values — #e6e9e8 and #eef1f0 — appear in product-card backgrounds and page canvas, providing the neutral airspace that a technically dense bag catalog needs to remain legible.

  Type runs in Bryant, a geometric grotesque with subtly warm proportions that prevents the utilitarian palette from reading as hostile. Display moments reach for the Exposure family (Exposure-10, Exposure-50), opening letter-spacing and dropping weight in editorial headers — a callout register rather than a headline hammer. Body copy at 16px stays at regular weight and trusts numbered feature callouts and close-up material photography to carry the narrative.

  Corner radii are minimal to nonexistent: buttons use {rounded.xs} and cards use {rounded.sm} at most, mirroring the mechanical precision of aircraft-aluminum clasps and weatherproof buckles. Product cards show one clean image, a product name, a horizontal color-swatch strip at {spacing.xs} gap, and price — no aggressive upsell layering. Destructive and alert states pull from #cc2e39; contextual colorway accents (#189cc5 blue, #4a69d4 indigo, #8164bf violet, #e9a93f amber, #efdbd2 bone) appear as swatch-picker markers and badge tints rather than structural UI hues. The palette's breadth reflects a product truth: Peak Design builds the same bag system in a dozen colorways, and the UI's job is to surface that range without visual cacophony.

colors:
  primary: "#407961"
  primary-active: "#008464"
  primary-disabled: "#9ea790"
  primary-dark: "#1a211e"
  ink: "#0c0c0c"
  body: "#484848"
  muted: "#606562"
  muted-soft: "#b8bcba"
  hairline: "#d7dad8"
  hairline-soft: "#e6e9e8"
  canvas: "#eef1f0"
  surface-soft: "#e6e9e8"
  surface-card: "#f9f9f9"
  on-primary: "#eef1f0"
  on-dark: "#eef1f0"
  alert: "#cc2e39"
  accent-blue: "#189cc5"
  accent-indigo: "#4a69d4"
  accent-violet: "#8164bf"
  accent-amber: "#e9a93f"
  accent-bone: "#efdbd2"
  accent-sage-pale: "#9ea790"
  scrim: "#101010"

typography:
  display-xl:
    fontFamily: "'Exposure-10', 'Exposure-10 Fallback', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Exposure-10', 'Exposure-10 Fallback', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Exposure-10', 'Exposure-10 Fallback', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Bryant', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Bryant', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Bryant', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Bryant', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Bryant', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  nav-label:
    fontFamily: "'Bryant', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.04em
    textTransform: uppercase
  spec-label:
    fontFamily: "'Bryant', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "'Bryant', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.04em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Bryant', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  price-display:
    fontFamily: "'Bryant', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-ghost-light:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    border: "1.5px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-dark:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1.5px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-label}"
    height: 60px
    logoHeight: 28px
    borderBottom: "none"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "4/3"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    nameTypography: "{typography.title-sm}"
    nameColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    swatchSize: 16px
    swatchGap: "{spacing.xs}"
    swatchBorderRadius: "{rounded.full}"
  hero-dark:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    paddingY: "{spacing.section}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaVariant: "button-ghost-light"
  hero-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    paddingY: "{spacing.section}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaVariant: "button-primary"
  feature-badge:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sale-badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-dark}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  color-swatch-picker:
    swatchSize: 20px
    swatchBorderRadius: "{rounded.full}"
    activeBorderWidth: 2px
    activeBorderColor: "{colors.ink}"
    activeBorderOffset: 2px
    gap: "{spacing.xs}"
  spec-row:
    backgroundColor: "{colors.surface-soft}"
    labelColor: "{colors.muted}"
    labelTypography: "{typography.spec-label}"
    valueColor: "{colors.ink}"
    valueTypography: "{typography.body-sm}"
    paddingY: "{spacing.sm}"
    dividerColor: "{colors.hairline}"
  product-image-gallery:
    backgroundColor: "{colors.surface-soft}"
    thumbnailSize: 72px
    thumbnailActiveRing: "2px solid {colors.ink}"
    thumbnailGap: "{spacing.sm}"
    rounded: "{rounded.sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.spec-label}"
    linkTypography: "{typography.body-sm}"
    paddingY: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — The primary CTA fills with sage green (#407961) and prints text in `{colors.on-primary}` (#eef1f0) using uppercase Bryant at 14px with 0.04em tracking. Corners land at `{rounded.xs}` (2px) — mechanical rather than friendly. Hover transitions to `button-primary-active` at #008464 (deeper teal); disabled state bleaches to pale sage `{colors.primary-disabled}` (#9ea790) at 60% opacity.

**`button-secondary`** — Transparent fill with a 1.5px solid `{colors.ink}` border, matching height and padding to `button-primary` for consistent row pairing on light surfaces. Intended for secondary actions where sage would compete with a nearby primary.

**`button-ghost-light`** — The dark-section counterpart: same shape and typography but border and text flip to `{colors.on-dark}` (#eef1f0), used inside `hero-dark` blocks where an ink border would be invisible against #1a211e.

**`button-dark`** — A solid `{colors.primary-dark}` (#1a211e) fill button for editorial or overlay contexts requiring a CTA darker than the sage primary. Text in `{colors.on-dark}`.

### Navigation

**`nav-bar`** — A 60px shelf in `{colors.primary-dark}` (#1a211e) holds the wordmark at left, a condensed horizontal category list at center, and an icon cluster (search, account, cart) at right. Labels use `{typography.nav-label}` — uppercase Bryant at 13px / 0.04em — giving the bar a field-guide register. No bottom border; the dark-to-light transition at the hero edge is the visual separator. On scroll the bar remains fixed and dark, never converting to a white or frosted-glass variant.

### Product Cards

**`product-card`** — Cards sit on `{colors.surface-card}` (#f9f9f9) with `{rounded.sm}` (4px) corners and a 4:3 image crop that favors the bag's volume over a square flat-lay. Below the image: product name in `{typography.title-sm}`, a horizontal `color-swatch-picker` strip at `{spacing.xs}` (4px) gap, then price in `{typography.price-display}` (Bryant 18px / semibold). No hover overlay or quick-add button intrudes on the card face — image shift on hover is the only interaction signal. Swatch circles are 16px diameter at `{rounded.full}` with a 2px `{colors.ink}` ring offset on the active state.

### Hero Sections

**`hero-dark`** — Full-bleed section on `{colors.primary-dark}` (#1a211e) with headline in `{typography.display-xl}` (Exposure-10, 56px, weight 400) and supporting copy in `{typography.body-md}`. The Exposure typeface at low weight and large size creates editorial contrast against Bryant's utilitarian role elsewhere. CTA uses `button-ghost-light`. Vertical padding is `{spacing.section}` (64px) per side.

**`hero-light`** — Light-canvas counterpart on `{colors.canvas}` (#eef1f0) with identical typographic scale, switching CTA to `button-primary` and text to `{colors.ink}`.

### Badges

**`feature-badge`** — Dark `{colors.primary-dark}` fill with `{colors.on-dark}` text in `{typography.spec-label}` (uppercase, 11px, 0.08em tracking) and `{rounded.xs}` corners. Applied at image corners for callouts like "NEW", "LAPTOP COMPATIBLE", and "CARRY-ON APPROVED".

**`sale-badge`** — Identical geometry to `feature-badge` but `{colors.alert}` (#cc2e39) fill. Appears in collection grids during promotional windows; never used on the same card face as `feature-badge` to avoid color collision.

### Text Input

**`text-input`** — `{rounded.xs}` corners, 1px `{colors.hairline}` border at rest, upgrading to 1.5px `{colors.ink}` on focus. Background is `{colors.canvas}` (#eef1f0) rather than pure white, softening the field against the page canvas. Placeholder in `{colors.muted}` (#606562), entered text in `{colors.ink}`.

### Spec Row

**`spec-row`** — A label/value pair row used in the product detail page's technical specification table. Label cell uses `{typography.spec-label}` in `{colors.muted}`; value cell uses `{typography.body-sm}` in `{colors.ink}`. Rows sit on `{colors.surface-soft}` with a `{colors.hairline}` divider. This is the brand's proof-of-engineering register: capacity in liters, laptop fit up to 16", material composition, and carry weight appear here with the same visual weight as product copy.

### Color Swatch Picker

**`color-swatch-picker`** — A horizontal strip of 20px circle swatches at `{rounded.full}`. Active swatch displays a 2px `{colors.ink}` ring offset 2px outward (ring-gap effect). Gap between swatches is `{spacing.xs}` (4px). System colorway values map to `colors.accent-*` tokens: bond blue (#189cc5), indigo (#4a69d4), violet (#8164bf), amber (#e9a93f), bone (#efdbd2), sage pale (#9ea790), plus product-specific custom values not enumerated in the design token set.

### Product Image Gallery

**`product-image-gallery`** — Main image panel on `{colors.surface-soft}` with `{rounded.sm}` corners. A horizontal strip of 72px thumbnails below (or beside on desktop) uses `{spacing.sm}` (8px) gaps; the active thumbnail receives a 2px `{colors.ink}` ring. No carousel dots — the thumbnail strip is the pagination indicator.

### Footer

**`footer`** — Matches nav in `{colors.primary-dark}` (#1a211e). Column headings in `{typography.spec-label}` (uppercase, `{colors.on-dark}`); links in `{typography.body-sm}` at `{colors.muted-soft}` (#b8bcba), lifting to `{colors.on-dark}` (#eef1f0) on hover. Social icon row uses 24px glyphs at `{colors.muted-soft}`. Vertical padding `{spacing.xxl}` (48px) top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero headline drops to `display-md` (36px); color swatch strip scrolls horizontally; spec rows stack label-above-value |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only (sub-menus suppressed); hero allows two-column image+text split |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav with flyout sub-menus; hero at full `display-xl` (56px); spec rows shown inline beside product image |
| Wide | > 1440px | Content max-width capped at 1440px with auto side margins; grid holds at four columns; hero image bleeds while content column stays within max-width |

### Touch Targets

- All buttons and nav items minimum 48px tall
- Color swatch circles: 20px visual with padding to 32px tap area
- Thumbnail strip items: minimum 48px tall with 8px inter-thumb gap
- Cart, search, and account icons each padded to 44×44px tap region
- Breadcrumb links minimum 32px tall on mobile

### Collapsing Strategy

- Nav: Desktop full horizontal with flyouts → Tablet top-level only → Mobile hamburger drawer on `{colors.primary-dark}` with stacked category links and icon row at bottom
- Product grid: 4 col → 2 col → 1 col; no single-column grid above mobile breakpoint
- Hero: Side-by-side text+image → Stacked (text above image) below 744px; headline scale steps down from `display-xl` to `display-md`
- Spec table: Two-column label/value inline → Full-width label-above-value stack below 744px
- Footer: Four-column link grid → Two-column → Stacked accordion with expand/collapse per section below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No pure white (#ffffff) in extracted palette; `{colors.surface-card}` assigned to #f9f9f9 (closest extracted value) — verify against actual product-card backgrounds
- Exposure-10 and Exposure-50 are likely custom/licensed display fonts; weight 400 assumed from typical editorial usage — confirm actual weight range with brand assets
- Exposure-50 variant usage context ambiguous (may be condensed, italic, or a heavier weight cut); mapped to `display-sm` as placeholder
- `meta theme-color` not set — mobile browser chrome color unconfirmed; #1a211e assumed based on nav
- Whether #e0eef2 (pale blue) and #e8e5ee (pale lavender) are page surfaces or product-specific colorway swatches is ambiguous; excluded from structural tokens
- #e2e2e2, #c0c0c0, #d1d0d0 appear in extracted palette but usage context (UI chrome vs. product imagery) could not be confirmed — not assigned to tokens
- Hover animation timing and easing curves not extractable from static analysis; 200ms ease-in-out assumed
- Cart interaction pattern (slide-out drawer vs. dedicated page) unconfirmed; drawer assumed from Shopify default behavior
- Exact heading hierarchy (h1–h4 pixel values) inferred from DTC norms; not directly measured from live DOM
