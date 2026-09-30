---
version: alpha
name: "Wempe"
source_url: "https://www.wempe.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every great German watch house keeps its own silence — Wempe's digital presence speaks in the same register as a Glashütte movement beneath a sapphire crystal: nothing ornamental, everything purposeful. The Hamburg-founded maison, now past its 147th year, earned its own manufacture certification (Wempe Chronometerwerke, Glashütte) long before "manufacture" became a marketing word, and that heritage is legible in a design language that uses black (#000000) as its single authoritative voice and reserves gold (#b8912a) for the exact moments it matters — hallmarks, divider rules, hover states on featured pieces. The canvas is pure white with no grey drift, because the brand trusts editorial photography of watch dials and gem-set brooches to supply all the warmth the layout needs. Typography runs in a Didot-adjacent serif for display: high contrast thick-to-thin strokes, generous negative tracking at large sizes, the same vertical tension a master watchmaker sees in a properly poised escapement. Body copy drops to a neutral grotesque — likely a geometric sans — so that legibility never competes with the headline's authority. Spacing is architectural: the grid breathes at 64-80px section gaps, product cards carry ample white air, and the navigation sits flat and near-invisible so that merchandise, not chrome, dominates first attention. Rounded corners are effectively absent; the vocabulary is rectangular throughout, with the single exception of pill-shaped filter tags in catalog views. Interaction states are restrained — hover darkens gold to a deeper amber, focus rings are thin and gold-tinted, active states compress rather than glow. The overall register is closer to a Geneva auction catalogue than an e-commerce interface: unhurried, high-contrast, resolved.

colors:
  primary: "#000000"
  primary-active: "#1a1a1a"
  primary-disabled: "#999999"
  gold: "#b8912a"
  gold-light: "#d4aa4e"
  gold-pale: "#f0e6c8"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f8f7f5"
  surface-card: "#ffffff"
  surface-dark: "#0d0d0d"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-gold: "#000000"
  error: "#b00020"

typography:
  display-xl:
    fontFamily: "'Wempe Display', 'Didot', 'GFS Didot', 'Bodoni MT', Georgia, serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Wempe Display', 'Didot', Georgia, serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Wempe Display', 'Didot', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.1px
  display-sm:
    fontFamily: "'Wempe Display', 'Didot', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.04em
  price-display:
    fontFamily: "'Wempe Display', 'Didot', Georgia, serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.14em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  label-gold:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.16em
    textTransform: uppercase
  eyebrow:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.2em
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 12px
  xl: 24px
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
  section: 80px
  hero: 120px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 40px
    height: 52px
    border: "1px solid {colors.primary}"
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary-disabled}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 15px 39px
    height: 52px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
  button-gold:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 40px
    height: 52px
    border: "none"
  button-ghost-light:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 15px 39px
    height: 52px
    border: "1px solid {colors.on-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 14px 16px
    height: 52px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxHeight: 28px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: "0 1px 8px rgba(0,0,0,0.06)"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"
    categoryHeaderTypography: "{typography.title-sm}"
    categoryHeaderColor: "{colors.gold}"
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    imageBackgroundColor: "{colors.surface-soft}"
    padding: "0"
    gap: "{spacing.md}"
  product-card-brand:
    typography: "{typography.eyebrow}"
    textColor: "{colors.muted}"
  product-card-name:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-hover:
    imageScale: 1.03
    transition: "opacity 0.3s ease, transform 0.4s ease"
  hero-full-bleed:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: "100vh"
    contentMaxWidth: 680px
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.gold}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    sublineColor: "rgba(255,255,255,0.75)"
    ctaGap: "{spacing.base}"
  editorial-split:
    layout: "50/50 or 60/40"
    imageRounded: "{rounded.none}"
    textPadding: "{spacing.section} {spacing.xxl}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.gold}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
  gold-rule-divider:
    borderTop: "1px solid {colors.gold}"
    width: 48px
    margin: "{spacing.lg} auto"
  category-eyebrow:
    typography: "{typography.eyebrow}"
    textColor: "{colors.gold}"
    marginBottom: "{spacing.sm}"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
    border: "1px solid {colors.hairline}"
  filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
  badge-new:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.label-gold}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  badge-exclusive:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-gold}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  watch-detail-panel:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.xl} 0"
    specsLabelTypography: "{typography.caption}"
    specsLabelColor: "{colors.muted}"
    specsValueTypography: "{typography.body-sm}"
    specsValueColor: "{colors.ink}"
    dividerColor: "{colors.hairline-soft}"
    referenceTypography: "{typography.caption}"
    referenceColor: "{colors.muted}"
  pdp-image-gallery:
    thumbnailBorder: "2px solid transparent"
    thumbnailBorderActive: "2px solid {colors.gold}"
    thumbnailGap: "{spacing.sm}"
    mainImageRounded: "{rounded.none}"
    backgroundColor: "{colors.surface-soft}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    backdropColor: "rgba(0,0,0,0.5)"
    inputTypography: "{typography.display-sm}"
    inputBorderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xxl}"
    resultLabelTypography: "{typography.title-sm}"
    resultLabelColor: "{colors.gold}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "rgba(255,255,255,0.7)"
    linkColorHover: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.gold}"
    borderTop: "none"
    padding: "{spacing.section} 0 {spacing.xl}"
  footer-bottom-bar:
    backgroundColor: "{colors.primary}"
    textColor: "rgba(255,255,255,0.45)"
    typography: "{typography.caption}"
    borderTop: "1px solid rgba(255,255,255,0.1)"
    padding: "{spacing.lg} 0"
  boutique-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    imageAspectRatio: "16/9"
    cityTypography: "{typography.display-sm}"
    cityColor: "{colors.ink}"
    addressTypography: "{typography.body-sm}"
    addressColor: "{colors.muted}"
    padding: "{spacing.lg}"
  certification-strip:
    backgroundColor: "{colors.surface-soft}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    iconColor: "{colors.gold}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    padding: "{spacing.xl} 0"

## Components

### Buttons

**`button-primary`** — A sharp-cornered black rectangle with fully uppercase, wide-tracked grotesque labels. At 52px tall and 40px horizontal padding, it reads substantial without being brash. Hover darkens to `{colors.primary-active}` (#1a1a1a) with no transition glow — just a clean value shift. Disabled state uses `{colors.primary-disabled}` (#999999), preserving the white label but draining authority from the block.

**`button-secondary`** — White fill, black 1px border, identical geometry to primary. Used when two equal-weight actions share a row (e.g. "Add to Cart" / "Book an Appointment"). Hover fills to `{colors.surface-soft}` to signal interactivity without collapsing the border-primary contrast.

**`button-gold`** — The single warm-temperature CTA, reserved for highest-priority conversion moments: enquiry submissions, Chronometerwerk certification prompts, boutique booking confirmations. Background is `{colors.gold}` (#b8912a), label in `{colors.on-gold}` (black) via `{typography.button-md}`. No hover glow — hover desaturates slightly to `{colors.gold-light}`.

**`button-ghost-light`** — Used over dark hero images; white border, white label, transparent fill. On hover, fill becomes `rgba(255,255,255,0.1)` without border change. Pairs with `button-primary` on dark-background hero sections where black would vanish.

### Text Input

**`text-input`** — Zero border-radius, thin 1px `{colors.hairline}` border, 52px height matching button height for row-alignment in forms. On focus the border sharpens to `{colors.primary}` (no shadow, no glow). Placeholder text in `{colors.muted-soft}`. Labels float above in `{typography.title-sm}` with `{colors.muted}` tint.

### Navigation

**`nav-bar`** — 72px tall, white fill, hairline bottom border. The Wempe wordmark occupies the left with a maximum height of 28px. Center links run in `{typography.nav-link}` (13px, uppercase, 0.08em tracked); the right cluster carries a search icon, language selector, and shopping bag icon at 40px touch footprints. On scroll past 80px, a faint box-shadow joins the hairline border to anchor the bar.

**`mega-menu`** — Opens on hover with a full-width panel that slides down from the nav-bar underside. Section headings (Watches, Jewellery, Services, Maisons) render in `{typography.title-sm}` with `{colors.gold}` tint. Sub-categories in `{typography.body-sm}`. A curated featured product image occupies the rightmost column. No rounded corners anywhere in the panel.

### Product Card

**`product-card`** — Portrait-ratio (3:4) image over a `{colors.surface-soft}` placeholder background, no border, no shadow, no radius. On hover the image scales 3% (`transform: scale(1.03)`) over 400ms ease, with a second image (dial close-up or wrist shot) cross-fading in at 300ms. Below the image: brand manufacture name in `{typography.eyebrow}` / `{colors.muted}`, model name in `{typography.display-sm}`, price in `{typography.price-display}`. A "Request Price" ghost label replaces the price figure for pieces sold on enquiry.

### Hero

**`hero-full-bleed`** — Full-viewport editorial imagery, text overlaid on a dark scrim region or positioned in a white content column. Eyebrow line renders in `{typography.eyebrow}` with `{colors.gold}` tint, headline in `{typography.display-xl}` (white on dark, ink on light). CTA buttons sit 40px below copy, either white ghost + gold or black primary depending on background. No decorative borders or geometric overlays.

**`editorial-split`** — 50/50 or 60/40 column layout: full-bleed image one side, editorial copy the other. Text column carries `{spacing.section}` vertical padding and `{spacing.xxl}` horizontal margin. Eyebrow in gold, headline in `{typography.display-md}`, body in `{typography.body-md}` at 1.65 line-height. A `{components.gold-rule-divider}` separates eyebrow from headline.

### Decorative / Brand-Signature Elements

**`gold-rule-divider`** — 48px wide, 1px tall gold (`{colors.gold}`) horizontal rule, centered, used as a section opener above headlines throughout editorial and PDP layouts. The most consistent brand-signature element across the site.

**`category-eyebrow`** — All-caps 11px label in `{colors.gold}` with 0.2em tracking, appears above every section and card group title. Functions as the warmth accent in an otherwise monochrome grid.

**`badge-new` / `badge-exclusive`** — Sharp-cornered label chips: gold for new references, black for exclusive/limited pieces. Both use `{typography.label-gold}` (11px, uppercase, wide tracking). Applied over product card images at top-left.

**`watch-detail-panel`** — The specification block on PDPs lists reference number, case diameter, movement calibre, water resistance, and strap variants. Labels in `{typography.caption}` / `{colors.muted}`, values in `{typography.body-sm}` / `{colors.ink}`. Rows separated by `{colors.hairline-soft}` 1px rules. The manufacture certification badge (Chronometerwerk logo) floats above this panel with a `{colors.gold}` accent border-left.

**`certification-strip`** — A full-width band in `{colors.surface-soft}` with centered columns: gold icon, label below in `{typography.caption}` / `{colors.muted}`. Communicates: Free shipping · Certified quality · Boutique service · Returns. Sits between hero and category grid.

**`search-overlay`** — Full-screen white panel triggered by the nav search icon. Input field runs at `{typography.display-sm}` size with a 1px hairline underline (no box). Below the input, results populate in two columns: "Watches" and "Jewellery" with `{colors.gold}` section labels in `{typography.title-sm}`.

### Footer

**`footer`** — Deep black (`{colors.primary}`) fill with four-column link grid. Column headers in `{typography.title-sm}` / `{colors.gold}`. Links in `{typography.body-sm}` at 70% white opacity, brightening to full white on hover. Newsletter input sits inline in the rightmost column — white border, black fill, white placeholder. The `{components.footer-bottom-bar}` carries copyright and legal links at 45% white opacity, separated by a 10% white hairline rule.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces horizontal links; hero headline drops to `{typography.display-md}`; mega-menu becomes full-screen drawer; footer collapses to single-column accordion |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; editorial-split stacks vertically (image above, text below); hero content left-aligned at 60% width |
| Desktop | 1128–1440px | Three- or four-column product grid; full mega-menu; editorial-split at 50/50; nav at full 72px height; section padding at `{spacing.section}` (80px) |
| Wide | > 1440px | Content max-width caps at 1440px with symmetrical margin-auto; hero image extends edge-to-edge; product grid stays at four columns; typographic scale unchanged |

### Touch Targets

- All interactive nav icons minimum 44×44px touch footprint on mobile
- Filter pills minimum height 40px on mobile; shown in horizontal scroll row with no wrapping
- Product card tap target covers full card including image — no separate CTA button on mobile
- Add-to-cart / enquiry buttons span full width on mobile viewports
- Footer accordion chevrons carry a 48px tap target height

### Collapsing Strategy

- Primary nav collapses to hamburger at < 1000px; drawer slides from left, full height, black fill
- Mega-menu panels become top-level drawer sections with expand/collapse chevrons
- Editorial-split always stacks image-first on mobile; text block padding reduces to `{spacing.xl}`
- Watch detail specification grid collapses from two-column to single-column on mobile
- Boutique cards collapse to single column with reduced image aspect ratio (16/9 → 4/3)
- Certification strip collapses from four-column to two-column at tablet, single-column on mobile
- Footer columns collapse to accordion on mobile; headings remain visible as tap targets

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the site returned "Access Denied" to the crawler. All palette values above are derived from brand-knowledge of Wempe's documented identity (black/white/gold luxury register) rather than live site extraction. Actual hex values for the specific gold tone, dark surface variants, and any secondary accent colors should be verified against the live site.
- **No font families extracted** — typeface names ("Wempe Display", Didot) are inferred from the brand's known editorial aesthetic and publicly visible identity materials. The actual font stack (custom webfont name, CDN origin, weight range) is unknown and must be confirmed via browser DevTools.
- **Logo wordmark geometry** — exact proportions, whitespace, and whether the logo uses a custom ligature or swash variant could not be confirmed.
- **Interaction timing curves** — hover transition durations and easing functions above are estimated at luxury-standard (300–400ms ease); actual values require live inspection.
- **Mobile navigation pattern** — whether the mobile drawer uses a slide-in or full-screen fade, and whether it has a dark or light fill, is inferred rather than extracted.
- **Price/enquiry logic** — which product categories suppress price in favor of "Request Price" could not be confirmed from the blocked extraction; rule above is based on category norms for haute horlogerie.
- **PDP image gallery count and layout** — the number of gallery images per product and thumbnail placement (left rail vs. bottom strip) is estimated.
