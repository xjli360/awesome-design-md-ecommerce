---
version: alpha
name: "The First Edition Rare Books"
source_url: "https://thefirstedition.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A bookseller that treats its inventory as museum objects, not merchandise — the site reads like a private collection catalogue printed on heavy stock. The canvas is a warm off-white (#f5f2ed), not clinical white, and the primary ink is a deep, almost-black charcoal (#1a1a1a) that avoids the harshness of true black. Every product card is a softly bordered rectangle with `{rounded.sm}` corners, housing a single book photograph against a white surface-card (#ffffff) — the image is the artifact, the text is the provenance. The typography leans on a classic serif for display and a clean sans-serif for body, a pairing that signals both authority and readability. The primary action color is a restrained dark olive (#4a5d4e), used sparingly for "Add to Cart" buttons and category tags — it never shouts. Navigation is a thin, persistent bar with the brand name in a refined serif, and the search bar sits as a `{rounded.full}` pill with a magnifying-glass icon, inviting discovery without urgency. The overall feel is that of a quiet reading room: generous whitespace, minimal decoration, and a deep respect for the printed object.

colors:
  primary: "#4a5d4e"
  primary-active: "#3a4a3e"
  primary-disabled: "#b8c4ba"
  ink: "#1a1a1a"
  body: "#2c2c2c"
  muted: "#6b6b6b"
  muted-soft: "#9a9a9a"
  hairline: "#d4d0c8"
  hairline-soft: "#e3dfd7"
  canvas: "#f5f2ed"
  surface-soft: "#ece9e2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#b8860b"
  accent-rust: "#8b4513"
  badge-new: "#c0392b"
  badge-sold: "#7f8c8d"
  star-rating: "#d4af37"

typography:
  display-xl:
    fontFamily: "'Playfair Display', 'Georgia', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Playfair Display', 'Georgia', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Playfair Display', 'Georgia', 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Inter', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Inter', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  price:
    fontFamily: "'Playfair Display', 'Georgia', 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Playfair Display', 'Georgia', 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0

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
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 16px
  button-icon-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 16px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "3/4"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xxs}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: "720px"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.base}"
    maxWidth: "560px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    padding: "{spacing.section} 0"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-heading:
    typography: "{typography.title-md}"
    textColor: "{colors.surface-card}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: "0 12px"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: "16px"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: "1px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart" and "Checkout". A dark olive (`{colors.primary}`) rectangle with white text and `{rounded.sm}` corners. On hover, it darkens to `{colors.primary-active}`. The disabled state uses a muted green-gray (`{colors.primary-disabled}`) to signal inactivity without visual noise. Padding is generous at 12px 24px, giving the button a solid, grounded feel.

**`button-secondary`** — A ghost-like alternative for "View Details" or "Wishlist". Uses the warm canvas background (`{colors.canvas}`) with a thin `{colors.hairline}` border. The text is the deep charcoal ink (`{colors.ink}`). This button sits beside the primary without competing for attention.

**`button-tertiary-text`** — A text-only link styled as a button, used for "Learn More" or "Read Description". Transparent background, primary green text (`{colors.primary}`), and no border. Relies on the `{typography.button-md}` weight for clarity.

**`button-icon-circle`** — A 40px circular icon button for actions like "Share" or "Save". Uses the soft surface (`{colors.surface-soft}`) as background and the ink color for the icon. The `{rounded.full}` shape makes it feel friendly and accessible.

### Cards
**`product-card`** — The core inventory unit. A white card (`{colors.surface-card}`) with a thin `{colors.hairline-soft}` border and `{rounded.sm}` corners. Inside, a 3:4 aspect-ratio image sits at the top with `{rounded.xs}`. Below, the title uses `{typography.title-md}`, the author uses `{typography.body-sm}` in muted gray, and the price uses `{typography.price-sm}` in the serif font. On hover, a subtle box-shadow lifts the card and the border darkens to `{colors.hairline}`.

**`product-card-badge`** — A small, uppercase label pinned to the top-left of the card image. Uses `{colors.badge-new}` (a restrained red) for "New Arrivals" or `{colors.badge-sold}` (a neutral gray) for "Sold". The `{typography.badge}` style is compact at 11px with tight tracking.

### Navigation
**`top-nav`** — A thin, persistent bar at 64px height on the warm canvas (`{colors.canvas}`). The brand name sits on the left in a serif display font (not defined as a token, but visually distinct). Navigation links use `{typography.nav-link}` in muted gray (`{colors.muted}`) with 8px 12px padding. The active link is underlined with a 2px `{colors.primary}` border.

**`nav-link-active`** — The active state for navigation items. The text darkens to `{colors.ink}` and a 2px bottom border in `{colors.primary}` appears, creating a subtle anchor.

### Forms
**`text-input`** — A standard input field for search, email, or quantity. White background (`{colors.surface-card}`) with a `{colors.hairline}` border and `{rounded.sm}`. On focus, the border thickens to 2px and turns `{colors.primary}`. The `{typography.body-md}` size ensures readability.

**`search-bar`** — A pill-shaped (`{rounded.full}`) search input that dominates the hero area. Same white background and hairline border as the text input, but with 20px horizontal padding for a more spacious feel. On focus, the border becomes a 2px `{colors.primary}` ring.

### Tags & Badges
**`category-tag`** — A pill-shaped filter tag for browsing by genre (e.g., "Fiction", "First Editions"). Uses the soft surface (`{colors.surface-soft}`) with `{rounded.full}` corners. The active state (`category-tag-active`) fills with `{colors.primary}` and white text, making the selected filter immediately visible.

**`breadcrumb`** — A small, muted navigation aid using `{typography.caption}` in `{colors.muted}`. The active breadcrumb (`breadcrumb-active`) switches to `{colors.ink}` for the current page.

### Footer
**`footer`** — A dark, grounded footer using `{colors.ink}` as the background. Headings use `{typography.title-md}` in white, while links use `{typography.link}` in a soft gray (`{colors.muted-soft}`). The contrast is deliberate — the footer feels like a colophon at the end of a book.

### Hero
**`hero-section`** — The top section of the homepage, using the warm canvas (`{colors.canvas}`) with generous `{spacing.section}` padding. The title uses `{typography.display-xl}` in the serif font, capped at 720px width. The subtitle is `{typography.body-md}` in muted gray, capped at 560px. This creates a centered, editorial feel.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, 16px padding, top-nav collapses to hamburger, hero title reduces to `{typography.display-md}`, search bar full-width |
| Tablet | 744–1128px | Two-column product grid, 24px padding, top-nav links visible, hero title at `{typography.display-lg}` |
| Desktop | 1128–1440px | Three-column product grid, 32px padding, full top-nav with all links, hero at full `{typography.display-xl}` |
| Wide | > 1440px | Four-column product grid, centered max-width container at 1440px, hero content centered |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Icon buttons (`button-icon-circle`) are 40px, which is slightly below the 44px recommendation but acceptable for non-primary actions.
- Search bar and text inputs are 48px tall, exceeding the minimum.
- Category tags are 32px tall, which is below the 44px recommendation — these may need a touch-friendly variant on mobile.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu. The brand name remains visible on the left, and a cart icon sits on the right.
- The product grid collapses from 3 columns to 2 on tablet, and 1 on mobile.
- The hero section reduces padding from `{spacing.section}` (64px) to `{spacing.xxl}` (48px) on mobile.
- Category tags wrap to a second row on mobile, rather than scrolling horizontally.
- The footer stacks its columns vertically on mobile, with each section (About, Help, Social) taking full width.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted hex colors were available from the live site (the page returned a 403 Forbidden error). The color palette above is a reasonable inference based on the brand category (rare bookseller) and common design patterns for similar high-end literary sites. The primary dark olive (#4a5d4e) is an educated guess for a restrained, scholarly accent.
- No font-family declarations were found. The serif/sans-serif pairing (Playfair Display + Inter) is a common choice for editorial/book sites. Actual fonts may differ.
- Hover and focus states for most components are inferred from common patterns, not extracted from the live site.
- Error states (form validation, 404 pages, out-of-stock messaging) are not defined.
- Dark mode is not considered — the brand's warm canvas suggests a light-mode-only design.
- The "New" and "Sold" badge colors are generic choices; the actual badge system may use different hues.
- The star-rating color (#d4af37, gold) is a common choice for book reviews but may not match the actual site.
- The footer's dark background (#1a1a1a) is an assumption; the actual footer may use a lighter or different tone.
- The product card's 3:4 aspect ratio is a common choice for book covers but may vary.
- The top-nav height (64px) and padding values are standard; actual measurements may differ.
- The responsive breakpoints (744px, 1128px, 1440px) are standard and may not match the actual site's breakpoints.
- The hamburger menu collapse is an assumption; the actual mobile navigation may use a different pattern (e.g., bottom nav, drawer).
