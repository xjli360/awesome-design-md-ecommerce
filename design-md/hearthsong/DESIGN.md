---
version: alpha
name: "HearthSong"
source_url: "https://www.hearthsong.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A childhood wonderland built on a canvas of warm white (#f7f7f8) and struck through with a single, unmistakable voltage: marigold (#f4af23). That yellow isn't a background wash — it's the brand's primary action, the color of the "Add to Cart" button, the price tag, the star-rating highlight, the little flag that says "Sale." It sits alongside a deep, almost-black ink (#121212) that gives headlines and product names a sturdy, no-nonsense gravity, while a secondary navy (#272d45) appears in footer blocks and section backgrounds to signal trust and durability. The palette is deliberately limited: a cool gray (#676986) for secondary text, a soft lavender-gray (#e5e5eb) for dividers and hairline rules, and a bright sky blue (#2a73e6) reserved for links and informational badges — a single accent that reads as "click here for details" rather than decoration. Typography leans on the geometric clarity of Assistant and Figtree, with Gilroy appearing in display contexts for a slightly more playful, rounded headline. Buttons are generously padded and softly rounded (`{rounded.sm}` ~8px), never pill-shaped — the brand prefers a friendly but grounded corner. Product cards sit on white (`{colors.canvas}`) with a subtle shadow, and the search bar is a full-width rectangle with a yellow submit orb, not a floating pill. The overall mood is open, bright, and slightly nostalgic — a digital toy store that trusts color to do the emotional work rather than heavy typography or ornate illustration.

colors:
  primary: "#f4af23"
  primary-active: "#e59f04"
  primary-disabled: "#ffd114"
  ink: "#121212"
  body: "#4d4d4d"
  muted: "#676986"
  muted-soft: "#d3d4dd"
  hairline: "#e5e5eb"
  hairline-soft: "#ececec"
  canvas: "#f7f7f8"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#121212"
  accent-blue: "#2a73e6"
  accent-blue-soft: "#99caf8"
  accent-blue-bg: "#edf2fb"
  navy: "#272d45"
  navy-dark: "#181b41"
  sale-red: "#cd592a"
  star-gold: "#f4af23"
  footer-bg: "#272d45"
  footer-text: "#e5e5e5"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Gilroy', 'Figtree', 'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Gilroy', 'Figtree', 'Assistant', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Figtree', 'Assistant', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Figtree', 'Assistant', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', 'Assistant', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', 'Figtree', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Figtree', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'Figtree', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Assistant', 'Figtree', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Assistant', 'Figtree', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Figtree', 'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Figtree', 'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Assistant', 'Figtree', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', 'Assistant', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  footer-link:
    fontFamily: "'Assistant', 'Figtree', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
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
    height: 48px
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
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.button-sm}"
  button-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.accent-blue}"
  text-input-error:
    border: "2px solid {colors.sale-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-price:
    typography: "{typography.title-md}"
    color: "{colors.primary}"
    padding: "0 {spacing.base}"
  product-price-sale:
    color: "{colors.sale-red}"
  product-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-free-shipping:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-gold}"
    size: 16px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.footer-link}"
    padding: "{spacing.section} {spacing.lg}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.canvas}"
    marginBottom: "{spacing.base}"
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.06)"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, filled with marigold (#f4af23) and set in dark ink (#121212) for high contrast. On hover, the background deepens to #e59f04. The disabled state uses a lighter yellow (#ffd114) with muted text. Padding is generous at 12px 24px, and the corner is softly squared at 8px — never pill-shaped. A secondary outline variant (`button-secondary`) uses a white fill with a 1px hairline border, and a text-only variant (`button-text`) appears in accent blue for less prominent actions like "View Details" or "Learn More."

**`button-sale`** — A compact, urgent button in sale red (#cd592a) with white text, used on product cards and sale banners. Smaller padding (8px 16px) and shorter height (36px) allow it to sit inline with product titles without overwhelming the card layout.

### Cards
**`product-card`** — A white card with a 12px corner radius and a subtle drop shadow (0 2px 8px rgba(0,0,0,0.08)). The product image sits flush to the top corners, while the title and price are padded below. On hover, the shadow deepens to 0 4px 16px rgba(0,0,0,0.12), creating a gentle lift. The price is always rendered in the primary marigold, except during sale events when it switches to sale red.

**`category-card`** — A smaller, flatter card (8px radius, lighter shadow) used for category navigation grids. Content is centered with base padding, and the title sits below a category icon or image.

### Navigation
**`nav-bar`** — A fixed 72px white bar with dark ink navigation links set in Figtree 600 weight. The active page is indicated by a 2px marigold underline. On hover, link text shifts to the primary marigold. The bar contains the brand logo on the left, category links in the center, and utility icons (search, account, cart) on the right.

**`search-bar`** — A full-width rectangular input with a 1px hairline border and 8px corner radius. The search submit button is a 40px square filled with marigold, containing a white magnifying glass icon. On focus, the input border switches to a 2px accent blue stroke.

### Badges
**`badge-new`** — A small, uppercase label in accent blue (#2a73e6) with white text, used to flag new arrivals. Tight padding (2px 8px) and a 4px corner keep it unobtrusive. **`badge-sale`** uses sale red, and **`badge-free-shipping`** uses navy (#272d45) — each badge color signals a different type of promotion without competing with the product card's primary marigold price.

### Footer
**`footer`** — A dark navy (#272d45) section with light gray text (#e5e5e5). Column headings are set in white title-sm weight. Links are 14px regular weight with generous line height for readability. The footer spans the full viewport width and contains brand information, customer service links, and social icons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; search bar becomes full-width below nav; footer columns stack vertically; hero banner reduces padding to 32px |
| Tablet | 744–1128px | Nav shows top-level categories only; product cards in 2-column grid; search bar remains full-width; footer shows 2-column layout |
| Desktop | 1128–1440px | Full nav with dropdowns; product cards in 3-4 column grid; search bar in nav; footer shows 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-5 column grid; increased whitespace around hero and category sections |

### Touch Targets
- All interactive elements (buttons, links, icons) maintain a minimum 44px touch target height.
- Nav hamburger icon is 48px × 48px.
- Product card tap area spans the full card width.
- Search submit button is 40px × 40px — slightly below ideal but acceptable with surrounding padding.

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-out drawer.
- Secondary footer links collapse into accordion sections on mobile.
- Category cards switch from a horizontal scroll strip to a vertical grid below 744px.
- Hero banner text reduces from display-xl to display-lg on tablet, and display-md on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were inferred from common patterns; the live site's actual `:hover` and `:focus` styles were not extractable from static CSS alone.
- Error and validation styling for form inputs (text-input-error) is assumed based on the sale red (#cd592a) being the only red in the palette; actual error styling may differ.
- The extracted font list includes "Gilroy" which may be a fallback or unused declaration; Assistant and Figtree appear more consistently in rendered text. Gilroy is used here for display headlines based on its presence in the extracted declarations.
- The extracted color list is large (30+ hex values) and includes many grays and blues that may belong to Shopify checkout widgets, social icons, or stock photography. The primary marigold (#f4af23) was selected as the most distinctive non-generic color. Secondary navy (#272d45) and accent blue (#2a73e6) were chosen based on frequency and contextual appearance in footer and link areas.
- Dark mode is not supported; all colors assume a light canvas.
- Sub-brand or seasonal palette variations (e.g., holiday themes) were not extracted.
- The `oke-widget-icons` font-family declarations suggest Okendo review widgets are integrated, but review-specific styling (star sizes, widget padding) could not be determined.
- Spacing values for section padding and component heights are best estimates based on common e-commerce patterns; exact pixel values from the live site were not extractable.
