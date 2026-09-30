---
version: alpha
name: "Lakeland Industries"
source_url: "https://www.lakeland.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Two greens in the extracted palette mark the boundary between this system and any consumer brand: #008936 — calibrated to the ANSI Z535 standard safety green that appears on approved workplace signage — and #92c836, a high-visibility lime reserved exclusively for proximity warnings and critical-action badges where missing information causes injury. Around that safety-signal vocabulary runs a blue gradient from #003366 deep navy (regulatory headers and certification seal backgrounds) through #0075cf (data-table chrome) to the sky-bright #1da7ee that drives every CTA, search-bar border, and active link state. Ink is #101820, a navy so dark it reads as black on screen but carries faint warmth compared to a pure render — it appears in page banners and product headings where legibility under fluorescent warehouse lighting matters. Typography commits entirely to Arial and Helvetica with no custom font loaded, an unusual discipline in 2020s DTC web design that prioritizes spec-sheet print fidelity over expressive brand character; a catalog that procurement officers print at 8pt on laser printers cannot afford a webfont that fails to embed. Corner radii sit almost at zero: {rounded.xs} at 2px is the universal workhorse — the {rounded.full} pill shape that consumer brands use to signal approachability would feel out of place next to arc-flash ratings and chemical resistance classes rendered in {typography.spec-label} uppercase. The #92c836 hi-vis green and #008936 safety green never appear in hover states or decorative gradients; they are reserved exclusively for certification badges and compliance-level indicators, keeping their urgency signal intact for the safety managers, purchasing agents, and first responders who depend on instant visual triage.

colors:
  primary: "#1da7ee"
  primary-active: "#0085d4"
  primary-dark: "#0075cf"
  primary-navy: "#003399"
  primary-disabled: "#f5fafd"
  ink: "#101820"
  body: "#303030"
  muted: "#495c68"
  muted-soft: "#aaaaaa"
  hairline: "#d0d0d0"
  hairline-soft: "#e6e6e6"
  canvas: "#fefefe"
  surface-soft: "#f2f2f2"
  surface-card: "#f8f8f8"
  surface-deep: "#f0f0f0"
  on-primary: "#fefefe"
  safety-green: "#008936"
  hi-vis-green: "#92c836"
  navy: "#003366"
  scrim: "#222222"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  spec-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  category-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 12px
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
    height: 40px
    border: none

  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"

  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.xs}"

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "2px solid {colors.primary}"

  button-navy:
    backgroundColor: "{colors.primary-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
    border: none

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: none

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted-soft}"

  nav-bar:
    backgroundColor: "{colors.primary-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    topBand:
      backgroundColor: "{colors.ink}"
      height: 36px
      textColor: "{colors.muted-soft}"
      typography: "{typography.caption}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderHover: "1px solid {colors.primary}"
    padding: "{spacing.base}"
    imageAspectRatio: "1 / 1"
    imageBackgroundColor: "{colors.canvas}"
    productCode:
      typography: "{typography.caption}"
      textColor: "{colors.muted}"
    productName:
      typography: "{typography.title-sm}"
      textColor: "{colors.ink}"
    pricingLabel:
      typography: "{typography.title-md}"
      textColor: "{colors.primary-navy}"

  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlayColor: "{colors.scrim}"
    overlayOpacity: 0.55
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"

  category-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.category-label}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    activeTextColor: "{colors.primary}"
    activeBorderBottom: "3px solid {colors.primary}"
    hoverBackgroundColor: "{colors.surface-deep}"

  certification-badge:
    backgroundColor: "{colors.safety-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  hi-vis-badge:
    backgroundColor: "{colors.hi-vis-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  compliance-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
    border: "1px solid {colors.hairline}"

  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    height: 44px
    placeholderColor: "{colors.muted-soft}"
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitTypography: "{typography.button-md}"
    submitRounded: "{rounded.none}"

  spec-table:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    headerBackgroundColor: "{colors.primary-navy}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.spec-label}"
    rowTextColor: "{colors.body}"
    rowTypography: "{typography.body-sm}"
    altRowBackgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.caption-bold}"
    labelTextColor: "{colors.muted}"

  protection-level-indicator:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    ratingLabelTypography: "{typography.spec-label}"
    ratingLabelColor: "{colors.muted}"
    ratingValueTypography: "{typography.title-md}"
    ratingValueColor: "{colors.ink}"
    certifiedDotColor: "{colors.safety-green}"
    conditionalDotColor: "{colors.hi-vis-green}"

  alert-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.none}"

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.primary}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
    bottomBarBackgroundColor: "{colors.navy}"
    bottomBarTextColor: "{colors.muted-soft}"
    bottomBarTypography: "{typography.caption}"

## Components

### Buttons

**`button-primary`** — A #1da7ee sky-blue block at 40px tall with white uppercase Arial at 14px/0.5px tracking, 2px radius. Active state darkens to #0085d4 on hover; disabled state washes to the pale #f5fafd surface with #aaaaaa text. Appears on primary commerce actions ("Add to Cart," "Request Quote," "Find a Distributor") and is the only button with a filled blue brand presence outside of `button-navy`.

**`button-secondary`** — White background with a 2px #1da7ee border and matching uppercase text at the same size as primary. Used beside primary actions for secondary paths like "Download Spec Sheet" or "Compare Models." On hover, border darkens to #0085d4 without background fill.

**`button-navy`** — #003399 deep navy fill with white uppercase text. Deployed in hero overlays and marketing banners where the primary blue would compete with background imagery; signals regulatory authority and institutional weight. No hover radius change — stays at {rounded.xs}.

**`button-ghost`** — Transparent background with #1da7ee uppercase text and no border. Used for low-priority inline actions like "See All" in category rows and "View More" within paginated grids.

### Nav Bar

**`nav-bar`** — A two-band header: a 36px #101820 top strip carrying utility links (account, distributor locator, global region selector) in 12px #aaaaaa caption type, stacked above a 56px #003399 navy main band with white bold nav-link labels at 14px. No rounded corners anywhere in the header assembly. On desktop, a full-width search bar with a 2px #1da7ee border spans below or inline within the main nav. Mega-dropdown panels emerge from the navy bar over a #f2f2f2 surface with #d0d0d0 column dividers.

### Product Card

**`product-card`** — Zero-radius card on #f8f8f8 with a 1px #d0d0d0 border that activates to a 1px #1da7ee highlight on hover. The image zone is square aspect ratio against a white canvas background. Product SKU code sits above the name in 12px #495c68 muted type; product name in 15px bold #101820 ink; pricing (where shown) in 18px bold #003399 navy. Certification badges — `certification-badge` and `hi-vis-badge` — stack horizontally below the image before the product name. No box-shadow; the hover border is the entire interaction signal.

### Hero

**`hero`** — Full-bleed photographic hero with a 0.55-opacity #222222 overlay ensuring text contrast over industrial photography (refinery workers, firefighters in turnout gear, chemical plant environments). Headline at 40px bold Arial in white, subhead at 22px bold, body copy at 16px regular. A single #1da7ee CTA button sits left-aligned over the overlay at {rounded.xs}. Minimum height 480px on desktop. The overlay is uniform rather than gradient — industrial seriousness over atmospheric softness.

### Category Navigation

**`category-nav`** — A horizontal strip of uppercase 13px category labels on a #f2f2f2 surface with 1px #d0d0d0 border at top and bottom. Active tab carries a 3px #1da7ee bottom border with no background change and no radius on any state. Pivots between protection categories: Fire, Chemical, Hi-Vis, Arc Flash, Cut Protection, Disposables. On mobile this strip scrolls horizontally with the active tab always scrolled into view.

### Certification Badges

**`certification-badge`** — #008936 green block at 2px radius with white uppercase 11px badge text, padding 3px/8px. Renders only for confirmed third-party certified protection standards (NFPA 2112, ANSI/ISEA 107, EN ISO standards). **`hi-vis-badge`** uses #92c836 lime fill with #101820 dark text — reserved for high-visibility classifications and proximity-warning levels. Neither badge style appears in marketing decoration or hover states; their semantic exclusivity is the design intention.

**`compliance-tag`** — A subdued version on #f2f2f2 surface with 1px #d0d0d0 border and 11px uppercase #aaaaaa spec-label text. Used for standards that are listed but not independently verified, or for pending certifications awaiting audit.

### Search Bar

**`search-bar`** — Full-width input at 44px tall with a 2px #1da7ee border at {rounded.xs} and a flush-jointed submit button in #1da7ee with {rounded.none} — the two pieces read as a single compound control. Placeholder text in #aaaaaa. On mobile the search bar expands to fill the full viewport width. The submit button carries white uppercase 12px button-sm type with no padding radius.

### Spec Table

**`spec-table`** — Zero-radius data table with a #003399 navy header row in white 11px uppercase spec-label type. Body rows alternate between white and #f2f2f2 with 14px #303030 body text. Attribute label cells use 12px bold #aaaaaa caption-bold type. Applied on product detail pages to display arc rating (cal/cm²), flame resistance standard, size range, material weight (oz/yd²), temperature rating, and chemical splash resistance.

### Protection Level Indicator

**`protection-level-indicator`** — A compact widget on #f2f2f2 surface with 1px #d0d0d0 border at {rounded.xs} displaying protection ratings in a 2-column grid. Rating attribute in 11px uppercase #aaaaaa; rating value in 18px bold #101820. A small dot before each value uses #008936 safety-green for fully certified ratings and #92c836 hi-vis for conditional or limited ratings. Embedded within product detail sidebars rather than in card grids.

### Alert Banner

**`alert-banner`** — A 100%-width #1da7ee blue strip with white 14px body text, no radius, and no close control by default. Used for sitewide announcements: distributor event schedules, certification standard updates, product safety notices. The blue matches primary exactly — it is an authoritative declaration, not a marketing interruption.

### Footer

**`footer`** — #101820 near-black background with section headings in 15px bold white and links in 14px #1da7ee blue arranged across four columns: Products, Industries Served, Resources, Company. A #003366 sub-basement bar carries copyright and legal links in 12px #aaaaaa caption type. No rounded elements anywhere in the footer assembly.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category-nav becomes horizontal scroll strip; nav collapses to hamburger over a full-height #003399 navy drawer; hero shrinks to 320px min-height; spec-table scrolls horizontally with sticky first column |
| Tablet | 744-1128px | Two-column product grid; category-nav shows 5–6 visible tabs before clipping; hero at 400px; search bar inline within the navy nav band |
| Desktop | 1128-1440px | Three- or four-column product grid; dual-band nav at full width with mega-dropdown panels; spec-table renders inline in product detail two-column layout |
| Wide | > 1440px | Max-width container centered at 1440px; product grid holds at 4 columns; hero may extend to 560px min-height with wider copy column |

### Touch Targets

- All buttons minimum 40px tall and 88px wide on mobile
- Category-nav tabs minimum 44px tall with 12px horizontal padding on each side
- Certification badges are display-only and non-tappable; the surrounding product card link is the tap target
- Search submit button maintains 44px height across all breakpoints
- Nav hamburger trigger is a 48×48px hit area independent of icon size
- Footer link rows have minimum 44px vertical spacing on mobile

### Collapsing Strategy

- The 36px utility top band (#101820 strip) collapses entirely below tablet; account and distributor links migrate into the nav drawer
- Category-nav becomes a momentum-scrolling horizontal strip on mobile; no overflow indicators shown, leftmost item is "All Categories"
- Spec tables clip to the 3 most critical columns on tablet (e.g., Standard, Rating, Size Range) with a "Show all specifications" toggle revealing the full column set
- Footer 4-column layout stacks to single-column accordions on mobile; each section heading is the tap target to expand its link list
- Hero CTA button stacks below the headline block on mobile rather than appearing inline

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand-specific custom typeface was detected in the extracted CSS; the Arial/Helvetica stack may indicate no webfont is loaded, or a font injected via JavaScript after the extraction point. If Lakeland uses a licensed typeface, it was not present.
- `primary-disabled` is approximated from #f5fafd, the palest blue-tinted surface in the extracted palette — no confirmed disabled-state color token was found.
- No error or destructive state color (typically a red) was present in the extracted palette; Lakeland may render error states via standard browser defaults or a red not captured in the extraction run.
- No confirmed modal overlay scrim opacity; 0.55 is an informed estimate based on dark-photography hero overlay conventions.
- No promotional or sale price color (red, orange, or accent) was found — Lakeland may not display retail-facing pricing or promotions on the extracted pages, which appear distributor/B2B oriented.
- Icon library style, weight, and size grid could not be determined from CSS extraction alone.
- WooCommerce appears in the font-family stack list, suggesting a WordPress/WooCommerce backend whose theme-level design tokens were filtered or not present in extractable CSS.
- Hover state colors for nav mega-dropdown links and card border transitions are inferred from the active-state blue pattern rather than directly extracted values.
- No loading, skeleton, or progress indicator styles were found; these likely exist in the WooCommerce theme layer.
