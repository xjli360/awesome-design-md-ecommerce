---
version: alpha
name: "Kamaka Hawaii"
source_url: "https://www.kamakahawaii.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A warm, sandalwood-scented brand built on a century of ukulele craft, anchored by the deep, sun-baked gold of #cbab63 — the color of aged koa wood and the brand’s primary voltage across headers, accents, and the signature Kamaka label. The palette draws from the Hawaiian landscape: #7c3f09 (rich earth), #6c2136 (volcanic wine), and #2f2f2f (lava rock) create a grounded, artisanal feel against a crisp white canvas. Typography runs Oswald for display — a condensed, confident sans-serif that nods to mid-century signage — paired with Work Sans for body, giving the site a clean, editorial rhythm. Product pages use generous whitespace and full-bleed hero imagery, with koa wood grain textures as visual anchors. Buttons are softly rounded (`{rounded.sm}`) and pill-shaped search bars (`{rounded.full}`) echo the curves of the instrument. The footer is a dense, information-rich grid of links and brand storytelling, with the Kamaka logo centered as a mark of provenance. The overall mood is one of quiet authority — not luxury, but the earned confidence of a family business that has shaped an instrument’s history for over 100 years.

colors:
  primary: "#cbab63"
  primary-active: "#b8944a"
  primary-disabled: "#e5d4a8"
  ink: "#2f2f2f"
  body: "#444444"
  muted: "#918c8c"
  muted-soft: "#b0acac"
  hairline: "#d4d4d4"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f8f6f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-earth: "#7c3f09"
  accent-wine: "#6c2136"
  accent-gold: "#f0b849"
  star-rating: "#cbab63"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Oswald', 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: 0.5px
  display-lg:
    fontFamily: "'Oswald', 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  display-md:
    fontFamily: "'Oswald', 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.2px
  display-sm:
    fontFamily: "'Oswald', 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  title-md:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Oswald', 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Oswald', 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Oswald', 'Work Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 400
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
    rounded: "{rounded.sm}"
    padding: 12px 28px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-pill-gold:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
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
  text-input-error:
    border: "2px solid {colors.accent-wine}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.accent-earth}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0 0 16px 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "12px 16px 4px 16px"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    padding: "0 16px 8px 16px"
  product-card-badge:
    backgroundColor: "{colors.accent-wine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    padding: "{spacing.base} 0"
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    color: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.canvas}"
    textTransform: uppercase
    letterSpacing: "1px"
  social-icon:
    color: "{colors.muted-soft}"
    size: 24px
  social-icon-hover:
    color: "{colors.primary}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.xl} 0 {spacing.base} 0"
  section-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    padding: "0 0 {spacing.lg} 0"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    padding: "{spacing.base} 0"
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  breadcrumb-link:
    typography: "{typography.caption-sm}"
    color: "{colors.muted}"
  breadcrumb-link-active:
    color: "{colors.ink}"
  breadcrumb-separator:
    color: "{colors.muted-soft}"
    padding: "0 {spacing.xs}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand gold `{colors.primary}` and white text set in Oswald uppercase. On hover, shifts to `{colors.primary-active}` for a subtle darkening. Disabled state uses `{colors.primary-disabled}` with reduced opacity. Used for "Add to Cart", "Shop Now", and primary form submissions.

**`button-secondary`** — An outlined variant with a `2px solid {colors.ink}` border on a white background. Hover fills with `{colors.ink}` and inverts text to white. Used for secondary actions like "Learn More" or "View Details".

**`button-tertiary-text`** — A text-only button with no background or border. Hover underlines or shifts color to `{colors.accent-earth}`. Used for "Read the Story" or "See All" links within content sections.

**`button-pill-gold`** — A fully rounded pill button using `{colors.primary}` background. Used for promotional badges, newsletter signup CTAs, and mobile sticky actions.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with a white background and subtle bottom border. Logo is left-aligned, nav links are centered or right-aligned in Oswald uppercase. On scroll, a drop shadow appears. Mobile collapses to a hamburger menu with a slide-in drawer.

**`nav-link-active`** — The active page link uses `{colors.primary}` to indicate current section. Hover state shifts to `{colors.accent-earth}` for warmth.

### Product Cards
**`product-card`** — A white card with `{rounded.md}` corners containing a 4:3 aspect ratio image and text below. The image has rounded top corners only. Title uses `{typography.title-sm}` in `{colors.ink}`, price uses `{typography.body-md}` in `{colors.primary}`. A `{colors.accent-wine}` badge can overlay the image for "New" or "Limited Edition" labels.

**`product-card-badge`** — A small, uppercase label overlaid on the product image, using `{colors.accent-wine}` background. Positioned top-left with `{rounded.xs}` corners.

### Forms
**`text-input`** — Standard text input with a `1px solid {colors.hairline}` border and `{rounded.sm}` corners. On focus, the border thickens to `2px solid {colors.primary}`. Error state uses `{colors.accent-wine}` border. Placeholder text uses `{colors.muted-soft}`.

### Search
**`search-bar-pill`** — A fully rounded pill-shaped search bar with a subtle border. On focus, the border switches to `{colors.primary}`. Used in the hero section and mobile search overlay.

### Footer
**`footer-section`** — A dark footer with `{colors.ink}` background and white text. Links are `{colors.muted-soft}` and hover to `{colors.primary}`. The footer is organized in a multi-column grid with headings in uppercase `{typography.title-sm}`. Social icons are 24px and hover to gold.

### Dividers & Sections
**`divider`** — A standard `1px` hairline used between sections. `{colors.hairline}` for strong separation, `{colors.hairline-soft}` for subtle grouping.

**`section-heading`** — Display-level heading in Oswald for major section titles. Paired with `section-subheading` in body weight for descriptive text below.

### Accordion
**`accordion-trigger`** — A clickable row with a bottom border, used for FAQs and product details. Content expands below with `{typography.body-sm}` in `{colors.body}`.

### Breadcrumbs & Pagination
**`breadcrumb-link`** — Small, muted links separated by a `{colors.muted-soft}` slash or chevron. Active page uses `{colors.ink}`.

**`pagination-button`** — Outlined square buttons for page navigation. Active page uses `{colors.primary}` fill with white text.

### Tags & Ratings
**`tag`** — Small, fully rounded pills with a soft background, used for filtering or categorizing products (e.g., "Soprano", "Concert", "Koa").

**`rating-stars`** — 16px star icons in `{colors.star-rating}` gold, used on product cards and reviews.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero text reduces to `{typography.display-md}`; search bar moves to a full-width overlay; footer grid becomes single column; buttons become full-width. |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards in 2-column grid; hero uses `{typography.display-lg}`; footer in 2-column grid. |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero uses `{typography.display-xl}`; footer in 4-column grid. |
| Wide | > 1440px | Content max-width at 1440px with centered layout; product cards in 4-column grid; hero section uses larger padding. |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility.
- Nav links have 48px tap targets on mobile.
- Search bar pill is 48px tall for easy tapping.
- Accordion triggers are 48px tall with generous padding.
- Pagination buttons are 44px x 44px minimum.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px.
- Product grid collapses from 4 columns to 3 to 2 to 1 as viewport shrinks.
- Footer grid collapses from 4 columns to 2 to 1.
- Hero section reduces font sizes and padding on mobile.
- Search bar becomes a full-screen overlay on mobile.
- Breadcrumbs hide on mobile, replaced by a "Back" button.
- Accordion content is collapsed by default on all viewports.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links were inferred from common patterns; exact transition durations and easing curves not extracted.
- Error styling for forms (colors, icons, messages) not observed on live site; `{colors.accent-wine}` used as a reasonable error color.
- Dark mode not implemented; no extracted data available.
- Sub-brand or product-line-specific color variations (e.g., limited edition finishes) not captured.
- Font weights for Oswald and Work Sans were estimated based on common usage; exact weights from live CSS not extracted.
- Spacing values for specific components (e.g., product card padding) were estimated from common e-commerce patterns.
- The extracted color list contains many framework and third-party widget colors (Shopify Pay, social icons, etc.). The true brand palette was inferred as the most distinctive and recurring colors: `#cbab63`, `#7c3f09`, `#6c2136`, `#2f2f2f`, `#918c8c`, `#444444`, `#eeeeee`, `#f0b849`, `#1e1f26`, `#382110`. The remaining colors (blues, pinks, greens) are likely from checkout widgets, social media icons, or stock imagery.
- No meta theme-color was found; mobile browser chrome color is unspecified.
- Animation and transition specifications (duration, easing, keyframes) not extracted.
- Focus ring styles (outline, offset, color) not observed.
- Modal and overlay styling (backdrop, close button, animation) not documented.
- Form validation states (success, warning) and associated icons not extracted.
- Loading states (spinners, skeleton screens) not observed.
- Error pages (404, 500) not captured.
