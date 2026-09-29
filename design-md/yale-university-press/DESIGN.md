---
version: alpha
name: "Yale University Press"
source_url: "https://yalebooks.yale.edu"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A scholarly publisher whose visual system is built on the authority of a single deep blue — #3858e9 — that appears as the primary action color, the link color, and the accent that pulls the eye through dense informational pages. This blue, paired with a near-black ink (#1e1e1e) for body text and a muted #949494 for secondary metadata, creates a hierarchy that feels both academic and digitally crisp. The press uses a restrained palette: #e0e0e0 for hairline borders, #f0f0f0 for soft surfaces, and #ffffff for the canvas, with occasional accents of #cc1818 (a scholarly red for sale prices or alerts) and #4ab866 (for success states). The typography relies on system fonts — primarily -apple-system and Segoe UI — at modest sizes, with body text at 16px and headings that rarely exceed 28px, trusting the content's weight rather than typographic drama. Buttons use {rounded.sm} corners (8px), giving them a precise, unpretentious feel, while the search bar employs {rounded.full} pill shapes for a touch of approachability. The overall impression is that of a serious institution that has modernized without sacrificing gravitas — the blue is confident but not aggressive, the spacing generous but not wasteful, and the entire interface feels built for long reading sessions rather than quick transactions.

colors:
  primary: "#3858e9"
  primary-active: "#183ad6"
  primary-disabled: "#ababab"
  ink: "#1e1e1e"
  body: "#32373c"
  muted: "#949494"
  muted-soft: "#cecece"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#cc1818"
  accent-green: "#4ab866"
  accent-gold: "#f0b849"
  accent-purple: "#7d268a"
  accent-blue-dark: "#00356b"
  accent-yellow-soft: "#fff5c9"
  accent-gold-soft: "#ecdc93"
  accent-orange: "#ff9900"
  accent-teal: "#1ea0c3"
  accent-blue-light: "#0693e3"
  accent-blue-mid: "#2679ce"
  accent-blue-bright: "#0a7aff"
  accent-blue-deep: "#0757fe"
  accent-blue-royal: "#2145e6"
  accent-gray-dark: "#444444"
  accent-gray-mid: "#757575"
  accent-gray-light: "#dfdfdf"
  accent-gray-pale: "#ababab"
  accent-navy: "#1e1f26"
  accent-brown: "#591b62"
  accent-blue-ink: "#003388"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
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
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-search:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 48px
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    color: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the brand's deep blue (#3858e9) background with white text. On hover, it shifts to the darker active state (#183ad6). The disabled state uses a muted gray (#ababab) to indicate non-interactivity. All primary buttons use 8px rounded corners and 44px height for comfortable touch targets.

**`button-secondary`** — An outlined variant with a white background, blue text, and a 2px blue border. Used for secondary actions like "Learn More" or "View Details" alongside primary buttons. Maintains the same 44px height and 8px rounded corners for visual consistency.

**`button-tertiary-text`** — A text-only button with no background or border, using the primary blue for its text color. Used for less prominent actions like "Cancel" or "Skip" within forms or modals.

**`button-pill-search`** — A fully rounded pill-shaped button used for search submission or filter actions. Uses the primary blue background with white text, 40px height, and generous horizontal padding for a friendly, approachable feel.

### Navigation
**`nav-bar`** — The top navigation bar, 64px tall with a white background and a subtle bottom border (#e0e0e0). Navigation links use 15px font size with 0.2px letter spacing for a slightly refined, academic feel. Active links are underlined with a 2px blue border.

**`breadcrumb`** — Secondary navigation using 13px caption text in muted gray. The active breadcrumb item switches to the near-black ink color to indicate the current page.

### Cards
**`product-card`** — Book product cards with white backgrounds, 8px rounded corners, and 16px padding. On hover, a subtle box shadow lifts the card. Product images within cards use 4px rounded corners for a softer edge.

### Forms
**`text-input`** — Standard text input fields with white backgrounds, 8px rounded corners, and a 1px hairline border. On focus, the border thickens to 2px and switches to the primary blue for clear visual feedback.

**`search-bar`** — A pill-shaped search input with a soft gray background (#f0f0f0) and 48px height. On focus, a 2px blue border appears. Used primarily in the site header for book and author searches.

### Badges
**`badge-new`** — A small gold (#f0b849) badge with dark text, used to indicate new releases or recently added titles. Uses 4px rounded corners and uppercase 11px font.

**`badge-sale`** — A red (#cc1818) badge with white text, used to indicate discounted prices or special offers. Same sizing and styling as the new badge for visual consistency.

### Footer
**`footer`** — The site footer uses a dark near-black background (#1e1e1e) with white text. Links appear in a lighter muted gray (#cecece) for readability. The footer spans the full width with generous padding of 64px top/bottom and 32px sides.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger menu replaces top nav, product cards stack vertically, search bar collapses to icon-only, footer links stack |
| Tablet | 744–1128px | Two-column product grid, top nav shows limited links with "More" dropdown, search bar remains full but narrower |
| Desktop | 1128–1440px | Full top nav with all links, three-column product grid, search bar at full width, breadcrumbs visible |
| Wide | > 1440px | Max-width container (1440px) centered, additional whitespace on sides, product grid can expand to four columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height
- Search bar and primary buttons use 48px height for comfortable tapping
- Icon buttons and badge elements use minimum 32px touch area
- Navigation links have 40px minimum touch height with adequate spacing

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product grid reduces from 4 columns to 2 columns at tablet, then 1 column at mobile
- Search bar collapses to icon-only trigger on mobile, expanding to full-width overlay on tap
- Footer link columns stack vertically below 744px
- Breadcrumbs hide on mobile, replaced by "Back" button where needed
- Secondary navigation (category filters) collapses to dropdown select below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted color list is heavily polluted with generic web framework colors (multiple blues, grays, and accent colors from WordPress/Shopify defaults). The true brand palette likely has fewer colors; the most distinctive primary appears to be #3858e9, but this should be verified against the actual brand style guide.
- No meta theme-color tag was found, so the browser chrome color is unknown.
- Font-family declarations were limited to system fonts; the brand may use a custom typeface (e.g., Yale's proprietary typeface) that wasn't detected in the extraction.
- Hover states for buttons and links are inferred from common patterns, not extracted from the live site.
- Error states for form inputs (validation colors, error messages) were not extracted.
- Dark mode styling is not present or not detected.
- Sub-brand or section-specific color variations (e.g., for different academic departments or series) are unknown.
- The exact spacing scale and component heights are estimated based on common patterns; actual values may differ.
- No extracted data for modal/dialog styling, tooltips, or notification banners.
- The accent color palette includes many colors that may be from third-party widgets (social icons, payment badges) rather than the brand's own design system.
