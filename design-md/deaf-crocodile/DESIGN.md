---
version: alpha
name: "Deaf Crocodile"
source_url: "https://www.deafcrocodile.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A midnight-black canvas (#111111) that feels less like a background and more like a theater curtain before the film starts — the brand's signature move is to let near-black absorb the page while a single olive-green accent (#77804b) acts as the house light, appearing on primary buttons, category tags, and hover states. The palette is deliberately restrained: a warm off-white canvas (#f5f5f5) for product cards and content areas, a cooler white (#ebebeb) for secondary surfaces, and a muted gray (#888888) for secondary text and borders. Color is used sparingly but with intent — a deep maroon (#d0473e) for sale badges and limited-edition markers, a muted teal (#7396a2) for special collection headers, and a restrained navy (#5487a0) for informational links. The typography runs Archivo at modest weights — display headlines sit at 500 weight rather than the heavy 700+ that entertainment brands often use, trusting the stark contrast of black on white rather than typographic muscle. Buttons are softly rounded (`{rounded.sm}`) and pill-shaped search bars (`{rounded.full}`) read as approachable, while product cards use a gentle corner (`{rounded.md}`) that keeps the interface feeling curated without being precious. The overall effect is a digital storefront that respects the films it sells — the design gets out of the way, letting the movie posters and cover art provide the color and drama.

colors:
  primary: "#77804b"
  primary-active: "#5c6338"
  primary-disabled: "#b8be9a"
  ink: "#111111"
  body: "#444444"
  muted: "#888888"
  muted-soft: "#c8c8c8"
  hairline: "#dedede"
  hairline-soft: "#ececec"
  canvas: "#f5f5f5"
  surface-soft: "#ebebeb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-maroon: "#d0473e"
  accent-teal: "#7396a2"
  accent-navy: "#5487a0"
  accent-purple: "#7e31b5"
  accent-red: "#d91f35"
  accent-gold: "#907341"
  accent-blue: "#0095d5"
  sale-badge: "#d0473e"
  sold-out-badge: "#444444"
  star-rating: "#907341"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Archivo', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Archivo', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Archivo', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'Archivo', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Archivo', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Archivo', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Archivo', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Archivo', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Archivo', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Archivo', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Archivo', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Archivo', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Archivo', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Archivo', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Archivo', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
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
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.sold-out-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-collection:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.accent-maroon}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's olive green (#77804b) with white text. Used for "Add to Cart", "Checkout", and primary navigation actions. On hover, the background deepens to `{colors.primary-active}` (#5c6338). In disabled state, the button fades to `{colors.primary-disabled}` (#b8be9a) with no shadow or interaction.

**`button-secondary`** — A white button with a subtle border (`{colors.hairline}`) and dark text, used for "View Details", "Continue Shopping", and secondary actions. On hover, the background shifts to `{colors.surface-soft}` and the border strengthens to `{colors.muted}`. This button maintains the same 44px height and `{rounded.sm}` corners as the primary.

**`button-tertiary-text`** — A text-only button with no background or border, using the brand's olive green for the text color. Used for "Cancel", "Clear Filters", and other low-emphasis actions. The text color shifts to `{colors.primary-active}` on hover.

**`button-pill`** — A fully rounded (`{rounded.full}`) compact button used for promotional banners, newsletter signups, and quick-add actions. Uses the same olive green background as the primary button but with smaller padding and `{typography.button-sm}`.

### Navigation
**`top-nav`** — A dark bar (`{colors.ink}`) spanning the full width, 60px tall, containing the brand logo, navigation links, and cart icon. Navigation links use `{typography.nav-link}` with uppercase letter-spacing (0.5px) for a refined, editorial feel. Active links are highlighted in the brand's olive green (`{colors.primary}`), while inactive links appear in a muted gray (`{colors.muted-soft}`). The cart icon uses `{colors.canvas}` and sits at the far right.

**`nav-link-active`** — Active navigation item with olive green text on the dark nav background. The uppercase styling and letter-spacing give it a film-festival-program feel.

**`nav-link-inactive`** — Inactive navigation item in muted gray (`{colors.muted-soft}`), maintaining the same uppercase treatment. On hover, the text color shifts toward white.

### Search
**`search-bar-pill`** — A pill-shaped search input (`{rounded.full}`) with a white background, subtle border, and placeholder text in `{colors.body}`. The 48px height makes it prominent but not overwhelming. On focus, the border transitions to `{colors.primary}`, signaling active state without animation.

**`search-bar-focused`** — The focused state of the search bar, distinguished by the olive green border. The background remains white, and the text color deepens to `{colors.ink}` for readability.

### Product Cards
**`product-card`** — A white card (`{colors.surface-card}`) with `{rounded.md}` corners containing a product image, title, price, and optional badges. The card sits on the `{colors.canvas}` background with no shadow in its default state, creating a clean, flat layout. On hover, a subtle box shadow (`0 4px 12px rgba(0,0,0,0.08)`) lifts the card slightly, providing the only depth cue in the interface.

**`product-card-image`** — The top portion of the product card, with rounded top corners (`{rounded.md} {rounded.md} 0 0`) to match the card container. Images are typically film posters or cover art, and the card's white background ensures they pop.

**`product-card-title`** — The film title rendered in `{typography.title-sm}` (16px, weight 600) in `{colors.ink}`. Titles are kept to one or two lines with no truncation.

**`product-card-price`** — The price displayed in `{typography.body-sm}` (14px, weight 400) in `{colors.body}`. Sale prices appear in `{colors.accent-maroon}`.

### Badges
**`badge-sale`** — A small, uppercase badge in maroon (`{colors.sale-badge}`) with white text, used to mark discounted items. The `{rounded.xs}` corners and tight padding (2px 8px) keep it unobtrusive but visible.

**`badge-sold-out`** — A dark gray badge (`{colors.sold-out-badge}`) indicating items that are no longer available. Uses the same sizing and typography as the sale badge but with a neutral, muted tone.

**`badge-collection`** — A teal badge (`{colors.accent-teal}`) used to denote special collections or curated sets. The teal provides a distinct visual cue separate from the sale and sold-out badges.

### Hero Section
**`hero-section`** — A full-width hero area with a black background (`{colors.ink}`) and white text, used for featured collections, new releases, and promotional campaigns. The section uses `{spacing.section}` for vertical padding, creating a dramatic, immersive entry point. The headline uses `{typography.display-xl}` at 32px with a slight negative letter-spacing for a modern, cinematic feel.

**`hero-cta`** — The primary call-to-action within the hero, using the olive green button style with larger padding (14px 32px) for visual weight. The button sits on the black background, making the green pop as the single color accent in the hero.

### Footer
**`footer`** — A dark footer (`{colors.ink}`) with muted gray text (`{colors.muted-soft}`) for links and body copy. The footer contains navigation links, social media icons, copyright information, and newsletter signup. Links use `{typography.link}` and transition to white on hover.

**`footer-link`** — Footer navigation links in muted gray, maintaining the brand's restrained color approach even in interactive elements.

**`footer-link-hover`** — On hover, footer links shift to white (`{colors.canvas}`), providing the only color change in the footer's dark expanse.

### Forms
**`text-input`** — A standard text input with a white background, `{rounded.sm}` corners, and a subtle border. The 44px height matches the primary button for visual consistency in forms. On focus, the border transitions to `{colors.primary}`. Error states use `{colors.accent-maroon}` for the border.

**`text-input-focused`** — The focused state of text inputs, distinguished by the olive green border. The background remains white for readability.

**`text-input-error`** — Error state for text inputs, using a maroon border (`{colors.accent-maroon}`) to indicate validation issues. Error messages appear below the input in `{colors.accent-maroon}` using `{typography.caption-sm}`.

**`select-dropdown`** — A styled select element matching the text input's dimensions and styling. The dropdown arrow uses `{colors.muted}` and shifts to `{colors.primary}` on focus.

### Filters
**`filter-chip`** — A pill-shaped filter option (`{rounded.full}`) with a light gray background (`{colors.surface-soft}`) and body text. Used for filtering products by format, genre, or collection. The chip has 6px 16px padding for a compact but tappable target.

**`filter-chip-active`** — The active state of a filter chip, filled with the brand's olive green and white text. Active chips sit alongside inactive ones, providing clear visual distinction.

### Cart
**`quantity-selector`** — A compact input for adjusting item quantities in the cart, matching the text input styling but at 40px height. The input is centered and typically flanked by minus and plus buttons.

**`cart-item`** — A cart line item with a white background, separated from other items by a soft hairline border (`{colors.hairline-soft}`). Each item contains the product image, title, price, quantity selector, and a remove button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero text reduces to 24px; search bar moves below nav; filter chips wrap to multiple rows; cart items show compact layout |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains single column with 28px text; filter chips in horizontal scroll; cart shows full layout |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses 32px display text; search bar in nav; filters in sidebar; cart shows full layout with thumbnails |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero uses 36px display text; additional whitespace around cards; filters in persistent sidebar |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Filter chips are 32px tall with 16px horizontal padding, exceeding the 44px touch target recommendation
- Product card tap targets (title, image, price) are the full card width
- Cart quantity selector buttons are 40px × 40px minimum
- Search bar is 48px tall for easy thumb access
- Nav links in mobile menu are 48px tall with full-width tap targets

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with the cart icon remaining visible
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Filter sidebar collapses to a horizontal chip strip on mobile and tablet, with a "Filters" button that opens a modal overlay
- Hero section reduces vertical padding from 64px to 40px on mobile
- Footer navigation collapses from multi-column to single-column stacked layout on mobile
- Cart moves from a slide-out drawer on desktop to a full-page view on mobile
- Search bar moves from inline in the nav to a full-width bar below the nav on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components could not be fully extracted; only primary button and product card hover states were confirmed from the live site
- Error styling for forms (text-input-error) is inferred from the brand's accent colors rather than extracted from live error states
- Dark mode is not supported and no dark mode tokens were found in the extracted data
- Sub-brand or collection-specific color palettes (e.g., limited edition releases) could not be extracted
- Animation and transition timing values (durations, easing functions) were not extractable from static CSS
- Focus ring styles and accessibility-focused interaction states were not present in the extracted data
- The brand's logo and icon system (SVG colors, sizes) could not be reliably extracted
- Shopify checkout widget colors (Klarna, Afterpay, PayPal buttons) were filtered from the extracted palette but may appear in the live checkout flow
- The extracted color list includes several tones that appear to be stock image dominant colors or social media icon colors (e.g., #137f24, #b4deb0, #dcf0d8, #eabdbd, #fadfdf, #e9d7b8, #faf0df, #516cf4) — these were not included in the design system tokens as they are not brand colors
- Font weights beyond 400, 500, 600, and 700 were not confirmed; variable font axes (if any) could not be extracted
- The brand's secondary font (Roboto) was found in declarations but its usage context (body text vs. headings) could not be determined
- Spacing values for specific components (e.g., exact padding on product cards) are estimated based on common e-commerce patterns rather than extracted measurements
