---
version: alpha
name: "Blue Underground"
source_url: "https://blue-underground.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A midnight-blue and coral-accented horror archive built on a deep #003388 foundation that reads as a collector’s vault rather than a streaming storefront. The extracted palette is dominated by a distinctive navy (#003388) and a bright cyan (#2ea3f2) that together create a cold, cinematic tension — the kind of light that glows off a CRT monitor in a dark room. Accents of #f5795d (a burnt coral) and #e09900 (a warning amber) puncture the blue field like emergency lights, while the grayscale runs from #222222 ink through #4e4e4e body text to #eeeeee canvas, giving the interface a gritty, pre-2015 web texture that suits the classic-horror audience. Typography defaults to Open Sans and Arial — workhorse sans-serifs with no pretense — and the layout uses hard corners ({rounded.none}) on most structural elements, reserving a soft {rounded.sm} (8px) for buttons and badge tags. The nav bar sits at 80px with a #003388 background and white text, a bold header that never recedes. Product cards use a white surface (#ffffff) with a #e2e2e2 hairline, and the primary CTA button (#2ea3f2 on white) feels like a hyperlink made solid — functional, not friendly. This is a design system built for browsing by flashlight.

colors:
  primary: "#2ea3f2"
  primary-active: "#1b70d1"
  primary-disabled: "#82c0c7"
  ink: "#222222"
  body: "#4e4e4e"
  muted: "#555555"
  muted-soft: "#bbbbbb"
  hairline: "#e2e2e2"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-coral: "#f5795d"
  accent-amber: "#e09900"
  accent-purple: "#974df3"
  accent-teal: "#29c4a9"
  nav-bg: "#003388"
  nav-text: "#ffffff"
  footer-bg: "#1f1f1f"
  footer-text: "#f0f0f0"
  badge-new: "#ea2c59"
  badge-sale: "#a82400"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    height: 80px
    padding: "0 {spacing.xl}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
  nav-link-active:
    backgroundColor: "rgba(255, 255, 255, 0.1)"
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "3/4"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
  badge-format:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.xl}"
  section-header:
    typography: "{typography.display-lg}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    height: 40px
    border: "1px solid {colors.hairline}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — The primary action button, rendered in bright cyan (#2ea3f2) with white uppercase text at 14px/600 weight. Uses an 8px corner radius ({rounded.sm}) and 44px height for comfortable tapping. On hover/active, shifts to a deeper blue (#1b70d1). Disabled state uses a desaturated cyan (#82c0c7) to signal non-interactivity while maintaining brand color. Used for "Add to Cart", "Shop Now", and primary form submissions.

**`button-secondary`** — An outlined variant with a white fill, #222222 text, and a 2px #e2e2e2 border. Active state darkens the border to ink (#222222) and adds a light gray (#f9f9f9) background. Used for "View Details", "Cancel", and secondary actions where visual weight should be lower than the primary button.

**`button-accent-coral`** — A high-emphasis coral (#f5795d) button reserved for urgent or promotional actions like "Limited Stock" or "Flash Sale". Shares the same 44px height and uppercase typography as the primary button but introduces a warm, urgent color that breaks the blue system.

**`button-accent-amber`** — An amber (#e09900) button with dark text (#222222) for contrast. Used for "Pre-Order" or "Notify Me" actions where the brand wants to signal availability without the urgency of coral. The amber sits between the cool blues and warm coral in the color spectrum, providing a mid-tone accent.

### Navigation
**`nav-bar`** — A fixed 80px header bar in deep navy (#003388) with white uppercase navigation links. The bar spans full width with 32px horizontal padding. Links sit inline with 8px vertical and 12px horizontal padding. The active link state uses a subtle white overlay (10% opacity) with 8px corner radius to indicate current page without a heavy underline or border.

**`nav-link`** — Uppercase 14px/600 weight Open Sans in white. Hover state adds a subtle opacity shift (to 80%). The active state uses a semi-transparent white background pill for visual separation.

### Cards
**`product-card`** — A white card with no corner radius, 16px padding, and a 3:4 image aspect ratio that favors vertical poster art — appropriate for a horror DVD/Blu-ray catalog. The title sits below the image in 16px/600 weight, with the price in 15px/400 weight body text below that. Cards stack in a responsive grid with 16px gaps. No shadow or border — the card relies on the white surface against the #eeeeee canvas for separation.

**`product-card-image`** — Zero-radius container with a forced 3:4 aspect ratio to accommodate standard movie poster dimensions. Images fill the container with object-fit: cover. On hover, a subtle scale transform (1.02) is applied via CSS.

### Badges
**`badge-new`** — A small pill in hot pink (#ea2c59) with white uppercase 11px/700 text. Used to flag newly added titles. Sits in the top-right corner of product card images with absolute positioning.

**`badge-sale`** — A deep red (#a82400) badge for sale/discount indicators. Same typography and positioning as the new badge but in a darker, more urgent red.

**`badge-format`** — A neutral gray (#f9f9f9 background, #555555 text) badge for format indicators like "Blu-ray", "DVD", "4K UHD", or "Limited Edition". Sits below the product card title or inline with the price.

### Search & Filters
**`search-bar`** — A white input field with 8px corner radius, 44px height, and a 1px #e2e2e2 border. On focus, the border thickens to 2px and turns cyan (#2ea3f2). Placeholder text is #555555. Includes a magnifying glass icon on the left (not tokenized here but assumed from the live site's icon set).

**`filter-dropdown`** — A 40px tall select dropdown with white background, 8px corner radius, and 1px hairline border. Uses 13px/400 body text. The dropdown arrow is rendered as a CSS pseudo-element in #4e4e4e. Active state matches the search bar focus style.

### Footer
**`footer`** — A full-width dark section (#1f1f1f) with light text (#f0f0f0). Contains link columns for "Shop by Format", "Collections", "Support", and "About". Links are 14px/400 weight with no underline. Hover adds a subtle color shift to #82c0c7. The footer includes a copyright line in #bbbbbb caption text at the bottom.

### Pagination
**`pagination-button`** — A 40px tall button with white background, 8px corner radius, and 1px hairline border. Uses uppercase 12px/600 text. The active page uses the primary cyan fill (#2ea3f2) with white text. Adjacent page buttons use the default white style. Disabled prev/next buttons use #bbbbbb text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav bar collapses to hamburger menu; search bar moves below nav; filter dropdowns stack vertically; footer links stack in single column |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but reduce padding; search bar sits inline with nav; filters display as horizontal row with 2-3 dropdowns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; search bar in nav; filters as horizontal row with all options visible; footer in 4-column layout |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px with auto margins; nav and footer expand to full viewport width with content constrained |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have 44px minimum tap area (12px padding on each side of 14px text)
- Filter dropdowns and search bar at 40-44px height
- Product card images are tappable with no minimum size constraint (content-driven)
- Pagination buttons at 40px height with 12px horizontal padding

### Collapsing Strategy
- Nav links collapse into a hamburger menu below 744px; the menu slides in from the left with a dark scrim overlay
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Filter dropdowns collapse from a horizontal row to a vertical stack below 744px; a "Filters" toggle button reveals/hides the stack
- Footer columns collapse from 4 to 2 at tablet breakpoint, then to 1 at mobile
- Search bar moves from inline in the nav (desktop/tablet) to a full-width bar below the nav (mobile)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are heavily weighted toward blues and grays, with a few accent colors (coral, amber, purple, teal) that may be from social icons, payment widgets, or stock imagery rather than intentional brand tokens. The true brand palette likely centers on #003388 (navy) and #2ea3f2 (cyan), but the exact hierarchy of accent colors is uncertain.
- Font-family declarations were limited to system stacks (Arial, Helvetica, Open Sans, Lucida, Courier New) and icon fonts (FontAwesome, ETmodules). No custom or brand-specific typeface was detected. Open Sans is assumed as the primary based on its presence in the extracted list and common usage in WordPress/Divi themes (the site appears to use Divi based on ETmodules references).
- Hover, focus, and active states for most components are inferred from common patterns rather than extracted from the live site. The nav-link active state (white overlay) is a reasonable guess but not confirmed.
- Error states, form validation styling, and empty-state illustrations were not extractable from the static analysis.
- Dark mode is not supported; the system is strictly light-mode with a white canvas and dark navy nav/footer.
- The extracted color list includes #3b5998 (Facebook blue) and #ea2c59 (likely a social icon or badge color) — these may not be core brand colors.
- No animation or transition timing values were extractable. A default 200ms ease-in-out is assumed for interactive state changes.
- The site may use a grid system (likely from Divi) with specific column widths and gutter sizes that were not extractable from the static analysis.
