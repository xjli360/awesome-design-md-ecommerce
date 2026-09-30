---
version: alpha
name: "Nodus"
source_url: "https://www.noduswatches.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Purple at the helm of a watch micro-brand's digital identity is a rare sight — most independents reach for navy or anthracite, but Nodus grounds its entire interactive layer in a deep violet (#331177) that reads as technical authority rather than luxury signaling. The near-black palette stacks — #111111 for type anchors, #1e1e1e and #272727 for layered surfaces — creates a cockpit-dark environment where watch photography sits without competing gradients or lifestyle noise. Red breaks the dark field sparingly: #cc3b3b for alerts and hover states, #bd0000 for deeper active presses, #e99292 as a desaturated blush for softer states. The positioning phrase Watch Research and Design embedded in the page title is a deliberate editorial posture — this is not a retailer but a studio in the tradition of small independent makers who publish technical rationale for every decision, from lug-to-lug width to lume application methodology. Typography runs on a system-sans stack (Helvetica Neue → Arial) without brand-custom webfonts, keeping perceived load near-instant and signaling that the work speaks through product photography and specification copy rather than typographic gesture. Component radii stay minimal — corners sit at 0–4px — reinforcing the precision-instrument aesthetic rather than consumer softness. The secondary deep navy (#112244) anchors hero backgrounds and editorial panels, creating a celestial-dark impression that pairs with watch photography shot against gradient backdrops. Spacing is generous at desktop and contracts sensibly on mobile, with product cards inheriting the dark canvas and letting dial photography carry the visual weight. The overall register is enthusiast-first: technically literate, photographically driven, and deliberately spare with decorative treatment.

colors:
  primary: "#331177"
  primary-active: "#22006e"
  primary-hover: "#4422aa"
  primary-disabled: "#7755aa"
  accent: "#cc3b3b"
  accent-active: "#bd0000"
  accent-soft: "#e99292"
  navy: "#112244"
  ink: "#111111"
  body: "#272727"
  muted: "#aaaaaa"
  hairline: "#e1e1e1"
  hairline-soft: "#eeeeee"
  canvas: "#fafafa"
  surface-soft: "#eeeeee"
  surface-card: "#fbfbfb"
  surface-dark: "#1e1e1e"
  surface-deeper: "#040404"
  on-primary: "#fafafa"
  on-dark: "#fafafa"

typography:
  display-xl:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.1px
  title-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  body-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.15px
  spec-label:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  overline:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price-display:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.1px

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
    height: 44px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.ink}"
  button-secondary-on-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.on-dark}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
    focusBorder: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-deeper}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.surface-dark}"
    logoColor: "{colors.on-dark}"
  announcement-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    padding: 0 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "4:3"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    metaTypography: "{typography.body-sm}"
    metaColor: "{colors.muted}"
    shadow: "0 1px 4px rgba(0,0,0,0.07)"
    hoverShadow: "0 6px 20px rgba(0,0,0,0.13)"
    padding: 16px
  product-card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    metaTypography: "{typography.body-sm}"
    metaColor: "{colors.muted}"
    padding: 16px
  hero-banner:
    backgroundColor: "{colors.surface-deeper}"
    textColor: "{colors.on-dark}"
    overlineTypography: "{typography.overline}"
    overlineColor: "{colors.primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    minHeight: 600px
    padding: 80px 48px
  spec-table:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    rowPadding: 8px 16px
    dividerColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"
  watch-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  watch-badge-limited:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  watch-badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 7px 14px
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  editorial-panel:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    overlineTypography: "{typography.overline}"
    overlineColor: "{colors.primary}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: 64px 48px
  footer:
    backgroundColor: "{colors.surface-deeper}"
    textColor: "{colors.on-dark}"
    bodyTypography: "{typography.body-sm}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    borderTop: "1px solid {colors.surface-dark}"
    padding: 48px 0

## Components

### Buttons

**`button-primary`** — Deep violet (#331177) fill with white text rendered in `{typography.button-md}` (uppercase, 1px letter-spacing), 44px tall, 4px radius (`{rounded.xs}`). Hover steps the fill to `{colors.primary-hover}` (#4422aa); active press drops to `{colors.primary-active}` (#22006e); disabled uses `{colors.primary-disabled}` at 60% opacity. The uppercase tracking and tight square corner deliver an instrument-panel register distinctly unlike consumer CTA buttons.

**`button-secondary`** — Transparent background with 1px solid ink border and ink text at the same `{typography.button-md}` scale and 44px height. On dark-surface contexts, `button-secondary-on-dark` swaps all ink tokens for `{colors.on-dark}` white; the border follows. Hover softens the border to `{colors.muted}` grey.

**`button-ghost`** — Zero padding, no border or background, violet text in `{typography.button-md}`. Used inline for section-level navigation such as "View all" or "Learn more" text links.

### Navigation

**`nav-bar`** — Sits on `{colors.surface-deeper}` (#040404), 60px tall, with logo wordmark and nav links in `{colors.on-dark}` white at `{typography.nav-link}`. A 1px `{colors.surface-dark}` border separates it from page content below. Cart count, search, and account are icon-only at right. On mobile the link set collapses to a hamburger; cart and search icons remain visible in the fixed bar. The `announcement-bar` above runs `{colors.navy}` with `{typography.caption}` copy for shipping thresholds or launch notices.

### Product Cards

**`product-card`** — Light `{colors.surface-card}` background with a 1px shadow that deepens to 6px on hover, signaling interactivity without animation cost. Title at `{typography.title-md}`, price at `{typography.price-display}`, watch reference or case material note at `{typography.body-sm}` in `{colors.muted}`. Radius is `{rounded.xs}` (4px). On dark collection grids, `product-card-dark` uses `{colors.surface-dark}` with all text tokens on the white scale — presenting each dial as an artifact under gallery conditions. Badges (`watch-badge`, `watch-badge-limited`) overlay the top-left corner of the card image.

### Watch Badges

**`watch-badge`** — Small rectangular chip in `{colors.primary}` carrying `{typography.overline}` text (10px, 1.8px tracked, uppercase). Used for "New", "In Stock", or collection labels. `watch-badge-limited` uses `{colors.accent}` (#cc3b3b) to signal limited-run or pre-order urgency — the red reads as an alert against both dark and light card surfaces. `watch-badge-sold-out` desaturates to `{colors.muted}` grey, visually deprioritizing unavailable pieces without removing them from the grid.

### Hero Banner

**`hero-banner`** — Full-bleed `{colors.surface-deeper}` (#040404) with an overline label in `{colors.primary}` above a `{typography.display-xl}` headline and a short `{typography.body-md}` subhead. Photography composites directly into the dark ground with no card border or overlay scrim — the dial simply emerges from the black. CTA is `button-primary` left-aligned on desktop; centered on mobile. Minimum height 600px to give dial imagery room to breathe.

### Spec Table

**`spec-table`** — Two-column definition list on `{colors.canvas}` with no outer decoration. Left column carries `{typography.spec-label}` (uppercase, tracked, 10px) in `{colors.muted}`; right column carries `{typography.body-sm}` in `{colors.ink}`. Rows separated by a `{colors.hairline-soft}` 1px rule at 8px/16px padding. This is one of the most read-dense patterns on the site — case diameter, lug width, movement caliber, water resistance, and lume type are compared without decoration, addressed to enthusiasts who know what they are looking for.

### Collection Filter

**`collection-filter`** — Rectangular chips with `{rounded.xs}` corners and a 1px `{colors.hairline}` border in rest state. Active chip inverts to `{colors.primary}` fill with white text and the border disappears. Typography is `{typography.button-sm}`. Filters cover series name, dial color, and case finish. On mobile the strip scrolls horizontally without wrapping.

### Editorial Panel

**`editorial-panel`** — Deep navy (#112244) section used for brand story, movement deep-dives, or research editorial. Overline in `{colors.primary}` above a `{typography.display-md}` heading and `{typography.body-md}` body copy in `{colors.on-dark}`. 64px vertical padding. The navy reads as a distinct mid-layer between the near-black hero and the lighter product grid surfaces.

### Footer

**`footer`** — Mirrors the nav's `{colors.surface-deeper}` ground with a 1px `{colors.surface-dark}` top border. Link columns use `{typography.body-sm}` at `{colors.muted}` and step to full white on hover. Column headings in `{typography.title-sm}` (uppercase, tracked). Social icons are monochrome SVG, icon-only at 20px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark; hero stacks headline above image; spec table runs full-width single column; collection filter becomes horizontal scroll strip; footer columns collapse to accordion |
| Tablet | 744–1128px | 2-column product grid; nav shows primary links inline; hero switches to side-by-side layout; editorial panel reflows to 60/40 split |
| Desktop | 1128–1440px | 3–4 column collection grid; full nav bar with all links and utility icons at right; hero uses full `display-xl` type; spec table floats beside product photography |
| Wide | > 1440px | Max content width ~1400px centered; hero padding expands; collection grid holds at 4 columns; side margins grow with whitespace rather than stretching the grid |

### Touch Targets

- All nav links, hamburger, cart, and search icons: minimum 44×44px
- Product card tap area covers full card surface, not just the title
- Collection filter chips: minimum 44px height
- Spec table rows are read-only; no tap-target requirement
- Watch badges are display-only overlays; no interactive target needed

### Collapsing Strategy

- Navigation collapses to hamburger at < 744px; cart and search remain pinned in the header bar
- Collection filters collapse from wrapped row to horizontal scroll strip on mobile; no truncation or dropdown
- Hero image moves to a stacked position below headline text on mobile; a dark background color provides legibility without a separate scrim layer
- Editorial panels reflow from side-by-side to stacked text-above-image
- Spec tables maintain full column width on mobile; no horizontal scroll — all rows display full-width
- Footer link columns collapse to tap-to-expand accordion groups on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom webfont detected — Nodus may load a brand typeface via JavaScript or a CDN not captured in static extraction; this spec uses the system-sans fallback (Helvetica Neue → Helvetica → Arial) throughout
- `primary-hover` (#4422aa) and `primary-active` (#22006e) are interpolated from the extracted primary #331177 — not directly observed in site CSS
- The site does not use Shopify; cart, checkout, and account page UI patterns were not captured in this extraction pass
- Dark-mode vs. light-mode split is ambiguous — both near-black and near-white surfaces appear in the extracted palette, suggesting mixed-surface section design rather than a toggled dark mode
- No icon system metadata extracted — watch brands commonly use custom SVG icon sets for water resistance ratings, movement type, power reserve, and complication indicators
- Animation timing (hover transitions, image fade-ins, scroll reveals) not captured in static extraction
- Typeface weights available in the system-sans stack may vary by OS; bold weight rendering will differ between macOS (Helvetica Neue) and Windows (Arial)
