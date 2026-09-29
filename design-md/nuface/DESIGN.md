---
version: alpha
name: "NuFace"
source_url: "https://www.mynuface.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A clinical-gadget brand that wraps medical-grade microcurrent technology in a palette of near-black (#010101) and a singular electric blue (#84abfc) — the only color that appears on primary CTAs, device-glow accents, and the brand's signature "NuFace" wordmark against a white (#ffffff) canvas. The extracted hex list is dominated by grays (#151515, #8a8a8a, #cacaca, #acacac, #e2e2e2, #e6e6e6, #dedede, #f7f7f7, #f8f8f8) and a few accent tones (#ee3a45 red, #279a4b green, #fb9e5b orange, #54cdcd teal, #b86c7b mauve, #647581 slate, #515f69 charcoal, #213884 navy, #5e7fce, #7ca7fd, #639cff, #3877f1 blues) that likely belong to checkout widgets (Shopify Pay, Klarna, Afterpay) and social icons rather than the brand itself. The true brand voice emerges from the contrast: glossy black product photography on white cards with `{rounded.sm}` corners, a typography system that mixes Poppins (for display headers) with Mabry Pro (for body copy), and a navigation bar that stays transparent until scroll, then snaps to white with a `{colors.hairline}` bottom border. Buttons are sharp-cornered rectangles (`{rounded.xs}`) filled with `{colors.primary}` blue, carrying `{colors.on-primary}` white text in Poppins Medium 14px — a deliberate departure from the pill-shaped CTAs of beauty competitors, signaling precision over softness. The checkout flow introduces a secondary accent (`#ee3a45`) for sale badges and error states, while the device product cards use a subtle `{colors.surface-soft}` (#f7f7f7) background to separate the hero device image from the white page. This is a brand that trusts its product's metallic sheen over decorative imagery — the design is a clean, slightly cool container for a device that promises visible results.

colors:
  primary: "#84abfc"
  primary-active: "#639cff"
  primary-disabled: "#cacaca"
  ink: "#010101"
  body: "#151515"
  muted: "#8a8a8a"
  muted-soft: "#acacac"
  hairline: "#e2e2e2"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-badge: "#ee3a45"
  error: "#e93636"
  success: "#279a4b"
  accent-orange: "#fb9e5b"
  accent-teal: "#54cdcd"
  accent-mauve: "#b86c7b"
  accent-slate: "#647581"
  accent-charcoal: "#515f69"
  accent-navy: "#213884"
  accent-blue-light: "#7ca7fd"
  accent-blue-mid: "#639cff"
  accent-blue-dark: "#3877f1"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Mabry Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', 'Mabry Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', 'Mabry Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Poppins', 'Mabry Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Poppins', 'Mabry Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Mabry Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Mabry Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Mabry Pro', 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Mabry Pro', 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Mabry Pro', 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Mabry Pro', 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', 'Mabry Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Poppins', 'Mabry Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Poppins', 'Mabry Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', 'Mabry Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Mabry Pro', 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Mabry Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  button-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary}40"
  text-input-error:
    border: "1px solid {colors.error}"
    textColor: "{colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    checkedColor: "{colors.primary}"
  radio:
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    checkedColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-transparent:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary}40"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.md} 0 0 0"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    borderBottom: "1px solid {colors.hairline}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 24px
    width: 24px
  rating-stars:
    textColor: "{colors.accent-orange}"
    fontSize: 16px
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  review-author:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  review-date:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  review-text:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-best-seller:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  icon-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  modal-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    maxWidth: 600px
  modal-close:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  step-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  step-inactive:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  step-complete:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with `{colors.primary}` (#84abfc) blue. Uses Poppins Medium 14px with 0.3px letter-spacing for a precise, clinical feel. Corners are minimally rounded at `{rounded.xs}` (4px), rejecting the pill shape common in beauty e-commerce. On hover, shifts to `{colors.primary-active}` (#639cff); disabled state uses `{colors.primary-disabled}` (#cacaca) with white text. Height is 44px with 12px/24px padding.
**`button-secondary`** — Outlined variant with white fill, `{colors.ink}` text, and a 1px `{colors.hairline}` border. Active state darkens the border to `{colors.ink}` and adds `{colors.surface-soft}` background. Same dimensions and typography as primary.
**`button-tertiary-text`** — A text-only link styled as a button, using `{colors.primary}` blue text with no background or border. Used for "Learn More" and "View Details" links within product cards.
**`button-pill`** — A smaller, fully rounded variant (`{rounded.full}`) used for filter chips and category tags. Uses `{colors.primary}` background with `{colors.on-primary}` text in button-sm (12px). Height is 36px with 10px/20px padding.
**`button-sale`** — Urgency-driven CTA using `{colors.sale-badge}` (#ee3a45) red background. Same dimensions as button-sm but with red fill. Used for "Shop Sale" and limited-time offers.

### Cards
**`product-card`** — White card (`{colors.surface-card}`) with `{rounded.sm}` (8px) corners and 16px padding. The product image sits on a `{colors.surface-soft}` (#f7f7f7) background within the card, creating a subtle separation from the white frame. Title uses `{typography.title-sm}` (16px Poppins Medium), price uses `{typography.body-md}` (16px Mabry Pro Regular). Sale badges overlay the top-left corner of the image area.
**`review-card`** — Customer review card with white background, `{rounded.sm}` corners, and a soft `{colors.hairline-soft}` border. Author name in `{typography.title-sm}`, date in `{typography.caption}` muted gray, review body in `{typography.body-sm}`. Star ratings use `{colors.accent-orange}` (#fb9e5b) for filled stars.

### Navigation
**`nav-bar`** — Fixed top navigation at 72px height. On scroll, snaps from transparent to white with a 1px `{colors.hairline}` bottom border. Navigation links use `{typography.nav-link}` — Poppins Medium 14px with 0.3px letter-spacing, uppercase. Active link has a 2px `{colors.primary}` bottom border. Inactive links use `{colors.muted}` (#8a8a8a). The NuFace logo (wordmark in `{colors.ink}` or `{colors.primary}`) sits left-aligned.
**`nav-bar-transparent`** — Initial state on hero sections: transparent background with white text. Used on full-bleed hero images to let the photography breathe.

### Forms
**`text-input`** — Standard input field with white background, `{colors.hairline}` border, `{rounded.xs}` corners, and 48px height. On focus, the border switches to `{colors.primary}` with a subtle blue box-shadow (`0 0 0 2px #84abfc40`). Error state uses `{colors.error}` (#e93636) border and text. Placeholder text in `{colors.muted}`.
**`select-input`** — Same dimensions and styling as text-input, with a custom dropdown arrow in `{colors.muted}`.
**`checkbox`** — Square checkbox with `{rounded.xs}` corners and `{colors.hairline}` border. Checked state fills with `{colors.primary}` and shows a white checkmark.
**`radio`** — Circular radio button with `{rounded.full}` and `{colors.hairline}` border. Checked state shows a `{colors.primary}` dot on white background.

### Footer
**`footer-section`** — Full-width footer with `{colors.ink}` (#010101) background and white text. Links use `{typography.link}` (14px Mabry Pro Regular) in `{colors.muted-soft}` (#acacac), shifting to white on hover. Section headings use `{typography.title-sm}` (16px Poppins Medium) in white. Padding is `{spacing.section}` (64px) vertical and `{spacing.xl}` (32px) horizontal. Includes newsletter signup, social icons, and legal links.

### Badges
**`badge-new`** — Blue badge (`{colors.primary}`) for new product launches. Uppercase 11px Poppins SemiBold with 0.5px letter-spacing.
**`badge-sale`** — Red badge (`{colors.sale-badge}`) for promotional pricing.
**`badge-best-seller`** — Teal badge (`{colors.accent-teal}` #54cdcd) for top-rated products.

### Modals
**`modal-overlay`** — Semi-transparent black scrim at 50% opacity over the page.
**`modal-card`** — White card with `{rounded.md}` (12px) corners, 32px padding, and max-width 600px. Close button is a 32px circle (`{rounded.full}`) with `{colors.surface-soft}` background and `{colors.ink}` icon.

### Progress & Steps
**`progress-bar`** — Thin 4px bar with `{rounded.full}` corners. Track is `{colors.hairline-soft}`, fill is `{colors.primary}`. Used in checkout and quiz flows.
**`stepper`** — Step indicator with 32px circles. Active step is `{colors.primary}` blue, inactive is `{colors.hairline-soft}` gray, complete is `{colors.success}` (#279a4b) green. Step labels in `{typography.caption}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero section reduces padding to 32px; buttons go full-width; footer links collapse into accordion; font sizes reduce by 2-4px; search bar becomes icon-only |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links (4-5) with hamburger for overflow; hero section uses 48px padding; side-by-side layout for product details; footer uses 2-column grid |
| Desktop | 1128–1440px | Full nav-bar with all links; three-column product grid; hero section at full padding (64px); multi-column footer (3-4 columns); maximum content width at 1128px |
| Wide | > 1440px | Content max-width at 1440px with centered layout; additional whitespace on sides; product grid can expand to 4 columns; hero section can use full-bleed imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) have minimum 44x44px tap target
- Icon buttons are 40x40px minimum
- Quantity selector buttons are 24x24px but sit within a 40px tall container
- Checkbox and radio targets are 44x44px (invisible hit area extends beyond visible element)
- Nav links have 44px minimum height
- Accordion headers have 48px minimum touch area

### Collapsing Strategy
- Top navigation collapses to hamburger menu at < 744px
- Product grid collapses from 3 columns to 2 at tablet, to 1 at mobile
- Footer multi-column layout collapses to single-column accordion at mobile
- Hero section reduces from side-by-side (text + image) to stacked at mobile
- Search bar collapses to icon-only at mobile, expanding on tap
- Product detail page collapses from 2-column (image + info) to stacked at mobile
- Review cards collapse from 2-column grid to single column at mobile
- Tab bars collapse to horizontal scroll at mobile
- Filter/sort options collapse to modal drawer at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (button-primary hover is inferred from primary-active, but exact transition timing and easing are unknown)
- Focus-visible styles for keyboard navigation (outline color, width, offset)
- Error state styling for forms beyond border color (error message typography, icon placement)
- Dark mode palette (no evidence of dark mode implementation)
- Sub-brand or collection-specific color variations (e.g., "NuFace Mini" vs "NuFace Trinity" might have distinct accent colors)
- Animation and transition specifications (duration, easing curves, stagger delays)
- Loading states (skeleton screens, spinner styles, shimmer animations)
- Empty states for cart, wishlist, search results
- Mobile bottom navigation bar (if present, its styling is unknown)
- Checkout flow specific styling (Shopify checkout may override brand styles)
- Print stylesheet
- Accessibility contrast ratios (whether `{colors.muted}` #8a8a8a on white passes WCAG AA)
- The font "Very Vogue Display" and "Dynalight" were found in the extracted list but appear to be decorative/fallback fonts, not primary brand fonts — their usage context is unknown
- The extracted hex list contains many colors that likely belong to third-party widgets (Shopify Pay, Klarna, Afterpay, social media icons) rather than the brand itself — these have been noted as accent colors but their exact brand usage is unconfirmed
