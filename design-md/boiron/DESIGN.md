---
version: alpha
name: "Boiron"
source_url: "https://boironusa.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep blue (#0033ab) anchors Boiron's digital presence—a color that reads as clinical authority without the coldness of a pure navy, appearing across primary buttons, navigation bars, and footer backgrounds. The palette is dominated by a family of blues (#0170b9, #0274be, #0073c6, #003388, #003399, #0070ad) that create a layered, trustworthy hierarchy, while a secondary teal (#00acad) and sage green (#77a464) appear as accent colors for dosage indicators and wellness badges. The canvas is a warm off-white (#f9f9f9) rather than pure white, softening the clinical edge, with surfaces stepping through #fafafa, #fbfbfb, and #f5f5f5 for card and section differentiation. Typography runs Montserrat for display and Open Sans for body—a pairing that balances geometric modernity with readable warmth. Buttons use tight {rounded.sm} corners (8px), while informational badges and dosage pills adopt {rounded.full} for a friendly, approachable feel. The overall mood is that of a clean pharmacy counter: organized, reassuring, and quietly competent, with the blue family doing the heavy lifting of trust-building while the teal and sage provide moments of wellness-oriented optimism.

colors:
  primary: "#0033ab"
  primary-active: "#002a8e"
  primary-disabled: "#8fa8d5"
  ink: "#111111"
  body: "#3a3a3a"
  muted: "#777777"
  muted-soft: "#808285"
  hairline: "#d9d9d9"
  hairline-soft: "#e6e6e6"
  canvas: "#f9f9f9"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#00acad"
  accent-sage: "#77a464"
  accent-blue-light: "#dfedf3"
  accent-blue-mid: "#0170b9"
  accent-blue-dark: "#003388"
  badge-green: "#61a229"
  badge-gray: "#4b4f58"
  footer-bg: "#003399"
  footer-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.accent-blue-light}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-teal-accent:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  text-input-error:
    border: "1px solid #c13515"
    rounded: "{rounded.sm}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  logo-container:
    height: 40px
    padding: "0 {spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.surface-card}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-badge:
    backgroundColor: "{colors.accent-blue-light}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-badge-green:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-badge-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  dosage-pill:
    backgroundColor: "{colors.accent-blue-light}"
    textColor: "{colors.accent-blue-dark}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  dosage-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
    opacity: 0.85
  footer-link-hover:
    opacity: 1
    textDecoration: underline
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
  tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 20px"
  tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 20px"
  hero-banner:
    backgroundColor: "{colors.accent-blue-light}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  info-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  info-card-icon:
    width: 48px
    height: 48px
    rounded: "{rounded.full}"
    backgroundColor: "{colors.accent-blue-light}"
  divider:
    height: 1px
    backgroundColor: "{colors.hairline}"
    margin: "{spacing.lg} 0"
  divider-soft:
    height: 1px
    backgroundColor: "{colors.hairline-soft}"
    margin: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in deep blue (#0033ab) with white text and 8px rounded corners. On hover, it darkens to #002a8e; when disabled, it fades to a muted blue-gray (#8fa8d5) with reduced opacity. The button uses Montserrat 600 at 15px with 0.2px letter spacing for a confident, pharmaceutical-grade presence. Minimum height is 44px with 12px vertical and 28px horizontal padding.

**`button-secondary`** — An outlined variant with a white fill, 2px solid primary-blue border, and primary-blue text. Hover state fills the background with the lightest blue tint (#dfedf3) and darkens the border to the active blue. Used for secondary actions like "Learn More" or "View Ingredients" alongside primary buttons.

**`button-tertiary-text`** — A text-only button with no background or border, using primary-blue Montserrat 600. Appears in contexts where a visual button would be too heavy, such as inline links within product descriptions or accordion headers.

**`button-teal-accent`** — A pill-shaped button using the accent teal (#00acad) with white text, reserved for wellness-oriented CTAs like "Find Relief" or "Explore Natural Solutions." The full rounded shape and smaller padding (8px vertical, 20px horizontal) distinguish it from the primary button family.

### Text Inputs & Forms
**`text-input`** — Standard single-line text input with white background, 14px horizontal padding, 44px height, and a light gray border (#d9d9d9). On focus, the border thickens to 2px and shifts to primary blue. Error state uses a red border (#c13515) with a 14px error message below in Open Sans caption weight.

**`select-input`** — Dropdown select styled identically to text inputs in dimensions and border treatment, with a custom chevron icon in muted gray. The dropdown panel uses the same surface-card white with a subtle shadow.

### Navigation
**`nav-bar`** — A 72px fixed header with white background, subtle bottom border (#e6e6e6), and uppercase Montserrat 600 navigation links at 14px. The logo container sits at 40px height with 16px horizontal padding. On scroll, a light box-shadow (0 2px 8px rgba(0,0,0,0.08)) replaces the bottom border for depth.

**`nav-link-active`** — Active navigation link with primary-blue text and a 3px solid blue bottom border. Inactive links render in muted gray (#777777) with no underline or border.

### Cards & Products
**`product-card`** — A white card with 12px rounded corners, 16px padding, a subtle border (#ebebeb), and a light drop shadow (0 1px 3px rgba(0,0,0,0.06)). On hover, the shadow deepens to 0 4px 12px rgba(0,0,0,0.1) and the border strengthens to #d9d9d9. The product image area maintains a 1:1 aspect ratio with 8px rounded corners.

**`product-badge`** — Small pill-shaped badges in light blue (#dfedf3) with dark blue text (#003388), using uppercase Montserrat 700 at 11px. Variants include green (#61a229) for "In Stock" or "New" indicators, and teal (#00acad) for "Natural" or "Wellness" tags.

**`dosage-pill`** — Small interactive pills for dosage selection, using the light blue background with dark blue text. The active state fills with primary blue and white text, creating a clear selected/unselected toggle.

### Footer
**`footer-section`** — A deep blue (#003399) footer spanning the full width, with white text at 85% opacity for links and full opacity for headings. Links underline on hover and return to full opacity. The section uses 64px vertical padding with 24px horizontal padding for content containment.

### Accordion & Tabs
**`accordion-header`** — Expandable section headers with a light gray background (#f5f5f5), 12px rounded corners, and Montserrat 600 at 14px. The content area below uses white background with 16px padding and Open Sans body text.

**`tab-active`** / **`tab-inactive`** — Tab navigation components with primary blue fill for active state and light gray fill for inactive. Both use 8px rounded corners and 8px vertical / 20px horizontal padding. Active tabs use white text; inactive tabs use muted gray text.

### Hero & Info Cards
**`hero-banner`** — Full-width promotional banner with light blue background (#dfedf3), large Montserrat display text, and a primary blue CTA button. Uses 64px vertical padding for generous breathing room.

**`info-card`** — Informational content card with white background, 12px rounded corners, 24px padding, and a subtle border. Includes a 48px circular icon container in light blue for visual hierarchy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack full-width; hero banner reduces to 32px vertical padding; dosage pills wrap to multiple rows; accordion becomes default for all section content |
| Tablet | 744–1128px | Two-column product grid; nav links visible but reduced to 5 items with "More" dropdown; search bar shrinks to icon-only with expandable input; footer columns arrange in 2x2 grid |
| Desktop | 1128–1440px | Full navigation with all links; three-column product grid; search bar fully visible; footer in 4-column layout; hero banner at full padding |
| Wide | > 1440px | Max-width container at 1440px with centered content; product grid expands to 4 columns; additional whitespace on left/right of hero banner |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product cards use full-card tap target area (no small hit zones)
- Dosage pills maintain minimum 36px height and 44px width for finger taps
- Accordion headers use full-width tap targets at 44px minimum height
- Tab items use minimum 40px height with adequate spacing between items

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px, with slide-in drawer from left
- Search bar collapses to icon-only below 744px, expanding to full-width overlay on tap
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer columns collapse from 4 to 2 at tablet breakpoint, stacking to single column on mobile
- Section padding reduces from 64px to 48px at tablet, 32px at mobile
- Hero banner text size reduces proportionally, with CTA button moving below headline on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for all components could not be fully extracted; primary-active (#002a8e) is inferred from common darkening patterns
- Error states for forms (red border, error message styling) are assumed from industry standards, not extracted from live site
- Focus ring styles (color, offset, thickness) were not present in extracted CSS
- Sub-brand or category-specific color palettes (e.g., for children's products, specific ailments) could not be identified
- Dark mode or high-contrast mode styles are not present in the extracted data
- Animation durations, easing curves, and transition properties were not reliably extractable
- The exact font weights used for Montserrat and Open Sans in production may vary from the 400/600/700 weights assumed here
- Spacing values are inferred from common patterns; exact padding/margin values may differ in production
- The accent teal (#00acad) and sage green (#77a464) appear in the extracted colors but their specific usage contexts (badges, icons, backgrounds) are inferred
- Mobile navigation drawer behavior (animation, overlay, close button) was not extractable from static CSS
- Print stylesheet and email-specific styling are not represented
