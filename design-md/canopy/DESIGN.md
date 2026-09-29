---
version: alpha
name: "Canopy"
source_url: "https://getcanopy.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A humidifier and shower-head brand that wraps warm, humid air in a palette anchored on #f1836b — a coral-tinged peach that reads as both the glow of a steam-filled bathroom and the blush of clean skin. The brand pairs this with #272d45, a deep navy-ink that grounds product photography and footer blocks, and #b1e3d6, a minty seafoam that surfaces in badges, progress indicators, and secondary accents. Typography splits between Ginto Nord for headlines — a condensed, squared-off sans with Nordic coldness — and Ogg Roman for body, a serif with soft, calligraphic terminals that whisper editorial warmth. Buttons are pill-shaped (`{rounded.full}`) and saturated, while product cards use `{rounded.lg}` corners that echo the gentle arc of a shower head. The checkout flow leans on `{rounded.sm}` for inputs and `{rounded.md}` for modals, keeping utility crisp while hero imagery stays generous. The overall effect is a bathroom brand that refuses to look clinical — it leans into spa-adjacent textures, soft gradients on `{colors.surface-soft}` (#f4f4f6), and a layout that treats whitespace like steam: expansive, softening, and slightly diffused at the edges.

colors:
  primary: "#f1836b"
  primary-active: "#ea5e40"
  primary-disabled: "#f7dfd9"
  ink: "#212121"
  body: "#272d45"
  muted: "#676986"
  muted-soft: "#d3d4dd"
  hairline: "#e5e5e5"
  hairline-soft: "#e5e5eb"
  canvas: "#f8f4f1"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-mint: "#b1e3d6"
  accent-deep-navy: "#272d45"
  accent-teal: "#0e7a82"
  star-rating: "#f2836b"
  error: "#f46b3e"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'ginto-nord', 'ginto-nord-medium', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ginto-nord', 'ginto-nord-medium', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'ginto-nord', 'ginto-nord-medium', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'ogg-roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'ogg-roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'ogg-roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'ogg-roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'ginto-nord', 'ginto-nord-medium', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'ginto-nord', 'ginto-nord-medium', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'ginto-nord', 'ginto-nord-medium', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 0.2px
  link:
    fontFamily: "'ogg-roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'ginto-nord', 'ginto-nord-medium', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  badge:
    fontFamily: "'ginto-nord', 'ginto-nord-medium', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px

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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-pill-accent:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  text-input-error:
    borderColor: "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
  product-card-image:
    rounded: "{rounded.lg}"
  product-card-badge:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.accent-deep-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  rating-star:
    color: "{colors.star-rating}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.md}"
  accordion-body:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.md} {spacing.md}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Subscribe", and "Shop Now". Rendered as a full pill (`{rounded.full}`) in the brand's coral-peach `{colors.primary}` with white text. On hover, shifts to `{colors.primary-active}` (#ea5e40). Disabled state uses `{colors.primary-disabled}` (#f7dfd9) with reduced opacity. Height is 48px with generous horizontal padding for a comfortable tap target.

**`button-secondary`** — Outline-style button for secondary actions like "Learn More" or "View Details". Uses the warm off-white `{colors.canvas}` background with `{colors.ink}` text. Active state fills with `{colors.hairline}`. Same pill shape and height as primary for visual consistency.

**`button-pill-accent`** — A smaller, accent-driven button used for promotional badges or "New" tags. Uses `{colors.accent-mint}` (#b1e3d6) background with dark text. Compact padding (10px 20px) and smaller typography (`{typography.button-sm}`).

### Cards
**`product-card`** — The primary product display component. A white (`{colors.surface-card}`) card with `{rounded.lg}` (20px) corners. Contains a product image with matching rounded corners, a title in `{typography.title-sm}`, price in `{typography.body-md}`, and optional `{colors.accent-mint}` badge. Hover state adds a subtle shadow (not captured in extracted data). Used on collection pages and featured product grids.

**`product-card-badge`** — A small pill badge overlaid on product images, used for "Best Seller", "New", or "Limited Edition". Uses `{colors.accent-mint}` background with `{typography.badge}` font.

### Navigation
**`nav-bar`** — Fixed top navigation at 72px height. Background is `{colors.canvas}` (#f8f4f1), the warm off-white that sets the brand's spa-like tone. Links use `{typography.nav-link}` (14px, 500 weight, 0.5px letter spacing). Active link color shifts to `{colors.primary}`. On mobile, collapses into a hamburger menu with a slide-out drawer.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with `{colors.surface-soft}` background and `{colors.muted}` placeholder text. Compact at 44px height, used in the nav bar and on search pages.

### Forms
**`text-input`** — Standard text input for checkout forms, newsletter signups, and account pages. Uses `{rounded.sm}` (8px) corners, `{colors.canvas}` background, and `{typography.body-md}`. Focus state gets a 2px `{colors.primary-disabled}` ring. Error state uses `{colors.error}` (#f46b3e) border.

### Hero
**`hero-section`** — Full-width hero banner on the homepage and landing pages. Background is `{colors.surface-soft}` (#f4f4f6) with `{typography.display-xl}` headline. Padding is `{spacing.section}` (64px) top and bottom, `{spacing.lg}` (24px) sides. Often paired with a full-bleed product image or lifestyle photography.

### Footer
**`footer`** — Dark footer using `{colors.accent-deep-navy}` (#272d45) background with white text. Contains link columns, social icons, and legal text. Padding is `{spacing.xxl}` (48px) top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero padding reduces to 32px; buttons become full-width; search bar moves into nav drawer |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero retains full-width with reduced padding (48px); footer columns wrap to 2x2 |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full padding (64px); footer in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; content centered; hero may include parallax or full-bleed imagery |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height
- Nav links have 48px tap area on mobile
- Product card tap targets (image, title, CTA) are at least 48px apart
- Accordion headers have 48px touch height

### Collapsing Strategy
- Nav bar collapses to hamburger menu below 744px
- Product grid reduces columns: 3 → 2 → 1
- Footer columns collapse: 4 → 2 → 1
- Hero text stacks below image on mobile
- Accordion sections collapse by default on all breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.
- Hover and focus states for most components were not reliably extracted from the live site (only active/disabled states for primary button)
- Error and validation styling for forms is inferred from the error color (#f46b3e) but exact border, icon, and message patterns are unknown
- Dark mode is not present on the live site; no dark palette tokens exist
- Sub-brand or seasonal color palettes (e.g., holiday collections) were not extracted
- The exact font weights for Ginto Nord and Ogg Roman are inferred from common usage; the site may use additional weights (e.g., Ginto Nord Light, Ogg Italic)
- Shadow and elevation values (box-shadow, drop-shadow) were not captured from the live CSS
- Animation durations and easing curves (transitions, hover effects) are unknown
- The checkout flow (Shopify-powered) may include third-party payment widget colors (Klarna, Afterpay) that are not part of the brand system
- Stock image dominant tones may have influenced the extracted hex list; the true brand palette may include additional muted earth tones not captured
- The extracted color list includes several generic web colors (#2c3e50, #53b7ff, #dedede) that are likely framework defaults or social icon colors, not brand tokens
