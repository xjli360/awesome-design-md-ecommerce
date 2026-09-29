---
version: alpha
name: "Diptyque"
source_url: "https://www.diptyqueparis.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A Parisian olfactory atelier that treats every surface as a canvas for understated luxury, Diptyque’s digital presence mirrors its boutiques: quiet, tactile, and deliberately restrained. The palette is anchored by a warm off-white canvas (`#f8f8f8`) and soft greys (`#e8e8e8`, `#f3f3f3`) that evoke the matte paper of its iconic oval labels, while a deep charcoal ink (`#1d1f22`) grounds body text and primary navigation. Signature accents emerge sparingly: a muted sage green (`#2e5538`) for botanical cues, a restrained crimson (`#d12f37`) for limited-edition markers, and a pale cerulean (`#1284e7`) for interactive links and hover states — never shouting, always purposeful. The typography relies on a system-native stack (`-apple-system`, `Helvetica Neue`, `Roboto`, `sans-serif`) at modest weights (400–600), with display sizes rarely exceeding 24px; the brand trusts negative space and the poetry of product names over typographic drama. Rounded corners are minimal (`{rounded.xs}` 4px on buttons, `{rounded.sm}` 8px on cards), preserving the crisp geometry of the Diptyque oval, while the single `{rounded.full}` pill shape is reserved for the search bar — a quiet invitation to explore. The overall effect is one of hushed elegance: a digital space that feels like a scented letter, not a storefront.

colors:
  primary: "#1d1f22"
  primary-active: "#292c30"
  primary-disabled: "#e5e7eb"
  ink: "#111214"
  body: "#292c30"
  muted: "#5f5f5f"
  muted-soft: "#8d8f9a"
  hairline: "#cccccc"
  hairline-soft: "#e6e5e5"
  canvas: "#f8f8f8"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#2e5538"
  accent-green-light: "#9ee2b0"
  accent-red: "#d12f37"
  accent-blue: "#1284e7"
  accent-blue-soft: "#dbedfb"
  badge-green: "#018937"
  badge-green-active: "#01a241"
  badge-green-dark: "#01702d"
  surface-strong: "#e8e8e8"
  scrim: "#111214"

typography:
  display-xl:
    fontFamily: "-apple-system, 'Helvetica Neue', 'Roboto', 'Segoe UI', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
  display-lg:
    fontFamily: "-apple-system, 'Helvetica Neue', 'Roboto', 'Segoe UI', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.3px
  display-md:
    fontFamily: "-apple-system, 'Helvetica Neue', 'Roboto', 'Segoe UI', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.2px
  title-md:
    fontFamily: "-apple-system, 'Helvetica Neue', 'Roboto', 'Segoe UI', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.15px
  title-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', 'Roboto', 'Segoe UI', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1px
  body-md:
    fontFamily: "-apple-system, 'Helvetica Neue', 'Roboto', 'Segoe UI', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', 'Roboto', 'Segoe UI', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, 'Helvetica Neue', 'Roboto', 'Segoe UI', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', 'Roboto', 'Segoe UI', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.15px
  badge:
    fontFamily: "-apple-system, 'Helvetica Neue', 'Roboto', 'Segoe UI', system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, 'Helvetica Neue', 'Roboto', 'Segoe UI', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', 'Roboto', 'Segoe UI', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, 'Helvetica Neue', 'Roboto', 'Segoe UI', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, 'Helvetica Neue', 'Roboto', 'Segoe UI', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
    backgroundColor: "{colors.canvas}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.base}"
  product-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-limited:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    height: 480px
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.3
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
    opacity: 0.8
  footer-link-hover:
    color: "{colors.on-primary}"
    opacity: 1
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    height: 44px
    width: 44px
  quantity-selector-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in deep charcoal (`{colors.primary}`) with white text and a subtle 4px corner radius (`{rounded.xs}`). On hover, it deepens to `{colors.primary-active}`; when disabled, it fades to `{colors.primary-disabled}` with muted text. Used for "Add to Bag", "Checkout", and primary form submissions. **`button-secondary`** — An outlined variant on a white canvas (`{colors.canvas}`) with a `{colors.hairline}` border that darkens to `{colors.ink}` on hover. The background shifts to `{colors.surface-soft}` on active state. Ideal for "View Details" or secondary checkout actions. **`button-ghost`** — A text-only button with no background or border, using `{colors.body}` text that darkens to `{colors.ink}` on hover with a subtle `{colors.surface-soft}` background. Used for dismissible actions, "Cancel", or inline links. **`button-pill`** — A fully rounded pill shape (`{rounded.full}`) reserved for promotional badges, filter tags, and quick-add actions. Compact at 36px height with tighter padding.

### Navigation
**`nav-bar`** — A fixed 72px header on a white canvas (`{colors.canvas}`) with a soft hairline bottom border (`{colors.hairline-soft}`). Navigation links use uppercase `{typography.nav-link}` at 13px with 0.5px letter-spacing, evoking the typographic restraint of a French perfume house. The active link is underlined with a 2px solid `{colors.ink}` border; inactive links render in `{colors.muted}`. The brand logo sits centered or left-aligned, with a search icon and cart icon on the right. **`nav-link-active`** — The selected navigation item, distinguished by a bottom border rather than a background color change, maintaining the brand's minimal aesthetic.

### Forms & Inputs
**`text-input`** — A clean 48px input field on a white background with a `{colors.hairline}` border and 4px corner radius (`{rounded.xs}`). On focus, the border switches to `{colors.ink}` for clear visual feedback. Error states use `{colors.accent-red}` for the border. Placeholder text uses `{colors.muted-soft}`. Used for email signup, search queries, and checkout forms. **`search-bar`** — The only fully rounded element (`{rounded.full}`) in the system, sitting on a `{colors.surface-soft}` background with a subtle border. On focus, it expands to a white background with a `{colors.ink}` border, signaling active input. Height is 48px with comfortable 10px 20px padding.

### Cards & Products
**`product-card`** — A white card (`{colors.surface-card}`) with an 8px corner radius (`{rounded.sm}`) and no shadow — the brand relies on generous whitespace and the product photography itself. The image area has rounded top corners (`{rounded.sm} {rounded.sm} 0 0`), while the title uses `{typography.title-sm}` and the price uses `{typography.body-md}` in `{colors.body}`. **`product-badge`** — Small uppercase badges in `{colors.accent-green}` for "New" or "Available", `{colors.accent-red}` for "Limited Edition", and `{colors.muted-soft}` for "Sold Out". Each uses `{typography.badge}` at 10px with 0.5px letter-spacing and 4px corner radius.

### Hero & Footer
**`hero-banner`** — A full-width 480px banner on `{colors.surface-soft}` with `{typography.display-lg}` text. An optional scrim overlay (`{colors.scrim}` at 30% opacity) ensures text readability over photography. Used for seasonal collections and new launches. **`footer`** — A deep charcoal (`{colors.primary}`) footer with white text at 80% opacity for links, increasing to full opacity on hover. Spacious padding (`{spacing.xxl}` vertical) with multiple columns for navigation, customer service, and newsletter signup.

### Interactive Elements
**`accordion-header`** — Used for product descriptions, ingredients, and shipping details. The header uses `{typography.title-md}` with a soft bottom border, expanding to reveal `{typography.body-sm}` content below. **`quantity-selector`** — A compact 44px control with a border and two side buttons for increment/decrement. The buttons have a subtle hover state (`{colors.surface-soft}`) for tactile feedback. **`icon-button`** — A 40px circular button (`{rounded.full}`) with no background by default, gaining a `{colors.surface-soft}` background on hover. Used for wishlist, share, and close actions.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero banner reduces to 320px height; footer stacks columns; search bar becomes full-width; accordions expand by default |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links with "More" dropdown; hero banner at 400px; footer uses 2-column grid; search bar remains pill-shaped but narrower |
| Desktop | 1128–1440px | Full nav-bar with all links; three-column product grid; hero banner at 480px; footer uses 4-column grid; side panels for cart and search overlay |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to 4 columns; hero banner content centered with generous margins; footer columns use max-width constraints |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons are 40px × 40px, exceeding the 44px recommendation for critical actions
- Product card tap targets (title, price, image) are at least 48px tall
- Accordion headers are 48px minimum touch height
- Quantity selector buttons are 44px × 44px

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-out drawer
- Product grid reduces from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer columns collapse from 4 to 2 to a single stacked layout
- Hero banner text overlay reduces font size and padding on mobile
- Search bar transitions from a compact pill to a full-width input on mobile
- Side panels (cart, search) become full-screen overlays on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow, scale, or border changes) could not be reliably extracted from the live site
- Error styling for form validation (text color, iconography, animation) beyond border color is undocumented
- Dark mode color tokens are absent; the brand may not support dark mode
- Sub-brand or seasonal color palettes (e.g., holiday collections, collaborations) are not captured
- Animation and transition timing values (duration, easing) are not available
- Focus ring styles (outline, offset, color) for keyboard navigation are not specified
- Dropdown and select component styling (arrow icon, menu panel) is missing
- Modal and dialog overlay styling (backdrop, close button, padding) is not defined
- Tooltip and popover component specifications are absent
- Loading state designs (skeleton screens, spinners) are not documented
- Multi-step checkout flow component states are not captured
- Typography scale for mobile (potential size reductions) is not confirmed
- Icon library and stroke weights are not specified
- Shadow/elevation tokens are not defined (the brand appears to avoid shadows)
