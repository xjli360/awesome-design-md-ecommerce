---
version: alpha
name: "Breville"
source_url: "https://www.breville.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A confident, kitchen-first appliance brand that balances professional-grade performance with warm, approachable design. Breville's palette is anchored in deep espresso browns and charcoals (#313638, #2d2c2f, #282726) that evoke the heft of stainless steel and the richness of freshly ground coffee, punctuated by a signature aubergine (#421540) that appears in product accents, navigation elements, and the brand's distinctive "Die-Cast" series. The system breathes through generous white space on a near-white canvas (#f5f5f5, #f8f8f8, #eff0f1), with secondary surfaces in warm greys (#bab9b8, #bbbab8, #e0e0e0) that suggest brushed metal and ceramic cooktops. A restrained accent palette of deep navy (#13294b), teal (#046b99), and a single bright blue (#00bbff) provides selective energy for call-to-action buttons and informational highlights, while amber (#d35b17) and green (#007a31) serve as status indicators for temperature and readiness. Typography relies on Archer-Book and Archer-Ssm — a refined, slightly geometric serif that feels both editorial and domestic — paired with system sans-serifs (Helvetica-Neue, Roboto, Arial) for UI density. The brand's signature design moves include pill-shaped buttons (`{rounded.full}`) that mirror the ergonomic curves of their appliances, softly rounded product cards (`{rounded.md}` ~12px), and a persistent top navigation bar that uses the deep aubergine as a grounding element. Every component feels tactile and deliberate, as if machined from a single billet of aluminum — there are no sharp corners on interactive elements, and the spacing system (`{spacing.base}`, `{spacing.lg}`, `{spacing.xl}`) creates breathing room that lets product photography and instructional content breathe. The overall effect is one of quiet authority: this is a brand that trusts the quality of its engineering over flashy decoration, using color and typography to signal precision, warmth, and culinary expertise.

colors:
  primary: "#421540"
  primary-active: "#2d0a2b"
  primary-disabled: "#c4b0c3"
  ink: "#313638"
  body: "#2d2c2f"
  muted: "#686563"
  muted-soft: "#7c7b78"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  border-strong: "#999999"
  canvas: "#f5f5f5"
  surface-soft: "#eff0f1"
  surface-card: "#ffffff"
  surface-strong: "#e8e8e8"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-blue: "#00bbff"
  accent-navy: "#13294b"
  accent-teal: "#046b99"
  accent-amber: "#d35b17"
  accent-green: "#007a31"
  accent-red: "#d32f2f"
  accent-warm-grey: "#bab9b8"
  accent-charcoal: "#282726"
  scrim: "#000000"
  star-rating: "#d35b17"

typography:
  display-xl:
    fontFamily: "'Archer-Book', 'Archer-Ssm', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Archer-Book', 'Archer-Ssm', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Archer-Book', 'Archer-Ssm', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'Archer-Book', 'Archer-Ssm', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Archer-Book', 'Archer-Ssm', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Archer-Book', 'Archer-Ssm', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Helvetica-Neue, Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Helvetica-Neue, Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Helvetica-Neue, Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "Helvetica-Neue, Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "Helvetica-Neue, Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "Helvetica-Neue, Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Helvetica-Neue, Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Helvetica-Neue, Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Helvetica-Neue, Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "Helvetica-Neue, Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  product-price:
    fontFamily: "Helvetica-Neue, Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  product-sale-price:
    fontFamily: "Helvetica-Neue, Arial, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
    color: "{colors.accent-red}"

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
    padding: 12px 28px
    height: 44px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  top-nav-link-active:
    backgroundColor: "rgba(255, 255, 255, 0.15)"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.accent-blue}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-blue}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-red}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
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
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-rating:
    color: "{colors.star-rating}"
    typography: "{typography.caption}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-overlay:
    backgroundColor: "rgba(0, 0, 0, 0.3)"
    textColor: "{colors.on-primary}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 48px
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
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
  badge-eco:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
  tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 28px
  add-to-cart-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
    border-top: "1px solid {colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 48px
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
    rounded: "{rounded.sm}"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 36px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature aubergine (#421540) with white text and a fully pill-shaped radius (`{rounded.full}`). Used for "Add to Cart," "Shop Now," and primary checkout flows. On hover, it shifts to a deeper aubergine (`{colors.primary-active}`), and in its disabled state it fades to a muted mauve (`{colors.primary-disabled}`) to signal inactivity without visual noise. The uppercase label (`{typography.button-md}`) with tight letter-spacing reinforces the brand's precision-engineered ethos.

**`button-secondary`** — An outlined or ghost variant on a white or near-white canvas (`{colors.canvas}`) with dark ink text. Typically used for "Learn More," "View Details," or secondary actions alongside primary buttons. On hover, the background fills with a soft grey (`{colors.surface-strong}`) to provide tactile feedback without competing with the primary action.

**`button-tertiary-text`** — A text-only button with no background or border, used for inline actions like "Cancel," "Clear Filters," or "See All." Relies on the same uppercase button typography but removes all container styling, keeping the interface clean and editorial.

**`button-accent-blue`** — A high-energy variant using the brand's bright blue (`{colors.accent-blue}`) for promotional CTAs, limited-time offers, or feature highlights that need to stand apart from the standard aubergine system. Shares the same pill shape and uppercase typography as the primary button.

**`button-pill-outline`** — A slim, outlined pill button used for filter chips, category tags, and toggle-style selections. The 1px hairline border (`{colors.hairline}`) keeps it lightweight, and the smaller typography (`{typography.button-sm}`) allows it to sit comfortably in dense UI regions like product listing pages.

### Navigation
**`top-nav`** — The persistent global navigation bar, anchored in the brand's deep aubergine (`{colors.primary}`) at 64px height. This dark, grounding element creates immediate brand recognition and provides high contrast for white logo text and navigation links. The bar spans full width and sits above all page content.

**`top-nav-link`** — Navigation links rendered in white with uppercase, medium-weight sans-serif typography (`{typography.nav-link}`). Each link has generous horizontal padding (`{spacing.base}`) for comfortable touch targets. The active state uses a semi-transparent white overlay (`rgba(255, 255, 255, 0.15)`) with subtle rounding (`{rounded.sm}`) to indicate the current section without adding a heavy underline or bar.

**`breadcrumb`** — Secondary navigation rendered in small caption text (`{typography.caption}`) with muted grey coloring. The active breadcrumb uses the darker ink color to indicate the current page. Breadcrumbs appear on product detail pages and category listings to support deep site navigation.

### Cards
**`product-card`** — The primary content container for product listings, featuring a white surface (`{colors.surface-card}`) with soft 12px rounding (`{rounded.md}`). The card has no padding at the container level — instead, the image occupies the full top half (with top-only rounding), and content padding is applied to the lower section (`{spacing.base}` horizontal, `{spacing.lg}` bottom). This creates a clean, magazine-like editorial grid for product photography.

**`product-card-badge`** — An amber (`{colors.accent-amber}`) badge overlaid on product images to indicate "New," "Best Seller," or "Limited Edition." The small uppercase label (`{typography.badge}`) with tight padding keeps the badge compact and non-intrusive. Additional badge variants use blue (`{colors.accent-blue}`) for "New" and red (`{colors.accent-red}`) for "Sale."

**`product-card-rating`** — Star ratings rendered in the brand's amber (`{colors.star-rating}`), providing a warm, food-friendly accent that echoes the color of caramelized sugar or toasted bread — a subtle nod to the culinary context of the products.

### Forms
**`text-input`** — Standard text input fields with a white background, 1px hairline border (`{colors.hairline}`), and subtle 8px rounding (`{rounded.sm}`). On focus, the border thickens to 2px and shifts to the brand's bright blue (`{colors.accent-blue}`) for clear, accessible focus indication. Error states use a red border (`{colors.accent-red}`) to signal validation issues.

**`select-dropdown`** — Dropdown selectors sharing the same dimensions and styling as text inputs, ensuring form consistency across the checkout, account, and product filter experiences.

**`quantity-selector`** — A compact, horizontally arranged control for adjusting product quantities. The central value uses body typography, flanked by small square buttons (`{rounded.xs}`) with soft grey backgrounds (`{colors.surface-soft}`) for increment and decrement actions. The entire control is bordered by a 1px hairline to visually group the three elements.

### Footer
**`footer`** — A full-width dark footer using the brand's deepest charcoal (`{colors.ink}`) as the background, with white and muted grey text for maximum readability. Section headings use uppercase caption typography for visual hierarchy, while links use the standard link style in a softer grey (`{colors.muted-soft}`) to reduce visual weight. The footer contains site maps, legal links, social icons, and newsletter signup forms.

### Badges & Tags
**`badge-new`**, **`badge-sale`**, **`badge-eco`** — Small, color-coded badges that communicate product attributes at a glance. Each uses the brand's uppercase badge typography (`{typography.badge}`) with minimal 4px rounding (`{rounded.xs}`) and tight padding. The blue variant signals new arrivals, red signals sale or clearance, and green signals eco-friendly or sustainable products. These badges appear on product cards, hero banners, and category pages.

### Accordion
**`accordion-header`** — Collapsible section headers used in product descriptions, FAQs, and specification panels. The header uses a soft grey background (`{colors.surface-soft}`) with the brand's serif title typography, creating a clear visual boundary between collapsed sections. Content panels use the white canvas background with body typography for readability.

### Tabs
**`tab-active`** and **`tab-inactive`** — Pill-shaped tab buttons used for product category filtering, specification toggles, and content segmentation. Active tabs fill with the brand's primary aubergine, while inactive tabs use a soft grey background with muted text. The pill shape (`{rounded.full}`) and uppercase button typography maintain consistency with the button system.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger menu; hero banner reduces to 48px padding; search bar moves to expandable icon; product cards stack vertically with full-width images; footer links stack in single column; accordion becomes primary content reveal pattern |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links with "More" dropdown; hero banner uses 32px padding; search bar remains visible but compact; footer uses two-column layout; product cards show 2-across grid |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links visible; hero banner uses section-level padding (64px); search bar at full width; footer uses three-column layout; product cards show 3-across grid with hover state for quick-add |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero banner uses max-width constraint; all components scale proportionally; additional whitespace at container edges; product cards show 4-across grid |

### Touch Targets
- All interactive elements (buttons, links, form controls) maintain a minimum 44px touch target height
- Top-nav links use 16px horizontal padding to ensure comfortable tap areas
- Quantity selector buttons are 28px minimum with adequate spacing between increment/decrement
- Product card tap targets extend to the full card area, not just the title or price text
- Filter chips and tab buttons use 8px vertical padding to reach 44px total height
- Search bar and text inputs use 48px height for comfortable interaction on all devices

### Collapsing Strategy
- Top navigation collapses from full link set to hamburger menu at the mobile breakpoint (< 744px)
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer collapses from 3 columns (desktop) to 2 (tablet) to 1 (mobile)
- Hero banner reduces vertical padding from 64px to 48px to 32px as viewport narrows
- Search bar collapses from full-width input to icon-only toggle on mobile
- Accordion sections remain collapsed by default on all breakpoints, expanding on user interaction
- Product card badges and ratings may stack vertically on mobile to maintain readability
- Breadcrumb navigation may truncate with "..." on mobile, showing only the current and parent page

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components beyond primary/secondary buttons (specific color values for card hover, link hover, tab hover, etc.)
- Focus ring styles (color, width, offset, and animation) for keyboard navigation
- Error state styling for select dropdowns, quantity selectors, and accordion interactions
- Success and warning state colors for form validation and system messages
- Dark mode color palette and component adjustments
- Sub-brand palettes for Breville's product lines (Barista Express, Die-Cast, Juice Fountain, etc.)
- Animation and transition timing values (duration, easing curves) for hover, focus, and state changes
- Loading state designs (skeleton screens, spinners, progress indicators)
- Modal and dialog component styling (overlay, close button, animation)
- Tooltip and popover component styling (arrow, background, z-index)
- Rating component star sizes and spacing for different display contexts
- Product image zoom and gallery interaction states
- Video player component styling (play button, controls, progress bar)
- Cookie consent banner and GDPR-related component styling
- Print stylesheet specifications
- Specific font weights for Archer-Book and Archer-Ssm beyond the 400 weight observed
- Exact font loading strategy and fallback font behavior
- Icon library specification (SVG, icon font, or custom illustration system)
- Z-index hierarchy for modals, overlays, navigation, and tooltips
- Box shadow values for cards, dropdowns, and elevated components
