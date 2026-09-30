---
version: alpha
name: "B4Adventure"
source_url: "https://b4adventure.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Five shades of the same cold-water column — from the deep anchoring teal of #226d7a down through its near-twin #1e6d7a, then rising through the fluorescent surface glint of #22b8d1, and finally dissolving into the ice washes of #b0e0e9 and #e4f5fa — that is the entire B4Adventure palette, built without a single warm accent or earth note, as focused as a dive kit where every piece earns its weight. The name doubles as a temporal claim: Before Adventure, the moment of preparation, the kit spread on the floor the night before departure. The UI mirrors that pre-launch energy with an information-forward posture — spec tables, filter panels, and comparison tools doing the heavy lifting rather than full-bleed photography — because the person shopping here is packing, not dreaming. Open Sans carries the voice throughout at modest weights; the hierarchy runs on size contrast and the palette's cool voltage rather than weight escalation, body copy at 400 and titles at 600, 700 reserved for display moments that need to read from across a campsite. Components default to {rounded.md} (12px) rather than the pill shapes of lifestyle apps or the hard corners of a mil-spec catalog — the pragmatic middle register that says this is gear, not aesthetics. The accent #22b8d1 is the fluorescent marker of the system, applied to primary CTAs and hover states like the reflective strip on a dry bag, visible from distance against both the dark teal fields and the pale ice-blue surfaces. The deep primary #226d7a anchors nav bars and filled badge states; its near-twin #1e6d7a provides active and pressed depth cues without switching hue families. The ice-blue washes — {colors.surface-soft} at #e4f5fa and {colors.accent-soft} at #b0e0e9 — keep the pale end of the palette active for card backgrounds and alternating table rows rather than defaulting to blank white-on-white layouts that would erase the brand's tonal discipline.

colors:
  primary: "#226d7a"
  primary-active: "#1e6d7a"
  primary-disabled: "#8cbec7"
  accent: "#22b8d1"
  accent-soft: "#b0e0e9"
  ink: "#1a3035"
  body: "#2e5059"
  muted: "#5c808a"
  hairline: "#c8e8ed"
  canvas: "#ffffff"
  surface-soft: "#e4f5fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 15px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.accent}"
    height: 44px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
    padding: "0 {spacing.xl}"
  nav-bar-link-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    imageRounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    captionTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    hoverBorder: "1px solid {colors.accent}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    minHeight: 480px
    padding: "{spacing.xxl} {spacing.xl}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
  announcement-bar:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label}"
    height: 36px
    padding: "0 {spacing.base}"
  gear-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  gear-badge-featured:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  category-tile:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    minHeight: 160px
    padding: "{spacing.base}"
    hoverBackgroundColor: "{colors.primary-active}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.title-sm}"
    rowTextColor: "{colors.body}"
    rowTypography: "{typography.body-sm}"
    alternateRowColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Filled #226d7a rectangle with {rounded.sm} (8px) corners and white Open Sans 600 text at 15px, 44px tall. On hover the background brightens to the accent cyan #22b8d1 in a watery surface-reflection shift that is the most legible state change in the system; active/pressed deepens to {colors.primary-active}. Disabled fades to {colors.primary-disabled} with no opacity change on the label. Use for all primary purchase, add-to-cart, and navigation CTAs.

**`button-secondary`** — White background with a 2px {colors.primary} border and matching teal label text. On hover the fill draws in as {colors.surface-soft} (ice blue) while border and text shift to {colors.primary-active}, creating a contained hover without introducing a new color. Use for secondary actions, filter confirmations, and "Learn More" calls where a primary CTA already occupies the same viewport.

**`button-ghost`** — Transparent background with teal text only, no border. Reserved for low-emphasis in-content actions — "See All" links within section headers, tertiary nav items, and inline text actions inside spec panels where a bordered box would visually compete with table structure.

### Nav Bar

**`nav-bar`** — Deep teal (#226d7a) full-width bar at 60px height carrying white Open Sans 600 nav links. Brand wordmark or logo anchors the left; primary category links center or fill the right cluster; cart, search, and account icons close the far right. Active link state uses {colors.primary-active} as a subtle same-hue inset with no underline — the tonal shift is readable against the dark field without requiring a contrasting indicator. On mobile, the nav collapses behind a hamburger icon and draws a full-height teal drawer from the left edge, with category links reloaded as accordion rows at 48px touch height.

### Product Card

**`product-card`** — White card with {rounded.md} (12px) corners and a 1px {colors.hairline} border; no drop shadow. Product image fills the top portion at full bleed with matching 12px radius at the top corners. Name in {typography.title-sm}, price in {typography.title-md} rendered in {colors.primary}. Gear badges stack horizontally below the image using the `gear-badge` component, capped at three per card. On hover the border transitions to {colors.accent} (bright cyan) — a single-color cue that reads as a clean lift without elevation.

### Hero Banner

**`hero-banner`** — Deep teal field at minimum 480px height with headline in {typography.display-xl} and subhead in {typography.display-sm}, both white. A `button-primary` CTA sits below the subhead with {spacing.lg} gap; on hover it flips to accent cyan, producing the highest-contrast moment on the page. Photography works best as a right-side inset (cropped to the right 40–50% of the hero) rather than a full bleed, since dark imagery against the teal field tends to muddiness; light or high-contrast product photography is the safe default.

### Announcement Bar

**`announcement-bar`** — A 36px strip of accent cyan (#22b8d1) sitting above the nav bar, carrying white uppercase label text at 12px/700. The cyan-over-teal two-tone top band is the brand's most immediately distinctive page-top signature. Used for sitewide promotions, free-shipping thresholds, and seasonal callouts. On mobile the strip drops to a single short message and clips overflow rather than wrapping to preserve the 36px strip height.

### Gear Badge

**`gear-badge`** — Small {rounded.xs} (4px) ice-blue chip ({colors.surface-soft} fill) with teal uppercase label type at 12px/700. Stacks horizontally on product cards to signal attributes such as "Waterproof", "UV 50+", "Packable", or "Field Tested". When a product carries a featured or new designation, `gear-badge-featured` applies the filled teal treatment with white text, distinguishing it from attribute badges at a glance. Never more than three badges per card to prevent stacking from crowding the price row.

### Category Tile

**`category-tile`** — Teal-filled {rounded.md} tile, minimum 160px tall, used in shop-by-category grid layouts. Category label in white {typography.title-md} anchors the bottom-left with a monochrome icon inset above it. On hover, background shifts to {colors.primary-active} and a right-facing arrow slides in from the right edge. Tiles lay out 2-across on mobile, 3-across on tablet, and 4-across on desktop within a constrained section.

### Spec Table

**`spec-table`** — Clean data table with an ice-blue header row ({colors.surface-soft} background, {typography.title-sm} in {colors.ink}) and alternating {colors.surface-soft}/{colors.canvas} row fills in {typography.body-sm}. Horizontal rules in {colors.hairline}; no vertical dividers. Used for product dimensions, material composition, weight ratings, and compatibility matrices. The alternating ice-blue rows connect the table to the palette without requiring additional colors, and make row-scanning tractable on wide product comparison pages.

### Footer

**`footer`** — Deep teal (#226d7a) full-width footer matching the nav-bar hue, creating a teal-bookend bracket around every page. Column headings in {typography.title-sm} at white/600; links in {typography.body-sm} at white/400 with an underline on hover. Social icon row uses white circular icon buttons at 36px with {rounded.full}. A hairline-width teal-on-teal divider separates the link columns from the legal/copyright row below, which carries {typography.caption} text at reduced opacity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav drawer; hero headline drops to {typography.display-md}; category tiles 2-across; spec tables scroll horizontally; announcement bar single short message |
| Tablet | 744–1128px | 2-column product grid; nav shows primary items, overflow collapses to "More" dropdown; hero at full height with text+image side-by-side layout; category tiles 3-across |
| Desktop | 1128–1440px | 3–4 column product grid; full nav bar expanded; hero content width capped and centered on teal field; spec tables at full width with sticky header row |
| Wide | > 1440px | Content max-width 1440px; nav and footer bleed edge-to-edge; product grid extends to 5-across; hero text line-length capped via max-width to prevent overly long measure |

### Touch Targets
- All interactive elements maintain a minimum 44×44px tap target
- Gear badges are display-only on cards; tap activates the full product card, not the badge
- Nav icons (cart, search, hamburger) reach 44px via padding, not raw element size
- Filter toggles on mobile use full-width rows at 48px height for comfortable one-handed operation
- Announcement bar links hit 36px height minimum; full-bar tap area routes to the promotion destination

### Collapsing Strategy
- Primary navigation collapses to a hamburger at < 744px; mega-menus become accordion panels inside the teal drawer
- Product filters shift from a left sidebar panel (desktop) to a bottom sheet or sticky top filter strip (mobile)
- Spec tables add horizontal scroll on mobile rather than reflowing into stacked key-value rows, preserving side-by-side comparison utility
- Hero CTAs stack vertically (primary above secondary/ghost) on mobile; sit side-by-side on tablet and above
- Footer columns reduce from 4-across to 2-across on tablet, then to single-column accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Live site returned a 403 Forbidden during extraction — only CSS-declared hex values were captured; no rendered imagery, SVG brand marks, or canvas-painted tokens were inspected
- Brand logo, wordmark treatment, and any proprietary or licensed typeface are unknown; Open Sans is inferred as the most intentional choice from the extracted font stack but may be a generic fallback
- Dark and neutral system colors (ink, body, muted, hairline) were not extractable and have been harmonically derived from the teal palette — verify against brand guidelines before production use
- No dark mode palette was detected or can be inferred from the extraction
- Exact breakpoint values are estimated from category conventions; actual CSS media query thresholds were not captured
- Icon library, illustration style, and photography art direction are unknown
- No pricing display patterns, sale badge treatments, add-to-cart interaction states, or checkout UI were visible during extraction
- Whether #22b8d1 is a deliberate interactive accent or simply a lighter variant of the primary teal cannot be confirmed without live UI inspection
