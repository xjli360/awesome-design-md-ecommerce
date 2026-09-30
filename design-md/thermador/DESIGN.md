---
version: alpha
name: "Thermador"
source_url: "https://www.thermador.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep ocean teal (#003344) dominates the viewport like the face of a professional range at midnight — a single, saturated anchor that signals authority without the predictable black-on-white minimalism of most premium appliance brands. The site architecture leans cinematic; full-bleed hero photography pushes product into dramatic lighting against dark backdrops, letting stainless steel and chrome catch the eye organically rather than through artificial badge systems. Typography runs a geometric sans-serif in light-to-medium weights at generous sizes, trusting letter-spacing and vertical rhythm over bold flourishes — headlines rarely exceed weight 500, creating a controlled tension between the dark palette and airy type. Navigation collapses into a spare horizontal bar with restrained link counts; category architecture favors curated editorial paths ("One-Two-Free" promotions, "Masterpiece" vs "Professional" collections) over dense mega-menus. Cards and containers carry minimal radius (`{rounded.xs}` to `{rounded.sm}`), reinforcing the architectural precision of the physical product lines. Spacing is generous — `{spacing.section}` or wider between content blocks — giving each appliance room to breathe the way a showroom floor separates a column and a cooktop. CTAs arrive in the brand teal with white text, rectangular and confident, occasionally outlined in secondary variants to pull hierarchy without competing. The overall digital impression is a showroom after hours: controlled lighting, deliberate silence between elements, and every surface reflecting something engineered.

colors:
  primary: "#003344"
  primary-active: "#002233"
  primary-disabled: "#7a9eab"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  surface-hero: "#0a0a0a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-steel: "#c0c8cc"
  accent-warm: "#b8860b"
  border-strong: "#aaaaaa"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-upper:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.4px
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  spec-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.5px
    textTransform: uppercase
  promo-headline:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.4px

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
  section: 80px
  section-lg: 120px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
    textDecoration: underline
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline-soft}
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    imageAspect: 4:3
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
  hero-cinematic:
    backgroundColor: "{colors.surface-hero}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-lg}"
    ctaComponent: button-primary
    minHeight: 85vh
    padding: "{spacing.section-lg} {spacing.xl}"
    overlayGradient: linear-gradient(180deg, transparent 40%, rgba(0,0,0,0.6) 100%)
  hero-split:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    layout: 50/50 image-right
    padding: "{spacing.section} {spacing.xl}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.promo-headline}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  collection-badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-md}"
    rowPadding: "{spacing.md} 0"
    borderBottom: 1px solid {colors.hairline-soft}
  category-nav-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    hoverBackgroundColor: "{colors.hairline-soft}"
  comparison-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    border: 1px solid {colors.hairline}
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.nav-link}"
    padding: "{spacing.section} {spacing.xl}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-lg}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: 0 8px 40px rgba(0,0,0,0.15)
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — Solid deep-teal rectangle with barely-there 2px radius, white text in medium-weight sans-serif at 16px with subtle letter-spacing. Hover state darkens to `{colors.primary-active}`; disabled state fades to the muted teal `{colors.primary-disabled}`. The near-square corners signal engineering precision rather than consumer friendliness.

**`button-secondary`** — Transparent fill with a 2px teal border, teal text. On hover, fills completely with `{colors.primary}` and flips text to white, creating a satisfying "slot into place" interaction. Used alongside primary buttons in hero sections and comparison tools where dual-action is needed.

**`button-tertiary`** — Text-only with underline, no background or border. Reserved for inline actions within editorial content and breadcrumb-adjacent navigation. Hover darkens the underline.

**`button-dark`** — Near-black fill (#1a1a1a) with white text, used in dark-on-dark hero contexts where the teal primary would disappear into the background photography.

### Navigation
**`nav-bar`** — A 64px-tall white bar with a subtle bottom hairline, carrying the Thermador wordmark left and a sparse set of category links in 14px medium-weight type. The restraint in link count (typically 5–7 top-level items) forces editorial hierarchy. On scroll, a slight shadow replaces the hairline.

**`nav-bar-dark`** — Inverted variant for pages where the hero bleeds edge-to-edge in dark photography. Same height and type treatment, white text on dark background, no visible border.

### Heroes
**`hero-cinematic`** — Full-viewport dark photography with a bottom gradient overlay ensuring text legibility. Headlines arrive in display-xl (48px, weight 300) — the thin strokes float over dense imagery without competing. A single CTA button sits below with generous vertical spacing. Minimum 85vh height ensures the appliance dominates the fold.

**`hero-split`** — A 50/50 layout for secondary landing pages: product photography right, headline + body + CTA left on white canvas. Used for category entries and promotional landing pages where the single-product focus of the cinematic hero is too narrow.

### Product Display
**`product-card`** — Light gray (`{colors.surface-soft}`) background with 4:3 product photography, title in `{typography.title-sm}`, and optional price/spec line in `{typography.body-sm}`. Minimal 4px radius. Hover lifts with a subtle box-shadow rather than color change, maintaining the showroom calm.

**`spec-table`** — Alternating label/value rows with uppercase 13px labels in weight 600 and regular-weight values. Thin hairline separators between rows. Used extensively on product detail pages for dimensions, capacities, and feature lists.

**`comparison-row`** — Structured grid row for side-by-side product comparison. Header cells use `{typography.title-sm}`, data cells use `{typography.body-sm}`. Bordered cells maintain readability across 3–4 product columns.

### Promotional
**`promo-banner`** — Full-width teal (`{colors.primary}`) banner with thin display type (`{typography.promo-headline}`) at 40px weight 300. Used for "One-Two-Free" style promotional campaigns. White text on brand color creates a confident break in the page rhythm.

**`collection-badge`** — Small gold/warm-accent pill for "Masterpiece" and "Professional" collection identifiers. Uppercase 11px text, tight padding, applied inline with product titles.

### Utility
**`search-overlay`** — Centered modal panel with rounded-md corners and a prominent drop shadow. Large input text (18px) with teal focus border. Results appear below in card format.

**`breadcrumb`** — Muted gray text at caption size with slash or chevron separators. Terminal node inherits ink color for active-state emphasis.

**`footer`** — Dark background (#1a1a1a) with columnar link lists in 14px white text, generous section-level top/bottom padding. Legal text drops to `{typography.caption}` in muted gray.

**`category-nav-tile`** — Rectangular tiles on category landing pages, light gray fill, 18px title centered or left-aligned depending on context. Hover shifts background to the softer hairline tone.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; hero shrinks to 70vh; display-xl drops to 32px; product cards stack single-column; spec-table becomes label-above-value layout; footer columns stack vertically |
| Tablet | 744–1128px | Two-column product grid; hero-split stacks vertically (image top, content bottom); nav shows truncated link set with overflow menu; comparison limited to 2 products |
| Desktop | 1128–1440px | Full nav visible; three-column product grid; hero-cinematic at full 85vh; comparison supports 3 products; spec-tables side-by-side on PDP |
| Wide | > 1440px | Content max-width caps at 1440px centered; hero imagery extends full bleed beyond content frame; increased section spacing (`{spacing.section-lg}`); four-column product grids on collection pages |

### Touch Targets
- All interactive elements maintain minimum 44×44px tap area on mobile
- Button height remains 48px across breakpoints; padding increases on mobile for thumb reach
- Nav hamburger icon area expands to 48×48px
- Card tap targets encompass the entire card surface, not just text

### Collapsing Strategy
- Navigation: progressive disclosure — full links → truncated with "More" → hamburger
- Product grids: 4-col → 3-col → 2-col → 1-col stack
- Hero: cinematic maintains aspect ratio down to tablet, then crops to portrait-friendly framing
- Spec tables: horizontal rows → stacked label/value blocks below 744px
- Comparison tool: hidden entirely on mobile; replaced with a "Compare" toggle that opens a drawer
- Footer: multi-column → single accordion-based column list

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#003344) was reliably extracted; the full palette (accent golds, grays, surface tones) is inferred from brand-knowledge and standard luxury-appliance conventions
- No font-family stacks were detected — the site likely loads custom webfonts via JavaScript bundles or behind anti-bot protections; Helvetica Neue is used as a reasonable proxy based on the brand's parent company (BSH/Bosch) design system patterns
- Exact border-radius values could not be confirmed; the near-zero radius approach is inferred from the architectural brand positioning
- Spacing scale is estimated — actual section padding and grid gaps were not extractable
- Promotional campaign components (e.g., "One-Two-Free") may rotate seasonally with different color treatments not captured here
- Dark-mode or alternate theme tokens are not represented; the site may serve different palettes for product-line sub-brands (Masterpiece vs Professional)
- Animation and transition timing values were not extractable
- Icon system details (stroke weight, grid size, style) are unknown
