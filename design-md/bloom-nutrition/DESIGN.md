---
version: alpha
name: "Bloom Nutrition"
source_url: "https://bloomnu.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A verdant, energetic wellness brand built on a deep forest-green primary (#215b32) that reads as chlorophyll-rich and grounded, not corporate or clinical. The brand's visual system is a study in contrast: a crisp white canvas (#ffffff) against that dense green, punctuated by a warm marigold accent (#ffcf2a) that appears in star ratings, sale badges, and micro-interactions — a citrus-bright jolt against the botanical base. A secondary sage-green family (#d4ead4, #bbe1ba, #bfdeb5) softens the palette, appearing in ingredient callouts, background sections, and product photography overlays, while a whisper-pink (#f2c3d2) and lavender (#ead4f8) surface in limited-edition packaging and social proof badges, suggesting a brand that knows its audience craves both efficacy and delight. Typography is a layered affair: the display voice is Gazpacho-Black, a heavy, slightly condensed sans-serif with a custom italic variant (Santi-Rey-Gazpacho-Italic-Black) that adds a hand-drawn, editorial flair to hero headlines and product names. Supporting body copy runs in Poppins and TTravels (Medium, DemiBold, Bold), creating a system that feels simultaneously playful and authoritative. Buttons are generously padded (`{spacing.lg}` horizontal, `{spacing.base}` vertical) with `{rounded.sm}` corners, while product cards use `{rounded.md}` and feature a subtle shadow that lifts the pack shot off the page. The navigation bar is fixed, full-width, and transparent-to-white on scroll, with the brand's green logo mark centered and a cart icon that pulses with `{colors.primary}`. The overall mood is one of approachable vitality — a supplement brand that doesn't look like a pharmacy aisle but like a farmer's market stall designed by a modern editorial studio.

colors:
  primary: "#215b32"
  primary-active: "#1c5633"
  primary-disabled: "#bfdeb5"
  ink: "#0b0b0b"
  body: "#222222"
  muted: "#676986"
  muted-soft: "#878787"
  hairline: "#e5e5e5"
  hairline-soft: "#dedede"
  canvas: "#fbf1e4"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#ffcf2a"
  accent-marigold-active: "#ffb548"
  accent-pink: "#f36178"
  accent-pink-soft: "#f2c3d2"
  accent-lavender: "#ead4f8"
  accent-blue: "#4271fe"
  sage-light: "#d4ead4"
  sage-mid: "#bbe1ba"
  sage-dark: "#77bc71"
  star-rating: "#ffcf2a"
  error: "#f36178"
  success: "#77bc71"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Gazpacho-Black', 'Santi-Rey-Gazpacho-Italic-Black', 'TTravels-Bold', sans-serif"
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Gazpacho-Black', 'TTravels-Bold', sans-serif"
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'TTravels-Bold', 'Poppins', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'TTravels-DemiBold', 'Poppins', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'TTravels-DemiBold', 'Poppins', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'TTravels-Medium', 'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'TTravels-Bold', 'Poppins', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'TTravels-DemiBold', 'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'TTravels-Medium', 'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'TTravels-Medium', 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'TTravels-Bold', 'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'TTravels-Bold', 'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
    textDecoration: line-through

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
    padding: 16px 32px
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 52px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 52px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 14px 30px
    height: 52px
  button-secondary-active:
    backgroundColor: "{colors.sage-light}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
    padding: 14px 30px
    height: 52px
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 52px
  button-accent-marigold-active:
    backgroundColor: "{colors.accent-marigold-active}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 52px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-pill-outline:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.primary}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 14px 16px
    height: 52px
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 13px 15px
    height: 52px
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.error}"
    padding: 13px 15px
    height: 52px
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 14px 16px
    height: 52px
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 2px 12px rgba(0,0,0,0.06)"
    padding: 0
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.1)"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.primary}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-section:
    backgroundColor: "{colors.sage-light}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "18px 40px"
    height: 56px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "12px 20px"
    height: 48px
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
    padding: "11px 19px"
    height: 48px
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.sage-light}"
    typography: "{typography.link}"
    hoverTextColor: "{colors.accent-marigold}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    marginBottom: "{spacing.base}"
  badge-sale:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-best-seller:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    height: 44px
  accordion-header:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-switch-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-switch-thumb:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px

## Components

### Buttons
**`button-primary`** — The workhorse CTA across the site. A solid forest-green (`{colors.primary}`) rectangle with `{rounded.sm}` corners and white text set in `{typography.button-md}` (TTravels-DemiBold, 15px, 0.3px letter-spacing). On hover, shifts to `{colors.primary-active}` (#1c5633). Disabled state uses `{colors.primary-disabled}` (#bfdeb5) with full opacity — no transparency. Used for "Add to Cart", "Subscribe & Save", and primary form submissions.

**`button-secondary`** — An outlined variant with `{colors.primary}` text and a 2px solid border on a `{colors.canvas}` background. Active state fills the background with `{colors.sage-light}` (#d4ead4) and deepens the border to `{colors.primary-active}`. Used for "Learn More", "Shop Bundles", and secondary checkout actions.

**`button-accent-marigold`** — The high-energy accent button. `{colors.accent-marigold}` (#ffcf2a) background with dark `{colors.ink}` text. Active state shifts to `{colors.accent-marigold-active}` (#ffb548). Reserved for sale CTAs, limited-time offers, and promotional banners where the brand wants maximum visual pop against the green-dominant palette.

**`button-pill-primary`** — A fully rounded (`{rounded.full}`) pill variant of the primary button, shorter at 44px height. Used in subscription selectors, flavor pickers, and inline cart actions where space is tighter.

**`button-pill-outline`** — An outlined pill with a 1.5px border. Used for secondary inline actions like "Compare" or "View Details" on product cards.

### Cards
**`product-card`** — A white card with `{rounded.md}` (12px) corners and a subtle shadow (`0 2px 12px rgba(0,0,0,0.06)`). The product image occupies the top half with `{rounded.md}` top corners only. Title uses `{typography.title-md}` (TTravels-DemiBold, 18px) in `{colors.ink}`. Price uses `{typography.price}` (TTravels-Bold, 18px) in `{colors.primary}`. On hover, the shadow deepens to `0 8px 24px rgba(0,0,0,0.1)`. Badges (sale, new, best-seller) are absolutely positioned at top-left with `{rounded.xs}` (4px) corners.

### Navigation
**`nav-bar`** — Fixed top navigation at 72px height on desktop, 64px on scroll. White background with a subtle bottom border (`{colors.hairline-soft}`). Logo is centered, nav links are uppercase TTravels-Medium at 14px with 0.5px letter-spacing. Active link has a 2px `{colors.primary}` bottom border. Cart icon uses `{colors.primary}` fill.

**`nav-link-active`** — Active navigation link with `{colors.primary}` text color and a 2px bottom border in the same green. Inactive links use `{colors.muted}` (#676986).

### Forms
**`text-input`** — Standard text input at 52px height with `{rounded.sm}` (8px) corners, a 1px `{colors.hairline}` border, and `{colors.body}` text. On focus, the border thickens to 2px `{colors.primary}`. Error state uses 2px `{colors.error}` (#f36178). Used for email signups, search, and checkout fields.

**`select-dropdown`** — Matches text-input styling but includes a custom chevron icon in `{colors.primary}`. Used for quantity, subscription frequency, and flavor selection.

### Badges
**`badge-sale`** — Marigold background (`{colors.accent-marigold}`) with dark text. Used for percentage-off badges on product cards and collection pages.

**`badge-new`** — Pink background (`{colors.accent-pink}`) with white text. Used for new product launches and limited drops.

**`badge-best-seller`** — Lavender background (`{colors.accent-lavender}`) with dark text. Used for top-performing products.

### Footer
**`footer-section`** — Full-width footer with `{colors.primary}` background and white text. Links use `{colors.sage-light}` (#d4ead4) and shift to `{colors.accent-marigold}` on hover. Section headings use `{typography.title-md}` with `{spacing.base}` bottom margin. Padding is `{spacing.xxl}` vertical, `{spacing.lg}` horizontal.

### Hero
**`hero-section`** — Full-width hero with `{colors.sage-light}` (#d4ead4) background. Headline uses `{typography.display-lg}` (Gazpacho-Black, 36px). CTA button is `{hero-cta}` at 56px height with 18px/40px padding. Used on homepage and collection landing pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Navigation collapses to hamburger menu. Product cards stack single-column. Hero text reduces to `{typography.display-md}` (28px). Buttons become full-width. Footer links stack vertically. Search bar moves to mobile drawer. |
| Tablet | 744–1128px | Navigation shows 4–6 links. Product cards display in 2-column grid. Hero maintains `{typography.display-lg}` but reduces padding. Sidebar filters become horizontal scroll. |
| Desktop | 1128–1440px | Full navigation with all links. Product cards in 3-column grid. Hero at full padding. Multi-column footer layout. |
| Wide | > 1440px | Max-width container at 1440px with centered content. Product cards in 4-column grid. Hero scales proportionally. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility.
- Product card tap targets (title, price, add-to-cart) are at least 48px tall.
- Navigation hamburger icon is 44x44px with 12px padding.
- Quantity selector buttons are 44x44px.
- Accordion headers are 48px minimum tap height.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses to a hamburger menu with a slide-in drawer from the left.
- Product filters collapse into a sticky bottom sheet with a "Filter" button.
- Footer link groups collapse into accordions with `{colors.primary}` chevron icons.
- Product description and ingredients sections collapse into accordions on all breakpoints.
- The search bar collapses to an icon that expands to a full-width overlay on tap.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components are inferred from the extracted palette and common patterns; actual `:hover`, `:focus`, and `:active` CSS could not be extracted from the live site.
- Error, success, and warning toast/notification styling is not present in the extracted data.
- Dark mode is not supported; no dark-mode tokens were found.
- Sub-brand or collection-specific palettes (e.g., limited-edition drops with custom colors) are not captured.
- The `Timesquare-Bold` and `Timesquare-Regular` fonts were found in the CSS but their usage context (headlines, decorative elements, or legacy) is unclear — they may be used sparingly for specific marketing campaigns.
- The `oke-widget-icons` font family suggests Okendo reviews integration; review widget styling (stars, text, layout) is not captured.
- Shopify checkout widget colors (e.g., `#4271fe` for Shop Pay, `#ffcf2a` for Afterpay) are present in the extracted palette but are not part of the Bloom brand system — they should be treated as third-party overrides.
- The `#fbf1e4` canvas color appears in the extracted palette but its usage context (background sections, product photography backdrop, or checkout) is uncertain; it may be a secondary background rather than the primary canvas.
- Animation and transition durations/easings are not extracted.
- Typography `fontWeight` values for Gazpacho-Black and TTravels variants are inferred from font naming conventions; actual CSS `font-weight` declarations may differ.
