---
version: alpha
name: "Herman Miller (Chairs)"
source_url: "https://store.hermanmiller.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every chair specification table on a Herman Miller product page runs in Soehne at 12px uppercase tracking — the same deliberate information density you'd find in a technical white-paper, not a lifestyle catalog. The palette anchors on an earthy, muted teal (#00816c) that darkens to #004e41 on hover and #004338 at section boundaries: three values of the same hue, no secondary chromatic accent doing decorative work at the UI layer. Against a #fafafa / #ffffff canvas with #252525 ink, the teal operates as the single active-state signal — search bars, primary CTAs, active nav underlines, and chair-category callouts all draw from the same well. A secondary register of alert colors — #e22d00 for clearance callouts, #cd4557 for promotional badges, #ce973d for select-collection highlights — enters only at the merchandising layer and never bleeds into core interface chrome.

  Button geometry is nearly orthogonal: {rounded.none} corners on primary and secondary CTAs mirror the rectilinear die-cast aluminum frames of the Aeron and Embody. This is not an accident — the interface shares the same formal logic as the objects it sells. Configurator rails run at a fixed 360px, aligned right, with 1px {colors.hairline} rules separating material swatches from adjustment controls; the spatial hierarchy maps directly to how an ergonomist walks a buyer through seat-pan depth before lumbar support. Type is set in Soehne throughout, a grotesque with ink-trap geometry that remains crisp at the small sizes spec tables demand, with system monospaced stacks (Consolas, Menlo) reserved for machine-readable values such as weight limits and adjustment ranges.

  The spacing system is architectural: a 64px section gap ({spacing.section}) gives the catalog room to breathe between product families, while {spacing.xs}–{spacing.sm} internal gutters enforce the precision a brand selling four-figure chairs needs to project. Navigation is top-fixed at 64px, dropping a single 1px {colors.hairline} rule — no shadow, no blur — and collapsing into a full-screen overlay on mobile rather than an accordion, preserving the brand's emphasis on deliberate spatial choice over feature density.

colors:
  primary: "#00816c"
  primary-hover: "#004e41"
  primary-deep: "#004338"
  primary-disabled: "#acacac"
  accent-red: "#e22d00"
  accent-crimson: "#cd4557"
  accent-crimson-deep: "#8a223b"
  accent-gold: "#ce973d"
  accent-gold-deep: "#ac7c2c"
  ink: "#252525"
  ink-deep: "#0c0c0c"
  body: "#474747"
  muted: "#616161"
  muted-soft: "#828282"
  hairline: "#e1e1e1"
  hairline-soft: "#ebebeb"
  hairline-strong: "#d2d2d2"
  canvas: "#ffffff"
  surface-soft: "#fafafa"
  surface-card: "#fefefe"
  surface-mid: "#f6f6f6"
  on-primary: "#ffffff"
  on-dark: "#fafafa"

typography:
  display-xl:
    fontFamily: "'Soehne', Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.07
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Soehne', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.11
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Soehne', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Soehne', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0
  title-sm:
    fontFamily: "'Soehne', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Soehne', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Soehne', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Soehne', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label-mono:
    fontFamily: "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Monaco, 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'Soehne', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.02em
  button-sm:
    fontFamily: "'Soehne', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.02em
  nav-link:
    fontFamily: "'Soehne', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  price-display:
    fontFamily: "'Soehne', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: 0
  spec-label:
    fontFamily: "'Soehne', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.08em
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
    rounded: "{rounded.none}"
    padding: 14px 24px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "1px solid {colors.ink}"
    outline: none
  text-input-error:
    border: "1px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    position: sticky
    top: 0
    zIndex: 100
  nav-link-default:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageBg: "{colors.surface-soft}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-muted-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  hero-full:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 520px
    paddingX: "{spacing.xxl}"
    paddingY: "{spacing.section}"
  hero-teal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    paddingX: "{spacing.xxl}"
    paddingY: "{spacing.section}"
  configurator-rail:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 360px
    borderLeft: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    position: sticky
    top: 64px
  configurator-tab:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: "12px 0"
    borderBottom: "2px solid transparent"
  configurator-tab-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.ink}"
  material-swatch:
    width: 32px
    height: 32px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    cursor: pointer
  material-swatch-selected:
    border: "2px solid {colors.ink}"
    outline: "2px solid {colors.canvas}"
    outlineOffset: 1px
  spec-row:
    borderBottom: "1px solid {colors.hairline-soft}"
    paddingY: "{spacing.md}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
  spec-value-mono:
    typography: "{typography.label-mono}"
    textColor: "{colors.body}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-collection:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  promo-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    height: 40px
    textAlign: center
    paddingX: "{spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
    gap: "{spacing.xs}"
  footer-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.surface-soft}"
    paddingY: "{spacing.xxl}"
    paddingX: "{spacing.section}"
    borderTop: "none"

## Components

### Buttons

**`button-primary`** — A flat, square-cornered block in #00816c with white type at 14px/500 weight and 0.02em tracking. The orthogonal geometry is load-bearing: it echoes the aluminum extrusions and right-angle welds visible on every chair frame. On hover, the fill darkens to #004e41 with no scale or shadow animation — just a color shift, matching the brand's preference for precision over performance. Disabled state uses #acacac fill and carries the same square corner, so the shape never signals softness through rounding.

**`button-secondary`** — A 1px #252525-bordered outline button on a white field, inverting to a solid #252525 fill on hover with #fafafa text. This binary flip (hollow → filled) is faster to scan than a hover-glow or opacity shift, reflecting the same information-economy the spec tables use. Padding mirrors the primary at 14px/24px so both buttons align to a 48px height and sit flush in paired CTA layouts.

**`button-ghost`** — Typographic-only with a plain underline, used for secondary links within body copy and legal footers. No background, no border — it recedes so product imagery and headline copy hold visual rank.

### Text Input

**`text-input`** — A 48px-tall hairline-bordered field at {rounded.none}, defaulting to a 1px #e1e1e1 rule that steps up to 1px #252525 on focus. There is no focus ring or box-shadow — focus is communicated entirely through border weight shift, consistent with the brand's rejection of decorative affordances. Error state swaps the border to #e22d00 with no fill change, so the field shape stays stable and the error signal is purely chromatic.

### Nav Bar

**`nav-bar`** — A 64px sticky header on #ffffff with a single 1px #e1e1e1 bottom rule, no shadow or blur. Links run in Soehne 14px/500, separated by generous horizontal padding rather than vertical dividers. The active state draws a 2px #00816c underline flush to the bar's bottom edge — a precise mechanical mark rather than a floating indicator. At < 744px the entire nav opens into a full-viewport overlay so the link list never competes with product photography for spatial priority.

### Product Card

**`product-card`** — Square-cornered with a 1px #ebebeb border and a #fafafa image field, presenting chair photography against a near-neutral ground. The title renders in Soehne 16px/500 and the price in a 22px/400 scale that reads comfortably without competing with the headline hierarchy on category pages. A badge slot sits at the image's top-left corner; only one badge appears at a time (sale, new, or collection) to avoid stacking signals.

### Hero

**`hero-full`** — Full-width section on #fafafa with headline in Soehne 56px/300 and body copy in 16px/400, padded 64px vertically. The light-weight display type at large scale is deliberate — it reads as engineered restraint, not underpowered. Imagery sits to the right of the headline block at desktop, becoming a full-width stacked composition on mobile.

**`hero-teal`** — An alternate hero with #00816c fill, used for seasonal promotions and sustainability-focused landing moments. White headline type on the teal ground maintains a high contrast ratio; body copy drops to 16px/400 in #ffffff. The same {rounded.none} geometry holds — no softening of corners to signal a warmer mood.

### Configurator Rail

**`configurator-rail`** — A 360px right-anchored sticky panel, top-offset 64px to clear the nav, separated from the product view by a 1px #e1e1e1 vertical rule. The panel's internal organization follows a tab system ({configurator-tab} / {configurator-tab-active}) dividing Fabric, Frame, and Options, with a 2px #252525 underline on the active tab replacing any filled-pill or chip treatment. Users adjust seat settings within the rail without scrolling the product detail section.

### Material Swatch

**`material-swatch`** — A 32px circle rendered at {rounded.full} with a 2px transparent border, growing a 2px #252525 border plus a 1px white outline offset on selection. The selected state uses outline-offset rather than an inner ring to avoid covering the color, preserving the accuracy of the material preview. Minimum touch target is 44×44px via padding to meet accessibility thresholds while keeping the visual swatch compact.

### Spec Row

**`spec-row`** — A two-column key-value row with the label in 11px/500 uppercase Soehne at #616161 and the value in 14px/400 at #252525, separated by a 1px #ebebeb bottom rule. Numeric spec values (weight capacity, height range, warranty years) use the monospaced stack ({typography.label-mono}) so figures align across rows without tabular-numeral OpenType features. Rows expand on click to reveal sub-specs; no chevron is shown — disclosure is triggered by the row itself.

### Badges

**`badge-sale`** — A flush #e22d00 rectangle at {rounded.none} with white 13px/500 text, sitting in the top-left image corner. Only one badge renders per card to prevent color collisions between the red, teal, and gold variants. `badge-collection` uses #ce973d to flag premium or limited-run chairs such as the Aeron Remastered; the gold hue places it apart from operational red without requiring a separate layout slot.

### Promo Banner

**`promo-banner`** — A 40px-tall full-width bar in #252525 with centered 14px/400 Soehne in #fafafa, sitting above the nav. Used for free-shipping thresholds, financing terms, and limited-time promotions; the dark fill ensures the main nav reads as a distinct layer below it rather than a continuation. The bar is dismissible on desktop but pinned on mobile to preserve promo visibility during scroll.

### Footer

**`footer-bar`** — A #252525 field with 14px/400 Soehne in #fafafa for body copy and #fafafa links styled with underline on hover. Internal sections (Shop, Support, Company, Legal) are arranged in a four-column grid on desktop, collapsing to a single accordion on mobile. No background-image texture or gradient — the footer holds the same orthogonal discipline as every other surface on the site.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; configurator rail moves below product images as a vertically scrolling form; nav collapses to full-screen overlay; hero headline scales to display-md (36px/300); promo banner pinned |
| Tablet | 744–1128px | Two-column product grid; configurator rail becomes a bottom sheet; hero switches to side-by-side layout; nav shows top-level links, secondary items in overflow dropdown |
| Desktop | 1128–1440px | Three-column product grid; configurator rail fixed at 360px right; full nav visible; section padding at spacing.section (64px) |
| Wide | > 1440px | Content max-width 1440px centered; outer gutters absorb excess space; section padding increases to 96px on hero blocks |

### Touch Targets

- All CTA buttons minimum 48px height, 44px minimum width
- Material swatches rendered at 32px visual size with padding to reach 44×44px tap area
- Nav links minimum 44px tap area with {spacing.sm} horizontal padding on mobile overlay
- Spec rows minimum 44px tall on mobile to support thumb tapping for expand/collapse
- Breadcrumb links minimum 44px tap height via padding

### Collapsing Strategy

- Nav: top-fixed link row on desktop → hamburger icon opening full-viewport overlay on mobile; no accordion — all links visible at once in the overlay
- Configurator rail: right-fixed 360px sticky panel on desktop → full-width stacked section below product images on mobile, with tabs replaced by a single vertical flow
- Product grid: 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- Hero: side-by-side text + image on desktop/tablet → stacked image-above-text on mobile, headline font-size steps down from display-xl to display-md
- Spec tables: full two-column layout collapses to single-column stacked label/value rows on mobile
- Promo banner: stays pinned on all breakpoints; dismissible only on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Soehne font weight variants actually loaded on the site (the full weight axis and which specific optical sizes are active) were not captured; weights 300/400/500 are inferred from visual inspection and known Klim Type Foundry conventions
- Exact border-radius in use: the site may apply a non-zero value (2–4px) on some interactive elements not captured during extraction; {rounded.none} is inferred from brand direction
- Configurator rail exact width (360px is estimated); actual breakpoint at which the rail converts to a bottom sheet was not confirmed
- Animation/transition timing values (duration, easing) not extracted — the site likely uses sub-200ms ease-out transitions on hover states
- Chair family sub-palette: individual collections (Aeron, Embody, Sayl, etc.) may have per-collection accent treatments beyond what the site-wide extraction captured
- Promo banner background color variants (some campaigns may use #00816c or #e22d00 rather than the default #252525) not confirmed
- Icon set dimensions and stroke weight used in the configurator and nav were not captured
- Mobile nav overlay background and backdrop-blur (if any) not confirmed
