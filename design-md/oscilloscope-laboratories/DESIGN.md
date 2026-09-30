---
version: alpha
name: "Oscilloscope Laboratories"
source_url: "https://www.oscilloscope.net"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A film distributor that treats its website like a repertory cinema lobby — warm amber light (#ffcc33) spilling across a charcoal wall (#1e1f26), with ticket-stub buttons and a marquee grid of poster art. The brand’s signature yellow (#ffcc33) appears on every primary CTA, navigation highlight, and badge, while a secondary palette of electric cyan (#1ea0c3), hot pink (#e94c89), and mint (#02e49b) signals genre diversity across the catalog. The site runs Montserrat at modest weights — display headlines at 500/600 rather than heavy 700+, letting the film stills and poster art carry the emotional weight. Navigation is a persistent top bar with dropdown menus, a search icon, and a shopping cart badge, all contained within a clean white canvas (#ffffff) that frames the yellow accents. The home page features a hero carousel of featured films, a grid of "Now Playing" titles, and a "Coming Soon" section — each film card a simple poster thumbnail with title, year, and director credit. The overall feel is that of a curated microcinema: generous whitespace, minimal UI chrome, and color used sparingly but with purpose.

colors:
  primary: "#ffcc33"
  primary-active: "#ebae31"
  primary-disabled: "#f0d080"
  ink: "#1e1f26"
  body: "#32373c"
  muted: "#949494"
  muted-soft: "#eeeeee"
  hairline: "#dddddd"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#1e1f26"
  accent-cyan: "#1ea0c3"
  accent-pink: "#e94c89"
  accent-mint: "#02e49b"
  accent-orange: "#ff9900"
  accent-red: "#ea4434"
  social-facebook: "#1778f2"
  social-twitter: "#1da1f2"
  social-instagram: "#e65678"
  social-youtube: "#ff0000"
  star-rating: "#ffcc33"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  meta:
    fontFamily: "'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: 2px solid "{colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
  text-input-error:
    border: 2px solid "{colors.accent-red}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid "{colors.hairline-soft}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  nav-dropdown-item:
    padding: 8px 24px
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  nav-dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  search-icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 40px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  hero-carousel:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    height: 480px
  hero-carousel-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.4
  hero-carousel-content:
    padding: "{spacing.xl}"
  film-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  film-card-poster:
    rounded: "{rounded.none}"
    aspectRatio: 2/3
  film-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  film-card-meta:
    typography: "{typography.meta}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  film-card-hover:
    boxShadow: 0 4px 12px rgba(0,0,0,0.15)
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  badge-new:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-coming-soon:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.primary}"
  social-icon:
    height: 24px
    textColor: "{colors.muted-soft}"
  social-icon-hover:
    textColor: "{colors.primary}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The brand's signature yellow (#ffcc33) button used for primary actions like "Buy Now", "Add to Cart", and "Subscribe". Text is uppercase Montserrat 600 at 14px, set against dark ink (#1e1f26) for strong contrast. On hover, the background shifts to a deeper amber (#ebae31). The disabled state uses a pale yellow (#f0d080) with muted text to signal inactivity.

**`button-secondary`** — An outlined variant with a 2px ink (#1e1f26) border on a white canvas. Used for secondary actions like "Learn More" or "View Trailer". On hover, the button inverts to a solid ink fill with white text. This creates a clear visual hierarchy alongside the primary button.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "Close". On hover, a soft gray (#f7f7f7) background appears to indicate interactivity. All buttons share the same uppercase Montserrat 600 typography and 8px border radius.

**`button-pill`** — A compact, fully rounded variant used for filters, tags, and quick actions. Uses the same yellow primary but at a smaller 12px uppercase weight. The pill shape (`{rounded.full}`) distinguishes it from standard rectangular buttons, suggesting a more casual or filter-like interaction.

### Navigation
**`nav-bar`** — A fixed 72px header with white background and a subtle bottom border. Navigation links are uppercase Montserrat 600 at 14px, with the brand's yellow used for the active state or hover underline. The bar contains left-aligned logo, center-aligned nav links (Films, Shop, About, News), and right-aligned search icon and cart badge.

**`nav-dropdown`** — Appears on hover of nav links that have subcategories. A white panel with 8px border radius, containing text links at body-sm weight. Items have 8px vertical padding and 24px horizontal padding. On hover, items get a soft gray background.

**`search-icon-button`** — A simple icon button with no background, used to toggle the search overlay. The icon is a standard magnifying glass in ink (#1e1f26). On mobile, this may expand into a full-width search input.

**`cart-badge`** — A small yellow circle with uppercase badge typography, positioned on the cart icon. Shows the number of items in the cart. The badge uses `{rounded.full}` for a circular shape, with a minimum width of 20px to accommodate double-digit counts.

### Cards
**`film-card`** — The core content unit for displaying films. A simple white card containing a poster image (2:3 aspect ratio), title, year, and director. No border radius — the poster sits flush against the card edge, creating a clean, gallery-like presentation. On hover, a subtle box shadow lifts the card. The title uses title-sm Montserrat 600, while metadata uses 12px regular weight in muted gray.

**`hero-carousel`** — A full-width featured section at the top of the home page, 480px tall with a dark background (#1e1f26). Film posters and text overlay sit on a semi-transparent black scrim (40% opacity). Content is padded at 32px. Navigation arrows (left/right) and dot indicators appear at the bottom.

### Forms
**`text-input`** — Standard text input with a 1px hairline border, 8px border radius, and 12px padding. On focus, the border becomes 2px solid yellow (#ffcc33). Error states use a 2px red (#ea4434) border. The input height is 48px for comfortable touch targeting.

**`select-input`** — Dropdown select styled consistently with text inputs — same height, padding, border, and border radius. The dropdown arrow is a custom chevron in ink color.

### Footer
**`footer`** — A dark section (#1e1f26) with light gray text (#eeeeee). Contains columns for navigation links, social media icons, and legal text. Links are 14px Montserrat 500, turning yellow on hover. Social icons are 24px and also turn yellow on hover. The footer uses section-level padding (64px top/bottom) with 24px horizontal padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger menu; hero carousel reduces to 320px height; film cards stack vertically; search becomes full-width input; footer columns stack |
| Tablet | 744–1128px | Two-column film grid; nav links remain visible but condensed; hero carousel at 400px; footer in 2-column layout |
| Desktop | 1128–1440px | Three-column film grid; full nav bar; hero carousel at 480px; footer in 4-column layout |
| Wide | > 1440px | Four-column film grid; max-width container at 1440px; hero carousel may expand to full viewport height |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Nav dropdowns have 48px tap targets on mobile
- Film cards have full-surface tap targets (no empty click zones)
- Social icons maintain 44x44px touch area even if icon is smaller

### Collapsing Strategy
- Top navigation collapses to a hamburger menu at < 744px
- Film grid collapses from 4 columns → 3 → 2 → 1 as viewport shrinks
- Footer columns collapse from 4 → 2 → 1
- Hero carousel content reduces padding and font sizes on mobile
- Search icon expands to full-width input on mobile
- Dropdown menus become accordion-style expandable sections on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components were inferred from common patterns — actual extracted hover colors may differ
- Error and validation styling (error messages, success states, loading spinners) not observed on live site
- Dark mode not implemented — all observations are light mode only
- Font sizes and line heights are estimated based on Montserrat's typical usage — exact values may vary
- The extracted color list includes many social media brand colors (#1778f2, #e65678, etc.) that are likely from share buttons, not the brand's own palette
- Several blues (#0693e3, #0757fe, #4280ff) may be from embedded widgets or checkout integrations rather than brand colors
- Animation and transition timing values not extracted
- Focus ring styles (keyboard accessibility) not observed
- Print stylesheet behavior unknown
- The brand's actual primary yellow (#ffcc33) was confirmed through multiple page elements, but secondary accent usage (cyan, pink, mint) is inferred from the extracted palette and may not be systematic
