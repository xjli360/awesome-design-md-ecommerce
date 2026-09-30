---
version: alpha
name: "Eden Brothers"
source_url: "https://www.edenbrothers.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The pairing of Playlist Script's looping calligraphic strokes against Raleway's art-deco geometry announces the tension at the center of Eden Brothers — one letterform drawn from wild handwriting, the other built on precise geometric construction, meeting in a seed catalog that treats growing things as both science and poetry. Near-black #121212 handles all body copy and deep UI surfaces; #dedede — the only other confirmed extraction — marks the hairline grid separating product cards and filter rails. A deeper botanical green carries the primary CTA system, inferred from the brand's persistent garden identity and flagged as unconfirmed in Known Gaps below. Playlist Script appears at large display scales only: seasonal hero headlines, collection introductions, editorial callouts — lending the warmth a seed catalog earns through accumulated specificity (heirloom variety names, days-to-maturity figures, hardiness zones). Raleway handles everything operational: navigation labels at weight 600, body copy at 400, price points and category titles at 700, with its subtle Art Nouveau terminals giving even utilitarian rows a faint elegance. Fontello wires the icon layer — cart glyphs, search icons, social links — keeping UI chrome sharp at any density. The spacing system runs generous, with {spacing.section} breaks between catalog rows letting botanical photography breathe. Rounded values stay conservative: product cards and inputs at {rounded.sm}, the search bar at {rounded.full}, no pill shapes elsewhere. The product card is dense-informative rather than editorial-minimal — variety name, package size, and price stack tightly in a compact footprint designed for high-volume browsing. A persistent top bar carries search, cart, and account through scroll. The overall sensibility is a heritage mail-order seed catalog that moved to digital without losing faith in the pleasure of the dense, well-organized browse.

colors:
  primary: "#3b6b35"
  primary-active: "#2d5228"
  primary-disabled: "#a8c9a4"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#6e6e6e"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f7f5f0"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-rust: "#b85c38"
  accent-script: "#4a3728"

typography:
  hero-script:
    fontFamily: "'Playlist Script', cursive"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0
  display-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
  nav-link:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  price-display:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  tag-label:
    fontFamily: "'Raleway', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
    padding: 11px 23px
    height: 46px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 42px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    detailTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    imageBorderRadius: "{rounded.sm}"
    padding: "{spacing.md}"
    border: "1px solid {colors.hairline}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.hero-script}"
    subheadTypography: "{typography.display-sm}"
    headlineColor: "{colors.accent-script}"
    subheadColor: "{colors.ink}"
    padding: "{spacing.section} 0"
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.ink}"
    padding: "{spacing.xxl} 0"
  category-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px {spacing.sm}"
    border: "1px solid {colors.primary}"
  sale-badge:
    backgroundColor: "{colors.accent-rust}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px {spacing.sm}"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px {spacing.sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} 0"
  tag-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.full}"
    padding: "6px {spacing.md}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  seasonal-editorial:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.hero-script}"
    bodyTypography: "{typography.body-md}"
    headlineColor: "{colors.accent-script}"
    bodyColor: "{colors.body}"
    padding: "{spacing.xxl}"
    rounded: "{rounded.md}"

---

## Components

### Buttons

**`button-primary`** — Solid botanical green fill with white Raleway text at weight 700 and 0.5px letter-spacing, giving the label a slightly formal printed quality. Set at 46px total height, 12px/24px padding, with {rounded.sm} corners that read grounded rather than playful. Active state darkens to {colors.primary-active}; disabled desaturates to the pale sage {colors.primary-disabled}.

**`button-secondary`** — White canvas fill with a 1px green border and matching green Raleway label at the same height and radius as primary. Used for secondary actions on product pages — Add to Wishlist, Save for Later — where the primary Add to Cart button already anchors hierarchy.

**`button-ghost`** — Transparent background, {colors.ink} label in {typography.button-sm}, {rounded.xs} corners. Used for inline text-adjacent actions like "View All," "Show More," and filter-adjacent links where a bordered or filled button would add visual noise.

### Navigation

**`nav-bar`** — 72px tall persistent bar on white canvas with a 1px {colors.hairline} bottom border. Logo anchors left; search, account, and cart icons cluster right via Fontello glyphs. {typography.nav-link} labels (14px, weight 600, 0.3px tracking) span the main category row horizontally. Sticky on scroll with no background shift or transparency change.

**`nav-mega-menu`** — Full-width dropdown panel on white with a top hairline border. Category columns in {typography.body-sm} display subcategory links; a featured botanical image may occupy the rightmost column on desktop. Triggered on hover on desktop; becomes a full-screen slide-in drawer on touch breakpoints.

**`search-bar`** — Pill-shaped ({rounded.full}) input on warm {colors.surface-soft} background. A magnifier glyph from Fontello sits left-inset at 16px. Lives inside the nav bar on desktop; expands to a full-width overlay on mobile after tapping the icon.

### Product Card

**`product-card`** — Fixed-width card with 1px {colors.hairline} border and {rounded.sm} radius. Product photograph fills the top portion; below, variety name in {typography.title-md} (Raleway 600), pack size and days-to-maturity details in {typography.body-sm}, and price in {typography.price-display} (Raleway 700 at 20px). Sale and New badges overlay the image corner. Cards sit in a 4-up grid on desktop, 2-up on tablet, 1-up on mobile.

### Hero Banner

**`hero-banner`** — Warm off-white {colors.surface-soft} background with a full-bleed botanical photograph filling roughly 55% of the panel on desktop. The headline runs in {typography.hero-script} (Playlist Script at 64px) in warm dark {colors.accent-script} (#4a3728), evoking a hand-lettered seed packet label. Subhead drops to {typography.display-sm} Raleway 700 in {colors.ink}. Seasonal variants (spring bulbs, fall planting, wildflower meadow) reuse the same template with swapped imagery and script text.

### Badges

**`category-badge`** — Small outlined chip in primary green: {colors.surface-soft} fill, 1px {colors.primary} border, uppercase {typography.badge} Raleway at {rounded.xs}. Tags plant types (Annual, Perennial, Native, Heirloom) on collection pages and product pages.

**`sale-badge`** / **`new-badge`** — Solid fills in rust {colors.accent-rust} and green {colors.primary} respectively, white uppercase {typography.badge}, corner-placed on product card images. Both use {rounded.xs} to align flush with the card's own corner radius.

### Footer

**`footer`** — Near-black {colors.ink} background with white body text and {colors.hairline} link text. {typography.body-sm} for links, {typography.title-sm} at weight 600 for column headers. Four-column grid on desktop collapses to two-column on tablet and accordion on mobile. Newsletter signup sits above the link columns with a borderless underline-style input tuned for the dark background.

### Seasonal Editorial Block

**`seasonal-editorial`** — A warm {colors.surface-soft} full-width panel with a Playlist Script headline in {colors.accent-script} and body copy in {typography.body-md} Raleway. Used between catalog sections to interrupt commercial density with a moment of garden narrative. {rounded.md} container on desktop; full-bleed with square edges on mobile.

### Tags and Filters

**`tag-chip`** — Pill-shaped ({rounded.full}) filter tags for collection filtering by color, season, sun requirements, and growing zone. Default state uses {colors.surface-soft} background with {colors.muted} text; active fills with {colors.primary} and white {colors.on-primary} label. {typography.tag-label} (Raleway 11px, 700, uppercase, 1px tracking) gives filter chips a botanical-reference character that echoes seed-packet annotation.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + Fontello icons; hero stacks vertically with script headline above image; mega-menu becomes full-screen drawer; search expands to full-width overlay; footer columns become tappable accordions |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + icons with categories in hamburger drawer; hero splits 50/50 image-text; mega-menu as side drawer |
| Desktop | 1128–1440px | Four-column product grid; full horizontal nav with mega-menu on hover; hero is 45/55 text-image split; sticky nav bar persists |
| Wide | > 1440px | Max content width 1440px centered; hero image extends full-bleed behind constrained text column; product grid stays 4-up with increased card padding |

### Touch Targets

- All nav icon buttons (cart, search, account) minimum 44×44px tappable area
- Product card entire surface is tappable — anchor wraps full card
- Quantity selector increment/decrement buttons minimum 40×40px
- Tag-chip filters minimum 36px tall with wider horizontal slop on mobile
- Footer accordion headers minimum 48px tall tap area

### Collapsing Strategy

- Nav mega-menu converts to a slide-in drawer from the left on tablet and mobile
- Product filter sidebar (desktop) converts to a bottom-sheet modal on mobile
- Hero banner stacks vertically below 744px: script headline above, photograph below, CTA below photograph
- Four-column product grid → two-column at 744px → one-column at 480px
- Seasonal editorial block loses {rounded.md} and becomes full-bleed below 744px
- Footer four-column grid → two-column at 744px → tap-to-expand accordion below 744px

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Primary brand color unconfirmed**: Only #121212 and #dedede were extracted from the live site; the botanical green primary (#3b6b35) is inferred from brand context and must be verified against the actual site stylesheet or brand guide before production use.
- **Full accent palette missing**: Rust accent (#b85c38), warm script-text brown (#4a3728), and surface-soft warm white (#f7f5f0) are inferred; no additional colors were extractable from the Shopify theme's CSS layer.
- **Font weights not confirmed**: Raleway is a variable-weight typeface; the specific weight assignments used for button labels, price displays, and nav links are estimated from convention rather than extracted CSS values.
- **Playlist Script display size**: The exact pixel size and baseline used for Playlist Script in hero contexts was not extractable; 64px is a plausible estimate for a seed-brand hero headline.
- **Component border-radius**: The Shopify theme's own token overrides may differ from the {rounded.sm} assumption applied to cards and inputs; verify in the live theme's `settings_data.json`.
- **Fontello glyph coverage**: Fontello is a custom-subset icon font; the specific glyphs included in Eden Brothers' build are not enumerable from page extraction alone.
- **Breakpoints**: Exact pixel breakpoints used by the Shopify theme are unconfirmed; values in Responsive Behavior reflect common Dawn/Shopify 2.0 theme conventions.
