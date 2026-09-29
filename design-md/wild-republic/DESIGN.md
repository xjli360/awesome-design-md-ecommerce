---
version: alpha
name: "Wild Republic"
source_url: "https://www.wildrepublic.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A plush-toy ecosystem built on a muted charcoal skeleton (#414145) that lets every animal's personality — the lime beak of a toucan, the orange crest of a cockatiel — pop without competition. The brand's true voltage is a fresh, almost-forest green (#0d944b) that appears on primary buttons, "Add to Cart" calls, and the site's single persistent accent; it reads less like a corporate green and more like the chlorophyll flash of a rainforest canopy. A secondary orange (#f26522) and a warm red (#d23827) handle sale badges and clearance markers, while a deep charcoal (#2d2d2d) and a softer graphite (#4f4f4d) build hierarchy in body text and secondary labels. The canvas is a cool off-white (#f7f7f7) — not pure white — which softens the browsing experience for a catalog of hundreds of plush animals, each photographed on white backgrounds that float against the gray. Rounded corners are restrained: product cards use a gentle {rounded.sm}, buttons use {rounded.md}, and no element goes fully pill-shaped except the search bar, which reads as a friendly invitation. Typography runs system-native (-apple-system, Helvetica Neue, Roboto, sans-serif) at modest weights — no brand-owned typeface, no display-heavy headlines; the animals do the heavy lifting. The nav bar is a charcoal strip (#414145) with white text, a rare dark header in a category that usually favors white navs, and it signals a brand that's confident enough to let its product be the light.

colors:
  primary: "#0d944b"
  primary-active: "#0a7a3d"
  primary-disabled: "#a3d9b5"
  ink: "#2d2d2d"
  body: "#414042"
  muted: "#777777"
  muted-soft: "#a9a9a9"
  hairline: "#dedede"
  hairline-soft: "#eaeaea"
  canvas: "#f7f7f7"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#f26522"
  accent-red: "#d23827"
  accent-purple: "#7f5fca"
  accent-yellow: "#ffcb42"
  accent-lime: "#d7e47c"
  nav-bg: "#414145"
  nav-text: "#ffffff"
  badge-sale: "#d23827"
  badge-new: "#7f5fca"
  star-rating: "#ffcb42"
  footer-bg: "#2d2d2d"
  footer-text: "#b3b3b3"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, 'San Francisco', 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
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
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.muted}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 48px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.surface-card}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
    backgroundColor: "{colors.surface-card}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
    rounded: "{rounded.xs}"
  nav-link-active:
    backgroundColor: "rgba(255,255,255,0.1)"
    textColor: "{colors.nav-text}"
    rounded: "{rounded.xs}"
  nav-link-hover:
    backgroundColor: "rgba(255,255,255,0.08)"
    textColor: "{colors.nav-text}"
    rounded: "{rounded.xs}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
    backgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "12px 32px"
    height: 48px
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  category-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(13,148,75,0.12)"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.surface-card}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "none"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 48px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 24px
    width: 24px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
  breadcrumb-link:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-link-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  pagination-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  pagination-button-disabled:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's forest green (#0d944b) and white text. On hover, it deepens to a darker green (#0a7a3d). The disabled state uses a pale green (#a3d9b5) with white text. All primary buttons use a 12px rounded corner and 48px height for a substantial, clickable presence.
**`button-secondary`** — A white button with a 1px hairline border, used for secondary actions like "View Details" or "Cancel". On hover, the background shifts to a soft gray (#f2f2f2) and the border darkens to muted gray (#777777). Same 48px height and 12px rounded corners as the primary button for visual consistency.
**`button-ghost`** — A text-only button with no background or border, used for inline actions like "Clear filters" or "See more". Hover state adds a subtle background tint (rgba(0,0,0,0.05)).
**`button-pill`** — A compact, fully rounded button used for filter chips and category tags. Uses the primary green on a 36px height with 8px horizontal padding. The outline variant uses a transparent background with a hairline border.
**`button-pill-outline`** — The outline counterpart to the pill button, used for unselected filter states. Transparent background with a 1px hairline border. On selection, it becomes the filled pill.

### Cards
**`product-card`** — A white card with a 1px soft hairline border and 8px rounded corners. Contains a square product image (1:1 aspect ratio, soft gray placeholder background), the product title in 16px semibold, and the price in 16px bold. On hover, the border becomes more visible and a subtle box shadow appears (0 2px 8px rgba(0,0,0,0.08)). Cards are spaced with 16px padding inside.
**`category-card`** — Similar to the product card but used for animal categories (e.g., "Jungle", "Ocean", "Farm"). On hover, the border turns green (#0d944b) and a green-tinted shadow appears, signaling the category is clickable.
**`hero-banner`** — A full-width banner with a soft gray background (#f2f2f2) and large headline text (32px bold). The CTA button sits prominently in the center or bottom-left, using the primary green button style. No rounded corners on the banner itself — it spans edge to edge.

### Navigation
**`nav-bar`** — A dark charcoal strip (#414145) spanning the full viewport width at 64px height. Navigation links are white, uppercase, 14px semibold with 0.5px letter spacing. The active link has a subtle white overlay (10% opacity). The search bar sits on the right side as a white pill with a full border radius.
**`nav-link`** — Uppercase 14px semibold text with 0.5px letter spacing. Active state shows a 10% white overlay background. Hover state shows an 8% white overlay. Links are padded 8px vertically and 12px horizontally.
**`breadcrumb-link`** — Small 12px gray links separated by slashes. The active (current) page is rendered in dark ink (#2d2d2d) without a link. Inactive breadcrumbs are muted gray (#777777).

### Forms
**`text-input`** — A white input field with a 1px hairline border and 8px rounded corners. On focus, the border becomes a 2px green (#0d944b) stroke. Error state uses a red border (#d23827). All inputs are 48px tall with 12px vertical and 16px horizontal padding.
**`select-input`** — Matches the text input styling but includes a dropdown arrow icon. Same height, padding, and border behavior.
**`newsletter-input`** — A white input with no border, used in the footer. Paired with a green submit button. The input and button are the same height (48px) and sit side by side.
**`quantity-selector`** — A compact control with a border, used on product detail pages. Contains a minus button, the quantity number, and a plus button. All three elements are 40px tall with 8px padding.

### Badges
**`badge-sale`** — A small red (#d23827) badge with white uppercase 11px bold text. Used to flag discounted items. 2px vertical and 8px horizontal padding with 4px rounded corners.
**`badge-new`** — A purple (#7f5fca) badge with the same typography and sizing, used for newly added products.
**`badge-out-of-stock`** — A gray (#777777) badge indicating an item is unavailable. Same sizing and typography.

### Footer
**`footer-section`** — A dark (#2d2d2d) section with light gray (#b3b3b3) body text. Links are the same light gray and turn white on hover. The newsletter signup form sits prominently in the footer with a white input and green submit button. The footer uses 64px vertical padding and 24px horizontal padding.

### Miscellaneous
**`star-rating`** — Yellow (#ffcb42) stars at 16px, used on product cards and detail pages. The rating count (e.g., "4.5") sits next to the stars in body text.
**`pagination-button`** — A 36px tall button with 8px horizontal padding. The active page uses the primary green fill; inactive pages are transparent with body text. Disabled buttons use a very light gray (#a9a9a9).
**`loading-spinner`** — A 24px spinning indicator in the primary green, used during product loading and form submissions.
**`tooltip`** — A dark (#2d2d2d) tooltip with white text, 4px rounded corners, and 4px/8px padding. Appears on hover for icon buttons and product features.
**`divider`** — A 1px horizontal line in soft hairline (#eaeaea), used between sections and product details.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items), hamburger nav replaces top links, search bar collapses to icon, footer stacks vertically, hero banner reduces padding to 32px |
| Tablet | 744–1128px | Two-column product grid (3-4 items), nav links visible but truncated, search bar remains full, footer splits into 2 columns |
| Desktop | 1128–1440px | Three-column product grid (4-6 items), full nav with all links, search bar at full width, footer in 4 columns, hero banner at full padding |
| Wide | > 1440px | Four-column product grid (6-8 items), max-width container at 1440px centered, nav links with extra spacing, hero banner centered with max-width |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height (48px preferred) for touch accessibility.
- Product card tap targets (title, price, image) are the full card area — no small links.
- Filter chips and category pills are 36px minimum height with 20px horizontal padding.
- Quantity selector buttons are 40px × 40px for easy tapping.
- Nav links on mobile expand to full-width 48px tap targets in the hamburger menu.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer. The search bar becomes a magnifying glass icon that expands to a full-width input on tap.
- Product filters collapse into a "Filter" button that opens a modal overlay on mobile.
- The footer's multi-column layout collapses to a single column on mobile, with accordion-style section headers for "Shop", "About", "Support", and "Connect".
- Product image galleries switch from horizontal thumbnails to a swipeable carousel on mobile.
- The hero banner reduces its headline to 24px and stacks the CTA below the text on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover and focus states** — Extracted only from observed behavior; exact box-shadow values, transition durations, and color opacity levels for hover/focus/active states are inferred from common patterns. The brand may use different values.
- **Error and validation styling** — No error messages, form validation states, or empty-state designs were observed on the live site. The error input border (#d23827) is inferred from the brand's red accent.
- **Dark mode** — The site does not appear to support dark mode. All colors are defined for light mode only.
- **Sub-brand or seasonal palettes** — Wild Republic may use special color palettes for holiday collections or licensed products (e.g., Disney, National Geographic). These were not observed.
- **Animation and motion** — No animation durations, easing curves, or transition properties were extracted. The site uses standard CSS transitions (likely 0.2s–0.3s ease) but exact values are unknown.
- **Typography scale** — Font sizes and weights are inferred from observed page elements and common system font behavior. The brand does not use a custom typeface, so exact sizing may vary slightly across browsers.
- **Component spacing** — Padding and margin values for components like product cards and badges are estimated from visual inspection. The brand may use a different spacing scale.
- **Checkout and cart** — Shopify's default checkout styling may override brand colors. The extracted color list includes several Shopify-related colors (#006fbb, #084e8a, #212b36) that are not part of the brand's design system.
- **Social media icons** — Colors like #7f5fca (Instagram gradient) and #d23827 (Pinterest) may appear in social link sections but are not brand colors.
- **Accessibility** — Color contrast ratios for text on backgrounds have not been verified. The muted gray (#777777) on white may not meet WCAG AA for small text.
