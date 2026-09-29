---
version: alpha
name: "Garden Light LED"
source_url: "https://gardenlightled.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The spec-grade navy (#06386b) that anchors Garden Light LED's header reads like a municipal infrastructure catalog before it reads like a shopping site — a deliberate posture for a brand whose primary audience is landscape architects, electrical contractors, and commercial installers who need photometric data first and buy buttons second. DM Serif Display carries all headlines with architectural weight: unhurried, low-contrast strokes that evoke the editorial language of lighting specification journals rather than the urgent CTAs of consumer retail. Lato handles everything operational — navigation, filter labels, spec metadata — in a clean sans that transmits technical precision without becoming cold.

  Color hierarchy is spare and credibility-forward. The deep navy (#06386b) owns headers, primary buttons, and section anchors; a steel teal (#247390) handles secondary interactive elements, hover states, and expandable filter panels. A hard red (#b80e02) appears as a promotional callout or stock-alert signal, used with restraint — it reads closer to an engineering warning flag than a sales badge. The canvas alternates between a warm cream (#f9f5f2) and a near-white (#f7f7f7), giving product photography room to breathe without the clinical flatness of a pure white grid. Supporting grays from near-black (#232325) through mid-tone (#93919b) to soft blue-gray (#abb8c3) carry the full range of text hierarchy, borders, and disabled states. Amber tones (#e09004, #b97600) surface in warm-CCT callouts and photometric spec annotations but are not structural UI color.

  Corners are sharp or near-sharp ({rounded.none} to {rounded.xs}) throughout — a consistent signal that this is specification-grade equipment, not a consumer lifestyle storefront. Navigation is dense and horizontal, carrying product family links, account access, CSI spec sheet downloads, and dealer login at the same visual level, organized for buyers who arrive already knowing which fixture family they need. Search is a thin rectangular field with a navy submit block — precision input, not casual browsing. The footer expands into a full department directory: product families, resources, company, dealer portal — the information architecture of a B2B procurement catalog mapped faithfully onto a web presence.

colors:
  primary: "#06386b"
  primary-active: "#003388"
  primary-disabled: "#abb8c3"
  teal: "#247390"
  teal-active: "#36809a"
  accent: "#b80e02"
  accent-active: "#6b120c"
  amber: "#e09004"
  amber-dark: "#b97600"
  ink: "#232325"
  body: "#4b4b4b"
  muted: "#93919b"
  hairline: "#d8d8d8"
  border-soft: "#abb8c3"
  canvas: "#f9f5f2"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-dark: "#32373c"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'DM Serif Display', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'DM Serif Display', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'DM Serif Display', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link-bold:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  utility-bar:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: 1px solid {colors.primary}
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: 1px solid rgba(255,255,255,0.45)
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 14px
    height: 42px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
    placeholderColor: "{colors.muted}"
  utility-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.utility-bar}"
    height: 36px
    paddingHorizontal: "{spacing.xl}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    paddingHorizontal: "{spacing.xl}"
    logoMaxHeight: 44px
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: 1px solid {colors.hairline}
    boxShadow: "0 4px 12px rgba(6,56,107,0.12)"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 44px
    border: 1px solid {colors.hairline}
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitTypography: "{typography.button-sm}"
    padding: 0 0 0 14px
  hero:
    backgroundColor: "{colors.primary}"
    overlayColor: "rgba(6,56,107,0.72)"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    minHeight: 540px
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: 1px solid {colors.hairline}
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    imageBackgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    metaTypography: "{typography.caption}"
    skuTypography: "{typography.spec-label}"
    skuColor: "{colors.muted}"
    hoverBorder: 1px solid {colors.teal}
  spec-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  new-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-dark}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  filter-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    border: none
  filter-tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    border: 1px solid {colors.hairline}
  filter-tab-hover:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  spec-table:
    backgroundColor: "{colors.surface-card}"
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.body}"
    border: 1px solid {colors.hairline}
    stripedRowColor: "{colors.surface-soft}"
    padding: "{spacing.sm} {spacing.base}"
  download-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: 1px solid {colors.hairline}
    padding: "{spacing.base}"
    iconColor: "{colors.teal}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
  category-section-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.display-sm}"
    borderBottom: 2px solid {colors.primary}
    paddingVertical: "{spacing.lg}"
    paddingHorizontal: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.border-soft}"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.nav-link-bold}"
    headingColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    dividerColor: "{colors.surface-dark}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
  footer-legal:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    height: 48px
    paddingHorizontal: "{spacing.xl}"

## Components

### Buttons

**`button-primary`** — Sharp-cornered ({rounded.none}) navy (#06386b) block in all-caps Lato 700 with 0.6px letter-spacing, giving CTAs the weight and formality of a technical data sheet heading rather than a consumer "Buy Now" label. Hover darkens to #003388; disabled state drains to the blue-gray (#abb8c3). Height is 44px — sized for desktop-professional precision rather than mobile-first thumb ergonomics.

**`button-secondary`** — Transparent fill with a 1px navy border and navy uppercase text. On hover, the fill floods to full navy and text inverts to white — a clean toggle that avoids gradients or shadows. Used for secondary actions like "Download Spec Sheet" alongside a primary "Add to Quote."

**`button-accent`** — Hard red (#b80e02) background with white uppercase Lato text. Reserved for high-urgency calls: promotional deadlines, stock-limit warnings, or featured product callouts in hero banners. Never used for routine navigation.

**`button-ghost`** — Transparent with a 45%-opacity white border and white uppercase text. Lives exclusively over the dark navy hero or footer backgrounds where a filled button would be visually heavy.

### Navigation

**`utility-bar`** — A 36px strip in dark charcoal (#32373c) above the main nav, carrying 12px Lato utility links: dealer login, account, contact, search. Sets a professional two-tier hierarchy before the brand header even renders.

**`nav-bar`** — 64px navy (#06386b) bar with the brand logo left-anchored and product family links in 14px Lato across the center span. No pill shapes; no mega-menu gradients. Dropdowns (`nav-dropdown`) are white rectangular panels with a subtle navy-tinted box shadow, bordered in the hairline gray (#d8d8d8).

**`search-bar`** — A full-width rectangular input with hairline border and a flush navy submit block on the right. No rounding. The Lato placeholder text sits at the {colors.muted} gray (#93919b); on focus the border upgrades to navy (#06386b).

### Product Cards

**`product-card`** — Zero-radius white card bordered in hairline (#d8d8d8) with a 4:3 product image area on a soft (#f7f7f7) background. Below the image: product name in 16px Lato 700, SKU slug in 11px uppercase {spec-label}, and a short description in 14px body-sm. On hover, the border upgrades to teal (#247390) — the only transition effect on the card. No drop shadows.

**`spec-badge`** / **`new-badge`** — Flat rectangular chips, navy for specification callouts ("IP67", "0-10V Dim") and red (#b80e02) for new-product flags. All-caps 11px Lato 700 with 0.8px tracking. Applied as overlays on the product image corner.

### Filters and Tables

**`filter-tab-active`** / **`filter-tab-inactive`** — A tab row with no rounding: active tabs fill solid navy with white uppercase text; inactive tabs sit on the soft gray (#f7f7f7) with a hairline border. Hover previews in teal (#247390). Used above product grids to filter by product family, wattage, CCT, or IP rating.

**`spec-table`** — The brand's most technically dense component. A bordered table with a navy header row in all-caps 11px spec-label and alternating white / soft-gray (#f7f7f7) rows in 14px Lato body-sm. Column headers: lumens, wattage, CCT, CRI, beam angle, IP rating, finish options. No rounding anywhere in the table shell.

**`download-card`** — A soft-gray (#f7f7f7) panel with a teal (#247390) document icon, a file-type label in 11px uppercase spec-label, a document title in 14px body-sm, and a ghost-style "Download PDF" link. Used in a grid in the Resources section for IES files, spec sheets, installation guides.

### Hero

**`hero`** — A full-bleed image or dark navy (#06386b) field with a 72%-opacity navy overlay bringing photographic subjects into the brand palette. Headline in DM Serif Display 48px at 1.12 line-height — architectural but not oversized. Subhead in 16px Lato 400 body-md. One `button-primary` and optionally one `button-ghost` CTA sit at the bottom of the content column. Minimum height 540px on desktop.

### Category Section Header

**`category-section-header`** — A pale (#f7f7f7) band with a 2px navy bottom border and the category name in DM Serif Display 24px, navy text. Functions as a visual chapter-break between product families on long archive pages, using seriffed type where all other section heads would use sans.

### Footer

**`footer`** — Near-black (#232325) background with four or five column groups: Products, Resources, Company, Dealers, Contact. Heading links in 14px Lato 700 white; sub-links in 14px Lato 400 at the blue-gray (#abb8c3). A thin charcoal (#32373c) divider separates the main footer from a `footer-legal` strip in the same charcoal with 12px muted gray legal text and copyright.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Utility bar collapses; nav becomes hamburger drawer in full-screen navy overlay. Hero headline drops to display-sm (24px DM Serif). Product grid shifts to single column. Filter tabs become a horizontal scroll strip. Spec tables gain horizontal scroll wrappers. |
| Tablet | 744–1128px | Two-column product grid. Nav shows logo + hamburger (no inline links). Hero headline at display-md (32px). Download cards in 2-up grid. Filter tabs wrap to two rows if needed. |
| Desktop | 1128–1440px | Three- or four-column product grid. Full horizontal nav with dropdowns. Hero at full display-xl (48px). Spec table fully visible. Download cards in 3-up grid. |
| Wide | > 1440px | Content column caps at 1320px centered with canvas side gutters. Hero uses wider image crop. Product grid may expand to five columns for category archive pages. |

### Touch Targets

- All nav links minimum 44px tap height via padding expansion on mobile drawer
- Filter tabs minimum 40px height on touch breakpoints
- Download card full row is tappable, not just the link text
- Mobile search submit button minimum 44×44px

### Collapsing Strategy

- Utility bar hides completely below 744px; dealer login and account access move into the hamburger drawer
- Dropdown nav converts to accordion within the drawer; no hover state on touch
- Spec tables scroll horizontally inside a fixed container rather than reflow to card layout — preserving column relationships critical for product comparison
- Filter tabs condense to a labeled horizontal scroll with no wrap below 744px; active tab is visually centered on load
- Footer collapses from four columns to two columns at tablet, single accordion at mobile

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom web font files confirmed; DM Serif Display and Lato are inferred from font-family stacks but may be loaded via Google Fonts — specific weights and FOUT behavior are unverified
- Exact nav height for mobile drawer and animation behavior (slide vs. fade) could not be extracted from static hints
- Product card hover animation timing and easing values are not available from extracted data
- Icon system (line vs. filled, stroke weight, specific glyph set for categories and downloads) is undocumented — Dashicons is present in the font stack suggesting WordPress default icons may be in use
- Many extracted colors in the lower half of the palette (#f78da7, #cf2e2e, #ff6900, #fcb900, #7bdcb5, #00d084, #8ed1fc, #0693e3, #9b51e0) are Gutenberg block-editor defaults and have no confirmed role in the brand UI
- Exact amber token usage (#e09004, #b97600) in UI vs. photography context is unclear; assigned here to warm-CCT annotation use only
- No confirmed breakpoint values or grid column counts from source; values above follow common Shopify/WooCommerce professional theme conventions
- Photometric data viewer or IES file preview UI (if present) is not captured in static extraction
