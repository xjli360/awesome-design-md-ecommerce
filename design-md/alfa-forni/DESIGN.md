---
version: alpha
name: "Alfa Forni"
source_url: "https://www.alfaforni.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep burgundy (#990521) burns through every call-to-action like the mouth of a wood-fired dome at peak temperature — a color closer to aged Montepulciano than the predictable tomato-red most oven brands default to. Alfa Forni's digital presence pairs this wine-dark primary with a secondary flame red (#d0382e) reserved for urgency states, sale callouts, and hover accents, creating a two-tone heat gradient that mirrors the thermal spectrum inside a 500°C chamber. The typographic system leans on Montserrat for display and navigational weight — its geometric openness at 700 weight reads industrial-Italian, the kind of lettering stamped into cast-iron doors — while Inter handles body copy at 400/500 weights, lending the dense spec sheets and temperature guides the mechanical clarity they demand. A custom `alfaforni` webfont appears on logo lockups and select hero headlines, giving display moments a proprietary silhouette. Surfaces stay neutral: a warm off-white canvas (#f5f5f5) sits behind product grids, while true-white (#ffffff) cards with `{rounded.sm}` corners float above it carrying individual oven models. Terracotta brown (#755847) anchors footer regions and "Made in Italy" heritage badges, referencing refractory brick without illustration. Navigation is dark (#212934) with generous `{spacing.lg}` between mega-menu categories (Wood, Gas, Hybrid, Accessories), and the mobile hamburger collapses into a full-screen overlay at that same near-black. Buttons run at 48px height with `{rounded.xs}` — barely softened rectangles that feel stamped rather than friendly, appropriate for a product that weighs 60kg and ships on a pallet. Spacing follows a compact European editorial rhythm: `{spacing.md}` gutters between product cards, `{spacing.section}` vertical breathing between lifestyle photography bands. The overall impression is a professional tools catalog dressed in winemaker's clothing — functional grids, restrained animation, and that singular burgundy pulse.

colors:
  primary: "#990521"
  primary-active: "#7a0419"
  primary-disabled: "#cc9aa6"
  flame: "#d0382e"
  flame-bright: "#de4528"
  heritage-blue: "#003399"
  terracotta: "#755847"
  ink: "#222222"
  ink-soft: "#212934"
  body: "#3e3e3e"
  muted: "#777777"
  muted-light: "#555555"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  border-mid: "#c3c3c3"
  canvas: "#ffffff"
  canvas-warm: "#f5f5f5"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-gray: "#efefef"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  nav-dark: "#212934"
  footer-bg: "#363636"
  accent-blue: "#446bb2"

typography:
  display-xl:
    fontFamily: "'alfaforni', 'Montserrat', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.37
    letterSpacing: 0
  body-lg:
    fontFamily: "'Inter', 'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Inter', 'Open Sans', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  price:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.border-mid}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  button-flame:
    backgroundColor: "{colors.flame}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.border-mid}"
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.xl}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.06)"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.10)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    backgroundColor: "{colors.canvas-warm}"
    rounded: "{rounded.xs}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section-lg} {spacing.xl}"
    minHeight: 560px
  hero-subtitle:
    typography: "{typography.body-lg}"
    textColor: "{colors.on-dark}"
    opacity: 0.85
  heritage-badge:
    backgroundColor: "{colors.terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  fuel-type-badge:
    backgroundColor: "{colors.surface-gray}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.ink}"
  temperature-indicator:
    backgroundColor: "{colors.flame}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.full}"
    height: 56px
    width: 56px
  category-nav-pill:
    backgroundColor: "{colors.surface-gray}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
  category-nav-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  comparison-table-header:
    backgroundColor: "{colors.canvas-warm}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.border-mid}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"

---

## Components

### Buttons

**`button-primary`** — A solid burgundy (#990521) rectangle with barely-rounded corners (`{rounded.xs}`) and uppercase Montserrat 600 tracking at 0.3px. On hover, darkens to `{colors.primary-active}` with no scale transform — the interaction is color-only, staying industrial. Disabled state washes to a muted rose (`{colors.primary-disabled}`). Used for "Add to Cart," "Configure Your Oven," and primary form submissions.

**`button-secondary`** — White fill with a `{colors.border-mid}` stroke, same height and radius as primary. Hover thickens border to ink-black and fills with `{colors.surface-soft}`. Paired alongside primary for "Compare Models" or "Download Specs" secondary actions.

**`button-flame`** — A brighter fire-red (#d0382e) variant reserved for promotional banners, limited-time offers, and sale CTAs. Same structural dimensions as primary but signals urgency through the warmer hue.

### Navigation

**`nav-bar`** — Fixed 72px white bar with a single-pixel bottom hairline. Logo (custom alfaforni font) sits left; mega-menu triggers sit center in `{typography.nav-link}` (Montserrat 500, 14px). Right side holds search icon, locale selector, and cart. On scroll, the hairline drops away and a subtle box-shadow takes over (`nav-bar-scrolled`).

**`mega-menu`** — Full-width dropdown with `{spacing.xl}` internal padding. Three to four columns: product categories with thumbnail images (Wood-Fired, Gas, Hybrid), a featured product spotlight, and a support/resource links column. White background, soft shadow below.

**`category-nav-pill`** / **`category-nav-pill-active`** — Horizontal scrollable pill row filtering product grids by fuel type or size. Inactive pills sit in `{colors.surface-gray}` with full radius; active pill snaps to `{colors.primary}` with white text.

### Product Cards

**`product-card`** — White card on the warm canvas, `{rounded.sm}` corners, and a delicate 1px `{colors.hairline-soft}` border. Image area uses a 4:3 ratio container with `{colors.canvas-warm}` placeholder. Below: product name in `{typography.title-sm}`, fuel-type badge, and price in `{typography.price}` colored `{colors.primary}`. Hover lifts the card shadow and darkens the border.

**`product-card-price`** — Price rendered in Montserrat 700 at 20px, colored in the primary burgundy to draw the eye without a separate badge.

### Hero

**`hero-section`** — Full-bleed dark background (often a lifestyle photograph of an oven in an outdoor kitchen) with overlaid white display text at `{typography.display-xl}`. Minimum 560px height ensures cinematic proportion. A subtitle line in `{typography.body-lg}` at 85% opacity sits below, followed by a primary CTA button.

### Badges & Indicators

**`heritage-badge`** — Small terracotta (#755847) label with `{typography.badge}` uppercase text, used for "Made in Italy," "Since 1977," or material callouts like "Refractory Brick." Tight `{rounded.xs}` corners.

**`fuel-type-badge`** — Pill-shaped (`{rounded.full}`) neutral badge on product cards indicating "Wood," "Gas," or "Hybrid" fuel source. Light gray fill, body-colored text.

**`temperature-indicator`** — Circular 56px element in flame-red (#d0382e) displaying max temperature ratings (e.g., "500°C") in `{typography.title-md}`. Used in spec comparison grids.

### Specification Tables

**`spec-table-row`** — Alternating-implied row with bottom hairline separator. Label column uses `{typography.spec-label}` (Inter 600, 13px) while value column uses `{typography.body-sm}`. Padding at `{spacing.md}` vertical keeps rows scannable without feeling cramped.

**`comparison-table`** — Multi-column table with a warm header row (`{colors.canvas-warm}`), used to compare 2-4 oven models side by side. Rounded container, hairline border, and `{typography.title-sm}` column headers.

### Search

**`search-bar`** — Pill-shaped (`{rounded.full}`) input with a subtle outer shadow. Placeholder text in `{colors.muted}`, input text in `{colors.ink}`. On focus, border transitions to `{colors.primary}`.

### Footer

**`footer`** — Dark charcoal (#363636) full-width footer with section-level padding. Column headings in `{typography.title-sm}` white, link lists in `{typography.body-sm}` with reduced opacity. Bottom bar contains legal links, locale selector, and social icons.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid. Nav collapses to hamburger with full-screen dark overlay. Hero reduces to 360px min-height with display-md type. Category pills scroll horizontally. Comparison table becomes swipeable cards. |
| Tablet | 744–1128px | Two-column product grid. Mega-menu becomes a stacked accordion. Hero holds full height. Spec tables remain full-width. Footer shifts to 2×2 column layout. |
| Desktop | 1128–1440px | Three-column product grid. Full mega-menu visible on hover. Hero section at designed 560px. Side-by-side comparison table up to 3 models. |
| Wide | > 1440px | Content max-width caps at 1440px with auto margins. Four-column product grid. Hero imagery extends full bleed while text container stays centered at 1200px. |

### Touch Targets
- All interactive elements maintain 48px minimum touch height on mobile
- Product card tap area covers full card surface including image
- Category pills maintain 44px hit area with `{spacing.sm}` gaps between
- Mega-menu links spaced at `{spacing.lg}` vertical on touch devices

### Collapsing Strategy
- Navigation categories collapse into a slide-out drawer below 744px with accordion sub-menus
- Product comparison table converts to a horizontal swipe carousel on mobile, one model per viewport
- Spec tables maintain full width but allow horizontal scroll on narrow viewports
- Footer columns stack vertically with collapsible section headings on mobile
- Hero CTA buttons stack vertically below 480px with full-width stretch

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The custom `alfaforni` webfont could not be analyzed for metrics (weight range, OpenType features) — it is loaded as a proprietary asset
- No CSS custom properties or design-token file was extractable; colors are inferred from computed styles and may vary by page template
- Exact border-radius values on product cards could not be confirmed — `{rounded.sm}` (8px) is an informed estimate from visual inspection
- Animation/transition durations and easing curves were not captured
- The site appears built on WordPress/Avada; many of the extracted colors (#f78da7, #ff6900, #fcb900, #7bdcb5) are Gutenberg editor defaults and are excluded from the design system
- Icon system details (custom SVG set vs. Font Awesome 5 usage patterns) were not fully mapped
- Dark-mode or alternate theme states were not detected
- Exact breakpoint values are estimated from common Avada framework defaults rather than confirmed from source CSS
