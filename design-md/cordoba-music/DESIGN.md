---
version: alpha
name: "Cordoba Music"
source_url: "https://www.cordobaguitars.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A warm, wood-toned instrument maker whose visual identity leans on a near-monochrome palette of #777777, #555555, and #090909 — a restrained, workshop-like atmosphere where the product photography does the heavy lifting. The extracted palette reveals a site built on a foundation of #f5f5f5 canvas and #eeeeee surfaces, with #e7e7e7 and #d9d9d9 creating subtle depth through hairline separations. The brand's true accent is a muted #3c763d green, likely used for "In Stock" badges or add-to-cart affirmations, paired with #8a6d3b (a warm olive) and #31708f (a dusty teal) — colors that evoke wood grain, aged brass, and vintage instrument cases rather than digital-native brightness. The typography stack defaults to Arial and Helvetica across sans-serif declarations, with Consolas and Courier New appearing for technical specs (scale lengths, fret counts). The site reads as a catalog-first experience: generous product grids, soft card corners at {rounded.md}, and a navigation system that prioritizes instrument categories over brand storytelling. Error states borrow from Bootstrap's alert system (#a94442 red, #f2dede pink background), suggesting a pragmatic, off-the-shelf approach to form validation rather than custom-designed feedback. The overall mood is utilitarian but respectful — a digital showroom for luthier-crafted instruments that doesn't try to outshine the wood.

colors:
  primary: "#3c763d"
  primary-active: "#2b542c"
  primary-disabled: "#dff0d8"
  ink: "#090909"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#9d9d9d"
  hairline: "#e7e7e7"
  hairline-soft: "#eeeeee"
  canvas: "#f5f5f5"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-green: "#3c763d"
  badge-green-bg: "#dff0d8"
  badge-green-border: "#d6e9c6"
  badge-warning: "#8a6d3b"
  badge-warning-bg: "#fcf8e3"
  badge-warning-border: "#faebcc"
  badge-error: "#a94442"
  badge-error-bg: "#f2dede"
  badge-error-border: "#ebccd1"
  badge-info: "#31708f"
  badge-info-bg: "#d9edf7"
  badge-info-border: "#bce8f1"
  accent-teal: "#5bc0de"
  accent-orange: "#f0ad4e"
  accent-red: "#d9534f"
  accent-green: "#5cb85c"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.25px
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  tech-spec:
    fontFamily: "Consolas, 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "10px {spacing.md}"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.badge-error}"
    backgroundColor: "{colors.badge-error-bg}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "10px {spacing.md}"
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(9,9,9,0.08)"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 600
  badge-in-stock:
    backgroundColor: "{colors.badge-green-bg}"
    textColor: "{colors.badge-green}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.sm}"
    border: "1px solid {colors.badge-green-border}"
  badge-warning:
    backgroundColor: "{colors.badge-warning-bg}"
    textColor: "{colors.badge-warning}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.sm}"
    border: "1px solid {colors.badge-warning-border}"
  badge-error:
    backgroundColor: "{colors.badge-error-bg}"
    textColor: "{colors.badge-error}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.sm}"
    border: "1px solid {colors.badge-error-border}"
  badge-info:
    backgroundColor: "{colors.badge-info-bg}"
    textColor: "{colors.badge-info}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px {spacing.sm}"
    border: "1px solid {colors.badge-info-border}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px {spacing.lg}"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.surface-card}"
  tech-spec-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.tech-spec}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  tech-spec-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    fontWeight: 700
    textTransform: uppercase
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px {spacing.md}"
    height: 36px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px {spacing.md}"
    height: 36px
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    height: 40px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart" and checkout flows. Rendered on a {colors.primary} green background with white text at {typography.button-md} weight 600. Corners are softly squared at {rounded.sm}. On hover, shifts to {colors.primary-active} (#2b542c). Disabled state uses {colors.primary-disabled} (#dff0d8) with {colors.muted} text.

**`button-secondary`** — A bordered alternative for "View Details" or "Compare" actions. White background with {colors.ink} text and a 1px {colors.hairline} border. Active state fills the background with {colors.surface-soft} and darkens the border to {colors.muted}. Height matches the primary at 44px for alignment in form rows.

**`button-tertiary-text`** — A text-only link styled as a button, used for "Learn More" or "Cancel" actions. Transparent background with {colors.primary} green text. No border or padding — relies on the typography weight for affordance.

### Cards
**`product-card`** — The core content container for instrument listings. A white card with {rounded.md} corners, 1px {colors.hairline-soft} border, and 16px padding. On hover, the border strengthens to {colors.hairline} and a subtle 2px/8px shadow lifts the card. Title uses {typography.title-md} in {colors.ink}, price uses {typography.body-md} at weight 600 in {colors.primary}.

**`tech-spec-table`** — A monospaced data table for instrument specifications (scale length, nut width, fret count). Uses {typography.tech-spec} (Consolas/Courier New) for a workshop-manual feel. Header row uses {colors.surface-soft} background with uppercase {typography.caption-sm} at weight 700. The table sits inside a {rounded.sm} container with a {colors.hairline} border.

### Navigation
**`nav-bar`** — The top-level site navigation, 64px tall with white background and a single {colors.hairline} bottom border. Links use {typography.nav-link} at 15px weight 600, uppercase with 0.5px letter spacing. Active links gain a 2px {colors.primary} bottom border. Inactive links render in {colors.muted}.

**`filter-chip`** — Pill-shaped category filters for product listing pages. Rendered on {colors.surface-soft} with {colors.body} text at {typography.button-sm}. Active state inverts to {colors.primary} background with white text. Height is 36px with 6px vertical padding for a compact, tag-like appearance.

### Forms
**`text-input`** — Standard form input for search, checkout, and contact forms. White background, 44px height, {rounded.xs} corners, 1px {colors.hairline} border. Focus state swaps the border to {colors.primary}. Error state uses {colors.badge-error} border with {colors.badge-error-bg} background for clear validation feedback.

**`select-dropdown`** — Dropdown selectors for product options (size, finish, quantity). Matches the text-input dimensions and styling for visual consistency. Uses native browser dropdown affordance rather than a custom chevron.

### Badges
**`badge-in-stock`** — Green-on-green badge for availability indicators. Uses {colors.badge-green-bg} (#dff0d8) background with {colors.badge-green} (#3c763d) text and a {colors.badge-green-border} (#d6e9c6) outline. {rounded.xs} corners with 2px vertical padding. Three additional badge variants follow the same pattern: warning (olive), error (red), and info (teal).

### Hero
**`hero-section`** — Full-width promotional banner for new arrivals or featured collections. Uses {colors.canvas} background with {typography.display-xl} headline and a {colors.muted} subtitle. Section-level padding of 64px top/bottom with 24px sides. No background image or overlay — relies on product photography placed alongside.

### Search
**`search-bar`** — Full-width search input with pill-shaped {rounded.full} corners. White background, 48px height, 1px {colors.hairline} border. Placeholder text in {colors.muted} at {typography.body-md}. Positioned in the nav-bar on desktop, collapses to a full-screen overlay on mobile.

### Footer
**`footer`** — Site footer on {colors.ink} (#090909) background, creating a dramatic dark anchor at the bottom of every page. Text renders in {colors.muted-soft} (#9d9d9d) at {typography.body-sm}. Links hover to white ({colors.surface-card}). Section padding of 64px top/bottom.

### Pagination
**`pagination-button`** — Page-number buttons for product listing grids. White background, 40px height, {rounded.xs} corners, 1px {colors.hairline} border. Active page uses {colors.primary} fill with white text. Used at the bottom of category and search results pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger menu; product cards go single-column; hero section reduces to 32px padding; search bar becomes full-width overlay; filter chips stack vertically; tech-spec tables scroll horizontally |
| Tablet | 744–1128px | Product cards display in 2-column grid; nav-bar shows condensed category labels; hero uses 48px padding; filter chips wrap to 2 rows; search bar remains inline but narrower |
| Desktop | 1128–1440px | Product cards in 3-column grid; full nav-bar with all categories visible; hero at 64px padding; filter chips in single horizontal row; search bar at max 480px width |
| Wide | > 1440px | Product cards in 4-column grid; max-width container at 1440px; hero content centered with 80px padding; additional whitespace around product cards |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Filter chips at 36px height are below the 44px recommendation — consider increasing to 44px on mobile
- Nav-bar links have minimum 48px tap area (64px bar height provides adequate spacing)
- Search bar at 48px height meets touch target requirements
- Pagination buttons at 40px height — consider 44px on mobile for easier tapping

### Collapsing Strategy
- Primary navigation collapses to hamburger icon at < 744px, revealing a full-screen slide-in menu
- Product filters collapse into a "Filter" button that opens a modal overlay on mobile
- Tech-spec tables become horizontally scrollable on screens < 600px rather than collapsing
- Hero section reduces vertical padding from 64px to 32px on mobile, with headline scaling down proportionally
- Footer link columns stack vertically on mobile, with each category becoming an accordion section
- Search bar transforms from inline component to full-screen overlay with auto-focus on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is heavily polluted with Bootstrap alert colors (#3c763d, #8a6d3b, #a94442, #31708f) and framework defaults (#5cb85c, #5bc0de, #f0ad4e, #d9534f) — the brand's true primary may differ from the #3c763d green identified as most distinctive
- No font-family declarations beyond system stacks (Arial, Helvetica) were found — the brand may use a custom web font that wasn't loaded during extraction
- Hover and focus states for all components are inferred from common patterns, not extracted from live CSS
- Error message styling and form validation patterns are assumed from Bootstrap conventions rather than confirmed brand choices
- Dark mode or high-contrast mode variants are not documented — no extracted data supports them
- The brand's actual logo color, accent palette, and secondary brand colors could not be reliably extracted from the generic palette
- Button loading states, disabled secondary states, and icon-only button variants are not defined
- The extracted list includes social-icon colors and stock-image dominant tones that may not represent brand colors
- No spacing or grid system values could be extracted — the spacing scale is a reasonable default, not brand-specific
- The brand may use a different type scale for product-specific pages (e.g., larger model names, smaller spec details) that wasn't captured
