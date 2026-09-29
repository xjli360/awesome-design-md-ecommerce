---
version: alpha
name: "Megababe"
source_url: "https://megababebeauty.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Megababe Beauty is a body-care brand that feels like a confident, witty friend who knows exactly what you need. The palette is anchored by a deep, almost-black ink (`#303030`) and a warm off-white canvas (`#f3f3f3`), creating a clean, editorial backdrop that lets product photography and playful accents pop. The brand's signature voltage comes from a vibrant primary blue (`#2332d5`), a bold, energetic hue that appears on primary CTAs, badges, and key interactive elements, paired with a softer, more approachable blue (`#dee6ff`) for secondary surfaces and hover states. A supporting cast of accent colors—a fresh green (`#29845a`), a warm amber (`#ffaa00`), a soft coral (`#ea5455`), and a playful purple (`#7367f0`)—adds personality without overwhelming the system. Typography is a study in contrast: the elegant, serifed `Fraunces` is used for display and title treatments, lending a touch of editorial sophistication, while the rounded, all-caps `Titan One` injects a dose of playful, retro energy into badges, buttons, and small headers. The overall mood is confident, clean, and slightly irreverent—a brand that takes body care seriously but doesn't take itself too seriously. Corners are generally soft (`{rounded.sm}` for buttons, `{rounded.md}` for cards), and the generous use of `{spacing.lg}` and `{spacing.xl}` between sections creates a breathable, premium feel. The system is built for a Shopify-powered e-commerce experience, with clear hierarchy, strong CTAs, and a focus on product discovery.

colors:
  primary: "#2332d5"
  primary-active: "#1a26b0"
  primary-disabled: "#a0a8f0"
  ink: "#303030"
  body: "#444444"
  muted: "#616161"
  muted-soft: "#808080"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#f3f3f3"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#29845a"
  accent-green-soft: "#cdfee1"
  accent-amber: "#ffaa00"
  accent-amber-soft: "#ffef9d"
  accent-coral: "#ea5455"
  accent-purple: "#7367f0"
  accent-blue-soft: "#dee6ff"
  badge-new: "#8051ff"
  badge-sale: "#f72119"
  star-rating: "#ffaa00"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Fraunces', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Fraunces', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Fraunces', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Fraunces', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Fraunces', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Fraunces', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Titan One', 'Arial Black', Impact, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Titan One', 'Arial Black', Impact, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Titan One', 'Arial Black', Impact, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Titan One', 'Arial Black', Impact, sans-serif"
    fontSize: 10px
    fontWeight: 400
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    borderColor: "{colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    borderColor: "{colors.accent-coral}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.body-md}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-coral}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    borderColor: "{colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: 16px 20px
  accordion-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: 16px 20px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  star-rating:
    textColor: "{colors.star-rating}"
    fontSize: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the brand's signature blue (`{colors.primary}`) with white uppercase text in Titan One. On hover, it deepens to `{colors.primary-active}`. The disabled state uses `{colors.primary-disabled}`. All primary buttons have `{rounded.sm}` corners and a compact 44px height.
**`button-secondary`** — An outlined or ghost variant on a white canvas with `{colors.ink}` text. The active state shifts the background to `{colors.surface-soft}`. Used for less prominent actions like "Learn More" or "Cancel".
**`button-ghost`** — A text-only button with `{colors.primary}` text and no background. Ideal for inline actions or secondary links within content areas.
**`button-pill-primary`** — A smaller, fully rounded (`{rounded.full}`) variant of the primary button, used for filters, tags, or quick-add actions. Uses `{typography.button-sm}`.
**`button-pill-outline`** — The outline counterpart to the pill primary, with a white background and `{colors.ink}` text. Used for filter toggles and secondary quick actions.

### Cards
**`product-card`** — The core product display unit on collection and search pages. Features a white background (`{colors.surface-card}`), `{rounded.md}` corners, and a soft shadow. The image area is also `{rounded.md}`. The title uses `{typography.title-sm}`, and the price uses `{typography.body-md}`. Sale prices are rendered in `{colors.accent-coral}`. Badges (e.g., "NEW", "SALE") are positioned at the top-left of the image, using `{colors.badge-new}` or `{colors.badge-sale}` with `{typography.badge}` and `{rounded.xs}` padding.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar at 72px height on a white canvas. Navigation links use `{typography.nav-link}` in Titan One uppercase. The active link is `{colors.primary}`, while inactive links are `{colors.muted}`. The bar includes a logo, main links, and a search icon.
**`nav-link-active`** / **`nav-link-inactive`** — Defines the active and inactive states for top-level navigation links. Active links use the brand blue; inactive links use a muted gray.

### Forms
**`text-input`** — Standard text input fields with a white background, `{colors.ink}` text, `{rounded.sm}` corners, and a 44px height. The active state gains a `{colors.primary}` border. The error state uses a `{colors.accent-coral}` border.
**`search-bar`** — A fully rounded (`{rounded.full}`) search input on a `{colors.surface-soft}` background, 48px tall. On focus, it transitions to a white background with a `{colors.primary}` border.
**`quantity-selector`** — A compact, horizontally-laid-out input for adjusting product quantities. Uses `{rounded.sm}` corners and a 40px height.

### Footer
**`footer-section`** — A dark footer with an `{colors.ink}` background and white text. Links are `{colors.muted-soft}` and turn white on hover. Uses `{typography.body-sm}` for general text and `{typography.link}` for links.

### Other Components
**`hero-section`** — The primary hero banner on the homepage. Uses a white or light gray background with `{colors.ink}` text in `{typography.display-xl}`. The CTA is a `button-primary` variant with extra padding (`14px 32px`) and a 48px height.
**`accordion`** — Used for FAQs and product details. A white background with `{colors.ink}` text in `{typography.title-sm}`, `{rounded.sm}` corners, and `16px 20px` padding. The active state shifts the background to `{colors.surface-soft}`.
**`star-rating`** — A simple star-based rating display using `{colors.star-rating}` (amber) at 16px font size.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero text scales down to `{typography.display-md}`; search bar becomes full-width; footer links stack. |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but may condense; hero uses `{typography.display-lg}`; sidebars collapse into accordions. |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero uses `{typography.display-xl}`; multi-column footer. |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can expand to four columns; increased whitespace (`{spacing.section}`) between sections. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet accessibility guidelines.
- Icon-only buttons (e.g., search, cart) have a minimum touch area of 44x44px.
- Product card CTAs are at least 44px tall.
- Accordion headers are at least 44px tall for easy tapping.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer.
- The product filter sidebar collapses into a bottom sheet or modal on mobile.
- Multi-column footers collapse into a single column with accordion-style sections.
- Hero sections may reduce to a single image with text overlay instead of a split layout.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components (only primary/secondary button and link hover states were reliably extracted).
- Focus and active states for text inputs and search bars (only border color changes were observed).
- Error and success states for forms beyond the text-input error border.
- Dark mode color palette (not present on the live site).
- Specific sub-brand or collection-specific color palettes (e.g., limited edition drops).
- Dropdown menu styles and behavior for the navigation.
- Modal, drawer, and overlay component styles.
- Tooltip and popover styling.
- Loading spinner and skeleton screen designs.
- Detailed typography scale for mobile (font sizes may scale down).
- Specific shadow values for cards and elevated components.
- Animation and transition timing curves.
- Icon set and illustration style guidelines.
