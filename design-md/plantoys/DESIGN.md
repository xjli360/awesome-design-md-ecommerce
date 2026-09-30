---
version: alpha
name: "PlanToys"
source_url: "https://plantoys.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Forty shades of forest open the PlanToys storefront: sage (#aacc98) anchors every primary action surface while #f0f6ed mint-washed panels separate editorial content from commerce, giving the layout the warmth of a toy shelf photographed at golden hour. The real design intelligence is in how the brand extends its product's own developmental color vocabulary into the interface — the primaries that appear on the toys themselves, red (#d21625), sky blue (#79c2d4), and sunshine yellow (#ffff00), reappear as category chips, age-range badges, and developmental-domain tags, so browsing a product grid teaches the same hue associations the product teaches a child. VAGRN-Bold carries all hero display text in a chunky, slightly compressed face that reads as hand-lettered without collapsing into whimsy; Nunito handles body paragraphs and product descriptions with rounded terminals that soften reading for a design-literate parent audience; Hind takes over for UI chrome — filter toggles, price strings, form labels — where optical neutrality beats personality. Corners are generous throughout: product cards sit at {rounded.md}, filter pills and age chips at {rounded.full}, and the primary CTA runs a full-radius pill that echoes the rounded profiles of the wooden objects on shelf. The sustainability mission is never subtext: a dedicated eco-badge system surfaces material certifications directly on product cards rather than relegating them to footer copy, and the sage-on-mint art direction anchors every hero to the brand's Thai forest origins. There are no hard dark backgrounds — the darkest structural element is the charcoal nav (#333336), which provides just enough contrast for wayfinding without importing the brand-tech gravity that would age the experience. The deepest purples (#50248f, #43467f) appear only in developmental-domain tags, functioning as a secondary signal system that turns product browsing into play rather than transaction.

colors:
  primary: "#aacc98"
  primary-active: "#7aad6e"
  primary-disabled: "#d0e6c7"
  eco-teal: "#47c1bf"
  sky-blue: "#79c2d4"
  toy-red: "#d21625"
  toy-yellow: "#ffff00"
  toy-green: "#37e983"
  toy-purple: "#50248f"
  toy-indigo: "#43467f"
  toy-pink: "#e8909c"
  ink: "#333336"
  body: "#5b5b5e"
  muted: "#969595"
  hairline: "#dedede"
  hairline-soft: "#eaecf0"
  canvas: "#f9fafb"
  surface-soft: "#f0f6ed"
  surface-card: "#f6f6f6"
  surface-strong: "#f2f2f2"
  on-primary: "#333336"
  on-dark: "#f9fafb"

typography:
  display-xl:
    fontFamily: "'VAGRN-Bold', 'Nunito', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'VAGRN-Bold', 'Nunito', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'VAGRN-Bold', 'Nunito', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Hind', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Hind', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  age-label:
    fontFamily: "'Hind', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  eco-tag:
    fontFamily: "'Hind', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "'Hind', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 18px
    fontWeight: 700
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.ink}"
    rounded: "{rounded.full}"
    padding: 12px 30px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1.5px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    logoHeight: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    imageBorderRadius: "{rounded.md}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    shadow: "0 2px 8px rgba(51,51,54,0.08)"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
  age-badge:
    backgroundColor: "{colors.eco-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.age-label}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.sm}"
  eco-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.eco-tag}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.sm}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1.5px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    height: 38px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    height: 38px
  dev-domain-tag:
    backgroundColor: "{colors.toy-indigo}"
    textColor: "{colors.on-dark}"
    typography: "{typography.age-label}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1.5px solid {colors.hairline-soft}"
    borderFocus: "1.5px solid {colors.primary}"
    rounded: "{rounded.full}"
    height: 44px
    padding: "0 {spacing.base}"
  sustainability-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — A full-radius sage pill (#aacc98, `{rounded.full}`) at 48px height, `{typography.button-md}` Nunito Bold in #333336 ink. Hover shifts fill to `{colors.primary-active}` (#7aad6e); disabled bleaches to `{colors.primary-disabled}` with `{colors.muted}` text. The pill shape is load-bearing — it mirrors the rounded profiles of wooden toy pieces and signals playfulness without infantilizing.

**`button-secondary`** — Canvas fill with a 2px solid #333336 border and `{rounded.full}` rounding, matching primary proportions exactly. Hover shifts border and text to `{colors.primary-active}`. Used for "Learn More" and secondary editorial CTAs where the sage primary would visually compete with adjacent photography.

**`button-ghost`** — Transparent background, `{colors.primary-active}` text, no border, `{rounded.full}`. Appears inline within product description copy and sustainability module prose; keeps the reading flow uninterrupted while still providing an actionable link.

### Text Input

**`text-input`** — 44px tall field at `{rounded.sm}`, 1.5px `{colors.hairline}` border that transitions to `{colors.primary}` on focus with no box-shadow added. Runs `{typography.body-md}` Nunito in `{colors.ink}`. The minimal state change (border color only) keeps forms quiet against the light mint-wash surface behind them.

### Navigation

**`nav-bar`** — The single hard-edged dark surface on the site: #333336 at 64px height. Logo (36px) in white, nav links in `{typography.nav-link}` (Hind SemiBold 15px) in `{colors.on-dark}`. A secondary utility row beneath carries search, account, and cart icons at 24px. The dark bar grounds an otherwise light, nature-toned layout and visually anchors page scroll.

### Product Card

**`product-card`** — `{colors.surface-card}` (#f6f6f6) panel at `{rounded.md}`, 8px shadow at 8% ink opacity. Product image fills the top portion with matching `{rounded.md}` clip. Title in `{typography.title-sm}` (Nunito SemiBold 16px), price in `{typography.price-display}` (Nunito Bold 18px). An `age-badge` and up to two `dev-domain-tag` chips float over the image at top-right. An `eco-badge` sits inline below the price line, never collapsed behind a tooltip.

### Hero Banner

**`hero-banner`** — Full-width section on `{colors.surface-soft}` (#f0f6ed), headline in `{typography.display-xl}` (VAGRN-Bold 56px), subhead in `{typography.body-md}`. Left-aligned text column on desktop with product photography spanning the right half; stacks vertically on mobile with image below. Primary CTA uses `button-primary`. No background pattern or illustration — photography carries all visual weight.

### Age Badge

**`age-badge`** — Teal (#47c1bf) full-radius pill at 24px height, white text in `{typography.age-label}` (Hind SemiBold 11px, uppercase, 0.5px tracking). Values like "2+" or "3–6 yrs". The teal reads as a consistent developmental-signal color distinct from the sage primary and the indigo domain tags, avoiding a three-way collision on the product card.

### Eco Badge

**`eco-badge`** — Light mint (#f0f6ed) pill with `{colors.primary-active}` text and a 1px `{colors.primary}` border, `{rounded.full}`. `{typography.eco-tag}` (Hind SemiBold 11px, uppercase). Labels: "Recycled Rubber", "Non-Toxic Paint", "FSC Certified Wood". Appears on product cards and again as an expanded certification cluster in the PDP sustainability section — never relegated to footer-only.

### Category Pill / Filter

**`category-pill`** — Inactive: #f0f6ed fill, #5b5b5e text, 1.5px #dedede border, `{rounded.full}`, 38px height. Active (`category-pill-active`): #aacc98 fill, #333336 text, matching border. Filter rows scroll horizontally on mobile without wrapping. Interaction is single-tap toggle; no confirmation dialog, no multi-select mode on mobile. Desktop shows a wrapping two-row grid of pills above the product shelf.

### Development Domain Tag

**`dev-domain-tag`** — Small #43467f indigo chip at `{rounded.xs}`, 22px height, `{colors.on-dark}` text in `{typography.age-label}`. Domain values: "Motor Skills", "Creativity", "Language", "Social", "Emotional". Product cards show up to two tags; PDP expands to the full domain set as a horizontal chip cluster. Tags on the PDP are tappable and filter the related-products shelf to matching developmental domains.

### Search Bar

**`search-bar`** — 44px `{rounded.full}` input pill, `{colors.canvas}` fill, `{colors.hairline-soft}` border shifting to `{colors.primary}` on focus. Magnifier icon in `{colors.muted}` sits left-inset; placeholder text in `{colors.muted}`, `{typography.body-md}`. Appears in the nav utility row as a compact variant and as a full-width element on the standalone search results page.

### Sustainability Strip

**`sustainability-strip`** — A 36px full-width banner in `{colors.primary}` (#aacc98) with a single centered sentence in `{typography.caption}` (Hind 12px, `{colors.on-primary}`). No CTA, no icon — purely editorial. Sits immediately below the nav bar on all pages. On product pages the strip rotates through two or three mission statements on a slow auto-cycle.

### Footer

**`footer`** — Charcoal (#333336) background mirroring the nav, `{typography.body-sm}` (Hind 14px) in `{colors.on-dark}`. Links in `{colors.primary}` with no underline; underline on hover. Four-column layout on desktop: About, Products, Sustainability, Connect. Social icons at 24px outline weight in `{colors.on-dark}`. A row of `eco-badge` chips runs directly above the legal copy line as a terminal trust signal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category pills scroll horizontally without wrapping; nav collapses to hamburger + centered logo + cart icon; hero stacks text above image; footer collapses to single-column accordion |
| Tablet | 744–1128px | Two-column product grid; category pills wrap to two rows; nav shows top-level categories without dropdown, utility icons visible; hero overlays text on image at reduced opacity |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdown category mega-menus; hero runs left/right split; sustainability strip and eco-badge clusters fully visible |
| Wide | > 1440px | Layout caps at 1440px max-width centered; four-column product grid available on collection pages; hero image scales to fill remaining viewport width beyond the content column |

### Touch Targets
- All interactive elements minimum 44×44px per iOS HIG
- Category pills padded to 38px height minimum; width expands to label content
- Age badge and eco badge on product cards are display-only; they do not carry a tap target
- Dev domain tags on PDP are tappable, filtering the related-products shelf
- Nav hamburger icon target padded to 48×48px on mobile
- Search icon in nav expands to full-width search overlay on tap

### Collapsing Strategy
- Product grid: 1 col (mobile) → 2 col (tablet) → 3 col (desktop) → 4 col (wide)
- Hero: stacked single-column (mobile) → text-on-image overlay (tablet) → left/right split (desktop+)
- Footer: single-column accordion (mobile) → two-column (tablet) → four-column (desktop+)
- Category filter row: horizontally scrollable single row (mobile) → two-row wrapping grid (tablet+)
- Sustainability strip: visible at all breakpoints; text truncates with ellipsis below 360px viewport width

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; charcoal (#333336) assumed for browser chrome tinting on Android but unconfirmed
- VAGRN-Bold is a proprietary face with uncertain weight variants and no confirmed variable axis; Nunito is specified as the fallback for all display positions
- Exact computed border-radius values not extracted; `{rounded.full}` for CTAs and `{rounded.md}` for cards are inferred from visual observation of product photography and toy-brand conventions
- Dropdown mega-menu background color, hover states, and column count not confirmed from extracted data
- Interactive hover colors (nav links, filter pills) derived by programmatic lightening/darkening of extracted hex values rather than from explicit extracted state tokens
- Toy-yellow (#ffff00) is pure saturated yellow from extraction — likely a product/illustration-only color; restricted here to toy photography context rather than UI chrome
- Sale badge palette and price strikethrough color (presumed `{colors.toy-red}`) not confirmed from extraction
- #0171e5 and #3056a7 appear in extraction but their origin (possibly Shopify-injected payment UI or third-party review widget chrome) is ambiguous; excluded from the design system palette
- #230051 (deep purple) appears in extraction but usage context is unclear — possibly a seasonal campaign color or third-party embed; not assigned a design token
