---
version: alpha
name: "UGallery"
source_url: "https://www.ugallery.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Gallery linen lives in the hex values before a single painting loads — UGallery's canvas, #f8f6f0, is the deliberate off-white of cotton rag paper rather than a design-system default, and the warm layering beneath it (#e6e3d8 surface cards, #dad5c5 tonal accents, #a19a83 muted secondary text) creates the ambient warmth of a sun-lit gallery room rather than the clinical brightness of a retail site. The brand's primary action color, #625d4c, is an olive-taupe that reads closer to undyed linen than a conventional CTA; it signals commitment without urgency, appropriate for an audience deliberating over original paintings rather than adding impulse items to a cart. Two typefaces divide labor sharply. Orpheus Pro, a revival of the mid-century titling serif, carries artwork titles, artist names in featured contexts, and the editorial copy that bridges the collector and the canvas. General Sans — a contemporary geometric sans — handles navigation, filters, body prose, and price labels, keeping the commercial scaffolding legible without competing with the art. Together they establish a clear rhythm: serif declares the work, sans-serif frames the transaction. All-uppercase General Sans labels with tracked letter-spacing index filters, medium tags, and section dividers, drawing on museum label tradition without its austerity. The deepest tone in the palette, #092933 — a near-teal dark navy — surfaces in the footer and select editorial modules, lending weight without invoking luxury-black clichés. Artwork image containers use zero rounding ({rounded.none}) to preserve the rectangular truth of a physical canvas; subtle {rounded.sm} appears only on interactive filter chips and price badges. Hover states lift cards with a soft shadow over the warm ivory surface rather than color shifts, keeping attention on the artwork rather than the interface. The price-range and medium filters collapse on mobile into a slide-over drawer, while the desktop view presents them as persistent pill chips along the gallery's top rail. UGallery's 'View artwork' CTA sits below each card in consistently quiet typography — General Sans medium, uppercase, tracked — reinforcing that the gallery, not the button, is the protagonist.

colors:
  primary: "#625d4c"
  primary-active: "#423e31"
  primary-disabled: "#a19a83"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#677279"
  muted-warm: "#a19a83"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#f8f6f0"
  surface-soft: "#e6e3d8"
  surface-card: "#f9f9f9"
  surface-warm: "#dad5c5"
  on-primary: "#f8f6f0"
  accent-teal: "#092933"
  on-accent: "#f8f6f0"
  error: "#e22120"

typography:
  display-xl:
    fontFamily: "'Orpheus Pro', Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Orpheus Pro', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Orpheus Pro', Georgia, serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  artwork-title:
    fontFamily: "'Orpheus Pro', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'General Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'General Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'General Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'General Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'General Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-upper:
    fontFamily: "'General Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  artist-byline:
    fontFamily: "'General Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.06em
    textTransform: uppercase
  price:
    fontFamily: "'General Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'General Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.07em
    textTransform: uppercase
  button-sm:
    fontFamily: "'General Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'General Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1.5px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted-warm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
    logoColor: "{colors.ink}"
  artwork-card:
    backgroundColor: "{colors.canvas}"
    imageContainer:
      rounded: "{rounded.none}"
      aspectRatio: "3/4"
      overflow: hidden
    hoverEffect: "box-shadow: 0 4px 20px rgba(66,62,49,0.12)"
    artistName:
      typography: "{typography.artist-byline}"
      textColor: "{colors.muted}"
      marginTop: "{spacing.md}"
    artworkTitle:
      typography: "{typography.artwork-title}"
      textColor: "{colors.ink}"
      marginTop: "{spacing.xs}"
    mediumLine:
      typography: "{typography.caption}"
      textColor: "{colors.muted-warm}"
      marginTop: "{spacing.xs}"
    priceDisplay:
      typography: "{typography.price}"
      textColor: "{colors.primary}"
      marginTop: "{spacing.sm}"
    ctaLabel:
      typography: "{typography.button-sm}"
      textColor: "{colors.primary}"
      backgroundColor: transparent
      marginTop: "{spacing.sm}"
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    layout: "split — 50% editorial text, 50% featured artwork image"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    padding: "{spacing.section} {spacing.xl}"
  filter-chip:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
  medium-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  price-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.primary-active}"
    typography: "{typography.price}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  artist-profile-strip:
    backgroundColor: "{colors.canvas}"
    layout: "horizontal — 56px circular portrait, name and bio stacked to the right"
    portraitRounded: "{rounded.full}"
    nameTypography: "{typography.title-sm}"
    nameColor: "{colors.ink}"
    bioTypography: "{typography.body-sm}"
    bioColor: "{colors.body}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.lg} 0"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted-warm}"
    iconColor: "{colors.muted}"
    height: 44px
  breadcrumb:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separator: "/"
    separatorColor: "{colors.hairline}"
  section-divider:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.md}"
    marginBottom: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-accent}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.surface-soft}"
    headingTypography: "{typography.label-upper}"
    headingColor: "{colors.on-accent}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The primary CTA, used for "Add to Cart" and "View Artwork" actions, renders in #625d4c with warm off-white text and deliberately sharp corners (`{rounded.none}`). The square geometry echoes the rectangular truth of a physical canvas and distinguishes committed actions from the rounded filter chips elsewhere in the UI. Active state deepens to #423e31; disabled state uses the muted sand #a19a83 as a background.

**`button-secondary`** — An outlined variant matching the primary's square geometry. Used for secondary actions like "Contact Artist" or "Save to Collection." The #625d4c border and text color maintain palette coherence without competing with the artwork above.

**`button-ghost`** — A light hairline-bordered button for low-emphasis tertiary actions (Share, Print). Renders in body text color so it reads as interface scaffolding rather than a call to action.

### Artwork Card

**`artwork-card`** — The primary browse unit across all gallery views. The image container uses zero rounding and a 3:4 portrait aspect ratio, mirroring a traditional canvas proportion. On hover, a warm shadow lifts the card without introducing color change, keeping attention on the art. Below the image, the artist name runs in `{typography.artist-byline}` — uppercase, tracked, muted — functioning like a museum credit line. The artwork title follows in Orpheus Pro `{typography.artwork-title}`, then a one-line medium and dimension descriptor in `{typography.caption}`, and finally the price in `{typography.price}` in the primary olive-taupe. A quiet uppercase text CTA rounds out the card without demanding visual hierarchy.

### Navigation

**`nav-bar`** — A warm linen bar at 68px, anchored by the UGallery wordmark in Orpheus Pro and navigation links in General Sans medium. A fine hairline border in #dedede separates it from the gallery content below. The nav holds its warm canvas tone throughout scrolling, providing a stable linen frame for the artwork beneath.

### Filters

**`filter-chip`** — Used for browsing by medium, size, price range, and style. Default state is transparent with a hairline border; active selection fills to #625d4c with warm off-white text — the same primary olive-taupe used in CTAs, establishing a unified active-state language. On mobile, the chip rail collapses to a single "Filter" toggle button that opens a full-screen drawer with an "Apply" primary button and "Clear All" ghost button at the bottom.

**`medium-tag`** — A smaller, non-interactive informational tag on artwork cards labeling the medium (Oil, Watercolor, Acrylic). Rendered in the warm ivory surface (#e6e3d8) with muted text, it reads as a catalog annotation rather than a clickable interface element.

### Hero

**`hero-editorial`** — A 50/50 split layout with editorial headline and CTA copy on one side and a full-height featured artwork on the other. The headline runs in Orpheus Pro `{typography.display-xl}` at 52px weight 400; the background field is the warm ivory `{colors.surface-soft}`. The CTA button uses the standard `button-primary` spec. On mobile the layout stacks vertically with the artwork image appearing first.

### Artist Profile

**`artist-profile-strip`** — A horizontal row component for artist attribution pages and editorial sections. A 56px circular portrait anchors the left, with the artist's name in `{typography.title-sm}` and a 2-line bio in `{typography.body-sm}` stacked to its right. A hairline underline separates successive strips. On artwork detail pages, this strip links to the artist's full profile.

### Footer

**`footer`** — Inverts the palette entirely onto #092933 (deep teal-navy), with off-white linen links and uppercase tracked column headings. This deep anchor grounds the page after the warm gallery scroll and provides editorial weight without resorting to generic black. Newsletter input uses a dark-mode variant of `text-input` with a surface-soft border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column artwork grid; filter chips collapse to a drawer toggle; nav collapses to hamburger; hero stacks vertically, image above headline; artist-profile-strip bio truncated to 2 lines |
| Tablet | 744–1128px | Two-column artwork grid; filter chips scroll horizontally in a single rail above the grid; nav shows condensed links; hero maintains split at 55/45 |
| Desktop | 1128–1440px | Three-column artwork grid; persistent horizontal filter rail below nav; full nav exposed; hero at 50/50 with generous lateral padding |
| Wide | > 1440px | Four-column grid inside a fixed 1360px container; section padding increases; hero artwork expands while text column stays width-constrained |

### Touch Targets

- All filter chips minimum 44px tall on mobile, full-width in drawer
- Entire artwork card is tappable — no separate isolated CTA tap zone needed
- Nav hamburger icon minimum 44×44px
- Medium-tag and price-badge are non-interactive; no touch target requirement
- Footer links minimum 44px line-height on mobile

### Collapsing Strategy

- Filter chips → full-width bottom slide-over drawer with "Apply Filters" primary button and "Clear All" ghost button pinned to drawer footer
- Multi-level nav (Browse, Artists, Collections, Gifts) → single-level accordion inside mobile drawer
- Artist bio in `artist-profile-strip` → 2-line clamp with "Read more" inline expand link
- Footer three-column layout → single stacked column on mobile; uppercase tracked headings preserved as section anchors
- Hero split → vertical stack (artwork image above editorial text) with reduced headline scale (display-md instead of display-xl)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Button border-radius on the live site not confirmed from extraction — `{rounded.none}` is inferred from gallery aesthetic conventions; actual site may use a 2–4px radius
- Exact nav height not extracted; 68px is an estimate based on typical art marketplace patterns
- Orpheus Pro weight variants (300/400/700) and licensed glyph subset not confirmed — only the family name was extracted
- General Sans weight map (which numeric weights are licensed) not confirmed beyond family name presence
- Hover interaction model (shadow vs. overlay vs. border change) not extracted from live CSS; shadow lift on artwork cards is inferred
- Mobile filter drawer structure not confirmed from live site; collapse-to-drawer is a common pattern but not validated against UGallery's actual implementation
- Logo treatment (wordmark-only vs. mark + wordmark) not determinable from extraction
- #008060 (Shopify checkout green) and #e22120 (Shopify error red) appear in extracted colors but are Shopify system defaults — excluded from the brand palette; #d21625 and #1e2d7d may also be Shopify system colors rather than brand choices
- Dark mode support, if any, not detectable from extracted data
