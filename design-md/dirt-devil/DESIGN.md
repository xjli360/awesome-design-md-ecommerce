---
version: alpha
name: "Dirt Devil"
source_url: "https://www.dirtdevil.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The chrome-red chassis that has anchored American household cleaning since the early twentieth century arrives on screen as a single, uncompromising voltage — #e01e2a — that drives every primary CTA, promotional badge, and hero overlay. Where competitors reach for clinical white or corporate blue to signal cleanliness, Dirt Devil makes the opposite wager: red means power, urgency, and deal momentum. The near-black ground (#121212, #231f20) reinforces that industrial confidence, while #f3f3f3 and #d9d9d9 light surfaces keep product photography crisp against neutral planes. A secondary blue (#334fb4) surfaces selectively for informational links and secondary CTAs, preventing the primary hue from overwhelming long catalog scroll sessions. Nunito Sans — a rounded geometric sans with low stroke contrast — carries all type across the system; its soft terminals temper what could otherwise feel like a purely utilitarian parts catalog. Buttons are moderately rounded ({rounded.sm}), not pill-shaped, communicating utility over playfulness. Product cards sit on {colors.surface-card} with a faint {colors.hairline} border, foregrounding photography of red-housed appliances against neutral fields. The soft blush {colors.promo-surface} (#fceaed) appears as the surface behind sale callouts — a diluted echo of the primary red that reduces visual fatigue on promotional pages. A dark charcoal {colors.surface-dark} (#242833) grounds footer sections and announcement strips, giving the composition a base that lets the red read at full intensity wherever it appears. Promotional badges carry {colors.primary} fills with {colors.on-primary} white uppercase type, treating the brand color as the urgency signal it has historically been.

colors:
  primary: "#e01e2a"
  primary-active: "#dd0022"
  primary-disabled: "#fceaed"
  accent-blue: "#334fb4"
  ink: "#121212"
  body: "#231f20"
  muted: "#696969"
  muted-mid: "#535356"
  charcoal: "#4f4c4d"
  hairline: "#dedede"
  hairline-soft: "#d9d9d9"
  canvas: "#f3f3f3"
  surface-card: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-dark: "#242833"
  promo-surface: "#fceaed"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 22px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.2px
  spec-label:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
    padding: 12px 26px
    height: 48px
  button-outline-red:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 12px 26px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  nav-utility-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageBackground: "{colors.canvas}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    titleTypography: "{typography.title-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 520px
    overlayOpacity: 0.55
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    height: 40px
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid transparent"
    padding: "{spacing.sm} {spacing.base}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 10px 20px
    height: 44px
    iconColor: "{colors.muted}"
  filter-chip:
    backgroundColor: "{colors.surface-card}"
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
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    altBackgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} {spacing.base}"
  comparison-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    headerBackgroundColor: "{colors.promo-surface}"
    padding: "{spacing.base}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline-soft}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Solid #e01e2a fill with white uppercase Nunito Sans at 15px/700 weight, 8px radius, and 48px height. Hover deepens to `{colors.primary-active}` (#dd0022); disabled collapses to the blush `{colors.primary-disabled}` with `{colors.muted}` label text. The dominant CTA across the site — Add to Cart, Shop Now, Find a Retailer.

**`button-secondary`** — White fill with a 2px solid `{colors.ink}` border and matching uppercase Nunito Sans label at the same 48px height as the primary. Used in two-up CTA pairings where a red button already occupies one slot and the secondary action needs visual parity without competing.

**`button-outline-red`** — Transparent fill with a 2px `{colors.primary}` border and red label text. Reserved for secondary product-page actions — Compare, Add to Wish List, View Details — where the red signal stays on-brand without the full weight of a filled button.

### Forms

**`text-input`** — White field with 1px `{colors.hairline}` border, 48px height, and Nunito Sans `{typography.body-md}`. Focus state upgrades the border to 2px `{colors.primary}` red, carrying the brand signal into utility moments without requiring a color fill.

**`search-bar`** — Pill-shaped (`{rounded.full}`) field that distinguishes search from standard form inputs at a glance. A `{colors.muted}` magnifier icon sits left-inset; the fully-rounded form reads as approachable on an otherwise utility-focused page.

### Navigation

**`nav-bar`** — 64px white bar with the Dirt Devil wordmark in `{colors.primary}` red, category links in `{typography.nav-link}`, and utility icons (search, cart, account) right-aligned. A single `{colors.hairline}` bottom border provides separation without adding visual weight.

**`nav-utility-bar`** — 36px strip in `{colors.ink}` above the main nav carries promotional copy — free shipping thresholds, limited-time offers — in `{typography.caption}` white. Keeps conversion-critical messaging visible without consuming hero space.

**`category-tab`** / **`category-tab-active`** — Horizontal rail below the main nav filters by vacuum type: Upright, Stick, Hand, Canister, Wet/Dry. The active tab renders a 2px `{colors.primary}` underline with a red label; inactive tabs use `{colors.body}` gray. No background fill — the underline alone carries selection state, keeping the tab bar visually quiet.

### Product Display

**`product-card`** — White card with a 1px `{colors.hairline}` border and `{rounded.sm}` radius. The product image renders against a `{colors.canvas}` light-gray field so red vacuum housings read at full saturation. Price in `{typography.price-display}` (22px/800 weight) carries `{colors.primary}` red; the product name runs `{typography.title-sm}` in ink. On desktop, the Add to Cart button appears on hover-state elevation; on mobile it is persistent and full-width.

**`product-badge`** / **`sale-badge`** — Uppercase 11px/700 labels with `{rounded.xs}` radius on a `{colors.primary}` fill, positioned absolute over the top-left corner of the product image. Applied for SALE, NEW, BEST SELLER, and bundle callouts. No more than two badges stack on a single card.

**`comparison-card`** — When a product is queued for comparison, its card gains a 2px `{colors.primary}` border and a `{colors.promo-surface}` blush strip across the header, making selected candidates visually distinct from the browse grid without a separate UI layer.

### Promotional

**`promo-banner`** — Full-width 40px strip in `{colors.primary}` with `{colors.on-primary}` caption text, pinned to the top of the viewport for time-limited offers. Dismissible via a white X icon. On mobile, long copy marquee-scrolls rather than wrapping.

**`hero`** — Dark-ground hero (`{colors.ink}` base with a 0.55 scrim over lifestyle photography) places `{typography.display-xl}` white headlines and a `{colors.primary}` CTA button at left or center alignment. Minimum 520px tall on desktop; image crops to portrait on mobile with text stacked above.

### Filtering

**`filter-chip`** / **`filter-chip-active`** — Pill-shaped chips (`{rounded.full}`) for horizontal filter rails or sidebar panels. Inactive: `{colors.surface-card}` fill, `{colors.hairline}` border, `{colors.ink}` text. Active: solid `{colors.primary}` fill, `{colors.on-primary}` white text. Minimum 36px height for touch accessibility.

### Data / Specifications

**`spec-table-row`** — Alternating `{colors.canvas}` and `{colors.surface-card}` row backgrounds, separated by `{colors.hairline-soft}` lines. The label column uses `{typography.spec-label}` (semibold 13px) and the value column uses `{typography.body-sm}`. Used on product detail pages for suction power, cord length, weight, filter type, and bin capacity.

### Footer

**`footer`** — `{colors.surface-dark}` (#242833) ground with `{colors.on-dark}` white copy in four link columns (Products, Support, About, Social). Link color is a softened `{colors.hairline-soft}` tone to maintain column hierarchy. The Dirt Devil wordmark appears in white, anchoring the brand identity on the dark base.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category tabs scroll horizontally; hero stacks headline above image; nav collapses to hamburger + cart icon; filter chips move to a slide-up drawer |
| Tablet | 744–1128px | Two-column product grid; full category tab rail visible; nav shows primary categories with hamburger overflow; hero uses landscape crop with side-by-side text and image |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with mega-dropdown for categories; hero full-bleed at 520px min-height; filter rail appears as left-column sidebar |
| Wide | > 1440px | Four-column product grid; max-width container (~1440px) centered on canvas; hero imagery extends edge-to-edge behind contained text column |

### Touch Targets

- All buttons minimum 48px height and 44px width
- Category tabs minimum 44px height with horizontal scroll momentum on mobile
- Filter chips minimum 36px height, 12px horizontal padding
- Cart, search, and account nav icons minimum 44×44px tap area
- Product card Add to Cart button full-width on mobile for easy reach

### Collapsing Strategy

- Primary navigation collapses to hamburger at < 1024px; logo in `{colors.primary}` and cart icon remain visible at all breakpoints
- Utility bar collapses to a single marquee-scroll message on mobile below 744px
- Specification tables collapse into accordion sections on mobile to reduce scroll depth on product detail pages
- Product comparison feature is hidden on mobile and replaced by a Compare link that opens a full-screen modal
- Footer four-column grid collapses to accordion-style expandable sections on mobile; social icons pin to the bottom

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font weight file extraction confirmed — Nunito Sans weight scale (400–800) inferred from common DTC patterns; verify 800 weight availability for display-xl headlines before committing
- Meta theme-color tag not set; no explicit dark-mode palette detected — assume light-mode-only unless the Shopify theme includes a dark scheme toggle
- Exact nav mega-dropdown layout, subcategory depth, and featured-product slot structure not extracted
- Animation and transition timing not detected — easing curves for hover elevations, drawer open/close, and tab underline transitions are inferred as standard 150–200ms ease-out
- Icon set style (line vs. filled, stroke weight, grid size) not confirmed from extraction
- Precise product card hover box-shadow values not extracted; elevation level is inferred
- Mobile breakpoint thresholds are inferred from Shopify Liquid defaults; confirm actual media query values in the active theme's CSS
- Accent blue (#334fb4) role and frequency of use not fully confirmed — extracted but usage context (links only vs. secondary buttons) requires visual audit
