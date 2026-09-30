---
version: alpha
name: "White Noise Records"
source_url: "https://www.whitenoiserecords.org"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record store that wears its orange — #fb6500 — like a neon tube sign flickering in a concrete basement, the single color that electrifies every CTA, price badge, and sale tag against a near-black canvas of #121212 and #222222. The brand lives in the gap between noise and signal: Barlow in modest weights (400–600) runs body copy at 14–16px, while display heads sit at 24–28px in weight 500, never shouting. Buttons are sharp-cornered rectangles (`{rounded.xs}` ~4px) with that orange fill, a deliberate resistance to the pill-shaped friendliness of marketplace design — this is a store for people who dig through crates, not swipe through feeds. Product cards use `{rounded.md}` (12px) on a #cac9c9 hairline, with stock-status badges in #008a00 (available) and #fb6500 (pre-order), and a secondary accent of #ffbd00 for sale pricing. The nav bar is a dark slab (#222222) with white text, the search bar a white pill (`{rounded.full}`) on that dark ground — the one soft shape in an otherwise angular system. Social icons pull in their platform colors (#3b5998 Facebook, #1da1f2 Twitter, #bd081c Pinterest, #d83776 Instagram), but they sit in a footer that's pure #121212, a deliberate dimming after the orange blast of the hero.

colors:
  primary: "#fb6500"
  primary-active: "#ae4600"
  primary-disabled: "#cac9c9"
  ink: "#121212"
  body: "#222222"
  muted: "#696969"
  muted-soft: "#8a9297"
  hairline: "#cac9c9"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  stock-available: "#008a00"
  stock-preorder: "#fb6500"
  sale-accent: "#ffbd00"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"
  social-pinterest: "#bd081c"
  social-instagram: "#d83776"
  social-youtube: "#fd355a"
  social-tumblr: "#35465c"
  social-whatsapp: "#1ab7ea"
  social-linkedin: "#0077b5"
  social-snapchat: "#f5dc30"
  social-klarna: "#ffb3c7"
  social-afterpay: "#b2fce4"
  social-paypal: "#0070ba"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Barlow', monospace, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  display-lg:
    fontFamily: "'Barlow', monospace, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Barlow', monospace, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Barlow', monospace, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Barlow', monospace, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Barlow', monospace, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', monospace, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Barlow', monospace, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Barlow', monospace, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Barlow', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "'Barlow', monospace, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Barlow', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Barlow', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0

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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
  button-pill-search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
  top-nav:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 8px
  product-card-image:
    rounded: "{rounded.md}"
    objectFit: cover
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    fontWeight: 600
  product-card-sale-price:
    typography: "{typography.body-md}"
    color: "{colors.sale-accent}"
    fontWeight: 600
  badge-stock:
    backgroundColor: "{colors.stock-available}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-preorder:
    backgroundColor: "{colors.stock-preorder}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.sale-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  social-icon:
    rounded: "{rounded.full}"
    height: 32px
  social-icon-facebook:
    backgroundColor: "{colors.social-facebook}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-twitter:
    backgroundColor: "{colors.social-twitter}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-pinterest:
    backgroundColor: "{colors.social-pinterest}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-instagram:
    backgroundColor: "{colors.social-instagram}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-youtube:
    backgroundColor: "{colors.social-youtube}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-tumblr:
    backgroundColor: "{colors.social-tumblr}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-whatsapp:
    backgroundColor: "{colors.social-whatsapp}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-linkedin:
    backgroundColor: "{colors.social-linkedin}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-snapchat:
    backgroundColor: "{colors.social-snapchat}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-klarna:
    backgroundColor: "{colors.social-klarna}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-afterpay:
    backgroundColor: "{colors.social-afterpay}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-paypal:
    backgroundColor: "{colors.social-paypal}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.base}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.on-dark}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"
  section-heading:
    typography: "{typography.display-lg}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with `{colors.primary}` (#fb6500) and white text on a sharp `{rounded.xs}` (4px) rectangle. Hover shifts to `{colors.primary-active}` (#ae4600), a darker burnt orange. Disabled state drops to `{colors.primary-disabled}` (#cac9c9) with `{colors.muted}` text, signaling non-interactivity without ambiguity. Padding is 10px 20px at 40px height, compact enough for inline use in product cards and cart summaries.

**`button-secondary`** — An outlined variant on a white `{colors.canvas}` background with `{colors.ink}` text, using the same `{rounded.xs}` and 40px height. Active state fills `{colors.hairline-soft}` (#dedede) for a subtle press effect. Used for "View Details" and "Add to Wishlist" actions where the orange primary would compete.

**`button-ghost`** — Fully transparent background with `{colors.ink}` text, no border, minimal padding (10px 16px). Reserved for tertiary actions like "Cancel" or "Clear Filters" in sidebar panels.

**`button-pill-search`** — The one pill-shaped button in the system, white `{colors.canvas}` fill with `{rounded.full}` and `{colors.muted}` text. 36px height, 8px 16px padding. Used exclusively for the search bar on the dark nav bar — the soft shape contrasts with the angular primary buttons, signaling a different mode (discovery vs. action).

### Navigation
**`top-nav`** — A dark slab at 64px height, `{colors.body}` (#222222) background with white `{colors.on-dark}` text. The nav uses `{typography.nav-link}` (Barlow 14px weight 600) for links. Active links switch to `{colors.primary}` (#fb6500), creating a glowing trail against the dark ground. The search bar sits as a white pill (`{rounded.full}`) within this dark bar, the only soft element in an otherwise hard-edged navigation.

**`nav-link-active`** / **`nav-link-inactive`** — Active links inherit the orange brand voltage; inactive links stay white. No underline or border — the color shift alone signals state.

### Cards
**`product-card`** — A white card on `{colors.canvas}` with `{rounded.md}` (12px) corners and 8px padding. The card image uses `object-fit: cover` with `{rounded.md}` to match the container. Title uses `{typography.title-sm}` (Barlow 16px weight 600), price uses `{typography.body-md}` at weight 600. Sale prices switch to `{colors.sale-accent}` (#ffbd00), a warm yellow that sits between the orange primary and the dark ink.

**`badge-stock`** / **`badge-preorder`** / **`badge-sale`** — Small rectangular badges at `{rounded.xs}` (4px) with `{typography.badge}` (Barlow 11px weight 600). Stock-available uses `{colors.stock-available}` (#008a00) green; pre-order uses `{colors.stock-preorder}` (#fb6500) orange; sale uses `{colors.sale-accent}` (#ffbd00) yellow with `{colors.ink}` text. Padding is 2px 6px — tight, informational, never decorative.

### Forms
**`search-bar`** — A white pill (`{rounded.full}`) on the dark nav, 40px height with 8px 16px padding. Uses `{typography.body-sm}` (Barlow 14px weight 400) for input text. The pill shape is the only rounded-full element in the system, reserved for search alone.

### Footer
**`footer`** — A deep `{colors.ink}` (#121212) slab with white text, using `{typography.body-sm}`. Social icons are 32px circles (`{rounded.full}`) filled with their respective platform colors — Facebook blue, Twitter blue, Pinterest red, Instagram pink, YouTube red, Tumblr navy, WhatsApp green, LinkedIn blue, Snapchat yellow, plus checkout badges for Klarna, Afterpay, and PayPal. The footer is the brand's color explosion, a deliberate contrast to the restrained dark-and-orange system above.

### Hero
**`hero-section`** — A full-width `{colors.ink}` (#121212) background with white text, using `{spacing.section}` (64px) vertical padding. The hero title uses `{typography.display-xl}` (Barlow 28px weight 500), the subtitle uses `{typography.body-md}` in `{colors.muted-soft}` (#8a9297). No hero image — the brand trusts typography and color to set the mood.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero padding reduces to 32px; search bar moves below nav; footer social icons wrap to 2 rows |
| Tablet | 744–1128px | Nav shows 4–5 links; product cards in 2-column grid; hero padding at 48px; search bar remains in nav |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3–4 column grid; hero at full 64px padding; search bar prominent in nav |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4–5 column grid; hero content centered with max-width 1200px |

### Touch Targets
- All buttons and links maintain minimum 44px touch height on mobile
- Social icons at 32px circles — borderline for touch; consider 40px on mobile
- Search bar at 40px height meets minimum touch target
- Nav hamburger icon at 44x44px hit area

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px; menu slides in from left
- Product card grid collapses from 4 columns to 2 columns at tablet, 1 column at mobile
- Footer social icons collapse from single row to 2-row wrap below 744px
- Hero section reduces vertical padding from 64px to 32px on mobile
- Search bar moves from inline in nav to full-width below nav on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the live site; only `button-primary` and `button-secondary` have confirmed active states. All other hover/focus styling should be assumed from platform conventions (Shopify default) until verified.
- Error styling for form inputs (validation borders, error messages) was not visible in the extracted data. The brand likely uses Shopify's default error patterns (#e74c3c red borders, red text) but this is unconfirmed.
- Dark mode is not present on the live site; the brand uses a dark nav and footer but the main canvas is white. No dark mode tokens are defined.
- Sub-brand or collection-specific palettes (e.g., genre-specific color coding for vinyl sections) could not be extracted. The system currently uses a single orange primary across all contexts.
- Typography scale beyond display-xl (28px) was not found; the brand may use larger sizes for landing pages or seasonal campaigns that weren't in the extracted CSS.
- The extracted font-family list included "monospace" as a fallback, but no monospace usage was confirmed in body or display text. This may be a CSS artifact or a secondary font for metadata (catalog numbers, barcodes).
- Social icon colors were extracted from the live site's icon set; the brand may use monochrome icons on hover or in different contexts that weren't captured.
- Checkout-widget colors (Klarna pink, Afterpay green, PayPal blue) were extracted but are likely from embedded payment iframes, not brand-controlled elements. They are included in the color palette for completeness but should not be used in brand UI outside of checkout contexts.
