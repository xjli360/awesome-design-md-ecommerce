---
version: alpha
name: "Palm Beach Autographs"
source_url: "https://palmbeachautographs.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The first visual fact is amber against black — #fca000 punching out of a #121212 field the way a spotlight hits a jersey in a trophy case. Palm Beach Autographs stages signed memorabilia on a dark canvas that signals vault weight rather than storefront brightness, and every design decision downstream flows from that framing choice. Alternate Gothic No. 1 D compresses headline names into the same tight column-width that sports publishing has used for press credentials and program covers since the offset-printing era; stacked in all-caps at display sizes, a player's name achieves the same visual authority on screen as on a stadium banner. For moments demanding even more spectral density, Prohibition steps in with its ink-heavy condensed geometry. The everyday interface — navigation links, body copy, input labels, filter text — runs in Assistant, a geometric sans that disappears into the chrome and keeps attention on the merchandise.

  Gold carries triple meaning here: it colors the primary CTA, marks authenticated provenance iconography, and invokes the literal gold ink of premium signing events. At active states, #fca000 shifts to #d88c00, maintaining contrast on the dark surface without breaking register. A secondary red — #d82727 — stakes out sale prices and urgency rails, reading as team-jersey crimson without competing with the primary. Authentication trust seals reach for #008c62, a green that the collectibles market has conditioned buyers to read as certified and verified. Link and informational accents pull from #405de6 and #334fb4, blues that signal navigational purpose without challenging gold's dominance.

  Card geometry is deliberately rectilinear: corners land at {rounded.xs} (4px), echoing the hard edges of trading cards, photographs, and framed prints — the physical objects being represented. Only pill-shaped category filters and authentication badges break into soft curves at {rounded.full}. Hairlines sit at #4d4d4d, holding grid structure visible against the dark field without lifting the surface. The result is a site that feels less like a lifestyle store and more like an authenticated archive: authoritative, display-oriented, lit from within by amber.

colors:
  primary: "#fca000"
  primary-active: "#d88c00"
  primary-disabled: "#7d5000"
  accent-red: "#d82727"
  accent-green: "#008c62"
  accent-blue: "#405de6"
  accent-blue-deep: "#334fb4"
  ink: "#f2f2f2"
  body: "#e6e6e6"
  muted: "#b3b3b3"
  muted-soft: "#808080"
  hairline: "#4d4d4d"
  hairline-soft: "#292929"
  canvas: "#121212"
  surface-soft: "#1a1a1a"
  surface-card: "#222222"
  surface-raised: "#2d2d2d"
  on-primary: "#121212"
  on-dark: "#f2f2f2"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'alternate-gothic-no-1-d', Arial Narrow, Arial, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'alternate-gothic-no-1-d', Arial Narrow, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.2px
    textTransform: uppercase
  display-sm:
    fontFamily: "'prohibition', 'alternate-gothic-no-1-d', Arial Narrow, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0
  title-md:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'eurostile', 'Assistant', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'eurostile', 'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  label-caps:
    fontFamily: "'Open Sans', 'Assistant', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
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
    padding: 12px 24px
    height: 44px
    hover:
      backgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    hover:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    hover:
      borderColor: "{colors.muted}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    focus:
      borderColor: "{colors.primary}"
      outline: "2px solid {colors.primary}"
      outlineOffset: 2px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "10px 48px 10px 14px"
    height: 44px
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.xs}"
      width: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    logoMaxWidth: 200px
    activeLinkColor: "{colors.primary}"
    activeLinkBorderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "4/3"
    padding: "{spacing.md}"
    playerName:
      typography: "{typography.title-sm}"
      textColor: "{colors.ink}"
    categoryLabel:
      typography: "{typography.label-caps}"
      textColor: "{colors.muted}"
    price:
      typography: "{typography.price-display}"
      textColor: "{colors.primary}"
    salePrice:
      typography: "{typography.price-display}"
      textColor: "{colors.accent-red}"
    originalPrice:
      typography: "{typography.price-sm}"
      textColor: "{colors.muted}"
      textDecoration: line-through
    hover:
      borderColor: "{colors.primary}"
      boxShadow: "0 4px 16px rgba(252,160,0,0.15)"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    minHeight: 480px
    overlay: "linear-gradient(to right, rgba(18,18,18,0.9) 40%, transparent 100%)"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.display-sm}"
    subtitleColor: "{colors.body}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.muted}"
    accentRule:
      width: 4px
      backgroundColor: "{colors.primary}"
      height: 100%
  authentication-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "#ffffff"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
    iconSize: 12px
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "#ffffff"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  provenance-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  price-block:
    currentPrice:
      typography: "{typography.price-display}"
      textColor: "{colors.primary}"
    salePrice:
      typography: "{typography.price-display}"
      textColor: "{colors.accent-red}"
    originalPrice:
      typography: "{typography.price-sm}"
      textColor: "{colors.muted}"
      textDecoration: line-through
    shippingNote:
      typography: "{typography.caption}"
      textColor: "{colors.muted}"
  category-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
    active:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      borderColor: "{colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline}"
  trust-strip:
    backgroundColor: "{colors.surface-soft}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    iconColor: "{colors.primary}"
    iconSize: 16px
    padding: "{spacing.md} 0"
    layout: flex-row
    gap: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    borderTop: "3px solid {colors.primary}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    headingColor: "{colors.ink}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Renders in #fca000 amber with #121212 near-black text, delivering reverse-contrast legibility on the dark canvas; on hover the amber deepens to #d88c00. Corners sit at {rounded.xs} (4px), echoing the rectilinear geometry of trading cards and framed prints. Disabled state desaturates to #7d5000 with {colors.muted} text, preserving hierarchy signal without inviting interaction.

**`button-secondary`** — Transparent background with a 1px {colors.primary} amber border and amber text label; hover fills the field to full amber so the affordance shifts from outline to solid without layout disruption. Shares uppercase {typography.button-md} with the primary, keeping the button family visually coherent.

**`button-ghost`** — Low-priority actions (share, save, sort controls) in transparent background with {colors.hairline} 1px border and {colors.ink} text. Hover nudges the border to {colors.muted}. Never pulls attention toward itself; gold always wins the hierarchy.

### Inputs

**`text-input`** — Sits on {colors.surface-soft} (#1a1a1a) with a 1px {colors.hairline} border and {colors.muted} placeholder text. Focus state applies a 2px {colors.primary} amber outline offset by 2px, making active fields immediately identifiable against dark surfaces. Fixed at 44px height to align flush with CTA button rows.

**`search-bar`** — Extends the text-input treatment with a right-mounted submit button filled in {colors.primary} and {colors.on-primary} icon; the button is squared to {rounded.xs} consistent with the rectilinear product philosophy, not rounded to an orb. The 48px right padding accommodates the submit zone without clipping query text.

### Navigation

**`nav-bar`** — 64px dark bar on {colors.canvas} with a 1px {colors.hairline} bottom divider. Links in {typography.nav-link} (Assistant 14px/600); active links shift to {colors.primary} with a 2px amber bottom border. Logo bounded at 200px left; primary CTA button anchored top-right. On mobile, collapses to hamburger with an amber menu icon.

### Product Cards

**`product-card`** — {colors.surface-card} (#222222) base with 1px {colors.hairline} border and {rounded.xs} corners. Category label in {typography.label-caps} at {colors.muted} sits above the player name in {typography.title-sm}; price in {typography.price-display} at {colors.primary} amber. Sale price overrides in {colors.accent-red}; original price strikes through in {colors.muted}. Hover border shifts to {colors.primary} with a warm amber box-shadow diffusing beneath the card.

### Badges

**`authentication-badge`** — Pill-shaped ({rounded.full}) in {colors.accent-green} (#008c62) with white {typography.label-caps} text and a small check icon. Positioned over the product image top-right; reads as certified without requiring explanatory copy anywhere nearby.

**`sale-badge`** — Sharp {rounded.xs} rectangle in {colors.accent-red} (#d82727) with white {typography.label-caps} text. Top-left of the product image, never overlapping the authentication badge. The two badge corners share the same 4px radius, reinforcing the angular system.

**`provenance-badge`** — {colors.primary} amber with {colors.on-primary} dark text in {typography.label-caps}; marks JSA-, Beckett-, or photo-matched items. Stacks below the authentication badge when both are present.

### Hero Banner

**`hero-banner`** — Full-width dark panel with a right-bleed action photograph. A left-side gradient scrim fades from rgba(18,18,18,0.9) at 40% to transparent at the right edge, preserving image drama while guaranteeing type legibility. Title in {typography.display-xl} (Alternate Gothic, all-caps, 52px); subtitle in {typography.display-sm}; body in {typography.body-md}. A 4px vertical rule in {colors.primary} runs left of the headline stack, channeling the press-credential energy the font family already implies.

### Trust Strip

**`trust-strip`** — A slim horizontal rail between hero and product grid listing trust signals (Authentication Guaranteed, Free Returns, Secure Checkout) in {typography.caption} with small {colors.primary} amber icons. {colors.surface-soft} background, 1px {colors.hairline} borders top and bottom, items spaced at {spacing.xl} gap across a flex row.

### Price Block

**`price-block`** — Standalone price assembly for PDP and cart contexts. Current price in {typography.price-display} at {colors.primary}; sale price in same type at {colors.accent-red}; struck-through original in {typography.price-sm} at {colors.muted}; shipping note in {typography.caption} at {colors.muted} below.

### Category Filter Pills

**`category-filter`** — Pill-shaped ({rounded.full}) toggle chips on {colors.surface-soft} with {colors.hairline} border in inactive state; {typography.button-sm} text at {colors.muted}. Active state fills to {colors.primary} amber with {colors.on-primary} dark text. Used above the product grid for sport, team, and item-type facets.

### Footer

**`footer`** — {colors.surface-soft} with a 3px {colors.primary} amber top border acting as the brand's accent spine. Column headings in {typography.label-caps} at {colors.ink}; links in {typography.body-sm} at {colors.muted}, hover shifting to {colors.primary}. Padding at {spacing.xxl} top and bottom. Bottom strip carries copyright in {typography.caption} at {colors.muted}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with amber icon; hero reduces to 320px min-height with copy stacked above image, gradient removed |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories, secondary links move to side drawer; hero restores left-copy layout at 360px |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with category dropdowns; hero at 480px min-height with full gradient |
| Wide | > 1440px | Container max-width capped at 1440px, centered; hero image scales to fill; product grid stays at four columns max |

### Touch Targets

- All buttons and inputs hold a minimum 44×44px tap target regardless of visual size
- Nav links padded to 44px vertical touch area on mobile drawer
- Badge taps expand via padding to at least 32px in each axis
- Category filter pills maintain 40px height minimum on mobile

### Collapsing Strategy

- Product filters collapse to a slide-up bottom sheet on mobile; remain a left sidebar at desktop
- Category mega-dropdown flattens to an accordion inside the mobile nav drawer
- Trust strip scrolls horizontally on mobile rather than wrapping; icons scale to 16px
- Breadcrumb truncates middle path segments with ellipsis beyond three levels on mobile
- Hero vertical rule accent hidden below tablet breakpoint to reduce chrome

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No animation or transition tokens extracted; duration and easing curves inferred from Shopify defaults
- Logo dimensions, exact lockup proportions, and wordmark color variants not confirmed
- Mega-dropdown column count and featured image zone layout not confirmed from live extraction
- Exact filter/facet component styling (checkbox shape, active indicator) not captured
- No confirmed dark/light mode toggle — dark canvas treated as primary based on extracted dominant colors
- Alternate Gothic No. 1 D and Prohibition are Adobe Fonts (Typekit) — fallback rendering if Typekit is blocked not confirmed
- Cart drawer styling, upsell module layout, and checkout page typography not captured
- Hover and focus transition timings not extracted
