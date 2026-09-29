---
version: alpha
name: "Kammok"
source_url: "https://kammok.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A single red thread — `#e43d30` — runs through every primary action on Kammok’s site, a signal of performance and urgency against a near-black `#121212` ink and a silver-gray `#dedede` that softens the edges of a gear brand built for the backcountry. The palette is deliberately sparse: no sage, no sky blue, no earth tones. Instead, Kammok treats its product photography — hammocks suspended between granite boulders, ultralight quilts glowing under a headlamp — as the only color it needs, letting `{colors.canvas}` white and `{colors.ink}` do the structural work. Buttons land in `{rounded.sm}` with a crisp 8px corner, not the pill shapes of lifestyle brands; the brand trusts that a clean rectangle and that red are enough to say “buy this, it works.” Typography runs a single sans-serif stack at modest weights — display headlines at 500, body at 400 — never competing with the texture of Dyneema or the grain of a tree trunk in the hero image. The nav bar is a thin white strip with a logo left, cart right, and a single “Shop” dropdown that collapses to a hamburger on mobile. Kammok’s design language is the opposite of “camping aesthetic” — it’s a gear brand that happens to sell hammocks, and the site reads like a tool catalog for people who sleep outside on purpose.

colors:
  primary: "#e43d30"
  primary-active: "#c62a1f"
  primary-disabled: "#f5a59e"
  ink: "#121212"
  body: "#2a2a2a"
  muted: "#6b6b6b"
  muted-soft: "#9e9e9e"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale-badge: "#e43d30"
  sold-out-badge: "#121212"
  star-rating: "#121212"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
    padding: 12px 24px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sold-out:
    backgroundColor: "{colors.sold-out-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 36px
  add-to-cart-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 52px

## Components

### Buttons
**`button-primary`** — The brand’s single call-to-action engine. Uses `#e43d30` fill with white uppercase text at 14px/600. On hover, darkens to `#c62a1f` (`{colors.primary-active}`). Disabled state drops to a washed `#f5a59e` (`{colors.primary-disabled}`). All buttons share `{rounded.sm}` (8px) — no pills, no outlines, no ghost variants for primary actions.

**`button-secondary`** — White fill with `{colors.ink}` text and a `{colors.hairline}` 1px border. Used for “View Details” on product cards and secondary checkout paths. Same height and padding as primary.

**`button-tertiary-text`** — Text-only link styled as a button. No background, no border. Used for “Learn More” in editorial sections and “Size Guide” links on product pages.

### Text Inputs
**`text-input`** — Standard form field with white background, `{colors.hairline}` border, and `{rounded.sm}`. Focus state uses a `{colors.ink}` border (2px). Used for email signup, search, and checkout forms. Placeholder text in `{colors.muted}`.

### Navigation
**`nav-bar`** — Fixed 64px white bar with logo left, hamburger (mobile) or dropdown menu (desktop) center, and cart icon right. Cart badge uses `{colors.primary}` fill with white count. No search bar in nav — search is a separate icon that expands on click.

### Product Cards
**`product-card`** — White card with `{rounded.sm}`, a 1:1 product image, title in `{typography.title-md}`, price in `{typography.body-md}`, and a color swatch row (if applicable). Hover state shows a subtle shadow (0 2px 8px rgba(0,0,0,0.08)). No add-to-cart on card — click goes to PDP.

**`badge-sale`** — Small `#e43d30` pill with white uppercase “SALE” text. Positioned top-left on product images. `{rounded.xs}` (4px) for a crisp, no-nonsense look.

**`badge-sold-out`** — Same shape as sale badge but `#121212` fill with white “SOLD OUT” text.

### Hero Section
**`hero-section`** — Full-width section with a large background image (product shot or lifestyle), overlaid with `{typography.display-xl}` headline and a `{button-primary}` CTA. Background color falls back to `{colors.surface-soft}`. Padding uses `{spacing.section}` top/bottom and `{spacing.lg}` sides.

### Search
**`search-bar`** — Pill-shaped input with `{colors.surface-soft}` background and `{rounded.full}`. Used in the mobile menu and on the search results page. Not present in the top nav by default — toggled via a magnifying glass icon.

### Footer
**`footer-link`** — Simple text link in `{colors.muted}`. No underline by default; underline on hover. Used in the 4-column footer for “About Us,” “Support,” “Community,” and “Legal” sections.

### Quantity Selector
**`quantity-selector`** — A compact row with minus/plus buttons and a center number. Background `{colors.surface-soft}`, `{rounded.sm}`, 36px height. Used on PDP and cart.

### Add to Cart Bar
**`add-to-cart-bar`** — Full-width sticky bar at the bottom of the PDP on mobile. Contains the primary CTA button. Same styling as `button-primary` but with extra padding (14px 24px) and 52px height for easier tapping.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; add-to-cart bar becomes sticky at bottom; hero section reduces padding to 32px top/bottom; search bar appears in expanded mobile menu |
| Tablet | 744–1128px | Two-column product grid; nav shows limited links (Shop, About, Support); hero uses 48px top/bottom padding; search icon visible in nav |
| Desktop | 1128–1440px | Full nav with dropdown menus; three-column product grid; hero uses 64px padding; search icon in nav; footer shows all 4 columns |
| Wide | > 1440px | Max-width container at 1440px; content centered; hero image scales up but text remains centered; product grid can show 4 columns if space allows |

### Touch Targets
- All buttons and interactive elements minimum 44px height (WCAG compliant)
- Mobile nav hamburger icon: 48x48px tap target
- Quantity selector buttons: 44x36px
- Product card tap target: entire card surface
- Cart icon: 44x44px

### Collapsing Strategy
- Nav links collapse to hamburger menu below 744px
- Footer columns collapse to single-column accordion below 744px
- Product grid collapses from 3 columns (desktop) to 2 (tablet) to 1 (mobile)
- Hero section collapses from full-width image with text overlay to stacked layout (image above text) below 744px
- Secondary navigation (breadcrumbs, filter bars) hides on mobile, replaced by a “Filter” button that opens a drawer

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extractable from the live site; the typography stack shown is a best-guess based on common Shopify sans-serif defaults (Helvetica Neue / Arial). The actual brand font may differ.
- Only three hex colors were extracted from the live site: `#e43d30`, `#dedede`, and `#121212`. All other color tokens (muted-soft, surface-soft, primary-disabled, etc.) are inferred from these three values and standard design-system patterns. They may not match the live site exactly.
- Hover states for text inputs, links, and secondary buttons were not extractable; the active/disabled states shown are reasonable approximations.
- No dark mode data was found; the system assumes light mode only.
- Error styling (form validation, out-of-stock messaging, payment errors) could not be extracted.
- Sub-brand or collection-specific palettes (e.g., “Roo” vs “Kickstarter” vs “Glider”) may exist but were not detected.
- The Shopify checkout widget colors (Afterpay, Klarna, etc.) were filtered out but may influence perceived brand palette on cart/payment pages.
- No animation or transition timing data was extractable.
