---
version: alpha
name: "Back to the Roots"
source_url: "https://backtotheroots.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Three distinct typefaces share the page in a combination that only makes sense once you understand the product — Petrona's old-style serifs carry the authority of a nineteenth-century seed catalog, Cabin's open humanist geometry handles everyday "add to cart" copy, and Anonymous Pro's monospaced counters surface on growing-guide timelines and germination data tables, treating horticultural precision with the same gravity a developer gives a version number. Against this typographic layering the dominant brand color is #00abc8 — a chlorinated-pool teal, bracingly synthetic against earthy browns (#744f28) and deep forest greens (#2a472b). That juxtaposition is the whole brand: the vivid artificial nudging the genuinely organic. Canvas defaults to #eae8e4, a warm parchment rather than clinical white, keeping product photography from feeling overlit and making teal CTAs read as invitation rather than command. The rounded vocabulary holds at a moderate {rounded.md} for cards and inputs — human enough to feel approachable, restrained enough not to cartoonify a brand whose audience spans children doing their first windowsill grow kit and adults managing backyard compost. Category tags and trust indicators go to {rounded.full}; product cards carry a faint hairline at #dadada with no drop-shadow, relying on the warm canvas ground to create visual separation. The footer flips to deep forest #2a472b, giving the page a planted quality rather than fading into white infinity. Amber #ff9900 surfaces only on sale badges and urgency callouts, never competing with the teal primary; coral #ed5a4d handles error states and occasionally punctuates editorial blog headers. Olive #5d8b16 and leaf #77b11e build a secondary green spectrum on certification icons and grow-progress indicators that reads ecological rather than decorative. Spacing runs generously in hero sections to let photographic content breathe; product grids tighten to {spacing.md} gutters on mobile, keeping an organic feel without sacrificing density.

colors:
  primary: "#00abc8"
  primary-active: "#00788c"
  primary-disabled: "#b3e6ef"
  deep-teal: "#00abbc"
  earth: "#744f28"
  earth-dark: "#5c3e20"
  forest: "#2a472b"
  forest-mid: "#185e21"
  olive: "#5d8b16"
  leaf: "#77b11e"
  sprout: "#31b44b"
  sprout-dark: "#0b9332"
  ink: "#121212"
  body: "#504545"
  muted: "#565656"
  hairline: "#dadada"
  hairline-soft: "#dedede"
  canvas: "#eae8e4"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  coral: "#ed5a4d"
  amber: "#ff9900"

typography:
  display-xl:
    fontFamily: "'Petrona', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Petrona', Georgia, serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Petrona', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-md:
    fontFamily: "'Cabin', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Cabin', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Cabin', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-sm:
    fontFamily: "'Cabin', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Cabin', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0.2px
  data-label:
    fontFamily: "'Anonymous Pro', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  grow-stat:
    fontFamily: "'Anonymous Pro', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.45
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Cabin', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Cabin', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Cabin', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  badge-label:
    fontFamily: "'Cabin', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
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
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.earth}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.earth}"
  button-earth:
    backgroundColor: "{colors.earth}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "2px solid {colors.primary}"
    errorBorder: "2px solid {colors.coral}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logotypeColor: "{colors.forest}"
    promoBarBackgroundColor: "{colors.forest}"
    promoBarTextColor: "{colors.on-primary}"
    promoBarTypography: "{typography.caption}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 10px 20px
    height: 44px
    iconColor: "{colors.muted}"
    focusBorder: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "1 / 1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.earth}"
    hoverBoxShadow: "0 4px 16px rgba(0,0,0,0.08)"
  category-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.forest}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 12px
    border: "1px solid {colors.hairline}"
  sale-badge:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.forest}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    ctaComponent: "button-primary"
    paddingY: "{spacing.section}"
    imagePosition: right
    maxWidth: 1440px
  grow-guide-callout:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    dataTypography: "{typography.data-label}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    accentColor: "{colors.primary}"
    borderLeft: "4px solid {colors.primary}"
  trust-badge-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    iconColor: "{colors.olive}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    paddingY: "{spacing.lg}"
    gap: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headlineTypography: "{typography.title-sm}"
    linkColor: "{colors.primary}"
    linkHoverColor: "{colors.leaf}"
    paddingY: "{spacing.section}"
  cart-drawer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    totalColor: "{colors.earth}"
    ctaComponent: "button-primary"
  error-message:
    color: "{colors.coral}"
    typography: "{typography.caption}"
    iconColor: "{colors.coral}"

## Components

### Buttons

**`button-primary`** — Teal #00abc8 fill with white text set in Cabin 700 at 15px, 48px tall with {rounded.md} corners. Hover darkens to #00788c; disabled washes to the derived #b3e6ef tint. This is the universal action color — "Shop Now", "Add to Cart", and all checkout progression steps share this spec, so teal reads unambiguously as "do the thing."

**`button-secondary`** — Outlined variant with a 2px earth-brown (#744f28) border on the warm canvas background. Text matches the border color, signaling a secondary tier without receding into neutrality. Typical use: "Learn More", "View All", and grow-guide CTAs placed beside a primary teal action.

**`button-earth`** — Solid warm brown (#744f28) fill with white text. Deployed in editorial and brand-story contexts — "Meet Our Farmers", blog module links, About page — where teal would read as too transactional. Same 48px height as `button-primary`, maintaining a consistent touch target across all CTA types.

**`button-text`** — Inline text link in #00abc8 with underline decoration, no background or border. Used for secondary navigation within content blocks, FAQ answers, and embedded grow-guide cross-references where a full button would interrupt reading flow.

### Text Input

**`text-input`** — 48px field, {rounded.sm} corners, 1px #dadada border on white. Focus ring upgrades to 2px #00abc8 echoing the primary; error state swaps to 2px #ed5a4d coral. Placeholder text at {colors.muted}. Covers email capture, site search before the pill treatment takes over, and all checkout fields.

### Navigation

**`nav-bar`** — White 64px bar with a faint #dedede hairline below. Logo in {colors.forest} deep green. Nav links in Cabin 600 14px. A slim promotional bar above the nav uses the forest green background with white caption-weight text — the standard Shopify pattern for surfacing free-shipping thresholds or seasonal campaign copy without crowding the main header.

**`search-bar`** — Pill-shaped ({rounded.full}), 44px, on a soft surface. Icon in {colors.muted}. Focus activates a 1px teal border. Sits inside the nav on desktop; expands to full-width overlay on mobile.

### Product Card

**`product-card`** — White card, 1px #dadada border, {rounded.md} corners, 1:1 image crop. Title in Cabin 600 15px ({typography.title-sm}); price in Cabin 600 18px ({typography.title-md}) rendered in earth brown. Category badges and sale/new callouts stack at the image's top-left corner. Hover introduces a gentle box-shadow lift without any translateY movement, keeping scroll feel stable on touch devices where hover intent is ambiguous.

### Category Badge

**`category-badge`** — Pill-shaped, {rounded.full}, soft surface fill with forest-green text in Cabin 700 uppercase 11px, 1px #dadada border. Labels product types — "Grow Kits", "Seeds", "Soil", "Mushroom" — and appears across hero sections, filter strips, and product-card overlays without visual conflict because the pill form separates it clearly from rectangular button shapes.

### Hero Banner

**`hero-banner`** — Full-width section on warm #eae8e4 canvas. Headline in Petrona {typography.display-xl} at {colors.forest}; body in Cabin {typography.body-md} at {colors.body}. Desktop shows a 50/50 image-right split; mobile stacks image above headline. Vertical padding at {spacing.section} each side. The warm ground lets product images with transparent backgrounds — soil bags, seed packets, grow-kit boxes — float without a knockout, a meaningful practical advantage for photography-heavy Shopify storefronts.

### Grow Guide Callout

**`grow-guide-callout`** — A {colors.forest} dark panel with {rounded.lg} corners and a 4px #00abc8 left-border accent signaling "information with authority." Headline in Petrona {typography.display-sm} in white; numbered steps in Cabin {typography.body-md}. Germination timing stats and data tables inside use Anonymous Pro {typography.data-label} — the only moment in the UI where the monospace face is visible to users, communicating science-backed claims without making an explicit statement about it.

### Trust Badge Strip

**`trust-badge-strip`** — A horizontal bar on the warm canvas, bordered top and bottom in 1px #dadada, carrying 3–5 certification marks (USDA Organic, B-Corp, Non-GMO Project, Certified Regenerative). Icons in {colors.olive}; labels in Cabin Regular 12px ({typography.caption}). Appears below the hero on the homepage and above the footer on collection pages — an unobtrusive but persistent proof layer.

### Sale and New Badges

**`sale-badge`** — Compact rectangle in amber #ff9900, dark ink text, {rounded.xs}. Positioned absolute at product-card image corner. Fires only on genuinely discounted SKUs, never used decoratively. **`new-badge`** — Same shape in primary teal with white text; marks newly added products and grow-kit seasonal drops.

### Footer

**`footer`** — Deep forest #2a472b background reverses the page to white type. Column heads in Cabin 600 ({typography.title-sm}); body links in Cabin 400 ({typography.body-sm}). Links in #00abc8 teal shift to #77b11e leaf-green on hover, keeping the nature palette coherent in the darkest zone of the page. Padding {spacing.section} per side.

### Cart Drawer

**`cart-drawer`** — Off-canvas panel, 400px wide on desktop, sliding from the right. White surface, 1px hairline left border. Cart totals in Cabin 600 18px rendered in {colors.earth} brown for a warm, receipt-like register of value. Full-width `button-primary` for the checkout step.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Hero stacks image above headline. Nav collapses to hamburger + logo + cart icon. Search expands to full-width overlay. Product grid is 2-column. Trust badge strip scrolls horizontally with snap. Cart drawer goes full-width. |
| Tablet | 744–1128px | Product grid expands to 3-column. Hero side-by-side at narrow 50/50. Nav shows logo + condensed link row + icons, no mega-menu. Grow guide callout goes full-width with reduced padding. |
| Desktop | 1128–1440px | Full nav with all category links visible. 4-column product grid. Hero constrains headline to ~50% with generous image zone right. Trust badge strip stretches to fill row. Cart drawer fixed at 400px. |
| Wide | > 1440px | Content max-width 1440px centered; canvas background fills viewport edges. Column counts and layout hold at desktop values. |

### Touch Targets
- All buttons minimum 48px tall across breakpoints
- Nav icon targets (cart, hamburger, search) minimum 44×44px
- Category badge rows maintain minimum {spacing.sm} gap between items
- Cart quantity stepper buttons minimum 40×40px
- Grow guide step numbers and inline links padded to 44px tap zone

### Collapsing Strategy
- Nav mega-menu (if present) collapses to full-screen overlay drawer on mobile
- Trust badge strip switches from flex-row to horizontal scroll with CSS snap at < 744px
- Grow guide callout drops left-border accent on mobile, retains forest-green block background
- Footer 4-column grid collapses to 2-column on tablet, 1-column accordion on mobile
- Hero image is hidden below 480px when layout is constrained; headline takes full width with increased bottom padding

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `primary-disabled` (#b3e6ef) is a derived tint — no true disabled-state teal was present in the extracted palette
- `earth-dark` (#5c3e20) is a derived shadow tone; actual hover color for earth CTAs not directly confirmed
- No `meta theme-color` was set on the page; PWA and mobile browser chrome color is unknown
- Exact animation timing and easing curves for drawer slide, card hover, and add-to-cart confirmation not extracted
- Shopify checkout pages likely use Shopify's default checkout theming; those surface and button colors may diverge from storefront tokens
- Hover states for nav-link underline and color transitions not directly observed during extraction
- Mega-menu or dropdown nav structure not confirmed; standard Shopify nav assumed
- Exact product-card box-shadow values not extracted; `0 4px 16px rgba(0,0,0,0.08)` is an approximation
- Font weight axis ranges for Petrona and Cabin variable font instances not confirmed; weights listed follow standard brand hierarchy patterns
- Mobile breakpoint pixel values estimated from Shopify Dawn theme defaults, not measured directly from the live site
