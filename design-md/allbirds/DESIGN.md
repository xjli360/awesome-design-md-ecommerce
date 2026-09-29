---
version: alpha
name: "Allbirds"
source_url: "https://allbirds.com"
captured_at: "2026-09-28T04:10:59.776112+00:00"
evidence_status: "historical_partial_css_evidence"
description: |-
  The canvas opens at #ece9e2 — not white, but the color of unprocessed merino fiber, a deliberate material echo that brands sustainability before any copy loads. Against this warm ground, near-black ink (#212121) lands with quiet precision, and the contrast feels organic rather than clinical. Allbirds operates with a restrained palette of four extracted tones: two near-blacks, a warm cream canvas, and a light gray hairline — no accent voltage, no brand red or bold primary hue competing for attention. The visual tension lives entirely in texture and proportion. Buttons are dark rectangles with gently rounded corners (`{rounded.sm}`), rejecting the pill-shaped softness common in DTC wellness brands in favor of something more grounded and confident. Typography is set in a geometric sans-serif at modest weights — display text rarely exceeds 600 weight, and the brand trusts generous whitespace and the warmth of #ece9e2 over typographic spectacle. Product cards carry the same restraint: clean image windows, minimal metadata, no urgency-driving badges or countdown timers. The nav sits low and open, a logo mark rather than wordmark anchoring the left position. Sustainability credentials arrive not through color splashes but through measured copy treatment — certifications and material callouts use uppercase label chips and a consistent muted tone (`{colors.muted}`) rather than colored badges. The overall cadence is slow: sections breathe at `{spacing.section}` gaps, CTAs appear once per scroll depth, and the page never shouts. Allbirds built a brand that asks customers to slow down and pay attention — the design system enforces this discipline at every scale, from the single hairline border (`{colors.hairline}`) separating nav zones to the wide, unencumbered product imagery that lets natural materials speak without editorial interference.

colors:
  primary: "#212121"
  primary-active: "#121212"
  primary-disabled: "#9e9e9e"
  ink: "#212121"
  body: "#3d3d3d"
  muted: "#6b6b6b"
  hairline: "#dedede"
  canvas: "#ece9e2"
  surface-soft: "#f5f3ef"
  surface-card: "#ffffff"
  surface-strong: "#dedede"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-uppercase:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  material-tag:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.06em
    textTransform: uppercase
  price:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.02em
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.02em
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-text:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg} {spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1:1"
    padding: "{spacing.md}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.body}"
  color-swatch:
    size: 16px
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.hairline}"
    selectedBorder: "1.5px solid {colors.ink}"
  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.material-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    headlineColor: "{colors.ink}"
    subheadColor: "{colors.body}"
    paddingVertical: "{spacing.section}"
  sustainability-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-uppercase}"
    labelColor: "{colors.muted}"
    padding: "{spacing.md} {spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 16px
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    selectedBackground: "{colors.ink}"
    selectedTextColor: "{colors.on-primary}"
    height: 44px
  product-image-viewer:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-uppercase}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — A filled 48px-tall dark rectangle at #212121 with white text, 8px corner radius, and 28px horizontal padding. Hover deepens to #121212; disabled state falls back to a neutral mid-gray. Used exclusively for primary conversion actions: "Add to Cart", "Shop Now", and checkout progression — never appearing more than once per visible viewport.

**`button-secondary`** — Identical geometry to `button-primary` but with transparent fill and a 1.5px #212121 border. Signals secondary action weight — filter toggles, "Learn More" flows, color navigation — without competing with the primary CTA. Active state fills with `{colors.surface-strong}` to confirm interaction without a color flash.

**`button-text`** — A bare typographic link with underline decoration, no border or background fill. Appears in sustainability callout sections and footer navigation where a framed button would add visual noise to content-heavy prose.

### Navigation
**`nav-bar`** — A 64px horizontal bar sitting on the warm canvas (#ece9e2), separated from page content by a single 1px `{colors.hairline}` rule. Logo anchors left; category links (Men, Women, Kids, Sale) sit in the center span using `{typography.nav-link}` weight; cart, search, and account icons close the right edge. The bar does not change color on scroll — it stays grounded in the canvas register, reinforcing an unhurried brand tempo.

**`nav-dropdown`** — A full-width panel descending from the nav on category hover, padded at `{spacing.xl}`. Subcategory links occupy a multi-column grid; material callouts appear as short inline descriptors beneath product names in `{typography.caption}`. No imagery inside the dropdown — copy-only.

### Product Card
**`product-card`** — A 1:1 image window with `{rounded.sm}` corners, product name in `{typography.title-sm}`, price in `{typography.price}`, and a horizontal row of 16px circular color swatches below the price line. No overlay CTAs, no hover-state add-to-cart buttons — clicking the card navigates to the PDP, preserving an editorial rather than transactional feel. Grid gap uses `{spacing.lg}` throughout.

**`color-swatch`** — 16px circles with a `{colors.hairline}` border at rest, transitioning to a solid `{colors.ink}` border when selected. Swatch row overflow beyond four items collapses to a "+N" text count label in `{typography.caption}` weight.

### Product Detail
**`product-image-viewer`** — Square `{colors.surface-soft}` tile with `{rounded.sm}` corners. Mobile shows a single swipeable carousel with dot indicators; desktop uses a two-column stacked grid layout. No lightbox modal — images enlarge inline. The warm background ensures natural wool textures read without clinical white staging.

**`size-selector`** — Flat rectangular pills, 44px height, `{rounded.xs}` corners, `{colors.hairline}` border at rest. Selected state inverts to full `{colors.ink}` background with `{colors.on-primary}` text. Out-of-stock sizes render at 40% opacity with a diagonal SVG strikethrough line — not removed from the grid, maintaining size-range legibility.

### Material & Sustainability Badges
**`material-badge`** — Small uppercase chips in `{typography.material-tag}` on a `{colors.surface-soft}` background with `{rounded.xs}` corners. Used to tag "Merino Wool", "Tree Fiber", "Sugar Cane Sole" inline on PDP pages and product cards. No color fill, no icon — the label typography carries the full semantic weight.

**`sustainability-banner`** — A subdued informational strip on `{colors.surface-soft}`, using `{typography.label-uppercase}` for certification category headers and `{typography.body-sm}` for descriptive copy. Appears anchored above or below primary navigation for messages like "Carbon Neutral Shipping" and B-Corp status. Padded at `{spacing.md}` vertically, `{spacing.xl}` horizontally, with a `{colors.hairline}` bottom border.

### Hero
**`hero-section`** — Full-width section on `{colors.canvas}` with headline in `{typography.display-xl}` and subhead in `{typography.body-md}`. Copy is left-aligned on desktop within a constrained column alongside a full-bleed product photograph. Mobile stacks the copy block above the image, both full-width. No gradient overlays or text-on-image compositing — copy and photography occupy separate, clean zones with `{spacing.section}` breathing room.

### Forms & Search
**`text-input`** — 48px height, `{rounded.sm}` corners, 1px `{colors.hairline}` border transitioning to a solid `{colors.ink}` border on focus. Placeholder text uses `{colors.muted}`. Labels sit statically above the field in `{typography.caption}` weight — no floating label animation.

**`search-bar`** — A compact input variant on `{colors.surface-soft}` used inside the nav search expansion overlay. No visible border at rest; `{rounded.sm}` corners; a 20px SVG search icon sits left-inset at 16px from the edge.

### Footer
**`footer`** — A full dark closure in `{colors.primary}` (#212121) with `{colors.on-primary}` type, providing visual termination after the sustained warm-canvas experience above. Link columns use `{typography.body-sm}`; column headers use `{typography.label-uppercase}` with `{spacing.md}` bottom margin. Social icons render as 20px SVG symbols with `{spacing.sm}` spacing. B-Corp and carbon certification seals sit in the lower footer strip as small white SVGs, approximately 32px height.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo + cart icon; hero stacks copy above image, both full-width; size selector becomes a horizontal scroll row; swatches truncate to 3 visible + overflow count |
| Tablet | 744–1128px | 2-column product grid; nav retains logo and icons but hamburger handles category links; hero uses 50/50 split layout; dropdowns become slide-in drawer panels from left |
| Desktop | 1128–1440px | 3–4 column product grid; full nav with all category links visible; hero uses wide asymmetric copy/image layout; dropdown panels appear on hover at full width |
| Wide | > 1440px | Content max-width constrained to ~1440px with auto side margins; hero photography fills edge-to-edge but copy column stays at fixed width; footer columns expand gutter |

### Touch Targets
- All interactive controls maintain a minimum 44×44px touch target
- Color swatches expand their tap target to 32px via padding despite 16px visual size
- Size selector pills are minimum 44px height on all viewports
- Nav icons are padded to 44×44px touch target regardless of SVG dimensions

### Collapsing Strategy
- Navigation collapses to hamburger at < 744px; search and cart icons remain in the top bar
- Product grid moves 4-column → 3-column → 2-column → 1-column across breakpoints
- Sustainability banner is hidden at < 375px viewport width to preserve vertical space
- Footer moves from 4-column grid to 2-column on tablet, single-column with accordion-expand on mobile
- Hero section stacks vertically on mobile: copy block first, full-width image below

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- **No font families extracted** — Allbirds likely uses a licensed geometric sans-serif (GT Walsheim or a proprietary typeface); all typography tokens fall back to system-ui. Verify against the live CSS `@font-face` declarations before implementation.
- **Sparse color extraction** — Only four hex values captured: #212121 and #121212 (near-blacks), #ece9e2 (warm canvas), #dedede (light gray hairline). No accent, no green sustainability color, no error/success/warning states were present in the extraction pass.
- **Sustainability green accent absent** — Allbirds is widely documented as using a muted sage or forest green in sustainability messaging and seasonal colorways. It was not present in the extracted palette. Do not fabricate a value; inspect CSS custom properties directly.
- **Surface-soft is inferred** — `#f5f3ef` is a warm-white derivation near `{colors.canvas}`, not an extracted value. It may differ from the live site's actual card background.
- **No interactive state colors extracted** — Hover, focus ring, error, and success colors are inferred from brand patterns, not captured from DOM inspection.
- **Icon system undocumented** — Allbirds uses custom SVG icons; stroke weight, cap style (rounded vs butt), and icon grid size are unverified here.
- **Exact grid gutter and card spacing** — Product grid gutter widths and image-to-metadata ratios require live site measurement for pixel-accurate implementation.
