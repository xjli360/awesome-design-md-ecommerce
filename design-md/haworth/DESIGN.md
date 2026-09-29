---
version: alpha
name: "Haworth"
source_url: "https://store.haworth.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The warm unbleached ground — #f2efde sitting beneath product photography and content blocks — is Haworth's quiet declaration that contract furniture doesn't have to feel like a procurement portal. Against this cream, deep navy (#001d34) and a forest-floor teal (#108474) operate as the two load-bearing poles of the palette: navy for structure, authority, and the footer mass; teal for every primary CTA, active state, and interactive anchor. The rust tertiary (#963928) surfaces sparingly on sale badges and promotional callouts — warm enough to signal urgency without tipping into clearance-rack aggression. The teal family itself is precise and internally coherent: #108474 primary, #0e4840 as the dark active press state, #aadddd as the washed-out disabled tone, and a cooled blue-green #65717b appearing in body borders — the brand keeps teal reserved for action signals and never dilutes it into decoration.

  Typography is where the tension lives. DM Serif Display at weight 400 is a strange choice for a B2B office furniture store — it reads closer to an architecture practice or high-end real estate developer than a task-chair specification sheet. Founders Grotesk carries the functional load: Medium at 14px for navigation labels and UI controls, Regular at 16px for prose, both shifting to all-caps at 0.5px tracking for button text. The serif/grotesque split generates a pairing that feels authored rather than defaulted — editorial authority in the headline register, specification-sheet clarity everywhere below it.

  Geometry is resolutely angular. `{rounded.none}` runs through every button, input field, and product card; the single exception is the color-swatch selector, which uses `{rounded.full}` circles — deliberate punctuation against otherwise hard corners that makes the swatches read like jeweler's dots rather than UI affordances. Hero sections alternate between two grounds: the navy (`{colors.navy}`) version for primary campaigns and the warm cream (`{colors.surface-soft}`) for workspace lifestyle photography, both pulling the same DM Serif Display headline at 56px. The blues — #004a78, #007ab4, #0579af — appear to serve informational link and availability states, keeping the teal palette reserved for primary interaction.

colors:
  primary: "#108474"
  primary-active: "#0e4840"
  primary-disabled: "#aadddd"
  navy: "#001d34"
  rust: "#963928"
  rust-dark: "#9f2828"
  ink: "#001d34"
  body: "#323232"
  muted: "#767676"
  muted-soft: "#888888"
  hairline: "#d9dde1"
  hairline-soft: "#e6e7e8"
  canvas: "#f9fafb"
  surface-soft: "#f2efde"
  surface-card: "#ffffff"
  surface-gray: "#f2f3f3"
  warm-blush: "#f4e8df"
  on-primary: "#ffffff"
  on-navy: "#f2efde"
  link: "#004a78"
  link-hover: "#007ab4"
  info-blue: "#0579af"
  success-green: "#2b7005"

typography:
  display-xl:
    fontFamily: "'DM Serif Display', Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'DM Serif Display', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'DM Serif Display', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Founders Grotesk Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Founders Grotesk Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.6px
    textTransform: uppercase
  body-md:
    fontFamily: "'Founders Grotesk Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Founders Grotesk Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Founders Grotesk Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Founders Grotesk Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Founders Grotesk Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Founders Grotesk Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'Founders Grotesk Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Founders Grotesk Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.navy}"
    padding: 12px 30px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: none
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.navy}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    comparePriceTypography: "{typography.price-compare}"
    captionTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    imageBg: "{colors.surface-gray}"
    padding: "{spacing.base}"
    badgePosition: top-left
  hero-section:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: button-primary
    minHeight: 560px
    padding: "64px 48px"
  hero-warm:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: button-secondary
    minHeight: 480px
  product-badge-sale:
    backgroundColor: "{colors.rust}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-badge-new:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.surface-gray}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: "0 16px"
    iconColor: "{colors.muted}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    gap: "{spacing.sm}"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.ink}"
    hoverBorder: "2px solid {colors.muted}"
    gap: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    linkColor: "{colors.on-navy}"
    linkHoverColor: "{colors.primary-disabled}"
    padding: "64px 0"
  category-filter-tab:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "2px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: "10px 0"
  section-divider:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xxl}"
  availability-badge:
    inStockColor: "{colors.success-green}"
    outOfStockColor: "{colors.rust}"
    typography: "{typography.caption}"
  review-summary:
    starColor: "{colors.navy}"
    countTypography: "{typography.caption}"
    scoreTypography: "{typography.title-md}"

## Components

### Buttons
**`button-primary`** — Solid teal (#108474) fill, all-caps Founders Grotesk Medium at 15px with 0.5px tracking, sharp corners (`{rounded.none}`), 48px tall, 32px horizontal padding. Hover darkens to `{colors.primary-active}` (#0e4840) with no geometry change — the color shift alone carries the interaction signal. Disabled washes to `{colors.primary-disabled}` (#aadddd) with white text.

**`button-secondary`** — 2px navy (`{colors.navy}`) border, transparent fill, same all-caps typographic treatment as primary. Hover inverts: navy background fills in, text shifts to warm cream (`{colors.on-navy}`). This inversion avoids introducing a fourth accent while clearly signaling engagement.

**`button-ghost`** — Inline text-only button in `{colors.primary}` teal, zero padding, no border. Used for "view all," "learn more," and inline navigational actions within content blocks. Underline appears on hover.

### Text Input
**`text-input`** — No radius (`{rounded.none}`), 1px `{colors.hairline}` border on a near-white `{colors.canvas}` background, 48px tall. Focus ring upgrades the border to 1px `{colors.primary}` teal. Founders Grotesk Regular via `{typography.body-md}`. All form fields — search, filter, checkout — share this sharp, spec-sheet aesthetic.

### Navigation
**`nav-bar`** — 72px tall on white canvas, deep navy logo mark, `{typography.nav-link}` for category labels (Founders Grotesk Medium, 14px). Cart, search, and account icons sit flush right. A 1px `{colors.hairline}` separates the bar from page content. Mega-menu dropdowns inherit the white background and hairline borders — no shadows, no elevation, just a clean reveal.

### Product Card
**`product-card`** — Hard corners throughout, product image on `{colors.surface-gray}` (#f2f3f3) to separate it from the white card body. Title in `{typography.title-md}` (Founders Grotesk Medium, 18px), price in `{typography.price-display}` (20px), compare-at price in `{typography.price-compare}` with strikethrough. Badges (`product-badge-sale`, `product-badge-new`) sit flush to the image top-left corner. Hover lifts the card with a subtle drop shadow — geometry never shifts.

### Hero
**`hero-section`** — Navy (`{colors.navy}`) background, warm cream text (`{colors.on-navy}`), DM Serif Display at 56px weight 400 for the headline. The serif at that weight against deep navy reads like a manufacturer's catalog page rather than a consumer storefront — authority without stiffness. CTA uses `button-primary` (teal on navy is the brand's highest-contrast pairing).

**`hero-warm`** — Cream ground (`{colors.surface-soft}`, #f2efde), same DM Serif Display headline in navy ink. Used for lifestyle and workspace context photography. The secondary CTA shifts to `button-secondary` (navy outline) to stay legible on the light ground.

### Badges
**`product-badge-sale`** — Flat rust rectangle (`{colors.rust}` #963928), `{typography.button-sm}` all-caps, zero border-radius, 4px vertical padding. Stacks flush to the image corner with no drop shadow.

**`product-badge-new`** — Identical geometry in navy `{colors.navy}` with cream text `{colors.on-navy}`.

### Search
**`search-bar`** — Light gray fill (`{colors.surface-gray}`), hard-edged, 44px tall, magnifying glass icon prefixed at `{colors.muted}`. No pill shape — consistent with the brand's flat-corner language. On focus the border shifts to `{colors.primary}` teal.

### Breadcrumb
**`breadcrumb`** — `{typography.caption}` (12px Founders Grotesk Regular) in `{colors.muted}`, chevron separator in `{colors.hairline}`, current page in `{colors.ink}`. Single horizontal line sitting above the product title or page headline.

### Color Swatch
**`color-swatch`** — 24px circles (`{rounded.full}`), the only fully rounded element in the interface. Selected state gets a 2px `{colors.ink}` navy ring; hover uses a 2px `{colors.muted}` ring. The deliberate contrast with the otherwise sharp-cornered system makes the swatches feel like material samples, not UI toggles.

### Footer
**`footer`** — Full-width navy band (`{colors.navy}`), warm cream/white text, `{typography.body-sm}` for link lists, `{typography.title-sm}` (all-caps, 12px, 0.6px tracking) for column headings. Four-column layout on desktop. Link hover uses `{colors.primary-disabled}` (#aadddd) — a lightened teal that reads as subtle feedback without leaving the blue-green family.

### Category Filter
**`category-filter-tab`** — `{typography.title-sm}` tabs (all-caps Founders Grotesk Medium, 12px), inactive in `{colors.muted}`, active with `{colors.ink}` text and a 2px `{colors.primary}` bottom border underline. No background fill changes — contrast comes from the teal underline alone, keeping the filter bar visually quiet.

### Section Divider
**`section-divider`** — Full-width `{colors.surface-soft}` cream band used to break page rhythm between product grid sections. Headline in `{typography.display-md}` (DM Serif Display, 36px) in `{colors.ink}` navy. Generous `{spacing.section}` top and bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer with full-screen overlay; hero text drops to `{typography.display-md}` (36px); hero min-height reduces to 360px; horizontal category filter tabs scroll with overflow-x hidden scrollbar; footer single-column with accordion sections |
| Tablet | 744–1128px | Two-column product grid; nav retains logo and icon cluster, top-level categories in horizontal overflow with fade mask; filter panel as a dismissible sidebar drawer |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with hover-triggered mega-menu dropdowns; hero gains side-by-side layout with image right-filling its half |
| Wide | > 1440px | Max-width container 1440px centered with auto margins; four-column product grid; hero image uses object-fit cover on the right 50% |

### Touch Targets
- All buttons minimum 48px tall per `button-primary` and `text-input` spec
- Color swatches render 24px visually but carry 32px tap area via transparent padding on mobile
- Hamburger and icon buttons minimum 44×44px tap surface
- Product cards are full-card tappable — no nested interactive child conflicts
- Filter toggles and accordion triggers minimum 48px tall on mobile

### Collapsing Strategy
- Desktop mega-menu nav collapses to a full-screen hamburger drawer on mobile; category hierarchy flattens to a single-level accordion
- Left-sidebar filter panel (desktop) moves to a bottom sheet on mobile, triggered by a sticky "Filter & Sort" bar at the bottom of the viewport
- Hero layout stacks headline → CTA → image vertically on mobile; image pushes below the fold on small viewports
- Breadcrumb hidden on mobile; a back-chevron button replaces it to conserve vertical space
- Footer columns collapse to accordion-gated sections on mobile, with the Haworth logo and legal row pinned at the bottom

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed border-radius value extracted from live site — `{rounded.none}` assumed throughout based on the angular visual language; a small xs or sm radius on cards is possible
- Distinction between `{colors.rust}` (#963928) and `{colors.rust-dark}` (#9f2828) functional roles unconfirmed — likely sale badge vs. error/warning states respectively
- Blue variants (#004a78, #007ab4, #0579af, #0e4840) purpose is inferred as informational links and availability states; no explicit semantic mapping extracted
- Exact CSS font-weight integers for Founders Grotesk Medium and Regular not confirmed — 500 and 400 assumed as standard mappings
- No dark mode tokens detected; whether dark-ground hero blocks constitute a partial dark mode or are strictly editorial components is unconfirmed
- Modal, overlay, and drawer scrim color not extracted
- Hover and focus ring treatment for product cards not extracted — box-shadow inferred from convention
- `JudgemeStar` is a Judge.me review widget icon font; star fill color and rating display exact spec not extractable from the brand palette alone
- Spacing scale for mega-menu dropdown internal layout not confirmed
- `{colors.warm-blush}` (#f4e8df) use case not confirmed — possibly used in promotional or lifestyle content sections
