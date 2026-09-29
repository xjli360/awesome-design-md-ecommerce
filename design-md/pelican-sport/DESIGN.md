---
version: alpha
name: "Pelican Sport"
source_url: "https://www.pelicansport.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Electric chartreuse (#d2de31) is the first thing that breaks from expectation — not the ocean blue most paddle brands default to, but the high-vis color of a buoy marker, a tow rope end-cap, a spray skirt pull tab. Pelican Sport builds its interface from a teal-and-forest-green spine (#108474 anchoring into #277158 and down into the near-black depths of #0c5132), then detonates that spine with two accent voltages: chartreuse for promotional callouts and amber (#fbcd0a) for secondary signals. The combination maps to how safety equipment actually looks on water — not aspirational photography blue but the literal palette of gear you grab in a hurry.

  Dark anchors run deep: #1a1a1a and #0a0a0a appear in footer backgrounds and high-contrast text blocks, and #1a1a2e (a blue-tinted near-black) introduces a depth register in hero sections that reads as open water after dark rather than generic dark mode. Against that, the canvas is near-white (#f9fafb) rather than pure white, softening light-mode surfaces without the gray neutrality that makes sporting-goods sites feel like industrial catalogues.

  Geologica carries the display work — its variable axis allows headline weights from 400 to 800 without losing legibility at the large sizes hero banners demand. Be Vietnam Pro handles sustained reading: product descriptions, spec copy, and review text, with enough openness between letters to stay comfortable across tablet widths. Kanit surfaces in label and badge contexts where geometric regularity and compact metrics matter more than warmth. The three-voice system is wider than most DTC brands maintain, but each register occupies a distinct size-weight range with little collision risk.

  Rounded corners stay controlled — {rounded.sm} on buttons and inputs, up to {rounded.md} on cards. No pill shapes anchor the primary action layer; the brand's authority comes from equipment precision. Orange (#ee9441) marks urgency: clearance badges, low-stock signals, time-limited promotions. Periwinkle (#7b8cde) and lavender (#a89cc8) tag sub-brand or discipline-specific lines, quiet accents that communicate product range without disrupting the primary teal identity. Because Pelican Sport operates under the Confluence Outdoor umbrella, the top navigation holds brand-switching context alongside product categories — an organizational complexity that shapes every layout decision from header height to mobile menu depth.

colors:
  primary: "#108474"
  primary-active: "#277158"
  primary-disabled: "#c1e6e6"
  forest-deep: "#0c5132"
  accent-chartreuse: "#d2de31"
  accent-amber: "#fbcd0a"
  accent-orange: "#ee9441"
  accent-periwinkle: "#7b8cde"
  accent-lavender: "#a89cc8"
  teal-muted: "#557777"
  teal-dark: "#3a4d4d"
  navy-deep: "#1a1a2e"
  blue-mid: "#1a4daf"
  ink: "#1a1a1a"
  body: "#555555"
  muted: "#6a7282"
  muted-soft: "#9ca3af"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  dark-canvas: "#0a0a0a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  alert-error: "#8b0000"

typography:
  display-xl:
    fontFamily: "'Geologica', 'Be Vietnam Pro', Arial, Helvetica, sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "'Geologica', 'Be Vietnam Pro', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Geologica', 'Be Vietnam Pro', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Be Vietnam Pro', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Be Vietnam Pro', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Be Vietnam Pro', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Be Vietnam Pro', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Be Vietnam Pro', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Kanit', 'Geologica', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Kanit', 'Geologica', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Kanit', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  label-upper:
    fontFamily: "'Kanit', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Be Vietnam Pro', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
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
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.on-dark}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-chartreuse:
    backgroundColor: "{colors.accent-chartreuse}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 40px
  promo-announcement-bar:
    backgroundColor: "{colors.accent-chartreuse}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    fontWeight: 600
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: 16px
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
    imageRounded: "{rounded.sm}"
  hero-banner:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    overlayColor: "{colors.ink}"
    overlayOpacity: 0.45
    paddingY: 64px
    minHeight: 480px
  category-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sale-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sport-tag:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  discipline-tag-periwinkle:
    backgroundColor: "{colors.accent-periwinkle}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    iconColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    typography: "{typography.body-md}"
  footer-dark:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.accent-chartreuse}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
  product-spec-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    labelColor: "{colors.muted}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    rowPadding: 10px 16px

## Components

### Buttons

**`button-primary`** — Renders in brand teal (#108474) with white uppercase Kanit text at 15px/600 weight and 0.5px tracking, giving it an equipment-manual register rather than a soft consumer tone. Fixed at 48px height with 28px horizontal padding and {rounded.sm} corners. Hover transitions to `button-primary-active` (#277158), deepening into forest green; the disabled state drains to pale teal `primary-disabled` (#c1e6e6) with muted gray text, clearly inactive without vanishing from the layout.

**`button-secondary`** — White fill with a 2px teal border and teal text, used alongside `button-primary` in two-action rows such as "Add to Cart" + "Find a Dealer". Shares the 48px height and uppercase Kanit typography of the primary so the two read as a matched pair without competing for the top position in the visual hierarchy.

**`button-ghost`** — Transparent background with a 2px white border and `on-dark` white text, reserved for placement over dark hero imagery and the near-black footer zone. The same uppercase Kanit metrics as `button-primary` preserve cross-context rhythm; this button should not appear on light backgrounds where it would disappear into the canvas.

**`button-chartreuse`** — Chartreuse (#d2de31) fill with ink (#1a1a1a) text, deployed for promotional events, seasonal sales, and "Shop the Sale" entry points. Its high-vis fill demands restraint — one instance per page section is the practical maximum before it degrades into visual noise competing with product photography.

### Text Input

**`text-input`** — White fill, 1px hairline border, 48px height, {rounded.sm}. On focus the border upgrades to 2px primary teal, providing a clear active indicator consistent with the primary action color system. Placeholder uses `muted-soft` (#9ca3af) at Be Vietnam Pro 16px/400 to match `body-md`, creating a natural transition between form context and surrounding page copy.

### Navigation

**`nav-bar`** — 72px tall, white background with a 1px hairline bottom border. Carries the Pelican/Confluence Outdoor lockup at left, core product category links in the center in `nav-link` (Be Vietnam Pro 15px/600), and utility icons — search, cart, account — at right. A collapsible mega-menu expands beneath with sub-brand switching rows, a structural necessity of the Confluence Outdoor multi-brand architecture that no single-brand site would need.

**`promo-announcement-bar`** — Chartreuse (#d2de31) bar at 40px height, pinned above the `nav-bar`. Carries promotional copy in `body-sm` at weight 600 with ink text so the high-contrast fill does not need the additional visual help of white-on-teal. Collapses entirely on mobile to reclaim vertical real estate, with its content surfaced in a dismissible sheet if the promotion is active.

### Product Card

**`product-card`** — White surface with a 1px soft hairline border and {rounded.sm} corners. Product image occupies the upper portion of the card with a matching {rounded.sm} crop. Title renders in `title-md` (Be Vietnam Pro 18px/600), price in `title-sm` (16px/600), and short descriptor or capacity spec in `caption` (13px/400 muted). Sport tags overlay the bottom-left of the image as `sport-tag` chips in primary teal; sale badges (`sale-badge`, orange #ee9441) pin to the image top-right corner so they are visible without the buyer entering the PDP.

### Hero Banner

**`hero-banner`** — Full-width, photography-backed, dark-overlaid section with `navy-deep` (#1a1a2e) as the fallback when images are unloaded or on slow connections. Overlay sits at 45% opacity to preserve mid-range image detail, particularly waterline and hull reflections. Headline uses `display-xl` (Geologica 56px/800), subline uses `body-md` (Be Vietnam Pro 16px/400) in `on-dark` white. The primary CTA is `button-primary` when the hero is dark-overlaid; `button-ghost` when placed over lighter images. Minimum height 480px desktop, 320px mobile.

### Badges and Tags

**`sport-tag`** — Primary teal fill, white uppercase Kanit 11px label used to mark paddle category directly on product card imagery: Kayak, SUP, Canoe, Pedal. **`discipline-tag-periwinkle`** — Periwinkle (#7b8cde) fill with the same `label-upper` type, used for sub-discipline or gear-type filters such as Recreational, Touring, Fishing, and Racing — a quiet signal that distinguishes activity segments within a single hull category. **`sale-badge`** — Orange (#ee9441) fill, white text, upper-right image corner pin. **`category-badge`** — Surface-soft (#f2f2f2) fill with body-gray text, for taxonomy labels in filter sidebars and breadcrumb trails.

### Search

**`search-bar`** — 44px height, hairline border, {rounded.sm}. Search icon in muted (#6a7282) at left interior; on focus, border upgrades to 2px primary teal and the icon shifts to `colors.primary`. Deployed in two contexts: as a slide-down overlay triggered from the nav-bar search icon on desktop, and as a full-width standalone module on collection/catalog page headers. Placeholder reads in `muted-soft` at `body-md` scale.

### Footer

**`footer-dark`** — Near-black (#0a0a0a) background with a 3px primary teal top border as the sole brand signal entering the dark zone. Heading columns use `title-sm` (Be Vietnam Pro 16px/600) in `on-dark` white; link items use `body-sm` (14px/400) in `muted-soft` gray with hover shifting to chartreuse (#d2de31), which reads warmly against the near-black field without requiring a color shift that would feel like an error state. Bottom row carries legal, warranty, and Confluence Outdoor attribution in `caption` size. Dealer-locator and manual-download links live here because equipment buyers use them long after purchase.

### Product Spec Table

**`product-spec-table`** — Surface-soft (#f2f2f2) background, {rounded.sm}, 1px hairline internal row dividers. Label column uses `caption` (Be Vietnam Pro 13px/400) in muted gray; value column uses `body-sm` (14px/400) in ink. Common rows for kayak PDPs: Length, Width, Weight, Weight Capacity, Hull Material, Cockpit Type, Seating Capacity. On mobile the table spans full width with condensed row padding; it does not collapse into an accordion — spec data is load-bearing for buyers comparing hull dimensions.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; promo bar hidden; nav collapses to hamburger + cart icon; hero 320px min-height; product grid 1-up or 2-up; footer columns stack vertically in accordion groups |
| Tablet | 744–1128px | 2–3 column product grid; nav shows logo + hamburger for secondary links; hero 420px; sidebar filters collapse into horizontal top filter bar |
| Desktop | 1128–1440px | Full nav with expanded mega-menu; 3–4 column product grid; sticky add-to-cart bar on PDP; hero 480px minimum |
| Wide | > 1440px | Content max-width 1440px, centered; hero spans full bleed edge-to-edge; product grid stays 4-up with larger card proportions |

### Touch Targets

- All interactive elements minimum 44×44px on mobile
- Nav hamburger zone expands to 48×48px via padding
- Filter checkboxes expand to 40px row height in the mobile filter sheet
- Add-to-cart button fixed at bottom of viewport on mobile PDP, full-width, 56px height
- Card tap targets cover the full card face, not just title text
- Spec table rows minimum 44px height on mobile for accessible tap selection

### Collapsing Strategy

- Promo announcement bar: hidden below 744px; active promotions surface in a dismissible banner sheet triggered on first scroll
- Mega-menu: replaced by a slide-in drawer on mobile with back-navigation breadcrumb supporting sub-brand switching
- Spec table: horizontal scroll on mobile below 400px when content exceeds viewport; column widths do not shrink below readable minimum
- Filter sidebar: collapses into a bottom sheet modal triggered by a sticky "Filter & Sort" bar on mobile catalog pages
- Footer columns: 2-up on tablet, 1-up accordion on mobile with expand/collapse per column group; always-visible legal row at bottom

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; mobile browser chrome tint is unknown — primary teal (#108474) assumed as a reasonable default
- Exact per-element font assignment (which pages lead with Geologica vs. Be Vietnam Pro) could not be confirmed from extracted stacks alone; assignment above reflects visual inference from brand register
- Baskerville appears in the font stack but its use context is unclear — likely editorial or blog pages, possibly a sub-brand; excluded from core component spec until confirmed
- Inter and Open Sans appear in the extracted stack but their role (system fallback, embedded widget, third-party app) is ambiguous; not incorporated into token definitions
- JudgemeIcons and JudgemeStar confirm the Judge.me review app is installed; star rating colors, badge layout, and widget styling are governed by that app and may not match brand tokens
- Exact button and card border-radius values not confirmed from CSS extraction; {rounded.sm} (8px) and {rounded.md} (12px) are inferred from visual register
- Hover and transition animation timing not extractable from static hints; 150ms ease-in-out assumed as default throughout
- No drop-shadow tokens defined — border-only card treatment assumed until elevation values are confirmed from live inspection
- The roles of #a89cc8 (lavender), #3ed660 (bright green), and #006400 (deep green) in the extracted palette are ambiguous; likely seasonal or promotional accent use not captured in the core component spec
- Amber (#fbcd0a) appears in the extracted palette but its precise UI placement (badge fill, promo label, icon accent) was not determinable without live DOM inspection
