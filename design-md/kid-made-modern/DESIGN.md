---
version: alpha
name: "Kid Made Modern"
source_url: "https://kidmademodern.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A craft brand that treats a child's workspace with the same seriousness as a design studio, anchored on a tricolor palette of forest-green #49945f, teal #2daaac, and cornflower #3d7db0 — colors that feel plucked from a premium marker set rather than a primary-school classroom. The brand's visual system runs on Hepta Slab, a sturdy serif with generous ball terminals that reads as both playful and authoritative, giving project titles and product names a hand-lettered warmth without sacrificing legibility. White canvas (`{colors.canvas}`) dominates product pages and project galleries, letting the craft materials — pom-poms, pipe cleaners, acrylic paint — supply the texture and color. Buttons and interactive elements use the forest-green as their primary voltage, with `{rounded.sm}` corners that feel friendly but not cartoonish; the brand trusts the inherent messiness of craft photography over decorative UI embellishment. Navigation is deliberately sparse — a single top bar with logo, search, and cart — because the real interface is the grid of craft kits and the "Projects" tab that surfaces step-by-step video tutorials. The checkout flow inherits Shopify's default widget styling, which introduces a slight visual break from the brand's custom palette, but the product detail pages maintain a clean, airy hierarchy: a large hero image, a short description in `{typography.body-md}`, and a prominent "Add to Cart" button in `{colors.primary}`. The overall mood is "modern art classroom" — organized enough for a parent to navigate quickly, colorful enough to hold a child's attention, and designed around the principle that the best interface is the one that gets out of the way and lets you make something.

colors:
  primary: "#49945f"
  primary-active: "#3a7a4c"
  primary-disabled: "#b3d4bc"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#2daaac"
  accent-blue: "#3d7db0"
  accent-yellow: "#f5c542"
  star-rating: "#f5c542"
  badge-sale: "#e74c3c"
  badge-new: "#2daaac"

typography:
  display-xl:
    fontFamily: "'Hepta Slab', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Hepta Slab', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Hepta Slab', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Hepta Slab', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Hepta Slab', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Hepta Slab', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  project-title:
    fontFamily: "'Hepta Slab', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-tertiary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-icon-circle:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  button-icon-circle-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "2px solid {colors.primary}"
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
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid #e74c3c"
  select-input:
    backgroundColor: "{colors.canvas}"
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
    padding: "0 {spacing.lg}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.lg}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.06)"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
    objectFit: "contain"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    typography: "{typography.badge}"
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-sale:
    typography: "{typography.badge}"
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-banner-image:
    width: "100%"
    height: "400px"
    objectFit: "cover"
    rounded: "{rounded.md}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.canvas}"
    textDecoration: "none"
  footer-link-hover:
    typography: "{typography.link}"
    color: "{colors.accent-teal}"
    textDecoration: "underline"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.canvas}"
    marginBottom: "{spacing.base}"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 36px
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 36px
    border: "1px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    height: 28px
    width: 28px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} 0"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 8px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 8px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: "16px"
  star-rating-empty:
    color: "{colors.hairline}"
    fontSize: "16px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop Now", and primary form submissions. Rendered in `{colors.primary}` (#49945f) with white text and `{rounded.sm}` corners. On hover, shifts to `{colors.primary-active}` (#3a7a4c). Disabled state uses `{colors.primary-disabled}` (#b3d4bc) to signal non-interactivity while maintaining brand color presence. Height is 48px with 14px 28px padding for comfortable touch targets.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Learn More". Uses a white background with a 2px `{colors.primary}` border and matching text color. Active state fills the background with `{colors.surface-soft}` and darkens the border to `{colors.primary-active}`. Maintains the same 48px height and `{rounded.sm}` corners as the primary button for visual consistency.

**`button-tertiary`** — A text-only button for subtle actions like "Cancel" or "Clear Filters". Transparent background with `{colors.primary}` text. On hover/active, gains a `{colors.surface-soft}` background. No border, no shadow — the lightest visual weight in the button hierarchy.

**`button-icon-circle`** — A circular 40px icon button used for search, cart, and account icons in the navigation. Uses `{colors.primary}` background with white icon. The `{rounded.full}` shape creates a friendly, approachable feel. An outlined variant (`button-icon-circle-outline`) exists for less prominent placements, using a white background with a 2px `{colors.primary}` border.

### Cards
**`product-card`** — The primary content container for the product grid. A white card with `{rounded.md}` corners and a subtle `boxShadow` (0 1px 4px rgba(0,0,0,0.06)) that creates gentle depth without distraction. On hover, the shadow deepens to 0 4px 12px rgba(0,0,0,0.1) to signal interactivity. The card image uses `object-fit: contain` to ensure craft product photos display without cropping — important for showing the full shape of kits and supplies. Product titles use `{typography.title-sm}` in `{colors.ink}`, prices use `{typography.body-sm}` in `{colors.body}`. Badges for "New" or "Sale" items are positioned absolutely in the top-left corner using `{rounded.xs}` pill shapes.

**`hero-banner`** — The full-width promotional banner at the top of the homepage and campaign pages. Uses `{colors.surface-soft}` background with `{typography.display-lg}` for the headline. The banner image spans full width at 400px height with `object-fit: cover`. A single CTA button in `{colors.primary}` sits below the headline with generous `{spacing.lg}` margin. The banner has no rounded corners — it spans edge-to-edge to create a immersive entry point.

### Navigation
**`nav-bar`** — A clean, minimal top navigation bar at 72px height. White background with `{colors.ink}` text for the logo and `{colors.muted}` for inactive nav links. Active nav links gain `{colors.primary}` text color with a 2px bottom border in the same green. On scroll, the bar becomes sticky with a subtle `boxShadow` (0 2px 8px rgba(0,0,0,0.08)) to separate it from page content. The search bar lives in the nav as a `{rounded.full}` pill with `{colors.surface-soft}` background and `{colors.muted}` placeholder text — on focus, it expands with a 2px `{colors.primary}` border.

**`filter-chip`** — Used in category and project listing pages for filtering by age range, craft type, or difficulty. Rendered as `{rounded.full}` pills with `{colors.surface-soft}` background and a 1px `{colors.hairline}` border. Active chips flip to `{colors.primary}` background with white text, making the selected filter immediately visible in a grid of options. Height is 36px with 6px 16px padding for easy tapping on mobile.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, and checkout forms. White background with 1px `{colors.hairline}` border and `{rounded.sm}` corners. On focus, the border thickens to 2px and switches to `{colors.primary}` for clear visual feedback. Error state uses a red (#e74c3c) border. Height is 48px with 12px 16px padding for comfortable typing.

**`select-input`** — Dropdown select for quantity, size, or variant choices. Shares the same dimensions and border styling as `text-input` for visual consistency across form elements. The dropdown arrow uses `{colors.muted}` to avoid competing with the content.

**`quantity-selector`** — A compact input group for adjusting item quantities on the product detail page and cart. Consists of a central text field with two small circular buttons (+ and -) on either side. The buttons use `{colors.surface-soft}` background and are 28px square for precise tapping. The entire group is 40px tall with `{rounded.sm}` corners and a 1px `{colors.hairline}` border.

### Footer
**`footer`** — A dark footer section using `{colors.ink}` (#1a1a1a) background with white text. Links use `{typography.link}` in white with no underline, switching to `{colors.accent-teal}` (#2daaac) with underline on hover. Section headings use `{typography.title-sm}` with generous `{spacing.base}` bottom margin. The footer is padded with `{spacing.xxl}` top and bottom for breathing room, with `{spacing.lg}` horizontal padding to match the nav bar.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product grid switches to 2 columns; hero banner height reduces to 250px; filter chips stack vertically; footer links stack in single column; search bar moves to full-width below nav |
| Tablet | 744–1128px | Nav bar shows all links with reduced padding; product grid uses 3 columns; hero banner at 350px height; filter chips wrap in 2 rows; footer uses 2-column layout |
| Desktop | 1128–1440px | Full nav bar with all links; product grid uses 4 columns; hero banner at 400px height; filter chips in single horizontal row; footer uses 3-column layout |
| Wide | > 1440px | Max-width container at 1440px with centered content; product grid can expand to 5 columns; hero banner at 450px height; additional whitespace around content sections |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Filter chips are 36px tall — slightly below the 44px guideline but acceptable for a craft site where fine motor control is expected
- Quantity selector buttons are 28px square — the smallest interactive element, used only in cart context where precision is needed
- Icon buttons in nav are 40px circles — comfortable for thumb tapping on mobile
- Product card images are tappable to navigate to product detail, with the entire card area as the hit target

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer
- The product filter sidebar (if present on desktop) collapses into a "Filter" button that opens a modal overlay on mobile
- The footer's multi-column link sections collapse into accordion-style expandable sections on mobile
- Hero banner text overlays collapse to stack below the image on mobile, ensuring text remains readable at small sizes
- Product image galleries collapse from thumbnail strip to swipeable carousel on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is limited to three hex values (#49945f, #2daaac, #3d7db0) — the brand may use additional accent colors (yellows, oranges, pinks) in marketing materials that weren't captured in the extraction
- No extracted hex for the brand's primary text color (#1a1a1a assumed), muted text, or surface colors — these are estimated based on common e-commerce patterns
- Font-family extraction only returned "Hepta Slab" and "object-fit: contain" — the body copy font family is assumed to be a system sans-serif stack; the actual body font may differ
- No hover state colors were extracted for buttons, links, or cards — active/disabled states are estimated
- Error state styling (form validation, error messages, empty states) is not present in the extracted data
- The brand's Shopify checkout flow likely uses Shopify's default widget colors, which may not match the brand palette — the exact checkout styling is unknown
- No data on loading states, skeleton screens, or spinner animations
- Dark mode is not supported and no color tokens for dark backgrounds exist
- Sub-brand or seasonal campaign palettes (e.g., holiday collections, licensed characters) are not captured
- The extracted colors may include Shopify Pay (#5a31f4), Klarna (#ffb3c7), or Afterpay (#b2fce4) widget colors that were not fully filtered — the three provided hexes appear brand-appropriate but should be verified against the actual site CSS
- No typography scale for mobile (font sizes may reduce at smaller viewports)
