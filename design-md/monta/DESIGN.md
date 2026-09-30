---
version: alpha
name: "Monta"
source_url: "https://www.montawatch.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The depth-gauge navy #001b32 anchors every load-bearing surface at Monta — navigation panel backgrounds, hero section overlays, footer fields — pulling the entire digital environment toward the pressure-rated instruments the brand produces. Swiss-made at an approachable price tier, yet the site enforces a discipline that never softens into affordability clichés. Futura PT carries the brand's typographic voice across headings, navigation labels, button copy, and spec callouts; its geometric monolinear construction and even stroke weights echo the indexed chapter rings and stamped case backs found on the watches themselves. Museo Sans steps in for longer editorial passages and product descriptions where Futura PT's rigidity would create fatigue over sustained reading.

  The accent red #ab141b appears with precision: limited-edition badges, sale callouts, active navigation underlines, and bezel highlights in product photography. It reads less like a promotional device and more like a countdown marker on a GMT bezel — present only when operationally necessary. The near-black #121212 grounds body copy and dark-surface contexts; the charcoal #3a3a3a serves mid-weight UI elements like inactive navigation states and secondary card backgrounds. Light grays #dedede and #aaaaaa carry hairlines, disabled states, and secondary labels without competing with the primary navy-and-black register.

  Rounding stays deliberately low throughout. Product cards use {rounded.xs} corners that signal precision manufacture rather than soft consumer goods; CTA buttons run at {rounded.none} — hard square shoulders as a brand signature consistent with case shapes that favor sharp lugs and straight-edge crowns. There are no pill forms, no bubble shapes, no radii that evoke sportswear or fashion retail.

  Product pages foreground specification density: lug width, water resistance depth, movement reference, lume compound name, crown tube diameter. This content renders in museo-sans-condensed at tight letter-spacing inside structured two-column tables, reinforcing an engineering-first identity without breaking retail UX flow. Monta's visual restraint — deep navy primary, near-black ground, one controlled red accent, geometric type, square geometry — lets product photography carry warmth and aspiration while the surrounding UI maintains the cool authority of instrument design.

colors:
  primary: "#001b32"
  primary-active: "#002d52"
  primary-disabled: "#4a6b85"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#aaaaaa"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  on-primary: "#ffffff"
  accent-red: "#ab141b"
  accent-red-active: "#8a0f15"

typography:
  display-xl:
    fontFamily: "'futura-pt-bold', 'futura-pt', Futura, 'Trebuchet MS', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.02em
    textTransform: uppercase
  display-md:
    fontFamily: "'futura-pt-bold', 'futura-pt', Futura, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.02em
    textTransform: uppercase
  display-sm:
    fontFamily: "'futura-pt', Futura, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.04em
    textTransform: uppercase
  title-md:
    fontFamily: "'futura-pt', Futura, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.06em
    textTransform: uppercase
  title-sm:
    fontFamily: "'futura-pt', Futura, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "'museo-sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'museo-sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'museo-sans-condensed', 'museo-sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  spec-label:
    fontFamily: "'museo-sans-condensed', 'museo-sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  price-display:
    fontFamily: "'futura-pt-bold', 'futura-pt', Futura, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'futura-pt', Futura, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'futura-pt', Futura, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'futura-pt', Futura, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.on-primary}"
  button-accent:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-red-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "1:1"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
    gap: "{spacing.sm}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,27,50,0.12)"
    rounded: "{rounded.xs}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 640px
    overlayOpacity: 0.45
  collection-tile:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-sm}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4:5"
  badge-limited:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  spec-table:
    backgroundColor: "{colors.canvas}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rowPaddingY: "{spacing.md}"
  watch-detail-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    activeBorderBottom: "2px solid {colors.primary}"
    gap: "{spacing.xl}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    inputBorder: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    mutedTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.section}"

## Components

### Buttons
**`button-primary`** — Flat navy (#001b32) block at zero border-radius, uppercase Futura PT at 14px/600 weight with 0.12em letter-spacing, 48px tall. The hard square corner is a deliberate brand signature — there are no pill or rounded CTAs anywhere on the site. Active state darkens to #002d52; disabled shifts to the muted slate #4a6b85.

**`button-secondary`** — Transparent fill with a 1px solid #001b32 border and matching navy type. Used for secondary actions on light canvas backgrounds. The `button-secondary-dark` variant swaps all values to white-on-transparent for placement over hero imagery or the navy footer.

**`button-accent`** — Identical geometry to `button-primary` but filled with accent-red #ab141b. Reserved for limited-edition launch CTAs, flash-sale actions, and high-urgency purchase prompts. Active state drops to #8a0f15 on press.

### Navigation
**`nav-bar`** — White canvas, 72px tall, hairline bottom border. All links rendered in Futura PT uppercase 13px/500/0.1em tracking. A `nav-bar-dark` variant in #001b32 activates when hero sections scroll out of view on collection and PDP pages. Dropdown panels expand flush below the bar as clean white cards with no shadow treatment. The announcement bar sits above the nav as a 36px near-black strip cycling shipping and promotional copy.

### Product Card
**`product-card`** — White surface with 2px corner radius, 1:1 square image crop, title in uppercase Futura PT 16px, price in futura-pt-bold 20px. Hover lifts with a soft navy-tinted shadow `0 4px 16px rgba(0,27,50,0.12)`. Badge overlays (`badge-limited`, `badge-new`, `badge-sale`) anchor to the top-left of the image frame as flat zero-radius chips — red for urgency states, navy for editorial newness.

### Hero Banner
**`hero-banner`** — Full-bleed image with a 45% dark scrim, minimum 640px tall. Display title renders in uppercase Futura PT Bold at 48px over the overlay; body copy in Museo Sans 300 weight below. CTAs use `button-secondary-dark` style to read clearly against photography. A `collection-tile` variant uses a 4:5 aspect ratio for collection landing grids.

### Spec Table
**`spec-table`** — Two-column layout present on every product detail page. Left column: spec labels in museo-sans-condensed uppercase 11px/700/0.1em tracking, muted gray #aaaaaa. Right column: values in Museo Sans 14px/300, near-black #121212. Rows separated by 1px #dedede hairlines at 12px vertical padding. The density is intentional — Monta buyers read every row, so every label is afforded equal weight.

### Badges
**`badge-limited`** and **`badge-sale`** share flat zero-radius geometry, accent-red #ab141b fill, and white museo-sans-condensed uppercase 11px labels. They appear as corner overlays on product card imagery. **`badge-new`** uses the same chip form in primary navy, deployed sparingly on new reference launches.

### Collection Filter
**`collection-filter`** — Horizontal inline tab strip beneath the collection heading. Each label in Futura PT uppercase 12px/600 with 32px gaps. Active item gains a 2px solid #001b32 bottom border; no fill, no background change, no pill. State is communicated entirely through the underline and color shift.

### Watch Detail Callout
**`watch-detail-callout`** — Soft-gray (#f4f4f4) inset block used for notable feature callouts on PDPs: water resistance credentials, movement provenance, lume specification. Title in uppercase Futura PT 13px; body in museo-sans-condensed caption style. Corners at {rounded.xs}. Provides structural rhythm on long product pages without requiring imagery.

### Footer
**`footer`** — Full-width #001b32 block, white primary text, muted-gray #aaaaaa for secondary labels and fine print. Section headings in uppercase Futura PT 13px/600; body links in Museo Sans 14px/300. Four-column grid on desktop collapses progressively through tablet to single-column on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero min-height 480px; nav collapses to hamburger drawer; spec table scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; hero min-height 560px; primary nav links visible, secondary links in drawer |
| Desktop | 1128–1440px | Three-to-four-column product grid; full nav with dropdown panels; spec table full-width two-column |
| Wide | > 1440px | Content container max-width 1440px centered; hero photography extends edge-to-edge behind contained text column |

### Touch Targets
- All buttons minimum 48px tall
- Collection filter tab items padded to minimum 44px touch target height
- Product card tap area covers full card face including image and text block
- Mobile nav hamburger minimum 44×44px hit area
- Announcement bar dismiss control minimum 44px if present

### Collapsing Strategy
- Navigation collapses to hamburger at < 744px; mega-menu dropdowns become full-height slide-in drawer
- Announcement bar persists at all breakpoints
- Spec table becomes horizontally scrollable below 744px — the two-column label/value format is preserved rather than stacked, because the comparative scan matters
- Footer four-column grid steps to two-column at tablet, single-column with accordion-collapsed sections at mobile
- Collection filter tabs scroll horizontally on mobile if item count exceeds viewport width; no wrapping

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.
- Exact button corner-radius on the live site inferred from visual language; a 2px value may differ from true computed radius
- Mega-menu column layout, column count, and featured-image slots not confirmed
- Product page image gallery interaction (zoom trigger, lightbox type, scroll snap) not observed
- Futura PT weight mapping per element (which weights are licensed and deployed) inferred; live mapping may differ
- Cart behavior — drawer vs. page routing — not confirmed
- Mobile sticky add-to-cart bar presence and behavior not confirmed
- Serif faces detected in font stack (Big Caslon, Cardo, ff-scala) likely used for editorial blog or long-form content; usage context and element mapping unclear
- Icon system style (outline vs. solid, stroke weight, pixel grid) not accessible without live inspection
