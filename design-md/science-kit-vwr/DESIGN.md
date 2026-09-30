---
version: alpha
name: "Science Kit (VWR)"
slug: science-kit-vwr
source_url: "https://www.sciencekit.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Thousands of catalog entries — dissection trays, refraction prisms, live butterfly larvae — sorted first by grade band and subject before anything commercial, an ordering that reveals the brand's dual audience. Science Kit (VWR's K-12 educational division) serves purchasing administrators and classroom teachers simultaneously, so the primary blue (#0052a5, VWR's institutional anchor) carries nav, primary CTAs, and category headers with the flat authority of a purchase order. A warm amber-orange (#e86c00) fires on grade-level badges, sale chips, and Add-to-Cart buttons, doing the affective work the blue cannot — it is the only element in the palette that signals that the end user is a twelve-year-old watching a chemical reaction rather than a procurement officer reconciling line items. Type runs on a system sans-serif stack (Arial, Helvetica) for all UI chrome and body copy, with Georgia serif reserved for editorial display headings in hero banners — a pairing that maps cleanly onto the brand's split register: clipboard-functional for product specs, marginally warmer when a landing page needs to sell the excitement of a volcano kit. Corner radii stay conservative throughout: {rounded.sm} at 4px on buttons and inputs, {rounded.md} at 6px on product cards. No pill softness, no generous rounding — the geometry reads catalog-institutional rather than consumer-marketplace. Product cards surface SKU codes in monospaced type directly beneath the image, flagging that the primary buyer reaches for a reorder number rather than browsing by thumbnail. Safety classification badges in {colors.safety-red} appear on chemistry and biology kits as first-class elements with visual weight comparable to an OSHA sticker — never a soft informational chip. The search bar spans full header width on desktop because with thousands of items across dozens of disciplines, search is the default navigation mode, not category browse.

colors:
  primary: "#0052A5"
  primary-active: "#003D7A"
  primary-disabled: "#99BBD9"
  accent: "#E86C00"
  accent-soft: "#FFF3E6"
  accent-active: "#C45900"
  ink: "#1A1A1A"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#DDDDDD"
  hairline-soft: "#EEEEEE"
  canvas: "#FFFFFF"
  surface-soft: "#F4F7FB"
  surface-card: "#FFFFFF"
  surface-warm: "#FDF6EF"
  on-primary: "#FFFFFF"
  success: "#2E7D32"
  success-soft: "#E8F5E9"
  error: "#C62828"
  safety-red: "#D32F2F"
  promo-yellow: "#FFC107"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  nav-utility:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  sku-label:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.5px
  price-display:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, Helvetica, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-primary-hover:
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
    padding: 8px 18px
    height: 40px
  button-add-to-cart:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-add-to-cart-hover:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 6px 14px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 38px
    focusBorder: "1px solid {colors.primary}"
  nav-top-utility:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-utility}"
    height: 30px
    padding: 0 {spacing.xl}
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 48px
    padding: 0 {spacing.xl}
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 8px 40px 8px 12px
    height: 40px
    searchIconColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
    imageAspectRatio: "4/3"
    hoverBorder: "1px solid {colors.primary}"
  product-card-sku:
    textColor: "{colors.muted}"
    typography: "{typography.sku-label}"
  product-card-price:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  product-card-sale-price:
    textColor: "{colors.accent}"
    typography: "{typography.price-display}"
  product-card-original-price:
    textColor: "{colors.muted}"
    typography: "{typography.price-sm}"
    textDecoration: line-through
  grade-band-badge:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  subject-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  safety-badge:
    backgroundColor: "{colors.safety-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  new-badge:
    backgroundColor: "{colors.promo-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  sale-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  sku-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.sku-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 360px
  hero-banner-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  kit-highlight-card:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 4px 14px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 4px 14px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline-soft}"
    activeTextColor: "{colors.ink}"
  stock-in:
    textColor: "{colors.success}"
    typography: "{typography.caption}"
    iconSize: 10px
  stock-out:
    textColor: "{colors.error}"
    typography: "{typography.caption}"
    iconSize: 10px
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    height: 38px
    buttonWidth: 32px
  promo-banner:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    width: 240px
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 10px
  footer:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Solid #0052a5 fill, white label at `{typography.button-md}` (Arial 15px bold), 4px radius, 40px height. Hover darkens to `{colors.primary-active}` (#003d7a) with no elevation change; disabled state fades to `{colors.primary-disabled}`. Used for account actions, checkout steps, and catalog navigation CTAs.

**`button-add-to-cart`** — The amber-orange (#e86c00) variant at identical dimensions to `button-primary`. This is the most prominent interactive element on product pages; it is deliberately the only non-blue interactive surface so that the commercial action reads instantly against institutional blue chrome. Hover deepens to `{colors.accent-active}`.

**`button-secondary`** — White fill with a 2px `{colors.primary}` border and primary-colored label. Used for secondary actions like "Save to List" or "Request Quote" alongside the primary Add-to-Cart.

**`button-ghost`** — Transparent fill, hairline border, primary-colored label at `{typography.button-sm}`, 32px height. Appears in filter panels, bulk-action toolbars, and pagination adjacents.

### Navigation

**`nav-top-utility`** — A 30px utility strip in `{colors.primary-active}` (darker blue) sitting above the main nav. Carries account links, phone number, and order-status text at `{typography.nav-utility}` in white. On mobile it collapses entirely.

**`nav-bar`** — 48px bar in `{colors.primary}`. Category labels render at `{typography.nav-link}` (Arial 14px bold, white). Hover reveals a `{nav-mega-menu}` panel that organizes subcategories by science discipline columns. The logo and a full-width `{search-bar}` sit in a white band directly above `nav-bar` rather than inline with it.

**`nav-mega-menu`** — White panel dropping below the nav with a subtle shadow and hairline border. Column headers match `{typography.title-sm}`; subcategory links use `{typography.body-sm}`. No images or featured products — the mega-menu is purely a category-tree navigation, reflecting catalog depth over merchandising ambition.

### Search

**`search-bar`** — Spans the full logo band on desktop (approximately 600px wide). White fill, hairline border, 4px radius, blue search-icon button on the right end. Autocomplete suggestions surface product names, catalog categories, and SKU direct-hits. On mobile it collapses to an icon that expands a full-width overlay.

### Product Card

**`product-card`** — White card, 1px hairline border, 6px radius. Image at 4:3 ratio occupies the top half. Below: `{product-card-sku}` in monospaced gray, then product name at `{typography.title-sm}`, then pricing row. Grade-band badges (`{grade-band-badge}`) and safety badges (`{safety-badge}`) stack over the top-left corner of the image. On hover the border shifts to `{colors.primary}` blue to indicate selection affordance. Quantity stepper and Add-to-Cart button appear below the price row — optimized for bulk re-ordering from the card without entering the PDP.

**`product-card-sku`** — Monospaced 11px gray text renders the item number directly below the image, before the product title. This ordering is deliberate: returning buyers locate items by catalog number, not by name.

### Badges and Labels

**`grade-band-badge`** — Amber-soft background (#fff3e6) with amber text, uppercase 11px bold, 2px radius. Values: "Grades K–2", "Grades 3–5", "Grades 6–8", "Grades 9–12". Appears on product cards and PDP headers.

**`subject-badge`** — Light blue-gray background (`{colors.surface-soft}`) with primary-blue text. Indicates discipline: Biology, Chemistry, Physics, Earth Science, STEM.

**`safety-badge`** — Solid `{colors.safety-red}` (#d32f2f), white uppercase label. Applied to kits containing chemicals, sharp instruments, or living organisms. Treated as a regulatory element, not a decorative chip — it carries full visual weight alongside the product title.

**`new-badge`** and **`sale-badge`** — Yellow (#ffc107) and amber-orange respectively, sitting in the top-right corner of product card images. Both use `{typography.badge}` at 2px radius.

### Hero and Promotions

**`hero-banner`** — Full-bleed `{colors.primary}` (blue) panel, display heading in Georgia serif at `{typography.display-xl}`, white text, minimum 360px height. Used for seasonal campaigns (Back to School, Spring Science, STEM Month). A secondary `{hero-banner-accent}` variant in `{colors.accent}` orange fires for sale events and catalog launches.

**`promo-banner`** — Single-line amber-orange strip at the very top of the viewport, above `{nav-top-utility}`, carrying shipping threshold or discount codes at `{typography.body-sm}`. Dismissible with an ×.

**`kit-highlight-card`** — Off-white warm surface (`{colors.surface-warm}`), hairline border, 6px radius, used in curated "Complete Lab Kits" or "Grade-Level Bundles" editorial sections. Combines image, title at `{typography.title-md}`, a brief description, grade badge, and a ghost CTA button.

### Filtering and Catalog

**`filter-sidebar`** — 240px left panel on desktop catalog pages. Accordion sections for Grade Band, Subject, Kit Type, Price Range, and Standards Alignment. Each section header at `{typography.title-sm}`, options at `{typography.body-sm}` with checkbox inputs.

**`category-chip`** — Pill-shaped chips above search results for quick subject-filtering. Inactive state is surface-soft with a hairline border; active state fills `{colors.primary}` with white text. The only pill-radius element in the UI — contrast against otherwise square-edged components signals a toggle rather than a navigation action.

**`breadcrumb`** — Gray `{typography.caption}` links separated by `/` hairline text. Always present on PDPs and category pages given deep catalog nesting (e.g. Science Kits → Biology → Dissection → Frog).

**`pagination`** — Numbered pages at `{typography.body-sm}`, active page filled `{colors.primary}`, 4px radius. Previous/next as ghost buttons. Catalog pages default to 24 items with a per-page selector (24/48/96) for bulk purchasing workflows.

### Stock and Pricing

**`stock-in`** / **`stock-out`** — Inline caption-size status below the price. Green checkmark (#2e7d32) for in-stock, red error (#c62828) for out-of-stock. Back-order availability dates appear alongside out-of-stock status.

**`quantity-stepper`** — Minus/plus flanking a text input, hairline border, 4px radius, 38px height. Defaults to 1; allows large quantities for classroom purchasing (sets of 30, cases of 100). Validates against min-order quantities where enforced by catalog rules.

### Footer

**`footer`** — Dark `{colors.primary-active}` (#003d7a) panel, 4-column grid on desktop: Shop by Category, Customer Service, About VWR Education, Connect. All links at `{typography.body-sm}` white. Section heads at `{typography.title-sm}` white bold. Bottom bar carries copyright, legal links, and accessibility statement.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; search bar expands to overlay; `nav-bar` collapses to hamburger icon; filter sidebar becomes bottom sheet; `nav-top-utility` hidden; hero min-height drops to 220px |
| Tablet | 744–1128px | 2-column product grid; search bar in collapsed icon form in nav; filter sidebar appears as horizontal chip strip above results rather than left panel; mega-menu replaced with full-screen drawer |
| Desktop | 1128–1440px | 3-column product grid; full `filter-sidebar` at 240px left; logo band + search bar + `nav-bar` stacked in header; mega-menu enabled |
| Wide | > 1440px | 4-column product grid; max content width 1400px centered; hero banner text column constrains to 700px rather than stretching full width |

### Touch Targets

- All `button-primary`, `button-add-to-cart`, `button-secondary` maintain 40px minimum height on all breakpoints
- `quantity-stepper` minus/plus buttons expand to 44px × 44px on mobile
- Category chip rows become horizontal scroll containers on mobile rather than wrapping
- Filter checkboxes use 36px tall touch targets on mobile even if visually compact

### Collapsing Strategy

- Header collapses top-down: `promo-banner` → `nav-top-utility` → logo/search band compresses → `nav-bar` becomes hamburger
- Filter sidebar becomes an off-canvas drawer triggered by a "Filter" chip button above results
- Mega-menu becomes a full-screen slide-in drawer with accordion category sections on tablet and mobile
- Product card quantity stepper and Add-to-Cart stack vertically below the price on screens narrower than 400px
- Footer columns collapse to a single accordion on mobile, all sections closed by default except "Customer Service"

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the site returned zero CSS custom properties or inline color values during extraction. All palette values in this file are cautious estimates based on VWR's publicly documented institutional blue and STEM educational context. Do not treat any hex value here as authoritative without live verification.
- **No font stacks extracted** — typography assignments (Georgia serif for display, Arial for UI) are inferred from the brand's institutional category and common patterns for educational supply catalogs. Actual webfonts may differ entirely.
- **Exact primary blue unconfirmed** — #0052a5 is used as VWR's widely referenced corporate blue but the Science Kit sub-brand may use a lighter or warmer variant. Verify against a screenshot of the live nav bar.
- **Accent orange unconfirmed** — #e86c00 is an estimated STEM-appropriate amber. The live site may use red, green, or a different warm hue for sale/accent treatments.
- **No theme-color meta tag** — no browser chrome color was declared, removing one additional color signal.
- **Platform unknown** — the site is not confirmed as Shopify; checkout and cart component patterns may differ from standard e-commerce conventions assumed here.
- **Pricing and procurement rules** — quantity discount tiers, min-order enforcement, and quote-request flows are not documented here; product-card and stepper components may need additional states.
- **Standards alignment filter** — many educational supply sites filter by NGSS/Common Core alignment; if present, this filter requires additional badge and tag tokens not included above.
