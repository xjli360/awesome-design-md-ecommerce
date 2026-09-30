---
version: alpha
name: "Lost City NYC"
source_url: "https://lostcitynyc.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Objects arrive at Lost City with mid-century Manhattan still embedded in them — bakelite radios, streamlined chrome fixtures, hand-lettered trade signs salvaged from demolished storefronts. The name is itself the design brief: a city of layered erasures, where what vanished defines what remains. The palette follows this logic of residue. Warm cream surfaces ({colors.canvas}, ~#f4f0e8) read like aged catalog paper rather than digital white; the primary deep terracotta ({colors.primary}, ~#7d3c28) echoes industrial brick and faded awning cloth. Ink stays warmly dark rather than pure black (~#1c1915), preserving the sense of archive rather than interface. Type is set in a humanist serif at modest weights — display headlines run 24–32px at weight 500–600, the scale of a museum placard rather than a banner ad. Product photography carries the visual work; component architecture steps back and lets a 1940s cabinet or a 1960s pendant fixture fill the frame. Corners are present but not pillow-shaped: {rounded.sm} on cards and inputs holds legible structure without borrowing the consumer-tech friendliness of {rounded.full} pill buttons. An inquiry-first purchase model shapes the entire flow — the product card's primary action is not a checkout button but a contact link, so the form component carries more typographic authority than a standard e-commerce conversion screen. Category navigation groups the collection by material and era (furniture, lighting, ceramics, industrial, signage), and the filter bar reads like a reference index rather than a facet tree. The footer doubles as a provenance statement, grounding the brand in Brooklyn and in the American manufacturing century it curates.

colors:
  primary: "#7d3c28"
  primary-active: "#5c2a1b"
  primary-disabled: "#c4967f"
  ink: "#1c1915"
  body: "#3a342e"
  muted: "#7a6e66"
  hairline: "#d5cec5"
  canvas: "#f4f0e8"
  surface-soft: "#ede8df"
  surface-card: "#fafaf7"
  on-primary: "#f4f0e8"
  accent-warm: "#c8a96e"
  accent-warm-soft: "#f0e6d0"
  provenance-tag: "#8b7355"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  category-label:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.5px
  price:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  provenance-note:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
    fontStyle: italic

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
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  inquiry-cta:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-md}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  category-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.category-label}"
    borderBottom: "1px solid {colors.hairline}"
    height: 44px
    gap: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.md}"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    imagePosition: right
    layout: two-column
  era-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 5px 12px
    border: "1px solid {colors.hairline}"
  provenance-badge:
    backgroundColor: "{colors.accent-warm-soft}"
    textColor: "{colors.provenance-tag}"
    typography: "{typography.category-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  price-tag:
    textColor: "{colors.ink}"
    typography: "{typography.price}"
    soldLabelTypography: "{typography.category-label}"
    soldColor: "{colors.primary-disabled}"
  image-gallery:
    backgroundColor: "{colors.surface-soft}"
    thumbnailBorder: "1px solid {colors.hairline}"
    activeThumbnailBorder: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    thumbnailGap: "{spacing.sm}"
  provenance-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.provenance-note}"
    borderLeft: "2px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    linkTypography: "{typography.nav-link}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — A muted terracotta block button set in uppercase sans-serif with 1px letter-spacing, evoking a dealer's rubber stamp rather than a consumer CTA. Active state darkens to `{colors.primary-active}` (#5c2a1b); disabled state renders in `{colors.primary-disabled}`, a washed-out coral. Height is 44px for a comfortable touch target without the oversized 56px slab common in mass-market e-commerce.

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` border and the same uppercase `{typography.button-md}` tracking as primary. Appears alongside `inquiry-cta` on detail pages for actions like "Save" or "Share."

**`button-ghost`** — Underlined `{colors.muted}` text with no background or border, rendered in `{typography.button-sm}`. Used for low-priority navigation links and inline "view all" prompts within category rows.

**`inquiry-cta`** — A terracotta-outlined button replacing the conventional "Add to Cart" action, reflecting the contact-to-purchase model. Text reads "Inquire" or "Make Offer" in the same uppercase tracking as other buttons. Transparent fill with `{colors.primary}` border and text; hover fills to the primary color with `{colors.on-primary}` text.

### Navigation
**`nav-bar`** — 64px tall, `{colors.canvas}` background with a 1px `{colors.hairline}` bottom border. The wordmark "Lost City" sits left-aligned in `{typography.display-md}`; a minimal link row (Shop, About, Contact) runs right in `{typography.nav-link}`. No mega-menu or dropdown — the collection is navigated through the `category-nav` bar below. Mobile collapses the link row to a hamburger toggle.

**`category-nav`** — A secondary horizontal strip beneath the main bar listing collection categories (Furniture, Lighting, Ceramics, Industrial, Signage) in `{typography.category-label}` uppercase. The active category gains a 1px bottom underline in `{colors.ink}`; inactive labels render in `{colors.muted}`. On mobile the strip becomes a horizontally scrollable row.

### Product Card
**`product-card`** — Zero border radius (`{rounded.none}`), consistent with the archival grid aesthetic — no rounding softens the object photograph. Image fills a 4:3 frame with no overlay or gradient; below it the object title renders in `{typography.title-sm}` and the price in `{typography.price}` (italic Georgia, reading like a catalog entry). A `provenance-badge` may appear overlaid at the image bottom-left, tagging the decade, origin, or material. Grid runs three columns on desktop.

### Era and Category Filters
**`era-filter`** — Compact toggle chips in `{typography.button-sm}` with `{rounded.xs}` corners and a 1px `{colors.hairline}` border. Active state fills to `{colors.ink}` with `{colors.on-primary}` text — a stark stamp-like inversion rather than a brand-color highlight. Chips are laid out in a horizontal scroll row below the category nav on mobile.

### Detail Page
**`image-gallery`** — A full-width primary image occupying 55–60% of the viewport width on desktop, with a four-thumbnail strip below it. All frames use `{rounded.none}`; the active thumbnail steps to a 1px `{colors.ink}` border. The gallery area sits on `{colors.surface-soft}` to separate the image field from the page canvas.

**`provenance-panel`** — A sidebar text block in `{typography.provenance-note}` (italic Georgia, 13px) separated from the main content column by a 2px left border in `{colors.hairline}`. Contains the object's documented history, dimensions, condition notes, and period attribution — the most text-dense component on the site. On tablet and below it moves beneath the image gallery as a full-width block.

**`price-tag`** — The price renders inline below the title in `{typography.price}`. Sold items replace the price string with "SOLD" in `{typography.category-label}` uppercase at `{colors.primary-disabled}`, preserving the archival document register rather than graying out to opacity or adding strikethrough.

### Hero
**`hero-banner`** — An editorial two-column layout on desktop: headline in `{typography.display-xl}` left-aligned on a `{colors.surface-soft}` ground, with a full-bleed object photograph at right. No gradient overlay, color wash, or text-on-image treatment — the object is presented cleanly against a neutral field. Vertical padding runs `{spacing.section}` top and bottom. On mobile the layout stacks with the photograph above and the headline below.

### Provenance Badge
**`provenance-badge`** — A small pill-tag using `{colors.accent-warm-soft}` fill and `{colors.provenance-tag}` text in `{typography.category-label}` uppercase. Values include decade ("1940s"), origin ("American Made"), or material ("Cast Iron"). Appears as an image overlay on product cards and as an inline tag in detail page headers.

### Footer
**`footer`** — Dark `{colors.ink}` ground with reversed `{colors.canvas}` text. Three columns on desktop: a brand provenance statement in `{typography.caption}`, navigation links in `{typography.nav-link}`, and contact/address details. The tonal shift to near-black reinforces the archival seriousness of the brand and doubles as a visual anchor for long browse pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; `category-nav` and `era-filter` scroll horizontally; `hero-banner` stacks image-above/text-below; `nav-bar` collapses to wordmark + hamburger; `provenance-panel` moves inline below image gallery |
| Tablet | 744–1128px | Two-column product grid; `category-nav` wraps to two lines if needed; `hero-banner` maintains two columns at reduced padding; detail page becomes single column with `provenance-panel` inline |
| Desktop | 1128–1440px | Three-column product grid; full `category-nav` visible in one row; two-column detail layout with fixed `provenance-panel` sidebar at right; `hero-banner` at full editorial proportions |
| Wide | > 1440px | Layout caps at 1440px centered on `{colors.canvas}` margins; optional four-column grid for large collections; `hero-banner` image scales up without distortion |

### Touch Targets
- Minimum 44×44px on all interactive controls: `button-primary`, `inquiry-cta`, `text-input`, `era-filter` chips
- `era-filter` chips maintain at least 8px horizontal gap to prevent mis-taps during horizontal scroll
- `nav-bar` hamburger tap zone is 44×44px regardless of rendered icon size
- `image-gallery` thumbnails have 48px minimum height on mobile

### Collapsing Strategy
- `category-nav` transitions from a fixed horizontal bar to a horizontally scrollable strip pinned below the mobile header
- `provenance-panel` collapses from a right-rail sidebar to a full-width inline block beneath the image gallery on tablet and below
- `footer` columns stack vertically on mobile: brand text first, nav links second, contact last
- `hero-banner` stacks vertically on mobile with image at top cropped to 16:9, headline and body text below

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site (possible JS-rendered tokens, anti-bot protection, or absence of `<meta theme-color>`). All palette values above are inferred from brand-knowledge of the archival antique-dealer aesthetic and the "lost city" editorial identity — treat as provisional pending live extraction.
- No font families were detected in extraction. Typography stacks (Georgia serif for editorial, Helvetica Neue for UI labels) are inferred from the genre; actual fonts may differ significantly, including the possibility of a licensed display typeface.
- Platform is not Shopify; CMS and e-commerce platform are unknown. Component interaction patterns for cart, checkout, and search may vary substantially from what is described here.
- Exact border radii, spacing rhythm, and responsive breakpoints are assumed from category conventions — no computed styles were extracted from the live site.
- Logo and wordmark treatment were not observed; `nav-bar` logo rendering above is speculative.
- Whether prices are displayed publicly or only on inquiry is unknown; the `price-tag` and `inquiry-cta` components above assume a mixed model common to mid-century antique dealers.
- Hover, focus, and keyboard-navigation states for `era-filter` and `category-nav` are inferred from interaction conventions rather than observed behavior.
