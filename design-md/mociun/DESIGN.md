---
version: alpha
name: "Mociun"
source_url: "https://www.mociun.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Warm cream (#f4f2f1) fills the canvas like unbleached linen laid beneath a tray of unmounted stones — the ground against which Mociun's terracotta signature (#9e483f) and amber-gold accents (#ca934d, #d5b961) read as geological rather than decorative. Three type families layer into a hierarchy that mirrors the brand's material specificity: Ogg's high-contrast display serifs carry the largest headlines; BeausiteFit holds editorial subheadings and product titles in its fitted, book-weight cut; BeausiteSlick's hairline and thin weights handle nav labels and captions at their most refined; and Assistant grounds all interactive UI in legible neutral sans. The result is a Brooklyn atelier that communicates in patina and mineral chemistry over flash and spectacle. Primary CTAs land in terracotta (#9e483f) — a muted earth-red drawn from fired clay rather than marketing crimson — placed against the warm neutral canvas with no drop shadows or hard borders, trusting the jewelry itself to supply visual tension. Corners hold sharp or near-sharp edges ({rounded.xs} to {rounded.sm}) throughout forms, cards, and buttons: the flatness frames organically irregular stone shapes without competing with their geometry. The amber and gold tones (#ca934d, #d5b961) function as metallic accents in price emphasis, hover states, and editorial badges rather than as an all-over gold wash — gesturing toward real metal specificity. Vertical spacing is generous in editorial registers, with section breaks opening to 64px of breath, while the product grid compresses to allow stone comparison. Detail pages lean text-heavy: cut, carat, stone origin, and setting material surface directly in the product description rather than behind collapsed menus. A warm near-black (#121212) anchors primary ink, keeping Ogg headlines from reading harsh against the cream ground, while a soft gray (#444444) handles body weight where the serif might otherwise overpower supporting copy.

colors:
  primary: "#9e483f"
  primary-active: "#7d3831"
  primary-disabled: "#d4a49f"
  ink: "#121212"
  body: "#444444"
  muted: "#888888"
  hairline: "#dedede"
  canvas: "#f4f2f1"
  surface-soft: "#f4f2f1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-amber: "#ca934d"
  accent-gold: "#d5b961"
  scrim: "#00000066"

typography:
  display-xl:
    fontFamily: "'Ogg', Georgia, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.07
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'BeausiteFit-Regular', 'BeausiteFit-Light', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'BeausiteSlick-Light', 'BeausiteSlick-Regular', Georgia, serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "'BeausiteFit-Regular', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'BeausiteSlick-Regular', Georgia, serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0.04em
  body-md:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.01em
  button-md:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.14
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.17
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'BeausiteSlick-Regular', 'BeausiteSlick-Light', Georgia, serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0.03em
  price:
    fontFamily: "'BeausiteFit-Regular', Georgia, serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-caps:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.12em
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
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
    padding: "12px 28px"
    height: 44px
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
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "11px 27px"
    height: 44px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.body}"
    padding: "10px 14px"
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspectRatio: "1/1"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    maxWidth: 1280px
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-caps}"
    height: 36px
  product-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  stone-detail-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.label-caps}"
    valueTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-md}"
    padding: "{spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    paddingBottom: "{spacing.xxl}"
    borderBottom: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px"
    height: 42px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    paddingVertical: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — Terracotta (#9e483f) fill on warm cream, uppercase tracking at 0.08em via `{typography.button-md}`, with near-flush `{rounded.xs}` corners that match the brand's aversion to soft edges. Active state steps to `{colors.primary-active}` (#7d3831); disabled washes to `{colors.primary-disabled}` (#d4a49f). No shadow or outline — the filled earth-red alone signals interactivity against the cream canvas.

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` border at `{rounded.xs}`, matched to `button-primary` in height and padding so primary/secondary pairings sit flush side by side. Near-black (#121212) text on cream reads as a quieter alternative without introducing any new surface color.

**`button-ghost`** — No border, no fill, underlined ink text at `{typography.button-sm}` with uppercase tracking. Used inline within product descriptions and editorial blocks where a bordered button would interrupt reading flow; relies entirely on underline and hover state for affordance.

### Navigation

**`nav-bar`** — 60px height, cream canvas background, 1px hairline bottom border. Nav links use `{typography.nav-link}` (BeausiteSlick-Regular, 13px, 0.03em tracking) — the serif weight distinguishes navigation from the Assistant-stack body text below. Logo centered or left-anchored; cart, search, and account icons sit right at 20px with 44px touch targets.

**`announcement-bar`** — Near-black (#121212) strip at 36px holding `{typography.label-caps}` (Assistant, 11px, all-caps, 0.12em tracking) in canvas white. Anchored above the nav; used for shipping thresholds and stone availability notices.

### Product Card

**`product-card`** — Square 1:1 image crop at `{rounded.none}`, no border, no shadow. Title in `{typography.title-md}` (BeausiteFit-Regular, 16px), price in `{typography.price}` (BeausiteFit-Regular, 15px), material or stone note in `{typography.caption}` (Assistant, 12px). On hover a secondary image may swap in; no color overlay or scrim is introduced over the image. Cards sit in a 2-col (mobile) to 4-col (desktop) grid with tight `{spacing.sm}` gutters so adjacent stones can be compared at a glance.

### Hero

**`hero-banner`** — Full-width cream canvas with headline in `{typography.display-xl}` (Ogg, 56px, weight 400, -0.5px tracking). Subhead in `{typography.display-sm}` (BeausiteSlick-Light, 22px). Supporting copy in `{typography.body-md}` (Assistant). Vertical padding at `{spacing.section}` (64px) prevents crowding the first content row. No decorative overlays — the type and a single centered product image carry all editorial weight.

### Badges

**`product-badge`** — Amber (#ca934d) fill, canvas white text at `{typography.caption}`, `{rounded.xs}` corners, 3px 8px padding. Used for "New", "One of a Kind", and "Made to Order" labels. Amber is used here deliberately rather than terracotta to avoid competing with primary CTAs; the distinction codes availability rather than action.

### Stone Detail Panel

**`stone-detail-panel`** — A cream surface-soft block below the product images that surfaces stone origin, cut, carat weight, and setting metal in a two-column definition layout: `{typography.label-caps}` (Assistant, 11px, all-caps) for field names, `{typography.body-sm}` (Assistant, 13px) for values. Separated from the product title zone by a 1px hairline. This panel is the brand's primary differentiator — it treats purchasing a ring like reading a provenance record, and it should never be collapsed or hidden behind an accordion on desktop.

### Collection Header

**`collection-header`** — Typographic-only category page header with headline in `{typography.display-md}` (BeausiteFit-Regular, 32px) and an optional editorial paragraph in `{typography.body-md}`. A 1px hairline bottom border separates the header from the product grid below. No hero images at the collection level; the type alone introduces each category.

### Search

**`search-bar`** — Surface-soft background, 1px hairline border, `{rounded.sm}`, Assistant body-md stack for the placeholder. Expands to a full-width modal overlay on mobile. Icon in `{colors.muted}` (#888888); no filled color on the icon itself. Search suggestions surface in a borderless dropdown below at `{rounded.xs}` with `{spacing.sm}` row padding.

### Footer

**`footer`** — Cream canvas background, 1px hairline top border. Four-column layout on desktop (About, Shop, Customer Care, Newsletter). Section headings in `{typography.title-sm}` (BeausiteSlick-Regular, 13px, 0.04em tracking), links in `{typography.body-sm}` (Assistant, 13px). Newsletter sign-up reuses the `text-input` spec paired with `button-primary`. Legal line in `{typography.caption}` at full width below the column grid.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | 1-col product grid; hero headline drops to 36px Ogg; nav collapses to hamburger with full-screen drawer; announcement bar single-line marquee; stone detail panel single-column stacked |
| Tablet | 744–1128px | 2-col product grid; hero at 44px; nav shows top-level categories, dropdowns on tap; collection header description truncates to 2 lines |
| Desktop | 1128–1440px | 3–4-col product grid; full nav with hover dropdowns; hero at 56px; stone detail panel in 2-col definition grid; footer in 4-col layout |
| Wide | > 1440px | Max-width 1280px centered; horizontal padding increases to maintain reading measure; product grid stays 4-col |

### Touch Targets

- All buttons minimum 44px height regardless of visual size
- Product card tap area covers the full image block and text row beneath it
- Nav links minimum 44px tap height even at 13px serif type size
- Cart, search, and account icons padded to 44×44px touch areas
- Stone detail panel field rows minimum 36px tap height on mobile

### Collapsing Strategy

- Product grid: 4-col → 3-col (1128px) → 2-col (744px) → 1-col (< 744px)
- Nav: full horizontal serif links → hamburger drawer at < 744px
- Footer: 4-col → 2-col (tablet) → 1-col stacked with accordions (mobile)
- Stone detail panel: 2-col definition list → single-column stacked at < 744px; never hidden behind an accordion on desktop
- Hero text: max-width constrained to 640px on desktop, full-bleed at mobile with reduced type scale
- Collection header description: visible on tablet+, collapsed to 0 height on mobile to prioritize grid

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `primary-active` (#7d3831) and `primary-disabled` (#d4a49f) were interpolated from extracted primary #9e483f — not directly observed in the site extraction
- `muted` (#888888) was constructed as a mid-gray; no explicit muted tone appeared in the top-hex list
- `surface-card` (#ffffff) is assumed for product card image backgrounds; pure white was not in the extracted palette
- Exact weight variants of BeausiteFit and BeausiteSlick (Bold vs Regular vs Light) as deployed at each typographic scale could not be confirmed without direct font-asset inspection
- Whether Ogg is the primary display face at the hero level or secondary to BeausiteFit could not be definitively confirmed; this file assumes Ogg leads at display-xl
- Button hover transition duration and easing values not available from extraction
- Focus ring color and style for keyboard navigation not captured
- Whether accent-gold (#d5b961) is used for text, icon, or decorative-only contexts not confirmed
- Logo mark color treatment (terracotta, ink, or metallic) could not be confirmed from extraction
- Mobile-specific type-size overrides for Ogg display headlines not confirmed
