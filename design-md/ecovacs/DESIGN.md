---
version: alpha
name: "Ecovacs"
source_url: "https://www.ecovacs.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Five shades of blue within the first screenful — that is the immediate impression of the Ecovacs storefront, where a saturated cobalt (#3877f5) commands every primary CTA and hero overlay while a constellation of supporting blues (#0075ff, #356cf1, #3070ed, #4098ff) shift across hover states, gradient endpoints, and interactive highlights like a lidar scan sweeping a dark room. The darkest layer is a near-black navy (#00112c) that backs the persistent header and mobile drawer, paired with a warmer slate (#253746) for subheadings and secondary navigation labels. Body copy sits in a cooler charcoal (#3e3a39) on a canvas that alternates between two near-whites — #f5f5f7 for section backgrounds and #f7f8f9 for the outermost page shell — giving product imagery a faintly cool stage rather than a flat white void. Typography runs on Noto Sans and SF Pro, both geometric sans-serifs chosen for legibility at small sizes: spec-comparison cells, sensor descriptions, and multi-line feature lists all render cleanly at 13–14px weight 400, while display headings use weight 700 at 36–48px with tight negative tracking to feel engineered rather than editorial. A vivid orange (#fa6400) breaks the blue field at exactly two pressure points — promotional banners and limited-time bundle CTAs — while a softer amber (#ffab47) marks star ratings and feature-highlight icons. Error and urgency states split between a deep red (#c12424) for price strike-throughs and stock warnings and a hot magenta-red (#e40046) for flash-sale countdowns. Product cards use `{rounded.sm}` corners with a 1px `{colors.hairline}` border, lifting on hover with a soft shadow; comparison tables — a signature Ecovacs pattern for its DEEBOT and WINBOT lineups — stripe alternating rows in `{colors.surface-soft}` and `{colors.surface-card}` with `{typography.body-sm}` spec text and green (#089a43) checkmarks for supported features. Buttons are moderately rounded (`{rounded.sm}` at 8px) rather than fully pilled, keeping the interface closer to a precision-tool dashboard than a consumer lifestyle brand. Spacing is generous — `{spacing.lg}` gutters between card columns, `{spacing.section}` vertical rhythm on hero blocks — allowing the robots themselves, rendered in photorealistic 3D product shots, to occupy visual center stage.

colors:
  primary: "#3877f5"
  primary-hover: "#1c4aa2"
  primary-active: "#1e5397"
  primary-disabled: "#99c2ff"
  ink: "#00112c"
  ink-secondary: "#253746"
  body: "#3e3a39"
  muted: "#687282"
  muted-soft: "#99a3ad"
  hairline: "#d4d9db"
  hairline-soft: "#e6e9eb"
  border-strong: "#b9c4c9"
  canvas: "#f7f8f9"
  surface-soft: "#f5f5f7"
  surface-card: "#ffffff"
  surface-strong: "#e0e0e0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-orange: "#fa6400"
  accent-amber: "#ffab47"
  accent-blue-light: "#4098ff"
  accent-blue-mid: "#356cf1"
  accent-steel: "#849cbc"
  accent-steel-soft: "#728fb2"
  error: "#c12424"
  alert-red: "#e40046"
  success: "#089a43"
  link-blue: "#007aff"
  star-rating: "#ffab47"
  scrim: "#111111"

typography:
  display-xl:
    fontFamily: "'SF Pro', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.8px
  display-lg:
    fontFamily: "'SF Pro', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'SF Pro', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'SF Pro', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'SF Pro', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'SF Pro', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'SF Pro', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Noto Sans', 'SF Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Noto Sans', 'SF Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Noto Sans', 'SF Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Noto Sans', 'SF Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Noto Sans', 'SF Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Noto Sans', 'SF Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.3px
  badge:
    fontFamily: "'SF Pro', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'SF Pro', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'SF Pro', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'SF Pro', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  price-display:
    fontFamily: "'SF Pro', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  price-strike:
    fontFamily: "'Noto Sans', 'SF Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
    textDecoration: line-through
  link:
    fontFamily: "'Noto Sans', 'SF Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'SF Pro', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px

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
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    borderColor: "{colors.primary}"
    borderWidth: 1px
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-hover:
    backgroundColor: "#d95500"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    borderColor: "{colors.on-dark}"
    borderWidth: 1px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
    borderWidth: 1px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  text-input-error:
    borderColor: "{colors.error}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    height: 56px
    boxShadow: "0 2px 8px rgba(0,0,0,0.15)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-mega-menu:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.primary}"
    borderWidth: 1px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
  product-card-hover:
    boxShadow: "0 6px 16px rgba(0,17,44,0.10)"
    borderColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  comparison-row:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  comparison-row-alt:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  comparison-header:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base}"
  feature-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 10px
  feature-badge-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 10px
  promo-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 10px
  sale-badge:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 10px
  price-block:
    currentPrice:
      textColor: "{colors.ink}"
      typography: "{typography.price-display}"
    originalPrice:
      textColor: "{colors.muted}"
      typography: "{typography.price-strike}"
    savingsBadge:
      textColor: "{colors.error}"
      typography: "{typography.caption}"
  spec-table-cell:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    padding: "{spacing.sm} {spacing.md}"
  stock-indicator:
    textColor: "{colors.success}"
    typography: "{typography.caption}"
  stock-indicator-low:
    textColor: "{colors.accent-orange}"
    typography: "{typography.caption}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-legal:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"

---

## Components

### Buttons
**`button-primary`** — The main conversion driver across the entire Ecovacs interface, used for "Buy Now," "Add to Cart," and hero CTAs. It fills with the cobalt primary (#3877f5) at `{rounded.sm}` (8px) corners and 48px height, using white `{typography.button-md}` text. On hover it deepens to `{colors.primary-hover}` (#1c4aa2); on press it drops another shade to `{colors.primary-active}` (#1e5397). The disabled state washes out to `{colors.primary-disabled}` (#99c2ff), keeping the blue family but signaling non-interactivity.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More," "Compare Models," or "View Specs." It carries a 1px `{colors.primary}` border on a white background with blue text. On hover the fill inverts to solid `{colors.primary}` with white text, creating a smooth toggle effect. Height and padding mirror the primary button for consistent vertical alignment in side-by-side layouts.

**`button-accent`** — Reserved for promotional urgency: flash-sale hero CTAs, limited-time bundle offers, and seasonal campaign banners. It uses the vivid orange `{colors.accent-orange}` (#fa6400) with white text, same `{rounded.sm}` radius and 48px height. Hover darkens to approximately #d95500. This button appears sparingly — typically once per page — to prevent orange fatigue.

**`button-ghost`** — A transparent button with a 1px white border, used inside dark hero banners and video overlays where the primary blue would clash with background imagery. Text and border use `{colors.on-dark}` white, with a subtle white-tinted fill on hover (rgba(255,255,255,0.1)).

### Cards
**`product-card`** — The core commerce unit for DEEBOT and WINBOT listings. It sits on a white `{colors.surface-card}` background with `{rounded.sm}` corners and a 1px `{colors.hairline}` border. The card stacks a product render (top), a model name in `{typography.title-sm}`, a short feature tagline in `{typography.body-sm}`, and a price block at the bottom. On hover, the border shifts to `{colors.primary}` blue and a soft box-shadow (`0 6px 16px rgba(0,17,44,0.10)`) lifts the card off the canvas. A `feature-badge` or `promo-badge` can float in the top-left corner.

### Navigation
**`nav-bar`** — A fixed header bar at 64px height using `{colors.ink}` (#00112c) as the background with white text. Navigation links render in `{typography.nav-link}` (15px, weight 500) with `{spacing.lg}` horizontal spacing. The bar shrinks to 56px on scroll with a subtle shadow. Product categories (DEEBOT, WINBOT, AIRBOT) trigger a `nav-mega-menu` dropdown on hover, which renders on a white card with product thumbnails, quick links, and feature callouts in `{typography.body-sm}`.

**`nav-link-active`** — The active nav state adds a 2px bottom border in `{colors.primary}` blue beneath the white link text, maintaining `{typography.nav-link}` styling.

### Search
**`search-bar`** — A pill-shaped (`{rounded.full}`) search input with a `{colors.surface-soft}` background, 44px height, and a magnifying glass icon in `{colors.muted}`. On focus, the background clears to white and a 1px `{colors.primary}` border appears. Placeholder text uses `{typography.body-sm}` in `{colors.muted-soft}`.

### Forms
**`text-input`** — Standard text field for contact forms, email signup, and checkout. White background, `{rounded.sm}` corners, 48px height, 1px `{colors.hairline}` border. On focus, the border widens to 2px in `{colors.primary}` blue. Error states switch to 2px `{colors.error}` red with an inline error message below in `{typography.caption}`.

### Comparison Tables
**`comparison-row` / `comparison-row-alt`** — Alternating table rows used in the DEEBOT comparison tool. Even rows use `{colors.surface-card}` white; odd rows use `{colors.surface-soft}` (#f5f5f7). Each row has a 1px `{colors.hairline}` bottom border and `{typography.body-sm}` text. Feature-supported cells show a green (#089a43) checkmark icon; unsupported cells show a muted dash.

**`comparison-header`** — The fixed header row in comparison tables, using `{colors.ink}` navy background with white `{typography.title-sm}` text. Each column header contains a robot thumbnail and model name.

### Badges
**`feature-badge`** — Small uppercase labels for product features ("LiDAR," "AI," "Auto-Empty"). Uses `{colors.primary}` blue background with white text, `{rounded.xs}` corners, and `{typography.badge}` (11px, weight 700, uppercase).

**`feature-badge-success`** — A green variant for "In Stock" and "New" labels, using `{colors.success}` (#089a43) fill. Same sizing and typography as the standard feature badge.

**`promo-badge`** — An orange promotional badge for "Sale," "Bundle Deal," or "Limited" labels. Uses `{colors.accent-orange}` (#fa6400) fill, creating visual urgency without competing with the primary blue CTAs.

**`sale-badge`** — A red badge for deep-discount or clearance items, using `{colors.error}` (#c12424). Reserved for price-reduction contexts where orange would understate the discount.

### Price Block
**`price-block`** — A composite component for product pricing. The current price renders in `{typography.price-display}` (24px, weight 700) in `{colors.ink}`. When discounted, the original price sits beside it in `{typography.price-strike}` with line-through decoration in `{colors.muted}`. A savings callout in `{colors.error}` `{typography.caption}` text (e.g., "Save 20%") can appear below.

### Hero
**`hero-banner`** — Full-bleed hero sections dominate the Ecovacs homepage, cycling between DEEBOT product launches with dark (`{colors.ink}`) backgrounds and lifestyle scenes on lighter `{colors.surface-soft}` canvases. Headline text uses `{typography.display-xl}` (48px, weight 700) with a primary or ghost button centered below. Vertical padding uses `{spacing.section}` (64px). Video backgrounds are common, with a semi-transparent scrim overlay to maintain text contrast.

### Footer
**`footer-section`** — A dark footer using `{colors.ink}` (#00112c) background with `{spacing.section}` vertical padding. Contains columns of product links, support links, and social icons. Newsletter signup uses a text input with a `button-primary` submit button inline.

**`footer-link`** — Footer navigation links in `{typography.link}` (14px, weight 400) with `{colors.muted-soft}` (#99a3ad) text. Hover brightens to `{colors.on-dark}` white.

### Stock & Spec
**`stock-indicator`** — A small green text label ("In Stock") using `{colors.success}` and `{typography.caption}`. When stock is low, the variant `stock-indicator-low` switches to `{colors.accent-orange}` with text like "Only 3 left."

**`spec-table-cell`** — Individual cells in robot specification tables, using `{typography.spec-label}` (12px, weight 500) with `{colors.body}` text on a white background and tight `{spacing.sm}` padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger with full-screen overlay on `{colors.ink}` background; product grid goes single-column; hero padding reduces to `{spacing.xl}` (32px); buttons become full-width stacked; display-xl drops to display-md sizing; comparison table scrolls horizontally with sticky first column. |
| Tablet | 744-1128px | Nav stays horizontal but mega-menu becomes a dropdown list; product grid uses 2 columns with `{spacing.lg}` gutters; hero uses 48px padding; comparison table shows 3 robots side-by-side. |
| Desktop | 1128-1440px | Full mega-menu navigation with product thumbnails; product grid uses 3-4 columns; hero at full `{spacing.section}` padding; comparison table shows up to 4 robots; all components at default sizes. |
| Wide | > 1440px | Max-width container (1440px) centered with `{colors.canvas}` fill on sides; product grid can expand to 4 columns with wider cards; hero may include parallax scroll or autoplay video. |

### Touch Targets
- All buttons maintain a minimum 48px height on mobile for comfortable thumb tapping.
- Nav hamburger icon uses a 44px square touch area.
- Product card tap areas span the entire card surface, not just the text or image.
- Search bar input area is 44px tall with generous horizontal padding.
- Comparison table checkmarks and feature cells have a minimum 40px row height.

### Collapsing Strategy
- Top navigation collapses behind a hamburger icon on mobile (< 744px), opening a full-screen dark overlay with stacked product category links and a search bar at the top.
- Product grids collapse from 3-4 columns on desktop to 2 on tablet and 1 on mobile, with card images scaling proportionally.
- Comparison tables switch from side-by-side layout to a horizontally scrollable view with the feature-name column frozen on the left edge.
- Hero banners reduce padding, drop font sizes one step, and stack CTA buttons vertically below the headline.
- Footer columns stack into an accordion pattern on mobile, with each section title toggling its link list open and closed.
- Mega-menu navigation degrades to a simple dropdown list on tablet and a full-screen overlay on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom or branded typeface was detected; the site relies on system and web-standard fonts (Noto Sans, SF Pro, Helvetica Neue). A proprietary display font may be loaded via JavaScript or CDN that was not captured in static extraction.
- Hover and focus transition durations were not extracted; a default 200ms ease-in-out is assumed for interactive states.
- Dark mode tokens are not available; all values assume a light theme on the cool near-white canvas.
- The extracted palette contains many overlapping blues (#3877f5, #0075ff, #356cf1, #3070ed, #4098ff, #007aff, #1c4aa2, #1e5397); some may be gradient endpoints, animation keyframes, or framework defaults rather than distinct design tokens. The primary and hover assignments here represent the most frequently occurring values.
- Error and validation states for form inputs (beyond border color) could not be confirmed; error text color, icon placement, and inline messaging are inferred.
- Animation specifications for hero carousel transitions, product-card hover lifts, and comparison-table expand/collapse were not observed.
- Regional variants (the extracted page title suggests ecovacs.com/jp) may carry different promotional color schemes or layout patterns not represented here.
- The "swiper-icons" font family detected in extraction is a third-party carousel library font, not a brand design token.
- Specific grid gap values, card inner padding, and mega-menu spacing were inferred from the spacing scale rather than directly measured.
