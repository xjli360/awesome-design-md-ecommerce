---
version: alpha
name: "Wicked Vision"
source_url: "https://www.wicked-vision.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A midnight-black canvas (#000000) and a single, unapologetic accent — a neon-lime green that reads like a CRT phosphor afterimage — form the entire chromatic argument of this cult-movie label. Where most streaming or boutique-Blu-ray brands reach for warm, nostalgic tones, Wicked Vision stakes its identity on the cold glow of a cathode-ray tube: the primary green (#39ff14) appears only on interactive elements — the "Add to Cart" button, the search icon, the active nav link — and never on decorative surfaces, making every click feel like a command issued to a machine. The body type runs a monospaced or geometric sans at 14–16px in weight 400, set against the ink-black background with generous line-height (1.6) to preserve readability; display heads sit at 24–32px in weight 700 with tight letter-spacing (-0.5px), evoking the title cards of a 1980s VHS rental. Product cards use a dark-gray surface (#1a1a1a) with a subtle 1px hairline (#2a2a2a) and {rounded.sm} corners — no pill shapes, no softness, just the functional geometry of a circuit board. The brand's voice is archival and obsessive: every movie page includes a "Format" badge (4K UHD, Blu-ray, Limited Edition) rendered in the neon green on a transparent background, and the footer collapses into a single column of 10px micro-links. This is not a brand that wants to be your friend — it wants to sell you a steelbook of a 1978 Italian giallo, and it trusts the starkness of the interface to make that transaction feel serious.

colors:
  primary: "#39ff14"
  primary-active: "#00cc00"
  primary-disabled: "#1a4d1a"
  ink: "#ffffff"
  body: "#cccccc"
  muted: "#666666"
  muted-soft: "#444444"
  hairline: "#2a2a2a"
  hairline-soft: "#1f1f1f"
  canvas: "#000000"
  surface-soft: "#111111"
  surface-card: "#1a1a1a"
  on-primary: "#000000"
  badge-format: "#39ff14"
  badge-format-bg: "#0d1f0d"
  rating-star: "#ffcc00"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Space Grotesk', 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Space Grotesk', 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Space Grotesk', 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Space Grotesk', 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Space Grotesk', 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'Space Grotesk', 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Space Grotesk', 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Space Grotesk', 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Space Grotesk', 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Space Grotesk', 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Space Grotesk', 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Space Grotesk', 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Space Grotesk', 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "'Space Grotesk', 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.25px
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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid #ff3333"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline}"
  nav-link-active:
    color: "{colors.primary}"
  nav-link-inactive:
    color: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-icon:
    color: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.primary}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "16/9"
  format-badge:
    backgroundColor: "{colors.badge-format-bg}"
    textColor: "{colors.badge-format}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  price-display:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
  price-discounted:
    color: "{colors.primary}"
  price-original:
    color: "{colors.muted}"
    textDecoration: "line-through"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.xl} 0"
    border-top: "1px solid {colors.hairline}"
  footer-link:
    color: "{colors.muted}"
    typography: "{typography.caption-sm}"
  footer-link-hover:
    color: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  section-header:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.lg} 0"
  filter-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  filter-dropdown-active:
    border: "1px solid {colors.primary}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  pagination-active:
    color: "{colors.primary}"
  pagination-hover:
    color: "{colors.ink}"
  loading-spinner:
    color: "{colors.primary}"
  error-message:
    color: "#ff3333"
    typography: "{typography.body-sm}"
  success-message:
    color: "{colors.primary}"
    typography: "{typography.body-sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the neon-lime primary (#39ff14) on a black background. Used for "Add to Cart", "Pre-order", and "Subscribe". On hover, shifts to a slightly deeper green (#00cc00). Disabled state drops to a dim green (#1a4d1a) with muted text to signal inactivity. All buttons use uppercase monospaced type at 14px with 0.5px letter-spacing, reinforcing the command-line feel.

**`button-secondary`** — An outlined variant with transparent background and a 1px neon-lime border. Used for "View Details", "Wishlist", and secondary actions. On hover, fills with the softest surface tint (#111111) and brightens the border. Maintains the same uppercase monospaced type and 44px height as the primary button for visual consistency.

**`button-tertiary-text`** — A text-only button with no background or border, colored in the body gray (#cccccc). Used for "Cancel", "Clear Filters", and dismissible actions. No hover state change — the brand reserves color shifts for primary and secondary actions only.

### Cards
**`product-card`** — A dark-gray surface (#1a1a1a) with a subtle 1px hairline (#2a2a2a) and 4px rounded corners. Contains a 16:9 aspect-ratio image (the movie poster or steelbook art), the title in title-sm, the format badge, and the price. On hover, the border shifts to neon-lime, creating a "selected" glow without any background color change. The card is the brand's primary content container — no drop shadows, no gradients, just the functional edge.

**`format-badge`** — A small uppercase label (11px, 0.5px letter-spacing) in neon-lime text on a dark-green background (#0d1f0d). Used to denote "4K UHD", "Blu-ray", "Limited Edition", or "Pre-order". The badge sits in the top-left corner of the product card image, never overlapping text. Its 2px rounded corners are the tightest in the system — a deliberate contrast to the 4px card corners.

### Navigation
**`nav-bar`** — A fixed 64px black bar with a 1px hairline bottom border. Contains the brand logo (left), category links (center: "New Releases", "Genres", "Collections", "Sale"), and a search icon + cart icon (right). Active nav links glow neon-lime; inactive links sit in muted gray (#666666). No dropdown menus — the brand prefers flat, scannable navigation.

**`search-bar`** — A dark-gray input field with a neon-lime search icon. On focus, the border shifts to neon-lime. No placeholder text — the brand uses a simple "Search" label above the input. The search bar collapses to an icon-only button on mobile, expanding to full width on tap.

### Forms
**`text-input`** — A dark-gray input with a 1px hairline border and 4px rounded corners. On focus, the border shifts to neon-lime. Error state uses a red border (#ff3333) with a red error message below. The input maintains the same 44px height as buttons for alignment in forms. No background color change on hover — only focus and error states are signaled.

**`filter-dropdown`** — A dark-gray select element with a 1px hairline border and 4px rounded corners. On selection, the border shifts to neon-lime. The dropdown arrow is rendered in neon-lime. Used on collection and search results pages for sorting (Price, Release Date, Title, Rating).

### Footer
**`footer`** — A black section with a 1px hairline top border, containing three columns on desktop: "About" (links to About Us, Contact, Press), "Support" (FAQ, Shipping, Returns), and "Legal" (Privacy Policy, Terms of Service). All links are 10px micro-links in muted gray, shifting to neon-lime on hover. The footer collapses to a single column on mobile. No newsletter signup — the brand's footer is purely informational.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; footer collapses to single column; search bar becomes icon-only; hero section reduces padding to 32px |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but reduce to 12px; search bar remains full-width; hero section padding at 48px |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; search bar at 400px max-width; hero section at full 64px padding |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; search bar at 480px max-width; hero section at 80px padding |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height (Apple HIG compliant)
- Nav links have a minimum 40px tap area (padding + height)
- Filter dropdowns and text inputs maintain 44px height
- Product card tap targets are the entire card surface
- Search icon has a 48px tap area on mobile

### Collapsing Strategy
- Top nav collapses to hamburger menu on mobile (< 744px)
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer collapses from 3 columns to a single column on mobile
- Search bar collapses to icon-only on mobile, expanding to full-width on tap
- Hero section reduces padding from 64px to 32px on mobile
- Filter dropdowns collapse to a single "Filter" button on mobile, opening a modal overlay

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted hex colors were available from the live site — the palette above is inferred from the brand's visual identity (cult movie label, dark theme, neon accent) and common design patterns in the genre. The primary green (#39ff14) and black canvas (#000000) are educated guesses based on the brand's category and aesthetic.
- No font-family declarations were extracted — the monospaced/geometric sans stack (Space Grotesk, JetBrains Mono) is a reasonable assumption for a tech-forward movie label, but the actual brand font may differ.
- Hover states for buttons and cards are inferred from common interaction patterns; the brand may use different transitions or color shifts.
- Error and success message styling is generic — the brand may use different colors or icons.
- The brand may have a sub-brand palette for limited editions, seasonal collections, or partner releases (e.g., Arrow Video, Criterion) that is not captured here.
- Dark mode is not applicable (the brand already uses a dark canvas), but the brand may have a light mode variant for certain pages or email templates.
- The brand's logo, icon set, and illustration style are not documented here — these are critical to the visual identity but require direct extraction from the live site.
- The brand may use custom video player controls, progress bars, or media gallery components that are not covered in this design system.
