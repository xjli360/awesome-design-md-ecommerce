---
version: alpha
name: "Fairytales Bookstore"
source_url: "https://fairytalesnashville.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A storybook-green (#36855c) doorframe against a warm gray (#f8f8f8) storefront — the brand’s primary color reads like a forest canopy, not a corporate green, and it appears on every button, badge, and navigation accent. The palette is deliberately muted: body text sits in #2b333f, a deep slate that softens reading fatigue, while #73859f and #919191 handle secondary labels and metadata with a quiet, almost chalky restraint. The single burst of warmth comes from #ffe53b, a marigold yellow used sparingly on sale badges and story-time callouts — it lands like a bookmark left in a favorite page. Typography runs Inter at modest weights (400–600), with display headlines at 24–28px and body copy at 15–16px, never shouting. Cards and buttons use {rounded.sm} (8px) corners — soft enough for a children’s store, not so round that they feel toy-like. The checkout flow introduces #006aff (a standard blue) and #d92b2b (an error red), but the brand’s own voice stays in the green-gray spectrum. The overall mood is calm, literate, and tactile without being precious — a bookstore that trusts its inventory and its readers.

colors:
  primary: "#36855c"
  primary-active: "#2c6f4d"
  primary-disabled: "#a3d4b8"
  ink: "#2b333f"
  body: "#1b1b1b"
  muted: "#73859f"
  muted-soft: "#919191"
  hairline: "#d6d6d6"
  hairline-soft: "#e6e6e6"
  canvas: "#f8f8f8"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#ffe53b"
  accent-marigold-soft: "#f1f37f"
  accent-sage: "#d7f5e6"
  accent-sage-strong: "#4e8e4a"
  error: "#d92b2b"
  link-blue: "#006aff"
  link-blue-hover: "#3374ff"
  star-rating: "#ff7734"
  scrim: "#041f2c"

typography:
  display-xl:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0

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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  text-input-error:
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    color: "{colors.primary}"
    border-bottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
    box-shadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    box-shadow: "0 4px 12px rgba(0,0,0,0.12)"
  badge-sale:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.accent-sage-strong}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-banner:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
    rounded: "{rounded.md}"
  story-time-badge:
    backgroundColor: "{colors.accent-marigold-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Subscribe". Rendered in the brand's forest green (#36855c) with white text and 8px rounded corners. On hover, darkens to #2c6f4d. When disabled, fades to a pale sage (#a3d4b8) with white text.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Save for Later". White background with a 1px green border. Hover fills the background with a soft gray (#f2f2f2) and darkens the border to the active green.

**`button-accent-marigold`** — A warm yellow (#ffe53b) button used sparingly for high-urgency actions like "Limited Edition" or "Story Time Registration". Text is dark (#2b333f) for contrast. No hover variant defined — used as a single-state accent.

### Cards
**`product-card`** — A white card with a subtle drop shadow (0 1px 3px rgba(0,0,0,0.08)) and 8px rounded corners. Contains a product image (full-width, no internal padding), title, author, price, and optional badges. On hover, the shadow deepens to 0 4px 12px rgba(0,0,0,0.12). No border — relies entirely on shadow for separation from the canvas.

**`hero-banner`** — A full-width promotional banner with a soft sage (#d7f5e6) background and dark text. Used for seasonal promotions, author events, and story-time announcements. Internal padding is 48px horizontal, 32px vertical. The banner may include a headline (display-xl), a subhead (body-md), and a button.

### Badges
**`badge-sale`** — A marigold yellow (#ffe53b) pill with uppercase 11px text. Used on product cards to indicate discounts or promotions. Text is dark (#2b333f) for readability. Padding is tight (2px 8px) to sit neatly in the top-right corner of a product image.

**`badge-new`** — A soft sage (#d7f5e6) pill with strong sage text (#4e8e4a). Indicates newly arrived titles. Same sizing and positioning as the sale badge.

**`badge-out-of-stock`** — A neutral gray (#f2f2f2) pill with muted text (#73859f). Indicates unavailable items. Same sizing.

**`story-time-badge`** — A soft marigold (#f1f37f) pill with full rounding and 4px 12px padding. Used in navigation or headers to highlight upcoming story-time events. Text is small (12px) and dark.

### Navigation
**`nav-bar`** — A 64px white bar with a subtle bottom border (#e6e6e6). Contains the store logo (left), nav links (center), and search/cart icons (right). Active nav links show a 2px green underline. On mobile, the nav collapses into a hamburger menu.

**`search-bar`** — A fully rounded (9999px) white input with a 1px gray border. On focus, the border becomes a 2px green stroke. Used for searching titles, authors, or categories. Includes a magnifying glass icon on the left.

### Forms
**`text-input`** — Standard text input for forms (newsletter signup, contact forms, checkout). White background, 8px rounded corners, 1px gray border. On focus, border becomes 2px green. Error state uses a red (#d92b2b) border. Height is 44px for comfortable touch interaction.

### Footer
**`footer-section`** — A deep navy (#2b333f) footer with white text. Contains columns for store info, customer service, social links, and a newsletter signup. Links are muted gray (#919191) and use the link typography. Padding is 64px top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack in single column; hero banner reduces padding to 24px; search bar moves below nav; footer columns stack vertically |
| Tablet | 744–1128px | Nav links visible but condensed; product cards in 2-column grid; hero banner at 32px padding; footer in 2-column layout |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3- or 4-column grid; hero banner at full padding; footer in 4-column layout |
| Wide | > 1440px | Max-width container (1440px) centered; product cards in 4-column grid; extra whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px.
- Nav bar hamburger icon is 48px × 48px.
- Search bar height is 44px.
- Product card tap targets (title, author, price) are at least 44px tall within the card.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger menu with a slide-out drawer.
- Product filters (category, age range, price) collapse into a "Filter" button that opens a modal or bottom sheet.
- Footer columns collapse from 4 columns to 2 (tablet) to 1 (mobile).
- Hero banner text reduces from display-xl to display-md on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components are inferred from common patterns; actual extracted hover colors are not available.
- Error styling for forms (error messages, validation icons) is not extracted — only the error border color (#d92b2b) is known.
- The extracted color list includes many generic web colors (#006aff, #d92b2b, #3374ff, #ff7734) that are likely from checkout widgets, social icons, or stock photography — not brand colors. The brand's true palette is assumed to be the green (#36855c), slate (#2b333f), muted blues (#73859f, #919191), and marigold (#ffe53b).
- Font weights and sizes are estimated from typical Inter usage; exact extracted values are not available.
- Dark mode is not supported — no dark theme colors were extracted.
- Sub-brand or seasonal color palettes are not documented.
- Animation and transition durations are not specified.
- The extracted font list includes "VideoJS" which is a video player font, not a brand font — it has been excluded.
- No extracted data for modal, tooltip, or dropdown styling.
