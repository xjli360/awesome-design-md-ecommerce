---
version: alpha
name: "Logitech G"
source_url: "https://www.logitechg.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A high-voltage gaming gear brand that runs on a near-black canvas (#1b1b1b) and two electric accents — a cyan-teal #00fdcf that reads like a live neon tube and a cooler #00b8fc that handles secondary highlights. The palette is deliberately sparse: #d7d7d7 for body text on dark surfaces, #f2f2f2 for light-mode surfaces, and #20a50a as a rare green accent for "in stock" or "online" indicators. The brand trusts darkness as its primary environment — product photography floats in black voids, navigation bars are solid #1b1b1b slabs, and every CTA button is a #00fdcf pill that feels like a power-up collectible. Corners are mostly sharp (`{rounded.none}`) on structural elements like cards and nav, but buttons and badges use `{rounded.full}` to create a clear hierarchy between interactive and informational surfaces. Typography runs a single sans-serif stack at moderate weights — display heads at 24px weight 600, body at 14px weight 400 — because the visual drama comes from the accent colors and the product imagery, not from type gymnastics. The G logo appears as a standalone geometric mark, often in #00fdcf on dark or #1b1b1b on light, and the overall mood is competitive, precise, and slightly industrial — like a pro esports rig rather than a living-room console.

colors:
  primary: "#00fdcf"
  primary-active: "#00d4ab"
  primary-disabled: "#006b59"
  ink: "#1b1b1b"
  body: "#d7d7d7"
  muted: "#9a9a9a"
  muted-soft: "#6a6a6a"
  hairline: "#3a3a3a"
  hairline-soft: "#2a2a2a"
  canvas: "#1b1b1b"
  surface-soft: "#2a2a2a"
  surface-card: "#242424"
  on-primary: "#1b1b1b"
  accent-blue: "#00b8fc"
  accent-green: "#20a50a"
  light-canvas: "#f2f2f2"
  light-body: "#1b1b1b"
  light-muted: "#6a6a6a"
  light-hairline: "#d7d7d7"

typography:
  display-xl:
    fontFamily: "'Logitech G Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Logitech G Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Logitech G Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Logitech G Display', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Logitech G Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Logitech G Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Logitech G Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Logitech G Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Logitech G Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Logitech G Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Logitech G Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Logitech G Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Logitech G Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Logitech G Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Logitech G Text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.25px

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
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-icon:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0px
  product-card-image:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-stock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid #ff4444"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.primary}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a pill-shaped button in the brand's signature cyan-teal (#00fdcf). Text is set in uppercase 14px weight 600 on a dark background. On hover, the button shifts to `{colors.primary-active}` (#00d4ab). The disabled state uses `{colors.primary-disabled}` (#006b59) with muted text, signaling the action is unavailable without visual noise.

**`button-secondary`** — An outlined variant with a transparent background and a 2px solid border in `{colors.primary}`. Text is the same uppercase 14px weight 600 in #00fdcf. On hover, the background fills with the primary color and text flips to dark. Used for "Learn More" or "Compare" actions alongside primary buttons.

**`button-tertiary`** — A text-only button with no background or border, using `{colors.body}` (#d7d7d7) for text. On hover, text shifts to `{colors.primary}`. Used for dismissible actions, "Cancel" in forms, or secondary navigation links.

**`button-icon`** — A 40x40px circular icon button on a `{colors.surface-soft}` (#2a2a2a) background. Used for cart, search, or menu toggles in the top nav. On hover, the background brightens to `{colors.hairline}` (#3a3a3a).

### Navigation
**`top-nav`** — A 64px dark bar (`{colors.canvas}` #1b1b1b) with a subtle bottom hairline. Contains the G logo, product category links, and icon buttons for search and cart. Links use `{typography.nav-link}` (14px weight 500) with active links highlighted in `{colors.primary}`. The nav is fixed to the top on desktop and collapses to a hamburger menu on mobile.

**`nav-link-active`** — Active navigation link styled in `{colors.primary}` (#00fdcf) with no background. Inactive links use `{colors.muted}` (#9a9a9a). On hover, inactive links transition to `{colors.body}` (#d7d7d7).

### Cards
**`product-card`** — A zero-corner card on `{colors.surface-card}` (#242424) with no padding at the container level. The product image fills the top edge-to-edge. Below the image, the title uses `{typography.title-sm}` (16px weight 600) and the price uses `{typography.body-sm}` (14px weight 400) in muted. Cards have no border or shadow — the dark surface provides enough separation.

**`product-card-image`** — The image container sits flush against the card edges with no rounding. Product photography is typically high-contrast against the dark background, with the device isolated and lit from above.

### Badges
**`badge-new`** — A small pill badge in `{colors.primary}` (#00fdcf) with dark text, used to flag newly released products. Text is uppercase 11px weight 700.

**`badge-sale`** — A pill badge in `{colors.accent-blue}` (#00b8fc) with dark text, used for promotional pricing or limited-time offers.

**`badge-stock`** — A pill badge in `{colors.accent-green}` (#20a50a) with dark text, used for "In Stock" or "Online" indicators on product detail pages.

### Forms
**`text-input`** — A standard input field on `{colors.surface-soft}` (#2a2a2a) with a `{colors.hairline}` (#3a3a3a) border and `{rounded.sm}` (8px) corners. On focus, the border thickens to 2px and switches to `{colors.primary}`. Error state uses a red border (#ff4444) with no background change.

**`search-bar`** — A pill-shaped search field on `{colors.surface-soft}` with a hairline border. On focus, the border becomes 2px solid `{colors.primary}`. The search icon sits inside the left padding. Used in the top nav and on the search results page.

### Hero
**`hero-section`** — A full-width dark section (`{colors.canvas}`) with generous padding (`{spacing.section}` top/bottom, `{spacing.xl}` sides). Contains a headline in `{typography.display-xl}`, supporting text in `{typography.body-md}`, and a large `{typography.button-md}` CTA button. Product imagery floats in the background or to the right.

**`hero-cta`** — A larger version of the primary button at 48px height with 14px 32px padding. Used exclusively in hero sections to drive the primary conversion action (e.g., "Shop Now" or "Learn More").

### Footer
**`footer`** — A dark footer matching the canvas background with a hairline top border. Links use `{typography.link}` (14px weight 400) in `{colors.muted}` (#9a9a9a) and shift to `{colors.primary}` on hover. The footer contains product categories, support links, legal text, and social icons. Padding is `{spacing.xxl}` (48px) top/bottom and `{spacing.xl}` (32px) sides.

**`divider`** — A 1px horizontal rule in `{colors.hairline}` (#3a3a3a). Used between sections, within cards, and in the footer to separate link groups.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger; product cards stack in single column; hero padding reduces to 32px; search bar moves to overlay; footer links stack vertically |
| Tablet | 744–1128px | Top nav shows limited links (G Hub, Support); product cards in 2-column grid; hero uses 50/50 split layout; search bar remains in nav |
| Desktop | 1128–1440px | Full top nav with all category links; product cards in 3-column grid; hero uses full-width layout with floating product; search bar in nav |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero content centered with max-width 1200px |

### Touch Targets
- All interactive elements (buttons, links, icons) have a minimum touch target of 44x44px on mobile.
- Icon buttons in the top nav are 40x40px with 4px padding around the icon.
- Product card tap targets include the entire card surface, not just the title or price.
- Search bar has a minimum height of 44px on mobile for ease of tapping.

### Collapsing Strategy
- The top nav collapses to a hamburger menu on mobile (< 744px), hiding all category links and secondary navigation.
- Product filters collapse to a "Filter" button that opens a bottom sheet on mobile.
- The footer link columns collapse to accordion-style sections on mobile, with the first column (Products) expanded by default.
- Hero sections reduce padding and stack content vertically on mobile, with the product image appearing below the text.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site. The typography stack above uses a plausible "Logitech G Display" and "Logitech G Text" naming convention — actual font names may differ (e.g., "Logitech G Sans" or a licensed font like "DIN Next" or "Univers"). The extracted hex colors (#d7d7d7, #00fdcf, #1b1b1b, #f2f2f2, #00b8fc, #20a50a) are the source of truth; typography names are inferred.
- Hover and focus states for most components are estimated based on common dark-mode patterns — actual transitions and color shifts may vary.
- Error styling for forms (text color, helper text, icon placement) was not extracted.
- Dark mode vs. light mode behavior is not documented — the site appears to default to dark mode with a light mode option, but the exact toggle behavior and color mappings are unknown.
- Sub-brand palettes (Logitech G for Xbox, Logitech G for PlayStation, Logitech G for PC) may use different accent colors — only the core brand palette is captured here.
- Loading states, skeleton screens, and animation timing are not extracted.
- The extracted hex list includes #20a50a (green) which may be a stock-image dominant tone or a checkout-widget color rather than a brand color — it's included as an accent but may not be consistently used across the site.
- No meta theme-color was found, so the browser chrome color on mobile is unknown.
