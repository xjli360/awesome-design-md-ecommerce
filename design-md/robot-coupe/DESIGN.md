---
version: alpha
name: "Robot Coupe"
source_url: "https://www.robot-coupe.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Green runs through Robot Coupe's digital presence the way it marks every physical machine housing — #5aa039 anchors navigation highlights, CTA buttons, and category badges with the directness of a power switch on stainless steel. The site reads like a technical catalogue given just enough digital polish: product imagery dominates on white canvas, specifications live in tightly gridded tables, and the color story stays restrained to that single institutional green against warm grays (#707070 for body copy, #717171 for secondary labels). There is no gradient play, no lifestyle-brand softness — corners stay sharp or barely eased (`{rounded.xs}` on cards, `{rounded.sm}` on buttons), communicating the precision engineering of a brand that invented the commercial food processor in 1963. Typography loads via JavaScript and likely resolves to a geometric sans in the Helvetica/Arial lineage, set at moderate weights; display headers read bold but never decorative, reinforcing the equipment-manual clarity that professional chefs expect. Product cards present a machine photograph, a model name in `{typography.title-md}`, and a single green "Discover" button — no star ratings, no lifestyle copy, no promotional noise. The navigation groups products by professional application (vegetable preparation, cutter mixers, blenders) rather than by marketing campaign, and a country-selector dropdown reflects the 100+ market reach. Spacing is generous at section level (`{spacing.section}`) but compressed within data-dense spec blocks (`{spacing.sm}` gutters), letting information breathe without wasting the screen real-estate a procurement officer needs to compare models. The overall impression is an engineering company that respects its users' time — functional, credible, green.

colors:
  primary: "#5aa039"
  primary-active: "#4a8730"
  primary-disabled: "#b5d4a6"
  ink: "#333333"
  body: "#707070"
  muted: "#717171"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#2b2b2b"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-steel: "#4a4a4a"
  footer-bg: "#333333"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  spec-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0
  spec-value:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0
  uppercase-tag:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    padding: 12px 24px
    height: 44px
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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.muted}"
  button-discover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-mobile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
    imageAspect: "4:3"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    overlay: "linear-gradient(to right, rgba(0,0,0,0.6), transparent)"
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    imageAspect: "16:9"
  category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.spec-value}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-table-row-alt:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.spec-value}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.ink}"
  country-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "10px 16px"
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    textDecoration: "none"
    textDecorationHover: "underline"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "10px 16px 10px 40px"
    height: 44px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    iconColor: "{colors.muted}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"

---

## Components

### Buttons

**`button-primary`** — Solid green (#5aa039) background with white text, used for all primary actions ("Discover", "Contact us", "Download PDF"). Corners at `{rounded.xs}` keep the industrial sharpness. Hover darkens to `{colors.primary-active}`; disabled state fades to `{colors.primary-disabled}` with reduced contrast. Height locks at 44px across all viewports.

**`button-secondary`** — White fill with a 1px `{colors.hairline}` border and dark text. Used for secondary actions like "Compare models" or "Back to list". Hover fills background to `{colors.surface-soft}` and strengthens the border. Same 44px height as primary for inline pairing.

**`button-discover`** — A larger variant (48px, `{rounded.sm}`) reserved for product-card CTAs and hero-banner actions. The extra padding (14px 32px) gives the label room to breathe against product photography.

### Navigation

**`nav-bar`** — 72px white bar with a subtle bottom hairline. Logo sits left, product-category links span the center in `{typography.nav-link}`, and a country-selector plus search icon anchor right. The green primary appears only as an underline indicator on the active category. On mobile, the bar compresses to 56px with a hamburger menu.

**`breadcrumb`** — Muted gray text at `{typography.caption}` scale with "/" separators. The final node renders in `{colors.ink}` to indicate current location within the product hierarchy.

### Product Display

**`product-card`** — White card with a thin `{colors.hairline-soft}` border, holding a 4:3 product photograph, model name in `{typography.title-md}`, and a brief descriptor in `{typography.body-sm}`. On hover, the border shifts to `{colors.primary}` and a subtle box-shadow lifts the card. The `button-discover` sits at the card's base.

**`category-card`** — Used on the homepage and category landing pages to group product families (e.g., "Vegetable Preparation Machines", "Cutter Mixers"). A 16:9 image area with a green `category-badge` overlay label, followed by a title and short description. Background uses `{colors.surface-soft}` to distinguish from the white canvas.

### Specification Tables

**`spec-table-row`** / **`spec-table-row-alt`** — Alternating white and `{colors.surface-soft}` rows create a zebra pattern for scanning dense specification data (bowl capacity, motor speed, weight, dimensions). Labels render in `{typography.spec-label}` (bold, 13px) while values use `{typography.spec-value}` (regular weight). Row padding is tight at `{spacing.sm}` vertical to pack information efficiently.

### Hero & Landing

**`hero-banner`** — Full-width dark section (min-height 480px) with a gradient overlay from opaque black (left) to transparent (right), letting the product photography show through while keeping white display text legible. Used on the homepage and major category pages. CTA is the `button-discover` variant in green.

### Footer

**`footer`** — Dark charcoal background (`{colors.footer-bg}`) with white body text. Organized in columns: product categories, company info, social links, and legal. Links use no underline by default, gaining one on hover. Generous `{spacing.section}` top/bottom padding separates it from content.

### Search

**`search-bar`** — White input with a magnifying-glass icon inset left (colored `{colors.muted}`). On focus, the border transitions to `{colors.primary}`. Used in the nav for product/model search and on documentation pages for filtering technical resources.

### Country Selector

**`country-selector`** — Dropdown-style component appearing in the nav and on the welcome splash page. Displays a flag icon and country name in `{typography.body-sm}`, with a `{rounded.xs}` border. The dropdown panel lists 100+ markets grouped by continent.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero banner stacks text above image; spec tables scroll horizontally; `button-discover` goes full-width |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only; hero retains overlay layout at reduced height (360px) |
| Desktop | 1128–1440px | Three-column product grid; full nav with all category links visible; spec tables display inline; hero at 480px |
| Wide | > 1440px | Content max-width 1440px centered; four-column grid on category pages; increased section padding |

### Touch Targets

- All interactive elements maintain 44px minimum touch height on mobile
- Product cards receive full-surface tap area, not just the button
- Nav hamburger icon uses a 48×48 tap zone with `{spacing.md}` padding
- Country-selector dropdown rows are 48px tall for thumb navigation

### Collapsing Strategy

- Navigation: full horizontal links → hamburger slide-out panel at < 744px
- Product grid: 4-col → 3-col → 2-col → 1-col with preserved card aspect ratios
- Spec tables: fixed layout → horizontally scrollable with sticky first column (label column)
- Hero text: overlay-on-image → stacked above image on mobile, removing the gradient overlay
- Footer columns: 4-across → 2×2 grid → single stacked accordion on mobile

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font families could not be extracted (likely loaded via JavaScript or custom web-font loader); the system stack specified here is an educated approximation based on the brand's geometric sans appearance
- Only three hex colors were captured from static markup (#707070, #717171, #5aa039); additional palette values (hover states, dark-surface tones, error/success semantics) are inferred from brand context rather than extracted
- No CSS custom properties or design-token variables were discoverable in static HTML
- Animation/transition timing values (hover durations, menu slide speed) were not captured
- Exact nav breakpoint and max-content-width values may differ from the 1440px assumed here
- Icon system (SVG sprite vs. inline vs. icon font) could not be determined from extraction
- Form validation states and toast/notification component styles are undocumented
