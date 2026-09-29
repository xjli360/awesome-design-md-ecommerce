---
version: alpha
name: "Bubble"
source_url: "https://hellobubble.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Bubble is a skincare brand that speaks to Gen Z with a voice that is equal parts playful and direct, wrapping its formulations in a visual language that feels like a fresh start. The brand's palette is anchored by a vibrant coral-coral-pink, `#f9644b`, which serves as the primary voltage for CTAs, badges, and accent moments, cutting through a clean, near-white canvas (`#f7f7f7`) and a soft, almost imperceptible surface (`#f8f9fa`). This coral is balanced by a deep, almost-black ink (`#231f20`) for body copy and headlines, creating a high-contrast, legible system that feels confident without being aggressive. Supporting tones like `#6c757d` (muted gray) and `#dee2e6` (hairline) provide structure, while a secondary palette of `#007bff` (a crisp blue for links) and `#28a745` (a fresh green for success states) hints at a broader, functional system beneath the playful surface. The typography is a deliberate mix of the familiar and the distinctive: system fonts like `-apple-system`, `Arial`, and `Helvetica Neue` provide a reliable, fast-loading baseline, while custom display faces like `FK-Screamer` and `IC-Grand` (and the serif `Reckless Neue`) are reserved for hero headlines and brand moments, injecting personality and a touch of editorial flair. The design system leans on generous whitespace, soft but defined rounded corners (`{rounded.sm}` for buttons, `{rounded.md}` for cards), and a consistent use of `{spacing.base}` and `{spacing.lg}` to create a layout that feels airy, approachable, and easy to navigate—a digital storefront that prioritizes clarity and a sense of calm efficacy over clinical sterility.

colors:
  primary: "#f9644b"
  primary-active: "#e04a30"
  primary-disabled: "#fccac2"
  ink: "#231f20"
  body: "#343a40"
  muted: "#6c757d"
  muted-soft: "#adb5bd"
  hairline: "#dee2e6"
  hairline-soft: "#e9ecef"
  canvas: "#f7f7f7"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#007bff"
  accent-green: "#28a745"
  accent-red: "#dc3545"
  accent-yellow: "#ffc107"
  accent-teal: "#17a2b8"
  star-rating: "#ffc107"
  badge-new: "#f9644b"
  badge-sale: "#dc3545"

typography:
  display-xl:
    fontFamily: "'FK-Screamer', 'IC-Grand', 'Reckless Neue', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'FK-Screamer', 'IC-Grand', 'Reckless Neue', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'FK-Screamer', 'IC-Grand', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'IC-Grand', 'Reckless Neue', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.1
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
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 19px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 3px {colors.primary-disabled}"
  text-input-error:
    borderColor: "{colors.accent-red}"
    textColor: "{colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    marginBottom: "{spacing.base}"
  hero-subheadline:
    typography: "{typography.display-sm}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  social-icon:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 36px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  rating-stars:
    textColor: "{colors.star-rating}"
    fontSize: 16px
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-header:
    typography: "{typography.title-sm}"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    paddingTop: "{spacing.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop Now", and key conversion points. It uses the brand's coral `{colors.primary}` background with white text, a comfortable `{rounded.sm}` corner, and a `{typography.button-md}` weight for clear legibility. On hover, it shifts to `{colors.primary-active}`; when disabled, it fades to `{colors.primary-disabled}`. The `button-secondary` variant offers a clean white background with `{colors.ink}` text, ideal for less prominent actions like "Learn More" or "View Details". A `button-secondary-outline` version uses a transparent background with a `1px` solid `{colors.hairline}` border for a lighter touch. For promotional or compact contexts (e.g., "Subscribe" or "Get Offer"), `button-pill-primary` uses a `{rounded.full}` shape and smaller `{typography.button-sm}` font, while `button-pill-outline` provides an outlined counterpart.

### Cards
**`product-card`** — The core product display unit on collection and search pages. It features a `{rounded.md}` corner, a clean `{colors.surface-card}` background, and a `1/1` aspect ratio image area with matching rounded corners. The card layout stacks the product image, then the `product-card-title` using `{typography.title-sm}`, and the `product-card-price` in `{colors.muted}`. A `product-card-badge` can be overlaid on the image for "New" or "Sale" indicators, using the `{typography.badge}` style and `{colors.badge-new}` or `{colors.badge-sale}` backgrounds. Cards use `{spacing.sm}` between elements and `{spacing.base}` padding around the text block.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar with a `{colors.canvas}` background, `{colors.ink}` text, and a `{typography.nav-link}` style that is uppercase and tightly tracked. The bar is `64px` tall. Active navigation links (`nav-link-active`) switch their text color to `{colors.primary}`. The nav bar contains the brand logo, primary page links (e.g., "Shop", "Routine", "About"), and utility icons (search, account, cart). On mobile, the nav collapses into a hamburger menu.

### Forms
**`text-input`** — Standard single-line text input for search, email signup, and account forms. It uses a `{colors.surface-card}` background, `{typography.body-md}` text, and `{rounded.sm}` corners. The input has a `1px` solid `{colors.hairline}` border by default. On focus, it gains a `{colors.primary}` border and a `3px` `{colors.primary-disabled}` box-shadow ring. An error state (`text-input-error`) uses a `{colors.accent-red}` border and text color. The input height is `48px` with `12px 16px` padding.

### Hero Section
**`hero-section`** — The primary brand storytelling block on the homepage and key landing pages. It uses a `{colors.surface-soft}` background to create a subtle separation from the main canvas. The `hero-headline` uses the expressive `{typography.display-xl}` font, while the `hero-subheadline` provides supporting text in `{colors.muted}`. A `button-primary` is typically placed below the subheadline. The section has `{spacing.section}` vertical padding and `{spacing.lg}` horizontal padding.

### Search
**`search-bar`** — A prominent, pill-shaped search bar (`{rounded.full}`) used in the nav or hero area. It has a `{colors.surface-card}` background, `{typography.body-md}` text, and a `48px` height. The bar includes a search icon on the left and placeholder text like "Search products...". On focus, it behaves like a `text-input-focus`.

### Footer
**`footer`** — A full-width footer with a `{colors.ink}` background and `{colors.canvas}` text. It uses `{typography.body-sm}` for general text and `{typography.link}` for footer links (`footer-link`), which are styled in `{colors.muted-soft}`. The footer contains columns for "Shop", "About", "Help", and social links. Social icons (`social-icon`) are circular (`{rounded.full}`), `36px` tall, with a `{colors.muted}` background and `{colors.canvas}` icon color.

### Badges
**`badge-new`** and **`badge-sale`** — Small, uppercase labels used on product cards and promotional banners. They use `{typography.badge}` (11px, bold, uppercase), `{rounded.xs}` corners, and `2px 8px` padding. `badge-new` uses the `{colors.primary}` coral, while `badge-sale` uses `{colors.accent-red}`. Both have white text.

### Accordion
**`accordion`** — Used for FAQ sections and product details. It has a `{colors.surface-card}` background, `{rounded.sm}` corners, and `{spacing.base}` vertical / `{spacing.lg}` horizontal padding. The `accordion-header` uses `{typography.title-sm}` and includes a chevron icon that rotates on open. The `accordion-content` uses `{typography.body-sm}` in `{colors.body}` with `{spacing.sm}` top padding.

### Rating Stars
**`rating-stars`** — A row of star icons used on product cards and reviews. The stars are rendered in `{colors.star-rating}` (yellow) at `16px` font size. Empty stars are shown in `{colors.muted-soft}`. The component is typically placed between the product title and price.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav bar collapses to hamburger menu; product cards stack vertically; hero section reduces padding to `{spacing.xl}`; search bar moves into nav drawer; footer columns stack. |
| Tablet | 744–1128px | Two-column product grid; nav bar remains visible with condensed links; hero section uses `{typography.display-lg}`; search bar is visible in nav. |
| Desktop | 1128–1440px | Three or four-column product grid; full nav bar with all links; hero section uses `{typography.display-xl}`; search bar is prominent in nav. |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can expand to four columns; hero section uses larger `{typography.display-xl}` with more whitespace. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Icon buttons and social icons are at least 36x36px with adequate padding.
- Product card tap areas cover the entire card surface.
- Accordion headers are fully tappable.

### Collapsing Strategy
- The top navigation bar collapses into a hamburger menu on mobile (< 744px).
- The footer's multi-column layout collapses into a single column on mobile.
- Product grids reduce from 4 columns on desktop to 2 on tablet and 1 on mobile.
- Hero section text and CTA stack vertically on mobile, with the image (if present) moving below the text.
- Search bar becomes a search icon in the nav on mobile, expanding to a full-width input on tap.
- Accordion content is hidden by default on all screen sizes, expanding on header tap.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (e.g., `button-secondary`, `nav-link`, `footer-link`) could not be reliably extracted from the live site's CSS.
- Error, success, and warning styling for forms (e.g., input validation messages, form-level alerts) is not fully documented.
- Dark mode or high-contrast mode color overrides are not present in the extracted data.
- Sub-brand or promotional campaign-specific palettes (e.g., limited edition drops) are not captured.
- The exact `font-weight` values for custom display fonts (`FK-Screamer`, `IC-Grand`, `Reckless Neue`) are inferred; actual weights may vary.
- Animation and transition timing (e.g., button hover, card lift, nav dropdown) is not specified.
- The `box-shadow` values for cards, modals, and dropdowns are not extracted.
- The `z-index` stacking order for overlays, modals, and nav is not defined.
- The exact `border-width` for `button-secondary-outline` and `text-input` is assumed to be `1px`.
- The `text-transform: uppercase` on `nav-link` and `badge` is inferred from the brand's visual style; it may not be applied universally.
- The `line-height` and `letter-spacing` values for custom fonts are estimates based on common web typography practices.
- The `aspectRatio` for `product-card-image` is assumed; actual product images may vary in ratio.
