---
version: alpha
name: "Bull Moose"
source_url: "https://www.bullmoose.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A #eeeeee warm gray canvas — the extracted dominant hex — sets a quiet, utilitarian stage for a movie-and-music retailer that trusts its inventory photography over decorative design. The brand’s typography leans on kanedagothic-extrabold for display moments, a heavy Japanese gothic face that lands with the weight of a vinyl crate, while body copy defaults to system sans-serif stacks. There is no single brand-color voltage; instead, the interface reads as a catalog-first marketplace where product images, pre-order badges, and price tags carry the visual load. Navigation is dense and text-heavy — genre dropdowns, format filters, and release calendars stack in a left-aligned column, echoing the browsing experience of a physical record store where you scan spines rather than hero images. Buttons use soft {rounded.sm} corners and a muted gray fill that blends into the canvas, reserving contrast for actionable text like “Add to Cart” or “Pre-Order.” The footer is a wall of links — store locations, trade-in policies, genre guides — organized in tight columns with {spacing.xs} gaps, prioritizing information density over breathing room. The overall feel is that of a well-organized warehouse: functional, browsable, and indifferent to trend, with the extracted #eeeeee canvas acting as the neutral ground that lets every movie poster and album cover pop.

colors:
  primary: "#eeeeee"
  primary-active: "#cccccc"
  primary-disabled: "#f5f5f5"
  ink: "#222222"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#e5e5e5"
  canvas: "#eeeeee"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#222222"
  on-primary-disabled: "#999999"
  accent-blue: "#007bff"
  accent-green: "#28a745"
  badge-new: "#ff6600"
  badge-preorder: "#ffcc00"
  price: "#222222"
  sale-price: "#cc0000"

typography:
  display-xl:
    fontFamily: "'kanedagothic-extrabold', 'Arial Black', 'Impact', sans-serif"
    fontSize: 32px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'kanedagothic-extrabold', 'Arial Black', 'Impact', sans-serif"
    fontSize: 24px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'kanedagothic-extrabold', 'Arial Black', 'Impact', sans-serif"
    fontSize: 18px
    fontWeight: 800
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
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
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary-disabled}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 8px 0
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.price}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    color: "{colors.sale-price}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: 32px 16px
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    color: "{colors.surface-card}"
    typography: "{typography.title-sm}"
  category-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  category-filter-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
    height: 36px

## Components

### Buttons
**`button-primary`** — The default action button, rendered on the warm gray canvas with a matching fill. The text sits in medium-weight system sans at 14px with 0.2px letter spacing, creating a subtle distinction from body copy. On hover, the fill shifts to `{colors.primary-active}` (#cccccc) for a gentle darkening cue; the disabled state drops to `{colors.primary-disabled}` (#f5f5f5) with `{colors.on-primary-disabled}` text, signaling inactivity without harsh contrast.

**`button-secondary`** — An outlined equivalent for less prominent actions, using a white surface-card background with a 1px hairline border (implied by the `{colors.hairline}` token). Hover adds a subtle shadow or border darkening. Used for “View Details” or “Add to Wishlist” alongside primary buttons.

**`button-ghost`** — A text-only button with no background or border, used for inline actions like “Clear Filters” or “Cancel.” The text uses `{colors.body}` at `{typography.button-sm}` size, with hover underlining as the only interaction cue.

### Cards
**`product-card`** — The core content container for movies, music, and games. A white surface-card background with `{rounded.sm}` corners and no shadow — the card relies on the `{colors.canvas}` background for separation. The image area fills the top with `{rounded.sm}` corners, while the title, format badge, and price stack below with `{spacing.xs}` gaps. Price is set in `{typography.body-md}` at full weight; sale prices switch to `{colors.sale-price}` (#cc0000) for urgency.

### Navigation
**`nav-bar`** — A fixed-height 56px bar using the `{colors.canvas}` background. Primary links (Movies, Music, Games, Trade-In) use `{typography.nav-link}` at 14px/500 weight, with dropdown arrows for genre submenus. The bar includes a logo lockup on the left and a search icon + cart icon on the right, all aligned to a 16px grid.

**`nav-dropdown`** — A white card that appears below nav links on hover or click. Items are stacked with `{spacing.sm}` padding, using `{typography.body-sm}` for genre names and `{typography.caption}` for sub-genres. The dropdown has `{rounded.md}` corners and a subtle hairline border.

### Forms
**`text-input`** — Standard input field for search, login, and checkout forms. White background with `{rounded.sm}` corners and a 1px `{colors.hairline}` border. Focus state adds a 2px `{colors.ink}` border. Height is 40px with 8px horizontal padding for comfortable text entry.

**`quantity-selector`** — A compact input for cart quantities, with decrement/increment buttons flanking a numeric display. Uses `{colors.surface-card}` background and `{rounded.sm}` corners, with 36px height for dense cart layouts.

### Badges
**`badge-new`** — An orange (#ff6600) pill for newly released items, set in 11px uppercase bold with white text. The `{rounded.xs}` corners keep it compact, fitting inside product-card titles or grid overlays.

**`badge-preorder`** — A yellow (#ffcc00) badge for upcoming releases, using dark text for contrast. Positioned similarly to the new badge but signaling availability status rather than novelty.

### Search
**`search-bar`** — A pill-shaped input (`{rounded.full}`) with white background, used in the nav bar and on search results pages. The 40px height matches button and input standards, with 16px horizontal padding for comfortable text entry. A magnifying glass icon sits on the left, and a clear button appears on text entry.

### Footer
**`footer`** — A dark (#222222) section at the page bottom, containing columns of links for store locations, trade-in policies, genre guides, and company info. `{typography.body-sm}` for link text with `{colors.muted-soft}` (#999999) for reduced visual weight. Column headings use `{typography.title-sm}` in white for hierarchy.

### Filters
**`category-filter`** — A pill-shaped filter chip for browsing by genre, format, or release year. Uses `{colors.surface-soft}` (#f2f2f2) background with `{typography.button-sm}` text. The active state (`category-filter-active`) inverts to `{colors.ink}` background with white text, making the selected filter stand out against the gray canvas.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; filters stack vertically; footer links collapse into accordion; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links with dropdowns; filters display as horizontal scrollable strip; footer shows two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; filters as sidebar or top strip; footer shows four columns; search bar in nav |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; filters as persistent sidebar; footer shows four columns with larger padding |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets extend to full card width for easy selection on mobile
- Filter chips are 36px+ tall with 14px+ horizontal padding
- Quantity selector buttons are 36px × 36px minimum
- Nav hamburger icon is 44px × 44px

### Collapsing Strategy
- On mobile, the top navigation collapses to a hamburger menu with a slide-out drawer
- Footer link groups collapse into accordion panels on mobile, with the first panel expanded by default
- Product filters collapse into a “Filter” button that opens a modal overlay on mobile
- Search bar collapses to an icon in the nav on mobile, expanding to full-width on tap
- Category strips collapse to a horizontal scroll with fade indicators on tablet and below

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Primary brand color is ambiguous — the extracted #eeeeee is a warm gray that may be a background default rather than a true brand color. The site may have a more distinctive accent (e.g., a signature blue or orange) that wasn’t captured in the extraction.
- No secondary or accent colors could be reliably extracted beyond the generic #eeeeee. Badge colors (#ff6600, #ffcc00) are inferred from common e-commerce patterns.
- Font family extraction returned Font Awesome icons and kanedagothic-extrabold — the latter is used for display headings, but body copy likely falls back to system fonts. Exact body font stack is assumed.
- Hover and focus states for buttons, links, and inputs are inferred from common patterns; exact colors and transitions are unknown.
- Error styling for forms (validation messages, error borders) could not be extracted.
- Dark mode or high-contrast mode variants are not present in the extracted data.
- Sub-brand or seasonal color palettes (e.g., holiday themes, genre-specific accents) are not documented.
- Spacing and sizing values are estimated from common e-commerce patterns; exact pixel values may vary on the live site.
- The site may use a different grid system or breakpoint set than the one documented here.
