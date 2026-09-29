---
version: alpha
name: "BioLite"
source_url: "https://www.bioliteenergy.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A teal (#008fa1) voltage runs through every BioLite interface like the glow of a camp stove at dusk — the brand's primary is a cool, deep cyan that reads as both outdoor-ready and tech-forward, distinct from the olive-and-charcoal palette of legacy camping gear companies. That teal anchors CTAs, the site's sticky top bar, and product-badge accents, while a secondary red (#d02f2e) appears sparingly for sale markers and error states, creating a stoplight-like tension against the otherwise calm palette. The canvas is a warm off-white (#faf0e4) rather than pure white, suggesting paper, tent fabric, or the inside of a fire-starting bellows — a subtle but deliberate departure from the sterile ecommerce norm. Typography pairs Fraunces, a variable serif with soft, almost edible curves, for display headings, with Arimo, a clean neo-grotesk sans, for body and UI text; the contrast is less "heritage meets modern" and more "campfire storytelling meets instrument panel." Product cards use generous white space, a soft hairline (#dedede), and a single teal accent line on hover, while the footer collapses into a dense, link-heavy column grid that mirrors the brand's dual identity (outdoor gear + energy tech). The overall mood is capable but warm — a brand that trusts its product photography to sell the romance of the backcountry, and uses the interface to stay out of the way.

colors:
  primary: "#008fa1"
  primary-active: "#068491"
  primary-disabled: "#c9c5be"
  ink: "#050505"
  body: "#414141"
  muted: "#798c5e"
  muted-soft: "#c9c5be"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#faf0e4"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#d02f2e"
  accent-green: "#3c9342"
  accent-gold: "#a77a06"
  dark-teal: "#00343b"
  charcoal: "#1c1c1c"

typography:
  display-xl:
    fontFamily: "'Fraunces', 'EB Garamond', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Fraunces', 'EB Garamond', Georgia, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Fraunces', 'EB Garamond', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Fraunces', 'EB Garamond', Georgia, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Arimo', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Arimo', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Arimo', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Arimo', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Arimo', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Arimo', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Arimo', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Arimo', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Arimo', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
  section: 80px

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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px rgba(0,143,161,0.2)"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.dark-teal}"
    textColor: "{colors.on-primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-hover:
    boxShadow: "0 4px 20px rgba(0,0,0,0.08)"
    borderBottom: "3px solid {colors.primary}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
  footer-section:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.on-primary}"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
  accordion-body:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} 0 {spacing.lg} 0"
  icon-circle:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
  icon-circle-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand teal (#008fa1) with white uppercase text. On hover, it shifts to the slightly darker active state (#068491). The disabled state uses the muted-soft gray (#c9c5be) to clearly signal non-interactivity while maintaining the same 8px rounded corners and 44px height. Used for "Add to Cart," "Shop Now," and primary checkout flows.

**`button-secondary`** — A warm off-white (#faf0e4) button with dark text, used for secondary actions like "Learn More" or "View Details." On hover, the background shifts to the surface-soft gray (#f0f0f0). The outline variant (`button-outline`) uses a transparent background with a teal text color and a 1px solid border, ideal for ghost buttons in hero sections or on product detail pages.

**`button-sm`** — A compact uppercase button (13px, 600 weight) used for inline actions like "Compare" or "Quick Add." Maintains the same 8px rounding and uppercase treatment as the standard button but at a reduced 36px height with 10px 20px padding.

### Cards
**`product-card`** — A white card with 12px rounded corners and no internal padding (product photography fills the top, text content sits below). On hover, a subtle box shadow lifts the card and a 3px teal bottom border appears, creating a clear selection state without overwhelming the product image. The card uses body-sm (14px) for product names and caption (13px) for pricing. Badges overlay the top-left corner of the product image.

**`product-badge`** — Small uppercase labels (11px, 700 weight) with 4px rounded corners. Three variants exist: the standard teal badge for "Best Seller" or "Top Rated," a red badge (#d02f2e) for sale items, and a green badge (#3c9342) for new arrivals. Each badge uses white text and sits with 8px padding from the card edge.

### Navigation
**`nav-bar`** — A fixed 64px teal bar spanning the full viewport width. Navigation links are uppercase 14px text in white, with generous 24px spacing between items. The bar includes a centered logo mark and a right-aligned cart icon with a badge counter. On scroll, the background deepens to dark-teal (#00343b) for improved contrast against page content. The mobile variant collapses to a hamburger menu with a full-screen overlay drawer.

**`category-tag`** — Pill-shaped tags (9999px rounding) used for product category filtering. The default state uses a light gray background (#f0f0f0) with body-colored text. The active state fills with teal and white text. Tags sit in a horizontally scrollable strip above the product grid, with 8px gaps between each tag.

### Forms
**`text-input`** — A 48px tall input field with warm off-white background and 8px rounded corners. On focus, a 2px teal ring appears via box-shadow. The placeholder text uses the muted-soft gray (#c9c5be). Used for search, newsletter signup, and checkout forms. Error states would use the accent-red (#d02f2e) for border and helper text.

### Footer
**`footer-section`** — A dark charcoal (#1c1c1c) footer with white text, divided into four columns on desktop. Links use the muted-soft gray (#c9c5be) and shift to white on hover. The footer includes a newsletter signup form (using the text-input component with a white variant), social media icon links, and legal text in caption size. Section padding is 80px top/bottom with 32px horizontal.

### Hero
**`hero-section`** — Full-width section with warm off-white background, featuring a large Fraunces display headline (48px), a supporting body paragraph, and a single teal CTA button. The hero typically includes a full-bleed product or lifestyle photograph on the right side (desktop) or below the text (mobile). No carousel — BioLite trusts a single strong hero image.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero stacks text above image; footer collapses to single column; category tags become horizontally scrollable; product cards use full-width images |
| Tablet | 744–1128px | Two-column product grid; nav remains expanded but with reduced link spacing; hero uses 50/50 split; footer uses two columns; category tags wrap to two rows |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; hero uses 60/40 text-to-image split; footer uses four columns; product cards show 3-4 per row |
| Wide | > 1440px | Max-width container at 1440px with centered content; four-column product grid; hero text column max-width at 600px; all spacing scales proportionally |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height (exceeding Apple's 44pt HIG recommendation)
- Category tags are minimum 36px tall with 16px horizontal padding for easy tapping
- Product card tap targets (image, title, price, add-to-cart) are each minimum 48px tall
- Nav bar hamburger icon is 44x44px with 8px internal padding
- Accordion headers are 48px tall with full-width tap targets

### Collapsing Strategy
- Top nav collapses from horizontal links to hamburger menu at 744px breakpoint
- Product grid collapses from 3 columns to 2 at 744px, then to 1 at 480px
- Footer collapses from 4 columns to 2 at 744px, then to 1 at 480px
- Hero section stacks vertically below 744px, with text above image
- Category tag strip becomes horizontally scrollable below 744px, with scroll-snap alignment
- Product image galleries collapse from thumbnail grid to single-image swipe carousel below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components were inferred from common ecommerce patterns; the live site may use different transitions or micro-interactions
- Error state styling for form inputs (red borders, error message typography) was not extractable from the static HTML/CSS
- The extracted hex list includes several colors (#478947, #517f70, #3c9342) that may be Shopify checkout widget colors rather than brand colors; the green badge variant (#3c9342) was kept as a reasonable assumption
- Font weights for Fraunces and Arimo were estimated from common variable font usage; the live site may use different optical sizes or weight axes
- Dark mode styling was not present in the extracted data; all components assume light mode only
- The meta theme-color tag was absent, suggesting the browser chrome color may not be explicitly set
- Sub-brand or seasonal palette variations (e.g., BioLite Energy vs. BioLite Camping) could not be determined
- Animation durations, easing curves, and transition properties were not extractable
- The "warm off-white" canvas (#faf0e4) may be a Shopify theme default rather than an intentional brand choice; its usage frequency in the extracted data was moderate but distinctive enough to include
- Accessibility contrast ratios between the teal primary and white text, or between muted text and the off-white canvas, have not been verified against WCAG 2.1 AA standards
