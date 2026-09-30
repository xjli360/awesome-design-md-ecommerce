---
version: alpha
name: "Seiko"
source_url: "https://www.seikowatches.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Seiko's digital palette graduates through a tight family of navies — #193c72, #14315d, #102648 — that reference blued-steel movement components more than conventional brand color theory; the depth shifts by section, with category headers sitting deepest and product backgrounds lifting to mid-tone, so the entire page reads as a single atmospheric gradient rather than a primary/accent contrast. Against this navy field, Jost — a geometric humanist sans with precisely machined letterforms — carries all display text at weights that shift from 300 for decorative subtitles up to 700 for series names, standing in for the engraved lettering on a watch dial. The lone warm color in the palette is a heritage gold at #a89579, reserved exclusively for prestige and limited-edition callout badges rather than distributed across the general UI — the watchmaker's discipline of keeping certain complications for the top tier. Seiko red (#b30b00) runs deeper and more serious than consumer-brand coral, appearing only in promotional ribbons and limited-availability alerts, never diluted for hover states. The lighter blues (#4c83d8, #3849a2, #3e5c9a) act as interactive midground: links, breadcrumbs, and selected-state indicators all live in this band, giving the palette a coherent spectral story from near-black navy through cobalt to near-white surface. Product cards give each watch photograph unobstructed breathing room on a white surface-card against the soft #e8ecf1 viewport. Corner radii are minimal throughout — {rounded.sm} on cards, {rounded.xs} on inputs — preserving a mechanical precision that rejects the pill-and-blob softness common to lifestyle brands. Navigation is structured across two tiers: a slim utility bar for region and language selectors sits above a taller product-series bar organized by collection names (Prospex, Presage, Astron, Coutura, Lukia) rather than generic product types. The footer runs full #193c72 with reversed text, echoing Seiko's historical catalog covers and grounding the page in the same deep navy the brand has used on press materials since the 1960s.

colors:
  primary: "#193c72"
  primary-active: "#14315d"
  primary-dark: "#102648"
  primary-disabled: "#4c83d8"
  accent-red: "#b30b00"
  accent-gold: "#a89579"
  mid-blue: "#3849a2"
  mid-blue-soft: "#3e5c9a"
  ink: "#1a1a1a"
  body: "#2e2e2e"
  muted: "#4d4d4d"
  hairline: "#e6e6e6"
  hairline-soft: "#f0f0f0"
  canvas: "#f9f9f9"
  surface-soft: "#e8ecf1"
  surface-card: "#ffffff"
  surface-mid: "#d9d9d9"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#1a1a1a"

typography:
  display-xl:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.04em
  display-md:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.02em
  display-sm:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.03em
  series-label:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  body-md:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  spec-label:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0.06em
    textTransform: uppercase
  badge:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-md:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.04em
  utility-link:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  price-display:
    fontFamily: "'Jost', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0

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
    padding: 14px 32px
    height: 48px
    border: none
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
    hoverBackgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.on-dark}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.mid-blue}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
    placeholderColor: "{colors.muted}"
  search-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 40px 10px 14px
    height: 44px
    iconColor: "{colors.primary}"
  utility-bar:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.utility-link}"
    height: 36px
    paddingInline: "{spacing.xl}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    activeIndicatorColor: "{colors.primary}"
    activeIndicatorHeight: 2px
    paddingInline: "{spacing.xl}"
  nav-series-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.series-label}"
    height: 44px
    hoverTextColor: "{colors.accent-gold}"
    paddingInline: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    imageBackgroundColor: "{colors.canvas}"
    padding: "{spacing.base}"
    modelNameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    seriesTypography: "{typography.series-label}"
    seriesColor: "{colors.muted}"
    hoverBorderColor: "{colors.mid-blue-soft}"
    hoverShadow: "0 4px 16px rgba(25,60,114,0.10)"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    ctaButton: "{components.button-ghost}"
    minHeight: 560px
    paddingInline: "{spacing.xl}"
    overlayGradient: "linear-gradient(90deg, rgba(25,60,114,0.85) 40%, transparent 100%)"
  collection-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  limited-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  watch-spec-row:
    backgroundColor: "transparent"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline-soft}"
    paddingBlock: "{spacing.sm}"
  series-tab:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    activeTextColor: "{colors.primary}"
    activeBorderBottom: "2px solid {colors.primary}"
    hoverTextColor: "{colors.primary}"
    paddingBlock: "{spacing.md}"
    paddingInline: "{spacing.base}"
  breadcrumb:
    textColor: "{colors.mid-blue-soft}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted}"
    activeTextColor: "{colors.muted}"
  availability-alert:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
    iconColor: "{colors.on-dark}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.accent-gold}"
    linkColor: "{colors.surface-soft}"
    linkHoverColor: "{colors.on-dark}"
    borderTop: "2px solid {colors.mid-blue}"
    paddingBlock: "{spacing.xxl}"
    paddingInline: "{spacing.xl}"
  country-selector:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-dark}"
    typography: "{typography.utility-link}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.mid-blue}"
    padding: "4px 10px"
  watch-family-card:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-sm}"
    captionTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    minHeight: 320px
    hoverOverlayColor: "rgba(25,60,114,0.4)"

## Components

### Buttons

**`button-primary`** — Square-cornered navy CTA ({rounded.none}) following the watch industry convention of mechanical edges over organic curves. Background is #193c72 and slides to #14315d on hover; uppercase Jost at 0.08em tracking references stamped bezel text. Used on "Add to Cart," "Find a Retailer," and all primary collection entry points.

**`button-secondary`** — Transparent fill with a 1px #193c72 border and matching uppercase label; sits alongside `button-primary` on product detail pages for secondary actions like "Learn More" or "Compare." Hover fills lightly with {colors.surface-soft} to confirm interaction without competing with the primary.

**`button-ghost`** — White border on transparent background, deployed over hero banners and dark navy sections where the primary navy button would vanish. Padding matches `button-primary` for identical visual weight in side-by-side hero layouts.

**`button-text-link`** — Unstyled underlined link in {colors.mid-blue}, used for in-body spec-page references and breadcrumb overrides. No button chrome; inline with body copy.

### Inputs & Search

**`search-input`** — A clean single-bar search with a magnifier icon in {colors.primary} at the right edge. Border is minimal ({colors.hairline}), focus ring swaps to {colors.primary} to remain on-brand. Lives in the utility-bar layer on mobile and expands to full-width overlay on desktop.

**`text-input`** — Shared with forms (newsletter, dealer locator, contact). {rounded.xs} preserves the mechanical aesthetic. Placeholder text in {colors.muted}.

### Navigation

**`utility-bar`** — Slim 36px bar in {colors.primary-dark} (#102648) running region/language selectors and perhaps a store-finder link. Type is tiny ({typography.utility-link}) in reversed white. Disappears on mobile, collapsing into the hamburger drawer.

**`nav-bar`** — 64px white bar containing the Seiko logotype left, search and region icons right. Active section is underscored with a 2px {colors.primary} line. Sticky on scroll with a hairline bottom border.

**`nav-series-bar`** — Secondary full-width bar in solid {colors.primary} listing collection families (Prospex, Presage, Astron, Coutura, Lukia, 5 Sports). Labels use {typography.series-label} — small-caps uppercase tracking — in white, shifting to {colors.accent-gold} on hover to signal the prestige hierarchy.

### Product Cards

**`product-card`** — Flat white card with a hairline border and zero radius; the absence of rounding is intentional, echoing case geometry. On hover a subtle blue shadow (0 4px 16px rgba(25,60,114,0.10)) lifts the card without deforming its edges. Series label renders in {typography.series-label} above the model name; price renders in {typography.price-display} below. Badge slots (new/limited/collection) stack top-left.

### Badges & Tags

**`collection-badge`** — Gold (#a89579) fill, black text, zero radius, uppercase microtype. Applied sparingly to prestige lines (Grand Seiko tier references, Presage Sharp Edged) to signal the reserve character of the accent color — one to two per collection grid page maximum.

**`limited-badge`** — Deep Seiko red (#b30b00) fill, white text. Appears on time-limited releases and inventory-scarcity alerts. Never used for promotional discounts — that role belongs to an inline text note rather than a badge.

**`new-badge`** — Navy fill, white text. Replaces `collection-badge` for current-season introductions that do not carry prestige pricing.

### Watch Spec Table

**`watch-spec-row`** — Horizontal label/value pairs separated by {colors.hairline-soft} bottom borders. Labels are uppercase small-caps via {typography.spec-label} in {colors.muted}; values sit in {typography.body-sm} in {colors.ink}. The pattern repeats for case diameter, water resistance, movement calibre, power reserve, and strap material — the canonical Seiko specification columns.

### Series Tabs

**`series-tab`** — Horizontal scroll row of collection-family tabs above a product grid. Inactive tabs are {colors.muted}; the active tab gains a 2px {colors.primary} underline and full navy text, mirroring the nav-bar active indicator. Used on collection landing pages to switch between sub-families (e.g., Prospex Diver → Prospex Fieldmaster).

### Hero Banner

**`hero-banner`** — Full-bleed minimum 560px section in {colors.primary} with an optional left-leaning linear-gradient overlay that fades to transparent, allowing a watch-in-action photograph to bleed off the right edge while keeping headline legibility. Headline in {typography.display-xl} weight 300 runs wide and light — deliberately not bold — to let the imagery hold tension. CTA uses `button-ghost`.

### Availability Alert

**`availability-alert`** — Full-width flat {colors.accent-red} bar that inserts above the Add-to-Cart zone on sold-out or pre-order PDPs. No border radius. Text in {typography.body-sm} reversed white, with a small clock or warning icon left-aligned.

### Footer

**`footer`** — Deep navy (#193c72) with {colors.accent-gold} column headings, white link text, and a top accent border in {colors.mid-blue}. Four columns: Collections, Support, Company, Social. A secondary row below the columns carries the legal micro-links in {typography.caption}. The heavy navy grounds the page and closes the palette loop opened by the hero.

### Country Selector

**`country-selector`** — Compact pill-adjacent control in {colors.primary-active} with a 1px mid-blue border, sitting in the utility bar. Dropdown reveals a two-column world-region grid. Type is {typography.utility-link} to keep visual weight minimal against the dark bar.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Utility bar hidden; nav-series-bar collapses to hamburger drawer; product grid goes 2-column; hero headline drops to {typography.display-md}; spec table stacks label over value |
| Tablet | 744–1128px | Nav-series-bar scrolls horizontally; product grid is 3-column; hero switches to 60/40 text/image split |
| Desktop | 1128–1440px | Full three-bar navigation (utility + main + series); product grid 4-column; hero at full 560px with gradient overlay active |
| Wide | > 1440px | Max-width container 1440px centered; hero image scales but text column width caps at 600px; grid stays 4-column with larger inter-card spacing |

### Touch Targets

- All nav-bar icons and series-tab items minimum 44 × 44px tap target
- Product cards are full-tap-zone links — no separate "tap here" sub-element
- `button-primary` and `button-secondary` minimum height 48px on all breakpoints
- Country selector dropdown items minimum 44px row height
- Series-tab horizontal scroll uses momentum scrolling (`-webkit-overflow-scrolling: touch`) with visible partial-crop on the right edge as scroll affordance

### Collapsing Strategy

- Utility bar (region/language) folds into hamburger drawer on < 744px
- Nav-series-bar (collection families) becomes a horizontal scroll row on tablet; full hamburger drawer item on mobile
- Hero banner shifts from side-by-side layout to stacked image-below-text on mobile with image cropped to 300px height
- Watch spec table reflows from two-column label/value grid to single-column stacked pairs on mobile
- Footer collapses four columns to single accordion-accordion-accordion-accordion on mobile with {colors.hairline} dividers

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom display typeface confirmed beyond Jost; Grand Seiko and prestige sub-brands may use a distinct serif or Japanese-script face not captured in the font-stack extraction
- Several extracted hex values (#0d6efd, #6610f2, #6f42c1, #d63384, #0dcaf0, #fd7e14) match Bootstrap 5 defaults exactly and were excluded as framework noise — if any are genuinely used for UI states, they would need a live-audit pass
- Exact motion/transition values (duration, easing curves for the hero crossfade and card hover lift) not extractable from static scrape
- Icon set details (outline vs. filled, stroke weight, grid size) not confirmed — Seiko uses custom SVG icons for movement complication indicators that differ from any standard icon library
- Dark-mode palette, if any, not confirmed — the navy-dominant scheme may simply invert to a lighter canvas rather than using a distinct dark-mode token set
- Hover states for `nav-series-bar` items use {colors.accent-gold} by inference from brand tier logic; actual interactive color not verified from live inspection
- Product image background color on collection grid cards not confirmed as pure white vs. a warm near-white; #f9f9f9 used as best approximation from extracted surfaces
