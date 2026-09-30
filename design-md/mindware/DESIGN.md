---
version: alpha
name: "MindWare"
source_url: "https://www.mindware.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A vivid, curiosity-driven educational brand that uses a saturated orange (#c74c00) as its primary voltage — not as a playful accent but as the structural anchor for CTAs, navigation highlights, and category badges, giving the entire site the energy of a freshly sharpened pencil and a blank challenge. The palette is unusually broad for a toy retailer: alongside the core orange sit a cool teal (#1f9cd8), a zingy lime (#80b800), a warm pink (#ee5f9e), and a deep marigold (#fac300), creating a color system that feels less like a brand guideline and more like a box of 64 crayons where every color has a job. The canvas is near-white (#eef9fd), a barely-there ice blue that keeps the page from feeling sterile, while ink (#181818) and body (#221f1f) provide dense, readable contrast. Typography runs on Roboto and Roboto Condensed — the condensed weight used for tight category labels and price tags, the standard weight for body copy — giving the system a clean, slightly technical feel that signals "learning tool" rather than "flashy toy." Buttons use full-height fills with `{rounded.sm}` corners, and the search bar sits in a pill-shaped container (`{rounded.full}`) with a bold orange outline. The overall mood is one of cheerful precision: every color has a reason, every corner is deliberate, and the white space is generous enough to let the product photography — often showing children mid-discovery — do the emotional work.

colors:
  primary: "#c74c00"
  primary-active: "#9d3700"
  primary-disabled: "#f6b6d2"
  ink: "#181818"
  body: "#221f1f"
  muted: "#444444"
  muted-soft: "#2c2c2c"
  hairline: "#acc9d4"
  hairline-soft: "#eef9fd"
  canvas: "#eef9fd"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#1f9cd8"
  accent-teal-active: "#0073b2"
  accent-lime: "#80b800"
  accent-pink: "#ee5f9e"
  accent-marigold: "#fac300"
  accent-orange-bright: "#fa6f22"
  accent-orange-deep: "#eb5a00"
  star-rating: "#fac300"
  sale-badge: "#ee5f9e"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Roboto', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Roboto', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Roboto', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Roboto', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Roboto', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', 'Arial', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Roboto', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  link:
    fontFamily: "'Roboto', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', 'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  category-label:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: 0

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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-orange:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-lime:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button-circle:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  icon-button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-sticky:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "2px solid {colors.primary}"
  search-bar-icon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: 8px 12px 4px 12px
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.primary}"
    padding: 0px 12px 12px 12px
  product-card-rating:
    color: "{colors.star-rating}"
    padding: 0px 12px 8px 12px
  product-card-badge:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.category-label}"
    rounded: "{rounded.lg}"
    padding: 16px
    border: "1px solid {colors.hairline}"
  category-card-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
    padding: 16px
  hero-banner:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: 48px 24px
    rounded: "{rounded.lg}"
  hero-banner-orange:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: 48px 24px
    rounded: "{rounded.lg}"
  hero-banner-lime:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: 48px 24px
    rounded: "{rounded.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: 48px 24px 24px 24px
  footer-link:
    color: "{colors.accent-teal}"
    typography: "{typography.link}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  new-badge:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
  breadcrumb-link:
    color: "{colors.accent-teal}"
    typography: "{typography.link}"
  breadcrumb-current:
    color: "{colors.body}"
    typography: "{typography.body-sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with MindWare's signature orange (#c74c00). Used for "Add to Cart," "Shop Now," and primary form submissions. On hover, it deepens to `{colors.primary-active}` (#9d3700). Disabled state uses a muted pink `{colors.primary-disabled}` (#f6b6d2) to signal inactivity without introducing gray. **`button-secondary`** — An outlined variant with a white fill and orange border, used for secondary actions like "View Details" or "Learn More." The 2px border keeps it visually balanced alongside the primary button. **`button-tertiary-text`** — A text-only button with no background or border, used for less prominent actions like "Cancel" or "Clear Filters." **`button-pill-orange`**, **`button-pill-teal`**, and **`button-pill-lime`** — Pill-shaped buttons (`{rounded.full}`) used for category filters, quick-add actions, and promotional tags. Each color maps to a distinct product category or promotion type, allowing users to visually scan by color.

### Cards
**`product-card`** — A white card with `{rounded.md}` corners containing a product image, title, price, and rating. The image area uses `{rounded.md}` on the top corners only, creating a subtle visual break between photo and text. The price is rendered in Roboto Condensed Bold at 18px in the primary orange, making it the most visually prominent text element on the card. **`category-card`** — A larger card with `{rounded.lg}` corners used for department navigation (e.g., "Brainy Toys," "Games," "STEM"). Inactive cards have a white fill with a light blue-gray border (`{colors.hairline}`). Active or hovered cards flip to a solid orange fill with white text, creating a clear selected state.

### Navigation
**`nav-bar`** — A white, full-width bar at 64px height containing the logo, primary navigation links, and utility icons (search, account, cart). Links use `{typography.nav-link}` at 15px weight 600. The active page link is underlined with a 2px orange border and orange text. On scroll, the nav collapses to 56px with a subtle drop shadow (`boxShadow: 0 2px 8px rgba(0,0,0,0.08)`). **`search-bar`** — A pill-shaped input (`{rounded.full}`) with a 2px orange border and a circular orange search icon button nested inside. The input placeholder text is `{colors.muted-soft}` (#2c2c2c).

### Forms
**`text-input`** — Standard input fields with a white background, `{rounded.sm}` corners, and a 1px `{colors.hairline}` border. On focus, the border thickens to 2px and turns orange. **`select-input`** — Dropdown selectors styled identically to text inputs for visual consistency.

### Badges & Chips
**`sale-badge`** — A pink (#ee5f9e) badge with uppercase condensed typography, used to flag discounted items. **`new-badge`** — A lime (#80b800) badge for new arrivals. **`filter-chip`** — Rounded pills (`{rounded.full}`) used in category filter bars. Inactive chips have a white fill with a hairline border; active chips flip to solid orange.

### Footer
**`footer`** — A dark footer (`{colors.ink}`) with white body text and teal (#1f9cd8) links. The footer uses generous padding (48px top, 24px sides and bottom) and contains columns for customer service, company info, and social links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; search bar moves to a collapsible overlay; category cards stack vertically; hero banners reduce padding to 24px; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; nav links become icons-only with labels hidden; search bar shrinks to icon-only trigger; category cards display in a 2xN grid; hero banners use 32px padding |
| Desktop | 1128–1440px | Three-column product grid; full nav links visible; search bar is always expanded; category cards in a horizontal scrollable strip; hero banners at full 48px padding |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; category cards show 5-6 per row; hero banners may include full-bleed background images |

### Touch Targets
- All interactive elements (buttons, links, chips) maintain a minimum 44x44px tap target on mobile.
- Icon buttons in the nav bar are 40x40px on mobile, 36x36px on desktop.
- Filter chips are 36px tall with 16px horizontal padding, exceeding the 44px tap target height requirement when accounting for the 8px gap between chips.

### Collapsing Strategy
- On mobile, the top navigation collapses to a hamburger menu with a slide-out drawer. The search bar collapses to a magnifying glass icon that opens a full-width overlay input.
- The category filter strip collapses to a horizontal scrollable row on tablet and mobile, with a "Filters" button that opens a modal.
- The footer collapses from a 4-column layout on desktop to a single-column accordion on mobile, with expandable sections for each category.
- Product cards switch from a grid to a single-column list on mobile, with larger images and full-width text.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex colors include several that may be checkout-widget colors (e.g., #0073b2, #fa6f22) or social-icon defaults. The brand's true primary (#c74c00) was identified as the most distinctive and frequently used accent, but secondary accent usage (teal, lime, pink) was inferred from the extracted palette and may not reflect the exact brand hierarchy.
- Font-family declarations were limited to system fonts (Arial, Helvetica, Roboto) — no custom brand font was detected. The site may use a web font that wasn't captured in the extraction.
- Hover, focus, and active states for most components (beyond buttons) could not be reliably extracted. The `text-input-focus` state is an educated guess based on the primary color.
- Error styling (form validation, error messages, empty states) was not present in the extracted data.
- Dark mode or high-contrast mode variants were not detected.
- The `star-rating` color (#fac300) was inferred from the extracted marigold — it's a common choice for ratings but may differ on the live site.
- Spacing values and component heights are estimated based on common e-commerce patterns and may not match the exact production values.
