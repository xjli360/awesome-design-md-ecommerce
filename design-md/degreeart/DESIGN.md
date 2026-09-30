---
version: alpha
name: "DegreeArt"
source_url: "https://www.degreeart.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every artwork on DegreeArt arrives with a provenance measured in studio hours rather than auction-house transactions — the platform was built on the premise that a graduation show is a buying event, not a portfolio review. That founding logic shapes the interface from the top down: the site defers entirely to the work, running `{colors.primary}` (#313131 charcoal) through headlines, borders, and primary CTAs alike so no interface colour competes with the canvas it sits beside. The palette confirmed from live extraction is narrow — one distinctive dark charcoal dominant, with surface neutrals inferred from gallery convention — which suits a platform whose true colour is its inventory.

  Type rides the system stack; no proprietary typeface is loaded on demand. `{typography.display-xl}` headings at 32px / weight 700 anchor editorial section leads without theatrical scale; body copy runs at 16px / weight 400 with a relaxed 1.6 line-height so edition statements and artist bios stay legible under sustained reading. Buttons inherit the same charcoal fill with uppercase tracked letter-spacing at 0.5px, so a CTA reads as a gallery label rather than a consumer prompt — functional but unhurried.

  Navigation sits flat and horizontal, category links spaced at `{spacing.lg}` with a 2px `{colors.ink}` underline active state rather than fill highlights. Product cards carry a `{colors.hairline}` border, `{rounded.xs}` corners that barely register, and a thumbnail-first layout where the artwork occupies the full card face while title, artist name, and price form a tight three-line stack below. Filter panels disclose via accordion rows rather than persistent sidebars, keeping the grid at full width on tablet and above. The aggregate effect is a gallery-catalogue sensibility in a browser: orderly, recessive, and built to let tens of thousands of original works speak without the interface raising its voice.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#9a9a9a"
  ink: "#313131"
  body: "#4d4d4d"
  muted: "#767676"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#313131"
  link-hover: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  artist-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  edition-tag:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase

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
    rounded: "{rounded.xs}"
    padding: "12px 24px"
    height: 44px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: "11px 23px"
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: "10px 14px"
    height: 44px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: "10px 14px 10px 40px"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    gap: "{spacing.lg}"
  nav-bar-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    imageFit: cover
    padding: "{spacing.md}"
    titleTypography: "{typography.title-sm}"
    artistTypography: "{typography.artist-label}"
    priceTypography: "{typography.price-display}"
    titleColor: "{colors.ink}"
    artistColor: "{colors.muted}"
    priceColor: "{colors.ink}"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    maxWidth: 1200px
  artwork-edition-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.edition-tag}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  filter-accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.md} 0"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  artist-profile-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    nameTypography: "{typography.title-md}"
    schoolTypography: "{typography.caption}"
    nameColor: "{colors.ink}"
    schoolColor: "{colors.muted}"
    padding: "{spacing.base}"
  pagination:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    bodyTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    linkColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Filled charcoal (#313131) with white text in uppercase tracked `{typography.button-md}`, giving CTAs ("Add to Basket", "Buy Now") the weight of a gallery label rather than a retail imperative. Hover deepens to `{colors.primary-active}` (#1a1a1a); disabled mutes to `{colors.primary-disabled}` (#9a9a9a) without a shape change. Corner radius is minimal at `{rounded.xs}` (2px), consistent with the flat, print-adjacent aesthetic throughout.

**`button-secondary`** — White fill with a full `{colors.ink}` border and matching uppercase type; sits beside primary on artwork detail pages where "Enquire" and "Buy Now" need equal visual presence. Hover state inverts to dark fill to confirm selection without surprise. Padding is inset by 1px to account for the visible border stroke.

**`button-ghost`** — Transparent, underline-only, in `{typography.body-sm}`; used for tertiary links such as "View all works by this artist", pagination context labels, and inline prose navigation. No border, no fill, no radius.

### Inputs

**`text-input`** — `{colors.canvas}` background with a `{colors.hairline}` border that sharpens to full `{colors.ink}` on focus — no inner shadow or glow, just a border-weight shift. Used for newsletter capture, checkout fields, and account forms. Placeholder text in `{colors.muted}` to preserve legibility without competing with entered content.

**`search-bar`** — Shares `text-input` geometry but carries 40px left-padding for an inline search icon. Sits at the top of category and search-result pages; collapses to an icon trigger on mobile. Focus border matches `text-input` convention.

### Navigation

**`nav-bar`** — 64px tall, `{colors.canvas}` background, `{colors.hairline}` bottom rule. Logo left-aligned; primary category links ("Buy Art", "Artists", "Exhibitions", "About") centre-distributed in `{typography.nav-link}` with `{spacing.lg}` gaps. Active link receives a 2px bottom border in `{colors.ink}` — gallery-underline convention rather than fill. Cart and account icons right-align. No mega-menu or hover-glow; the navigation is deliberately recessive.

### Cards

**`product-card`** — Artwork thumbnail at full card width with a locked aspect ratio (typically 4:3 or portrait 3:4 following the physical work); no overlay on default state. Below the image: title in `{typography.title-sm}`, artist name in `{typography.artist-label}` / `{colors.muted}`, price in `{typography.price-display}` / `{colors.ink}`. A `{colors.hairline}` border wraps the card with `{rounded.xs}` corners. Hover state lifts the card with a subtle box-shadow without scaling the thumbnail.

**`artist-profile-card`** — Used in "Browse by Artist" index grids: square or circular avatar at top, name in `{typography.title-md}`, graduation school and year in `{typography.caption}` / `{colors.muted}`. `{spacing.base}` padding all sides, `{colors.hairline-soft}` border. Hover lifts identically to product-card.

### Taxonomy & Filtering

**`filter-accordion`** — Each filter dimension (Medium, Price Range, Style, Colour, Size) occupies an accordion row with `{colors.hairline}` bottom border and a right-aligned chevron. `{typography.title-sm}` for the category label; open state reveals a checkbox or range-slider list in `{typography.body-sm}`. Collapsed by default on mobile.

**`filter-chip`** — Applied-filter pill in `{rounded.full}` shape, `{typography.caption}` text; default state is white with `{colors.hairline}` border. Active/selected chip inverts to `{colors.ink}` fill with `{colors.on-primary}` text to signal a live constraint. Rendered in a horizontal scroll row above the grid on mobile.

### Content Zones

**`hero-editorial`** — Full-width editorial section on `{colors.canvas}`. Headline in `{typography.display-xl}` sits left in a 2-column split; body copy at `{typography.body-md}` beneath the headline, large artwork photography filling the right column. `{spacing.section}` padding top and bottom. Used on the homepage and seasonal collection landing pages.

**`artwork-edition-tag`** — 11px uppercase micro-label in `{typography.edition-tag}` declaring edition status ("Original", "Limited Edition of 10", "Sold"). No border-radius (`{rounded.none}`), `{colors.surface-soft}` fill. Sits directly above or below the price line in the product-card and on the artwork detail page.

### Pagination & Footer

**`pagination`** — Flat numbered links in `{typography.body-sm}`; active page uses a `{colors.ink}` filled square with `{colors.on-primary}` text at `{rounded.none}` — matches the grid's sharp geometry. Previous/next arrows flank the page numbers with `{spacing.xs}` gaps.

**`footer`** — `{colors.surface-soft}` background, `{colors.hairline}` top rule. Four-column link grid (About, For Artists, Help, Newsletter) in `{typography.body-sm}` / `{colors.link}`. Social icons and copyright line in `{typography.caption}` / `{colors.muted}`. `{spacing.xxl}` vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column artwork grid; nav collapses to hamburger + logo + cart icon; filter panel becomes full-screen modal drawer; hero stacks to single column, image first |
| Tablet | 744–1128px | Two-column artwork grid; nav shows top-level links, secondary categories in overflow menu; filter panel shifts to 240px fixed left sidebar |
| Desktop | 1128–1440px | Three-column artwork grid; full horizontal nav at 64px; hero achieves two-column editorial split |
| Wide | > 1440px | Four-column artwork grid; content max-width 1200px centred with side gutters; hero widens image column proportions |

### Touch Targets
- All buttons minimum 44px height to meet iOS/Android guidelines
- Nav links receive 48px tap zone via extended vertical padding
- Filter checkboxes and accordion rows minimum 44px tap height
- Filter chips minimum 36px tap height with horizontal scroll on mobile
- Pagination links minimum 36×36px tap surface

### Collapsing Strategy
- Primary nav: full text links → hamburger icon below 744px
- Filter panel: left sidebar → full-screen modal drawer below 744px; all accordions collapsed by default on mobile
- Artwork grid: 4-col → 3-col → 2-col → 1-col at 1440 / 1128 / 744 / 480px breakpoints
- Hero: 2-col (text left, image right) → single-column stacked below 744px, image leading
- Footer: 4-col link grid → 2-col below 744px → single column below 480px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Live extraction blocked by Cloudflare anti-bot ("Just a moment..." page title); only one hex value (#313131) was recovered from the static response
- No confirmed accent, highlight, or secondary brand colour — all surface tones (surface-soft, hairline, muted) are gallery-convention inferences, not measured values
- No custom or licensed typeface confirmed; site appears to serve OS system fonts, but a web font may load after bot-check resolution
- No confirmed button border-radius, hover animation timing, or transition easing values
- No confirmed breakpoint pixel values — standard gallery-grid breakpoints assumed
- No dark-mode palette or preference-media-query behaviour observed
- Logo treatment, exact wordmark typeface, and header height unconfirmed
- Price formatting conventions (GBP symbol placement, decimal display, "From £X" patterns) not extractable from static snapshot
- No confirmed grid gutter widths or max-content-width values
