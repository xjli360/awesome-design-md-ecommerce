---
version: alpha
name: "Case-Mate"
source_url: "https://www.case-mate.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A glossy, confident accessories brand that lives in the tension between #0d0d0d ink and a signature #c24d74 rose-mauve — a color that reads neither pink nor beige but something distinctly Case-Mate, appearing on product-detail swatches, add-to-cart buttons, and the brand’s own jelly-tote hero imagery. The palette is overwhelmingly near-white (#f5f5f5, #eeeeee, #f2f2f2) with a secondary accent of #d93f4c (a punchier red-coral) and a deep #9c305d plum for sale badges and limited-edition markers. Typography layers two distinct voices: Scotch Display (a condensed, high-contrast serif) for product names and editorial headlines, and Epilogue (a clean, geometric sans) for body copy and navigation — a pairing that signals both fashion credibility and tech-accessory precision. Buttons use {rounded.full} pill shapes in the rose-mauve primary, while product cards adopt a softer {rounded.md} corner that mirrors the rounded silhouette of the brand’s signature phone cases. The Jelly Tote bag — a translucent, candy-colored accessory — drives the visual language: glossy surfaces, soft reflections, and a sense of playful luxury that avoids both minimalism and maximalism. The site’s Shopify backbone means checkout flows inherit platform defaults, but the brand’s own surfaces — from the {colors.surface-soft} category strips to the {colors.hairline} dividers — maintain a consistent, polished neutrality that lets the product photography and those two accent colors do the emotional work.

colors:
  primary: "#c24d74"
  primary-active: "#a83e62"
  primary-disabled: "#e8b3c5"
  ink: "#0d0d0d"
  body: "#333333"
  muted: "#aaaaaa"
  muted-soft: "#cdcdcd"
  hairline: "#d7d7d7"
  hairline-soft: "#e7e7e7"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  accent-coral: "#d93f4c"
  accent-plum: "#9c305d"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale-badge: "#d93f4c"
  star-rating: "#0d0d0d"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Scotch Display', 'Scotch Display Compressed', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Scotch Display', 'Scotch Display Condensed', serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Scotch Display', 'Scotch Display Condensed', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
  button-secondary-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
  button-pill-accent:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-coral}"
  product-card-swatch:
    rounded: "{rounded.full}"
    height: 24px
  sale-badge:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  limited-badge:
    backgroundColor: "{colors.accent-plum}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand’s signature rose-mauve {colors.primary} with white text and a full pill shape. Used for “Add to Cart,” “Shop Now,” and primary checkout actions. On hover, shifts to {colors.primary-active} (#a83e62). Disabled state uses {colors.primary-disabled} (#e8b3c5) with white text, maintaining the pill silhouette.

**`button-secondary`** — A white button with dark text, outlined by a 1px {colors.hairline} stroke. Used for secondary actions like “View Details” or “Continue Shopping.” Hover state fills the background with {colors.surface-soft} (#f5f5f5). The outline variant (`button-secondary-outline`) uses a 1.5px {colors.ink} stroke for higher contrast on light backgrounds.

**`button-pill-accent`** — A smaller, coral-accented pill button using {colors.accent-coral} (#d93f4c). Reserved for sale promotions, limited-time offers, and urgency-driven CTAs. Typography is {typography.button-sm} with tighter padding (10px 20px).

**`icon-button-circle`** — A 40px circular icon button on a {colors.surface-soft} background. Used for wishlist hearts, cart icons, and mobile menu toggles. Hover state darkens the background to {colors.hairline} (#d7d7d7). The outline variant (`icon-button-outline`) uses a white background with a 1px {colors.hairline} stroke.

### Navigation
**`top-nav`** — A fixed 72px white bar with uppercase nav links in {typography.nav-link}. The logo sits left-aligned (typically the Case-Mate wordmark in {colors.ink}), with category links (“Cases,” “Bags,” “Accessories,” “Sale”) centered or right-aligned. Active links use {colors.primary} text; inactive links use {colors.muted}. A search icon and cart icon sit on the far right.

**`nav-link-active`** — Active navigation link styled in {colors.primary} rose-mauve with uppercase {typography.nav-link}. No underline or background — color alone signals the active state.

**`nav-link-inactive`** — Inactive navigation link in {colors.muted} (#aaaaaa). On hover, transitions to {colors.ink} (#0d0d0d).

**`search-bar-pill`** — A pill-shaped search input on a {colors.surface-soft} background. Placeholder text in {colors.muted}. Focus state adds a 1.5px {colors.primary} stroke. The search icon sits inside the left padding.

### Cards
**`product-card`** — A white card with {rounded.md} corners, containing a product image, title, price, and optional swatch dots. The image area uses {colors.surface-soft} as a fallback background before the product photo loads. Cards are typically displayed in a 3–4 column grid on desktop, collapsing to 2 columns on tablet and 1 column on mobile.

**`product-card-title`** — Product name in {typography.title-sm} with {colors.ink} text. Limited to 2 lines with ellipsis overflow.

**`product-card-price`** — Regular price in {typography.body-md} with {colors.ink}. Sale prices use {colors.accent-coral} (#d93f4c) via `product-card-sale-price`.

**`product-card-swatch`** — A 24px circular color swatch dot, using {rounded.full}. Colors are set dynamically per product variant (e.g., rose-mauve, black, white, coral). Active swatch has a 2px {colors.primary} ring.

### Badges
**`sale-badge`** — A small coral badge using {colors.accent-coral} background, white text, and {typography.badge} (11px uppercase). Positioned top-left on product card images. Uses {rounded.sm} for a slightly softened rectangle.

**`limited-badge`** — A plum badge using {colors.accent-plum} (#9c305d) background. Reserved for limited-edition drops and collaborations. Same typography and corner radius as the sale badge but distinct color to signal exclusivity rather than discount.

### Hero
**`hero-section`** — A full-width section with a {colors.surface-soft} background, typically featuring a large product hero image (Jelly Tote bag or flagship phone case) alongside a headline in {typography.display-xl} (Scotch Display serif). The hero CTA button sits below the headline, using `hero-cta` styling. Padding is {spacing.section} (64px) top and bottom, with {spacing.lg} (24px) horizontal.

**`hero-cta`** — A large pill button in {colors.primary} with white text, using {typography.button-md}. Slightly wider padding (14px 32px) than the standard button-primary to match the hero’s scale.

### Category Strip
**`category-strip`** — A horizontal scrollable strip of category tabs (e.g., “Phone Cases,” “Jelly Tote Bags,” “AirPods Cases,” “Sale”). Background is {colors.canvas} with {colors.muted} text for inactive tabs. Active tabs use `category-tab-active` with a {colors.surface-soft} fill and {colors.ink} text, rendered as pills with {rounded.full}.

**`category-tab-active`** — Active category pill with {colors.surface-soft} background and {colors.ink} text. Padding 8px 16px, {rounded.full}.

**`category-tab-inactive`** — Inactive category pill with transparent background and {colors.muted} text. On hover, text transitions to {colors.ink}.

### Footer
**`footer-section`** — A dark footer on {colors.ink} (#0d0d0d) background with white text. Contains columns for “Shop,” “Support,” “About,” and “Connect.” Links use {colors.muted-soft} (#cdcdcd) and turn white on hover. Section headings use `footer-heading` in {typography.title-sm}.

**`footer-link`** — Footer link in {colors.muted-soft} with {typography.link}. Hover state transitions to {colors.canvas} (#ffffff).

**`newsletter-input`** — A white pill input field for email signup, placed in the footer. Uses {rounded.full} with {colors.hairline} stroke. Placeholder text in {colors.muted}. Focus state adds a {colors.primary} stroke.

**`newsletter-submit`** — A rose-mauve pill submit button adjacent to the newsletter input. Uses {colors.primary} background, white text, and {typography.button-sm}. Same height (48px) as the input for visual alignment.

### Accordion
**`accordion-header`** — Used on product detail pages for “Description,” “Shipping & Returns,” and “Care Instructions” sections. Styled in {typography.title-sm} with {colors.ink} text. A plus/minus icon sits on the right. No background — just a bottom {colors.hairline} border.

**`accordion-content`** — Expanded content area below the header, using {typography.body-sm} with {colors.body} (#333333) text. Padding collapses to {spacing.sm} top and {spacing.base} bottom for a clean reveal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top nav collapses to hamburger menu; category strip becomes horizontally scrollable; hero section reduces padding to {spacing.xl} (32px); accordion becomes default layout for all product info |
| Tablet | 744–1128px | Two-column product grid; top nav shows 3–4 category links; hero uses {typography.display-lg} (32px) instead of display-xl; footer columns stack to 2×2 grid |
| Desktop | 1128–1440px | Three-column product grid; full top nav with all categories visible; hero at full scale with {typography.display-xl}; footer in 4-column layout |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) with centered content; hero image scales up but headline stays at {typography.display-xl} |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility.
- Category strip tabs are at least 40px tall with 16px horizontal padding.
- Product card swatches are 24px circles with 8px touch padding around each.
- Search bar and newsletter inputs are 48px tall for comfortable tap targets.
- Icon buttons (wishlist, cart, menu) are 40px circles with 8px internal icon padding.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu at < 744px, with a slide-out drawer from the left.
- Product grid reduces from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Footer column layout collapses from 4 columns (desktop) to 2×2 (tablet) to single column (mobile).
- Hero section reduces vertical padding from 64px to 32px on mobile, and the headline font size drops from 42px to 28px.
- Category strip becomes a horizontally scrollable row on mobile, with no wrapping.
- Product detail accordions are always expanded on desktop (no accordion behavior) but collapse on mobile and tablet.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were inferred from common patterns rather than extracted from the live site. Specific transition durations and easing curves are not documented.
- Error styling for form inputs (newsletter, search) was not extracted. Default to a 1.5px {colors.accent-coral} stroke with {colors.accent-coral} error text.
- Dark mode is not supported and no dark-mode color tokens were extracted.
- The extracted font list includes multiple Scotch Display variants (compressed, condensed, dingbats) — the exact usage of each variant (e.g., dingbats for decorative elements) is unclear from the extraction alone.
- Shopify checkout colors (Shopify Pay, Klarna, Afterpay badges) were filtered out; these may appear on product pages but are not part of the Case-Mate design system.
- Star rating component color was set to {colors.ink} based on the extracted palette, but the live site may use a different color (e.g., {colors.primary} or {colors.accent-coral}).
- The extracted hex list includes many near-white shades (#eeeeee, #f5f5f5, #f2f2f2, #ededed, #f1f1f1) — these were consolidated into {colors.surface-soft} (#f5f5f5) and {colors.hairline-soft} (#e7e7e7), but the exact usage of each shade (e.g., #ededed vs #f1f1f1) could not be precisely mapped.
- No extracted data for loading states, skeleton screens, or empty states.
- The brand’s Jelly Tote bag and other product photography may introduce additional accent colors not captured in the extracted palette.
