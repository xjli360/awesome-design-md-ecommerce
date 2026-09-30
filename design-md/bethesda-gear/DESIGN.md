---
version: alpha
name: "Bethesda Gear"
source_url: "https://gear.bethesda.net"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A dark, atmospheric storefront where the brand's signature #272d45 — a deep midnight blue — sets the stage for merchandise that glows against it. The palette reads like a dungeon-crawler's inventory screen: #676986 muted steel for secondary text, #f0b300 and #e32c2b as twin accent voltages (gold for loot, red for danger), and #2c3e50 for card surfaces that feel like forged metal plates. Type runs Trade Gothic as the primary voice — a condensed, muscular sans-serif that carries the weight of fantasy RPG titles — with Assistant and Montserrat as supporting faces for body copy and navigation. The store leans into a `{rounded.sm}` 8px corner radius across buttons and cards, never fully pill-shaped, preserving a slightly industrial feel that matches the Bethesda Game Studios aesthetic. Product cards sit on `{colors.surface-soft}` (#f4f4f6) canvases with `{colors.hairline}` (#dbdde4) borders, while the primary CTA button (#e32c2b) uses `{colors.on-primary}` white text and a `{rounded.sm}` 8px radius — a call to action that reads as urgent without being hostile. The nav bar runs full-width at 80px height, dark (#272d45) with white nav links, and the search bar adopts the same midnight background with a `{rounded.sm}` treatment. Badges use #f0b300 gold on dark backgrounds for "NEW" and "SALE" labels, while sold-out states fade to #787878 muted gray. The overall effect is a store that feels like walking through a game hub — dark corridors, illuminated displays, and loot that catches the light.

colors:
  primary: "#e32c2b"
  primary-active: "#cf3a34"
  primary-disabled: "#dedede"
  ink: "#121212"
  body: "#3f3f3f"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5eb"
  canvas: "#ffffff"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  surface-dark: "#272d45"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-gold: "#f0b300"
  accent-gold-active: "#dbb544"
  accent-red: "#e32c2b"
  accent-teal: "#00caaa"
  accent-teal-active: "#00756a"
  badge-sold-out: "#787878"
  badge-new-bg: "#f0b300"
  badge-new-text: "#121212"
  star-rating: "#f0b300"
  footer-bg: "#2c3e50"
  footer-text: "#e5e5eb"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Trade Gothic', 'Montserrat', 'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Trade Gothic', 'Montserrat', 'Assistant', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Trade Gothic', 'Montserrat', 'Assistant', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Trade Gothic', 'Montserrat', 'Assistant', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Trade Gothic', 'Montserrat', 'Assistant', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Trade Gothic', 'Montserrat', 'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', 'Montserrat', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Assistant', 'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Trade Gothic', 'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Trade Gothic', 'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Trade Gothic', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'Assistant', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Trade Gothic', 'Montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.27
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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.hairline}"
    padding: 10px 22px
    height: 44px
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.badge-new-text}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 80px
  nav-link:
    color: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    color: "{colors.accent-gold}"
  search-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0px 0px"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-new-bg}"
    textColor: "{colors.badge-new-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.link}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  checkout-button:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.badge-new-text}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in #e32c2b red with white text and an 8px `{rounded.sm}` corner. On hover, shifts to #cf3a34 active state. Disabled state fades to #dedede background with #676986 muted text. Used for "Add to Cart" and primary purchase flows.

**`button-secondary`** — White background with #121212 ink text and a `{rounded.sm}` corner. Used for secondary actions like "View Details" or "Continue Shopping." The outline variant adds a 2px #dbdde4 hairline border for visual distinction against white canvases.

**`button-gold`** — The #f0b300 gold accent button with dark #121212 text. Used sparingly for premium actions like "Pre-Order" or "Limited Edition" purchases. Carries the same 8px radius and 44px height as primary buttons.

**`button-dark`** — Deep midnight blue (#272d45) background with white text. Used for actions within dark-themed sections or hero banners. Maintains the consistent 44px height and `{rounded.sm}` corner.

### Cards
**`product-card`** — White card with `{rounded.sm}` corners and no padding at the container level. The product image fills the top with `{rounded.sm} {rounded.sm} 0px 0px` corner treatment. Title uses `{typography.title-sm}` with 16px horizontal padding, price uses `{typography.body-md}` in #121212 ink. Cards sit on `{colors.surface-soft}` (#f4f4f6) backgrounds with `{colors.hairline}` (#dbdde4) borders between items.

### Badges
**`badge-new`** — Gold (#f0b300) background with dark (#121212) text, 11px uppercase Trade Gothic at 700 weight, 4px `{rounded.xs}` corner. Used for new arrivals and restocks. **`badge-sale`** uses the primary red (#e32c2b) with white text. **`badge-sold-out`** uses muted gray (#787878) with white text. All badges have 2px vertical and 8px horizontal padding.

### Navigation
**`nav-bar`** — Full-width 80px bar in #272d45 midnight blue. Nav links use 15px uppercase Trade Gothic at 600 weight with 0.5px letter-spacing, white text. Active state highlights in #f0b300 gold. The search bar within the nav uses the same dark background with a `{rounded.sm}` corner and white text placeholder.

### Forms
**`text-input`** — White background, 44px height, `{rounded.sm}` corner, 1px #dbdde4 hairline border. On focus, border thickens to 2px #e32c2b red. Uses `{typography.body-md}` (Assistant 16px/400). Used for email signup, search, and checkout fields.

### Footer
**`footer`** — Deep navy (#2c3e50) background with light gray (#e5e5eb) text. Links use `{typography.link}` (Assistant 14px/400). Padding uses `{spacing.section}` (64px) vertically and `{spacing.xl}` (32px) horizontally. Contains site navigation, social links, and legal text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, reduced hero height (300px), stacked footer, 16px page padding |
| Tablet | 744–1128px | 2-column product grid, expanded nav with dropdowns, 400px hero, 24px page padding |
| Desktop | 1128–1440px | 3-4 column product grid, full nav bar, 400px hero, 32px page padding, max-width container |
| Wide | > 1440px | 4-column product grid, max-width 1440px centered, expanded hero with parallax |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have 48px touch targets (16px horizontal padding on 15px text)
- Product card tap targets cover full card width with minimum 120px height
- Quantity selector and dropdowns use 44px minimum touch area

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product filters collapse to modal/drawer below 744px
- Footer link columns stack vertically below 744px
- Hero text overlay reduces font size from 32px to 24px on mobile
- Search bar collapses to icon-only trigger below 744px, expanding to full-width overlay on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from static CSS; only primary button active state was confirmed
- Error styling for form validation (red borders, error messages) not observed in extraction
- Dark mode variant not present on live site; all observed pages use light canvas with dark nav/footer
- Sub-brand palettes for individual game franchises (Fallout, Elder Scrolls, Starfield, Doom) not extracted; each likely has its own accent colors
- Typography hierarchy beyond display and body sizes is inferred from common patterns; exact font sizes for h2-h6 not confirmed
- Spacing scale is estimated from observed padding/margin patterns; exact section spacing may vary
- Checkout flow colors (Shopify Pay buttons, Klarna badges) were filtered from extraction but may introduce additional accent colors
- Animation and transition durations (hover fades, card lifts) not extracted
- Iconography system (cart icon, search icon, menu icon) not captured; likely uses SVG or icon font
- Loading states and skeleton screens not observed
- Mobile nav drawer design (slide-in vs overlay) not confirmed from extraction
