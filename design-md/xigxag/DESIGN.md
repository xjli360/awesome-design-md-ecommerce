---
version: alpha
name: "xigxag"
source_url: "https://xigxag.co.uk"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep-purple audiobook marketplace that reads like a midnight library — #351352 is the brand's primary voltage, a dark violet that wraps every primary CTA, navigation bar, and hero section in a moody, immersive glow. The site pairs this with a near-black ink (#13101a) for body text and a crisp white canvas (#f0f0f0) for backgrounds, creating a high-contrast reading environment that never feels harsh. Accent colors arrive as deliberate surprises: #02e49b (a bright mint) for success states and secondary badges, #ff9900 (warm amber) for price highlights and limited-time offers, and #e94c89 (vibrant pink) for wishlist hearts and social proof elements. The typography leans on a single serif stack — "inherit, serif" from the extracted declarations — suggesting a system that trusts classic book-like proportions over trendy sans-serif efficiency. Buttons use {rounded.sm} (8px) corners, while search bars and category pills take {rounded.full} for a friendly, approachable feel. The overall impression is of a brand that takes reading seriously but not solemnly: the dark violet backdrop of the hero section, the mint-green "Listen Now" badges, and the amber price tags all conspire to say "this is a bookstore, but it's also a discovery engine." The extracted hex list is unusually long (30+ colors), many of which are likely checkout-widget tints (Afterpay pink, Klarna blue) and social-icon brand colors — the true brand palette is tighter, centered on the violet-black-white triad with four accent notes.

colors:
  primary: "#351352"
  primary-active: "#2a0f42"
  primary-disabled: "#7a5a8a"
  ink: "#13101a"
  body: "#32373c"
  muted: "#949494"
  muted-soft: "#a6a6a6"
  hairline: "#444444"
  hairline-soft: "#f2f2f2"
  canvas: "#f0f0f0"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-mint: "#02e49b"
  accent-amber: "#ff9900"
  accent-pink: "#e94c89"
  accent-blue: "#0693e3"
  accent-purple: "#8430cd"
  star-rating: "#ff9900"
  error: "#ea4434"
  success: "#00d084"
  link: "#1ea0c3"
  link-visited: "#8430cd"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-lg:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px

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
  button-primary-lg:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 52px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    padding: 10px 22px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  button-pill-mint:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button-circle:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-circle-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    border: "2px solid {colors.primary}"
    padding: 11px 15px
  text-input-error:
    border: "1px solid {colors.error}"
    padding: 12px 16px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 12px 20px
    height: 48px
  search-bar-focus:
    border: "2px solid {colors.primary}"
    padding: 11px 19px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.accent-mint}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    opacity: 0.8
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    marginTop: "{spacing.xxs}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "top-right"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-cta:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    height: 52px
    marginTop: "{spacing.lg}"
  hero-subtitle:
    typography: "{typography.body-lg}"
    color: "{colors.on-primary}"
    opacity: 0.85
    marginTop: "{spacing.base}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
    marginBottom: "{spacing.sm}"
  footer-link-hover:
    color: "{colors.on-primary}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 16px
    gap: "{spacing.xxs}"
  badge-mint:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.base} 0"
  section-header:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-header-accent:
    borderLeft: "4px solid {colors.primary}"
    paddingLeft: "{spacing.md}"

## Components

### Buttons
**`button-primary`** — The workhorse CTA, filled with the brand's deep violet {colors.primary} and white text. Used for "Add to Cart," "Subscribe," and "Start Listening" actions. On hover, it shifts to {colors.primary-active} (#2a0f42) for a subtle darkening effect. The disabled state uses {colors.primary-disabled} (#7a5a8a) to signal unavailability without losing brand recognition. A larger variant (`button-primary-lg`) exists for hero sections and landing-page CTAs, with increased padding and font size.

**`button-secondary`** — An outlined button with a white fill and violet border, used for "Learn More" and "View Details" actions. The active state darkens both the border and text to {colors.primary-active}. This button sits alongside the primary CTA in hero sections and product detail pages, offering a clear visual hierarchy without competing for attention.

**`button-ghost`** — A text-only button with no background or border, used in navigation dropdowns and as "Cancel" or "Skip" actions. On hover, it gains a subtle background tint (rgba(53, 19, 82, 0.08)) for affordance without adding visual weight.

**`button-pill-mint`** — A fully rounded pill button in the brand's accent mint (#02e49b), used for "Listen Now" badges on product cards and "New Release" tags. The mint against the dark violet creates a high-energy contrast that draws the eye. A sibling variant (`button-pill-amber`) uses #ff9900 for "Limited Offer" and "Sale" callouts.

### Cards
**`product-card`** — The primary content container for audiobook listings. A white card with a soft shadow, 12px rounded corners, and 16px internal padding. The card contains a square aspect-ratio image, the book title in {typography.title-sm}, the author name in muted {typography.caption}, and the price in bold {typography.price}. On hover, the shadow deepens to indicate interactivity. A mint badge (`product-card-badge`) overlays the top-right corner for "Exclusive" or "New" labels.

### Navigation
**`nav-bar`** — A fixed 64px bar filled with the brand's deep violet {colors.primary}. Navigation links use white text at 15px with medium weight. The active link is underlined with a 2px mint border, creating a clear wayfinding signal. Inactive links sit at 80% opacity. The search bar lives within the nav on desktop, expanding to full width on mobile.

### Forms
**`text-input`** — A standard input field with a white background, 1px gray border, and 8px rounded corners. On focus, the border thickens to 2px and shifts to the brand violet. Error states swap the border to #ea4434 (red) with an accompanying error message in the same color. The search variant (`search-bar`) uses fully rounded corners and slightly larger padding for a more inviting feel.

### Footer
**`footer`** — A dark section using {colors.ink} (#13101a) as background, with muted gray text (#a6a6a6) for links and body copy. Links lighten to white on hover. The footer is divided into columns for "About," "Help," "Categories," and "Social" links, with a copyright line at the bottom.

### Badges
**`badge-mint`**, **`badge-amber`**, **`badge-pink`** — Small uppercase labels used to tag products with status or promotion. Mint signals "New" or "Exclusive," amber signals "Sale" or "Limited," and pink signals "Trending" or "Staff Pick." All badges use 11px bold uppercase text with tight padding and 4px rounded corners.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product cards go single-column; hero text reduces to {typography.display-lg}; search bar moves to a collapsible drawer; footer stacks vertically |
| Tablet | 744–1128px | Nav shows 4-5 links; product cards in 2-column grid; hero maintains {typography.display-xl} but reduces padding; footer shows 2-column layout |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero at full height with side-by-side text and illustration; footer in 4-column layout |
| Wide | > 1440px | Max-width container (1440px) centered; product cards in 4-column grid; hero may include additional decorative elements |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target size
- Product cards have a minimum tap area of 120x120px for the entire card surface
- Category pills are 36px tall with 16px horizontal padding, ensuring comfortable tapping
- Icon buttons are 40x40px circles, exceeding the 44px recommendation for critical actions

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-in drawer for links
- Search bar collapses from a full input to an icon button on mobile, expanding to full-width on tap
- Product card grid reduces columns from 4 to 1 as viewport shrinks
- Footer columns stack vertically below 744px, with accordion-style expandable sections for link groups
- Category pill strip becomes horizontally scrollable on mobile, with a "See All" link at the end

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list contains 30+ colors, many of which are likely third-party widget colors (Shopify Pay, Klarna, Afterpay, social icons) — the true brand palette is estimated at 8-10 colors, but exact brand-specific secondary colors beyond violet, mint, amber, and pink are uncertain
- No meta theme-color was extracted — the browser chrome color is unknown
- Font-family declarations returned only "inherit, serif" — the actual font stack is inferred as Georgia for body and Helvetica Neue for UI, but the brand may use a custom serif or a specific system font stack
- Hover states for most components are inferred from common patterns, not extracted from live CSS
- Error states (form validation, 404 pages, empty states) are not documented from the live site
- Dark mode support is unknown — the brand may or may not have a dark theme
- Animation and transition timings (hover transitions, page load animations, skeleton screens) are not extracted
- Specific spacing values for grid gaps, section margins, and component internal padding are estimated from common patterns
- The brand's logo and icon system (favicon, app icon, social media assets) is not documented
- Checkout flow styling (cart, payment forms, order confirmation) is not captured — these may use Shopify's default styling
