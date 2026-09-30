---
version: alpha
name: "Silicon Power"
source_url: "https://www.silicon-power.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Silicon Power's palette reads like a circuit board shot in low light: the page surface is built from a cascade of near-identical grays — #f1f1f1, #f4f4f4, #f7f7f7, #ebebeb — laid over dark #272626 and #1c1c1c near-blacks that anchor headers and full-bleed hero sections. Against all of that ash and charcoal, a single voltage element fires: #f14595, a saturated magenta-pink that runs every primary CTA, product badge, and section accent bar. The move is deliberate for a Taiwanese storage hardware manufacturer — SSDs, USB drives, DRAM, memory cards — that uses the charcoal foundation to signal engineering precision and reserves the pink for the action path only, the way a dark drive enclosure might carry a single LED status light.

  Nunito Sans handles all Latin text, a rounded geometric that sits between the stiffness of Helvetica-derived system fonts and the friendliness-at-any-cost of consumer rounded faces. Weights run 400 for body, 600 for titles, 700 for display and button labels. Noto Sans TC and Microsoft JhengHei (微軟正黑體) handle Traditional Chinese throughout, anchoring the brand's Asia-Pacific distribution identity — the font stack is bilingual by operational necessity, not decoration.

  A second accent, #003399 deep navy, enters as a credibility counterpart to the magenta: applied to product-line certification badges and "Where to Buy" CTAs where authority matters more than urgency. Between those two anchors, a gray band from #6a6a6a through #b5b5b5 covers every secondary text state, caption, and border without requiring tints of either accent. Corner geometry stays close to square — {rounded.xs} at 4px for buttons and inputs, {rounded.sm} at 8px for cards — a catalog-practical choice that prioritizes grid density over personality curves. The barely-blush surface tone #f0eaea appears as a product image background, placing hardware renders on a near-neutral field that separates them from pure white canvas without introducing warmth into the broader system. Spacing is catalog-generous: {spacing.section} at 64px separates major product-line blocks, while {spacing.base} governs internal card padding throughout the grid.

colors:
  primary: "#f14595"
  primary-active: "#c9347d"
  primary-disabled: "#f8bdd8"
  accent-navy: "#003399"
  accent-navy-active: "#002280"
  ink: "#272626"
  body: "#4f4f4f"
  muted: "#6a6a6a"
  muted-soft: "#888888"
  hairline: "#e1e1e1"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-warm: "#f0eaea"
  surface-card: "#f4f4f4"
  surface-dark: "#1c1c1c"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  mid-dark: "#323232"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito Sans', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Nunito Sans', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', 'Noto Sans TC', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Noto Sans TC', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Noto Sans TC', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Noto Sans TC', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Noto Sans TC', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', 'Noto Sans TC', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Nunito Sans', 'Noto Sans TC', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Nunito Sans', 'Noto Sans TC', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px

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
  button-primary-active:
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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-navy:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    border: "1px solid {colors.hairline}"
    height: 42px
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
  product-card-image:
    backgroundColor: "{colors.surface-warm}"
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-navy:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    headlineTypography: "{typography.display-xl}"
    accentColor: "{colors.primary}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.spec-label}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    iconColor: "{colors.muted}"
  section-header:
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    accentBar: "4px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.mid-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    accentColor: "{colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"

## Components

### Buttons

**`button-primary`** — Magenta (#f14595) fill, white text, 44px tall, {rounded.xs} (4px) radius. Active state darkens to #c9347d; disabled washes to a pale #f8bdd8 with white text retained. Applied exclusively to primary purchase, download, and "Add to Cart" actions across all product pages.

**`button-secondary`** — White canvas background with {colors.ink} text and a 1px {colors.hairline} border, same 44px height and geometry as primary. Appears alongside primary buttons for "Compare," "Specs," or "Add to Wishlist" flows where the action is reversible or secondary.

**`button-navy`** — Deep #003399 fill with white text, identical height and radius to button-primary. Reserved for "Where to Buy" CTAs and retailer-link actions — carries authority rather than urgency, distinguishing purchase-path from retail-redirect.

**`button-ghost`** — Transparent background, 1px magenta border, #f14595 text. Used on dark hero surfaces or card overlays where a filled button would dominate; communicates a secondary-within-primary context.

### Text Input

**`text-input`** — White background, 1px {colors.hairline} border, 42px height, {rounded.xs}. On focus, the border shifts to {colors.primary} magenta — a consistent accent signal that requires no extra affordance. Placeholder text renders in {colors.muted}.

### Navigation

**`nav-bar`** — White canvas, 64px tall, bottom {colors.hairline-soft} separator. Links use {typography.nav-link} at 14px/weight 600. A dark variant (nav-bar-dark) inverts to {colors.ink} background for immersive product-launch hero layouts. Mega-menu dropdowns appear below the bar on desktop, inheriting {colors.surface-card} backgrounds and {rounded.sm} container edges.

### Product Card

**`product-card`** — {colors.surface-card} (#f4f4f4) background, {rounded.sm} corners, 1px {colors.hairline-soft} border. The image zone uses {colors.surface-warm} (#f0eaea) — a barely-blush off-white — to float hardware renders off a neutral field. Title renders in {typography.title-sm} at 600 weight; price in {typography.title-md}. Badges (NEW, HOT, AWARD) pin to the top-left corner of the image zone.

### Hero

**`hero`** — Full-width {colors.surface-dark} (#1c1c1c) panel, minimum 480px tall. Headline in {typography.display-xl} with product name segments colored {colors.primary}. Supporting copy and spec callouts in {colors.on-dark}. Primary CTA is always button-primary; secondary CTA uses button-ghost on the dark field.

### Category Chips

**`category-chip`** / **`category-chip-active`** — Pill-shaped ({rounded.full}) filter tokens that run horizontally above product grids: Storage, Flash, DRAM, Power Banks, and sub-categories. Inactive chips are {colors.surface-soft} with {colors.body} text; the active chip fills solid {colors.primary} magenta. Horizontal snap-scroll container on mobile.

### Spec Table

**`spec-table`** — White background with {colors.surface-soft} header rows. Column labels use {typography.spec-label} (11px, uppercase, 1px tracking) in {colors.muted}. Row values use {typography.body-sm}. A critical component: Silicon Power products carry extensive spec rows (interface, form factor, capacity, read/write speeds, MTBF, warranty). Lightweight 1px {colors.hairline} borders; {rounded.sm} outer container.

### Search Bar

**`search-bar`** — Pill-shaped ({rounded.full}), {colors.surface-soft} background, 44px height. Magnifier icon in {colors.muted}. Results panel drops as a {colors.canvas} container with {rounded.sm} corners, listing product names in {typography.body-sm} and category labels in {typography.caption}.

### Product Badges

**`product-badge`** — Magenta fill for editorial labels ("NEW," "HOT," "AWARD WINNER"). **`product-badge-navy`** — Navy fill for product-line or certification markers ("PCIe Gen 4," "PS5 Compatible"). Both use {typography.badge} at 11px/700 and {rounded.xs} with 2px 8px padding, pinned to image corners or beside product titles.

### Section Header

**`section-header`** — A 4px left border in {colors.primary} accompanies {typography.display-md} headings to visually segment product-line blocks (Storage Solutions, Flash Memory, Power Banks). The accent bar is the only decorative element allowed at this level — no underlines, no background fills.

### Footer

**`footer`** — {colors.mid-dark} (#323232) background, off-white {colors.on-dark} body text, {colors.muted-soft} (#888888) for secondary links. {colors.primary} magenta appears on hover states and the brand wordmark. Layout is a four-column grid: Products, Support, About, Social — collapsing to a single accordion stack on mobile.

### Breadcrumb

**`breadcrumb`** — Small {typography.caption} text in {colors.muted}, hairline separators, current node in {colors.ink}. Appears on all product detail and support pages below the nav bar.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces horizontal mega-menu; hero min-height drops to 320px; spec tables scroll horizontally in a snap container; category chips scroll horizontally; all CTAs go full-width |
| Tablet | 744–1128px | Two-column product grid; mega-menu collapses to a horizontal scroll bar; hero at 400px; section padding reduces from {spacing.section} to {spacing.xl}; footer grid collapses to two columns |
| Desktop | 1128–1440px | Three- to four-column product grid; full horizontal nav with mega-menu dropdowns; hero at 480px; breadcrumb and spec tables fully visible |
| Wide | > 1440px | Content max-width ~1440px centered; hero background bleeds edge-to-edge; four-column product grid maintained; footer four-column layout preserved |

### Touch Targets
- All buttons minimum 44px tall (button-primary, button-secondary, button-navy, button-ghost)
- Category chips minimum 36px tall on mobile with 12px horizontal padding
- Nav links in hamburger drawer expand to full-width rows with 48px minimum row height
- Product cards maintain 16px gutters on mobile to preserve tappability

### Collapsing Strategy
- Mega-menu navigation collapses to a categorized slide-in drawer at tablet breakpoint
- Product grid collapses: 4-col (wide) → 3-col (desktop) → 2-col (tablet) → 1-col (mobile)
- Spec tables use horizontal scroll on mobile rather than collapsing or hiding columns — all spec data must remain accessible
- Hero copy stacks vertically on mobile: headline, then subhead, then full-width CTA row
- Footer: 4-column grid → 2-column → single accordion (each section collapses independently)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; mobile browser chrome color and PWA theming unknown
- The warm off-white #f0eaea is assigned to product image backgrounds based on palette position; its actual DOM usage context (section background vs. image container vs. something else) is unconfirmed
- Exact button corner radius not verified from DOM inspection; {rounded.xs} (4px) is inferred from the catalog's near-square visual aesthetic
- Nunito Sans weight distribution (400/600/700) is inferred from typical hardware catalog usage — actual computed font-weight values per element not captured
- Hover transition timing and easing curves for buttons, cards, and nav dropdowns not extracted
- Dark-mode support not detected; assumed absent
- #003399 navy scope is uncertain — may be limited to specific product-line landing pages rather than used as a global secondary CTA color
- FontAwesome is confirmed in the stack but the specific icon subset, sizes, and which components use icon-only vs. icon+label patterns are not mapped
- Animation behavior for mega-menu dropdowns, hero carousels, and product image zoom not captured
- Whether Silicon Power uses a custom icon set beyond FontAwesome for product-category glyphs is unknown
