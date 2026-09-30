---
version: alpha
name: "Marky Sparky"
source_url: "https://markysparkytoys.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-voltage STEM toy brand that runs on primary-color jolts — #d20000 (a stop-sign red that appears on every add-to-cart button, sale badge, and "Shop Now" CTA), #2b00ff (a saturated electric blue used for secondary actions and product-category headers), and #ffb036 (a warm marigold reserved for star ratings, highlight badges, and price flashes). The brand treats its white canvas (#f9f9f9) as a clean lab bench where products sit in crisp, shadowless product cards with {rounded.sm} corners, letting the toy's own saturated packaging do the visual work. Typography runs Poppins at 600 weight for headings and Open Sans at 400 for body — a rationalist pairing that reads as educational rather than playful, reinforcing the STEM positioning. Navigation is a full-width black bar (#111111) with white links, a pattern borrowed from e-commerce tooling rather than toy brands, signaling utility over whimsy. The footer repeats the black bar with a three-column layout of quick links, customer service, and a newsletter signup field styled as a {rounded.sm} input with a red submit button. Sale badges are pill-shaped {rounded.full} in #d20000 with white text, often paired with a "NEW" badge in #06b608 (a bright green). The brand uses generous section spacing ({spacing.section}) between product grids and category strips, and the search bar sits as a full-width field with a magnifying-glass icon in #006fcf. Despite the toy category, the design language is closer to a utility e-commerce store than a playful children's brand — the red and blue carry all the energy, while the typography and layout stay neutral and functional.

colors:
  primary: "#d20000"
  primary-active: "#b00000"
  primary-disabled: "#f77575"
  ink: "#111111"
  body: "#444444"
  muted: "#777777"
  muted-soft: "#c4c4c4"
  hairline: "#eeeeee"
  hairline-soft: "#f2f2f2"
  canvas: "#f9f9f9"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#2b00ff"
  accent-blue-active: "#1e00cc"
  accent-marigold: "#ffb036"
  accent-green: "#06b608"
  accent-teal: "#1cb5b5"
  accent-orange: "#f48920"
  accent-gold: "#d0a306"
  star-rating: "#ffb036"
  sale-badge: "#d20000"
  new-badge: "#06b608"
  nav-bg: "#111111"
  nav-text: "#ffffff"
  footer-bg: "#111111"
  footer-text: "#c4c4c4"
  search-icon: "#006fcf"
  error-red: "#e55151"
  error-red-soft: "#fff8f8"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', 'Open Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', 'Open Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Poppins', 'Open Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', 'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Poppins', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Poppins', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Poppins', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.accent-blue-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.error-red-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.error-red}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 600
  product-compare-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  new-badge:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-submit:
    backgroundColor: "{colors.search-icon}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 48px
    width: 48px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    padding: "{spacing.md} 0"
  category-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
  category-link-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.nav-text}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.footer-text}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.nav-text}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 56px
  section-heading:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  error-message:
    backgroundColor: "{colors.error-red-soft}"
    textColor: "{colors.error-red}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.error-red}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in #d20000 with white text and {rounded.sm} corners. Used for "Add to Cart", "Shop Now", and primary checkout actions. On hover, shifts to `button-primary-active` (#b00000). Disabled state uses `button-primary-disabled` (#f77575) with reduced opacity.

**`button-secondary`** — Electric blue (#2b00ff) alternative for secondary actions like "View Details" or "Learn More". Follows the same sizing and radius as the primary button. Active state darkens to #1e00cc.

**`button-outline`** — A bordered variant with transparent background, #111111 text, and a 2px #eeeeee border. Used for "Cancel" or "Clear" actions in filters and forms. Maintains the same 48px height and {rounded.sm} radius.

**`button-sm`** — Compact version of the primary button at 36px height, used for inline actions like "Quick Add" on product cards or pagination controls. Uses {typography.button-sm} at 14px.

**`button-pill`** — Fully rounded variant ({rounded.full}) used sparingly for promotional badges or "Subscribe" CTAs in the newsletter section. Same compact 36px height as `button-sm`.

### Navigation
**`nav-bar`** — Full-width black (#111111) bar at 64px height with white uppercase nav links. Contains the brand logo on the left, primary navigation links in the center, and utility icons (search, account, cart) on the right. Active link state shows a 2px red underline.

**`nav-link-active`** — White text with a 2px solid #d20000 bottom border. Uppercase Poppins 600 at 14px with 0.3px letter-spacing.

**`nav-link-inactive`** — Muted gray (#c4c4c4) text with no underline. Hover transitions to white.

**`category-strip`** — A horizontal scrollable strip of category links below the nav bar on product listing pages. Links are styled as `category-link` with {rounded.sm} padding. Active category uses `category-link-active` with red background and white text.

### Cards
**`product-card`** — White card with {rounded.sm} corners and 16px padding. Contains product image, title, price (with optional compare-at price), and badges. On hover, elevates with a subtle box-shadow (0 4px 12px rgba(0,0,0,0.08)). No border — relies on the white canvas (#f9f9f9) for separation.

**`product-title`** — Uses {typography.title-sm} (Poppins 600 at 16px) in #111111. Truncates to two lines on product grid cards.

**`product-price`** — Red (#d20000) at {typography.body-md} weight 600. Compare-at prices use `product-compare-price` with line-through and muted gray (#777777).

**`sale-badge`** — Pill-shaped badge in #d20000 with white uppercase text at 11px. Positioned top-left on product images. Padding is 2px 8px.

**`new-badge`** — Same pill shape as sale badge but in bright green (#06b608). Used for newly added products.

**`star-rating`** — Marigold (#ffb036) stars at 16px. Rendered as filled and empty star icons. No numeric rating displayed — purely visual.

### Forms
**`text-input`** — White background with 1px #eeeeee border, 48px height, 12px 16px padding, and {rounded.sm} corners. Uses {typography.body-md} (Open Sans 400 at 16px). Focus state (`text-input-focus`) switches to a 2px #d20000 border. Error state (`text-input-error`) uses a pink-tinted background (#fff8f8) with a 2px #e55151 border.

**`search-bar`** — Full-width input field with a magnifying glass icon (#006fcf) positioned on the left or as a separate submit button (`search-submit`). The input itself is white with 1px #eeeeee border and {rounded.sm} corners. The submit button is a 48px square in #006fcf with white icon.

**`newsletter-input`** — Slightly shorter input at 44px height, used in the footer. Paired with `newsletter-submit` — a red button at the same height.

### Footer
**`footer`** — Full-width black (#111111) section with {spacing.xxl} vertical padding. Three-column layout: quick links, customer service, and newsletter signup. Footer headings use `footer-heading` (Poppins 600 at 16px in white). Links use `footer-link` (Open Sans 400 at 14px in #c4c4c4) with hover to white.

### Hero
**`hero-section`** — Full-width section on the homepage with {spacing.section} padding. Contains `hero-heading` (36px Poppins 600), `hero-subheading` (16px Open Sans 400), and `hero-cta` (a large 56px red button with 18px Poppins 600 text).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns). Nav collapses to hamburger menu. Category strip becomes horizontally scrollable. Footer stacks to single column. Hero heading reduces to 28px. |
| Tablet | 744–1128px | Two-column product grid. Nav links remain visible but condensed. Category strip shows 4-5 visible links with scroll. Footer shows two columns. |
| Desktop | 1128–1440px | Three-column product grid. Full nav with all links visible. Category strip shows all links. Footer shows three columns. Hero at full size. |
| Wide | > 1440px | Four-column product grid on category pages. Max-width container at 1440px centered. Additional whitespace on sides. |

### Touch Targets
- All buttons and interactive elements minimum 44px height (48px preferred)
- Nav links on mobile: minimum 48px tap target
- Category strip links: minimum 44px tap target
- Product card CTAs: minimum 44px height
- Search bar submit: 48px square
- Newsletter submit: 44px height

### Collapsing Strategy
- **Mobile (< 744px):** Navigation collapses to hamburger icon. Category strip scrolls horizontally with no visible overflow. Product grid collapses to single column. Footer stacks vertically. Hero section reduces padding to {spacing.xl}.
- **Tablet (744–1128px):** Navigation remains expanded but secondary links may collapse into a "More" dropdown. Product grid shows 2 columns. Footer shows 2 columns.
- **Desktop (1128–1440px):** Full layout. Navigation shows all primary links. Product grid shows 3 columns. Footer shows 3 columns.
- **Wide (> 1440px):** Content constrained to max-width 1440px. Product grid expands to 4 columns. Additional whitespace on sides.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states:** Only primary button hover (#b00000) and product card shadow were reliably extracted. Secondary button hover, link hover colors, and category strip hover states are inferred from common patterns.
- **Focus states:** No focus ring styles were extracted. Assumed 2px solid #d20000 outline on all interactive elements.
- **Error states:** Error input styling (#fff8f8 background with #e55151 border) was extracted from one instance. No form validation text styles, success states, or warning states were found.
- **Dark mode:** No dark mode implementation detected. All extracted colors assume light mode.
- **Typography scale:** Font sizes for display-xl (36px) and hero are inferred from common e-commerce patterns. Only Poppins and Open Sans were reliably extracted; exact sizes and weights are best estimates.
- **Spacing scale:** Section spacing (64px) and component padding are inferred from typical Shopify STEM toy store layouts. Exact values may vary.
- **Color usage:** The extracted palette includes many colors that may be Shopify widget defaults (#006fcf for search icon, #1cb5b5 for Afterpay, #06b608 for Klarna). The brand's true primary is #d20000 (red) based on its consistent use across CTAs and badges. Secondary is #2b00ff (blue). Accent colors (#ffb036 marigold, #06b608 green) appear on badges and ratings.
- **Font loading:** Poppins and Open Sans are likely loaded via Google Fonts. Exact font weights (400, 600) are inferred. Variable font support is unknown.
- **Component states:** Disabled button styling (#f77575) was extracted from one instance. No disabled input, disabled link, or loading state styles were found.
- **Border radius:** All extracted corners appear to use {rounded.sm} (8px). No instances of {rounded.md} or {rounded.lg} were found in the extracted data.
- **Animation/transition:** No transition durations, easing functions, or animation styles were extracted. Assumed 200ms ease-in-out for hover states.
- **Iconography:** Search icon color (#006fcf) was extracted. No other icon colors or styles were found. Social media icons in footer are likely brand-colored defaults.
- **Checkout flow:** Shopify checkout styling was not extracted. Colors like #1cb5b5 (teal) and #06b608 (green) may belong to payment widgets rather than the brand.
