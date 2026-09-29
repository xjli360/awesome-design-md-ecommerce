---
version: alpha
name: "Kudos"
source_url: "https://kudoscare.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The only diaper brand that foregrounds textile sourcing as its primary visual argument, Kudos structures every layout decision around the cotton-science story rather than around the category's default of smiling baby photography. A grounded sage (#5b8a6a) — the color of dried herbs rather than hospital scrubs — serves as the single brand voltage: it appears on primary CTAs, the logo mark, and the thin rules that divide content sections. Against it, a warm near-white canvas (#fafaf7) and a softly toasted surface-soft (#f2efe8) create layered depth without pulling in a second hue. The palette reads as certifiably clean rather than clinically sterile, which matters for a brand whose core promise is skin that never meets a harsh synthetic. Corner radii hold at `{rounded.md}` throughout — not the sharp geometry of pharmaceutical packaging, not the exaggerated pill-shapes of budget baby care, but a confident middle register that signals both precision and gentleness. The radius appears consistently on cards, inputs, and material-callout badges, lending the system a coherence that survives across breakpoints. Typography runs in a geometric sans at restrained weights: display copy sits at 28–36px weight 600 rather than reaching for the 700+ muscle that safety-anxious baby brands tend to telegraph. The brand trusts its material story; the type does not amplify it. Product cards are deliberately stripped bare — one clean image on `{colors.surface-card}`, a two-line name in `{colors.ink}`, a material-layer callout pill in `{colors.muted}`, an add-to-cart button at full width — no star-count stacks, no urgency badges, no countdown timers. Navigation caps at four links plus a cart icon; the footer mirrors that restraint with certification marks, a newsletter form, and nothing decorative. Kudos earns trust through what it omits as much as what it shows.

colors:
  primary: "#5b8a6a"
  primary-active: "#3d6b50"
  primary-disabled: "#b8d4c0"
  ink: "#1c1c1a"
  body: "#3a3a37"
  muted: "#7a7a73"
  hairline: "#e0ddd5"
  canvas: "#fafaf7"
  surface-soft: "#f2efe8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  cotton-highlight: "#e8f0e5"
  warm-section: "#f7f3ec"
  error: "#c0392b"
  success: "#3d8a4a"

typography:
  display-xl:
    fontFamily: "'DM Sans', 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'DM Sans', 'Plus Jakarta Sans', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'DM Sans', 'Plus Jakarta Sans', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', 'Plus Jakarta Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', 'Plus Jakarta Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', 'Plus Jakarta Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', 'Plus Jakarta Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'DM Sans', 'Plus Jakarta Sans', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'DM Sans', 'Plus Jakarta Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  material-callout:
    fontFamily: "'DM Sans', 'Plus Jakarta Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px
  label-upper:
    fontFamily: "'DM Sans', 'Plus Jakarta Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'DM Sans', 'Plus Jakarta Sans', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
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
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 50px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 27px
    height: 50px
    border: "1.5px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.cotton-highlight}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottom: "1px solid {colors.hairline}"
    position: sticky
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    imageBackgroundColor: "{colors.surface-soft}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.body-md}"
    mutedTypography: "{typography.material-callout}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    maxContentWidth: 560px
  material-badge:
    backgroundColor: "{colors.cotton-highlight}"
    textColor: "{colors.primary-active}"
    typography: "{typography.material-callout}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  subscription-callout:
    backgroundColor: "{colors.warm-section}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg} {spacing.xl}"
    accentColor: "{colors.primary}"
    labelTypography: "{typography.label-upper}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
  size-selector:
    chipBackgroundColor: "{colors.surface-soft}"
    chipTextColor: "{colors.ink}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 40px
    padding: 0 16px
    outOfStockOpacity: 0.4
  comparison-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    headerBackgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    kudosValueColor: "{colors.primary}"
    competitorValueColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
  trust-badge-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.primary}"
    headingTypography: "{typography.title-sm}"
    legalTypography: "{typography.caption}"
    legalColor: "{colors.muted}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — A 50px-tall sage-green button at `{rounded.md}` carrying white text in `{typography.button-md}` (600 weight, 15px). Hover deepens the fill to `{colors.primary-active}` without changing shape or padding; the disabled state bleaches to `{colors.primary-disabled}` and suppresses the pointer cursor. Reserved exclusively for highest-intent actions: Add to Cart, Subscribe & Save, and checkout continuations — never for navigation or editorial links.

**`button-secondary`** — Matches `button-primary` in height and radius but reverses the fill: canvas background, 1.5px sage border, sage text. On hover the background lifts to `{colors.cotton-highlight}`, creating a gentle fill-in without drop shadow. Used for secondary actions adjacent to a primary CTA — "Try Once," "Learn More," "View All Sizes" — always deferring visually to the primary.

### Text Input

**`text-input`** — 48px height at `{rounded.sm}` with a 1px `{colors.hairline}` border at rest, snapping to a 2px `{colors.primary}` focus ring on active without layout shift. Placeholder text in `{colors.muted}`. Used for email capture in the newsletter form, address entry at checkout, and coupon-code entry — the same token set applies in all contexts.

### Navigation

**`nav-bar`** — A 68px sticky header on `{colors.canvas}` with a thin `{colors.hairline}` bottom border. Logo anchors left; `{typography.nav-link}` links occupy the center on desktop; a cart icon and "Shop Now" primary button sit right. No mega-menu: categories resolve to a compact two-level dropdown on hover. On scroll, a subtle box-shadow replaces the bottom border rather than introducing a background color change, preserving the header's lightweight feel.

### Product Card

**`product-card`** — White at `{colors.surface-card}` with `{rounded.md}` corners. The product image renders against a `{colors.surface-soft}` swatch background — a deliberate choice that prevents white-background product photography from dissolving into the page canvas. Below the image: product name in `{typography.title-sm}`, a `material-badge` inline on the next line, price in `{typography.body-md}` weight 500, then a full-width add-to-cart button. No star ratings, countdown timers, or promotional badge stacking.

### Hero Section

**`hero-section`** — Full-width band on `{colors.surface-soft}` (the warm linen-toned off-white, not the pure canvas). Headline in `{typography.display-xl}` at -0.5px tracking; body paragraph in `{typography.body-md}` constrained to 560px max-width. A horizontal button pair follows — primary CTA left, secondary ghost CTA right. The hero avoids full-bleed photography in favor of product-on-surface imagery with generous negative space on either side.

### Material Badge

**`material-badge`** — A full-pill chip (`{rounded.full}`) in `{colors.cotton-highlight}` with `{colors.primary-active}` text at `{typography.material-callout}` (13px, weight 500, 0.1px tracking). Appears directly below the product name on product cards and at the top of the PDP copy block. Copy is always a factual material claim — "100% Cotton Inner," "PFAS-Free Outer," "Plant-Based Adhesive" — never a marketing superlative.

### Subscription Callout

**`subscription-callout`** — A warm-cream section block (`{colors.warm-section}`) at `{rounded.md}`, opened by a `{typography.label-upper}` overline ("SUBSCRIBE & SAVE") in `{colors.muted}`, followed by a `{typography.display-md}` headline and a savings figure rendered in `{colors.primary}`. Two buttons appear inline beneath: the sage primary subscribe button and a secondary "Buy Once" ghost button. Placed once per PDP, below the first scroll threshold, never in the sticky add-to-cart bar.

### Size Selector

**`size-selector`** — A horizontal row of chips, one per diaper size (Newborn through Size 6). Each chip is 40px tall at `{rounded.sm}`, resting on `{colors.surface-soft}` with `{colors.ink}` text in `{typography.button-sm}`. The selected state fills with `{colors.primary}` and flips text to `{colors.on-primary}`. Out-of-stock sizes are not hidden — they render at 40% opacity with a diagonal hairline strikethrough, preserving the size range context for new visitors.

### Comparison Table

**`comparison-table`** — A two-column table (Kudos vs. Conventional Diapers) with a `{colors.surface-soft}` header row and `{colors.surface-card}` body rows. Header cells in `{typography.title-sm}`; body cells in `{typography.body-sm}`. Kudos column values appear in `{colors.primary}` to mark positive differentiation; the competitor column renders in `{colors.muted}`. The container carries `{rounded.md}` corners and a `{colors.hairline}` border. No zebra-striping — horizontal rules in `{colors.hairline}` separate rows instead.

### Trust Badge Strip

**`trust-badge-strip`** — A narrow horizontal band (above the footer or beneath the hero) displaying certification logos — GOTS, OEKO-TEX, and similar marks — in a centered flex row with `{colors.hairline}` top and bottom borders. Labels beneath each logo in `{typography.caption}` at `{colors.muted}`. Static, never animated; the strip communicates verification through density of marks rather than motion.

### Footer

**`footer`** — `{colors.surface-soft}` background with a `{colors.hairline}` top border and `{spacing.section}` vertical padding. Three link columns in `{typography.body-sm}` with `{colors.primary}` link color; a newsletter email input and subscribe button occupying a fourth column on desktop. Column headings in `{typography.title-sm}`. Brand mark, legal links, and copyright block in `{typography.caption}` at `{colors.muted}` pinned to the footer bottom. No promotional banners or imagery in the footer.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo + cart icon; hero stacks copy above product image; size-selector scrolls horizontally in a single row; comparison table becomes horizontally scrollable; footer four-column layout collapses to single column with accordion link groups |
| Tablet | 744–1128px | Two-column product grid; nav links become visible without hamburger; hero goes side-by-side text/image split; subscription callout full-width; footer shifts to two-column layout |
| Desktop | 1128–1440px | Three-column product grid; nav-bar at full 68px with all links visible; hero max-width 1200px centered; comparison table full-width; footer four-column layout |
| Wide | > 1440px | Content constrained to 1440px max-width centered on canvas; hero and section padding expands symmetrically; product grid holds at three columns with larger inter-card gutters |

### Touch Targets

- All interactive chips and buttons enforce a minimum 44×44px tap target on mobile, even when visual height is 40px
- Cart icon tap area padded to 44×44px; the visual glyph is 24px
- Hamburger menu tap zone is 44×44px flush to the right viewport edge
- Size-selector chips allow horizontal scroll on mobile rather than wrapping to prevent multi-row layout breaks
- Material badges are non-interactive and exempt from the 44px rule

### Collapsing Strategy

- Hero CTA pair collapses to full-width stacked buttons on mobile, primary above secondary, with `{spacing.sm}` gap
- Navigation drops all link text below 744px, retaining only logo, hamburger trigger, and cart icon
- Trust badge strip reflows to a 2×N grid on mobile instead of a single horizontal row
- Comparison table wraps in a `-webkit-overflow-scrolling: touch` horizontal scroll container on mobile; the row-label column becomes sticky at left
- Footer link groups collapse to tap-to-expand accordions on mobile to reduce scroll depth

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — kudoscare.com likely renders design tokens via JavaScript or behind anti-bot protection at extraction time. All palette values are brand-knowledge estimates; the primary sage (#5b8a6a) is an inference from Kudos's documented natural-materials positioning and public brand imagery, not a measured screen value. Verify all hex codes against the live site before shipping any implementation.
- **No font stacks extracted** — typeface choice (DM Sans) is an educated inference for a DTC baby brand launched in this era; the actual font may differ. Check the network panel for Google Fonts, Adobe Fonts, or self-hosted woff2 requests on kudoscare.com to confirm.
- **No meta theme-color present** — could not confirm primary brand color through mobile browser chrome theming signal.
- **Exact border-radius values unconfirmed** — `{rounded.md}` at 12px is a reasonable estimate; live values may be tighter (8px) or softer (16px). Inspect computed styles on the live site.
- **Secondary accent color unknown** — no extracted data confirms whether the brand uses a warm yellow, cream-gold, or terracotta accent beyond the sage primary and warm neutral surfaces.
- **Icon library and stroke weight unknown** — glyph style and line weight for navigation and UI icons not observable from static extraction; likely a 1.5–2px stroke weight system consistent with the brand's refined positioning.
- **Motion and animation language unknown** — easing curves, transition durations, and scroll-triggered animation patterns not observable from static extraction.
- **Subscription vs. one-time purchase UI flow unconfirmed** — component structure for the dual-option ATC bar is estimated from category conventions; actual implementation may differ significantly.
