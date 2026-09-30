---
version: alpha
name: "SturmGlow (Dr. Barbara Sturm)"
source_url: "https://www.drsturm.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A clinical-luxury skincare system built on a foundation of scientific precision and minimalist restraint, where the single anchor color `#313131` — a deep, warm charcoal — carries the weight of every primary CTA, navigation link, and headline, projecting an aura of understated authority rather than overt promotion. The brand speaks in the quiet language of the dermatologist's office: a pure white canvas (`{colors.canvas}`) allows product photography and ingredient stories to breathe, while soft surfaces (`{colors.surface-soft}`) and card backgrounds (`{colors.surface-card}`) create subtle depth without visual noise. Typography runs system-native through -apple-system, BlinkMacSystemFont, and Segoe UI — a deliberate choice that prioritizes legibility and performance over decorative type, reinforcing the brand's "science first" ethos. Rounded corners are sparingly applied: pills and badges use `{rounded.full}` for a touch of approachability, while cards and inputs land at `{rounded.md}` (12px) — enough to soften the clinical edge without sacrificing the brand's professional credibility. The overall feeling is that of a luxury medical spa: calm, precise, and utterly confident in its own expertise, where every pixel serves the product, not the personality.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#1a1a1a"
  body: "#313131"
  muted: "#6b6b6b"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-glow: "#c4a882"
  badge-new: "#313131"
  badge-sale: "#c13515"
  star-rating: "#313131"
  scrim: "#000000"
  error: "#c13515"
  success: "#2e7d32"
  info: "#1565c0"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px rgba(49,49,49,0.1)"
  text-input-error:
    border: "1px solid {colors.error}"
    textColor: "{colors.error}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  select:
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
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.04)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-banner-image:
    rounded: "{rounded.none}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    marginTop: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px rgba(49,49,49,0.1)"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    textDecoration: none
  footer-link-hover:
    textDecoration: underline
  footer-heading:
    typography: "{typography.micro-label}"
    textColor: "{colors.on-primary}"
    marginBottom: "{spacing.base}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    padding: "{spacing.base} 0"
    typography: "{typography.title-sm}"
  accordion-content:
    padding: "0 0 {spacing.base}"
    typography: "{typography.body-sm}"
  tab-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  tab-inactive:
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
  tab-hover:
    textColor: "{colors.primary}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px
  ingredient-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  price-display:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  price-display-sale:
    textColor: "{colors.badge-sale}"
  price-display-original:
    textColor: "{colors.muted}"
    textDecoration: line-through
    typography: "{typography.body-md}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 44px
    width: 44px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    padding: "0 {spacing.xs}"
  notification-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  notification-banner-success:
    backgroundColor: "{colors.success}"
  notification-banner-error:
    backgroundColor: "{colors.error}"
  notification-banner-info:
    backgroundColor: "{colors.info}"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.12)"
  modal-close:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 10px"
    fontSize: 12px
  checkbox:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  radio:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  radio-checked:
    border: "6px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature charcoal `{colors.primary}` with white text and a subtle 8px rounded corner. On hover, the background deepens to `{colors.primary-active}` (#1a1a1a). When disabled, it fades to `{colors.primary-disabled}` (#a0a0a0) with reduced opacity. Uppercase label uses `{typography.button-md}` (14px, 500 weight, 0.5px letter-spacing) for a clinical, authoritative feel. Height is 44px with 12px/24px padding.

**`button-secondary`** — An outlined variant with a white background, charcoal text, and a 1px solid `{colors.primary}` border. Active state inverts the background to `{colors.surface-soft}` with a darker border. Used for "Add to Cart" alternatives, "Learn More" links, and secondary form actions. Same dimensions and typography as primary.

**`button-tertiary-text`** — A text-only button with no background or border, using `{colors.primary}` text. Used for "Cancel", "Skip", and inline navigation links within forms and modals. Maintains the same uppercase `{typography.button-md}` styling.

**`button-pill-primary`** — A compact, fully rounded variant (9999px) for badges, tags, and filter chips. Uses `{typography.button-sm}` (12px uppercase) with 10px/20px padding and 36px height. Appears in category strips and as "NEW" indicators on product cards.

### Cards
**`product-card`** — The primary product display unit, a white card with 12px rounded corners and a subtle 1px/3px shadow. The image area occupies the top half with matching top-rounded corners. Title uses `{typography.title-sm}` (16px, 500 weight), price uses `{typography.body-md}` (16px, 400 weight). On hover, the shadow deepens to 4px/12px. Badges are positioned absolutely at the top-left with `{rounded.full}` pill styling.

**`hero-banner`** — A full-width section with a soft gray background (`{colors.surface-soft}`), generous padding (64px top/bottom), and a minimum height of 400px. Headlines use `{typography.display-xl}` (32px, 300 weight) for a light, airy feel. The CTA button sits below with extra top margin.

### Navigation
**`nav-bar`** — A fixed 72px white bar with a subtle bottom border (`{colors.hairline-soft}`). Navigation links use `{typography.nav-link}` (13px uppercase, 500 weight). Active links show a 2px bottom border in `{colors.primary}`. On scroll, a light box-shadow appears. The bar collapses to a hamburger menu on mobile.

**`search-bar`** — A fully rounded (9999px) input field with 48px height, white background, and a light border. On focus, the border switches to `{colors.primary}` with a subtle 2px ring. Placeholder text uses `{colors.muted}`.

### Forms
**`text-input`** — Standard 48px input with 12px rounded corners, white background, and a `{colors.hairline}` border. Focus state adds a primary-colored border and a 2px ring at 10% opacity. Error state switches to `{colors.error}` (#c13515). Includes textarea variant with matching styling.

**`checkbox`** and **`radio`** — 20px square/round controls with `{colors.hairline}` borders. Checked state fills with `{colors.primary}`. Radio buttons use a 6px inner dot pattern.

**`select`** — Matches text-input dimensions with a custom dropdown arrow. Uses `{typography.body-md}`.

**`quantity-selector`** — A compact 44px control with increment/decrement buttons on either side, separated by a central number display. Buttons use `{colors.surface-soft}` background.

### Footer
**`footer`** — A full-width charcoal section (`{colors.primary}`) with white text. Links are white with no underline by default, gaining underline on hover. Headings use `{typography.micro-label}` (12px uppercase) for clear section hierarchy. Padding is 48px top/bottom.

### Modals & Notifications
**`modal-overlay`** — A 50% opacity black scrim covering the viewport. The modal content sits centered with 12px rounded corners, 32px padding, and a 8px/32px shadow.

**`notification-banner`** — A full-width bar in `{colors.primary}` with white text. Variants use `{colors.success}` (green), `{colors.error}` (red), and `{colors.info}` (blue) backgrounds.

### Badges & Tags
**`ingredient-badge`** — A fully rounded pill with `{colors.surface-soft}` background and `{typography.caption-sm}` text. Used for ingredient highlights (e.g., "Hyaluronic Acid", "Vitamin C").

**`product-card-badge`** — A small charcoal pill positioned at the top-left of product images. Uses `{typography.badge}` (11px uppercase, 600 weight) for "NEW" or "BESTSELLER" labels.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack; hero banner reduces padding to 32px; font sizes scale down one step; search bar becomes full-width; footer links stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav remains visible with condensed links; hero banner uses 48px padding; side-by-side form layouts; footer uses 2-column grid |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero banner at full 64px padding; standard form layouts; footer uses 4-column grid |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid can expand to 4 columns; hero banner may include full-bleed imagery |

### Touch Targets
- All interactive elements maintain minimum 44px height (buttons, inputs, links)
- Icon buttons and quantity controls use 44px × 44px touch targets
- Checkboxes and radios use 20px with 44px clickable area via padding
- Bottom nav links have 48px tap targets on mobile
- Close buttons in modals use 32px minimum with 44px padding

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Footer grid collapses from 4 columns to 1 column on mobile
- Hero banner text stacks vertically on mobile (image behind text)
- Accordion replaces tabbed content below 744px
- Sidebar filters collapse to a bottom sheet on mobile
- Multi-step forms collapse to single-page scroll on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for tertiary buttons and text links could not be reliably extracted
- Error state styling for forms (icons, helper text positioning) is inferred from common patterns
- Sub-brand or collection-specific color palettes (e.g., "The Cream", "The Serum") are not captured
- Dark mode styling is not present on the live site and therefore not defined
- Animation and transition timing values (durations, easing curves) are not extracted
- Focus-visible ring styles for keyboard navigation are assumed but not confirmed
- Product swatch colors (for shade variants) are not captured
- Loading states (spinners, skeleton screens) are not defined
- Dropdown menu styling (mega menu, flyout) is not captured
- Video player controls and styling are not included
- Cookie consent banner and GDPR-specific styling is not captured
- Print stylesheet overrides are not defined
- Custom scrollbar styling is not present on the live site
- Internationalization (RTL) layout adjustments are not captured
- Accessibility contrast ratios for all color combinations have not been verified
- Specific font weights for system fonts (e.g., 300 vs 400) are inferred from common usage
- Letter-spacing values for headlines are estimated based on brand tone
- Line-height values are calculated from common readability standards
- Shadow depths for cards and modals are approximated from visual inspection
- Border radius values for cards and inputs are estimated from screenshot analysis
