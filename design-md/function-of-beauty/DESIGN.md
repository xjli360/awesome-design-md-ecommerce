---
version: alpha
name: "Function of Beauty"
source_url: "https://www.functionofbeauty.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A personalized haircare brand that speaks in the confident, clean language of science-meets-self-expression. The palette pivots on a clinical white canvas (`{colors.canvas}`) and a vivid cyan primary (`#1990c6`) that reads as both laboratory-clean and playful — it's the color of a clear blue sky after a storm, not a sterile hospital. A deeper teal (`#136f99`) provides active-state gravity, while the near-black ink (`#121212`) keeps body text sharp and legible against the predominantly light surfaces. The system leans heavily on a single, recurring neutral gray (`#dedede`) for hairlines, borders, and muted backgrounds — there is no warm gray or beige in sight, reinforcing the brand's precision-formulation ethos. Typography, though not explicitly declared in CSS, reads as a clean geometric sans-serif (likely Inter or a similar system font) at moderate weights — display headlines hover around 24–28px at weight 600, while body text stays at 14–16px with generous line-height for readability. The signature design move is the pill-shaped CTA button (`{rounded.full}`) in the primary cyan, often paired with a white secondary outline variant — a nod to the brand's "build your own formula" quiz flow. Product cards use soft, consistent rounding (`{rounded.md}`) and a clean card shadow, while the navigation bar is a thin, almost invisible strip of white with the logo centered and a sticky cart icon. The overall feel is optimistic, data-driven, and approachable — a brand that says "we've analyzed your hair" without feeling clinical or cold.

colors:
  primary: "#1990c6"
  primary-active: "#136f99"
  primary-disabled: "#a0d4eb"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-yellow: "#f5c518"
  accent-green: "#4caf50"
  error: "#d32f2f"
  star-rating: "#f5c518"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  link:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm}"
    height: 200px
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    marginTop: "{spacing.xs}"
  product-card-rating:
    typography: "{typography.caption}"
    color: "{colors.star-rating}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.base}"
    minHeight: 400px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    marginTop: "{spacing.lg}"
  badge-new:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-custom:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  quiz-progress-bar:
    backgroundColor: "{colors.hairline}"
    height: 4px
    rounded: "{rounded.full}"
  quiz-progress-fill:
    backgroundColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  ingredient-swatch:
    width: 32px
    height: 32px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  ingredient-swatch-selected:
    border: "2px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
  cart-icon:
    width: 24px
    height: 24px
    color: "{colors.ink}"
  cart-icon-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    width: 18px
    height: 18px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill-shaped button in the brand's signature cyan (`{colors.primary}`). Used for "Build My Formula", "Add to Cart", and "Start Quiz" flows. On hover, it deepens to `{colors.primary-active}`. The disabled state uses a pale cyan (`{colors.primary-disabled}`) to signal inactivity without visual noise. Text is always white (`{colors.on-primary}`) with 600-weight font and 0.3px letter spacing for a crisp, confident read.

**`button-secondary`** — An outlined variant of the primary button, using a white fill with a 2px solid cyan border. Used for "Learn More" and "View Details" actions, especially on hero sections and product cards where a full cyan button would compete with the primary CTA. Active state shifts the border to `{colors.primary-active}`. The outline treatment maintains the brand's clean, scientific aesthetic while providing clear visual hierarchy.

**`button-tertiary-text`** — A text-only button with no background or border, used for secondary actions like "Cancel", "Skip", or "See All". The text color is the primary cyan, and on hover it may underline or shift to `{colors.primary-active}`. This is the quietest button variant, reserved for low-importance interactions within forms and modals.

### Cards
**`product-card`** — The standard product display card, used across collection pages, search results, and the "Shop by Hair Type" sections. Features a white background with a soft shadow (`boxShadow: 0 2px 8px rgba(0,0,0,0.08)`) and 12px corner rounding (`{rounded.md}`). The card contains a product image with 8px rounding, a title in `{typography.title-sm}`, price in bold body-md, and a star rating in yellow (`{colors.star-rating}`). On hover, the shadow deepens to indicate interactivity. Cards are typically displayed in a 3-4 column grid on desktop, collapsing to 2 columns on tablet and a single column on mobile.

**`product-card-hover`** — The elevated state of the product card, triggered on mouse hover or focus. The shadow increases to `0 4px 16px rgba(0,0,0,0.12)`, creating a subtle lift effect. No border or color changes occur, keeping the interaction clean and minimal.

### Navigation
**`nav-bar`** — The primary site navigation, a thin white bar (`{colors.canvas}`) with a 1px soft hairline bottom border. The logo is centered, with nav links in uppercase 14px text at weight 500. The cart icon sits on the right with a small cyan badge showing item count. On mobile, the nav collapses into a hamburger menu with a slide-out drawer. The bar has a fixed height of 64px and a z-index that keeps it above all content.

**`nav-link-active`** — The active navigation link state, indicated by the primary cyan text color and a 2px cyan bottom border. This provides a clear, understated indicator of the current page or section. Inactive links use the muted gray (`{colors.muted}`) to recede visually.

### Forms
**`text-input`** — Standard text input fields used in the quiz flow, account creation, and checkout. Features a white background, 8px rounding (`{rounded.sm}`), and a 1px hairline border. On focus, the border thickens to 2px and turns cyan (`{colors.primary}`). Error states use a red border (`{colors.error}`). Disabled inputs fade to a soft gray background with muted text. Padding is generous (12px 16px) for comfortable typing.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) used in the site header and on search result pages. Shares the same styling as the text input but with full rounding for a friendlier appearance. Active state uses a 2px cyan border. The search bar often includes a magnifying glass icon on the left and a clear button on the right when text is entered.

### Footer
**`footer`** — The site footer uses a dark background (`{colors.ink}`) with white text for maximum contrast. Links are rendered in a muted gray (`{colors.muted-soft}`) and lighten on hover. The footer is divided into columns for "Shop", "Learn", "Support", and "Connect", with the brand's social media icons and newsletter signup form. Padding is generous at 48px top and bottom.

### Badges
**`badge-new`** — A small, pill-shaped badge with a yellow background (`{colors.accent-yellow}`) and dark text, used to flag new products or features. The typography is uppercase 11px at weight 600 with 0.5px letter spacing for a tight, readable label.

**`badge-sale`** — A red badge (`{colors.error}`) with white text, used to indicate discounted or sale items. Same shape and typography as the new badge, but the color signals urgency.

**`badge-custom`** — A cyan badge (`{colors.primary}`) with white text, used to denote customizable products — a core differentiator for the brand. This badge appears on product cards and in the quiz flow to highlight items that can be personalized.

### Quiz Components
**`quiz-progress-bar`** — A thin, 4px tall progress bar used in the "Build Your Formula" quiz. The background is the neutral gray (`{colors.hairline}`), and the fill is the primary cyan. The bar is fully rounded (`{rounded.full}`) and spans the full width of the quiz container. Progress is calculated as a percentage of completed steps.

**`quiz-progress-fill`** — The animated fill portion of the quiz progress bar. Transitions smoothly between steps using a CSS transition on width. The color is the primary cyan, reinforcing the brand's identity throughout the quiz experience.

**`ingredient-swatch`** — A 32px circular swatch used in the quiz to select hair goals, ingredients, or fragrance preferences. Each swatch has a 2px hairline border and a solid color fill. Selected swatches gain a 2px cyan border (`{colors.primary}`) to indicate choice. Swatches are typically arranged in a grid or horizontal scroll.

### Cart
**`cart-icon`** — A 24px icon representing the shopping cart, typically located in the top-right corner of the nav bar. The icon is a simple outline or filled cart shape in the ink color. It serves as the primary entry point to the cart drawer or page.

**`cart-icon-badge`** — A small, 18px circular badge overlaid on the cart icon, displaying the current item count. The badge uses the primary cyan background with white text in `{typography.caption-sm}`. The number is centered within the circle, and the badge is positioned at the top-right of the cart icon.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout for product grids; nav collapses to hamburger menu; hero section reduces to 300px min-height; product cards stack vertically; footer columns stack; quiz progress bar remains full-width; search bar moves to a collapsible overlay |
| Tablet | 744–1128px | Two-column product grids; nav links remain visible but condensed; hero section maintains 400px height; product cards display in 2-column grid; footer columns display in 2x2 grid; quiz interface uses side-by-side layout for options |
| Desktop | 1128–1440px | Three-column product grids; full nav bar with all links visible; hero section at full height; product cards in 3-column grid; footer in 4-column layout; quiz uses full-width layout with inline ingredient swatches |
| Wide | > 1440px | Max-width container at 1440px with centered content; product grids may expand to 4 columns; hero section may include full-bleed imagery; all layouts remain consistent with desktop but with increased whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px per WCAG guidelines
- Product card tap targets (title, image, CTA) are at least 48px tall
- Navigation links have a minimum 44px tap area, even when text is smaller
- Cart icon and badge are wrapped in a 44x44px touch target
- Quiz option swatches are 44x44px minimum (32px visual + 12px padding)
- Quantity selector buttons are 44x44px minimum
- Search bar has a 48px height for comfortable tapping

### Collapsing Strategy
- Top nav collapses from full link set to hamburger menu at < 744px
- Product grids collapse from 3 columns to 2 at 744px, then to 1 at < 744px
- Footer columns collapse from 4 to 2 at 744px, then to 1 at < 744px
- Hero section collapses from side-by-side text/image to stacked layout at < 744px
- Quiz step indicators collapse from horizontal bar to vertical list at < 744px
- Ingredient swatch grids collapse from 4 columns to 2 at < 744px
- Cart drawer (if used) becomes a full-screen overlay on mobile
- Search bar collapses from inline to a toggleable overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components beyond primary/secondary buttons and product cards (e.g., nav links, footer links, badges)
- Error styling for form validation beyond text input borders (e.g., error messages, icon states)
- Sub-brand or seasonal palette variations (e.g., limited edition colors, holiday themes)
- Dark mode or high-contrast mode specifications
- Animation and transition timing values (e.g., button hover transitions, card lift animations)
- Typography scale for mobile-specific sizes (assumed same as desktop but may vary)
- Icon library specifications (e.g., custom vs. system icons, stroke widths, sizes)
- Modal and dialog component styling (e.g., overlay, close button, content padding)
- Tooltip and popover component styling (e.g., background, arrow, positioning)
- Loading state specifications (e.g., skeleton screens, spinner colors and sizes)
- Accessibility specifications beyond touch targets (e.g., focus ring styles, ARIA labels)
- Print stylesheet specifications
- RTL (right-to-left) language support
- Specific font-family declarations from the live site (none found; assumed Inter or system font)
