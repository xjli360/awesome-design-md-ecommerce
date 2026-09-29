---
version: alpha
name: "Passion Planner"
source_url: "https://passionplanner.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The muted rose of #ba6a6a — not coral, not blush, but the tone of dried petals still holding their original color — marks every primary CTA on passionplanner.com and anchors a palette assembled like a physical flat-lay: dark walnut ink at #463a29, amber spills at #f4ad3a, an olive-khaki accent at #959264, and a warm cream canvas at #fbf9f3 that reads like natural cotton rather than bleached white. PPEditorial's high-contrast serifs define the headline register — hairline horizontals against muscular verticals give each section header deliberate editorial weight, distinguishing Passion Planner from the lifestyle-generic scripts common in adjacent journaling brands. AvenirCustom handles everything below 24px: navigation labels, button copy, filter toggles, form fields, the geometric letters carrying the planning-oriented clarity the audience expects. Cabin and Lato fill the fallback chain, sharing enough proportion with Avenir that a stack swap goes unnoticed. Corner radii stay measured: `{rounded.sm}` on inputs and buttons, `{rounded.md}` on product cards — personal without veering juvenile. At 48px tall, buttons carry deliberate authority, the click feeling like committing to a plan rather than a casual tap. Amber (#f4ad3a) functions as the brand's urgency signal: announcement bars, limited-run tags, seasonal collection callouts. Olive-khaki (#959264) settles into muted secondary labels and footer navigation, bridging the brown-ink world and the cream canvas without landing on any single seasonal hue. Product cards devote a horizontal swatch row to colorway selection — a dozen covers at any given time — without crowding the tile, because choosing the right cover is part of the purchase ritual for a Passion Planner customer. Hairlines at #dedede read as connective tissue between sections rather than hard separators, consistent with a brand whose thesis is that visible structure enables personal flow.

colors:
  primary: "#ba6a6a"
  primary-active: "#9a4a4a"
  primary-disabled: "#ddb8b8"
  ink: "#463a29"
  body: "#5c4a36"
  muted: "#959264"
  hairline: "#dedede"
  canvas: "#fbf9f3"
  surface-soft: "#f4f6f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  amber: "#f4ad3a"
  amber-soft: "#fef8e2"
  olive: "#959264"
  error: "#d72c0d"
  sale: "#f9423a"
  near-black: "#121212"

typography:
  display-xl:
    fontFamily: "'PPEditorial', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'PPEditorial', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'PPEditorial', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  editorial-quote:
    fontFamily: "'PPEditorial', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    fontStyle: italic
  title-md:
    fontFamily: "'AvenirCustom', 'Cabin', 'Lato', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'AvenirCustom', 'Cabin', 'Lato', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Cabin', 'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Cabin', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'AvenirCustom', 'Cabin', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  price:
    fontFamily: "'AvenirCustom', 'Cabin', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'AvenirCustom', 'Cabin', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.6px
    textTransform: uppercase
  label:
    fontFamily: "'AvenirCustom', 'Cabin', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'AvenirCustom', 'Cabin', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'AvenirCustom', 'Cabin', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'AvenirCustom', 'Cabin', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.4px

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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.near-black}"
    typography: "{typography.caption}"
    height: 40px
    padding: "0 {spacing.base}"
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    imageRounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    textColor: "{colors.ink}"
    shadow: "0 2px 8px rgba(70, 58, 41, 0.08)"
    padding: "{spacing.md}"
    swatchRowGap: 6px
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.ink}"
    gap: 6px
  planner-type-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  collection-filter-pill:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    selectedBackgroundColor: "{colors.ink}"
    selectedTextColor: "{colors.canvas}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    minHeight: 560px
    padding: "{spacing.section}"
  testimonial-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    bodyTypography: "{typography.editorial-quote}"
    textColor: "{colors.ink}"
    padding: "{spacing.xl}"
  email-signup:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    inputBackgroundColor: "{colors.canvas}"
    inputTypography: "{typography.body-md}"
    buttonTypography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    labelTypography: "{typography.label}"
    padding: "{spacing.section}"
    columns: 4

## Components

### Buttons

**`button-primary`** — The rose-ground primary (#ba6a6a) with white text and `{rounded.sm}` corners sits at 48px tall with generous 28px horizontal padding; on hover it deepens to `{colors.primary-active}` (#9a4a4a) with no scale transform, keeping the interaction feeling deliberate. The `button-primary-disabled` state lightens to `{colors.primary-disabled}` (#ddb8b8), maintaining legibility without harsh contrast loss. Letter-spacing at 0.5px in AvenirCustom 600 gives the label a slightly spaced, composed feel without going full uppercase.

**`button-secondary`** — Transparent fill with a 1.5px rose border and rose text; identical 48px height to primary allows side-by-side CTA pairing (e.g., "Add to Cart" / "View Details") without visual hierarchy collapse. Hover inverts to rose fill with white text.

**`button-ghost`** — Ink-colored text on transparent with no border, used for tertiary actions like "View all" and in-page text navigation. Carries the same AvenirCustom 600 weight as the other buttons to maintain type consistency across the action register.

### Navigation

**`nav-bar`** — Cream canvas bar at 64px with a hairline bottom border; top-level links in AvenirCustom 500 14px. The amber `{colors.amber}` announcement bar sits above at 40px, making the combined masthead 104px at desktop — plan hero images to account for this fixed offset. Cart and account icons align right with 44px tap targets.

**`announcement-bar`** — Amber (#f4ad3a) ground with near-black (#121212) caption text; used for free-shipping thresholds, seasonal promotions, and new collection drops. The amber-on-walnut combination elsewhere on the page ties announcements to the brand's urgency color rather than a generic red.

### Cards

**`product-card`** — White surface tile with `{rounded.md}` corners and a subtle walnut-tinted drop shadow; the title runs `{typography.title-md}` (AvenirCustom 600 18px) and the price runs `{typography.price}` (AvenirCustom 700 16px). A horizontal swatch row of up to 8 `color-swatch` circles sits below the title; selecting a swatch swaps the product image. `planner-type-badge` labels (Weekly, Daily, Undated) float top-left on the image.

**`testimonial-card`** — Cream canvas with `{rounded.md}` and a hairline border; the quote text runs PPEditorial italic at 22px (`{typography.editorial-quote}`), giving customer voice the same editorial register as the site's section headlines. Attribution sits below in `{typography.caption}` olive-khaki.

### Filters and Taxonomy

**`collection-filter-pill`** — Hairline-bordered pill with `{rounded.full}` at rest; on selection, fills with `{colors.ink}` (#463a29) and inverts text to `{colors.canvas}`. Used for format filters (Weekly, Daily, Undated), size filters (Letter, A5, Pocket), and year filters. The walnut fill on selection echoes the brand's brown-grounded identity rather than defaulting to a generic dark chip.

**`planner-type-badge`** — Olive-khaki text on surface-soft in tight `{rounded.xs}` corners; communicates product format at a glance on listing tiles without competing with the rose CTA below. Sits flush to the image corner, not floated inside it.

**`color-swatch`** — 20px circles in `{rounded.full}`; the selected state gains a 2px walnut-ink ring with a 2px white gap between ring and swatch, making selection visible across all colorways including dark covers. Expands to 28px on mobile for comfortable tap precision.

### Forms

**`text-input`** — Cream-canvas field with hairline border at rest, rose border at focus; 48px tall to match button height for clean row alignment in subscription and checkout flows. Placeholder text in olive-khaki (`{colors.muted}`) rather than generic gray keeps the form within the brand's warm color range.

**`email-signup`** — Rose-ground section with a cream input inset; the subscribe button inherits the rose fill matching the section background, differentiated by its slightly darker hover state and white label. Used on the homepage and as a footer-adjacent block. Generous `{spacing.xxl}` padding keeps the block from feeling cramped against surrounding content.

### Layout

**`hero-banner`** — Warm surface-soft ground at minimum 560px height; PPEditorial display-xl headlines (48px, weight 400) drop in at desktop scale, giving the hero a magazine-spread feeling. Body copy in Cabin 16px sits beneath with 1.6 line-height for relaxed reading. A product flat-lay or lifestyle image typically bleeds to the right column in a 50/50 split at desktop.

**`footer`** — Full-width walnut-brown (`{colors.ink}`) ground with cream text organized in four columns at desktop; column headers use `{typography.label}` (AvenirCustom 600 uppercase 12px) and links use `{typography.body-sm}` with no underline at rest, underline on hover. The dark footer creates a strong visual close after the cream-dominant page body.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; announcement bar wraps to two lines (auto height); nav collapses to hamburger icon; swatch row gains horizontal scroll; footer collapses to accordion sections |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links with secondary in mega-dropdown; hero headline scales to `display-md` (36px); testimonial carousel shows one card with peek |
| Desktop | 1128–1440px | Three-column product grid; full nav bar; hero at `display-xl` (48px); testimonials show two cards; collection filters in a sticky left rail |
| Wide | > 1440px | Four-column product grid; content maxes at 1440px with `{colors.canvas}` gutters; hero image bleeds full width behind a centered text column |

### Touch Targets

- All buttons, swatches, and filter pills meet 44×44px minimum tap target
- Color swatches expand from 20px to 28px on mobile for finger-precision picking
- Mobile nav links stack to 48px tall for thumb-accessible tap zones
- Announcement bar close button (if present) sits at 44×44px regardless of visible icon size

### Collapsing Strategy

- Footer four-column layout collapses to single-column accordion on mobile; walnut background and cream text persist across all breakpoints
- Product card swatch row scrolls horizontally on mobile (overflow-x: auto, no wrap) rather than wrapping to a second line that would inflate card height unpredictably
- Hero headline scales from `display-xl` (48px) at desktop to `display-sm` (28px) at mobile to avoid oversized PPEditorial text overwhelming narrow viewports
- Collection filter pills move from a sticky left sidebar at desktop to a horizontal scroll strip pinned below the nav on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No `meta theme-color` was extracted; browser chrome color on mobile Safari is unconfirmed and will default to system chrome
- Shopify admin interface colors (#008060, #35ee7a) appear in the extraction pool and are explicitly excluded from the brand palette
- System UI blues (#007aff, #049cff) are likely sourced from iOS form controls or Shopify-embedded components rather than brand design decisions; excluded
- AvenirCustom is a JavaScript-loaded custom font; exact available weight range and optical sizes could not be confirmed from static extraction
- PPEditorial italic weight availability is unconfirmed; `fontStyle: italic` in `editorial-quote` may fall back to browser-synthesized italic if only the roman weight is served
- Hover transition timing and easing curves for buttons, swatches, and filter pills require live browser inspection to confirm exact values
- Mobile navigation drawer treatment (slide-in panel, full-screen overlay, or drop-down) could not be determined from static extraction
- Exact product card shadow values are estimated from walnut ink base; live computed styles required for pixel-accurate specification
- Whether #f1e04d (yellow) and #d72c0d (red-orange) are brand colors or Shopify sale/badge system colors is ambiguous from extraction alone
