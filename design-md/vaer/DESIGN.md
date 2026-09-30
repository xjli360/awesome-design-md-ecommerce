---
version: alpha
name: "Vaer"
source_url: "https://www.vaerwatches.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The entire vaerwatches.com palette resolves to seven shades of gray, and that constraint is the design statement. #1a1a1a anchors every primary surface — buttons, headlines, cart overlays — while a tight cluster of near-identical light grays (#dedede, #e0e0e0, #e1e1e1) handles borders and card surfaces, an extraction artifact that reveals just how little tonal variation the brand tolerates. Mid-tone #8e8e8e carries secondary copy and disabled states; nothing brighter punctuates the grid. There is no accent color. The brand bets entirely on product photography — steel bezels, lume-painted indices, canvas and rubber straps — to supply the chromatic warmth that a conventional palette would provide with a single highlight hex.

  Archivo handles all typographic work. The grotesque's slightly condensed proportions read as functional rather than decorative, a natural fit for the spec-label copy (water resistance depths, case diameters, movement calibers) that Vaer's audience parses before anything else. Uppercase tracking does the hierarchical work that color cannot: `{typography.spec-label}` runs at 0.08em in 600 weight, while display headings lean light — low weight at high point size, trusting the font's geometry over typographic mass.

  Buttons carry `{rounded.none}`: the primary CTA in solid #1a1a1a with white reverse Archivo uppercase; the secondary in white fill with a matching 1px #1a1a1a border, so the two read as a precision pair rather than a conventional marketing hierarchy. No pill shape appears anywhere on the page.

  Product cards lean on full-bleed 1:1 photography, zero rounding, and a thin #dedede hairline border. The information layer is compact: collection name in `{typography.spec-label}` muted gray, model name in `{typography.title-sm}`, case diameter, price. The spec-before-name ordering reflects how this audience shops — by size and collection before any model identifier.

  Collection filters (Field, Diver, Dress, Pilot) use uppercase letter-spaced labels and an underline active state, keeping the system monochrome end to end. The footer flips to a full #1a1a1a dark ground — the one surface where the brand's primary color stretches across the full viewport width, lending the institutional weight that a micro-brand's warranty and origin story needs.

colors:
  primary: "#1a1a1a"
  primary-active: "#121212"
  primary-disabled: "#8e8e8e"
  ink: "#1a1a1a"
  body: "#1a1a1a"
  muted: "#8e8e8e"
  hairline: "#dedede"
  hairline-mid: "#e0e0e0"
  hairline-soft: "#e1e1e1"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#1a1a1a"

typography:
  display-xl:
    fontFamily: "'Archivo', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Archivo', sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Archivo', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Archivo', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Archivo', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Archivo', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Archivo', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Archivo', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "'Archivo', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "'Archivo', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Archivo', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Archivo', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.04em
  collection-label:
    fontFamily: "'Archivo', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    padding: 14px 28px
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
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
  button-ghost-on-dark:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.on-primary}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.06)"
  mobile-nav-overlay:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-sm}"
    position: fixed
    inset: 0
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageBorder: "1px solid {colors.hairline-soft}"
    nameTypography: "{typography.title-sm}"
    specTypography: "{typography.spec-label}"
    priceTypography: "{typography.title-md}"
    textColor: "{colors.ink}"
    specColor: "{colors.muted}"
    padding: "{spacing.md}"
    imageAspectRatio: "1/1"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaVariant: button-ghost-on-dark
    minHeight: 80vh
    imageStyle: full-bleed with text overlay or 50/50 split
  hero-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaVariant: button-primary
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: 6px 10px
    border: "1px solid {colors.hairline}"
  collection-filter:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.collection-label}"
    activeTextColor: "{colors.ink}"
    activeIndicator: "2px solid {colors.primary}"
    padding: "{spacing.sm} 0"
    gap: "{spacing.xl}"
  strap-swatch:
    size: 24px
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.primary}"
    unselectedBorder: "1px solid {colors.hairline}"
    gap: "{spacing.sm}"
  case-size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    rowBorder: "1px solid {colors.hairline-soft}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rowPadding: "{spacing.md} 0"
  movement-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    labelTypography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.surface-soft}"
    headingTypography: "{typography.spec-label}"
    bodyTypography: "{typography.body-sm}"
    legalTypography: "{typography.caption}"
    legalColor: "{colors.muted}"
    dividerColor: "rgba(255,255,255,0.15)"
    padding: "{spacing.section} 0"

## Components

### Buttons
**`button-primary`** — Solid #1a1a1a fill with white Archivo uppercase at 0.08em tracking, strictly square corners (`{rounded.none}`), 48px height. Hover deepens to #121212; disabled collapses to #8e8e8e fill with the same white reverse type, signaling inactivity without introducing a new color. The uppercase letter-spacing is load-bearing: it distinguishes CTAs from body copy in a system that cannot use a color accent to do that work.

**`button-secondary`** — White canvas fill with a 1px #1a1a1a border, matching the primary's height and radius exactly so the two sit as a machined pair. Hover shifts the fill to #f5f5f5 while the border holds. Used for secondary actions ("View All", "Learn More") placed alongside a primary CTA.

**`button-ghost-on-dark`** — Transparent fill with a 1px white border, white uppercase Archivo type. Used exclusively over dark (#1a1a1a) hero backgrounds where a solid primary button would be invisible. Hover fills with rgba(255,255,255,0.1) — the subtlest acknowledgment the system allows.

**`button-text-link`** — Transparent, underline decoration, body-sm weight. Lowest hierarchy action; appears in spec panels, FAQ accordions, and footer secondary links.

### Text Input
**`text-input`** — Zero-radius field with 1px #dedede border, 48px height to align with paired buttons in form rows. Focus replaces the hairline with a full 1px #1a1a1a border — no color shift, just border assertion. Placeholder at #8e8e8e. Used in newsletter subscription and contact forms; the footer variant inverts to transparent fill with a 1px white border for placement on the dark footer ground.

### Navigation
**`nav-bar`** — 64px white bar with 1px #dedede bottom border. Wordmark left, collection links center or right-clustered, cart and account icons rightmost. Archivo 13px at 0.04em tracking for nav links; hover applies an underline rather than a weight change or color shift. On scroll, a soft box-shadow lands without altering the white background — depth through shadow, not color.

**`mobile-nav-overlay`** — Full-screen #1a1a1a takeover triggered by the hamburger. Collection links render in `{typography.display-sm}` white Archivo, stacked with generous line spacing. The overlay is one of only two places the primary color covers a full viewport surface (the other being the footer), giving mobile navigation a deliberate gravity that matches the watch category's purchase weight.

### Product Card
**`product-card`** — Square 1:1 photography, 1px #e1e1e1 image frame, no card shadow, no rounding anywhere. Below the image: collection name in `{typography.spec-label}` at #8e8e8e, model name in `{typography.title-sm}` at #1a1a1a, case diameter in spec-label weight, then price in `{typography.title-md}`. The spec-before-name stack reflects how Vaer's audience shops — by size and collection tier before model designation. No star rating or review count appears in the card grid; social proof lives on the detail page.

### Hero
**`hero`** — Full-bleed #1a1a1a dark ground or a 50/50 split with product photography on one side. Headline in `{typography.display-xl}` at weight 400 — the low weight against a large point size is deliberate, avoiding the heaviness of a 700-weight display in a brand that relies on restraint. CTA renders as `button-ghost-on-dark` (white border, white type) over the dark background. A white or `{colors.surface-soft}` subhead at `{typography.body-md}` sits below the headline.

**`hero-light`** — Secondary landing sections use `{colors.surface-soft}` as the ground with `{colors.ink}` type and a standard `button-primary` CTA. Deployed for collection introductions and brand story blocks midpage.

### Spec Badge
**`spec-badge`** — Small rectangular tag in #f5f5f5 with a 1px #dedede border, `{typography.spec-label}` uppercase. Used inline on the product detail page to surface key attributes: "200M WR", "Swiss Automatic", "Sapphire Crystal", "MIL-SPEC". Multiple badges sit in a horizontal wrapping row. The flat rectangle with no rounding is the spec system's irreducible visual atom.

### Collection Filter
**`collection-filter`** — Horizontal strip of uppercase, letter-spaced collection names. Inactive labels in #8e8e8e; active state brings the label to #1a1a1a and adds a 2px underline bottom border. No filled pill or background tile — the monochrome system cannot absorb a pill fill without creating a false color hierarchy. On desktop the strip runs full-width below the nav; on mobile it becomes a horizontal scroll container with snap points.

### Strap Swatch Selector
**`strap-swatch`** — 24px circular swatches for strap color and material. Selected state gains a 2px #1a1a1a ring with a 2px gap between swatch and ring; unselected uses a 1px #dedede border. Swatches are the only location on the product detail page where colors outside the gray palette appear (the actual strap material colors), making them a natural focal anchor. On mobile swatches grow to 36px for touch clearance.

### Case Size Selector
**`case-size-selector`** — Borderless-adjacent toggle group for mm sizing (36mm, 39mm, 42mm). Unselected: white fill, 1px #dedede border, muted `{typography.spec-label}` text. Selected: #1a1a1a fill, white type — matching the primary button's logic applied to a segmented control. Buttons share borders so the group reads as a single machined selector strip.

### Spec Table
**`spec-table`** — Two-column key-value layout on the product detail page. Label column in `{typography.spec-label}` at #8e8e8e; value column in `{typography.body-sm}` at #1a1a1a. Rows separated by 1px #e1e1e1 hairlines, no zebra striping, no background alternation. The label/value pair is the unit of meaning and never collapses to stacked on any breakpoint — preserving the horizontal scanning pattern that watch buyers use when comparing specifications.

### Movement Callout
**`movement-callout`** — Full-width #f5f5f5 section block that foregrounds the movement inside a reference (e.g., "Swiss Sellita SW200-1 — 26 Jewels, 28,800 vph"). Headline in `{typography.display-sm}`; key stats listed in a two- or three-column `{typography.spec-label}` grid below. No rounding, `{spacing.xxl}` padding, optional close-up movement photograph. Sits mid-page on the product detail page, breaking the scroll before the spec table.

### Footer
**`footer`** — Full #1a1a1a dark ground, white type throughout. Column headings in `{typography.spec-label}` uppercase; link lists in `{typography.body-sm}`. Columns: Watches (by collection), Support (FAQ, Warranty, Returns), Company (About, Press, Careers). Newsletter row uses a transparent-fill, white-bordered text input with an inline submit icon. Copyright and legal links appear below a `rgba(255,255,255,0.15)` divider in `{typography.caption}` at #8e8e8e.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to wordmark + hamburger triggering full-screen dark overlay; hero goes full-bleed stacked (image above, text/CTA below); collection filter becomes horizontal scroll strip with snap points; spec table stays two-column |
| Tablet | 744–1128px | 2-column product grid; nav retains wordmark and icons, collection links collapse to hamburger or truncate to 3 visible; hero switches to 50/50 split; movement callout goes single-column |
| Desktop | 1128–1440px | 3-column product grid; full nav with all collection links visible; hero at full min-height 80vh with split or overlay layout; movement callout 2-column with image |
| Wide | > 1440px | Grid and content max-width capped (~1280px) and centered; hero content constrained within max-width; footer columns spread across full width with gutter margins |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Case size selector buttons expand to 44px height on mobile from desktop default
- Strap swatches grow from 24px to 36px on mobile with proportional ring gap
- Nav icons (cart, account, hamburger) padded to 44px tap target regardless of visible icon size
- Collection filter labels padded vertically to 44px hit area on mobile horizontal scroll

### Collapsing Strategy
- Collection filter collapses to horizontal scroll with momentum and snap points on mobile; no wrapping, no visible scroll bar
- Spec table remains two-column at all breakpoints — label/value pairing is the unit and never stacks
- Product card information layer maintains full compact format at all sizes; no info fields are hidden on mobile
- Hero image promotes to top position on mobile with headline and CTA stacked below, maintaining full-width bleed
- Footer columns reflow to a 2-column grid on tablet and a single stacked column on mobile; newsletter row goes full-width last

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No accent or highlight color extracted — the entire palette is neutral grays; if Vaer uses a color accent for sale banners, in-stock indicators, or limited-edition flags, it was not captured in this extraction
- Footer background may use #121212 (also extracted) rather than #1a1a1a — the two are visually indistinguishable at a glance but are distinct tokens; a live DOM inspection would confirm which token each surface uses
- Exact nav height not confirmed from extraction; 64px is an estimate based on independent micro-brand watch site conventions
- No secondary typeface detected — Vaer may use a serif or condensed grotesque for editorial campaign sections; only Archivo confirmed from the stack
- Button corner radius not confirmed from static extraction; `{rounded.none}` assumed from the brand's industrial-functional positioning
- Hover and focus transition durations and easing curves not available from static extraction
- Collection-specific accent colors not captured — some Vaer dial colorways (navy, olive, cream) may feed into section theming or filter active states in ways the gray extraction cannot represent
- Image lazy-load placeholder color and skeleton screen treatment not confirmed
