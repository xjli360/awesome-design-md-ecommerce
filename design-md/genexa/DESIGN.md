---
version: alpha
name: "Genexa"
source_url: "https://genexa.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A clean-medicine brand that wears its clinical credibility like a white coat — the palette runs almost entirely on a grayscale axis from #0f0f0f to #f2f2f2, with two sharp accent voltages: a medical-blue #4d5bcd that appears on primary CTAs and ingredient callouts, and a warm-terracotta #ec523e reserved for sale badges, price drops, and urgency signals. The typography stack splits between TT Norms Pro (a geometric sans-serif with precise, almost pharmaceutical letterforms) for headings and body copy, and GalaxieCopernicus Book Italic — an unexpected serif italic used sparingly for pull-quotes or ingredient-story moments, lending a rare note of editorial warmth. Buttons use {rounded.sm} corners (8px) rather than pills, reinforcing a trustworthy, non-gimmicky feel — this is medicine, not a toy. The canvas is #ffffff, but the brand's true surface language is a layered gray: #f1efeb for soft cards, #dedede for dividers, and #d1d1d1 for disabled states. Product cards sit on {surface-card} with a subtle {hairline} border, and the hero section often uses a full-bleed image with a dark scrim (#121212 at 40%) and white text — a clean, confident, doctor's-office-meets-modern-DTC aesthetic. The overall mood is honest, minimal, and slightly serious, with the accents doing all the emotional work.

colors:
  primary: "#4d5bcd"
  primary-active: "#3a47b0"
  primary-disabled: "#b0b8e6"
  ink: "#0f0f0f"
  body: "#262428"
  muted: "#757575"
  muted-soft: "#969696"
  hairline: "#d1d1d1"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f1efeb"
  surface-card: "#ffffff"
  surface-warm: "#dcd7cd"
  on-primary: "#ffffff"
  accent-sale: "#ec523e"
  accent-warm: "#eb9247"
  scrim: "#121212"
  border-strong: "#202020"

typography:
  display-xl:
    fontFamily: "'TT Norms Pro Bold', 'Montserrat', sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'TT Norms Pro Bold', 'Montserrat', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'TT Norms Pro Bold', 'Montserrat', sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'TT Norms Pro Bold', 'Montserrat', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'TT Norms Pro Regular', 'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'TT Norms Pro Regular', 'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'TT Norms Pro Regular', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'TT Norms Pro Regular', 'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'TT Norms Pro Bold', 'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'TT Norms Pro Bold', 'Montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'TT Norms Pro Bold', 'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'TT Norms Pro Regular', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'TT Norms Pro Bold', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge:
    fontFamily: "'TT Norms Pro Bold', 'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  italic-quote:
    fontFamily: "'GalaxieCopernicus-BookItalic', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    fontStyle: italic

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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  text-input-error:
    border: "2px solid {colors.accent-sale}"
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(15,15,15,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: 16px
  product-card-hover:
    boxShadow: "0 4px 16px rgba(15,15,15,0.1)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm}"
    height: 200px
    objectFit: cover
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: absolute
    top: 8px
    left: 8px
  hero-section:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  hero-overlay:
    backgroundColor: "rgba(18,18,18,0.4)"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    marginTop: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    hoverColor: "{colors.canvas}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-certified:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
  accordion-header:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    padding: "0 {spacing.lg} {spacing.base}"
  ingredient-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    borderLeft: "4px solid {colors.primary}"
  ingredient-callout-icon:
    width: 48px
    height: 48px
    rounded: "{rounded.full}"
    backgroundColor: "{colors.primary}"
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  testimonial-quote:
    typography: "{typography.italic-quote}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.base}"
  testimonial-author:
    typography: "{typography.caption-bold}"
    textColor: "{colors.muted}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.lg} 0"
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.base} 0"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheader:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xl}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using the medical-blue #4d5bcd background with white text. On hover, it shifts to a slightly darker #3a47b0. The disabled state uses a lighter blue #b0b8e6. All primary buttons use {rounded.sm} (8px) corners and bold 15px type with 0.5px letter spacing for a precise, clinical feel. Height is 48px with 14px/28px padding.

**`button-secondary`** — An outlined variant with a white background, blue text, and a 2px solid blue border. Used for secondary actions like "Learn More" or "View Details". Active state darkens the border and text while adding a soft gray background. Same 48px height as primary for alignment.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "Skip". Hover state adds a subtle background tint. Uses the same typography and height as primary buttons for consistency.

**`button-sale`** — A smaller, urgent button using the terracotta #ec523e accent. Used exclusively for sale/promotional CTAs like "Shop Sale" or "Save Now". Height is 40px with tighter padding, using the smaller button typography.

### Cards
**`product-card`** — The core product display unit, a white card with a 1px soft hairline border and 12px rounded corners. Contains a product image (200px tall, 8px rounded), title in 18px semibold, and price in 16px regular. On hover, the card gains a subtle shadow and the border darkens. A sale badge (terracotta) can be positioned absolutely at the top-left.

**`testimonial-card`** — A soft gray (#f1efeb) card with a 1px hairline border and 12px rounded corners. Features an italic quote from the GalaxieCopernicus font stack, followed by the author's name in bold caption type. Used for customer reviews and ingredient testimonials.

**`ingredient-callout`** — A soft gray card with a 4px blue left border accent. Contains an icon (48px blue circle) and body text. Used to highlight specific clean ingredients or certifications. The blue left border creates a visual anchor that ties back to the primary brand color.

### Navigation
**`nav-bar`** — A 72px white header with a 1px soft bottom border. Contains the logo on the left, navigation links in the center, and utility icons (search, cart, account) on the right. On scroll, the border is replaced by a subtle shadow. The nav uses 14px bold type with 0.3px letter spacing.

**`nav-link`** — Individual navigation items with 8px/16px padding. Active state shows the primary blue text color with a 2px blue bottom border. Inactive links use the dark ink color.

### Forms
**`text-input`** — A 48px tall input field with white background, 8px rounded corners, and a 1px hairline border. On focus, the border becomes 2px solid primary blue. Error state uses a 2px terracotta border. Padding is 12px/16px with 16px body type.

**`search-bar`** — A pill-shaped (full rounded) search input, 48px tall, with white background and 1px hairline border. On focus, the border becomes 2px primary blue. Used in the header and on search result pages.

### Badges
**`badge-new`** — A small blue badge with white text, 4px rounded corners, and 2px/6px padding. Used to indicate new products or ingredients.

**`badge-sale`** — A small terracotta badge with white text, same dimensions as the new badge. Used for sale items and promotions.

**`badge-certified`** — A warm beige (#dcd7cd) badge with dark text, slightly larger padding (4px/8px). Used for certifications like "USDA Organic" or "Non-GMO Verified".

### Footer
**`footer`** — A dark (#0f0f0f) footer with white text, 48px padding on top/bottom and 32px on sides. Links use the muted gray (#969696) color and turn white on hover. Contains columns for company info, support, and legal links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger menu replaces nav links, product cards stack vertically, hero section reduces to 320px min-height, buttons become full-width, font sizes scale down one step |
| Tablet | 744–1128px | Two-column product grid, nav links collapse into hamburger, hero maintains 400px min-height, side-by-side layout for ingredient callouts |
| Desktop | 1128–1440px | Full nav bar visible, three-column product grid, hero at 480px min-height, multi-column footer |
| Wide | > 1440px | Max-width container at 1440px, centered content, hero can expand to 560px with larger imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets are the full card surface area
- Accordion headers are 48px minimum height for easy tapping
- Nav links in mobile menu are 48px tall with 16px padding

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-in drawer
- Product grids collapse from 3 columns (desktop) to 2 (tablet) to 1 (mobile)
- Multi-column footer collapses to a single column with accordion-style sections
- Hero section reduces image height and stacks text/CTA vertically
- Ingredient callouts shift from side-by-side to stacked layout
- Search bar in header collapses to an icon that expands on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: While some hover behaviors are inferred (button darkening, card shadows), exact transition durations and easing curves could not be extracted from static analysis
- **Error states**: Form validation styling (error messages, success states) beyond the error border color is not documented
- **Dark mode**: No evidence of a dark mode variant in the extracted data
- **Sub-brand palettes**: Genexa may have product-line-specific colors (e.g., Kids, Adult, Pet) that were not captured
- **Animation system**: No extracted data on micro-interactions, page transitions, or loading states
- **Typography scale**: Exact font sizes for all 12+ text styles are inferred from common patterns; the live site may use additional sizes
- **Spacing system**: The spacing scale is a standard 4px grid assumption; actual spacing may vary by component
- **Iconography**: No extracted data on icon style, stroke weight, or sizing conventions
- **Color contrast**: Accessibility ratios for text-on-background combinations have not been verified against WCAG standards
- **Checkout flow**: Shopify checkout styling (which may differ from the main site) was not captured
- **Print styles**: No print-specific CSS was extracted
- **Focus states**: Keyboard focus indicators were not captured in the extraction
