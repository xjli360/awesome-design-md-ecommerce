---
version: alpha
name: "Cangshan"
source_url: "https://cangshancutlery.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand forged in the tension between raw craftsmanship and refined minimalism, Cangshan Cutlery speaks to the cook who respects the blade as much as the meal. The palette is anchored by a deep, almost arterial red — `#e32525` and its close variants `#e32e25` and `#e31e25` — that appears on primary actions, badges, and select accents, evoking the heat of a forge and the precision of a honed edge. This red is set against a cool, architectural foundation of near-blacks (`#1c1c1c`, `#0d0d0d`, `#1a1a1a`) and slate grays (`#676986`, `#646464`, `#6c757d`), with a crisp white canvas (`#fafafa`, `#f7f7f8`, `#f4f4f6`) that lets product photography breathe. The typographic voice is a deliberate hybrid: classic serifs like `Big Caslon`, `Bodoni MT`, `Cardo`, and `Georgia` lend editorial gravitas and a sense of heritage, while `Jost`, `Myriad`, and `Oswald` introduce clean, modern geometry for navigation and technical specs. This mix of old-world serif and contemporary sans-serif mirrors the brand's own story — traditional Japanese steel techniques housed in modern, minimalist handles. The signature design move is the use of `{rounded.xl}` (32px) on hero cards and `{rounded.full}` on search and filter inputs, creating soft, approachable entry points into an otherwise sharp, precise world. Product cards use `{rounded.md}` (12px) with subtle `{colors.hairline}` borders, while the primary button is a bold, pill-shaped (`{rounded.full}`) block of `{colors.primary}` that demands interaction. The overall mood is one of controlled intensity: the red never overwhelms, the serifs never feel fussy, and the generous whitespace (section padding at `{spacing.section}` 64px) gives each knife the gallery-like presentation it deserves.

colors:
  primary: "#e32525"
  primary-active: "#9f1919"
  primary-disabled: "#806363"
  ink: "#1c1c1c"
  body: "#333333"
  muted: "#646464"
  muted-soft: "#aaaaaa"
  hairline: "#e5e5e5"
  hairline-soft: "#f2f2f2"
  canvas: "#fafafa"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-deep: "#272d45"
  accent-slate: "#676986"
  badge-red: "#ad2328"
  badge-new: "#b2f9e9"
  star-rating: "#2c3e50"
  scrim: "#0d0d0d"

typography:
  display-xl:
    fontFamily: "'Big Caslon', 'Bodoni MT', Cardo, Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Big Caslon', 'Bodoni MT', Cardo, Georgia, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Big Caslon', 'Bodoni MT', Cardo, Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Jost', 'Myriad', Oswald, 'Almarai', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "'Jost', 'Myriad', Oswald, 'Almarai', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  title-sm:
    fontFamily: "'Jost', 'Myriad', Oswald, 'Almarai', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Jost', 'Myriad', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Jost', 'Myriad', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', 'Myriad', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'Jost', 'Myriad', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Jost', 'Myriad', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Jost', 'Myriad', Oswald, 'Almarai', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', 'Myriad', Oswald, 'Almarai', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.75px
    textTransform: uppercase
  link:
    fontFamily: "'Jost', 'Myriad', Georgia, serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Jost', 'Myriad', Oswald, 'Almarai', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  text-input-error:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  hero-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    rounded: "{rounded.xl}"
    padding: "{spacing.section}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
    boxShadow: "0 0 0 4px rgba(227,37,37,0.15)"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-material:
    backgroundColor: "{colors.accent-slate}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  accordion-trigger:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 0 {spacing.base} 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered as a bold, pill-shaped button in the signature Cangshan red (`{colors.primary}`). The uppercase, letter-spaced typography (`{typography.button-md}`) and full rounding (`{rounded.full}`) create a confident, premium feel. On hover/active, the button deepens to `{colors.primary-active}` (`#9f1919`), and in its disabled state it fades to a muted rose `{colors.primary-disabled}` (`#806363`). **`button-secondary`** — An outlined or ghost variant on a white canvas (`{colors.canvas}`) with dark ink text (`{colors.ink}`). Maintains the same pill shape and uppercase typography, but uses a subtle border (1px `{colors.hairline}`) that can be toggled. On active, the background shifts to `{colors.hairline-soft}` (`#f2f2f2`). **`button-tertiary-text`** — A minimal text-only button in `{colors.primary}`, used for secondary actions like "View Details" or "Clear Filters." No background, no border — just the brand red with the same uppercase, letter-spaced styling.

### Cards
**`hero-card`** — A large, editorial card used for hero banners and featured collections. It uses a soft surface background (`{colors.surface-soft}`) with generous padding (`{spacing.section}`) and a pronounced 32px rounding (`{rounded.xl}`). The typography is the brand's serif display (`{typography.display-lg}`), lending a magazine-like gravitas. **`product-card`** — The standard product listing card, a clean white (`{colors.surface-card}`) container with 12px rounding (`{rounded.md}`). The product image sits flush to the top corners (rounded top-only via `{rounded.md} {rounded.md} 0 0`), while the title uses the uppercase sans-serif `{typography.title-sm}` and the price uses `{typography.body-md}`. Cards are typically arranged in a responsive grid with `{spacing.lg}` (24px) gaps.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height, using a white canvas (`{colors.canvas}`) and the brand's uppercase, letter-spaced nav-link typography (`{typography.nav-link}`). On scroll, a subtle box-shadow (`0 2px 8px rgba(0,0,0,0.08)`) is added for depth. The nav typically contains the logo (often a serif wordmark), category links, and a search icon.

### Forms
**`text-input`** — Standard text inputs use a white background (`{colors.canvas}`), `{typography.body-md}`, and 8px rounding (`{rounded.sm}`). On focus, a 2px `{colors.primary}` border is applied. Error states also use a 2px `{colors.primary}` border, signaling the brand's red as the sole error color. **`search-bar`** — The site search input is a pill-shaped (`{rounded.full}`) field, 48px tall, with a white background. On focus, it receives a 2px `{colors.primary}` border and a soft red glow (`0 0 0 4px rgba(227,37,37,0.15)`).

### Badges
**`badge-new`** — A small, mint-green (`{colors.badge-new}`) badge used to denote new arrivals. Uses `{typography.badge}` (10px, uppercase, bold) with 4px rounding (`{rounded.xs}`). **`badge-sale`** — A red (`{colors.primary}`) badge for sale or clearance items, same typography and rounding. **`badge-material`** — A pill-shaped badge in slate (`{colors.accent-slate}`) used to indicate knife material (e.g., "DAMASCUS", "GERMAN STEEL"). Uses `{typography.caption-sm}` (11px, uppercase, medium weight) with full rounding (`{rounded.full}`).

### Footer
**`footer-section`** — A full-width footer with a deep ink background (`{colors.ink}`) and muted-soft text (`{colors.muted-soft}`). Headings use `{typography.title-sm}` in white (`{colors.canvas}`), and links use `{typography.link}` with underline. The section has `{spacing.section}` (64px) vertical padding.

### Accordion
**`accordion-trigger`** — Used for product details, FAQs, and filter panels. The trigger is a full-width, white-background bar with `{typography.title-md}` in ink. Content panels use `{typography.body-md}` with `{spacing.base}` bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero card padding reduces to 24px; search bar becomes full-width; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav shows limited links; hero card uses 40px padding; search bar remains pill but narrower |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero card at full `{spacing.section}` padding; search bar at standard width |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centers content; hero card may feature larger typography |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Icon buttons and quantity selectors are at least 40px × 40px.
- Nav links have a minimum 48px tap area, even if the text is smaller.
- Search bar and text inputs are 48px tall for comfortable tapping.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu, with the logo centered and the cart/search icons remaining visible.
- Product filters collapse into a slide-out drawer or an accordion panel.
- The multi-column footer collapses into a single column with accordion-style sections.
- Hero cards may reduce to a single image with overlaid text rather than side-by-side content.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus-visible states for secondary buttons and text links were not fully extracted; assumed to use `{colors.hairline-soft}` background or underline toggle.
- Error styling for forms beyond the 2px red border is missing (e.g., error message typography, icon placement).
- Sub-brand or collection-specific palettes (e.g., "Cangshan Forged", "Cangshan German Steel") may exist but were not detected.
- Dark mode is not supported; all tokens assume a light theme.
- Animation and transition durations (e.g., button hover, card lift, nav scroll) were not extracted; a default 200ms ease-in-out is recommended.
- The exact font weights for serif faces (Big Caslon, Bodoni MT, Cardo) are inferred; actual weights may vary by browser availability.
- Star rating color (`{colors.star-rating}`) is assumed from a detected hex; actual implementation may use SVG or icon font.
- The `oke-widget-icons` font family is used for product reviews but its specific glyphs and styling are not documented here.
