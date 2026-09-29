---
version: alpha
name: "BeginAgain"
source_url: "https://beginagaintoys.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A wooden toy brand that uses a sky-blue (#a9c7e7) as its primary — an unusual choice for a category that defaults to primary-color primaries or earth tones, and it signals a brand more interested in imagination than pedagogy. The palette is a study in soft contrast: a warm brown ink (#5f3f3f) sits against a near-white canvas (#f6f6f6), with a marigold accent (#dad55e) and a butter-yellow highlight (#fffa90) that appear on badges, swatches, and product details. The brand's typography runs Arial and Helvetica — system sans-serifs that feel unpretentious and child-friendly, with no custom typeface to distract from the wooden textures and saturated product photography. Buttons use a bright blue (#318cdd) for primary actions, while secondary actions and navigation links use the brown ink. Product cards are softly rounded ({rounded.md}), and the overall layout is generous with whitespace, letting each toy breathe against the light canvas. The footer and utility sections shift to a darker ground (#2b2b2b) with reversed type, creating a clear visual boundary between the playful product zone and the informational footer. The brand's voice is warm, direct, and slightly whimsical — the kind of design that trusts the product's physicality to do the heavy lifting.

colors:
  primary: "#a9c7e7"
  primary-active: "#8bb0d4"
  primary-disabled: "#d4e3f3"
  ink: "#5f3f3f"
  body: "#454545"
  muted: "#777620"
  muted-soft: "#aaaaaa"
  hairline: "#c5c5c5"
  hairline-soft: "#e9e9e9"
  canvas: "#f6f6f6"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#2b2b2b"
  accent-marigold: "#dad55e"
  accent-butter: "#fffa90"
  accent-coral: "#f1a899"
  accent-coral-soft: "#fddfdf"
  footer-bg: "#2b2b2b"
  footer-text: "#eeeeee"
  link-blue: "#003eff"
  link-blue-alt: "#007fff"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.sm}"
  product-badge:
    backgroundColor: "{colors.accent-butter}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    borderColor: "{colors.hairline}"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  category-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    borderColor: "{colors.hairline}"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using the sky-blue brand color ({colors.primary}) on a white or light canvas. Uppercase 14px type with 0.5px letter-spacing gives it a confident, slightly playful weight. On hover, the background shifts to {colors.primary-active}; disabled state uses {colors.primary-disabled} with muted text. Used for "Add to Cart," "Shop Now," and newsletter signup.

**`button-secondary`** — A white button with brown ink text, bordered implicitly by the canvas. Used for "Learn More" and secondary product actions. Same dimensions and typography as primary, but relies on the surrounding layout for visual separation.

**`button-accent`** — A marigold ({colors.accent-marigold}) button reserved for promotional badges, sale callouts, and limited-edition product flags. Same structure as primary but visually distinct — it signals urgency or specialness without the sky-blue brand default.

### Cards
**`product-card`** — A white card with {rounded.md} corners, 16px padding, and a softly rounded product image. The card stacks vertically: image on top, then product title in {typography.title-sm}, price in {typography.body-md}, and a {colors.accent-butter} badge for "New" or "Bestseller" tags. Cards sit on the {colors.canvas} background with generous spacing between them ({spacing.lg}).

**`product-badge`** — A small, uppercase label in {colors.accent-butter} with {colors.ink} text, used to flag product attributes. Rounded {rounded.xs} with 4px/8px padding. Appears as an overlay on product images or inline below the title.

### Navigation
**`nav-bar`** — A 64px fixed-height bar on {colors.canvas} with {colors.ink} navigation links. The active page is underlined with a 2px {colors.primary} border. On mobile, the nav collapses into a hamburger menu with a full-screen overlay. The logo sits left-aligned, with category links and a search icon on the right.

**`nav-link-active`** — The active navigation state, distinguished by a bottom border in the brand sky-blue. No background change — the brand trusts the underline and the link's own typographic weight to indicate location.

### Forms
**`text-input`** — A white input field with {rounded.sm} corners, 48px height, and a {colors.hairline} border. On focus, the border swaps to {colors.primary} with a 2px box-shadow in {colors.primary-disabled}. Used for search, newsletter email, and contact forms. Placeholder text uses {colors.muted-soft}.

**`search-bar`** — A pill-shaped ({rounded.full}) search input, 48px tall, with a {colors.hairline} border. The rounded shape is the brand's most distinctive form language — it appears on the homepage hero and persists across the site. On focus, the same primary border treatment applies.

### Footer
**`footer-section`** — A dark section ({colors.footer-bg}) with reversed type ({colors.footer-text}). Links use {typography.link} in white, with hover states that shift to {colors.primary}. The footer is divided into columns for "Shop," "About," "Support," and "Connect," with social icons in {colors.muted-soft}. The copyright line sits at the bottom in {typography.caption}.

### Hero
**`hero-section`** — A full-width section on {colors.surface-soft} with {colors.ink} display type. The hero features a large product image or lifestyle shot, with a headline in {typography.display-xl} and a {button-primary} CTA. The background color provides a soft contrast to the white product cards below without competing with the product photography.

### Category Chips
**`category-chip`** — Pill-shaped ({rounded.full}) filter chips used on collection pages. Inactive chips are white with a {colors.hairline} border; active chips fill with {colors.primary} and invert the text to {colors.on-primary}. The chip layout scrolls horizontally on mobile, with a "See All" option at the end.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text scales down to {typography.display-md}; category chips scroll horizontally; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible but truncated; hero uses {typography.display-xl} with reduced padding; category chips wrap to two rows |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; hero at full width with 64px section padding; category chips in a single row |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to four columns; hero content centered with larger margins |

### Touch Targets
- All buttons and links maintain a minimum 44px touch target height
- Category chips are at least 40px tall with 16px horizontal padding
- Search bar is 48px tall for comfortable tapping
- Nav links have 48px tap areas even when text is smaller
- Product card images link to product pages with a minimum 120px tap zone

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px
- Product grid collapses from 4 columns to 3 to 2 to 1 as viewport shrinks
- Footer columns stack vertically below 744px, with accordion-style expand/collapse for each section
- Category chips switch from a wrapped grid to a horizontal scroll below 744px
- Hero section reduces padding and font size below 744px, and the background image may crop to a square aspect ratio
- Secondary navigation (breadcrumbs, sub-category links) hides below 744px, replaced by a "Back" button

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components beyond primary/secondary buttons could not be reliably extracted from the live site; the above uses reasonable defaults (darken by 10% for hover, 2px primary outline for focus) but should be verified against the brand's actual CSS
- Error states for form inputs (validation, required fields, error messages) were not visible in the extracted data; placeholder colors and error border colors are assumed
- The extracted color list includes several blues (#318cdd, #003eff, #007fff) that may be framework defaults or social-icon colors rather than brand colors — the primary (#a9c7e7) was chosen as the most distinctive and frequently occurring non-gray, non-blue accent
- Font stack is limited to Arial and Helvetica; no custom typeface was detected, which may indicate the brand uses a web font loaded via JavaScript or a third-party service that wasn't captured
- Dark mode or high-contrast mode styles are not present in the extracted data
- Sub-brand or seasonal color palettes (holiday, limited edition) are not documented
- Animation and transition durations (hover fades, card entrance animations) were not extractable
- The brand's logo color and usage guidelines are not included — the logo likely uses {colors.ink} or {colors.primary} but this should be confirmed
- Accessibility contrast ratios between certain color pairs (e.g., {colors.muted} on {colors.canvas}) should be verified against WCAG 2.1 AA standards
