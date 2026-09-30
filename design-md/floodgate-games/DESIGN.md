---
version: alpha
name: "Floodgate Games"
source_url: "https://floodgategames.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A board-game publisher whose visual identity is anchored on a deep navy field (#002554) and a cyan signal (#00a9e0) that reads like a lighthouse beam across a dark tabletop. The palette is maritime in weight — the ink is near-black (#1a1118), the body text a cool charcoal (#555555), and the canvas a warm off-white (#f7f5f0) that softens the screen the way a well-worn game board softens a table. A single marigold accent (#ffb81c) appears sparingly, like a victory token or a meeple crown, while a coral error-red (#ff6b6b) provides the only other saturated note. The typography is where the brand reveals its character: Gelica, a rounded serif with generous ball terminals, carries display and title roles — it feels hand-drawn, friendly, and slightly whimsical, like the art on a game box lid. Greycliff, a geometric sans-serif, handles body and UI copy, creating a clean counterpoint to Gelica's warmth. Buttons and cards use soft radii (`{rounded.sm}` for buttons, `{rounded.md}` for cards), never sharp corners, and the primary CTA sits in that cyan field (`{colors.primary}`) with white text (`{colors.on-primary}`). The nav bar is a full-bleed strip of the deepest navy (`{colors.ink}`), creating a strong top boundary. The overall effect is one of deliberate contrast: a dark, serious frame around playful, illuminated content — the tabletop after the lights go down, the box lid lifted.

colors:
  primary: "#00a9e0"
  primary-active: "#0090c0"
  primary-disabled: "#c8d8e8"
  ink: "#1a1118"
  body: "#555555"
  muted: "#707372"
  muted-soft: "#dedede"
  hairline: "#c8d8e8"
  hairline-soft: "#e8eef5"
  canvas: "#f7f5f0"
  surface-soft: "#f4f7fb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#ffb81c"
  accent-marigold-active: "#e6a500"
  error: "#ff6b6b"
  dark-bg: "#002554"
  dark-bg-deep: "#001a3a"

typography:
  display-xl:
    fontFamily: "'Gelica', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Gelica', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Gelica', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Gelica', Georgia, serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Gelica', Georgia, serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Greycliff', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  body-lg:
    fontFamily: "'Greycliff', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Greycliff', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Greycliff', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Greycliff', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "'Greycliff', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Greycliff', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Greycliff', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Greycliff', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Greycliff', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-marigold-active:
    backgroundColor: "{colors.accent-marigold-active}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.xl}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    rounded: "{rounded.xs}"
  nav-link-active:
    backgroundColor: "rgba(255,255,255,0.1)"
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    rounded: "{rounded.xs}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 0
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.dark-bg-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
  hero-section:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.xl}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.on-primary}"
  hero-subtitle:
    typography: "{typography.body-lg}"
    color: "{colors.muted-soft}"
  section-header:
    typography: "{typography.display-lg}"
    color: "{colors.ink}"
    padding: "{spacing.section} 0 {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's cyan signal (`{colors.primary}`) and white text (`{colors.on-primary}`). On hover/active, it deepens to `{colors.primary-active}` (#0090c0). The disabled state uses a pale blue-gray (`{colors.primary-disabled}`) with muted text. All primary buttons use `{rounded.sm}` (8px) and uppercase Greycliff at 15px/600.

**`button-secondary`** — An outlined variant with a dark-ink border on the warm canvas background. The active state fills with the deep navy (`{colors.dark-bg}`) and flips text to white. Used for "Learn More" or "View All" actions that should not compete with the primary CTA.

**`button-accent-marigold`** — A special-purpose button using the marigold accent (`{colors.accent-marigold}`) with dark ink text. Reserved for high-visibility actions like "Add to Cart" on product detail pages or promotional banners. Active state shifts to `{colors.accent-marigold-active}` (#e6a500).

**`button-ghost`** — A text-only button with no background, using the primary cyan for its text color. Used for secondary actions within cards or for "Cancel" / "Close" patterns. Hover state adds a subtle background tint.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with a soft 12px radius (`{rounded.md}`) and a thin, nearly invisible border (`{colors.hairline-soft}`). The card image clips to the top corners via `{rounded.md} {rounded.md} 0 0`. On hover, the border strengthens to `{colors.hairline}` and a subtle shadow lifts the card. The title uses Gelica at 18px/500, the price sits below in Greycliff body-sm at `{colors.muted}`.

### Navigation
**`nav-bar`** — A full-width strip of the deepest navy (`{colors.dark-bg}`), 72px tall, with white uppercase nav links. The active state applies a semi-transparent white background and switches the link text to the primary cyan. The bar is fixed or sticky on desktop, collapsing to a hamburger on mobile.

**`nav-link`** — Uppercase Greycliff at 14px/600 with 0.5px letter-spacing. Links have 8px horizontal padding and a 4px rounded hover/active background. The active state uses `rgba(255,255,255,0.1)` for a subtle highlight.

### Forms
**`text-input`** — A white input field with a 1px hairline border and 8px radius. On focus, the border becomes a 2px cyan stroke (`{colors.primary}`). Error state uses a 2px coral border (`{colors.error}`). All inputs use Greycliff body-md (16px/400) for entered text.

### Badges
**`badge-new`** — A marigold pill badge with dark ink text, used to flag newly released games. Uses `{rounded.full}` and uppercase 11px/600 Greycliff with 1px letter-spacing.

**`badge-sale`** — A coral pill badge (`{colors.error}`) with white text for discount indicators.

**`badge-out-of-stock`** — A muted gray pill badge (`{colors.muted-soft}`) with `{colors.muted}` text for unavailable items.

### Search
**`search-bar`** — A full-radius pill input with a white background and hairline border. On focus, the border becomes a 2px cyan stroke. The pill shape (`{rounded.full}`) gives it a friendly, approachable feel consistent with the brand's rounded aesthetic.

### Footer
**`footer`** — A deep navy section (`{colors.dark-bg-deep}`) with white body-sm text and link-colored navigation. Uses generous vertical padding (`{spacing.xxl}`) and a multi-column layout for links, social icons, and legal text.

### Hero
**`hero-section`** — A full-width navy (`{colors.dark-bg}`) section with white display-xl headlines and body-lg subtext. The hero may feature a game illustration or product photo as a background element, with the text overlaid. Padding is `{spacing.section}` (64px) on top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; hero text shrinks to display-lg; search bar moves below nav; footer stacks vertically |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards in 2-column grid; hero maintains display-xl but reduces padding; footer uses 2-column layout |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero at full size with 64px padding; multi-column footer |
| Wide | > 1440px | Max-width container (1440px) centered; product cards may expand to 4-column; hero content centered with wider margins |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have 48px minimum touch area (including padding)
- Search bar is 48px tall for comfortable tapping
- Product card CTAs are at least 44px tall
- Badge pills are at least 24px tall with 10px horizontal padding

### Collapsing Strategy
- Primary nav collapses to a hamburger menu below 744px; the hamburger icon sits in the nav bar with the brand logo
- Product card grids collapse from 3 columns to 2 at tablet, to 1 at mobile
- Footer columns collapse from 4 to 2 at tablet, to a single stack at mobile
- Hero section reduces vertical padding from 64px to 32px on mobile
- Search bar moves from the nav bar to below it on mobile, becoming full-width
- Product filters (if present) collapse into a slide-out drawer on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is heavily weighted toward blues and grays, with only one marigold accent and one coral error color. The brand's true primary (#00a9e0) and secondary (#ffb81c) were identified as the most distinctive non-generic colors, but the full brand palette may include additional game-specific accent colors (e.g., greens, purples) that were not captured.
- Font-family declarations found were Gelica, Georgia, Greycliff, inherit, and serif. The exact font weights and styles for Gelica (italic, bold, etc.) and Greycliff (light, medium, bold) were not extracted. The typography scale above uses reasonable defaults based on common web usage.
- Hover and active states for most components are inferred from common patterns; exact extracted values were not available.
- Error, success, and warning state colors beyond the coral error (#ff6b6b) were not extracted.
- Dark mode colors were not extracted; the brand uses a dark navy background for nav and hero, but a full dark-mode palette is unknown.
- Sub-brand or collection-specific palettes (e.g., for individual game lines) were not captured.
- The Shopify platform integration may introduce checkout-specific colors (e.g., Shopify Pay buttons) that are not part of the brand's design system.
- Social media icon colors (Facebook blue, Twitter blue, Instagram gradient) were filtered from the extracted list but may appear in the footer.
- Stock image dominant tones (e.g., warm browns, greens from game photography) may have influenced the extracted color list.
- The exact `textTransform` property for button typography (uppercase) is inferred from the brand's uppercase nav links and common board-game industry patterns; it may not be present on all button variants.
