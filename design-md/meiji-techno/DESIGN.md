---
version: alpha
name: "Meiji Techno"
source_url: "https://www.meijitechno.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Meiji Techno's palette runs the full optical path of teal light — deep instrument-grade #226d7a as the primary anchor, brightening to the luminous #22b8d1 of a back-illuminated stage, then dispersing into the barely-tinted #e4f5fa wash that fills section backgrounds. The monochromatic discipline is unusual for a hardware brand and reads as a deliberate echo of the aqueous environments that microscopy objectives are designed to study: immersion oil, water-dip lenses, stained biological samples suspended in saline. There are no warm accents, no oranges or ambers — only a cool, precise blue-green register from saturation peak to near-white. Typography runs on system-accessible stacks anchored by Open Sans, kept tight in weight (600 at headlines, 400 at body) so that specification tables and optical parameter grids remain readable at small print sizes; scientific catalogs demand that dense tables hold legibility, and Meiji delivers that in a utilitarian font choice rather than a display face with personality. Button radii are moderate — `{rounded.sm}` at 8px — stopping short of pill-form friendliness and well short of hard-square industrial. Cards use `{rounded.md}` at 12px, a practical middle ground that signals approachability without frivolity. Spacing is generous at the section level (64px breaks), reflecting a catalog-style layout where each product family — stereo microscopes, biological scopes, polarizing instruments, industrial systems — occupies a distinct visual zone. The surface hierarchy is minimal: white cards sit on `{colors.surface-soft}` (#e4f5fa) tinted sections, with `{colors.hairline}` borders doing the containment work. Search and filter toolbars carry the brand teal at full saturation, signaling that product discovery is the primary customer journey. The overall register is a scientific instrument company that trusts the quality and specificity of its product photography over decorative UI — the design stays out of the way of the optics.

colors:
  primary: "#226d7a"
  primary-hover: "#1e6d7a"
  primary-active: "#185e6a"
  primary-disabled: "#b0e0e9"
  accent: "#22b8d1"
  accent-soft: "#b0e0e9"
  ink: "#1a2a30"
  body: "#344d55"
  muted: "#6b8e99"
  hairline: "#c5e2ec"
  hairline-soft: "#dff0f5"
  canvas: "#ffffff"
  surface-soft: "#e4f5fa"
  surface-card: "#ffffff"
  surface-teal: "#b0e0e9"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  error: "#c0392b"
  success: "#1e7d4b"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  spec-label:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  tag:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
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
    rounded: "{rounded.sm}"
    padding: 11px 22px
    height: 42px
    hoverBackground: "{colors.primary-hover}"
    activeBackground: "{colors.primary-active}"
    disabledBackground: "{colors.primary-disabled}"
    disabledText: "{colors.on-primary}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.primary}"
    padding: 10px 22px
    height: 42px
    hoverBackground: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    hoverBackground: "{colors.surface-soft}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 22px
    height: 42px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
    activeColor: "{colors.primary}"
    dropdownBackground: "{colors.canvas}"
    dropdownShadow: "0 4px 16px rgba(34,109,122,0.12)"
  top-utility-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    linkColor: "{colors.surface-teal}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    shadow: "0 2px 8px rgba(34,109,122,0.08)"
    hoverShadow: "0 6px 20px rgba(34,109,122,0.15)"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    modelLabelTypography: "{typography.spec-label}"
    modelLabelColor: "{colors.muted}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    overlayGradient: "linear-gradient(135deg, {colors.primary} 55%, {colors.accent} 100%)"
    ctaButton: "{components.button-accent}"
  hero-teal-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    accentBar: "4px solid {colors.accent}"
    padding: "{spacing.section} {spacing.xl}"
  category-nav-strip:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    height: 48px
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    itemPadding: "10px {spacing.base}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    headerTextColor: "{colors.primary}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.ink}"
    rowBorder: "1px solid {colors.hairline-soft}"
    altRowBackground: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    iconColor: "{colors.primary}"
    height: 44px
    padding: "0 {spacing.base}"
  badge-category:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    border: "1px solid {colors.hairline}"
  badge-new:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  product-series-block:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    headerBackground: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    bodyTextColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    headerColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    activeFilterBadge: "{colors.surface-teal}"
    activeFilterText: "{colors.primary}"
    checkboxAccent: "{colors.primary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.surface-teal}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    dividerColor: "rgba(255,255,255,0.15)"
    padding: "{spacing.xxl} {spacing.xl} {spacing.lg}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.primary}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline}"

## Components

### Buttons

**`button-primary`** — Deep teal #226d7a fill with white text at 14px/600 weight Open Sans, 8px radius, 42px height, 22px horizontal padding. Hover steps to #1e6d7a, active to #185e6a; disabled state uses #b0e0e9 fill keeping white text. Deployed on all primary CTAs: "Request a Quote," "Download Specs," "Find a Dealer."

**`button-secondary`** — White background with teal border (1.5px solid #226d7a) and teal text, matching button-primary height and radius. Background shifts to `{colors.surface-soft}` on hover. Used alongside button-primary for secondary actions like "Learn More" or "Compare Models."

**`button-ghost`** — Transparent background, teal text, no border. Padding reduced to 10×16px. Appears in tight navigation contexts and within spec-table rows for "View Full Specs" links.

**`button-accent`** — Bright #22b8d1 fill with white text. Reserved for hero CTAs where the primary teal background would cause contrast blending. Creates luminous call-to-action pop against dark teal hero sections.

### Navigation

**`nav-bar`** — 64px white bar with 1px hairline underline. Logo renders in primary teal. Nav links are 13px/600 Open Sans with teal active underline indicator. Dropdowns are white cards with 4px teal left-accent border, shadow `0 4px 16px rgba(34,109,122,0.12)`. Sits below a 36px `top-utility-bar` in full primary teal carrying contact, dealer locator, and language links.

**`category-nav-strip`** — A secondary horizontal strip in `{colors.surface-teal}` (#b0e0e9) positioned below the main nav on product category pages. Items for Biological, Stereo, Polarizing, Industrial, and Digital systems; active item inverts to full teal fill with white text at `{rounded.xs}`.

### Product Discovery

**`product-card`** — White card, 12px radius, subtle teal-tinted shadow that deepens on hover. Product image sits on `{colors.surface-soft}` tinted background to maintain visual consistency across differently lit studio shots. Model number renders in `{typography.spec-label}` (11px uppercase, muted) above the product name in `{typography.title-sm}`. Badge slots for NEW and series label appear top-right of the image frame.

**`product-series-block`** — Used for series landing sections (MA series, RZ series, etc.). Header bar uses full primary teal with white title in `{typography.title-md}`; body area is `{colors.surface-soft}` with descriptive text and 2-3 key spec callouts before linking to individual models.

**`filter-sidebar`** — Left-rail filter panel, white background with hairline border. Section headers in primary teal 15px/600. Checkboxes use teal accent; active filter pills render in `{colors.surface-teal}` with teal text, dismissible via ×.

**`search-bar`** — Pill-shaped (9999px radius) with teal search icon, 44px height. Focus state upgrades border from hairline to 2px solid primary teal. Expands to full-width on mobile.

### Data Display

**`spec-table`** — The most heavily used component on product pages. Header row in `{colors.surface-soft}` with `{typography.spec-label}` (11px uppercase) in primary teal. Alternating rows use `{colors.surface-soft}` for the off-white stripe. Cell text in `{typography.body-sm}`. Optical parameters (magnification, NA, WD, FOV) are displayed in this component on every individual microscope model page.

### Hero & Sections

**`hero-section`** — 480px minimum height, primary teal background with a 135° gradient bleeding toward #22b8d1 at the bottom-right. Headline in 36px/700 white, subhead in 20px/600 white. CTA uses `button-accent` to separate from the teal background. Typically carries a product hero image flush-right with drop shadow removed.

**`hero-teal-light`** — Alternate hero for sub-category pages. `{colors.surface-soft}` (#e4f5fa) background with dark ink text, and a 4px solid `{colors.accent}` left accent bar on the headline block. Lower contrast intensity than the full teal hero, used for informational or support sections.

### Badges & Labels

**`badge-category`** — `{colors.surface-soft}` fill with primary teal text, hairline border, 4px radius. Labels product series or application type (Clinical, Research, Industrial, Educational).

**`badge-new`** — #22b8d1 accent fill, white text, 4px radius. Applied top-right on product card image area for recently released models.

### Footer

**`footer`** — Full-width primary teal (#226d7a) footer. Column headers in 15px/600 white; body links in `{colors.surface-teal}` (#b0e0e9) stepping to white on hover. Divided by 15% white opacity rules. Bottom strip carries copyright in caption-size. The full primary teal footer creates bookend symmetry with the dark top utility bar.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Nav collapses to hamburger on white bar; category-nav-strip becomes horizontal scroll. Product cards stack to 1 column. Spec tables scroll horizontally with pinned left column for parameter names. Hero text scales to display-sm (20px). Filter sidebar slides in as bottom sheet. |
| Tablet | 744–1128px | 2-column product grid. Nav shows logo + hamburger + utility icons (search, contact). Category strip remains visible. Hero switches to split layout: text left, image right at 50/50. Spec tables fully visible at tablet width. |
| Desktop | 1128–1440px | Full nav with dropdown menus. 3-column product grid. Filter sidebar fixed left rail (240px). Hero at full 480px height with gradient. Spec tables, series blocks, and comparison tools render at designed widths. |
| Wide | > 1440px | Max-width container at 1400px centered. Hero background extends edge-to-edge, content constrained. Product grid may expand to 4 columns on very wide viewports. Section padding increases to section (64px) vertically. |

### Touch Targets

- All buttons minimum 42px height; nav tap targets padded to 44px minimum
- Category nav strip items minimum 44px tall on mobile via increased vertical padding
- Filter checkboxes padded to 40×40px tap zone even when visually smaller
- Product cards tap the entire card surface as a link unit
- Search bar expands to full viewport width minus 32px margin on mobile

### Collapsing Strategy

- Primary navigation: logo + hamburger on mobile; full horizontal links at desktop ≥1128px
- Category nav strip: horizontal scroll with visible scroll indicator on mobile; fixed horizontal list on tablet+
- Filter sidebar: hidden by default on mobile behind a "Filter" button that triggers bottom sheet overlay; always visible left rail on desktop
- Spec tables: horizontal scroll container on mobile with sticky first column; full table at tablet+
- Product series blocks: image stacks above text on mobile; side-by-side at tablet+
- Footer columns: 1-column accordion on mobile; 4-column grid at desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned HTTP 403 during extraction — all colors derived from the extracted palette hints only; no confirmation of exact usage context (primary nav vs. hero vs. CTA) was possible
- No brand-specific typeface confirmed; Open Sans assumed from stack order in extraction (`Open Sans, Roboto, Arial, sans-serif`) but a custom or licensed web font may be in use behind the block
- No confirmed icon system — scientific instrument brands often use custom line icons for microscopy diagrams and application icons; none extracted
- No dark mode or alternate theme variants confirmed
- Exact button border-radius and height values are inferred from category conventions, not extracted from live CSS
- No motion/animation tokens extracted — transitions on hover states, dropdown reveals, and image zoom on product cards are unconfirmed
- No confirmed secondary brand color beyond the teal-to-light-teal spectrum; an entirely neutral or warm accent may exist in print materials not reflected in the web palette
- Pricing display patterns, add-to-cart flows, and quote-request form styling could not be observed due to site block
- Mobile breakpoints are inferred at industry-standard values; actual CSS breakpoints not confirmed
