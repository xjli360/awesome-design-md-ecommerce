---
version: alpha
name: "Honest Jon's"
source_url: "https://www.honestjons.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record shop that feels like a crate-digging session in a friend’s basement, Honest Jon’s uses a saturated blue (#009be3) as its primary voltage — the same electric hue that lights up the “Latest 100 arrivals” page title and every add-to-cart button, against a warm off-white canvas (#e5e3df) that reads more like aged paper than sterile digital white. The palette is deliberately chaotic: a lime-green accent (#a0a600) sits next to a hot pink (#cc0090), a deep navy (#002869) anchors the footer, and a fire-engine red (#be0000) marks sale prices and stock warnings, creating a visual language that mirrors the unpredictable joy of finding a rare pressing in a stack of records. Typography runs Myriad Pro Regular for display headers — a condensed, slightly retro sans-serif that nods to 90s CD booklet design — paired with system fonts (-apple-system, Arial, Helvetica Neue) for body copy, keeping the reading experience clean while the headers do the heavy lifting of character. Buttons are sharp-cornered rectangles ({rounded.none}) with 1px hairline borders (#d7d7d7), a deliberate anti-modern choice that gives the interface a utilitarian, no-nonsense feel — this is a shop for collectors who want speed and information density, not a lifestyle brand selling vibes. The nav bar runs a tight 48px height with a sticky top bar that collapses on scroll, and product cards use a compact 8px radius ({rounded.sm}) with a subtle shadow, prioritizing shelf-like density over breathing room. The overall mood is that of a well-organized record bin: functional, slightly worn, and absolutely alive with color signals that reward attention.

colors:
  primary: "#009be3"
  primary-active: "#0082c4"
  primary-disabled: "#b3ddf5"
  ink: "#1e1e1e"
  body: "#444444"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#d7d7d7"
  hairline-soft: "#e5e3df"
  canvas: "#f4f4f4"
  surface-soft: "#e5e3df"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-lime: "#a0a600"
  accent-pink: "#cc0090"
  accent-navy: "#002869"
  accent-red: "#be0000"
  sale-red: "#be0000"
  stock-warning: "#be0000"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"
  social-pinterest: "#bd081d"

typography:
  display-xl:
    fontFamily: "'Myriad Pro Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Myriad Pro Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Myriad Pro Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Myriad Pro Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Myriad Pro Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Myriad Pro Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Myriad Pro Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, Arial, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
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
    rounded: "{rounded.none}"
    padding: 10px 20px
    height: 36px
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
    padding: 9px 19px
    height: 36px
    border: 1px solid "{colors.hairline}"
  button-accent-lime:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 10px 20px
    height: 36px
  button-accent-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 36px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
    border-bottom: 1px solid "{colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 0 16px
    height: 48px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    border-bottom: 2px solid "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    box-shadow: 0 1px 3px rgba(0,0,0,0.08)
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: 1/1
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.sm} 0"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    padding: "{spacing.xs} {spacing.sm} {spacing.sm}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    color: "{colors.sale-red}"
    padding: "{spacing.xs} {spacing.sm} {spacing.sm}"
  badge-new:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  badge-out-of-stock:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 36px
    border: 1px solid "{colors.hairline}"
  footer:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    color: "{colors.surface-card}"
    typography: "{typography.link}"
  social-icon:
    width: 24px
    height: 24px
    rounded: "{rounded.none}"
  stock-indicator:
    typography: "{typography.caption}"
    color: "{colors.stock-warning}"
    padding: "{spacing.xs} 0"

## Components

### Buttons
**`button-primary`** — A sharp-cornered rectangle in electric blue (#009be3) with white text, used for primary actions like "Add to Cart" and "Checkout". On hover, it shifts to `primary-active` (#0082c4). Disabled state uses a pale blue fill (`primary-disabled`) with white text. Height is a compact 36px, reflecting the site's information-dense layout.

**`button-secondary`** — An outlined variant with a white fill, ink text, and a 1px hairline border (#d7d7d7). Used for secondary actions like "View Details" or "Continue Shopping". Hover adds a subtle shadow. Same 36px height as primary for alignment in forms.

**`button-accent-lime`** and **`button-accent-pink`** — Accent buttons using the brand's lime green (#a0a600) and hot pink (#cc0090), reserved for promotional actions, newsletter signups, or category filters. These inject the brand's eclectic energy into the interface without competing with the primary blue.

### Cards
**`product-card`** — A white card with an 8px radius ({rounded.sm}) and a subtle box-shadow (0 1px 3px rgba(0,0,0,0.08)). The image area uses a 1:1 aspect ratio with top-rounded corners. Title uses `title-sm` (16px Myriad Pro), price uses `body-md` (15px system font). Sale prices render in `sale-red` (#be0000). Cards are designed for dense grid layouts — no excessive padding, just enough breathing room for the eye.

**`badge-new`** — A lime-green (#a0a600) label with uppercase 10px bold text, pinned to the top-left of product images for new arrivals. Sharp corners match the button system.

**`badge-sale`** — Red (#be0000) badge for discounted items, same typography and corner treatment as `badge-new`.

**`badge-out-of-stock`** — Gray (#888888) badge for unavailable items, signaling unavailability without visual aggression.

### Navigation
**`nav-bar`** — A 48px sticky top bar with white background and a 1px bottom hairline. Navigation links are uppercase Myriad Pro at 13px with 0.5px letter spacing. The active link gets a 2px bottom border in `primary` blue. On scroll, the bar collapses to a thinner variant (36px) to maximize content space.

**`nav-link`** — Inline navigation items with 16px horizontal padding. Hover state adds a subtle underline. Active state uses the primary blue border treatment.

### Forms
**`text-input`** — A 36px tall input with a 1px hairline border, white fill, and 8px/12px padding. Focus state swaps the border to `primary` blue (#009be3). No border-radius — consistent with the brand's utilitarian aesthetic.

**`search-bar`** — Identical to `text-input` in structure but used in the header for record/artist searches. No rounded corners, no search icon by default — just a clean text field with placeholder text.

### Footer
**`footer`** — A deep navy (#002869) band at the bottom of every page. Links render in white with `body-sm` typography. Social media icons (Facebook, Twitter, Pinterest) use their respective brand colors from the palette. The footer includes a newsletter signup form using the standard `text-input` and `button-accent-lime` components.

### Stock Indicators
**`stock-indicator`** — A caption-sized text element in red (#be0000) that appears below product prices when stock is low or sold out. Uses the same red as sale badges, creating a consistent urgency signal across the interface.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; search bar moves below nav; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible but truncated; search bar remains in header |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; search bar in header with category dropdown |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; additional whitespace on sides |

### Touch Targets
- All buttons and links maintain a minimum 44px touch target height on mobile
- Product card tap targets are the full card area
- Nav hamburger icon is 48x48px on mobile
- Search bar input height remains 36px but padding increases to 12px for better touch accuracy

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Product grid columns reduce from 4 to 1 on mobile
- Footer links collapse into accordion sections on mobile
- Category filter strip collapses to a dropdown select on mobile
- Search bar moves from inline to full-width below the nav on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.
- Hover states for buttons and links were inferred from common patterns; actual hover colors may differ
- Error state styling for form inputs (border color, error message typography) could not be extracted
- Dark mode is not present on the live site; no dark palette tokens exist
- Sub-brand or collection-specific color variations (e.g., for different genres or labels) were not observed
- The extracted hex list includes social media brand colors (#3b5998, #1da1f2, #bd081d) and several near-duplicate grays — the true brand palette likely uses fewer distinct values
- Font sizes and line heights are estimated from common record-store ecommerce patterns; actual values may vary
- No animation or transition durations were extractable from static analysis
- The site may use a different primary color for UK vs. international markets; only the UK site was analyzed
- Checkout flow styling (Shopify Pay buttons, payment method icons) was not analyzed
