---
version: alpha
name: "Pamela Love"
source_url: "https://www.pamelalove.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Ortica-Light letterforms lean at a near-whisper weight over a canvas of warmed cream (#f8f4f2), announcing that every choice here is deliberate restraint rather than absence of ambition. Pamela Love's jewelry—cast talons, celestial arcs, molten bronze settings—demands a digital container that feels excavated rather than designed: deep espresso-black (#170c0a) grounds the site like scorched earth, while a copper-warm terracotta (#956c56) and a dusty rose-tan (#c89173) echo the oxidized metal and raw gemstone surfaces of the objects themselves. The typographic stack is unusually layered for a jewelry brand—Peskia and Ortica-Light for display, EB Garamond for editorial prose, Pitch Sans for functional UI labels, ag-book-extended for section headers—suggesting a studio that treats each typographic register as a distinct material rather than a single house style. Buttons carry zero border-radius at their core: no pill forms, no friendly rounding, all square-edged authority, a hard corner that mirrors the forged quality of the product. Product cards sit on a neutral warm-gray surface (#d3cfce), photographed on skin or stone rather than white infinity, so the image bleeds to edge without a visible frame. Navigation runs in tight Pitch Sans uppercase tracking, compressed against the left, a quiet grid that never competes with the editorial photography below it. The overall surface temperature is warm without being feminine in any conventional sense—cream and espresso and copper together read closer to a craftsperson's worktable than a jewelry-box lining. Social-share icons (Twitter/Facebook blues, Pinterest red) are isolated from the brand palette entirely; the only voltage that belongs to Pamela Love is the earthen spectrum from #f8f4f2 through #956c56 to #170c0a.

colors:
  primary: "#170c0a"
  primary-active: "#373737"
  primary-disabled: "#a1a1a1"
  ink: "#170c0a"
  body: "#373737"
  muted: "#606060"
  muted-soft: "#a1a1a1"
  hairline: "#d9d9d9"
  hairline-soft: "#e6e6e6"
  canvas: "#f8f4f2"
  surface-soft: "#d3cfce"
  surface-card: "#e6e6e6"
  surface-warm: "#f8f4f2"
  on-primary: "#f8f4f2"
  accent-copper: "#956c56"
  accent-rose-tan: "#c89173"
  accent-dark-terra: "#812a17"
  divider: "#dbdbdb"

typography:
  display-xl:
    fontFamily: "'Ortica-Light', 'EB Garamond', Georgia, serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Ortica-Light', 'EB Garamond', Georgia, serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Peskia', 'Ortica-Light', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: 0.1px
  display-sm:
    fontFamily: "'ag-book-extended', 'Instrument Sans', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.08em
    textTransform: uppercase
  title-md:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Pitch Sans', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.06em
    textTransform: uppercase
  body-md:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  caption-pitch:
    fontFamily: "'Pitch Sans', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "'Pitch Sans', 'Instrument Sans', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Pitch Sans', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-label:
    fontFamily: "'Pitch Sans', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  price:
    fontFamily: "'Instrument Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.02em
  logo-display:
    fontFamily: "'Culture', 'Peskia', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.04em

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
    height: 44px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 44px
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.logo-display}"
    paddingX: "{spacing.xl}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-label}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.lg}"
    shadowY: 4px
    shadowBlur: 12px
    shadowColor: "rgba(23,12,10,0.08)"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspect: "4/5"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.md}"
    gap: "{spacing.sm}"
    imageObjectFit: cover
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    imageCursor: zoom-in
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    minHeight: 80vh
    paddingX: "{spacing.xxl}"
    paddingY: "{spacing.section}"
    imageBlend: multiply
    textAlign: left
  hero-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 70vh
    paddingX: "{spacing.xxl}"
    paddingY: "{spacing.section}"
  editorial-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    paddingX: "{spacing.xxl}"
    paddingY: "{spacing.section}"
    maxWidth: 680px
    textAlign: left
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-pitch}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-badge-new:
    backgroundColor: "{colors.accent-copper}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-pitch}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-lg}"
    subheadTypography: "{typography.display-sm}"
    borderBottom: "1px solid {colors.hairline}"
    paddingY: "{spacing.xxl}"
    paddingX: "{spacing.xxl}"
  filter-pill:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
  filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 40px
    paddingX: "{spacing.base}"
    iconColor: "{colors.muted}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    itemTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    borderLeft: "1px solid {colors.hairline}"
    width: 400px
    paddingX: "{spacing.xl}"
    paddingY: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.caption-pitch}"
    headingTypography: "{typography.display-sm}"
    paddingX: "{spacing.xxl}"
    paddingY: "{spacing.section}"
    linkColor: "{colors.surface-soft}"
    linkHoverColor: "{colors.accent-copper}"
    dividerColor: "rgba(248,244,242,0.15)"
  divider-rule:
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    marginY: "{spacing.lg}"
  announcement-bar:
    backgroundColor: "{colors.accent-copper}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-pitch}"
    height: 36px
    paddingX: "{spacing.base}"

## Components

### Buttons

**`button-primary`** — A completely square-cornered fill button in deep espresso (#170c0a) with cream (#f8f4f2) Pitch Sans uppercase labels at 12px/0.12em tracking. The zero-radius edge signals forged craft rather than consumer friendliness. On hover, the background shifts to dark charcoal (#373737); disabled state uses #a1a1a1 without border modification. Minimum height 44px ensures accessibility without softening the industrial silhouette.

**`button-secondary`** — An outlined square-edge button matching the primary in size and typography but with a 1px #170c0a stroke over transparent fill. On hover the fill inverts — background becomes espresso, label becomes cream — creating a clean toggle effect without introducing new colors. Works on both light canvas and warm-gray surface backgrounds.

**`button-ghost`** — Text-only, no border, no background. Uses muted gray (#606060) Pitch Sans uppercase for supplementary actions like "View All" in editorial strips. No hover state fill; only a subtle opacity shift to 0.7.

### Navigation

**`nav-bar`** — 64px bar in cream (#f8f4f2) with a 1px #d9d9d9 bottom border. The wordmark uses `{typography.logo-display}` in Culture or Peskia at left; navigation links use `{typography.nav-label}` in Pitch Sans uppercase center or right. A minimal icon cluster (search, account, cart) anchors the far right. The overall tone is archival-editorial rather than e-commerce utilitarian — category links appear without visual decoration, no underlines on rest state.

**`nav-dropdown`** — A borderless overlay panel, light canvas fill with a very soft shadow (4px Y, 12px blur, 8% espresso tint). Links inside use `{typography.nav-label}` with generous vertical spacing ({spacing.lg} per item). No background hover fill on links — only a copper (#956c56) color shift.

### Product Cards

**`product-card`** — Images render at 4:5 portrait aspect in `object-fit: cover` on warm gray (#d3cfce) surface. No border, no rounded corner. Title in `{typography.title-md}` Instrument Sans sits {spacing.sm} below the image; price in `{typography.price}` follows immediately. On hover the card surface shifts to #e6e6e6 — no scale transform, no box shadow — the stillness matches the object photography. "New" badges use `{typography.caption-pitch}` in copper (#956c56) fill.

### Hero

**`hero`** — Full-bleed dark hero in #170c0a with left-aligned display heading in Ortica-Light at 56px weight 300. Subheading renders in `{typography.display-sm}` ag-book-extended uppercase. Photography is darkroom-toned against skin or stone, layered multiply over the espresso field. Minimum 80vh; internal padding uses {spacing.section} vertical, {spacing.xxl} horizontal so text sits in the lower third.

**`hero-light`** — Cream (#f8f4f2) variant for collection openings. Same left-aligned editorial treatment but heading color switches to #170c0a, body copy uses `{typography.body-md}` EB Garamond at 17px for a more literary, less campaign feel.

### Editorial Strip

**`editorial-strip`** — A full-width band in surface-soft (#d3cfce) containing a constrained 680px text column. Heading in `{typography.display-md}` Peskia; body in `{typography.body-md}` EB Garamond. Used for artist statements, material sourcing notes, and process descriptions. No CTA inside the strip itself — a separate button-secondary appears below the block.

### Filters

**`filter-pill`** / **`filter-pill-active`** — Square-edge ghost pills for collection filtering. Inactive: 1px #d9d9d9 border, transparent fill, #606060 label. Active: #170c0a fill, cream label, same 0px radius. Pills sit in a horizontal scroll row on mobile without wrapping.

### Footer

**`footer`** — Full espresso (#170c0a) background with cream (#f8f4f2) link text in Pitch Sans uppercase 11px. Column headers use `{typography.display-sm}` ag-book-extended. Social icons render in #d3cfce; on hover they warm to accent-copper (#956c56). A fine 1px divider at 15% cream opacity separates the newsletter input from the link columns above.

### Announcement Bar

**`announcement-bar`** — 36px strip in copper (#956c56) above the nav, Pitch Sans uppercase 11px, cream text. Used for shipping promotions and new collection drops. Single centered line only.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen dark overlay menu; hero heading drops to 36px Ortica-Light; filter pills scroll horizontally; cart drawer goes full-width |
| Tablet | 744–1128px | Two-column product grid; nav retains wordmark + icon cluster only (categories hidden behind hamburger); hero heading 44px; editorial strip full-width with internal padding |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with inline category links; hero heading 56px; cart drawer fixed 400px; editorial strip max-width 680px centered |
| Wide | > 1440px | Four-column product grid; outer gutters expand to keep content max-width ~1360px; hero text column constrained to 600px left; footer columns gain more breathing room |

### Touch Targets

- All buttons minimum 44px height; ghost text buttons padded to 44px tap target with invisible padding
- Nav icons (search, cart, account) minimum 44×44px hit area
- Filter pills minimum 40px height on mobile with 8px horizontal gap between pills
- Product card entire surface is tappable to PDP; no separate CTA button required at this scale

### Collapsing Strategy

- Navigation: full desktop nav → wordmark + icons only (tablet) → hamburger full-screen overlay (mobile), overlay background #170c0a at 98% opacity
- Product grid: 4 col → 3 col → 2 col → 1 col, gutter stays {spacing.base} throughout
- Hero: text left-aligned on all breakpoints; image proportion shifts from 50/50 text+image split (desktop) to image-top text-below stack (mobile)
- Editorial strip: prose column expands to 100% width below tablet, with {spacing.xl} padding preserved
- Footer: 4-column link grid collapses to 2 columns (tablet) then accordion-expandable single column (mobile)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed hex values for interactive link states (underline color, visited color) — muted gray (#606060) assumed
- Font files for Culture, Peskia, and Ortica-Light are proprietary/custom; exact weights and optical sizes beyond "Light/Regular" are unconfirmed
- ag-book-extended weight variants (bold vs. regular) not confirmed from extraction; "regular/400" assumed for section headers
- No extracted shadow tokens; values in nav-dropdown and cart-drawer are estimated from common Shopify theme conventions
- Meta theme-color absent — mobile browser chrome color unspecified; #170c0a recommended as a reasonable default given the dark brand
- Hover/focus ring color for keyboard accessibility not extractable from static scrape; recommend 2px offset outline in #956c56 (accent-copper) for brand coherence
- Several near-identical grays (#dbdbdb, #dedede, #d9d9d9, #e6e6e6) suggest possible redundancy in the live stylesheet; exact semantic assignments (hairline vs. surface vs. divider) are inferred from visual hierarchy rather than confirmed token names
- The reds extracted (#c8232c, #cc3333, #cb2b2b, #f94c43) are consistent with Pinterest share buttons and error states, not brand colors — excluded from the primary palette
- Social blues (#4469af, #00aced, #2980b9, #899df1) similarly excluded as platform-injected colors
