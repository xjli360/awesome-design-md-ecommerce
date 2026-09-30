---
version: alpha
name: "Blue Kazoo"
source_url: "https://bluekazoo.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Puzzle brands usually reach for primary-school primaries; Blue Kazoo names itself after its chosen voltage and bets on the cooler end of the spectrum — a saturated cobalt that distinguishes it from washed periwinkle lifestyle brands and flat-navy corporate ones. That blue runs through every primary CTA, category tab, and branded badge on a white-first canvas that surrenders the stage to illustrated puzzle photography. Where the primary is assertive, the surrounding palette is warm-complementary: an orange-amber accent fires on promotional tags and sale stickers, while a lemon-yellow marks theme and age-range chips so a shopper can parse puzzle type at a glance without reading copy. Typography reaches for a rounded geometric sans — the category sweet spot that reads friendly without tipping into juvenile — set at generous line heights suited to shoppers scanning piece-counts and difficulty ratings on small screens. Product cards float on {colors.surface-card} with {rounded.lg} corners and a hairline border in {colors.hairline}, giving the impression of a gallery wall rather than a warehouse shelf; each card leads with a single full-bleed puzzle image, then difficulty and size-spec chips running below the title. Rounded pill shapes ({rounded.full}) appear on filter chips and category navigation, reinforcing a soft-edged, family-inclusive tone without abandoning the premium positioning that adult puzzle collectors expect. Primary calls-to-action use a filled {rounded.full} pill; secondary actions sit in a ghost variant carrying {colors.primary} as stroke and label, keeping both options light against the white canvas. The overall grid is restrained — base padding at {spacing.base} on mobile, column gutters widening at {spacing.lg} on tablet — letting the puzzle art carry visual weight across all breakpoints.

colors:
  primary: "#1A5CCC"
  primary-active: "#1347A8"
  primary-disabled: "#A8C4F0"
  accent: "#FF8C38"
  highlight: "#FFC926"
  ink: "#1A1F36"
  body: "#3D4163"
  muted: "#6B7099"
  hairline: "#D4DAEA"
  hairline-soft: "#EBF0FA"
  canvas: "#FFFFFF"
  surface-soft: "#F4F7FF"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  badge-easy: "#3DBF6E"
  badge-hard: "#D94040"

typography:
  display-xl:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  badge-label:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  piece-count:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
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
    padding: 14px 28px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
    padding: 12px 26px
    height: 48px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 38px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    border: "1px solid {colors.hairline}"
    imageRatio: "1/1"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.md}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.xl}"
  difficulty-badge:
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    easyBackgroundColor: "{colors.badge-easy}"
    easyTextColor: "{colors.on-primary}"
    hardBackgroundColor: "{colors.badge-hard}"
    hardTextColor: "{colors.on-primary}"
  piece-count-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.piece-count}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "4px 12px"
  category-filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "8px 16px"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorderColor: "{colors.primary}"
  promo-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"
  new-arrival-sticker:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    padding: 12px 20px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Filled cobalt pill (`{rounded.full}`) at 48px tall using `{typography.button-md}` at weight 700 with `{colors.on-primary}` text. Hover steps the background to `{colors.primary-active}`; disabled state flattens to `{colors.primary-disabled}` with no pointer events.

**`button-secondary`** — Ghost variant with a 2px stroke in `{colors.primary}` and matching label on a white fill. Same pill radius and 48px height as `button-primary`, clearly subordinate without breaking visual pairing. Used for "View Details" alongside a primary "Add to Cart."

**`button-sm`** — Compact cobalt pill at 38px for card-level actions within the product grid or inline upsell modules. Shares `{rounded.full}` with larger siblings for shape consistency across scales.

### Text Inputs & Search
**`text-input`** — Standard form field with `{rounded.md}` corners and a `{colors.hairline}` border that transitions to `{colors.primary}` on focus. Placeholder sits in `{colors.muted}` to contrast white fill without competing with field labels.

**`search-bar`** — Full-pill field on `{colors.surface-soft}` for placement in the nav or as a catalog header. Focus switches the border to `{colors.primary}`, keeping the active state obvious without a drop shadow. Icon sits left-inset at 20px.

### Navigation
**`nav-bar`** — White bar at 64px tall with a `{colors.hairline}` bottom border. Brand logo anchors the left; category links in `{typography.nav-link}` at weight 700 run center or right; cart icon and search icon close the right side. On mobile, links collapse to a hamburger drawer that slides in from left.

### Product Cards
**`product-card`** — Square-ratio (1:1) puzzle image dominates the card face. Title in `{typography.title-md}` and price in `{typography.title-sm}` sit below with `{spacing.md}` padding on all sides. `{rounded.lg}` corners and a `{colors.hairline}` border give each card gallery-wall separation from the white canvas. A `difficulty-badge` overlays the image at top-left; a `piece-count-chip` appears inline below the title. A `promo-badge` or `new-arrival-sticker` occupies the top-right of the image when applicable.

### Badges & Chips
**`difficulty-badge`** — Uppercase `{typography.badge-label}` with `{rounded.xs}` corners. Green (`{colors.badge-easy}`) for beginner puzzles; red (`{colors.badge-hard}`) for expert. Display-only; nearest tappable area is the card itself.

**`piece-count-chip`** — Pill chip with `{colors.surface-soft}` fill and `{colors.primary}` text surfacing piece count as a scannable spec (e.g., "500 Pieces"). Groups naturally with theme or format chips beneath the product title.

**`category-filter-chip`** — Outlined pill for the catalog filter strip. Default: white fill, `{colors.hairline}` border, `{colors.body}` label. Active: `{colors.primary}` fill with `{colors.on-primary}` text — the same blue token as `button-primary`, so active filters read as brand-owned actions rather than passive states.

**`promo-badge`** — Warm orange (`{colors.accent}`) filled badge for sale or bundle promotions. Provides contrast against white card backgrounds and dark puzzle imagery alike. Top-right image placement keeps it out of title and piece-count reading zone.

**`new-arrival-sticker`** — Lemon-yellow (`{colors.highlight}`) pill that flags new SKUs without urgency-coded red. Text stays `{colors.ink}` for legibility on the pale fill.

### Hero Banner
**`hero-banner`** — Full-width section on `{colors.surface-soft}` with a display headline in `{typography.display-xl}` and supporting body in `{typography.body-md}`. A `button-primary` CTA anchors below the body copy. On desktop the layout runs as a two-column split — text left, puzzle lifestyle photography right. On mobile it stacks vertically with image below copy and full-width button.

### Footer
**`footer`** — Dark `{colors.ink}` background with `{colors.canvas}` body text and `{colors.hairline-soft}` link color. Desktop runs three link columns; mobile collapses to stacked accordion sections. Brand logo appears reversed to white at the top of the block.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, nav collapses to hamburger drawer, hero stacks vertically, filter chips scroll horizontally in a single row above grid |
| Tablet | 744–1128px | Two-column product grid, nav links visible, hero runs two-column at reduced display type, filter chip strip stays horizontal |
| Desktop | 1128–1440px | Three- or four-column product grid, full nav visible, filter rail appears as left sidebar with vertical chip list |
| Wide | > 1440px | Grid caps at four columns, content max-width ~1280px centered with increased lateral padding at `{spacing.section}` |

### Touch Targets
- All interactive chips and buttons minimum 44px tall
- `button-primary` and `button-secondary` at 48px exceed minimum comfortably
- `button-sm` at 38px — pad card tap zone to 44px via surrounding anchor
- Difficulty badges are display-only; card itself is the interactive surface
- Nav hamburger icon minimum 44×44px tap area on mobile

### Collapsing Strategy
- Category filter chips move from vertical left sidebar (desktop) to a horizontally scrollable pill strip pinned above the product grid (mobile/tablet)
- Hero two-column layout collapses to full-width stacked on mobile; image drops below headline copy to keep CTA above the fold
- Footer three-column link layout stacks to single column with accordion expand/collapse on mobile
- Nav links hide behind hamburger at < 744px; logo and cart icon always visible in the bar

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted — the site appears to load palette tokens via JavaScript or has anti-bot protections in place; all color values above are informed estimates based on the brand name ("Blue Kazoo" strongly implies a blue primary) and puzzle-category DTC conventions, not live data
- No font families were extracted — the typeface stack (Nunito/Poppins) is a category-appropriate assumption; actual brand typeface may differ materially
- No meta theme-color found, so mobile browser chrome accent is unknown
- Shopify platform status unconfirmed (platform-shopify: False) — cart, checkout, and collection-page component patterns may follow a different e-commerce framework
- Difficulty tier labeling (e.g., Easy / Medium / Hard vs. numeric ratings) not confirmed from live data
- Exact piece-count SKU tiers (100 / 300 / 500 / 1000 / 2000 / 5000) not verified
- Hover, focus-ring, and motion tokens (transition duration, easing curves) not extractable without live browser interaction
- Dark mode support status unknown
- Custom illustration or icon style not verified; puzzle-category brands often use hand-drawn motifs that would materially affect badge and empty-state design
