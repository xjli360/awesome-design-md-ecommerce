---
version: alpha
name: "Meri Meri"
source_url: "https://merimeri.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A children's party and nursery brand that builds its visual world on a pale, warm canvas of #fcf7f4 — a blush-tinged off-white that feels like the light in a nursery at golden hour — and then introduces voltage through a single, unexpected accent: #d96544, a dried-terracotta orange that appears on buttons, badges, and hover states, never as a background flood. The palette is restrained but not minimal: #b59677 (a dusty, almost-sage brown) and #ecced1 (a faded rose) sit alongside #222222 for body text and #54545e for captions, creating a system that reads as hand-picked rather than algorithmic. Typography is the brand's true signature: Clearface Bold, a serif with pronounced ball terminals and a warm, slightly condensed posture, is used for all display and title text — it gives every product name and heading the weight of a vintage children's book title. Halant, a softer serif with generous proportions, handles body copy, while New Atten — a rounded, friendly sans-serif — appears on buttons and navigation, creating a deliberate tension between old-world display and modern utility. Corners are soft but not pill-shaped: product cards use {rounded.md} (12px), buttons use {rounded.sm} (8px), and the search bar uses {rounded.full} only as a visual anchor. The brand avoids heavy shadows, preferring thin {colors.hairline} borders (#dedede) and subtle surface separations. The overall effect is one of curated whimsy — a party supply store that feels more like a paper-goods atelier, where every interaction is wrapped in the warmth of #f5eee6 and the quiet confidence of a brand that knows its audience values beauty over urgency.

colors:
  primary: "#d96544"
  primary-active: "#c25436"
  primary-disabled: "#f0c4b0"
  ink: "#222222"
  body: "#54545e"
  muted: "#878787"
  muted-soft: "#a0a0a0"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#fcf7f4"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-rose: "#ecced1"
  accent-sage: "#b59677"
  accent-gold: "#e0b252"
  accent-coral: "#ef7853"
  accent-pink: "#f5c3be"
  accent-red: "#ec0101"
  accent-green: "#428445"
  accent-dark: "#191919"
  accent-warm: "#f5eee6"

typography:
  display-xl:
    fontFamily: "'Clearface Bold', 'Georgia', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Clearface Bold', 'Georgia', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Clearface Bold', 'Georgia', 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Clearface Bold', 'Georgia', 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'New Atten', 'Open Sans', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'Halant', 'Georgia', 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Halant', 'Georgia', 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'New Atten', 'Open Sans', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'New Atten', 'Open Sans', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Halant', 'Georgia', 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'New Atten', 'Open Sans', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'New Atten', 'Open Sans', -apple-system, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  price:
    fontFamily: "'New Atten', 'Open Sans', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
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
    placeholderColor: "{colors.muted}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.accent-red}"
    padding: 12px 16px
    height: 48px
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-lg}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.primary}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "top-left"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "12px 20px"
    height: 48px
    iconColor: "{colors.muted}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
    padding: "12px 20px"
    height: 48px
  hero-banner:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
    textDecoration: none
  footer-link-hover:
    color: "{colors.surface-card}"
    typography: "{typography.link}"
    textDecoration: underline
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px"
    height: 44px
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
    width: 100px
  add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
    width: "100%"
  add-to-cart-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
    width: "100%"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    color: "{colors.ink}"
  pagination:
    typography: "{typography.button-sm}"
    color: "{colors.muted}"
  pagination-active:
    typography: "{typography.button-sm}"
    color: "{colors.ink}"
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
  rating-stars:
    color: "{colors.accent-gold}"
    size: 16px
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
**`button-primary`** — The primary call-to-action, rendered in {colors.primary} (#d96544) with white text and {typography.button-md} in uppercase New Atten. Used for "Add to Cart", "Shop Now", and primary checkout actions. On hover, shifts to {colors.primary-active} (#c25436). Disabled state uses {colors.primary-disabled} (#f0c4b0) to signal inactivity without visual noise.

**`button-secondary`** — A outlined variant on the warm {colors.canvas} background with {colors.ink} text and a {colors.hairline} border. Used for "View Details", "Learn More", and secondary actions. Active state fills with {colors.surface-soft} (#f7f7f7). Maintains the same 44px height and uppercase New Atten typography as primary.

**`button-ghost`** — A text-only button with no background or border, used for "Cancel", "Clear Filters", and inline actions. Hover state adds a subtle background tint. Typography matches the button system but with reduced padding for tighter layouts.

### Cards
**`product-card`** — The core product display unit, a white card with {rounded.md} (12px) corners and a thin {colors.hairline-soft} border. Contains a square aspect-ratio image with rounded top corners, a {typography.title-lg} product name in Clearface Bold, and a {typography.price} price in {colors.primary}. On hover, the border shifts to {colors.primary} and a subtle shadow lifts the card. An optional {colors.accent-gold} badge sits at the top-left corner for sale or new items.

**`hero-banner`** — A full-width section on {colors.accent-warm} (#f5eee6) background, featuring {typography.display-xl} in Clearface Bold and a prominent {colors.primary} CTA button. Minimum height of 400px, with generous padding that creates breathing room for seasonal messaging and promotional imagery.

### Navigation
**`nav-bar`** — A fixed-height (72px) navigation bar on {colors.canvas} with a subtle bottom border. Links use {typography.nav-link} in uppercase New Atten at 13px. Active links are underlined with a 2px {colors.primary} bar. Inactive links render in {colors.muted} (#878787). The bar collapses to a hamburger menu on mobile.

**`breadcrumb`** — Secondary navigation using {typography.caption} in Open Sans. Inactive crumbs are {colors.muted}, active (current page) is {colors.ink}. Separators are slashes in {colors.hairline}.

### Forms
**`text-input`** — Standard input field with white background, {colors.hairline} border, and {rounded.sm} (8px) corners. Uses {typography.body-md} in Halant for readability. Focus state swaps the border to {colors.primary}. Error state uses {colors.accent-red} (#ec0101). Placeholder text is {colors.muted}.

**`select-input`** — Dropdown variant of the text input with a custom chevron icon in {colors.muted}. Maintains the same dimensions and border system.

**`newsletter-input`** — A compact input (44px) paired with a {colors.primary} submit button. Used in the footer for email capture. The input uses {typography.body-sm} and the button uses {typography.button-sm} to maintain proportion within the footer layout.

### Footer
**`footer`** — A dark section on {colors.ink} (#222222) with white text. Links are {colors.muted-soft} (#a0a0a0) and underline on hover. Contains the newsletter signup, navigation columns, and social links. Typography is {typography.body-sm} in Halant for body content and {typography.caption} in Open Sans for legal text.

### Interactive Elements
**`accordion`** — Expandable sections with a {typography.title-md} header in New Atten and a bottom border. Content uses {typography.body-sm} in Halant. Used for product descriptions, shipping details, and FAQ sections.

**`quantity-selector`** — A compact 100px-wide control with {rounded.sm} corners and a {colors.hairline} border. Contains increment/decrement buttons and a numeric display. Uses {typography.button-md} for the number.

**`add-to-cart`** — A full-width button (100% of parent) for product pages. Matches {colors.primary} styling with uppercase New Atten. Active state shifts to {colors.primary-active}. Positioned at the bottom of product detail sections.

**`pagination`** — Page navigation using {typography.button-sm} in New Atten. Active page has a {colors.surface-soft} background and {rounded.sm} corners. Inactive pages are {colors.muted}. Used on collection and search result pages.

**`rating-stars`** — A 16px star icon in {colors.accent-gold} (#e0b252) for product reviews. Rendered as inline SVG or icon font. Half-star support for fractional ratings.

**`tooltip`** — A dark ({colors.ink}) tooltip with white text and {rounded.xs} (4px) corners. Uses {typography.caption} in Open Sans. Appears on hover for icon buttons, size selectors, and informational icons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked footer, reduced hero height (300px), full-width buttons |
| Tablet | 744–1128px | Two-column product grid, expanded nav, side-by-side footer columns, 48px hero padding |
| Desktop | 1128–1440px | Three-column product grid, full nav bar, multi-column footer, 64px hero padding |
| Wide | > 1440px | Four-column product grid, max-width container (1440px), extended hero with larger typography |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets are the full card surface, not just text
- Quantity selector buttons are 40px × 40px minimum
- Accordion headers are 48px minimum tap height
- Search bar and nav links have 48px touch zones

### Collapsing Strategy
- Navigation collapses to a hamburger menu below 744px, with a slide-out drawer
- Product grid reduces columns from 4 → 3 → 2 → 1 as viewport narrows
- Footer stacks vertically on mobile, with accordion-style collapsible sections
- Hero banner reduces padding and font size on mobile, with CTA stacking below text
- Breadcrumbs truncate to show only current and parent page on mobile
- Sidebar filters collapse to a modal overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and ghost buttons could not be fully extracted; inferred from common patterns
- Error message styling (color, typography, iconography) not observed on live site
- Dark mode or high-contrast mode not implemented; no corresponding tokens exist
- Loading states (spinners, skeleton screens) not extracted; placeholder behavior assumed
- Focus ring styles (outline, offset, color) not observed; accessibility implementation unknown
- Sub-brand or seasonal palette variations not captured; only core palette extracted
- Animation durations and easing curves not observed; no motion tokens defined
- Icon library and stroke weights not extracted; icon colors inferred from context
- Checkout flow styling (Shopify Pay, Klarna, Afterpay) filtered out as widget colors
- The extracted color list contained 28+ colors, many of which are likely checkout widgets, social icons, or stock image tones. The true brand palette was inferred from the most distinctive and frequently occurring colors in the UI context.
