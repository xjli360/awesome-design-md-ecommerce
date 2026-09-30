---
version: alpha
name: "Boll & Branch"
source_url: "https://www.bollandbranch.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Boll & Branch is a luxury bedding brand that wraps you in quiet, organic comfort. The palette is anchored by a warm off-white canvas (`#fffefb`) and a deep, almost-charcoal ink (`#1d1d1c`), with soft greige and stone tones (`#787573`, `#616161`, `#d9d9d6`) that create a serene, tactile atmosphere. A restrained accent of dusty rose (`#bd2828`) appears sparingly, like a single thread of color in an otherwise neutral weave. The brand’s typography pairs the refined, serif elegance of Louize with the clean, modern utility of Fakt, a mix that feels both heirloom and contemporary. Signature design moves include generous white space, soft rectangular cards with `{rounded.sm}` corners, and a persistent sense of air and light — nothing feels crowded or loud. The overall effect is one of considered simplicity: a digital space that feels as calm and high-quality as the organic cotton sheets it sells.

colors:
  primary: "#1d1d1c"
  primary-active: "#45351b"
  primary-disabled: "#d9d9d6"
  ink: "#1d1d1c"
  body: "#616161"
  muted: "#787573"
  muted-soft: "#c8c8c8"
  hairline: "#d9d9d6"
  hairline-soft: "#edede9"
  canvas: "#fffefb"
  surface-soft: "#f9f8f3"
  surface-card: "#ffffff"
  on-primary: "#fffefb"
  accent-rose: "#bd2828"
  accent-gold: "#b78c47"
  accent-sand: "#ebe1d5"
  accent-stone: "#7d7364"
  accent-navy: "#2e344a"
  star-rating: "#b78c47"
  badge-new: "#bd2828"
  badge-sale: "#bd2828"
  scrim: "#1d1d1c"

typography:
  display-xl:
    fontFamily: "'Louize', 'Georgia', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Louize', 'Georgia', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Louize', 'Georgia', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Fakt', 'Arial', sans-serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Fakt', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Fakt', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Fakt', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Fakt', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Fakt', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Fakt', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Fakt', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Fakt', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Fakt', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Fakt', 'Arial', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-rose}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
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
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    marginTop: "{spacing.xxs}"
  product-card-rating:
    color: "{colors.star-rating}"
    fontSize: 12px
    marginTop: "{spacing.xs}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.3
  badge:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
    textDecoration: "underline"
  footer-link-hover:
    color: "{colors.accent-gold}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    width: 40px
    height: 40px
  color-swatch:
    rounded: "{rounded.full}"
    width: 32px
    height: 32px
    border: "2px solid transparent"
  color-swatch-selected:
    border: "2px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a solid rectangle in the brand's deep ink (`#1d1d1c`) with white text. It uses the uppercase, letter-spaced Fakt button typography and has no border radius, giving it a crisp, tailored feel. On hover, the background shifts to a warm brown (`#45351b`). The disabled state fades to a light greige (`#d9d9d6`) with muted text.
**`button-secondary`** — An outlined variant with a transparent background and a 1px solid ink border. It shares the same uppercase Fakt typography and zero border radius, but the background fills with ink on hover, inverting the text color. This is used for less prominent actions like "View Details" or "Learn More."
**`button-tertiary`** — A text-only button with no background or border, used for inline actions like "Cancel" or "Clear." It maintains the uppercase Fakt typography and sits flush against its container, relying on hover underline for affordance.
**`button-pill`** — A smaller, fully rounded button used for filters, tags, or quick-select options. It uses the smaller uppercase Fakt typography and `{rounded.full}` for a friendly, tactile shape. The background is ink, with white text.

### Cards
**`product-card`** — The primary product display unit on listing pages. It has a white background, no border radius, and a 1:1 aspect ratio image. Below the image, the product title appears in `{typography.title-sm}`, the price in `{typography.body-sm}` with muted color, and an optional star rating in gold (`#b78c47`). There is no shadow or border — the card relies on generous spacing and the image itself for hierarchy.
**`hero-banner`** — A full-width, large-format hero used on the homepage and collection pages. It has a soft off-white background (`#f9f8f3`) and uses the serif Louize display typography for the headline. A subtle dark scrim overlay can be applied when text sits on a photography background. The minimum height is 400px, with generous padding on all sides.

### Navigation
**`nav-bar`** — The top-level site navigation, fixed at 72px height with a white background and a thin bottom border in `{colors.hairline-soft}`. Links use uppercase Fakt at 14px with 0.3px letter spacing. The active link is indicated by a 2px bottom border in ink. The nav includes a logo, primary links (Sheets, Towels, Bedding, etc.), a search icon, and a cart icon.
**`nav-link-active`** — The active state for a top-level navigation link, distinguished by a 2px solid bottom border in the primary ink color.
**`nav-link-inactive`** — The default state for navigation links, rendered in the muted stone color (`#787573`).

### Forms
**`text-input`** — A standard text input field with a white background, 1px hairline border, and zero border radius. It uses the body Fakt typography at 16px. On focus, the border changes to the primary ink color. Error states use a rose border (`#bd2828`). The input height is 48px with 12px horizontal padding.
**`quantity-selector`** — A compact, two-button control for adjusting product quantities. It has a 1px hairline border, zero border radius, and 40px height. The increment/decrement buttons sit on a soft surface background (`#f9f8f3`) and are 40px square.

### Footer
**`footer`** — The site footer is a full-width block with a deep ink background (`#1d1d1c`) and white text. Links are underlined and turn gold (`#b78c47`) on hover. The footer contains columns for customer service, the brand story, and social links, with generous vertical padding.

### Badges
**`badge`** — A small, inline label used for sale or new-arrival indicators. It has a rose background (`#bd2828`), white text, zero border radius, and uses the smallest uppercase Fakt typography. The gold variant (`#b78c47`) is reserved for "New" badges.
**`color-swatch`** — A circular swatch for selecting product colors. It is 32px in diameter with a full border radius. The selected state is indicated by a 2px solid ink border. Unselected swatches have a transparent border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero banner reduces to 300px min-height; footer links stack; typography scales down one step (display-xl becomes 32px). |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but reduced font size; hero banner at 400px; side-by-side layout for product details; footer columns in a 2x2 grid. |
| Desktop | 1128–1440px | Full three- or four-column product grid; expanded nav with all links; hero banner at 500px; standard layout for product details with image gallery and description side by side. |
| Wide | > 1440px | Max-width container (1440px) centered; extra whitespace on sides; hero banner can extend to 600px; product grid can show 5 columns for certain categories. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px and minimum width of 44px to meet WCAG touch target guidelines.
- Color swatches are 32px, but the tap area extends to 44px via invisible padding.
- Quantity selector buttons are 40px, which is below the 44px recommendation; this is a known gap.
- Nav links have a 72px tap area due to the nav bar height.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer.
- The product filter sidebar collapses into a dropdown or modal on mobile.
- The footer's multi-column layout collapses into a single column on mobile, with accordion-style sections for each column.
- The hero banner's text overlay collapses to a smaller size, and the image may be cropped to a 4:5 aspect ratio.
- Product image galleries collapse from a thumbnail strip to a swipeable carousel.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links were inferred from the brand's aesthetic; exact color values for hover (e.g., `button-secondary` hover background) were not extracted from the live site.
- Error styling for form inputs (error message typography, iconography) was not reliably extracted.
- Sub-brand palettes (e.g., for "Boll & Branch x [Collaborator]") were not identified.
- Dark mode tokens are not present; the brand does not appear to support a dark mode.
- Animation and transition timing values (ease, duration) were not extracted.
- Specific font weights for Louize and Fakt were inferred from common usage; exact weight values may vary.
- The `star-rating` color was inferred from product card hints; the exact hex value for the star icon fill was not extracted.
- The `badge-new` color was inferred from the brand's accent palette; the exact hex for "New" badges was not extracted.
- The `scrim` opacity value (0.3) was inferred; the exact opacity used on hero overlays was not extracted.
- The `quantity-selector` button height (40px) is below the recommended 44px touch target; this may be a design choice or a gap.
