---
version: alpha
name: "Planet Mu"
source_url: "https://www.planet.mu"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record label and shop that uses a high-voltage orange-red (#ff4c2d) as its primary signal — a color that reads as urgent, almost warning-like, against a canvas of near-white (#d0d0d0) and stark black ink. The brand leans on a small set of accent colors that feel lifted from early internet culture: a pure yellow (#ffff00) and a saturated cyan (#0099ff) that together with the primary orange create a primary-color triad reminiscent of 90s rave flyers and net.art. Typography runs on a mix of Circular Pro (Bold and Medium weights) and Circular Std Book, with Arial and Helvetica as fallbacks — the brand trusts bold weight and generous size over decorative typefaces. Buttons and interactive elements use {rounded.full} pill shapes, while product cards and content containers use {rounded.sm} (8px) — a subtle distinction that keeps the shop feel approachable without losing edge. The overall mood is loud but controlled: the orange-red dominates every primary action, the yellow and cyan appear as badges, sale markers, or limited-edition flags, and the gray (#d0d0d0) provides a quiet structural grid for releases, tracklists, and artist pages. There is no meta-theme-color, no Shopify framework, and no attempt at luxury — this is a label that sells music directly, with the visual confidence of a flyer stapled to a telephone pole.

colors:
  primary: "#ff4c2d"
  primary-active: "#e03a1f"
  primary-disabled: "#ffb3a3"
  ink: "#000000"
  body: "#1a1a1a"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d0d0d0"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#ffff00"
  accent-cyan: "#0099ff"
  badge-new: "#ffff00"
  badge-sale: "#ff4c2d"
  star-rating: "#000000"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Circular-Pro-Bold', 'CircularStd-Book', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Circular-Pro-Bold', 'CircularStd-Book', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Circular-Pro-Medium', 'CircularStd-Book', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Circular-Pro-Bold', 'CircularStd-Book', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Circular-Pro-Medium', 'CircularStd-Book', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'CircularStd-Book', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'CircularStd-Book', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'CircularStd-Book', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Circular-Pro-Bold', 'CircularStd-Book', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Circular-Pro-Bold', 'CircularStd-Book', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'CircularStd-Book', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Circular-Pro-Medium', 'CircularStd-Book', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Circular-Pro-Bold', 'CircularStd-Book', Arial, Helvetica, sans-serif"
    fontSize: 10px
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
  hero-banner-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
  tracklist-item:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 8px 0
  tracklist-item-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: 8px 12px
  artist-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
  artist-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's signature orange-red (#ff4c2d) with white text and full pill rounding. Uses uppercase bold type at 14px with 0.5px letter-spacing for a confident, slightly aggressive tone. On hover, shifts to a darker active state (#e03a1f); on disable, fades to a soft peach (#ffb3a3) with no interaction.

**`button-secondary`** — An outlined-equivalent button with white background and black text, maintaining the same pill shape and uppercase bold typography. Used for secondary actions like "View All" or "Browse Artists." Active state uses the soft surface background (#f5f5f5) to indicate press.

**`button-accent-yellow`** — A high-visibility variant using the brand's pure yellow (#ffff00) with black text, reserved for limited drops, pre-order announcements, or flash sale triggers. Same pill shape and typography as primary, but the yellow-on-black reads as urgent and celebratory.

**`button-accent-cyan`** — A secondary accent button using the brand's saturated cyan (#0099ff) with white text, used for genre tags, streaming links, or external platform CTAs. Maintains the full pill shape and uppercase bold system.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, white background with black text. Links use uppercase 14px medium weight type with 0.3px letter-spacing. Active link adopts the primary orange-red color; inactive links sit in muted gray (#666666). No background fill on nav items — only text color changes signal state.

**`nav-link-active`** — Active navigation link styled with the brand's primary orange-red (#ff4c2d) against transparent background. No underline or border — color alone carries the active state.

**`nav-link-inactive`** — Inactive navigation link in muted gray (#666666), same transparent background and uppercase typography. Hover state transitions to the primary orange-red.

### Cards
**`product-card`** — A white card with 8px rounding used for album, EP, and merchandise listings. Contains an image area (also 8px rounded), title, artist name, format, and price. On hover, the entire card shifts to a soft gray background (#f5f5f5) with no border or shadow — a subtle lift that doesn't compete with the product imagery.

**`artist-card`** — A white card for artist profile pages, using 8px rounding and the medium title typography. On hover, the text color shifts to the primary orange-red while the background softens, creating a clear but restrained interactive signal.

**`product-card-image`** — The image container within product cards, using 8px rounding to match the card itself. No border or overlay — the album art or product photo sits flush against the card edge.

### Badges
**`badge-new`** — A small yellow (#ffff00) badge with black text, 10px uppercase bold type, and 4px rounding. Used to flag new releases, restocks, or recently added items. Padded 2px vertically and 8px horizontally for a compact, tag-like appearance.

**`badge-sale`** — A small orange-red (#ff4c2d) badge with white text, same typography and sizing as the new badge. Used for sale items, discounts, or limited-time offers. The color matches the primary button, creating visual consistency across promotional elements.

### Forms
**`text-input`** — A standard text input with white background, 8px rounding, 44px height, and 16px horizontal padding. Uses the body-md typography (16px) for readability. On focus, the border shifts to the primary orange-red — no outline, just a color change on the 1px hairline border.

**`text-input-focus`** — The focused state of the text input, distinguished by a primary orange-red border (#ff4c2d) replacing the default hairline gray. No additional glow or shadow — the color shift alone signals active input.

### Search
**`search-bar`** — A pill-shaped search input with soft gray background (#f5f5f5), 40px height, and 16px horizontal padding. Uses body-sm typography (14px) for placeholder text. The full rounding and soft background make it feel integrated into the page rather than a separate UI element.

### Footer
**`footer-section`** — A full-width footer with black background (#000000) and white text. Contains links, social icons, and copyright information. Links use the muted-soft gray (#999999) for a lower visual hierarchy, with hover transitioning to white.

**`footer-link`** — Footer navigation links in muted-soft gray (#999999) with 14px regular weight type. On hover, shifts to white for clear but restrained feedback.

### Hero
**`hero-banner`** — A full-width hero section with black background and white text, using the display-xl typography (32px bold). Used for featured releases, label compilations, or major announcements. No overlay or gradient — the black canvas makes the white and orange-red text pop.

**`hero-banner-accent`** — A variant hero section using the primary orange-red background with white text and display-lg typography (28px bold). Used for sale events, limited drops, or urgent announcements where the brand wants maximum visual impact.

### Tracklist
**`tracklist-item`** — A transparent tracklist row with 8px vertical padding, using body-sm typography (14px). Track numbers, titles, and durations are separated by consistent spacing. On hover, the row gets a soft gray background and 12px horizontal padding for a subtle highlight effect.

**`tracklist-item-hover`** — The hover state of a tracklist item, adding a soft gray background (#f5f5f5) and 12px horizontal padding to the default transparent row. No border or color change — the background shift alone signals the interactive state.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to 24px; search bar becomes full-width; tracklist padding reduces |
| Tablet | 744–1128px | Two-column product grid; nav remains visible with reduced link spacing; hero maintains 28px; search bar stays pill-shaped but narrower |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 32px; standard search bar width; tracklist shows full metadata |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero text scales to 36px; additional whitespace around cards |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have 48px touch area (64px bar height provides natural padding)
- Product cards have full-card tap targets (no small hit areas)
- Search bar is 40px tall — slightly below the 44px recommendation but acceptable for non-primary interaction
- Tracklist items have 40px minimum touch height (8px padding × 2 + 14px font × 1.45 line-height ≈ 36px, padded to 40px)

### Collapsing Strategy
- Navigation collapses to a hamburger menu below 744px, with a slide-in drawer from the left
- Product grid collapses from 4 columns to 3 to 2 to 1 as viewport narrows
- Hero banner text reduces in size but maintains full-width layout
- Tracklist metadata (duration, catalog number) hides below 744px, showing only track number and title
- Footer links stack vertically below 744px, with social icons moving to a separate row

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is small (5 colors) and may not represent the full brand palette — particularly missing are any secondary grays for hover states, error colors, or link-specific colors. The primary orange-red (#ff4c2d) is distinctive and likely correct, but the yellow and cyan may be accent colors used sparingly rather than core brand colors.
- No meta-theme-color was found, suggesting the brand may not use a browser theme color or it's set dynamically.
- Font-family declarations found include Arial, Calibri, Circular-Pro-Bold, Circular-Pro-Medium, CircularStd-Book, Helvetica, monospace, and sans-serif. The Circular variants are likely the brand's primary typeface, but exact weights and usage patterns (display vs. body vs. button) are inferred from common DTC label patterns rather than extracted.
- No hover states, active states, focus rings, or error styling could be extracted — all interactive states in this document are inferred from common patterns in the brand's category.
- No dark mode or high-contrast mode data was found.
- No spacing or rounded values could be extracted from the live site — the values in this document are based on common DTC record label patterns and may not match the actual site exactly.
- The brand may use additional accent colors for genre tagging, format badges (vinyl, CD, digital), or limited edition runs that were not captured in the extraction.
- No typography scale beyond the extracted font names could be reliably determined — font sizes, weights, and line heights are estimated based on the brand's category and the extracted font names.
