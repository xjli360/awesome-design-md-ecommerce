---
version: alpha
name: "Unbottled"
source_url: "https://unbottled.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Unbottled is a French body-care brand that has built its entire visual identity around the conviction that solid, plastic-free products should feel like a small daily luxury, not a sacrifice. The palette is anchored by a warm, almost edible coral — `#f79b76` — that appears on primary buttons, badges, and accent elements, giving every interaction a soft, sunlit glow. This is balanced against a deep teal `#108474` used for secondary actions, selected-product highlights, and the brand's signature "solid" badge, creating a natural, botanical tension between earth and fruit. The canvas is a clean `#eeeeee` rather than pure white, lending the entire site a slightly warmer, more tactile feel than the typical stark e-commerce template. Typography relies on DM Sans for body text and DM Serif Display for headlines, a pairing that reads as both contemporary and artisanal — the serif brings a touch of editorial sophistication to product titles, while the sans keeps navigation and pricing clean. Accent yellows (`#fde16c`, `#fbcd0a`) and a muted lavender (`#a89cc8`) appear in limited, intentional doses — on sale badges, star ratings, and secondary informational tags — preventing the palette from feeling monochromatic. The brand's commitment to `{rounded.full}` pills for buttons and `{rounded.sm}` for cards creates a friendly, approachable interface where nothing feels sharp or industrial. This is a design system that trusts color over chrome, using generous `{spacing.xl}` and `{spacing.xxl}` gutters to let product photography and the warm coral-teal contrast breathe.

colors:
  primary: "#f79b76"
  primary-active: "#ff7743"
  primary-disabled: "#fdf2ee"
  ink: "#333333"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#888888"
  hairline: "#dddddd"
  hairline-soft: "#e9e9e9"
  canvas: "#eeeeee"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  teal: "#108474"
  teal-soft: "#c1e6e6"
  teal-bg: "#edf5f5"
  yellow: "#fde16c"
  yellow-bright: "#fbcd0a"
  yellow-soft: "#ffff00"
  lavender: "#a89cc8"
  coral-light: "#ff9c76"
  orange-accent: "#ffac34"
  facebook: "#3b5998"
  twitter: "#1da1f2"

typography:
  display-xl:
    fontFamily: "'DM Serif Display', 'Baskerville', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'DM Serif Display', 'Baskerville', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    opacity: 0.85
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-outline-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    boxShadow: "0 2px 8px rgba(51,51,51,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 1px 3px rgba(51,51,51,0.06)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 12px rgba(51,51,51,0.10)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-badge:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-card-badge-sale:
    backgroundColor: "{colors.yellow-bright}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "16px 32px"
    height: 56px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  social-icon:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  social-icon-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
  star-rating:
    textColor: "{colors.yellow-bright}"
    fontSize: 16px
  star-rating-empty:
    textColor: "{colors.hairline}"
    fontSize: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered as a pill-shaped button in the signature coral `#f79b76`. On hover, it deepens to `#ff7743`; when disabled, it fades to a soft peach `#fdf2ee` with muted text. Used for "Add to Cart", "Subscribe", and primary checkout flows. The full rounded shape (`{rounded.full}`) and generous horizontal padding (`14px 28px`) make it feel tactile and inviting.

**`button-secondary`** — A teal `#108474` pill button used for secondary actions like "Learn More" or "Discover the Range". On hover, it subtly reduces opacity to 85% rather than changing color, maintaining the brand's clean teal identity. Shares the same dimensions and typography as the primary button for visual consistency.

**`button-outline`** — A transparent button with a `#dddddd` hairline border and dark ink text. On hover, the border thickens to `#333333` and the background fills with the soft surface tone `#f9fafb`. Used for "View Details" on product cards and secondary navigation paths where visual weight should be minimal.

### Cards
**`product-card`** — A white card with soft `{rounded.md}` corners and a subtle drop shadow (`0 1px 3px rgba(51,51,51,0.06)`). The product image sits flush to the top corners (`{rounded.md} {rounded.md} 0 0`), while text content below uses `{typography.body-sm}`. On hover, the shadow deepens to `0 4px 12px rgba(51,51,51,0.10)`, creating a gentle lift effect. Badges overlay the top-left of the image area.

**`product-card-badge`** — A small teal `#108474` pill badge with uppercase white text, positioned over product images to indicate "Solid" or "New" status. Sale variants use a bright yellow `#fbcd0a` background with dark ink text for urgency.

### Navigation
**`nav-bar`** — A 72px fixed-height bar on the `#eeeeee` canvas, separated from content by a soft `#e9e9e9` bottom border. Navigation links use uppercase `{typography.nav-link}` with 0.5px letter-spacing for a refined, editorial feel. On scroll, the bar transitions to a white background with a subtle shadow for visual separation.

**`search-bar`** — A pill-shaped search input with white background and `#dddddd` border. On focus, the border switches to the brand coral `#f79b76` and the placeholder text transitions from muted to ink. Designed for quick product lookup across the catalog.

### Forms
**`text-input`** — Standard form input with `{rounded.sm}` corners, white background, and a `#dddddd` border. On focus, the border doubles to 2px and adopts the primary coral. Error states use the active coral `#ff7743` for clear visual feedback. All inputs share a consistent 48px height for alignment.

**`quantity-selector`** — A compact horizontal control with `{rounded.sm}` corners on a soft `#f9fafb` background. The plus/minus buttons are transparent but maintain the same height, creating a clean, integrated look. Used on product detail pages for adjusting purchase amounts.

### Footer
**`footer-section`** — A dark `#333333` footer with white text, providing strong contrast to the warm canvas above. Links are rendered in `#888888` and shift to the brand coral on hover. Social media icons sit in soft circular buttons that fill with coral on interaction. The footer uses generous `{spacing.xxl}` padding to feel substantial without crowding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text scales to `{typography.display-md}`; buttons become full-width; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses `{typography.display-xl}`; side-by-side footer columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero with large serif display; multi-column footer with social icons |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid can expand to four columns; hero uses larger imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons and social icons are exactly 40px, exceeding the 44px recommendation where visual density requires it
- Product card tap targets include the entire card surface, not just text links
- Quantity selector buttons are 40px tall with adequate spacing between plus/minus

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-out drawer
- Product filters collapse into a modal overlay on mobile
- Multi-column footer collapses to a single stacked column below 744px
- Hero section reduces vertical padding from `{spacing.section}` to `{spacing.xxl}` on mobile
- Product image galleries switch from thumbnail strip to swipeable dots on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and outline buttons were inferred from common patterns; exact transition durations and easing curves were not extractable
- Error state styling for text inputs (iconography, helper text positioning) was not visible on the live site
- Dark mode palette is not defined; the brand currently operates in light mode only
- Sub-brand or seasonal palette variations (e.g., holiday collections) were not observed
- Loading states (skeleton screens, spinners) were not extractable from static analysis
- Focus ring styles (outline, offset, color) for keyboard navigation were not reliably captured
- Animation timing and easing curves for transitions (hover, focus, page load) are not specified
- Specific font weights for DM Sans and DM Serif Display beyond what appears in the typography section were not confirmed
- Star rating component sizing and spacing for mobile vs. desktop was not fully resolved
