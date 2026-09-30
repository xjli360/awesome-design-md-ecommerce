---
version: alpha
name: "Le Chat qui Fume"
source_url: "https://www.lechatquifume.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A Parisian movie-merchandise storefront that feels like a late-night cinema lobby — deep charcoal walls (#121212) absorbing the glow of a single blue neon sign (#334fb4). The brand operates in two registers: a nocturnal, almost monochrome base (ink-black backgrounds, silver-gray body text at #dedede, soft dove-gray surfaces at #f3f3f3) and a single electric-blue accent that appears on the primary CTA, the shopping-bag icon, and the category badges. That blue (#334fb4) is the only color that escapes the dark; it reads less like a brand color and more like the light from a projector spilling onto a black curtain. Typography runs Assistant at moderate weights (300–500) for body and Lato for display headings — a pairing that splits the difference between French film-poster serifs and modern e-commerce legibility. Product cards sit on the dark canvas with a subtle #242833 surface, using {rounded.sm} corners that feel precise rather than friendly. The overall mood is cult-cinema serious: no gradients, no playful illustrations, no soft shadows. Every element earns its place by being either purely functional (the search bar, the cart count) or purely atmospheric (the film-strip divider, the monochrome hero image).

colors:
  primary: "#334fb4"
  primary-active: "#2a4199"
  primary-disabled: "#6b7fc9"
  ink: "#121212"
  body: "#dedede"
  muted: "#a0a0a0"
  muted-soft: "#c0c0c0"
  hairline: "#3a3a3a"
  hairline-soft: "#2a2a2a"
  canvas: "#121212"
  surface-soft: "#242833"
  surface-card: "#242833"
  on-primary: "#ffffff"
  on-dark: "#dedede"
  badge-bg: "#334fb4"
  badge-text: "#ffffff"
  star-rating: "#f5a623"
  error: "#e74c3c"
  success: "#2ecc71"

typography:
  display-xl:
    fontFamily: "'Lato', 'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Lato', 'Assistant', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Lato', 'Assistant', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Lato', 'Assistant', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Assistant', 'Lato', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Assistant', 'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', 'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'Lato', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Assistant', 'Lato', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Assistant', 'Lato', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Assistant', 'Lato', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Lato', 'Assistant', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Lato', 'Assistant', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
  link:
    fontFamily: "'Assistant', 'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lato', 'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 6px
  md: 10px
  lg: 16px
  xl: 24px
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  search-icon:
    color: "{colors.muted}"
    size: 18px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: 1
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.body}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.body}"
    typography: "{typography.display-xl}"
    height: 480px
  hero-overlay:
    backgroundColor: "#000000"
    opacity: 0.4
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: 48px 24px
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.primary}"
  cart-icon:
    color: "{colors.body}"
    size: 22px
  cart-count-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: 2px 6px
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  error-message:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px

## Components

### Buttons
**`button-primary`** — The single electric-blue CTA (#334fb4) on a dark canvas. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, darkens to #2a4199 (`{colors.primary-active}`). Disabled state shifts to a muted blue (#6b7fc9) with reduced opacity. Text is white, set in Lato 600 at 15px with 0.5px letter spacing for a slightly cinematic weight.

**`button-secondary`** — A dark-surface button (#242833) with silver-gray text (#dedede). Used for secondary actions like "View Details" or "Continue Shopping". Active state sinks into the full black canvas (#121212). No border — relies on the surface contrast against the ink background.

**`button-tertiary-text`** — A text-only button with no background. Used for links like "Cancel" or "Learn More". Inherits the body text color and sits flush against the dark canvas.

### Text Inputs
**`text-input`** — A dark-surface input field (#242833) with silver-gray placeholder text. Focus state reveals a 2px blue border (#334fb4) — the only time a border appears in the system. Padding is generous (12px 16px) for a 44px height. Used for search, email capture, and checkout forms.

### Navigation
**`nav-bar`** — A fixed 64px bar on the full ink background (#121212). Navigation links are uppercase Lato 600 at 14px with 0.5px tracking. Active links glow blue (#334fb4); inactive links sit at muted gray (#a0a0a0). The brand logo (typically a cat silhouette or "LE CHAT QUI FUME" in Lato) sits left-aligned. The cart icon with a blue count badge sits right-aligned.

### Product Cards
**`product-card`** — A square-format card on a #242833 surface with 6px rounded corners. The product image fills the top with a 1:1 aspect ratio and matching corner radius. Title is Assistant 500 at 16px in silver-gray; price is Assistant 400 at 16px in blue (#334fb4). A small uppercase badge (e.g., "NEW" or "SOLD OUT") sits in the top-left corner on a blue background with 2px padding and 2px rounded corners.

### Hero Section
**`hero-section`** — A full-width, 480px-tall section on the ink canvas. Typically features a monochrome or desaturated film-still image with a 40% black overlay. The headline is Lato 700 at 36px in silver-gray. No CTA in the hero — the brand lets the imagery breathe.

### Footer
**`footer`** — A dense, text-heavy footer on the ink background. Links are Assistant 400 at 14px in muted gray (#a0a0a0), turning blue on hover. Sections include "Collections", "About", "Help", and social links. A thin 1px hairline (#3a3a3a) separates the footer from the main content.

### Badges & Tags
**`product-card-badge`** — A small uppercase label (11px, 600 weight, 0.5px tracking) on a blue background with white text. Used for "NEW", "EXCLUSIVE", or "SOLD OUT". 2px padding, 2px rounded corners.

**`category-tag`** — A pill-shaped tag (full rounded) on a dark surface (#242833) with silver-gray text. Used for filtering by category (e.g., "Horror", "Sci-Fi", "Cult"). Active state fills with blue.

### Dividers
**`divider`** — A 1px hairline in #3a3a3a. Used sparingly — between sections, below the nav, above the footer. The brand prefers whitespace over lines.

### Loading & Error States
**`loading-spinner`** — A 24px blue spinner (#334fb4) centered on the dark canvas. No text — the brand trusts the visual.

**`error-message`** — A red (#e74c3c) banner with white text, 6px rounded corners, and 12px 16px padding. Used for form validation, out-of-stock notifications, and API errors.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; hero height reduces to 320px; search bar moves below nav; footer stacks vertically |
| Tablet | 744–1128px | Nav shows 4–5 links; product cards in 2-column grid; hero height at 400px; search bar inline in nav |
| Desktop | 1128–1440px | Full nav (6+ links); product cards in 3-column grid; hero at 480px; search bar with expanded input |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero may include parallax effect |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Nav links have a 48px tap area (even if text is smaller).
- Product card tap targets (image, title, price) are each independently tappable with a 44px minimum.
- Category tags have 14px horizontal padding to ensure easy tapping on mobile.

### Collapsing Strategy
- On mobile, the top nav collapses into a hamburger menu with a slide-in drawer from the left.
- The category filter strip collapses into a horizontal scrollable row with a "See All" expand button.
- The footer collapses from a 4-column layout to a single-column accordion (each section toggles open/close).
- Product image galleries collapse from a 4-thumbnail row to a single swipeable carousel.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were inferred from the extracted colors and common patterns; actual live-site hover animations (e.g., scale, shadow) were not extractable.
- Error and success states (form validation, toast notifications) were not present in the extracted data; colors are placeholders based on convention.
- The extracted font list ("Assistant, Lato") may be incomplete — there could be additional fallback stacks or a third font for decorative headings that wasn't captured.
- The meta theme-color was absent; the brand likely uses the ink (#121212) as the browser chrome color, but this is unconfirmed.
- Sub-brand or collection-specific palettes (e.g., limited-edition drops with different accent colors) were not observed.
- Dark mode is irrelevant here — the entire site is already dark — but a light-mode variant was not extracted.
- The extracted hex list included only 5 colors; the brand may use additional tones (e.g., a warm accent for sale badges, a green for in-stock indicators) that weren't present in the sampled pages.
- Checkout-widget colors (Shopify Pay, Klarna, Afterpay) were filtered out but may appear in the live cart flow.
