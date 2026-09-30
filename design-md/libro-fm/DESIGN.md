---
version: alpha
name: "Libro.fm"
source_url: "https://libro.fm"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A teal-and-coral bookstore ecosystem where #62b9b6 (a minty seafoam) and #e96c7a (a warm watermelon pink) trade primary duty depending on context — the teal anchors the main navigation and brand lockup, while the coral drives membership CTAs and promotional banners, creating a two-color system that feels like a co-op rather than a corporation. The palette draws heavily from independent bookstore interiors: #f2f2f7 as the soft off-white canvas, #404040 as body text, and #222222 for headlines, with #7f7edb (a lavender accent) appearing on category tags and author badges. Type runs museo-sans-rounded and greycliff-cf — both rounded humanist sans-serifs — giving every headline and button a friendly, approachable curve that matches the {rounded.sm} 8px corners on cards and the {rounded.full} pill-shaped search bar. The design trusts generous whitespace ({spacing.section} 64px between major sections) and a three-column grid for audiobook discovery, with cover art doing the heavy lifting. Membership badges use #62cb91 (a fresh green) for "active member" status, while sale tags lean on #ffe000 (a marigold yellow) pulled from the extracted palette. The footer stacks six columns of bookstore links in {typography.body-sm} at 14px, with a persistent "Support Local" callout in the primary teal. Every interactive element — from the search bar to the "Listen Now" button — uses a 48px touch target, and the sticky bottom-player bar (a signature audiobook pattern) sits at 72px with a translucent white scrim.

colors:
  primary: "#62b9b6"
  primary-active: "#4aa6a3"
  primary-disabled: "#c6e6e5"
  accent-coral: "#e96c7a"
  accent-coral-active: "#e24052"
  accent-lavender: "#7f7edb"
  accent-lavender-active: "#5756d0"
  accent-green: "#62cb91"
  accent-green-active: "#40c079"
  accent-yellow: "#ffe000"
  ink: "#222222"
  body: "#404040"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#c6c6c8"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f2f2f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-coral: "#ffffff"
  on-lavender: "#ffffff"
  on-dark: "#ffffff"
  player-scrim: "rgba(255, 255, 255, 0.95)"

typography:
  display-xl:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
    textTransform: uppercase
  button-lg:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  player-time:
    fontFamily: "'museo-sans-rounded', 'greycliff-cf', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
    fontVariantNumeric: tabular-nums

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
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-coral}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-coral-active:
    backgroundColor: "{colors.accent-coral-active}"
    textColor: "{colors.on-coral}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  button-pill-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-coral}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "2px solid {colors.accent-coral}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    color: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-cover:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1:1"
  product-card-info:
    padding: "{spacing.md} {spacing.base}"
  badge:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.on-lavender}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-coral}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-headline:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    maxWidth: 600px
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    maxWidth: 500px
  category-strip:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.md} 0"
    gap: "{spacing.sm}"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.body}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.primary}"
  footer-heading:
    color: "{colors.ink}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.md}"
  player-bar:
    backgroundColor: "{colors.player-scrim}"
    borderTop: "1px solid {colors.hairline-soft}"
    height: 72px
    padding: "{spacing.md} {spacing.lg}"
  player-progress:
    backgroundColor: "{colors.hairline-soft}"
    height: 4px
    rounded: "{rounded.full}"
  player-progress-fill:
    backgroundColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  player-control:
    color: "{colors.ink}"
    height: 40px
    rounded: "{rounded.full}"
  player-control-hover:
    color: "{colors.primary}"
  membership-cta:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-coral}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    height: 56px
  membership-cta-active:
    backgroundColor: "{colors.accent-coral-active}"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.xl}"

## Components

### Buttons
**`button-primary`** — The default call-to-action, filled with the brand teal {colors.primary} (#62b9b6). Used for "Add to Cart", "Sign Up", and "Browse" actions. On hover, shifts to {colors.primary-active} (#4aa6a3). Disabled state uses {colors.primary-disabled} (#c6e6e5) with muted text. Height is 48px with 14px vertical padding and 24px horizontal padding, corners at {rounded.sm} (8px).

**`button-coral`** — The accent primary for membership and promotional CTAs, filled with {colors.accent-coral} (#e96c7a). Used for "Start Free Trial", "Join Now", and limited-time offers. Active state shifts to {colors.accent-coral-active} (#e24052). Same dimensions as button-primary for consistency.

**`button-secondary`** — An outlined variant with a white fill and teal border (2px solid {colors.primary}). Used for secondary actions like "Learn More" or "View Details". On hover, background shifts to {colors.surface-soft} and border to {colors.primary-active}.

**`button-ghost`** — A text-only button with no background or border. Used for "Cancel", "Skip", or inline navigation. On hover, text color shifts to {colors.primary}. Maintains 48px height for consistent touch targets.

**`button-pill`** — A compact pill-shaped button using {rounded.full} for tag-like actions such as "Filter" or "Genre" toggles. Available in teal and coral variants. Height is 40px with 10px vertical padding.

### Cards
**`product-card`** — The primary audiobook discovery unit. A white card with a 1:1 cover image at the top (corners rounded at {rounded.sm}) and metadata below (title, author, narrator, length, price). Uses a subtle box shadow (0 1px 3px rgba(0,0,0,0.08)) that deepens on hover (0 4px 12px rgba(0,0,0,0.12)). The info section uses {spacing.md} horizontal padding and {spacing.base} bottom padding.

### Navigation
**`top-nav`** — A 72px fixed header with white background and a subtle bottom border ({colors.hairline-soft}). Contains the brand logo (teal lockup), nav links in {typography.nav-link} (15px, weight 500), and a search icon. Active nav links get a 2px teal bottom border and teal text color. On mobile, collapses to a hamburger menu.

**`category-strip`** — A horizontal scrollable strip of pill-shaped category tags. Each tag is 36px tall with {rounded.full} corners, {colors.surface-soft} background, and {colors.body} text. Active tags switch to {colors.primary} background with white text.

### Forms
**`text-input`** — Standard form input with 48px height, 12px vertical padding, 16px horizontal padding, and a 1px {colors.hairline} border. On focus, border thickens to 2px {colors.primary} with no outline. Error state uses 2px {colors.accent-coral} border. Placeholder text in {colors.muted-soft}.

**`search-bar`** — A pill-shaped search field ({rounded.full}) with {colors.surface-soft} background and 1px {colors.hairline-soft} border. On focus, background shifts to white and border to 2px {colors.primary}. Height is 48px for consistent touch target.

### Badges
**`badge`** — Small uppercase labels (11px, weight 600) used for metadata flags. Available in four colors: lavender ({colors.accent-lavender}) for "New Release", green ({colors.accent-green}) for "Member Exclusive", yellow ({colors.accent-yellow}) for "Sale", and coral ({colors.accent-coral}) for "Limited Time". Padding is 2px vertical, 8px horizontal with {rounded.xs} corners.

### Footer
**`footer`** — A six-column grid layout on desktop, collapsing to two columns on tablet and single column on mobile. Uses {colors.surface-soft} background with {colors.body} text. Column headings use {typography.title-sm} in {colors.ink}. Links use {typography.link} (14px, underlined) with hover state shifting to {colors.primary}. Includes a "Support Local" callout in the primary teal.

### Player Bar
**`player-bar`** — A sticky bottom bar at 72px height with translucent white background (rgba(255, 255, 255, 0.95)) and a top border. Contains album art thumbnail, track info (title, narrator), playback controls (play/pause, forward/backward), progress bar, and time display. Progress bar is 4px tall with {rounded.full} corners — gray track ({colors.hairline-soft}) with teal fill ({colors.primary}). Control buttons are 40px circles with hover state shifting to teal.

### Hero Section
**`hero-section`** — A full-width banner at minimum 400px height with {colors.surface-soft} background. Features a headline in {typography.display-xl} (36px, weight 700) constrained to 600px max-width, and a subtitle in {typography.body-md} constrained to 500px. Includes a primary CTA button and optional secondary link. Padding is {spacing.section} (64px) vertical.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; top-nav collapses to hamburger; product cards stack vertically; footer collapses to single column; hero padding reduces to 32px; search bar moves to expandable icon; category strip becomes horizontal scroll |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links (logo, search, account); footer shows two columns; hero padding at 48px; category strip shows 5-6 visible tags |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links visible; six-column footer; hero at full padding (64px); category strip shows 8+ visible tags |
| Wide | > 1440px | Max-width container at 1440px centered; three-column grid with wider cards; hero content centered with larger max-widths; category strip expands to show all tags |

### Touch Targets
- All interactive elements (buttons, inputs, links) maintain minimum 44x44px touch target per WCAG 2.1
- Primary CTAs use 48px height for comfortable tapping
- Player controls use 40px circular targets with 48px tap area via padding
- Category tags use 36px height with 8px internal padding
- Search bar uses 48px height on all breakpoints

### Collapsing Strategy
- Top nav collapses to hamburger menu at < 744px, revealing full link set in a slide-out drawer
- Product grid collapses from 3 columns → 2 columns → 1 column as viewport shrinks
- Footer collapses from 6 columns → 2 columns → 1 column
- Hero section reduces vertical padding from 64px to 32px on mobile
- Category strip becomes horizontally scrollable with overflow-x: auto on mobile, hiding overflow tags
- Search bar collapses to an icon-only trigger on mobile, expanding to full-width overlay on tap
- Player bar reduces metadata display on mobile (hides narrator, shows only title)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted color list is noisy with 30+ hex values including many blues (#00a0ff through #00e3ff range) that appear to be social media icon colors (Twitter/X, Facebook) and payment-widget colors (Shopify Pay, Klarna, Afterpay). The true brand palette was inferred from the most distinctive and frequently occurring non-framework colors: #62b9b6 (teal), #e96c7a (coral), #7f7edb (lavender), #62cb91 (green), #ffe000 (yellow). These should be verified against the brand's official style guide.
- Font stack was extracted from CSS declarations but exact weights and sizes for each token are inferred from common patterns. The brand uses museo-sans-rounded and greycliff-cf as primary fonts — exact font-weight values (400, 500, 600, 700) and letter-spacing values are best guesses based on typical usage.
- Hover, active, focus, and disabled states for all components are inferred from common design patterns, not extracted from live site CSS.
- Error states (form validation, empty states, 404 pages) were not extracted and use generic patterns.
- Dark mode is not present on the live site and is not defined.
- Player bar design (progress bar, controls, layout) is inferred from common audiobook player patterns and may differ from actual implementation.
- Membership pricing tiers, subscription flow, and checkout components were not extracted.
- Animation durations, easing curves, and transition properties were not extracted.
- The "Support Local" bookstore partner network UI (store selection, location-based filtering) was not extracted.
