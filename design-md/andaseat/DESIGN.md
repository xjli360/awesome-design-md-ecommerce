---
version: alpha
name: "AndaSeat"
source_url: "https://www.andaseat.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A gaming throne brand that wraps its audience in a high-contrast visual system built on a deep ink canvas (#222222) and a sharp, unmistakable primary blue (#4388e8) that feels pulled from a neon-lit esports arena. The palette is deliberately aggressive — a secondary orange (#ff4200) and a hot pink (#e81e63) appear in badge work and accent details, while the body text runs on a near-black (#18191b) against a clean white (#ffffff) background, creating the kind of crisp legibility you need when scanning specs mid-match. Typography leans on Hind and Montserrat — both geometric sans-serifs with tight apertures and a mechanical precision that mirrors the brand's product language of adjustable armrests, lumbar support systems, and cold-rolled steel frames. Buttons carry the full weight of the primary blue with a {rounded.sm} corner that softens the industrial edge just enough to feel premium rather than hostile. Product cards use a subtle surface-soft (#f5f5f5) to lift the chair photography, while the footer collapses into a dense grid of muted (#878787) links on a dark surface (#111111). The brand's signature move is the orange-and-blue voltage: a CTA in #4388e8 next to a sale badge in #ff4200 creates the kind of competitive tension that says "buy now, this deal won't last." There is no hesitation in this system — every color choice is a call to action, every corner radius a concession to comfort in a category that could easily feel cold.

colors:
  primary: "#4388e8"
  primary-active: "#2b6fd4"
  primary-disabled: "#a0c4f0"
  ink: "#222222"
  body: "#18191b"
  muted: "#878787"
  muted-soft: "#a0a0a0"
  hairline: "#dedede"
  hairline-soft: "#eaeaea"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#ff4200"
  accent-pink: "#e81e63"
  accent-gold: "#e6c273"
  accent-green: "#87ae2e"
  accent-red: "#ec0101"
  accent-teal: "#56cfe1"
  dark-surface: "#111111"
  dark-muted: "#383838"
  sale-badge: "#ff4d00"
  error: "#cc2d2d"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Hind', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Hind', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Montserrat', 'Hind', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Hind', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Hind', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Hind', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Hind', 'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Hind', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Hind', 'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Hind', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Hind', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Hind', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Hind', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Montserrat', 'Hind', sans-serif"
    fontSize: 11px
    fontWeight: 700
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
    padding: 12px 28px
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
    padding: 11px 27px
    height: 44px
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-orange}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  feature-badge:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-section:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's distinctive blue (#4388e8) with white uppercase Montserrat text. On hover, it shifts to a deeper active state (#2b6fd4). The disabled state uses a pale blue (#a0c4f0) to signal non-interactivity while maintaining brand continuity. All primary buttons use a {rounded.sm} corner that balances the aggressive typography with a touch of approachability.

**`button-secondary`** — An outlined variant on a white background with ink (#222222) text. The border matches the ink color at 1px weight. Hover fills the background with a 10% opacity ink overlay. Used for "Learn More" and "Compare" actions where the primary blue would overwhelm the layout.

**`button-accent-orange`** — The urgency variant, using the brand's orange (#ff4200) for limited-time offers, flash sales, and "Shop Now" CTAs on product cards. Same sizing and typography as button-primary, but the orange creates a secondary voltage that competes with the blue for attention.

### Cards
**`product-card`** — A white card with a {rounded.sm} corner and a subtle shadow (0px 2px 8px rgba(0,0,0,0.08)). The product image fills the top with its own {rounded.sm} crop. Below, the title uses title-sm weight 500, while the price appears in body-md with the accent-orange color to draw the eye. A sale-badge or feature-badge overlays the top-left corner of the image.

**`sale-badge`** — A small, sharp badge in the brand's sale orange (#ff4d00) with white uppercase text. Positioned absolutely over the product image at a 4px offset from the top-left edge. The {rounded.xs} corner keeps it tight and urgent.

**`feature-badge`** — A hot pink (#e81e63) badge used for "New Arrival," "Limited Edition," or "Pro Series" labels. Same dimensions as sale-badge but signals exclusivity rather than discount.

### Navigation
**`nav-bar`** — A fixed top navigation at 72px height on a white canvas. Logo sits left-aligned, with a centered or right-aligned link strip using uppercase Montserrat nav-link tokens. On scroll, a 1px hairline (#dedede) bottom border appears. Mobile collapses into a hamburger menu with a full-screen overlay.

**`search-bar`** — A pill-shaped input on a light gray surface (#f5f5f5) with muted placeholder text. The {rounded.full} radius contrasts with the system's otherwise angular {rounded.sm} buttons, making the search feel more conversational and exploratory.

### Footer
**`footer-section`** — A dark (#111111) full-width band containing a multi-column grid of links, social icons, and legal text. Links use muted (#878787) color at link weight, with a hover state that shifts to white. The section padding uses {spacing.section} (64px) top and bottom.

**`footer-link`** — Inline text links in the footer. No underline by default; on hover, a 1px bottom border appears in white. The muted color keeps the footer from competing with the main content while remaining legible on the dark surface.

### Hero
**`hero-section`** — A full-viewport-height section on the ink (#222222) background, with white display-xl text. The hero typically features a large product shot (chair in a gaming setup) with a gradient overlay. A single primary button sits below the headline. The section uses {spacing.section} padding on all sides.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, hero text reduces to display-lg, buttons full-width |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, hero maintains two-column layout |
| Desktop | 1128–1440px | Three-column product grid, full nav bar, hero uses display-xl with side-by-side text and image |
| Wide | > 1440px | Max-width container at 1440px, centered content, product grid expands to four columns |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height
- Nav links have a 48px tap area (padding extends beyond text)
- Product card CTAs are at least 48px tall on mobile
- Search bar maintains 44px height across all breakpoints

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Product grid shifts from 4-column to 3-column to 2-column to 1-column as viewport shrinks
- Footer grid collapses from 4 columns to 2 columns at tablet, then single column at mobile
- Hero section stacks vertically below 744px (image below text)
- Secondary navigation (category filters) collapses into a dropdown select on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs and links were not reliably extracted from the live site; assumed standard 10% opacity overlay for secondary buttons and underline for links
- Error state styling for form validation (border color, error message typography) was not observed
- Dark mode palette is not defined; the brand uses a dark footer but no system-wide dark mode was detected
- Sub-brand or collection-specific color variations (e.g., "Kaiser" series vs "Dark Knight" series) may use different accent colors not captured in the global palette
- Animation and transition timing values (ease curves, duration) were not extracted
- Dropdown menu styling (mega menu, account menu) was not observed on the live site
- The extracted hex list includes several reds (#ec0101, #cc2d2d, #eb2226, #a30003, #b93434, #d47d7d) that may be checkout-widget or social-icon colors rather than brand palette — the primary red (#ec0101) was kept as error, but the full set may need review
- Font weights beyond 400, 500, 600, 700 were not confirmed for all typefaces (Hind may have 300 weight available)
- Letter-spacing values for body text and captions were inferred from common gaming-brand patterns rather than extracted
