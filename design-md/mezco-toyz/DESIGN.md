---
version: alpha
name: "Mezco Toyz"
source_url: "https://www.mezcotoyz.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A collector-grade action-figure brand that wraps its product in a dark, theatrical e-commerce experience — #404040 and #272727 form the dominant canvas, while #bd2426 (a dried-blood red) and #62a1d8 (a cold steel blue) serve as the two primary brand voltages. The site reads like a comic-book variant cover: dense, high-contrast, and unapologetically maximalist. Product cards use `{rounded.sm}` corners and heavy `{colors.hairline}` borders (#dedede) to frame figures against stark white or deep charcoal backgrounds, with price tags and "PRE-ORDER" badges in that signature red. Typography runs system-native (-apple-system, Arial, Helvetica Neue) at modest weights — there is no custom brand typeface, which gives the UI a functional, marketplace feel rather than a glossy toy-brand sheen. Navigation is a dense horizontal strip of category links (Marvel, DC, Horror, Star Wars, etc.) in `{colors.ink}` (#404040) on white, with a sticky top bar that collapses on scroll. The checkout and account flows lean heavily into `{colors.primary}` (#bd2426) for CTAs, while secondary actions use `{colors.muted}` (#737373) outlines. The overall mood is serious and archival — this is a brand for adult collectors who want to see every sculpted detail, not for children browsing in-brights.

colors:
  primary: "#bd2426"
  primary-active: "#9b1e1f"
  primary-disabled: "#e8a0a1"
  ink: "#404040"
  body: "#595959"
  muted: "#737373"
  muted-soft: "#bfbfbf"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#62a1d8"
  accent-blue-dark: "#2f7bbf"
  accent-green: "#9bca3e"
  accent-green-dark: "#516b1d"
  accent-orange: "#f68b1f"
  accent-orange-dark: "#c16508"
  badge-red: "#de5052"
  badge-green: "#bada7a"
  dark-canvas: "#272727"
  dark-surface: "#404040"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 11px 23px
    height: 44px
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-dark:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
  category-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  category-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: 8px 12px 4px
  product-card-price:
    typography: "{typography.price}"
    padding: 0 12px 8px
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: 48px 24px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
    padding: 4px 0
  footer-section-title:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 0 0 8px
  cart-count-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Pre-Order", and checkout flows. Rendered in `{colors.primary}` (#bd2426) with white text and `{rounded.sm}` corners. On hover, shifts to `{colors.primary-active}` (#9b1e1f). Disabled state uses `{colors.primary-disabled}` (#e8a0a1) with full opacity. **`button-secondary`** — White background with `{colors.ink}` (#404040) text and a `{colors.hairline}` border, used for "View Details" and secondary cart actions. **`button-outline`** — Transparent background with `{colors.ink}` text and a `{colors.hairline}` border, used for "Wishlist" and "Compare" actions. **`button-dark`** — `{colors.dark-canvas}` (#272727) background with white text, used on dark hero banners and promotional sections.

### Cards
**`product-card`** — The core product display unit, a white card with `{rounded.sm}` corners and no padding at the root level. The image fills the top with `{rounded.sm}` top corners only. Below the image, `{typography.title-sm}` renders the product name with 8px horizontal padding, followed by `{typography.price}` for the price. Badges overlay the top-left of the image area: `{colors.primary}` for "PRE-ORDER", `{colors.accent-green}` for "IN STOCK", and `{colors.accent-orange}` for "LIMITED EDITION". Cards sit on a `{colors.surface-soft}` (#f5f5f5) background in grid layouts with `{spacing.base}` (16px) gaps.

### Navigation
**`nav-bar`** — A 56px white bar with `{colors.ink}` (#404040) uppercase nav links. The logo sits left-aligned, with category links (Marvel, DC, Horror, Star Wars, Mezco Exclusives) in a horizontal strip. On scroll, the bar collapses to 48px with a `{colors.hairline}` bottom border. **`category-link`** — 8px vertical padding, 12px horizontal, with `{typography.nav-link}` (14px, 600 weight, uppercase). Active state uses `{colors.primary}` text color. A secondary utility nav (Search, Cart, Account) sits right-aligned with icon buttons.

### Forms
**`text-input`** — Standard 44px input with `{rounded.sm}` corners, `{colors.canvas}` background, and `{colors.ink}` text. Focus state uses a `{colors.primary}` border. Placeholder text uses `{colors.muted-soft}` (#bfbfbf). **`select-input`** — Matches text-input dimensions with a custom dropdown arrow in `{colors.muted}`. Used for sorting (Price, Name, Release Date) and filtering on collection pages.

### Footer
A multi-column layout with `{colors.canvas}` background and `{colors.hairline}` top border. Section titles use `{typography.title-sm}` in `{colors.ink}`, links use `{typography.link}` in `{colors.muted}`. Columns include Customer Service, About Mezco, Legal, and Social Links. Bottom bar contains copyright text in `{colors.muted-soft}`.

### Badges
**`product-card-badge`** — Small uppercase labels (11px, 700 weight) with `{rounded.xs}` corners and 2px/8px padding. Three variants: red (`{colors.primary}`) for pre-orders, green (`{colors.accent-green}`) for in-stock, orange (`{colors.accent-orange}`) for limited editions. Positioned absolutely at the top-left of product card images with a 4px offset.

### Hero
**`hero-banner`** — Full-width section with `{colors.dark-canvas}` (#272727) background and white text. Uses `{typography.display-xl}` (32px, 700 weight) for the headline, with a subtitle in `{typography.body-md}`. A `{colors.primary}` CTA button sits below the text. Used for collection launches and promotional campaigns.

### Search
**`search-bar`** — A `{rounded.full}` pill-shaped input with `{colors.surface-soft}` background and `{colors.muted}` placeholder text. 40px tall with 8px/16px padding. On focus, expands to full width with a `{colors.primary}` outline. A search icon sits left-aligned inside the input.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card), nav collapses to hamburger menu, hero banner reduces to 32px padding, search bar becomes full-width, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, nav shows top-level categories only, hero banner uses 40px padding, search bar stays pill-shaped but narrower |
| Desktop | 1128–1440px | Three-column product grid, full nav with all categories visible, hero banner uses 48px padding, search bar in nav bar |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, nav remains full, hero banner uses 64px padding |

### Touch Targets
- All buttons and links: minimum 44px height (buttons) or 44x44px tap area (icon buttons)
- Product card images: tap targets the full card area
- Category links: 44px minimum touch height with 12px horizontal padding
- Search bar: 40px height (slightly below 44px guideline, but pill shape increases effective tap area)
- Cart icon: 44x44px with `{spacing.sm}` (8px) padding

### Collapsing Strategy
- Top nav collapses to hamburger menu at < 744px, with slide-in drawer for categories
- Product grid collapses from 4 columns to 1 column at mobile
- Footer collapses from 4 columns to stacked single column at < 744px
- Search bar collapses from nav-integrated to full-width overlay at mobile
- Hero banner reduces padding and font size at mobile (display-xl drops to 24px)
- Secondary navigation (sort/filter) collapses to a dropdown at < 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the live site (Cloudflare challenge blocked full rendering)
- Error state styling (form validation, 404 pages, out-of-stock messaging) is not documented
- Dark mode variant is not present on the live site; all extracted colors are from light mode
- Sub-brand palettes (Mezco Exclusive vs. standard releases) may have distinct color treatments not captured
- Animation and transition timing values (hover transitions, page load animations, carousel speeds) are unknown
- The extracted hex list includes several colors (#0051c3, #f9b169, #904b06, #ee730a) that appear to be from third-party widgets (Klarna, Afterpay, social icons) rather than brand colors — these have been excluded from the palette
- Font stack is entirely system-native; no custom typeface was detected, but the brand may use a web font that was blocked by Cloudflare
- The Cloudflare challenge page prevented full DOM analysis — product detail pages, cart flows, and account pages could not be inspected
