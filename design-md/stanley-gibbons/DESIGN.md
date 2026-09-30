---
version: alpha
name: "Stanley Gibbons"
source_url: "https://www.stanleygibbons.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A Cape of Good Hope Triangular or a Penny Black arrives on the Stanley Gibbons website the same way it appears in their printed catalogue — lot reference in tight Montserrat capitals, catalogue value in Libre Baskerville roman, condition notes in Open Sans at sustained-reading weight — a tripartite typographic system descended directly from 170 years of auction print. The palette compresses that heritage into two anchor points: antique gold (#c9a84c) and near-black navy (#0e1a2e), the same combination embossed on the spine of every Stanley Gibbons World Catalogue since the Victorian era. Between them, a warm cream canvas (#f5f0e8) substitutes for archival stock, rejecting clinical digital white in favour of a tone that signals age and provenance. The pale gold (#f0e0a0) that washes certain panel surfaces echoes the ivory mounts collectors slide beneath their finest imperforates — not decorative, but referential. The navy is not monolithic: #0e1a2e anchors the deepest hero fields, #152340 handles section headers, #1d2f4f lifts the navigation strip, three steps creating perceived depth without resort to gradients. Corner radii are minimal — {rounded.xs} on cards, {rounded.sm} on primary action buttons — because hard geometry suits a dealer of historical documents. The gold primary CTA (#c9a84c) carries dark navy lettering ({colors.ink}), a pairing that reads as both legible and premium. Condition badges, rarity indicators, and catalogue-reference chips use 11px Montserrat all-caps with generous tracking — the digital equivalent of a dealer's hand-stamped stock notation, compact enough to sit beside a 32px stamp thumbnail without competing. Footer runs full-width in the deepest navy (#0e1a2e) with cream type ({colors.on-dark}) and gold rule separators, mirroring the colophon page of the printed catalogue in column division and typographic hierarchy.

colors:
  primary: "#c9a84c"
  primary-active: "#a07828"
  primary-disabled: "#f0e0a0"
  ink: "#0e1a2e"
  body: "#1d2f4f"
  muted: "#5a6e85"
  hairline: "#d6ccb4"
  canvas: "#f5f0e8"
  surface-soft: "#f0e0a0"
  surface-card: "#ffffff"
  on-primary: "#0e1a2e"
  on-dark: "#f5f0e8"
  navy-deep: "#0e1a2e"
  navy-mid: "#152340"
  navy-nav: "#1d2f4f"
  gold-dark: "#a07828"
  condition-fine: "#1a6b3a"
  condition-used: "#7a8a9a"
  error: "#c0392b"

typography:
  display-xl:
    fontFamily: "'Libre Baskerville', Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Libre Baskerville', Georgia, serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Libre Baskerville', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.03em
  body-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.08em
    textTransform: uppercase
  lot-number:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.1em
    textTransform: uppercase
  catalogue-value:
    fontFamily: "'Libre Baskerville', Georgia, serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'Libre Baskerville', Georgia, serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.06em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.03em
  category-label:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  search-input:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
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
    padding: 12px 28px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.navy-mid}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.navy-mid}"
  button-secondary-on-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.on-dark}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 8px 0
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.search-input}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar-strip:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.navy-nav}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "3px solid {colors.primary}"
    logoColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspect: "4/3"
    shadowHover: "0 4px 16px rgba(14,26,46,0.14)"
  product-card-lot-number:
    typography: "{typography.lot-number}"
    textColor: "{colors.muted}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.navy-mid}"
  product-card-catalogue-value:
    typography: "{typography.catalogue-value}"
    textColor: "{colors.gold-dark}"
  hero:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} 0"
    accentColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    subheadColor: "{colors.surface-soft}"
    subheadTypography: "{typography.body-md}"
    headlineAccentBorder: "4px solid {colors.primary}"
  section-header:
    backgroundColor: "{colors.navy-mid}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-sm}"
    padding: "{spacing.lg} {spacing.xl}"
    borderLeft: "4px solid {colors.primary}"
  lot-reference-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.lot-number}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    border: "1px solid {colors.hairline}"
  catalogue-value-stamp:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.gold-dark}"
    typography: "{typography.catalogue-value}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  condition-badge:
    backgroundColor: "{colors.navy-nav}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  condition-badge-fine:
    backgroundColor: "{colors.condition-fine}"
    textColor: "#ffffff"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  condition-badge-used:
    backgroundColor: "{colors.condition-used}"
    textColor: "#ffffff"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    inputTypography: "{typography.search-input}"
    inputColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonTypography: "{typography.button-sm}"
    height: 48px
  breadcrumb:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  category-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.navy-mid}"
    typography: "{typography.category-label}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
    hoverBackground: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"
  auction-countdown:
    backgroundColor: "{colors.navy-mid}"
    textColor: "{colors.on-dark}"
    labelTypography: "{typography.title-md}"
    digitColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    iconColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.primary}"
    borderTop: "2px solid {colors.primary}"
    padding: "{spacing.section} 0"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    letterSpacing: 0.08em
    textTransform: uppercase

## Components

### Buttons

**`button-primary`** — Antique gold (#c9a84c) fill with dark navy (#0e1a2e) Montserrat uppercase text at {typography.button-md}. At 44px height and {rounded.sm} corners, the proportions recall a well-struck catalogue stamp. Hover deepens to `button-primary-active` (#a07828); disabled bleeds to pale gold ({colors.primary-disabled}) with muted text. Reserved for "Add to Cart", "Bid Now", "Buy Now", and primary registration CTAs — never diluted to secondary actions.

**`button-secondary`** — 2px navy-mid border on a transparent field, matching primary in height and Montserrat typography. Used for "View Details", "Add to Watchlist", and secondary navigation actions. On dark hero or section-header backgrounds, `button-secondary-on-dark` swaps border and text to cream ({colors.on-dark}), maintaining contrast against the navy field.

**`button-ghost`** — Transparent field, gold (#c9a84c) text, no border. Used for inline link-style actions — "View All Lots", "See More Results" — where a bordered button would add structural weight to an already data-dense panel. The gold text colour is the sole affordance signal.

### Text Input & Search

**`text-input`** — Warm cream (#f5f0e8) field with a single hairline border, 44px height, and {rounded.xs} corners. On focus, the border upgrades to 2px gold ({colors.primary}), a deliberate echo of the gold rule that separates catalogue sections in print. Placeholder text sits in the muted palette ({colors.muted}).

**`search-bar`** — Full-width unified search with an attached gold-filled submit button. The input carries {typography.search-input} (Open Sans 15px) and the attached button runs {typography.button-sm} in Montserrat caps. The integrated single-height treatment — shared border, flush button — presents the bar as a catalogue-lookup instrument rather than a form element. Focus ring upgrades the entire composite to a 2px gold outline.

### Navigation

**`nav-bar`** — Two-layer navigation: a 36px `nav-bar-strip` in deep navy (#0e1a2e) carrying account links, trust signals, and the telephone number in 13px caption type; then the main 64px navy strip ({colors.navy-nav}) with Montserrat nav-links, the gold Stanley Gibbons wordmark on the left, and account/basket icons on the right. A 3px gold bottom border ({colors.primary}) separates navigation from page content, functioning as both a brand mark and a structural horizon line.

### Product Cards

**`product-card`** — White surface, 1px hairline border, {rounded.xs}. The card stacks a 4:3 image panel above a data zone structured top-to-bottom as: lot reference in `product-card-lot-number` (grey Montserrat caps), product title in `product-card-title` ({typography.title-md}), catalogue value in `product-card-catalogue-value` (gold-dark Libre Baskerville), then market price in `product-card-price` ({typography.price-display}). Hover elevates with a soft navy-tinted shadow (`0 4px 16px rgba(14,26,46,0.14)`), connecting the shadow colour to the brand palette without a visible glow.

**`lot-reference-tag`** — Pale-gold surface (#f0e0a0), hairline border, tight Montserrat lot-number type. Appears as a chip in the upper corner of product cards and at the head of lot-detail pages. Styled to suggest a dealer's stock ticket rather than a UI interface badge.

**`catalogue-value-stamp`** — Cream canvas background with gold-dark ({colors.gold-dark}) Libre Baskerville value text. Bordered by hairlines top and bottom. On product cards it occupies a dedicated row, cleanly separating catalogue value from the live market price directly beneath it — a distinction collectors read as the premium-over-catalogue spread.

### Badges & Labels

**`condition-badge`** — {rounded.xs}, tight Montserrat badge type (11px, all-caps, 0.08em tracking). Default uses navy-nav background for standard grades. `condition-badge-fine` uses #1a6b3a green for VF/Superb/Superb grades; `condition-badge-used` uses condition-used grey for postally-used examples. Placed as an overlay on the product card image corner or inline in lot-detail page headers.

**`category-pill`** — White pill with hairline border and navy-mid Montserrat category-label type. On hover, fills to gold (#c9a84c) with dark navy text — an instantaneous fill transition that confirms selection without a heavy UI state change. Used in category-browsing filter rows and the homepage featured-categories grid.

**`trust-badge`** — Pale-gold surface, gold icon ({colors.primary}), Open Sans caption text. Deployed in horizontal groups of three or four beneath the cart module and on the homepage, surfacing "Established 1856", "100% Guaranteed Authentic", and "Expert Certificates Available". The pale-gold background ties these to the primary palette while keeping them visually subordinate to product imagery.

### Hero

**`hero`** — Full-bleed deep navy (#0e1a2e) with the page headline in {typography.display-xl} (Libre Baskerville cream) and a secondary line in pale gold (#f0e0a0). A 4px left-rule in {colors.primary} brackets the headline block — the sole graphic element beyond type and a right-panel product image. Layout is left-text / right-image at a 50/50 split on desktop, with a pair of stacked CTAs (primary gold + `button-secondary-on-dark`) below the subhead.

### Auction Components

**`auction-countdown`** — Navy-mid (#152340) panel with Montserrat "Lot Closes In" label in {typography.title-md} and gold ({colors.primary}) digit blocks for days / hours / minutes / seconds. The gold-on-navy contrast is the highest-contrast pairing in the design system, appropriate for time-sensitive bidding information. Appears as a sticky strip above the lot-detail image on active auctions, and as a compact inline element on collection listing cards.

### Section Headers

**`section-header`** — Full-width navy-mid (#152340) band with Libre Baskerville display-sm cream headline and a 4px left-border accent in gold. Used above curated collection rows, category landing headers, and editorial spotlight sections. The left-rule treatment directly echoes the running-head decoration in the printed catalogue.

### Footer

**`footer`** — Full-width deep navy (#0e1a2e) block, 2px gold top rule. Four-column link grid with `footer-heading` labels (Montserrat title-sm, forced uppercase, 0.08em letter-spacing) over body-sm Open Sans links in cream ({colors.on-dark}); active links render in gold ({colors.primary}). The Stanley Gibbons Royal Warrant crest and "Founded 1856" wordmark sit in a secondary strip with a hairline separator above them. The footer column division and typographic hierarchy deliberately mirror the colophon page of the printed World Catalogue.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger on navy-nav strip with gold icon; search bar drops to second row below wordmark; hero stacks headline above image full-width; auction-countdown becomes full-width pinned top strip; catalogue-value-stamp collapses to inline "(Cat. £xxx)" parenthetical |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories with overflow behind "More" dropdown; hero runs 55/45 text-image split; category-pill row scrolls horizontally with fade mask at edges |
| Desktop | 1128–1440px | Three-column product grid; full two-tier navigation visible; hero constrained to 1280px max-width with 50/50 split; category-pill row wraps to two rows maximum; nav-bar-strip visible |
| Wide | > 1440px | Four-column product grid; all content constrained to 1440px max-width; navy-deep side gutters fill the remainder; hero image scales within fixed text block |

### Touch Targets

- All primary and secondary buttons: minimum 44 × 44px
- Product card: entire card surface is the tap target; no isolated sub-elements navigated independently
- Condition badges: not independently tappable; the enclosing card or lot-detail tap zone covers them
- Nav items on mobile drawer: 48px minimum tap height with full-width gold-left-rule active highlight
- Category pills: minimum 36px height at all breakpoints; 12px horizontal padding floor
- Auction-countdown digit blocks: display only; adjacent "Place Bid" CTA provides the action at 44px minimum

### Collapsing Strategy

- `nav-bar-strip` (top 36px utility row) hides below 744px; trust signals migrate to footer
- Two-tier desktop nav collapses to a single hamburger icon at mobile; the full-screen navy drawer stacks strip / main nav / category links vertically in the same visual hierarchy
- `catalogue-value-stamp` dedicated row on product cards condenses to inline parenthetical at mobile to keep card height under 280px
- Auction-countdown moves from sticky right-panel sidebar (desktop lot detail) to pinned full-width top strip on mobile and tablet
- Four-column footer grid folds to single accordion column on mobile; Royal Warrant strip remains pinned at all breakpoints as a trust credential

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Muted text color (#5a6e85) is derived, not extracted — the actual muted tone may be a lighter warm-grey closer to the cream palette
- Hairline border color (#d6ccb4) is derived from the cream canvas; the live border token may be a cooler grey with no warm tint
- Surface-card white (#ffffff) is assumed; no pure-white hex appeared in the extraction
- Error state (#c0392b) and condition-fine green (#1a6b3a) are accessible standard values, not brand-extracted
- Hover-state timing, focus-ring width, and transition durations are not captured from the static render
- Exact Montserrat weight distribution across nav levels (500 vs 600 vs 700) is inferred from hierarchy convention, not confirmed
- Royal Warrant crest treatment — vector vs. raster, colour inversion on dark surfaces — is not described in the extraction
- Icon set identity (catalogue browse icons, social icons, trust credential marks) is not confirmed; likely custom SVGs or a licensed set
- Font loading strategy (self-hosted vs Google Fonts CDN) and subsetting approach not confirmed
- Breakpoint values for the category-pill horizontal scroll behaviour are estimated from common practice
