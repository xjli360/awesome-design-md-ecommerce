---
version: alpha
name: "Chaosium"
source_url: "https://www.chaosium.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep violet #221155 anchors the Chaosium brand — not as a background but as a gravitational force that appears in headers, navigation bars, product badges, and the footer, giving the entire site the weight of a grimoire cover. Against this dark, saturated purple, a sharp red #fd5757 acts as the primary action color for CTAs, sale badges, and critical alerts, creating a tension that feels both urgent and arcane. The canvas is a warm off-white #fffdea, like aged parchment, rather than a sterile digital white, and it carries body text in a neutral dark gray #444444 that reads as ink on paper. Supporting accents include a cool blue #4496f6 for secondary links and a muted gold #f1a500 for highlights and star ratings, while a soft pink #f4c8c8 and pale red #ffdddd appear in error states and discount banners. The layout uses generous whitespace and a clean grid, but the color choices — the violet, the red, the parchment — signal that this is a world of mythos, horror, and tabletop storytelling, not a generic e-commerce store. Buttons are sharply rectangular with {rounded.sm} corners, avoiding the pill shapes of consumer brands, and the typography leans on a single sans-serif stack at moderate weights, letting the color system do the emotional work. The overall impression is that of a well-worn rulebook: serious, tactile, and slightly ominous, but welcoming to those who know the lore.

colors:
  primary: "#221155"
  primary-active: "#1a0e44"
  primary-disabled: "#8a7ab5"
  ink: "#444444"
  body: "#444444"
  muted: "#757575"
  muted-soft: "#e5e5e5"
  hairline: "#dfdfdf"
  hairline-soft: "#e5e5e5"
  canvas: "#fffdea"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#fd5757"
  accent-red-active: "#d14343"
  accent-red-disabled: "#f4c8c8"
  accent-blue: "#4496f6"
  accent-blue-active: "#476bef"
  accent-gold: "#f1a500"
  accent-green: "#008a06"
  error-bg: "#ffdddd"
  error-text: "#cc4749"
  success-bg: "#d5ffd8"
  success-text: "#008a06"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.accent-red-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.accent-red-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    border: 2px solid "{colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.accent-blue}"
  text-input-error:
    border: 2px solid "{colors.error-text}"
    backgroundColor: "{colors.error-bg}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: rgba(255, 255, 255, 0.1)
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  badge-preorder:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: rgba(255, 255, 255, 0.85)

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in a sharp red `#fd5757` that demands attention against the dark violet navigation or the parchment canvas. On hover, it deepens to `#d14343`; when disabled, it fades to a soft pink `#f4c8c8`. Text is white, set in 15px/600 weight with 0.5px letter spacing for a slightly authoritative read. Corners are minimally rounded at `{rounded.sm}` (4px), avoiding the friendliness of pills.

**`button-secondary`** — Uses the brand's deep violet `#221155` as background, reserved for secondary actions like "View Details" or "Learn More" that sit alongside primary red CTAs. Hover state darkens to `#1a0e44`. Same typography and corner radius as primary, maintaining visual consistency across the button family.

**`button-tertiary`** — An outlined variant with a 2px violet border on a transparent background, used for less prominent actions within card layouts or content sections. Text is violet `#221155`; on hover, the background fills with a subtle tint.

**`button-ghost`** — Text-only violet link styled as a button, used for "Cancel" or "Back" actions in forms and modals. No border, no background — just the typography and hover underline.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with 8px rounded corners (`{rounded.md}`) and no border, relying on a soft drop shadow for separation from the parchment canvas. The image sits flush to the top corners, then title and price stack below with 16px horizontal padding. Title uses `{typography.title-sm}` (16px/600), price uses `{typography.body-md}` (16px/400). Cards are typically displayed in a 3- or 4-column grid on desktop.

### Navigation
**`nav-bar`** — A fixed-height 64px bar filled with the deep violet `#221155`, containing the Chaosium logo on the left and uppercase nav links on the right. Links are white, 14px/600 with 0.3px letter spacing. The active or hovered link gets a subtle white semi-transparent background (`rgba(255,255,255,0.1)`) with 4px rounding. On mobile, the nav collapses into a hamburger menu.

**`nav-link`** — Individual navigation items with 8px vertical and 16px horizontal padding. The uppercase treatment and letter spacing give the nav a slightly formal, rulebook-like feel.

### Badges
**`badge-sale`** — A compact red badge (`#fd5757`) with white uppercase text at 11px/700, used to flag discounted products. 4px corners and 4px/8px padding keep it tight and legible.

**`badge-new`** — Blue badge (`#4496f6`) for new releases, same typography and dimensions as the sale badge but distinct in color to avoid confusion.

**`badge-preorder`** — Gold badge (`#f1a500`) with dark text (`#444444`), used for upcoming titles available for pre-order. The gold stands out against the violet and red palette without competing with the primary action color.

### Forms
**`text-input`** — A standard input field with 44px height, 4px corners, and a 1px `#dfdfdf` border on the parchment canvas. On focus, the border becomes a 2px blue `#4496f6` line. Error state swaps the border to `#cc4749` and fills the background with pale red `#ffdddd`. Success state uses `#008a06` border and `#d5ffd8` background.

### Search
**`search-bar`** — A 44px-tall input with 4px corners, placed prominently in the header or on collection pages. Uses the parchment canvas background with a 1px `#dfdfdf` border. On focus, the border switches to blue `#4496f6`. No pill shape — the 4px corner keeps it consistent with the button system.

### Footer
**`footer`** — A deep violet `#221155` block with 48px vertical padding and white text. Links are 14px/400 in white, stacked in columns for desktop and collapsed into a single column on mobile. The footer carries copyright, legal links, and social icons.

### Hero
**`hero-section`** — Full-width violet `#221155` section with 64px vertical padding, used on the homepage and category landing pages. The title is 32px/700 white, the subtitle is 16px/400 at 85% white opacity. The hero may feature a background image or illustration overlaid with a violet scrim.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger; product cards stack vertically; hero padding reduces to 32px; footer links stack in one column |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but font size drops to 13px; hero title reduces to 28px |
| Desktop | 1128–1440px | Three-column product grid; full nav with uppercase links; hero at full 64px padding |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero may feature parallax or larger imagery |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Nav links have 44px minimum touch area even when visual height is smaller
- Product card tap targets (title, price, image) are at least 48px tall
- Badges are at least 24px tall for legibility

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer from the left
- Footer link columns collapse to a single vertical stack below 744px
- Product grids reduce columns: 4 → 3 → 2 → 1 as viewport shrinks
- Hero section reduces vertical padding from 64px to 32px on mobile
- Search bar may move from the header into a toggleable overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site; the typography stack assumes a generic sans-serif fallback (`'Helvetica Neue', Helvetica, Arial, sans-serif`). The actual brand may use a custom typeface (e.g., a display font for headings) that could not be captured.
- Hover and focus states for most components (beyond buttons and inputs) were not extractable; the system assumes standard CSS transitions where not specified.
- Error and success states for forms are inferred from the extracted hex palette but not confirmed against live validation patterns.
- The brand may have a secondary palette for sub-brands (e.g., Call of Cthulhu, RuneQuest) that was not visible in the extracted colors.
- Dark mode is not supported; the system assumes the parchment canvas `#fffdea` as the sole background.
- Drop shadow values, z-index layering, and animation timing were not extractable.
- The extracted hex list includes several colors that may be from third-party widgets (e.g., `#002fe1`, `#008a06`) rather than core brand tokens; these have been mapped to accent and status roles but should be verified against design documentation.
