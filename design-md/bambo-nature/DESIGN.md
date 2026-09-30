---
version: alpha
name: "Bambo Nature"
source_url: "https://bambonatureusa.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A Scandinavian baby-care brand that wraps its products in a warm, earthy palette anchored by a deep, confident blue (#006fcf) and a soft, creamy canvas (#fbf9f4), creating a visual language that feels both clinical and comforting. The brand’s voice is gentle but direct, using Maven Pro for clean, readable body text and the hand-drawn Learning Curve script for accent moments that whisper “natural” and “handmade.” The signature orange (#f48120) appears as a deliberate accent — not as a primary CTA voltage but as a warmth signal on badges, sale markers, and secondary highlights, like a sunbeam breaking through a Nordic forest canopy. Product imagery is treated with generous whitespace and soft, pill-shaped cards (`{rounded.full}`), while the navigation stays minimal — a simple white bar with the logo centered and a thin, muted hairline (`{colors.hairline}`) separating it from the hero. The overall feeling is one of quiet trust: the blue says “safe,” the cream says “clean,” and the orange says “alive.” Buttons are softly rounded (`{rounded.sm}`) and use the primary blue for high-confidence actions, while secondary actions use a transparent or outline style. The footer is dense with links, organized in a three-column grid on desktop, collapsing to a single column on mobile, with a soft gray background (`{colors.surface-soft}`) that grounds the page without competing with the hero imagery. The brand’s sustainability messaging is woven into the design through small leaf icons and earthy tones like #6bbbae (a muted sage) and #809687 (a warm olive), used sparingly in badges and category tags. The overall impression is of a brand that doesn’t shout — it leans in, speaks softly, and lets the product do the talking.

colors:
  primary: "#006fcf"
  primary-active: "#005a9e"
  primary-disabled: "#b3d4f0"
  ink: "#231f20"
  body: "#242833"
  muted: "#5f6368"
  muted-soft: "#c4c4c4"
  hairline: "#dedede"
  hairline-soft: "#f1f1f1"
  canvas: "#fbf9f4"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#f48120"
  accent-orange-active: "#d4602c"
  accent-sage: "#6bbbae"
  accent-olive: "#809687"
  accent-lavender: "#9b7793"
  accent-stone: "#463729"
  star-rating: "#fbbc04"
  error: "#eb001b"
  success: "#34a853"

typography:
  display-xl:
    fontFamily: "'Maven Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Maven Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Maven Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Maven Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Maven Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Maven Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Maven Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Maven Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Maven Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Maven Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Maven Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Maven Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Maven Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  script-accent:
    fontFamily: "'Learning Curve', cursive"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
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
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 38px
  button-accent-orange-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.accent-orange}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    textColor: "{colors.body}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.md}"
  badge-new:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-eco:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  star-rating:
    color: "{colors.star-rating}"
    size: "16px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the brand’s deep blue (#006fcf) on a white background. On hover, it darkens to `{colors.primary-active}` (#005a9e). The disabled state uses a pale blue `{colors.primary-disabled}` (#b3d4f0) with white text. All primary buttons have a soft 8px radius (`{rounded.sm}`) and use `{typography.button-md}` for clear, confident copy.

**`button-secondary`** — An outlined variant with a white fill and a 2px solid blue border. On hover, the fill becomes the primary blue and text flips to white. Used for “Learn More” and “View Details” actions where the primary button would be too heavy.

**`button-accent-orange`** — A smaller, warmer button using the brand’s signature orange (#f48120). Used for sale badges, limited-time offers, and secondary CTAs in product cards. The active state deepens to `{colors.accent-orange-active}` (#d4602c).

### Cards
**`product-card`** — A white card with a 12px radius (`{rounded.md}`) and 16px padding. The product image sits inside with a softer 8px radius (`{rounded.sm}`) and a 1:1 aspect ratio. Price is set in `{typography.title-sm}` in the ink color, while sale prices switch to `{colors.accent-orange}`. Badges (new, eco, sale) are pill-shaped (`{rounded.full}`) and sit at the top-left of the image.

### Navigation
**`nav-bar`** — A fixed 72px white bar with the logo centered. Navigation links are uppercase, 14px, weight 500, with 0.5px letter spacing. The active link uses the primary blue. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

### Forms
**`text-input`** — A clean, white input with a 1px hairline border and 8px radius. On focus, the border thickens to 2px and turns primary blue. Height is 44px with 12px vertical and 16px horizontal padding.

### Footer
**`footer-section`** — A soft gray background (`{colors.surface-soft}`) with three columns of links on desktop. Each column has a `{typography.title-sm}` heading with 16px bottom margin. Links are 14px body weight, turning blue on hover. The section has 64px vertical padding.

### Badges
**`badge-new`**, **`badge-eco`**, **`badge-sale`** — Small, pill-shaped badges with uppercase 11px text. The “new” and “sale” badges use the accent orange, while the “eco” badge uses the muted sage (#6bbbae). All have 2px vertical and 8px horizontal padding.

### Category Tags
**`category-tag`** — Pill-shaped tags with a soft gray background and 12px caption text. The active state fills with primary blue and white text. Used in filter strips and category navigation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; footer collapses to single column; hero text reduces to `{typography.display-lg}`; search bar becomes full-width |
| Tablet | 744–1128px | Two-column product grid; nav remains horizontal but links may truncate; footer shows two columns; hero maintains `{typography.display-xl}` but with reduced padding |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; three-column footer; hero has maximum whitespace |
| Wide | > 1440px | Max-width container (1440px) centered; all layouts scale proportionally; extra whitespace on sides |

### Touch Targets
- All buttons and links have a minimum touch target of 44x44px
- Product card images have a minimum tap area of 120x120px
- Category tags are at least 40px tall for easy tapping
- Quantity selector buttons are 44x44px minimum
- Accordion headers have 44px minimum tap height

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px
- Product grid collapses from 3 columns to 2 at tablet, then 1 at mobile
- Footer collapses from 3 columns to 2 at tablet, then 1 at mobile
- Hero section reduces vertical padding by 50% on mobile
- Search bar becomes full-width and moves below the hero on mobile
- Category tag strip becomes horizontally scrollable on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all interactive elements could not be fully extracted from the live site; the active states provided are best estimates based on common accessibility patterns
- Error states for form inputs (validation, error messages) were not observed on the live site
- Dark mode is not supported and no dark-mode color tokens were found
- The exact font weights and sizes for Maven Pro and Learning Curve were inferred from common usage patterns; the live site may use different weights
- The brand’s sub-brand or promotional color palettes (e.g., holiday, seasonal) were not observed
- The exact spacing and padding values for components were estimated from common e-commerce patterns; the live site may use different values
- The script accent font (Learning Curve) was found in the CSS but its usage context (headings, quotes, badges) is inferred
- The brand’s iconography style (line weight, fill, color) was not extracted
- The checkout flow (Shopify) uses its own design system and is not covered here
- The brand’s animation and transition timing values were not extracted
- The brand’s print or packaging design system is not reflected in this digital design system
