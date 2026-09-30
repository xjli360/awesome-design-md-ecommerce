---
version: alpha
name: "Lume Deodorant"
source_url: "https://lumedeodorant.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A confident, unapologetically pink brand that redefines body care with a bold, playful, and science-backed voice. The palette is anchored by a vibrant hot pink `#de1b83` that screams "this is not your grandmother's deodorant," supported by a deep maroon `#200000` and near-black `#020000` that ground the system with unexpected sophistication. The brand leans hard into its signature pink — it appears on every primary CTA, badge, and accent, creating a visual heartbeat that's impossible to ignore. Secondary accents of electric blue `#0077d7`, warm gold `#ffe593`, and a punchy orange `#fe5000` add energy without competing with the dominant rose. The canvas is a warm off-white `#fff4fd` with subtle pink undertones, while surfaces use `#fff4f7` and `#fff4f0` to keep the entire experience feeling soft and approachable. Typography is set in Poppins, a geometric sans-serif that balances the brand's playful personality with clean readability — display sizes at 28px and 24px carry the bold headlines, while body copy at 16px and 14px keeps product descriptions legible. Every corner is generously rounded (`{rounded.sm}` for buttons, `{rounded.md}` for cards, `{rounded.full}` for pills and badges), reinforcing the brand's friendly, approachable ethos. The result is a system that feels like a confident friend — warm, direct, and never apologetic about its pinkness.

colors:
  primary: "#de1b83"
  primary-active: "#b41469"
  primary-disabled: "#fcb5ce"
  ink: "#200000"
  body: "#201f21"
  muted: "#716e74"
  muted-soft: "#8f8d92"
  hairline: "#f6f6f7"
  hairline-soft: "#ebfff2"
  canvas: "#fff4fd"
  surface-soft: "#fff4f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#0077d7"
  accent-blue-active: "#0061a2"
  accent-purple: "#ad0da6"
  accent-purple-active: "#992494"
  accent-orange: "#fe5000"
  accent-orange-active: "#f15a2c"
  accent-gold: "#ffe593"
  accent-gold-active: "#ffeeac"
  badge-pink: "#de1b83"
  badge-blue: "#0077d7"
  badge-purple: "#ad0da6"
  badge-orange: "#fe5000"
  star-rating: "#f6da5b"
  error: "#d60d0d"
  error-soft: "#fff4e2"
  success: "#ebfff2"
  scrim: "#170000"

typography:
  display-xl:
    fontFamily: "'Poppins', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Poppins', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'Poppins', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Poppins', system-ui, sans-serif"
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
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  badge-new:
    backgroundColor: "{colors.badge-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-sale:
    backgroundColor: "{colors.badge-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-best-seller:
    backgroundColor: "{colors.badge-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  add-to-cart-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 56px

## Components

### Buttons
**`button-primary`** — The workhorse CTA across the entire site, rendered in the brand's signature hot pink `{colors.primary}` with white text. Hover state shifts to `{colors.primary-active}` for a subtle darkening effect, while disabled state uses `{colors.primary-disabled}` for a muted, low-contrast appearance. The 8px rounded corners (`{rounded.sm}`) keep the button feeling friendly and modern, while the 48px height and 28px horizontal padding provide a generous, easy-to-tap target.

**`button-secondary`** — An outlined variant that inverts the primary button's color relationship, using a white background with a 2px solid `{colors.primary}` border and pink text. On hover, the background shifts to `{colors.surface-soft}` and the border darkens to `{colors.primary-active}`, creating a subtle pressed effect. Used for secondary actions like "Learn More" or "View Details" alongside primary CTAs.

**`button-tertiary-text`** — A minimal text-only button with no background or border, using `{colors.primary}` for the text. This is the lightest touch option, used for inline actions like "Cancel" or "Skip" where visual weight should be minimized. The text remains pink to maintain brand consistency.

**`button-pill-primary`** and **`button-pill-secondary`** — Pill-shaped variants of the primary and secondary buttons, using `{rounded.full}` for a completely rounded appearance. These are used for promotional badges, subscription CTAs, and any action that benefits from a more playful, approachable silhouette. The pill shape is a signature Lume design move, appearing on badges and search bars as well.

### Cards
**`product-card`** — A clean white card with `{rounded.md}` corners that houses product imagery, titles, and pricing. The card itself has no padding — all internal spacing is handled by child elements — and uses `{colors.surface-card}` for a crisp, clean background. Product titles use `{typography.title-sm}` in `{colors.ink}`, while prices are set in `{typography.body-md}` in `{colors.primary}` to draw the eye to the cost.

**`product-card-image`** — The image area of the product card, which uses `{rounded.md}` on the top corners only, creating a seamless transition into the text content below. This subtle detail keeps the card feeling cohesive while allowing the image to bleed to the edges.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, using `{colors.canvas}` background with a subtle bottom border in `{colors.hairline}`. Navigation links use `{typography.nav-link}` — uppercase, 14px, weight 600 with 0.5px letter spacing — for a clean, authoritative feel. Active links switch to `{colors.primary}` to indicate the current section.

### Badges
**`badge-new`**, **`badge-sale`**, **`badge-best-seller`** — Small, pill-shaped badges (`{rounded.full}`) that sit on product cards and hero sections to highlight special items. Each badge uses a distinct accent color from the brand palette: pink for new products, orange for sale items, and blue for best sellers. The 11px uppercase typography with 0.5px letter spacing ensures readability at small sizes while maintaining the brand's confident voice.

### Forms
**`text-input`** — Standard text input fields with a white background, 48px height, and `{rounded.sm}` corners. The default state uses a `{colors.hairline}` border, which shifts to `{colors.primary}` on focus and `{colors.error}` when validation fails. The 12px vertical and 16px horizontal padding provides comfortable typing space.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) that spans the full width of its container on mobile and collapses to a fixed width on desktop. The 48px height and 20px horizontal padding create a generous touch target, while the active state border in `{colors.primary}` provides clear focus indication.

### Footer
**`footer`** — A dark footer section using `{colors.ink}` as the background with white text for maximum contrast. Links use `{colors.muted-soft}` in the default state and shift to `{colors.canvas}` on hover, creating a subtle interactive cue. The 48px vertical padding provides breathing room for link lists and legal text.

### Interactive Elements
**`accordion`** — Collapsible sections used for product descriptions, ingredient lists, and FAQ content. Each accordion has a white background with `{rounded.sm}` corners and a `{colors.hairline}` border. The header uses `{typography.title-sm}` in `{colors.ink}` for clear hierarchy, while the body content flows in `{typography.body-md}`.

**`quantity-selector`** — A compact control for adjusting product quantities in the cart, using a 40px height with `{rounded.sm}` corners and a `{colors.hairline}` border. The small footprint allows it to sit comfortably alongside add-to-cart buttons without dominating the layout.

**`add-to-cart-bar`** — A prominent, full-width CTA bar at 56px height that appears on product detail pages. Using `{colors.primary}` with white text and `{rounded.sm}` corners, it's designed to be the most visually dominant element on the page, driving the primary conversion action.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, nav collapses to hamburger, product cards stack vertically, hero text reduces to `{typography.display-lg}`, search bar expands to full width, footer links stack |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, hero maintains `{typography.display-xl}`, search bar fixed width, footer links in two columns |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, hero section at max width, search bar centered, footer links in four columns |
| Wide | > 1440px | Max-width container at 1440px, product grid expands to four columns, hero section uses larger imagery, all components at their maximum comfortable size |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets extend to the full card area, not just the title or price
- Accordion headers are 48px minimum height for easy tapping on mobile
- Add-to-cart bar is 56px tall, exceeding the minimum touch target for critical actions
- Badges are 24px minimum height with 4px padding to ensure readability and tapability

### Collapsing Strategy
- Top navigation collapses to a hamburger menu at 744px breakpoint, with the brand logo remaining visible
- Product grid collapses from 4 columns to 3 to 2 to 1 as viewport narrows
- Footer link columns collapse from 4 to 2 to 1, with accordion-style sections on mobile
- Hero section reduces font size and stacks CTA buttons vertically on mobile
- Search bar transitions from fixed-width to full-width below 744px
- Product card images maintain aspect ratio but reduce in size proportionally

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for tertiary text buttons (no reliable extraction available)
- Error state styling for dropdowns and select elements
- Success and warning toast/notification styling
- Dark mode color overrides (not present on the live site)
- Sub-brand or seasonal palette variations (e.g., holiday collections)
- Focus ring styles and keyboard navigation indicators
- Loading state skeletons or spinners
- Tooltip and popover styling
- Modal/dialog overlay styling
- Disabled state for text inputs and select elements
- Checkbox and radio button custom styling
- Slider/range input styling
- Table and data display styling
- Print stylesheet overrides
- Animation timing and easing curves
- Icon library specifications (SVG vs icon font, sizing conventions)
