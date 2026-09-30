---
version: alpha
name: "Lelit"
source_url: "https://lelit.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The sharpest corner on a Lelit page is also its loudest signal — a block of flat #fe0000 red against #111111 near-black with no radius, no gradient, no apology. The CTA reads less like an interface affordance and more like the red power indicator on the machines themselves. This is deliberate Italian industrial restraint: the brand does not seduce; it specifies. Eurostile Ext-Med, the extended geometric sans-serif Aldo Novarese drew in 1962, drives every headline and navigation label with the same square authority it lent to Alfa Romeo dashboards and ESA mission patches. Precision-as-typography is not a posture here — it is a lineage.

  The warm greige surface (#e3ddd8) appears as a section-break field behind feature copy and lifestyle photography, introducing just enough warmth to offset chrome and stainless steel machine imagery. Off-whites (#f4f3f1, #fafafa) handle the card and canvas layers, keeping product images clean without the clinical flatness of pure white. The dark navy (#003388) surfaces selectively as a secondary badge and link accent, a nod to archival Lelit catalog colorways without disrupting the red-on-black primary hierarchy.

  Corners are universally square (`{rounded.none}`) across buttons, inputs, product cards, and badges. There is no pill shape, no rounded card, no softened input field anywhere in the system. This orthogonal discipline is the most distinctive spatial decision in the design: it positions Lelit as a precision instrument, not a consumer appliance. Buttons uppercase their labels in Eurostile at tight tracking (0.08em), and the spec table — a grid of boiler temperatures, pump pressures, and portafilter diameters — is the true hero of any product detail page, rendered in a two-column alternating stripe with `{colors.surface-soft}` rows and all-caps `{typography.spec-label}` for the label column.

  Navigation runs at 70px height with a hairline bottom border, the mega-menu capped by a 3px red top rule that signals section entry like a pressure gauge entering the green zone. The footer inverts to #111111 with warm sand link text and red hover states — the full palette in night mode, without requiring a separate theme token set.

colors:
  primary: "#fe0000"
  primary-active: "#cc0000"
  primary-disabled: "#ff9999"
  ink: "#111111"
  body: "#32373c"
  muted: "#abb8c3"
  hairline: "#eeeeee"
  canvas: "#fafafa"
  surface-soft: "#f4f3f1"
  surface-card: "#ffffff"
  surface-warm: "#e3ddd8"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-navy: "#003388"

typography:
  display-xl:
    fontFamily: "'Eurostile Ext-Med', 'Eurostile Extended', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.02em
  display-md:
    fontFamily: "'Eurostile Ext-Med', 'Eurostile Extended', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'Eurostile Ext-Med', 'Eurostile Extended', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.01em
  title-sm:
    fontFamily: "'Eurostile Ext-Med', 'Eurostile Extended', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'Eurostile Ext-Med', 'Eurostile Extended', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Eurostile Ext-Med', 'Eurostile Extended', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Eurostile Ext-Med', 'Eurostile Extended', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.05em
    textTransform: uppercase
  badge:
    fontFamily: "'Eurostile Ext-Med', 'Eurostile Extended', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  spec-label:
    fontFamily: "Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
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
    padding: 12px 28px
    height: 44px
  button-primary-hover:
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
    border: "2px solid {colors.ink}"
    padding: 10px 26px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-ghost-red:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 70px
    borderBottom: "1px solid {colors.hairline}"
  mega-menu:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xl} {spacing.xxl}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 560px
    overlayOpacity: 0.45
    ctaSpacing: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.title-sm}"
    captionTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderHover: "1px solid {colors.primary}"
    padding: "{spacing.base}"
    imageBg: "{colors.surface-soft}"
  series-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  navy-badge:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  spec-table:
    backgroundColor: "{colors.surface-card}"
    alternateRowBg: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rowPadding: "{spacing.sm} {spacing.base}"
  feature-strip:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  category-filter:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.surface-warm}"
    linkHoverColor: "{colors.primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Flat #fe0000 fill, no border radius, white Eurostile text in all-caps at 0.08em tracking. The square geometry is non-negotiable: it echoes the machine chassis and signals engineering intent rather than consumer softness. Hover darkens to #cc0000 (`{colors.primary-active}`); disabled state washes to #ff9999 (`{colors.primary-disabled}`) with no cursor change, keeping the layout stable.

**`button-secondary`** — Transparent fill with a 2px solid #111111 border. On hover, the border fills to solid ink and text inverts to white — a hard snap, not a fade, consistent with the brand's zero-softening posture. Used for secondary CTAs on product detail pages alongside a `button-primary` that anchors the hierarchy.

**`button-ghost-red`** — Transparent with a 1px red border and red label text. Appears on dark-background hero panels and footer CTAs where the primary's filled red would flatten against the surface. Smaller padding and `{typography.button-sm}` type keep it subordinate in weight to `button-primary`.

### Navigation

**`nav-bar`** — 70px height, white canvas, hairline bottom border. Logo sits left; category links (Machines, Accessories, Support, Dealers) run center-right in Eurostile uppercase at 13px with 0.05em tracking. Cart and language toggles anchor the far right via FontAwesome icons. No sticky behavior observed — scrolls away on long product pages to give photography full viewport.

**`mega-menu`** — Drops from the nav with a 3px red top border acting as the only color signal that the menu is open. Interior uses a white card with category columns in `{typography.body-sm}`, sub-category links indented under bold Eurostile heads. Closes on outside click with no animation delay — the interaction is abrupt by design, matching the rest of the UI's no-transition philosophy.

### Product Card

**`product-card`** — White card, no radius, hairline border that flips to a 1px red border on hover. Machine image sits on a `{colors.surface-soft}` (#f4f3f1) field at top; series badge (red or navy) overlays the top-left corner. Name renders in `{typography.title-sm}`, brief descriptor in `{typography.body-sm}` muted text below. Price and a `button-primary` sit at card bottom with consistent padding. Cards use a 3-column grid on desktop, collapsing to 2 on tablet and 1 on mobile.

### Spec Table

**`spec-table`** — The mechanical soul of every product page. Two-column grid: left column is all-caps `{typography.spec-label}` in `{colors.muted}`, right column is `{typography.body-sm}` in `{colors.ink}`. Alternating rows use `{colors.surface-soft}` for the odd stripe; every row is separated by a 1px `{colors.hairline}` rule. No outer border on the table itself — it bleeds to the content column width. Values like "E61 group head", "PID controller", "58mm portafilter" are presented as plain text with no iconography.

### Hero Banner

**`hero-banner`** — Full-bleed machine photography at minimum 560px height with a 45% dark overlay on the image to ensure white text legibility. Headline in `{typography.display-xl}` Eurostile, sub-copy in `{typography.body-md}` Arial. A single `button-primary` sits below. On mobile the overlay deepens to ~60% as the image crops to portrait and the text column narrows. No carousel autoplay observed; navigation arrows if multiple slides are present.

### Badges

**`series-badge`** / **`navy-badge`** — 10px all-caps Eurostile at 0.1em tracking, zero radius, tight 4×8px padding. Red badges label the product series (Bianca, Victoria, Mara X); navy badges flag awards, certifications, or "New" designations. Both sit flush to card corners or inline with product titles — never rounded, never shadowed.

### Feature Strip

**`feature-strip`** — Full-width section with `{colors.surface-warm}` (#e3ddd8) background, breaking the white-on-white card grid to create visual chapter breaks between product families and editorial content. Headline in `{typography.title-md}`, body in `{typography.body-sm}`. Typically contains a 2-column icon-plus-text grid listing machine features (PID, rotary pump, E61 group) with FontAwesome icons at 24px.

### Category Filter

**`category-filter`** — Horizontal pill-less toggle bar above product grids. Inactive state: `{colors.surface-soft}` fill, `{colors.ink}` label. Active state: `{colors.primary}` fill, white label — the only place a non-button element takes the red fill. Zero radius keeps it consistent with button geometry. Used to filter by machine type (home, prosumer, commercial) or by boiler configuration.

### Footer

**`footer`** — Full-width #111111 block with 4-column link grid in `{typography.body-sm}`. Column heads in `{typography.title-sm}` white; link text in `{colors.surface-warm}` (#e3ddd8) for contrast without full white brightness; hover state snaps to `{colors.primary}` red. Social icons via FontAwesome at 18px. Bottom bar carries legal copy in `{typography.caption}` at reduced opacity (0.6) — no separate background, same #111111 surface.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero image crops portrait with deepened overlay; nav collapses to hamburger + logo only; mega-menu becomes full-screen drawer; spec table scrolls horizontally; category filter wraps to 2 rows |
| Tablet | 744–1128px | 2-column product grid; nav retains logo and cart icon, category links collapse to hamburger; hero text scales to `{typography.display-md}`; feature strip goes single-column |
| Desktop | 1128–1440px | 3-column product grid; full nav-bar at 70px; mega-menu drops on hover; hero at full 560px min-height; spec table at fixed 2-column layout |
| Wide | > 1440px | Content max-width caps at ~1320px and centers; hero image scales to fill but text column stays constrained; no additional layout changes |

### Touch Targets

- All buttons minimum 44px height (matching the defined component height)
- Category filter tabs minimum 44px height on mobile, expanded padding
- Nav hamburger and cart icons minimum 44px × 44px tap area
- Product card entire surface is tappable to PDP; badge does not intercept tap

### Collapsing Strategy

- Navigation: hamburger drawer at < 1128px, retaining logo and cart icon in the bar
- Product grid: 3 → 2 → 1 column at tablet and mobile breakpoints
- Mega-menu: full-screen slide-in drawer on mobile replacing the dropdown overlay
- Hero CTA: stacks below headline text on mobile; inline on desktop
- Spec table: horizontal scroll container on mobile rather than reflowing to single column, preserving label-value pairing

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Multiple extracted hex values (#f78da7, #7bdcb5, #00d084, #8ed1fc, #0693e3, #9b51e0, #fcb900, #ff6900, #cf2e2e) appear to be WordPress Gutenberg block editor palette defaults injected into the DOM; they were excluded from the design system as non-brand colors
- Eurostile Ext-Med weight variants (bold vs. regular within the Extended cut) and exact font-weight numeric values not confirmed from extraction — assumed 700 for display/UI uses
- No meta theme-color detected; PWA/app icon theming and status-bar color unconfirmed
- Exact mega-menu animation behavior (transition duration, easing) not directly observed
- Product configurator or machine comparison table styling not seen in extraction — likely exists on deeper PDP pages
- Hover and focus ring color for text inputs not confirmed; assumed to match `{colors.ink}` based on brand pattern
- Mobile nav drawer animation and overlay scrim color not confirmed from extraction
- Whether #003388 navy is a live brand accent or a legacy catalog color appearing only in archived pages could not be determined
