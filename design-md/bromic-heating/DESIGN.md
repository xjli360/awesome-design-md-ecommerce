---
version: alpha
name: "Bromic Heating"
source_url: "https://www.bromic.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Charcoal steel glowing at one edge — that visual runs through every pixel of the Bromic digital experience. The single most distinctive extracted color, #313131, is not an accent but the atmosphere itself: a near-black charcoal that functions as both primary ink and the dominant canvas tone, collapsing the boundary between product photography and interface chrome. Against this darkness, a warm amber (#e8740c) bleeds into CTAs and hover states the way infrared heat bleeds into cold air — present but restrained, never garish. Typography stays strictly utilitarian: system sans-serif stacks at moderate weights, letting full-bleed product imagery of brushed-aluminum heater housings and dancing flame carry the brand voice. Display headlines run large (40–56px) at weight 600, spaced tight with negative letter-spacing that echoes the precision-milled slots of Bromic's radiant panels. Cards and product tiles use `{rounded.xs}` or `{rounded.none}` — sharp geometry that mirrors the rectilinear hardware silhouettes. The layout grid breathes wide on desktop (max-width ~1440px, generous `{spacing.section}` vertical rhythm) then collapses to edge-to-edge hero blocks on mobile, preserving the cinematic ratio of dark field to illuminated product. Navigation is minimal: a slim sticky bar with white logotype on dark, hamburger-collapsing below 1024px, reinforcing that the product — not the UI — is the spectacle. Surface hierarchy relies on subtle value shifts (#1a1a1a → #242424 → #313131) rather than borders or shadows, producing depth without ornament. The overall effect is a digital showroom lit by a single warm source, every element receding so the glow of heated metal can advance.

colors:
  primary: "#e8740c"
  primary-active: "#cf6508"
  primary-disabled: "#e8740c66"
  ink: "#313131"
  ink-inverse: "#ffffff"
  body: "#d4d4d4"
  body-dark: "#a8a8a8"
  muted: "#888888"
  hairline: "#3d3d3d"
  hairline-light: "#e0e0e0"
  canvas: "#1a1a1a"
  canvas-light: "#ffffff"
  surface-soft: "#242424"
  surface-card: "#2c2c2c"
  surface-elevated: "#313131"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-light: "#1a1a1a"
  accent-warm: "#f5a623"
  accent-heat: "#ff6b35"
  success: "#2ecc71"
  error: "#e74c3c"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.07
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 44px
    fontWeight: 600
    lineHeight: 1.09
    letterSpacing: -1px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.19
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.1px
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  overline:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
    opacity: 0.6
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 1px solid {colors.hairline}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.body}
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: 1px solid {colors.primary}
    backgroundColor: "{colors.surface-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: 0 48px
    borderBottom: 1px solid {colors.hairline}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    backdropFilter: blur(12px)
    borderBottom: 1px solid {colors.hairline}
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
    padding: 0
    overflow: hidden
  product-card-image:
    aspectRatio: 4/3
    objectFit: cover
    backgroundColor: "{colors.surface-soft}"
  product-card-body:
    padding: "{spacing.lg}"
    typography: "{typography.title-md}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    minHeight: 85vh
    padding: "{spacing.section-lg} {spacing.xxl}"
    typography: "{typography.display-xl}"
  hero-overlay:
    background: "linear-gradient(180deg, transparent 40%, {colors.canvas} 100%)"
    position: absolute
    inset: 0
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    borderSpacing: 0
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: 1px solid {colors.hairline}
  spec-table-value:
    typography: "{typography.body-md}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: 1px solid {colors.hairline}
  category-badge:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.body}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  comparison-toggle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    border: 1px solid {colors.hairline}
  comparison-toggle-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
    borderTop: 1px solid {colors.hairline}
  footer-heading:
    typography: "{typography.caption}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.md}"
  image-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    gap: "{spacing.xs}"
  image-gallery-thumb:
    rounded: "{rounded.xs}"
    border: 2px solid transparent
    opacity: 0.6
  image-gallery-thumb-active:
    border: 2px solid {colors.primary}
    opacity: 1
  heat-zone-indicator:
    backgroundColor: "radial-gradient(ellipse, {colors.accent-warm}33 0%, transparent 70%)"
    textColor: "{colors.accent-warm}"
    typography: "{typography.caption}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    gap: "{spacing.sm}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px 12px 48px
    height: 48px
    border: 1px solid {colors.hairline}

---

## Components

### Buttons

**`button-primary`** — A solid amber-orange (#e8740c) rectangle with barely-there radius (`{rounded.xs}`), white text set in weight 600 at 16px. On hover, the background deepens to `{colors.primary-active}` with a subtle 150ms ease transition. Disabled state drops to 60% opacity with the color muted to a semi-transparent amber. Used exclusively for purchase-intent actions: "Add to Cart," "Request a Quote," "Find a Dealer."

**`button-secondary`** — Transparent fill with a 1px border in `{colors.hairline}`, housing white text that matches the primary button's weight and size. On hover the border brightens to `{colors.body}` and the fill shifts to `{colors.surface-soft}`. This button appears alongside the primary for lower-priority actions: "Compare Models," "Download Spec Sheet," "View Gallery."

**`button-ghost`** — No background, no border; just `{colors.primary}` text that underlines on hover. Used inline within body copy or spec sections for tertiary navigation like "Learn more about infrared technology."

### Navigation

**`nav-bar`** — A 72px-tall fixed bar on a pure dark canvas (`{colors.canvas}`) with a single-pixel bottom border. The Bromic logotype sits left in white; primary navigation links (Products, Commercial, Residential, Support) are spaced evenly center-right in `{typography.nav-link}`. On scroll, the bar gains a subtle backdrop blur. Below 1024px, links collapse into a hamburger icon that triggers a full-screen dark overlay menu with large-tap link targets.

### Product Cards

**`product-card`** — A sharp-cornered (`{rounded.xs}`) container on `{colors.surface-card}` holding a 4:3 product image above a `{spacing.lg}` padded body zone. The image area has a soft dark fallback (`{colors.surface-soft}`) during load. Product name renders in `{typography.title-md}`, category in `{typography.overline}`, and a brief spec line (e.g., "6.0 kW | 20m² coverage") in `{typography.body-sm}` at `{colors.muted}`. Hover lifts the card 4px via box-shadow with a 200ms transition. No explicit border — depth comes from the value shift between card and canvas.

### Hero Section

**`hero-section`** — Full-bleed dark section occupying at least 85vh, anchored by a large product or lifestyle photograph with a bottom-gradient overlay fading to `{colors.canvas}`. Headline text (`{typography.display-xl}`, white) sits in the lower-third left-aligned, with a one-line subhead in `{typography.body-lg}` at `{colors.body}`. A primary CTA button floats below with `{spacing.lg}` separation. On mobile, the image aspect tightens and text shifts to center-aligned with reduced font size.

### Spec Table

**`spec-table`** — A contained block on `{colors.surface-soft}` listing technical specifications in two-column rows. Labels use `{typography.spec-label}` (uppercase, 12px, muted) and values use `{typography.body-md}` (white). Rows are divided by 1px `{colors.hairline}` borders. The table fills its container width and collapses gracefully on mobile by stacking label above value.

### Category Badge

**`category-badge`** — Small pill in `{colors.surface-elevated}` with uppercase overline text (`{typography.overline}`), used above product cards or within filters to denote heater type: "TUNGSTEN," "PLATINUM," "ECLIPSE." Minimal horizontal padding (12px), sharp radius.

### Comparison Toggle

**`comparison-toggle`** — A pill-shaped (`{rounded.full}`) toggle button used in product comparison interfaces. Inactive state shows a bordered ghost style; active state fills with `{colors.primary}` and white text. Arranged in a horizontal row, these allow users to toggle between compared models.

### Image Gallery

**`image-gallery`** — A main image area with a row of thumbnail selectors below. Thumbnails are `{rounded.xs}` with 60% opacity; the active thumbnail gains full opacity and a 2px `{colors.primary}` border. Main image transitions via a crossfade. The gallery container sits on `{colors.surface-soft}` with minimal internal gap (`{spacing.xs}`).

### Heat Zone Indicator

**`heat-zone-indicator`** — A radial gradient overlay used on product detail pages to visualize heating coverage area. A warm amber glow at 20% opacity radiates from center, with coverage specs displayed in `{typography.caption}` using `{colors.accent-warm}`. Purely decorative-informational; no interactive states.

### Search

**`search-input`** — A full-rounded (`{rounded.full}`) input field on `{colors.surface-soft}` with a magnifying glass icon inset left. Placeholder text in `{colors.muted}`, typed text in `{colors.body}`. On focus, the border shifts to `{colors.primary}`. Used in the site-wide search modal and dealer-locator sections.

### Footer

**`footer`** — Full-width dark section with top hairline border, organized in a 4-column grid (collapsing to 2 on tablet, stacked on mobile). Column headings use `{typography.caption}` in white; links use `{typography.body-sm}` in `{colors.body-dark}`. Bottom row contains legal text, region selector, and social icons. Generous vertical padding (`{spacing.section}`) separates footer from content above.

### Breadcrumb

**`breadcrumb`** — A horizontal trail using `{typography.body-sm}` in `{colors.muted}`, with chevron separators in `{colors.hairline}`. The final crumb is rendered in `{colors.on-dark}` without a link. Sits directly below the nav-bar with `{spacing.base}` top margin.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero text centers and drops to `{typography.display-md}`; nav collapses to hamburger; product cards stack full-width; spec tables stack label/value vertically; footer collapses to single column accordion |
| Tablet | 744–1128px | Two-column product grid; nav remains condensed with hamburger; hero retains left-alignment but at `{typography.display-lg}`; footer uses 2-column grid; comparison toggles scroll horizontally |
| Desktop | 1128–1440px | Full nav links visible; three-column product grid; hero at full `{typography.display-xl}`; side-by-side spec tables in comparison view; footer 4-column grid |
| Wide | > 1440px | Content max-width caps at 1440px and centers; additional lateral whitespace on canvas; hero imagery may extend full bleed while text container remains constrained |

### Touch Targets
- All interactive elements maintain a minimum 44×44px tap target on mobile
- Product card entire surface is tappable, not just the text link
- Hamburger icon has 48px hit area with generous padding from screen edge
- Footer links spaced at minimum `{spacing.lg}` vertically when stacked

### Collapsing Strategy
- Navigation: full horizontal links → hamburger + slide-over dark panel
- Product grids: 3-col → 2-col → 1-col with maintained card aspect ratios
- Spec tables: side-by-side columns → stacked label-above-value
- Hero sections: maintain minimum 60vh on mobile; text overlays shift from lower-third to center
- Footer: 4-col grid → 2-col → collapsible accordion sections
- Comparison view: fixed side-by-side on desktop → horizontal scroll with snap on mobile

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site is behind Cloudflare anti-bot protection ("Just a moment..." challenge page) — full CSS/token extraction was blocked
- Only a single hex color (#313131) was reliably extracted; the amber/orange primary and surface hierarchy are inferred from widely-visible Bromic brand materials and product photography, not live CSS inspection
- No custom web fonts detected — the site likely loads proprietary or licensed typefaces via JavaScript after the challenge clears; system stack is used as fallback throughout this spec
- Exact border-radius values on cards and buttons could not be measured; `{rounded.xs}` (4px) is a conservative estimate based on the brand's architectural aesthetic
- Exact nav-bar height, spacing values, and breakpoints are estimated from brand-typical patterns for premium hardware companies, not measured from computed styles
- Animation/transition timing functions and durations are estimated defaults (150–200ms ease)
- Dark mode is assumed as the primary theme based on available brand materials; a light variant may exist for certain landing pages or documentation sections but was not extractable
