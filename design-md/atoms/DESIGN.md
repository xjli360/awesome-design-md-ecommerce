---
version: alpha
name: "Atoms"
source_url: "https://atoms.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Seventeen measurements per foot, quarter-size increments from 5 to 14, a canvas stretching from #f4f4f4 to #212121 without a single warm tint: Atoms designs sneakers the way a machinist approaches tolerances, and the interface inherits that logic exactly. Helvetica Now Display carries every headline — its optical precision at large sizes reads almost clinical, a deliberate choice over the humanist alternatives in the same stack. Where emphasis demands a different temperature, VC Garamond Condensed appears as editorial counter-weight, and PT Mono surfaces for data-dense labels — size charts, measurement tables, the quarter-unit selectors that are the brand's signature differentiator. The typeface pairing is rare: a grotesque-meets-condensed-serif combination that signals craft without warmth.

  The palette is an exercise in controlled restraint. Off-white (#f4f4f4) serves as the primary canvas — not pure white, which reads as sterile, but warm-adjacent without committing to warmth. Near-black (#212121) anchors every call-to-action and body-text element. The most distinctive chromatic arrivals in the system are colorway echoes, not branding fixtures: electric lime (#c1f651) signals an active product drop; golden (#ffcf2a) and amber (#ffa621) mark seasonal colorways. A muted slate-lavender (#676986) functions as quiet UI state color — hover transitions, secondary labels. Borders and dividers live in the gray band between #dedede and #e5e5e5, giving grid lines enough weight to read without interrupting the clean field.

  Corners stay close to square: {rounded.xs} at 2px governs buttons and inputs; {rounded.sm} at 4px softens product cards and size chips. The precision metaphor extends to spacing — a tight 4px base unit builds up in strict multiples, and nothing floats between a defined step. The size-selector component — a horizontal row of quarter-unit chips (5, 5.25, 5.5…) rendered in PT Mono — is the most brand-specific UI pattern, switching to {colors.primary} fill on selection. Touch targets stay generous at 44px minimum despite the dense sizing grid, ensuring even 10.75 chips are tappable.

  Imagery runs full-bleed and white-saturated — shoe photography against near-white fields, shadows so diffuse they read as drawings rather than photographs. Navigation is minimal: wordmark left, search right, cart count in monospace numerals. Product pages prioritize the measurement table and size-selector over promotional copy, trusting engineering data to close the sale more than any tagline would.

colors:
  primary: "#212121"
  primary-active: "#111827"
  primary-disabled: "#878787"
  ink: "#212121"
  body: "#374151"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  canvas: "#f4f4f4"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#f4f4f4"
  accent-lime: "#c1f651"
  accent-gold: "#ffcf2a"
  accent-amber: "#ffa621"
  accent-slate: "#676986"
  accent-dusty: "#c9d4d9"
  divider: "#dedede"
  scrim: "#212121"

typography:
  display-xl:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: -0.2px
  editorial:
    fontFamily: "'VC Garamond Condensed', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  mono-label:
    fontFamily: "'PT Mono', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  mono-data:
    fontFamily: "'PT Mono', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  size-chip:
    fontFamily: "'PT Mono', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  price:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    padding: 14px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    focusBorderColor: "{colors.primary}"
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    cartCountTypography: "{typography.mono-label}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1:1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.base}"
  size-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.size-chip}"
    padding: 8px 10px
    minWidth: 52px
    height: 36px
  size-chip-selected:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    typography: "{typography.size-chip}"
  size-chip-unavailable:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
    textDecoration: line-through
    rounded: "{rounded.sm}"
    typography: "{typography.size-chip}"
  color-swatch:
    width: 24px
    height: 24px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.primary}"
    selectedOutlineGap: 2px
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: button-primary
    imagePosition: right
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 560px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 2px 6px
    textTransform: uppercase
    letterSpacing: 0.5px
  badge-colorway:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 2px 6px
    textTransform: uppercase
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: 8px {spacing.base}
    height: 36px
    textAlign: center
  product-measurement-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headerTypography: "{typography.mono-label}"
    cellTypography: "{typography.mono-data}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  editorial-callout:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.editorial}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.accent-slate}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    columns: 4

## Components

### Buttons

**`button-primary`** — Near-black (#212121) fill with off-white (#f4f4f4) text, 2px radius, all-caps with 0.8px letter-spacing. Height 44px keeps a solid touch target while the near-zero rounding holds the clinical geometry. Hover state deepens to #111827; disabled falls back to #878787 fill with muted text.

**`button-secondary`** — Transparent fill, 1px #212121 border, near-black text. Identical uppercase tracking and 44px height as primary, with no fill to distinguish by negative space alone. Used for secondary CTAs (add to wishlist, view size guide) where hierarchy must read without color.

**`button-ghost`** — No border, no fill, underlined near-black text in `button-sm` scale. Reserved for low-priority in-page links within product descriptions and return policy blocks where a bordered element would interrupt the copy flow.

### Size Selector

**`size-chip`** and variants — The brand's defining UI pattern. Quarter-size increments (5, 5.25, 5.5, 5.75…) render as PT Mono chips in a horizontally scrollable row. Default state is #f4f4f4 background with a 1px #e5e5e5 border at 4px radius. Selected state flips to full #212121 fill with #f4f4f4 text. Unavailable sizes retain the default border but gray the text to #9ca3af with a strikethrough. Chips hold a 52px minimum width so four-character values like 10.75 never wrap. The row scrolls horizontally on all viewports rather than wrapping to preserve the linear scale reading.

### Navigation

**`nav-bar`** — 60px tall, #f4f4f4 background, 1px #e5e5e5 bottom border. Wordmark is left-anchored; search icon and cart are right-anchored with the cart item count rendered in PT Mono to match the precision aesthetic. Top-level category links in Helvetica Now Display 14px weight 400 — no bold, no underline, no dropdown mega-menu.

### Product Card

**`product-card`** — Square 1:1 image on #f5f5f5 background, 4px radius. Title in `title-sm`, price in `price` style directly below. Color swatches appear as 24px `color-swatch` circles under the title row. Cards are static — no hover reveal, no quick-add overlay; all purchase interaction lives on the PDP.

### Hero

**`hero`** — Full-width, 560px minimum height, #f4f4f4 canvas. Display-xl headline sits left-aligned in the left column; shoe photography occupies the right half at natural bleed with no scrim or overlay. On mobile the layout stacks vertically with image above and headline below, and a `button-primary` CTA centered under the text.

### Color Swatch

**`color-swatch`** — 24px filled circles in a horizontal row. The selected swatch gains a 2px #212121 border with a 2px transparent gap between the circle edge and the border ring, creating a halo effect. Colorway names surface on hover or tap via a `mono-label` tooltip below the row.

### Badges

**`badge-new`** — Zero-radius rectangle, all-caps 12px caption, #212121 fill, off-white text. Appears in the top-left corner of product card images for new arrivals. **`badge-colorway`** — Same geometry with electric lime (#c1f651) fill and near-black text; used when a colorway has just dropped or is marked as a limited edition.

### Announcement Bar

**`announcement-bar`** — Full-width 36px bar in #212121 with off-white caption text, centered, all-caps with 0.5px letter-spacing. Single message only — no rotating carousel — covering free shipping thresholds, new drop dates, or waitlist openings.

### Product Measurement Table

**`product-measurement-table`** — #f5f5f5 background, 1px #e5e5e5 grid lines, 4px radius on the container. Column headers in PT Mono 12px; cell data in PT Mono 14px. Maps foot length in millimeters to the corresponding quarter-size, reinforcing the brand's precision positioning directly in the purchase flow.

### Editorial Callout

**`editorial-callout`** — Full-width text section on #f4f4f4 canvas using VC Garamond Condensed at 40px for the headline, body in Helvetica Now Display 16px. Accent underline or rule in #676986. Appears between product collections as a brand-voice break, typically one short declarative sentence about fit philosophy.

### Footer

**`footer`** — #212121 background, four columns on desktop. Column headings in `title-sm` (Helvetica Now Display 14px weight 500); links in `body-sm` weight 400 at #e5e5e5. Copyright and legal in `caption`. No large logo mark — just the wordmark reproduced small in off-white.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; size-chip row scrolls horizontally without wrapping; hero stacks image above headline; nav collapses to hamburger icon + centered wordmark |
| Tablet | 744–1128px | Two-column product grid; hero side-by-side with reduced padding; nav shows top-level links with no icons |
| Desktop | 1128–1440px | Three-column product grid; full nav bar at 60px; hero at 560px min-height with full typography scale |
| Wide | > 1440px | Max-width container ~1320px centered; four-column product grid; hero image scales up proportionally within the fixed-width container |

### Touch Targets

- All size-chip and color-swatch elements maintain a minimum 44×44px touch target via padding, even when the visible chip is smaller
- Nav icons (search, cart) hit 44×44px tap areas
- Quantity stepper controls on PDP: 44×44px per button
- Footer accordion triggers on mobile: full-width 44px tap rows

### Collapsing Strategy

- Footer four-column grid collapses to a single-column accordion at < 744px; each section heading is a tap-to-expand toggle
- Announcement bar remains single-line at all widths; long messages truncate with ellipsis rather than wrapping
- Product measurement table scrolls horizontally on mobile inside a scroll container; the first column (size label) sticks left
- Editorial callout reduces editorial font from 40px to 28px (`display-md`) on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border-radius not confirmed from extraction — 2px (`rounded.xs`) inferred from brand's near-square aesthetic; may be 0px in production
- Helvetica Now Display variable weight range not confirmed; 400 and 500 observed in font stack hints; bolder weights (600+) may exist for display contexts
- VC Garamond Condensed usage is confirmed in the font stack but specific component assignments are inferred, not extracted
- Accent colors (#c1f651, #ffcf2a, #ffa621) appear as product colorway references; their roles as UI tokens versus purely decorative/product palette are unconfirmed
- #2563eb and #5468ff appear in extracted colors but their UI role is unclear — likely Shopify UI defaults or link states, not Atoms brand colors
- Nav height (60px) estimated; not directly measured from extraction
- Animation and transition specs (hover easing, duration) not available from extraction
- Cart drawer / mini-cart design not captured
- Dark mode or alternate theme variants not observed
- surface-card (#ffffff) inferred as standard practice; not directly confirmed from the extracted palette
