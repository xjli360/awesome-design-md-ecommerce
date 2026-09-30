---
version: alpha
name: "Rancilio"
source_url: "https://www.ranciliogroup.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every surface on the Rancilio site earns its existence through restraint — a near-black (#252525) drawn so close to true black it registers as industrial rather than simply dark, held against a neutral #f5f5f5 canvas that keeps product photography isolated from ambient noise. The brand doesn't reach for a signature accent color; the machines themselves — the Silvia's brushed stainless boiler cap, the professional Class's commercial group head geometry — are the visual event, and the interface steps aside to let them perform. Type runs exclusively on system stacks (Arial, Helvetica Neue, -apple-system) at controlled weights, giving pages the register of a precision spec sheet: measured, unornamented, exact. Rancilio, founded in Milan in 1927, treats the product shot the way a data sheet treats a circuit schematic — multiple angles, component callouts, cutaway renders, no lifestyle fog. Buttons sit at low-radius corners ({rounded.xs} to {rounded.sm}), matching the machines' squared-off stainless housings rather than the pill forms prevalent in consumer software. The mid-gray band (#bfbfbf, #949494, #d9d9d9) handles all subordinate work — navigation hairlines, ghost states, helper text, section dividers — so nothing in that register competes with the product. Where other espresso brands lead with café-mood photography, Rancilio foregrounds machine anatomy and heritage timeline entries that function as engineering credentials rather than nostalgia. Spacing is generous at the section level (64px between content blocks) but tight inside component groups, echoing the close-tolerance assembly philosophy the brand has maintained for nearly a century. The result reads as a European trade catalog cross-bred with a product configurator, where material specifications and professional pedigree carry the persuasive weight.

colors:
  primary: "#252525"
  primary-active: "#010101"
  primary-disabled: "#bfbfbf"
  ink: "#252525"
  body: "#4a4a4a"
  muted: "#949494"
  muted-soft: "#bfbfbf"
  hairline: "#d9d9d9"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  dark-navy: "#1e1f26"
  mid-gray: "#bfbfbf"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.25px
  spec-label:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  eyebrow:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase

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
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
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
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.canvas}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
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
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    imageAspect: "4/3"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    minHeight: 600px
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 480px
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    alternateRowBackground: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.body}"
    rowBorder: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} {spacing.base}"
  machine-badge:
    backgroundColor: "{colors.dark-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  award-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    captionTypography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg} {spacing.xl}"
  range-grid:
    backgroundColor: "{colors.canvas}"
    cardBorder: "1px solid {colors.hairline}"
    cardHoverBorder: "1px solid {colors.primary}"
    cardRounded: "{rounded.none}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    gap: "{spacing.base}"
  heritage-timeline:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    accentColor: "{colors.mid-gray}"
    yearTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-sm}"
    paddingVertical: "{spacing.section}"
    connectorColor: "{colors.muted-soft}"
  section-divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    marginVertical: "{spacing.section}"
  footer:
    backgroundColor: "{colors.dark-navy}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted-soft}"
    linkTypography: "{typography.body-sm}"
    labelTypography: "{typography.spec-label}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Full-bleed #252525 with white uppercase label (14px/700/0.5px tracking), 4px corner radius, and 48px height. Active state drops to pure #010101; disabled fills with #bfbfbf and retains white text. The uppercase treatment aligns with the technical spec-sheet register of the surrounding UI, making CTAs feel like confirmed actions rather than soft invitations.

**`button-secondary`** — White fill with a 2px solid #252525 outline, matching height and typography to the primary button. The outline treatment gives a clear visual hierarchy without introducing any new color into the palette. Used for secondary actions like "Find a Dealer," "Download Brochure," or "Compare Models."

**`button-ghost`** — Transparent fill with 2px white border and white label, deployed exclusively on dark hero-banner surfaces where filled buttons would lose contrast. Same type scale as primary and secondary. The ghost treatment keeps the action hierarchy intact on dark fields without breaking the monochromatic system.

### Text Input

**`text-input`** — 48px height with 1px #d9d9d9 border at rest, snapping to 1px #252525 on focus. Placeholder text in #949494; entered text in #252525. Corner radius stays at {rounded.xs} to match the button family geometry. No shadow or glow on focus — the border weight change alone signals state.

### Navigation

**`nav-bar`** — 72px tall on a white background with a 1px #d9d9d9 bottom hairline. Nav links at 14px/700/0.25px tracking signal that navigation labels belong to the same typographic register as action labels — both are functional, neither is decorative. The dark variant (`nav-bar-dark`) inverts to a #252525 fill for campaign landing pages and full-bleed hero contexts where the white nav would feel disconnected.

### Product Card

**`product-card`** — Zero border-radius, 1px #d9d9d9 perimeter border, 24px internal padding, 4:3 image aspect ratio favoring machine side-profile and three-quarter studio shots. On hover, the border color steps to #252525 without animation; the snap rather than transition reinforces the mechanical, non-soft-landing character of the brand. Title at {typography.title-md}, secondary copy at {typography.body-sm}.

### Hero Banner

**`hero-banner`** — Full-bleed #252525 with white type, 600px minimum height, {spacing.section} vertical padding. Headline uses {typography.display-xl} (48px/700/−0.5px tracking). The dark fill turns product photography into a reveal moment — machinery emerging from shadow rather than floating on white. The light variant (`hero-banner-light`) uses #f5f5f5 fill for secondary section heroes on interior and sub-category pages.

### Specification Table

**`spec-table`** — Two-column label/value layout with labels in {typography.spec-label} (11px/700/uppercase/1px tracking) at #949494 and values in {typography.body-sm} at #4a4a4a. Alternating rows in #f5f5f5 and white. This component carries significant persuasive weight on product detail pages, where pump pressure (9 bar), boiler volume, power draw, and water tank capacity define the purchase decision for informed buyers. Row borders in {colors.hairline-soft}.

### Machine Badge

**`machine-badge`** — A tight rectangular chip in {colors.dark-navy} (#1e1f26) with {typography.eyebrow} text (11px/700/uppercase/1.5px tracking), zero border-radius. Applied over product card imagery to signal product line tier — "Professional," "Home," "Super Automatic" — without obscuring the machine geometry beneath it.

### Award Strip

**`award-strip`** — A horizontal #f5f5f5 band with a 1px top hairline, used to surface industry certifications, barista competition sponsorships, and trade publication recognition. Eyebrow label at {typography.spec-label}; individual award captions at {typography.caption}. Positions professional pedigree as an ambient credential rather than a hero claim.

### Range Grid

**`range-grid`** — 3-column card grid on desktop, each cell bordered in 1px #d9d9d9 with zero radius. Card hover state steps border to 1px #252525. Title at {typography.title-md}, descriptor text at {typography.body-sm}, 16px gap between cards. Used on the main product-line landing page to let buyers self-select into home, professional, or super-automatic categories before entering individual product detail.

### Heritage Timeline

**`heritage-timeline`** — Full-bleed #252525 section with white text and #bfbfbf connecting lines between dated entries. Year anchors at {typography.display-md} (32px/700), body copy at {typography.body-sm}. The dark field makes the timeline read as institutional record — 1927 founding date, key model launches, professional certifications — rather than brand mythology.

### Footer

**`footer`** — {colors.dark-navy} (#1e1f26) background, white primary text, #bfbfbf for navigation links. Section column labels in {typography.spec-label} (uppercase/tracked). Body links and legal text at {typography.body-sm}. The one-step shift from #252525 (page ink) to #1e1f26 (footer field) is subtle enough to read as a tonal landing zone rather than a new color statement.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; hero-banner drops to 360px min-height; range-grid single-column; spec-table horizontal scroll with sticky label column; button height reduces to 44px; product-card image stacks above text |
| Tablet | 744–1128px | Nav expands to 2-level horizontal with dropdowns; range-grid 2-column; hero-banner at 480px min-height; product-card maintains side-by-side image and text |
| Desktop | 1128–1440px | Full nav with mega-dropdown for product lines; range-grid 3-column; spec-table inline beside product image; heritage-timeline horizontal scroll |
| Wide | > 1440px | Content caps at 1280px max-width; hero-banner image fills remaining bleed without content scaling; section spacing increments +8px per zone |

### Touch Targets
- All buttons minimum 44×44px on mobile
- Hamburger menu icon minimum 44×44px tap zone with padding
- Product card entire surface area is tappable, not limited to the CTA button
- Spec-table rows minimum 40px tall to support horizontal swipe recognition without accidental tap activation
- Badge and award-strip elements non-interactive; no minimum target required

### Collapsing Strategy
- Primary nav: hamburger at < 744px with slide-in drawer; full horizontal above 744px
- Range grid: 3-col → 2-col at tablet → 1-col at mobile
- Hero text block: overlaid left-aligned on desktop; stacks below image on mobile
- Spec table: horizontal scroll container with position-sticky label column on mobile
- Heritage timeline: vertical stack on mobile; horizontal scroll on desktop
- Footer columns: 4-col → 2-col at tablet → 1-col accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; all font stacks resolve to system fonts (Arial, Helvetica Neue, -apple-system). Rancilio may use a licensed face loaded via CSS `@font-face` not captured in static extraction.
- The majority of extracted hex values (#3858e9, #1890ff, #40a9ff, #91d5ff, #00d084, #0693e3, #1778f2, #ea4434, #f00075, #02e49b, #e94c89) appear to be WordPress admin panel, Gutenberg block editor, Ant Design component library, or social-media-embed brand colors — not Rancilio design tokens.
- No meta theme-color is set; mobile browser address-bar treatment and PWA splash behavior are undefined.
- Primary interactive accent is ambiguous — the extracted palette suggests near-black as the primary, but a distinct CTA accent (red, copper, or gold referencing machine hardware) may exist on product detail or dealer-locator pages not reached by the crawler.
- Motion and animation tokens not captured; product reveal transitions, hover animations on range-grid cards, and scroll-triggered section entrances are unknown.
- Dark mode support status is unknown.
- Icon system style (line weight, filled vs. outlined, corner radius) is not derivable from color extraction alone.
- Dealer-locator and configurator sub-experiences may carry distinct component styles not reflected here.
