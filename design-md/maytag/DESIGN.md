---
version: alpha
name: "Maytag"
source_url: "https://www.maytag.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every Maytag washing machine ships with a steel lid heavy enough to feel like a commitment — and the digital presence mirrors that physical weight. The brand's documented deep blue (#003da5) functions less like a corporate accent and more like an enamel coating, applied thickly across the top navigation, hero overlays, and primary CTAs where it reads as the color of a factory floor sign demanding attention. A bright yellow (#ffc220) punches through that blue the way a caution stripe cuts across an industrial beam — it marks promotional badges, sale callouts, and seasonal campaign buttons, creating a two-tone voltage system that no other appliance brand runs this aggressively. Below that high-contrast pair, the UI settles into a utilitarian palette of cool greys (#58595b, #a7a8aa, #d1d3d4) that echo stamped-metal control panels and powder-coated chassis. Typography is emphatically sans-serif: heavy-weight condensed headings deliver product names and price points at a shout, while body copy runs in a standard system sans-serif stack at 400 weight with generous line-height for specification tables and feature lists that need to be scanned, not savored. Corners are kept tight — buttons and cards use modest radii (`{rounded.xs}` to `{rounded.sm}`), refusing the soft, friendly pill shapes of lifestyle brands in favor of squared-off containers that suggest precision-stamped sheet metal. Product cards sit on clean white surfaces (`{colors.surface-card}`) with hairline borders (`{colors.hairline}`) rather than drop shadows, stacking in dense grids that prioritize comparison shopping over editorial browsing. The hero module runs full-bleed photography of washers and dryers shot at eye level against dark studio backgrounds, overlaid with bold white display text and a yellow "Shop Now" button (`{colors.accent-yellow}`) that creates maximum contrast against the scrim. Navigation is horizontal and utility-dense: category mega-menus for washers, dryers, kitchen, and parts sit alongside a persistent search bar and account/cart icons, all on a deep blue bar (`{colors.primary}`) that anchors every page. The spacing system runs tighter than lifestyle DTC — `{spacing.md}` and `{spacing.base}` dominate interior padding, opening up only at section boundaries (`{spacing.section}`) to separate major content blocks. The overall system reads as a showroom floor: bright overhead lighting, everything on a grid, nothing decorative that doesn't also communicate a product specification or a price.

colors:
  primary: "#003da5"
  primary-active: "#002d7a"
  primary-disabled: "#99b3d6"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#58595b"
  muted-soft: "#a7a8aa"
  hairline: "#d1d3d4"
  hairline-soft: "#e6e7e8"
  border-strong: "#939598"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-strong: "#e6e7e8"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-yellow: "#ffc220"
  accent-yellow-active: "#e5a800"
  accent-red: "#da291c"
  accent-green: "#008a00"
  accent-blue-light: "#0077c8"
  scrim: "#000000"
  star-rating: "#ffc220"
  promo-banner: "#1a1a1a"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  nav-link-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  product-price:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  product-sale-price:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
    color: "{colors.accent-red}"
  spec-label:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.35
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
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-promo:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 36px
    height: 52px
  button-promo-active:
    backgroundColor: "{colors.accent-yellow-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-outline-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.on-dark}"
  top-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  top-nav-utility:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link-sm}"
    height: 36px
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  top-nav-link-active:
    backgroundColor: "rgba(255, 255, 255, 0.15)"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.xs}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.xl}"
    border-bottom: "2px solid {colors.primary}"
  mega-menu-heading:
    typography: "{typography.title-sm}"
    color: "{colors.primary}"
  mega-menu-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "4px 0"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.accent-red}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs} {rounded.xs} 0 0"
  product-card-content:
    padding: "{spacing.base} {spacing.base} {spacing.lg}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.product-price}"
    color: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.product-sale-price}"
    color: "{colors.accent-red}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-rating:
    color: "{colors.star-rating}"
    typography: "{typography.caption}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-overlay:
    backgroundColor: "rgba(0, 0, 0, 0.45)"
    textColor: "{colors.on-dark}"
  hero-banner-cta:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: "16px 36px"
    height: 52px
  hero-banner-secondary-cta:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "13px 27px"
    height: 48px
    border: "2px solid {colors.on-dark}"
  promo-bar:
    backgroundColor: "{colors.promo-banner}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    height: 36px
  compare-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.lg}"
    border-top: "2px solid {colors.primary}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
    border-bottom: "1px solid {colors.hairline-soft}"
  spec-table-label:
    typography: "{typography.spec-label}"
    color: "{colors.ink}"
  spec-table-alt-row:
    backgroundColor: "{colors.surface-soft}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
    border-right: "1px solid {colors.hairline}"
  filter-heading:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.md} 0"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 14px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.caption}"
    color: "{colors.on-dark}"
    textTransform: uppercase
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-energy-star:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    border-bottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} 0"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    color: "{colors.ink}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    height: 36px

## Components

### Buttons
**`button-primary`** — The workhorse CTA rendered in Maytag's deep blue (#003da5) with white uppercase text and a tight 4px radius (`{rounded.xs}`) that keeps the shape squared-off and industrial. Used for "Add to Cart," "Find a Retailer," and primary checkout actions. On hover the blue deepens to (#002d7a), and the disabled state washes out to a pale steel-blue (#99b3d6) that recedes without disappearing. The heavy 700-weight uppercase label (`{typography.button-md}`) with wide letter-spacing gives every button the authority of a control-panel label.

**`button-secondary`** — A white-fill button outlined with a 2px blue border, used for secondary actions like "Compare," "View Details," and "Save for Later." The text runs in the primary blue rather than ink, creating a clear visual hierarchy against the filled primary button. On hover the background tints to a soft grey (`{colors.surface-soft}`) and the border darkens to match the active primary state.

**`button-tertiary-text`** — A borderless, background-free text button in blue for inline actions: "See All Features," "Clear Filters," "View Specs." Shares the uppercase typography of the primary button but removes all container chrome, relying on color alone to signal interactivity.

**`button-promo`** — The high-visibility promotional CTA in bright yellow (#ffc220) with dark ink text. Reserved for hero banners, seasonal sale modules, and campaign landing pages where maximum contrast against dark photography backgrounds is needed. At 52px height with `{typography.button-lg}` it runs slightly larger than the standard primary to command attention at the top of the page funnel.

**`button-outline-dark`** — A white-bordered ghost button designed for use on dark backgrounds — hero overlays, the footer, and full-bleed promotional sections. The 2px white border and white text provide legibility against photography without competing with the yellow promo CTA.

### Navigation
**`top-nav`** — A 64px primary navigation bar in deep blue (#003da5) that anchors every page. The bar holds the Maytag wordmark, category links (Washers, Dryers, Kitchen, Laundry Accessories, Parts & Filters), a search input, and account/cart icons — all in white. This is the single strongest brand signal on the page, establishing the blue immediately on load.

**`top-nav-utility`** — A slim 36px utility bar above the primary nav in near-black (#1a1a1a), holding secondary links: "Find a Store," "Support," "Order Status," and the phone number. The darker bar creates a visual cap that frames the blue navigation below and provides a place for service-oriented links that don't belong in the main product navigation.

**`mega-menu`** — Category flyouts drop below the nav on a white surface with a 2px blue bottom border that ties them visually to the parent bar. Headings within the mega-menu use the primary blue (`{colors.primary}`) while links use standard body color, creating a clear scan pattern. The panel accommodates product-type links, promotional imagery, and "Shop All" CTAs in a multi-column layout.

**`search-bar`** — A compact search field integrated into the top nav with a white background, 1px hairline border, and 4px radius. On focus the border shifts to a 2px blue ring, matching the input focus pattern used across all form elements.

### Cards
**`product-card`** — The primary product listing unit: a white card with a 1px soft border (`{colors.hairline-soft}`) and minimal 4px rounding (`{rounded.xs}`). The image fills the top half with a light grey background (`{colors.surface-soft}`) for loading states, and content padding (`{spacing.base}` sides, `{spacing.lg}` bottom) holds the product title, price, rating stars, and an "Add to Compare" checkbox. Cards are designed for dense grid layouts where shoppers scan across 15–20 products per page, so visual density is prioritized over editorial whitespace.

**`product-card-badge`** — A yellow (#ffc220) badge with dark ink text overlaid on the product image corner, used for "Best Seller," "Top Rated," and promotional flags. The uppercase badge typography (`{typography.badge}`) and tight padding keep it compact. Variant badges use blue (`{colors.primary}`) for "New" items and red (`{colors.accent-red}`) for clearance markdowns.

**`product-card-rating`** — Star ratings rendered in yellow (#ffc220) with caption-size review counts. The yellow stars echo the promotional badge color, creating a consistent warm accent that contrasts against the dominant blue-and-grey palette.

### Specification Table
**`spec-table`** — A striped table used on product detail pages to present capacity, dimensions, energy ratings, cycle options, and installation requirements. Alternating rows use the soft surface (`{colors.surface-soft}`) against white, with bold spec labels (`{typography.spec-label}`) on the left and standard body text on the right. The 1px bottom border separates rows without adding visual weight. This is the single most-used component on appliance PDPs, often running 30+ rows.

### Compare Bar
**`compare-bar`** — A sticky bar that appears at the bottom of product listing pages when the user selects items for comparison. The soft grey background (`{colors.surface-soft}`) with a 2px blue top border anchors it to the Maytag brand system. It holds thumbnail images, product names, and a "Compare Now" primary button, accommodating up to four products side by side.

### Filter Sidebar
**`filter-sidebar`** — A left-rail filter panel on product listing pages with a white background and a 1px right border separating it from the grid. Filter groups (Price, Capacity, Color, Features, Energy Star) use collapsible accordion headers (`{typography.title-sm}`) with checkboxes and range sliders inside. Active filter selections appear as blue-filled chips (`{colors.primary}`) at the top of the sidebar for quick removal.

### Forms
**`text-input`** — Standard input fields with a white background, 1px hairline border, and 4px radius. The 48px height provides comfortable touch targets, and focus states use a 2px blue border matching the primary color. Error states switch to a 2px red border (`{colors.accent-red}`) with inline error text below the field.

**`select-dropdown`** — Styled dropdowns matching text-input dimensions and border treatment, used for capacity selectors, color pickers, and sort-order controls on listing pages.

### Hero
**`hero-banner`** — A full-bleed hero module with a dark background (either solid ink or photography with a 45% black overlay) and white display text at the largest scale (`{typography.display-xl}`). The primary CTA is the yellow promo button, with an optional white-outline secondary CTA. Hero modules typically showcase seasonal promotions, new product launches, or bundle deals with prominent pricing callouts.

### Promotional Bar
**`promo-bar`** — A narrow black banner above the utility nav that cycles through promotional messages: free delivery thresholds, financing offers, and seasonal sale announcements. White caption text on the dark background ensures high contrast without competing with the blue navigation system below.

### Badges
**`badge-sale`** — Red (#da291c) badges for clearance and markdown pricing. **`badge-new`** — Blue (#003da5) badges for new arrivals and just-launched models. **`badge-energy-star`** — Green (#008a00) badges for Energy Star certified appliances, a critical trust signal in the major-appliance category where energy efficiency directly impacts purchase decisions. All three variants share the uppercase badge typography and tight 4px rounding.

### Footer
**`footer`** — A dark footer in near-black (#1a1a1a) with four-column link groups: Products, Support, About Maytag, and Connect. Section headings use uppercase caption typography, while links run in muted grey (`{colors.muted-soft}`). The footer also holds legal text, warranty information links, and the Whirlpool Corporation parent-brand disclosure — all in the smallest caption size.

### Accordion
**`accordion-header`** — Borderless accordion headers with a bottom hairline, used on PDPs for Features, Specifications, Reviews, and Q&A sections. The clean divider-based approach (rather than filled backgrounds) keeps the page feeling open and scannable, consistent with the showroom-floor aesthetic.

### Breadcrumb & Pagination
**`breadcrumb`** — Small caption-size breadcrumbs in muted grey, with the current page in ink. Used on PDPs and category pages to show the navigation path: Home > Washers > Top Load Washers > [Model]. **`pagination-button`** — Bordered page-number buttons at the bottom of listing grids, with the active page filled in primary blue.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger with full-screen blue overlay; utility bar hides behind menu; hero reduces to stacked layout with text above CTA; filter sidebar converts to bottom-sheet modal triggered by "Filter" button; compare bar stacks vertically showing 2 products max; spec table scrolls horizontally; mega-menu becomes accordion-style drill-down |
| Tablet | 744–1128px | Two-column product grid; top-nav shows logo, search icon, and hamburger; utility bar remains visible; hero maintains overlay layout at reduced padding; filter sidebar remains as collapsible left rail; compare bar shows 3 products; spec table fits without scroll; footer collapses to two columns |
| Desktop | 1128–1440px | Three- to four-column product grid; full top-nav with all category links, search bar, and utility icons; hero runs full-bleed with section-level padding; filter sidebar fixed at 280px width; compare bar shows 4 products with full thumbnails; footer in four columns |
| Wide | > 1440px | Max-width container at 1440px centered; four-column product grid; hero imagery scales to container max-width; additional canvas-color margin at viewport edges; all components maintain desktop proportions |

### Touch Targets
- All buttons maintain 48px minimum height; the promo button runs 52px for hero emphasis
- Top-nav links use 16px horizontal padding for comfortable mobile taps
- Filter checkboxes and accordion headers maintain 44px minimum tap height
- Product card tap target extends to full card surface, not just text elements
- Pagination buttons use 36px height with adequate inter-button spacing
- Search input maintains 40px height in nav, expanding to 48px in mobile full-screen search
- Compare checkboxes on product cards use 24px visible checkbox with 44px tap-target padding

### Collapsing Strategy
- Top navigation collapses from full horizontal links to hamburger menu at < 744px; utility bar folds into the hamburger panel
- Product grid collapses from 4 columns (wide) to 3-4 (desktop) to 2 (tablet) to 1 (mobile)
- Filter sidebar converts from persistent left rail to modal bottom-sheet on mobile
- Compare bar reduces from 4-product horizontal to 2-product stacked on mobile
- Spec tables switch from full-width to horizontally scrollable on screens below 744px
- Hero banners shift from text-overlay-on-image to stacked text-above-image on mobile
- Footer collapses from 4 columns to 2 (tablet) to 1 (mobile) with accordion-style section reveal
- Mega-menu converts from hover-triggered flyout to tap-triggered accordion drill-down on touch devices
- Breadcrumbs truncate to show only parent and current page on mobile, with "..." for intermediate levels

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All color values are estimated from widely-documented Maytag brand guidelines, not extracted from the live site** — the site returned "Access Denied" during crawl, blocking all CSS/token extraction
- **No font-family stacks were extracted** — typography tokens use system sans-serif defaults; Maytag may use a proprietary or licensed typeface (possibly a custom Helvetica variant or brand-specific face) that could not be verified
- Exact border-radius values could not be measured; the `{rounded.xs}` (4px) default is an informed estimate based on the brand's industrial aesthetic
- Hover, focus-ring, and transition/animation values (duration, easing) were not captured
- Dark mode palette, if one exists, is unknown
- Exact spacing and padding values are estimates; the live site may use a different scale or component-specific overrides
- The accent-yellow (#ffc220) is based on Maytag's widely-recognized gold/yellow brand accent but may differ from the exact digital token
- The primary blue (#003da5) is based on Maytag's documented brand blue; the live implementation may use a variant
- Sub-brand or product-line-specific color treatments (e.g., Maytag Commercial, Maytag Pet Pro) are not represented
- Modal, toast, and tooltip component styles were not captured
- Loading states (skeleton screens, spinners) are unknown
- Image carousel and gallery interaction patterns on PDPs were not observed
- Exact mega-menu column counts and content structure could not be verified
- Icon system (SVG sprite, icon font, or inline SVG) is unknown
- Z-index stacking order for modals, mega-menus, compare bar, and sticky nav is not documented
- Print stylesheet specifications are not included
- Financing/payment badge styling (Affirm, PayPal) was not captured
- Form validation patterns beyond border color (inline messages, toast notifications) are estimated
