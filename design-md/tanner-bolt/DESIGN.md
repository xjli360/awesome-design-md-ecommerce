---
version: alpha
name: "Tanner Bolt"
source_url: "https://www.tannerbolt.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Thousands of SKUs — grade-5 hex bolts, nylon insert lock nuts, threaded rod sold by the foot — demand a catalog UI that earns trust before the buyer even reads the spec. Tanner Bolt's design language leans into industrial utility: a deep charcoal ink (#1c2126) paired with a high-visibility safety orange primary (#e05c1a) that echoes the color conventions of hardware jobsite signage and fastener packaging. The surface reads white and clean, never clinical, because buyers arrive with a part number in hand and need to confirm spec, finish, and quantity with minimal friction. Navigation is dense and hierarchical — product categories branch deep — so typographic hierarchy does heavy lifting: a condensed-weight display scale for section headers, a readable mid-weight body for spec tables, and a small caption tier for dimension callouts and tolerance notes. Corner radii stay minimal, {rounded.xs} on inputs and cards, {rounded.none} on data tables, signaling that this is a tool, not a lifestyle brand. Buttons are flat-rectangle rather than pill-shaped, keeping the chrome subdued so product photography and specification grids get full visual priority. The muted warm gray surfaces ({colors.surface-soft}) differentiate spec-detail panels from the main canvas without introducing decorative color. Orange appears only at primary CTAs — "Add to Cart," "Request Quote," quantity selectors — making its appearance a reliable signal of action rather than decoration. Footer carries part-certification badges and bulk-discount callouts in small-caps caption type, the way a printed distributor catalog would. NOTE: All hex values and font choices below are inferred from category conventions; the live site returned a 405 error and yielded zero extracted tokens. Treat this palette as a plausible starting point pending a live extraction pass.

colors:
  primary: "#e05c1a"
  primary-active: "#b84a12"
  primary-disabled: "#f0b898"
  ink: "#1c2126"
  body: "#2e363e"
  muted: "#5a6470"
  hairline: "#d0d5da"
  hairline-soft: "#e8eaec"
  canvas: "#ffffff"
  surface-soft: "#f5f4f2"
  surface-card: "#ffffff"
  surface-strong: "#edecea"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  safety-orange: "#e05c1a"
  steel-blue: "#2a4f72"
  steel-blue-muted: "#4a7299"
  success: "#2d7d45"
  warning: "#c98a00"
  error: "#b92c2c"
  table-row-alt: "#f9f8f6"
  badge-new: "#e05c1a"
  badge-stock: "#2d7d45"

typography:
  display-xl:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  spec-label:
    fontFamily: "'Roboto Mono', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  small-caps-label:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.25px
  part-number:
    fontFamily: "'Roboto Mono', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px

rounded:
  none: 0px
  xs: 3px
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
    padding: 10px 20px
    height: 42px
    border: none
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
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 42px
    border: "1.5px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    rounded: "{rounded.xs}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.steel-blue}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  button-quote:
    backgroundColor: "{colors.steel-blue}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 42px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    padding: 8px 12px
    height: 40px
  quantity-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    width: 64px
    height: 40px
    textAlign: center
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    searchButtonBg: "{colors.primary}"
    searchButtonColor: "{colors.on-primary}"
    searchButtonRounded: "{rounded.none}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
    logoTextColor: "{colors.on-dark}"
    borderBottom: none
  nav-top-utility:
    backgroundColor: "#111518"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    height: 32px
  nav-category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 40px
    borderBottom: "1px solid {colors.hairline}"
    activeIndicator: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    partNumberStyle: "{typography.part-number}"
    nameStyle: "{typography.title-sm}"
    priceStyle: "{typography.price-display}"
    priceColor: "{colors.primary}"
    ctaStyle: "{typography.button-sm}"
    imageBg: "{colors.surface-strong}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBg: "{colors.surface-strong}"
    headerColor: "{colors.ink}"
    headerTypography: "{typography.small-caps-label}"
    rowColor: "{colors.body}"
    rowTypography: "{typography.spec-label}"
    altRowBg: "{colors.table-row-alt}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
  badge-in-stock:
    backgroundColor: "{colors.badge-stock}"
    textColor: "{colors.on-dark}"
    typography: "{typography.small-caps-label}"
    rounded: "{rounded.xs}"
    padding: 2px 7px
  badge-low-stock:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.on-dark}"
    typography: "{typography.small-caps-label}"
    rounded: "{rounded.xs}"
    padding: 2px 7px
  badge-out-of-stock:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-dark}"
    typography: "{typography.small-caps-label}"
    rounded: "{rounded.xs}"
    padding: 2px 7px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaBg: "{colors.primary}"
    ctaColor: "{colors.on-primary}"
    ctaRounded: "{rounded.xs}"
    minHeight: 320px
    padding: "{spacing.section} {spacing.xl}"
  category-tile:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    hoverLabelColor: "{colors.primary}"
    iconColor: "{colors.steel-blue}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.body}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    height: 36px
    width: 36px
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    headerTypography: "{typography.small-caps-label}"
    headerColor: "{colors.muted}"
    itemTypography: "{typography.body-sm}"
    itemColor: "{colors.body}"
    checkmarkColor: "{colors.primary}"
    borderRight: "1px solid {colors.hairline-soft}"
    width: 240px
  quote-form-panel:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    headlineTypography: "{typography.title-md}"
    headlineColor: "{colors.ink}"
    ctaBg: "{colors.steel-blue}"
    ctaColor: "{colors.on-dark}"
    ctaRounded: "{rounded.xs}"
  footer:
    backgroundColor: "#111518"
    textColor: "{colors.muted}"
    headingTypography: "{typography.small-caps-label}"
    headingColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.primary}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Flat-rectangle orange (#e05c1a) CTA, 42px tall with 3px radius, carrying `{typography.button-md}` in white. Active state darkens to `{colors.primary-active}` without elevation change; the brand avoids drop-shadow on action elements, keeping UI chrome flat. Used exclusively for "Add to Cart," "Buy Now," and primary confirmation actions so the orange read is never diluted by decoration.

**`button-secondary`** — White fill with a 1.5px `{colors.hairline}` border, same proportions as primary. Carries "Request Quote," "Save for Later," and secondary navigation triggers. On hover, the border firms to `{colors.ink}` to signal interactivity without color conflict with the orange primary.

**`button-quote`** — Steel blue (#2a4f72) fill for the Request-a-Quote action, visually distinct from primary e-commerce orange. Signals a different transaction mode — negotiated bulk pricing versus immediate purchase — using color rather than copy alone.

**`button-tertiary-text`** — Underlined steel-blue text link at `{typography.button-sm}` weight, no border or fill. Used inside spec-detail panels and confirmation dialogs for low-priority navigations ("See full specs," "View similar parts").

### Search

**`search-bar`** — Full-width on mobile, ~480px capped on desktop, with a flush-attached orange search button at the right edge (`{rounded.none}` where they meet). Placeholder reads in `{colors.muted}`. Because buyers arrive with part numbers, the input should accept both free text and exact SKU strings, and `{typography.spec-label}` monospace activates when the input matches a part-number pattern.

### Navigation

**`nav-bar`** — Charcoal (#1c2126) top bar, 56px, holding logo left, search center, and account/cart icons right in white. Below it, a 32px utility strip in near-black (#111518) carries phone number, account links, and shipping threshold copy in `{typography.caption}`. The two-tier nav reserves color contrast for product content below rather than spending it on chrome.

**`nav-category-strip`** — Warm light-gray strip beneath the main nav listing top-level category tabs (Bolts, Nuts, Washers, Screws, Anchors, Threaded Rod…). Active tab gets a 2px bottom rule in `{colors.primary}`. Overflow categories collapse into a "More ▾" dropdown on viewports under 1128px.

### Product Card

**`product-card`** — Minimal bordered card (`1px {colors.hairline}`) on a white surface, 3px radius. Image zone is `{colors.surface-strong}` with the fastener centered on white. Part number renders in `{typography.part-number}` monospace above the product name. Price displays large in `{typography.price-display}` orange. Stock badge (green/amber/red) sits top-right of image. "Add to Cart" button is full-width at card bottom.

### Spec Table

**`spec-table`** — Zero-radius data table with alternating row fills (`{colors.table-row-alt}` / white). Column headers in `{typography.small-caps-label}` on `{colors.surface-strong}` background. Cell values in `{typography.spec-label}` monospace so dimension columns (diameter, thread pitch, length) align cleanly at decimal points. No rounded corners; the table reads as engineering document, not marketing card.

### Badges

Stock availability uses a three-state badge system — `badge-in-stock` (green), `badge-low-stock` (amber), `badge-out-of-stock` (red) — all in `{typography.small-caps-label}` with 2px vertical / 7px horizontal padding at `{rounded.xs}`. Badge color is the primary information signal; copy ("In Stock," "Low Stock," "Call for Availability") is secondary.

### Hero Banner

**`hero-banner`** — Full-width dark band on `{colors.ink}`, minimum 320px tall. Headline in `{typography.display-xl}` white, sub-copy in `{typography.body-md}` muted white (~80% opacity). A single orange CTA button at `{rounded.xs}` anchors the call to action. No gradient overlays; the dark solid reads as industrial rather than editorial.

### Category Tiles

**`category-tile`** — Square or near-square cards on `{colors.surface-strong}` with a simple steel-blue icon above the category name in `{typography.title-sm}`. Border highlights to `{colors.primary}` on hover, label shifts to orange simultaneously, creating a paired hover signal that requires no additional UI state indicator.

### Quote Form Panel

**`quote-form-panel`** — Aside panel (right column on PDP desktop layout, full-width drawer on mobile) in `{colors.surface-soft}` with 8px radius. Carries quantity input, finish/grade selectors, and the steel-blue "Request Quote" CTA. Separated from the primary Add-to-Cart path by color (steel blue vs. orange) and surface (tinted vs. white) without needing a visual divider line.

### Footer

**`footer`** — Near-black (#111518) with a 3px `{colors.primary}` top border as the only brand-color accent. Column headers in `{typography.small-caps-label}` white; links in `{typography.body-sm}` muted gray, turning orange on hover. Bottom row carries certification logos (ISO, ASTM), payment icons, and legal copy in `{typography.caption}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; search bar full-width below logo; nav-category-strip becomes horizontal scroll; filter sidebar converts to sheet drawer; product cards stack 1-up; spec table gains horizontal scroll wrapper; hero banner reduces to 240px min-height |
| Tablet | 744–1128px | 2-column product grid; filter sidebar collapses to top filter-chip row; nav category strip shows 5 tabs with "More ▾" overflow; hero banner 280px min-height; quote panel drops below product images |
| Desktop | 1128–1440px | 3-column product grid; filter sidebar fixed at 240px left; full nav-category-strip visible; PDP uses 60/40 split (images left, details+quote panel right); spec tables unconstrained |
| Wide | > 1440px | Max content width 1400px centered; 4-column grid on catalog pages; hero banner expands to 400px with side-by-side layout; footer columns spread to 5 |

### Touch Targets

- All buttons minimum 44×44px; quantity stepper +/− buttons 40×40px with generous tap zone
- Filter checkboxes expand touch area to 40px height per row via padding
- Mobile nav items minimum 48px tall
- Breadcrumb links spaced at least 8px apart vertically on mobile

### Collapsing Strategy

- Category navigation collapses depth-first: sub-sub-categories fold into the parent drawer before top-level tabs collapse
- Filter sidebar converts to a bottom sheet on mobile, opened by a persistent "Filter & Sort" button above the product grid
- Spec tables scroll horizontally inside a clipped container rather than stacking rows; a gradient fade-right indicates overflow
- Quote form panel stacks below product images on tablet and mobile; on desktop it occupies the right column of the PDP

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All hex colors are estimated** — the live site returned HTTP 405 (Method Not Allowed) and zero color tokens were extracted; the palette above reflects industrial-distributor category conventions, not confirmed brand values
- **Font stack unconfirmed** — no font-family declarations were captured; Roboto Condensed + Roboto are plausible but unverified; custom or licensed typefaces are possible
- **Logo treatment unknown** — whether the wordmark is typeset or a custom lockup is unconfirmed; logo color on dark backgrounds is assumed white
- **Primary brand color unverified** — safety orange (#e05c1a) is inferred from industrial category norms; the actual brand accent may be a different hue (corporate blue, red, yellow)
- **Spacing and radius tokens** — all radius and spacing values are category-default assumptions; Tanner Bolt may use tighter or looser spacing scaled to its catalog density
- **Component states** — hover, focus-ring, and loading states are inferred from accessible-component best practices, not observed from the live UI
- **Dark mode** — unknown whether a dark mode or high-contrast mode is offered
- **Icon system** — glyph style (outline, filled, duotone) and icon library are unknown
