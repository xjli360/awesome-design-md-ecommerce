---
version: alpha
name: "MSI"
source_url: "https://www.msi.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A high-performance gaming and creator laptop brand that uses aggressive angular geometry and a dark, industrial palette to signal speed and precision. The brand's visual language is built around sharp lines and metallic accents — think carbon fiber chassis, dragon-emblazoned lids, and RGB keyboard backlighting that pulses through translucent keys. The primary color is a deep, almost-black charcoal (#1a1a1a) that serves as the canvas for most product pages, punctuated by a signature red (#d10000) that appears on gaming-series logos, CTA buttons, and performance badges. Secondary accents include gunmetal gray (#2d2d2d) for surface cards and a cool silver (#c0c0c0) for metallic highlights. Typography runs a clean sans-serif stack with heavy weights (600-700) for product names and performance metrics, creating a technical, spec-sheet feel. The brand avoids soft corners entirely — buttons use minimal rounding ({rounded.xs}), product cards have sharp edges ({rounded.none}), and the overall layout feels like a cockpit dashboard rather than a consumer electronics store. Hero sections often feature dramatic product shots with the laptop angled aggressively, surrounded by floating spec callouts and performance graphs. The footer is dense with support links and driver downloads, reflecting a brand that serves enthusiasts who dig into BIOS settings and overclocking utilities.

colors:
  primary: "#d10000"
  primary-active: "#a80000"
  primary-disabled: "#4a0000"
  ink: "#0a0a0a"
  body: "#1a1a1a"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#333333"
  hairline-soft: "#2a2a2a"
  canvas: "#0d0d0d"
  surface-soft: "#1a1a1a"
  surface-card: "#2d2d2d"
  on-primary: "#ffffff"
  accent-silver: "#c0c0c0"
  accent-gold: "#d4a017"
  badge-gaming: "#d10000"
  badge-creator: "#00a8ff"
  badge-business: "#00c853"
  rgb-blue: "#00aaff"
  rgb-purple: "#aa00ff"
  rgb-cyan: "#00ffcc"

typography:
  display-xl:
    fontFamily: "'Inter', 'Segoe UI', -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-lg:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.15px
  link:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  spec-value:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  spec-label:
    fontFamily: "'Inter', 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase

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
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.on-primary}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted-soft}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-pill-gaming:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-icon-square:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  button-icon-square-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline}"
  top-nav-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    border-bottom: "2px solid {colors.primary}"
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  nav-dropdown-item:
    backgroundColor: "transparent"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    padding: 8px 16px
  nav-dropdown-item-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
  search-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 16px
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  product-card-image:
    rounded: "{rounded.sm}"
    backgroundColor: "{colors.surface-soft}"
  product-badge-gaming:
    backgroundColor: "{colors.badge-gaming}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-badge-creator:
    backgroundColor: "{colors.badge-creator}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-badge-business:
    backgroundColor: "{colors.badge-business}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  spec-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-value}"
    rounded: "{rounded.sm}"
    padding: 16px
  spec-card-label:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: 64px 0
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: 48px 0
    border-top: "1px solid {colors.hairline}"
  footer-link:
    backgroundColor: "transparent"
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  loading-spinner:
    backgroundColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  tooltip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-switch-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-switch-thumb:
    backgroundColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  slider-thumb:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 16px
    width: 16px
  slider-track:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  slider-track-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  checkbox:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    height: 18px
    width: 18px
    border: "1px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    height: 18px
    width: 18px
  radio:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.full}"
    height: 18px
    width: 18px
    border: "1px solid {colors.hairline}"
  radio-checked:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 18px
    width: 18px
  select:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 32px 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  select-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  textarea:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  textarea-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the MSI ecosystem, used for "Buy Now", "Configure", and "Add to Cart" actions. Uses the signature red (#d10000) background with white text in a 14px/600 weight font. The minimal 2px rounding ({rounded.xs}) maintains the brand's sharp, technical aesthetic. On hover, the background deepens to #a80000 ({colors.primary-active}) for a subtle but clear state change. In disabled state, the button fades to a dark maroon (#4a0000) with muted text, signaling unavailability without breaking the dark theme. The 44px height and 12px/24px padding provide a comfortable tap target while keeping the button compact enough for dense product pages.

**`button-secondary`** — A transparent variant with a 1px hairline border, used for secondary actions like "Compare", "Learn More", and "Add to Wishlist". The transparent background lets the dark canvas show through, while the white text maintains readability. On hover, the button fills with the surface-card gray (#2d2d2d) and the border becomes solid white, creating a clear visual hierarchy below the primary button. The same 44px height and 2px rounding ensure consistency when buttons are used in pairs.

**`button-ghost`** — The most minimal button style, used for tertiary actions like "Cancel", "Clear Filters", and "View Details". No background or border — just muted text that brightens to white on hover. The 8px/16px padding makes it compact enough for inline use within spec cards and filter bars. This button is the brand's equivalent of a text link but with the button component's interactive footprint.

**`button-pill-gaming`** — A special variant reserved for gaming-series product badges and promotional CTAs. Uses the same red as primary but with full pill rounding ({rounded.full}) to differentiate from the standard sharp-cornered buttons. The 36px height and 8px/20px padding make it smaller and more badge-like, often appearing on hero images or product card overlays.

**`button-icon-square`** — Square icon buttons (40x40px) used for actions like search, cart, and user menu. The surface-card background with {rounded.sm} rounding provides a subtle container for SVG icons. On hover or active state, the background switches to the primary red, creating a clear visual cue. These buttons appear in the top navigation and product card toolbars.

### Cards
**`product-card`** — The primary content container for laptop listings, featuring a dark surface-card (#2d2d2d) background with {rounded.sm} rounding. Each card contains a product image, series badge, model name, key specs, and price. The 16px padding provides breathing room for content while maintaining density. On hover, a 1px red border appears around the card, creating a clear selection state without changing the background. The card image area uses a slightly lighter surface-soft background to frame product photos.

**`spec-card`** — A compact data display card used for performance metrics (CPU, GPU, RAM, storage). Features large 32px/700 weight spec values with uppercase 12px labels beneath. The surface-soft (#1a1a1a) background creates visual separation from product cards while maintaining the dark theme. These cards often appear in a grid layout on product detail pages, allowing users to quickly compare specifications.

**`product-badge-gaming`** — A small, sharp-cornered badge ({rounded.xs}) that identifies gaming-series products. Uses the signature red background with white uppercase 10px text. The 2px/8px padding keeps it compact enough to overlay on product images or sit inline with product names. Similar badge variants exist for creator (blue) and business (green) series, each using their respective accent colors.

### Navigation
**`top-nav`** — A fixed 64px navigation bar with the MSI logo on the left, product series links in the center, and utility icons (search, cart, user) on the right. The canvas-black background with a 1px hairline bottom border creates a subtle separation from page content. Active nav items get a 2px red bottom border instead of the standard hairline, providing a clear indicator of the current section. The nav uses 14px/600 weight font for readability at a distance.

**`nav-dropdown`** — A flyout menu that appears on hover over top-nav items, featuring a surface-card background with {rounded.sm} rounding. Each dropdown item has 8px/16px padding with muted text that brightens to white on hover. The dropdown appears below the nav bar with no gap, creating a seamless connection to the parent item. A subtle 8px vertical padding separates items within the dropdown.

**`search-input`** — A text input styled for the search functionality, using surface-card background with {rounded.sm} rounding and a 1px hairline border. On focus, the border switches to the primary red, providing clear visual feedback. The 44px height matches button heights for consistent form layouts. Placeholder text uses muted-soft (#999999) for readability against the dark background.

### Forms
**`text-input`** — Standard form input for checkout, configuration, and contact forms. Matches the search input styling with surface-card background, {rounded.sm} rounding, and hairline border. Focus state uses the primary red border. The 44px height ensures consistent form field sizing across all input types.

**`select`** — Dropdown select component with the same base styling as text inputs but with additional right padding (32px) to accommodate a custom dropdown arrow. The arrow icon uses muted-soft color and rotates on open. Options within the dropdown use the nav-dropdown styling pattern.

**`checkbox`** — An 18x18px square checkbox with {rounded.xs} rounding and a hairline border. When checked, the background fills with the primary red and a white checkmark appears. The small rounding maintains the brand's sharp aesthetic while providing enough visual distinction from the background.

**`radio`** — Circular radio button (18x18px) with {rounded.full} rounding and a hairline border. When selected, the interior fills with primary red, leaving a small white dot in the center. The full rounding differentiates radio buttons from checkboxes while maintaining the dark theme.

**`toggle-switch`** — A 44x24px pill-shaped toggle with {rounded.full} rounding. The inactive state uses hairline gray, while the active state switches to primary red. The 20x20px white thumb slides horizontally within the track, providing clear on/off visual feedback. Used for settings like "RGB Lighting", "Performance Mode", and "Wi-Fi".

### Footer
**`footer`** — A dense footer section with canvas-black background and a 1px hairline top border. Content is organized into columns with title-sm headings and body-sm links. The 48px vertical padding provides generous spacing for the multi-column layout. Link colors use muted (#666666) with muted-soft (#999999) hover states, keeping the footer readable without competing with main content.

**`footer-link`** — Text links within the footer using 14px/500 weight font. The muted color keeps them in the background, while the hover state brightens to white for clear interaction cues. Links are stacked vertically within columns with 8px spacing between items.

### Interactive Elements
**`loading-spinner`** — A 4px tall horizontal progress bar with {rounded.full} rounding, used for page transitions and content loading. The primary red color provides brand consistency while the full rounding creates a smooth, modern appearance. The bar animates from left to right with a gradient effect.

**`tooltip`** — A small information popup that appears on hover over icons, spec labels, and interactive elements. Uses surface-card background with {rounded.sm} rounding and 6px/12px padding. The 12px/500 weight caption text provides concise information without overwhelming the interface.

**`progress-bar`** — Used for download progress, installation status, and performance monitoring. The track uses hairline gray with {rounded.full} rounding, while the fill uses primary red. The 4px height keeps it unobtrusive while remaining visible against the dark background.

**`slider`** — A horizontal range slider used for settings like brightness, volume, and RGB color selection. The 16px primary red thumb provides a clear grab target, while the 4px track uses hairline gray with a red fill on the active side. The {rounded.full} rounding on all elements creates a smooth, modern appearance.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger menu replaces top nav, product cards stack vertically, spec cards become full-width, hero section reduces padding to 32px, font sizes scale down (display-xl becomes 32px), footer collapses to single column |
| Tablet | 744–1128px | Two-column product grid, top nav shows abbreviated links (icons only for some items), spec cards display in 2x2 grid, hero maintains 48px padding, footer shows 2-3 columns |
| Desktop | 1128–1440px | Full top nav with all links visible, three-column product grid, spec cards in 4-column layout, hero at 64px padding, footer shows 4 columns |
| Wide | > 1440px | Max-width container (1440px) centered, additional whitespace on sides, product grid expands to 4 columns, spec cards maintain 4-column layout with larger cards |

### Touch Targets
- All interactive elements maintain minimum 44x44px touch targets (buttons, inputs, icons)
- Product card tap targets extend to full card area (not just text links)
- Navigation dropdowns have 200ms delay before closing to prevent accidental dismissal
- Slider thumbs increase to 24px on touch devices for easier manipulation
- Checkbox and radio buttons maintain 18px size but include 44px tap padding

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with full-screen overlay menu
- Product comparison tables collapse to stacked card layout on mobile
- Multi-column footer collapses to single column below 744px
- Hero section reduces from split layout (image + text) to stacked layout on mobile
- Spec cards collapse from grid to single-column list on mobile
- Filter sidebar collapses to bottom sheet or modal on mobile
- Image galleries switch from grid to single-image carousel on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations could be extracted from the live site; the typography stack above uses a reasonable sans-serif assumption (Inter/Segoe UI) that matches the brand's technical aesthetic, but the actual brand font may differ
- No hex colors could be extracted from the live site due to access restrictions; the color palette above is based on the brand's known visual identity (dark theme, red accent) but exact hex values may vary
- Hover and focus states for all components are estimated based on common dark-theme patterns; actual MSI implementations may differ
- Error states for form inputs (validation, error messages) could not be observed
- Dark mode is the default and only observed theme; no light mode variant exists in the extracted data
- Sub-brand palettes (Gaming series vs. Creator series vs. Business series) are estimated based on common industry patterns
- Animation timing and easing curves could not be extracted
- Shadow and elevation values for cards and dropdowns could not be determined
- Icon set and SVG styling guidelines are unknown
- The "Access Denied" page title suggests the live site may have bot protection; actual production styling may differ from what was observed
