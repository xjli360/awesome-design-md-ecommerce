---
version: alpha
name: "Boomkat"
source_url: "https://www.boomkat.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A single hex — #313131 — governs Boomkat’s entire visual identity, a near-black ink that reads as deliberate, archival, and anti-sensational in a category where album covers and artist pages often scream for attention. The site is a dense, text-forward grid built for deep browsing: track titles, label names, and format codes stack in compact rows with minimal imagery, trusting the listener’s knowledge over the visual hook. There are no pill-shaped search bars or soft cards here — corners are sharp ({rounded.none}), spacing is tight ({spacing.sm} between rows), and the primary action is the simple text link that opens a player or adds to cart. The type stack is the system default cascade (-apple-system, Helvetica Neue, Arial, sans-serif), a deliberate refusal of branded typography that keeps the focus on content, not container. White canvas (#ffffff) and a single hairline (#dddddd) provide the only relief from the ink density; the result is a record store that feels like a library — quiet, authoritative, and built for people who already know what they’re looking for. The brand’s signature move is the absence of move: no hero carousel, no gradient, no accent color. Every pixel is subordinate to the catalog.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#6e6e6e"
  muted-soft: "#9e9e9e"
  hairline: "#dddddd"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#313131"
  link-hover: "#1a1a1a"
  badge-new: "#313131"
  badge-sale: "#d32f2f"
  star-rating: "#313131"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.2px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
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
    rounded: "{rounded.none}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 9px 19px
    height: 40px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 40px
    border: "none"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 600
  badge-format:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  player-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: 64px
    borderTop: "1px solid {colors.hairline}"
  player-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "6px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart" and checkout flows. Solid ink (#313131) fill with white text, zero border radius, and compact 10px 20px padding. On hover, shifts to `{colors.primary-active}` (#1a1a1a). Disabled state uses `{colors.primary-disabled}` (#a0a0a0) with no outline — the button simply fades into the background.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Preview". White background with ink text and a 1px hairline border. Hover state adds a subtle background tint (`{colors.surface-soft}`). Used sparingly to avoid visual clutter.

**`button-tertiary-text`** — A text-only button for inline actions like "Clear filters" or "Show more". No background, no border, just ink text with underline on hover. The most minimal button in the system, reflecting Boomkat's preference for content over chrome.

**`button-add-to-cart`** — The primary purchase button, slightly taller (44px) than standard buttons to accommodate longer text like "Add to Basket — £12.99". Same ink fill as `button-primary` but with 12px 24px padding for visual weight in the product detail area.

### Cards
**`product-card`** — The core browsing unit: a compact rectangle with zero border radius, white background, and 8px padding. Contains an image placeholder (`{colors.surface-soft}`), the artist name in `{typography.body-sm}` muted, the album title in `{typography.title-sm}` ink, and the price in bold `{typography.body-md}`. No shadow, no hover lift — the card is a container, not a statement.

**`product-card-image`** — A simple rectangle with soft gray background, no rounded corners. The image is the content; the container disappears. Aspect ratio varies by format (LP, CD, digital).

### Navigation
**`top-nav`** — A 56px fixed bar with white background and a single hairline bottom border. Contains the Boomkat logo (text, not icon), genre links (Electronic, Experimental, Ambient, etc.), and a search icon. Links are uppercase `{typography.nav-link}` with 16px horizontal padding. Active section gets a 2px ink underline.

**`nav-link`** — Uppercase, 14px, weight 600, with 16px horizontal padding. No background change on hover — the link text simply stays ink. Active state adds a 2px bottom border in ink.

**`search-bar`** — A flat input field with soft gray background (`{colors.surface-soft}`), no border, no rounded corners. 40px height with 8px 12px padding. Focus state switches to a 1px ink border. The search icon sits inside the field on the left.

### Forms
**`text-input`** — A standard input with white background, 1px hairline border, and zero border radius. 40px height with 8px 12px padding. Focus state swaps the hairline for ink. Used for email signup, checkout forms, and filter inputs.

**`filter-dropdown`** — A compact select element (36px height) with white background, 1px hairline border, and zero border radius. Used in the catalog header for sorting by genre, format, or price. The dropdown arrow is the only decorative element.

### Badges
**`badge-format`** — A small uppercase label indicating format (LP, CD, MP3, WAV). Soft gray background with muted text, 2px 6px padding. Sits above the album title on product cards.

**`badge-new`** — An ink-filled badge for new arrivals. Same dimensions as format badge but with high contrast. Used sparingly — only for releases less than a week old.

**`badge-sale`** — A red (#d32f2f) badge for discounted items. Same dimensions as other badges. The only color accent in the entire system, used exclusively for price reductions.

### Player
**`player-bar`** — A 64px fixed bottom bar with white background and top hairline border. Contains playback controls (play/pause, skip), track info (artist — title), and a progress bar. The progress bar is a thin 2px ink line with a 12px circular handle.

**`player-button`** — A transparent square button (32px) for play/pause, skip, and volume. Ink icon with no background change on hover. The button is the icon — no container, no border.

### Footer
**`footer`** — A soft gray section (`{colors.surface-soft}`) with 32px vertical padding and a top hairline border. Contains links to About, Contact, Shipping, and Terms in `{typography.body-sm}` muted. No columns, no icons — just a single block of text links.

**`footer-link`** — A simple text link in muted gray with underline on hover. No color change — the underline is the only indicator.

### Pagination
**`pagination`** — A row of page numbers with 8px padding each. Active page gets an ink fill with white text; inactive pages are transparent with ink text. No rounded corners, no border. The simplest possible pagination.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item per row). Top nav collapses to hamburger menu. Search bar moves to a toggleable overlay. Player bar reduces to 48px height. Filter dropdowns stack vertically. Footer links stack in a single column. |
| Tablet | 744–1128px | Two-column product grid. Top nav shows genre links but collapses sub-genres under a "More" dropdown. Search bar remains visible but shrinks to 60% width. Player bar shows condensed track info (artist only). |
| Desktop | 1128–1440px | Three-column product grid. Full top nav with all genre links visible. Search bar at full width. Player bar shows full track info. Filter dropdowns in a horizontal row. |
| Wide | > 1440px | Four-column product grid. Max-width container (1440px) centered on screen. Additional whitespace on sides. No other layout changes — the system scales by adding columns, not complexity. |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Player buttons are 44x44px on mobile (up from 32x32px on desktop).
- Filter dropdowns expand to full width on mobile for easier tapping.
- Pagination numbers are 44x44px touch targets on mobile (up from 32x32px on desktop).

### Collapsing Strategy
- Top nav genre links collapse into a hamburger menu on mobile. The hamburger icon is the only persistent element in the collapsed nav.
- Search bar collapses into a search icon on mobile. Tapping the icon opens a full-width overlay with the input field and a close button.
- Product card details (format badge, price) remain visible at all breakpoints — nothing collapses inside the card.
- Footer links collapse from a horizontal row to a vertical stack on mobile.
- Filter dropdowns collapse from a horizontal row to a vertical stack on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extracted from the live site. The remaining colors (white, grays, red for sale badge) are inferred from common web patterns and may not match the exact brand values. The red for sale badges (#d32f2f) is a guess based on standard e-commerce convention.
- No font-family declarations beyond the system default stack were found. Boomkat may use a custom typeface (e.g., a monospaced or serif font for the logo) that wasn't captured in the extraction.
- Hover states for buttons and links are inferred from common patterns (darkening the primary color, adding underline). Actual hover behavior may differ.
- Error styling for forms (validation messages, error borders) was not observed. A standard red (#d32f2f) border and text is assumed but not confirmed.
- Dark mode support is unknown. The site may use `prefers-color-scheme` media queries, but no dark mode styles were extracted.
- The player bar's exact height, progress bar styling, and button sizes are estimated from typical music player UIs. Actual dimensions may vary.
- No animation or transition timings were extracted. The site likely uses instant state changes (no fade, no slide) given its minimal aesthetic, but this is unconfirmed.
- The logo (text or icon) was not extracted. Boomkat's wordmark may use a custom typeface or a specific arrangement of the brand name.
- Sub-brand or category-specific color variations (e.g., a "Staff Picks" section with a different accent) were not observed.
