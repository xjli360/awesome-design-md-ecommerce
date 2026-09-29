---
version: alpha
name: "No. 2"
source_url: "https://no2.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The name is already an object: the No. 2 pencil, cedar-bodied, cadmium-yellow, the single implement trusted to fill in Scantron bubbles and draft first novels. No. 2 the brand takes that inheritance and distills it into a paper goods system built around the same modest confidence — nothing decorative that isn't load-bearing. The palette reads like a stationery drawer: warm graphite (#1C1C1A) handles all primary type, a cream-paper canvas (#FEFCF7) serves as the default ground, and a single charge of pencil yellow (#F2C53D) activates every CTA, hover state, and accent mark. Supporting surfaces in #F5F1E8 recall the weight of uncoated stock — cream rather than brilliant white, as though the interface were printed on 80# text. Typography runs in two registers: a display serif for headlines gives the brand the editorial gravity of a printed goods catalog, while a humanist sans-serif handles body copy and UI chrome at weights that stay under 600 so nothing shouts over the objects. Corners are nearly absent — {rounded.xs} on cards and inputs, {rounded.sm} on buttons — because stationery is cut, not molded; precision matters more than softness. Only search and collection badges break to {rounded.full}, the single geometric concession in an otherwise rectilinear system. Spacing follows the logic of a well-margined printed page: {spacing.section} between major content breaks, generous internal padding inside product cards, hairlines used sparingly to separate rather than decorate. The primary CTA uses dark ink on yellow rather than white on color — a firm signal that this is a brand that puts the object first and the interface second.

colors:
  primary: "#F2C53D"
  primary-active: "#D4A820"
  primary-disabled: "#F9E4A0"
  ink: "#1C1C1A"
  body: "#3D3A35"
  muted: "#7A7570"
  graphite-mid: "#888480"
  hairline: "#DDD9D2"
  hairline-soft: "#EAE7E1"
  canvas: "#FEFCF7"
  surface-soft: "#F5F1E8"
  surface-card: "#FFFFFF"
  on-primary: "#1C1C1A"
  kraft: "#C4A882"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', 'Georgia', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Cormorant Garamond', 'Georgia', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  eyebrow:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.4px

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
    padding: "12px 24px"
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "11px 23px"
    height: 44px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: "12px 0"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: "10px 14px"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoHeight: 22px
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.ink}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    gap: "{spacing.sm}"
    imagePadding: "{spacing.base}"
    bodyPadding: "{spacing.base}"
    borderHover: "1px solid {colors.hairline}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.muted}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
    ctaComponent: button-primary
  collection-strip:
    backgroundColor: "{colors.canvas}"
    labelTypography: "{typography.eyebrow}"
    labelColor: "{colors.muted}"
    linkTypography: "{typography.title-md}"
    linkColor: "{colors.ink}"
    gap: "{spacing.lg}"
    paddingVertical: "{spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  badge-limited:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  pdp-atc-bar:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    priceTypography: "{typography.display-md}"
    priceColor: "{colors.ink}"
    ctaComponent: button-primary
    paddingVertical: "{spacing.base}"
    paddingHorizontal: "{spacing.xl}"
    position: sticky
    bottom: 0
  search-overlay:
    backgroundColor: "{colors.canvas}"
    inputComponent: text-input
    resultTitleTypography: "{typography.title-md}"
    resultTitleColor: "{colors.ink}"
    resultBodyTypography: "{typography.body-sm}"
    resultBodyColor: "{colors.muted}"
    matchHighlightColor: "{colors.primary}"
    scrim: "rgba(28, 28, 26, 0.45)"
    padding: "{spacing.lg}"
  newsletter-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    inputComponent: text-input
    ctaComponent: button-primary
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
  footer-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.eyebrow}"
    headlineColor: "{colors.graphite-mid}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.canvas}"
    linkHoverColor: "{colors.primary}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.xl}"

---

## Components

### Buttons

**`button-primary`** — Pencil yellow (#F2C53D) fill with graphite-ink text at `{typography.button-md}`, 4px radius, 44px height. Dark-on-yellow rather than white-on-color: it reads as a foil-stamped paper label rather than a typical digital CTA. Active state deepens to `{colors.primary-active}`; disabled fades to `{colors.primary-disabled}` with muted text, preserving geometry without indicating interactivity.

**`button-secondary`** — Transparent field with a 1px `{colors.ink}` border, matching the primary in height, radius, and typography. Used for subordinate actions such as "View All" or "Save for Later" — the outline weight is the same as a drawn rule, keeping the action legible without competing with yellow.

**`button-ghost`** — Fully transparent, underline only. Inherits `{typography.button-md}` but signals editorial intent rather than transactional urgency. Used inline in body text modules and editorial feature blocks where a bordered button would be too heavy.

### Form Inputs

**`text-input`** — 44px height, `{rounded.xs}` (2px), a `{colors.hairline}` border that sharpens to `{colors.ink}` on focus with no shadow or glow — the transition communicates entirely through line weight. Placeholder text in `{colors.muted}`; typography at `{typography.body-md}`. The narrow rounding keeps the field consistent with the brand's cut-paper geometry.

### Navigation

**`nav-bar`** — A 60px `{colors.canvas}` bar separated from page content by a featherweight `{colors.hairline-soft}` underline. The brand mark sits at 22px height; category links use `{typography.title-md}` weight 500. On mobile the links collapse into a full-screen drawer triggered by a minimal hamburger icon; the search icon and cart count remain pinned in the bar at all breakpoints.

### Cards

**`product-card`** — Image fills the card top on a `{colors.surface-soft}` cream pad with `{spacing.base}` internal padding, so the object floats rather than bleeds. Title renders in `{typography.title-md}`, price in `{typography.body-md}`, secondary descriptors (paper weight, ruling, format count) in `{typography.caption}` / `{colors.muted}`. No lift shadow on hover — instead a `{colors.hairline}` border appears around the entire card, as if the sheet had been drawn forward in a stack of inventory.

### Merchandising

**`hero-banner`** — Cream `{colors.surface-soft}` ground. An `{typography.eyebrow}` uppercase label leads the headline, providing catalog-index context ("New Arrivals — Spring"). Headline in `{typography.display-xl}` at weight 400 — no mechanical exertion. Body copy at `{typography.body-md}` with generous 1.6 line height. Primary CTA below. Padding uses `{spacing.section}` vertically so the module breathes like a printed spread, not a digital banner.

**`collection-strip`** — A full-width horizontal band of named category links (Notebooks, Pencils, Cards, Loose Paper) preceded by an `{typography.eyebrow}` label in `{colors.muted}`. Links use `{typography.title-md}`. Separated from surrounding modules by `{colors.hairline}` top and bottom borders. On mobile converts to horizontal scroll without visible scrollbar.

### Badges

**`badge-new`** — Pill at `{rounded.full}`, `{colors.primary}` fill, `{colors.on-primary}` (graphite ink) text at `{typography.caption}` 11px/500. Positioned in the upper-left corner of the product card image. Reads as a small paper label stickered onto the product rather than a digital notification.

**`badge-limited`** — Identical pill geometry with `{colors.ink}` fill and `{colors.canvas}` text — the same shape, the opposite value. Used to signal scarcity or archive editions without adding alarm color. The two badge types can coexist on a card (stacked vertically) when a new product is also in limited supply.

### Product Detail

**`pdp-atc-bar`** — Sticky bottom bar on mobile: `{colors.canvas}` background, `{colors.hairline}` top border, price at `{typography.display-md}` serif left-aligned, full-width `button-primary` occupying the remaining width. The serif price treatment at display scale creates a deliberate contrast with the utilitarian CTA — price is the object's value; the button is merely a mechanism. On desktop the bar dissolves into the inline right-column layout.

### Discovery

**`search-overlay`** — Triggered from the nav icon, expands as a full-width panel over a `rgba(28, 28, 26, 0.45)` scrim. A single full-width `text-input` sits at the panel top. Results list below with titles in `{typography.title-md}` and subcategory or format descriptors in `{typography.body-sm}` / `{colors.muted}`. Matching characters are highlighted in `{colors.primary}` yellow — the only moment of yellow inside a monochrome result row.

### Marketing

**`newsletter-block`** — A `{colors.surface-soft}` cream band with `{spacing.section}` vertical padding and a `{colors.hairline}` top border. Headline at `{typography.display-md}` serif, body at `{typography.body-md}`. Single `text-input` for email followed immediately by `button-primary`. No legal microtext clutter above the fold; a single `{typography.caption}` line below the input handles consent language.

### Footer

**`footer-nav`** — Dark `{colors.ink}` ground with `{colors.canvas}` text throughout. Column headers in `{typography.eyebrow}` at `{colors.graphite-mid}` — reduced contrast gives a catalog-index feel, like section tabs on a divider card. Nav links in `{typography.body-sm}`, link hover state transitions to `{colors.primary}` yellow — the most legible use of yellow against a dark field. Brand mark and copyright at `{typography.body-sm}` in a bottom-flush row.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; `pdp-atc-bar` becomes sticky bottom bar; `hero-banner` stacks text above or below image; `collection-strip` becomes horizontal scroll; `footer-nav` columns collapse to accordion |
| Tablet | 744–1128px | Two-column product grid; nav shows brand mark and icon set only, category links in drawer; hero adopts split layout (text left, image right at 50/50); `pdp-atc-bar` inline in right column |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav bar with all category links visible; hero at full-bleed with constrained text column (~480px wide); `newsletter-block` two-column (headline left, form right) |
| Wide | > 1440px | Content max-width capped at ~1300px with expanded lateral margins; grid holds at four columns; hero text column constrained for comfortable measure (~55–60 characters); side margins serve as negative space, not wasted canvas |

### Touch Targets
- All interactive elements minimum 44×44px (buttons, inputs, nav icons)
- `collection-strip` links padded to 44px tap height on mobile even when text is smaller
- Badge overlays on product cards are display-only — no tap target needed
- Quantity selectors on PDP minimum 40×40px per control
- Footer accordion toggles on mobile minimum 48px tap height

### Collapsing Strategy
- `nav-bar` category links fold into a full-screen left drawer below 744px; search and cart icons remain in the bar
- `collection-strip` converts from wrapped pill row to single-row horizontal scroll on mobile with momentum scrolling
- `footer-nav` multi-column grid collapses to stacked accordion sections on mobile; expanded state shows links beneath header
- `hero-banner` switches from side-by-side to full-width stacked layout below 744px, image first or text first depending on editorial priority
- `newsletter-block` switches from two-column (headline + form side by side) to single-column stacked below 744px
- Product grid drops from four to two columns at tablet breakpoint, then to one column at mobile

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No colors extracted**: The live site returned zero hex values. All palette decisions — pencil yellow (#F2C53D) as primary, graphite (#1C1C1A) as ink, cream (#FEFCF7) as canvas — are inferred from brand-name logic and paper goods category conventions. Every color must be verified against actual brand assets before implementation.
- **No fonts extracted**: Zero font-family stacks were captured from the site. Cormorant Garamond (display) and Neue Haas Grotesk (body) are educated guesses for a premium paper goods aesthetic. Actual typefaces must be confirmed from brand style guide or network inspection.
- **Non-Shopify platform**: The site does not appear to run on Shopify; cart drawer behavior, variant selectors, and checkout flow patterns may differ substantially from standard DTC conventions modeled here.
- **No meta theme-color**: Mobile browser chrome color is unknown; defaulting to `{colors.canvas}` (#FEFCF7) is a reasonable assumption but unconfirmed.
- **Logo and wordmark treatment unknown**: Size, weight, capitalization style, and any logotype vs. wordmark distinction for the No. 2 mark could not be observed. The nav spec uses a placeholder height of 22px.
- **Interaction and animation unconfirmed**: Hover transitions, drawer animation timing, card hover behavior, and any scroll-triggered effects are inferred from category conventions, not observed on the live site.
- **Navigation structure uncertain**: The number of top-level category links, presence of a megamenu, and any editorial or journal section in the nav are unknown.
