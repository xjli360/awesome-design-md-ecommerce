---
version: alpha
name: "The Drama Book Shop"
source_url: "https://www.dramabookshop.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep teal storefront — `#003e51` — that feels like a proscenium arch rendered in ink, not paint. The Drama Book Shop doesn't shout "theatre" with marquee bulbs or crimson velvet; it signals through a hushed, scholarly palette of teal (`#335f72`), pale aqua (`#d6e9ee`), and warm gray (`#dedede`) on a near-black body (`#121212`). American Typewriter, the brand's primary face, carries the weight of printed playbills and typeset scripts — its slab serifs and uneven letterforms evoke the tactile authority of a Broadway program. Buttons are softly rounded (`{rounded.sm}`) and filled with the primary teal, while secondary actions sit in the pale aqua or the light gray, keeping the interface calm and legible. The site reads as a quiet, knowledgeable companion — a bookstore that trusts its inventory and its audience's literacy, not flashy merchandising. White space (`{spacing.section}`) between sections gives each book, event, and resource room to breathe, and the consistent use of `{rounded.md}` on cards and `{rounded.full}` on search inputs maintains a gentle, approachable edge. There is no gratuitous ornament; every design decision serves the text.

colors:
  primary: "#003e51"
  primary-active: "#002c3a"
  primary-disabled: "#809ba8"
  ink: "#121212"
  body: "#335f72"
  muted: "#809ba8"
  muted-soft: "#a3bcc9"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-aqua: "#d6e9ee"
  accent-warm-gray: "#dedede"

typography:
  display-xl:
    fontFamily: "'American Typewriter', 'American Typewriter Bold', 'Courier New', monospace"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'American Typewriter', 'American Typewriter Bold', 'Courier New', monospace"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "'American Typewriter', 'American Typewriter Bold', 'Courier New', monospace"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'American Typewriter', 'American Typewriter Bold', 'Courier New', monospace"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica', 'Jost', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica', 'Jost', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica', 'Jost', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'American Typewriter', 'American Typewriter Bold', 'Courier New', monospace"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'American Typewriter', 'American Typewriter Bold', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'Helvetica', 'Jost', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'American Typewriter', 'American Typewriter Bold', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Helvetica', 'Jost', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    backgroundColor: "{colors.accent-aqua}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-tertiary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
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
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-aqua}"
    marginTop: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-aqua}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.accent-aqua}"
    typography: "{typography.link}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with `{colors.primary}` teal and set in American Typewriter at 15px with 0.5px letter spacing. On hover, it shifts to `{colors.primary-active}` (`#002c3a`). The disabled state uses `{colors.primary-disabled}` (`#809ba8`). Padding is 12px vertical, 24px horizontal, with `{rounded.sm}` corners.

**`button-secondary`** — An alternative action using the pale aqua `{colors.accent-aqua}` background with teal text. Same dimensions and typography as the primary button. Used for "Add to Cart" alternatives, secondary CTAs in hero sections, or event RSVPs.

**`button-tertiary`** — A text-based button with a 1px `{colors.hairline}` border on a white background. Teal text, same typography. Used for "Learn More" or "View Details" links that need less visual weight.

### Cards
**`product-card`** — A white card with `{rounded.md}` corners and 16px padding. The product image sits at the top with `{rounded.sm}` corners. Below it, the title uses `{typography.title-md}` and the price uses `{typography.body-sm}` in `{colors.body}`. Cards stack in a responsive grid with `{spacing.base}` gaps.

**`product-card-image`** — The image within a product card, cropped to a consistent aspect ratio (typically 3:4 for books) with `{rounded.sm}` corners and `object-fit: contain` as extracted from the site.

### Navigation
**`nav-bar`** — A 64px white bar with a 1px `{colors.hairline}` bottom border. Navigation links use `{typography.nav-link}` (American Typewriter, 14px, 600 weight, 0.5px letter spacing). The active link is underlined with a 2px `{colors.primary}` border and the text color changes to `{colors.primary}`.

### Hero
**`hero-section`** — A full-width teal section (`{colors.primary}`) with white text. The main headline uses `{typography.display-xl}` (36px American Typewriter Bold). A subtitle below uses `{typography.body-md}` in `{colors.accent-aqua}`. Vertical padding is `{spacing.section}` (64px), horizontal padding is `{spacing.xl}` (32px).

### Search
**`search-bar`** — A pill-shaped input (`{rounded.full}`) with white background and 1px `{colors.hairline}` border. On focus, the border becomes 2px `{colors.primary}`. Typography is `{typography.body-md}` (Helvetica, 16px). Height is 48px with 12px vertical and 20px horizontal padding.

### Badges
**`badge-new`** — A small teal badge (`{colors.primary}`) with white text, `{rounded.xs}` corners, and 2px vertical / 8px horizontal padding. Uses `{typography.badge}` (11px Helvetica, uppercase, 700 weight, 0.5px letter spacing). Used for "New Arrival" or "Just In" labels.

**`badge-sale`** — A pale aqua badge (`{colors.accent-aqua}`) with teal text. Same dimensions and typography as the new badge. Used for "Sale" or "Discount" labels.

### Footer
**`footer-section`** — A full-width teal section (`{colors.primary}`) with white text and `{typography.body-sm}`. Links within the footer use `{colors.accent-aqua}` and `{typography.link}`. Padding is `{spacing.section}` vertical and `{spacing.xl}` horizontal.

### Section Headers
**`section-header`** — A display-level heading using `{typography.display-md}` (28px American Typewriter Bold) in `{colors.ink}`. Bottom margin is `{spacing.lg}` (24px). Used to introduce product categories, events, or featured collections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu. Product cards stack in single column. Hero text reduces to `{typography.display-md}`. Search bar becomes full-width. Footer links stack vertically. |
| Tablet | 744–1128px | Nav links remain visible but condensed. Product cards display in 2-column grid. Hero retains `{typography.display-xl}` but with reduced horizontal padding. |
| Desktop | 1128–1440px | Full nav bar with all links. Product cards in 3-column grid. Hero at full width with `{spacing.section}` padding. Sidebar or featured collections visible. |
| Wide | > 1440px | Maximum content width capped at 1440px with centered layout. Additional whitespace on sides. Product cards may expand to 4-column grid. |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Search bar is 48px tall, exceeding the 44px minimum.
- Nav links have a minimum 48px tap area (height of nav bar).
- Product cards have a minimum 48px tap area for the entire card as a link.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer.
- The search bar collapses from a full input with placeholder text to an icon-only button that expands on tap.
- Product grids collapse from 3 or 4 columns to 2 columns on tablet and 1 column on mobile.
- Footer link columns collapse from 4 columns to 2 columns on tablet and 1 column on mobile.
- Hero sections reduce vertical padding from `{spacing.section}` to `{spacing.xxl}` on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components (buttons, links, inputs) could not be reliably extracted from the live site. The `primary-active` color (`#002c3a`) is an inferred darker shade of the primary, not a confirmed extracted value.
- Error styling for form inputs (validation messages, error borders) was not observed.
- The exact font weights used for American Typewriter (e.g., 400, 600, 700) are inferred from common web usage; the extracted CSS only showed "American Typewriter" and "American Typewriter Bold" without numeric weights.
- The secondary font stack (`Helvetica`, `Jost`) was extracted but the specific usage contexts (body vs. headings) are inferred from common design patterns.
- Dark mode styling is not present on the live site.
- Sub-brand or seasonal color palettes (e.g., holiday promotions, event-specific themes) were not extracted.
- The extracted color list is relatively small (5 colors) and may not represent the full design system. The teal (`#003e51`) is the most distinctive and is treated as primary, but the brand may use additional accent colors not captured.
- Shopify-specific widget colors (checkout buttons, payment badges) were filtered out but may have been mixed with brand colors in the extraction.
- The `object-fit: contain` declaration was extracted but its specific application (product images, hero images) is inferred.
