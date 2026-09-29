---
version: alpha
name: "Tekla"
source_url: "https://teklafabrics.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A quiet, tactile luxury brand for the bath and home, Tekla operates on a restrained palette anchored by near-black `#181818` and soft off-white `#f6f6f6`. The brand’s signature move is the absence of visual noise — a deliberate sparseness that lets material and form speak. Primary actions pulse in a sharp, unapologetic red (`#fd2121`), a single accent that cuts through the monochrome calm with surgical precision. Secondary reds (`#ff0000`, `#f04747`) suggest hover and error states, while muted grays (`#9ca3af`, `#9e9e9d`, `#5c5c5c`) handle secondary text and borders. A single green (`#149d22`) appears for stock or availability indicators, the only non-neutral, non-red color in the system. Typography leans on system-ui and sans-serif stacks, avoiding custom typefaces in favor of clean, legible utility. Corners are soft but not pill-like — `{rounded.sm}` (8px) for buttons, `{rounded.md}` (12px) for cards — creating a gentle, approachable feel without sacrificing precision. The overall mood is one of edited restraint: a brand that trusts its product photography, its negative space, and its singular red accent to do all the work.

colors:
  primary: "#fd2121"
  primary-active: "#ff0000"
  primary-disabled: "#f04747"
  ink: "#181818"
  body: "#5c5c5c"
  muted: "#9ca3af"
  muted-soft: "#9e9e9d"
  hairline: "#9ca3af"
  hairline-soft: "#9e9e9d"
  canvas: "#f6f6f6"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  stock-green: "#149d22"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0px
  display-md:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0px
  title-md:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0px
  body-md:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body-sm:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  caption:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px
  button-md:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
    textDecoration: underline
  nav-link:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 10px
    fontWeight: 600
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
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
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 2px rgba(0,0,0,0.05)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.canvas}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    maxWidth: "600px"
  hero-subtext:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginTop: "{spacing.base}"
  badge-stock:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  accordion:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-header:
    typography: "{typography.title-md}"
    padding: "{spacing.sm} 0"
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
    height: 44px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "0 12px"
    height: 44px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand’s signature red (`#fd2121`) with white text and an 8px rounded corner. Hover state deepens to `#ff0000`; disabled state fades to `#f04747`. Text is uppercase, 14px, medium weight, with 0.5px letter-spacing. Padding is 12px vertical, 24px horizontal, yielding a 44px tall button that feels substantial but not heavy.

**`button-secondary`** — An outlined alternative on the soft off-white canvas (`#f6f6f6`), using the near-black ink (`#181818`) for text and a 1px solid border. Same sizing and typography as primary, but inverted — used for “Add to Cart” secondary actions or “View Details” links where the red would overwhelm.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like “Cancel” or “Clear.” Typography matches the other buttons, but the lack of container keeps it visually subordinate.

### Cards
**`product-card`** — A white card with 12px rounded corners and 16px padding, housing a square product image (8px rounded) and two text rows: the product title in 18px medium weight, and the price in 14px body gray (`#5c5c5c`). The card has no shadow or border — it relies on the contrast between the white surface and the soft canvas (`#f6f6f6`) background to define its boundaries.

### Navigation
**`nav-bar`** — A 64px tall, white bar with uppercase 14px medium-weight links. Sticky variant gains a subtle 1px shadow (`rgba(0,0,0,0.05)`) on scroll. The bar is anchored by the brand’s near-black logo on the left and a compact set of links (Shop, Journal, About) on the right, with a search icon and cart icon.

**`search-bar`** — A pill-shaped input (9999px radius) with a 1px hairline border, 48px tall, 12px vertical and 20px horizontal padding. On focus, the border switches from gray (`#9ca3af`) to near-black (`#181818`). The bar sits in the nav or a dedicated search overlay.

### Forms
**`text-input`** — A 48px tall input with 8px rounded corners, 12px vertical and 16px horizontal padding, and a 1px hairline border. Focus state swaps the border to near-black; error state swaps to the primary red. The background is the soft off-white canvas, keeping the form field visually quiet.

### Footer
**`footer-section`** — A full-width block in the brand’s near-black (`#181818`) with white text, using 14px body-sm typography for links and information. Links are underlined on hover. The section uses 64px vertical padding and 24px horizontal padding, creating a grounded, weighty base for the page.

### Badges
**`badge-stock`** — A small green (`#149d22`) badge with white text, 4px rounded corners, and 2px vertical / 8px horizontal padding. Used to indicate “In Stock” or “Available.” The only non-red, non-neutral color in the system, it reads as a calm affirmative.

**`badge-sale`** — A small red (`#fd2121`) badge with white text, matching the stock badge’s sizing and shape. Used for “Sale” or “Limited Edition” flags.

### Accordion
**`accordion`** — A border-bottom-only container (1px solid `#9e9e9d`) with no background. The header uses 18px medium-weight title typography; the content uses 14px body gray. Used for product details, shipping info, and FAQ sections. The open/close indicator is a simple plus/minus icon in the near-black ink.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to 24px; buttons become full-width; accordion becomes default for all content sections |
| Tablet | 744–1128px | Two-column product grid; nav remains visible but compact; hero text at 28px; search bar moves to overlay |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 32px; search bar inline in nav |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero text remains 32px but with wider max-width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Icon buttons (search, cart, hamburger) are at least 44x44px with 8px internal padding.
- Product card tap targets extend to the full card area, not just the title/price text.
- Accordion headers are 44px minimum tap height.

### Collapsing Strategy
- On mobile, the top navigation collapses to a hamburger menu with a slide-out drawer.
- The search bar collapses from an inline input to a tap-to-open overlay on mobile and tablet.
- Product filters collapse into a bottom sheet or accordion on mobile.
- The footer’s multi-column link layout collapses to a single-column stacked layout below 744px.
- Hero banners reduce from two-column (image + text) to single-column (text stacked above or below image) on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and ghost buttons could not be reliably extracted from the live site; assumed to use a 10% opacity overlay on the ink color.
- Error styling for text inputs (iconography, helper text position) was not observed; only the border color change to primary red is documented.
- Sub-brand or seasonal palette variations (e.g., holiday collections, limited-edition drops) were not captured.
- Dark mode preferences are not supported by the current site; all tokens assume a light canvas.
- Typography scale for mobile (e.g., reduced font sizes below 744px) was not explicitly extracted; the display-xl size is a best-guess based on heading proportions.
- The exact font-family stack is a system-ui fallback; no custom web font was detected in the page’s CSS.
- Animation durations, easing curves, and transition properties were not extracted.
- Focus ring styles (outline, offset, color) were not observed and should default to a 2px solid ink outline.
- The stock-green badge (`#149d22`) was inferred from a single occurrence; its hover/active states are undefined.
- Spacing values for nested components (e.g., product card internal grid gaps) are estimates based on common e-commerce patterns.
