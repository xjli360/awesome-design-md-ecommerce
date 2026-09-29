---
version: alpha
name: "Nest Diapers"
source_url: "https://nestdiapers.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A clean, safe, and sustainable baby care brand built on a deep teal anchor (#115e67) that reads as clinical-soft rather than pastel-nursery — the brand’s primary voltage appears in logo marks, navigation bars, and subscription CTAs, while a warm marigold accent (#ffc945) and a safety-red (#c00000) handle urgency badges and sale flags. The canvas is a near-white (#f2f2f2) that avoids the sterile hospital white of competitors, and the body text runs a modest #212121 on that surface for high contrast without harshness. Typography pairs Poppins (for display and button labels) with Sofia Sans (for body copy), giving the brand a rounded, approachable sans-serif voice that matches the softness of a diaper product without tipping into cutesy. Signature design moves include a pill-shaped search bar (`{rounded.full}`), product cards with generous `{rounded.md}` corners, and a sticky top nav that carries the teal background with white text — a rare inversion that makes the brand feel like a destination rather than a utility. The checkout flow uses Shopify’s native widgets (hence the #34ccdd and #4a9f53 accents in the extracted palette), but the brand’s own color system stays disciplined: teal for trust, marigold for delight, red for urgency, and a soft green (#028e48) for sustainability badges. The overall mood is calm, competent, and parent-friendly — no loud gradients, no heavy shadows, just clean rectangles with subtle rounding and a lot of breathing room.

colors:
  primary: "#115e67"
  primary-active: "#0d4a51"
  primary-disabled: "#8ab8e9"
  ink: "#212121"
  body: "#434242"
  muted: "#7e7d7d"
  muted-soft: "#d8d8d8"
  hairline: "#d8d8d8"
  hairline-soft: "#f2f2f2"
  canvas: "#f2f2f2"
  surface-soft: "#f2e9db"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#ffc945"
  accent-marigold-active: "#ffc22b"
  accent-red: "#c00000"
  accent-red-active: "#d12328"
  accent-green: "#028e48"
  accent-green-soft: "#bbfcbb"
  accent-orange: "#ff7f15"
  error-bg: "#ffebe8"
  error-text: "#dd2200"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Archivo Black', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', 'Archivo Black', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', 'Archivo Black', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Poppins', 'Archivo Black', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Archivo Black', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Archivo Black', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Sofia Sans', 'Poppins', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Sofia Sans', 'Poppins', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Sofia Sans', 'Poppins', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Sofia Sans', 'Poppins', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', 'Archivo Black', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Poppins', 'Archivo Black', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', 'Archivo Black', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Poppins', 'Archivo Black', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Sofia Sans', 'Poppins', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Poppins', 'Archivo Black', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px

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
    padding: 14px 24px
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-accent-marigold-active:
    backgroundColor: "{colors.accent-marigold-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-pill-subscribe:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
    backgroundColor: "{colors.error-bg}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    size: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-bar-scrolled:
    backgroundColor: "{colors.primary-active}"
    height: 56px
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
    rounded: "{rounded.sm}"
  nav-link-active:
    backgroundColor: "rgba(255, 255, 255, 0.15)"
    textColor: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    shadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-hover:
    shadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  badge-sustainable:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: "400px"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.on-primary}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "rgba(255, 255, 255, 0.85)"
    marginTop: "{spacing.md}"
  hero-cta:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "rgba(255, 255, 255, 0.8)"
    typography: "{typography.link}"
    textDecoration: none
  footer-link-hover:
    textColor: "{colors.accent-marigold}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.on-primary}"
    marginBottom: "{spacing.md}"
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    paddingTop: "{spacing.sm}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  rating-stars:
    color: "{colors.accent-marigold}"
    size: 16px
  rating-stars-empty:
    color: "{colors.hairline}"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 8px
  progress-bar-fill:
    backgroundColor: "{colors.accent-green}"
    rounded: "{rounded.full}"
    height: 8px
  toast-success:
    backgroundColor: "{colors.accent-green-soft}"
    textColor: "{colors.accent-green}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  toast-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"

## Components

### Buttons
**`button-primary`** — The brand’s primary call-to-action, filled with the deep teal `{colors.primary}` and white text. Used for “Add to Cart”, “Subscribe & Save”, and “Shop Now” actions. On hover, shifts to `{colors.primary-active}` with no border change. Disabled state uses `{colors.primary-disabled}` — a muted blue-gray that signals the action is unavailable without visual noise.

**`button-secondary`** — An outlined variant with a white fill and teal border, used for secondary actions like “Learn More” or “View Details”. The 2px border maintains visual weight alongside the primary button. Hover state fills the background with a 10% opacity teal overlay.

**`button-accent-marigold`** — A warm, high-energy button reserved for promotional CTAs, limited-time offers, and hero-section actions. The marigold `{colors.accent-marigold}` against dark ink text creates the highest contrast in the system. Hover darkens to `{colors.accent-marigold-active}`.

**`button-accent-red`** — A compact, urgent button used for “Clearance”, “Last Chance”, or “Low Stock” badges. Smaller padding and font size keep it from competing with primary CTAs while still commanding attention.

**`button-pill-subscribe`** — A fully pill-shaped variant used specifically for subscription sign-up flows. The `{rounded.full}` shape differentiates subscription actions from one-time purchase buttons, reinforcing the recurring-commitment nature of the action.

### Text Inputs & Forms
**`text-input`** — Standard text field with a white background, subtle hairline border, and 12px internal padding. On focus, the border thickens to 2px and switches to `{colors.primary}`. Error state uses a red border and a light pink background (`{colors.error-bg}`) for clear visual feedback. Placeholder text uses `{colors.muted}`.

**`select-dropdown`** — Matches the text-input styling but includes a custom chevron icon in `{colors.muted}`. Used for size, quantity, and subscription frequency selectors.

**`checkbox`** — A 20px square with 2px hairline border and 4px corner radius. Checked state fills with `{colors.primary}` and displays a white checkmark icon. Used in subscription agreements, consent forms, and filter panels.

### Navigation
**`nav-bar`** — A sticky top navigation bar with a solid `{colors.primary}` background and white text. Logo sits left-aligned, nav links center-aligned, and cart/account icons right-aligned. On scroll, the bar shrinks from 64px to 56px height and the background shifts to `{colors.primary-active}` for a subtle depth cue. The bar carries a 1px bottom border in a slightly lighter teal for visual separation.

**`nav-link`** — Navigation links with 8px vertical and 12px horizontal padding. Active or hover state adds a semi-transparent white overlay (`rgba(255, 255, 255, 0.15)`) with 8px rounding. The font is Poppins at 14px weight 600 with 0.2px letter spacing — tight enough to fit multiple links on mobile, open enough to read clearly.

### Cards
**`product-card`** — A white card with 12px rounding, 16px internal padding, and a subtle drop shadow (`0 2px 8px rgba(0,0,0,0.08)`). The product image fills the top with a matching 12px rounding and a 1:1 aspect ratio. Title uses `{typography.title-sm}` in ink, price uses `{typography.body-md}` in teal. On hover, the shadow deepens to `0 4px 16px rgba(0,0,0,0.12)` for a gentle lift effect.

### Badges
**`badge-sale`** — A compact red badge with white uppercase text, used to flag discounted items. The 8px rounding and 4px/8px padding make it sit neatly on the top-left corner of product images.

**`badge-sustainable`** — A green badge (`{colors.accent-green}`) used for eco-friendly, organic, or sustainably sourced products. The soft green (`{colors.accent-green-soft}`) is used as a background for larger sustainability callout sections.

**`badge-new`** — A marigold badge for new arrivals or recently launched products. The high-contrast yellow against ink text creates excitement without the urgency of red.

### Hero Section
**`hero-section`** — A full-width section with a teal background, used on the homepage and campaign landing pages. Minimum height of 400px with generous padding. The title uses `{typography.display-xl}` in white, the subtitle uses `{typography.body-md}` at 85% opacity, and the CTA button uses `{colors.accent-marigold}` for maximum contrast against the teal background.

### Footer
**`footer`** — A dark teal (`{colors.primary-active}`) footer with white text at 80% opacity for links. Links turn marigold on hover. The footer is organized into columns with `{typography.title-sm}` headings and `{typography.body-sm}` link lists. Padding is generous at 48px vertical and 24px horizontal.

### Accordion
**`accordion`** — Used for FAQ sections and product details. A white card with 12px rounding, 1px hairline border, and 16px padding. The header uses `{typography.title-sm}` and toggles a chevron icon on click. Content area uses `{typography.body-sm}` with 8px top padding.

### Quantity Selector
**`quantity-selector`** — A compact control for adjusting product quantities in the cart or on the product page. A white background with hairline border, 8px rounding, and 40px height. The plus/minus buttons have a soft beige background (`{colors.surface-soft}`) and are 40px square.

### Progress Bar
**`progress-bar`** — Used for subscription progress, order tracking, or free-shipping thresholds. A hairline-gray track with full rounding and 8px height. The fill uses `{colors.accent-green}` to indicate completion.

### Toast Notifications
**`toast-success`** — A green-tinted notification for successful actions (e.g., “Item added to cart”). Uses `{colors.accent-green-soft}` as background and `{colors.accent-green}` for text.

**`toast-error`** — A pink-tinted notification for errors (e.g., “Out of stock”). Uses `{colors.error-bg}` as background and `{colors.error-text}` for text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger menu; product cards stack in single column; hero section reduces padding to 32px; search bar moves below nav; footer columns stack vertically; buttons go full-width; quantity selector reduces to 32px height |
| Tablet | 744–1128px | Nav-bar shows 4-5 links with overflow menu; product cards display in 2-column grid; hero section maintains 400px min-height; footer shows 2-column layout; search bar remains in nav |
| Desktop | 1128–1440px | Full nav-bar with all links visible; product cards in 3-column grid; hero section at full padding; footer shows 4-column layout; search bar in nav with expanded width |
| Wide | > 1440px | Max-width container at 1440px with centered content; product cards in 4-column grid; hero section may include full-bleed background image; footer columns maintain 4-column layout with increased horizontal padding |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have 44px minimum touch area (8px padding on 14px text = 30px, padded with additional 7px on each side via transparent click area)
- Quantity selector buttons are 40px × 40px — meets touch target minimum
- Checkbox has 20px visible area with 44px invisible click zone
- Accordion headers have 44px minimum touch height
- Search bar has 48px height for easy tapping

### Collapsing Strategy
- Primary nav collapses to hamburger menu at < 744px; the hamburger icon uses `{colors.on-primary}` on the teal nav bar
- Product filters collapse into a slide-out drawer on mobile, with a “Filter” button that opens from the left
- Footer link columns stack vertically on mobile, with accordion-style expand/collapse for each column heading
- Product image galleries collapse from thumbnail strip to swipeable carousel on mobile
- Cart summary collapses to a sticky bottom bar on mobile, expanding to full page when tapped
- Search bar collapses from inline to full-width overlay on mobile, with auto-focus on the input field

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons (button-secondary) were inferred from common patterns — exact opacity or color shift not extracted from live site
- Error styling for text inputs (border color, background tint) was inferred from the extracted `#ffebe8` and `#dd2200` — exact error message typography and icon placement not confirmed
- Shadow values for product cards were not extractable from static CSS — `0 2px 8px` is an educated guess based on common Shopify theme patterns
- Dark mode is not supported by the brand’s current implementation — no dark-mode media queries or color overrides were found
- Sub-brand palettes (e.g., Nest Diapers vs. Nest Wipes vs. Nest Training Pants) were not distinguishable from the extracted color list
- The `#34ccdd` and `#4a9f53` colors in the extracted list are likely Shopify Pay and Klarna/Afterpay checkout widget colors, not brand colors — they were excluded from the palette
- The `#0b6b6b` and `#15727d` colors are likely hover/active variants of the primary teal — exact usage not confirmed
- Font weights for Poppins and Sofia Sans were inferred from common web usage — the live site may use additional weights (e.g., Poppins 500, Sofia Sans 300) that were not extracted
- The `#8ab8e9` color is used as primary-disabled — this is an assumption based on its low saturation relative to the primary teal
- The `#f2e9db` color appears in the extracted list and is used as `surface-soft` — its exact usage (e.g., background for subscription cards, testimonial sections) is unknown
- The `#00730b` color is likely a Shopify success green and was excluded from the brand palette
- The `#222222` color is very close to `#212121` (ink) — the exact usage distinction between these two dark grays is unclear
