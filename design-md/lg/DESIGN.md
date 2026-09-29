---
version: alpha
name: "LG"
source_url: "https://www.lg.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The LG logo — a winking face drawn from two letterforms inside a circle — bets that warmth can survive at appliance scale, and the refrigerators section of lg.com accepts that bet visually without sentimentality. Cherry-red (#a50034) appears exactly once per viewport as the singular CTA or badge voltage, never diffused into accent trails; the rest of the page is a studied white-and-pearl system (#ffffff canvas, #f4f4f4 surface-soft) that lets glass-finish steel product photography do the persuasion. Type runs LG Smart, falling back to Helvetica Neue: display headings land at 48px weight-700 with -0.5px tracking — large enough to anchor a product hero but not so theatrical it collides with the engineering credibility that refrigerator buyers require. Body and specification copy runs at 400 weight, 16px or 14px, dense enough for BTU ratings and drawer configurations without losing readability at small viewport widths. The button geometry is deliberate: primary CTAs use `{rounded.xs}` (4px), hard-edged relative to lifestyle-brand pill conventions, mirroring the rectilinear form factor of the refrigerators themselves. Card shadows are very soft (0 2px 12px rgba(0,0,0,0.08)), keeping the product image dominant and the UI frame invisible. The top navigation switches modes: the main bar is white with ink-colored links, but hover-activated mega-menu panels drop into a dark charcoal (#1a1a1a) field that reframes category browsing as editorial rather than transactional. Energy Star badges render in a cooler forest-green (#4a7c59) to signal environmental credential without competing with the primary red. Comparison UI — a recurring feature in appliance commerce — uses a sticky bottom-of-viewport bar with bordered secondary buttons and checkbox states, keeping multi-SKU decisions visible without occluding product imagery.

colors:
  primary: "#a50034"
  primary-active: "#8a0029"
  primary-hover: "#be0039"
  primary-disabled: "#e8a0b4"
  ink: "#1a1a1a"
  body: "#444444"
  muted: "#767676"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  eco-badge: "#4a7c59"
  new-badge-bg: "#a50034"
  comparison-bar-bg: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-bold:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  spec-label:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  price-display:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  badge:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'LG Smart', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    rounded: "{rounded.xs}"
    padding: 12px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
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
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
    padding: 11px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 28px
  nav-mega-panel:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.xxl}"
  category-tabs:
    backgroundColor: "{colors.canvas}"
    activeTextColor: "{colors.primary}"
    inactiveTextColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    activeBorderBottom: "2px solid {colors.primary}"
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    shadow: "0 2px 12px rgba(0,0,0,0.08)"
    imageAspectRatio: "1 / 1"
  product-card-name:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-spec:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 560px
    imagePosition: right
    padding: "{spacing.section} 0"
  hero-banner-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 600px
  feature-highlight:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    iconSize: 48px
    iconColor: "{colors.primary}"
    padding: "{spacing.section} 0"
    columns: 3
  energy-badge:
    backgroundColor: "{colors.eco-badge}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  new-badge:
    backgroundColor: "{colors.new-badge-bg}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  comparison-bar:
    backgroundColor: "{colors.comparison-bar-bg}"
    textColor: "{colors.ink}"
    shadow: "0 -2px 12px rgba(0,0,0,0.10)"
    position: sticky
    bottom: 0
    padding: "{spacing.md} {spacing.xl}"
    typography: "{typography.body-sm}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTypography: "{typography.title-sm}"
    cellTypography: "{typography.spec-label}"
    borderColor: "{colors.hairline}"
    rowAlternateBackground: "{colors.surface-soft}"
    padding: "{spacing.sm} {spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 48px
    iconColor: "{colors.ink}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 16px"
    activeBackground: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    activeBorder: "1px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — A 48px-tall, 4px-rounded rectangle in LG cherry-red (#a50034) with white weight-600 type at 16px. The near-square radius keeps visual alignment with the rectilinear geometry of the refrigerator SKUs shown alongside; this is a considered departure from lifestyle pill-buttons. Hover shifts to #be0039, active depresses to #8a0029; disabled renders in desaturated pink (#e8a0b4) without hiding the button shape.

**`button-secondary`** — White background with a 1px solid ink (#1a1a1a) border and ink text, 48px tall, matching the primary in height and rounding. Hover fills with `{colors.surface-soft}` rather than inverting — secondary actions receive confirmation, not voltage. Used for "Add to Compare" and "Save to Wishlist" CTAs adjacent to a primary buy button.

**`button-ghost`** — Transparent background, primary-red text, no border, `{rounded.xs}`. Used for "View Details" and "Learn More" within product cards and feature-highlight rows where a bordered button would add excess visual weight.

### Text Input

**`text-input`** — 48px tall, `{rounded.xs}`, 1px `{colors.hairline}` border. Focus state tightens the border to `{colors.ink}` without a glow ring — consistent with LG's preference for contained rather than diffused state signals. Placeholder type in `{colors.muted}` at `{typography.body-md}`.

### Navigation

**`nav-bar`** — 64px white bar with a bottom hairline. The LG logo sits left at 28px height; product-category links run in 14px weight-500 `{typography.nav-link}`; account, search, and cart icons occupy the right rail. On hover, category links open `nav-mega-panel`: a full-width dark charcoal (#1a1a1a) overlay with white type organized in sub-category columns — a visual mode shift from retail to editorial browse that gives the navigation a second identity without a separate dark-mode implementation.

**`category-tabs`** — A 48px horizontal strip beneath the hero for switching between refrigerator sub-types (French Door, Side-by-Side, Bottom Freezer, Counter Depth, etc.). The active tab anchors with a 2px `{colors.primary}` underline and primary-red label; inactive tabs use `{colors.muted}` text with no fill change. No background highlight on selection — the underline alone carries the state signal.

### Product Card

**`product-card`** — White surface with a soft 12px diffused shadow and `{rounded.sm}` corners — no hard border. Internal 16px padding. Product image occupies roughly 60% of card height in a 1:1 aspect ratio. Below: model name in `{typography.title-sm}`, a horizontal row of `spec-badge` chips for capacity and configuration, price in `{typography.price-display}`, and an "Add to Compare" checkbox lower-left. `energy-badge` and `new-badge` tokens float as absolute overlays at the top-left corner of the product image.

### Badges

**`energy-badge`** — Forest-green (#4a7c59) background, all-caps white 11px `{typography.badge}` type, `{rounded.xs}`. Reading "ENERGY STAR" or the efficiency tier. The squared radius aligns with the card geometry and reads as certification rather than marketing flair.

**`new-badge`** — Same dimensions as `energy-badge` but `{colors.primary}` (#a50034) background. Sits top-left of product imagery. Only applied to current model-year SKUs — never stacked with `energy-badge` vertically; they sit in separate positions or are prioritized by editorial.

**`spec-badge`** — Light gray (`{colors.surface-soft}`) chip with bold 12px `{typography.caption-bold}` text. Inline below the product name for quick reads: "29 cu. ft.", "4-Door", "InstaView™". Multiple badges sit in a horizontal flex row with `{spacing.xs}` gaps.

### Hero

**`hero-banner`** — Full-width, minimum 560px tall. Default variant uses `{colors.surface-soft}` with product image right-aligned and headline copy left-aligned in `{typography.display-xl}`. The dark variant (`hero-banner-dark`) flips to `{colors.surface-dark}` for flagship launches or seasonal campaigns, headline and subhead in `{colors.on-dark}`. Neither variant uses a scrim overlay — product images are photographed on matching backgrounds rather than composited over gradients.

### Feature Highlights

**`feature-highlight`** — Three-column section on desktop, each column centered: a 48px icon in `{colors.primary}`, heading in `{typography.display-md}`, and two to three lines in `{typography.body-md}`. Used above the product grid to surface LG ThinQ AI, Door-in-Door, and Craft Ice features. No card borders — columns float on `{colors.canvas}` with `{spacing.section}` vertical padding, relying on whitespace alone to separate sections.

### Comparison Bar

**`comparison-bar`** — Sticky to the bottom of the viewport when two or more products are checked. White background with an upward-facing shadow. Contains product thumbnails (48×48px), model names in `{typography.body-sm}`, a ghost "Remove" action per product, and a `button-primary` "Compare Now" CTA rightmost. Maximum four products; at capacity the checkbox on unchecked cards becomes disabled.

### Spec Table

**`spec-table`** — Appears on product detail pages below the hero. Header row in `{colors.surface-soft}`, alternating content rows in canvas and soft-gray, all borders in `{colors.hairline}`. Headers in `{typography.title-sm}`, values in `{typography.spec-label}` (13px, 400 weight) — technical density appropriate for capacity, compressor type, and connectivity specs without the austerity of a government data table.

### Search

**`search-bar`** — 48px tall, `{rounded.xs}`, surface-soft background with a hairline border. Sits in the nav bar on desktop. On mobile, collapses to a magnifying-glass icon that expands to a full-width overlay input with the same token treatment.

### Filter Chips

**`filter-chip`** — Horizontally scrollable on mobile, wrapping grid on desktop. Default: white background, `{colors.hairline}` border, `{colors.body}` text in `{typography.button-sm}`, `{rounded.full}`. Selected state inverts to `{colors.ink}` background with `{colors.on-dark}` text — the only place the full-pill shape appears in the LG refrigerators UI, creating a clear visual contrast with the otherwise rectilinear button system.

### Footer

**`footer`** — Full-width `{colors.ink}` (#1a1a1a) band. White headings in `{typography.title-sm}`, hairline-gray links in `{typography.body-sm}`. Four columns on desktop: Products, Support, Company, Connect (social icon row). LG logo top-left in white. Legal and regulatory text runs in `{typography.caption}` in `{colors.muted}` on a separate bottom strip with a hairline top border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category-tabs scroll horizontally with active tab snapping to view; hero-banner stacks vertically (image above, copy below); comparison-bar collapses to thumbnail count badge + "Compare" button only; nav links collapse behind hamburger |
| Tablet | 744–1128px | Two-column product grid; hero-banner splits 50/50; feature-highlight drops to two columns; mega-menu panel remains full-width but sub-columns reduce to two |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav-bar with all links visible; feature-highlight at three columns; comparison-bar shows all selected product thumbnails and model names |
| Wide | > 1440px | Content max-width ~1400px centered; hero-banner image may bleed beyond content boundary; product grid holds at four columns |

### Touch Targets
- All buttons minimum 48px tall, 44px wide
- Category tabs 48px tall with full label-width tap target
- "Add to Compare" checkboxes minimum 24×24px hit area with 12px padding buffer around them
- Filter chips minimum 36px tall on mobile
- Hamburger and nav icons minimum 44×44px
- Product card entire surface is tappable on mobile (links to PDP)

### Collapsing Strategy
- Nav links collapse at < 1128px to hamburger; cart, search, and account icons remain at all widths
- Category tab strip becomes horizontally scrollable at < 744px; active tab auto-scrolls into view on mount
- Feature-highlight: 3 cols → 2 cols at tablet → 1 col at mobile, left-aligned (not centered)
- Product card spec-badge row wraps at < 320px; price and CTA remain on separate lines
- Spec table scrolls horizontally inside a scroll container on mobile; first column (label) is sticky-left
- Comparison-bar product slots reduce: shows max two thumbnails on mobile with "+N more" label

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from lg.com — the site loads design tokens via JavaScript or is behind anti-bot protection. All color values are from publicly documented LG brand guidelines (LG Red #a50034 is cited in multiple brand identity references) and must be validated against a live design-system audit before production use.
- No font-family stacks were extracted. "LG Smart" is LG's documented proprietary typeface; web delivery format (WOFF2 source URLs, loading strategy, subset coverage) is unknown. Helvetica Neue fallback is assumed.
- Font weight axis for LG Smart is unconfirmed — weights 400, 600, 700 are assumed based on typical brand typeface ranges; a full weight audit against the live CDN is required.
- Dark-mode support on lg.com was not confirmed; no dark-mode token variants are defined.
- Exact box-shadow values for product cards and comparison-bar are estimated from visual inspection conventions; live DevTools inspection is required.
- Pricing display treatment (MSRP vs. sale strikethrough, financing callout format, installment display) needs live SKU verification.
- LG ThinQ, InstaView, Craft Ice, and Door-in-Door feature icon assets require access to LG's design system or CDN — placeholder 48px icon sizing is assumed.
- Hover and focus animation timing (transition duration, easing curves) is unspecified; 150ms ease-in-out is a reasonable default but should be confirmed.
