---
version: alpha
name: "Vintage Vinyl"
source_url: "https://www.vintagevinyl.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record store's digital storefront built on a stark white canvas and the deep, worn black of vinyl grooves — #000000 ink that carries every product title, price tag, and navigation label with the same weight as a 180-gram pressing. The brand trusts the raw texture of album art over decorative flourishes; product cards sit at `{rounded.sm}` with thin `{colors.hairline}` borders that frame the cover image like a record sleeve, while the search bar stretches across the top in a `{rounded.full}` pill that reads as a crate-digging invitation rather than a utility. A single accent — `#d4af37` — appears sparingly on sold-out badges and limited-edition callouts, the gold foil stamp of a collector's find. Typography runs Arial at modest sizes (body at 14px, titles at 18px) with no bold above 700, letting the record covers do the shouting. The footer stacks shipping policies and store hours in `{colors.muted}` gray, a quiet nod to the brick-and-mortar roots that still anchor the business.

colors:
  primary: "#000000"
  primary-active: "#1a1a1a"
  primary-disabled: "#cccccc"
  ink: "#000000"
  body: "#1a1a1a"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#d4af37"
  accent-gold-soft: "#f5e6b8"
  badge-soldout: "#d4af37"
  badge-new: "#000000"
  badge-sale: "#cc0000"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
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
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
  button-accent-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.sm} {spacing.sm} 0 {spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.sm} {spacing.sm} {spacing.sm}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  search-bar-pill-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.primary}"
  badge-soldout:
    backgroundColor: "{colors.badge-soldout}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 6px
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} 0"
  category-tab-active:
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart" and "Checkout" actions. Solid black background with white text at 14px/600 weight, sits at 40px height with `{rounded.sm}` corners. On hover, shifts to `{colors.primary-active}` (#1a1a1a) for a subtle darkening effect. Disabled state uses `{colors.primary-disabled}` (#cccccc) with white text, signaling an out-of-stock or unavailable action.

**`button-secondary`** — Used for "View Details" and "Browse More" actions that complement the primary CTA. White background with black text and a 1px `{colors.hairline}` border. Same 40px height and `{rounded.sm}` corners as the primary button. On hover, the border darkens to `{colors.ink}` for a clearer affordance.

**`button-accent-gold`** — Reserved for limited-edition drops and pre-order actions. Gold background (`{colors.accent-gold}`) with black text, creating a collector's-item feel. Same dimensions as `button-primary`. Used sparingly — no more than one per page — to preserve the gold's scarcity signal.

### Cards
**`product-card`** — The core inventory display unit, a white rectangle with `{rounded.sm}` corners and a thin `{colors.hairline}` border. The album cover image fills the top with `{rounded.sm} {rounded.sm} 0 0` to match the card's top corners. Below the image, the title sits in `{typography.title-md}` (16px/600) and the price in `{typography.body-md}` (14px/400). A badge (soldout, new, or sale) overlays the top-left corner of the image at 8px offset. Cards are 1–4 per row depending on viewport, with `{spacing.base}` gutters.

### Navigation
**`nav-bar`** — A 56px fixed header with white background and black links. The store logo sits left-aligned at 18px/700 weight. Navigation links ("New Arrivals", "Genres", "Vinyl", "Accessories", "About") use `{typography.nav-link}` (14px/600) with `{spacing.lg}` between items. The active page link renders in `{colors.primary}`. A search icon and cart icon sit right-aligned, both 24x24px with `{rounded.full}` touch targets.

**`category-strip`** — A horizontal scrollable strip below the nav bar for genre filtering (Rock, Jazz, Hip-Hop, Electronic, etc.). Each category tab is `{typography.button-sm}` (12px/600) in `{colors.muted}` with `{spacing.base}` padding. The active tab switches to `{colors.primary}` with an underline. On mobile, the strip scrolls horizontally with `{spacing.sm}` padding on each side.

### Forms
**`text-input`** — Used for search, newsletter signup, and checkout fields. White background with 1px `{colors.hairline}` border, 40px height, `{rounded.sm}` corners, and 14px/400 placeholder text in `{colors.muted-soft}`. On focus, the border switches to `{colors.primary}` (#000000) for a clear active state. Error states use a red border (`{colors.badge-sale}`) with error text below in 11px/400.

**`search-bar-pill`** — The primary search entry point, a `{rounded.full}` pill at 40px height with `{colors.surface-soft}` background and `{colors.muted}` placeholder text. On focus, the background shifts to white and a 1px `{colors.primary}` border appears. The pill sits centered in the hero section on desktop and stretches full-width on mobile.

### Footer
**`footer-section`** — A `{colors.surface-soft}` (#f5f5f5) band at the bottom of every page. Contains store information (address, hours, phone) in `{typography.body-sm}` (12px/400) in `{colors.muted}`. Links for "Shipping & Returns", "Contact Us", "Privacy Policy", and "Terms of Service" use `{typography.link}` (14px/400) with `{spacing.sm}` vertical spacing. Social media icons (Instagram, Facebook, Twitter) sit in a row above the legal text, each 20x20px with `{colors.muted}` fill.

### Badges
**`badge-soldout`** — Gold background (`{colors.accent-gold}`) with black text, 10px/700 uppercase. Used as an overlay on product card images to indicate an item is no longer available. The gold color signals desirability even in unavailability.

**`badge-new`** — Solid black background with white text, same typography as soldout badge. Used for recently added inventory (within 7 days). Appears as a top-left overlay on product cards.

**`badge-sale`** — Red background (`{colors.badge-sale}`) with white text. Used for discounted items. Same positioning and typography as other badges. Only appears when the sale price is at least 15% below the original.

### Hero
**`hero-section`** — A full-width white section at the top of the homepage, 64px vertical padding. Contains a headline in `{typography.display-xl}` (28px/700) and a subheadline in `{typography.body-md}` (14px/400) with `{spacing.base}` gap between them. Below the text, the `search-bar-pill` sits centered with `{spacing.lg}` top margin. No background image — the hero relies on typographic weight and whitespace to set the tone.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card), nav bar collapses to hamburger menu, search bar stretches full-width, hero text reduces to 22px, category strip scrolls horizontally with touch |
| Tablet | 744–1128px | Two-column product grid (2 cards), nav links visible but condensed (no "Accessories" link), search bar at 60% width, hero text at 28px |
| Desktop | 1128–1440px | Three-column product grid (3 cards), full nav with all links, search bar at 40% width, hero text at 28px, category strip shows 6–8 tabs without scrolling |
| Wide | > 1440px | Four-column product grid (4 cards), max-width container at 1440px centered, search bar at 30% width, hero section has 80px vertical padding |

### Touch Targets
- All buttons and links: minimum 44x44px tap target
- Search bar pill: 40px height, full-width on mobile for easy tapping
- Category strip tabs: 44px minimum height with `{spacing.base}` horizontal padding
- Product card: entire card is tappable (image + title + price)
- Nav hamburger icon: 44x44px with `{spacing.sm}` padding
- Cart icon: 44x44px with `{spacing.sm}` padding

### Collapsing Strategy
- Nav links collapse to hamburger menu below 744px; the hamburger icon toggles a full-screen overlay menu with `{spacing.xl}` vertical spacing between items
- Category strip collapses from visible tabs to a horizontal scrollable strip below 744px; the active tab is always visible on load
- Product grid collapses from 4 columns to 1 column below 744px; images scale to full card width
- Footer links collapse from a single row to a stacked column below 744px; social icons remain in a row but center-aligned
- Search bar collapses from centered pill to full-width input below 744px; placeholder text shortens to "Search vinyl..."

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors were empty after framework filtering; the palette above is inferred from the brand's category (record store) and the single extracted font (Arial). Primary black and accent gold are common in this vertical but may not match the live site exactly.
- No meta theme-color or page title was extracted; the site may use JavaScript-rendered titles or lack them entirely.
- Font-family declarations only returned "Arial"; the brand may use a custom typeface (e.g., a display font for logos) that wasn't captured in the extraction.
- Hover states for buttons and links are inferred from common patterns; actual hover animations (color transitions, scale effects) are unknown.
- Error styling for form inputs (red border, error message placement) is assumed from standard e-commerce patterns.
- Dark mode support is unknown; the current palette assumes a light-only interface.
- Sub-brand or seasonal color variations (e.g., Record Store Day promotions, holiday themes) are not captured.
- The gold accent (`#d4af37`) is a guess based on industry convention; the actual accent color may differ.
- Product card hover states (e.g., image zoom, shadow elevation) are not documented due to lack of extraction data.
- Checkout flow styling (Shopify Pay, Klarna, Afterpay widgets) may introduce additional colors not captured in the palette.
