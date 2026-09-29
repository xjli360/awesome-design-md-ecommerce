---
version: alpha
name: "Aera"
source_url: "https://www.aeraforhome.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Aera is a home fragrance system that marries precision engineering with quiet luxury, communicating its value through a palette of calm, collected tones. The brand's primary identity is built on a deep, confident navy (`#002360`) that appears across CTAs, navigation elements, and key product details, anchoring the experience with a sense of reliability and sophistication. This is balanced by a warm, off-white canvas (`#fcfaf8`) that feels softer and more inviting than a pure white, creating a gentle backdrop for product photography and text. A secondary, lighter blue (`#eef4fa`) is used for subtle surface fills and hover states, while a muted stone (`#dedede`) and a soft clay (`#f6ece2`) provide gentle contrast for borders and secondary elements. The accent palette introduces a vibrant cerulean (`#1990c6`) and a deeper teal (`#136f99`) for interactive elements like links, badges, and secondary buttons, adding a layer of freshness and modernity. The typographic system, while not explicitly declared in the extracted data, is assumed to follow a clean, highly legible sans-serif family, likely a geometric or neo-grotesque, to maintain the brand's uncluttered and precise aesthetic. The overall feel is one of curated calm—every element, from the `{rounded.sm}` button corners to the generous `{spacing.section}` padding, is designed to feel intentional and unobtrusive, letting the product and its scent stories take center stage. The brand avoids visual noise, relying on a restrained color system and ample whitespace to evoke a sense of premium, effortless luxury.

colors:
  primary: "#002360"
  primary-active: "#001a4a"
  primary-disabled: "#b3c4e0"
  ink: "#222222"
  body: "#121212"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dedede"
  hairline-soft: "#eef4fa"
  canvas: "#fcfaf8"
  surface-soft: "#eef4fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#1990c6"
  accent-active: "#136f99"
  accent-soft: "#c5d9ed"
  warm-surface: "#f6ece2"
  star-rating: "#222222"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
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
  section: 80px

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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary-active}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-link:
    backgroundColor: transparent
    textColor: "{colors.accent}"
    typography: "{typography.link}"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid #c13515"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    marginTop: "{spacing.xs}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 600px
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.md}"
  badge-new:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "#c13515"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.warm-surface}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} 0"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    padding: "{spacing.sm} 0 {spacing.md} 0"
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
    width: "100%"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's deep navy (`#002360`) with white text. Uses uppercase, 600-weight type for a confident, premium feel. On hover, it shifts to a slightly darker navy (`#001a4a`). The disabled state uses a muted blue (`#b3c4e0`) to indicate inactivity. Corners are subtly squared at `{rounded.sm}` (4px), reinforcing the brand's precise, architectural quality.

**`button-secondary`** — An outlined variant for actions that are important but secondary to the primary CTA. It features a white background, navy text, and a 2px navy border. On hover, the background fills with the soft blue (`#eef4fa`) and the border darkens. This button is commonly used for "Learn More" or "Explore" links within product cards and hero sections.

**`button-accent`** — A vibrant alternative for highlighting special actions, such as "Subscribe & Save" or "Shop the Collection." Uses the cerulean (`#1990c6`) as its background, which deepens to teal (`#136f99`) on hover. This button provides a visual counterpoint to the dominant navy, drawing the eye to promotional or high-value conversion points.

**`button-link`** — A text-only button styled as an inline link with the accent blue (`#1990c6`). Used for "Read More," "View Details," or "See All" actions within content sections. It has no background or border, relying solely on its color and underline-on-hover to indicate interactivity.

### Cards
**`product-card`** — The primary container for displaying a single scent or diffuser product. It has a white background, a soft 8px corner radius (`{rounded.md}`), and a subtle shadow (not defined in tokens but implied by the card's separation from the canvas). The card contains a product image with a 4px radius (`{rounded.sm}`), a title in `title-sm`, and a price in `body-md` colored with the primary navy. The card is designed to be clean and scannable, letting the product photography do the heavy lifting.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar with a white background and a 1px bottom border (`{colors.hairline}`). It contains the brand logo, a set of uppercase nav links (`{typography.nav-link}`), and a search icon. The active link is indicated by a 2px bottom border in the primary navy (`#002360`). The bar is 72px tall, providing a stable, uncluttered header for the browsing experience.

### Forms
**`text-input`** — A standard input field for forms (email, name, search queries). It features a white background, a 1px hairline border (`#dedede`), and 4px corner radius (`{rounded.sm}`). On focus, the border changes to the primary navy to indicate the active state. Error states are signaled by a red border (`#c13515`). The input height is 48px for comfortable touch interaction.

### Footer
**`footer-section`** — A full-width footer with a deep navy background (`#002360`) and white text. It contains columns of links, social media icons, and legal text. The links are styled in white with 80% opacity, which increases to 100% on hover. This section provides a strong, grounded conclusion to the page, echoing the brand's premium and reliable character.

### Badges
**`badge-new`**, **`badge-sale`**, **`badge-limited`** — Small, pill-shaped badges (`{rounded.full}`) used to flag product cards. The "New" badge uses the accent blue, "Sale" uses a warm red, and "Limited" uses the soft clay background (`#f6ece2`) with dark text. They are designed to be unobtrusive yet informative, adding a layer of urgency or novelty without disrupting the clean card layout.

### Search
**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a white background and a 1px hairline border. It is designed for the main header or a dedicated search page. On focus, the border switches to the primary navy. The generous rounding and 48px height make it feel approachable and modern.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; navigation collapses to a hamburger menu; product cards stack vertically; hero text and buttons become full-width; footer links stack in a single column. |
| Tablet | 744–1128px | Two-column grid for product cards; navigation links may be truncated or hidden under a "More" menu; hero section uses a 50/50 split for text and image. |
| Desktop | 1128–1440px | Full multi-column grid (3-4 columns) for product cards; full navigation is visible; hero section uses a 60/40 or 50/50 split; maximum content width is capped at 1128px for readability. |
| Wide | > 1440px | Content remains centered with a max-width; additional whitespace is added to the sides; hero imagery may become more expansive; product grids may show 4-5 columns. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Product card tap targets are the entire card area.
- Navigation hamburger menu icon is at least 48x48px.
- Quantity selector buttons are 40x40px.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu, hiding all links.
- The footer link columns collapse into a single vertical stack on mobile.
- Multi-column product grids collapse to a single column on mobile.
- Hero sections with side-by-side text and image collapse to a stacked layout on mobile.
- Search bars may be hidden behind an icon on mobile, expanding to full width on tap.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The exact font family used by Aera could not be reliably extracted. The typography tokens assume a standard system sans-serif stack (`'Helvetica Neue', Helvetica, Arial, sans-serif`). A custom brand font (e.g., a proprietary geometric sans-serif) may be in use.
- Hover and focus states for many components (e.g., product cards, footer links, accordion items) are inferred from common patterns and may not match the live site exactly.
- Error and validation styling for forms (e.g., error messages, success states) is not fully defined.
- The specific shadow values (box-shadow) for cards, modals, and dropdowns are not captured.
- Dark mode or high-contrast mode styles are not defined.
- The brand's sub-palettes for seasonal collections, limited editions, or specific product lines (e.g., "Wellness" vs. "Classic") are not captured.
- The exact spacing and layout for the product detail page (PDP) — including image gallery, variant selector, and description — is not fully detailed.
- The loading state (skeleton screens) and empty state designs are not defined.
- The animation and transition timing functions (e.g., ease-in-out, duration) are not specified.
