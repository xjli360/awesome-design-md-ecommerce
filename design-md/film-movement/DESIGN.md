---
version: alpha
name: "Film Movement"
source_url: "https://www.filmmovement.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A cinema distributor's digital storefront that wears its love of film on its sleeve — literally, via a hot-pink primary (#fe2873) that reads less like a brand guideline and more like a neon marquee for a repertory house. That pink, paired with a deep charcoal ink (#1e1e1e) and a warm parchment canvas (#f5f2e9), creates a system that feels both archival and alive: the pink is the "now playing" voltage, the charcoal is the theater seat, the parchment is the lobby carpet. Abril Fatface, a slab serif with dramatic weight contrast, handles display roles — it's the font of poster credits and opening titles, not body copy. Montserrat and Nunito Sans provide the utilitarian sans-serif work for navigation, pricing, and metadata, keeping the experience legible while the display type does the emotive work. The extracted palette reveals a secondary teal family (#016684, #00728d, #2bb4df) that likely serves as a supporting accent for membership tiers, badges, or genre tags, and a goldenrod (#f8d063) that could mark "staff picks" or "new arrivals." The system avoids hard corners — buttons and cards use {rounded.sm} and {rounded.md} — but the overall mood is more editorial than e-commerce: generous whitespace, serif-led hierarchy, and a color story that feels curated rather than algorithmic. The pink is not a discount banner; it's a signal of taste.

colors:
  primary: "#fe2873"
  primary-active: "#bf2059"
  primary-disabled: "#fc96ba"
  ink: "#1e1e1e"
  body: "#3f3f3f"
  muted: "#777279"
  muted-soft: "#d4d4d4"
  hairline: "#e1e3e2"
  hairline-soft: "#ededed"
  canvas: "#f5f2e9"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#016684"
  accent-teal-light: "#2bb4df"
  accent-gold: "#f8d063"
  accent-gold-soft: "#fbf1bf"
  accent-warm: "#fae7b7"
  accent-blue: "#4c6eae"
  accent-red: "#e31937"

typography:
  display-xl:
    fontFamily: "'Abril Fatface', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0
  display-lg:
    fontFamily: "'Abril Fatface', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "'Abril Fatface', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
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
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-meta:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.canvas}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  membership-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, always rendered in the brand's signature pink (#fe2873) with white text and uppercase Montserrat at 14px. On hover or active, it deepens to {colors.primary-active} (#bf2059). The disabled state uses a soft pink {colors.primary-disabled} (#fc96ba) to maintain visual continuity without implying interactivity. All buttons share a consistent {rounded.sm} (8px) corner radius and 44px height for touch consistency.

**`button-secondary`** — An outlined alternative for less prominent actions, using a 2px solid {colors.ink} border on the warm canvas background. On hover, the button fills solid with {colors.ink} and inverts the text to {colors.canvas}. This button is used for "Add to Cart" alternatives, "Learn More" links, and secondary purchase paths.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel," "View Details," or "Remove." The text color matches {colors.primary} to maintain brand consistency, and the hover state adds a subtle background tint (not yet extracted, likely a 10% opacity of primary).

### Cards
**`product-card`** — The core content container for film listings, featuring a poster image that spans the full width of the card, followed by the film title in {typography.title-sm} and metadata (director, year, runtime) in {typography.caption} at {colors.muted}. The card uses {rounded.md} (12px) and sits on a white {colors.surface-card} background. No border is used; the card relies on the contrast between the white surface and the warm {colors.canvas} page background for definition.

**`product-card-title`** — The film title within a product card, set in Montserrat 600 weight at 16px. It sits directly below the poster image with {spacing.base} padding on the sides and top, and {spacing.xs} on the bottom before the metadata block.

**`product-card-meta`** — The metadata block below the title, using Nunito Sans at 12px in {colors.muted} (#777279). Padding is {spacing.xs} top and {spacing.base} bottom to create a comfortable reading rhythm.

### Badges
**`badge-new`** — A small, high-contrast badge in the brand pink, used to flag new releases or recently added titles. The uppercase Montserrat at 11px sits on a tight {rounded.xs} (4px) pill with 2px vertical and 8px horizontal padding.

**`badge-teal`** — A secondary badge in {colors.accent-teal} (#016684), likely used for membership tiers, curated collections, or special programming. Same typography and sizing as the new badge, but the color signals a different category of content.

**`badge-gold`** — A warm gold badge in {colors.accent-gold} (#f8d063) with dark text, used for "Staff Pick," "Award Winner," or "Critic's Choice" designations. The gold-on-ink contrast is lower than the pink or teal badges, making it feel more editorial than promotional.

### Navigation
**`nav-bar`** — A fixed-height (72px) top navigation bar on the warm canvas background, with a subtle bottom border in {colors.hairline-soft} (#ededed). Navigation links use Montserrat at 14px with 500 weight and 0.3px letter spacing. The active state underlines the link with a 2px {colors.primary} border and shifts the text color to pink.

**`nav-link-active`** — The active navigation state, distinguished by the pink text color and a 2px solid underline in the same pink. This creates a clear, brand-consistent wayfinding signal without relying on background fills or heavy visual weight.

### Forms
**`text-input`** — Standard text inputs for search, login, and checkout forms. They use a white background with a 1px {colors.hairline} (#e1e3e2) border and {rounded.sm} corners. On focus, the border thickens to 2px and shifts to {colors.primary}, providing a clear but understated interaction state. Input text uses Nunito Sans at 16px for readability.

**`search-bar`** — A pill-shaped search input ({rounded.full}) with a white background and 1px hairline border. The pill shape differentiates it from standard text inputs and gives it a more approachable, discovery-oriented feel. On focus, the border becomes 2px solid {colors.primary}.

### Footer
**`footer`** — A dark footer section on {colors.ink} (#1e1e1e) background with light text. Links are rendered in {colors.muted-soft} (#d4d4d4) and use the standard link typography. The footer has generous padding of {spacing.xxl} (48px) vertically and {spacing.section} (64px) horizontally on desktop, creating a substantial closing section to the page.

### Hero
**`hero-section`** — The primary hero area, typically used on the homepage or collection pages. It uses a dark {colors.ink} background with white text, creating high contrast for the Abril Fatface display typography. The hero title uses {typography.display-xl} at 48px, while the subtitle uses body copy in {colors.muted-soft} for hierarchy.

### Filters
**`filter-chip`** — A pill-shaped filter option for browsing films by genre, year, or collection. Inactive chips have a light background ({colors.surface-soft}) with a 1px hairline border. Active chips invert to a solid {colors.ink} background with white text, providing clear visual feedback for the selected state.

### Membership
**`membership-badge`** — A teal pill badge used to indicate membership status or subscription tiers. The teal color ({colors.accent-teal}) differentiates membership content from the general catalog, which uses the pink primary. The badge uses {rounded.full} for a friendly, approachable feel and slightly larger padding (4px vertical, 12px horizontal) than the content badges.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger; hero text reduces to {typography.display-lg}; product cards stack vertically; filter chips wrap to 2-column grid; footer collapses to single column |
| Tablet | 744–1128px | 2-column product grid; nav links visible but condensed; hero maintains {typography.display-xl} but with reduced padding; filter chips in horizontal scroll strip |
| Desktop | 1128–1440px | 3-column product grid; full nav with all links; hero at full width with max-width container; filter chips in horizontal strip with overflow fade |
| Wide | > 1440px | 4-column product grid; max-width container (1440px) centered; hero content centered with 50% max-width; additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, chips) maintain minimum 44px height for touch accessibility
- Search bar and text inputs are 48px tall for comfortable tapping
- Filter chips are 36px tall with 16px horizontal padding, exceeding the 44px touch target in width
- Nav links have 72px tap area height due to the nav-bar container

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px, with the full-width drawer overlay
- Product grid collapses from 4 columns on wide screens to 1 column on mobile
- Filter chips transition from a horizontal scroll strip on desktop/tablet to a wrapped 2-column grid on mobile
- Footer columns stack vertically below 744px, with each section taking full width
- Hero section reduces vertical padding on mobile, from {spacing.section} to {spacing.xxl}

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links are inferred from the extracted primary-active color (#bf2059) but exact transition timing and opacity values are not confirmed
- Error states for form inputs (border color, helper text styling) are not present in the extracted data
- Dark mode is not supported; the system is built on a warm light canvas (#f5f2e9) with no dark variant detected
- The Abril Fatface font may be used only for specific display roles (hero titles, section headers) — its exact sizing hierarchy beyond the three display levels is uncertain
- The secondary teal, gold, and blue accent colors are inferred from frequency in the extracted palette but their specific use cases (membership, badges, genre tags) are speculative
- Modal and overlay styling (background scrim opacity, close button placement) is not captured
- Loading states and skeleton screen patterns are not present in the extracted data
- The extracted font list includes "Arial!important" which suggests some inline overrides, but the primary font stack (Abril Fatface, Montserrat, Nunito Sans) is consistent enough to build from
- Checkout flow components (payment forms, address inputs, order summary) are not represented in the extracted data
- Animation and transition timing values (hover fade, card lift, menu open/close) are not available
