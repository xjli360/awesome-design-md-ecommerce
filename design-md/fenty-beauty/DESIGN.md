---
version: alpha
name: "Fenty Beauty"
source_url: "https://www.fentybeauty.com"
captured_at: "2026-09-28T04:10:05.521425+00:00"
evidence_status: "historical_partial_css_evidence"
description: |-
  Fenty Beauty by Rihanna is a radical, inclusive force in makeup — a brand that rewrote the industry’s color palette by launching with 40 foundation shades and never looking back. The visual system mirrors that ethos: a crisp, almost editorial white canvas (`#ffffff`) is punctuated by a confident, unapologetic red (`#bd0100`) that serves as the brand’s primary voltage, appearing on CTAs, badges, and hero accents. This red is balanced by a sophisticated, cool-toned neutral palette — warm taupe (`#ebdad3`), dusty rose (`#e0beb1`), soft lilac (`#d8cbda`), and deep plum (`#6c4e71`) — that echo the brand’s skin-tone-first philosophy and its Killawatt highlighter family. The typography is anchored by the proprietary **Brown** typeface, a rounded, humanist sans-serif that feels both approachable and fashion-forward, paired with the more delicate **Loud** for display moments. Buttons and cards use soft, pill-like radii (`{rounded.sm}` at 8px for CTAs, `{rounded.lg}` at 20px for product cards), avoiding harsh corners to maintain a tactile, skin-friendly feel. The overall mood is one of confident, joyful glamour — not minimal, not maximal, but precisely *Fenty*: a system where a `{colors.primary}` red button sits next to a `{colors.muted}` (#a8a8a8) secondary link, and where the `{colors.canvas}` (#ffffff) background lets the product photography and the model’s skin do the real talking. The brand’s Shopify platform is evident in the modular, product-card-heavy layout, with `{colors.hairline}` (#d8d8d8) dividers and `{colors.surface-soft}` (#f7f4f3) section backgrounds creating a clean, shoppable grid.

colors:
  primary: "#bd0100"
  primary-active: "#9a0100"
  primary-disabled: "#e8a6a6"
  ink: "#292829"
  body: "#373737"
  muted: "#a8a8a8"
  muted-soft: "#c0c0c0"
  hairline: "#d8d8d8"
  hairline-soft: "#e1dce4"
  canvas: "#ffffff"
  surface-soft: "#f7f4f3"
  surface-card: "#ffffff"
  surface-strong: "#f2f2f2"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-gold: "#f2c94c"
  accent-blue: "#003087"
  accent-light-blue: "#009cde"
  accent-deep-blue: "#0e4595"
  accent-warm-taupe: "#ebdad3"
  accent-dusty-rose: "#e0beb1"
  accent-soft-lilac: "#d8cbda"
  accent-deep-plum: "#6c4e71"
  accent-brown: "#684537"
  accent-purple: "#8d89a5"
  accent-red-badge: "#d42b2a"
  accent-gold-star: "#f2ae14"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Loud', 'Brown', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Loud', 'Brown', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Brown', 'Loud', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Brown', 'Loud', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Brown', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Brown', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Brown', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Brown', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Brown', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Brown', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Brown', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
  link:
    fontFamily: "'Brown', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Brown', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'Brown', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    padding: 14px 32px
    height: 48px
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
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    height: 64px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-swatch:
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    height: 480px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
  search-bar-icon:
    color: "{colors.muted}"
    height: 20px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
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
  badge-shade:
    backgroundColor: "{colors.accent-warm-taupe}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "1px solid {colors.hairline}"
  color-swatch-selected:
    border: "2px solid {colors.ink}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
    width: 120px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  rating-stars:
    color: "{colors.accent-gold-star}"
    height: 16px
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The brand’s primary call-to-action, rendered in the signature Fenty red (`#bd0100`) with white text. Uses a soft 8px radius (`{rounded.sm}`) and the bold `button-md` typography with 0.5px letter-spacing for a confident, editorial feel. On hover, the background deepens to `{colors.primary-active}` (#9a0100). The disabled state uses a muted pink (`{colors.primary-disabled}` #e8a6a6) to signal inactivity without visual noise.

**`button-secondary`** — An outlined variant for secondary actions, built on a white canvas with a 2px solid ink (`{colors.ink}` #292829) border. Shares the same dimensions and typography as the primary button but inverts the color relationship. On active state, the background fills with `{colors.surface-soft}` (#f7f4f3) for a subtle press effect.

**`button-tertiary-text`** — A text-only link styled as a button, used for less prominent actions like "View Details" or "Learn More". The text color matches the brand red (`{colors.primary}`) and inherits the `button-md` weight for visual consistency, but has no background or border.

**`button-pill-primary`** — A fully pill-shaped variant (`{rounded.full}`) used for promotional badges, filter tags, or compact CTAs. Uses the smaller `button-sm` typography and tighter padding (10px 24px) to sit comfortably alongside product imagery.

### Cards
**`product-card`** — The core product display unit, a white card with a 20px radius (`{rounded.lg}`) that frames product photography. The image area uses a top-only radius (`{rounded.lg} {rounded.lg} 0 0`) to create a seamless transition into the text content below. The card title uses `title-sm` (16px, weight 500) and the price uses `body-md` (16px, weight 400) in `{colors.body}` (#373737). A `product-card-badge` overlays the top-left corner of the image for "New" or "Best Seller" flags.

**`review-card`** — A bordered card (1px `{colors.hairline-soft}` #e1dce4) with a 12px radius (`{rounded.md}`) and 16px padding. Used to display customer reviews with star ratings (`{colors.accent-gold-star}` #f2ae14) and body text in `{colors.body}`.

### Navigation
**`nav-bar`** — A fixed-height (64px) white bar with a 1px bottom border (`{colors.hairline}` #d8d8d8). Navigation links use the `nav-link` typography — 14px, weight 600, uppercase with 1px letter-spacing — for a clean, fashion-editorial feel. The active link state drops a 2px red (`{colors.primary}`) bottom border beneath the text.

**`nav-link-active`** — The active navigation state, distinguished by a red bottom border and red text color, signaling the current section or page.

### Forms
**`text-input`** — A standard input field with a 1px `{colors.hairline}` border, 8px radius, and 48px height. On focus, the border thickens to 2px and switches to the brand red (`{colors.primary}`). Error states also use a 2px red border, paired with an error message in `{colors.primary}`.

**`search-bar`** — A pill-shaped (`{rounded.full}`) search input on a `{colors.surface-soft}` (#f7f4f3) background, 48px tall with 20px horizontal padding. The search icon sits in `{colors.muted}` (#a8a8a8) for a low-contrast, elegant feel.

**`quantity-selector`** — A compact, bordered control (1px `{colors.hairline}`, 8px radius) for adjusting product quantities. Contains two square buttons (40x40px) flanking a central numeric display, all in `{colors.ink}`.

### Footer
**`footer`** — A dark section anchored on `{colors.ink}` (#292829) with white text. Links use `{colors.muted-soft}` (#c0c0c0) and shift to full white on hover. The section padding is generous (`{spacing.xxl}` top and bottom) to create breathing room for legal text, social links, and newsletter signup.

### Badges & Swatches
**`badge-new`** — A gold (`{colors.accent-gold}` #f2c94c) badge with dark text, used to flag new arrivals. Uses the `badge` typography (11px, weight 700, uppercase) with tight padding (2px 6px) and a 4px radius.

**`badge-sale`** — A red (`{colors.primary}`) badge with white text for sale or promotional items. Same typography and dimensions as `badge-new`.

**`badge-shade`** — A pill-shaped tag in `{colors.accent-warm-taupe}` (#ebdad3) used to label foundation shades or product variants. Uses the smaller `caption` typography (12px, weight 500) for a softer, more informational appearance.

**`color-swatch`** — A 32px circular swatch with a 1px `{colors.hairline}` border. The selected state adds a 2px `{colors.ink}` border for clear visual distinction.

### Accordion
**`accordion`** — A vertically stacked disclosure component with a bottom border (`{colors.hairline}`) and 16px vertical padding. The header uses `title-sm` (16px, weight 500) and the content area uses `body-sm` (14px, weight 400) in `{colors.body}`. Used for product details, shipping info, and FAQ sections.

### Hero
**`hero-banner`** — A full-width section (480px tall) on a `{colors.surface-soft}` (#f7f4f3) background, featuring large display typography (`display-lg` at 36px) and a primary CTA button. The layout is centered, with generous whitespace to let the product or campaign imagery breathe.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; product cards stack vertically; nav-bar collapses to hamburger menu; hero banner height reduces to 320px; search bar moves to a dedicated overlay; footer links stack; typography scales down (display-xl becomes 32px) |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links (Shop, Explore, Search icon); hero banner at 400px; side panels appear for filters on collection pages; accordion remains expanded by default |
| Desktop | 1128–1440px | Full nav-bar with all links visible; three-column product grid; hero banner at 480px; sticky nav-bar with scroll shadow; product detail page uses two-column layout (image left, details right) |
| Wide | > 1440px | Max-width container (1440px) centered; product grid expands to four columns; hero banner remains 480px but content is centered with larger margins; typography scales up slightly (display-xl to 56px) |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44x44px touch target on mobile and tablet.
- Product card swatches are 32x32px with 8px spacing to prevent mis-taps.
- Quantity selector buttons are 40x40px, exceeding the minimum for reliable use.
- Nav-bar hamburger icon is 48x48px.
- Search bar pill is 48px tall, easy to tap on mobile.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer.
- The secondary navigation (category strip) collapses into a horizontal scrollable row on mobile and tablet.
- Product filters collapse into a bottom sheet or modal on mobile.
- The footer’s multi-column layout collapses into a single column on mobile, with accordion-style sections for link groups.
- The hero banner’s secondary text and smaller CTAs are hidden on mobile, leaving only the primary headline and CTA.
- Product image galleries switch from a thumbnail strip to a swipeable carousel on mobile.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Hover and focus states for all components beyond the primary button and text input could not be reliably extracted from the live site’s CSS. Specific values for `:hover`, `:focus`, `:active`, and `:visited` on secondary buttons, links, and navigation items are inferred from common patterns.
- Error styling for form components (text-input error icon, error message typography and spacing) is not fully documented; the error border color is set to `{colors.primary}` but the full error state (icon, message placement) is a best-guess.
- Dark mode is not supported by the current site; no dark-mode token overrides are defined.
- Sub-brand palettes (Fenty Skin, Fenty Fragrance) may have distinct accent colors not captured in the main system. The `accent-*` tokens cover the most common secondary colors observed.
- The exact `font-weight` values for the Brown and Loud typefaces are estimated based on common usage (600 for bold, 400 for regular); the actual font files may have different weight mappings.
- Animation and transition durations (e.g., button hover, nav-bar scroll shadow, accordion expand) are not specified; a default 200ms ease-in-out is assumed.
- The `product-card` hover state (shadow, scale, or border change) was not consistently observed; no hover token is defined.
- The `search-bar` autocomplete/suggestion dropdown styling is not documented.
- Accessibility-focused tokens (focus-visible outlines, high-contrast mode overrides) are not present in the extracted data.
