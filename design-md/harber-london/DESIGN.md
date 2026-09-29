---
version: alpha
name: "Harber London"
source_url: "https://www.harberlondon.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The tan that defines Harber London — `#af9363`, a shade indistinguishable from fresh vegetable-tanned hide — appears not as decoration but as structural identity: it governs every primary CTA, every leather-hue callout, and the small stitching-detail icons that punctuate the product grid. The canvas underneath runs warm, cycling between `#f5f1ee` and `#f5f2eb` rather than clinical white, so full-grain leather photography reads as continuity rather than contrast. Against that warmth, the type system runs two registers: Libre Baskerville at large display sizes carries the Old World craft authority that a brand selling £200 cardholders requires, while Neue Haas Unica handles all UI chrome — quantity selectors, nav labels, shipping banners — with the disciplined neutrality of Swiss print. An unexpected deep teal, `#108474`, cuts through the earth-tone palette on selected accent moments: free-delivery banners, availability indicators, and the active underline in tabbed navigation. It is cool, mineralic, and deliberate — the only hue on the page with no leather analogue. Product cards carry almost no chrome: a soft `{colors.surface-soft}` tray, a hairline border at `#e9e9e9`, and a Libre Baskerville product name set at 16px regular weight, trusting the object image to do the persuasion. Buttons are pressed flush — border-radius sits at 2px, a near-hard corner that signals craft over consumer-tech friendliness, echoing the squared-off edges of press-stamped leather hardware. The checkout corridor tightens to a single column with generous `{spacing.xxl}` vertical rhythm, reducing distraction at the highest-intent moment on the site. Mobile collapses the top nav to a minimal hamburger while the Harber London wordmark stays centred and visible at all breakpoints, functioning as the single fixed visual anchor across device widths.

colors:
  primary: "#af9363"
  primary-active: "#8a5533"
  primary-disabled: "#d4c4a8"
  ink: "#0b0b0b"
  body: "#4f4f4f"
  muted: "#7b7b7b"
  muted-soft: "#9c9c9c"
  hairline: "#e9e9e9"
  hairline-strong: "#dadada"
  canvas: "#ffffff"
  surface-soft: "#f5f1ee"
  surface-card: "#fefefe"
  surface-warm: "#f5f2eb"
  on-primary: "#ffffff"
  accent-teal: "#108474"
  accent-teal-light: "#edf5f5"
  leather-mid: "#805536"
  leather-light: "#ae9163"
  text-mid: "#555555"
  scrim: "#0b0b0b"

typography:
  display-xl:
    fontFamily: "'Libre Baskerville', Baskerville, Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Libre Baskerville', Baskerville, Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Libre Baskerville', Baskerville, Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Neue Haas Unica', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px
  title-md:
    fontFamily: "'Neue Haas Unica', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.05px
  title-sm:
    fontFamily: "'Neue Haas Unica', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Neue Haas Unica', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Neue Haas Unica', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Neue Haas Unica', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-uppercase:
    fontFamily: "'Neue Haas Unica', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Neue Haas Unica', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Neue Haas Unica', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Neue Haas Unica', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.1px
  product-name:
    fontFamily: "'Libre Baskerville', Baskerville, Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  price:
    fontFamily: "'Neue Haas Unica', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.product-name}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    imageTray: "{colors.surface-soft}"
    contentPadding: "{spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "{spacing.section}"
  collection-header:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-lg}"
    captionTypography: "{typography.body-md}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.section}"
  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 4px 10px
  delivery-banner:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  product-tag:
    backgroundColor: "{colors.accent-teal-light}"
    textColor: "{colors.accent-teal}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.ink}"
    borderDefault: "1px solid {colors.hairline-strong}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline-strong}"
    typography: "{typography.caption}"
    activeTextColor: "{colors.ink}"
  rating-stars:
    starColor: "{colors.primary}"
    emptyStarColor: "{colors.hairline-strong}"
    typography: "{typography.caption}"
  trust-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    iconColor: "{colors.primary}"
    paddingVertical: "{spacing.lg}"
    paddingHorizontal: "{spacing.section}"
    borderTop: "1px solid {colors.hairline}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    nameTypography: "{typography.product-name}"
    priceTypography: "{typography.price}"
    borderLeft: "1px solid {colors.hairline}"
    width: 400px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.muted-soft}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — The primary CTA wears `{colors.primary}` (`#af9363`) with white text set in `{typography.button-md}`: 14px Neue Haas Unica, weight 500, tracked 0.8px, forced uppercase. Near-flush `{rounded.xs}` corners (2px) reject pill-shaped consumer friendliness in favour of the squared-off edge found on press-stamped leather hardware. Active state deepens to `{colors.primary-active}` (`#8a5533`), the shade of aged oiled leather; disabled washes out to `{colors.primary-disabled}` (`#d4c4a8`). Height is fixed at 48px with 14px vertical and 28px horizontal padding.

**`button-secondary`** — White fill with a 1px `{colors.ink}` border and `{colors.ink}` uppercase text, sharing the 2px radius and 48px height of its primary sibling. It functions as the add-to-wishlist or "Continue shopping" counterweight. On hover, the background shifts to `{colors.surface-soft}` to acknowledge the interaction without colour drama.

**`button-ghost`** — Transparent background, `{colors.body}` text, no border, underlined. Reserved for tertiary actions like "View full details" and soft cancel flows where adding visual weight would disrupt page hierarchy.

### Text Input

**`text-input`** — 48px tall, 1px `{colors.hairline}` border, `{rounded.xs}` corners. On focus, the border shifts to `{colors.primary}` with no shadow bloom — keeping the focus ring warm rather than reaching for the electric-blue browser default that would fight the palette. Placeholder text in `{colors.muted}` at `{typography.body-md}`.

### Navigation

**`nav-bar`** — 64px fixed header on `{colors.canvas}`, separated from page content by a single 1px `{colors.hairline}` rule. Left: collection links in `{typography.nav-link}` (14px Neue Haas Unica) on desktop, hamburger on mobile. Centre: the Harber London wordmark in `{typography.display-md}` Libre Baskerville. Right: search icon, wishlist, and cart with count badge. The bar does not shift colour or gain shadow on scroll — it remains grounded and white across all scroll positions.

### Product Card

**`product-card`** — A flat `{colors.surface-card}` rectangle with a 1px `{colors.hairline}` border and zero radius. Product photography sits on a `{colors.surface-soft}` (`#f5f1ee`) tray at the card top, creating a warm lightbox for the leather object without requiring a separate background layer. The product name renders in `{typography.product-name}` — 16px Libre Baskerville, weight 400 — lending craftsmanship authority to even short SKU strings. Price appears immediately below in `{typography.price}` at a slightly lighter visual weight. A hover state swaps to a secondary lifestyle image via CSS opacity transition. `{color-swatch}` dots (20px, `{rounded.full}`) line up below the price for multi-colourway SKUs, with selected state indicated by a 2px `{colors.ink}` ring.

### Hero Banner

**`hero-banner`** — Full-bleed image or flat `{colors.surface-soft}` panel at minimum 560px tall. The heading uses `{typography.display-xl}` (48px Libre Baskerville, regular weight); the subheadline uses `{typography.body-md}`. A `button-primary` CTA sits 24px below the subheadline. Copy is left-aligned on desktop and centred on mobile. No overlay scrim is applied over photography — Harber London shoots against light, warm backgrounds that require no darkening treatment.

### Collection Header

**`collection-header`** — A contained band in `{colors.surface-warm}` (`#f5f2eb`) spanning full width, housing the collection title in `{typography.display-lg}` and a one-sentence editorial descriptor in `{typography.body-md}`. It functions as a transitional pause between the nav and the product grid — a warm landing zone before the product matrix begins. Padding is generous at `{spacing.xxl}` vertical to let the serif heading breathe.

### Material Badge

**`material-badge`** — A small rectangular chip with `{colors.surface-soft}` fill, a 1px `{colors.primary}` border, and `{colors.primary-active}` text in `{typography.label-uppercase}` (11px, tracked 1.2px, uppercase). Used to call out leather provenance — "Full-Grain Leather", "Veg-Tan", "Deadstock" — reinforcing material credibility without overloading the product card. Zero border-radius echoes the pressed-leather hardware motif.

### Delivery Banner

**`delivery-banner`** — A slim full-width strip in `{colors.accent-teal}` (`#108474`) placed above the main nav or within product pages. White `{typography.body-sm}` copy, centred. The teal is the brand's only cool hue; restricting it to high-value messaging (free delivery thresholds, dispatch guarantees) preserves its signal strength — using it for decorative purposes would dilute it immediately.

### Product Tag

**`product-tag`** — Small rectangular chip in `{colors.accent-teal-light}` (`#edf5f5`) with `{colors.accent-teal}` text set in `{typography.label-uppercase}`. Applied as system-state labels: "New", "Personalise", "Ships in 24h". Hard `{rounded.none}` corners match the brand's no-pill philosophy across all small UI elements.

### Trust Strip

**`trust-strip`** — A `{colors.surface-soft}` horizontal band with four centred trust pillars (Free Returns / Handmade in London / Lifetime Guarantee / Carbon Neutral Delivery), each with a small line-style icon in `{colors.primary}` above a `{typography.caption}` label. A 1px `{colors.hairline}` top rule separates it from the product grid above. This component appears both below the hero and above the footer.

### Rating Stars

**`rating-stars`** — Star icons rendered in `{colors.primary}` (`#af9363`) rather than the conventional yellow, so the rating motif inherits the leather-tan palette rather than breaking it. Empty stars use `{colors.hairline-strong}`. Review count and score text in `{typography.caption}`.

### Cart Drawer

**`cart-drawer`** — A 400px right-side panel sliding over the page on add-to-cart, on `{colors.canvas}` white. Line items show thumbnail, product name in `{typography.product-name}`, and price in `{typography.price}`. The checkout CTA uses `button-primary` at full drawer width. A 1px `{colors.hairline}` left border separates the panel from the dimmed page content beneath. On mobile, the drawer becomes full-screen.

### Footer

**`footer`** — Deep `{colors.ink}` (`#0b0b0b`) ground with `{colors.canvas}` column headings in `{typography.title-sm}` (13px Neue Haas Unica, uppercase, tracked 0.5px) and `{colors.muted-soft}` body links in `{typography.body-sm}`. Four-column layout on desktop collapses to stacked accordions on mobile. Social icons and payment-method logos live in the bottom gutter at reduced opacity to avoid visual competition with the link columns.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centred wordmark; hero copy centres; hero min-height reduces to 380px; collection-header stacks vertically with reduced padding; material-badge wraps inline below product name; cart-drawer becomes full-screen overlay |
| Tablet | 744–1128px | Two-column product grid; nav shows wordmark left + icons right with mega-menu hidden; hero shifts to 50/50 split image-text layout; footer reduces to two columns; trust-strip holds four pillars in a tighter row |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu nav with collection imagery; hero at full 560px; trust-strip displays four pillars at comfortable spacing; cart-drawer is 400px panel |
| Wide | > 1440px | Content maxes at 1440px centred; four-column product grid; hero padding expands symmetrically; footer gains wider gutters between columns |

### Touch Targets

- All interactive targets minimum 44×44px on touch viewports
- Color swatches expand to 28px diameter on mobile
- Nav hamburger maintains a 44×44px hit area regardless of icon visual size
- Cart, wishlist, and search icons in nav achieve 44px touch height via vertical padding

### Collapsing Strategy

- Footer link groups collapse to accordions on mobile (chevron toggle, max-height CSS animation)
- Mega-menu navigation disappears below 1128px and is replaced by an off-canvas drawer
- Product filter sidebar converts to a bottom-sheet modal on mobile
- Trust strip reduces from four static pillars to a horizontally scrollable carousel below 744px
- Cart drawer becomes a full-screen overlay on mobile rather than a 400px side panel

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Animation timing and easing curves not extractable from static extraction — hover transitions, drawer open/close, and image-swap durations are estimated
- Exact mega-menu column structure (number of columns, featured image dimensions) not confirmed
- Icon library source not identified — likely a custom SVG set; JudgemeIcons and JudgemeStar are review-widget-only assets
- Exact Neue Haas Unica weights available in the licence not confirmed; 400 and 500 assumed safe; weight 300 (light) may not be licensed
- Personalisation and engraving UI pattern not available — a bespoke product flow not reflected in the component set above
- `#1755aa` (blue) and `#fbcd0a` (yellow) appear in the extracted palette but have no clear brand role — likely payment-badge or third-party widget colours
- `#a89cc8` (lavender) and `#c1e6e6` (pale teal) appear at low frequency — possibly leather colour-option swatches for specific SKUs rather than UI tokens
- Exact product card hover transition type (opacity crossfade vs. CSS transform) not confirmed from static audit
