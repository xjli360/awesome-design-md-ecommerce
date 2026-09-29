---
version: alpha
name: "Kenmore Stamp Company"
source_url: "https://www.kenmorestamp.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Perforations, watermarks, and centering grades — Kenmore Stamp Company speaks the dense vocabulary of serious philately through a near-black #313131 that functions simultaneously as the primary action color, body text, and the visual weight of a catalog printed on quality stock. The site appears to load behind anti-bot protection, so only a single extracted color survived scraping; the full palette below is therefore a minimal, principled derivation from that one anchor rather than a confirmed brand system. What the anchor tells you: this is a business that does not reach for vivid color to sell — dark charcoal doing the work of red, teal, or orange in most retail contexts signals confidence in the product catalog itself. Type runs entirely on system stacks — Arial and fallbacks — suggesting either a legacy CMS or a deliberate rejection of web-font overhead in favor of fast catalog-page loads, consistent with a mail-order heritage that pre-dates e-commerce. Rounded values trend toward zero; the mental model is ledger lines and stamp grids, not rounded pill cards. The spacing system is generous at section level to accommodate philatelic imagery — perforation scans, certificate reproductions, country lot tables — while staying compact in the data-dense grid cells that list face values, grades, and set identifiers. Buttons carry the same charcoal as the brand anchor on a white canvas, creating a two-tone vocabulary that echoes black printer's ink on white paper: the aesthetic of the philatelic auction catalog translated directly into the purchase flow.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#9a9a9a"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#767676"
  hairline: "#d6d6d6"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-warm: "#faf9f7"
  on-primary: "#ffffff"
  accent-red: "#8b1a1a"
  accent-red-soft: "#c0392b"
  badge-new: "#2c5f2e"
  badge-sale: "#8b1a1a"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  catalog-id:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  price-display:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  lot-label:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 10px
  xl: 16px
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
    padding: 10px 20px
    height: 40px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.accent-red-soft}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 48px
    borderBottom: none
  nav-bar-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    height: 36px
    borderBottom: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 38px
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    height: 38px
  search-submit:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 38px
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
    imageAspectRatio: "1/1"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    idTypography: "{typography.catalog-id}"
    gap: "{spacing.xs}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 6px rgba(0,0,0,0.12)"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.lot-label}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.lot-label}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.xl}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
  category-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.base} {spacing.lg}"
    titleTypography: "{typography.display-sm}"
  lot-table-row:
    backgroundColor: "{colors.canvas}"
    altBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} {spacing.md}"
    idTypography: "{typography.catalog-id}"
    priceTypography: "{typography.title-sm}"
  lot-table-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.lot-label}"
    padding: "{spacing.sm} {spacing.md}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "›"
    gap: "{spacing.xs}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 32px
    width: 32px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "#cccccc"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderTop: "3px solid {colors.accent-red}"
  country-section-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderLeft: "3px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
    marginBottom: "{spacing.sm}"

## Components

### Buttons

**`button-primary`** — Solid #313131 charcoal fill with white type at 14px bold, 40px tall, nearly square corners (`{rounded.xs}` = 2px). The primary action reads as a printer's block stamp rather than a soft CTA: authoritative, no gradient, no shadow. Hover darkens to `{colors.primary-active}` (#1a1a1a); disabled state uses a mid-gray `{colors.primary-disabled}` with white text maintained.

**`button-secondary`** — White canvas with charcoal border and charcoal text, matching the primary's 40px height and 2px radius. On hover the fill shifts to `{colors.surface-soft}` with a slightly darker border, keeping the ink-on-paper inversion legible.

**`search-submit`** — The one component where `{colors.accent-red}` (#8b1a1a) appears as a fill, aligning the search trigger with the visual tradition of red-ink philatelic pricing stamps. Sits flush against the search input field at the same 38px height.

### Navigation

**`nav-bar`** — Full-width charcoal bar at 48px, white nav-link text at 14px bold. No logo type treatment extracted; expect a wordmark or small emblem at left. A secondary bar below (`nav-bar-secondary`) carries department links — country categories, approval selections, mint sets — on a light `{colors.surface-soft}` background with a `{colors.hairline}` bottom rule.

### Cards and Catalog Grid

**`product-card`** — Minimal border box with 1px `{colors.hairline}` rule and near-zero rounding. Stamp images render square at a 1:1 aspect. Below the image: the Scott catalog ID in `{typography.catalog-id}` (monospace, tracking 0.5px), then the lot description in `{typography.body-sm}`, then the price in `{typography.price-display}` at 18px bold. On hover, the border upgrades to charcoal with a light shadow — the card "lifts" without any radius change.

**`lot-table-row`** — Many catalog pages use a tabular rather than card layout. Alternating `{colors.canvas}` / `{colors.surface-soft}` rows with a `{colors.hairline-soft}` bottom rule; the ID column uses monospace `{typography.catalog-id}`, the price column uses `{typography.title-sm}` bold. The `lot-table-header` row runs full charcoal with white uppercase labels at 11px tracking 0.8px.

### Badges

**`badge-sale`** and **`badge-new`** — Hard-edged rectangular chips with no border-radius, matching the perforation-cut aesthetic of the product. Sale uses deep philatelic red `{colors.badge-sale}` (#8b1a1a); new-arrival uses deep collector green `{colors.badge-new}` (#2c5f2e). Both render 11px uppercase bold text with 2px vertical / 6px horizontal padding.

### Layout Sections

**`hero`** — Full-bleed charcoal panel with white headline (`{typography.display-xl}`) and body copy. No gradient, no image overlay in the extracted state — pure typographic confidence. Padding is generous at `{spacing.xxl}` top/bottom.

**`category-banner`** — Warm off-white `{colors.surface-warm}` header with a 2px charcoal bottom border acting as a section underline. Country or topic name renders at `{typography.display-sm}`. Used at the top of each country or topical category page.

**`country-section-header`** — Within a multi-country listing page, a left-bordered heading (`3px solid {colors.primary}`) in `{typography.title-md}` on `{colors.surface-soft}` separates each country's lot block. The border-left acts as a visual tab marker.

**`footer`** — Charcoal fill with a 3px accent-red top border, white body text, and medium-gray link color (#cccccc) to maintain hierarchy without full brightness. Carries mailing address, approval service links, and collector resource navigation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; lot tables scroll horizontally or collapse to card stacks; nav bar collapses to hamburger; search bar moves to full-width row below nav |
| Tablet | 744–1128px | Two-column product grid; secondary nav fits in horizontal scroll strip; category banners full-width |
| Desktop | 1128–1440px | Three- or four-column product grid; full secondary nav visible; lot tables full-width with all columns |
| Wide | > 1440px | Grid expands to five columns maximum; content centered with max-width ~1400px; side gutters fill with canvas |

### Touch Targets

- All buttons minimum 40px tall; search submit and primary CTA preferably 44px on mobile
- Lot table rows minimum 44px tall on mobile to support tap-to-expand detail
- Pagination controls minimum 44×44px touch area even when visual size is 32px
- Nav links in collapsed menu minimum 48px row height

### Collapsing Strategy

- Secondary nav category links: visible full strip on desktop/tablet; hamburger-or-select dropdown on mobile
- Lot tables: prefer horizontal scroll container over collapsing columns; pin the Scott ID and price columns
- Country section headers: retain left-border style at all breakpoints; reduce padding at mobile
- Hero padding scales from `{spacing.xxl}` desktop to `{spacing.lg}` mobile; headline drops from display-xl to display-md

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extracted — the site returned a Cloudflare "Just a moment…" challenge page, blocking full CSS/token scraping. The entire color palette beyond #313131 is inferred from philatelic industry conventions and the single anchor, not confirmed brand values.
- No custom web fonts detected; all typography stacks are system sans-serif. It is unknown whether the live site loads a custom font via JS after bot-check, or genuinely uses Arial/system fonts throughout.
- No meta theme-color, no Open Graph color, no extracted button states, no confirmed link color.
- Accent red (#8b1a1a, #c0392b) and badge green (#2c5f2e) are designer inference for a traditional philatelic context — not extracted.
- Logo treatment, wordmark weight, and any brand illustration or iconography system are completely unknown.
- Checkout, account, and approval-service flows are unscraped; component specs for those surfaces are missing entirely.
- Whether the site uses a table-first catalog layout or a card grid as primary browse UI could not be confirmed from the blocked page load.
