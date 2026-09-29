---
version: alpha
name: "Phlur"
source_url: "https://phlur.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A modern fine fragrance house that speaks in whispers and punctuates with pigment. Phlur's digital presence is a study in restrained sensuality — a mostly-white canvas (`#fefefe`) overlaid with a muted gray palette (`#666666`, `#888888`, `#999999`, `#aaaaaa`, `#b0b0b0`, `#b6b6b6`, `#bdbdbd`, `#dedede`, `#e5e5e5`, `#e6e6e6`) that never shouts. The brand's emotional voltage comes from a constellation of accent colors: a deep indigo (`#272d45`) and a brighter navy (`#2e3192`, `#334fb4`) that anchor navigation and key typography, a warm amber (`#ffcf2a`) that appears in badges and highlights, and a series of unexpected pastel-magenta (`#df6980`), teal (`#0e7a82`, `#0881b0`), and violet (`#a45cec`) swatches that feel like the color of a scent memory. Typography is built on ABCRepro-Regular — a clean, slightly condensed grotesque — with ABCReproMono-Medium for accent moments and Figtree as a secondary sans. The brand uses generous whitespace (`{spacing.section}`) and soft corners (`{rounded.sm}` on cards, `{rounded.md}` on buttons) to create a tactile, almost haptic feel. There is no aggressive gradient or heavy shadow; instead, Phlur relies on thin hairlines (`{colors.hairline}`: `#e5e5e5`) and subtle surface differentiation (`{colors.surface-soft}`: `#f4f4f6`, `{colors.surface-card}`: `#fafafa`) to create hierarchy. The overall effect is that of a perfume counter in a minimalist gallery — quiet, deliberate, and utterly confident in its own restraint.

colors:
  primary: "#272d45"
  primary-active: "#1a1f30"
  primary-disabled: "#b6b6b6"
  ink: "#121212"
  body: "#666666"
  muted: "#888888"
  muted-soft: "#999999"
  hairline: "#e5e5e5"
  hairline-soft: "#e6e6e6"
  canvas: "#fefefe"
  surface-soft: "#f4f4f6"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-amber: "#ffcf2a"
  accent-indigo: "#2e3192"
  accent-navy: "#334fb4"
  accent-teal: "#0e7a82"
  accent-teal-light: "#0881b0"
  accent-magenta: "#df6980"
  accent-violet: "#a45cec"
  accent-red: "#812424"
  star-rating: "#ffcf2a"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'ABCRepro-Regular', aktiv-grotesk, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'ABCRepro-Regular', aktiv-grotesk, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'ABCRepro-Regular', aktiv-grotesk, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'ABCRepro-Regular', aktiv-grotesk, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'ABCRepro-Regular', aktiv-grotesk, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'ABCRepro-Regular', aktiv-grotesk, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', aktiv-grotesk, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', aktiv-grotesk, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', aktiv-grotesk, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'ABCRepro-Regular', aktiv-grotesk, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'ABCRepro-Regular', aktiv-grotesk, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Figtree', aktiv-grotesk, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'ABCRepro-Regular', aktiv-grotesk, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'ABCReproMono-Medium', 'Courier New', monospace"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  mono-accent:
    fontFamily: "'ABCReproMono-Medium', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

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
    rounded: "{rounded.md}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    padding: 0
  button-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 32px
    height: 48px
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
    border: "1px solid {colors.accent-red}"
  text-input-placeholder:
    textColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.body}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "3/4"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "14px 32px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
  search-icon:
    textColor: "{colors.muted}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    textColor: "{colors.body}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    textTransform: uppercase
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-panel:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  color-swatch-selected:
    border: "2px solid {colors.primary}"
  star-rating:
    textColor: "{colors.star-rating}"
    fontSize: "14px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 48px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    padding: "0 12px"
  drawer-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  drawer-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the Phlur site. Rendered in the signature deep indigo (`{colors.primary}`) with white text and an 8px rounded corner (`{rounded.md}`). Uses uppercase ABCRepro-Regular at 14px with 0.5px letter-spacing. On hover, shifts to `{colors.primary-active}` (#1a1f30). Disabled state uses `{colors.primary-disabled}` (#b6b6b6). Height is 48px with 14px/32px padding.

**`button-secondary`** — An outlined variant with a transparent background, indigo text, and a 1px solid border matching the primary color. Same typography and height as primary. Active state fills with `{colors.surface-soft}` (#f4f4f6) and darkens the border to `{colors.primary-active}`.

**`button-tertiary-text`** — A text-only button with no background or border. Uses `{colors.body}` (#666666) for text, matching the uppercase button typography. Intended for secondary actions like "Cancel" or "Learn More" in drawers and modals.

**`button-amber`** — A warm accent button using `{colors.accent-amber}` (#ffcf2a) as background with dark ink text. Used sparingly for promotional CTAs, limited-edition drops, or sale badges. Same dimensions as `button-primary`.

### Cards
**`product-card`** — The primary product display unit. A white card (`{colors.canvas}`) with a 4px rounded corner (`{rounded.sm}`). The image area occupies a 3:4 aspect ratio with the top corners rounded. Title uses `{typography.title-sm}` in ink, price uses `{typography.body-sm}` in body gray. An optional amber badge (`{colors.accent-amber}`) can overlay the image for "New" or "Limited Edition" labels.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height with a white background and a subtle bottom border (`{colors.hairline-soft}`). Navigation links use uppercase ABCRepro-Regular at 13px with 0.5px letter-spacing. Active links are colored in the primary indigo with a 2px bottom border. Inactive links are body gray.

### Forms
**`text-input`** — Standard input field with a white background, 4px rounded corners, and a 1px hairline border. On focus, the border switches to primary indigo. Error state uses `{colors.accent-red}` (#812424). Placeholder text is `{colors.muted-soft}` (#999999). Height is 48px with 12px/16px padding.

### Search
**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a soft surface background (`{colors.surface-soft}`). Uses body typography and a muted search icon. Height is 48px with 12px/20px padding. Designed to appear in the nav bar or as a full-width hero element.

### Footer
**`footer-section`** — A full-width footer with a soft surface background (`{colors.surface-soft}`). Links use `{typography.link}` in body gray. Section headings are uppercase title-sm in ink. Padding uses the section spacing token for generous vertical rhythm.

### Drawer
**`drawer-panel`** — A slide-in panel from the right side of the viewport, used for cart, mobile nav, and filters. White background with 24px padding. Overlaid by a 50% opacity scrim (`{colors.scrim}` at 0.5).

### Accordion
**`accordion-trigger`** — A full-width clickable row with a bottom hairline border. Uses title-sm typography in ink. The panel below uses body-sm in body gray with zero top padding and base bottom padding. Used extensively on product detail pages for notes, ingredients, and shipping info.

### Badges
**`product-card-badge`** — A small, uppercase monospace badge (`{typography.badge}`) on an amber background (`{colors.accent-amber}`) with dark ink text. 4px rounded corners with 4px/8px padding. Used for "NEW", "LIMITED", or "BESTSELLER" labels.

### Color Swatches
**`color-swatch`** — A 32px circular swatch (`{rounded.full}`) used in product variant selectors. Selected state shows a 2px primary indigo border. The swatch colors themselves are drawn from the brand's accent palette: teal, magenta, violet, amber, and navy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, nav collapses to hamburger drawer, product cards stack vertically, hero text reduces to display-md, search bar moves to drawer, footer links stack |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but reduced spacing, hero uses display-lg, search bar appears in nav, footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, hero uses display-xl, search bar prominent in nav, footer uses 3-column layout |
| Wide | > 1440px | Max-width container at 1440px, centered content, four-column product grid, expanded hero with larger imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons and swatches are at least 32px with 44px tap area via padding
- Accordion triggers are full-width with 48px minimum tap height
- Nav links have 44px tap height with adequate spacing

### Collapsing Strategy
- Primary navigation collapses to a hamburger icon at < 744px, revealing a full-height drawer panel
- Product filters collapse to a "Filter" button that opens a drawer on mobile and tablet
- Footer link columns collapse to accordion sections on mobile
- Search bar collapses to an icon on mobile, expanding to full-width on tap
- Product image galleries collapse from thumbnail strip to dot indicators on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components (beyond primary button) could not be reliably extracted
- Error and success styling for form validation (colors, icons, messages) is inferred but not confirmed
- Dark mode palette is entirely absent from the extracted data
- Sub-brand or collection-specific color palettes (e.g., limited edition drops) may exist but were not captured
- Animation durations, easing curves, and transition properties are not available
- Specific font weights beyond 400 and 500 are inferred; exact weight values may vary
- Dropdown and select menu styling (native vs custom) is unknown
- Modal and dialog component details (sizing, close button placement, animation) are not confirmed
- Loading states (skeleton screens, spinners) are not documented
- The `oke-widget-icons` font-family suggests Okendo review widgets are used, but their specific styling tokens are not extracted
- `aktiv-grotesk-extended` may be used for specific headings or hero text, but its usage context is unclear
- `object-fit: cover` appears in CSS but its specific component mapping is unknown
