---
version: alpha
name: "Banquet Records"
source_url: "https://www.banquetrecords.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record shop that trusts its blue — not a generic navy or a trendy cobalt, but a specific #61afd5 that reads as both a clear sky and a vintage pressing-label center. This cyan-adjacent primary sits against a #2e475b ink that feels like a well-worn sleeve, giving the whole interface a quiet, knowledgeable confidence. There is no aggressive red or urgent orange here; the brand communicates through a calm, considered palette where the primary blue appears on key CTAs and category headers, while the deep ink handles body copy and navigation. The layout leans on generous whitespace and a clean grid, letting album artwork do the heavy lifting — product cards use soft {rounded.md} corners that echo the gentle curve of a 12-inch cover, and buttons carry a modest {rounded.sm} radius that feels purposeful without being playful. Typography runs a straightforward sans-serif stack at moderate weights, with display sizes staying lean enough to not compete with the vivid sleeve art. The search experience is central — a full-width bar with {rounded.full} ends that invites browsing by artist, label, or format. The overall mood is that of a knowledgeable clerk who lets the records speak first: the interface is a frame, not the picture.

colors:
  primary: "#61afd5"
  primary-active: "#4a8ca8"
  primary-disabled: "#b3d9e8"
  ink: "#2e475b"
  body: "#3a5a6e"
  muted: "#6b8a9e"
  muted-soft: "#9bb3c4"
  hairline: "#d0dce5"
  hairline-soft: "#e3eaf0"
  canvas: "#ffffff"
  surface-soft: "#f4f7f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-ink: "#ffffff"
  badge-new: "#e8a838"
  badge-sale: "#c45a4a"
  stock-in: "#5ba85a"
  stock-low: "#e8a838"
  star-rating: "#e8a838"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px
  price:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
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
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.muted}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  button-icon-square:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  button-icon-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
    height: 34px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 17px
    height: 34px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px {colors.primary-disabled}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    border: "1px solid {colors.badge-sale}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px {colors.primary-disabled}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(46, 71, 91, 0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
  product-card-info:
    padding: "{spacing.md} {spacing.base}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginBottom: "{spacing.xs}"
  product-card-artist:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    marginBottom: "{spacing.xs}"
  product-card-format:
    typography: "{typography.caption-sm}"
    color: "{colors.muted-soft}"
    marginBottom: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-stock-in:
    backgroundColor: "{colors.stock-in}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-stock-low:
    backgroundColor: "{colors.stock-low}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    marginBottom: "{spacing.base}"
  hero-subheading:
    typography: "{typography.body-lg}"
    color: "{colors.body}"
    marginBottom: "{spacing.lg}"
  category-nav:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  category-link:
    typography: "{typography.nav-link}"
    color: "{colors.muted}"
    padding: "{spacing.sm} {spacing.base}"
  category-link-active:
    typography: "{typography.nav-link}"
    color: "{colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "2px solid {colors.primary}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 32px
    width: 32px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    typography: "{typography.link}"
    color: "{colors.canvas}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 42px
    border: "1px solid {colors.hairline}"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 42px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  section-header:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.lg} 0 {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Sign Up". Renders in the brand's distinctive #61afd5 blue with white text on a compact 40px height. On hover, shifts to `primary-active` (#4a8ca8) for a subtle darkening. The disabled state uses `primary-disabled` (#b3d9e8) with reduced opacity and no pointer events.

**`button-secondary`** — An outlined alternative for "View Details", "Pre-Order", and secondary actions. Uses a white background with ink text and a 1px hairline border. On hover, the border deepens to muted and the background picks up `surface-soft`. Maintains the same 40px height and 6px corner radius as primary.

**`button-ghost`** — A text-only button for inline actions like "Clear Filters" or "Cancel". No background or border in default state; on hover, a soft `surface-soft` background appears. Uses the same typography and height as other button variants for alignment consistency.

**`button-pill-primary`** — A compact, fully rounded variant used for "View All" links, category quick-links, and mobile filter toggles. Smaller at 34px height with tighter padding, using the same primary blue. The pill shape (`{rounded.full}`) differentiates it from standard buttons.

**`button-pill-outline`** — The outlined counterpart to the pill button, used for "Sort By" dropdown triggers and "Reset" actions. White background with a hairline border and ink text, maintaining the same compact 34px height and full rounding.

### Navigation
**`top-nav`** — A fixed 64px header bar on white canvas with a thin bottom hairline. Contains the brand logo on the left, a set of nav links (New Releases, Vinyl, CDs, Merch, Events, Sale) in the center, and utility icons (Search, Account, Cart) on the right. Active nav links use the primary blue; inactive links sit in muted gray and shift to ink on hover.

**`category-nav`** — A secondary navigation strip below the hero or above product listings. Displays format and genre filters (Vinyl 12", Vinyl 7", CD, Cassette, etc.) as horizontal links. The active category gets a 2px bottom border in primary blue, while inactive links remain muted.

**`filter-bar`** — A horizontal row of filter chips for refining product listings by price range, condition, label, and release year. Each chip is a pill-shaped toggle with a soft background and hairline border; the active state fills with primary blue and white text. Multiple chips can be active simultaneously.

### Cards
**`product-card`** — The core product display unit, a white card with a 1:1 aspect ratio image area and a text block below. The image uses `{rounded.md}` on top corners only, creating a subtle framing effect. Below the image, the info area shows the artist name in muted, the album title in ink at title-sm weight, the format label in muted-soft caption, and the price in bold. On hover, the card gains a subtle shadow and a slightly stronger border.

### Forms
**`text-input`** — Standard single-line input for forms, search filters, and account fields. White background with a hairline border and 6px radius. On focus, the border switches to primary blue with a 3px outer glow in `primary-disabled`. Error state uses the `badge-sale` red for the border.

**`select-input`** — Dropdown selector for format, genre, and sort options. Matches the text-input styling with a custom chevron icon. The selected value appears in ink; placeholder text uses muted.

**`search-bar`** — A full-width, pill-shaped search field with a soft background and hairline border. Used on the homepage hero and as a persistent element in the top nav. On focus, the background turns white and the border highlights with primary blue and its glow. Includes a search icon on the left and a clear button on the right when text is entered.

### Badges
**`badge`** — Small uppercase labels for product attributes. The default badge uses primary blue for general labels like "Pre-Order" or "Exclusive". Specialized variants exist for "New Release" (amber), "Sale" (red), "In Stock" (green), and "Low Stock" (amber). All badges share the same 11px uppercase typography, 4px rounding, and compact padding.

### Footer
**`footer`** — A dark section on `ink` background with white text. Contains columns for Help, About, Connect, and a newsletter signup form. Links render in `muted-soft` and brighten to white on hover. The newsletter input matches the standard text-input style but sits on the dark background, with the submit button in primary blue.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 columns), hamburger menu replaces top nav, filter bar collapses to a single "Filter" button that opens a drawer, search bar moves to a dedicated overlay, category nav hides behind a "Browse" dropdown, hero section reduces padding to 32px vertical |
| Tablet | 744–1128px | Two-column product grid (3 columns), top nav shows abbreviated links (icons only for utility items), filter bar shows as a horizontal scrollable strip, category nav remains visible with condensed labels, hero uses 48px vertical padding |
| Desktop | 1128–1440px | Three-column product grid (4 columns), full top nav with text labels, filter bar shows all chips in a wrapping row, category nav fully expanded, hero at standard 64px padding |
| Wide | > 1440px | Four-column product grid (5-6 columns), max-width container at 1440px centered, additional whitespace on sides, hero can accommodate larger display typography |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Filter chips and category links have 36px minimum height with generous padding
- Product card tap targets (Add to Cart, Quick View) are at least 40px tall
- Search bar height stays at 48px across all breakpoints
- Navigation links have 44px tap areas even when visually compact

### Collapsing Strategy
- Top nav collapses to hamburger menu at mobile breakpoint, with a slide-in drawer for all links
- Category nav collapses to a single "Browse" select dropdown on mobile
- Filter bar collapses to a single "Filter & Sort" button that opens a modal/drawer
- Product grid reduces from 4-5 columns on wide screens to 2 columns on mobile
- Hero section reduces vertical padding and may stack CTA buttons vertically on mobile
- Footer columns stack to a single column on mobile, with newsletter form spanning full width
- Search transitions from inline bar to full-screen overlay on mobile for better keyboard experience

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were found during extraction; the typography stack uses Inter as a reasonable sans-serif default for an independent record store — this should be verified against the actual site CSS or design tokens
- Only two hex colors were extracted (#61afd5 and #2e475b); the remaining color tokens (muted, hairline, surface, badge colors) are inferred from common design patterns for this brand category and should be validated against the live site
- Hover, focus, and active states for all components are inferred from standard interaction patterns — actual site implementations may differ
- Error and validation styling (error messages, success states, form validation) is not present in the extracted data
- Dark mode support is unknown — the current palette assumes a light theme
- Animation and transition durations/easings are not specified
- Icon set and illustration style are not documented
- Product card hover shadow values and image aspect ratios are assumed based on common record store patterns
- Checkout flow components (cart drawer, checkout button, payment forms) are not represented in the extracted data
- The brand may use a custom font for logos or display headings that was not captured in extraction
- Sub-brand or seasonal color variations (Record Store Day exclusives, sale events) are not documented
