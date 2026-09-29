---
version: alpha
name: "Technogym"
source_url: "https://www.technogym.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A high-voltage fitness brand that runs on a jolt of #f4e116, a near-neon yellow that appears nowhere in nature but everywhere on the site — primary CTAs, navigation highlights, product badges, and the signature "Biocircuit" equipment rings. This is not a muted, aspirational wellness palette; it's a gym-floor attention system, pairing that electric yellow with a deep navy #192f5d for trust and a near-black #1a1918 for body text. The brand's visual language is unapologetically engineered: every component has a hard, precise edge — {rounded.none} on buttons, cards, and inputs — communicating industrial-grade performance rather than soft hospitality. Product imagery dominates, with equipment photographed against stark white or black backgrounds at extreme angles, emphasizing carbon-fiber textures and hydraulic lines. Typography runs a clean sans-serif at moderate weights, with display sizes at 24–32px and body copy at 14–16px, never competing with the photography. The footer is a dense grid of links in {colors.muted} #858580, while the header carries a sticky top nav with a yellow-accented "Shop" dropdown and a search icon that opens a full-screen overlay. Badges for "New," "Sale," and "Exclusive" appear in #f4e116 on dark backgrounds, creating a retail urgency that feels more like a premium automotive showroom than a fitness blog. The overall impression is of a brand that sells precision machinery — because it does.

colors:
  primary: "#f4e116"
  primary-active: "#ffe01e"
  primary-disabled: "#d8d8d8"
  ink: "#1a1918"
  body: "#0d0d0d"
  muted: "#858580"
  muted-soft: "#c4c4c4"
  hairline: "#d8d8d8"
  hairline-soft: "#ededed"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#1a1918"
  navy: "#192f5d"
  navy-dark: "#000066"
  red-accent: "#bd3d44"
  orange-accent: "#e7772f"
  blue-link: "#016fd0"
  green-positive: "#19b13e"

typography:
  display-xl:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.44
    letterSpacing: 0
  title-sm:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.25px
  nav-link-active:
    fontFamily: "'Technogym Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.25px
    color: "{colors.primary}"

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
  section: 72px

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
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: 2px solid "{colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-navy-active:
    backgroundColor: "{colors.navy-dark}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-icon-square:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 44px
    width: 44px
  button-icon-square-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.ink}"
  text-input-error:
    border: 2px solid "{colors.red-accent}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    border: 1px solid "{colors.hairline-soft}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    border: 1px solid "{colors.hairline}"
  checkbox:
    rounded: "{rounded.none}"
    size: 20px
    border: 2px solid "{colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.ink}"
    border: 2px solid "{colors.ink}"
  radio:
    rounded: "{rounded.full}"
    size: 20px
    border: 2px solid "{colors.hairline}"
  radio-checked:
    border: 6px solid "{colors.ink}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid "{colors.hairline-soft}"
  top-nav-item-active:
    textColor: "{colors.primary}"
    borderBottom: 2px solid "{colors.primary}"
  top-nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 0
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  top-nav-dropdown-item:
    padding: 8px 24px
  top-nav-dropdown-item-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
  search-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 44px
    width: 44px
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
  search-input-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    rounded: "{rounded.none}"
    padding: 16px 24px
    border: none
    borderBottom: 2px solid "{colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.red-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  product-card-badge-new:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  category-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    border: 1px solid "{colors.hairline}"
  category-card-active:
    border: 2px solid "{colors.primary}"
    textColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-active:
    textColor: "{colors.primary}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.md}"
  footer-newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: none
  footer-newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 24px
    height: 48px
  footer-social-icon:
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.none}"
    height: 24px
  footer-social-icon-active:
    textColor: "{colors.primary}"
  badge-default:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.red-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  badge-new:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  badge-exclusive:
    backgroundColor: "{colors.orange-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    margin: "0 8px"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    padding: 4px 12px
  pagination-disabled:
    textColor: "{colors.muted-soft}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 44px
    border: 1px solid "{colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 44px
    width: 44px
  quantity-selector-button-active:
    backgroundColor: "{colors.surface-soft}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    borderBottom: 1px solid "{colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    padding: "0 0 {spacing.base} 0"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    borderBottom: 1px solid "{colors.hairline}"
  tab-active:
    textColor: "{colors.ink}"
    borderBottom: 2px solid "{colors.primary}"
  tab-inactive:
    textColor: "{colors.muted}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 6px 12px
  modal-overlay:
    backgroundColor: "rgba(0,0,0,0.5)"
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    maxWidth: 600px
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  notification-success:
    backgroundColor: "{colors.green-positive}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 12px 16px
  notification-error:
    backgroundColor: "{colors.red-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 12px 16px
  notification-info:
    backgroundColor: "{colors.blue-link}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 12px 16px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in #f4e116 with black text. These are sharp rectangles with zero border-radius, communicating precision engineering. On hover, the yellow shifts to #ffe01e for a brighter state. The disabled state drops to #d8d8d8 with muted text, signaling the button is non-functional. Used for "Add to Cart," "Shop Now," and "Learn More" actions across product pages and hero sections.

**`button-secondary`** — An outlined variant with a 2px black border on white background. On hover, the fill inverts to black with white text. This button is used for "View Details," "Compare," and secondary actions where the primary yellow would be visually overwhelming. The uppercase label and sharp corners maintain the industrial brand language.

**`button-tertiary-text`** — A text-only button with no background or border, used for "Cancel," "Back," and less prominent actions. On hover, the text color shifts to the brand yellow, providing a subtle but distinct feedback state. This is the quietest button in the system, reserved for navigation and form controls.

**`button-navy`** — A deep navy #192f5d button with white text, used primarily on light backgrounds where the yellow would compete with other elements. The hover state darkens to #000066. This button appears in footer CTAs, newsletter signups, and on product detail pages where a more conservative action is needed.

### Cards
**`product-card`** — A sharp-edged white card with no border-radius, containing a product image, title, price, and optional badges. The image area sits on a soft gray #f7f7f7 background, ensuring product photography pops. Badges appear in the top-left corner in yellow (#f4e116 for "New"), red (#bd3d44 for "Sale"), or navy (#192f5d for "Exclusive"). The card has no shadow or border, relying on the grid spacing and content hierarchy for visual separation.

**`category-card`** — A bordered card (1px #d8d8d8) used for navigation categories on the homepage. On active or hover state, the border thickens to 2px and turns yellow, with the category title also shifting to yellow. This card is used for equipment categories like "Treadmills," "Bikes," and "Strength Training."

**`hero-banner`** — A full-width section with a near-black #1a1918 background and white text, featuring a large headline (32px, bold), optional yellow accent text, and a yellow CTA button. The banner uses no border-radius, stretching edge-to-edge. Product imagery is often overlaid or positioned to the right, with the text block on the left. The yellow accent text (#f4e116) is used for key value propositions or promotional copy.

### Navigation
**`top-nav`** — A 72px white header with a thin bottom border (#ededed). Navigation links are 14px medium weight with 0.25px letter spacing. The active link state shows a yellow (#f4e116) bottom border and yellow text. A search icon sits on the right, opening a full-screen overlay with a large text input. The "Shop" link triggers a dropdown menu with product categories, each item having a hover state that turns yellow.

**`search-overlay`** — A full-screen white overlay with a large, borderless text input (24px, semibold) underlined by a 2px black line. Search results appear below as product cards. The overlay has no border-radius, consistent with the brand's sharp aesthetic. A close button (X) sits in the top-right corner.

**`breadcrumb`** — A simple text-based navigation component using 13px gray (#858580) text with ">" separators. The active (current) page is rendered in black (#1a1918). No background or border, just inline text. Used on product listing and detail pages.

### Forms
**`text-input`** — A 48px tall input with a 1px #d8d8d8 border and zero border-radius. On focus, the border thickens to 2px black. Error state uses a 2px red (#bd3d44) border. Disabled inputs have a gray background (#f7f7f7) with muted text (#c4c4c4). The input uses 16px body text for readability.

**`select-input`** — Matches the text-input styling: 48px tall, 1px border, no border-radius. The dropdown arrow is rendered in black. Used for size, quantity, and filter selections.

**`checkbox`** and **`radio`** — Square checkboxes (no border-radius) and circular radio buttons, both 20px with a 2px #d8d8d8 border. Checked state fills with black. Radio buttons use a 6px inner circle on checked state.

### Footer
**`footer`** — A dense, dark section (#1a1918 background) with white headings and gray (#c4c4c4) body links. Links turn yellow on hover. The footer includes a newsletter signup form with a white input and yellow submit button. Social media icons are rendered in gray, turning yellow on hover. The footer is divided into columns: "Products," "Support," "Company," and "Connect."

### Badges
**`badge-default`** — Yellow (#f4e116) background with black text, 11px uppercase bold. Used for "New" and promotional tags. Zero border-radius, sitting flush against the product card edge.

**`badge-sale`** — Red (#bd3d44) background with white text. Used for discount and sale items. Same typography and sharp corners as the default badge.

**`badge-new`** — Navy (#192f5d) background with white text. Used for newly launched products or exclusive collections.

**`badge-exclusive`** — Orange (#e7772f) background with white text. Used for limited-edition or partner-exclusive products.

### Notifications
**`notification-success`** — Green (#19b13e) background with white text. Used for success messages like "Added to Cart" or "Order Confirmed." No border-radius, 12px padding.

**`notification-error`** — Red (#bd3d44) background with white text. Used for error states, form validation failures, and payment issues.

**`notification-info`** — Blue (#016fd0) background with white text. Used for informational messages like shipping updates or policy changes.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack vertically; hero banner text reduces to 24px; footer columns stack; search overlay becomes full-screen; category cards become full-width; buttons expand to full-width; quantity selector shrinks to 36px height |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links (Shop, Support, Search); hero banner uses 28px headline; footer splits into 2x2 grid; category cards show 3 per row; search overlay uses 60% width |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; hero banner at 32px headline; footer in 4 columns; category cards show 4 per row; search overlay at 40% width |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero banner content centered with max-width; category cards show 5 per row; search overlay at 30% width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons (search, close, social) are 44px x 44px on mobile, 40px x 40px on desktop
- Dropdown menu items have 44px minimum touch height
- Quantity selector buttons are 44px x 44px on all breakpoints
- Checkbox and radio buttons are 20px x 20px with 44px touch area via padding

### Collapsing Strategy
- Top navigation collapses to a hamburger menu at < 744px, with a slide-in drawer for navigation links
- Product filters collapse to a "Filter" button that opens a modal on mobile
- Footer columns stack vertically on mobile, with accordion-style expandable sections
- Multi-column layouts (product grids, category cards) reduce column count as viewport shrinks
- Hero banner text and CTA stack vertically on mobile
- Search overlay transitions from a centered panel to full-screen on mobile
- Breadcrumbs truncate on mobile, showing only the current page and a "Back" link

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site; the typography block uses a speculative "Technogym Sans" name. The actual brand font may be a custom typeface, "Technogym" branded font, or a standard sans-serif like Helvetica Neue or Arial. Font sizes and weights are estimated from visual analysis of the site.
- Hover and active states for many components (dropdown items, footer links, social icons) are inferred from common patterns; actual implementations may differ.
- No dark mode styles were observed; the site appears to use a light-only theme.
- Error styling for forms (validation messages, error icons) is not confirmed; the red border (#bd3d44) is an assumption based on the extracted color list.
- The extracted color list contains many colors that appear to be from third-party widgets (payment buttons, social icons, stock imagery). The true brand palette likely centers on #f4e116 (yellow), #1a1918 (near-black), #192f5d (navy), and #ffffff (white). The red, orange, green, and blue values are included as accent/utility colors but may not all be actively used in the design system.
- No animation or transition timing values were extracted; the site likely uses standard 200-300ms ease transitions for hover states.
- The "Technogym Sans" font family is a placeholder; the actual font stack should be verified from the site's CSS or brand guidelines.
- Sub-brand or regional palette variations (e.g., Technogym Japan, Technogym for Business) are not documented.
- Accessibility contrast ratios have not been verified against WCAG standards; the yellow-on-white combination (#f4e116 on #ffffff) may fail contrast requirements for body text.
