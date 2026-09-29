---
version: alpha
name: "Hero Cosmetics"
source_url: "https://www.herocosmetics.us"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand built for the acne-prone, Hero Cosmetics speaks in a warm, honest vernacular anchored on a creamy off-white canvas of {colors.canvas} (#fcfaf7) and a deep, almost-charcoal ink of {colors.ink} (#231f20). The palette is intentionally restrained—earthy neutrals like {colors.muted} (#42403a) and {colors.muted-soft} (#a29f9a) provide structure, while a soft gold {colors.primary} (#fadca9) serves as the brand's primary voltage, appearing in CTAs, badges, and product highlights. This is not a clinical, sterile skincare brand; it feels lived-in and approachable, with gentle accents of blush (#ffeaea), sage (#f4fbf7), and sky blue (#d0eaf7) that surface in ingredient callouts and educational modules. Typography leans on a dual system: the display faces are the elegant, hand-drawn BerettaSans (in Regular, Bold, and Light weights) and the quirky Etna-LightItalic, while body copy and buttons use the sturdy, geometric FuturaPT family (Book, Demi, Bold, Heavy). The result is a brand that feels both artisanal and trustworthy—like a friend who happens to be a dermatologist. Signature design moves include pill-shaped buttons ({rounded.full}), soft card corners ({rounded.md} ~12px), and generous whitespace that gives the skin-care routines room to breathe. The Shopify platform underpins a clean, conversion-focused layout where product cards use a subtle {colors.hairline} (#dedede) border and the primary CTA glows in {colors.primary} (#fadca9) against the warm canvas.

colors:
  primary: "#fadca9"
  primary-active: "#f9d79c"
  primary-disabled: "#f8eee1"
  ink: "#231f20"
  body: "#42403a"
  muted: "#42403a"
  muted-soft: "#a29f9a"
  hairline: "#dedede"
  hairline-soft: "#f5f4f0"
  canvas: "#fcfaf7"
  surface-soft: "#f5f4f0"
  surface-card: "#ffffff"
  on-primary: "#231f20"
  accent-blush: "#ffeaea"
  accent-sage: "#f4fbf7"
  accent-sky: "#d0eaf7"
  accent-warm: "#f8eee1"
  accent-lavender: "#e2e5f3"
  accent-mint: "#eaf5f3"
  accent-peach: "#f2f7f8"
  accent-stone: "#e2e2ea"
  accent-frost: "#eaf3f3"
  badge-gold: "#fadca9"
  badge-blue: "#1990c6"
  badge-blue-active: "#136f99"
  star-rating: "#231f20"
  error: "#ffeaea"
  success: "#eaf5f3"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'BerettaSans-Bold', 'FuturaPT-Heavy', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'BerettaSans-Bold', 'FuturaPT-Bold', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'BerettaSans-Regular', 'FuturaPT-Book', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'BerettaSans-Light', 'FuturaPT-Light', Georgia, serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'FuturaPT-Demi', 'FuturaPT-Bold', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'FuturaPT-Demi', 'FuturaPT-Bold', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  body-md:
    fontFamily: "'FuturaPT-Book', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'FuturaPT-Book', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'FuturaPT-Book', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'FuturaPT-Book', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'FuturaPT-Demi', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'FuturaPT-Demi', 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'FuturaPT-Demi', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'FuturaPT-Demi', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "'FuturaPT-Book', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'FuturaPT-Demi', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  italic-accent:
    fontFamily: "'Etna-LightItalic', 'FuturaPT-BookOblique', Georgia, serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0.2px
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill-gold:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: "1px solid {colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-badge:
    backgroundColor: "{colors.badge-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  product-badge-blue:
    backgroundColor: "{colors.badge-blue}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.base}"
  hero-headline:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheadline:
    typography: "{typography.display-sm}"
    color: "{colors.body}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "16px 40px"
  ingredient-badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  ingredient-badge-blush:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  ingredient-badge-sky:
    backgroundColor: "{colors.accent-sky}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    color: "{colors.canvas}"
    typography: "{typography.link}"
    textDecoration: none
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-body:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
  tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 44px
  add-to-cart-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "16px 32px"
    height: 56px
    boxShadow: "0 -2px 10px rgba(0,0,0,0.05)"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill-shaped button in the brand's signature gold {colors.primary} (#fadca9). Uses uppercase FuturaPT-Demi at 14px with 1px letter-spacing for a confident, editorial feel. On hover, shifts to {colors.primary-active} (#f9d79c); disabled state uses {colors.primary-disabled} (#f8eee1) with muted text. The full border-radius ({rounded.full}) is a defining brand gesture—no hard corners on CTAs.

**`button-secondary`** — An outlined variant on the warm canvas background, with a 2px solid {colors.ink} (#231f20) border. Maintains the same pill shape and typography as primary, but inverts the color relationship. Used for "Learn More" or secondary actions where the gold CTA would compete.

**`button-tertiary-text`** — A text-only button with no background or border, using {colors.ink} and the same uppercase Demi typography. Appears in navigation dropdowns and as "Skip" links in onboarding flows.

**`button-pill-gold`** — A smaller, compact version of the primary button (12px font, 10px vertical padding), used for in-card CTAs, filter tags, and quick-add actions. Same gold fill and pill shape.

**`button-pill-outline`** — A compact outlined pill with a 1px {colors.hairline} (#dedede) border. Used for secondary filter tags and "Compare" toggles.

### Cards
**`product-card`** — The core product display unit, a white card with soft {rounded.md} (12px) corners and a subtle {colors.hairline-soft} (#f5f4f0) border. On hover, the border deepens to {colors.hairline} (#dedede) and a gentle box-shadow lifts the card. The product image occupies the top with its own rounded top corners, creating a clean visual hierarchy. Typography uses {typography.body-sm} for product names and {typography.caption} for prices.

**`product-badge`** — A small gold pill badge overlaying product cards, using {typography.badge} (11px uppercase Demi). Used for "Best Seller," "New," or "Bundle & Save" labels. A blue variant ({colors.badge-blue} #1990c6) exists for clinical or dermatologist-recommended badges.

**`ingredient-badge`** — Small rectangular badges with soft {rounded.sm} (8px) corners, used in ingredient callout sections. Each badge has a pastel background (sage, blush, or sky) with dark text, creating a friendly, educational feel. The typography is {typography.caption-sm} (12px book weight).

### Navigation
**`top-nav`** — A fixed 72px navigation bar on the warm canvas background, with a single hairline border at the bottom. Navigation links use {typography.nav-link} (14px uppercase Demi) with a 2px underline on the active state. The bar contains the brand logo, product category links, a search icon, and a cart icon.

**`nav-link-active`** — Active navigation link with a 2px solid underline in {colors.ink}. The uppercase Demi typography gives the nav a structured, editorial feel.

**`nav-link-inactive`** — Inactive navigation links in {colors.muted} (#42403a), maintaining the same typography but without the underline.

### Forms
**`search-bar`** — A pill-shaped search input on {colors.surface-soft} (#f5f4f0) with a 1px {colors.hairline} border. On focus, the background shifts to white and the border thickens to 2px {colors.ink}. Uses {typography.body-sm} (14px Book) for placeholder text.

**`newsletter-input`** — A full-rounded email input for the footer, with white background and 1px hairline border. Paired with a dark {colors.ink} submit button in the same pill shape.

**`quantity-selector`** — A pill-shaped stepper control with plus/minus buttons flanking a numeric display. Uses {colors.surface-soft} background and {typography.body-md} for the quantity number.

### Footer
**`footer-section`** — A dark section with {colors.ink} (#231f20) background and white text. Contains link columns, social icons, and a newsletter signup. Links use {typography.link} with no underline by default, appearing as clean white text on the dark background.

### Hero
**`hero-section`** — The full-width brand introduction area, using the warm canvas background with generous {spacing.section} (64px) vertical padding. The headline uses {typography.display-xl} (48px BerettaSans-Bold) for maximum impact, while the subheadline uses {typography.display-sm} (24px BerettaSans-Light) for a softer, more inviting tone. The CTA is a large gold pill button.

### Tabs
**`tab-active`** — Active filter or category tab with a gold {colors.primary} background and pill shape. Uses {typography.button-sm} (12px uppercase Demi). Inactive tabs use {colors.surface-soft} background with muted text.

### Accordion
**`accordion-header`** — Expandable section headers for FAQs and product details, with {typography.title-sm} (16px Demi) and a bottom hairline border. The body uses {typography.body-sm} (14px Book) with additional padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack vertically; hero headline reduces to 32px; buttons become full-width; footer links stack; search bar moves to drawer |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links with "More" dropdown; hero uses 40px headline; side-by-side ingredient badges; accordion remains expanded by default |
| Desktop | 1128–1440px | Full top-nav with all links visible; three-column product grid; hero uses 48px headline; multi-column footer; search bar visible in nav |
| Wide | > 1440px | Max-width container (1440px) centered; product grid expands to four columns; hero content centered with larger margins; additional whitespace around sections |

### Touch Targets
- All interactive elements maintain minimum 44px height for touch accessibility
- Icon buttons are 40px x 40px with 8px internal padding
- Product card CTAs are 48px tall with 14px vertical padding
- Navigation links have 24px minimum touch area between items
- Quantity selector buttons are 44px tall with 16px width per button

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with a slide-in drawer
- Product grid reduces from 4 columns to 2 columns on tablet, to 1 column on mobile
- Footer link columns stack vertically on mobile, with accordion-style expandable sections
- Hero section reduces vertical padding from 64px to 32px on mobile
- Search bar moves from inline in nav to a full-screen overlay on mobile
- Ingredient badges wrap to 2 columns on tablet, single column on mobile
- Product detail accordions default to collapsed on mobile, expanded on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons (color shifts, underlines) could not be reliably extracted
- Error state styling for form inputs (border colors, error message typography) not observed
- Active/pressed states for icon buttons and quantity selectors not documented
- Sub-brand or collection-specific color palettes (e.g., "Mighty Patch" vs "Rescue Balm") may exist
- Dark mode or high-contrast mode styles not present in extracted data
- Loading states (skeleton screens, spinner colors) not captured
- Focus ring styles and keyboard navigation indicators not observed
- Tooltip and popover styling (background, arrow, shadow) not documented
- Modal/dialog overlay styling (scrim opacity, animation) not extracted
- Dropdown menu styling (background, shadow, item hover states) not fully captured
- Star rating interactive states (hover, selected) not documented
- Cart drawer or mini-cart styling not observed
- Mobile bottom navigation or tab bar styling not present in extracted data
- Custom select/ dropdown arrow styling not captured
- Video player controls and play button styling not documented
- Progress bar or step indicator styling not observed
- Toast/notification styling (success, error, warning variants) not extracted
- Print stylesheet considerations not available
