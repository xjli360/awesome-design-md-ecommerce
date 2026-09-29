---
version: alpha
name: "Milestone Films"
source_url: "https://www.milestonefilms.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, cinephile-grey canvas (#1c1b1b) that feels like a 35mm frame before the projector starts — the site is a digital archive of independent and restored cinema, and its palette reads like a film-stock contact sheet: warm blacks, silver-grey mids (#cfcfcf, #6a6a6a), and a single urgent orange-red (#fc4c03) that punches through for CTAs and price badges like a "NOW SHOWING" marquee. The typography runs Montserrat at clean, readable weights — display titles sit in bold 600, body text in 400 with generous line-height — and Nunito Sans appears for secondary copy, giving the interface a slightly European, art-house feel. Buttons are sharp-cornered rectangles (`{rounded.none}`) with the orange-red fill, a deliberate choice that says "buy a ticket, no fuss," while product cards for Blu-rays and DVDs use soft grey borders (`{rounded.sm}`) and white canvases (`{colors.canvas}`) to let cover art breathe. The nav bar is a fixed dark strip (`{colors.ink}`) with white links, and the footer collapses into a dense, information-rich block of links and social icons — blue Twitter (#00aced), blue Facebook (#4469af), red YouTube (#c8232c) — each a raw platform color, unmediated. There is no hero animation, no parallax; the site trusts the magnetism of film posters and the authority of a well-organized grid. The overall mood is that of a repertory cinema lobby: serious, welcoming, and lit by the glow of a marquee.

colors:
  primary: "#fc4c03"
  primary-active: "#e04000"
  primary-disabled: "#fca07a"
  ink: "#1c1b1b"
  body: "#363636"
  muted: "#6a6a6a"
  muted-soft: "#909090"
  hairline: "#cfcfcf"
  hairline-soft: "#e9e9e9"
  canvas: "#ffffff"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#4469af"
  link-hover: "#2b00ff"
  error: "#c8232c"
  success: "#307a07"
  social-twitter: "#00aced"
  social-facebook: "#4469af"
  social-youtube: "#c8232c"
  sale-badge: "#fc4c03"
  sold-out-badge: "#555555"
  price: "#1c1b1b"
  star-rating: "#f45b4f"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Nunito Sans', 'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', 'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Nunito Sans', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  footer-link:
    fontFamily: "'Nunito Sans', 'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.muted}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.link}"
    padding: 0
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-link-item:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-item-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    margin-top: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    color: "{colors.price}"
  product-card-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  product-card-sold-out:
    backgroundColor: "{colors.sold-out-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    height: 44px
    padding: "0 16px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.footer-link}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link-item:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.footer-link}"
    padding: "4px 0"
  footer-link-item-hover:
    textColor: "{colors.on-dark}"
  social-icon-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.none}"
    height: 32px
  social-icon-link-hover:
    textColor: "{colors.on-dark}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    margin-bottom: "{spacing.lg}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-link:
    color: "{colors.link}"
  breadcrumb-current:
    color: "{colors.ink}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the marquee orange `{colors.primary}` and set in uppercase Montserrat 600. Sharp corners (`{rounded.none}`) reinforce a no-nonsense, ticket-booth directness. On hover, the fill deepens to `{colors.primary-active}`; disabled state uses `{colors.primary-disabled}` with the same sharp geometry.

**`button-secondary`** — An outlined variant with a white fill, ink text, and a 1px `{colors.hairline}` border. Used for "Add to Wishlist" or "View Details" actions alongside primary buttons. Active state swaps the border to `{colors.muted}` and the background to `{colors.surface-soft}`.

**`button-link`** — A text-only button styled as a hyperlink, using `{colors.link}` blue and `{typography.link}`. Used for inline actions like "Read More" or "View All" within product descriptions.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with a soft 4px radius (`{rounded.sm}`) and 8px padding. The card contains a product image (typically a film poster or Blu-ray cover), a title in `{typography.title-sm}`, and a price in bold `{typography.body-md}`. A badge overlay — either `{colors.sale-badge}` orange for sale items or `{colors.sold-out-badge}` grey for out-of-stock — sits in the top-left corner, set in uppercase `{typography.badge}`.

### Navigation
**`nav-bar`** — A fixed 64px dark bar (`{colors.ink}`) spanning the full viewport width. Navigation links use `{typography.nav-link}` in white with uppercase lettering and 0.3px tracking. The active or hovered link switches to `{colors.primary}` orange. The bar contains the brand logo on the left and a collapsible menu on the right for mobile.

**`nav-link-item`** — Individual navigation links with 8px/12px padding. On desktop, they sit horizontally; on mobile, they stack vertically in a slide-out drawer.

### Forms
**`text-input`** — A standard input field with a white background, 1px `{colors.hairline}` border, and sharp corners. Focus state uses a 1px `{colors.ink}` border; error state uses `{colors.error}` red. Height is 44px with 10px/12px padding for comfortable text entry.

**`search-bar`** — A dedicated search input with a 1px `{colors.hairline}` border and a `{colors.primary}` submit button attached. The input uses `{typography.body-md}` for legibility. On mobile, the search bar may collapse into an icon that expands on tap.

### Footer
**`footer`** — A dense, dark footer (`{colors.ink}`) with multiple columns of links in `{typography.footer-link}`. Links are `{colors.muted-soft}` by default and lighten to `{colors.on-dark}` on hover. Social media icons use raw brand colors (`{colors.social-twitter}`, `{colors.social-facebook}`, `{colors.social-youtube}`) on hover, matching the platform's native identity.

### Hero & Sections
**`hero-banner`** — A full-width dark section (`{colors.ink}`) with white text in `{typography.display-lg}`. Used for featured film collections or seasonal promotions. Padding is `{spacing.section}` (64px) top and bottom, with `{spacing.lg}` on the sides.

**`section-heading`** — A `{typography.display-md}` heading in `{colors.ink}` with `{spacing.lg}` bottom margin. Used to label product categories, collections, or informational sections.

### Pagination
**`pagination-button`** — A square button with a white background, 1px `{colors.hairline}` border, and sharp corners. The active page uses `{colors.primary}` fill with white text. Buttons are 8px/12px padded and use `{typography.body-sm}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in single column; hero banner reduces padding to `{spacing.xl}`; search bar becomes icon-only; footer columns stack vertically. |
| Tablet | 744–1128px | Nav links remain visible but may wrap; product cards display in 2-column grid; hero banner uses `{spacing.xxl}` padding; search bar remains expanded. |
| Desktop | 1128–1440px | Full nav bar with all links; product cards in 3- or 4-column grid; hero banner uses `{spacing.section}` padding; footer displays in 3–4 columns. |
| Wide | > 1440px | Max-width container (1440px) centered; product cards may expand to 4–5 columns; hero banner content centered with generous margins. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch-target guidelines.
- Nav bar links have 12px horizontal padding to ensure comfortable tap areas.
- Social icon links are 32px × 32px with additional 8px padding for touch.
- Pagination buttons are at least 36px × 36px.

### Collapsing Strategy
- **Nav bar**: On mobile (< 744px), the full nav link list collapses into a hamburger menu icon. Tapping opens a vertical slide-out drawer with all links stacked.
- **Search bar**: On mobile, the search input collapses into a magnifying-glass icon. Tapping expands the full input field below the nav bar.
- **Product grid**: On mobile, the multi-column grid collapses to a single column. On tablet, it collapses to 2 columns.
- **Footer**: On mobile, the multi-column footer collapses to a single column with links stacked. On tablet, it collapses to 2 columns.
- **Hero banner**: On mobile, the hero banner's padding reduces from `{spacing.section}` to `{spacing.xl}`, and any side-by-side content stacks vertically.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (e.g., product-card image zoom, text-input focus ring) could not be reliably extracted from the static HTML/CSS.
- Error styling for form validation (error messages, input border colors on invalid state) is inferred from the `{colors.error}` value but not confirmed.
- The exact font weights for Montserrat and Nunito Sans in use are estimated from the extracted font-family declarations; the live site may use additional weights (e.g., 300, 700) not captured.
- Sub-brand or collection-specific color palettes (e.g., for "Milestone Classics" or "World Cinema") are not documented.
- Dark mode preferences are not supported; the site appears to use a fixed light/dark scheme.
- The `meta theme-color` was not set, so browser chrome styling is undefined.
- The extracted hex list includes many generic web colors (multiple greys, blues, reds) that may be from Shopify widgets, social icons, or stock images rather than intentional brand choices. The primary `#fc4c03` (orange-red) was selected as the most distinctive accent, but its exact usage (e.g., as a button color vs. a badge color) is inferred from common e-commerce patterns.
- Animation and transition durations (e.g., hover effects, menu slide-in) are not documented.
- The `object-fit: cover` declaration suggests images are cropped to fill containers, but exact aspect ratios for product cards and hero banners are unknown.
