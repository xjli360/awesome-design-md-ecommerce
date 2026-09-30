---
version: alpha
name: "Weezie"
source_url: "https://weezietowels.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Weezie is a bath-and-lifestyle brand that wraps the ritual of toweling in quiet luxury and personal expression. The palette is anchored by a deep navy ink (`#14334c`) that reads as both nautical and residential — it appears on primary buttons, navigation bars, and monogrammed embroidery, giving every interaction a sense of weight and permanence. Against this, the canvas is a warm off-white (`#f3f3f3`) rather than a sterile pure white, softened further by surface cards in `#dedede` and muted hairlines in `#333333`. Accents arrive as restrained punches: a coral `#ff8f77` for sale badges and highlight tags, a crisp `#334fb4` for secondary CTAs, and a pale sky `#a7cfe9` that surfaces in illustrations and seasonal palettes. The typography system is deliberately eclectic — Apercu (in regular, bold, light, and medium weights) carries body and UI copy with a clean, slightly condensed European feel, while display headlines and monogram lockups use the serifed warmth of Clearface or the hand-drawn charm of Birdie and Blue Vinyl. Rounded corners are generous but not cartoonish: buttons use `{rounded.sm}` (8px), product cards use `{rounded.md}` (12px), and the signature search bar uses `{rounded.full}` (pill shape). The brand trusts negative space, low-contrast text hierarchies, and the tactile promise of thick cotton over aggressive marketing noise — every component feels like it belongs in a calm, well-edited bathroom.

colors:
  primary: "#14334c"
  primary-active: "#0f263a"
  primary-disabled: "#a7cfe9"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#f3f3f3"
  canvas: "#f3f3f3"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-coral: "#ff8f77"
  accent-blue: "#334fb4"
  accent-sky: "#a7cfe9"
  accent-navy-light: "#136f99"
  accent-navy-mid: "#1990c6"
  accent-red: "#ba1f31"
  badge-sale: "#ff8f77"
  badge-new: "#334fb4"
  monogram-thread: "#14334c"
  scrim: "#242833"

typography:
  display-xl:
    fontFamily: "'Clearface', 'Apercu', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Clearface', 'Apercu', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Apercu', 'Apercu Medium', -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Apercu', 'Apercu Medium', -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Apercu', 'Apercu Medium', -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Apercu', 'Apercu Medium', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Apercu', 'Apercu Light', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Apercu', 'Apercu Light', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Apercu', 'Apercu Light', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Apercu', 'Apercu Medium', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Apercu', 'Apercu Medium', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "'Apercu', 'Apercu Medium', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Apercu', 'Apercu Medium', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'Apercu', 'Apercu Bold', -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  monogram:
    fontFamily: "'Birdie', 'Blue Vinyl', 'Clearface', cursive"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 2px

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
  button-primary-hover:
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
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 14px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.accent-sky}"
  nav-bar:
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
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 56px
  search-bar-icon:
    color: "{colors.muted}"
    size: 20px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "3/4"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-monogram:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.monogram}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 48px
  color-swatch:
    rounded: "{rounded.full}"
    size: 32px
  color-swatch-selected:
    outline: "2px solid {colors.primary}"
    outlineOffset: "2px"
  monogram-preview:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.monogram}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Shop Now" across the site. Rendered in the deep navy `#14334c` with white text and 8px rounded corners. On hover, it shifts to `#0f263a` for a subtle darkening effect. The disabled state uses `#a7cfe9`, a pale sky blue that signals inactivity without visual noise. Height is fixed at 48px with 14px vertical and 32px horizontal padding.

**`button-secondary`** — An outlined or ghost variant used for "Learn More" and secondary checkout actions. Uses the canvas background (`#f3f3f3`) with navy text, a 1px solid `#14334c` border, and the same 48px height as the primary. Hover fills the background with `#dedede` for a soft press effect.

**`button-tertiary`** — A text-only link styled as a button, used for "View Details" and "See All" links. Transparent background with navy text and no border, relying on the typography system's `button-md` for weight and spacing.

**`button-pill`** — A compact, fully rounded variant used for filter tags, monogram preview toggles, and quick-add actions. Uses the same navy background but at 40px height with tighter padding (10px 24px) and smaller type (`button-sm`).

### Cards
**`product-card`** — The primary product display unit, a white card with 12px rounded corners and no internal padding (images bleed to the top corners). The image area uses a 3:4 aspect ratio with top-rounded corners only. Title uses `title-sm` (16px, medium weight) and price uses `body-sm` (14px, light weight) for a clear but understated hierarchy.

**`hero-section`** — Full-width promotional sections that pair a large headline (`display-xl`, 48px Clearface) with a primary CTA button. Background is the warm canvas `#f3f3f3` with generous section padding (64px vertical, 24px horizontal). Used for seasonal collections and brand storytelling.

### Navigation
**`nav-bar`** — A fixed top navigation at 72px height on a `#f3f3f3` background. Links are set in `nav-link` (13px, medium weight, 0.8px letter spacing, uppercase) for a refined, editorial feel. Active links use the primary navy; inactive links use `#333333`. The bar includes the logo, main links, search icon, and cart icon.

**`nav-link-active`** — Active navigation state with navy text and no background change, relying on color alone for differentiation.

**`nav-link-inactive`** — Inactive navigation state using `#333333` body text, maintaining the same typography for consistency.

### Forms
**`text-input`** — Standard form input for checkout fields, gift messages, and monogram text entry. White background with 8px rounded corners, 48px height, and 14px padding. On focus, it gains a 2px navy border with a sky blue (`#a7cfe9`) box-shadow ring for clear accessibility.

**`search-bar`** — The site's signature search component, a pill-shaped input at 56px height with full rounding. White background with navy text and a muted gray search icon. Used in the navigation and on search result pages.

**`quantity-selector`** — A compact input for selecting product quantities, styled as a white card with 8px rounded corners and 48px height. Includes minus/plus buttons flanking the numeric value.

### Badges & Tags
**`badge-sale`** — A coral (`#ff8f77`) badge used for sale items and promotional tags. Small 4px rounded corners with 4px 8px padding and bold 11px type. Rendered as an inline block that overlays product card images.

**`badge-new`** — A blue (`#334fb4`) badge for new arrivals and limited-edition drops. Same dimensions and typography as the sale badge but in the brand's crisp accent blue.

**`badge-monogram`** — A special badge that previews monogrammed text in the brand's cursive font stack (Birdie, Blue Vinyl, Clearface). Navy background with white text, 8px rounded corners, and generous 8px 16px padding to accommodate the decorative script.

### Footer
**`footer`** — A full-width footer on the deep navy `#14334c` background with white text. Uses `body-sm` for general content and `link` for navigation links. Padding is 48px vertical and 24px horizontal. Includes columns for customer service, about links, and social media icons.

### Accordion
**`accordion`** — Collapsible sections used for product details, shipping information, and FAQ content. White background with 8px rounded corners, 16px vertical padding, and 24px horizontal padding. The header uses `title-sm` and the expanded content uses `body-md` in `#333333`.

### Color Swatches
**`color-swatch`** — Circular 32px swatches for product color selection. Fully rounded with a 2px navy outline on the selected state, offset by 2px for clear visibility. Used in product detail pages and collection filters.

### Monogram Preview
**`monogram-preview`** — A dedicated component for previewing custom embroidery. Uses the canvas background with navy text in the cursive monogram font. 12px rounded corners with 24px padding. This is a signature Weezie feature that appears on product detail pages and the monogramming customization flow.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger nav, product cards stack full-width, hero text reduces to `display-lg`, search bar collapses to icon-only, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, expanded nav links, hero uses `display-xl` at 36px, search bar remains visible but shorter (48px), footer uses two-column layout |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, hero at full `display-xl` (48px), search bar at 56px, footer uses four-column layout |
| Wide | > 1440px | Max-width container at 1440px, four-column product grid, hero content centered with max-width 800px, all components scale proportionally |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Color swatches are 32px with 8px touch padding for comfortable selection
- Accordion headers are 48px tall for easy tapping
- Navigation links have 16px vertical padding within the 72px nav bar
- Quantity selector buttons are 44px wide for thumb-friendly interaction

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-out drawer
- Product grids reduce from 4 columns to 2 to 1 as viewport shrinks
- Hero sections stack vertically on mobile (headline above CTA, image below)
- Footer columns collapse to a single stack on mobile, with accordion-style section headers
- Search bar reduces to an icon-only trigger on mobile, expanding to a full-screen overlay
- Product filters collapse to a bottom sheet on mobile, with a "Filter" button trigger

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons could not be fully extracted (assumed standard darkening/underline patterns)
- Error styling for form inputs (border colors, error message typography) not reliably captured from the live site
- Focus ring styles beyond the text-input focus state are inferred; actual implementation may use different offsets or colors
- Dark mode is not present on the live site; no dark palette tokens are defined
- Sub-brand or seasonal palette variations (e.g., holiday collections, limited-edition drops) may introduce additional accent colors not captured here
- Monogram font stack (Birdie, Blue Vinyl, Clearface) is inferred from font declarations; actual rendering may vary by browser and operating system
- Animation and transition durations (e.g., button hover, accordion expand, nav drawer slide) are not specified; standard 200-300ms ease-in-out is assumed
- Loading states (skeleton screens, spinners) are not documented; the brand may use custom loading patterns
- The `Ardsley Center`, `Ardsley Left`, `Ardsley Right`, `Crosby Center`, `Crosby Left`, `Crosby Right`, `Deuce`, and `Dink` font families were found in declarations but their usage context (headlines, decorative elements, or legacy content) could not be determined
- Shopify-specific components (cart drawer, checkout buttons, product variant selectors) may have platform-default styling that overrides the design system
