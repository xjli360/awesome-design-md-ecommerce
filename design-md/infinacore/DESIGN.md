---
version: alpha
name: "InfinaCore"
source_url: "https://www.infinacore.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A charging-essentials brand that runs on a #108474 teal voltage — the color of a circuit board's copper trace under green solder mask — set against a near-black #0b0d0c ink that reads as technical rather than luxury. The palette is deliberately narrow: a white #eeeeee canvas, a single accent teal, and a warm signal yellow #e9a220 that appears only on discount badges and limited-edition packaging callouts, never on primary actions. Type uses Nunito Sans at generous 18-20px body sizes with 1.5 line-height, giving product descriptions a reading-room cadence unusual for accessories retail. Every product card is a white #ffffff rectangle with a soft #d1d1d1 hairline and {rounded.sm} corners — no drop shadows, no gradients — creating a catalog-grid feel that lets the physical product photography (cables, bricks, MagSafe pucks) do the selling. The top nav is a full-bleed #0e0e0e bar with white text, a single centered logo, and a cart icon that flips to #108474 on hover. Search is a pill-shaped field with a #555555 border and {rounded.full} corners, placed in the nav's right gutter. The brand's signature move is the "power ring" — a circular #108474 stroke that animates around the hero product image on page load, suggesting wireless energy transfer. Checkout buttons are full-width teal pills with white text, 48px tall, using {typography.button-md} at 600 weight. Error states use #c60101 red, success states use #13e601 green — both applied sparingly to form validation only. The overall mood is industrial minimalism with a single warm accent: a charging brand that wants to feel like the device itself, not the lifestyle around it.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#a3d5c9"
  ink: "#0b0d0c"
  body: "#2c2a2a"
  muted: "#555555"
  muted-soft: "#7b7b7b"
  hairline: "#d1d1d1"
  hairline-soft: "#e7e7e7"
  canvas: "#eeeeee"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#e9a220"
  accent-yellow-active: "#d18c14"
  success: "#13e601"
  error: "#c60101"
  nav-bg: "#0e0e0e"
  badge-new: "#a89cc8"
  badge-sale: "#e9a220"
  star-rating: "#ffca10"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', Inter, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito Sans', Inter, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Nunito Sans', Inter, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Inter, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Inter, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Inter, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Inter, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', Inter, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', Inter, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', Inter, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Nunito Sans', Inter, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  link:
    fontFamily: "'Nunito Sans', Inter, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', Inter, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Nunito Sans', Inter, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0

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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  text-input-error:
    borderColor: "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.surface-card}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-cart-icon:
    textColor: "{colors.surface-card}"
    hoverTextColor: "{colors.primary}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
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
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  power-ring-hero:
    strokeColor: "{colors.primary}"
    strokeWidth: 3px
    size: 280px
    animation: "spin 4s linear infinite"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  footer:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    hoverTextColor: "{colors.primary}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0"

## Components

### Buttons
**`button-primary`** — Full-width teal pill with white text, used for all primary checkout and add-to-cart actions. On hover, shifts to `{colors.primary-active}` (#0d6b5d). Disabled state uses `{colors.primary-disabled}` (#a3d5c9) with cursor not-allowed. The pill shape (`{rounded.full}`) is consistent across all button variants — no squared-off primary buttons exist in the system.

**`button-secondary`** — White pill with a 1px `{colors.hairline}` border and `{colors.ink}` text. Used for "Learn More" and "View Details" links within product cards. Active state fills the background with `{colors.hairline-soft}` (#e7e7e7). No disabled variant defined — secondary buttons are always interactive.

**`button-accent-yellow`** — Smaller 36px pill using `{colors.accent-yellow}` (#e9a220) background with dark `{colors.ink}` text. Reserved exclusively for sale badges, limited-edition callouts, and promotional banners. Active state darkens to `{colors.accent-yellow-active}` (#d18c14). Never used for primary purchase flows.

### Navigation
**`nav-bar`** — Full-bleed `{colors.nav-bg}` (#0e0e0e) bar at 64px height. Contains a centered logo mark (the InfinaCore "I" with a lightning-bolt terminal) and a right-aligned cart icon. The cart icon defaults to white and transitions to `{colors.primary}` on hover — the only color shift in the entire nav. No dropdown menus, no search bar in the nav (search lives below the hero on mobile, in the nav gutter on desktop). The nav is sticky with a 1px `{colors.hairline}` bottom border on scroll.

**`nav-link`** — Uppercase 14px/600 weight text in white, used for footer navigation columns and mobile menu items. Not used in the top nav (which has no text links). Letter-spacing 0.5px gives a technical, spec-sheet feel.

### Product Cards
**`product-card`** — White rectangle with `{rounded.sm}` corners and a 1px `{colors.hairline}` border. No shadow. The card contains a 4:3 product image at the top (with top corners rounded), followed by the product title in `{typography.title-sm}` (18px/600) and the price in `{typography.price}` (18px/700). The price uses `{colors.primary}` for the dollar amount and `{colors.muted}` for the decimal cents. On hover, the card gains a 2px `{colors.primary}` border and a subtle scale(1.02) transform. Cards are laid out in a responsive grid with 16px gaps.

**`badge-new`** — Small lavender (#a89cc8) badge with white uppercase text, placed at the top-left of product card images. Used for newly launched SKUs. 2px horizontal padding, 4px height.

**`badge-sale`** — Yellow (#e9a220) badge with dark text, same dimensions as `badge-new`. Used for discounted items. The two badge types never appear on the same card.

### Forms & Inputs
**`text-input`** — White 48px input with 1px `{colors.hairline}` border and `{rounded.sm}` corners. Focus state adds a 2px `{colors.primary}` box-shadow and `{colors.primary}` border. Error state swaps to `{colors.error}` (#c60101) border with a red helper text below. Placeholder text uses `{colors.muted}` (#555555). Used for email capture, search, and checkout address fields.

**`search-bar-pill`** — 40px pill with `{rounded.full}` corners, white background, and `{colors.muted}` placeholder text. Contains a magnifying glass icon in `{colors.muted-soft}` (#7b7b7b). On focus, the border shifts to `{colors.primary}`. On desktop, this sits in the nav bar's right gutter; on mobile, it appears below the hero as a full-width element.

### Hero & Visual Elements
**`hero-section`** — Full-width section on `{colors.canvas}` (#eeeeee) background with `{spacing.section}` vertical padding. Contains a single product hero image (typically a charging station or cable bundle) centered with the `power-ring-hero` animation. Below the image: a `{typography.display-xl}` headline in `{colors.ink}`, a `{typography.body-md}` subhead in `{colors.body}`, and a `{typography.button-md}` primary CTA. No carousel — the hero is a single static frame.

**`power-ring-hero`** — A 280px circular stroke in `{colors.primary}` that rotates around the hero product image. The stroke is 3px thick with a 12px gap at the top (charging indicator metaphor). Animation is a continuous 4-second spin. Only visible on the homepage hero; removed on product detail pages.

**`star-rating`** — 16px star icons in `{colors.star-rating}` (#ffca10). Used on product cards and review sections. Empty stars use `{colors.hairline}` (#d1d1d1). The rating number (e.g., "4.8") sits beside the stars in `{typography.caption}` with `{colors.muted}` color.

### Footer
**`footer`** — Full-bleed `{colors.nav-bg}` (#0e0e0e) section with `{spacing.section}` padding. Contains four columns of navigation links (Shop, Support, Company, Connect) in `{typography.nav-link}` uppercase. Below the columns: a horizontal `{colors.hairline}` divider, then a row with copyright text in `{typography.caption-sm}` and social media icons. All links default to `{colors.muted-soft}` (#7b7b7b) and hover to `{colors.primary}` (#108474). The footer also contains a newsletter signup form using `{typography.text-input}` and `{typography.button-primary}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card). Hero image at 100% width. Search bar moves below hero. Nav bar collapses to hamburger menu. Footer columns stack vertically. Power-ring animation reduced to 200px. |
| Tablet | 744–1128px | Two-column product grid (2 cards). Nav bar shows logo and cart only (no search). Search bar appears below hero as a centered pill. Footer columns display in 2x2 grid. Power-ring at 240px. |
| Desktop | 1128–1440px | Three-column product grid (3 cards). Full nav bar with search pill in right gutter. Footer columns in 4-column layout. Power-ring at full 280px. Hero image at 60% container width. |
| Wide | > 1440px | Four-column product grid (4 cards). Max-width container at 1440px, centered. All desktop behaviors maintained with additional whitespace. Power-ring scales to 300px. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility.
- Product card tap targets are the entire card surface (not just text).
- Cart icon has 48x48px hit area.
- Hamburger menu button on mobile is 48x48px.
- Star rating stars are 24x24px on touch devices.

### Collapsing Strategy
- Top nav: On mobile, the nav bar collapses to a hamburger menu with a slide-out drawer. The drawer contains all nav links in `{typography.nav-link}` uppercase with 48px tap targets.
- Product grid: Collapses from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile). Gap remains constant at 16px.
- Footer: Collapses from 4 columns → 2 columns (tablet) → single column (mobile). The newsletter signup form becomes full-width on mobile.
- Hero section: On mobile, the power-ring animation is removed entirely to reduce motion and page weight. The hero image stacks vertically above the text content.
- Search bar: Moves from nav bar (desktop) to below hero (mobile/tablet) and becomes full-width.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only primary button and nav cart icon hover states were extractable. Secondary button, link, and card hover states are inferred from common patterns — actual values may differ.
- **Error/validation styling**: Error color (#c60101) and success color (#13e601) were extracted from the palette but their exact application (border, background, text) is inferred. Form validation message styling is unknown.
- **Dark mode**: No dark mode variant was detected. The brand uses a dark nav and footer but the main canvas is light (#eeeeee). A system-level dark mode may not exist.
- **Typography scale**: Font sizes, weights, and line heights are estimated from the extracted Nunito Sans usage and common e-commerce patterns. The exact type scale may differ — particularly display sizes (32px for display-xl is an estimate).
- **Spacing scale**: The spacing tokens follow a standard 4px/8px/16px/24px/32px/48px/64px scale common to Shopify themes. Actual spacing values on the live site may vary by 2-4px.
- **Animation details**: The power-ring animation (spin duration, stroke gap, size) is inferred from the brand's visual metaphor. Actual animation parameters may differ.
- **Sub-brand palettes**: No secondary brand colors (e.g., for product lines like "MagSafe" vs "USB-C") were extractable. The palette is treated as monolithic.
- **Checkout flow**: Shopify's default checkout styling may override brand colors. The extracted palette includes some Shopify-widget colors that were filtered out — actual checkout appearance may differ from the design system described here.
- **Font stack**: The extracted font-family declarations include "Nunito Sans" as the primary brand font, but also show "Inter", "Arial", and "Helvetica" as fallbacks. The exact font loading strategy (Google Fonts, self-hosted) is unknown.
