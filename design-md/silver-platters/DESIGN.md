---
version: alpha
name: "Silver Platters"
source_url: "https://www.silverplatters.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A single warm gray (#eeeeee) sets the tone for Silver Platters — a Seattle-based media emporium that has been selling vinyl, CDs, movies, and gear since 1983. The brand's digital presence mirrors its physical stores: utilitarian, browsable, and unpretentious, with a near-monochrome palette that lets product photography and album art supply all the color. There is no hero gradient, no brand illustration system, no signature accent hue — just a clean white canvas (`{colors.canvas}`), soft gray surfaces (`{colors.surface-soft}`), and a hairline border (`{colors.hairline}`) that separates content zones with the subtlety of a record sleeve's inner seam. Typography relies on system-level icon fonts (Font Awesome 5 Brands, Font Awesome 5 Free) for navigation affordances and a custom spruce-icon-pack for category icons, suggesting a pragmatic approach to UI: use what works, don't over-engineer. Buttons use the full pill shape (`{rounded.full}`) for primary actions, while secondary controls and input fields default to a softer 8px radius (`{rounded.sm}`). The overall impression is that of a well-organized record store's website — built for scanning, not for lingering. The extracted palette yields only one distinctive hex (#eeeeee), which functions as the brand's primary surface tone rather than a traditional brand color; there is no primary-action color in the extracted data, meaning the site likely relies on black text on white backgrounds for CTAs, or the primary color is embedded in images rather than CSS. This is a design system built on restraint — or on the absence of a formal system — where the product is the hero and the interface steps back.

colors:
  primary: "#eeeeee"
  primary-active: "#cccccc"
  primary-disabled: "#f5f5f5"
  ink: "#222222"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#222222"
  on-dark: "#ffffff"
  link: "#0066cc"
  link-visited: "#551a8b"
  star-rating: "#f5a623"
  sale-badge: "#cc0000"
  out-of-stock: "#999999"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
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
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.link}"
    padding: 4px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.sale-badge}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 4px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-out-of-stock:
    backgroundColor: "{colors.out-of-stock}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  category-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "6px 0"
    borderBottom: "1px solid transparent"
  category-link-active:
    textColor: "{colors.ink}"
    fontWeight: 600
    borderBottom: "2px solid {colors.ink}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.ink}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.ink}"
  breadcrumb-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "4px 0"
  breadcrumb-link-hover:
    textColor: "{colors.link}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} 0"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "4px 0"
  footer-link-hover:
    textColor: "{colors.link}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action uses a full pill shape (`{rounded.full}`) with the brand's warm gray surface (`{colors.primary}`) and dark text (`{colors.on-primary}`). On hover/active, the background darkens to `{colors.primary-active}` (#cccccc). Disabled state uses a lighter gray (`{colors.primary-disabled}`) with muted text, signaling non-interactivity without harsh contrast. Padding of 12px 24px and 44px height keep the button substantial but not oversized.

**`button-secondary`** — An outlined variant with white background, dark text, and a 1px hairline border. On hover, the background shifts to `{colors.surface-soft}`. This button is used for less prominent actions like "Clear Filters" or "Cancel". The 11px 23px padding accounts for the 1px border to maintain equal 44px height with the primary button.

**`button-link`** — A text-only button styled as a hyperlink, used for inline actions like "View Details" or "See More". No background, no border — just the link blue (`{colors.link}`) and standard link typography. Hover state adds underline (not specified in tokens but standard behavior).

### Text Inputs
**`text-input`** — Standard form input with white background, 1px hairline border, and 8px corner radius. Focus state swaps the border to `{colors.ink}` for clear keyboard focus indication. Error state uses `{colors.sale-badge}` red border. Padding of 10px 14px provides comfortable typing space within the 44px height.

**`select-input`** — Dropdown selector matching the text input's dimensions and border style. The chevron icon is assumed to be provided by the spruce-icon-pack or Font Awesome.

### Navigation
**`nav-bar`** — A 56px fixed-height top bar with white background and a subtle bottom hairline. The sticky variant adds a light box-shadow (`0 2px 4px rgba(0,0,0,0.08)`) when scrolled. Navigation links use 14px semibold type with 8px 12px padding for comfortable tap targets.

**`nav-link`** — Inline navigation items with transparent background. Active state uses `{colors.surface-soft}` background with `{rounded.sm}` to create a subtle "pill" indicator. This avoids the need for an underline or bottom-border pattern.

### Product Cards
**`product-card`** — The core content unit, a white card with soft hairline border and 8px rounded corners. On hover, it gains a subtle shadow (`0 4px 12px rgba(0,0,0,0.08)`) and a slightly stronger border. The image area uses a 1:1 aspect ratio with 4px rounding. Title sits below at 14px semibold, price at 14px regular in muted gray.

**`product-card-sale-badge`** — A small red badge (`{colors.sale-badge}`) with white uppercase text, 4px rounding, and 2px 6px padding. Positioned absolutely over the top-left of the product image.

**`product-card-out-of-stock`** — A gray badge (`{colors.out-of-stock}`) indicating unavailable items. Same dimensions as the sale badge but communicates a different state.

### Filters & Categories
**`filter-chip`** — Pill-shaped toggle buttons for category and price-range filtering. Default state is a soft gray background with hairline border. Active state inverts to dark background with white text, making selected filters immediately visible in a list.

**`category-link`** — Sidebar or dropdown category links with transparent background. Active state uses a 2px bottom border in `{colors.ink}` — a classic e-commerce pattern for indicating the current department.

### Pagination
**`pagination-button`** — Numbered page buttons with white background and hairline border. Active page uses inverted colors (dark background, white text). Padding of 8px 12px creates square-ish buttons that are easy to tap.

### Footer
**`footer-section`** — A soft gray (`{colors.surface-soft}`) footer area with a top hairline separator. Links use caption-size type in muted gray, switching to link blue on hover. The section padding of 32px top and bottom provides breathing room for multiple link columns.

### Icon Buttons
**`icon-button`** — Circular 36px buttons with transparent background, used for cart, account, and search icons. On hover, a soft gray background appears. The full pill radius (`{rounded.full}`) ensures a perfect circle.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items per row). Nav bar collapses to hamburger menu. Search bar moves to a full-width overlay. Filter sidebar becomes a bottom sheet or accordion. Footer stacks vertically. Product card padding reduces to 8px. |
| Tablet | 744–1128px | Two-column product grid. Nav bar shows top-level categories as text links with a "More" dropdown. Filter sidebar appears as a collapsible left panel (280px). Footer uses 2-3 columns. |
| Desktop | 1128–1440px | Three-column product grid. Full nav bar with all categories visible. Persistent left filter sidebar (280px). Footer uses 4 columns. Product cards show hover shadow effects. |
| Wide | > 1440px | Four-column product grid. Max-width container (1440px) centered. Additional whitespace on sides. Filter sidebar remains 280px. |

### Touch Targets
- All interactive elements (buttons, links, chips) maintain minimum 44px height for touch accessibility.
- Icon buttons are 36px minimum (slightly below the 44px ideal but standard for icon-only controls).
- Filter chips use 6px 14px padding within a 44px height to ensure comfortable tapping.
- Product card links (title, image) have implicit tap targets through the card's clickable area.
- Pagination buttons are 36px+ with adequate spacing between them.

### Collapsing Strategy
- **Mobile (< 744px):** Nav bar collapses to a hamburger icon. Search bar becomes a full-screen overlay triggered by a search icon. Filter sidebar collapses to a "Filters" button that opens a bottom sheet or modal. Footer collapses to a single column with accordion sections for link groups. Product grid switches to 1-2 columns.
- **Tablet (744–1128px):** Nav bar shows primary categories as text links; secondary categories go into a "More" dropdown. Filter sidebar is collapsible (shown/hidden via toggle). Footer uses 2-3 columns.
- **Desktop (1128–1440px):** Full nav bar visible. Filter sidebar is persistent. Footer uses 4 columns.
- **Wide (> 1440px):** Content is constrained to a max-width container. No further collapsing; whitespace increases.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Primary brand color:** Only one hex (#eeeeee) was extracted from the live site. This appears to be a surface/background color, not a traditional brand-primary-action color. The actual CTA color (likely black, dark gray, or blue) could not be determined from the extracted data. The `primary` token above uses #eeeeee as the most distinctive extracted color, but this should be validated against the actual site's buttons and links.
- **Font family:** No standard web-safe font family was extracted. The site uses Font Awesome and spruce-icon-pack for icons, but the body text font family is unknown. The typography block uses Helvetica Neue as a reasonable sans-serif default for a media retailer, but this is an assumption.
- **Hover states:** Only a few hover states could be inferred from common patterns. Most interactive hover states (links, buttons, cards) are assumed based on e-commerce conventions rather than extracted data.
- **Error states:** Form validation styling (error messages, success states, required field indicators) is not present in the extracted data. The error border color for text inputs is assumed.
- **Dark mode:** No evidence of dark mode support in the extracted data.
- **Sub-brand palettes:** Silver Platters may have sub-brands or seasonal color schemes (e.g., for vinyl, CDs, movies) that are not captured in the extracted data.
- **Animation/transition:** No timing, easing, or animation tokens could be extracted. Hover transitions are assumed to use a standard 200ms ease.
- **Spacing scale:** The spacing tokens are based on common e-commerce patterns (8px grid) rather than extracted values. The actual spacing on the site may differ.
- **Icon system:** While Font Awesome and spruce-icon-pack are referenced, the specific icon set, sizes, and usage guidelines are unknown.
- **Rating/star display:** The star-rating color (#f5a623) is a common gold for ratings but was not extracted from the site. It's included as a reasonable default for a media retailer that likely has reviews.
- **Sale/price badges:** The sale-badge red (#cc0000) and out-of-stock gray (#999999) are assumed based on common e-commerce patterns, not extracted data.
