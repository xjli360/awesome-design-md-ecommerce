---
version: alpha
name: "Momotaro Apotheca"
source_url: "https://momotaroapotheca.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dusky rosewood palette anchored on #78555a — a muted, almost dusty mauve that reads as grown-up intimacy rather than clinical pink — and #e8ae9e, a warm salmon blush that surfaces in hover states, decorative borders, and the brand's signature "Shop by Concern" cards. The canvas is #ffede2, a soft cream that wraps the entire experience in a feeling of morning light through linen curtains, while #453f3f provides a near-black ink that keeps body copy legible without the harshness of pure #121212. Typography pairs Playfair Display for editorial headings — its bracketed serifs and high contrast lending a 19th-century apothecary gravity — with Archivo for UI labels and body copy, a geometric sans that stays neutral and trustworthy. Buttons use {rounded.full} pill shapes in the primary rosewood, while secondary CTAs invert to a transparent outline on the cream canvas. Product cards float on {rounded.lg} corners with soft shadows, and the persistent "Free Shipping over $50" banner sits in #e38c76 — a deeper coral that signals urgency without alarm. The brand avoids hard edges: every input, badge, and toggle uses at least {rounded.sm}, and the sticky nav collapses to a compact 56px on mobile with the cart icon and hamburger menu flanking the wordmark.

colors:
  primary: "#78555a"
  primary-active: "#5e4044"
  primary-disabled: "#c4a8ab"
  ink: "#453f3f"
  body: "#453f3f"
  muted: "#78555a"
  muted-soft: "#c4a8ab"
  hairline: "#dedede"
  hairline-soft: "#f3f3f3"
  canvas: "#ffede2"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-coral: "#e38c76"
  accent-salmon: "#e8ae9e"
  accent-blue: "#334fb4"
  accent-blue-light: "#1199ff"
  badge-new: "#e38c76"
  star-rating: "#453f3f"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Archivo', 'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02px
  title-sm:
    fontFamily: "'Archivo', 'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.01px
  body-md:
    fontFamily: "'Archivo', 'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Archivo', 'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Archivo', 'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02px
  caption-sm:
    fontFamily: "'Archivo', 'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.01px
  badge:
    fontFamily: "'Archivo', 'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.05px
    textTransform: uppercase
  button-md:
    fontFamily: "'Archivo', 'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.03px
  button-sm:
    fontFamily: "'Archivo', 'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.02px
  link:
    fontFamily: "'Archivo', 'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Archivo', 'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02px
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.accent-salmon}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-coral}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    height: 56px
    boxShadow: "0 2px 8px rgba(18,18,18,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  concern-card:
    backgroundColor: "{colors.accent-salmon}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    minHeight: 120px
  concern-card-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
    textDecoration: none
  footer-link-hover:
    textDecoration: underline
  announcement-bar:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
    height: 36px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a full pill in the brand's dusty rosewood {colors.primary}. Used for "Add to Cart," "Subscribe & Save," and checkout entry points. On hover, deepens to {colors.primary-active}; when disabled, fades to {colors.primary-disabled} with a lighter text. The pill shape is consistent across all button variants, reinforcing the brand's soft, approachable stance.

**`button-secondary`** — An outlined variant with a transparent fill and a 2px solid border in {colors.primary}. Used for "Learn More" and "View Details" links where the primary action is already present. On hover, fills with {colors.accent-salmon} for a warm, low-pressure feedback. Text remains {colors.primary} throughout.

**`button-accent-coral`** — A smaller, higher-energy button in {colors.accent-coral}, reserved for promotional banners, limited-time offers, and the "Shop Sale" trigger. Uses {typography.button-sm} to fit tighter spaces like announcement bars and mini-cart footers.

### Cards
**`product-card`** — A white card with {rounded.lg} corners and no border, relying on a subtle box-shadow for separation. The image occupies the top half with matching top radius, followed by the product title in {typography.title-sm} and the price in bold {typography.body-md}. A floating badge in {colors.badge-new} may appear over the image corner for new arrivals or sale items.

**`concern-card`** — A larger, content-driven card used in the "Shop by Concern" section (e.g., "Cycle Support," "Menopause," "Libido"). Rendered in {colors.accent-salmon} by default, with the concern name centered in {typography.title-sm}. On hover, the background shifts to {colors.primary} and text inverts to white, creating a clear selection state.

### Navigation
**`nav-bar`** — A fixed top bar at 72px on desktop, with the brand wordmark centered or left-aligned, flanked by nav links in uppercase {typography.nav-link}. The background is {colors.canvas} with a soft bottom hairline. On scroll, the bar shrinks to 56px and gains a subtle shadow. Mobile collapses to a hamburger menu and cart icon.

**`announcement-bar`** — A persistent strip above the nav in {colors.accent-coral}, displaying shipping thresholds, promotions, or wellness tips in {typography.caption}. Full-width with centered text and {spacing.sm} vertical padding.

### Forms
**`text-input`** — Standard input fields with a {colors.canvas} background, {rounded.sm} corners, and a 1px {colors.hairline} border. On focus, the border thickens to 2px and switches to {colors.primary}. Error state uses a 2px {colors.accent-coral} border. Used for email signup, search, and checkout forms.

**`search-bar`** — A pill-shaped search field with a white background and 1px hairline border. On focus, the border becomes 2px {colors.primary}. Includes a magnifying glass icon on the left and a clear button on the right when text is present.

### Footer
**`footer-section`** — A full-width footer in {colors.primary} with white text. Contains columns for customer care, about us, and social links. Links use {typography.link} and underline on hover. The background provides a strong visual closure to the page, contrasting with the light canvas above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + cart; product cards stack single-column; concern cards reduce to 2-column grid; footer links stack vertically; announcement bar text shrinks to {typography.caption-sm} |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards in 2-column grid; concern cards in 3-column grid; footer in 2-column layout |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; concern cards in 4-column grid; footer in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px with centered content; nav bar expands to full width; product cards may show 4 per row |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons in the nav (cart, search, hamburger) are 48x48px tap targets
- Quantity selector +/- buttons are 36x36px with adequate spacing
- Accordion headers have 48px minimum touch height

### Collapsing Strategy
- Primary nav links collapse into a hamburger menu below 744px
- Product card grid reduces from 3 columns to 2 at tablet, to 1 at mobile
- Footer sections stack vertically on mobile, with accordion-style expand/collapse for link groups
- "Shop by Concern" cards reduce from 4 columns to 2 on mobile
- Announcement bar text truncates or scrolls on very narrow screens (< 400px)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary and secondary buttons have confirmed hover colors
- Error state styling for forms (validation messages, iconography) is inferred from the coral accent but not verified
- The extracted color list includes #334fb4 and #1199ff, which appear to be Shopify Pay and Klarna widget colors — these are not brand colors and should not be used in UI components
- The font "Cocogoose Pro Regular" was found in the CSS but its usage context (headings vs. decorative) is unclear; it may be a legacy or fallback font
- Dark mode is not present on the live site; no dark palette tokens exist
- Sub-brand or seasonal color palettes (e.g., holiday, limited edition) are not documented
- Loading states, skeleton screens, and spinner animations are not captured
- The exact box-shadow values for product cards and modals are not extracted
- Transition durations and easing curves are not specified
