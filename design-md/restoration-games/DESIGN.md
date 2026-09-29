---
version: alpha
name: "Restoration Games"
source_url: "https://restorationgames.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A board-game publisher that treats its catalog like a museum of play — every title is a restored classic, and the site communicates that mission through a restrained palette anchored on a deep institutional blue (#003388) that reads as archival rather than playful. That blue appears in the primary header, footer bars, and key navigation elements, while a secondary accent of #2ea3f2 adds a bright, sky-like lift to interactive states and hovered links. The canvas is a warm off-white (#fafafa) with card surfaces in pure white (#ffffff), creating a clean, readable hierarchy for game boxes and product photography. Typography relies on Montserrat for headings — a geometric sans-serif with a slightly architectural feel — and Open Sans for body copy, giving the interface a stable, editorial rhythm. Buttons use a modest {rounded.sm} radius that avoids both the hard edge of finance and the pill-shaped friendliness of consumer apps; this is a brand that values precision over whimsy. The top navigation bar is compact at 60px, with dropdown menus that reveal subcategories like "Restored Games" and "Upcoming Releases" — a taxonomy that reinforces the restoration narrative. Product cards are simple: a white background, a game-box image, the title in Montserrat at 18px weight 600, and a muted price line. There is no badge system for discounts or ratings; the brand trusts the game itself to sell. The footer is dense with links, social icons, and a newsletter signup, all set against the #003388 background with white text. The overall impression is of a specialty publisher that knows its audience — collectors, hobbyists, and nostalgia-seekers — and builds a site that feels like a well-organized library rather than a discount bin.

colors:
  primary: "#003388"
  primary-active: "#2ea3f2"
  primary-disabled: "#bcc8c9"
  ink: "#23282d"
  body: "#3e3e3e"
  muted: "#555555"
  muted-soft: "#7e7e7e"
  hairline: "#d9d9d9"
  hairline-soft: "#e2e2e2"
  canvas: "#fafafa"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-purple: "#974df3"
  accent-teal: "#29c4a9"
  accent-orange: "#ef8f61"
  error: "#c13515"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
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
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 1px {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
    padding: "0 {spacing.lg}"
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
  footer-link-hover:
    textColor: "{colors.primary-active}"
  social-icon:
    width: 24px
    height: 24px
    textColor: "{colors.on-primary}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
  newsletter-button:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-icon:
    textColor: "{colors.muted}"
    width: 18px
    height: 18px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-restored:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Pre-Order", and key conversion points. Rendered in the brand's deep blue (#003388) with white uppercase Montserrat text at 14px weight 600. On hover, the background shifts to the bright blue accent (#2ea3f2), providing a clear interactive signal. The disabled state uses a muted teal-gray (#bcc8c9) with white text. The button has a modest 4px radius and 44px height, with 12px vertical and 24px horizontal padding.

**`button-secondary`** — An outlined variant with a white background, 2px solid blue border, and blue text. Used for secondary actions like "Learn More" or "View Details" alongside primary buttons. On hover, it fills with the primary blue and inverts to white text. Height and padding match the primary button for consistent alignment in button groups.

**`button-tertiary`** — A text-only button with no background or border, used for less prominent actions like "Cancel" or "See All". The text is blue and underlines on hover. Padding is minimal (12px 16px) to keep the footprint small.

### Navigation
**`nav-bar`** — A fixed-height 60px bar in the primary blue, containing the brand logo on the left and navigation links on the right. Links use Montserrat at 14px weight 500 with 0.3px letter spacing, all in white. The bar has no border or shadow, relying on the color contrast with the white page content below.

**`nav-dropdown`** — A white card that appears on hover over navigation items, with a subtle box shadow and 4px radius. Contains subcategory links in the same nav-link typography but in dark ink (#23282d). The dropdown has 8px padding around its content.

### Cards
**`product-card`** — The primary content container for game listings, used on category pages and search results. A white card with a 1px hairline border (#d9d9d9) and a light box shadow. Contains the game box image (full width), the game title in Montserrat 16px weight 600, and the price in Open Sans 14px muted gray. On hover, the shadow deepens to indicate interactivity. The card has 16px padding and a 4px radius.

**`hero-section`** — A full-width banner used on the homepage and landing pages, with a deep blue background and white text. The headline uses display-xl (36px Montserrat weight 700) and the CTA is a white button with blue text. The section has 64px vertical padding and 24px horizontal padding.

### Forms
**`text-input`** — Standard form input for search, newsletter signup, and checkout fields. A white background with a 1px hairline border and 4px radius. On focus, the border becomes the primary blue with a matching 1px box-shadow ring. Height is 44px with 10px vertical and 14px horizontal padding.

**`newsletter-input`** — A slightly shorter input (40px) used specifically in the footer signup form. Same styling as text-input but paired with a newsletter-button that uses the bright blue accent for visual distinction.

### Badges
**`badge-new`** — A small teal (#29c4a9) pill used to flag newly restored games. Uses uppercase Montserrat at 11px weight 700 with 2px vertical and 8px horizontal padding and a 2px radius.

**`badge-sale`** — An orange (#ef8f61) badge for discounted titles. Same sizing and typography as the new badge.

**`badge-restored`** — A purple (#974df3) badge indicating a game that has been restored from an older edition. Same sizing and typography.

### Tags
**`category-tag`** — A pill-shaped filter tag used on category pages, with a soft gray background (#f4f4f4) and dark body text. The active state fills with the primary blue and white text. Both states use a full pill radius and 4px vertical / 12px horizontal padding.

### Footer
**`footer`** — A full-width footer in the primary blue with white text. Contains three columns: navigation links, social media icons, and a newsletter signup form. Links are Open Sans 14px and turn the bright blue accent on hover. The section has 48px vertical padding and 24px horizontal padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Navigation collapses to hamburger menu; product cards stack in single column; hero text reduces to 24px; footer columns stack vertically |
| Tablet | 744–1128px | Navigation links visible but condensed; product cards in 2-column grid; hero maintains 28px text; footer in 2 columns |
| Desktop | 1128–1440px | Full navigation with dropdowns; product cards in 3-column grid; hero at full 36px display; footer in 3 columns |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; additional whitespace around hero |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch target recommendations.
- Navigation hamburger icon is 48px × 48px on mobile.
- Category tags and badges are at least 32px tall for easy tapping.
- Social media icons in footer are 44px × 44px tap areas.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu that opens a full-screen overlay with navigation links in the primary blue background.
- Product card grids reduce from 4 columns on wide screens to 1 column on mobile.
- The hero section reduces vertical padding from 64px to 32px on mobile.
- Footer columns stack from 3 columns to 1 column on mobile, with the newsletter signup appearing first.
- Breadcrumb navigation hides on mobile, replaced by a "Back" button on product pages.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is heavily weighted toward blues and grays, which may reflect WordPress admin defaults (the site appears to use Divi theme) rather than the brand's true design system. The primary blue (#003388) and accent blue (#2ea3f2) are the most distinctive and likely intentional, but the presence of many similar blues (#006799, #0073aa, #0085ba, #008ec2) suggests framework defaults bleeding through.
- Hover and active states for most components (beyond buttons) could not be reliably extracted from static CSS.
- Error state styling for form inputs (validation colors, error messages) is not present in the extracted data.
- Dark mode or high-contrast mode variants are not defined.
- The exact font weights and sizes for Montserrat and Open Sans are inferred from common usage patterns; the site may use additional weights (e.g., Montserrat 300 for light text) that were not captured.
- Spacing values (padding, margins, grid gaps) are estimated from typical Divi theme defaults and may not match the exact production values.
- The newsletter signup form's success/error states (confirmation messages, inline validation) are not documented.
- Product card hover effects (image zoom, overlay text) are assumed based on common e-commerce patterns but not confirmed from extracted data.
- The site's use of icons (social media, search, cart) is assumed to be from a standard icon set (likely Font Awesome or Divi's built-in icons) but exact icon styles are not documented.
- Sub-brand or seasonal color variations (e.g., holiday themes, limited edition packaging) are not captured.
- The extracted font list includes "ETmodules" which is a Divi theme icon font — this is not a standard typography choice and should be ignored for text styling.
