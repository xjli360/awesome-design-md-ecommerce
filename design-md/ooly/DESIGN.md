---
version: alpha
name: "Ooly"
source_url: "https://www.ooly.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A cheerful, low-friction arts-and-crafts marketplace that runs on a near-monochrome base of #dedede, #222222, and #121212—a palette that reads as a clean, uncluttered sketchbook page rather than a colorful toy store. The brand’s primary voltage is not a single saturated hue but the contrast between a warm off-white canvas and a near-black ink, letting the actual product photography (markers, paints, clay, stickers) supply all the chroma. Poppins, a geometric sans-serif with a friendly circular “O” and open apertures, runs at modest weights (400–600) across the site; display sizes hover around 24px rather than shouting, and body copy at 14px keeps the reading rhythm quick. Buttons are pill-shaped (`{rounded.full}`) with 48px height and generous 16px horizontal padding, giving them a squishy, approachable feel that matches the “Create your happy!” tagline. The top navigation is a simple, centered logo flanked by icon-only links (search, account, cart) with no dropdowns—everything feels like a single-page app for browsing. Product cards use a soft `{rounded.md}` (12px) corner, a white `{surface-card}` background, and a thin `{hairline}` border (#dedede) that keeps the grid airy. The search bar is a full-width pill with a `{rounded.full}` radius and a subtle `{hairline-soft}` border, placed prominently below the hero. The overall impression is of a brand that trusts its product to be the color, and uses typography and whitespace as the quiet, reliable frame.

colors:
  primary: "#dedede"
  primary-active: "#c4c4c4"
  primary-disabled: "#f0f0f0"
  ink: "#121212"
  body: "#222222"
  muted: "#555555"
  muted-soft: "#888888"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#121212"
  on-dark: "#ffffff"
  accent-yellow: "#f5c518"
  accent-green: "#4caf50"
  accent-pink: "#e91e63"
  badge-new: "#e91e63"
  badge-sale: "#f5c518"
  star-rating: "#121212"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Poppins', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
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
    rounded: "{rounded.full}"
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-accent:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
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
    height: 64px
    padding: "0 {spacing.lg}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline-soft}"
  search-bar-pill-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.ink}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    marginTop: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
    textAlign: center
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    marginBottom: "{spacing.md}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.on-dark}"
    typography: "{typography.link}"
    textDecoration: none
  footer-link-hover:
    color: "{colors.primary}"
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    textAlign: center
  category-card-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  add-to-cart-button:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 48px
  add-to-cart-button-hover:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"

## Components

### Buttons
**`button-primary`** — The default call-to-action, a pill-shaped button with a light gray `{colors.primary}` background and near-black `{colors.on-primary}` text. On hover, it shifts to `{colors.primary-active}` (#c4c4c4) for a subtle darkening effect. The disabled state uses `{colors.primary-disabled}` (#f0f0f0) with muted text, signaling non-interactivity without harsh contrast. Used for “Shop Now”, “View All”, and secondary CTAs throughout the site.

**`button-secondary`** — An outlined variant with a white background, black text, and a 1px `{colors.hairline}` border. Hover state darkens the border to `{colors.ink}`. Used for “Learn More” or “Add to Wishlist” actions where the primary button would be too dominant.

**`button-tertiary-text`** — A text-only button with transparent background and `{colors.ink}` text. No border, no padding beyond the text itself. Used for “Cancel”, “Skip”, or inline navigation links within forms and modals.

**`button-pill-accent`** — A bright yellow pill (`{colors.accent-yellow}`) used sparingly for high-energy calls like “Get Started” or promotional banners. The yellow against the near-black text creates a cheerful, urgent contrast that breaks the monochrome base.

### Navigation
**`top-nav`** — A fixed-height (64px) white bar with centered logo and icon-only links for search, account, and cart. The logo is the primary brand identifier; no text links appear in the top nav. The background is `{colors.canvas}` with a 1px `{colors.hairline}` bottom border on scroll. On mobile, the cart and account icons remain visible, while search expands to a full-width input.

### Search
**`search-bar-pill`** — A full-width pill input with a soft gray background (`{colors.surface-soft}`) and a thin `{colors.hairline-soft}` border. On focus, the background turns white and the border thickens to 2px `{colors.ink}`, providing a clear active state. The placeholder text uses `{colors.muted-soft}`. A magnifying glass icon sits at the left edge.

### Product Cards
**`product-card`** — A white card with `{rounded.md}` corners, a 1px `{colors.hairline}` border, and 8px padding. On hover, the border switches to `{colors.ink}` and a subtle box shadow lifts the card. The title uses `{typography.title-sm}` and the price uses `{typography.body-md}` with a 600 weight. Badges (New, Sale) appear as small uppercase pills in the top-left corner.

**`badge-new`** and **`badge-sale`** — Small, uppercase pill badges. “New” uses a pink background (`{colors.badge-new}`) with white text; “Sale” uses a yellow background (`{colors.badge-sale}`) with near-black text. Both have `{rounded.sm}` corners and tight padding.

### Hero Section
**`hero-section`** — A centered, full-width section with generous vertical padding (`{spacing.section}`). The heading uses `{typography.display-xl}` in `{colors.ink}`, followed by a subheading in `{colors.muted}` body copy. A single `button-primary` or `button-pill-accent` sits below. No background image or color block — the hero relies on typography and whitespace.

### Footer
**`footer`** — A dark section with `{colors.ink}` background and white text. Links use `{typography.link}` and turn to `{colors.primary}` on hover. Organized in a multi-column grid with headings in `{typography.title-sm}`. Social media icons appear as white glyphs that shift to `{colors.primary}` on hover.

### Category Cards
**`category-card`** — A soft gray (`{colors.surface-soft}`) card with `{rounded.md}` corners, centered text, and `{spacing.lg}` padding. On hover, the background shifts to `{colors.primary}` (#dedede) and the text to `{colors.on-primary}` (#121212). Used for browsing product categories like “Markers”, “Paint”, “Clay”.

### Quantity Selector
**`quantity-selector`** — A compact, bordered input with minus/plus buttons flanking a numeric display. The container has `{rounded.sm}` corners and a 1px `{colors.hairline}` border. The buttons are icon-only with `{colors.ink}` text, and the numeric value is centered in `{typography.body-md}`.

### Add to Cart Button
**`add-to-cart-button`** — A solid black (`{colors.ink}`) pill with white text, used exclusively on product detail pages. On hover, it shifts to `{colors.body}` (#222222). The button is wider than standard CTAs (32px horizontal padding) to accommodate the “Add to Cart” text comfortably.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; search bar becomes a full-width input below the logo; product cards stack in a single column; hero padding reduces to 32px top/bottom; footer links stack vertically. |
| Tablet | 744–1128px | Top nav remains full; product cards display in a 2-column grid; search bar remains pill-shaped but shrinks to 60% width; hero padding at 48px. |
| Desktop | 1128–1440px | Product cards in a 3- or 4-column grid; search bar at 50% width; hero padding at 64px; category cards in a 4-column row. |
| Wide | > 1440px | Max-width container (1440px) centered; product cards in a 4-column grid; search bar at 40% width; all spacing scales proportionally. |

### Touch Targets
- All interactive elements (buttons, links, icons) have a minimum height of 44px and minimum width of 44px on mobile.
- Icon buttons in the top nav are 40x40px with `{rounded.full}` corners.
- Quantity selector buttons are 40x40px with `{rounded.sm}` corners.
- Search bar has a 48px height for easy tapping.

### Collapsing Strategy
- The top nav collapses to a hamburger menu on mobile (< 744px), hiding all icon links except the cart.
- The footer multi-column grid collapses to a single column on mobile, with accordion-style expandable sections for link groups.
- Category cards collapse from a 4-column row to a 2-column grid on tablet and a single column on mobile.
- The hero section reduces vertical padding by half on mobile to conserve screen space.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list (#dedede, #222222, #121212) is sparse and generic (grays and near-blacks). The brand’s true primary color may be a more distinctive hue (e.g., a bright pink, yellow, or teal) that appears in product photography or marketing materials but was not captured in the HTML/CSS extraction. The `accent-yellow`, `accent-green`, and `accent-pink` tokens are educated guesses based on common arts-and-crafts brand palettes and should be verified against the live site’s design assets.
- Hover and focus states for most components are inferred from common patterns; the exact transitions, durations, and easing curves are unknown.
- Error styling for form inputs (e.g., invalid email, missing required field) is not captured. A red border (`#d32f2f`) and error text in `{typography.caption}` with `{colors.muted}` are assumed but not confirmed.
- Dark mode is not present on the live site; no dark-mode tokens are defined.
- The font-family declaration found only “Poppins, sans-serif”. The exact fallback stack (e.g., system fonts) is assumed. Variable font weights and optical sizing are not confirmed.
- Sub-brand or seasonal color palettes (e.g., holiday collections, limited-edition packaging) are not represented.
- The `rounded` scale values (xs through full) are estimated from visual inspection of the live site’s button and card radii; exact pixel values may vary.
- Spacing scale values (xxs through section) are based on common 4px/8px grid systems and may not match the site’s actual spacing tokens exactly.
