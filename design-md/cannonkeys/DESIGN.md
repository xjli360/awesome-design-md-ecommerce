---
version: alpha
name: "CannonKeys"
source_url: "https://cannonkeys.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Fifty flag-palette swatches in the extracted color set are keyboard legend graphics — every group buy ships with home-nation key labels, so the brand's true voltage only surfaces when those country colors are stripped away. What remains: #d80027 crimson on every decisive CTA, #108474 deep teal pulling focus on selected states and hover surfaces, and #ddc7ab warm parchment keeping product grids from reading as purely technical. The site runs Nunito Sans as its workhorse — a rounded sans-serif that softens the hobby's spec-heavy vocabulary without feeling casual — with Baskerville held in reserve for the rare editorial headline, lending an almost cataloguey gravitas to limited-run board announcements.

  Layout geometry stays deliberately flat: {rounded.sm} on cards and inputs, {rounded.xs} on status badges, no pill shapes anywhere in the interface. Navigation rides a dark-to-darker bar (#3d4246 descending toward #202223) with #d80027 hover underlines. The group-buy lifecycle label is the brand's most distinctive UI pattern — a fixed-width uppercase chip locked to the product-card top-left corner, rotating through amber (#d87b00, INTEREST CHECK), crimson (#d80027, LIVE), teal (#108474, SHIPPING), and slate (#555555, FULFILLED) to communicate a product's place in the months-long production cycle.

  Product photography sits on #f9fafb off-white with keycap macro shots cropped square, giving the grid a dense collector's-inventory rhythm. Spacing is generous between rows ({spacing.xl} gap) and tight within cards ({spacing.sm} internal padding). The search and filter experience prioritizes SKU-style facets — switch type, layout, form factor, availability — over discovery-mode browsing, a clear signal that the target audience already knows exactly what it wants before it arrives. Sale pricing surfaces in #d87b00 amber rather than crimson, keeping discounts legible without cannibalizing CTA color.

colors:
  primary: "#d80027"
  primary-active: "#a2001d"
  primary-disabled: "#f0a0a8"
  accent-teal: "#108474"
  accent-teal-active: "#0a5f52"
  accent-amber: "#d87b00"
  ink: "#202223"
  body: "#3d4246"
  muted: "#7b7b7b"
  muted-light: "#555555"
  hairline: "#eeeeee"
  hairline-dark: "#3d4246"
  canvas: "#f9fafb"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  surface-dark: "#202223"
  surface-mid-dark: "#3d4246"
  surface-warm: "#ddc7ab"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-teal: "#ffffff"
  badge-interest: "#d87b00"
  badge-live: "#d80027"
  badge-shipping: "#108474"
  badge-fulfilled: "#555555"

typography:
  display-xl:
    fontFamily: "Baskerville, Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  caption-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  price-display:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  badge-label:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  mono:
    fontFamily: "monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-teal}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-teal-active:
    backgroundColor: "{colors.accent-teal-active}"
    textColor: "{colors.on-teal}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    hoverAccent: "{colors.primary}"
    borderBottom: none
  nav-bar-top-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    imageBg: "{colors.canvas}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.sm}"
  gb-status-badge:
    rounded: "{rounded.xs}"
    typography: "{typography.badge-label}"
    padding: 4px 8px
    variants:
      interest-check:
        backgroundColor: "{colors.badge-interest}"
        textColor: "{colors.on-primary}"
      live:
        backgroundColor: "{colors.badge-live}"
        textColor: "{colors.on-primary}"
      shipping:
        backgroundColor: "{colors.badge-shipping}"
        textColor: "{colors.on-teal}"
      fulfilled:
        backgroundColor: "{colors.badge-fulfilled}"
        textColor: "{colors.on-primary}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    ctaButton: button-primary
  sale-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
  price-display:
    currentPriceColor: "{colors.ink}"
    currentPriceTypography: "{typography.price-display}"
    comparePriceColor: "{colors.muted}"
    comparePriceTypography: "{typography.price-compare}"
    saleCurrentPriceColor: "{colors.primary}"
    compareTextDecoration: line-through
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-dark}"
    focusBorder: "2px solid {colors.accent-teal}"
    iconColor: "{colors.muted}"
    height: 42px
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 6px 12px
    activeBackgroundColor: "{colors.accent-teal}"
    activeTextColor: "{colors.on-teal}"
    activeBorder: "1px solid {colors.accent-teal}"
  layout-flag-chip:
    width: 24px
    height: 16px
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    tooltipTypography: "{typography.caption-sm}"
  countdown-timer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    digitTypography: "{typography.display-md}"
    labelTypography: "{typography.caption-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    accentColor: "{colors.primary}"
  product-gallery:
    thumbnailBorder: "2px solid transparent"
    thumbnailActiveBorder: "2px solid {colors.primary}"
    thumbnailRounded: "{rounded.xs}"
    mainImageBg: "{colors.canvas}"
    mainImageRounded: "{rounded.sm}"
  announcement-bar:
    backgroundColor: "{colors.surface-mid-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary}"
    typography: "{typography.caption}"
    height: 36px
  spec-table:
    headerBg: "{colors.surface-soft}"
    headerTypography: "{typography.title-sm}"
    rowBorderColor: "{colors.hairline}"
    labelTypography: "{typography.body-sm}"
    valueTypography: "{typography.body-sm}"
    monoValue: "{typography.mono}"
    rounded: "{rounded.sm}"
    rowHeight: 36px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "1px solid {colors.hairline-dark}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Crimson (#d80027) fill with white text at 44px tall, {rounded.sm} corners, Nunito Sans Bold 15px with 0.3px tracking. Used for "Add to Cart," "Join Group Buy," and all primary account actions. Active state drops to #a2001d; disabled fades to dusty rose (#f0a0a8) — the red language is preserved even in inactive states rather than switching to a neutral gray.

**`button-secondary`** — White fill with a 1px {colors.hairline} border and {colors.ink} text. Appears paired alongside button-primary for actions like "Add to Wishlist" or "View Build Guide." Padding mirrors button-primary so the two sit at identical height in a side-by-side layout.

**`button-teal`** — Deep teal (#108474) fill with white text, identical geometry to button-primary. Used for confirmation flows and availability-notification actions, visually distinguishing "I want in" (teal) from "buy now" (crimson). Active darkens to #0a5f52.

### Nav Bar

**`nav-bar`** — Full-width dark (#202223) bar at 60px height. Nav links in Nunito Sans SemiBold 14px, white text, with a #d80027 underline on hover. No drop shadow — the dark surface provides separation from the light page content without additional chrome. A 36px crimson announcement strip (`nav-bar-top-strip`) rides above carrying sale copy or GB deadline notices in uppercase caption type.

### Product Card

**`product-card`** — White card at {rounded.sm} with 1px {colors.hairline} border. Keycap photography sits on the {colors.canvas} (#f9fafb) image background, cropped square. Title renders in {typography.title-sm} Nunito Sans SemiBold; price in {typography.price-display} Bold 20px. The `gb-status-badge` locks to the card's top-left image corner. When on sale, `sale-badge` occupies the top-right corner in amber, with the compare price struck through in {colors.muted} below the current price.

### Group-Buy Status Badge (`gb-status-badge`)

The brand's most operationally distinct UI element: a fixed-size uppercase chip in {rounded.xs} at 10px Nunito Sans ExtraBold with 1px letter spacing, pinned to the product image corner in four lifecycle colors:
- **INTEREST CHECK** — amber ({colors.badge-interest}) signals early demand gathering, no commitment yet
- **LIVE** — crimson ({colors.badge-live}) matches the CTA color, reinforcing urgency and action
- **SHIPPING** — teal ({colors.badge-shipping}) signals fulfilment underway, a calmer resolved state
- **FULFILLED** — slate ({colors.badge-fulfilled}) archives completed runs for reference browsing

### Countdown Timer (`countdown-timer`)

A dark-surface ({colors.surface-dark}) block placed on LIVE group-buy product pages. Digits render in {typography.display-md} Nunito Sans Bold with {typography.caption-sm} unit labels below each stack. A {colors.primary} crimson accent rule underlines each digit group. Communicates deadline pressure without additional copy — the color alone carries the urgency.

### Search Bar (`search-bar`)

White fill, {rounded.sm}, 1px {colors.hairline-dark} border that focuses to a 2px teal ({colors.accent-teal}) ring. The teal focus state is deliberate — it is the only place in the UI where interaction focus uses teal rather than crimson, distinguishing utility from purchase. Filter chips beneath follow the same teal-active language for consistency.

### Filter Chips (`filter-chip`)

Compact rectangular chips in {rounded.xs} with {colors.surface-soft} fill. On selection: teal fill ({colors.accent-teal}), white text, teal border. Typography uses {typography.caption} at 12px uppercase with 0.5px tracking. Facets include switch type, form factor, PCB compatibility, hotswap support, and availability status — a spec-first filtering vocabulary for an enthusiast audience.

### Layout Flag Chips (`layout-flag-chip`)

24×16px country-flag images in {rounded.xs} borders, arranged in a horizontal scroll row on product pages for selecting regional key legends (ANSI, ISO, JIS, Nordic, etc.). These flag graphics are the source of nearly every non-brand color in the extracted palette — they are decorative product data, not brand signals. Each chip sits within a minimum 36×36px tap target for accessibility.

### Hero Banner (`hero-banner`)

Full-bleed dark ({colors.surface-dark}) section, minimum 480px tall. Headline in {typography.display-xl} Baskerville — the only place the serif appears — with {typography.body-md} Nunito Sans body copy. A subtle dark-to-transparent gradient anchors the bottom edge where text overlaps photography. CTA uses `button-primary`.

### Price Display (`price-display`)

Current price in {typography.price-display} Bold 20px in {colors.ink}; compare price in {typography.price-compare} 14px struck through in {colors.muted}. On sale, the current price color switches to {colors.primary} crimson — the only instance where crimson applies to non-interactive text, creating an unambiguous sale signal that the brand color vocabulary supports without extra iconography.

### Spec Table (`spec-table`)

Used on PDPs for switch actuation specs, PCB layout data, and build dimensions. Header row at {colors.surface-soft} in {typography.title-sm}; value cells in {typography.body-sm}; numeric and SKU values in {typography.mono} for scan-readability. {rounded.sm} outer container, {colors.hairline} row borders, 36px row height for dense listing without scrolling.

### Footer (`footer`)

Full-width dark ({colors.surface-dark}) block with column layout for nav links, social handles, and newsletter input. Link text defaults to {colors.on-dark} white with {colors.primary} crimson hover. Headings in {typography.title-sm} white; body links in {typography.body-sm} {colors.muted}. A single 1px {colors.hairline-dark} top border divides footer from content — no additional shadow or transition.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with slide-in drawer; hero reduces to 320px min-height; filter chips scroll horizontally in a single row; countdown timer reflows to 2×2 digit grid |
| Tablet | 744–1128px | 2-column product grid; nav shows primary links with secondary in overflow menu; hero at 400px; filter sidebar becomes bottom-sheet drawer |
| Desktop | 1128–1440px | 3–4 column product grid; full nav bar with all primary links; left-panel facet filters visible by default; hero at full 480px |
| Wide | > 1440px | Container max-width 1440px centered; grid holds at 4 columns; hero gains lateral padding; footer columns gain breathing room |

### Touch Targets
- All button heights minimum 44px for reliable thumb activation
- Filter chips have minimum 36px touch area via 8px vertical padding
- Flag chips (24×16px visual) are wrapped in a minimum 36×36px tap target
- Nav hamburger icon minimum 44×44px hit area
- Product card entire surface is tappable — no tap-target ambiguity between title and image zones

### Collapsing Strategy
- Announcement bar collapses to a single-line ticker/marquee on mobile (< 744px)
- Product filters move from left sidebar (desktop) to a bottom-sheet drawer (mobile and tablet)
- Spec table reflows from multi-column to single-column stacked label/value pairs on mobile
- Countdown timer digit groups reflow from a single horizontal row to a 2×2 grid on mobile
- Footer columns stack vertically on mobile; newsletter input goes full-width
- GB status badge remains pinned to card corner at all breakpoints — never hidden

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font weights for Nunito Sans not confirmed against loaded CSS — Bold/ExtraBold assignments are inferred from visual hierarchy; actual weights may differ
- No meta theme-color extracted; mobile browser chrome color unknown (likely #202223 or #d80027 based on dark nav pattern)
- Exact border-radius values unconfirmed from computed styles — {rounded.sm} (8px) is estimated from visual inspection
- Actual nav bar height not measured; 60px is an informed estimate
- Product card hover state (shadow, image zoom scale) not observable from static extraction
- Dark-mode support unconfirmed; the site may be light-only despite dark nav/footer/hero surfaces
- Baskerville as editorial display font is inferred; the live site may use Nunito Sans exclusively for headlines
- JudgemeIcons and JudgemeStar are third-party review widget fonts, not brand assets — review star rendering may differ from native star glyphs
- Exact flag-chip row scroll behavior (snap, free-scroll, paginated) not confirmed
