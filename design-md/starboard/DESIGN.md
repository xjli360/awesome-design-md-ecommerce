---
version: alpha
name: "Starboard"
source_url: "https://sup.star-board.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-energy watersports brand that uses #fdbc00 — a sharp, almost solar-flare yellow — as its primary voltage, appearing across product badges, sale tags, and the signature "SHOP NOW" button that anchors every product grid. The brand has been building boards since 1994, and the design system carries that legacy through a surprisingly restrained palette: a near-black ink (#191a1d) for headlines, a warm gray body (#464646), and a generous white canvas (#f5f5f5) that lets product photography — shots of windsurfing rigs slicing through turquoise water or SUP boards resting on sand — do the heavy lifting. Montserrat runs at 600–700 weight for display headings, giving the brand a sporty, condensed feel that reads fast at a glance, while Open Sans handles body copy at 400 weight for readability. The system uses a single bright accent (#00aeef) for secondary CTAs and informational badges, creating a clear visual hierarchy: yellow means "act now," blue means "learn more." Product cards use soft 12px corners ({rounded.md}) and a subtle surface card (#ffffff) lifted off the canvas with a thin hairline (#e6e6e6), while the top navigation stays fixed with a full-width white bar and a bold yellow search icon. The brand trusts its action photography and bold color blocking over decorative flourishes — there are no gradients, no shadows, no ornamental borders. Every design decision points toward clarity and speed, matching the experience of being on the water: direct, responsive, and built for movement.

colors:
  primary: "#fdbc00"
  primary-active: "#e0a800"
  primary-disabled: "#fde48a"
  ink: "#191a1d"
  body: "#464646"
  muted: "#696969"
  muted-soft: "#8a8a8a"
  hairline: "#e6e6e6"
  hairline-soft: "#ececec"
  canvas: "#f5f5f5"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#191a1d"
  accent-blue: "#00aeef"
  accent-red: "#fa4238"
  accent-green: "#05d92d"
  sale-red: "#dd2c00"
  badge-new: "#1c64f6"
  badge-sale: "#dd2c00"
  footer-bg: "#191a1d"
  footer-text: "#f8f8f8"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 26px
    height: 44px
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-sticky:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.sale-red}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-accent:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.primary}"
    borderWidth: 2px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  category-nav:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    height: 48px
  category-nav-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in a bold yellow (#fdbc00) with dark text (#191a1d) for high contrast. On hover, the background shifts to `{colors.primary-active}` (#e0a800). The disabled state uses `{colors.primary-disabled}` (#fde48a) with muted text. All buttons use Montserrat at 14px, uppercase, 600 weight, with 0.5px letter spacing for a sporty, action-oriented feel.

**`button-secondary`** — A white button with dark text, used for secondary actions like "View Details" or "Learn More." Maintains the same typography and padding as the primary button but sits on the white canvas, creating a clean, minimal alternative.

**`button-outline`** — A transparent button with a dark border and text, used for tertiary actions. The border is 1.5px solid `{colors.ink}`. On hover, the background fills with `{colors.ink}` and text inverts to white.

**`button-accent-blue`** — A blue variant (#00aeef) with white text, used for informational CTAs like "Read Reviews" or "See Specs." This creates a clear visual distinction from the yellow primary — yellow means "buy now," blue means "explore."

### Cards
**`product-card`** — The core product display unit, a white card with 12px rounded corners ({rounded.md}) and a thin 1px hairline (#e6e6e6). The card contains a product image (rounded top corners), the product title in `{typography.title-sm}`, the price in `{typography.title-sm}`, and optional badges. On hover, the card lifts with a subtle box-shadow (0 4px 12px rgba(0,0,0,0.08)). Sale prices render in `{colors.sale-red}` (#dd2c00).

### Navigation
**`nav-bar`** — A fixed 64px white bar spanning the full viewport width. Navigation links use Montserrat 13px uppercase, 600 weight, with 0.3px letter spacing. The brand logo sits left-aligned, the primary nav links center-aligned, and the search icon (a yellow circle) right-aligned. On scroll, the bar gains a subtle 2px shadow.

**`category-nav`** — A secondary 48px navigation strip below the main nav, used for product category filtering (e.g., Windsurf, SUP, Foil). Active categories are underlined with a 2px yellow border. Inactive categories render in `{colors.muted}` (#696969).

### Badges
**`badge-new`** — A small blue (#1c64f6) pill badge with white uppercase text, used to flag newly released products. Rendered at 11px with 0.5px letter spacing.

**`badge-sale`** — A red (#dd2c00) pill badge with white uppercase text, used for discounted items. Same typography and spacing as the new badge.

**`badge-accent`** — A blue (#00aeef) pill badge used for informational tags like "Best Seller" or "Award Winner."

### Forms
**`text-input`** — A standard 48px text input with 12px padding and 8px rounded corners. The default state has a 1px hairline border (#e6e6e6). On focus, the border switches to a 2px yellow (#fdbc00) stroke. Placeholder text uses `{colors.muted}` (#696969).

### Hero
**`hero-section`** — A full-width section with a background color of `{colors.canvas}` (#f5f5f5) and large display typography. The hero typically features a full-bleed product image with an overlay of yellow-accented text and a primary CTA button. The section uses 64px vertical padding and 24px horizontal padding.

### Footer
**`footer`** — A dark (#191a1d) full-width footer with white text (#f8f8f8). Links use Open Sans 14px at 400 weight. The footer contains three columns: brand info, customer service links, and social media icons. Social icons render in white with a yellow hover state.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces nav links, hero text reduces to 24px, buttons become full-width, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, nav links collapse to icon-only, hero uses 28px display text, category nav becomes horizontal scrollable |
| Desktop | 1128–1440px | Three-column product grid, full nav links visible, hero uses 36px display text, category nav shows all items |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero content centered with max-width 1200px |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Search bar is 44px tall with 20px horizontal padding for comfortable tapping
- Category nav items have 48px touch targets with 12px padding
- Product card images link to product pages with a minimum 200px tap area

### Collapsing Strategy
- Main navigation collapses to a hamburger menu below 744px, with a slide-out drawer containing all nav links and search
- Category navigation becomes a horizontal scrollable strip below 744px, with arrow indicators for overflow
- Product grid collapses from 4 columns to 1 column on mobile, with full-width cards
- Footer columns stack vertically below 744px, with accordion-style expandable sections for links
- Hero section reduces padding from 64px to 32px on mobile, with text overlay moving below the image

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list includes several framework-default blues (#007aff, #1c64f6) and checkout-widget colors that may not be part of the brand's core palette — the true primary is #fdbc00 (yellow), which is the most distinctive and brand-specific color in the list
- Hover and active states for buttons and links were inferred from common patterns, not extracted from the live site
- Typography scale (font sizes, weights, line heights) was estimated based on common Montserrat/Open Sans pairings and typical e-commerce patterns — exact values may differ from the live site
- Box shadows, gradient overlays, and transition durations were not extractable from the static HTML/CSS
- Error states for form inputs (validation colors, error messages) were not observed
- Dark mode is not supported — the site appears to be light-mode only
- The brand may use additional accent colors for seasonal campaigns or sub-brand lines (e.g., Starboard Foil, Starboard SUP) that were not captured
- Iconography style (line vs. filled, stroke weights) was not extractable
- The "swiper-icons" font-family declaration suggests a slider/carousel component, but its styling details are unknown
