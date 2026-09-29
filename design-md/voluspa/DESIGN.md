---
version: alpha
name: "Voluspa"
source_url: "https://www.voluspa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Voluspa is a handcrafted luxury home fragrance brand that wraps its warm, artisanal identity in a palette of soft neutrals and restrained accents. The canvas is a clean white (#ffffff) with subtle warmth from surface tones like {colors.surface-soft} (#f4f4f4) and {colors.surface-card} (#ece8e1), creating a tactile, layered feel that echoes the brand's hand-poured candles and oil diffusers. The primary action color is a crisp blue (#007aff), a deliberate contrast to the otherwise muted environment, used sparingly for CTAs and interactive elements. The ink (#333333) and body (#898989) text maintain readability without harshness, while the hairline (#ddd8d0) and muted-soft (#d9d4cc) lines keep the layout airy and refined. A signature accent green (#85c28e) appears in product badges and nature-inspired cues, and a restrained red (#ff0000) is reserved for sale indicators. The typography system pairs the clean, geometric Barlow family for body and UI text with the elegant, serifed Libre Baskerville for display headings, evoking a sense of heritage craftsmanship. Pinyon Script, a delicate calligraphic face, is used sparingly for decorative or signature-style accents, while Work Sans supports secondary UI roles. The overall mood is one of quiet luxury—generous whitespace, soft corners ({rounded.sm} on cards, {rounded.md} on buttons), and a deliberate avoidance of visual noise. Every design decision reinforces the brand's promise: handcrafted, intentional, and beautifully scented.

colors:
  primary: "#007aff"
  primary-active: "#0056cc"
  primary-disabled: "#b3d9ff"
  ink: "#333333"
  body: "#898989"
  muted: "#a1a1a1"
  muted-soft: "#d9d4cc"
  hairline: "#ddd8d0"
  hairline-soft: "#e3e3e3"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ece8e1"
  surface-warm: "#eae5db"
  on-primary: "#ffffff"
  accent-green: "#85c28e"
  accent-red: "#ff0000"
  badge-new: "#85c28e"
  badge-sale: "#ff0000"
  star-rating: "#333333"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Libre Baskerville', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
  display-lg:
    fontFamily: "'Libre Baskerville', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.3px
  display-md:
    fontFamily: "'Libre Baskerville', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.2px
  display-sm:
    fontFamily: "'Libre Baskerville', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  title-md:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  body-md:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Barlow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  decorative:
    fontFamily: "'Pinyon Script', 'Brush Script MT', cursive"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px

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
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 38px
  icon-button:
    backgroundColor: transparent
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
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline-soft}"
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0 0 16px 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.sm} {spacing.base}"
  product-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.sm}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.body}"
  footer-link-hover:
    textColor: "{colors.ink}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-input-focus:
    border: "1px solid {colors.ink}"
  newsletter-submit:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.md}"
    padding: "12px 20px"
    height: 44px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} 0"
  accordion-body:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature blue ({colors.primary}) with white text. Uses Barlow 600 weight, uppercase, with a 12px rounded corner. On hover/active, it shifts to a deeper blue ({colors.primary-active}). The disabled state uses a pale blue ({colors.primary-disabled}) to maintain visual hierarchy without confusion. Height is 44px with 12px vertical and 24px horizontal padding.

**`button-secondary`** — An outlined alternative with a white background, ink text, and a 1px hairline border. Maintains the same uppercase Barlow 600 typography and 44px height. On active, the border thickens visually by switching to ink color and the background takes on a soft surface tone. Used for "Add to Cart" secondary actions and "Learn More" links.

**`button-tertiary-text`** — A text-only button with no background or border, used for less prominent actions like "Cancel" or "View All". Uses the same uppercase Barlow 600 style but with no padding beyond the text itself.

**`button-pill`** — A fully rounded variant of the primary button, used for promotional badges, filter tags, and quick-add actions. Smaller at 38px height with 10px vertical padding, it uses the same blue but with a pill shape.

### Cards
**`product-card`** — The core product display unit, a white card with soft 8px rounded corners. The image area has rounded top corners only, creating a natural visual break. The title uses Barlow 600 at 16px, while the price sits below in body weight. Cards are spaced with 16px padding on sides and bottom. No shadow is used, relying instead on the contrast between the white card and the soft surface background.

**`product-badge`** — A small, green ({colors.accent-green}) label with white uppercase Barlow 700 text, used for "NEW" or "BESTSELLER" indicators. The 4px rounded corners and tight padding keep it unobtrusive but legible. A red variant ({colors.accent-red}) is reserved for sale or clearance items.

### Navigation
**`top-nav`** — A fixed 72px white bar with a subtle bottom border ({colors.hairline-soft}). Navigation links use Barlow 600 at 13px with generous 0.8px letter spacing in uppercase. The active state is indicated by a 2px bottom border in ink. The logo typically sits centered or left-aligned, using the Libre Baskerville display face or a wordmark.

**`nav-link-active`** — Active navigation link with an underline indicator. The text remains ink, while inactive links fade to muted gray ({colors.muted}).

### Forms
**`search-bar`** — A pill-shaped search input with a soft gray background ({colors.surface-soft}) and subtle border. On focus, the background turns white and the border switches to ink. Uses Barlow 400 at 14px for placeholder and input text. Height is 44px with 10px vertical padding.

**`newsletter-input`** — A standard email input with a white background and hairline border, 12px rounded corners. The submit button sits adjacent, using ink background with white text in Barlow 600 uppercase.

**`quantity-selector`** — A compact control with a white background, hairline border, and 8px rounded corners. The increment/decrement buttons sit on either side with a soft surface background. Used on product detail pages for adjusting cart quantities.

### Footer
**`footer`** — A warm-toned section ({colors.surface-warm}) with a top hairline border. Headings use Barlow 600 at 16px in ink, while links are Barlow 500 at 14px in body gray. The layout typically includes 3-4 columns of links, a newsletter signup, and social icons. Padding is generous at 48px vertical.

### Accordion
**`accordion`** — A bordered section used for product descriptions, ingredients, and FAQs. Each item has a bottom hairline-soft border. The header uses Barlow 600 at 16px, and the body uses Barlow 400 at 14px in body gray. Padding is 16px top and bottom with no horizontal padding to align with the parent container.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 items per row), hamburger menu replaces top nav links, hero section reduces to 48px padding, footer stacks to single column, search bar collapses to icon-only, accordion becomes default for product details |
| Tablet | 744–1128px | Two-column product grid (3-4 items per row), top nav shows limited links with "More" dropdown, hero maintains 64px padding, footer shows 2 columns, search bar remains full but smaller |
| Desktop | 1128–1440px | Full top nav with all links, 4-column product grid, hero with 64px padding, footer with 3-4 columns, search bar full width in nav |
| Wide | > 1440px | Max-width container at 1440px centered, product grid can show 5 items per row, hero may include full-bleed imagery, footer columns expand |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons are 40px x 40px minimum
- Quantity selector buttons are 40px x 40px
- Product card tap targets cover the full card area
- Accordion headers are minimum 44px tall for easy tapping

### Collapsing Strategy
- Top nav collapses to hamburger menu on mobile (< 744px)
- Product grid reduces columns from 4-5 to 2 on mobile
- Footer columns stack vertically on mobile
- Hero section reduces vertical padding on mobile
- Search bar collapses to icon-only on mobile, expanding to full-width on tap
- Product descriptions and details use accordion pattern on mobile, expand to full-width on tablet and above
- Secondary navigation (breadcrumbs, filters) collapses to dropdown or hidden on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow, scale, or border change) could not be reliably extracted
- Error styling for form inputs (red border, error message typography) is not captured
- Sub-brand or collection-specific palettes (e.g., holiday, limited edition) are not documented
- Dark mode or high-contrast mode styles are not available
- Loading states (skeleton screens, spinners) are not defined
- Focus ring styles for keyboard navigation are not captured
- Micro-interactions (button press, card hover, menu animation) timing and easing values are unknown
- Dropdown menu styles (mega menu, account menu) are not fully extracted
- Mobile bottom navigation or tab bar styles are not documented
- Specific Shopify theme customizations (cart drawer, checkout) may override base styles
- Print stylesheet behavior is not documented
