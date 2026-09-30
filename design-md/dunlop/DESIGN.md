---
version: alpha
name: "Dunlop"
source_url: "https://www.jimdunlop.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-voltage red (#ef0000) rips through an otherwise industrial gray-and-white grid — the same red that has marked Dunlop’s guitar picks, straps, and effects pedals since 1965. The brand’s digital presence mirrors its physical product: functional, direct, and built for musicians who need gear that works without fanfare. Franklin Gothic, a mid-century workhorse typeface, carries the weight in three distinct cuts — Book for body text, Condensed for tight navigation labels, and Demi for product titles — creating a typographic system that feels engineered rather than styled. The palette leans heavily on neutral grays (#757575, #e5e5e5, #f5f5f5) and crisp white canvas, with red deployed surgically: primary CTAs, price highlights, and the signature Dunlop logo mark. A secondary blue (#002fe1) appears in select product badges and category headers, adding a cool counterpoint to the dominant warmth. Corners are mostly sharp ({rounded.none}) on product cards and navigation, with soft rounding ({rounded.sm}) reserved for buttons and input fields — a subtle nod to the tactile edges of actual guitar hardware. The overall impression is that of a workshop manual: information-dense, hierarchically clear, and utterly indifferent to decorative flourish.

colors:
  primary: "#ef0000"
  primary-active: "#cc0000"
  primary-disabled: "#ffdddd"
  ink: "#222222"
  body: "#444444"
  muted: "#757575"
  muted-soft: "#8d8d8d"
  hairline: "#dfdfdf"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#002fe1"
  accent-blue-soft: "#476bef"
  accent-gold: "#f1a500"
  accent-green: "#008a06"
  badge-red: "#cc4749"
  badge-blue: "#007dc6"
  badge-gold: "#f1a500"
  logo-red: "#ef0000"
  logo-blue: "#002fe1"

typography:
  display-xl:
    fontFamily: "'FranklinGothicDemi', 'Franklin Gothic Demi', arial, helvetica, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'FranklinGothicDemi', 'Franklin Gothic Demi', arial, helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'FranklinGothicDemi', 'Franklin Gothic Demi', arial, helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'FranklinGothicCondensed', 'Franklin Gothic Condensed', arial, helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "'FranklinGothicCondensed', 'Franklin Gothic Condensed', arial, helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  body-lg:
    fontFamily: "'FranklinGothicBook', 'Franklin Gothic Book', arial, helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-md:
    fontFamily: "'FranklinGothicBook', 'Franklin Gothic Book', arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'FranklinGothicBook', 'Franklin Gothic Book', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'FranklinGothicBook', 'Franklin Gothic Book', arial, helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  caption-sm:
    fontFamily: "'FranklinGothicBook', 'Franklin Gothic Book', arial, helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'FranklinGothicCondensed', 'Franklin Gothic Condensed', arial, helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'FranklinGothicDemi', 'Franklin Gothic Demi', arial, helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'FranklinGothicDemi', 'Franklin Gothic Demi', arial, helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
    textTransform: uppercase
  link:
    fontFamily: "'FranklinGothicBook', 'Franklin Gothic Book', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'FranklinGothicCondensed', 'Franklin Gothic Condensed', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  product-title:
    fontFamily: "'FranklinGothicDemi', 'Franklin Gothic Demi', arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  product-price:
    fontFamily: "'FranklinGothicDemi', 'Franklin Gothic Demi', arial, helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
    color: "{colors.primary}"

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
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
    padding: 12px 28px
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
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    border-bottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.product-title}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.product-price}"
    color: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    border-bottom: "1px solid {colors.hairline-soft}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    border-bottom: "2px solid {colors.primary}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    color: "{colors.canvas}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.primary}"
  badge-new:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
    border-bottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} 0"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.muted-soft}"
    padding: "0 {spacing.xs}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  pagination-button-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand’s signature red (#ef0000) with white text in Franklin Gothic Demi uppercase. On hover, the background deepens to `{colors.primary-active}` (#cc0000). The disabled state uses a pale pink `{colors.primary-disabled}` (#ffdddd) with muted text, signaling the action is unavailable without visual noise. All primary buttons use `{rounded.sm}` (4px) — a subtle softening of the otherwise sharp brand language.

**`button-secondary`** — An outlined variant with a white background, dark text, and a 2px hairline border. The active state swaps the border to `{colors.ink}` and adds a light gray background. Used for “Add to Wishlist,” “View Details,” and secondary form actions. The uppercase Demi typeface maintains brand consistency while the lighter visual weight distinguishes it from primary actions.

**`button-tertiary`** — A text-only button with no background or border, using the primary red for its text color. Used for “Learn More” links within product descriptions and “Clear Filters” in the sidebar. The lack of container allows it to sit inline with body copy without disrupting the reading flow.

**`button-pill`** — A fully rounded variant (`{rounded.full}`) reserved for promotional badges, “Shop Now” calls in hero banners, and mobile filter toggles. Smaller in height (36px) than standard buttons, it uses the smaller button typography token and appears in both red and blue (`{colors.accent-blue}`) variants for category-specific promotions.

### Cards
**`product-card`** — The primary content container for the product grid, using a white background with a soft hairline border (`{colors.hairline-soft}`) and no border-radius — a deliberate design choice that echoes the utilitarian aesthetic of guitar hardware. On hover, the border darkens to `{colors.hairline}` and a subtle box shadow lifts the card. The image area occupies the top 60% with a `{colors.surface-soft}` background for product photography. Below, the title sits in `{typography.product-title}` (Franklin Gothic Demi, 16px) and the price in `{typography.product-price}` (same face, 18px, rendered in `{colors.primary}`). A small badge (`{colors.accent-blue}` or `{colors.accent-gold}`) may appear in the top-left corner for “NEW” or “LIMITED EDITION” flags.

### Navigation
**`nav-bar`** — A fixed-height (72px) white bar with a single hairline bottom border. Navigation links use Franklin Gothic Condensed in uppercase with 0.8px letter spacing — a compressed, industrial feel that maximizes information density. The active link is underlined by `{colors.primary}`; inactive links render in `{colors.muted}`. On scroll, the bar collapses to 56px (`nav-bar-sticky`) with the same styling, preserving the brand’s compact typographic rhythm.

**`category-strip`** — A secondary navigation row below the main nav, listing product categories (Picks, Straps, Pedals, Accessories) as horizontally scrollable tabs. Active tabs receive a 2px bottom border in `{colors.primary}` and the primary red text color; inactive tabs use `{colors.muted}`. The strip itself has a `{colors.hairline-soft}` bottom border and sits flush with the content below.

### Forms
**`text-input`** — Standard single-line input with a white background, 1px hairline border, and 4px rounding. On focus, the border thickens to 2px and switches to `{colors.primary}`. The error state uses the same 2px primary red border, paired with an error message in `{colors.primary}` below the field. Height is 44px with 10px/14px padding for comfortable touch targeting.

**`select-input`** — Matches the text-input styling exactly, with a custom dropdown arrow in `{colors.muted}`. Used for product filters (size, color, category) and checkout forms. The open state shows a subtle `{colors.hairline}` border and a rotated arrow indicator.

**`quantity-selector`** — A compact input group with decrement/increment buttons flanking a centered numeric value. Uses the same border and rounding as text inputs but with tighter padding (6px/12px) and a 40px height. The buttons use `{colors.muted}` text on hover to indicate interactivity.

### Footer
**`footer`** — A dark section (`{colors.ink}` background) with white text, organized into four columns: Customer Service, About Dunlop, Resources, and Newsletter Signup. Links render in white with `{colors.primary}` hover states. The newsletter input matches the standard text-input but with a white border on the dark background. The bottom bar includes copyright text in `{colors.muted}` and social media icons in white. Section padding uses `{spacing.section}` (64px) vertically and `{spacing.xl}` (32px) horizontally.

### Badges
**`badge-new`** — A gold (`{colors.accent-gold}`) background with dark text, used for newly released products. The condensed uppercase type at 11px fits within a tight 2px/8px padding. **`badge-sale`** uses the primary red background with white text. **`badge-limited`** uses the accent blue (`{colors.accent-blue}`) for limited edition or exclusive items. All badges share the same typography and 4px rounding.

### Hero
**`hero-banner`** — A full-width section with a `{colors.surface-soft}` background, large display typography (`{typography.display-xl}`), and a single primary CTA button. The banner may include a background image (product photography or lifestyle shot) with a subtle overlay. The CTA button uses the standard primary styling but with larger padding (14px/32px) and 48px height for visual prominence. Content is centered with `{spacing.section}` vertical padding.

### Accordion
**`accordion-header`** — Used in product descriptions, FAQs, and filter panels. The header uses `{typography.title-md}` (Franklin Gothic Condensed uppercase) with a `{colors.hairline-soft}` bottom border. On click, the header toggles the content visibility and rotates a chevron icon. The content area uses `{typography.body-md}` with `{spacing.base}` padding on all sides.

### Breadcrumbs
**`breadcrumb`** — A simple horizontal list of links separated by a `{colors.muted-soft}` slash or chevron. Active (current page) links use `{colors.ink}`; parent links use `{colors.muted}`. The typography is `{typography.caption}` (13px Franklin Gothic Book) for a subtle, non-intrusive navigation aid.

### Pagination
**`pagination-button`** — Used on category and search results pages. Each page button is 36px tall with 8px/12px padding, a 1px hairline border, and 4px rounding. The active page uses `{colors.primary}` background with white text; disabled buttons (previous/next when at boundary) use `{colors.surface-soft}` background with `{colors.muted-soft}` text.

### Tooltips
**`tooltip`** — A dark (`{colors.ink}`) background with white text, appearing on hover over icons, truncated text, and form labels. The tooltip uses `{typography.caption}` (13px) with 4px/8px padding and 4px rounding. A small arrow points to the trigger element.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item), hamburger nav replaces full category strip, hero banner reduces to 48px vertical padding, footer collapses to single column, search bar moves to top of nav, product card badges stack vertically |
| Tablet | 744–1128px | Two-column product grid (2 items), category strip becomes horizontally scrollable, nav bar retains full links but reduces font size to 12px, hero banner uses 56px vertical padding, footer shows two columns |
| Desktop | 1128–1440px | Three-column product grid (3 items), full nav bar with all links visible, category strip shows 6-8 tabs, hero banner at full 64px padding, footer shows four columns |
| Wide | > 1440px | Four-column product grid (4 items), max-width container at 1440px centered, nav bar and category strip remain at full width with increased horizontal padding, hero banner may include full-bleed background image |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets (title, price, image) are at least 48px tall
- Mobile nav hamburger icon is 48x48px with 12px internal padding
- Quantity selector buttons are 40x40px with clear visual feedback
- Pagination buttons are 36x36px — acceptable for desktop but should be 44x44px on mobile

### Collapsing Strategy
- Main navigation collapses to a hamburger menu at < 744px, with a slide-out drawer containing all links and category items
- Category strip collapses to a single “Categories” dropdown on mobile, with horizontal scroll on tablet
- Product filters collapse to a “Filter” button that opens a modal overlay on mobile, remaining as a persistent sidebar on desktop
- Footer columns stack to single column on mobile, two columns on tablet, four on desktop
- Hero banner reduces vertical padding by 25% on mobile to conserve screen space
- Product card badges stack vertically on mobile to avoid horizontal overflow

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for product cards, navigation links, and buttons were inferred from common e-commerce patterns; the exact box-shadow values, transition durations, and color shifts could not be extracted from the live site.
- **Error styling** for form validation (error messages, border colors, iconography) is assumed based on the primary red; the actual error palette and message placement were not observed.
- **Dark mode** is not present on the live site; no dark theme tokens have been defined.
- **Sub-brand palettes** (MXR, Way Huge, Rockman) may use distinct color systems that were not captured in the extraction. The `{colors.accent-blue}` and `{colors.accent-gold}` tokens are placeholders for these potential variations.
- **Typography scale** (font sizes, line heights, letter spacing) was estimated from observed Franklin Gothic usage and common e-commerce hierarchies; exact values may differ from the site’s CSS.
- **Spacing scale** follows a standard 4px/8px/16px/24px/32px/48px/64px progression; the actual site may use non-linear spacing values.
- **Animation and transition** specifications (duration, easing, motion triggers) were not extracted; a standard 200ms ease-in-out is assumed for all interactive states.
- **Iconography** (search, cart, hamburger, social media) was not analyzed; the system assumes a consistent 24x24px icon set with `{colors.muted}` default and `{colors.primary}` hover states.
- **Checkout flow** (cart, payment, confirmation) was not accessible; the extracted color list includes potential Shopify Pay and Klarna colors that were filtered out. The actual checkout design may deviate from the main site’s system.
- **Accessibility** (focus rings, contrast ratios, screen reader labels) was not verified; the system assumes standard 2px `{colors.primary}` focus outlines on all interactive elements.
