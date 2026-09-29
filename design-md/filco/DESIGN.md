---
version: alpha
name: "Filco"
source_url: "https://www.diatec.co.jp"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A Japanese keyboard manufacturer that has been producing mechanical keyboards since 1992, Filco's design language is one of deliberate restraint — a near-total absence of branding on the product itself, with the logo appearing only on the packaging and the included keycap puller. The site lives on a #f5f5f5 canvas, a warm off-white that reads as paper stock rather than screen white, and the product photography is shot on the same tone so the keyboards appear to float in their own atmosphere. Every keyboard is shown from a straight-on top-down angle, the keycaps rendered in crisp focus against that soft ground, with no lifestyle shots, no hands typing, no desk setups — just the object itself, presented with the seriousness of a tool. The navigation is a single horizontal strip of Japanese text (the site's primary language) with no dropdowns, no mega-menus, no search bar visible on load, and the product pages are built as long scrolls of technical specifications rather than marketing copy. The color palette is monochromatic — the keyboards themselves come in black, white, and occasionally navy or red — and the only accent color on the site is the deep navy of the footer background, which creates a hard visual stop at the bottom of every page. There are no animations, no hover effects beyond a simple underline on text links, and no JavaScript-driven interactivity on the product pages; the site functions as a catalog, not a storefront. The typography is system sans-serif at modest sizes, with product names set at 18px and body text at 12px, creating a dense information hierarchy that prioritizes specification density over readability. The overall effect is that of a PDF catalog rendered as a website — utilitarian, information-rich, and utterly indifferent to the conventions of modern DTC design.

colors:
  primary: "#f5f5f5"
  primary-active: "#e0e0e0"
  primary-disabled: "#fafafa"
  ink: "#333333"
  body: "#555555"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#cccccc"
  hairline-soft: "#dddddd"
  canvas: "#f5f5f5"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  footer-bg: "#1a1a2e"
  footer-text: "#cccccc"
  on-primary: "#333333"
  accent-red: "#cc0000"
  accent-navy: "#1a1a2e"

typography:
  display-xl:
    fontFamily: "sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  spec-label:
    fontFamily: "sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  spec-value:
    fontFamily: "sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    height: 32px
  button-primary-hover:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 7px 15px
    height: 32px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 6px 10px
    height: 30px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  product-card-image:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  product-card-name:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.spec-value}"
    rounded: "{rounded.none}"
    padding: "{spacing.md}"
  product-spec-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
    textDecoration: "underline"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  page-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.md}"
    borderBottom: "1px solid {colors.hairline-soft}"
    paddingBottom: "{spacing.sm}"

## Components

### Buttons
**`button-primary`** — A solid dark rectangle with no border radius, using white text on the ink background. The button is compact at 32px height with 8px horizontal padding, matching the dense information density of the site. On hover, the background shifts to the footer navy for a subtle state change. There is no disabled state styling visible on the live site.
**`button-secondary`** — An outlined version with a 1px hairline border on the canvas background. The text remains ink-colored, and on hover the background fills with the soft hairline tone. Used for secondary actions like "View Details" on product listing pages.

### Navigation
**`nav-bar`** — A minimal 48px strip with a soft bottom border, containing text links in Japanese. The active link gets a 2px bottom border in ink, while inactive links render in muted gray. There are no dropdowns, no search bar, and no icons — just a horizontal row of text. The navigation does not collapse on mobile; it wraps to a second line if needed.
**`breadcrumb`** — Simple text-based breadcrumbs in caption size, with muted gray for non-active segments and ink for the current page. No arrows or separators are used; segments are separated by a space or a simple ">" character.

### Product Cards
**`product-card`** — A minimal card with no border, no shadow, and no border radius. The product image sits on the canvas background, and the product name appears below in title-sm weight. The price follows in body-sm in muted gray. There is no hover effect on the card itself — the entire card may be clickable, but there is no visual feedback. The card uses base padding around its content.

### Product Specifications
**`product-spec-table`** — A dense table of technical specifications rendered on a soft surface background. Each row contains a spec label in bold caption size and a spec value in regular caption size. The table has no borders, no alternating row colors, and no visual hierarchy beyond the weight difference between label and value. Used extensively on product detail pages where the keyboard's switch type, keycap material, interface, and dimensions are listed.

### Footer
**`footer`** — A deep navy (#1a1a2e) band at the bottom of every page, creating a hard visual stop. Text is rendered in light gray (#cccccc) at body-sm size. Links are underlined. The footer contains company information, support links, and legal text. There is no newsletter signup, no social media icons, and no decorative elements.

### Typography System
**`page-title`** — The largest text on the page at 24px bold, used for product names and category headings. It sits on the canvas with no decoration.
**`section-heading`** — An 18px bold heading with a soft bottom border, used to separate sections on product detail pages. The border is a single hairline-soft line with 8px bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Product cards stack in single column; navigation wraps to two lines; spec tables remain full-width but text may scale down |
| Tablet | 744–1128px | Product cards display in 2-column grid; navigation remains horizontal; spec tables maintain two-column layout |
| Desktop | 1128–1440px | Product cards display in 3-column grid; full navigation visible; spec tables use wider columns |
| Wide | > 1440px | Content max-width caps at 1200px; margins increase; layout remains identical to desktop |

### Touch Targets
- Navigation links are text-only with no minimum touch target size enforced
- Buttons at 32px height are below the recommended 44px minimum for touch
- Product cards are likely clickable but have no explicit touch target sizing

### Collapsing Strategy
- Navigation does not collapse to a hamburger menu; it wraps to a second line on narrow screens
- Product images do not collapse or reflow; they scale down proportionally
- Spec tables do not collapse to accordion; they remain as full-width tables that may require horizontal scrolling on very narrow screens
- Footer links do not collapse; they stack vertically on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#f5f5f5) was extractable from the live site; all other colors in this document are inferred from screenshots and general observation of the brand's visual language
- The site uses system sans-serif with no specific font-family declaration beyond "sans-serif"; no custom typeface could be identified
- Hover states for buttons and links are inferred from common web patterns, not extracted from the live site
- No form error states, validation styling, or disabled button styling could be observed
- The site appears to have no dark mode, no mobile hamburger menu, and no interactive components beyond basic links
- No search component, cart icon, or user account navigation could be found on the live site
- The brand's product color variants (black, white, navy, red) are inferred from product photography, not from any color swatch UI on the site
- No animation, transition, or micro-interaction timing data could be extracted
- The site is primarily in Japanese; English translations of navigation labels and product names were not extracted
