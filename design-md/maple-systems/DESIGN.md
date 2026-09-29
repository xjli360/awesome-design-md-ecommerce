---
version: alpha
name: "Maple Systems"
source_url: "https://www.maplesystems.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Maple Systems stakes its catalog on a single engineering-grade blue — #0675c4 — that runs every clickable element from the "Add to Cart" button on a 5-inch operator panel to the active state indicator in the top navigation. The industrial control palette underneath it is deliberately spare: near-black ink at #1e1e1e on a white canvas, hairlines at #dcddde separating specification blocks without announcing themselves, and a charcoal #313131 footer that closes each page like a panel enclosure lid; no accent color competes, and visual hierarchy is achieved through weight and spatial proximity rather than hue contrast. The deep navy #003388 surfaces only in promotional anchors and section dividers — a muted declaration of technical authority rather than a lifestyle pitch. Type runs entirely on the system font stack: Roboto leading with -apple-system, Segoe UI, and Helvetica Neue in the fallback chain, a choice that reads less as a budget default and more as an honest engineering standard — the same typeface purchasing managers encounter in their datasheet viewer and PLC configuration software. Display sizes land conservatively at 36px weight 700, making room for the dense spec tables and product grids that do the actual selling; button labels carry fontWeight 600 at 0.5px letter-spacing, pressed into corners rounded to just {rounded.sm} (4px) — a corner radius that tracks closer to a machined chamfer than consumer-app softness, with pill shapes and dramatic radii absent entirely. Product cards form the atomic unit of the catalog: a 1px {colors.hairline} border, a product thumbnail, a {typography.title-sm} name, abbreviated specs in {typography.caption} scale, and a price in {typography.title-md} — in that order, without decoration. The site's information architecture mirrors how industrial buyers actually shop: by product family, by display size, by I/O count and communication protocol. Spec tables, with their {colors.surface-soft} header rows and uppercase {typography.spec-label} column heads, serve as the primary persuasion mechanism — Maple Systems trusts engineering data over photography.

colors:
  primary: "#0675c4"
  primary-hover: "#006ba1"
  primary-active: "#005a87"
  primary-disabled: "#b8d4ec"
  ink: "#1e1e1e"
  body: "#2f2f2f"
  muted: "#949494"
  hairline: "#dcddde"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  navy-deep: "#003388"
  dark-slate: "#2e3440"
  charcoal: "#313131"
  success: "#4ab866"

typography:
  display-xl:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Fira Sans', Roboto, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0.6px
    textTransform: uppercase
  button-md:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 10px
  xl: 16px
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
    padding: 10px 20px
    height: 42px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 42px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    hoverTextDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    focusBorderColor: "{colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 70px
    borderBottom: "1px solid {colors.hairline}"
    activeColor: "{colors.primary}"
    activeBorderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    priceTypography: "{typography.title-md}"
  hero-banner:
    backgroundColor: "{colors.dark-slate}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.sm}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.spec-label}"
    borderColor: "{colors.hairline}"
    cellTypography: "{typography.body-sm}"
    rowStripeColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
  product-family-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderTopAccent: "3px solid {colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    accentColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 40px
    iconColor: "{colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.muted}"
  availability-chip-in-stock:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  availability-chip-unavailable:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  promo-strip:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  category-tab-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
    typography: "{typography.nav-link}"
  category-tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.hairline}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Solid #0675c4 fill with white text at fontWeight 600 and 0.5px letter-spacing, contained by a 4px border-radius ({rounded.sm}) that reads as deliberately sharp. Hover state shifts to #006ba1, active press to #005a87; disabled drains to the pale #b8d4ec fill. At 42px height and 10px×20px padding, this button stacks cleanly in product card footers, sidebar CTAs, and inline spec-section actions without overwhelming the data density around it.

**`button-secondary`** — White fill with a 1px #0675c4 border and matching blue label text. Deployed for parallel-priority actions like "Request a Quote" or "Download Datasheet" placed beside an add-to-cart primary. Shares the same 42px height and {rounded.sm} corner so button pairs align flush on the grid baseline without custom offset.

**`button-text-link`** — Transparent background, #0675c4 text at {typography.body-sm} scale. Underlines on hover. Used for inline navigation anchors, "View All" pagination links, and sub-actions within spec blocks where a full-height button would visually outrank the surrounding content.

### Navigation
**`nav-bar`** — 70px white bar with a 1px #dcddde bottom border as the sole elevation separator — no drop shadow at any scroll depth. Links run at {typography.nav-link} (14px, weight 500) with a 2px #0675c4 bottom border marking the active section. A persistent search icon and cart count badge occupy the right rail. On mobile this bar collapses entirely to a hamburger toggle.

**`category-tab-active` / `category-tab-inactive`** — A horizontal tab strip separating product lines such as HMIs, PLCs, and Remote I/O. Active tab carries a 2px #0675c4 underline on a white field; inactive tabs rest on #f0f0f0 with #2f2f2f text. No animated transitions — state change is binary and instant, consistent with the engineering-first aesthetic.

### Product Display
**`product-card`** — The core commerce unit: 1px #dcddde border, {rounded.sm} corners, {spacing.base} internal padding. Top zone holds a product thumbnail; below it sits the {typography.title-sm} name (15px, weight 600), a single line of comma-separated specs in {typography.caption} (12px, weight 400), and a price in {typography.title-md} (18px, weight 600). The add-to-cart button docks flush to the card's lower edge.

**`product-family-card`** — Larger feature card used on category landing pages, distinguishable by a 3px #0675c4 top accent border against the #eeeeee card body. Carries a {typography.title-md} heading and two lines of {typography.body-sm} descriptive copy. Functions as a grouping entry point — e.g., "5" Color HMI Panels" — rather than a single purchasable SKU.

**`spec-table`** — The most load-bearing component on the site. Header row fills #f0f0f0 with {typography.spec-label} columns (11px, uppercase, 0.6px tracking). Data rows alternate between #ffffff and #eeeeee for scanability; values use {typography.body-sm}. No border-radius — the table runs edge-to-edge inside its container. Hairlines at #dcddde divide every row and column. On mobile the table scrolls horizontally inside a scroll container with the spec-name column sticky.

### Search & Utility
**`search-bar`** — 40px input field with a 1px #0675c4 border and a magnifier icon in matching primary blue. Placeholder and value text run at {typography.body-sm}. On mobile the field is hidden behind a tap-to-expand icon that animates to full-width; on desktop it sits inline in the nav rail.

**`breadcrumb`** — Muted gray (#949494) path chain in {typography.caption} scale, separated by "/" dividers. Parent-page segments are #0675c4 links with underline on hover; the current page carries no link and stays gray. Appears immediately below the nav-bar on all product, category, and support pages.

**`availability-chip-in-stock` / `availability-chip-unavailable`** — Compact inline badge pinned to each product listing. In-stock reads #4ab866 fill with white {typography.caption} text, 2px×8px padding, and {rounded.xs} corners. Unavailable or discontinued variants use #949494 fill with the same dimensions. Display-only — the nearest ancestor card carries the tap region.

**`promo-strip`** — Full-width banner in #003388 navy with white {typography.body-sm} copy. Used sparingly for sitewide shipping thresholds, trade show announcements, or product launch notices. No close control — the strip dismisses only on page navigation.

**`hero-banner`** — Full-bleed section in dark slate (#2e3440) hosting white headline copy at {typography.display-xl} (36px, weight 700) with supporting body text at {typography.body-md}. The primary CTA sits in a #0675c4 button at {rounded.sm}. Vertical padding at {spacing.section} (64px) and horizontal at {spacing.xl} (32px). Typically carries a product photography composite or industrial installation photo.

**`footer`** — #313131 charcoal background with #f0f0f0 text and #dcddde hairlines dividing columns. Four columns on desktop (Products, Support, Company, Contact) with {typography.title-sm} headings at weight 600 and {typography.body-sm} link lists below. Collapses to a single-column accordion on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger + logo; search-bar hides behind tap-to-expand icon; spec-table scrolls horizontally with sticky left column; hero-banner headline drops to display-md (28px) and CTA button goes full-width |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows abbreviated primary links with overflow dropdown; category-tab strip scrolls horizontally; spec-table stays full-width inside a horizontal scroll container |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav-bar with all category links visible; spec-table max-width 960px centered in container |
| Wide | > 1440px | Grid caps at four columns; max-width container at 1440px with canvas color filling beyond edges; promo-strip remains full viewport width |

### Touch Targets
- All buttons maintain minimum 42px height matching the button-primary height token
- Nav-bar links inflated to 48px tap height via vertical padding
- Availability chips and category badges are display-only; the parent product-card absorbs the touch region
- Search icon in collapsed nav expands to a 44px × 44px tap target before the input field renders
- Footer accordion section headers meet 44px minimum height on mobile

### Collapsing Strategy
- Primary navigation condenses to hamburger at < 744px; mega-menu or dropdown panels replaced by stacked full-width accordions
- Spec-table scrolls horizontally inside an overflow container; the first (spec-name) column is position-sticky so parameter labels remain visible while values scroll
- Footer four-column grid collapses to single-column accordion; sections expand/collapse independently
- product-family-card switches from horizontal image-left + text-right layout to stacked vertical at < 744px
- hero-banner reduces headline from display-xl (36px) to display-md (28px) on mobile; supporting copy truncates to two lines with a "Learn More" link
- Category-tab strip becomes horizontally scrollable at < 744px rather than wrapping or truncating tab labels

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; site runs on a WooCommerce/WordPress stack using the system font stack (Roboto, -apple-system, Segoe UI, Helvetica Neue). Specific typographic scale sizes and weights are inferred from common WooCommerce theme defaults — not extracted pixel values.
- A large share of extracted hex colors are WordPress Gutenberg block editor default palette entries (#00d084, #0693e3, #cd2653, #f0b849, #4ab866, #3c6df0, #d93025, #7a00df, #34e2e4, #4721fb, #ab1dfe, etc.) rather than brand design tokens; these have been excluded from the color system.
- `primary-disabled` (#b8d4ec) is derived by lightening the primary blue and is not present in the extracted color set.
- No meta theme-color set; mobile browser chrome color is unspecified.
- Exact nav-bar height, logo lockup dimensions, and sticky-header scroll behavior are engineering-informed estimates, not confirmed measurements.
- No shadow values, animation easing curves, or transition durations were extractable; motion design is unspecified.
- Product photography art direction (background treatment, aspect ratio, shadow style) not confirmed from extraction.
- Whether Fira Sans is actively loaded by the site (listed in font stacks) or merely a fallback candidate is unverified; spec-label may render in Roboto in practice.
