---
version: alpha
name: "Major Fitness"
source_url: "https://www.major-fitness.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A power rack built to absorb thousand-pound Olympic lifts doesn't apologize for its geometry, and Major Fitness carries that same uncompromising mass into its digital skin. The brand arrives at a visual system anchored on near-black hero sections ({colors.surface-dark}) colliding with crimson primary red ({colors.primary}) — a pairing that reads less like branding and more like a warning label stenciled onto industrial steel. Where most fitness-equipment storefronts diffuse their edges with gradient overlays and softened product cards, Major Fitness plants both feet: flat planes, zero decorative radius on interactive elements ({rounded.none} to {rounded.xs}), and product photography isolated on white canvas so matte-steel frames can carry their own weight. Display headlines run condensed and heavy — 700–800 weight at compressed widths that mirror the stenciled numerals on a weight plate rather than the smooth curves of athleisure lettering. The system oscillates deliberately between full-bleed dark hero environments ({colors.surface-dark}) and clean white product pages ({colors.canvas}), never blending the two registers into a muddled mid-tone. Specification grids — two columns, tight leading, tracked uppercase labels — perform the same function as a spec sheet stapled to a gym floor model: they tell a serious buyer exactly what they need before committing to freight delivery. Badge treatments calling out "COMMERCIAL GRADE" or "FREE SHIPPING" run in all-caps micro-label at minimal size with heavy tracking, borrowing the visual logic of load-rating stickers. The footer anchors the entire canvas with a 3px crimson top border, a low-light reminder that this is a brand that ships barbell systems, not boutique supplements. Every spacing decision leans generous: 64px section breaks, 48px tall CTAs, and 24px interior card padding that prevents the dense spec content from collapsing into noise. The overall register is direct, load-bearing, and built for a buyer who reads weight capacity before lifestyle copy.

colors:
  primary: "#d42b2b"
  primary-active: "#b01f1f"
  primary-disabled: "#f0aaaa"
  ink: "#111111"
  body: "#333333"
  muted: "#666666"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  surface-mid: "#2d2d2d"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-yellow: "#f5c518"
  price-strike: "#999999"

typography:
  display-xl:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.2px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0
    textTransform: uppercase
  title-md:
    fontFamily: "'Barlow', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Barlow', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Barlow', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  spec-label:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price-display:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  price-sm:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  button-md:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Barlow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px

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
    height: 50px
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
    padding: 13px 27px
    height: 50px
    border: "2px solid {colors.ink}"
  button-ghost-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 50px
    border: "2px solid {colors.on-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "2px solid {colors.ink}"
    rounded: "{rounded.xs}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "none"
  nav-bar-dropdown:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
    rounded: "{rounded.none}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    height: 40px
    textAlign: center
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    ctaButton: button-primary
    overlayOpacity: 0.5
  hero-split:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    layout: "50/50 image-right"
    paddingVertical: "{spacing.xxl}"
    ctaButton: button-primary
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    imageBackground: "{colors.surface-soft}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  spec-grid:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    columns: 2
    gap: "{spacing.base}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    borderTop: "3px solid {colors.primary}"
  compare-table:
    headerBackgroundColor: "{colors.surface-dark}"
    headerTextColor: "{colors.on-dark}"
    rowEvenBackgroundColor: "{colors.surface-soft}"
    rowOddBackgroundColor: "{colors.canvas}"
    cellTypography: "{typography.body-sm}"
    headerTypography: "{typography.spec-label}"
    highlightBorder: "2px solid {colors.primary}"
    rounded: "{rounded.none}"
  category-tile:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-sm}"
    rounded: "{rounded.none}"
    overlayGradient: "linear-gradient(to top, rgba(0,0,0,0.7) 0%, transparent 60%)"
    hoverScale: 1.03
  trust-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    iconColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    paddingVertical: "{spacing.lg}"
  accordion-faq:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    iconColor: "{colors.primary}"
    padding: "{spacing.lg} 0"
  rating-stars:
    filledColor: "{colors.accent-yellow}"
    emptyColor: "{colors.hairline}"
    labelTypography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.spec-label}"
    paddingVertical: "{spacing.section}"
    borderTop: "3px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.on-dark}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.surface-mid}"
    height: 44px
    iconColor: "{colors.on-dark}"

## Components

### Buttons

**`button-primary`** — The primary CTA is a solid crimson ({colors.primary}) block at 50px height with 1px tracked uppercase lettering at 16px. Sharp `{rounded.xs}` corners reject the pill softness typical of lifestyle brands; this is a buy button built like a bumper plate. On active/press, the background shifts to `{colors.primary-active}` with no transition animation — direct, not animated. On hover, a 5% darkening via filter is acceptable; no glow, no shadow. Disabled state uses `{colors.primary-disabled}` and retains uppercase typography.

**`button-secondary`** — White fill with 2px solid `{colors.ink}` border and matching uppercase button-md typography. Used for secondary actions like "Learn More" or "Compare." On dark backgrounds, the `button-ghost-dark` variant replaces this with transparent fill and 2px white border, maintaining the same height and padding.

### Navigation

**`nav-bar`** — Full-width dark bar ({colors.surface-dark}) at 64px with `{typography.nav-link}` labels in {colors.on-dark}. Top of page sits a `promo-banner` in `{colors.primary}` at 40px, carrying free-shipping thresholds or sale callouts in tracked uppercase {typography.button-sm}. Dropdown menus use `{colors.surface-mid}` panels with no rounded corners — they extend flush below the nav rail like a drawer opening downward. No backdrop blur or shadow; the darkness of the panel provides separation.

### Product Card

**`product-card`** — White card with a 1px hairline border and `{rounded.xs}` corner. The image zone uses `{colors.surface-soft}` as background for isolated product photography. Title runs `{typography.title-sm}` in `{colors.ink}`; price runs `{typography.price-sm}`. Strikethrough pricing uses `{colors.price-strike}` with regular weight beside the active price. Badge chips — "COMMERCIAL GRADE," "NEW ARRIVAL" — are `{rounded.none}` crimson blocks sitting flush to the top-left image corner using `{typography.micro-label}`.

### Hero Sections

**`hero-dark`** — Full-bleed `{colors.surface-dark}` with a semi-transparent overlay over photography. Title in `{typography.display-xl}` in white; body copy in `{typography.body-md}` at reduced opacity (0.8). Primary button sits below with 24px gap. No centered text layout — left-aligned with 64px left padding on desktop.

**`hero-split`** — White canvas with product image occupying the right 50% and copy occupying the left, padded {spacing.xxl} vertically. Title uses `{typography.display-md}` in `{colors.ink}`. Good for category landing pages where photography needs breathing room against white.

### Spec Grid

**`spec-grid`** — Two-column grid on `{colors.surface-soft}` with a 3px `{colors.primary}` top accent. Labels in `{typography.spec-label}` (tracked uppercase, muted) pair with values in `{typography.body-sm}`. Used inline on product detail pages below the add-to-cart block. Gap is `{spacing.base}` between rows; padding is `{spacing.lg}` all sides.

### Compare Table

**`compare-table`** — Full-width table with `{colors.surface-dark}` header row carrying `{typography.spec-label}` in white. Alternating rows use `{colors.surface-soft}` and `{colors.canvas}`. The featured-product column is highlighted with a 2px `{colors.primary}` border on all sides. No rounded corners anywhere in the table. Used to compare rack models side-by-side on category and landing pages.

### Category Tiles

**`category-tile`** — Full-bleed photography with a bottom-to-top gradient overlay (rgba 0,0,0 0.7 at base, transparent at 60%). Title text in `{typography.display-sm}` sits at the bottom-left over the gradient. On hover, the image scales 1.03× via transform. No border radius — tiles are hard-edged grid cells.

### Trust Bar

**`trust-bar`** — Horizontal strip on `{colors.surface-soft}` carrying 3–4 icon + label pairs (Free Shipping, Warranty, Commercial Grade, Expert Support). Icons in `{colors.primary}`; labels in `{typography.body-sm}` `{colors.muted}`. Hairline borders top and bottom. Sits between hero and category grid sections.

### FAQ Accordion

**`accordion-faq`** — Flush-left items separated by 1px `{colors.hairline}` borders. Title row in `{typography.title-sm}` with a `{colors.primary}` chevron icon on the right. Body text in `{typography.body-sm}` expands below with 16px top padding. No animation delay — expand is immediate. No card border; the accordion lives on the raw white canvas.

### Footer

**`footer`** — `{colors.surface-dark}` base with a 3px `{colors.primary}` top border anchoring the section. Column headings in `{typography.spec-label}` (tracked uppercase, white). Links in `{typography.body-sm}` at 0.7 opacity, 1.0 on hover. Logo lockup in white, top-left of the footer grid. Bottom bar carries copyright in `{typography.caption}` with legal links at reduced opacity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero text reduces to display-sm scale; nav collapses to hamburger + logo; spec grid stacks to 1 column; trust-bar icons stack vertically 2×2; promo-banner text wraps to 2 lines at 36px height |
| Tablet | 744–1128px | 2-column product grid; hero split becomes stacked (image above, copy below); nav shows primary categories only, overflow into hamburger; compare table scrolls horizontally |
| Desktop | 1128–1440px | 3-column product grid; full nav with dropdown panels; hero-split activates 50/50 layout; spec grid 2 columns; trust-bar runs horizontal full-width |
| Wide | > 1440px | Max-width container at 1440px centered on canvas; product grid optionally 4 columns; hero padding increases to 96px vertical; footer grid expands to 5 columns |

### Touch Targets

- All buttons minimum 50px height, 44px minimum width
- Nav hamburger icon target 44×44px
- Accordion rows minimum 52px tap height
- Product card CTA affordance covers full card on mobile (card-level tap)
- Quantity stepper buttons minimum 44×44px

### Collapsing Strategy

- Navigation: full horizontal → hamburger + logo at < 1000px; dropdown panels become full-screen overlays on mobile
- Hero: 50/50 split collapses to stacked image-above-copy at < 744px; display-xl text scales down to display-sm
- Spec grid: 2-column always collapses to 1-column on mobile
- Compare table: horizontal scroll with sticky first column below 744px
- Trust bar: 4-item horizontal row wraps to 2×2 grid below 480px
- Footer: 4-column grid → 2-column → 1-column (single stacked list) on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors extracted from the live site (site likely loads design tokens via JavaScript or is behind anti-bot protection); all palette values in this file are inferred from category conventions and Major Fitness's known crimson-and-black product photography identity — verify before implementation
- No font-family stacks extracted; typography uses Barlow / Barlow Condensed as reasonable condensed-sans defaults consistent with industrial fitness brand aesthetics — confirm actual typefaces from brand assets or rendered screenshot
- No meta theme-color detected — cannot confirm mobile browser chrome tint color
- Exact button radius values (the site may use 0px sharp corners or up to 6px) are unconfirmed; {rounded.xs} (4px) is a conservative estimate
- Accent yellow ({colors.accent-yellow}) is inferred for sale/promotional badges — may not be a confirmed brand color
- Promo banner cadence, exact copy patterns, and sale-event color behavior are undocumented
- Platform is confirmed non-Shopify; underlying e-commerce platform unknown, which may affect component naming conventions in production templates
