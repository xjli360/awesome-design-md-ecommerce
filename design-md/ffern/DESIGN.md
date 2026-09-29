---
version: alpha
name: "Ffern"
source_url: "https://ffern.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Ffern is a British fragrance house that operates on a seasonal ledger — four bottles a year, no more, no less. The brand's visual language is a slow, tactile poem written in parchment and earth. The canvas is not white but a warm, living off-white (`#faf9f7`), the meta theme-color that sets the stage for a palette drawn from dried petals, bark, and stone. The dominant hue, `#f5f2ec`, is the color of unbleached linen, while `#e8e2d5` and `#d2c2af` read as aged paper and sun-bleached wood. Accents arrive as mineral greys (`#9b9b9b`, `#868686`, `#717267`) and deep, resinous browns (`#835436`, `#a36f4d`, `#66594a`), with a single, deliberate pop of warmth in `#e2976e` and `#fbbd54` — like a sliver of amber catching light. The typography is a quiet conversation between FfernType, a proprietary serif that carries the weight of tradition, and FfernTypeMono, a monospace that whispers of apothecary labels and botanical catalogues. There are no hard corners in the Ffern world; `{rounded.full}` is the default for buttons and badges, while `{rounded.lg}` (20px) and `{rounded.md}` (12px) soften cards and containers, making every interaction feel like handling a smooth, water-worn stone. The brand's signature design move is the absence of urgency — generous whitespace, low-contrast text in `{colors.ink}` (#585858) against `{colors.canvas}` (#faf9f7), and a deliberate avoidance of aggressive CTAs. The primary button, `{colors.primary}` (#bd957b), is the color of a worn leather journal, not a call to action but an invitation to pause.

colors:
  primary: "#bd957b"
  primary-active: "#a36f4d"
  primary-disabled: "#d2c2af"
  ink: "#585858"
  body: "#7e7469"
  muted: "#9b9b9b"
  muted-soft: "#cac9c6"
  hairline: "#dcdcdc"
  hairline-soft: "#e5e0d8"
  canvas: "#faf9f7"
  surface-soft: "#f5f2ec"
  surface-card: "#fcfbf7"
  on-primary: "#faf9f7"
  accent-warm: "#e2976e"
  accent-gold: "#fbbd54"
  accent-deep: "#835436"
  accent-charcoal: "#717267"
  badge-new: "#e2976e"
  badge-sold-out: "#9b9b9b"
  star-rating: "#fbbd54"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'FfernType', 'Spectral', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'FfernType', 'Spectral', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'FfernType', 'Spectral', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'FfernType', 'Spectral', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'FfernType', 'Spectral', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'FfernType', 'Spectral', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'FfernType', 'Spectral', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'FfernType', 'Spectral', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'FfernTypeMono', 'SFMono-Regular', 'Consolas', 'Liberation Mono', 'Menlo', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'FfernTypeMono', 'SFMono-Regular', 'Consolas', 'Liberation Mono', 'Menlo', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'FfernTypeMono', 'SFMono-Regular', 'Consolas', 'Liberation Mono', 'Menlo', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "'FfernType', 'Spectral', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'FfernTypeMono', 'SFMono-Regular', 'Consolas', 'Liberation Mono', 'Menlo', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'FfernTypeMono', 'SFMono-Regular', 'Consolas', 'Liberation Mono', 'Menlo', monospace"
    fontSize: 10px
    fontWeight: 400
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
  section: 80px

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
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill-warm:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-warm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  hero-heading:
    typography: "{typography.display-xl}"
    maxWidth: 720px
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 560px
    marginTop: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.body}"
  footer-link-hover:
    textColor: "{colors.ink}"
  social-icon:
    textColor: "{colors.muted}"
    height: 24px
  social-icon-hover:
    textColor: "{colors.ink}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
  accordion-body:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    paddingTop: "{spacing.sm}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  star-rating-empty:
    color: "{colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in a full-pill shape using `{rounded.full}`. The background is `{colors.primary}` (#bd957b), a warm, muted leather-brown that feels organic and grounded, not aggressive. Text is set in `{typography.button-md}`, a monospace uppercase at 13px with 1px letter-spacing, in `{colors.on-primary}` (#faf9f7). On hover, the background deepens to `{colors.primary-active}` (#a36f4d). The disabled state uses `{colors.primary-disabled}` (#d2c2af) with `{colors.muted}` text, signaling a faded, inert presence.

**`button-secondary`** — A ghost button with a transparent background and a single `{colors.hairline}` (#dcdcdc) border. Text is `{colors.ink}` (#585858) in the same monospace uppercase. On hover, the background fills with `{colors.surface-soft}` (#f5f2ec) and the border shifts to `{colors.ink}`. This button is used for secondary actions like "Learn More" or "Add to Wishlist," where the primary button carries the main intent.

**`button-tertiary-text`** — A plain text button with no background or border. It uses `{typography.button-md}` and `{colors.ink}`. This is the quietest option, reserved for links within content or subtle actions like "Cancel" or "View Details."

**`button-pill-warm`** — A smaller, accent-driven pill using `{colors.accent-warm}` (#e2976e), a soft terracotta. Typography is `{typography.button-sm}` (11px monospace uppercase). Used for promotional badges or seasonal callouts, such as "Spring Edition" or "Limited Release."

### Cards
**`product-card`** — The primary container for fragrance listings. It sits on `{colors.surface-card}` (#fcfbf7), a slightly warmer white than the canvas, with `{rounded.lg}` (20px) corners and `{spacing.base}` (16px) padding. The product image is contained within `{rounded.md}` (12px) to create a nested softness. The title uses `{typography.title-sm}` (16px serif), and the price is set in `{typography.body-sm}` (14px serif) in `{colors.body}` (#7e7469). There is no shadow — the card relies on the subtle contrast between `{colors.surface-card}` and the `{colors.canvas}` background.

**`hero-section`** — The full-width hero area, backed by `{colors.surface-soft}` (#f5f2ec). The heading is `{typography.display-xl}` (48px serif) with a max-width of 720px, and the subheading is `{typography.body-md}` (16px serif) in `{colors.body}` at 560px max-width. The section padding is `{spacing.section}` (80px) vertically and `{spacing.xl}` (32px) horizontally. This is the brand's most expansive layout, designed to feel like a gallery wall.

### Navigation
**`nav-bar`** — A fixed-height (72px) bar on `{colors.canvas}` with a single `{colors.hairline-soft}` (#e5e0d8) bottom border. Links are set in `{typography.nav-link}`, a 12px monospace uppercase with 0.5px letter-spacing. The active state is indicated by a 1px solid `{colors.ink}` bottom border on the link itself. Inactive links are `{colors.muted}` (#9b9b9b). The nav carries the brand logo (typically a wordmark in `{typography.display-sm}`) on the left, with links centered or right-aligned.

### Forms
**`text-input`** — A simple, bordered input on `{colors.canvas}` with `{rounded.sm}` (8px) corners. The border is `{colors.hairline}` (#dcdcdc) at rest, shifting to `{colors.primary}` (#bd957b) on focus. Error states use `{colors.accent-warm}` (#e2976e) for the border. Typography is `{typography.body-md}` (16px serif) in `{colors.ink}`. Padding is 12px vertical, 16px horizontal, with a total height of 48px.

### Badges
**`badge-new`** — A small, full-pill badge using `{colors.badge-new}` (#e2976e) as background. Text is `{typography.badge}` (10px monospace uppercase) in `{colors.on-primary}`. Padding is 4px vertical, 12px horizontal. Used to flag new seasonal fragrances.

**`badge-sold-out`** — Identical shape and typography to `badge-new`, but with a `{colors.badge-sold-out}` (#9b9b9b) background. This badge is deliberately muted, signaling unavailability without visual urgency.

### Footer
**`footer`** — A full-width section on `{colors.surface-soft}` (#f5f2ec). Links are `{typography.link}` (14px serif, underlined) in `{colors.body}` (#7e7469), shifting to `{colors.ink}` on hover. Social icons are 24px tall in `{colors.muted}`, darkening to `{colors.ink}` on hover. The footer layout typically includes columns for "About," "Help," and "Social," with the brand's mailing address and copyright in `{typography.caption}` (12px monospace uppercase).

### Accordion
**`accordion`** — A collapsible panel for FAQs or product details. The container is `{colors.canvas}` with a `{colors.hairline-soft}` border and `{rounded.sm}` (8px) corners. The header uses `{typography.title-sm}` (16px serif) in `{colors.ink}`, and the body uses `{typography.body-sm}` (14px serif) in `{colors.body}` with `{spacing.sm}` (8px) top padding. This component is used extensively on product pages to describe scent notes, ingredients, and shipping details.

### Star Rating
**`star-rating`** — A 16px star icon in `{colors.star-rating}` (#fbbd54), a warm gold. Empty stars are rendered in `{colors.hairline}` (#dcdcdc). The component is typically placed below the product title on cards and above the price.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; hero heading reduces to `{typography.display-lg}` (36px); product cards stack vertically; footer links stack; search bar reduces to icon-only; accordions expand by default. |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but reduce font-size to 11px; hero section padding reduces to `{spacing.xxl}` (48px) vertical; footer splits into two rows. |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero heading at `{typography.display-xl}` (48px); standard section padding of 80px. |
| Wide | > 1440px | Max-width container at 1440px, centered; hero heading max-width expands to 800px; product grid can show four columns; increased whitespace around all components. |

### Touch Targets
- All buttons and interactive elements maintain a minimum height of 48px on mobile.
- Nav links have a minimum tap area of 44x44px.
- Accordion headers have a minimum height of 48px for easy tapping.
- Social icons are 24px with 12px padding, exceeding the 44px touch target when grouped.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu. The brand logo remains visible.
- The product grid collapses from 3 columns to 2 (tablet) to 1 (mobile).
- The footer link columns collapse into a single vertical stack on mobile.
- The hero section reduces its heading size and padding to fit smaller screens.
- Accordions are fully expanded by default on mobile to reduce the need for tapping.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover and focus states for all components (e.g., `button-secondary` hover border color, `text-input` focus ring) could not be reliably extracted from the live site CSS.
- Error styling for forms (e.g., error message typography, icon placement) is inferred from the accent-warm color but not confirmed.
- Dark mode is not present on the site; no dark palette tokens exist.
- Sub-brand or seasonal palette variations (e.g., for limited editions) are not captured.
- The exact `font-weight` values for FfernType and FfernTypeMono are not known; weights are assumed to be 400 (regular) based on the brand's restrained aesthetic.
- `letter-spacing` and `line-height` values for some typography tokens are estimated based on common serif and monospace conventions.
- The `star-rating` component's exact icon path or SVG is not specified.
- The `search-bar` component's clear button and dropdown behavior are not documented.
- The `nav-bar`'s mobile hamburger menu animation and overlay behavior are not specified.
- The `product-card`'s hover state (e.g., subtle shadow or border change) is not confirmed.
