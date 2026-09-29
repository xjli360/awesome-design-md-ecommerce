---
version: alpha
name: "Tiger"
source_url: "https://www.tiger-corporation.com/en/usa"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep navy (#003388) anchors every navigation bar, footer panel, and hero overlay on Tiger's appliance storefront — a color dense enough to evoke the enamel finish of their vacuum-insulated flasks. Against a pale #eeeeee canvas, product photography does the persuading while typography stays lean and mechanical: Barlow Semi Condensed in medium weight handles headlines at scale, its narrow letterforms echoing the compressed proportions of a rice cooker's LCD display, while standard-width Barlow carries body copy with quiet geometric clarity. Noto Sans JP appears for bilingual product descriptions, a nod to Tiger's Osaka headquarters and the dual-market audience the US storefront serves. CTAs fire in #ff6900 — a saturated orange that reads as thermal energy, heat indicators, and the orange ring on the company's tiger-head logomark — while informational accents reach for #34e2e4, a bright teal used in feature callouts and comparison-table highlights. Cards hold `{rounded.sm}` corners, buttons sit at `{rounded.xs}`, and the overall geometry prefers right angles over softness, letting the brushed-steel product renders feel at home inside the UI frame. Spacing runs generous at section boundaries (`{spacing.section}` = 64px between feature blocks) but tightens inside product spec grids where data density matters. The palette deliberately avoids pastels and lifestyle warmth — this is an engineering-first brand that sells precision temperature control, vacuum insulation, and induction heating, and the interface mirrors that posture: dark structured headers, bright functional accents, white breathing room, nothing decorative that doesn't earn its pixel.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#8099c4"
  accent: "#ff6900"
  accent-active: "#e05e00"
  accent-disabled: "#ffc599"
  teal: "#34e2e4"
  teal-muted: "#31cdcf"
  ink: "#313131"
  body: "#32373c"
  muted: "#abb8c3"
  hairline: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  surface-dark: "#004a59"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  on-dark: "#ffffff"
  error: "#cf2e2e"
  success: "#67a671"
  warning: "#fcb900"
  info: "#146ff8"

typography:
  display-xl:
    fontFamily: "'Barlow Semi Condensed', 'Barlow', -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Barlow Semi Condensed', 'Barlow', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Barlow Semi Condensed', 'Barlow', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Barlow Semi Condensed', 'Barlow', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Barlow', 'Noto Sans JP', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Barlow', 'Noto Sans JP', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', 'Noto Sans JP', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-lg:
    fontFamily: "'Barlow Semi Condensed', 'Barlow', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Barlow Semi Condensed', 'Barlow', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow Semi Condensed', 'Barlow', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Barlow Semi Condensed', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "'Barlow Semi Condensed', sans-serif"
    fontSize: 22px
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
  hero: 96px

components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.accent-disabled}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 10px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.muted}
    focusBorder: 2px solid {colors.primary}
  text-input-error:
    border: 2px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline}
    padding: 0 {spacing.xl}
  nav-bar-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    height: 72px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    boxShadow: 0 8px 24px rgba(0,0,0,0.12)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    boxShadow: 0 1px 4px rgba(0,0,0,0.06)
    hoverBoxShadow: 0 4px 16px rgba(0,0,0,0.1)
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: 1/1
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.hero} {spacing.xl}"
    minHeight: 520px
  hero-banner-cta:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
  feature-badge:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.surface-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: 1px solid {colors.hairline}
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  spec-table-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    minHeight: 200px
  comparison-highlight:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.surface-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    opacity: 0.8
    hoverOpacity: 1.0
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px 12px 44px
    height: 44px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted}"
  technology-callout:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"

---

## Components

### Buttons

**`button-primary`** — Orange (#ff6900) solid fill with white uppercase Barlow Semi Condensed text at 600 weight. Corners hold a tight `{rounded.xs}` (4px) for a technical, engineered feel. On hover the fill darkens to `{colors.accent-active}`; disabled state fades to `{colors.accent-disabled}` with reduced contrast. Height is a fixed 48px with generous horizontal padding (28px) to accommodate longer CTA labels like "Add to Cart" or "View Specifications."

**`button-secondary`** — White fill with a 2px navy border and navy text. On hover/active the fill inverts to solid navy with white text, creating a satisfying toggle effect. Used for secondary actions like "Compare Models" or "Download Manual."

**`button-tertiary`** — Transparent background with navy text, no border. Functions as an inline action link with button-level tap targets. Appears in product detail sidebars and footer navigation clusters.

### Navigation

**`nav-bar`** — 72px-tall white bar with a single-pixel `{colors.hairline}` bottom border. Logo sits left, category links center in `{typography.nav-link}` (Barlow 14px/500), utility icons (search, account, cart) right. Sticky on scroll with a subtle box-shadow that activates after 1px of scroll offset.

**`nav-bar-dark`** — Deep navy variant used on campaign landing pages where the hero image bleeds to the top edge. White text and logo lockup, no bottom border.

**`mega-menu`** — Full-width dropdown triggered by category hover. No rounded corners — the panel attaches flush to the nav bar bottom edge. Contains product category tiles arranged in a 4-column grid with thumbnail images, organized by appliance type (Rice Cookers, Thermal, Electric Kettles, Specialty).

### Product Cards

**`product-card`** — White card with `{rounded.sm}` corners and a barely-visible resting shadow. Image area fills the top in a 1:1 aspect ratio against a soft gray (#eeeeee) background. Below: product title in `{typography.title-sm}`, a one-line feature tagline in `{typography.body-sm}`, and price in `{typography.price}` (Barlow Semi Condensed 22px/700). On hover the shadow deepens and the card lifts 2px via translateY. No border — elevation alone defines the card boundary.

**`product-card-image`** — Square container with `{colors.surface-soft}` fill. Product renders are centered with ~10% internal padding so the appliance never touches the frame edge. Supports a `feature-badge` overlay (positioned top-left, 8px inset) for callouts like "New" or "Best Seller."

### Hero

**`hero-banner`** — Full-bleed section in deep navy (#003388) with white display text. Minimum height 520px, vertically centered content. Background supports a subtle gradient overlay on product photography. CTA button uses the orange `hero-banner-cta` variant with slightly larger padding (16px 32px) for visual weight at hero scale.

### Specification Tables

**`spec-table-row`** — Alternating rows are NOT used; instead a consistent hairline border separates each row. Label column uses `{typography.spec-label}` (uppercase, 13px, muted color) while value column uses `{typography.spec-value}` (15px, ink color). This two-column layout accommodates technical specs like capacity (liters), wattage, dimensions, and weight that are critical to purchase decisions for kitchen appliances.

### Technology Callouts

**`technology-callout`** — Dark teal (#004a59) panel with white text, used to highlight proprietary technologies (e.g., "Tacook Synchronized Cooking," "Ultra Steam," "VE Stainless Steel"). Rounded at `{rounded.sm}`, padded generously, often containing an icon illustration alongside explanatory body text.

### Category Tiles

**`category-tile`** — Soft gray background, `{rounded.sm}` corners, 200px minimum height. Contains a category name in `{typography.title-md}` and a subtle product silhouette or icon. Used on the homepage and collection landing pages to direct shoppers into appliance families.

### Search

**`search-bar`** — Soft gray (#eeeeee) fill with `{rounded.sm}` corners. A magnifying glass icon sits 16px from the left edge; input text starts at 44px indent. Placeholder text in `{colors.muted}`. On focus, the border shifts to 2px solid `{colors.primary}` and the background transitions to white.

### Footer

**`footer`** — Deep navy background matching the primary brand color. Text and links render in white at reduced opacity (0.8), brightening to full opacity on hover. Organized in 4-5 columns: Products, Support, Company, Legal, and a newsletter signup. Newsletter input uses a white-fill text field beside an orange submit button.

### Breadcrumbs

**`breadcrumb`** — Muted-color path rendered in `{typography.caption}` with "/" separators. Sits below the nav bar with `{spacing.md}` vertical padding. Links are underlined on hover; current page is rendered in `{colors.ink}` without a link.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + logo + cart icon. Hero text drops to `{typography.display-md}`. Product grid becomes single-column. Spec tables stack label above value. Footer columns collapse to accordion. |
| Tablet | 744–1128px | Product grid shifts to 2-column. Nav retains hamburger but adds search bar inline. Hero height reduces to 400px. Category tiles become 2×2 grid. |
| Desktop | 1128–1440px | Full nav with category links visible. Product grid at 3-4 columns. Mega menu activates on hover. Spec tables render as two-column rows. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Side padding increases to 48px. Hero imagery can extend full bleed while text container remains constrained. |

### Touch Targets

- All interactive elements maintain 44px minimum touch target on mobile, even when visually smaller
- Product card tap area covers the entire card surface, not just the title link
- Nav hamburger icon has 48px × 48px tap zone
- Footer accordion headers have 48px row height with full-width tap surface
- Spec table rows are non-interactive; only embedded links within values are tappable

### Collapsing Strategy

- Navigation: category links collapse into a slide-out drawer at mobile; search moves into drawer header
- Product grids: 4-col → 3-col → 2-col → 1-col as viewport narrows
- Hero: stacked layout (image above, text below) at mobile; side-by-side at tablet+
- Comparison tables: horizontal scroll with sticky first column at mobile
- Mega menu: replaced entirely by category list in the mobile drawer
- Footer: multi-column layout becomes stacked accordions with expand/collapse toggles

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted color list contains ~15 colors matching the default WordPress/Gutenberg palette (#00d084, #0693e3, #cf2e2e, #ff6900, #fcb900, #7bdcb5, #8ed1fc, #9b51e0, #f78da7, #abb8c3), suggesting the scraper captured a CMS color-picker widget rather than applied brand tokens; true brand-specific palette may be narrower
- No CSS custom properties or design-token variables were captured — the site likely loads styles through a Shopify theme's compiled assets
- Exact border-radius values on cards and buttons are inferred from visual inspection patterns rather than extracted token values
- Animation/transition timing (hover durations, ease curves) not captured
- Exact box-shadow values for card elevation states are approximated
- Icon system details (stroke width, grid size, icon font vs SVG) not determined from extraction
- Mobile nav drawer transition and overlay scrim opacity not captured
- Barlow font weight range actually loaded (which of 100–900 are subset) is unknown — 400, 500, 600, 700 assumed based on typical usage
- Whether Noto Sans JP is loaded for all pages or only Japanese-locale pages is unclear
- Exact breakpoint values are estimated from common Shopify theme patterns, not measured from this specific theme
