---
version: alpha
name: "No Idea Records"
source_url: "https://www.noidearecords.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record store that feels like a basement show flyer stapled to a telephone pole — #103948 (deep teal) and #bc5631 (burnt orange) are the two poles of voltage, the teal serving as primary ink on a #fcfcfc canvas, the orange used sparingly for price tags, sold-out badges, and the occasional accent line that says "this matters." The site runs Josefin Sans at display sizes with its geometric, almost stencil-like letterforms, then drops into Rubik for body copy — a switch that feels like going from the marquee to the liner notes. Borders are thin (#ebeced hairline), corners are mostly sharp ({rounded.none} on cards, {rounded.xs} on buttons), and the whole thing reads like a zine that happens to sell vinyl: product titles are set in display weight, prices in a smaller muted body, and the only real ornament is the orange badge that tells you something is sold out. There is no hero video, no carousel, no newsletter popup — just a grid of records, a search bar, and the quiet confidence that if you're here, you already know what you want. The #121212 footer anchors the page with the weight of a stage monitor.

colors:
  primary: "#103948"
  primary-active: "#0d2e3a"
  primary-disabled: "#8a9ea8"
  ink: "#121212"
  body: "#333333"
  muted: "#6b6b6b"
  muted-soft: "#9a9a9a"
  hairline: "#ebeced"
  hairline-soft: "#f0f0f0"
  canvas: "#fcfcfc"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#fcfcfc"
  accent-orange: "#bc5631"
  accent-orange-light: "#d47a56"
  sold-out-badge: "#bc5631"
  price-tag: "#bc5631"
  footer-bg: "#121212"
  footer-text: "#dedede"

typography:
  display-xl:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Rubik', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.accent-orange}"
    marginTop: "{spacing.xs}"
  product-card-sold-out:
    backgroundColor: "{colors.sold-out-badge}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  badge-sold-out:
    backgroundColor: "{colors.sold-out-badge}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a solid teal rectangle with sharp {rounded.xs} corners and Josefin Sans at 15px. Used for "Add to Cart" and "Checkout" flows. On hover, the background shifts to `{colors.primary-active}` (#0d2e3a) with no border change — the darkening is subtle, like a record sleeve sliding out of its jacket. The disabled state uses `{colors.primary-disabled}` (#8a9ea8), a washed-out teal that signals unavailability without shouting.

**`button-secondary`** — An outlined variant on a white canvas with teal text and a thin `{colors.hairline}` border. Used for "View Details" and "Browse All" links that need to sit alongside primary buttons without competing. Hover adds a subtle background tint of `{colors.surface-soft}`.

**`button-accent`** — The burnt orange accent button, used sparingly for "Pre-order" or limited-edition drops. Smaller at 36px height with `{typography.button-sm}`, it reads as urgent but not aggressive — the orange is warm, not warning.

### Cards
**`product-card`** — A flat white rectangle with no rounded corners and no shadow — the record sits on the page like it's sitting on a shelf. The album art fills the top (object-fit: contain), the title sits below in `{typography.title-sm}`, and the price appears in `{colors.accent-orange}`. Sold-out items get a small orange `{typography.badge}` in the top-left corner of the card. There is no hover lift, no overlay, no animation — the card trusts the album art to do the selling.

**`product-card-sold-out`** — The sold-out badge is a small orange rectangle (`{colors.sold-out-badge}`) with white uppercase text, positioned absolutely at the top-left of the product card. It's the only decorative element on the card — everything else is information.

### Navigation
**`nav-bar`** — A 60px white bar with a thin `{colors.hairline}` bottom border. Navigation links are set in Josefin Sans at 14px with 0.5px letter spacing and uppercase — they read like section headers on a record sleeve. The active link gets a 2px teal bottom border. The nav is minimal: typically "Home," "Shop," "About," "Contact," and a cart icon.

**`nav-link-active`** — The active state uses `{colors.primary}` text and a 2px solid bottom border in the same teal. No background change, no pill shape — just a line that says "you are here."

### Forms
**`text-input`** — A white input field with a thin `{colors.hairline}` border and sharp corners. On focus, the border switches to `{colors.primary}` — the teal appears only when the user engages. Used for search, newsletter signup, and checkout forms. The placeholder text is `{colors.muted-soft}` (#9a9a9a), barely there.

**`search-bar`** — A slightly recessed input on `{colors.surface-soft}` background, used for searching the record catalog. Same sharp corners and thin border as `text-input`, but the background tint signals it's a utility, not a form field. No icon inside — just placeholder text.

### Footer
**`footer`** — A `{colors.footer-bg}` (#121212) rectangle at the bottom of every page, with `{colors.footer-text}` (#dedede) body copy. Links are the same muted gray, underlined only on hover. The footer typically contains store hours, shipping info, and social links — no newsletter signup, no decorative patterns. It's the stage monitor: dark, functional, unadorned.

### Badges
**`badge-sold-out`** — A small orange rectangle with white uppercase text at 11px. Used exclusively for sold-out items. The orange (`{colors.sold-out-badge}`) is the same as `{colors.accent-orange}` — the brand uses one orange for everything, from price tags to sold-out badges to the occasional accent line.

**`badge-new`** — A small teal rectangle with white uppercase text, used for new arrivals. Same shape and size as the sold-out badge, but in `{colors.primary}`. The two badges are the brand's only color-coded signals — everything else is black, white, or gray.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 columns), nav collapses to hamburger, search bar full-width, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid (3-4 columns), nav links visible, search bar 50% width, footer in two rows |
| Desktop | 1128–1440px | Three-column product grid (4-5 columns), full nav, search bar 33% width, footer in three columns |
| Wide | > 1440px | Max-width container at 1440px centered, product grid expands to 6 columns, nav and search remain same |

### Touch Targets
- All buttons and links: minimum 44px height, 44px width for icon-only targets
- Product cards: entire card is tappable (no separate "view" link)
- Nav links: 44px minimum tap area, even on desktop
- Search bar: 44px height for easy tapping on mobile
- Cart icon: 44x44px minimum tap target

### Collapsing Strategy
- Top nav collapses to a hamburger menu below 744px, with a slide-in drawer from the left
- Product grid collapses from 6 columns (wide) to 2 columns (mobile) — never single column
- Footer collapses from three columns (desktop) to stacked (mobile)
- Search bar collapses from inline to full-width below 744px
- Category filters (if present) collapse to a dropdown below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for `button-secondary` and `text-input` could not be reliably extracted — the live site may use a subtle background tint or border color change that wasn't visible in static analysis
- Error styling for form validation (red borders, error messages) was not found — the site may use Shopify's default error patterns
- Dark mode is not supported — the site uses a white canvas throughout with no media query for `prefers-color-scheme: dark`
- Sub-brand or collection-specific color palettes (e.g., "New Arrivals" vs. "Sale") could not be determined — the extracted colors suggest a single palette across all pages
- The `object-fit: contain` declaration was found on product images, but the exact aspect ratio (likely 1:1 for album art) could not be confirmed
- Font weights for Josefin Sans and Rubik beyond the extracted declarations are assumed — the site may use additional weights (e.g., 300, 700) that weren't present in the sampled CSS
- The `meta theme-color` was absent, meaning the browser chrome on mobile defaults to white or system color — no brand color in the address bar
- Checkout flow styling (Shopify checkout) was not analyzed — the extracted colors may include Shopify Pay widget colors that are not part of the brand's design system
- Animation and transition durations were not extracted — the site likely uses minimal transitions (0.2s or 0.3s) for hover states, but exact values are unknown
