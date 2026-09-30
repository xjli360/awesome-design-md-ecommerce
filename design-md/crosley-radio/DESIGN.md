---
version: alpha
name: "Crosley Radio"
source_url: "https://www.crosleyradio.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Alternate Gothic No. 2 D commands every headline register — a condensed American display face borrowed from 1930s newspaper mastheads and diner signage — set against Source Serif Pro's antiquarian warmth in editorial panels. The contrast is the system: acumin-pro-extra-condensed handles secondary display type at near-architectural compression, Muli carries all interface chrome in a clean sans-serif that stays invisible, and minion-pro handles long-form editorial copy with the texture of a catalog printed on uncoated stock. The single confirmed brand anchor is #383637, a warm charcoal that refuses pure black — it carries a faint reddish-brown undertone visible at small sizes and in fine hairline borders. It functions as primary CTA fill, nav text, and product ink simultaneously, trusting a warm-white canvas to yield chromatic priority to the hardware photography. Crosley's product line — the CR series, Cruiser, and Stack-O-Matic turntables — ships in up to twenty colorways ranging from avocado green to burgundy to cream; the digital system treats those product colors as the brand palette rather than competing with its own accent system. Buttons use solid charcoal fill with minimal rounding close to `{rounded.xs}`, echoing the boxy cabinet proportions of the hardware. Product cards run image-heavy at square or 4:3 crops; color-variant selectors appear as small circular swatches beneath each card, foregrounding the interior-decoration dimension of a turntable purchase. Section headings pair alternate-gothic-no-2-d in all-caps with a Source Serif Pro sub-header one scale below — a two-voice editorial register that reads like a well-typeset product magazine from 1962. The overall spacing is generous, with wide section gaps that let product photography breathe rather than compressing listings into a dense grid.

colors:
  primary: "#383637"
  primary-active: "#1f1e1f"
  primary-disabled: "#a8a6a7"
  ink: "#383637"
  body: "#4c4a4b"
  muted: "#767374"
  hairline: "#e2e0e1"
  canvas: "#ffffff"
  surface-soft: "#f9f7f6"
  surface-card: "#ffffff"
  surface-mid: "#f0eeed"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'alternate-gothic-no-2-d', 'Alternate Gothic No 2', 'Franklin Gothic Medium', sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: 0.02em
    textTransform: uppercase
  display-lg:
    fontFamily: "'alternate-gothic-no-2-d', 'Alternate Gothic No 2', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.02em
    textTransform: uppercase
  display-md:
    fontFamily: "'acumin-pro-condensed', 'acumin-pro-extra-condensed', 'Condensed Gothic', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: 0.01em
  display-sm:
    fontFamily: "'acumin-pro-condensed', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: 0
  editorial-header:
    fontFamily: "'Source Serif Pro', 'minion-pro', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-editorial:
    fontFamily: "'Source Serif Pro', 'minion-pro', Georgia, serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  price:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0
  button-md:
    fontFamily: "'acumin-pro-condensed', 'Muli', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'acumin-pro-condensed', 'Muli', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  label-caps:
    fontFamily: "'acumin-pro-condensed', 'Muli', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.02em

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
    padding: 14px 32px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 72px
    logoZone: left
    ctaZone: right
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1 / 1"
    gap: "{spacing.sm}"
    padding: "{spacing.base}"
  product-card-name:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.primary}"
  color-swatch-selector:
    swatchSize: 20px
    swatchGap: "{spacing.xs}"
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderActive: "2px solid {colors.primary}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.editorial-header}"
    ctaTypography: "{typography.button-md}"
    paddingY: "{spacing.section}"
    textAlign: left
  section-header:
    headlineTypography: "{typography.display-lg}"
    subheadTypography: "{typography.editorial-header}"
    textColor: "{colors.ink}"
    subtextColor: "{colors.muted}"
    paddingBottom: "{spacing.lg}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  category-chip:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    borderActive: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    paddingY: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Solid charcoal (#383637) fill with white text in acumin-pro-condensed at 15px uppercase, letter-spaced 0.08em. Rounding is minimal (`{rounded.xs}`, 4px) to echo the boxy cabinet geometry of the hardware. Hover transitions to `{colors.primary-active}` (#1f1e1f); disabled uses `{colors.primary-disabled}` at full opacity with pointer-events removed.

**`button-secondary`** — Same uppercase condensed typography, white background with a 1px `{colors.primary}` border. Used for secondary purchase actions — add-to-wishlist, compare, or a secondary CTA alongside the primary on product detail pages.

**`button-ghost`** — Transparent background, charcoal text, no border. Appears inside editorial sections as a tertiary action ("Shop All", "Learn More") where a bordered button would interrupt the magazine-page rhythm.

### Inputs

**`text-input`** — Clean white field with 1px `{colors.hairline}` border upgrading to 1px `{colors.primary}` on focus. Muli 16px, `{rounded.xs}`, 48px height. Serves newsletter subscription, account forms, and checkout fields. No floating labels — placeholder text in `{colors.muted}` clears on first keystroke.

**`search-bar`** — Pill-shaped (`{rounded.full}`) variant used in the nav affordance. 44px height with slightly compressed padding; search icon sits inline at right edge. Activates on Enter or icon click with no separate submit button.

### Navigation

**`nav-bar`** — 72px white horizontal bar with a subtle bottom hairline. Wordmark anchored at left; category links (Turntables, Bluetooth, Accessories, Lifestyle) in Muli 14px semibold at center; cart count badge and search trigger at right. Sticks on scroll desktop-wide; collapses to hamburger with a full-screen drawer below 744px.

### Product Cards

**`product-card`** — No border-radius on the card container. Square image crop fills the top; product name below in Muli 16px semibold, price in Muli 18px bold, then a row of 20px `color-swatch-selector` circles showing available colorways. No shadow at rest; soft drop-shadow on hover elevates the card subtly. `product-badge` floats absolute top-left over the image.

**`color-swatch-selector`** — Row of 20px circular swatches for colorway selection. Active swatch receives a 2px charcoal ring with a 2px white gap, the conventional selected-state indicator. A tooltip with the colorway name appears on hover; on mobile, the active name appears as a label below the swatch row.

### Hero & Section Headers

**`hero-banner`** — Full-bleed or warm-surface section with alternate-gothic-no-2-d headline at 72px uppercase, Source Serif Pro sub-header at 28px below it, and a single `button-primary`. Text block is left-aligned with product photography filling the right half on desktop; stacks vertically (image first) below 744px. Display type scales down through breakpoints.

**`section-header`** — Two-voice header used above product grids and editorial features: alternate-gothic-no-2-d at 48px all-caps, with a Source Serif Pro line at 28px beneath it. The register reads like a magazine spread headline-and-deck pair, giving product category pages an editorial rather than a catalog feeling.

**`product-badge`** — Sharp-cornered (`{rounded.none}`) label in 11px uppercase Acumin condensed. Charcoal background with white text for "NEW"; same geometry used for SALE with a color token not confirmed from extraction (see Known Gaps). Positioned absolute over product card images.

**`category-chip`** — Pill filter tags above product grids for filtering by type or colorway family. Active state adds a 1px charcoal border; inactive rests on `{colors.surface-mid}`. Label-caps typography at 11px uppercase with 0.12em letter-spacing keeps the tags compact and legible at small scale.

### Footer

**`footer`** — Full-width charcoal (#383637) background with white text in four columns: Shop, Support, About, Newsletter. Column headings use `{typography.label-caps}`; column links use `{typography.body-sm}` at normal weight. Newsletter signup appears as a white-bordered `text-input` variant with an inline `button-primary` submit. Social icons in a row at the bottom right; legal links in `{colors.muted}` below the column grid.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger nav with full-screen drawer, single-column product grid, hero stacks vertically (image above text), swatch rows scroll horizontally |
| Tablet | 744–1128px | Two-column product grid, sub-category nav links collapse into hamburger, hero maintains side-by-side at reduced type scale |
| Desktop | 1128–1440px | Three- or four-column product grid, full horizontal nav with dropdown panels, hero at full 72px display type |
| Wide | > 1440px | Content max-width constrained to ~1280px, hero image bleeds edge-to-edge while text block remains in content column |

### Touch Targets

- All buttons minimum 48px height and 44px width on mobile
- Color swatches expand from 20px to 28px on touch devices for accessibility
- Nav links in hamburger drawer spaced to minimum 44px tap height
- Cart and search icon buttons padded to minimum 44×44px touch area with invisible padding extension

### Collapsing Strategy

- Nav: full horizontal bar with dropdowns → icon strip plus hamburger → full-screen drawer overlay
- Product grid: 4-col → 3-col → 2-col → 1-col descending through breakpoints
- Hero type: 72px → 48px → 36px across Wide / Desktop / Mobile; layout shifts from side-by-side to stacked below 744px
- Section headers: alternate-gothic headline 48px → 36px → 28px; Source Serif sub-header scales proportionally
- Footer: four-column grid → accordion-style expandable sections on mobile; newsletter field remains visible by default

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#383637) was extracted from the live site; all palette tokens beyond primary are derived from brand aesthetic knowledge rather than confirmed extraction — treat non-primary color tokens as estimates requiring verification against live computed styles
- No accent or promotional color confirmed; Crosley likely uses a warm red or orange for SALE badges and urgency CTAs — omitted here due to lack of extraction evidence; add a `sale` and `accent` token once confirmed
- Footer background assumed to be primary charcoal (#383637) based on the meta theme-color value; could be a lighter dark or true black (#000000) in practice
- Font weights for Muli, acumin-pro-condensed, and alternate-gothic-no-2-d are inferred from typical usage conventions; exact integers should be verified against live computed styles via browser DevTools
- Exact button and input border-radius values were not extractable; `{rounded.xs}` (4px) is inferred from the hardware product aesthetic — verify against computed border-radius on live CTAs
- Hero layout (left-text / right-image split) and section-header two-voice pattern are inferred from the brand category and font stack; direct DOM confirmation was not available from extraction
