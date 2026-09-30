---
version: alpha
name: "Better World Books"
source_url: "https://www.betterworldbooks.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A used-book marketplace that wears its mission on its sleeve — literally, in the #baf0c6 mint-green badge that signals "carbon-balanced shipping" on every eligible product card, a color that appears nowhere else in the system and reads like a breath of fresh air against the otherwise serious #444444 and #313131 dark-ink text blocks. The brand leans into a library-like trustworthiness: deep navy #044573 anchors the top navigation and footer, while a single red #f11e28 accent — used sparingly for sale prices and donation-badge highlights — provides the only moment of urgency in an otherwise calm, low-contrast palette. The typography stack pairs the geometric clarity of Poppins (headings) with the sturdy readability of Zilla Slab (body), a serif+sans-serif combination that signals both academic credibility and approachability. Product cards use soft `{rounded.sm}` corners and generous `{spacing.base}` padding, with the book cover image doing most of the emotional work — the UI steps back. The search bar is a wide, pill-shaped `{rounded.full}` field in #f5f5f5, and the primary CTA ("Add to Cart") sits in #044573 with white text, a button that feels solid but never pushy. The overall mood is that of a well-lit independent bookstore: warm grays, clean whites, one bold accent, and a quiet confidence that the product — and the mission — will speak for itself.

colors:
  primary: "#044573"
  primary-active: "#00335a"
  primary-disabled: "#8baac4"
  ink: "#444444"
  body: "#313131"
  muted: "#4d4d4d"
  muted-soft: "#aaaaaa"
  hairline: "#eeeeee"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#baf0c6"
  accent-red: "#f11e28"
  accent-red-soft: "#fce4e5"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Poppins', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'Poppins', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Zilla Slab', 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Zilla Slab', 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Poppins', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Zilla Slab', 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Poppins', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
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
    border: 2px solid "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: 2px solid "{colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  text-input-error:
    border: 2px solid "{colors.accent-red}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: 2px solid "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-bar-link-hover:
    textColor: "{colors.accent-green}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 32px 24px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  badge-carbon-balanced:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-donation:
    backgroundColor: "{colors.accent-red-soft}"
    textColor: "{colors.accent-red}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 48px 24px
  category-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  category-link-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
  book-price:
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
  book-price-sale:
    textColor: "{colors.accent-red}"
    typography: "{typography.title-md}"
  book-original-price:
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    textDecoration: line-through

## Components

### Buttons
**`button-primary`** — The primary call to action across the site, used for "Add to Cart", "Checkout", and "Sign Up". Rendered in deep navy `{colors.primary}` with white text and `{rounded.sm}` corners. On hover, shifts to `{colors.primary-active}`. Disabled state uses `{colors.primary-disabled}` with white text, signaling the action is unavailable without visual noise. Height is 44px with 12px vertical padding and 24px horizontal padding, creating a solid, readable button that doesn't overwhelm the card layout.

**`button-secondary`** — An outlined variant used for "Learn More", "View Details", and secondary checkout actions. White background with a 2px `{colors.primary}` border and navy text. On hover, the border deepens to `{colors.primary-active}` and the background shifts to `{colors.surface-soft}`. Same dimensions as `button-primary` for consistent alignment in button groups.

**`button-ghost`** — A text-only button for tertiary actions like "Cancel" or "Remove". Transparent background with `{colors.primary}` text. On hover, a subtle background tint may be applied (not extracted). Same padding and height as other buttons to maintain vertical rhythm.

**`button-accent-red`** — Used exclusively for high-urgency actions like "Clearance Sale" or limited-time offers. Solid `{colors.accent-red}` background with white text. Same dimensions as `button-primary`. This button should be used sparingly — once per page maximum — to preserve its urgency signal.

### Cards
**`product-card`** — The core product display unit, used for every book listing. White background with `{rounded.sm}` corners and 12px padding. The book cover image sits at the top, followed by title (using `{typography.title-md}`), author (using `{typography.body-sm}` in `{colors.muted}`), and price (using `{typography.title-md}` in `{colors.ink}`). On hover, a subtle box shadow lifts the card. Badges for carbon-balanced shipping (`{badge-carbon-balanced}`) or sale pricing (`{badge-sale}`) sit in the top-left corner of the image area.

### Navigation
**`nav-bar`** — The persistent top navigation bar, rendered in `{colors.primary}` at 64px height. Logo sits left-aligned, with nav links using `{typography.nav-link}` in white. On hover, links shift to `{colors.accent-green}`. The search bar (`{search-bar}`) is centered or right-aligned, using a pill shape in `{colors.surface-soft}`. On mobile, the nav collapses into a hamburger menu.

**`footer`** — A full-width footer in `{colors.primary}` with white text. Contains links, mission statements, and social proof. Uses `{typography.body-sm}` for link text and `{typography.caption}` for section headers. Padding is 32px vertical, 24px horizontal.

### Forms
**`text-input`** — Standard text input for search, login, and checkout forms. White background, `{rounded.sm}` corners, 1px `{colors.hairline}` border. On focus, the border thickens to 2px `{colors.primary}`. Error state uses 2px `{colors.accent-red}` border. Height is 44px with 10px vertical and 16px horizontal padding.

**`search-bar`** — The primary search input, distinct from standard text inputs. Uses a pill shape (`{rounded.full}`) with `{colors.surface-soft}` background. On focus, background shifts to white and a 2px `{colors.primary}` border appears. Height is 48px with 12px vertical and 20px horizontal padding.

### Badges
**`badge-carbon-balanced`** — A small, mint-green badge (`{colors.accent-green}`) with dark text (`{colors.ink}`) indicating carbon-balanced shipping. Uses `{typography.badge}` with `{rounded.xs}` corners and 2px vertical, 8px horizontal padding. This is the brand's most distinctive visual signal — a splash of green in an otherwise navy-and-gray system.

**`badge-sale`** — A red badge (`{colors.accent-red}`) with white text for sale pricing. Same dimensions as `badge-carbon-balanced`. Used on product cards and category pages.

**`badge-donation`** — A soft red badge (`{colors.accent-red-soft}`) with `{colors.accent-red}` text for donation-linked purchases. Same dimensions as other badges.

### Hero
**`hero-section`** — The full-width hero area on the homepage and category landing pages. Uses `{colors.surface-soft}` background with `{colors.ink}` text. The heading uses `{typography.display-xl}` with 48px vertical padding. A subheading in `{typography.body-md}` sits below, followed by a `{button-primary}` CTA. The hero may feature a background image or illustration, but the text overlay always maintains readability against the soft gray canvas.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero padding reduces to 32px; search bar moves below logo; footer links stack vertically |
| Tablet | 744–1128px | Nav links visible but condensed; product cards in 2-column grid; hero uses 40px padding; search bar remains in nav |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-4 column grid; hero at 48px padding; search bar centered in nav |
| Wide | > 1440px | Max-width container (1440px) centered; product cards in 4-5 column grid; hero may feature full-bleed imagery |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have 8px vertical padding within the 64px nav bar, ensuring 44px+ tap targets
- Search bar at 48px height exceeds the 44px minimum
- Product card images are tappable as a single unit, with the entire card area as the hit target
- Badges are informational only and not interactive

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger icon with a slide-out drawer
- Secondary nav links (categories) collapse into a horizontal scrollable strip or a "Categories" dropdown
- Product filters collapse into a "Filter" button that opens a modal or bottom sheet
- Footer link columns collapse into accordion-style sections
- The hero section reduces vertical padding and may hide secondary text

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for `button-ghost` and `badge` components were not reliably extracted from the live site; assumed standard opacity or background shifts
- Error styling for form validation (error messages, iconography) was not observed; placeholder assumes red border only
- Active/visited states for `link` and `nav-link` components were not extracted; defaults assumed
- Sub-brand or seasonal color palettes (e.g., holiday promotions, genre-specific themes) were not observed
- Dark mode is not implemented on the live site; no dark-mode tokens exist
- The `accent-red` usage frequency and exact placement rules were inferred from limited page views; the brand may use it more or less aggressively
- Font weights beyond 400, 500, 600, and 700 were not observed; variable font axes may exist but were not extracted
- Animation and transition timing values (ease, duration) were not extracted; standard 200-300ms ease-in-out assumed
- The `accent-green` badge may have a hover state or tooltip on desktop; not observed
- Checkout flow components (payment forms, address inputs) were not fully extracted; may use Shopify or third-party widget styling that differs from the brand system
