---
version: alpha
name: "Annabelle's Book Club LA"
source_url: "https://www.annabellesbookclubla.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy anchor (#003399) grounds Annabelle's Book Club LA — a bookstore that reads more like a warmly lit living room than a retail grid. That blue, the most distinctive signal in the palette, wraps the primary navigation, the footer, and every key CTA, while a secondary navy (#01426a) and a lighter blue (#24588d) build a layered, oceanic depth across the site. The canvas is a soft off-white (#eeeeee), not a clinical white, which keeps the experience feeling papery and analog — like the pages of a well-loved paperback. Body text runs in a dark charcoal (#232323) with secondary copy in mid-gray (#555555), and the typography (falling back through system sans-serif stacks) leans on Font Awesome for iconography rather than a custom brand typeface, suggesting a lean, content-first build. The design avoids hard corners in key interaction points — buttons and input fields use a gentle 8px radius (`{rounded.sm}`), while cards and modals step up to 12px (`{rounded.md}`) for a soft, approachable feel. There is no hero video, no heavy illustration system; the brand trusts book covers as its primary visual language, letting the products speak. The overall mood is studious but not austere — a calm, blue-lit space where the inventory is the decoration.

colors:
  primary: "#003399"
  primary-active: "#002a7a"
  primary-disabled: "#99b3e6"
  ink: "#232323"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#dddddd"
  canvas: "#eeeeee"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-navy: "#01426a"
  accent-light-blue: "#24588d"

typography:
  display-xl:
    fontFamily: "'Georgia', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Georgia', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Georgia', 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Arial', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
    height: auto
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    textDecoration: underline
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
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid #d32f2f"
  textarea:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  select:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-bar-mobile:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: "0 {spacing.base}"
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    rounded: "{rounded.xs}"
  nav-link-active:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    rounded: "{rounded.xs}"
    backgroundColor: "rgba(255, 255, 255, 0.15)"
  nav-link-hover:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    rounded: "{rounded.xs}"
    backgroundColor: "rgba(255, 255, 255, 0.1)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0, 0, 0, 0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1.5"
    objectFit: cover
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 600
    marginTop: "{spacing.sm}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "#d32f2f"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 720px
  hero-subtitle:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
    maxWidth: 600px
    marginTop: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "2px solid {colors.primary}"
  search-icon:
    textColor: "{colors.muted}"
    fontSize: 16px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.85
  footer-link-hover:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 1
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
    marginBottom: "{spacing.base}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.xl}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.xl} 0"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  category-chip-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  pagination:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "0 12px"
    height: 40px
  quantity-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "0 12px"
    height: 40px
  cart-item:
    backgroundColor: "{colors.surface-card}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  cart-total:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
    width: "100%"
  checkout-button-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
    width: "100%"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.body}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.primary}"
  breadcrumb-link-hover:
    typography: "{typography.caption}"
    textColor: "{colors.primary-active}"
    textDecoration: underline
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    margin: "0 {spacing.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's deep navy (#003399) with white text and a gentle 8px radius. Used for add-to-cart, checkout, and submit actions. On hover, the background deepens to `{colors.primary-active}` (#002a7a). The disabled state (`{colors.primary-disabled}`) uses a muted blue (#99b3e6) to signal inactivity while maintaining brand consistency.

**`button-secondary`** — A bordered alternative for less prominent actions. Rendered on the soft canvas background (`{colors.canvas}`) with a subtle `{colors.hairline}` border. On hover, the background shifts to `{colors.surface-soft}` for a light fill effect. Ideal for "Continue Shopping" or "Cancel" actions.

**`button-tertiary-text`** — A text-only link styled as a button, using the primary blue for its text color. No background or border — used for inline actions like "View Details" or "Learn More." On hover, the text color deepens to `{colors.primary-active}` and an underline appears.

### Cards
**`product-card`** — The core inventory display unit. A white card (`{colors.surface-card}`) with a 12px radius and a soft border (`{colors.hairline-soft}`). Contains a product image (cropped to a 1:1.5 book-cover aspect ratio with `{rounded.sm}` corners), a title in `{typography.title-sm}`, the author name in `{typography.body-sm}` at `{colors.body}`, and the price in a bold `{typography.body-md}`. On hover, the card gains a subtle shadow and a slightly stronger border.

**`product-card-image`** — The book cover image within a product card. Uses `object-fit: cover` and a 1:1.5 aspect ratio to maintain consistent book proportions. The 8px radius (`{rounded.sm}`) softens the cover edges without distorting the artwork.

### Navigation
**`nav-bar`** — A full-width, 64px bar in the brand's primary navy (`{colors.primary}`). White navigation links sit on this dark background with 8px horizontal padding and a 4px radius. The active state uses a semi-transparent white overlay (`rgba(255, 255, 255, 0.15)`) to indicate the current page. On mobile, the bar compresses to 56px height.

**`nav-link`** — Individual navigation items within the bar. White text in `{typography.nav-link}` (15px, weight 600, 0.5px letter-spacing). The hover state adds a lighter overlay (`rgba(255, 255, 255, 0.1)`), and the active state uses a slightly more opaque one.

### Forms
**`text-input`** — Standard text input for search, email signup, and contact forms. A white background with a 1px `{colors.hairline}` border and 8px radius. On focus, the border thickens to 2px and switches to `{colors.primary}` for clear visual feedback. Error state uses a red border (#d32f2f) to indicate validation issues.

**`search-bar`** — A pill-shaped (`{rounded.full}`) search input with 20px horizontal padding. The full radius gives it a friendly, approachable feel. On focus, the border becomes a 2px primary blue. A search icon in `{colors.muted}` sits inside the input, aligned to the left.

### Badges
**`badge-new`** — A small, uppercase label in the primary navy with white text, 4px radius, and tight padding (2px 8px). Used to flag newly added inventory.

**`badge-sale`** — Same structure as `badge-new` but with a red (#d32f2f) background for sale or discount items.

**`badge-out-of-stock`** — Uses `{colors.muted-soft}` (#999999) for a neutral, low-priority indicator that an item is unavailable.

### Footer
**`footer`** — A full-width navy (`{colors.primary}`) footer with white text at 85% opacity for links. Headings use `{typography.title-sm}` with a 24px bottom margin. The footer is generously padded with 48px vertical spacing and 24px horizontal padding. Link hover restores full opacity.

### Category Chips
**`category-chip`** — Pill-shaped (`{rounded.full}`) filter chips for browsing by genre or category. The default state uses `{colors.surface-soft}` with dark text. The active state fills with `{colors.primary}` and white text. On hover, the background shifts to `{colors.hairline-soft}` for a subtle lift.

### Pagination
**`pagination`** — Standard numbered pagination for browsing multiple pages of inventory. The active page uses a navy background (`{colors.primary}`) with white text and 8px radius. Inactive pages have no background but gain `{colors.surface-soft}` on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar compresses to 56px height; product cards stack in a single column; search bar reduces padding; hero section padding reduces to 32px vertical; category chips wrap to multiple rows; footer links stack vertically |
| Tablet | 744–1128px | Product cards display in a 2-column grid; nav-bar remains at 64px; hero section keeps 64px vertical padding; search bar maintains full pill shape |
| Desktop | 1128–1440px | Product cards in a 3- or 4-column grid; full nav-bar with all links visible; hero section at full `{spacing.section}` padding; search bar centered with max-width |
| Wide | > 1440px | Content max-width capped at 1440px with auto margins; product cards may expand to 4-5 columns; hero text max-width scales proportionally |

### Touch Targets
- All buttons and links maintain a minimum 44px height for touch accessibility
- Category chips have 32px minimum height with 16px horizontal padding
- Search bar and text inputs are 48px tall for comfortable tapping
- Nav links have 32px minimum touch area (8px padding on each side)
- Pagination buttons are 36px minimum with 12px horizontal padding

### Collapsing Strategy
- On mobile, the nav-bar collapses to a hamburger menu; full links are hidden behind a toggle
- Product card grids collapse from 4 columns to 2 columns on tablet, to 1 column on mobile
- Category chips collapse from a single horizontal scrollable row to a wrapped multi-row layout on mobile
- Footer link columns collapse from 3-4 columns to a single vertical stack on mobile
- Hero section reduces vertical padding from 64px to 32px on mobile
- Search bar reduces horizontal padding from 20px to 12px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface was detected; the site relies on system fonts (Arial, Georgia) and Font Awesome for icons. A dedicated brand font may exist but wasn't extractable from the live site.
- Hover and active states for most components are inferred from common patterns; actual site behavior may differ.
- Error styling for forms (validation messages, error icons) was not extractable; a red (#d32f2f) border is assumed based on convention.
- Dark mode support was not detected; the palette assumes a light-only experience.
- The extracted color list is dominated by blues and grays, which may indicate a limited palette or a site that hasn't been fully themed. The primary (#003399) is the most distinctive and is assumed to be the brand anchor.
- No meta theme-color was found, suggesting the site may not have a PWA or mobile browser chrome configuration.
- The site does not appear to run on Shopify (platform-shopify: False), so checkout components are speculative.
- Animation and transition durations were not extractable; a standard 200-300ms ease-in-out is assumed.
- Focus ring styling (outline, box-shadow) for keyboard accessibility was not extractable.
- Loading states (skeleton screens, spinners) were not observed on the live site.
- The extracted font-family list only includes Font Awesome variants, not body or heading fonts. The typography block uses system font stacks as a best-guess.
