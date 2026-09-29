---
version: alpha
name: "Joybird"
source_url: "https://joybird.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A mid-century modern furniture brand that feels like a warm, curated living room brought to life through a teal-and-charcoal palette anchored on `#107c8c` — a deep, confident teal that appears on primary buttons, navigation accents, and product badges, carrying the brand's signature voltage without overwhelming the eye. The canvas is a soft `#f1f1f1` rather than pure white, giving the entire experience a lived-in, tactile warmth that distinguishes Joybird from stark, white-box furniture competitors. Secondary accents of `#b85455` (a dusty brick red) and `#fdde5c` (a warm mustard) appear on sale tags and promotional banners, while `#f56a62` and `#70db96` provide error and success signals respectively. Typography runs on Interstate, a geometric sans-serif with a friendly, slightly condensed character that echoes mid-century signage — display headings sit at modest weights (500-600) rather than heavy 700+, trusting the brand's generous product photography and `{spacing.section}` whitespace to carry visual hierarchy. Buttons use `{rounded.sm}` (8px) corners — soft but not pill-shaped — while product cards and modals use `{rounded.md}` (12px) for a gentle, approachable feel. The brand's voice is aspirational yet accessible: "Design your dream sofa" appears in `{colors.ink}` (`#262626`) on `{colors.canvas}` (`#ffffff`) cards, with `{colors.muted}` (`#717171`) supporting text that recedes respectfully. A consistent `{colors.hairline}` (`#cccccc`) defines card edges and dividers, while `{colors.hairline-soft}` (`#e5e5e5`) softens secondary borders. The overall mood is one of thoughtful retro-modernism — every corner is slightly softened, every color slightly desaturated from pure primaries, creating a system that feels both nostalgic and contemporary.

colors:
  primary: "#107c8c"
  primary-active: "#0d6370"
  primary-disabled: "#dbeded"
  ink: "#262626"
  body: "#424242"
  muted: "#717171"
  muted-soft: "#a5a7a9"
  hairline: "#cccccc"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  surface-strong: "#f6f6f6"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-red: "#b85455"
  accent-mustard: "#fdde5c"
  accent-orange: "#f8ab5e"
  accent-green: "#70db96"
  accent-error: "#f56a62"
  accent-purple: "#a176c8"
  accent-blue: "#759beb"
  accent-teal-light: "#65beb3"
  badge-sale: "#dd0000"
  badge-sale-bg: "#ffebe8"
  star-rating: "#fdde5c"
  scrim: "#000000"
  footer-bg: "#333333"
  footer-text: "#9ca3af"

typography:
  display-xl:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.3px
  link:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link-active:
    fontFamily: "'interstate', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px

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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 0
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  button-pill-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
    border: "1px solid {colors.hairline}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  icon-button-circle:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  top-nav-active-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link-active}"
    borderBottom: "2px solid {colors.primary}"
  top-nav-logo:
    height: 28px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  search-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-red}"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-badge-sale:
    backgroundColor: "{colors.badge-sale-bg}"
    textColor: "{colors.badge-sale}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-best-seller:
    backgroundColor: "{colors.accent-mustard}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    height: "480px"
  hero-banner-overlay:
    backgroundColor: "rgba(0,0,0,0.2)"
    textColor: "{colors.on-dark}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.on-dark}"
  category-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  category-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.footer-text}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  text-input-error:
    border: "2px solid {colors.accent-error}"
  text-input-label:
    typography: "{typography.caption}"
    textColor: "{colors.body}"
  text-input-helper:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    rounded: "{rounded.xs}"
    border: "2px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  radio-checked:
    border: "2px solid {colors.primary}"
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-active:
    backgroundColor: "{colors.primary}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "0 0 {spacing.base} 0"
  modal:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.16)"
    padding: "{spacing.lg}"
  modal-overlay:
    backgroundColor: "rgba(0,0,0,0.5)"
  modal-close:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  tab-active:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
  stepper:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 44px
  stepper-button:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 44px
    width: 44px
  stepper-input:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    textAlign: "center"
    width: 48px
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid transparent"
  color-swatch-selected:
    border: "2px solid {colors.ink}"
  color-swatch-teal:
    backgroundColor: "{colors.primary}"
  color-swatch-red:
    backgroundColor: "{colors.accent-red}"
  color-swatch-mustard:
    backgroundColor: "{colors.accent-mustard}"
  color-swatch-orange:
    backgroundColor: "{colors.accent-orange}"
  color-swatch-green:
    backgroundColor: "{colors.accent-green}"
  color-swatch-purple:
    backgroundColor: "{colors.accent-purple}"
  color-swatch-blue:
    backgroundColor: "{colors.accent-blue}"
  color-swatch-teal-light:
    backgroundColor: "{colors.accent-teal-light}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
    margin: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  pagination-inactive:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 16px
  rating-count:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  spinner:
    color: "{colors.primary}"
    height: 24px
    width: 24px
  spinner-large:
    color: "{colors.primary}"
    height: 48px
    width: 48px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  notification-success:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  notification-error:
    backgroundColor: "{colors.accent-error}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  notification-info:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the Joybird experience, rendered in the brand's signature teal (`{colors.primary}`) with white text. Used for "Add to Cart", "Design Your Sofa", and "Checkout" actions. On hover, it deepens to `{colors.primary-active}` (`#0d6370`), and in its disabled state it fades to `{colors.primary-disabled}` (`#dbeded`) with muted text. The 8px corner radius (`{rounded.sm}`) keeps the button friendly without being overly pill-shaped.

**`button-secondary`** — A white button with a charcoal border (`{colors.hairline}`) and dark text, used for "Learn More", "View Details", and secondary checkout actions. On active state, the border thickens and turns to `{colors.ink}` (`#262626`), and the background shifts to `{colors.surface-soft}` (`#f1f1f1`). Height matches the primary button at 48px for visual alignment.

**`button-tertiary-text`** — A text-only button in the brand teal, used for "See All", "Shop Now", and inline navigation links. No background or border — relies entirely on the teal color and button typography for affordance.

**`button-pill-primary`** and **`button-pill-secondary`** — Fully rounded pill buttons (40px height) used for filter tags, category chips, and promotional badges. The primary variant uses teal fill; the secondary uses a white fill with a subtle hairline border. Both use `{typography.button-sm}` for compact sizing.

### Cards
**`product-card`** — The core product display component, a white card with a soft shadow (`0 1px 3px rgba(0,0,0,0.08)`) and 12px rounded corners. The image area occupies the top with a 4:3 aspect ratio and rounded top corners only. On hover, the shadow deepens (`0 4px 16px rgba(0,0,0,0.12)`) to signal interactivity. The card contains a title (`{typography.title-sm}`), price (`{typography.body-md}`), optional sale price in `{colors.accent-red}`, and a rating row with stars and count.

**`category-card`** — Used for collection browsing (e.g., "Sofas", "Sectionals", "Chairs"). A white card with a soft shadow and 12px rounded corners, displaying a collection image and title. On hover, the background shifts to `{colors.surface-soft}` and the title turns teal, with an elevated shadow.

### Navigation
**`top-nav`** — A 72px white navigation bar with a subtle bottom border (`{colors.hairline-soft}`). Links use `{typography.nav-link}` (15px, weight 500), and the active link is indicated by a 2px teal underline and bold weight. The Joybird logo sits at 28px height. The nav includes a search icon, account icon, and cart icon — all using `{typography.nav-link}` sizing.

**`search-bar`** — A soft gray (`{colors.surface-soft}`) input field with a hairline border and 8px rounded corners. On focus, the border becomes a 2px teal stroke and the background turns white. The search dropdown that appears below uses `{rounded.md}`, a white background, and a 4px shadow.

### Forms
**`text-input`** — Standard 48px input field with white background, hairline border, and 8px rounded corners. On focus, the border becomes a 2px teal stroke. Error state uses a 2px `{colors.accent-error}` border. Labels use `{typography.caption}` and helper text uses `{typography.caption-sm}` in muted gray.

**`select-input`** — Matches the text-input dimensions and styling, with a custom dropdown arrow in `{colors.muted}`.

**`checkbox`** and **`radio`** — Small rounded controls with 2px hairline borders. Checked state fills with teal. Radio buttons use full rounding.

**`toggle`** — A 44x24 pill-shaped toggle with gray background. Active state fills with teal.

### Footer
**`footer`** — A dark footer (`{colors.footer-bg}` = `#333333`) with light gray text (`{colors.footer-text}` = `#9ca3af`). Section headings are white (`{colors.canvas}`) using `{typography.title-sm}`. Links are `{typography.link}` in footer-text, hovering to white. The footer contains columns for "Shop", "Support", "About", and "Connect", plus a newsletter signup form.

### Badges
**`product-badge-sale`** — A red-on-pink badge (`{colors.badge-sale}` on `{colors.badge-sale-bg}`) with uppercase 11px bold text and 4px rounded corners. Used to flag discounted items.

**`product-badge-new`** — A white-on-teal badge signaling new arrivals. Same typography and sizing as the sale badge.

**`product-badge-best-seller`** — A dark-text-on-mustard badge (`{colors.accent-mustard}`) for best-selling items.

### Modals
**`modal`** — A white overlay panel with 12px rounded corners, 8px shadow, and 24px padding. The backdrop uses 50% opacity black. The close button is a 32px circular icon button with no background.

### Tabs
**`tab-active`** and **`tab-inactive`** — Underline-style tabs where the active tab has a 2px teal bottom border and teal text, while inactive tabs use muted gray text. Both use `{typography.button-md}`.

### Stepper
**`stepper`** — A quantity selector with a soft gray background, 8px rounded corners, and 44px height. The minus and plus buttons are 44x44 transparent squares flanking a centered 48px-wide input.

### Color Swatches
**`color-swatch`** — 32px circular swatches used for fabric color selection. Selected state shows a 2px `{colors.ink}` border. Predefined swatch colors include teal, red, mustard, orange, green, purple, blue, and light teal — matching the brand's accent palette.

### Notifications
**`notification-success`** — Green background (`{colors.accent-green}`) with dark text, used for "Added to Cart" confirmations.
**`notification-error`** — Red background (`{colors.accent-error}`) with white text, used for error messages.
**`notification-info`** — Teal background (`{colors.primary}`) with white text, used for informational messages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger menu; hero banner height reduces to 320px; product cards stack vertically; footer columns stack to single column; search bar becomes full-width; filter sidebar becomes a bottom sheet; category cards display in 2-column grid |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links with "More" dropdown; hero banner at 400px; footer shows 2-column layout; filter sidebar is collapsible; category cards in 3-column grid |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links visible; hero banner at 480px; footer in 4-column layout; persistent filter sidebar; category cards in 4-column grid |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero banner at 520px; all layouts scale proportionally; additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target size on mobile
- Icon buttons are 40x40px with 36px visible icon area
- Color swatches are 32px with 44px tap area via padding
- Stepper buttons are 44x44px
- Product card CTAs are full-width on mobile (48px height)
- Bottom nav bar (mobile) uses 56px height for thumb reachability

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with a slide-out drawer
- Product filters collapse to a bottom sheet on mobile, with a "Filter" button triggering the overlay
- Footer columns collapse from 4-column to 2-column at tablet, to single column at mobile
- Product image galleries collapse from thumbnail strip to dot indicators on mobile
- Multi-column text sections (e.g., product descriptions) collapse to single column below 744px
- Sidebar content (e.g., cart summary) collapses to a slide-in drawer on mobile
- Hero banner text overlays shift from side-aligned (desktop) to center-aligned (mobile)
- Category navigation strips collapse to horizontal scroll on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus-visible states for all interactive elements (only primary button hover is confirmed)
- Error message styling for form validation (text color, iconography, timing)
- Disabled state styling for secondary buttons, text inputs, and select inputs
- Sub-brand or collection-specific color palettes (e.g., "Briar", "Hugo", "Sawyer" collections may have unique accents)
- Dark mode or high-contrast mode color overrides
- Loading skeleton or placeholder component specifications
- Empty state designs for search results, cart, and wishlist
- Animation timing curves and duration values for transitions and micro-interactions
- Dropdown menu styling for account and cart flyouts
- Accordion expand/collapse animation details
- Tooltip positioning and arrow direction specifications
- Star rating half-star and empty-star rendering details
- Print stylesheet specifications
- Focus ring color and offset values for keyboard navigation
- Mobile bottom navigation bar styling and behavior
- Pull-to-refresh and swipe gesture specifications for mobile
- Cookie consent banner styling
- Accessibility color contrast ratios for all text-on-background combinations
- Internationalization text length handling for buttons and labels
