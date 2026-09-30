---
version: alpha
name: "Puzz"
source_url: "https://puzz.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A puzzle-and-games archive that wears its 1999 heritage as a quiet confidence — the primary green `#6aaa64` (a Wordle-correct-leaf green) and its deeper sibling `#538d4e` (the meta theme-color) suggest a brand that grew up alongside browser-based casual gaming, not a startup chasing trends. The palette leans heavily into midnight blues (`#1a1a2e`, `#16213e`, `#0f3460`) for backgrounds and nav bars, creating a dark-theme-ready canvas that makes the green CTAs and gold accent `#b59f3b` pop like correct guesses. Type runs system-native (`-apple-system`, `BlinkMacSystemFont`, `Roboto`, `Segoe UI`) — no custom font investment, which signals a lean engineering team prioritizing load speed and accessibility over brand typography. Buttons carry `{rounded.sm}` corners (8px) rather than pills, and the `{rounded.md}` (12px) on cards keeps the interface crisp without feeling toy-like. The extracted color list includes a purple `#8b5cf6` and a red `#e74c3c` that likely serve as category badges or difficulty indicators, while the `#d7dadc` and `#e2e8f0` grays handle borders and muted text. This is a brand that trusts its content — 47,000+ puzzles — over visual polish; the design system is a container, not a decoration.

colors:
  primary: "#6aaa64"
  primary-active: "#5a9654"
  primary-disabled: "#a0d49c"
  ink: "#1a1a2e"
  body: "#2d3748"
  muted: "#718096"
  muted-soft: "#a0aec0"
  hairline: "#d7dadc"
  hairline-soft: "#e2e8f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  dark-canvas: "#0d1117"
  dark-surface: "#16213e"
  dark-card: "#1a1a2e"
  gold: "#b59f3b"
  gold-soft: "#c9a96e"
  purple: "#8b5cf6"
  red: "#e74c3c"
  green-correct: "#6aaa64"
  green-present: "#b59f3b"
  green-absent: "#3a3a3c"
  blue-link: "#58a6ff"
  success: "#117700"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    padding: 12px 24px
    height: 44px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-dark:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-gold:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  text-input-error:
    border: "1px solid {colors.red}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline}"
  top-nav-dark:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.dark-surface}"
  nav-link-active:
    textColor: "{colors.primary}"
    border-bottom: "2px solid {colors.primary}"
  nav-link-dark-active:
    textColor: "{colors.primary}"
    border-bottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0, 0, 0, 0.08)"
    border: "1px solid {colors.hairline}"
  product-card-dark:
    backgroundColor: "{colors.dark-card}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.dark-surface}"
  category-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  category-badge-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  category-badge-gold:
    backgroundColor: "{colors.gold-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  difficulty-badge-easy:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  difficulty-badge-medium:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  difficulty-badge-hard:
    backgroundColor: "{colors.red}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  footer:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  puzzle-grid:
    gap: "{spacing.base}"
    padding: "{spacing.lg}"
  puzzle-cell:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: "1px solid {colors.hairline-soft}"
  puzzle-cell-correct:
    backgroundColor: "{colors.green-correct}"
    textColor: "{colors.on-primary}"
  puzzle-cell-present:
    backgroundColor: "{colors.green-present}"
    textColor: "{colors.ink}"
  puzzle-cell-absent:
    backgroundColor: "{colors.green-absent}"
    textColor: "{colors.on-primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Play Now", "Start Puzzle", and "Subscribe" actions. Rendered in `#6aaa64` green with white text and 8px rounded corners. On hover, shifts to `#5a9654`; disabled state uses `#a0d49c`. Height is 44px with 12px vertical and 24px horizontal padding. The `button-secondary` variant uses a white background with a `#d7dadc` border and `#1a1a2e` text, ideal for "Cancel" or "Back" actions. `button-ghost` has no background or border, used for text-only actions like "Learn More" in content areas. `button-dark` uses the `#16213e` dark surface background for use on light canvases. `button-gold` uses `#b59f3b` for premium or featured actions.

### Navigation
**`top-nav`** — A 64px fixed-height bar with white background and a `#d7dadc` bottom border. Nav links use `{typography.nav-link}` at 15px weight 500. Active state underlines with a 2px `#6aaa64` green border. The dark variant (`top-nav-dark`) uses `#0d1117` background with white text and a `#16213e` border, used on puzzle pages and archive sections. Mobile collapses to a hamburger menu with a slide-out drawer.

### Cards
**`product-card`** — Used for puzzle thumbnails in grid views. White background, 12px rounded corners, 16px padding, and a `#e2e8f0` border. On hover, gains a subtle `0 4px 12px rgba(0, 0, 0, 0.08)` shadow and the border shifts to `#d7dadc`. The dark variant (`product-card-dark`) uses `#1a1a2e` background for dark mode sections. Cards contain a thumbnail image, title, category badge, and difficulty indicator.

### Badges
**`category-badge`** — Pill-shaped tags for puzzle categories (Crosswords, Word Search, Sudoku). Default state is light gray (`#f7f7f7`) with `#718096` text. Active state fills with `#6aaa64` green and white text. Gold variant (`category-badge-gold`) uses `#c9a96e` for premium or featured categories. **`difficulty-badge`** — Small rectangular badges (4px rounded) indicating puzzle difficulty: easy (`#6aaa64`), medium (`#b59f3b`), hard (`#e74c3c`). Uses `{typography.badge}` (11px uppercase bold).

### Forms
**`text-input`** — Standard input field with 44px height, 8px rounded corners, and a `#d7dadc` border. Focus state swaps to a 2px `#6aaa64` border with no outline. Error state uses `#e74c3c` red border. **`search-bar`** — A wider 48px input with 12px rounded corners and 16px horizontal padding, used for the main puzzle search. Focus state mirrors the text-input pattern.

### Footer
**`footer`** — Full-width dark section on `#0d1117` background with `#a0aec0` text. Links use `{typography.link}` at 14px weight 500. Hover state shifts link color to `#6aaa64`. Padding uses `{spacing.section}` (64px) vertical and `{spacing.lg}` (24px) horizontal. Contains columns for puzzle categories, about links, and social icons.

### Hero
**`hero-section`** — Full-width banner on `#16213e` dark surface with white text. Title uses `{typography.display-xl}` (32px bold) and subtitle uses `{typography.body-md}` (16px regular) in `#a0aec0`. Used on the homepage and category landing pages. Includes a search bar and primary CTA button.

### Puzzle Grid
**`puzzle-grid`** — A responsive grid with `{spacing.base}` (16px) gap and `{spacing.lg}` (24px) padding. **`puzzle-cell`** — Individual cells within the grid, used for Wordle-style letter reveals. Three states: correct (`#6aaa64` green), present (`#b59f3b` gold), absent (`#3a3a3c` dark gray). White background default with `{rounded.sm}` (8px) corners.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column puzzle grid, hamburger nav, stacked hero layout, reduced padding (16px), smaller display text (24px) |
| Tablet | 744–1128px | Two-column puzzle grid, expanded nav links, hero with side-by-side content, 24px padding |
| Desktop | 1128–1440px | Three-column puzzle grid, full top-nav with all links visible, hero with search bar centered, 32px padding |
| Wide | > 1440px | Four-column puzzle grid, max-width container at 1440px, hero content centered with 64px padding |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have 48px tap targets on mobile (padding increased)
- Search bar height is 48px for comfortable touch input
- Puzzle cells are minimum 48px × 48px on mobile
- Category badges have 32px minimum tap targets

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with slide-out drawer containing all nav links
- Puzzle grid reduces columns from 4 to 1 on mobile
- Footer columns stack vertically below 744px
- Hero section stacks content vertically below 744px (title, subtitle, search, CTA)
- Category filter strip collapses to horizontal scroll on mobile
- Sidebar content (if present) moves below main content on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components were inferred from common patterns; actual extracted hover colors may differ
- Error state styling (form validation, toast notifications) was not extracted from the live site
- Dark mode toggle behavior and exact dark palette mapping are inferred from extracted dark colors; the brand may not have a formal dark mode
- Animation and transition timings (hover transitions, page loads, puzzle animations) were not captured
- Icon set and illustration style (custom SVG vs. icon library) could not be determined from extracted data
- Sub-brand or seasonal color variations (holiday themes, special puzzle events) are not represented
- The purple `#8b5cf6` and red `#e74c3c` colors are present in extracted data but their specific usage (badges, links, errors) is inferred
- Font stack is system-native; no custom font files or weights were found on the live site
- Spacing scale is inferred from common patterns; actual component spacing may vary
- The extracted color list contains many grays and blues that may be framework defaults; the true brand palette may be smaller than represented
