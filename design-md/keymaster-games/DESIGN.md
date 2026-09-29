---
version: alpha
name: "Keymaster Games"
source_url: "https://keymastergames.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Three display typefaces on a single storefront — sculpin for geometric headlines, Bricolage Grotesque for characterful UI labels, maple-web for warm body text — is the kind of typographic layering that board-game retailers almost never attempt online, yet Keymaster makes the stacking order feel editorial rather than cluttered. The extracted palette runs five stops from near-white #dedede through mid-gray #777777 down to near-black #121212, a monochrome corridor with no accent hue visible in the static CSS extraction. This is a deliberate gamble: every pixel of chromatic energy belongs to the game artwork — illustrated boxes, painted landscapes, hand-lettered title lockups — and the site shell refuses to compete. Primary CTAs render in solid #191919 with `{colors.on-primary}` white text, dense and authoritative against the lighter canvas, while `{colors.surface-dark}` panels at #121212 create full-bleed hero sections that turn each featured title into a cinema-poster reveal. Buttons and cards use modest rounding (`{rounded.sm}` to `{rounded.md}`), keeping containers structured so that the organic, hand-illustrated game art provides all the curvilinear warmth. Navigation sits in Bricolage Grotesque at a restrained weight, its variable-width strokes lending a handmade quality that quietly rhymes with the tabletop ethos — things built to be touched and shared around a table. Body copy in maple-web reads warm and approachable at paragraph length, a softer voice that bridges sculpin's geometric sharpness and the humanist navigation type. A monospace face appears in accent contexts — edition numbers, game-stat callouts, promotional lockups — adding a utilitarian register that nods toward rulebook typography. Spacing runs generous, with `{spacing.xl}` and `{spacing.section}` gutters between game collections signaling gallery-wall presentation rather than catalog density. The overall system reads as a tabletop publishing house that happens to sell through Shopify: restrained chrome, editorial type hierarchy, and an absolute conviction that the brightest thing on every page should be the game itself.

colors:
  primary: "#191919"
  primary-active: "#121212"
  primary-disabled: "#777777"
  ink: "#121212"
  body: "#555555"
  muted: "#777777"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  surface-dark-elevated: "#191919"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-dark-muted: "#dedede"
  on-dark-subtle: "#777777"

typography:
  display-xl:
    fontFamily: "sculpin, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "sculpin, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "sculpin, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "sculpin, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-lg:
    fontFamily: "maple-web, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "maple-web, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "maple-web, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
    textDecoration: line-through
  link:
    fontFamily: "maple-web, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  mono-accent:
    fontFamily: "monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-dark:
    backgroundColor: "{colors.on-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 56px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-icon-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
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
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.xl}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 0
    overflow: hidden
  product-card-image:
    aspectRatio: "1 / 1"
    objectFit: cover
    rounded: "{rounded.md} {rounded.md} {rounded.none} {rounded.none}"
  product-card-body:
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
  product-card-hover:
    transform: "translateY(-4px)"
    boxShadow: "0 12px 24px rgba(18, 18, 18, 0.1)"
    transition: "transform 0.25s ease, box-shadow 0.25s ease"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-lg}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    textAlign: center
  hero-split:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    layout: "two-column 50/50"
    imageAspectRatio: "4 / 3"
    padding: "{spacing.section} {spacing.xl}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    padding: "{spacing.xxl} 0"
    textAlign: center
  game-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  game-badge-outline:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 7px"
    border: "1px solid {colors.hairline}"
  player-count-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  game-stat-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.mono-accent}"
    padding: "{spacing.sm} 0"
    borderBottom: "1px solid {colors.hairline}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 16px 48px rgba(18, 18, 18, 0.15)"
  search-result-item:
    padding: "{spacing.md} {spacing.base}"
    typography: "{typography.body-sm}"
    hoverBackground: "{colors.surface-soft}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark-muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"
  newsletter-signup:
    backgroundColor: "{colors.surface-dark-elevated}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
  newsletter-input:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.on-dark-subtle}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 48px
    border: "1px solid {colors.hairline}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 420px
    padding: "{spacing.lg}"
    boxShadow: "-8px 0 32px rgba(18, 18, 18, 0.12)"
  cart-line-item:
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
    imageSize: 80px
    imageRounded: "{rounded.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  price-display:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  price-compare-display:
    typography: "{typography.price-compare}"
    textColor: "{colors.muted}"

---

## Components

### Buttons
**`button-primary`** — The main call-to-action, rendered in near-black #191919 with white text and Bricolage Grotesque at 14px/600 weight in uppercase with 0.5px letter spacing. Uses `{rounded.sm}` (8px) corners and a 48px height. On hover the background deepens to `{colors.primary-active}` (#121212), creating a subtle darkening shift. The disabled state swaps to `{colors.primary-disabled}` (#777777), a mid-gray that clearly communicates inactivity without breaking the monochrome palette.

**`button-secondary`** — An outlined variant with a white fill and a 2px solid #191919 border, used for secondary actions like "View Details" or "Add to Wishlist." On hover the fill inverts to `{colors.primary}` with white text, making the secondary-to-primary state change feel like a decisive click-through rather than a passive highlight.

**`button-dark`** — A white button with #121212 ink text, designed for use on dark hero sections and `{colors.surface-dark}` panels. This inverted variant ensures CTAs remain visible and legible against the full-bleed game-art backgrounds that define the brand's hero regions.

**`button-add-to-cart`** — An oversized variant of the primary button at 56px height and `{typography.button-lg}` (16px), used exclusively on product detail pages. The extra vertical padding and larger type give the add-to-cart action more visual gravity than standard navigation buttons.

**`button-ghost`** — A text-only button with no background or border, using the primary ink color. Reserved for tertiary actions like "Cancel" or inline text links that need button-level click targets without visual weight.

**`button-icon-circle`** — A 40px circular button on a soft gray `{colors.surface-soft}` background with `{rounded.full}`, used for utility actions like search, cart toggle, and hamburger menu. The circle shape distinguishes utility controls from content-level CTAs.

### Cards
**`product-card`** — A white card with a `{colors.surface-soft}` (#f5f5f5) background and `{rounded.md}` (12px) corners. The product image fills the top half at a 1:1 aspect ratio with the card body below providing title in `{typography.title-sm}` and price in `{typography.price}`. On hover the card lifts 4px with a soft box shadow (`0 12px 24px rgba(18, 18, 18, 0.1)`), creating a gentle elevation effect that invites interaction.

**`product-card-image`** — The image region of the product card, using top-only rounding (`{rounded.md} {rounded.md} {rounded.none} {rounded.none}`) so the image flows into the card body seamlessly. Object-fit is set to cover, ensuring game-box art fills the frame without letterboxing.

**`product-card-body`** — The text region below the image, padded at `{spacing.base}` (16px). Game title renders in Bricolage Grotesque at 16px/600 weight, with the price below in Bricolage Grotesque at 18px/700. The compare-at price, when present, appears struck through in `{colors.muted}`.

### Navigation
**`nav-bar`** — A fixed 72px white navigation bar with a 1px bottom border in `{colors.hairline}` (#dedede). Links use Bricolage Grotesque at 14px/500 weight with 0.3px letter spacing — the variable-width character of the face gives navigation items a handmade warmth that most sans-serif navigations lack. Active links gain a 2px ink underline, while inactive links sit in `{colors.muted}` (#777777).

**`nav-bar-dark`** — An alternate navigation state for dark hero pages where the bar renders on `{colors.surface-dark}` (#121212) with `{colors.on-dark}` white text. Used when the page opens with a full-bleed dark hero that extends behind the navigation.

**`nav-link-active`** — The active state for navigation links, distinguished by a 2px bottom border in `{colors.primary}`. Typography matches `{typography.nav-link}` but the added underline provides clear wayfinding.

**`nav-link-inactive`** — Default navigation links in `{colors.muted}` (#777777), ensuring the active link stands out without needing background pills or weight changes.

### Badges
**`game-badge`** — A small rectangular badge in #191919 with white text, using `{typography.badge}` (11px uppercase Bricolage Grotesque) and `{rounded.xs}` (4px). Applied for labels like "New," "Bestseller," or "Back in Stock."

**`game-badge-outline`** — A transparent badge with a 1px `{colors.hairline}` border and `{colors.muted}` text. Used for secondary metadata tags like game categories or mechanics that should be visible but not attention-grabbing.

**`player-count-badge`** — A pill-shaped badge (`{rounded.full}`) on a `{colors.surface-soft}` background with `{colors.body}` text at `{typography.caption}` size. Displays player count ranges (e.g., "2-4 Players") and game duration as quick-scan metadata on product cards and detail pages.

### Game Stats
**`game-stat-row`** — A key-value row for displaying game metadata (play time, player count, age range, complexity) on product detail pages. Labels render in `{typography.caption}` (Bricolage Grotesque 13px) and values in `{typography.mono-accent}` (monospace 13px), separated by a 1px `{colors.hairline}` bottom border. The monospace value column nods toward rulebook typography and keeps numeric data visually aligned.

### Forms
**`text-input`** — A standard text input with a white background, `{rounded.sm}` (8px) corners, and a 1px `{colors.hairline}` border at 48px height. On focus, the border transitions to `{colors.primary}` (#191919) to provide a clear focus indicator without introducing a new color. Body text uses maple-web at 16px for input values.

**`text-input-focus`** — The focused state of text inputs, where the border switches from `{colors.hairline}` to `{colors.primary}`. No other visual change occurs, keeping the interaction minimal and relying solely on the border contrast shift.

### Search
**`search-overlay`** — A modal-style search panel with a white background, `{rounded.md}` corners, and a prominent shadow (`0 16px 48px rgba(18, 18, 18, 0.15)`). The input field uses `{typography.body-md}` with generous `{spacing.lg}` padding. Results appear as a scrollable list below the input.

**`search-result-item`** — Individual search results padded at `{spacing.md} {spacing.base}` with `{typography.body-sm}` text. On hover, the background shifts to `{colors.surface-soft}`, providing a subtle highlight for keyboard and pointer navigation.

### Footer
**`footer`** — A full-width footer on `{colors.surface-dark}` (#121212) with `{colors.on-dark}` white headings and `{colors.on-dark-muted}` (#dedede) link text. Padded with `{spacing.section}` vertically and `{spacing.xl}` horizontally. Link columns organize by category — Games, Support, Company — with each heading in `{typography.title-sm}`.

**`footer-heading`** — Section headings within the footer, using Bricolage Grotesque at 16px/600 in white with a `{spacing.base}` bottom margin. The bold weight distinguishes headings from the lighter link list below.

### Newsletter
**`newsletter-signup`** — A contained signup block on `{colors.surface-dark-elevated}` (#191919), slightly lighter than the footer background to create visual separation. Title uses `{typography.display-sm}` (sculpin 22px) and the description uses `{typography.body-sm}`. The input field has a transparent background with a 1px `{colors.on-dark-subtle}` (#777777) border, keeping the dark aesthetic cohesive.

**`newsletter-input`** — The email input within the newsletter block, using maple-web at 16px with a transparent background and `{colors.on-dark-subtle}` border. On focus, the border brightens to `{colors.on-dark}` (#ffffff).

### Announcement Bar
**`announcement-bar`** — A 40px strip at the top of the page in `{colors.primary}` (#191919) with white `{typography.caption}` text, centered. Used for shipping thresholds, new game launches, or promotional messages.

### Cart
**`cart-drawer`** — A slide-in cart panel at 420px width on a white background with a left shadow (`-8px 0 32px rgba(18, 18, 18, 0.12)`). Padded with `{spacing.lg}` and containing a scrollable list of line items.

**`cart-line-item`** — Individual cart items with an 80px thumbnail (`{rounded.sm}` corners), title in `{typography.title-sm}`, and price in `{typography.price}`. Each item is separated by a 1px `{colors.hairline}` bottom border with `{spacing.base}` vertical padding.

### Accordion
**`accordion-header`** — Expandable section headers on product detail pages, using `{typography.title-sm}` in ink with a 1px `{colors.hairline}` bottom border. Padded at `{spacing.base}` vertically. Used for game description, components list, rules overview, and shipping information.

**`accordion-content`** — The expanded content area using `{typography.body-sm}` in `{colors.body}` (#555555) with bottom padding only, keeping the layout tight against the header.

### Pricing
**`price-display`** — The current product price using `{typography.price}` (Bricolage Grotesque 18px/700) in `{colors.ink}`. Stands alone without currency symbol decoration.

**`price-compare-display`** — The original or compare-at price in `{colors.muted}` (#777777) with a line-through, rendered at `{typography.price-compare}` (14px/400). Used alongside `price-display` for sale items.

### Quantity Selector
**`quantity-selector`** — A compact stepper input at 48px height with `{rounded.sm}` corners and a 1px `{colors.hairline}` border. Minus and plus buttons flank a centered numeric value in `{typography.body-md}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces nav links, hero reduces to 360px min-height with `{typography.display-md}`, full-width buttons, stacked cart line items |
| Tablet | 744-1128px | Two-column product grid, top nav condenses to logo + icons with dropdown menus, hero uses `{typography.display-lg}`, search collapses to icon trigger |
| Desktop | 1128-1440px | Three-column product grid, full horizontal nav with all links visible, hero uses `{typography.display-xl}` at full 560px height, cart drawer slides from right |
| Wide | > 1440px | Max-width container (1440px) centered, four-column product grid, increased horizontal padding, hero imagery scales to fill viewport width behind centered content |

### Touch Targets
- All buttons maintain a minimum 48px touch height on mobile devices.
- Icon buttons are 40px with 44px minimum touch padding.
- Product cards have full-card tap area linking to the product detail page.
- Accordion headers maintain a minimum 48px tap height with full-width hit area.
- Nav hamburger icon uses a 44px square touch target.

### Collapsing Strategy
- The top navigation collapses to a hamburger icon at the tablet breakpoint (< 1128px), opening a full-height slide-out drawer with stacked nav links.
- The search bar collapses to a magnifying glass icon on tablet and mobile, expanding to a full-screen overlay on tap.
- Product grids step down from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile), maintaining consistent `{spacing.base}` gutters.
- Footer link columns stack vertically on mobile, with each section collapsing into an accordion.
- Hero sections reduce min-height and step down the type scale, with background images cropping to center on narrower viewports.
- The cart drawer becomes a full-screen overlay on mobile (< 744px) instead of a side panel.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No accent or brand hue was found in the CSS extraction — the palette is entirely grayscale (#dedede through #121212). Keymaster likely loads accent colors (game-specific palettes, promotional hues) via JavaScript or inline styles on dynamic elements. Any accent color needed for implementation should be sourced from the specific game's box-art palette or confirmed against the live site.
- Canvas color (#ffffff) and surface-soft (#f5f5f5) are inferred from Shopify defaults and the grayscale direction of the extracted palette — not directly observed in the extraction.
- Font weights for sculpin, Bricolage Grotesque, and maple-web are estimated from typical usage of these typefaces; actual CSS `font-weight` values may differ.
- The `textTransform: uppercase` on button and badge typography is an editorial assumption based on the brand's geometric, structured aesthetic — not confirmed from extracted CSS.
- Hover and active states for most components are inferred; only the primary darkening to #121212 is based on extracted color proximity.
- Dark mode tokens are speculative — the site may be dark-first rather than light-with-dark-sections, but the extraction did not confirm a global dark canvas.
- Animation durations, easing curves, and transition properties are not documented.
- Focus ring styles (outline color, offset, width) are not confirmed.
- Modal and overlay scrim opacity values are not extracted.
- Game-specific color theming (per-title hero palettes matching box art) likely exists but could not be captured as static design tokens.
- The monospace font stack is a generic `monospace` — the actual typeface name used on the site was not resolved.
