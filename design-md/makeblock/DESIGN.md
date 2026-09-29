---
version: alpha
name: "Makeblock"
source_url: "https://www.makeblock.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dark, industrial engineering canvas (#121212) and a crisp silver-gray (#dedede) form the primary voltage of Makeblock, a brand that treats its STEM audience as builders rather than browsers. The near-black background, paired with a secondary gray (#171414) for surface depth, signals workshop-grade seriousness — this is not a pastel children's toy brand but a platform for robotics, laser cutters, and programmable hardware. The brand's typographic voice runs on Montserrat for display and Lato for body, both geometric sans-serifs that echo the precision of CNC-machined aluminum and laser-etched circuit boards. Signature design moves include high-contrast product photography against the dark canvas, monospace code snippets (`{typography.code}`) that speak directly to the developer-educator audience, and sharp rectangular buttons (`{rounded.none}`) that avoid the friendly pill shapes of consumer brands — every corner is a right angle, every edge a deliberate cut. The top navigation is a floating dark bar (`{colors.ink}`) with white text, and the hero section often features a full-bleed product image with a semi-transparent overlay (`{colors.scrim}`) and bold white typography. Makeblock's color palette is intentionally restrained — no bright accent color emerges from the extracted data, suggesting the brand relies on the physical products themselves (neon-green LED strips, blue servo cables, red laser dots) to provide chromatic energy. The shopping experience is powered by Shopify, but the checkout is visually subdued, matching the brand's monochrome ethos. This is a design system built for the maker mindset: functional, modular, and unadorned.

colors:
  primary: "#dedede"
  primary-active: "#b0b0b0"
  primary-disabled: "#f0f0f0"
  ink: "#121212"
  body: "#171414"
  muted: "#4a4a4a"
  muted-soft: "#6a6a6a"
  hairline: "#2a2a2a"
  hairline-soft: "#3a3a3a"
  canvas: "#121212"
  surface-soft: "#1a1a1a"
  surface-card: "#171414"
  on-primary: "#121212"
  on-dark: "#dedede"
  scrim: "#000000"
  code-bg: "#1e1e1e"
  code-text: "#dedede"
  success: "#4caf50"
  error: "#f44336"
  warning: "#ff9800"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Lato', 'Source Sans Pro', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Lato', 'Source Sans Pro', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Source Sans Pro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Source Sans Pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Source Sans Pro', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Lato', 'Source Sans Pro', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  code:
    fontFamily: "'Consolas', 'Monaco', 'Menlo', 'Courier New', 'SFMono-Regular', 'Liberation Mono', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  code-sm:
    fontFamily: "'Consolas', 'Monaco', 'Menlo', 'Courier New', 'SFMono-Regular', 'Liberation Mono', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-lg:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "'Lato', 'Source Sans Pro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-tertiary-text:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  icon-button:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  icon-button-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  top-nav-item:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  top-nav-item-active:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  top-nav-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "8px 20px"
    height: 36px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.error}"
  select:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.none}"
    padding: "16px 40px"
    height: 56px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  section-header:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-md}"
    padding: "{spacing.lg} 0"
  section-subheader:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.body-lg}"
    padding: "{spacing.sm} 0"
  code-block:
    backgroundColor: "{colors.code-bg}"
    textColor: "{colors.code-text}"
    typography: "{typography.code}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  code-inline:
    backgroundColor: "{colors.code-bg}"
    textColor: "{colors.code-text}"
    typography: "{typography.code-sm}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
  accordion:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  accordion-header:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  tab:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  tab-active:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
    border-bottom: "2px solid {colors.primary}"
  pagination:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
  pagination-disabled:
    backgroundColor: "transparent"
    textColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
  breadcrumb:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} 0"
  breadcrumb-current:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
  breadcrumb-separator:
    backgroundColor: "transparent"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    padding: "0 {spacing.xs}"
  loading-spinner:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    height: 24px
    width: 24px
  loading-spinner-large:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    height: 48px
    width: 48px
  tooltip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  modal:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.7
  modal-header:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    padding: "0 0 {spacing.base} 0"
  modal-body:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    padding: "0 0 {spacing.lg} 0"
  modal-footer:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    padding: "{spacing.base} 0 0 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action on a dark canvas. Uses a silver-gray fill (`{colors.primary}`) with dark text (`{colors.on-primary}`) and sharp zero-radius corners (`{rounded.none}`) to match the brand's industrial aesthetic. On hover, the fill shifts to a darker silver (`{colors.primary-active}`). The disabled state uses a lighter gray (`{colors.primary-disabled}`) with reduced contrast. Height is 48px with 14px vertical and 32px horizontal padding for a substantial, confident presence.

**`button-secondary`** — An outlined variant for secondary actions. Transparent background with a 2px solid border in the primary silver-gray (`{colors.primary}`). Text matches the border color. On active state, the button fills with `{colors.primary}` and text flips to `{colors.on-primary}`. Padding is 13px vertical and 31px horizontal to account for the 2px border.

**`button-tertiary-text`** — A text-only button for the least prominent actions. No background, no border — just the primary silver-gray text (`{colors.primary}`) in `{typography.button-md}`. Used for "Learn more" links within product cards or "Cancel" actions in modals.

**`button-ghost`** — A transparent button with white text (`{colors.on-dark}`) for use on dark backgrounds like the hero section or overlay panels. On hover, the background becomes `{colors.surface-soft}` for subtle feedback.

**`icon-button`** — A 40x40px square button with no background and white icon color. Used for close, menu, and search icons in the top navigation. Active state adds a `{colors.surface-soft}` background.

### Cards
**`product-card`** — A dark card (`{colors.surface-card}`) with no rounded corners, containing a product image, title, price, and optional badges. The image area uses `{colors.surface-soft}` as a placeholder background. The title is set in `{typography.title-sm}` with white text, while the price uses `{typography.body-md}` in the primary silver-gray (`{colors.primary}`) to draw attention to the cost.

**`product-card-badge`** — A small rectangular badge overlaid on product cards. Uses the primary silver-gray (`{colors.primary}`) with dark text in uppercase `{typography.badge}`. Variants exist for sale (`{colors.error}` red) and new (`{colors.success}` green) indicators, both with white text.

### Navigation
**`top-nav`** — A fixed-height (64px) dark navigation bar (`{colors.ink}`) spanning the full viewport width. Navigation items use `{typography.nav-link}` (uppercase Montserrat 14px) in white, with the active state highlighted in the primary silver-gray (`{colors.primary}`). A primary CTA button (`{colors.primary}`) sits at the right edge for "Shop Now" or "Get Started" actions.

**`breadcrumb`** — A simple horizontal breadcrumb trail using `{typography.caption}`. Current page is white (`{colors.on-dark}`), parent pages are muted (`{colors.muted}`), and separators use a softer muted tone (`{colors.muted-soft}`) with 4px horizontal padding.

### Forms
**`text-input`** — A 48px tall input field with a dark surface background (`{colors.surface-soft}`), white text, and a subtle hairline border (`{colors.hairline}`). On focus, the border switches to the primary silver-gray (`{colors.primary}`). Error state uses a red border (`{colors.error}`). All corners are sharp (`{rounded.none}`).

**`select`** — A dropdown select element matching the text-input styling: dark background, white text, hairline border, 48px height, sharp corners.

**`search-bar`** — A 44px tall search input with the same dark surface background and hairline border. Focus state uses the primary silver-gray border. No rounded corners — the brand avoids pill shapes entirely.

### Hero
**`hero-section`** — A full-width section with a dark background (`{colors.ink}`) and large display typography (`{typography.display-xl}`). A semi-transparent overlay (`{colors.scrim}` at 50% opacity) sits over the background image for text legibility. The primary CTA (`{colors.primary}`) is a large 56px tall button with `{typography.button-lg}`.

### Code
**`code-block`** — A code snippet block with a dark monospace background (`{colors.code-bg}`) and silver-gray text (`{colors.code-text}`). Uses `{typography.code}` (Consolas/Monaco stack) with 8px rounded corners and 16px padding. Used for programming examples, API documentation, and tutorial steps.

**`code-inline`** — An inline code span with the same dark background and monospace font, but smaller (`{typography.code-sm}`) with 2px rounded corners and minimal padding. Used within body text to highlight function names, variables, or commands.

### Footer
**`footer`** — A full-width dark footer (`{colors.ink}`) with muted text (`{colors.muted}`) in `{typography.body-sm}`. Links are muted by default and shift to the primary silver-gray (`{colors.primary}`) on hover. Section headings use `{typography.title-sm}` in white. Padding is generous at 80px vertical and 32px horizontal.

### Modal
**`modal`** — A dark card (`{colors.surface-card}`) with no rounded corners, containing a header, body, and footer section. A dark overlay (`{colors.scrim}` at 70% opacity) covers the background. The header uses `{typography.title-md}` in white, the body uses `{typography.body-md}` in muted gray, and the footer contains action buttons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger menu; hero typography reduces to `{typography.display-md}`; footer stacks vertically; search bar moves to drawer; product card badges become full-width strips |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited items with "More" dropdown; hero uses `{typography.display-lg}`; footer uses two-column layout; search bar remains visible but compact |
| Desktop | 1128–1440px | Three-column product grid; full top-nav visible; hero uses `{typography.display-xl}`; footer uses four-column layout; search bar at full width |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px with centered content; hero may include side panel with product specs; footer uses four-column layout with wider spacing |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px and minimum width of 44px on mobile and tablet
- Icon buttons are 40x40px with 44x44px tap area via padding
- Top-nav items have 8px vertical padding for comfortable tapping
- Product card CTAs are 48px tall for easy finger targeting
- Search bar is 44px tall with 16px horizontal padding

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px), with a slide-out drawer containing all navigation items
- Product grid reduces from 4 columns to 1 column on mobile
- Hero section reduces font size and may stack content vertically on mobile
- Footer collapses from 4 columns to a single vertical stack on mobile
- Search bar becomes a full-screen overlay on mobile
- Product filters collapse to a "Filter" button that opens a modal on mobile
- Code blocks become horizontally scrollable on mobile rather than wrapping

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted accent color — the brand's true primary accent (if any) could not be determined from the extracted hex list. The extracted colors (#dedede, #171414, #121212) suggest a monochrome palette, but the brand may use a bright accent (e.g., cyan, green, or orange) in product imagery or marketing materials that was not captured in the HTML/CSS extraction
- Hover and focus states for many components are inferred from common patterns rather than extracted from the live site
- Error, success, and warning colors are generic guesses (#f44336, #4caf50, #ff9800) — the brand may use different semantic colors
- Typography sizes and weights are estimated based on common STEM/education brand patterns and the extracted font families (Montserrat, Lato) — actual values may differ
- The brand's Shopify checkout styling could not be extracted — the checkout may use a different color scheme than the main site
- Dark mode is not applicable as the brand already uses a dark canvas by default
- No data on animation durations, easing curves, or transition effects
- No data on iconography style or icon set used
- No data on photography style or image treatment (e.g., filters, overlays)
- No data on the brand's sub-brand or product-line color variations (e.g., mBot, Laserbox, Neuron)
- The extracted font list includes "siyuan" (likely Source Han Sans / Noto Sans CJK) — this may be used for Chinese-language content, but its specific usage context is unknown
- No data on the brand's print or packaging design system
- The meta theme-color tag was absent, suggesting the brand may not use a browser theme color or it is set via JavaScript
