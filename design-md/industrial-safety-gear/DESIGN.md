---
version: alpha
name: "Industrial Safety Gear"
source_url: "https://www.industrialsafetygear.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Bootstrap 3's complete contextual-color vocabulary — success green #3c763d, warning amber #8a6d3b, danger red #a94442, info teal #5bc0de — maps precisely onto OSHA hazard-level logic at Industrial Safety Gear, a PPE distributor operating since 2002. The alignment is not accidental: a site selling hard hats, respirators, and fall-arrest harnesses genuinely needs a visual language where color carries regulatory meaning, and Bootstrap's semantic palette delivers that out of the box. Every alert banner, badge, and contextual button shade corresponds to a safety classification the customer already knows from the job site. The result is a utility-first interface running on Arial and Helvetica Neue at 14px body copy — no custom typefaces, no editorial photography art direction, no brand hero moments. The canvas is white with light-gray surface wells (#f5f5f5, #eeeeee) that segment category browsing, and the primary CTA blue (#337ab7) sits at the top of a three-stop hover ramp that darkens toward #204d74 at active state. Rounded corners across the site hold at `{rounded.xs}` — 4px on inputs, buttons, and cards — the minimum that softens a rect without suggesting consumer warmth. Text hierarchy is compressed: display headings sit at 24–30px, body at 14px, and captions at 12px, all in weight 400–700 with no italic or variable-font variation detected. The wide gray palette (#9d9d9d, #777777, #555555, #080808) runs from disabled states through body copy to near-black ink with no warm deviation. The palette's closest thing to a brand signature is the simultaneous presence of all four Bootstrap alert states at full saturation — a color system designed for industrial triage rather than retail desirability. Spacing is tight and grid-disciplined, consistent with a catalog-browsing experience where product density and scannable specification tables outrank visual breathing room.

colors:
  primary: "#337ab7"
  primary-hover: "#286090"
  primary-active: "#204d74"
  primary-disabled: "#d9edf7"
  primary-border: "#2e6da4"
  ink: "#080808"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#9d9d9d"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  hairline-mid: "#e7e7e7"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#eeeeee"
  surface-light: "#ececec"
  on-primary: "#ffffff"
  success-text: "#3c763d"
  success-bg: "#dff0d8"
  success-dark: "#2b542c"
  success-btn: "#5cb85c"
  success-btn-hover: "#449d44"
  success-btn-active: "#398439"
  warning-text: "#8a6d3b"
  warning-bg: "#fcf8e3"
  warning-dark: "#66512c"
  warning-btn: "#f0ad4e"
  danger-text: "#a94442"
  danger-bg: "#f2dede"
  danger-dark: "#843534"
  danger-btn: "#d9534f"
  info-btn: "#5bc0de"
  info-bg: "#d9edf7"
  disabled-bg: "#e6e6e6"
  disabled-text: "#9d9d9d"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  button-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  code:
    fontFamily: "Consolas, 'Courier New', Menlo, Monaco, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  price:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.xs}"
    padding: 6px 12px
    border: "1px solid {colors.primary-border}"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary-active}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-mid}"
  button-lg:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    border: "1px solid {colors.primary-border}"
  button-success:
    backgroundColor: "{colors.success-btn}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    border: "1px solid {colors.success-dark}"
  button-success-hover:
    backgroundColor: "{colors.success-btn-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-warning:
    backgroundColor: "{colors.warning-btn}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    border: "1px solid {colors.warning-dark}"
  button-danger:
    backgroundColor: "{colors.danger-btn}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    border: "1px solid {colors.danger-dark}"
  button-info:
    backgroundColor: "{colors.info-btn}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  button-disabled:
    backgroundColor: "{colors.disabled-bg}"
    textColor: "{colors.disabled-text}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    cursor: not-allowed
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    border: "1px solid {colors.hairline}"
    height: 34px
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "inset 0 1px 1px rgba(0,0,0,0.075), 0 0 8px rgba(51,122,183,0.6)"
  nav-bar:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline-mid}"
    height: 50px
    padding: 0 {spacing.base}
  nav-bar-brand:
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    paddingY: "{spacing.md}"
  nav-link-hover:
    backgroundColor: "{colors.disabled-bg}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  nav-link-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-sku:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  alert-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: "1px solid {colors.success-btn-active}"
  alert-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: "1px solid {colors.warning-dark}"
  alert-danger:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: "1px solid {colors.danger-dark}"
  alert-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: "1px solid {colors.primary-disabled}"
  badge-default:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  badge-success:
    backgroundColor: "{colors.success-text}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  badge-warning:
    backgroundColor: "{colors.warning-btn}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  badge-danger:
    backgroundColor: "{colors.danger-text}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 34px
    padding: 6px 12px
  search-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none} {rounded.xs} {rounded.xs} {rounded.none}"
    padding: 6px 12px
    height: 34px
  breadcrumb:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    separatorColor: "{colors.muted-soft}"
  breadcrumb-active:
    textColor: "{colors.body}"
  breadcrumb-link:
    textColor: "{colors.primary}"
  pagination-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    padding: 6px 12px
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary-border}"
  pagination-disabled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.disabled-text}"
  panel:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
  panel-heading:
    backgroundColor: "{colors.surface-soft}"
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: 10px 16px
    borderBottom: "1px solid {colors.hairline}"
    rounded: "{rounded.xs} {rounded.xs} {rounded.none} {rounded.none}"
  hero-banner:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderBottom: "1px solid {colors.hairline-mid}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subtext:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.sm}"
  table-striped-row-odd:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
  table-striped-row-even:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
  table-header:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    padding: 8px
    borderBottom: "2px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
    borderTop: "1px solid {colors.hairline-mid}"
  footer-link:
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.caption-bold}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.sm}"

## Components

### Buttons

**`button-primary`** — Standard Bootstrap-style primary button using #337ab7 fill with white text and a 1px #2e6da4 border, at 4px radius. Hover shifts background to #286090, active to #204d74, maintaining the same border-radius throughout. Disabled state uses #e6e6e6 background with #9d9d9d text and `cursor: not-allowed`.

**`button-secondary`** — White background with #555555 text and a #e5e5e5 border, mirroring Bootstrap's default button. Hover lightens to #ececec background. Used for cancel, back-navigation, and secondary catalog actions.

**`button-success` / `button-warning` / `button-danger` / `button-info`** — Four contextual button variants keyed to OSHA safety-level semantics. Success (#5cb85c) marks compliant or in-stock states; warning (#f0ad4e) flags conditional or limited availability; danger (#d9534f) signals hazardous-material products or required safety training; info (#5bc0de) surfaces regulatory guidance links. Each carries a darker-toned 1px border for definition against white surfaces.

**`button-lg`** — Enlarged 18px variant of the primary button at 10px vertical padding, used for primary checkout and bulk-order submission CTAs.

### Alerts

**`alert-success` / `alert-warning` / `alert-danger` / `alert-info`** — The four Bootstrap 3 contextual alert components are load-bearing UI at ISG: success green (#dff0d8 / #3c763d) confirms order placement and safety-certification status; warning amber (#fcf8e3 / #8a6d3b) surfaces low-stock, regulatory notice, or hazmat shipping flags; danger red (#f2dede / #a94442) marks backordered or discontinued items and required safety acknowledgments; info blue (#d9edf7 / #337ab7) delivers shipping policy and compliance notices. All use 4px radius and 1px contextual border, 16px internal padding.

### Navigation

**`nav-bar`** — 50px horizontal bar in #ececec with a 1px #e7e7e7 bottom border. Brand name at left in 18px bold Arial. Navigation links are 14px weight-400 with hover background #e6e6e6 and active state #eeeeee. No mega-menu; category depth is handled by a left-sidebar panel tree on interior pages.

### Product Card

**`product-card`** — White card with 1px #e5e5e5 border and 4px radius. Product image sits at top full-width; title renders in 16px bold #337ab7 (functions as a link); SKU/part number in 12px #777777 below title; price in 18px bold #080808; an "Add to Cart" `button-primary` at card bottom. Cards are arranged in a Bootstrap 3 grid (col-sm-6 / col-md-4 / col-lg-3 pattern).

### Search

**`search-bar` + `search-button`** — An input-group pattern: 34px-tall text input with 1px #e5e5e5 border and 4px left-radius, adjoined to a flush `button-primary` with square left edge and 4px right-radius. Focus state adds Bootstrap's blue box-shadow glow (rgba 51,122,183 at 0.6 opacity). Keyword and part-number search are the primary navigation mode for this SKU-dense catalog.

### Panels

**`panel`** — White box with 1px #e5e5e5 border and 4px radius. Panel heading is #f5f5f5 with 1px bottom border, 16px bold heading text, and 10px vertical / 16px horizontal padding. Used for category sidebars, product specifications, and account management sections.

### Tables

**`table-striped-row-odd` / `table-striped-row-even`** — Alternating #f5f5f5 and #ffffff rows at 14px body text, 8px cell padding. Headers use #ececec background with 12px uppercase bold labels and a 2px bottom border. Spec tables for PPE ratings, ANSI class levels, and arc-flash ratings are the primary data medium on product detail pages.

### Breadcrumb

**`breadcrumb`** — Light #f5f5f5 strip with 8px/16px padding and 4px radius. Links render in #337ab7, active (current page) segment in #555555. Separator is a muted #9d9d9d slash. Breadcrumbs are persistent on category and product pages given catalog depth.

### Badges / Labels

**`badge-default` / `badge-success` / `badge-warning` / `badge-danger`** — Pill-shaped `{rounded.full}` labels at 11px uppercase bold. Default gray (#777777) for general tags; success green (#3c763d) for "In Stock" or "ANSI Certified"; warning amber (#f0ad4e) for "Limited Stock" or "Ships Separately"; danger red (#a94442) for "Hazmat" or "Special Order".

### Footer

**`footer`** — #ececec background with 1px #e7e7e7 top border. Three-to-four column Bootstrap grid of links at 13px / #337ab7, with section headings in 12px uppercase bold #555555. Copyright line in 12px #777777. No social icons detected; links cover categories, policies, and contact.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger collapses nav-bar; search bar full-width; sidebar filters hidden behind toggle button; table horizontal scroll |
| Tablet | 744–1128px | Two-column product grid (col-sm-6); nav links truncate or wrap; sidebar filters visible in collapsed accordion |
| Desktop | 1128–1440px | Three-to-four column product grid; left sidebar filter panel always visible; nav-bar full horizontal; panel grids at full Bootstrap 12-col |
| Wide | > 1440px | Centered max-width container (~1170px Bootstrap container); side margins expand; no additional layout changes |

### Touch Targets

- All buttons respect Bootstrap 3's 34px default height minimum; `button-lg` reaches 46px
- Pagination items padded to 38px+ tap height on mobile
- Nav links padded to 44px minimum tap height in collapsed mobile menu
- Checkbox and radio inputs in filter sidebar target 20×20px minimum

### Collapsing Strategy

- Left-sidebar category/filter panel collapses to a top-bar toggle button on mobile with slide-down drawer
- Primary nav collapses to hamburger icon revealing a stacked link list at full viewport width
- Product specification tables overflow-x with scroll rather than reflow, preserving tabular data integrity
- Multi-column panel grids stack single-column below 576px breakpoint
- Search bar and button group collapse to full-width stacked layout on smallest breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected — site uses system Arial/Helvetica stack throughout; no web font loading observed
- No meta theme-color set; brand primary was inferred from dominant Bootstrap primary blue (#337ab7)
- Info alert text color (#31708f) not present in extracted hex list; Bootstrap 3 default assumed
- Logo treatment and brand lockup colors not extractable from CSS alone; logo may be an image asset
- No custom icon font metrics beyond fontello family name detected; glyph set and sizing unknown
- Hero/banner imagery not inspectable from color extraction; product photography style undetermined
- Hover and focus transition timing (duration/easing) not captured in extracted tokens
- Mobile breakpoints assumed from Bootstrap 3 defaults (576px, 768px, 992px, 1200px); site may override
- No dark mode or high-contrast mode variants detected
- Cart, checkout, and account UI components not extractable without authenticated session
