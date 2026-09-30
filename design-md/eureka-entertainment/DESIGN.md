---
version: alpha
name: "Eureka Entertainment"
source_url: "https://eurekavideo.co.uk"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep-crimson accent of #c90000 against a near-white canvas of #fdfdfd announces Eureka Entertainment as a home for serious cinema — the red is not a playful brand mark but a signal of authority, used sparingly on primary CTAs, the masthead logo, and the "Masters of Cinema" series badge. The palette is deliberately restrained: body text in #2c2d33, secondary copy in #5d7380, and hairline borders in #dadada create a reading environment that prioritizes film stills and poster art over decorative UI. Typography relies on system-native stacks — Helvetica Neue, Arial, and BlinkMacSystemFont — with Andale Mono reserved for technical metadata (run times, aspect ratios, release years), a nod to the collector's impulse for specification. Cards and buttons use gentle radii ({rounded.sm} ~8px) that never compete with the hard edges of film frames, while the footer and secondary navigation recede into #eeeeee surfaces. The brand trusts its product photography entirely: there are no hero illustrations, no decorative gradients, no brand patterns — just a white gallery wall with red accents.

colors:
  primary: "#c90000"
  primary-active: "#a30000"
  primary-disabled: "#f0b3b3"
  ink: "#2c2d33"
  body: "#43454b"
  muted: "#5d7380"
  muted-soft: "#888888"
  hairline: "#dadada"
  hairline-soft: "#eeeeee"
  canvas: "#fdfdfd"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#d43858"
  accent-link: "#0073aa"
  badge-new: "#1e7e34"
  badge-coming-soon: "#117a8b"
  star-rating: "#d39e00"
  error: "#bd2130"
  success: "#1e7e34"
  info: "#117a8b"
  warning: "#856404"

typography:
  display-xl:
    fontFamily: "Helvetica Neue, Arial, BlinkMacSystemFont, -apple-system, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Helvetica Neue, Arial, BlinkMacSystemFont, -apple-system, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Helvetica Neue, Arial, BlinkMacSystemFont, -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "Helvetica Neue, Arial, BlinkMacSystemFont, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Helvetica Neue, Arial, BlinkMacSystemFont, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Helvetica Neue, Arial, BlinkMacSystemFont, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Helvetica Neue, Arial, BlinkMacSystemFont, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Helvetica Neue, Arial, BlinkMacSystemFont, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-mono:
    fontFamily: "Andale Mono, Courier New, Courier, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Helvetica Neue, Arial, BlinkMacSystemFont, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "Helvetica Neue, Arial, BlinkMacSystemFont, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "Helvetica Neue, Arial, BlinkMacSystemFont, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Helvetica Neue, Arial, BlinkMacSystemFont, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Helvetica Neue, Arial, BlinkMacSystemFont, -apple-system, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
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
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    outline: "2px solid {colors.primary}"
    outlineOffset: "1px"
  text-input-error:
    border: "1px solid {colors.error}"
  select:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(44,45,51,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "2/3"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-coming-soon:
    backgroundColor: "{colors.badge-coming-soon}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-price:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.title-md}"
    textColor: "{colors.accent-sale}"
  product-card-price-original:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-soft}"
    textDecoration: "line-through"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    height: 480px
  hero-banner-overlay:
    backgroundColor: "rgba(44,45,51,0.5)"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  section-header:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"
    paddingBottom: "{spacing.sm}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: "14px"
  loading-spinner:
    color: "{colors.primary}"
    size: "24px"
  toast-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  toast-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  toast-info:
    backgroundColor: "{colors.info}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  modal-overlay:
    backgroundColor: "rgba(44,45,51,0.6)"
  modal-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    maxWidth: "600px"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.md} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's signature #c90000 on a white canvas. Text is uppercase 14px weight 600 with 0.3px letter-spacing, giving it a confident editorial tone. On hover, the background deepens to #a30000; the disabled state uses #f0b3b3. All primary buttons use {rounded.sm} (8px) — enough softness to feel approachable without undermining the serious brand voice.

**`button-secondary`** — An outlined variant for less prominent actions, using a white background with a 1px {colors.hairline} border and {colors.ink} text. Active state swaps the border to {colors.ink} and adds a light gray background. Used for "Add to Wishlist," "View Details," and secondary form actions.

**`button-text`** — A borderless, backgroundless button that uses only the brand red for text. Reserved for inline actions like "Clear filters," "Cancel," or "Read more." The active state shifts to #a30000.

**`button-pill`** — A compact, fully rounded variant ({rounded.full}) used for category filters, tag badges, and mobile navigation chips. Smaller padding and 12px uppercase text keep it unobtrusive while maintaining the brand's red accent.

### Cards
**`product-card`** — The primary content container for film titles, built as a white card with a subtle 1px {colors.hairline-soft} border and {rounded.sm} corners. On hover, the border darkens to {colors.hairline} and a light box shadow lifts the card. The image area occupies the top two-thirds at a 2:3 aspect ratio (standard Blu-ray/DVD proportions), with rounded top corners only. Below sit the title, format badge, price, and action buttons.

**`product-card-badge`** — Small uppercase labels that flag film editions: "Blu-ray," "DVD," "Limited Edition," "Restored." The default badge uses the brand red background; a pink (#d43858) variant signals sale pricing, green (#1e7e34) marks new releases, and teal (#117a8b) indicates pre-orders or coming-soon titles. All badges use {rounded.xs} (4px) and 10px bold uppercase type.

### Navigation
**`top-nav`** — A 64px white bar with a bottom border of {colors.hairline-soft}. Navigation links use 14px weight 500 in {colors.muted} by default, switching to {colors.primary} with a 2px red bottom border when active. The logo (typically the Eureka wordmark or "Masters of Cinema" crest) sits left-aligned, with primary navigation items centered or right-aligned depending on viewport.

**`breadcrumb`** — Small 12px gray text for secondary navigation paths like "Home > Shop > Blu-ray > The Passion of Joan of Arc." The active (current) page uses {colors.ink} while ancestor links remain {colors.muted}. No separators are rendered between items — just spacing and color changes.

### Forms
**`text-input`** — Standard form input with a white background, 1px {colors.hairline} border, and 15px body text. Focus state adds a 2px red outline with 1px offset. Error state swaps the border to #bd2130. Height is 44px for comfortable touch targeting.

**`select`** — Dropdown menus styled identically to text inputs, used for filtering by format, genre, year, or region. The native dropdown arrow is preserved for accessibility.

**`filter-chip`** — Pill-shaped toggle buttons for faceted search filters (e.g., "Blu-ray," "4K UHD," "Region B"). Default state is white with a gray border; active state fills with {colors.ink} and white text. Multiple chips can be active simultaneously.

### Footer
**`footer`** — A light gray (#eeeeee) section at the bottom of every page, containing links to About, Contact, Shipping, Privacy Policy, and social media. Text is 13px in {colors.muted} (#5d7380), with hover links turning to the brand red. The footer includes copyright information and payment method icons in a subdued grayscale.

### Feedback & Status
**`toast-success`** / **`toast-error`** / **`toast-info`** — Temporary notification bars that appear at the top of the viewport. Success uses green (#1e7e34), error uses red (#bd2130), and info uses teal (#117a8b). All use white text and {rounded.sm} corners, with a 15px body font.

**`loading-spinner`** — A simple rotating circle in {colors.primary} (#c90000), 24px in size, used during product list loading, checkout processing, and image lazy-loading.

**`modal-overlay`** / **`modal-card`** — A semi-transparent dark overlay (60% opacity of {colors.ink}) with a centered white card at {rounded.md} (12px). Used for quick-view product details, newsletter signups, and confirmation dialogs. The card has 32px padding and a max-width of 600px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger menu; hero banner height reduces to 320px; filter chips stack vertically; search bar moves to persistent header; footer links stack in single column |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links with "More" dropdown; hero banner at 400px; filter chips wrap to two rows; sidebar filters become horizontal strip |
| Desktop | 1128–1440px | Three-column product grid; full top-nav visible; hero banner at 480px; filter chips in horizontal row; sidebar filters visible on category pages |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero banner expands to full width with max-height 560px; additional whitespace around product cards |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Filter chips and badges are at least 32px tall with 16px horizontal padding.
- Product card images link to detail pages with a minimum tap area of 120px × 180px.
- Mobile navigation hamburger icon has a 48px × 48px tap target.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer containing all links and a search field.
- Product grid reduces columns from 4 to 1 as viewport narrows, with images maintaining their 2:3 aspect ratio.
- Sidebar filters collapse into a horizontal scrollable strip on tablet, and into a "Filters" button that opens a modal on mobile.
- Footer link columns stack vertically below 744px, with each section becoming an accordion to save vertical space.
- Hero banner text overlays shift from side-by-side to stacked on mobile, with reduced font sizes.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: While primary button hover (#a30000) and card hover (border + shadow) are documented, secondary hover states for all components (e.g., filter chips, pagination buttons, footer links) were inferred from common patterns rather than extracted from the live site.
- **Error and validation styling**: The error state for text inputs (#bd2130 border) is based on the extracted color list, but specific error message typography, iconography, and animation timing are not confirmed.
- **Focus and active states**: Keyboard focus outlines beyond the text-input focus style are not documented. The brand may use custom focus rings or rely on browser defaults.
- **Dark mode**: No dark mode implementation was detected. The brand's near-white canvas (#fdfdfd) and reliance on film stills suggest dark mode may not be a priority, but it's unconfirmed.
- **Typography scale**: Font sizes and weights were inferred from common editorial e-commerce patterns. The extracted font list includes system fonts only — no custom typefaces were detected. The brand may use a variable font or web font not captured in the extraction.
- **Animation and transition**: No animation durations, easing curves, or transition properties were extracted. The brand likely uses subtle fades and slides, but specifics are unknown.
- **Sub-brand palettes**: "Masters of Cinema" may have its own color variant (e.g., a gold or cream accent) that was not captured in the extraction. The Montage and Eureka Classics lines may also diverge.
- **Checkout and cart**: Shopify Pay, Klarna, and Afterpay colors were filtered from the extraction, but the brand's checkout UI styling (progress bars, summary cards, payment forms) is undocumented.
- **Accessibility contrast ratios**: While the primary red (#c90000) on white (#ffffff) likely passes WCAG AA for large text, its use on smaller elements (badges, links) should be verified. The muted text (#5d7380 on #fdfdfd) may fail contrast requirements.
