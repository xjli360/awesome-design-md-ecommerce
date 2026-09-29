---
version: alpha
name: "Honey-Can-Do"
source_url: "https://www.honeycando.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Honey-Can-Do is a brand built on the quiet confidence of organization — not sterile minimalism, but a warm, approachable clarity that makes tidying feel achievable. The palette is anchored by a deep teal `#12465b` and a vibrant sea-green `#108474`, which together evoke a sense of calm, natural order — think of a well-kept pantry or a tidy linen closet. These primary hues are supported by a soft, extensive neutral system: a warm off-white canvas (`#f9fafb`), a slightly cooler surface (`#f2f2f2`), and a range of grays from `#eeeeee` to `#333333` that provide depth without harshness. A bright, optimistic yellow `#fbcd0a` acts as a signature accent, used for badges, sale tags, and other moments of delight. The brand’s typography leans on a mix of `Montserrat` and `Nunito Sans`, with `Jost` appearing as a display accent — all humanist sans-serifs that feel friendly and legible at every size. Rounded corners are generous but not cartoonish: buttons use `{rounded.sm}` (8px), cards use `{rounded.md}` (12px), and the search bar uses `{rounded.full}`, creating a tactile, approachable interface. The overall mood is one of gentle authority — Honey-Can-Do doesn’t shout, it simply makes the right choice the easy one.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#c1e6e6"
  ink: "#333333"
  body: "#555555"
  muted: "#666666"
  muted-soft: "#888888"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fbcd0a"
  accent-red: "#dc143c"
  accent-blue: "#007497"
  accent-blue-light: "#1990c6"
  accent-blue-dark: "#136f99"
  accent-purple: "#a89cc8"
  accent-teal: "#12465b"
  accent-teal-light: "#edf5f5"
  star-rating: "#ffff00"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
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
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    margin-top: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    margin-top: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    margin-top: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  category-card-image:
    rounded: "{rounded.md}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: "16px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Shop Now", and checkout flows. It uses a solid `{colors.primary}` fill with white text and `{rounded.sm}` corners. On hover, it transitions to `{colors.primary-active}`. The disabled state uses `{colors.primary-disabled}` with `{colors.muted}` text to signal inactivity.
**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Learn More". It has a transparent background, `{colors.primary}` text, and a 2px solid border in the same teal. On active state, it fills with `{colors.primary}` and inverts the text to white.
**`button-tertiary`** — A text-only button for less prominent actions, such as "Cancel" or "Clear Filters". It has no background or border, relying solely on `{colors.primary}` text color for affordance.
**`button-accent-yellow`** — A high-energy variant reserved for promotional CTAs, such as "Sale" banners or limited-time offers. It uses `{colors.accent-yellow}` as a background with dark `{colors.ink}` text, creating a strong contrast that draws the eye.

### Cards
**`product-card`** — The primary container for product listings on collection and search pages. It has a white `{colors.surface-card}` background, `{rounded.md}` corners, and 16px internal padding. The product image sits at the top with its own `{rounded.md}` treatment, followed by the title in `{typography.title-sm}` and the price in `{typography.price}`. Cards are typically arranged in a responsive grid with `{spacing.base}` gaps.
**`category-card`** — Used for browsing product categories on the homepage or navigation. It features a white background, `{rounded.md}` corners, and generous `{spacing.lg}` padding. A category image or icon is centered above the category name, which is set in `{typography.title-sm}`.

### Navigation
**`nav-bar`** — The persistent top navigation bar, 64px tall with a white `{colors.canvas}` background. It contains the brand logo, primary navigation links set in `{typography.nav-link}`, a search icon, and a cart icon. The active link state uses `{colors.primary}` text color to indicate the current page.
**`nav-link`** — Individual navigation items styled with `{typography.nav-link}`. On hover, the text color transitions to `{colors.primary}`. There is no underline or background change — the brand relies on color shift and spacing for feedback.

### Forms
**`text-input`** — Standard single-line text input for forms like search, newsletter signup, and checkout. It has a white background, `{colors.hairline}` border, `{rounded.sm}` corners, and 12px vertical padding. On focus, the border thickens to 2px and changes to `{colors.primary}`. Error state uses a 2px `{colors.accent-red}` border.
**`select-input`** — A dropdown selector styled consistently with `text-input`, using the same dimensions, border, and corner radius. The chevron icon is typically rendered as a background SVG.
**`quantity-selector`** — A compact input for adjusting item quantities in the cart. It has a white background, `{colors.hairline}` border, `{rounded.sm}` corners, and contains a minus button, the current quantity, and a plus button.

### Badges
**`badge-sale`** — A small, high-contrast badge used to flag discounted items. It uses a `{colors.accent-red}` background with white text, `{rounded.xs}` corners, and `{typography.badge}` styling. It is typically positioned in the top-left corner of a product card image.
**`badge-new`** — A badge for new arrivals, using `{colors.primary}` as the background. It follows the same sizing and typography as `badge-sale`.
**`badge-sale-yellow`** — An alternative sale badge using `{colors.accent-yellow}` with dark `{colors.ink}` text. This is used in contexts where the red badge might clash, such as on hero banners or promotional sections.

### Hero
**`hero-banner`** — A full-width promotional section typically found at the top of the homepage. It uses a `{colors.accent-teal}` background with white text, `{typography.display-lg}` for the headline, and generous `{spacing.section}` vertical padding. A single `hero-banner-cta` button in `{colors.accent-yellow}` is centered below the headline to drive traffic to a featured collection.

### Footer
**`footer`** — The site-wide footer, using the same `{colors.accent-teal}` background as the hero for visual consistency. It contains multiple columns of links, social media icons, and a copyright notice. All text is white, with links styled as `{typography.link}`. The footer has `{spacing.section}` vertical padding.

### Accordion
**`accordion-header`** — A clickable header for expandable content sections, such as product descriptions or FAQ items. It has a `{colors.surface-soft}` background, `{typography.title-sm}` text, and `{rounded.sm}` corners. The header includes a chevron icon that rotates on open.
**`accordion-content`** — The expandable panel below an accordion header. It has a white `{colors.canvas}` background and `{colors.body}` text in `{typography.body-md}`. Content padding is `{spacing.base}` on all sides.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces nav links, hero banner reduces to 2/3 height, search bar collapses to icon-only, footer links stack vertically |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but condensed, hero banner at full height, search bar is full-width but below the nav, footer links in two columns |
| Desktop | 1128–1440px | Three-column product grid, full nav bar with all links, hero banner at full height with larger typography, search bar in the nav, footer links in four columns |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, hero banner may include a secondary CTA, all elements use maximum spacing |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet accessibility guidelines.
- Icon-only buttons (e.g., search, cart, hamburger menu) are at least 44x44px with adequate padding.
- Product card tap targets (title, image, add-to-cart) are separated by at least 8px to prevent mis-taps.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu. The search bar becomes an icon that opens a full-screen overlay.
- The product grid collapses from 4 columns on wide screens to 1 column on mobile.
- The footer link columns collapse from 4 on desktop to 1 on mobile, stacking vertically.
- Hero banner content (headline, subtext, CTA) stacks vertically on mobile, with reduced font sizes and padding.
- Accordion sections are always collapsed by default on mobile to save vertical space.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (e.g., product cards, category cards, footer links) could not be reliably extracted from the live site. These should be defined with subtle color shifts or underlines.
- Error styling for forms (e.g., validation messages, error icons) was not observed. A standard pattern using `{colors.accent-red}` for borders and text is assumed.
- Dark mode is not currently supported. All tokens assume a light theme.
- Sub-brand or seasonal palettes (e.g., holiday collections) were not observed. The current palette is the core system.
- The exact font weights for `Montserrat` and `Nunito Sans` in use across all typography levels could not be fully verified. The weights listed are best estimates based on common usage.
- Animation and transition durations (e.g., button hover, accordion expand) were not extracted. A standard 200-300ms ease-in-out is recommended.
- The star rating component's exact size and spacing could not be confirmed. The `{colors.star-rating}` value of `#ffff00` is a placeholder based on extracted data.
- The `Jost` font family was found in the CSS but its specific usage (e.g., display headlines, logos) could not be determined. It is not included in the primary typography stack.
