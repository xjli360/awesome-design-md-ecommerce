---
version: alpha
name: "Hers"
source_url: "https://www.forhers.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A direct-to-consumer wellness brand that uses a single, unapologetic dark gray — #313131 — as its anchor, a choice that reads as clinical, serious, and trustworthy in a category that often defaults to pastels or aspirational whites. This ink-like primary sits on a pure white canvas (#ffffff), creating a high-contrast, almost editorial layout where product photography and medical-grade copy do the heavy lifting. The typography stack is a system-native fallback chain (system-ui, -apple-system, sans-serif), suggesting a pragmatic, load-speed-first approach rather than a bespoke typeface investment; the brand trusts its color and photography to carry personality. Buttons are softly rectangular ({rounded.sm} ~8px), and the overall spacing is generous — section padding at 64px, card padding at 24px — giving the interface a clean, unhurried breathing room that feels more like a doctor's office brochure than a frantic e-commerce store. There is no bright accent color; the brand's visual tension comes from the interplay of #313131 against white, with subtle gray dividers (#e0e0e0) and muted body text (#6b6b6b) creating hierarchy without noise. The overall mood is one of quiet authority: a brand that sells prescription-grade treatments and wants you to take them seriously.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#6b6b6b"
  muted: "#8c8c8c"
  muted-soft: "#b3b3b3"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#d32f2f"
  success: "#2e7d32"
  link: "#1a73e8"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
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
    padding: 14px 24px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: 2px solid "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: 2px solid "{colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: 1px solid "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    margin-top: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    margin-top: "{spacing.xs}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
    border: 1px solid "{colors.primary}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.body}"
  footer-link-hover:
    color: "{colors.primary}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border-bottom: 1px solid "{colors.hairline}"
    padding: "{spacing.base} 0"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for checkout, sign-up, and key conversion points. Rendered in the brand's signature dark gray (#313131) with white text, softly rounded at 8px. On hover, the background deepens to `{colors.primary-active}` (#1a1a1a). The disabled state uses a lighter gray (`{colors.primary-disabled}`) to visually deprioritize the action.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details." Uses a white background with a 2px solid border in `{colors.primary}`. On hover, the background shifts to `{colors.surface-soft}` (#f7f7f7) and the border to `{colors.primary-active}`.

**`button-tertiary-text`** — A text-only button for subtle actions like "Cancel" or "Skip." No background or border; uses `{colors.primary}` for the text. On hover, the text darkens to `{colors.primary-active}`.

### Forms
**`text-input`** — Standard text input for forms, with a white background, 1px `{colors.hairline}` border, and 8px rounded corners. On focus, the border thickens to 2px and switches to `{colors.primary}`. Error state uses a red border (`{colors.error}`). Placeholder text uses `{colors.muted}`.

### Navigation
**`nav-bar`** — A fixed top navigation bar, 64px tall, with a white background and a subtle 1px bottom border in `{colors.hairline}`. Navigation links use `{typography.nav-link}` at 14px weight 600. The bar is sticky on scroll.

### Cards
**`product-card`** — A product listing card with a white background, 8px rounded corners, and 16px padding. The product image sits at the top with its own 8px rounding. Below, the title uses `{typography.title-sm}` and the price uses `{typography.body-md}` in `{colors.primary}`.

### Hero
**`hero-section`** — A full-width hero banner with a white background, centered content, and generous padding (64px top/bottom, 24px sides). The headline uses `{typography.display-xl}`. A primary CTA button (`{hero-cta}`) sits below the headline.

### Badges
**`badge`** — A small, uppercase label used for "NEW," "BESTSELLER," or "PRESCRIPTION REQUIRED." Uses `{colors.primary}` background with white text, 4px rounding, and tight padding (2px 8px). An outlined variant (`{badge-outline}`) inverts the colors for use on colored backgrounds.

### Footer
**`footer-section`** — A full-width footer with a light gray background (`{colors.surface-soft}`) and body-colored text. Links use `{typography.link}` and shift to `{colors.primary}` on hover. The section has 64px padding top and bottom.

### Accordion
**`accordion`** — A collapsible content panel used for FAQ sections. Each item has a white background, a bottom border in `{colors.hairline}`, and 16px padding. The header uses `{typography.title-sm}` and is clickable to reveal the content below, which uses `{typography.body-sm}` in `{colors.body}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav bar collapses to hamburger menu; product cards stack vertically; hero text reduces to 24px; section padding reduces to 32px |
| Tablet | 744–1128px | Two-column grid for product cards; nav links visible but condensed; hero text at 28px; section padding at 48px |
| Desktop | 1128–1440px | Three-column grid for product cards; full nav bar with all links; hero text at 32px; standard section padding at 64px |
| Wide | > 1440px | Max-width container at 1440px; content centered; no further layout changes |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Primary CTA buttons are 48px tall to exceed the minimum.
- Nav bar links have 48px tap areas even if the text is smaller.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer.
- Product grids collapse from 3 columns (desktop) to 2 (tablet) to 1 (mobile).
- Hero sections reduce padding and font size on mobile to avoid overflow.
- Footer links collapse into a single column on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was reliably extracted from the live site. All other colors (primary-active, disabled, body, muted, hairline, etc.) are inferred from common design patterns and may not match the exact brand implementation.
- No font-family declarations beyond the system-native stack were found. The brand may use a custom typeface (e.g., a licensed font) that is loaded via JavaScript or a CDN not captured in the extraction.
- Hover, focus, and active states for all components are estimated based on standard accessibility and design conventions. Exact transition durations, box shadows, and border-radius values for interactive states are unknown.
- Error, success, and link colors are generic defaults and may not reflect the brand's specific palette.
- Dark mode, if supported, was not detected. All colors assume a light theme.
- The extracted color list was extremely sparse (only one color after framework filtering), so the brand's true secondary palette (if any) could not be determined. The design system above assumes a monochromatic approach, but the brand may use additional accent colors not captured.
