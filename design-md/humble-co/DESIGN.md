---
version: alpha
name: "The Humble Co."
source_url: "https://thehumble.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The Humble Co. presents a clean, conscientious oral-care brand built on a foundation of soft, warm neutrals and a single, grounded green — `#108474` — that acts as the brand's quiet, confident signature. The palette is deliberately restrained: a canvas of `#ffffff` and `#f7f5f4` supports a hierarchy of grays from the near-black `#1d1d1d` for primary text, through `#333333` and `#555555` for body copy, down to `#dddddd` and `#eeeeee` for hairlines and soft surfaces. This creates a calm, trustworthy atmosphere that never competes with the product photography. Typography leans on the geometric, humanist clarity of Nunito Sans, with display sizes set at modest weights — the brand trusts whitespace and generous padding over heavy boldface. Every corner is softened: buttons and cards use `{rounded.sm}` (8px) and `{rounded.md}` (12px), while the signature search bar and badge elements go to `{rounded.full}` for a friendly, approachable feel. The overall mood is one of gentle authority — a brand that is serious about sustainability but never preachy, using warm greys and a single accent green to signal both eco-responsibility and everyday comfort. The palette also includes a subtle secondary accent in `#d2815f` (a warm terracotta) and a muted blue `#9ccdfc` for informational elements, adding just enough warmth and personality to keep the system from feeling sterile.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#c1e6e6"
  ink: "#1d1d1d"
  body: "#333333"
  muted: "#555555"
  muted-soft: "#666666"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f7f5f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-terracotta: "#d2815f"
  accent-blue: "#9ccdfc"
  accent-yellow: "#fbcd0a"
  accent-purple: "#a89cc8"
  badge-green: "#108474"
  badge-new: "#fbcd0a"
  error: "#c35121"
  info: "#2f6ed6"
  link: "#2f6ed6"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  link:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    color: "{colors.primary}"
    border-bottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    box-shadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    box-shadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm}"
  badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    color: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    padding: "0 {spacing.lg} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for add-to-cart, subscribe, and checkout flows. It uses the brand green `{colors.primary}` as a solid background with white text, set in `{typography.button-md}` at 600 weight with subtle letter-spacing. On hover, it shifts to `{colors.primary-active}` for a darker, grounded state; disabled state uses `{colors.primary-disabled}` with muted text to signal inactivity without visual noise.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details". It keeps the same typography and height as the primary button but uses a white background with a 2px `{colors.primary}` border and green text. The active state inverts the border to `{colors.primary-active}` and adds a soft surface background.

**`button-tertiary`** — A text-only link-style button for less prominent actions, such as "Cancel" or "Skip". It has no background or border, relying solely on `{colors.primary}` text color and the standard button typography. Padding is kept minimal to align with adjacent content.

**`button-pill`** — A fully rounded variant (`{rounded.full}`) used for promotional badges, filter tags, or compact CTAs in tight spaces. It uses the same green background and white text but at a smaller `{typography.button-sm}` size and reduced padding, making it suitable for inline or badge-like placements.

### Cards
**`product-card`** — The primary container for product listings, featuring a white background, soft rounded corners (`{rounded.md}`), and a subtle box-shadow for depth. The card includes an image area with `{rounded.sm}` corners, product title in `{typography.title-sm}`, price in `{typography.body-md}`, and a short description in `{typography.body-sm}`. On hover, the shadow deepens to signal interactivity. The card uses `{spacing.base}` padding for consistent internal rhythm.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with a white background and a soft bottom border. Navigation links use `{typography.nav-link}` at 15px with 600 weight. The active link is indicated by `{colors.primary}` text color and a 2px green underline. The bar collapses to a hamburger menu on mobile, with the logo centered and cart/account icons on the right.

### Forms
**`text-input`** — Standard text input fields for forms, with a white background, `{rounded.sm}` corners, and a 1px `{colors.hairline}` border. On focus, the border thickens to 2px and turns `{colors.primary}`. Error states use a 2px `{colors.error}` border. The input height is 48px with 12px vertical and 16px horizontal padding for comfortable touch interaction.

### Badges
**`badge`** — Small, fully rounded labels used for product attributes like "Eco-Friendly", "Bestseller", or "New". The default badge uses `{colors.badge-green}` background with white text. A special `badge-new` variant uses `{colors.badge-new}` (yellow) with dark text for highlighting new arrivals. Both use `{typography.badge}` at 11px uppercase with tight tracking.

### Search
**`search-bar`** — A pill-shaped search input (`{rounded.full}`) used in the header or on search pages. It has a white background, 1px `{colors.hairline}` border, and `{typography.body-md}` text. On focus, the border becomes a 2px `{colors.primary}` stroke. The height is 48px with generous horizontal padding for a comfortable typing area.

### Footer
**`footer`** — A full-width footer with a soft `{colors.surface-soft}` background and muted text. Links are styled with `{typography.link}` and turn `{colors.primary}` on hover. The footer uses `{spacing.xxl}` vertical padding and `{spacing.section}` horizontal padding for breathing room. It typically contains columns for product categories, support links, social icons, and newsletter signup.

### Hero
**`hero-section`** — The primary hero banner on the homepage, using a soft `{colors.surface-soft}` background with generous `{spacing.section}` padding. The heading uses `{typography.display-xl}` in `{colors.ink}`, while the subheading uses `{typography.body-md}` in `{colors.muted}`. The hero typically features a large product image or lifestyle photo alongside a primary CTA button.

### Accordion
**`accordion`** — Expandable content panels used for FAQs or product details. Each accordion item has a white background, `{rounded.sm}` corners, and a 1px `{colors.hairline-soft}` border. The header uses `{typography.title-sm}` with `{colors.ink}` and 16px/24px padding. Content area collapses with smooth animation, revealing text in `{typography.body-md}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero padding reduces to 32px; buttons become full-width; search bar moves to collapsible drawer |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses 48px padding; side-by-side content sections; footer stacks in two rows |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses 64px padding; multi-column footer; standard button widths |
| Wide | > 1440px | Max-width container at 1440px; centered layout with increased whitespace; four-column product grid; larger hero imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44x44px touch target
- Product card tap areas extend to full card dimensions
- Accordion headers have 48px minimum height for easy tapping
- Nav bar icons (cart, account, search) are at least 44x44px
- Mobile hamburger menu button is 48x48px

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product grid reduces from 3 columns to 2 at tablet, then 1 at mobile
- Footer columns collapse from 4 to 2 at tablet, then stack vertically at mobile
- Hero section reduces padding and stacks content vertically below 744px
- Search bar becomes an expandable overlay on mobile
- Accordion panels remain single-column at all breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover state colors for secondary and tertiary buttons (only primary-active was reliably extracted)
- Focus ring styles and colors for keyboard navigation
- Error state styling for forms beyond border color (no error message typography or iconography extracted)
- Disabled state styling for text inputs and search bars
- Dark mode palette (not present on live site)
- Sub-brand or seasonal color palettes (e.g., limited edition products)
- Animation timing and easing curves for transitions and hover effects
- Specific box-shadow values for cards and modals (estimated from visual inspection)
- Typography scale for mobile (font sizes may reduce at smaller breakpoints)
- Icon set specifications (social media, cart, account, search icons)
- Loading state and skeleton screen designs
- Modal and overlay component specifications
- Dropdown menu styles for navigation and forms
- Tooltip and popover component designs
