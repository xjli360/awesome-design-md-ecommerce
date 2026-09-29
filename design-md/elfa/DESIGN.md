---
version: alpha
name: "Elfa"
source_url: "https://www.elfa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Elfa is a Swedish-born organization brand that speaks in quiet, confident tones — a system built on deep navy blues (#224466, #222299, #222288) and forest greens (#119977, #117711, #118877), anchored by a near-black theme color (#2d2926) that grounds the entire experience. The palette reads like a well-edited wardrobe: primary blues (#224466) carry the weight of navigation and structure, while accent greens (#119977) appear as thoughtful punctuation — perhaps on sale badges, sustainability callouts, or drawer-front highlights. There is no loud red or aggressive orange; the brand trusts depth over volume. The canvas is presumed white (#ffffff), letting the rich jewel tones of `{colors.primary}` and `{colors.primary-active}` do the heavy lifting on buttons, links, and interactive elements. Typography follows a clean sans-serif stack (likely system-native or a geometric like Gotham or Proxima Nova), with `{typography.display-xl}` at a restrained 28px and `{typography.button-md}` at 16px — nothing shouts. Corners are softly rounded (`{rounded.sm}` at 8px for buttons, `{rounded.md}` at 12px for cards), avoiding both the harshness of zero-radius and the playfulness of pills. The overall mood is Scandinavian utility meets premium quietude: every pixel feels considered, every color has a job, and the white space between components is as important as the components themselves. This is a system for people who believe that organization is not about hiding things, but about giving everything a rightful place.

colors:
  primary: "#224466"
  primary-active: "#222299"
  primary-disabled: "#223388"
  ink: "#2d2926"
  body: "#223333"
  muted: "#224433"
  muted-soft: "#225522"
  hairline: "#224488"
  hairline-soft: "#225533"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#119977"
  accent-green-light: "#118877"
  accent-navy-dark: "#222244"
  accent-navy-deep: "#222266"
  badge-sale: "#119977"
  badge-new: "#222299"
  star-rating: "#222255"
  scrim: "#2d2926"

typography:
  display-xl:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 12px 22px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    textColor: "{colors.primary-active}"
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.primary-active}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  search-bar-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(45, 41, 38, 0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    height: 56px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.hairline-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  category-tile-hover:
    backgroundColor: "{colors.hairline-soft}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.md} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the Elfa experience. Uses the deep navy `{colors.primary}` (#224466) background with white text, set in `{typography.button-md}` at 16px weight 600. Corners are softly squared at `{rounded.sm}` (8px). On hover/active, shifts to `{colors.primary-active}` (#222299). Disabled state uses `{colors.primary-disabled}` (#223388). Padding is 14px vertical, 24px horizontal, with a fixed height of 48px for consistent alignment across forms and product pages.

**`button-secondary`** — An outlined variant for less prominent actions. White background with a 2px solid `{colors.primary}` border, same typography and height as primary. On active, border shifts to `{colors.primary-active}` and background to `{colors.surface-soft}`. Used for "Compare" or "Save for later" actions.

**`button-tertiary-text`** — A text-only button with no background or border. Uses `{colors.primary}` text color and `{typography.button-md}`. Active state darkens to `{colors.primary-active}`. Reserved for secondary inline actions like "Cancel" or "Learn more."

**`button-accent-green`** — A special-purpose button using the accent green `{colors.accent-green}` (#119977). Slightly shorter at 40px with 10px/20px padding. Used for sustainability callouts, eco-friendly product badges, or seasonal promotions.

### Cards
**`product-card`** — The primary content container for product listings. White background with a subtle `{colors.hairline-soft}` border and `{rounded.md}` (12px) corners. On hover, the border strengthens to `{colors.hairline}` and a soft shadow appears (`0 4px 12px rgba(45, 41, 38, 0.08)`). The image area uses `{rounded.md}` on top corners only, creating a natural visual hierarchy. Text uses `{typography.body-sm}` for product names and `{typography.caption}` for pricing.

**`category-tile`** — Used for navigation and browsing by room or product type. Light gray background (`{colors.surface-soft}`) with `{rounded.md}` corners and `{typography.title-sm}`. On hover, background shifts to `{colors.hairline-soft}`. Padding is `{spacing.lg}` (24px) all around, creating generous touch targets.

### Navigation
**`nav-bar`** — The top-level site navigation, fixed at 72px height with a white background and a thin `{colors.hairline-soft}` bottom border. Links use uppercase `{typography.nav-link}` at 14px weight 600. Active links show a 2px `{colors.primary}` bottom border and primary text color; inactive links use `{colors.muted}`.

**`nav-link-active`** — Active navigation state with transparent background, primary text color, and a 2px solid bottom border in `{colors.primary}`. Creates a clear visual anchor for the current section.

**`nav-link-inactive`** — Default navigation state with transparent background and `{colors.muted}` text color. No bottom border.

### Forms
**`text-input`** — Standard text input field with white background, `{colors.body}` text, and a 1px `{colors.hairline}` border. Corners are `{rounded.sm}` (8px). On focus, border thickens to 2px `{colors.primary}`. Error state uses `{colors.primary-active}` border. Height is 48px with 12px/16px padding for comfortable typing.

**`search-bar`** — The primary search input, similar to text-input but with `{rounded.md}` (12px) corners for a slightly softer feel. Maintains the same focus and error states. Used in the header and on search results pages.

### Badges
**`badge-sale`** — A small promotional badge using the accent green `{colors.badge-sale}` (#119977) background. Set in uppercase `{typography.badge}` at 11px weight 700 with 0.5px letter spacing. Corners are `{rounded.xs}` (4px) with 2px/8px padding. Used for discounts and promotions.

**`badge-new`** — A "New" badge using the navy `{colors.badge-new}` (#222299) background. Same typography and dimensions as the sale badge. Used for newly launched products or collections.

### Hero
**`hero-section`** — The full-width hero banner at the top of landing pages. Uses the near-black `{colors.ink}` (#2d2926) background with white text in `{typography.display-xl}`. Padding is `{spacing.section}` (64px) vertical and `{spacing.lg}` (24px) horizontal. The primary CTA inside uses `{typography.button-md}` at 16px with 16px/32px padding and a 56px height for prominence.

### Footer
**`footer`** — The site footer with `{colors.ink}` background and white text. Uses `{typography.body-sm}` for content. Padding is `{spacing.xxl}` (48px) vertical and `{spacing.lg}` (24px) horizontal. Links use `{colors.hairline-soft}` with a hover state of `{colors.on-primary}`.

**`footer-link`** — Footer navigation links in `{colors.hairline-soft}` with `{typography.link}` at 14px weight 500. On hover, text color shifts to `{colors.on-primary}` for clear interaction feedback.

### Accordion
**`accordion-header`** — Used for product specifications, FAQs, and filter panels. White background with `{colors.ink}` text in `{typography.title-sm}`. Padding is `{spacing.base}` (16px) vertical and `{spacing.md}` (12px) horizontal, with a `{colors.hairline-soft}` bottom border.

**`accordion-content`** — The expandable content area beneath accordion headers. White background with `{colors.body}` text in `{typography.body-sm}`. Padding is `{spacing.md}` (12px) top, `{spacing.md}` (12px) sides, and `{spacing.lg}` (24px) bottom for comfortable reading.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero section reduces padding to 32px; search bar moves to full-width below nav; category tiles become 2-column grid |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links with "More" dropdown; hero maintains 48px padding; category tiles in 3-column grid; footer links in 2-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links visible; hero at 64px padding; category tiles in 4-column grid; footer links in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px with centered content; four-column product grid; extended category tiles; hero content max-width at 1200px |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets are the full card area, not just text links
- Accordion headers are 48px minimum height for easy tapping
- Category tiles have 24px padding creating generous tap zones
- Mobile nav hamburger icon is 44x44px with 8px padding

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with slide-out drawer
- Product grid reduces from 4 columns to 3 to 2 to 1 as viewport narrows
- Hero section reduces vertical padding from 64px to 48px to 32px
- Footer links collapse from 4-column to 2-column to single-column
- Category tiles reduce from 4-column to 3-column to 2-column
- Search bar moves from inline in nav to full-width below nav on mobile
- Product filters collapse to accordion or modal on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components could not be fully extracted; only primary and secondary buttons have confirmed hover/active colors
- Error styling for text inputs (iconography, helper text placement) is inferred from common patterns rather than extracted
- Dark mode values are not available; the brand does not currently appear to support a dark theme
- Sub-brand or seasonal color palettes (e.g., holiday, collaboration) were not detected
- Typography font family is inferred as Gotham or similar geometric sans-serif; no explicit font-face declarations were found in the extracted CSS
- Loading states (skeleton screens, spinners) were not captured
- Animation durations and easing curves are not specified
- Dropdown and select menu styling is not documented
- Checkbox and radio button styling is not available
- Modal/dialog overlay styling (backdrop, close button, animation) is not captured
- Tooltip and popover styling is missing
- Table and data grid styling is not documented
- Print stylesheet behavior is unknown
