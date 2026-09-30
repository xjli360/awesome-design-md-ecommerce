---
version: alpha
name: "Tokyo Otaku Mode"
source_url: "https://otakumode.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-energy marketplace for anime figures and merchandise, Tokyo Otaku Mode (TOM) uses a crisp white canvas punctuated by a signature cerulean blue (#0094c8) that acts as the brand's primary voltage—appearing across primary CTAs, navigation highlights, and key product badges. The palette is surprisingly restrained for an anime shop: a warm off-white canvas (#fafafa) and a deep near-black ink (#202020) create a clean stage for colorful product photography, while a secondary accent of gold (#d1aa00) and a bright lime (#c3d825) inject the playful energy fans expect. The typography system leans heavily on Lato for English text, paired with system CJK fonts like Hiragino Kaku Gothic Pro and Meiryo for Japanese product names—a bilingual design move that signals authenticity without sacrificing readability. Product cards use soft rounded corners (`{rounded.md}`) and generous whitespace (`{spacing.lg}`) to let the intricate figure photography breathe, while a persistent top nav with a search bar and cart icon keeps the shopping flow frictionless. The overall mood is clean and trustworthy rather than chaotic—a deliberate counterpoint to the dense, maximalist aesthetic of many otaku retailers.

colors:
  primary: "#0094c8"
  primary-active: "#007da9"
  primary-disabled: "#a0d8ef"
  ink: "#202020"
  body: "#555555"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#d0d0d0"
  hairline-soft: "#e9e9e9"
  canvas: "#fafafa"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#d1aa00"
  accent-gold-bright: "#f1cf00"
  accent-lime: "#c3d825"
  accent-red: "#c9171e"
  accent-orange: "#f08300"
  accent-cyan: "#00bcd4"
  star-rating: "#f8b500"
  badge-new: "#56b6ea"
  badge-sale: "#c9171e"

typography:
  display-xl:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
  link:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  price-sale:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  price-original:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: line-through

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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-lime:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    color: "{colors.accent-red}"
  product-card-price-original:
    typography: "{typography.price-original}"
    color: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-limited:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    height: 400px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.on-primary}"
  category-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  category-nav-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  cart-icon:
    color: "{colors.ink}"
    fontSize: 24px
  cart-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    width: 20px
    height: 20px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Pre-order," and checkout flows. Rendered in the brand's signature cerulean (#0094c8) with white text and a subtle 8px radius. On hover, it shifts to a deeper blue (#007da9); the disabled state uses a pale blue (#a0d8ef) to indicate inactivity without visual noise.

**`button-secondary`** — An outlined variant used for "View Details," "Wishlist," and secondary navigation actions. White background with cerulean text, matching the primary button's dimensions and radius for visual consistency. Hover state adds a thin border or subtle shadow.

**`button-accent-gold`** — Reserved for premium actions like "TOM Points" redemption, limited-edition drops, and membership upgrades. Uses the gold accent (#d1aa00) with dark text (#202020) to signal exclusivity and value.

**`button-accent-lime`** — Used sparingly for promotional CTAs, seasonal sales, or gamified actions like "Spin the Wheel." The bright lime (#c3d825) with dark text creates a high-energy callout that stands apart from the primary system.

### Cards
**`product-card`** — The core content unit for displaying anime figures, apparel, and collectibles. A white card with a 12px radius and a subtle drop shadow (0 1px 4px rgba(0,0,0,0.06)) that lifts on hover to 0 4px 12px rgba(0,0,0,0.1). The image area occupies the top two-thirds with a matching radius clipped to the card's top corners. Below, the title sits in 16px/600 weight, the price in 18px/700 weight, and sale prices appear in red (#c9171e) with the original price struck through in muted gray (#888888). Badges for "New," "Sale," or "Limited" overlay the top-left corner of the image.

**`hero-banner`** — A full-width promotional banner used for seasonal campaigns, new arrivals, and brand collaborations. The default background is the primary cerulean, but it can accept gradient overlays or product-specific imagery. Text is centered at 24px/700 weight with generous padding.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, white background, containing the TOM logo on the left, category links (Figures, Apparel, Accessories, etc.) in the center, and a search icon + cart icon on the right. The cart icon carries a red badge (#c9171e) with a white count number. On scroll, the bar gains a subtle bottom shadow (0 1px 3px rgba(0,0,0,0.08)).

**`category-nav`** — A secondary horizontal strip below the main nav for sub-categories (e.g., "Nendoroid," "Scale Figures," "Plush"). Links are 14px/700 weight in body gray (#555555) with the active category underlined in cerulean (#0094c8). On mobile, this collapses into a horizontal scrollable strip.

### Forms
**`text-input`** — Standard input fields for search, login, and checkout forms. White background, 44px height, 12px padding, 8px radius. On focus, a 2px cerulean ring (#a0d8ef) appears around the field. Placeholder text uses muted gray (#888888).

### Footer
**`footer`** — A dark footer section (#202020) with light gray text (#aaaaaa) for links and copyright information. Organized into columns for "Shop," "Help," "About TOM," and "Community." Links lighten to white on hover. Includes social media icons and a newsletter signup form.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero banner height reduces to 250px; search bar moves to a toggleable overlay; category nav becomes horizontally scrollable; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav remains full but category links may truncate; hero banner at 350px; footer in two-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav with all category links visible; hero banner at 400px; footer in four-column layout |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero banner may extend full width with background imagery |

### Touch Targets
- All interactive elements (buttons, links, icons) maintain a minimum 44x44px touch target on mobile
- Cart icon badge is 20x20px minimum, centered within the icon's touch area
- Product card images are tappable and link to product detail pages
- Category nav items have 48px minimum height for easy tapping

### Collapsing Strategy
- Main navigation collapses to a hamburger menu below 744px, revealing a full-screen overlay with all links and search
- Category sub-nav becomes a horizontal scrollable strip on mobile, with a "See All" option for overflow
- Footer columns stack vertically on mobile, with accordion-style expandable sections for each column
- Product filters (sort, category, price range) collapse into a single "Filter" button that opens a bottom sheet

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for secondary and tertiary buttons could not be reliably extracted from the live site; the active states provided are inferred from the primary button pattern
- Error states for form inputs (validation, error messages) were not observed in the extracted data
- The exact font sizes and line heights for body and display text are estimated based on common Lato usage patterns; the live site may use slightly different values
- Dark mode is not supported; the palette is light-only
- The extracted color list includes many grays and blues that may be from third-party widgets (e.g., social icons, payment badges); the primary (#0094c8) and accent colors were selected as the most distinctive and brand-relevant
- The font stack includes several CJK fonts (Apple LiSung, Hei, MS UI Gothic, PMingLiU, Simhei) that are likely fallbacks for Japanese text; the primary English font appears to be Lato based on usage patterns
- Sub-brand palettes for specific franchises or collaborations (e.g., "TOM Shop," "TOM Points") were not extracted
- Animation and transition durations (e.g., hover effects, modal transitions) were not captured
- The specific hex for the "TOM Points" badge and loyalty program elements could not be isolated from the general palette
