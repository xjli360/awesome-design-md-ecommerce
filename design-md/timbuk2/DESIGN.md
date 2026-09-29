---
version: alpha
name: "Timbuk2"
source_url: "https://www.timbuk2.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Timbuk2's color system reads like a bag customizer's swatch wall made literal — deep navy #2d3142, golden yellow #e5c225, forest green #42583f, hot pink #f03680, and burnt orange #d76800 don't perform assigned brand roles so much as sit in standby, mirroring the custom bag builder that has defined the brand since its San Francisco bike-messenger origins in 1989. The primary CTA lives in that same golden yellow, so the "add to cart" button and the strap color option feel drawn from the same material logic rather than from a separate visual system. Dark navy #2d3142 anchors the wordmark, navigation, and primary headlines — a color that suggests waxed canvas and night commutes more than corporate polish. No custom font stack was extracted from the live site (likely loaded via JavaScript); the typographic sensibility reads lean and utilitarian regardless — modest display weights, tightly tracked labels, no decorative serifs anywhere in the stack. The brand's DNA is functional: readable first, expressive second, which puts the visual energy in the product rather than in the chrome surrounding it. Shapes are quietly angular. Buttons sit at {rounded.xs} or {rounded.sm}, not the pill-shaped softness of lifestyle brands — the strap hardware on a Timbuk2 bag is a buckle, not a curve, and the UI carries the same attitude. Product cards carry minimal border radii, letting photography of the bags carry visual weight. The one place roundness becomes expressive is the customizer's color-swatch UI — {rounded.full} circles that users click to mix panel, strap, and lining colors, the single tactile interaction the entire brand is built around. The expanded palette — blush #ebccc7, sand #e8daca, amber #f6c960, mint #0ab968, purple #9370b3, red #c23838 — exists not as decorative UI accent but as product inventory pulled directly into CSS for real-time bag previews. The surface system stays deliberately stripped: near-white #f5f5f5 backgrounds, white cards, a #dedede hairline — so that the swatch array does all the visual lifting without competition from the surrounding interface.

colors:
  primary: "#e5c225"
  primary-active: "#c9ab1e"
  primary-disabled: "#f3e694"
  ink: "#2d3142"
  body: "#33363f"
  muted: "#8b8b8b"
  muted-soft: "#939393"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#2d3142"
  on-dark: "#ffffff"
  accent-green: "#42583f"
  accent-orange: "#d76800"
  accent-pink: "#f03680"
  accent-red: "#c23838"
  accent-amber: "#f6c960"
  accent-blush: "#ebccc7"
  accent-sand: "#e8daca"
  accent-mint: "#0ab968"
  accent-purple: "#9370b3"
  navy-mid: "#364477"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 44px
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: -0.6px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.2px
  filter-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0
  price-compare:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  swatch-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.4px
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
    border: none
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
  button-secondary-active:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: none
    logoColor: "{colors.primary}"
  nav-bar-scrolled:
    backgroundColor: "{colors.ink}"
    boxShadow: "0 2px 12px rgba(0,0,0,0.35)"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.none}"
    imageBorderRadius: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    comparePriceTypography: "{typography.price-compare}"
    comparePriceColor: "{colors.muted}"
    padding: "{spacing.md}"
    hoverBoxShadow: "0 4px 16px rgba(0,0,0,0.10)"
    hoverTransform: "translateY(-2px)"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: button-primary
    minHeight: 560px
    overlay: "linear-gradient(to right, rgba(45,49,66,0.82) 0%, rgba(45,49,66,0.30) 55%, transparent 100%)"
    contentMaxWidth: 580px
  hero-split:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    leftPanelBackground: "{colors.ink}"
    leftPanelTextColor: "{colors.on-dark}"
    rightPanelBackground: "{colors.surface-soft}"
    gap: 0
  color-swatch:
    size: 32px
    rounded: "{rounded.full}"
    borderWidth: 2px
    borderColorDefault: transparent
    borderColorSelected: "{colors.ink}"
    borderColorHover: "{colors.muted-soft}"
    offsetSelected: "0 0 0 2px {colors.ink}"
    gap: "{spacing.sm}"
  custom-builder-panel:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    sectionLabelTypography: "{typography.swatch-label}"
    sectionLabelColor: "{colors.muted}"
    selectedIndicatorColor: "{colors.ink}"
    padding: "{spacing.lg}"
    stepConnectorColor: "{colors.primary}"
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-custom:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.filter-label}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    padding: "8px 14px"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    activeBorderColor: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
    iconColor: "{colors.muted}"
    padding: "0 {spacing.base}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    fontWeight: 700
    height: 36px
    textTransform: uppercase
    letterSpacing: 0.5px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Golden yellow (#e5c225) fill with dark navy text (#2d3142) at 15px uppercase 700-weight, sitting on a 4px (`{rounded.xs}`) radius at 48px tall. The pairing is intentional: the CTA uses the same color vocabulary as the bag customizer's swatches, so clicking "add to cart" feels like making a color selection. Hover drops to `button-primary-active` (#c9ab1e), and disabled washes out to `button-primary-disabled` (#f3e694) with muted text.

**`button-secondary`** — Dark navy (#2d3142) fill with white text, same dimensions and radius as primary. Used for secondary CTAs like "customize bag" or "view all" where the action is real but subordinate to the purchase flow.

**`button-ghost`** — Transparent background with a 2px navy border and navy uppercase text. Appears alongside primary on hero sections and editorial pages — "explore collection" to the right of a "shop now" yellow button. Hover fills lightly with `{colors.surface-soft}`.

### Text Input

**`text-input`** — White background, 1px `{colors.hairline}` border at `{rounded.xs}`, 48px tall. On focus, the border sharpens to `{colors.ink}`. Placeholder in `{colors.muted}`. Used in newsletter blocks and the checkout form; no floating label pattern, just conventional top-aligned labels in `{typography.title-sm}`.

### Navigation

**`nav-bar`** — Full dark navy (#2d3142) bar at 64px tall, white text and nav links in `{typography.nav-label}` at 14px/600 weight. The Timbuk2 logo wordmark appears in golden yellow (#e5c225), making it the sole pop of color in an otherwise monochrome header. On scroll, a tighter shadow appears without the bar changing color. Mobile collapses to a hamburger at left, logo centered, cart icon at right.

**`nav-dropdown`** — White fly-out panel with a 3px `{colors.primary}` top border acting as a brand underline, box shadow for depth. Category tiles use `{typography.body-sm}` links in `{colors.ink}` with a `{colors.primary}` hover underline.

**`promo-banner`** — A 36px full-width bar in golden yellow (#e5c225) sitting above the nav, with navy uppercase caption text. Used for site-wide promotions ("FREE SHIPPING ON ORDERS $49+"). The yellow on navy/yellow-on-ink rhythm anchors the entire page header zone.

### Product Card

**`product-card`** — No border radius (`{rounded.none}`), a 1px `{colors.hairline}` border, white fill. Product name in `{typography.title-sm}`, price in `{typography.price}` (700 weight), compare-at price struck through in `{colors.muted}`. On hover, lifts 2px with a subtle shadow. Badge overlays (sale, new, custom) sit in the top-left corner. The swatch strip — a row of `{rounded.full}` color circles — appears below the image to signal available colorways without requiring a hover interaction.

### Hero

**`hero`** — Full-bleed lifestyle photography with a left-to-right gradient scrim (navy at 82%, fading to transparent), headline in `{typography.display-xl}` white, body copy in `{typography.body-md}` white, and a `button-primary` CTA. Min-height 560px. On mobile the scrim transitions to a bottom-to-top gradient so the text reads clearly over the image below.

**`hero-split`** — Two-column layout used for category pages: left panel dark navy (#2d3142) with white headline and CTA, right panel light (#f5f5f5) with the product image. No border radius, no gap — the hard edge between panels mirrors the angular button aesthetic.

### Customizer

**`color-swatch`** — 32px circles at `{rounded.full}`, rendered in the actual bag color (e.g., #42583f for forest, #f03680 for pink). Selected state shows a 2px navy ring with a 2px gap, created via `box-shadow`. Swatches are grouped by zone: panel, strap, lining, hardware — each group labeled in `{typography.swatch-label}` (11px uppercase, 600 weight, `{colors.muted}`).

**`custom-builder-panel`** — The core interactive surface: a light-gray (#f5f5f5) panel with 1px hairline border and 8px radius, divided into labeled sections for each bag zone. A step indicator line in `{colors.primary}` connects completed zones. The live 3D or 2D bag preview sits to the right in a white canvas area.

### Badges

**`badge-sale`** — Burnt orange (#d76800) fill, white text, 4px radius, uppercase 11px. Overlays product card imagery top-left.

**`badge-new`** — Dark navy fill, white text, same dimensions. Signals new arrivals without competing with sale pricing.

**`badge-custom`** — Golden yellow fill, navy text — appears on the customizer entry point card, matching the primary CTA color to reinforce that customization is the main brand action.

### Collection Filter

**`collection-filter`** — Inline pill-style filter buttons, 13px/500 weight, 1px hairline border at `{rounded.xs}`. Inactive: white background, navy text. Active: navy background, white text. Used to filter by category (messenger, backpack, tote), feature (laptop sleeve, waterproof), and color family. The color-family filter tiles show a small color dot beside the label.

### Search

**`search-bar`** — Light gray (#f5f5f5) fill, 44px tall, `{rounded.xs}`, no elevation. A muted search icon sits inline at left. Expands to full-width on mobile. No autocomplete dropdown styling was extractable.

### Footer

**`footer`** — Dark navy fill matching the nav, with a 3px `{colors.primary}` top border as a brand bookend. Section headings in `{typography.title-sm}` white, links in `{typography.body-sm}` at #dedede resting, warming to golden yellow (#e5c225) on hover. Social icons appear as minimal line icons in white. The footer bottom strip carries the Timbuk2 logo in yellow and a single legal-text line in `{colors.muted-soft}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger + centered logo + cart icon; hero switches to bottom-gradient scrim; hero-split stacks vertically with navy panel on top; product grid goes 2-up with compressed card padding; color-swatch row truncates to 6 swatches with "+N more" label; custom-builder-panel becomes a full-screen modal sheet |
| Tablet | 744–1128px | Nav shows top-level items, secondary items in hamburger overflow; product grid 3-up; hero-split becomes 40/60 column split; custom-builder-panel moves to a side drawer; filter bar scrolls horizontally |
| Desktop | 1128–1440px | Full nav with mega-menu dropdowns; product grid 4-up; hero at 560px min-height; custom-builder-panel shows as persistent side panel next to preview canvas; promo-banner visible |
| Wide | > 1440px | Content max-width caps at 1400px centered; hero image fills full bleed behind contained content column; product grid stays 4-up with expanded card padding |

### Touch Targets

- All primary action buttons minimum 48px tall
- Color swatch circles minimum 32px with 8px gap (effective hit area ~40px)
- Nav hamburger icon minimum 44×44px
- Filter pill buttons minimum 40px tall on mobile
- Footer links minimum 44px line-height on mobile to prevent mis-taps

### Collapsing Strategy

- Navigation: full links → top-level only with overflow hamburger → full hamburger at mobile
- Custom builder: persistent side panel → drawer overlay → full-screen modal sheet
- Product card swatch row: show all → truncate to 6 + count badge at mobile
- Hero copy: three-line headline at desktop → two-line at tablet → one-line large at mobile with body copy hidden
- Promo banner: full message → short message ("FREE SHIP $49+") → icon + short message on smallest breakpoints
- Collection filters: horizontal scrolling pill row replaces sidebar facets below tablet

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font family was extractable from the live site — font stacks fall back to system sans-serif; actual brand typeface may be a licensed grotesque loaded via JavaScript (Shopify theme JS bundles are opaque to static extraction)
- No `meta theme-color` was set, so mobile browser chrome color cannot be confirmed — navy #2d3142 is inferred from nav dominance
- Custom builder interaction states (3D preview rendering, zone-hover highlights, animation timing) are JavaScript-driven and unavailable from static extraction
- Exact button border-radius values could not be confirmed from extracted CSS — `{rounded.xs}` (4px) is inferred from the brand's angular aesthetic rather than measured values
- Typography scale sizes (display, body, caption) are estimated from visual inspection patterns common to Shopify-hosted DTC brands; no computed CSS font-size values were captured
- Dark-mode palette, if any, is unconfirmed — no `prefers-color-scheme` tokens were detected
- Product card hover animation easing curves and duration values are unextracted
- Checkout and account portal pages (Shopify-hosted subdomain) likely use Shopify's own design tokens rather than Timbuk2's brand tokens and are not represented here
