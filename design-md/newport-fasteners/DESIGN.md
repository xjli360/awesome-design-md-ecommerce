---
version: alpha
name: "Newport Fasteners"
source_url: "https://www.newportfasteners.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Newport Fasteners runs on a five-color signal system borrowed from the shop floor: deep navy #163959 anchors structural chrome and header weight, industrial red #bd2426 fires every primary CTA, safety green #9bca3e flags in-stock availability, caution orange #f68b1f marks promotions and quantity-break callouts, and warm amber #f9b169 catches secondary price annotations. The palette reads like hardware-aisle wayfinding — each hue carries a functional meaning rather than an aesthetic one, and the chromatic spread is unusually wide for a B2B catalog site. Typography stays in the system font stack (Arial, Helvetica Neue, sans-serif) at modest weights; no custom typeface is loaded, which keeps the page lean for procurement managers who need to scan part specs without waiting on a font CDN. Buttons are squarely rectangular — `{rounded.xs}` at most — because the interface makes no pretense of softness. Part numbers render in courier monospace so a #10-32 × 1-1/4 socket cap screw visually distinguishes itself from prose at a glance. A persistent #163959 utility strip pinned above the main nav carries the toll-free number, account login, and live cart count — the three controls a returning B2B buyer reaches for before any navigation element. The search bar takes structural prominence in the header, wider than the logo, because the dominant buyer journey is "know the spec, find the SKU, reorder." Category depth is a selling point rather than an admission of complexity: machine screws branch into drive type, then material, then diameter and pitch. The overall register is catalog-functional — dense information, hard edges, zero decorative chrome, and color deployed strictly as a status signal.

colors:
  primary: "#bd2426"
  primary-active: "#521010"
  primary-disabled: "#de5052"
  ink: "#272727"
  body: "#404040"
  muted: "#595959"
  muted-soft: "#737373"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#ebebeb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  navy: "#163959"
  navy-mid: "#2f7bbf"
  navy-light: "#62a1d8"
  green-stock: "#9bca3e"
  green-stock-dark: "#516b1d"
  green-stock-light: "#bada7a"
  orange-promo: "#f68b1f"
  orange-promo-light: "#f9b169"
  orange-hot: "#ee730a"
  orange-dark: "#904b06"
  alert-red: "#de5052"
  utility-gray: "#bfbfbf"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
  utility-bar:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  price-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
  part-number:
    fontFamily: "courier, monaco, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
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
    padding: 8px 16px
    height: 36px
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
    textColor: "{colors.navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 7px 15px
    height: 36px
    border: "1px solid {colors.navy}"
  button-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 6px 10px
    height: 32px
  text-input-focus:
    border: "1px solid {colors.navy-mid}"
    outlineColor: "{colors.navy-light}"
  utility-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.utility-bar}"
    height: 32px
    padding: 0 16px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    boxShadow: "0 4px 8px rgba(0,0,0,0.15)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 36px
    width: "100%"
  search-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0 16px
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 8px
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.navy-mid}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.primary}"
  product-card-part-number:
    typography: "{typography.part-number}"
    textColor: "{colors.muted}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.none}"
  stock-badge-in:
    backgroundColor: "{colors.green-stock}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  stock-badge-out:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  promo-badge:
    backgroundColor: "{colors.orange-promo}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  price-block:
    priceColor: "{colors.primary}"
    priceMsrpColor: "{colors.muted}"
    priceTypography: "{typography.price-lg}"
    unitTypography: "{typography.caption}"
    savingsColor: "{colors.green-stock-dark}"
  breadcrumb:
    textColor: "{colors.navy-mid}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.muted}"
    typography: "{typography.caption}"
  quantity-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 32px
    width: 64px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.navy}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
  alert-bar:
    backgroundColor: "{colors.orange-promo}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 4px 16px
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.navy-light}"
    typography: "{typography.body-sm}"
    padding: 32px 0
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.navy-mid}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 32px
    minWidth: 32px

## Components

### Buttons
**`button-primary`** — Solid #bd2426 red fill, white bold 14px Arial text, 36px tall, 2px radius. Hover deepens to `{colors.primary-active}` (#521010); disabled renders as `{colors.primary-disabled}` (#de5052) with no cursor. The primary action at every funnel step: "Add to Cart," "Buy Now," "Check Out."

**`button-secondary`** — White fill with a 1px #163959 navy border, matching height and radius, navy text. Used for secondary purchase actions ("Request a Quote," "Add to Saved List") and filter reset controls. On hover, navy border intensifies to `{colors.navy-mid}`.

**`button-navy`** — #163959 navy fill, white text, same geometry as the primary. Reserved for account-tier actions ("Sign In," "Create Account," "Track Order") and utility CTAs in the header stripe where the red primary would create signal ambiguity.

### Search
**`search-bar`** — Full-width text field in the header, 36px tall, hairline 1px border, 2px radius. Focus state shifts the border to `{colors.navy-mid}` with a soft `{colors.navy-light}` outline glow. The right edge abuts `search-button` flush, forming a single compound control. This bar is structurally wider than the logo — part-number entry is the primary interaction, not logo recognition.

**`search-button`** — #bd2426 red cap on the right end of the search bar, zero radius, white label or magnifier icon, 14px bold. Shares the 36px height with the input it terminates.

### Navigation
**`utility-bar`** — #163959 navy strip pinned at viewport top, 32px tall, 12px white Arial text. Left: promotional copy or shipping threshold. Right: toll-free phone number, "Sign In / My Account," cart icon with item count badge. Collapses on mobile scroll.

**`nav-bar`** — White 56px bar below the utility strip: logo left, `search-bar` spanning the center, and account/cart icon cluster right. Bottom hairline divides it from the category row. No drop shadow — the hairline is the only separator.

**`nav-dropdown`** — White overlay triggered by top-level category hover, no border radius, 1px hairline border on all sides, 8px box shadow below. Multi-column layout of subcategories in `{typography.body-md}`; active subcategory gets a `{colors.navy-mid}` underline. Closes on mouse-out with no transition delay.

### Product Card
**`product-card`** — Dense rectangular card, zero radius, 1px hairline border, 8px padding. Product image on `{colors.surface-soft}` background at 1:1 ratio occupies the top half. Title in #2f7bbf `{typography.title-sm}` wraps to two lines max. Part number in courier `{typography.part-number}` sits below in muted gray. Unit price in #bd2426 `{typography.price-sm}` anchors the bottom-left; `stock-badge-in` or `stock-badge-out` sits top-right of the image.

**`product-card-part-number`** — Courier monospace at 13px renders spec codes (thread pitch, length, grade) visually distinct from prose, enabling rapid visual scanning across a dense grid. Color is `{colors.muted}` (#595959) to subordinate it below the title without hiding it.

### Price Block
**`price-block`** — The product detail page price zone: `{colors.primary}` red at `{typography.price-lg}` (20px bold) leads, MSRP struck through in `{colors.muted}` alongside, unit descriptor ("/ 100 pcs," "/ box") in `{typography.caption}` to the right. Quantity-break pricing table stacks below in `{typography.body-sm}` with row alternation at `{colors.surface-soft}`. Savings amount renders in `{colors.green-stock-dark}` (#516b1d) — the darkened green signals a positive delta without the urgency of the red.

### Badges
**`stock-badge-in`** — #9bca3e green fill, white bold 12px text, 2px radius. Short text only: "In Stock" or a count ("500+ available"). Green is the same hue used for safety-compliance markings in physical warehouses — the meaning transfers without explanation.

**`stock-badge-out`** — #bd2426 red pill, same geometry as the in-stock badge. "Out of Stock" or "Backordered." Maintaining identical dimensions ensures product-card grid rows do not shift based on availability state.

**`promo-badge`** — #f68b1f orange fill, white bold 12px text, 2px radius. Carries "SALE," "NEW," or quantity-break callouts like "Buy 500+." Sits above the stock badge in visual hierarchy; the orange reads as alerting but not alarming, between the red urgency signal and the green positive signal.

### Category Tile
**`category-tile`** — #ebebeb soft-gray rectangle, zero radius, 1px hairline border, #163959 navy bold 14px title, 8px vertical / 12px horizontal padding. Used on the homepage and category landing pages as a link grid. Hover state: background shifts to `{colors.hairline}` (#dedede). Text-only — no icon or illustration required — keeping the grid maintainable as the category tree evolves.

### Alert Bar
**`alert-bar`** — Full-width #f68b1f orange strip below the nav, 13px white body-sm text centered or left-aligned, 4px top/bottom padding. Used for shipping thresholds ("Free shipping on orders over $99"), site-wide promotions, and lead-time warnings. Can be toggled off server-side without layout shift since it holds no structural role.

### Footer
**`footer`** — #163959 navy background, white `{typography.body-sm}` text, `{colors.navy-light}` (#62a1d8) for anchor links. Four-column layout at desktop: Shop by Category, Resources, Company, Contact. The Contact column presents the toll-free number and email in `{typography.title-sm}` white bold — the footer doubles as a sales contact surface for B2B buyers who scroll to verify legitimacy.

### Pagination
**`pagination`** — Row of 32px square page-number buttons, 2px radius, 1px hairline border, `{colors.navy-mid}` text in `{typography.button-sm}`. Active page fills `{colors.primary}` red with white text. Prev / Next chevron buttons flank the sequence. Tight 4px gap between items keeps the control compact beneath dense product grids.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Utility bar hidden; search bar drops below logo row to full width; hamburger replaces category nav; product grid 2-column; price block stacks vertically; filters collapse to bottom-sheet modal |
| Tablet | 744–1128px | Utility bar shows abbreviated (phone only); category nav compresses to horizontal scroll or single "Categories" dropdown; product grid 3-column; sidebar filters present but narrow |
| Desktop | 1128–1440px | Full utility bar + nav bar + category strip; product grid 4–5 column; left sidebar filters on category pages; mega-menu dropdowns on category hover |
| Wide | > 1440px | Max-width container ~1400px centered; gutters expand; product grid holds at 5-column maximum; no content scaling beyond container |

### Touch Targets
- All buttons minimum 36px tall; primary CTA increases to 44px on mobile
- Quantity stepper +/− controls minimum 40px wide × 36px tall
- Category tiles minimum 44px tall on mobile
- Nav hamburger icon minimum 44×44px hit area
- Pagination buttons increase to 40px on mobile

### Collapsing Strategy
- Category mega-menu collapses to an accordion drawer inside the mobile hamburger panel
- Utility bar phone and account links migrate to the hamburger footer on mobile
- Left-rail category filter sidebar collapses to a slide-up bottom sheet on mobile, triggered by a persistent "Filter" button above the grid
- Breadcrumb truncates to the last 2 levels with an ellipsis on viewports below 744px
- Multi-column footer collapses to a single-column accordion on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned a Cloudflare challenge page — all color and font data extracted from the Cloudflare interstitial, not the live Newport Fasteners storefront; actual brand tokens may differ materially
- No custom typeface detected; system Arial stack confirmed, but the live site may load a commercial font (e.g., Proxima Nova, Open Sans) via CSS not captured in extraction
- No meta theme-color defined; mobile browser chrome color is unspecified
- Logo dimensions, wordmark color, and exact SVG treatment are unconfirmed
- Exact border-radius values for inputs and buttons inferred from industrial-catalog conventions, not measured from live UI screenshots
- Actual heading size ladder (H1–H4) not measured from live product or category pages
- Product photography style (white-background studio vs. contextual) unconfirmed
- Dark mode or high-contrast mode support unknown
- Whether the green (#9bca3e) and orange (#f68b1f) are first-party brand colors or inherited from Cloudflare UI elements cannot be confirmed without live site access
