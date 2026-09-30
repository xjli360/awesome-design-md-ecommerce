---
version: alpha
name: "Carbide 3D"
source_url: "https://www.carbide3d.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep indigo (#3e34d3) as the primary action voltage is an unusual frequency for a CNC hardware company — it reads closer to a developer tool or productivity SaaS than a shop-floor machine catalog, and that dissonance is deliberate. Carbide 3D sells desktop routers and laser cutters to an audience that writes G-code and reads stack traces as fluently as they read grain direction in walnut, and the color system meets them there. Near-black backgrounds at #000309 and #23263b create a dark-mode-first shell where the indigo accent fires with near-LED intensity; #5468ff handles hover and active states with a cooler, brighter push upward on the spectrum. Muted purple-grays at #7777a3 and #807ea3 bridge the chromatic interval between deep dark surfaces and lighter canvas zones — the entire palette is rooted in violet rather than the safety orange or industrial red common to workshop hardware brands. Even the off-white at #f5f5fa carries a ghost of indigo, tinting every rest-state surface with the brand frequency. Typography extracted only as inherit, suggesting a runtime-loaded geometric sans-serif or a system-UI stack throughout. The visual register leans dense and legible — display lines carry weight without theatrical sizing, and machine spec rows demand density-tolerant readability over headline drama. Corner radii stay in the {rounded.xs} to {rounded.md} range, enough to read as contemporary product UI without mimicking the pill-heavy friendliness of lifestyle-consumer brands. Primary CTAs sit at {rounded.sm}, crisp but not aggressive. A persistent dark header at {colors.surface-nav} makes the indigo {colors.primary} button the only warm-spectrum light source in the chrome zone. The site alternates deliberately between dark hero bands at {colors.surface-dark} and white content sections at {colors.canvas}, producing a cadence that separates marketing claims from technical data. Machine listing pages carry dense spec tables in monospace; Carbide Create and Carbide Motion software pages carry workflow diagrams and tutorial callouts. Two distinct audiences — makers who want to start cutting today, and businesses evaluating floor capacity — are served by the same system of surface alternation, indigo action hierarchy, and type scale calibrated for specification density.

colors:
  primary: "#3e34d3"
  primary-active: "#5468ff"
  primary-disabled: "#7777a3"
  ink: "#262627"
  body: "#2c2e40"
  muted: "#777777"
  muted-alt: "#797979"
  muted-purple: "#807ea3"
  accent-purple: "#7777a3"
  slate: "#969faf"
  hairline: "#eaeaea"
  canvas: "#ffffff"
  surface-soft: "#f5f5fa"
  surface-card: "#ffffff"
  surface-dark: "#23263b"
  surface-nav: "#000309"
  surface-deep: "#262627"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-dark-muted: "rgba(255,255,255,0.60)"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label-upper:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-value:
    fontFamily: "'SF Mono', 'Fira Code', 'Consolas', monospace"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px

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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    transition: background-color 150ms ease
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.6
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    border: "1.5px solid rgba(255,255,255,0.40)"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
    height: auto
  button-ghost-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.surface-nav}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    padding: 0 32px
    borderBottom: none
  nav-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    paddingX: "{spacing.md}"
    hoverColor: "{colors.primary-active}"
  nav-dropdown:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    borderTop: "2px solid {colors.primary}"
    padding: 24px 32px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    imageRatio: "4/3"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
    shadow: "0 2px 8px rgba(62,52,211,0.06)"
  product-card-hover:
    shadow: "0 6px 24px rgba(62,52,211,0.12)"
    borderColor: "{colors.accent-purple}"
  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: 80px 0
  hero-dark-band:
    backgroundColor: "{colors.surface-nav}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: 80px 0
  software-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  category-label:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
    border: "1px solid {colors.hairline}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rowPadding: 10px 16px
    accentBar: "3px solid {colors.primary}"
  spec-row-alt:
    backgroundColor: "{colors.canvas}"
  feature-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    accentBar: "3px solid {colors.primary}"
    border: "1px solid {colors.hairline}"
  cta-band:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    padding: 64px 32px
    alignment: center
  software-card:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid rgba(255,255,255,0.08)"
    padding: "{spacing.xl}"
    topAccent: "2px solid {colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  pagination-dot-active:
    backgroundColor: "{colors.primary}"
    size: 8px
    rounded: "{rounded.full}"
  pagination-dot-inactive:
    backgroundColor: "{colors.hairline}"
    size: 8px
    rounded: "{rounded.full}"
  tag-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  footer:
    backgroundColor: "{colors.surface-nav}"
    textColor: "{colors.on-dark-muted}"
    linkColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: 64px 0

---

## Components

### Buttons

**`button-primary`** — Solid indigo (#3e34d3) fill at 44px height with `{rounded.sm}` (4 px) corners and a white label in `{typography.button-md}` (15 px / 600 weight). On hover or focus, the background transitions 150ms to `{colors.primary-active}` (#5468ff), a perceptibly cooler and brighter indigo that signals responsiveness without leaving the brand's hue family. The disabled state uses `{colors.primary-disabled}` at 60% opacity with a `not-allowed` cursor. This button anchors every machine page CTA, software download prompt, and add-to-cart flow.

**`button-secondary`** — Transparent fill with a 1.5 px border and label both in `{colors.primary}`, same 44px height. Pairs with `button-primary` in hero and landing sections. On dark surfaces (`{colors.surface-dark}`, `{colors.surface-nav}`), the `button-secondary-dark` variant swaps to 40%-opacity white border and `{colors.on-dark}` label to remain legible against deep backgrounds.

**`button-ghost`** and **`button-ghost-dark`** — Text-only, no border, no fill. Used for secondary navigation actions, "Learn More" links inside spec tables, and comparison flows where button chrome would add clutter. Ghost-dark variant applies on dark surface bands.

### Nav Bar

**`nav-bar`** — Persistent near-black header at `{colors.surface-nav}` (#000309), 60 px tall. Navigation links render in `{colors.on-dark}` at `{typography.nav-link}` (14 px / 500 weight), with hover states pushing to `{colors.primary-active}`. The right-aligned `button-primary` ("Shop" or category CTA) is the only indigo element in the chrome zone, making it immediately legible as the action destination against the void background. Sub-menus drop as full-width `nav-dropdown` panels with a `{colors.surface-deep}` background and a 2 px `{colors.primary}` top border accent. On mobile, links collapse behind a hamburger icon (44×44 px touch target) into a slide-in drawer.

### Product Card

**`product-card`** — White `{colors.canvas}` card, 1 px `{colors.hairline}` border, `{rounded.md}` (8 px) corners, and a subtle `rgba(62,52,211,0.06)` shadow that warms slightly toward indigo. Machine imagery fills a 4:3 image container flush at card top with no padding. Below the image: machine name in `{typography.title-md}`, a one-line descriptor in `{typography.body-sm}` at `{colors.muted}`, and price in `{typography.price-display}` (20 px / 700). A `software-badge` ("Carbide Create") may overlay the image corner. Hover state lifts the shadow and shifts the border to `{colors.accent-purple}`, giving a controlled indigo-family focus response without full fill color change.

### Hero Section

**`hero-section`** — Full-width band at `{colors.surface-dark}` (#23263b), 80 px vertical padding. Headline in `{typography.display-xl}` (52 px / 700 / −0.5 px tracking) in `{colors.on-dark}`, supporting copy in `{typography.body-md}`, followed by a horizontal pair of `button-primary` + `button-secondary-dark`. Machine photography sits right-aligned on desktop, stacking below copy on mobile. The dark surface makes the indigo CTA appear luminous, functioning as a visual lighthouse on the page.

**`hero-dark-band`** — A deeper variant at `{colors.surface-nav}` (#000309) for above-the-fold homepage placement and product launch banners. Same type treatment, greater tonal depth. The indigo button contrast ratio is highest here, producing maximum visual weight for conversion-critical placements.

### Software Badge

**`software-badge`** — Compact label in `{typography.label-upper}` (11 px / 700 / 1.2 px tracking, all-caps) in `{colors.on-primary}` on `{colors.primary}` fill, `{rounded.xs}` (2 px). Appears on product cards to call out bundled software ("Carbide Create", "Carbide Motion"), in nav dropdowns as product identifiers, and on software landing pages as section anchors. The `category-label` variant uses `{colors.surface-soft}` background and `{colors.body}` text for neutral product categorization tags.

### Spec Table

**`spec-table`** — Two-column definition table on `{colors.surface-soft}` (#f5f5fa) with `{rounded.md}` border and a 3 px left accent strip in `{colors.primary}`. Left column: spec label in `{typography.spec-label}` (13 px / 400) at `{colors.muted}`. Right column: spec value in `{typography.spec-value}` (13 px / 500, monospace) at `{colors.ink}` — the monospace choice signals technical precision and makes mm/rpm/watt values align cleanly across rows. Alternating rows (`spec-row-alt`) flip to `{colors.canvas}` white for scanability in long machine specs. On mobile the table scrolls horizontally with a right-side fade shadow.

### Feature Callout

**`feature-callout`** — Light-surface card on `{colors.surface-soft}`, `{rounded.md}`, 1 px `{colors.hairline}` border, and a 3 px left accent bar in `{colors.primary}`. Title in `{typography.title-md}`, body in `{typography.body-sm}` at `{colors.body}`. Used in software feature grids (toolpath library callouts for Carbide Create, probing wizard highlights for Carbide Motion) and accessory detail sections. Typically deployed in three-column grids on desktop with the indigo left bar providing horizontal rhythmic punctuation across the row.

### CTA Band

**`cta-band`** — Full-width dark section at `{colors.surface-dark}`, centered headline in `{typography.display-sm}` (24 px / 600) in `{colors.on-dark}`, supporting line in `{typography.body-md}` at `{colors.on-dark-muted}`, then a centered `button-primary`. Appears between product category sections to re-assert brand identity within white catalog zones and before footer. Padding 64 px vertical, 32 px horizontal.

### Software Card

**`software-card`** — Used on Carbide Create and Carbide Motion product pages. Dark `{colors.surface-dark}` background, subtle `rgba(255,255,255,0.08)` border, `{rounded.md}`, and a 2 px `{colors.primary}` top border accent that distinguishes each product within the software family. Software icon or interface screenshot at top, product name in `{typography.title-md}` in `{colors.on-dark}`, descriptor in `{typography.body-sm}` at `{colors.on-dark-muted}`. Download and "Learn More" CTAs appear as `button-primary` and `button-ghost-dark` pair.

### Footer

**`footer`** — Near-black `{colors.surface-nav}` (#000309) with full `{colors.on-dark}` white link text and `{colors.on-dark-muted}` (60% white) body copy. Four-column link grid (Machines / Software / Accessories / Support) on desktop, single-column labeled sections on mobile. Logo sits top-left; social icons and legal links bottom-right. Typography at `{typography.body-sm}`. The footer shares the same surface as the nav bar, bookending the page with identical dark-indigo-system endpoints.

### Breadcrumb & Pagination

**`breadcrumb`** — Inline `{typography.caption}` (12 px) links in `{colors.muted}` separated by `{colors.hairline}` chevrons, active segment in `{colors.ink}`. Appears on machine detail and software pages to support navigation depth.

**`pagination-dot-active`** / **`pagination-dot-inactive`** — 8 px circles, `{rounded.full}`. Active in `{colors.primary}` indigo, inactive in `{colors.hairline}`. Used in machine image carousels and software screenshot sliders.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger drawer; hero stacks copy above machine image; spec tables get horizontal scroll with right-fade indicator; product card grid 1-up; feature callout grid 1-up; cta-band padding reduces to 40px 16px; footer collapses to labeled accordions |
| Tablet | 744–1128px | Nav shows primary product links, hides tertiary; product card grid 2-up; hero shifts to side-by-side at upper end of breakpoint; feature callout grid 2-up; spec table max-width 480px; footer 2-column |
| Desktop | 1128–1440px | Full nav with dropdown capability; product card grid 3-up; hero fully side-by-side with large machine imagery; feature callout grid 3-up; software card grid 2-up; spec table 560px max-width; footer 4-column |
| Wide | > 1440px | Content max-width 1280px centered with auto horizontal margins; hero image scales proportionally; additional whitespace added to section padding (section + 16px); no additional grid columns |

### Touch Targets

- All interactive buttons minimum 44px tall (matches `button-primary` height)
- Nav hamburger icon minimum 44×44 px touch area regardless of visual icon size
- Product card entire surface is clickable, not just the CTA button
- Spec table rows are non-interactive; parent card or page handles navigation
- Pagination dots minimum 32px touch target despite 8px visual size (via invisible padding)

### Collapsing Strategy

- Primary navigation collapses to a slide-in drawer on mobile, ordered by purchase priority: Machines → Software → Accessories → Support → About
- Feature callout three-column grids stack vertically on mobile; dense software feature lists may accordion-expand on tap
- Spec tables that exceed viewport width receive horizontal scroll containers with a right-shadow overflow indicator
- Hero side-by-side layout collapses to stacked copy-then-image below 744px; image may be cropped to 16:9 in the mobile stack
- Nav dropdowns are replaced by accordion sections inside the mobile drawer
- Footer four-column link grid collapses to labeled accordion sections to prevent excessive vertical scrolling

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Font family**: Extraction returned only `inherit` — the actual typeface loaded at runtime (likely Inter, DM Sans, or a custom geometric sans-serif) could not be identified. All typography tokens default to `system-ui` as a safe fallback; verify against the live site's computed styles.
- **Exact border radii**: Corner radius values are inferred from the dark/technical aesthetic and visual register; live DOM values require inspector verification.
- **Dark-mode toggle**: The site uses dark surfaces and white sections but whether a CSS `prefers-color-scheme` dark mode or user-toggled dark mode is implemented is unconfirmed.
- **Icon system**: No icon library, sprite, or glyph set was extractable — Carbide 3D likely uses a custom SVG set for machine navigation, software callouts, and feature icons.
- **Animation tokens**: Transition durations and easing functions (used on CTA hover states, hero imagery, and carousels) were not captured.
- **Pricing display treatment**: The exact type treatment for machine pricing ($1,299–$3,000+ range) including sale/discount callout colors (likely indigo or a red accent) is unconfirmed.
- **Meta theme-color**: Not set — no PWA or pinned-tab branding configured.
- **Secondary accent palette depth**: Whether #7777a3 / #807ea3 appear as interactive elements (tag hovers, secondary links) or purely as decorative muted tones requires live-site verification.
- **Email/newsletter input**: Subscription form styling (present in most e-commerce footers) not confirmed from extraction.
