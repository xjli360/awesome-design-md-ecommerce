---
version: alpha
name: "Slackers"
source_url: "https://slackers.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A cluttered, generous bazaar of pop-culture obsessions where a deep navy blue (#003388) anchors the header and footer, while a vivid cobalt (#1a7ac4) drives every primary action — add-to-cart buttons, navigation highlights, and category links. The palette is a noisy mix of retail urgency and playful chaos: a sharp red (#a20505) marks sale badges and clearance tags, a muted teal (#0e766d) appears in select category accents, and a warm gray scale (#bfbfbf, #ededed, #f4f4f4) provides the neutral backdrop for product grids. The canvas is a clean white (#fefefe) with soft gray surfaces (#f4f4f4) for card backgrounds, while the ink (#1f1f1f) keeps body text readable against the busy visual landscape. Typography runs Open Sans at modest weights — display headlines sit at 24px weight 600, body text at 14px weight 400, and buttons at 15px weight 600 — creating a functional, no-nonsense hierarchy that lets the product photography and price tags do the heavy lifting. The search bar uses a pill shape ({rounded.full}) with a subtle border (#bfbfbf), while product cards have soft corners ({rounded.sm}) and a light shadow that lifts them off the page. Category navigation runs as a horizontal strip of pill-shaped buttons with the primary blue fill, creating clear visual paths through music, movies, games, toys, and comics. The footer is a dense information hub with multiple columns, social icons in their brand colors (#3e5c9a for Facebook, #55acee for Twitter), and a newsletter signup that mirrors the primary button style. The overall feel is that of a well-organized record store — lots of visual texture, clear pricing, and a sense that every square inch is selling something.

colors:
  primary: "#1a7ac4"
  primary-active: "#006ba1"
  primary-disabled: "#8a9faf"
  ink: "#1f1f1f"
  body: "#313131"
  muted: "#474747"
  muted-soft: "#607385"
  hairline: "#bfbfbf"
  hairline-soft: "#ededed"
  canvas: "#fefefe"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#a20505"
  accent-teal: "#0e766d"
  accent-purple: "#7a00df"
  accent-maroon: "#3e5c9a"
  accent-twitter: "#55acee"
  accent-instagram: "#4721fb"
  accent-pink: "#faaca8"
  sale-badge: "#a20505"
  category-blue: "#003388"
  star-rating: "#1e90ff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  price:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "'Open Sans', 'PT Sans', 'Raleway', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
    color: "{colors.accent-red}"

rounded:
  none: 0px
  xs: 3px
  sm: 6px
  md: 10px
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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-category:
    backgroundColor: "{colors.category-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-category-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.category-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-bar-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-bar-link-active:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.on-primary}"
  top-header:
    backgroundColor: "{colors.category-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    marginTop: "{spacing.xs}"
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.base}"
  category-pill:
    backgroundColor: "{colors.category-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  category-pill-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.category-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.85
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.sm}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 42px
    border: "1px solid {colors.hairline}"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 42px
  social-icon:
    width: 24px
    height: 24px
    rounded: "{rounded.full}"
  social-icon-facebook:
    backgroundColor: "{colors.accent-maroon}"
  social-icon-twitter:
    backgroundColor: "{colors.accent-twitter}"
  social-icon-instagram:
    backgroundColor: "{colors.accent-instagram}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.base}"
    minHeight: 300px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    height: 48px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
    padding: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"
  pagination-inactive:
    textColor: "{colors.muted}"
    padding: "4px 10px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for add-to-cart, checkout, and submit actions. Rendered in the brand's cobalt blue (#1a7ac4) with white text and a soft 6px corner radius. On hover, it shifts to a deeper navy (#006ba1). The disabled state fades to a muted steel blue (#8a9faf) with reduced opacity. Height is 44px with 12px/24px padding for comfortable tap targets.

**`button-secondary`** — An outlined alternative for less prominent actions like "View Details" or "Cancel". Uses a white background with a 1px hairline border (#bfbfbf) and dark ink text. Matches the primary button's 44px height and 6px radius for visual consistency in grouped button layouts.

**`button-sale`** — A compact, urgent button used exclusively for clearance and sale items. Uses the accent red (#a20505) with white text, smaller 13px font, and a tighter 36px height. Appears on product cards and in sale category sections to create visual urgency.

**`button-category`** — Pill-shaped navigation buttons used in the category strip and filter bars. Uses the deep navy (#003388) with white text and a full 9999px radius. Active state switches to the primary cobalt (#1a7ac4). Height is 36px with 8px/20px padding for a compact, tappable chip.

### Cards
**`product-card`** — The core product display unit, a white card with a 6px radius and subtle box shadow (0 1px 3px rgba(0,0,0,0.1)). Contains a square aspect-ratio product image, a 14px bold title, and the price below. Sale items display the price in red (#a20505) with a red sale badge pinned to the top-left corner of the image. Cards stack in a responsive grid with 16px gaps.

**`sale-badge`** — A small, sharp red badge pinned to sale product cards. Uses the accent red (#a20505) with white uppercase 11px bold text and a 3px radius. Padding is 2px/8px for a compact tag that doesn't overwhelm the product image.

### Navigation
**`nav-bar`** — The primary horizontal navigation bar, a 48px strip in deep navy (#003388) with white links. Links have 16px horizontal padding and a 2px white underline on the active state. The nav contains category links (Music, Movies, Games, Toys, Comics) and a search icon.

**`top-header`** — A thin 36px utility bar above the main nav, also in deep navy (#003388). Contains store info, shipping announcements, and account/login links in 12px white text. Creates a clear information hierarchy before the main navigation.

**`category-strip`** — A horizontal scrollable strip of category pills below the hero banner. Background is a soft gray (#f4f4f4) with pill-shaped buttons in deep navy (#003388) for active categories and outlined pills for inactive ones. Used for sub-category filtering (e.g., "Vinyl", "CDs", "Cassettes" under Music).

### Forms
**`text-input`** — Standard form input for search, newsletter, and checkout forms. White background with a 1px hairline border (#bfbfbf), 14px body text, and a 6px radius. On focus, the border thickens to 2px and switches to the primary blue (#1a7ac4). Height is 42px with 10px/14px padding.

**`search-bar`** — A pill-shaped search input with a 9999px radius, used in the header and on search pages. Matches the text-input styling but with a full pill shape and 20px horizontal padding for a more prominent, friendly appearance. Focus state mirrors the text-input with a 2px primary blue border.

**`newsletter-input`** — Footer-specific email input that matches the text-input styling. Paired with a primary blue submit button (`newsletter-button`) that uses the button-sm typography and 42px height for a seamless inline form.

### Footer
**`footer`** — A dense, multi-column footer in deep navy (#003388) with white text. Contains column headings in 14px bold, links in 14px regular at 85% opacity, social media icons in their brand colors, and a newsletter signup form. Padding is 48px vertical and 16px horizontal. Social icons are 24px circles with brand-specific background colors (Facebook: #3e5c9a, Twitter: #55acee, Instagram: #4721fb).

### Hero
**`hero-banner`** — A full-width promotional banner with a soft gray background (#f4f4f4), 24px bold headline, and a primary blue CTA button. Minimum height is 300px with 48px vertical padding. Used for seasonal promotions, new arrivals, and featured categories. The CTA button matches the primary button style but with 32px horizontal padding for a more prominent call-to-action.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns), hamburger menu replaces nav-bar, category strip becomes horizontally scrollable, hero banner reduces to 200px min-height, footer stacks into single column, search bar collapses to icon-only |
| Tablet | 744–1128px | Two-column product grid, nav-bar shows top-level categories only, category strip remains scrollable, hero banner at 250px min-height, footer shows 2-3 columns |
| Desktop | 1128–1440px | Three-column product grid, full nav-bar with all categories visible, category strip shows all pills without scroll, hero banner at 300px min-height, footer shows 4 columns |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, all elements at their largest comfortable size, footer shows 5 columns with additional link groups |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Category pills are 36px height (slightly below ideal but consistent with industry patterns for chip-style navigation)
- Product card tap targets include the entire card surface, not just the title or price
- Search bar is 44px height for easy one-handed tapping
- Social media icons are 24px circles with 44px touch padding

### Collapsing Strategy
- Top header (36px utility bar) collapses on mobile to save vertical space, with its content moved into the hamburger menu
- Nav-bar collapses to a hamburger icon on mobile, with a slide-out drawer revealing all categories
- Category strip becomes a horizontally scrollable row on mobile and tablet, with no visible scrollbar but swipeable
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer collapses from 5 columns (wide) to 1 column (mobile), with accordion-style expandable sections for each column heading
- Hero banner reduces min-height from 300px to 200px on mobile, with smaller headline and CTA text

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for most components could not be reliably extracted from static HTML/CSS. The button-primary hover state (#006ba1) is inferred from the extracted color list, but secondary, tertiary, and link hover states are unconfirmed.
- **Error styling** for form inputs (validation errors, required field indicators) was not present in the extracted data. The text-input focus state is confirmed, but error borders, error messages, and success states are unknown.
- **Dark mode** is not supported on the live site based on extracted data. No dark mode colors or media queries were found.
- **Typography scale** is inferred from common Open Sans usage patterns. The exact font sizes, weights, and line heights for each token are estimates based on the extracted font declarations and typical e-commerce hierarchy. The actual site may use slightly different values.
- **Spacing system** is a best-guess based on common 8px grid patterns. The extracted CSS did not include a clear spacing scale, so values are set to standard increments that match the visual density of the site.
- **Sub-brand palettes** for specific categories (Music, Movies, Games, Toys, Comics) may exist but were not extracted. The category-blue (#003388) is used uniformly across all categories in the extracted data.
- **Checkout flow** colors (Shopify Pay, Klarna, Afterpay) were present in the extracted color list but are not part of the brand's design system. These have been excluded from the color palette.
- **Social icon colors** are standard brand colors for Facebook (#3e5c9a), Twitter (#55acee), and Instagram (#4721fb) and may not reflect the exact shades used on the live site.
- **Animation and transition** values (durations, easing functions) were not extractable. The site likely uses simple hover transitions, but specific timing is unknown.
- **Accessibility contrast ratios** have not been verified against WCAG standards. The primary blue on white (#1a7ac4 on #ffffff) likely passes, but the red on white (#a20505 on #ffffff) and navy on white (#003388 on #ffffff) should be checked.
