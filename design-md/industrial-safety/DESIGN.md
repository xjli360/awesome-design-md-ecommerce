---
version: alpha
name: "Industrial Safety"
source_url: "https://www.industrialsafety.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Catalog density is the brand's primary design signal — a 50,000-SKU product grid where faceted filters, ANSI/OSHA compliance badges, and safety-standard labels do the visual work that lifestyle photography does elsewhere. The single confirmed surface color extracted from the live site, #313131 (a near-black charcoal), anchors navigation and body text in a utility-forward register that reads as authoritative rather than decorative. This is procurement UI, not lifestyle browsing: search boxes carry structural weight, category navigation spans the full breadth of PPE hierarchy (head protection, hand protection, respiratory, hi-vis apparel), and product cards lead with SKU numbers and specification references rather than editorial copy. Button shapes lean rectangular — {rounded.sm} at most — because the audience is a safety manager buying in bulk, not a consumer scrolling a feed. The typography runs entirely on system stacks (Arial, Roboto, Helvetica Neue), reinforcing the institutional register: no custom font spend, no brand-personality distraction. Where accent color appears on CTAs and add-to-cart actions, it almost certainly draws from the high-visibility spectrum; the orange-amber family is load-bearing in industrial safety culture, encoded in ANSI Z535 signage standards and embedded in every hi-vis vest and hard hat the category sells. Color temperature reads cool and controlled — dark header, white card field, hairline grid — with accent voltage reserved for the action layer. Whitespace is functional rather than expressive: tight {spacing.sm} between product attributes, generous {spacing.section} only at page transitions. Because the site was behind anti-bot protection during extraction and returned only one confirmed color (#313131) with no custom fonts, the accent palette below is inferred from industrial safety category norms and noted fully in Known Gaps.

colors:
  primary: "#e85d04"
  primary-active: "#c44f03"
  primary-disabled: "#f4a87a"
  ink: "#313131"
  body: "#444444"
  muted: "#767676"
  hairline: "#d4d4d4"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  safety-yellow: "#ffd600"
  caution-amber: "#f5a623"
  warning-red: "#c8102e"
  success-green: "#1e7e34"
  compliance-navy: "#1a3a6b"
  compliance-navy-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  sku-label:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  compliance-tag:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: 10px 20px
    height: 40px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 9px 19px
    height: 40px
  button-quote:
    backgroundColor: "{colors.compliance-navy}"
    textColor: "{colors.compliance-navy-text}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 40px
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-utility-bar:
    backgroundColor: "#222222"
    textColor: "#aaaaaa"
    typography: "{typography.caption}"
    height: 36px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 48px 10px 16px
    height: 44px
    submitButtonColor: "{colors.primary}"
    submitButtonTextColor: "{colors.on-primary}"
  category-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 48px
    hoverIndicatorColor: "{colors.primary}"
    hoverIndicatorHeight: 2px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "1:1"
    nameTypography: "{typography.body-sm}"
    skuTypography: "{typography.sku-label}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
  compliance-badge:
    backgroundColor: "{colors.compliance-navy}"
    textColor: "{colors.compliance-navy-text}"
    typography: "{typography.compliance-tag}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  warning-badge:
    backgroundColor: "{colors.warning-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.compliance-tag}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  caution-badge:
    backgroundColor: "{colors.caution-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.compliance-tag}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  in-stock-badge:
    backgroundColor: "{colors.success-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.compliance-tag}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
  filter-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    sectionHeaderTypography: "{typography.title-sm}"
    sectionHeaderColor: "{colors.ink}"
    width: 240px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  product-quantity-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 72px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "#aaaaaa"
    typography: "{typography.body-sm}"
    linkColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — A flat orange (#e85d04) button with uppercase text at 0.6px letter-spacing, 40px height, and {rounded.sm} corners. The uppercase treatment signals the industrial register: this is action-oriented procurement UI, not a lifestyle prompt. Active state deepens to #c44f03; disabled washes to the tint #f4a87a. Padding is 10px 20px, which keeps the footprint dense relative to the product-card grid.

**`button-secondary`** — White canvas with {colors.ink} text and a 1px {colors.hairline} border, matching height and corner radius to `button-primary` for consistent row-pairing on product cards and comparison panels. Used for "Add to Compare," "View Spec Sheet," and download-SDS actions.

**`button-quote`** — Deep navy ({colors.compliance-navy}) with white text in {typography.button-sm}, reserved for "Request a Quote" flows. The navy color distinguishes bulk/contract purchasing from single-unit add-to-cart and visually aligns the button with `compliance-badge` chips on the same card.

### Navigation

**`nav-bar`** — The main navigation sits on a {colors.ink} (#313131) background at 56px height, carrying reversed-out white links in {typography.nav-link} weight 600. An upper `nav-utility-bar` at 36px in deeper #222222 handles account links, order history, and a phone support number at {typography.caption} size in muted gray. The two-bar dark header gives the UI an authoritative, institutional top — consistent with safety signage aesthetics where dark borders signal regulatory weight.

**`search-bar`** — Embedded in the nav bar on desktop, the search input uses a 2px {colors.primary} orange border to pull the eye immediately. A submit button fills solid orange to the right of the field. Search is the primary navigation mode in a 50,000-SKU catalog; the orange framing ensures it reads as the most important interactive element on screen.

**`category-nav`** — A full-width {colors.surface-soft} strip below the nav carrying up to eight top-level PPE category links in {typography.nav-link}. On hover, a 2px primary-orange bottom indicator activates, keeping the accent color vocabulary consistent with the search bar framing. The soft-gray background creates a clear visual break from the dark header without introducing a third surface color.

### Product Card

**`product-card`** — A white {colors.surface-card} tile with 1px hairline border and 2px corner rounding ({rounded.xs}), deliberately minimal to let product photography and spec data carry weight. The top half is a square 1:1 image well. Below it: product name in {typography.body-sm}, SKU number in {typography.sku-label} (monospaced Courier, 11px, for scan-readability in dense grids), price in {typography.price-display} weight 700 at the {colors.primary} orange, and a row of certification chip badges. A full-width add-to-cart `button-primary` anchors the card bottom with a quantity spinner (`product-quantity-input`) alongside it.

### Compliance & Status Badges

**`compliance-badge`** — Navy ({colors.compliance-navy}) background with white uppercase text at 10px and 0.8px letter-spacing on {rounded.xs} corners. Used for ANSI Z87.1, EN 388, NFPA 70E, OSHA 1910, and similar certifications. These badges are functionally load-bearing — a procurement officer scanning category results filters by standard first, brand second.

**`warning-badge`** — Red ({colors.warning-red}) background for hazard-level callouts: "Flammable," "Electrical Hazard," "Chemical Splash." The color follows ANSI Z535 danger-signal convention and triggers immediate attention without requiring an icon.

**`caution-badge`** — Amber ({colors.caution-amber}) with {colors.ink} text for lower-severity notices: "Ships 5–7 Days," "Limited Stock," or CAUTION-level safety flags consistent with the ANSI Z535 yellow standard. Dark text on amber clears the 4.5:1 contrast ratio at 10px bold.

**`in-stock-badge`** — Green ({colors.success-green}) confirms immediate availability, rounding out the ANSI-derived color vocabulary across the badge system.

### Hero Banner

**`hero-banner`** — Full-width dark charcoal ({colors.ink}) panel with reversed-out white headline ({typography.display-xl}) and {typography.body-md} supporting copy, left-aligned. A single `button-primary` CTA sits below the copy block. The dark field lets photography of hi-vis vests, hard hats, and orange gloves read at full saturation without needing a drop shadow or scrim overlay. Padding is {spacing.section} vertical and {spacing.xxl} horizontal — enough breathing room for the type, tight enough to keep the overall register purposeful rather than spacious.

### Filter Sidebar

**`filter-sidebar`** — A 240px left-rail panel in {colors.surface-soft} with 1px hairline border and no border-radius ({rounded.none}) — it reads as structural scaffolding, not a UI card. Section headers (Brand, Category, Certification, Price Range, Color) render in {typography.title-sm} weight 600 at {colors.ink}. Facet items use {typography.body-sm} with checkbox inputs. The sidebar has no shadow and no inner padding rhythm beyond {spacing.sm} per row; the design prioritizes scan speed over visual hierarchy.

### Footer

**`footer`** — Matches the nav-bar in charcoal ({colors.ink}) for visual bookending, with a 3px {colors.primary} orange top border as the only accent. Column headings in {typography.title-sm} white weight 600; links in {typography.body-sm} at #aaaaaa muted gray. The bottom strip carries OSHA compliance language, privacy policy, and copyright in {typography.caption}. The orange top border is the closest the brand comes to a decorative flourish — it visually closes the CTA color loop that the search bar and buttons opened.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger replaces horizontal nav links; search bar drops below header full-width; filter sidebar collapses to bottom drawer triggered by sticky "Filter & Sort" button; product grid shifts to 2-column; compliance badges truncate to icon-only; `nav-utility-bar` folds into hamburger menu |
| Tablet | 744–1128px | Search remains in header; product grid is 3-column; filter sidebar collapses to a toggleable panel; `nav-utility-bar` hidden; category-nav scrolls horizontally |
| Desktop | 1128–1440px | Full two-bar nav; 4-column product grid; persistent filter sidebar; hero banner at full crop; breadcrumb trail visible |
| Wide | > 1440px | Content container caps at 1440px centered; hero fills viewport width with side padding expanding to {spacing.xxl}; product grid stays at 4-column |

### Touch Targets

- All buttons minimum 44px height on mobile (button-primary and button-secondary both meet this at 40px desktop; bump to 44px mobile)
- Filter sidebar checkboxes padded to 44×44px tap target on mobile drawer
- Product card image well is a full-card tap target on mobile
- Nav hamburger at 44×44px
- Compliance badge text (10px) minimum scales to 11px on mobile for readability; badges that overflow wrap rather than truncate

### Collapsing Strategy

- Filter sidebar converts to full-height bottom drawer on mobile and tablet, triggered by sticky "Filter & Sort" button at viewport bottom
- Category nav collapses to a horizontally scrollable chip row at tablet and below
- Utility bar (account, orders, phone number) folds into hamburger menu at tablet and below
- Product grid: 4-col desktop → 3-col tablet → 2-col mobile; optional list-view toggle for dense SKU scanning persists at all breakpoints
- Hero banner headline scales from {typography.display-xl} (32px) to 24px on mobile with padding reducing to {spacing.lg}

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Palette**: Only one hex color (#313131, confirmed as charcoal ink/nav background) was extracted from the live site. The site returned a "Just a moment…" anti-bot challenge and did not render product content. All accent colors — primary orange, caution amber, warning red, compliance navy, safety yellow, success green — are inferred from ANSI Z535 signage conventions and industrial safety category norms, not confirmed from the actual site.
- **True primary CTA color**: The actual add-to-cart button color could be a different orange variant, a safety green, a corporate blue, or a neutral charcoal. Extraction was blocked before any interactive elements could be sampled.
- **Typography**: No custom font-family was detected. The system stack (Arial/Roboto/Helvetica Neue) is confirmed present, but it is unknown whether a licensed display face, icon font, or custom web font loads asynchronously after the anti-bot gate.
- **Logo and wordmark**: No logo color, lock-up treatment, or brandmark geometry could be verified.
- **Component framework**: It is unknown whether the site runs a custom component library or a commercial B2B e-commerce platform (BigCommerce, Unilog, Infor CX, Epicor P21) with its own design tokens and override layer.
- **Navigation taxonomy**: Exact top-level category count, mega-menu depth, and faceted filter hierarchy are unconfirmed.
- **B2B pricing patterns**: Tiered volume pricing display, quote-only SKU presentation, and contract-price masking conventions are assumed from B2B industrial norms but not confirmed from the live UI.
- **Meta theme-color**: No theme-color meta tag was present, which may indicate a non-mobile-optimized legacy stack or dynamic injection.
