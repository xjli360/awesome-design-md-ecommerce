---
version: alpha
name: "Taikan"
source_url: "https://www.taikan.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dark, almost obsidian canvas (#131313) is the defining gesture of Taikan — a phone-accessories brand that treats the screen as a vanishing point and the case as a sculptural object. The palette is overwhelmingly black and near-black (#272727, #222222, #3e3e3e, #1d1d1d), with a single sharp accent of #f0523d, a desaturated vermilion that appears on price tags, add-to-cart buttons, and sale badges. Typography runs Clarkson and proxima-nova at modest weights — there is no display face, no decorative serif; the brand communicates through product photography and tight, utilitarian copy blocks. Buttons are pill-shaped (`{rounded.full}`) and sit flush against the dark canvas, while product cards use `{rounded.lg}` corners that echo the rounded bezels of the phones themselves. The footer is a dense grid of links in #aaaaaa on #131313, and social icons appear in their native brand colors (#3b5998 for Facebook, #e4405f for Instagram, #0976b4 for Twitter), suggesting the brand lets platform identity bleed through rather than enforcing a monochrome lockup. The overall effect is of a premium aftermarket — not a case you buy because you have to, but one you choose because it matches the phone's own black-glass minimalism.

colors:
  primary: "#f0523d"
  primary-active: "#cc2127"
  primary-disabled: "#dc5d54"
  ink: "#111111"
  body: "#222222"
  muted: "#aaaaaa"
  muted-soft: "#d0d0d0"
  hairline: "#e4e4e4"
  hairline-soft: "#eeeeee"
  canvas: "#131313"
  surface-soft: "#1d1d1d"
  surface-card: "#272727"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale-badge: "#f0523d"
  price: "#f6f6f6"
  social-facebook: "#3b5998"
  social-instagram: "#e4405f"
  social-twitter: "#0976b4"
  social-youtube: "#cc2127"
  social-pinterest: "#ff6600"
  social-tiktok: "#111111"
  code-highlight: "#ae81ff"
  code-string: "#00b4b3"
  code-keyword: "#f92672"

typography:
  display-xl:
    fontFamily: "'Clarkson', 'proxima-nova', 'Century Gothic', 'CenturyGothic', 'AppleGothic', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Clarkson', 'proxima-nova', 'Century Gothic', 'CenturyGothic', 'AppleGothic', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Clarkson', 'proxima-nova', 'Century Gothic', 'CenturyGothic', 'AppleGothic', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Clarkson', 'proxima-nova', 'Century Gothic', 'CenturyGothic', 'AppleGothic', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Clarkson', 'proxima-nova', 'Century Gothic', 'CenturyGothic', 'AppleGothic', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Clarkson', 'proxima-nova', 'Century Gothic', 'CenturyGothic', 'AppleGothic', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Clarkson', 'proxima-nova', 'Century Gothic', 'CenturyGothic', 'AppleGothic', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Clarkson', 'proxima-nova', 'Century Gothic', 'CenturyGothic', 'AppleGothic', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Clarkson', 'proxima-nova', 'Century Gothic', 'CenturyGothic', 'AppleGothic', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
  link:
    fontFamily: "'Clarkson', 'proxima-nova', 'Century Gothic', 'CenturyGothic', 'AppleGothic', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Clarkson', 'proxima-nova', 'Century Gothic', 'CenturyGothic', 'AppleGothic', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
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
    rounded: "{rounded.full}"
    padding: 14px 32px
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    border: 2px solid "{colors.primary}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
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
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
  product-card-image:
    rounded: "{rounded.lg}"
  product-card-price:
    backgroundColor: transparent
    textColor: "{colors.price}"
    typography: "{typography.body-md}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    textTransform: uppercase
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-facebook:
    backgroundColor: transparent
    textColor: "{colors.social-facebook}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-instagram:
    backgroundColor: transparent
    textColor: "{colors.social-instagram}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-twitter:
    backgroundColor: transparent
    textColor: "{colors.social-twitter}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-youtube:
    backgroundColor: transparent
    textColor: "{colors.social-youtube}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-pinterest:
    backgroundColor: transparent
    textColor: "{colors.social-pinterest}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-tiktok:
    backgroundColor: transparent
    textColor: "{colors.social-tiktok}"
    rounded: "{rounded.full}"
    height: 32px
  code-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
  code-highlight:
    backgroundColor: transparent
    textColor: "{colors.code-highlight}"
  code-string:
    backgroundColor: transparent
    textColor: "{colors.code-string}"
  code-keyword:
    backgroundColor: transparent
    textColor: "{colors.code-keyword}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill in the brand's signature vermilion (#f0523d) against the dark canvas. On hover and active states, the button deepens to `{colors.primary-active}` (#cc2127), and when disabled it shifts to `{colors.primary-disabled}` (#dc5d54) — a lighter, desaturated version that still reads as red but loses contrast. Text is white `{colors.on-primary}` set in `{typography.button-md}` with 0.5px letter-spacing for a slightly premium, deliberate feel.

**`button-secondary`** — A dark-on-dark pill that uses `{colors.surface-card}` (#272727) as its background, creating a subtle layered effect against the `{colors.canvas}` (#131313). On hover, it lifts to `{colors.surface-soft}` (#1d1d1d). Text remains white. This button is used for "View Details" and "Learn More" actions where the primary button is reserved for purchase or add-to-cart.

**`button-tertiary-text`** — A text-only button in `{colors.muted}` (#aaaaaa) with no background or border. Used for secondary actions like "Cancel" or "Clear filters" within forms and filter panels. The typography drops to `{typography.button-sm}` to visually subordinate it.

### Cards
**`product-card`** — The core product display unit, a dark card (`{colors.surface-card}` #272727) with `{rounded.lg}` (20px) corners that echo the rounded bezels of modern smartphones. The product image sits inside the card with its own `{rounded.lg}` treatment, creating a nested-radius effect. Price is rendered in `{colors.price}` (#f6f6f6) — a near-white that stands out against the card background — using `{typography.body-md}`. Sale items receive a `{sale-badge}` in `{colors.sale-badge}` (#f0523d) pinned to the top-left corner of the image.

### Navigation
**`nav-bar`** — A fixed 64px bar in `{colors.canvas}` (#131313) with uppercase nav links in `{typography.nav-link}`. Active links use `{colors.primary}` (#f0523d), inactive links use `{colors.muted}` (#aaaaaa). The bar sits flush with the top of the viewport — no border, no shadow, just the dark canvas extending to the edge.

### Forms
**`text-input`** — A dark input field on `{colors.surface-card}` (#272727) with a 1px `{colors.hairline}` (#e4e4e4) border and `{rounded.sm}` (8px) corners. On focus, the border thickens to 2px and switches to `{colors.primary}` (#f0523d). Placeholder text is `{colors.muted}` (#aaaaaa). The input height is 48px to match button heights for aligned form rows.

### Footer
The footer is a dense grid of links on `{colors.canvas}` (#131313). Column headings use `{typography.caption}` in uppercase with `{colors.on-primary}` (#ffffff). Individual links use `{typography.link}` in `{colors.muted}` (#aaaaaa). Social icons appear in their native brand colors — Facebook blue (#3b5998), Instagram pink (#e4405f), Twitter blue (#0976b4), YouTube red (#cc2127), Pinterest orange (#ff6600), and TikTok black (#111111) — a deliberate break from the monochrome palette that signals platform-native engagement.

### Code Blocks
**`code-block`** — Used for product specifications and technical details, rendered on `{colors.surface-soft}` (#1d1d1d) with `{rounded.sm}` (8px) corners and 16px padding. Inline code highlighting uses a Dracula-inspired palette: keywords in `{colors.code-keyword}` (#f92672), strings in `{colors.code-string}` (#00b4b3), and other tokens in `{colors.code-highlight}` (#ae81ff). This is an unusual choice for a phone-accessories brand and suggests a developer or tech-enthusiast audience.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger menu. Product cards stack in single column. Footer grid collapses to single column. Search bar becomes icon-only. |
| Tablet | 744–1128px | Nav-bar shows limited links (Shop, About, Support). Product cards in 2-column grid. Footer in 2-column grid. |
| Desktop | 1128–1440px | Full nav-bar with all links. Product cards in 3-column grid. Footer in 4-column grid. Search bar full-width. |
| Wide | > 1440px | Max-width container at 1440px, centered. Product cards in 4-column grid. Additional whitespace on sides. |

### Touch Targets
- All interactive elements (buttons, links, icons) maintain minimum 44px height for touch targets.
- Search bar is 48px tall on all breakpoints.
- Social icons are 32px with 44px tap area via padding.
- Nav links have 44px tap area on mobile.

### Collapsing Strategy
- Nav-bar collapses to hamburger menu at < 744px, with a slide-in drawer from the left.
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport narrows.
- Footer grid collapses from 4 columns → 2 → 1.
- Search bar collapses to icon-only at mobile, expanding to full-width on tap.
- Sale badges remain visible at all breakpoints but reduce font size on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow, scale, or overlay) could not be reliably extracted from the live site.
- Error styling for form inputs (validation colors, error messages) is not present in the extracted data.
- Dark mode is not applicable — the brand already uses a dark canvas as its default.
- Sub-brand or collection-specific palettes (e.g., limited-edition colors) are not captured.
- The extracted color list includes many social-icon brand colors and code-highlighting colors that may not be part of the core design system — these are noted in the colors block but may be over-represented.
- Font weights beyond 400, 500, 600, and 700 could not be confirmed — the extracted CSS may not include all weights available in the font files.
- The extracted font list includes many fallbacks (Arial, Geneva, Tahoma) that are likely not the brand's intended typeface — Clarkson and proxima-nova are the most likely primary fonts based on frequency and specificity.
- Transition durations and easing curves are not captured.
- Focus-visible styles for keyboard navigation are not present in the extracted data.
- The `meta theme-color` was not set on the live site, so the browser chrome color is unknown.
