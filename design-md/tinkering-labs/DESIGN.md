---
version: alpha
name: "Tinkering Labs"
source_url: "https://tinkeringlabs.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand built for the moment a child's hand first touches a motor wire, where #ee5d35 — a hot, almost metallic orange — strikes against #003388, a deep navy that reads less like a sky and more like a circuit-board substrate. The palette is deliberately high-contrast: #ee5d35 powers every primary CTA and hero accent, while #003388 anchors headers, navigation, and the footer, creating a visual tension that mirrors the brand's promise of "messy, creative, real" engineering. Type runs Lato at clean, readable weights — display sits at 24–32px in weight 700, body at 16px weight 400 — with generous line heights that keep instructions and product descriptions from feeling dense. Cards and buttons use {rounded.sm} (8px) corners, a subtle softening that prevents the industrial palette from feeling cold. The hero section typically pairs a full-bleed product photo with an overlaid CTA pill in #ee5d35, while product cards stack a white canvas (#eeeeee) with a navy title and orange price badge. Badges for "Ages 8+" or "New" appear as small {rounded.full} pills in #003388 with white text, echoing the brand's signal that this is serious play. The overall feel is workshop-meets-playroom: clean enough for a parent to trust, bright enough for a kid to grab.

colors:
  primary: "#ee5d35"
  primary-active: "#d44a24"
  primary-disabled: "#f5a88c"
  ink: "#003388"
  body: "#313131"
  muted: "#444444"
  muted-soft: "#abb8c3"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#00d084"
  accent-purple: "#7a00df"
  accent-teal: "#34e2e4"
  badge-new: "#003388"
  badge-sale: "#ee5d35"
  star-rating: "#ff6900"
  error: "#dc3232"
  success: "#00d084"

typography:
  display-xl:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.63
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.3px
  link:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.2px

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    border: "2px solid {colors.ink}"
    padding: 10px 22px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  button-pill-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 700
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  badge-pill:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 600px
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 500px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
    textDecoration: none
  footer-link-hover:
    textDecoration: underline
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "12px 20px"
    height: 48px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.base} 0"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.primary}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 16px
  error-message:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  success-message:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with #ee5d35 and white text. Used for "Add to Cart", "Shop Now", and hero CTAs. On hover, shifts to `{colors.primary-active}` (#d44a24). Disabled state uses `{colors.primary-disabled}` (#f5a88c). Height is 48px with {rounded.sm} corners.

**`button-secondary`** — An outlined button with a 2px `{colors.ink}` border on a white background. Used for "Learn More" or secondary actions. Text is `{colors.ink}`. Hover state fills the background with `{colors.ink}` and inverts text to white.

**`button-tertiary-text`** — A text-only button with no background or border. Used for "Cancel" or "View Details" links. Hover state adds underline.

**`button-pill-primary`** — A pill-shaped variant of the primary button, used for badges or compact CTAs like "Subscribe". Uses {rounded.full} and 40px height.

**`button-pill-ink`** — A pill button in `{colors.ink}` with white text, used for "Ages 8+" or "New" badges in the category strip.

### Cards
**`product-card`** — A white card with a subtle shadow (`0 2px 8px rgba(0,0,0,0.08)`) and {rounded.sm} corners. Contains a square image with rounded top corners, a title in `{colors.ink}` using `{typography.title-sm}`, and a price in `{colors.primary}` using `{typography.body-md}` with weight 700. Hover state raises the shadow to `0 4px 16px rgba(0,0,0,0.12)`.

### Navigation
**`nav-bar`** — A 72px white bar with a bottom hairline. Navigation links use `{typography.nav-link}` (15px, weight 700). Active links turn `{colors.primary}`. The logo sits left-aligned, links center-aligned, and cart/account icons right-aligned.

### Forms
**`text-input`** — A 48px tall input with a 1px `{colors.hairline}` border and {rounded.sm} corners. On focus, the border becomes a 2px `{colors.primary}` stroke with no outline. Placeholder text uses `{colors.muted-soft}`.

### Footer
**`footer`** — A full-width section with `{colors.ink}` background and white text. Links are white with no underline by default, gaining underline on hover. Organized in columns with `{typography.body-sm}` for body copy and `{typography.link}` for links.

### Badges
**`badge-pill`** — A small pill in `{colors.ink}` with white uppercase text (11px, weight 700, 0.5px letter spacing). Used for "New", "Ages 8+", or "Best Seller" tags. Padding is 4px 12px.

**`badge-sale`** — Same as `badge-pill` but with `{colors.primary}` background. Used for "Sale" or "20% Off" tags.

### Hero
**`hero-section`** — A full-width section with `{colors.surface-soft}` background, containing a heading in `{typography.display-xl}` and a subheading in `{typography.body-md}`. The heading is capped at 600px width, the subheading at 500px. A primary CTA button sits below.

### Search
**`search-bar`** — A pill-shaped search input with a 1px `{colors.hairline}` border and {rounded.full} corners. 48px tall with 12px 20px padding. On focus, the border becomes `{colors.primary}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack full-width; hero padding reduces to 32px; font sizes drop one step (display-xl becomes 24px) |
| Tablet | 744–1128px | Two-column product grid; nav links visible but compact; hero text max-width reduces to 80%; search bar moves to nav |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses 600px heading width; category strip scrolls horizontally |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered with larger whitespace |

### Touch Targets
- All buttons and links: minimum 44px height, 44px width for icon-only targets
- Product card tap targets: entire card is clickable
- Nav links: 48px minimum tap height
- Search bar: 48px height
- Category strip tabs: 44px minimum height

### Collapsing Strategy
- On mobile (< 744px): nav links collapse into a hamburger menu; product grid collapses to single column; category strip becomes a horizontal scrollable row; footer columns stack vertically
- On tablet (744–1128px): nav links remain visible but "Shop" and "About" may collapse into a "More" dropdown; product grid shows 2 columns; footer shows 2 columns
- On desktop: full layout with no collapsing

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list contains 30+ hex values, many of which appear to be default WordPress/Gutenberg palette colors (e.g., #00d084, #0693e3, #cf2e2e). The true brand palette likely centers on #ee5d35 (orange) and #003388 (navy), but hover states, disabled states, and secondary accents are inferred from common patterns rather than extracted.
- Font-family declarations only returned "Lato" from the live site. Fallback stacks are assumed based on common web standards.
- No meta theme-color was found; the brand may not set one, or it may be set via JavaScript.
- The platform is not Shopify; the brand likely uses WordPress/WooCommerce or a custom solution. Checkout and cart component styling is unknown.
- Hover states for buttons and links are inferred from common accessibility patterns (darkening primary, underlining links).
- Error and success message styling is assumed from the palette; no live error states were extracted.
- Dark mode is not supported and no dark-mode tokens are defined.
- Sub-brand or seasonal palette variations (e.g., holiday themes) are not captured.
- Typography line heights and letter spacing are estimated from typical Lato usage; the live site may use different values.
- Spacing scale is based on common 4px/8px systems; the live site may use a different rhythm.
- Component heights (48px for buttons, 72px for nav) are standard estimates; actual values may vary.
- The extracted hex list includes #faaca8 (pink), #dad0ec (lavender), #fafae1 (cream), #67a671 (sage), #fdd79a (peach), #004a59 (teal), #330968 (deep purple), #31cdcf (cyan), #020381 (dark blue), #2874fc (bright blue), #f78da7 (pink), #ff6900 (orange) — these may be used for specific product categories, seasonal promotions, or illustration accents, but their exact roles are unknown.
