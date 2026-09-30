---
version: alpha
name: "Ovii"
source_url: "https://ovii.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A clinical warmth runs through Ovii — #df5641, a dried-terracotta red, appears as the primary accent on CTAs, ingredient callouts, and cart badges, while the rest of the palette stays almost entirely achromatic: #141414 for deep ink, #f6f6f6 for soft canvas, and #d1d1d1 for hairline borders. The brand lives in the tension between supplement-lab authority and bath-product softness; Inter at 400/500 weight handles all body and button copy at 14–16px, while meno-display (a serif with condensed variant) appears in hero headlines and product titles at 24–32px, lending a editorial, almost journal-like tone. Product cards use {rounded.sm} corners and generous {spacing.base} padding, with the primary red reserved for the "Add to Cart" button and the subscription toggle — a deliberate scarcity that makes the red feel urgent rather than decorative. The site uses a single-column product detail layout with a sticky bottom cart bar on mobile, and the checkout flow inherits Shopify's native button shapes but wraps them in the brand's red and off-white (#fbf7ee) surface. A sage-green (#60a57e) appears in ingredient badges and "vegan" flags, and a muted gold (#dd9a1a) shows up in star ratings and "best seller" tags — a three-accent system that reads as natural and unforced, like a botanist's field notes rather than a beauty brand's mood board.

colors:
  primary: "#df5641"
  primary-active: "#b33323"
  primary-disabled: "#f2c4bb"
  ink: "#141414"
  body: "#171717"
  muted: "#545454"
  muted-soft: "#808284"
  hairline: "#d1d1d1"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#60a57e"
  accent-sage-soft: "#f2faf0"
  accent-gold: "#dd9a1a"
  accent-gold-soft: "#fcf1cd"
  badge-red: "#df5641"
  badge-green: "#108043"
  off-white: "#fbf7ee"
  lavender: "#d9dbed"
  lavender-soft: "#dee2ee"
  star-rating: "#dd9a1a"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'meno-display', 'meno-display-condensed', Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'meno-display', 'meno-display-condensed', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'meno-display', 'meno-display-condensed', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'sofia-pro', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'sofia-pro', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'sofia-pro', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'sofia-pro', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'sofia-pro', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Inter', 'sofia-pro', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', 'sofia-pro', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', 'sofia-pro', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'sofia-pro', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Inter', 'sofia-pro', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
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
    padding: 14px 28px
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
    padding: 13px 27px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge:
    backgroundColor: "{colors.accent-sage-soft}"
    textColor: "{colors.accent-sage}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-best-seller:
    backgroundColor: "{colors.accent-gold-soft}"
    textColor: "{colors.accent-gold}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.lavender-soft}"
    textColor: "{colors.lavender}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  star-rating:
    textColor: "{colors.star-rating}"
    fontSize: 14px
  hero-section:
    backgroundColor: "{colors.off-white}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  cart-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  subscription-toggle-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, filled with {colors.primary} (#df5641) and white text. Used for "Add to Cart", "Subscribe & Save", and checkout entry points. On hover, shifts to {colors.primary-active} (#b33323) for a deeper, more urgent red. Disabled state uses {colors.primary-disabled} (#f2c4bb) to signal inactivity without visual noise. The button has {rounded.sm} corners, 48px height, and 28px horizontal padding for a comfortable tap target.

**`button-secondary`** — An outlined or ghost alternative with white background and {colors.ink} text. Used for "Learn More", "View Details", and secondary product actions. Hover adds a subtle {colors.hairline} border. Same 48px height and {rounded.sm} as primary for visual consistency.

**`button-tertiary-text`** — A text-only button in {colors.primary} with no background or border. Used for inline actions like "Cancel" or "Remove" in cart and form contexts. Hover adds underline.

**`button-pill`** — A fully rounded variant ({rounded.full}) used for promotional badges, "Shop Now" links in hero sections, and sticky mobile cart CTAs. Smaller padding (10px 24px) and smaller typography ({typography.button-sm}) to fit tighter spaces.

### Cards
**`product-card`** — The primary product display unit, a white card with {rounded.sm} corners. Contains a product image (also {rounded.sm}), title in {typography.title-sm}, price in {typography.body-sm} with {colors.body}, and optional badges. Cards are laid out in a 2–4 column grid depending on viewport. No shadow — relies on {colors.hairline} borders and whitespace for separation.

**`product-card-image`** — The product photo area, cropped to a 1:1 or 4:5 aspect ratio with {rounded.sm}. On hover, may include a subtle scale transform (1.02x) for a "pick me up" feel.

### Navigation
**`nav-bar`** — A fixed or sticky top bar at 64px height, white background, containing the logo (left), navigation links (center), and cart icon (right). Links use {typography.nav-link} at 14px/500 weight, with active state in {colors.ink} and default in {colors.muted}. On mobile, the nav collapses into a hamburger menu with a slide-in drawer.

**`nav-link`** — Text-only navigation items with no background. Active state uses {colors.ink} and a subtle underline or bold weight shift. Inactive links are {colors.muted} (#545454).

### Forms
**`text-input`** — Standard text input fields with white background, {colors.body} text, {rounded.sm}, and 48px height. Focus state adds a {colors.primary} border (2px) and removes default outline. Used for email capture, search, and checkout fields.

**`text-input-focus`** — Focus variant with {colors.primary} border and subtle box-shadow (0 0 0 3px rgba(223,86,65,0.1)).

### Badges & Tags
**`badge`** — Small uppercase labels used for ingredient flags ("Vegan", "Gluten-Free") and product attributes. Background in {colors.accent-sage-soft} (#f2faf0), text in {colors.accent-sage} (#60a57e). {rounded.xs} with 4px/8px padding.

**`badge-best-seller`** — Gold variant for "Best Seller" tags. Background {colors.accent-gold-soft} (#fcf1cd), text {colors.accent-gold} (#dd9a1a).

**`badge-new`** — Lavender variant for "New" tags. Background {colors.lavender-soft} (#dee2ee), text {colors.lavender} (#d9dbed).

### Hero
**`hero-section`** — Full-width promotional section with {colors.off-white} (#fbf7ee) background. Contains a headline in {typography.display-xl} (meno-display, 32px), a subtitle in {typography.body-md}, and a {button-pill} CTA. Padding uses {spacing.section} (64px) top/bottom and {spacing.lg} (24px) sides.

**`hero-headline`** — The primary hero text, using meno-display serif at 32px with -0.5px letter-spacing. Color is {colors.ink} (#141414).

**`hero-subtitle`** — Supporting text below the headline, using Inter at 16px/400 with {colors.muted} (#545454). 16px margin-top from headline.

### Footer
**`footer`** — Dark footer with {colors.ink} (#141414) background and white text. Contains link columns, social icons, and legal text. Links use {colors.muted-soft} (#808284) for reduced contrast. Padding is {spacing.xxl} (48px) top/bottom and {spacing.lg} (24px) sides.

**`footer-link`** — Footer navigation links in {colors.muted-soft} (#808284) with {typography.link} (14px/400). Hover shifts to white.

### Cart & Subscription
**`cart-badge`** — A small circular badge (20px) on the cart icon showing item count. Background {colors.badge-red} (#df5641), white text, {rounded.full}. Positioned absolutely at the top-right of the cart icon.

**`subscription-toggle`** — A segmented control for one-time vs. subscription purchase. Default state uses {colors.surface-soft} (#f6f6f6) background with {colors.body} text. Active state uses {colors.primary} (#df5641) with white text. {rounded.sm} with 8px/16px padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; sticky bottom cart bar appears; hero padding reduces to 32px; buttons become full-width; subscription toggle stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains 64px padding; side-by-side subscription toggle; search bar moves to nav |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full width with 64px padding; search bar in nav; product detail page uses two-column layout (image left, details right) |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero may include background imagery; product detail page has wider image area |

### Touch Targets
- All buttons and interactive elements minimum 44px height (48px preferred)
- Cart icon and hamburger menu have 44x44px tap area
- Subscription toggle segments are 48px tall for easy tapping
- Product card links have 44px minimum touch area

### Collapsing Strategy
- Navigation links collapse into hamburger menu below 744px
- Product grid reduces columns from 4 → 3 → 2 → 1 as viewport narrows
- Hero section reduces padding from 64px to 32px on mobile
- Footer link columns stack vertically below 744px
- Search bar moves from nav to a full-width expandable field on mobile
- Sticky bottom cart bar appears only on mobile (< 744px), containing "Add to Cart" button and price

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components could not be reliably extracted from static CSS; the active/disabled variants provided are best estimates based on common patterns
- Error styling (form validation, input error states) not observed on live site
- Dark mode not present on the site; no dark palette tokens available
- Sub-brand or seasonal color palettes (if any) not observed
- Typography line-height and letter-spacing values are estimated based on common Inter and meno-display usage; exact values may vary
- Font weight for meno-display could not be confirmed beyond "400" — the brand may use 300 or 500 for specific headings
- Animation/transition durations and easing curves not extracted
- Focus ring styles (keyboard accessibility) not observed
- Loading states (skeleton screens, spinners) not documented
- Shopify checkout button styling may override brand tokens; the checkout flow's exact appearance is unknown
- The extracted color list included #66ff65 (a bright green) which is likely a Shopify Pay or checkout-widget color, not a brand color — excluded from palette
- The extracted list also included #4c4c4b and #676869 which appear to be system grays from Shopify's UI — not included as brand tokens
