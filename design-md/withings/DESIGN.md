---
version: alpha
name: "Withings"
source_url: "https://www.withings.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Withings stakes its identity on a single cobalt, #003399, that reads equally at home on a lifestyle e-commerce page and a clinical dashboard — a deliberate blurring of the boundary between consumer watch brand and medical instrument maker. The hybrid smartwatch sits at the center of this proposition: domed mineral glass over steel hands, yet a hidden optical sensor logging VO2 max and atrial fibrillation events. The extracted palette tells that health data story in color: five shades of red — from deep crimson #7f1d1d through alarm-level #dc2626 and the flat-UI #e74c3c — form an implied severity ladder for out-of-range metric alerts, while a lavender #8672c1 and dusky rose #df6389 quietly mark a feminine product line without ever becoming decorative. Amber #ffb75d bridges sport and wellness, surfacing on activity rings and caloric-burn indicators. Aeonik carries the entire typographic load: a geometric sans-serif with the measured precision of French engineering, set at light-to-medium weights so display copy never shouts — 48–64px headings land at fontWeight 400 or 500, trusting negative space and cobalt to carry authority rather than typographic mass. Layouts default to an off-white #fafafa canvas, card surfaces step up to pure white, and sections divide by generous vertical spacing rather than ruled lines. Buttons are subtly rounded at `{rounded.sm}` (8px), closer to a clinical instrument interface than a playful consumer app. The overall vocabulary is European medtech restrained by fashion sense: no decorative illustration, no gradient, just precise data typography, a watch face on white, and a cobalt that means it.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#99b3e6"
  ink: "#0f0f0f"
  body: "#1a1a1a"
  muted: "#c9c9c9"
  hairline: "#ddd9d6"
  canvas: "#fafafa"
  surface-soft: "#f0efee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  health-alert: "#dc2626"
  health-alert-dark: "#b91c1c"
  health-critical: "#7f1d1d"
  health-rose: "#f43f5e"
  health-rose-light: "#fb7185"
  accent-purple: "#8672c1"
  accent-rose: "#df6389"
  accent-amber: "#ffb75d"
  accent-amber-dark: "#d77700"
  blue-mid: "#289ff0"
  blue-light: "#49b0f5"

typography:
  display-xl:
    fontFamily: "'Aeonik', Arial, Helvetica, sans-serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'Aeonik', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.96px
  display-md:
    fontFamily: "'Aeonik', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Aeonik', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'Aeonik', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Aeonik', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Aeonik', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Aeonik', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Aeonik', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-sm:
    fontFamily: "'Aeonik', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Aeonik', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Aeonik', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  metric-display:
    fontFamily: "'Aeonik', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.0
    letterSpacing: -1px
  nav-link:
    fontFamily: "'Aeonik', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "'Aeonik', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
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
    logoHeight: 28px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    imageAspectRatio: "1:1"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    shadow: "0 2px 12px rgba(0,0,0,0.06)"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 640px
    imagePosition: right
    padding: "{spacing.section} 0"
  metric-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    metricTypography: "{typography.metric-display}"
    labelTypography: "{typography.label-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  metric-alert-badge:
    backgroundColor: "{colors.health-alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  health-severity-dot:
    size: 8px
    colorSafe: "#22c55e"
    colorWarning: "{colors.accent-amber}"
    colorCritical: "{colors.health-alert}"
    rounded: "{rounded.full}"
  category-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "8px 16px"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: none
  product-spec-row:
    backgroundColor: transparent
    textColor: "{colors.body}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "12px 0"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.hairline}"
    activeBorder: "2px solid {colors.primary}"
  comparison-table:
    backgroundColor: "{colors.surface-card}"
    headerBackgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    checkColor: "{colors.primary}"
    crossColor: "{colors.muted}"
  sticky-add-to-cart:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-sm}"
    padding: "{spacing.section} 0"

## Components

### Buttons
**`button-primary`** — Cobalt #003399 fill at 48px height with `{rounded.sm}` (8px) rounding and 14px/28px padding. Aeonik weight-500 at 16px. On hover/active the fill deepens to `{colors.primary-active}` (#002277); disabled state washes to `{colors.primary-disabled}`, a pale cobalt that still reads as the brand color. Primary CTAs include "Add to cart", "Discover", and "Shop now".

**`button-secondary`** — White surface with a 1.5px cobalt border at matching height and rounding. Used wherever a secondary action must be present without competing with the primary — common in product configurators and comparison prompts where purchase leads and detail follows.

**`button-ghost`** — Transparent background with `{colors.ink}` text, no border. Reserved for navigation dropdowns and inline editorial CTAs where the surrounding container provides sufficient visual framing.

### Text Input
**`text-input`** — White background with a 1px `{colors.hairline}` border at rest, upgrading to a 1px cobalt ring on focus. At 48px height it aligns flush with button rows in search and newsletter forms. Placeholder text runs in `{colors.muted}` gray.

### Navigation
**`nav-bar`** — 64px tall on `{colors.canvas}`, separated from page content by a hairline bottom border. Aeonik weight-400 at 15px for nav links — deliberately lighter than the CTA buttons so the header stays recessive against hero content below. Logo sits at 28px height. On scroll, a diffuse box-shadow replaces the static hairline, lifting the bar above page content without a heavy background shift.

### Product Card
**`product-card`** — White card at `{rounded.md}` (12px) with a 2px/12px diffuse shadow — borderless, surface-only containment that reads as clean medtech rather than retail. Image occupies a square 1:1 crop at the top; below it, Aeonik title-md, an uppercase `{typography.label-sm}` category tag, and a `{typography.price}` line. On hover, shadow deepens and the image scales to ~1.02 with a 200ms ease.

### Hero
**`hero`** — Full-width off-white `{colors.canvas}` section, minimum 640px tall. Headline at `{typography.display-xl}` (64px weight 400) anchors the left column; product photography fills the right. CTA row pairs a `button-primary` with a `button-ghost` "Compare models" link. Vertical padding runs `{spacing.section}` top and bottom. No background photography — the white field and the product image carry all atmospheric weight.

### Metric Card
**`metric-card`** — White card at `{rounded.lg}` (20px) used both in health dashboard showcases and product-feature callouts. The central figure renders in `{typography.metric-display}` (48px, weight 300) — light enough to read as instrument data rather than marketing claim. An uppercase `{typography.label-sm}` label names the metric below. A hairline border replaces shadow here, distinguishing data containers from product cards in mixed layouts.

### Health Alert Badge
**`metric-alert-badge`** — `{colors.health-alert}` (#dc2626) fill at `{rounded.xs}` (4px), caption-scale white text. Appears inline within health metric displays when a reading deviates from baseline. The five extracted reds (#dc2626, #b91c1c, #7f1d1d, #f43f5e, #fb7185) map to a severity spectrum — light rose for mild deviation, deep crimson for critical — enabling urgency communication without iconography alone.

### Health Severity Dot
**`health-severity-dot`** — 8px circle using `{rounded.full}`. Three states: green #22c55e for safe, `{colors.accent-amber}` for warning, and `{colors.health-alert}` for critical. Used in health history timelines and at-a-glance metric summaries throughout the ScanWatch feature pages.

### Category Chip
**`category-chip`** — `{rounded.full}` pill shape with a hairline border in neutral state; active state flips to cobalt fill with white text, border removed. Used to filter the product catalog (Watches, Scales, Sleep, Blood Pressure). The full-radius pill shape is intentional shape language: pills signal filter/tag, 8px-rounded rectangles signal action.

### Color Swatch
**`color-swatch`** — 24px circle, 1.5px `{colors.hairline}` border at rest, 2px `{colors.primary}` ring when selected — consistent with the focus ring logic used throughout. Tap zone expands to 44px on mobile via padding. Used in watch band and case finish configurators.

### Comparison Table
**`comparison-table`** — White card at `{rounded.md}` with hairline cell borders. Check marks render in `{colors.primary}` cobalt; absent features use a `{colors.muted}` em dash. Header row in `{typography.title-md}` on `{colors.canvas}` background; body rows in `{typography.body-sm}`. On mobile the table gains a horizontal scroll container rather than collapsing columns.

### Sticky Add-to-Cart Bar
**`sticky-add-to-cart`** — Pins to the viewport bottom after the product hero scrolls out of view. White background, 1px top hairline border. Displays product name in `{typography.title-md}` and price in `{typography.price}` beside a compact `button-primary`. Height self-sizes to content; padding is `{spacing.base}` × `{spacing.lg}`.

### Footer
**`footer`** — Near-black `{colors.ink}` (#0f0f0f) background. Column headings in `{typography.label-sm}` (uppercase, weight 500) in white. Body links in `{colors.muted}` gray, upgrading to `{colors.surface-card}` on hover. Bottom bar holds copyright and regulatory links in `{typography.caption}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero stacks headline above image (image capped at 300px); nav collapses to hamburger with full-screen overlay; product-card grid is 1-col; comparison table scrolls horizontally; sticky-add-to-cart always visible |
| Tablet | 744–1128px | 2-column product-card grid; hero image shrinks to 45% width; nav shows top-level links, secondary items in dropdown; metric-card grid is 2-col |
| Desktop | 1128–1440px | Full 3–4 column product grid; hero at full 640px min-height; comparison table fully expanded; sticky-add-to-cart appears only after hero exit |
| Wide | > 1440px | Content max-width 1440px centered; hero gains lateral breathing room via increased horizontal padding; section spacing increases proportionally |

### Touch Targets
- All interactive elements maintain a minimum 44×44px touch target on mobile
- Color swatches expand from 24px visual size to 44px tap zone via padding offset
- Nav hamburger tap zone is 48×48px
- Sticky add-to-cart button spans full available width minus horizontal margins on mobile
- Category chips enforce min-height 44px on touch viewports

### Collapsing Strategy
- Navigation: full link bar (desktop) → top-level links only (tablet) → hamburger with full-screen overlay (mobile)
- Product grid: 4-col → 3-col → 2-col → 1-col across breakpoints
- Hero: side-by-side (desktop) → stacked with image below headline (mobile)
- Metric cards: 4-col row (desktop) → 2-col (tablet) → 1-col (mobile)
- Comparison table: full horizontal (desktop/tablet) → horizontal scroll container (mobile)
- Footer columns: 4-col → 2-col → 1-col; legal bar stacks vertically on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Aeonik weight ladder in production use — the site applies `!important` overrides; weights 300/400/500 are inferred from visual hierarchy, not DOM extraction
- Semantic token names for the health severity color system — only raw hex values were captured, not the threshold or naming convention Withings uses internally
- Button height, padding, and border-radius values are not pixel-confirmed from live DOM; values are inferred from visual proportion
- Dark mode or night-mode implementation not captured; one may exist for the Health Mate companion app context
- Accent colors #8672c1 (purple) and #df6389 (rose) are confirmed extracted but their precise product-line mapping is unverified from extraction alone
- Icon system type (SVG sprite, icon font, or inline) not identified; Withings uses extensive custom health and horology icons
- Animation timing and easing curves for the product configurator and metric card transitions not captured
- Mobile navigation structure (mega-menu vs. flat list vs. accordion) not confirmed from extraction
