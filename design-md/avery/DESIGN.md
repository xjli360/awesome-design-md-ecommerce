---
version: alpha
name: "Avery"
source_url: "https://www.avery.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Avery's color vocabulary was alphabetized before it was digitized — the same flag-blue (#0039a6) that has lived on ring-binder packaging for decades now anchors every major navigation surface, while a single hard red (#ea001c) closes every primary CTA: find → buy, two nodes with no lifestyle detour between them. CircularXXWeb runs the entire type hierarchy across four weights (Book, Medium, Bold, Black), a geometric workhorse that stays legible at the compressed scales a label-product catalog demands; ABCDiatype-Heavy joins the stack only at hero moments, pushing campaign headlines into editorial weight without disturbing the workhorse below. The palette doubles as a functional vocabulary rather than a decorative one: the yellow (#eaaa00) that marks a highlighter SKU on a physical shelf reappears as a UI warning indicator, the green (#07a200) that signals "in stock" is the same green on the highlighter cap, and the red (#ea001c) that closes the CTA loop is the same red on the label dispenser — the interface inherits the shelf's color logic rather than inventing a parallel digital system.

  Surface architecture stays deliberately recessive. Off-white planes (#f1f1f1, #f7f7f7) carry product thumbnail backgrounds so template imagery does the brand-building work uninterrupted; a blue-tinted wash (#f3fcff) marks active selection states with a barely-there gesture, and a whisper-pink (#fdf3f3) surfaces form errors without alarm. Buttons carry the minimum radius that removes sharpness without suggesting softness ({rounded.xs}), a posture that reads: utility tool, not discovery experience. The search bar places a red submit button flush against the input field, visually merging find and buy into a single action unit. Navigation body text settles on a dark charcoal (#383d46) rather than pure black, slightly warming the functional grid. Filter chips break from the squared posture to use {rounded.full} — the one soft gesture in an otherwise rectilinear catalog — signaling interactivity without disturbing the grid. The footer drops into near-black (#1d2124), keeping the product surface luminous above while holding legal and support copy at reduced visual weight.

colors:
  primary: "#ea001c"
  primary-active: "#c5001d"
  primary-hover: "#bd2130"
  primary-disabled: "#fdf3f3"
  secondary: "#0039a6"
  secondary-hover: "#0057b8"
  secondary-active: "#004085"
  accent-sky: "#00b4eb"
  ink: "#242424"
  body: "#383d46"
  muted: "#6d6d6d"
  muted-light: "#8c8c8c"
  hairline: "#b9b9b9"
  hairline-soft: "#dae0e5"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#f1f1f1"
  surface-blue-tint: "#f3fcff"
  surface-red-tint: "#fdf3f3"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"
  status-success: "#07a200"
  status-success-active: "#1e7e34"
  status-warning: "#eaaa00"
  status-warning-active: "#d39e00"
  status-error: "#ea001c"
  mid-gray: "#53565a"
  dark-charcoal: "#1d2124"

typography:
  hero-display:
    fontFamily: "'ABCDiatype-Heavy', 'CircularXXWeb-Black', sans-serif"
    fontSize: 56px
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-xl:
    fontFamily: "'CircularXXWeb-Black', sans-serif"
    fontSize: 40px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'CircularXXWeb-Black', sans-serif"
    fontSize: 28px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'CircularXXWeb-Bold', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'CircularXXWeb-Bold', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'CircularXXWeb-Medium', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'CircularXXWeb-Book', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'CircularXXWeb-Book', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'CircularXXWeb-Book', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'CircularXXWeb-Bold', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'CircularXXWeb-Medium', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0
  nav-link:
    fontFamily: "'CircularXXWeb-Medium', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge-label:
    fontFamily: "'CircularXXWeb-Bold', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 10px
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-light}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.secondary-hover}"
    textColor: "{colors.on-secondary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.secondary}"
    borderColor: "{colors.secondary}"
    borderWidth: 1.5px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-ghost-hover:
    backgroundColor: "{colors.surface-blue-tint}"
    textColor: "{colors.secondary-active}"
    borderColor: "{colors.secondary-active}"
  button-sm-utility:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 34px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    borderColor: "{colors.secondary}"
    outlineColor: "{colors.surface-blue-tint}"
    outlineWidth: 2px
  text-input-error:
    borderColor: "{colors.status-error}"
    backgroundColor: "{colors.surface-red-tint}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 48px
    iconColor: "{colors.muted}"
    submitButtonBackgroundColor: "{colors.primary}"
    submitButtonTextColor: "{colors.on-primary}"
    submitButtonRounded: "{rounded.xs}"
  search-bar-focus:
    borderColor: "{colors.secondary}"
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottomColor: "{colors.hairline-soft}"
    borderBottomWidth: 1px
    logoAccentColor: "{colors.primary}"
  nav-bar-link-active:
    textColor: "{colors.primary}"
    borderBottomColor: "{colors.primary}"
    borderBottomWidth: 2px
  nav-bar-link-hover:
    textColor: "{colors.secondary}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.canvas}"
    paddingVertical: "{spacing.sm}"
    paddingHorizontal: "{spacing.base}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline-soft}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    imageBackgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.base}"
  product-card-hover:
    borderColor: "{colors.secondary}"
    boxShadow: "0 2px 8px rgba(0,57,166,0.12)"
  template-card:
    backgroundColor: "{colors.canvas}"
    previewBackgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline-soft}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    labelTypography: "{typography.body-sm}"
    metaTypography: "{typography.caption}"
    padding: "{spacing.md}"
  template-card-hover:
    borderColor: "{colors.secondary}"
    boxShadow: "0 2px 8px rgba(0,57,166,0.10)"
  template-card-selected:
    outlineColor: "{colors.primary}"
    outlineWidth: 2px
  hero-section:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    headingTypography: "{typography.hero-display}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
  hero-section-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
  category-badge:
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  category-badge-red:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  category-badge-blue:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
  category-badge-green:
    backgroundColor: "{colors.status-success}"
    textColor: "{colors.canvas}"
  category-badge-yellow:
    backgroundColor: "{colors.status-warning}"
    textColor: "{colors.ink}"
  category-badge-gray:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.mid-gray}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  filter-chip-active:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    borderColor: "{colors.secondary}"
  filter-chip-hover:
    borderColor: "{colors.secondary}"
    textColor: "{colors.secondary}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
  section-header:
    headingTypography: "{typography.display-md}"
    subheadingTypography: "{typography.body-md}"
    headingColor: "{colors.ink}"
    subheadingColor: "{colors.muted}"
    paddingBottom: "{spacing.lg}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    buttonColor: "{colors.secondary}"
    height: 40px
  status-toast-success:
    backgroundColor: "{colors.status-success}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  status-toast-error:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.dark-charcoal}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTopColor: "{colors.mid-gray}"
    borderTopWidth: 1px
    paddingVertical: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — The red (#ea001c) CTA button is the single highest-contrast element on any page surface, carrying the Avery brand voltage directly into the action moment. Corner radius stays at {rounded.xs} (4px), keeping utility posture without hard industrial edges. Hover deepens to #bd2130, active collapses further to #c5001d; disabled state drops to the whisper-pink surface (#fdf3f3) with muted text, preserving layout without suggesting interactivity.

**`button-secondary`** — Deep flag-blue (#0039a6) background with white text, matching primary in height (44px) and radius but signaling a secondary action tier. Hover lifts to #0057b8; used for "Add to Cart" alternatives, account actions, and template-save flows where the purchase signal belongs to a different red CTA above.

**`button-ghost`** — Transparent fill with a 1.5px #0039a6 border, reserving secondary real estate without adding visual weight. Hover fills the surface-blue-tint (#f3fcff) background to confirm interactivity. Common in filter panels and inline form actions.

**`button-sm-utility`** — Light gray (#f1f1f1) background at 34px height for subsidiary actions: quantity adjustments, copy-link, share. Sits below the primary/secondary hierarchy and does not use brand color; typography drops to {typography.button-sm}.

### Search Bar

**`search-bar`** — A 48px full-width input with a flush-right red (#ea001c) submit button at {rounded.xs}. The red submit marker visually merges search into the purchase funnel — the same color that fires every buy CTA fires the find action. On focus, the border transitions to the secondary blue (#0039a6) with a light blue-tint outline to confirm keyboard navigation without displacing the red submit.

### Navigation

**`nav-bar`** — White canvas (#ffffff) with 64px height and a hairline bottom border (#dae0e5). Logo mark renders in primary red (#ea001c). Navigation links use CircularXXWeb-Medium at 14px in dark charcoal (#383d46); active links take a 2px red underline at {rounded.none} — no pill or box treatment. The functional catalog structure (Labels, Stickers, Office Products, etc.) maps directly to top-level nav items without decorative grouping.

**`promo-banner`** — A full-width red (#ea001c) strip sitting above the nav, running {typography.body-sm} promotional copy in white. Links inside use canvas white (#ffffff) underlined. Dismissible on mobile; persistent on desktop.

### Product & Template Cards

**`product-card`** — White canvas card at {rounded.sm} with a 1px hairline-soft border (#dae0e5). Product thumbnail sits on a light gray (#f7f7f7) image plane so white-label packaging reads cleanly. Title renders at {typography.title-sm}, price at {typography.title-md} with the secondary blue (#0039a6) for pricing emphasis on sale items. Hover state intensifies the border to secondary blue with a subtle shadow.

**`template-card`** — Narrower than a product card, optimized for grid display of Avery label templates. Preview thumbnail on #f7f7f7; label text at {typography.body-sm}; meta (size, count, SKU) at {typography.caption} in muted gray. Selected state applies a 2px red (#ea001c) outline directly on the card border — no overlay or checkbox; the selection state mirrors the physical "pick this template" action.

### Category Badges

**`category-badge-*`** — Five color variants (red, blue, green, yellow, gray) at {rounded.full} with uppercase {typography.badge-label} at 11px. The color variants are not arbitrary: red = Avery brand/new, blue = best-seller/featured, green = in-stock/available, yellow = on-sale/highlighted, gray = informational. The color-badge system mirrors the physical label category color-coding so users familiar with Avery shelving recognize the conventions immediately.

### Filter Chips

**`filter-chip`** — Pill-shaped ({rounded.full}) interactive filter elements; the only {rounded.full} component in the catalog grid, marking the filter rail as an interactive zone distinct from the squared product grid. Default state: white fill with hairline border; active state flips to secondary blue (#0039a6) fill with white text; hover adds a blue border without fill.

### Hero

**`hero-section`** — Navy blue (#0039a6) full-bleed section carrying ABCDiatype-Heavy at 56px for campaign copy. The dark blue backdrop isolates the hero from the white catalog below with a hard color break rather than a gradient. The primary CTA button ({colors.primary} red) gains additional visual voltage against the blue field. A light variant (`hero-section-light`) uses #f7f7f7 background for secondary promotional rows.

### Status & Feedback

**`status-toast-success`** — Green (#07a200) toast with white text at {typography.body-sm} and {rounded.xs}. Used for "Item added to cart," "Template saved," and order confirmation micro-moments.

**`status-toast-error`** — Primary red (#ea001c) toast. Since the primary CTA is also red, error toasts are differentiated by position (top of viewport) and icon rather than color alone.

### Footer

**`footer`** — Near-black (#1d2124) background with a mid-gray top border (#53565a) creating a recessive base layer below the product canvas. Column headings at {typography.title-sm} in #f7f7f7; link body at {typography.body-sm} in #b9b9b9 hairline; hover lifts links to canvas white (#ffffff). Keeps legal and support copy visually subordinate without hiding it.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with slide-in drawer; search bar expands full-width above fold; promo banner wraps to two lines; filter chips scroll horizontally in a single row; hero section drops to display-md at 28px |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level items, secondary items move to a "More" dropdown; search bar remains prominent; filter rail collapses to a modal sheet triggered by a filter button |
| Desktop | 1128–1440px | Three- to four-column product grid; full horizontal nav with all primary categories visible; filter rail persists as left sidebar on category pages; hero section at full 56px hero-display |
| Wide | > 1440px | Grid constrains to 1440px max-width with auto side margins; hero content centers at 960px max; no additional columns added beyond four |

### Touch Targets

- All interactive elements maintain minimum 44px height on mobile (buttons, input fields, filter chips)
- Filter chips on mobile expand padding to 10px 18px to meet touch target requirements
- Nav drawer links height minimum 48px with {spacing.base} horizontal padding
- Quantity stepper buttons minimum 40×40px with explicit hit-area expansion via padding

### Collapsing Strategy

- Primary nav: full horizontal → hamburger drawer at < 744px; drawer slides from left, overlay scrim at 50% opacity
- Filter rail: left sidebar (desktop) → horizontal chip scroll (tablet) → bottom-sheet modal (mobile)
- Hero section: full bleed with left-aligned copy (desktop) → centered stacked copy (mobile) at reduced typography scale
- Product grid: 4-col → 3-col (desktop breakpoint) → 2-col (tablet) → 1-col (mobile)
- Promo banner: single line (desktop) → wraps (mobile); dismissible on all breakpoints via ×close icon

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- True canvas white (#ffffff) is not present in the extracted palette; assumed as page base from industry convention and site rendering
- Exact button border-radius not confirmed from CSS extraction; {rounded.xs} (4px) inferred from visual inspection pattern for utility-catalog brands
- Icon and illustration system not captured — Avery uses product-category icons in nav but style (outline/filled/illustrated) is unconfirmed
- Exact font-size scale for the design editor / Avery Design & Print tool (a separate embedded app) not captured; the component system above covers marketing/catalog surfaces only
- Monospace font stack (Consolas, Courier New, Menlo) appears in extracted fonts but use context is unclear — possibly code/SKU display in print templates
- Animation and transition timing values not extractable from static extraction
- Dark-mode support not confirmed; no `prefers-color-scheme` signals detected
- Print stylesheet conventions (Avery's core use case involves print-accurate rendering) not captured in this design system
- Exact grid column count and gutter widths not confirmed; 8px base grid assumed from spacing scale
