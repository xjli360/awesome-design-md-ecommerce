---
version: alpha
name: "Anker"
source_url: "https://www.anker.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand that lives in the gap between industrial reliability and consumer warmth, Anker’s palette is anchored by a deep near-black ink (#080a0f) and a signature cyan (#00befa) that reads as engineered energy — the kind of blue you’d see on a high-end power meter or a charging indicator LED. The canvas is a cool off-white (#f5f5f7), not a sterile #ffffff, which softens the technical product photography of charging docks, cables, and power banks. Secondary accents of green (#00db84) and orange (#ff9900) appear sparingly — the green on “GaN” badges and fast-charge indicators, the orange on limited-edition or promotional elements. Typography runs system-native (-apple-system, Helvetica Neue) at moderate weights (400–600), never competing with the product itself; the brand trusts its industrial design and spec sheets to do the selling. Corners are gently rounded ({rounded.sm} on buttons, {rounded.md} on product cards), avoiding the harshness of a pure rectangle while staying far from the pill-shaped friendliness of consumer lifestyle brands. The nav bar sits at 64px, compact and utilitarian, with a sticky search bar that collapses on mobile. Anker’s design voice says: this equipment will outlast your expectations, and it looks good enough to leave on your desk.

colors:
  primary: "#00befa"
  primary-active: "#10b5ec"
  primary-disabled: "#6d8a9a"
  ink: "#080a0f"
  body: "#1d1d1f"
  muted: "#75787f"
  muted-soft: "#9ca3af"
  hairline: "#e2e2e2"
  hairline-soft: "#f1f3f5"
  canvas: "#f5f5f7"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-green: "#00db84"
  accent-orange: "#ff9900"
  badge-blue: "#2c7ed0"
  error-red: "#da3c3c"
  star-rating: "#ff9900"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
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
    height: 44px
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
    height: 44px
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 1px {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(8, 10, 15, 0.08)"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1/1"
  badge-tech:
    backgroundColor: "{colors.badge-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 1px {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for “Add to Cart”, “Shop Now”, and “Learn More” on product pages and hero sections. Filled with `{colors.primary}` (#00befa) and white text, with `{rounded.sm}` corners. On hover, shifts to `{colors.primary-active}` (#10b5ec). Disabled state uses `{colors.primary-disabled}` (#6d8a9a) to indicate unavailability.

**`button-secondary`** — An outlined or ghost variant used for secondary actions like “View Details” or “Compare”. White background with `{colors.ink}` text and a 1px `{colors.hairline}` border. Hover adds a subtle shadow.

**`button-tertiary`** — A text-only button with `{colors.primary}` text, used for links within content blocks or “Read More” prompts. No background or border; hover underlines.

**`button-accent-green`** — A smaller, compact button used for “Fast Charging” or “GaN” badges and promotional CTAs. Filled with `{colors.accent-green}` (#00db84) and white text, `{rounded.sm}` corners, 36px height.

### Cards
**`product-card`** — The primary product display component on collection and search pages. White background (`{colors.surface-card}`), `{rounded.md}` corners, 16px padding. Contains a square product image (`{rounded.md}`), title (`{typography.title-sm}`), price (`{typography.body-md}`), and rating stars (`{colors.star-rating}`). On hover, a subtle box-shadow lifts the card.

**`product-card-image`** — The image container within a product card. Maintains a 1:1 aspect ratio and `{rounded.md}` corners. Images are object-fit: cover.

### Navigation
**`nav-bar`** — The sticky top navigation bar, 64px tall, white background (`{colors.canvas}`). Contains the Anker logo, nav links (`{typography.nav-link}`), and a search icon. On scroll, a 1px bottom border (`{colors.hairline}`) appears.

**`nav-link-active`** — The active navigation link state. Uses `{colors.ink}` text and a 2px bottom border in `{colors.primary}`.

**`nav-link-inactive`** — Inactive navigation links use `{colors.muted}` (#75787f) text. On hover, they transition to `{colors.ink}`.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, and contact forms. White background, `{colors.body}` text, `{rounded.sm}` corners, 44px height. On focus, a 1px `{colors.primary}` border and matching box-shadow appear.

**`search-bar`** — The search input field, typically placed in the nav or on search pages. Uses `{colors.surface-soft}` (#f2f2f2) background for a subtle inset look. On focus, switches to white background with `{colors.primary}` outline.

### Badges
**`badge-tech`** — Used for technical specifications like “GaN”, “PowerIQ”, or “100W”. Blue background (`{colors.badge-blue}`), white text, uppercase `{typography.badge}`, `{rounded.xs}` corners.

**`badge-green`** — Used for “Fast Charge” or “Eco” indicators. Green background (`{colors.accent-green}`), white text.

### Footer
**`footer`** — The site footer, full-width with `{colors.ink}` (#080a0f) background and white text. Contains link columns, social icons, and legal text. Links use `{colors.muted-soft}` (#9ca3af) for readability on dark.

### Hero
**`hero-section`** — The primary hero banner on the homepage and campaign pages. White background, large display typography (`{typography.display-xl}`), and a prominent `{colors.primary}` CTA button (`{hero-cta}`). Padding uses `{spacing.section}` (64px) top and bottom.

### Dividers
**`divider`** — A standard 1px horizontal rule in `{colors.hairline}` (#e2e2e2), used between sections and product rows.

**`divider-soft`** — A lighter 1px rule in `{colors.hairline-soft}` (#f1f3f5), used within cards or accordion panels.

### Accordion
**`accordion-header`** — The clickable header of an accordion panel, used on FAQ and product specification sections. White background, `{typography.title-sm}`, `{rounded.sm}` corners. On expand, the bottom corners become square.

**`accordion-content`** — The expandable content area below an accordion header. White background, `{typography.body-md}`, 16px padding.

### Tooltip
**`tooltip`** — A small, dark tooltip used for feature explanations or spec highlights. `{colors.ink}` background, white text, `{rounded.xs}` corners, 4px horizontal and 8px vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in single column; hero padding reduces to 32px; search bar moves to full-width below nav; footer links stack vertically; accordion becomes default for product specs. |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards display in 2-column grid; hero maintains 48px padding; search bar remains in nav. |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero at 64px padding; search bar in nav with dropdown. |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero content centered with max-width 1200px. |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility.
- Nav links have 48px tap targets on mobile.
- Accordion headers have 48px tap targets.
- Product card CTAs are at least 44px tall.

### Collapsing Strategy
- On mobile (< 744px), the nav bar collapses to a hamburger icon with a slide-out drawer.
- Product filters collapse into a sticky bottom sheet on mobile.
- Product description sections collapse into accordion panels on mobile and tablet.
- Footer link columns collapse into a single vertical stack on mobile.
- Hero images switch from landscape to portrait crop on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors include many framework defaults and checkout-widget colors (Shopify Pay pink #f81ce5, Afterpay blue #0070f3, Klarna pink #ff0080). The brand’s true primary (#00befa) was identified as the most distinctive and frequently used accent, but hover states and disabled variants are inferred.
- No custom font family was found beyond system fonts. Anker may use a custom typeface (e.g., Anker Sans) that is loaded via JavaScript or a CDN not captured in the extraction. The system-native stack is used as a fallback.
- Dark mode styling is not present in the extracted data. The brand may not support it, or it may be loaded conditionally.
- Error states for forms (validation colors, error messages) are not reliably extracted. The red #da3c3c is used as a general error color.
- Star rating color (#ff9900) is inferred from the extracted orange hex and common e-commerce patterns.
- Badge colors (#2c7ed0, #00db84) are inferred from extracted hexes that appear in technical badge contexts.
- No data on loading states (spinners, skeletons) or animation timing/easing curves.
- Sub-brand or campaign-specific palettes (e.g., Soundcore, Nebula) are not captured.
- The extracted font list includes JudgemeStar (a review widget font) and monospace fonts (Consolas, Courier New) that are not part of the brand’s primary typography system.
