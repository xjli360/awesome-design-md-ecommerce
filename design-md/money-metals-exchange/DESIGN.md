---
version: alpha
name: "Money Metals Exchange"
source_url: "https://www.moneymetals.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Spot price tickers cycling live gold, silver, platinum, and palladium quotes define the header before a single product image loads — Money Metals Exchange reads as a commodity desk first and a retail shop second. The confirmed dark charcoal (#313131) anchors the typographic system as the primary ink color, giving pricing tables and editorial body copy alike a dense, newspaper-authority weight. System fonts throughout (-apple-system, Helvetica Neue, Roboto, sans-serif) keep the interface free of brand risk: no custom typeface means no licensing overhead, and the utilitarian stack signals institutional seriousness rather than lifestyle aspiration. Primary interactive elements — "Add to Cart," "Buy Now," and pricing CTAs — reach for a gold-adjacent amber consistent with the physical product category, making every conversion moment a visual echo of the metal itself. Cards lean toward rectangular with minimal rounding ({rounded.xs}), projecting the rectilinear geometry of bullion bars over the soft corners of consumer brands. Trust signals are architectural, not decorative: BBB rating, money-back guarantees, and secure-checkout badges are placed in fixed proximity to purchase flows rather than relegated to the footer. The color temperature is cool and institutional — white canvas with charcoal text, gold accents, and occasional muted silver-gray panels ({colors.surface-soft}) that echo the appearance of a certified coin slab. Educational editorial content (guides to buying gold, IRA rollovers, market commentary) sits in a second navigation tier, signaling a brand that sells conviction alongside metal. Responsive breakpoints collapse the live-price ticker into a scrollable marquee on mobile, where the product grid shifts from three columns to a single-column stacked layout with persistent sticky buy buttons. The overall experience is transactional confidence: every pixel earns the user's trust that they are purchasing real, certified precious metals from a regulated dealer.

colors:
  primary: "#b8860b"
  primary-active: "#9a7009"
  primary-disabled: "#e8d5a3"
  primary-dark: "#8b6914"
  ink: "#313131"
  body: "#444444"
  muted: "#6b6b6b"
  muted-soft: "#9a9a9a"
  hairline: "#d9d9d9"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#1a2a3a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  gold: "#d4af37"
  silver: "#aaaaaa"
  price-up: "#2e7d32"
  price-down: "#c62828"
  trust-blue: "#1a3a5c"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  price-spot:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  ticker-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  table-header:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase

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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-buy-now:
    backgroundColor: "{colors.trust-blue}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    height: 40px
    padding: "0 {spacing.sm}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 52px
    secondaryBarBg: "{colors.canvas}"
    secondaryBarBorder: "1px solid {colors.hairline}"
  spot-price-ticker:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.ticker-label}"
    height: 36px
    metalNameColor: "{colors.gold}"
    priceUpColor: "{colors.price-up}"
    priceDownColor: "{colors.price-down}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    imageAspectRatio: "1:1"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    premiumColor: "{colors.muted}"
  product-table:
    backgroundColor: "{colors.canvas}"
    headerBg: "{colors.surface-soft}"
    headerTypography: "{typography.table-header}"
    headerColor: "{colors.muted}"
    rowTypography: "{typography.body-sm}"
    rowColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rowBorder: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    activeRowBg: "#fff8e1"
    activeRowBorderLeft: "3px solid {colors.primary}"
  metal-badge-gold:
    backgroundColor: "#fff8e1"
    textColor: "{colors.primary-dark}"
    border: "1px solid {colors.primary-disabled}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  metal-badge-silver:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  metal-badge-platinum:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.silver}"
    minHeight: 420px
    contentMaxWidth: 1200px
  trust-badge-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.primary}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md} {spacing.xl}"
    iconSize: 24px
  price-calculator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    labelTypography: "{typography.title-sm}"
    resultTypography: "{typography.price-display}"
    resultColor: "{colors.primary}"
  ira-section:
    backgroundColor: "{colors.trust-blue}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    accentColor: "{colors.gold}"
  editorial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    titleTypography: "{typography.title-md}"
    categoryColor: "{colors.primary}"
    categoryTypography: "{typography.caption}"
    imageAspectRatio: "16:9"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "#cccccc"
    linkColor: "#eeeeee"
    headingColor: "{colors.on-dark}"
    bodyTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.section} {spacing.xl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Gold-amber (#b8860b) fill with white text at 44px height and 4px radius, used for "Add to Cart" and immediate buy actions across the catalog. The amber directly echoes the physical product category, making every purchase CTA a visual reference to the metal being sold. Hover darkens to `{colors.primary-active}` (#9a7009); disabled state washes to pale amber `{colors.primary-disabled}`.

**`button-buy-now`** — Institutional navy `{colors.trust-blue}` fill at 48px height for high-commitment CTAs like "Buy Now" on product detail pages. The heavier height and cooler navy signal a more serious, irreversible commitment than adding to cart. Pairs with `button-secondary` to give users a lower-pressure alternative on the same flow.

**`button-secondary`** — White canvas with `{colors.ink}` text and a 1px `{colors.hairline}` border, matching `button-primary` in height (44px). Used for "Learn More," "Download Guide," and secondary navigation actions where the gold CTA needs a lower-contrast companion without competing for attention.

### Navigation
**`nav-bar`** — Two-tier structure: a dark `{colors.surface-dark}` primary bar housing the logo, top-level category links (Gold, Silver, Platinum, Palladium, IRA, News), and account/cart controls; a lighter `{colors.canvas}` secondary bar for subcategory drill-down with a 1px `{colors.hairline}` bottom border. The dark primary bar establishes institutional authority immediately, before the white content canvas opens below it.

### Spot Price Ticker
**`spot-price-ticker`** — A full-width strip in near-black `{colors.ink}` running above the primary nav, displaying live spot prices for all four metals. Metal names render in `{colors.gold}` via `{typography.ticker-label}` (12px uppercase, 0.5px tracking); price values use `{colors.price-up}` (green) or `{colors.price-down}` (red) to show intraday direction at a glance. This bar is the first element encountered on load, framing the site as a live market interface — not a static catalog.

### Product Cards
**`product-card`** — Minimal border card with `{rounded.xs}` (2px radius) and a 1:1 product image. Product name renders in `{typography.title-sm}`, price-per-unit in `{typography.price-display}` colored `{colors.primary}`, and a smaller premium line in `{colors.muted}`. Three-column grid on desktop, two-column on tablet, single-column on mobile. A 1px `{colors.hairline}` border replaces drop shadows to keep high-density catalog pages visually tight and scannable.

### Product Table
**`product-table`** — Dense pricing grids showing quantity breakpoints, unit price, total cost, and premium over spot. Column headers use `{typography.table-header}` (11px uppercase, 0.8px tracking) over `{colors.surface-soft}`; row text in `{typography.body-sm}` on white. The active/selected quantity row highlights in pale amber (#fff8e1) with a 3px `{colors.primary}` left border accent, drawing the eye to the currently selected tier. This component is central to the brand's value proposition: transparent, comparative bulk pricing rewarding larger buyers.

### Metal Badges
**`metal-badge-gold`** — Warm amber-tinted chip (#fff8e1 background, `{colors.primary-dark}` text) that identifies gold product listings. **`metal-badge-silver`** and **`metal-badge-platinum`** use progressively cooler neutral backgrounds to mirror the physical properties and market temperature of each metal. All variants use `{typography.caption}` at 2px/8px padding with `{rounded.xs}` — compact enough to sit inline with product titles or table rows without displacing surrounding text.

### Hero
**`hero`** — Dark navy `{colors.surface-dark}` full-width banner with a display headline in `{typography.display-xl}` (white), supporting text in muted `{colors.silver}`, and paired CTA buttons. Minimum 420px height accommodates product photography or illustrated bullion imagery. The dark background creates maximum contrast for the gold `button-primary` CTA — making the first conversion moment the visually dominant event on the page.

### Trust Badge Bar
**`trust-badge-bar`** — A horizontal strip in `{colors.surface-soft}` placed immediately below the hero or directly above "Add to Cart" on product pages, housing 3–4 trust signals (BBB Accredited, Secure Checkout, Free Shipping threshold, Money-Back Guarantee). Icons are 24px in `{colors.primary}` gold; labels in `{typography.body-sm}`. The placement — always adjacent to the purchase zone — treats trust as transactional infrastructure, not decorative reassurance.

### Price Calculator
**`price-calculator`** — Interactive widget on product detail and editorial pages for computing total cost at various quantities. Input fields follow `text-input` styling; result lines render in `{typography.price-display}` colored `{colors.primary}`. The widget sits in a `{colors.surface-soft}` panel with 1px `{colors.hairline}` border, 6px radius (`{rounded.md}`), and `{spacing.xl}` padding — visually separated from the product description but within the right-rail purchase zone.

### IRA Section
**`ira-section`** — Full-bleed navy panel (`{colors.trust-blue}`) for Gold IRA and Precious Metals IRA promotional blocks. White headline in `{typography.display-md}`, body in white `{typography.body-md}`, and a gold `button-primary` CTA. The `{colors.gold}` accent may appear in subheadlines or thin decorative rules to reinforce the metals theme within the institutional navy field. This section signals product category breadth beyond retail coin sales.

### Editorial Card
**`editorial-card`** — Article preview cards for the Money Metals Insider newsletter and market commentary. 16:9 image at top, category label in `{colors.primary}` using `{typography.caption}`, title in `{typography.title-md}`, excerpt in `{typography.body-sm}`. A thin 1px `{colors.hairline-soft}` border and `{rounded.xs}` corners keep the cards consistent with the catalog grid aesthetic. Used in a three-column layout on desktop, single-column on mobile.

### Footer
**`footer`** — Near-black `{colors.ink}` background with a 3px `{colors.primary}` gold top border as the sole decorative element — the gold accent bookends the page against the top ticker bar, creating visual closure. Four-column link grid on desktop with section headings in `{typography.title-sm}` white and links in medium gray (#cccccc) `{typography.body-sm}`. Houses legal copy, regulatory disclosure, payment method icons, and newsletter signup.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Spot price ticker collapses to auto-scrolling marquee; nav collapses to hamburger with full-screen drawer; product grid single-column; "Add to Cart" floats as sticky bottom bar on product detail; price tables scroll horizontally with product name column frozen left |
| Tablet | 744–1128px | Ticker shows all four metals statically; nav shows top-level categories with sub-nav on tap; product grid two-column; price calculator stacks below main product info |
| Desktop | 1128–1440px | Full two-tier nav with hover mega-menus; three-column product grid; price calculator in right-rail sidebar on product detail pages |
| Wide | > 1440px | Content constrained to 1200px max-width centered on `{colors.canvas}`; ticker, hero, and footer backgrounds extend edge to edge |

### Touch Targets
- All CTA buttons minimum 44px height
- Nav items in mobile drawer minimum 48px tap target
- Quantity stepper inputs minimum 44px × 44px
- Table rows on mobile minimum 44px row height for comfortable selection
- Cart and account icons in mobile nav bar minimum 44px × 44px hit area

### Collapsing Strategy
- Primary nav collapses to hamburger at < 744px; secondary nav folds into accordion within the full-screen drawer
- Spot price ticker transitions from static bar (≥ 744px) to auto-scrolling marquee (< 744px), cycling one metal at a time
- Product comparison table collapses to horizontal scroll with the product name column frozen left
- Hero shifts from side-by-side text+image to stacked text-over-image at < 744px
- Trust badge bar collapses to a 2×2 grid on mobile, then to a single-column vertical stack at very narrow widths
- Price calculator moves from right-rail to full-width below product images on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extractable due to anti-bot protection ("Just a moment..." Cloudflare challenge page); the full palette is approximated from precious metals category conventions — all colors beyond `{colors.ink}` should be treated as provisional
- No confirmed primary brand color; gold-amber (#b8860b) is a category-logical inference for a precious metals dealer, not a documented brand hex value
- No custom brand typeface detected; system font stack confirmed, but specific weight pairings and size scales used on the live site remain unverified
- Navy `{colors.trust-blue}` (#1a3a5c) is an approximation of the site's dark header and promotional panel color
- Price-up/price-down green and red are standard financial convention, not confirmed brand-specified values
- Spot price ticker scroll speed, metal ordering, and price-change animation behavior could not be observed
- No meta theme-color was present, suggesting dynamic theming or non-standard header implementation
- IRA section layout, editorial card grid structure, and footer column count are inferred from the brand's known product focus rather than live page observation
