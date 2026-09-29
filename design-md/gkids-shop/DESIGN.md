---
version: alpha
name: "Gkids Shop"
source_url: "https://store.gkids.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A storefront for animated film that trusts its product imagery to do the heavy lifting, wrapping every DVD, Blu-ray, and collectible in a restrained gray-scale system anchored on #3a3a3a — the ink color that appears on every price, every product title, and every navigation label. The palette is almost monastic: #191919 for the deepest text, #4d4d4d and #555555 for secondary information, #777777 for muted labels and footnotes, all set against a #dedede hairline that separates rows and cards with a softness that avoids the harshness of pure black-on-white. The single departure from gray is #c1c9d1, a cool steel-blue that appears in badge backgrounds and subtle UI accents — it reads as the color of a winter sky or an ink wash, not as a brand color in the traditional sense. Typography runs Avenir Next at modest weights (400 for body, 600 for titles), with display sizes staying under 24px even on hero sections; the brand trusts the film stills and poster art to provide visual drama, not oversized type. Buttons are compact rectangles at `{rounded.sm}` with 12px vertical padding, never pill-shaped, never oversized — they sit quietly beside the product, inviting rather than demanding. The overall feel is that of a small, curated cinema lobby: clean, slightly cool, letting the movies speak.

colors:
  primary: "#3a3a3a"
  primary-active: "#191919"
  primary-disabled: "#777777"
  ink: "#191919"
  body: "#3a3a3a"
  muted: "#4d4d4d"
  muted-soft: "#555555"
  hairline: "#dedede"
  hairline-soft: "#c1c9d1"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-steel: "#c1c9d1"
  accent-steel-soft: "#e0e5ea"
  badge-bg: "#c1c9d1"
  badge-text: "#191919"
  footer-bg: "#121212"
  footer-text: "#777777"
  sale: "#4a5764"

typography:
  display-xl:
    fontFamily: "'Avenir Next', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'Avenir Next', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Avenir Next', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Avenir Next', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'Avenir Next', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Avenir Next', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Avenir Next', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Avenir Next', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Avenir Next', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Avenir Next', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Avenir Next', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Avenir Next', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
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
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 40px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.caption}"
  badge-new:
    backgroundColor: "{colors.accent-steel}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.lg} 0 {spacing.md} 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the store, used for "Add to Cart", "Checkout", and "Subscribe". A compact 40px-tall rectangle in `{colors.primary}` (#3a3a3a) with white uppercase text at 14px/600. On hover, it deepens to `{colors.primary-active}` (#191919). The disabled state fades to `{colors.primary-disabled}` (#777777) with no border change — the gray-on-gray signals unavailability without extra decoration.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Learn More". White background with `{colors.primary}` text and a 1px `{colors.hairline}` border. Hover fills the background with `{colors.surface-soft}` (#f5f5f5). Same 40px height and uppercase typography as the primary.

**`button-tertiary-text`** — A text-only button for inline actions like "Clear" or "Cancel". No background, no border, just `{colors.primary}` text at 14px/600 uppercase. Hover underlines or shifts opacity — the brand keeps it minimal.

**`button-pill`** — A small, fully rounded pill for filter chips, tag dismissals, or compact actions. 32px tall with 8px vertical padding, `{colors.primary}` background, white text at 12px/600 uppercase. Used sparingly — the brand prefers rectangles for primary actions.

### Cards
**`product-card`** — The core product display unit, used in grid and list views. No border radius, no shadow — the card is simply a container for the product image and text. The image fills the full width, with title (`{typography.title-md}` in `{colors.ink}`) and price (`{typography.body-md}` in `{colors.primary}`) stacked below with `{spacing.sm}` between them. Badges (New, Sale, Exclusive) sit in the top-left corner of the image area, using `{colors.accent-steel}` background with dark text.

**`cart-item`** — A horizontal row in the cart drawer or page, with product thumbnail, title, quantity selector, price, and remove link. Separated from adjacent items by a 1px `{colors.hairline}` bottom border. The remove link uses `{typography.caption}` in `{colors.muted}` — intentionally low-visibility to avoid accidental taps.

### Navigation
**`nav-bar`** — A 60px fixed top bar with white background and a 1px `{colors.hairline}` bottom border. Navigation links are uppercase 14px/600 in `{colors.muted}` (#4d4d4d), with the active page indicated by a 2px `{colors.primary}` bottom border. The logo (typically the GKIDS wordmark) sits left-aligned at 20px, with cart icon and search icon right-aligned. No dropdowns — the nav is flat and simple.

**`search-bar`** — A 40px tall text input with 1px `{colors.hairline}` border and `{rounded.sm}` corners. On focus, the border switches to `{colors.primary}`. The placeholder text uses `{colors.muted-soft}` (#555555). A search icon sits inside the left padding at 16px.

### Forms
**`text-input`** — Standard form input for checkout fields, newsletter signup, and account forms. 40px tall with 10px horizontal padding, 1px `{colors.hairline}` border, `{rounded.sm}` corners. Focus state swaps the border to `{colors.primary}`. Error state (not extracted) would likely use a red accent — this is a known gap.

**`quantity-selector`** — A compact horizontal control with minus/plus buttons flanking a centered numeric display. 40px tall with 1px `{colors.hairline}` border and `{rounded.sm}` corners. The buttons use `{colors.muted}` text on hover.

### Footer
**`footer`** — A dark section (`{colors.footer-bg}` #121212) with `{colors.footer-text}` (#777777) for all copy. Links are the same muted gray, with no underline decoration. The footer typically contains three columns: customer service links, about links, and social icons (which may use their brand colors — not extracted). Copyright text sits at the bottom in `{typography.caption}`.

### Badges
**`badge-new`** — A small uppercase label for new arrivals, using `{colors.accent-steel}` (#c1c9d1) background with `{colors.badge-text}` (#191919) text. 2px vertical padding, 6px horizontal, `{rounded.xs}` (2px) corners. Positioned absolutely over the product image top-left.

**`badge-sale`** — Same dimensions and typography as the new badge, but using `{colors.sale}` (#4a5764) background with white text. The darker steel-blue signals a different category of information (pricing vs. availability).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item per row), nav collapses to hamburger menu, search bar becomes full-width below nav, footer stacks vertically, product card images at full viewport width |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but may truncate to 4-5 items, search bar in nav at 240px width, footer in two columns |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links visible, search bar at 320px width, footer in three columns, max-width container at 1128px centered |
| Wide | > 1440px | Four-column product grid, same max-width container at 1128px with increased whitespace on sides, nav bar remains centered |

### Touch Targets
- All buttons and interactive elements minimum 40px height (exceeds Apple's 44px recommendation for critical actions, but meets WCAG 2.1 for non-critical)
- Product card tap targets: entire card is clickable, not just the title or image
- Quantity selector buttons: 40px × 40px minimum tap area
- Nav links: 60px height ensures comfortable tapping on mobile
- Cart item remove link: intentionally smaller (12px text) — secondary action, not primary

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger menu icon on the left, with the logo centered and cart icon on the right
- The product grid collapses from 3-4 columns to 1 column on mobile, ensuring each product card gets full-width image display
- The footer collapses from 3 columns to a single vertical stack on mobile
- Search bar moves from inline in the nav to a full-width section below the nav on mobile
- Collection headers reduce from `{typography.display-md}` (20px) to `{typography.title-lg}` (18px) on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only extracted for primary button (darkens to #191919). Secondary button hover (likely surface-soft fill) and text-input focus (border to primary) are inferred from common patterns — not verified from live site CSS.
- **Error states**: No form validation styling extracted. Error text color, border color, and icon usage are unknown.
- **Dark mode**: No dark mode detected on the live site. The footer uses #121212 as a dark section, but there's no system-preference toggle.
- **Social media icon colors**: The extracted palette includes #c1c9d1 which may be a social icon color (e.g., Facebook, Twitter, Instagram) — not confirmed as a brand color.
- **Checkout flow**: Shopify's default checkout styling may override brand tokens. The extracted colors may include Shopify Pay, Klarna, or Afterpay widget colors that aren't part of the GKIDS brand system.
- **Animation/transition**: No transition durations, easing functions, or animation properties extracted. The site likely uses simple 0.2-0.3s ease transitions on hover/focus states.
- **Sub-brand palettes**: GKIDS distributes films from multiple studios (Studio Ghibli, Cartoon Saloon, etc.). Product pages for specific films may use film-specific color accents that aren't captured in the store-level palette.
- **Font weights**: Only font-family names were extracted, not specific weights. The 400/600 assignments are inferred from common Avenir Next usage patterns — the live site may use 500 or 700 in specific contexts.
- **Spacing scale**: The spacing tokens are inferred from common e-commerce patterns and the extracted component dimensions. Not all values (e.g., section: 64px) are verified from the live site CSS.
- **Rounded corners**: The extracted site uses minimal rounding (4px on buttons, 0px on product cards). The `{rounded.full}` token is defined for potential use but not observed on any live component.
