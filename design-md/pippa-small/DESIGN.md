---
version: alpha
name: "Pippa Small"
source_url: "https://www.pippasmall.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Raw gold wire coiled around a rough-cut turquoise captures the Pippa Small ethos before a single navigation element loads — the store inherits the patience of artisans in Kabul and Rajasthan who fabricate the jewellery by hand. Near-black ink (#1c1b1b) sits over layered cool grounds (#efefef, #f1f1f1) that shift subtly by section rather than holding a single stark white canvas, giving the site the density of a museum catalogue rather than a product feed. Playfair Display carries every headline in its classical serif cut — the font choice never concedes to a condensed grotesque or a geometric alternative, committing fully to the handpress-book register and treating each collection name as a chapter heading. Against this composed neutral field a single voltage fires: a deep fuchsia-pink (#e13e82) that marks every primary call-to-action — Add to Cart, newsletter submit, checkout proceed — with the decisiveness of a wax seal on archival paper. Two ecological accent tones, sage (#d2e4c4) and forest green (#307a07), surface in provenance callouts and sustainability strips, anchoring the brand's artisan-community commitments across Afghanistan, Pakistan, and India without overwhelming the editorial neutral field. Warm silver (#c0c0c0) and muted blush (#e4c4c4) handle secondary surfaces: image overlays, hover tints, soft dividers. Rounded tokens sit at {rounded.none} on primary buttons — flat, sharp geometry that reads as hand-finished rather than factory-cast — while {rounded.xs} marks provenance tags as small pressed labels. Spacing breathes at {spacing.section} between story modules, giving documentary photography room to read fully before the next product grid begins. The overall cadence is slow and intentional, built for customers who expect to spend time reading provenance copy the way they would inspect a hallmark stamp — turning the piece over to find the maker's mark before committing.

colors:
  primary: "#e13e82"
  primary-active: "#c8232c"
  primary-disabled: "#e4c4c4"
  ink: "#1c1b1b"
  body: "#363636"
  muted: "#6a6a6a"
  muted-soft: "#a1a1a1"
  hairline: "#dedede"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f1f1f1"
  surface-card: "#e9e9e9"
  on-primary: "#ffffff"
  accent-sage: "#d2e4c4"
  accent-forest: "#307a07"
  accent-blush: "#e4c4c4"
  silver: "#c0c0c0"

typography:
  display-xl:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
  body-md:
    fontFamily: "sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  button-md:
    fontFamily: "sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.2px
    textTransform: uppercase
  button-sm:
    fontFamily: "sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  label-upper:
    fontFamily: "sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 2px
    textTransform: uppercase
  nav-link:
    fontFamily: "sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.5px
  price:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 0 {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    gap: "{spacing.sm}"
  product-card-hover:
    imageOverlay: "{colors.hairline-soft}"
    overlayOpacity: 0.04
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    minHeight: 560px
    contentMaxWidth: 640px
    padding: "{spacing.section}"
  provenance-badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  sustainability-strip:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.section}"
  story-module:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    imageWidth: "50%"
    gap: "{spacing.xxl}"
    padding: "{spacing.section} 0"
  collection-label:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.label-upper}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.sm}"
  newsletter-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headlineTypography: "{typography.display-sm}"
    padding: "{spacing.xxl} {spacing.section}"
    inputBackground: transparent
    inputBorder: "1px solid {colors.silver}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonTypography: "{typography.button-sm}"
  footer:
    backgroundColor: "#121212"
    textColor: "{colors.muted-soft}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headlineTypography: "{typography.label-upper}"
    padding: "{spacing.section}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    gap: "{spacing.xs}"

## Components

### Buttons

**`button-primary`** — Fuchsia-pink (#e13e82) fill on a flat, square-cornered rectangle (`{rounded.none}`); all-caps spaced label in `{typography.button-md}` at 13px with 1.2px tracking. The absence of border-radius is deliberate — it registers as handmade stamp rather than software-era pill. Active state deepens to #c8232c; disabled bleaches to soft blush `{colors.primary-disabled}` with a `{colors.muted}` label. Height fixed at 48px across all breakpoints.

**`button-secondary`** — White canvas fill with a 1px solid ink border; mirrors the primary label style and height for visual pairing on PDPs. Appears as the "Wishlist" or "Enquire" CTA alongside Add to Cart, maintaining equal visual weight without the fuchsia voltage.

**`button-ghost`** — Transparent background with underlined ink text; used inline within editorial body copy and provenance story modules for non-commerce navigation such as "Meet the Makers" or "Read More". No height constraint — flows inline with paragraph rhythm.

### Text Input

**`text-input`** — Full 1px `{colors.hairline}` border rectangle at rest, deepening to `{colors.ink}` on focus; no border-radius consistent with the brand's sharp-edged aesthetic. Placeholder in `{colors.muted}` at `{typography.body-sm}`. Used in search, newsletter signup, and checkout address fields. Height 48px.

### Nav Bar

**`nav-bar`** — White canvas at 64px height with a 1px `{colors.hairline}` bottom border. Logo rendered in Playfair Display sits centred or left-anchored. Collection links in `{typography.nav-link}` (13px, tracked sans-serif) span horizontally; secondary links (Journal, About, Stockists) appear at reduced prominence to the right. On scroll, a hairline shadow replaces the bottom border via `nav-bar-scrolled` without adding a colour fill. Hamburger icon replaces link set below 744px.

### Product Card

**`product-card`** — Zero border-radius with a 4:5 portrait image on a white card ground. Product name in `{typography.title-md}` (Playfair Display, 18px, weight 600); price in `{typography.price}` (Playfair Display, 16px, regular). Hover adds a barely-visible `{colors.hairline-soft}` tint at 4% opacity over the image — enough to signal interactivity without a heavy overlay. No drop shadow; image contrast carries depth. Provenance badges overlay the lower-left image corner.

### Hero Banner

**`hero-banner`** — Full-bleed editorial image with a text block at `{spacing.section}` inset padding. Headline in `{typography.display-xl}` (Playfair Display, 40px, weight 700); subline in `{typography.body-md}` (sans-serif, 16px). Minimum height 560px. Background `{colors.surface-soft}` used when no image fills the frame. On mobile the text block stacks below the image at full width with headline scaling to `{typography.display-md}`.

### Provenance Badge

**`provenance-badge`** — Sage (#d2e4c4) chip at `{rounded.xs}` (2px) with `{typography.label-upper}` (10px, 2px tracking, caps). Surfaces origin country or artisan collective name on product cards and PDP headers. Never rendered in the primary fuchsia — provenance and commerce stay visually distinct.

### Sustainability Strip

**`sustainability-strip`** — Full-width sage (#d2e4c4) band carrying a single `{typography.body-sm}` statement ("Hand-made in Afghanistan", "Certified Fairtrade"). Padding `{spacing.md}` vertical, `{spacing.section}` horizontal. Inserted between content modules as a quiet factual interruption rather than a marketing block.

### Story Module

**`story-module`** — 50/50 split between documentary photography and editorial copy. Headline in `{typography.display-md}` (Playfair Display, 28px), body in `{typography.body-md}`. Gap between image and text `{spacing.xxl}`; module padding `{spacing.section}` top and bottom. Image alternates sides across successive modules. Used for artisan profiles, collection origins, and ethical-sourcing narratives. On mobile, image moves above text at full width.

### Newsletter Bar

**`newsletter-bar`** — Near-black (`{colors.ink}`) fill with white copy. Headline in `{typography.display-sm}` (Playfair Display, 22px). Input field carries a 1px `{colors.silver}` border on a transparent background; submit button fires the fuchsia primary with `{typography.button-sm}` all-caps label. Padding `{spacing.xxl}` vertical, `{spacing.section}` horizontal.

### Footer

**`footer`** — Deeper near-black (#121212) separates the footer from the newsletter bar above it. Column heads in `{typography.label-upper}` (caps, 2px tracked); links in `{typography.body-sm}` at `{colors.muted-soft}`, brightening to `{colors.canvas}` on hover. Social icons inline with the legal line at the base. Four columns on desktop, two-column grid on tablet, stacked on mobile.

### Collection Label

**`collection-label`** — Transparent background, `{colors.muted}` text in `{typography.label-upper}`, underscored by a 1px `{colors.hairline}`. Sits above product grids to identify collection or category name without requiring a filled chip or background block. Acts as a visual chapter heading for each grid section.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + centred logo; hero text block stacks below image; product grid 2-column; story modules stack vertically (image above text); footer columns stack single column |
| Tablet | 744–1128px | Nav shows 2–3 primary links; product grid 3-column; hero text overlaps image at 40% width; story modules stay 60/40 split; footer 2×2 grid |
| Desktop | 1128–1440px | Full nav bar with all collection links; product grid 4-column; 50/50 story modules; newsletter bar full width |
| Wide | > 1440px | Content max-width cap at 1440px with auto side margins; hero image extends edge-to-edge behind constrained text block |

### Touch Targets

- All buttons maintain 48px height minimum across breakpoints
- Nav hamburger icon 44×44px touch target with extended invisible padding
- Entire product card surface is tappable on mobile, not just the image or title
- Provenance badge minimum 32px height with 8px horizontal padding on touch viewports
- Footer links minimum 44px vertical tap clearance via increased line-height

### Collapsing Strategy

- Top nav: hamburger at < 744px; off-canvas drawer slides in with full collection link tree including provenance and about sub-links
- Story modules: image moves above text on mobile, never hidden or cropped to a thumbnail
- Product grid: 2-col mobile → 3-col tablet → 4-col desktop; strict uniform rows, no masonry layout
- Hero headline scales: `{typography.display-xl}` (40px) desktop → `{typography.display-md}` (28px) tablet → `{typography.display-sm}` (22px) mobile
- Footer: 4-col desktop → 2-col tablet → single-col mobile; column heads remain visible at all breakpoints
- Sustainability strip remains full-width at all breakpoints; text wraps if needed rather than truncating

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No dedicated brand typeface file detected; Playfair Display assumed to load from Google Fonts — exact weight subset and whether an italic cut is used not confirmed from extraction
- Primary fuchsia (#e13e82) confirmed as extracted; no CSS custom property file or design-token JSON available to confirm its formal brand name or whether it is the only primary-action color
- Hover and focus state ring styles for interactive elements inferred from design conventions, not directly extracted from source CSS
- Mobile navigation drawer open state, animation curve, and backdrop treatment not confirmed from available hints
- Logo treatment not confirmed — whether the Pippa Small wordmark uses Playfair Display or a bespoke lettering file is unknown
- Cart drawer versus dedicated cart page pattern not confirmed; likely a slide-in drawer per Shopify defaults but unverified
- No dark-mode palette detected; site appears to operate light-mode only
- Social icon set, sizing, and hover treatment not captured in extraction
- Product image hover behaviour (second image swap vs. zoom vs. none) not confirmed
- Exact border treatment on text inputs (full border vs. bottom-only hairline) could not be confirmed from extraction
