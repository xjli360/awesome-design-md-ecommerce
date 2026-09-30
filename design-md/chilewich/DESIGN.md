---
version: alpha
name: "Chilewich"
source_url: "https://www.chilewich.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Woven vinyl photographed so close you can count the strand — that is the operating logic behind Chilewich's digital presence. The palette reads directly off the sample book: a compressed neutral spectrum running from silver (#c7c7c7) through warm steel (#686c6d) to near-black charcoal (#191919), all grounded on a warm linen canvas (#f2f1ec) that registers as material rather than screen. Dutch 801, a proportioned classical serif, governs every headline — an unexpected move for a home-goods e-commerce site and exactly the right one, lending the product catalog the authority of a textile archive. Body copy shifts to Plain, a geometric sans, creating a serif/sans split that feels curated without announcing itself. There is no brand-voltage accent in the conventional sense: #e51717 appears only as a promotional or alert marker, #1a57ff surfaces on editorial hyperlinks, and primary CTAs run in #191919 — a charcoal deep enough to read as black — earning hierarchy through value contrast alone rather than a vivid punch color. Geometry is flat and orthogonal throughout; buttons carry zero border-radius ({rounded.none}), product cards sit in a strict grid with no shadow, and filter rails favor checkbox rows over pill tags. The spacing system breathes at the collection level — hero and grid sections open at {spacing.section} margins — then compresses inside the card to preserve information density. The most brand-specific UI primitive is the swatch selector: small square chips ({rounded.sm}) with an active ring rather than a filled state, keeping the product's own colorway visible at all times. What the interface does quietly and well is refuse to compete with the product. The warm off-white surface and restrained gray scale exist so that a woven placemat photographed on a slate table feels like the loudest thing on the page.

colors:
  primary: "#191919"
  primary-active: "#121212"
  primary-disabled: "#a5a7a8"
  ink: "#191919"
  body: "#515052"
  muted: "#777777"
  muted-soft: "#a5a7a8"
  hairline: "#dbdbdb"
  hairline-soft: "#dedede"
  canvas: "#faf7f7"
  surface-linen: "#f2f1ec"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#faf7f7"
  on-dark: "#faf7f7"
  warm-gray-mid: "#686c6d"
  warm-gray-dark: "#555555"
  charcoal: "#232323"
  alert: "#e51717"
  link: "#1a57ff"

typography:
  display-xl:
    fontFamily: "'Dutch 801', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Dutch 801', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Dutch 801', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Dutch 801', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Plain', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Plain', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.03em
  body-md:
    fontFamily: "'Plain', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Plain', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Plain', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  label-upper:
    fontFamily: "'Plain', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  button-md:
    fontFamily: "'Plain', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Plain', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Plain', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.05em
  price:
    fontFamily: "'Plain', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  price-large:
    fontFamily: "'Plain', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
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
    textColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 14px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    height: 44px
    padding: "0 {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-sm}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageBg: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.body}"
    gap: "{spacing.sm}"
  swatch-selector:
    chipSize: 24px
    chipRounded: "{rounded.sm}"
    chipBorder: "1px solid {colors.hairline}"
    chipBorderActive: "1px solid {colors.ink}"
    chipRingActive: "2px solid {colors.ink}"
    chipRingOffset: 2px
    gap: "{spacing.xs}"
  hero-banner:
    backgroundColor: "{colors.surface-linen}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 520px
    padding: "{spacing.section} {spacing.xl}"
    textMaxWidth: 480px
  collection-header:
    backgroundColor: "{colors.surface-linen}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xl} 0"
  filter-rail:
    backgroundColor: "{colors.canvas}"
    borderRight: "1px solid {colors.hairline}"
    labelTypography: "{typography.label-upper}"
    labelColor: "{colors.muted}"
    optionTypography: "{typography.body-sm}"
    optionColor: "{colors.ink}"
    checkboxBorder: "1px solid {colors.hairline}"
    checkboxBorderActive: "1px solid {colors.ink}"
    checkboxBgActive: "{colors.ink}"
    checkboxCheckColor: "{colors.on-primary}"
    width: 220px
  badge-sale:
    backgroundColor: "{colors.alert}"
    textColor: "#ffffff"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  product-detail-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    thumbnailBorder: "1px solid {colors.hairline}"
    thumbnailBorderActive: "1px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 44px
    width: 120px
  footer:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    headingColor: "{colors.muted-soft}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Solid charcoal (#191919) fill, near-white (#faf7f7) text, zero border-radius, uppercase tracking-widened label via `{typography.button-md}`. The sharp corners are a deliberate signal: no softening, no friendly rounding. Hover deepens to #121212; disabled state bleaches to `{colors.primary-disabled}` with low-contrast text. Minimum height 48px, padding generous at 14px top/bottom so the uppercase label has air without inflating the button to a block.

**`button-secondary`** — Transparent background with a 1px solid ink border, pairing cleanly next to `button-primary` in add-to-cart rows. On hover the fill inverts to solid charcoal and text flips to `{colors.on-primary}` — the same state as primary — so the two buttons form a toggle pair without introducing a third color. Border drops on the hover state since the fill takes over.

**`button-text`** — Bare underlined `{typography.body-sm}` link used for low-priority actions: view all, clear filters, read more. No padding, no background, no height constraint.

### Inputs

**`text-input`** — Hairline 1px border (#dbdbdb) at rest sharpens to 1px ink on focus. No radius anywhere. Height 48px matches `button-primary` for vertical alignment on checkout form rows. Placeholder in `{colors.muted}`. Error state swaps border to `{colors.alert}`.

**`search-bar`** — Surface-soft (#f5f5f5) fill, borderless at rest, hairline border on focus. Leading search icon in muted gray. Zero radius. Used collapsed (icon-only) in the desktop nav and expanded full-width on mobile. Maintains the orthogonal grid language of the product imagery behind it.

### Navigation

**`nav-bar`** — 64px tall, warm canvas (#faf7f7) background, a single 1px hairline border-bottom. The logo is typeset in Dutch 801 via `{typography.display-sm}` rather than an image lockup — preserving sharp rendering at all resolutions. Category links run in `{typography.nav-link}` (Plain, 13px, 0.05em tracking). Search, account, and cart icons cluster at the right. On scroll, the nav acquires a 0 8px 16px shadow at low opacity rather than changing color, so the warm off-white persists.

### Product Grid

**`product-card`** — Zero-radius image tile on a #f5f5f5 background, no shadow, no card border. Below the image: product name in `{typography.title-sm}` and price in `{typography.price}`, separated from the image by `{spacing.sm}`. Grid gutters — not card chrome — define item boundaries. Swatch chips appear below the price row; on desktop they surface on hover, on mobile they are always visible.

**`swatch-selector`** — 24×24px square chips at `{rounded.sm}` (4px radius), arranged in a horizontal row with `{spacing.xs}` (4px) gaps. Each chip renders the product colorway as a background swatch tile. Inactive: 1px `{colors.hairline}` border. Active: 2px `{colors.ink}` ring with 2px offset — the ring-offset technique is the brand-specific detail that keeps the colorway visible inside the active state rather than covering it with a filled background.

### Badges

**`badge-sale`** — Flat #e51717 rectangle, zero radius, all-caps white label via `{typography.label-upper}`. Positioned absolute at the top-left corner of the product image tile. The hard corner against the hard card corner is intentional — no softening on a functional marker.

**`badge-new`** — Identical geometry to `badge-sale` with charcoal (#191919) fill. Deployed for new colorway or new collection introductions.

### Hero & Editorial

**`hero-banner`** — Full-bleed or 50/50 split layout (text left, product image right). Warm linen (#f2f1ec) background on solid-fill heroes; unobstructed full-bleed photograph otherwise. Headline in `{typography.display-xl}` (Dutch 801, 48px, weight 400), subhead in `{typography.body-md}`, then a `button-primary`. Minimum height 520px. Text block max-width 480px prevents runaway line lengths on wide viewports.

**`collection-header`** — A full-width linen-background band above the product grid. Collection name in `{typography.display-md}` (Dutch 801, 28px), optional descriptor sentence in `{typography.body-md}`. Vertical padding `{spacing.xl}` above and below.

### Filtering

**`filter-rail`** — Left sidebar, 220px wide, 1px right border in `{colors.hairline}`. Section labels in `{typography.label-upper}` (muted, spaced-uppercase). Options in `{typography.body-sm}`. Checkboxes are square (zero radius): hairline border at rest, solid ink fill with white checkmark when active. Sections are expanded by default on desktop — no accordion collapse — because Chilewich's filter taxonomy (size, shape, colorway, material) is shallow enough to show at once.

### Product Detail

**`product-detail-image`** — Square panel on #f5f5f5, no radius. Thumbnail strip below uses `{colors.hairline}` border at rest, `{colors.ink}` border when active. Clicking the main image opens a full-viewport overlay with a minimal close mark — no carousel chrome, no zoom controls beyond the overlay itself.

**`quantity-selector`** — Minus icon / number / plus icon treated as a single bordered unit: 1px `{colors.hairline}`, no radius, 44px tall, 120px wide. The number field is center-aligned. On mobile it is tap-only; on desktop it is directly editable. Icon tap targets expand to meet 44×44px minimums via padding.

### Footer

**`footer`** — Deep charcoal (#232323) background, `{colors.on-dark}` text throughout. Column headings in `{typography.label-upper}` colored `{colors.muted-soft}`. Links in `{typography.body-sm}`. A single horizontal rule at 1px `{colors.warm-gray-dark}` separates the link columns from the legal row. No background distinction between the two zones — one continuous dark band.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter rail becomes a full-screen bottom-sheet drawer triggered by a "Filter" button; nav collapses to hamburger + centered logo + cart icon; hero stacks headline above image; swatch chips always visible below card price |
| Tablet | 744–1128px | Two-column product grid; filter rail replaced by a horizontal chip-scroll bar above the grid; nav retains full links but compresses letter-spacing slightly; hero remains split 50/50 if space allows |
| Desktop | 1128–1440px | Three-column product grid with 220px left sidebar filter rail; full nav with all category labels; hero at full 50/50 split; swatch chips appear on card hover only |
| Wide | > 1440px | Content max-width 1440px centered; four-column product grid option available; hero image scales to fill but text block stays capped at 480px max-width |

### Touch Targets

- All primary and secondary buttons minimum 48px height
- Swatch chips expand from 24px to 36px on mobile for reliable tap accuracy
- Quantity selector minus/plus icons minimum 44×44px tap area via padding
- Filter rail checkbox rows minimum 44px height on mobile
- Nav hamburger minimum 44×44px tap area

### Collapsing Strategy

- Filter rail: 220px sidebar on desktop ≥ 1128px; full-screen drawer (slide up) on mobile/tablet behind a "Filter" pill button
- Navigation: full horizontal category bar at desktop; hamburger drawer on mobile with category accordion inside the drawer
- Product card swatch row: hover-reveal on desktop (up to 8 chips), always-visible on mobile (up to 5 chips, "+N" truncation for larger colorway sets)
- Hero text/image: side-by-side on desktop and tablet, stacked with image below text on mobile
- Footer columns: 4-up on desktop, 2-up on tablet, single-column accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Border-radius values not confirmed from live site extraction; zero-radius / flat aesthetic is inferred from brand photography styling and modernist product positioning
- Button padding, height, and exact letter-spacing values are estimates — Chilewich's Shopify theme did not expose CSS custom properties in the extraction
- Dutch 801 weight variants in use are unconfirmed; Regular (400) assumed for display use based on the brand's avoidance of heavy typographic treatment
- "Plain" typeface identity is ambiguous — may be a custom or licensed geometric sans; Helvetica is the confirmed stack fallback
- No dark-mode or alternate-theme tokens were detectable
- Motion and animation timing functions not captured
- Exact product grid column counts and gutter widths unconfirmed; 3-column desktop is an informed estimate based on category depth and standard home-goods e-commerce conventions
- Icon style (line vs filled, stroke weight) not determinable from color extraction alone
- No confirmation of whether the logo is a wordmark image asset or live typeset text
