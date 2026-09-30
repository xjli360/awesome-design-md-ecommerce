---
version: alpha
name: "Lakesidetrader"
source_url: "https://www.lakesidetrader.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The page title announces "German WWII Daggers, Medals and Militaria" without apology or softening — the entire design logic of Lakesidetrader flows from that directness. This is a specialist collector's dealer, not a lifestyle brand, and the visual language reads accordingly: a parchment-toned canvas ({colors.canvas} near #f5f2ec) that evokes archival paper and museum case linings, anchored by a deep military olive primary (#2d4a1e) that recurs in navigation, primary actions, and section dividers. A brass-gold accent (#b8962e) plays the role of the authority marker — it appears on badges, price highlights, and the thin rule lines that separate catalog entries, borrowing from the stamped-metal aesthetic of the artifacts themselves. Typography leans on Georgia-class serifs for display headings, lending provenance and weight appropriate to objects that carry historical significance; body copy drops to a legible system sans-serif to keep condition notes, provenance details, and lot descriptions scannable in dense catalog layouts. Corners are close to square throughout — {rounded.xs} on cards, {rounded.none} on image frames — because the inventory being presented predates rounded-corner design thinking by about eighty years, and softening the interface would signal the wrong era entirely. Product photography sits on near-white surface cards against the warmer parchment ground, giving each object the clean isolation of a catalog plate. The nav bar carries deep charcoal ink on parchment, with the olive primary reserved for the active state underline and primary CTA buttons. Search and filter controls use hairline borders and conservative padding; this is a browsing audience of patient, knowledgeable collectors, not impulse buyers, so density and legibility matter more than motion or surprise. Footer typography shrinks to caption scale with muted ink, holding legal text, contact information, and provenance disclaimers in a manner that reads less like a modern storefront footer and more like the fine print on an auction house catalog back cover.

colors:
  primary: "#2d4a1e"
  primary-active: "#1e3314"
  primary-disabled: "#8fa882"
  ink: "#1a1a1a"
  body: "#2e2e2e"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#c8c2b8"
  hairline-soft: "#e0dbd2"
  canvas: "#f5f2ec"
  surface-soft: "#eee9e0"
  surface-card: "#ffffff"
  on-primary: "#f5f2ec"
  accent-brass: "#b8962e"
  accent-brass-dark: "#8a6e1a"
  accent-brass-muted: "#d4b96a"
  nav-bg: "#1a1a1a"
  nav-text: "#f5f2ec"
  danger: "#8b1a1a"
  badge-sold: "#4a4a4a"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', 'Palatino Linotype', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 17px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-label:
    fontFamily: "system-ui, -apple-system, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.6px
    textTransform: uppercase
  button-md:
    fontFamily: "system-ui, -apple-system, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.4px
  button-sm:
    fontFamily: "system-ui, -apple-system, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "system-ui, -apple-system, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  lot-number:
    fontFamily: "system-ui, -apple-system, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
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
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 42px
    border: none
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
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 21px
    height: 42px
    border: "1.5px solid {colors.primary}"
  button-brass:
    backgroundColor: "{colors.accent-brass}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 42px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    padding: 9px 12px
    height: 40px
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "2px solid {colors.accent-brass}"
    activeIndicator: "2px solid {colors.accent-brass}"
  nav-bar-top-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-label}"
    height: 32px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    padding: "{spacing.md}"
    shadow: "0 1px 4px rgba(0,0,0,0.08)"
  product-card-sold:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    badgeBackground: "{colors.badge-sold}"
    badgeText: "{colors.canvas}"
    badgeTypography: "{typography.caption-label}"
  lot-number-badge:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.lot-number}"
    borderTop: "1px solid {colors.hairline}"
    paddingTop: "{spacing.xs}"
  condition-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    border: "1px solid {colors.hairline}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    accentRule: "3px solid {colors.accent-brass}"
    backgroundBlend: "dark overlay on period photography"
  category-card:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.accent-brass}"
    hoverBorderColor: "{colors.accent-brass-muted}"
    imageOverlay: "rgba(0,0,0,0.45)"
    padding: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    height: 44px
    buttonBackground: "{colors.primary}"
    buttonColor: "{colors.on-primary}"
    buttonTypography: "{typography.button-md}"
  catalog-filter-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.caption-label}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    headingColor: "{colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "›"
    separatorColor: "{colors.hairline}"
  provenance-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.caption-label}"
    labelColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    borderLeft: "3px solid {colors.accent-brass}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  price-tag:
    textColor: "{colors.primary}"
    typography: "{typography.price-display}"
    strikethroughColor: "{colors.muted}"
    strikethroughTypography: "{typography.body-md}"
  footer:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.accent-brass-muted}"
    headingTypography: "{typography.caption-label}"
    headingColor: "{colors.accent-brass}"
    borderTop: "2px solid {colors.accent-brass}"
    padding: "{spacing.xxl} {spacing.xl}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    activeBackground: "{colors.primary}"
    activeText: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 36px

## Components

### Buttons
**`button-primary`** — Olive military green (#2d4a1e) fill on a near-square {rounded.xs} corner, holding 42px height with compact 10px/22px padding. Active state deepens to #1e3314; disabled washes to the muted sage #8fa882 while keeping the same geometry. Used for "Add to Cart," "Inquire," and primary catalog actions.

**`button-secondary`** — White/parchment canvas with a 1.5px olive border and olive text, same height as primary for alignment in paired CTA rows (e.g., "Buy Now" / "Ask a Question"). Hover fills lightly with {colors.surface-soft}.

**`button-brass`** — The accent variant in #b8962e, reserved for featured-sale banners, newsletter subscribe, and "Request Full Catalog" prompts where the brass authority register is appropriate. Same corner and height as primary.

**`button-text`** — Transparent background with underlined olive text, 13px. Used for secondary navigation actions: "View More in Category," "Return to Results," inline provenance source links.

### Inputs & Search
**`text-input`** — White card background, 1px {colors.hairline} border sharpening to 1.5px olive on focus, {rounded.xs} corner, 40px height. Placeholder in {colors.muted-soft}. Used in contact forms, inquiry forms, and the order-search panel.

**`search-bar`** — 44px composite: left is a full-width text input with no left border radius; right is a flush olive button with magnifier icon and {typography.button-md}. The two-part structure echoes a classic catalog index card with a subject tab.

### Navigation
**`nav-bar-top-strip`** — A 32px olive (#2d4a1e) strip running above the main nav, carrying uppercase 11px links to "My Account," "Order Status," and "Contact Us." Sets the authority register before the page begins.

**`nav-bar`** — Charcoal (#1a1a1a) full-width bar, 56px tall, with uppercase 13px nav links spaced generously in {colors.nav-text} parchment. A 2px brass (#b8962e) rule lines the bottom edge — the single decorative element that signals the brand's material world without leaning into kitsch. Active category underlines in brass.

**`breadcrumb`** — Small 12px caption chain in {colors.muted} with › separators, linking back through category > subcategory > item. Sits directly below the nav bar above product pages.

### Product Cards
**`product-card`** — Zero-radius bordered white card with a 4:3 image at top (period-accurate for catalog photography), title in 17px bold Georgia serif, then the lot number badge in uppercase 11px muted text. Price renders in 20px Georgia bold olive. Cards in sold state use the `product-card-sold` variant: surface-soft background, muted text, and a charcoal "SOLD" badge in uppercase 11px.

**`condition-badge`** — Small inline pill in {colors.surface-soft} with 1px hairline border, uppercase 11px text. Values: "Excellent," "Very Good," "Good," "Fair," "Relic." Appears below the title line on every item listing, before the price.

**`lot-number-badge`** — Plain text above the title or below the image, separated by a 1px hairline top border. Carries the internal catalog reference (e.g., "LOT #DG-4412"). No background color — purely typographic.

### Hero & Category
**`hero-banner`** — Full-width band in military olive, with a dark period photograph (parade ground, medals spread, dagger in leather case) layered under a 0.45 opacity scrim. Heading in 32px bold Georgia parchment, with a 3px brass rule between the eyebrow label and the main title. Padding is generous at {spacing.xxl} vertical. Subheading in {typography.body-md} parchment at reduced opacity.

**`category-card`** — Dark charcoal background with a 2px brass border, holding a category label in bold 15px Georgia parchment over a dark image overlay. Grid of 4–6 cards below the hero: "German Daggers," "Medals & Decorations," "Field Equipment," "Documents & Photographs," etc. Hover tightens the brass border to accent-brass-muted.

### Catalog & Detail
**`catalog-filter-panel`** — Left-rail panel on desktop, collapsing to a slide-down drawer on mobile. {colors.canvas} background, 1px hairline border, {rounded.xs}. Filter category headings in uppercase olive {typography.caption-label}; option checkboxes in {typography.body-sm}. Includes price-range inputs using the `text-input` component.

**`provenance-block`** — A surface-soft panel with a 3px left accent rule in brass, holding structured provenance data: "Acquired from," "Original Period," "Maker Marks," "References." Labels in uppercase olive 11px, values in {typography.body-sm}. Used on the detail page below the primary description to surface authentication context.

**`pagination`** — Row of square 36px buttons in {rounded.xs} with hairline borders. Active page fills with primary olive and parchment text. Numeric links in {typography.button-sm}. Used at the bottom of every category listing page.

### Footer
**`footer`** — Full-width charcoal panel with a 2px brass top rule, echoing the nav-bar underline. Four-column layout on desktop: "About Lakeside Trader," "Selling," "Customer Service," "Connect." Column headings in {typography.caption-label} brass; links in {typography.body-sm} {colors.accent-brass-muted}. Legal and copyright text at the very bottom in {colors.muted} 12px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter panel collapses to top drawer triggered by "Filter & Sort" button; nav collapses to hamburger menu revealing full category tree; hero banner cuts to 2-line heading at 24px; breadcrumb hidden to save vertical space |
| Tablet | 744–1128px | 2-column product grid; filter panel remains accessible via slide-out drawer rather than left rail; nav shows top-level categories only with dropdown on tap; hero banner at 28px heading |
| Desktop | 1128–1440px | 3-column product grid with left-rail filter panel (220px fixed); full nav bar with all category links visible; hero at full 32px display-xl |
| Wide | > 1440px | Grid centers in a max-width container (~1400px); product grid expands to 4 columns; hero image area extends full bleed while text container stays constrained |

### Touch Targets
- All primary nav links minimum 44px tap height via padding expansion
- Filter checkboxes padded to 40px tall touch zones on mobile
- "Add to Cart" and "Inquire" buttons full-width on mobile at 48px height
- Pagination buttons expand to 44px on mobile

### Collapsing Strategy
- Filter rail → top accordion drawer on mobile and tablet; opens above the product grid
- Multi-level category nav → hamburger flyout with indented subcategory tree
- Provenance block → collapsed under "Show Provenance" disclosure toggle on mobile
- Product card condition badge and lot number collapse to a single line separated by a centered dot on narrow cards

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site — the palette above is inferred from the militaria dealer category aesthetic and common conventions for collector/antique commerce sites; actual brand colors may differ significantly
- No font stacks were extracted — typography above uses Georgia serif + system sans-serif as a plausible inference; the actual site may use a web font (e.g., a slab serif or a period-inspired typeface) loaded via JS
- Platform is confirmed non-Shopify; the actual CMS or e-commerce platform is unknown, which may affect component structure (faceted search behavior, cart drawer vs. cart page, etc.)
- Meta theme-color is absent, confirming minimal PWA configuration; mobile browser chrome color is unknown
- No extracted spacing, border-radius, or shadow tokens — all values above are inferred from the catalog/heritage-dealer archetype
- Sold/available state visual treatment is inferred; actual implementation may use overlays, ribbons, or strikethrough price differently
- No data on actual category taxonomy depth or the number of top-level nav items, which would materially affect mobile nav design decisions
