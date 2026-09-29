---
version: alpha
name: "Peak Design"
source_url: "https://www.peakdesign.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, near-black green (#1a211e) sets the stage for a brand that builds carry solutions for people who move through the world with intention. That primary color — a shade pulled from dense forest understory rather than synthetic gear — wraps every primary button, every navigation bar, and every product-card border, creating a consistent visual anchor that reads as serious and grounded. The palette is overwhelmingly neutral: #606562 and #b8bcba for body text and muted elements, #e6e9e8 and #eef1f0 for soft surfaces and canvases, with #0c0c0c and #101010 providing deep ink tones for high-impact typography. Against this subdued backdrop, two accent colors emerge: a restrained sage (#9ea790) that appears in environmental photography overlays and secondary badges, and a sharp signal red (#cc2e39) reserved for sale markers, limited-edition callouts, and urgent CTAs. The typography system leans on Exposure-10, a condensed, high-contrast geometric sans that gives headlines a technical, expedition-grade feel — think instrument panel labels and topographic map legends. Body copy runs in Geist, a clean, low-contrast sans that stays legible across product descriptions and spec tables. Corners are minimal: buttons use {rounded.sm} (8px), cards use {rounded.md} (12px), and the only full-radius element is the search bar at {rounded.full}, a deliberate contrast to the otherwise squared-off interface. The brand trusts density over whitespace — product cards pack images, specs, pricing, and reviews into tight {spacing.md} grids, and the nav bar carries five-plus links plus a utility menu without feeling crowded. The overall effect is a tool, not a destination: Peak Design’s site feels like the inside of a well-organized camera bag, where every compartment has a purpose and nothing is decorative.

colors:
  primary: "#1a211e"
  primary-active: "#0c0c0c"
  primary-disabled: "#606562"
  ink: "#0c0c0c"
  body: "#606562"
  muted: "#989898"
  muted-soft: "#b8bcba"
  hairline: "#d7dad8"
  hairline-soft: "#e6e9e8"
  canvas: "#ffffff"
  surface-soft: "#eef1f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#9ea790"
  accent-red: "#cc2e39"
  accent-teal: "#189cc5"
  accent-blue: "#4a69d4"
  accent-green: "#008464"
  accent-gold: "#e9a93f"
  accent-purple: "#8164bf"
  star-rating: "#e9a93f"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Exposure-10', 'Exposure-10 Fallback', 'Bryant', 'Helvetica', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Exposure-10', 'Exposure-10 Fallback', 'Bryant', 'Helvetica', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Exposure-10', 'Exposure-10 Fallback', 'Bryant', 'Helvetica', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Exposure-10', 'Exposure-10 Fallback', 'Bryant', 'Helvetica', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Geist', 'Geist Fallback', 'Open Sans', 'Helvetica', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Geist', 'Geist Fallback', 'Open Sans', 'Helvetica', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Geist', 'Geist Fallback', 'Open Sans', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Geist', 'Geist Fallback', 'Open Sans', 'Helvetica', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Geist', 'Geist Fallback', 'Open Sans', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Geist', 'Geist Fallback', 'Open Sans', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Geist', 'Geist Fallback', 'Open Sans', 'Helvetica', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Geist', 'Geist Fallback', 'Open Sans', 'Helvetica', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Geist', 'Geist Fallback', 'Open Sans', 'Helvetica', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Geist', 'Geist Fallback', 'Open Sans', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Geist', 'Geist Fallback', 'Open Sans', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Geist', 'Geist Fallback', 'Open Sans', 'Helvetica', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Geist', 'Geist Fallback', 'Open Sans', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Geist', 'Geist Fallback', 'Open Sans', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 600
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill-search:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-rating:
    typography: "{typography.caption-sm}"
    color: "{colors.accent-gold}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-section-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  hero-cta:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    color: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  radio-checked:
    border: "6px solid {colors.primary}"
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-active:
    backgroundColor: "{colors.primary}"
  toggle-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-limited:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
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
    color: "{colors.body}"
    padding: "{spacing.sm} 0"
  breadcrumb:
    typography: "{typography.caption-sm}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.hairline}"
    padding: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  pagination-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.6
  modal-content:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    maxWidth: 600px
  toast-success:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  toast-error:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  skeleton:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    animation: "pulse 1.5s ease-in-out infinite"

## Components

### Buttons
**`button-primary`** — The workhorse CTA across the entire site, rendered in the brand's deep green (#1a211e) with white text. Uses Geist 14px/600 with 0.3px letter spacing for a precise, technical feel. Corners are a modest 8px — not pill-shaped, not sharp. On hover, the background shifts to near-black (#0c0c0c). The disabled state drops to a muted mid-gray (#606562), signaling the button is present but non-functional.

**`button-secondary`** — An outlined variant with a white fill and a 2px solid border in the primary green. Text and border shift to near-black on hover, while the background takes on a soft surface tint (#eef1f0). Used for "Learn More" and "Compare" actions alongside primary buttons.

**`button-tertiary-text`** — A text-only button with no background or border, used for secondary actions like "Cancel" or "View Details." The text sits in the primary green and underlines on hover.

**`button-accent-red`** — A high-urgency variant using the signal red (#cc2e39) for limited-edition drops, clearance sales, and "Act Fast" callouts. Same sizing and typography as the primary button, but the color signals a different emotional register — urgency rather than reliability.

**`button-pill-search`** — The only full-radius button in the system, used exclusively for the search submit action. It's a compact 40px tall with the primary green background, designed to sit inside the search bar's pill-shaped container.

### Cards
**`product-card`** — The core product display unit, a white card with a 1px soft hairline border and 12px rounded corners. Contains a square-ratio image (8px rounded), a title in Geist 16px/600, price in 16px/400, and a gold star rating. On hover, the border strengthens to a standard hairline and a subtle shadow lifts the card. A red badge can overlay the image for sale items.

**`product-card-badge`** — A small, sharp-cornered (4px) label in signal red with uppercase 11px/600 white text. Used for "SALE," "NEW," or "LIMITED" callouts. The badge-new variant uses teal (#189cc5), and badge-limited uses gold (#e9a93f) with dark text.

### Navigation
**`nav-bar`** — A fixed 64px white bar with a 1px bottom hairline. Navigation links are 14px/600 uppercase Geist in body gray (#606562), with the active state underlined by a 2px primary-green border. The bar carries the logo, up to five category links, a search icon, a cart icon, and a user menu — all within a compact horizontal space.

**`nav-link-active`** — The active nav state uses the primary green for text and a 2px bottom border in the same green. Inactive links sit in body gray with no underline.

### Forms
**`text-input`** — A standard 48px input with 8px rounded corners, a 1px hairline border, and 12px/16px padding. On focus, the border thickens to 2px and turns primary green. Error state swaps the border to signal red (#cc2e39). Used for search, email signup, and checkout fields.

**`select-input`** — Matches the text input sizing and styling, used for dropdowns like "Sort by" and "Filter by." The chevron icon sits in the primary green.

**`checkbox`** — A 20px square with 4px rounded corners and a 2px hairline border. When checked, the fill becomes primary green with a white checkmark icon.

**`radio`** — A 20px circle with a 2px hairline border. When selected, the border thickens to 6px in primary green, creating a filled-ring appearance.

**`toggle`** — A 44px by 24px pill with a hairline gray background. When active, the background fills with primary green and the 20px white knob slides to the right.

### Footer
**`footer-section`** — A deep green (#1a211e) footer with white text, padded at 48px top/bottom and 32px left/right. Links render in a muted light gray (#b8bcba) and brighten to white on hover. The section contains columns for support, company, community, and legal links, plus a newsletter signup form.

### Hero
**`hero-section`** — A full-width banner, typically in the primary green with white text, using the Exposure-10 48px/700 display type. Minimum height of 400px. A light variant exists with a soft surface background (#eef1f0) and dark text for editorial content. The CTA button inverts to white background with green text.

### Search
**`search-bar`** — A 40px pill-shaped input with a soft surface background (#eef1f0) and a 1px hairline border. On focus, the background turns white and the border thickens to 2px in primary green. The search button is a 40px primary-green pill nested inside the bar's right edge.

### Badges
**`badge-sale`** — Red (#cc2e39) with white text, 4px rounded, used for discount callouts.
**`badge-new`** — Teal (#189cc5) with white text, used for new product introductions.
**`badge-limited`** — Gold (#e9a93f) with dark ink text, used for limited-edition or exclusive items.

### Feedback
**`toast-success`** — A green (#008464) notification bar with white text, 8px rounded, used for positive confirmations like "Added to Cart."
**`toast-error`** — A red (#cc2e39) notification bar with white text, used for error messages like "Out of Stock."
**`tooltip`** — A near-black (#0c0c0c) label with white text, 4px rounded, used for hover explanations on icons and technical specs.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked footer, reduced hero height (300px), smaller display type (32px), search bar collapses to icon-only |
| Tablet | 744–1128px | Two-column product grid, expanded nav (5 links visible), two-column footer, hero at 350px with 36px display type |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, three-column footer, hero at 400px with 48px display type |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, hero at 450px with 52px display type |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Icon buttons (search, cart, user menu) are 40px circles, meeting the 44px touch target recommendation when including padding
- Product card links and CTAs have 48px minimum touch targets
- Form inputs (text, select) are 48px tall for comfortable tap targets
- Toggle switches are 24px tall with 20px knobs, requiring precise tap — acceptable for settings pages

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-out drawer for category links
- Product grid reduces from 4 columns to 1 column on mobile, with images scaling to full width
- Footer columns stack vertically on mobile, with accordion-style expandable sections for link groups
- Hero section reduces padding and font size on mobile, with the CTA button scaling to full width
- Search bar collapses to an icon-only trigger on mobile, expanding to full-width overlay on tap
- Secondary navigation (breadcrumbs, filters) collapses to a single "Filter" button on mobile, opening a modal overlay

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons, text inputs, and navigation links are inferred from common patterns; exact color transitions and timing are not extracted
- Error styling for form validation (error messages, icon placement, border animations) is not confirmed from the live site
- Dark mode styling is not present on the live site and is not implemented
- Sub-brand or collection-specific palettes (e.g., "Everyday," "Travel," "Camera") may exist but are not extracted
- Animation durations, easing curves, and transition properties are not captured
- The exact font weights for Exposure-10 and Geist are inferred from common usage; the site may use additional weights (e.g., 300, 800, 900) not found in CSS
- Shopify checkout widget colors (e.g., Klarna pink, Afterpay blue) are present in the extracted hex list but are not part of the brand's design system
- Social media icon colors (Facebook blue, Instagram gradient) are present in the extracted list but are not brand colors
- Stock photography dominant tones (e.g., sky blue, grass green) may be present in the extracted list and are not design tokens
- The exact spacing between product card elements and the grid gap are not confirmed; current values are best estimates
- Focus ring styling (color, offset, thickness) for keyboard navigation is not extracted
- Loading states (spinners, skeleton screens) are not confirmed beyond the basic skeleton component
- The brand's typography scale may include additional sizes (e.g., 10px, 40px) not found in the extracted CSS
- Color contrast ratios for accessibility (WCAG AA/AAA) are not verified against the extracted palette
- The brand's icon set (stroke width, size, color) is not documented
- Print stylesheets and email template styling are not included
