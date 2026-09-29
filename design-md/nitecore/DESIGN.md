---
version: alpha
name: "Nitecore"
source_url: "https://www.nitecore.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  High-voltage #ffdd00 yellow — the exact shade of a lithium cell's caution stripe — sears out of a near-black #111111 canvas that dominates every viewport. Nitecore sells lumen counts the way performance vehicles sell horsepower; hero banners stack five-digit spec numbers in condensed Teko at display scale, each digit the same electric yellow, daring the viewer to compare. The typographic system runs unusually deep for a hardware manufacturer — Anton drives impact headlines with its compressed black weight, Barlow carries navigation and mid-level section titles in a semi-condensed cut that reads as engineered rather than editorial, Rajdhani lends a blueprint-schematic quality to specification tables, and Inter supplies clean body copy at 400-weight. Four distinct type families, coordinated by condensation and stroke density rather than serifs or decorative faces. Product cards sit on #231f20 dark surfaces with `{rounded.sm}` corners (4px) that keep the geometry tool-sharp; there are no pill shapes, no generous consumer-lifestyle radii anywhere in the system. The palette is deliberately constrained — yellow for every action and attention state, a single #4caf78 green for success and stock confirmations, and a disciplined gradient of neutrals from #0e0e0e through #888888 to #f5f5f5 that builds spatial depth without introducing warmth or color noise. Photography carries the emotion: beam shots slicing through forest darkness, macro details of anodized aluminum knurling, size comparisons against an 18650 cell. The UI stays structural, using generous `{spacing.xl}` column gutters and `{spacing.section}` vertical breaks to let each product hero breathe. Navigation deploys a full-width dark mega-menu organized by use-case verticals — flashlights, headlamps, power solutions, fans — each category anchored by a silhouette product image beneath a `{typography.uppercase-tag}` label. The cumulative effect is closer to an avionics instrument panel than a consumer retail grid: data-dense, hierarchy-precise, and illuminated by a single dominant signal color.

colors:
  primary: "#ffdd00"
  primary-active: "#ffc400"
  primary-disabled: "#6b5c00"
  ink: "#ffffff"
  body: "#e7e7e7"
  muted: "#888888"
  muted-soft: "#6d6e70"
  hairline: "#3a3a3a"
  hairline-soft: "#2a2a2a"
  canvas: "#111111"
  surface-soft: "#1a1a1a"
  surface-card: "#231f20"
  surface-raised: "#323232"
  on-primary: "#111111"
  on-dark: "#ffffff"
  success: "#4caf78"
  spec-highlight: "#ffd400"
  caution-amber: "#ffda09"
  light-canvas: "#f5f5f5"
  light-surface: "#ffffff"
  light-ink: "#231f20"
  light-body: "#595856"
  light-muted: "#8c8c8c"
  light-hairline: "#d0d0d0"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Teko', 'Anton', 'Barlow Condensed', sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Anton', 'Teko', 'Barlow Condensed', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0
  display-md:
    fontFamily: "'Anton', 'Teko', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0
  display-sm:
    fontFamily: "'Barlow', 'Barlow Condensed', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.28px
  title-md:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  spec-value:
    fontFamily: "'Teko', 'Rajdhani', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: 0
  spec-unit:
    fontFamily: "'Rajdhani', 'Barlow', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  micro-label:
    fontFamily: "'Inter', 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  uppercase-tag:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 1.2px
    textTransform: uppercase
  link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.primary}
    padding: 12px 24px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  button-ghost-hover:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.hairline}
    padding: 12px 16px
    height: 44px
  text-input-focus:
    border: 1px solid {colors.primary}
    boxShadow: 0 0 0 1px {colors.primary}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline-soft}
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-soft}"
    boxShadow: 0 2px 8px rgba(0,0,0,0.4)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: 1px solid {colors.hairline-soft}
  product-card-hover:
    border: 1px solid {colors.primary}
    boxShadow: 0 0 0 1px {colors.primary}
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: 1 / 1
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.title-md}"
    textColor: "{colors.primary}"
  product-card-spec:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    minHeight: 560px
    padding: "{spacing.section} 0"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-accent:
    textColor: "{colors.primary}"
  hero-subhead:
    typography: "{typography.display-sm}"
    textColor: "{colors.body}"
  spec-badge:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.primary}"
    typography: "{typography.spec-value}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  spec-badge-unit:
    typography: "{typography.spec-unit}"
    textColor: "{colors.muted}"
  lumen-display:
    typography: "{typography.display-xl}"
    textColor: "{colors.spec-highlight}"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    minHeight: 180px
  category-tile-hover:
    backgroundColor: "{colors.surface-raised}"
    border: 1px solid {colors.hairline}
  category-tile-label:
    typography: "{typography.uppercase-tag}"
    textColor: "{colors.muted}"
  category-tile-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.hairline}
    height: 44px
    padding: 0 16px
  search-bar-focus:
    border: 1px solid {colors.primary}
  search-bar-icon:
    textColor: "{colors.muted}"
    size: 18px
  mega-menu:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.xxl}"
    borderTop: 1px solid {colors.hairline-soft}
  mega-menu-heading:
    typography: "{typography.uppercase-tag}"
    textColor: "{colors.primary}"
  mega-menu-link:
    typography: "{typography.nav-link}"
    textColor: "{colors.body}"
  mega-menu-link-hover:
    textColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
    borderTop: 1px solid {colors.hairline}
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.primary}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-dark}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-stock:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.success}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
  spec-table-header:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    backgroundColor: "{colors.surface-card}"
    padding: "{spacing.sm} {spacing.md}"
  spec-table-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  spec-table-cell:
    padding: "{spacing.sm} {spacing.md}"
    borderBottom: 1px solid {colors.hairline-soft}
  comparison-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
  comparison-card-active:
    border: 2px solid {colors.primary}
  breadcrumb:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  tooltip:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
---

## Components

### Buttons

**`button-primary`** — A #ffdd00 yellow rectangle with #111111 dark text, set in uppercase Barlow 600 at 14px with 0.5px letter-spacing. Corners clip at `{rounded.sm}` (4px), keeping the shape utilitarian. On hover, the background shifts to the deeper #ffc400 (`primary-active`). Disabled state drops to #6b5c00 with #6d6e70 text — still recognizably yellow, but desaturated enough to read as inert. Height locks at 44px with 12px 24px padding.

**`button-secondary`** — Transparent background with a 1px #ffdd00 border, yellow text matching the stroke. On hover, the fill floods to `{colors.primary}` and the text inverts to `{colors.on-primary}`. Same 44px height and `{rounded.sm}` corners as primary. Used for secondary actions on dark backgrounds where a solid yellow would compete with the hero image.

**`button-ghost`** — No border, no fill, white text on dark. Set in `{typography.button-sm}` (12px uppercase Barlow 600). Hover reveals a `{colors.surface-raised}` (#323232) background. Used for tertiary actions, filter toggles, and inline link-like buttons within product spec sections.

### Text Input

**`text-input`** — Dark card surface (#231f20) with a 1px #3a3a3a border and white text. Placeholder text renders in `{colors.muted}` (#888888). On focus, the border and a 1px box-shadow both switch to `{colors.primary}` — a yellow glow ring that signals active input without overwhelming the dark UI. Height matches buttons at 44px for inline pairing in search rows and filter bars.

### Navigation

**`nav-bar`** — A 64px-tall bar on #111111 canvas with the Nitecore wordmark left-aligned (typically rendered as a yellow lockup on dark) and `{typography.nav-link}` text links (Barlow 500, 14px, 0.3px tracking). A subtle 1px `{colors.hairline-soft}` bottom border separates the nav from content. On scroll, the background darkens to `{colors.surface-soft}` with a diffuse shadow (0 2px 8px rgba(0,0,0,0.4)) to lift the bar off the hero. Nav links highlight in `{colors.primary}` on hover.

**`mega-menu`** — Drops below the nav as a full-width panel on `{colors.surface-soft}` (#1a1a1a) with a top hairline border. Section headings use `{typography.uppercase-tag}` in `{colors.primary}` — yellow all-caps at 11px with 1.2px tracking — creating a visual index. Sub-links are `{typography.nav-link}` in `{colors.body}`, shifting to yellow on hover. Product category columns include silhouette product images at 80px square above each group.

### Product Card

**`product-card`** — A `{colors.surface-card}` (#231f20) rectangle with `{rounded.sm}` corners and a 1px `{colors.hairline-soft}` border. The product image sits in a 1:1 aspect-ratio container with a slightly lighter `{colors.surface-soft}` background. Title renders in `{typography.title-sm}` (Barlow 500, 16px), price in `{typography.title-md}` (Barlow 600, 18px) colored `{colors.primary}`. A `{typography.caption}` spec line below the title shows key specs like "1000 lumens | USB-C | IP68" in `{colors.muted}`. On hover, the border and a 1px box-shadow switch to `{colors.primary}`, framing the card in yellow.

### Hero Banner

**`hero-banner`** — Full-width, minimum 560px tall, on the #111111 canvas with `{spacing.section}` vertical padding. The headline uses `{typography.display-xl}` — Teko at 72px, weight 700, line-height 1.0 — typically split so the product name renders in white and the key spec number (lumen count, battery capacity) renders in `{colors.primary}`. A `{typography.display-sm}` subhead in `{colors.body}` (#e7e7e7) sits below at 28px Barlow 600. The product image floats right or center, often shot against a beam-of-light gradient rather than a flat background.

### Spec Badge

**`spec-badge`** — A compact inline block on `{colors.surface-raised}` (#323232) with `{rounded.xs}` corners. The numeric value renders in `{typography.spec-value}` (Teko 600 at 32px) in `{colors.primary}`, with the unit label below in `{typography.spec-unit}` (Rajdhani 500, 14px) in `{colors.muted}`. Used in product detail pages to display key performance figures — lumens, runtime hours, beam distance — in a scannable horizontal row.

**`lumen-display`** — The hero-scale variant of the spec badge. Uses `{typography.display-xl}` at 72px in `{colors.spec-highlight}` (#ffd400). Typically a single large number (e.g., "12000") with no background, floated above or beside the product hero image. The slight color shift from primary #ffdd00 to spec-highlight #ffd400 creates a warm-vs-bright distinction between UI actions and data callouts.

### Category Tile

**`category-tile`** — A 180px minimum-height rectangle on `{colors.surface-card}` with `{rounded.sm}` corners. Each tile contains a centered product silhouette image, a `{typography.uppercase-tag}` label in `{colors.muted}` (e.g., "FLASHLIGHTS"), and a `{typography.title-md}` title in `{colors.ink}`. On hover, the background shifts to `{colors.surface-raised}` and a 1px `{colors.hairline}` border appears. Used on the homepage and mega-menu to organize the product catalog by use-case vertical.

### Search Bar

**`search-bar`** — A 44px-tall input on `{colors.surface-card}` with `{rounded.xs}` corners and a 1px `{colors.hairline}` border. The magnifying-glass icon renders in `{colors.muted}` at 18px. Placeholder text uses `{typography.body-md}` in `{colors.muted}`. On focus, the border shifts to `{colors.primary}` — consistent with the text-input focus treatment. Typically placed in the nav bar or as a persistent element in the mega-menu.

### Badges

**`badge-new`** — A small pill on `{colors.primary}` with `{colors.on-primary}` text in `{typography.micro-label}` (10px, weight 700). Used on product cards and category listings to flag new arrivals. The `{rounded.xs}` corner radius keeps it angular, matching the industrial aesthetic.

**`badge-sale`** — Same dimensions as `badge-new` but on `{colors.success}` (#4caf78) with white text. Used sparingly — Nitecore rarely discounts — for clearance items and bundle deals.

**`badge-stock`** — Inverted: `{colors.surface-raised}` background with `{colors.success}` text. Indicates "In Stock" or "Ships Today" status on product detail pages.

### Spec Table

**`spec-table`** — A structured data table on `{colors.surface-soft}` used on product detail pages. Header cells use `{typography.caption}` in `{colors.muted}` on `{colors.surface-card}` with `{spacing.sm}` by `{spacing.md}` padding. Data cells use `{typography.body-sm}` for text values and `{typography.spec-value}` for numeric performance figures, with 1px `{colors.hairline-soft}` bottom borders between rows.

### Comparison Card

**`comparison-card`** — Used in side-by-side product comparison views. `{colors.surface-card}` background with `{rounded.sm}` corners and a 1px `{colors.hairline}` border. The active/selected card gets a 2px `{colors.primary}` border to highlight the user's current focus. Interior layout stacks product image, name, key spec badges, and price vertically with `{spacing.lg}` padding.

### Footer

**`footer`** — Full-width on `{colors.canvas}` with a 1px `{colors.hairline}` top border. Section headings use `{typography.title-sm}` in `{colors.ink}`. Link columns use `{typography.link}` (Inter 400, 14px) in `{colors.muted}`, shifting to `{colors.primary}` on hover. Vertical padding is `{spacing.section}` (64px). Bottom row contains legal links, region selector, and social icons — all in `{colors.muted}` at caption scale.

### Breadcrumb

**`breadcrumb`** — `{typography.caption-sm}` (11px Inter 400) in `{colors.muted}` with `{colors.hairline}` separator characters. The current/active segment uses `{colors.ink}`. Sits below the nav bar with `{spacing.sm}` vertical margin, providing path context on product detail and category pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + slide-out drawer. Hero headline drops to 36px Teko. Product grid shifts to single-column. Spec badges stack vertically. Mega-menu becomes full-screen overlay. Category tiles become horizontal scroll strip. Footer columns collapse to accordions. |
| Tablet | 744-1128px | Two-column product grid. Hero headline at 48px. Mega-menu opens as a two-column panel. Spec badge row scrolls horizontally if more than 4 items. Nav shows primary links; secondary items move to overflow menu. |
| Desktop | 1128-1440px | Three- or four-column product grid. Full mega-menu with all category columns visible. Hero at full 72px display-xl scale. Comparison view supports up to 3 cards side by side. Spec table renders full-width with all columns. |
| Wide | > 1440px | Content max-width caps at 1440px, centered with `{colors.canvas}` bleed. Product grid may extend to five columns for category pages. Hero images scale proportionally but text sizes remain at desktop values. Side padding increases to `{spacing.xxl}`. |

### Touch Targets
- All interactive elements maintain a minimum 44px touch target on mobile
- Product card tap area covers the entire card surface, not just the title or image
- Spec badges in horizontal scroll rows use `{spacing.sm}` gaps with snap-scrolling
- Hamburger menu icon is 44x44px with a `{spacing.sm}` inset from the screen edge
- Footer accordion toggles use 48px row height for comfortable tapping

### Collapsing Strategy
- Navigation: hamburger drawer below 744px, horizontal links above
- Product grid: 1 col mobile, 2 col tablet, 3-4 col desktop, up to 5 col wide
- Spec badge rows: vertical stack on mobile, horizontal scroll on tablet, inline row on desktop
- Mega-menu: full-screen overlay on mobile, two-column dropdown on tablet, full-width panel on desktop
- Comparison cards: single-card carousel with swipe on mobile, side-by-side on tablet+
- Spec tables: switch to key-value pair list on mobile, full table on tablet+
- Footer: accordion sections on mobile, multi-column grid on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font weights and optical sizes for AstaSans and RobotoFlex could not be determined from extraction — these may serve as fallback or region-specific (CJK) typefaces
- The site uses multiple near-identical yellows (#ffdd00, #ffd400, #ffde00, #ffda09, #ffc400, #fedd02) — it is unclear whether these are intentional contextual variants or rendering artifacts; this spec consolidates them into primary (#ffdd00), primary-active (#ffc400), and spec-highlight (#ffd400)
- Dark/light mode toggling behavior was not observed, but the presence of many light grays (#f0f0f0, #f5f5f5, #f8f8f8) suggests some pages or sections may use a light canvas — the `light-*` color tokens are included speculatively
- Hiragino Sans GB, PingFang SC, and Microsoft YaHei appear in font stacks, likely for CJK locale support; their specific usage contexts are not mapped in this spec
- Animation and transition timings (hover fade durations, mega-menu open speed, product card hover scale) were not extracted
- Icon system details (icon font vs. inline SVG, icon grid size, stroke weight) are unknown
- The exact grid system (column count, gutter width, max-width) could not be confirmed from color/font extraction alone
