---
version: alpha
name: "NovelKeys"
source_url: "https://novelkeys.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Helvetica Rounded's soft-cornered letterforms are the brand's most precise design decision — the same radius that rounds a Cherry-profile keycap's legends rounds every headline and CTA on screen, making the typography literally mirror the physical product. Four overlapping reds (#ca2929, #b52424, #d51f24, #ce272d) crowd the extracted palette not from inconsistency but from the demands of a drop-culture shop where sold-out, low-stock, and error states each need distinct visual weight at a glance. Against this functional riot of reds, the olive-sage accent (#a1ad62) lands unexpectedly — warm and earthy, the kind of color that appears on artisan keycap colorway renders before it reaches retail interfaces. The confirmed meta theme-color (#0099db) anchors primary CTAs and active states with a saturated cyan-blue that holds on both the #f0f0f0 section bands and the #231f20 near-black footer. Body copy and product specs run on Neuzeit Office Pro — an upright humanist sans that stays legible at catalog density (14px product names, 12px switch specs) — while Helvetica Rounded carries all headlines and interactive labels, creating a deliberate two-family system where rounded forms own identity and interaction, and the office sans owns information. Corner radius stays controlled — `{rounded.xs}` on stock badges and swatch dots, `{rounded.sm}` on inputs and product cards, never approaching pill. The canvas alternates between pure white product sections and #f0f0f0 bands to chunk a long-scroll Shopify layout into scannable zones without hard dividers. Stock state is the dominant UI pattern: greens (#00a651, #49a339) signal available inventory, the reds gate checkout entry, and badge-level type at 11px bold keeps status readable without competing with product photography. The mid-blue navy (#3e5c9a) serves as a collection-tab accent, lifting category navigation above single-color storefront monotony.

colors:
  primary: "#0099db"
  primary-active: "#007ab5"
  primary-disabled: "#99d5ef"
  ink: "#231f20"
  body: "#2a2a2a"
  muted: "#bbbbbb"
  hairline: "#e5e5e9"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-olive: "#a1ad62"
  accent-navy: "#3e5c9a"
  accent-sky: "#67b8cd"
  stock-in: "#00a651"
  stock-in-alt: "#49a339"
  stock-out: "#d51f24"
  stock-low: "#ca2929"
  error: "#b52424"

typography:
  display-xl:
    fontFamily: "'Helvetica Rounded', 'HelveticaRoundedLTWXX-Black', sans-serif"
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Rounded', 'HelveticaRoundedLTWXX-Bold', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Helvetica Rounded', 'HelveticaRoundedLTWXX-Bold', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Rounded', 'HelveticaRoundedLTWXX-Bold', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Neuzeit Office Pro', 'NeuzeitOfficeSRPro-Regular', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Neuzeit Office Pro', 'NeuzeitOfficeSRPro-Regular', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Neuzeit Office Pro', 'NeuzeitOfficeSRPro-Regular', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Rounded', 'HelveticaRoundedLTWXX-Bold', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Helvetica Rounded', 'HelveticaRoundedLTWXX-Bold', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Helvetica Rounded', 'HelveticaRoundedLTWXX-Bold', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Rounded', 'HelveticaRoundedLTWXX-Bold', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "'Helvetica Rounded', 'HelveticaRoundedLTWXX-Black', sans-serif"
    fontSize: 18px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'Neuzeit Office Pro', 'NeuzeitOfficeSRPro-Regular', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px

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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    typography: "{typography.body-md}"
    focusBorder: "2px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    cartIconColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    imageAspect: "1/1"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
    hoverElevation: "0 4px 12px rgba(0,0,0,0.10)"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    minHeight: 520px
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaButton: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  badge-in-stock:
    backgroundColor: "{colors.stock-in}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.stock-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-low-stock:
    backgroundColor: "{colors.stock-low}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-olive}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  stock-indicator:
    in-stock:
      color: "{colors.stock-in}"
      typography: "{typography.caption}"
    low-stock:
      color: "{colors.stock-low}"
      typography: "{typography.caption}"
    out-of-stock:
      color: "{colors.stock-out}"
      typography: "{typography.caption}"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    selectedRing: "2px solid {colors.ink}"
    selectedRingOffset: 2px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    iconColor: "{colors.muted}"
    height: 40px
    focusBorder: "1px solid {colors.primary}"
  collection-tab:
    activeColor: "{colors.primary}"
    activeTypography: "{typography.title-sm}"
    activeBorderBottom: "2px solid {colors.primary}"
    inactiveColor: "{colors.muted}"
    inactiveTypography: "{typography.title-sm}"
    backgroundColor: "{colors.canvas}"
  drop-countdown:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    digitTypography: "{typography.display-md}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg} {spacing.xl}"
    accentColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} 0"
    accentColor: "{colors.primary}"

---

## Components

### Buttons

**`button-primary`** — Solid #0099db fill, white Helvetica Rounded Bold label at 15px, 44px tall, `{rounded.sm}` corners. Darkens to #007ab5 on press; disabled state fades fill to #99d5ef while keeping white text. Used for add-to-cart, checkout, and modal confirmation actions.

**`button-secondary`** — White canvas background with a 2px #0099db border and cyan text, matching primary height (44px) and corner radius. Background lifts to `{colors.surface-soft}` on hover; border and text shift to #007ab5 on press. Used for "Notify Me", filter resets, and secondary confirmation paths.

**`button-tertiary`** — Transparent, ink-colored Helvetica Rounded Bold at 13px. No border or fill; used for dismissal links, "Learn More", and inline text-link-style actions where visual mass would crowd a dense layout.

### Text Inputs

**`text-input`** — Canvas background, 1px `{colors.hairline}` border, `{rounded.sm}` radius, 10px vertical / 14px horizontal padding. Placeholder in `{colors.muted}`. Focus ring upgrades to 2px `{colors.primary}` border with no layout shift. Used across search, cart notes, and all Shopify checkout fields.

### Navigation

**`nav-bar`** — White bar, 64px tall, 1px `{colors.hairline}` bottom border. Logo left-anchored in `{colors.ink}`; nav links in Helvetica Rounded Bold 14px centered; cart and account icons right-anchored. Collapses to hamburger plus remaining icons at mobile widths, with a full-height slide-out drawer for category navigation.

**`collection-tab`** — Horizontal tab strip pinned below the collection header. Active tab renders `{colors.primary}` label with a 2px solid bottom border underline; inactive tabs use `{colors.muted}` with no fill change. `{typography.title-sm}` throughout. On mobile the strip scrolls horizontally rather than collapsing to a dropdown.

### Product Cards

**`product-card`** — 1px `{colors.hairline}` border, `{rounded.sm}` corners, square 1:1 image on a `{colors.surface-soft}` background swatch. Title in `{typography.title-sm}`, price in `{typography.price}` (Helvetica Rounded Black 18px), variant summary in `{typography.caption}`. Stock badge floats top-left over the image. On hover the card lifts with a soft diffuse shadow (0 4px 12px rgba(0,0,0,0.10)) with no border change.

### Stock & Status Badges

**`badge-in-stock`** / **`badge-out-of-stock`** / **`badge-low-stock`** — Three badge variants at 11px Helvetica Rounded Bold uppercase, `{rounded.xs}` corners, 3px/8px padding. Fills: green (#00a651), bright-red (#d51f24), dark-red (#ca2929). All use white text. Overlay the product card image at top-left and appear inline on PDPs below the product title.

**`badge-sale`** — Olive-sage (#a1ad62) fill, same typographic spec as stock badges. Signals markdown pricing without competing with the red stock signals — the hue distance is wide enough to avoid confusion at a glance.

**`badge-new`** — Primary blue (#0099db) fill, same spec. Used for new arrivals and recently-launched group buy products; communicates novelty rather than urgency.

### Stock Indicator (PDP Inline)

**`stock-indicator`** — Text-only status line rendered below the add-to-cart button using `{typography.caption}` (Neuzeit Office Pro 12px). Green for in-stock, dark-red for low-stock, bright-red for out-of-stock. No badge shape — the inline text format keeps the indicator subordinate to the CTA without adding visual clutter on a dense product detail page.

### Color Swatches

**`color-swatch`** — 24px diameter circles, `{rounded.full}`, arranged in a horizontal row beneath product titles on cards and PDPs. Selected swatch gains a 2px `{colors.ink}` ring with a 2px gap offset to float the ring visually clear of the fill. Out-of-stock swatches render with a diagonal pseudo-element strike-through. Touch target expands to 40px via padding even though the visible dot is 24px.

### Search

**`search-bar`** — 40px tall input on `{colors.surface-soft}` with a 1px `{colors.hairline}` border, `{rounded.sm}` corners, leading magnifier icon in `{colors.muted}`. Focus upgrades to 1px `{colors.primary}` border. On mobile, activating the search input expands to a full-width overlay with auto-focus and a predictive results dropdown.

### Hero

**`hero`** — Full-bleed dark (#231f20) banner, minimum 520px tall, for featured drops and homepage campaigns. Headline in `{typography.display-xl}` (Helvetica Rounded Black 36px, white); sub-copy in `{typography.body-md}` (Neuzeit 16px, white at 80% opacity); CTA uses `button-primary`. On mobile, the minimum height collapses to 320px and the headline scales down to match `{typography.display-md}`.

### Drop Countdown

**`drop-countdown`** — Dark `{colors.ink}` panel with `{rounded.md}` corners used for group buy and limited-run timers. Digit values in `{typography.display-md}` (Helvetica Rounded Bold 24px, white); unit labels in `{typography.caption}` rendered in `{colors.muted}`. A `{colors.primary}` accent stripe runs along the top edge. When the timer reaches zero, the panel transitions out and is replaced by add-to-cart without a page reload.

### Footer

**`footer`** — Full-width `{colors.ink}` background. Column headings in `{typography.title-sm}` (white), link text in `{typography.body-sm}` (muted). Four-column grid on desktop, single stacked column on mobile. Social icons sized at 24px in brand-native colors. NovelKeys wordmark repeats in `{colors.primary}` at the base, grounding the page in brand color before it exits the viewport.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav bar collapses to hamburger + slide drawer; hero shrinks to 320px min-height; collection tabs scroll horizontally; filter sidebar becomes a bottom sheet; footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid; nav bar retains full links if horizontal space allows, otherwise hamburger; hero at 420px; collection tabs visible without scroll |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav bar with inline search visible; hero at 520px; footer in four-column grid; drop countdown in single horizontal row |
| Wide | > 1440px | Content max-width capped at ~1400px centered; hero copy max-width 960px; lateral padding increases to prevent image stretch |

### Touch Targets

- All buttons minimum 44px tall to meet WCAG 2.5.5 target-size requirements
- Color swatches use a 40px invisible touch target even though the visible dot is 24px
- Collection tabs minimum 44px touch height with expanded lateral padding
- Nav icons (cart, account, hamburger) minimum 44×44px tap area via padding expansion
- Stock badges are display-only and not interactive; no minimum target required

### Collapsing Strategy

- Primary nav collapses to hamburger first; search icon remains visible at all breakpoints
- Collection tabs shift from fixed horizontal strip to horizontally scrollable strip on mobile — no dropdown
- Product grid steps: 4-col → 3-col → 2-col → 1-col as viewport narrows
- Drop countdown tiles reflow from a single horizontal row to a 2×2 grid on mobile
- Filter controls move from a left sidebar into a bottom sheet on mobile, triggered by a "Filter" button above the product grid
- Footer columns stack vertically in priority order: navigation links, newsletter signup, social icons, legal text

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed border-radius values extracted from live CSS; all `rounded.*` values are inferred from Helvetica Rounded brand aesthetic and Shopify defaults
- `primary-active` (#007ab5) and `primary-disabled` (#99d5ef) are computed derivations from #0099db — not directly observed in the extracted palette
- Button padding and height not confirmed from DOM inspection; 44px height and 12px/24px padding are accessibility-minimum assumptions
- Usage split between NeuzeitOfficeSRPro-Bold and NeuzeitOfficeSRPro-Regular not confirmed; bold-weight body usage is speculative
- No hover/focus animation durations or easing curves extracted from the live site
- The four near-identical reds (#ca2929, #b52424, #d51f24, #ce272d) likely map to distinct semantic states in Shopify theme variables but exact mapping was not confirmed
- No dark-mode or alternate theme variants observed; site appears to ship a single light-mode skin
- Exact icon library (custom SVG vs. third-party set) not identified from extraction
