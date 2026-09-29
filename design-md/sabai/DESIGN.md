---
version: alpha
name: "Sabai"
source_url: "https://sabai.design"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Sabai is a furniture brand built on the conviction that sustainability shouldn't mean sacrificing style or convenience. The palette is grounded in warm, earthy neutrals — `#9c8d85`, `#c9bcac`, `#b9afa9` — that feel like sun-baked clay or raw linen, avoiding the sterile grays of fast furniture. A single, deliberate accent of `#ffb600` (a confident, almost mustard yellow) acts as the brand's primary voltage, appearing on CTAs, badges, and key interactive elements, while a secondary `#ff8327` and `#e16a13` add a touch of warmth. The typography leans on the humanist and slightly quirky "Mabry Pro" for display and "Maison Neue" for body, creating a voice that is approachable, editorial, and never corporate. Rounded corners are generous but not cartoonish — `{rounded.md}` (12px) on cards and `{rounded.lg}` (20px) on buttons — softening the hard lines of modernism. The canvas is a warm off-white `#f8f4ef`, not pure white, giving the entire experience the feel of a well-loved, sunlit room. Deep navy `#1d1b3e` and charcoal `#373737` provide contrast for text and structure, while a subtle `#f0eede` and `#f1eedc` hint at a secondary, more botanical or organic layer. The overall mood is one of considered calm — a brand that trusts material honesty and gentle color over aggressive marketing.

colors:
  primary: "#ffb600"
  primary-active: "#e16a13"
  primary-disabled: "#f1eedc"
  ink: "#1d1b3e"
  body: "#373737"
  muted: "#8e7e76"
  muted-soft: "#a99d96"
  hairline: "#c9bcac"
  hairline-soft: "#d3c8bb"
  canvas: "#f8f4ef"
  surface-soft: "#f0eede"
  surface-card: "#ffffff"
  on-primary: "#1d1b3e"
  accent-warm: "#ff8327"
  accent-red: "#cd3824"
  accent-pink: "#ee575a"
  accent-gold: "#ccb560"
  accent-green: "#806e28"
  star-rating: "#ffb600"
  scrim: "#1d1b3e"

typography:
  display-xl:
    fontFamily: "'Mabry Pro', 'Maison Neue', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Mabry Pro', 'Maison Neue', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Mabry Pro', 'Maison Neue', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Mabry Pro', 'Maison Neue', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Maison Neue', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Maison Neue', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Maison Neue', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Maison Neue', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Maison Neue', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Maison Neue', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Maison Neue', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Maison Neue', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Maison Neue', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "'Maison Neue', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Maison Neue', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
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
    rounded: "{rounded.lg}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.sm}"
  badge-sustainable:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: "16px 32px"
    height: 56px
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.section} 0 {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the brand's signature `#ffb600` yellow. Rounded to `{rounded.lg}` (20px) for a friendly, approachable feel. On hover, it transitions to `{colors.primary-active}` (`#e16a13`), a deeper, more grounded orange. The disabled state uses a muted `#f1eedc` background with `{colors.muted}` text, signaling unavailability without visual noise.
**`button-secondary`** — An outlined variant on the warm `{colors.canvas}` background, with a `2px` solid `{colors.hairline}` border. It inherits the same `{rounded.lg}` shape and `{typography.button-md}` size, making it a perfect companion for less critical actions like "Learn More" or "Save for Later."
**`button-tertiary-text`** — A purely text-based button with no background or border. Uses `{colors.ink}` for the label, relying on the `{typography.button-md}` weight for clarity. Used for in-line actions like "Remove" or "Cancel."
**`button-pill-primary`** — A compact, fully rounded (`{rounded.full}`) pill button used for filters, tags, or secondary CTAs. Uses the primary yellow and smaller `{typography.button-sm}` for a dense, scannable UI.

### Cards
**`product-card`** — The core product display unit. A white (`{colors.surface-card}`) card with `{rounded.md}` (12px) corners. The image area is clipped to the top corners only (`{rounded.md} {rounded.md} 0 0`), creating a clear visual hierarchy. The title uses `{typography.title-sm}` and the price uses `{typography.body-md}` in `{colors.body}`. No drop shadow is used, keeping the surface flat and honest.
**`product-card-title`** — The product name, set in `{typography.title-sm}` (16px/600 weight). Padded with `{spacing.sm}` top and `{spacing.base}` sides to create breathing room from the image.
**`product-card-price`** — The price, set in `{typography.body-md}` (16px/400 weight) in `{colors.body}`. Positioned below the title with `{spacing.sm}` bottom padding.

### Badges
**`badge-sustainable`** — A soft, tonal badge on `{colors.surface-soft}` (`#f0eede`) background, signaling eco-friendly materials or practices. Uses `{typography.badge}` (11px/700 weight/uppercase) and `{rounded.full}` for a pill shape.
**`badge-sale`** — A high-contrast badge using `{colors.accent-red}` (`#cd3824`) on a white `{colors.canvas}` background. Used for markdowns or clearance items. Same typography and pill shape as the sustainable badge.
**`badge-new`** — A vibrant badge using the primary `{colors.primary}` yellow on `{colors.on-primary}` text. Used for new arrivals or collections.

### Navigation
**`top-nav`** — A fixed or sticky navigation bar at 72px height on the `{colors.canvas}` background. Uses `{typography.nav-link}` (14px/500 weight) for a clean, uncluttered appearance. The active state is indicated by a `2px` solid `{colors.primary}` bottom border.
**`nav-link-active`** — The active navigation link, distinguished by a subtle `2px` bottom border in `{colors.primary}`. The text remains in `{colors.ink}`.
**`nav-link-inactive`** — Inactive navigation links use `{colors.muted}` (`#8e7e76`) to visually recede, keeping focus on the active section.

### Forms
**`text-input`** — A standard text input with a `1px` `{colors.hairline}` border and `{rounded.sm}` (8px) corners. On focus, the border thickens to `2px` and switches to `{colors.primary}`, providing a clear, warm interaction cue.
**`text-input-focus`** — The focused state of the text input, using a `2px` solid `{colors.primary}` border.
**`select-dropdown`** — A styled select element matching the text input's dimensions and border treatment. Uses `{rounded.sm}` and `{typography.body-md}`.
**`quantity-selector`** — A compact, pill-shaped (`{rounded.full}`) control for adjusting item quantities. Uses a `1px` `{colors.hairline}` border and `{typography.body-md}`.

### Hero & Sections
**`hero-section`** — The primary brand hero, using the `{colors.canvas}` background and `{typography.display-xl}` (48px) for the headline. Padded with `{spacing.section}` (64px) top and bottom to create a commanding presence.
**`hero-cta`** — The hero's primary call-to-action button, larger than standard at 56px height. Uses `{colors.primary}` background and `{rounded.lg}`.
**`section-heading`** — A section-level heading using `{typography.display-md}` (28px). Padded with `{spacing.section}` top and `{spacing.lg}` bottom to establish clear content groupings.

### Footer
**`footer`** — A dark footer on `{colors.ink}` (`#1d1b3e`) background, providing a strong visual anchor at the bottom of the page. Uses `{typography.body-sm}` for general text and `{typography.link}` for navigation links in `{colors.muted-soft}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger menu; hero text scales down to `{typography.display-lg}`; section padding reduces to `{spacing.xxl}`. |
| Tablet | 744–1128px | Two-column product grid; top-nav remains visible but may condense; hero uses `{typography.display-xl}` at smaller scale. |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links visible; standard section padding. |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero may feature a larger background image. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px.
- Icon buttons are 40x40px, exceeding the minimum.
- Product card tap areas cover the entire card surface.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu on mobile (< 744px).
- The product grid collapses from 4 columns to 1 column on mobile.
- The footer's multi-column layout stacks vertically on mobile.
- Hero section padding reduces from `{spacing.section}` to `{spacing.xxl}` on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components (e.g., button-secondary hover, text-input focus ring) are inferred from the primary-active color but not explicitly extracted from the live site.
- Error styling for forms (e.g., error border color, error message typography) is not available.
- Dark mode or high-contrast mode color overrides are not defined.
- Sub-brand or collection-specific palettes (e.g., "The Outdoor Collection") are not captured.
- Specific animation/transition durations and easing curves are not extracted.
- The exact font weights for "Mabry Pro" and "Maison Neue" are inferred from common usage; the site may use additional weights.
- The `{spacing.section}` value is an editorial estimate based on common DTC furniture site patterns.
- The `{typography.display-xl}` font size is an estimate for a hero headline; the actual site may use a different size.
