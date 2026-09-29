---
version: alpha
name: "Bullstrap"
source_url: "https://www.bullstrap.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A leather goods brand that builds its entire visual identity around the tension between a deep, almost-black ink (#222222) and a single saturated accent — a rich, slightly cooled crimson (#c51c34) that appears on the primary CTA, the add-to-cart button, and the brand's signature logo mark. The site reads as a product-first catalog: generous product imagery on a white canvas (#fafafa) with tight typographic control from Barlow Condensed, a condensed sans-serif that gives headlines a muscular, automotive-grade density at 700 weight. The secondary palette introduces a warm saddle-brown (#b59677) and a deep teal (#108474) that surface in category badges and accent stripes, suggesting a brand that straddles rugged utility and refined craftsmanship. Navigation is minimal — a single sticky bar with dropdown menus, the logo centered, and a search icon that expands into a full-width input on click. Product cards use a soft shadow on hover and a clean 1px hairline (#dedede) border in rest state, with the crimson accent reserved exclusively for the "Add to Cart" button and the price display. The checkout flow, powered by Shopify, inherits the brand's crimson for the primary action but defaults to Shopify's own button styles for secondary actions, creating a slight visual disconnect between the marketing pages and the purchase funnel. The overall feel is one of restrained masculinity — no decorative flourishes, no rounded corners beyond {rounded.sm} on buttons, no gradients — just a sharp, inventory-focused layout that lets the leather textures and product photography do the selling.

colors:
  primary: "#c51c34"
  primary-active: "#a11529"
  primary-disabled: "#e88a96"
  ink: "#222222"
  body: "#1b1b1b"
  muted: "#7b7b7b"
  muted-soft: "#c7c7c7"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#fafafa"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-saddle: "#b59677"
  accent-teal: "#108474"
  accent-gold: "#e0b252"
  badge-green: "#428445"
  badge-red: "#ec0101"
  star-rating: "#e0b252"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
    textTransform: uppercase
  title-sm:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.75px
    textTransform: uppercase
  link:
    fontFamily: "'Jost', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', sans-serif"
    fontSize: 20px
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
    padding: 12px 32px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 31px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 31px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  price-display:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.price}"
  price-sale-display:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.price-sale}"
  badge-inventory:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  star-rating:
    backgroundColor: transparent
    textColor: "{colors.star-rating}"
    typography: "{typography.caption}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  search-icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
    height: 44px
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
  category-card-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 0 0 16px 0
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in the signature crimson (#c51c34) with white uppercase Barlow Condensed text. Used exclusively for "Add to Cart", "Shop Now", and primary checkout actions. On hover, the background shifts to a deeper crimson (#a11529). The disabled state uses a pale pink (#e88a96) to indicate inactivity while maintaining brand recognition.

**`button-secondary`** — A white button with ink-colored text, used for secondary actions like "View Details" or "Learn More". The outline variant uses a transparent background with a 1px ink border. Both variants share the same 44px height and uppercase typography as the primary button, maintaining visual consistency across the action hierarchy.

**`button-tertiary-text`** — A text-only button with no background or border, used for less prominent actions like "Cancel" or "Clear Filters". Inherits the same uppercase Barlow Condensed styling but removes the container, relying on hover underline for affordance.

### Cards
**`product-card`** — A clean, borderless card with a white background and no rounded corners. The product image sits flush against the top edge, with the title, price, and a star-rating row below. On hover, a subtle shadow elevates the card, and the "Add to Cart" button fades in. The card uses a 1px hairline border (#dedede) in its rest state to define the boundary.

**`category-card`** — A full-width card with a soft gray background (#f5f5f5), used for category navigation on the homepage. The category name appears in uppercase Barlow Condensed centered over the image. On hover, the background shifts to a slightly darker gray (#eeeeee), providing a subtle interactive cue without animation.

### Navigation
**`nav-bar`** — A fixed-position top bar at 64px height with a white background. The brand logo sits centered, with navigation links in uppercase Barlow Condensed on either side. The search icon and cart icon sit on the right edge. On scroll, a 1px bottom hairline appears to separate the nav from the page content.

**`nav-dropdown`** — A full-width dropdown panel that appears on hover over top-level nav items. Contains category links in a two-column grid layout, with no rounded corners and a 1px top hairline. Links use the same uppercase Barlow Condensed styling as the nav bar.

### Forms
**`text-input`** — A standard text input with a white background, 1px hairline border (#dedede), and 4px rounded corners. On focus, the border shifts to the ink color (#222222) with no outline offset. Used for search, newsletter signup, and checkout fields.

**`search-bar`** — A slightly shorter input (44px) with a soft gray background (#f5f5f5) and no border, used in the expanded search overlay. The placeholder text appears in muted gray (#7b7b7b). The search icon sits inside the input on the left.

### Badges
**`badge-inventory`** — A small green badge (#428445) with white uppercase text, used to indicate "In Stock" status on product cards. Uses 2px horizontal padding and 2px rounded corners.

**`badge-sale`** — A crimson badge (#c51c34) with white text, used to indicate sale pricing. Same dimensions as the inventory badge but uses the brand's primary color for urgency.

**`badge-new`** — A teal badge (#108474) with white text, used to indicate new arrivals. Provides a visual break from the crimson and green badges while maintaining the brand's accent palette.

### Footer
**`footer`** — A full-width footer with an ink-colored background (#222222) and white text. Links appear in a lighter gray (#c7c7c7) and use the Jost font family at 14px. The footer is divided into columns for customer service, company info, and social links, with a copyright line at the bottom.

### Hero
**`hero-section`** — A full-bleed section with a white background and large Barlow Condensed headline (48px). The hero typically features a single product image on one side and a headline with a primary CTA on the other. No decorative elements — just typography, photography, and the crimson button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product cards stack in single column; hero becomes stacked layout with image above text; search bar becomes full-width below nav; footer columns stack vertically |
| Tablet | 744–1128px | Nav links reduce to 4-5 items; product cards display in 2-column grid; hero uses 50/50 split layout; search bar remains in nav but collapses to icon on scroll |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero uses 60/40 split with image dominant; search bar expands on click to full-width overlay |
| Wide | > 1440px | Max-width container at 1440px with centered content; product cards in 4-column grid; hero maintains 60/40 split but with larger typography (56px display-xl) |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height
- Nav links have 48px touch area (padding + height)
- Product card "Add to Cart" button appears on tap for mobile (always visible)
- Search icon has 44x44px tap target
- Accordion headers have 48px touch area
- Cart icon has 44x44px tap target

### Collapsing Strategy
- Top nav collapses to hamburger menu at < 744px
- Product grid reduces columns: 4 → 3 → 2 → 1
- Footer columns stack: 4 columns → 2 columns → 1 column
- Hero section: side-by-side → stacked
- Search bar: inline → full-width overlay
- Category cards: horizontal scroll strip → vertical stack
- Product filters: sidebar → bottom sheet on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons could not be reliably extracted from the live site; the above uses a standard darken pattern
- Error states for form inputs (validation colors, error messages) were not visible in the extracted data
- The exact font weights for Jost (body text) could not be confirmed beyond 400 and 500; the site may use additional weights
- Dark mode is not implemented on the live site; no dark mode palette exists
- The Shopify checkout flow uses default Shopify button styles that differ from the brand's primary button (rounded corners, font family); this inconsistency is noted but not codified
- Sub-brand or collection-specific color palettes (e.g., limited edition leather colors) were not extracted
- The exact shadow values for product card hover states could not be determined from the extracted data
- Animation durations and easing curves were not extractable from static HTML/CSS analysis
- The "JudgemeStar" font declaration suggests a review widget, but its exact styling (size, color, spacing) could not be confirmed
- The meta theme-color of #000000 suggests a potential dark header or full-bleed section on some pages, but this was not consistently observed across the site
