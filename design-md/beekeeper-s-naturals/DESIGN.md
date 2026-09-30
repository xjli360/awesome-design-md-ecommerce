---
version: alpha
name: "Beekeeper's Naturals"
source_url: "https://beekeepersnaturals.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep navy (#334499) anchors Beekeeper's Naturals like a midnight apiary — it appears on every primary button, every header background, and every product-badge ribbon, giving the brand a serious, trusted-medicine weight that the honey-toned wellness category usually avoids. Against that blue, a marigold accent (#f8da52) and a forest green (#22522f) create a triad that reads as both apothecary and meadow: the gold appears on sale tags, star ratings, and secondary CTAs; the green on ingredient callouts and subscription badges. The canvas is a warm off-white (#f2f0f0) rather than pure white — a deliberate softening that makes the brand feel less clinical and more like a handwritten label on a tincture bottle. Typography splits between Ivy Presto (a serif with calligraphic swashes used for display headlines and product names) and Josefin Sans (a geometric sans-serif for body copy and buttons), creating a herbalist-meets-modern tension. Product cards use generous {rounded.lg} corners and a soft shadow, while the nav bar stays compact at 64px with a sticky white background and the marigold accent reserved for the cart icon. The checkout flow swaps the navy for a lighter blue (#013c31) on progress indicators, and the footer collapses into a dense, three-column grid of small links in {colors.muted} (#595959) — the only place the brand lets itself feel crowded.

colors:
  primary: "#334499"
  primary-active: "#1f1f1f"
  primary-disabled: "#d1cece"
  ink: "#121212"
  body: "#1f1c1a"
  muted: "#595959"
  muted-soft: "#858585"
  hairline: "#cfcfcf"
  hairline-soft: "#e3e3e3"
  canvas: "#f2f0f0"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#f8da52"
  accent-gold-active: "#fed83f"
  accent-green: "#22522f"
  accent-green-soft: "#013c31"
  badge-cream: "#fffbea"
  badge-cream-active: "#fefbeb"
  star-rating: "#f8da52"
  sale-badge: "#f8da52"
  subscription-badge: "#22522f"
  scrim: "#101010"

typography:
  display-xl:
    fontFamily: "'Ivy Presto', 'ivypresto-display', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Ivy Presto', 'ivypresto-display', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Ivy Presto', 'ivypresto-display', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Ivy Presto', 'ivypresto-display', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Josefin Sans', 'sofia-pro', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'Josefin Sans', 'sofia-pro', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Josefin Sans', 'sofia-pro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Josefin Sans', 'sofia-pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Josefin Sans', 'sofia-pro', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Josefin Sans', 'sofia-pro', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Josefin Sans', 'sofia-pro-condensed', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Josefin Sans', 'sofia-pro', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Josefin Sans', 'sofia-pro', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Josefin Sans', 'sofia-pro', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "'Josefin Sans', 'sofia-pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Josefin Sans', 'sofia-pro', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-gold-active:
    backgroundColor: "{colors.accent-gold-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 8px 0
  button-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0 0 16px 0
  product-card-image:
    rounded: "{rounded.lg}"
  product-card-title:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-sale-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.accent-gold}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.surface-card}"
    typography: "{typography.title-sm}"
  badge-subscription:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  cart-icon:
    backgroundColor: transparent
    textColor: "{colors.accent-gold}"
    height: 24px
  cart-icon-count:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 20px
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 16px 20px
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Subscribe," and "Shop Now" actions. Rendered in the deep navy (#334499) with white uppercase Josefin Sans text at 14px/600 with 1px letter-spacing. The 8px corner radius and 48px fixed height give it a solid, pill-like presence. On hover, the background shifts to near-black (#1f1f1f) with no border change. Disabled state drops to a muted gray (#d1cece) with soft-gray text (#858585) — used only on sold-out or pre-order items.

**`button-secondary`** — An outlined variant used for "Learn More" and secondary product actions. Uses the warm off-white canvas (#f2f0f0) background with navy text and a 1px navy border (implied by the background contrast). Active state shifts the background to the hairline-soft (#e3e3e3). Height and padding match the primary button for alignment in form layouts.

**`button-gold`** — The accent variant reserved for promotional CTAs, sale banners, and limited-time offers. Uses the marigold (#f8da52) background with dark ink (#121212) text. Active state deepens to the darker gold (#fed83f). This button is visually louder than the primary and should be used sparingly — typically once per page on the highest-value conversion action.

**`button-text`** — A text-only button used for "View Details," "Read Reviews," and filter resets. No background, navy text at 12px/600 uppercase with 0.8px letter-spacing. Active state darkens the text to near-black (#1f1f1f). Padding is minimal (8px vertical) to allow inline placement near product cards or descriptions.

### Cards
**`product-card`** — The primary product display unit on collection pages and search results. A white background card with 20px corner radius, no border, and a subtle shadow (implied by the card background contrast against the canvas). The image area occupies the top portion with matching 20px radius, followed by a 16px padded content area containing the product name (Ivy Presto 22px), price (Josefin Sans 16px), and optional badges. Badges sit in the top-left corner of the image area — green for subscription items, gold for sale items. Star ratings use the marigold color at 16px.

**`product-card-title`** — The product name rendered in Ivy Presto at 22px with 1.3 line-height. This is the only place the serif face appears at a small size, creating a handwritten-label feel against the otherwise geometric sans-serif system.

**`product-card-badge`** — A small, uppercase label pinned to the top-left of product images. Green background (#22522f) for subscription items, gold (#f8da52) for sale items. Uses 10px/700 condensed sans with 0.8px letter-spacing and 4px padding on all sides. The 4px corner radius keeps it sharp but friendly.

### Navigation
**`nav-bar`** — A sticky top navigation bar at 64px height with white background and no border-bottom (the hairline is implied by content contrast). Contains the brand logo (typically an SVG or text in Ivy Presto), 5-6 nav links in 13px/500 uppercase Josefin Sans, a search icon, and a cart icon. The cart icon uses the marigold accent (#f8da52) to draw the eye. Active nav links switch to the navy primary color; inactive links are muted (#595959).

**`nav-link-active`** — The currently selected navigation item. Navy text (#334499) with no underline or background change — the color shift alone signals state. Used in the top nav and footer link lists.

**`nav-link-inactive`** — Default navigation link state. Muted gray (#595959) text at 13px/500 uppercase. On hover, the color shifts to the navy primary (no dedicated hover token — the active color serves as hover).

### Forms
**`text-input`** — Standard text input for search, email capture, and checkout forms. White background, 16px Josefin Sans body text, 12px padding on all sides, 48px height, and 8px corner radius. Focus state adds a 2px navy border (implied by the focus token — the border color is the primary). Error state uses a red border (exact hex not extracted — see Known Gaps) with the same padding and typography.

**`search-bar`** — A full-pill search input used in the header and on search pages. White background with muted placeholder text (#595959) at 16px. The 9999px corner radius creates a pill shape. On focus, the placeholder shifts to ink (#121212) and the input gains a navy border.

### Footer
**`footer-section`** — The site footer, rendered on a near-black background (#121212) with soft-gray text (#858585). Three columns of links with uppercase headings in white (#ffffff) at 14px/600. Links are 14px/400 with no underline. On hover, link text shifts to the marigold accent (#f8da52). Padding is 48px vertical and 24px horizontal, with a 64px section gap above.

**`footer-heading`** — Column headings in the footer. White text at 14px/600 uppercase with 0.5px letter-spacing. No background — just the text on the dark footer background.

### Badges
**`badge-subscription`** — Green badge (#22522f) with white text, used on product cards and subscription CTAs to indicate recurring delivery options. 10px/700 uppercase condensed sans with 4px padding and 4px corner radius.

**`badge-new`** — Gold badge (#f8da52) with dark ink text, used on new product launches and seasonal items. Same typography and sizing as the subscription badge.

**`badge-sale`** — Gold badge identical to `badge-new` but used specifically for discounted items. The two gold badges share a token but differ in semantic usage — `badge-sale` appears on product cards with a strikethrough original price.

### Miscellaneous
**`star-rating`** — Product review stars rendered in the marigold accent (#f8da52) at 16px. Used on product cards and review sections. The star icon is typically a filled SVG glyph with no outline.

**`cart-icon`** — The shopping cart icon in the top nav. Rendered in marigold (#f8da52) at 24px height. The icon is typically a simple bag or basket outline. A count badge (navy circle with white number) overlays the top-right corner when items are in the cart.

**`cart-icon-count`** — The item count badge on the cart icon. An 18px navy circle (#334499) with white text at 11px/400. Positioned absolutely at the top-right of the cart icon.

**`accordion-header`** — Used on FAQ pages and product descriptions. A soft-gray background (#f5f5f5) with ink text at 14px/600 uppercase. 16px padding on all sides and 8px corner radius. Clicking expands the accordion content below.

**`accordion-content`** — The expandable content area below accordion headers. White background with body text at 16px/400. 16px padding and 8px corner radius. No border — the header and content share the same width and radius.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text shrinks to 28px; footer stacks to single column; search bar moves to full-width below nav; product cards use full-width with 16px horizontal padding |
| Tablet | 744–1128px | Two-column product grid; nav links visible (5-6 items); hero text at 36px; footer in two columns; search bar in nav remains pill but shrinks to 200px max-width |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero text at 48px; footer in three columns; search bar in nav at 300px max-width; product cards at 320px min-width |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero section expands to full-width with 80px padding; footer columns expand to four with additional legal links |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height (buttons are 48px, inputs are 48px, nav links have 44px tap area via padding)
- Cart icon and search icon have 44x44px tap targets (24px icon + 10px padding on each side)
- Accordion headers are 48px minimum height for easy tapping
- Product card CTAs are 48px tall and span the full card width on mobile
- Star ratings are 16px with 8px gap — individual stars are not interactive (the entire rating area links to reviews)

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger menu with a slide-out drawer; the search bar moves to a full-width row below the nav
- The footer collapses from three columns to a single vertical stack on mobile; accordion-style disclosure is used for footer link groups (headings are tappable to expand/collapse)
- Product filters (on collection pages) collapse to a horizontal scroll strip on mobile, with a "Filter" button that opens a bottom sheet
- The hero section collapses its image to a 50% height crop on mobile, with text overlay at the bottom
- Accordion content on FAQ pages collapses by default on all breakpoints — only the active section is expanded

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links are inferred from active states — exact hover hex values (e.g., a lighter navy for button-primary hover) were not extracted from the live site
- Error state hex for text inputs (red border) was not found in the extracted color list — a standard red (#d32f2f or similar) is assumed but not confirmed
- Dark mode is not present on the live site — no dark-mode tokens exist in the extracted data
- Sub-brand or seasonal color palettes (e.g., holiday promotions, limited-edition packaging) were not extracted — the palette above represents the core brand only
- Font weights for Ivy Presto are assumed at 400 (regular) based on display usage — the exact weight for display-xl (48px) may be 300 or 500 depending on the specific font file loaded
- The exact border radius for product-card images (whether they inherit the card's 20px radius or use a separate value) was not confirmed — the token assumes inheritance
- Shadow values (box-shadow for product cards, dropdowns, modals) were not extracted — the design system uses implied shadows via background contrast but exact blur/spread values are unknown
- Checkout-specific styling (Shopify Pay button, Klarna badge, Afterpay messaging) was not extracted — these may use third-party colors outside the brand palette
- The marigold accent (#f8da52) appears in multiple contexts (sale badges, star ratings, cart icon) — exact usage rules for when to use gold vs. navy as the primary accent were not documented
- The green accent (#22522f) usage is limited to subscription badges — it may also appear on ingredient callouts or "natural" labels, but this was not confirmed from the extracted data
