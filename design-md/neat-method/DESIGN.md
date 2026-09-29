---
version: alpha
name: "Neat Method"
source_url: "https://neatmethod.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Neat Method is a professional home organization brand that speaks in quiet, confident tones — a palette of deep charcoals ({colors.ink}: #363535), soft grays ({colors.muted}: #5f6166, {colors.muted-soft}: #8a8c91), and warm off-whites ({colors.canvas}: #fafafa) that feels like a freshly edited closet. The brand's signature voltage is a restrained royal purple ({colors.primary}: #3e34d3) that appears sparingly — on primary CTAs, accent lines, and the occasional badge — lending a sense of curated luxury without shouting. A secondary gold accent ({colors.gold}: #a98f36) and a muted sage ({colors.sage}: #515a4e) hint at the natural, textile-rich world of custom drawer liners and velvet hangers. The typography relies on a clean, inherited sans-serif system ({typography.body-md}) that prioritizes readability over personality, letting the before-and-after photography and generous whitespace carry the emotional weight. Rounded corners are soft but not pill-like — {rounded.sm} (8px) on cards and {rounded.md} (12px) on buttons — creating a tactile, approachable feel that mirrors the brand's promise of calm, orderly spaces. The overall mood is professional yet warm, like a trusted consultant who arrives with labeled bins and a quiet smile.

colors:
  primary: "#3e34d3"
  primary-active: "#2c2e40"
  primary-disabled: "#7777a3"
  ink: "#363535"
  body: "#5f6166"
  muted: "#8a8c91"
  muted-soft: "#8a8c93"
  hairline: "#dddddd"
  hairline-soft: "#eaeaea"
  canvas: "#fafafa"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  gold: "#a98f36"
  sage: "#515a4e"
  error: "#dc1512"
  scrim: "#0d0d0d"
  dark-ink: "#2f2f2f"
  deep-charcoal: "#262627"
  near-black: "#000309"

typography:
  display-xl:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0px
  display-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0px
  title-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0px
  title-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0px
  body-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0px
  body-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  caption:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px
  button-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  nav-link:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0px
  badge:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.ink}"
  button-gold:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 48px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    padding: "0 {spacing.base} {spacing.base} {spacing.base}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 32px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-gold:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.lg} 0 {spacing.base} 0"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's signature purple ({colors.primary}: #3e34d3) and white text. On hover or active state, the background shifts to a deep navy ({colors.primary-active}: #2c2e40). When disabled, it fades to a muted lavender ({colors.primary-disabled}: #7777a3). The button uses {typography.button-md} at 15px with 0.5px letter spacing for a slightly elevated, intentional feel. Corners are softly rounded at {rounded.md} (12px), and the height is a comfortable 48px.

**`button-secondary`** — An outlined variant on a white canvas ({colors.canvas}) with {colors.ink} text and a 1px {colors.hairline} border. Active state swaps the border to {colors.ink} and adds a light gray background ({colors.surface-soft}). Used for "Learn More" or "View All" actions where the primary purple would be too dominant.

**`button-gold`** — A special accent button using the brand's gold ({colors.gold}: #a98f36) for premium or limited-edition calls-to-action. Shares the same dimensions and typography as `button-primary` but carries a more luxurious, celebratory tone.

**`button-text`** — A text-only button with no background or border, using {colors.primary} for the text. Used for inline actions like "Read More" or "Add Note" where a full button would feel heavy.

### Cards
**`product-card`** — A clean, white card ({colors.surface-card}) with {rounded.sm} (8px) corners. The image sits flush to the top corners, while the title and price are padded with {spacing.base} (16px) on the sides. The title uses {typography.title-sm} (16px, weight 600) and the price is set in {typography.body-md} with the brand purple ({colors.primary}) to draw the eye. Cards are designed to sit in a 3- or 4-column grid on desktop, collapsing to 2 columns on tablet and a single column on mobile.

### Navigation
**`nav-bar`** — A fixed or sticky top bar at 72px height, white background ({colors.canvas}) with {colors.ink} text. Navigation links use {typography.nav-link} (15px, weight 500). The active link is underlined with a 2px {colors.primary} border. The bar may include a centered logo and a right-aligned cart icon with a badge count.

### Forms
**`text-input`** — A standard input field with a white background, 1px {colors.hairline} border, and {rounded.sm} (8px) corners. On focus, the border thickens to 2px and turns {colors.primary}. Error state uses a 2px {colors.error} (#dc1512) border. Padding is 12px vertical and 16px horizontal, with a height of 48px for comfortable touch targeting.

### Footer
**`footer-section`** — A dark footer with a {colors.ink} (#363535) background and white text ({colors.canvas}). Links are set in {colors.muted-soft} (#8a8c93) using {typography.link}. The footer typically contains three columns: brand info, quick links, and a newsletter signup. Padding is {spacing.xxl} (48px) vertical and {spacing.lg} (24px) horizontal.

### Badges
**`badge-new`** — A small uppercase badge with {colors.primary} background and white text, using {typography.badge} (11px, weight 700, uppercase). Corners are {rounded.xs} (4px) with 2px vertical and 8px horizontal padding. Used to flag new products or services.

**`badge-sale`** — Same dimensions as `badge-new` but with {colors.error} (#dc1512) background for sale or clearance items.

**`badge-gold`** — Same dimensions as `badge-new` but with {colors.gold} (#a98f36) background for premium or exclusive items.

### Hero
**`hero-section`** — A full-width hero area with a light gray background ({colors.surface-soft}: #f7f7f7) and {colors.ink} text. The heading uses {typography.display-xl} (28px, weight 400) with generous padding of {spacing.section} (64px) vertical and {spacing.lg} (24px) horizontal. A single `hero-cta` button sits below the heading, using the primary purple with larger padding (14px 32px) for emphasis.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero padding reduced to 32px; buttons go full-width; search bar hidden behind icon |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero uses 2-column text/image layout; footer stacks to 2 columns |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with all links; hero uses full-width image with overlaid text; footer in 3 columns |
| Wide | > 1440px | Max-width container at 1440px with centered content; product grid can expand to 4 columns; hero uses wider typography scale |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px for touch accessibility.
- Icon buttons in the nav bar are at least 44x44px with 8px padding.
- Product card tap targets (title, price, image) are at least 48px tall.
- Badges are kept small (20px height) but are always paired with a larger touchable parent.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer.
- The search bar collapses into a magnifying glass icon that opens a full-screen overlay.
- The product grid collapses from 4 columns to 2 (tablet) to 1 (mobile).
- The hero section collapses from a side-by-side layout to stacked on mobile.
- The footer collapses from 3 columns to 2 (tablet) to a single column (mobile).

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links could not be reliably extracted from the live site; the active states defined above are best guesses based on color relationships.
- Error styling for forms (beyond the border color) is inferred; actual error message typography and iconography are unknown.
- The brand's sub-palette for seasonal or promotional campaigns (e.g., holiday gold, summer sage) is not captured.
- Dark mode tokens are not defined, as the site appears to use a light-only theme.
- The exact font family is declared as "inherit" in the extracted CSS; the system font stack used above is a reasonable fallback but may not match the actual font loaded by Shopify.
- Animation durations, easing curves, and transition properties are not extracted.
- Focus ring styles (outline, offset, color) for keyboard navigation are not present in the extracted data.
- The spacing scale is inferred from common patterns; exact values for padding/margin on specific components may vary.
- The gold and sage accent colors are present in the extracted hex list but their exact usage context (badges, borders, backgrounds) is assumed based on brand positioning.
