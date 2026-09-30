---
version: alpha
name: "Arpin Philately"
source_url: "https://www.arpinphilately.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The #ff6600 orange assigned as the site's meta theme-color sits on Arpin Philately's catalogue like a price sticker on a penny black — the single proprietary decision on a canvas otherwise assembled entirely from Bootstrap 3's utility palette. Every other color on the page is a known quantity: #337ab7 link-blue, #777777 body mist, #eeeeee row dividers. The orange appears only where commerce must interrupt archival browsing — the Add to Cart button, the search submit, the brand name in the dark navbar — and nowhere else. That restraint is not minimalism; it is the discipline of a catalogue database that respects the collector's attention.

  Typography is unambiguous in its priorities. Arial and Helvetica Neue carry lot numbers, condition grades, country classifiers, and catalogue descriptions without editorial weight. No custom typeface, no variable-weight display moment. The monospace stack — Consolas, Courier New — surfaces in lot reference fields, echoing the printed catalogue tradition where alphanumeric codes are treated as data, not copy. Font Awesome 5 and Glyphicons Halflings supply every icon: magnifiers, cart glyphs, sort arrows, chevrons. The interface trusts structure over decoration.

  Alert states adopt Bootstrap's full semantic register — success greens (#3c763d on #dff0d8 with #d6e9c6 border), warning ambers (#8a6d3b on #fcf8e3 with #faebcc border), danger reds (#a94442 on #f2dede with #ebccd1 border), and info blues (#31708f on #d9edf7 with #bce8f1 border) — used for shipping notices, stock flags, and condition warnings rather than marketing moments. The near-black #110011, with its faint violet undertone distinguishing it from a flat #000, anchors the heaviest heading weight and carries something of the archival ink it references.

  Geometry throughout is {rounded.xs} or {rounded.none} — stamps are rectangular, perforations are precise, and catalogue rows are squared-off. There is no pill shape in this interface. The footer and navbar share the same #080808 near-black field, framing the white content area between two dark bands and giving the layout a formal, catalogue-cover composure.

colors:
  primary: "#ff6600"
  primary-active: "#e05500"
  primary-disabled: "#ffb380"
  accent-red: "#ef3340"
  link: "#337ab7"
  link-active: "#286090"
  ink: "#110011"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#9d9d9d"
  hairline: "#eeeeee"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  nav-bg: "#080808"
  success-text: "#3c763d"
  success-bg: "#dff0d8"
  success-border: "#d6e9c6"
  warning-text: "#8a6d3b"
  warning-bg: "#fcf8e3"
  warning-border: "#faebcc"
  error-text: "#a94442"
  error-bg: "#f2dede"
  error-border: "#ebccd1"
  info-text: "#31708f"
  info-bg: "#d9edf7"
  info-border: "#bce8f1"
  danger-btn: "#d9534f"
  dark-green: "#226600"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
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
    lineHeight: 1.375
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
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  lot-number:
    fontFamily: "Consolas, 'Courier New', Courier, monospace"
    fontSize: 12px
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
    height: 34px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
    border: "1px solid {colors.hairline}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.button-md}"
    padding: 0
    border: none
  button-danger:
    backgroundColor: "{colors.danger-btn}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 34px
    focusBorderColor: "{colors.link}"
    focusShadow: "inset 0 1px 1px rgba(0,0,0,0.075), 0 0 8px rgba(51,122,183,0.6)"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 50px
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-dark}"
    borderBottom: none
  nav-bar-brand:
    textColor: "{colors.primary}"
    typography: "{typography.title-md}"
    fontWeight: 700
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    imageAspect: "1/1"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
  stamp-listing-row:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    lotNumberTypography: "{typography.lot-number}"
    lotNumberColor: "{colors.muted}"
    titleTypography: "{typography.body-md}"
    titleColor: "{colors.link}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.ink}"
    hoverBackgroundColor: "{colors.surface-soft}"
  condition-badge:
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
    variants:
      mint:
        backgroundColor: "{colors.success-bg}"
        textColor: "{colors.success-text}"
        borderColor: "{colors.success-border}"
      used:
        backgroundColor: "{colors.warning-bg}"
        textColor: "{colors.warning-text}"
        borderColor: "{colors.warning-border}"
      damaged:
        backgroundColor: "{colors.error-bg}"
        textColor: "{colors.error-text}"
        borderColor: "{colors.error-border}"
  alert:
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    typography: "{typography.body-md}"
    border: "1px solid transparent"
    variants:
      success:
        backgroundColor: "{colors.success-bg}"
        textColor: "{colors.success-text}"
        borderColor: "{colors.success-border}"
      warning:
        backgroundColor: "{colors.warning-bg}"
        textColor: "{colors.warning-text}"
        borderColor: "{colors.warning-border}"
      danger:
        backgroundColor: "{colors.error-bg}"
        textColor: "{colors.error-text}"
        borderColor: "{colors.error-border}"
      info:
        backgroundColor: "{colors.info-bg}"
        textColor: "{colors.info-text}"
        borderColor: "{colors.info-border}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 34px
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitRounded: "{rounded.xs}"
  category-sidebar:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    headerTypography: "{typography.title-sm}"
    headerColor: "{colors.ink}"
    linkTypography: "{typography.body-md}"
    linkColor: "{colors.link}"
    linkHoverColor: "{colors.link-active}"
    activeLinkColor: "{colors.primary}"
    activeLinkFontWeight: 700
    nestedIndent: "{spacing.md}"
  breadcrumb:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 8px 15px
    typography: "{typography.body-sm}"
    separatorColor: "{colors.muted}"
    linkColor: "{colors.link}"
    activeColor: "{colors.muted}"
  catalogue-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTypography: "{typography.title-sm}"
    headerColor: "{colors.body}"
    rowTypography: "{typography.body-md}"
    rowColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    stripeBackgroundColor: "{colors.surface-soft}"
    hoverBackgroundColor: "{colors.hairline}"
  pagination:
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    linkColor: "{colors.link}"
    borderColor: "{colors.hairline}"
    height: 34px
  footer:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-dark}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"

---

## Components

### Buttons

**`button-primary`** — Orange (#ff6600) on a squared {rounded.xs} container at 34px tall, using the plain Arial stack at 14px. Hover shifts to #e05500 ({colors.primary-active}); disabled fades to the washed #ffb380. The orange CTA appears only at decisive moments — Add to Cart, Search submit, Checkout — never as decoration.

**`button-secondary`** — Soft-surface fill with a {colors.hairline} border and {colors.body} text, used for secondary actions like View Details or Save to Wishlist. Identical geometry to primary, distinguished only by fill.

**`button-link`** — Transparent, no padding, {colors.link} blue text at {typography.button-md}. Used for inline filter resets, pagination links, and catalogue row actions where a full button would overload the data-dense layout.

**`button-danger`** — Bootstrap danger red (#d9534f) for destructive actions such as Remove from Cart. Same 34px height and {rounded.xs} geometry as the primary button.

### Forms & Search

**`text-input`** — Standard Bootstrap form control: canvas white, {colors.hairline-soft} border, 34px height, {rounded.xs}. Focus ring is a blue box-shadow keyed to {colors.link}, preserving the Bootstrap interaction idiom across all catalogue filter fields, search, and checkout forms.

**`search-bar`** — Inline input with a flush-right orange submit button ({colors.primary} fill, {colors.on-primary} icon). The Glyphicons magnifier glyph appears inside the submit. Used in both the navbar and dedicated catalogue search pages. Input stretches to fill available width.

### Navigation

**`nav-bar`** — A {colors.nav-bg} (#080808) Bootstrap navbar at 50px tall frames the top of every page. The brand name renders in {colors.primary} orange at 18px bold — the only orange element in the navigation chrome. Nav links sit in {colors.muted-soft} (#9d9d9d), brightening to {colors.on-dark} white on hover. Dropdown menus open on click with a canvas-white panel and hairline border.

**`nav-bar-brand`** — The Arpin wordmark in {colors.primary} against the dark bar is the most visible brand-color placement on any page. No logomark or icon accompanies it; the name alone carries recognition.

### Product Display

**`product-card`** — A {colors.hairline}-bordered card with a 1:1 stamp image at top, title in {typography.title-sm}, price in {typography.price}, and a condition line in {typography.caption} / {colors.muted}. Used in grid views on category landing pages. No drop shadow; border alone defines the card edge.

**`stamp-listing-row`** — The dominant catalogue format. Each row carries a monospace lot number in {typography.lot-number} / {colors.muted}, a title hyperlink in {colors.link}, country and denomination tags in {colors.muted}, and a right-aligned price in {typography.body-md}. Rows alternate with {colors.surface-soft} stripe and brighten on hover to {colors.surface-soft}.

**`condition-badge`** — A small inline label at {typography.caption} in {rounded.xs}, indicating philatelic condition (Mint/NH, Hinged/Used, Damaged/Fault). The badge maps directly to Bootstrap's semantic color triples: success greens for mint, warning ambers for hinged or used, error reds for faulty or damaged material.

**`catalogue-table`** — Full-width table with a {colors.surface-soft} header row at {typography.title-sm}, alternating stripe rows, and {colors.hairline} cell borders. Sortable columns display Glyphicons sort-arrow indicators in the header. The table is the primary format for country or topic collections with many line items.

### Alerts & Feedback

**`alert`** — Bootstrap alert panels in four semantic variants, each using the corresponding text/background/border token triple. Success alerts carry shipping confirmations and successful cart actions; warning alerts flag limited stock or discontinued items; danger alerts surface payment or checkout errors; info alerts deliver shipping policy notices and promotional copy.

### Sidebar & Navigation

**`category-sidebar`** — A filterable category tree in a {colors.surface-soft} box with {colors.hairline} border and {rounded.xs}. Section headers render at {typography.title-sm}; links use {typography.body-md} in {colors.link}, with the active item switching to {colors.primary} orange and bold weight. Nested subcategories indent by {spacing.md}. On mobile the sidebar moves below results or into a collapsible accordion.

**`breadcrumb`** — A Bootstrap breadcrumb strip in {colors.surface-soft} with a hairline border, sitting above catalogue content. Separator is "/" in {colors.muted}; prior crumbs are {colors.link} links; the current page crumb renders in {colors.muted} without underline.

**`pagination`** — Bootstrap pagination strip below catalogue results at 34px height with {rounded.xs}. The active page fills {colors.primary} orange with {colors.on-primary} white text. Inactive page links are {colors.link} blue; borders are {colors.hairline}.

### Footer

**`footer`** — The dark {colors.nav-bg} footer mirrors the navbar, with {colors.muted-soft} body text and links that brighten to {colors.on-dark} on hover. Standard Bootstrap footer layout: copyright line and horizontal links to Shipping, Returns, Contact, and About pages. A {colors.hairline} top border separates the footer from the canvas below the last catalogue section.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Navbar collapses to hamburger toggle; category sidebar shifts below results or into a collapsible accordion; catalogue tables scroll horizontally or reformat as stacked cards; product card grid becomes single-column |
| Tablet | 744–1128px | Two-column product card grid; sidebar collapses to a horizontal filter strip above results; navbar links remain visible in compact form |
| Desktop | 1128–1440px | Full three-column card grid or paginated table with sidebar; Bootstrap 12-column grid at full width; search bar spans half the navbar |
| Wide | > 1440px | Container fixed at 1140px max-width; layout centers with side gutters; no additional structural changes |

### Touch Targets

- Navbar links reach 44px touch height via Bootstrap's navbar padding expansion on mobile
- Pagination links expand to 44px on mobile via responsive CSS
- Add to Cart and primary CTA buttons remain at 34px desktop height; mobile should expand to 44px minimum via responsive overrides
- Category sidebar accordion toggle provides a full-row tap target on mobile

### Collapsing Strategy

- Category tree hidden on mobile; exposed via a "Filter" or "Categories" toggle button above results
- Catalogue table format switches to stacked card rows below 600px to minimize horizontal scroll
- Footer columns stack single-column below 744px
- Dropdown nav menus convert to off-canvas or accordion on mobile

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The confirmed brand primary #ff6600 appears in meta theme-color but not in the extracted top-color list, suggesting it is applied to a small number of elements (CTAs, brand name) rather than broad surfaces — exact coverage unknown
- No custom brand typeface detected; the entire type stack resolves to Arial and Helvetica Neue system fonts; custom @font-face declarations may be absent or served via a CDN path not captured in extraction
- Exact navbar and footer hex confirmed as #080808 from extraction; may be pure #000000 in some contexts
- Logo treatment — whether a graphical mark, wordmark, or combined lockup accompanies the brand name in the navbar — could not be determined from extraction
- The roles of #ef3340 (accent red) and #226600 (dark green) in the brand are unclear; they may mark sale pricing or promotional tags but their specific usage could not be confirmed
- Bootstrap 3 Glyphicons and Font Awesome 5 Brands/Free are both detected; which icon set is used for which component contexts is not determinable from extraction alone
- No animation, transition duration, or easing values were extractable
- Product photography style, stamp image aspect ratios, and watermark treatment are unknown
- Mobile breakpoint behavior is inferred from Bootstrap 3 defaults; custom responsive overrides may differ
