---
version: alpha
name: "City Lights"
source_url: "https://www.citylights.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A San Francisco independent bookstore that has been a literary anchor since 1953, City Lights presents itself online as a direct, no-frills portal to its physical shelves. The brand’s digital presence is dominated by a deep, intellectual navy (#1a2a3a) used for primary navigation, key headers, and the site’s persistent top bar, creating a sense of weight and permanence against a stark white canvas (#ffffff). There is no decorative imagery on the homepage; instead, the visual hierarchy is built entirely through typographic contrast and generous whitespace, with book covers providing the only color. The primary call-to-action buttons—used for adding items to a cart or searching the inventory—are rendered in a warm, muted brick red (#c0392b), a deliberate accent that feels pulled from a vintage bookbinding cloth rather than a digital interface. This red is the single point of warmth in an otherwise monochromatic system. Body text is set in a clean, readable serif (Georgia) at 16px, while navigation and headers use a geometric sans-serif (Montserrat) to signal a modern, curated sensibility. The search bar is a simple, unrounded rectangle (`{rounded.none}`) with a subtle hairline border (`{colors.hairline}`), emphasizing utility over ornament. Product cards for books are minimal: a cover image, the title in bold, the author in `{colors.muted}`, and the price—no ratings, no badges, no social proof. The design trusts the book itself to sell. Footer navigation is dense and text-heavy, reflecting the store’s role as a publisher and cultural institution, with links to events, the foundation, and a newsletter signup that uses the same brick-red button. The overall effect is that of a well-organized library catalog: serious, trustworthy, and entirely focused on the written word.

colors:
  primary: "#c0392b"
  primary-active: "#a93226"
  primary-disabled: "#e6b0aa"
  ink: "#1a2a3a"
  body: "#2c3e50"
  muted: "#7f8c8d"
  muted-soft: "#bdc3c7"
  hairline: "#d5d8dc"
  hairline-soft: "#e5e8e8"
  canvas: "#ffffff"
  surface-soft: "#f4f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-navy: "#1a2a3a"
  accent-gold: "#d4a017"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    padding: 0
    height: auto
  button-text-link-hover:
    textColor: "{colors.primary-active}"
    textDecoration: underline
  top-nav:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.xl}"
  nav-item:
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: "8px {spacing.md}"
  nav-item-active:
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-author:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.canvas}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  badge-new:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0"
    borderBottom: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart," "Checkout," and primary newsletter signup. It is a solid, unrounded rectangle in brick red (`{colors.primary}`) with white uppercase text in Montserrat 600. On hover, it shifts to a darker shade (`{colors.primary-active}`). When disabled, it fades to a pale pink (`{colors.primary-disabled}`) with no pointer events. The lack of border-radius reinforces the brand's serious, editorial tone.

**`button-secondary`** — A secondary action button with a white background, ink-colored text, and a thin hairline border. Used for "View Details" or "Cancel" actions. On hover, the border becomes ink-colored and the background shifts to the softest gray (`{colors.surface-soft}`). It shares the same height and typography as the primary button for alignment in forms.

**`button-text-link`** — A text-only button styled as a link, used for "Read More" or "Learn About Our History" within body copy. It uses the brick red (`{colors.primary}`) and the serif link typography. On hover, it darkens to `{colors.primary-active}` and gains an underline. It has no padding or background, allowing it to sit inline with text.

### Navigation
**`top-nav`** — A persistent, full-width bar in the deep navy (`{colors.accent-navy}`) that spans the top of every page. It contains the City Lights logo (text-based, white), a set of nav items, and a search icon. The nav is 64px tall with horizontal padding of `{spacing.xl}`. The background color provides the brand's primary structural anchor.

**`nav-item`** — Individual navigation links (e.g., "Books," "Events," "About") rendered in white Montserrat 500. The active state is indicated by a 2px brick-red bottom border (`{colors.primary}`). There is no background highlight, keeping the nav clean and typographic.

### Search
**`search-bar`** — The primary search input for the inventory, presented as a simple white rectangle with a 1px hairline border. It uses the serif body font (Georgia) to match the reading experience. On focus, the border changes to `{colors.ink}`. There is no rounded corner, icon, or decorative element inside the input itself—only placeholder text. The search button is a `button-primary` placed immediately to the right.

### Cards
**`product-card`** — A minimal card for displaying a single book. It consists of a cover image (full width, no border), the title in `{typography.title-sm}` and `{colors.ink}`, the author in `{typography.body-sm}` and `{colors.muted}`, and the price in `{typography.body-md}` and `{colors.ink}`. There is no background fill, shadow, or border on the card itself; the whitespace around the image and text defines the card boundary. On hover, the title may underline, but there is no lift or scale effect.

### Badges
**`badge-new`** — A small, gold (`{colors.accent-gold}`) uppercase badge used to denote newly arrived titles or editions. It has 2px padding and a 2px border-radius, making it a subtle, non-intrusive label. The text is in Montserrat 700 at 10px.

**`badge-sale`** — A brick-red (`{colors.primary}`) badge used for discounted items. It shares the same dimensions and typography as the new badge but uses the brand's primary color for urgency.

### Footer
**`footer`** — A dense, text-heavy footer in the deep navy (`{colors.accent-navy}`) with white and light gray text. It contains multiple columns of links (Books, Events, About, Support, Foundation), a newsletter signup form, and copyright information. Links are in the serif body font at 14px and light gray (`{colors.muted-soft}`), turning white on hover. The newsletter signup uses a white input (`{colors.canvas}`) and a brick-red submit button (`{colors.primary}`).

### Section Headers
**`section-header`** — A typographic divider used on category pages (e.g., "New Fiction," "Staff Picks"). It uses `{typography.display-md}` in `{colors.ink}` with a 1px hairline bottom border. It has `{spacing.lg}` padding above and below the text, creating a clear visual break between sections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; product cards stack in single column; footer columns stack vertically; search bar becomes full-width below nav. |
| Tablet | 744–1128px | Top nav remains visible but nav items may be truncated; product cards display in 2–3 column grid; footer columns display in a 2x2 grid. |
| Desktop | 1128–1440px | Full top nav with all items; product cards in 3–4 column grid; footer columns in a single row; search bar is a fixed width in the nav. |
| Wide | > 1440px | Content is max-width constrained (1128px) and centered; nav remains full-width with the navy background extending to viewport edges. |

### Touch Targets
- All buttons and interactive elements maintain a minimum height of 44px.
- Nav items on mobile have a minimum touch area of 48x48px.
- Search bar input has a minimum height of 44px for easy tapping.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu. The search bar moves below the nav, becoming a full-width element.
- The footer's multi-column layout collapses to a single vertical stack on mobile, with each link group separated by a hairline border.
- Product cards collapse from a multi-column grid to a single column on mobile, with the book cover image taking full width.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extractable from the live site. The typography choices (Montserrat for headers, Georgia for body) are based on common independent bookstore web design patterns and should be verified against the actual site's CSS.
- No meta theme-color was found; the brand's primary navy (`#1a2a3a`) is a strong candidate for a browser chrome color.
- Hover and focus states for all components are inferred from common web standards and the brand's general design language; actual site implementations may differ.
- Error states for form inputs (e.g., invalid email in newsletter signup) are not defined; a red border (`{colors.primary}`) with an error message in `{colors.primary}` is a reasonable assumption.
- The site's platform (Shopify or other) could not be determined; this may affect the styling of checkout buttons and cart components.
- Dark mode styling is not defined; the brand's navy background may translate to a dark mode with a lighter navy canvas and white text.
- Sub-brand or seasonal color palettes (e.g., for the City Lights Foundation or special events) are not captured.
