---
version: alpha
name: "FX Luminaire"
source_url: "https://www.fxl.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every UI decision serves the same purpose as the fixtures themselves — to make the light the subject and let the housing recede. FX Luminaire operates in near-darkness by design: a deep obsidian canvas (#0C0C0C) anchors the entire system, with product photography occupying full-bleed hero frames where amber wash rakes across stone pathways and timber fascia at dusk. The primary accent, a warm amber (#C8843A), arrives precisely where a specification professional would place a fixture — marking active states, primary CTAs, and interactive highlights — while the surrounding interface holds in charcoal and cool-gray to avoid competing with the warmth of simulated light. Type runs a geometric sans-serif (Montserrat or a close equivalent), with display headings at 32–40px in weight 600 to project authority in specification contexts without tipping into decorative excess. Body copy drops to 13–15px with generous line-height for dense product-data grids: lumens output, beam-spread tables, color-temperature selectors, IP ratings. Corner radii are deliberately restrained — {rounded.xs} for form chrome, {rounded.sm} for cards, {rounded.none} wherever photography or technical drawings bleed — maintaining an architectural register that pill shapes would soften away. The product configurator, the core workflow for specification professionals, uses a stepped panel layout where fixture family, wattage, beam angle, and finish are each surfaced as a discrete selection tier, making the ordering logic visible without requiring a catalog reference. Hairlines at #2A2A2A divide content zones while the surface hierarchy (obsidian → charcoal → dark-card) creates readable depth without any light-mode canvas. The brand does not maintain a retail tone; there are no lifestyle promises, only specification confidence and photometric precision.

colors:
  primary: "#C8843A"
  primary-active: "#A86A22"
  primary-disabled: "#7A5228"
  primary-glow: "#C8843A26"
  ink: "#FFFFFF"
  body: "#CCCCCC"
  muted: "#888888"
  muted-soft: "#555555"
  hairline: "#2A2A2A"
  hairline-soft: "#1E1E1E"
  canvas: "#0C0C0C"
  surface-soft: "#181818"
  surface-card: "#1F1F1F"
  surface-elevated: "#252525"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  success: "#4CAF7A"
  warning: "#E8A930"
  error: "#E05555"
  ip-badge: "#2A4A6A"
  spec-accent: "#4A7A9B"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Gotham', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Gotham', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Gotham', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Montserrat', 'Gotham', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Gotham', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Montserrat', 'Gotham', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Gotham', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  spec-data:
    fontFamily: "'Roboto Mono', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  caption:
    fontFamily: "'Montserrat', 'Gotham', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Montserrat', 'Gotham', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Montserrat', 'Gotham', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  overline:
    fontFamily: "'Montserrat', 'Gotham', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Gotham', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Gotham', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', 'Gotham', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
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
    padding: "12px 24px"
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "11px 23px"
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.muted-soft}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: "10px 14px"
    height: 44px
    placeholderColor: "{colors.muted}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 32px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imageRatio: "4/3"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
  hero-fullbleed:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    imageOverlay: "linear-gradient(to right, rgba(0,0,0,0.78) 0%, rgba(0,0,0,0.18) 60%)"
    minHeight: "520px"
    ctaSpacingTop: "{spacing.xl}"
  spec-badge:
    backgroundColor: "{colors.ip-badge}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  beam-angle-chip:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
    borderSelected: "1px solid {colors.primary}"
    textColorSelected: "{colors.primary}"
  product-configurator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    stepHeaderTypography: "{typography.title-md}"
    stepBodyBackground: "{colors.surface-card}"
    stepPadding: "{spacing.lg}"
    activeStepAccent: "{colors.primary}"
  photometric-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.spec-data}"
    headerBackground: "{colors.surface-card}"
    headerTypography: "{typography.caption}"
    borderColor: "{colors.hairline}"
    rowAlternate: "{colors.surface-soft}"
    cellPadding: "8px 12px"
  finish-swatch:
    size: "36px"
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.primary}"
    gap: "{spacing.xs}"
  section-divider:
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.overline}"
    labelColor: "{colors.muted}"
    marginY: "{spacing.section}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    height: 44px
    padding: "0 {spacing.base}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.caption}"
    headingColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Amber-filled with white uppercase type and a 4px radius. The warm amber (#C8843A) communicates the brand's light-source vocabulary without decorative gesture; the 0.5px tracking on button labels keeps them legible at small sizes in specification contexts where label density is high. Active state deepens to #A86A22; disabled collapses to a muted bronze-gray (#7A5228) with low-contrast muted text so unavailability is legible without relying on color alone.

**`button-secondary`** — Transparent fill with a hairline border (#2A2A2A) and white text. Pairs with `button-primary` in dual-CTA contexts such as "Configure Fixture" adjacent to "Download IES File." Hover shifts background to `{colors.surface-soft}` and border to `{colors.muted-soft}` to confirm interactivity against the dark canvas without introducing amber into a secondary role.

**`button-ghost`** — No background, no border; amber text only. Reserved for tertiary actions inside data-dense views — configurator step footers, photometric table controls — where additional chrome would crowd specification grids.

### Inputs

**`text-input`** and **`select-input`** — Dark-card fill (`{colors.surface-card}`) with a hairline border that shifts to amber on focus. Placeholder text in `{colors.muted}` provides affordance without competing with the ambient dark. Height 44px satisfies touch targets for specification workflows accessed on job-site tablets. The `select-input` carries a muted chevron icon to signal dropdown behavior without a heavy chrome indicator.

### Navigation

**`nav-bar`** — 72px tall, obsidian background with a bottom hairline at `{colors.hairline}`. Logo sits at 32px height on the left; product-family nav links in `{typography.nav-link}` spread across the center; a search icon and "Find a Rep" CTA button anchor the trailing edge. Sticky on scroll so navigation remains accessible during long specification sessions with dense product-data pages below the fold.

### Product Card

**`product-card`** — Dark-card surface with 8px radius and a soft hairline border. The 4:3 image ratio frames fixture photography against dark exterior or stone backgrounds. Title renders in `{typography.title-sm}`, secondary detail (series name, wattage range) in `{typography.body-sm}` at `{colors.muted}`. `spec-badge` chips for IP rating and listing certifications stack horizontally inside the `{spacing.base}` padding zone below the image.

### Hero

**`hero-fullbleed`** — Full-bleed nighttime photography at minimum 520px tall, with a directional gradient scrim (78% opacity left, 18% right) that allows white display type to read cleanly over outdoor scenes without washing the image. Headline in `{typography.display-xl}`, subhead in `{typography.body-md}` at `{colors.body}`, and a primary CTA at `{spacing.xl}` below the headline baseline.

### Spec Badge

**`spec-badge`** — Compact IP-rating and certification chips in deep navy (#2A4A6A) with white uppercase badge type at 10px. Appears on product cards, inside the configurator, and on product detail pages to communicate certification status without interrupting the amber-primary visual hierarchy.

### Beam Angle Chips

**`beam-angle-chip`** — Rectangular chips (4px radius) on a dark-elevated surface. Displays beam-spread values (15°, 25°, 40°, 60°, 90°) as selectable options within the configurator. Selected state adds an amber border and amber text; unselected state uses `{colors.body}` text on `{colors.surface-elevated}`. No filled background on selection, preventing amber from saturating a multi-select grid.

### Product Configurator

**`product-configurator`** — Multi-step panel in `{colors.surface-soft}` housing discrete selection tiers: fixture family → wattage → beam angle → color temperature → finish. Each step renders inside a `{colors.surface-card}` sub-panel with `{spacing.lg}` internal padding. The active step shows a 3px left-border accent in `{colors.primary}`; completed steps carry a muted checkmark in `{colors.muted}`. Step headers use `{typography.title-md}`; option labels use `{typography.body-md}`.

### Photometric Table

**`photometric-table`** — Monospaced data in `{typography.spec-data}` on an obsidian canvas. Column headers sit in a `{colors.surface-card}` row with `{typography.caption}` labels. Alternating data rows use `{colors.surface-soft}` for scannability across dense lumen-distance-footcandle matrices. Hairline column borders in `{colors.hairline}`. The table accommodates 6–10 columns without horizontal scroll at desktop widths.

### Finish Swatch

**`finish-swatch`** — 36px circular swatches in a horizontal row with `{spacing.xs}` gap. Default state: no border (color fill only). Selected state: 2px amber border with a transparent 2px offset creating a ring effect. Finish names appear as `{typography.caption}` in `{colors.muted}` below the row. Standard values: Architectural Bronze, Matte Black, Textured White, Hunter Green.

### Footer

**`footer`** — Dark-soft background (`{colors.surface-soft}`) with a top hairline. Column headings in `{typography.caption}` at `{colors.ink}`; links in `{typography.body-sm}` at `{colors.body}`, shifting to `{colors.primary}` on hover. Standard columns: Products, Resources (IES/photometric file downloads), Support, Find a Rep, Company. A bottom strip carries legal text in `{typography.caption-sm}` and certification logos.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid. Nav collapses to hamburger with full-screen dark-canvas overlay. Hero min-height drops to 320px; scrim covers full frame. Configurator steps become full-width accordion panels stacked vertically. Photometric tables scroll horizontally with pinned first column. |
| Tablet | 744–1128px | Two-column product grid. Nav shows logo and icon tray (search, hamburger). Hero text left-aligned with 48px side margins over scrim. Configurator renders as horizontal step tabs above the option panel. |
| Desktop | 1128–1440px | Three-column product grid. Full nav bar with all product-family links visible. Hero supports 50/50 split layout (copy left, tinted photography right) or full-bleed with scrim. Configurator panel sits in a 360px right rail alongside the product detail view. |
| Wide | > 1440px | Four-column product grid. Hero photography scales to full viewport width. Content max-width capped at 1440px centered; full-bleed hero images and section backgrounds extend to viewport edge. |

### Touch Targets

- All interactive elements (buttons, chips, nav items, swatch selectors) maintain minimum 44×44px tap targets
- Beam-angle chips and finish swatches receive 8px invisible padding zones on mobile to prevent adjacent-element mis-taps
- Configurator step headers are full-width tappable accordion triggers on mobile, not limited to the label text
- Icon-only nav controls (search, hamburger) are padded to 44px square regardless of visible icon size

### Collapsing Strategy

- Primary nav collapses to hamburger at < 1024px; the mega-menu becomes a full-screen stacked drawer over the dark canvas
- Photometric data tables reflow to card-per-row format below 744px, surfacing only the three highest-priority columns (distance, center-beam fc, beam spread) with a "Show all columns" expand trigger
- Finish swatch rows wrap to two rows maximum; overflow swatches collapse behind a "+N more" chip styled as `{typography.caption}` in `{colors.muted}`
- Configurator steps transition from vertical timeline (desktop) to horizontal stepper tabs (tablet) to full-width accordions (mobile)
- Hero layouts shift from 50/50 split (desktop) to stacked image-above, copy-below (mobile) with the scrim removed in favor of a solid `{colors.canvas}` content block

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All colors are brand-knowledge inference** — the live site returned "Access Denied" with no extractable palette. The amber primary (#C8843A) and obsidian canvas (#0C0C0C) are reasonable estimates for a professional architectural outdoor lighting brand but must be verified against actual brand guidelines or design tokens before shipping.
- **All typography is inferred** — no font-family stacks were extracted. Montserrat is a common geometric sans for professional specification brands; FX Luminaire may use a licensed typeface (Gotham, Proxima Nova, Brandon Grotesque, or a proprietary cut) that would shift typographic weight and spacing significantly.
- **Dark-mode assumption is unconfirmed** — the dark-canvas design direction is consistent with outdoor lighting brand conventions and dramatic product photography, but the live site may operate in light mode or support both modes with a toggle.
- **No theme-color meta tag** — browser chrome metadata could not confirm primary brand color.
- **Product configurator UX is speculative** — the stepped-panel layout is inferred from specification-industry conventions; actual workflow, step count, and option structure are unconfirmed.
- **Photometric table schema unknown** — column structure, data density, and download formats (IES, LDT) are estimated from outdoor lighting industry norms; actual table design is unconfirmed.
- **Certification badge palette inferred** — IP-badge blue (#2A4A6A) is a reasonable neutral for regulatory content but is not extracted from the site.
- **Navigation structure unknown** — product family groupings, mega-menu depth, and utility link placement cannot be confirmed without live site access.
