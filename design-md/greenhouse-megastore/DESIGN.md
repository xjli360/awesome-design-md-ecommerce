---
version: alpha
name: "Greenhouse Megastore"
source_url: "https://www.greenhousemegastore.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Terracotta and brick divide the brand hierarchy at Greenhouse Megastore before a single product image resolves — #df7a5d (the site's meta theme-color, a warm orange-terracotta) drives every primary CTA and sale signal, while #843134, a deep soil-rich burgundy, anchors price tags, trust strips, and heading weight. Against a near-black backdrop (#121212) in the nav and footer, and a deliberate stack of neutral grays (#f7f7f7, #dedede) for surface hierarchy, the combination reads less like a garden catalog and more like the interior of a serious supply depot: warm enough to invite, earthy enough to signal authority. Figtree, the single typeface, is a geometric sans-serif with softened terminals — at 700 weight for hero display and 600 for UI labels, it carries the confidence of a megastore without the cold register of a hardware chain. Body copy runs at 400/16px with a 1.6 line-height, appropriate for a catalog where customers are comparing glazing specs and frame gauges alongside price. Buttons use `{rounded.sm}` corners throughout — an explicit rejection of the pill-shaped softness that consumer lifestyle brands favor. The 8px radius reads as purposeful and utilitarian: this is a supplier, not a boutique. Primary CTAs in terracotta, outlined secondaries in burgundy, and a full-bleed trust strip in #843134 immediately beneath the nav that front-loads the brand's shipping and warranty commitments before the first product card loads. Product cards sit on white with a 1px #dedede hairline border; the only non-neutral element is the price, rendered in burgundy at 22px/700, optimized for rapid price-scanning in a dense grid. Category tiles use a light gray (#f7f7f7) field with a thin terracotta top-edge bar to signal navigation depth across a sprawling SKU inventory — greenhouses, raised beds, cold frames, accessories — without relying on imagery to carry the hierarchy. The dark nav and footer bracket the page, giving a 700+ SKU megastore a composed, structured feel that prevents the product volume from reading as chaos.

colors:
  primary: "#df7a5d"
  primary-active: "#c55d3e"
  primary-disabled: "#f0c0ae"
  accent: "#843134"
  accent-active: "#6b2528"
  ink: "#121212"
  body: "#323232"
  muted: "#444444"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    padding: 13px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.accent}"
    borderColor: "{colors.accent}"
    borderWidth: 2px
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 26px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    typography: "{typography.body-md}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
  trust-strip:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    overlayOpacity: 0.4
    minHeight: 500px
    ctaLabel: "button-primary"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    imageRadius: "{rounded.xs}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.accent}"
    padding: "{spacing.base}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  promo-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    accentBarColor: "{colors.primary}"
    accentBarHeight: 3px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    height: 44px
    typography: "{typography.body-md}"
    iconColor: "{colors.muted}"
    focusBorderColor: "{colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    separatorColor: "{colors.hairline}"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "transparent"
    inactiveTextColor: "{colors.body}"
    rounded: "{rounded.xs}"
    typography: "{typography.button-sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"

## Components

### Buttons

**`button-primary`** — The terracotta (#df7a5d) CTA is the universal commit signal: "Add to Cart," "Shop Now," "Get a Quote." At 48px tall with {rounded.sm} corners and 600-weight Figtree, it reads as confident without being aggressive. Hover darkens to {colors.primary-active} (#c55d3e); the disabled state fades to a pale {colors.primary-disabled}, preserving the terracotta hue while removing affordance.

**`button-secondary`** — An outlined button in burgundy ({colors.accent}, #843134) for secondary actions — "Learn More," "View Details," "Compare." The 2px border at the same 48px height as the primary creates a clean visual hierarchy in dual-CTA product hero layouts without the secondary bleeding visual weight into the primary.

**`button-ghost`** — Text-only in {colors.body} for low-stakes actions: "Cancel," "Clear Filters," wishlist toggles on product cards. No border, no fill, no padding.

### Navigation

**`nav-bar`** — Near-black (#121212) with white type in {typography.nav-link}. The dark band establishes a clear ceiling to the page and carries the brand's supplier-grade seriousness without decorative chrome. At 60px the nav is compact and product-first; there is no search-bar folded into the nav at desktop — search occupies its own strip or a modal trigger.

**`trust-strip`** — Full-bleed burgundy ({colors.accent}) bar anchored immediately below the nav bar, announcing free shipping thresholds, return windows, and warranty terms in {typography.body-sm} white. It loads before first product content, front-loading the brand's key commitments in the first 24px of scroll space — a persuasion move common among functional megastores that compete on service, not aesthetics.

### Cards

**`product-card`** — White surface with a 1px {colors.hairline} border and {rounded.sm} corners. Product photography occupies the full card width with {rounded.xs} image clipping. Title in {typography.title-sm}, price in {typography.price-display} at 22px/700 in {colors.accent} burgundy — the price is the only non-neutral element in the card, ensuring cost legibility at a glance in dense 3–4 column grid views.

### Badges

**`sale-badge`** — Terracotta ({colors.primary}) filled chip, {typography.badge} (11px, 700, uppercase), {rounded.xs} corners, pinned to the top-left of product card images during sale events and clearance sections. The terracotta mirrors the CTA button color, signaling urgency through the same visual vocabulary as the "Buy" action.

**`promo-badge`** — Burgundy ({colors.accent}) variant of the sale badge, used for "NEW," "BEST SELLER," and featured-category callouts. The terracotta/burgundy split lets sale and editorial promotional signals coexist in a product grid without colliding.

### Discovery

**`category-tile`** — Light gray ({colors.surface-soft}) card with a 3px terracotta accent bar running across the top edge — a low-cost signal of active or featured status that doesn't require iconography or imagery. Title in {typography.title-md}, {rounded.sm} corners. Organizes the megastore taxonomy (Greenhouses, Raised Beds, Cold Frames, Shade Structures, Accessories) into a scannable grid on the homepage and category landing pages.

**`search-bar`** — White input with {colors.hairline} border, placeholder text in {colors.muted}. Focus state replaces the border with the terracotta {colors.primary} highlight — the only form interaction that uses the primary accent. Paired with a muted {colors.muted} search icon at the trailing edge. On desktop, typically housed in a dedicated bar above the nav or in a top-of-page strip; on mobile, promoted below the collapsed nav.

**`breadcrumb`** — Horizontal navigation path in {typography.body-sm}. Ancestor segments in {colors.muted}; the current page segment in {colors.ink}. Hairline-colored `›` separators. Essential wayfinding for a megastore where customers may drill four levels deep (Greenhouses → Glass Greenhouses → Lean-To → 6×8).

### Utility

**`pagination`** — Compact number row beneath product grids. Active page: {colors.primary} fill with {colors.on-primary} text. Inactive pages: transparent with {colors.body} text. {rounded.xs} corners. Typography in {typography.button-sm} keeps the row tight and grid-proportionate.

**`footer`** — Near-black (#121212) mirroring the nav, with {colors.on-dark} base text, {colors.hairline} for secondary link lists, and {colors.primary} terracotta on link hover. Headings in {typography.title-sm}, link lists in {typography.body-sm}. The matched dark top/bottom bands bracket the full page and give a high-SKU catalog a composed, structured quality that photographic product grids alone cannot.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replacing full category menu; trust strip condenses to one line or scrolls horizontally; hero headline scales to ~28px; search bar moves below nav bar |
| Tablet | 744–1128px | 2–3 column product grid; nav may remain full horizontal or collapse to hamburger depending on category count; hero at 400px minimum height |
| Desktop | 1128–1440px | Full horizontal nav with fly-out category dropdowns; 3–4 column product grid; hero at 500px minimum height; trust strip at full legibility |
| Wide | > 1440px | Content constrained to 1440px max-width; side margins expand symmetrically; hero may scale to 600px; product grid holds at 4 columns |

### Touch Targets
- All buttons and inputs minimum 44px tall for tap safety
- Category tiles minimum 44px tap area regardless of visual height
- Nav bar at 60px provides adequate tap clearance for all nav links
- Pagination buttons maintain minimum 36px width × 44px height

### Collapsing Strategy
- Full desktop horizontal nav collapses to a hamburger drawer on mobile with hierarchical category accordion inside
- Product grid: 4-col → 3-col → 2-col → 1-col across breakpoints
- Hero display typography scales from 48px (desktop) to 28px (mobile) via fluid or stepped scaling
- Trust strip wraps gracefully to two lines on mobile rather than truncating
- Category tile grid: 4-col → 3-col → 2-col on mobile, stacking vertically if needed

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Canvas/page background white (#ffffff) inferred from Shopify theme defaults — not present in extracted hex list
- Exact production button border-radius not confirmed; {rounded.sm} (8px) assumed from Shopify Dawn/Figtree theme conventions
- Navigation structure depth (number of dropdown levels, mega-menu vs. fly-out) not extractable from color/font pass
- Whether an announcement bar or promotional banner sits above the nav bar is not confirmed
- Icon set style (outlined, filled, custom SVG, or emoji-adjacent) not detectable from extraction
- Hover and transition animation timing/easing values not extracted
- Mobile navigation pattern (slide drawer, full-screen overlay, accordion) not confirmed
- Figtree loading strategy (Google Fonts CDN vs. self-hosted) not confirmed
- Product grid gutter and column gap exact values not extracted
- Dark-mode or high-contrast mode support not detected
