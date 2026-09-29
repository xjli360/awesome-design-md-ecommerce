---
version: alpha
name: "Noissue"
source_url: "https://www.noissue.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The background here is not white — it's a warm, faintly toasted cream (#f7f1ec) that reads like unbleached kraft under studio light, a quiet material signal that sustainability is designed into the surface before a single word loads. Against that canvas, a deep indigo-purple (#2c1847) anchors the logo, primary navigation, and editorial headlines with the gravity of a brand that knows exactly where it stands in the market; it's an unusual choice for a packaging company, closer to independent publishing than industrial supply. The hot pink (#ff379c) that fires on every primary CTA and hover state carries an equally unexpected chromatic confidence — the kind of color voltage typically reserved for fashion houses, deployed here on "Start designing" buttons and interactive product controls. Teal greens (#22b38c, #39bd97) function as a distinct semantic layer, appearing on eco-certification marks, progress indicators, and sustainability badges rather than as decorative accent — they do work, not mood. Typography runs PPMori throughout: a geometric sans with just enough humanist warmth to prevent the brand from reading as cold. Display sizes hit 48px at weight 700 with tightly negative tracking (-0.5px), letting the letterforms read large without shouting; body copy at 16px / weight 400 on the warm cream sits at a softer contrast than pure white, easing longer reads on product descriptions and policy pages. Corner radii follow a pill-and-card grammar: buttons and filter chips are fully rounded (`{rounded.full}`), product cards and inputs land at `{rounded.md}`–`{rounded.lg}`, and there is no hard square corner visible in the UI hierarchy. Spacing is generous — `{spacing.section}` above and below marketing blocks, `{spacing.xxl}` between product grid rows — giving each packaging option room to display its print surface properly. The footer inverts to solid `{colors.primary}` indigo, a structural move that closes the page and makes the newsletter signup feel like a distinct commitment rather than a footnote.

colors:
  primary: "#2c1847"
  primary-active: "#1a0e2b"
  primary-disabled: "#c2c2c9"
  accent: "#ff379c"
  accent-active: "#e0007e"
  accent-disabled: "#ffd1e8"
  eco: "#22b38c"
  eco-light: "#39bd97"
  coral: "#fd566f"
  ink: "#111111"
  body: "#4f4f4f"
  muted: "#909090"
  muted-light: "#838383"
  hairline: "#d8d8d8"
  hairline-soft: "#eeeeee"
  canvas: "#f7f1ec"
  surface-soft: "#f5f0e8"
  surface-warm: "#f0f0e8"
  surface-card: "#fcfaf7"
  surface-neutral: "#f7f7f7"
  surface-cool: "#f5f4f6"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  on-eco: "#ffffff"

typography:
  display-xl:
    fontFamily: "'PPMori', 'PPMori Fallback', Helvetica, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'PPMori', 'PPMori Fallback', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'PPMori', 'PPMori Fallback', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'PPMori', 'PPMori Fallback', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'PPMori', 'PPMori Fallback', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'PPMori', 'PPMori Fallback', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'PPMori', 'PPMori Fallback', Helvetica, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'PPMori', 'PPMori Fallback', Helvetica, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'PPMori', 'PPMori Fallback', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'PPMori', 'PPMori Fallback', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'PPMori', 'PPMori Fallback', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  eco-tag:
    fontFamily: "'PPMori', 'PPMori Fallback', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'PPMori', 'PPMori Fallback', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'PPMori', 'PPMori Fallback', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'PPMori', 'PPMori Fallback', Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  mono:
    fontFamily: "Consolas, 'Liberation Mono', Menlo, Monaco, 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
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
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.accent-disabled}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: 1.5px solid
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-eco:
    backgroundColor: "{colors.eco}"
    textColor: "{colors.on-eco}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-sm:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
    border: 1px solid
  text-input-focus:
    borderColor: "{colors.primary}"
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
  text-input-error:
    borderColor: "{colors.coral}"
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-logo:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    overflow: hidden
    padding: "{spacing.base}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.eco}"
    textColor: "{colors.on-eco}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    paddingY: "{spacing.section}"
    layout: split-50/50 on desktop, stacked on mobile
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.primary}"
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 520px
  eco-badge:
    backgroundColor: "{colors.surface-warm}"
    borderColor: "{colors.eco}"
    textColor: "{colors.eco}"
    typography: "{typography.eco-tag}"
    rounded: "{rounded.full}"
    padding: 5px 12px
    border: 1.5px solid
  certification-chip:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    iconColor: "{colors.eco}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: 1px solid
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    height: 44px
    buttonSize: 44px
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    fillColor: "{colors.eco}"
    rounded: "{rounded.full}"
    height: 6px
  tooltip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.primary-disabled}"
    typography: "{typography.body-sm}"
    paddingY: "{spacing.section}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
  footer-newsletter-input:
    backgroundColor: "rgba(255,255,255,0.1)"
    borderColor: "rgba(255,255,255,0.3)"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: 12px 20px

## Components

### Buttons

**`button-primary`** — Hot pink (#ff379c) fill on a fully pill-shaped container (`{rounded.full}`) at 48px tall, 28px horizontal padding. This is noissue's primary action voltage, appearing on "Start designing", "Add to cart", and quote-request flows. Hover transitions to `{colors.accent-active}` (#e0007e) at 150ms ease. Disabled state mutes to `{colors.accent-disabled}` with no opacity reduction on text.

**`button-secondary`** — Outlined pill with 1.5px `{colors.primary}` border and matching text on `{colors.canvas}` fill, identical 48px geometry to primary. On hover the fill inverts to solid `{colors.primary}` and text flips to `{colors.on-primary}` — a clean inversion without any shape change or bounce.

**`button-dark`** — Solid `{colors.primary}` (deep indigo) fill with white text, `{rounded.full}`, 48px. Used as a secondary hero CTA or for sections where the cream canvas makes the pink primary feel redundant.

**`button-eco`** — Teal (`{colors.eco}`) fill with white text, pill-shaped. Reserved exclusively for sustainability-action CTAs: certifications, material choices, or eco-impact pages. Not interchangeable with `button-primary`.

**`button-sm`** — Same hot-pink + `{rounded.full}` grammar as `button-primary` compressed to 36px tall with 20px horizontal padding, used in product card overlays and horizontal filter rows.

### Text Inputs

**`text-input`** — `{rounded.md}` corners on `{colors.surface-card}` fill, 1px `{colors.hairline}` border, 48px tall. Focus ring shifts border color to `{colors.primary}` (indigo). Error state uses `{colors.coral}`. Placeholder in `{colors.muted}`. The surface-card fill (#fcfaf7) is a half-step warmer than the page canvas, creating visual separation without a strong outline.

### Navigation

**`nav-bar`** — 64px tall, `{colors.canvas}` background, anchored by a 1px `{colors.hairline-soft}` bottom border. Logo lockup in `{colors.primary}` indigo. Category links rendered in `{typography.nav-link}` (PPMori 500, 15px, `{colors.ink}`). A `button-primary` pill sits at the far right for "Start designing". On scroll the bar stays pinned; the cream background keeps it legible against product imagery without adding a drop shadow.

### Product Cards

**`product-card`** — `{rounded.lg}` rounded corners on `{colors.surface-card}`, `{spacing.base}` inner padding. Product photography fills the upper portion at a square or 4:3 ratio; below sit product name in `{typography.title-sm}`, starting price range in `{typography.body-sm}/{colors.body}`, and a horizontal row of `certification-chip` components. A `product-card-badge` in `{colors.eco}` marks new or featured items in the upper-left corner. Hover lifts the card with a soft box-shadow; no scale transform.

### Hero Section

**`hero`** — Full-width 50/50 split on desktop: left column holds headline in `{typography.display-xl}/{colors.primary}`, a subhead paragraph in `{typography.body-md}/{colors.body}` (max-width 520px), and a row of CTA buttons (`button-primary` + `button-secondary`) with `{spacing.base}` gap. Right column renders product photography or brand illustration bleeding to the edge. Canvas background throughout with `{spacing.section}` vertical padding. On mobile the image stacks above the text block.

### Eco Badges and Certification

**`eco-badge`** — Pill chip with 1.5px `{colors.eco}` border, `{colors.surface-warm}` fill, and `{colors.eco}` text in `{typography.eco-tag}` (all-caps, 11px). Used inline in category headers and product detail pages to call out certified sustainable materials without requiring an icon.

**`certification-chip`** — `{rounded.sm}` rectangular chip, `{colors.canvas}` fill, `{colors.hairline}` border, body text in `{typography.caption}` with a small eco-green icon left of the label. Multiple chips tile horizontally with `{spacing.sm}` gap; on narrow viewports they wrap to a second row rather than truncating.

### Category Pills

**`category-pill`** / **`category-pill-active`** — Horizontal filter controls for packaging categories (mailers, tissue, boxes, tape, etc.). Inactive: `{colors.surface-soft}` fill, `{colors.primary}` text. Active: solid `{colors.primary}` fill, `{colors.on-primary}` text. Pills sit in a horizontally scrollable row on mobile with `{spacing.sm}` between items and `{spacing.base}` left-padding inset.

### Search

**`search-bar`** — Full-width `{rounded.full}` pill at 48px, `{colors.surface-card}` fill, 1px `{colors.hairline}` border. A magnifying-glass icon in `{colors.muted}` sits 20px from the left edge. Focus shifts border to `{colors.primary}` indigo. Used at the top of product catalog pages above the category pill row.

### Quantity Stepper

**`quantity-stepper`** — 44px tall, `{rounded.sm}` border in `{colors.hairline}`, minus/plus icon buttons flanking a centered count in `{typography.title-sm}`. Minimum order quantities for packaging products are enforced here (e.g., minimum 25 units), with counts displayed as multiples. Insufficient-quantity state shifts border to `{colors.coral}`.

### Progress Bar

**`progress-bar`** — 6px tall `{rounded.full}` track in `{colors.hairline-soft}`, filled left-to-right with `{colors.eco}`. Used in multi-step design-upload and customization flows, and on sustainability impact meters showing recycled material percentages.

### Footer

**`footer`** — Solid `{colors.primary}` (deep indigo) background with `{spacing.section}` top/bottom padding, four-column layout on desktop. Section headings in `{typography.title-sm}/{colors.on-primary}`. Nav links in `{typography.body-sm}` at reduced opacity (#c2c2c9), transitioning to full white on hover. Newsletter row: a translucent `{rounded.full}` input (semi-opaque white border, white placeholder text) with a `button-primary` pill submit button attached right. Certification logos (FSC, B-Corp, etc.) render in white/monochrome at the bottom of the column.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero image stacks above headline; nav collapses to hamburger + logo + cart icon; category pills in horizontally scrollable row; product grid 1-column; footer columns stack vertically; `{typography.display-xl}` drops to `{typography.display-md}` |
| Tablet | 744–1128px | 2-column product grid; hero uses stacked layout with wider text max-width; nav shows top-level links, secondary items in dropdown; footer in 2-column layout |
| Desktop | 1128–1440px | Full 50/50 split hero; 3–4 column product grid; all nav links visible; 4-column footer |
| Wide | > 1440px | Content max-width 1280px centered; `{colors.canvas}` side gutters; hero photography can extend edge-to-edge behind centered text overlay |

### Touch Targets
- `button-primary` and `button-secondary` are 48px tall — above the 44px minimum
- Category pills minimum 36px tall for comfortable thumb tap
- Quantity stepper buttons minimum 44×44px tap area
- Hamburger icon minimum 44×44px touch target
- Product card entire face is the tap target — no small "view" link required
- `eco-badge` and `certification-chip` are display-only on mobile, not interactive

### Collapsing Strategy
- Navigation: full link row at tablet+; hamburger slide-in drawer on mobile with `{colors.primary}` indigo fill
- Hero: image-text split collapses to stacked (image above text) at < 744px; headline scale drops from `{typography.display-xl}` (48px) to `{typography.display-md}` (28px)
- Product grid: 4-col → 3-col → 2-col → 1-col descending through breakpoints
- Category pills: fixed horizontal scroll row on mobile, wrapping row on tablet+
- Footer newsletter: stacked (input then button below) on mobile; inline pill+button on tablet+
- Certification chips: wrap to second row rather than truncate

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- PPMori is a paid custom typeface loaded via `@font-face`; exact available cuts (Regular, SemiBook, Extralight) and weight axis values not confirmed from extraction — weights inferred from PPMori's known offering
- No border-radius values extracted from CSS; all radii derived from visual inspection of pill and card patterns on the live site
- Exact button padding, height, and line-height values not directly extracted — estimated from visual analysis
- Animation timing values (easing curves, durations for hover transitions and drawer open/close) not captured in static color extraction
- No dark mode variant detected; the brand operates in a single warm-light-mode theme
- Several extracted hex values (#33475b, #22b8cf, #0070f3, #f81ce5, #e64980) appear to be third-party embed colors (HubSpot CRM widget, Mantine UI, Next.js error overlay) and were excluded from the palette
- Icon and illustration style (noissue uses custom eco-themed brand illustrations) not described; visual style appears hand-drawn/organic rather than geometric
- Mobile navigation drawer design (background color, animation direction, link sizing) could not be confirmed from static extraction
