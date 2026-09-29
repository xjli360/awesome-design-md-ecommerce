---
version: alpha
name: "Pro-Ject Audio Systems"
source_url: "https://project-audio.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Forty-three years of platter-spin distilled into a single navy voltage — #003388 appears on every call-to-action, structural rule, and product badge across the site, an anchor color so deeply saturated it reads as ink on the white canvas yet registers as unmistakably engineered rather than merely dark. Pro-Ject positions its turntables the way Vienna positions its watchmakers: heritage-forward and technically precise, with product photography shot against controlled neutral backgrounds that let machined aluminum tonearms and matte-lacquer plinths carry the page without lifestyle distraction. Type runs in Lato across all contexts, a geometric humanist that balances engineering credibility with approachability — display headlines set at heavy 700 weight signal catalog authority while specification tables drop to regular 14px, trusting the mechanical product to supply the premium signal. An electric violet (#720eec) surfaces rarely but deliberately as a secondary accent, cutting against the deep navy to mark awards, certifications, and promotional callouts without softening the overall palette toward consumer-lifestyle warmth. Near-black #0a0a0a grounds the hero sections, letting turntable imagery sink into darkness the way a listening room should — intimate, directional, free of distraction. Gray #949494 handles metadata, secondary copy, and breadcrumbs, providing mid-range contrast between the white canvas and near-black ink without any warm or cool cast. The structural vocabulary stays angular throughout: buttons and cards carry no radius or a minimal 2px, reinforcing the machined-component precision of the product line. No pill shapes, no warm curves, no soft containers. The grid is dense with model numbers, specifications, and comparative tables, reflecting a customer base that researches cartridge tracking force, platter mass, and signal-to-noise ratios before adding to cart. Section headings arrive with a 3px solid #003388 underline rule — a detail that echoes engineering diagram tolerance markings — and the footer retreats into near-black #0a0a0a with muted gray links, maintaining the listening-room atmosphere that characterizes the brand's identity end to end.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#99aacc"
  accent-violet: "#720eec"
  accent-violet-muted: "#9b59e6"
  ink: "#0a0a0a"
  body: "#444444"
  muted: "#949494"
  charcoal: "#32373c"
  hairline: "#d0d0d0"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  surface-dark: "#1e1f26"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#dd1717"
  warning: "#ff9900"

typography:
  display-xl:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 38px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-label:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 10px
  xl: 16px
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
    padding: 12px 28px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.primary}"
    padding: 10px 26px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.on-dark}"
    padding: 10px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 16px
    height: 44px
    focusBorder: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 36px
    linkHoverColor: "{colors.primary}"
  nav-bar-mobile:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-label}"
    height: 56px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 16px
    imageAspectRatio: "1:1"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    hoverBorder: "1px solid {colors.primary}"
  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 540px
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    padding: 64px 0
  category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  spec-table:
    backgroundColor: "{colors.canvas}"
    labelColor: "{colors.charcoal}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    rowBorder: "1px solid {colors.surface-soft}"
    alternatingRowBackground: "{colors.surface-soft}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.title-sm}"
  award-badge:
    backgroundColor: "{colors.accent-violet}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkColor: "{colors.surface-soft}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    padding: 48px 0
    borderTop: "3px solid {colors.primary}"
  section-heading:
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    borderBottom: "3px solid {colors.primary}"
    paddingBottom: 8px
    marginBottom: 32px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.muted}"
  model-number-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.charcoal}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  product-filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.spec-label}"
    border: "1px solid {colors.hairline}"
    activeAccent: "{colors.primary}"
    checkboxColor: "{colors.primary}"
  series-navigation-tab:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 10px 20px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    focusBorder: "1px solid {colors.primary}"
    height: 44px

## Components

### Buttons

**`button-primary`** — Solid #003388 navy, uppercase Lato 700 with 0.6px letter-spacing, no border radius. Height 44px with 12px/28px padding. Hover darkens to `{colors.primary-active}` (#002266); disabled state uses washed-out #99aacc. The all-caps uppercase treatment reinforces the engineering catalog aesthetic rather than the conversational lowercase of lifestyle brands.

**`button-secondary`** — White fill with a 2px #003388 border and matching navy text. Mirrors primary dimensions exactly so paired CTA rows — "Buy Now" alongside "Find a Dealer" — sit at identical heights with clear hierarchy through fill vs. outline contrast.

**`button-ghost`** — Transparent with a 1px white border for use over the `{colors.surface-dark}` hero. Same uppercase Lato 700 treatment, ensuring hero CTAs read against dark photography without requiring a filled colored block.

### Text Input & Search

**`text-input`** — White background with 1px `{colors.hairline}` border, 2px `{rounded.xs}` radius — barely curved, consistent with the squared-off visual language. Focus ring upgrades to a 2px solid `{colors.primary}` navy. Used across contact forms, dealer finders, and checkout fields.

**`search-bar`** — Light `{colors.surface-soft}` fill replacing the white of text-input, making it visually distinct as a navigation element. Magnifier icon in `{colors.muted}` gray. Appears in the top nav on desktop and expands to full-width on mobile.

### Navigation

**`nav-bar`** — 64px white bar with a 1px `{colors.hairline}` bottom border. Logo at 36px height on the left; navigation labels in uppercase-tracking Lato 700 14px across the center; cart, search, and account icons right-aligned. Link hover color shifts to `{colors.primary}` navy without underline.

**`nav-bar-mobile`** — Near-black #0a0a0a bar at 56px, reversing the desktop treatment. White navigation labels and icon buttons. A hamburger triggers a full-screen overlay drawer.

**`series-navigation-tab`** — Horizontal tab row used within product family pages (e.g., Debut Carbon series variants). Inactive tabs: `{colors.surface-soft}` fill, `{colors.body}` text, uppercase button-sm. Active tab flips to solid `{colors.primary}` navy with white text — a hard switch rather than an underline indicator, keeping the mechanical aesthetic.

### Product Card

**`product-card`** — Zero-radius, 1px `{colors.hairline}` border. Product image on `{colors.surface-soft}` background at 1:1 aspect ratio. Title in `{typography.title-sm}`, price in `{typography.price-display}` 24px/700, secondary meta in `{typography.body-sm}` muted gray. Hover state upgrades the border to `{colors.primary}` navy — a single navy edge appearing on hover reinforces the primary color's function as the interactive signal.

### Hero

**`hero-section`** — Full-width dark-field section using `{colors.surface-dark}` (#1e1f26), minimum 540px height. Headline in `{typography.display-xl}` 38px/700, subline in `{typography.body-md}` white. Primary CTA button sits on dark, using the ghost variant or standard primary. Designed to frame product photography with near-zero ambient light.

### Badges & Tags

**`category-badge`** — Solid `{colors.primary}` navy fill, white `{typography.spec-label}` uppercase text, no radius, 3px/8px padding. Used on product listing cards to identify product line (e.g., "TURNTABLE", "PHONO STAGE").

**`award-badge`** — Electric violet `{colors.accent-violet}` (#720eec) fill with white spec-label text. Appears on product cards or detail pages to surface industry awards (EISA, What Hi-Fi) without interfering with the primary navy hierarchy. Zero radius.

**`model-number-tag`** — `{colors.surface-soft}` pill-less rectangle with `{colors.charcoal}` uppercase spec-label text. Surfaced beneath product names on listing pages to distinguish SKU variants (e.g., "DC / 2M RED").

### Specification Table

**`spec-table`** — Full-width table with `{typography.spec-label}` uppercase column headers on `{colors.surface-soft}` background and `{typography.body-sm}` row values on white. Row borders in `{colors.surface-soft}`, alternating rows with `{colors.surface-soft}` fill. The table is the primary differentiator on product detail pages — motor type, platter material, output voltage — and receives equal visual weight to the product imagery.

### Section Heading

**`section-heading`** — `{typography.display-md}` with a 3px solid `{colors.primary}` bottom border rule and 8px padding-below. Used to open catalog sections ("Turntables", "Phono Pre-amplifiers", "Accessories"). The thick underline rule echoes engineering specification diagrams and functions as a section delimiter without requiring a full horizontal rule.

### Footer

**`footer`** — Near-black `{colors.ink}` (#0a0a0a) background anchoring the page. Column headings in `{typography.title-sm}` white; link text in `{typography.body-sm}` `{colors.muted}` gray that lifts to white on hover. A 3px `{colors.primary}` navy rule at the top of the footer bridges the body-to-footer transition. Social icons, distributor finder link, and the "Handmade in Europe" wordmark appear in the bottom sub-row.

### Product Filter Sidebar

**`product-filter-sidebar`** — White background with `{typography.spec-label}` uppercase category headings and `{typography.body-sm}` filter options. Custom checkboxes fill with `{colors.primary}` navy on selection. Spec-label treatment on filter headings ("PRICE RANGE", "DRIVE TYPE") maintains the catalog-document register across browse and search views.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav over `{colors.ink}` bar; hero headline drops to `{typography.display-sm}` 22px; spec tables scroll horizontally; filter sidebar becomes a bottom sheet modal |
| Tablet | 744–1128px | Two-column product grid; nav collapses non-primary links into an overflow menu; hero maintains dark-field treatment at reduced height (~420px) |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with all series links visible; filter sidebar renders persistently left of product grid |
| Wide | > 1440px | Max-width container (~1400px) centered; hero images extend edge-to-edge behind a constrained text column; spec tables expand to show additional comparison columns |

### Touch Targets

- All primary and secondary buttons maintain 44px minimum height on mobile
- Product cards expand tap area to the full card surface, not just the title or image
- Navigation tab row items minimum 44px height with 16px horizontal padding
- Filter checkboxes padded to 44×44px invisible tap targets even when the visible indicator is smaller
- Cart and account nav icons maintain 44×44px touch area in the mobile bar

### Collapsing Strategy

- Primary nav: all product-series links ("Turntables", "Phono Stages", "Cables") collapse into a hamburger at < 1128px; the navy logo and cart/search icons remain in a persistent 56px black bar
- Series navigation tabs: horizontal scroll at < 744px rather than wrapping to multiple rows, preserving the single-row tab-bar aesthetic
- Spec table: horizontal scroll container below 744px with sticky first column (parameter label) so the model name stays visible while scrolling across variant columns
- Product filter sidebar: hidden off-canvas at < 1128px, triggered by a "Filter & Sort" button that opens a bottom sheet with the same spec-label filter list
- Hero text: `{typography.display-xl}` at desktop scales to `{typography.display-sm}` at mobile; CTA buttons stack vertically below the subline at < 480px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Intermediate gray hairline (#d0d0d0) was interpolated — the extraction returned #949494 and #f0f0f0 with no value between them; the exact border color used on form inputs and product cards was not directly captured
- Many extracted colors (#5865f2 Discord, #0866ff Meta, #0d66c2 LinkedIn, #ea4434, #e94c89) are social-share widget colors injected by third-party scripts, not brand tokens; they were excluded from the palette
- Exact button radius was not extractable — the site may use 0px or 2px; the zero-radius interpretation is based on the brand's engineering aesthetic and European catalog conventions
- Font weights above 700 and the full Lato weight stack were not confirmed; the brand may use Lato Black (900) for large display treatments
- Accent violet (#720eec) usage context is uncertain — it may be limited to a specific promotional page or award-display component rather than a system-wide accent token
- No custom icon font details available for `asppsicons2`; icon sizing and color behavior on interactive states were not captured
- Dark mode or night-mode variant could not be confirmed; `surface-dark` (#1e1f26) usage may be restricted to hero sections rather than a full dark theme
