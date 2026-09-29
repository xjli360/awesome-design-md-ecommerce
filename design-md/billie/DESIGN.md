---
version: alpha
name: "Billie"
source_url: "https://mybillie.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Billie is a direct-to-consumer body-care brand that reimagines the everyday rituals of shaving and grooming with a distinctly playful, unpretentious, and body-positive voice. The brand lives on a clean white canvas (`#ffffff`) and uses a restrained palette where soft, muted tones like `#f5f0eb` and `#e8e0d8` create a warm, approachable foundation rather than a sterile one. There is no aggressive brand color commanding every CTA — instead, Billie trusts generous whitespace, friendly illustration, and a system font stack anchored on `nowie-web` and `-apple-system` to feel human and accessible. Typography is intentionally low-contrast and understated: body copy sits at modest weights (400–500) with comfortable line heights around 1.5, while display treatments rarely exceed 600 weight, avoiding the heavy-handedness of traditional CPG. The brand’s signature design move is the soft pill shape — buttons, input fields, and badges all use `{rounded.full}` (9999px) to erase any hard edge, reinforcing a tactile, gentle quality. Cards and containers use `{rounded.lg}` (20px) to maintain softness without losing structure. The overall mood is one of calm confidence: pastel-adjacent neutrals, no harsh shadows, and a layout that breathes. Billie’s visual system says “we take care, not ourselves too seriously.”

colors:
  primary: "#f5a623"
  primary-active: "#d4891e"
  primary-disabled: "#fce4b8"
  ink: "#2d2d2d"
  body: "#4a4a4a"
  muted: "#8c8c8c"
  muted-soft: "#b0b0b0"
  hairline: "#dcdcdc"
  hairline-soft: "#eaeaea"
  canvas: "#ffffff"
  surface-soft: "#f9f6f2"
  surface-card: "#ffffff"
  surface-warm: "#f5f0eb"
  on-primary: "#ffffff"
  accent-pink: "#f7c5cc"
  accent-green: "#c8e6c9"
  accent-blue: "#bbdefb"
  badge-new: "#f5a623"
  badge-sale: "#e57373"
  star-rating: "#f5a623"

typography:
  display-xl:
    fontFamily: "nowie-web, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "nowie-web, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "nowie-web, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "nowie-web, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "nowie-web, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "nowie-web, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "nowie-web, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "nowie-web, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 0
  button-pill:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 14px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.badge-sale}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 14px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
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
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
  product-card-image:
    rounded: "{rounded.lg}"
    aspectRatio: "1 / 1"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.body}"
    typography: "{typography.link}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a full-width or inline pill with a warm amber background (`{colors.primary}`) and white text. On hover, it shifts to `{colors.primary-active}` for a subtle darkening effect. The disabled state uses `{colors.primary-disabled}` to signal inactivity without visual noise. All variants share `{rounded.full}` for a soft, tactile feel.

**`button-secondary`** — A ghost-style pill with a white fill and a thin `{colors.hairline}` border. On active/hover, the border deepens to `{colors.ink}` and the background shifts to `{colors.surface-soft}`. Used for “Learn More” or “Add to Cart” alternatives where primary is too dominant.

**`button-tertiary-text`** — A text-only button with no background or border. Uses `{typography.button-md}` and `{colors.ink}`. Reserved for secondary actions like “Cancel” or “Skip” in flows where visual weight should be minimal.

**`button-pill`** — A small, compact pill used for filter tags or category toggles. Background is `{colors.surface-warm}`, text is `{colors.ink}`, and the shape is `{rounded.full}`. Active state swaps to `{colors.primary}` with white text.

### Cards
**`product-card`** — The core product display unit. A white card with `{rounded.lg}` corners, no shadow, relying on generous whitespace and a 1:1 aspect ratio image. The badge overlay uses `{rounded.full}` and sits at the top-left corner. Text below the image uses `{typography.title-sm}` for the product name and `{typography.body-sm}` for the price.

**`hero-section`** — A full-width banner with a warm `{colors.surface-warm}` background, large display typography, and centered or left-aligned content. Padding is `{spacing.section}` vertically to create breathing room. Used on landing pages and collection headers.

### Navigation
**`nav-bar`** — A fixed or sticky top bar at 64px height with a white background and a subtle `{colors.hairline-soft}` bottom border. Navigation links use `{typography.nav-link}` in uppercase with `{colors.ink}`. The active link is underlined with a 2px `{colors.primary}` border. The logo sits left, links center or right, and a cart icon is always present.

### Forms
**`text-input`** — A pill-shaped input field with a white background, `{rounded.full}`, and a `{colors.hairline}` border. On focus, the border switches to `{colors.ink}`. Error state uses `{colors.badge-sale}` for the border. Disabled inputs fade to `{colors.surface-soft}` with `{colors.muted}` text.

**`select-input`** — A pill-shaped dropdown styled identically to `text-input` but with a custom chevron icon. Uses `{typography.body-md}` for consistency.

**`checkbox`** and **`radio`** — Small, square (checkbox) or circular (radio) controls with a `{colors.hairline}` border and white fill. Checked state fills with `{colors.primary}` (checkbox) or shows a thick `{colors.primary}` ring (radio). Both use `{rounded.xs}` for checkbox and `{rounded.full}` for radio.

### Footer
**`footer`** — A full-width footer with a `{colors.surface-warm}` background. Links use `{typography.link}` in `{colors.body}`. Dividers between sections use `{colors.hairline-soft}`. Padding is `{spacing.xxl}` top and bottom. The footer is organized in a multi-column grid on desktop and collapses to a single column on mobile.

### Badges
**`badge`** — A small, rounded pill used for labels like “New,” “Bestseller,” or “Limited Edition.” Default uses `{colors.surface-warm}` background. The `badge-primary` variant uses `{colors.primary}` for emphasis. Both use `{typography.badge}` in uppercase.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero section reduces padding to `{spacing.xl}`; footer collapses to single column; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav-bar remains expanded but links may condense; hero section uses `{spacing.section}` padding; footer uses two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links visible; hero section uses `{spacing.section}` padding; footer uses four columns |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid may expand to four columns; all spacing scales proportionally |

### Touch Targets
- All interactive elements (buttons, inputs, links) have a minimum height of 48px on mobile to meet accessibility standards.
- Icon buttons are 40x40px with `{rounded.full}` to ensure easy tapping.
- Nav links have a minimum touch area of 44x44px even when text is smaller.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer.
- The product filter sidebar collapses into a bottom sheet or modal on mobile.
- The multi-column footer collapses to a single column with accordion-style sections.
- Hero sections reduce vertical padding from `{spacing.section}` to `{spacing.xl}` on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only active and disabled states are documented where visible.
- Error styling for forms (e.g., validation messages, error icons) is inferred from common patterns but not confirmed from the live site.
- Dark mode is not supported and no dark-mode tokens were found.
- Sub-brand or seasonal palette variations (e.g., holiday, limited edition) are not captured.
- Animation and transition durations (e.g., button hover, card lift) are not specified.
- The exact `nowie-web` font weight mappings (e.g., 500 vs 600) are based on typical usage but may vary.
- Shadow and elevation tokens (e.g., for modals, dropdowns) were not found in the extracted data.
- The site’s error page (“Something went wrong”) may have unique styling not representative of the main design system.
