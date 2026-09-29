---
version: alpha
name: "Newbury Comics"
source_url: "https://www.newburycomics.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A black-and-white punk energy runs through Newbury Comics, where `#121212` ink and `#eeeeee` canvas create a high-contrast grid that refuses to be quiet. The brand lives in the gap between a record store's chaotic wall of vinyl and a clean e‑commerce shelf — product thumbnails sit on `#dedede` soft surfaces with `{rounded.sm}` corners, while the top nav and footer clamp down in solid black. There is no gradient, no pastel, no decorative illustration; the only color comes from the album art, movie posters, and Funko Pop boxes that fill every card. The meta theme-color is `#000000`, a browser‑chrome commitment to darkness that signals "this is not a toy store." Buttons are flat black rectangles with white type — no pill shapes, no rounded warmth — and the search bar is a simple outlined field, not a friendly orb. The typography stack is conspicuously absent from extracted CSS beyond Font Awesome icons, suggesting a lean system‑font fallback or a Shopify‑theme default that hasn't been customized. The result is a storefront that feels like a basement show: raw, loud, and built for the hunt, not the browse.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#555555"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#cc0000"
  accent-yellow: "#ffcc00"
  badge-sale: "#cc0000"
  badge-new: "#121212"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.25px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
    color: "{colors.accent-red}"

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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    padding: 4px 0
  button-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 44px
    width: 44px
  top-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  top-nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    padding: "4px 0"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "10px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "10px 20px"
    height: 40px
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 32px 8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    padding: "0 4px"

## Components

### Buttons
**`button-primary`** — A flat black rectangle with white uppercase type. No border radius, no shadow, no hover lift. On hover, the background deepens to `#000000`. The disabled state uses `#555555` to signal inactivity without introducing a secondary color. Used for "Add to Cart," "Checkout," and primary form submissions.

**`button-secondary`** — An outlined variant with a 2px black border on a white background. On hover, the fill inverts to solid black. Used for "View Details," "Pre-Order," and secondary calls to action where the primary button is already present.

**`button-text-link`** — A plain text button with no background or border, styled as a standard link. Used for "Cancel," "Clear Filters," and inline actions within product cards.

**`button-icon`** — A 44x44px square icon button with no background. Used for cart, account, and search icons in the top nav. The size matches the minimum touch target recommendation.

### Navigation
**`top-nav`** — A solid black bar spanning the full viewport width at 56px height. Contains the brand logo, navigation links, and icon buttons. The background is `#121212` with white text. Links have 8px vertical padding and 12px horizontal padding. The active link is underlined with a 2px white border.

**`top-nav-link`** — White text on black background with no hover background change. The active state adds a bottom border underline. No dropdown indicators or chevrons — the nav is flat and direct.

### Cards
**`product-card`** — A white card with `{rounded.sm}` (4px) corners and 8px padding. The product image sits in a `{rounded.xs}` (2px) container on a `#eeeeee` background, maintaining a 1:1 aspect ratio. The title uses `{typography.title-md}` and the price uses `{typography.price}` with 8px and 4px top margins respectively. Sale badges appear as small red rectangles with white uppercase text.

**`product-card-badge`** — A small rectangular badge with `#cc0000` background and white uppercase text. Used for "SALE," "NEW," or "EXCLUSIVE" labels. Positioned absolutely over the top-left corner of the product image.

### Forms
**`search-bar`** — A simple outlined input field with no border radius. The default state has a 1px `#dedede` border. On focus, the border thickens to 2px and turns black. The input height is 40px with 8px vertical and 12px horizontal padding.

**`newsletter-input`** — Matches the search bar styling but sits within the footer context. Paired with a `newsletter-submit` button that is a flat black rectangle with white uppercase type.

**`filter-dropdown`** — A standard select dropdown with a 1px `#dedede` border, no border radius, and 40px height. The text uses `{typography.body-sm}`. Right padding is 32px to accommodate a custom dropdown arrow.

### Footer
**`footer`** — A solid black section with `{spacing.section}` vertical padding and `{spacing.lg}` horizontal padding. Links are white with no underline until hover. The newsletter signup form sits prominently in the footer, with the input and submit button side by side.

**`footer-link`** — White text on black background with 4px vertical padding. No underline in default state. On hover, an underline appears.

### Breadcrumbs
**`breadcrumb`** — Small gray text (`#666666`) used for navigation hierarchy. Links within breadcrumbs are black (`#121212`). Separators are lighter gray (`#999999`) with 4px horizontal padding. Used on collection and product pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu. Product grid goes to 2 columns. Filter dropdowns stack vertically. Footer links stack in a single column. Search bar moves to a full-width row below the nav. |
| Tablet | 744–1128px | Top nav shows limited links (3-4). Product grid uses 3 columns. Filter dropdowns remain inline but narrower. Footer links in 2 columns. |
| Desktop | 1128–1440px | Full top nav with all links visible. Product grid uses 4 columns. Filters in a horizontal bar above products. Footer links in 3 columns. |
| Wide | > 1440px | Maximum content width of 1440px centered. Product grid uses 5 columns. Additional whitespace on sides. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px.
- Icon buttons are 44x44px squares.
- Product card tap targets include the entire card, not just the title or price.
- Filter dropdowns and search inputs are 40px tall — slightly below the 44px recommendation but acceptable for text inputs.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu on mobile, revealing a full-screen overlay with all links.
- The product grid collapses from 5 columns on wide screens to 2 columns on mobile.
- Filter options collapse into a single "Filter" button on mobile that opens a slide-out panel.
- The footer collapses from 3 columns to a single column on mobile.
- The search bar collapses from a visible input on desktop to a search icon that expands on tap on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font family was extractable from the live site. The typography block uses system font fallbacks. The brand may use a custom typeface that is loaded via JavaScript or a Shopify theme setting not visible in extracted CSS.
- Hover and focus states for most components are inferred from common patterns — actual extracted hover colors were not available.
- Error states for form inputs (validation errors, required field indicators) were not observed.
- Dark mode is not supported — the brand uses a white canvas with black text exclusively.
- The extracted color palette is limited to three grayscale values (`#eeeeee`, `#dedede`, `#121212`) plus white and black. The brand may use accent colors for seasonal promotions or specific product categories that were not present in the extracted data.
- The `accent-red` and `accent-yellow` tokens are speculative — red is commonly used for sale badges in e-commerce, and yellow may appear in the brand's logo or promotional banners.
- Loading states, skeleton screens, and empty states were not documented.
- The newsletter form's success and error states are unknown.
- Mobile navigation overlay animation timing and behavior are not specified.
- Product card hover states (image zoom, shadow lift) are not confirmed from extracted data.
- The brand's logo is not represented in the design system — it may be an image or SVG with specific sizing and spacing requirements.
- Checkout flow components (cart drawer, checkout button, shipping form) are not included as they are typically handled by Shopify's default checkout.
