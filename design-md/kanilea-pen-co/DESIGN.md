---
version: alpha
name: "Kanilea Pen Co."
source_url: "https://kanileapenco.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Mahogany dark (#573837) carries the whole Kanilea visual identity — the color of koa wood grain, aged resin barrel stock, and a freshly turned pen body before its final lacquer. Alone against white canvas it registers as precise and warm without tipping into decoration; combined with its two extracted counterpoints — electric Pacific #00ccff and deep-ocean cobalt #092fb8 — it creates a three-note tonal system that maps directly onto the physical world of the product: wood, water, and ink. #573837 anchors every primary CTA, the footer band, and the nav logo treatment; #092fb8 handles link text and informational depth; #00ccff reads as a highlight accent and hover signal, the way light bounces off a lacquered barrel surface. Type runs in Geneva and Verdana, system humanists that predate custom web font stacks — not a fallback but a fitting match. Both faces were engineered for screen legibility at the sizes where pen specifications (nib grade: Extra Fine, Fine, Medium, Broad; fill system: cartridge/converter, piston, vacuum) must hold their form without blur. Verdana's wide inter-character spacing lets long model names breathe in product headers; Geneva handles tight navigation labels and price figures without muddying at 14px. The pairing reads functional and material, letting craft live in the product photography and handcrafted barrel resin rather than in a proprietary typeface. Corner radii stay conservative: `{rounded.sm}` (8px) on buttons and inputs, `{rounded.xs}` (4px) on nib-grade and material specification badges, `{rounded.md}` (12px) on product cards. No pill shapes or fully circular UI appears anywhere — the geometry signals a workshop over a consumer app, every edge squared as if cut on a lathe. Warm off-white `{colors.surface-soft}` cushions product imagery, preventing the optical flatten that pure white creates beneath photographed wood and resin. The footer reverses into solid `{colors.primary}` mahogany, anchoring the page with the same visual weight as the physical object being sold. Section spacing at `{spacing.section}` (64px) between content bands stays generous; component-internal gaps compress to `{spacing.sm}` (8px) — the same dense-but-airy balance of a well-typeset specification sheet.

colors:
  primary: "#573837"
  primary-active: "#3d2827"
  primary-disabled: "#b09a99"
  accent-cyan: "#00ccff"
  accent-cyan-active: "#00a8d4"
  accent-cobalt: "#092fb8"
  accent-cobalt-active: "#072598"
  ink: "#1a1a1a"
  body: "#3a3a3a"
  muted: "#6b6b6b"
  muted-soft: "#9a9a9a"
  hairline: "#d8d0ce"
  hairline-soft: "#ede8e7"
  canvas: "#ffffff"
  surface-soft: "#f8f5f3"
  surface-card: "#ffffff"
  surface-warm: "#f2ece9"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  link: "#092fb8"
  link-hover: "#072598"

typography:
  display-xl:
    fontFamily: "Geneva, Verdana, 'Trebuchet MS', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Geneva, Verdana, 'Trebuchet MS', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-md:
    fontFamily: "Geneva, Verdana, 'Trebuchet MS', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Verdana, Geneva, 'Trebuchet MS', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Verdana, Geneva, 'Trebuchet MS', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Geneva, Verdana, 'Trebuchet MS', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.1px
  badge:
    fontFamily: "Geneva, Verdana, 'Trebuchet MS', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "Geneva, Verdana, 'Trebuchet MS', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Geneva, Verdana, 'Trebuchet MS', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  pen-name:
    fontFamily: "Geneva, Verdana, 'Trebuchet MS', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "Geneva, Verdana, 'Trebuchet MS', sans-serif"
    fontSize: 18px
    fontWeight: 600
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
    rounded: "{rounded.sm}"
    padding: "14px 24px"
    height: 48px
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 24px"
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
    padding: "13px 23px"
    height: 48px
    hoverBackgroundColor: "{colors.surface-warm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    padding: "12px 16px"
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxWidth: 160px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    titleTypography: "{typography.pen-name}"
    priceTypography: "{typography.price}"
    subtitleTypography: "{typography.body-sm}"
    subtitleColor: "{colors.muted}"
    imageRatio: "3/4"
    hoverShadow: "0 4px 16px rgba(87,56,55,0.14)"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subTypography: "{typography.body-md}"
    subColor: "{colors.body}"
    ctaTypography: "{typography.button-md}"
    minHeight: 520px
    imageAlign: right
    padding: "{spacing.section} {spacing.xl}"
  spec-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  material-chip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.xxl} 0"
    borderBottom: "1px solid {colors.hairline}"
  pen-detail-panel:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.pen-name}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.primary}"
    descTypography: "{typography.body-md}"
    descColor: "{colors.body}"
    specLabelTypography: "{typography.caption}"
    specLabelColor: "{colors.muted}"
    padding: "{spacing.xl}"
    gap: "{spacing.lg}"
  ink-swatch:
    rounded: "{rounded.full}"
    size: 32px
    border: "2px solid {colors.hairline}"
    activeBorder: "2px solid {colors.primary}"
    tooltipTypography: "{typography.caption}"
  limited-tag:
    backgroundColor: "{colors.accent-cobalt}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    linkColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The primary action button fills with `{colors.primary}` mahogany (#573837) and white text, sitting at 48px height with `{rounded.sm}` radius. On hover it deepens to `{colors.primary-active}` (#3d2827), one tone darker as if the wood grain shifted under pressure. The disabled state desaturates to `{colors.primary-disabled}`, a pale warm brown that reads unavailable without breaking the palette. Used for Add to Cart, Checkout, and email capture CTAs throughout the site.

**`button-secondary`** — Outlined variant: white fill, 1px `{colors.primary}` border and matching text, identical height and radius to the primary. Hover fills with `{colors.surface-warm}` to add warmth without competing against a nearby primary. Appears on collection pages for "View All" and "Learn More" actions alongside editorial copy.

**`button-ghost`** — Transparent background, no border, `{colors.body}` text, no radius. Used as an inline text-action (e.g., "Read the full story," "See all colorways") within editorial sections where a boxed button would interrupt prose flow.

### Text Input

**`text-input`** — Single-line input at 48px height, `{rounded.sm}` radius, 1px `{colors.hairline}` border at rest. Focus state steps to a 2px `{colors.primary}` stroke, pulling the warm brown into the form context. Placeholder renders in `{colors.muted}`. Used in newsletter signup banners, coupon entry at checkout, and any site search field.

### Navigation

**`nav-bar`** — White canvas bar at 64px height with a 1px `{colors.hairline}` bottom separator. Logo sits left at up to 160px; navigation links (Collections, Limited Edition, About, Contact) sit center-right in `{typography.nav-link}` with no active underline — text shifts to `{colors.primary}` on hover. Cart icon anchors the far right with a small quantity indicator badge in `{colors.primary}` fill.

### Product Display

**`product-card`** — A 3:4 portrait image frame shows the full pen barrel; title renders in `{typography.pen-name}` uppercase with an `{spacing.sm}` gap down to price in `{typography.price}`. Material chips (`material-chip`) overlay the image corner at lower-left, and a `limited-tag` badge pins to upper-right when applicable. The `{rounded.md}` card container picks up a warm directional shadow on hover, reinforcing the physical-object reading of the product.

**`pen-detail-panel`** — The right-column product panel stacks model name in `{typography.pen-name}`, price in `{typography.price}` colored `{colors.primary}`, and an editorial paragraph in `{typography.body-md}`. Below the description, a specification grid pairs `{typography.caption}` labels in `{colors.muted}` (Nib Size, Fill System, Material, Length, Weight) with `{typography.body-md}` values. Ink swatch row appears when multiple colorways exist. The Add to Cart button spans full panel width.

**`ink-swatch`** — 32px circular dots in a flex row, 2px `{colors.hairline}` border at rest, switching to `{colors.primary}` on selection. Appears on product detail pages when multiple pen finishes or matched ink colors are offered. Hovering reveals a tooltip in `{typography.caption}` with the finish name.

### Content Blocks

**`hero`** — Full-bleed band in `{colors.surface-soft}` at minimum 520px height; headline in `{typography.display-xl}` occupies the left 55%, product photography bleeds to the right edge with no padding. The single CTA is `button-primary` at standard size below the subhead copy. Vertical rhythm uses `{spacing.section}` padding top and bottom so the band reads as a standalone visual unit.

**`collection-header`** — A narrower editorial banner atop category and collection pages. Title in `{typography.display-md}`, supporting copy in `{typography.body-md}`, both on `{colors.surface-soft}`. A 1px `{colors.hairline}` bottom border divides it cleanly from the product grid below. Padding compresses at `{spacing.xxl}` vertical, creating a tighter band than the hero.

**`spec-badge`** — Uppercase label on `{colors.surface-warm}` background with `{colors.muted}` text, used to tag nib grade (EF, F, M, B), fill system, and material notes in both product cards and the detail panel. `{rounded.xs}` keeps it reading as data rather than decoration.

**`material-chip`** — A stronger `{colors.primary}` fill version of the spec badge, used to call out premium material highlights (Koa, Ebonite, Urushi, Titanium) as image overlays or pinned panel tags. White text on mahogany creates immediate visual hierarchy that draws the eye to the distinguishing material first.

**`limited-tag`** — Deep cobalt `{colors.accent-cobalt}` (#092fb8) fill with white text in `{typography.badge}` uppercase. Applied to the product card image corner and alongside the product title in the detail panel to flag limited-edition runs. The cool cobalt contrasts against warm surface tones and the mahogany primary, ensuring the tag is always legible.

**`footer`** — Full-width band reversing into solid `{colors.primary}` (#573837). White copy, navigation links, and legal text render in `{typography.body-sm}` and `{typography.caption}` on the mahogany ground. Three to four columns on desktop (brand column, collections, customer service, newsletter signup) collapse to a stacked single column on mobile. No hairline top border — the color shift from white canvas to mahogany is separation enough.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with drawer on `{colors.primary}` ground; hero stacks text above image at full width; pen-detail-panel stacks below image with sticky add-to-cart bar at bottom; section padding reduces to `{spacing.lg}` |
| Tablet | 744–1128px | Two-column product grid; nav bar retains horizontal links; hero splits 50/50 text and image; pen-detail-panel sits right of image in 40/60 split |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; hero uses 45/55 text/image split; pen-detail-panel in 50/50 layout |
| Wide | > 1440px | Content max-width 1400px centered; four-column product grid; hero text block caps at 560px; extra whitespace absorbed by outer margins |

### Touch Targets

- All buttons minimum 48px tall and 44px wide
- Nav links padded to a minimum 44px tap height
- Ink swatches scale from 32px on desktop to a minimum 40px diameter on mobile
- Spec badges grouped with `{spacing.xs}` gaps; combined spec-area tap zone targets 44px minimum

### Collapsing Strategy

- Nav collapses to logo + hamburger below 744px; drawer slides left over a solid `{colors.primary}` overlay background
- Hero image de-prioritizes below tablet; text block takes full width with minimum 40px vertical padding
- Product grid steps: 1 col < 744px → 2 col 744–1128px → 3 col 1128–1440px → 4 col > 1440px
- Footer multi-column grid stacks to single centered column at < 744px; newsletter input goes full width
- Pen detail panel transitions from side-by-side (≥744px) to stacked with a fixed-bottom add-to-cart bar at < 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom or licensed typeface detected; Geneva and Verdana are system fonts only — brand may use a commissioned display face loaded via JS or a third-party CDN that was not captured in extraction
- Only three distinct hex colors extracted; accent usage hierarchy (when #00ccff vs. #092fb8 is preferred) is inferred from color-theory contrast roles, not confirmed from live component inspection
- No dark mode or alternate surface palette detected
- No animation timing, easing, or transition values extracted — hover durations and page transitions are inferred as conventional (150–200ms ease)
- No confirmed icon set or illustration system — nib, barrel, and converter glyphs likely exist in the product UI but were not extractable
- Exact product grid column gutters and breakpoints not confirmed from computed styles
- No shadow scale beyond the product card hover state — full elevation system may be minimal
- No confirmed typeface weight range; Geneva and Verdana have limited weight axes (regular and bold), so intermediate weights (500, 600) may render as bold on some platforms
