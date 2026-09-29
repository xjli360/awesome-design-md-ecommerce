---
version: alpha
name: "Maiden Home"
source_url: "https://maidenhome.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Maiden Home is a direct-to-consumer furniture brand that speaks in a quiet, confident voice — one that trusts the weight of a well-chosen neutral over the shout of a trend. The palette is anchored by a deep, almost-black ink (`#1c1c1c`) and a warm off-white canvas (`#f5f5f1`), with a secondary slate (`#6c757d`) that appears in product descriptions, secondary buttons, and footer links. The brand's primary voltage comes from a restrained navy (`#334fb4`) and a cooler cerulean (`#1990c6`) used sparingly — on the "Shop the Look" CTA, on the checkout button, and on the single accent line in the top nav. These blues never dominate; they punctuate. The typography runs on ABC Whyte and Maison Neue, both geometric sans-serifs with a slightly condensed, architectural feel that echoes the clean lines of the furniture itself. Body copy sits at 16px on a 1.5 line height, with display headlines at 28px in a weight 500 that feels deliberate, not loud. Corners are soft but not pillowy — cards and buttons use `{rounded.sm}` (8px) and `{rounded.md}` (12px), while the search bar and primary CTA use `{rounded.full}` for a friendly, approachable finish. The overall mood is one of curated calm: generous whitespace, a muted hairline (`#dedede`) that defines sections without drawing attention, and a single hero image that carries the emotional weight of the page. Maiden Home does not need to shout; it invites you to sit down.

colors:
  primary: "#334fb4"
  primary-active: "#242833"
  primary-disabled: "#6c757d"
  ink: "#1c1c1c"
  body: "#242833"
  muted: "#6c757d"
  muted-soft: "#dedede"
  hairline: "#dedede"
  hairline-soft: "#f5f5f1"
  canvas: "#f5f5f1"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#1990c6"
  accent-blue-hover: "#136f99"
  badge-new: "#334fb4"
  badge-sale: "#1990c6"
  star-rating: "#1c1c1c"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'ABC Whyte', 'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ABC Whyte', 'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'ABC Whyte', 'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'ABC Whyte', 'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'ABC Whyte', 'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'ABC Whyte', 'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'ABC Whyte', 'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'ABC Whyte', 'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'ABC Whyte', 'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px

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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-accent:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-blue-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.primary-disabled}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "4/5"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.surface-soft}"
  badge:
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
  rating-stars:
    color: "{colors.star-rating}"
    size: "16px"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: "40px"
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop the Look", and checkout flows. It features a deep navy (`{colors.primary}`) background with white text, full pill rounding (`{rounded.full}`), and uppercase lettering with 0.5px tracking. On hover, the background shifts to a darker, almost-ink navy (`{colors.primary-active}`). The disabled state uses the muted slate (`{colors.primary-disabled}`) to signal inactivity without visual noise.

**`button-secondary`** — A ghost-style button with a transparent background, dark ink text, and a 1px hairline border. Used for "Learn More" and "View Details" actions that need to sit alongside primary buttons without competing. On hover, the background fills with the soft canvas tone (`{colors.hairline-soft}`).

**`button-accent`** — A secondary accent button using the cooler cerulean blue (`{colors.accent-blue}`) for less critical but still actionable CTAs, such as "Subscribe" or "Get Inspired". On hover, it deepens to `{colors.accent-blue-hover}`.

**`button-tertiary-text`** — A plain text button with no background or border, used for inline actions like "Cancel" or "Clear Filters". Inherits the standard button typography but remains visually minimal.

### Cards
**`product-card`** — The primary product display unit, a white card (`{colors.surface-card}`) with softly rounded corners (`{rounded.sm}`). The image occupies a 4:5 aspect ratio, cropped cleanly to the card's top edge. Below, the product title sits in a 14px semi-bold (`{typography.title-sm}`), with the price in a muted 14px body (`{typography.body-sm}`). A small badge (`{rounded.xs}`) can appear in the top-left corner of the image for "New" or "Sale" indicators.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px tall, using the warm off-white canvas (`{colors.canvas}`) background. Links are set in ABC Whyte at 14px weight 500 with 0.3px letter spacing. The active link is underlined with a 2px navy bar (`{colors.primary}`). Inactive links render in the muted slate (`{colors.muted}`). The logo sits left-aligned, with a search icon and cart icon on the right.

### Forms
**`text-input`** — Standard text input fields for search, email signup, and address forms. They use a white background (`{colors.surface-soft}`), a 1px hairline border (`{colors.hairline}`), and 8px corner rounding (`{rounded.sm}`). On focus, the border switches to the primary navy (`{colors.primary}`). Error states swap the border to the muted slate (`{colors.primary-disabled}`).

### Footer
**`footer`** — A full-width footer with a dark ink background (`{colors.ink}`) and light text. Links are set in the muted-soft tone (`{colors.muted-soft}`) and lighten to white on hover. The footer is divided into columns for "Shop", "About", "Support", and "Follow Us", with generous padding (`{spacing.xxl}`) top and bottom.

### Badges
**`badge`** — Small, uppercase labels used to flag new arrivals. They use the navy primary (`{colors.badge-new}`) with white text, 4px rounding (`{rounded.xs}`), and tight padding. A sale variant (`{badge-sale}`) uses the cerulean accent (`{colors.badge-sale}`).

### Search
**`search-bar`** — A pill-shaped search field (`{rounded.full}`) with a white background and 1px hairline border. It appears in the top nav on desktop and as a full-width bar on mobile. On focus, the border shifts to the primary navy.

### Hero
**`hero-section`** — The full-width hero banner on the homepage and collection pages. It uses the off-white canvas background (`{colors.canvas}`) with a large display headline (`{typography.display-xl}`) and a single primary CTA button. The hero image is full-bleed and sits below or behind the text, depending on the layout.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in a single column; hero text reduces to `{typography.display-md}`; search bar becomes full-width; footer columns stack vertically. |
| Tablet | 744–1128px | Nav bar shows full links but with reduced spacing; product cards display in a 2-column grid; hero uses a split layout (text left, image right). |
| Desktop | 1128–1440px | Standard layout: 3-4 column product grid; full nav bar with search; hero uses full-width image with overlaid text. |
| Wide | > 1440px | Max-width container (1440px) centered; additional whitespace on sides; product grid expands to 4 columns. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Product card images and CTAs are at least 48px tall.
- Nav bar links have a minimum 40px tap area.
- Search bar and text inputs are 48px tall for easy tapping.

### Collapsing Strategy
- On mobile, the top navigation collapses to a hamburger icon with a slide-out drawer.
- The product filter sidebar collapses to a "Filter" button that opens a modal overlay.
- The footer's multi-column layout collapses to a single column with accordion-style sections.
- The hero section's text and image stack vertically on mobile, with the image above the text.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons and text inputs could not be fully verified; the active states above are inferred from common patterns.
- Error styling for forms (validation messages, error icons) was not observed on the live site.
- Dark mode is not supported; no dark palette tokens were found.
- Sub-brand or collection-specific palettes (e.g., "Outdoor", "Bedroom") may exist but were not extracted.
- The exact font weights for ABC Whyte and Maison Neue are assumed based on common usage; the live site may use additional weights (e.g., 300, 700).
- Animation and transition durations (e.g., button hover, nav drawer slide) were not captured.
- The `object-fit: contain` declaration found in the CSS hints suggests specific image handling, but its context (product images vs. hero images) is unclear.
- The `inherit` value in font-family hints may indicate a fallback or a specific component override that could not be isolated.
