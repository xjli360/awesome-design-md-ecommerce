---
version: alpha
name: "Ghost Lifestyle"
source_url: "https://ghostlifestyle.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A dark, high-contrast supplement brand that wraps gym culture in streetwear attitude, anchored on a near-black canvas (#121212) and a single electric-blue accent (#007aff) that fires across every CTA, badge, and interactive element. The brand’s tagline — “BE SEEN BEYOND THE WALLS OF THE GYM” — is not decorative; it’s the design thesis. Ghost runs a condensed, muscular type system built on futura-pt-condensed for display headers and Roboto for body, creating a typographic tension between compressed power and readable utility. The palette is deliberately sparse: a light gray (#dedede) for body text against the dark canvas, with the blue serving as the only color voltage. There are no gradients, no secondary warm tones, no pastels — the brand trusts pure black, pure white, and that single blue to carry all emotional weight. Product cards use hard corners (`{rounded.none}`) and tight padding, while buttons and badges lean into pill shapes (`{rounded.full}`) for a streetwear-meets-performance feel. The Shopify-powered checkout introduces third-party widget colors (Klarna, Afterpay) that sit outside the brand system, creating a visual break between the curated Ghost experience and the transactional layer. Ghost’s design is not friendly — it’s confrontational, gym-floor direct, with every pixel earning its place against the dark.

colors:
  primary: "#007aff"
  primary-active: "#0066d6"
  primary-disabled: "#4da3ff"
  ink: "#121212"
  body: "#dedede"
  muted: "#9e9e9e"
  muted-soft: "#757575"
  hairline: "#2a2a2a"
  hairline-soft: "#1e1e1e"
  canvas: "#121212"
  surface-soft: "#1a1a1a"
  surface-card: "#1e1e1e"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-light: "#121212"
  accent-blue: "#007aff"
  badge-new: "#007aff"
  star-rating: "#dedede"
  error: "#ff3b30"
  success: "#34c759"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'futura-pt-condensed', 'Futura PT Condensed', 'Arial Narrow', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'futura-pt-condensed', 'Futura PT Condensed', 'Arial Narrow', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'futura-pt-condensed', 'Futura PT Condensed', 'Arial Narrow', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'futura-pt-condensed', 'Futura PT Condensed', 'Arial Narrow', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'futura-pt-condensed', 'Futura PT Condensed', 'Arial Narrow', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
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
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
    opacity: 0.5
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.body}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 8px 0
    height: auto
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
    height: 100%
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
    height: 100%
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px {spacing.base}"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px {spacing.base}"
    height: 40px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px {spacing.base}"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px {spacing.base}"
    height: 44px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px {spacing.base}"
    height: 44px
    border: "1px solid {colors.error}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px {spacing.sm}"
    height: 20px
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px {spacing.sm}"
    height: 20px
    border: "1px solid {colors.primary}"
  badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px {spacing.sm}"
    height: 20px
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 48px
    marginTop: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
    padding: "{spacing.xs} 0"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.link}"
    padding: "{spacing.xs} 0"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "4px"
    height: 36px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    height: 28px
    width: 28px
  accordion:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a pill-shaped button (`{rounded.full}`) in electric blue (`{colors.primary}`) with white uppercase Roboto text. On hover, it shifts to a deeper blue (`{colors.primary-active}`). The disabled state uses a lighter blue (`{colors.primary-disabled}`) at 50% opacity, signaling non-interactivity without breaking the brand’s color consistency. All primary buttons maintain a 44px height and 24px horizontal padding for comfortable thumb targeting on mobile.

**`button-secondary`** — An outlined variant for secondary actions, using a transparent background with a 1px hairline border (`{colors.hairline}`) and body-colored text. On hover, the background fills with `{colors.surface-soft}` and the border shifts to `{colors.body}`, creating a subtle elevation effect. This button lives alongside primary CTAs in cart drawers, filter bars, and modal footers.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "View details" or "Cancel". The button has zero padding on the sides and relies solely on its uppercase Roboto weight-700 typography to communicate clickability. Hover adds no background change — only the text color shifts to `{colors.primary}`.

**`icon-button`** — A 40x40px circular button used for cart icons, close modals, and mobile menu toggles. The default state is transparent; on hover, a `{colors.surface-soft}` background appears. The icon itself is rendered in `{colors.body}` and scales to 20x20px.

### Navigation
**`top-nav`** — A fixed 64px bar on `{colors.canvas}` with a 1px hairline bottom border. Navigation links use futura-pt-condensed at 16px uppercase weight-600, with 16px horizontal padding. The active state adds a 2px `{colors.primary}` bottom border and shifts the link text to blue. The nav collapses to a hamburger menu below 744px.

**`nav-link`** — Individual navigation items that fill the full 64px height of the top nav. Inactive links display in `{colors.body}`; active links switch to `{colors.primary}` with a 2px bottom border. The condensed typeface gives the nav a tight, athletic feel — each character earns its horizontal space.

### Cards
**`product-card`** — A hard-cornered (`{rounded.none}`) card on `{colors.surface-card}` with 16px padding. The product image occupies a 1:1 aspect ratio square with a `{colors.surface-soft}` background placeholder. Below the image, the title uses `{typography.title-sm}` in `{colors.body}`, and the price sits in `{colors.muted}` with 4px top margin. On hover, the entire card background shifts to `{colors.surface-soft}`, creating a subtle lift without shadows — Ghost avoids drop shadows entirely, preferring background color shifts for depth.

### Badges
**`badge`** — A small pill-shaped label (`{rounded.full}`) at 20px height, using `{colors.primary}` background with white uppercase 10px Roboto text. Used for "NEW", "BEST SELLER", and limited-edition flags. The outline variant (`{badge-outline}`) inverts the relationship — transparent background with a 1px blue border — for secondary labeling. A `{badge-sold-out}` variant uses `{colors.muted}` background for out-of-stock indicators.

### Forms
**`text-input`** — A standard input field with `{colors.surface-soft}` background, 1px hairline border, and `{rounded.sm}` corners. The 44px height matches button sizing for aligned form rows. On focus, the border switches to `{colors.primary}` and the background lightens to `{colors.surface-card}`. Error state uses `{colors.error}` (#ff3b30) for the border.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) at 40px height, using `{colors.surface-soft}` background with a 1px hairline border. On focus, the border shifts to `{colors.primary}` and the background becomes `{colors.surface-card}`. The search icon sits at the left edge in `{colors.muted}`.

### Footer
**`footer`** — A full-width section on `{colors.canvas}` with a 1px hairline top border. Links use `{typography.link}` in `{colors.muted}`, shifting to `{colors.body}` on hover. The footer is organized in a multi-column grid on desktop, collapsing to a single column on mobile. Social icons sit in `{colors.muted}` and shift to `{colors.primary}` on hover.

### Accordion
**`accordion`** — A border-bottom-only accordion with `{typography.title-sm}` in `{colors.body}` for the trigger. The content panel uses `{typography.body-sm}` in `{colors.muted}` with 16px bottom padding. No background or border-radius — the accordion is purely typographic, relying on the hairline divider for visual separation. Used for product descriptions, ingredient lists, and FAQ sections.

### Quantity Selector
**`quantity-selector`** — A pill-shaped control (`{rounded.full}`) at 36px height, using `{colors.surface-soft}` background. Contains two 28px circular buttons (minus/plus) flanking the quantity number in `{typography.body-md}`. Used in cart drawers and product detail pages for adjusting item count.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger; product cards go single-column; hero min-height reduces to 300px; footer links stack vertically; search bar moves to overlay |
| Tablet | 744–1128px | Top nav shows 4-5 links; product cards in 2-column grid; hero maintains 400px min-height; footer in 2-column layout |
| Desktop | 1128–1440px | Full top nav with all links; product cards in 3-4 column grid; hero at full height; footer in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero content centered with max-width 1200px |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for thumb targeting
- Icon buttons are 40x40px — slightly below the 44px ideal but acceptable for secondary controls
- Quantity selector buttons are 28x28px — the smallest touch target in the system, used only in cart context
- Search bar is 40px tall with 16px horizontal padding for comfortable tap area

### Collapsing Strategy
- Top nav links collapse to hamburger menu below 744px; the hamburger icon uses `{icon-button}` sizing
- Product grid collapses from 4 columns (desktop) to 2 columns (tablet) to 1 column (mobile)
- Footer collapses from 4 columns to 2 columns to single column stacked
- Search bar collapses from inline (desktop) to full-screen overlay (mobile) with auto-focus
- Accordion content is collapsed by default on all breakpoints, expanding on click

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex palette is sparse (only #dedede, #121212, #007aff) and may not represent the full brand system — secondary accents, error states, and hover colors are inferred from common patterns rather than extracted from the live site
- Font-family declarations found (Roboto, futura-pt-condensed, SourceSansPro) but exact font weights and sizes for each typography token are estimated from common usage — the live site may use different sizes or weights
- Hover states for buttons, cards, and links are inferred from common dark-theme patterns — actual hover transitions and animations could not be extracted
- Shopify checkout introduces third-party widget colors (Klarna pink, Afterpay black) that sit outside the brand system — these are not captured in the palette
- No dark mode variant is defined — the entire site is already dark-themed, so a light mode toggle would require a separate palette
- Error and success colors (#ff3b30, #34c759) are Apple system defaults — Ghost may use custom values
- Drop shadow values, transition durations, and animation easing curves could not be extracted
- Mobile navigation drawer styling (background, overlay, animation) could not be reliably determined
- Product card hover states may include image zoom or overlay effects not captured in the static extraction
- The extracted #007aff is a generic iOS blue — it may be a Shopify default rather than Ghost's intentional brand color, but it's the most distinctive accent in the palette and is treated as primary
