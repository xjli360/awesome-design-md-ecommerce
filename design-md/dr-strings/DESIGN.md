---
version: alpha
name: "DR Strings"
source_url: "https://www.drstrings.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A high-voltage blue (#116dff) cuts across a near-black (#080808) and warm gray (#5f6360) stage, making every CTA, product-highlight badge, and navigation accent feel like a live-wire signal against the dark. The brand lives in the tension between industrial precision and musical resonance — the hex palette is lean, with no pastels or soft gradients, only a stark ink-to-canvas contrast that mirrors the clarity of a fresh set of strings. Typography runs Arial and Helvetica at sensible sizes, with Japanese fallbacks (hiragino kaku gothic pro, meiryo) indicating a global audience; there is no proprietary typeface, no decorative weight, just clean legibility at 14–16px body and 20–24px headings. Cards and buttons use a moderate {rounded.sm} (8px) — enough to soften the edge without losing the precision feel — while the primary blue button sits at 48px height with white text, a confident call to action against the dark canvas. The product grid is the heart of the site: each string set presented on a white card with the blue accent used sparingly for price or "NEW" badges, letting the product photography (coils of nickel and steel) carry the texture. The nav bar stays fixed, dark, and compact, with the brand wordmark in white and the blue accent reserved for the cart icon and search trigger. There is no decorative flourish — every design decision serves the signal-to-noise ratio, as if the interface itself were a well-tuned instrument.

colors:
  primary: "#116dff"
  primary-active: "#0a4fbf"
  primary-disabled: "#7baaff"
  ink: "#080808"
  body: "#5f6360"
  muted: "#8a8f8d"
  muted-soft: "#b0b5b3"
  hairline: "#d1d5d3"
  hairline-soft: "#e5e8e6"
  canvas: "#ffffff"
  surface-soft: "#f5f6f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  badge-new: "#116dff"
  badge-sale: "#e63946"
  star-rating: "#f4c542"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, 'Hiragino Kaku Gothic Pro', 'Meiryo', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, Helvetica, 'Hiragino Kaku Gothic Pro', 'Meiryo', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arial, Helvetica, 'Hiragino Kaku Gothic Pro', 'Meiryo', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, 'Hiragino Kaku Gothic Pro', 'Meiryo', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, 'Hiragino Kaku Gothic Pro', 'Meiryo', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, 'Hiragino Kaku Gothic Pro', 'Meiryo', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, 'Hiragino Kaku Gothic Pro', 'Meiryo', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, 'Hiragino Kaku Gothic Pro', 'Meiryo', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Helvetica, 'Hiragino Kaku Gothic Pro', 'Meiryo', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, 'Hiragino Kaku Gothic Pro', 'Meiryo', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, 'Hiragino Kaku Gothic Pro', 'Meiryo', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, Helvetica, 'Hiragino Kaku Gothic Pro', 'Meiryo', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "Arial, Helvetica, 'Hiragino Kaku Gothic Pro', 'Meiryo', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, 'Hiragino Kaku Gothic Pro', 'Meiryo', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px

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
    padding: 14px 24px
    height: 48px
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
    padding: 13px 23px
    height: 48px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  search-icon:
    textColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
  hero-heading:
    typography: "{typography.display-xl}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
  category-tab-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  rating-stars:
    color: "{colors.star-rating}"
  cart-icon:
    textColor: "{colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px

## Components

### Buttons
**`button-primary`** — The primary call to action across the site, used for "Add to Cart", "Shop Now", and checkout triggers. Rendered in the brand's high-voltage blue (#116dff) with white text, an 8px radius, and 48px height for a confident, tappable presence. On hover, it deepens to `{colors.primary-active}` (#0a4fbf); disabled state uses `{colors.primary-disabled}` (#7baaff) with reduced opacity.

**`button-secondary`** — A white button with dark text, used for secondary actions like "View Details" or "Learn More". Maintains the same 48px height and 8px radius as the primary, with a 1px hairline border for definition on light backgrounds.

**`button-secondary-outline`** — A transparent button with a blue text label and blue border, used for "Compare" or "Save for Later" actions. The outline treatment keeps the interface clean while maintaining the brand's blue signal.

**`button-pill-primary`** — A compact, fully rounded variant used for filter tags, "NEW" badges on navigation items, and quick-add actions. Smaller padding (10px 20px) and smaller type (`{typography.button-sm}`) allow it to sit inline with text or in tight UI clusters.

### Navigation
**`nav-bar`** — A fixed, dark (`{colors.ink}`) bar at 64px height, carrying the brand wordmark in white and navigation links in `{typography.nav-link}`. The cart icon and search trigger are rendered in `{colors.primary}` blue, creating a subtle but persistent brand signal at the top of every page. Active nav links shift to blue text.

**`nav-link-active`** — The active state for navigation items, switching text color from white to `{colors.primary}` to indicate the current section.

### Cards
**`product-card`** — The primary content container for the product grid, a white card with an 8px radius (`{rounded.sm}`). The product image sits at the top with matching radius, followed by the title in `{typography.title-sm}`, a truncated description in `{typography.body-sm}`, and the price in `{typography.body-md}`. Badges (NEW, SALE) overlay the top-left corner of the image.

**`product-card-image`** — The product photo area within a card, using the same 8px radius as the card itself for visual continuity.

### Badges
**`badge-new`** — A compact, uppercase label in `{colors.primary}` blue with white text, used to flag newly released string sets. Rendered at 11px with 0.5px letter spacing for a tight, technical feel.

**`badge-sale`** — A red (#e63946) variant of the badge, used for promotional pricing or clearance items. Maintains the same typography and padding as the new badge.

### Forms
**`text-input`** — A standard text input field at 48px height with 8px radius, white background, and dark text. On focus, the border shifts to `{colors.primary}` blue, providing a clear active state. Used for search, newsletter signup, and account forms.

### Search
**`search-bar`** — A pill-shaped search input (`{rounded.full}`) at 44px height, with a blue search icon on the left. The rounded shape contrasts with the more angular buttons and cards, giving the search action a distinct, friendly identity.

### Footer
**`footer`** — A dark (`{colors.ink}`) footer section containing links, legal text, and social icons. Links render in `{colors.muted-soft}` and shift to `{colors.primary}` blue on hover, maintaining the brand's signal-on-dark pattern.

### Hero
**`hero-section`** — A full-width dark section (`{colors.ink}`) used for homepage hero banners and category headers. The heading uses `{typography.display-xl}` in white, with a subheading in `{colors.muted-soft}` for secondary text.

### Category Strip
**`category-strip`** — A horizontal scrollable strip of category links (e.g., "Electric", "Acoustic", "Bass") rendered in `{typography.button-sm}`. The active category is underlined with a 2px blue border (`{colors.primary}`).

### Rating
**`rating-stars`** — A five-star rating display using a warm gold (#f4c542) for filled stars, rendered inline with product cards and review sections.

### Cart
**`cart-icon`** — A shopping cart icon rendered in `{colors.primary}` blue, positioned in the top nav bar. The blue treatment ensures the cart is immediately visible against the dark nav background.

### Quantity Selector
**`quantity-selector`** — A compact control for adjusting product quantities on the cart and product detail pages. Uses a soft gray background (`{colors.surface-soft}`) with dark text and 8px radius, with plus/minus buttons flanking the numeric value.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text stacks; category strip becomes swipeable; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains side-by-side layout; search bar remains in nav |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; hero full-width with large imagery; search bar in nav with expanded width |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero content constrained to 1200px; search bar expands to 400px |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Product card tap targets (title, price, image) are each independently tappable with minimum 48px height
- Category strip items have 48px minimum touch area, even when text is smaller
- Quantity selector plus/minus buttons are 44px × 44px minimum
- Nav hamburger icon (mobile) is 48px × 48px

### Collapsing Strategy
- Product grid collapses from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- Navigation links collapse into hamburger menu at < 744px; the brand wordmark and cart icon remain visible
- Category strip collapses from horizontal scroll (all breakpoints) to a dropdown selector on mobile
- Hero section collapses from side-by-side image + text to stacked layout on mobile
- Footer links collapse from multi-column layout to single-column stacked list on mobile
- Search bar collapses from inline nav element to full-width overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted color palette is sparse (only 3 colors from live site HTML+CSS); the brand's true secondary palette (e.g., product-specific accent colors, gauge color coding) could not be reliably determined
- No meta theme-color was found; mobile browser chrome color is unknown
- Font-family declarations are generic (Arial, Helvetica, Japanese fallbacks); no proprietary or custom typeface was detected — the brand may use a web font that was not captured in the extraction
- Hover, focus, and active states for most components (beyond buttons) are inferred from common patterns rather than extracted from live CSS
- Error states for forms (validation, error messages) were not observed
- Dark mode preferences or implementations are unknown
- Sub-brand or product-line-specific palettes (e.g., "DR Hi-Beam", "DR Pure Blues") may exist but were not extracted
- Spacing values are based on common e-commerce patterns rather than extracted from live site measurements
- The extracted blue (#116dff) is a distinctive accent but may not be the brand's only primary; the gray (#5f6360) and near-black (#080808) suggest a dark theme preference that may vary by page section
