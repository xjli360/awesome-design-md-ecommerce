---
version: alpha
name: "Thorlabs"
source_url: "https://www.thorlabs.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The search bar on Thorlabs' homepage functions as the de facto hero — a wide, high-contrast input that dominates the masthead, reflecting a site built for engineers who already know the part number and need only a fast path to the datasheet. The font pairing is the sharpest design signal the extraction yielded: Manrope, a geometric sans-serif with tight apertures and crisp numeric figures, serves the UI and catalog layer, while Ysabeau — an unusual semi-formal roman with classical stroke contrast — steps in for display contexts, lending a grain of editorial authority to what is otherwise a precision catalog. Japanese and Simplified Chinese Noto stacks signal a serious international engineering audience rather than consumer localization. The layout vocabulary is dense-grid catalog rather than editorial magazine: product tiles lead with part numbers in an uppercase tracked weight, spec tables sit flush against hairline rules, and category navigation runs deep — photonics, optomechanics, spectroscopy, microscopy, quantum optics each forking into dozens of sub-paths. Because no hex palette was extractable from live extraction (the site hydrates tokens via JavaScript), color tokens below derive from widely-observed brand knowledge: a deep-navy header that reads close to charcoal, an amber-orange primary action color consistent with Thorlabs' visible identity across marketing and product pages, and a bright white catalog canvas. Rounded values skew minimal — `{rounded.xs}` appears throughout because nearly-square cards and rectangular buttons fit a brand whose audience trusts measurement precision over friendly radius. Spacing compresses in listing grids, where information density is a feature rather than a concession, and expands on product-detail pages where spec tables and dimensional drawings demand room to breathe.

colors:
  primary: "#e87722"
  primary-active: "#c9611a"
  primary-hover: "#d56b1d"
  primary-disabled: "#f4c49a"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d6d6d6"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-header: "#1c2b3a"
  on-primary: "#ffffff"
  on-header: "#ffffff"
  link: "#1b5ea8"
  link-hover: "#144a8a"
  success: "#2e7d32"
  success-surface: "#e8f5e9"
  warning: "#f5a623"
  part-number-ink: "#444444"

typography:
  display-xl:
    fontFamily: "'Ysabeau', 'Manrope', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Ysabeau', 'Manrope', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Manrope', 'Noto Sans JP', 'Noto Sans SC', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Manrope', 'Noto Sans JP', 'Noto Sans SC', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  part-number:
    fontFamily: "'Manrope', monospace"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  table-cell:
    fontFamily: "'Manrope', 'Noto Sans JP', 'Noto Sans SC', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  breadcrumb-text:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge-label:
    fontFamily: "'Manrope', sans-serif"
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
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 7px 14px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 9px 14px
    height: 40px
    focusBorder: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: "10px 48px 10px 16px"
    height: 44px
    submitButtonBackground: "{colors.primary}"
    submitButtonColor: "{colors.on-primary}"
    submitButtonRounded: "{rounded.none}"
  nav-bar:
    backgroundColor: "{colors.surface-header}"
    textColor: "{colors.on-header}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-top-strip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-header}"
    typography: "{typography.caption}"
    height: 32px
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.link}"
    linkHoverColor: "{colors.primary}"
    padding: "{spacing.xl}"
    shadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    partNumberTypography: "{typography.part-number}"
    partNumberColor: "{colors.muted}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    hoverBorder: "1.5px solid {colors.primary}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base}"
    hoverBorder: "1.5px solid {colors.primary}"
    hoverBackground: "{colors.canvas}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    headerColor: "{colors.muted}"
    cellTypography: "{typography.table-cell}"
    cellColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rowAlternateBackground: "{colors.surface-soft}"
    padding: "{spacing.sm} {spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.breadcrumb-text}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    linkColor: "{colors.link}"
    linkHoverColor: "{colors.primary}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-instock:
    backgroundColor: "{colors.success-surface}"
    textColor: "{colors.success}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-discontinued:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  hero-masthead:
    backgroundColor: "{colors.surface-header}"
    textColor: "{colors.on-header}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    height: 36px
    minWidth: 36px
  footer:
    backgroundColor: "{colors.surface-header}"
    textColor: "{colors.on-header}"
    linkColor: "#a0b4c8"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-header}"
    padding: "{spacing.xxl} 0"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    headingTypography: "{typography.title-sm}"
    labelTypography: "{typography.body-sm}"
    checkboxAccent: "{colors.primary}"
    rounded: "{rounded.none}"

## Components

### Buttons
**`button-primary`** — Amber-orange `{colors.primary}` rectangle with near-square `{rounded.xs}` corners, 40px tall, Manrope bold at 14px with slight letter-spacing. Hover darkens to `{colors.primary-hover}`, active press to `{colors.primary-active}`, disabled state washes to the pale `{colors.primary-disabled}` without size change. Used for catalog primary CTAs: "Add to Cart", "Request Quote", "Add to Favorites".

**`button-secondary`** — White canvas with a 1.5px amber-orange border and orange text, matching primary button geometry exactly. Signals an alternative action of equal legitimacy — common on product-detail pages where both "Add to Cart" and "Download Datasheet" must coexist without hierarchy confusion.

**`button-ghost`** — Transparent with a 1px `{colors.hairline}` border, body-colored text, `{typography.button-sm}`, 36px height. Used for low-stakes actions — "Compare", "Share", "Clear Filters" — where visual weight must stay subordinate to primary actions nearby.

### Search Bar
**`search-bar`** — The visual anchor of the entire site. Runs nearly full-width on desktop at 44px height, with a 2px `{colors.primary}` orange border that distinguishes it immediately as the primary interaction surface. The attached submit button fills solid orange and uses `{rounded.none}` so it reads as fused with the input — a single compound control rather than two adjacent elements. Placeholder text uses `{colors.muted}` at `{typography.body-md}`. Part-number lookup is the dominant use case; the border weight conveys that this is the fastest path through the catalog.

### Navigation
**`nav-bar`** — Deep-navy `{colors.surface-header}` bar at 56px with white Manrope `{typography.nav-link}` labels. Above it, `nav-top-strip` in near-black `{colors.ink}` at 32px carries account, region selector, and currency links in `{typography.caption}`. The two-tier arrangement separates utility navigation from product navigation without requiring a visible dividing line — the contrast delta between near-black and deep-navy provides the visual break. `nav-mega-menu` drops below the nav bar as a wide white panel with a subtle shadow, organized into heading-grouped link columns; link hover color shifts to `{colors.primary}` orange as the only hover feedback.

### Product Card
**`product-card`** — Bordered rectangle with `{rounded.xs}` corners and a 1px `{colors.hairline}` edge. Part numbers sit above the product title in `{typography.part-number}` — uppercase, tracked, semi-monospace weight — because engineers recognize the SKU before they read the description. Image well uses `{colors.surface-soft}` background to cleanly float white-background instrument photos. On hover the border intensifies to 1.5px `{colors.primary}` orange; no shadow lift is used, keeping the aesthetic closer to a reference catalog than a consumer shop.

### Category Tile
**`category-tile`** — Soft-surface fill with a hairline border that sharpens to an orange `{colors.primary}` 1.5px border and lifts to `{colors.canvas}` background on hover. Title uses `{typography.title-sm}`. These tiles form the primary navigation surface below the main nav bar — photonics, optomechanics, imaging, fiber optics, spectroscopy each occupying a tile in a dense uniform grid. Icon presence assumed but glyph set undocumented.

### Spec Table
**`spec-table`** — The workhorse component for product pages. Alternating rows with `{colors.surface-soft}` on odd rows. Column headers render in `{typography.spec-label}` — 11px uppercase Manrope at 0.4px tracking — in `{colors.muted}`. Data cells use `{typography.table-cell}` in `{colors.body}`. Tables span the full content column; horizontal scrolling is preferred over truncation for wide spec matrices. Contains wavelength ranges, numerical apertures, coating specifications, damage thresholds, and dimensional data.

### Badges
**`badge-new`** — Orange `{colors.primary}` tag in `{typography.badge-label}`, uppercase, tight padding, `{rounded.xs}`. Appears at the top-left of product card images for newly released catalog items. **`badge-instock`** — `{colors.success-surface}` green-tinted background with `{colors.success}` text, confirming immediate stock availability — a critical procurement signal for lab buyers on timeline. **`badge-discontinued`** — Muted gray surface with `{colors.muted}` text; appears inline with part numbers on superseded SKUs.

### Hero Masthead
**`hero-masthead`** — Navy `{colors.surface-header}` section with `{typography.display-xl}` Ysabeau headline — one of the few places where Ysabeau's classical proportions surface at full scale, giving instrument-launch banners a weight of institutional seriousness rather than SaaS enthusiasm. Body copy uses `{typography.body-md}` Manrope in `{colors.on-header}`. Generous `{spacing.xxl}` vertical padding.

### Footer
**`footer`** — Matches the header's `{colors.surface-header}` navy to bracket the page frame. Links render in `#a0b4c8` slate-blue rather than full white, reducing contrast fatigue across columns covering all product categories, regional offices, and compliance certifications. Heading labels use `{typography.title-sm}` in `{colors.on-header}`.

### Filter Sidebar
**`filter-sidebar`** — Left-rail white panel on category listing pages, bordered on the right with a 1px `{colors.hairline}` edge. Checkboxes use `{colors.primary}` orange as the check accent. Facets cover product family, wavelength range, material, coating, thread standard. No rounded corners — `{rounded.none}` throughout for catalog-register consistency.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger drawer nav; search bar full-width below header strip; spec tables scroll horizontally; breadcrumbs collapse to parent + current only; filter sidebar becomes bottom-sheet modal |
| Tablet | 744–1128px | 2-column product grid; nav condenses to icon+label strip with tap-to-open mega-menu; search bar prominent above fold; category tiles in 3-column grid |
| Desktop | 1128–1440px | 3–4 column product grid; full two-tier nav with hover mega-menus; left-sidebar filter panel on category pages; spec tables fixed-layout at full width |
| Wide | > 1440px | Max-width container (~1400px) centered with widening side margins; product grid stays at 4 columns; no additional density added |

### Touch Targets
- All buttons minimum 40px height; primary CTA bumps to 44px on mobile
- Search submit button maintains full 44px tap-height on mobile
- Product card entire surface is tappable on mobile viewport
- Nav drawer items minimum 44px vertical tap zone
- Pagination controls minimum 36×36px; active page control enlarged to 40×40px
- Filter checkboxes minimum 24×24px touch area with extended tap zone

### Collapsing Strategy
- Mega-menu category nav collapses to full-screen hamburger drawer on mobile and tablet
- Left-sidebar product filters move to bottom-sheet modal on mobile; modal persists filter state across open/close cycles
- Spec tables switch to horizontally-scrollable containers below 744px; column headers sticky on horizontal scroll
- `nav-top-strip` utility bar hides entirely on mobile; account icon migrates into hamburger drawer header
- Breadcrumbs truncate to "… / Parent Category / Current Page" on mobile to prevent wrapping
- Category tile grids reflow from 4-column (desktop) → 3-column (tablet) → 2-column (mobile)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extractable from the live site — the site hydrates design tokens via JavaScript rendering, defeating static palette extraction. All color tokens above are approximated from widely observed Thorlabs brand knowledge (navy header, orange CTA, white catalog canvas) and must be validated against the live site or an internal style guide before production use.
- Exact primary orange hex unverified — `#e87722` is a close approximation; the documented brand value may differ by hue or saturation.
- Exact header navy hex unverified — `#1c2b3a` is estimated from visual lightness; the true value may lean more blue or more neutral.
- Ysabeau usage context unclear — present in the font stack but whether it appears only in hero/marketing contexts, also in editorial landing pages, or in print-download templates is undocumented here.
- Custom icon set not captured — Thorlabs uses technical schematic-style category icons; stroke weight, grid size, and glyph library are undocumented.
- Stock-status variants beyond "New" and "In Stock" (e.g., "Discontinued", "Backorder", "Custom / Quote Required", "Export Controlled") not fully enumerated.
- Mega-menu column layout depth, max columns, and overflow behavior not documented.
- Dark-mode or high-contrast accessibility stylesheet presence unknown.
- Pricing display conventions (volume pricing tiers, currency-switch behavior, logged-in vs. guest price visibility) not captured.
