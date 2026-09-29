---
version: alpha
name: "Plum Paper"
source_url: "https://www.plumpaper.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Bressay Display at the hero scale announces the brand before any product photograph loads — a high-contrast editorial serif drawn from printing tradition, transplanted to a planner storefront to position the act of organizing one's year within the same register as choosing paper goods from a fine stationer. Below it, Adobe Garamond Pro carries product names, navigation labels, and body copy in a typeface descended from sixteenth-century Venetian punchcutters; its old-style figures and bracketed serifs make pricing and feature text feel typeset rather than templated, and its generous x-height holds legibility at the 15–17px sizes the brand favors.

  The brand name is a direct chromatic brief. `{colors.primary}` — a deep plum-purple near #7A4B7D — anchors every primary CTA, the active-category underline strip, and the customizer step indicator in a hue that reads simultaneously as botanical and elevated. The canvas `{colors.canvas}` is warm off-white rather than stark white, evoking cream paper stock, with `{colors.surface-soft}` stepping to a lavender-tinted near-white for section fills and hover states. `{colors.surface-card}` brings product thumbnails to pure white, floating them cleanly against the warmed field. Hairlines throughout carry a faint plum cast at `{colors.hairline}`, keeping structural dividers chromatically related to the primary rather than defaulting to cold neutral gray.

  Radii are present but measured: `{rounded.sm}` on text inputs and small product cards, `{rounded.md}` on larger feature panels and the customizer container, `{rounded.full}` reserved for pill badges marking seasonal collections or sale states. No hard edge appears anywhere, but the radius curve never crosses into the aggressive softness that marks consumer fintech products. Spatial rhythm is generous — `{spacing.section}` 64px between major content bands, `{spacing.xl}` 32px internal gutters — letting campaign photography function as editorial spreads rather than catalog thumbnails.

  The planner customizer is the brand's most differentiated screen: a sequential multi-step layout with step indicators in `{colors.primary}`, Garamond-labeled option fields that adopt a `{colors.surface-soft}` background when selected, and a live cover-preview panel that updates in real time as the shopper configures layout, binding, and personalization text. The combination of Bressay Display headlines and Garamond form labels inside this flow makes the purchase experience read closer to a bespoke stationer consultation than a software configuration wizard — which is, architecturally, the entire point of the typographic system.

colors:
  primary: "#7A4B7D"
  primary-active: "#5E3961"
  primary-disabled: "#C9A8CC"
  ink: "#2A2025"
  body: "#4A3F4D"
  muted: "#7A6E7D"
  hairline: "#DDD0DF"
  canvas: "#FDFAF8"
  surface-soft: "#F5EFF7"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  plum-light: "#EDE0EF"
  parchment: "#FAF6F0"
  accent-warm: "#B8926A"

typography:
  display-xl:
    fontFamily: "'bressay-display', serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -1px
  display-md:
    fontFamily: "'bressay-display', serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'bressay-display', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'adobe-garamond-pro', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'adobe-garamond-pro', serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  price:
    fontFamily: "'adobe-garamond-pro', serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  body-md:
    fontFamily: "'adobe-garamond-pro', serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'adobe-garamond-pro', serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'adobe-garamond-pro', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  overline:
    fontFamily: "'adobe-garamond-pro', serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'adobe-garamond-pro', serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.05em
  nav-label:
    fontFamily: "'adobe-garamond-pro', serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.01em

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
    padding: "12px 28px"
    height: 46px
    border: none
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "11px 27px"
    height: 46px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px 14px"
    height: 44px
    focusBorder: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 68px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
    logoColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    border: "1px solid {colors.hairline}"
    hoverShadow: "0 4px 16px rgba(122, 75, 125, 0.10)"
  hero-banner:
    backgroundColor: "{colors.parchment}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
    minHeight: 540px
  customizer-stepper:
    backgroundColor: "{colors.surface-soft}"
    activeStepColor: "{colors.primary}"
    inactiveStepColor: "{colors.hairline}"
    completedStepColor: "{colors.plum-light}"
    connectorColor: "{colors.hairline}"
    typography: "{typography.caption}"
    stepIndicatorSize: 28px
    stepIndicatorRounded: "{rounded.full}"
    connectorHeight: 2px
  customizer-option-field:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.body-sm}"
    valueTypography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.primary}"
    selectedBackground: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  cover-preview-panel:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    shadow: "0 2px 12px rgba(0, 0, 0, 0.10)"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    position: sticky
    top: "{spacing.xl}"
  badge-pill:
    backgroundColor: "{colors.plum-light}"
    textColor: "{colors.primary-active}"
    typography: "{typography.overline}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  badge-pill-sale:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  category-filter-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-label}"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "2px solid {colors.primary}"
    inactiveBorderBottom: "2px solid transparent"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    linkColor: "{colors.primary}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} {spacing.xxl}"

## Components

### Buttons
**`button-primary`** — Full plum fill (`{colors.primary}`) with off-white text, 8px radius, 46px height, and Garamond semibold at 15px with 0.05em letter-spacing. Darkens to `{colors.primary-active}` on hover/press; fades to `{colors.primary-disabled}` when inactive. Used for primary purchase actions ("Add to Cart", "Start Customizing") and the customizer step-advance button.

**`button-secondary`** — Warm white canvas background with a 1px plum border and plum text, matching primary dimensions. Hover state transitions background to `{colors.surface-soft}` and border to `{colors.primary-active}`. Used for secondary CTAs like "View Details", "Save Design", and gift card entry points.

**`button-ghost`** — Transparent background, ink text with underline decoration, no border. Used for low-priority editorial prompts ("Learn More", "See All Styles") that live adjacent to photography.

### Text Input
**`text-input`** — Warm white fill, 1px `{colors.hairline}` border at rest, upgrading to `{colors.primary}` on focus. Adobe Garamond Pro body-md at 17px, 44px height, 10px/14px padding. Placeholder text in `{colors.muted}`. Primary use is personalization fields inside the customizer (name, title line, monogram initials).

### Navigation
**`nav-bar`** — Warm white canvas, 68px tall, single hairline bottom border. Logo rendered in Bressay Display at `{typography.display-sm}` (28px, weight 400), giving the masthead an editorial magazine proportionality. Navigation category links in Garamond nav-label at 15px. Cart, search, and account icons share the same visual weight as the text links.

### Product Card
**`product-card`** — Pure white surface with 1px plum-cast hairline border and 8px radius. Portrait 3:4 aspect ratio for planner cover photography. Title in Garamond title-sm (18px semibold), price in matching price scale (18px semibold). Hover lifts a soft plum-tinted drop shadow. Badges float at top-left using `badge-pill` or `badge-pill-sale`.

### Hero Banner
**`hero-banner`** — Full-width parchment background with Bressay Display at 64px for the headline and Garamond body-md for the subheading. Minimum 540px height gives campaign photography editorial breathing room. Primary CTA button sits inline below the copy block.

### Customizer Stepper
**`customizer-stepper`** — Horizontal step indicator spanning the top of the customizer view. Active step circle in `{colors.primary}`, completed steps in `{colors.plum-light}`, pending steps in `{colors.hairline}`. Step labels in Garamond caption (13px, 0.02em tracking). Connecting lines 2px in `{colors.hairline}`. All circles use `{rounded.full}`.

### Customizer Option Field
**`customizer-option-field`** — Selectable form option blocks for layout, cover, binding, and personalization choices. Rest state: canvas background, hairline border. Selected state: `{colors.surface-soft}` background, `{colors.primary}` border. Label in Garamond body-sm (15px), description/value in body-md (17px). 12px vertical padding, 8px radius. Selected state persists until the shopper changes the selection.

### Cover Preview Panel
**`cover-preview-panel`** — Sticky right-column panel that renders the configured planner cover in real time as option fields change on the left. White surface card with faint drop shadow and 4px radius. Caption label in Garamond 13px muted text beneath the thumbnail. Stays in viewport as the user scrolls through option rows.

### Badges
**`badge-pill`** — Plum-light fill with primary-active text, full-pill radius, 11px Garamond uppercase with 0.12em tracking. For editorial collection labels: "New Arrivals", "Limited Edition", "Best Seller".

**`badge-pill-sale`** — Warm amber fill (`{colors.accent-warm}`) with white text, matching pill shape. For promotional states: "20% Off", "Sale Ends Sunday".

### Category Filter Tabs
**`category-filter-tab`** — Borderless inline tabs for planner type navigation (Weekly, Monthly, Academic, Hourly). Inactive: muted gray text, transparent bottom border. Active: ink text, 2px plum bottom border. Garamond nav-label at 15px. Sits below the primary nav as a secondary filtering row.

### Footer
**`footer`** — Surface-soft background with hairline top border. Column headings in Garamond title-sm (18px semibold), body links in body-sm (15px). Link color `{colors.primary}`. 64px top and bottom padding with 48px horizontal gutters. Warm parchment-adjacent ground maintains coherence with the overall canvas system.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger + logo + cart icon; hero headline drops to display-md (40px Bressay); product grid 1-column; customizer stepper collapses to "Step X of Y" text indicator; cover-preview-panel shifts below option fields |
| Tablet | 744–1128px | 2-column product grid; nav shows logo + cart/account icons with hamburger for category links; customizer runs 2-column (options left, preview right at reduced width); hero min-height drops to 420px |
| Desktop | 1128–1440px | Full horizontal nav with category links visible; 3–4 column product grid; customizer at full 2-column layout with sticky preview panel; hero at full 540px+ with 64px Bressay Display |
| Wide | > 1440px | Content max-width ~1280px centered with expanded horizontal padding; hero photography bleeds full width with text block constrained to max-width; section spacing gains additional top/bottom padding beyond base {spacing.section} |

### Touch Targets
- All interactive elements minimum 44×44px on touch viewports
- Customizer option fields expand to minimum 52px height on mobile
- Category filter tabs receive increased horizontal padding to meet 44px tap width
- Product card touch area covers the full card surface including badge and image regions

### Collapsing Strategy
- Primary nav: logo + icon cluster visible at all breakpoints; category links collapse to drawer overlay below 1128px
- Customizer stepper: full horizontal indicator at desktop/tablet; collapses to inline "Step 2 of 5" text label at mobile
- Footer: 4-column grid collapses to 2-column at tablet, 1-column stacked accordion at mobile
- Product grid: 4 → 3 → 2 → 1 columns across Wide → Desktop → Tablet → Mobile
- Hero: photography remains full-width at all breakpoints; headline and body copy reflow with reduced Bressay sizes

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted**: The site returned zero color tokens from the live extraction pass, most likely due to JS-loaded CSS variables or anti-bot mitigations. All color values here are inferred from the brand name ("plum") and premium stationery/planner DTC norms — treat as informed placeholders requiring visual verification against the live site.
- **Primary color unverified**: `{colors.primary}` #7A4B7D is a plausible deep plum-purple but has not been confirmed against actual brand assets; the true primary may be lighter (lavender-adjacent ~#9B6BA0) or darker (near-burgundy ~#5A3060).
- **Accent warm color unverified**: `{colors.accent-warm}` #B8926A (warm amber) is inferred as a reasonable sale/highlight accent — completely unconfirmed.
- **Canvas warmth unverified**: Off-white `{colors.canvas}` #FDFAF8 is inferred; the site may use pure #FFFFFF or a different warm tint.
- **Bressay Display weight availability**: Weight 400 (regular) is assumed; the licensed instance on site may expose only specific weights (e.g., Light 300, Medium 500). Confirm before specifying non-400 weights.
- **Adobe Garamond Pro weight range**: Weight 600 (semibold) is assumed available; the actual web font may only expose 400 and 700. Verify the licensed weight axis before using 600.
- **Customizer UI architecture**: The multi-step sequential customizer layout is inferred from product offering (personalized planners) and category norms — actual interaction model may differ (modal overlay, accordion, single-page scroll, or iframe-based preview).
- **Button radius**: `{rounded.sm}` 8px is an inference; the brand may use `{rounded.md}` 12px or pill-shaped `{rounded.full}` CTAs.
- **No meta theme-color**: Mobile chrome bar color could not be confirmed.
