---
version: alpha
name: "Linksys"
source_url: "https://www.linksys.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Arimo — Google's metrically compatible Arial substitute — carries all editorial weight on linksys.com, a deliberate choice that prioritizes cross-platform rendering fidelity over typographic personality; it is the font equivalent of the hardware it represents: invisible infrastructure that simply works. A single #0098ed anchors the entire interactive system — every primary CTA, every nav hover underline, every active tab indicator runs through this one cerulean voltage, never doubled or softened into a tint family. Below it sits a tight grayscale stack: #121212 for headings, #323232 for body, #444444 for muted annotations, then #dedede and #f7f7f7 holding hairlines and section backgrounds — six colors total that compose without decoration. The geometry is utilitarian rather than playful: buttons favor `{rounded.xs}` corners, product cards sit on `{rounded.sm}` frames, and the brand's credibility is built through specification grids and compatibility badges rather than illustration or lifestyle photography. CTAs land as solid #0098ed fills with `{colors.on-primary}` type, and secondary actions step back to outlined treatments — a clear hierarchy that mirrors how networking dashboards prioritize primary action paths. Section rhythm divides neatly: hero at full-viewport with a headline in display-xl and support subhead in body-md, followed by product-feature strips that alternate between #121212 and #f7f7f7 panels to create cadence without color variety. The footer is dense charcoal — `{colors.dark-body}` — with legal links at caption scale. There are no gradients, no decorative patterns, no color outside the six extracted values; Linksys's design system reads like a spec sheet rendered in CSS: categorical, complete, and deliberately cold.

colors:
  primary: "#0098ed"
  primary-active: "#007bc4"
  primary-disabled: "#80ccf6"
  ink: "#121212"
  body: "#323232"
  muted: "#444444"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  dark-surface: "#121212"
  dark-body: "#323232"

typography:
  display-xl:
    fontFamily: "Arimo, Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arimo, Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Arimo, Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Arimo, Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arimo, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "Arimo, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arimo, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arimo, Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Arimo, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Arimo, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Arimo, Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Arimo, Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "Arimo, Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    border: "2px solid {colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: 12px 16px
    height: 48px
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    activeColor: "{colors.primary}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.lg}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
    imageBackground: "{colors.surface-soft}"
  product-card-hover:
    borderColor: "{colors.primary}"
    boxShadow: "0 4px 16px rgba(0,152,237,0.15)"
  hero-banner:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
    border: "1px solid {colors.hairline}"
  promo-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    height: 44px
    searchIconColor: "{colors.primary}"
  category-filter:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  feature-strip-dark:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
  feature-strip-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
  footer:
    backgroundColor: "{colors.dark-body}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0 {spacing.xl}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"

## Components

### Buttons

**`button-primary`** — Solid #0098ed fill with white type at 16px/600 weight, `{rounded.xs}` (4px) corners, 48px height. Hover shifts background to `{colors.primary-active}` (#007bc4) with no border-radius change. The singular blue is never tinted or outlined in this state; full fill is the only sanctioned primary treatment.

**`button-secondary`** — White background with a 2px #0098ed border and `{colors.primary}` text; signals secondary priority without stepping down to ghost opacity. Height matches primary at 48px so CTA pairs align. Used on light panels where both actions need clear affordance.

**`button-ghost`** — Transparent background, 2px white border, white type. Deployed exclusively inside dark hero panels where `button-primary` and `button-secondary` would both clash with the `{colors.dark-surface}` backdrop. Hover darkens the background at low opacity.

### Form Controls

**`text-input`** — 1px `{colors.hairline}` border, `{rounded.xs}` radius, 48px height, placeholder in `{colors.muted}` (#444444). Focus swaps the border to `{colors.primary}` with no shadow spread — clean and precise. Validation error states are inferred as red border; no extracted value confirmed.

### Navigation

**`nav-bar`** — 64px tall, `{colors.canvas}` background, 1px `{colors.hairline}` bottom border. Category links at 15px/500 weight with `{colors.primary}` underline or color change on hover. Logo anchors the left edge; cart, account, and search utilities cluster right. On scroll, a soft shadow separates the bar from content.

**`nav-dropdown`** — Full-width mega-menu panel on category hover. White background with a 3px `{colors.primary}` top accent stripe. Internal links at `{typography.body-sm}`, padded at `{spacing.lg}`. `boxShadow` provides elevation over the page below; escaping closes the panel.

### Product Card

**`product-card`** — White surface, 1px `{colors.hairline}` border, `{rounded.sm}` corners. Product image renders on an `{colors.surface-soft}` swatch zone inside the card. Title at `{typography.title-md}`, supporting copy at `{typography.body-sm}`. Hover elevates border to `{colors.primary}` and adds a faint blue shadow (`product-card-hover`). Promo badges overlay the image zone as absolute chips.

### Hero

**`hero-banner`** — Full-bleed `{colors.dark-surface}` (#121212) panel with headline at display-xl (48px/700) and subhead at body-md in white. CTA row holds one `button-primary` and one `button-ghost` side by side. Min-height 480px; collapses to 320px on mobile with stacked vertical CTAs.

**`hero-banner-light`** — Mirrors the dark hero's proportions and type scale on `{colors.surface-soft}` with `{colors.ink}` type. Used for promotional or seasonal modules where the full-black treatment would feel too heavy.

### Badges and Tags

**`spec-badge`** — Small chip on `{colors.surface-soft}`, 1px hairline border, `{typography.spec-label}` (13px/500). Surfaces key product specs on cards and PDP pages: "WiFi 7", "Tri-Band", "4×4 MU-MIMO". Purely informational — no color, no interaction.

**`promo-badge`** — Solid #0098ed chip in 11px/700 all-caps badge typography, `{rounded.xs}`. Applied as an absolute overlay on product card imagery: "NEW", "SALE", "BEST SELLER". The only instance where the primary blue appears in small-scale type.

### Search

**`search-bar`** — 44px height, matches text-input border treatment. Magnifier icon in `{colors.primary}` signals interactivity. Appears in the sticky nav as a collapsed icon that expands inline, and as a full-width bar on the search results page.

### Category Filter

**`category-filter`** — Horizontal chip row for product taxonomy (Routers, Mesh, Switches, Accessories, Security). Inactive chips: `{colors.surface-soft}` background, `{colors.body}` text, `{rounded.full}` radius. Active chip: solid `{colors.primary}`, `{colors.on-primary}` text. Transitions at 150ms ease. Overflows to horizontal scroll on mobile.

### Feature Strips

**`feature-strip-dark`** — Alternating full-bleed section on `{colors.dark-surface}`. Headline at display-sm, body at body-md in white. Used for specification callouts and technical marketing copy. Image floats right or left of copy block.

**`feature-strip-light`** — Same 50/50 layout on `{colors.canvas}` with `{colors.ink}` type. Alternates with the dark variant to build page rhythm without introducing additional colors.

### Footer

**`footer`** — `{colors.dark-body}` (#323232) background, 4-column link grid. Column heads at `{typography.title-sm}` in white (`{colors.on-primary}`), links at `{typography.body-sm}` in `{colors.hairline}` gray. Sub-footer strip holds copyright, legal links, and cookie preferences at `{typography.caption}` scale.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero collapses to 320px min-height with stacked CTAs; nav becomes hamburger drawer; product grid 1 column; category filters horizontal-scroll chips |
| Tablet | 744–1128px | 2-column product grid; nav retains logo and utility icons, hamburger for category links; hero at 400px; feature strips stack image above copy |
| Desktop | 1128–1440px | Full mega-nav with dropdowns; 3–4 column product grid; hero at 480px; feature strips use 50/50 horizontal split |
| Wide | > 1440px | Max-width container (~1280px) centered; hero may scale to 560px; grid adds 5th column for accessories category |

### Touch Targets

- All buttons and nav links minimum 44×44px tap zone
- Category filter chips minimum 36px tall with adequate horizontal padding
- Product card tap zone covers full card surface, including image zone
- Mobile nav drawer items minimum 48px row height
- Footer links minimum 44px vertical tap clearance in mobile accordion

### Collapsing Strategy

- Mega-nav collapses to hamburger at < 1128px; off-canvas drawer slides from left
- Hero CTA pair stacks vertically on mobile; both buttons expand to full width
- Feature strips switch from side-by-side to stacked image-above-copy at < 744px
- Footer 4-column grid collapses to 2 columns at tablet, then accordion single-column at mobile
- Spec badge rows truncate to 3 visible badges with "Show all specs" expand link on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No secondary or accent colors extracted beyond the single brand blue (#0098ed) and grayscale stack; error, success, and warning state colors are not extractable from the available hints and are left unspecified
- Font weights in active deployment are unconfirmed; Arimo supports 400–700 but the specific weight pairings used on linksys.com are not derivable from the meta extraction
- Shadow values and elevation tokens (card shadow, nav scroll shadow) are reasonable defaults — not extracted from the live site
- Animation timing curves and transition durations are absent from the extracted hints
- Icon set (product category glyphs, UI affordance icons) is not identifiable — may be a custom SVG set or a licensed library
- Exact button border-radius in production may differ from the `{rounded.xs}` (4px) estimate; only theme-color and hex palette were available
- Dark-mode support status cannot be determined from the extracted hints
- Any loyalty, rewards, or promotional color tokens (sale red, clearance amber) are not present in the six extracted values
