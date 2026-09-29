---
version: alpha
name: "Third Eye Comics"
source_url: "https://shop.thirdeyecomics.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A comic book store that uses a high-voltage blue (#2932fc) as its primary signal — not the muted indigo or navy you'd expect from a pop-culture retailer, but a piercing, almost electric cobalt that reads as urgent and collectible. This blue appears on every primary CTA, the top nav bar, and the site's meta-theme-color (#000000) provides a pitch-black frame that makes the blue and the warm accent palette — a coral (#fb8077), a teal (#0da19a), a magenta (#ed66b2), and a purple (#86469c) — pop like variant covers on a spinner rack. The typography stacks Fjalla One (a condensed, all-caps display face with a newspaper-headline punch) for headings and Poppins (a geometric sans-serif with open apertures) for body text, creating a contrast between shouty, slabby display and clean, readable body copy. Product cards use a white canvas (#ffffff) with a soft gray hairline (#dedede) and rounded corners ({rounded.sm} ~8px), while the footer and secondary surfaces shift to a warm off-white (#f1f1f0) that keeps the experience from feeling cold despite the black-and-blue dominance. The overall mood is that of a convention booth or a comic shop's new-arrivals wall — dense, colorful, and designed to catch your eye from across the room.

colors:
  primary: "#2932fc"
  primary-active: "#1a22d6"
  primary-disabled: "#a0a3fe"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#737376"
  muted-soft: "#a0a0a0"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-coral: "#fb8077"
  accent-teal: "#0da19a"
  accent-magenta: "#ed66b2"
  accent-purple: "#86469c"
  badge-new: "#286ef8"
  badge-sale: "#fb8077"
  star-rating: "#ffb400"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Fjalla One', 'Poppins', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Fjalla One', 'Poppins', sans-serif"
    fontSize: 30px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Fjalla One', 'Poppins', sans-serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Fjalla One', 'Poppins', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Fjalla One', 'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 1px
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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-bar-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "8px 12px 4px"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "0 12px 12px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.base}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.canvas}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 36px
    padding: "0 12px"
  add-to-cart-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    height: 48px
    padding: "0 24px"

## Components

### Buttons
**`button-primary`** — The workhorse CTA, filled with the brand's electric blue (#2932fc) and white text. On hover, it shifts to a slightly deeper blue (`{colors.primary-active}`). The disabled state uses a pale blue (`{colors.primary-disabled}`) to indicate inactivity without losing brand identity. All buttons use Poppins 600 weight at 15px with 8px rounded corners for a friendly but assertive feel.

**`button-secondary`** — An outlined variant with a white fill and a 2px solid border in the primary blue. Used for secondary actions like "View Details" or "Cancel" where the full blue fill would be too heavy. The border keeps it visually connected to the primary button system.

**`button-accent-coral`** and **`button-accent-teal`** — Accent buttons for special promotions, limited-edition drops, or clearance sales. The coral (#fb8077) is used for "Sale" or "Clearance" CTAs, while the teal (#0da19a) appears on "Pre-Order" or "Coming Soon" buttons. These provide visual variety on product pages without competing with the primary blue.

### Navigation
**`nav-bar`** — A pitch-black (#121212) top bar that spans the full viewport width, creating a dramatic frame for the brand's logo and navigation links. The nav links use Fjalla One in all-caps at 15px with 1px letter spacing, rendered in white. The active link state switches to the primary blue, providing a clear wayfinding signal. The bar sits at 64px tall — compact enough for a comic shop's dense layout but tall enough to feel substantial.

**`nav-bar-link`** and **`nav-bar-link-active`** — Individual navigation items within the top bar. Inactive links are white, active links are primary blue. The all-caps Fjalla One treatment gives them a newspaper-headline urgency that matches the brand's comic-book aesthetic.

### Cards
**`product-card`** — A white card with 8px rounded corners and no padding at the container level (padding is handled by child elements). The card image uses `{rounded.sm}` on the top corners only, creating a natural photo frame. The title sits in Poppins 600 at 16px with 8px horizontal padding, and the price follows in regular 16px. This card appears in grid layouts on collection pages and search results.

**`product-card-title`** and **`product-card-price`** — Typography tokens for the card's text content. The title uses the ink color (#121212) for high contrast, while the price uses the body color (#3a3a3a) to keep it slightly less prominent.

### Badges
**`badge-new`** and **`badge-sale`** — Small uppercase badges that overlay product card images. The "New" badge uses a bright blue (#286ef8), while the "Sale" badge uses coral (#fb8077). Both are 11px Poppins 700 weight with 0.5px letter spacing, set in white on a colored background with 4px rounded corners.

### Forms
**`text-input`** — Standard text input with a white background, 1px hairline border (#dedede), and 8px rounded corners. On focus, the border thickens to 2px and switches to the primary blue, providing a clear active state. The input height of 48px matches the button height for aligned form layouts.

**`search-bar`** — A pill-shaped search input with a soft gray background (#f9f9f9), 1px hairline border, and fully rounded corners. The pill shape is a deliberate contrast to the more angular buttons and cards, giving the search experience a friendly, approachable feel.

### Footer
**`footer`** — A pitch-black footer matching the nav bar, creating a bookend effect. Links use the muted-soft gray (#a0a0a0) to keep them readable but less prominent than the main content. The footer uses 48px vertical padding and 16px horizontal padding, with body-sm typography for a clean, information-dense layout.

### Hero
**`hero-section`** — A full-width hero area on the black background, using the display-xl typography for the main headline and body-md for the subtitle. The hero is designed to feature new releases, events, or promotional campaigns with high visual impact.

**`hero-title`** and **`hero-subtitle`** — The hero's text components. The title uses Fjalla One at 36px in all-caps white, while the subtitle uses Poppins 400 at 16px in muted-soft gray.

### Tags
**`category-tag`** and **`category-tag-active`** — Pill-shaped tags for filtering products by category (e.g., "Marvel," "DC," "Indie"). Inactive tags have a soft gray background, while the active tag fills with the primary blue. The pill shape and 13px button-sm typography make them compact enough for horizontal scroll strips.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards go to 2-column grid; hero text reduces to display-md; search bar moves below nav; category tags scroll horizontally |
| Tablet | 744–1128px | Nav bar shows limited links (3-4); product cards in 3-column grid; hero maintains display-lg; search bar remains in nav area |
| Desktop | 1128–1440px | Full nav bar with all links; product cards in 4-column grid; hero uses display-xl; search bar centered in nav |
| Wide | > 1440px | Max-width container at 1440px; product cards in 5-column grid; hero content centered with max-width |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Nav bar links have 48px touch targets (8px padding on 64px bar)
- Category tags have 32px minimum height with 16px horizontal padding
- Search bar has 44px height with 20px horizontal padding
- Quantity selector buttons have 36px height with 12px horizontal padding

### Collapsing Strategy
- Nav bar links collapse to a hamburger menu icon below 744px
- Product card grid reduces columns: 5 → 4 → 3 → 2 as viewport shrinks
- Hero section reduces typography size and may stack vertically on mobile
- Category tag strip becomes horizontally scrollable on mobile with hidden overflow
- Footer links stack vertically on mobile, with reduced padding

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components (button-secondary, text-input, nav links) are inferred from common patterns but not extracted from the live site
- Error styling for form validation (border colors, error text colors, helper text) not observed
- Dark mode or high-contrast mode variants not present in extracted data
- Sub-brand or collection-specific color palettes (e.g., variant covers, exclusive editions) not captured
- Loading states (spinners, skeleton screens) not extracted
- Modal/dialog styling (overlay, close button, content padding) not observed
- Dropdown menu styling for nav bar (mega menu, sub-links) not extracted
- The extracted color list includes many generic web colors (grays, blues) — the brand's true primary (#2932fc) was identified as the most distinctive non-gray color, but accent colors (#fb8077, #0da19a, #ed66b2, #86469c) may represent promotional or limited-use colors rather than core brand tokens
- Font weights for Fjalla One (only available in 400) and Poppins (available in multiple weights) are inferred from common usage — exact weight usage per component may vary
- Spacing values are estimated from common e-commerce patterns; exact padding/margin values may differ on the live site
