---
version: alpha
name: "Jiggy Puzzles"
source_url: "https://jiggypuzzles.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A polished, art-forward puzzle brand built on a warm ivory canvas (#fcfbf9) and a deep violet primary (#42416e) that reads as sophisticated rather than playful — the brand trusts a restrained, museum-like palette to elevate the puzzle category from hobby to decor. Gold accents (#ab8c52) appear sparingly on badges, product details, and framing cues, lending a subtle luxury feel without tipping into gilding. The typography stack pairs a bold, condensed Brandon Grotesque for headlines with the rounded, modern Bricolage Grotesque for body copy, creating a contrast between stately display and approachable reading. Product cards use soft, generous corner radii ({rounded.md}) and sit on the warm canvas with a subtle shadow, mimicking the feel of framed art leaning against a wall. The checkout flow inherits Shopify’s standard widget colors, but the brand’s own interface is remarkably restrained — nearly monochrome with violet as the single voltage, gold as the single accent, and no secondary palette competing for attention. The overall effect is calm, curated, and slightly editorial: puzzles presented not as toys but as objects worth framing, which the tagline directly promises.

colors:
  primary: "#42416e"
  primary-active: "#38385e"
  primary-disabled: "#a49c8b"
  ink: "#212121"
  body: "#2e2e2e"
  muted: "#636262"
  muted-soft: "#a09e99"
  hairline: "#e8d4ae"
  hairline-soft: "#f0ebe2"
  canvas: "#fcfbf9"
  surface-soft: "#f7f4ef"
  surface-card: "#ffffff"
  on-primary: "#fcfbf9"
  gold-accent: "#ab8c52"
  gold-light: "#e8d4ae"
  gold-dark: "#806430"
  badge-bg: "#42416e"
  badge-text: "#fcfbf9"
  star-rating: "#ab8c52"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'BrandonGrotesque-Bold', 'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'BrandonGrotesque-Bold', 'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'BrandonGrotesque-Bold', 'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'BrandonGrotesque-Bold', 'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'BrandonGrotesque-Bold', 'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'BrandonGrotesque-Bold', 'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'BrandonGrotesque-Bold', 'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'BrandonGrotesque-Bold', 'Bricolage Grotesque', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary-active}"
  button-gold:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-gold-active:
    backgroundColor: "{colors.gold-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    padding: 0
  button-text-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.link}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid #c13515"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-gold-badge:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    padding: "{spacing.base} 0"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.xl} 0 {spacing.base}"
  section-subheader:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    padding: "0 0 {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.hairline}"
  footer-link-active:
    typography: "{typography.link}"
    textColor: "{colors.gold-accent}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
    textTransform: uppercase
    letterSpacing: "0.5px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "2px solid {colors.primary}"
  badge-default:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-gold:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 7px"
    border: "1px solid {colors.primary}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: "16px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0 {spacing.base}"
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    borderLeft: "4px solid {colors.gold-accent}"
  testimonial-author:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} 0 0"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: "1px"
    margin: "{spacing.lg} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the deep violet {colors.primary} with white text and a soft 8px radius ({rounded.sm}). Used for "Add to Cart", "Shop Now", and primary checkout flows. On hover, shifts to {colors.primary-active} (#38385e) for a subtle darkening. Disabled state uses the muted {colors.primary-disabled} (#a49c8b) to signal inactivity without visual noise. The uppercase Brandon Grotesque Bold at 16px with 0.5px letter-spacing gives the button a confident, editorial weight.

**`button-secondary`** — An outlined variant with a white fill, violet text, and a 2px solid border matching {colors.primary}. Used for "Learn More", "View Details", and secondary actions alongside the primary button. Active state darkens the border and text to {colors.primary-active}. The transparent background ensures it sits comfortably on the warm canvas without competing with the primary button.

**`button-gold`** — A tertiary accent button using the gold {colors.gold-accent} as background, reserved for premium cues: "Frame Your Puzzle", "Gift This Puzzle", or limited-edition collections. Active state deepens to {colors.gold-dark} (#806430). Used sparingly to preserve the gold's signaling value.

**`button-text-link`** — A text-only button with no background or border, styled as a link in {colors.primary}. Used for "Read Reviews", "See Details", and inline navigation within product cards. Active state shifts to {colors.primary-active}. The underline is omitted by default, appearing only on hover (not tokenized here but implied).

### Cards
**`product-card`** — The core product display unit: a white card ({colors.surface-card}) with a 12px radius ({rounded.md}) and a soft drop shadow (0 2px 8px rgba(0,0,0,0.08)). The image occupies the top half with matching top radius, while the title and price sit below with 16px horizontal padding. A violet or gold badge can be positioned absolutely at the top-left corner of the image area. The card feels like a framed print — the generous radius and subtle shadow echo a matted frame leaning against a wall.

**`testimonial-card`** — A review or quote card on a soft surface background ({colors.surface-soft}) with a 4px gold left border accent. The body text uses {typography.body-sm} in {colors.body}, while the author name appears below in {typography.title-sm} in {colors.ink}. The 24px padding and 12px radius give it a comfortable, readable footprint.

### Navigation
**`nav-bar`** — A fixed or sticky top bar at 72px height on the warm canvas background ({colors.canvas}). Navigation links use uppercase Brandon Grotesque Bold at 14px with 0.5px letter-spacing. The active page is indicated by a 2px solid underline in {colors.primary}. A subtle bottom border in {colors.hairline-soft} separates the nav from the page content. The logo (typically the Jiggy wordmark) sits left-aligned, with cart and account icons right-aligned.

**`nav-link-active`** — The active navigation state: violet text ({colors.primary}) with a 2px solid bottom border in the same violet. The uppercase treatment and letter-spacing create a crisp, editorial tab feel.

**`nav-link-inactive`** — Default navigation state: dark text ({colors.ink}) with no underline. On hover, the text shifts to {colors.primary} (not tokenized but implied).

### Forms
**`text-input`** — Standard text input fields for email capture, search, and checkout forms. A white background with a 1px {colors.hairline} border and 8px radius. On focus, the border thickens to 2px and shifts to {colors.primary} for clear visual feedback. Error state uses a 2px #c13515 border (Shopify's default error red, retained for consistency).

**`select-input`** — Dropdown selectors matching the text-input styling: white background, 1px hairline border, 8px radius, 48px height. Used for quantity selection, puzzle piece count filters, and sort options.

**`quantity-selector`** — A compact 40px-tall input for adjusting puzzle quantities in the cart. Matches the text-input styling but with tighter padding (8px 12px). The adjacent +/- buttons (not tokenized) follow the same border and radius treatment.

### Footer
**`footer`** — A dark footer on {colors.ink} (#212121) background with white text. Links appear in {colors.hairline} (#e8d4ae) — a warm gold-beige that reads as elegant against the dark background. Active/hover links shift to {colors.gold-accent} (#ab8c52). Section headings are uppercase title-sm in white with 0.5px letter-spacing. The footer uses generous 64px vertical padding and contains columns for "Shop", "About", "Support", and social links.

### Badges
**`badge-default`** — A small violet badge (4px 8px padding, 8px radius) used for "New", "Best Seller", or "Limited Edition" labels on product cards. Uppercase Brandon Grotesque Bold at 11px with 0.5px letter-spacing ensures readability at small sizes.

**`badge-gold`** — A gold-accent badge reserved for premium indicators: "Framed", "Gift Wrap", or "Exclusive". Uses the same sizing and typography as the default badge but with {colors.gold-accent} background.

**`badge-outline`** — An outlined variant with transparent background and a 1px {colors.primary} border. Used for "In Stock" or "Available" indicators where a filled badge would be too heavy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row), nav collapses to hamburger, hero text reduces to {typography.display-lg} (36px), buttons become full-width, footer stacks vertically, search bar moves to a slide-out panel |
| Tablet | 744–1128px | Two-column product grid (2 cards per row), nav links remain visible but condensed, hero uses {typography.display-xl} at 42px, buttons maintain inline layout, footer uses 2-column grid |
| Desktop | 1128–1440px | Three-column product grid (3 cards per row), full nav with all links visible, hero at full {typography.display-xl} (48px), standard button sizing, footer uses 4-column grid |
| Wide | > 1440px | Four-column product grid (4 cards per row), max-width container at 1440px centered, hero may include a full-bleed image, footer remains 4-column with additional whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons (cart, account, search) are 48px × 48px with {rounded.full} for easy tapping
- Product card tap targets include the entire card surface, not just the title or button
- Accordion headers are 48px tall for comfortable finger interaction
- Quantity selector +/- buttons are 44px × 44px minimum

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-out panel from the left
- Product filters (if present) collapse to a "Filter" button that opens a modal or bottom sheet on mobile
- Footer columns collapse from 4 to 2 at tablet, then to a single vertical stack on mobile
- Hero section reduces vertical padding from 64px to 32px on mobile, with text scaling down proportionally
- Search bar transforms from an inline input to a full-screen overlay on mobile
- Product card badges may be hidden or reduced in size on mobile to prevent crowding

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (buttons, links, cards) are inferred from common patterns but not extracted from the live site; actual hover transitions (color, shadow, scale) may differ
- Error and validation styling for forms (beyond the basic error border) is not captured — inline error messages, success states, and tooltip styling are unknown
- Dark mode is not supported on the live site; no dark palette tokens are defined
- The extracted font list includes "BrandonGrotesque-Bold", "Bricolage Grotesque", and "Nunito Sans" — the exact font stack order and fallback chain for each variant is inferred; actual weights (e.g., 400, 500, 600, 700) are assumed based on common usage
- The gold accent (#ab8c52) appears in extracted colors but its exact usage (badges, borders, icons, or all three) is inferred from typical brand patterns
- Star rating color is assumed to be gold (#ab8c52) based on common e-commerce patterns, but the actual rating component styling is not extracted
- Shopify checkout widget colors (Klarna, Afterpay, etc.) are present in the extracted hex list but are not part of the brand's design system; they are excluded from the palette
- The extracted hex list includes many near-white and near-gray variants (#f5f2ec, #fcfbf9, #f7f7f7, #f2f2f2, #f7f4ef, #f0ebe2, #ece7db, #f4f0e8) — the primary canvas is identified as #fcfbf9 (the lightest and most frequent), but the brand may use multiple surface tones for different contexts
- Animation and transition timing (ease, duration) are not captured
- Iconography style (line vs. filled, stroke weight) is not documented
- The "NEW" badge and other promotional indicators may have additional styling (e.g., animation, gradient) not captured
- Product card shadow values are estimated; actual box-shadow may vary in spread, blur, or color
- The hero section's exact layout (full-bleed image vs. contained, text overlay vs. side-by-side) is not extracted
- Footer social icon colors and hover states are not captured
- The brand's logo treatment (wordmark vs. icon, color variants) is not documented
