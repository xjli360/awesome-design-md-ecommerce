---
version: alpha
name: "Turtle Beach"
source_url: "https://www.turtlebeach.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dark, aggressive gaming-hardware brand that lives in the black of #121212 and the electric purple of #7538ff — the primary voltage that fires every CTA, badge, and category highlight. The brand's visual system is built on high-contrast layers: a near-black canvas (#121212), a slightly lifted surface (#1a1f26), and a mid-tone card surface (#232a34) that creates depth without relying on shadows. The purple (#7538ff) is the single brand signal, appearing on primary buttons, active navigation states, and promotional accents, with a hover state that deepens to #660bfd. Secondary accents of hot pink (#f83b78) and cyan (#4dfce0) appear on limited-edition products and sale badges, while the typography system relies on a proprietary Turtle Beach SW family in multiple weights — Light, Medium, and Bold — with Noto Sans as the primary fallback. Buttons are sharply rectangular with {rounded.sm} corners, never pill-shaped, communicating precision and readiness. The nav bar is a full-width dark band (#121212) with white text and a sticky search icon, while product cards use a subtle {rounded.md} radius on a #232a34 surface with white body text (#e6e8ef) and muted secondary copy (#919db1). The brand's voice is direct and competitive — "Hear Everything. Defeat Everyone." — and the design system follows suit: no decorative flourishes, no soft gradients, just high-contrast blocks of color, bold typography, and a relentless focus on gaming performance.

colors:
  primary: "#7538ff"
  primary-active: "#660bfd"
  primary-disabled: "#919db1"
  ink: "#121212"
  body: "#e6e8ef"
  muted: "#919db1"
  muted-soft: "#606978"
  hairline: "#363c46"
  hairline-soft: "#232a34"
  canvas: "#121212"
  surface-soft: "#1a1f26"
  surface-card: "#232a34"
  on-primary: "#ffffff"
  accent-pink: "#f83b78"
  accent-pink-active: "#ef2d6c"
  accent-cyan: "#4dfce0"
  accent-orange: "#ffa020"
  badge-green: "#31d77e"
  badge-red: "#fe353d"
  badge-pink: "#cc0869"
  star-rating: "#ffa020"

typography:
  display-xl:
    fontFamily: "'Turtle Beach SW Bold', 'Turtle Beach SW Bold Fallback', 'Noto Sans', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Turtle Beach SW Bold', 'Turtle Beach SW Bold Fallback', 'Noto Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Turtle Beach SW Medium', 'Turtle Beach SW Medium Fallback', 'Noto Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "'Turtle Beach SW Bold', 'Turtle Beach SW Bold Fallback', 'Noto Sans', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Turtle Beach SW Medium', 'Turtle Beach SW Medium Fallback', 'Noto Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Turtle Beach SW Bold', 'Turtle Beach SW Bold Fallback', 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.25px
  body-md:
    fontFamily: "'Turtle Beach SW', 'Turtle Beach SW Fallback', 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Turtle Beach SW', 'Turtle Beach SW Fallback', 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Turtle Beach SW Medium', 'Turtle Beach SW Medium Fallback', 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Turtle Beach SW Bold', 'Turtle Beach SW Bold Fallback', 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Turtle Beach SW Bold', 'Turtle Beach SW Bold Fallback', 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Turtle Beach SW Bold', 'Turtle Beach SW Bold Fallback', 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.75px
    textTransform: uppercase
  link:
    fontFamily: "'Turtle Beach SW Medium', 'Turtle Beach SW Medium Fallback', 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Turtle Beach SW Medium', 'Turtle Beach SW Medium Fallback', 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Turtle Beach SW Bold', 'Turtle Beach SW Bold Fallback', 'Noto Sans', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Turtle Beach SW Bold', 'Turtle Beach SW Bold Fallback', 'Noto Sans', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pink-active:
    backgroundColor: "{colors.accent-pink-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline}"
  nav-link-active:
    color: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.body}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.body}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    color: "{colors.accent-pink}"
  product-card-badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.display-xl}"
    height: 600px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-icon:
    color: "{colors.muted}"
    size: 20px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    border-top: "1px solid {colors.hairline}"
  footer-link:
    color: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.body}"
  category-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 48px
  category-nav-active:
    color: "{colors.primary}"
    border-bottom: "2px solid {colors.primary}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's signature purple (#7538ff) with white text and 4px corner radius. On hover, the background deepens to #660bfd. The disabled state drops to #919db1, a muted gray that signals inactivity without visual noise. All buttons use uppercase bold typography at 14px with 1px letter-spacing for a sharp, authoritative read.

**`button-secondary`** — A dark-surface button (#232a34) with white body text, used for secondary actions like "View Details" or "Learn More." The active state shifts the background to #363c46, maintaining the layered-dark aesthetic. Same uppercase bold typography as primary.

**`button-tertiary`** — A text-only button with no background, using the brand purple (#7538ff) for the text. Used for ghost actions like "Cancel" or "Clear Filters." The hover state adds a subtle underline.

**`button-pink`** — An accent button using the hot pink (#f83b78) from the brand's limited-edition palette. Used for sale CTAs, promotional banners, and special product launches. Active state deepens to #ef2d6c.

### Cards
**`product-card`** — A dark card surface (#232a34) with 8px rounded corners, containing a product image, title, price, and optional badges. The card has no shadow — depth is created through the contrast between the card surface and the darker canvas (#121212). Titles use 16px bold uppercase, prices use 20px bold, and sale prices render in hot pink (#f83b78).

**`product-card-badge`** — Small uppercase labels (11px, 0.5px letter-spacing) pinned to the top-left of product cards. Green (#31d77e) for "In Stock" or "New," pink (#f83b78) for "Sale," and purple (#7538ff) for "Exclusive." Badges have 2px corner radius and 2px 8px padding.

### Navigation
**`nav-bar`** — A full-width 64px dark bar (#121212) with a subtle bottom border (#363c46). Navigation links are 14px uppercase medium weight with 0.5px letter-spacing. The active link state uses the brand purple (#7538ff). The nav includes a search icon and cart icon on the right side.

**`category-nav`** — A secondary navigation strip (#1a1f26) below the main nav, 48px tall, containing product category links. Active categories are indicated by a 2px bottom border in brand purple (#7538ff).

### Forms
**`text-input`** — A dark input field (#232a34) with a 1px hairline border (#363c46), 4px corner radius, and 16px body text. On focus, the border switches to brand purple (#7538ff). Height is 44px with 12px 16px padding.

**`quantity-selector`** — A compact input for cart quantities, 40px tall with the same dark surface and hairline border as text inputs. Used in cart and product detail pages.

### Hero
**`hero-banner`** — A full-width 600px hero section on the dark canvas (#121212), featuring a 48px bold display headline and a single primary CTA button. The hero may include a background image or video with a dark overlay for text readability.

### Footer
**`footer`** — A dark footer (#121212) with a top border (#363c46), using muted gray (#919db1) for link text and body copy. Links hover to white (#e6e8ef). The footer contains column-based navigation, legal text, and social media icons.

### Search
**`search-bar`** — A compact 40px search input (#232a34) with a 1px hairline border and a 20px search icon in muted gray (#919db1). On focus, the border turns purple. The search bar appears in the main nav and on search results pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product cards go single-column; hero height reduces to 400px; category nav becomes a horizontal scroll strip; footer columns stack vertically |
| Tablet | 744–1128px | Nav shows limited links (Home, Headsets, Accessories, Support); product cards display in 2-column grid; hero height at 500px; category nav shows 4-5 items with scroll |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero at 600px; category nav shows all items; side-by-side product detail layout |
| Wide | > 1440px | Max-width container at 1440px centered; product cards in 4-column grid; additional whitespace on sides; hero may include parallax effects |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Nav links minimum 48px tap area
- Product card CTAs minimum 44px tap area
- Quantity selector buttons minimum 40px tap area
- Search icon minimum 44px tap area
- Category nav items minimum 44px tap area

### Collapsing Strategy
- Main nav collapses to hamburger menu below 744px
- Category nav becomes a horizontal scroll strip below 744px
- Product grid collapses from 4 columns to 3 to 2 to 1 as viewport shrinks
- Footer columns stack vertically below 744px
- Hero text and CTA stack vertically below 744px
- Product detail page switches from side-by-side to stacked below 744px
- Search bar may collapse to icon-only below 480px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for many components (text-input, quantity-selector, footer links) are inferred from common patterns rather than extracted from live site CSS
- Error styling for form inputs (border color, error message typography) not extracted
- Dark mode is the default; no light mode variant extracted
- Sub-brand palettes for Turtle Beach (e.g., Stealth series, Recon series) not extracted — may use accent colors like cyan (#4dfce0) or orange (#ffa020)
- Typography scale for mobile (smaller font sizes) not extracted — current values are desktop-first
- Animation and transition timing values (hover transitions, page load animations) not extracted
- Modal and overlay component styling not extracted
- Dropdown menu styling (nav submenus, sort/filter dropdowns) not extracted
- Checkout flow styling (Shopify checkout) not extracted — may use different palette
- Social media icon colors not extracted — may use brand-specific colors
- Stock image dominant tones may have influenced extracted hex list; brand's true primary (#7538ff) was identified as the most distinctive color in the list
- The extracted hex list includes many grays and accent colors — the brand's palette is primarily dark with purple as the single brand signal, with pink, cyan, and orange as secondary accents for specific use cases
