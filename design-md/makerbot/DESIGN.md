---
version: alpha
name: "MakerBot"
source_url: "https://www.makerbot.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Warm drafting-paper cream (#f6f3ef) pressed against electric near-ultraviolet (#100aed) — that pairing is MakerBot's most revealing design decision: a hardware manufacturer whose entire identity pivots on an education mission chose the palette of a student's sketchbook rather than a server room. The canvas holds cream across three elevations — primary surface at #f6f3ef, card backgrounds softening to #ede8df, and dividers warming further to #dad0c0 — so the interface reads like layered stock rather than the cold whites typical of precision machinery. Only the primary CTA fires in that startling electric blue, applied with discipline to interactive targets. The secondary signal system is unusually rich: red (#ff0021, #e51b00) handles urgency and error states, green (#028d05, #007d04, #00c84e) maps success and printer availability, and yellow (#ffd204) flags caution without alarm. This four-color semantic system is uncommon in consumer hardware and reflects MakerBot's classroom context, where printer lifecycle events — job queued, print complete, filament low, maintenance required — need to be legible at a glance from across a lab.

  Type alternates between two working registers. Messina Sans handles brand voice — headline presence, navigation labels, button copy — with humanist warmth that positions MakerBot as pedagogy-first rather than hardware-first. IBM Plex Sans takes the data layer: build specifications, material names, layer-height readouts, and technical footnotes. The juxtaposition is deliberate: human authority for the brand, engineering authority for the machine. Baskerville surfaces selectively in editorial or testimonial contexts, borrowing institutional weight from academic serif conventions without committing to a serif identity system.

  Corner radii land at a considered middle register — `{rounded.sm}` at 8px for cards, inputs, and primary buttons — enough to signal approachability to K–12 audiences without crossing into overtly playful territory. The system tightens to `{rounded.xs}` for inline tags and table cells, reserving `{rounded.full}` only for status badges and filament swatches. Dark-navy (#000e1a) functions as a secondary dark surface for hero-banner moments and inverted top-bar overlays, creating dramatic contrast without reaching for pure black. The electric blue primary carries the singular action color across the entire interface with almost no exceptions, making every CTA unmistakable against the warm neutral ground.

colors:
  primary: "#100aed"
  primary-active: "#003388"
  primary-disabled: "#0693e3"
  ink: "#161616"
  body: "#282828"
  muted: "#5a5a5a"
  hairline: "#c4c4c4"
  hairline-soft: "#eeeeee"
  canvas: "#f6f3ef"
  surface-soft: "#ede8df"
  surface-card: "#ffffff"
  surface-warm: "#dad0c0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-red: "#ff0021"
  accent-red-dark: "#e51b00"
  accent-red-deep: "#ba1600"
  accent-green: "#028d05"
  accent-green-dark: "#007d04"
  accent-green-bright: "#00c84e"
  accent-yellow: "#ffd204"
  accent-orange: "#ff4102"
  accent-mint: "#00d084"
  dark-navy: "#000e1a"
  gray-mid: "#979797"

typography:
  display-xl:
    fontFamily: "'Messina Sans', Arial, Helvetica, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Messina Sans', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Messina Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Messina Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Messina Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'IBM Plex Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'IBM Plex Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'IBM Plex Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-sm:
    fontFamily: "'IBM Plex Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Messina Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Messina Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Messina Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  mono-sm:
    fontFamily: "'IBM Plex Mono', 'IBM Plex Sans', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  editorial-serif:
    fontFamily: "Baskerville, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0

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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    opacity: 0.5
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.ink}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    focusBorderColor: "{colors.primary}"
    placeholderColor: "{colors.muted}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    placeholderColor: "{colors.muted}"
    focusBorderColor: "{colors.primary}"
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
    activeLinkColor: "{colors.primary}"
    activeLinkBorderBottom: "2px solid {colors.primary}"
  nav-bar-dark:
    backgroundColor: "{colors.dark-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    activeLinkColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    imageAspectRatio: "4/3"
    imageBackground: "{colors.surface-soft}"
    ctaColor: "{colors.primary}"
  curriculum-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    borderLeft: "4px solid {colors.primary}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.dark-navy}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.sm}"
    paddingVertical: "{spacing.section}"
    accentColor: "{colors.primary}"
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    paddingVertical: "{spacing.section}"
  status-badge-success:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  status-badge-success-soft:
    backgroundColor: "{colors.accent-green-bright}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  status-badge-error:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  status-badge-warning:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  status-badge-info:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  spec-row:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.mono-sm}"
    valueColor: "{colors.ink}"
    padding: 10px 0
  ecosystem-tab:
    inactiveBackgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    inactiveTextColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    gap: "{spacing.xs}"
  grade-level-tag:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  filament-swatch:
    size: 32px
    rounded: "{rounded.full}"
    defaultBorder: "2px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.primary}"
    selectedOutline: "2px solid {colors.primary}"
    outlineOffset: 2px
  filament-selector-panel:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    headerTypography: "{typography.title-sm}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    swatchGap: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.gray-mid}"
    linkHoverColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    padding: "{spacing.xxl} 0"
    borderTop: "none"

## Components

### Buttons

**`button-primary`** — The electric-blue (#100aed) primary button is the singular action signal across the entire interface, appearing on add-to-cart, configure-printer, and request-quote flows. It carries `{rounded.sm}` corners at 48px height with Messina Sans weight-600 copy. Active state drops to the deep navy-blue `{colors.primary-active}` (#003388); disabled reduces opacity to 0.5 over the lighter `{colors.primary-disabled}` (#0693e3).

**`button-secondary`** — An outlined ghost on the cream canvas, bordered in `{colors.ink}` at 2px with matching 48px height. Used for secondary choices on product pages — "Compare," "Download Spec Sheet," "Add to Wishlist." Hover state fills to `{colors.surface-soft}` without changing the border.

**`button-ghost`** — Text-only, primary-blue label, no border or background. Applied to tertiary actions inside dense layouts like spec-table rows, accordion footers, and inline curriculum links. Never used as a standalone page-level CTA.

### Navigation

**`nav-bar`** — Sits on the cream canvas (#f6f3ef) at 72px height with a barely-there `{colors.hairline-soft}` bottom border. Active section is distinguished by a 2px electric-blue bottom border on the link itself, not a background fill, keeping the bar visually light. Messina Sans weight-500 at 15px.

**`nav-bar-dark`** — The inverted variant on dark-navy (#000e1a) appears for product-category landing pages and the homepage hero section's sticky state on scroll. Active links still use `{colors.primary}` blue so the electric accent reads clearly against the dark ground. Mobile expands into a full-screen overlay drawer.

### Forms & Inputs

**`text-input`** — Cream background, thin `{colors.hairline}` border at 1px, `{rounded.xs}` corners, 48px height. Focus state replaces the hairline with a 2px electric-blue stroke — no glow or shadow, just the color swap. Error state uses `{colors.accent-red}` on both border and helper text. Placeholder copy renders in `{colors.muted}`.

**`search-input`** — Set in `{colors.surface-soft}` (#ede8df) rather than white, giving the search field a warm inset quality against the cream canvas. Slightly shorter at 44px, `{rounded.sm}` corners. Leading magnifier icon in `{colors.muted}`; clears to primary blue on focus.

### Product Cards

**`product-card`** — White surface-card against the cream canvas creates a subtle lift without an explicit drop shadow. 1px `{colors.hairline}` border, `{rounded.sm}` corners, and an image region set against `{colors.surface-soft}` for visual separation. Product name in `{typography.title-md}`, descriptor copy in `{typography.body-sm}`. CTA link in `{colors.primary}` blue, not a full button.

**`curriculum-card`** — The education-specific card variant. Warm `{colors.surface-soft}` background with a 4px electric-blue left border accent signals educational content at a glance. Carries grade-level tags (`grade-level-tag`) in the upper-right corner and meta information (subject area, duration) in `{typography.caption}` / `{colors.muted}`.

### Status Badges

**`status-badge-success`** and **`status-badge-success-soft`** — Two green variants: dark (#028d05) for printer-ready or in-stock states, and bright (#00c84e) for recently-completed print jobs. Both `{rounded.full}`, uppercase IBM Plex Sans weight-600 at 11px.

**`status-badge-error`** — Vivid red (#ff0021) on white for filament-out, print-failed, or connectivity-lost states. The deeper variants (#e51b00, #ba1600) are reserved for destructive-action confirmation dialogs, not badges.

**`status-badge-warning`** — Yellow (#ffd204) with `{colors.ink}` text (not white — the yellow is too light for white legibility). Used for filament-low, firmware-update-available, and maintenance-recommended states.

**`status-badge-info`** — Primary blue (#100aed) with white text. Appears on "NEW" labels, feature-release announcements, and active-queue indicators in the print dashboard.

### Spec Rows

**`spec-row`** — Two-column horizontal row: left label in `{typography.body-sm}` / `{colors.muted}`, right value in `{typography.mono-sm}` / `{colors.ink}`. Separated by a `{colors.hairline}` bottom border. IBM Plex Mono renders print-resolution, layer-height, nozzle-diameter, and build-volume values, giving hardware specs a technical, instrument-readout character. Used in both product detail pages and print-dashboard info panels.

### Hero Banners

**`hero-banner`** — Full-bleed dark-navy (#000e1a) with white body text and electric-blue CTA. Title in `{typography.display-xl}` (Messina Sans 56px/700), supporting body in `{typography.body-md}`. Section padding at `{spacing.section}` top and bottom.

**`hero-banner-light`** — The cream-surface variant for mid-page promotional sections — new printer launch, ecosystem expansion announcements. Warm background reduces visual fatigue across long pages compared to back-to-back dark heroes.

### Ecosystem Tabs

**`ecosystem-tab`** — Segmented pill-tab system used to switch between product lines (METHOD, Sketch, LABS) or content categories (Printers, Filament, Software, Curriculum). Inactive state on `{colors.surface-soft}`, active fills with `{colors.primary}` and flips to white text. `{rounded.xs}` keeps the tabs from reading as bubble-shaped; the grouping renders as a compact bar with `{spacing.xs}` gap between items.

### Filament Components

**`filament-swatch`** — 32px circular chip in `{rounded.full}` with a 2px `{colors.hairline}` border at rest. Selected state adds a 2px offset electric-blue outline ring. Renders in a horizontal scrollable row on mobile, wrapping grid on tablet and up.

**`filament-selector-panel`** — Warm `{colors.surface-soft}` container with `{rounded.sm}` and `{spacing.lg}` padding. Header label in `{typography.title-sm}`, swatch labels in `{typography.caption}` / `{colors.muted}`. The entire panel sits inline beneath the product image on product detail pages rather than in a modal.

### Grade Level Tags

**`grade-level-tag`** — Small pill in `{colors.surface-warm}` (#dad0c0) with uppercase IBM Plex Sans label. Communicates curriculum target range (K–2, 3–5, 6–8, 9–12, Higher Ed) on curriculum-cards and course-catalog entries without competing with the electric-blue primary.

### Footer

**`footer`** — Near-black (#161616) background, column layout with white headings in `{typography.title-sm}` and gray-mid (#979797) link text that lifts to white on hover. No border-top; the contrast with the warm canvas above provides sufficient visual separation. Bottom row carries legal copy in `{typography.caption}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout; nav collapses to hamburger opening full-screen dark-navy overlay drawer; product cards stack vertically; ecosystem-tab bar scrolls horizontally; hero type scales to display-sm (28px); filament swatches in horizontal scroll row |
| Tablet | 744–1128px | Two-column product card grid; nav bar shows primary links with overflow in dropdown; hero type at display-md (36px); curriculum cards in two-column grid; spec rows maintain full width |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav bar with all sections visible; hero banner at display-xl (56px); sidebar-style filament selector panel on product detail pages |
| Wide | > 1440px | Max-width container at 1440px centered; hero background extends edge-to-edge behind contained content; increased section padding to maintain rhythm at large viewports |

### Touch Targets

- All buttons minimum 48px tall; ghost/text buttons gain 12px vertical padding to meet target without adding visual bulk
- Filament swatches are 32px but wrapped in a 48px tap zone with invisible padding
- Ecosystem-tab items gain 44px minimum tap height on mobile even at compact visual size
- Navigation drawer links set to 56px row height on mobile for easy scanning and tapping
- Form inputs maintain 48px height across all breakpoints

### Collapsing Strategy

- Primary nav: full horizontal on desktop; icon+label on tablet; hamburger drawer on mobile
- Product cards: 4-col → 3-col → 2-col → 1-col across Wide/Desktop/Tablet/Mobile
- Spec rows: always full-width two-column; label truncates to abbreviation on mobile (e.g., "Build Volume" → "Build Vol.")
- Ecosystem tabs: wrap on desktop, horizontal scroll with fade mask on tablet and mobile
- Hero banners: type scale steps down one level per breakpoint; CTA buttons shift from inline-pair to stacked on mobile
- Curriculum cards: 3-col → 2-col → 1-col; left-border accent preserved at all sizes
- Footer: four-column → two-column → single accordion-collapsed on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `surface-card` white (#ffffff) is a standard inference — not directly observed in extraction; exact card background unconfirmed
- `#0693e3` and `#00d084` appear in WordPress Gutenberg editor defaults and may not be intentional MakerBot brand colors; treated here as `primary-disabled` and `accent-mint` but usage context is uncertain
- Exact font weights for Messina Sans (whether the brand uses a full variable-weight version or select static cuts) could not be confirmed from extraction
- IBM Plex Mono presence is inferred from the IBM Plex Sans brand relationship and `monospace` stack entry; a dedicated `IBM Plex Mono` cut was not explicitly extracted
- Animation and transition timing (hover state durations, drawer animation, tab-switch transitions) are not extractable from static color/font analysis
- Whether the nav bar uses the cream or dark-navy default on the homepage (vs. scrolled state) could not be confirmed
- Exact spacing scale is an 8px-grid inference; MakerBot's production design tokens were not accessible
- Baskerville editorial usage frequency and exact weight/size application in production could not be confirmed from available extraction data
- Print-management dashboard and hardware-facing UI components (job queue, print progress, remote monitoring) were not observable from the marketing site extraction
