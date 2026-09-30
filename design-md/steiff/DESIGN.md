---
version: alpha
name: "Steiff"
source_url: "https://www.steiffusa.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A soft, enduring world built on the warmth of #fafafa and the alert red of #d73246 — the exact shade of a Steiff button-in-ear, that tiny brass-rimmed disc that has marked every bear since 1904. The site reads like a collector’s cabinet: generous white canvas (#ffffff) carries product photography in crisp isolation, while the signature red appears sparingly — on the primary CTA, on sale badges, on the “Shop” nav link — so it lands like a found treasure, not a sales pitch. Typography pairs Bodoni Moda (a serif with sharp, elegant contrast) for display headings with Work Sans (a clean, warm sans-serif) for body and buttons, creating a dialogue between heirloom craft and modern usability. Cards use soft rounding ({rounded.sm} at 8px) and thin hairline borders (#ebebeb) that echo the delicate stitching on a bear’s paw. The footer is dense with links in #3c3c3c, anchored by a large Steiff logo and a newsletter signup field with a red button — the brand’s quiet insistence on community and continuity. There is no harsh geometry; even the search bar is pill-shaped ({rounded.full}), and the product grid breathes with generous padding ({spacing.lg} to {spacing.xl}). The overall mood is one of careful preservation — a digital space that feels as tactile and trustworthy as the plush it sells.

colors:
  primary: "#d73246"
  primary-active: "#c12a3c"
  primary-disabled: "#f0a0a8"
  ink: "#0e0c0c"
  body: "#3c3c3c"
  muted: "#656565"
  muted-soft: "#adadad"
  hairline: "#ebebeb"
  hairline-soft: "#f0f0f0"
  canvas: "#fafafa"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sale-badge: "#d73246"
  sale-badge-text: "#ffffff"
  accent-sage: "#32786e"
  accent-gold: "#fab446"
  accent-sky: "#8ca0b9"
  accent-rose: "#fabeaf"
  accent-terracotta: "#9b6a45"
  footer-bg: "#0e0c0c"
  footer-text: "#adadad"
  link-hover: "#d73246"

typography:
  display-xl:
    fontFamily: "'Bodoni Moda', Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Bodoni Moda', Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Bodoni Moda', Georgia, 'Times New Roman', serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Work Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Work Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Work Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Work Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Work Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Work Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Work Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Work Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Work Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Work Sans', 'Helvetica Neue', Arial, sans-serif"
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
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
  button-pill-red:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    marginTop: "{spacing.xs}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.md}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.link-hover}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  category-strip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  category-tab-active:
    textColor: "{colors.primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The brand’s primary call-to-action, filled with Steiff red (#d73246) and white text. Used for “Add to Cart,” “Shop Now,” and primary checkout actions. On hover, it darkens to `{colors.primary-active}` (#c12a3c). The disabled state uses a soft pink `{colors.primary-disabled}` (#f0a0a8) to indicate inactivity without visual noise.

**`button-secondary`** — An outlined or ghost variant for secondary actions like “Learn More” or “View Details.” On `{colors.canvas}` background, it uses a 1px solid `{colors.hairline}` border and `{colors.ink}` text. Hover adds a subtle background tint of `{colors.surface-soft}`.

**`button-pill-red`** — A fully rounded pill variant reserved for promotional badges, sale tags, or compact CTAs in tight spaces like product cards or the sticky header. Uses `{typography.button-sm}` for a tighter fit.

### Cards
**`product-card`** — The core product display unit. A white card (`{colors.surface-card}`) with `{rounded.sm}` corners and a thin `{colors.hairline}` border. The product image sits at the top with matching corner rounding. Below, the title uses `{typography.title-sm}` in `{colors.ink}`, and the price uses `{typography.body-md}` in `{colors.primary}` to draw the eye. A `{sale-badge}` overlays the top-left corner of the image when applicable.

**`sale-badge`** — A small, uppercase red badge (`{colors.sale-badge}`) with white text, `{rounded.xs}` corners, and tight padding. Used to flag discounts, limited editions, or “New” arrivals. The typography is `{typography.badge}` — 11px, bold, uppercase.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height, white background (`{colors.surface-card}`), with a thin `{colors.hairline}` bottom border. The Steiff logo sits left-aligned; primary links (“Shop,” “About,” “Collectors,” “Gifts”) use `{typography.nav-link}` in `{colors.ink}`. The active link (or hover state) shifts to `{colors.primary}`. A search icon and cart icon sit right-aligned.

**`category-strip`** — A horizontal scrollable strip below the hero, containing product categories (e.g., “Teddy Bears,” “Animals,” “Limited Edition”). Links use `{typography.nav-link}` in `{colors.muted}`; the active category uses `{colors.primary}`. No background — just text on the canvas.

**`breadcrumb`** — A secondary navigation aid on product detail pages. Uses `{typography.caption}` in `{colors.muted}`, with the current page in `{colors.ink}`. Separators are simple “/” in `{colors.muted-soft}`.

### Forms
**`text-input`** — Standard text input for forms (newsletter signup, search, account fields). White background, `{rounded.sm}`, 44px height, with `{typography.body-md}` placeholder text in `{colors.muted}`. On focus, the border shifts to `{colors.primary}` (#d73246) for clear visual feedback.

**`newsletter-input`** — A compact input specifically for the footer newsletter signup. 40px height, `{rounded.sm}`, paired with a `{newsletter-button}` of the same height. The button uses `{colors.primary}` and `{typography.button-sm}`.

### Footer
**`footer`** — A dark section (`{colors.footer-bg}` #0e0c0c) with light text (`{colors.footer-text}` #adadad). Links use `{typography.link}` and shift to `{colors.link-hover}` (#d73246) on hover. The layout is a multi-column grid with columns for “Shop,” “About,” “Support,” and “Connect.” A newsletter signup form sits in the center column. The Steiff logo appears in white at the top of the footer.

### Hero
**`hero-section`** — The top-of-page hero on the homepage and collection pages. Uses `{colors.canvas}` (#fafafa) as background, with `{spacing.section}` vertical padding. The heading uses `{typography.display-xl}` in `{colors.ink}`, and the subheading uses `{typography.body-md}` in `{colors.muted}`. A single `{button-primary}` sits below the subheading. The hero may include a full-bleed product image on desktop.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero padding reduced to {spacing.xl}; footer stacks vertically; search bar moves to drawer. |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero uses two-thirds width for text; footer uses two-column layout. |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero uses full-width image with text overlay; footer uses four-column grid. |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to four columns; hero uses larger display typography (48px). |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Product card tap targets (image, title, price) are at least 48px tall.
- Nav bar links have 48px tap height.
- Search bar and newsletter inputs are 40–44px tall.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses into a hamburger menu; the search bar moves into a slide-out drawer.
- The category strip becomes a horizontally scrollable row on mobile and tablet.
- The footer’s multi-column grid collapses to a single column on mobile, with accordion-style expandable sections for each column.
- Product images switch from landscape to square crop on mobile to maintain visual consistency.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for buttons, links, and cards were inferred from common patterns; exact hover transitions (e.g., background color, shadow) were not extracted.
- **Error styling** for form inputs (e.g., invalid email, required field) was not observed; a red border (`{colors.primary}`) with an error message in `{colors.body}` is assumed.
- **Dark mode** is not supported; the palette is light-only.
- **Sub-brand palettes** (e.g., “Steiff Baby,” “Steiff Collectors”) may exist but were not extracted; the primary palette is used for all.
- **Font weights and sizes** for `Bodoni Moda` and `Work Sans` were estimated based on common usage; exact values from the live site’s CSS were not fully captured.
- **Animation and transition durations** (e.g., button hover, card lift) were not extracted; a default of 0.2s ease-in-out is recommended.
- **Iconography** (e.g., search, cart, social media) was not analyzed; the brand likely uses custom SVG icons in `{colors.ink}` or `{colors.primary}`.
- **Checkout flow** (Shopify Pay, Klarna, Afterpay) colors were filtered out; the extracted list included #007aff, #5897fb, and #63a31e which are likely from payment widgets, not the brand.
