---
version: alpha
name: "Gothic Arch"
source_url: "https://www.gothicarchgreenhouses.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every call-to-action button on gothicarchgreenhouses.com runs the same flat signal red (#cc0000) — no gradient, no shadow blur, no hover shimmer, just a solid rectangle that reads like a hardware-store price tag. The palette underneath is catalog-utilitarian: ten neutrals spanning #111111 through #f6f6f6 form the working surface, while that red and a single horticultural green (#339933) carry all the emotional weight. A deep marine teal (#006080) surfaces in informational links and product-detail callouts — the one cool-temperature accent in an otherwise achromatic system. Baskerville appears in the font stack alongside Arial and Helvetica, an unexpected serif that is telling: it signals the serious hobbyist and commercial grower audience that Gothic Arch has served since its 1946 founding in Mobile, Alabama, giving product description copy a slight almanac formality that a pure sans-serif stack would flatten. Button corners are barely radiused ({rounded.xs}), inputs sit inside rectangular shells, and the product grid packs tightly without the breathing room of lifestyle brands. Navigation runs multiple levels deep with no animation budget — category trees, filter sidebars, and spec tables share the same high-density philosophy. Whitespace is functional: it separates sections rather than creates atmosphere. The #e83e8c pink and #ff9933 orange in the extracted palette are almost certainly UI-framework artifacts — Bootstrap badge defaults or Font Awesome state tints — rather than Gothic Arch choices. The true brand signal is in what is absent: no lifestyle photography art direction, no motion, no aspirational overlay copy. Just panel dimensions, glazing options, a note about Alabama weather testing, and a red button that has read "Add to Cart" with exactly this weight for two decades.

colors:
  primary: "#cc0000"
  primary-active: "#aa0000"
  primary-disabled: "#e09090"
  brand-green: "#339933"
  brand-teal: "#006080"
  ink: "#111111"
  body: "#444444"
  muted: "#777777"
  muted-soft: "#888888"
  mid-gray: "#585858"
  dark-gray: "#2b2b2b"
  hairline: "#dcdcdc"
  hairline-soft: "#eeeeee"
  canvas: "#fcfcfc"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-strong: "#f3f3f3"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  spec-label:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 10px
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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.mid-gray}"
  button-green:
    backgroundColor: "{colors.brand-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 38px
  text-input-focus:
    border: "1px solid {colors.mid-gray}"
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 44px
  nav-bar-top:
    backgroundColor: "{colors.dark-gray}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 32px
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.brand-teal}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
  product-card-price-original:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  new-badge:
    backgroundColor: "{colors.brand-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  hero-banner:
    backgroundColor: "{colors.dark-gray}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 28px
  category-tile:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    headerBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
  breadcrumb:
    textColor: "{colors.brand-teal}"
    separatorColor: "{colors.muted}"
    typography: "{typography.caption}"
    activeTextColor: "{colors.muted-soft}"
  promo-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 36px
  footer:
    backgroundColor: "{colors.dark-gray}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  sidebar-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"

## Components

### Buttons

**`button-primary`** — A flat #cc0000 rectangle with barely any radius ({rounded.xs}, 2px), uppercase Arial at 14px with 0.5px letter-spacing. The uppercase treatment and near-square corners give it a catalog-hardware authority with no softness. Active state darkens to #aa0000; disabled washes to #e09090 while keeping text white. This is the site's single dominant action signal, used for Add to Cart, Buy Now, and top-of-funnel CTAs.

**`button-secondary`** — White fill with a 1px {colors.hairline} border and matching uppercase typography. On hover the border darkens to {colors.mid-gray} (#585858) to signal interactivity without changing the label color. Used for Compare, Wishlist, and filter-reset actions alongside the primary red.

**`button-green`** — Identical construction to button-primary but filled with {colors.brand-green} (#339933). Reserved for availability messaging ("In Stock," "Request a Quote") and ecological callouts where the red CTA would send a conflicting signal. Never used as the dominant page action.

### Navigation

**`nav-bar`** — A near-black (#111111) full-width bar at 44px. Nav links render as white uppercase bold Arial at 14px. A utility strip above it (`nav-bar-top`, 32px, #2b2b2b) carries phone numbers, account links, and free-shipping thresholds in 12px caption weight. Dropdowns emerge as flush white panels with a hairline border and no entry animation — the transition is immediate, matching the overall zero-motion budget of the site.

### Product Cards

**`product-card`** — Zero border-radius, 1px {colors.hairline} border, {spacing.sm} padding. The product title renders in {colors.brand-teal} (#006080) as an underlined link — teal is the site's consistent link color across all product references. Price sits below in {colors.primary} red at 20px bold. When a sale price applies, the original floats in struck-through {colors.muted} gray. No hover lift, no shadow — the card is static; interactivity lives only in the title's color change on hover.

**`sale-badge` / `new-badge`** — Flush rectangular chips (no radius) positioned top-left over product images. Sale badges use primary red; New badges use {colors.brand-green}. Both are 11px uppercase bold Arial at 2px 6px padding. These are the only graphical overlays that appear on product imagery.

### Hero

**`hero-banner`** — Charcoal ({colors.dark-gray}, #2b2b2b) background with the display headline in Baskerville at 36px. Against the dark field the serif reads more like a trade-magazine print ad than a contemporary e-commerce hero. The CTA inherits button-primary. Body copy uses white {typography.body-md} at 16px regular. There is no background photography in the default hero state — the color block alone anchors the header.

### Spec Table

**`spec-table`** — Two-column definition table with a {colors.surface-soft} header row and alternating {colors.surface-card}/{colors.surface-strong} row fills. Labels render in {typography.spec-label} (13px bold Arial); values in {typography.body-sm} (14px regular Arial). All cell borders run {colors.hairline}. No rounded corners. This is the highest information-density component on the site: panel dimensions, glazing type, shipping weight, frame gauge, and warranty terms all land here, and legibility at this scale is the primary design concern.

### Breadcrumb

**`breadcrumb`** — Compact 12px caption-weight Arial links in {colors.brand-teal}, separated by a {colors.muted} slash character. The current page label renders in {colors.muted-soft} without an underline. Sits immediately above product titles and category headings to communicate hierarchy across a deep catalog structure.

### Promo Bar

**`promo-bar`** — Full-width {colors.primary} red strip at 36px, carrying free-shipping thresholds or seasonal offers in 12px white caption text centered horizontally. Sits at the very top of the page, above even the utility nav strip. When active it is the first element a visitor reads — the site uses it as its highest-reach promotional surface.

### Footer

**`footer`** — Full-width {colors.dark-gray} background with four to six link-group columns. Section headings in {typography.title-sm} white; links in {colors.hairline-soft} (#eeeeee) at {typography.body-sm}. The base of the footer carries payment-method logos (Visa, MasterCard, AMEX, PayPal, Discover) as small grayscale assets. No animated or hover-state transitions on footer links.

### Sidebar Filter

**`sidebar-filter`** — Left-rail component on category pages with checkbox and radio filters for frame type, panel size, glazing material, and price range. {colors.surface-soft} background with no radius; group headings use {typography.title-sm} in {colors.ink}. Applied filter chips inherit the hairline-border treatment from button-secondary, appearing inline below the filter label when active.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger icon; hero headline drops to {typography.display-md}; sidebar filter moves to a full-screen modal drawer triggered by a "Filter" button |
| Tablet | 744–1128px | Two-column product grid; top utility nav collapses to icon row; hero remains full-bleed with reduced vertical padding |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar and utility strip visible; sidebar filter renders inline in left rail at fixed width ~220px |
| Wide | > 1440px | Max-width container (~1200px) centered; four-column product grid; hero image extends edge-to-edge behind contained text column |

### Touch Targets

- All primary and secondary buttons enforce 40px minimum height as set in component spec
- Collapsed mobile nav links should have 48px tap height inside the drawer accordion
- Checkbox and radio filter controls should have full-row touch targets, not icon-only hit areas
- Product card images should be entirely tappable — the link wrapper spans the full card, not just the title text

### Collapsing Strategy

- Navigation: hamburger toggle at < 744px; category dropdowns become full-width accordion panels inside the mobile drawer
- Sidebar filters: slide-in modal at < 1128px, triggered by a "Filter" button pinned above the product grid
- Spec tables: horizontal scroll container on mobile; the label column uses position sticky at left: 0 to remain readable while values scroll
- Hero text block: stacks below any background image on mobile rather than overlaying it
- Footer columns: collapse to a single-column accordion list below 744px, with section headings acting as toggle triggers

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected — Baskerville is inferred from the system font-family stack; exact weight usage, optical sizing, and whether it is used in headings vs. body cannot be confirmed without live rendering
- Primary CTA color identified as #cc0000 based on it being the most distinctive non-gray in the extracted palette; confirm this is the true action color and not a secondary accent
- No meta theme-color provided — mobile browser chrome color and PWA manifest color are unknown
- #e83e8c (Bootstrap pink) and #ff9933 (Bootstrap orange) treated as framework artifacts and excluded from the brand token set; verify these do not appear as intentional Gothic Arch UI colors
- #acbad5, #0000ff, and #0000cc appear in the extracted palette and are likely default hyperlink states or framework variables; not assigned to named brand tokens
- Logo mark, illustration style, and icon set could not be extracted — no custom iconography assumed beyond standard e-commerce and arrow glyphs
- Exact CSS breakpoints and grid column counts are inferred from catalog-site conventions, not confirmed from live stylesheets
- All transition and animation durations assumed absent or at immediate (0ms); no motion values could be extracted
