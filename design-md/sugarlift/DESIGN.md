---
version: alpha
name: "Sugarlift"
source_url: "https://www.sugarlift.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Sugarlift's entire interface runs on a single axis of light — from #141414 at the darkest to #fafafa at the palest — with no chromatic accent anywhere in the extracted palette. This is not minimalism by default but a deliberate act of curation: a gallery that withholds color from its own chrome so that every painting, photograph, and mixed-media piece can carry its own luminance without competition. The nav, cards, and footers dissolve into a continuous near-white canvas ({colors.canvas}), and the only thing holding visual weight is the art itself.

  Geist Sans — Vercel's geometric neutral — serves as the sole text typeface, chosen for its optically even width at display sizes and sturdy x-height in body copy. The monospace stack (Menlo, Consolas, Courier New) surfaces in catalog numbers, edition details, and provenance fields, creating a document-register contrast against editorial prose that makes metadata feel archival rather than commercial. Headings run at light or regular weight with generous tracking; nothing fights for attention at the typographic level either.

  Radius is nearly absent: artwork cards and CTAs use {rounded.none} or {rounded.xs}, echoing the clean-edged frames of physical gallery walls. The only soft shape is the browse filter chip, which takes {rounded.full} to signal an interactive, removable facet distinct from institutional content. Buttons on primary actions — inquiry, purchase, waitlist — are square-shouldered, reinforcing the institutional register expected of a gallery handling significant transactions.

  Spacing reads like white-glove installation: generous padding inside artwork cards, wide gutters between grid items, and long scroll-sections that treat each work as if it occupies its own wall. The hairline ({colors.hairline}: #e5e7eb) separates sections without noise. Muted labels in #9ca3af carry metadata — artist nationality, medium, dimensions — while title and price-on-request breathe freely above them. The result is a screen that behaves more like a printed gallery catalog than a typical e-commerce grid.

colors:
  primary: "#111827"
  primary-active: "#141414"
  primary-disabled: "#9ca3af"
  ink: "#111827"
  body: "#374151"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-soft: "#f3f4f6"
  border-light: "#d1d5db"
  canvas: "#ffffff"
  surface-soft: "#f3f4f6"
  surface-card: "#fafafa"
  surface-warm: "#f1f1f0"
  on-primary: "#ffffff"
  dark: "#1f2937"
  mid: "#4b5563"

typography:
  display-xl:
    fontFamily: "geistSans, 'geistSans Fallback', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "geistSans, 'geistSans Fallback', sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "geistSans, 'geistSans Fallback', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "geistSans, 'geistSans Fallback', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "geistSans, 'geistSans Fallback', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "geistSans, 'geistSans Fallback', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "geistSans, 'geistSans Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "geistSans, 'geistSans Fallback', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  button-md:
    fontFamily: "geistSans, 'geistSans Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.02em
  button-sm:
    fontFamily: "geistSans, 'geistSans Fallback', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.02em
  label-mono:
    fontFamily: "Menlo, Consolas, 'Courier New', 'Liberation Mono', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  nav-link:
    fontFamily: "geistSans, 'geistSans Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  artwork-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    padding: "{spacing.md}"
    titleTypography: "{typography.title-sm}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
  artist-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    imageAspectRatio: "1/1"
    rounded: "{rounded.none}"
    nameTypography: "{typography.title-md}"
    metaTypography: "{typography.body-sm}"
    metaColor: "{colors.muted}"
  exhibition-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    imageAspectRatio: "16/9"
    rounded: "{rounded.none}"
    titleTypography: "{typography.display-sm}"
    dateTypography: "{typography.caption}"
    dateColor: "{colors.muted}"
    borderBottom: "1px solid {colors.hairline}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    subColor: "{colors.body}"
    paddingVertical: "{spacing.section}"
  artwork-detail:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-sm}"
    artistTypography: "{typography.title-md}"
    metaTypography: "{typography.label-mono}"
    metaColor: "{colors.muted}"
    priceTypography: "{typography.title-md}"
    dividerColor: "{colors.hairline}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    border: "1px solid {colors.border-light}"
  catalog-tag:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.label-mono}"
    border: "1px solid {colors.border-light}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  inquiry-form:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl}"
  section-divider:
    borderColor: "{colors.hairline}"
    marginVertical: "{spacing.section}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.xxl}"

## Components

### Buttons
**`button-primary`** — A stark near-black (#111827) rectangle with square corners ({rounded.none}), 44px tall with 24px horizontal padding. The gallery's sole CTA color is its typographic default: no brand accent, just inverted ink on canvas. Hover deepens to `{colors.primary-active}` (#141414); disabled state softens to `{colors.primary-disabled}` (#9ca3af) without disrupting the grayscale palette.

**`button-secondary`** — White canvas with a 1px ink border and the same square geometry as primary. Used for secondary actions — "Save to Collection," "Share," "Download Press Release" — placed beside a primary inquiry button. On dark surfaces (footer, dark modal overlays) border and text invert to canvas (#ffffff).

**`button-ghost`** — Transparent background with ink text, no border. Used inline for "View Artist Profile," "See All Exhibitions," and contextual navigations where a full button frame would add visual weight against white canvas.

### Text Inputs
**`text-input`** — 44px tall, {rounded.xs} corners, 1px hairline border (#e5e7eb) at rest sharpening to full ink (#111827) on focus. Placeholder in `{colors.muted}` (#6b7280). Used in the artwork inquiry form, newsletter signup, and collector login. Inside `inquiry-form`, fields sit on `{colors.surface-warm}` (#f1f1f0) background creating a tonal separation from the main canvas without introducing a new color.

### Navigation
**`nav-bar`** — 64px fixed bar on white canvas, separated from content by a 1px hairline (#e5e7eb). Wordmark sits left in `{typography.title-md}` weight. Center links (Artists, Exhibitions, Artworks, Fairs) in `{typography.nav-link}` at 14px/400 weight — deliberately unassertive, not competing with the art below. Right side holds a search icon and collector login. Navigation flows to full browse pages rather than dropdown megamenus.

### Cards
**`artwork-card`** — Portrait-oriented (3:4 ratio) image with zero radius on near-white `{colors.surface-card}` (#fafafa). Below the image: artwork title in `{typography.title-sm}`, artist name and medium in `{typography.caption}` at `{colors.muted}`. Price shown as "Price on Request" in the same caption style, or a formatted figure for listed works. Hover reveals a thin ink overlay at ~8% opacity with a centered inquiry CTA.

**`artist-card`** — Square (1:1) artist portrait on `{colors.surface-soft}`, name in `{typography.title-md}`, gallery affiliation or represented-since note in `{typography.body-sm}` at muted. Used in the Artists grid and as a sidebar module on artwork detail pages.

**`exhibition-card`** — Wide (16:9) banner image with no radius on white canvas. Exhibition title in `{typography.display-sm}`, date range and venue in `{typography.caption}` at `{colors.muted}`. A 1px `{colors.hairline}` bottom border separates rows in the exhibitions archive grid, standing in for physical wall divisions.

### Artwork Detail
**`artwork-detail`** — Two-column desktop layout: left holds the zoomable artwork image; right holds a metadata column. Title in `{typography.display-sm}`, artist name as a link in `{typography.title-md}`, then a monospace label stack (`{typography.label-mono}`) for year, medium, dimensions, and edition — all in `{colors.muted}`. A 1px `{colors.hairline}` divider separates the metadata block from the inquiry CTA (`button-primary`) and a "Request Price" secondary button below it.

### Catalog Tag
**`catalog-tag`** — Monospace label in a thin border box ({rounded.xs}, 1px `{colors.border-light}` border). Carries edition numbers ("Ed. 3/15"), media classifications ("Archival Pigment Print"), and provenance markers. The monospace stack (Menlo/Consolas) shifts the register from editorial to documentary — these labels feel stamped rather than designed.

### Filter Chip
**`filter-chip`** — Pill-shaped ({rounded.full}) small buttons for browse facets: Medium, Price Range, Style, Nationality. Inactive: `{colors.surface-soft}` background with a 1px `{colors.border-light}` border and `{colors.body}` text. Active: `{colors.ink}` background with `{colors.on-primary}` text. State transition at 150ms. On mobile these form a horizontally scrolling strip rather than a wrapping grid.

### Hero Section
**`hero-section`** — Full-width white canvas with headline in `{typography.display-xl}` (48px/300 weight) and short editorial sub-text in `{typography.body-md}` at `{colors.body}`. No background imagery on the primary hero — the gallery relies on the artwork grid directly below to supply visual payload. Vertical padding uses `{spacing.section}` (64px) top and bottom.

### Inquiry Form
**`inquiry-form`** — Full-width panel on `{colors.surface-warm}` (#f1f1f0) background with `{rounded.none}` and `{spacing.xxl}` (48px) padding. Fields follow the `text-input` style; the submit button is `button-primary`. Triggered from artwork detail pages and artist pages. The warm off-white background distinguishes the transactional zone from the browse canvas without introducing color.

### Footer
**`footer`** — Dark (`{colors.dark}`, #1f2937) full-width strip with reversed typography: nav links in `{colors.muted-soft}` (#9ca3af), legal text in `{typography.caption}`. Four-column layout on desktop: About, Artists, Exhibitions, Contact/Social. A newsletter signup `text-input` sits at the top of the footer block before the dark zone begins, bridging the canvas-to-dark transition.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column artwork grid; nav collapses to hamburger menu; artwork-card hides medium/price metadata; hero headline drops to display-sm (24px); filter chips horizontal-scroll strip |
| Tablet | 744–1128px | Two-column artwork grid; nav links remain visible (abbreviated labels); artist-card 2-up grid; exhibition cards full-width stacked; artwork-detail stacks image above metadata |
| Desktop | 1128–1440px | Three-column artwork grid; two-column artwork-detail; four-column footer; full nav visible |
| Wide | > 1440px | Content max-width 1440px centered; artwork grid expands to four columns; hero padding increases to 96px top/bottom |

### Touch Targets
- All interactive artwork cards enforce a minimum 44×44px tap target via image-area padding on mobile
- Filter chips are 36px min-height on mobile inside a horizontal scroll container
- Nav icons (search, account) are 44×44px tap areas regardless of rendered icon size
- Primary inquiry CTA stretches full-width below the artwork image on mobile

### Collapsing Strategy
- Artwork grid: 4-col → 3-col → 2-col → 1-col across breakpoints
- Artwork detail: side-by-side → stacked (image above, metadata below) below 1128px
- Footer: 4-col → 2-col → 1-col stacked below 744px
- Exhibition cards: 2-col → 1-col below tablet
- Filter chips: horizontal scroll strip on mobile; wrapping grid on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No chromatic accent or brand hue detected; the entire extracted palette is a Tailwind gray scale — a hover highlight or link color may exist on the live site and was not captured by extraction
- geistSans custom weight axis not confirmed; light (300) and medium (500) weights assigned from the public Geist font axis range
- Exact nav height and card internal padding not measured from live DOM; values follow gallery-site conventions
- Monospace font usage context inferred from font-stack presence only; may be limited to code/CMS fields rather than catalog labels
- Animation and transition timing curves not extracted
- Dark mode support unknown; extracted theme-color (#ffffff) suggests light-only, but the Tailwind + Geist setup may include a dark-class variant
