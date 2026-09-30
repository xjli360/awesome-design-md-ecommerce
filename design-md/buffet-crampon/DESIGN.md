---
version: alpha
name: "Buffet Crampon"
source_url: "https://www.buffet-crampon.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, resonant charcoal (#32312f) grounds Buffet Crampon's digital presence — not a soft warm gray but a near-black that reads as serious, European, and permanent, the same weight as the African blackwood used in their professional clarinets. Against this ink, a warm parchment canvas (#fcfbf8) carries product imagery and editorial content, while a single amber accent (#f7a674) appears sparingly — on hover states, active navigation markers, and instrument detail callouts — like the glow of a single stage light in an otherwise dark concert hall. The typography runs on futura-pt for headlines and Open Sans for body, a pairing that balances geometric precision with humanist readability; headlines sit tight at 24–32px with generous tracking, echoing the measured spacing of engraved instrument markings. Product cards use soft corners ({rounded.sm}) and thin hairlines (#d1d1d1), letting the photography of polished wood and silver keys command attention. The footer collapses into a dense, monochrome block of links and legal text, while the header stays minimal — a logo lockup, a search icon, and a hamburger menu on mobile — never competing with the instruments themselves. The brand's Japanese-market presence (the page title appears in Japanese) suggests a dual identity: French heritage craftsmanship presented with Japanese editorial restraint. Buttons are tall and narrow, with uppercase labels and no fill until hover, a deliberate withholding that mirrors the discipline of a musician waiting for the downbeat.

colors:
  primary: "#32312f"
  primary-active: "#f7a674"
  primary-disabled: "#d1d1d1"
  ink: "#111111"
  body: "#32312f"
  muted: "#7d7d7d"
  muted-soft: "#aaa69f"
  hairline: "#d1d1d1"
  hairline-soft: "#e9e7e2"
  canvas: "#fcfbf8"
  surface-soft: "#f6f3ef"
  surface-card: "#ffffff"
  on-primary: "#fcfbf8"
  accent-amber: "#f7a674"
  accent-gold: "#f5b668"
  accent-red: "#e02b27"
  accent-green: "#63aa08"
  footer-bg: "#32312f"
  footer-text: "#cdcdcd"

typography:
  display-xl:
    fontFamily: "'futura-pt', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 0.5px
  display-lg:
    fontFamily: "'futura-pt', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  display-md:
    fontFamily: "'futura-pt', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  title-md:
    fontFamily: "'futura-pt', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'futura-pt', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'futura-pt', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'futura-pt', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'futura-pt', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'futura-pt', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary-active}"
    borderBottom: "2px solid {colors.primary-active}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(50,49,47,0.08)"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-overlay:
    backgroundColor: "rgba(50,49,47,0.4)"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.accent-amber}"
  badge-new:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
    height: 40px
  icon-button-hover:
    textColor: "{colors.primary-active}"

## Components

### Buttons
**`button-primary`** — The primary action button, rendered as a solid charcoal (#32312f) rectangle with no border-radius, uppercase futura-pt label, and generous horizontal padding. On hover, the fill shifts to amber (#f7a674) and the text to charcoal, creating a warm glow that signals interactivity without losing the brand's serious tone. The disabled state uses a light gray (#d1d1d1) fill with muted text, visually receding from attention. Height is fixed at 48px for consistent alignment across forms and CTAs.

**`button-secondary`** — An outlined variant with transparent background, charcoal text, and a 1px solid charcoal border. On hover, the fill and text swap — the button becomes solid charcoal with white text — preserving the same 48px height and uppercase typography. Used for secondary actions like "Learn More" or "View Range" alongside primary buttons.

**`icon-button`** — A minimal 40px square with no background and no border, carrying a single icon in charcoal. On hover, the icon color shifts to amber (#f7a674). Used for search, cart, and menu toggles in the navigation bar, where the icon itself is the only affordance.

### Navigation
**`nav-bar`** — A fixed-height 72px bar on a white canvas (#fcfbf8), containing the brand logo lockup on the left and navigation links on the right. Links are set in uppercase futura-pt at 14px with 0.5px letter-spacing. The active link is indicated by a 2px solid amber (#f7a674) bottom border and amber text. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

**`nav-link-active`** — The active state for top-level navigation items, distinguished by amber text color and a thin amber underline. Inactive links remain charcoal (#32312f) with no underline, creating a clear visual hierarchy without relying on font-weight changes.

### Cards
**`product-card`** — A white card with a 4px border-radius and no padding at the container level, allowing product photography to bleed edge-to-edge. The card body contains a title in futura-pt 16px/500 and a price in Open Sans 16px/400, both with 16px horizontal padding. On hover, a subtle box-shadow (0 4px 12px rgba(50,49,47,0.08)) lifts the card slightly. The hairline border (#d1d1d1) separates the card from the surrounding grid.

**`product-card-title`** — The instrument name, set in futura-pt title-sm (16px/500) with 16px horizontal and 4px bottom padding. The type is tight and precise, mirroring the engraved brand mark on the instrument itself.

**`product-card-price`** — The price in Open Sans body-md (16px/400) with 4px top and 16px bottom padding. The weight is deliberately lighter than the title, letting the instrument name lead the eye.

### Forms
**`text-input`** — A simple rectangular input field on a white background with a 1px hairline (#d1d1d1) border and 12px/16px padding. On focus, the border shifts to charcoal (#32312f), providing a clear but understated active state. Height is 48px to match button alignment in forms. No border-radius — consistent with the brand's rectilinear design language.

**`search-bar`** — A 48px-tall input on a soft surface (#f6f3ef) with a 1px hairline border, used in the site's search overlay. The background tint differentiates it from standard text inputs while maintaining the same rectangular form. Typography is Open Sans body-md.

### Badges
**`badge-new`** — A small amber (#f7a674) pill with 2px/8px padding and uppercase futura-pt at 11px. Used to flag new product arrivals or limited editions. The amber against charcoal text creates a warm, attention-grabbing accent that doesn't compete with the primary brand color.

**`badge-sale`** — A red (#e02b27) pill with white text, used sparingly for promotional pricing. The red is the brand's only saturated color outside the amber family, reserved for urgency signals.

### Footer
**`footer-section`** — A dense, full-width block on a charcoal (#32312f) background with light gray (#cdcdcd) text. Links are set in Open Sans 14px/400 with no underline. On hover, links shift to amber (#f7a674). The footer contains multiple columns of links, legal text, and social icons, all set against the dark canvas. Padding is 48px vertical and 24px horizontal.

### Hero
**`hero-section`** — A full-width section on a white canvas with a large futura-pt headline (32px/600) and a dark overlay (rgba(50,49,47,0.4)) over background imagery. The overlay ensures text readability against product photography, which often features high-contrast wood and silver. Section padding is 64px vertical and 24px horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; hero text reduces to 24px; product cards stack single-column; footer links stack vertically; search bar moves to overlay |
| Tablet | 744–1128px | Nav links visible but condensed; product cards in 2-column grid; hero padding reduces to 48px vertical; footer columns reduce to 2 |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero at full 64px padding; footer in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero text scales to 36px |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height
- Icon buttons are 40px with 48px touch area via padding
- Navigation links have 48px tap targets on mobile
- Product card images are tappable with full-card hit area

### Collapsing Strategy
- Navigation links collapse into hamburger menu below 744px
- Product grid reduces columns from 4 to 3 to 2 to 1 as viewport shrinks
- Footer columns collapse from 4 to 2 to 1 below 744px
- Hero text reduces font-size by 25% on mobile
- Search bar transitions from inline to overlay on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs and search bars could not be fully extracted; focus border color is inferred from the brand's primary color
- Error styling (form validation, error messages, error borders) was not present in extracted data
- Dark mode is not supported; the brand uses a light canvas exclusively
- Sub-brand palettes (e.g., Buffet Crampon vs. Besson vs. Antoine Courtois) could not be distinguished
- The extracted font list includes "ES Face" and "The Future Mono" which may be used for specific editorial or technical content but their usage context is unknown
- Social icon colors and checkout-widget colors (Klarna, Afterpay) were filtered from the extracted hex list but may still appear in the live site
- Animation and transition durations, easing curves, and micro-interaction patterns were not extractable
- The brand's icon set (luma-icons, Buffet-Crampon-Theme-Icon) could not be mapped to specific UI contexts
- Print stylesheet and accessibility contrast ratios were not verified against WCAG standards
- The Japanese-language page title suggests a dual-language site, but the design system's localization strategy (typography adjustments for CJK characters, layout changes for longer text) is undocumented
