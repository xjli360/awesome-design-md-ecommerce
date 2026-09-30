---
version: alpha
name: "Single Stone"
source_url: "https://www.singlestone.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every ring in the Single Stone catalog opens with its stone's biography — old European cuts, mine cuts, and rose-cut diamonds described by era, carat geometry, and provenance rather than retail tier. The palette follows that curatorial logic: antique gold (#a88d48) is the brand's single voltage, warm like aged patina rather than polished brightness, paired against near-absolute blacks (#171717, #121212) that give each diamond uncontested luminance. A secondary note of deep teal (#09728c) appears in select accent positions — link hovers, editorial markers — adding the quiet distinctiveness that separates a curated gem cabinet from a category retailer. Cream (#fcf1cd) surfaces in editorial passages and callout fields, warming the otherwise cool neutral ground. Navy (#1e2d47) anchors footer and deep feature sections, grounding the brand in archival formality.

  Type divides cleanly between two registers. Playfair Display carries all editorial and display moments — ring names, provenance headers, hero text — at weights where bracketed serifs are explicitly visible at 36–60px. Jost handles the transactional and navigational layer: prices, labels, CTAs, nav items — geometric and measured, a disciplined counterpart to the serif's warmth. Together they produce a page that reads like a gemologist's report bound into an art catalogue, neither purely romantic nor purely clinical. Letter-spacing on uppercase labels and buttons runs wide (1.5–2px), a precision that emphasizes craft heritage rather than digital fluency.

  Corner radii are minimal throughout — buttons at `{rounded.none}`, product cards at `{rounded.xs}` — consistent with the language of metalwork, where hard edges signal a jeweler's hand. Spacing is generous at editorial scale (`{spacing.section}` at 64px and `{spacing.xxl}` between stone groupings), letting each piece breathe as its own world, while detail typography compresses tightly around carat, cut, and color specifications. The canvas flips between registers: pale grey (#f2f2f2) for product listings; near-black (#121212) for hero and story sections — a deliberate inversion that lets antique gold (#a88d48) read with equal warmth in both light and dark contexts.

colors:
  primary: "#a88d48"
  primary-active: "#dd9a1a"
  primary-disabled: "#dedede"
  navy: "#1e2d47"
  teal: "#09728c"
  cream: "#fcf1cd"
  ink: "#171717"
  body: "#232323"
  muted: "#555555"
  muted-mid: "#4c4c4b"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#f2f2f2"
  canvas-dark: "#121212"
  surface-soft: "#e2e2e2"
  surface-card: "#f2f2f2"
  on-primary: "#171717"
  on-dark: "#f2f2f2"

typography:
  display-xl:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 60px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  display-italic:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.5
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  title-sm:
    fontFamily: "'Jost', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.3px
  body-md:
    fontFamily: "'Jost', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Jost', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  label-upper:
    fontFamily: "'Jost', 'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 2px
    textTransform: uppercase
  price:
    fontFamily: "'Jost', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Jost', 'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', 'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Jost', 'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.8px

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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.on-dark}"
    padding: 13px 31px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "4/5"
    imageBackgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-sm}"
    priceTypography: "{typography.price}"
    labelTypography: "{typography.label-upper}"
    labelColor: "{colors.muted}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-italic}"
    ctaVariant: button-ghost
    minHeight: 600px
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.xl}"
  provenance-tag:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.ink}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
    border: none
  stone-spec-row:
    backgroundColor: transparent
    labelTypography: "{typography.label-upper}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.body}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} 0"
  ring-detail-hero:
    backgroundColor: "{colors.surface-card}"
    imageBackgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-md}"
    provenanceTypography: "{typography.display-italic}"
    priceTypography: "{typography.title-md}"
    rounded: "{rounded.none}"
    primaryCtaVariant: button-primary
    secondaryCtaVariant: button-secondary
  collection-filter:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
  editorial-callout:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.primary}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge-handcrafted:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.label-upper}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: none
    padding: "{spacing.sm} {spacing.base}"
    placeholderColor: "{colors.muted}"
    iconColor: "{colors.muted}"
    iconFocusColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.label-upper}"
    bodyTypography: "{typography.body-sm}"
    linkHoverColor: "{colors.primary}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.xl}"
    paddingHorizontal: "{spacing.xl}"

## Components

### Buttons

**`button-primary`** — Gold (`{colors.primary}`) fill with near-black text (`{colors.on-primary}`), set in all-caps Jost at 13px with 1.5px letter-spacing and square corners (`{rounded.none}`). Hover transitions the fill to brighter amber (`{colors.primary-active}`). At 48px height the button reads as a declaration rather than an invitation — appropriate for a high-consideration purchase like a ring.

**`button-secondary`** — Transparent background with a 1px `{colors.primary}` border and matching text. Uses the same uppercase Jost treatment as primary; border and text brighten to `{colors.primary-active}` on hover. Sits at the same 48px height for visual parity in side-by-side CTA layouts on the ring PDP.

**`button-ghost`** — Transparent with a 1px `{colors.on-dark}` border, used exclusively over dark hero and editorial backgrounds (`{colors.canvas-dark}`). The 1.5px letter-spacing holds the label legible against complex photographic backgrounds without requiring a fill.

### Navigation

**`nav-bar`** — Light `{colors.canvas}` ground with `{typography.nav-link}` links in `{colors.ink}` (Jost 13px, 0.8px tracking). Height 72px, separated from page content by a single `{colors.hairline}` bottom border. Logo renders in `{colors.ink}`. The nav stays fixed on scroll with no background shift — the hairline is the only structural separator.

### Product Cards

**`product-card`** — Off-white `{colors.surface-card}` ground with a minimal `{rounded.xs}` corner. Image crops to a 4:5 portrait ratio on `{colors.surface-soft}`, emphasizing ring silhouette. A `{typography.label-upper}` cut-classification line (e.g. "OLD EUROPEAN CUT") in `{colors.muted}` sits above the title; stone name renders in `{typography.display-sm}` (Playfair Display, 24px); price follows in `{typography.price}` (Jost, 18px). This ordering — classification, name, price — mirrors the hierarchy of a gem report rather than a retail listing.

### Hero

**`hero`** — Full-bleed section on `{colors.canvas-dark}`. Headline in `{typography.display-xl}` (Playfair Display, 60px) with `{colors.on-dark}` text; an italic subhead in `{typography.display-italic}` appears below, typically carrying a provenance line or editorial phrase. CTA renders as `button-ghost` against the dark ground. Minimum height 600px with `{spacing.xxl}` vertical padding.

### Provenance & Detail Components

**`provenance-tag`** — A cream-filled (`{colors.cream}`) flat label in `{typography.label-upper}` (Jost, 11px, 2px tracking) with no border radius. Applied to individual stones on collection pages and the PDP to signal vintage origin — "CIRCA 1920", "ANTWERP CUT". Reads warmly against both the light `{colors.canvas}` product ground and the darker `{colors.navy}` editorial panels.

**`stone-spec-row`** — A horizontal row inside a gemological specs table. Label column in `{typography.label-upper}` at `{colors.muted}`; value column in `{typography.body-sm}` at `{colors.body}`. Each row has a `{colors.hairline-soft}` bottom border. Applied to carat, cut grade, color, clarity, origin, and metal on the PDP — the component where Single Stone's curatorial positioning is most concretely expressed.

**`ring-detail-hero`** — The PDP layout unit. Image area on `{colors.surface-soft}` with no radius. Title in `{typography.display-md}`, provenance italic in `{typography.display-italic}`, price in `{typography.title-md}`. Add-to-cart maps to `button-primary`, enquire-now maps to `button-secondary`. Square corners throughout reinforce the metalwork precision register.

### Editorial & Content

**`editorial-callout`** — Full-width block on `{colors.navy}` with headline in `{typography.display-md}` and body in `{typography.body-md}`, both `{colors.on-dark}`. Gold `{colors.primary}` is applied to pull-quotes, horizontal rules, or highlighted names within the copy. Used for brand-story sections, "About Our Diamonds", and handcraft narratives where the tone shifts from transactional to archival.

**`badge-handcrafted`** — A small outlined badge with `{colors.primary}` text and a 1px `{colors.primary}` border on transparent ground, rendered in `{typography.label-upper}`. Applied in hero and collection contexts to mark "HANDCRAFTED" or "ONE OF A KIND" provenance without crowding the product image.

### Collection & Search

**`collection-filter`** — Flat pill-tags with a 1px `{colors.hairline}` border and transparent background, copy in `{typography.caption}`. Active state inverts to `{colors.ink}` fill with `{colors.on-dark}` text. Used for cut-type, era, and metal-type filters on collection and search results pages.

**`search-bar`** — Low-contrast search area on `{colors.surface-soft}` with no border and square corners. Placeholder in `{colors.muted}`; icon shifts from `{colors.muted}` to `{colors.primary}` on focus. Expands inline within the header rather than opening an overlay panel.

### Footer

**`footer`** — Near-black `{colors.canvas-dark}` ground with column headings in `{typography.label-upper}` and nav links in `{typography.body-sm}`. Link hover color is `{colors.primary}` (antique gold against dark ground). Generous `{spacing.section}` top padding gives the footer the visual weight appropriate to a high-consideration purchase — it reads as a destination, not a collapse.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline scales to `{typography.display-md}`; nav collapses to hamburger drawer; stone-spec-row label stacks above value; product-card image expands to full width |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links only, secondary items collapse; ring-detail-hero stacks image above copy; editorial-callout reduces padding to `{spacing.xl}` |
| Desktop | 1128–1440px | Three-column product grid; ring-detail-hero splits 50/50 image and copy side-by-side; full nav-bar link set visible; editorial-callout uses constrained centered column |
| Wide | > 1440px | Content max-width ~1440px centered; side margins expand; hero text may shift from centered to left-aligned with stone image pinned right; product grid may extend to four columns |

### Touch Targets

- `button-primary` and `button-secondary` are minimum 48px height on all viewports
- `collection-filter` tags expand tap target to minimum 44px via vertical padding on mobile
- `nav-bar` hamburger hit area is minimum 44×44px
- `stone-spec-row` rows expand to 48px height on mobile for legibility and thumb navigation

### Collapsing Strategy

- Navigation collapses to a left-sliding drawer at < 744px; drawer ground is `{colors.canvas-dark}` with `{colors.on-dark}` links and `{colors.primary}` active state
- Three-column product grid collapses to two columns at 744px and single column at < 480px
- Hero italic subhead (`{typography.display-italic}`) hides at < 480px to preserve headline impact at the smallest sizes
- Stone spec table switches from two-column inline layout to label-above-value stacked layout at < 744px
- Editorial callout body copy reduces from 16px to 15px on mobile while retaining the Jost typeface and line-height

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Whether button text on gold CTA uses dark (`#171717`) or light (`#f2f2f2`) is unconfirmed; file defaults to dark for accessibility (contrast ratio ~5.8:1 vs ~3.1:1 for light)
- Exact nav behavior on scroll (fixed canvas throughout vs. transparent-to-opaque) not determinable from extraction alone
- `#108043` (forest green) and `#f2faf0` (pale sage) are likely Shopify admin badge remnants; omitted from brand palette
- `#212b36` is a known Shopify admin dark color and has been excluded; `#1e2d47` is retained as the brand navy
- `primary-disabled` hex is derived from the extracted `{colors.hairline}` (#dedede) rather than a confirmed disabled-state token
- Hover and focus-ring treatment on interactive elements not captured in static color extraction
- Exact logo lockup (wordmark vs. monogram vs. signet mark) and header logo sizing cannot be confirmed without visual inspection
- Animation timing curves on card hover, gallery transitions, and drawer open/close are not available from extraction
- Whether Open Sans is used alongside Jost or has been fully superseded by it in the current build is ambiguous from font-stack order alone
