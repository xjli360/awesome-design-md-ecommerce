---
version: alpha
name: "Nomad Grills"
source_url: "https://nomadgrills.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Steel grates, tack-welded frames, and a $399 price point that implies no wasted material — Nomad's visual language follows the same discipline as its hardware. The site anchors on a near-void navy `#112233` that reads almost as black until it sits next to true black `#121212`, where the chromatic difference surfaces as a subtle cool cast that distinguishes structural zones from body text. Branded steel-blue `#2a4d7f` — the meta theme-color — carries all interactive scaffolding: primary buttons, hover states on navigation links, and price-callout badges that the brand treats as product specs rather than marketing elements. The neutral gray axis runs from `#dedede` hairlines through `#e3e2e1` warm surfaces to `#a3a2a1` muted labels, mapping onto the powder-coat and brushed-steel tones of the grill itself without forced analogy.

  Type is the unexpected character here. HCo Gotham SSm handles all UI scaffolding — form labels, nav, body copy — but the display stack reaches for Magnesium MVB Condensed, an ink-trap display face with an American vernacular weight that reads less like an outdoor-recreation brand and more like a vintage machine-stamped serial plate. Termina handles section labels in tight spaced uppercase, reinforcing a workshop register. The result is a typographic hierarchy that feels physically grounded rather than aspirational.

  Buttons are sharp-edged (`{rounded.xs}`) or borderless, never pill-shaped; every CTA could exist as a painted stencil on a steel surface. The "Made in USA" badge uses the same no-radius treatment, sitting alongside price callouts (`{typography.price-display}`) that use Magnesium MVB at a scale that makes $399 feel declarative rather than discounted. Navigation sits in a dark `{colors.ink}` bar with reversed white type, collapsing at mobile into a compact menu that preserves the full product lineup. Spec tables use `{colors.surface-soft}` row backgrounds and `{typography.title-sm}` labels in tracked uppercase, matching the format of an equipment datasheet more than a lifestyle PDP.

colors:
  primary: "#2a4d7f"
  primary-active: "#1e3d6b"
  primary-disabled: "#6b8ab0"
  ink: "#112233"
  body: "#121212"
  muted: "#a3a2a1"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#e3e2e1"
  surface-card: "#f5f4f3"
  on-primary: "#ffffff"
  steel-mid: "#a3a2a1"
  ash-light: "#e3e2e1"
  navy-deep: "#112233"

typography:
  display-xl:
    fontFamily: "'magnesium-mvb-condensed', 'magnesium-mvb', 'termina', sans-serif"
    fontSize: 60px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px
    textTransform: uppercase
  display-md:
    fontFamily: "'magnesium-mvb-condensed', 'magnesium-mvb', sans-serif"
    fontSize: 38px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.5px
    textTransform: uppercase
  display-sm:
    fontFamily: "'magnesium-mvb', 'termina', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'HCo Gotham SSm', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'HCo Gotham SSm', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  body-md:
    fontFamily: "'HCo Gotham SSm', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'HCo Gotham SSm', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'HCo Gotham SSm', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.4px
  button-md:
    fontFamily: "'HCo Gotham SSm', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.75px
    textTransform: uppercase
  button-sm:
    fontFamily: "'HCo Gotham SSm', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'HCo Gotham SSm', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 1.25px
    textTransform: uppercase
  price-display:
    fontFamily: "'magnesium-mvb', 'termina', sans-serif"
    fontSize: 34px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0
  badge:
    fontFamily: "'HCo Gotham SSm', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.75px
    textTransform: uppercase
  label-tag:
    fontFamily: "'termina', 'HCo Gotham SSm', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 2.5px
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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
  button-ghost-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.on-primary}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "none"
    logoColor: "{colors.on-primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "4/3"
    padding: "{spacing.base}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    overlayColor: "{colors.navy-deep}"
    overlayOpacity: 0.55
  price-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 6px 12px
  made-in-usa-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.steel-mid}"
    padding: 6px 12px
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.title-sm}"
    valueTypography: "{typography.body-sm}"
    rowBorder: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    altRowBackgroundColor: "{colors.canvas}"
  section-label:
    textColor: "{colors.primary}"
    typography: "{typography.label-tag}"
    marginBottom: "{spacing.sm}"
  product-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 4px 10px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headerBackgroundColor: "{colors.ink}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.title-md}"
    rounded: "{rounded.none}"
    borderLeft: "none"
  announcement-bar:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    height: 36px
    textAlign: center
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-primary}"
    borderTop: "2px solid {colors.primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — A solid `{colors.primary}` navy fill at 48px height with sharp `{rounded.xs}` corners, all-caps Gotham SSm at 1.75px letter-spacing. On hover the fill deepens to `{colors.primary-active}`; the uppercase tracking ensures legibility at smaller viewport widths without size increase. Disabled state drains to `{colors.primary-disabled}` with no opacity trick, keeping the button visually legible as unavailable rather than invisible.

**`button-secondary`** — Transparent background with a 2px `{colors.primary}` border; same height and typography as primary. Functions as a "learn more" or "compare" companion wherever the primary CTA commits the user to cart or checkout.

**`button-ghost-dark`** — Reversed for hero and dark-background sections: transparent fill, 2px white border, white text. Used directly over `{colors.ink}` panels where a filled button would compete with product photography.

### Nav Bar

**`nav-bar`** — Full-width `{colors.ink}` bar at 64px sitting atop an optional `{colors.navy-deep}` announcement strip. All links in `{typography.nav-link}` — 12px tracked uppercase Gotham SSm in white — with the brand wordmark reversed white or a horizontal lockup logo. No underline hover; color shifts to `{colors.primary}` on hover, keeping focus obvious without a layout shift. A cart icon with item-count badge sits right-aligned; the badge inherits `{colors.primary}` fill and `{typography.badge}` type.

### Product Card

**`product-card`** — A `{colors.surface-card}` card with a 1px `{colors.hairline}` border and minimal `{rounded.xs}` radius. The image occupies a fixed 4:3 aspect ratio above copy; below it, the product name in `{typography.title-md}` tracked uppercase, price in `{typography.price-display}` using Magnesium MVB, and a short descriptor line in `{typography.body-sm}`. A `made-in-usa-badge` and optional `price-badge` sit as overlay pills on the image corner. No shadow; border alone provides lift.

### Hero Section

**`hero-section`** — Dark `{colors.ink}` canvas at minimum 560px tall, with product photography treated as a full-bleed background image behind a `{colors.navy-deep}` scrim at 55% opacity to keep headline contrast. Headline in `{typography.display-xl}` — Magnesium MVB Condensed, uppercase, up to 60px — with a subtitle in `{typography.display-sm}`. A `button-primary` and `button-ghost-dark` sit side by side below the subtitle, separated by `{spacing.base}` gap. On mobile the background image crops to portrait; the headline drops to `display-md` scale.

### Price Badge

**`price-badge`** — A hard-edged `{colors.primary}` chip with `{typography.badge}` type in white, no border radius. Communicates the $399 price point with the same visual weight as a spec label, not a promotional sticker. Sits flush to an image corner or inline within a spec table row.

### Made in USA Badge

**`made-in-usa-badge`** — Same zero-radius geometry as the price badge but on `{colors.ink}` fill with a 1px `{colors.steel-mid}` border and white `{typography.badge}` text. The brand places this prominently on all PDPs and hero panels; it functions as a trust signal treated with the typographic register of a certification mark.

### Spec Table

**`spec-table`** — Alternating `{colors.surface-soft}` / `{colors.canvas}` rows, each with a 1px `{colors.hairline}` horizontal rule. Labels in `{typography.title-sm}` uppercase navy-deep and values in `{typography.body-sm}` regular weight. No outer border; the table bleeds to the content column width. Used for cooking surface dimensions, weight, fuel type, and country of manufacture — Nomad treats specs as the primary product narrative.

### Section Label

**`section-label`** — A `{colors.primary}` inline tag in `{typography.label-tag}` — 11px Termina, 2.5px tracking, uppercase — positioned above section headlines. Acts as the document-structure indicator that separates hero, features, specs, and testimonial blocks without introducing a full divider component.

### Announcement Bar

**`announcement-bar`** — A 36px `{colors.navy-deep}` strip pinned above the nav, centered `{typography.badge}` white text for shipping thresholds or launch messages. Dismissable on mobile; persistent on desktop. Reinforces the dark-palette entry experience before the full nav renders.

### Cart Drawer

**`cart-drawer`** — A right-side slide panel with `{colors.canvas}` body and a `{colors.ink}` header bar carrying `{typography.title-md}` white label. No border-radius on the drawer itself; the transition is a hard-edge slide matching the brand's zero-softness UI surface language. Line items use `{typography.body-sm}` for product names and `{typography.title-sm}` for prices.

### Footer

**`footer`** — Full-width `{colors.ink}` background with a 2px `{colors.primary}` top border acting as a brand-color terminus. Column headings in `{typography.title-sm}` white; links in `{typography.body-sm}` `{colors.muted}` with hover shifting to `{colors.on-primary}`. Social icons sit inline at 20px, white fill. The Made in USA registration mark appears in the legal row in `{typography.caption}` `{colors.muted}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; hero headline scales from `display-xl` (60px) to `display-md` (38px); product cards stack single-column; spec table collapses to card-style label-above-value layout; hero CTA buttons stack vertically; announcement bar becomes single-line scrolling ticker |
| Tablet | 744–1128px | Two-column product grid; nav retains full link row but removes sub-category labels; hero maintains two-up CTA layout; spec table restores two-column format |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; hero at full 60px headline; spec table inline with product image in a 60/40 split |
| Wide | > 1440px | Max content width capped at 1440px with `{colors.ink}` bleed to viewport edges; hero image scales without cropping; product grid optionally expands to four columns |

### Touch Targets

- All interactive elements (buttons, nav links, cart icon, badge close) minimum 44×44px tap area
- Mobile nav hamburger and close icon both 48×48px with generous padding
- Cart drawer line-item quantity controls use 36px minimum height with `{spacing.md}` gap between adjacent controls
- Footer links padded to 40px vertical tap target despite 14px type size

### Collapsing Strategy

- Navigation: full horizontal link bar collapses to hamburger icon at < 744px; cart icon always visible
- Hero: two-column CTA layout stacks to single column below 744px; image crops from landscape to portrait using `object-position: center top`
- Spec table: switches from row (label + value inline) to card (label stacked above value) below 744px
- Product grid: 4 → 3 → 2 → 1 column at wide / desktop / tablet / mobile breakpoints
- Announcement bar: multi-message static display on desktop; auto-scrolling single ticker on mobile to save height

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact canvas background color not extracted — white `#ffffff` assumed; the site may use a very light off-white or dark-mode default canvas that wasn't captured
- `winco` font-family usage could not be confirmed — font identified in stack but no rendered specimen observed; may be a fallback or icon font
- Exact border-radius values on product image containers not confirmed from extraction; `{rounded.xs}` (4px) is an inference from the industrial visual register
- Hover and focus states for text inputs and nav links are inferred from brand conventions, not observed in live extraction
- Mobile navigation drawer interior colors (background, link color, close icon color) not confirmed — dark variant assumed from nav bar palette
- No explicit dark-mode or light-mode conditional tokens extracted; the heavy use of `#112233` canvas suggests single-mode dark-first design but is unconfirmed
- Product photography treatment (overlay opacity, blend mode) is estimated from visible contrast ratios; exact values require browser devtools inspection
- `magnesium-mvb` / `magnesium-mvb-condensed` are licensed web fonts; exact weight variants available (e.g., whether a `400` weight exists) are not confirmed from extraction alone
