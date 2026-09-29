---
version: alpha
name: "StrangeCat Toys"
source_url: "https://www.strangecattoys.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  StrangeCat Toys runs its catalog on a substrate of near-black anthracite — #16171d walls, #0a0a0a footers, the #101219-to-#1a1d29 shift of a dark hero module — punctuated by electric green (#62e483) when a drop goes live or an in-stock badge fires; that green does not appear as a background or button color, it surfaces as signal, the way a notification LED blinks on a shelf of silent hardware. The primary CTA blue (#0273ed) handles all transactional moments at sharp contrast against both dark modules and the off-white listing canvas (#f5f5f5, matching the meta theme-color exactly), while amber-gold (#81632c) marks limited-run pricing and variant highlights with the collector-market weight of a price sticker without actual foil. Display headings use Asul — slightly compressed letterforms and serif-adjacent character that signal independent design authority rather than mass retail — with Inter underneath for body copy, search labels, and UI affordances; together they create a two-tier editorial texture that runs clean on mobile without losing the genre specificity that designer-toy buyers expect. Icon sets from FontAwesome and Pe-icon-7-stroke reinforce that collector-community energy: functional glyphs drawn from the shared visual grammar of forums and hobby stores. Corner radius runs minimal throughout; most components hold to {rounded.xs} (4px) or {rounded.sm} (8px), keeping silhouettes sharp and slightly industrial against the near-black bars, with {rounded.full} appearing only on pill badges and availability dots. Backgrounds oscillate between the light canvas family (#f5f5f5, #f2f2f2, #e9e9e9) for clean product browsing and the dark surface family (#16171d, #101219, #0a0a0a) for hero and featured-drop contexts; a warm cream (#eae1da) and slate-blue (#424557) complete the system as editorial accent surfaces in lookbook and feature-drop layouts, broadening the palette past the monochrome default without abandoning its night-market atmosphere.

colors:
  primary: "#0273ed"
  primary-active: "#0075ff"
  primary-disabled: "#b9b9b9"
  ink: "#0a0a0a"
  body: "#252324"
  muted: "#8c8c8c"
  mid-gray: "#484848"
  hairline: "#d8d8d8"
  hairline-soft: "#e9e9e9"
  canvas: "#f5f5f5"
  surface-soft: "#f2f2f2"
  surface-card: "#e9e9e9"
  on-primary: "#ffffff"
  dark-ink: "#ffffff"
  dark-surface: "#16171d"
  dark-surface-alt: "#101219"
  dark-surface-deep: "#1a1d29"
  accent-green: "#62e483"
  gold: "#81632c"
  error: "#df2c21"
  warm-cream: "#eae1da"
  slate: "#424557"

typography:
  display-xl:
    fontFamily: "'Asul', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Asul', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Asul', serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Asul', serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-lg:
    fontFamily: "'Inter', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  label-caps:
    fontFamily: "'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-ghost-dark:
    backgroundColor: transparent
    textColor: "{colors.dark-ink}"
    border: "1px solid rgba(255,255,255,0.3)"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: 10px 14px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.dark-ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.mid-gray}"
  nav-bar-logo:
    textColor: "{colors.dark-ink}"
    typography: "{typography.display-sm}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    imageBg: "{colors.surface-card}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    padding: "{spacing.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.body}"
  product-card-price-sale:
    textColor: "{colors.error}"
    typography: "{typography.price-sm}"
  badge-in-stock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  badge-sold-out:
    backgroundColor: "{colors.mid-gray}"
    textColor: "{colors.dark-ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  badge-limited:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  hero-dark:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.dark-ink}"
    titleTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  hero-drop-card:
    backgroundColor: "{colors.dark-surface-alt}"
    textColor: "{colors.dark-ink}"
    rounded: "{rounded.sm}"
    accentColor: "{colors.accent-green}"
    padding: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.muted}"
    height: 40px
    padding: 0 12px
  price-display:
    typography: "{typography.price-lg}"
    textColor: "{colors.body}"
    saleColor: "{colors.error}"
    compareColor: "{colors.muted}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.body}"
  editorial-surface:
    backgroundColor: "{colors.warm-cream}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.dark-surface-deep}"
    textColor: "{colors.dark-ink}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.body}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    typography: "{typography.button-sm}"

## Components

### Buttons
**`button-primary`** — Solid blue (#0273ed) fill on a {rounded.xs} (4px) corner, Inter semi-bold at 14px, 44px height with 24px horizontal padding. Hover shifts to the slightly brighter extracted variant (#0075ff). The compact proportions reflect a buyer community that wants fast transactional action over lifestyle pageantry — no oversized padding, no pill rounding.

**`button-secondary`** — Transparent background with a 1px primary-blue border and blue label text, sharing the primary's exact proportions. Used for secondary actions such as "Add to Wishlist" or "View More" where a filled button would compete with the cart CTA.

**`button-ghost-dark`** — Transparent with a semi-opaque white border (30% opacity), deployed exclusively on dark-surface hero and drop-card modules. White text at {typography.button-md} maintains legibility against the #16171d or #101219 backgrounds without introducing a light surface that would break the dark-module atmosphere.

### Navigation
**`nav-bar`** — Near-black (#0a0a0a) background, 60px height, with white text links at Inter 14px/500 weight. The consistently dark bar frames the entire browsing experience, separating the brand header from the product canvas below. Logo renders in Asul display-sm on the left; cart, search, and account icons from FontAwesome appear on the right rail at a minimum 48px tap target.

### Product Cards
**`product-card`** — Light #f2f2f2 surface with {rounded.xs} corners and {spacing.sm} padding. Image container sits at #e9e9e9 to distinguish it from the card body without a border. Title uses Inter 14px/600 in dark ink; price uses Inter 14px/400 in body tone. Sale prices invert to error red (#df2c21); the original price renders in muted gray (#8c8c8c) with strikethrough. No drop shadow — the card differentiates from the #f5f5f5 canvas through subtle value shift alone.

### Badges
**`badge-in-stock`** — Electric green (#62e483) pill with near-black text at Inter 11px/700 uppercase. This is the most distinctive single element in the system: the green reads against both dark hero modules and light card surfaces without color adjustment, functioning as the brand's primary live-status signal. Sold-out flips to mid-gray (#484848) with white text. New, Sale, and Limited variants maintain the same {rounded.full} pill geometry with blue, red, and amber fills respectively — a consistent badge language across the catalog.

### Hero & Drop Modules
**`hero-dark`** — Full-width dark section at #16171d with a minimum 480px height and {spacing.section} vertical padding. Asul display-xl leads the heading hierarchy; Inter body-md handles descriptor copy. This module is where the brand's strongest identity expression lives — collector-market aesthetics over softened lifestyle framing. The dark surface is the brand's home base, not a decorative accent.

**`hero-drop-card`** — Nested card inside dark hero modules, using #101219 background and {rounded.sm} corners, deployed for featured-drop countdowns, artist spotlights, or preorder announcements. Accent-green (#62e483) appears as a rule, dot, or label indicator marking live or upcoming status, preserving its signal function even inside a dark context.

### Search
**`search-bar`** — Light #f2f2f2 surface, 1px hairline border, {rounded.xs}, 40px height with 12px horizontal padding. A FontAwesome magnifying-glass icon insets on the left in muted gray (#8c8c8c). No pill rounding — consistent with the sharp-corner system bias across all interactive elements.

### Pricing
**`price-display`** — Inter 20px/700 for the primary price in body ink, dropping to Inter 14px/400 for compare-at prices in muted gray with strikethrough. Sale price renders at the same 20px/700 weight in error red (#df2c21). Gold (#81632c) can be applied to limited-edition price labels or variant callouts at the title-sm scale.

### Footer
**`footer`** — Deep navy-black (#1a1d29) background with white-adjacent text and muted gray (#8c8c8c) navigation links. Mirrors the nav-bar's dark bookend logic, closing the page with the same brand frame that opens it. Inter body-sm throughout; {spacing.section} vertical padding with a multi-column link grid collapsing to stacked on mobile.

### Editorial Surfaces
**`editorial-surface`** — Warm cream (#eae1da) background at {rounded.sm}, used for artist-profile callouts, lookbook-style feature sections, or editorial interludes between dark hero modules and light product grids. Provides material contrast against the dominant gray-black-white register without introducing a color that disrupts the night-market palette logic.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav overlay on dark-surface drawer, hero height collapses to 320px, search expands full-width |
| Tablet | 744–1128px | 2–3 column product grid, horizontal nav with overflow scroll, hero at 400px, filters in bottom sheet |
| Desktop | 1128–1440px | 4-column product grid, full nav bar with category dropdown, hero at 480px+, filters in left sidebar |
| Wide | > 1440px | Container max-width ~1400px centered, side gutters increase, grid holds at 4 columns |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Nav icon buttons (cart, search, account) padded to 48px tap area
- Badge pills gain 8px invisible hit area beyond visual bounds
- Pagination numbers minimum 40px square on mobile

### Collapsing Strategy
- Nav collapses to hamburger + centered logo + cart icon on mobile
- Product filters shift from desktop left-sidebar to mobile bottom-sheet drawer
- Footer collapses from 4-column link grid → 2-column at tablet → accordion stack on mobile
- Hero CTA buttons stack vertically at mobile if two are present side-by-side on desktop
- Badge and price elements remain fully visible at all breakpoints; they never truncate or collapse into tooltips

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Asul and Inter size/weight values not confirmed from CSS extraction — scales inferred from typical Shopify theme patterns for the collectibles category
- Two very similar CTA blues (#0273ed vs #0075ff) extracted; which is default vs. hover state could not be confirmed from static extraction
- `#81632c` (amber-gold) context not confirmed — may appear in pricing, limited-edition badge fills, or hover states rather than all three
- `#424557` (slate-blue) usage context not confirmed — could be a secondary dark surface, a disabled input state, or a pagination inactive tone
- `on-primary` (#ffffff) and `dark-ink` (#ffffff) not extracted — assumed as necessary contrast pairs for colored and dark surfaces respectively
- Logo treatment (Asul wordmark vs. custom glyph, whether Asul appears in logo at all) not confirmed from extraction
- Whether the dark surface family (#0a0a0a, #16171d, #101219) represents a dark-mode toggle or dedicated page sections could not be confirmed
- Exact corner radius values not extracted — {rounded.xs} system bias inferred from collector/hobby site aesthetics, not measured CSS
- Hover and focus ring colors for form inputs beyond the primary blue not extracted
- `#62e483` (electric green) confirmed as present but exact component context (badge fill, rule, dot, text) not verified from static extraction
