---
version: alpha
name: "Alice, Ever After Books"
source_url: "https://www.aliceeverafterbooks.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A children's bookstore in Buffalo, NY that wraps itself in a slate-and-ink palette — #73859f, a quiet blue-gray that reads as neither childish nor corporate, anchors the brand alongside #2b333f for deep text and #eff4f8 for the page canvas. The extracted colors suggest a system built on muted confidence: #919191 and #707070 for secondary text, #f1f1f1 and #f8f8f8 for soft surfaces, with #bce7f4 as a possible accent for interactive elements. The brand runs on Inter and Arial, a pragmatic sans-serif stack that prioritizes legibility for young readers and their parents. Buttons use {rounded.sm} corners — friendly but not cartoonish — while the overall layout leans on generous {spacing.lg} and {spacing.xl} gaps that give children's book covers room to breathe. The store's physical address at 295 Parkside Ave grounds the digital experience in a real place, and the meta theme-color of #eff4f8 ensures the browser chrome itself feels like a page from a well-loved picture book. There is no heavy-handed whimsy here; the design trusts the books themselves to provide color and wonder, while the interface stays calm, organized, and quietly supportive.

colors:
  primary: "#73859f"
  primary-active: "#5c6f8a"
  primary-disabled: "#b3bfd0"
  ink: "#2b333f"
  body: "#3d4853"
  muted: "#707070"
  muted-soft: "#919191"
  hairline: "#d6d6d6"
  hairline-soft: "#e6e6e6"
  canvas: "#eff4f8"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-light: "#bce7f4"
  accent-warm: "#ff7734"
  error: "#e1251b"
  star-rating: "#ff7734"

typography:
  display-xl:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 12px 20px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
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
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.accent-light}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.base}"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    margin-bottom: "{spacing.lg}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for adding items to cart, submitting forms, and key navigational actions. Rendered in the brand's slate blue-gray {colors.primary} with white text at 15px/600 weight. On hover, shifts to {colors.primary-active} (#5c6f8a) for a subtle darkening. Disabled state uses {colors.primary-disabled} (#b3bfd0) with white text, signaling the action is unavailable without visual noise.

**`button-secondary`** — An outlined alternative for less prominent actions like "Continue Shopping" or "View Details". Uses a white background with {colors.ink} text and a 1px {colors.hairline} border. On hover, the border darkens to {colors.muted} and the background shifts to {colors.surface-soft}. Maintains the same 44px height and {rounded.sm} corners as the primary button for visual consistency.

**`button-ghost`** — A text-only button for tertiary actions like "Cancel" or "Clear Filters". No background or border, uses {colors.primary} text at the same button-md typography. On hover, adds a subtle {colors.surface-soft} background. Used sparingly to avoid clutter in dense UI areas.

### Cards
**`product-card`** — The primary container for displaying book covers and metadata in grid and list views. A white card with {rounded.md} (12px) corners and no border, relying on the natural contrast against {colors.canvas} or {colors.surface-soft} backgrounds. The book cover image sits flush to the top with rounded top corners, while title and price sit below with {spacing.sm} and {spacing.base} padding respectively. On hover, the card gains a subtle shadow (1px 2px 8px rgba(43, 51, 63, 0.08)) to indicate interactivity.

### Navigation
**`nav-bar`** — A 72px fixed-height bar with {colors.canvas} background and a thin {colors.hairline-soft} bottom border. Contains the store logo on the left, primary navigation links in the center, and utility icons (search, cart, account) on the right. Active nav links are indicated by a 2px {colors.primary} bottom border. The bar remains sticky on scroll for desktop, collapsing to a hamburger menu on mobile.

**`nav-link-active`** — Uses {colors.ink} text with a 2px {colors.primary} underline. The underline animates in on hover for inactive links, creating a smooth transition between states. Inactive links use {colors.muted} (#707070) to reduce visual weight.

### Forms
**`text-input`** — Standard form input for search, newsletter signup, and checkout fields. White background with 1px {colors.hairline} border and {rounded.sm} corners. On focus, the border thickens to 2px and shifts to {colors.primary}, with the label or placeholder remaining visible. Error states use a 2px {colors.error} border with an accompanying error message in {typography.caption}.

**`search-bar`** — A specialized input for the site search, distinguished by {rounded.full} (pill shape) corners. Uses the same dimensions as text-input but with a search icon inset on the left. On focus, the border transitions to {colors.primary} and a dropdown of suggested results appears below.

### Badges
**`badge-new`** — A small pill-shaped label for new arrivals, using {colors.accent-light} (#bce7f4) background with {colors.ink} text. The light blue reads as fresh and youthful without competing with book cover colors. Used inline on product cards and category headers.

**`badge-sale`** — A red pill badge for discounted items, using {colors.error} (#e1251b) background with white text. The high-contrast red ensures sale items are immediately visible in grid views. Both badges share the same {typography.badge} sizing and {rounded.full} shape for consistency.

### Footer
**`footer`** — A dark footer section using {colors.ink} (#2b333f) background with light gray text at {colors.muted-soft} (#919191). Contains three columns: store information, customer service links, and social media icons. Links use {colors.muted-soft} and lighten to {colors.surface-soft} on hover. The footer includes the store's physical address (295 Parkside Ave, Buffalo, NY 14214) and a copyright line, reinforcing the local bookstore identity.

### Hero
**`hero-section`** — The full-width banner area on the homepage, using {colors.canvas} background with {spacing.section} (64px) vertical padding. Contains a featured book cover, a headline in {typography.display-xl}, and a supporting description in {typography.body-md}. The hero may include a {colors.accent-light} accent bar or decorative element to draw attention to seasonal promotions or new arrivals.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid, hamburger nav, reduced hero padding to {spacing.xl}, product cards stack vertically, search bar collapses to icon-only, footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, hero uses {typography.display-lg}, search bar remains full-width but with reduced padding |
| Desktop | 1128–1440px | Three-column product grid, full nav bar with all links, hero at full {spacing.section} padding, search bar with dropdown suggestions |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero may feature a two-column layout with book cover and description side by side |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets extend to full card width and height
- Nav bar hamburger icon uses a 48x48px touch area
- Pagination buttons are 36px tall with 12px horizontal padding, meeting touch guidelines
- Search icon in mobile nav uses a 44x44px touch target

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-in drawer from the left
- Product grid reduces from 4 columns to 1 column on mobile, with 2 columns on tablet
- Footer columns collapse from 3 to 1 on mobile, with links stacked vertically
- Hero section reduces vertical padding from {spacing.section} to {spacing.xl} on mobile
- Search bar collapses to an icon button on mobile, expanding to full-width on tap
- Breadcrumb trail truncates to show only the current page and parent category on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; the above uses reasonable inferences from the color palette
- Error styling for form validation (border colors, error message placement) is inferred from the extracted error red (#e1251b) but exact implementation details are unknown
- Dark mode is not present on the live site and has not been designed
- Sub-brand or seasonal color palettes (e.g., holiday themes, author-specific landing pages) are not documented
- Animation durations and easing curves (transitions, hover effects) are not specified; a future revision should define a motion system
- Typography hierarchy for mobile (scaled-down font sizes) is not confirmed from extraction; the above uses standard responsive scaling
- The extracted font list is limited to Arial, Helvetica, and Inter; the exact weight and style usage for headings vs. body text is inferred
- Iconography style (filled vs. outlined, stroke width) is not documented
- Spacing values for specific components (e.g., product card internal padding) are inferred from common patterns and may differ from the live site
- The accent color #bce7f4 is present in the extraction but its exact usage (links, badges, backgrounds) is speculative
- Checkout flow styling (Shopify Pay, Klarna, Afterpay widgets) was filtered from extraction and is not documented
