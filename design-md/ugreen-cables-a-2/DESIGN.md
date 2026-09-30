---
version: alpha
name: "Ugreen"
source_url: "https://www.ugreen.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Ugreen plants its brand name directly in its primary color: #007934 saturates every call-to-action button, active nav indicator, compatibility tag border, and trust icon — the hex is the brand statement, legible before any logo loads. Against a near-white canvas of #f8f8f8 sectioned by #e9eaeb hairlines, that green reads with the precision of a signal light, never competing with the product photography it frames. Metropolis drives all type — a geometric sans whose near-equal stroke widths match the clean-line engineering language that cables, adapters, and charging hubs demand. Display headers hold at 700 weight and 40px; body copy breathes at 400/16px between spec tables and feature callouts.

  The color system builds outward from the green anchor in two directions: a warm promotional tier and a cool information tier. #ee9441 orange fires on limited-time deal badges while #ee901d saturates deep discount labels; the pairing feels urgent without reading as alarm. On the cooler side, #7b1ec7 purple marks premium product tiers and #1975b7 occupies anchor links — neither enters hero compositions, reserving them as information-layer signals rather than brand statements. Error states use a dark-field red doublet (#c30000 foreground, #8b0000 for deep backgrounds) with enough visual mass to interrupt scanning without competing with the brand green. The bright accent #3ed660 surfaces only in compatibility confirmation states, a lighter cousin of the primary that signals "yes" at a glance.

  Product cards sit on #ffffff with `{rounded.md}` corners and a ghost #e9eaeb border that transitions to solid #007934 on hover — the primary hue becomes the universal active-state marker throughout the interface. The surface tint #eef8f2 underlays compatibility tags and in-stock labels, a whispered version of the primary used as a positive-state field rather than a decorative fill. Category filter pills use `{rounded.full}` geometry and invert to solid green on selection, making the active filter unmistakable in dense grid views. The footer flips to #121212, topped with a 2px #007934 rule that carries the brand's green through to its darkest register without softening it.

colors:
  primary: "#007934"
  primary-active: "#006400"
  primary-disabled: "#c8c8c8"
  ink: "#121212"
  body: "#404040"
  muted: "#a3a3a3"
  hairline: "#dadada"
  hairline-soft: "#e9eaeb"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-muted: "#f0f1f2"
  surface-card: "#ffffff"
  surface-green-tint: "#eef8f2"
  on-primary: "#ffffff"
  promo-orange: "#ee9441"
  promo-orange-deep: "#ee901d"
  accent-blue: "#1975b7"
  accent-purple: "#7b1ec7"
  accent-green-bright: "#3ed660"
  error: "#c30000"
  error-deep: "#8b0000"

typography:
  display-xl:
    fontFamily: "Metropolis, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Metropolis, -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Metropolis, -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Metropolis, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Metropolis, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Metropolis, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Metropolis, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Metropolis, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-strong:
    fontFamily: "Metropolis, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  badge:
    fontFamily: "Metropolis, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "Metropolis, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "Metropolis, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Metropolis, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Metropolis, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.2px

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
    padding: "12px 24px"
    height: 44px
    hoverBackgroundColor: "{colors.primary-active}"

  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 44px

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: "11px 23px"
    height: 44px
    hoverBackgroundColor: "{colors.surface-green-tint}"

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
    height: 36px

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px

  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 40px
    iconColor: "{colors.muted}"

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoHeight: 32px
    activeIndicatorColor: "{colors.primary}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    imageAspectRatio: "1/1"
    priceTypography: "{typography.price-display}"
    nameTypography: "{typography.title-sm}"
    captionTypography: "{typography.body-sm}"
    hoverBorderColor: "{colors.primary}"
    hoverShadow: "0 4px 16px rgba(0,121,52,0.10)"

  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    overlayGradient: "linear-gradient(90deg, rgba(18,18,18,0.85) 0%, rgba(18,18,18,0.2) 100%)"

  promo-badge:
    backgroundColor: "{colors.promo-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  sale-badge:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  compatibility-tag:
    backgroundColor: "{colors.surface-green-tint}"
    textColor: "{colors.primary-active}"
    typography: "{typography.caption-strong}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
    padding: "4px 12px"

  spec-chip:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    iconColor: "{colors.primary}"

  category-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "8px 18px"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: none

  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    headerTypography: "{typography.title-md}"
    itemNameTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    borderLeft: "1px solid {colors.hairline}"

  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    iconColor: "{colors.primary}"
    typography: "{typography.caption-strong}"
    padding: "{spacing.base}"
    rounded: "{rounded.sm}"

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.on-primary}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    borderTop: "2px solid {colors.primary}"
---

## Components

### Buttons

**`button-primary`** — Solid #007934 fill with white 600-weight Metropolis text, 44px tall and 8px radius. Hover deepens to #006400; the disabled state pulls the fill to #c8c8c8 while retaining white text. Used for Add to Cart, Shop Now, and all checkout progression steps — the green remains the only saturated fill color in any standard purchase flow.

**`button-secondary`** — White fill with a 1.5px #007934 border and matching green text. Hover washes the background to #eef8f2, echoing the primary without competing with it. Appears alongside button-primary as the secondary CTA for spec sheets, comparison views, and modal triggers.

**`button-ghost`** — Transparent background, 1px #dadada border, #404040 text, 36px height and 4px radius. Used for pagination controls, filter-reset actions, and inline content expanders where primary hierarchy is unnecessary.

### Search

**`search-bar`** — Full-pill geometry (`{rounded.full}`) set on a #f8f8f8 surface at 40px height. A muted gray icon sits at rest inside the leading edge; focus transitions the border to 1.5px #007934. Deployed persistently in the top-nav header, collapsing to an icon-only trigger on mobile that expands to a full-width overlay on tap.

### Navigation

**`nav-bar`** — 64px white bar with a 1px #e9eaeb bottom border. Logo on the left at 32px height; primary category links in 500-weight Metropolis with #007934 active underline indicators; search and cart icons on the right. A white megamenu panel drops below the bar on desktop with sub-category columns and promotional image slots.

### Product Card

**`product-card`** — White surface with 12px radius and a ghost 1px #e9eaeb border that intensifies to solid #007934 on hover, paired with a green-tinted box-shadow (rgba(0,121,52,0.10)). Product name in 600/16px title-sm, price in 700/24px price-display, and a horizontal spec-chip strip beneath the name. Badge stack — new, promo, sale — overlays the top-left corner of the product image; compatibility tags sit below the name before the price.

### Hero Banner

**`hero-banner`** — #121212 base with a left-to-right gradient overlay that fades from 85% opacity to 20%, protecting white headline legibility over dark product imagery. Heading in 700/40px display-xl, body copy in 400/16px body-md, both white. The primary CTA sits below the body using button-primary; a secondary text link in button-ghost style sits alongside it on desktop.

### Badges

**`promo-badge`** — #ee9441 orange fill, 700-weight uppercase Metropolis at 11px, 4px radius. Fires on time-limited deal pricing and bundle offers. **`sale-badge`** — #c30000 red fill for clearance and markdown events. **`new-badge`** — #007934 green fill for product launches and first-to-market items. All three share the same size and radius, stacking vertically in the top-left corner of a product card image when multiple states coexist.

### Compatibility Tags

**`compatibility-tag`** — Pill-shaped (`{rounded.full}`), #eef8f2 fill with a 1px #007934 border, #006400 text in 600/12px caption-strong Metropolis. Labels USB Power Delivery wattage tiers, MagSafe certification, and operating system compatibility. Always appears in a horizontal row beneath the product name, before the price line — a positive-state signal rather than a promotional element.

### Spec Chips

**`spec-chip`** — #f0f1f2 fill, 4px radius, 400/12px caption text. Packages discrete specifications — port count, cable length, transfer speed — in a tight horizontal strip on product cards. A small #007934 icon precedes each label, threading the primary green through at the smallest interactive scale.

### Category Pills

**`category-pill`** — Outlined pill at rest: 1px #dadada border, white fill, #404040 text. On activation inverts to solid #007934 fill with white text, border removed. Controls product grid filtering for connector type, wattage tier, and cable standard; the active state is the same green inversion used in buttons and nav indicators, maintaining a single active-state grammar site-wide.

### Cart Drawer

**`cart-drawer`** — 400px right-side slide-in on a white canvas with a 1px #dadada left border. Section header in 600/18px title-md; item names in 400/14px body-sm; unit prices in 700/24px price-display. Checkout button spans the full drawer width using button-primary styles. Quantity steppers use button-ghost geometry.

### Trust Badges

**`trust-badge`** — #f8f8f8 soft tile with 8px radius, a #007934 icon at center, and a 600/12px caption-strong label below. Deployed in a 4-across horizontal strip between the hero and the product grid: warranty duration, safety certification, return window, and support channel — the icon green anchors Ugreen's primary color into a trust-signaling register.

### Footer

**`footer`** — #121212 background entered from the page body via a 2px #007934 top border, carrying the brand's primary green through the darkest region of the page. Column headings in 600/16px title-sm white; body links in 400/14px body-sm #a3a3a3 that rise to white on hover. Social icons and payment method logos sit in the base row at reduced opacity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; search-bar expands to full-width modal on tap; hero drops to 320px min-height with centered text; trust-badge strip scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; top nav shows logo + condensed category links + icons; hero shifts to split image/text layout; category pills wrap to two rows |
| Desktop | 1128–1440px | Three- to four-column product grid; full megamenu nav; hero at 480px with left-aligned text overlay; trust-badge strip in a fixed 4-across row |
| Wide | > 1440px | Content container max-width 1440px centered; hero image bleeds edge-to-edge; product grid caps at four columns; side canvas fills with #f8f8f8 |

### Touch Targets

- All interactive buttons maintain 44×44px minimum tap area
- Category pills add 4px invisible vertical padding on mobile to reach 44px height
- Cart, search, and nav icons expand to 44px tap zones via surrounding padding
- Spec-chips are display-only on mobile; horizontal swipe replaces hover-to-reveal

### Collapsing Strategy

- Primary nav collapses at 744px into a full-screen slide-in drawer with accordion category sections and a persistent search input at the top
- Megamenu panels are disabled below 1128px; category links navigate directly without sub-menus
- Hero headline scales from display-xl (40px) to display-md (28px) below 744px
- Footer columns stack from 4-across to 2-across at tablet, single-column at mobile with full-width dividers between sections
- Product card spec-chip strip truncates to three chips on mobile with a "show more" text expander

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; mobile browser chrome color and PWA/home-screen tile color are unknown
- Canvas white (#ffffff) was likely filtered as a framework default and is assumed; not directly confirmed from extraction
- Exact Metropolis weight and size scale were not extractable from the live site; values derived from geometric sans conventions suitable for a technical accessories brand
- Hover and focus transition durations and easing curves not captured
- Megamenu structure — column count, featured image panel dimensions, sub-category groupings — not confirmed from extraction
- #7b1ec7 purple and #1975b7 blue positional roles (premium tier vs. link vs. badge) inferred from color hierarchy; exact usage contexts not confirmed
- Loyalty or rewards tier badge colors not confirmed
- Mobile navigation drawer background color and section divider treatment not extracted
- Product image container background (pure white vs. #f8f8f8 lightbox crop) not confirmed
