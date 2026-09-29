---
version: alpha
name: "Ojook"
source_url: "https://ojookcare.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Ojook is a clean, conscientious oral-care brand that turns daily brushing into a ritual rather than a chore. The palette centers on a confident primary blue (`#147bbb`) that reads as fresh and clinical without feeling cold — it appears across buttons, links, and key accents, often paired with a warm coral (`#ff9579`) that softens the experience and signals the brand's friendly, approachable tone. The canvas is a near-white (`#f4f4f6`) with subtle warmth, while surfaces use soft grays (`#f7f7f8`, `#e5e5eb`) for cards and containers. Ink is a deep charcoal (`#303030`) for body text, with muted tones (`#676986`, `#9a9db1`) for secondary information and hairline borders (`#e0e0e0`, `#dddddd`). A secondary blue (`#006fcf`) provides hover states and active links, while a deep navy (`#272d45`) anchors the footer and darker sections. The brand also employs a minty teal (`#b2f9e9`) and a vibrant green (`#00caaa`) for badges, sustainability callouts, and eco-friendly messaging. Typography relies on `acumin` as the primary sans-serif, supported by system fallbacks (`-apple-system`, `Roboto`, `Helvetica Neue`), and a `PT Serif` for editorial moments. Buttons are softly rounded (`{rounded.sm}`), cards use gentle radii (`{rounded.md}`), and the overall feel is one of thoughtful, approachable minimalism — a brand that takes oral health seriously but never sternly.

colors:
  primary: "#147bbb"
  primary-active: "#006fcf"
  primary-disabled: "#dcebf5"
  ink: "#303030"
  body: "#272d45"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#e0e0e0"
  hairline-soft: "#e5e5eb"
  canvas: "#f4f4f6"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-coral: "#ff9579"
  accent-teal: "#b2f9e9"
  accent-green: "#00caaa"
  footer-bg: "#272d45"
  footer-text: "#d3d4dd"
  error: "#c8232c"
  star-rating: "#ff9579"
  badge-new: "#00caaa"
  badge-sale: "#ff9579"
  social-facebook: "#4469af"
  social-twitter: "#00aced"

typography:
  display-xl:
    fontFamily: "'acumin', -apple-system, 'Roboto', 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'acumin', -apple-system, 'Roboto', 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'acumin', -apple-system, 'Roboto', 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'acumin', -apple-system, 'Roboto', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'acumin', -apple-system, 'Roboto', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'acumin', -apple-system, 'Roboto', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'acumin', -apple-system, 'Roboto', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'acumin', -apple-system, 'Roboto', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'acumin', -apple-system, 'Roboto', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'acumin', -apple-system, 'Roboto', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'acumin', -apple-system, 'Roboto', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'acumin', -apple-system, 'Roboto', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'acumin', -apple-system, 'Roboto', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  editorial:
    fontFamily: "'PT Serif', 'Georgia', 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.7
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    color: "{colors.primary}"
  nav-link-inactive:
    color: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
  product-card-compare-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    textDecoration: line-through
  badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    borderColor: "{colors.hairline}"
  search-bar-focus:
    borderColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section}"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.on-primary}"
  social-icon:
    color: "{colors.footer-text}"
    size: 24px
  social-icon-hover:
    color: "{colors.primary}"
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    padding: "{spacing.base} {spacing.lg}"
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Subscribe", and key conversion points. Rendered in the brand's signature blue (`{colors.primary}`) with white text and a soft 8px radius (`{rounded.sm}`). On hover, shifts to a deeper blue (`{colors.primary-active}`). Disabled state uses a pale blue (`{colors.primary-disabled}`) with muted text. Uppercase label with 0.5px letter-spacing reinforces the clean, intentional brand voice.

**`button-secondary`** — An outlined variant used for secondary actions like "Learn More" or "View Details". Features a transparent background with the primary blue text and a 1px border. On hover, fills with the primary blue and white text. Maintains the same uppercase typography and 8px radius as the primary button for visual consistency.

**`button-ghost`** — A text-only button for tertiary actions within cards or content areas. No background or border, just the primary blue text. Used for "Read Reviews" or "See All" links where a full button would be too heavy.

**`button-pill`** — A fully rounded pill button used for filters, tags, and compact CTAs in mobile navigation or search overlays. Smaller typography (`{typography.button-sm}`) and tighter padding make it suitable for dense layouts.

### Cards
**`product-card`** — The core product display component, featuring a rounded image area and structured text layout. The card itself has a white background with a 12px radius (`{rounded.md}`) and subtle shadow. The title uses `{typography.title-sm}` in `{colors.ink}`, while the price sits below in `{typography.body-md}`. A compare-at price appears in `{colors.muted}` with strikethrough when a sale is active. Badges overlay the top-left corner of the image for "New" or "Sale" indicators.

**`testimonial-card`** — A review or quote card with a white background, 12px radius, and 24px padding. Features a star rating in the coral accent (`{colors.star-rating}`) and body text in `{typography.body-sm}`. Used on product pages and the homepage social proof section.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with a near-white canvas background (`{colors.canvas}`). Logo sits left-aligned, with navigation links in uppercase `{typography.nav-link}`. Active links use the primary blue, inactive links use muted gray. On scroll, a subtle bottom border appears. Mobile collapses to a hamburger menu with a full-screen overlay drawer.

**`footer`** — A dark navy (`{colors.footer-bg}`) footer section with light gray text (`{colors.footer-text}`). Contains link columns, social media icons, and a newsletter signup. Links use `{typography.link}` and turn white on hover. Social icons are 24px and shift to the primary blue on hover.

### Forms
**`text-input`** — Standard text input for forms, newsletter signup, and search. White background with a light gray border (`{colors.hairline}`), 8px radius, and 48px height. On focus, the border shifts to the primary blue. Error state uses a red border (`{colors.error}`). Placeholder text uses `{colors.muted}`.

**`search-bar`** — A fully rounded pill-shaped search input used in the header and mobile navigation. White background with a subtle border, 48px height, and 20px horizontal padding. On focus, the border highlights in primary blue. Includes a magnifying glass icon in `{colors.muted}`.

### Badges
**`badge`** — Small, uppercase labels used for product flags. The default badge uses the mint teal (`{colors.accent-teal}`) for "New" or "Eco-Friendly" indicators. The sale variant uses the coral accent (`{colors.accent-coral}`) for "Sale" or "Limited Edition". Both have 4px radius and tight 4px 8px padding.

### Accordion
**`accordion`** — Expandable content panels used on product pages for descriptions, ingredients, and shipping details. White background with a light gray border and 8px radius. Headers use `{typography.title-sm}` with a chevron icon that rotates on open. Content area has 16px 24px padding with body typography.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger navigation, stacked product cards, full-width hero, reduced padding |
| Tablet | 744–1128px | Two-column product grid, visible top nav links, 32px section padding |
| Desktop | 1128–1440px | Three-column product grid, full navigation, 64px section padding, multi-column footer |
| Wide | > 1440px | Max-width container at 1440px, centered content, expanded whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44x44px touch target
- Product card CTAs are at least 48px tall
- Mobile navigation links have 48px tap areas
- Accordion headers are 48px tall for easy tapping
- Social icons in footer are 44x44px with adequate spacing

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Multi-column footer collapses to single column below 744px
- Product grid shifts from 3 columns to 2 at tablet, to 1 at mobile
- Hero section reduces heading size and stacks CTA buttons vertically on mobile
- Accordion content is collapsed by default on all breakpoints
- Search bar collapses to icon-only on mobile, expanding on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for secondary and ghost buttons could not be fully extracted — assumed standard fill/color inversion
- Error state styling for text inputs (icon, message placement) not observed — used standard red border
- Dark mode preferences not detected — no `prefers-color-scheme` media queries found
- Sub-brand or collection-specific palettes (e.g., whitening vs. sensitivity lines) not identified
- Loading states (skeleton screens, spinners) not observed
- Dropdown menu styling for navigation (mega menu vs. simple dropdown) not confirmed
- Modal/dialog overlay styling (backdrop opacity, close button placement) not extracted
- Tooltip and popover styling not present on the site
- Form validation message styling (success, warning) not observed
- Animation timing and easing curves not extracted from CSS
- Print stylesheet not reviewed
- Accessibility focus indicators (outline styles) not confirmed in extracted CSS
