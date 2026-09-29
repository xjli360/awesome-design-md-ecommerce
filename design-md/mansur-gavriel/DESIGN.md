---
version: alpha
name: "Mansur Gavriel"
source_url: "https://mansurgavriel.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Violet at #a45cec sits at the center of gravity — an unusual commitment for a brand that otherwise communicates through restraint, near-white surfaces (#fefefe), and the quiet authority of Supreme-LL set at low weights. The design operates as a tension between that single saturated decision and the rectilinear austerity surrounding it: sharp corners on every interactive element, no border radii on buttons or inputs, generous whitespace between modules that reads more like a printed lookbook than a commerce page. A warm off-white surface (#e6e6dc) backs editorial sections, stepping just far enough from pure white to register as a material choice. The palette carries additional voltage in a saturated red (#e44434) and deep navy (#000f9f), appearing as accent signals in badge and campaign contexts — color-blocking logic that mirrors the brand's product line, where bold hue meets architectural proportion. Gray runs in five increments from #888888 through #646464 to #121212, each step carrying a different editorial function: body text, muted labels, ink — never a colored highlight.

  Navigation presents at 13px/400-weight, deliberately underscaled so the wordmark holds the room alone. CTAs break the silence with full-saturation violet at 48px height, their uppercase tracking (0.08em) matching the label-level type that annotates filters and badges throughout. Product photography bleeds to edge on borderless cards; the `{colors.surface-card}` ground dissolves behind imagery so that color and form carry without frame interference. The footer inverts entirely to `{colors.ink}` (#121212), pulling white type from that dark field and anchoring the page with the same decisive contrast that opens on the announcement bar above. Spacing between editorial modules holds at `{spacing.section}` — 64px — forcing deliberate pauses that resist scroll momentum. The brand's digital geometry is emphatically rectilinear: luxury expressed through proportion and interval rather than the softened curves that dominate the broader apparel category.

colors:
  primary: "#a45cec"
  primary-active: "#8b3fd4"
  primary-disabled: "#d9b3f5"
  accent-red: "#e44434"
  accent-navy: "#000f9f"
  ink: "#121212"
  body: "#646464"
  muted: "#787878"
  muted-light: "#888888"
  hairline: "#dedede"
  canvas: "#fefefe"
  surface-soft: "#e6e6dc"
  surface-card: "#fefefe"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Supreme-LL', 'Supreme', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Supreme-LL', 'Supreme', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Supreme-LL', 'Supreme', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Supreme-LL', 'Supreme', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Supreme-LL', 'Supreme', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.05em
    textTransform: uppercase
  body-md:
    fontFamily: "'Supreme-LL', 'Supreme', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Supreme-LL', 'Supreme', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Supreme-LL', 'Supreme', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  button-md:
    fontFamily: "'Supreme-LL', 'Supreme', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Supreme-LL', 'Supreme', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-label:
    fontFamily: "'Supreme-LL', 'Supreme', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  price-display:
    fontFamily: "'Supreme-LL', 'Supreme', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  label-uppercase:
    fontFamily: "'Supreme-LL', 'Supreme', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase

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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: none
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 80vh
    padding: "{spacing.xxl}"
  editorial-grid:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    captionTypography: "{typography.caption}"
    columns: 2
    gap: "{spacing.lg}"
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    activeTextColor: "{colors.primary}"
    activeBorderBottom: "1px solid {colors.primary}"
    gap: "{spacing.lg}"
  size-selector:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    backgroundSelected: "{colors.ink}"
    textColorSelected: "{colors.on-dark}"
    width: 40px
    height: 40px
  color-swatch:
    rounded: "{rounded.full}"
    size: 16px
    borderSelected: "1px solid {colors.ink}"
    offset: 2px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    height: 36px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    labelTypography: "{typography.label-uppercase}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Full-saturation violet (#a45cec) fill with `{rounded.none}` — no softening of corners anywhere on the interactive layer. Label runs in `{typography.button-md}` at 13px/500-weight uppercase with 0.08em letter-spacing, ensuring the call-to-action registers as a directive rather than an invitation. Active state deepens to `{colors.primary-active}` (#8b3fd4); disabled state retreats to `{colors.primary-disabled}`, maintaining the 48px height baseline across all states.

**`button-secondary`** — Transparent fill with 1px `{colors.ink}` border, padding inset by 1px to preserve height parity with the primary. On hover, the border inverts to a solid ink fill with `{colors.on-dark}` text — a binary switch rather than a gradual fade.

**`button-ghost`** — No border, no fill; bare label in `{typography.button-sm}` for "View All" links and editorial navigation where a full button would interrupt module flow.

### Text Input

**`text-input`** — Square corners (`{rounded.none}`), 1px `{colors.hairline}` border stepping to `{colors.ink}` on focus. The transition is the only animated state change in the field; placeholder in `{colors.muted}` recedes cleanly. Used across search, email capture, and checkout.

### Navigation

**`nav-bar`** — 56px tall on a `{colors.canvas}` ground, separated from content by a 1px `{colors.hairline}` underline. Links use `{typography.nav-label}` at 13px/400-weight — deliberately light against the wordmark's authority. Cart and search icons sit right-aligned with no visible badge count on default state; a slide-down drawer handles mega-menu content without full-page reflow.

### Product Card

**`product-card`** — Borderless, no shadow or elevation; the 3:4 portrait image bleeds to the card edge so the `{colors.surface-card}` ground disappears behind photography. Below the image: name in `{typography.body-sm}` and price in `{typography.price-display}`, both `{colors.ink}`. Color swatches render as 16px circles beneath the name using the `color-swatch` component. No hover zoom animation — the brand relies on editorial stillness.

### Hero Banner

**`hero-banner`** — Full-viewport-width editorial block backed by `{colors.surface-soft}` (#e6e6dc) as the default warm field. Headline at `{typography.display-xl}` (48px/300-weight) keeps scale monumental without heaviness; a single CTA button sits below, typically `button-primary`. Campaign pages swap the backing for full-bleed photography, dropping the headline over the image with no scrim.

### Editorial Grid

**`editorial-grid`** — Two-column module on desktop used for lookbook and campaign spreads. Captions in `{typography.caption}` at 11px/`{colors.body}`, positioned below each image with `{spacing.lg}` gap between columns. The combination of low-weight caption type and generous inter-module `{spacing.section}` (64px) reproduces print-lookbook pacing in the scroll context.

### Collection Filter

**`collection-filter`** — Horizontal strip of category labels using `{typography.label-uppercase}` — 10px, 0.12em tracking, uppercase. Active selection adds a 1px `{colors.primary}` underline and shifts the label to violet — the only place the primary appears outside CTA contexts on collection pages. Inactive labels stay in `{colors.ink}`.

### Size Selector

**`size-selector`** — 40×40px flat squares with no rounding, `{colors.hairline}` border at rest. Selected state fills to `{colors.ink}` with `{colors.on-dark}` reversed text. Sold-out sizes carry a diagonal strike-through line in `{colors.hairline}` and do not receive the selected fill.

### Badges

**`badge-new`** — Violet (`{colors.primary}`) fill, flat rectangle with 2px × 6px padding, `{typography.label-uppercase}`. Overlays the top-left corner of product cards for seasonal drops and new arrivals.

**`badge-sale`** — Identical geometry to badge-new, `{colors.accent-red}` (#e44434) fill. The red creates sufficient contrast against photography without introducing a third interaction pattern.

### Color Swatch

**`color-swatch`** — 16px circle (`{rounded.full}`) representing a colorway option on product cards and PDPs. Selected state: 1px `{colors.ink}` ring with 2px offset gap — the ring sits outside the swatch circle rather than overlapping it, keeping the underlying hue fully visible.

### Announcement Bar

**`announcement-bar`** — 36px violet (`{colors.primary}`) band pinned above the nav; the brand's most saturated surface, setting tone before the user reaches any product. Copy in `{typography.label-uppercase}`, `{colors.on-primary}` white. A single centered line; no dismiss control on default state.

### Footer

**`footer`** — Full-width `{colors.ink}` (#121212) band reversing all type to `{colors.on-dark}` white. Section headers in `{typography.label-uppercase}`; navigation links in `{typography.body-sm}`. Four-column grid on desktop. The footer is the only place the brand commits fully to dark ground; it anchors the violet-on-white page with a definitive close.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + cart icon; hero reduces to 50vh; collection filter becomes horizontal scroll strip with fade-out edge; footer stacks into labeled accordions |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level labels inline with hamburger for sub-navigation; hero at 65vh; filter bar visible above grid |
| Desktop | 1128–1440px | Three- or four-column product grid depending on collection density; full nav with hover dropdowns; hero at 80vh; editorial grid at 2-up |
| Wide | > 1440px | Layout max-width caps at 1440px and centers; editorial modules gain symmetric left-right margin; hero image crops to fill without aspect-ratio stretch |

### Touch Targets

- Buttons minimum 48px height across all variants
- Size selector cells 40×40px visible; tap area extends to 44×44px via invisible padding
- Navigation icons 44×44px tap area minimum with optical centering
- Color swatches 16px visible circle, 32px tap area via padding on all sides
- Filter labels minimum 36px tap height with vertical padding

### Collapsing Strategy

- Footer four-column grid collapses to labeled accordions on mobile; category label acts as toggle, links expand below
- Collection filter transitions from horizontal tab-bar to a modal "Filter / Sort" trigger on mobile, keeping the grid edge-to-edge
- Product card names truncate to one line on mobile grid; full name visible on PDP
- Editorial two-column grid collapses to full-width single-image stack on mobile with caption below each image
- Announcement bar persists at full width on all breakpoints; text truncates with ellipsis if copy exceeds single line

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; announcement bar and primary CTA color assumptions derive from palette distinctiveness ranking
- Supreme-LL weight range not confirmed from extraction — 300/400/500 assumed from luxury apparel norms; the variable font may offer a wider axis range
- Hover transition durations and easing curves not extractable from static analysis; no animation tokens defined
- Exact nav height (56px) is an estimate based on Shopify theme conventions; may differ from live measurement
- #007aff in the extracted palette closely matches iOS system blue and is likely a Shopify UI artifact or browser default; excluded from brand tokens
- Mega-menu / dropdown structure not confirmed; component omitted pending live inspection
- PDP image gallery behavior (swipe, zoom, thumbnail rail), size guide modal, and accordion tab layout not modeled due to insufficient extraction depth
- Dark mode not observed on site; no dark-mode token variants defined
- Exact letter-spacing values for Supreme-LL display sizes not confirmed; values interpolated from visible rendering proportions
