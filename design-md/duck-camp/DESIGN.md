---
version: alpha
name: "Duck Camp"
source_url: "https://duckcamp.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A hunting and fishing brand that wraps its outdoor ethos in a marsh-green (#108474) and duck-boat orange (#ef5023) palette, with a secondary sage (#aaccaa) and a warm tan (#9c8d5f) that read like a well-worn canvas jacket. The brand uses P22 Mackinac Pro for display — a serif with a slight traditionalist tilt — and Baton Turbo for body, creating a tension between old-world hunting-lodge typography and modern e-commerce utility. The site's canvas is a soft off-white (#f9fafb) rather than pure white, and the hairline (#e5e6e9) is barely there, letting product photography and the orange CTAs do the heavy lifting. Duck Camp's primary button is a full-bleed orange (#ef5023) pill with white text, and the secondary button inverts to a white pill with a green (#108474) outline — a two-button system that feels like a choice between "go hunting" and "stay at camp." The navigation bar sits at 80px with a transparent background that picks up the page's canvas color, and the logo is a wordmark in P22 Mackinac Pro, often accompanied by a small duck silhouette. The brand's voice is direct, masculine, and unpretentious — it's the kind of site where the "Shop by Species" dropdown sits next to "New Arrivals," and the footer is a dense grid of links in {colors.muted} (#7b7b7b) with a thick green (#108474) top border. The product cards use a soft {rounded.sm} (8px) and a clean white surface, with the price in {typography.title-md} and the product name in {typography.body-sm}. The brand also uses a mustard yellow (#fbcd0a) sparingly — likely for sale badges or limited-edition callouts — and a slate gray (#3a3a3a) for body text that's softer than pure black. The overall feel is a campfire-lit e-commerce experience: warm, grounded, and built for the person who owns more than one pair of waders.

colors:
  primary: "#ef5023"
  primary-active: "#d9441e"
  primary-disabled: "#f5a68a"
  ink: "#3a3a3a"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#9c8d5f"
  hairline: "#e5e6e9"
  hairline-soft: "#eeeeee"
  canvas: "#f9fafb"
  surface-soft: "#f2ede5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#108474"
  accent-green-light: "#c1e6e6"
  accent-sage: "#aaccaa"
  accent-mustard: "#fbcd0a"
  accent-tan: "#9c8d5f"
  accent-orange-light: "#e97f46"
  accent-lavender: "#a89cc8"
  accent-olive: "#41470e"
  accent-teal: "#6ca1a9"

typography:
  display-xl:
    fontFamily: "'P22 Mackinac Pro', 'Baskerville', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'P22 Mackinac Pro', 'Baskerville', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'P22 Mackinac Pro', 'Baskerville', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'P22 Mackinac Pro', 'Baskerville', Georgia, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Baton Turbo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Baton Turbo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Baton Turbo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Baton Turbo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Baton Turbo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Baton Turbo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Baton Turbo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Baton Turbo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Baton Turbo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Baton Turbo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Baton Turbo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  nav-link-mobile:
    fontFamily: "'Baton Turbo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-green}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.accent-green}"
  button-secondary-active:
    backgroundColor: "{colors.accent-green-light}"
    textColor: "{colors.accent-green}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.accent-green}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-orange:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.accent-green}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
    border: "1px solid {colors.accent-green}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.accent-green}"
  text-input-error:
    border: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.accent-green}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
  top-nav-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.accent-green}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  mobile-nav-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link-mobile}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.sm} 0 {spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "0 {spacing.sm} {spacing.sm} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.accent-mustard}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-section-overlay:
    backgroundColor: "rgba(0,0,0,0.3)"
    textColor: "{colors.on-primary}"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
  category-tile-active:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "4px solid {colors.accent-green}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.accent-green}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  dropdown-menu:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  dropdown-item:
    padding: "{spacing.sm} {spacing.base}"
  dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 52px
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
    padding: "0 {spacing.xs}"
  pagination-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  pagination-button-active:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
  pagination-button-disabled:
    textColor: "{colors.muted-soft}"
  loading-spinner:
    color: "{colors.accent-green}"
    size: 24px
  rating-stars:
    color: "{colors.accent-mustard}"
    size: 16px
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  review-card-author:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  review-card-date:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a full-pill orange (#ef5023) button with white text in Baton Turbo 16px/600. Hover state darkens to #d9441e (`{colors.primary-active}`). Disabled state fades to a pale orange (#f5a68a). Used for "Add to Cart," "Shop Now," and primary checkout actions. The pill shape (`{rounded.full}`) is consistent across all button variants, reinforcing the brand's campfire-friendly, approachable tone.

**`button-secondary`** — An outlined pill with a 2px green (#108474) border on a white background. Hover fills the background with a pale green (#c1e6e6). Used for "Learn More," "View Details," and secondary actions that sit alongside the primary orange button. The green outline creates a clear visual hierarchy without competing with the orange primary.

**`button-tertiary-text`** — A text-only button with no background or border, using the ink (#3a3a3a) color. Used for "Cancel," "Skip," and other low-emphasis actions. Hover state adds an underline.

**`button-pill-orange`** — A smaller, compact version of the primary pill, used for inline actions like "Shop by Species" filters or quick-add buttons on product cards. Same orange fill, white text, but 14px font and tighter padding.

**`button-pill-green`** — A green (#108474) filled pill used for "Subscribe," "Save," or eco-friendly callouts. Same compact sizing as the orange pill variant.

**`button-pill-outline`** — A thin 1px green outline pill with transparent background, used for "Filter" or "Sort" buttons in category navigation. Hover fills with the green.

### Cards
**`product-card`** — A white card with soft 8px corners (`{rounded.sm}`) containing a product image, title in `{typography.title-sm}`, and price in `{typography.body-md}`. The image has rounded top corners only, creating a clean separation between photo and text. Badges (sale, new, limited) sit in the top-left corner of the image area in mustard yellow, orange, or green.

**`review-card`** — A white card with 8px corners containing the review text, author name in caption, date in caption-sm, and a star rating in mustard yellow (#fbcd0a). Padding is 16px on all sides.

### Navigation
**`top-nav`** — An 80px transparent navigation bar that picks up the page's canvas color. On scroll, it gains a subtle box shadow. Logo (P22 Mackinac Pro wordmark, often with a duck silhouette) sits left, nav links center, and utility icons (search, account, cart) right. Active nav link has a 2px green bottom border.

**`mobile-nav-panel`** — A full-screen slide-in panel from the left, with nav links in 18px/600 Baton Turbo. Background is white, and a close button sits in the top-right corner.

**`dropdown-menu`** — A white dropdown with 8px corners and a subtle shadow, used for "Shop by Species" and "Shop by Category" sub-navigation. Items have 8px/16px padding, and hover state uses the soft tan background (#f2ede5).

### Forms
**`text-input`** — A standard input field with 8px corners, 12px/16px padding, and a light gray border (#e5e6e9). Focus state switches to a green (#108474) border. Error state uses the orange (#ef5023) border.

**`search-bar`** — A full-pill search input with 12px/20px padding and a light gray border. Focus state switches to green border. Used in the top nav and on search result pages.

**`newsletter-input`** — A pill-shaped email input used in the footer, paired with a green submit button. The input has 12px/20px padding and a light gray border.

### Footer
**`footer`** — A dense grid of links in muted gray (#7b7b7b) with a thick 4px green (#108474) top border. Headings are in `{typography.title-sm}` in ink (#3a3a3a). Links hover to green. The newsletter signup sits in the footer, with a pill input and green submit button. Social media icons (likely in the extracted lavender #a89cc8) sit at the bottom.

### Badges
**`product-card-badge`** — A small mustard yellow (#fbcd0a) badge with uppercase 11px/700 text, used for "Limited Edition" or "Staff Pick." Corners are 4px.

**`product-card-badge-sale`** — An orange (#ef5023) badge for sale items, same sizing.

**`product-card-badge-new`** — A green (#108474) badge for new arrivals, same sizing.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns), hamburger menu replaces top nav, hero section collapses to stacked layout, footer links collapse into accordions, search bar moves to mobile panel |
| Tablet | 744–1128px | Two-column product grid, top nav remains but some links hide behind a "More" dropdown, hero section uses 50/50 split, footer remains grid but with fewer columns |
| Desktop | 1128–1440px | Three-column product grid, full top nav visible, hero section uses 60/40 split with large display typography, footer grid with 4-5 columns |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centers content, hero section uses full-width imagery with overlay text |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px
- Mobile nav links are 48px tall for easy tapping
- Quantity selector buttons are 40x40px
- Pagination buttons are 40x40px
- Dropdown items have 44px minimum height

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Footer link groups collapse to accordions below 744px
- Product filters collapse to a slide-out drawer on mobile
- Hero section text and image stack vertically below 744px
- Multi-column product grids reduce columns as viewport shrinks (4 → 3 → 2 → 1)
- Search bar collapses to an icon that opens a full-screen overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for tertiary text buttons (underline vs. color change) not confirmed from extraction
- Error state styling for forms (error messages, icon placement) not extracted
- Sub-brand or collection-specific palette variations (e.g., "Duck Camp x [Partner]") not captured
- Dark mode or high-contrast mode styles not present on the live site
- Animation and transition durations (ease-in-out, spring, etc.) not extracted
- Focus ring styling (outline color, width, offset) for keyboard accessibility not confirmed
- Loading states for product grids and search results (skeleton screens vs. spinners) not extracted
- Empty states for cart, wishlist, and search results not captured
- Modal and overlay styling (background scrim opacity, close button placement) not confirmed
- Tooltip and popover styling not extracted
- The extracted font list includes "JudgemeIcons" and "JudgemeStar" which are third-party review widget fonts, not brand typography
- The extracted color list includes many grays and near-whites that may be framework defaults or checkout widget colors; the brand's true primary is the distinctive orange (#ef5023) and green (#108474) pairing
