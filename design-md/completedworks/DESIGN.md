---
version: alpha
name: "Completedworks"
source_url: "https://www.completedworks.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The citrus warmth of #ff974f appears as a single charged mark against a parchment ground (#f1efe9) — not a dominant surface but a punctuation that wakes up an otherwise spare palette of near-blacks and warm neutrals. Where most jewelry labels reach for gallery-white and cold silver to signal luxury, Completedworks holds the canvas at #f1efe9, a cream close enough to paper to read as analog before any product image loads, and lets that analog temperature carry the brand's character across every page state. Self Modern carries the display-level editorial weight at the top of the type hierarchy — a contemporary serif set light (weight 400, never 700) so it reads as a literary whisper rather than a market shout — while SemplicitaPro handles navigation, product labels, and all utilitarian copy in tightly tracked uppercase at 13px, producing the flat, spare atmosphere of a gallery wall card. The pairing of an idiosyncratic serif with a humanist sans creates a tonal split between the poetic (headlines, brand voice, editorial features) and the functional (nav, filters, price labels) that mirrors the brand's own position between fine-art object and wearable piece.

  Buttons carry no radius at all: flat-cornered rectangles in near-black (#1c1c1c) with uppercase labels function as rubber stamps, refusing any ergonomic softening that might read as casual. The orange (#ff974f) surfaces as a signal color for new-arrival badges, hover interrupts, and promotional callouts rather than owning the primary action — it is an interrupt, not a foundation. A deep navy (#112244) appears in announcement bars and footer contrast layers, giving the site a second dark register that reads colder and more institutional than the ink. Product cards hold a strict 3:4 portrait ratio without internal padding, treating sculptural pieces the way an object photograph is mounted in a museum catalog — edge to edge, no room to breathe. Quick-add overlays appear flat in ink with warm cream text, consistent with the zero-radius interaction vocabulary at every layer. Generous whitespace between collection rows and the near-absence of decorative dividers mean page structure is communicated entirely through proximity and type weight — not rules, borders, or color fills.

colors:
  primary: "#ff974f"
  primary-active: "#e8793a"
  primary-disabled: "#ffd4b5"
  accent-navy: "#112244"
  ink: "#1c1c1c"
  ink-soft: "#121212"
  body: "#1c1c1c"
  muted: "#767676"
  hairline: "#dedede"
  canvas: "#f1efe9"
  surface-soft: "#f1efe9"
  surface-card: "#ffffff"
  on-primary: "#1c1c1c"
  on-dark: "#f1efe9"

typography:
  display-xl:
    fontFamily: "'Self Modern', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Self Modern', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Self Modern', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'SemplicitaPro', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'SemplicitaPro', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  body-md:
    fontFamily: "'SemplicitaPro', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'SemplicitaPro', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'SemplicitaPro', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.4px
  price:
    fontFamily: "'SemplicitaPro', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-sale:
    fontFamily: "'SemplicitaPro', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'SemplicitaPro', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'SemplicitaPro', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.4px
  logo-display:
    fontFamily: "'Self Modern', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.3px
  editorial-label:
    fontFamily: "'SemplicitaPro', sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1.8px
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 8px 0
    borderBottom: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    padding: 12px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.logo-display}"
  announcement-bar:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 34px
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
    imageFit: cover
  product-card-sale-price:
    textColor: "{colors.primary}"
    typography: "{typography.price-sale}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.editorial-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.editorial-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    labelTypography: "{typography.editorial-label}"
    minHeight: 85vh
    padding: "{spacing.xxl} {spacing.xxl}"
  collection-editorial:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  filter-pill:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.editorial-label}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.editorial-label}"
    rounded: "{rounded.none}"
    padding: 6px 14px
  quick-add-button:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 40px
    width: "100%"
  size-selector-pill:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.ink}"
    activeBackground: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    padding: 8px 14px
  swatch-selector:
    size: 22px
    borderRadius: "{rounded.full}"
    activeBorder: "1.5px solid {colors.ink}"
    gap: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.editorial-label}"
    linkColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
  newsletter-input:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.on-dark}"
    rounded: "{rounded.none}"
    padding: 10px 14px
    height: 40px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"

## Components

### Buttons

**`button-primary`** — A zero-radius rectangle in near-black (#1c1c1c) with warm cream (#f1efe9) uppercase tracking at 1.4px letter-spacing. The stamp-like geometry is intentional: no pill, no rounded corner, no softening. On hover the fill shifts to the brand orange (#ff974f) with dark text, so the interaction signal arrives through color rather than shape. Height is fixed at 44px with generous horizontal padding (28px each side) to give the flat form adequate presence.

**`button-secondary`** — Same geometry and uppercase typography as primary but expressed as a 1px outlined ghost, transparent fill, ink text. The border collapses to ink on hover rather than changing to orange, maintaining a visual hierarchy where the outlined form always reads as subordinate. Pair it with `button-primary` on checkout and product pages; never let two outlines sit side by side.

**`button-ghost`** — Text-only link underlined with a 1px border-bottom, no bounding box. Used for secondary editorial actions (view all, read more) where the button would over-weight the composition. The underline maintains a tangible hit area signal without introducing a background.

### Product Card

**`product-card`** — A frameless 3:4 portrait tile with no internal padding; photography bleeds to all four edges. Below the image, title and price stack in 13px SemplicitaPro Regular with a single `{spacing.sm}` gap — no metadata beyond material or color below the fold. Sale prices surface in the brand orange (#ff974f) via `product-card-sale-price` rather than a struck-through original, keeping the price row visually clean. Badges (new, sale) overlay the top-left corner of the image at 8px margin, never below it.

### Navigation

**`nav-bar`** — Cream-ground bar at 60px height with the Self Modern wordmark centered or left-aligned, flanked by utility icons (search, bag, account) right. Navigation links sit in 13px SemplicitaPro at 0.4px tracking with no weight change — they do not bold on hover. A 1px hairline border-bottom (#dedede) is the sole separator from page content. The `announcement-bar` in accent-navy sits above it, disappearing on scroll.

### Filters

**`filter-pill`** and **`filter-pill-active`** — Flat-rectangle chips in the same typographic register as navigation (editorial-label, 10px uppercase, 1.8px tracking). Inactive chips carry a hairline border; active chips invert to solid ink fill with cream text. No radius anywhere. The chip row scrolls horizontally on mobile with no scroll indicator.

### Hero

**`hero-banner`** — Full-bleed on the parchment canvas with Self Modern at 48px, weight 400, negative letter-spacing (–0.5px). A small editorial-label category tag (10px uppercase, 1.8px tracking) sits above the headline as a category identifier. The CTA button (`button-primary` or `button-ghost`) floats below the subtitle with `{spacing.lg}` separation. Minimum height is 85vh — photography or solid cream fill dominates; UI chrome is minimal.

### Collection Editorial

**`collection-editorial`** — A full-width dark-ground break using the accent-navy (#112244), used between product grid rows to introduce seasonal context or campaign copy. Headline in Self Modern display-md (32px) in warm cream, body in SemplicitaPro body-md, and an optional `button-ghost` in cream for editorial navigation. The navy provides contrast without competing with the ink ground of the footer.

### Footer

**`footer`** — Ink-ground (#1c1c1c) with four-column link columns labeled in 10px uppercase SemplicitaPro (editorial-label), links in 13px body-sm. Newsletter input sits inline with a ghost button to the right, both in cream outline against the dark field. Social icons render as plain text links rather than SVG glyphs. Bottom bar carries legal copy in caption weight with a hairline divider above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer (cream background, full-height); announcement bar retains full width; hero switches to square or 4:5 crop; filter chips scroll horizontally in a single row |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links inline, secondary items in overflow; hero maintains 85vh with reduced typography scale (display-md instead of display-xl) |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with account and bag icons; collection-editorial sections show side-by-side text and image layout |
| Wide | > 1440px | Four-column product grid; max-width container (~1440px) centered with canvas-colored side gutters; hero typography scales to display-xl with additional leading |

### Touch Targets

- All buttons minimum 44px height, full-width on mobile where width allows
- Filter pills stack two rows or switch to a collapsible drawer on mobile
- Size selector tiles maintain minimum 40×40px tap target regardless of visual size
- Swatch selectors expand to 28px diameter on touch viewports

### Collapsing Strategy

- Footer columns collapse to accordions on mobile with a 1px hairline divider and no background change
- Nav drawer slides from the right on mobile at full viewport height; overlay scrim is translucent ink
- Collection editorial sections stack vertically (text below image) on mobile and tablet
- Announcement bar remains visible on mobile but truncates with an ellipsis if copy exceeds one line

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No animation or transition timing values extracted; easing curves for hover, drawer open, and image zoom are assumed as standard ease-out defaults
- Exact grid gutter widths and column counts for the collection page not confirmed from extraction
- Mobile navigation pattern (hamburger vs. slide-over vs. full-page overlay) inferred from brand conventions, not directly extracted
- Hover state behavior for nav links (underline, color shift, or none) not confirmed
- Precise font weights available in the Self Modern variable font not confirmed; weight 400 assumed as the primary cut; bold variant availability unknown
- No icon system or icon set identified from extraction; cart, search, and account icons assumed as simple line icons
- Page transition behavior (none, fade, slide) not extractable from static analysis
- Exact product card hover state (quick-add reveal, image swap, zoom) not confirmed
- Color usage split between #1c1c1c and #121212 (two near-identical dark values extracted) may indicate a dark-mode or component-specific sub-palette; treated as equivalent here
