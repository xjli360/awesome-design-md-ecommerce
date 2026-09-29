---
version: alpha
name: "Ultimaker"
source_url: "https://www.ultimaker.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Electric blue #100aed arrives at the interface the way a status LED fires on a live print head — immediate, unambiguous, and engineered rather than styled. Ultimaker's visual language is built on the tension between that voltage and a near-black base (#1b1b1b, #000e1a) pulled from deep-shadow industrial photography: machines photographed against darkness rather than white infinity coves. IBM Plex Sans carries the bulk of the typographic work, its rational construction making spec readouts, layer counts, and filament weights feel at home in a UI that might otherwise read as generic corporate tech. IBM Plex Sans Condensed appears in tighter informational contexts — material badges, printer model labels — where horizontal compression earns real estate without sacrificing legibility. Artex, the geometric display typeface found in the stack, carries the headline register: its precise construction echoes the build-plate grid while remaining warm enough for a brand selling to engineers who care about craft. The warm cream tone (#dad0c0) surfaces in editorial photography backdrops, grounding machine imagery in a material studio environment rather than a sterile lab. Orange-red #ff4500 reads as a functional alert register rather than a decorative accent — consistent with an interface where color carries semantic weight. The palette runs a disciplined gray ladder from #ececec through #8d8d8d to #444444, giving the system room to differentiate disabled states, hover layers, and border weights without reaching for new hues. Rounded corners are conservative: `{rounded.xs}` on form inputs, `{rounded.sm}` on cards — nothing softer than that. The brand's confidence lives in exactness.

colors:
  primary: "#100aed"
  primary-active: "#003388"
  primary-disabled: "#b8b8b8"
  primary-dark: "#003399"
  accent: "#ff4500"
  accent-amber: "#ff9900"
  ink: "#1b1b1b"
  body: "#32373c"
  muted: "#8d8d8d"
  muted-light: "#949494"
  hairline: "#d9d9d9"
  hairline-light: "#ececec"
  canvas: "#ffffff"
  canvas-warm: "#faf8f6"
  surface-soft: "#f1f1f1"
  surface-card: "#ececec"
  surface-dark: "#000e1a"
  surface-mid-dark: "#282828"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  neutral-warm: "#dad0c0"

typography:
  display-xl:
    fontFamily: "'Artex', 'Messina Sans', 'IBM Plex Sans', Arial, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Artex', 'Messina Sans', 'IBM Plex Sans', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Artex', 'Messina Sans', 'IBM Plex Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'IBM Plex Sans', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "'IBM Plex Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'IBM Plex Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'IBM Plex Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'IBM Plex Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'IBM Plex Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  label-condensed:
    fontFamily: "'IBM Plex Sans Condensed', 'IBM Plex Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.6px
    textTransform: uppercase
  spec-mono:
    fontFamily: "'IBM Plex Sans', monospace, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'IBM Plex Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'IBM Plex Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'IBM Plex Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  eyebrow:
    fontFamily: "'IBM Plex Sans Condensed', 'IBM Plex Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1px
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
    rounded: "{rounded.xs}"
    padding: 13px 28px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 12px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 12px 27px
    height: 48px
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 28px
    height: 48px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 9px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-light}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: none
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-light}"
    rounded: "{rounded.sm}"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.primary}"
    minHeight: 620px
  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
    border: "1px solid {colors.hairline}"
  printer-model-tag:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  alert-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  spec-row:
    backgroundColor: "{colors.canvas}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    typography: "{typography.spec-mono}"
    borderBottom: "1px solid {colors.hairline-light}"
    padding: "12px 0"
  comparison-table:
    headerBg: "{colors.surface-dark}"
    headerText: "{colors.on-dark}"
    rowBg: "{colors.canvas}"
    altRowBg: "{colors.surface-soft}"
    cellTypography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    border: "1px solid {colors.hairline-light}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-light}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    height: 48px
  section-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.primary}"
    headlineTypography: "{typography.display-sm}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: none
  feature-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"

---

## Components

### Buttons

**`button-primary`** — Electric blue (#100aed) fill, white label, 4px radius; the sharpness signals engineering precision rather than consumer softness. Active state drops to deep navy (#003388); disabled uses mid-gray (#b8b8b8) fill with white text — no opacity trick. At 48px height with 28px horizontal padding, it reads as a clear action target without inflating to enterprise-CTA scale. Used for primary purchase and configuration actions.

**`button-secondary`** — White canvas with a 1.5px ink border; matches height and radius to the primary exactly. Sits beside `button-primary` in two-CTA hero and PDP layouts where neither action should dominate the other.

**`button-ghost`** — Transparent fill, 1.5px primary-blue border, primary-blue label. Preferred on dark backgrounds (`{colors.surface-dark}`) where a solid primary button would be too heavy and a white outline would feel generic.

**`button-dark`** — Near-black (#1b1b1b) fill with white label. Used in contexts where the electric primary blue would clash with page-level dark backgrounds, such as footer CTAs or dark-section panels.

**`button-sm`** — Same electric blue fill at 36px height; used for inline actions like "Add to comparison" on product listing rows where 48px would overwhelm the row.

### Text Input

**`text-input`** — White canvas, 1px hairline border at rest, 1.5px primary-blue stroke on focus — the only keyboard-cue color in the form system. 4px radius keeps the corner sharp. 48px height aligns with button height for clean form-row pairing. Placeholder uses `{colors.muted}` (#8d8d8d). Error state should inherit `{colors.accent}` (#ff4500) border.

### Navigation

**`nav-bar`** — White canvas, 72px tall, 1px hairline-light separator. Nav links at IBM Plex Sans 14px medium weight — deliberately lean, keeping visual weight on the product photography below. Desktop nav exposes top-level product categories, Solutions, and Resources with a utility strip (search, language, account) at right. `nav-bar-dark` swaps to `{colors.surface-dark}` (#000e1a) for hero-overlaid pages; no separator needed against a dark page background.

### Product Card

**`product-card`** — White canvas, 1px `{colors.hairline-light}` border, 8px radius. Image zone sits on `{colors.surface-soft}` (#f1f1f1) — a neutral stage for machine renders that avoids the pure-white-on-white problem. Title at IBM Plex Sans 18px semi-bold; body copy at 14px regular; 24px internal padding. Badges (`printer-model-tag`, `material-badge`) sit above the headline in the card header zone.

### Hero Section

**`hero-section`** — Deep `{colors.surface-dark}` (#000e1a) background; 52px display-xl headline in Artex, white; eyebrow label in primary blue uppercase condensed sits above the headline. Body copy at 16px regular, muted by a 70% white opacity in dark contexts. Minimum 620px height to contain full-machine silhouette photography. Primary CTA and a secondary ghost button sit side-by-side below the copy.

### Badges

**`material-badge`** — Soft gray fill with hairline border; IBM Plex Sans Condensed 12px uppercase at 0.6px tracking. Used on product cards and PDP material selectors to label filament types, print cores, and compatibility tiers.

**`printer-model-tag`** — Electric blue fill, white label; marks printer model designations ("S5", "S7", "Factor 4") inline with product titles and in comparison tables. The blue here is a direct signal that this is a model identifier, not a status.

**`alert-badge`** — Vivid #ff4500 fill, white label. Marks out-of-stock, compatibility warnings, or hardware error states. Used functionally only — never as a promotional accent.

### Spec Row

**`spec-row`** — Full-width horizontal layout: muted gray label floated left, ink-colored value right; IBM Plex Sans semi-monospaced at 13px with 0.2px tracking for digit stability. Bottom border separates rows. Used in printer specification panels and filament data sheets. Multi-value specs (e.g., build volume XYZ) use the same row pattern with the value formatted as a single string.

### Comparison Table

**`comparison-table`** — Header row uses `{colors.surface-dark}` background with white IBM Plex Sans semi-bold headers at 16px. Body rows alternate between canvas and `{colors.surface-soft}` for legibility across wide column sets. Thin `{colors.hairline-light}` borders on all sides. Cell text at 14px regular. A sticky first column on scroll holds the spec-name label. Checkmark icons for boolean specs use the primary blue; X icons use the muted gray, not the alert red.

### Search Bar

**`search-bar`** — Soft gray fill (`{colors.surface-soft}`), hairline border at rest, no inner shadow. Focus: 1.5px primary-blue stroke. 4px radius. 48px height. Placeholder at `{colors.muted-light}`. A search-submit icon button appears inside the right edge using primary blue fill.

### Section Header

**`section-header`** — Transparent background; eyebrow in `{colors.primary}` (#100aed) using `{typography.eyebrow}` (12px Condensed, uppercase, 1px tracked); headline in `{typography.display-sm}` at 28px. Eyebrow-above-headline pattern mirrors industrial panel conventions of category-then-value. Used above product grid sections, feature breakdowns, and ecosystem callouts.

### Feature Callout

**`feature-callout`** — Soft gray (`{colors.surface-soft}`) fill, 8px radius, 32px padding. Title at 18px semi-bold, body at 14px regular. A 3px primary-blue left-border accent marks the callout visually; used for "Why Ultimaker" panel blocks and key differentiation statements.

### Footer

**`footer`** — Deep `{colors.surface-dark}` (#000e1a) background; column heading labels at IBM Plex Sans 16px semi-bold in white; link text in `{colors.hairline}` (#d9d9d9) — a secondary hierarchy without a new hue. Legal copy and country selector at 13px caption scale. No top border; the page content bleeds directly into the footer background on dark-section pages.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger with full-screen dark drawer; hero headline drops to `{typography.display-sm}`; product cards stack vertically one-up; spec table scrolls horizontally with sticky label column; comparison table is 2 columns max |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level items only, secondary in drawer; hero maintains full-width dark panel; section headers stay side-margin aligned; comparison table shows up to 3 printer columns |
| Desktop | 1128–1440px | Three-column product grid; full nav visible with utility strip; hero shifts to split layout — headline/CTA left, machine render right; comparison table shows full column set |
| Wide | > 1440px | Content max-width 1440px centered; hero image bleeds edge-to-edge behind a contained text column; four-column product grid for accessories and materials |

### Touch Targets

- All buttons and interactive controls minimum 48×48px tap area
- Mobile nav drawer items: 56px row height
- Spec rows and comparison table cells: 44px minimum touch height on mobile
- Badge and tag elements: padded to at least 32px height on touch viewports

### Collapsing Strategy

- Primary nav collapses to hamburger at < 1024px; drawer is full-screen with the dark background and white links
- Comparison table horizontally scrollable below 1128px; first column (spec label) sticks at left edge
- Spec rows maintain full-width two-column layout until 480px, below which label and value stack vertically
- Hero body copy truncated to two lines on mobile; full text visible on tablet and up
- Section header eyebrow hidden on mobile below 375px to preserve headline prominence

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Artex typeface role is inferred from font-stack position; exact use cases (display-only vs. broader UI) not confirmed from extraction
- Messina Sans appears in the stack but its specific UI role (marketing vs. interface) is unconfirmed
- Exact button border-radius not measured from CSS; 4px is inferred from engineering-brand aesthetic and extracted color data pattern
- Hover and transition specs (duration, easing curves) not captured in extraction
- Dark-mode vs. dark-section distinction unclear — the deep #000e1a tones may be section-level design rather than a full site-wide dark mode
- #dad0c0 (warm cream/beige) token included but its precise UI role is uncertain; may be editorial photography backdrop only, not a UI surface
- #ff9900 (amber orange) role not confirmed; possibly used in rating stars, status indicators, or partner ecosystem badges
- Icon system and glyph library structure not accessible from extraction
- Nav height (72px) and responsive breakpoint values are estimated from convention, not measured from live CSS
- Print-specific or accessibility (high-contrast) theme overrides not captured
