---
version: alpha
name: "AEMC Instruments"
source_url: "https://www.aemc.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Safety yellow (#ffd100) occupies every primary CTA and nav accent at AEMC — the same hue stenciled on high-voltage warning placards appears in category banners and search submit buttons, closing the perceptual gap between the physical clamp meter on a technician's belt clip and the catalog page that sold it. Dark charcoal (#3c404d) carries structural weight: top navigation, body text, and footer chrome all run at this near-black depth, lending the interface the gravity of a calibration data sheet rather than a retail landing page. Two pale sky tints (#7fcdfe, #aadeff) appear selectively in product photography overlays and accent zones, echoing the backlit LCD readouts on AEMC's panel meters and power analyzers. The silver-gray (#c1ccd0) occupies spec table headers, input borders, and divider lines — reading like anodized aluminum against the white product-page canvas. A secondary warm yellow (#ffde00) sits adjacent to the primary, providing a soft hover graduation without breaking the electrical-signal palette.

  Typography lands on Calibri and Arial at controlled weights with no decorative cuts anywhere. Display headings reach 36px at weight 700; body runs 14px at weight 400; uppercase letter-spacing on spec-label rows and product-number callouts signals the engineering register the brand inhabits. Nothing displays at the oversized proportions common to consumer storefronts — an engineer scanning measurement ranges and CAT ratings needs density, not drama.

  Corner radii hold at a blunt {rounded.xs} (4px) across buttons, inputs, cards, and filter tiles. Nothing pills or rounds dramatically; the geometry sits closer to the square housing of a switchboard instrument than the softened forms of a lifestyle app. Hairline borders at {colors.hairline} trace product card perimeters and spec table rows without adding visual noise.

  The information hierarchy puts product family, model number, and key measurement ranges into view before any headline copy. Filter panels run left-rail in category views, scoped by measurement type and product line. Specification tables dominate detail pages — accuracy class, CAT rating, compliance standard, and measurement range rows precede marketing prose. Hero sections use the dark charcoal field with yellow headline accents and white body type, producing high contrast that reads as authoritative rather than alarming.

colors:
  primary: "#ffd100"
  primary-active: "#e6bc00"
  primary-warm: "#ffde00"
  primary-disabled: "#fff3a3"
  ink: "#3c404d"
  body: "#3c404d"
  muted: "#6b7585"
  hairline: "#d6d6d6"
  hairline-soft: "#eaeaea"
  canvas: "#ffffff"
  surface-soft: "#f4f5f6"
  surface-card: "#ffffff"
  surface-steel: "#c1ccd0"
  on-primary: "#3c404d"
  on-dark: "#ffffff"
  accent-sky: "#7fcdfe"
  accent-sky-soft: "#aadeff"
  nav-dark: "#3c404d"

typography:
  display-xl:
    fontFamily: "Calibri, Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Calibri, Arial, Helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "Calibri, Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Calibri, Arial, Helvetica, sans-serif"
    fontSize: 17px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Calibri, Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Calibri, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Calibri, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Calibri, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "Calibri, Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  spec-value:
    fontFamily: "Arial, Calibri, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  product-number:
    fontFamily: "Calibri, Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Calibri, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Calibri, Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Calibri, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Calibri, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
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
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 9px 19px
    height: 40px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.accent-sky}"
    typography: "{typography.button-sm}"
    padding: 6px 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 38px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    outline: "2px solid {colors.primary-disabled}"
  nav-bar:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "3px solid {colors.primary}"
  nav-bar-top:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 32px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    boxShadow: "0 4px 12px rgba(60,64,77,0.14)"
    padding: "{spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    modelTypography: "{typography.product-number}"
    padding: "{spacing.base}"
  product-card-hover:
    border: "1px solid {colors.surface-steel}"
    boxShadow: "0 2px 8px rgba(60,64,77,0.12)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
    padding: 0 12px
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    width: 44px
    height: 40px
  hero:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 400px
    padding: "{spacing.xxl} {spacing.xl}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    accentBar: "3px solid {colors.primary}"
    padding: "{spacing.lg}"
    hoverBackgroundColor: "{colors.surface-steel}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBg: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.spec-value}"
    cellTextColor: "{colors.body}"
    rowBorderColor: "{colors.hairline-soft}"
    alternateRowBg: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  product-badge-new:
    backgroundColor: "{colors.accent-sky}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline}"
  filter-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    headerTypography: "{typography.title-sm}"
    accentColor: "{colors.primary}"
    checkmarkColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.accent-sky-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    topBorder: "4px solid {colors.primary}"
    padding: "{spacing.xxl} 0"
  alert-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"

## Components

### Buttons

**`button-primary`** — Yellow (#ffd100) fill with charcoal (#3c404d) text at `{typography.button-md}` weight 700, 40px tall, `{rounded.xs}` corners. The dark-on-yellow pairing draws contrast without softening into consumer register. Active state darkens to `{colors.primary-active}` (#e6bc00); disabled state washes to `{colors.primary-disabled}` with muted text so the affordance reads as inactive without disappearing entirely.

**`button-secondary`** — White canvas fill with charcoal text and a 1px `{colors.hairline}` border. Matches primary in height and radius so the two sit side-by-side without size mismatch. Hover/active state fills with `{colors.surface-soft}` to provide feedback without introducing a new color. Use for non-destructive secondary actions like "Download Datasheet" adjacent to a primary "Add to Cart."

**`button-ghost`** — Transparent background, `{colors.accent-sky}` text with underline decoration, 13px weight 700. Deployed for low-hierarchy links inside body content or spec panels — small print actions like "Compare Models" or "View All Accessories."

### Text Input & Search

**`text-input`** — White canvas, 1px `{colors.hairline}` border, `{rounded.xs}`, 38px height. Placeholder text in `{colors.muted}`. Focus state promotes the border to `{colors.primary}` with a 2px outer ring in `{colors.primary-disabled}`, using the brand yellow as focus signal rather than a generic blue ring — consistent with the electrical-yellow brand language.

**`search-bar` + `search-submit`** — The search input and its submit button are flush at `{rounded.xs}` on the input side and `{rounded.none}` on the button side, forming a single compound control. The submit button is a 44×40px yellow square with a charcoal search icon — the yellow panel reads as a push-button indicator light, consistent with panel-instrument aesthetics.

### Navigation

**`nav-bar-top`** — Slim 32px utility bar in `{colors.ink}` with `{colors.on-dark}` caption text. Carries phone number, distributor locator, and login links — the technical-customer utility layer above main navigation.

**`nav-bar`** — 56px dark charcoal rail with a 3px `{colors.primary}` bottom border line that runs full width. Nav links in `{colors.on-dark}` at `{typography.nav-link}` weight 600. The yellow underline border anchors the brand accent at page top without requiring a fully yellow nav bar.

**`nav-dropdown`** — White panel with 1px `{colors.hairline}` border and medium box-shadow, `{rounded.xs}`. Items in `{colors.ink}` at `{typography.nav-link}`. Product categories organized by measurement discipline — voltage, current, power quality, insulation — rather than product type. No mega-imagery; the dropdown is density-first.

### Product Cards

**`product-card`** — White card with 1px `{colors.hairline}` border, `{rounded.xs}`, and `{colors.surface-soft}` image well. Model number renders in `{typography.product-number}` (12px uppercase tracked) above the product name in `{typography.title-sm}`. No star ratings or review counts are surfaced at card level; the professional buyer cares about model number and key spec callout. Hover promotes the border to `{colors.surface-steel}` and adds a subtle shadow lift.

### Hero

**`hero`** — Dark charcoal (#3c404d) field with white headline at `{typography.display-xl}` and body copy at `{typography.body-md}`. Accent elements — CTA button, category pill labels, decorative rule — all render in `{colors.primary}` yellow. Minimum 400px height allows product photography to sit alongside headline text at desktop without cropping. The charcoal-yellow-white palette reads as industrial without requiring photography to carry the brand load.

### Category Tiles

**`category-tile`** — Light surface fill (`{colors.surface-soft}`) with a 3px left-edge accent bar in `{colors.primary}`, 1px `{colors.hairline}` perimeter border, `{rounded.xs}`. Title at `{typography.title-md}` weight 700. Hover fills the tile background to `{colors.surface-steel}` for a steel-panel hover effect consistent with the instrument-housing metaphor. Tiles organize the catalog by measurement discipline: Power Quality, Ground Resistance, Insulation, Clamp-On, etc.

### Specification Table

**`spec-table`** — The signature component of any product detail page. Header row in `{colors.surface-soft}` with `{typography.spec-label}` (12px uppercase, weight 700, letter-spaced) for column names. Cell rows alternate with `{colors.surface-soft}` fill and divided by `{colors.hairline-soft}` lines. Row borders use `{rounded.none}` — full-square grid geometry matching the precision-instrument context. Spec values render at `{typography.spec-value}` (13px regular). This table should be the dominant content block on detail pages, appearing before any marketing description.

### Badges

**`product-badge`** — Yellow fill (`{colors.primary}`) with charcoal text, `{rounded.xs}`, 11px uppercase weight 700. Used for "SALE," "FEATURED," "DISCONTINUED." The yellow badge on a white card card creates a direct product-label analogue — the same way a calibration sticker sits on physical instruments.

**`product-badge-new`** — Sky-blue fill (`{colors.accent-sky}`) with charcoal text. Differentiates new-product introductions from promotional states, using the blue accent color that otherwise signals information/data contexts.

### Filter Panel

**`filter-panel`** — Left-rail white panel with 1px `{colors.hairline}` border and `{rounded.xs}`. Section headers at `{typography.title-sm}` weight 600. Filter options at `{typography.body-sm}` with checkbox controls; checked state fills the checkbox with `{colors.primary}` yellow. Filters organized by: Measurement Category, Product Family, Number of Functions, Standards Compliance (IEC/UL/CSA). The yellow checkbox accent maintains brand consistency without requiring custom form control rendering.

### Footer

**`footer`** — Dark charcoal field matching `{colors.nav-dark}`, topped with a 4px `{colors.primary}` yellow border line. Section headings at `{typography.title-sm}` in `{colors.on-dark}`; link text in `{colors.accent-sky-soft}` (#aadeff) for accessibility against the dark ground. Columns: Products, Support, Company, Distributors. Bottom row holds legal copy at `{typography.caption}`. The yellow top border mirrors the nav-bar bottom border, bookending page content with the brand's primary accent.

### Alert Banner

**`alert-banner`** — Full-width yellow bar (`{colors.primary}`) with charcoal text at `{typography.body-sm}`. Used for site-wide announcements, trade show schedules, or calibration service notices. The yellow banner occupies the zone between the utility nav and main nav — readable as a system-level indicator rather than a promotional intrusion.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter panel moves to modal drawer triggered by "Filter" button; nav collapses to hamburger with full-screen overlay; hero stacks headline above photography; spec tables scroll horizontally with sticky first column |
| Tablet | 744–1128px | Two-column product grid; filter panel may remain as collapsible sidebar or move to top filter strip; nav shows primary categories with overflow menu; hero runs side-by-side layout at reduced image size |
| Desktop | 1128–1440px | Three- or four-column product grid; left-rail filter panel fixed-width (~240px); full horizontal nav with dropdowns; hero at full 400px+ height with image right |
| Wide | > 1440px | Content constrained to max-width (~1400px) centered with canvas-color gutters; grid remains four-column; spec tables gain breathing room with wider cell padding |

### Touch Targets

- All primary buttons minimum 40px height; tap targets padded to 44px vertically where content is short
- Filter checkboxes padded to 44×44px touch zones even if visual size is smaller
- Nav hamburger icon minimum 44×44px
- Product card entire surface is tappable on mobile, not just the title link
- Search submit button minimum 44px wide on mobile

### Collapsing Strategy

- Primary nav collapses to hamburger at < 744px; product-category mega-nav becomes accordion inside the overlay
- Filter panel converts from persistent left-rail to a bottom sheet or modal drawer on mobile; active filter count shown on trigger button
- Spec table gains horizontal scroll container on mobile with the parameter-name column sticky-left
- Hero copy and CTA stack vertically; image moves below fold or becomes a background with reduced opacity on very narrow viewports
- Utility nav (top bar with phone/login) hides on mobile or condenses to icon-only
- Category tile grid collapses from 4-across → 2-across → 1-across through breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected — site uses system stack (Calibri, Arial, Helvetica). No OpenType features, variable-font axes, or licensed display weights can be confirmed; all typographic tokens are derived from system font behavior
- Hyperlink body-text color not reliably extracted; `{colors.accent-sky}` family used as proxy — actual link treatment may use a standard browser default or a distinct dark-blue not present in the extracted palette
- `primary-active` (#e6bc00), `primary-disabled` (#fff3a3), `muted` (#6b7585), `hairline-soft` (#eaeaea), `surface-soft` (#f4f5f6) are derived/extrapolated from extracted colors — not directly sampled
- Dark mode or alternate color scheme not detected in extraction
- Exact nav height, mega-menu column layout, and dropdown animation timing not measured from live site
- Interactive hover and focus-ring treatment for product cards not confirmed beyond structural inference
- E-commerce cart, checkout, and pricing display format not confirmed — unclear whether direct purchase or distributor-redirect flow is primary
- Product comparison table UI not observed — likely present given the catalog depth but visual treatment unconfirmed
- CAD/drawing download and documentation portal styling not captured
- Mobile breakpoint exact pixel values are inferred from common practice, not measured from the live responsive implementation
