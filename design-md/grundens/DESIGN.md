---
version: alpha
name: "Grundens"
source_url: "https://grundens.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand built for the harshest marine environments, Grundens uses a palette anchored on deep marine navy (#242d35) and a high-voltage safety orange (#fe5000) that cuts through fog, spray, and low light — the same visual logic as a PFD or a channel marker. The primary CTA, the search icon, and the cart badge all carry that orange, a deliberate jolt against the dark, weathered backgrounds (#090b0d, #191919) that dominate the site. The secondary palette introduces a muted sea-foam (#abc7ca) and a cool slate (#242833), colors that read as wet stone and salt-bleached canvas rather than decorative pastels. Typography runs Colfax Web at clean, functional weights — display sizes sit at 400–600 weight, never decorative, always legible at arm's length in a pitching boat. Buttons are generously padded with {rounded.sm} corners, product cards use {rounded.md}, and the overall grid feels industrial and purposeful: wide gutters, dense information, no wasted motion. The brand trusts its product photography — wet neoprene, dripping Gore-Tex, steel hardware — to carry the sensory load, keeping the UI itself as a transparent, fast-loading shell. There is no hero carousel; the homepage leads with a single strong product image and a direct value prop, reflecting a customer who knows what they need and doesn't want to browse.

colors:
  primary: "#fe5000"
  primary-active: "#e04500"
  primary-disabled: "#ffb080"
  ink: "#090b0d"
  body: "#242d35"
  muted: "#242833"
  muted-soft: "#4a5259"
  hairline: "#d0d3d4"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#abc7ca"
  accent-blue: "#334fb4"
  dark-bg: "#191919"
  dark-surface: "#121212"

typography:
  display-xl:
    fontFamily: "'colfax-web', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'colfax-web', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'colfax-web', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'colfax-web', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'colfax-web', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'colfax-web', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'colfax-web', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'colfax-web', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'colfax-web', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'colfax-web', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
  link:
    fontFamily: "'colfax-web', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'colfax-web', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'colfax-web', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 44px
  search-icon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
  category-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.title-md}"
    padding: 16px 0
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 0 0 16px 0

## Components

### Buttons
**`button-primary`** — The primary call-to-action, always filled with Grundens orange (#fe5000). Used for "Add to Cart", "Shop Now", and primary checkout actions. On hover, darkens to `{colors.primary-active}`. Disabled state uses `{colors.primary-disabled}` with reduced opacity. Text is white, uppercase, 600 weight.

**`button-secondary`** — A white button with dark text for secondary actions like "View Details" or "Learn More". Maintains the same 48px height and padding as primary for visual consistency. Outline variant uses a transparent background with a 1px solid `{colors.hairline}` border.

**`button-dark`** — Used on dark backgrounds (hero sections, footer). Inverted primary: black fill with white text. Same dimensions and corner radius as the other button variants.

### Cards
**`product-card`** — White card with `{rounded.md}` corners containing a product image, title, price, and optional badge. The image area uses `{colors.surface-soft}` as a placeholder background. Cards sit on a white or light gray canvas with generous spacing between them. No shadow — the brand relies on clean borders and consistent layout.

**`product-card-badge`** — Small orange pill badge overlaid on product images for "New", "Sale", or "Best Seller" labels. Uses `{typography.badge}` with tight padding and `{rounded.sm}` corners.

### Navigation
**`nav-bar`** — Full-width white bar at 64px height. Contains the brand logo (left), category links (center, uppercase), and utility icons (right: search, account, cart). On scroll, reduces to 56px. The cart icon carries a `{colors.primary}` badge for item count.

**`category-nav`** — Secondary navigation below the main bar for subcategories (e.g., "Jackets", "Bibs", "Waders"). Links are uppercase, 14px, 600 weight. Active state underlined with `{colors.primary}`.

### Forms
**`text-input`** — Standard input field with white background, `{rounded.sm}` corners, and 1px `{colors.hairline}` border. Focus state uses `{colors.body}` border. Error state uses a red border (exact hex not extracted — see Known Gaps). Padding is generous at 12px vertical / 16px horizontal.

### Search
**`search-bar`** — Pill-shaped input with `{rounded.full}` corners on a light gray background. Used in the mobile menu and desktop header. The search icon is a standalone orange circle (`{rounded.full}`) that triggers the search action.

### Footer
**`footer-section`** — Full-width dark section (`{colors.ink}`) with white text. Contains link columns, newsletter signup, and legal text. Links use `{typography.link}` at 14px, 500 weight. Dividers between columns use `{colors.muted-soft}`.

### Hero
**`hero-section`** — Full-viewport-height section on dark background (`{colors.dark-bg}`) with white text. Features a single large product image or lifestyle photo, a headline in `{typography.display-xl}`, and a `button-primary` CTA. No carousel — static, direct, product-focused.

### Accordion
**`accordion-header`** — Used for product details (size guide, materials, care instructions) and FAQ sections. Header is clickable, 16px padding top/bottom, with a chevron icon that rotates on expand. Content area collapses with smooth transition.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger menu replaces nav links, product cards stack vertically, search bar moves to header overlay |
| Tablet | 744–1128px | Two-column product grid, category nav collapses to dropdown, search icon remains in header |
| Desktop | 1128–1440px | Full nav bar visible, three-column product grid, search bar expands inline |
| Wide | > 1440px | Max-width container at 1440px, centered content, larger product images |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Nav links have 48px tap area (padding + hit area)
- Accordion headers have 48px minimum tap height
- Icon buttons (search, cart, account) minimum 44x44px tap area

### Collapsing Strategy
- Main nav links collapse into hamburger menu below 744px
- Category sub-nav collapses into select dropdown below 744px
- Product filters collapse into accordion panel on mobile
- Footer link columns stack vertically below 744px
- Search bar collapses to icon-only on mobile, expands to full-width overlay on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list includes several dark grays (#090b0d, #191919, #121212) that may represent a dark mode variant, but the exact dark mode palette and toggle behavior could not be confirmed.
- Font weight values for Colfax Web are inferred from common usage (400, 500, 600, 700); the exact weight for each type style may vary.
- Hover and focus states for text inputs (border color, shadow) were not extractable from static HTML/CSS.
- Error state colors for forms (red border, error text) were not present in the extracted palette.
- The secondary blue (#334fb4) appears in the palette but its usage context (links, badges, accents) could not be determined.
- Button hover animations, transition durations, and easing curves were not extractable.
- The exact corner radius values are estimated based on visual inspection of screenshots; the brand may use slightly different values.
- Product card shadow or border properties were not extractable from the available data.
- The brand may use a specific grid system or column count that could not be confirmed.
- Typography line-height and letter-spacing values are estimated based on common web typography best practices for the font.
