---
version: alpha
name: "BaubleBar"
source_url: "https://baublebar.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Mulish headlines give way to utopia-std serifs at the editorial scale — a typographic split that maps BaubleBar's dual register: everyday product listings set in clean geometric sans, campaign moments elevated by italic slab-serif display. Three saturated accents interrupt an otherwise graduated neutral stack: teal (#009879) loads every primary CTA and add-to-cart confirmation state, coral (#f94c43) flags sale and clearance callouts, amber (#f6a429) marks gifting surfaces and bestseller badge moments. The remaining 80% of each page runs in near-blacks (#202223, #121212), a mid-gray ladder (#484848, #7e7e7e, #939393), and a white canvas — restraint that lets each accent voltage hit with full saturation on contact. Buttons carry a near-flat profile consistent with the Mulish grid geometry: not the pill friendliness of beauty brands, not the hard square corners of fashion editorial. Product cards float photography on white without visible card borders, giving jewelry room to breathe rather than boxing it into shelves. Filter capsules break the grid intentionally with {rounded.full} shapes, marking the one interactive zone that reads explicitly touchable. The announcement bar runs inverted — deep ink (#202223) background with all-caps Mulish captions — functioning as a persistent orientation stripe rather than a dismissible notice. Personalization and gift-finder modules reach for amber ({colors.highlight}) over sale coral ({colors.sale}), a color distinction that preserves promotional hierarchy even when both badge types appear on the same product card. The cool-grey accent (#c5c8d1) surfaces exclusively in helper text, placeholder states, and decorative dividers — it never substitutes for the hairline system ({colors.hairline}, #dedede). At the display scale, utopia-std-headline carries optical mass that weighted Mulish body text cannot, letting hero banners read as editorial spreads rather than catalog listings. The page title's "Luxury Jewelry & Personalized Accessories" framing is backed by white-space generosity and photography priority, not surface ornamentation.

colors:
  primary: "#009879"
  primary-active: "#007a62"
  primary-disabled: "#99d4c9"
  sale: "#f94c43"
  sale-active: "#d93a31"
  highlight: "#f6a429"
  ink: "#202223"
  body: "#484848"
  muted: "#7e7e7e"
  muted-soft: "#939393"
  hairline: "#dedede"
  hairline-soft: "#e7e7e7"
  canvas: "#ffffff"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  surface-mid: "#efefef"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  cool-grey: "#c5c8d1"

typography:
  display-xl:
    fontFamily: "'utopia-std-headline', utopia-std, Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'utopia-std-headline', utopia-std, Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'utopia-std-headline', utopia-std, Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'utopia-std-headline', utopia-std, Georgia, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Mulish, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "Mulish, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0.2px
  body-md:
    fontFamily: "Mulish, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Mulish, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Mulish, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "Mulish, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "Mulish, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Mulish, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "Mulish, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  price:
    fontFamily: "Mulish, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  price-sale:
    fontFamily: "Mulish, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  price-original:
    fontFamily: "Mulish, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0
    textDecoration: line-through
  badge:
    fontFamily: "Mulish, sans-serif"
    fontSize: 10px
    fontWeight: 800
    lineHeight: 1.2
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
    rounded: "{rounded.xs}"
    padding: 14px 32px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.ink}"
  button-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-sale-hover:
    backgroundColor: "{colors.sale-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-bold}"
    height: 36px
    textAlign: center
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    imageAspectRatio: "1:1"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    textColor: "{colors.sale}"
  product-card-price-original:
    typography: "{typography.price-original}"
    textColor: "{colors.muted}"
  sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  new-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  highlight-badge:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subheadingTypography: "{typography.body-md}"
    padding: "{spacing.section}"
    minHeight: 480px
  hero-banner-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    subheadingTypography: "{typography.body-md}"
    padding: "{spacing.section}"
    minHeight: 480px
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  color-swatch:
    rounded: "{rounded.full}"
    size: 20px
    border: "1.5px solid {colors.hairline}"
  color-swatch-selected:
    rounded: "{rounded.full}"
    size: 20px
    border: "2.5px solid {colors.ink}"
    outlineOffset: 2px
  wishlist-button:
    backgroundColor: transparent
    iconColor: "{colors.muted}"
    iconColorActive: "{colors.sale}"
    rounded: "{rounded.full}"
    size: 32px
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    height: 40px
  personalization-module:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Teal (#009879) fill with white all-caps Mulish text at 13px/1.5px tracking, 4px radius. Sits at 48px tall to meet touch targets comfortably. Hover darkens to `{colors.primary-active}` (#007a62); disabled washes to `{colors.primary-disabled}` (#99d4c9) while retaining white text. This button carries add-to-cart, checkout, and subscription confirm actions site-wide.

**`button-secondary`** — White canvas fill with 1.5px ink border and matching all-caps Mulish. Used for secondary actions like "Save for Later" and "View Details." Hover introduces a `{colors.surface-soft}` fill tint while the border and text remain ink. Maintains the same 48px height and 4px radius as primary.

**`button-sale`** — Coral (#f94c43) fill for sale-entry CTAs and promotional landing pages. Uses identical typography and radius to primary; visually distinct from primary teal to signal discounted price context. Deepens to `{colors.sale-active}` on hover.

**`button-ghost`** — Transparent fill with a hairline border at 40px height, used for filter-reset, "Load More," and secondary nav actions. Lowercase button-sm typography at reduced tracking keeps it lighter weight than primary or secondary.

### Text Input

**`text-input`** — Flat (0px radius) with a single hairline border that steps up to ink on focus, matching the editorial square geometry. Placeholder text in muted gray (#7e7e7e). No fill tint on focus; border weight change alone signals state. Height 48px for form accessibility.

### Navigation

**`nav-bar`** — White canvas at 60px with a hairline bottom border. Navigation links in 14px Mulish 600 with tight letter-spacing. Topped by the **`announcement-bar`** — 36px inverted ink stripe with centered all-caps caption-bold Mulish. The two bars stack to a combined 96px at the top of each page, a persistent orientation block on all breakpoints.

**`nav-dropdown`** — Full-width panel that drops below the nav-bar hairline border on category hover. White background with body-sm Mulish for subcategory links. Padded at `{spacing.lg}` inside to let product imagery or editorial content breathe alongside text links.

### Product Card

**`product-card`** — Borderless white card, square image aspect ratio, stacked below with title in body-sm and price in 15px bold Mulish. No card shadow or border; the grid gap between cards creates the visual separation. Sale items show `{colors.sale}` price alongside a struck-through original in muted gray. Badges (`sale-badge`, `new-badge`, `highlight-badge`) overlay the top-left corner of the image at 0px radius with uppercase micro-Mulish.

### Badges

Three badge variants share the same 10px/800-weight/uppercase Mulish structure and flat shape, differentiated only by color. **`sale-badge`** uses coral (#f94c43) for markdown callouts. **`new-badge`** uses ink (#202223) for new arrivals and recent additions. **`highlight-badge`** uses amber (#f6a429) with dark text for gifting picks, bestsellers, and personalization callouts — amber is bright enough that dark `{colors.ink}` text clears WCAG AA contrast, unlike white-on-amber.

### Hero Banner

**`hero-banner`** — Light gray surface (`{colors.surface-soft}`) or inverted ink for campaign moments (`hero-banner-dark`). Headline in utopia-std-headline at 48px — the serif weight gives editorial authority no sans could match at this size. Subheading in body-md Mulish. Minimum 480px tall on desktop to anchor the editorial photograph. CTA button centered or left-aligned depending on layout variant.

### Filter Pills

**`filter-pill`** / **`filter-pill-active`** — Full-radius capsule shapes (9999px) that contrast sharply with the flat-corner button family. Inactive pills are soft-gray fill with hairline border; active flips to ink fill with white text. This shape difference makes the filter bar immediately scannable as an interaction zone distinct from product actions below it.

### Color Swatches

**`color-swatch`** — 20px circular dot with a 1.5px hairline border. **`color-swatch-selected`** — same diameter but 2.5px ink border with a 2px offset outline ring for clear selection indication without enlarging the tap target.

### Personalization Module

**`personalization-module`** — Soft gray card (`{colors.surface-soft}`) with an amber (`{colors.highlight}`) accent stripe or header to visually separate personalization CTAs (monogram, gifting, custom orders) from sale content. Rounded at `{rounded.sm}` to distinguish module containers from the flat product card grid.

### Footer

**`footer`** — Light gray surface with a top hairline, body-sm Mulish in mid-gray, ink-colored links. Padded at `{spacing.xxl}` vertically. Consistent with the surface-soft system used across section dividers; does not use a dark or full-bleed black variant.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + icon strip; announcement bar persists; hero banner reduces to 320px min-height; filter pills scroll horizontally in a no-wrap row |
| Tablet | 744–1128px | Two-column product grid; nav may use partial collapse with key categories visible; hero banner at 400px min-height; side-by-side hero text + image layout |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with dropdowns; hero at full 480px+ with constrained content width |
| Wide | > 1440px | Max content width capped (~1440px) with symmetric gutter expansion; product grid holds at four columns; hero image expands edge-to-edge behind constrained text column |

### Touch Targets

- All buttons minimum 48px tall; ghost button at 40px is acceptable for secondary/tertiary contexts
- Color swatches 20px visual with at least 32px touch proxy wrapper
- Wishlist icon button 32px with 8px transparent padding bringing effective target to 48px
- Filter pills 40px height minimum on mobile to support thumb interaction

### Collapsing Strategy

- Desktop mega-nav collapses to icon-row + hamburger drawer on mobile; drawer uses full-height slide-in panel
- Product grid drops from 4 → 3 → 2 → 1 column as viewport narrows; grid gap reduces from `{spacing.lg}` to `{spacing.sm}` at mobile
- Hero banner text overlays image on mobile (absolute positioned) rather than stacking below to preserve above-fold impact
- Announcement bar remains full-width and persistent across all breakpoints; text may truncate to single scrolling marquee on mobile
- Filter bar switches from wrap to horizontal scroll on mobile; active filter count badge appears on filter toggle button

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border radius not confirmed from extraction; 4px (xs) assumed based on Mulish geometric aesthetic
- Whether utopia-std-headline is used in italic-only or also upright forms at display scale
- Specific font weights in use beyond what CSS stacks imply (Mulish supports 200–900; active weights unconfirmed)
- Navigation dropdown structure — mega-nav vs. simple flyout, column count, editorial imagery presence
- Animation and transition timings (hover fade durations, drawer slide speeds)
- Mobile navigation pattern beyond hamburger assumption (full-screen overlay vs. side drawer)
- Exact product grid gap values and column count rules per breakpoint
- Whether color swatch out-of-stock state uses a diagonal strike or opacity reduction
- Loading skeleton / placeholder styling for product cards
- Cart drawer vs. cart page routing behavior on add-to-cart
