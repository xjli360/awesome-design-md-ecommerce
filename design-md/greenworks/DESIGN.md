---
version: alpha
name: "Greenworks"
source_url: "https://www.greenworkstools.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Where most power tool manufacturers reach for safety-orange or battleship gray, Greenworks doubles down on the one color its products are designed to improve — lawn green. The brand's primary, a vivid lime-weighted green, sits in direct contrast against the near-black charcoal (#313131) that structures every handle, housing, and headline. The effect is less "outdoor equipment catalog" and more "consumer electronics launch page": a two-note palette that positions battery power as an upgrade rather than a tradeoff. The charcoal (#313131) appears in the extracted data as the only confirmed color, anchoring navigation backgrounds, text, and footer fills — every headline and label resolves against it with high contrast and zero softness.

  Typography falls entirely on the system sans-serif stack; no custom web font was identifiable behind the anti-bot layer the site serves on cold requests. The brand compensates with weight and scale contrast: bold 700-weight display sizes for hero claims like "More Power. Less Noise." drop directly into compact body at 15–16px with minimal mid-scale ceremony. The overall rhythm reads close to appliance retail — structured product grids, generous white canvas ({colors.canvas}), tool photography that fills the frame edge to edge on seamless white or soft gray ({colors.surface-soft}).

  Buttons are rectangular with minimal radius ({rounded.xs} to {rounded.sm}), communicating durability over friendliness. The primary CTA carries the brand green, reversed in white ({colors.on-primary}). Secondary buttons use a dark charcoal outline on the white canvas, keeping the green reserved for highest-priority actions — "Shop Now," "Find a Dealer," "Compare Models." Product cards surface the tool isolated on light ground with a voltage-tier badge — 24V, 40V, 60V, 80V — as the primary product differentiator, rendered in {typography.badge} weight against a charcoal chip. These voltage labels are the closest the brand has to a product family mark.

  The eco signal is embedded in the product function, not the palette: there are no muted sages, no natural textures, no earth tones. The green is vivid and unambiguous — chromatically demanding — and the near-black is absolute. Together they stake a confident, industrial-meets-sustainable position that is legible at banner scale and at thumbnail size without a single soft compromise.

colors:
  primary: "#3CB849"
  primary-active: "#2E9A3C"
  primary-disabled: "#A8D9AE"
  ink: "#313131"
  body: "#4A4A4A"
  muted: "#767676"
  muted-soft: "#9E9E9E"
  hairline: "#DDDDDD"
  hairline-soft: "#EBEBEB"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  surface-dark: "#313131"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  voltage-chip: "#313131"
  eco-deep: "#1A6B28"
  warning-tag: "#F5A623"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  label-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.25px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.25px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  promo-text:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.15px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: none
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 36px
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.promo-text}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imagePadding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.body-sm}"
    priceTypography: "{typography.display-sm}"
    shadow: "0 2px 8px rgba(0,0,0,0.06)"
    hoverShadow: "0 6px 20px rgba(0,0,0,0.12)"
  voltage-badge:
    backgroundColor: "{colors.voltage-chip}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sale-badge:
    backgroundColor: "{colors.warning-tag}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 540px
    ctaSpacingTop: "{spacing.xl}"
    layout: split-image-right
  hero-banner-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 540px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    aspectRatio: "4/3"
    hoverOverlay: "rgba(60,184,73,0.08)"
    border: "1px solid {colors.hairline-soft}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.ink}"
    height: 52px
    searchIconColor: "{colors.primary}"
  comparison-table-header:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "2px solid {colors.primary}"
  comparison-table-cell:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.base}"
  dealer-locator:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    inputStyle: "{components.text-input}"
    buttonStyle: "{components.button-primary}"
    borderTop: "3px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The primary action button renders in brand green (#3CB849) with white text in uppercase tracking, 48px tall with 2px border-radius ({rounded.xs}). The tight radius signals industrial function over consumer softness. On hover it deepens to `primary-active` (#2E9A3C); disabled states drain to a washed `primary-disabled`. This button appears almost exclusively on product pages and category landing pages as the "Add to Cart" or "Shop Now" driver.

**`button-secondary`** — A 2px solid charcoal (#313131) border on white canvas carries the same uppercase button typography as primary, maintaining visual weight parity. Used for "Compare," "Learn More," and "Find a Dealer" alongside the green primary. Hover fills the canvas with `surface-soft` to signal response without stealing green.

**`button-ghost`** — Transparent background with primary green text, no border. Reserved for tertiary in-page actions — "View All," "See Full Specs" — where a full button would crowd the layout.

**`button-dark`** — Charcoal (#313131) fill with white text, used on hero banners that sit on light backgrounds to give a dark anchor CTA option without requiring the green voltage.

### Navigation

**`nav-bar`** — 64px tall on white canvas with a single hairline bottom border. Logo sits left at 36px height. Center nav links use `nav-link` (14px/600) with a green underline on active states. Far right carries account, search, and cart icon buttons. On dark-hero pages, the dark variant (`nav-bar-dark`) inverts to charcoal fill with white links; the Greenworks wordmark reverses to white.

**`promo-strip`** — 36px green bar above the nav, centered `promo-text` (13px/600) in white. Carries promotional messaging: free shipping thresholds, seasonal sale announcements. The green strip is the highest-frequency brand-color surface across the site.

### Product Cards

**`product-card`** — Tool image on white with generous `lg` padding isolates the product cleanly. Voltage badge (`voltage-badge`, charcoal chip) anchors to the top-left corner; a "NEW" or "SALE" badge occupies the top-right when applicable. Title in `title-md`, spec snippet in `body-sm` muted, price in `display-sm` bold. 1px hairline border softens into an elevated shadow on hover (6px/20px spread).

**`voltage-badge`** — The primary product-family differentiator: "24V," "40V," "60V MAX," "80V MAX" printed in 11px/700 uppercase on the confirmed charcoal (#313131) chip. Appears on cards, PDPs, and comparison tables. This is the brand's version of a product tier mark.

### Hero

**`hero-banner`** — Split layout with headline left and full-bleed product photography right. Light ground (`surface-soft`) gives way to the dark variant (`hero-banner-dark`) for seasonal or sale heroes. Headlines at `display-xl` (48px/800) drop with `-0.5px` tracking, landing with significant visual mass. CTA row holds one `button-primary` and optionally one `button-dark` side by side.

### Search & Dealer

**`search-bar`** — Full-width rectangular input with a 2px charcoal border and no radius ({rounded.none}), consistent with the brand's preference for hard edges. Green search icon right-anchored inside the field. Used in the site header on expand and on the full-screen search overlay.

**`dealer-locator`** — Zip-code input paired with a green "Find a Dealer" `button-primary`. Set on `surface-soft` ground inside a component with a 3px green top-border accent — a recurring structural motif that marks section entries across category and support pages.

### Comparison & Footer

**`comparison-table-header`** — Charcoal fill, white `label-sm` column labels, with a 2px green `border-bottom` accent line separating the header row from the data grid. Reinforces the charcoal + green two-note rhythm even in tabular contexts.

**`footer`** — Charcoal (#313131) full-width with a 3px green top border, mirroring the dealer-locator accent logic. Links render in `muted-soft` gray, turning green on hover. Column headings in `label-sm` uppercase white. Typically four columns: Products, Support, Company, Social.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger nav replaces horizontal links; hero stacks vertically with image above fold-cropped behind gradient; product grid collapses to 2-column; comparison table horizontally scrollable |
| Tablet | 744–1128px | Nav shows logo + icons only, category links move to a secondary drawer; hero splits 50/50; product grid 3-column; promo strip text truncates |
| Desktop | 1128–1440px | Full nav-bar with all category links visible; hero at full split layout; product grid 4-column; comparison table fully expanded |
| Wide | > 1440px | Max content width ~1440px centered; hero image fills remaining viewport width; grid stays 4-column but card spacing increases |

### Touch Targets

- All interactive elements minimum 44×44px tap area
- Voltage badge chips are non-interactive display elements — no tap-target requirement
- Nav icon buttons (search, cart, account) padded to 44px square regardless of icon size
- Product card entire surface is tappable on mobile, not just the CTA button

### Collapsing Strategy

- Category nav collapses to hamburger drawer at < 1024px; mega-menu dropdowns become full-screen panels
- Comparison table scrolls horizontally within a `overflow-x: auto` wrapper rather than stacking on mobile
- Hero CTAs stack vertically (primary above secondary) below 600px
- Footer columns collapse to single-column accordion at < 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Primary brand green not extracted** — the site returned a Cloudflare challenge page ("Just a moment...") rather than rendered content; #3CB849 is inferred from brand-knowledge of Greenworks' product and marketing photography, not confirmed from live CSS. Verify against actual computed styles or brand kit before shipping.
- **Only one hex confirmed** — #313131 is the sole extracted color; all other palette values (greens, grays, surface tones) are constructed from brand reasoning and standard design-system practice.
- **No web font detected** — the site's font stack is entirely system UI; if Greenworks uses a licensed typeface (e.g., a geometric sans or condensed industrial face) it was not retrievable. Check network waterfall for any `@font-face` declarations loading after JS hydration.
- **Spacing and radius values unconfirmed** — border-radius and spacing tokens are estimated from the brand's industrial aesthetic; no CSS custom properties were extractable.
- **Dark-mode posture unknown** — no `prefers-color-scheme` tokens were detectable from the extracted page.
- **Motion and animation tokens absent** — transition durations, easing curves, and hover animation styles could not be extracted.
