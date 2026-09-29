---
version: alpha
name: "P. Mauriat"
source_url: "https://www.pmauriatmusic.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, resonant navy (#003388) anchors the P. Mauriat digital presence — not as a background but as the primary voltage for CTAs, navigation bars, and product highlights, evoking the dark lacquer of a professional saxophone bell. The palette is unexpectedly cool and aquatic: a pale cyan (#ccffff) washes over hero sections and hover states like stage light through smoke, while teal (#247390) and steel blue (#0068a0) provide secondary depth. The brand avoids the warm brass-and-amber clichés of wind-instrument marketing, instead leaning into a clean, almost clinical precision with generous white canvas (#fcfbfe) and soft gray surfaces (#e9e6ed, #cfc8d8). Typography runs Open Sans at modest weights — body text at 400, headings at 600 — with Arial and Helvetica as reliable fallbacks, suggesting a pragmatic approach to legibility over typographic flair. Sharp 4px corners (`{rounded.xs}`) on buttons and cards read as precise and engineered, while the full pill radius (`{rounded.full}`) is reserved for search bars and badge indicators, creating a single friendly gesture in an otherwise rectilinear system. The product grid uses shadowless cards with thin hairline borders (#dcdde1), letting instrument photography — rich brass gradients and dark keywork — provide all the visual weight. A distinctive purple accent (#720eec) appears sparingly for sale badges and limited-edition callouts, adding a rare jolt of unexpected color that signals exclusivity.

colors:
  primary: "#003388"
  primary-active: "#002a6e"
  primary-disabled: "#8099c4"
  ink: "#141b38"
  body: "#434960"
  muted: "#767676"
  muted-soft: "#cecece"
  hairline: "#dcdde1"
  hairline-soft: "#e5e5e5"
  canvas: "#fcfbfe"
  surface-soft: "#e9e6ed"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#ccffff"
  accent-teal: "#247390"
  accent-steel: "#0068a0"
  accent-purple: "#720eec"
  accent-gold: "#fa9b57"
  accent-red: "#aa0000"
  accent-green: "#008a20"
  accent-yellow: "#ffba00"
  badge-sale: "#aa0000"
  badge-new: "#008a20"
  badge-limited: "#720eec"
  star-rating: "#ffba00"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.63
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.42
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.31
    letterSpacing: 0.2px
  link:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px

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
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
  button-accent-cyan-active:
    backgroundColor: "#b3ffff"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    height: 36px
    border: "1px solid {colors.primary}"
  icon-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
    rounded: "{rounded.xs}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(20, 27, 56, 0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 16px rgba(20, 27, 56, 0.12)"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(20, 27, 56, 0.08)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  product-card-badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-section-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-overlay:
    backgroundColor: "rgba(0, 51, 136, 0.6)"
    textColor: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
  search-icon:
    textColor: "{colors.muted}"
    height: 20px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-dark:
    backgroundColor: "{colors.muted}"
    height: 1px
  badge-default:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-accent:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  rating-stars:
    textColor: "{colors.star-rating}"
    height: 16px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
  filter-chip-hover:
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in deep navy (#003388) with white text and sharp 4px corners. On hover, the background darkens to `{colors.primary-active}` (#002a6e); the disabled state fades to a muted blue-gray `{colors.primary-disabled}` (#8099c4). Used for "Add to Cart," "Learn More," and primary form submissions. **`button-secondary`** — An outlined variant with a white fill, navy text, and a 2px navy border. Active state shifts the border and text to `{colors.primary-active}` with a soft gray background `{colors.surface-soft}`. **`button-accent-cyan`** — A high-contrast alternative on dark backgrounds, using pale cyan (#ccffff) fill with dark ink text. Hover deepens to `#b3ffff`. **`button-pill-primary`** — A compact, fully rounded version of the primary button, used for "Shop Now" badges and compact CTAs. **`button-pill-outline`** — A 1px outlined pill for secondary compact actions like "Compare" or "Quick View."

### Cards
**`product-card`** — A shadowless card with a 1px soft hairline border and 4px corners, letting instrument photography provide all visual weight. On hover, a subtle box shadow rises and the border strengthens to `{colors.hairline}`. The card contains an image area with 4:3 aspect ratio, a title in `{typography.title-sm}`, a price in `{typography.body-md}`, and optional badges. **`product-card-badge`** — Small pill badges positioned at the top-left of the card image. Three variants exist: red (`{colors.badge-sale}`) for sale items, green (`{colors.badge-new}`) for new arrivals, and purple (`{colors.badge-limited}`) for limited editions. All use uppercase 11px bold type with 0.3px letter spacing.

### Navigation
**`nav-bar`** — A 72px white header with a thin bottom border. On scroll, a subtle shadow replaces the border. Navigation links use 15px semibold type; the active page is underlined with a 2px navy bar. **`nav-dropdown`** — A white dropdown panel with 8px rounded corners and a soft shadow, containing links in `{typography.body-sm}`. Hover states on dropdown items tint the background to `{colors.surface-soft}`.

### Forms
**`text-input`** — A 44px tall input with 4px corners, white fill, and a 1px hairline border. On focus, the border thickens to 2px navy. Error state swaps to a 1px red border (`{colors.accent-red}`). **`select-input`** — Matches the text input dimensions and styling, with a custom dropdown arrow in `{colors.muted}`. **`filter-chip`** — Pill-shaped filter toggles with a 1px hairline border. Active chips fill with navy and white text; hover chips show a navy border outline.

### Hero
**`hero-section`** — A full-width section with navy background and white text, using `{typography.display-xl}`. A cyan variant (`{colors.accent-cyan}`) with dark ink text provides an alternative for landing pages. **`hero-overlay`** — A semi-transparent navy overlay (60% opacity) for hero images, ensuring text legibility against variable photography.

### Footer
**`footer-section`** — A dark navy (`{colors.ink}`) footer with white text and muted gray links. Link hover shifts to full white. Section dividers use `{colors.muted}` at 1px. The footer contains column headings in `{typography.title-sm}` and body links in `{typography.link}`.

### Badges
**`badge-default`** — A soft gray pill for neutral labels like "In Stock" or "Free Shipping." **`badge-primary`** — A navy pill for branded tags. **`badge-accent`** — A purple pill (`{colors.accent-purple}`) for exclusive or premium callouts. All badges use 11px uppercase bold type with 0.3px letter spacing and full pill rounding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to `{typography.display-lg}`; filter chips stack vertically; footer columns stack; search bar reduces height to 40px |
| Tablet | 744–1128px | Two-column product grid; nav links show top-level only; hero padding reduces to 48px; filter chips wrap in a horizontal scroll |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; hero at full padding (64px); filter chips in a horizontal strip |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered with max-width 1200px |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons are 40x40px with 4px corners
- Filter chips are 36px tall with 16px horizontal padding
- Product card tap targets (title, price, badge) are at least 44px tall within the card

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-in drawer from the left
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer columns collapse from 4 columns (desktop) to 2 (tablet) to a single stack (mobile)
- Filter chips collapse from a horizontal strip (desktop) to a vertical accordion (mobile)
- Hero sections reduce padding and font size on mobile, with optional image removal

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary and secondary buttons have confirmed hover colors
- Error styling for forms is inferred from the red accent color (#aa0000); actual error message typography and iconography are unknown
- Dark mode is not present on the live site; no dark palette tokens exist
- Sub-brand or collection-specific palettes (e.g., for "P. Mauriat Signature" vs. "P. Mauriat Classic") could not be determined
- The exact border-radius values for product cards and buttons are inferred from the extracted palette's sharp aesthetic; actual values may vary
- Animation and transition timing (ease curves, durations) are not extractable from static CSS
- The font stack includes WooCommerce as a fallback, suggesting a WooCommerce plugin; actual heading and body font sizes are estimated from typical Open Sans implementations
- Social media icon colors and checkout widget colors (Shopify Pay, Klarna, Afterpay) may be present in the extracted palette but have been excluded from the design system
- The extracted color list is heavily weighted toward blues, grays, and one bright accent (#720eec purple); the true brand primary (#003388) was selected as the most distinctive non-gray color
