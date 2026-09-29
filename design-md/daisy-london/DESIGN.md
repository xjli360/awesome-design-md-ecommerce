---
version: alpha
name: "Daisy London"
source_url: "https://www.daisyjewellery.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Five tones of silver — an #f2f2f2 canvas running through #d6d6d6, #aaaaaa, #818181, to #1f1f1f ink — orbit a single chromatic note: #869791, a chalky blue-sage that reads like oxidized sterling in afternoon light, worn smooth. Where most demi-fine brands reach for cream or blush to signal warmth, Daisy London strips the field to near-monochrome and trusts product photography to carry the entire color story — the daisy of the name is vivid yellow in nature, silver-gray in execution, and that paradox is deliberate: the flower signals everyday ease, the London gray signals restraint. Type architecture runs on two poles: freight-display-pro at large sizes and light weights (300–400) handles the editorial register, its open apertures giving collection names room to breathe; canada-type-gibson or a comparable humanist grotesque handles navigation, labels, and cart UI in fine tracking and controlled leading — the contrast between the serif's organic curves and the grotesque's geometric precision mirrors the brand's blending of botanical charm motifs with clean London minimalism. Interaction chrome stays deliberately quiet throughout: buttons prefer {rounded.sm} corners, inputs sit flush with {colors.hairline} borders, and the rare {rounded.full} pill surfaces only on meaning badges and promotional tags rather than on primary CTAs. Hover states resolve as a measured shift to {colors.primary-active} rather than a color jump or shadow lift — the brand communicates confidence through stillness. Product cards float on {colors.surface-soft} in a tight 4:5 ratio with {spacing.sm} internal breathing room, each charm or ring photographed large enough to show metal texture. The "With Meaning" brand posture surfaces not as marketing copy but as interface logic: every piece carries a semantic label — zodiac, birthstone, sentiment — set in {typography.caption} beneath the product name, treating each SKU as a personally meaningful object rather than a catalogue entry.

colors:
  primary: "#869791"
  primary-active: "#6b7b76"
  primary-disabled: "#c4ccc9"
  ink: "#1f1f1f"
  body: "#404040"
  muted: "#818181"
  muted-soft: "#aaaaaa"
  hairline: "#d6d6d6"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  silver-mid: "#aaaaaa"
  silver-light: "#d6d6d6"

typography:
  display-xl:
    fontFamily: "'freight-display-pro', 'Big Caslon', 'Bodoni MT', Georgia, serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'freight-display-pro', 'Big Caslon', Georgia, serif"
    fontSize: 38px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'freight-display-pro', 'Big Caslon', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'canada-type-gibson', 'brandon-grotesque', elza, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-md:
    fontFamily: "'canada-type-gibson', 'brandon-grotesque', elza, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.02em
  body-md:
    fontFamily: "'canada-type-gibson', 'brandon-grotesque', elza, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'canada-type-gibson', 'brandon-grotesque', elza, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'canada-type-gibson', 'brandon-grotesque', elza, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  label-xs:
    fontFamily: "'canada-type-gibson', 'brandon-grotesque', elza, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-md:
    fontFamily: "'canada-type-gibson', 'brandon-grotesque', elza, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'canada-type-gibson', 'brandon-grotesque', elza, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'canada-type-gibson', 'brandon-grotesque', elza, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.04em
  price-display:
    fontFamily: "'canada-type-gibson', 'brandon-grotesque', elza, sans-serif"
    fontSize: 16px
    fontWeight: 400
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 46px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 46px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.body-md}"
    captionTypography: "{typography.caption}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.none}"
    imagePadding: "{spacing.sm}"
    textPadding: "{spacing.sm} 0"
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    headlineColor: "{colors.ink}"
    subheadColor: "{colors.body}"
    ctaComponent: "button-primary"
    minHeight: 560px
    imageFit: cover
  collection-banner:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-md}"
    labelTypography: "{typography.label-xs}"
    headlineColor: "{colors.ink}"
    labelColor: "{colors.primary}"
    padding: "{spacing.xl} {spacing.section}"
  meaning-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 10px
    border: "1px solid {colors.silver-light}"
  wishlist-icon:
    color: "{colors.muted-soft}"
    activeColor: "{colors.ink}"
    hoverColor: "{colors.primary}"
    size: 20px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "10px {spacing.md}"
    iconColor: "{colors.muted}"
  jewelry-detail-panel:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    titleColor: "{colors.ink}"
    bodyColor: "{colors.body}"
    priceColor: "{colors.ink}"
    dividerColor: "{colors.hairline}"
    padding: "{spacing.xl}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-xs}"
    height: 36px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.ink}"
    headlineTypography: "{typography.label-xs}"
    linkTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    iconColor: "{colors.muted-soft}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — A blue-sage fill (#869791) with spaced uppercase `{typography.button-md}` and `{rounded.sm}` corners, 46px tall. On hover the fill deepens to `{colors.primary-active}` (#6b7b76) with no scale or shadow change; the brand signals confidence through stillness rather than animation. Disabled state bleaches to `{colors.primary-disabled}` (#c4ccc9). Used for "Add to Bag," "Shop Now," and checkout progression.

**`button-secondary`** — White canvas, ink border, identical dimensions to the primary. Reads as a lower-commitment action: save to wishlist, view all, continue browsing. Active state introduces a `{colors.surface-soft}` fill wash behind the ink text. The border weight (1px) intentionally matches `{colors.hairline}` weight elsewhere so the secondary button never shouts.

**`button-ghost`** — Hairline-bordered, muted text, `{rounded.sm}`. Appears as filter chips, metal-type toggles (Gold / Silver / Rose Gold), and size or length variant selectors on the PDP. The border reads as a field marker rather than a CTA; selected state inverts to `{colors.ink}` background with `{colors.canvas}` text.

### Navigation

**`nav-bar`** — 64px tall on a white ground with a featherweight `{colors.hairline-soft}` bottom rule. Logo appears as logotype-only in `{colors.ink}`; on hover the wordmark may shift to `{colors.primary}`. Nav links at 13px in light grotesque (`{typography.nav-link}`) cover Collections, Symbols & Meanings, Gifting, and Sale. Wishlist and bag icons in `{colors.muted-soft}` anchor the right rail; they thicken to `{colors.ink}` on hover. Mobile falls back to a hamburger icon; bag count badge uses `{typography.label-xs}` in a `{rounded.full}` dot.

**`announcement-bar`** — A 36px band above the nav in `{colors.ink}` carrying `{colors.canvas}` `{typography.label-xs}` copy for shipping thresholds, promotion codes, or editorial callouts. The stark contrast provides maximum salience without requiring any brand-color accent.

### Product Card

**`product-card`** — Borderless, no corner rounding (`{rounded.none}`). The image occupies a near-square 4:5 container on `{colors.surface-soft}` with `{spacing.sm}` internal pad so the jewelry doesn't bleed to the tile edge. Below the image: product name in `{typography.body-md}` and `{colors.ink}`, a meaning descriptor (e.g. "Scorpio · Birthstone") in `{typography.caption}` and `{colors.muted}`, then price in `{typography.price-display}`. Wishlist heart overlays the top-right corner of the image plate on hover, shifting from `{colors.muted-soft}` to `{colors.primary}`. Grid is 2-up on mobile, 3-up on tablet, 4-up on desktop.

### Hero & Editorials

**`hero-editorial`** — Full-bleed image or flat `{colors.surface-soft}` panel, minimum 560px tall. Headline in `{typography.display-xl}` at weight 300 — the lightest setting, chosen deliberately to match the "effortless" brand voice; heavy display type would contradict it. Subhead at `{typography.body-md}` in `{colors.body}`. A single `button-primary` CTA; no secondary option in the hero unit. Left-aligned on desktop, centered on mobile.

**`collection-banner`** — Section headers for category landings pair a `{typography.label-xs}` overline in `{colors.primary}` (the sage-blue used as an accent label here, not a fill) with a `{typography.display-md}` headline in `{colors.ink}`. No supporting imagery required — the typographic weight difference between the 10px overline and 28px headline carries the hierarchy alone.

### Jewelry Detail Panel

**`jewelry-detail-panel`** — Right-hand panel on the PDP. Product title at `{typography.display-md}`, price directly below in `{typography.price-display}`, then a `{colors.hairline}` 1px divider rule. Stone or material description in `{typography.body-md}`, meaning narrative in `{typography.caption}` at light italic weight. Length or size selector rendered as ghost buttons in a horizontal row. Add to Bag as `button-primary`, full width on mobile. Below the fold: Care Instructions, Metal Options, and Why We Love It collapsed in a plain accordion using `{colors.hairline}` dividers and `{typography.body-sm}` body copy.

### Meaning Badge

**`meaning-badge`** — A `{rounded.full}` pill in `{colors.surface-soft}` with a `{colors.silver-light}` border, carrying a single word or short phrase ("Zodiac," "Birthstone," "Protection") in `{typography.caption}`. These tags appear on product cards and PDPs alike; they do not use `{colors.primary}` as a fill and never carry interactive state — they are informational, not filterable. Their presence reinforces the brand's core proposition: every piece ships with a reason to exist.

### Search

**`search-bar`** — A `{colors.surface-soft}` input with a `{colors.hairline}` outline and a loupe icon in `{colors.muted}` on the left leading edge. Text at `{typography.body-sm}`; corner at `{rounded.xs}`. On mobile the bar expands to a full-screen modal overlay with a close icon; on desktop it expands inline within the nav rail. Results appear in a drop-panel with product thumbnails on `{colors.canvas}`, name + price in matching card typography.

### Footer

**`footer`** — `{colors.surface-soft}` background, `{colors.hairline}` top rule. Four link columns on desktop, each headed by a `{typography.label-xs}` label in `{colors.ink}`; link text at `{typography.body-sm}` in `{colors.muted}`, shifting to `{colors.ink}` on hover. Newsletter sign-up runs inline in the leftmost column: `text-input` + `button-primary`. Social row (Instagram, Pinterest, TikTok) uses 20px `{colors.muted-soft}` icons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with slide-in drawer; hero headline drops to display-lg (38px) weight 300; jewelry detail panel stacks below full-width image; meaning badges wrap horizontally; Add to Bag becomes sticky 52px bottom bar |
| Tablet | 744–1128px | 2-column product grid; nav collapses to icon set + hamburger at the narrow end; hero allows 50/50 text-image split; collection banners retain full typographic display |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav bar with all links visible; PDP splits 60/40 image/detail; announcement bar shows rotating messages |
| Wide | > 1440px | Content max-width ~1440px centered with auto side margins; grid holds at 4 columns; hero image scales but text block caps at 600px wide to preserve reading measure |

### Touch Targets

- All buttons minimum 44px tall; `button-primary` and `button-secondary` sit at 46px
- Wishlist icon tap target padded to 44×44px regardless of the visible 20px icon size
- Ghost variant selector buttons expand to 44px tall on mobile breakpoints
- Sticky "Add to Bag" bar on mobile PDP: full-width, 52px tall, fixed to bottom of viewport

### Collapsing Strategy

- Primary nav collapses to hamburger below 744px; cart and wishlist icons remain pinned top-right at all sizes
- PDP accordions (Care, Metal Options, Why We Love It) default-closed on breakpoints below 1128px
- Announcement bar persists across all breakpoints, reduced to one message on mobile (no marquee or carousel)
- Footer 4-column layout collapses to single-column stacked accordion on mobile; newsletter sign-up promotes to top of footer stack

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No strongly chromatic brand-defined primary color was found in the extraction; #869791 (blue-sage) is the most distinctive extracted value and has been designated primary, but it may function as a supporting UI tone rather than an intentional signature accent — verify against the brand style guide
- Exact licensed weights for freight-display-pro and canada-type-gibson were not determinable from the live Shopify template; Light (300) and Regular (400) are assumed for display, Medium (500) for UI — confirm against the brand's font license
- Meta theme-color was absent, leaving no definitive mobile browser chrome color; `{colors.canvas}` (#ffffff) is assumed
- Button corner radius was not extractable; `{rounded.sm}` (8px) is a category-appropriate default — verify against PDP and cart button screenshots
- Animation timings and easing curves for hover transitions, drawer open/close, accordion expand, and cart slide-in were not captured
- Product image aspect ratio (4:5 assumed) should be confirmed against active Shopify theme image-crop settings
- Any seasonal palette variants (e.g. gold-tone holiday accent) were not detected in the extraction window
