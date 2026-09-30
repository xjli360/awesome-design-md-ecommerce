---
version: alpha
name: "Verso Books"
source_url: "https://www.versobooks.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A radical leftist publisher that uses a near-black ink (#121212) on a warm off-white canvas (#dedede) as its primary visual argument — not as a minimalist affectation but as a political and economic one, signaling that the book is the object, not the interface. The site runs Aktiv Grotesk in three weights (thin, regular, arabic) at modest sizes, with no hero carousel, no full-bleed photography, and no decorative illustration; the cover image of each book carries all the emotional weight. Navigation is a single horizontal strip of categories (Theory, History, Fiction, etc.) in 14px regular weight, with no dropdowns, no mega-menus, and no search bar visible until you click the magnifying-glass icon. The product grid uses a tight 2-column layout on desktop with 12px gaps (`{spacing.md}`) and no rounded corners on cards (`{rounded.none}`) — the only radius in the system is the 4px (`{rounded.xs}`) on the newsletter signup button and the 8px (`{rounded.sm}`) on the search input. This is a bookstore built for people who already know what they want: the interface gets out of the way, the typography is utilitarian, and the only color outside the black/white/gray spectrum is the occasional red sale badge or the yellow "New" flag on recently published titles. The footer is a dense column of links in 12px caption weight, with no social-media icons — just text links to Twitter, Instagram, and the Verso blog. The entire experience reads as a warehouse with good lighting: functional, serious, and indifferent to persuasion.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#666666"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#dedede"
  surface-soft: "#d0d0d0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-badge: "#cc0000"
  new-badge: "#e6a817"
  link-underline: "#121212"

typography:
  display-xl:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'aktiv-grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
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
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: 1px solid "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    padding: 0
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: 1px solid "{colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: 1px solid "{colors.sale-badge}"
  search-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    textDecoration: underline
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xxs}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  new-badge:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    typography: "{typography.caption}"
    textColor: "{colors.on-primary}"
    textDecoration: underline
  newsletter-signup:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Subscribe", and "Checkout". Rendered as a solid near-black rectangle with white uppercase text in 14px medium weight. On hover, the background shifts to pure black (`{colors.primary-active}`) with no additional shadow or scale transform — the change is barely perceptible, which is intentional. The disabled state uses `{colors.primary-disabled}` (#666666) to indicate the action is unavailable without drawing attention.

**`button-secondary`** — An outlined variant used for "Preview", "Read Excerpt", and secondary purchase options. The 1px border matches the primary ink color, and the background is transparent. On hover, the button fills solid with the primary color and the text inverts to white. This is the only button with a visible border in the system — all other buttons are either solid or text-only.

**`button-tertiary-text`** — A text-only link styled as a button, used for "View All" links in category sections and "Learn More" on blog entries. No border, no background, just an underlined text link in the primary ink color. The underline is present at rest, not just on hover — Verso does not hide its affordances.

### Cards
**`product-card`** — The core content unit of the site, used in the book grid, search results, and category pages. A white rectangle with zero border radius and no shadow — the book cover image is the only visual element. The card contains the cover image, the title in 16px regular weight, the author name in 14px muted gray, and the price in 16px regular weight. No hover state changes the card itself; the only interactive element is the "Add to Cart" button that appears on hover or focus. The card's austerity is a deliberate editorial choice: the book is the object, not the container.

**`sale-badge`** and **`new-badge`** — The only color accents in the entire system outside the black/white/gray palette. The sale badge is a small red (#cc0000) rectangle with white uppercase text reading "SALE" or a discount percentage. The new badge is a warm yellow (#e6a817) rectangle with black text reading "NEW". Both use 11px bold uppercase type and 4px corner radius. They sit in the top-left corner of the product card image, overlapping the cover.

### Navigation
**`nav-bar`** — A single horizontal strip of category links in 14px regular weight, centered on the page. The bar is 56px tall with a background matching the page canvas (`{colors.canvas}`). There is no logo in the nav bar — the Verso wordmark appears above the nav in the header. The active category is indicated by an underline on the link text. No dropdowns, no mega-menus, no search bar visible at rest — the search icon sits to the right of the category list and expands into a full-width input on click.

### Forms
**`text-input`** — Used in the checkout flow, account creation, and the newsletter signup form. A white rectangle with a 1px light gray border and 8px corner radius — the only input in the system with visible rounding. On focus, the border shifts to the primary ink color. Error state uses a red border matching the sale badge color. The newsletter signup input is paired with a small primary-colored submit button (`{newsletter-signup}`) that sits flush to the right edge of the input.

**`search-input`** — A hidden input that expands to full width when the search icon is clicked. Same styling as the text input but with reduced vertical padding (10px top/bottom instead of 12px) to match the 44px height. The search icon is a simple magnifying glass in the primary ink color, with no background circle or container.

### Footer
**`footer`** — A dense, full-width footer with a near-black background and white text. Contains three columns: "About" links (About Us, Jobs, Events), "Help" links (Shipping, Returns, Contact), and "Connect" links (Twitter, Instagram, Blog, Newsletter). All links are 12px caption weight with underlines. No social media icons — just text. The footer also contains the copyright line and a link to the Shopify privacy policy. Padding is 48px top/bottom and 16px left/right, matching the site's tight grid.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav categories collapse to hamburger menu; search icon moves to header; footer stacks to single column; book covers scale to full width |
| Tablet | 744–1128px | Two-column product grid; nav categories remain visible but truncate to 5 items with "More" link; footer remains three columns but narrows |
| Desktop | 1128–1440px | Two-column product grid with wider gutters; full nav category strip visible; search input expands on click without overlaying content |
| Wide | > 1440px | Max-width container at 1440px; product grid remains two-column but with larger cover images; nav bar remains centered within max-width |

### Touch Targets
- All buttons and links maintain a minimum 44px tap target height on mobile
- Search icon tap target is 48x48px on mobile (expanded from 32x32px on desktop)
- Hamburger menu icon tap target is 48x48px
- Product card "Add to Cart" button appears on tap (not just hover) on mobile devices
- Category links in the nav bar have 48px tap height on mobile (expanded from 40px on desktop)

### Collapsing Strategy
- On mobile, the nav bar collapses to a hamburger menu with a full-screen overlay drawer
- The search input collapses to an icon that expands to a full-width overlay on tap
- The product grid collapses from 2 columns to 1 column
- The footer collapses from 3 columns to a single stacked column
- Category filters on collection pages collapse to a "Filter" button that opens a bottom sheet
- The "Quick Add" button on product cards is hidden on mobile; users must tap through to the product page

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (the site may use a subtle shadow or border change, but this could not be reliably extracted from the static CSS)
- Error message styling for form validation (text color, background, icon usage)
- Focus ring styling for keyboard navigation (width, color, offset)
- Sub-brand or series-specific color palettes (Verso World History, Radical Thinkers, etc. may have distinct covers but the site itself uses a single palette)
- Dark mode (the site does not appear to offer a dark mode toggle)
- Loading states for product grids and search results (skeleton screens or spinners)
- Empty state designs for search results and category pages
- Animation and transition timings (the site appears to use minimal transitions, but exact durations and easing curves could not be extracted)
- The exact shade of red used for sale badges (#cc0000 is an approximation based on extracted data; the actual value may vary slightly)
- The exact shade of yellow used for new badges (#e6a817 is an approximation; the actual value may vary slightly)
- Checkout flow colors (Shopify's default checkout may override Verso's palette; the extracted colors included some Shopify Pay and Klarna widget colors that were filtered out)
