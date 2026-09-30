---
version: alpha
name: "Dark Delicacies"
source_url: "https://www.darkdel.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A specialty bookstore that feels like a candlelit library curated by a horror collector with exacting taste, anchored on a near-black ink (#111111) and a warm, restrained palette of weathered grays (#eeeeee, #aaaaaa, #444444, #282b2d) that evoke aged paper, iron shelves, and the patina of well-loved paperbacks. The brand’s single voltage of color is a dried-blood red (#e74c3c) used sparingly — on the primary CTA, on sale badges, and as the hover-state underline on navigation links — a deliberate jolt against the otherwise monochrome stage. Typography splits between a gothic calligraphic display face (Kingthings Calligraphica, used for the logo and section headers) and a clean, utilitarian sans-serif body stack (Proxima Nova, Open Sans, Helvetica Neue) that keeps product descriptions and category labels legible without romanticism. Corners are almost universally sharp (`{rounded.none}`) — product cards, buttons, and input fields all sit at 0px radius, reinforcing the no-frills, archival sensibility. The only exception is the search bar, which takes a gentle `{rounded.sm}` (8px) to signal interactivity. Spacing is generous but not airy: `{spacing.lg}` (24px) between cards, `{spacing.section}` (64px) between major content blocks, and `{spacing.base}` (16px) inside buttons and inputs. The overall effect is that of a serious, slightly gothic archive — the design never winks, never over-decorates, and trusts the inventory of horror, mystery, and the macabre to provide all the atmosphere.

colors:
  primary: "#e74c3c"
  primary-active: "#c0392b"
  primary-disabled: "#f58c8c"
  ink: "#111111"
  body: "#222222"
  muted: "#444444"
  muted-soft: "#525252"
  hairline: "#ced0d2"
  hairline-soft: "#e3e5e7"
  canvas: "#f4f4f4"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#f5871f"
  accent-warm-soft: "#ffbf80"
  badge-sale: "#e03939"
  badge-sale-text: "#ffffff"
  badge-new: "#6688ff"
  badge-new-text: "#ffffff"
  star-rating: "#ff9b00"
  star-rating-empty: "#d5d5d5"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Kingthings Calligraphica', 'Georgia', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
  display-md:
    fontFamily: "'Kingthings Calligraphica', 'Georgia', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.3px
  title-lg:
    fontFamily: "'Oswald', 'Impact', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "'Proxima Nova', 'Open Sans', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Proxima Nova', 'Open Sans', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Proxima Nova', 'Open Sans', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Proxima Nova', 'Open Sans', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Proxima Nova', 'Open Sans', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Proxima Nova', 'Open Sans', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Proxima Nova', 'Open Sans', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Proxima Nova', 'Open Sans', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Proxima Nova', 'Open Sans', 'Helvetica Neue', sans-serif"
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-price:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.title-md}"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.badge-sale-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.badge-new-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  star-rating:
    color: "{colors.star-rating}"
    emptyColor: "{colors.star-rating-empty}"
    size: 16px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  pagination:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 4px 10px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's dried-blood red (#e74c3c) with white text and zero border radius. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, shifts to `{colors.primary-active}` (#c0392b), a deeper crimson. Disabled state uses `{colors.primary-disabled}` (#f58c8c), a washed-out pink that signals unavailability without competing with the active state. Padding is generous at 12px 24px, height 44px, with 0.5px letter-spacing on the button text for a slightly more deliberate read.

**`button-secondary`** — An outlined or ghost-style button on the light canvas (#f4f4f4) with ink (#111111) text. Used for "Continue Shopping", "Cancel", and secondary actions. Active state fills with `{colors.surface-soft}` (#eeeeee). Shares the same 44px height and 0px radius as the primary button, maintaining a consistent vertical rhythm across all interactive elements.

**`button-tertiary-text`** — A text-only button in the primary red, used for "View Details", "Learn More", and inline actions. No background, no border, just the red text on hover. Typography uses `{typography.button-sm}` (13px, 600 weight) to keep it visually subordinate to the primary and secondary buttons.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, solid ink (#111111) background with white text. Links are set in `{typography.nav-link}` (14px, 600 weight, uppercase, 0.5px letter-spacing) for a crisp, authoritative feel. The active link is underlined with a 2px solid `{colors.primary}` (#e74c3c) border. The logo uses `{typography.display-md}` in Kingthings Calligraphica, providing the only decorative typography in the navigation.

**`nav-link-active`** — The active navigation link state, distinguished by a 2px bottom border in the primary red. The text color also shifts to `{colors.primary}` on hover, creating a clear visual hierarchy between active and inactive states.

### Search
**`search-bar`** — The only element in the system with a rounded corner (`{rounded.sm}`, 8px), this subtle softening signals interactivity and approachability. Background is the light canvas (#f4f4f4), text is body (#222222), and the input is 44px tall with 10px 16px padding. On focus, the border shifts to `{colors.primary}` (#e74c3c), maintaining the brand's restrained use of color as a signal.

### Cards
**`product-card`** — A sharp-cornered card with white background and body text. No shadow, no border radius — the card relies on the contrast between the white surface and the light canvas (#f4f4f4) background for separation. The price is displayed in `{colors.primary}` (#e74c3c) using `{typography.title-md}` (18px, 600 weight) to draw the eye. Badges for "Sale" and "New" are positioned at the top-left corner of the card image.

**`product-card-badge-sale`** — A sharp-cornered badge in deep red (#e03939) with white uppercase text (11px, 700 weight). Padding is tight at 2px 8px, keeping the badge compact and unobtrusive.

**`product-card-badge-new`** — A sharp-cornered badge in blue (#6688ff) with white text, used for newly added inventory. Shares the same typography and padding as the sale badge for visual consistency.

### Forms
**`text-input`** — A standard input field with 0px radius, light canvas background, and 44px height. Padding is 10px 16px. On focus, the border changes to `{colors.primary}` (#e74c3c), providing the only color feedback in the form. Error states (not fully extracted) would likely follow the same pattern with a red border.

### Footer
**`footer`** — A full-width footer on the ink (#111111) background with muted-soft (#525252) text. Links are set in `{typography.link}` (14px, 400 weight) and inherit the muted-soft color. The footer uses `{spacing.section}` (64px) padding top and bottom, with `{spacing.lg}` (24px) between link groups.

### Hero
**`hero-section`** — A full-width hero banner on the ink (#111111) background with white text. The headline uses `{typography.display-xl}` (36px, Kingthings Calligraphica) for a gothic, literary feel. Padding is 64px 24px, creating a dramatic vertical space that lets the typography breathe against the dark background.

### Categories
**`category-strip`** — A horizontal strip of category tabs on the light canvas (#f4f4f4) background. Tabs are set in `{typography.button-sm}` (13px, 600 weight). The active tab uses `{colors.primary}` (#e74c3c) background with white text, while inactive tabs remain transparent with body text. All tabs share the 0px radius and 8px 16px padding.

### Pagination
**`pagination`** — A simple pagination strip with transparent backgrounds and body text. The active page uses `{colors.primary}` (#e74c3c) background with white text, 4px 10px padding, and 0px radius. Inactive pages have no background, relying on the text color for hierarchy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Navigation collapses to hamburger menu; product cards stack in single column; hero padding reduces to 32px 16px; category strip becomes a horizontal scrollable row; search bar moves below nav; footer links stack vertically |
| Tablet | 744–1128px | Navigation remains horizontal but with reduced link spacing; product cards display in 2-column grid; hero padding at 48px 24px; category strip shows 4-5 visible tabs with overflow scroll |
| Desktop | 1128–1440px | Full navigation with all links visible; product cards in 3-column grid; hero at full 64px 24px padding; category strip shows all tabs; search bar in top nav |
| Wide | > 1440px | Max-width container at 1440px with centered content; product cards in 4-column grid; hero remains at 64px padding but content area is centered; category strip centered within max-width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum height of 44px for touch accessibility
- Navigation hamburger icon is 44x44px with 8px padding
- Category tabs are 44px tall with 8px 16px padding
- Pagination buttons are 44x44px minimum
- Search bar is 44px tall with 16px padding

### Collapsing Strategy
- Navigation: On mobile (< 744px), the full nav bar collapses to a hamburger menu. The logo remains visible. The search bar moves below the nav into a dedicated row.
- Category strip: On mobile, the category strip becomes a horizontal scrollable row with a "scroll hint" arrow on the right edge. On tablet, it shows 4-5 tabs with overflow scroll.
- Footer: On mobile, footer link groups collapse from a multi-column layout to a single vertical stack. The newsletter signup (if present) remains at the top of the footer.
- Product grid: Collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: While primary and secondary button hover states were extracted (#c0392b for primary, #eeeeee for secondary), hover states for text inputs, links, and category tabs were not reliably extracted from the live site. These are inferred from common patterns.
- **Error styling**: Form error states (red borders, error text) were not present in the extracted data. The system likely uses the primary red (#e74c3c) for error borders and a lighter red (#fde9e9) for error backgrounds, but this is speculative.
- **Dark mode**: No dark mode variant was detected. The brand's existing dark backgrounds (ink #111111) suggest a natural dark mode extension, but no tokens were extracted.
- **Sub-brand palettes**: The extracted colors include several accent colors (#f5871f orange, #6688ff blue, #ff9b00 gold) that may belong to sub-brands, seasonal promotions, or third-party widgets. Their specific usage contexts are unknown.
- **Font weights**: The extracted font declarations include "ProximaNova-Semibold" and "Oswald" with `!important`, but exact font weights for each typography token were inferred from common web usage (Proxima Nova 400/600, Oswald 600, Kingthings Calligraphica 400).
- **Spacing values**: The spacing scale is based on common e-commerce patterns and the observed density of the site. Exact padding and margin values for every component were not extractable.
- **Shadow and elevation**: No box-shadow values were extracted. The brand appears to rely on flat design with no shadows, but this is an inference from the extracted CSS.
- **Animation and transition**: No transition durations or easing functions were extracted. The brand likely uses simple 150-200ms ease transitions for hover states, but this is speculative.
- **Third-party widget colors**: The extracted list includes #5897fb (likely a social media or widget blue), #ff9b00 and #995d00 (possibly star ratings or sale accents), and #6688ff (possibly a "new" badge or link color). These may not be core brand colors.
