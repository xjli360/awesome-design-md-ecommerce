---
version: alpha
name: "Tilit"
source_url: "https://www.tilitnyc.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Tilit is a kitchen uniform brand built for the working chef — tough, tactile, and unpretentious. The palette leans heavily on industrial neutrals: deep charcoals like `#3a3a3a` and `#494949` form the backbone, while soft off-whites (`#f8f8f8`, `#eeeeee`, `#f2f2f2`) keep the canvas light and breathable. A single shot of red (`#ca1818`) appears as the brand's accent voltage — used sparingly on sale badges, cart counts, and critical CTAs. The typography is a two-type system: Montserrat for clean, modern headings and Barlow for body and button copy, both sans-serif and highly legible at small sizes. Rounded corners are minimal — `{rounded.sm}` (8px) on buttons and `{rounded.md}` (12px) on cards — keeping the feel utilitarian rather than playful. The overall mood is workshop-ready: matte textures, generous padding, and a restrained use of color that lets product photography and craftsmanship take center stage. Tilit's design system feels like a well-worn apron — functional, honest, and built to last.

colors:
  primary: "#ca1818"
  primary-active: "#a31313"
  primary-disabled: "#f5c2c2"
  ink: "#090909"
  body: "#3a3a3a"
  muted: "#656565"
  muted-soft: "#9b9b9b"
  hairline: "#bebebe"
  hairline-soft: "#e6e6e6"
  canvas: "#f8f8f8"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-sale: "#ca1818"
  badge-new: "#28a745"
  badge-soldout: "#dc3545"
  star-rating: "#eb9247"
  accent-warm: "#ddeeee"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Barlow', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Barlow', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Barlow', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Barlow', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Barlow', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Barlow', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Barlow', 'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', 'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Barlow', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow', 'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Barlow', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Barlow', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Barlow', 'Montserrat', sans-serif"
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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-tertiary-hover:
    textColor: "{colors.primary}"
  button-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
    border: "1px solid {colors.hairline}"
  button-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.badge-soldout}"
  select-input:
    backgroundColor: "{colors.surface-card}"
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
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "12px 16px 4px"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "0 16px 12px"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.1)"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-soldout:
    backgroundColor: "{colors.badge-soldout}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    maxWidth: "600px"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    maxWidth: "500px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 40px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-md}"
    padding: "{spacing.sm} 0 {spacing.base}"
  filter-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  cart-icon:
    textColor: "{colors.ink}"
    height: 24px
  cart-count:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  rating-stars-empty:
    color: "{colors.hairline}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Shop Now". Rendered in the brand's signature red (`{colors.primary}`) with white text and an 8px rounded corner (`{rounded.sm}`). On hover, it deepens to `{colors.primary-active}`. The disabled state uses a pale pink `{colors.primary-disabled}` to signal inactivity.

**`button-secondary`** — A ghost-style button with a white background and a subtle `{colors.hairline}` border. Used for "View Details", "Cancel", and secondary checkout actions. Hover adds a soft `{colors.surface-soft}` background and a stronger `{colors.muted}` border.

**`button-tertiary`** — A text-only button with no background or border, used for "Learn More" or "Clear Filters". Hover shifts the text color to `{colors.primary}`.

**`button-pill`** — A fully rounded pill button used in filter strips and category navigation. The active state inverts to a dark `{colors.ink}` background with white text.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with a `{colors.canvas}` background. On scroll, it gains a subtle box-shadow and switches to a solid white `{colors.surface-card}` background. Navigation links are uppercase Montserrat with 0.5px letter spacing. The active link is underlined with a 2px `{colors.primary}` border.

**`nav-link`** — Individual navigation items with `{colors.body}` text that transitions to `{colors.primary}` on hover. Active links use a bottom border accent.

### Forms
**`text-input`** — Standard text input fields with a white background, 1px `{colors.hairline}` border, and 8px rounded corners. On focus, the border thickens to 2px and turns `{colors.primary}`. Error states use a red `{colors.badge-soldout}` border.

**`select-input`** — Dropdown selectors matching the text input styling, used for size, quantity, and filter selections.

**`search-bar`** — A fully rounded pill-shaped search input with a white background and subtle border. On focus, the border becomes 2px `{colors.primary}`.

### Cards
**`product-card`** — Product display cards with a white background and 12px rounded corners (`{rounded.md}`). The image area has rounded top corners only. On hover, the card lifts with a soft box-shadow. Titles use `{typography.title-sm}` and prices use `{typography.body-md}`.

### Badges
**`badge-sale`** — A small red badge with white text, 4px rounded corners, and uppercase 11px font. Used to highlight discounted items.

**`badge-new`** — A green badge (`{colors.badge-new}`) for new arrivals.

**`badge-soldout`** — A red badge (`{colors.badge-soldout}`) for out-of-stock items.

### Footer
**`footer`** — A dark footer section with `{colors.ink}` background and white text. Links are muted gray (`{colors.muted-soft}`) and turn white on hover. The newsletter input is a white field with a red submit button.

### Accordion
**`accordion-header`** — Used for FAQ sections and product descriptions. Headers have no background, use `{typography.title-sm}`, and are separated by a soft `{colors.hairline-soft}` border. Content areas use `{typography.body-md}`.

### Filter Chips
**`filter-chip`** — Pill-shaped filter buttons used in collection pages. Inactive chips have a white background and border. Active chips invert to a dark `{colors.ink}` background.

### Cart
**`cart-icon`** — A simple shopping bag icon in `{colors.ink}`. The cart count badge is a small red circle (`{colors.primary}`) with white text, positioned at the top-right of the icon.

### Dividers
**`divider`** — A 1px horizontal line in `{colors.hairline-soft}` for subtle separation. `divider-strong` uses `{colors.hairline}` for more pronounced breaks.

### Ratings
**`rating-stars`** — Star icons in `{colors.star-rating}` (a warm amber `#eb9247`). Empty stars use `{colors.hairline}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger menu replaces nav links, product cards stack vertically, hero text centers and shrinks to 24px, filter chips collapse into a dropdown, footer stacks links vertically |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but condensed, search bar shrinks to icon-only on scroll, footer uses two-column layout |
| Desktop | 1128–1440px | Full three-column product grid, expanded nav with all links, search bar fully visible, hero section uses full-width imagery |
| Wide | > 1440px | Max-width container at 1440px, content centered, product grid expands to four columns, hero section uses larger typography (display-xl at 42px) |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Filter chips and badge elements are at least 32px tall
- Cart icon and nav links have a minimum 44x44px tap area
- Accordion headers are 48px tall for easy tapping

### Collapsing Strategy
- Primary navigation collapses into a hamburger menu below 744px
- Search bar collapses to an icon-only toggle below 744px, expanding to full width on tap
- Product grid reduces from 4 columns to 2 columns on tablet, to 1 column on mobile
- Filter sidebar collapses into a bottom sheet or dropdown on mobile
- Footer link columns collapse into a single vertical stack below 744px
- Hero section reduces font sizes and centers text alignment on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (exact shadow values, transition timing) could not be reliably extracted
- Error styling for form validation (error messages, icon placement) was not visible in the extracted data
- Dark mode palette is not defined — the site appears to use a light-only theme
- Sub-brand or collection-specific color variations (e.g., seasonal palettes) are not captured
- Animation timing and easing curves (transitions, hover effects) are not specified
- Focus ring styles for keyboard navigation are not documented
- Loading states (spinners, skeleton screens) are not defined
- Modal and overlay component styling (background scrim, close button) is missing
- Tooltip and popover component specifications are absent
- Print stylesheet considerations are not included
