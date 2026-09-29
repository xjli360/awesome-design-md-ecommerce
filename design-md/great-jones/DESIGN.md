---
version: alpha
name: "Great Jones"
source_url: "https://greatjonesgoods.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Great Jones is a direct-to-consumer cookware brand that brings a sense of warmth, wit, and color to the kitchen. The brand's palette is anchored by a deep, earthy green (`#0e5540`) that appears on primary buttons, key navigation elements, and product details, evoking a sense of groundedness and natural quality. This is paired with a rich navy (`#243d94`) used for secondary actions and accents, creating a confident, trustworthy foundation. The brand's voice is playful and modern, expressed through a signature golden yellow (`#f4a620`) that highlights sale badges, promotional banners, and interactive hover states, injecting energy and optimism. A soft, neutral canvas (`#ede1d4`) serves as the primary background for product pages and cards, offering a warm, tactile feel that contrasts with the stark white (`#ffffff`) often used in the rest of the e-commerce world. Typography relies on the serif warmth of CooperBT, used for display headlines and product titles to convey a sense of heritage and approachability, while body copy and UI elements are set in a clean, legible serif stack (`Times, Times New Roman, serif`). The design system employs generous spacing (`{spacing.lg}` and `{spacing.xl}`) around product imagery and generous padding (`{spacing.base}`) inside cards and buttons, creating a breathable, editorial layout. Signature moves include the use of `{rounded.full}` pill-shaped buttons for primary CTAs and `{rounded.sm}` for input fields and cards, balancing friendliness with structure. The overall mood is that of a trusted, stylish friend who knows their way around a kitchen—confident but not pretentious, colorful but not chaotic.

colors:
  primary: "#0e5540"
  primary-active: "#0a5640"
  primary-disabled: "#ad9f92"
  ink: "#121212"
  body: "#322659"
  muted: "#7d766f"
  muted-soft: "#ad9f92"
  hairline: "#dedede"
  hairline-soft: "#e2e8f0"
  canvas: "#ede1d4"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#f4a620"
  accent-yellow-active: "#f5a800"
  accent-blue: "#243d94"
  accent-blue-active: "#1990c6"
  accent-purple: "#805ad5"
  accent-pink: "#df95a1"
  accent-red: "#bc004b"
  badge-sale: "#b91d47"
  badge-new: "#5bbad5"
  star-rating: "#f4a620"
  scrim: "#171923"

typography:
  display-xl:
    fontFamily: "'CooperBT', 'Times', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'CooperBT', 'Times', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'CooperBT', 'Times', 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'CooperBT', 'Times', 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Times', 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Times', 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Times', 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Times', 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Times', 'Times New Roman', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'CooperBT', 'Times', 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'CooperBT', 'Times', 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  link:
    fontFamily: "'Times', 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'CooperBT', 'Times', 'Times New Roman', serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  badge:
    fontFamily: "'CooperBT', 'Times', 'Times New Roman', serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    padding: 14px 28px
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
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-accent-yellow-active:
    backgroundColor: "{colors.accent-yellow-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-accent-blue-active:
    backgroundColor: "{colors.accent-blue-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    padding: 0
    height: auto
  button-text-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    textDecoration: underline
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.xl}"
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px {spacing.base}"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px {spacing.base}"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl}"
  hero-headline:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    maxWidth: "600px"
  hero-subheadline:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginTop: "{spacing.lg}"
    maxWidth: "500px"
  hero-cta:
    marginTop: "{spacing.xl}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
  footer-link-hover:
    color: "{colors.accent-yellow}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-button:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
  accordion-header:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: "16px"
  divider:
    borderBottom: "1px solid {colors.hairline}"
    margin: "{spacing.lg} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop Now", and checkout flows. Rendered as a full pill shape (`{rounded.full}`) in the brand's deep green (`{colors.primary}`) with white text (`{colors.on-primary}`). On hover, it shifts to a slightly darker green (`{colors.primary-active}`). The disabled state uses a muted beige (`{colors.primary-disabled}`) to indicate inactivity.

**`button-secondary`** — An outlined variant used for secondary actions like "Learn More" or "View Details". It features a transparent background with a 2px solid border in the ink color (`{colors.ink}`). On hover, the background fills with the ink color and text inverts to white (`{colors.on-primary}`).

**`button-accent-yellow`** — A high-energy variant reserved for promotional CTAs, sale banners, and limited-time offers. Uses the signature golden yellow (`{colors.accent-yellow}`) with dark text (`{colors.ink}`) for maximum contrast and urgency. Active state deepens to `{colors.accent-yellow-active}`.

**`button-accent-blue`** — Used for secondary brand actions or informational CTAs, such as "Sign Up" for the newsletter or "Explore Guides". It uses the rich navy (`{colors.accent-blue}`) with white text, and its active state shifts to a brighter blue (`{colors.accent-blue-active}`).

**`button-text-link`** — A text-only button used for inline actions like "Read More" or "View Recipe". It inherits the primary green (`{colors.primary}`) and underlines on hover, matching the link typography.

### Cards
**`product-card`** — The core product display unit on collection pages and search results. It features a white background (`{colors.surface-card}`) with soft rounding (`{rounded.sm}`) and generous padding (`{spacing.base}`). The image container maintains a 1:1 aspect ratio. The title uses `{typography.title-sm}`, and the price is set in `{typography.body-md}`. Badges (sale, new) are positioned absolutely at the top-left corner.

### Navigation
**`top-nav`** — The primary site navigation bar, fixed at 72px height with a warm canvas background (`{colors.canvas}`). Navigation links use `{typography.nav-link}` in the brand's serif font, CooperBT. The active link is indicated by a 2px bottom border in the primary green (`{colors.primary}`). Inactive links are muted (`{colors.muted}`).

### Forms
**`text-input`** — Standard form input used for addresses, account details, and checkout fields. It has a white background, `{rounded.sm}`, and a 1px hairline border. On focus, the border thickens to 2px and turns primary green. Error state uses a 2px red border (`{colors.accent-red}`).

**`search-bar`** — The site search input, styled with a white background, `{rounded.sm}`, and a 1px hairline border. On focus, the border becomes 2px primary green. It is 44px tall with comfortable padding.

**`newsletter-input`** — A pill-shaped input (`{rounded.full}`) used in the footer for email sign-ups. It pairs with the `newsletter-button`, which uses the accent yellow for a clear, action-oriented call-to-action.

### Footer
**`footer-section`** — The site footer uses the primary green (`{colors.primary}`) as a bold, grounding element. All text and links are white (`{colors.on-primary}`). Links hover to the accent yellow (`{colors.accent-yellow}`), providing a warm, interactive highlight against the dark background.

### Badges
**`product-card-badge`** — A small, pill-shaped badge (`{rounded.full}`) used to highlight product attributes. The default badge uses the accent yellow (`{colors.accent-yellow}`) with dark text. Sale badges use a bold red (`{colors.badge-sale}`), and new badges use a bright blue (`{colors.badge-new}`), both with white text for clarity.

### Hero
**`hero-section`** — The top-level hero banner on the homepage and landing pages. It uses the warm canvas background (`{colors.canvas}`) with generous vertical padding (`{spacing.section}`). The headline uses `{typography.display-xl}` in CooperBT, and the subheadline is set in `{typography.body-md}` with a constrained max-width for readability.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger menu; hero headline reduces to `{typography.display-lg}`; buttons become full-width; footer stacks vertically. |
| Tablet | 744–1128px | Two-column product grid; top-nav remains visible with reduced link spacing; hero retains `{typography.display-xl}` but with smaller max-width; side-by-side footer layout. |
| Desktop | 1128–1440px | Three or four-column product grid; full top-nav with all links; hero is full-width with centered text; standard button sizes. |
| Wide | > 1440px | Max-width container (1440px) centered on screen; product grid can expand to four columns; hero content remains centered with larger max-width. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px.
- Icon buttons are 40x40px with `{rounded.full}` for easy tapping.
- Product card CTAs are at least 48px tall.

### Collapsing Strategy
- The top navigation collapses into a hamburger menu on mobile (< 744px).
- The product grid collapses from 4 columns on wide screens to 1 column on mobile.
- The footer's multi-column layout collapses to a single vertical stack on mobile.
- Hero sections reduce headline size and stack CTA buttons vertically on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: While active and disabled states are defined for primary buttons, hover states for secondary buttons, text inputs, and other components were inferred from common patterns and may not match the exact live implementation.
- **Error styling**: Error states for inputs (e.g., invalid email, missing required fields) are defined with a red border, but the exact error message typography, iconography, and animation were not extracted.
- **Sub-brand palettes**: Great Jones may have seasonal or collection-specific color palettes (e.g., for limited-edition cookware colors) that are not captured in this system.
- **Dark mode**: No dark mode tokens were found on the live site. All tokens assume a light theme.
- **Loading states**: Skeleton screens, spinner animations, and loading indicators were not extracted.
- **Focus styles**: Keyboard focus outlines (e.g., `:focus-visible`) were not reliably extracted and may need to be added for accessibility compliance.
- **Typography scale**: The exact font sizes for all typography tokens (e.g., `display-xl`, `body-sm`) were inferred from common brand usage and may not match the precise values in the design files.
- **Spacing scale**: The `section` token (64px) is an estimate for major section padding; actual values may vary by page.
- **Component variants**: Dropdown menus, tooltips, modals, and toast notifications were not observed on the live site and are not included.
