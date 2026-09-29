---
version: alpha
name: "Finex"
source_url: "https://finexusa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Finex is a cast iron cookware brand that feels both heirloom and industrial, grounded in a deep, earthy green (#108474) that appears across primary buttons, badges, and accent elements. The brand's visual identity is built on a warm, slightly off-white canvas (#f9fafb) with soft surfaces (#f2f2f2, #eeeeee) that evoke the patina of well-seasoned iron. Typography relies on a clean sans-serif stack (Jost, Nunito Sans, Arial) with generous letter-spacing in display sizes, creating a modern, approachable feel that contrasts with the ruggedness of the product. Signature design moves include the use of a warm gold accent (#cb932d, #fbcd0a) for highlights, badges, and secondary CTAs, and a consistent application of soft rounded corners (`{rounded.sm}` to `{rounded.md}`) on cards and buttons that soften the industrial material. The mood is confident and craft-forward — dark ink (#333333, #161616) on light canvas, with muted text (#555555, #666666) for secondary information, and a hairline (#dddddd, #cccccc) that defines product cards and input fields without adding visual noise. The brand trusts photography of its cast iron in use over heavy typographic hierarchy, and the color palette supports this with a restrained range of neutrals punctuated by that signature green and gold.

colors:
  primary: "#108474"
  primary-active: "#0d6b5c"
  primary-disabled: "#a8d5cc"
  ink: "#333333"
  body: "#555555"
  muted: "#666666"
  muted-soft: "#7b7b7b"
  hairline: "#dddddd"
  hairline-soft: "#e9e9e9"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#cb932d"
  accent-gold-light: "#fbcd0a"
  accent-teal: "#c1e6e6"
  accent-purple: "#a89cc8"
  badge-new: "#ffff00"
  badge-sale: "#1990c6"
  badge-sale-active: "#136f99"
  social-facebook: "#3b5998"

typography:
  display-xl:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
  display-lg:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  display-md:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.25px
  display-sm:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.25px
  title-md:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.25px
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
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    height: 48px
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
    height: 48px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 52px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 44px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  social-icon:
    backgroundColor: "{colors.social-facebook}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
  badge-count:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    padding: 2px 6px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for add-to-cart, checkout, and key conversions. Filled with the brand's signature green (#108474) and white text. On hover, it shifts to a darker green (#0d6b5c). The disabled state uses a lighter, muted green (#a8d5cc). All primary buttons use `{rounded.sm}` for a soft, approachable corner.
**`button-secondary`** — A ghost-style button with a white background and dark ink text, used for secondary actions like "Learn More" or "View Details". An outlined variant (`button-secondary-outline`) uses a transparent background with a green border and text, maintaining the brand's accent color.
**`button-gold`** — An accent button using the warm gold (#cb932d) for promotional CTAs, sale banners, or limited-time offers. It pairs with dark ink text for contrast and readability.
**`button-pill`** — A fully rounded pill button used for filters, tags, or compact actions. Uses the primary green with white text and `{rounded.full}`.

### Cards
**`product-card`** — The primary product display card, used on collection pages and search results. Features a white background, soft rounded corners (`{rounded.md}`), and a subtle shadow (implied by the surface-card color). The product image area uses the same corner radius. Badges overlay the top-left corner of the image.
**`product-card-badge`** — A small, uppercase label for promotions, new arrivals, or sale items. Uses the gold accent (#cb932d) for standard badges, blue (#1990c6) for sale items, and yellow (#ffff00) for new arrivals. All badges use `{rounded.xs}` and tight padding.

### Navigation
**`nav-bar`** — The top navigation bar, fixed at 72px height with a white background. Navigation links use the `nav-link` typography (Jost, 15px, 600 weight, 0.5px letter-spacing). The active link state switches text color to the primary green (#108474). The bar collapses to a hamburger menu on mobile.

### Forms
**`text-input`** — Standard text input fields for search, newsletter signup, and account forms. Uses a white background, `{rounded.sm}`, and 48px height. On focus, the border transitions to the primary green (#108474). Placeholder text uses the muted color (#666666).

### Hero
**`hero-section`** — The full-width hero banner on the homepage and landing pages. Uses a soft gray background (#f2f2f2) with large display typography and a prominent primary CTA button. The hero image typically features product photography with natural lighting.

### Search
**`search-bar`** — A pill-shaped search input with a white background, used in the header and on search result pages. Uses `{rounded.full}` for a friendly, approachable feel. The placeholder text is muted (#666666), and the input text is dark ink (#333333).

### Footer
**`footer-section`** — A dark footer with a deep ink background (#333333) and light text. Links use a muted gray (#7b7b7b) that lightens on hover. Social media icons use brand-specific colors (e.g., Facebook blue #3b5998) in a circular format.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger navigation, stacked product cards, reduced hero height |
| Tablet | 744–1128px | Two-column product grid, visible top nav links (condensed), side-by-side hero content |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links, expanded hero with larger imagery |
| Wide | > 1440px | Max-width container (1440px), centered content, four-column product grid for large collections |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px on mobile.
- Product card tap areas extend to the full card boundary for easy selection.
- Navigation hamburger icon is 48x48px for comfortable tapping.
- Form inputs and buttons are 48px tall to meet accessibility standards.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer for links.
- Product grids collapse from 4 columns on wide screens to 1 column on mobile.
- Hero sections stack vertically on mobile, with text below the image.
- Footer links collapse into accordion-style sections on mobile to save vertical space.
- Search bar reduces in width and may move to a full-screen overlay on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components (only primary button and text-input have documented active/focus states).
- Error styling for form inputs (border color, error message typography, icon placement).
- Loading states (spinner, skeleton, shimmer) for product cards, images, and buttons.
- Dark mode color overrides (the brand's dark footer suggests potential dark mode support, but no full palette is defined).
- Sub-brand or seasonal color palettes (e.g., holiday collections, limited-edition colors).
- Specific shadow values (box-shadow, drop-shadow) for cards, modals, and dropdowns.
- Typography scale for mobile (font sizes may reduce on smaller screens, but exact values are not extracted).
- Animation and transition durations (ease-in-out timing for hover states, page transitions).
- Modal and overlay component styles (background scrim, close button, padding).
- Rating and review component styling (star icons, text layout).
- Quantity selector and variant picker (dropdown, button group, color swatch).
- Cart and checkout flow components (cart item row, summary panel, payment form).
