---
version: alpha
name: "Tudor"
source_url: "https://www.tudorwatch.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The heraldic five-petaled rose at Tudor's center hasn't changed since 1952 — a deliberate anachronism that functions as the brand's entire visual argument. Every primary CTA, the shield-shaped logo frame, and the signature strap fabric inherit a single deep crimson (#CC0000) that reads as institutional rather than aggressive against expansive black-and-white photography. Tudor occupies a studied position between Swiss watchmaking heritage and accessible precision, marketed through a "Born to Dare" campaign that favors gritty adventure imagery — polar expeditions, saturation dives — over the drawing-room settings common among horological neighbors on the prestige ladder. The type system reinforces this duality: headline scales run in architecturally spaced uppercase that signals military brevity, while body copy settles into a clean humanist sans at modest weight. Product cards use high-aspect-ratio portrait crops to show the full watch face and bracelet without truncation, giving the wrist context that close-cropped dial shots deny. Navigation organizes by collection line — Black Bay, Pelagos, Royal, Ranger, 1926, Glamour Double Date — each carrying its own sub-palette of dial variants (black, blue, burgundy, silver) that coexist within the master crimson-black-white system. Hierarchy is enforced almost entirely by scale and padding; borders are sparse and hairline-weight where they appear. Buttons are sharp-cornered or carry only a vestigial radius ({rounded.xs}), never pill-shaped — a deliberate signal of engineering precision over lifestyle-brand warmth. Product detail pages organize technical specifications in two-column definition tables with tabular-figure numerals, nodding to instrument-panel legibility. The sole recurring decorative element is the rose badge itself, rendered in #CC0000 at every scale from 16px favicon to 120px embossed PDP header.

colors:
  primary: "#CC0000"
  primary-active: "#A30000"
  primary-disabled: "#E89999"
  ink: "#0A0A0A"
  body: "#2B2B2B"
  muted: "#717171"
  hairline: "#D4D4D4"
  hairline-soft: "#EBEBEB"
  canvas: "#FFFFFF"
  surface-soft: "#F4F4F4"
  surface-card: "#FFFFFF"
  surface-dark: "#111111"
  surface-dark-mid: "#1E1E1E"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  gold-accent: "#B8960C"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.07
    letterSpacing: 0.04em
    textTransform: uppercase
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.14
    letterSpacing: 0.03em
    textTransform: uppercase
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.05em
    textTransform: uppercase
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.01em
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.10em
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.04em
  spec-value:
    fontFamily: "'Helvetica Neue', Helvetica, 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0.02em
  collection-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.18em
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.10em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.10em
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
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
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.on-dark}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "0"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    padding: "{spacing.md} {spacing.base}"
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "none"
    height: 48px
    padding: "{spacing.md} {spacing.lg}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "none"
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.xl} {spacing.xxl}"
    borderTop: "1px solid {colors.hairline}"
    shadowY: "8px"
    shadowBlur: "24px"
    shadowColor: "rgba(0,0,0,0.08)"
  collection-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    activeIndicator: "2px solid {colors.primary}"
    typography: "{typography.nav-link}"
    height: 44px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    padding: "{spacing.lg}"
    hoverScale: 1.03
  product-card-eyebrow:
    typography: "{typography.collection-label}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xs}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  hero-fullbleed:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: "100vh"
    overlay: "linear-gradient(to bottom, transparent 40%, rgba(0,0,0,0.65) 100%)"
  hero-eyebrow:
    typography: "{typography.collection-label}"
    textColor: "{colors.primary}"
    marginBottom: "{spacing.sm}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  tudor-rose-badge:
    color: "{colors.primary}"
    colorOnDark: "{colors.on-dark}"
    sizes: "16px favicon / 32px nav / 64px PDP header / 120px embossed hero"
    usage: "standalone SVG heraldic rose — never recolored outside brand red or white-on-dark"
  spec-table:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rowPadding: "{spacing.md} {spacing.base}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.spec-value}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rowSeparator: "1px solid {colors.hairline-soft}"
  material-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.gold-accent}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  campaign-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 480px
    textMaxWidth: 480px
    padding: "{spacing.section} 0"
  boutique-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    addressTypography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Flat crimson block (`{colors.primary}`, #CC0000) at 48px tall, zero border radius, uppercase tracking at 0.12em. Hover transitions to `{colors.primary-active}` (#A30000) with no shape change. Disabled state uses `{colors.primary-disabled}` — a pale wash that signals inactivity without the bleed of an opacity trick. Used exclusively for high-commitment actions: "Discover", "Book an Appointment", "Buy Now".

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` perimeter and matching uppercase tracking. The `button-secondary-dark` variant inverts both border and type to `{colors.on-dark}` for use over dark photography. Vertical padding mirrors the primary so mixed-button rows stay aligned without explicit height-matching CSS.

**`button-ghost`** — Underline-only text link at `{typography.button-sm}` scale. Used for soft navigational nudges ("See All Models", "View Collection") in contexts where a bordered button would add visual weight the section doesn't need.

### Navigation

**`nav-bar`** — 72px fixed header on `{colors.canvas}` with a 1px `{colors.hairline}` bottom border. The Tudor heraldic rose anchors the left; collection links (Black Bay, Pelagos, Royal, Ranger, 1926, Glamour Double Date) span center in `{typography.nav-link}` uppercase. Utility icons (search, boutique locator, account) sit right. A `nav-bar-dark` variant activates over full-bleed heroes — identical layout, palette swapped to `{colors.surface-dark}` / `{colors.on-dark}`, border suppressed.

**`nav-mega-menu`** — Full-viewport-width panel that drops on hover below the fixed bar. Left column: collection still image. Center column: model-name list in `{typography.title-sm}`. Right column: editorial campaign still. No rounded corners, no drop shadow beyond a subtle 8px/24px box-shadow; separation is structural, not decorative.

**`collection-strip`** — A secondary 44px horizontal strip beneath the main nav on collection landing pages. Active segment carries a 2px `{colors.primary}` bottom indicator. Scrolls horizontally on mobile without a scrollbar track.

### Product Card

**`product-card`** — Portrait-aspect (3:4) imagery on `{colors.surface-soft}`, sharp corners, no shadow. Eyebrow in `{typography.collection-label}` / `{colors.muted}` (e.g., "BLACK BAY 58") precedes the model name in `{typography.title-md}` and price in `{typography.body-md}`. Hover applies a 1.03 scale transform to the image only — the text block stays anchored. No quick-add drawer or hover overlay; all purchase intent routes through the detail page.

### Hero

**`hero-fullbleed`** — Full-viewport photographic hero with a gradient overlay (transparent to rgba(0,0,0,0.65)) over `{colors.surface-dark}`. The eyebrow line uses `{typography.collection-label}` in `{colors.primary}` — the sole instance of red text in the composition. Headline uses `{typography.display-xl}` in `{colors.on-dark}`. CTA pair of `button-primary` + `button-secondary-dark` sits left-aligned below the headline with `{spacing.sm}` gap between buttons.

### Spec Table

**`spec-table`** — Two-column definition table for PDP technical panels: Movement, Case, Bracelet, Water Resistance. Label column at `{typography.caption}` / `{colors.muted}`; value column at `{typography.spec-value}` / `{colors.ink}`. Rows separated by 1px `{colors.hairline-soft}` lines. No alternating background. The `spec-value` font stack includes `'Courier New'` fallback to ensure numeric specs (e.g., "39 mm", "200 m / 660 ft") align in tabular columns on less capable rendering environments.

### Campaign Banner

**`campaign-banner`** — Minimum 480px-tall editorial section that appears between collection grids as a rhythm break. Dark photographic background (`{colors.surface-dark}`) with headline in `{typography.display-md}` and body in `{typography.body-md}` set over maximum 480px text column. Carries "Born to Dare" campaign imagery and a paired CTA row. Padding uses `{spacing.section}` top/bottom to give it visual breathing room distinct from the surrounding product grids.

### Tudor Rose Badge

**`tudor-rose-badge`** — The SVG heraldic five-petaled rose rendered in `{colors.primary}` (#CC0000) at multiple fixed sizes: 16px favicon, 32px in-nav, 64px standalone PDP header, 120px embossed hero element. On dark surfaces it switches to `{colors.on-dark}`. Never rendered in any intermediate color or with opacity reduction — the rose is either full-crimson or full-white.

### Material Tag

**`material-tag`** — Small pill at `{typography.caption}` scale used in product configurator and comparison modules to identify case/bracelet material variants (Steel, Yellow Gold, Two-Tone). `{colors.gold-accent}` (#B8960C) is applied as an accent dot or left border for gold-material options, distinguishing them from the main crimson brand system without introducing a competing dominant hue.

### Boutique Card

**`boutique-card`** — Used in the store-locator grid alongside a full-bleed map embed on desktop. White card with 1px `{colors.hairline}` border, `{spacing.lg}` padding, no shadow. Boutique name in `{typography.title-md}`, address block in `{typography.body-sm}`, and a `button-ghost` "Get Directions" link at bottom. On mobile the card grid stacks above a reduced-height map embed.

### Footer

**`footer`** — `{colors.surface-dark}` background with a 3px `{colors.primary}` top border — the last crimson accent before page end. Four columns: Collections, Brand (About Tudor, History, Born to Dare), Services (After-Sales, Guarantee, Boutique Locator), Social/Newsletter. Column headings in `{typography.title-sm}` uppercase; links in `{typography.body-sm}`. Legal links and locale selector run in a `{colors.surface-dark-mid}` strip below the primary footer grid.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to Tudor rose + hamburger drawer; hero headline scales down to `display-md`; `collection-strip` scrolls horizontally without indicator; spec-table remains 2-col with horizontal overflow scroll |
| Tablet | 744–1128px | 2-column product grid; nav links visible in full but mega-menu simplified to single-column list; hero CTAs stack vertically; campaign-banner stacks image above copy |
| Desktop | 1128–1440px | 3-column product grid; full mega-menu on hover; campaign-banner splits 50/50; spec-table tab panel appears as persistent side rail on PDP |
| Wide | > 1440px | Content constrained to ~1320px centered; hero photography bleeds full-width behind constrained text column; 4-column product grid on collection pages; footer 5-column at this breakpoint |

### Touch Targets

- All interactive elements minimum 44×44px on mobile
- Nav hamburger expands hit area to 48×48px
- `product-card` full tile is tappable — no separate affordance zone
- `spec-table` rows do not need independent tap targets; parent tab-panel handles scroll
- Boutique map pins 44px diameter with tooltip on first tap, navigation on second

### Collapsing Strategy

- Navigation collapses to a full-screen right-to-left slide-in drawer; collection links become large accordion items revealing model-name lists
- `nav-mega-menu` is entirely absent on mobile and tablet; all sub-navigation lives inside the drawer accordion
- `campaign-banner` image moves above copy block on mobile; minimum height reduces to 320px; text padding falls back to `{spacing.xl}`
- `footer` 4-column grid collapses to single-column accordion with `{typography.title-sm}` headings as toggle triggers
- `collection-strip` converts from underlined tabs to a no-scrollbar horizontal scroll container with touch momentum

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extractable — the site returned HTTP 403 Access Denied; all palette values above are approximations based on widely documented Tudor brand identity. The Tudor shield red is the primary public-facing identifier but the precise value (#CC0000 used here) should be confirmed against the live site CSS
- No font stacks were extracted; Tudor may use a proprietary or licensed typeface not identified here — Helvetica Neue is the closest documented match from marketing material analysis but should be verified
- Button corner radius is unconfirmed; `{rounded.none}` is inferred from the brand's engineering-precision posture; some secondary UI elements may carry `{rounded.xs}` or `{rounded.sm}`
- Section padding, grid gutter widths, and column counts are estimated from brand aesthetic reference, not extracted computed CSS
- Animation timing and easing (mega-menu open, hover transitions, hero parallax) are entirely absent from extraction
- Dark-mode OS-level support is unknown; the brand's heavy dark-surface use is intentional art direction, but whether a `prefers-color-scheme: dark` media query is wired up is unconfirmed
- Gold accent (#B8960C) is an approximation for yellow-gold material callouts; Tudor's specific gold dial/case photography color may differ
- Price display locale (CHF vs. local currency, VAT inclusion, installment options) could not be verified
- Whether Tudor uses a custom typeface (similar to Rolex's proprietary type) or a licensed geometric sans is unknown without font file inspection
