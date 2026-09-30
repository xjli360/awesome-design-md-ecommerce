---
version: alpha
name: "Cove"
source_url: "https://www.subzero-wolf.com/cove"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Dusky violet (#5b5378) anchors a dishwasher interface — an unexpected chromatic choice for an appliance category dominated by stainless neutrals and clinical whites. Cove, the dedicated dishwasher division within the Sub-Zero & Wolf ecosystem, deploys this muted amethyst across primary navigation states, active indicators, and hero overlays, creating an immediate separation from the utilitarian aesthetic of competing brands. The purple deepens to near-indigo (#494260, #2d293c) for hover states and footer regions, establishing vertical hierarchy through saturation shifts rather than hue changes. Typography runs on Museo Sans in ExtraLight through Medium weights — the lighter cuts handle display and hero headlines at generous sizes, while Medium anchors buttons and navigation labels. This weight distribution produces an airy, gallery-like reading experience where the appliance photography dominates and text recedes into supporting architecture. Body copy and specification tables rely on a warm charcoal (#4c4d4f) against a near-white canvas (#f7f7f7), maintaining readability without the harshness of pure black on white. Component radii stay conservative — `{rounded.xs}` to `{rounded.sm}` on buttons and cards — reflecting the precision engineering ethos of the parent brand family. Accent colors serve functional roles: a saturated blue (#0081c6) for interactive links and informational callouts, a deep teal (#00393b) for environmental messaging badges, and a muted red (#af272e) for alerts and discontinuation notices. Spacing is generous and architectural, with `{spacing.section}` breathing room between feature blocks that each showcase a single dishwasher capability in full-bleed photography paired with concise spec copy. The grid holds a 1440px maximum content width with symmetric margins, collapsing to edge-to-edge imagery on mobile while preserving generous vertical rhythm throughout.

colors:
  primary: "#5b5378"
  primary-active: "#494260"
  primary-disabled: "#8e849e"
  ink: "#2d293c"
  body: "#4c4d4f"
  muted: "#808184"
  muted-soft: "#777777"
  hairline: "#d2d2d2"
  hairline-soft: "#ebebeb"
  canvas: "#f7f7f7"
  surface-soft: "#ececec"
  surface-card: "#ffffff"
  surface-dark: "#38393a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-blue: "#0081c6"
  accent-blue-active: "#00669d"
  accent-teal: "#00393b"
  accent-red: "#af272e"
  accent-red-deep: "#9c2815"
  accent-green: "#c4d600"
  accent-green-dark: "#467810"
  accent-amber: "#da9735"
  accent-purple: "#603cba"
  charcoal: "#3d3e3f"
  charcoal-light: "#5c5c5c"
  border-medium: "#cdcdcd"
  scrim: "#2d293c"

typography:
  display-xl:
    fontFamily: "'Museo Sans', 'museo-sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 200
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Museo Sans', 'museo-sans', sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Museo Sans', 'museo-sans', sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Museo Sans', 'museo-sans', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Museo Sans', 'museo-sans', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Museo Sans', 'museo-sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'Museo Sans', 'museo-sans', sans-serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Museo Sans', 'museo-sans', sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Museo Sans', 'museo-sans', sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Museo Sans', 'museo-sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-mono:
    fontFamily: "'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Museo Sans', 'museo-sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Museo Sans', 'museo-sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Museo Sans', 'museo-sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  spec-label:
    fontFamily: "'Museo Sans', 'museo-sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  spec-value:
    fontFamily: "'Museo Sans', 'museo-sans', sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.23
    letterSpacing: 0
  eyebrow:
    fontFamily: "'Museo Sans', 'museo-sans', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 1.2px
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.primary}
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.button-md}"
    padding: 0
    textDecoration: none
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline}
    padding: 0 {spacing.xl}
  nav-bar-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline-soft}
    shadow: 0 2px 8px rgba(45,41,60,0.06)
  product-card-hover:
    shadow: 0 4px 16px rgba(45,41,60,0.12)
    border: 1px solid {colors.hairline}
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 560px
    padding: "{spacing.section-lg} {spacing.xl}"
    overlay: linear-gradient(180deg, rgba(45,41,60,0.0) 0%, rgba(45,41,60,0.65) 100%)
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
    maxWidth: 680px
  hero-subhead:
    typography: "{typography.body-lg}"
    textColor: "{colors.on-dark}"
    opacity: 0.9
    maxWidth: 520px
  feature-block:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
    display: grid
    gridTemplateColumns: 1fr 1fr
    gap: "{spacing.xxl}"
    alignItems: center
  feature-block-image:
    rounded: "{rounded.none}"
    width: 100%
    aspectRatio: 4/3
    objectFit: cover
  feature-block-text:
    padding: "{spacing.xl}"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline-soft}
  spec-table-row:
    padding: "{spacing.md} 0"
    borderBottom: 1px solid {colors.hairline-soft}
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  spec-table-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.body}"
  badge-eco:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separator: "/"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.body}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    opacity: 0.75
    opacityHover: 1.0
  tab-bar:
    backgroundColor: "{colors.surface-card}"
    borderBottom: 2px solid {colors.hairline-soft}
    padding: 0
  tab-active:
    textColor: "{colors.primary}"
    typography: "{typography.title-sm}"
    borderBottom: 2px solid {colors.primary}
    padding: "{spacing.md} {spacing.lg}"
  tab-inactive:
    textColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    borderBottom: 2px solid transparent
    padding: "{spacing.md} {spacing.lg}"
  model-selector:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
  model-selector-active:
    border: 2px solid {colors.primary}
    shadow: 0 0 0 3px rgba(91,83,120,0.12)
  image-gallery:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    thumbnailSize: 64px
    thumbnailRounded: "{rounded.xs}"
    thumbnailBorderActive: 2px solid {colors.primary}
    gap: "{spacing.sm}"
  cta-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    padding: "{spacing.xl} {spacing.xxl}"
    rounded: "{rounded.none}"

## Components

### Buttons
**`button-primary`** — Solid violet (#5b5378) background with white uppercase text in Museo Sans Medium at 14px with generous letter-spacing. Corners are barely softened at `{rounded.xs}` (4px), keeping the precision-engineered feel. On hover, background deepens to `{colors.primary-active}` (#494260); disabled state lightens to `{colors.primary-disabled}` with reduced opacity.

**`button-secondary`** — Transparent fill with a 2px violet border and violet text. On hover/active, the fill floods to `{colors.primary}` and text inverts to white, creating a satisfying state toggle. Used for secondary actions like "View Specifications" or "Compare Models."

**`button-tertiary`** — Text-only link-style button in `{colors.accent-blue}` without underline or background. Reserved for inline actions within content blocks and breadcrumb-adjacent navigation.

### Navigation
**`nav-bar`** — 72px-tall white bar with a single-pixel hairline bottom border. Logo sits left-aligned, primary navigation links center in Museo Sans Medium 14px with 0.3px letter-spacing. The dark variant (`nav-bar-dark`) uses `{colors.ink}` background for immersive hero sections where the nav overlays full-bleed imagery.

**`breadcrumb`** — Caption-weight path trail using forward-slash separators in `{colors.hairline}`. The final active segment renders in `{colors.body}` while ancestor links remain in `{colors.muted}` with hover underlines.

**`tab-bar`** — Horizontal tab navigation with a 2px bottom border. Active tab shows `{colors.primary}` text with a matching 2px indicator line; inactive tabs sit in `{colors.muted}` with transparent borders. Used for switching between product specifications, features, and reviews.

### Product Display
**`product-card`** — White card on the `{colors.canvas}` background with `{rounded.sm}` corners, a subtle 1px `{colors.hairline-soft}` border, and a light box-shadow. On hover, shadow deepens and border tightens to `{colors.hairline}`, providing lift without color shift. Interior padding uses `{spacing.lg}` (24px).

**`model-selector`** — Selection card for choosing between dishwasher models (panel-ready, stainless, etc.). Default state shows a single-pixel `{colors.hairline}` border; active/selected state promotes to 2px `{colors.primary}` border with a subtle 3px violet glow ring. Interior holds a product thumbnail, model number, and key differentiator text.

**`image-gallery`** — Full-width main image area with a horizontal strip of 64px square thumbnails beneath. Active thumbnail receives a 2px `{colors.primary}` border; thumbnails use `{rounded.xs}` corners. Gap between thumbnails is `{spacing.sm}`.

### Hero & Feature
**`hero-banner`** — Full-bleed dark section (minimum 560px height) with bottom-gradient overlay (transparent to 65% `{colors.scrim}`). Display-xl headline in white sits bottom-left with a max-width of 680px. A secondary body-lg subhead follows at 90% opacity. Primary CTA button sits below with `{spacing.lg}` separation.

**`feature-block`** — Two-column grid (1:1) alternating image and text content. Images are uncropped at 4:3 aspect ratio with no border-radius. Text column receives `{spacing.xl}` padding with a title-lg headline, body-md description, and an optional tertiary link. Columns reverse order on alternating rows for visual rhythm.

### Specifications
**`spec-table`** — White card with `{rounded.sm}` corners holding rows of label-value pairs. Each row is separated by a 1px `{colors.hairline-soft}` divider with `{spacing.md}` vertical padding. Labels render in `{typography.spec-label}` (Museo Sans 500, 13px, `{colors.muted}`); values in `{typography.spec-value}` (300 weight, `{colors.body}`).

### Badges
**`badge-eco`** — Dark teal (#00393b) pill with white uppercase eyebrow text. Applied to energy-efficient models and sustainability callouts. Padding is compact (4px 10px) with `{rounded.xs}` corners.

**`badge-new`** — Lime green (#c4d600) background with dark ink text. Used sparingly to flag newly released models or features. Same dimensional treatment as badge-eco.

### Footer
**`footer`** — Deep violet-black (`{colors.ink}`) full-width section with generous `{spacing.section}` vertical padding. Links render in white body-sm at 75% opacity, rising to full opacity on hover. Footer grid arranges into four columns on desktop, collapsing to stacked accordion groups on mobile.

### Call-to-Action
**`cta-banner`** — Full-width violet band with centered white title-md text and optional inline button. No border-radius — the sharp horizontal edges create a clear section break. Used for dealer-locator prompts and newsletter signups.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero reduces to 360px min-height; nav collapses to hamburger menu with slide-out drawer; feature-block stacks vertically (image on top); spec-table goes full-width; footer columns stack as accordions; tab-bar becomes horizontally scrollable |
| Tablet | 744–1128px | Two-column grid returns for feature-blocks; product-cards display 2-up; nav shows top-level links with overflow into "More" dropdown; hero restores to 480px min-height; footer shows 2×2 column grid |
| Desktop | 1128–1440px | Full two-column feature-blocks; product-cards display 3-up; all nav links visible; spec-tables sit beside product imagery in side-by-side layout; image-gallery thumbnails expand to 80px |
| Wide | > 1440px | Content max-width locks at 1440px with auto margins; hero imagery extends full-bleed behind max-width content overlay; increased `{spacing.section-lg}` between major blocks; product-cards may display 4-up in comparison views |

### Touch Targets
- Minimum 48px height for all interactive elements on mobile
- Tab bar items maintain 48px tap zones with `{spacing.md}` horizontal padding
- Model selector cards use full-width tap targets on mobile
- Footer accordion headers are 56px tall with clear expand/collapse indicators
- Gallery thumbnails scale to 56px on mobile with `{spacing.sm}` gaps maintained

### Collapsing Strategy
- Navigation: full link set → condensed with overflow → hamburger with drawer
- Feature blocks: side-by-side → stacked with image priority
- Product cards: 4-up → 3-up → 2-up → single column with horizontal scroll option
- Spec tables: inline beside imagery → full-width below imagery
- Footer: four columns → two columns → single-column accordions
- Tab bar: fixed → horizontally scrollable with fade-edge indicators
- Hero headlines: display-xl (48px) → display-lg (36px) → display-md (28px)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Museo Sans weight mappings (ExtraLight = 200, Light = 300, Medium = 500 assumed from standard conventions — live CSS custom properties not extracted)
- No CSS custom properties or design-token JSON found; colors derived from rendered pixel sampling which may miss context-dependent overlays
- Interaction motion/easing curves not captured (transitions likely exist on hover states and drawer animations)
- Exact box-shadow values estimated from visual appearance; no computed style extraction available
- Icon system undocumented — the site likely uses an SVG sprite or icon font for UI glyphs (arrows, chevrons, close marks)
- Form validation states (error, success, warning) colors inferred from extracted reds but not confirmed in context
- Dark-mode or alternate color scheme not detected (site appears single-theme)
- The parent Sub-Zero & Wolf brand shares significant chrome with Cove; some extracted colors (#af272e, #893424, #a9402c, #c0311a) may belong to Wolf or Sub-Zero sub-brands rather than Cove specifically
