---
version: alpha
name: "Cowboy"
source_url: "https://cowboy.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A Belgian e-bike brand that paints its digital world in near-black (#1d1d1d) and warm stone (#f1eee9), with a single green accent (#569d5f) that appears only where the bike’s battery, range, or ride metrics live — never on decorative elements. The brand treats its product photography as the primary design system: full-bleed hero images of the bike in motion against foggy European landscapes, with type set in SuisseIntl at modest weights (400–600) and generous line heights (1.4–1.6) that never compete with the visual. Buttons are pill-shaped (`{rounded.full}`) and use the near-black as background, while secondary actions float as underlined text links in a muted #737373. The checkout and configurator flows lean into a lighter canvas (#f5f5f5) with card-based layouts (`{rounded.md}` at 12px) that feel like selecting a bike in a showroom rather than filling out a form. The color story is deliberately restrained: no bright blues, no red CTAs, no gradient overlays — just the bike’s own aluminum frame and the green pulse of its battery indicator. The footer collapses into a dense, single-column stack on mobile, with legal links in #6b7280 and social icons in the same near-black as the header. The overall effect is less "tech startup" and more "industrial design portfolio" — the bike is the hero, and the interface is its quiet, well-mannered docent.

colors:
  primary: "#1d1d1d"
  primary-active: "#292929"
  primary-disabled: "#737373"
  ink: "#1d1d1d"
  body: "#232323"
  muted: "#737373"
  muted-soft: "#a3a3a3"
  hairline: "#d4d4d4"
  hairline-soft: "#e5e5e5"
  canvas: "#f5f5f5"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#569d5f"
  accent-green-soft: "#dff0fd"
  warm-stone: "#f1eee9"
  warm-stone-soft: "#f1e8da"
  warm-stone-dark: "#e5e0dc"
  legal-link: "#6b7280"
  star-rating: "#e3bf78"
  scrim: "#181817"

typography:
  display-xl:
    fontFamily: "'SuisseIntl', 'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -1px
  display-lg:
    fontFamily: "'SuisseIntl', 'Inter', sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'SuisseIntl', 'Inter', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'SuisseIntl', 'Inter', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'SuisseIntl', 'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'SuisseIntl', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'SuisseIntl', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'SuisseIntl', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'SuisseIntl', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'SuisseIntl', 'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'SuisseIntl', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'SuisseIntl', 'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'SuisseIntl', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'SuisseIntl', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'SuisseIntl', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'SuisseIntl', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0

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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    fontWeight: 600
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline-soft}"
  search-field-segment:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: 8px 16px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: 8px 0
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  category-tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "4/3"
  product-card-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  configurator-step:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
    border: "1px solid {colors.hairline}"
  configurator-step-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
    border: "2px solid {colors.primary}"
  configurator-option:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  configurator-option-selected:
    backgroundColor: "{colors.accent-green-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.accent-green}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "48px 24px"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    hoverTextColor: "{colors.on-primary}"
  footer-legal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.legal-link}"
    typography: "{typography.caption-sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "80px 24px"
  hero-image:
    rounded: "{rounded.none}"
    aspectRatio: "16/9"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  scrim-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.4
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.warm-stone-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
  modal:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
    boxShadow: "0 4px 24px rgba(0,0,0,0.12)"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Order Now", "Configure", and "Book Test Ride". Rendered as a pill-shaped button in near-black (#1d1d1d) with white text. On hover, shifts to a slightly lighter near-black (#292929). Disabled state fades to #737373 with white text, signaling the action is unavailable. Padding is generous at 14px 32px to accommodate the pill shape.

**`button-secondary`** — Used for "Learn More" and "Compare Models" actions. White background with a 1px hairline border (#d4d4d4) and near-black text. Hover state adds a subtle shadow. Disabled state fades to #f5f5f5 background with #a3a3a3 text.

**`button-tertiary-text`** — Text-only underlined link used for "View Details" and "Read Reviews". No background, near-black text with underline. Hover state darkens the text to #292929. Used sparingly to avoid visual clutter.

**`button-accent-green`** — Reserved for battery-related actions, range calculators, and eco-mode toggles. Uses the brand's green accent (#569d5f) as background with white text. Pill-shaped and smaller than primary buttons (10px 24px padding). Hover state darkens the green slightly.

### Navigation
**`top-nav`** — A fixed 72px header with a white background and a subtle bottom border (#ebebeb). Contains the Cowboy logo on the left, nav links in the center, and a "Shop" / "Test Ride" CTA on the right. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

**`nav-link-active`** — Active navigation link with bold weight (600) and near-black color. Used for the current page or section.

**`nav-link-inactive`** — Inactive navigation link in muted gray (#737373). Hover state transitions to near-black.

### Cards
**`product-card`** — The primary card for displaying bike models in the shop grid. White background, 12px rounded corners, 16px padding, and a subtle hairline border. Contains a product image (4:3 aspect ratio, 8px rounded corners), model name, price, and a badge for "New" or "Sale". Hover state adds a subtle shadow and slightly elevates the card.

**`product-card-badge`** — A small, green badge positioned at the top-left of the product image. Uses the accent green (#569d5f) with white text and uppercase 11px font. Padding is tight (4px 8px) to avoid overlapping the image.

### Configurator
**`configurator-step`** — A step in the bike customization flow (frame color, accessories, battery). Light gray background (#f5f5f5), 12px rounded corners, 24px padding, and a 1px hairline border. Active step gets a 2px near-black border and white background.

**`configurator-option`** — An individual option within a configurator step (e.g., "Matte Black" frame color). Soft gray background (#f6f6f6), 8px rounded corners, 12px 16px padding. Selected state uses a light green background (#dff0fd) with a green border (#569d5f).

### Footer
**`footer`** — A dark footer section with near-black background (#1d1d1d) and white text. Contains columns for "Shop", "Support", "Company", and "Legal". Links are in muted gray (#a3a3a3) and turn white on hover. Padding is generous at 48px 24px.

**`footer-legal`** — The legal bar at the bottom of the footer, with smaller text (#6b7280) and a subtle top border. Contains copyright, privacy policy, and terms of service links.

### Hero
**`hero-section`** — The full-width hero section on the homepage and landing pages. White background with large display text (48px) and a full-bleed product image (16:9 aspect ratio). Padding is 80px 24px on desktop, reducing to 48px 16px on mobile.

**`scrim-overlay`** — A semi-transparent black overlay (#181817 at 40% opacity) used on hero images to improve text readability. Applied as a gradient from bottom to top.

### Badges
**`badge-new`** — A small green badge used to indicate new models or features. Green background (#569d5f), white text, uppercase 11px font, 2px 6px padding, and 4px rounded corners.

**`badge-sale`** — A warm stone badge (#e5e0dc) used for sale or promotion items. Near-black text, same typography as `badge-new`.

### Modals
**`modal`** — A centered modal dialog used for "Quick View" and "Test Ride Booking". White background, 12px rounded corners, 24px padding, and a subtle box shadow. Overlay is a semi-transparent black (#181817 at 50% opacity).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger nav, reduced hero padding (48px 16px), product cards stack vertically, configurator steps become full-width, footer collapses to single column |
| Tablet | 744–1128px | Two-column product grid, top nav remains visible but links collapse to icons, hero text reduces to 36px, configurator uses two-column layout |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links visible, hero text at 48px, configurator uses three-column layout |
| Wide | > 1440px | Max-width container at 1440px, centered content, hero image scales to fill but maintains aspect ratio |

### Touch Targets
- All interactive elements (buttons, links, icons) have a minimum touch target of 44x44px
- Product card images are tappable and navigate to the product detail page
- Configurator options are at least 48px tall for easy tapping
- Footer links have 16px vertical padding for comfortable tapping

### Collapsing Strategy
- Top nav collapses to hamburger menu on mobile (< 744px)
- Product grid collapses from 3 columns to 2 columns on tablet, to 1 column on mobile
- Configurator steps collapse from 3 columns to 2 columns on tablet, to 1 column on mobile
- Footer columns collapse from 4 columns to 2 columns on tablet, to 1 column on mobile
- Hero section reduces padding and font size on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links were inferred from common patterns; exact hover colors (e.g., button-primary hover) were not extractable from the live site
- Error styling for form inputs (e.g., invalid email, missing fields) was not observed; a red accent (#c13515) is assumed but not confirmed
- Dark mode is not implemented on the live site; all colors are light-mode only
- Sub-brand palettes (e.g., for Cowboy Cross, Cowboy ST models) were not distinguishable from the main palette
- Animation and transition durations (e.g., button hover, card elevation) were not extractable; 200ms ease-in-out is assumed
- The exact font weight for display-xl (48px) was inferred from common usage; the extracted font-family list did not include weight values
- The accent green (#569d5f) appears in battery/range indicators but its exact usage context (icon, text, background) was not fully observed
- The warm stone palette (#f1eee9, #f1e8da, #e5e0dc) appears in background sections but its exact role (e.g., hero background vs. card background) was not confirmed
- The star rating color (#e3bf78) was extracted from a single instance; its usage across reviews is assumed but not verified
- The legal link color (#6b7280) was extracted from footer links; hover state color was not observed
- The modal overlay opacity (50%) was inferred from common patterns; exact opacity was not extractable
- The configurator option selected state (green background + border) was inferred from the extracted green accent; exact styling may vary
