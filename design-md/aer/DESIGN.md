---
version: alpha
name: "Aer"
source_url: "https://www.aersf.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dark, disciplined travel-gear brand that builds its entire visual system around a black canvas (`#000000` meta theme-color) and a single red accent (`#d20000`) used with surgical restraint — not as a logo color but as a low-voltage indicator for stock warnings, sale badges, and the rare destructive action. The palette is overwhelmingly achromatic: `#404040`, `#575757`, `#707070`, `#959595`, and `#d9d9d9` form a precise gray scale that lets product photography — backpacks against urban concrete, travel organizers in flat-lay — carry all the warmth. Surfaces are flat and matte; there are no gradients, no shadows, no glossy reflections. Typography runs Helvetica Now Display at moderate weights (`400`–`700`) with tight tracking (`0px`–`0.5px`) and generous line heights (`1.4`–`1.6`), producing a clean, technical readout that mirrors the brand's engineering-forward product copy. Buttons are sharp-cornered rectangles (`{rounded.none}`) or subtle pills (`{rounded.sm}`) — never the friendly `{rounded.full}` of consumer lifestyle brands. The nav bar is fixed, black (`#212121`), and dense: a left-aligned logo, a center search field with a `#1199ff` accent orb, and right-aligned utility icons. Product cards use `{rounded.sm}` with a white (`#fafafa`) surface and `#eaeaea` hairline border, mimicking the clean edges of a tech accessory. The footer collapses into a single column of `#959595` links on a `#f2f2f2` canvas. Every design decision reads as intentional reduction — the brand trusts its product to speak, not its interface.

colors:
  primary: "#d20000"
  primary-active: "#950f0f"
  primary-disabled: "#651818"
  ink: "#212121"
  body: "#404040"
  muted: "#707070"
  muted-soft: "#959595"
  hairline: "#d9d9d9"
  hairline-soft: "#eaeaea"
  canvas: "#fafafa"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-strong: "#f2f2f2"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  search-accent: "#1199ff"
  sale-badge: "#d20000"
  stock-warning: "#d20000"
  success: "#1f873d"
  social-facebook: "#3b5998"
  social-twitter: "#00aced"
  social-pinterest: "#cb2027"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0px
  display-sm:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0px
  title-md:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0px
  title-sm:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0px
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0px
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  nav-link:
    fontFamily: "'Helvetica Now Display', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.25px

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
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  search-orb:
    backgroundColor: "{colors.search-accent}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-circle:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  stock-warning-badge:
    backgroundColor: "{colors.stock-warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  footer:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
    height: 24px

## Components

### Buttons
**`button-primary`** — A sharp-cornered, uppercase red (`#d20000`) rectangle used for primary actions like "Add to Cart" and "Checkout." On hover, it deepens to `#950f0f`; disabled state fades to `#651818`. The `{typography.button-md}` type is set in Helvetica Now Display at 14px/600 with 0.5px letter spacing, all caps. No pill rounding, no gradient — the brand's engineering ethos demands a clean, decisive edge.

**`button-secondary`** — An outlined variant on a white (`#fafafa`) canvas with `{colors.ink}` text and a 1px `{colors.hairline}` border. Used for "View Details" and secondary cart actions. Hover adds a subtle `{colors.hairline-soft}` background fill.

**`button-tertiary-text`** — A text-only link styled as a button, used for "Learn More" and "Read Reviews." No background, no border, `{colors.ink}` text with underline on hover.

**`button-pill-accent`** — A rare pill-shaped button (`{rounded.sm}`) reserved for sale callouts and limited-time offers. Uses `{typography.button-sm}` (12px/600 uppercase) with tight padding (8px 16px). The only button with any rounding — a deliberate departure from the system's hard edges.

### Navigation
**`top-nav`** — A fixed black (`#212121`) bar at 64px height. Left: logo in white. Center: a search field with a `#1199ff` orb (40px circle, `{rounded.full}`). Right: utility icons (cart, account, menu) in `{colors.muted-soft}`. Links are `{typography.nav-link}` (14px/500) with 0.25px tracking. Active state is white; inactive is `#959595`.

**`nav-link-active`** — White text on transparent background. No underline, no highlight — the active state is communicated purely through color contrast against the dark nav.

**`nav-link-inactive`** — `#959595` text on transparent background. Hover transitions to white.

### Cards
**`product-card`** — A white (`#ffffff`) card with `{rounded.sm}` (4px) corners and a `{colors.hairline-soft}` border. No shadow, no elevation — the card sits flat on the `#fafafa` canvas. Image occupies the top with `{rounded.sm} {rounded.sm} 0 0`. Title uses `{typography.title-sm}` (16px/500) with `{spacing.base}` padding. Price uses `{typography.body-md}` (16px/400) below.

**`sale-badge`** — A sharp-cornered red (`#d20000`) rectangle with white uppercase text (`{typography.badge}`: 11px/700, 0.5px tracking). Positioned absolutely over the product image top-left. No rounding, no glow — just a flat, urgent signal.

**`stock-warning-badge`** — Identical to sale-badge but used for "Low Stock" or "Almost Gone" indicators. Same red (`#d20000`), same typography, same flat rectangle.

### Forms
**`search-bar`** — A white (`#fafafa`) input field with `{rounded.sm}` (4px) corners and `{colors.hairline}` border. Height 40px, padding 8px 16px. Placeholder text in `{colors.muted}` (14px/400). Focus state adds a `{colors.search-accent}` (`#1199ff`) border — the only blue in the system, used exclusively for search.

### Footer
**`footer`** — A `#f2f2f2` section with `{spacing.section}` (64px) top/bottom padding and `{spacing.lg}` (24px) side padding. Links in `#959595` (`{typography.link}`: 14px/400). Column headings in `{colors.ink}` (`{typography.title-sm}`: 16px/500). Social icons are 24px circles with `{rounded.full}` and `{colors.muted-soft}` fill.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-up). Footer collapses to stacked links. Nav reduces to hamburger menu. Search bar moves to a collapsible drawer. |
| Tablet | 744–1128px | Two-column product grid. Footer shows 2–3 columns. Nav retains full links but compresses spacing. |
| Desktop | 1128–1440px | Three-column product grid. Footer shows 4 columns. Full nav with search orb visible. |
| Wide | > 1440px | Four-column product grid. Max-width container (1440px) with centered content. Footer remains 4 columns. |

### Touch Targets
- All interactive elements (buttons, links, icons) meet minimum 44x44px tap target.
- Nav icons (cart, account, menu) are 40px circles with 48px touch area.
- Search orb is 40px with 48px touch area.
- Product card images are tappable with no minimum size — entire card is a link.

### Collapsing Strategy
- On mobile (<744px), the top nav collapses to a hamburger menu with a slide-out drawer.
- The search bar collapses to an icon that expands into a full-width input overlay.
- The footer collapses from 4 columns to a single vertical stack.
- Product grid collapses from 3 columns to 1 column.
- Category filters (if present) collapse to a dropdown select.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex list is heavily weighted toward grays (`#d9d9d9`, `#959595`, `#404040`, `#707070`, `#f2f2f2`, etc.) and includes several likely non-brand colors (`#3b5998` Facebook blue, `#00aced` Twitter blue, `#cb2027` Pinterest red, `#1f873d`/`#198754` success greens, `#1b9500`/`#d3efcd` Shopify greens). The true brand primary (`#d20000`) was identified as the most distinctive accent in the list.
- Hover states for buttons and links are inferred from common patterns — exact transition durations and background fills are not extracted.
- Error styling (form validation, error messages, empty states) is not present in extracted data.
- Dark mode is not supported — the brand uses a black nav and white canvas consistently.
- Typography weights and sizes are inferred from extracted font-family declarations (`Helvetica Now Display`, `Helvetica Neue`) and common brand patterns — exact `fontWeight` and `fontSize` values for each token are not extracted.
- `letterSpacing` and `textTransform` values are based on brand convention (uppercase buttons, tight tracking) rather than extracted CSS.
- Product card padding and image rounding are inferred from common e-commerce patterns — exact values are not extracted.
- Footer column count and layout are inferred from common patterns — exact breakpoints are not extracted.
- The `#1199ff` search accent is present in extracted colors but its exact usage (search orb, focus state) is inferred from context.
- Social icon colors (`#3b5998`, `#00aced`, `#cb2027`) are extracted but their usage (footer, product sharing) is inferred.
