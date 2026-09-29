---
version: alpha
name: "Kylie Cosmetics"
source_url: "https://kyliecosmetics.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Kylie Cosmetics by Kylie Jenner is a beauty empire built on a foundation of millennial-pink confidence and glossy, aspirational glamour. The brand's digital presence mirrors its product philosophy: bold, unapologetically feminine, and meticulously curated. The palette is anchored by a signature dusty rose (`#b3848f`) that appears across primary CTAs, badges, and accent elements, creating a cohesive visual identity that feels both luxurious and approachable. This is supported by a deeper, more grounded mauve (`#905d5d`) used for active states and secondary accents, while a clean white canvas (`#f8f8f8`) provides the necessary breathing room for product photography to shine. The brand's voice is amplified through a sophisticated typographic system that pairs the elegant, custom Tt-Chocolate script for display headings with the sturdy UniversLTStd-Bold for navigation and buttons, creating a deliberate contrast between playful femininity and editorial authority. Signature design moves include pill-shaped buttons (`{rounded.full}`) that soften the user interface, generous use of negative space, and a consistent application of the primary rose across interactive elements. The overall feel is that of a luxury boutique translated for the digital age — intimate, high-contrast, and designed to make every product feel like a coveted treasure. The dark ink (`#040404`) used for body text against the light canvas ensures readability, while muted tones (`#393939`, `#373737`) provide hierarchy without competing with the vibrant product imagery. This is a system that trusts its color story and typographic contrast to create a memorable, instantly recognizable brand experience.

colors:
  primary: "#b3848f"
  primary-active: "#905d5d"
  primary-disabled: "#efd7e5"
  ink: "#040404"
  body: "#333333"
  muted: "#393939"
  muted-soft: "#645458"
  hairline: "#cccccc"
  hairline-soft: "#dedede"
  canvas: "#f8f8f8"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-rose: "#f8f1f4"
  accent-pink: "#ffb8b8"
  accent-red: "#fb5858"
  accent-orange: "#c74a21"
  accent-blue: "#007aff"
  accent-blue-dark: "#191d48"
  accent-teal: "#1990c6"
  accent-teal-dark: "#136f99"
  star-rating: "#5897fb"
  error: "#fb5858"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Tt-Chocolate', 'script412displayregular', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Tt-Chocolate', 'script412displayregular', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "'UniversLTStd-Bold', 'YourFontName', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  display-sm:
    fontFamily: "'UniversLTStd-Bold', 'YourFontName', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.25px
  title-md:
    fontFamily: "'UniversLTStd-Bold', 'YourFontName', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'UniversLTStd-Bold', 'YourFontName', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.25px
  body-md:
    fontFamily: "'UniversLTStd-Bold', 'YourFontName', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'UniversLTStd-Bold', 'YourFontName', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'UniversLTStd-Bold', 'YourFontName', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.5px
  caption-sm:
    fontFamily: "'UniversLTStd-Bold', 'YourFontName', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.25px
  badge:
    fontFamily: "'UniversLTStd-Bold', 'YourFontName', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'UniversLTStd-Bold', 'YourFontName', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'UniversLTStd-Bold', 'YourFontName', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0.75px
    textTransform: uppercase
  link:
    fontFamily: "'UniversLTStd-Bold', 'YourFontName', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'UniversLTStd-Bold', 'YourFontName', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 1px
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
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-rose:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-field-segment:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: 8px 16px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  product-card-swatch:
    rounded: "{rounded.full}"
    height: 24px
  hero-banner:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    height: 480px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 6px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 40px
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a pill-shaped button with a full fill of the signature dusty rose (`{colors.primary}`). The button uses uppercase, letter-spaced bold type (`{typography.button-md}`) for a confident, editorial feel. On hover, the background shifts to the deeper mauve (`{colors.primary-active}`), and on disabled state it fades to a soft blush (`{colors.primary-disabled}`) with muted text. The generous horizontal padding (`32px`) and full rounding create a tactile, luxurious appearance.

**`button-secondary`** — A white pill button with dark ink text, used for secondary actions like "View All" or "Learn More." The borderless design relies on the contrast between the white canvas and the surrounding layout. Hover state introduces a subtle shadow or border (not captured in tokens). Disabled state uses muted text on a light surface.

**`button-tertiary-text`** — A text-only button styled as a link but using the primary rose color. Used for inline actions like "Add to Bag" within product cards or "Shop Now" in promotional banners. No background or border, relying entirely on typographic weight and color for hierarchy.

### Navigation
**`top-nav`** — A fixed-height, white navigation bar (`72px`) that houses the brand logo, navigation links, and utility icons (search, account, cart). Navigation links are set in uppercase, letter-spaced bold type (`{typography.nav-link}`) with the active state highlighted in the primary rose. The bar uses a subtle bottom hairline (`{colors.hairline}`) to separate it from the page content.

**`nav-link-active`** — Active navigation links are distinguished by the primary rose color, creating a clear visual indicator of the current section. The uppercase, bold treatment ensures legibility at small sizes.

**`nav-link-inactive`** — Inactive navigation links are rendered in a muted gray (`{colors.muted}`), receding into the background to allow the active link and brand logo to command attention.

### Cards
**`product-card`** — The core product display component, featuring a white background with medium rounding (`{rounded.md}`). The card contains a product image (with matching rounded corners), product title, price, and a color swatch strip. On hover, the card may elevate with a subtle shadow (not captured in tokens). The layout is clean and minimal, allowing the product photography to be the hero.

**`product-card-badge`** — Small, uppercase badges overlaid on product card images to denote "New," "Best Seller," or "Limited Edition." Badges use the primary rose background with white text, set in tight letter-spaced type (`{typography.badge}`). The small padding and slight rounding (`{rounded.sm}`) keep them unobtrusive yet legible.

**`product-card-swatch`** — Circular color swatches displayed on product cards to indicate available shades. Each swatch is a small, fully rounded circle (`24px`) that shows the actual product color. Multiple swatches are displayed in a horizontal row, with a "+N more" label if the count exceeds the visible limit.

### Forms
**`search-bar-pill`** — The site search is rendered as a pill-shaped input field with a soft gray background (`{colors.surface-soft}`) and muted placeholder text. The pill shape (`{rounded.full}`) maintains the brand's friendly, approachable aesthetic. On focus, the border may highlight with the primary rose (not captured in tokens). A search icon is positioned at the leading edge.

**`quantity-selector`** — A compact, horizontally arranged component for adjusting product quantities. It features a minus button, the current quantity display, and a plus button, all contained within a lightly rounded rectangle (`{rounded.sm}`). The component uses body-sm typography and maintains a consistent `40px` height for easy interaction.

### Footer
**`footer-section`** — The site footer uses a dark ink background (`{colors.ink}`) with white text, creating a strong visual anchor at the bottom of every page. The footer is organized into columns for navigation, customer service, and social links. Typography is set in body-sm for readability against the dark background.

**`footer-link`** — Footer links are rendered in a muted, soft tone (`{colors.muted-soft}`) to reduce visual weight against the dark background. On hover, links may lighten (not captured in tokens). The link typography uses standard body weight and size for comfortable reading.

### Badges
**`badge-new`** — A soft pink badge (`{colors.accent-pink}`) used to flag new product arrivals. The badge uses uppercase, letter-spaced type (`{typography.badge}`) and is lightly rounded (`{rounded.sm}`). The pink background is playful and attention-grabbing without being aggressive.

**`badge-sale`** — A red badge (`{colors.accent-red}`) used to denote sale or promotional items. The high-contrast red background with white text ensures immediate visibility. The badge follows the same typographic and rounding conventions as the new badge for consistency.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack vertically; hero banner height reduces to 320px; search bar moves to full-width below nav; color swatches reduce to 20px; button padding reduces to 14px 24px |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links with "More" dropdown; hero banner at 400px; search bar remains in nav; product cards show 3 swatches max |
| Desktop | 1128–1440px | Full navigation visible; three-column product grid; hero banner at 480px; search bar in nav with full functionality; product cards show all swatches |
| Wide | > 1440px | Maximum content width of 1440px with centered layout; four-column product grid; hero banner at 520px; additional whitespace around components |

### Touch Targets
- All interactive elements maintain a minimum touch target of 44x44px on mobile devices
- Button heights are consistently 48px for primary and secondary actions
- Icon buttons are 40x40px with adequate padding for finger taps
- Color swatches are 32x32px on desktop, 28x28px on mobile for easy selection
- Navigation links have a minimum 44px tap area, even when text is smaller

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile, with a slide-out drawer for full navigation
- Product filters collapse into a single "Filter" button on mobile, opening a modal overlay
- Footer columns stack vertically on mobile, with accordion-style expandable sections
- Hero banner text overlays collapse to a single line on mobile, with CTA button remaining full-width
- Multi-column product grids reduce to single column on mobile for optimal viewing
- Search functionality moves from inline to a full-screen overlay on mobile devices

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons, tertiary text buttons, and footer links could not be reliably extracted from the live site
- Error states for form inputs (validation, error messages, error borders) were not observed in the extracted data
- Focus states for all interactive elements (keyboard navigation outlines) are not documented
- Sub-brand palettes for Kylie Skin and Kylie Jenner Fragrances may have distinct color variations not captured in the primary system
- Dark mode styling is not present on the live site and therefore not documented
- Animation and transition timing values (ease-in-out durations, spring animations) were not extractable
- Shadow/elevation tokens for cards, modals, and dropdowns are missing from the extracted data
- Loading states (skeleton screens, spinner designs) are not documented
- Dropdown menu styling for navigation and form selects is not captured
- Modal and overlay component specifications (backdrop, positioning, close button) are incomplete
- The exact font weights for Tt-Chocolate (likely 400 only) and UniversLTStd-Bold (likely 700 only) are inferred from font names
- Responsive breakpoints are estimated based on common e-commerce patterns, not extracted from the live site
- Accessibility contrast ratios between certain color combinations (e.g., muted text on soft backgrounds) have not been verified
