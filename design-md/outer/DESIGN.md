---
version: alpha
name: "Outer"
source_url: "https://liveouter.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Outer is an outdoor furniture brand that reimagines the backyard as an extension of the home, not a separate, less comfortable space. The brand's visual language is anchored in a deep, confident navy (`#223843`) that reads as both premium and grounded — it appears on primary navigation, key CTAs, and footer backgrounds, creating a consistent frame of reliability. Against this, a crisp white canvas (`#ffffff`) keeps the product photography and lifestyle imagery breathing, while a soft silver-grey (`#dedede`) appears in hairline borders and subtle dividers, echoing the aluminum and steel frames of the furniture itself. The accent palette introduces a vibrant sky blue (`#1990c6`) and a deeper oceanic teal (`#136f99`) that appear in hover states, secondary badges, and promotional highlights — these blues feel organic to the outdoor setting, not arbitrary brand decoration. A near-black (`#121212`) provides high-contrast body text for readability in bright sunlight, and a system blue (`#007aff`) handles standard link and interactive affordances. Typography runs Barlow, a geometric sans-serif with warm, open apertures that balance modernity with approachability — display sizes sit at moderate weights (500–600) rather than heavy 700+, letting the furniture's silhouette and material texture carry the visual weight. The system uses generous `{rounded.sm}` (8px) on cards and buttons — soft enough to feel friendly, not so pill-shaped that it undermines the clean, architectural lines of the product. Spacing is generous: `{spacing.section}` (64px) separates major content blocks, while `{spacing.lg}` (24px) and `{spacing.xl}` (32px) create comfortable breathing room around product grids and feature panels. The overall effect is a brand that feels like a well-edited outdoor room — intentional, uncluttered, and quietly luxurious, where every design decision serves the goal of making the outdoors feel as livable as indoors.

colors:
  primary: "#223843"
  primary-active: "#1a2d36"
  primary-disabled: "#a0b4bd"
  ink: "#121212"
  body: "#223843"
  muted: "#6b7b84"
  muted-soft: "#9aabb3"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f6f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#1990c6"
  accent-blue-hover: "#136f99"
  accent-blue-soft: "#e6f4fb"
  link-blue: "#007aff"
  star-rating: "#223843"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    padding: 14px 32px
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
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-accent:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-blue}"
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
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-blue}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid #d32f2f"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "4/3"
  product-card-content:
    padding: "{spacing.base} {spacing.base} {spacing.lg}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 600
  product-card-badge:
    backgroundColor: "{colors.accent-blue-soft}"
    textColor: "{colors.accent-blue}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  feature-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  feature-panel-accent:
    backgroundColor: "{colors.accent-blue-soft}"
    textColor: "{colors.accent-blue}"
    typography: "{typography.title-sm}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    textColor: "{colors.on-primary}"
    opacity: 1
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "#d32f2f"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Uses the brand's deep navy (`#223843`) with white text, 8px rounded corners, and 48px height. On hover, it shifts to `#1a2d36` for a subtle darkening effect. The disabled state uses a muted grey-blue (`#a0b4bd`) to signal unavailability without visual noise. Padding of 14px top/bottom and 32px left/right gives it a substantial, confident presence.

**`button-secondary`** — An outlined variant with a white background and navy text, framed by a 2px solid navy border. Used for secondary actions like "Learn More" or "View Details." Hover state fills the background with the soft surface tone (`#f5f6f7`) and darkens the border to `#1a2d36`. Same height and rounded corners as primary for visual consistency.

**`button-tertiary-text`** — A text-only button with no background or border. Uses navy text at 15px/600 weight. Appears in contexts where a minimal interaction is needed, such as "Cancel" in forms or "See All" in content strips.

**`button-pill-accent`** — A pill-shaped button using the accent blue (`#1990c6`) for promotional or highlight CTAs. Full rounded corners, smaller padding (10px 24px), and smaller typography (13px/600). Used for limited-time offers, new collection announcements, or seasonal campaigns.

### Cards
**`product-card`** — The primary product display unit. A white card with 8px rounded corners, no padding on the container (padding is handled by child elements). The image area occupies a 4:3 aspect ratio with rounded top corners only. Content area receives 16px horizontal padding and 24px bottom padding. The title uses 16px/600 weight in ink, while the price appears in 16px/600 weight in navy to draw attention.

**`product-card-badge`** — A small, soft badge overlaid on product images or within card content. Uses a light blue background (`#e6f4fb`) with accent blue text (`#1990c6`), 4px rounded corners, and uppercase 11px/600 typography. Used for "New," "Best Seller," or "Eco-Friendly" labels.

### Navigation
**`top-nav`** — A fixed-position navigation bar at 72px height with white background and a subtle bottom border (`#e8e8e8`). Navigation links use 14px/500 weight, uppercase with 0.5px letter spacing. Active links appear in navy, inactive in muted grey. The nav houses the logo, main category links, search icon, and cart icon.

**`nav-link-active`** and **`nav-link-inactive`** — Define the two states for top navigation items. Active links use the primary navy to indicate current page or section. Inactive links use the muted grey (`#6b7b84`) to recede visually. Both share the same typography for consistent alignment.

### Forms
**`text-input`** — Standard text input fields with white background, 1px hairline border (`#dedede`), 8px rounded corners, and 48px height. On focus, the border thickens to 2px and shifts to accent blue (`#1990c6`). Error state uses a red border (`#d32f2f`). Padding of 12px top/bottom and 16px left/right provides comfortable cursor placement.

**`search-bar`** — A slightly differentiated input for search functionality. Uses a soft background (`#f5f6f7`) instead of white, with the same rounded corners and height as text inputs. On focus, it transitions to white background with a 2px accent blue border, signaling active search mode.

### Footer
**`footer`** — A full-width footer with navy background (`#223843`) and white text. Contains columns for customer support, company info, product categories, and social links. Links appear at 80% opacity, increasing to full opacity on hover. Section padding of 64px top/bottom and 32px left/right creates a substantial closing statement for each page.

### Badges
**`badge-new`** — A pill-shaped badge using accent blue (`#1990c6`) with white text. Used to flag newly launched products or collections. The full rounded shape and uppercase 11px/600 typography make it distinct from the softer product-card badge.

**`badge-sale`** — A red pill badge (`#d32f2f`) for sale or clearance items. Same shape and typography as the new badge but with urgency-inducing red. Used sparingly to maintain impact.

### Dividers
**`divider`** — A full-width horizontal line at 1px height using the standard hairline color (`#dedede`). Used between major sections or content blocks.

**`divider-soft`** — A lighter version using `#e8e8e8` for subtler separation within cards or between related content items.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger navigation, reduced hero padding (32px), stacked footer columns, smaller display typography (display-xl drops to 32px) |
| Tablet | 744–1128px | Two-column product grid, expanded navigation with dropdowns, hero padding at 48px, two-column footer, display-xl at 40px |
| Desktop | 1128–1440px | Three-column product grid, full top-nav visible, hero at full section padding (64px), four-column footer, full display-xl at 48px |
| Wide | > 1440px | Max-width container at 1440px centered, four-column product grid, extended hero with larger imagery, all typography at maximum sizes |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch targets on mobile
- Product card tap targets extend to full card area, not just text
- Navigation hamburger icon is 48x48px for easy thumb access
- Cart and search icons in top nav are 44x44px minimum
- Form inputs maintain 48px height for comfortable touch interaction

### Collapsing Strategy
- Top navigation collapses to hamburger menu at < 744px, with full-height overlay drawer
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer columns collapse from 4 (desktop) to 2 (tablet) to stacked single column (mobile)
- Hero section reduces vertical padding from 64px to 32px on mobile, with text centered instead of left-aligned
- Product card images switch from 4:3 to 1:1 aspect ratio on mobile for better vertical scrolling
- Search bar collapses to icon-only on mobile, expanding to full-width overlay on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow elevation, scale, or border change) could not be reliably extracted from static CSS
- Error styling for form validation (error messages, iconography, animation) is inferred from common patterns but not confirmed
- Dark mode palette is not present on the live site — all extracted colors assume light mode
- Sub-brand or collection-specific palettes (e.g., "Coastal," "Modern," "Rustic") may exist but were not detected
- Loading states, skeleton screens, and spinner animations are not documented
- Focus ring styles (outline, offset, color) for keyboard accessibility are not confirmed
- Modal and overlay patterns (sizing, animation, scrim opacity) are inferred from common practice
- Toast/notification component styling is absent from extracted data
- Dropdown menu styling (shadow, z-index, animation) for navigation sub-menus is not captured
- Quantity selector and variant picker (color swatches, size options) styling details are missing
- Mobile bottom navigation or tab bar patterns are not present in extracted data
- Checkbox and radio button custom styling is not documented
- Tooltip and popover component specifications are absent
- Print stylesheet behavior is unknown
