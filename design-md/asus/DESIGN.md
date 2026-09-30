---
version: alpha
name: "Asus"
source_url: "https://www.asus.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Neon-gradient arcs sweeping from violet (#7761ff) through cyan (#37d5ff) to mint (#35f5cb) — that animated spectrum is the first thing that hits on asus.com, long before any product photo loads. The primary blue (#006ce1) carries CTAs, links, and interactive affordances, but it deliberately steps back from the hero stage, letting those gradient flourishes and full-bleed product photography own the viewport. Type is split between two distinct personalities: condensed bold faces like Kairos Sans Condensed Bold and FF DIN Condensed Bold slam product names and hero headlines into tight vertical columns, while TT Norms Pro handles body copy, navigation labels, and UI text with clean geometric curves at regular and medium weights. This duality — compressed energy for display, relaxed neutrality for reading — maps directly to the split audience of spec-obsessed enthusiasts and everyday laptop buyers. The layout sits on a near-black (#16151b) dark canvas for gaming and ROG sections, then flips to bright white with soft gray (#f5f5f5) surface cards for mainstream products, creating two tonal worlds within a single domain. Product cards use sharp `{rounded.xs}` corners and dense specification grids — no friendly pill shapes here. Buttons stay squared off at `{rounded.xs}` to `{rounded.sm}`, reinforcing a precision-engineered ethos. Spacing runs tighter than most consumer electronics sites: `{spacing.md}` between spec rows, `{spacing.lg}` between card groups, with `{spacing.section}` reserved only for major category breaks. A warm peach accent (#ffb980) and muted gold (#cdab82) surface in promotional badges and premium product tiers, providing just enough warmth to prevent the blue-and-dark palette from reading as sterile. The mega-navigation is a content-dense flyout that treats every product line as its own storefront, with thumbnail grids and comparison shortcuts baked directly into the nav layer. Hover states across the site rely on the lighter sky blue (#248dff) rather than simple opacity shifts, giving interactive elements a deliberate luminance bump against both dark and light backgrounds.

colors:
  primary: "#006ce1"
  primary-active: "#0051a8"
  primary-hover: "#248dff"
  primary-disabled: "#aecffa"
  ink: "#181818"
  ink-deep: "#16151b"
  body: "#4d4d4d"
  muted: "#818181"
  muted-soft: "#7f7f7f"
  subtle: "#616161"
  hairline: "#dcdcdc"
  hairline-soft: "#e1e1e1"
  border-mid: "#505050"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#16151b"
  surface-dark-elevated: "#262626"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-violet: "#7761ff"
  accent-indigo: "#535dff"
  accent-blue-mid: "#2659ff"
  accent-blue-bright: "#0a56ff"
  accent-sky: "#1e9cff"
  accent-cyan: "#37d5ff"
  accent-aqua: "#36d9f8"
  accent-teal: "#36e4e5"
  accent-mint: "#35f5cb"
  accent-warm: "#ffb980"
  accent-gold: "#cdab82"
  accent-soft-blue: "#aecffa"
  accent-soft-teal: "#add3e2"

typography:
  display-xl:
    fontFamily: "'KairosSansCondensedBold', 'FFDINCondensedBold', Impact, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'KairosSansCondensedBold', 'FFDINCondensedBold', Impact, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
    textTransform: uppercase
  display-md:
    fontFamily: "'KairosSansCondensedBold', 'FFDINCondensedBold', Impact, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: 0
    textTransform: uppercase
  title-lg:
    fontFamily: "'TTNormsProMedium', 'TT Norms Pro', Roboto, 'Segoe UI', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'TTNormsProMedium', 'TT Norms Pro', Roboto, 'Segoe UI', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'TTNormsProMedium', 'TT Norms Pro', Roboto, 'Segoe UI', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'TTNormsProRegular', 'TT Norms Pro', Roboto, 'Segoe UI', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'TTNormsProRegular', 'TT Norms Pro', Roboto, 'Segoe UI', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'TTNormsProRegular', 'TT Norms Pro', Roboto, 'Segoe UI', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "'TTNormsProMedium', 'TT Norms Pro', Roboto, 'Segoe UI', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'TTNormsProRegular', 'TT Norms Pro', Roboto, 'Segoe UI', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  spec-value:
    fontFamily: "'TTNormsProMedium', 'TT Norms Pro', Roboto, 'Segoe UI', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  price-display:
    fontFamily: "'TTNormsProMedium', 'TT Norms Pro', Roboto, 'Segoe UI', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: -0.2px
  button-md:
    fontFamily: "'TTNormsProMedium', 'TT Norms Pro', Roboto, 'Segoe UI', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'TTNormsProMedium', 'TT Norms Pro', Roboto, 'Segoe UI', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'TTNormsProMedium', 'TT Norms Pro', Roboto, 'Segoe UI', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  promo-tag:
    fontFamily: "'KairosSansCondensedBold', 'FFDINCondensedBold', Impact, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  badge-label:
    fontFamily: "'TTNormsProMedium', 'TT Norms Pro', Roboto, 'Segoe UI', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: 0.2px

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
    padding: 10px 24px
    height: 40px
    borderWidth: 0
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 23px
    height: 40px
    borderWidth: 1px
    borderColor: "{colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
  button-ghost-on-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    borderWidth: 1px
    borderColor: "{colors.on-dark}"
    padding: 9px 23px
    height: 40px
  button-dark-fill:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 40px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: 0 40px
  nav-bar-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
    borderBottom: 1px solid {colors.hairline}
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.xl}"
    boxShadow: 0 8px 32px rgba(0,0,0,0.12)
    borderTop: 2px solid {colors.primary}
  mega-menu-category-heading:
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.sm}"
  mega-menu-thumbnail:
    width: 80px
    height: 80px
    rounded: "{rounded.xs}"
    objectFit: contain
    backgroundColor: "{colors.surface-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    borderWidth: 1px
    borderColor: "{colors.hairline-soft}"
  product-card-hover:
    boxShadow: 0 4px 20px rgba(0,0,0,0.1)
    borderColor: "{colors.primary}"
  product-card-image:
    aspectRatio: 4/3
    objectFit: contain
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    maxLines: 2
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xxl}"
  hero-banner-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
    maxWidth: 640px
  hero-banner-subline:
    typography: "{typography.body-md}"
    textColor: "{colors.on-dark}"
    opacity: 0.85
    maxWidth: 480px
  hero-banner-gradient:
    background: "linear-gradient(135deg, {colors.accent-violet}, {colors.accent-indigo}, {colors.accent-cyan}, {colors.accent-mint})"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xxl}"
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  spec-badge-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  spec-badge-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  promo-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.promo-tag}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  promo-badge-warm:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.promo-tag}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  promo-badge-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.promo-tag}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    borderWidth: 0
  search-bar-dark:
    backgroundColor: "{colors.surface-dark-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    minHeight: 180px
    textAlign: center
  category-tile-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  category-tile-hover:
    backgroundColor: "{colors.canvas}"
    boxShadow: 0 4px 16px rgba(0,0,0,0.08)
  comparison-row:
    padding: "{spacing.md} 0"
    borderBottom: 1px solid {colors.hairline-soft}
  comparison-row-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
    width: 200px
  comparison-row-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  dark-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} 0"
  dark-section-heading:
    typography: "{typography.display-lg}"
    textColor: "{colors.on-dark}"
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  footer-heading:
    typography: "{typography.caption-bold}"
    textColor: "{colors.on-dark}"
    textTransform: uppercase
    marginBottom: "{spacing.md}"
  gradient-text:
    background: "linear-gradient(90deg, {colors.accent-violet}, {colors.accent-cyan}, {colors.accent-mint})"
    backgroundClip: text
    webkitTextFillColor: transparent
    typography: "{typography.display-lg}"
  badge-new:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink-deep}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  tab-bar:
    borderBottom: 2px solid {colors.hairline}
    gap: "{spacing.lg}"
  tab-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid {colors.primary}
    padding: "{spacing.md} 0"
  tab-inactive:
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.md} 0"

---

## Components

### Buttons

**`button-primary`** — Solid ASUS blue (#006ce1) fill with white text, using `{rounded.xs}` for a clean
squared-off look consistent with the brand's technical precision. On hover the fill shifts to a brighter
sky blue (`{colors.primary-hover}` / #248dff), providing a noticeable luminance lift. Active state deepens
to #0051a8. Disabled state uses a washed-out blue with reduced opacity.

**`button-secondary`** — Transparent background with a 1px blue border and blue text. On hover, the button
inverts to a filled primary state — background becomes `{colors.primary}` and text flips to white. This
fill-on-hover pattern is a signature ASUS interaction: outline at rest, solid on engagement.

**`button-ghost`** — No border, no background, dark text. Used for tertiary actions in toolbars and filter
strips. A subtle underline or background tint appears on hover.

**`button-ghost-on-dark`** — White text with a 1px white border against dark backgrounds. Common on hero
banners and ROG-themed sections where the primary blue would compete with gradient backgrounds.

**`button-dark-fill`** — Solid near-black (#181818) fill with white text. Used as the primary CTA in
light-themed product sections where the blue button would clash with blue-heavy product photography.

### Navigation

**`nav-bar`** — A 56px-tall persistent top bar on near-black (#16151b) with white text at
`{typography.nav-link}`. Houses the ASUS logo, product-line links, and utility icons (search, account,
cart). The dark nav bar is consistent across all sub-brands and never switches to a light variant.

**`nav-bar-secondary`** — A 48px white secondary bar that appears below the main nav on product category
pages. Carries sub-category tabs (e.g., "Gaming," "Business," "Creator") with a subtle bottom hairline
border.

**`mega-menu`** — Full-width dropdown on white canvas with a 2px blue top-border accent. Interior is
organized into columns with `{typography.title-sm}` category headings and 80×80px product thumbnails.
Product entries link directly to detail pages, with comparison shortcuts as text links beneath each group.
Box shadow at `0 8px 32px rgba(0,0,0,0.12)` gives the panel clear separation from page content.

### Product Card

**`product-card`** — White card with a 1px `{colors.hairline-soft}` border and `{rounded.xs}` corners.
Product image sits in a 4:3 container with `contain` fit and a soft gray (#f5f5f5) background, so every
laptop renders at a uniform size regardless of aspect ratio. Title uses `{typography.title-sm}` capped
at two lines. Price sits below in `{typography.price-display}`. On hover, a faint blue border and
drop shadow appear, inviting click-through.

### Hero Banner

**`hero-banner`** — Full-bleed section on `{colors.surface-dark}` with product photography covering
60-70% of the width. Headline in `{typography.display-xl}` (condensed uppercase) sits to one side, capped
at 640px width. A subline in `{typography.body-md}` at 85% opacity provides a one-sentence value prop.
CTA uses `button-ghost-on-dark` or `button-primary` depending on contrast needs.

**`hero-banner-gradient`** — Variant used for brand campaigns and new product launches. Background runs a
135-degree gradient from violet (#7761ff) through cyan (#37d5ff) to mint (#35f5cb). Product imagery is
composited over the gradient. Headlines may use `gradient-text` or remain white depending on contrast
requirements.

### Spec Badge

**`spec-badge`** — Small rounded-rectangle chip on `{colors.surface-soft}` that displays a key
specification. Label in `{typography.spec-label}` appears in muted gray; value directly below in
`{typography.spec-value}` in full ink. Used in rows of 4-6 beneath product images on detail pages
(e.g., "Display: 16" OLED," "Weight: 1.6 kg," "Battery: 90Wh").

### Promotional Badges

**`promo-badge`** — Small blue pill with white uppercase text at `{typography.promo-tag}`. Applied to
product cards and listing items for labels like "NEW," "HOT," and "BEST SELLER."

**`promo-badge-warm`** — Peach-orange (#ffb980) variant for time-sensitive promotions and seasonal sales.
Dark ink text ensures readability.

**`promo-badge-gold`** — Muted gold (#cdab82) for premium and limited-edition product lines.

### Search

**`search-bar`** — Pill-shaped (`{rounded.full}`) input on soft gray, 44px tall, no visible border. Sits
in the nav utility area and expands to a full overlay on focus. Placeholder text in `{colors.muted}`.

**`search-bar-dark`** — Dark-surface variant (#262626) for use within the dark nav bar. White text, no
border, same pill shape.

### Category Tile

**`category-tile`** — Rounded rectangle (`{rounded.sm}`) on `{colors.surface-soft}` with centered product
category icon and title in `{typography.title-md}`. Minimum height of 180px. On hover, background lightens
to white and a subtle shadow appears. Used on landing pages to route users into product verticals.

### Comparison Row

**`comparison-row`** — Horizontal rule-separated row for spec-comparison tables. Label column at 200px
width in muted `{typography.spec-label}`; value columns in `{typography.spec-value}`. Rows alternate
between no background and a very faint `{colors.surface-soft}` stripe on expanded tables.

### Dark Section

**`dark-section`** — Full-width block on `{colors.surface-dark}` (#16151b) with `{spacing.section}`
vertical padding. Headlines in `{typography.display-lg}` (condensed uppercase, white). Used for gaming,
ROG, and performance-focused content blocks where visual drama is needed.

### Tab Bar

**`tab-bar`** — Horizontal tab strip with a 2px bottom border. Active tab shows blue text and a 2px
blue underline; inactive tabs show muted text with no underline. Tabs use `{typography.nav-link}` and
are spaced at `{spacing.lg}` gaps.

### Gradient Text

**`gradient-text`** — Display-sized text with a 90-degree horizontal gradient fill from violet through
cyan to mint, using `background-clip: text`. Applied to hero headlines and campaign slogans where the
brand's signature gradient needs to appear as typography rather than a background wash.

### Footer

**`footer`** — Near-black (#16151b) background matching the main nav. Content organized into columns
with uppercase `{typography.caption-bold}` headings and `{typography.body-sm}` links in muted gray that
brighten to white on hover. Bottom strip carries legal links and region selector.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; hero headline drops to `{typography.display-md}` (28px); product cards stack single-column; mega-menu becomes full-screen overlay; spec badges wrap to 2-per-row; comparison table scrolls horizontally |
| Tablet | 744–1128px | Product cards in 2-column grid; hero text and image stack vertically; mega-menu uses 2-column layout; category tiles 3-per-row; search bar remains inline in nav |
| Desktop | 1128–1440px | Product cards in 3–4 column grid; hero uses side-by-side text/image layout; mega-menu fully expanded with thumbnail grids; full comparison table visible |
| Wide | > 1440px | Content max-width capped at 1440px and centered; hero images scale up; product grid may expand to 5 columns on category pages; generous lateral padding increases |

### Touch Targets
- All tappable elements maintain a minimum 44×44px hit area on mobile
- Product card tap target extends to the full card surface, not just the title text
- Spec badges gain additional vertical padding on touch devices (12px → 16px)
- Nav hamburger icon uses a 48×48px touch zone
- Footer links increase line-height to 2.0 on mobile for comfortable vertical tapping

### Collapsing Strategy
- Mega-menu product thumbnails are hidden below 744px; text-only list replaces them
- Spec-badge rows collapse from 6-across to 2-across, with horizontal scroll available
- Comparison tables switch from static columns to a horizontally scrollable card view
- Category tiles reduce from descriptive labels to icon-only on narrow viewports
- Hero gradient backgrounds simplify to a two-stop gradient on mobile for performance
- Footer columns collapse into accordion sections with tap-to-expand headings

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- ROG sub-brand likely uses a distinct red accent and dedicated `ROGFonts-Regular` face for gaming pages, but the specific red hex was not present in the top extracted colors; gaming-section tokens may need separate extraction
- ASUS Icons webfont was detected but individual glyph mappings and icon sizing conventions could not be determined from extraction
- Exact transition durations and easing curves for hover states, mega-menu open/close, and gradient animations are not available from static extraction
- Shadow elevation scale (card, dropdown, modal layers) is approximated; precise values may differ between product verticals
- The Myriad Pro font stacks appear in some regions/pages — unclear whether this is a legacy style or an active A/B variant
- CJK-specific typography tokens (Microsoft JhengHei, PingFang TC, BIZ UDGothic) were detected but their size and weight overrides for localized pages could not be determined
- Dark-mode toggle behavior (if any exists beyond the gaming sections) was not captured
- Exact grid column counts and gutter widths for the product listing pages were not extractable from color/font hints alone
