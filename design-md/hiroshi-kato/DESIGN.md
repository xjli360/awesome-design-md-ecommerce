---
version: alpha
name: "Hiroshi Kato"
source_url: "https://kato-brand.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Raw selvedge and the slow accumulation of earned character: Hiroshi Kato arrives online anchored by a deep jade teal (#108474) that reads less like a corporate primary and more like a pigment pulled from centuries of Japanese natural dyeing — shibori indigo reduced to its bluer registers, then shifted green by oxidation and time. That teal carries every primary CTA, active nav underline, and announcement bar on a canvas of near-whites (#fafafa, #f9fafb) and layered warm grays (#eeeeee, #f2f2f2, #e9e9e9), the kind of tonal field that lets cloth photography do the selling without competing signals. A secondary earth palette runs beneath: burnt sienna (#b2591f) and amber (#a36710) connect to the iron-rich finishes, vegetable tannins, and oxidized copper hardware that characterize the brand's material vocabulary. Marigold (#fbcd0a) appears as a sharp promotional accent — sale badges, limited-drop callouts — crisp against the muted field without contaminating it. Type pairs Baskerville for display and editorial work — its bracketed serifs carrying the weight of craft-manifesto photography without requiring bold — against Nunito Sans for all UI, navigation, and body copy, a humanist sans that reads warm and direct. Button labels run Nunito Sans all-caps at 700 weight with generous letter-spacing, closer to a woven label than a screen UI convention, reinforcing the garment-world heritage even in interactive states. Corners are deliberately restrained: `{rounded.xs}` at 2px on buttons reads as almost-none, and `{rounded.none}` on product card imagery keeps the textile flush with the grid — there is no softening of the cloth's own edge. The `{spacing.section}` rhythm gives product photography sustained room to breathe, trusting the fabric's texture and colorway over copy density.

colors:
  primary: "#108474"
  primary-active: "#0c6b5e"
  primary-disabled: "#c1e6e6"
  primary-light: "#c1e6e6"
  accent-rust: "#b2591f"
  accent-amber: "#a36710"
  accent-marigold: "#fbcd0a"
  accent-lavender: "#a89cc8"
  ink: "#202020"
  ink-deep: "#121212"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#888888"
  hairline: "#dadada"
  hairline-soft: "#e9e9e9"
  hairline-faint: "#eeeeee"
  canvas: "#fafafa"
  canvas-warm: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale-badge: "#fbcd0a"
  sale-badge-text: "#202020"

typography:
  display-xl:
    fontFamily: "Baskerville, 'Noto Serif', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Baskerville, 'Noto Serif', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Baskerville, 'Noto Serif', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label-caps:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.2px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  price-display:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0

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
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "13px 31px"
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "12px 16px"
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-faint}"
  nav-bar-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageRounded: "{rounded.none}"
    cardRounded: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    gap: "{spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 600px
    padding: "{spacing.section}"
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl}"
    rounded: "{rounded.none}"
  collection-header:
    backgroundColor: "{colors.canvas-warm}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    descriptionTypography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.ink}"
  size-swatch:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    size: 40px
  size-swatch-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  size-swatch-unavailable:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    textDecoration: line-through
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    height: 36px
  tag-label:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.label-caps}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline-faint}"
    headingTypography: "{typography.label-caps}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — The primary CTA surface runs #108474 (jade teal) with white text in Nunito Sans 13px/700 weight and 1.2px letter-spacing — all-caps like a woven garment label rather than a digital affordance. At 48px height with 2px rounding that functionally reads as none, the button communicates certainty without softness. Active state deepens to #0c6b5e; disabled falls back to the pale teal of #c1e6e6 with muted gray text, keeping the color family intact even in unavailable states.

**`button-secondary`** — Transparent field with a 1px ink (#202020) border and matching all-caps label at identical height and padding to primary. Used for secondary actions on product pages — "Add to Wishlist," "Size Guide," auxiliary collection CTAs — where the primary action is already occupied by the teal button.

**`button-ghost`** — Teal border (#108474) with teal text on a transparent ground. Reserved for editorial landing sections and campaign modules where the primary teal is already the dominant surface color and a solid fill would collapse into background rather than pop.

### Navigation

**`nav-bar`** — Near-white (#fafafa) ground at 64px height, separated from page content by a faint #eeeeee bottom border rather than a shadow. Nav links at 14px Nunito Sans 600 with subtle 0.3px tracking sit beside the wordmark and icon controls. The active link underlines in a 2px #108474 rule; hover shifts the label to teal without the rule, keeping the active state clearly distinguished. No mega-menu chrome — category labels expand to simple dropdown lists.

### Product Card

**`product-card`** — Zero rounding on both the image frame and the card container; the product photograph bleeds flush to the grid edge, respecting the textile's own boundary rather than imposing a UI crop. Product name renders in 14px Nunito Sans 600 at #202020; price below at the same size and weight, same color unless discounted. On hover, most cards swap to a secondary colorway or back-of-garment detail without additional UI overlay. Sale badges sit at the image's top-left corner in marigold (#fbcd0a) with ink text in label-caps — high contrast against virtually any garment color.

### Size Swatches

**`size-swatch`** — 40px square tiles with 2px rounding, rendered in white with a #dadada hairline border and ink label-caps text. Active state fully inverts: black fill (#202020), white text, black border — a clean binary that avoids the ambiguity of a partial-fill or checkmark overlay. Unavailable sizes remain in the grid at reduced opacity with a strikethrough rather than vanishing; the complete size range stays legible, honest about stock without hiding the scope of the offering.

### Hero

**`hero-banner`** — Full-bleed dark canvas (#121212) for campaign photography, headline in Baskerville 48px/400 weight at white, sub-copy in Nunito Sans body-md. Minimum 600px height on desktop. The serif weight at 400 — not bold — carries gravitas through letter form rather than mass, consistent with the brand's restraint. CTA renders in the white-on-teal primary button variant, usually left-anchored against a portrait-oriented campaign image.

**`hero-editorial`** — A softer campaign module using #f2f2f2 as a warm light background for material-sourcing narratives, craft methodology, or capsule collection stories. Baskerville 32px headline above Nunito Sans 16px body paragraphs, generous `{spacing.xxl}` padding on all sides. No rounding on the container — it sits flush with the content column.

### Collection Header

**`collection-header`** — A canvas-warm (#f9fafb) band above the product grid with the collection name in Baskerville 22px and a short descriptor in Nunito Sans 16px below. A hairline bottom border (#dadada) cleanly separates it from the filter row and grid. Used on all category and filtered collection pages.

### Filters

**`filter-pill`** — Pill-shaped tags (`{rounded.full}`) in #f2f2f2 with a hairline border for unselected state; tapping inverts to ink fill with white label. The pill form creates deliberate contrast with the brand's otherwise angular, no-radius component language — filter controls are visually distinct from static UI elements, making the interactive layer immediately readable on dense collection pages.

### Announcement Bar

**`announcement-bar`** — A 36px teal (#108474) strip pinned above the nav, white label-caps text horizontally centered. Carries shipping thresholds, limited-run alerts, or seasonal promotional copy. Because the primary teal appears nowhere else in the nav zone, the announcement bar seeds brand color at the very top of every page load before photography renders.

### Footer

**`footer`** — Deep ink (#121212) ground, the darkest surface in the system. Section headings in Nunito Sans 11px all-caps 700 with 1.5px tracking; body links in near-white (#eeeeee) at 14px. Four-column grid on desktop with a brand statement or material philosophy in the leftmost column, followed by navigation, customer service, and social/legal columns. The footer's darkness provides a formal close to each page, consistent with the brand's sense of craft seriousness over approachable warmth.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer + centered wordmark + cart icon; hero headline scales to display-sm Baskerville (~22px); filter pills scroll horizontally in a snap container; size swatches wrap in a tighter grid |
| Tablet | 744–1128px | Two-column product grid; nav may retain visible top-level labels with a condensed layout; hero maintains full image height with display-md Baskerville (~32px); hero-editorial modules shift to side-by-side layout |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with hover-triggered dropdowns; hero at full 600px+ height with display-xl Baskerville at 48px; footer four-column layout |
| Wide | > 1440px | Content max-width caps around 1400px with auto side margins; product grid holds at four columns; hero photography bleeds edge-to-edge with content container centered over it |

### Touch Targets
- All interactive elements maintain a minimum 44×44px touch target on mobile
- Size swatch tiles are 40px rendered but extended to 44px via invisible padding zones
- Nav hamburger and cart icon each provide 48×48px tap zones
- Filter pills have at minimum 44px height on mobile via increased vertical padding

### Collapsing Strategy
- Desktop nav category dropdowns collapse to a slide-in left drawer on mobile, with category headings as tap-to-expand accordion rows
- Four-column product grid collapses through two-column (tablet) to single-column (mobile)
- Hero editorial modules stack vertically on mobile: image full-width above, text block below with `{spacing.lg}` gap
- Footer four-column grid collapses to single-column accordion on mobile with tap-to-reveal link groups
- Announcement bar text may condense or cycle through multiple messages on narrow viewports

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed proprietary brand typeface — Nunito Sans is inferred as the UI font and Baskerville as the display serif from the extracted font stack, but exact usage zones, weights in use, and whether Noto Serif serves as a fallback or primary role cannot be verified without a full CSS audit
- Exact border-radius system is unconfirmed; the xs/sm scale here is inferred from the brand's minimalist, structured menswear aesthetic rather than extracted measurements
- Hover transition durations and easing curves (likely subtle ease-out in the 150–200ms range) are not extractable from static color/font hints
- Dark mode support is unknown — the extracted palette does not reveal a documented inverse theme
- The role of accent-lavender (#a89cc8) is unclear — it may appear for a specific product category, a collaboration capsule colorway, or a seasonal accent rather than a persistent UI token
- Surface-card is assumed to be pure #ffffff (standard Shopify convention) rather than extracted from the palette directly
- Social icon colors (#3b5998, #1da1f2, #dd4b39, #e60023, #0073b1) in the extracted list are third-party brand colors attached to share widgets, not Hiroshi Kato design tokens — excluded from the palette
- Exact nav height, logo lockup dimensions, column gutter widths, and product grid gap values require live DOM inspection to confirm
