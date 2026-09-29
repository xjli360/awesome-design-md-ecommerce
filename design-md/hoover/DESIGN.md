---
version: alpha
name: "Hoover"
source_url: "https://www.hoover.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A sage-green accent (#aaccaa) sitting alongside fire-engine red (#bb0321) is not the palette instinct for a company that has been making cleaning equipment for over a century — yet it is precisely the move that keeps Hoover's digital storefront from reading as purely industrial. The red is unambiguous: it lands on every primary CTA, hero callout, and promotional flag, with its hover state stepping to #bf1a2f — barely a half-degree shift, enough to register as the brand pressing forward. Beneath that single voltage, three grays carry the structural load. #484848 handles body text and secondary labels; #e1e3e4 frames input strokes and card borders; #dedede draws the row separators and background hairlines. Near-black #121212 reserves itself for the heaviest display moments — hero headings and product titles — while the sage (#aaccaa) resurfaces in feature callout fills, promotional chip backgrounds, and illustrated category badges, doing the work of signaling "highlighted" without borrowing the urgency the red already owns.

  Typography is entirely Roboto, a deliberate choice for a brand whose customers compare suction wattage, filtration stages, and compatible bag SKUs in the same session they are making a purchase decision. Roboto's even stroke weight and open x-height keep spec tables and product names equally legible at 12px and 32px. Display headings push to weight 700 to hold their own against photography-forward hero layouts; body and UI labels stay at 400–500 so spec-heavy product pages do not collapse into visual noise. Button labels sit at 500 weight and 15px inside a modestly squared CTA shape — `{rounded.sm}` at 4px — that skips the pill trend in favor of something more engineered, matching the mechanical aesthetic of upright vacuums and robot mops without going fully boxy.

  What makes the system distinctive in its category is the two-color signal discipline: most appliance brands default to charcoal-on-white with a blue primary, and Hoover has instead committed to a red-and-sage pairing where red means act and sage means feature. The white canvas and cool mid-grays give product photography the room it needs; neither the red nor the sage appears unless it has a job to do. That restraint is what makes the red feel loud when it does fire.

colors:
  primary: "#bb0321"
  primary-hover: "#bf1a2f"
  primary-active: "#9a0019"
  primary-disabled: "#e8a0ac"
  accent-sage: "#aaccaa"
  accent-sage-muted: "#c8ddc8"
  ink: "#121212"
  body: "#484848"
  muted: "#767676"
  hairline: "#dedede"
  hairline-soft: "#e1e3e4"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-sage: "#eef4ee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  rating-star: "#bb0321"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-strong:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-upper:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
    height: 48px
    textTransform: uppercase
    letterSpacing: 0.5px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 48px
    textTransform: uppercase
  button-secondary-hover:
    backgroundColor: "{colors.surface-sage}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline-soft}"
    borderFocus: "1px solid {colors.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    activeColor: "{colors.primary}"
    hoverColor: "{colors.primary}"
  nav-utility-icon:
    color: "{colors.body}"
    hoverColor: "{colors.primary}"
    size: 24px
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    nameTypography: "{typography.title-md}"
    nameColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    ratingColor: "{colors.rating-star}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.hairline}"
    minHeight: 480px
    ctaButton: "{components.button-primary}"
    overlayScrim: "linear-gradient(to right, rgba(18,18,18,0.7) 40%, transparent)"
  promo-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  sage-badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline-soft}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    height: 48px
    iconColor: "{colors.muted}"
    submitButtonBackgroundColor: "{colors.primary}"
    submitButtonColor: "{colors.on-primary}"
    submitButtonRounded: "{rounded.none} {rounded.sm} {rounded.sm} {rounded.none}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    height: 36px
  filter-chip-active:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.accent-sage}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    height: 36px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    hoverBorder: "2px solid {colors.primary}"
    hoverTextColor: "{colors.primary}"
    padding: "{spacing.lg}"
    iconSize: 48px
  spec-row:
    backgroundColor: "{colors.canvas}"
    altBackgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "10px {spacing.base}"
  feature-callout:
    backgroundColor: "{colors.surface-sage}"
    borderLeft: "4px solid {colors.accent-sage}"
    headlineTypography: "{typography.title-md}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.caption-strong}"
    headingColor: "{colors.on-dark}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Hoover red (#bb0321) fill with white uppercase label at {typography.button-md}, 48px tall, {rounded.sm} corners. Hover state steps to #bf1a2f; active press drops to {colors.primary-active} (#9a0019). Disabled washes to {colors.primary-disabled} with white text and a `not-allowed` cursor. The uppercase treatment and 0.5px letter-spacing give the button a hardware-catalogue authority that matches the product's mechanical character.

**`button-secondary`** — Transparent fill with a 2px solid red (#bb0321) border and red label at {typography.button-md} uppercase. Hover fills with {colors.surface-sage} (#eef4ee) — a soft green wash that signals interactivity without borrowing the urgency of the filled primary. Height matches primary at 48px so the two can sit in a row without size disparity.

**`button-ghost`** — Hairline-bordered utility button at 40px for secondary actions like "View All" links in category grids. Body-gray text, no fill, {rounded.sm}. Used where a full outlined-red button would over-weight the hierarchy.

### Text Input & Search

**`text-input`** — White fill, {colors.hairline-soft} border at rest, darkening to {colors.body} (#484848) on focus with no ring. Roboto {typography.body-md} at 16px; placeholder in {colors.muted}. Height 48px aligns with buttons in horizontal search layouts.

**`search-bar`** — Inline search combining a text input with a flush-right red submit button. The input uses {rounded.sm} on left corners only; the submit button inherits right-side {rounded.sm} corners, creating a single visual unit. Focus applies a red border to the entire container. Icon search glyph sits left-padded at 20px in {colors.muted}.

### Navigation

**`nav-bar`** — White canvas bar at 64px with a single-pixel {colors.hairline} bottom border. Wordmark sits left; utility icons (search, account, cart) sit right at 24px in {colors.body} gray, turning {colors.primary} red on hover. Primary category links use {typography.nav-link} weight 500, activating to red underline on hover. A top promotional banner above the nav uses {colors.primary} red fill with white {typography.caption-strong} text for site-wide sale messaging.

### Product Card

**`product-card`** — White surface, {rounded.md} corners, 1px {colors.hairline-soft} border, and a hover shadow (`0 4px 16px rgba(0,0,0,0.10)`) that lifts the card slightly. Product name in {typography.title-md} weight 600; price in {typography.price-display} weight 700; star rating dots in {colors.rating-star} red; review count caption in {colors.muted} at {typography.caption}. Add-to-cart below the price uses `button-secondary` rather than primary — the card grid should not fire red everywhere.

### Hero Banner

**`hero-banner`** — Dark overlay on full-bleed product photography with a left-anchored text column. Headline at {typography.display-xl} weight 700 in white; subhead at {typography.body-md} in {colors.hairline}; primary CTA uses `button-primary`. The scrim gradient runs right-to-left, fading from 70% black opacity at the text column to transparent, so product imagery reads on the right half. Minimum height 480px.

### Promo Badge & Feature Callout

**`promo-badge`** — Red fill (#bb0321), white uppercase label at {typography.label-upper}, {rounded.xs} corners. Used on product cards and search results to flag sales, bundles, or new arrivals.

**`sage-badge`** — Sage fill (#aaccaa) with near-black label at {typography.label-upper}, {rounded.xs}. Used for "Award Winner", "Editor's Choice", or curated collection tags — approval signals that sit outside the promotional urgency of the red badge.

**`feature-callout`** — Soft sage background ({colors.surface-sage} #eef4ee) with a 4px left border in {colors.accent-sage}. Headline at {typography.title-md} weight 600 in {colors.ink}; body copy at {typography.body-sm} in {colors.body}. Used inline on product detail pages to call out HEPA filtration, pet-specific modes, and award recognition.

### Category Tile

**`category-tile`** — Light gray surface ({colors.surface-soft}), {rounded.md} corners, center-aligned icon at 48px, and a {typography.title-sm} label in {colors.ink} below. On hover, a 2px red border replaces the default state and the label shifts to {colors.primary}. Grid runs 4-across on desktop, 2-across on mobile.

### Spec Table

**`spec-row`** — Alternating white and {colors.surface-soft} rows. Label column at {typography.spec-label} in {colors.muted}; value column at {typography.body-sm} in {colors.ink}. Bottom hairline border in {colors.hairline}. Used on product detail pages to surface wattage, cord length, filtration type, and weight specs in a scannable two-column layout.

### Filter Chip

**`filter-chip`** — Pill-shaped at {rounded.full}, 36px tall, {colors.surface-soft} fill, hairline border, {typography.button-sm} in {colors.body}. Active/selected state switches fill to {colors.accent-sage} (#aaccaa) with {colors.ink} label and drops the border — the sage is the system's only affirmative-state color, so it reads immediately as "this filter is on."

### Footer

**`footer`** — Near-black (#121212) fill with a 3px red top border that restates the brand's primary color at the page bottom. Column headings at {typography.caption-strong} in white; links and body copy at {typography.body-sm} in {colors.hairline}, lightening to white on hover. Payment method icons and trust badges sit in a sub-footer row with a subtle hairline separator above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero drops to 320px min-height; category tiles 2-across; filter chips scroll horizontally in a single row |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories inline; hero at 400px min-height; category tiles 3-across; filter panel shifts to collapsible top bar |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with mega-menu dropdown; hero at 480px min-height; filter sidebar 240px fixed left; spec table two-column |
| Wide | > 1440px | Max-width container 1440px centered; hero background extends edge-to-edge while content column stays within grid; product grid stays at four columns with wider gutters |

### Touch Targets

- All interactive controls (buttons, chips, nav icons) minimum 44×44px on mobile
- Filter chips on mobile expand to 44px height and gain extra horizontal padding to aid thumb targeting
- Cart and account icons in the mobile nav bar padded to a 48px touch zone despite 24px visual glyph size
- Product card touch target covers the entire card surface, not just the title or image

### Collapsing Strategy

- Primary nav links collapse behind a hamburger at < 744px; drawer slides in from left over a {colors.scrim} overlay
- Promotional announcement banner persists on mobile at reduced {typography.caption} size, single line
- Hero text column stacks above the image on mobile; scrim is removed and image sits below as a full-width block
- Spec table collapses to a single full-width column on mobile with label above value, separated by {colors.hairline}
- Footer columns stack vertically on mobile, each section collapsible with a + toggle
- Search bar in the nav collapses to a magnifying-glass icon on mobile, expanding inline on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Custom icon set not identified; SVG glyph library for product category navigation (Robot, Upright, Stick, Handheld, Carpet) is not confirmed from extraction
- Exact font loading method not confirmed — Roboto may be loaded via Google Fonts CDN or bundled; no `@font-face` data extracted
- Mega-menu structure and column layout for the primary nav dropdown not extractable from static hints
- Hover/focus animation durations and easing curves not extracted; 150ms ease-in-out assumed as a framework default
- Product card image aspect ratio not confirmed; 4:3 and 1:1 both appear plausible from category layouts
- Dark mode not detected; no alternate palette defined
- Exact grid gutter widths not extracted; 16px (mobile) and 24px (desktop) assumed from Shopify framework defaults
- Checkout and account flow components not accessible from the public storefront extraction
