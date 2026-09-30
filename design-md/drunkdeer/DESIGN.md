---
version: alpha
name: "DrunkDeer"
source_url: "https://drunkdeer.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-performance gaming keyboard brand that operates in the dark — literally. The canvas is #121212, not white; the primary voltage is #874cd3, a saturated violet that reads as cybernetic signal rather than playful accent. This is a brand that trusts deep shadow (#222222, #282828) and near-black (#111111) as its comfortable habitat, letting the purple pulse as the only color that escapes the void. Typography runs Montserrat and Poppins at modest weights — display sits at 24–32px in weight 500/600, never screaming, because the keyboards themselves are the visual spectacle. The extracted border-radius of 10px (`{rounded.md}`) appears consistently across product cards, buttons, and module edges — a single, repeatable corner radius that gives the interface a precise, machined feel without going fully pill-shaped. The meta theme-color of #282828 confirms the brand lives in this dark space even in the browser chrome. Product imagery is the hero: keyboards photographed in low light with per-key RGB glow, making each switch and keycap a point of light against the black. The violet (#874cd3) appears in primary CTAs, active states, and accent highlights — it is the single brand voltage that carries every "Add to Cart" button and spec-badge dot. There is no white anywhere except on text (#dedede body copy) and on-primary surfaces. The brand feels like a control room at night: focused, illuminated only where necessary, and built for precision.

colors:
  primary: "#874cd3"
  primary-active: "#6b3aa8"
  primary-disabled: "#3d2a5c"
  ink: "#dedede"
  body: "#dedede"
  muted: "#999999"
  muted-soft: "#666666"
  hairline: "#333333"
  hairline-soft: "#282828"
  canvas: "#121212"
  surface-soft: "#1a1a1a"
  surface-card: "#222222"
  on-primary: "#ffffff"
  accent-green: "#112211"
  accent-blue-dark: "#111177"
  accent-blue-mid: "#111166"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Poppins', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Poppins', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Montserrat', 'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  link:
    fontFamily: "'Montserrat', 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 10px
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
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  icon-button-circle:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
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
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.md}"
    height: 36px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's distinctive violet (#874cd3). Hover state shifts to `{colors.primary-active}` (#6b3aa8) for a subtle darkening effect, while disabled state drops to `{colors.primary-disabled}` (#3d2a5c) with muted text. The 10px corner radius (`{rounded.md}`) matches the machined aesthetic of the keyboards themselves.

**`button-secondary`** — A dark card-background button with a hairline border, used for less prominent actions like "View Details" or "Compare". The border provides definition against the dark canvas without competing with the primary violet.

**`button-tertiary-text`** — A text-only button using the primary violet, reserved for inline actions like "Learn More" or "Read Specs". No background or border keeps it minimal against the dark interface.

**`button-pill-accent`** — A fully pill-shaped variant used for small badges, filter tags, and quick-action toggles. The full roundness (`{rounded.full}`) creates a deliberate contrast with the otherwise consistent 10px radius system.

### Navigation
**`top-nav`** — A fixed 72px dark bar with uppercase nav links in Montserrat 500. Active links glow in the brand violet, while inactive links sit in muted gray. A single-pixel hairline border at the bottom provides the only separation from content.

**`nav-link-active` / `nav-link-inactive`** — Uppercase navigation links that shift color to signal current section. The uppercase treatment and 0.5px letter-spacing give the nav a technical, precision-oriented feel.

### Cards
**`product-card`** — The primary product display unit, built on `{colors.surface-card}` (#222222) with 10px rounded corners. Each card contains a product image (also 10px rounded), a title, specs, and price. The dark card against the #121212 canvas creates subtle depth without harsh shadows.

**`product-card-badge`** — A small violet badge pinned to product cards for "New", "Sale", or "Pre-order" indicators. The 4px radius (`{rounded.xs}`) keeps it compact and legible.

**`spec-badge`** — A neutral badge used for technical specifications (switch type, connectivity, layout). The soft background and muted text keep specs readable without competing with primary badges.

### Forms
**`text-input`** — Dark card-background input fields with hairline borders and 10px radius. Focus state swaps the border to primary violet, creating a clear active indicator against the dark interface.

**`search-bar`** — A dedicated search input matching the text-input pattern but with reduced height for header placement. The 10px radius maintains consistency with the button system.

**`quantity-selector`** — A compact control for cart quantity adjustments, built on a soft surface with button-sm typography. The 36px height keeps it proportional alongside product cards.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to `{typography.display-md}`; buttons go full-width |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero maintains `{typography.display-lg}` |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at `{typography.display-xl}` |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered |

### Touch Targets
- All interactive elements maintain minimum 44px height for touch accessibility
- Icon buttons and quantity selectors at 40px and 36px respectively — acceptable for desktop but should expand to 44px on mobile
- Product card tap targets (entire card is clickable) at minimum 200px height

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with slide-out drawer from the left
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport shrinks
- Hero section reduces typography scale and stacks CTA buttons vertically below 744px
- Footer links collapse into accordion-style sections below 744px
- Search bar collapses to icon-only trigger below 744px, expanding to full-width overlay on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the live site; only primary button hover was inferred from the active color
- Error styling for form inputs (validation messages, error borders) was not present in extracted data
- Dark mode is the default and only mode — no light mode variant was detected
- Sub-brand or collection-specific color palettes (e.g., limited edition keyboard colors) were not captured
- The extracted hex list includes several near-black values (#111111, #222222, #282828, #121212) that appear to be different surfaces rather than a single canvas — the exact hierarchy of dark surfaces is inferred from typical gaming keyboard site patterns
- Font weight hierarchy (which weights map to which text roles) is partially inferred from common Montserrat/Poppins usage patterns
- Animation and transition timing values were not extractable from static CSS
- The extracted colors include #112211, #111177, and #111166 which may be RGB LED accent colors or checkout-widget artifacts — their exact usage context is unclear
