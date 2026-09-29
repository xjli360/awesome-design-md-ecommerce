---
version: alpha
name: "GoldieBlox"
source_url: "https://goldieblox.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A purple that reads as electric optimism — #d18cff — is the first color your eye catches on GoldieBlox, and it never lets go. That violet appears on the primary CTA, the header stripe, the "Shop" button, and the "Add to Cart" pill, making every purchase action feel like a reward rather than a transaction. The brand pairs this with a warm coral accent (#f3584c) for sale badges and secondary highlights, and a marigold yellow (#ffb71b) that pops against the white canvas (#ffffff) of product cards and the soft lavender surface (#f6e6df) of category blocks. Typography runs SofiaPro at clean, readable sizes — body copy at 16px with generous line-height (1.6) and display headlines at 28–32px in weight 600, never shouting. The overall mood is a workshop that happens to be a store: rounded corners everywhere ({rounded.lg} on cards, {rounded.full} on buttons), a mint accent (#19d3c5) for "New" badges and progress indicators, and a pink (#fb96d8) that shows up in the footer and on the "Girls" navigation tab, reinforcing the brand's core audience without being saccharine. The checkout flow uses Shopify's default gray (#dedede) for dividers and muted text (#726d75) for secondary copy, keeping the focus on the product photography and the bright, confident palette that says "engineering is for everyone."

colors:
  primary: "#d18cff"
  primary-active: "#b86aff"
  primary-disabled: "#e8d4ff"
  ink: "#121212"
  body: "#444444"
  muted: "#726d75"
  muted-soft: "#a0a0a0"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f6e6df"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-coral: "#f3584c"
  accent-yellow: "#ffb71b"
  accent-mint: "#19d3c5"
  accent-pink: "#fb96d8"
  accent-blue: "#74bedd"
  badge-sale: "#f3584c"
  badge-new: "#19d3c5"
  star-rating: "#ffb71b"
  footer-bg: "#121212"
  footer-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'SofiaPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'SofiaPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'SofiaPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'SofiaPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'SofiaPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'SofiaPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'SofiaPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'SofiaPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'SofiaPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'SofiaPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'SofiaPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'SofiaPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'SofiaPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'SofiaPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'SofiaPro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary-active}"
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.md}"
  text-input-error:
    border: "2px solid {colors.accent-coral}"
    rounded: "{rounded.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-default:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
    rounded: "{rounded.lg}"
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.footer-text}"
    hoverTextColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.footer-text}"
    marginBottom: "{spacing.base}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: "600px"
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: "500px"
  category-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  category-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
    backgroundColor: "{colors.surface-soft}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: "16px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: "0 {spacing.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a pill-shaped button in the brand's signature purple (#d18cff) with white text. Used for "Add to Cart," "Shop Now," and primary form submissions. On hover, shifts to a deeper violet (#b86aff); disabled state uses a pale lavender (#e8d4ff) with white text.

**`button-secondary`** — An outlined variant with a white background, purple text, and a 2px purple border. Used for "Learn More," "View Details," and secondary actions that need visual presence without competing with the primary CTA. Active state fills with the soft surface color (#f6e6df) and deepens the border to the active purple.

**`button-accent-coral`** — A coral (#f3584c) pill button used for sale-related actions, clearance sections, and urgency-driven CTAs. Smaller padding than primary, intended for badge-adjacent placement or compact layouts.

**`button-accent-yellow`** — A marigold (#ffb71b) pill button with dark text (#121212), used for "Subscribe," "Get Started," and promotional CTAs where the brand wants high contrast without purple.

### Cards
**`product-card`** — A white card with a 1:1 product image at the top (rounded top corners only), followed by the product title and price. The card sits on a subtle shadow (0 2px 8px rgba(0,0,0,0.06)) and lifts on hover (0 4px 16px rgba(0,0,0,0.12)). Badges for "Sale," "New," or "Sold Out" overlay the top-left of the image.

**`category-card`** — A white card with a larger padding area, used to represent product categories or collections. On hover, the background shifts to the soft surface color (#f6e6df) and the shadow deepens, creating a tactile "selected" feel.

### Navigation
**`nav-bar`** — A 72px white header with a thin bottom border (#e8e8e8). Contains the brand logo on the left, navigation links in the center, and utility icons (search, cart, account) on the right. On scroll, becomes sticky with a subtle box-shadow. Active nav links are underlined with a 2px purple border.

**`nav-link-active`** — The currently selected navigation item, rendered with purple text and a 2px bottom border in the same purple. All other nav links use the ink color (#121212) with no underline.

### Forms
**`text-input`** — A standard text input with a 1px hairline border (#dedede), 12px corner radius, and 48px height. On focus, the border thickens to 2px and turns purple. Error state swaps the border to coral (#f3584c). Used for email signups, search queries, and checkout fields.

**`search-bar`** — A pill-shaped search field with a soft surface background (#f6e6df) and 1px hairline border. On focus, the background turns white and the border becomes 2px purple. The rounded-full shape matches the button style, creating a consistent "pill" language across interactive elements.

### Footer
**`footer`** — A dark footer (#121212) with white text, spanning the full width of the viewport. Contains columns for "Shop," "About," "Support," and "Connect," each with a heading in the title-sm typography and links in body-sm. Link hover color shifts to purple (#d18cff). Social media icons appear in the bottom row, using their brand colors (not recolored).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product cards go single-column; hero section reduces padding to 32px; buttons go full-width; footer stacks vertically |
| Tablet | 744–1128px | Nav links visible but condensed; product cards in 2-column grid; hero padding at 48px; search bar moves to nav overlay |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero at full padding; search bar in nav bar |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero content centered with max-width constraints |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px
- Product card tap area includes the entire card surface
- Nav hamburger icon has 48x48px tap area
- Quantity selector +/- buttons are 44x44px each
- Badge tap targets are the parent card, not the badge itself

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px; the hamburger icon is purple (#d18cff) on white
- Product grid collapses from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- Footer columns collapse from 4 columns (desktop) to 2 columns (tablet) to stacked (mobile)
- Hero section collapses from side-by-side text + image to stacked (text on top, image below) below 744px
- Search bar collapses from inline in nav (desktop) to overlay modal (tablet/mobile)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card badges (sale, new, sold-out) could not be extracted — assumed no change or subtle opacity shift
- Error styling for form validation (inline messages, border colors for success/warning) not observed on live site
- Sub-brand or collection-specific color palettes (e.g., "GoldieBlox + Friends" or seasonal themes) not captured
- Dark mode variant not implemented on the live site
- Animation durations and easing curves not extractable from static CSS
- Focus ring styles (keyboard accessibility outline) not observed — recommend 2px solid #d18cff with 2px offset
- Loading states (spinner, skeleton) not present in extracted assets
- Mobile navigation drawer (hamburger menu) exact styling (overlay, animation, link hierarchy) not captured
- Checkout flow uses Shopify default styling — brand colors may not carry through to Shopify-hosted checkout pages
- Social media icon colors extracted as brand defaults (e.g., Facebook blue, Instagram gradient) — not recolored to match brand palette
