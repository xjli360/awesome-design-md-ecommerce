---
version: alpha
name: "Princeton University Press"
source_url: "https://press.princeton.edu"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A scholarly publisher that signals authority through a deep navy anchor (#111432) and a restrained palette of lavender-tinged grays (#b6b7d5, #d6d6e7, #f5f5fa) that feel like academic stone rather than commercial white. The brand's primary voltage comes from #3c4fe0, a vivid periwinkle blue that appears in navigation, links, and key interactive elements — unexpected for a university press, more reminiscent of a modern SaaS platform than a traditional academic house. This blue sits alongside a warm amber accent (#ff9326) used sparingly for special offers and callouts, and a soft cream (#fdf8ed) that surfaces in featured content areas. The system uses generous whitespace and subtle surface distinctions (#efeff5, #fcfcfd) to create hierarchy without heavy borders, with hairlines at #d6d6e7 and softer separators at #ededed. Typography runs clean and legible across the catalog-heavy interface, where book covers provide the primary visual interest against a predominantly neutral backdrop. The overall feel is serious but approachable — a library reading room lit by a single warm lamp.

colors:
  primary: "#3c4fe0"
  primary-active: "#2a3cc4"
  primary-disabled: "#b6b7d5"
  ink: "#111432"
  body: "#23263b"
  muted: "#5a5e9a"
  muted-soft: "#727272"
  hairline: "#d6d6e7"
  hairline-soft: "#ededed"
  canvas: "#ffffff"
  surface-soft: "#f5f5fa"
  surface-card: "#ffffff"
  surface-warm: "#fdf8ed"
  on-primary: "#ffffff"
  accent-amber: "#ff9326"
  accent-amber-dark: "#e09600"
  accent-rose: "#f9c9bf"
  accent-gold: "#f4daa6"
  error: "#e62600"
  error-soft: "#fff4f4"
  success: "#003399"
  link-blue: "#3c4fe0"
  footer-bg: "#111432"
  footer-text: "#b6b7d5"
  badge-new: "#aa1177"
  badge-sale: "#ff9326"

typography:
  display-xl:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-lg:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  book-title:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  book-author:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
    color: "{colors.muted}"

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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-ghost-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
  button-accent-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  text-input-error:
    border: "1px solid {colors.error}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(17, 20, 50, 0.08)"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 16px rgba(17, 20, 50, 0.12)"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.on-primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.book-title}"
    rounded: "{rounded.sm}"
    boxShadow: "0 1px 3px rgba(17, 20, 50, 0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(17, 20, 50, 0.12)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "2/3"
  product-card-meta:
    typography: "{typography.book-author}"
    color: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-subject:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-featured:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 0 {spacing.base} 0"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.hairline}"
    margin: "0 {spacing.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with periwinkle blue (#3c4fe0) and white text. Used for "Add to Cart", "Subscribe", and primary form submissions. On hover, deepens to `{colors.primary-active}`. Disabled state uses the muted lavender `{colors.primary-disabled}` with white text. Height is 44px with 12px vertical padding and 24px horizontal.

**`button-secondary`** — An outlined variant with a white fill and periwinkle blue border and text. Used for "Preview" and "Learn More" actions. On hover, the background shifts to `{colors.surface-soft}` and the border deepens. Same 44px height as primary for alignment in button groups.

**`button-ghost`** — A text-only button with no border or background, using periwinkle blue text. Used for "Cancel", "View All", and inline actions. On hover, a subtle `{colors.surface-soft}` background appears. Padding is 12px 16px with no fixed height.

**`button-accent-amber`** — A warm amber variant (`{colors.accent-amber}`) with dark ink text. Used sparingly for special promotions, limited-time offers, and featured calls-to-action. Same dimensions as `button-primary` for consistency.

### Cards
**`product-card`** — The primary content container for book listings. A white card with a subtle drop shadow (`0 1px 3px rgba(17, 20, 50, 0.08)`) and 4px corner rounding. On hover, the shadow deepens to `0 4px 12px rgba(17, 20, 50, 0.12)`. The card contains a book cover image at 2:3 aspect ratio with rounded top corners, followed by the book title in serif, author name in muted sans-serif, and price.

**`product-card-image`** — The book cover area within a product card. Rounded at the top corners only, maintaining a sharp bottom edge where it meets the metadata. Aspect ratio is locked at 2:3 (standard book proportions).

### Navigation
**`nav-bar`** — A 64px white navigation bar with a subtle bottom hairline (`{colors.hairline-soft}`). Contains the Princeton University Press logo, main navigation links in `{typography.nav-link}`, and a search icon. When sticky, gains a light shadow. Active nav links show a 2px periwinkle bottom border.

**`nav-dropdown`** — A floating dropdown panel for sub-navigation. White background with 8px rounding and a substantial shadow (`0 4px 16px rgba(17, 20, 50, 0.12)`). Contains category links and featured content.

**`breadcrumb`** — A secondary navigation pattern using 12px caption text in muted gray. The active (current page) breadcrumb uses ink color. Separators are hairline-colored with 8px horizontal margin.

### Forms
**`text-input`** — A standard text input with white background, 44px height, 12px 16px padding, and a hairline border. On focus, gains a 2px periwinkle border with no outline. Error state uses a red border (`{colors.error}`). Used for email signups, search, and form fields.

**`search-bar`** — A dedicated search input with 8px rounding and 48px height. Slightly larger than standard inputs to accommodate the search icon and placeholder text. On focus, the border becomes 2px periwinkle.

### Badges
**`badge-new`** — A small magenta badge (`{colors.badge-new}`) with white uppercase text. Used to flag newly published titles. 2px 8px padding with 2px rounding.

**`badge-sale`** — An amber badge (`{colors.badge-sale}`) with dark ink text. Used for discounted titles and special offers. Same dimensions as `badge-new`.

**`badge-subject`** — A pill-shaped category tag with soft lavender background and muted text. Used for subject-area filtering and taxonomy labels. 4px 12px padding with full rounding.

### Hero
**`hero-banner`** — A full-width hero section with soft lavender background (`{colors.surface-soft}`) and large serif display text. Used for featured titles, series launches, and seasonal promotions. The `hero-banner-featured` variant uses a warm cream background (`{colors.surface-warm}`) for editorial content.

### Footer
**`footer-section`** — A dark navy footer (`{colors.footer-bg}`) with lavender-tinged gray text. Contains link columns, social icons, and copyright information. Links lighten to white on hover. Padding is 48px top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to 24px; search bar becomes full-width; footer links stack |
| Tablet | 744–1128px | Two-column product grid; nav links condense; hero maintains 28px text; sidebar filters become horizontal chips; footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero at 36px; sidebar filters visible; footer uses 4-column layout |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero centered with max-width; additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Category chips are minimum 40px tall with 16px horizontal padding
- Product cards have full-area tap targets (no small hit areas)
- Nav hamburger icon is 48px × 48px tap area
- Search icon in nav is 44px × 44px tap area

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Category filter strip becomes a horizontal scrollable row below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1
- Footer link columns collapse to single column below 744px
- Hero banner reduces font size and padding below 744px
- Breadcrumbs truncate with ellipsis on mobile (show last 2 levels)
- Sidebar filters become a collapsible accordion below 1128px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font family declarations could not be reliably extracted from the live site; the serif (Source Serif Pro) and sans-serif (Inter) choices are inferred from common academic publishing patterns and should be verified against the brand's actual typeface selection
- Hover and active states for most components are inferred from common patterns; actual brand-specific transitions and animations are unknown
- Error state styling for forms (error messages, validation icons) could not be extracted
- Dark mode or high-contrast mode styling is not present in the extracted data
- Sub-brand or series-specific color palettes (e.g., Princeton Science Library, Bollingen Series) could not be identified
- The extracted color list includes many generic web colors (grays, blues) that may not all be part of the intentional design system; the most distinctive colors (#3c4fe0, #ff9326, #aa1177, #111432) are likely brand-specific
- Button hover states, focus rings, and transition durations are not available from the extraction
- The extracted color #337ab7 is likely a default Bootstrap link color and should be verified before use
- Social media icon colors and hover states are not included in the extraction
- Loading states, skeleton screens, and empty states are not documented
- Print styles and PDF export formatting are unknown
- The checkout flow (if using a third-party provider) may have its own styling that overrides the brand system
