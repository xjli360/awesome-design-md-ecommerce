---
version: alpha
name: "Inside Weather"
source_url: "https://insideweather.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Inside Weather is a direct-to-consumer furniture brand that builds its visual identity around the tension between warm, approachable comfort and sharp, modern precision. The palette is anchored by a deep, almost-black ink (`#222222`) and a clean white canvas (`#fbfbfb`), with a secondary layer of soft grays (`#ebebeb`, `#e8e9eb`, `#e9e9e9`) that create a quiet, residential backdrop. Against this restraint, the brand deploys a single, high-voltage accent — a vivid coral-orange (`#f57e61`) and a bolder red-orange (`#ff3300`) — used sparingly on primary CTAs, sale badges, and key interactive elements. This is not a system that shouts; it whispers with texture. The typography relies on Poppins, a geometric sans-serif with a friendly, open feel, set at moderate weights (400–600) and generous line heights, letting product photography and whitespace carry the emotional weight. Corners are softly rounded (`{rounded.sm}` 8px on buttons, `{rounded.md}` 12px on cards), avoiding the harshness of sharp edges while staying more structured than the pill-shaped friendliness of, say, a marketplace. The overall mood is one of curated calm — a digital showroom that feels like a well-edited apartment, where every element, from the hairline-thin borders (`#d2d5d8`) to the muted secondary text (`#7a7a7a`), is designed to make the furniture the hero. The brand's signature move is the use of a warm, almost greige surface (`#f6f6f7`) for cards and soft surfaces, creating depth without contrast, and a single green accent (`#3ea36a`) for success states or eco-friendly badges, hinting at a sustainability ethos.

colors:
  primary: "#f57e61"
  primary-active: "#ff3300"
  primary-disabled: "#e8e9eb"
  ink: "#222222"
  body: "#31373d"
  muted: "#7a7a7a"
  muted-soft: "#9f9f9f"
  hairline: "#d2d5d8"
  hairline-soft: "#e3e3e3"
  canvas: "#fbfbfb"
  surface-soft: "#f6f6f7"
  surface-card: "#ffffff"
  surface-strong: "#f1f2f3"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-green: "#3ea36a"
  badge-sale: "#ff3300"
  badge-new: "#3ea36a"
  star-rating: "#222222"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
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
    padding: 14px 32px
    height: 48px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.primary-active}"
  text-input-placeholder:
    textColor: "{colors.muted}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline-soft}"
  search-bar-active:
    border: "1px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "top-left"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0"
  swatch-color:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "1px solid {colors.hairline}"
  swatch-color-selected:
    border: "2px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 48px
    padding: "0 {spacing.sm}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 32px
    width: 32px
  star-rating:
    textColor: "{colors.star-rating}"
    fontSize: 16px
    gap: "{spacing.xxs}"
  review-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  review-card-author:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Shop Now", and key conversion points. It uses the brand's coral accent (`{colors.primary}`) on a clean white background (`{colors.on-primary}`), with a soft 8px radius (`{rounded.sm}`) that feels approachable without being overly pill-shaped. On hover, it shifts to the more intense red-orange (`{colors.primary-active}`), and in its disabled state it fades to a light gray (`{colors.primary-disabled}`) with muted text, signaling non-interactivity.

**`button-secondary`** — A bordered alternative for less prominent actions, such as "Learn More" or "View Details". It sits on the white canvas (`{colors.canvas}`) with a thin hairline border (`{colors.hairline}`) and dark ink text (`{colors.ink}`). On active state, the border thickens to the full ink color, and the background takes on the soft surface tone (`{colors.surface-soft}`).

**`button-tertiary-text`** — A text-only button for inline actions like "Clear Filters" or "Cancel". It has no background or border, relying solely on the ink color and the button typography to communicate interactivity.

**`button-pill-primary`** — A fully rounded variant (`{rounded.full}`) used for promotional badges, sale tags, or compact CTAs in hero sections. It uses the same coral background but with smaller padding and font size, making it feel like a sticker or tag.

**`button-pill-outline`** — The outlined counterpart to the pill button, used for secondary promotional elements or filter tags. It has a white background and a thin hairline border, keeping it visually light.

### Cards
**`product-card`** — The core product display unit, used on collection pages and search results. It has a white background (`{colors.canvas}`) and a 12px rounded corner (`{rounded.md}`), creating a subtle card-like separation from the page. The image area is rounded at the top, while the title and price sit below with consistent padding. A badge can be overlaid on the top-left corner for sale or new items.

**`review-card`** — A bordered card for customer testimonials and product reviews. It uses a 1px hairline-soft border (`{colors.hairline-soft}`) and 12px radius, with the author name set in muted caption style. The layout is simple, with the star rating and review text flowing vertically.

### Navigation
**`nav-bar`** — The top-level site navigation, fixed at 72px height with a white background and a subtle bottom border (`{colors.hairline-soft}`). Navigation links are set in uppercase Poppins at 14px weight 500, with the active link underlined by a 2px ink-colored border. Inactive links are muted (`{colors.muted}`) to reduce visual noise.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a soft gray background (`{colors.surface-soft}`) and a thin border. On focus, the border switches to the full ink color, providing clear active state feedback. It sits at 44px height, compact enough for the nav bar but large enough for comfortable tapping.

### Forms
**`text-input`** — Standard text input for forms like checkout, account creation, and contact pages. It has a white background, 8px radius, and a 1px hairline border. On focus, the border becomes ink-colored, and on error it switches to the red-orange (`{colors.primary-active}`). Placeholder text uses the muted gray (`{colors.muted}`).

**`select-dropdown`** — A dropdown selector for options like size, color, or quantity. It mirrors the text-input styling but includes a custom arrow indicator (not specified here). The height and padding match the text input for visual consistency.

**`quantity-selector`** — A compact, bordered control for adjusting item quantities. It has two square buttons on either side (minus and plus) and a central numeric display. The buttons are transparent with a subtle hover state, and the whole component is 48px tall to match other form elements.

### Badges
**`badge-new`** — A small, green (`{colors.badge-new}`) badge for marking newly added products or collections. It uses uppercase 11px font with 0.5px letter spacing and a 4px radius, making it feel like a tag or sticker.

**`badge-sale`** — A red-orange (`{colors.badge-sale}`) badge for sale or discounted items. It shares the same typography and radius as the new badge, ensuring visual consistency across badge types.

**`badge-out-of-stock`** — A neutral gray badge for out-of-stock items. It uses the strong surface background (`{colors.surface-strong}`) and muted text, signaling unavailability without drawing attention.

### Hero
**`hero-banner`** — The full-width hero section on the homepage and key landing pages. It has a soft gray background (`{colors.surface-soft}`) and large display typography, with generous padding (`{spacing.section}`) top and bottom. A primary CTA button sits within the hero, using the standard button-primary styling. The minimum height is 400px to ensure visual impact.

### Footer
**`footer`** — The site footer, inverted with a dark ink background (`{colors.ink}`) and white text. Links are set in muted-soft gray (`{colors.muted-soft}`) and transition to white on hover. The layout uses xxl padding for breathing room, creating a clear visual end to the page.

### Accordion
**`accordion`** — A vertically stacked disclosure component used for FAQs, product details, and shipping information. Each item has a bottom border (`{colors.hairline-soft}`) for separation, with a clickable header and expandable content area. The header uses title-sm typography, while the content uses body-sm with muted body color.

### Swatches
**`swatch-color`** — A circular color swatch (32px diameter) used for product color options. It has a thin hairline border and a 2px ink border when selected, providing clear visual feedback for the active option.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, nav collapses to hamburger menu, hero banner reduces to 300px min-height, product cards stack vertically, search bar moves to full-width below nav, buttons become full-width, accordion remains default, footer links stack in single column |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but compact, hero banner at 400px min-height, product cards in 2-column grid, search bar in nav, buttons remain inline, footer links in 2-column layout |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, hero banner at 400px min-height, product cards in 3-column grid, search bar in nav, buttons inline, footer links in 4-column layout |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, hero banner at 450px min-height, product cards in 4-column grid, all elements maintain desktop behavior with increased whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum height of 44px for comfortable tapping on mobile.
- Swatch colors are 32px diameter, with 8px touch extension on mobile for easier selection.
- Quantity selector buttons are 32px square, with 12px padding around them for touch accuracy.
- Nav bar links have 48px tap targets on mobile, even if the text is smaller.
- Accordion headers have 48px tap targets for easy expansion.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu, with the logo centered and the cart icon remaining visible.
- The product grid collapses from 4 columns on wide to 1 column on mobile, with images scaling to full width.
- The hero banner reduces its min-height and stacks the CTA below the headline text.
- The footer collapses from a 4-column layout to a single column, with accordion-style sections for link groups.
- Search bar moves from the nav to a full-width element below the nav on mobile, with a persistent search icon in the nav bar.
- Product filters collapse into a slide-out drawer on mobile, rather than a persistent sidebar.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (e.g., nav links, footer links, accordion headers) could not be reliably extracted from the live site and are inferred from common patterns.
- Error styling for form inputs (e.g., validation messages, error icons) is not fully documented and may vary.
- Dark mode or high-contrast mode variants are not present in the extracted data.
- The exact font weights for Poppins (e.g., 300, 400, 500, 600, 700) are assumed based on common usage; the site may use additional weights.
- Sub-brand or seasonal color palettes (e.g., holiday, collaboration) are not captured.
- Animation and transition durations (e.g., button hover, card lift) are not specified.
- The exact spacing for product card image aspect ratios and grid gaps is inferred from common e-commerce patterns.
- The `textTransform: uppercase` on nav-link and badge is inferred from common DTC furniture brand patterns; the actual site may use mixed case.
- The `border` property on components like button-secondary and text-input is assumed to be `1px solid`; the actual stroke width may vary.
