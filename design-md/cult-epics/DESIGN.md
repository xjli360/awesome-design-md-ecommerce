---
version: alpha
name: "Cult Epics"
source_url: "https://www.cultepics.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A vault door painted in #ff0000 — that single, unapologetic red is the brand's handshake, appearing on the home-page hero banner, the "Shop" button, and the site's only persistent accent against a concrete-and-steel palette of #222222, #292e31, and #1e1e1e. The site feels like a midnight crawl through a video-store annex where the horror, cult, and exploitation sections never got the memo about streaming. Abril Fatface, a slab serif with the gravity of a film-title card, anchors display headlines at 28–36px, while the body runs in Open Sans at 14–16px — a deliberate tension between theatrical and utilitarian. The extracted color list is dominated by grays (#ced4d9, #777777, #aaaaaa, #d6d6d6, #e7e7e7, #e5e5e5, #e1e1e1, #d4d4d4, #ededed, #eaeaea) and blues (#0084b4, #0096ff, #009aee, #00a8ff, #a8d8ee), but the brand's true signature is the red #ff0000 and the gold #ffd658 that appears on badge-like elements and price highlights. The marigold #fecf72 and amber #f3a847 suggest sale or limited-edition callouts. A secondary green #8bc027 appears in stock-status indicators. The site uses pill-shaped buttons (`{rounded.full}`) for primary CTAs, while product cards use a softer `{rounded.sm}`. The nav bar is a dark slab (#222222) with white text, and the footer drops into near-black (#1e1e1e). This is a brand that trusts high-contrast typography and color-blocking over photography — the red and gold do the emotional work.

colors:
  primary: "#ff0000"
  primary-active: "#cc0000"
  primary-disabled: "#ff6666"
  ink: "#222222"
  body: "#292e31"
  muted: "#777777"
  muted-soft: "#aaaaaa"
  hairline: "#d6d6d6"
  hairline-soft: "#e7e7e7"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#ffd658"
  accent-marigold: "#fecf72"
  accent-amber: "#f3a847"
  accent-green: "#8bc027"
  badge-red: "#ff0000"
  badge-gold: "#ffd658"
  dark-bg: "#1e1e1e"
  nav-bg: "#222222"
  footer-bg: "#1e1e1e"
  link-blue: "#0084b4"
  link-blue-hover: "#009aee"

typography:
  display-xl:
    fontFamily: "'Abril Fatface', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-lg:
    fontFamily: "'Abril Fatface', Georgia, serif"
    fontSize: 30px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'Abril Fatface', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Abril Fatface', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.ink}"
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 60px
    padding: "0 {spacing.xl}"
  nav-link-item:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-item-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "3/4"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    fontWeight: 700
  product-card-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-gold:
    backgroundColor: "{colors.badge-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-accent:
    color: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
    typography: "{typography.link}"
  badge-stock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "6px 16px"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in full red (#ff0000) with white text and a pill shape (`{rounded.full}`). On hover, it shifts to `{colors.primary-active}` (#cc0000). The disabled state uses `{colors.primary-disabled}` (#ff6666). Used for "Add to Cart", "Shop Now", and primary checkout flows. **`button-secondary`** — An outlined variant with a 2px solid `{colors.ink}` border on a white background. Active state fills the background with `{colors.surface-soft}`. Used for "Learn More" or secondary product actions. **`button-gold`** — A warm accent button using `{colors.accent-gold}` (#ffd658) with dark ink text, reserved for limited-edition drops, pre-orders, or VIP callouts. **`button-ghost`** — Transparent background with `{colors.ink}` text, used for tertiary actions like "Cancel" or "View Details" in card overlays.

### Navigation
**`nav-bar`** — A fixed-height 60px dark bar (`{colors.nav-bg}` #222222) spanning full viewport width. Navigation links use `{typography.nav-link}` (Open Sans, 14px, 600 weight, 0.5px letter spacing, uppercase) in white. The active link switches to `{colors.primary}` red. The bar contains the brand logo (typically set in Abril Fatface at 22px), a search icon, and a cart icon. On mobile, the nav collapses into a hamburger menu. **`nav-link-item`** — Individual navigation links with 8px horizontal padding. Active state uses `{colors.primary}` text color to indicate the current page.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with `{rounded.sm}` (8px) corners and 16px padding. The product image occupies a 3:4 aspect ratio with `{rounded.xs}` (4px) corners. The title sits below in `{typography.title-sm}` (Open Sans, 16px, 600 weight), followed by the price in `{typography.body-md}` at 700 weight. Badges overlay the top-left of the image: `{colors.badge-red}` for "New" or "Exclusive", `{colors.badge-gold}` for "Limited Edition". A stock badge (`{colors.accent-green}`) appears when inventory is available. Cards have a subtle shadow on hover (not tokenized here due to extraction limits).

### Forms
**`text-input`** — Standard text input with white background, 1px `{colors.hairline}` border, and `{rounded.sm}` (8px) corners. On focus, the border thickens to 2px and turns `{colors.primary}` red. Error state uses a 2px `{colors.primary}` border with red text for the error message (not tokenized). Height is 44px with 10px vertical and 16px horizontal padding. **`search-bar`** — A pill-shaped (`{rounded.full}`) search input with a 1px `{colors.hairline}` border. On focus, the border becomes 2px `{colors.primary}`. Used in the nav bar and on the home page hero.

### Hero
**`hero-banner`** — A full-width section with `{colors.dark-bg}` (#1e1e1e) background and white text, using `{typography.display-xl}` (Abril Fatface, 36px). The primary accent color (`{colors.primary}`) is used for highlighted words or CTAs within the hero. Padding is 64px vertical and 32px horizontal. On mobile, the hero reduces to 48px vertical padding and the font drops to `{typography.display-md}` (24px).

### Badges
**`product-card-badge`** — Small uppercase labels (11px, 700 weight, 0.3px letter spacing) with `{rounded.xs}` (4px) corners and 2px/8px padding. Red background (`{colors.badge-red}`) for new/exclusive items, gold (`{colors.badge-gold}`) for limited editions, and green (`{colors.accent-green}`) for stock indicators. **`badge-sale`** — A red badge specifically for sale/discount callouts, using the same typography and corner radius.

### Category Tags
**`category-tag`** — Pill-shaped (`{rounded.full}`) tags with `{colors.surface-soft}` background and `{colors.muted}` text, used for filtering product categories (e.g., "Horror", "Cult", "Exploitation"). Active state uses `{colors.primary}` background with white text. Padding is 6px vertical, 16px horizontal.

### Footer
**`footer`** — A full-width dark section (`{colors.footer-bg}` #1e1e1e) with `{colors.muted-soft}` (#aaaaaa) text in `{typography.body-sm}` (Open Sans, 14px). Links use `{typography.link}` and transition to white on hover. Padding is 48px vertical and 32px horizontal. The footer contains columns for "About", "Customer Service", "Newsletter Signup", and social links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; hero font drops to `{typography.display-md}` (24px); product cards stack single-column; footer columns stack vertically; hero padding reduces to 48px vertical; search bar moves to full-width below nav |
| Tablet | 744–1128px | Nav remains horizontal but with reduced padding; product cards display in 2-column grid; hero font uses `{typography.display-lg}` (30px); footer columns display in 2x2 grid |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero at full `{typography.display-xl}` (36px); footer in 4-column layout |
| Wide | > 1440px | Max-width container (1440px) centered; product cards may expand to 4-column grid; hero remains full-width with max-width content area |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height to meet WCAG touch-target guidelines.
- Nav links have 8px horizontal padding, but the full 60px nav bar height ensures adequate tap area.
- Category tags and badges are at least 32px tall with 6px vertical padding.
- Search bar and text inputs are 44px tall.
- Product card CTAs (e.g., "Add to Cart") use `{typography.button-sm}` (14px) with 44px height.

### Collapsing Strategy
- **Mobile (< 744px):** The top nav collapses into a hamburger menu; the search bar moves below the nav as a full-width element; product cards collapse from multi-column to single-column; the hero banner reduces font size and padding; the footer collapses from 4 columns to a single vertical stack.
- **Tablet (744–1128px):** The nav remains expanded but with tighter padding; product cards collapse to 2 columns; the hero font reduces to `{typography.display-lg}`; the footer collapses to a 2x2 grid.
- **Desktop (1128–1440px):** All elements display at full width; the nav is fully expanded; product cards display in 3 columns.
- **Wide (> 1440px):** The main content area is constrained to a 1440px max-width container; the nav and footer remain full-width; product cards may expand to 4 columns.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states:** While `{colors.primary-active}` (#cc0000) is inferred for button hover, exact hover colors for links, secondary buttons, and ghost buttons were not extracted from the live site. The `link-blue-hover` (#009aee) is an educated guess based on the extracted blues.
- **Focus states:** No focus-ring styles (outline, box-shadow) were extracted. Accessibility focus indicators are assumed but not confirmed.
- **Error states:** Text-input error styling (border color, error message typography) is inferred from the primary red; no extracted data confirms this.
- **Dark mode:** The site uses a dark nav and footer, but no system-preference dark mode was detected. The `{colors.dark-bg}` (#1e1e1e) is used for hero and footer only.
- **Shadow tokens:** No box-shadow values were extracted. Product cards likely have a subtle shadow on hover, but the exact values are unknown.
- **Sub-brand palettes:** The extracted colors include multiple blues (#0084b4, #0096ff, #009aee, #00a8ff, #a8d8ee) that may belong to third-party widgets (social icons, payment badges) rather than the brand itself. The `{colors.link-blue}` (#0084b4) is a best guess for link color.
- **Font weights:** Abril Fatface only comes in 400 weight; Open Sans weights (400, 600, 700) are inferred from common usage. Exact weights for body, title, and button text were not extracted.
- **Line heights and letter spacing:** These values are estimated based on standard web typography best practices; the extracted CSS did not include these properties.
- **Animation/transition:** No transition durations or easing functions were extracted. Button hover transitions are assumed but not confirmed.
- **Grid system:** The responsive breakpoints and column counts are inferred from common patterns; the exact grid system (e.g., 12-column, 8-column) was not extracted.
- **Iconography:** No icon set or SVG data was extracted. The nav likely uses a search icon and cart icon, but their exact style is unknown.
- **Checkout flow:** The extracted colors include several blues and grays that may belong to Shopify Pay, Klarna, or Afterpay widgets. These are not part of the brand's design system.
