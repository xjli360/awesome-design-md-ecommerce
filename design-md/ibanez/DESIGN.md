---
version: alpha
name: "Ibanez"
source_url: "https://www.ibanez.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Guitar bodies materialized from #0a0a0a void — this is Ibanez's primary visual grammar: instruments photographed on total black, hardware glinting without a visible light source, finish colors radiating as if luminescent against the void. The site operates as a dark-mode-native catalog, with near-black (#0a0a0a and #222222) stacked for canvas and surface-soft, then #303030 cards lifting slightly above the depth floor. Condensed Oswald in all-caps uppercase carries every headline at weights from 400 to 700, while Open Sans handles technical spec paragraphs at 16px/1.6 — the pairing mirrors the contrast between a guitar's raw steel strings and its resonant tonewood. Raleway appears for sub-category labels with tracked-out uppercase at 11–14px, adding an editorial register between the muscular display and the utilitarian body text. The brand also carries a full Japanese font stack (Hiragino, YuGothic, Meiryo, HGS明朝E) anchored to its domestic market, hinting that the English site is one node of a globally parallel system.

  Color voltage arrives through a category-stripe system: a 4px horizontal rule in series-specific hues runs beneath product card images, color-coding the lineup without cluttering the dark canvas. The RG series pulls {colors.primary} (#41529a, a slate navy); the S series bleeds {colors.accent-red} (#dd2211); AZ takes {colors.accent-orange} (#eb5505); Prestige and Premium carry {colors.accent-purple} (#724c8c) and {colors.accent-cyan} (#00a7cb); the GIO entry-level line runs {colors.accent-green} (#61b14b), signaling accessibility without apology. This chromatic taxonomy borrows from physical finish chip selectors — each hue becomes a series marker rather than decoration.

  No border radii appear in the structural UI — buttons, inputs, cards, and nav containers all use {rounded.none}, a sharp-cornered industrial grammar matching the machined-metal aesthetic of a guitar's cavity covers and hardware plates. Finish swatch selectors are the single exception, rendered as small circles ({rounded.full}) that echo fretboard dot inlays. The search bar and text inputs sit borderless except for a 1px {colors.hairline} stroke; focus states promote {colors.primary} as the only pop of color in otherwise monochromatic form fields. CTAs appear in solid {colors.primary} blocks with 1.5px letter-spacing in Oswald uppercase — punchy at small sizes without becoming aggressive.

colors:
  primary: "#41529a"
  primary-active: "#2d3a75"
  primary-disabled: "#6b7ab8"
  accent-red: "#dd2211"
  accent-orange: "#eb5505"
  accent-orange-warm: "#e9611d"
  accent-green: "#61b14b"
  accent-purple: "#724c8c"
  accent-cyan: "#00a7cb"
  accent-blue: "#0066aa"
  accent-sky: "#5da8eb"
  ink: "#ebebeb"
  body: "#bcbcbc"
  muted: "#888888"
  muted-dark: "#555555"
  hairline: "#555555"
  hairline-soft: "#303030"
  canvas: "#0a0a0a"
  surface-soft: "#222222"
  surface-card: "#303030"
  surface-mid: "#3a3a3a"
  on-primary: "#ffffff"
  on-dark: "#ebebeb"
  alert: "#dd2211"
  caution: "#eb5505"
  sale: "#dd2211"
  new-badge: "#41529a"
  cream: "#fffeef"

typography:
  display-xl:
    fontFamily: "Oswald, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
    textTransform: uppercase
  display-lg:
    fontFamily: "Oswald, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "Oswald, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: 0
    textTransform: uppercase
  display-sm:
    fontFamily: "Oswald, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: 0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "Raleway, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "Raleway, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  series-label:
    fontFamily: "Oswald, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "Oswald, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "Oswald, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Oswald, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Oswald, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  price-display:
    fontFamily: "Oswald, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.1
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
    rounded: "{rounded.none}"
    padding: 12px 28px
    height: 44px
    hoverBackgroundColor: "{colors.primary-active}"
    disabledBackgroundColor: "{colors.primary-disabled}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 11px 27px
    height: 44px
    hoverBackgroundColor: "{colors.surface-card}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 11px 24px
    hoverBackgroundColor: "{colors.surface-soft}"
  button-text:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    hoverTextColor: "{colors.ink}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorderColor: "{colors.primary}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoHeight: 36px
    dropdownBackgroundColor: "{colors.surface-soft}"
    dropdownTextColor: "{colors.body}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    subTextTypography: "{typography.body-sm}"
    subTextColor: "{colors.body}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    imageBackgroundColor: "{colors.surface-soft}"
    seriesStripeHeight: 4px
  hero:
    backgroundColor: "{colors.canvas}"
    overlayColor: "rgba(0,0,0,0.5)"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 600px
    ctaGap: "{spacing.md}"
    contentMaxWidth: 640px
  series-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.series-label}"
    rounded: "{rounded.none}"
    padding: "4px 12px"
  category-stripe:
    height: 4px
    rounded: "{rounded.none}"
    seriesColors:
      RG: "{colors.primary}"
      S: "{colors.accent-red}"
      AZ: "{colors.accent-orange}"
      Prestige: "{colors.accent-purple}"
      Premium: "{colors.accent-cyan}"
      GIO: "{colors.accent-green}"
      Artist: "{colors.accent-blue}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    alternateRowColor: "{colors.canvas}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} {spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorderColor: "{colors.primary}"
    height: 40px
    iconColor: "{colors.muted}"
    iconHoverColor: "{colors.ink}"
  gallery-viewer:
    backgroundColor: "{colors.canvas}"
    thumbnailBackgroundColor: "{colors.surface-soft}"
    thumbnailBorder: "2px solid transparent"
    thumbnailActiveBorder: "2px solid {colors.primary}"
    rounded: "{rounded.none}"
    thumbnailSize: 64px
    gap: "{spacing.sm}"
  finish-swatch:
    size: 28px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.ink}"
    borderInactive: "2px solid transparent"
    gap: "{spacing.xs}"
    tooltipBackgroundColor: "{colors.surface-soft}"
    tooltipTypography: "{typography.caption}"
  new-badge:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.muted-dark}"
    typography: "{typography.caption}"
    activeTextColor: "{colors.ink}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.ink}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline-soft}"
    padding: "{spacing.xxl} 0"
    legalTypography: "{typography.caption}"
    legalColor: "{colors.muted}"

## Components

### Buttons

**`button-primary`** — Solid {colors.primary} (#41529a) block with Oswald uppercase at 14px/1.5px letter-spacing and {rounded.none} corners; the hard edge reads as industrial hardware, not consumer SaaS. Hover darkens to {colors.primary-active} (#2d3a75) with no transition delay — the state change is immediate, like a switch. Disabled state uses {colors.primary-disabled} (#6b7ab8), a desaturated version of primary that remains visible on the dark canvas without implying interactability.

**`button-secondary`** — Transparent fill with a 1px {colors.ink} border and the same Oswald uppercase spec as primary. The outline approach lets the dark canvas show through, keeping the composition uncluttered when primary and secondary CTAs share a row. Hover fills with {colors.surface-card} (#303030).

**`button-ghost`** — Reserved for tertiary actions adjacent to primary; border and text take {colors.primary} (#41529a) rather than ink, so the element signals affiliation with the primary action without competing for hierarchy. Used for "Compare," "Add to Wishlist," and spec-download links.

**`button-text`** — Borderless, no fill, {colors.body} text. Appears in dense spec areas and footer navigation where a bordered button would overwhelm the layout.

### Text Input & Search

**`text-input`** — {colors.surface-soft} fill on the dark canvas reads as a slightly lighter cavity, not a bright field. The 1px {colors.hairline} border is subtle enough to disappear on first glance; focus promotes it to {colors.primary} (#41529a) as the only interactive color signal. Placeholder text in {colors.muted} (#888888) provides enough contrast without suggesting filled state.

**`search-bar`** — Identical construction to text-input but shorter (40px height) with a leading magnifier icon in {colors.muted}. The icon shifts to {colors.ink} on focus, extending the monochromatic progression from muted to active. No rounded corners — the search bar sits flush with nav and filter containers, treated as an input slot in a hardware panel.

### Navigation

**`nav-bar`** — 64px tall, {colors.canvas} background with a 1px {colors.hairline-soft} bottom border that barely separates nav from hero photography. Nav links use Oswald 13px/uppercase/1px tracking — compact enough to accommodate eight or more series categories without wrapping. Dropdowns surface from {colors.surface-soft} as full-width panels, listing series with their 4px color-stripe accents repeated inline as left-border marks. The Ibanez wordmark logomark sits at 36px height.

### Product Card

**`product-card`** — {colors.surface-card} (#303030) lifts off {colors.surface-soft} (#222222) by just 14 levels of lightness — the card boundary is present but not aggressive. The series category stripe (4px, series-specific accent color) runs as a top border on the image container, providing the primary visual differentiator between guitar lines before the user reads the name. Name renders in {typography.title-sm} (Raleway 13px uppercase), price in {typography.price-display} (Oswald 24px), and secondary info (body, scale length) in {typography.body-sm} muted text. No drop shadow — cards separate by background contrast alone.

### Hero

**`hero`** — Full-bleed dark photography with guitars as the only light source in the composition. A 50% black scrim over the lower portion of the image ensures text legibility on wildly different photography. Headline runs {typography.display-xl} (Oswald 56px/uppercase) in {colors.ink} (#ebebeb); subhead uses {typography.body-md} in {colors.body}. CTA row places button-primary and button-ghost side by side with {spacing.md} gap. Minimum height 600px; content is left-aligned in a 640px max-width column with {spacing.section} left padding.

### Series Badge & Category Stripe

**`series-badge`** — A compact tag (Oswald 22px/uppercase, {colors.primary} fill) that appears at the top of series-landing headers and in mega-menu series blocks. Because the six primary series each have a dedicated accent color managed by {category-stripe}, the badge itself defaults to {colors.primary} navy and inherits the series accent only when it appears inside a series-specific context (the stripe handles differentiation at the card level).

**`category-stripe`** — A 4px horizontal bar using series-specific accent colors (RG: {colors.primary} #41529a, S: {colors.accent-red} #dd2211, AZ: {colors.accent-orange} #eb5505, Prestige: {colors.accent-purple} #724c8c, Premium: {colors.accent-cyan} #00a7cb, GIO: {colors.accent-green} #61b14b). Appears as a top border on product card image containers, as a left-border mark on dropdown nav list items, and as a full-width rule under series landing page headers. It is the primary brand language distinguishing one guitar line from another.

### Spec Table

**`spec-table`** — Two-column layout with alternating {colors.surface-soft} and {colors.canvas} row backgrounds. Labels (Body, Neck, Frets, Scale, Pickups, Hardware) render in {typography.spec-label} (Oswald 11px/uppercase/1px tracking) in {colors.muted}; values render in {typography.body-sm} in {colors.ink}. The label column width is fixed at 40%; values may contain multi-line content (e.g. pickup model strings). A 1px {colors.hairline-soft} bottom border separates rows. The table makes no use of zebra stripe color for emphasis — every row is equally important.

### Gallery Viewer

**`gallery-viewer`** — The primary guitar image renders on {colors.canvas} black, maximizing finish visibility. Below it, a horizontal scroll of 64×64px thumbnails in {colors.surface-soft} containers uses a 2px {colors.primary} active border and transparent inactive border to indicate selection — the only border radius exception is {rounded.none} here also. Thumbnails change main image on hover (desktop) or tap (mobile) without page navigation.

### Finish Swatch

**`finish-swatch`** — 28px circles ({rounded.full}) in a horizontal row showing available color finishes. Active state gains a 2px {colors.ink} border with 2px gap (implemented as box-shadow offset) to avoid clipping the finish color. Tooltip surfaces on hover in {colors.surface-soft} using {typography.caption}, showing the finish name (e.g. "Black Flat," "Cosmic Blue Star Burst Flat"). This is the sole use of {rounded.full} in the product UI.

### Badges

**`new-badge`** and **`sale-badge`** — Both use {rounded.none} rectangles at {typography.spec-label} (Oswald 11px/uppercase) sizing. New badges use {colors.new-badge} (#41529a) fill; sale badges use {colors.sale} (#dd2211). Positioned as absolute overlays in the top-left corner of product card image containers. Never stacked — if a guitar is both new and on sale, sale takes precedence.

### Footer

**`footer`** — {colors.surface-soft} (#222222) background with a 1px {colors.hairline-soft} top border. Column headings in {typography.title-sm} (Raleway uppercase, {colors.ink}); links in {typography.body-sm} ({colors.body}), hovering to {colors.ink}. Legal text, copyright, and regional links run in {typography.caption} at {colors.muted}. No hover underlines on nav links — color shift alone signals interactability, consistent with the spare dark treatment throughout.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to display-md (28px); nav collapses to hamburger with full-screen overlay in surface-soft; spec table scrolls horizontally; gallery thumbnails move below main image in 5-across row |
| Tablet | 744–1128px | Two-column product grid; hero content shifts to 50% width left-aligned; nav shows top-level series labels, subcategories collapse to dropdown; search bar moves to secondary nav row |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu nav with series stripes as left-border accents on list items; hero min-height 600px with large display-xl headline |
| Wide | > 1440px | Four-column product grid; hero extends to 700px min-height; content column max-width caps at 1440px with auto side margins; spec table expands to two-column layout side-by-side |

### Touch Targets

- All buttons minimum 44px height on mobile — button-primary and button-secondary expand to full-width on screens under 480px
- Finish swatches increase from 28px to 36px on touch devices; gap widens to {spacing.sm}
- Nav hamburger trigger is 48×48px tappable area regardless of icon visual size
- Product card tap area covers the full card including image, not just the title link

### Collapsing Strategy

- Mega-menu nav compresses to accordion-style overlay on mobile; series category entries retain their 4px accent-color left border inside the accordion
- Spec table converts to a single-column stacked label-above-value layout below 480px to eliminate horizontal scroll
- Gallery viewer drops thumbnail row to a dot-indicator pagination system on screens narrower than 480px
- Hero CTA buttons stack vertically on mobile with {spacing.sm} gap; button-primary leads

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Custom `ibanez-fonts` face referenced in font stack but not identifiable from extraction — weight variants, exact metrics, and usage contexts unknown; Oswald/Raleway fill inferred from secondary stack ordering
- Meta theme-color not set — no reliable primary brand color confirmation from HTML; #41529a inferred as primary from its distinctiveness relative to generic grays and blues in the extracted palette
- Exact series-to-color mapping for all sub-series (e.g., Iron Label, Axion Label, Premium vs. Prestige boundary) not extractable; accent color assignments above are approximated from the palette distribution
- Animation and transition timing values not captured — hover transitions on cards, nav dropdowns, and gallery swaps are unspecified
- Price formatting, currency switcher, and regional pricing UI not captured; Ibanez operates regional subdomains with different catalogs
- Authenticated/logged-in states (wishlist, comparison tray, dealer locator form) not visible during extraction
- Mobile nav animation (slide-in vs. fade overlay) not determinable from static extraction
- Japanese-language font rendering priorities within the multilingual stack not confirmed for non-JP locales
