---
version: alpha
name: "James Allen"
source_url: "https://www.jamesallen.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every diamond on James Allen's product pages rotates in 360° high-definition under a deep-navy stage (#0c1636) — an interface decision that solved the primary anxiety of online jewelry buying before streaming product video became ubiquitous. The brand operates two visual registers: an immersive dark mode (near-black navy #100e31, #0c1636) built for diamond theater and ring configuration, and a clean warm-cream ground (#fffbf7) reserved for editorial and lifestyle content. Brown LL carries the primary typographic voice — a humanist sans with slightly squared apertures that reads as modern premium without geometric coldness; Lora surfaces in editorial display moments as a contrast serif, and Pinyon Script appears in wedding-facing contexts as the sole calligraphic gesture toward tradition. The CTA system is architecturally split: a bright #0066ff handles all commerce actions — add to cart, filter selection, ring builder progression — while the deep navy family (#0c1636, #100e31, #151542) functions as brand environment rather than traditional primary color. Buttons use measured corner radii rather than sharp edges or full pills, a posture that reads as precise and assured, fitting for a brand that asks customers to examine facet symmetry at 40× zoom. Neutral surface fills (#f3f5f7, #e9ebec) keep chrome recessive so the diamond occupies visual center stage. The sage #77ab94 appears on certification and ethical-sourcing callouts — a provenance signal delivered with quietude rather than marketing volume. The overall system reads as a digital jeweler's loupe: clinical precision in the product environment, warmth in the editorial wrapping.

colors:
  primary: "#0066ff"
  primary-active: "#0024d6"
  primary-disabled: "#8a8aa0"
  navy-deep: "#100e31"
  navy-dark: "#0c1636"
  navy-mid: "#151542"
  navy-surface: "#2c2c55"
  charcoal: "#2a2d39"
  ink: "#1a1a1a"
  body: "#4a4a4a"
  muted: "#8a8aa0"
  muted-light: "#b4b4b4"
  hairline: "#d9d9d9"
  hairline-soft: "#e8e8e8"
  hairline-strong: "#c4c4c4"
  canvas: "#fffbf7"
  canvas-neutral: "#ffffff"
  surface-soft: "#f3f5f7"
  surface-card: "#f6f6f6"
  surface-mid: "#f2f2f2"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  alert-error: "#eb1000"
  alert-error-soft: "#f56c6c"
  sage: "#77ab94"
  sky: "#029af0"

typography:
  display-xl:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Brown LL', 'Nunito Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Brown LL', 'Nunito Sans', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Brown LL', 'Nunito Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Brown LL', 'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Brown LL', 'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Brown LL', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Brown LL', 'Nunito Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-label:
    fontFamily: "'Brown LL', 'Nunito Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Brown LL', 'Nunito Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Brown LL', 'Nunito Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Brown LL', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "'Brown LL', 'Nunito Sans', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  price-sm:
    fontFamily: "'Brown LL', 'Nunito Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  script-accent:
    fontFamily: "'Pinyon Script', cursive"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Brown LL', 'Nunito Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  filter-label:
    fontFamily: "'Brown LL', 'Nunito Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
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
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-dark:
    backgroundColor: "{colors.navy-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas-neutral}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted-light}"
  nav-bar:
    backgroundColor: "{colors.canvas-neutral}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-dark:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.canvas-neutral}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imageBackground: "{colors.surface-mid}"
    priceTypography: "{typography.price}"
    labelTypography: "{typography.caption-label}"
    nameTypography: "{typography.body-sm}"
  diamond-viewer:
    backgroundColor: "{colors.navy-dark}"
    controlsColor: "{colors.on-dark}"
    overlayTextColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    badgeTypography: "{typography.badge}"
  ring-builder-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    stepActiveColor: "{colors.primary}"
    stepInactiveColor: "{colors.muted-light}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  filter-panel:
    backgroundColor: "{colors.canvas-neutral}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    sliderActiveColor: "{colors.primary}"
    sliderTrackColor: "{colors.hairline-strong}"
    labelTypography: "{typography.filter-label}"
    rounded: "{rounded.sm}"
  certification-badge:
    backgroundColor: "{colors.sage}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  price-display:
    textColor: "{colors.navy-deep}"
    typography: "{typography.price}"
    strikethroughColor: "{colors.muted-light}"
    captionTypography: "{typography.caption}"
  hero-dark:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    accentTypography: "{typography.script-accent}"
    subTypography: "{typography.body-md}"
  search-bar:
    backgroundColor: "{colors.canvas-neutral}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    height: 44px
    iconColor: "{colors.muted}"
    typography: "{typography.body-md}"
  diamond-4c-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.caption-label}"
    padding: 6px 12px
  comparison-table:
    backgroundColor: "{colors.canvas-neutral}"
    headerBackground: "{colors.navy-mid}"
    headerTextColor: "{colors.on-dark}"
    rowEvenBackground: "{colors.surface-soft}"
    rowOddBackground: "{colors.canvas-neutral}"
    borderColor: "{colors.hairline-soft}"
    typography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-light}"
    headingTypography: "{typography.caption-label}"
    linkTypography: "{typography.body-sm}"
    dividerColor: "{colors.navy-surface}"
  promo-banner:
    backgroundColor: "{colors.navy-mid}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    accentColor: "{colors.sky}"
  error-state:
    textColor: "{colors.alert-error}"
    iconColor: "{colors.alert-error}"
    softBackground: "#fff5f5"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"

## Components

### Buttons

**`button-primary`** — Bright #0066ff fill at 48px height with an 8px corner radius, the workhorse for every commerce action: "Add to Cart," "Start with a Diamond," ring-builder step progression. Hover state deepens to `{colors.primary-active}` (#0024d6); disabled state applies `{colors.primary-disabled}` (#8a8aa0) at 60% opacity. Letter-spacing sits at a positive 0.2px to keep the Brown LL label readable at 15px without crowding.

**`button-secondary`** — Warm-cream `{colors.canvas}` background with a 1px #0066ff border and matching blue label text; inherits the same 48px height and 8px radius as the primary. Used for secondary ring-builder paths ("Browse All Diamonds") and side-by-side compare CTAs where a filled blue button would dominate.

**`button-dark`** — Deep navy (#0c1636) fill with white text; deployed on hero banners and diamond-theater sections where the blue primary would dissolve into the dark background. Identical height and radius geometry to `button-primary`.

**`button-ghost`** — Transparent background with #0066ff label text only; used for low-priority inline actions such as filter resets, "View More," and editorial link prompts.

### Text Input

**`text-input`** — White (`{colors.canvas-neutral}`) fill, 1px #d9d9d9 border that upgrades to a 1px #0066ff outline on focus. 48px tall, 4px radius — precise without harshness. Placeholder text renders in `{colors.muted-light}` (#b4b4b4).

### Navigation

**`nav-bar`** — White background with a 1px #e8e8e8 bottom border at 72px height. Links in Brown LL 14px/500 weight with hover underline. A `nav-bar-dark` variant uses `{colors.navy-deep}` (#100e31) background with white text for pages whose hero content begins with a dark canvas section.

### Product Cards

**`product-card`** — White card with 1px hairline border and 8px rounding. Diamond product images sit on a neutral #f2f2f2 swatch background to prevent color cast from the warm cream canvas. Price type is large (24px/700) in deep navy to anchor hierarchy; category labels above the name use all-caps spaced captions at 12px for clear taxonomy.

### Diamond Viewer

**`diamond-viewer`** — The product's signature: a deep-navy (#0c1636) presentation stage for the 360° HD rotating diamond. Controls, zoom indicators, and quality badges render in white against the dark field. The 12px corner radius softens the stage frame against the rounded silhouettes of engagement ring photography. A `{typography.badge}` all-caps label ("HD 360°") anchors to the corner.

### Ring Builder Panel

**`ring-builder-panel`** — Soft-surface (#f3f5f7) background, 8px rounding, and 32px interior padding. A multi-step progress indicator uses #0066ff for the current step and #b4b4b4 for upcoming steps. This panel persists as a right-column scaffold through the full ring customization flow (choose setting → choose diamond → customize metal).

### Filter Panel

**`filter-panel`** — White background with a 1px hairline border. Range sliders (carat, price) use an #0066ff active track on a #c4c4c4 inactive track. All filter group labels render in all-caps spaced Brown LL at 13px/500. Used as a persistent left-rail column on the diamond search grid exposing the 4C filters.

### Badges

**`certification-badge`** — Sage green (#77ab94) pill with white all-caps 11px/700 text. Applied to GIA- and AGS-certified stones and ethical-sourcing callouts. The sage tone marks trust credentials without competing with the blue CTA system or triggering urgency associations of promotional red or orange.

**`diamond-4c-chip`** — Soft-surface fill, 1px hairline border, 4px radius. Used inline in product cards and the ring builder to surface cut grade, color grade, and clarity at a glance. Caption-label all-caps type keeps the chip legible at compact sizes.

### Hero Sections

**`hero-dark`** — Full-bleed deep navy (#100e31) canvas with Lora display-xl heading in white and white body subtext. CTA uses `button-primary` (blue reads as vivid against the dark field). Used for high-stakes seasonal landing pages — proposal season, new collection launches.

**`hero-editorial`** — Warm cream (#fffbf7) canvas. Lora display-xl provides editorial weight; a Pinyon Script accent (`{typography.script-accent}`) may overlay as a seasonal flourish for bridal-oriented content. CTA uses `button-secondary` (blue-outlined on cream for visual clarity).

### Search Bar

**`search-bar`** — Full-pill radius, 44px tall, white fill with a 1px hairline border. Deployed as the top-nav persistent search entry and as a hero-section diamond-search launch point. Magnifying glass icon in `{colors.muted}` (#8a8aa0).

### Comparison Table

**`comparison-table`** — Side-by-side diamond spec comparison with a deep-navy (#151542) header row in white text, alternating soft-surface and white body rows. Used in the "Compare Diamonds" overlay for reviewing 4C grades, cut grades, and certification side by side.

### Footer

**`footer`** — Dark charcoal (#2a2d39) background with muted-gray (#b4b4b4) link text. Section headers in all-caps spaced Brown LL 12px. Row dividers use `{colors.navy-surface}` (#2c2c55) to create subtle separation within the dark field without introducing a hard contrast line.

### Promo Banner

**`promo-banner`** — Medium navy (#151542) strip pinned above the main nav. White body text with sky-blue (#029af0) highlights for offer terms and codes. Caption-scale type keeps it unobtrusive; single line at desktop, wraps gracefully on mobile.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; diamond viewer fills full viewport width; ring builder becomes a bottom-sheet flow rather than a sidebar panel; nav collapses to hamburger; filter panel launches as a full-screen modal drawer |
| Tablet | 744–1128px | Two-column product grid; ring builder shifts to a sticky bottom CTA bar; nav shows primary categories inline with a collapsed mega-menu; filter panel available as a slide-in drawer |
| Desktop | 1128–1440px | Three-column product grid; ring builder shows as a persistent right-rail panel; full mega-nav with all category columns visible; filter panel renders as a persistent left-rail column on diamond search |
| Wide | > 1440px | Grid max-width capped at ~1440px, centered; hero images scale to fill but content column stays centered; diamond viewer capped at ~640px to maintain intimacy with the product |

### Touch Targets

- All 4C range slider handles use a minimum 44px drag-target height
- Ring builder step buttons minimum 48px height and 200px width on mobile
- Diamond comparison checkboxes minimum 44×44px touch area
- Bottom-sheet swipe zone extends to the full card width rather than a narrow handle strip
- Filter clear/apply buttons minimum 48px height in the mobile filter drawer

### Collapsing Strategy

- Mega-nav collapses to hamburger icon below 1128px; drawer opens from the left edge
- Ring builder collapses: right-rail panel → sticky bottom CTA bar → full-screen bottom-sheet modal
- Filter panel collapses to a floating "Filters · N" chip button that opens a full-screen drawer at mobile
- Diamond 4C comparison table scrolls horizontally on mobile with a fixed left-column thumbnail and name
- Promo banner wraps to two lines below 480px rather than truncating or hiding

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Page title extracted as "Blue Nile: Diamond Jewelers" — likely a scraper routing error or A/B test artifact; hex colors and font stacks appear consistent with James Allen's documented visual system, but the primary palette should be verified against live jamesallen.com production markup
- No gold/champagne accent token extracted — James Allen historically uses warm gold tones in ring detail photography and some editorial UI; a value near #c9a96e or #d4af6a would be expected but was not captured in the extraction
- Exact button corner-radius not confirmed from devtools — 8px (`{rounded.sm}`) assigned based on mid-market premium positioning; verify against live computed styles
- Brown LL weight variants (Book, Regular, Bold, Light) not enumerated in extraction; fontWeight assignments are estimates based on visual hierarchy expectations for the category
- Pinyon Script confirmed in stacks but deployment contexts (hero overlays, certificates, email headers) not audited — usage recommendations are inferred from brand category and seasonal patterns
- Meta theme-color absent — no mobile chrome color signal captured; `{colors.navy-dark}` (#0c1636) assumed as intended status-bar color based on dominant dark surface
- Animation and transition values not extracted — diamond viewer rotation behavior, product card hover transitions, and ring builder step animations are not specified
- Dark-mode stylesheet behavior unknown — the diamond-viewer dark stage suggests intentional dark surfaces, but a full prefers-color-scheme implementation was not confirmed
