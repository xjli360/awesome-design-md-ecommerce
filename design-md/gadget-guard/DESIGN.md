---
version: alpha
name: "Gadget Guard"
source_url: "https://www.gadgetguard.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A protective accessories brand that builds its visual identity around a sharp orange accent (#ff5501) — the color of a warning cone, a safety vest, the glow of a phone in low battery — set against a nearly monochrome field of grays (#d1d1d1, #7d7d7d, #c2c2c2, #e2e2e2, #f0f0f0, #f9f9f9, #f2f2f2, #e5e5e5, #f6f6f6) that reads as industrial restraint rather than premium minimalism. The palette is dominated by a cool silver-gray spectrum with a secondary blue (#006bb4, #1979c3, #499bf8) that appears in links and secondary actions, while the orange (#ff5501, #e65525, #ee5513) is reserved exclusively for primary CTAs, sale badges, and urgency signals — a single voltage that cuts through the gray like a hazard light. The typography stack relies on acumin-pro as the primary brand face, a clean geometric sans-serif with moderate contrast, paired with Open Sans as a web-fallback and Helvetica Neue for system-level consistency. Rounded corners are minimal — the system uses {rounded.sm} (8px) for buttons and cards, {rounded.md} (12px) for modals, and {rounded.full} only for badge pills and search fields, preserving a functional, slightly industrial feel that matches the product category (screen protectors, cases, cables). The canvas is near-white (#fcfcfc) with surface cards in pure white (#ffffff) and hairline borders in #e8e8e8, creating a clean but not sterile layout. The brand's design language prioritizes clarity and trust over warmth — there is no soft gradient, no playful illustration, no decorative flourish. Every element earns its place through utility, and the orange acts as a single point of visual urgency that guides the user through purchase decisions.

colors:
  primary: "#ff5501"
  primary-active: "#e65525"
  primary-disabled: "#fdf0d5"
  ink: "#1a1a1a"
  body: "#303030"
  muted: "#555555"
  muted-soft: "#7d7d7d"
  hairline: "#e8e8e8"
  hairline-soft: "#f2f2f2"
  canvas: "#fcfcfc"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link-blue: "#006bb4"
  link-blue-hover: "#1979c3"
  accent-blue: "#499bf8"
  badge-sale: "#ff5501"
  badge-new: "#006bb4"
  star-rating: "#c07600"
  star-rating-empty: "#d1d1d1"
  error: "#e65525"
  success: "#1979c3"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'acumin-pro', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'acumin-pro', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'acumin-pro', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'acumin-pro', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'acumin-pro', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'acumin-pro', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'acumin-pro', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'acumin-pro', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'acumin-pro', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.25px
  badge:
    fontFamily: "'acumin-pro', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'acumin-pro', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'acumin-pro', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'acumin-pro', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  link:
    fontFamily: "'acumin-pro', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'acumin-pro', 'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.25px

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
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.muted}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.button-md}"
    padding: 8px 16px
  button-text-hover:
    backgroundColor: transparent
    textColor: "{colors.link-blue-hover}"
    typography: "{typography.button-md}"
    padding: 8px 16px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
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
    border: "2px solid {colors.link-blue}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
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
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.muted-soft}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  product-card-rating:
    typography: "{typography.caption-sm}"
    padding: "0 {spacing.base} {spacing.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "2px solid {colors.link-blue}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
    border: "1px solid {colors.hairline}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base}"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  modal-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    boxShadow: "0 4px 24px rgba(0,0,0,0.12)"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's signature orange (#ff5501) with white text. Used for "Add to Cart", "Buy Now", and "Shop Sale" actions. On hover, shifts to a deeper orange (#e65525). Disabled state uses a pale peach (#fdf0d5) with muted text, signaling the action is unavailable without visual noise. Height is 48px with 12px vertical padding and 24px horizontal, giving a substantial but not oversized tap target.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "Compare". Uses a white background with a 2px hairline border (#e8e8e8) and dark text (#1a1a1a). On hover, the background shifts to surface-soft (#f6f6f6) and the border darkens to muted (#555555). Same 48px height as primary for alignment in form layouts.

**`button-text`** — A text-only button used for inline actions like "View Details" or "Cancel". Renders in link-blue (#006bb4) with no background or border. On hover, shifts to a deeper blue (#1979c3). Padding is 8px vertical, 16px horizontal for comfortable touch spacing without visual weight.

**`button-pill-primary`** — A pill-shaped variant of the primary button, used for sale badges, filter tags, and compact CTAs. Uses {rounded.full} for the pill shape, 40px height, and the same orange/white color scheme. The pill form signals a more casual, promotional interaction compared to the standard rectangular button.

**`button-pill-outline`** — An outlined pill button for filter tags and category selectors. White background with a 1px hairline border and dark text. Used in product listing filters and search refinement panels where multiple selections are possible.

### Text Inputs & Forms
**`text-input`** — Standard text input for search, email signup, and checkout forms. White background with a 1px hairline border (#e8e8e8) and 12px padding. On focus, the border thickens to 2px and shifts to link-blue (#006bb4), providing a clear focus indicator without relying on outline. Error state uses a 2px orange border (#e65525) to match the brand's urgency color.

**`select-input`** — Dropdown select for quantity, size, and product options. Matches the text-input styling with a white background, hairline border, and 48px height. The dropdown arrow is rendered in muted (#555555) to maintain the functional, no-frills aesthetic.

**`search-bar`** — The site search input uses a pill shape ({rounded.full}) with a surface-soft background (#f6f6f6) and hairline border. On focus, the border becomes 2px link-blue and the background shifts to white. The pill shape distinguishes search from form inputs, making it feel more exploratory and less transactional.

### Navigation
**`nav-bar`** — The primary navigation bar is 64px tall with a white background and a 1px hairline bottom border. Navigation links use 14px acumin-pro at 500 weight with 0.25px letter spacing. Active links are indicated by a 2px orange underline (#ff5501), while inactive links render in muted (#555555). The nav bar collapses to a hamburger menu on mobile.

**`nav-link-active`** — Active navigation state with a 2px orange bottom border (#ff5501) and full-opacity ink text (#1a1a1a). The orange underline is the only decorative element in the nav, consistent with the brand's minimal approach to visual hierarchy.

**`nav-link-inactive`** — Inactive navigation state with muted text (#555555) and no underline. On hover, the text shifts to full opacity ink (#1a1a1a) with a subtle transition.

### Product Cards
**`product-card`** — The core product display unit, used in grid and list views. A white card with a 1px hairline border (#e8e8e8) and {rounded.sm} corners. The card has no internal padding — the image fills the top with {rounded.sm} applied to the top corners only. Product title uses title-md (18px, 600 weight), price uses body-md (16px, 400 weight), and ratings use caption-sm (11px, 500 weight). On hover, the border shifts to muted-soft (#7d7d7d) and a subtle box shadow appears (0 2px 8px rgba(0,0,0,0.08)).

**`product-card-badge`** — Overlaid on the product image to indicate sales, new arrivals, or exclusive items. Uses the orange (#ff5501) for sale badges and link-blue (#006bb4) for new badges. Badges are pill-shaped ({rounded.full}) with uppercase 11px text at 700 weight and 0.5px letter spacing. Positioned at the top-left of the product image with 8px margin.

**`product-card-rating`** — Star rating display using a warm gold (#c07600) for filled stars and light gray (#d1d1d1) for empty stars. The numeric rating (e.g., "4.5") appears next to the stars in caption-sm. This is the only warm color outside the orange system, providing a subtle quality signal.

### Hero & Content Sections
**`hero-section`** — Full-width hero banners with a surface-soft background (#f6f6f6) and 64px vertical padding. The hero uses display-xl (36px, 700 weight) for headlines with -0.5px letter spacing for a slightly tighter, more editorial feel. The hero CTA button is 52px tall with 14px vertical padding and 32px horizontal, making it the largest button on the page.

**`accordion-header`** — Used for FAQ sections and product details. A white background with a 1px hairline bottom border and 16px padding. The header uses title-md (18px, 600 weight) with a chevron icon that rotates on open. No background change on hover — the interaction is signaled solely by the chevron rotation.

**`accordion-content`** — The expanded content area below each accordion header. Uses body-md (16px, 400 weight) with 16px padding. Content can include bullet lists, paragraphs, and specification tables. No border or background distinction from the header — the separation comes from the header's bottom border.

### Footer
**`footer`** — A dark footer with ink background (#1a1a1a) and muted-soft text (#7d7d7d). Links are rendered in muted-soft and shift to white on hover. The footer uses 48px vertical padding and 16px horizontal padding, with columns for product categories, support links, and legal information. No decorative elements — just text links and a copyright line.

### Modals & Overlays
**`modal-overlay`** — A semi-transparent black overlay (#000000 at 50% opacity) that appears behind modals and lightboxes. No blur effect — the brand keeps interactions simple and direct.

**`modal-card`** — The modal container with a white background, {rounded.md} corners (12px), and 32px padding. Uses a box shadow (0 4px 24px rgba(0,0,0,0.12)) for depth separation from the overlay. Used for quick-view product previews, size guides, and confirmation dialogs.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row), nav collapses to hamburger, hero text reduces to 24px, search bar moves to top of page, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, hero retains 28px text, sidebar filters become horizontal strip |
| Desktop | 1128–1440px | Three-column product grid, full nav with dropdowns, hero at 36px, sidebar filters visible, product cards show hover states |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero full-width with content constrained to 1200px |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px on mobile, with 48px preferred for primary actions.
- Product card tap targets (title, price, rating) are at least 44px tall with 8px padding between them.
- Nav hamburger icon is 44x44px with 12px padding inside the touch area.
- Filter chips and badge pills are 40px tall with 8px horizontal padding.
- Accordion headers are 48px tall with 16px padding for easy tapping.

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a full-screen overlay menu.
- Product filters collapse to a horizontal scrollable strip on tablet, and to a "Filter" button with a slide-out panel on mobile.
- Footer columns collapse to a single column on mobile, with accordion-style expandable sections for each category.
- Product image galleries collapse from thumbnail strip to swipeable dots on mobile.
- Hero sections reduce text size and remove secondary copy on mobile, keeping only the headline and primary CTA.
- Search bar collapses from a full-width input to an icon button that expands on tap.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is dominated by grays and blues with a single orange accent (#ff5501). While the orange appears to be the primary brand color, it's possible the brand uses a different accent color in marketing materials or seasonal campaigns that wasn't captured in the extraction.
- Font-family declarations included acumin-pro, Open Sans, and Helvetica Neue, but exact font weights, sizes, and line heights were not extracted from the live site. The typography scale above is reconstructed based on common e-commerce patterns and the brand's functional aesthetic.
- Hover, focus, and active states for all components are inferred from common patterns rather than extracted from the live site. The brand may use different transition durations, easing functions, or color shifts.
- Error, success, and warning states for forms and validation are not confirmed from the live site. The error color (#e65525) is assumed from the orange family, but the brand may use a different color for validation feedback.
- Dark mode support is not confirmed. The extracted palette suggests a light-mode-only design, but the brand may have a dark mode that wasn't captured.
- The brand's sub-brand or promotional color palettes (e.g., for specific product lines or seasonal campaigns) are not represented in the extracted data.
- Iconography style, illustration approach, and photography treatment were not extracted. The brand may use specific icon sets or image filters that affect the overall visual system.
- The extracted font list includes system fonts (Arial, Consolas, Courier New, Menlo, Monaco) that are likely fallbacks or code-specific, not brand fonts. The primary brand font is assumed to be acumin-pro based on its presence in the extracted list.
- The brand's Shopify platform status is marked as False, but the extracted colors include several that match Shopify's default palette (#1979c3, #499bf8). These may be from embedded widgets or a custom integration.
