---
version: alpha
name: "Blueair"
source_url: "https://www.blueair.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep navy and teal share a polarity that structures every screen: #002955 anchors the nav bar, footer, and brand identity while #0e7a82 — a muted, almost clinical teal — fires on every primary CTA and add-to-cart button. Neither color fights the white-canvas product photography that a purifier brand depends on; the system is built around restraint at the color layer so the imagery can carry the promise of clean, open air. Gilroy handles all display and UI text, its geometric letterforms held at 400–600 weight rather than the heavy 700+ a lifestyle brand might reach for; the decision reads as Swedish engineering precision, where legibility and measured confidence matter more than typographic drama. Product pages carry dense specification grids — CADR ratings, filter lifespans, room coverage in square feet — and the type scale accommodates this with small-but-clear caption scales and an uppercase spec-label style in `{typography.spec-label}` that organizes technical data into scannable rows without visual noise. The lavender-gray neutral range (#676986, #9a9db1, #d3d4dd) forms a continuous tonal progression from body text through borders to near-white background surfaces (#f4f4f6, #f7f7f8), generating depth through value shift rather than heavy shadow. Cards hold `{rounded.sm}` corner radii — legible as modern without the pill-softness of a wellness brand, matching the purifier hardware's clean rectilinear forms. Filter chips for room type and performance tier travel horizontally on mobile using the same navy-to-teal contrast logic as the primary button: selected state fills #002955, idle state rests on #e5e5eb. Promotional banners run full navy with reversed type, reserving the teal only for the inline action link — a habit that keeps the palette's signal-to-noise ratio high across long catalog pages. The footer returns to deep navy, bookending the light canvas in the same gesture as the nav, and the Shopify review widget imports `oke-widget-icons` as a separate icon font sitting quietly alongside Gilroy.

colors:
  primary: "#002955"
  primary-active: "#00244b"
  primary-disabled: "#9a9db1"
  cta: "#0e7a82"
  cta-active: "#0a616a"
  cta-disabled: "#d3d4dd"
  ink: "#272d45"
  body: "#676986"
  muted: "#9a9db1"
  muted-soft: "#99a9bb"
  hairline: "#d3d4dd"
  hairline-soft: "#e5e5eb"
  canvas: "#ffffff"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  surface-subtle: "#f7f7f8"
  on-primary: "#ffffff"
  on-cta: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Gilroy', Roboto, -apple-system, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Gilroy', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Gilroy', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Gilroy', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gilroy', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "'Gilroy', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gilroy', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Gilroy', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  spec-label:
    fontFamily: "'Gilroy', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.36
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'Gilroy', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Gilroy', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Gilroy', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Gilroy', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Gilroy', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
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
    backgroundColor: "{colors.cta}"
    textColor: "{colors.on-cta}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.cta-active}"
    textColor: "{colors.on-cta}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.cta-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-navy:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.primary}"
  button-secondary-teal:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.cta}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.cta}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-subtle}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    height: 44px
    padding: 0 16px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: none
  nav-bar-scrolled:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: "0 2px 12px rgba(0,41,85,0.18)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    hoverBoxShadow: "0 4px 16px rgba(0,41,85,0.10)"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.on-primary}"
    minHeight: 580px
    primaryCtaBackground: "{colors.cta}"
    primaryCtaText: "{colors.on-cta}"
    secondaryCtaBorder: "1.5px solid {colors.on-primary}"
    secondaryCtaText: "{colors.on-primary}"
    paddingX: "{spacing.xl}"
    paddingY: "{spacing.xxl}"
  feature-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
    border: "1px solid {colors.hairline-soft}"
  award-badge:
    backgroundColor: "{colors.cta}"
    textColor: "{colors.on-cta}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
    height: 36px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: none
    padding: 8px 16px
    height: 36px
  spec-row:
    backgroundColor: "{colors.canvas}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline-soft}"
    paddingY: 12px
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.cta}"
    height: 40px
    paddingX: "{spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  comparison-table:
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.title-sm}"
    rowBackgroundAlt: "{colors.surface-subtle}"
    rowBackgroundBase: "{colors.canvas}"
    cellTypography: "{typography.body-sm}"
    cellColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
  subscription-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.cta}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.cta}"
    padding: 3px 8px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.hairline}"
    mutedColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    paddingY: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Teal (#0e7a82) fill with white type; Blueair's single CTA driver for add-to-cart, find-your-purifier flows, and modal confirmations. Hover/active deepens to `{colors.cta-active}` (#0a616a); disabled state falls to `{colors.cta-disabled}` fill with `{colors.muted}` label, preserving the action area's legibility without drawing attention. Geometry holds at `{rounded.sm}` with 48px height and generous 28px horizontal padding.

**`button-navy`** — Deep navy (#002955) fill for primary actions that live within dark or teal hero panels where the teal CTA would lose contrast against the background. Same height, radius, and `{typography.button-md}` as button-primary; uses `{colors.on-primary}` white type. Appears sparingly so the teal remains the dominant action color.

**`button-secondary`** — White canvas with a 1.5px navy border and navy label; pairs with button-primary to surface a "learn more" or "compare" alternate action. A `button-secondary-teal` variant swaps border and label to `{colors.cta}` for contexts where navy borders would read as primary weight.

**`button-ghost`** — Transparent, no border; navy text in `{typography.button-md}`. Reserved for inline text CTAs like "See all filters" or "Read full specs" within body copy and spec table footers.

### Inputs

**`text-input`** — Canvas fill, `{colors.hairline}` border at rest, snapping to a solid `{colors.primary}` navy on focus to surface the brand color at the interaction layer. Placeholder in `{colors.muted}`. Height 48px, `{rounded.sm}`.

**`search-bar`** — Sits on `{colors.surface-subtle}` near-white with a muted search icon in `{colors.muted}`. On desktop it occupies the right cluster of the nav; on mobile it expands full-width below the nav row. Height 44px, `{rounded.sm}`.

### Navigation

**`nav-bar`** — Full-width navy (#002955) at 72px on desktop; all labels and icons in `{colors.on-primary}` white at `{typography.nav-link}`. Logo anchors left, primary category links center, cart/account icons right. On scroll the `nav-bar-scrolled` variant drops a soft navy box-shadow without changing color. Mobile collapses all links into a hamburger drawer that opens a full-width navy overlay.

### Product Cards

**`product-card`** — White card with `{rounded.sm}` corners and a 1px `{colors.hairline}` border. Product image fills the top third; below, a padding block contains the name in `{typography.title-md}`, a horizontal row of `feature-badge` pills for certifications, price in `{typography.price-display}`, and the teal add-to-cart `button-primary`. On hover a navy-tinted `box-shadow` lifts the card without distorting the border. On mobile the card goes full-width single column.

### Hero

**`hero-section`** — Deep navy background, minimum 580px height on desktop. Headline in `{typography.display-xl}` at 48px/600 weight, reversed out in `{colors.on-primary}`. Body paragraph at `{typography.body-md}`. The primary CTA button uses `{colors.cta}` teal fill; the secondary CTA uses a white-bordered outline style with `{colors.on-primary}` text. Product image anchors the right half of a split layout on desktop; on mobile the image stacks below the text block. Subhero sections with a soft `{colors.surface-soft}` background use `{typography.display-md}` in `{colors.ink}` for product-family headlines.

### Badges and Tags

**`feature-badge`** — Soft lavender-gray fill (`{colors.surface-soft}`) in a `{rounded.full}` pill; used for certifications like "Energy Star", "HEPASilent Ultra", and "App Compatible". Type at `{typography.badge}` 11px/700. Sits as a horizontal row of pills beneath the product name on cards and PDPs.

**`award-badge`** — Teal fill, white type, `{rounded.xs}` square-ish corner; used as an image overlay on product cards to flag best-seller or editor's-choice status. Intentionally sharper than `feature-badge` to distinguish editorial from certification.

**`subscription-tag`** — Hollow pill with `{colors.cta}` teal border and teal label; marks filter subscription or replacement program enrollment. Appears in the cart and on PDP pricing rows to separate one-time purchase from recurring.

### Filter Chips

**`filter-chip`** / **`filter-chip-active`** — A horizontally scrolling row of room-size, CADR-tier, price-range, or product-series filters. Idle: white canvas, `{colors.hairline}` border, `{colors.body}` text. Active: solid `{colors.primary}` navy fill, white type. Both variants use `{rounded.full}` at 36px height for quick thumb interaction. No wrapping — mobile overflow scrolls.

### Specification Table

**`spec-row`** — Uppercase `{typography.spec-label}` in `{colors.muted}` left, value in `{typography.body-sm}` `{colors.ink}` right, divided by a `{colors.hairline-soft}` bottom rule. Used across all product detail pages for CADR, room coverage, noise level (dB), filter life, and energy consumption. Dense but never compressed — 12px vertical padding per row keeps the grid scannable.

### Comparison Table

**`comparison-table`** — Header row in `{colors.primary}` navy with `{colors.on-primary}` white labels in `{typography.title-sm}`. Data rows alternate between `{colors.canvas}` and `{colors.surface-subtle}` for zebra-stripe legibility. Spec labels in `{typography.spec-label}` `{colors.muted}` left column; values in `{typography.body-sm}` `{colors.ink}` in model columns. Horizontal scroll on mobile with the label column frozen.

### Promotional Banner

**`promo-banner`** — 40px full-width navy strip above the nav bar. White `{typography.body-sm}` text for free-shipping or sale copy; inline action link in `{colors.cta}` teal. Dismissible on mobile with a close icon in `{colors.on-primary}` white.

### Breadcrumb

**`breadcrumb`** — `{typography.caption}` in `{colors.muted}` for ancestor nodes; active node in `{colors.ink}`. Separator uses `{colors.hairline}` slash character. Sits below the nav bar on category and product detail pages.

### Footer

**`footer`** — Returns to `{colors.primary}` navy, forming a structural bookend with the nav. Section headings in `{typography.title-sm}` white; link text in `{colors.hairline}` gray at `{typography.body-sm}`; legal and meta links drop to `{colors.muted-soft}`. Four-column grid on desktop collapses to stacked accordions with `{colors.hairline-soft}` dividers on mobile. Newsletter input row uses `text-input` with a teal `button-primary` submit button inline.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger overlay on `{colors.primary}` navy; hero stacks headline above image; filter chips scroll horizontally, no wrap; product grid 1 column; spec table full-width; comparison table horizontal scroll with frozen label column; footer becomes stacked accordions |
| Tablet | 744–1128px | 2-column product grid; nav shows primary links, hides secondary dropdowns; hero side-by-side at reduced padding; filter chip row allows 2-row wrap before enabling overflow scroll; comparison table shows 2 model columns |
| Desktop | 1128–1440px | 3–4 column product grid; full nav with all category links visible; hero at full 580px min-height with split image/text; spec and comparison tables in full multi-column layout on PDPs |
| Wide | > 1440px | Content container max-width 1400px centered; hero and footer backgrounds bleed edge-to-edge; nav gains breathing room between link items; product grids cap at 4 columns |

### Touch Targets
- Filter chips minimum 36px height with at least 8px horizontal gap between pills
- Mobile nav drawer items minimum 48px tap height
- Add-to-cart and all primary CTA buttons fixed at 48px height
- Icon buttons (cart, search, hamburger) minimum 44×44px touch area
- Spec table rows minimum 44px touch height on mobile for accordion expand

### Collapsing Strategy
- Desktop horizontal nav → mobile full-screen navy hamburger drawer
- 4-column product grid → 2-column (tablet) → 1-column (mobile)
- Side-by-side hero image+text → stacked image below text on mobile
- Horizontal filter chip row clips with `overflow-x: scroll` on mobile; no wrapping
- Comparison table frozen first column + horizontal scroll on tablet and mobile
- Desktop footer 4-column grid → mobile `{colors.hairline}` divider accordions on navy
- Promo banner height can collapse from 40px to 32px on mobile to conserve vertical space

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No `meta theme-color` extracted; mobile browser chrome color unconfirmed — likely `#002955` navy based on nav
- Exact button border-radius in pixels not confirmed from extracted CSS; `{rounded.sm}` (8px) is inferred from visual inspection of the live site
- Hover and focus state transition timing and duration not available from static extraction
- Gilroy has nine named weights (Thin through Black); only the 400–600 range is inferred here — use of 700 or 800 on hero display is unverified
- `{colors.cta-active}` (#0a616a) is a darkened derivative of the extracted #0e7a82, not directly scraped
- `{colors.primary-active}` (#00244b) is extracted from the palette but its exact role (nav hover, active state, footer gradient) is unconfirmed
- Price display size (22px) and cart icon style are inferred, not extracted from CSS
- Mobile nav drawer animation curve and drawer width not captured
- Product comparison table exact column count and sticky behavior not confirmed
- Shopify checkout, cart drawer, and order-confirmation pages likely fall back to Shopify defaults and are outside this spec
- `oke-widget-icons` review-widget icon font styles and color overrides not extracted
- Dark-mode or high-contrast alternate theme not confirmed to exist
