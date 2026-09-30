---
version: alpha
name: "Logitech G"
source_url: "https://www.logitechg.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-voltage gaming gear brand that runs on a near-black chassis (#1b1b1b) and a single neon-blue accent (#00b8fc) that reads as cold cathode, not friendly sky. The palette is deliberately sparse — three grays (#d7d7d7, #f2f2f2, #1b1b1b) and two electric accents (#00fdcf, #00b8fc) — creating a system where the accent color becomes the sole visual event on every page. Buttons and interactive elements use `{rounded.sm}` (8px) rather than pills, preserving a tool-like precision that matches the brand's peripheral hardware. The site's Japanese title (ロジクール G -先進のゲーミングギアと周辺機器) signals a global-first approach, with product photography doing the heavy lifting of texture and material feel. The green accent (#20a50a) appears sparingly as a status indicator, never as a primary action color. This is a brand that trusts its hardware photography and its single electric blue to communicate speed and precision — no gradients, no decorative flourishes, just dark canvas and one bright signal.

colors:
  primary: "#00b8fc"
  primary-active: "#0099d4"
  primary-disabled: "#004466"
  ink: "#1b1b1b"
  body: "#d7d7d7"
  muted: "#999999"
  muted-soft: "#666666"
  hairline: "#333333"
  hairline-soft: "#2a2a2a"
  canvas: "#1b1b1b"
  surface-soft: "#2a2a2a"
  surface-card: "#222222"
  on-primary: "#1b1b1b"
  accent-cyan: "#00fdcf"
  accent-green: "#20a50a"
  accent-green-active: "#178008"
  surface-light: "#f2f2f2"
  surface-light-card: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Arial, 'Noto Sans JP', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
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
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-accent-green-active:
    backgroundColor: "{colors.accent-green-active}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.accent-green}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 56px
  badge-new:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-feature:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  search-bar-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.primary}"
  footer-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
  category-tile-hover:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption-uppercase}"
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  spec-table-row-alt:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
  toggle-switch-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
  toggle-switch-thumb:
    backgroundColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 20px
  toggle-switch-thumb-active:
    backgroundColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 20px
  slider-track:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  slider-track-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  slider-thumb:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 20px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the brand's electric blue (#00b8fc) on a near-black background. On hover, it shifts to a deeper blue (#0099d4) for state feedback. The disabled state drops to a muted dark blue (#004466) with gray text, signaling unavailability without visual noise. The 8px corner radius (`{rounded.sm}`) keeps the button feeling like precision hardware rather than a friendly pill.

**`button-secondary`** — A dark-surface variant that sits on the near-black canvas with a slightly lighter background (#2a2a2a) and light gray text (#d7d7d7). On hover, the background moves to the hairline color (#333333), creating a subtle lift. Used for secondary actions like "Learn More" or "Compare" alongside primary buttons.

**`button-ghost`** — A transparent-background button with light gray text, used for tertiary actions in dense layouts. On hover, it gains a dark surface background (#2a2a2a) for affordance. Common in product detail pages for "Add to Wishlist" or "Share" actions.

**`button-accent-cyan`** — The secondary accent button using the cyan (#00fdcf) from the extracted palette. This is reserved for special promotional actions or "New" product launches where the brand wants a different voltage than the primary blue. Text is near-black (#1b1b1b) for contrast.

**`button-accent-green`** — A smaller, compact button using the green accent (#20a50a), exclusively for status indicators like "In Stock" or "Add to Cart" when stock is confirmed. On hover, it darkens to a deeper green (#178008). The 36px height makes it suitable for inline use in product cards.

### Cards
**`product-card`** — The primary product display unit, using a slightly lighter dark surface (#222222) than the canvas (#1b1b1b) to create depth through value contrast rather than shadow. The 8px radius (`{rounded.sm}`) matches the button system. On hover, the card background shifts to the surface-soft color (#2a2a2a), providing a subtle state change without animation. Product images sit in a same-radius container, maintaining the system's consistent corner language.

**`category-tile`** — A navigation tile for product categories, using the surface-soft background (#2a2a2a) with title-sm typography. On hover, the background moves to the hairline color (#333333), creating a clear selection state. Used in the main navigation dropdown and category landing pages.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height on the near-black canvas. The scrolled state reduces to 56px, creating a more compact reading experience. Navigation links use 14px medium-weight type with 0 letter-spacing, and the active state switches to the primary blue (#00b8fc). The brand logo sits left-aligned, with primary navigation links center-aligned and utility icons (search, cart, account) right-aligned.

**`nav-link-active`** — The active navigation link uses the primary blue (#00b8fc) against the dark canvas, creating a clear signal of current section. Inactive links use the muted gray (#999999), receding into the background until hovered.

### Forms
**`text-input`** — A dark-themed input field with surface-soft background (#2a2a2a) and light gray text (#d7d7d7). The focus state adds a primary blue border (#00b8fc) without changing the background, maintaining the dark aesthetic. Error states use the green accent (#20a50a) as a border color — an unusual choice that signals "correctable" rather than "dangerous."

**`toggle-switch`** — A pill-shaped toggle with a 24px height, using the hairline color (#333333) for the off state and primary blue (#00b8fc) for the on state. The thumb is a 20px circle that slides horizontally, using the body color (#d7d7d7) off and on-primary (#1b1b1b) on. Used for settings like "RGB Lighting" or "On-Board Memory."

**`slider-track`** — A thin (4px) pill-shaped track for DPI or sensitivity adjustments. The active portion uses primary blue (#00b8fc), while the inactive portion uses the hairline color (#333333). The thumb is a 20px circle in primary blue, providing a clear grab target.

### Badges
**`badge-new`** — A compact cyan (#00fdcf) badge with near-black text (#1b1b1b), used exclusively for new product launches. The 4px radius (`{rounded.xs}`) and 11px uppercase type create a technical, precision feel. The badge sits at the top-left corner of product images.

**`badge-sale`** — A green (#20a50a) badge with dark text (#1b1b1b), used for promotional pricing. Same dimensions as the new badge but with a different accent color to distinguish the message type.

**`badge-feature`** — A primary blue (#00b8fc) badge with near-black text (#1b1b1b), used for highlighting specific product features like "Wireless" or "Ultra-Light." This is the most common badge type, appearing on product cards and category pages.

### Footer
**`footer-section`** — A full-width footer on the near-black canvas with muted gray (#999999) body text. Links use the lighter body color (#d7d7d7) and shift to primary blue (#00b8fc) on hover. The footer is organized in a multi-column grid with section headers in caption-uppercase typography.

### Hero
**`hero-section`** — The primary hero area using the near-black canvas with display-xl typography. The hero CTA uses the button-lg size (56px height) with primary blue background, creating a strong visual anchor. Product photography or lifestyle imagery fills the hero background, with text overlay in the body color (#d7d7d7).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, nav collapses to hamburger menu, hero text reduces to display-lg, product cards stack vertically, search becomes icon-only |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but condensed, hero maintains display-xl but with reduced padding, category tiles in 3-column grid |
| Desktop | 1128–1440px | Full layout with 4-column product grid, expanded nav with all links visible, hero at full size, category tiles in 4-column grid |
| Wide | > 1440px | Max-width container at 1440px, centered layout with increased whitespace, product grid expands to 5 columns, hero content centered |

### Touch Targets
- All interactive elements maintain minimum 44px height on mobile
- Product card tap targets (buttons, links) are minimum 48px
- Toggle switches and sliders maintain 24px height with 44px touch area
- Navigation hamburger icon is 48px × 48px
- Search icon button is 48px × 48px
- Cart icon button is 48px × 48px

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product filters collapse to a slide-out drawer on mobile
- Product image galleries collapse to single-image carousel on mobile
- Footer multi-column grid collapses to single-column stacked layout on mobile
- Category tiles collapse from 4-column to 2-column on tablet, single-column on mobile
- Hero content reduces font size and padding on mobile, with CTA stacking vertically if needed

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were found during extraction; the typography block uses a system font stack as a reasonable default. The actual brand font (likely a custom or licensed gaming typeface) could not be determined.
- The extracted hex colors (#d7d7d7, #00fdcf, #1b1b1b, #f2f2f2, #00b8fc, #20a50a) appear to be a mix of brand colors and generic web palette. The near-black (#1b1b1b) and electric blue (#00b8fc) are the most distinctive and likely brand primaries, but the cyan (#00fdcf) and green (#20a50a) may be secondary accents or could be from third-party widgets.
- Hover states for all components are inferred from common dark-theme patterns; actual hover colors may differ.
- Error states for forms (validation messages, error icons) could not be extracted.
- Dark mode is not applicable as the site already uses a dark canvas; a light mode variant may exist but was not detected.
- Sub-brand palettes (Logitech G vs. standard Logitech) could not be distinguished.
- Animation timing, easing curves, and transition durations were not extractable.
- Shadow values (box-shadow, drop-shadow) were not extractable from the static analysis.
- The green accent (#20a50a) may be a stock "in stock" indicator color rather than a brand color; its usage should be verified against actual product pages.
- The surface-light (#f2f2f2) and surface-light-card (#ffffff) tokens are inferred for potential light-themed sections; their actual usage is unconfirmed.
