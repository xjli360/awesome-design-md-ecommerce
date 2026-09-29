---
version: alpha
name: "Quality Arcades"
source_url: "https://www.qualityarcades.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A neon-lit, high-voltage brand that wraps arcade nostalgia in a custom-machine factory aesthetic, anchored on a deep-space ink (#040926) canvas that makes every accent — the electric blue (#006fcf), the arcade-pink (#ff00c9), the marquee-yellow (#ffba22), and the gamer-purple (#9528fa) — pop like a CRT screen in a dark room. The brand uses Bungee for display headlines, a retro-futuristic geometric font that feels like a 1980s arcade marquee, paired with Archivo Narrow for body text — a condensed sans-serif that packs information dense without sacrificing legibility. Buttons and badges use sharp, slightly rounded corners (`{rounded.sm}` ~8px) rather than pills, reinforcing the precision of a factory-built machine. The primary CTA blue (#006fcf) is the same blue used for the brand's "Customize" and "Add to Cart" actions, creating a consistent voltage across the purchase funnel. Product cards sit on white (`{colors.canvas}` #fdfdfd) with thin hairlines (`{colors.hairline}` #231f20), and every machine photo is presented full-bleed against that white — no shadows, no gradients, just the raw cabinet. The footer and navigation use the deep-space ink with white text, punctuated by accent bars in orange (#f48120) and pink (#ff00c9) that serve as section dividers and hover-state indicators. The overall effect is a brand that feels like a custom arcade cabinet itself: dark, glowing, precise, and built to order.

colors:
  primary: "#006fcf"
  primary-active: "#005bb5"
  primary-disabled: "#b3d9f5"
  ink: "#040926"
  body: "#231f20"
  muted: "#3086c8"
  muted-soft: "#6a6a6a"
  hairline: "#231f20"
  hairline-soft: "#d0d0d0"
  canvas: "#fdfdfd"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-pink: "#ff00c9"
  accent-yellow: "#ffba22"
  accent-orange: "#f48120"
  accent-purple: "#9528fa"
  accent-green: "#95ff0e"
  accent-red: "#ff0000"

typography:
  display-xl:
    fontFamily: "'Bungee', 'Archivo Narrow', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 1px
  display-lg:
    fontFamily: "'Bungee', 'Archivo Narrow', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.5px
  display-md:
    fontFamily: "'Bungee', 'Archivo Narrow', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.25px
  title-md:
    fontFamily: "'Archivo Narrow', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Archivo Narrow', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Archivo Narrow', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Archivo Narrow', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Archivo Narrow', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Archivo Narrow', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Archivo Narrow', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
  link:
    fontFamily: "'Archivo Narrow', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Archivo Narrow', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Archivo Narrow', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
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
    padding: 12px 24px
    height: 44px
  button-accent-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.accent-pink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  badge-new:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-custom:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-accent-bar:
    backgroundColor: "{colors.accent-orange}"
    height: 4px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  section-divider:
    backgroundColor: "{colors.accent-pink}"
    height: 2px
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Customize", "Add to Cart", and "Get Started". Rendered in electric blue (`{colors.primary}`) with white text and a subtle 8px corner radius (`{rounded.sm}`). On hover, shifts to a deeper blue (`{colors.primary-active}`). Disabled state uses a pale blue (`{colors.primary-disabled}`) with white text, signaling the action is unavailable.

**`button-secondary`** — An outlined or ghost-style button for secondary actions like "Learn More" or "View Details". Uses white background (`{colors.canvas}`) with dark ink text (`{colors.ink}`), maintaining the same 44px height and 8px corner radius as the primary button. Hover state adds a thin hairline border (`{colors.hairline}`).

**`button-accent-pink`** — A high-energy accent button reserved for limited-time offers, flash sales, or "Build Your Own" flows. Uses the arcade-pink (`{colors.accent-pink}`) as background with white text. Same dimensions as `button-primary`.

**`button-accent-yellow`** — A marquee-yellow button used for "Add to Cart" on sale items or for "Subscribe" CTAs. Yellow (`{colors.accent-yellow}`) background with dark ink text (`{colors.ink}`) for maximum contrast.

### Cards
**`product-card`** — The primary product display unit for arcade machines. A white card (`{colors.canvas}`) with a thin hairline border (`{colors.hairline}`) and 8px corner radius (`{rounded.sm}`). Contains a full-bleed product image, title in `title-sm`, and price in `body-md` colored with the primary blue. No shadow — the card relies on the hairline and whitespace for definition.

**`product-card-image`** — The image area within a product card, cropped to a 4:3 aspect ratio and rounded at the top corners (`{rounded.sm}`). Images are presented without overlays or gradients, showing the raw cabinet design.

### Badges
**`badge-new`** — A small, uppercase badge in arcade-pink (`{colors.accent-pink}`) with white text, used to flag newly released machines. 4px corner radius (`{rounded.xs}`) and tight padding (2px 8px) keep it unobtrusive.

**`badge-sale`** — A marquee-yellow badge (`{colors.accent-yellow}`) with dark ink text, used for discounted machines. Same dimensions as `badge-new`.

**`badge-custom`** — A purple badge (`{colors.accent-purple}`) with white text, used to indicate machines that are fully customizable. Same dimensions as `badge-new`.

### Navigation
**`nav-bar`** — The top navigation bar, fixed at 72px height, using the deep-space ink (`{colors.ink}`) background with white text. Contains the brand logo, navigation links, and a search icon. Links use `nav-link` typography with 8px 16px padding.

**`nav-link`** — Standard navigation link in white text on the dark nav bar. On hover or active state, text color shifts to arcade-pink (`{colors.accent-pink}`) to indicate the current section.

### Forms
**`text-input`** — Standard text input for search, contact forms, and customization fields. White background (`{colors.canvas}`) with dark body text (`{colors.body}`), 8px corner radius (`{rounded.sm}`), and 10px 16px padding. Focus state adds a 2px primary-blue border.

**`search-bar`** — The site search input, styled identically to `text-input` but with a magnifying glass icon on the left. Used in the nav bar and on the search results page.

### Footer
**`footer`** — The site footer, using the deep-space ink (`{colors.ink}`) background with white text. Contains columns for product categories, support links, and company information. Links use `footer-link` styling with muted blue (`{colors.muted}`) text.

**`footer-accent-bar`** — A 4px-high horizontal bar in orange (`{colors.accent-orange}`) that runs across the top of the footer, serving as a visual separator from the main content area.

### Hero
**`hero-section`** — The full-width hero banner on the homepage, using the deep-space ink (`{colors.ink}`) background with white text. Features a large headline in `display-xl` (Bungee), a subheading in `body-md`, and a primary CTA button (`hero-cta`). Background may include subtle geometric patterns or grid lines reminiscent of arcade cabinet art.

**`hero-cta`** — The primary call-to-action within the hero section. Slightly larger than `button-primary` (48px height, 14px 32px padding) to command attention. Uses the same electric blue (`{colors.primary}`) with white text and 8px corner radius.

### Filters
**`filter-tag`** — A filter chip used on collection pages to narrow down machines by category, price, or features. Light gray background (`{colors.surface-soft}`) with dark text, 8px corner radius, and 6px 12px padding. Active state (`filter-tag-active`) switches to primary blue background with white text.

### Dividers
**`section-divider`** — A 2px-high horizontal line in arcade-pink (`{colors.accent-pink}`) used to separate major sections on the page. Provides a consistent visual rhythm and a pop of brand color.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Navigation collapses to hamburger menu; product cards stack in single column; hero text reduces to `display-lg`; buttons become full-width; filter tags wrap to multiple rows |
| Tablet | 744–1128px | Navigation shows condensed links; product cards display in 2-column grid; hero retains `display-xl` but with reduced padding; filter tags show in a horizontal scrollable strip |
| Desktop | 1128–1440px | Full navigation with all links visible; product cards in 3-column grid; hero with maximum padding and full `display-xl`; filter tags in a static grid |
| Wide | > 1440px | Maximum content width of 1440px centered; product cards in 4-column grid; hero with extra whitespace on sides; all elements scale proportionally |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Navigation links have 48px touch target height (including padding)
- Filter tags have 36px minimum touch target height
- Search bar has 44px touch target height
- Product card images are tappable with no minimum size requirement (images scale responsively)

### Collapsing Strategy
- Navigation: On mobile, the full nav bar collapses to a hamburger menu icon; links appear in a full-screen overlay with the deep-space ink background
- Product grid: Collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer columns: On mobile, footer links collapse into an accordion-style layout with expandable sections
- Filter tags: On tablet and mobile, filter tags become a horizontally scrollable strip rather than a static grid
- Hero section: On mobile, hero padding reduces by 50% and the CTA button becomes full-width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs and filter tags could not be reliably extracted from the live site; placeholder values are based on common patterns
- Error styling for forms (validation messages, error borders) was not visible on the live site
- Dark mode preferences or alternate color schemes were not detected
- The extracted hex color list includes several orange variants (#f48120, #f58720, #f89f20, #f79a20, #f68d20, #f37521, #e16f27, #d4602c, #d05b2e) that may represent a single brand orange with different rendering contexts; the most saturated (#f48120) was chosen as the accent-orange token
- The extracted list also includes #ff0000 (red) and #95ff0e (green) which may be used for stock indicators or status badges but their exact usage could not be confirmed
- Font weights for Bungee and Archivo Narrow are assumed based on typical web usage; variable font weights may be available
- The brand's logo treatment and any custom iconography were not captured in the extraction
- Animation and transition durations (e.g., button hover, nav link color change) were not measurable from static CSS extraction
- Checkout flow styling (Shopify Pay, cart drawer) was not analyzed
