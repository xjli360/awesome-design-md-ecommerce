---
version: alpha
name: "Woodard"
source_url: "https://www.woodard-furniture.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A wrought-iron rocker built in 1920 still turns up on Michigan porches, its powder coat worn to bare metal in spots — unchanged in structure, unlacquered in claim. Woodard's digital presence inherits that economy: a single extracted anchor, charcoal #313131, carries navigation labels, product names, and primary CTAs against a warm off-white canvas without a competing accent voltage. There is no brand Rausch, no seasonal marigold — the palette cedes authority entirely to product photography, where cast-aluminum weave patterns, powder-coat textures, and cushion piping do the persuading. Body copy runs in the system sans-serif stack at 16px/1.6, sensible and unobtrusive; display headings step to a bracketed serif — Georgia, 'Times New Roman' — that ages appropriately into the 1866 founding claim rather than chasing current variable-font releases.

  Buttons suppress every flourish: {rounded.xs} corners, {colors.primary} fill, {colors.on-primary} label, uppercase tracking — a shape closer to a furniture hangtag than a SaaS dashboard CTA. Hover darkens to {colors.primary-active} with no scale transform, no shadow theater. Product cards are quiet containers: a lifestyle photograph at 4:3 aspect ratio, a collection slug in {typography.title-sm} uppercase, a price in {typography.price-display}, and a single "View Collection" anchor. Finish swatches appear as a tight horizontal strip of labeled chips below the product title rather than an expanded color grid with preview thumbnails.

  Navigation assumes a deep catalog organized by frame material and collection name. The mega-menu expands over {colors.canvas} rather than pushing content; a sticky {typography.nav-link} category rail on collection pages keeps the material taxonomy visible without full-page reload. The spacing scale runs wide — {spacing.section} at 64px governs section breaks — because a shopper comparing a cast-aluminum dining set reads finish descriptions and weight specs, not urgency countdowns. The footer surfaces "Est. 1866" in {typography.caption} at full {colors.ink} opacity beside dealer-locator links and finish-care guides, treating the founding year as a product specification rather than sentiment. On mobile the three-column product grid collapses to single-column full-bleed imagery; the mega-menu becomes a full-height drawer and the swatch strip scrolls horizontally.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#b0aba6"
  ink: "#1c1c1c"
  body: "#3d3a36"
  muted: "#7a7571"
  hairline: "#e0dbd3"
  hairline-soft: "#ede9e4"
  canvas: "#ffffff"
  surface-soft: "#f6f3ee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 38px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: -0.25px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.25px
    textTransform: uppercase
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.25px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price-display:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  finish-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px

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
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.xxl}"
    columnGap: "{spacing.xxl}"
  category-rail:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 48px
    position: sticky
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/3"
    gap: "{spacing.sm}"
  collection-hero:
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    minHeight: 560px
    overlayColor: "{colors.scrim}"
    overlayOpacity: 0.42
    paddingX: "{spacing.xxl}"
  finish-swatch:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    selectedTextColor: "{colors.ink}"
    typography: "{typography.finish-label}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  heritage-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.finish-label}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.xs}"
  price-tag:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    gap: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-primary}"
    borderTop: "none"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Charcoal #313131 fill with white uppercase label at 1.25px tracking; corners at `{rounded.xs}` (4px) rather than fully square or pill-shaped, placing it in the register of a hangtag rather than a commerce CTA. Active state deepens fill to `{colors.primary-active}` with no transform or shadow — the weight shift alone signals the press. Disabled state uses `{colors.primary-disabled}` without reducing opacity on the label, keeping text scannable.

**`button-secondary`** — Canvas background with a 1px `{colors.primary}` border and matching text; same uppercase `{typography.button-md}` as primary. Hover transitions background to `{colors.surface-soft}` and border to `{colors.primary-active}`. Used for secondary catalog actions such as "Download Spec Sheet" or "Find a Dealer" placed alongside a primary "View Collection."

**`button-text-link`** — Transparent background, `{colors.ink}` text, underlined, `{typography.button-sm}` uppercase. Reserve for in-body text links and footer utility navigation where a bordered button would over-weight the page hierarchy.

### Text Input

**`text-input`** — 1px `{colors.hairline}` border at rest, advancing to 1px `{colors.primary}` on focus with no animated glow. Placeholder in `{colors.muted}`. `{rounded.xs}` corners match button geometry, keeping the form language consistent. Height is 48px throughout — adequate for fabric-covered fingers but not oversized relative to the product photography it sits beside.

### Navigation

**`nav-bar`** — 72px tall, `{colors.canvas}` background, bottom hairline border. Logo anchors left; primary category links (Collections, Dining, Seating, Occasional, Covers & Accessories) centered in `{typography.nav-link}` uppercase at 12px/1px tracking; search icon, account, and dealer-locator anchors right. No cart icon — the brand sells through dealers and direct inquiry, not a checkout cart.

**`mega-menu`** — Full-width panel expanding below the nav bar with a top and bottom `{colors.hairline}` border; no drop shadow. Columns organized by material type (Wrought Iron, Aluminum, All-Weather Wicker) with collection thumbnail grids inside each. Body text in `{typography.body-sm}`. Closes on outside click; no animation delay longer than 150ms.

**`category-rail`** — Sticky 48px bar appearing on collection listing pages. Links in `{typography.nav-link}` muted at `{colors.muted}`, active link advances to `{colors.ink}` with a 2px bottom border in `{colors.primary}`. Scrolls horizontally on mobile without wrapping.

### Product Card

**`product-card`** — No border radius, no card shadow — the image sits flush on the page surface. 4:3 image aspect ratio favors outdoor lifestyle photography over tight product-only shots. Below the image: collection name in `{typography.title-sm}` uppercase at `{colors.muted}`, product name in `{typography.title-md}` at `{colors.ink}`, price in `{typography.price-display}`, and a `{typography.finish-label}` count of available finishes ("14 Finishes"). No hover overlay on the image; the entire card is clickable.

### Finish Swatches

**`finish-swatch`** — Rectangular chip with 1px `{colors.hairline}` border, no radius, short finish name in `{typography.finish-label}` uppercase. Selected state switches border to 1px `{colors.primary}`. Chips arrange in a single horizontal scroll row on mobile PDPs; on desktop they wrap to a max of two rows before collapsing to a "Show All" toggle. Swatches represent powder-coat names (Textured Black, White Sand, Hammered Pewter) rather than color swatches alone — the name carries more information than a paint chip.

### Hero

**`collection-hero`** — Full-bleed lifestyle photograph with a `{colors.scrim}` overlay at 42% opacity to ensure legibility. Collection name renders in `{typography.display-xl}` white, optionally with a sub-caption in `{typography.body-md}` white at 80% opacity. A single `button-primary` or `button-secondary` CTA anchors bottom-left on desktop; on mobile it drops to the bottom of the block outside the image. Minimum height 560px desktop, 400px mobile.

### Heritage & Material Badges

**`heritage-badge`** — Small rectangular chip in `{colors.surface-soft}` with 1px `{colors.hairline}` border, no radius. Text in `{typography.caption}` at `{colors.body}`. Used to surface "Est. 1866," "Made in the USA," or "Lifetime Frame Warranty" claims inline on collection pages and PDPs — treated as a specification, not a marketing stamp.

**`material-badge`** — Slightly smaller than the heritage badge; `{rounded.xs}` radius. Used for material taxonomy labels (Wrought Iron, Cast Aluminum, Woven) on product cards and in filter panels. Text in `{typography.finish-label}` at `{colors.muted}`.

### Price Tag

**`price-tag`** — Price range ("Starting at $1,299") in `{typography.price-display}` (Georgia, 20px) at `{colors.ink}`. No strikethrough price or sale badge treatment unless a promotional event is active. The serif renders the number with more gravity than a sans-serif would at the same size.

### Breadcrumb

**`breadcrumb`** — `{typography.caption}` links in `{colors.muted}` separated by a slash or chevron in `{colors.hairline}`; active/current page advances to `{colors.ink}` without a link underline. Placed 16px above the collection heading on PDPs and listing pages.

### Footer

**`footer`** — Full-width `{colors.primary}` (#313131) background with `{colors.on-primary}` text throughout. Four to five link columns (Collections, Resources, About, Dealer Locator, Care & Warranty) in `{typography.body-sm}`. "Est. 1866" rendered in `{typography.caption}` at full white opacity in the bottom strip alongside copyright and legal links. Social icons as 20px inline SVGs in white. No footer newsletter form — lead capture is routed to a dealer-contact flow.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; full-bleed hero at 400px min-height; mega-menu becomes full-height left drawer; swatch strip scrolls horizontally; category rail collapses behind a "Browse" toggle |
| Tablet | 744–1128px | Two-column product grid; nav-bar collapses logo+hamburger on the left, key CTA on right; hero text bumps down to display-lg; category-rail visible horizontally |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with mega-menu; sticky category rail active; collection-hero at full 560px; breadcrumb visible |
| Wide | > 1440px | Max content width 1440px centered on a canvas background; four-column product grid on listing pages; hero image scales to fill with object-fit cover |

### Touch Targets

- All interactive elements (swatch chips, nav links, icon buttons) maintain minimum 44×44px hit area regardless of visible size
- Swatch chips expand to 36px height on mobile even if label is small
- The category-rail links receive 12px vertical padding on touch viewports

### Collapsing Strategy

- Mega-menu collapses to a full-height slide-in drawer at < 1128px; top-level categories are accordion-expanded
- Finish swatches collapse from a two-row grid to a single horizontal scroll strip at < 744px
- Footer columns collapse to a single-column accordion at < 744px; "Est. 1866" strip remains visible at the bottom
- Collection hero headline drops from `display-xl` (52px) to `display-md` (28px) on mobile
- Breadcrumb is hidden at < 744px to reduce header clutter on small PDPs

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Sparse color extraction**: only one hex color (#313131) was recovered; the live site returned an anti-bot interstitial ("Just a moment…") during extraction. The full brand palette — any accent, highlight, or promotional color — is unconfirmed.
- **No custom typeface detected**: extraction returned only system font stacks. The serif display pairing (Georgia, 'Times New Roman') is an inference from heritage brand positioning and was not observed in the live site's CSS. Woodard may use a licensed web font not visible during extraction.
- **No meta theme-color defined**: mobile browser chrome color unknown.
- **No accent or promotional color confirmed**: a warm bronze or ochre accent is plausible for a heritage patio brand but was not extracted and is therefore absent from the palette.
- **Component-level measurements unverified**: button heights, card gap widths, and exact border radii are design-system inferences, not measurements taken from the live site.
- **Checkout and dealer-locator flows unobserved**: Woodard's primary conversion path runs through dealer contact rather than a standard e-commerce checkout; the precise form and CTA patterns for that flow are not documented here.
- **Icon set and illustration style unknown**: nav icons and decorative elements (if any) could not be captured behind the anti-bot gate.
