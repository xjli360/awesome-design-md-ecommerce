---
version: alpha
name: "Full Focus"
source_url: "https://fullfocus.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Verdana on a bright white canvas with pure magenta (#ff00ff) on every action trigger is an unusual pairing for a planner brand — the typeface was engineered for early CRT screen readability, the color is too saturated for lifestyle aesthetics, yet together they produce something that reads as deliberate utility rather than accident. Full Focus sells a paper planning system built on a "Big 3" daily priorities framework, and the design mirrors that system's core claim: the path to achievement should be visible, unambiguous, and slightly uncomfortable to ignore.

  The palette organizes itself in layers of commitment. Deep navy (#003388), dark teal (#004a59), and brooding indigo-purple (#330968) provide structural tones — the category colors a planner user assigns week by week, role by role, horizon by horizon. Magenta fires at the points of decision: buy buttons, featured CTAs, progress-ring fills. Accent violet (#4721fb) appears at secondary interactive moments; warm cream (#fafae1) surfaces the "how it works" editorial sections where the reading mood should slow from transactional to reflective. Charcoal (#313131) carries body text without the harshness of pure black.

  Verdana's typographic range is narrow by design — the stack runs 400 for reading weight and 700 for display, with no intermediate steps. Full Focus leans into this constraint rather than fighting it: hierarchy comes from size steps and spatial breathing, not from a multi-weight superfamily. The monoline quality of Verdana at 40px echoes the ruled lines and grid columns of the physical planner itself. Everything on the page feels written rather than composed, which suits a brand whose core product is a structured blank page.

  Buttons hold at {rounded.sm} — purposeful, slightly formal rectangles that resist the pill-softness of wellness brands and signal transactional commitment. Cards at {rounded.md} sit on white canvas, letting planner flat-lay photography carry the surface texture. Section breaks at {spacing.section} create chapter-level rhythm on long product pages, mirroring the planner's own section philosophy. On mobile, the magenta primary persists as a sticky bottom bar through the entire product-detail scroll.

colors:
  primary: "#ff00ff"
  primary-active: "#cc00cc"
  primary-disabled: "#ff99ff"
  ink: "#313131"
  body: "#32373c"
  muted: "#444444"
  muted-soft: "#abb8c3"
  hairline: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#fafae1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-navy: "#003388"
  accent-purple: "#330968"
  accent-teal: "#004a59"
  accent-violet: "#4721fb"

typography:
  display-xl:
    fontFamily: "Verdana, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Verdana, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "Verdana, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-sm:
    fontFamily: "Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Verdana, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-label:
    fontFamily: "Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 700
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
    padding: "14px 28px"
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: "12px 26px"
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
    padding: "12px 24px"
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: "12px 16px"
    height: 48px
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.lg}"
    logoColor: "{colors.ink}"
    ctaButton: "{components.button-primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.ink}"
    descriptionTypography: "{typography.body-sm}"
    descriptionColor: "{colors.muted}"
    badgeBackgroundColor: "{colors.primary}"
    badgeTextColor: "{colors.on-primary}"
    badgeTypography: "{typography.label-sm}"
    badgeRounded: "{rounded.xs}"
  hero-block:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    ctaButton: "{components.button-primary}"
    padding: "{spacing.section} 0"
    imagePosition: right
    maxWidth: 1200px
  feature-section:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-md}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.section} {spacing.lg}"
    iconColor: "{colors.primary}"
    iconSize: 32px
  system-badge:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  category-tag-purple:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  category-tag-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    accentBar: "4px solid {colors.primary}"
    quoteTypography: "{typography.body-md}"
    quoteColor: "{colors.body}"
    attributionTypography: "{typography.title-sm}"
    attributionColor: "{colors.ink}"
  email-capture:
    backgroundColor: "{colors.accent-navy}"
    headlineTypography: "{typography.title-md}"
    headlineColor: "{colors.canvas}"
    labelTypography: "{typography.label-sm}"
    labelColor: "{colors.canvas}"
    inputBackground: "{colors.canvas}"
    inputRounded: "{rounded.xs}"
    ctaButton: "{components.button-primary}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
    borderTop: "3px solid {colors.primary}"
  sticky-cta-bar:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    height: 56px
    ctaButton: "{components.button-primary}"
    display: mobile-only

## Components

### Buttons
**`button-primary`** — Solid magenta (#ff00ff) fill, white Verdana bold label, 8px radius. The color is abrupt enough to function as a demand: every buy trigger, "Start the System" CTA, and checkout confirmation on the site uses this token, making the action layer unmissable. Active state darkens to #cc00cc; disabled washes to #ff99ff with `cursor: not-allowed`.

**`button-secondary`** — White fill with a 2px magenta border and magenta label text. Used for softer entry points — "Learn More," plan comparisons, and sample downloads — where the user is still deciding rather than committing. Shares the 48px height and Verdana bold 15px with the primary, so button pairs never produce height jitter.

**`button-ghost`** — Transparent fill, 2px ink border, ink label. Appears in nav overflow menus and tertiary actions like "View Full Comparison" where a colored border would compete with the primary CTA in the same row.

### Text Input
**`text-input`** — White canvas, 1px hairline border at rest, jumps to a 1px magenta border on focus. Verdana 16px/400, 4px corner radius stays visually square against the rounded cards surrounding it. Used in email capture bars, site search, and checkout address fields.

### Navigation
**`nav-bar`** — White background, 64px height, hairline bottom border. Logo in dark ink at far left; navigation links in Verdana bold 14px spaced across center; magenta primary CTA button anchored at far right for direct purchase entry. On mobile, collapses to hamburger-left, logo-center, cart-icon-right.

### Cards
**`product-card`** — White card at {rounded.md}, 1px hairline border, 16px padding. Product photography fills a 3:4 portrait aspect ratio matching the physical planner's proportions; title in Verdana bold 16px; price in Verdana bold 20px. A magenta badge with {typography.label-sm} uppercase at the top-left corner marks new editions or bundle SKUs.

### Hero
**`hero-block`** — Full-width white section, 1200px max-width container. Headline at Verdana bold 40px, subhead at Verdana regular 16px/1.6, single magenta CTA below. Image panel docks right on desktop (planner flat-lay or lifestyle photography), stacks above headline on mobile. Top and bottom padding at {spacing.section} maintains the chapter-break rhythm.

### Feature Section
**`feature-section`** — Cream background (#fafae1 via {colors.surface-soft}) is the warmest surface on the site and is reserved for "How the system works" sequences. A 32px magenta icon heads each step, followed by {typography.display-md} title and {typography.body-md} body. The cream shift slows reading pace from transactional to instructional without a layout change.

### Badges and Tags
**`system-badge`** — Navy pill in {colors.accent-navy} (#003388) with white {typography.label-sm} uppercase, full radius. Marks planner edition or framework level (e.g., "FULL FOCUS SYSTEM," "GUIDED VERSION"). **`category-tag-purple`** and **`category-tag-teal`** — square-edged chips in #330968 and #004a59 respectively, applied to planner section labels like "Roles & Goals" and "Weekly Preview."

### Testimonial Card
**`testimonial-card`** — Cream surface, {rounded.md}, 4px left-edge magenta accent bar as the sole decorative element. Quote in body-md/body color; attribution in title-sm/ink. Arranged in a 3-column grid on desktop, collapsing to a single horizontal scroll lane on mobile. The accent bar maintains visual linkage to the primary action system without adding magenta weight to the quote itself.

### Email Capture
**`email-capture`** — Navy (#003388) full-bleed band: white headline in title-md, canvas-white label-sm field labels, white input boxes at {rounded.xs}, magenta CTA. The navy-to-magenta transition is the most color-dense moment on the site and appears at the base of long-form landing pages just before the footer.

### Footer
**`footer`** — Dark ink (#313131) background, 3px magenta top border as a visual terminus that echoes the CTA system one final time. Canvas-white body copy, hairline-tinted links that shift to magenta on hover. Four-column link group grid on desktop; collapses to accordion-expand on mobile.

### Sticky CTA Bar
**`sticky-cta-bar`** — Mobile-only: white bar, 56px tall, docked to the bottom viewport edge with a hairline top border. Contains a full-width magenta primary button. Persists through the entire product-detail scroll and disappears only when the footer enters the viewport.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; sticky magenta CTA bar at viewport bottom; nav collapses to hamburger drawer; hero image stacks above headline; product grid becomes single-column vertical scroll |
| Tablet | 744–1128px | Two-column product grid; hero splits text-left / image-right at 50/50; nav links visible inline; feature section becomes 2-column step layout |
| Desktop | 1128–1440px | Three-column product grid; hero at full bleed with 1200px max-width container; feature section 3-column; testimonials 3-column grid |
| Wide | > 1440px | Content locked to 1200px max-width; canvas-white gutters fill the remainder; no additional layout changes |

### Touch Targets
- All interactive elements minimum 48px tall (buttons, inputs, nav links)
- Sticky CTA bar is full-width and 56px tall for comfortable thumb reach from either corner
- Product card entire surface area is tappable, not only the CTA button
- Hamburger icon tap target padded to 44×44px regardless of visible icon size

### Collapsing Strategy
- Nav: inline desktop links → left-slide hamburger drawer on mobile; CTA button demoted to sticky bottom bar
- Hero: two-column (text left, image right) → single column (image top, text + CTA below)
- Feature steps: 3-column icon grid → vertical stacked numbered list
- Product grid: 3 → 2 → 1 columns as viewport narrows
- Testimonials: 3-column → horizontal scroll lane → single stacked column
- Footer: 4-column link groups → stacked accordion with tap-to-expand per section

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted palette contains many Gutenberg/WordPress block-editor default colors (#00d084, #0693e3, #0d6efd, #cf2e2e, #ff6900, #007cba, #006ba1) that are almost certainly CMS editor artifacts, not brand tokens — the true brand palette is difficult to isolate from the editor palette
- Pure magenta (#ff00ff) as primary is distinctive enough to warrant verification against the live site's actual CTA buttons; it may be a content-editor highlight or selection color rather than a confirmed brand primary
- Only one font family extracted (Verdana, sans-serif); no custom or variable font was detected — the site may load a proprietary typeface via JavaScript that was not captured during extraction
- Verdana does not support intermediate weights (only 400/700 are available); if a custom font is confirmed, the type scale should be rebuilt with appropriate weight tokens
- No dark-mode token set extracted; dark-mode support is unknown
- Border-radius values inferred from visual category norms rather than extracted from computed styles; {rounded.sm} and {rounded.md} should be verified against the live site
- Email, checkout, and account-portal UI flows were not accessible during extraction; input validation states (error, warning, success) and their colors are not confirmed
