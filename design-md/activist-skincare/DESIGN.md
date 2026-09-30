---
version: alpha
name: "Activist Skincare"
source_url: "https://activistskincare.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand built on the conviction that effective skincare and environmental responsibility are not mutually exclusive, Activist Skincare communicates its mission through a palette rooted in nature and a typographic voice that feels both grounded and modern. The primary green (#108474) acts as the brand's visual anchor, appearing across buttons, badges, and key interactive elements, while a deeper forest tone (#0a4021) provides weight and hierarchy. The canvas is a warm off-white (#f9fafb) that softens the digital experience, complemented by a secondary cream (#f8f2e3) that evokes recycled paper and sustainable packaging. Accents of yellow (#fbcd0a) and teal (#c1e6e6) add moments of brightness and freshness, while the extensive use of light grays (#eeeeee, #dddddd, #dadada) creates a clean, airy structure. The brand's signature typographic move is the use of a condensed display font, FeatureDisplayCondensed or Vinila-Compressed, for headlines and hero text, lending a bold, editorial feel that contrasts with the softer, more readable body copy set in Halant or Nunito Sans. This interplay of compressed, assertive headlines and warm, approachable body text mirrors the brand's core message: that activism can be both powerful and inviting. Rounded corners, from soft pills (`{rounded.full}`) to gentle card radii (`{rounded.sm}`), reinforce a tactile, approachable quality, while generous spacing (`{spacing.section}`) gives each product and message room to breathe, avoiding the clutter of conventional beauty e-commerce.

colors:
  primary: "#108474"
  primary-active: "#0a4021"
  primary-disabled: "#c1e6e6"
  ink: "#333333"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#888888"
  hairline: "#cccccc"
  hairline-soft: "#dadada"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fbcd0a"
  accent-teal: "#c1e6e6"
  accent-purple: "#a89cc8"
  accent-blue: "#1990c6"
  badge-green: "#0a4021"
  badge-cream: "#f8f2e3"
  star-rating: "#ffff00"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Vinila-Compressed', 'FeatureDisplayCondensed', Impact, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Vinila-Compressed', 'FeatureDisplayCondensed', Impact, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Vinila-Compressed', 'FeatureDisplayCondensed', Impact, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Halant', Georgia, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Halant', Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
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
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Subscribe & Save", and key conversion points. Rendered in the brand's signature green (`{colors.primary}`) with white text (`{colors.on-primary}`) and a soft 8px radius (`{rounded.sm}`). On hover or active state, the background deepens to a forest green (`{colors.primary-active}`). The disabled state uses a muted teal (`{colors.primary-disabled}`) with gray text to indicate inactivity.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Ingredients". Uses a white background with a 2px solid green border (`{colors.primary}`). On active state, the background shifts to a soft gray (`{colors.surface-soft}`) and the border deepens to `{colors.primary-active}`. Maintains the same 48px height and 8px radius as the primary button for visual consistency.

**`button-pill`** — A smaller, fully rounded variant (`{rounded.full}`) used for filter tags, subscription toggles, and compact CTAs. Uses the same green-to-white color scheme as `button-primary` but at a reduced height (40px) and smaller typography (`{typography.button-sm}`).

### Cards
**`product-card`** — The primary product display unit, a white card (`{colors.surface-card}`) with an 8px radius (`{rounded.sm}`). The product image occupies the top portion with its own rounded top corners (`{rounded.sm} {rounded.sm} 0 0`). Below, product name, a short description, and price are set in `{typography.body-sm}`. A small badge (`{colors.badge-green}`) may overlay the image for "New", "Bestseller", or "Refillable" labels.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height on a white background (`{colors.canvas}`). Links are set in uppercase `{typography.nav-link}` with 0.5px letter-spacing. The active link is underlined with a 2px green border (`{colors.primary}`). The bar includes a centered logo and a right-aligned cart icon with a badge count.

### Forms
**`text-input`** — Standard input fields for email signups, search, and checkout forms. A white background (`{colors.canvas}`) with a 1px light gray border (`{colors.hairline}`) and 8px radius (`{rounded.sm}`). On focus, the border thickens to 2px and turns green (`{colors.primary}`). Placeholder text uses the muted gray (`{colors.muted}`).

### Footer
**`footer-section`** — A deep green footer (`{colors.primary-active}`) with white text. Links are set in `{typography.link}` and maintain the white color. The footer is divided into columns for quick links, sustainability info, and a newsletter signup. Padding is generous at `{spacing.xxl}` top and bottom.

### Accordion
**`accordion-header`** — Used for FAQ sections and product details. The header has a soft gray background (`{colors.surface-soft}`) with a serif title (`{typography.title-sm}`). On click, it expands to reveal `accordion-content` with a white background and body text. Both sections share the same 8px radius and padding.

### Quantity Selector
**`quantity-selector`** — A compact control for adjusting product quantities on the cart or product page. A white background with a 1px border (`{colors.hairline}`) and 8px radius. Contains minus, number, and plus buttons, all at 40px height.

### Star Rating
**`star-rating`** — A visual rating component using yellow stars (`{colors.star-rating}`) at 16px. Used on product cards and review sections to display customer ratings.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero text reduces to `{typography.display-lg}`; footer columns stack; search bar becomes full-width. |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links; hero uses `{typography.display-xl}`; footer columns arrange in a 2x2 grid. |
| Desktop | 1128–1440px | Full three-column product grid; nav-bar shows all primary links; hero uses full `{typography.display-xl}`; footer columns in a single row. |
| Wide | > 1440px | Max-width container at 1440px; content remains centered; additional whitespace on sides; hero may include a larger background image. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px.
- Nav-bar links have a minimum height of 48px for tap targets.
- Quantity selector buttons are at least 40x40px.
- Accordion headers are at least 48px tall.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer.
- Product filters collapse into a single "Filter" button that opens a modal or overlay.
- Footer columns collapse into a single column with accordion-style section headers.
- Multi-column product grids collapse to single-column on mobile.
- Hero sections may reduce to a single image with text overlay.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons and text inputs could not be reliably extracted from the live site.
- Error styling for form inputs (e.g., red borders, error messages) was not observed.
- Sub-brand or campaign-specific palettes (e.g., for limited editions) are not captured.
- Dark mode styles are not present in the extracted data.
- Specific font weights for each typography token were inferred from common web usage; exact weights from the live site may vary.
- The exact `letterSpacing` and `lineHeight` values for typography tokens are estimated based on standard practices for the identified fonts.
- Animation and transition durations (e.g., button hover, accordion expand) were not extracted.
- The `star-rating` color (`#ffff00`) is a pure yellow; it may be used in a semi-transparent or gradient form on the live site.
- The `scrim` color (`#121212`) is assumed for overlays; its opacity is unknown.
- The `fontFamily` for `display-*` tokens uses `!important` in the extracted CSS, suggesting a high specificity override; this may impact theming.
