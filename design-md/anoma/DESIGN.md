---
version: alpha
name: "Anoma"
source_url: "https://www.anomawatches.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every dial in the Anoma lineup reads as a solved problem: indices stripped to the minimum needed to tell the time, hands tapered to the point of near-disappearance, and a dial texture—often brushed or grained—that only declares itself under raking light. The brand operates at the edge of the independent micro-watch world where a single model may run for two years before a revision, and where the website is less a shop than a slow argument for paying attention. The color logic follows the same restraint: a near-black canvas (#0d0d0d) absorbs photography the way a lightbox would, letting polished brass indices and lume plots carry warmth without the brand imposing a signature hue. The one departure from neutrality is a muted antique-gold accent (#b8956a) used only for price callouts, active navigation states, and the faintest border highlight on product cards — present enough to signal intentionality, absent enough to stay out of the dial's way. Type runs a classical-cut serif at display sizes — tracking tightened to feel engraved rather than set — and switches to a geometric sans at body and caption scale, the same move every serious horological publisher makes when legibility overtakes atmosphere. `{rounded.none}` dominates: buttons are rectangular, cards carry at most `{rounded.xs}` on the image container, and the search field is a bare underline. The overall effect is closer to a printed catalogue than a Shopify storefront, which is exactly the positioning the brand needs to compete against heritage names at one-fifth the price.

colors:
  primary: "#b8956a"
  primary-active: "#9a7a52"
  primary-disabled: "#d9c4a8"
  ink: "#f0ede8"
  body: "#c8c4bc"
  muted: "#888480"
  hairline: "#2e2c28"
  hairline-soft: "#232220"
  canvas: "#0d0d0d"
  surface-soft: "#141412"
  surface-card: "#1a1917"
  surface-raised: "#222018"
  on-primary: "#0d0d0d"
  on-dark: "#f0ede8"
  error: "#d45c44"
  success: "#5a9e72"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.04em
  title-sm:
    fontFamily: "'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.06em
  body-md:
    fontFamily: "'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.03em
  label-uppercase:
    fontFamily: "'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.14em
    textTransform: uppercase
  price-display:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  spec-label:
    fontFamily: "'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.08em

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
    padding: 14px 32px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    opacity: 0.5
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.muted}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 10px 0
    borderBottom: "1px solid {colors.muted}"
  text-input:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "10px 0"
    border: "none"
    borderBottom: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
    focusBorderBottom: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
    activeColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageRounded: "{rounded.none}"
    titleTypography: "{typography.display-sm}"
    labelTypography: "{typography.label-uppercase}"
    priceTypography: "{typography.price-display}"
    labelColor: "{colors.muted}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    hoverBorder: "1px solid {colors.primary}"
  hero:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    titleColor: "{colors.ink}"
    subtitleColor: "{colors.body}"
    layout: full-bleed
    overlayGradient: "linear-gradient(to right, rgba(13,13,13,0.85) 40%, transparent 100%)"
    ctaComponent: "{components.button-primary}"
    minHeight: 90vh
  dial-feature-section:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-lg}"
    annotationTypography: "{typography.caption}"
    titleColor: "{colors.ink}"
    annotationColor: "{colors.muted}"
    layout: alternating-image-text
    padding: "{spacing.section} {spacing.xl}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.body}"
    rowBorder: "1px solid {colors.hairline}"
    padding: "{spacing.md} 0"
    rounded: "{rounded.none}"
  badge-limited:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.label-uppercase}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  badge-sold-out:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  image-zoom-viewer:
    backgroundColor: "{colors.canvas}"
    cursorStyle: crosshair
    thumbnailBorder: "1px solid {colors.hairline}"
    activeThumbnailBorder: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-uppercase}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} {spacing.xl}"
    columns: 4
  section-divider:
    borderTop: "1px solid {colors.hairline}"
    margin: "{spacing.section} 0"
  movement-callout:
    backgroundColor: "{colors.surface-raised}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    titleColor: "{colors.ink}"
    bodyColor: "{colors.body}"
    accentColor: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Flat rectangular block with zero border-radius, antique-gold fill (#b8956a), and near-black text. Uppercase tracking-wide label at 13px gives it the feel of a stamped maker's mark rather than a web button. Active state darkens to #9a7a52; disabled fades through `{colors.primary-disabled}` at reduced opacity. Never used more than once per viewport — treated as a single editorial CTA.

**`button-secondary`** — Transparent background with a 1px hairline border (`{colors.hairline}`) and `{colors.ink}` label. On hover, the surface lifts subtly to `{colors.surface-soft}` and the border sharpens to `{colors.muted}`. Shares the rectangular, uppercase label aesthetic with the primary but reads as the quieter of the two.

**`button-ghost`** — Borderless except for a 1px bottom rule on the text itself, functioning as a styled inline text link. Used for secondary navigation within product pages ("View full specifications", "Explore movement"). Understated by design; never competes with the primary CTA.

### Text Input

**`text-input`** — No box, no background, no corner radius. A single bottom border (`{colors.hairline}`) is the only visual container; focus state promotes the border to `{colors.primary}`. Placeholder text in `{colors.muted}`. The form field reads as a blank line awaiting inscription, consistent with the engraved, print-catalogue sensibility.

### Navigation

**`nav-bar`** — 64px high, `{colors.canvas}` background, separated from content by a single `{colors.hairline}` bottom border. Logo in `{typography.display-sm}` Cormorant Garamond at normal weight — treated as a wordmark rather than a logotype. Nav links in `{typography.nav-link}` (10px uppercase, 0.1em tracking). Active link switches to `{colors.primary}`. On mobile, collapses to logo + hamburger; no mega-menus, no dropdowns.

### Product Card

**`product-card`** — Image fills the card to the edges (no inner padding, `{rounded.none}` on image container). Below, a thin strip of metadata: model family in `{typography.label-uppercase}` at `{colors.muted}`, model name in `{typography.display-sm}` Garamond, price in `{typography.price-display}` with `{colors.primary}`. The outer card border (`{colors.hairline}`) sharpens to `{colors.primary}` on hover, the only movement signal in an otherwise static card. Sold-out models carry `{components.badge-sold-out}` overlaid at the top-left of the image.

### Hero

**`hero`** — Full-bleed, near-full-viewport image with a left-anchored gradient scrim fading left-to-right (`{colors.canvas}` at ~85% opacity to transparent). Title in `{typography.display-xl}` Garamond at fontWeight 300 — the light weight reads as a caption engraved below a dial photograph rather than a banner headline. Subtitle in `{typography.body-md}` at `{colors.body}`. Single `{components.button-primary}` CTA below. No autoplay video; static dial photography is the rule.

### Dial Feature Section

**`dial-feature-section`** — Alternating image/text pairs, each occupying the full viewport width in two halves. The image half shows extreme macro photography — lume plots, hand stack, text aperture. The text half opens with a `{typography.display-lg}` Garamond heading and continues in `{typography.body-md}` with annotation-style labels in `{typography.caption}` at `{colors.muted}`. Layout is strictly rectangular with no overlap or parallax; the motion belongs to the viewer's eye, not the scroll.

### Spec Table

**`spec-table`** — Two-column key/value grid sitting on `{colors.surface-soft}` with no outer border, only row-level hairlines between entries. Labels in `{typography.spec-label}` (`{colors.muted}`), values in `{typography.body-sm}` (`{colors.body}`). Movement name, case diameter, lug width, water resistance, crystal, and strap material are standard entries. No interactive expand/collapse — all specs visible at once.

### Badges

**`badge-limited`** — 1px border in `{colors.primary}`, transparent fill, `{typography.label-uppercase}` in `{colors.primary}`. Used for limited-run editions only. **`badge-sold-out`** — `{colors.surface-soft}` fill, `{colors.muted}` text, same typography. Both are strictly rectangular with `{rounded.none}`.

### Movement Callout

**`movement-callout`** — A full-width dark panel (`{colors.surface-raised}`) dedicated to the movement specification, typically placed mid-page between the hero and the spec table. A short `{typography.display-md}` heading names the caliber; `{typography.body-md}` body copy describes finishing and provenance. A thin `{colors.primary}` left-border rule (3px) on the text block is the single accent mark in an otherwise monochrome section.

### Footer

**`footer`** — Four-column grid on `{colors.surface-soft}`, separated from page content by `{colors.hairline}` top border. Column headers in `{typography.label-uppercase}`, links in `{typography.body-sm}` at `{colors.body}`. Bottom strip carries legal copy in `{typography.caption}` at `{colors.muted}`. No social icon row; any social links appear as plain text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout; hero height drops to 70vh; nav collapses to logo + hamburger drawer; product grid becomes 1-up; spec table stack as definition list; dial-feature sections become full-width stacked blocks |
| Tablet | 744–1128px | Product grid 2-up; dial-feature sections remain 50/50 split but image crops more aggressively; nav links visible if ≤4 items, otherwise drawer |
| Desktop | 1128–1440px | 3-up product grid; nav fully visible; hero title scales to display-xl; dial-feature sections use generous inner padding |
| Wide | > 1440px | Content max-width caps at 1440px with `{colors.canvas}` fill beyond; hero image continues edge-to-edge; no font scaling above desktop values |

### Touch Targets

- All interactive elements minimum 44×44px on touch viewports
- Bottom-border-only text inputs gain invisible padding to reach touch minimum
- Product cards are fully tappable (entire card surface, not just text)
- Nav hamburger icon: 44×44px tap area regardless of visible glyph size

### Collapsing Strategy

- Spec table remains fully visible on mobile (no accordion) — watch buyers read specs
- Dial feature sections stack image-above-text on mobile; alternating pattern applies only ≥744px
- Footer collapses from 4 columns → 2 columns at tablet → single accordion-toggle columns at mobile
- Movement callout panel retains full-width treatment at all breakpoints; only inner padding reduces

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All colors are inferred** — the live site returned zero extracted hex values (likely JS-rendered tokens or anti-bot blocking). The palette above is constructed from brand-knowledge of the independent micro-watch category and should be verified against the actual site stylesheet before shipping.
- **Fonts unconfirmed** — no font-family stacks were extracted. Cormorant Garamond (display) and DM Sans (body) are reasonable defaults for this brand tier but may not match the live site. Run a DevTools font audit to confirm.
- **Primary brand color unknown** — the antique-gold (#b8956a) is a category-informed guess. The actual accent may be cooler (silver-adjacent), warmer (bronze), or absent in favor of a pure monochrome system.
- **Logo treatment** — whether Anoma uses a wordmark, monogram, or pictorial mark is unconfirmed; the nav-bar spec treats it as a wordmark.
- **Strap/variant selectors** — the UI pattern for selecting strap color, buckle type, or dial variant could not be inferred without product page markup.
- **Pricing and currency format** — price display typography is speculative; actual formatting (e.g., no symbol, comma-separated thousands, CHF vs USD) unverified.
- **Platform** — site is not confirmed Shopify; component assumptions may need adjustment for a custom or Squarespace-based stack.
