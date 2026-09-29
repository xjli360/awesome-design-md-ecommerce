---
version: alpha
name: "Falcon Northwest"
source_url: "https://www.falcon-nw.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Orange sparks off a matte-black ground like a welder's arc — #fb940f is the single voltage that drives every call-to-action, active nav indicator, and configuration-step highlight on Falcon Northwest's dark-canvas interface. The site's palette reads more like an aircraft instrument cluster than a typical gaming-PC storefront: a tightly controlled near-black canvas (#202020) absorbs the eye, while supporting accents — electric cyan (#02e2f2) for spec highlights and status indicators, signal gold (#ffd91a) for limited-edition and performance-tier badges, neon green (#00ff85) for availability and benchmark callouts — each appear sparingly and only when they carry information. There is no decorative glow, no gratuitous gradient; every accent pixel earns its presence by conveying state or hierarchy. Typography runs Founders Grotesk across five weights, from Regular 400 for body copy to Bold 700 for mid-level headings, but the real identity carrier is Founders Grotesk X-Condensed — reserved exclusively for hero display headlines and model-name lockups (Talon, Tiki, FragBox) where its tall, narrow letterforms pack oversized type into tight vertical spaces without crowding full-bleed product photography. Body text sits at 16px Regular with generous 1.6 line-height, trusting the dark canvas to push contrast rather than relying on heavy weights. Buttons are sharp-cornered at `{rounded.xs}` (4px) — just enough to soften the rectangle without drifting toward consumer-friendly pills — and product cards float on `{colors.surface-card}` panels with `{rounded.sm}` (8px) radii, each anchored by a hero product render above a compact spec strip rendered in `{typography.spec-label}` style. The nav bar is a slim 64px rail pinned to the viewport top, carrying the Falcon crest at left and a condensed-weight model menu that collapses into a hamburger below 744px. Section spacing runs at `{spacing.section}` (64px) between major content blocks, giving each system its own breathing room against the dark field. Configuration selectors use a bordered-tile pattern — `{colors.surface-soft}` background with a `{colors.hairline}` border that swaps to a 2px `{colors.primary}` ring on selection — so users can scan GPU, CPU, and storage options without modal interruption. The overall system speaks to an audience that already knows what an RTX 5090 is: information density is high, decorative chrome is near zero, and the only thing louder than the specs is the orange.

colors:
  primary: "#fb940f"
  primary-active: "#e07d00"
  primary-disabled: "#7d4a08"
  accent-cyan: "#02e2f2"
  accent-gold: "#ffd91a"
  accent-green: "#00ff85"
  ink: "#fefefe"
  body: "#eeeeee"
  muted: "#d8d8d8"
  muted-soft: "#999999"
  hairline: "#3a3a3a"
  hairline-soft: "#2e2e2e"
  border-strong: "#555555"
  canvas: "#202020"
  surface-soft: "#2a2a2a"
  surface-card: "#303030"
  surface-strong: "#383838"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Founders Grotesk X-Cond', 'Founders Grotesk Bold', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Founders Grotesk X-Cond', 'Founders Grotesk Bold', -apple-system, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Founders Grotesk Bold', 'Founders Grotesk Semibold', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Founders Grotesk Semibold', 'Founders Grotesk Medium', -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Founders Grotesk Medium', 'Founders Grotesk Regular', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Founders Grotesk Regular', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Founders Grotesk Regular', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Founders Grotesk Medium', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Founders Grotesk Regular', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  spec-label:
    fontFamily: "'Founders Grotesk Medium', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  model-display:
    fontFamily: "'Founders Grotesk X-Cond', 'Founders Grotesk Bold', -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.8px
    textTransform: uppercase
  uppercase-tag:
    fontFamily: "'Founders Grotesk Bold', -apple-system, system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Founders Grotesk Semibold', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Founders Grotesk Semibold', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Founders Grotesk Semibold', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Founders Grotesk Medium', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  micro-label:
    fontFamily: "'Founders Grotesk Bold', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px

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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: 1px solid {colors.hairline}
  button-secondary-active:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.primary}
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline-soft}
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    specTypography: "{typography.spec-label}"
    bodyTypography: "{typography.body-sm}"
    imageAspectRatio: 4:3
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 600px
    padding: "{spacing.section}"
    overlayGradient: "linear-gradient(to right, #202020 30%, transparent 70%)"
  spec-chip:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  spec-chip-highlight:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.canvas}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  config-option:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: 1px solid {colors.hairline}
  config-option-selected:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: 2px solid {colors.primary}
  performance-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.canvas}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  availability-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  model-title-lockup:
    textColor: "{colors.ink}"
    typography: "{typography.model-display}"
    accentColor: "{colors.primary}"
  gallery-thumbnail:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    border: 2px solid transparent
    height: 64px
    width: 64px
  gallery-thumbnail-active:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.primary}
    height: 64px
    width: 64px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.primary}"
    borderTop: 1px solid {colors.hairline}
    padding: "{spacing.section} 0"
  section-heading:
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    marginBottom: "{spacing.xl}"

---

## Components

### Buttons

**`button-primary`** — The main CTA is a solid `{colors.primary}` (#fb940f) rectangle with `{rounded.xs}` corners and white text at `{typography.button-md}` weight 600. On hover, the background deepens to `{colors.primary-active}` (#e07d00) with a subtle brightness shift; on press, it darkens further. The disabled state drops to `{colors.primary-disabled}` (#7d4a08) with `{colors.muted-soft}` text, effectively vanishing into the dark canvas to signal unavailability without drawing attention.

**`button-secondary`** — A bordered ghost button: `{colors.surface-card}` fill with a 1px `{colors.hairline}` border and `{colors.ink}` text. On hover, the fill shifts to `{colors.surface-strong}` and the border brightens slightly. Used for secondary actions like "View Specs" or "Compare" where the orange primary would compete with the main CTA.

**`button-ghost`** — A text-only button in `{colors.primary}` with no background or border. Used for inline actions like "Learn more" or "See all configurations." On hover, the text gains a 1px underline offset 4px below the baseline.

### Text Input

**`text-input`** — Dark-field input with `{colors.surface-soft}` background, 1px `{colors.hairline}` border, and `{colors.ink}` text. Placeholder text renders in `{colors.muted-soft}`. On focus, the border transitions to 1px solid `{colors.primary}`, providing a clear orange ring that stands out against the dark palette. The `{rounded.xs}` corner radius matches buttons for visual consistency. Height is 44px with 12px vertical / 16px horizontal padding.

### Navigation Bar

**`nav-bar`** — A 64px-tall fixed bar with `{colors.canvas}` background and a faint `{colors.hairline-soft}` bottom border. The Falcon crest sits at the far left; model names (Talon, Tiki, FragBox, Mach V) run horizontally in `{typography.nav-link}` — uppercase, 14px, Founders Grotesk Semibold. Active model links receive a 2px `{colors.primary}` underline offset 4px below the text. Right-side utilities (search icon, support link, cart) are rendered as icon buttons in `{colors.muted}` that brighten to `{colors.ink}` on hover. Below 744px the model menu collapses into a hamburger icon that opens a full-screen dark overlay with stacked nav links.

### Product Card

**`product-card`** — A `{colors.surface-card}` panel with `{rounded.sm}` corners containing a 4:3 aspect-ratio product render on a transparent/dark background, followed by the system name in `{typography.title-md}`, a one-line tagline in `{typography.body-sm}`, and a horizontal spec strip. The spec strip uses `spec-chip` tokens — small `{colors.surface-strong}` pills in `{typography.spec-label}` showing GPU, CPU, and RAM shorthand. Cards have `{spacing.base}` internal padding and cast no box-shadow; separation from the canvas comes purely from the fill-color difference. On hover, the entire card border gains a 1px `{colors.hairline}` outline and the product image scales up ~3% with a 200ms ease-out transition.

### Hero Banner

**`hero-banner`** — Full-width section with a minimum height of 600px. A full-bleed product photograph occupies the right two-thirds while a linear gradient overlay (`#202020` at 30% opacity fading to transparent) ensures text legibility on the left. The headline renders in `{typography.display-xl}` — Founders Grotesk X-Condensed at 64px uppercase — stacked above a one-line subhead in `{typography.body-md}`. A `button-primary` CTA sits below with `{spacing.lg}` (24px) top margin. The hero cycles between featured systems with a subtle crossfade; navigation dots at bottom-center use `{colors.muted-soft}` for inactive and `{colors.primary}` for active.

### Spec Chip

**`spec-chip`** — A compact inline tag at `{typography.spec-label}` (12px uppercase Founders Grotesk Medium) on a `{colors.surface-strong}` background with `{rounded.xs}` corners and 4px/10px padding. Used inside product cards and configuration panels to display hardware specs (e.g., "RTX 5090", "i9-15900K", "64GB DDR5"). The highlight variant `spec-chip-highlight` swaps the background to `{colors.accent-cyan}` (#02e2f2) with `{colors.canvas}` text to call out flagship or upgraded components.

### Configuration Selector

**`config-option`** — A bordered tile for selecting hardware components during system configuration. Background is `{colors.surface-soft}`, border is 1px `{colors.hairline}`, text is `{typography.caption}`, with `{rounded.sm}` corners and `{spacing.md}`/`{spacing.base}` padding. Each tile shows the component name, a brief spec line, and a price delta. **`config-option-selected`** swaps the border to 2px solid `{colors.primary}`, making the orange ring the sole selection indicator — no checkmark, no fill change. Tiles are laid out in a vertical stack on mobile and a 2–3 column grid on tablet and above. Hovering an unselected tile brightens the border to `{colors.border-strong}`.

### Performance Badge

**`performance-badge`** — A small `{colors.accent-gold}` (#ffd91a) pill with `{colors.canvas}` text at `{typography.uppercase-tag}` (10px bold uppercase). Used to flag performance tiers ("ELITE", "ULTRA", "PRO") on product cards and configuration headers. The `availability-badge` variant uses `{colors.accent-green}` (#00ff85) for in-stock / ready-to-ship messaging.

### Model Title Lockup

**`model-title-lockup`** — The system name rendered in `{typography.model-display}` (Founders Grotesk X-Condensed, 48px uppercase) in `{colors.ink}`, often paired with a thin `{colors.primary}` accent bar (3px wide, 40px tall) to the left of the text block. Used at the top of individual product pages and in the hero banner when a single system is featured.

### Gallery

**`gallery-thumbnail`** — A 64x64px square with `{colors.surface-soft}` background and `{rounded.xs}` corners displaying a downscaled product angle. The active thumbnail (`gallery-thumbnail-active`) gains a 2px `{colors.primary}` border. Thumbnails sit in a horizontal row below the main product image, scrollable on mobile. The main image area fills the available width with the product centered on a transparent-to-dark gradient background.

### Search Bar

**`search-bar`** — A 44px-tall input field with `{colors.surface-soft}` fill, `{rounded.sm}` corners, and a magnifying-glass icon in `{colors.muted}` at the left edge. Placeholder text reads "Search systems, specs, support..." in `{colors.muted-soft}`. On focus, the input expands to reveal a dropdown suggestions panel with `{colors.surface-card}` background and `{rounded.sm}` corners, showing recent searches and popular models.

### Footer

**`footer`** — A `{colors.canvas}` section with a `{colors.hairline}` top border. Content is organized into 4 columns on desktop: Systems, Support, Company, and Connect. Link text is `{typography.body-sm}` in `{colors.body}` that transitions to `{colors.primary}` on hover. The Falcon crest appears at bottom-left in `{colors.muted-soft}` alongside copyright text in `{typography.caption-sm}`. Social icons are rendered in `{colors.muted}` and brighten to `{colors.ink}` on hover. The footer collapses to stacked accordions on mobile.

### Section Heading

**`section-heading`** — A display-level heading in `{typography.display-lg}` (40px uppercase X-Condensed) with `{spacing.xl}` bottom margin. Used to introduce major page sections like "Featured Systems", "Why Falcon Northwest", or "Configure Your Build."

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + full-screen overlay. Hero banner stacks vertically — image above, text below — at reduced 360px min-height. Product cards go single-column, full-width. Config options stack in a single column. Gallery thumbnails scroll horizontally. Footer columns become stacked accordions. Display-xl drops to 36px. |
| Tablet | 744–1128px | Nav shows top 3 model links; overflow goes to a "More" dropdown. Product cards display in a 2-column grid. Config options use a 2-column layout. Hero maintains side-by-side layout but image occupies 55% width. Section spacing reduces to 48px. |
| Desktop | 1128–1440px | Full nav with all model links visible. Product cards in a 3-column grid. Config options in a 3-column grid. Hero at full 600px height with 65/35 image-text split. All spacing at default token values. |
| Wide | > 1440px | Content max-width caps at 1440px and centers on canvas. Product cards remain 3 columns but gain additional horizontal padding. Hero image can extend to viewport edge while text stays within the content column. |

### Touch Targets

- All interactive elements maintain a minimum 44x44px touch target on mobile and tablet
- Nav hamburger icon uses a 48x48px hit area
- Gallery thumbnails scale up to 72x72px on touch devices for easier selection
- Config option tiles have a minimum height of 56px on mobile
- Spec chips in product cards gain 4px additional vertical padding on touch devices

### Collapsing Strategy

- Navigation: model links collapse to hamburger at < 744px; utilities (search, cart) remain visible as icons
- Product grids: 3 columns → 2 columns at 1128px → 1 column at 744px
- Config grids: 3 columns → 2 columns at 1128px → 1 column stacked at 744px
- Hero banner: side-by-side → stacked (image on top) at 744px
- Footer: 4-column grid → 2-column at 744px → single-column accordions at < 480px
- Spec strips on product cards: horizontal scroll with fade-out edge indicator on mobile
- Section headings: display-lg (40px) → 28px on mobile; display-xl (64px) → 36px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color was declared; the dark canvas (#202020) is inferred from extracted color frequency, not a confirmed meta tag
- Exact Founders Grotesk X-Condensed font-weight values could not be confirmed — 700 is assumed for display roles based on typical usage; the actual weight may differ
- Interactive configuration builder behavior (multi-step flow, real-time price updates, drag-reorder) could not be fully mapped from static extraction
- Hover and focus transition durations are estimated at 150–200ms ease-out; actual values may differ
- The site is not on Shopify; cart and checkout UI patterns were not extractable and may use a custom or third-party solution
- Box-shadow and elevation values on modals, dropdowns, and tooltips were not captured
- The exact gradient stops and overlay opacity on hero banners are estimated from visual inspection
- #fb940f and #f7941d both appeared as extracted oranges — they may map to distinct interactive states or be aliased across CSS and SVG assets
- #ffd91a and #ffca05 similarly appeared as near-duplicate golds; one may be a hover or print variant
