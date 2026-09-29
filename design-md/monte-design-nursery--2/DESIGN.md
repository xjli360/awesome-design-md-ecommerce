---
version: alpha
name: "Monte Design"
source_url: "https://montedesign.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A nursery and home furniture brand that builds its visual identity around three grays — `#dedede`, `#747474`, and `#121212` — creating a restrained, architectural atmosphere that lets the furniture's natural wood tones and soft curves take center stage. The brand uses Chap, a refined serif typeface with elegant bracketed serifs and moderate contrast, as its sole declared font family, giving product names and category headers a quiet editorial dignity. The palette is deliberately minimal: a warm light gray (`#dedede`) serves as the primary canvas and secondary surface, the mid-tone (`#747474`) handles body text and muted elements, and near-black (`#121212`) anchors headlines and primary ink. There are no bright accent colors — no nursery pastels, no brand red — which is an unusual and confident choice for a children's furniture brand. The design system trusts materiality and photography over color: the grain of solid wood, the drape of upholstery, the softness of rounded corners on crib rails and dresser edges. Buttons and interactive elements use the same gray palette, with `{rounded.sm}` corners that echo the furniture's gentle geometry. The overall effect is that of a design studio's lookbook — quiet, premium, and completely uninterested in the typical nursery-brand playbook of pastel gradients and whimsical icons.

colors:
  primary: "#747474"
  primary-active: "#5a5a5a"
  primary-disabled: "#b0b0b0"
  ink: "#121212"
  body: "#747474"
  muted: "#999999"
  muted-soft: "#b0b0b0"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-warm: "#dedede"
  on-primary: "#ffffff"
  on-ink: "#ffffff"
  wood-accent: "#c4a882"

typography:
  display-xl:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
    textTransform: uppercase
  body-md:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  caption-sm:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Chap', 'Georgia', 'Times New Roman', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.8px
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
  section: 80px

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
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-wood-accent:
    backgroundColor: "{colors.wood-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
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
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid #c13515"
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
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  logo-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    height: 40px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    backgroundColor: "{colors.surface-warm}"
    rounded: "{rounded.none}"
    aspectRatio: "4/5"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    height: "60vh"
    minHeight: "400px"
  hero-cta:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: "48px"
  hero-cta-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  section-header:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    paddingBottom: "{spacing.xl}"
  category-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
  category-card-image:
    backgroundColor: "{colors.surface-warm}"
    rounded: "{rounded.none}"
    aspectRatio: "1/1"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.caption}"
    textColor: "{colors.canvas}"
    paddingBottom: "{spacing.md}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} 0"
  divider:
    backgroundColor: "{colors.hairline}"
    height: "1px"
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: "1px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: "44px"
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    width: "44px"
    height: "44px"
  add-to-cart-button:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: "48px"
  add-to-cart-button-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  breadcrumb:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption-sm}"
    textColor: "{colors.ink}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    width: "40px"
    height: "40px"
  pagination-button-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  notification-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  notification-banner-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    textDecoration: "underline"
  loading-spinner:
    color: "{colors.primary}"
    size: "24px"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in `{colors.primary}` (#747474) mid-gray with white text and `{rounded.sm}` corners. On hover, the background deepens to `{colors.primary-active}` (#5a5a5a). The disabled state uses `{colors.primary-disabled}` (#b0b0b0). All primary buttons use `{typography.button-md}` — 14px Chap with 0.5px letter-spacing, uppercase — and sit at 44px height with 12px/28px padding.

**`button-secondary`** — An outlined variant with a white background, `{colors.ink}` text, and a 1px `{colors.hairline}` border. Active state swaps the border to `{colors.primary}`. Same 44px height and typography as primary, but with 11px/27px padding to account for the border.

**`button-tertiary-text`** — A text-only button with no background or border, using `{colors.ink}` text. On hover/active, the text shifts to `{colors.primary}`. Used for "View Details" links and secondary actions within product cards.

**`button-wood-accent`** — A special accent button using `{colors.wood-accent}` (#c4a882), a warm wood-tone beige that complements the brand's furniture photography. Same sizing and typography as `button-primary`. Used sparingly for "Shop by Material" or "Explore Collections" CTAs on the homepage.

### Cards
**`product-card`** — A minimal, borderless card with white background and no rounding. The product image sits in a `{colors.surface-warm}` (#dedede) container at a 4:5 aspect ratio, creating a soft, editorial frame. Below the image, the title uses `{typography.title-md}` (16px Chap) in `{colors.ink}`, and the price uses `{typography.body-md}` (16px) in `{colors.body}` (#747474). Optional badges (e.g., "NEW", "SALE") render as small black rectangles with white uppercase text at 10px.

**`category-card`** — A square (1:1) card for browsing furniture categories (Cribs, Dressers, Gliders). The image sits on a `{colors.surface-warm}` background, with the category name set in `{typography.title-md}` below. No rounding — the brand avoids soft corners on its grid cards, reserving rounding for interactive elements only.

### Navigation
**`nav-bar`** — A 72px white bar with a 1px `{colors.hairline}` bottom border. Logo sits at 40px height using `{typography.display-sm}` (20px Chap). Navigation links use `{typography.nav-link}` — 13px Chap, uppercase with 0.8px letter-spacing. Active links get a 2px `{colors.ink}` bottom border; inactive links render in `{colors.muted}` (#999999).

**`breadcrumb`** — A simple text trail using `{typography.caption-sm}` (11px Chap) in `{colors.muted}`, with the active (current) page in `{colors.ink}`. No separators other than a forward slash or chevron — the brand keeps navigation minimal.

### Forms
**`text-input`** — A 48px tall input with white background, `{colors.hairline}` border, and `{rounded.sm}` corners. Focus state swaps the border to `{colors.primary}`. Error state uses a red border (#c13515). Text is set in `{typography.body-md}` (16px Chap). The select input follows the same pattern.

**`quantity-selector`** — A horizontal stepper with a 44px height, `{colors.hairline}` border, and `{rounded.sm}` corners. The decrement/increment buttons are 44px squares with no rounding, centered on the text. The current quantity displays in `{typography.body-md}`.

### Footer
**`footer`** — A full-width black (`{colors.ink}`) section with white text. Column headings use `{typography.caption}` (12px uppercase Chap with 0.3px letter-spacing). Links render in `{colors.muted-soft}` (#b0b0b0) and shift to white on hover. Padding is generous at 48px vertical and 80px horizontal.

### Accordion
**`accordion-header`** — A clickable row with white background, `{typography.title-md}` (16px Chap) in `{colors.ink}`, and a 1px `{colors.hairline}` bottom border. Padding is 16px vertical. The content panel uses `{typography.body-md}` in `{colors.body}` (#747474) with 16px padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 col), nav collapses to hamburger menu, hero height reduces to 50vh, product cards stack vertically, footer columns stack to single column, section padding reduces to 32px |
| Tablet | 744–1128px | Two-column product grid (2 col), nav links remain visible but condensed, hero height at 55vh, footer columns in 2x2 grid, section padding at 48px |
| Desktop | 1128–1440px | Three-column product grid (3 col), full nav bar visible, hero at 60vh, footer columns in full row, section padding at 80px |
| Wide | > 1440px | Four-column product grid (4 col) on category pages, max-width container at 1440px centered, hero content constrained to 1200px, same padding as desktop |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height
- Quantity selector buttons are 44px × 44px
- Mobile nav hamburger icon is 44px × 44px
- Product card tap targets (title, price, image) are full card width
- Accordion headers are full width with 44px minimum height

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product grid collapses from 3 columns → 2 columns → 1 column
- Footer collapses from 4 columns → 2 columns → 1 column
- Hero section reduces height from 60vh → 50vh on mobile
- Product card image aspect ratio remains 4:5 across all breakpoints
- Section padding reduces by 40% on mobile (80px → 48px → 32px)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components are inferred from common patterns; actual hover transitions (duration, easing) not extracted
- Focus ring styles (color, offset, thickness) not found in extracted CSS
- Error state colors for forms are assumed (#c13515 is a common error red); actual brand error palette unknown
- Success/confirmation state colors not extracted
- Dark mode not implemented on live site
- Font weights beyond 400 (regular) not confirmed — Chap may have italic or bold variants not declared in extracted CSS
- Actual line-height values are estimated based on typical serif typesetting; extracted CSS did not include explicit line-height declarations
- Letter-spacing values for uppercase styles are inferred from common practice (0.05em–0.08em range)
- The wood-accent color (#c4a882) is an approximation based on common wood tones; actual brand accent color may differ
- Animation and transition timing values (duration, easing curves) not extracted
- Dropdown menu styles (mega menu, sub-navigation) not observed on live site
- Mobile navigation drawer (hamburger menu) animation and overlay styles not extracted
- Shopify-specific checkout button styles (Shopify Pay, cart drawer) not included — these are platform defaults, not brand design
- Social media icon colors and hover states not extracted
- Newsletter signup form error/success states not observed
- Product swatch (color/material selector) UI not confirmed — may use image-based swatches rather than colored circles
- Loading states (skeleton screens, spinners) beyond basic spinner not documented
- Print stylesheet not available
