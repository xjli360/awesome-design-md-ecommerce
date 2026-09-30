---
version: alpha
name: "Bario Neal"
source_url: "https://www.barioneal.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every ring in the Bario Neal catalog arrives against surfaces pale enough to read as the absence of color — a deliberate visual silence that concentrates the eye entirely on hand-formed metal and ethically sourced stone. The single extracted structural anchor is #313131, a dense charcoal that governs all typographic ink and border rules without tipping fully into pure black; this one shade carries the compositional weight that louder brands distribute across multi-color accent families. The surrounding palette is a warm neutral system — parchment whites (#f9f8f6) and clean canvas (#ffffff) that read closer to raw linen than clinical digital white, with hairlines at a barely-tinted off-tone (#e8e4de) that segment content without asserting territory.

  Navigation is architecturally spare: a compact row of category names over a full-width editorial hero, letting stone color and metal finish set all tonal mood. Product cards rest in minimal sharp-cornered containment at {rounded.none} to {rounded.xs}, mirroring the precision geometry of metalwork rather than the soft-pill vocabulary of mass-market ecommerce. Primary actions present as sober dark rectangles rather than rounded fills — the commerce infrastructure is visible but deliberately un-aggressive. Type runs in system sans-serif stacks at restrained weights, with display lines at generous letter-spacing (0.08–0.12em) that signal spaciousness over urgency. Body copy sits at 14–15px with tall leading tuned for the long material-description reads that educated jewelry buyers expect.

  No decorative noise competes with gemstone photography. The brand's Philadelphia studio character — handcraft, ethical sourcing, measured precision — shows in a UI where #313131 and white carry all tonal responsibility, margins are wide, {spacing.section} breaks separate catalog tiers generously, and the overall grid breathes like a portfolio rather than a retail shelf. Inquiry and consultation flows favor simple outlined inputs on the warm canvas, and custom-ring CTAs carry the same visual weight as standard add-to-cart buttons, signaling that bespoke commissions are a primary transaction mode rather than a specialty service.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#b0b0b0"
  ink: "#313131"
  body: "#4d4d4d"
  muted: "#7a7a7a"
  muted-light: "#a8a8a8"
  hairline: "#e8e4de"
  canvas: "#ffffff"
  surface-soft: "#f9f8f6"
  surface-card: "#ffffff"
  surface-warm: "#f3ede8"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.10em
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.08em
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.05em
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.06em
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.04em
  label-caps:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.10em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.06em
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    borderBottom: "1px solid {colors.ink}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  text-input-label:
    textColor: "{colors.muted}"
    typography: "{typography.label-caps}"
    marginBottom: "{spacing.xs}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoWidth: 140px
  nav-bar-mobile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  product-card-name:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.body}"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    minHeight: 80vh
    paddingX: "{spacing.xxl}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
  category-band:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    paddingY: "{spacing.section}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    borderBottom: "1px solid {colors.hairline}"
    activeIndicator: "2px solid {colors.ink}"
    height: 48px
  material-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  inquiry-cta:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    paddingY: "{spacing.section}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.nav-link}"
    paddingY: "{spacing.section}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.muted-light}"
    typography: "{typography.caption}"
    activeTextColor: "{colors.ink}"

## Components

### Buttons

**`button-primary`** — A flat #313131 rectangle with zero border-radius and uppercase letter-spaced type at 13px/500 weight. The shape echoes a ring shank's clean-cut geometry. Active state deepens to `{colors.primary-active}` (#1a1a1a); disabled reduces to `{colors.primary-disabled}` with the same letterform treatment. Height is fixed at 48px with 32px horizontal padding, making it optically wide and grounded rather than compact.

**`button-secondary`** — Transparent background, 1px `{colors.ink}` border, identical uppercase typography and 48px height to the primary. On hover, the border floods with `{colors.primary}` fill and the text inverts to `{colors.on-primary}`, so both button variants converge visually in active states. The two-state convergence prevents any ghost-button ambiguity on interaction.

**`button-text`** — No fill, no box border. A 1px bottom-border underline is the sole affordance. Used for secondary editorial actions ("Learn about our sourcing," "View all settings") where adding a boxed button would compete with nearby product content.

### Text Input

**`text-input`** — Minimal outlined field with sharp corners and a `{colors.hairline}` border that steps up to full `{colors.ink}` on focus. Labels are set in `{typography.label-caps}` — uppercase 11px at 500 weight — rendering above the field in `{colors.muted}`, a treatment borrowed from print jewelry order forms. The 48px height aligns precisely with `button-primary` for side-by-side form row layouts.

### Navigation

**`nav-bar`** — A clean 72px white bar with a wordmark logo at roughly 140px wide, category links in 13px/400 weight, and a 1px `{colors.hairline}` base rule. No visual complexity in the bar itself; the brand name anchors the left and the category links sit right or center with generous inter-link spacing. Dropdown panels appear as simple flat sheets on `{colors.surface-soft}` with no elevation shadows. Mobile collapses to 60px with a minimal hamburger that opens a right-side drawer on `{colors.canvas}`.

### Product Card

**`product-card`** — Sharp-cornered tiles on `{colors.surface-soft}` background, 3:4 portrait image ratio tuned for ring and hand photography. Name in `{typography.title-sm}`, price in `{typography.price-display}` at `{colors.body}` weight. No hover overlays or quick-add floating buttons — the entire tile is a click-through to the detail page, maintaining the portfolio-browse feel. A `{typography.caption}` material badge may appear overlaid on the image corner for ethical sourcing callouts.

### Hero / Editorial

**`hero-editorial`** — Full-width, minimum 80vh, no fixed height. Editorial title in `{typography.display-xl}` at weight 300 with wide letter-spacing floats above a subtitle in `{typography.body-md}`. CTA buttons sit below with `{spacing.xl}` vertical gap. Background images are pale-toned or desaturated enough that dark ink type reads directly without an overlay scrim — the brand resists darkening its photography to serve text layout.

### Category Band

**`category-band`** — A `{colors.surface-soft}` horizontal strip used between catalog sections, carrying a `{typography.label-caps}` section heading and optionally a short editorial line in `{typography.body-sm}`. Padding at `{spacing.section}` top and bottom creates the wide-breathing rhythm that distinguishes the catalog from a dense product grid.

### Filter Bar

**`filter-bar`** — A 48px sticky row of category or material filter tabs set in `{typography.label-caps}` at `{colors.muted}`. Active tab shifts to `{colors.ink}` with a 2px bottom-border indicator — no pill background, no filled chip. A hairline bottom rule anchors the bar visually. Scrolls horizontally on narrow viewports rather than wrapping to preserve the single-line tab row.

### Material Badge

**`material-badge`** — A compact tag with no radius, 1px `{colors.hairline}` border, and `{typography.caption}` in `{colors.muted}`. Surfaces on product cards and detail pages to communicate sourcing notes (Recycled 14k Gold, Lab-Grown Diamond, Conflict-Free). The intentionally quiet framing prevents these from reading as marketing stamps while still signaling the brand's ethical positioning.

### Inquiry CTA

**`inquiry-cta`** — A full-width warm-surface block on `{colors.surface-warm}` used to promote custom consultation and studio visits. Title in `{typography.display-md}` at weight 300, body in `{typography.body-md}`, a primary button paired with a `button-text` for the secondary action. Padding at `{spacing.section}` top and bottom. Carrying the same visual weight as a standard product section positions bespoke commissions as co-equal commerce rather than a specialty upsell.

### Footer

**`footer`** — Palette inversion: `{colors.primary}` (#313131) background with all text in `{colors.on-dark}`. Navigation columns in `{typography.nav-link}`, legal and secondary content in `{typography.body-sm}`, top padding at `{spacing.section}`. No gradients, no accent color details — the dark footer reads as a definitive visual endpoint after the light-toned catalog above.

### Breadcrumb

**`breadcrumb`** — Placed at the top of product detail pages, using `{typography.caption}` in `{colors.muted}` with "/" separators in `{colors.muted-light}` and the current segment in `{colors.ink}`. Sits 16px from the content area top edge, providing navigational orientation without competing with the product title below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero reduces to 60vh minimum; section padding halves to {spacing.xl}; filter bar scrolls horizontally; inquiry CTA stacks text above buttons |
| Tablet | 744–1128px | Two-column product grid; nav expands to full category links; hero returns to 70vh; category band and inquiry CTA maintain two-column layouts |
| Desktop | 1128–1440px | Three or four-column product grid; full nav with hover dropdown panels; hero at 80vh minimum; filter bar sticks on scroll |
| Wide | > 1440px | Content container capped at ~1440px and centered; grid holds at four columns; hero may expand to full-bleed with max-width text column |

### Touch Targets

- All buttons and nav links maintain a minimum 44×44px tap target on touch viewports.
- Filter bar tabs expand to 48px height on mobile to meet tap-target requirements.
- Product card entire tile is the tap region, not the image alone.
- Material badges are display-only on mobile; no interactive tap behavior.

### Collapsing Strategy

- Navigation collapses to a hamburger icon below 744px; the drawer slides in from the right on a `{colors.canvas}` background with full category list and a close control.
- The inquiry CTA section stacks headline, body copy, and buttons into a single centered column below 744px.
- Product card titles truncate to two lines on narrow viewports; price always displays in full.
- Footer columns reflow to a single stacked list below 744px with increased vertical spacing between groups.
- The hero's display-xl text scales down to the display-md size token below 744px to prevent overflow on short text containers.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site was behind Cloudflare anti-bot protection during extraction ("Just a moment…" page title); only one hex color (#313131) was recovered — full palette is unavailable from live-site extraction.
- No custom or licensed brand typeface was detected; only system-UI fallback stacks are present. Bario Neal likely uses a licensed serif or geometric sans for display — the typography definitions here should be replaced once the actual typeface is identified.
- All surface and hairline colors (surface-soft, surface-warm, hairline) are inferred from fine jewelry brand character, not extracted. Verify against actual site once accessible.
- No meta theme-color was set; canonical brand accent or highlight color (if any beyond charcoal) is unknown.
- Whether a UI-level gold or warm-metal accent token exists in the digital system is unconfirmed; none was added due to insufficient extraction evidence.
- Component-level animation durations, box-shadow values, and hover transition timing are not available and have been omitted.
- Product detail page layout (ring configurator, stone selector, size picker) structure is inferred from jewelry category conventions, not observed directly.
