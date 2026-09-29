---
version: alpha
name: "Funko Official"
source_url: "https://funko.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Dimbo-Italic — the stout, round-edged display slab used for every top-of-page headline — announces the brand's register before a single product image loads; those cartoon-adjacent letterforms are as deliberate a signal as the oversized vinyl heads themselves. The canvas splits between a deep charcoal #1d2124 header and a near-white #f3f3f7 body, staging product photography against a dim backdrop that reads as display-case lighting rather than lifestyle whitespace. Primary CTAs fire in one optic yellow (#fed555) — precisely the hue pressed onto physical Funko packaging — with dark #111111 ink on top rather than white, a counterintuitive choice that keeps the energy without reaching for contrast polish. ProximaNova handles all body and UI hierarchy across five weights (Regular through Black) plus two condensed cuts; the condensed variants compress category headers and sale callouts into tight horizontal bands suited for a catalog running to thousands of SKUs that must scan cleanly at mobile widths. Corners hold at {rounded.sm} on product cards and callout panels, {rounded.xs} on CTA buttons, and reach {rounded.full} only on filter chips — a restraint that distinguishes the store from lifestyle apps that pill-shape everything. Five accent colors carry semantic weight without announcement: red (#c92a1d) marks clearance and urgency; forest green (#008827) confirms availability and price drops; ocean blue (#0070cc) carries secondary links and interactive states; teal (#117a8b) marks collector-exclusive tiers; deep gold (#fec822) surfaces on premium and limited-edition callouts. The dark navy #1c1b37 hero and footer backdrop creates a theatric display-case quality — a spotlight void behind illuminated figures — rather than the neutral-warm canvas most DTC brands default to. Spacing runs generous for the category: {spacing.xl} gutters between product rows prevent the dense SKU grid from collapsing into noise, and {spacing.section} padded hero panels give editorial moments room to breathe against catalog density.

colors:
  primary: "#fed555"
  primary-active: "#fec822"
  primary-disabled: "#bfbfbf"
  accent-red: "#c92a1d"
  accent-red-dark: "#990000"
  accent-green: "#008827"
  accent-green-dark: "#005518"
  accent-blue: "#0070cc"
  accent-blue-dark: "#005499"
  accent-teal: "#117a8b"
  sale-red: "#cc0000"
  ink: "#111111"
  ink-secondary: "#2d2d2d"
  body: "#535353"
  muted: "#6c6c6c"
  muted-light: "#888888"
  hairline: "#dbdbdb"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f3f3f7"
  surface-card: "#f9f9f9"
  surface-mid: "#ededf3"
  surface-lavender: "#d4d4e3"
  surface-dark: "#1d2124"
  surface-navy: "#1c1b37"
  on-primary: "#111111"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Dimbo-Italic', 'Dimbo-Regular', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
    fontStyle: italic
  display-lg:
    fontFamily: "'Dimbo-Regular', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0
  display-md:
    fontFamily: "'Dimbo-Regular', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'ProximaNova-Bold', 'Proxima Nova', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "'ProximaNova-Semibold', 'Proxima Nova', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'ProximaNova-Semibold', 'Proxima Nova', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'ProximaNova-Regular', 'Proxima Nova', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'ProximaNova-Regular', 'Proxima Nova', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'ProximaNova-Regular', 'Proxima Nova', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label-condensed:
    fontFamily: "'ProximaNovaCond-Bold', 'Proxima Nova Condensed', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.6px
    textTransform: uppercase
  badge:
    fontFamily: "'ProximaNova-Bold', 'Proxima Nova', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'ProximaNova-Bold', 'Proxima Nova', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'ProximaNova-Bold', 'Proxima Nova', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'ProximaNova-Semibold', 'Proxima Nova', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  price:
    fontFamily: "'ProximaNova-Black', 'Proxima Nova', sans-serif"
    fontSize: 20px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'ProximaNova-Bold', 'Proxima Nova', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  mono:
    fontFamily: "'Geist Mono', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

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
    padding: "12px 24px"
    height: 48px
    border: none
    hover:
      backgroundColor: "{colors.primary-active}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "12px 24px"
    height: 48px
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "12px 24px"
    height: 48px
    hover:
      backgroundColor: "{colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "10px 20px"
    hover:
      borderColor: "{colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px"
    height: 44px
    focus:
      border: "2px solid {colors.primary}"
      outline: none
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "10px 16px 10px 44px"
    height: 44px
    iconColor: "{colors.muted}"
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.xs}"
      height: 36px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
    logoHeight: 40px
    activeAccent: "{colors.primary}"
    megaMenu:
      backgroundColor: "{colors.canvas}"
      textColor: "{colors.ink}"
      rounded: "{rounded.sm}"
      boxShadow: "0 8px 24px rgba(0,0,0,0.2)"
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.ink}"
    padding: "{spacing.sm}"
    aspectRatio: "1/1"
    hover:
      boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
      borderColor: "{colors.hairline}"
  hero-banner:
    backgroundColor: "{colors.surface-navy}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.title-lg}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    ctaBackground: "{colors.primary}"
    ctaText: "{colors.on-primary}"
    ctaRounded: "{rounded.xs}"
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-exclusive:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  category-chip:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.ink}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 36px
    active:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
  price-display:
    regularTypography: "{typography.price}"
    regularColor: "{colors.ink}"
    saleTypography: "{typography.price}"
    saleColor: "{colors.accent-red}"
    originalTypography: "{typography.price-sm}"
    originalColor: "{colors.muted}"
    originalDecoration: line-through
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.surface-soft}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} {spacing.xl}"
    socialIconColor: "{colors.on-dark}"
    socialIconHover: "{colors.primary}"

## Components

### Buttons

**`button-primary`** — Yellow `{colors.primary}` (#fed555) fill with dark `{colors.on-primary}` ink text, set in all-caps `{typography.button-md}` at `{rounded.xs}` corners and 48px fixed height. On hover the background deepens to `{colors.primary-active}` (#fec822); the disabled state falls back to `{colors.primary-disabled}` (#bfbfbf) with `{colors.muted}` text and a `not-allowed` cursor. This is the only yellow element in the interactive layer, keeping the CTA unambiguous across every page context.

**`button-secondary`** — Charcoal `{colors.surface-dark}` fill with white `{colors.on-dark}` text; matches the nav-bar surface so it reads as part of the dark-mode vocabulary. Darkens to `{colors.ink}` on hover. Used for secondary CTAs on hero panels, collection headers, and product detail pages where the primary yellow is already occupied.

**`button-ghost`** — Transparent with a `{colors.hairline}` 1px border and dark `{colors.ink}` text in `{typography.button-sm}`. Border strengthens to `{colors.ink}` on hover. Appears as a filter-clear control, "see all" link-button, or secondary action alongside a primary CTA, keeping visual weight minimal.

### Navigation

**`nav-bar`** — Fixed 64px bar on `{colors.surface-dark}` (#1d2124) with white `{colors.on-dark}` links in `{typography.nav-link}`. A `{colors.primary}` yellow accent marks the active top-level item. Mega-menu panels drop onto a white `{colors.canvas}` background with `{rounded.sm}` corners and a pronounced box-shadow, providing maximum legibility contrast against the dark bar above. The logo sits at 40px height, left-aligned on desktop.

### Search

**`search-bar`** — Mounts inside the nav bar on desktop; moves below the nav on mobile. Uses `{colors.surface-soft}` fill with `{rounded.sm}` corners and a left-side loupe icon in `{colors.muted}`. The submit button is a small `{colors.primary}` yellow chip at `{rounded.xs}`. On focus, the border transitions to `{colors.primary}` to reinforce the brand's interactive color.

### Product Grid

**`product-card`** — White `{colors.canvas}` tile with `{rounded.sm}` corners and a hairline `{colors.hairline-soft}` border. The image occupies a 1:1 square tile against `{colors.surface-soft}`; `badge-sale` or `badge-new` overlays anchor to the top-left corner of the image. Title uses `{typography.title-sm}` in `{colors.ink}`; price uses `{typography.price-sm}`. On hover a soft shadow lifts the card without shifting its bounds. Inner padding is `{spacing.sm}` on all sides.

### Hero & Editorial

**`hero-banner`** — The signature dark navy `{colors.surface-navy}` (#1c1b37) backdrop, 480px minimum height, with Dimbo-Italic headline in `{typography.display-xl}` and subhead in `{typography.title-lg}`, both in white `{colors.on-dark}`. Padding runs `{spacing.section}` vertically and `{spacing.xl}` horizontally, giving the type generous breathing room before the product grid begins. The inline CTA uses `{colors.primary}` yellow fill at `{rounded.xs}`, consistent with the global button-primary. On collection pages the banner collapses to a narrower 200px callout band with the same color tokens.

### Badges & Tags

**`badge-sale`** — Urgent `{colors.sale-red}` (#cc0000) chip with white `{colors.on-dark}` all-caps text in `{typography.badge}`, placed top-left on product tile images. Used for percentage discounts and clearance states; its red color sits outside the standard accent palette to ensure it reads as an alarm rather than a category signal.

**`badge-new`** — Forest green `{colors.accent-green}` (#008827) with the same geometry and typography as `badge-sale`. Marks new arrivals and recently restocked SKUs. The green/red badge pair creates an unambiguous traffic-light read across the product grid.

**`badge-exclusive`** — Brand yellow `{colors.primary}` (#fed555) with dark `{colors.on-primary}` ink text. Reserved for Pop! Exclusives, convention exclusives, and retailer-specific releases. The yellow badge signals special status without the urgency register of the red sale badge; it is the only non-image element on a product card that shares the primary CTA color.

### Filter & Category

**`category-chip`** — `{colors.surface-mid}` (#ededf3) background with `{colors.ink}` text in `{typography.label-condensed}` (condensed bold, uppercase, tracked at 0.6px). Pill-shaped at `{rounded.full}`, height 36px. The active state swaps to `{colors.primary}` yellow fill with `{colors.on-primary}` dark text — the only other context outside of CTAs where the primary yellow appears as a fill. Chips scroll horizontally at mobile with visible overflow to hint at more options.

### Pricing

**`price-display`** — Regular price in `{colors.ink}` at `{typography.price}` (ProximaNova-Black, 20px). Sale price renders in `{colors.accent-red}` at the same scale; the original price is simultaneously shown in `{colors.muted}` with `line-through` decoration at `{typography.price-sm}`. The red/muted pairing creates an unambiguous markdown read without requiring a separate badge element around the price block.

### Footer

**`footer`** — `{colors.surface-dark}` (#1d2124) background matching the nav bar, closed at the top with a `3px solid {colors.primary}` yellow border — the brand color's final punctuation mark on the page. Column headings use `{typography.title-sm}` in `{colors.on-dark}`; body links use `{typography.body-sm}` in `{colors.surface-soft}` for soft contrast against the dark surface. Social icons default to `{colors.on-dark}` white, flipping to `{colors.primary}` yellow on hover. Padding is `{spacing.xxl}` vertical and `{spacing.xl}` horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger over `{colors.surface-dark}`; hero headline drops to `{typography.display-md}`; category chips scroll horizontally; search bar moves below nav |
| Tablet | 744–1128px | Two- or three-column product grid; primary nav categories visible with hamburger for overflow; hero shifts to 60/40 text-image split at reduced height |
| Desktop | 1128–1440px | Four-column product grid; full horizontal nav with mega-menu dropdowns; hero spans full viewport width; search bar sits inside nav bar |
| Wide | > 1440px | Five- or six-column product grid; max-width container centered with `{colors.surface-dark}` extending edge-to-edge on nav and hero; content constrained to ~1440px |

### Touch Targets

- All buttons and chips maintain a minimum 44×44px tappable area regardless of visible height
- Category chips at 36px visual height are padded to 44px tap target
- Badge overlays are display-only and require no tap target sizing
- Mobile nav drawer rows use at least 48px height with full-width tap area
- Product card touch target covers the entire tile including image and text block

### Collapsing Strategy

- Top nav collapses to a hamburger icon at < 744px; mega-menu subcategories become full-screen slide-in drawer panels over `{colors.surface-dark}`
- Footer four-column link grid collapses to two columns at tablet and a single-column accordion at mobile
- Product grid reduces 4-col → 3-col → 2-col → 1-col across Desktop → Tablet → Mobile
- Category chip row converts from flex-wrap to horizontal scroll at < 744px with a right-side fade mask to signal overflow
- Hero banner minimum height reduces from 480px to 280px at mobile; Dimbo display headline scales from 48px to 28px (`{typography.display-md}`)
- Price display stacks sale and original price vertically at mobile rather than inline

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact border-radius values not confirmed from CSS extraction; `{rounded.xs}` (4px) and `{rounded.sm}` (8px) approximated from visual inspection of buttons and cards
- Dimbo font appears to be a single-weight display typeface used only at display scale; its full character set, fallback behavior, and italic-vs-regular switching logic are not documented
- Mega-menu animation timing and easing (fade, slide, duration) not captured from extracted data
- Focus-ring and keyboard navigation outline styles not extracted; color and width unknown
- Seasonal or campaign theme overlays (San Diego Comic-Con, Halloween, Spooky season) likely swap hero colors and badge accent hues — these states are not reflected in the token set
- Cart drawer and checkout flow component styles not captured; they may use a partially distinct component sub-system
- Personalized Pops custom-builder interface appears to be a separate interactive experience with its own layout and component language not covered here
- `#d4d4e3` (surface-lavender) and `#117a8b` (accent-teal) usage contexts were not fully confirmed; assigned to surface and exclusive-tier roles based on positional inference from the extracted palette
