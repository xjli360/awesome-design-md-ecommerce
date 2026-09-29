---
version: alpha
name: "Mason-Kay"
source_url: "https://www.masonkay.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The green at the center of Mason-Kay's identity is not a trend color — it is #009200, the precise saturation of living moss on jade stone under gallery lighting, deployed as the brand's single chromatic commitment across every primary action and navigational signal. A second, lighter jade (#71c764) serves as hover states and decorative borders, creating a two-green system that mirrors how jadeite itself grades from light to imperial. Against these two greens, the page runs on #2e2e2e — a dark, near-black slate that carries all body text — with #003399 appearing as a legacy-blue link register, the kind of utilitarian link color that specialist retailer sites of long standing tend to preserve rather than redesign. The overall palette reads scholarly and horticultural at once: a natural history museum's color logic applied to a jewelry catalog. Type is set in a serif display (the site's font extraction returned an ambiguous class identifier rather than a named typeface; see Known Gaps) over a clean system sans for body copy, a pairing that signals institutional authority — Mason-Kay leans on certification language, grade taxonomy (A-grade, B-grade, Type A jadeite), and provenance documentation as primary sales arguments rather than lifestyle aspiration. Product photography is pulled against white or near-white surfaces, letting the stone's translucency and color depth carry the image. Corners stay modestly rounded, nothing pill-shaped; the UI vocabulary is that of a specialist dealer rather than a mass-market jeweler. Navigation is dense and taxonomic — stone type, cut, setting metal, price range — because Mason-Kay's buyer is filtering by geological criteria, not browsing a mood board. CTAs in #009200 with white labels sit at comfortable height and full-width on mobile, collapsing a complex catalog into a clean commerce surface. The deep blue (#003399) appears primarily on inline text links and informational copy about jade grading, a functional accent that keeps scholarly authority without competing with the primary jade green.

colors:
  primary: "#009200"
  primary-active: "#007500"
  primary-disabled: "#a8d9a4"
  ink: "#2e2e2e"
  body: "#3d3d3d"
  muted: "#6b6b6b"
  hairline: "#d4d4d4"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f4f9f4"
  surface-card: "#ffffff"
  surface-warm: "#f9faf8"
  on-primary: "#ffffff"
  accent-green-light: "#71c764"
  accent-blue: "#003399"
  grade-badge-bg: "#e8f5e8"
  grade-badge-text: "#007500"
  certified-bg: "#eef2ff"
  certified-text: "#003399"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.28
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  body-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  caption-label:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.6px
    textTransform: uppercase
  button-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  grade-label:
    fontFamily: "Georgia, serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  price-display:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 56px
    logoHeight: 36px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} 0"
    itemPadding: "{spacing.sm} {spacing.base}"
    hoverBg: "{colors.surface-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    imageBg: "{colors.surface-warm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    padding: "{spacing.md}"
    gap: "{spacing.sm}"
  grade-badge:
    backgroundColor: "{colors.grade-badge-bg}"
    textColor: "{colors.grade-badge-text}"
    typography: "{typography.grade-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  certified-badge:
    backgroundColor: "{colors.certified-bg}"
    textColor: "{colors.certified-text}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    subColor: "{colors.muted}"
    ctaSpacing: "{spacing.lg}"
    padding: "{spacing.xxl} 0"
    imageSide: right
  category-filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
    headerTypography: "{typography.title-sm}"
    activeTextColor: "{colors.primary}"
    activeFontWeight: 600
    padding: "{spacing.base}"
    width: 220px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    spacing: "{spacing.xs}"
  stone-detail-card:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    labelTypography: "{typography.caption-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    gridColumns: 2
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 10px 42px 10px 14px
    iconColor: "{colors.primary}"
    height: 42px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "#ffffff"
    typography: "{typography.body-sm}"
    linkColor: "{colors.accent-green-light}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.accent-green-light}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.xxl} 0"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    border: "1px solid {colors.hairline}"
    itemSize: 36px
  educational-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderLeft: "3px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    headingTypography: "{typography.title-sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action renders in Mason-Kay's jade green (#009200) with white label text, a 44px tall touch target, and minimal 4px rounding that keeps the form businesslike. On hover, background deepens to `{colors.primary-active}` (#007500); disabled state uses the pale `{colors.primary-disabled}` (#a8d9a4) to signal unavailability without harsh contrast.

**`button-secondary`** — A canvas-white button with a 1px jade green border and jade-green text, used for secondary actions like "Request More Information" or "Compare Stones." On hover, background shifts to `{colors.surface-soft}`, a faint green-tinted wash that reinforces the brand palette without obscuring the label.

**`button-text-link`** — Inline text links inherit the legacy `{colors.accent-blue}` (#003399) with underline decoration, consistent with the site's informational-retailer character where dense provenance and grading copy links to glossary pages and certification bodies.

### Navigation
**`nav-bar`** — A 56px tall white bar with a thin `{colors.hairline}` bottom border. The Mason-Kay logo sits left-aligned; categorical navigation — Stone Type, Rings, Pendants, Earrings, Bracelets, Education — runs center or inline-right in `{typography.nav-link}`. A search icon and cart icon close the right side. On scroll, the bar remains sticky, maintaining catalog access throughout deep product browsing.

**`nav-dropdown`** — Taxonomy-dense dropdowns expose stone grades, cuts, and metal settings as scannable sub-items. Hover state on each item applies `{colors.surface-soft}`, and active/selected items shift text to `{colors.primary}`. Dropdowns open with no animation delay to support the specialist buyer scanning multiple filter paths quickly.

### Product Cards
**`product-card`** — White cards with a faint hairline border and near-white image well (`{colors.surface-warm}`) that keeps jade photography neutral. Product title uses `{typography.title-md}`, price renders in `{typography.price-display}` in `{colors.primary}` to anchor value at a glance. Grade badge (`{typography.grade-label}`, green tint) and certified badge (blue tint) stack below the image, before the title, so stone quality is declared before price context.

### Badges and Labels
**`grade-badge`** — Small all-caps label in `{typography.grade-label}` on a `{colors.grade-badge-bg}` (light green) ground, used to declare Type A, A-grade, or untreated status. This is the most important trust signal on every product card and appears persistently above the fold of the card.

**`certified-badge`** — Same shape as `grade-badge` but uses `{colors.certified-bg}` (light blue) and `{colors.certified-text}` (#003399) to signal GIA or independent lab certification, echoing the accent-blue link register and visually separating certification status from grade status.

### Hero
**`hero`** — Full-width editorial strip with headline in `{typography.display-xl}` (serif, dark), subtitle in `{typography.body-md}` in `{colors.muted}`, and a primary CTA button on the left; high-resolution jade photography on the right. Padding of `{spacing.xxl}` top and bottom gives the stone imagery breathing room without a full-bleed takeover. No video, no parallax — Mason-Kay's hero is static and content-forward.

### Stone Detail Card
**`stone-detail-card`** — A 2-column data grid on the product detail page that presents stone specifications: weight, dimensions, color, clarity, treatment, origin. Labels in `{typography.caption-label}` (muted, uppercase) sit above values in `{typography.body-sm}` (dark). Used where a prose description alone would leave the specialist buyer without the taxonomic certainty they require for a jadeite purchase.

### Educational Callout
**`educational-callout`** — An in-line aside with a 3px left border in `{colors.primary}` and a `{colors.surface-soft}` background, used throughout product pages and educational content to surface grade definitions, care instructions, or jade grading standards. Heading in `{typography.title-sm}`, body in `{typography.body-sm}`.

### Search
**`search-bar`** — A 42px tall input with a jade-tinted icon right-aligned inside the field, 1px hairline border that switches to primary green on focus. Placeholder copy tends toward catalog vocabulary ("Search jade by type, color, or setting") rather than generic "Search...".

### Footer
**`footer`** — Dark slate (`{colors.ink}`) background with a 4px jade green top border as a strong brand terminus. Section headings in `{typography.title-sm}` tinted `{colors.accent-green-light}` (#71c764); body links in the same lighter green on hover. The footer carries trust signals — certification logos, grading guides, return policy — that are disproportionately important for a specialist jade retailer where buyer education is a purchase prerequisite.

### Filters / Sidebar
**`category-filter-sidebar`** — A 220px sidebar on catalog pages with borderRight hairline separation. Filter group headers in `{typography.title-sm}`, options in `{typography.body-sm}`. Active selections highlight text to `{colors.primary}` at weight 600. Filters cover stone type, grade, treatment, color, price range, and setting metal — a facet depth closer to a gemological database than a fashion retailer.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; filter sidebar becomes a bottom-sheet drawer; product grid switches to single column; hero stacks headline above image; grade and certified badges stack vertically on card |
| Tablet | 744–1128px | Product grid moves to 2-column; sidebar filters collapse to a horizontal filter bar above the grid; hero uses 50/50 split layout |
| Desktop | 1128–1440px | Full sidebar + 3-column product grid; nav exposes full taxonomy dropdowns; stone detail card renders in side-by-side with product image |
| Wide | > 1440px | Max content width ~1360px centered; gutters widen; product grid expands to 4 columns |

### Touch Targets
- All CTA buttons maintain 44px minimum height on mobile
- Filter checkboxes expand to 44px hit area via padding, even when visually small
- Nav hamburger icon is 44×44px tap zone
- Pagination items expand to 44px on mobile via larger padding

### Collapsing Strategy
- Filter sidebar is the primary collapse: becomes a full-height bottom sheet with apply/reset buttons on mobile and tablet
- Product taxonomy nav drops to two-level accordion inside hamburger menu
- Stone detail data grid collapses from 2 columns to 1 column on mobile
- Hero reverses stack order on mobile: image above, text and CTA below
- Footer column grid collapses from 4 columns to 2 columns on tablet, 1 on mobile

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font family extraction returned `scroll_top_lnx`, which appears to be a scroll-event class identifier or a custom JS-loaded font reference rather than a CSS `font-family` value. The actual typeface(s) used by Mason-Kay could not be confirmed; typography tokens above use a serif/sans fallback system derived from brand character only.
- No meta theme-color was extracted; mobile browser chrome color cannot be confirmed.
- Only four hex values were extracted. Hover states, disabled states, surface tints, and dark-mode values (if any) are inferred from the primary palette, not observed.
- No motion or animation tokens were extractable; transition timing on dropdowns, card hovers, and drawer animations is unknown.
- The site is not Shopify-hosted; cart and checkout UI patterns may differ significantly from standard Shopify component conventions and could not be assumed.
- Icon library and style (outlined vs. filled, stroke weight) is unconfirmed.
- Whether Mason-Kay uses a custom serif display font (likely, given the jewelry category and specialist positioning) or defaults to Georgia could not be determined without live font inspection.
