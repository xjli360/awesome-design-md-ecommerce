---
version: alpha
name: "Dino-Lite"
source_url: "https://www.dinolite.us"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The amber (#f5b301) in Dino-Lite's palette reads like a calibration mark on a precision instrument — a single warm frequency against a field of blues and grays that would otherwise read as pure technical infrastructure. Two blues do the structural work: an electric cornflower (#1863dc) handles every primary CTA, active nav state, and interactive affordance, while a deep navy (#034574) anchors section headers, hero backgrounds, and structural chrome. Together they form a hierarchy that mirrors how microscopy professionals parse information — high-contrast foreground signal against a stable, neutral working surface.

  Surface layers are built from a family of near-whites (#f7f7f7, #f4f4f4, #eff1f3) that sit neither paper-white nor gray, neutral enough that product photography retains full chromatic authority. Ink hits #212121, body text drops to #2b2b2b and #555555 for hierarchy, and a muted purple-gray (#4e4b66) surfaces for secondary metadata — a subtle departure from straight grays that prevents the interface from reading as purely utilitarian. Typography runs the OS cascade with Roboto at the front, choosing rendering consistency over custom-font personality: body copy sits at 14–16px weight 400, section headers move to 20–24px at weight 600–700 without the dramatic scale jumps consumer lifestyle brands favor.

  Corners stay small and consistent — `{rounded.xs}` to `{rounded.sm}` across buttons, cards, and inputs. No pill-shaped CTAs, no soft organic radii; the system geometry matches the machined-tolerance aesthetic of the instruments themselves. Product cards carry the full specification load: magnification range, resolution, connectivity type, and application domain (PCB inspection, dermatology, gemology, forensics, education) all visible without a secondary click. The cyan accent (#0ac3ec) surfaces on interactive overlays and comparison highlights, while a sky-blue (#33b2ff) handles selection rings and secondary link states — a three-blue system that would be chaotic in any consumer context except the technical instrument catalog, where professional buyers are trained to read multi-variable data simultaneously. Promotional callouts and featured-spec badges take the amber, letting a single warm token do the attention work that other brands assign to red.

colors:
  primary: "#1863dc"
  primary-dark: "#034574"
  primary-active: "#003388"
  primary-disabled: "#d1eaff"
  accent-amber: "#f5b301"
  accent-cyan: "#0ac3ec"
  accent-sky: "#33b2ff"
  accent-periwinkle: "#9999ff"
  ink: "#212121"
  body: "#2b2b2b"
  muted: "#555555"
  muted-soft: "#858585"
  muted-meta: "#4e4b66"
  hairline: "#e2e2e2"
  hairline-soft: "#eaeaea"
  border: "#bdc3c7"
  silver: "#d0d5d2"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#f4f4f4"
  surface-muted: "#eff1f3"
  surface-blue: "#d1eaff"
  on-primary: "#ffffff"
  success: "#008000"

typography:
  display-xl:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-blue}"
    textColor: "{colors.primary-active}"
    border: "1.5px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeLinkColor: "{colors.primary}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.xl}"
  nav-bar-mobile:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-primary}"
    height: 56px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    subtextColor: "{colors.muted}"
    metaColor: "{colors.muted-meta}"
    linkColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  hero-banner:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-primary}"
    accentColor: "{colors.accent-amber}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  spec-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  application-tag:
    backgroundColor: "{colors.surface-blue}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  category-filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  category-filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  product-compare-row:
    backgroundColor: "{colors.surface-soft}"
    alternateBackgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  breadcrumb:
    textColor: "{colors.muted}"
    linkColor: "{colors.primary}"
    separatorColor: "{colors.border}"
    typography: "{typography.caption}"
  alert-banner:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.xl}"
  tab-nav:
    backgroundColor: "{colors.canvas}"
    activeTextColor: "{colors.primary}"
    inactiveTextColor: "{colors.muted}"
    activeBorderColor: "{colors.primary}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.title-sm}"
  footer:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.surface-blue}"
    sectionHeadTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  success-indicator:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 8px

## Components

### Buttons
**`button-primary`** — Solid electric blue (`{colors.primary}`) rectangle with `{rounded.sm}` radius and white label at 15px weight 500. Height locks at 44px. Hover deepens to `{colors.primary-active}` with no shadow; disabled state uses pale blue wash `{colors.primary-disabled}` with `{colors.muted}` text. Reserved for transactional CTAs: "Add to Cart", "Get a Quote", "Download Software" — never for navigation or secondary actions.

**`button-secondary`** — White fill with a 1.5px `{colors.primary}` border and blue label matching primary in height and radius. Hover fills `{colors.surface-blue}` while the border shifts to `{colors.primary-active}`. Appears paired with primary in product detail pages (primary = buy, secondary = compare or download datasheet).

**`button-ghost`** — Transparent background, `{colors.primary}` text only, `{typography.button-sm}`. Used for inline text-links that need a button affordance without visual weight: "View all accessories", "See full specs", "Load more results".

### Search
**`search-bar`** — Single-line input with `{rounded.sm}` radius joined to a solid `{colors.primary}` submit button carrying a magnifier icon in `{colors.on-primary}`. The input takes `{colors.canvas}` fill with `{colors.hairline}` border shifting to `{colors.primary}` on focus. Appears in the top nav and at the head of catalog pages; width expands to full-bleed on mobile.

### Navigation
**`nav-bar`** — White canvas, 64px tall, with a 1px `{colors.hairline}` bottom border. Brand wordmark anchored left, mega-menu product links centered in `{typography.nav-link}` highlighting `{colors.primary}` on active hover, search and cart icons right-anchored. Drops a full-width panel for application-domain columns (Industrial, Medical, Education, Research) with thumbnail product rows per domain.

**`tab-nav`** — Horizontal tab row on product detail pages separating Specifications, Downloads, Applications, and Gallery. Active tab shows a 2px `{colors.primary}` bottom indicator and `{colors.primary}` text label; inactive tabs render in `{colors.muted}`. Full-width bottom border in `{colors.hairline}` provides the baseline.

### Product Card
**`product-card`** — `{rounded.sm}` card on `{colors.surface-card}` with a 1px `{colors.hairline}` border. Top: square-cropped product image at full card width. Below: product name in `{typography.title-md}`, model number in `{typography.caption}` at `{colors.muted-meta}`, a row of `application-tag` pill chips, then magnification range and resolution rendered in `{typography.spec-label}` uppercase formatting. A `{colors.primary}` "View Details" link anchors the bottom. Featured units carry a `{colors.accent-amber}` `spec-badge` overlaid in the top-right corner of the image.

### Hero Banner
**`hero-banner`** — Full-width deep navy (`{colors.primary-dark}`) section. Headline in `{typography.display-xl}` at `{colors.on-primary}`, supporting copy in `{typography.body-md}`, and a `{colors.accent-amber}` accent stripe or badge callout for the promotion or product family name. CTA renders as `button-primary` on the dark surface. Product photography or illustrated microscope render floats right on desktop, stacks below text on mobile.

### Spec & Application Badges
**`spec-badge`** — Small amber rectangle with `{rounded.xs}` corners and `{typography.badge}` text in `{colors.ink}`. Applied directly over product card images for "NEW", "POPULAR", or key-spec callouts like "5MP". Amber was chosen over red so the badge reads informational rather than error-adjacent — consistent with the instrument-grade vocabulary.

**`application-tag`** — Soft blue pill (`{colors.surface-blue}` fill, `{colors.primary}` text) on `{rounded.full}` with `{typography.badge}` label. One to four appear below each product card name communicating domain use: PCB Inspection, Dermatology, Gemology, Forensics, Education, Quality Control.

### Filters
**`category-filter-chip`** / **`category-filter-chip-active`** — Pill-shaped filter tokens for catalog pages. Inactive: `{colors.surface-soft}` fill, `{colors.hairline}` border, `{colors.ink}` text. Active: fills `{colors.primary}` with `{colors.on-primary}` text. Rendered as a horizontal-scroll row on mobile; left-rail panel at fixed width on desktop.

### Comparison Table
**`product-compare-row`** — Alternating-stripe table for side-by-side spec comparison. Row headers use `{typography.spec-label}` (uppercase, 11px, bold) in the first column; values use `{typography.body-sm}`. Rows alternate between `{colors.surface-soft}` and `{colors.canvas}`; dividers in `{colors.hairline}`.

### Alert / Promo Banner
**`alert-banner`** — Full-width amber (`{colors.accent-amber}`) strip pinned to the top of the viewport for site-wide promotions, free-shipping thresholds, or new-product launches. Copy in `{typography.body-sm}` at `{colors.ink}`, center-aligned. Dismissible via an X icon at the far right.

### Footer
**`footer`** — Deep navy (`{colors.primary-dark}`) multi-column layout. Section headers in `{typography.title-sm}` at `{colors.on-primary}`; links in `{typography.body-sm}` at `{colors.surface-blue}` for contrast on dark. Columns: Products, Applications, Support, About, Distributors. Bottom bar carries legal copy and social icons in `{typography.caption}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; horizontal-scroll filter chips replace left panel; hamburger nav opens `{colors.primary-dark}` drawer; hero stacks text above image |
| Tablet | 744–1128px | Two-column product grid; mega-menu collapses to icon-plus-label row; filter panel slides in as overlay sheet |
| Desktop | 1128–1440px | Three-column product grid; full horizontal mega-menu visible; left-rail filter panel on by default; hero splits text/image 50/50 |
| Wide | > 1440px | Container max-width 1400px centered with `{colors.canvas}` gutters; four-column grid unlocks for accessories catalog |

### Touch Targets
- All interactive elements (buttons, filter chips, nav icons, tab items) maintain minimum 44×44px hit area on touch viewports
- Filter chips expand vertical padding to `{spacing.base}` on mobile to prevent mis-taps during scroll
- Product card tap target covers the full card face below 744px; no separate "View Details" link tap needed

### Collapsing Strategy
- Desktop left-rail filter panel collapses to a horizontal-scroll strip pinned above the product grid on mobile
- Mega-menu product domain columns collapse to nested accordion rows in the mobile drawer
- Spec comparison table scrolls horizontally on mobile with the first column (spec label) sticky
- Application-tag rows on product cards wrap freely; excess tags hidden behind a "+N more" chip on cards narrower than 320px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected — typography resolves to the system cascade (Roboto + OS fallbacks); a custom display font is not confirmed and may not exist
- Exact button border-radius not measured directly; `{rounded.sm}` (8px) inferred from general blue-rectangle CTA aesthetic
- Hover/focus animation timing and easing curves not extractable from static color extraction
- Dark-mode support status unknown; no `prefers-color-scheme` signals present in extracted tokens
- Icon set identity unclear — both FontAwesome and a custom `asppsicons2` font detected; which icons map to which UI roles is unconfirmed
- Role of `#9999ff` (periwinkle) and `#0073aa` not confirmed; both may originate from a CMS admin layer or third-party plugin rather than the brand's public-facing UI
- Product configurator interaction model (dropdowns vs. swatches vs. filter chips) not verifiable from extraction alone
- Exact mega-menu column structure and link hierarchy not verified against live DOM
