---
version: alpha
name: "Bauman Rare Books"
source_url: "https://www.baumanrarebooks.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A gilded, scholarly marketplace where #ebcb45 — a warm, aged-gold yellow — punctuates an otherwise bone-white and pale-gray canvas (#ececec), evoking the patina of leather-bound first editions rather than the sterile white of a modern e-commerce site. The brand leans into its heritage: proxima-nova at moderate weights (400–600) sets a tone of understated erudition, while Arial serves as a pragmatic fallback for system-level text. Signature design moves include a persistent top nav with a deep link structure (Shop, Authors, Browse, About) that mirrors a physical bookstore's taxonomy, and product pages that foreground condition notes and provenance details — the bibliophile's equivalent of a tasting menu. Buttons and CTAs use the gold as a restrained accent, never overwhelming the page; the real drama comes from high-resolution images of rare books, their spines and gilding catching light against the soft gray backdrop. The footer is dense with informational columns (Customer Service, Events, Press, Sign Up), treating the site as a destination for collectors rather than a quick-transaction funnel. There are no hard corners anywhere — inputs and cards use gentle {rounded.sm} radii — but the overall feel is serious and archival, not playful. The extracted palette is sparse (two colors), suggesting a brand that relies on photography and whitespace over chromatic variety.

colors:
  primary: "#ebcb45"
  primary-active: "#d4b42e"
  primary-disabled: "#f2e29a"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#ececec"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#1a1a1a"
  gold-accent: "#ebcb45"
  gold-light: "#f5e68a"

typography:
  display-xl:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  product-card-condition:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the gold #ebcb45 fill against dark text. Used for "Add to Cart", "Checkout", and "Subscribe" actions. On hover, darkens to #d4b42e (`primary-active`); disabled state fades to a pale gold with muted text. The 4px corner radius (`{rounded.sm}`) keeps it refined without feeling sharp. **`button-secondary`** — An outlined variant with a white background and a 1px hairline border. Used for "View Details", "Continue Shopping", and secondary form actions. Active state fills with the soft surface gray. **`button-ghost`** — A text-only button with no border or background, used for inline actions like "Cancel" or "Clear Filters". Hover adds a subtle underline or opacity shift.

### Cards
**`product-card`** — The core inventory display unit: a white card with a 4px radius, containing a book image, title, author, condition note, and price. The price is rendered in the gold accent color to draw the eye. Condition labels (e.g., "Fine", "Near Fine") appear as small badges. Cards sit on the `{colors.surface-soft}` page background with generous spacing between them. On hover, a subtle shadow or border color change indicates interactivity.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height, white background with a soft bottom border. Navigation links are uppercase, 14px, with 0.8px letter-spacing — a deliberate choice that reads as formal and editorial. The active page link gets a gold underline and text color. The nav includes dropdowns for Shop by Category, Authors, and Browse by Binding, mimicking a physical bookstore's organizational logic. A search icon and cart icon sit on the right.

### Forms
**`text-input`** — Standard input fields with a 1px hairline border, 4px radius, and 44px height. On focus, the border shifts to gold. Used for search, newsletter signup, and checkout forms. Labels sit above the input in `{typography.caption}`. **`search-bar`** — A pill-shaped search field with a soft gray background and hairline border, used in the hero and header. Focus state switches the border to gold. Placeholder text reads "Search rare books..." in muted gray.

### Footer
**`footer`** — A dense, multi-column footer on a soft gray background. Columns include: Customer Service (Shipping, Returns, FAQ), About (Our Story, Press, Events), and Connect (Newsletter Signup, Social Links). Links are in muted gray, headings in dark ink. The newsletter signup uses a `text-input` paired with a `button-primary`. The footer also contains copyright and legal text in `{typography.caption}`.

### Badges
**`badge-new`** — A small gold pill used to denote newly acquired inventory. **`badge-sold`** — A gray pill for items that have been sold, rendered in white text on a muted background. Both use 11px uppercase type with tight tracking.

### Hero
**`hero-section`** — A full-width section on the homepage featuring a large book image or collection montage, overlaid with a heading and subheading. The heading uses `display-xl` (36px, weight 600), and the subheading is body text in muted gray. A `search-bar` sits below the text. The hero has no background color — it relies on the image to set the tone.

### Breadcrumbs
**`breadcrumb`** — A simple text-based navigation aid using `{typography.caption}` in muted-soft gray, with the active page in dark ink. Separators are "›" in the same muted tone.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product cards stack single-column; hero text reduces to `display-md`; footer columns stack vertically; search bar moves below hero text; quantity selector and add-to-cart stack vertically |
| Tablet | 744–1128px | Nav links remain but some dropdowns become accordion; product cards display in 2-column grid; hero remains full-width with reduced padding; footer columns display in 2x2 grid |
| Desktop | 1128–1440px | Full nav with dropdowns; product cards in 3-column grid; hero at max width with centered content; footer in 4-column layout |
| Wide | > 1440px | Content max-width at 1440px with centered container; product cards may expand to 4-column grid; hero image scales with viewport; additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch target guidelines.
- Nav hamburger icon is 48x48px with adequate padding.
- Product card tap targets (title, image, price) are at least 44px in height.
- Search bar has a 48px height for easy tapping.
- Footer links have 44px minimum tap area.

### Collapsing Strategy
- On mobile, the top nav collapses to a hamburger menu; dropdowns become expandable accordion panels within the menu.
- The hero section's image and text stack vertically on mobile, with the search bar moving below the text.
- Product cards collapse from a multi-column grid to a single column on mobile.
- The footer's multi-column layout collapses to a single vertical stack on mobile.
- Breadcrumbs may be hidden on mobile and replaced with a "Back" button.
- The quantity selector and add-to-cart button stack vertically on mobile product pages.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is very sparse (only two colors: #ebcb45 and #ececec). The brand likely uses additional accent colors (e.g., for sold badges, error states, or social icons) that could not be reliably extracted. The palette above includes inferred grays and whites based on common e-commerce patterns, but these should be verified against the live site's CSS.
- Font weights beyond the declared "proxima-nova" family (e.g., 300, 700, 800) could not be confirmed. The typography block uses 400, 500, and 600 as reasonable defaults for a scholarly brand.
- Hover states for buttons and links (beyond the primary-active color) are inferred from common patterns. The brand may use subtle shadow or border changes that were not captured.
- Error styling for form inputs (e.g., red borders, error message typography) could not be extracted.
- The brand's dark mode or high-contrast mode preferences are unknown.
- Sub-brand or collection-specific color variations (e.g., for signed editions, first editions, or specific authors) could not be identified.
- The exact border-radius values for cards and inputs are inferred from the general aesthetic; the live site may use slightly different radii.
- The spacing scale is a best-guess based on typical e-commerce layouts; the brand may use a custom spacing system.
- The hero section's overlay gradient or shadow treatment could not be extracted.
- The brand's icon set (e.g., search, cart, social) and their specific colors are unknown.
- The footer's newsletter signup form behavior (success/error states) is not documented.
