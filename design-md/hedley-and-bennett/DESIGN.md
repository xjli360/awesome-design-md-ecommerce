---
version: alpha
name: "Hedley & Bennett"
source_url: "https://www.hedleyandbennett.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Hedley & Bennett is a kitchen apparel and tool brand built on a foundation of rugged utility and quiet confidence. The palette is anchored by a deep, almost charcoal ink (#2d2b29) and a warm off-white canvas (#f8f7f7), with accents of a bold, unapologetic red (#e72106) that appears on primary actions and signature details. The supporting cast of muted grays and blues — #959b9e, #676986, #2c383f, #1f3045 — evokes the texture of well-worn denim and seasoned steel, while the sparing use of a vibrant blue (#2563eb) for links and interactive elements adds a modern, digital-native counterpoint. The typography is decisively set in DM Sans, a geometric sans-serif that balances approachability with a no-nonsense clarity, and is occasionally punctuated by the assertive, all-caps presence of FUTURA for headings or badges. Rounded corners are minimal — a soft 4px (`{rounded.xs}`) on buttons and cards — reinforcing a sense of precision and craftsmanship rather than playfulness. The overall mood is that of a workshop: honest materials, considered details, and a color story that feels both timeless and distinctly Californian. The design system prioritizes legibility and hierarchy, using generous spacing (`{spacing.lg}` to `{spacing.section}`) to let product photography and the brand's signature red do the heavy lifting.

colors:
  primary: "#e72106"
  primary-active: "#c41c04"
  primary-disabled: "#f8a08a"
  ink: "#2d2b29"
  body: "#374151"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#d1d5db"
  hairline-soft: "#e5e7eb"
  canvas: "#f8f7f7"
  surface-soft: "#f4f1ee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#2563eb"
  accent-blue: "#676986"
  accent-dark-blue: "#1f3045"
  badge-red: "#e72106"
  badge-new: "#2563eb"
  star-rating: "#2d2b29"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'DM Sans', 'FUTURA', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'DM Sans', 'FUTURA', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'DM Sans', 'FUTURA', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', 'FUTURA', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', 'FUTURA', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'FUTURA', 'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'DM Sans', 'FUTURA', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'DM Sans', 'FUTURA', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', 'FUTURA', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-red:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
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
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    border: "2px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    border: "2px solid {colors.ink}"
  text-input-error:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in a bold red (#e72106) with white text. It uses a tight 4px corner radius (`{rounded.xs}`) and 44px height, projecting a sense of decisive action. On hover, it shifts to a deeper red (#c41c04). The disabled state fades to a soft salmon (#f8a08a), signaling non-interactivity without visual noise.

**`button-secondary`** — A clean, low-emphasis alternative with a white background and a subtle hairline border (#d1d5db). The text remains in the dark ink (#2d2b29). On hover, the background warms to the soft surface tone (#f4f1ee) and the border darkens to the ink color, providing clear feedback without competing with the primary button.

**`button-tertiary-text`** — A text-only button with no background or border, used for less critical actions like "Cancel" or "Learn More." It inherits the ink color and button typography, relying on spacing and placement for hierarchy.

**`button-pill-red`** — A compact, fully rounded pill variant reserved for badges, filters, or promotional tags. It uses the same brand red but with smaller padding and font size, making it suitable for inline or crowded layouts.

### Cards
**`product-card`** — The core product display unit, built on a white surface with a soft 4px radius. The image area sits on a warm off-white background (#f4f1ee) to subtly frame product photography. The title uses `title-sm` (18px, weight 500) and the price uses `body-md` (16px, weight 400) in the body gray (#374151). No shadow or border is used, keeping the focus on the product itself.

### Navigation
**`top-nav`** — A 72px tall, white navigation bar that spans the full viewport. Links are set in uppercase DM Sans with 0.5px letter-spacing, reinforcing the brand's workshop-meets-modern aesthetic. The active state is indicated by a 2px red underline (#e72106), while inactive links are muted (#6b7280). The cart icon and search icon are simple line-art SVGs in the ink color.

**`nav-link-active`** — The active navigation state, distinguished by a 2px solid red underline. This is the only decorative element on the nav bar, ensuring the user's current section is immediately clear.

**`nav-link-inactive`** — The default navigation state, rendered in the muted gray (#6b7280). On hover, it transitions to the ink color (#2d2b29), providing a subtle but clear interactive cue.

### Forms
**`text-input`** — A standard text input with a white background, 48px height, and a 1px hairline border (#d1d5db). On focus, the border thickens to 2px and turns ink (#2d2b29). Error states use a 2px red border (#e72106). The placeholder text is set in `body-md` at the muted-soft color (#9ca3af).

**`search-bar`** — A compact 44px search input with a white background and a 1px hairline border. The focus state mirrors the text-input pattern. It is designed to sit within the top nav or a dedicated search overlay.

### Footer
**`footer`** — A dark, full-width footer with an ink (#2d2b29) background and white text. Links are set in the muted-soft gray (#9ca3af) and shift to white on hover. The layout uses generous vertical padding (`{spacing.xxl}`) and a multi-column grid for newsletter signup, navigation, and social links.

### Badges
**`badge`** — A small, uppercase badge used for sale indicators, "Best Seller" tags, or limited-time offers. It uses the brand red (#e72106) with white text, a 4px radius, and tight padding (2px 8px). The font is FUTURA at 11px with 0.5px letter-spacing, giving it a crisp, industrial feel.

**`badge-new`** — A blue variant (#2563eb) of the standard badge, reserved for "New Arrival" tags. It follows the same sizing and typography rules, providing a visual distinction from promotional badges.

### Hero
**`hero-section`** — A full-width hero area with a soft off-white background (#f4f1ee) and large display typography. It uses `display-xl` (48px, weight 700) for the headline and `body-md` for supporting text. The section padding is 64px on top and bottom, with 24px on the sides. A primary CTA button is typically centered or left-aligned within the hero.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; top-nav collapses to hamburger menu; hero text scales to `display-lg` (36px); product cards stack vertically; search bar moves to a full-width overlay; footer collapses to stacked rows. |
| Tablet | 744–1128px | Two-column grid for product cards; top-nav remains visible but with reduced link spacing; hero text uses `display-md` (28px); search bar is a compact icon in the nav. |
| Desktop | 1128–1440px | Three-column grid for product cards; full top-nav with all links visible; hero text uses `display-xl` (48px); search bar is a full input field in the nav. |
| Wide | > 1440px | Max-width container (1440px) centered; four-column grid for product cards; hero section has increased padding; all elements scale proportionally. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px and a minimum width of 44px to meet WCAG touch target guidelines.
- Icon buttons are 40x40px with a 4px radius, providing a clear hit area.
- Product card images are tappable and link to the product detail page.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu that opens a full-screen overlay. The search bar becomes a magnifying glass icon that expands into a full-width input.
- The product grid collapses from 4 columns on wide screens to 1 column on mobile.
- The footer's multi-column layout collapses to a single column on mobile, with accordion-style expandable sections for navigation links.
- The hero section's layout shifts from a side-by-side text-and-image arrangement to a stacked vertical layout on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons were inferred from common patterns but not directly extracted from the live site.
- Error styling for form inputs (text-input-error) is based on the primary red but the exact shade and border width are assumptions.
- Dark mode is not supported; all tokens assume a light theme.
- Sub-brand or seasonal palettes (e.g., holiday collections) were not captured.
- The exact font weight for FUTURA in headings is assumed to be 700, but the live site may use a different weight.
- Spacing values for specific components (e.g., product card margins) are estimates based on common e-commerce patterns.
- The `star-rating` color is assumed to match the ink color, but the live site may use a different shade.
- The `scrim` color for overlays is assumed to be black at full opacity, but the actual implementation may use a semi-transparent value.
