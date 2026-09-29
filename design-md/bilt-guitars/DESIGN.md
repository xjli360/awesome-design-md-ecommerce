---
version: alpha
name: "Bilt Guitars"
source_url: "https://www.biltguitars.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every instrument at Bilt begins as a blank configuration — the site is structured around a spec-builder, not a fixed catalog, which means the UI must simultaneously hold the intimacy of a lutherie conversation and the precision of a parts manifest. The canvas is near-black, running from #110c1d at the deepest hero moments to #1a1230 in panel backgrounds, a darkness that evokes the velvet interior of a hard-shell case rather than a generic dark-mode treatment. Against this field, the brand's primary action color is a deep navy #003388 — a restrained choice that carries every call-to-action ("Start Building," "Add to Cart," spec confirmation) while resisting the excitability of the brighter colors elsewhere in the extracted palette.

  The accent system runs two deliberate temperatures. Warm amber (#a88548) marks wood-selection callouts and material labels, mapping visually to the maple tops and mahogany backs photographed in product previews — a color that smells like a workshop. Electric green (#00d084) is reserved exclusively for selection-confirmed state inside the configurator: option swatches glow with a faint rgba wash and a 2px border in that color at `{rounded.xs}`, making the "you chose this" signal unmissable even on near-black surfaces where standard focus rings disappear. The pairing of these two accent temperatures against the dark canvas creates a visual language closer to workshop instrumentation than to a retail storefront.

  Type is set in gdsherpa, an uncommon face that carries condensed authority at display sizes and stays legible as a spec label at 11px uppercase with tracking. Button text runs uppercase, reinforcing the precision-spec register. Rounded corners are held deliberately tight — `{rounded.xs}` on interactive elements, `{rounded.sm}` on cards — keeping every surface angular enough to feel machined rather than lifestyle-softened. The configurator's option grids run on dense `{spacing.sm}` gutters that breathe out to `{spacing.section}` between major content bands, giving the hero room to photograph each body silhouette in full while keeping the builder UI compact and scannable.

  Flashes of violet (#7a00df, #ab1dfe) and cyan (#34e2e4, #31cdcf) appear in the extracted palette but almost certainly belong to WordPress Gutenberg block-editor defaults or one-off promotional overlays rather than the core brand system; they are noted in Known Gaps and excluded from primary tokens.

colors:
  primary: "#003388"
  primary-active: "#020381"
  primary-disabled: "#256bed"
  accent-gold: "#a88548"
  accent-electric: "#00d084"
  ink: "#111111"
  body: "#313131"
  muted: "#444444"
  hairline: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#32373c"
  surface-dark: "#1a1230"
  surface-darkest: "#110c1d"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  selection-wash: "rgba(0, 208, 132, 0.12)"
  scrim: "rgba(0, 0, 0, 0.72)"

typography:
  display-xl:
    fontFamily: "'gdsherpa', system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -1px
  display-lg:
    fontFamily: "'gdsherpa', system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'gdsherpa', system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'gdsherpa', system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: 0
  title-md:
    fontFamily: "'gdsherpa', system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'gdsherpa', system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'gdsherpa', system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'gdsherpa', system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'gdsherpa', system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'gdsherpa', system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  micro-label:
    fontFamily: "'gdsherpa', system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-lg:
    fontFamily: "'gdsherpa', system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'gdsherpa', system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'gdsherpa', system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'gdsherpa', system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px

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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    opacity: 0.5
    rounded: "{rounded.xs}"
  button-primary-lg:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 36px
    height: 56px
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.on-dark}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-ghost-gold:
    backgroundColor: "transparent"
    textColor: "{colors.accent-gold}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.accent-gold}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.muted}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid rgba(255,255,255,0.08)"
    logoPosition: left
    ctaPosition: right
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageRounded: "{rounded.xs}"
    imageAspectRatio: "4/3"
  hero:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    subColor: "{colors.hairline}"
    minHeight: 100vh
    imageAlignment: center
    ctaMarginTop: "{spacing.xl}"
  configurator-panel:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid rgba(255,255,255,0.08)"
    groupLabelTypography: "{typography.spec-label}"
    groupLabelColor: "{colors.accent-gold}"
    groupGap: "{spacing.lg}"
  option-swatch:
    size: 32px
    rounded: "{rounded.xs}"
    borderUnselected: "1px solid {colors.muted}"
    borderSelected: "2px solid {colors.accent-electric}"
    backgroundSelected: "{colors.selection-wash}"
    gap: "{spacing.sm}"
  spec-badge:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.accent-gold}"
    typography: "{typography.spec-label}"
    border: "1px solid {colors.accent-gold}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  category-filter:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.muted}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted}"
    activeColor: "{colors.on-dark}"
  wood-preview-caption:
    textColor: "{colors.accent-gold}"
    typography: "{typography.micro-label}"
    letterSpacing: 1.2px
  section-divider:
    borderTop: "1px solid rgba(255,255,255,0.08)"
    marginTop: "{spacing.section}"
    marginBottom: "{spacing.section}"
  footer:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.accent-electric}"
    borderTop: "1px solid rgba(255,255,255,0.08)"
    padding: "{spacing.xxl} 0"
    columns: 3

## Components

### Buttons

**`button-primary`** — Navy (#003388) fill at 48px tall with `{rounded.xs}` corners and uppercase gdsherpa at 14px/700/0.8px tracking; this is the workshop-spec register, not a lifestyle CTA. Hover state deepens to #020381 (`primary-active`); a disabled state shifts to the lighter #256bed with reduced opacity. The `button-primary-lg` variant at 56px height and 16px type is used for the hero's singular "Start Building" action, where it needs to read clearly against a full-bleed instrument photo.

**`button-secondary`** — A transparent-fill button with a 1px white border on dark surfaces, holding the same 48px height and uppercase treatment as the primary. Designed to appear beside the primary on hero and product-detail sections where two actions coexist — "Build" and "View Specs" — without one overwhelming the other. On light-canvas sections the border color inherits `{colors.ink}`.

**`button-ghost-gold`** — A smaller 36px ghost button in amber (#a88548) used in material-selection and wood-preview contexts. Its gold border against the dark surface echoes the warmth of the instrument photography and reinforces the material-callout register without competing with the primary navy CTA.

### Text Input

**`text-input`** — Inputs sit on the surface-darkest (#110c1d) ground with a 1px muted border at `{rounded.xs}`, standing 48px tall to match button targets for visual rhythm. Placeholder text renders in muted (#444444); focus state sharpens the border to the primary navy (#003388) — a subtle but clear active signal against the dark field. The form is intentionally minimal and unstyled beyond this: Bilt's contact and lead-capture forms are brief, treating the configurator as the primary interaction rather than a shopping cart.

### Nav Bar

**`nav-bar`** — A 64px-tall fixed header on surface-darkest (#110c1d), separated from content by an 8%-white-alpha bottom border that is almost invisible but holds the layer separation on dark page sections. Navigation links run in `{typography.nav-link}` (14px/600/0.3px tracking) in on-dark white; the logo lockup anchors left; a `button-primary` CTA ("Build Your Guitar") sits at the right edge. On scroll, no background change — the header remains static in opacity and color because the page background is already dark.

### Product Card

**`product-card`** — Cards live on the surface-card ground (#32373c) with `{rounded.sm}` corners and 16px internal padding. The model name renders in `{typography.title-md}` (18px/600) in on-dark white; a two-line spec summary in `{typography.body-sm}` sits below in muted (#444444). A `spec-badge` in the card's lower corner labels the body style — Single Cut, Double Cut, Semi-hollow — giving the catalog grid a scannable taxonomy without additional UI chrome. The card image uses a 4:3 aspect ratio with `{rounded.xs}` corners, photographed against a neutral dark ground so the wood grain reads clearly.

### Hero

**`hero`** — Full-viewport-height section on surface-darkest (#110c1d) with a large studio silhouette or in-use instrument photograph filling the majority of the frame. The headline runs in `{typography.display-xl}` (48px/700/−1px tracking); a single-sentence sub-copy line in `{typography.body-md}` with hairline (#eeeeee) color sits below. One `button-primary-lg` ("Start Building") is the sole CTA — there are no carousels, no parallax, no competing links. The guitar's silhouette does the persuading; the headline names what it is.

### Configurator Panel

**`configurator-panel`** — The builder UI occupies a two-column layout: instrument preview left, option groups right. The option panel sits on surface-dark (#1a1230) with `{rounded.sm}` corners, 24px internal padding, and a faint 8%-white-alpha border to lift it visually off the page ground. Each option group carries a `{typography.spec-label}` heading in amber (#a88548) — "BODY STYLE," "FINISH," "PICKUPS," "NECK" — followed by a grid of `option-swatch` chips. Group spacing is `{spacing.lg}` between categories and `{spacing.sm}` between individual swatches.

### Option Swatches

**`option-swatch`** — 32px square chips at `{rounded.xs}`, containing either a material thumbnail (wood grain, finish photo, hardware close-up) or a text label for non-visual options. Unselected state shows a 1px muted border; selected state transitions to a 2px electric-green (#00d084) border with a `{colors.selection-wash}` background tint — rgba(0,208,132,0.12). Because this green appears nowhere else in the UI, selection state is impossible to confuse with hover or focus. Swatches expand to 44px minimum on touch viewports.

### Spec Badges

**`spec-badge`** — Rectangular labels with no border-radius (`{rounded.none}`), amber (#a88548) text on surface-darkest (#110c1d), framed by a 1px amber border. Typography is `{typography.spec-label}` (11px/700/uppercase/1px tracking). Used to label body style, scale length, and pickup configuration in catalog grids and on product cards. The zero-radius treatment is intentional — badges should read like data tags stamped on a parts bin, not like lifestyle chips.

### Category Filter

**`category-filter`** — Small inline filter pills on transparent ground with a 1px muted border, rendered in `{typography.button-sm}`. Active state fills with primary navy (#003388) and shifts text to on-primary white. Used above catalog grids to filter by model family or body style. The `{rounded.xs}` corner matches all other interactive elements in the system.

### Footer

**`footer`** — Dark footer on surface-darkest (#110c1d) with a faint top border, body text in muted (#444444) at `{typography.body-sm}`, and nav links in on-dark white at the same scale. Three-column layout at desktop (About / Build / Legal), stacking to single column on mobile. Social icon links render in on-dark white at 24×24px; hover shifts to accent-electric (#00d084) — the only place the green appears outside of the configurator, connecting the "confirmed selection" energy to outbound links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout; configurator stacks to preview above, option groups below as accordion; nav collapses to hamburger icon at 44×44px; hero headline drops to `display-md` (28px); option swatches expand to 44px touch targets; product grid at 1 column |
| Tablet | 744–1128px | Configurator shows two-column at tighter gutters; product card grid at 2 columns; nav shows primary links and hides secondary items; hero headline at `display-lg` (36px) |
| Desktop | 1128–1440px | Full two-column configurator with side-by-side preview and option panel; product grid at 3 columns; nav fully expanded with all links visible |
| Wide | > 1440px | Content max-width caps at 1440px with auto side margins; hero image scales to fill via object-fit cover with letter-box effect; product grid holds at 3 columns with wider card padding |

### Touch Targets

- Option swatches expand from 32px to 44px minimum on mobile and tablet
- Primary and secondary buttons maintain 48px height across all breakpoints
- Nav hamburger touch target is 44×44px with 8px padding on all sides
- Footer link rows gain 8px additional vertical padding on mobile for comfortable tapping
- Spec badges add 4px vertical padding on mobile to increase tap area

### Collapsing Strategy

- Configurator option groups collapse to an accordion by category on mobile; only one group is open at a time to avoid scroll depth
- Product grid: 3-col → 2-col → 1-col as viewport narrows
- Category filter strip switches from inline row to a horizontally scrollable strip on mobile; no line-wrapping
- Footer columns collapse to a single stacked list at mobile; social icons move to the top of the footer stack above the navigation links
- Nav bar height stays fixed at 64px across all breakpoints; the CTA button collapses to an icon-only state at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Violet (#7a00df, #ab1dfe) and cyan (#34e2e4, #31cdcf) in the extracted palette are likely WordPress Gutenberg block-editor color presets, not brand-owned UI tokens; their actual role in brand UI could not be confirmed
- The canvas background color was not extracted from the live site; #ffffff is assumed for light-mode page sections based on typical WordPress/Gutenberg templates
- No brand-published typography documentation exists for gdsherpa; all font-size, weight, line-height, and letter-spacing values are inferred from visual inspection rather than a design spec
- The exact configurator interaction model (linear step-by-step wizard vs. free-choice option picker) could not be determined from extracted data alone
- No confirmed spacing scale from the live site; values follow a standard 8px-base rhythm as a reasonable default
- Logo lockup proportions, exact wordmark font, and any secondary logomark treatment were not extractable
- Hover and focus animation timing (transition durations, easing) could not be extracted; values in components are structural only and do not specify animation
