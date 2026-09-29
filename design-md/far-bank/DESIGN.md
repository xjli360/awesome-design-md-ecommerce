---
version: alpha
name: "Far Bank"
source_url: "https://farbank.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep-navy (#001d40) and near-black (#1a1919) palette that feels less like outdoor gear and more like a fly-fishing library at dusk — the brand trusts darkness as its canvas, not white. The primary voltage comes from a cool steel-blue (#789fbb), used sparingly on CTAs and accent lines, while a brighter cobalt (#334fb4) appears as a secondary jolt on select links and badges. Typography is a layered system of display faces — ff-good-headline-web-pro-con for condensed hero headlines, bagatela for serif elegance on editorial spreads, and Assistant for clean body copy — creating a hybrid of sporting-club heritage and modern utility. Corners are mostly soft but never pill-shaped; cards use {rounded.md} (12px) and buttons use {rounded.sm} (8px), with the occasional full-radius on small badge elements. The nav bar sits at 80px tall, transparent on hero imagery, then snaps to a solid {colors.ink} scrim on scroll. Product photography is moody and low-contrast, with fly rods and reels shot against dark surfaces, making the silver hardware and bright fly line the only highlights. The search bar is a dark field with a subtle {colors.hairline} border, not a glowing orb. This is a brand that says "we are serious about the craft" through restraint — no bright oranges, no hero gradients, no playful illustrations. Every component feels engineered for a customer who values precision over flash.

colors:
  primary: "#789fbb"
  primary-active: "#5a8aa8"
  primary-disabled: "#b3c9d9"
  ink: "#1a1919"
  body: "#242833"
  muted: "#7a99ac"
  muted-soft: "#c7c7c7"
  hairline: "#dedede"
  hairline-soft: "#f3f3f3"
  canvas: "#f8f8f8"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  navy: "#001d40"
  accent-blue: "#334fb4"
  dark-surface: "#121212"

typography:
  display-xl:
    fontFamily: "'ff-good-headline-web-pro-con', 'Trade Gothic Next', 'Montserrat', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ff-good-headline-web-pro', 'Trade Gothic Next', 'Montserrat', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 0
  display-md:
    fontFamily: "'bagatela', 'Roboto Slab', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'ff-good-headline-web-pro-con', 'Trade Gothic Next', 'Montserrat', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-sm:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0
  nav-link:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Assistant', 'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.20
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
    padding: 12px 24px
    height: 44px
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
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-dark-active:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
  button-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid #c13515"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 80px
  nav-bar-transparent:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 80px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "0 0 16px 0"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "8px 16px 0"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "4px 16px"
  badge:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  search-bar:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    height: 600px
  hero-overlay:
    backgroundColor: "rgba(26, 25, 25, 0.4)"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-dark:
    backgroundColor: "{colors.muted}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered on {colors.primary} (#789fbb) background with white text and 8px rounded corners. On hover, shifts to {colors.primary-active} (#5a8aa8); disabled state uses {colors.primary-disabled} (#b3c9d9). Uppercase 14px type at weight 600, 0.5px letter-spacing. Used for "Add to Cart", "Shop Now", and primary form submissions.

**`button-secondary`** — Outlined variant on white canvas with a 1px {colors.hairline} border. Active state fills {colors.surface-soft} and darkens the border to {colors.muted}. Same typography and sizing as primary. Used for "Learn More", "View Details", and secondary checkout actions.

**`button-dark`** — Solid {colors.ink} (#1a1919) background for use on light surfaces or inside product cards. Hover shifts to {colors.navy} (#001d40). Same sizing and typography as primary. Used for "Quick Add" and "Subscribe" CTAs in content-heavy areas.

**`button-text`** — Ghost button with no background or border, using {colors.body} text. Hover changes text to {colors.primary}. Used for "Cancel", "Back", and tertiary navigation within modals and drawers.

### Navigation
**`nav-bar`** — Fixed 80px dark bar with {colors.ink} background, white uppercase nav links at 14px/600. Logo sits left, primary links center, utility icons (search, account, cart) right. On hero sections, the bar becomes transparent (`nav-bar-transparent`) with a white text overlay, gaining a dark scrim on scroll.

**`nav-link`** — Inline navigation item with 8px horizontal padding. Active state highlights text in {colors.primary}. No underline or background fill — the color shift alone signals current section.

### Cards
**`product-card`** — White card with 12px rounded corners, no border, subtle shadow. Image fills the top with matching top-radius rounding. Title uses {typography.title-sm} (16px/600), price uses {typography.body-md} (16px/400) in {colors.body}. Padding of 16px on sides and bottom. Hover state lifts the card 4px with a deeper shadow.

**`hero-section`** — Full-width 600px tall container on {colors.ink} background. Content is centered with {typography.display-xl} headline, optional subtitle in {typography.body-md}, and a single `button-primary`. A semi-transparent overlay (`hero-overlay`) sits between background image and text for readability.

### Badges
**`badge`** — Small pill-shaped label on {colors.navy} (#001d40) background with white uppercase 11px type. Used for "New", "Limited Edition", and category tags. Full border-radius, 4px vertical / 10px horizontal padding.

**`badge-sale`** — Same shape and typography as `badge`, but on {colors.accent-blue} (#334fb4) background. Used for "Sale", "Clearance", and promotional markers.

### Forms
**`text-input`** — Standard 48px input field on {colors.canvas} background with 1px {colors.hairline} border and 8px rounded corners. Focus state shifts border to {colors.primary}. Error state uses a red border (#c13515) with red error text below. Placeholder text in {colors.muted-soft}.

**`search-bar`** — Dark variant of text-input on {colors.dark-surface} (#121212) background, used in the nav and on dark hero sections. White text, 1px {colors.hairline} border. Focus shifts border to {colors.primary}.

### Footer
**`footer`** — Full-width dark section on {colors.ink} with 64px vertical padding. Links in {colors.muted} (#7a99ac) at 14px/500, hover to white. Column layout with newsletter signup, brand story links, and legal text. A `divider-dark` (1px {colors.muted}) separates content rows.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; hero height reduces to 400px; product cards stack vertically; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero at 500px; search bar moves to nav overlay |
| Desktop | 1128–1440px | Full nav with all links; three-column product grid; hero at 600px; search bar inline in nav |
| Wide | > 1440px | Max-width container at 1440px; content centered; hero may extend full-width with parallax |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility
- Nav links have 48px touch area (8px padding on 14px text)
- Search bar and text inputs are 48px tall for comfortable tapping
- Product card CTAs are 44px minimum
- Badge pills are 28px tall — acceptable for decorative labels but not primary interactions

### Collapsing Strategy
- Primary nav links collapse into hamburger menu below 744px; utility icons (search, cart, account) remain visible
- Product grid shifts from 3-column to 2-column at tablet, single-column at mobile
- Hero headline reduces from 48px to 32px on mobile; subtitle may be hidden
- Footer columns collapse from 4 to 2 at tablet, single column at mobile
- Search bar becomes a full-width overlay on mobile, triggered by icon tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are dominated by dark neutrals (#1a1919, #001d40, #121212) and muted blues (#789fbb, #7a99ac, #c7c7c7) — the palette appears intentionally restrained, but the extracted list may miss secondary accent colors used sparingly (e.g., a warm leather-brown or olive-green that appears in product photography). The bright #334fb4 is the only non-neutral accent and is used as a secondary brand color here, but its actual usage frequency on the live site is unconfirmed.
- Font-family declarations include many faces (bagatela, ff-good-headline-web-pro-con, bebas-neue-pro-expanded, program-narrow) that may be used for specific editorial or marketing sections rather than system-wide. The primary body and UI faces (Assistant, Open Sans) are more reliably extracted.
- Hover, focus, and active states for all components are inferred from common patterns — exact extracted values for `button-primary-active`, `text-input-focus`, and `nav-link-active` are not confirmed from the live site.
- Error, success, and warning color tokens are absent from extraction — red (#c13515) is assumed for errors based on convention.
- Dark mode is not detected; the brand's heavy use of dark backgrounds may mean "dark mode" is the default experience rather than a separate theme.
- Sub-brand or collection-specific palettes (e.g., fly rods vs. apparel vs. accessories) are not captured.
- Typography scale for mobile (reduced sizes, adjusted line heights) is not extracted — desktop values are used as defaults.
- Shadow values (card elevation, nav scrim, modal overlays) are not extracted — only color and opacity are noted.
- The `hero-overlay` opacity (0.4) is an estimate based on common practice, not extracted from the live site.
