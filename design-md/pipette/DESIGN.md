---
version: alpha
name: "Pipette"
source_url: "https://pipettebaby.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy anchor of #084b6d sets the tone for Pipette — a baby and sensitive-skin brand that feels more like a calm, clinical consultation than a nursery pastel explosion. That primary blue, pulled from the live site's most frequent hex, appears on every primary CTA, the site header, and key product badges, lending a pharmaceutical seriousness to a category usually drenched in pink or mint. The counterpoint is a warm off-white canvas of #fefdf9, a papery, unbleached backdrop that avoids the sterile glare of pure white and makes the brand feel grounded in natural ingredients. Typography leans on Recoleta, a rounded serif with a gentle, almost editorial weight, used for display headings at generous sizes — it's the kind of typeface that says "trust us, we've done the research" without raising its voice. Body copy runs in a clean sans-serif (likely system or a Shopify default) at modest weights, letting the serif headlines and the photography carry the emotional load. The palette is restrained: muted blues (#676986, #9cb7c5, #a4b7bc) and soft grays (#e5e5e5, #f4f4f6) create a hierarchy of calm, while a teal accent (#0e7a82) appears sparingly on secondary badges or ingredient callouts. Corners are softly rounded — buttons at {rounded.sm}, cards at {rounded.md} — never pill-shaped, never sharp, always the radius of a baby's knuckle. The overall effect is a brand that treats skincare for the smallest humans with the same rigor as adult dermatology, but wraps it in a warm, unbleached cloth.

colors:
  primary: "#084b6d"
  primary-active: "#063a54"
  primary-disabled: "#8bb0c4"
  ink: "#272d45"
  body: "#676986"
  muted: "#9a9db1"
  muted-soft: "#d3d4dd"
  hairline: "#e5e5e5"
  hairline-soft: "#f4f4f6"
  canvas: "#fefdf9"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#0e7a82"
  accent-teal-soft: "#a4b7bc"
  badge-blue: "#9cb7c5"
  dark-text: "#121212"

typography:
  display-xl:
    fontFamily: "'Recoleta', Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Recoleta', Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Recoleta', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Recoleta', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Recoleta', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  footer-link:
    fontFamily: "-apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-accent:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
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
  text-input-error:
    border: "2px solid #c13515"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.md}"
  product-badge:
    backgroundColor: "{colors.badge-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-accent:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "64px 24px"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.footer-link}"
    padding: "48px 24px"
  footer-link-item:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.footer-link}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "16px 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 0 16px 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Shop Now", and key conversion points. Rendered in deep navy {colors.primary} with white text, a soft 8px radius, and 44px height for comfortable tap targets. On hover, shifts to {colors.primary-active} (#063a54); disabled state uses {colors.primary-disabled} (#8bb0c4) with reduced opacity if needed.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Ingredients". Uses a white fill with a 2px solid {colors.primary} border. On hover, fills with {colors.primary} and inverts text to white. Same 44px height and 8px radius as the primary button for visual consistency.

**`button-tertiary-text`** — A text-only button for less prominent actions like "Cancel" or "Read Reviews". No background or border; text color is {colors.primary}. On hover, may underline or shift opacity. Used sparingly to avoid clutter.

**`button-pill-accent`** — A small, fully rounded accent button used for promotional badges, "NEW" tags, or ingredient callouts. Uses {colors.accent-teal} (#0e7a82) as background, white text, and a compact 8px 16px padding. Not a primary conversion tool — more of a visual signal.

### Cards
**`product-card`** — The standard product display card used on collection pages and search results. White background with a 12px rounded corner, 16px padding, and a subtle shadow or border from {colors.hairline}. Product images sit inside a matching 12px rounded container. Price, title, and a quick-add button stack below. On hover, may lift slightly with a soft shadow.

**`product-badge`** — A small, uppercase label applied to product cards for attributes like "Fragrance-Free" or "Dermatologist Tested". Uses {colors.badge-blue} (#9cb7c5) background with white text, 4px radius, and tight padding. A secondary variant uses {colors.accent-teal} for "New" or "Best Seller" tags.

### Navigation
**`top-nav`** — The site-wide header bar, 72px tall, fixed or sticky. White background ({colors.canvas}) with links in {colors.ink} at 14px medium weight. The active page link gets a 2px bottom border in {colors.primary}. Logo sits left, navigation links center or right, with a cart icon and search icon on the far right. On mobile, collapses to a hamburger menu.

### Forms
**`text-input`** — Standard text input for forms (email signup, search, account). White background, 44px height, 12px padding, 8px radius, and a 1px {colors.hairline} border. On focus, the border thickens to 2px and turns {colors.primary}. Error state uses a red border (#c13515) with an error message below in {colors.body}.

### Hero
**`hero-section`** — The full-width hero banner on the homepage and key landing pages. Uses {colors.canvas} background with a large Recoleta headline (42px), a supporting paragraph in {colors.body}, and a single {colors.primary} CTA button. The hero image (product or lifestyle photography) sits adjacent or as a full background with a subtle overlay. Padding is generous at 64px vertical.

### Search
**`search-bar`** — A pill-shaped search input (9999px radius) used in the header or on search pages. 40px height, white background, 1px {colors.hairline} border, and placeholder text in {colors.muted}. On focus, the border turns {colors.primary}. May include a magnifying glass icon on the left.

### Footer
**`footer-section`** — The site footer, rendered in {colors.primary} background with white text. Links are 13px regular weight, stacked in columns. Includes legal text, social icons, and a newsletter signup. Padding is 48px vertical. Link hover state may underline or shift to a lighter blue.

### Accordion
**`accordion-header`** — Used on product detail pages for "Ingredients", "How to Use", and "Shipping & Returns" sections. White background, 16px padding top and bottom, a 1px {colors.hairline} bottom border, and a 16px bold title. Clicking toggles open the accordion content below.

**`accordion-content`** — The expandable content area below an accordion header. Uses {colors.body} text at 16px regular weight, with 16px bottom padding. May include bullet lists or paragraphs.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger; hero text shrinks to 28px; product cards stack vertically; search bar moves to full-width below nav; footer columns stack. |
| Tablet | 744–1128px | Two-column product grid; top-nav links visible but condensed; hero uses 32px headline; search bar remains in header but smaller. |
| Desktop | 1128–1440px | Full three- or four-column product grid; top-nav fully expanded; hero uses 42px headline; search bar in header at standard size. |
| Wide | > 1440px | Max-width container (1440px) centered; hero may use wider imagery; product grid may expand to five columns; whitespace increases. |

### Touch Targets
- All buttons and interactive elements are at least 44px tall (primary, secondary, text inputs).
- Icon buttons (cart, search, hamburger) are at least 44x44px tap targets.
- Accordion headers are 44px+ tall for easy tapping.
- Product card quick-add buttons are 44px tall.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px; the menu slides in from the left or right.
- Product grid collapses from 4 columns to 2 columns at tablet, to 1 column at mobile.
- Hero section reduces font size and may stack image below text on mobile.
- Footer columns collapse from 4 columns to 2 columns at tablet, to 1 column at mobile.
- Search bar moves from header to a full-width bar below the nav on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components (beyond primary button) could not be reliably extracted from the live site; the above uses reasonable defaults (darken, underline, border shift).
- Error styling for forms (red border, error message) is inferred from common patterns; exact error text color and iconography not confirmed.
- Dark mode is not present on the live site; no dark palette defined.
- Sub-brand or seasonal color palettes (e.g., holiday, limited edition) not extracted.
- The exact font stack for body copy is assumed to be system sans-serif; the only named font found was Recoleta. The sans-serif fallback is a best guess.
- Spacing values (padding, margins) are estimated from common e-commerce patterns; exact values may vary by page.
- The `button-pill-accent` component is inferred from the teal accent color; its exact usage (badges, tags) is speculative.
- No extracted data for loading states, skeleton screens, or empty states.
- The extracted hex list includes several grays and blues that may be Shopify or widget defaults; the primary (#084b6d) and accent (#0e7a82) are the most distinctive brand colors.
