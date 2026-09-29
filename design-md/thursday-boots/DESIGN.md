---
version: alpha
name: "Thursday Boots"
source_url: "https://thursdayboots.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  #243a3e — a dark forest teal close enough to midnight on aged leather to explain the brand positioning — anchors every layer of the Thursday Boot Company experience: meta theme-color, sticky navigation fill on scroll, primary CTAs, and editorial accent lines all resolve to this single hue without a second brand voltage anywhere in sight. Frank Ruhl Libre, a display serif with roots in editorial print and strong optical compensation at large sizes, carries every hero headline and section title; the face reads historical without being archaic, which mirrors the brand's argument that craft and price point are not mutually exclusive. Nunito Sans handles all functional UI — nav links, body copy, button labels, size-grid text, form inputs — at weights light enough to disappear behind product photography rather than compete with it. The supporting palette is cool and deliberately recessive: near-whites (#fafafa, #f9f9f9) lay beneath mid-grays (#9b9b9b, #737373), a near-black ink (#121212) handles text contrast, and hairline borders (#dedede, #e9e9e9) provide structure without weight. Medium blues (#2374ab, #236898, #16496b) surface only on interactive links and callout borders, staying in the same cool register as the primary teal. The pale-blue tint (#deeaf2, #c8dcea) marks promotional banners and informational callouts — cool enough to read neutral, distinct enough to separate a message type from ambient page content. Corner geometry is intentionally flat: buttons sit at {rounded.xs}, cards at {rounded.sm}, with no pill shapes in the main shopping flow. Spatial rhythm is generous — {spacing.section} between editorial breaks, {spacing.xl} internal padding on hero surfaces — trusting photography and the craft claim to do the persuasion.

colors:
  primary: "#243a3e"
  primary-active: "#1a2e31"
  primary-disabled: "#7a9c9f"
  ink: "#121212"
  body: "#4a4a4a"
  muted: "#737373"
  muted-soft: "#9b9b9b"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#fafafa"
  surface-soft: "#f9f9f9"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  accent-link: "#2374ab"
  accent-link-mid: "#236898"
  accent-link-dark: "#16496b"
  surface-tint: "#deeaf2"
  surface-tint-mid: "#c8dcea"

typography:
  display-xl:
    fontFamily: "'Frank Ruhl Libre', Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Frank Ruhl Libre', Georgia, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Frank Ruhl Libre', Georgia, serif"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.3px
  price-display:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  overline:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1.5px
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
    padding: 14px 32px
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageRounded: "{rounded.sm}"
    padding: "{spacing.base}"
    shadow: "none"
  product-card-name:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-badge-sale:
    backgroundColor: "{colors.accent-link}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 600px
    padding: "{spacing.section} {spacing.xl}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 44px
    width: 44px
  size-selector-selected:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.xs}"
  size-selector-unavailable:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
  trust-badge:
    backgroundColor: "{colors.surface-tint}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.surface-tint-mid}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  info-callout:
    backgroundColor: "{colors.surface-tint}"
    textColor: "{colors.accent-link-dark}"
    border: "1px solid {colors.surface-tint-mid}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  review-stars:
    starColor: "{colors.primary}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.surface-tint}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Forest teal (#243a3e) fill with white uppercase Nunito Sans at `{typography.button-md}` (15px / weight 700 / 0.8px tracking), 48px tall, 4px radius corners. Hover shifts to `{colors.primary-active}` (#1a2e31) with no elevation change; the brand avoids shadows on interactive elements. Disabled state desaturates to `{colors.primary-disabled}` without changing text color or geometry.

**`button-secondary`** — Transparent fill with a 1.5px teal border and teal text, same height and radius as primary. Used for secondary actions on product pages and size-guide drawers. The border weight is intentionally heavier than a 1px hairline to hold legibility against light backgrounds.

**`button-ghost`** — 40px height, neutral hairline border, ink text, uppercase `{typography.button-sm}`. Appears in filter panels and nav drawers where a full-weight CTA would create visual competition.

### Text Inputs

**`text-input`** — 48px height, `{rounded.xs}` corners, `{colors.hairline}` default border sharpening to a 1.5px teal ring on focus. Placeholder text renders in `{colors.muted}`. The input height matches button-primary to allow inline form rows without alignment correction.

### Navigation

**`nav-bar`** — 64px fixed header on a `{colors.canvas}` ground with a bottom hairline at `{colors.hairline-soft}`. Nav links use `{typography.nav-link}` (14px / weight 600 / 0.3px tracking). On scroll past a threshold, the bar transitions to `nav-bar-scrolled`: the full background becomes `{colors.primary}` and text inverts to white — a deliberate brand moment that reinforces the teal identity on every scroll interaction across the site.

### Product Cards

**`product-card`** — Flat card on `{colors.canvas}`, `{rounded.sm}` image corners, no box shadow. Name renders in `{typography.title-sm}`, price in `{typography.price-display}` (18px / weight 700). Badges overlay the image at the top-left corner. The absence of shadows is deliberate — the brand's editorial photography provides depth through content rather than chrome.

### Badges

**`product-badge`** — Teal fill, white uppercase overline text (11px / 1.5px tracking), `{rounded.xs}`. Used for "Bestseller," "New," and collection labels. Sale and promotional variants swap to `{colors.accent-link}` (medium blue) to visually differentiate pricing events from editorial categorization.

### Hero Section

**`hero-section`** — Full-bleed `{colors.primary}` background with white Frank Ruhl Libre display text at `{typography.display-xl}` (52px / weight 700 / -0.5px tracking) and `{typography.body-md}` subtext. Minimum 600px tall, `{spacing.section}` vertical padding. On product collection pages, the hero may include a short editorial statement in `{typography.display-sm}` above a product grid.

### Size Selector

**`size-selector`** — 44×44px square tiles with `{rounded.xs}` corners and a default 1px hairline border. Selected state fills the tile with `{colors.primary}` and inverts text to white with a 1.5px border. Unavailable sizes render on `{colors.surface-card}` with `{colors.muted}` text and a lighter hairline; they are not crossed out, only visually de-emphasized.

### Trust Badges & Info Callouts

**`trust-badge`** — Pale-blue tint surface (#deeaf2) with teal text and a `{colors.surface-tint-mid}` border. Renders inline with messaging like "Free Returns," "Handcrafted Quality," or "1-Year Warranty." The `{typography.caption}` scale (12px) keeps these readable without drawing attention from the product.

**`info-callout`** — Wider informational block on `{colors.surface-tint}` with `{colors.accent-link-dark}` text, `{rounded.sm}` corners, and `{spacing.base}` internal padding. Used for shipping windows, sizing notes, and care instructions within product descriptions.

### Review Stars

**`review-stars`** — Stars render in `{colors.primary}` (teal, not the conventional amber), giving the rating display a brand-consistent color rather than a borrowed convention. Count and average text use `{typography.body-sm}` in `{colors.body}`.

### Collection Filter

**`collection-filter`** — Pill-less filter chips on a hairline border, `{rounded.xs}`, `{typography.body-sm}`. Active filter text shifts to `{colors.primary}` with no fill change — a restrained active state that avoids background color as a selection signal.

### Footer

**`footer`** — Full-bleed `{colors.primary}` teal background, white text and headings, link text in `{colors.surface-tint}` (pale blue) for legibility against the dark ground. Heading labels at `{typography.title-sm}` (16px / weight 600), link lists at `{typography.body-sm}`. `{spacing.section}` top and bottom padding. The footer and hero share the same background color, bookending every page view with the brand's primary hue.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero height reduces to 480px; size selector tiles shrink to 40×40px; filter drawer replaces inline filter panel |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links, secondary links in overflow menu; hero at 540px; trust badges stack in two columns |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with hover dropdowns; hero at full 600px with left-aligned text block and right-side image split |
| Wide | > 1440px | Max-width container (1440px) centered; side margins grow; hero image fills remainder; product grid locks to four columns |

### Touch Targets

- Size selector tiles minimum 44×44px on mobile, with 8px gap between tiles
- All primary and secondary buttons maintain 48px height on mobile
- Nav hamburger icon minimum 44×44px tap area
- Filter chip minimum height 40px on mobile
- Footer links use `{spacing.base}` vertical gap for comfortable tap spacing

### Collapsing Strategy

- Primary nav collapses fully to hamburger at mobile breakpoint; no partial display
- Collection filters move from an inline left sidebar to a bottom-sheet drawer on mobile
- Product description accordion sections replace expanded copy blocks below 744px
- Trust badge row wraps to two-column grid below 480px
- Hero text block stacks above image on mobile (text first, then image below)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Pure white (#ffffff) not confirmed in extraction; `{colors.canvas}` assigned to #fafafa as the lightest extracted near-white
- Font weight range for Frank Ruhl Libre not extracted; weights 500–700 inferred from typical editorial serif use patterns
- Exact button border-radius not pixel-confirmed; {rounded.xs} (4px) inferred from screenshot geometry and brand formality register
- Hover/focus animation durations and easing curves not extractable from static analysis
- Specific Frank Ruhl Libre optical size or variable-font axis settings not confirmed
- Mobile hero image crop behavior (focal point, object-position) not observed
- Exact nav breakpoint pixel value not confirmed; 744px assumed from Shopify Dawn theme defaults
- Discount/compare-at-price color treatment not extracted; assumed to use `{colors.accent-link}` based on sale badge pattern
