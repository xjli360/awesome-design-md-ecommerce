---
version: alpha
name: "Huion"
source_url: "https://www.huion.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The first visual signal is #00bfd6 — a digital cyan sitting at the exact intersection of teal and aqua, with no warmth softening its edge. Huion wraps a highly technical drawing-tablet catalog in a framework-derived visual system (Element UI) whose neutral ramp runs from #303133 body copy through #606266 secondary text, #909399 placeholder labels, and #c0c4cc disabled states — a precise descending scale that keeps every surface cool and recessive until that single cyan lands on a button, a badge, or a promo bar. The deliberateness signals an audience that reads spec sheets: customers comparing 8192-level pressure sensitivity against 60ms report rates don't need visual interference.

  Aileron carries the type, a geometric sans-serif with proportions close to Futura but apertures opened enough for small-size legibility. At weight 700 it reads as engineering precision rather than editorial force; display headlines step from 48px hero scale through 32px section titles and 18px card titles with no dramatic contrast jumps. The Aileron-Bold variant is reserved for product names and pricing — the moments that need to hold against photography. Button labels and nav links sit at 500 weight, between reading and calling.

  Rounded corners are restrained: buttons and inputs use {rounded.xs} (4px) rather than the pill shapes common in consumer apps, placing Huion squarely in professional-tools territory. Product cards sit on white surfaces with 1px borders and barely-there shadows; the pen displays and tablets do the selling. Hero banners run edge-to-edge with near-black backgrounds and product photography that makes the screen glow from within. The brand's status palette — #67c23a success, #f56c6c alert, #e6a23c warning, #409eff info — is lifted from Element UI's semantic layer, freeing the cyan to mean exactly one thing: Huion action. Soft teal #aadddd serves as the primary's disabled sibling, keeping color logic within a single family. An extracted #ffff00 appears in campaign overlays but belongs to imagery rather than to the system.

colors:
  primary: "#00bfd6"
  primary-active: "#00a8bc"
  primary-disabled: "#aadddd"
  ink: "#111111"
  ink-soft: "#222222"
  body: "#303133"
  muted: "#606266"
  muted-soft: "#909399"
  disabled: "#c0c4cc"
  hairline: "#dcdfe6"
  hairline-soft: "#e4e7ed"
  canvas: "#ffffff"
  surface-soft: "#f5f7fa"
  surface-page: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#67c23a"
  danger: "#f56c6c"
  warning: "#e6a23c"
  info: "#409eff"
  link: "#409eff"

typography:
  display-xl:
    fontFamily: "'Aileron', 'Aileron-Bold', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Aileron', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.4px
  display-md:
    fontFamily: "'Aileron', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Aileron', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Aileron', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Aileron', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Aileron', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Aileron', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Aileron', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  price-display:
    fontFamily: "'Aileron', 'Aileron-Bold', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'Aileron', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Aileron', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-sm:
    fontFamily: "'Aileron', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  nav-link:
    fontFamily: "'Aileron', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  tab-label:
    fontFamily: "'Aileron', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
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
    padding: 10px 24px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 24px
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    stickyOnScroll: true
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
    shadow: "0 2px 8px rgba(0,0,0,0.06)"
    imageBackground: "{colors.surface-soft}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 560px
    layout: "50/50 split — copy left, product photography right"
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.xs}"
    ctaTypography: "{typography.button-md}"
  promo-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 36px
    textAlign: center
    dismissible: true
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute top-left over card image"
  sale-badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  spec-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    border: "1px solid {colors.hairline-soft}"
  price-block:
    priceColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    strikethroughColor: "{colors.muted-soft}"
    strikethroughTypography: "{typography.body-sm}"
    discountColor: "{colors.danger}"
    discountTypography: "{typography.body-sm}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    headerTextColor: "{colors.body}"
    headerTypography: "{typography.title-sm}"
    cellTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    highlightBorder: "2px solid {colors.primary}"
    highlightBackground: "{colors.surface-soft}"
    stickyFirstColumn: true
  category-nav:
    backgroundColor: "{colors.surface-page}"
    textColor: "{colors.body}"
    activeColor: "{colors.primary}"
    activeBorder: "2px solid {colors.primary}"
    typography: "{typography.tab-label}"
    padding: "{spacing.base} 0"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    height: 36px
    iconColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.ink-soft}"
    textColor: "{colors.disabled}"
    linkColor: "{colors.muted-soft}"
    headingColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    dividerColor: "{colors.body}"
    padding: "{spacing.xxl} 0"
    columns: 4

## Components

### Buttons

**`button-primary`** — Renders in #00bfd6 with white label text at {typography.button-md} (15px/500). On hover the background darkens to {colors.primary-active} (#00a8bc); disabled state uses the soft teal {colors.primary-disabled}. Corners are {rounded.xs} (4px), height is 40px. This is the single highest-intent action on every product page and in the checkout flow.

**`button-secondary`** — White background with a 1px {colors.primary} border and matching label text. Same corner radius and height as the primary. Used for lower-intent CTAs ("Add to Wishlist", "Compare", "Learn More") where the cyan outline signals affiliation without commanding the same visual weight as the filled button.

**`button-ghost`** — Transparent background, {colors.muted} text, 1px {colors.hairline} border, {typography.button-sm} (13px/500). Appears in filter panels, modal footers, and card secondary actions where further visual separation from primary and secondary is needed.

### Inputs

**`text-input`** — 36px height with {rounded.xs} corners and a 1px {colors.hairline} border that transitions to {colors.primary} on focus, providing a clean cyan focus ring. Placeholder text in {colors.muted-soft}; active text in {colors.body}. Used across search, account management, and checkout fields.

**`search-bar`** — Inherits text-input geometry and focus behavior. A magnifier icon in {colors.muted-soft} sits at the left inset. On the global nav it sits right of the logo; on mobile it collapses to a tappable icon that expands the full input inline.

### Navigation

**`nav-bar`** — 64px white bar with a 1px {colors.hairline-soft} bottom edge. The Huion logo anchors the left; product category links run center at {typography.nav-link}; account icon, cart counter, and language/region selector anchor the right. Mega-menu dropdowns on hover reveal subcategory columns with product thumbnail previews. The bar becomes sticky on scroll and picks up a subtle box shadow.

**`category-nav`** — A secondary horizontal strip below the global nav on listing pages. {colors.surface-page} background, tabs styled with {typography.tab-label}; the active tab carries a 2px {colors.primary} underline rule. On narrow viewports the strip scrolls horizontally with fade masks at both edges signaling overflow.

### Product Cards

**`product-card`** — White card, {rounded.sm} corners, 1px {colors.hairline} border, and a 0 2px 8px ambient shadow. The image zone uses {colors.surface-soft} as a placeholder background and fills the top portion of the card. Below: product name in {typography.title-md}, a row of `spec-tag` chips, a `price-block`, and a `button-primary` or `button-secondary` add-to-cart. A `product-badge` in {colors.primary} overlays the image corner for NEW or BESTSELLER labels; a `sale-badge` in {colors.danger} shows percentage discounts.

### Hero

**`hero-banner`** — Full-bleed section with {colors.ink} background. Product photography (glowing pen display surface, stylus mid-stroke) occupies the right 50–60% of the frame. The left column holds a headline at {typography.display-xl} in {colors.canvas}, a one-line descriptor at {typography.body-md} in semi-transparent white, and a {colors.primary} `button-primary` CTA. Minimum height 560px on desktop; on mobile, the image moves above the text block and the total height collapses.

### Promo Bar

**`promo-bar`** — A 36px full-width strip in {colors.primary} that lives above the nav bar during sales and product launches. Text centered at {typography.body-sm} in {colors.on-primary}. Dismissed via an × icon at the right edge. For informational (non-sale) announcements, background may swap to {colors.ink}.

### Badges

**`product-badge`** — 2px 8px padding, {rounded.xs}, {typography.spec-label} all-caps, in {colors.primary} on white text. Marks "NEW", "BEST SELLER", "PRO", or "BUNDLE" labels. Positioned absolutely over the top-left corner of the card image.

**`sale-badge`** — Identical sizing to `product-badge` but in {colors.danger}. Displays discount magnitude ("−30%"). Usually stacked below or adjacent to `product-badge`.

**`spec-tag`** — Flat ({rounded.none}) chip in {colors.surface-soft} with a 1px {colors.hairline-soft} border. Label text in {typography.spec-label} uppercase at {colors.muted}. Rendered inline in product listings to surface key differentiators: "8192 Levels", "60 RPS", "Android Ready". Wraps to a second line when space runs short.

### Pricing

**`price-block`** — Current price at {typography.price-display} (22px, 700) in {colors.ink}. When a discount is active, the original price appears struck-through at {typography.body-sm} in {colors.muted-soft}, and the savings amount or percentage appears in {colors.danger} at {typography.body-sm}. When no discount applies, only the current price renders with no surrounding markup.

### Comparison

**`comparison-table`** — Horizontal scroll table used on category landing pages. Column headers carry product thumbnail, name at {typography.title-sm}, and price. Spec row labels sit left in {colors.muted} at {typography.body-sm}. The highlighted/recommended column gets a 2px {colors.primary} border on all four sides and a {colors.surface-soft} column background. First column (spec name) is sticky on horizontal scroll.

### Footer

**`footer`** — Dark {colors.ink-soft} background, four-column link grid on desktop. Column headings in {colors.canvas} at {typography.title-sm}; links in {colors.muted-soft} at {typography.body-sm}. Social platform icons in {colors.disabled}. A {colors.body} hairline divides the link grid from the legal and copyright bar at the base. A newsletter signup renders as an inline `text-input` + `button-primary` pair at the top of the footer.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks image above copy; nav collapses to hamburger + full-screen drawer; category-nav becomes horizontal scroll strip; comparison table becomes swipeable card stack |
| Tablet | 744–1128px | 2-column product grid; hero is 50/50 text-image split; primary nav links visible, secondary links in dropdown; mega-menu becomes simplified 2-column |
| Desktop | 1128–1440px | 3–4 column product grid; full mega-menu with thumbnail previews; hero at full 560px height; comparison table shows 4+ columns |
| Wide | > 1440px | Max content width ~1280px centered; hero background stretches edge-to-edge with image right-anchored; product grid stays at 4-up max |

### Touch Targets

- All buttons minimum 40px height per the default component spec
- Nav hamburger, cart, account icons padded to 44×44px tap area
- Quantity stepper +/− buttons: 36px each with {spacing.sm} gap between
- Search trigger icon on mobile padded to 44×44px
- Product image zone on cards is fully tappable as a link (no separate small CTA required on mobile)

### Collapsing Strategy

- Global nav: hamburger at < 744px; mega-menu becomes a full-height left-edge drawer
- Category nav: collapses to a horizontally scrollable tab row with left/right fade edges
- Product grid: 4-up → 3-up → 2-up → 1-up descending across breakpoints
- Hero: left/right 50/50 split → full-bleed with text overlay → stacked image-over-copy on mobile
- Comparison table: full horizontal table → swipeable per-column cards on mobile, first column becomes sticky row header
- Footer: 4-column → 2-column → single-column accordion with collapsed link lists on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `primary-active` (#00a8bc) is derived at −10% lightness from the primary; actual hover/pressed hex not directly extracted and may differ
- Button border-radius confirmed as Element UI's default 4px; exact Huion override not independently verified from live CSS
- No intermediate font-weight tokens (300, 500) explicitly confirmed from extraction; assumed available since Aileron is a full-weight family
- Exact nav bar height (64px) inferred from visual proportion; not extracted
- Hero minimum height (560px) inferred from category page observation; actual campaign hero may vary
- `#ffff00` appears in extracted colors but its system role is unclear — likely campaign image overlay or canvas accent, not a repeatable UI token; excluded from components
- No dark-mode color tokens detected; site appears light-mode-only
- Icon library identified as `element-icons` in font stacks; any custom Huion icon glyphs beyond the Element UI set are not documented
- Mega-menu hover/focus behavior and animation duration not captured
