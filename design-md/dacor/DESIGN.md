---
version: alpha
name: "Dacor"
source_url: "https://www.dacor.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Brushed graphite rendered as light — that is the first impression Dacor's digital surface delivers. A single dominant charcoal (#313131) swallows the canvas on hero panels and product stages, forcing stainless-steel ranges and matte-black cooktops into sharp photographic relief the way a museum spots a sculpture against a dark wall. Where most appliance sites default to clinical white grids, Dacor inverts the convention: dark backgrounds dominate above the fold, and white space enters only when spec tables and configurator panels demand functional contrast. Typography runs entirely on system stacks — no custom web font ships in the initial paint, keeping load times tight and letting the oversized product imagery do the emotional work. Display headlines land around 40–48px at weight 300–400, deliberately light in stroke so they never compete with the hardware glamour shots they caption; the effect is closer to an architectural specification sheet than a retail page. Buttons sit in `{rounded.none}` or barely-there 2–4px radii (`{rounded.xs}`), reinforcing a precision-instrument aesthetic: hard edges, no playful pills, no consumer-marketplace softness. The navigation stacks product categories — Ranges, Cooktops, Wall Ovens, Ventilation, Refrigeration — inside a full-width mega-menu that drops over a semi-opaque `{colors.scrim}` backdrop, creating a cinematic curtain effect. Product cards present each appliance in a clean `{colors.surface-card}` tile with a generous `{spacing.lg}` internal gutter, a thin `{colors.hairline}` border, and a model-number caption in `{typography.caption}` weight 500. Accent color is almost absent from the default palette; the site relies on a monochromatic charcoal-to-white gradient for hierarchy, reserving color for interactive focus states and error validation. This restraint means the photography palette — warm kitchen scenes, copper pots, marble countertops — supplies all the warmth the interface withholds.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#9e9e9e"
  ink: "#313131"
  ink-strong: "#000000"
  body: "#4a4a4a"
  muted: "#767676"
  muted-soft: "#a0a0a0"
  hairline: "#d9d9d9"
  hairline-soft: "#e8e8e8"
  border-strong: "#b0b0b0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#313131"
  surface-darker: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-dark-muted: "#c0c0c0"
  scrim: "#000000"
  error: "#c62828"
  success: "#2e7d32"
  focus-ring: "#5c9ded"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.20
    letterSpacing: -0.4px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  uppercase-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 1.5px
    textTransform: uppercase
  spec-value:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  mega-menu-heading:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, system-ui"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 1.0px
    textTransform: uppercase

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
  hero: 80px
  section: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    opacity: 1
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 1px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.primary-active}
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
    textDecoration: underline
  button-dark:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.surface-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.primary}
    placeholderColor: "{colors.muted}"
  text-input-error:
    border: 1px solid {colors.error}
    focusBorder: 1px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline-soft}
    padding: 0 {spacing.xl}
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
    padding: 0 {spacing.xl}
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.mega-menu-heading}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.xxl}"
    borderTop: 1px solid {colors.hairline-soft}
    scrimColor: "{colors.scrim}"
    scrimOpacity: 0.5
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-lg}"
    minHeight: 600px
    padding: "{spacing.hero} {spacing.xl}"
    ctaStyle: button-dark
  hero-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-lg}"
    minHeight: 600px
    padding: "{spacing.hero} {spacing.xl}"
    ctaStyle: button-primary
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline-soft}
    imageAspect: 4/3
    hoverBorder: 1px solid {colors.border-strong}
  product-card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    border: none
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    imageAspect: 16/9
    hoverOverlay: "rgba(0,0,0,0.04)"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.uppercase-label}"
    valueTypography: "{typography.spec-value}"
    rowPadding: "{spacing.md} 0"
    rowBorder: 1px solid {colors.hairline-soft}
  comparison-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: 56px
    padding: 0 {spacing.lg}
    border: 1px solid {colors.hairline}
    rounded: "{rounded.none}"
  feature-strip:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    iconSize: 48px
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    gap: "{spacing.xl}"
  kitchen-gallery:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
    padding: "{spacing.section} {spacing.xl}"
  dealer-locator:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputHeight: 48px
    inputTypography: "{typography.body-md}"
    inputRounded: "{rounded.xs}"
    inputBorder: 1px solid {colors.hairline}
    resultTypography: "{typography.body-sm}"
    resultPadding: "{spacing.md} {spacing.base}"
    resultBorder: 1px solid {colors.hairline-soft}
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    separatorColor: "{colors.muted-soft}"
    padding: "{spacing.md} 0"
  footer:
    backgroundColor: "{colors.surface-darker}"
    textColor: "{colors.on-dark-muted}"
    headingTypography: "{typography.uppercase-label}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.on-dark-muted}"
    linkHoverColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: none
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: 2px 8px

---

## Components

### Buttons

**`button-primary`** — A charcoal (#313131) filled rectangle with barely-rounded corners (`{rounded.xs}` at 2px) and white text at `{typography.button-lg}`. The minimal radius communicates precision rather than friendliness. On hover, the fill deepens to `{colors.primary-active}` (#1a1a1a); disabled state flattens to `{colors.primary-disabled}` (#9e9e9e) with white text, conveying inactivity without opacity shifts.

**`button-secondary`** — White fill with a 1px `{colors.primary}` border and charcoal text. Shares the same 48px height and `{rounded.xs}` corners as the primary variant. On hover the background shifts to `{colors.surface-soft}` and the border darkens. Used for secondary actions like "Compare Models" alongside a primary "View Details" CTA.

**`button-ghost`** — A text-only underlined link styled as a button, inheriting `{typography.button-md}`. No background, no border, no padding except vertical breathing room. Used inline within editorial sections and spec callouts where a full button would break the visual rhythm.

**`button-dark`** — Inverted for dark-background contexts: white fill, charcoal text. Appears inside `hero-dark` panels and `feature-strip` sections. Same geometry as `button-primary`, just color-swapped.

### Navigation

**`nav-bar`** — A 64px-tall white bar with a thin `{colors.hairline-soft}` bottom border. The Dacor wordmark sits left; product-category links in `{typography.nav-link}` (14px, weight 500) space evenly across the center. Right side holds utility icons (search, account, where-to-buy). A dark variant (`nav-bar-dark`) runs `{colors.surface-dark}` background with white text, used on dark hero pages.

**`mega-menu`** — Drops below the nav on category hover, spanning full viewport width over a 50%-opacity `{colors.scrim}` backdrop. Category headings use `{typography.mega-menu-heading}` (11px uppercase, 1px letter-spacing) with product links beneath in `{typography.body-sm}`. The panel is divided into 3–4 columns with `{spacing.xxl}` horizontal padding.

### Hero Sections

**`hero-dark`** — The signature Dacor composition: a full-bleed dark panel (minimum 600px tall) with a large lifestyle or product photograph bleeding edge-to-edge behind a `{colors.surface-dark}` overlay. Headline in `{typography.display-xl}` (48px, weight 300) sits left-aligned with generous `{spacing.hero}` vertical padding. A `button-dark` CTA anchors below the subtitle. The thin font weight against the dark ground creates the architectural-drawing quality that separates Dacor from heavier appliance-brand layouts.

**`hero-light`** — Same structure on `{colors.surface-soft}` with dark text and a `button-primary` CTA. Used for secondary landing pages and promotional content where a dark mood is not required.

### Product Display

**`product-card`** — A borderless white tile (`{colors.surface-card}`) with a 1px `{colors.hairline-soft}` edge. Product image in 4:3 aspect ratio fills the top; model name in `{typography.title-sm}` and series caption in `{typography.caption}` sit below with `{spacing.lg}` internal padding. On hover, the border strengthens to `{colors.border-strong}`, providing a subtle lift without shadow or transform. No rounded corners — the square edges match the rectilinear geometry of the appliances themselves. A dark variant (`product-card-dark`) renders on `{colors.surface-dark}` with white text and no border.

**`category-tile`** — Larger rectangular tiles (16:9 image) used on the homepage or category index to represent product lines (e.g., "48-inch Ranges," "Induction Cooktops"). Text overlays in `{typography.title-md}` with a subtle dark hover scrim. Square corners, `{colors.surface-soft}` fill.

### Specification & Comparison

**`spec-table`** — Alternating rows separated by 1px `{colors.hairline-soft}` rules. Spec names render in `{typography.uppercase-label}` (11px, weight 600, all-caps with 1.5px tracking) and values in `{typography.spec-value}` (14px, weight 600). Row padding of `{spacing.md}` keeps the table dense but scannable — appliance specs can easily run 20+ rows, so vertical economy matters.

**`comparison-bar`** — A sticky 56px bar that appears when users select models to compare. `{colors.surface-soft}` background, no rounded corners, with selected model thumbnails and a "Compare Now" `button-primary`.

### Feature & Gallery

**`feature-strip`** — A dark (`{colors.surface-dark}`) horizontal band showcasing 3–4 key features with 48px icons, `{typography.title-md}` headings, and `{typography.body-sm}` descriptions. Items space at `{spacing.xl}` gaps. Used mid-page to break between product photography sections.

**`kitchen-gallery`** — A masonry or grid layout of lifestyle kitchen photographs with `{spacing.sm}` gutters. No rounded corners on images. Optional captions in `{typography.caption}` below each image. Full section uses `{spacing.section}` vertical padding.

### Utility

**`dealer-locator`** — A zip-code input field (`{rounded.xs}`, 48px tall, `{typography.body-md}`) with a search button. Results list below with `{typography.body-sm}` dealer names and addresses, each row separated by `{colors.hairline-soft}`. Padding at `{spacing.md}` vertically and `{spacing.base}` horizontally.

**`breadcrumb`** — A single-line trail in `{typography.caption-sm}` (11px) with `{colors.muted}` for ancestor links and `{colors.ink}` for the current page. Separator glyphs in `{colors.muted-soft}`. Sits above the page title with `{spacing.md}` bottom margin.

**`badge-new`** — A small charcoal pill (`{colors.primary}` background, `{typography.caption-sm}`, `{rounded.xs}`) used to flag newly released models on product cards and category listings.

### Footer

**`footer`** — A dark slab (`{colors.surface-darker}`, #1a1a1a) with column headings in `{typography.uppercase-label}` and link lists in `{typography.body-sm}`. Link color is `{colors.on-dark-muted}` (#c0c0c0) brightening to `{colors.on-dark}` on hover. Section padding at `{spacing.section}` top and bottom. No top border — the dark fill provides enough separation from the content above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + logo; hero min-height drops to 400px with `{typography.display-md}` headlines; product cards stack single-column; mega-menu becomes a full-screen slide-over; spec-table scrolls horizontally; comparison-bar becomes a bottom sheet; footer columns stack vertically; section padding halves to `{spacing.xxl}` |
| Tablet | 744–1128px | Two-column product grid; hero headline scales to `{typography.display-lg}`; mega-menu retains overlay but narrows to 2 columns; feature-strip items wrap to 2×2 grid; nav shows logo + key links, utility icons move to hamburger overflow |
| Desktop | 1128–1440px | Full nav with all category links visible; three-column product grid; hero at full 600px+ height with `{typography.display-xl}`; mega-menu at full 3–4 columns; side-by-side comparison view for up to 3 models |
| Wide | > 1440px | Content max-width caps at 1440px and centers; hero images may extend beyond content width as full-bleed; additional whitespace in `{spacing.section}` gutters; four-column product grid available on category pages |

### Touch Targets

- All interactive elements maintain a 48px minimum touch target on mobile and tablet
- Nav hamburger icon uses a 48×48px hit area regardless of visible icon size
- Product card tap area encompasses the entire card surface, not just the title text
- Spec-table rows gain 4px additional vertical padding on touch devices for easier row targeting
- Dealer-locator search button expands to full width below the input on mobile

### Collapsing Strategy

- Navigation: hamburger drawer on mobile; partial collapse (key links + overflow) on tablet; full horizontal bar on desktop
- Product grids: 1 column mobile → 2 columns tablet → 3 columns desktop → 4 columns wide
- Hero content: headline and CTA stack vertically and center on mobile; left-aligned with image right on desktop
- Spec tables: fixed first column with horizontal scroll on mobile; full table on desktop
- Feature strips: vertical stack on mobile → 2×2 on tablet → horizontal row on desktop
- Kitchen gallery: single-column scroll on mobile → 2-column masonry on tablet → 3-column on desktop
- Mega-menu: full-screen slide-over on mobile → overlay panel on desktop
- Comparison: bottom-sheet drawer on mobile → sticky bar on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Anti-bot wall blocked full extraction.** Page title returned "Just a moment..." (Cloudflare challenge page), meaning color tokens, font stacks, spacing values, and component measurements could not be reliably scraped. The single extracted hex (#313131) is consistent with Dacor's known dark-charcoal brand identity but the full runtime palette was not available.
- **No custom font families detected.** Only system-font stacks were found. Dacor may load a proprietary or licensed typeface (potentially a geometric sans or a thin-weight display face) via JavaScript after the anti-bot gate clears; this could not be confirmed.
- **Accent/highlight color unknown.** Dacor may use a secondary accent (warm metallics, a brand blue, or a highlight tone) for CTAs or promotional elements that was not captured in extraction. The monochromatic charcoal palette above is conservative — verify against the live site.
- **Exact spacing and sizing tokens are estimated.** Without access to computed styles, all spacing, padding, height, and border-radius values are inferred from Dacor's general aesthetic and category conventions rather than measured from the DOM.
- **No theme-color meta tag found.** Mobile browser chrome color is undefined; likely inherits from the dark palette but the exact value is unconfirmed.
- **Interactive states (focus rings, animation durations, easing curves) are not captured.** Focus ring color `{colors.focus-ring}` (#5c9ded) is a standard accessible blue placeholder — the actual brand value may differ.
- **Product configurator / build-your-kitchen tool** likely exists on the live site but its component structure, step indicators, and interactive patterns could not be analyzed through the anti-bot wall.
