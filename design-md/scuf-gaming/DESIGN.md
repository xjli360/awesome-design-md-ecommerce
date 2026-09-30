---
version: alpha
name: "SCUF Gaming"
source_url: "https://scufgaming.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A midnight-blue (#19212c) chassis holds the brand's entire identity — this is the color of pro-gamer focus, the dark of a dimmed tournament room where only controller LEDs and monitor glow cut through. Against that deep navy, a single high-voltage orange (#ff8f1c) fires every primary CTA, thumbstick ring, and configurator highlight, while a secondary electric blue (#2563eb) handles secondary actions and link states. The typography stack splits cleanly: Sofia Sans Semi Condensed for display and button text (tight, competitive, space-efficient), Tomorrow for technical specs and data readouts, and Verveine-Regular as an unexpected cursive accent for limited-edition drops and signature series. Corners are mostly sharp — {rounded.none} on cards and panels — but thumbsticks and D-pads get {rounded.full} treatment, mirroring the actual hardware. The configurator is the beating heart: a three-column layout with live 3D controller preview, swatch grid of shell colors (#ece81a yellow, #ff0a02 red, #3b8649 green), and component selector tabs that feel more like a CAD tool than an ecommerce page. Badges read "PRO" and "LIMITED" in all-caps Sofia Sans at 10px, pinned to the top-right of product cards with a {rounded.sm} clip. The brand doesn't soften anything — there is no pastel, no gradient wash, no generous whitespace. It's dense, technical, and built for people who care about trigger tension and paddle placement more than lifestyle photography.

colors:
  primary: "#ff8f1c"
  primary-active: "#e67e00"
  primary-disabled: "#ffd699"
  ink: "#19212c"
  body: "#333132"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#d8d8d8"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f1f3f5"
  surface-card: "#ffffff"
  surface-dark: "#19212c"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-blue: "#2563eb"
  accent-yellow: "#ece81a"
  accent-red: "#ff0a02"
  accent-green: "#3b8649"
  badge-pro: "#ff8f1c"
  badge-limited: "#2563eb"
  badge-sale: "#ff0a02"
  swatch-shell-dark: "#19212c"
  swatch-shell-black: "#121212"
  swatch-shell-gray: "#444444"
  swatch-shell-silver: "#909090"
  swatch-shell-white: "#fafafa"
  swatch-shell-yellow: "#ece81a"
  swatch-shell-red: "#ff0a02"
  swatch-shell-green: "#3b8649"
  configurator-bg: "#f5f5f5"
  configurator-active: "#19212c"
  configurator-text: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Sofia Sans Semi Condensed', 'Tomorrow', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Sofia Sans Semi Condensed', 'Tomorrow', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Sofia Sans Semi Condensed', 'Tomorrow', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Sofia Sans Semi Condensed', 'Tomorrow', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Sofia Sans Semi Condensed', 'Tomorrow', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Sofia Sans Semi Condensed', 'Tomorrow', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Tomorrow', 'Sofia Sans Semi Condensed', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Tomorrow', 'Sofia Sans Semi Condensed', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Tomorrow', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Tomorrow', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Sofia Sans Semi Condensed', 'Tomorrow', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Tomorrow', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Sofia Sans Semi Condensed', 'Tomorrow', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Sofia Sans Semi Condensed', 'Tomorrow', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Sofia Sans Semi Condensed', 'Tomorrow', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Tomorrow', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Sofia Sans Semi Condensed', 'Tomorrow', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Tomorrow', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Tomorrow', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
    color: "{colors.accent-red}"
  accent-font:
    fontFamily: "'Verveine-Regular', cursive"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0

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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "#2a3a4e"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-config-add:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 52px
  button-config-save:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 52px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    aspectRatio: 1/1
  product-card-badge:
    backgroundColor: "{colors.badge-pro}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.body}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    textColor: "{colors.accent-red}"
  configurator-panel:
    backgroundColor: "{colors.configurator-bg}"
    rounded: "{rounded.none}"
  configurator-sidebar:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  configurator-tab-active:
    backgroundColor: "{colors.configurator-active}"
    textColor: "{colors.configurator-text}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 12px 20px
  configurator-tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 12px 20px
  swatch-button:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  swatch-button-selected:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.link}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  limited-edition-badge:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  sale-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 0 0 16px 0

## Components

### Buttons

**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Configure Now", and "Buy Now" flows. Rendered in the brand's signature orange (#ff8f1c) with white text and a subtle 4px corner radius. On hover, it shifts to a deeper orange (#e67e00). The disabled state drops to a pale peach (#ffd699) with white text, signaling the action is unavailable without visual noise.

**`button-secondary`** — Used for "View Details", "Learn More", and secondary configurator actions. Uses the deep navy (#19212c) background with white text, maintaining the brand's dark, technical mood. Hover state lifts to a slightly lighter navy (#2a3a4e). This button shares the same 44px height and {rounded.sm} as the primary for visual consistency.

**`button-outline`** — A bordered variant for tertiary actions like "Cancel" or "Compare". Transparent background with a 1px solid {colors.hairline} border and navy text. The outline keeps the same 44px height and {rounded.sm} radius, ensuring it stacks neatly alongside primary and secondary buttons in toolbars.

**`button-config-add`** — The primary action button inside the controller configurator. Full-width, no corner radius, 52px tall, using the brand orange with white text in 18px Sofia Sans Semi Condensed. This button sits at the bottom of the configurator sidebar and is intentionally larger and more commanding than standard CTAs.

**`button-config-save`** — The secondary configurator button for saving drafts or sharing configurations. Uses the dark navy background, same full-width and 52px height as the add button, creating a clear visual hierarchy between "add to cart" and "save for later".

### Navigation

**`nav-bar`** — A fixed-position top navigation bar at 72px height on desktop, collapsing to 56px on scroll. White background with uppercase Sofia Sans Semi Condensed nav links at 15px, 0.5px letter-spacing. The SCUF logo sits left-aligned, with primary links (Controllers, Configurator, Pro, Accessories) in the center, and utility icons (search, cart, account) right-aligned.

**`nav-link-active`** — Active navigation links render in the brand orange (#ff8f1c) with no underline or background change. The color shift alone signals the current section, keeping the nav clean and competitive.

**`nav-link-inactive`** — Inactive links render in a muted gray (#6b7280), maintaining readability without competing with the active state. Hover state transitions to navy (#19212c) for subtle feedback.

### Cards

**`product-card`** — A sharp-cornered card with a white background, 1:1 aspect ratio product image, and a bottom information strip containing the product name, badge (if applicable), and price. No border — the card relies on the image and content density for structure. Hover state adds a subtle shadow and slightly lifts the card.

**`product-card-badge`** — A small uppercase badge pinned to the top-right of the product image. Badge background color varies by type: orange for "PRO", blue for "LIMITED", red for "SALE". The badge uses 10px Sofia Sans Semi Condensed at 700 weight with 0.5px letter-spacing, fitting snugly with 2px vertical and 8px horizontal padding.

### Configurator

**`configurator-panel`** — The main configurator workspace, a light gray (#f5f5f5) background area that holds the 3D controller preview and component selection grid. No rounded corners — the configurator is a tool, not a marketing page.

**`configurator-sidebar`** — A white sidebar panel running the full height of the configurator, containing component categories (Shell, Thumbsticks, D-Pad, Triggers, Paddles) and their options. Each category is an accordion with a trigger and expandable content area.

**`configurator-tab-active`** — Active component category tabs within the sidebar. Dark navy (#19212c) background with white text, no rounded corners, 12px vertical padding. The active tab feels pressed into the sidebar, like a physical button.

**`configurator-tab-inactive`** — Inactive tabs use a soft gray (#f1f3f5) background with muted gray (#6b7280) text. On hover, the text shifts to navy for affordance.

**`swatch-button`** — Circular color swatches (32px diameter) used for shell and component color selection. Each swatch displays the actual color as its background. The selected state adds a 2px white ring with a 1px navy outer ring for clear visual distinction.

### Forms

**`text-input`** — Standard text input fields with a white background, navy text, and a 1px solid {colors.hairline} border. Focus state swaps the border to the brand orange (#ff8f1c) with a subtle box-shadow. Used for search, account forms, and checkout fields.

**`select-input`** — Dropdown select fields matching the text input styling. Used primarily in the configurator for component size and tension options.

### Footer

**`footer`** — A full-width dark navy (#19212c) footer section with white text. Links render in a muted gray (#9ca3af) and shift to white on hover. The footer contains four columns: Shop, Support, About, and Legal, each with a title in uppercase Sofia Sans Semi Condensed and body links in Tomorrow.

### Hero

**`hero-banner`** — The primary hero section on the homepage and collection pages. Dark navy background with white text, featuring a large product image or lifestyle shot. The hero CTA uses the brand orange button with white text, positioned to draw immediate attention.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; configurator becomes full-screen modal; product cards stack vertically; hero text reduces to {typography.display-md} |
| Tablet | 744–1128px | Two-column product grid; configurator sidebar collapses to bottom sheet; nav links reduce to icon-only for utility items |
| Desktop | 1128–1440px | Three-column product grid; full configurator sidebar + 3D preview; full nav link text visible |
| Wide | > 1440px | Four-column product grid; configurator expands to show additional component detail panels; max-width container at 1440px |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Swatch buttons at 32px diameter meet minimum touch target size with adequate spacing (8px gap between swatches)
- Configurator tabs at 44px minimum touch height
- Accordion triggers at 48px touch height for easy finger targeting

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Configurator sidebar collapses to bottom sheet on tablet, full-screen modal on mobile
- Footer columns stack to single column below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Hero banner reduces font size and may hide secondary text below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted from the live site; the above represents best-guess based on common patterns and the brand's visual language
- Error state styling for form inputs (validation colors, error message typography) was not observable
- Dark mode is not implemented on the live site; all observations are from the light theme
- The extracted hex color list is heavily weighted toward grays and neutrals (#19212c through #737373), with only a few distinctive accents (#ff8f1c orange, #2563eb blue, #ece81a yellow, #ff0a02 red, #3b8649 green). The brand's true primary is #ff8f1c (the most distinctive non-neutral), but the extracted palette may include checkout-widget colors and social-icon colors that aren't part of the core design system
- Font sizes and weights for typography tokens are estimated based on common usage patterns and the brand's competitive positioning; actual values may vary
- The Verveine-Regular cursive font appears to be used sparingly for limited-edition product names and signature series — exact usage context is inferred
- Component spacing values (padding, margins) are estimated based on visual inspection and may not match production pixel-perfect values
- Animation and transition timing (hover transitions, page transitions, configurator animations) were not extractable
- The configurator's 3D preview component behavior and loading states were not observable in static extraction
