---
version: alpha
name: "BFI Shop"
source_url: "https://shop.bfi.org.uk"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep violet #783df6 anchors the BFI Shop experience — not a timid accent but a confident, almost theatrical primary that appears on every add-to-bag button, navigation highlight, and membership badge. This purple, paired with a secondary royal blue #003399, evokes the BFI's institutional heritage while the violet signals a modern, curated film-merchandise sensibility. The canvas is near-white #fefefe, with a warm gray #e8e8e8 for card backgrounds and a cool medium gray #494949 for body text, creating a clean, readable hierarchy that lets film posters and product photography carry the emotional weight. Typography runs Helvetica Neue Medium at modest sizes — display sits at 20–24px rather than the heavy 700+ weights common in e-commerce — trusting the brand's cultural authority over typographic muscle. Search bars use {rounded.full} pill shapes, product cards employ {rounded.sm} corners, and the persistent top nav carries the BFI logo alongside a dark #1e1e1e background for the primary navigation strip. The checkout flow introduces a secondary dark surface #202024 for the cart sidebar, creating a distinct transactional zone. Membership badges and limited-edition tags use the violet #783df6 against white, while sold-out indicators shift to the muted #e6e6e6. The overall mood is that of a cinema lobby gift shop — polished, slightly dramatic, and deeply respectful of the films it represents.

colors:
  primary: "#783df6"
  primary-active: "#5a2bc4"
  primary-disabled: "#c8b0f9"
  ink: "#1e1e1e"
  body: "#494949"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#e8e8e8"
  hairline-soft: "#f0f0f0"
  canvas: "#fefefe"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-dark: "#202024"
  on-primary: "#ffffff"
  accent-blue: "#003399"
  accent-dark: "#221155"
  sold-out: "#e6e6e6"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Helvetica Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Helvetica Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.2px
  link:
    fontFamily: "'Helvetica Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.2px

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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 56px
  sub-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 44px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
  badge-membership:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sold-out:
    backgroundColor: "{colors.sold-out}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-limited:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  cart-sidebar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  hero-banner:
    backgroundColor: "{colors.accent-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Bag", "Checkout", and "Subscribe". Rendered in the brand violet #783df6 with white text and {rounded.sm} corners. On hover, shifts to a darker violet #5a2bc4. Disabled state uses a pale lavender #c8b0f9 with white text, signaling the action is unavailable. Padding is 12px 24px with a 44px height for comfortable touch targeting.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Save for Later". Uses a white background with dark text #1e1e1e and a 1px solid hairline border #e8e8e8. Hover state adds a subtle shadow. Same dimensions as primary for consistent alignment.

**`button-accent-blue`** — Reserved for BFI membership-related CTAs and exclusive pre-order actions. Uses the royal blue #003399 with white text. Same sizing and rounded corners as the primary button. This button signals institutional authority and membership benefits.

### Cards
**`product-card`** — The core product display component, used across collection pages and search results. Features a white background with {rounded.sm} corners and a 1px hairline border #e8e8e8. The image area occupies the top portion with a soft gray #f7f7f7 background for loading states. Product title uses {typography.title-sm}, price uses {typography.body-md} in the body color #494949, and any badges overlay the top-left corner of the image. On hover, the card gains a subtle elevation shadow and the border shifts to the muted gray #e6e6e6.

**`product-card-image`** — The image container within a product card. Uses {rounded.sm} to match the parent card's corners. Background is the soft surface color #f7f7f7 for placeholder states. Images are cropped to a 3:4 aspect ratio for consistency across the catalog.

### Navigation
**`top-nav`** — The persistent primary navigation bar, fixed to the top of the viewport. Uses a dark background #1e1e1e with white text. Height is 56px on mobile, 64px on desktop. Contains the BFI logo on the left, a search icon on the right, and a hamburger menu on mobile. On desktop, the hamburger is replaced with category links using {typography.nav-link}.

**`sub-nav`** — A secondary navigation strip below the top nav for category filtering (e.g., "All", "Blu-ray", "DVD", "Merchandise", "Books"). Uses a white background with body-colored text. Active category is underlined with the primary violet #783df6. This strip scrolls horizontally on mobile with a fade-out gradient at the edges.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, and checkout forms. White background with a 1px hairline border #e8e8e8 and {rounded.sm} corners. Focus state uses a 2px primary violet #783df6 border. Placeholder text is the muted color #6a6a6a. Height is 44px with 10px 14px padding for comfortable typing.

**`search-bar-pill`** — The search input styled as a pill shape using {rounded.full}. Background is the soft surface color #f7f7f7 with body-colored text. On focus, the background shifts to white and a subtle shadow appears. Includes a magnifying glass icon on the left side. Height is 44px with 10px 20px padding.

### Badges
**`badge-membership`** — A small, prominent badge indicating BFI member pricing or exclusive member content. Uses the primary violet #783df6 background with white text. Text is uppercase with 0.5px letter spacing at 11px. Padding is 2px 8px with {rounded.xs} corners.

**`badge-sold-out`** — Indicates an item is no longer available. Uses a light gray #e6e6e6 background with muted text #6a6a6a. Same sizing and typography as the membership badge but with lower contrast to visually de-emphasize the item.

**`badge-limited`** — A special badge for limited edition releases, pre-orders, or exclusive items. Uses the accent blue #003399 background with white text. Same sizing as other badges but with a distinct color to draw attention to scarcity.

### Footer
**`footer`** — The site footer with a dark background #1e1e1e and light muted text #929292. Contains links to BFI policies, social media icons, and a newsletter signup form. Links use {typography.link} and shift to white on hover. The newsletter input uses the same styling as `text-input` but with a dark background variant.

### Hero
**`hero-banner`** — A full-width promotional banner at the top of the homepage or collection pages. Uses a deep dark background #221155 with white text. The display typography is set at 28px with -0.5px letter spacing for a slightly compressed, cinematic feel. A subtle gradient overlay ensures text readability over background images.

### Cart
**`cart-sidebar`** — A slide-in panel from the right side of the screen for the shopping cart. Uses a dark background #202024 with white text. Contains line items with product thumbnails, titles, quantities, and prices. The checkout button uses `button-primary` styling. On mobile, this panel takes the full screen width.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item per row), hamburger navigation, full-screen cart sidebar, hero banner collapses to 200px height, sub-nav scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid, top nav shows limited category links, cart sidebar is 400px wide, hero banner at 300px height |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all categories, cart sidebar is 480px wide, hero banner at 400px height |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, cart sidebar at 520px wide, hero banner at 500px height |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets span the full card area
- Filter tags and badges are minimum 32px tall for comfortable tapping
- Search bar and text inputs are 44px tall
- Navigation links have 48px touch areas within the top nav

### Collapsing Strategy
- Top nav collapses to hamburger menu on mobile (< 744px)
- Sub-nav becomes a horizontally scrollable strip on mobile with fade edges
- Product grid collapses from 4 columns to 1 column on mobile
- Cart sidebar becomes full-screen overlay on mobile
- Footer links collapse into accordion sections on mobile
- Hero banner text overlays collapse to single-line titles on mobile
- Search bar expands to full width on mobile when focused

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors appear to be a generic web palette (grays, one violet, one blue) — the violet #783df6 is the most distinctive and was selected as primary, but the brand may have additional accent colors (e.g., a specific film-related palette) that couldn't be extracted
- Font-family extraction returned "helvetica-neue-medium, sans-serif !important" — assumed Helvetica Neue across all weights, but the brand may use a custom or variable font for display sizes
- Hover states for buttons and cards are inferred from common patterns, not extracted from the live site
- Error states for form inputs (validation, error messages) were not observed
- Dark mode styling is not present on the live site
- Sub-brand or seasonal color palettes (e.g., BFI Flare, BFI London Film Festival) were not extracted
- Checkout flow colors may include Shopify Pay, Klarna, or Afterpay widget colors that couldn't be separated
- Stock image dominant tones may have influenced the extracted color list
- Specific spacing values and component dimensions are estimated from common e-commerce patterns, not directly extracted
