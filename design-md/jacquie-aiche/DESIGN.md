---
version: alpha
name: "Jacquie Aiche"
source_url: "https://www.jacquieaiche.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every primary CTA glows in #ee9441 — an amber pulled directly from the hand-set citrines and warm yellow gold at the core of the Jacquie Aiche vocabulary. The color is not an arbitrary brand mark: it reads as molten metal before casting, an honest extraction from the jewelry photography that fills the canvas. Arizona, a bracketed serif with archival authority, carries editorial display heads; Diatype, a compact geometric sans-serif, runs body copy and UI chrome. The pairing produces a site that reads like a studio lookbook rather than a shopping interface — visual weight belongs to the imagery, not the chrome.

  The palette holds unexpected depth: a dark crimson #8b0000, the precise tone of a rough ruby cabochon, surfaces in editorial badges and select hover states. Near-black ink at #121212 anchors captions and metadata; hairlines resolve to #dedede against white canvas, nearly invisible. Navigation sits typographically slim on a white bar with no background fill and no shadow, so the full atmospheric weight of each editorial photograph lands without competition.

  Geometry is organic throughout. Filter pills and compact CTAs carry {rounded.full} shapes, mirroring bezel curves and rope-chain links. Product cards use {rounded.sm} — just enough warmth without rounding into casualness. Spacing is unhurried: section intervals at 64px allow each collection module to close fully before the next opens. On product detail pages, a small gemstone-type badge marks stone varieties in {typography.caption} text on a surface-soft ground, threading gemological precision into the editorial register without interrupting it.

  The amber primary appears almost exclusively at conversion moments — add to cart, wishlist, checkout — earning its warmth by restraint. The rest of the interface recedes into gray and white, letting the jewelry be the only color in the room.

colors:
  primary: "#ee9441"
  primary-active: "#d4782a"
  primary-disabled: "#f5c98a"
  crimson: "#8b0000"
  forest-deep: "#006400"
  forest-mid: "#128522"
  grass: "#3ed660"
  silver: "#c8c8c8"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#6b6b6b"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f8f5f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-crimson: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'arizona', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'arizona', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'arizona', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'arizona', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'diatype', 'Arimo', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'diatype', 'Arimo', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  body-md:
    fontFamily: "'diatype', 'Arimo', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'diatype', 'Arimo', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'diatype', 'Arimo', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  button-md:
    fontFamily: "'diatype', 'Arimo', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'diatype', 'Arimo', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'diatype', 'Arimo', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  price-display:
    fontFamily: "'arizona', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge-label:
    fontFamily: "'diatype', 'Arimo', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
    borderBottom: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1 / 1"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.sm}"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    layout: fullbleed-image-with-overlay
    overlayScrim: "rgba(0,0,0,0.12)"
    ctaLabel: "Shop Now"
  collection-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    rounded: "{rounded.none}"
    textAlign: center
  gemstone-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
    border: "1px solid {colors.hairline}"
  editorial-badge-crimson:
    backgroundColor: "{colors.crimson}"
    textColor: "{colors.on-crimson}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
    height: 36px
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
  jewelry-detail-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
    badgeComponent: gemstone-badge
    padding: "{spacing.xl}"
    borderLeft: "1px solid {colors.hairline}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.display-sm}"
    rounded: "{rounded.none}"
    border: none
    borderBottom: "1px solid {colors.hairline}"
    resultThumbnail: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.caption}"
    headlineTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Full-pill amber (#ee9441) CTA with white uppercase Diatype at 14px and tracking 0.08em, 48px tall. Reserved for the highest-conversion moments: "Add to Cart," "Shop Now," and checkout progression. Active state shifts the fill to #d4782a; disabled washes to a pale #f5c98a. No border — the color carries all authority.

**`button-secondary`** — Same pill geometry, white fill with a 1px ink border and dark text. Appears alongside the primary for lower-hierarchy choices like "Save to Wishlist" or "Continue Shopping." Hover inverts to ink fill and white type.

**`button-ghost`** — No radius, no fill. A baseline-underlined text link using the same uppercase button-md type treatment. Used inside editorial prose modules and footer columns for the lightest-weight navigational actions.

### Product Card

**`product-card`** — Square-cropped photography at {rounded.sm} with a white background. Product name in Diatype body-md, price rendered in Arizona price-display for a quiet editorial register that distinguishes it from the UI copy stack. No badge overlays clutter the grid — hover triggers a secondary image swap rather than an overlay CTA, keeping the browsing experience clean.

### Navigation

**`nav-bar`** — 60px fixed white bar with a hairline bottom rule at #dedede. Brand wordmark is centered on mobile; on desktop it shifts left with full category links in uppercase Diatype at 13px/0.06em tracking. Cart and account icons anchor the right side at minimum 44×44px tap targets. The bar does not change appearance on scroll — it remains white and hairline-bordered throughout, avoiding the distraction of sticky shadow effects.

### Hero Editorial

**`hero-editorial`** — Full-bleed photography with a 12% black scrim for headline legibility. Headline in Arizona display-xl (48px/weight 400), sub-copy in Diatype body-md below it. CTA sits beneath the copy stack, not overlaid on the image, so the photograph is never interrupted. On mobile the image crops to portrait ratio and the headline steps down to display-md.

### Collection Banner

**`collection-banner`** — A surface-soft (#f8f5f0) interstitial band separating thematic clusters within a collection page (Body Chains / Rings / Pendants / Ear Cuffs). Display-md Arizona headline centered, short Diatype body paragraph below. No image — the warmth of the off-white ground provides the texture. Vertical padding at 48px, horizontal at 32px.

### Gemstone Badge

**`gemstone-badge`** — Small pill on the product detail page identifying stone type: Citrine, Sapphire, Turquoise, Ruby, Diamond, Moonstone. Surface-soft fill, 1px hairline border, uppercase badge-label at 10px with 0.1em tracking. Multiple stones stack horizontally as a row of pills. The badge-label typography shared with editorial-badge-crimson ensures consistent micro-text scale across the system.

### Editorial Badge (Crimson)

**`editorial-badge-crimson`** — Deep ruby #8b0000 pill reserved for high-attention editorial labels: "New Arrival," "Handmade," "Limited." White type in badge-label. Never used for error states — crimson belongs to the jewelry register, not the form register.

### Filter Pills

**`filter-pill`** / **`filter-pill-active`** — Horizontal filter strip on collection pages. Inactive: white fill, hairline border, ink text in caption scale. Active inverts to full ink fill and white text — a binary toggle with no intermediate or indeterminate states. Touch target 36px minimum. On mobile, the filter strip collapses into a bottom-sheet modal triggered by a "Filter" ghost button.

### Jewelry Detail Panel

**`jewelry-detail-panel`** — On desktop, a right-column panel alongside a sticky image stack. Title in Arizona display-sm, price in Arizona price-display, material and stone details in Diatype body-sm. Gemstone-badge row sits below the price. A left hairline border separates it visually from the image column. On mobile the panel stacks below the image carousel.

### Search Overlay

**`search-overlay`** — Full-screen white overlay. Query text rendered in Arizona display-sm so the typed search term reads as a headline. Results populate as a compact list with 48×48px product thumbnails, title in body-sm, and price in caption. Escape or outside-click dismisses. No background blur — the overlay is opaque white, keeping focus entirely on the search interaction.

### Footer

**`footer`** — Full-width ink (#121212) band. White Diatype caption links (12px) in four columns on desktop, collapsing to a single-column accordion on mobile. Section headings in title-sm. Newsletter input and inline submit live in the footer band at the top of the column stack. No logos or trust badges — the footer is typographically restrained, mirroring the minimal nav aesthetic.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero crops to 4:5 portrait; filter strip becomes bottom-sheet modal; jewelry detail panel stacks below image |
| Tablet | 744–1128px | 2-column product grid; nav shows wordmark plus icons only, no text links; collection banner maintains full layout; detail panel remains stacked |
| Desktop | 1128–1440px | 3-column product grid; full nav with all category links visible; jewelry detail panel splits into 2-column with sticky left image |
| Wide | > 1440px | 4-column product grid; container max-width 1440px centered; section spacing increased to 80px |

### Touch Targets

- All filter pills minimum 36px height with 8px horizontal padding
- All buttons minimum 48px height across every viewport
- Nav icons minimum 44×44px tap zone regardless of visual size
- Product card entire surface is tappable — no separate CTA required in grid view
- Gemstone badges in detail panel are not interactive; no tap-target requirement

### Collapsing Strategy

- Desktop mega-menu (if present) collapses to slide-in drawer from the left on mobile
- Side filter panel converts to bottom-sheet modal triggered by a ghost-button on mobile
- Footer 4-column grid collapses to single-column accordion with disclosure toggles on mobile
- 2-column jewelry detail layout stacks to single column below 1128px breakpoint
- Hero sub-copy hides on mobile viewports narrower than 375px to preserve headline impact

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No `meta theme-color` extracted; canvas color assumed `#ffffff` from standard Shopify defaults
- Role of green tones (#006400, #128522, #3ed660) is ambiguous — may relate to gemstone photography color sampling, sale/availability badges, or Shopify framework UI states; not assigned named semantic roles pending visual confirmation
- Exact wordmark rendering unknown — the "JACQUIE AICHE" logotype likely uses Arizona or a related bracketed serif, but weight, size, and letter-spacing could not be confirmed from static extraction
- Button border-radius assumed {rounded.full} based on fine-jewelry brand conventions; exact pixel value not confirmed from extraction
- Hover/focus transition durations and easing curves not extractable from static analysis; 200ms ease recommended as a default
- Mega-menu structure (fly-out columns vs. full-screen overlay) not confirmed
- Exact product grid column counts and gutter widths not extracted; values in this file are inferred from standard Shopify grid behavior
- No confirmed mobile nav pattern (hamburger drawer vs. bottom nav bar)
