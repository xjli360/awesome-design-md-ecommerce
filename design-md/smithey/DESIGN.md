---
version: alpha
name: "Smithey"
source_url: "https://smithey.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Smithey Ironware Company speaks in the language of heirloom craftsmanship, where every surface carries the quiet confidence of cast iron seasoned over generations. The brand's palette is drawn from the forge itself — deep verdant greens like {colors.primary} (#203d3e) anchor the experience, evoking the patina of well-loved cookware, while warm brass accents in {colors.accent} (#b68b32) catch the light like polished fittings on a vintage skillet. The canvas is a soft, almost chalky white ({colors.canvas} #f6f6f6) that feels tactile and approachable, not clinical. Text lives in near-black {colors.ink} (#141414) and charcoal {colors.body} (#333029), with muted tones like {colors.muted} (#6c757d) and {colors.muted-soft} (#545454) supporting secondary information. Hairlines draw in {colors.hairline} (#dedede) and a softer {colors.hairline-soft} (#e2e2e2), keeping edges defined without harshness. The typography leans on Gotham and GothamSSm — a geometric sans-serif with a sturdy, American industrial feel that matches the brand's South Carolina roots. Display sizes run moderate, never shouting, while body text at 14–16px stays readable and grounded. Rounded corners are restrained: a soft {rounded.sm} (8px) on buttons, {rounded.md} (12px) on cards, and {rounded.lg} (20px) on hero images — nothing so pill-like that it undermines the honest, forged-metal character. The overall mood is warm, substantial, and unhurried, like a Sunday morning spent seasoning a new skillet.

colors:
  primary: "#203d3e"
  primary-active: "#112626"
  primary-disabled: "#747474"
  accent: "#b68b32"
  accent-active: "#8c6b26"
  ink: "#141414"
  body: "#333029"
  muted: "#6c757d"
  muted-soft: "#545454"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#f6f6f6"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-strong: "#cccccc"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  on-dark: "#ffffff"
  error: "#c13515"
  error-soft: "#fce4e0"
  success: "#203d3e"
  star-rating: "#b68b32"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Gotham', 'GothamSSm', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Gotham', 'GothamSSm', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Gotham', 'GothamSSm', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Gotham', 'GothamSSm', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham', 'GothamSSm', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham', 'GothamSSm', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Gotham', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Gotham', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Gotham', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'Gotham', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Gotham', 'GothamSSm', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Gotham', 'GothamSSm', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Gotham', 'GothamSSm', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham', 'GothamSSm', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Inter', 'Gotham', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Gotham', 'GothamSSm', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.8px
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0px
  button-icon-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.error}"
  select-input:
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
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 600
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-image:
    rounded: "{rounded.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.on-primary}"
    opacity: 0.85
  badge-new:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-best-seller:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 44px
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
    opacity: 0.8
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
    opacity: 1
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
    textTransform: uppercase
    letterSpacing: "1px"
  newsletter-input:
    backgroundColor: "rgba(255,255,255,0.1)"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid rgba(255,255,255,0.3)"
  newsletter-input-focus:
    backgroundColor: "rgba(255,255,255,0.15)"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "2px solid {colors.accent}"
  newsletter-button:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 48px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the Smithey experience. Rendered in the brand's deep green ({colors.primary} #203d3e) with white text, it carries a modest 8px rounded corner ({rounded.sm}) and 48px height. On hover, it deepens to {colors.primary-active} (#112626). The disabled state uses {colors.primary-disabled} (#747474) to signal unavailability without visual noise. All primary buttons use uppercase Gotham at 14px with 0.5px letter spacing for a deliberate, crafted feel.

**`button-secondary`** — An outlined variant that sits on the canvas background ({colors.canvas} #f6f6f6) with a 2px solid border in the brand green. The text matches the border color. On hover or active, the button fills solid green and inverts to white text. This button is used for "Learn More" or "View Details" actions where the primary button is reserved for cart or checkout.

**`button-accent`** — A warm brass variant using {colors.accent} (#b68b32) for moments of celebration or highlight — "Add to Cart" after selection, "Subscribe" on the newsletter, or limited-edition product launches. Hover deepens to {colors.accent-active} (#8c6b26). This button should be used sparingly to preserve its specialness.

**`button-text`** — A borderless, backgroundless button that uses only the brand green text. Used for tertiary actions like "Cancel", "Clear filters", or "View all". Padding is minimal (8px vertical, no horizontal) so it reads as inline text with intent.

**`button-icon-circle`** — A 40px circular icon button used for search toggles, cart icons, and mobile menu triggers. The background is {colors.surface-soft} (#f6f6f6) with the icon in {colors.ink} (#141414). The full rounded shape ({rounded.full}) keeps it friendly and unobtrusive.

### Cards
**`product-card`** — The primary product display unit across collection pages and search results. A white background ({colors.surface-card} #ffffff) with a subtle 1px shadow and 12px rounded corners ({rounded.md}). The image area uses the same corner radius on top edges only, creating a clean visual break. The title uses {typography.title-sm} in {colors.ink}, while the price appears in {colors.primary} at body-md weight 600. On hover, the shadow deepens to 4px/12px for a subtle lift effect. Cards are spaced at {spacing.base} (16px) in a responsive grid.

**`hero-section`** — Full-width hero blocks that anchor landing pages and category headers. The background fills with {colors.primary} (#203d3e) and text renders in white. The hero image itself receives a generous {rounded.lg} (20px) corner radius, softening the industrial edge. The title uses display-xl (36px) while the subtitle sits at body-md with 85% opacity for hierarchy.

### Navigation
**`nav-bar`** — A fixed-position top navigation bar at 72px height on desktop, shrinking to 64px on scroll with a subtle drop shadow. The background is the canvas white ({colors.canvas} #f6f6f6) and links use uppercase Gotham at 13px with 0.8px letter spacing. Active links render in {colors.primary}, inactive in {colors.muted}. The logo sits centered or left-aligned depending on viewport, with the cart and search icons grouped on the right.

**`nav-link`** — Individual navigation items that transition between muted and primary color states. No background fill — the color change alone signals state. The generous letter spacing and uppercase treatment give the nav a editorial, magazine-like quality that suits the brand's storytelling approach to cookware.

### Forms
**`text-input`** — Standard text inputs for search, account forms, and checkout. A white background with a 1px {colors.hairline} (#dedede) border and 8px rounded corners. On focus, the border thickens to 2px and shifts to {colors.primary} for clear visual feedback. Error states swap the border to {colors.error} (#c13515). Height is consistently 48px for touch-friendly tap targets.

**`select-input`** — Dropdown selectors styled identically to text inputs for visual consistency. Used for quantity selection, sorting, and filter dropdowns. The chevron icon uses {colors.muted} (#6c757d).

**`newsletter-input`** — A specialized input for the footer newsletter signup, designed to sit on the dark green footer background. Uses a semi-transparent white background (rgba 255,255,255,0.1) with a subtle white border. On focus, the border shifts to {colors.accent} (#b68b32) for a warm glow. The companion submit button uses the accent color to complete the interaction.

### Footer
**`footer-section`** — A full-width footer in {colors.primary} (#203d3e) with white text. Links render at 85% opacity and return to full opacity on hover. Section headings use uppercase Gotham with 1px letter spacing for structure. The footer includes accordion-style mobile navigation for smaller screens, with the accordion headers using a bottom border in a lighter green tone.

### Badges
**`badge-new`** — A warm brass badge ({colors.accent} #b68b32) for new arrivals and recently launched products. Uses uppercase Gotham at 11px with tight 4px/8px padding and a subtle 4px corner radius ({rounded.xs}).

**`badge-sale`** — A red badge ({colors.error} #c13515) for markdown items. Same typography and sizing as the new badge, but the color signals urgency and savings.

**`badge-best-seller`** — A green badge ({colors.primary} #203d3e) for top-performing products. Uses the brand's own primary color to signal endorsement and quality.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; footer links become accordion; hero text centers; buttons go full-width; search bar moves to overlay; product cards stack vertically with full-width images |
| Tablet | 744–1128px | Two-column product grid; nav shows limited links with "More" dropdown; footer shows two-column layout; hero maintains side-by-side layout; buttons remain inline but smaller |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; footer in four-column layout; hero uses split layout with image right; standard button sizing |
| Wide | > 1440px | Four-column product grid on collection pages; max-width container (1440px) centers content; hero scales proportionally; extra whitespace around product cards |

### Touch Targets
- All interactive elements maintain minimum 44px height for touch accessibility
- Icon buttons (search, cart, menu) are 40px circles with 44px tap area via padding
- Product card tap targets (title, image, button) are separated by at least 8px
- Accordion headers in mobile footer have 48px minimum height
- Quantity selector buttons are 40px with 44px tap area

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Secondary navigation (category strip) collapses to a horizontal scrollable strip below 744px
- Footer link groups collapse to accordion panels below 744px
- Product filters collapse to a slide-out drawer below 744px
- Multi-column product grids reduce columns by one at each breakpoint
- Hero sections stack vertically below 744px (text above image)
- Search bar becomes a full-screen overlay below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card images (zoom effect, alternate image reveal) couldn't be reliably extracted
- Error message styling for form validation (text color, background, iconography) is inferred from general brand colors
- Loading states (skeleton screens, spinners) are not documented — colors and animation timing are unknown
- Dark mode is not implemented on the current site — all values assume light theme
- Sub-brand or seasonal color palettes (holiday, limited edition) are not captured
- Focus ring styles (outline width, color, offset) for keyboard navigation are not documented
- Micro-interactions (button press feedback, card entrance animations) timing and easing curves are unknown
- Mobile bottom navigation bar (if any) behavior and styling is not captured
- Cookie consent banner and GDPR-related UI styling is not documented
- Print stylesheet overrides are not available
- Custom checkbox and radio button styling (if any) is not captured — may use browser defaults
