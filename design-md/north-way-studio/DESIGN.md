---
version: alpha
name: "The North Way Studio"
source_url: "https://www.thenorthwaystudio.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deeper than the bridal-blush palettes that dominate the category, The North Way Studio anchors its visual language in a near-black forest green (#243125) — a color more at home in pine shadow than on a jewelry pedestal, and exactly the choice that makes the brand feel like a studio rather than a boutique. Against it, honeyed parchment (#f5ebdf) and a barely-there canvas (#fffefc) carry product photography without competition, letting metal surfaces and stone inclusions do the speaking that copy usually crowds out. Warm terracotta-gold (#cd9b77) surfaces as an accent — not the flat corporate gold of mass-market wedding jewelry, but something closer to the tone of reclaimed brass or sun-aged copper, reinforcing the studio's handmade positioning. The muted taupe mid-tones (#bebba4, #e6e2e1) prevent any two surfaces from snapping against each other harshly; every border and card background feels as though it was laid in the same low northern light.

  Type extraction returned no font stacks — the site almost certainly loads its typefaces through a Shopify theme JavaScript bundle — so the typography scale below interprets the visual register of the studio: sparse, unhurried display lines; fine body copy; an avoidance of heavy weight in running text. The display scale skews large and light-weighted at 300–400, consistent with Nordic fine-jewelry studios that treat white space as the primary design element and treat bold as a last resort. Components use `{rounded.none}` almost exclusively — this is a studio that does not reach for the pill or soft-corner radius; edges are kept flat, echoing the angularity of cut stone and hammered band profiles. The ring-sizer, material selector, and consultation-inquiry form are first-class UI surfaces that deserve the same visual gravity as the primary CTA. A warm canvas backdrop (`{colors.surface-soft}`) under editorial text sections prevents the site from reading as a sterile white-box gallery while keeping jewelry photography legible and central.

colors:
  primary: "#243125"
  primary-active: "#1a2519"
  primary-disabled: "#8a9e8c"
  ink: "#111111"
  body: "#333232"
  muted: "#bebba4"
  hairline: "#dedede"
  canvas: "#fffefc"
  surface-soft: "#f5ebdf"
  surface-card: "#e6e2e1"
  on-primary: "#fffefc"
  accent-gold: "#cd9b77"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 1.5px
    textTransform: uppercase
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.3px
  price:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 2px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  label-tag:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.5px
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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-card}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.none}"
    padding: "{spacing.md}"
  product-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label-tag}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 80vh
  material-swatch:
    size: 32px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.primary}"
    borderInactive: "1px solid {colors.hairline}"
  ring-size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderActive: "1px solid {colors.primary}"
    borderInactive: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    chipSize: 44px
  collection-filter-tag:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    borderActive: "1px solid {colors.primary}"
    borderInactive: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    quoteTypography: "{typography.display-sm}"
    attributionTypography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  editorial-band:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    accentRuleColor: "{colors.accent-gold}"
    accentRuleWidth: 40px
    accentRuleHeight: 1px
    padding: "{spacing.section} {spacing.xl}"
  inquiry-form:
    backgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.title-sm}"
    inputBorder: "1px solid {colors.hairline}"
    inputBorderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.muted}"
    bodyTypography: "{typography.body-sm}"
    labelTypography: "{typography.nav-label}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Forest green (#243125) fill with near-white text, uppercase at 2px letter-spacing, zero border-radius on all corners. This flatness signals studio seriousness — no softening for approachability. Active state drops to #1a2519; disabled swaps to the muted sage #8a9e8c, which preserves the green identity without implying interactability. Appears on add-to-bag, consultation submit, and ring-inquiry CTAs.

**`button-secondary`** — Transparent background with a 1px forest-green stroke, same uppercase typographic treatment as the primary. Used in paired-CTA moments ("Enquire" next to "Add to cart") and on editorial callout sections. The hairline border keeps the pairing visually balanced without the secondary reading as inactive.

**`button-ghost`** — No border, no fill; underlined text in near-black (#111111). Surfaces within editorial prose for "Learn more" anchors and in the footer link clusters where underline alone distinguishes it from body copy.

### Navigation

**`nav-bar`** — 64px height on the near-warm-white canvas (#fffefc), separated from page content by a 1px hairline (#dedede). Nav links are uppercase at 12px with 1px tracking — a deliberately quiet register that refuses to compete with photography below. Logo sits centred or left-aligned. On mobile the bar collapses to a hamburger that opens a full-height left-edge drawer over a dark scrim (#121212).

### Product Card

**`product-card`** — Product imagery sits on a warm pale gray (#e6e2e1) background tile with no shadow and no border-radius, so metal and stone surfaces read cleanly against neutral tone. Below the image: product name in `{typography.title-md}` and price in the editorial serif `{typography.price}` — the only serif voice on the card. A row of `{material-swatch}` chips below the price allows metal-variant switching without leaving the collection grid. No hover-reveal; all key information is persistently visible.

### Hero Section

**`hero-section`** — Minimum 80vh, using parchment (#f5ebdf) as the background when photography does not fill the full frame, or as a low-opacity overlay on full-bleed imagery. Heading at `{typography.display-xl}` — 52px, weight 300 — gives the photography room. A single `{button-primary}` anchors below the subheading, never more than one CTA competing for attention in the hero zone.

### Ring Size Selector

**`ring-size-selector`** — A responsive grid of flat square chips (44×44px, no border-radius) displaying EU and US ring sizes. Inactive chips carry a 1px hairline border; the active selection gains a 1px forest-green border. No chip is pre-selected — the absence of a default nudges customers toward the ring-sizer tool or the inquiry form, reinforcing the made-to-measure positioning over transactional self-service.

### Material Swatch

**`material-swatch`** — 32px circular swatches representing metal variants (yellow gold, white gold, rose gold, platinum, sterling). The active swatch is ringed by a 2px primary-green border; inactive swatches carry a 1px hairline. Swatches appear both on the product grid card and on the PDP immediately below the product title — the two surfaces share identical state logic.

### Collection Filter Tag

**`collection-filter-tag`** — Flat rectangular chips with no fill at rest, 1px hairline border. Active filter gains a 1px forest-green border matching the ring-size selector language. Typography is `{typography.button-sm}` uppercase, consistent with every interactive text element on the site. The filter row sits above the product grid on desktop; collapses into a bottom-sheet modal on mobile.

### Testimonial Card

**`testimonial-card`** — Parchment (#f5ebdf) field, no border, no drop shadow, no border-radius. The quote text is set in `{typography.display-sm}` — 24px serif at 400 weight — giving customer language the same editorial display treatment as headline copy. Attribution sits below in `{typography.caption}` at 11px, in the muted taupe (#bebba4) to clearly subordinate it. No star-rating widget: the studio uses full prose testimonials, consistent with a high-touch bespoke service register.

### Editorial Band

**`editorial-band`** — Full-width deep forest green (#243125) strip for mid-page narrative moments: the studio origin story, material sourcing practices, custom-consultation pitch. Heading in `{typography.display-md}` (36px, 300 weight), body in `{typography.body-md}`, both in `{colors.on-primary}`. A 40px horizontal rule in terracotta-gold (#cd9b77) separates the heading from body copy — the only place the accent-gold color appears at full intensity rather than as a swatch reference.

### Inquiry Form

**`inquiry-form`** — Warm parchment background (#f5ebdf) with flat-cornered inputs and 1px hairline borders that sharpen to a 1px forest-green on focus. Labels are uppercase at `{typography.title-sm}`. The form handles both custom ring commissions and in-person consultation bookings — it is a first-class surface, not an afterthought footer widget. Submit button is full `{button-primary}` width on mobile.

### Footer

**`footer`** — Near-black (#111111) ground with near-white (#fffefc) primary text. Column headings in uppercase `{typography.nav-label}`; link text in `{typography.body-sm}` at the muted taupe (#bebba4) to maintain depth without introducing a new color. The terracotta-gold accent is withheld in the footer to keep the dark field visually unified. Four columns on desktop, two on tablet, accordion on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to left-edge hamburger drawer; hero heading drops to `{typography.display-md}`; ring-size chips remain 44×44px, wrap to 5-across; inquiry form fields stack full-width; filter opens as bottom sheet |
| Tablet | 744–1128px | Two-column product grid; nav shows abbreviated labels or partial link set; hero at 60vh minimum; editorial band reduces horizontal padding to `{spacing.lg}`; testimonials collapse to single-column |
| Desktop | 1128–1440px | Three or four-column product grid; full nav links and utility row visible; hero at 80vh with centred text block; editorial band at full `{spacing.section}` padding; filter panel stays persistent above the grid |
| Wide | > 1440px | Grid constrained to 1400px max-width centred; editorial band text block capped at 760px for readability; hero photography scales without stretching the overlay text block |

### Touch Targets
- Ring-size chips minimum 44×44px with 8px gaps
- Material swatches minimum 44×44px on touch viewports (expanded tap area over the 32px visual)
- Nav drawer links minimum 48px tall tap target
- Add-to-bag and inquiry-submit buttons full-width on mobile, minimum 48px height
- Collection filter tags minimum 40px height on touch viewports

### Collapsing Strategy
- Navigation collapses below 744px into a full-height left-edge drawer over `{colors.scrim}` overlay
- Product filtering panel becomes a bottom sheet on mobile, dismissible by swipe-down or backdrop tap
- Testimonials shift from 2-column grid to single-column vertical scroll
- Footer 4-column link grid collapses to 2-column on tablet, then labelled accordion on mobile
- Ring-sizer tool opens as a full-screen modal on mobile; an inline side panel on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font families were detected — the site loads typefaces through a Shopify theme JavaScript bundle or CDN. The typography scale uses Georgia serif and system-sans stacks as stand-ins; actual brand fonts must be confirmed by inspecting loaded `<style>` or theme asset files.
- `#006fcf` is the PayPal Checkout button blue injected by Shopify Payments — excluded from the brand palette.
- `#6bbd4f`, `#fac151`, and `#d84339` appear to be Shopify review-widget or notification-UI colors (green confirm, amber warning, red error), not North Way Studio brand colors — excluded.
- `primary-active` (#1a2519) and `primary-disabled` (#8a9e8c) are derived approximations; the exact interactive-state tokens were not extractable from the live site.
- No breakpoint pixel values confirmed from the extracted data — mobile/tablet/desktop bounds are inferred from Shopify Dawn theme defaults.
- Logo mark details, any monogram or hallmark graphic, and secondary logomark variants were not captured.
- If a ring configurator (mixed-metal, stone-picker, engraving field) exists, its additional UI states are not detailed here.
- Meta theme-color was absent, so the browser chrome color on mobile cannot be confirmed.
