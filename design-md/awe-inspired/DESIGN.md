---
version: alpha
name: "Awe Inspired"
source_url: "https://www.aweinspired.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep midnight navy (#272d45) is the first atmospheric impression at Awe Inspired — not a neutral backdrop but a deliberate choice that positions each piece as something ceremonial rather than commercial. The brand sells jewelry in the language of empowerment, energetic resonance, and intention-setting; the deep saturated navy communicates gravity without the harshness of pure black (#121212). From that foundation, dusty indigo (#676986) handles secondary surfaces — muted body text, supporting labels, quiet navigation links — giving the palette a ritualistic depth that most gold-and-ivory jewelry brands never attempt. The warm sand and gold tones (#baa58d, #d3bc8d) feel earned rather than decorative: they emerge from the dark canvas like precious metal catching ambient light, doing the work that overt metallic swatches usually overstate. Amber (#ee9441) appears in promotional badges and callout states, terracotta (#b44220) in limited accent contexts — together they form a warm chromatic arc echoing natural stone, resin, and unpolished gold without illustrating any of those things directly. A teal (#0e7a82) surfaces rarely, possibly for email capture modules or a specific collection line. Figtree — a geometric sans with subtly softened terminals — handles all type. It avoids both the cold sharpness of pure grotesques and the nostalgia of editorial serifs, landing in a zone that reads as modern and accessible without demanding attention away from the product. Display headings lean on weight 500–600 rather than bold; the brand trusts the deep navy canvas to carry visual authority without typographic force. Primary CTAs sit in full-pill geometry ({rounded.full}), echoing circle shapes common in amulet and talisman iconography, while product cards use softer {rounded.md} corners. The near-white canvas (#f4f4f6) carries a faint blue-lilac undertone that keeps the midnight navy from reading as oppressive and unifies surface treatments across page sections. The overall composition reads as digital altar rather than boutique storefront — precise and built for buyers who understand jewelry as a personal practice.

colors:
  primary: "#272d45"
  primary-active: "#1c1b1f"
  primary-hover: "#3a4060"
  primary-disabled: "#9a9db1"
  indigo-mid: "#676986"
  ink: "#121212"
  body: "#323232"
  muted: "#676986"
  hairline: "#d1d1d1"
  hairline-soft: "#e5e5e5"
  canvas: "#f4f4f6"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#f4f4f6"
  on-dark: "#f4f4f6"
  accent-gold: "#d3bc8d"
  accent-sand: "#baa58d"
  accent-amber: "#ee9441"
  accent-terracotta: "#b44220"
  accent-teal: "#0e7a82"

typography:
  display-xl:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-label:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Figtree', sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 12px rgba(39,45,69,0.08)"
    height: 60px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    imageBorderRadius: "{rounded.sm}"
    padding: "{spacing.base}"
    hoverElevation: "0 4px 20px rgba(39,45,69,0.12)"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaVariant: "button-primary-gold"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
  collection-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-sale:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  empowerment-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    borderLeft: "3px solid {colors.accent-gold}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  jewelry-detail-panel:
    backgroundColor: "{colors.surface-card}"
    titleTypography: "{typography.display-md}"
    priceTypography: "{typography.price-display}"
    descriptionTypography: "{typography.body-md}"
    accentColor: "{colors.accent-gold}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    iconColor: "{colors.indigo-mid}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
  swatch-selector:
    activeBorder: "2px solid {colors.primary}"
    inactiveBorder: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    size: 28px
    gap: "{spacing.sm}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    height: 44px
    width: 120px
  trust-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-label}"
    iconColor: "{colors.accent-gold}"
    paddingVertical: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.accent-sand}"
    headlineTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid rgba(244,244,246,0.12)"
    paddingVertical: "{spacing.section}"

## Components

### Buttons
**`button-primary`** — Full-pill ({rounded.full}) midnight navy (#272d45) fill, 48px tall with 32px horizontal padding, Figtree 15px/600. Hover state shifts to #3a4060; disabled state fills with muted indigo-gray (#9a9db1). The pill geometry is the brand's most legible recurring motif — it mirrors the circle and amulet shapes throughout jewelry photography and icon treatments.

**`button-secondary`** — Transparent background with a 1.5px navy border and navy text, identical pill geometry and height to primary. Used for secondary CTAs on product detail pages and checkout flows; pairs naturally with button-primary in two-CTA layouts without competing for hierarchy.

**`button-ghost`** — Lower-prominence pill with hairline border (#d1d1d1) and body-color text. Used for "view all" links, filter dismissals, and tertiary navigation actions where visual weight must stay minimal.

**`button-primary-gold`** — Used specifically in hero banners and dark-surface sections; accent gold (#d3bc8d) fill with midnight navy text. Provides warm metal-adjacent resonance against the dark navy hero without the contrast harshness of a bright white CTA.

### Navigation
**`nav-bar`** — 64px tall, canvas (#f4f4f6) background with a hairline (#d1d1d1) border-bottom. Figtree 14px/500 for all nav links. A scrolled variant adds a soft navy-tinted box-shadow (rgba(39,45,69,0.08)) to signal elevation. Logo renders in midnight navy against the pale canvas. Cart and account icons render in body or muted ink.

### Product Card
**`product-card`** — White (#ffffff) surface with 12px rounded corners ({rounded.md}) and 16px internal padding. Product image uses 8px corners ({rounded.sm}). Title in title-sm (16px/600), price in price-display (20px/600), supporting text in body-sm. On hover, a soft navy-tinted elevation shadow (rgba(39,45,69,0.12)) lifts the card. Badge chips (badge-new, badge-sale) overlay the top-left image corner using full-pill geometry.

### Hero Banner
**`hero-banner`** — Full-bleed midnight navy (#272d45) background with display-xl headline in on-dark (#f4f4f6), body-md supporting copy in on-dark, and a button-primary-gold CTA for warm contrast. Section-scale vertical padding (64px). Background may incorporate product imagery with a dark overlay to retain the navy atmosphere.

### Badges
**`collection-badge`** — Warm amber fill (#ee9441) with navy text, full-pill, uppercase 11px/700. Used for collection labels, "staff picks," and featured-item callouts on grid pages.

**`badge-new`** — Navy fill with on-primary text, same pill geometry. Applied as an image overlay on new arrival products.

**`badge-sale`** — Terracotta fill (#b44220) with white text. Used for promotional pricing and markdown states. The terracotta is tonally warm and avoids the urgency-signaling red common to discount-driven sites.

### Trust Strip
**`trust-strip`** — Full-width midnight navy bar, accent gold icons (#d3bc8d), uppercase caption-label type in on-dark. Communicates free shipping thresholds, return policy, and brand empowerment statements in a single horizontal band typically placed directly below the nav or above the footer.

### Empowerment Callout
**`empowerment-callout`** — Off-white surface (#f7f7f7) with a 3px accent-gold left-border, display-sm headline in midnight navy, body-md editorial copy. This is a distinctively on-brand section type — used for narrative content about piece intentions, crystal properties, and collection backstories — absent from most purely transactional jewelry sites.

### Jewelry Detail Panel
**`jewelry-detail-panel`** — Product detail layout with display-md title, price-display pricing, and body-md description. Accent gold used as a decorative horizontal rule or icon accent color between the price and the add-to-cart area. No rounded corners on the panel itself (rounded.none) — the panel bleeds against the page canvas with the card surface providing quiet separation.

### Search
**`search-bar`** — Full-pill ({rounded.full}) search field, 44px tall, with an indigo-mid (#676986) search icon. Rendered in a dropdown overlay or dedicated search drawer. Focus ring applies the primary navy border color; placeholder text uses the muted indigo (#676986).

### Footer
**`footer`** — Full midnight navy (#272d45) background with on-dark body copy and warm sand (#baa58d) link color for navigational links. Title-sm column headers, body-sm link lists. A barely-visible top border (12% opacity white) separates footer from page content. Newsletter input field within the footer uses the standard text-input component.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with slide-in drawer over a midnight navy overlay; hero headline drops to display-md (32px); trust strip scrolls horizontally; product card image fills full column width; add-to-cart expands to full-width button |
| Tablet | 744–1128px | Two-column product grid; nav links visible but compact; hero shifts to stacked image-over-copy or side-by-side at mid-tablet; jewelry detail panel stacks image above text; empowerment callouts go full width |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with all collection links visible; hero displays full-bleed with large display-xl headline; detail panel renders in two-column layout with image on the left |
| Wide | > 1440px | Max-width container (~1400px) centered with hero background bleeding full width; product grid stays at four columns with increased gutter; footer columns expand with more whitespace |

### Touch Targets
- All buttons minimum 44px tall; pill geometry ensures adequate horizontal touch area at typical label lengths
- Swatch selectors minimum 28px diameter, 4px gap between swatches, with a 2px navy border ring on active state
- Hamburger nav icon minimum 44×44px tap area
- Add-to-cart expands to full-width on mobile viewport (with 16px horizontal margin each side)
- Quantity selector minimum 44px tall; stepper buttons minimum 44px wide

### Collapsing Strategy
- Navigation: collection links collapse to hamburger below 1128px; search becomes icon-only below 744px; mega-menu drops to a flat list in the drawer
- Hero: two-column layout collapses to stacked (image above headline) at tablet; hero image may be suppressed on smallest viewports to prioritize CTA visibility
- Product grid: 4 → 3 → 2 → 1 column as viewport narrows
- Empowerment callout sections: multi-column layout collapses to single column; left-border accent retained at all breakpoints
- Footer: multi-column grid collapses to accordion-style expandable sections on mobile; newsletter input remains visible above the accordion

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; mobile browser chrome color for PWA-style experiences is unknown — midnight navy (#272d45) is the logical default
- Exact Figtree weight availability beyond 400/500/600 not confirmed from extraction; 300 (light) and 700 (bold) variants are available in the Figtree typeface but usage on this site is unverified
- Animation and transition values (hover durations, card image zoom behavior, drawer slide timing) not extractable from static hints; 200ms ease transitions assumed throughout
- Icon library source unidentified — oke-widget-icons appears to be the review-platform widget only; the site's own UI icons may use a separate pack or inline SVGs
- Collection-specific accent color usage not confirmed; individual collections may override the amber/terracotta accent scheme with dedicated hues
- Mobile navigation drawer background color and overlay opacity not confirmed from extraction
- Exact sticky header behavior and scroll-trigger threshold not confirmed
- Product card hover interaction (image swap, zoom, pan) not determinable from static extraction
