---
version: alpha
name: "Tarinika"
source_url: "https://www.tarinika.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep teal (#108474) — the color of polished malachite and Indian meenakari enamel — anchors Tarinika's entire action system; every primary button, hover state, and navigational accent draws from this single brand voltage while the surrounding palette stays conspicuously restrained. Against a near-white canvas (#fafafa), the contrast is sharp but never harsh, lending the site the feel of a well-lit showroom rather than a marketplace aggregator. Canela, the contemporary display serif, carries the editorial weight of product naming and category headers — its slightly bracketed terminals evoke hand-lettered heritage jewelry catalogs without performing nostalgia — while Barlow handles everything below: nav links, product metadata, body copy, and form labels all render in this clean geometric sans, keeping UI surfaces readable without competing with jewelry photography. The palette beyond the primary teal reads deliberately spare: near-black ink (#0e0808) for primary text, a descending grayscale from #363636 through #7a7a7a and #d3d3d3 to off-white surfaces (#f2f2f2, #fafafa), with lighter teal extractions (#aadddd, #47c1bf) reserved for badge fills, hover halos, and occasion chips. That restraint places the color burden squarely on gold-toned and gemstone photography — a discipline common to high-quality jewelry e-commerce. No radius decision veers aggressive: category pill filters round to {rounded.full}, CTAs take a modest {rounded.xs}, and product card images land on a barely-there corner that reads contemporary without feeling commoditized. Spacing is generous through the browse experience — product grids breathe at {spacing.xxl} gutters on desktop, and the hero runs full-bleed imagery with centered Canela text overlay, placing jewelry against editorial photography rather than catalog white. The Indian cultural context surfaces through category architecture (temple jewelry, jhumkas, mangalsutras, and necklace sets as distinct navigation nodes), occasion-tagging vocabulary (Wedding, Festive, Daily Wear), and set-indicator chips that surface multi-piece product relationships directly on the tile, keeping complex Indian bridal jewelry sets legible in a grid context.

colors:
  primary: "#108474"
  primary-active: "#0a6159"
  primary-disabled: "#aadddd"
  primary-light: "#47c1bf"
  primary-subtle: "#aadddd"
  teal-mid: "#49abb5"
  teal-light: "#aadddd"
  ink: "#0e0808"
  body: "#363636"
  muted: "#7a7a7a"
  hairline: "#d3d3d3"
  hairline-soft: "#e1e1e1"
  canvas: "#fafafa"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-red: "#e50122"
  scrim: "#100f0f"

typography:
  display-xl:
    fontFamily: "'Canela', 'Apple Garamond', Baskerville, Georgia, serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Canela', 'Apple Garamond', Baskerville, Georgia, serif"
    fontSize: 38px
    fontWeight: 300
    lineHeight: 1.18
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Canela', 'Apple Garamond', Baskerville, Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Barlow', Avenir, 'Avenir Next', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'Barlow', Avenir, 'Avenir Next', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  body-md:
    fontFamily: "'Barlow', Avenir, 'Avenir Next', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', Avenir, 'Avenir Next', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', Avenir, 'Avenir Next', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Barlow', Avenir, 'Avenir Next', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow', Avenir, 'Avenir Next', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Barlow', Avenir, 'Avenir Next', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
  price-display:
    fontFamily: "'Barlow', Avenir, 'Avenir Next', Arial, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Barlow', Avenir, 'Avenir Next', Arial, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Barlow', Avenir, 'Avenir Next', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  category-label:
    fontFamily: "'Barlow', Avenir, 'Avenir Next', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.5px
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
    padding: 14px 28px
    height: 48px
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
    border: "1px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline-soft}"
    height: 64px
    logoMaxHeight: 40px
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    shadow: "0 4px 16px rgba(0,0,0,0.08)"
    itemPadding: "10px 16px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageRounded: "{rounded.xs}"
    cardRounded: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.md}"
    hoverShadow: "0 4px 20px rgba(0,0,0,0.07)"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  price-original:
    textColor: "{colors.muted}"
    typography: "{typography.price-display}"
    textDecoration: line-through
  price-discounted:
    textColor: "{colors.sale-red}"
    typography: "{typography.price-sale}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.category-label}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  hero-section:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.canvas}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    overlayOpacity: 0.38
    contentMaxWidth: 640px
    textAlign: center
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0"
    textAlign: center
  occasion-badge:
    backgroundColor: "{colors.primary-subtle}"
    textColor: "{colors.primary-active}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  set-indicator:
    backgroundColor: "{colors.teal-light}"
    textColor: "{colors.primary-active}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  wishlist-button:
    backgroundColor: transparent
    iconColor: "{colors.muted}"
    iconColorActive: "{colors.sale-red}"
    rounded: "{rounded.full}"
    size: 36px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.hairline}"
    linkColor: "{colors.teal-light}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"

## Components

### Buttons
**`button-primary`** — Renders in deep teal (#108474) with white Barlow 600 uppercase text tracked at 1px, giving it a formal register appropriate for a heritage jewelry purchase. At 48px height and {rounded.xs} corners it reads as confident without the rounded softness common in Western fashion e-commerce. Active and hover states shift background to #0a6159, staying within the teal family. Disabled states use the lightest extracted teal (#aadddd) so even inactive surfaces remain on-palette.

**`button-secondary`** — A 1px teal-bordered outline button with matching teal text; no background fill. It pairs on PDP layouts beside `button-primary` (Add to Cart + Wishlist, or Add to Cart + View Full Set). The shared teal color ties both buttons visually without creating hierarchy confusion.

**`button-ghost`** — Hairline-bordered (#d3d3d3), ink-colored text; used for filter resets, "load more" pagination triggers, and low-emphasis navigation controls. Removes itself from the brand-color conversation entirely.

### Text Input
**`text-input`** — Near-white (#fafafa) background, hairline (#d3d3d3) resting border, teal (#108474) focus ring. Barlow body-md keeps form copy consistent with product copy. Applied across newsletter signup, coupon fields, and address forms.

### Navigation
**`nav-bar`** — Near-white (#fafafa) background with a very soft hairline-soft bottom border. At 64px height, photography directly beneath has room to breathe. Top-level category labels (Necklaces, Earrings, Bangles, Jewellery Sets, etc.) render in 13px Barlow 500 tracked at 0.5px. On hover, items may receive a teal underline accent rather than a background fill, keeping the bar light.

**`nav-dropdown`** — White (#ffffff) panel with a soft shadow and 1px hairline-soft border. Category items at nav-link scale with 10px vertical padding. Sub-groupings (e.g. Temple Jewelry under Necklaces, Jhumkas under Earrings) appear as labeled column clusters.

### Product Card
**`product-card`** — Square or slightly portrait image with {rounded.xs} corners. Below: product name in title-sm Barlow 600, price in price-display. When discounted, the original price renders struck-through in muted (#7a7a7a) and the sale price appears in red (#e50122). A `set-indicator` badge overlays the image bottom-left when the item is part of a multi-piece set. The wishlist icon sits top-right of the image and becomes visible on hover/focus. No drop shadow at rest; a gentle shadow lifts the card on hover.

**`product-badge`** and **`product-badge-sale`** — Teal and red corner chips respectively, both at 11px Barlow 700 uppercase. `product-badge` flags editorial status (New, Bestseller, Limited); `product-badge-sale` flags promotional discounts. Both overlay the top-left of product images.

### Hero
**`hero-section`** — Full-bleed editorial photography with a 38% dark scrim (near-black #100f0f). Heading in display-xl Canela Light centered; a short subhead in body-md Barlow below; `button-primary` CTA centered beneath that. The Canela weight at 300 keeps text from feeling heavy atop jewelry photography — the type illuminates rather than competes.

### Collection Header
**`collection-header`** — A soft-gray (#f2f2f2) full-width band with the collection name in display-md Canela centered and a short descriptor in caption Barlow below. Gives each category page a distinct editorial landing quality rather than dropping directly into the product grid.

### Occasion Badge
**`occasion-badge`** — Pill-shaped ({rounded.full}) chip in light teal (#aadddd) fill with dark teal (#0a6159) text. Labels such as "Wedding", "Festive", "Daily Wear", and "Office Wear" appear on product tiles and at the top of collection pages as a secondary browse axis alongside category navigation.

### Set Indicator
**`set-indicator`** — Small inline tag with light-teal fill (#aadddd) and dark-teal text, using {rounded.xs} corners. Surfaces "Necklace Set", "Earring Pair", "Bangles Set of N" annotations directly on the product tile so customers understand multi-piece composition before clicking through — critical for the complex bridal and festival set assortments that anchor the catalog.

### Search
**`search-bar`** — Pill-shaped ({rounded.full}) input with soft gray fill (#f2f2f2) and no visible resting border. A search glyph sits left-aligned in muted (#7a7a7a). Focus state adds a teal (#108474) ring. Appears in the nav header on desktop and as a full-width bar in the mobile drawer.

### Announcement Bar
**`announcement-bar`** — Full-width teal (#108474) band above the nav bar, white caption-scale Barlow announcing free-shipping thresholds, sale events, or discount codes. 36px height keeps it compact; center-aligned text maximizes legibility at a glance.

### Footer
**`footer`** — Near-black (#0e0808) background with hairline-tone body text (#d3d3d3) and light-teal link accents (#aadddd) on hover. Section headings in title-sm Barlow 600 uppercase. Multi-column layout on desktop covers: Shop categories, Customer Service, About, payment trust badges, social icons, and a newsletter field using the standard `text-input` on a dark surface.

### Breadcrumb
**`breadcrumb`** — Caption-scale Barlow in muted (#7a7a7a) with "/" separators; the active (current page) node renders in ink (#0e0808). Appears on collection pages and PDP, aiding navigation within the deep category hierarchy — temple jewelry, meenakari, kundan, polki, and gold-plated each branch separately.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer with full-width slide-in panel; hero heading drops to display-lg Canela; announcement bar wraps to two lines if needed; search expands to full-width bar |
| Tablet | 744–1128px | 2-column product grid; abbreviated nav labels with overflow into drawer; hero text overlay at ~60% width; collection header padding reduces to {spacing.xl} |
| Desktop | 1128–1440px | 3–4 column product grid; full mega-menu nav with dropdown columns; hero full-bleed with centered overlay at max-width 640px |
| Wide | > 1440px | Content max-width caps around 1400px and centers; hero image scales but text block holds 640px; product grid may expand to 5 columns for accessories |

### Touch Targets
- All nav items minimum 44×44px tappable area
- Category pill filters padded to at least 44px height on mobile
- Wishlist icon on product card expands tap zone to a 44px invisible circle around the 36px visible target
- Primary and secondary CTA buttons stretch to full-width on mobile below 375px
- Set-indicator and occasion-badge chips maintain 32px minimum height with horizontal padding for tap comfort

### Collapsing Strategy
- Desktop mega-menu collapses to a hamburger icon at tablet breakpoint; the drawer slides in from the left with full category tree
- Dropdown sub-category columns stack vertically inside the mobile drawer with 44px accordion rows
- Filter panel (faceted refinement by occasion, metal, stone) shifts from a sidebar on desktop to a bottom-sheet modal on mobile
- Product image secondary-hover behavior converts to a swipeable carousel on touch devices
- Footer columns collapse from 4 to 2 at tablet and to 1 at mobile; newsletter signup stacks below category links

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- primary-active (#0a6159) is manually darkened from the extracted primary (#108474) — not directly present in the extraction
- Canela and Barlow are inferred from the font-family stack strings; actual weights loaded (Canela Light 300 vs Regular 400 vs Medium 500) cannot be confirmed without a full CSS parse or font-loading trace
- Gold and metallic accent colors are absent from the extraction despite Indian jewelry UI commonly featuring gold-tone icon fills, swatch borders, and rating stars — likely loaded via JS or absent from static HTML
- Precise product grid gutter values and internal card spacing could not be confirmed from static extraction
- Whether a custom Canela license is in use or the site falls back to Apple Garamond / Baskerville system stacks is unconfirmed
- Social icon colors (#1da1f1 Twitter, #4266b2 Facebook, #f14336 Google) are present in extraction and explicitly excluded from the brand palette
- No confirmed hover/focus transition durations or easing curves extracted
- Dark mode support, if any, is not determinable from the extraction data
