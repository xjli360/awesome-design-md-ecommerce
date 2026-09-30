---
version: alpha
name: "Magnolia"
source_url: "https://magnolia.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A sage-and-cream retail world built on the tension between #5b2ea6 — a deep, almost ecclesiastical purple that appears in product badges, footer headings, and editorial accents — and a ground of #e9e5d5, a warm limestone beige that serves as the brand’s true canvas. The palette reads like a farmhouse pantry: #79765d (olive drab), #4c6063 (slate teal), #3d452e (forest shadow), and #85650b (aged brass) sit alongside #f9e8c5 (buttermilk) and #f3f1e9 (flax linen). White (#fefefe) is reserved for product cards and content blocks, while #222222 ink keeps body copy sharp against the soft grounds. Typography layers Merriweather’s serif gravity for display and body — its bracketed serifs and moderate contrast evoke printed recipe cards and heirloom books — against Montserrat for buttons and navigation, where clean geometric sans-serif signals action rather than atmosphere. Corners are predominantly soft: cards use {rounded.md} (12px), buttons use {rounded.sm} (8px), and the occasional pill-shaped search or badge uses {rounded.full}. The design system resists the hard digital edge; even the hairline (#e9e5d5, identical to the canvas) disappears into the background, making separations feel like paper folds rather than code borders. Product photography — often styled on wood surfaces or against neutral linen — carries the emotional weight; the UI steps back, framing rather than competing. The overall effect is a store that feels like a restored house: warm, slightly worn, and deliberate in every material choice.

colors:
  primary: "#5b2ea6"
  primary-active: "#4a2591"
  primary-disabled: "#d4c5e8"
  ink: "#222222"
  body: "#4b4b4b"
  muted: "#79765d"
  muted-soft: "#939274"
  hairline: "#e9e5d5"
  hairline-soft: "#f3f1e9"
  canvas: "#e9e5d5"
  surface-soft: "#f6f6f5"
  surface-card: "#fefefe"
  on-primary: "#ffffff"
  accent-sage: "#576132"
  accent-teal: "#4c6063"
  accent-brass: "#85650b"
  accent-buttermilk: "#f9e8c5"
  accent-forest: "#3d452e"
  accent-stone: "#575449"
  accent-error: "#de3618"
  accent-link: "#6596c3"

typography:
  display-xl:
    fontFamily: "'Merriweather', 'MinionPro-Regular', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Merriweather', 'MinionPro-Regular', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Merriweather', 'MinionPro-Regular', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'Merriweather', 'MinionPro-Regular', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "'Merriweather', 'MinionPro-Regular', serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Merriweather', 'MinionPro-Regular', serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Merriweather', 'MinionPro-Regular', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Merriweather', 'MinionPro-Regular', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Merriweather', 'MinionPro-Regular', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'Montserrat', sans-serif"
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
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 0
    height: 44px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.accent-error}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.xl}"
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.xl}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "0 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "0 16px"
    height: 48px
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-sale:
    backgroundColor: "{colors.accent-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    maxWidth: 600px
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    maxWidth: 500px
    marginTop: "{spacing.md}"
  hero-cta:
    component: button-primary
    marginTop: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.surface-card}"
    marginBottom: "{spacing.md}"
  footer-link:
    typography: "{typography.body-sm}"
    color: "{colors.muted-soft}"
    textDecoration: none
  footer-link-hover:
    typography: "{typography.body-sm}"
    color: "{colors.surface-card}"
    textDecoration: underline
  section-heading:
    typography: "{typography.display-lg}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginBottom: "{spacing.xl}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.lg} 0"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-panel:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} 0 {spacing.md} 0"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    height: 44px
    width: 44px
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.muted-soft}"
    margin: "0 {spacing.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Shop Now," and checkout progression. Rendered in the brand's deep purple {colors.primary} with white text and {rounded.sm} corners, it carries an uppercase Montserrat label at 14px/600 weight. On hover, the background shifts to {colors.primary-active} (#4a2591); disabled state uses {colors.primary-disabled} (#d4c5e8) with reduced opacity. The button maintains a consistent 44px height with generous 28px horizontal padding to accommodate longer product names in the CTA.

**`button-secondary`** — An outlined alternative for secondary actions like "View Details" or "Save for Later." Uses a white background with a 2px solid {colors.ink} border, matching the primary button's 44px height and uppercase Montserrat typography. Active state fills the background with {colors.surface-soft} (#f6f6f5). This button appears frequently on product cards and in cart summaries where visual hierarchy must distinguish between primary and secondary paths.

**`button-tertiary`** — A text-only button for low-emphasis actions such as "Cancel" or "Clear Filters." No background or border, relying solely on {colors.ink} text in uppercase Montserrat. The 44px height matches sibling buttons for alignment in grouped button bars, but padding is horizontal-only (12px left/right) to keep the footprint minimal.

**`button-pill`** — A compact, fully rounded button used for filter chips, category tags, and promotional badges. Uses {typography.button-sm} (12px uppercase) with 8px/20px padding and a 36px height. The pill shape ({rounded.full}) distinguishes it from standard buttons, signaling a toggleable or dismissible interaction.

### Cards
**`product-card`** — The primary container for product display across collection pages, search results, and related-product grids. A white card ({colors.surface-card}) with {rounded.md} corners, 16px padding, and a subtle drop shadow (0 2px 8px rgba(0,0,0,0.06)). The card image occupies the top with {rounded.sm} corners and a 1:1 aspect ratio. Below, the product title uses {typography.title-sm} (uppercase Montserrat, 14px/600) with the price in {typography.body-sm} at {colors.body}. On hover, the shadow deepens to 0 4px 16px rgba(0,0,0,0.1), providing a subtle lift effect. Badges (New, Sale, Sold Out) overlay the top-left of the image using pill-shaped labels.

### Navigation
**`nav-bar`** — The persistent top navigation, 72px tall on the {colors.canvas} background. Navigation links use {typography.nav-link} — 13px uppercase Montserrat with 0.8px letter-spacing — creating a refined, editorial feel. The active link is highlighted in {colors.primary}. On scroll, the nav transitions to a white background ({colors.surface-card}) with a subtle bottom shadow, and the height reduces to 64px for a more compact reading state. The logo (typically "MAGNOLIA" in a serif or custom wordmark) sits left-aligned, with nav links centered or right-aligned depending on viewport.

### Forms
**`text-input`** — Standard text entry fields for search, email signup, and address forms. A white input with {rounded.sm} corners, 48px height, and a 1px {colors.hairline} border. Typography uses {typography.body-md} (16px Merriweather) for readability. On focus, the border thickens to 2px and shifts to {colors.primary}, providing clear focus indication. Error state uses a 2px {colors.accent-error} (#de3618) border with an accompanying error message in the same red.

**`select-input`** — Dropdown selectors for options like size, quantity, and sort order. Matches the text-input dimensions and styling, with a custom chevron icon in {colors.muted}. The selected value displays in {typography.body-md}.

**`textarea`** — Multi-line text input for order notes or contact forms. Shares the same border, background, and typography as text-input but without a fixed height, expanding vertically with content.

### Footer
**`footer`** — A dark, anchored footer on {colors.ink} (#222222) background, spanning the full viewport width. Content is padded at {spacing.section} (64px) vertically and {spacing.xl} (32px) horizontally. Footer headings use {typography.title-sm} (uppercase Montserrat) in white, while links use {typography.body-sm} in {colors.muted-soft} (#939274). On hover, footer links lighten to white with underline. The footer typically organizes content into 3-4 columns: Shop, About, Customer Service, and Newsletter Signup, with a copyright line at the bottom in {colors.muted}.

### Badges
**`badge-new`** — A purple pill badge ({colors.primary}) for new arrivals, using {typography.badge} (10px uppercase Montserrat, 700 weight) in white. Positioned at the top-left of product card images with 2px/10px padding.

**`badge-sale`** — A red pill badge ({colors.accent-error}, #de3618) for discounted items. Same typography and positioning as badge-new, but the red signals urgency and markdown.

**`badge-sold-out`** — A muted olive pill badge ({colors.muted}, #79765d) for out-of-stock items. The desaturated color communicates unavailability without visual noise.

### Hero
**`hero-section`** — The full-width hero banner on the homepage and campaign pages. Rendered on the {colors.canvas} background with generous padding. The hero title uses {typography.display-xl} (36px Merriweather, 700 weight) constrained to 600px max-width for readability. A subtitle in {typography.body-md} (16px Merriweather) sits below with a 500px max-width. The primary CTA button sits below the subtitle, using the standard button-primary component. The hero typically features a full-bleed lifestyle image on the right or as a background, with text overlaid on the left.

### Accordion
**`accordion-trigger`** — Expandable section headers used in product descriptions, FAQs, and footer menus. Uses {typography.title-md} (16px Merriweather, 700 weight) in {colors.ink} with a bottom border of 1px {colors.hairline}. The trigger has 12px vertical padding and includes a chevron icon that rotates on open state.

**`accordion-panel`** — The expandable content area below each accordion trigger. Uses {typography.body-md} in {colors.body} with 8px top padding and 16px bottom padding. Content flows naturally within the panel, supporting paragraphs, lists, and inline links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grids (1-2 columns), nav collapses to hamburger menu, hero text stacks vertically, footer stacks to single column, buttons full-width, padding reduces to 16px |
| Tablet | 744–1128px | Two-column product grids, nav links visible but condensed, hero maintains side-by-side layout, footer splits to 2 columns, padding at 24px |
| Desktop | 1128–1440px | Three-to-four-column product grids, full nav with all links, hero at full width with generous whitespace, footer in 3-4 columns, max-width container at 1128px |
| Wide | > 1440px | Max-width container at 1440px, product grids can expand to 5 columns, hero content centered with wider text constraints, extra whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon-only buttons (search, cart, menu) use 44x44px touch targets even if the visual icon is smaller
- Product card tap targets extend to the full card area, not just the title or price
- Accordion triggers are full-width with 44px minimum tap height
- Quantity selector buttons are 44x44px for easy +/- tapping

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu at < 744px, with a slide-out drawer from the left
- Product filters collapse to a modal or bottom sheet on mobile, triggered by a "Filter" button
- Footer columns collapse to a single vertical stack on mobile, with accordion-style expandable sections
- Hero section reduces image height and stacks text below on mobile
- Multi-column product grids reduce to 1 column on mobile, 2 on tablet
- Search bar collapses to an icon on mobile, expanding to full-width on tap
- Breadcrumbs truncate to show only the current page and parent on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components are inferred from common patterns; exact transition durations and easing curves not extracted
- Focus ring styles (outline color, width, offset) not captured from the live site
- Error message styling (color, typography, iconography) for form validation not extracted
- Dark mode or high-contrast mode variants not present on the live site
- Sub-brand or seasonal palette variations (e.g., holiday, collaboration) not documented
- Custom checkbox and radio button styling not extracted; likely uses browser defaults or minimal customization
- Loading states (spinners, skeleton screens) not observed on the live site
- Modal/dialog overlay styling (backdrop color, animation) not captured
- Tooltip and popover styling not extracted
- The extracted hex list includes many colors that may be Shopify checkout widgets or stock image tones; the brand's true primary (#5b2ea6) was selected as the most distinctive non-generic color, but secondary accents like #576132 (sage) and #4c6063 (teal) may be more prominent in certain sections
- Font weights for Merriweather and Montserrat are inferred from common web usage; exact weights used in headings vs. body may vary
- Letter-spacing values for uppercase typography are estimated based on typical brand usage; exact values may differ
- Box shadow values for cards and nav are estimated from common e-commerce patterns; exact values not extracted
- Animation durations and easing curves for transitions (nav scroll, card hover, accordion toggle) not captured
