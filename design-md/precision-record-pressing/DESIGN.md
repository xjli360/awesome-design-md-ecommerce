---
version: alpha
name: "Precision Record Pressing"
source_url: "https://www.precisionpressing.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A vinyl pressing plant that wears its industrial confidence in a coral-red primary (#f16365) — a color that reads more like a hot-stamped label than a corporate brand mark, and that appears against a deep navy ink (#0d3042) that evokes the dark of a record sleeve. The palette is deliberately un-soft: alongside the coral come a burnt orange (#fe8335), a near-black (#04030c), and a muted clay (#a06755), suggesting a system built for a tactile, analog audience rather than a polished digital one. Buttons carry the coral fill with white text, while secondary actions drop into outline or ghost states against the dark canvas. Typography is absent from extracted hints, but the brand’s voice — “Vinyl Pressing Without Limits” — suggests a bold, condensed sans-serif for display work and a clean, readable sans for body copy. The site uses generous spacing (section-level padding at 64px) and soft but present rounded corners on cards and buttons ({rounded.sm} to {rounded.md}), balancing the heavy ink with breathing room. The overall effect is a factory floor translated into a digital storefront: honest, loud where it needs to be, and built around the physical object of the record.

colors:
  primary: "#f16365"
  primary-active: "#ea3427"
  primary-disabled: "#fab185"
  ink: "#0d3042"
  body: "#144862"
  muted: "#767986"
  muted-soft: "#b8bac6"
  hairline: "#d6c9b2"
  hairline-soft: "#faf9fe"
  canvas: "#faf9fe"
  surface-soft: "#d7abc8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#fe8335"
  accent-deep-orange: "#fa841a"
  accent-purple: "#4433cc"
  accent-maroon: "#5b1a10"
  accent-olive: "#3a4725"
  accent-yellow: "#fbfb6d"
  accent-clay: "#a06755"
  accent-brown: "#4d372f"
  accent-tan: "#d6c9b2"
  accent-rose: "#d7abc8"
  accent-sienna: "#9d6459"
  accent-umber: "#6a3512"
  accent-navy: "#144862"
  accent-charcoal: "#3e414a"
  accent-jet: "#04030c"
  accent-ivory: "#faf9fe"
  accent-stone: "#b8bac6"
  accent-slate: "#767986"
  accent-rust: "#f16366"
  accent-tangerine: "#fe973c"
  accent-black: "#000001"

typography:
  display-xl:
    fontFamily: "'Industry', 'Arial Black', 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Industry', 'Arial Black', 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Industry', 'Arial Black', 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Helvetica Neue', 'Arial', sans-serif"
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
  lg: 16px
  xl: 24px
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
    padding: 14px 28px
    height: 48px
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
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 28px
    height: 48px
  button-tertiary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-orange-active:
    backgroundColor: "{colors.accent-deep-orange}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.primary-active}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(4, 3, 12, 0.1)"
    border: "1px solid {colors.primary}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 700
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-section-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
  badge-limited:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
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
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.title-md}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.base}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.lg} 0"
  divider-strong:
    backgroundColor: "{colors.ink}"
    height: 2px
    margin: "{spacing.lg} 0"
  icon-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-circle-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  step-indicator:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  step-indicator-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  step-indicator-complete:
    backgroundColor: "{colors.accent-olive}"
    textColor: "{colors.on-primary}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  modal-overlay:
    backgroundColor: "rgba(4, 3, 12, 0.6)"
  modal-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with coral-red (#f16365) and white text. On hover, it deepens to a darker red (#ea3427); disabled state fades to a soft peach (#fab185). Used for "Order Now", "Get a Quote", and "Add to Cart" actions. The 8px rounded corners ({rounded.sm}) keep the button feeling approachable but not pill-soft — a deliberate midpoint between industrial and friendly.
**`button-secondary`** — An outlined variant with a 2px solid ink (#0d3042) border on a white canvas. On hover, the fill swaps to ink and text inverts to white. Used for "Learn More" and "View Details" actions where the primary button is already present.
**`button-tertiary`** — A text-only ghost button in coral-red. On hover, a soft rose (#d7abc8) background appears behind the text. Used for "Cancel" or "Skip" actions in forms and modals.
**`button-accent-orange`** — A secondary accent button in burnt orange (#fe8335), used sparingly for "Sale" or "Limited Edition" CTAs. On hover, it shifts to a deeper orange (#fa841a).

### Cards
**`product-card`** — A white card with a 1px soft hairline border (#faf9fe) and 12px rounded corners ({rounded.md}). On hover, a subtle box shadow appears and the border shifts to coral-red (#f16365). The card contains a square image slot ({rounded.sm}), a title in 18px semibold, and a price in coral-red bold. Used for vinyl records, bundles, and accessories.
**`hero-section`** — A full-width banner with a deep navy (#0d3042) background and white text. Display type runs at 48px heavy weight. An accent variant swaps the background to coral-red (#f16365). Used for homepage hero, category headers, and promotional banners.

### Navigation
**`nav-bar`** — A white 72px bar with a 1px hairline bottom border. Navigation links are 15px uppercase semibold in ink (#0d3042), with the active state switching to coral-red (#f16365). The bar collapses to a hamburger menu on mobile. A sticky variant is used on product listing pages.
**`nav-link-active`** — Active navigation link in coral-red, indicating the current page or section.
**`nav-link-inactive`** — Inactive navigation link in muted gray (#767986), used for non-current pages.

### Forms
**`text-input`** — A white input field with a 1px hairline border (#d6c9b2) and 8px rounded corners ({rounded.sm}). On focus, the border thickens to 2px coral-red (#f16365). Error state uses a 2px dark red border (#ea3427). Used for name, email, phone, and message fields in contact and checkout forms.
**`search-bar`** — A pill-shaped input with full rounding ({rounded.full}), 1px hairline border, and 48px height. On focus, the border switches to 2px coral-red. Used for searching vinyl records by artist, album, or catalog number.

### Badges
**`badge-new`** — A coral-red pill badge with white uppercase text. Used to flag newly added records.
**`badge-sale`** — A burnt orange pill badge for discounted items.
**`badge-limited`** — A purple (#4433cc) pill badge for limited edition pressings.

### Footer
**`footer`** — A deep navy (#0d3042) section with muted gray text (#b8bac6). Links are 14px medium weight in the same muted gray, switching to coral-red on hover. Used for site-wide footer with links to About, FAQ, Contact, and Social Media.

### Dividers
**`divider`** — A 1px hairline (#d6c9b2) horizontal rule with 24px vertical margin.
**`divider-strong`** — A 2px ink (#0d3042) horizontal rule for section breaks.

### Icons & Indicators
**`icon-circle`** — A 40px circle with a soft rose (#d7abc8) background and ink icon. Used for social media icons and feature icons.
**`icon-circle-accent`** — A 40px circle with coral-red background and white icon. Used for primary feature highlights.
**`step-indicator`** — A 32px circle for multi-step forms (e.g., checkout). Inactive steps are soft hairline with muted text; active steps are coral-red with white text; completed steps are olive (#3a4725) with white text.

### Modals & Tooltips
**`modal-overlay`** — A semi-transparent black overlay (60% opacity) behind modal cards.
**`modal-card`** — A white card with 12px rounded corners and 32px padding. Used for confirmation dialogs, quick-view product modals, and form overlays.
**`tooltip`** — A small dark tooltip with 4px rounded corners and 6px/12px padding. Used for hover hints on icons and buttons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; hero text scales to 28px; product cards stack vertically; buttons become full-width; footer links stack |
| Tablet | 744–1128px | Two-column product grid; nav remains visible but condensed; hero text at 36px; side padding reduces to 24px |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full display size; standard side padding of 32px |
| Wide | > 1440px | Max-width container at 1440px; centered content with generous margins; four-column product grid on category pages |

### Touch Targets
- All buttons and interactive elements maintain a minimum 48px height for touch accessibility
- Icon circles and step indicators are 40px and 32px respectively — the 40px size is preferred for touch targets
- Search bar and text inputs are 48px tall
- Navigation links have a minimum 44px tap area on mobile

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px
- Product grid reduces from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Hero section reduces padding and font size on mobile; background image may be cropped
- Footer link columns stack vertically on mobile
- Side-by-side form fields (e.g., first/last name) stack on mobile
- Multi-step indicators collapse to a simple progress bar on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font family declarations could not be extracted from the live site; the typography block uses reasonable fallbacks based on brand category (industrial sans-serif for display, clean sans for body). Actual font choices may differ.
- Hover and focus states for many components (e.g., footer links, tooltips, step indicators) are inferred from common patterns rather than extracted from the site.
- Error styling for forms (text-input-error) is assumed based on the primary-active color; actual error states may use a different color or include icons.
- Dark mode preferences are not supported; the design system assumes a light canvas (#faf9fe) as the default background.
- Sub-brand or seasonal color palettes (e.g., holiday, special edition) are not captured.
- The extracted color list includes many accent colors that may be used sparingly or only in specific contexts (e.g., product images, social icons). The primary palette (coral, navy, white) is the most reliable.
- Animation and transition durations (e.g., hover transitions, modal entrance) are not defined.
- Accessibility ratios (contrast, focus indicators) have not been verified against WCAG standards.
