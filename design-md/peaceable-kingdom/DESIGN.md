---
version: alpha
name: "Peaceable Kingdom"
source_url: "https://www.mindware.com/brand/peaceable-kingdom"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A playful, educational brand built on a warm white canvas and a distinctive coral-orange primary (#c74c00) that appears on every add-to-cart button, navigation accent, and product badge — a color that reads more like a child's crayon box than a corporate identity. The palette is deliberately cheerful: a soft pink (#ee5f9e) for sale tags and promotional banners, a sky blue (#1f9cd8) for informational badges and age-range indicators, and a bright green (#80b800) for "new" labels and eco-friendly messaging. Typography runs on Roboto Condensed for headlines and Arial for body text, creating a clear hierarchy where condensed display faces at 24–32px carry product names and category headers, while standard sans-serif at 14–16px handles descriptions and pricing. The brand uses generous {rounded.lg} (20px) on product cards and {rounded.full} on buttons and badges, giving every interactive element a soft, approachable feel that signals "made for children and families." Navigation is a clean white bar with the coral-orange logo mark and category dropdowns, while the footer stacks multiple columns of links in muted gray (#444444) against a light blue-gray background (#acc9d4). Product cards feature a white background with a subtle drop shadow, a large product image, the title in Roboto Condensed Bold, a star-rating row, and a coral-orange "Add to Cart" button — the same button pattern repeated across the entire site. The overall effect is a brand that feels like a well-organized toy box: colorful but not chaotic, structured but not rigid, with enough visual warmth to appeal to both parents and children.

colors:
  primary: "#c74c00"
  primary-active: "#9d3700"
  primary-disabled: "#f6b6d2"
  ink: "#181818"
  body: "#221f1f"
  muted: "#444444"
  muted-soft: "#6a6a6a"
  hairline: "#d0d0d0"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-pink: "#ee5f9e"
  accent-blue: "#1f9cd8"
  accent-green: "#80b800"
  accent-orange: "#fa6f22"
  accent-yellow: "#fac300"
  accent-teal: "#67bae8"
  accent-sky: "#eef9fd"
  accent-warm-gray: "#acc9d4"
  star-rating: "#fac300"
  sale-badge: "#ee5f9e"
  new-badge: "#80b800"
  age-badge: "#1f9cd8"
  link-blue: "#0073b2"
  footer-bg: "#acc9d4"
  footer-text: "#2c2c2c"

typography:
  display-xl:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  price:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
    color: "{colors.accent-pink}"

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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-accent:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  text-input-error:
    border: "2px solid {colors.accent-pink}"
    rounded: "{rounded.sm}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.price}"
    padding: "{spacing.xs} {spacing.base}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    padding: "{spacing.xs} {spacing.base}"
  product-card-rating:
    typography: "{typography.caption}"
    color: "{colors.star-rating}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
    margin: "0 {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-age:
    backgroundColor: "{colors.age-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-eco:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.footer-text}"
  footer-link-hover:
    color: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginBottom: "{spacing.base}"
  hero-banner:
    backgroundColor: "{colors.accent-sky}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "12px 32px"
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  category-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1:1"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 18px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "10px 24px"
    height: 44px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Shop Now," and primary form submissions. Features a solid coral-orange (#c74c00) background with white uppercase Roboto Condensed text. On hover, the background shifts to a deeper burnt orange (#9d3700). The disabled state uses a pale pink (#f6b6d2) background with white text. All primary buttons use full pill rounding for a friendly, approachable feel.

**`button-secondary`** — An outlined variant used for "Learn More," "View Details," and secondary actions. White background with a 2px coral-orange border and coral-orange text. On hover, the border and text shift to the deeper burnt orange, and the background becomes a soft off-white. Same pill rounding and uppercase condensed typography as the primary button.

**`button-tertiary-text`** — A text-only button used for "Cancel," "Clear Filters," and inline actions. No background or border, just coral-orange Roboto Condensed uppercase text. On hover, the color shifts to burnt orange with no underline decoration, keeping the interface clean.

**`button-pill-accent` / `button-pill-blue` / `button-pill-green`** — Small accent pill buttons used for promotional tags, category filters, and quick-action links. Each uses a distinct brand accent color (pink, blue, green) with white text and full pill rounding. These appear on sale banners, age-range selectors, and eco-friendly product badges.

### Cards
**`product-card`** — The primary product display component, used on category pages, search results, and featured collections. A white card with soft 20px rounding and a subtle drop shadow (0 2px 8px rgba(0,0,0,0.08)). Contains a square product image with rounded top corners, the product title in Roboto Condensed 16px/600, the price in 18px/700, a star-rating row in yellow (#fac300), and a coral-orange "Add to Cart" pill button at the bottom. On hover, the shadow deepens slightly to indicate interactivity.

**`category-card`** — Used on the homepage and category landing pages to display product categories. A white card with 20px rounding, a square category image with 12px rounding, and the category name in Roboto Condensed 16px/600. The card has a lighter shadow (0 2px 8px rgba(0,0,0,0.06)) and padding of 24px. On hover, the entire card lifts slightly with a subtle translateY animation.

### Badges
**`badge-new`** — A small green (#80b800) pill badge with white uppercase text, used to flag newly added products. Padding of 4px 10px with full pill rounding and 11px/700 Roboto Condensed text. Positioned at the top-left corner of product images.

**`badge-sale`** — A pink (#ee5f9e) pill badge identical in structure to the new badge, used for discounted items. Appears over the product image with the word "SALE" or a percentage off.

**`badge-age`** — A blue (#1f9cd8) pill badge used to display recommended age ranges (e.g., "Ages 4+"). Same structure as other badges, positioned near the product title or on the product detail page.

**`badge-eco`** — A green (#80b800) pill badge used for eco-friendly or sustainable products. Same structure, with text like "Eco-Friendly" or "Sustainable Materials."

### Navigation
**`top-nav`** — A clean white navigation bar 72px tall, containing the Peaceable Kingdom logo (coral-orange text or mark), a search bar, and category dropdown links. Navigation links use Roboto Condensed 16px/600 in dark ink (#181818). The active and hover states shift the link color to coral-orange. The nav bar has a subtle bottom border (1px solid #d0d0d0) to separate it from the page content.

**`nav-dropdown`** — A white dropdown panel with 8px rounding, appearing below category links on hover. Contains subcategory links in Arial 16px/400 with 8px vertical padding per item. The dropdown has a light shadow and appears with a smooth fade-in animation.

### Forms
**`text-input`** — Standard text input used for search, newsletter signup, and contact forms. White background, 14px horizontal padding, 10px vertical padding, 44px height, 8px rounding, and a 1px light gray border. On focus, the border becomes 2px coral-orange. Error state uses a 2px pink border.

**`search-bar`** — A pill-shaped search input used in the top navigation. Soft gray background (#f7f7f7), 16px horizontal padding, 8px vertical padding, 40px height, full pill rounding, and a 1px light gray border. On focus, the border becomes 2px coral-orange. Includes a magnifying glass icon on the left.

**`newsletter-input` / `newsletter-submit`** — A paired input and button for email signup. The input is a white pill with 18px horizontal padding, 44px height, and a 1px light gray border. The submit button is a coral-orange pill with 24px horizontal padding and the same height. The pair sits side by side with no gap, creating a seamless combined component.

### Footer
**`footer`** — A multi-column footer with a light blue-gray background (#acc9d4) and dark gray text (#2c2c2c). Contains columns for "Shop," "About," "Support," and "Connect," each with a Roboto Condensed 16px/600 heading and Arial 14px/400 link list. Links hover to coral-orange. The footer includes a newsletter signup row, social media icons (likely in the brand's accent colors), and a copyright line at the bottom. Padding of 48px top and bottom.

### Hero
**`hero-banner`** — A full-width promotional banner used on the homepage and seasonal landing pages. Light sky blue background (#eef9fd) with dark ink text, large Roboto Condensed display typography (28px/700), and a coral-orange CTA button. Padding of 64px on top and bottom, 32px on sides, with 20px rounding on the bottom corners. The banner may include a background illustration or pattern overlay.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row); nav collapses to hamburger menu; hero banner reduces padding to 32px 16px; footer stacks to single column; search bar becomes a full-width expandable input; product card images reduce to 3:4 aspect ratio; buttons become full-width on mobile |
| Tablet | 744–1128px | Two-column product grid; nav shows all top-level categories but hides subcategories behind dropdowns; hero banner uses 48px padding; footer shows 2 columns; search bar remains visible but shrinks to 32px height |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; hero banner at full padding; footer shows 4 columns; search bar at 40px height; product cards show hover shadow lift |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px centered; nav and footer remain at full width; hero banner may include a full-width background image; product cards maintain 1:1 image ratio |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px on mobile devices
- Product card "Add to Cart" buttons are at least 44px tall with 20px horizontal padding
- Nav hamburger icon is 48x48px with 8px internal padding
- Category card tap areas cover the entire card surface
- Badge tap targets are at least 32x32px with adequate spacing between adjacent badges
- Footer links have 44px minimum tap height with 8px vertical padding between items

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-in drawer from the left containing all category links and a search bar
- Product filters collapse to a "Filter" button that opens a modal overlay on mobile
- Product description sections (details, reviews, shipping) collapse into accordion panels on mobile and tablet
- Footer columns collapse from 4 columns to 2 columns at 744px, then to a single column below 480px
- Hero banner text and CTA stack vertically on mobile, with the CTA becoming full-width
- Product image galleries collapse from thumbnail strip to swipeable carousel on mobile
- Category navigation (age ranges, themes) collapses from horizontal scroll to a dropdown selector on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow depth, translateY animation) were inferred from common e-commerce patterns, not extracted from the live site
- Error states for form validation (text-input-error) are assumed based on the accent-pink color, but exact styling (icon placement, message position) is unknown
- Sub-brand palettes for specific product lines (e.g., "Peaceable Kingdom Preschool" vs. "Peaceable Kingdom Family") could not be extracted
- Dark mode or high-contrast mode styles are not present in the extracted data
- The exact font weights for Roboto Condensed (600 vs 700) are inferred; the live site may use different weight values
- Button hover animations (scale, shadow) are not documented in the extracted CSS
- The star-rating component's exact implementation (SVG vs icon font, size, spacing) is unknown
- Dropdown menu animation timing and easing functions are not available
- The hero banner's background illustration or pattern is not captured in the extracted data
- Social media icon colors and hover states are not documented
- The checkout flow (cart page, payment forms) is not represented in the extracted data
- Accessibility focus styles (outline, ring) are not present in the extracted CSS
- The exact spacing between product card elements (title to price, price to rating) is inferred from common patterns
- Mobile navigation drawer animation (slide direction, overlay opacity) is assumed
- The newsletter form's success and error states are not documented
- Category card hover effects (lift, shadow change) are inferred from the product card pattern
- The brand's icon set (search, cart, user, heart) is not extracted; icon colors and sizes are assumed
- Print styles and reduced-motion preferences are not documented
