---
version: alpha
name: "Genelec"
source_url: "https://www.genelec.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A studio-monitor manufacturer whose design language is built on a near-black canvas (#111111) that makes every product photograph and spec diagram feel like it's floating in a calibrated listening room. The brand's primary accent, a cool cyan (#5bbad5), appears only in small, precise doses — active-state toggles, selected filter chips, and the illuminated power ring on the 8000-series monitors — never as a background or a headline color. This restraint is the core design move: the interface trusts high-contrast typography in Helvetica Neue LT Pro (set at 400 weight for body, 700 for display) and generous negative space over decorative elements. The secondary palette includes a warm orange (#da532c) used exclusively for warning indicators and peak-level alerts, and a deep navy (#0e141b) that serves as the surface for product detail cards and spec tables. Rounded corners are minimal — the search bar and primary CTAs use {rounded.sm} (8px), while product cards and modals use {rounded.md} (12px) — a deliberate rejection of the pill-shaped friendliness common in consumer tech. The overall mood is that of a precision instrument interface: monochromatic, information-dense, with color reserved entirely for signaling function rather than brand personality.

colors:
  primary: "#5bbad5"
  primary-active: "#4aa8c4"
  primary-disabled: "#2a5a6a"
  ink: "#111111"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e8e8e8"
  hairline-soft: "#f3f3f3"
  canvas: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#0e141b"
  surface-dark: "#111111"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  warning: "#da532c"
  warning-active: "#c44a26"
  accent-cyan: "#5bbad5"
  accent-navy: "#0e141b"
  accent-warm: "#da532c"

typography:
  display-xl:
    fontFamily: "'helvetica-neue-lt-pro', Helvetica Neue, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'helvetica-neue-lt-pro', Helvetica Neue, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'helvetica-neue-lt-pro', Helvetica Neue, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'helvetica-neue-lt-pro', Helvetica Neue, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'helvetica-neue-lt-pro', Helvetica Neue, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-lg:
    fontFamily: "'helvetica-neue-lt-pro', Helvetica Neue, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'helvetica-neue-lt-pro', Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'helvetica-neue-lt-pro', Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'helvetica-neue-lt-pro', Helvetica Neue, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'helvetica-neue-lt-pro', Helvetica Neue, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'helvetica-neue-lt-pro', Helvetica Neue, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'helvetica-neue-lt-pro', Helvetica Neue, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'helvetica-neue-lt-pro', Helvetica Neue, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'helvetica-neue-lt-pro', Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'helvetica-neue-lt-pro', Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-warning-active:
    backgroundColor: "{colors.warning-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(91, 186, 213, 0.15)"
  text-input-error:
    border: "1px solid {colors.warning}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
  product-card-image:
    rounded: "{rounded.md}"
  product-card-spec:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 600px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 36px"
    height: 48px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-spec:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "64px 0"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-dark:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-active:
    backgroundColor: "{colors.primary}"
  toggle-thumb:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  slider-track:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  slider-thumb:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  modal:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "32px"
    maxWidth: 600px
  modal-overlay:
    backgroundColor: "rgba(17, 17, 17, 0.6)"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "16px 0"
  accordion-header:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  accordion-content:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "12px 0"
  table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    fontWeight: 700
    padding: "12px 16px"
    borderBottom: "1px solid {colors.hairline}"
  table-cell:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "12px 16px"
    borderBottom: "1px solid {colors.hairline}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Explore", "Shop Now", and "Learn More" actions on the hero section and product pages. On hover, it shifts to a slightly darker cyan (#4aa8c4). The disabled state uses a muted teal (#2a5a6a) to indicate inactivity without introducing a separate gray. **`button-secondary`** — An outlined button with a 2px solid black border on a white background, used for secondary actions like "Compare" and "Downloads". On hover, the background fills with black and text inverts to white, creating a strong visual hierarchy. **`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "View Details". On hover, a soft gray background (#f3f3f3) appears behind the text. **`button-warning`** — An orange button (#da532c) reserved exclusively for destructive actions like "Reset to Defaults" or "Clear All Filters" in the product configuration interface.

### Navigation
**`nav-bar`** — A fixed 72px white header with a thin bottom border (#e8e8e8). Navigation links are uppercase, 14px, weight 600, with 0.5px letter spacing. The active page link is underlined with a 2px cyan bar (#5bbad5) and the text turns cyan. Inactive links are muted gray (#666666). The logo sits on the left, and a search icon and language selector sit on the right. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

### Cards
**`product-card`** — A dark navy (#0e141b) card with white text, used for product listings and detail pages. The card has 12px rounded corners and 24px padding. Product images are also rounded at 12px. Spec badges inside the card use an even darker background (#111111) with soft gray text (#999999) and 4px rounded corners. The card's dark surface makes the product photography — typically shot on a black background — feel continuous with the card itself, as if the monitor is floating in its own listening room.

### Forms & Inputs
**`text-input`** — A standard 44px input field with 8px rounded corners, a 1px hairline border (#e8e8e8), and placeholder text in soft gray (#999999). On focus, the border turns cyan (#5bbad5) with a subtle 3px cyan box-shadow at 15% opacity. Error states swap the border to orange (#da532c). **`search-bar`** — Similar to the text input but with slightly tighter padding (10px vertical) and a 1px hairline border. On focus, the border turns cyan. The search bar is always present in the nav on desktop and collapses into a search icon on mobile.

### Badges
**`badge-new`** — A cyan badge with white uppercase text at 11px, weight 700, with 0.5px letter spacing. Used to mark newly released products. **`badge-warning`** — An orange badge with white text, used for "Peak" or "Warning" indicators on audio meters and configuration panels. **`badge-spec`** — A dark badge (#111111) with soft gray text (#999999), used for technical specifications like "150W", "40Hz–20kHz", or "Class D" inside product cards.

### Footer
**`footer`** — A full-width dark section (#111111) with soft gray text (#999999) at 14px. Links are the same soft gray and turn cyan (#5bbad5) on hover. The footer contains columns for product categories, support, company info, and social links. A thin divider line (#e8e8e8 at 10% opacity) separates the main content from the copyright bar.

### Toggles & Sliders
**`toggle`** — A pill-shaped toggle (24px tall, 44px wide) with a gray background (#e8e8e8) and a white circular thumb. When active, the background fills with cyan (#5bbad5). Used for features like "Auto Power Off" and "Room Compensation" in the product configuration interface. **`slider-track`** — A thin 4px gray line (#e8e8e8) with a 20px cyan circular thumb. Used for volume and EQ adjustments in the monitor calibration tools.

### Tables
**`table-header`** — A light gray (#f3f3f3) row with bold 12px text and 12px/16px padding. Used for spec comparison tables on product pages. **`table-cell`** — White rows with 14px body text and a thin bottom border (#e8e8e8). Alternating row colors are not used; instead, the table relies on the hairline border for visual separation.

### Modals
**`modal`** — A white card with 12px rounded corners, 32px padding, and a max width of 600px. The overlay is a semi-transparent black (#111111 at 60% opacity). Used for product quick-views, video embeds, and configuration dialogs. The modal header uses `{typography.title-lg}` and the body uses `{typography.body-md}`.

### Accordions
**`accordion`** — A white section with a thin bottom border (#e8e8e8) and 16px vertical padding. The header uses `{typography.title-md}` and the content uses `{typography.body-md}` with 12px top padding. Used for FAQ sections and product feature breakdowns.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero text reduces to 28px; filter chips wrap; tables become scrollable horizontally; footer columns stack |
| Tablet | 744–1128px | Nav links remain visible but reduce font size to 13px; product cards display in 2-column grid; hero text at 36px; filter chips in a scrollable horizontal strip |
| Desktop | 1128–1440px | Full nav with uppercase links; product cards in 3-column grid; hero text at 48px; filter chips in a multi-row grid; tables display normally |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero section expands to full viewport height with parallax effect |

### Touch Targets
- All interactive elements maintain minimum 44x44px touch targets on mobile
- Filter chips are 32px tall with 16px horizontal padding, exceeding the 44px height minimum when combined with surrounding spacing
- Search bar and primary CTAs are 48px tall on mobile for easier tapping
- Accordion headers have 44px minimum tap height (16px padding + 18px text + 10px additional padding)

### Collapsing Strategy
- Top nav: full links on desktop, hamburger menu on mobile with full-screen overlay
- Product filters: visible sidebar on desktop, collapsible accordion on mobile
- Product comparison table: full table on desktop, horizontally scrollable on mobile
- Footer: 4-column layout on desktop, 2-column on tablet, single-column on mobile
- Hero section: full-width image with text overlay on desktop, stacked layout (image above text) on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is dominated by neutral tones (black, white, grays) with two accent colors (cyan #5bbad5 and orange #da532c). The cyan is the most distinctive brand color and has been designated as the primary. However, the extracted list may include social media icon colors or stock image dominant tones rather than intentional brand colors. The true brand palette may include additional accent colors not captured in the extraction.
- Font-family declarations were limited to "helvetica-neue-lt-pro" and Font Awesome. The actual font stack may include additional weights (300, 500, 700) or a secondary font for code/technical content that was not extracted.
- Hover, focus, and active states for all components are inferred from common patterns rather than extracted from the live site. The actual interaction states may differ.
- Error styling for forms (error messages, error iconography, validation patterns) was not extracted and is based on standard conventions.
- Dark mode styling is not present in the extracted data. The brand's dark canvas (#111111) and navy surface (#0e141b) suggest a potential dark mode, but no toggle or alternate palette was found.
- The extracted theme-color meta tag is #ffffff, indicating a white browser chrome on mobile. This may change in future iterations.
- No animation or transition timing values were extracted. The brand likely uses subtle transitions (0.2s–0.3s ease) for hover states and page transitions, but exact values are unknown.
- Iconography style (line vs. filled, stroke weight, icon set) was not extracted beyond Font Awesome usage.
- Product photography treatment (consistent lighting, background, angle) is a significant part of the brand's visual identity but cannot be captured in token form.
