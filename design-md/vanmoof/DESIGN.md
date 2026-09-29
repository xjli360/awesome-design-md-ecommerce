---
version: alpha
name: "VanMoof"
source_url: "https://www.vanmoof.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A monochrome machine punctuated by a single electric signal: #4945ff, a saturated indigo that appears nowhere in the brand's own product photography but everywhere in its interface — the unlock button on the app, the active state on the bike's matrix display, the accent line on the S5 frame render. The palette is almost entirely grayscale: #222222 ink, #313131 body, #f7f7f7 canvas, #e0e0e0 hairline. This is a brand that treats color as a rare resource, not a decorative one. The typography stack confirms the editorial ambition: PPEditorialNew (a sharp, serifled display face with high contrast) sits alongside Unica77LLWeb (a Swiss neo-grotesk) and Unica77Mono for code-like data readouts. The brand speaks through mechanical precision — thin hairlines, tight letter-spacing on display text, and a near-total absence of decorative rounding. Buttons use {rounded.sm} (8px), not pills. Cards use {rounded.md} (12px). The only {rounded.full} token appears on the search bar and the primary CTA, making those moments genuinely special. The extracted hex #f1ff3b — a neon chartreuse — appears in the bike's own LED matrix (the "kick-lock" indicator and e-shifter feedback) and is used sparingly in UI as a status badge. The brand's voice is confident, minimal, and slightly Dutch: direct, unadorned, and built for riders who care about engineering as much as aesthetics.

colors:
  primary: "#4945ff"
  primary-active: "#3a36e0"
  primary-disabled: "#b3b3ff"
  ink: "#222222"
  body: "#313131"
  muted: "#6a6a6a"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#f7f7f7"
  surface-soft: "#f3f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#a70000"
  success: "#428042"
  accent-neon: "#f1ff3b"
  accent-blue: "#dbeef9"
  scrim: "#030303"

typography:
  display-xl:
    fontFamily: "'PPEditorialNew', 'Unica77LLWeb', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'PPEditorialNew', 'Unica77LLWeb', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.75px
  display-md:
    fontFamily: "'PPEditorialNew', 'Unica77LLWeb', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Unica77LLWeb', -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Unica77LLWeb', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Unica77LLWeb', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Unica77LLWeb', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Unica77LLWeb', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Unica77LLWeb', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
    textTransform: uppercase
  caption-sm:
    fontFamily: "'Unica77LLWeb', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  mono:
    fontFamily: "'Unica77Mono', 'SF Mono', 'Fira Code', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Unica77LLWeb', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Unica77LLWeb', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Unica77LLWeb', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Unica77LLWeb', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Unica77LLWeb', -apple-system, system-ui, sans-serif"
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
  section: 80px

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
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
    border: "1px solid {colors.hairline}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.error}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-badge:
    backgroundColor: "{colors.accent-neon}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 40px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    height: 56px
  hero-secondary-cta:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    height: 56px
    border: "1px solid {colors.hairline}"
  feature-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  feature-card-icon:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    height: 48px
    width: 48px
  feature-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.caption}"
    textColor: "{colors.canvas}"
  status-badge:
    backgroundColor: "{colors.accent-neon}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  status-badge-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  status-badge-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  mono-data:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.mono}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"

## Components

### Buttons
**`button-primary`** — The primary action button, rendered in {colors.primary} with white text and {rounded.sm} corners. Used for "Book a Test Ride", "Add to Cart", and "Configure" CTAs. On hover, shifts to {colors.primary-active} (#3a36e0). Disabled state uses {colors.primary-disabled} (#b3b3ff). The uppercase button text at 15px with 0.5px letter-spacing gives it a technical, precise feel.

**`button-secondary`** — An outlined variant with a white background, ink text, and a 1px {colors.hairline} border. Active state thickens the border to {colors.ink}. Used for "Learn More" and "Compare" actions where the primary button would be too aggressive.

**`button-tertiary`** — A text-only button with no background or border. Used for "View Details" links and dismiss actions. Inherits the same uppercase button typography but without the visual weight of a filled button.

**`button-pill-primary`** — A smaller, fully rounded variant ({rounded.full}) of the primary button, used in the search bar and filter controls. Height is 40px with tighter padding, making it suitable for inline use.

**`button-pill-outline`** — The outlined counterpart to the pill button, used for filter chips and secondary search actions. The pill shape signals a toggle-able or dismissable action.

### Cards
**`product-card`** — The primary content card for bike listings, with a white background, {rounded.md} corners, and 16px padding. The card contains an image area with {rounded.sm} corners, a price using {typography.title-sm}, and a CTA button. A neon badge ({colors.accent-neon}) overlays the image for "New" or "In Stock" indicators.

**`feature-card`** — Used in the "Why VanMoof" section and feature grids. Contains an icon in a soft gray square ({colors.surface-soft}, {rounded.sm}), a title in {typography.title-md}, and body text. The card has no border — it relies on generous padding and the contrast between {colors.surface-card} and {colors.canvas} to define its boundaries.

**`hero-section`** — The full-width hero area with {colors.canvas} background, {typography.display-xl} headline, and two CTAs (primary and secondary). The hero uses 80px vertical padding and contains the bike's hero image. The headline uses PPEditorialNew at 48px with tight letter-spacing, creating a magazine-like editorial feel.

### Navigation
**`top-nav`** — A 72px fixed navigation bar with {colors.canvas} background and a subtle bottom border ({colors.hairline-soft}). Contains the VanMoof logo, nav links (Bikes, Accessories, App, Support), and a search icon. The nav links use uppercase {typography.nav-link} at 14px with 0.5px letter-spacing.

**`nav-link`** — Standard nav link with {colors.body} text and 8px/16px padding. Active state adds a 2px bottom border in {colors.primary}, creating a clean underline indicator.

### Forms
**`text-input`** — Standard text input with a white background, {rounded.sm} corners, and a 1px {colors.hairline} border. Focus state switches the border to {colors.primary}. Error state uses {colors.error} (#a70000) for the border. Height is 48px with 12px/16px padding.

**`search-bar`** — A pill-shaped search input ({rounded.full}) with a 1px {colors.hairline} border. Focus state uses {colors.primary} border. Height is 48px with 12px/20px padding. Used in the top nav and on the search results page.

### Badges & Status
**`status-badge`** — A small, inline badge using {colors.accent-neon} (#f1ff3b) background with ink text. Used for "New", "In Stock", and "Limited Edition" labels. The neon color is a direct reference to the bike's LED matrix display.

**`status-badge-error`** — Error badge using {colors.error} background with white text. Used for "Out of Stock" and "Service Required" indicators.

**`status-badge-success`** — Success badge using {colors.success} (#428042) background with white text. Used for "Ready to Ship" and "Fully Charged" indicators.

### Data Display
**`mono-data`** — A monospaced data display block using {typography.mono} (Unica77Mono) on a soft gray background ({colors.surface-soft}) with {rounded.xs} corners. Used for battery percentage, speed readouts, range estimates, and firmware version numbers. The mono typeface gives these data points a technical, instrument-panel feel.

### Footer
**`footer`** — A dark footer with {colors.ink} background and white text. Contains column headings in {typography.caption} (uppercase, 13px) and links in {colors.muted-soft}. The footer uses 48px vertical padding and contains the brand's legal text, social links, and newsletter signup.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; hero headline drops to {typography.display-md} (28px); product cards stack vertically; footer columns collapse to single column; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grid; top-nav shows all links but with reduced padding; hero uses {typography.display-lg} (36px); feature cards in 2x2 grid; footer in 2-column layout |
| Desktop | 1128–1440px | Full three-column product grid; top-nav at full width; hero at full {typography.display-xl} (48px); feature cards in 3-column grid; footer in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; hero content centered with 80px padding; product grid expands to 4 columns for accessories; feature cards maintain 3-column grid with increased padding |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons are 40x40px with 48px touch area via padding
- Product card CTAs are 40px tall with 20px padding
- Nav links have 8px/16px padding for comfortable tap targets
- Search bar is 48px tall for easy thumb access

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with a full-screen overlay menu
- Product grid collapses from 3 columns to 2 at tablet, to 1 at mobile
- Feature cards collapse from 3 columns to 2 at tablet, to 1 at mobile
- Footer columns collapse from 4 to 2 at tablet, to 1 at mobile
- Hero section reduces headline size and stacks CTAs vertically at mobile
- Search bar moves from inline in the nav to full-width below the nav at mobile
- Product card badges overlay on desktop, become inline below the image on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components are inferred from the primary-active color and standard interaction patterns; exact hover transitions (duration, easing) were not extractable
- Error styling for forms uses #a70000 from the extracted palette, but the exact error message typography and iconography are inferred
- The extracted hex list includes several colors (#e5e7eb, #f3f4f6, #cecece, #efefef) that may be framework defaults or checkout widget colors; the palette above uses the most distinctive and frequently occurring grays
- Dark mode styling was not extractable from the live site; the current palette assumes a light mode default
- The exact font weights for PPEditorialNew and Unica77LLWeb are inferred from common usage; the live site may use additional weights
- Sub-brand or campaign-specific color variations (e.g., limited edition bike colors) are not captured
- Animation and transition timing values (durations, easings) were not extractable
- The #428042 (success green) and #a70000 (error red) are inferred from the extracted list; their exact usage in the design system is unconfirmed
- The accent-neon (#f1ff3b) usage is inferred from the bike's LED matrix; its exact UI application frequency is unknown
- Shopify checkout widget colors (if present) may have been filtered out; the palette assumes a custom checkout experience
