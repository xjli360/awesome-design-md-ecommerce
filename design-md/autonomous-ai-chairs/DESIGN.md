---
version: alpha
name: "Autonomous.ai (Chairs)"
source_url: "https://www.autonomous.ai/office-chairs"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Fraunces — an optical-size variable serif that adjusts its own letterform contours as size changes — headlines a brand whose product line is literally called "Autonomous," a coincidence too precise to be accidental. Against that literary display face, the body and UI layer runs entirely in system fonts (-apple-system, BlinkMacSystemFont, Helvetica Neue), creating a deliberate two-register system: poetic at the hero scale, efficient inside the product grid. The primary blue, #1174dc, reads closer to enterprise SaaS than consumer furniture — an intentional signal that these are chairs built for people who treat their home office as infrastructure rather than décor. Dark supporting neutrals (#111111 ink, #4a4a4a body) keep the canvas dense and product-forward; there are no warm creams or lifestyle off-whites anywhere in the palette. Status colors are operationally literal: #ff3333 for out-of-stock and error states, #1ab759 for in-stock confirmations, #ff9900 for flash-sale timers and deal badges — a traffic-light scheme that scales to a brand moving thousands of chairs per month across dozens of SKUs. Light blue tints (#e7f0ff, #d0e1fe, #eff5f8) surface in comparison highlights and feature callout backgrounds, extending the primary hue into a full tonal band without introducing a second color family. JetBrains Mono appears for numerical spec displays — weight capacity in kilograms, lumbar adjustment range in millimeters, seat depth — treating ergonomic data with the same typographic register as IDE terminal output. Corner radii are moderate: `{rounded.sm}` on cards, `{rounded.xs}` on badges and inputs, `{rounded.full}` on filter chips and warranty pills, resisting both the hyper-rounded consumer-app softness and the zero-radius enterprise grid. The result reads like a product configurator whose designers decided, at some inflection point, that the UI itself should carry weight.

colors:
  primary: "#1174dc"
  primary-hover: "#2a78fb"
  primary-active: "#0e5bb5"
  primary-disabled: "#a7cff8"
  primary-tint-soft: "#e7f0ff"
  primary-tint-mid: "#d0e1fe"
  primary-tint-strong: "#78b5f5"
  primary-tint-subtle: "#eff5f8"
  ink: "#111111"
  ink-strong: "#222222"
  ink-secondary: "#4a4a4a"
  body: "#555555"
  muted: "#8e8e8e"
  muted-soft: "#9c9c9c"
  hairline: "#d3d3d3"
  hairline-soft: "#f2f2f2"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#fafafa"
  surface-tint: "#eff5f8"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  status-success: "#1ab759"
  status-success-light: "#40dd7f"
  status-error: "#ff3333"
  status-error-deep: "#ea2f2f"
  status-error-soft: "#ff5858"
  status-warning: "#ff9900"
  status-warning-deep: "#ff8800"
  status-warning-soft: "#ffbb33"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Fraunces', Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1px
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-number:
    fontFamily: "'JetBrains Mono', Consolas, 'Courier New', monospace"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  spec-label:
    fontFamily: "'JetBrains Mono', Consolas, 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.6px
    textTransform: uppercase
  price-display:
    fontFamily: "'JetBrains Mono', Consolas, 'Courier New', monospace"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  price-sm:
    fontFamily: "'JetBrains Mono', Consolas, 'Courier New', monospace"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  countdown:
    fontFamily: "'JetBrains Mono', Consolas, monospace"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 2px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
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
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.primary}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-cta-large:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 40px
    height: 56px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    height: 44px
    padding: 0 16px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
  nav-bar-scrolled:
    backgroundColor: "{colors.ink-strong}"
    textColor: "{colors.on-dark}"
    height: 56px
    boxShadow: "0 2px 12px rgba(0,0,0,0.35)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: 16px
    imageAspectRatio: "4/3"
    hoverShadow: "0 4px 20px rgba(0,0,0,0.10)"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink-strong}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.ink}"
  product-card-price-original:
    typography: "{typography.price-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    minHeight: 560px
    padding: 64px 32px
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subheadline:
    typography: "{typography.display-sm}"
    textColor: "{colors.primary-tint-strong}"
  spec-panel:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 24px
  spec-row-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  spec-row-value:
    typography: "{typography.spec-number}"
    textColor: "{colors.ink}"
  badge-in-stock:
    backgroundColor: "{colors.status-success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-out-of-stock:
    backgroundColor: "{colors.status-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.status-warning}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 8px 24px
    height: 40px
  countdown-timer:
    backgroundColor: "{colors.status-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.countdown}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
  warranty-badge:
    backgroundColor: "{colors.primary-tint-soft}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary-tint-mid}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  filter-chip:
    backgroundColor: "{colors.canvas}"
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
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
    borderSelected: "2px solid {colors.primary}"
    selectedRingOffset: 2px
  comparison-highlight:
    backgroundColor: "{colors.primary-tint-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  comparison-panel:
    backgroundColor: "{colors.surface-tint}"
    border: "1px solid {colors.primary-tint-mid}"
    rounded: "{rounded.sm}"
    padding: 24px
  footer:
    backgroundColor: "{colors.ink-strong}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.primary-tint-strong}"
    padding: 64px 0 40px

## Components

### Buttons

**`button-primary`** — Renders at 44px tall in #1174dc with white text, `{rounded.xs}` corners, and 24px horizontal padding. Hover brightens to #2a78fb; active press deepens to #0e5bb5; disabled drains to #a7cff8 with no opacity reduction. This is the Add to Cart and Configure CTA — every product page ends on this button.

**`button-secondary`** — White fill, 1.5px #1174dc stroke, matching blue label text. Matches `button-primary` in height and radius. Used for "Compare," "Add to Wishlist," and "View Specs" alongside a primary CTA; the blue border ensures it reads as a real action without competing.

**`button-ghost`** — Transparent fill with a 1px `{colors.hairline}` border and ink text. Handles tertiary navigation actions: "View all specs," "See full comparison," filter resets. Low visual weight keeps product content dominant.

**`button-cta-large`** — Hero and section-level CTA at 56px height, `{rounded.sm}` corners, 40px horizontal padding. Appears over the dark hero canvas where it needs to stand on its own without surrounding UI support.

### Navigation

**`nav-bar`** — Dark background at #111111, 64px tall, white text and icons. The inverted nav is the brand's single most distinctive surface choice: it signals an engineering-first company before the user has read a word. On scroll past a threshold, `nav-bar-scrolled` drops to 56px and gains a 12px box shadow to maintain legibility against lighter page backgrounds. Category links show a #1174dc underline accent on hover.

### Hero

**`hero-section`** — Full-bleed dark (#111111) section, minimum 560px tall. The Fraunces display stack enters at `{typography.display-xl}` for the main headline; sub-copy uses `{typography.display-sm}` in `{colors.primary-tint-strong}` (#78b5f5) to establish depth without introducing a second hue. Occasionally, a JetBrains Mono spec callout ("300 lb capacity") floats near the headline to ground the poetry in product fact.

### Product Card

**`product-card`** — #fafafa background, 1px `{colors.hairline-soft}` border, `{rounded.sm}` corners. On hover, shadow lifts to a 20px spread at 10% black. Product name uses `{typography.title-md}`; price renders in `{typography.price-sm}` via JetBrains Mono. Original price strikes through in `{colors.muted}`. Stock badges pin to the image corner at `{rounded.xs}`.

### Spec Panel

**`spec-panel`** — A `{colors.surface-soft}` inset panel with `{rounded.sm}` corners listing ergonomic parameters in a two-column label/value grid. Labels use `{typography.spec-label}` — JetBrains Mono, 11px, all-caps, 0.6px tracking — and values use `{typography.spec-number}` at 18px mono weight 500. The grid makes back angle, seat depth, and max load read like hardware documentation rather than marketing copy.

### Badges

**`badge-in-stock`** / **`badge-out-of-stock`** / **`badge-sale`** / **`badge-new`** — Four variants on the same base: 11px uppercase `{typography.badge}`, `{rounded.xs}`, 3px/8px padding. Green #1ab759 for stock, red #ff3333 for unavailable, amber #ff9900 with dark ink text for sale (inverted for contrast at this saturation), and primary blue for new arrivals. The four-state badge system maps directly to the fulfillment and marketing states the brand operates at scale.

### Promo Banner & Countdown

**`promo-banner`** — 40px sticky top bar in `{colors.primary}` blue with `{typography.body-sm}` white text. Carries sitewide discount codes, shipping thresholds, and event announcements. **`countdown-timer`** — Replaces or sits within the promo bar during flash sales; red #ff3333 background with JetBrains Mono at 24px, 2px letter-spacing to hold column width stable as digits tick down.

### Filter Chips & Search

**`filter-chip`** — `{rounded.full}` pill with hairline border at rest; toggles to solid `{colors.primary}` fill on activation (`filter-chip-active`). Used in the category rail and top quick-filter row to narrow by series, height range, and weight capacity. **`search-bar`** — Matches text-input geometry (44px, `{rounded.xs}`) but starts borderless on `{colors.surface-soft}`; a 1.5px primary stroke appears on focus to signal interaction readiness.

### Warranty Badge

**`warranty-badge`** — A `{rounded.full}` pill in `{colors.primary-tint-soft}` with blue text and a `{colors.primary-tint-mid}` border. "Lifetime Warranty" appears in this component near the product title — the brand's differentiating promise surfaced at the design-system level so no page omits it.

### Comparison Panel

**`comparison-panel`** — A `{colors.surface-tint}` (#eff5f8) inset section with `{colors.primary-tint-mid}` border used to surface head-to-head spec comparisons. `{comparison-highlight}` chips in `{colors.primary-tint-soft}` call out winning attributes within the table cells.

### Footer

**`footer`** — #222222 background with `{colors.muted-soft}` body text. Link text uses `{colors.primary-tint-strong}` (#78b5f5) against the dark field. Echoes the nav's dark bookend; the page opens and closes on near-black, framing product content as the lit stage between them.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark; hero headline drops to `{typography.display-md}`; spec panels stack vertically; filter chips scroll horizontally in a fixed strip; `button-cta-large` spans full width |
| Tablet | 744–1128px | Two-column product grid; nav shows primary categories inline, secondary links in hamburger drawer; hero at `{typography.display-lg}`; spec panel in two columns; promo banner text truncates to single line |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with category dropdowns; hero at `{typography.display-xl}`; left-rail filter sidebar at 240px fixed width; spec comparison table visible in full |
| Wide | > 1440px | Four-column product grid; hero content max-width 1200px centered with image fill; comparison table expands to additional columns; nav max-width constrained with generous side gutters |

### Touch Targets

- All buttons, filter chips, and nav links maintain a minimum 44×44px touch region
- Color swatches render at 24px visually but receive a 44px tap area via invisible padding
- Countdown timer digits are non-interactive; per-digit min-width holds column layout stable during animation
- Mobile filter strip items have 48px height and 12px horizontal gap for thumb navigation

### Collapsing Strategy

- Product filter sidebar (desktop left rail) becomes a bottom sheet triggered by a sticky "Filter" ghost button on mobile
- Spec comparison table scrolls horizontally on mobile and tablet rather than reflowing to stacked rows — spec numbers need column alignment to be readable
- Hero layout splits text-left / image-right at desktop; stacks to image-top / text-below under 744px
- Promo banner collapses from multi-message carousel to single truncated string on mobile; countdown timer shrinks digit font from 24px to 18px
- Nav mega-menus become a full-screen slide-over drawer on touch devices with a back-stack breadcrumb

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Fraunces optical-size axis settings (opsz range, wght axis range) not confirmed from extraction — variable font parameters assumed from typical Fraunces v2 defaults
- Exact nav dropdown/mega-menu column layout, width, and hover trigger behavior not captured in static hints
- Icon set details (stroke weight, outline vs. filled, icon library origin) not present in color or font extraction
- Shadow/elevation scale beyond the product-card hover state is estimated — no box-shadow values were extractable
- Animation easing curves and transition durations not in extracted hints — ease-out assumed for micro-interactions throughout
- Exact image crop ratio for product cards (3:2 vs. 4:3 vs. square) inferred from grid structure, not confirmed
- Mobile nav drawer animation style (slide, fade, push) not determinable from static extraction
- Whether JetBrains Mono is self-hosted or loaded via CDN not confirmed; fallback stack (Consolas, Courier New) covers most environments
