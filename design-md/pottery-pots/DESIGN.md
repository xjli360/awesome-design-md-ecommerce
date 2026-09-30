---
version: alpha
name: "Pottery Pots"
source_url: "https://www.potterypots.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bare concrete floors, a single oversized vessel catching afternoon light — Pottery Pots builds its digital presence the way an architecture gallery curates a show: one object at a time against an almost-white field (#f7fafd). The canvas breathes at that pale blue-grey temperature rather than pure white, lending the faintest atmospheric depth that keeps product photography from floating in a void. Surfaces step down through a warm grey (#eeeeee) for collection grids and filter panels, creating just enough figure-ground separation without introducing hard dividers. The primary interaction color is a confident black — buttons, navigation links, and CTAs all arrive in near-pure ink, treating every click-target as a deliberate mark on paper rather than a colored lozenge demanding attention. Typography leans on a geometric sans-serif stack at restrained weights; display headings sit large but light (weight 300–400), giving headlines the quality of etched stone rather than shouted signage. Body copy holds at 16px with generous `{spacing.lg}` line-height, respecting the same negative space philosophy that defines the physical product line. Product cards use `{rounded.none}` — no softened corners, no playful pills — reinforcing the architectural register. The sole curve lives in circular material-swatch selectors (`{rounded.full}`), a functional flourish that echoes the planters' own silhouettes. Navigation is minimal: a sticky top bar collapses to a slide-out drawer on mobile, with category labels in uppercase micro-tracking that reads like gallery-wall didactics. Image aspect ratios run tall (3:4 and 4:5), framing each planter as a portrait subject. Hover states are subtle — a 120ms opacity fade to 0.7 rather than color shifts — keeping the gallery-quiet tone intact across interactions.

colors:
  primary: "#1a1a1a"
  primary-active: "#000000"
  primary-disabled: "#999999"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#767676"
  muted-soft: "#a0a0a0"
  hairline: "#eeeeee"
  hairline-soft: "#f2f2f2"
  canvas: "#f7fafd"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-warm: "#c8b89a"
  accent-sage: "#8a9a7b"
  error: "#c0392b"
  success: "#2d6a4f"

typography:
  display-xl:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-upper:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.1px
  nav-upper:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 1px
    textTransform: uppercase
  price:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0

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
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    textTransform: uppercase
    letterSpacing: 1px
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
    padding: 13px 31px
    height: 48px
    border: 1px solid {colors.ink}
    textTransform: uppercase
    letterSpacing: 1px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    textDecoration: underline
    textUnderlineOffset: 3px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.ink}
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-upper}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
    position: sticky
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    boxShadow: 0 1px 0 {colors.hairline}
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 0
    imageAspectRatio: 4/5
    imageObjectFit: cover
    hoverOpacity: 0.7
    transition: opacity 120ms ease
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.md}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 85vh
    padding: "{spacing.section} {spacing.xl}"
    imageObjectFit: cover
    overlayTextPosition: bottom-left
  hero-headline:
    typography: "{typography.display-xl}"
    maxWidth: 680px
  hero-subline:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    maxWidth: 480px
    marginTop: "{spacing.base}"
  collection-grid:
    columns: 3
    gap: "{spacing.xs}"
    padding: 0 {spacing.xl}
  collection-header:
    typography: "{typography.display-md}"
    textAlign: center
    marginBottom: "{spacing.xl}"
  material-swatch:
    width: 28px
    height: 28px
    rounded: "{rounded.full}"
    border: 2px solid transparent
    borderActive: 2px solid {colors.ink}
  material-swatch-label:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    marginTop: "{spacing.xs}"
  size-selector:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 10px 20px
    border: 1px solid {colors.hairline}
    borderActive: 1px solid {colors.ink}
  filter-panel:
    backgroundColor: "{colors.surface-card}"
    padding: "{spacing.lg}"
    borderRight: 1px solid {colors.hairline}
    width: 280px
  filter-heading:
    typography: "{typography.caption-upper}"
    color: "{colors.muted}"
    marginBottom: "{spacing.md}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    separator: "/"
    separatorSpacing: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.caption-upper}"
    color: "{colors.muted-soft}"
    marginBottom: "{spacing.base}"
  search-overlay:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    position: fixed
    inset: 0
    zIndex: 1000
    padding: "{spacing.xl}"
  search-input:
    typography: "{typography.display-md}"
    border: none
    borderBottom: 2px solid {colors.ink}
    padding: "{spacing.md} 0"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center

---

## Components

### Buttons

**`button-primary`** — A rectangular, cornerless black button with white uppercase text tracked at 1px. The zero-radius silhouette matches the architectural language of the planters themselves — no softness, all intent. On hover the background deepens to pure black; disabled state fades to `{colors.primary-disabled}` mid-grey. Minimum touch width is 160px on product pages.

**`button-secondary`** — Outlined variant sharing the same dimensions and uppercase treatment. A single-pixel ink border on transparent ground inverts on hover, filling black with white text in a 200ms transition. Used for secondary actions like "View all" on collection teasers and "Add to wishlist" on product detail.

**`button-text`** — An underlined text link styled as a button for inline actions (read more, view specs). The underline sits 3px below baseline to avoid collision with descenders. Color matches `{colors.ink}` with no background or border.

### Navigation

**`nav-bar`** — A 64px-tall sticky header on a white surface with uppercase category links at `{typography.nav-upper}` tracking. A thin 1px `{colors.hairline}` bottom border grounds it against the pale canvas. Logo sits left, navigation center, utility icons (search, account, cart) right. On scroll the border transitions to a subtle box-shadow.

**`announcement-bar`** — A 36px strip above the nav in solid ink-black carrying `{typography.caption}` white text for shipping thresholds or promotions. Dismissible via a small "×" icon on the right edge.

### Product Card

**`product-card`** — Zero-radius card with a `{colors.surface-soft}` grey background filling the image area at a 4:5 portrait ratio. Product photography uses `object-fit: cover`. On hover, image opacity fades to 0.7 over 120ms — no scale transform, no overlay — keeping the gallery aesthetic quiet. Title appears below at `{typography.title-sm}` weight 500, followed by price at `{typography.price}`. No rating stars, no badges — pure product focus.

### Hero

**`hero-section`** — Full-bleed lifestyle photography at 85vh minimum height with headline text anchored bottom-left. The `{typography.display-xl}` headline at weight 300 floats over imagery without a scrim, relying on image art direction (light pots on dark backgrounds or vice versa) for contrast. A body-text subline at `{typography.body-md}` and a `button-primary` CTA stack below with `{spacing.base}` gaps.

### Material & Size Selectors

**`material-swatch`** — Circular 28px color dots (`{rounded.full}`) representing finishes like charcoal, grey, sandy beige, and terracotta. Active state gains a 2px ink border. A caption label below names the material.

**`size-selector`** — Rectangular inline chips with `{rounded.none}` and a hairline border. Active selection switches to ink border. Chips display dimension text (e.g. "Ø 40 × H 35 cm") in `{typography.body-sm}`.

### Filter Panel

**`filter-panel`** — A 280px left-rail panel on desktop with grouped filter sections (Material, Size, Color, Shape). Each group heading uses `{typography.caption-upper}` in muted grey. Checkboxes and collapsible accordions let users narrow selections. Panel collapses to a bottom-sheet on mobile.

### Search

**`search-overlay`** — Full-screen takeover with a large text input styled at `{typography.display-md}` with only a bottom border. No rounded search bar — the line-only input reinforces the architectural minimalism. Recent searches and suggested products appear below in a grid.

### Footer

**`footer`** — Inverted section using `{colors.primary}` (dark) background with white text. Columns for Shop, About, Support, Social. Headings in `{typography.caption-upper}` with muted-soft color, links in `{typography.body-sm}`. Generous `{spacing.section}` vertical padding mirrors the spacious page rhythm.

### Breadcrumb

**`breadcrumb`** — A quiet wayfinding trail in `{typography.caption}` muted grey with "/" separators. Sits above collection headings with `{spacing.lg}` bottom margin.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero drops to 60vh; filter panel becomes bottom-sheet modal; footer stacks to single column; section padding reduces to `{spacing.xl}` |
| Tablet | 744–1128px | Two-column product grid; nav remains visible but condenses spacing; hero headline drops to `{typography.display-lg}`; filter panel overlays from left as slide-out |
| Desktop | 1128–1440px | Three-column grid with left filter rail; full sticky nav; hero at 85vh; all components at default sizing |
| Wide | > 1440px | Content max-width caps at 1440px and centers; grid may expand to four columns on collection pages; `{spacing.section-lg}` between major blocks |

### Touch Targets

- All interactive elements maintain 44×44px minimum tap area on mobile
- Material swatches expand to 36px diameter on touch devices with 12px gap
- Size selector chips increase padding to 14px 24px on mobile
- Nav hamburger icon is 48×48px touch target

### Collapsing Strategy

- Navigation categories move into a full-height slide-out drawer with `{typography.title-md}` sizing for easy scanning
- Product grid reduces from 3 → 2 → 1 columns as viewport narrows
- Filter panel transitions from persistent sidebar (desktop) → slide-out overlay (tablet) → bottom-sheet (mobile)
- Hero section reduces min-height and headline scale but maintains bottom-left text anchor
- Footer columns stack vertically with accordion expand/collapse for each section on mobile
- Announcement bar text truncates with ellipsis on narrow screens, full message on desktop

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Fonts unverified**: Only Font Awesome icon fonts were detected in extraction. The actual body/display typeface could not be confirmed — Inter is used as a reasonable geometric sans-serif placeholder based on the site's visual style, but the real font may differ (possibly a custom or commercially licensed face loaded via JS)
- **Color palette extremely sparse**: Only two colors (#f7fafd, #eeeeee) were extracted — both near-white/light-grey background tones. The dark primary (#1a1a1a) and accent tones (warm, sage) are inferred from widely-observable brand materials but could not be confirmed from extraction
- **Interaction tokens missing**: Transition durations, easing curves, and hover-state specifics are estimated from common architectural-brand patterns rather than extracted CSS custom properties
- **Spacing scale assumed**: No spacing variables were captured; the scale above follows standard 4px-grid increments typical of the observed layout rhythm
- **Component dimensions approximate**: Button heights, nav height, and card ratios are based on visual inspection patterns and may differ from actual computed values
- **Dark mode**: No dark-mode tokens detected or documented; the brand appears to operate exclusively in light mode
- **Icon system**: Font Awesome 6 Pro was detected but it is unclear whether custom SVG icons supplement or replace it in the UI
