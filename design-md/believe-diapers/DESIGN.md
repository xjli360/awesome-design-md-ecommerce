---
version: alpha
name: "Believe Diapers"
source_url: "https://believediapers.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A baby-care brand that stakes its entire visual identity on a single, unexpected typographic choice: Kopius, a serif typeface with generous ball terminals and a warm, slightly condensed posture, set as `!important` across the site — a deliberate rebellion against the sans-serif orthodoxy of modern DTC. The palette orbits around a deep, warm charcoal (`#3d3935`) as ink, with a muted stone (`#645f59`) and a cool, trustworthy blue (`#6383ac`) that appears in secondary accents and link treatments. The canvas is pure white (`#ffffff`), and the brand's primary voltage is a vivid, almost electric blue (`#0075fe`) — a color that reads as both medical-grade reliability and digital-native confidence, used sparingly on CTAs and interactive elements. Generous whitespace and a restrained use of `{rounded.sm}` (8px) on buttons and cards keep the interface soft without sacrificing clarity. The site's `{colors.hairline}` (`#dbdbdb`) delineates sections with a light touch, while `{colors.surface-soft}` (`#f4f9ff`) — a barely-there blue tint — backs subscription cards and trust badges, reinforcing the brand's association with purity and care. The typographic system pairs Kopius for display and headline work with Jost, a geometric sans-serif, for body copy and navigation, creating a rhythm that feels editorial without being precious. Product imagery dominates: diapers photographed on clean backgrounds, with bamboo-leaf motifs and soft greens (`#04af53`) appearing only in environmental cues (leaf icons, sustainability callouts). The brand's voice is direct and reassuring — "Premium Bamboo Baby Diapers & Wipes" — and the design system mirrors that: no decorative flourishes, no heavy shadows, just clear information architecture and a quiet confidence that the product speaks for itself.

colors:
  primary: "#0075fe"
  primary-active: "#0275ff"
  primary-disabled: "#b5b5b5"
  ink: "#3d3935"
  body: "#645f59"
  muted: "#7a7a7a"
  muted-soft: "#888888"
  hairline: "#dbdbdb"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f4f9ff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#6383ac"
  accent-green: "#04af53"
  accent-red: "#ff5268"
  star-rating: "#f14336"
  badge-new: "#02c316"

typography:
  display-xl:
    fontFamily: "'Kopius', 'Georgia', 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Kopius', 'Georgia', 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Kopius', 'Georgia', 'Times New Roman', serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Jost', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Jost', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Jost', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Jost', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Jost', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Jost', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Jost', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Jost', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Jost', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px

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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
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
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    checkedBackground: "{colors.primary}"
    checkedBorder: "{colors.primary}"
  radio:
    border: "2px solid {colors.hairline}"
    checkedBorder: "{colors.primary}"
    checkedDot: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.accent-blue}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(61,57,53,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 600
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
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
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    maxWidth: 600px
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 56px
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(61,57,53,0.06)"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0,117,254,0.15)"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  subscription-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  subscription-card-featured:
    border: "2px solid {colors.primary}"
    boxShadow: "0 4px 16px rgba(0,117,254,0.12)"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Subscribe Now", "Add to Cart", and "Get Started". Rendered in `{colors.primary}` (#0075fe) with white text and `{rounded.sm}` corners. On hover, shifts to `{colors.primary-active}` (#0275ff). Disabled state uses `{colors.primary-disabled}` (#b5b5b5) with white text. Height is 48px with 14px vertical and 28px horizontal padding.

**`button-secondary`** — An outlined alternative for less prominent actions like "Learn More" or "View Details". White background with `{colors.ink}` text and a 2px `{colors.hairline}` border. Active state darkens the border to `{colors.ink}` and adds `{colors.surface-soft}` background.

**`button-ghost`** — A text-only button for inline actions like "See all" or "Read reviews". Uses `{colors.accent-blue}` (#6383ac) for a softer, less aggressive call-to-action than the primary blue.

**`button-pill`** — A fully rounded variant (`{rounded.full}`) used for promotional badges or "Shop Now" CTAs in hero sections. Same `{colors.primary}` background but with tighter padding (10px 24px) and `{typography.button-sm}`.

### Cards
**`product-card`** — The standard product display card, used on collection pages and subscription flows. White background with a 1px `{colors.hairline-soft}` border and `{rounded.sm}` corners. On hover, the border thickens to `{colors.hairline}` and a subtle shadow appears. The image container uses a 1:1 aspect ratio with `{rounded.sm}`. Title uses `{typography.title-sm}` with `{spacing.sm}` margin above the price, which is set in `{typography.body-md}` at weight 600.

**`subscription-card`** — A larger card for subscription plan selection, with `{spacing.lg}` padding and a `{colors.hairline}` border. The featured variant (e.g., "Most Popular") gets a 2px `{colors.primary}` border and a blue-tinted shadow for emphasis.

**`trust-badge`** — Small informational badges for "Free Shipping", "30-Day Trial", or "Bamboo Certified". Uses `{colors.surface-soft}` background with `{colors.body}` text in `{typography.caption}`, `{rounded.sm}`, and `{spacing.sm}` vertical / `{spacing.base}` horizontal padding.

### Navigation
**`nav-bar`** — The top navigation bar, 72px tall with white background and `{colors.ink}` text in `{typography.nav-link}`. A 1px `{colors.hairline-soft}` bottom border separates it from the page content. Active nav links get `{colors.primary}` text color and a 2px bottom border in the same blue. Hover state shifts to `{colors.accent-blue}`.

**`footer-section`** — The site footer, inverted on `{colors.ink}` (#3d3935) with white text. Links use `{colors.muted-soft}` (#888888) and lighten to white on hover. Padding is `{spacing.xxl}` vertical and `{spacing.lg}` horizontal.

### Forms
**`text-input`** — Standard text input for email, name, and address fields. White background, `{colors.ink}` text, `{rounded.sm}`, and a 1px `{colors.hairline}` border. Focus state doubles the border to 2px and switches to `{colors.primary}`. Error state uses a 2px `{colors.accent-red}` border.

**`select-dropdown`** — Matches the text input styling for consistency in subscription and checkout forms.

**`checkbox`** — A 2px `{colors.hairline}` border with `{rounded.xs}` corners. Checked state fills with `{colors.primary}` background and border.

**`radio`** — Circular with a 2px `{colors.hairline}` border. Checked state shows a `{colors.primary}` outer border and a `{colors.primary}` inner dot.

### Search
**`search-bar`** — A pill-shaped search bar (`{rounded.full}`) used on the hero and collection pages. White background, 56px height, 12px 24px padding, and a 1px `{colors.hairline}` border with a subtle shadow. Focus state gains a 2px `{colors.primary}` border and a blue-tinted shadow.

### Badges
**`badge-new`** — A green (`#02c316`) pill badge for "New Arrivals" or "Just In". Uses `{typography.badge}` (11px, uppercase, weight 700) with 4px 10px padding.

**`badge-sale`** — A red (`#ff5268`) pill badge for sale items.

**`badge-eco`** — A green (`#04af53`) pill badge for "Bamboo" or "Eco-Friendly" labels.

### Other
**`hero-section`** — The page hero, backed by `{colors.surface-soft}` (#f4f9ff) with `{spacing.section}` vertical padding. Heading uses `{typography.display-xl}` (42px Kopius) with a 600px max-width. Subheading in `{typography.body-md}` with `{colors.body}`.

**`accordion`** — Collapsible sections for FAQs and product details. Each item has a `{colors.hairline-soft}` bottom border. The header uses `{typography.title-sm}` and the content area uses `{typography.body-md}` with `{colors.body}` text and `{spacing.base}` vertical padding.

**`rating-stars`** — Star rating display, rendered in `{colors.star-rating}` (#f14336) at 16px per star.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero heading reduces to `{typography.display-lg}` (32px); subscription cards stack vertically; search bar reduces to icon-only |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but reduced font size; hero uses `{typography.display-lg}`; subscription cards display in 2-column grid |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full `{typography.display-xl}`; subscription cards in 3-column grid |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can expand to 4 columns; hero content max-width increases to 800px |

### Touch Targets
- All interactive elements (buttons, inputs, links) maintain a minimum 44px height for touch accessibility.
- Nav links have 48px touch area (72px bar height ensures comfortable tap targets).
- Product cards have 16px padding ensuring tap targets around CTAs are at least 44px.
- Search bar is 56px tall for easy thumb access on mobile.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer.
- The product grid collapses from 3 columns (desktop) to 2 (tablet) to 1 (mobile).
- The hero section reduces vertical padding from `{spacing.section}` to `{spacing.xxl}` on mobile.
- Subscription plan cards stack vertically on mobile instead of the 3-column desktop layout.
- The footer collapses from a 4-column link grid to a single-column accordion on mobile.
- Search transforms from a full text input to an icon-triggered overlay on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: While button and card hover states are inferred from common patterns, the exact color values for `button-secondary-hover` and `nav-link-hover` were not extractable from the static CSS. The `{colors.accent-blue}` (#6383ac) is an educated guess based on its presence as a secondary accent.
- **Error and validation styling**: Error text colors, border colors for error states, and success messages were not observed. The `{colors.accent-red}` (#ff5268) is used for error borders based on its presence in the extracted palette, but exact usage is unconfirmed.
- **Focus ring styles**: The `:focus-visible` outline color and width for keyboard navigation were not extractable. A 2px `{colors.primary}` outline is assumed.
- **Dark mode**: No dark mode implementation was detected. The brand currently operates exclusively in light mode.
- **Typography scale**: Font sizes for `display-xl` through `caption` are inferred from common DTC patterns and the relative hierarchy of the site. Exact pixel values for each level were not extractable from the compiled CSS. Kopius appears to be used for display/headline work (set as `!important`), while Jost handles body and UI text.
- **Spacing scale**: The spacing tokens follow a standard 4px/8px grid, but exact values for `section` and `xxl` are estimated based on common e-commerce patterns.
- **Rounded corner values**: `{rounded.sm}` (8px) is confirmed from button and card styles. Other values in the scale are standard increments.
- **Sub-brand or seasonal palettes**: No evidence of holiday, limited-edition, or collaboration-specific color variations.
- **Checkout-specific styling**: Shopify's default checkout theme may override some form and button styles. The tokens above represent the brand's own site, not the checkout flow.
- **Animation and transition timing**: Transition durations and easing curves were not extractable. A standard 200ms ease-in-out is assumed for hover/focus states.
- **The extracted color list is heavily polluted with Shopify widget colors (Klarna pink `#ff5268`, Afterpay blue `#0300fe`, social media brand colors) and generic framework grays. The true brand palette is narrower: `#3d3935` (ink), `#645f59` (body), `#6383ac` (accent blue), `#0075fe` (primary), `#f4f9ff` (surface soft), and `#ffffff` (canvas). The remaining colors in the extraction are either checkout widgets, social icons, or stock image dominant tones.
