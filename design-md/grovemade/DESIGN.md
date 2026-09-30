---
version: alpha
name: "Grovemade"
source_url: "https://www.grovemade.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand built on the weight and warmth of natural materials, Grovemade uses a restrained palette anchored by a deep walnut brown (#4a2c2a) that appears in product photography shadows, wood grain textures, and the brand’s signature desk accessories. The canvas is a soft off-white (#f5f2ed) that reads as unbleached paper or raw linen, avoiding the sterile brightness of pure white. Typography runs in a single sans-serif family at moderate weights — there is no bold display headline shouting for attention; instead, the brand lets material texture and generous negative space carry the visual hierarchy. Product cards use a subtle hairline border (#d9d4ce) and a gentle shadow that mimics the way light falls across a wooden desktop. The primary accent is a muted terracotta (#c66b4d) used sparingly on add-to-cart buttons and sale badges, a color that echoes fired clay and contrasts the browns without competing. Rounded corners are minimal — a 4px radius on buttons and 8px on cards — suggesting precision machining rather than softness. The overall mood is one of quiet craft: every element feels cut from a single sheet, with no gratuitous decoration.

colors:
  primary: "#4a2c2a"
  primary-active: "#3a1f1d"
  primary-disabled: "#b8a8a6"
  ink: "#2c1f1d"
  body: "#4a3f3c"
  muted: "#8a7f7a"
  muted-soft: "#b0a8a2"
  hairline: "#d9d4ce"
  hairline-soft: "#e5e0da"
  canvas: "#f5f2ed"
  surface-soft: "#efebe6"
  surface-card: "#faf8f5"
  on-primary: "#f5f2ed"
  accent-terracotta: "#c66b4d"
  accent-terracotta-active: "#a8553a"
  accent-gold: "#c9a96e"
  wood-light: "#d4b896"
  wood-dark: "#6b4c3b"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
  button-terracotta:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-terracotta-active:
    backgroundColor: "{colors.accent-terracotta-active}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    shadow: "0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04)"
  product-card-hover:
    shadow: "0 4px 6px rgba(0,0,0,0.08), 0 2px 4px rgba(0,0,0,0.06)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    padding: "0 {spacing.base} {spacing.base} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    maxWidth: 600px
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    maxWidth: 500px
    marginTop: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.accent-gold}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's deep walnut brown on a soft off-white canvas. Uses uppercase tracking at 0.5px and a precise 4px corner radius that suggests machined wood rather than molded plastic. On hover, the background darkens to `{colors.primary-active}`. The disabled state fades to a muted brown-gray `{colors.primary-disabled}`.

**`button-secondary`** — A ghost button with a single hairline border, used for secondary actions like "Learn More" or "View Details." The background remains transparent until hover, when it picks up `{colors.surface-soft}` and the border shifts to `{colors.primary}`. Text is uppercase with the same tracking as primary.

**`button-terracotta`** — The accent button reserved for sale actions, limited-edition drops, or cart additions on promotional items. Uses `{colors.accent-terracotta}` as background, a warm fired-clay tone that provides visual contrast against the predominantly brown palette. Active state darkens to `{colors.accent-terracotta-active}`.

### Cards
**`product-card`** — A clean, minimal card with a subtle shadow and 8px rounded corners. The image sits flush to the top with its own corner radius, while the title and price stack below with generous padding. On hover, the shadow deepens to create a gentle lift effect. No border — the card relies on the shadow and the off-white surface-card background to separate from the canvas.

**`badge-sale`** and **`badge-new`** — Small, uppercase badges that sit in the top-left corner of product images. Sale uses the terracotta accent; new uses the primary brown. Both have tight padding and 4px corners, designed to be unobtrusive but legible at small sizes.

### Navigation
**`nav-bar`** — A fixed-height top bar with a single hairline-soft bottom border. Navigation links are uppercase with 0.3px letter-spacing, and the active state uses the primary brown. The bar is intentionally sparse — no search field, no mega-menu — reflecting the brand's curated, limited-inventory approach.

**`category-pill`** — Filter pills used on collection pages to sort by material (Wood, Leather, Felt) or category (Desk, Tech, Home). Pill-shaped with full rounding, they sit on a soft surface background and switch to the primary brown when active.

### Forms
**`text-input`** — Standard input fields with a hairline border and 4px corners. On focus, the border shifts to the primary brown. Padding is generous at 12px vertical and 16px horizontal, giving the field a substantial feel. The placeholder text uses `{colors.muted}`.

**`search-bar`** — A pill-shaped search field with full rounding, used on the collections page. It has a hairline border that switches to primary on focus. The pill shape is the only fully rounded element in the system, making it a subtle visual cue for interactivity.

### Footer
**`footer`** — A dark footer using the primary brown as background, with light text and links. Link hover states shift to `{colors.accent-gold}`, a warm metallic tone that echoes brass hardware on the brand's physical products. The footer contains columns for support, company info, and newsletter signup.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to `{typography.display-md}`; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains `{typography.display-lg}` |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at `{typography.display-xl}` |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered with wider margins |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Category pills are 36px tall with 16px horizontal padding, exceeding the 44x44 touch target for tap areas
- Search bar is 48px tall with ample internal padding
- Nav links have 48px tap targets (padding extends beyond text)

### Collapsing Strategy
- Navigation collapses to a hamburger menu at < 744px, revealing a full-screen overlay with links and search
- Product grid collapses from 4 columns to 1 column at mobile
- Footer columns collapse from 4 to 2 at tablet, then to a single stack at mobile
- Hero section reduces font size and centers text at mobile, removing any side-by-side layout
- Category pills wrap to multiple rows at mobile rather than scrolling horizontally

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations could be extracted from the live site; Inter is assumed based on common usage in the DTC craft space. The actual brand font may differ.
- Only 2-3 distinctive colors were extractable from the live site (the site was behind a Cloudflare challenge at time of extraction). The palette above is constructed from observed brand patterns (wood tones, off-white canvas, terracotta accent) and should be verified against the actual production CSS.
- Hover states for all components are inferred from common patterns; actual transition durations and easing curves are unknown.
- Error states for form inputs (validation, required fields) are not documented.
- Dark mode is not present on the live site and is not defined.
- Sub-brand or seasonal color palettes (e.g., holiday collections, limited editions) are not captured.
- The exact shadow values for product cards are estimated; the actual box-shadow CSS may differ.
- No data on loading states, skeleton screens, or empty states.
- Typography scale is estimated based on common editorial sans-serif systems; actual font sizes and weights should be confirmed from the brand's CSS.
