---
version: alpha
name: "Burpee"
source_url: "https://www.burpee.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Seed packets carry more data per square inch than most product pages ever attempt — days to maturity, USDA hardiness zones, germination rates, and spacing requirements all compete for real estate before price even enters the conversation. Burpee's UI inherits this density directly: product detail pages function closer to botanical data sheets than to standard e-commerce, and the navigation tree branches by plant family, sun tolerance, and harvest timing rather than by color or occasion. The brand's garden green (#3a6e2f) anchors primary actions and category headers, grounding every surface in something organically legible before any photograph loads. Against that green, an amber-orange (#e07228) signals sale events and promotional badges — a pairing that reads simultaneously as harvest-season warmth and commercial urgency, which is exactly what a spring seed sale requires. Type runs in a clean transitional serif for display — carrying the authority of a 150-year catalog without the rigidity of a financial institution — while body copy settles into a readable sans-serif that accommodates dense planting guides and customer reviews at the same scroll. White canvas (#ffffff) and a pale sage surface (#f3f7f0) create breathing room between photography-heavy category rows, while product cards float on surface-card white with a soft hairline border ({rounded.sm}) rather than drop shadows, keeping the focus on the seed packet artwork itself. Rounded corners stay conservative throughout — {rounded.sm} on cards, {rounded.xs} on badges — because this brand's visual credibility comes from specificity, not softness. The planting-zone finder widget, persistent in the footer and recallable from the header, anchors the entire experience in a geographic utility most DTC brands never need to consider; it is the most honest expression of what Burpee actually sells, which is not seeds but rather successful gardens in specific climates.

colors:
  primary: "#3a6e2f"
  primary-active: "#2d5525"
  primary-disabled: "#a8cfa0"
  accent-orange: "#e07228"
  accent-orange-active: "#b85a18"
  accent-orange-soft: "#fdf0e6"
  ink: "#1c1c1c"
  body: "#3d3d3d"
  muted: "#6b6b6b"
  hairline: "#dde3d8"
  hairline-soft: "#eef1eb"
  canvas: "#ffffff"
  surface-soft: "#f3f7f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-heirloom: "#6b3d2e"
  badge-organic: "#3a6e2f"
  badge-new: "#e07228"
  sale-red: "#c0392b"
  zone-blue: "#2c6a9a"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  data-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  data-value:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-original:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  button-add-to-cart:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-add-to-cart-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
  nav-bar-utility:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoHeight: 40px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    shadow: "0 4px 12px rgba(0,0,0,0.10)"
    padding: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1:1"
    padding: "{spacing.md}"
    gap: "{spacing.sm}"
  product-card-name:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-price-original:
    typography: "{typography.price-original}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  variety-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
    variants:
      heirloom:
        backgroundColor: "{colors.badge-heirloom}"
        textColor: "{colors.on-primary}"
      organic:
        backgroundColor: "{colors.badge-organic}"
        textColor: "{colors.on-primary}"
      new:
        backgroundColor: "{colors.badge-new}"
        textColor: "{colors.on-primary}"
      exclusive:
        backgroundColor: "{colors.ink}"
        textColor: "{colors.on-primary}"
  growing-data-grid:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    labelTypography: "{typography.data-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.data-value}"
    valueColor: "{colors.ink}"
    columns: 3
  planting-zone-widget:
    backgroundColor: "{colors.zone-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    inputRounded: "{rounded.xs}"
    inputBorder: "1px solid {colors.hairline-soft}"
  hero-seasonal:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    imagePosition: right
    primaryButtonBackground: "{colors.primary}"
    primaryButtonText: "{colors.on-primary}"
    primaryButtonRounded: "{rounded.sm}"
    minHeight: 480px
  sale-banner:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.none}"
    height: 44px
  category-nav-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    borderActive: "2px solid {colors.primary}"
    backgroundColorActive: "{colors.primary}"
    textColorActive: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    height: 44px
    padding: "0 {spacing.base}"
    iconColor: "{colors.muted}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
    width: 240px
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.ink}"
  review-stars:
    filledColor: "{colors.accent-orange}"
    emptyColor: "{colors.hairline}"
    size: 16px
  quantity-stepper:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 40px
    buttonWidth: 40px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline-soft}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons
**`button-primary`** — Primary CTA runs garden green (#3a6e2f) at 44px height with {rounded.sm} corners; use for navigation-forward actions such as "Shop Now," "View All Vegetables," or "Find My Zone." Active state deepens to #2d5525; disabled washes out to #a8cfa0 to preserve the green palette tone.

**`button-add-to-cart`** — Add-to-cart deliberately breaks from primary green to amber-orange (#e07228), separating browse mode from buy mode at a glance. The orange reads as harvest urgency alongside ripe-vegetable photography and triggers the purchase intent signal more immediately than a second green button would.

**`button-secondary`** — White canvas with a 2px primary-green border and green label text — functionally outlined, matching the card border language throughout the catalog. Use for lower-stakes actions: "Save to Wishlist," "Compare Varieties," "Print Planting Guide."

### Product Cards
**`product-card`** — A square 1:1 seed-packet image dominates the upper portion; the packet artwork carries primary visual weight and is never cropped or skewed. Below it: variety name in {typography.title-sm}, price in {typography.price}, struck-through original in {typography.price-original} if discounted, and one to three `variety-badge` chips. A {colors.hairline} border on {rounded.sm} corners separates cards without drop shadows, keeping shelf density high and focus on the packet itself.

### Variety Badges
**`variety-badge`** — Small uppercase pill badges at 11px tracking 0.5px, {rounded.xs}. Four variants signal provenance instantly without requiring users to open the product page: Heirloom (warm brown #6b3d2e) for open-pollinated heritage cultivars, Organic (primary green) for certified seed, New (orange #e07228) for recent introductions, and Exclusive (ink black) for Burpee-only varieties. These badges are display-only, not interactive.

### Growing Data Grid
**`growing-data-grid`** — A 3-column agronomic data panel rendered on {colors.surface-soft} displaying Days to Germination, Days to Maturity, Plant Spacing, Sun Exposure, Water Needs, and USDA Hardiness Zone. Labels use {typography.data-label} in {colors.muted} (uppercase, 12px, 0.5px tracking); values use {typography.data-value} in {colors.ink}. This component has no equivalent in fashion or food DTC — it is the most category-specific UI element in the system and lives immediately below the product image, above the Add to Cart row.

### Navigation
**`nav-bar-utility`** — A 36px primary-green bar sits above the main navigation, carrying shipping threshold messaging ("Free shipping on orders over $35"), a zone-finder quick link, and sign-in. It is the first horizontal band visible on load and establishes the green brand temperature before the logo appears.

**`nav-bar`** — White 64px bar with Burpee logo left-anchored. Center holds category links — Vegetables, Flowers, Herbs, Fruit, Garden Supplies — in {typography.nav-link}. Right cluster holds search, account, and cart icons. Hover treatment is underline only; no button background on primary nav links. Separated from page content by a single 1px {colors.hairline} bottom border.

**`mega-menu`** — Hovering a top-level category opens a full-width dropdown panel listing subcategories in columns (e.g., Vegetables → Tomatoes, Peppers, Cucumbers, Squash, Beans…) with a curated editorial image on the far right. Shadow is 4px/12px at 10% black opacity, lifting the panel cleanly from the page canvas without heaviness.

### Hero
**`hero-seasonal`** — Split layout with headline copy left and seasonal garden photography right on a {colors.surface-soft} background. Headline in {typography.display-xl}, subhead in {typography.body-md} in {colors.body}. Two stacked CTAs: primary green button ("Shop Spring Seeds") above a plain text link ("View All Vegetables"). Minimum height 480px on desktop; collapses to single-column with image below copy below 744px.

### Sale Banner
**`sale-banner`** — Full-width {colors.accent-orange} strip at 44px with white {typography.button-md} text, no radius ({rounded.none}), sitting directly below the utility bar when a promotion is active. Used for seasonal events — Spring Savings, Summer Sale, Seed of the Year — and dismissed after session acknowledgment.

### Search
**`search-bar`** — 44px inline search bar in the main nav, expanding on focus to show a suggestion dropdown. Placeholder "Search 6,000+ varieties…" communicates catalog breadth immediately. Magnifier icon in {colors.muted}; border flips from {colors.hairline} to 2px {colors.primary} on focus, consistent with text-input focus behavior across the system.

### Category Navigation Pills
**`category-nav-pill`** — Horizontal scrolling row of {rounded.full} filter pills on category pages: All, Heirloom, Organic, Best Sellers, On Sale, Days to Harvest (short/medium/long). Default: {colors.surface-soft} fill with {colors.ink} text. Active: primary green fill, white text, border removed. Scroll row fades out at right edge with a canvas gradient on mobile.

### Planting Zone Widget
**`planting-zone-widget`** — Accepts a zip code and returns the USDA hardiness zone, then persists as a session cookie to filter planting date guidance across product pages. Zone-blue (#2c6a9a) background differentiates this widget from the commercial green system — blue reads as informational utility rather than commerce. Appears in the footer and can be recalled from a header link.

### Filter Sidebar
**`filter-sidebar`** — Pinned left at 240px on desktop with a {colors.hairline} right border, listing facets: Plant Type, Sun Exposure, Days to Maturity, Hardiness Zone, Seed Type (Heirloom/Hybrid/Organic), Price Range. Section headings in {typography.title-sm}; facet options in {typography.body-sm} with checkbox inputs. Collapses to a bottom sheet modal on mobile and tablet.

### Footer
**`footer`** — Dark ink (#1c1c1c) base with four columns: About Burpee, Customer Service, Gardening Resources, Newsletter Signup. Link text in {colors.hairline-soft} for readable contrast without full white brightness. Newsletter form is the primary footer conversion surface — Burpee's 150-year catalog heritage makes the email list a meaningful retention channel.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; mega-menu collapses to full-screen accordion drawer via hamburger toggle; hero stacks image below copy; category pills scroll horizontally with right-edge fade; search expands to full-width overlay on tap; utility bar trims to icon-only strip; filter sidebar becomes bottom-sheet modal |
| Tablet | 744–1128px | 2-column product grid; mega-menu becomes slide-in side panel; hero goes 60/40 split; filter sidebar collapses to modal sheet accessed via a "Filter" button; growing data grid drops to 2 columns |
| Desktop | 1128–1440px | 3–4 column product grid; full-width mega-menu dropdown; filter sidebar pinned left at 240px; growing data grid renders all 6 specs in 3 columns |
| Wide | > 1440px | Content max-width 1440px centered; product grid holds at 4 columns; hero image scales but copy column stays fixed at ~520px wide |

### Touch Targets
- All buttons minimum 44×44px
- Quantity stepper increment/decrement buttons expand to 48×48px on mobile
- Nav bar icons (cart, account, search) maintain 44px touch area regardless of 24px visual icon size
- Category filter pills minimum 36px height on mobile, 32px on desktop
- Variety badges are display-only and carry no touch target requirement
- Filter facet checkboxes minimum 44px tap height on mobile

### Collapsing Strategy
- Filter sidebar → bottom sheet modal on mobile and tablet; pinned left only on desktop and wide
- Mega-menu → full-screen accordion drawer on mobile (hamburger); slide-in side panel on tablet; full-width dropdown on desktop+
- Growing data grid → 2-column on mobile (deprioritize least-critical spec); 3-column on tablet and desktop
- Utility bar → icon-only strip on mobile (no text labels); full text on tablet+
- Footer columns → single accordion stack on mobile; 2-column on tablet; 4-column on desktop and wide
- Planting zone widget → full-width input on mobile; compact inline form on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the live site blocked extraction or loads color tokens via JavaScript. All palette values are inferred from widely observable brand identity (Burpee's green is a well-documented brand element; orange sale accents are visible in any product catalog screenshot). Treat all hex values as provisional until verified against live computed styles.
- **No font stacks extracted** — typeface choices are inferred from brand archetype (heritage American seed catalog, 1876 founding). Actual font families must be confirmed by inspecting network font requests or computed CSS on burpee.com; the Georgia/system-sans pairing here is a plausible stand-in only.
- **No meta theme-color declared** — Burpee does not set a theme-color meta tag; mobile browser chrome color will be system default.
- **Exact border-radius values unknown** — {rounded.sm} (8px) is a conservative default for a catalog-heritage brand; verify against live component inspection.
- **Badge color assignments** — heirloom brown, organic green, and new orange are logical inferences from category semantics, not extracted from computed badge styles.
- **Planting zone widget exact treatment** — widget existence and function are publicly documented; the zone-blue (#2c6a9a) and exact layout are inferred, not extracted.
- **Typography weights and sizes** — all scale values are informed estimates based on category norms for data-dense e-commerce; must be verified against live CSS before implementation.
- **Sale and promotional system** — the sale-red (#c0392b) token is inferred from standard e-commerce conventions; Burpee may use a different hue for markdown pricing.
