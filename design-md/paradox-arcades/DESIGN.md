---
version: alpha
name: "Paradox Arcades"
source_url: "https://www.paradoxarcades.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, saturated navy (#112233) anchors Paradox Arcades as a brand that takes arcade-making seriously — not as nostalgia-laden novelty but as precision engineering for commercial operators. The palette reads like a control panel at midnight: #112233 for primary surfaces, #112255 as a slightly brighter active state, and a warning-red #cc3b3b that appears on critical CTAs and error states. The brand's secondary red (#bd0000) is darker and more aggressive, used sparingly for sale badges or urgent indicators, while #e99292 softens into a pastel-pink accent on hover states or secondary badges. The canvas (#fafafa) is nearly white but carries a faint warmth, and the ink (#111111) is almost-black, creating high contrast without the harshness of pure #000000. Typography runs a dual-axis system: Antonio for display headlines — a compressed, uppercase-friendly sans that evokes retro arcade marquees — and Montserrat for body copy, providing a clean, geometric counterpoint. Dosis and Exo appear as secondary display options, likely for scoreboards or leaderboard modules. Rounded corners are minimal: the brand uses {rounded.xs} (4px) on cards and {rounded.sm} (8px) on buttons, avoiding the pill-shaped friendliness of consumer apps in favor of a more industrial, cabinet-like feel. The spacing system is generous at {spacing.section} (64px) for major sections, but internal padding stays tight at {spacing.md} (12px) to maximize screen real estate for game previews and machine specs. This is a brand that communicates durability, performance, and a slight edge — the digital equivalent of a powder-coated steel cabinet with custom-molded control decks.

colors:
  primary: "#112233"
  primary-active: "#112255"
  primary-disabled: "#aaaaaa"
  ink: "#111111"
  body: "#272727"
  muted: "#aaaaaa"
  muted-soft: "#e1e1e1"
  hairline: "#eeeeee"
  hairline-soft: "#fbfbfb"
  canvas: "#fafafa"
  surface-soft: "#fbfbfb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#cc3b3b"
  accent-red-dark: "#bd0000"
  accent-red-soft: "#e99292"
  dark-surface: "#040404"
  dark-ink: "#1e1e1e"

typography:
  display-xl:
    fontFamily: "'Antonio', 'Oswald', 'Exo', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 2px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Antonio', 'Oswald', 'Exo', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 1.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Antonio', 'Oswald', 'Exo', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Antonio', 'Oswald', 'Exo', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "'Montserrat', 'Dosis', 'Exo', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'Montserrat', 'Dosis', 'Exo', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  body-md:
    fontFamily: "'Montserrat', 'Dosis', 'Exo', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Dosis', 'Exo', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Dosis', 'Exo', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Antonio', 'Oswald', 'Exo', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Dosis', 'Exo', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Dosis', 'Exo', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', 'Dosis', 'Exo', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Dosis', 'Exo', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  score-display:
    fontFamily: "'Dosis', 'Exo', 'Antonio', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 2px

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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.primary}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-red-active:
    backgroundColor: "{colors.accent-red-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.xl}"
  nav-bar-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.xs}"
  nav-bar-link-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.xs}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "16/9"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-red-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-section-overlay:
    backgroundColor: "{colors.dark-surface}"
    opacity: 0.7
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 48px
    border: "1px solid {colors.primary}"
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  scoreboard-module:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.score-display}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.primary-active}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.primary}"
    height: 2px

## Components

### Buttons
**`button-primary`** — The workhorse CTA across the site, rendered in deep navy {colors.primary} with white text and 8px rounded corners. On hover or active state, the background shifts to {colors.primary-active} (#112255), a slightly brighter blue that provides clear feedback without animation. The disabled state uses {colors.primary-disabled} (#aaaaaa), a neutral gray that signals unavailability without competing with active elements. All primary buttons use uppercase Montserrat at 14px with 0.5px letter spacing, maintaining the brand's industrial precision.

**`button-secondary`** — An outlined variant with a white background and 2px solid border in {colors.primary}. Used for secondary actions like "Learn More" or "Add to Quote" where the primary button is already present. Hover state fills the background with {colors.primary} at 10% opacity (not yet extracted, noted in gaps). The border ensures the button remains visible against any background.

**`button-accent-red`** — Reserved for high-urgency actions: "Buy Now", "Limited Stock", or "Clearance". Uses {colors.accent-red} (#cc3b3b) as background with white text. Active state deepens to {colors.accent-red-dark} (#bd0000). This button should appear no more than once per viewport to preserve its urgency signal.

### Cards
**`product-card`** — The primary content container for arcade machine listings. A white card with 4px rounded corners and a 1px {colors.hairline} border, containing a 16:9 image thumbnail, product title in {typography.title-sm}, specs in {typography.body-sm}, and a price callout. Internal padding is {spacing.base} (16px) on all sides. On hover, the card gains a subtle shadow (not yet extracted, noted in gaps) and the border shifts to {colors.primary}.

**`product-card-badge`** — Small uppercase Antonio badges affixed to the top-left corner of product card images. The default badge uses {colors.accent-red} for general callouts like "Featured" or "Popular". A sale variant uses {colors.accent-red-dark} for "Sale" or "Clearance", and a "New" variant uses {colors.primary-active} for recently added products. All badges have 4px rounded corners and tight 2px/8px padding.

### Navigation
**`nav-bar`** — A fixed-position top navigation bar at 64px height, filled with {colors.primary} (#112233). Navigation links use uppercase Montserrat at 14px with 0.5px letter spacing, rendered in white. The active link gets a {colors.primary-active} background with 4px rounded corners. The nav bar includes the brand logo (typically rendered in white Antonio display type) on the left, primary navigation links in the center, and utility links (Quote, Contact) on the right.

**`nav-bar-link`** — Individual navigation items with transparent background and white text. On hover, the background shifts to {colors.primary-active} at 50% opacity (not yet extracted, noted in gaps). Active page links use the full {colors.primary-active} background. Padding of 8px/12px provides comfortable tap targets.

### Forms
**`text-input`** — Standard text input fields with white background, 4px rounded corners, and a 1px {colors.hairline} border. On focus, the border shifts to {colors.primary} (#112233). Internal padding of 10px/14px and 44px height matches the button height for aligned form rows. Placeholder text uses {colors.muted} (#aaaaaa).

**`search-bar`** — A dedicated search input with 8px rounded corners and a 1px {colors.hairline} border. Slightly taller than standard inputs at 48px to accommodate a search icon on the left. On focus, the border shifts to {colors.primary}. Used primarily on product listing pages and the site header.

### Footer
**`footer`** — A full-width footer in {colors.primary} with white text. Internal padding of 48px vertical and 32px horizontal. Footer links use {typography.link} at 14px with 0.8 opacity, shifting to full opacity on hover. The footer is divided into columns for product categories, support links, company information, and social media icons. A {colors.hairline} divider separates the main footer from the copyright bar at the bottom.

### Special Components
**`hero-section`** — Full-viewport-width hero banners on the homepage and category pages. Background is {colors.dark-surface} (#040404) with white text using {typography.display-xl} (48px Antonio uppercase). A semi-transparent overlay at 0.7 opacity ensures text readability against background imagery. Internal padding of 64px vertical and 32px horizontal provides breathing room for headline, subheadline, and primary CTA.

**`scoreboard-module`** — A specialized component for displaying high scores, leaderboards, or tournament results. Uses a dark background ({colors.dark-surface}) with a 1px {colors.primary-active} border and 4px rounded corners. Score values render in {typography.score-display} (32px Dosis bold with 2px letter spacing) for maximum readability at a distance. Internal padding of 24px provides space for multiple score entries.

**`filter-tag`** — Pill-shaped filter chips with 8px rounded corners and a 1px {colors.hairline} border. Used on product listing pages to filter by game type, price range, or features. Active state fills the background with {colors.primary} and white text. Inactive tags use {colors.surface-soft} background with {colors.body} text. Padding of 6px/14px keeps them compact for horizontal scrolling strips.

**`divider`** — A 1px horizontal rule in {colors.hairline} for separating content sections. A stronger variant at 2px uses {colors.primary} for major section breaks or under headlines.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, nav collapses to hamburger menu, product cards stack vertically, hero text reduces to {typography.display-lg} (36px), filter tags scroll horizontally, search bar moves to sticky header |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but condensed, hero uses {typography.display-xl} (48px), sidebar filters appear as dropdown, footer collapses to two columns |
| Desktop | 1128–1440px | Three-column product grid, full nav bar with all links visible, hero at full width with {typography.display-xl} (48px), persistent sidebar filters, footer in four columns |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero content constrained to 1200px, additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch targets
- Filter tags are minimum 36px tall with 14px horizontal padding for comfortable tapping
- Product card CTAs are full-width on mobile to maximize tap area
- Nav bar hamburger icon is 48px × 48px on mobile

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px, with a full-screen overlay menu
- Product filters collapse to a single "Filter" button that opens a bottom sheet on mobile
- Footer columns collapse from four to two on tablet, single column on mobile
- Hero section reduces vertical padding from 64px to 40px on mobile
- Product card badges stack vertically on narrow cards (below 300px width)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for button-secondary (background fill at 10% opacity) and nav-bar-link (background at 50% opacity) are inferred from common patterns but not extracted from the live site
- Error styling for form inputs (border color, error message typography) not available from extraction
- Focus ring styles (color, offset, thickness) not extracted — likely uses {colors.primary} with 2px offset
- Shadow tokens for product card hover states not extracted — likely a subtle box-shadow with {colors.ink} at low opacity
- Dark mode palette not available — the site appears to use a light-only design with dark hero sections
- Sub-brand or category-specific color variations not extracted (e.g., "Classic Arcade" vs "Modern Cabinet" categories may have distinct accent colors)
- Animation and transition timing values (hover transitions, page load animations) not extracted
- Icon set and social media icon colors not extracted — likely uses white on dark backgrounds and {colors.muted} on light
- Loading states and skeleton screen designs not available
- Print stylesheet and reduced-motion preferences not documented
- The extracted color list is heavily weighted toward dark blues, grays, and reds — the brand's TRUE primary (#112233) was identified as the most distinctive dark navy, but secondary accent colors beyond red (if any exist) could not be confirmed
