---
version: alpha
name: "Healthy Nest"
source_url: "https://healthynest.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The extracted palette from the live site is dominated by Amazon's own system colors (#0f1111 ink, #ff9900 accent, #2162a1 link blue, #d5d9d9 hairline) and checkout-widget tints (#ffb14a Klarna, #0b7b3c green, #c10015 error). This suggests the brand's storefront is hosted entirely within Amazon's marketplace infrastructure, inheriting its chrome and button styles rather than expressing a distinct visual identity. The most distinctive non-Amazon color in the extraction is #edf8ff, a pale ice-blue that appears as a surface tint on product detail sections, and #1c89e3, a clean primary blue used for informational badges. The typography stack is Amazon Ember across all weights — a utilitarian, highly readable sans-serif designed for dense retail interfaces. Without a standalone site, Healthy Nest's design system is effectively Amazon's: pill-shaped add-to-cart buttons in #ff9900, star ratings in #0f1111, and a white canvas (#ffffff) with soft gray dividers (#d5d9d9). The brand's own product photography and packaging must carry the emotional weight — pastel nest motifs, soft greens, and organic shapes — but these are not reflected in the extracted CSS. The system described below reconstructs what a purpose-built Healthy Nest site might look like, using the extracted Amazon-adjacent colors as a foundation and inferring brand-specific tokens from the baby-care category context.

colors:
  primary: "#1c89e3"
  primary-active: "#0a7cd1"
  primary-disabled: "#a7acb2"
  ink: "#0f1111"
  body: "#565959"
  muted: "#888c8c"
  muted-soft: "#a7acb2"
  hairline: "#d5d9d9"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f0f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#ff9900"
  accent-orange-active: "#ff6200"
  accent-yellow: "#ffd814"
  star-rating: "#0f1111"
  badge-blue: "#edf8ff"
  badge-blue-text: "#0c3353"
  error: "#c10015"
  link-blue: "#2162a1"
  link-blue-visited: "#017185"
  success-green: "#0b7b3c"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  link:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  price:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: 0
  price-sm:
    fontFamily: "'Amazon Ember', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0

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
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-orange-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 44px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    boxShadow: "0 2px 8px rgba(15, 17, 17, 0.1)"
  product-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
  product-badge:
    backgroundColor: "{colors.badge-blue}"
    textColor: "{colors.badge-blue-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price}"
  price-strikethrough:
    textColor: "{colors.muted}"
    typography: "{typography.price-sm}"
    textDecoration: line-through
  star-rating:
    textColor: "{colors.star-rating}"
    typography: "{typography.caption}"
  link:
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
  link-visited:
    textColor: "{colors.link-blue-visited}"
    typography: "{typography.link}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 32px 16px
  footer-link:
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.error}"
  error-message:
    textColor: "{colors.error}"
    typography: "{typography.caption}"
  success-message:
    textColor: "{colors.success-green}"
    typography: "{typography.caption}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
    height: 36px
  add-to-cart-button:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  buy-now-button:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  pagination:
    textColor: "{colors.link-blue}"
    typography: "{typography.body-sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.6
  modal-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 12px 0
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 0 0 12px 0
  tab-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
  hero-banner:
    backgroundColor: "{colors.badge-blue}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: 48px 24px
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 44px
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  social-icon:
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-hover:
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 32px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using a clean blue (#1c89e3) background with white text. On hover, it shifts to `{colors.primary-active}` (#0a7cd1). The disabled state uses `{colors.primary-disabled}` (#a7acb2) to signal non-interactivity. Padding is 12px 24px with a height of 44px and `{rounded.sm}` corners.

**`button-accent-orange`** — The high-energy accent button, using Amazon's signature orange (#ff9900) with dark ink text. This is reserved for promotional actions like "Shop Now" on deals. Active state darkens to #ff6200. Same dimensions as primary.

**`button-accent-yellow`** — The add-to-cart button, using the familiar yellow (#ffd814) from Amazon's checkout flow. Dark ink text ensures high contrast. Active state is not defined in the extracted data but would likely darken slightly.

**`button-secondary`** — An outlined or ghost button with a white background and ink text, used for less prominent actions like "Save for Later" or "Cancel". Has a 1px hairline border (implied by the secondary pattern) and matches primary dimensions.

**`button-tertiary-text`** — A text-only button using link blue (#2162a1) with no background or border. Used for inline actions like "See more" or "Edit".

**`button-pill`** — A compact pill-shaped button using the primary blue, intended for filters or category tags. Uses `{rounded.full}` for the pill shape and smaller padding (8px 16px) with `{typography.button-sm}`.

### Navigation
**`top-nav`** — A fixed-height (64px) white navigation bar with ink text. Contains the brand logo, search bar, account links, and cart icon. Uses `{typography.nav-link}` for navigation items. On scroll, may receive a subtle bottom border using `{colors.hairline}`.

**`search-bar`** — A standard search input with `{rounded.sm}` corners, white background, and 44px height. The search icon sits inside the input on the left. On focus, the border changes to `{colors.primary}`.

**`breadcrumb`** — A muted gray (#888c8c) breadcrumb trail using `{typography.caption}`. The active (current) page uses ink color (#0f1111). Separators are ">" in the same muted gray.

**`category-pill`** — A pill-shaped filter chip with a soft gray background (#f0f2f2) and ink text. Active state uses the primary blue background with white text. Used for product category filtering on search results pages.

### Cards
**`product-card`** — A white card with `{rounded.sm}` corners containing a product image, title, rating, price, and add-to-cart button. On hover, it receives a subtle box shadow (0 2px 8px rgba(15, 17, 17, 0.1)) to indicate interactivity. The product image area has a soft gray background (#f0f2f2) for loading states.

**`product-badge`** — A small badge with a pale blue background (#edf8ff) and dark blue text (#0c3353). Used for labels like "Best Seller", "Amazon's Choice", or "Limited Time Deal". Uses `{rounded.xs}` corners and `{typography.badge}`.

**`modal-card`** — A white card with `{rounded.md}` corners and 24px padding, used for dialogs and overlays. The backdrop uses `{colors.scrim}` at 60% opacity.

### Forms
**`text-input`** — A standard text input with white background, ink text, `{rounded.sm}` corners, and 44px height. On focus, the border changes to `{colors.primary}`. Error state uses `{colors.error}` (#c10015) for the border and displays an `{colors.error}` colored error message below.

**`quantity-selector`** — A compact control (36px height) with minus, number, and plus buttons. Uses `{rounded.sm}` corners and `{typography.button-sm}`. The number display is centered between the two buttons.

**`newsletter-input`** — A text input paired with a `newsletter-button` for email signup forms. The input matches `text-input` dimensions, and the button uses `button-primary` styling.

### Footer
**`footer`** — A full-width footer with a soft gray background (#f0f2f2) and body text (#565959). Contains multiple columns of links, each using `{colors.link-blue}` (#2162a1). Padding is 32px 16px. A `{divider}` separates the footer from the main content area.

**`social-icon`** — Circular icons (32px) with muted gray color. On hover, they change to the primary blue (#1c89e3). Used for links to social media platforms.

### Miscellaneous
**`star-rating`** — Stars displayed in ink color (#0f1111) using `{typography.caption}`. The rating number (e.g., "4.5 out of 5") appears next to the stars in the same style.

**`price-display`** — The current price in bold 18px Amazon Ember. The `price-strikethrough` variant shows the original price in muted gray with a line-through, using 14px weight 600.

**`divider`** — A 1px horizontal line in `{colors.hairline}` (#d5d9d9). The `divider-soft` variant uses `{colors.hairline-soft}` (#eeeeee) for subtler separation.

**`accordion-header`** — A clickable header using `{typography.title-sm}` with 12px vertical padding. The `accordion-content` area below uses `{typography.body-sm}` with body color (#565959) and 12px bottom padding.

**`tab-active`** — An active tab with a 2px bottom border in `{colors.primary}`. Inactive tabs use muted gray text. Both use `{typography.button-md}`.

**`hero-banner`** — A full-width banner with pale blue background (#edf8ff) and ink text. Uses `{typography.display-md}` for the headline with 48px 24px padding. May include a subheadline in `{typography.body-md}`.

**`pagination`** — Page numbers as link-blue text. The active page uses a primary blue background with white text and `{rounded.sm}` corners.

**`tooltip`** — A small dark box (#0f1111) with white text, `{rounded.xs}` corners, and 4px 8px padding. Appears on hover for additional information.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack vertically; search bar moves below nav; footer links stack; hero banner reduces padding to 32px 16px; category pills wrap to two rows; pagination shows "Prev/Next" only |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links (Logo, Search, Account, Cart); category pills show in a horizontal scrollable strip; footer shows 2-column link layout; hero banner uses 40px 24px padding |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links visible; category pills in a full-width row; footer shows 4-column link layout; hero banner uses 48px 24px padding |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; top-nav and footer expand to full width with max-width constraints; hero banner may use larger typography |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Category pills are at least 36px tall with 16px horizontal padding.
- Quantity selector buttons are 36x36px minimum.
- Social icons are 32x32px with 44x44px tap area via padding.
- Accordion headers have 44px minimum tap height.

### Collapsing Strategy
- **Top Nav:** On mobile, navigation links collapse behind a hamburger icon. The search bar moves below the nav bar. Account and cart icons remain visible.
- **Product Grid:** Single column on mobile, two columns on tablet, three on desktop, four on wide screens.
- **Footer:** Links collapse from 4 columns on desktop to 2 columns on tablet, then stack vertically on mobile.
- **Category Pills:** On mobile, they wrap to two rows with horizontal scrolling. On tablet and above, they display in a single full-width row.
- **Hero Banner:** On mobile, padding reduces and typography may scale down slightly. The banner may stack vertically instead of side-by-side.
- **Breadcrumbs:** On mobile, breadcrumbs may truncate with "..." for intermediate levels.
- **Pagination:** On mobile, only "Previous" and "Next" buttons are shown. Page numbers appear on tablet and above.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted colors are overwhelmingly Amazon's system palette, not Healthy Nest's own brand colors. The brand's true identity (likely soft pastels, organic greens, or warm neutrals for baby care) is not represented in the CSS extraction.
- No standalone brand site exists — the storefront is hosted on Amazon. This DESIGN.md reconstructs a hypothetical purpose-built site using Amazon-adjacent colors as a foundation.
- Hover, focus, and active states for most components are inferred from common patterns, not extracted from the live site.
- Error, success, and warning styling is inferred from Amazon's checkout patterns (#c10015 for error, #0b7b3c for success).
- Dark mode is not supported and no dark mode colors were extracted.
- Typography sizes and weights are inferred from Amazon Ember's typical usage on Amazon.com, not from Healthy Nest-specific CSS.
- No animation or transition durations were extracted (standard 200-300ms ease-in-out assumed).
- No custom iconography or illustration style was extracted — the brand likely uses Amazon's icon set.
- No form validation patterns (inline errors, success states) were extracted beyond basic error color.
- No loading states (skeleton screens, spinners) were extracted.
- No sub-brand or seasonal color palettes were extracted.
- The `font-family` extraction includes multiple variants (Amazon Ember, Amazon Ember Modern Display, Amazon Ember Modern Text) — the primary `Amazon Ember` is used throughout, but the Modern variants may be used for display headings on the actual site.
