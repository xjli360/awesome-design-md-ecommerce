---
version: alpha
name: "Ritual"
source_url: "https://ritual.com"
captured_at: "2026-09-28T04:10:46.922280+00:00"
evidence_status: "historical_partial_css_evidence"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep navy (#142b6f) anchors Ritual's entire experience — not as a background but as the brand's primary identity color, appearing on every key CTA, the site header, and the signature subscription flow. This is a brand that communicates scientific rigor through color rather than clinical sterility: the navy reads as authoritative without being cold, paired with a warm marigold (#ffd600) that appears exclusively on the "Add to Cart" button and select promotional badges, creating a visual voltage that says "trust this product" rather than "buy this thing." The supporting palette is intentionally muted — a pale blue-gray (#a1aac5) for secondary text and borders, a whisper-light off-white (#eaeef0) for the main canvas, and a restrained charcoal (#141414) for body copy. What makes Ritual's system distinctive is the absence of a true white background: the canvas is always slightly tinted (#eaeef0 or #fcf8ee), giving every page a soft, editorial warmth that distinguishes it from the stark white of supplement competitors. Typography runs CircularXX at moderate weights — display headlines sit at 500 weight rather than the heavy 700s of clinical brands, and body copy at 400 with generous line-height (1.6) creates a reading experience closer to a premium magazine than a nutrition label. The brand's visual signature is the "see-through" product photography — clear capsules with visible ingredients — which the UI supports with generous whitespace, soft card radii ({rounded.md}), and a complete absence of hard visual edges. Every interaction feels considered but not precious: buttons have a subtle 8px rounding ({rounded.sm}), input fields use a 4px rounding ({rounded.xs}), and the only full-pill radius ({rounded.full}) appears on the search bar and the "Subscribe" badge, marking those as the two most important user actions.

colors:
  primary: "#142b6f"
  primary-active: "#0f2259"
  primary-disabled: "#8a95b7"
  ink: "#141414"
  body: "#2b2727"
  muted: "#717171"
  muted-soft: "#a1aac5"
  hairline: "#dedede"
  hairline-soft: "#e8e6e5"
  canvas: "#eaeef0"
  surface-soft: "#f5f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#ffd600"
  accent-marigold-active: "#e6c100"
  accent-terracotta: "#c83d1e"
  accent-sage: "#4c840d"
  accent-sand: "#f6ede0"
  accent-warm-white: "#fcf8ee"
  badge-new: "#ffd600"
  badge-subscribe: "#142b6f"
  star-rating: "#ffd600"
  error: "#c83d1e"
  success: "#4c840d"
  link: "#0b38bd"

typography:
  display-xl:
    fontFamily: "'CircularXX', 'CircularXX', sans-serif"
    fontSize: 42px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'CircularXX', 'CircularXX', sans-serif"
    fontSize: 34px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'CircularXX', 'CircularXX', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'CircularXX', 'CircularXX', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'CircularXX', 'CircularXX', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'CircularXX', 'CircularXX', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'CircularXX', 'CircularXX', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'CircularXX', 'CircularXX', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'CircularXX', 'CircularXX', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "'CircularXX', 'CircularXX', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'CircularXX', 'CircularXX', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'CircularXX', 'CircularXX', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'CircularXX', 'CircularXX', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'CircularXX', 'CircularXX', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  nav-link:
    fontFamily: "'CircularXX', 'CircularXX', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0

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
    padding: 14px 28px
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-marigold-active:
    backgroundColor: "{colors.accent-marigold-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.link}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.accent-marigold}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    opacity: 0.8
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-subscribe:
    backgroundColor: "{colors.badge-subscribe}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-sale:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.85
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  accordion-header:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    fillColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 6px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
  modal-overlay:
    backgroundColor: "rgba(0, 0, 0, 0.5)"
  modal-content:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Subscribe", and "Start Your Ritual". Solid navy (#142b6f) background with white text, 8px rounding ({rounded.sm}), and 48px height. On hover, shifts to a slightly darker navy (#0f2259). Disabled state uses a muted blue-gray (#8a95b7) to indicate unavailability without visual noise.

**`button-secondary`** — Outline-style button for secondary actions like "Learn More" or "View Details". White background with navy text and a 1px navy border. Maintains the same 48px height and 8px rounding as the primary button for visual consistency. Hover state fills the background with navy at 10% opacity.

**`button-accent-marigold`** — High-energy accent button reserved for promotional CTAs, limited-time offers, and the "Subscribe & Save" upsell. Marigold (#ffd600) background with dark ink (#141414) text. On hover, darkens to (#e6c100). This button carries the brand's emotional voltage — use sparingly.

**`button-text-link`** — Minimal text-only button for inline actions like "See ingredients" or "Read reviews". Uses the brand's link blue (#0b38bd) and the link typography token. No background or border — purely text, with underline on hover.

### Navigation
**`nav-bar`** — Fixed top navigation bar at 72px height, solid navy (#142b6f) background with white text. Contains the Ritual logo (left), product category links (center), and utility icons (cart, account, search — right). The search icon triggers the search bar pill.

**`nav-link-active`** — Active navigation link with a 2px marigold (#ffd600) bottom border underline. White text at full opacity.

**`nav-link-inactive`** — Inactive navigation link at 80% opacity white. On hover, returns to full opacity.

### Cards
**`product-card`** — Product display card with white background, 12px rounding ({rounded.md}), and 16px padding. Contains a product image (8px rounding), title (title-sm typography), price (body-md), and a star rating. Cards sit on the tinted canvas (#eaeef0) background, creating a subtle floating effect.

**`badge-new`** — Pill-shaped badge for "New" or "Just Launched" indicators. Marigold (#ffd600) background with dark ink text. Uses uppercase badge typography with 0.5px letter-spacing.

**`badge-subscribe`** — Pill-shaped badge for subscription-eligible products. Navy (#142b6f) background with white text. Same typography and shape as badge-new, but uses the brand's primary color to signal trust and commitment.

**`badge-sale`** — Pill-shaped badge for sale or discount items. Terracotta (#c83d1e) background with white text. Used sparingly to avoid visual noise.

### Forms
**`text-input`** — Standard text input field with white background, 4px rounding ({rounded.xs}), 48px height, and a 1px hairline (#dedede) border. On focus, the border thickens to 2px and shifts to navy (#142b6f). Placeholder text uses muted (#717171) color.

**`search-bar-pill`** — Full-pill-radius search input at 48px height. White background with muted placeholder text. Used in the navigation bar and on the search results page. The pill shape signals this is the primary discovery action.

**`toggle-switch`** — Pill-shaped toggle for subscription preferences (monthly vs. every 2 months). 24px height, gray (#dedede) background when off, navy (#142b6f) when active. The circular knob is white.

**`progress-bar`** — Thin (6px) pill-shaped progress bar for the subscription quiz flow. Light gray (#e8e6e5) background track with navy (#142b6f) fill. The quiz uses this to show step completion without numeric indicators.

### Overlays
**`modal-overlay`** — Semi-transparent black (50% opacity) scrim behind modals and the mobile navigation drawer.

**`modal-content`** — White card with 12px rounding ({rounded.md}) and 32px padding. Used for ingredient detail popups, subscription confirmation, and the cart drawer.

**`tooltip`** — Dark ink (#141414) background with white text, 4px rounding, and 8px/12px padding. Used for ingredient hover states and feature explanations.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to 28px; search bar moves to drawer |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero uses 34px display; search bar remains in nav |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 42px display; search bar pill visible in nav |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to four columns; hero text remains at 42px with increased whitespace |

### Touch Targets
- All buttons and interactive elements minimum 44px height (buttons are 48px, meeting WCAG 2.1 touch target requirements)
- Navigation links have minimum 44px tap area even when text is smaller
- Product card tap targets (title, price, image) are the full card width
- Toggle switches are 24px height with 44px minimum touch area via padding
- Badges are minimum 28px height for touch interaction

### Collapsing Strategy
- Navigation collapses to a hamburger menu at < 744px, with the full nav appearing in a slide-in drawer from the left
- Product grids collapse from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- The hero section collapses from a two-column layout (text + product image) to a single stacked column on mobile
- The footer collapses from a four-column link grid to a single-column accordion on mobile
- The search bar collapses from an inline pill in the nav to a full-screen overlay on mobile
- Subscription quiz steps collapse from a side-by-side layout to stacked cards on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Hover and focus states for secondary buttons, text inputs, and navigation links were inferred from common patterns rather than extracted from the live site
- Error state styling (form validation, API errors) could not be reliably extracted — the error color (#c83d1e) is an educated guess based on the extracted hex list
- Dark mode is not present on the live site and no dark mode tokens are defined
- The extracted font list includes "Dutch801 Rm BT" and "Dutch801 Rm BT Headline" which may be used for specific editorial content or print materials — these are not included in the primary typography system as they appear infrequently on the live site
- The extracted hex list includes several colors (#4b3dc4, #db7f16, #e4c25e, #ffef99, #fff7cc) that may be used for specific promotional campaigns or seasonal badges — these are not included in the core palette
- Animation durations and easing curves (transitions, hover effects, page loads) were not extractable from static analysis
- The subscription quiz flow (multi-step questionnaire) has specific component states (active step, completed step, future step) that could not be fully reverse-engineered
- Mobile navigation drawer animation and overlay behavior was inferred from common patterns
- The "See-through" product photography treatment (clear capsules with visible ingredients) is a content strategy decision that affects component layout but is not a design token
