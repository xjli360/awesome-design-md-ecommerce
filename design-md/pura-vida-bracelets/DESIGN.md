---
version: alpha
name: "Pura Vida Bracelets"
source_url: "https://www.puravidabracelets.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Thread around thread around thread — the entire catalog is organized as a color delivery system, the stacked-wrist shot being the explicit outcome the product photography architects toward. The canvas arrives as a bleached neutral stack: near-white surfaces (#f9fafb, #f9f9f9) layered with warm cream (#f3efdc) for editorial and gifting moments, all chromatic weight carried by a coral tuned precisely between ripe fruit and afternoon sun (#ff7f55) and a deep reef teal (#108474) that reads as the brand's moral register — appearing on charitable partnership callouts, announcement bars, and cause-marketing badges rather than hard-sell CTAs. Supporting color notes include an amber-yellow (#fbcd0a) that surfaces on NEW and flash-sale badges, and a soft lavender (#a89cc8) that arrives with seasonal capsule collections. The near-black ink (#241f20) avoids pure black, warming headlines and body copy by a few degrees.

  Nunito Sans carries all functional UI copy — a humanist sans with rounded letterforms that signals approachability without sliding into infantilism. Baskerville appears in sparse editorial moments to add gravity to cause-marketing and gifting copy, suggesting that a $14 bracelet can still be a meaningful object. The engraving font collection — Engraving Brand, Engraving Chasing Waves, Engraving Old London, Engraving Courier, Engraving Lucida — exists entirely inside the personalization tool, where customers preview their name or message in five script registers before committing to a purchase.

  Corners arrive soft throughout: `{rounded.sm}` for buttons and inputs, `{rounded.md}` for product cards, `{rounded.full}` for color swatches and filter pills. The system never approaches a hard corner except at the footer's background edge. Spacing is generous, with product grid cards sitting in airy columns and hero sections drawing deep breath at `{spacing.section}` vertical padding.

  The Pura Vida Club membership — a monthly bracelet subscription — receives dedicated warm-cream surface treatment (`{colors.surface-warm}`), distinguishing recurring-value propositions from transactional product display. Cause-partnership callouts are consistently teal (#108474), reserving coral's warmer energy for commerce-driving actions.

colors:
  primary: "#ff7f55"
  primary-active: "#e5623a"
  primary-disabled: "#ffc4ae"
  secondary: "#108474"
  secondary-light: "#c1e6e6"
  secondary-soft: "#d3f4ef"
  accent-yellow: "#fbcd0a"
  accent-lavender: "#a89cc8"
  accent-mint: "#c5f7f0"
  ink: "#241f20"
  body: "#555555"
  muted: "#7b7b7b"
  muted-light: "#888888"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#f9f9f9"
  surface-warm: "#f3efdc"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-editorial:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.6px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  price:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 17px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
    textDecoration: line-through
  engraving-preview:
    fontFamily: "'Engraving Brand', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 1.5px
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px

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
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoMaxHeight: 40px
  announcement-bar:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.caption}"
    height: 40px
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    imageRounded: "{rounded.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    comparePriceTypography: "{typography.price-compare}"
    padding: "{spacing.base}"
    swatchGap: "{spacing.xs}"
  swatch-color:
    size: 22px
    borderRadius: "{rounded.full}"
    selectedBorder: "2px solid {colors.ink}"
    unselectedBorder: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingY: "{spacing.section}"
    paddingX: "{spacing.xl}"
    ctaStyle: "button-primary"
    layout: image-right-text-left
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  badge-cause:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  badge-new:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  club-membership-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    accentColor: "{colors.primary}"
    borderLeft: "4px solid {colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  engraving-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    previewTypography: "{typography.engraving-preview}"
    previewBackgroundColor: "{colors.surface-warm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    fontSwatchGap: "{spacing.sm}"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.title-md}"
    itemTypography: "{typography.body-sm}"
    subtotalTypography: "{typography.title-sm}"
    borderLeft: "1px solid {colors.hairline}"
    width: 420px
    ctaStyle: "button-primary"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.caption}"
    accentColor: "{colors.primary}"
    linkHoverColor: "{colors.primary}"
    padding: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — Full-bleed coral (#ff7f55) with white uppercase Nunito Sans at 700 weight, 8px radius, 48px height. The dominant purchase-trigger CTA for add-to-cart, checkout, and club join flows. Active state deepens to #e5623a; disabled washes to a petal coral (#ffc4ae) at the same geometry.

**`button-secondary`** — Same dimensions as primary but uses deep reef teal (#108474) with white text. Reserved for cause-partnership CTAs, "Shop the Cause" links, and secondary conversion actions where coral would create visual competition. The consistent use of teal here reinforces system-level color meaning across badges and the announcement bar.

**`button-outline`** — Transparent fill with a 2px ink border, uppercase Nunito Sans, 48px height matching filled button geometry. Used for ghost actions — View All, Load More, and low-priority navigation links — where a filled button would oversaturate a section with competing color.

**`button-text`** — Bare text in coral (#ff7f55), no border or background. Used for inline micro-actions: Remove from cart, Edit personalization, and review read-more triggers, where adding button chrome would inflate visual weight.

### Inputs

**`text-input`** — White fill, 1px `{colors.hairline}` border at rest, upgrading to a 2px coral border on focus. Nunito Sans 16px/400, 48px height, 8px radius matches button geometry throughout the system. Used for email capture, search, and engraving text entry; the engraving field also pipes live input into the `engraving-selector` preview panel.

### Navigation

**`nav-bar`** — White canvas, 64px height, `{colors.hairline-soft}` bottom border. Nunito Sans 14px/700 for mega-menu category links. Logo anchors left, category links span center, cart, search, and account icons sit right. Collapses to a hamburger drawer at mobile breakpoints with the full category tree inside a full-screen overlay.

**`announcement-bar`** — Stacked above nav at 40px, teal fill (#108474) with white uppercase caption text. Rotates between free shipping threshold messaging, cause promotions, and club sign-up pitches. The teal ensures the brand's charitable register is the very first color the eye encounters.

### Product Cards

**`product-card`** — Soft-gray surface (#f9f9f9), 12px card radius, 8px image radius. Title in Nunito Sans 15px/700; sale price at 17px/700 with a line-through compare price in 14px/400 beside it. Up to eight color swatches (22px circles at `{rounded.full}`, ink border on selected state) appear below the title and truncate with a "+N" overflow chip when variants exceed display capacity. Card lifts 2px with a soft shadow on hover.

**`swatch-color`** — 22px diameter circles at `{rounded.full}`, 36px touch target. Selected state uses a 2px ink outline set 2px away from the swatch fill using a CSS outline offset technique so the swatch color reads fully. Unselected uses a 1px `{colors.hairline}` border. The same swatch token scales to 32px on product detail pages.

### Badges

**`badge-sale`** — Coral pill at `{rounded.xs}`, white uppercase 11px caption, positioned top-left over product imagery. Uses the primary color to match CTA energy and signal purchase urgency without introducing an isolated warning color into the system.

**`badge-cause`** — Teal pill at `{rounded.xs}`, white uppercase caption. Marks products tied to charity and artisan partnerships. The teal deliberately echoes the announcement bar and secondary button, building system-level meaning for the color as the brand's moral signal.

**`badge-new`** — Amber-yellow (#fbcd0a) pill with ink text, same padding and radius. Used for new arrivals and collection launches; the yellow reads apart from both coral and teal without triggering urgency or warning associations.

### Club Membership

**`club-membership-banner`** — Warm cream surface (#f3efdc), 12px radius, 4px coral left border accent. Heading at Nunito Sans 18px/700, body at 14px/400, with an embedded `button-primary` CTA. The cream surface deliberately separates subscription-value propositions from the cooler transactional grays surrounding product listings, marking it as a different category of offer.

### Personalization

**`engraving-selector`** — Light-gray surface (#f9fafb) container holding a text input, a row of labeled font-style swatch tiles, and a live preview panel rendered on warm cream (#f3efdc). The preview tile renders the customer's entered text in the currently selected engraving family — Engraving Brand, Chasing Waves, Old London, Courier, or Lucida — updating in real time. Active font swatch gets a 2px ink border; all others remain at 1px hairline.

### Filtering

**`filter-pill`** / **`filter-pill-active`** — `{rounded.full}` pills for color, collection, price range, and material filtering. Inactive is white with a hairline border; active inverts to ink fill with white text. No checkmark or icon — the full inversion is the only active signal. Pill rows scroll horizontally without wrapping at mobile widths.

### Cart Drawer

**`cart-drawer`** — 420px right-panel, white background, 1px `{colors.hairline}` left edge. Header in 18px/700, line items in 14px/400, subtotal in 15px/700. Cause-donation upsell modules and personalization summary appear inline between items and the full-width coral checkout CTA.

### Footer

**`footer`** — Near-black (#241f20) background, white link text in 14px/400, section heads in white uppercase 11px caption. Coral (#ff7f55) applied as link hover color, preserving primary brand presence in a dark context. Four-column layout at desktop: Shop, Club, Charity, Connect. Social icon row sits above the legal strip; icons carry their extracted platform colors (#e60023 Pinterest, #3b5998 Facebook) on a dark surface.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav; filter pills scroll horizontally without wrap; hero text stacks above image; cart drawer goes full-width; engraving selector becomes a full-height modal sheet |
| Tablet | 744–1128px | Two-column product grid; top-level nav categories collapse to a horizontal scrollable tab row; club membership banner goes single-column |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu with multi-column category layout; hero splits 50/50 image-right / text-left |
| Wide | > 1440px | Four-column product grid; hero and content sections max at 1440px container centered with expanding side margins |

### Touch Targets

- All buttons: minimum 48px height × 44px width
- Color swatches: 22px visual diameter, 36px tap target via padding
- Filter pills: 36px height with horizontal padding for comfortable tapping
- Nav hamburger and icon buttons: 44×44px minimum tap target
- Announcement bar close button (if present): 44px minimum

### Collapsing Strategy

- Mega-menu collapses to a full-screen slide-in drawer at tablet and below, with accordion sub-categories
- Announcement bar persists across all breakpoints; font-size may drop from 11px to 10px on small mobile
- Footer four-column grid collapses to single-column accordion on mobile, each section independently expandable
- Swatch row on product cards limits to six visible at mobile widths, showing a "+N more" chip; desktop shows up to ten
- Engraving selector becomes a full-screen bottom-sheet modal at mobile widths to give the font preview panel adequate vertical space

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed button corner radius from live CSS — `{rounded.sm}` (8px) inferred from Shopify theme conventions and the brand's consistently soft-corner aesthetic
- Canvas white (#ffffff) not directly extracted; inferred from the cluster of near-whites (#f9fafb, #f9f9f9, #fafafa) present in extraction
- Exact nav height, logo lockup dimensions, and mega-menu column count not confirmed without JavaScript rendering
- Engraving font size scale and weight values are estimates; live rendering may differ across the five font variants
- Hover transition durations and easing curves not extractable; Shopify default values (200–300ms ease) assumed throughout
- Club membership tier count, pricing, and whether badge assets differ per tier not captured in extraction
- Role of accent lavender (#a89cc8) — permanent palette member vs seasonal capsule only — not confirmed
- Accent mint (#c5f7f0) and secondary-soft (#d3f4ef) usage contexts not confirmed; likely informational or background tints rather than interactive states
