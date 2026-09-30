---
version: alpha
name: "Little Tikes"
source_url: "https://www.littletikes.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A primary blue (#259ce1) that reads as a bright, optimistic sky — not corporate navy or tech cobalt — anchors a playground of bold, chunky forms across the site. That blue hits buttons, badges, and the iconic red-and-yellow roof silhouette of the Cozy Coupe, while a deeper secondary blue (#22569c) provides weight in headers and footer blocks. The typography stack is a deliberate mix: Dinghy (a custom display face with a hand-drawn, slightly irregular feel) for headlines and hero text, GrilledCheeseBTN for playful callouts, and Nunito for body copy — a rounded sans-serif that keeps the reading experience soft and child-friendly. Oswald appears in uppercase navigation labels, adding a condensed, sporty contrast. The canvas is pure white (#ffffff), with hairline borders in #dedede that separate product tiles and category strips without adding visual noise. Product cards use generous {rounded.md} corners and a clean white surface, letting the toy photography — bright, shadowless, often against white or pastel backdrops — do the selling. Buttons are tall (48px minimum) with {rounded.sm} corners and the primary blue fill, while secondary actions drop to a white fill with a blue outline. The overall mood is unapologetically playful but not chaotic: the color palette stays tight (three blues, two grays, white), and the layout follows a strict 12-column grid with wide gutters. The brand trusts its 50-year heritage badge — "Parent Trusted for Over 50 Years" — as a persistent trust signal in the header, rendered in a small, uppercase Oswald label. There is no dark mode, no gradient, no shadow-heavy card treatment; the design is flat, bright, and built for speed on Shopify.

colors:
  primary: "#259ce1"
  primary-active: "#1e7fc4"
  primary-disabled: "#b3ddf5"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  secondary-blue: "#22569c"
  heritage-badge-bg: "#22569c"
  heritage-badge-text: "#ffffff"
  sale-badge-bg: "#e63946"
  sale-badge-text: "#ffffff"
  out-of-stock: "#dedede"
  star-rating: "#f4c542"

typography:
  display-xl:
    fontFamily: "'Dinghy', 'Oswald', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Dinghy', 'Oswald', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Dinghy', 'Oswald', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
  link:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Oswald', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'Oswald', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  playful-callout:
    fontFamily: "'GrilledCheeseBTN', 'Dinghy', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 12px 26px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  text-input-error:
    border: "2px solid {colors.sale-badge-bg}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    textColor: "{colors.primary}"
    border-bottom: "3px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: 0
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 700
    color: "{colors.ink}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.sale-badge-bg}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "8px"
    left: "8px"
  product-card-rating:
    color: "{colors.star-rating}"
    fontSize: "14px"
    padding: "0 {spacing.base} {spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    height: "400px"
    rounded: "{rounded.none}"
  hero-banner-alt:
    backgroundColor: "{colors.secondary-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    height: "300px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "10px 20px"
    height: 48px
  search-bar-focus:
    border: "2px solid {colors.primary}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    height: "120px"
  category-tile-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  footer-section:
    backgroundColor: "{colors.secondary-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.85
  footer-link-hover:
    opacity: 1
    textDecoration: "underline"
  heritage-badge:
    backgroundColor: "{colors.heritage-badge-bg}"
    textColor: "{colors.heritage-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 12px"
    display: "inline-block"
  sale-badge:
    backgroundColor: "{colors.sale-badge-bg}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  out-of-stock-badge:
    backgroundColor: "{colors.out-of-stock}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
    width: "100px"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
    width: "100%"
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
    fontWeight: 600
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with `#259ce1` and white text in bold Nunito at 16px. Used for "Add to Cart," "Shop Now," and primary form submissions. On hover, it shifts to `#1e7fc4` (`button-primary-active`). The disabled state (`button-primary-disabled`) drops to a pale blue `#b3ddf5` with white text, signaling non-interactivity while maintaining brand color presence. Height is 48px with `{rounded.sm}` corners — tall enough for easy tapping on mobile.

**`button-secondary`** — An outlined variant with a white fill, `#259ce1` text, and a 2px solid blue border. Used for "Learn More," "View Details," and secondary actions alongside primary buttons. On hover, the background fills with `#f5f5f5` (`surface-soft`) and the border shifts to `#1e7fc4`. Padding is slightly reduced (12px 26px) to account for the border width, keeping the total height at 48px.

**`button-tertiary-text`** — A text-only button with no background or border, used for "Clear Filters," "Cancel," and inline navigation links. Uses `{typography.button-sm}` (14px bold Nunito) and `#259ce1` text. Hover adds no background change but can include an underline if context-appropriate.

### Cards
**`product-card`** — The primary product display unit: a white card with `{rounded.md}` corners and a soft `#e8e8e8` border. The card has no internal padding (padding: 0) — the product image fills the top edge-to-edge, with title, price, and rating stacked below at `{spacing.sm}` and `{spacing.base}` gutters. On hover, the border turns `#259ce1` and a subtle `boxShadow` lifts the card. A `sale-badge` sits absolutely positioned at the top-left corner of the image area.

**`category-tile`** — A clickable tile for product categories (e.g., "Outdoor," "Role Play," "Ride-Ons"). Default state is a soft gray background (`#f5f5f5`) with dark text in `{typography.title-sm}`. On hover, the entire tile fills with `#259ce1` and white text — a bold, satisfying color flip that signals interactivity. Height is 120px with `{rounded.md}` corners.

### Navigation
**`nav-bar`** — A fixed-height (72px) white bar with a `#dedede` bottom border. Contains the brand logo (left), navigation links (center), and utility icons (search, cart, account — right). Links use Oswald at 15px with 1px letter spacing, all uppercase. The active link has a 3px `#259ce1` bottom border; hover turns the text `#259ce1`. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

**`search-bar`** — A pill-shaped input (`{rounded.full}`) with a `#dedede` border and 48px height. On focus, the border thickens to 2px and turns `#259ce1`. The input placeholder text uses `{typography.body-md}` in `#6a6a6a`. On mobile, the search bar expands to full width below the nav.

### Forms
**`text-input`** — Standard form input with a white fill, `{rounded.sm}` corners, and a `#dedede` 1px border. Height is 48px with 12px 16px padding. Focus state swaps to a 2px `#259ce1` border with no outline. Error state uses a 2px `#e63946` border (matching the sale badge red). Used for email signups, search filters, and account forms.

**`quantity-selector`** — A compact, 44px-tall input with a `#dedede` border and `{rounded.sm}` corners, 100px wide. Contains a numeric input flanked by minus/plus buttons. Used exclusively on product detail pages for cart quantity adjustment.

### Footer
**`footer-section`** — A deep blue (`#22569c`) footer block spanning the full viewport width. Links are white with 0.85 opacity, using `{typography.link}` (14px Nunito, semibold). On hover, opacity returns to 1 and an underline appears. The section uses `{spacing.section}` (64px) for top/bottom padding and `{spacing.xl}` (32px) for horizontal padding. Contains brand info, customer service links, legal text, and social icons.

### Badges
**`heritage-badge`** — A small, uppercase Oswald badge in `#22569c` with white text, used to call out "Parent Trusted for Over 50 Years" in the header and footer. Padding is 4px 12px with `{rounded.xs}` corners. It's always inline-block so it sits naturally alongside other header elements.

**`sale-badge`** — A red (`#e63946`) badge with white text, absolutely positioned on product cards. Uses `{typography.badge}` (11px Oswald, uppercase, 0.5px letter spacing). Padding is 2px 8px with `{rounded.xs}` corners.

**`out-of-stock-badge`** — A gray (`#dedede`) badge with `#6a6a6a` text, replacing the sale badge on unavailable products. Same typography and sizing as `sale-badge`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger; product cards stack full-width; hero banner height reduces to 250px; search bar moves below nav; category tiles become 2-column grid; footer collapses to stacked links |
| Tablet | 744–1128px | 2-column product grid; nav links remain visible but condensed; hero banner at 350px; category tiles in 3-column grid; search bar in nav remains full-width |
| Desktop | 1128–1440px | 3-4 column product grid; full nav with all links; hero banner at 400px; category tiles in 4-column grid; search bar in nav with compact width |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid expands to 4 columns; hero banner remains 400px; category tiles in 5-column grid; all whitespace scales proportionally |

### Touch Targets
- All buttons and interactive elements minimum 48px height
- Nav links minimum 44px tap area (padding accounts for this)
- Product cards have full-card tap target (entire card is clickable)
- Category tiles have full-tile tap target
- Quantity selector buttons (minus/plus) minimum 44x44px
- Search bar and text inputs minimum 48px height
- Footer links minimum 44px tap area (padding added on mobile)

### Collapsing Strategy
- Primary nav collapses to hamburger menu at < 744px; menu opens as full-screen overlay with vertical link list
- Product grid collapses from 4 columns (desktop) to 2 columns (tablet) to 1 column (mobile)
- Category tiles collapse from 5 columns (wide) to 2 columns (mobile)
- Hero banner text and CTA stack vertically on mobile; image may crop or resize
- Footer link columns collapse to single column on mobile; accordion pattern used for link groups
- Search bar moves from inline nav position to full-width below nav on mobile
- Product card badges (sale, out-of-stock) remain visible but may reposition on smaller cards
- Breadcrumb trail truncates on mobile (shows only last 2 levels with "..." for earlier levels)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for `button-secondary` and `button-tertiary-text` are inferred from common patterns; exact color transitions not extracted from live site
- Error styling for form validation (error messages, iconography, animation) not observed; `text-input-error` border color is an assumption based on sale badge red
- Sub-brand or seasonal color palettes (e.g., holiday themes, licensed characters) not captured; only core brand palette extracted
- Dark mode not present on live site; no dark theme tokens defined
- Typography scale for mobile (font-size reductions, line-height adjustments) not extracted; current values are desktop-first
- Animation and transition timing (hover fades, menu open/close speed, card lift) not observed; no `transition` properties defined
- Focus-visible styles for keyboard navigation not extracted; only `:focus` states defined
- Shopify-specific components (cart drawer, checkout button, payment icons) not captured beyond basic `add-to-cart-button`
- Star rating component exact sizing and spacing not extracted; `product-card-rating` uses generic 14px
- The extracted hex list (#259ce1, #3a3a3a, #dedede, #22569c, #121212) is a generic web palette of blues and grays with one bright accent (#259ce1). No distinctive brand color (e.g., the iconic Cozy Coupe red or yellow) appeared in the top extracted colors, likely because those colors appear in product photography rather than UI chrome. The primary blue (#259ce1) is the most distinctive accent in the extracted set and is used as the brand's primary UI color.
