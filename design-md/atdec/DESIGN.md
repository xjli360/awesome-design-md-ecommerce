---
version: alpha
name: "Atdec"
source_url: "https://atdec.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The burnt-orange pair — #d85030 and #db4f30, separated by barely a perceptual step — functions as Atdec's precision mark: not a lifestyle accent but an engineering callout, the visual equivalent of a red-dot indicator on a torque specification. Mounted against the near-white #f5f5f6 field and anchored by deep-navy #221155, these flame-adjacent tones communicate that the brand's products are built to bear load and hold position. Gotham and GothamBook carry the typographic architecture: geometric, squared at the joints, constructed with the same logic as aluminum extrusion — efficient rather than expressive, suited to a procurement audience that scans spec sheets rather than browsing by mood.

  The palette respects the product category without sentimentalizing it. An #e0e0e0 hairline evokes brushed-metal surface quality; #f5f5f6 reads as clean-room white rather than warm ivory. Interactive blue #0a7cff and its softer companion #4593ed handle link states and secondary actions, borrowing from browser-native conventions — a pragmatic choice for a site where engineers and facilities managers navigate to load-rating tables without friction. Warm mid-tone #e17a61 sits between the primary and its disabled state, softening transitions in a context where abruptness would feel unfinished rather than bold.

  Component geometry is straight-edged by conviction. Buttons use a shallow `{rounded.sm}` — the industrial register demands it. Category pills are the single departure: `{rounded.full}` filter chips that function as toggles rather than actions, where the pill shape aids visual distinction from CTA affordances. Product cards carry `{rounded.sm}` corners just sufficient to lift them from the grid without suggesting consumer softness. Data tables and spec-badge components are first-class UI citizens here, treated with the same care as marketing CTAs, because the purchase decision hinges on a kilogram rating or a VESA compatibility check.

  Spacing is generous at section scale and compressed at the component level. Product grids pack efficiently for procurement scanning across many SKUs in one session; hero sections breathe to foreground high-resolution product photography against the #221155 navy. Material Icons Outlined supplies the utility icon language — consistent stroke weight that reads naturally alongside Gotham's skeletal geometry. The system is aimed at the person specifying a broadcast-studio installation or a trading-floor rollout, not styling a personal desk.

colors:
  primary: "#d85030"
  primary-active: "#b83820"
  primary-hover: "#c44428"
  primary-disabled: "#f0c4b8"
  brand-navy: "#221155"
  accent-blue: "#0a7cff"
  accent-blue-soft: "#4593ed"
  warm-mid: "#e17a61"
  ink: "#221155"
  body: "#3d3d3d"
  muted: "#767676"
  hairline: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-navy: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Gotham', 'GothamBook', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Gotham', 'GothamBook', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'Gotham', 'GothamBook', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'GothamBook-medium', 'GothamBook', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'GothamBook', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'GothamBook', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'GothamBook', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Gotham', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Gotham', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
  nav-link:
    fontFamily: "'Gotham', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'GothamBook', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  label-caps:
    fontFamily: "'Gotham', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
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
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-navy:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    placeholderColor: "{colors.muted}"
    focusBorder: "1px solid {colors.accent-blue}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    height: 44px
    iconColor: "{colors.muted}"
    focusBorder: "1px solid {colors.accent-blue}"
    padding: 10px 14px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    accentColor: "{colors.primary}"
    activeIndicator: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.body-sm}"
    hoverBorderColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-navy}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.title-md}"
    minHeight: 480px
    paddingV: "{spacing.section}"
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
    gap: "{spacing.xs}"
  data-table:
    headerBackground: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.label-caps}"
    cellTextColor: "{colors.body}"
    cellTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    stripeBackground: "{colors.surface-soft}"
    cellPadding: "{spacing.sm} {spacing.base}"
  alert-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-navy}"
    linkColor: "{colors.accent-blue-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    padding: "{spacing.xxl} 0"

---

## Components

### Buttons

**`button-primary`** — Filled #d85030 at 44px height with Gotham 600 15px label in white. Hover lifts to #c44428, active drops to #b83820; disabled drains to the pale #f0c4b8 blush, all sharing `{rounded.sm}` at 4px — the shallowest radius compatible with a clickable affordance. The warmth of the orange against any background, including the navy hero, provides sufficient contrast without needing outline or shadow scaffolding.

**`button-secondary`** — White fill with a 1px #d85030 border and matching label text, identical height to the primary. Used for parallel actions ("Download Spec Sheet" beside "Add to Cart") where both options deserve visual presence but hierarchy must remain legible. The orange border draws the eye to the pair as a unit while the fill difference declares priority.

**`button-ghost`** — Transparent background with #221155 ink label, no border. Reserved for tertiary actions within content areas — "View All", "Read More", dismissal links — where a bordered or filled element would add visual weight disproportionate to the action's importance.

**`button-navy`** — Solid #221155 fill with white text, deployed on dark-background sections (footer, navy hero) where the primary orange would create uncomfortable simultaneous contrast. Same geometry as the primary.

### Navigation

**`nav-bar`** — White canvas, 64px tall, 1px #e0e0e0 bottom border. Wordmark left-aligned; primary product categories (Desk Mounts, Wall Mounts, Ceiling Mounts, Floor Stands, Accessories) centered in Gotham 600 14px; search and account icons right-aligned in #767676 muted. Active category marked by a 2px #d85030 bottom underline rather than a filled chip — the brand uses color as a line, consistent with its preference for linear emphasis over fill. Dropdowns open against the #f5f5f6 surface with 1px #e0e0e0 borders.

### Product Card

**`product-card`** — White surface with 1px #e0e0e0 border and `{rounded.sm}` corners, promoting to a 1px #d85030 border on hover to signal selection readiness. Image zone uses #f5f5f6 fill to neutralize shadows on product photography. Title renders in GothamBook-medium 18px; meta text (load rating, VESA range) in GothamBook 14px #767676 muted. Spec badges stack below the title in a flex-wrap row, each using the `spec-badge` pattern. No price display on category pages — this is a B2B catalog routed to resellers.

### Hero Section

**`hero-section`** — Deep #221155 navy canvas, minimum 480px, white type. Heading in Gotham 700 48px; subhead in GothamBook-medium 18px. The #d85030 primary button CTA sits cleanly against the navy — warmth pops against the cool dark without additional scaffolding. Section padding is `{spacing.section}` vertical. Desktop layout splits: text and CTA left, product image right; mobile stacks image above, text below.

### Spec Badges

**`spec-badge`** — Compact information chips for attributes such as "75 kg Load Capacity", "VESA 75×75–400×200", or "IP54 Rated". Uses #f5f5f6 surface, 1px #e0e0e0 border, `{rounded.xs}` corners, and `spec-label` typography at 11px/500. Appears on product cards and product detail pages as a fast-scan summary row. Non-interactive: display only, no hover or press state required.

### Category Pills

**`category-pill`** — Rounded filter controls for product browsing and filtering. Inactive: #f5f5f6 background, #3d3d3d body text, 1px hairline border. Active: #d85030 fill, white text, 1px #d85030 border. The `{rounded.full}` shape is the one departure from the brand's rectilinear language — justified because pill filters function as persistent toggles, not momentary actions, and the shape difference from rectangular buttons prevents mode confusion.

### Data Table

**`data-table`** — Specification and compatibility tables are primary content, not secondary documentation. Header row: #f5f5f6 background, `label-caps` typography (Gotham 700, 11px, uppercase, 1px letter-spacing). Data rows: GothamBook 14px body, #f5f5f6 alternating stripe, 1px #e0e0e0 borders throughout. Cell padding is `{spacing.sm}` vertical, `{spacing.base}` horizontal. On mobile, tables scroll horizontally with the first column (attribute label) sticky.

### Search Bar

**`search-bar`** — Single-line input, 44px height, 1px #e0e0e0 border, `{rounded.sm}`. A Material Icons Outlined search glyph sits left-inset at #767676. Focus promotes the border to 1px #0a7cff accent-blue — consistent with browser-native expectations for a B2B audience accustomed to enterprise UI conventions. Autocomplete suggestions drop against a white surface with 1px #e0e0e0 outline and `{rounded.sm}` corners.

### Alert Banner

**`alert-banner`** — Full-width #d85030 strip for promotional messages, shipping notices, or stock alerts. White `body-sm` text, `{spacing.sm}` vertical padding. Because it deploys the primary brand color at full saturation across the entire viewport width, it should appear at most once per page load for content with genuine urgency — overuse depletes the orange's CTA authority across the rest of the page.

### Footer

**`footer`** — Deep #221155 background, white body text, #4593ed soft-blue links. Four-column grid on desktop: product categories, support resources, company, and region/language. Column headings use `label-caps` typography to create hierarchy within a low-contrast zone. Legal text and copyright in GothamBook 12px caption. Collapses to accordion stack on mobile.

### Breadcrumb

**`breadcrumb`** — Horizontal wayfinding trail in GothamBook 12px caption. Inactive steps: #767676 muted. Current page: #221155 ink. Separator chevron: #e0e0e0 hairline. Gap between items: `{spacing.xs}`. Provides essential orientation in a deep catalog hierarchy (e.g., Mounts → Desk Mounts → Single Monitor → AWMS-2B).

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen drawer; hero min-height 320px with stacked layout; data tables scroll horizontally with sticky first column; spec badges wrap to two per row |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories with overflow menu; hero at full 480px with split layout beginning to emerge; side-by-side spec badge rows |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with mega-menu dropdowns; hero at full split layout (text+CTA left, product image right) |
| Wide | > 1440px | Four-column product grid; max-width container centered at 1440px; hero may use full-bleed background image with constrained text column |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Category pills minimum 36px height on mobile, 32px on tablet+
- Nav items in mobile drawer minimum 48px row height for comfortable thumb reach
- Spec badges are display-only and require no touch target
- Table rows minimum 44px height to support row-tap to expand on mobile

### Collapsing Strategy
- Primary nav collapses to hamburger icon at < 744px; all product category links move into a full-screen slide-in drawer with chevron-disclosed subcategories
- Hero split layout stacks vertically on mobile — product image above fold, text and CTA below
- Data tables scroll horizontally on mobile with the attribute-label column pinned sticky left; do not attempt to reflow table columns
- Footer four-column grid collapses to two columns on tablet, then to single accordion-style stack on mobile with each section independently expandable
- Product card spec-badge rows truncate to a maximum of three visible badges on mobile with a "+N more" expand trigger

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand-published design token file or public style guide found; all type sizes, weights, and component dimensions are inferred from the Gotham/GothamBook font stack and B2B industrial catalog conventions
- `primary-active` (#b83820) and `primary-disabled` (#f0c4b8) are derived from the extracted primary orange-red, not confirmed from live CSS inspection
- Body text color (#3d3d3d) is absent from the extracted palette; likely a near-black used at body scale that was not captured as a dominant swatch
- Exact nav height, button padding, card border-radius, and section spacing not confirmed via live DOM inspection — values reflect category norms
- Icon set confirmed as Material Icons Outlined from the extracted font-family stack but per-feature glyph assignments not verified
- Exact Gotham weight mapping (Book vs Book-medium vs Gotham 500 vs Black) not confirmed via live font loading inspection
- No dark-mode, high-contrast, or accessibility-variant tokens detected
- Regional pricing, currency formatting, and locale-specific layout variants (Atdec serves North America) not captured
