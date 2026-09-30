---
version: alpha
name: "Record Grouch"
source_url: "https://www.recordgrouch.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record store that wears its red like a badge of honor — #cc3b3b, the primary voltage, appears on buttons, badges, and sale tags against a near-white canvas of #f5f5f5 and #fafafa. The brand leans into a high-contrast, almost punk sensibility: deep ink (#222222) for body text, near-black (#111111, #040404) for headers and heavy structural elements, and a secondary red (#bd0000) for active states and urgent callouts. The palette is deliberately limited — no pastels, no gradients, just raw red, white, and black with a single muted gray (#aaaaaa) for secondary text and disabled states. Poppins, set at modest weights (400–600), provides a geometric, slightly playful counterpoint to the aggressive color scheme; it appears in both uppercase navigation links and body copy, giving the site a zine-like editorial feel. The design system is built around hard edges and clear hierarchy: cards use minimal rounding ({rounded.sm} ~8px), buttons are compact rectangles, and the only pill shape appears on search inputs. This is a store that wants you to find what you're looking for fast — no decorative flourishes, no ambient photography, just product, price, and that insistent red.

colors:
  primary: "#cc3b3b"
  primary-active: "#bd0000"
  primary-disabled: "#e99292"
  ink: "#222222"
  body: "#272727"
  muted: "#aaaaaa"
  muted-soft: "#e1e1e1"
  hairline: "#eeeeee"
  hairline-soft: "#fbfbfb"
  canvas: "#f5f5f5"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#bd0000"
  accent-new: "#cc3b3b"
  badge-stock: "#222222"
  badge-sold: "#aaaaaa"

typography:
  display-xl:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.25px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'Poppins', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    color: "{colors.accent-sale}"
    marginTop: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.accent-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold:
    backgroundColor: "{colors.badge-sold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-stock:
    backgroundColor: "{colors.badge-stock}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginTop: "{spacing.md}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.md} 0"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  cart-icon:
    color: "{colors.ink}"
    height: 24px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
    padding: "0 4px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a compact rectangle in `{colors.primary}` (#cc3b3b) with white text set in Poppins 600 uppercase. On hover/active, it shifts to `{colors.primary-active}` (#bd0000) for a darker, more urgent red. The disabled state uses `{colors.primary-disabled}` (#e99292), a washed-out pink that signals unavailability without ambiguity. Padding is tight (12px top/bottom, 24px left/right) to keep buttons from overwhelming the product grid.

**`button-secondary`** — An outlined variant for secondary actions like "Clear Filters" or "Cancel". Uses the same compact dimensions as primary but with a white fill and a 2px solid `{colors.ink}` border. Hover state inverts to `{colors.ink}` fill with white text.

**`button-tertiary`** — A text-only button for inline actions like "View All" or "See Details". Uses `{colors.primary}` for the text color with no background or border, relying on the brand's high-contrast palette for legibility.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with `{rounded.sm}` corners and `{spacing.sm}` padding, sitting on the `{colors.canvas}` (#f5f5f5) background. The product image fills the top with `{rounded.xs}` corners and a 1:1 aspect ratio. Below, the title uses `{typography.title-md}` in `{colors.ink}`, and the price uses `{typography.body-md}` with 600 weight. Sale prices switch to `{colors.accent-sale}` (#bd0000). Badges (New, Sale, Sold, In Stock) overlay the image top-left, using the brand's red or black palette.

### Navigation
**`nav-bar`** — A 64px-high bar on `{colors.canvas}` with `{spacing.lg}` horizontal padding. Links use `{typography.nav-link}` — Poppins 500, uppercase, 1px letter-spacing. The active state turns the link color to `{colors.primary}`. The cart icon sits right-aligned with a `{colors.primary}` badge showing item count.

### Forms
**`text-input`** — A standard input field with `{rounded.sm}`, a 1px `{colors.hairline}` border, and 12px/16px padding. On focus, the border thickens to 2px and switches to `{colors.primary}`. The search bar variant uses `{rounded.full}` for a pill shape, matching the brand's single rounded element.

### Badges
**`badge-new`**, **`badge-sale`**, **`badge-sold`**, **`badge-stock`** — Small uppercase labels with `{rounded.xs}` corners and 2px/8px padding. New and Sale use the brand's reds (#cc3b3b and #bd0000 respectively); Sold uses `{colors.badge-sold}` (#aaaaaa); In Stock uses `{colors.badge-stock}` (#222222). All have white text for maximum contrast.

### Footer
**`footer`** — A dark band in `{colors.ink}` (#222222) with white body text. Links use `{colors.muted-soft}` (#e1e1e1) for a softer contrast. Padding is generous at `{spacing.xxl}` top/bottom and `{spacing.lg}` sides.

### Hero
**`hero-section`** — A full-width section on `{colors.canvas}` with `{spacing.section}` vertical padding. The title uses `{typography.display-xl}` (32px, 600 weight) in `{colors.ink}`, and the subtitle uses `{typography.body-md}` in `{colors.body}` (#272727). No background image or decorative element — just type and whitespace.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 columns); nav collapses to hamburger; hero padding reduces to `{spacing.xl}`; buttons become full-width; search bar moves below nav |
| Tablet | 744–1128px | Two-column product grid (3 columns); nav links visible but condensed; hero maintains `{spacing.section}` padding; category strip scrolls horizontally |
| Desktop | 1128–1440px | Three-column product grid (4 columns); full nav with all links; hero at full width; category strip wraps to multiple rows |
| Wide | > 1440px | Four-column product grid (5 columns); max-width container at 1440px; hero content centered; category strip centered |

### Touch Targets
- All buttons and links: minimum 44px height (buttons) and 44x44px tap area for icon-only elements
- Search bar: 48px height for comfortable tapping
- Product cards: entire card is tappable, minimum 120px height
- Category tabs: 44px minimum height with 16px horizontal padding
- Quantity selector: 40px height with 12px horizontal padding

### Collapsing Strategy
- Navigation links collapse to a hamburger menu below 744px
- Category strip becomes a horizontally scrollable row on mobile and tablet
- Product grid reduces from 4–5 columns on wide to 2 columns on mobile
- Hero section reduces vertical padding from `{spacing.section}` to `{spacing.xl}` on mobile
- Search bar moves from inline in the nav to a full-width element below the nav on mobile
- Footer links stack vertically on mobile instead of horizontal rows

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons were not reliably extracted from the live site; the active state (#bd0000) is used as a best-guess hover for primary buttons
- Error styling for form inputs (validation messages, error borders) was not found in the extracted data
- Dark mode is not supported by the brand; no dark-mode tokens were extracted
- Sub-brand or seasonal color palettes (if any) were not detected
- The exact font weight for Poppins in headings (600) is inferred from the extracted font-family declarations and common usage; the live site may use 700 for some display elements
- The `textTransform: uppercase` on button and nav-link typography is inferred from the brand's aesthetic and common record-store design patterns, not extracted from CSS
- The `border` property on `button-secondary` and `text-input` components is inferred from the high-contrast design language; exact border widths and colors may vary
- The `aspectRatio: "1 / 1"` on product card images is a common pattern for record covers but was not explicitly extracted
- The `hero-section` component is inferred from the brand's minimal design language; no hero content was extracted from the live site
- The `quantity-selector` component is a standard e-commerce pattern; its exact styling was not extracted
- The `cart-badge` component's dimensions are inferred from common patterns; exact size may vary
