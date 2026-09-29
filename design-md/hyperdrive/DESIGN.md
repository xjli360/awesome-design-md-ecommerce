---
version: alpha
name: "HyperDrive"
source_url: "https://www.hypershop.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dark, industrial palette anchored on #171717 — near-black with a trace of warmth — that makes every product shot of brushed aluminum and USB-C ports feel like a precision instrument under studio light. The brand lives in the gap between consumer electronics and pro gear: the canvas is #121212, the body text is #dedede (a pale silver rather than pure white), and the only color relief comes from the product itself — no accent hue competes with the anodized metal of the docks and hubs. Typography runs a custom family split across myFontBold, myFontMedium, myFontLight, and myFontRegular, with Inter as the fallback; headings sit at 24–32px in bold weight, body at 15–16px in regular, and the overall density is tight, technical, and information-rich. The site uses Shopify as its commerce layer, so checkout buttons inherit the platform's default blue-green (#008060) — a pragmatic concession that breaks the dark theme momentarily. Navigation is a fixed top bar at 60px with the HyperDrive wordmark in myFontMedium, category links in myFontRegular at 14px, and a cart icon with a badge count. Product cards use a soft 8px radius (`{rounded.sm}`), a 1px hairline in #2a2a2a, and hover states that lift the card with a subtle shadow — the only moment the interface acknowledges interactivity beyond the cursor. The overall effect is a store that feels like a component catalog for a hardware startup: functional, monochrome, and utterly deferential to the aluminum objects it sells.

colors:
  primary: "#171717"
  primary-active: "#2a2a2a"
  primary-disabled: "#3a3a3a"
  ink: "#dedede"
  body: "#b0b0b0"
  muted: "#888888"
  muted-soft: "#666666"
  hairline: "#2a2a2a"
  hairline-soft: "#333333"
  canvas: "#121212"
  surface-soft: "#1a1a1a"
  surface-card: "#1f1f1f"
  on-primary: "#ffffff"
  on-dark: "#dedede"
  shopify-checkout: "#008060"
  badge-new: "#ff6b35"
  badge-sale: "#e63946"
  star-rating: "#f4a261"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'myFontBold', Inter, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'myFontBold', Inter, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'myFontMedium', Inter, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'myFontMedium', Inter, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'myFontMedium', Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'myFontRegular', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'myFontRegular', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'myFontRegular', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'myFontLight', Inter, sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.38
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'myFontLight', Inter, sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.33
    letterSpacing: 0.1px
  badge:
    fontFamily: "'myFontMedium', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'myFontRegular', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'myFontMedium', Inter, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'myFontMedium', Inter, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'myFontRegular', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'myFontRegular', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  price:
    fontFamily: "'myFontMedium', Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-checkout:
    backgroundColor: "{colors.shopify-checkout}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary-active}"
  text-input-error:
    border: "1px solid {colors.badge-sale}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    border-bottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border-bottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline-soft}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.3)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.price}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    padding: "{spacing.md} 0 0"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 14px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary-active}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
    border-top: "1px solid {colors.hairline}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.ink}"
  cart-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  section-header:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.xl} 0 {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action for adding products to cart or proceeding to checkout. Uses the brand's near-black `#171717` fill with white text, 8px corner radius, and 44px height. On hover, the background shifts to `#2a2a2a` for a subtle lift; disabled state drops to `#3a3a3a` with muted text. Text is set in myFontMedium at 15px with 0.3px letter spacing.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "Compare". Transparent background with a 1px hairline border in `#2a2a2a` and `#dedede` text. Active state fills the background with `#1a1a1a`. Used alongside primary buttons to create visual hierarchy without introducing a second color.

**`button-ghost`** — A text-only button for tertiary actions like "Clear filters" or "Cancel". No background or border, muted gray text at 13px. Hover state changes text color to `#dedede`. Minimal footprint for dense UI areas like filter sidebars.

**`button-checkout`** — The Shopify checkout button, which breaks the dark theme with a green `#008060` background. This is a platform concession — the brand does not control this color. White text, 48px height, and full-width on mobile. Used exclusively in the cart drawer and at the final purchase step.

### Cards
**`product-card`** — The primary product display unit across collection pages and search results. A `#1f1f1f` surface with 8px rounded corners and a 1px `#2a2a2a` border. The image area occupies the top half with the same corner radius clipped to the top edges only. Title sits below in myFontRegular at 16px, price in myFontMedium at 18px. On hover, the border lightens to `#333333` and a subtle box shadow appears — the card lifts slightly from the dark canvas.

**`product-card-badge`** — A small uppercase label pinned to the top-left corner of product images. Orange `#ff6b35` for "NEW" badges, red `#e63946` for "SALE". Set in myFontMedium at 11px with 0.5px letter spacing and 2px horizontal padding. The badge sits flush against the card edge with no margin — it feels like a warehouse tag.

### Navigation
**`nav-bar`** — A fixed 60px top bar on the dark `#121212` canvas with a 1px bottom hairline. The HyperDrive wordmark is left-aligned in myFontMedium; category links (Docks, Hubs, Power, Accessories) are center-aligned in myFontRegular at 14px. The cart icon with badge sits right-aligned. Active nav links get a 2px bottom border in `#171717`. On mobile, the category links collapse into a hamburger menu.

**`search-bar`** — A compact 40px input field with `#1f1f1f` background and 8px radius. On focus, the border shifts to `#2a2a2a`. Placeholder text in `#666666`. The search icon sits inside the input on the left. On mobile, the search bar expands to full width below the nav bar.

### Forms
**`text-input`** — Standard form input for checkout fields (name, address, email). 40px height, `#1f1f1f` background, 8px radius, and a 1px `#2a2a2a` border. Focus state uses `#2a2a2a` border. Error state switches to red `#e63946`. Text is 14px myFontRegular in `#dedede`. The dark theme means inputs feel like recessed panels rather than elevated fields.

### Footer
**`footer-section`** — A `#1a1a1a` section at the bottom of every page, separated by a 1px hairline. Contains link columns (Support, Products, Company, Legal) in myFontRegular at 14px with `#888888` color. Hover state lifts links to `#dedede`. Social icons appear as simple glyphs in `#666666`. The footer is dense but quiet — no background images or decorative elements.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; search bar moves below nav; buttons go full-width; product cards stack with no gap |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; search bar remains in nav; side filters become a top filter bar |
| Desktop | 1128–1440px | Three-column product grid; full nav with all category links; search bar in nav; filters in left sidebar; product cards show hover states |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; nav remains same; product cards have increased padding |

### Touch Targets
- All buttons and interactive elements are minimum 44px height (exceeds Apple's 44pt guideline)
- Nav links have 48px tap area on mobile (padding extends hit area)
- Cart icon has 40px touch target with 8px internal padding
- Product card links (title, image) have minimum 48px tap zones
- Filter checkboxes use 24px touch targets with 8px padding

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger menu with slide-out drawer
- Category links in the nav are hidden on mobile; only the wordmark and cart remain visible
- Product filters collapse into a single "Filter" button that opens a bottom sheet
- The search bar collapses from a full input to a search icon that expands on tap
- Footer link columns collapse into accordion sections on mobile
- Product descriptions collapse to 3 lines with a "Show more" toggle

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted font names (`myFontBold`, `myFontMedium`, `myFontLight`, `myFontRegular`) appear to be custom font-family declarations from the Shopify theme — their actual font file names and weights could not be determined. The weights assigned in this document are inferred from the naming convention.
- Hover and active states for most components are inferred from common dark-theme patterns; the live site's actual hover transitions (duration, easing) could not be extracted.
- The extracted color palette is heavily skewed toward near-black and gray tones — the brand's true accent color (if any) could not be determined from the extracted hex list. The `badge-new` and `badge-sale` colors are standard e-commerce badge conventions, not confirmed brand colors.
- Shopify checkout colors (`#008060`) are platform defaults, not brand choices. The brand may override these in their checkout customization, but that could not be verified.
- Error states, loading states, and empty states for forms and product lists are not documented — these are standard Shopify defaults and may differ from the brand's intent.
- Dark mode is not applicable (the site is already dark-themed), but a light mode variant could not be extracted.
- The `star-rating` color (`#f4a261`) is a common amber tone for review stars; the brand may use a different shade or custom star icon.
- Typography line-height values are estimated from common web practices; the actual line-height declarations in the site's CSS could not be precisely extracted.
- Spacing values for component padding and margins are inferred from the extracted layout; the brand's actual spacing scale may differ.
- The `rounded` scale uses standard values; the brand may use custom radii not captured in the extracted CSS.
