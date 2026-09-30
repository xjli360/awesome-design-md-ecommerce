---
version: alpha
name: "Jono Pandolfi"
source_url: "https://www.jonopandolfi.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A tactile, handcrafted dinnerware brand rooted in the quiet warmth of artisan ceramics. The palette is anchored by a deep navy `#21385c` — the brand's signature color, drawn from the meta theme-color and used across headers, navigation, and primary accents — paired with a clean off-white canvas `#f6f6f6` that lets the clay's natural texture breathe. Body text runs in `#222222` on `#dedede`-toned surfaces, while `#141414` and `#333333` provide deep ink for headlines and strong typography. The brand's voice is restrained and material: a single accent red `#c72e2f` appears sparingly for cart badges and sale indicators, while `#439fdb` and `#1990c6` bring a cerulean note to secondary links and hover states. A soft blush `#fcd6d7` and pale green `#d3efcd` surface in product photography overlays and limited-edition badges. Every corner is softly rounded — `{rounded.sm}` for buttons, `{rounded.md}` for cards — echoing the wheel-thrown pottery process. The typography is set entirely in Inter, a clean sans-serif that balances the handmade feel with modern legibility. The design system feels like a well-lit studio: generous whitespace, muted surfaces, and deliberate color placement that never competes with the product.

colors:
  primary: "#21385c"
  primary-active: "#136f99"
  primary-disabled: "#cccccc"
  ink: "#141414"
  body: "#222222"
  muted: "#545454"
  muted-soft: "#939393"
  hairline: "#e2e2e2"
  hairline-soft: "#f6f6f6"
  canvas: "#f6f6f6"
  surface-soft: "#dedede"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#c72e2f"
  accent-blue: "#439fdb"
  accent-blue-hover: "#1990c6"
  accent-green: "#1b9500"
  blush: "#fcd6d7"
  pale-green: "#d3efcd"
  badge-red: "#c72e2f"
  badge-green: "#1b9500"
  link-blue: "#1990c6"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Inter', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 600
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
  button-primary-hover:
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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.muted}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 12px
  button-text-hover:
    textColor: "{colors.accent-blue-hover}"
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
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-limited:
    backgroundColor: "{colors.blush}"
    textColor: "{colors.accent-red}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  hero-cta-hover:
    backgroundColor: "{colors.primary-active}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  cart-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: "0 6px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Shop Now", and checkout flows. Rendered in the brand's deep navy `{colors.primary}` with white text and soft 8px rounding. On hover, shifts to `{colors.primary-active}` (#136f99) for a subtle cerulean lift. Disabled state uses `{colors.primary-disabled}` (#cccccc) with muted text, signaling inactivity without visual noise.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Learn More". Uses a white canvas background with a thin `{colors.hairline}` border that darkens to `{colors.muted}` on hover. The background shifts to `{colors.surface-soft}` (#dedede) on hover, maintaining the brand's tactile, material feel.

**`button-text`** — A minimal text-only button for inline actions like "Cancel" or "Clear filters". Uses `{colors.primary}` text that transitions to `{colors.accent-blue-hover}` (#1990c6) on hover. No background or border — pure typographic interaction.

### Cards
**`product-card`** — The core product display component, used across collection pages and search results. A white card with 12px rounding (`{rounded.md}`) and 16px padding. On hover, a subtle box-shadow lifts the card, creating depth without overwhelming the product photography. The product image sits within a 1:1 aspect ratio container with 8px rounding.

**`product-card-image`** — The image container within product cards. Uses `{rounded.sm}` to softly frame the ceramic pieces, echoing the wheel-thrown curves of the dinnerware. The square aspect ratio ensures consistent grid alignment across all product views.

### Navigation
**`nav-bar`** — The primary site navigation, fixed at 72px height with a white canvas background and a subtle `{colors.hairline-soft}` bottom border. Navigation links use uppercase Inter at 14px with 0.5px letter-spacing, giving the brand a refined, editorial feel. Active links are underlined with a 2px `{colors.primary}` border.

**`nav-link-active`** — The active state for navigation items. Uses `{colors.primary}` text color with a 2px bottom border in the same navy, creating a clean, anchored indicator that doesn't distract from the page content.

### Badges
**`badge-new`** — A pill-shaped badge for new arrivals, using `{colors.accent-green}` (#1b9500) for a fresh, organic feel. The uppercase 11px type with 0.5px letter-spacing fits neatly within 4px vertical padding.

**`badge-sale`** — A red badge (`{colors.accent-red}` #c72e2f) for sale items, using the brand's single high-contrast accent color. Same pill shape and typography as the new badge, ensuring visual consistency across badge types.

**`badge-limited`** — A softer, blush-toned badge (`{colors.blush}` #fcd6d7) for limited-edition pieces. Uses red text on the pink background, creating a warm, exclusive feel that matches the handcrafted brand voice.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, and contact forms. A white canvas background with 48px height and 16px horizontal padding. The default state has a `{colors.hairline}` border that thickens to 2px `{colors.primary}` on focus. Error state uses a 2px `{colors.accent-red}` border for clear validation feedback.

**`search-bar`** — A pill-shaped search input with full rounding (`{rounded.full}`), used in the header and mobile navigation. The 44px height and 20px horizontal padding create a compact but touch-friendly target. On focus, the border thickens to 2px `{colors.primary}`.

### Footer
**`footer`** — The site footer uses the brand's deep navy `{colors.primary}` as a full-width background, creating a strong visual anchor at the bottom of every page. White text at 80% opacity for links, increasing to full opacity on hover. The generous padding (`{spacing.xxl}` vertical) gives the footer breathing room.

**`footer-link`** — Footer navigation links in white with 80% opacity, using the standard link typography. The reduced opacity creates hierarchy against headings and brand copy, while full opacity on hover provides clear interactive feedback.

### Hero
**`hero-section`** — The primary hero banner on the homepage and collection pages. Uses the canvas background (`{colors.canvas}` #f6f6f6) with large display typography. The section padding (`{spacing.section}` = 64px) creates generous whitespace around the headline and CTA.

**`hero-cta`** — The hero's primary call-to-action button, larger than standard buttons at 14px vertical padding. Uses the same `{colors.primary}` background with `{colors.primary-active}` hover state, maintaining brand consistency while providing visual hierarchy.

### Interactive Elements
**`icon-button`** — A circular icon button (40x40px) for actions like search toggle, cart open, and mobile menu. Transparent background with `{colors.muted}` icon color, shifting to `{colors.surface-soft}` background and `{colors.ink}` icon on hover.

**`cart-badge`** — A small red pill badge that appears on the cart icon, showing item count. Uses `{colors.accent-red}` with white text, minimum 20px width to accommodate single and double digits. The badge is positioned at the top-right of the cart icon.

**`quantity-selector`** — A compact input for adjusting product quantities on the cart and product detail pages. Uses 40px height with a `{colors.hairline}` border and `{rounded.sm}` rounding. The typography matches body-md for consistency with surrounding product information.

**`accordion-header`** — Used for product details, shipping information, and FAQ sections. A clickable header with `{colors.ink}` text and a `{colors.hairline-soft}` bottom border. The padding provides comfortable touch targets on mobile.

**`accordion-content`** — The expandable content area beneath accordion headers. Uses `{colors.body}` text with `{colors.canvas}` background. Content padding matches the header for visual alignment.

**`divider`** — A 1px horizontal rule using `{colors.hairline}` (#e2e2e2), used to separate sections within product cards, cart items, and content blocks.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger navigation, stacked footer, full-width hero, reduced typography sizes (display-xl drops to 24px), search bar collapses to icon button |
| Tablet | 744–1128px | Two-column product grid, expanded navigation with dropdowns, two-column footer, hero retains display-xl at 28px |
| Desktop | 1128–1440px | Three-column product grid, full navigation visible, three-column footer, hero at full display-xl (32px), search bar visible in header |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, extended footer with brand story section, hero with background imagery |

### Touch Targets
- All interactive elements maintain minimum 44x44px touch targets on mobile
- Navigation links have 48px minimum height on mobile for easy tapping
- Product card CTAs are 48px tall on touch devices
- Accordion headers are 48px minimum height
- Icon buttons remain 40x40px but with 12px additional padding on mobile

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Footer sections stack vertically on mobile, with accordion-style expandable columns
- Hero section reduces padding from 64px to 32px on mobile
- Search bar collapses to icon button on mobile, expanding to full-width overlay on tap
- Badges remain visible but reduce font size to 10px on mobile
- Product card padding reduces from 16px to 12px on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons and text inputs could not be fully verified from static analysis — the extracted values represent best-guess transitions
- Error styling for forms (validation messages, error icons) was not reliably extracted — placeholder values use the brand's accent red
- Dark mode preferences were not detected — the system currently assumes light mode only
- Sub-brand or collection-specific palettes (e.g., limited-edition colorways) were not captured
- Animation durations and easing curves (transitions, hover effects) were not extractable from the static site
- Focus ring styles for keyboard navigation were not observed — accessibility team should define these
- Loading states (skeleton screens, spinner colors) were not present in the extracted data
- Dropdown menu styles (mega-menu, nested navigation) were not fully captured
- Mobile-specific typography scales (reduced sizes) are estimated based on common responsive patterns
- Print stylesheet specifications were not available
