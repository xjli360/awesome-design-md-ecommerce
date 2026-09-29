---
version: alpha
name: "Gorjana"
source_url: "https://gorjana.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  freight-big-pro doing editorial work in a dainty-jewelry context is Gorjana's most immediate surprise — the baroque ligatures of a magazine-headline serif float above grids of stackable rings and fine chain necklaces priced for everyday wear rather than occasion. The store commits to two extracted hues: near-black (#121212) ink over a white canvas, with #dedede as the only hairline breathing between page sections. That restraint is the brand's argument — a Shopify storefront that reads less like a jeweler's case and more like a California fashion magazine, right down to the lowercase wordmark set in futura-pt. The serif/sans pairing is load-bearing throughout. freight-big-pro handles all display and editorial moments — hero headlines, lookbook callouts, collection titles — at light weights that keep letterforms open and airy. futura-pt takes all functional text: navigation, labels, price strings, button copy, always tracked wide and set uppercase, a geometric chorus to the organic serif above. Together they produce a voice that is unhurried without reaching for beach vocabulary. CTAs land flat and square-cornered ({rounded.none}), reversed white-on-black for primary actions, ink-bordered white for secondary — no gradient, no drop shadow, no hover animation beyond a simple color flip. The promotional bar across the top runs #121212 with reversed caption text, functionally identical to the footer, which makes the page feel like a single tonal envelope: dark stripe, white body, dark stripe. Gift discovery is the commercial spine — "Gift's They'll Love" anchors the page title and the navigation surfaces a gift guide entry early. Product cards stay spare: image, name in body-sm futura-pt, price in a matching weight, no badge clutter or inline swatch pickers. Filter chips hold square corners and a hairline border, activating to a full ink border on selection, keeping the editorial calm intact even in the most utilitarian functional state.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#9b9b9b"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#767676"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  promo-bar: "#121212"
  on-promo: "#ffffff"

typography:
  display-xl:
    fontFamily: "'freight-big-pro', serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'freight-big-pro', serif"
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'freight-big-pro', serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.18
    letterSpacing: -0.2px
  editorial-sub:
    fontFamily: "'freight-big-pro', serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 1.8px
    textTransform: uppercase
  title-sm:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 1.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.2px
  body-sm:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.1px
  caption:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 1.2px
    textTransform: uppercase
  price:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.2px
    textTransform: uppercase
  wordmark:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 3px
    textTransform: lowercase

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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 46px
    hoverBackgroundColor: "{colors.primary-active}"

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 46px
    hoverBackgroundColor: "{colors.surface-soft}"

  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
    borderBottom: "1px solid {colors.ink}"

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 46px

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.wordmark}"

  promo-bar:
    backgroundColor: "{colors.promo-bar}"
    textColor: "{colors.on-promo}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
    padding: "0 {spacing.base}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    imageRounded: "{rounded.none}"
    nameTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    textColor: "{colors.ink}"
    gap: "{spacing.sm}"
    imageAspectRatio: "4/5"
    padding: "{spacing.sm} 0"

  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    ctaComponent: "button-primary"
    padding: "{spacing.xxl} {spacing.section}"
    textAlign: center

  editorial-module:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-lg}"
    subTypography: "{typography.editorial-sub}"
    bodyTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    layout: "split-50-50"
    gap: "{spacing.xxl}"

  collection-header:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-md}"
    subTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    textAlign: center
    paddingBottom: "{spacing.xl}"

  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderActive: "1px solid {colors.ink}"
    backgroundActive: "{colors.surface-soft}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.md}"
    height: 34px

  category-label:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "0"

  gift-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"

  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    linkColor: "{colors.on-primary}"
    linkHoverOpacity: 0.7

  search-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
    overlayColor: "{colors.ink}"
    overlayOpacity: 0.4

  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    borderLeft: "1px solid {colors.hairline}"

  section-divider:
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    marginY: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — Square-cornered ({rounded.none}), fully reversed: #ffffff label set in futura-pt tracked at 2px letter-spacing over a #121212 fill. Height is 46px with 32px horizontal padding. Hover darkens to `{colors.primary-active}`; disabled state desaturates to `{colors.primary-disabled}` with muted label. This button appears as the dominant CTA on hero banners, add-to-cart flows, and email capture modules.

**`button-secondary`** — Same dimensions and typography as primary but inverted: #121212 ink label inside a white fill with a 1px `{colors.ink}` border. Used for secondary actions like "Shop All" or "View Details" alongside a hero CTA. On hover the fill shifts to `{colors.surface-soft}`.

**`button-ghost`** — Zero background, zero border, only a 1px ink underline beneath the label. Reserved for inline navigation actions, "Learn More" links in editorial modules, and filter resets. Smallest visible footprint in the action hierarchy.

### Inputs

**`text-input`** — Full-width, square-cornered, 46px height. Hairline (#dedede) border rests to a full ink border on focus — no box-shadow, no color fill change. Placeholder text in `{colors.muted}` futura-pt body-md. Used across email capture, search, and checkout forms.

### Navigation

**`nav-bar`** — 60px tall, white canvas, hairline bottom border. Logo rendered as lowercase futura-pt wordmark (`{typography.wordmark}`) tracked at 3px. Navigation links sit in `{typography.nav-link}` — 12px futura-pt, 1.2px letter-spacing, uppercase. Icon cluster right-aligns: search, account, bag. On mobile the nav collapses behind a hamburger, replacing link rows with a full-height drawer.

**`promo-bar`** — 36px strip pinned above the nav. #121212 fill, `{colors.on-primary}` caption text, center-aligned. Communicates free shipping thresholds, site-wide promotions, and holiday messaging. Shares the same background as the footer, creating the top/bottom dark-stripe envelope.

### Product Display

**`product-card`** — No border, no rounded corners, no shadow. 4:5 ratio image at top, name in 13px futura-pt below with 8px gap, price in `{typography.price}` a line beneath. Hover reveals a quick-add or alternate image swap with no card frame change. Grid defaults to 4 columns desktop, 2 columns mobile.

**`filter-chip`** — 34px height, hairline border at rest, full ink border when active, `{colors.surface-soft}` background fill on active. Typography is `{typography.caption}` — 11px uppercase futura-pt at 1.2px tracking. No pill rounding; the square corners match the button system.

### Editorial Modules

**`hero-banner`** — Center-aligned display text in freight-big-pro at 56px/300-weight over a soft-surface background. Subhead in futura-pt body-md beneath, with a `button-primary` CTA below that. Large vertical padding ({spacing.xxl} top and bottom) keeps the typographic field from feeling crowded against a full-width image or video behind it.

**`editorial-module`** — Split 50/50 layout pairing an image with a text column. Headline in freight-big-pro display-lg, subhead in editorial-sub (22px/300 serif), body in futura-pt body-md. Used for brand story, material education, and campaign storytelling. Gap between columns is {spacing.xxl}.

**`collection-header`** — Center-aligned, white canvas, display-md freight-big-pro heading with an optional futura-pt body-md descriptor paragraph beneath. Bottom padding {spacing.xl} before the filter row begins. Serves every category landing page and curated collection.

### Badges and Labels

**`gift-badge`** — Inline label with hairline border, surface-soft fill, no rounding. Caption typography in `{colors.body}`. Used to tag gift-eligible products or curated gift guide collections. Low visual weight — it annotates rather than shouts.

**`category-label`** — Borderless, backgroundless, muted-ink caption text. Appears above product card names in collection contexts to indicate sub-category (e.g., "Necklaces", "Rings"). Acts as visual indexing without adding UI mass.

### Overlays and Drawers

**`search-drawer`** — Full-width overlay dropping from the nav, white canvas background, single futura-pt input at body-md scale with a hairline bottom border replacing the frame. Suggestions appear as plain text links beneath. Background receives a 40% ink scrim.

**`cart-drawer`** — Right-side slide-in panel, white fill, hairline left border, no shadow. Heading in title-md uppercase futura-pt, line items in body-sm. Subtotal and checkout CTA anchor the bottom of the drawer as a sticky footer strip.

### Footer

**`footer`** — Full #121212 background reversing all text to `{colors.on-primary}`. Column headings in title-sm (uppercase futura-pt, 1.5px tracking), links in body-sm at reduced opacity on hover. Mirrors the promo bar background, closing the tonal envelope of the page. Social icons and legal links sit in the bottom row at caption scale.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column editorial modules; 2-column product grid; hamburger nav with full-height drawer; hero headline drops to display-md (32px); filter chips scroll horizontally in a single row |
| Tablet | 744–1128px | 2–3 column product grid; split editorial modules remain but stack at 744px breakpoint; nav links visible but icon cluster compressed |
| Desktop | 1128–1440px | 4-column product grid; full nav link row; editorial modules at 50/50 split; hero at full display-xl (56px) |
| Wide | > 1440px | Max content width ~1440px centered; hero image extends edge-to-edge behind constrained text column; grid stays at 4 columns |

### Touch Targets

- All nav-bar icons minimum 44×44px tap target regardless of visible glyph size
- Filter chips minimum 44px height on mobile (override from 34px desktop)
- Product card tap targets cover the full image+text block, not just the title link
- Cart icon and hamburger both meet 44px minimum

### Collapsing Strategy

- Navigation collapses to hamburger below 744px; drawer is full-height with close icon at top-right
- Editorial 50/50 modules stack image-above-text below 744px; image takes 100vw, text column padded {spacing.base}
- Product grid: 4 col → 3 col at 1128px → 2 col at 744px; never single-column except editorial hero units
- Filter row becomes horizontal scroll at mobile without visible scrollbar; active filter count shown as badge on filter icon

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only two hex values were extracted (#dedede, #121212); the full palette almost certainly includes warm gold/champagne accent tones used on hover states, sale price text, and promotional callouts — these are likely loaded via JS or CSS-in-JS and were not captured
- No meta theme-color set; mobile browser chrome color cannot be confirmed
- Sale/strike-through price color unknown — may be a warm red or muted tone; assumed body color here but unverified
- Exact button hover transition duration and easing not extractable from static scrape
- Swatch rendering approach for multi-color products (dot, label, or image thumbnail) not confirmed
- Icon set style (stroke weight, corner style) not determined from extraction
- Exact grid gutter widths and max-content widths not confirmed numerically; values above are inferred from category conventions for this aesthetic tier
