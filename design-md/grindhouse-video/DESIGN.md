---
version: alpha
name: "Grindhouse Video"
source_url: "https://grindhousevideo.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A video store that wears its blood-red heart on its sleeve — #f70f0f is the meta-theme color and the brand's primary voltage, a stop-sign red that bleeds into every primary CTA, badge, and category label. The canvas is near-black (#0a0909), not white, making the experience feel like walking into a dimly lit theater lobby where only the neon exit signs and poster frames glow. Type runs DM Sans at clean weights — body copy at 14–16px in weight 400, titles at 18–22px in weight 700 — with generous tracking that keeps readability high against the dark backdrop. Category pills use {rounded.full} and sit in a horizontal strip, each one a saturated accent: horror in #ff0000, cult in #1e2d7d, exploitation in #008a00, anime in #00badb. The search bar is a dark pill with white text and a red icon, floating above a grid of product cards that use {rounded.sm} corners and white (#f3f5f6) backgrounds to pop against the dark page. The footer collapses into a dense stack of links in #677279, with social icons in their brand colors (#3b5998, #1da1f2, #bd081c) — a rare moment of external color bleeding into the system. The overall effect is a digital grindhouse: loud, proud, unapologetically genre-specific, with a red that doesn't whisper.

colors:
  primary: "#f70f0f"
  primary-active: "#cc0000"
  primary-disabled: "#8a3333"
  ink: "#0a0909"
  body: "#f3f5f6"
  muted: "#677279"
  muted-soft: "#8a9297"
  hairline: "#212121"
  hairline-soft: "#4a4a4a"
  canvas: "#0a0909"
  surface-soft: "#121212"
  surface-card: "#f3f5f6"
  on-primary: "#ffffff"
  on-dark: "#f3f5f6"
  category-horror: "#ff0000"
  category-cult: "#1e2d7d"
  category-exploitation: "#008a00"
  category-anime: "#00badb"
  category-comedy: "#ffbd00"
  category-action: "#ee0000"
  badge-sale: "#00aa00"
  badge-new: "#1e2d7d"
  badge-oos: "#a9a9a9"
  star-rating: "#ffbd00"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"
  social-pinterest: "#bd081c"
  social-instagram: "#d83776"
  social-tiktok: "#fd355a"
  social-youtube: "#ff0000"
  social-linkedin: "#0077b5"
  social-snapchat: "#f5dc30"
  checkout-paypal: "#35465c"
  checkout-shopify: "#a3afef"
  checkout-klarna: "#ffbd00"
  checkout-afterpay: "#00badb"

typography:
  display-xl:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.36
    letterSpacing: 0
  title-lg:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.44
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0.25px
  badge:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  link:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
    textTransform: uppercase

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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-pill-category:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  button-pill-category-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-pill-category-horror:
    backgroundColor: "{colors.category-horror}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-pill-category-cult:
    backgroundColor: "{colors.category-cult}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-pill-category-exploitation:
    backgroundColor: "{colors.category-exploitation}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-pill-category-anime:
    backgroundColor: "{colors.category-anime}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-pill-category-comedy:
    backgroundColor: "{colors.category-comedy}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-pill-category-action:
    backgroundColor: "{colors.category-action}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  text-input-error:
    border: 2px solid "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    border: 2px solid "{colors.primary}"
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline}"
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  top-nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid "{colors.primary}"
  logo:
    height: 32px
    padding: 0 16px
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    padding: 12px 16px
    gap: 8px
    overflowX: auto
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: 2/3
    objectFit: cover
  product-card-title:
    typography: "{typography.title-sm}"
    padding: 8px 12px 0
  product-card-price:
    typography: "{typography.body-sm}"
    padding: 4px 12px 8px
  product-card-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
    position: absolute
    top: 8px
    left: 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
  badge-oos:
    backgroundColor: "{colors.badge-oos}"
    textColor: "{colors.ink}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: 32px 16px
    borderTop: 1px solid "{colors.hairline}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
    padding: 4px 0
  footer-link-hover:
    textColor: "{colors.body}"
  footer-heading:
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    marginBottom: 12px
  social-icon:
    height: 24px
    width: 24px
    rounded: "{rounded.full}"
  social-icon-facebook:
    backgroundColor: "{colors.social-facebook}"
  social-icon-twitter:
    backgroundColor: "{colors.social-twitter}"
  social-icon-pinterest:
    backgroundColor: "{colors.social-pinterest}"
  social-icon-instagram:
    backgroundColor: "{colors.social-instagram}"
  social-icon-tiktok:
    backgroundColor: "{colors.social-tiktok}"
  social-icon-youtube:
    backgroundColor: "{colors.social-youtube}"
  social-icon-linkedin:
    backgroundColor: "{colors.social-linkedin}"
  social-icon-snapchat:
    backgroundColor: "{colors.social-snapchat}"
  newsletter-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
    border: 1px solid "{colors.hairline}"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  cart-icon:
    textColor: "{colors.body}"
    height: 24px
  cart-count:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
    padding: 0 4px
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  checkout-button-active:
    backgroundColor: "{colors.primary-active}"
  checkout-button-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a solid red rectangle with white text. Used for "Add to Cart", "Checkout", and "Subscribe" actions. On hover, darkens to #cc0000 (`{colors.primary-active}`). When disabled, fades to a muted red with gray text (`{colors.muted}`). The `{rounded.sm}` corners keep it feeling modern but not playful.

**`button-secondary`** — An inverted button with a white background and dark text, used for "View Details" and "Continue Shopping" actions. The border is implied by the white card background it sits on. Active state uses `{colors.hairline}` as a subtle press effect.

**`button-tertiary`** — A text-only button in `{colors.primary}` with no background, used for "Cancel" or "Clear Filters" actions. Minimal footprint, relies on the red to signal interactivity.

**`button-pill-category`** — A dark pill button (`{rounded.full}`) with white text, used in the horizontal category strip. Each category gets its own color variant: horror (#ff0000), cult (#1e2d7d), exploitation (#008a00), anime (#00badb), comedy (#ffbd00), action (#ee0000). The active state switches to the primary red.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with `{rounded.sm}` corners, containing a 2:3 aspect ratio image and text below. The image uses `object-fit: cover` to fill the top half cleanly. The title runs `{typography.title-sm}` and the price uses `{typography.body-sm}`. Badges are absolutely positioned over the top-left of the image.

**`product-card-badge`** — A small uppercase label (`{typography.badge}`) with `{rounded.xs}` corners. Three variants exist: `badge-sale` (green #00aa00), `badge-new` (blue #1e2d7d), and `badge-oos` (gray #a9a9a9). Positioned 8px from the top and left of the card image.

### Navigation
**`top-nav`** — A 64px dark bar (`{colors.ink}`) with a 1px bottom border in `{colors.hairline}`. Contains the logo (32px height) and nav links in uppercase `{typography.nav-link}`. Active links get a 2px bottom border in `{colors.primary}`.

**`category-strip`** — A horizontal scrollable strip on `{colors.surface-soft}` background, containing pill buttons for each genre. 12px padding top/bottom, 16px left/right, with 8px gaps between pills. Scrolls horizontally on mobile.

### Forms
**`text-input`** — A dark input field (`{colors.surface-soft}`) with a 1px `{colors.hairline}` border and `{rounded.sm}` corners. On focus, the border thickens to 2px and turns `{colors.primary}`. Error state also uses a 2px red border.

**`search-bar`** — A full-width pill (`{rounded.full}`) with the same dark background and hairline border. On focus, the border becomes 2px red. The search icon sits inside the left padding in `{colors.primary}`.

**`newsletter-input`** — A 40px tall input in the footer, paired with a `newsletter-button` that uses `{colors.primary}`. The button is 40px tall with `{rounded.sm}` corners.

### Footer
**`footer`** — A dark section (`{colors.ink}`) with 32px padding and a top border in `{colors.hairline}`. Links are `{colors.muted}` and turn white on hover. Headings use `{typography.title-sm}` in white. Social icons are 24px circles in their respective brand colors, placed in a row.

### Badges & Indicators
**`cart-count`** — A small red circle (`{rounded.full}`) with white text, positioned over the cart icon. Uses `{typography.caption-sm}` and has a minimum width of 18px to accommodate double digits.

**`star-rating`** — Yellow stars (`{colors.star-rating}`) at 14px, used on product cards to show customer ratings.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 columns), category strip scrolls horizontally, top nav collapses to hamburger menu, footer stacks vertically, search bar reduces to icon-only |
| Tablet | 744–1128px | Two-column product grid (3 columns), top nav shows all links, category strip is fully visible, footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid (4 columns), top nav with full links, category strip centered, footer uses 4-column layout |
| Wide | > 1440px | Four-column product grid (5 columns), max-width container at 1440px, content centered |

### Touch Targets
- All buttons and links have a minimum height of 44px for touch accessibility
- Category pills are 36px tall with 8px padding — slightly below the 44px ideal but acceptable for horizontal scrolling strips
- Social icons are 24px circles with adequate spacing (16px gap) for touch
- Cart icon and count badge are 24px and 18px respectively, positioned with sufficient padding

### Collapsing Strategy
- Top nav links collapse into a hamburger menu below 744px
- Category strip becomes horizontally scrollable with overflow-x: auto below 744px
- Product grid reduces from 4 columns to 2 columns on mobile
- Footer sections stack vertically on mobile, using 2 columns on tablet, and 4 columns on desktop
- Search bar collapses to an icon-only trigger on mobile, expanding to full width on tap
- Newsletter form stacks input and button vertically on mobile, side-by-side on tablet and above

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components were not fully extractable from the live site; only primary button and text-input focus states were observed
- Error styling for forms (validation messages, error icons) was not visible in the extracted data
- Dark mode is not applicable — the site already uses a dark canvas as its default
- Sub-brand or seasonal color palettes (e.g., Halloween, Black Friday) were not observed
- The exact font weight for DM Sans in different contexts could not be confirmed; weights 400, 600, and 700 are assumed based on common usage
- The `monospace` fallback in font-family declarations may indicate a secondary monospace font for code or metadata, but no specific usage was observed
- Checkout widget colors (PayPal, Shopify Pay, Klarna, Afterpay) are included but may not be part of the brand's design system — they are platform defaults
- Social icon colors are from the extracted list and match known brand colors, but their exact usage (hover states, sizes) could not be verified
- The star-rating component's exact implementation (half-stars, clickability) was not observed
- Product card hover states (shadow, scale, border) were not extractable
- The newsletter form's success and error states were not visible
- Mobile navigation's hamburger menu animation and overlay behavior were not observed
- The site's loading states and skeleton screens were not part of the extracted data
