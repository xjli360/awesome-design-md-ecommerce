---
version: alpha
name: "Legion Paper"
source_url: "https://www.legionpaper.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Three near-identical navies — #112233, #112244, #112255 — stack in Legion Paper's interface the way sheets stack in a ream: each imperceptibly different from the next, collectively communicating depth and material permanence rather than brand expressiveness. The dominant primary (#112244) reads as archival authority against the #f5f5f5 near-white canvas, a pairing that evokes a printer's proof sheet more than a commercial storefront. Navigation and hero backgrounds pull from this same deep field; the three navy variants likely separate header, hero, and footer treatments rather than occupying distinct semantic roles within a single screen.

  Montserrat carries all display, navigation, and button text — its geometric apertures and upright posture suit a brand selling physical precision; uppercase tracking at 0.5px on nav links and labels creates the catalog-page register that specialty-paper customers expect. Open Sans handles body copy and specification text with a neutral authority that keeps the focus on product data: GSM weights, surface textures, archival ratings. The interplay between the two typefaces is functional rather than expressive — two tools from the same rational tradition, each doing the job it is suited for.

  Rounded corners are minimal throughout: `{rounded.xs}` (4px) on buttons and inputs, `{rounded.sm}` (8px) on cards. Hard corners would read as cheap commodity design; extreme rounding would undercut the brand's technical credibility. The 4–8px band is the middle ground a professional supplier earns. Paper-spec badges use `{rounded.xs}` with a hairline border, mimicking the small classification stamps found on physical paper packaging. Category filter pills allow `{rounded.full}` as the one interface surface where a softer affordance signal genuinely benefits interaction.

  The five extracted values cover the entire necessary palette. There is no accent color, no highlight hue, no success green — Legion Paper's audience trusts specification data over persuasive visual design, and the restraint honors that. Product photography and paper samples carry the visual differentiation work that a consumer brand would otherwise assign to color. The primary-disabled state and muted text are derived rather than independently extracted, suggesting the site may rely on framework defaults for these roles.

colors:
  primary: "#112244"
  primary-active: "#112233"
  primary-disabled: "#6b7a96"
  navy-alt: "#112255"
  navy-deep: "#112233"
  ink: "#222222"
  body: "#444444"
  muted: "#6b6b6b"
  spec-muted: "#888888"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Open Sans', system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Open Sans', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Open Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "'Open Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    height: 44px
  button-primary-on-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "4/3"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    badgeTypography: "{typography.spec-label}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    minHeight: 480px
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaStyle: "button-primary-on-dark"
    padding: "{spacing.section} 0"
  paper-spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  category-filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  category-filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.surface-soft}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  section-header:
    textColor: "{colors.primary}"
    typography: "{typography.display-md}"
    borderBottom: "2px solid {colors.primary}"
    paddingBottom: "{spacing.sm}"
    marginBottom: "{spacing.lg}"
  paper-weight-tag:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "3px 7px"
  promo-banner:
    backgroundColor: "{colors.navy-alt}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

### Buttons

**`button-primary`** — Deep navy (#112244) fill with white Montserrat uppercase text at 14px and 0.5px tracking. At 44px tall and 4px radius, the button reads like a document control rather than a consumer CTA — calibrated for professional purchasers selecting paper stock by specification, not impulse. Active state shifts to `primary-active` (#112233), the darkest extracted navy; disabled state desaturates to the muted navy-gray `primary-disabled`. The uppercase letter-spacing ties the button visually to the nav-link register, reinforcing coherence across interactive surfaces.

**`button-secondary`** — White fill with a 1px solid navy border and matching navy text, sharing the same Montserrat uppercase treatment as `button-primary` to maintain typographic consistency. Used for secondary actions on light backgrounds: add to favorites, download spec sheet, view sample pack. Active state lifts the fill to `surface-soft` (#f5f5f5) and deepens the border to `primary-active`, providing a clear pressed state without color drama.

**`button-primary-on-dark`** — White canvas fill with navy text, designed specifically for placement on navy hero or footer backgrounds where `button-primary` would disappear. Keeps the identical 44px height and 4px radius for shape consistency across all contexts. The contrast reversal is the minimum intervention — no rounded softening, no additional padding, no new typeface weight.

### Text Input

**`text-input`** — White fill, 44px height, 4px radius, hairline border (#dddddd) at rest. Focus promotes the border to solid primary navy via `borderFocus`, a direct and quiet signal. Open Sans `body-md` is used here rather than Montserrat — the readable sans-serif suits the data-entry register better than a geometric display face. Applies to paper-weight range selectors, search fields, newsletter signup, and checkout address inputs.

### Navigation

**`nav-bar`** — Full-width primary navy (#112244) masthead at 64px. White Montserrat nav-links in uppercase with 0.5px tracking create a header that functions like a trade catalog's section index. The dark background provides its own visual separation from the canvas below — no hairline separator needed. Logo lockup reverses to white. A secondary row may exist for category links; it likely shares the same navy background with a slightly adjusted opacity or a hairline soft border between rows.

### Product Card

**`product-card`** — White surface with hairline border and 8px radius. Product image occupies a fixed 4:3 aspect ratio zone at the top. Below: product name in `title-md` (Montserrat 18px/600), a horizontal flex row of `paper-spec-badge` elements showing weight, surface type, and archival rating, then a short product description in `body-sm`. Price renders in `title-md` weight. Hover state uses a box-shadow elevation rather than a color shift — appropriate given the constrained palette. Out-of-stock or limited-availability items may use a muted overlay.

### Hero

**`hero`** — Navy background panel spanning full viewport width at minimum 480px tall. Display heading in `display-xl` (Montserrat 40px/700, white), subhead in `body-md` (Open Sans 16px, white at 80% opacity for visual hierarchy). CTA uses `button-primary-on-dark` — white fill, navy text — so the action reads clearly against the dark field without introducing a new color. On mobile the heading drops to 28px (`display-md` scale) and the panel collapses to 320px minimum height. Paper texture or high-resolution product photography may underlay the navy field at reduced opacity.

### Paper Spec Badge

**`paper-spec-badge`** — Small inline chip rendered in `surface-soft` (#f5f5f5) with a hairline border and 4px radius. Open Sans `spec-label` (uppercase, 11px, 0.3px tracking) renders classification values such as "300 GSM", "Hot Press", "Acid Free", or "100% Cotton". Multiple badges appear in a wrapping flex row on product cards and product detail pages, giving the layout a technical data-sheet quality that signals to professional buyers without requiring a table. All badges use the same neutral fill — no color-coding by category, maintaining the monochromatic discipline.

**`paper-weight-tag`** — A filled navy variant of the spec badge, used to prominently call out GSM weight on the card image or at the top of the detail page. White `spec-label` text inverts against the primary navy fill. Appears where GSM is the most decision-critical attribute — typically the primary sort criterion for printmakers and photographers.

### Category Filter Pills

**`category-filter-pill`** / **`category-filter-pill-active`** — Pill-shaped (full-radius) filters for navigating the product catalog. Inactive: white fill, navy border and text. Active: navy fill, white text. Both use Montserrat `button-sm` uppercase. The full radius is a deliberate break from the otherwise rectangular vocabulary — filter pills benefit from the distinct affordance that pills provide, and the shape contrast against rectangular buttons makes the filter row visually parseable at a glance. On mobile the filter row scrolls horizontally.

### Search Bar

**`search-bar`** — Same construction as `text-input` but rendered with a leading search glyph icon in `muted` (#6b6b6b). Focus border promotes to primary navy. Can appear inside the nav-bar on desktop (constrained to ~320px width) or as a full-width panel at the top of the catalog page on mobile. No autocomplete styling is specified from extraction.

### Breadcrumb

**`breadcrumb`** — Muted (#6b6b6b) Open Sans `body-sm` links separated by a "›" character in the same muted color. The active final segment renders in `ink` (#222222) at normal weight without a link underline. Sits above product titles and category headings to orient professional buyers navigating a taxonomy that can be four or five levels deep (Fine Art Papers → Watercolor → Hot Press → 100% Cotton → 300 GSM). The minimal treatment ensures it reads as orientation data rather than a competing navigation element.

### Promo Banner

**`promo-banner`** — Full-width slim bar using `navy-alt` (#112255), the most blue-shifted of the extracted navy trio, to distinguish it from the primary nav without introducing a new hue. White `body-sm` text announces shipping thresholds, seasonal promotions, or sample kit availability. Sits above the `nav-bar` at the very top of the page. No close button specified from extraction.

### Section Header

**`section-header`** — Primary navy `display-md` Montserrat heading (28px/600) with a 2px solid navy rule beneath it, separating catalog sections: Fine Art Papers, Digital Printing, Specialty Stocks, Book Arts. The rule echoes horizontal divisions in printed reference catalogs and technical data sheets, grounding the digital layout in the physical medium the brand supplies.

### Footer

**`footer`** — Uses `navy-deep` (#112233), the darkest of the extracted navies, for maximum visual weight and separation from the page body. Section headings in white Montserrat `title-sm` (uppercase, 0.5px tracking). Link text uses `surface-soft` (#f5f5f5) — slightly off-white to reduce harshness against the deep navy. Body and legal text in Open Sans `body-sm`. Newsletter signup field and submit button sit inline in the footer's first column, using `text-input` and `button-primary-on-dark` respectively.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger icon + logo; hero heading scales to `display-md` (28px); hero min-height 320px; spec badge rows wrap; section padding reduces to `spacing.xxl`; filter pills scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; nav may abbreviate to icon-label links or a condensed bar; hero at 380px min-height; side panel hidden, filters above grid |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all category links visible; hero at 480px; side filter panel for category and attribute browsing |
| Wide | > 1440px | Max-width container (~1400px) centered on canvas; optional four-column product grid for bulk catalog pages; hero background extends edge-to-edge behind contained content |

### Touch Targets

- All buttons and filter pills minimum 44px tall per WCAG 2.1 AA guidance
- Breadcrumb links padded to 44px vertical tap zone even when `body-sm` text renders smaller
- Nav hamburger icon minimum 44×44px tap area
- Paper-spec badges are display-only (non-interactive) and exempt from minimum size requirement
- Promo banner close control (if present) minimum 44×44px

### Collapsing Strategy

- Top nav collapses to logo + hamburger at < 744px; category menu slides in as a full-height drawer sharing the same primary navy background
- Desktop side filter panel collapses to a horizontally scrollable `category-filter-pill` row pinned above the product grid on mobile and tablet
- Hero subhead may be hidden on mobile to reduce scroll depth; CTA and heading remain
- Footer 4-column link grid collapses to 2-column on tablet and single-column accordion on mobile; accordion headers use the same `title-sm` uppercase treatment
- `section-header` rule remains full-width at all breakpoints; heading size may step down from `display-md` to `display-sm` on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No accent, warning, success, or error color extracted — promotional badge colors (sale, new, limited), form validation states, and cart feedback are unspecified; a warm red or amber would need live-site confirmation
- Primary-disabled, body, muted, hairline, and spec-muted values are approximated — the site likely defines these via CSS custom properties loaded at runtime and they were not surfaced by static extraction
- No confirmed hover color for text links or nav items — assumed to be an underline treatment or lightened navy variant
- Logo typeface weight and whether it uses a custom Montserrat cut or a separate logotype file could not be confirmed
- Icon set style (line, filled, mixed) not determinable from color/font extraction alone — specialty paper brands commonly use thin line icons or technical-illustration glyphs
- Product comparison table and spec-grid component patterns not mappable from available hints — these are likely important surfaces given the data-heavy purchasing workflow
- Dark/light mode support not assessed; the three-navy palette would require significant rethinking for a light-mode nav if the site currently defaults to light
- No extracted colors for interactive states on the `nav-bar` dropdown panels — hover and active states on sub-navigation items are unknown
- Sample kit and swatch-request workflow UI not extractable from static hints — may involve a dedicated multi-step flow with specialized components
