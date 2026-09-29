---
version: alpha
name: "Europa Editions"
source_url: "https://www.europaeditions.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A small press that wraps literary fiction in a distinctive teal-green signal — #098782 — that appears on every book spine, footer stripe, and primary button, a color more at home in a Mediterranean tide pool than on a publisher's website. The palette is restrained but not ascetic: #098782 anchors the brand, supported by a warm accent red (#d0091c) for price tags and sale badges, a cool secondary teal (#42a19d) for secondary actions, and a full gray spectrum from #222222 ink to #f5f5f5 canvas. The site reads as a clean, typographic-first experience — Georgia and Helvetica Neue in the font stack suggest a respect for print tradition, while generous whitespace and soft card radii (`{rounded.md}`) keep the digital reading room calm. Navigation is minimal: a top bar with logo, search, and cart, then a category strip of genres. Book covers do the heavy lifting — the UI steps back, using thin hairlines (`#eceded`) and muted body text (`#6f7072`) to frame rather than compete. The overall feeling is of a well-edited bookstore where every element has earned its place.

colors:
  primary: "#098782"
  primary-active: "#076c68"
  primary-disabled: "#bcc0c0"
  ink: "#222222"
  body: "#6f7072"
  muted: "#888888"
  muted-soft: "#bcc0c0"
  hairline: "#eceded"
  hairline-soft: "#edeeee"
  canvas: "#f5f5f5"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#d0091c"
  accent-red-active: "#a60716"
  accent-orange: "#cf6e0e"
  accent-blue: "#61b6d9"
  star-rating: "#f08a24"
  sale-badge: "#d0091c"
  footer-bg: "#098782"
  footer-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-author:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.accent-red}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.footer-text}"
  category-strip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.base}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.on-primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with `{colors.primary}` teal and white text. Used for "Add to Cart", "Subscribe", and primary form submissions. On hover, shifts to `{colors.primary-active}`. Disabled state uses `{colors.primary-disabled}` with white text. All buttons use uppercase sans-serif type at 14px with 0.5px letter-spacing.

**`button-secondary`** — An outlined variant with transparent background and a 2px `{colors.primary}` border. Text is `{colors.primary}`. Used for "Preview" or "Learn More" actions alongside primary buttons. On hover, fills with `{colors.primary}` and white text.

**`button-accent-red`** — Reserved for sale-related actions and limited-time offers. Uses `{colors.accent-red}` background with white text. Matches the sale-badge color for visual consistency.

### Cards
**`product-card`** — A clean, borderless card with `{rounded.sm}` corners and white background. The book cover image fills the top, with title, author, and price stacked below. No shadow — relies on the cover art and typographic hierarchy. The title uses `{typography.title-sm}` in `{colors.ink}`, author in `{typography.caption}` in `{colors.muted}`, and price in `{typography.body-sm}`. Sale prices render in `{colors.accent-red}`.

**`sale-badge`** — A small red badge (`{colors.sale-badge}`) with white uppercase text, pinned to the top-left corner of product images. Uses `{rounded.xs}` for a subtle squared-off look that matches the button system.

### Navigation
**`nav-bar`** — A 72px white bar with a bottom hairline (`{colors.hairline}`). Contains the Europa Editions logo (left), nav links (center), and search/cart icons (right). Links use `{typography.nav-link}` — uppercase, 14px, 0.3px letter-spacing. Active link or current section uses `{colors.primary}` text.

**`category-strip`** — A secondary navigation row below the main nav, listing genres (Fiction, Nonfiction, etc.). Active category has a 2px `{colors.primary}` bottom border. Inactive categories use `{colors.body}` text.

### Forms
**`text-input`** — Standard input with white background, `{colors.hairline}` border, and `{rounded.xs}` corners. On focus, the border switches to `{colors.primary}`. Uses `{typography.body-md}` (Georgia serif) for a reading-friendly feel.

**`search-bar`** — A pill-shaped (`{rounded.full}`) input with `{colors.surface-soft}` background and a subtle hairline border. Used in the header and on search pages. Height is 40px — compact enough to not dominate the nav.

### Footer
**`footer`** — A full-width teal band (`{colors.footer-bg}`) with white text. Contains links, newsletter signup, and social icons. Links use `{typography.link}` in white. Padding is generous at `{spacing.xxl}` vertical.

### Hero
**`hero-banner`** — A teal background section (`{colors.primary}`) with white text, used for featured collections or seasonal promotions. Title uses `{typography.display-md}` and subtitle uses `{typography.body-md}`. Padding is `{spacing.section}` vertical to create breathing room.

### Breadcrumbs
**`breadcrumb`** — Small gray links (`{colors.muted}`) in `{typography.caption}`. The active (current) page uses `{colors.ink}`. Separators are slashes or chevrons in `{colors.muted-soft}`.

### Pagination
**`pagination`** — Numbered page links in `{typography.body-sm}` with `{colors.body}` text. The active page is a filled `{colors.primary}` circle (`{rounded.full}`, 32px). Inactive pages are text-only with hover underlines.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero banner reduces padding; category strip becomes a horizontal scroll; footer stacks links vertically |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but compact; hero banner uses medium padding; search bar collapses to icon |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero banner at full padding; search bar visible with input |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can show 4 columns; hero banner width constrained |

### Touch Targets
- All buttons and links: minimum 44px height
- Nav links: 44px tap area even if text is smaller
- Search icon: 44x44px tap target
- Category strip items: 44px minimum height
- Product card: entire card is tappable (links to product page)

### Collapsing Strategy
- Main nav: links collapse into hamburger menu below 744px
- Category strip: horizontal scroll on mobile (no collapse, just swipe)
- Search bar: full input collapses to search icon on tablet and below
- Footer: multi-column layout collapses to single column on mobile
- Product grid: 3 columns → 2 columns → 1 column as viewport shrinks
- Hero banner: large padding reduces by 50% on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were not reliably extracted from the live site CSS — the extracted font-family declarations were heavily media-query-scoped and may not represent the full typographic system
- The exact font stack for body text is inferred from Georgia presence in the extracted list, but the primary font for UI elements (buttons, nav) appears to be Helvetica Neue / Helvetica / Arial — the exact weight and size hierarchy is reconstructed from common publishing patterns
- Dark mode is not present on the live site and was not extracted
- Error states for form inputs (validation colors, error messages) were not found in the extracted data
- The extracted color list is large (30+ colors) and includes many grays — the true brand palette likely uses fewer colors, with the teal (#098782) and red (#d0091c) as the two accents; the remaining grays are likely from images, borders, and framework defaults
- Sub-brand or imprint-specific palettes (if any) were not extracted
- Animation and transition timings were not captured
- The extracted font-family declarations include many media-query-specific values (e.g., `/only screen and (min-width:40.0625em)/`) that suggest responsive font sizing, but the exact breakpoint values and size changes could not be determined
- Iconography style (line vs. filled, stroke weight) was not extracted
