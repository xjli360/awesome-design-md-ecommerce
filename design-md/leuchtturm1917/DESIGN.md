---
version: alpha
name: "Leuchtturm1917"
source_url: "https://www.leuchtturm1917.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Numbered pages — every folio printed, 1 through 249 — is the small act of German precision that grounds everything else on leuchtturm1917.com. Against that systematic logic, the site strips visual noise completely: the single UI tone reliably extracted is a mid-gray (#757575), set against white canvas and near-black ink, with all chromatic energy deferred to product photography where 25-plus cover colors carry the full brand palette. System typefaces — Arial and Helvetica, unmodified and unembellished — arrive not as a cost-saving shortcut but as typographic infrastructure that disappears in service of content, the digital equivalent of dotted-grid paper. The lighthouse mark (Leuchtturm, lighthouse in German) functions as a compact identity anchor in the header rather than a sprawling mascot; its silhouette prints cleanly at 24px and at invoice-corner scale alike. Navigation is organized by product system — Notebooks, Planners, Accessories — each category a flat text link with no dropdown megamenu, trusting users who arrive knowing exactly which gram-weight cover they want. Product tiles sit in a disciplined column grid, thumbnail images cropped consistently to show binding and spine color. Corners stay mildly squared — a modest {rounded.sm} on cards and {rounded.xs} on inputs — never the soft pillowing of consumer lifestyle brands, never the hard austerity of pure utility. Form inputs and CTAs share the same proportional logic: 48px touch-target height, tight letter-spacing at small sizes, weight stepping between 400 body and 700 display. Color-picker swatches for cover selection are the one UI component where the brand's rainbow identity surfaces directly — circles in {rounded.full}, each selection state signaled by border weight rather than background flood. The result is a design system built for catalog density: grid-faithful, chromatic only where the product demands it, and uninterested in decorative noise.

colors:
  primary: "#757575"
  primary-active: "#4a4a4a"
  primary-disabled: "#b5b5b5"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#757575"
  muted-soft: "#a0a0a0"
  hairline: "#d9d9d9"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  swatch-border-selected: "#1a1a1a"
  swatch-border-default: "#d9d9d9"
  badge-new: "#1a1a1a"
  badge-limited: "#757575"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Helvetica Neue Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  product-price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge-label:
    fontFamily: "'Helvetica Neue Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  swatch-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 24px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 23px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 10px 14px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoWidth: 140px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageRounded: "{rounded.xs}"
    gap: "{spacing.sm}"
    padding: "{spacing.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.product-price}"
    textColor: "{colors.body}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.08)"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    borderDefault: "2px solid {colors.swatch-border-default}"
    borderSelected: "2px solid {colors.swatch-border-selected}"
    borderUnavailable: "1px solid {colors.hairline-soft}"
    gap: "{spacing.xs}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px
  category-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "2px solid transparent"
    borderActive: "2px solid {colors.ink}"
    padding: "{spacing.sm} 0"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  accordion-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    buttonSize: 40px

## Components

### Buttons

**`button-primary`** — 48px tall, zero border radius, uppercase Helvetica Neue Bold at 14px with 0.5px letter-spacing. Background is near-black `{colors.ink}` at rest, stepping to `{colors.primary-active}` on hover. The flush square geometry reads as label-precision — it mirrors the hard corners of a printed notebook cover rather than signaling softness or approachability. Disabled state uses `{colors.primary-disabled}` (light gray) with white text; the contrast intentionally low to communicate inactivity without hiding the element.

**`button-secondary`** — White fill with a 1px `{colors.ink}` border, identical height and typographic treatment to primary. Hover state floods to `{colors.surface-soft}`. Used for secondary CTAs such as "Add to Wishlist" or "View All Colors" placed alongside a dominant primary action. The matched sizing ensures the two buttons form an even-weight binary rather than a clear hierarchy.

**`button-ghost`** — Transparent background, underlined `{colors.body}` text at `{typography.button-sm}`. No border, no hover background — underline removes on hover. Used inside product descriptions and editorial copy for soft in-line navigation without breaking the reading flow with a visible button shape.

### Text Input

**`text-input`** — 48px height, `{rounded.xs}` corners, 1px `{colors.hairline}` border at rest stepping to 1px `{colors.ink}` on focus. Arial 16px weight 400, no floating label. Placeholder collapses on first character. The search variant swaps to `{colors.surface-soft}` background with a leading magnifier icon in `{colors.muted}` and drops the explicit border at rest, relying on background contrast alone.

### Navigation

**`nav-bar`** — 64px tall, white canvas, 1px `{colors.hairline}` bottom border. The wordmark at approximately 140px width anchors the left; right cluster holds search, country selector, and cart count badge. Category links use `{typography.nav-link}` at weight 400; hover steps to weight 600 with no underline or background change — a weight-only state that keeps the bar visually quiet. On scroll past 80px, `box-shadow: 0 2px 8px rgba(0,0,0,0.06)` appears without layout shift, providing depth cue without a color change.

### Product Card

**`product-card`** — White surface, `{rounded.xs}` on both the image and the container. Product image fills card width at a consistent square or 4:3 crop showing the cover, spine, and elastic-band closure. Title renders in `{typography.title-sm}`, price in `{typography.product-price}` at `{colors.body}`. Hover lifts the card with `box-shadow: 0 4px 16px rgba(0,0,0,0.08)` — no translateY, no scale transform — keeping the grid stable and preserving the impression of a catalog laid flat rather than animated merchandise.

### Color Swatches

**`color-swatch`** — 24px diameter circles in `{rounded.full}`, with a 2px border: `{colors.swatch-border-default}` at rest, `{colors.swatch-border-selected}` (near-black) when active. Unavailable cover colors render at 40% opacity with a diagonal CSS line through the circle. Color names appear in `{typography.swatch-label}` beneath the swatch row on hover or selection. The swatch grid is the brand's primary chromatic surface on the product detail page — the one place where the full cover-color system becomes a UI element rather than a background.

### Hero Banner

**`hero-banner`** — `{colors.surface-soft}` or full-bleed product photography background. Title at `{typography.display-xl}` in near-black, body copy at `{typography.body-md}`. Minimum 480px height on desktop. CTA uses the `button-primary` component, left-aligned or centered depending on image composition. On mobile, background image crops to the upper third to preserve subject matter; text block reflows below as a white-canvas section.

### Category Filter

**`category-filter`** — Horizontal tab row at `{typography.title-sm}`. Active tab distinguished solely by `border-bottom: 2px solid {colors.ink}` — no background fill, no color change, no pill shape. Inactive tabs hold `{colors.body}`. The underline-only active state is a precise, minimal signal drawn directly from the grid-ruled-page aesthetic of the product itself. On mobile the row becomes horizontally scrollable with no visible scrollbar and snap-points at each tab.

### Badges

**`badge-new`** and **`badge-limited`** — Hard-cornered (`{rounded.none}`) label chips, 10px uppercase Helvetica Neue Bold at 1px letter-spacing. `badge-new` uses `{colors.badge-new}` (near-black) fill with white text. `badge-limited` uses `{colors.badge-limited}` (mid-gray) fill with white text. Both sit as absolute-positioned overlays on the top-left corner of the product card image. The hard corner is deliberate — soft-rounded badges would dissolve against the notebook cover photography.

### Search Bar

**`search-bar`** — 40px height, `{rounded.xs}`, `{colors.surface-soft}` background. Leading magnifier icon in `{colors.muted}`, placeholder in `{colors.muted}`. Focus state adds `border: 1px solid {colors.ink}`. Inline results appear in a white drop-panel at `{rounded.xs}` with `{colors.hairline}` border; each result row uses `{typography.body-sm}` with the matched substring bolded.

### Footer

**`footer`** — `{colors.ink}` (near-black) background, `{colors.on-dark}` primary text. Links render in `{colors.muted-soft}` stepping to `{colors.canvas}` on hover. Organized in a 4-column grid on desktop: Products, Service, Company, Newsletter. Newsletter input uses a dark-surface variant of the standard `text-input` with an inverted border. Bottom row: country selector, legal links in `{typography.caption}`, all left-aligned.

### Accordion

**`accordion-item`** — Used on product detail pages for Features, Specifications, and Delivery sections. Only a `{colors.hairline}` bottom border separates items — no card chrome. Expand/collapse via a `+` / `−` glyph at right. Body copy in `{typography.body-sm}`. No animation easing — instant open/close matching the precise, no-surplus aesthetic across the system.

### Breadcrumb

**`breadcrumb`** — 12px Arial, `{colors.muted}` for parent crumbs, `{colors.ink}` for the active leaf. Forward-slash separator with single-space padding on each side. Sits 16px below the nav bar and 16px above the page title. No hover underline on parent crumbs — plain text links only.

### Quantity Stepper

**`quantity-stepper`** — Minus button, numeric display, plus button in a horizontal inline group. Each element 40px tall, `{rounded.xs}`, with 1px `{colors.hairline}` border. Typography `{typography.title-md}`. No native spinner arrows on the number cell — the `−` and `+` buttons are the only controls, keeping the component visually consistent and touch-friendly.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger drawer nav replacing horizontal link row, hero image stacks above copy block, color swatch row scrolls horizontally, footer collapses to stacked accordions |
| Tablet | 744–1128px | 2-column product grid, nav retains wordmark and icon cluster but drops text category links to icon-only, hero runs side-by-side layout at reduced padding |
| Desktop | 1128–1440px | 3–4 column product grid, full horizontal nav with category text links visible, hero at full 480px minimum height |
| Wide | > 1440px | Max content width 1440px centered with increased horizontal padding; grid holds at 4 columns, no additional reflow |

### Touch Targets

- All interactive elements minimum 48×48px on mobile viewports
- Color swatches expand to 32px diameter on touch devices with increased `{spacing.sm}` gap between circles
- Category filter tabs gain 12px vertical padding on mobile for comfortable horizontal scroll
- Cart and search icons in the mobile nav bar set to 44px tap zone despite smaller visual icon size
- Quantity stepper buttons remain 40px height; on mobile, full-width layout ensures adequate horizontal span

### Collapsing Strategy

- Desktop horizontal nav → mobile hamburger drawer with nested accordion by category, closing on backdrop tap
- PDP specification rows → accordion sections on mobile, visible labeled grid on desktop
- Footer 4-column layout → stacked independently collapsible accordion panels on mobile
- Category filter tab bar persists as scroll-snap horizontal row at all breakpoints; never wraps to multi-line
- Hero side-by-side layout → stacked image-above-text at mobile, with image cropped to top-third to preserve cover art

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color extracted (#757575); full palette likely injected via JavaScript or blocked by anti-bot — ink, canvas, surface, and hairline tokens are inferred from standard design conventions, not confirmed from the live site
- No meta theme-color present — mobile browser chrome color undetermined
- Font stack is system/web-safe only (Arial, Helvetica, Helvetica Neue Bold); no custom web font confirmed — all typography tokens use the extracted system stack without embellishment
- Notebook cover accent colors (sage, navy, lemon, burgundy, forest, etc.) are not represented as UI design tokens — they exist as product data, not extractable as reliable system-level tokens
- Button hover and active colors, focus ring style, and transition durations not confirmed — derived from accessible conventions
- Precise nav-bar height and responsive breakpoints not extracted — values inferred from typical DTC e-commerce patterns
- Sale or discount pricing color not confirmed — omitted from token set to avoid fabrication
- No dark-mode palette detected or documented
- Primary CTA color may differ from `{colors.ink}` — the actual button fill on the live site could be a specific brand black or a dark navy not captured in the single-color extraction
