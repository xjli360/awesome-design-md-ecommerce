---
version: alpha
name: "The Artling"
source_url: "https://theartling.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Gold where most contemporary gallery platforms choose institutional black or clinical white, The Artling's #b79b54 brass primary anchors every purchase CTA, filter accent, and navigational emphasis — a warm metallic register that signals accessible connoisseurship rather than auction-house austerity. The double-serif type stack deepens this editorial identity: Addington CF carries display headings and hero callouts at weights 500–700, while Lora handles body copy and artwork descriptions, a pairing borrowed from art-book and catalogue publishing rather than e-commerce convention. Rounded corners are near-absent across the system — artwork cards run `{rounded.none}`, buttons sit at `{rounded.sm}` (4px), and only filter pills use `{rounded.full}` — the geometry stays flat and measured so that photography commands the frame without interference. The canvas is #fdfcfa, a warm off-white that preserves a print-on-paper naturalness without clinical gallery brightness; hairlines draw from #d9d9d9, light enough to divide an artwork grid without competing with the work itself. What most distinguishes The Artling's visual language is a pastel medium-tagging system: each artwork category carries its own hue — #b5dced for photography, #c6e5b8 for sculpture, #ddcee2 for prints, #efe7a5 for works on paper, #f3d6b9 for ceramics, #f6d8d8 for textiles — rendered at `{rounded.full}` as compact pill badges that communicate medium at a glance. Status signals are high-chroma: #890000 marks sold works and #005f16 flags available inventory, both appearing as small flat badges overlaid on the artwork image. Text hierarchy steps through #2b2b2b (ink), #444444 (body), and #747474 (metadata), a restrained three-stop ladder legible across both dense grid views and full-bleed editorial layouts.

colors:
  primary: "#b79b54"
  primary-active: "#8d7840"
  primary-disabled: "#d9d1c2"
  gold-warm: "#cfa948"
  ink: "#2b2b2b"
  body: "#444444"
  muted: "#747474"
  muted-light: "#acacac"
  hairline: "#d9d9d9"
  hairline-soft: "#e5e7eb"
  canvas: "#fdfcfa"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  surface-warm: "#d9d1c2"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-crimson: "#890000"
  accent-forest: "#005f16"
  status-error: "#bd1717"
  tag-blue: "#b5dced"
  tag-green: "#c6e5b8"
  tag-lavender: "#ddcee2"
  tag-yellow: "#efe7a5"
  tag-peach: "#f3d6b9"
  tag-rose: "#f6d8d8"

typography:
  display-xl:
    fontFamily: "'Addington CF', Lora, Georgia, serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Addington CF', Lora, Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Addington CF', Lora, Georgia, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Addington CF', Lora, Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Addington CF', Lora, Georgia, serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Lora, 'Addington CF', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "Lora, 'Addington CF', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'Addington CF', Lora, Georgia, serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  footer-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
  artwork-card:
    backgroundColor: "{colors.surface-card}"
    titleTypography: "{typography.title-sm}"
    artistTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    mediumTypography: "{typography.caption}"
    titleColor: "{colors.ink}"
    artistColor: "{colors.muted}"
    priceColor: "{colors.ink}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
    imageAspectRatio: "1/1"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    paddingVertical: "{spacing.section}"
  category-tag:
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
    defaultBackgroundColor: "{colors.tag-blue}"
    textColor: "{colors.ink}"
  sold-badge:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  available-badge:
    backgroundColor: "{colors.accent-forest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    activeBorderColor: "{colors.primary}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  price-label:
    textColor: "{colors.ink}"
    typography: "{typography.price}"
    currencyMutedColor: "{colors.muted}"
  curator-pick-banner:
    backgroundColor: "{colors.surface-warm}"
    accentBorderColor: "{colors.primary}"
    headlineTypography: "{typography.display-sm}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.footer-link}"
    headingTypography: "{typography.caption-bold}"
    linkColor: "{colors.muted-light}"
    headingColor: "{colors.on-dark}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    iconColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px

## Components

### Buttons
**`button-primary`** — A 44px flat rectangle at `{rounded.sm}` filled with brass #b79b54, white label text in Helvetica Neue at 14px with 0.5px letter-spacing. Active state deepens to #8d7840; disabled washes to #d9d1c2 with muted text. The near-sharp corner geometry is intentional — it echoes the flat artwork grid rather than the pill-CTA softness of lifestyle commerce.

**`button-secondary`** — Outlined counterpart: white canvas fill, 1px #b79b54 border, and gold text. Used for secondary actions (Save to Wishlist, Request a Quote, Make an Offer) beside a primary CTA. Does not change border to a neutral on hover — the gold border persists to keep brand presence on passive states.

**`button-ghost`** — Transparent background with underlined muted-gray text at `{typography.button-md}`. Used for tertiary editorial actions like "See All Works" and "Read Artist Statement" within body content zones.

### Text Input
**`text-input`** — 44px input on #ffffff with a 1px #d9d9d9 hairline border. On focus, the border transitions to #b79b54 gold — the only place focus state introduces color outside of buttons. Placeholder text in #747474. Lora body-md at 16px. Corner radius at `{rounded.sm}` matches the button system.

### Navigation
**`nav-bar`** — 64px header on #fdfcfa canvas divided from page content by a bottom hairline in #d9d9d9. Logo is an ink-#2b2b2b wordmark on the left; right side carries search, account, and cart icons at 24px. Navigation links in Helvetica Neue nav-link (14px, 400) with underline-only hover — no fill or pill highlight. Category mega-nav drops on hover with a white panel at full viewport width, organized by medium.

### Artwork Card
**`artwork-card`** — Zero-radius cards in a responsive CSS grid, image area at 1:1 aspect ratio above a flush metadata block. Title line in Addington CF title-sm (16px, 500) in ink; artist name in Lora body-sm (14px) in #747474 muted; price in Addington CF price (16px, 600) in ink. Category tag badges row below the artist line. On hover, the image receives a subtle 1.02× scale transform with no card shadow elevation — the effect reads as zoom-in rather than lift.

### Hero Banner
**`hero-banner`** — Full-width editorial zones on #fdfcfa canvas with Addington CF display-xl at 40px. Body copy in Lora body-md at 16px, line-height 1.65. A single `button-primary` CTA sits below the subhead at `{spacing.lg}` gap. Vertical padding at `{spacing.section}` (64px). Image compositions use split-halves — photography occupies 50–60% of viewport width alongside the headline block; no full-bleed overlay text.

### Category Tags
**`category-tag`** — 11px uppercase-spaced pill badges at `{rounded.full}` with the pastel swatch set: #b5dced photography, #c6e5b8 sculpture, #ddcee2 prints, #efe7a5 works on paper, #f3d6b9 ceramics, #f6d8d8 textiles. Text is always #2b2b2b ink regardless of swatch. Multiple tags stack in a horizontal flex row with `{spacing.xs}` (4px) gaps; truncate at 2 on mobile grid cards with a "+N" overflow indicator.

### Status Badges
**`sold-badge`** — #890000 crimson flat badge at `{rounded.xs}` with white uppercase type at 11px, positioned top-left on the artwork image. No border, no blur — high-chroma flat signal. **`available-badge`** — #005f16 forest green for works that are explicitly in-stock or part of a limited edition with remaining count.

### Filter Pills
**`filter-pill`** — Horizontal scrolling filter strip below the nav for medium, price, size, and style filters. Inactive: #f2f2f2 fill, ink text, no border. Active: adds a 1px #b79b54 border with gold text — the same primary token that drives buttons, making active filters visually consistent with the CTA system. Caption typography at 13px Helvetica Neue.

### Curator Pick Banner
**`curator-pick-banner`** — A warm #d9d1c2 surface zone with a 3px #b79b54 gold left-edge accent rule. Addington CF display-sm (22px) headline, Lora body-md description. Used in collection editorial sections and curated theme pages (e.g., "Art Under $1,000", "New Arrivals from Southeast Asia"). Padding at `{spacing.xl}` all sides.

### Footer
**`footer`** — Dark #2b2b2b background with white on-dark text. Column headings in caption-bold (Helvetica Neue 13px, 600); links in footer-link (13px, 400) at #acacac muted-light for a receded treatment. Four standard columns: About, Discover, Sell With Us, Support. Newsletter input field floats in a top footer zone above the column grid with the text-input focus gold ring intact on dark background.

### Search Bar
**`search-bar`** — Inline field on #f2f2f2 surface-soft with a #b79b54 search icon (right-aligned). Expands to full width on focus on mobile, collapses to icon-only within the compressed nav state. Corner radius `{rounded.sm}`, same 44px height as the text-input.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column artwork grid; filter pills scroll horizontally; nav collapses to hamburger + wordmark + cart; hero headline scales to display-md (28px); category tags truncate to 2 per card |
| Tablet | 744–1128px | Two-column artwork grid; filter bar wraps to two rows; nav shows top-level category labels only; hero switches to stacked image-over-text layout |
| Desktop | 1128–1440px | Three- to four-column artwork grid; full mega-nav with category flyouts; split-image hero layout; curator banners use two-column editorial layout |
| Wide | > 1440px | Content container capped at 1440px and centered on canvas; section padding increases to 80px; artwork grid stays at four columns with wider gutters |

### Touch Targets
- All interactive elements minimum 44×44px tap area
- Filter pills padded to 44px tap height on mobile regardless of visual label size
- Artwork card tap area covers full card tile including whitespace below image metadata
- Nav icons (search, account, cart) maintain minimum 48px horizontal spacing
- Category tag badges on mobile are individually tappable with 36px minimum vertical hit area

### Collapsing Strategy
- Artwork card category tags truncate to 2 badges with "+N" indicator at mobile
- Artist biography text collapses behind "Read more" toggle below 100 characters on mobile detail pages
- Footer collapses from 4 columns to 2 at tablet, to a single accordion-disclosure column at mobile
- Mega-nav category flyout becomes a full-screen drawer on mobile with back-navigation
- Price filter range inputs collapse into a single trigger chip on narrow viewports

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Meta theme-color not set; primary #b79b54 inferred from dominant extracted hex palette, not confirmed from `<meta>` tag
- Addington CF is a commercial typeface (Yellow Design Studio); weight variants available (Light 300, Regular 400, Bold 700, ExtraBold 800) not confirmed from extraction — weights assumed from visual hierarchy patterns
- Lora usage split between editorial body and UI labels not confirmed; defaulted to 400/body and 600/price based on font-stack order in extraction
- Exact border-radius values not extractable; 4px (sm) assumed from flat art-market UI conventions
- Hover/transition animation timing not extractable from static extraction
- Mobile navigation pattern (full-screen overlay vs. slide-in drawer) not confirmed
- Dark mode support not evidenced; no dark surface tokens present in extraction
- Cart and wishlist icon color treatment (gold vs. ink) on nav-bar not confirmed
