---
version: alpha
name: "Mrs. Meyer's"
source_url: "https://mrsmeyers.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A garden-apron palette anchored on #3f2021 (a deep, soil-rich brown) that runs through every product label, navigation bar, and footer — not as an accent but as the brand's steady, grounded presence. The secondary voice is #a6192e (a dried-rose red) that appears on sale badges, limited-edition banners, and the signature "M" mark, while #f3e008 (marigold yellow) and #22c55e (stem green) surface on seasonal labels and ingredient callouts. The site uses Clarendon BT W05 Roman at display sizes — a serif with the weight of a garden trowel — paired with NewsGoth BT for body copy, creating a farmstand-meets-utility-company contrast. Product cards sit on #fafafa canvas with {rounded.sm} corners and a single #e5e5e5 hairline, letting the label photography (each scent rendered as a watercolor botanical) carry the emotional weight. The top nav is a full-width #3f2021 band with white Clarendon text, and the search bar is a pill-shaped field with #d3d3d3 border that expands on focus to reveal a #f0f9ff background. Buttons are solid #3f2021 rectangles with {rounded.xs} corners and white NewsGoth — no gradients, no shadows, just the directness of a clean kitchen counter. The checkout flow introduces #1878b9 (a bright, unexpected blue) on the "Add to Cart" confirmation, a small jolt of clarity in an otherwise warm, earth-toned system.

colors:
  primary: "#3f2021"
  primary-active: "#630000"
  primary-disabled: "#a4a7a9"
  ink: "#1f2937"
  body: "#455560"
  muted: "#757575"
  muted-soft: "#949494"
  hairline: "#d3d3d3"
  hairline-soft: "#e5e5e5"
  canvas: "#fafafa"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-rose: "#a6192e"
  accent-marigold: "#f3e008"
  accent-stem: "#22c55e"
  accent-sky: "#38bdf8"
  accent-coral: "#ee907b"
  accent-blue: "#1878b9"
  sale-red: "#e22120"
  rating-star: "#f59e0b"
  error: "#fc0000"
  success: "#0b4320"
  warning: "#634004"
  info: "#056792"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Clarendon BT W05 Roman', 'Clarendon Pro', Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Clarendon BT W05 Roman', 'Clarendon Pro', Georgia, serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Clarendon BT W05 Roman', 'Clarendon Pro', Georgia, serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Clarendon BT W05 Roman', 'Clarendon Pro', Georgia, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'NewsGoth BT', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'NewsGoth BT', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.15px
  body-md:
    fontFamily: "'NewsGoth BT', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'NewsGoth BT', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'NewsGoth BT', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'NewsGoth BT', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.1px
  badge:
    fontFamily: "'NewsGoth BT', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'NewsGoth BT', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'NewsGoth BT', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'NewsGoth BT', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  link:
    fontFamily: "'NewsGoth BT', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Clarendon BT W05 Roman', 'Clarendon Pro', Georgia, serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'NewsGoth BT', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "'NewsGoth BT', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
    color: "{colors.sale-red}"

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
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
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
    padding: 11px 27px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-accent:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.on-primary}"
    padding: 8px 16px
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  search-bar-pill-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-sale-badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-rating:
    typography: "{typography.caption}"
    color: "{colors.rating-star}"
    marginTop: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    padding: "{spacing.xs} 0"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.accent-marigold}"
    typography: "{typography.link}"
    padding: "{spacing.xs} 0"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-image:
    rounded: "{rounded.sm}"
  section-header:
    typography: "{typography.display-md}"
    marginBottom: "{spacing.lg}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.md}"
    rounded: "{rounded.xs}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.md}"
  badge-new:
    backgroundColor: "{colors.accent-stem}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    height: 40px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 40px
  checkout-button:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a solid #3f2021 rectangle with {rounded.xs} corners and white NewsGoth BT text. On hover, it deepens to #630000. The disabled state uses #a4a7a9, a muted gray that signals unavailability without visual noise. Used for "Add to Cart", "Subscribe", and "Shop Now" actions.

**`button-secondary`** — An outlined variant with a white background and #3f2021 text, maintaining the same {rounded.xs} corners and 44px height. The active state shifts to #630000 text on #f7f7f7 background. Used for "Learn More" and "View Details" links where the primary button would overwhelm.

**`button-tertiary-text`** — A text-only button with no background or border, using #3f2021 NewsGoth BT at button-md size. Used for "Cancel", "Clear Filters", and inline navigation within product lists.

**`button-pill-accent`** — A fully rounded pill in #a6192e (accent-rose) with white text, used sparingly for limited-edition launches, seasonal collections, and "New Arrivals" badges that need to pop against the earthy palette.

### Text Inputs
**`text-input`** — A standard form field with #fafafa background, #1f2937 text, and a #d3d3d3 border. On focus, the background shifts to #f7f7f7 and the border remains #d3d3d3, keeping the interaction subtle. Used for email signups, search queries, and checkout forms.

**`text-input-focus`** — The focused state of the text input, with a slightly lighter background (#f7f7f7) and the same border color. No outline or glow — the brand avoids visual clutter.

### Navigation
**`nav-bar`** — A full-width #3f2021 band at 72px height, containing the logo (Clarendon BT W05 Roman in white) and navigation links. On scroll, it compresses to 64px with a slightly darker #630000 background. The bar is fixed at the top of the viewport.

**`nav-link`** — Uppercase Clarendon BT W05 Roman at 15px with 0.5px letter spacing, white text on the dark nav bar. The active state adds a 2px white underline. Hover state is a subtle opacity shift.

**`search-bar-pill`** — A pill-shaped input field with white background, #d3d3d3 border, and placeholder text in #757575. On focus, the background shifts to #f7f7f7 and the placeholder disappears. The pill shape is the only fully rounded element in the system, making it feel approachable.

### Product Cards
**`product-card`** — A white card with {rounded.sm} corners, 12px padding, and a 1:1 aspect ratio product image. The title uses title-sm (16px NewsGoth BT, weight 600), price uses price (18px weight 700), and rating uses caption (13px) in #f59e0b. On hover, a subtle box-shadow appears (0 2px 8px rgba(0,0,0,0.08)).

**`product-card-sale-badge`** — A small #e22120 badge with white text in badge typography (11px uppercase, weight 700), positioned at the top-left of the product image. Uses {rounded.xs} corners and 2px 8px padding.

**`product-card-rating`** — Star ratings displayed in #f59e0b (marigold yellow) using caption typography. Positioned below the price with 4px top margin.

### Footer
**`footer`** — A #3f2021 band with white text, using body-sm typography (14px NewsGoth BT). Links are white with 8px vertical padding, and hover to #f3e008 (accent-marigold). The footer contains three columns: "Shop" (product categories), "Learn" (about, ingredients, blog), and "Support" (FAQ, contact, shipping).

**`footer-link`** — White text links with 4px vertical padding. On hover, the text shifts to #f3e008, creating a warm highlight against the dark background.

### Badges
**`badge-new`** — A #22c55e (stem green) badge for new product arrivals, using badge typography (11px uppercase, weight 700) with white text and {rounded.xs} corners.

**`badge-limited`** — A #a6192e (accent-rose) badge for limited-edition or seasonal products, same typography and corner radius.

**`badge-sale`** — A #e22120 (sale-red) badge for discounted items, using the same badge pattern. The red is the most saturated color in the system, reserved exclusively for price reductions.

### Accordion
**`accordion-header`** — A clickable header with white background, #1f2937 text in title-sm (18px NewsGoth BT, weight 700), and 16px 12px padding. Uses {rounded.xs} corners. Used for FAQ sections and product details.

**`accordion-content`** — The expanded content area, with white background, #455560 body text in body-sm (14px), and 12px 12px padding. No border — relies on the header's visual weight for hierarchy.

### Checkout
**`checkout-button`** — A #1878b9 (accent-blue) button with white text, {rounded.sm} corners, and 14px 32px padding at 48px height. This is the only blue element in the system, used exclusively for the checkout flow to signal a transition from browsing to purchasing. The blue is a deliberate departure from the earthy palette, creating a clear visual cue that the user has entered a transactional context.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in 2-column grid; hero banner reduces to 32px display text; footer stacks to single column; search bar becomes full-width below nav |
| Tablet | 744–1128px | Nav bar shows 4 primary links; product cards in 3-column grid; hero banner uses 36px display text; footer shows 2 columns; search bar is 50% width |
| Desktop | 1128–1440px | Full nav bar with all links; product cards in 4-column grid; hero banner at 42px display text; footer shows 3 columns; search bar is 360px fixed width |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid with larger images; hero banner expands to full bleed with 48px display text; footer shows 4 columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets (title, price, image) are each at least 48px tall
- Nav bar hamburger icon is 44x44px with 8px padding
- Quantity selector buttons are 40x40px with 12px internal padding
- Accordion headers are 48px minimum height for easy tapping
- Footer links have 44px minimum touch area (8px vertical padding + 28px text height)

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with a slide-in drawer from the left
- Product grid reduces from 4 columns to 2 columns on mobile, then to single column below 480px
- Footer columns collapse from 4 to 2 at tablet, then to single column on mobile
- Hero banner text reduces from 42px to 32px on mobile, with image stacking below text
- Search bar becomes full-width below 744px, positioned below the nav bar
- Accordion content collapses by default on all breakpoints, expanding on click
- Product card sale badges and limited badges remain visible on all breakpoints, but reduce font size to 10px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components are inferred from common patterns; the live site may use different transitions or opacity values
- Error states for form inputs (validation, required fields) were not extractable from the provided data
- Dark mode is not supported by the brand; no dark palette tokens are defined
- Sub-brand palettes (e.g., seasonal collections, limited-edition scents) may use additional colors not present in the extracted list
- The extracted font list includes multiple fallback stacks; the exact font-weight mappings for Clarendon BT and NewsGoth BT are inferred from common web usage
- Animation durations and easing curves were not extractable; the brand likely uses simple 0.2s ease transitions
- The checkout flow's accent blue (#1878b9) is an assumption based on the extracted color list; its exact usage context (button vs. link vs. background) is inferred
- Social media icon colors (Instagram, Facebook, Pinterest) were filtered from the extracted list; the brand may use custom icon colors
- The meta theme-color tag was not present in the extracted hints; the brand may not use a browser chrome color
- Shopify platform defaults (e.g., checkout button styles, cart drawer) may override some design tokens; the extracted colors include Shopify Pay and Afterpay widget colors that were filtered out
