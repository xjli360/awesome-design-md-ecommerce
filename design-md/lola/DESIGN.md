---
version: alpha
name: "Lola"
source_url: "https://mylola.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The ingredient list comes before the product name on every LOLA page — that reversal of hierarchy is the clearest signal of the brand's operating logic. Primary teal (#207c83) anchors every CTA and structural element, a hue that reads closer to medical authority than beauty trend, deliberately placed against the soft-pink conventions of the feminine care category. A near-black navy (#272d45) carries heading and body copy weight, while a warm amber (#ff9529) surfaces sparingly on promotional callouts and urgency tags, preventing the palette from reading clinical or cold. The lightest surface (#f7f7f8) is barely perceptible against white — bare backgrounds let product photography and ingredient copy carry visual weight without competition. Apercu handles all display and UI work: letters set at 500–600 weight rather than heavy 700+, trusting tight tracking and clean geometric letterforms over typographic muscle. Cabin takes over for body copy, its humanist warmth softening the data-dense ingredient panels and transparency disclosures that distinguish LOLA from legacy competitors. Buttons use {rounded.sm} to {rounded.md} curvature rather than full pill shapes, positioning the brand as health-and-wellness rather than fashion — friendly without being frivolous. The subscription-first model shapes every purchase pattern: subscription pricing leads before one-time options in product cards, a prominent toggle holds visual weight near add-to-cart, and a mint-tinted surface (#b2f9e9) flags the savings tier with a restrained pastel rather than a loud promotional stripe. Product bundling sits at the top of the purchase hierarchy — build-your-box flows appear before single-product add-to-cart. Navigation carries product categories in clean horizontal structure with a sticky header that collapses on scroll to preserve the reading space that dense ingredient and mission copy demands. An eyebrow type style — 11px Apercu, 1.5px letter-spacing, uppercase — marks ingredient transparency sections, giving certification claims visual authority without icon clutter.

colors:
  primary: "#207c83"
  primary-active: "#175d63"
  primary-disabled: "#a8cfd2"
  primary-light: "#d0eaec"
  accent-orange: "#ff9529"
  accent-mint: "#b2f9e9"
  navy: "#272d45"
  navy-soft: "#2e3f51"
  ink: "#1a1b18"
  body: "#2e3f51"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#e5e5eb"
  hairline-soft: "#d3d4dd"
  canvas: "#ffffff"
  surface-soft: "#f7f7f8"
  surface-card: "#f4f4f6"
  surface-mint: "#b2f9e9"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#d72c0d"
  brown: "#514945"

typography:
  display-xl:
    fontFamily: "'Apercu', 'Cabin', -apple-system, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Apercu', 'Cabin', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Apercu', 'Cabin', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Apercu', 'Cabin', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Apercu', 'Cabin', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Cabin', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  eyebrow:
    fontFamily: "'Apercu', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Apercu', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Apercu', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Apercu', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Apercu', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  tag:
    fontFamily: "'Apercu', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  ingredient-label:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
    stickyOnScroll: true
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    subtextTypography: "{typography.body-sm}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.navy}"
    border: "1px solid {colors.hairline-soft}"
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    activeOptionBackground: "{colors.canvas}"
    activeOptionBorder: "1.5px solid {colors.primary}"
    activeTextColor: "{colors.primary}"
    inactiveTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    savingsBadgeBackground: "{colors.surface-mint}"
    savingsBadgeTextColor: "{colors.primary-active}"
    savingsBadgeTypography: "{typography.tag}"
  hero-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.accent-mint}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.sm}"
    minHeight: 560px
  ingredient-badge:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-active}"
    typography: "{typography.ingredient-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
    border: "1px solid {colors.primary-disabled}"
  savings-badge:
    backgroundColor: "{colors.surface-mint}"
    textColor: "{colors.primary-active}"
    typography: "{typography.tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  promotion-banner:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.eyebrow}"
    height: 36px
    textAlign: center
  build-your-box-card:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    headingColor: "{colors.navy}"
    bodyColor: "{colors.body}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.sm}"
  category-pill:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    borderActive: "1.5px solid {colors.primary}"
    backgroundActive: "{colors.primary-light}"
    textColor: "{colors.muted}"
    textColorActive: "{colors.primary-active}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  transparency-strip:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    eyebrowTypography: "{typography.eyebrow}"
    bodyTypography: "{typography.body-sm}"
    eyebrowColor: "{colors.accent-mint}"
    padding: "{spacing.xxl} 0"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The primary action button renders in teal (#207c83) at 48px tall with 8px rounding, matching the brand's health-forward positioning without the clinical hardness of a fully square corner. `hover` darkens to `primary-active` (#175d63); `disabled` fades to `primary-disabled` (#a8cfd2) with full opacity text retained. The letter-spacing on `button-md` (0.5px) gives Apercu a slightly formal, confident presence at button scale.

**`button-secondary`** — White fill with a 1.5px teal border and teal text creates a contained ghost style that holds visual weight alongside `button-primary` without competing. Used for "learn more" and secondary subscription actions. Active state shifts border and text to `primary-active`.

**`button-ghost`** — Transparent background, ink text with underline, no radius. Appears in footer navigation, inline editorial links, and the "what's in it" ingredient transparency flows where a button shape would look out of place in running copy.

### Subscription Toggle

**`subscription-toggle`** — A two-option segmented control (Subscribe & Save / One-Time) built on a soft-gray track (#f7f7f8). The active option lifts to a white card with a 1.5px teal border, matching the `text-input` focus ring language. A mint savings badge (#b2f9e9 background, #175d63 text) attaches to the subscribe option to surface the discount tier passively without requiring the user to switch tabs to discover it. Typography is `body-sm` (Cabin 14px) so the toggle doesn't dominate the product card hierarchy.

### Product Card

**`product-card`** — Sits on a `surface-card` (#f4f4f6) background with 12px rounding and a 1px `hairline-soft` border. Product title in `title-sm` (Apercu 16px/600), price in `price-display` (Apercu 20px/600, navy #272d45), variant descriptor in `body-sm` (Cabin 14px, muted). Ingredient badges stack horizontally below the product name in `ingredient-badge` pill style. The subscription toggle appears directly above the add-to-cart button rather than in a separate drawer.

### Navigation

**`nav-bar`** — 64px tall, white canvas, 1px bottom hairline. LOLA logo in primary teal left-aligned. Category links (Tampons, Pads & Liners, Personal Care, Sexual Wellness, Bundles) centered in `nav-link` Apercu 14px/500. Right side holds account, cart icon with item count. Collapses to a hamburger + logo + cart on mobile. On scroll past 80px, the bar becomes sticky with a subtle drop shadow rather than a background color change.

### Hero Banner

**`hero-banner`** — Dark navy (#272d45) full-width background anchors the homepage hero, giving maximum contrast for white display text and the teal CTA button. An eyebrow label in mint (#b2f9e9) uppercase Apercu 11px leads the heading hierarchy, used for category or campaign callouts ("ORGANIC COTTON", "DOCTOR-APPROVED"). Heading in `display-xl` (Apercu 40px/600), body in `body-md` (Cabin 16px), CTA button in primary teal. Min-height 560px on desktop; image sits right column or as a full-bleed background with scrim.

### Ingredient Badge

**`ingredient-badge`** — Light teal chip (#d0eaec background, #175d63 text, 1px #a8cfd2 border) used to enumerate product ingredients inline on product detail pages. Typography is `ingredient-label` (Cabin 11px/400, 0.2px tracking). Chips wrap in a flex row, max 3 visible above the fold with an "all ingredients →" ghost link to expand. This component is the most distinctive pattern on the site — no other DTC brand in the category treats ingredient chips as primary product-card UI.

### Promotion Banner

**`promotion-banner`** — A full-width site-top strip in accent-orange (#ff9529) with white uppercase eyebrow text. 36px tall, single line, dismissible via an × icon in white. Used for sitewide promotions, free shipping thresholds, and launch announcements. Only one active at a time; never stacked.

### Build-Your-Box Card

**`build-your-box-card`** — A `surface-soft` (#f7f7f8) panel with 1px hairline border and 12px rounding that presents the bundle configurator entrypoint. Heading in `title-md` (Apercu 18px/600, navy), supporting copy in `body-sm` (Cabin 14px, body). CTA uses `button-primary`. This card appears above fold on the homepage and at the top of the products listing page, encoding the subscription bundle as the preferred purchase path before individual products.

### Transparency Strip

**`transparency-strip`** — A full-width dark navy section used between product modules and the footer to deliver mission copy: ingredient sourcing, certifications (organic, hypoallergenic), and comparison-to-legacy-brands statements. Eyebrow in mint uppercase Apercu, body in Cabin 14px white. No imagery — text-only, generous vertical padding, maximum 3 columns on desktop.

### Footer

**`footer`** — Dark navy background matching the transparency strip, creating a unified dark lower register. Four-column link grid (Shop, About, Help, Social) in `body-sm` Cabin with `muted-soft` (#9a9db1) link color lightening to white on hover. Column headings in `title-sm` Apercu 16px/600 white. Copyright and legal links in `caption` 13px below a 1px #676986 divider.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger + logo + cart; hero stacks text above image; product grid 1-up; subscription toggle full-width; ingredient badges scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; nav remains horizontal with abbreviated labels; hero switches to 50/50 split; build-your-box card spans full width above grid |
| Desktop | 1128–1440px | Three-column product grid; full nav with all category labels; hero uses right-column image with left text; transparency strip renders 3-column |
| Wide | > 1440px | Content max-width 1440px centered; hero image scales to fill without stretching text column; four-column product grid optional on category pages |

### Touch Targets

- All buttons minimum 48px height; icon-only buttons (cart, account, ×) minimum 44×44px tappable area
- Subscription toggle options minimum 44px height per segment
- Ingredient badge chips non-interactive at mobile; tapping expands full ingredient modal
- Category pills minimum 36px height with 12px horizontal padding at mobile

### Collapsing Strategy

- Nav: full horizontal → hamburger drawer; category pills move into drawer top section
- Hero: 50/50 side-by-side → stacked (text first, image second)
- Transparency strip: 3 columns → 1 column with accordion expand per certification claim
- Footer: 4-column link grid → single-column accordion sections
- Product card ingredient badges: wrap row → truncate to 2 with "+N more" expand chip
- Promotion banner: persists across all breakpoints; text truncates with ellipsis below 375px

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font weight confirmations for Apercu: the brand uses Apercu but the exact weights loaded (300/400/500/600) could not be verified from extraction; weights above are inferred from visual hierarchy conventions
- Exact button border-radius in production: extraction shows no explicit radius values; {rounded.sm} (8px) is an informed estimate from visual inspection
- Dark-mode or alternate theme: no dark-mode meta-color extracted; unknown whether a dark-mode palette exists
- Precise spacing scale: no design token file was accessible; spacing values follow an 8px-base grid convention and may not match production exactly
- Icon library: product uses custom or licensed icons (likely from an icon font) — specific glyph set and sizing not extractable
- Shopify platform colors (#008060 Shopify green, #35ee7a, #049cff, #ffb503) present in extraction and excluded from brand palette; confirm none bleed into brand UI
- Outfit font usage: Outfit appears in the font stack extraction but its role relative to Apercu and Cabin is ambiguous — may be a fallback or used in a specific third-party widget
