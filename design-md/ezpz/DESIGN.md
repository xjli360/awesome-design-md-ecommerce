---
version: alpha
name: "ezpz"
source_url: "https://ezpzfun.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A sage-and-coral feeding universe where #aaccaa — a soft, botanical green — sets the emotional temperature, not as an accent but as the dominant atmospheric color across page backgrounds, product photography backdrops, and the brand's signature silicone placemats. The palette is deliberately muted and non-stimulating: #73bec4 (a dusty teal that doubles as the browser chrome's theme-color), #fb8077 (a warm coral used sparingly for CTAs and sale badges), and a full spectrum of warm grays from #f6f6f6 canvas through #494949 body text to #121212 for deep ink. The brand trusts DM Sans at modest weights (400–600) and generous leading (1.5–1.6) to keep the reading experience calm and accessible for exhausted parents. Every product image sits on a clean white or sage ground with no hard shadows — the silicone mats and bowls are photographed flat, head-on, as if laid out on a nursery table. Buttons use {rounded.full} pill shapes in either primary teal or coral, with 48px minimum height for easy tapping by sticky toddler fingers. The navigation is a single-row affair with a centered logo, a search icon, and a cart badge — no mega-menus, no category dropdowns, just the brand's four product families as text links in {colors.muted-soft} #777777. The checkout flow inherits Shopify's default widget chrome, which introduces a slight visual break from the brand's soft palette, but the product pages themselves maintain a consistent 12px grid with 24px gutters and generous 64px section spacing that gives each product room to breathe.

colors:
  primary: "#73bec4"
  primary-active: "#5a9ea3"
  primary-disabled: "#c5e4e7"
  ink: "#121212"
  body: "#494949"
  muted: "#777777"
  muted-soft: "#777777"
  hairline: "#dedede"
  hairline-soft: "#e1e3e4"
  canvas: "#f6f6f6"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#aaccaa"
  accent-coral: "#fb8077"
  accent-coral-active: "#e0665e"
  accent-teal: "#73bec4"
  star-rating: "#494949"
  badge-sale: "#fb8077"
  badge-new: "#aaccaa"

typography:
  display-xl:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-accent-coral-active:
    backgroundColor: "{colors.accent-coral-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-pill-sage:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
    backgroundColor: "{colors.accent-sage}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  hero-section:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  search-icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
  cart-badge:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  social-icon:
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a full-pill in the brand's dusty teal (#73bec4). Used for "Add to Cart", "Shop Now", and primary form submissions. On hover, shifts to `{colors.primary-active}` (#5a9ea3). Disabled state uses `{colors.primary-disabled}` (#c5e4e7) with muted text. Minimum 48px height for touch accessibility.

**`button-secondary`** — An outlined pill on the `{colors.canvas}` background with `{colors.ink}` text. Used for secondary actions like "Learn More" or "View Details". The 1px border uses `{colors.hairline}` (#dedede). Same 48px height as primary for consistent vertical rhythm.

**`button-accent-coral`** — A high-visibility coral pill (#fb8077) reserved for urgency-driven actions: limited-time offers, sale entry points, and "Subscribe & Save" calls. Active state darkens to #e0665e. Shares the same dimensions and typography as `button-primary` to maintain form consistency.

**`button-pill-sage`** — A softer, smaller pill in the brand's sage green (#aaccaa) used for filter tags, category navigation, and "Explore" links within hero sections. Uses `{typography.button-sm}` at 40px height for a more compact footprint.

### Cards
**`product-card`** — The primary product display unit, a white card with `{rounded.md}` corners. The product image area sits on a sage-green (#aaccaa) background — a deliberate choice that makes the silicone products (often in white, coral, or teal) pop without competing. The title uses `{typography.title-md}` in `{colors.ink}`, price in `{typography.body-md}` in `{colors.body}`. No shadow — the card relies on the `{colors.hairline}` border for separation.

### Navigation
**`nav-bar`** — A single-row, 72px-tall navigation bar on `{colors.canvas}` (#f6f6f6). The logo is centered; to the left sit product family text links (e.g., "Placemats", "Bowls", "Sets") in `{colors.muted}`. To the right: a search icon button and a cart badge. The cart badge is a coral (#fb8077) pill with white text, sized 20px. Active nav links switch to `{colors.ink}` (#121212).

### Forms
**`text-input`** — Standard text input with `{rounded.sm}` corners, 48px height, and a 1px `{colors.hairline}` border. On focus, the border thickens to 2px and shifts to `{colors.primary}` (#73bec4). Used for email signups, search queries, and checkout fields. Placeholder text uses `{colors.muted}` (#777777).

### Badges
**`badge-sale`** — A coral pill badge (#fb8077) with white uppercase text, used to flag discounted items on product cards and collection pages. Padding is tight (4px 12px) to sit neatly on card corners.

**`badge-new`** — A sage-green pill badge (#aaccaa) with dark text, used for new arrivals and recently launched products. Shares the same dimensions and typography as the sale badge for visual consistency.

### Footer
**`footer-section`** — A full-width footer on `{colors.surface-soft}` (#f6f6f6) with `{spacing.xxl}` vertical padding. Links are `{colors.muted}` (#777777) in `{typography.link}`. Social icons are 32px circular buttons with muted text color. The footer includes a newsletter signup form using the standard `text-input` component.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero padding reduces to 32px; product cards stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav remains expanded with text links; hero uses 48px padding |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero uses 64px padding; product cards show hover states |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid can expand to four columns |

### Touch Targets
- All buttons and interactive elements: minimum 48px height, 44px width
- Nav links: minimum 44px tap area
- Search icon: 40px diameter circle
- Cart badge: 20px diameter, positioned with 8px offset from icon edge
- Product card "Add to Cart" buttons: 48px height, full-width on mobile

### Collapsing Strategy
- Navigation: text links collapse into a hamburger menu below 744px; the logo remains centered
- Product grid: collapses from 3 columns (desktop) to 2 (tablet) to 1 (mobile)
- Hero section: reduces vertical padding by 50% on mobile; background image may crop or stack
- Footer: multi-column link layout collapses to single column below 744px
- Search: expands to full-width overlay on mobile; remains a compact icon on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors include Shopify checkout widget defaults (e.g., payment button blues) that could not be reliably separated from brand colors — the palette above represents best-effort filtering
- Font-family declarations were extracted as raw CSS values including `!important` overrides; DM Sans appears to be the primary brand typeface but Arial and Helvetica are listed as fallbacks
- Hover and focus states for most components (beyond primary button) could not be extracted from static CSS
- Error state styling for form inputs (color, icon, message placement) was not visible in extracted data
- Dark mode or high-contrast mode variants are not present in the extracted CSS
- The brand's Shopify theme may introduce additional component styles (e.g., cart drawer, product variant selector) that were not captured
- Sub-brand or collection-specific palette variations (e.g., holiday editions) are unknown
- Animation durations, easing curves, and transition properties were not extractable from the static analysis
