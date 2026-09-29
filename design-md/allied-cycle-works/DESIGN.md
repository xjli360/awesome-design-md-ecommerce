---
version: alpha
name: "Allied Cycle Works"
source_url: "https://alliedcycleworks.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep blue #1878b9 anchors the brand — not as a sky or water reference, but as a deliberate industrial accent that signals precision engineering against a near-white #fafafa canvas. The palette is lean: a single red #e22120 used sparingly for sale badges or urgent markers, a near-black #121212 for body text, and a middle gray #dedede for structural dividers and secondary backgrounds. There are no gradients, no decorative color blocks — the brand trusts the geometry of carbon frames and the clarity of product photography to carry visual interest. Typography runs at modest sizes with generous line-height, letting spec sheets and build details breathe without crowding. Buttons are flat rectangles with {rounded.sm} corners, never pills — the brand avoids friendly curves in favor of a machined, deliberate feel. The Shopify checkout flow introduces a second blue (#1878b9 again as the primary CTA color), keeping the purchase experience visually continuous with the rest of the site. The overall impression is of a workshop catalog translated to screen: clean, unadorned, and confident in the object itself.

colors:
  primary: "#1878b9"
  primary-active: "#135f94"
  primary-disabled: "#a3c9e5"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#fafafa"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#e22120"
  accent-red-soft: "#f5c6c6"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
    textTransform: uppercase

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
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-tertiary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
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
    padding: 7px 19px
    height: 36px
    border: "1px solid {colors.hairline}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  icon-button-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 8px 0
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-hover:
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "0 {spacing.base} {spacing.base} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-stock:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0"
  hero-heading:
    typography: "{typography.display-xl}"
    marginBottom: "{spacing.base}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.lg}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-current:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.hairline}"
    margin: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"
  pagination-disabled:
    color: "{colors.muted-soft}"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  skeleton-loader:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop Now", and checkout initiation. Flat rectangular shape with {rounded.sm} corners and the brand's deep blue #1878b9 fill. On hover, darkens to #135f94 (`{colors.primary-active}`). Disabled state uses a washed-out blue `{colors.primary-disabled}`. Text is white, set in `{typography.button-md}` at 15px with 0.2px letter-spacing for a precise, engineered feel.

**`button-secondary`** — Outline variant for secondary actions like "View Details" or "Learn More". White background with a 1px `{colors.hairline}` border. On hover, background shifts to `{colors.surface-soft}` and border to `{colors.ink}`. Same typography as primary, maintaining consistent 44px height.

**`button-tertiary`** — Text-only button for less prominent actions like "Clear Filters" or "Cancel". Uses `{colors.primary}` text on a transparent background. Hover adds a subtle `{colors.surface-soft}` background. No border, no padding beyond the text itself — the most minimal CTA in the system.

**`button-pill`** — A compact, fully rounded variant used for filter chips, category tags, and mobile navigation items. Smaller at 36px height with `{typography.button-sm}`. The pill outline version uses a transparent background with a hairline border, allowing it to sit alongside filled pills in filter bars.

### Cards
**`product-card`** — The primary product display unit, used in collection grids and search results. A white card with `{rounded.md}` corners and no border — the card relies on the photography and whitespace to define its edges. On hover, a subtle box-shadow lifts the card. The image area uses `{rounded.md}` on top corners only, creating a clean transition from photo to text. Title uses `{typography.title-sm}` at 16px/600, price uses `{typography.body-md}` at 16px/400.

**`badge-sale`** — A small, high-contrast label for discounted items. Uses the brand's red #e22120 as background with white text in uppercase 11px/600. Minimal padding (2px 8px) and `{rounded.xs}` corners keep it unobtrusive but legible against product photography.

**`badge-new`** — Blue variant of the badge system, using `{colors.primary}` for new arrivals or limited editions. Same typography and dimensions as the sale badge, differentiated only by color.

### Navigation
**`nav-bar`** — Fixed-position top navigation at 72px height. White background with a subtle bottom border (`{colors.hairline-soft}`). Navigation links are uppercase 14px/500 with 0.2px letter-spacing. Active state underlines with a 2px `{colors.primary}` border-bottom. The nav includes a logo lockup on the left and utility icons (search, account, cart) on the right.

**`nav-dropdown`** — Flyout menu for secondary navigation. White card with `{rounded.md}` corners and a soft box-shadow. Items are 14px/400 with 8px vertical padding. No icons — just text links that inherit the nav's uppercase treatment for top-level items and sentence case for sub-items.

**`filter-chip`** — Pill-shaped filter tags used in collection pages. Filled variant uses `{colors.surface-soft}` background; active state switches to `{colors.primary}` with white text. Outline variant uses transparent background with hairline border. All chips use `{typography.caption}` at 13px.

### Forms
**`text-input`** — Standard form input for search, account forms, and checkout. White background with a 1px `{colors.hairline}` border and `{rounded.sm}` corners. On focus, the border switches to `{colors.primary}`. Error state uses `{colors.accent-red}` border. Input text is 16px/400 with 12px 16px padding, matching the body text size for readability.

**`select-input`** — Dropdown select styled consistently with text inputs. Same dimensions, border, and corner radius. The dropdown arrow is a custom SVG in `{colors.muted}`, not the browser default.

### Footer
**`footer-section`** — Dark footer using `{colors.ink}` (#121212) as background. Text is white at 14px/400. Links are `{colors.muted-soft}` (#999999) and lighten to white on hover. The footer contains brand info, customer service links, legal text, and social icons. Section padding is 48px top and bottom.

### Accordion
**`accordion`** — Collapsible sections used for product specifications, sizing guides, and FAQ content. Each item has a bottom border (`{colors.hairline-soft}`). Header uses `{typography.title-sm}` at 16px/600 with 16px vertical padding. Content area uses `{typography.body-sm}` at 14px/400 with 16px bottom padding. No icons — the accordion relies on the text weight change and border to indicate expandability.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; filter bar becomes a bottom sheet; hero text reduces to `{typography.display-lg}`; product cards stack vertically; footer links collapse into accordion |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links only; filter bar remains visible but chips wrap; hero uses `{typography.display-xl}`; product cards in 2-column grid |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; filter bar with horizontal chip row; hero at full width with `{typography.display-xl}`; product cards in 3-column grid |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; nav remains full; filter bar centered within container; hero may include side image or video |

### Touch Targets
- All interactive elements (buttons, links, filter chips) maintain minimum 44x44px touch target
- Icon buttons are 40x40px with 8px padding
- Filter chips are 36px tall with 14px horizontal padding
- Accordion headers have 16px padding top and bottom for easy tapping
- Product card images link to product pages with full-card tap target

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Filter bar collapses to a "Filters" button that opens a bottom sheet below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Footer link groups collapse to accordion panels below 744px
- Hero section reduces heading size and may stack image below text below 744px
- Secondary navigation (breadcrumbs, pagination) collapses to single-line truncation below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extractable from the live site; the typography block uses Inter as a reasonable system-ui fallback, but the actual brand font may differ
- Hover and focus states for all components are inferred from common patterns, not extracted from live CSS
- Error state styling for forms (error messages, validation icons) is not confirmed
- Dark mode or high-contrast mode styles are not present in extracted data
- Sub-brand or collection-specific color variations (e.g., gravel vs. road vs. mountain) are not documented
- Checkout flow styling (Shopify-specific) may introduce additional colors or button variants not captured here
- Loading states, empty states, and error states for product grids and search results are not extracted
- Animation durations, easing curves, and transition properties are not available
- The extracted hex list (#1878b9, #dedede, #fafafa, #e22120, #121212) is sparse and may not represent the full brand palette — particularly missing are any secondary or tertiary accent colors, gradient usage, or photography overlay colors
