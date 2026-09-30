---
version: alpha
name: "Ink4Less"
source_url: "https://ink4less.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Twenty-six years of ink-cartridge arbitrage have produced a visual shorthand that any bargain-hunter decodes instantly: #ff5501 orange commands every primary add-to-cart button, sale badge, and promotional banner — the color of a clearance sticker applied with institutional confidence across a catalog spanning hundreds of printer models. Against it sits #0088cc, a no-pretense cyan-blue that earns its keep on navigation links, account anchors, breadcrumb trails, and informational highlights without attempting brand differentiation. The canvas is #f6f6f6 gray-white — a practical staging ground for dense SKU listing pages where pricing numerals and compatibility notes matter more than art direction. Typography stays in the Open Sans / Arial / Helvetica stack: no custom type investment, no variable font, just legible geometric sans-serifs at utilitarian sizes with tight information hierarchy. A 12px caption layer carries yield specs and cartridge page-count data; a compact 14px body handles product descriptions; display sizes stay modest, rarely breaking 26px, because the hero territory belongs to savings percentages and "SAVE 80%" callouts rather than brand slogans.

  Rounding is conservative — {rounded.xs} and {rounded.sm} on buttons and cards, with pill shapes ({rounded.full}) reserved for small compatibility-match badges and promotional label chips. The grid follows a Porto/Magento catalog layout: a narrow left sidebar for layered navigation (category, brand, price, yield-range filters), a 3–4 column product grid in the content area, and a utility top bar carrying account, cart, and quick-search. Micro-accents in #0cc485 green signal in-stock status and success confirmations; #eb2771 pink marks flash-sale or clearance triggers; #e02b27 red handles error, out-of-stock, and critical alerts. A broad neutral ramp — #777777 through #e7e7e7 — governs dividers, secondary labels, disabled states, and the catalog's structural chrome. The overall register is dense, function-forward catalog retail: trust earned through SKU depth, compatibility tables, and visible price comparison rather than brand photography or editorial whitespace.

colors:
  primary: "#0088cc"
  primary-active: "#007bdb"
  primary-disabled: "#aaaaaa"
  accent: "#ff5501"
  accent-active: "#e04800"
  accent-disabled: "#ffc4a8"
  success: "#0cc485"
  promo: "#eb2771"
  info: "#0ae3eb"
  error: "#e02b27"
  ink: "#222529"
  body: "#303030"
  muted: "#777777"
  muted-soft: "#aaaaaa"
  hairline: "#e7e7e7"
  hairline-soft: "#eeeeee"
  border-mid: "#c1c1c1"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#f4f4f4"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  on-dark: "#ffffff"
  utility-bar: "#514943"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  savings-callout:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge-label:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  compat-tag:
    fontFamily: "Consolas, 'Courier New', Menlo, Monaco, monospace"
    fontSize: 11px
    fontWeight: 400
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
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
    states:
      hover:
        backgroundColor: "{colors.accent-active}"
      disabled:
        backgroundColor: "{colors.accent-disabled}"
        textColor: "{colors.muted}"

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: 9px 19px
    height: 40px
    states:
      hover:
        backgroundColor: "{colors.primary}"
        textColor: "{colors.on-primary}"

  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    states:
      hover:
        textColor: "{colors.primary-active}"
        textDecoration: underline

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.border-mid}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 38px
    placeholderColor: "{colors.muted}"
    states:
      focus:
        border: "1px solid {colors.primary}"
        outline: "2px solid rgba(0,136,204,0.18)"

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 44px
    utilityBarBg: "{colors.utility-bar}"
    utilityBarColor: "{colors.on-dark}"
    megaMenuBg: "{colors.canvas}"
    megaMenuBorder: "{colors.hairline}"

  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.border-mid}"
    rounded: "{rounded.xs}"
    height: 40px
    buttonBg: "{colors.accent}"
    buttonColor: "{colors.on-accent}"
    buttonTypography: "{typography.button-md}"
    buttonRounded: "{rounded.none}"

  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageBg: "{colors.surface-soft}"
    hoverShadow: "0 2px 8px rgba(0,0,0,0.12)"
    addToCartBg: "{colors.accent}"
    addToCartColor: "{colors.on-accent}"
    addToCartTypography: "{typography.button-sm}"

  price-block:
    priceColor: "{colors.accent}"
    priceTypography: "{typography.price-display}"
    listPriceColor: "{colors.muted}"
    listPriceTypography: "{typography.body-sm}"
    listPriceDecoration: line-through
    savingsColor: "{colors.success}"
    savingsTypography: "{typography.savings-callout}"

  badge-sale:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px

  badge-instock:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px

  badge-clearance:
    backgroundColor: "{colors.promo}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 3px 8px

  compatibility-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.compat-tag}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 2px 8px

  sidebar-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-sm}"
    itemTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    activeColor: "{colors.primary}"
    checkboxAccent: "{colors.primary}"

  hero-savings-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    displayTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaBg: "{colors.accent}"
    ctaColor: "{colors.on-accent}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    minHeight: 280px
    padding: "{spacing.xxl} {spacing.section}"

  promo-strip:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.caption-bold}"
    height: 36px
    textAlign: center

  breadcrumb:
    textColor: "{colors.muted}"
    linkColor: "{colors.primary}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    activeColor: "{colors.body}"

  pagination:
    activePageBg: "{colors.primary}"
    activePageColor: "{colors.on-primary}"
    inactivePageColor: "{colors.primary}"
    border: "1px solid {colors.border-mid}"
    rounded: "{rounded.none}"
    typography: "{typography.button-sm}"
    height: 36px

  cart-count-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    size: 20px

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    linkColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The primary CTA fires in #ff5501 orange with white type, channeling the deal-signal language of the catalog rather than the brand's blue. Height holds at 40px with 10px/20px padding and {rounded.xs} corners that read catalog-utilitarian rather than designed. Hover compresses to #e04800; disabled washes to {colors.accent-disabled} with {colors.muted} text to clearly signal inactivity.

**`button-secondary`** — Outlined in {colors.primary} blue with matching blue text on white, the secondary sits beside add-to-cart for secondary actions such as "Add to Wishlist" or "Compare." On hover the button floods solid blue and inverts to white type, giving it a clear selection moment without a separate active variant token.

**`button-text-link`** — Transparent background, {colors.primary} blue text, no underline at rest. Used throughout product descriptions, account menus, and footer navigation columns. Underline appears only on hover, keeping dense catalog pages visually quiet between action targets.

### Search Bar

**`search-bar`** — A full-width input joined flush on the right to a solid {colors.accent} orange submit button, deliberately matching the CTA color to reinforce that search is a deal-finding action. The input carries a {colors.border-mid} border with {rounded.xs} on the input-side edges and no radius where it butts the button. Focus state rings the input with a low-opacity blue outline from {colors.primary}.

### Navigation

**`nav-bar`** — A two-tier header: a compact utility bar in {colors.utility-bar} warm brown-gray carrying phone number, account links, and order-status access; below it a white category nav at 44px height with a full-width mega-menu on hover. Mega-menu panels render on {colors.canvas} white with {colors.hairline} borders and {typography.nav-link} labels. On mobile, both tiers collapse into a single hamburger drawer.

### Product Card

**`product-card`** — Cards sit on white with a 1px {colors.hairline} border and {rounded.xs} corners. The image area uses {colors.surface-soft} as a neutral mount. Title renders in {typography.title-sm}, followed immediately by the price block: sale price in {typography.price-display} orange, struck-through MSRP in {colors.muted} {typography.body-sm}, and a green savings line in {typography.savings-callout}. The add-to-cart button lives at card bottom in {colors.accent} full width. On hover the card lifts slightly with a 0 2px 8px shadow.

### Price Block

**`price-block`** — The brand's core value-communication unit: three stacked lines — {colors.accent} orange sale price at 22px bold, struck-through MSRP in {colors.muted} body-sm, and a "SAVE $X.XX" line in {colors.success} green. This orange/gray-strike/green trio repeats verbatim on every SKU listing, cart line item, and checkout summary.

### Badges

**`badge-sale`** — A tight {rounded.xs} chip in {colors.accent} orange with 11px uppercase bold white type. Sits at the top-left corner of product card imagery. **`badge-instock`** — Identical geometry in {colors.success} green; communicates availability without requiring the user to read further. **`badge-clearance`** — Full-pill {rounded.full} in {colors.promo} pink/magenta, used for liquidation or flash events to visually break from standard sale pricing and signal urgency.

### Compatibility Chip

**`compatibility-chip`** — A {rounded.full} pill using monospace {typography.compat-tag} on {colors.surface-card} with a {colors.hairline} border. Lists printer model numbers (e.g., `HP OfficeJet 5252`) inline within product titles or inside compatibility tables. The monospace face communicates precision and machine-readability for a catalog audience performing model lookups.

### Sidebar Filter

**`sidebar-filter`** — Porto-style layered navigation panel: {colors.surface-soft} background, no radius on the outer panel, {typography.title-sm} section headers (Brand, Category, Price, Page Yield), {typography.body-sm} checkbox items. Active filter selections colorize to {colors.primary} blue. The panel renders at approximately 220px wide on desktop, collapses to a slide-in drawer on mobile.

### Hero Savings Banner

**`hero-savings-banner`** — A full-width {colors.primary} blue band anchoring the homepage above the catalog grid. Headline in {typography.display-xl} white leads with a quantity or savings claim ("10,000+ Compatible Cartridges — Up to 80% Off MSRP"). CTA button in {colors.accent} orange on the blue ground creates strong contrast. No lifestyle photography; the banner is text- and pricing-first.

### Promo Strip

**`promo-strip`** — A 36px {colors.accent} orange bar at the very top of every page, above the nav tiers, carrying free-shipping thresholds or limited-time discount codes in {typography.caption-bold} white. Single-line on desktop; wraps gracefully on narrow viewports.

### Breadcrumb

**`breadcrumb`** — {typography.caption} in {colors.muted} gray with {colors.primary} blue links and a {colors.muted-soft} separator. The active (current) segment renders in {colors.body} non-linked. Sits immediately above the product title or category heading on all interior pages.

### Footer

**`footer`** — {colors.ink} dark background with a 3px {colors.primary} blue top border accent. Column headings in {typography.title-sm} {colors.on-dark} white; body links in {colors.on-dark} white at {typography.body-sm}. Carries trust anchors: "Over 26 Years in Business," secure-checkout icon row, return policy, and contact information.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; sidebar filter collapses to a slide-in drawer triggered by a floating "Filter" button; nav reduces to hamburger menu; search bar expands to full width below header strip; promo-strip wraps to two lines if copy exceeds single line |
| Tablet | 744–1128px | 2-column product grid; sidebar renders as collapsible accordion above the grid rather than a fixed left panel; nav shows primary category labels only with mega-menu on tap; search bar integrated in header at reduced width |
| Desktop | 1128–1440px | 3–4 column product grid; sidebar fixed at ~220px left; full mega-menu navigation; promo strip and dual-tier header at full width; product quick-view available as modal overlay |
| Wide | > 1440px | Content area capped at ~1400px and centered with symmetrical gutters; product grid holds at 4 columns; hero banner image may extend edge-to-edge behind a constrained text container |

### Touch Targets

- Add-to-cart buttons minimum 40px height, full card width on mobile tap
- Filter checkbox rows expand to 44px tap height on mobile
- Hamburger nav links minimum 48px height per row
- Pagination controls minimum 36px × 36px per item
- Utility bar links in mobile drawer minimum 44px tap height

### Collapsing Strategy

- Left sidebar filter → slide-in drawer (mobile), inline collapsible accordion (tablet), fixed panel (desktop)
- Mega-menu category dropdowns → accordion within mobile hamburger nav
- Product comparison bar → hidden on mobile, bottom-fixed strip on tablet and above
- Quick-view modal → full-screen sheet on mobile, centered overlay on tablet+
- Breadcrumb → truncates middle path segments with ellipsis on mobile, preserving first and last node

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface confirmed; Open Sans extracted from font stack but may be a Porto/Magento theme default — weight and size hierarchy inferred from catalog norms rather than direct observation
- Exact pixel heights of the dual-tier nav bar not captured; 36px utility bar and 44px category nav estimated from Porto theme conventions
- Hero banner imagery, copy patterns, and section layout not directly observed; assumed to be savings-focused text banners based on brand positioning and page title
- Icon sets (porto-icons, luma-icons) present in font stacks but individual glyph usage in nav and product cards inferred from Magento/Porto conventions, not extracted
- #514943 warm brown present in extracted colors; confirmed as utility-bar token but exact additional usage contexts (promotional element, footer accent, category header) not verified
- #5897fb and #0ae3eb appear in extracted colors but specific UI contexts not confirmed — likely third-party widget chrome (live chat, social login, payment provider)
- Mobile breakpoint behavior inferred from Porto Magento theme patterns; not directly observed from site extraction
- Card hover shadow values estimated; exact box-shadow definition not captured from CSS extraction
- Accent-active (#e04800) derived by darkening #ff5501; not directly extracted from site
