---
version: alpha
name: "Seed"
source_url: "https://seed.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A single hex — #313131 — governs the entire Seed experience, a dark, almost-black ink that reads as deliberate restraint rather than accident. The brand sells live bacteria for the gut, but the interface never reaches for the probiotic pastels or earthy greens that wellness competitors default to; instead it lays a monochrome foundation where science photography — petri dishes, capsules, microscope imagery — provides the only color. The site loads behind a Cloudflare challenge page ("Just a moment..."), which means the extracted palette is thin, but what remains is a system built on high-contrast typography against white canvas, with no rounded corners softer than {rounded.sm} and no decorative gradients. Seed’s voice is clinical but warm: body copy runs at 16px in system-ui stacks, captions at 13px, and the primary action — typically "Add to Cart" or "Learn More" — sits inside a #313131 pill with white text, a button that feels more like a seal than a call to action. The brand trusts its product shots and ingredient diagrams to carry emotional weight; the UI stays out of the way, using hairline-thin borders ({colors.hairline}) and generous vertical spacing ({spacing.section}) to create a reading rhythm closer to a scientific journal than a DTC storefront. There is no secondary accent color — no teal, no amber, no rose — which makes the rare appearance of a product image or clinical illustration feel like a deliberate reveal. The typography stack is pure system default: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif, with Apple Color Emoji and Noto Color Emoji appended for symbol support. This is a brand that refuses to perform friendliness; it performs authority instead.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#757575"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#313131"
  link-hover: "#1a1a1a"
  error: "#d32f2f"
  success: "#2e7d32"
  badge-science: "#313131"
  badge-new: "#313131"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  legal:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
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
  checkbox:
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    size: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-science}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.base}"
  hero-headline:
    typography: "{typography.display-xl}"
    maxWidth: 720px
  hero-subheadline:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    maxWidth: 560px
  hero-cta:
    marginTop: "{spacing.lg}"
  section-header:
    typography: "{typography.display-md}"
    padding: "0 0 {spacing.base}"
  section-subheader:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "0 0 {spacing.base}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.primary}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.lg} 0"
  ingredient-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  rating-stars:
    color: "{colors.primary}"
    size: 16px
  trust-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  testimonial-author:
    typography: "{typography.caption}"
    fontWeight: 600
    marginTop: "{spacing.base}"
  faq-item:
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  faq-question:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  faq-answer:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    paddingTop: "{spacing.sm}"
  science-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    borderLeft: "4px solid {colors.primary}"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  skeleton-loader:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    height: 16px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  modal-overlay:
    backgroundColor: "rgba(49, 49, 49, 0.6)"
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    maxWidth: 600px
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    size: 32px
  notification-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  notification-banner-error:
    backgroundColor: "#fdecea"
    textColor: "{colors.error}"
  notification-banner-success:
    backgroundColor: "#e8f5e9"
    textColor: "{colors.success}"

## Components

### Buttons
**`button-primary`** — The primary CTA is a full-pill button in #313131 with white text, 15px/600 weight, and 32px horizontal padding. On hover it deepens to #1a1a1a. The disabled state uses #a0a0a0 text on a lighter background. The secondary variant inverts to a white fill with a 2px #313131 border, shifting to #f5f5f5 on hover. A tertiary text-only button exists for inline actions like "Read the science" — no border, no background, just the ink color and underline on hover.

### Navigation
**`nav-bar`** — A fixed 72px white bar with a single hairline bottom border. Navigation links run at 14px/500 weight in #313131, with the active page indicated by a 2px bottom border in the same ink. The logo sits left-aligned, typically in display-sm weight. On mobile, the nav collapses into a hamburger menu with a full-screen overlay drawer.

### Cards
**`product-card`** — A white card with 8px rounding, no shadow, and a 1:1 product image that rounds only at the top corners. The title uses title-sm (16px/600), the price uses body-md with 600 weight, and a science badge (11px uppercase, full-pill, #313131 fill) overlays the image top-left. No drop shadow — the card relies on the image and typography hierarchy alone.

### Forms
**`text-input`** — Standard 48px input with 4px rounding, a 1px #e0e0e0 border, and 16px body copy. On focus the border thickens to 2px #313131. Error state swaps to #d32f2f. Checkboxes are 20px squares with 2px rounding, filled #313131 when checked. Selects mirror the input styling with a custom chevron.

### Footer
**`footer`** — A #f5f5f5 section with body-sm copy at #4a4a4a. Links run at 14px/500 in #757575, darkening to #313131 on hover. The layout uses a multi-column grid with section-level padding (80px vertical). A thin divider separates legal text at the bottom.

### Science Callouts
**`science-callout`** — A #f5f5f5 box with 4px rounding, 24px padding, and a 4px #313131 left border. Used for ingredient breakdowns, clinical study summaries, and "how it works" explanations. Body copy runs at 14px with 1.57 line height.

### Accordion
**`accordion-trigger`** — A border-bottom row with title-sm weight, no background, and 16px vertical padding. The content panel drops in below with body-md at #4a4a4a. Used extensively on product pages for FAQ and ingredient detail.

### Badges
**`ingredient-badge`** — Small full-pill tags in #f5f5f5 with 12px/400 copy. Used to label probiotic strains (e.g., "L. plantarum", "B. longum"). The science badge variant uses #313131 fill with white uppercase text for "NEW" or "CLINICALLY STUDIED" flags.

### Trust Elements
**`trust-badge`** — A bordered box with caption-sm copy, used for "Free Shipping", "30-Day Guarantee", "Third-Party Tested" icons. No rounding beyond 4px. `testimonial-card` uses the soft surface background with 8px rounding and a 16px/1.625 body for quote text, with the author name in caption weight below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; hero headline drops to 28px; product cards stack full-width; accordions become the primary content reveal; footer stacks vertically; CTA buttons become full-width. |
| Tablet | 744–1128px | Two-column product grids; nav links remain visible but condensed; hero maintains 36px headline; side-by-side science callouts; footer uses 2-column grid. |
| Desktop | 1128–1440px | Three-column product grids; full nav with all links; hero max-width constrained to 720px; multi-column footer; ingredient badges in flex-wrap rows. |
| Wide | > 1440px | Content max-width at 1200px centered; hero and section headers align to a 12-column grid; product cards can span 4 columns; extra whitespace on left/right. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height.
- Icon-only buttons (close, hamburger, search) are 44x44px with 9999px rounding.
- Accordion triggers are full-width with 48px minimum tap height.
- Checkbox and radio targets include a 44x44px invisible hit area.

### Collapsing Strategy
- Top navigation collapses to a hamburger icon at < 744px; the menu opens as a full-screen overlay with vertical link stack and 48px tap targets.
- Multi-column footer collapses to a single vertical stack at < 744px, with accordion-style section headers for "Shop", "Learn", "Support", "Company".
- Product image galleries collapse from thumbnail strip to single-image swipe at < 744px.
- Side-by-side science callouts and ingredient grids collapse to single-column at < 744px.
- Hero sections reduce headline size and stack CTA buttons vertically at < 744px.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extractable from the live site due to Cloudflare challenge page blocking full CSS/HTML access. The remaining color tokens (muted, hairline, surface-soft, etc.) are inferred from common DTC wellness patterns and the brand's monochrome design language — they may not match the live site exactly.
- No secondary or accent color could be extracted. Seed may use a brand accent (e.g., a deep green or muted gold) on the actual product pages behind the challenge wall.
- Font-family declarations are system defaults only. Seed may use a custom typeface (e.g., a licensed sans-serif like Graphik or Untitled Sans) on the live site that was not exposed during extraction.
- Hover, focus, active, and disabled states for all components are inferred from common accessibility patterns and the brand's high-contrast ethos — not extracted from live CSS.
- Error, success, and warning color tokens are generic WCAG-compliant values, not brand-specific.
- No dark mode tokens were found. The brand may support dark mode on product pages.
- Button padding values (14px 32px) are estimated from common DTC patterns and the brand's minimalist aesthetic; actual live values may differ.
- Rounded corner values (4px for inputs, 8px for cards, full for buttons) are inferred from the brand's clinical, no-nonsense design language — the live site may use slightly different radii.
- Spacing scale (section: 80px) is an estimate based on typical editorial wellness layouts; actual vertical rhythm may vary.
- No animation or transition timing data was extractable. The brand likely uses subtle fades and slides (200-300ms ease-in-out) but this is unconfirmed.
- Product card aspect ratio (1:1) is assumed from common supplement DTC patterns; actual product images may use 4:5 or 3:4.
- The brand's checkout flow, cart drawer, and account pages were not accessible during extraction.
